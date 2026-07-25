# AGENTS.md

This repository is an Obsidian knowledge vault made of Markdown files.

## Primary rules
- Read `VAULT_INDEX.md` and `vault_manifest.json` before making changes.
- Prefer updating existing relevant notes instead of creating duplicates.
- Create new notes only when no existing note is a good destination.
- Preserve Markdown readability and Obsidian wikilinks.
- Keep note titles clear and stable.
- When adding, renaming, or materially changing notes, update both:
  - `VAULT_INDEX.md`
  - `vault_manifest.json`

## Folder routing
- Raw captures and temporary notes -> `inbox/`
- Papers and paper-specific reading notes -> `sources/papers/`
- Downloaded paper PDFs -> `sources/papers/_pdf/` (local-only and Git-ignored)
- YouTube or podcast source notes -> `sources/youtube/`
- Evergreen ideas and distilled knowledge -> `concepts/`
- Active plans, product ideas, and execution docs -> `projects/`
- Reusable Obsidian note templates -> `templates/`

## Research workflow
- Search the vault before creating a note, and link new work to existing concepts or projects.
- Prefer primary sources. Record a DOI or canonical URL whenever one exists.
- Use the lifecycle `unread` -> `reading` -> `read` -> `synthesized` -> `ready-to-publish` -> `published`.
- Keep source notes descriptive: distinguish what a source reports from interpretation or inference.
- Tie important claims to a page, section, figure, table, or quoted passage when the source permits it.
- Never invent citation metadata, evidence locations, results, or quotations. Mark unavailable details explicitly.
- Use the templates in `templates/` for research briefs, paper notes, syntheses, and publication drafts.

## Publishing to the research garden
- Treat this vault as private and `/Users/tsn/Documents/workspace/research-garden` as public.
- Promote by creating or updating a self-contained public page; never move or delete the originating vault notes.
- Before editing the garden, read its `AGENTS.md` and follow its publication gate.
- Do not copy private commentary, credentials, personal data, raw PDFs, copyrighted full text, or unsupported claims.
- A publication candidate must have `status: ready-to-publish`, resolved citation metadata, evidence for material claims, and a completed privacy review.
- After a garden page is published, update the originating vault publication draft with:
  - `status: published`
  - `garden_path`
  - `published_url`
  - `published_at`
- Add the public article to `published_in` on directly related paper or synthesis notes when useful.
- Do not commit, push, or deploy either repository unless the user explicitly requests it.

## For YouTube links
When given a YouTube link:
1. Create a detailed source note in `sources/youtube/`
2. Extract the main ideas, nuanced insights, and actionable points
3. Update any relevant existing notes in `concepts/` or `projects/`
4. Add links between the source note and related notes
5. Update `VAULT_INDEX.md`
6. Update `vault_manifest.json`

## Editing style
- Do not rewrite unrelated sections.
- Keep changes high-signal and organized.
- Prefer concise headings and bullets.
- Add a short `## Sources` section when a note comes from external material.

## Output expectation
After completing a task, summarize:
- files created
- files updated
- why each file was changed
