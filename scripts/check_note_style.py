#!/usr/bin/env python3
"""Check vault notes against the mechanical rules in templates/Note Style Guide.md.

A script can catch em dashes, curly quotes, AI-tell words, heavy bold, emoji
and generic headings, and footnotes used without a definition. It cannot tell
whether a heading states its point, a term is defined at first use, or a claim
says how sure it is. Those need a reader: see .claude/agents/note-reviewer.md.

Usage (from anywhere inside the vault):
  python3 scripts/check_note_style.py NOTE.md ...   check these notes
  python3 scripts/check_note_style.py --all         check every in-scope note
  python3 scripts/check_note_style.py --staged      check staged notes (git pre-commit hook)
  python3 scripts/check_note_style.py --hook        Claude Code PostToolUse hook (JSON on stdin)

Exit status: 0 when there are no errors (warnings are allowed), 1 when there are
errors. In --hook mode errors exit 2, which Claude Code shows to Claude.
"""
import json
import os
import re
import subprocess
import sys

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUIDE = "templates/Note Style Guide.md"

# Notes written in the vault's own voice. Blog sources are other people's
# articles; templates, social captions and root files follow other rules.
INCLUDE = ("concepts/", "projects/", "sources/", "books/", "thinking/")
EXCLUDE = ("sources/blogs/", "sources/papers/_pdf/")

MAX_BOLD_PER_SECTION = 4

AI_TELLS = [
    r"delv(?:e|es|ed|ing)", r"realms?", r"robust", r"comprehensive(?:ly)?",
    r"leverag(?:e|es|ed|ing)", r"pivotal", r"underscor(?:e|es|ed|ing)",
    r"seamless(?:ly)?", r"tapestry", r"testament to", r"deep[- ]dives?",
    r"unpack(?:s|ed|ing)?", r"intricate", r"holistic(?:ally)?", r"actionable",
    r"landscape",
]
EMPTY_PHRASES = [
    r"only time will tell", r"experts (?:believe|agree|say)", r"studies (?:show|suggest)",
    r"it(?:'s| is) (?:important|worth) (?:to note|noting)", r"needless to say",
    r"hair on (?:your|the back of your) neck", r"please internali[sz]e",
    r"if you remember (?:one|only one)", r"game[- ]changer", r"let'?s dive",
]
GENERIC_HEADINGS = {
    "overview", "introduction", "intro", "background", "summary", "results",
    "discussion", "conclusion", "conclusions", "notes", "details", "misc",
    "miscellaneous", "key points", "key takeaways", "takeaways", "what's next",
    "next steps", "thoughts", "context", "misc notes",
}
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿⬀-⯿]")
CURLY = re.compile("[“”‘’]")
FOOTNOTE_DEF = re.compile(r"^\[\^([^\]\s]+)\]:")
FOOTNOTE_REF = re.compile(r"\[\^([^\]\s]+)\](?!:)")
BOLD = re.compile(r"\*\*[^*\n]+\*\*|__[^_\n]+__")
TELL_RE = re.compile(r"\b(?:" + "|".join(AI_TELLS) + r")\b", re.I)
EMPTY_RE = re.compile(r"(?:" + "|".join(EMPTY_PHRASES) + r")", re.I)


def in_scope(rel):
    rel = rel.replace(os.sep, "/")
    return rel.endswith(".md") and rel.startswith(INCLUDE) and not rel.startswith(EXCLUDE)


def mask(line):
    """Blank out inline code, links and URLs so their text isn't checked as prose."""
    line = re.sub(r"`[^`]*`", " ", line)
    line = re.sub(r"\[\[[^\]]*\]\]", " ", line)
    line = re.sub(r"\]\([^)]*\)", "]", line)
    line = re.sub(r"https?://\S+", " ", line)
    return line


