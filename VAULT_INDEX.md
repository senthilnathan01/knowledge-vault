# Vault Index

## Inbox
- `inbox/` — temporary captures and notes that still need sorting
- `inbox/Inbox.md` — inbox guide for triage and routing

## Sources / YouTube
- `sources/youtube/` — detailed notes from YouTube videos and podcasts
- `sources/youtube/YouTube Sources.md` — YouTube source guide for capture and follow-up

## Sources / Articles
- `sources/articles/` — essays, statements and lab posts by others, one source note each
- `sources/articles/Jakub Pachocki - An Alien Mind.md` — OpenAI's chief scientist (Sept 2026): AI is grown, may soon drive its own development, chain-of-thought monitoring is weakening, scaling should meet mandated safety bars
- `sources/articles/Daniel Selsam - Personal Statement on AI Risk.md` — OpenAI researcher (Sept 2026): situational awareness is undermining evaluation, a two-premise case for catastrophe, the 2026 agent swarms, cognitive offloading

## Sources / Papers
- `sources/papers/` — private paper notes and reading evidence
- `sources/papers/Paper Sources.md` — paper intake, reading, and citation guide
- `sources/papers/_pdf/` — local-only downloaded PDFs; ignored by Git

## Sources / Blogs
- `sources/blogs/` — published blog articles imported as private Markdown source notes
- `sources/blogs/Blog Sources.md` — catalog of all imported articles with publication dates and original URLs

## Concepts
- `concepts/` — evergreen ideas, frameworks, and distilled learnings
- `concepts/Concepts.md` — concept guide for evergreen notes
- `concepts/AI Safety.md` — hub note and top-down learning route for AI safety
- `concepts/AI Safety - Foundations.md` — Step 1: the map, the accident/misuse/structural taxonomy, the core argument, and the major camps
- `concepts/AI Safety - Problem Framings.md` — Step 2: capability vs. alignment, outer/inner alignment, reward hacking, goal misgeneralization, goal vs value alignment, orthogonality and instrumental convergence
- `concepts/AI Safety - Risk by Capability Level.md` — Step 3: risk by capability tier — today's misuse/robustness, frontier misalignment signals (sleeper agents, alignment faking, scheming, evaluation awareness, the 2026 agent incidents), advanced-AI loss of control
- `concepts/Recursive Self-Improvement.md` — AI doing a growing share of AI research: the feedback loop, how far along it is, why it shrinks time for safety checks, and the steer-or-slow responses
- `concepts/Chain-of-Thought Monitoring.md` — reading a model's written reasoning to catch bad intent: why it works, why grading the reasoning teaches hiding, its limits, and why it is getting less reliable

## Thinking
- `thinking/` — my own questions, ideas and discussion conclusions; matters more than any single source note
- `thinking/Thinking.md` — guide: what goes in each list and when an entry becomes its own note
- `thinking/Open Questions.md` — running list of questions to work out, with where each came from and Claude's first take where offered
- `thinking/Ideas.md` — running list of things to try, build, write or connect

## Projects
- `projects/` — active project plans, execution notes, and product thinking
- `projects/Projects.md` — project guide for active work
- `projects/BlueDot AGI Strategy Course.md` — course tracker: curriculum, progress, each lesson's readings with links to their source notes, exercise answers
- `projects/Game Theory and Strategic Interaction.md` — project hub for game theory, strategic interaction, and related applications

## Templates
- `templates/` — reusable Obsidian templates
- `templates/Templates.md` — template guide
- `templates/Research Brief.md` — research question and scope
- `templates/Paper Note.md` — structured paper reading note
- `templates/Synthesis Note.md` — multi-source synthesis
- `templates/Publication Draft.md` — private staging note for public promotion
- `templates/Thinking Note.md` — a question or idea thought through: current answer, case for and against, what would change my mind
- `templates/Source Note.md` — source note for essays, statements, posts, videos and podcasts
- `templates/Note Style Guide.md` — how to write notes: consumable writing for a newcomer, linking notes into a map, certainty marking, footnote citations, and diagrams

## Workflow
- `.claude/skills/ingest/SKILL.md` — what "ingest" means: the full source-to-notes workflow
- `.claude/skills/consumable-writing/SKILL.md` — the consumable-writing skill the note style guide is built on
- `scripts/check_note_style.py` — checks notes against the style guide's mechanical rules; run by the git pre-commit hook (`.githooks/pre-commit`) and a Claude Code hook (`.claude/settings.json`)
- `.claude/agents/note-reviewer.md` — reviewer agent that runs the style guide's final check on a note before it is committed
- `RESEARCH_WORKFLOW.md` — end-to-end private research and public promotion workflow
