---
name: ingest
description: Turn links, files or pasted material into vault notes the way this vault expects - verified source notes, durable concept notes, citations on every claim, links, index and manifest updates, style checks, small commits and a push. Use whenever the user says "ingest", "ingest this", "ingest these", or hands over sources to be written up in the knowledge vault.
---

# Ingest

"Ingest" means: the user has read (or wants recorded) the material they attached, and wants it written into the vault now, properly, without being walked through each step. Do every step below unless the user says otherwise. If the user only wants to discuss a source, they will discuss instead of saying "ingest"; then write nothing.

The vault is private. Its concept notes are also the raw material for the public AI safety site in `/Users/tsn/Documents/workspace/research-garden`, so write concept notes that someone other than the user could learn from. Never publish to the garden as part of an ingest.

## 1. Read every source in full, and record exact metadata

- Read the whole source, not a summary of it. Get: exact title, author(s) and their role, publication date, publisher, canonical URL, and today's date as `accessed`.
- If a field is not on the page, write "not stated". If you could not confirm something, write "not verified". Never guess a date, title or author.
- When a fetch is blocked (for example openai.com returns 403 to WebFetch), open the page in a browser tool and read the page text there. For Google Docs, the published (`/pub`) URL reads cleanly; cite the URL the user gave.
- A page that is only a course wrapper or reading list (a BlueDot lesson page, a syllabus) is not a source note. Record its readings and exercise prompts in the course tracker in `projects/`, and ingest the readings themselves.

## 2. Search the vault before writing

- Read `VAULT_INDEX.md` and `vault_manifest.json`. Grep `concepts/`, `sources/` and `projects/` for the source's key terms and authors.
- Prefer adding a section to an existing note over creating a near-duplicate. Create a new note only when no existing note is a good home.

## 3. Write one source note per source

- Route by type:

  | Source | Folder | Template |
  | --- | --- | --- |
  | Paper, preprint, technical report | `sources/papers/` | `templates/Paper Note.md` |
  | Essay, blog post, statement, news or lab post by someone else | `sources/articles/` | `templates/Source Note.md` |
  | YouTube video or podcast | `sources/youtube/` | `templates/Source Note.md` (cite timestamps) |
  | The user's own published blog posts | `sources/blogs/` | as already imported |
  | Course page | no source note; course tracker in `projects/` | |

- Name the file by the source's title (`Author - Title.md` for essays), and keep it stable.
- Report what the source says, in the author's order, with the section heading (or timestamp, or page) for each step. Keep the source's claims apart from interpretation: put the user-facing interpretation under its own heading, marked as interpretation.
- Quotations: short (a phrase or one sentence), exact, with the section they come from. Never reconstruct a text from many quotes. Notes may be promoted to a public site, so write as if they will be read by others.
- Set `status: read` (or `synthesized` once its ideas are in concept notes, which this skill does in step 4).

## 4. Pull durable ideas into concept notes

- A durable idea is one that would help many readers understand AI safety (or the note's field) a year from now: a mechanism, a distinction, an argument, a well-documented case.
- Skip passing details: course logistics ("this is unit 1"), sign-up prompts, who recommended what, release-note trivia, dated product names unless they are evidence for a claim.
- For each durable idea: add a section to the best existing concept note, or create an atomic concept note named after the idea (for example `concepts/Recursive Self-Improvement.md`). Atomic notes are the units that later become garden pages.
- Keep the AI safety route notes (`concepts/AI Safety - *.md`) as the study path, and link atomic notes from the relevant step.

## 5. Cite everything that came from a source

- Every source the user attached is cited at least in its own source note and in every concept note that uses it.
- Every factual claim taken from a source gets a footnote (`[^key]`) whose definition sits in `## Sources` at the end: `Author (YYYY, Month DD). *Title*. Publisher. URL`.
- Use the same footnote key for the same source across notes (for example `[^pachocki-alien]`).
- When a source reports something it did not witness (an incident, another lab's result), attribute it: "Pachocki says...", not a flat statement.
- Mark certainty next to each claim: established, debated, the author's view, or the user's own view.

## 6. Write in the vault's style

- Follow `templates/Note Style Guide.md`, which applies `.claude/skills/consumable-writing/SKILL.md`. Headings state the point, terms are defined at first use, each key idea gets an example, analogies say where they break.
- Run `python3 scripts/check_note_style.py <note>` on every new or changed note and fix all errors. Edits made through Bash skip the automatic hook, so run it by hand after them.
- Before committing, ask the `note-reviewer` agent to review each new or materially changed note, and fix what it finds.

## 7. Link it into the vault

- Source note -> the concept notes it fed, and the route step or project it belongs to.
- Concept notes -> back to the source notes, and back and forward along the AI safety route.
- If the source is a course reading: tick the lesson in the course tracker in `projects/` and list the reading under it with a link to the source note.
- If the user mentioned something worth remembering about how they study, update memory.

## 8. Update the index and manifest

- Add or update entries in `VAULT_INDEX.md` and `vault_manifest.json` for every created or materially changed note. Edit the manifest as text to keep its formatting; check that it still parses as JSON.

## 9. Commit in small steps, then push

- Typical order: source notes; concept notes; route, tracker and index updates. One coherent change per commit, with a message that says what and why.
- Push the current branch when done (per `AGENTS.md`). Do not push to the garden, and do not deploy.

## 10. Report back

Tell the user, briefly:

- files created and files updated, and why each changed;
- the two or three ideas most worth discussing, as questions;
- which concept notes look ready to become garden pages, and what they still need (never publish without being asked);
- anything you could not verify.