def check_text(text):
    """Return a list of (line_number, level, message) for one note."""
    problems = []
    lines = text.split("\n")
    in_front = bool(lines) and lines[0].strip() == "---"
    in_code = False
    in_sources = False
    section_bold = 0
    section_line = 0
    refs, defs = {}, {}

    def close_section():
        if section_bold > MAX_BOLD_PER_SECTION:
            problems.append((section_line, "warning",
                             f"{section_bold} bold spans in this section; bold only what a skimmer must catch "
                             f"(about {MAX_BOLD_PER_SECTION} at most)"))

    for i, raw in enumerate(lines, 1):
        if in_front:
            if i > 1 and raw.strip() == "---":
                in_front = False
            continue
        if raw.lstrip().startswith(("```", "~~~")):
            in_code = not in_code
            continue
        if in_code:
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", raw)
        if heading:
            close_section()
            section_bold, section_line = 0, i
            title = heading.group(2).strip()
            in_sources = title.lower() == "sources"
            if EMOJI.search(title):
                problems.append((i, "error", "emoji in a heading"))
            if len(heading.group(1)) > 1 and title.lower().rstrip(":") in GENERIC_HEADINGS:
                problems.append((i, "warning",
                                 f'heading "{title}" names a topic; state the section\'s point instead'))

        m = FOOTNOTE_DEF.match(raw)
        if m:
            defs.setdefault(m.group(1), i)
            continue
        prose = mask(raw)
        for ref in FOOTNOTE_REF.findall(prose):
            refs.setdefault(ref, i)
        if in_sources:
            continue  # citations keep their original titles and punctuation

        if "—" in prose:
            problems.append((i, "error", "em dash; use a comma, colon, period or parentheses"))
        if re.search(r"\s–\s|\s--\s", prose):
            problems.append((i, "warning", "spaced en dash or double hyphen used as a dash"))
        if CURLY.search(prose):
            problems.append((i, "error", "curly quotes; use straight quotes"))
        for word in sorted({w.lower() for w in TELL_RE.findall(prose)}):
            problems.append((i, "warning", f'AI-tell word "{word}"; say it plainly'))
        for phrase in sorted({p.lower() for p in EMPTY_RE.findall(prose)}):
            problems.append((i, "warning", f'"{phrase}": hype, an instruction to the reader, or an unsourced claim'))
        if not heading:
            section_bold += len(BOLD.findall(prose))
    close_section()

    for ref, line in refs.items():
        if ref not in defs:
            problems.append((line, "error", f"footnote [^{ref}] is used but never defined"))
    for ref, line in defs.items():
        if ref not in refs:
            problems.append((line, "warning", f"footnote [^{ref}] is defined but never used"))
    return sorted(problems)


def report(rel, problems, out):
    for line, level, message in problems:
        print(f"{rel}:{line}: {level}: {message}", file=out)


def git(*args):
    return subprocess.run(["git", "-C", VAULT, *args], capture_output=True, text=True, check=True).stdout


def run_files(rels):
    errors = warnings = 0
    for rel in rels:
        with open(os.path.join(VAULT, rel), encoding="utf-8") as f:
            problems = check_text(f.read())
        report(rel, problems, sys.stdout)
        errors += sum(p[1] == "error" for p in problems)
        warnings += sum(p[1] == "warning" for p in problems)
    print(f"{len(rels)} note(s) checked: {errors} error(s), {warnings} warning(s). Rules: {GUIDE}")
    return 1 if errors else 0


def run_staged():
    names = [n for n in git("diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z").split("\0") if n]
    errors = 0
    for rel in filter(in_scope, names):
        problems = check_text(git("show", f":{rel}"))
        report(rel, problems, sys.stderr)
        errors += sum(p[1] == "error" for p in problems)
    if errors:
        print(f"\nNote style check: {errors} error(s) in staged notes. Rules: {GUIDE}\n"
              "Fix them and stage again. To skip the check once: git commit --no-verify", file=sys.stderr)
        return 1
    return 0


def run_hook():
    try:
        payload = json.load(sys.stdin)
    except ValueError:
        return 0
    path = (payload.get("tool_input") or {}).get("file_path") or (payload.get("tool_response") or {}).get("filePath")
    if not path:
        return 0
    rel = os.path.relpath(os.path.realpath(path), os.path.realpath(VAULT))
    if rel.startswith("..") or not in_scope(rel) or not os.path.isfile(path):
        return 0
    with open(path, encoding="utf-8") as f:
        problems = check_text(f.read())
    if not problems:
        return 0
    lines = [f"{rel}:{line}: {level}: {message}" for line, level, message in problems]
    header = f"Note style check ({GUIDE}) found problems in {rel}:"
    if any(p[1] == "error" for p in problems):
        print("\n".join([header, *lines, "Fix the errors before committing; the pre-commit hook blocks them."]),
              file=sys.stderr)
        return 2
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": "\n".join([header, *lines, "These are warnings: fix them unless there is a good reason."]),
    }}))
    return 0


def main(argv):
    if argv == ["--hook"]:
        return run_hook()
    if argv == ["--staged"]:
        return run_staged()
    if argv == ["--all"]:
        rels = []
        for top in INCLUDE:
            for root, _, files in os.walk(os.path.join(VAULT, top)):
                rels += [os.path.relpath(os.path.join(root, f), VAULT) for f in files]
        return run_files(sorted(r for r in rels if in_scope(r)))
    if not argv or any(a.startswith("-") for a in argv):
        print(__doc__, file=sys.stderr)
        return 2
    rels = [os.path.relpath(os.path.abspath(a), VAULT) for a in argv]
    return run_files(rels)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
