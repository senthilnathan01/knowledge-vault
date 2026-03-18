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
- YouTube or podcast source notes -> `sources/youtube/`
- Evergreen ideas and distilled knowledge -> `concepts/`
- Active plans, product ideas, and execution docs -> `projects/`

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