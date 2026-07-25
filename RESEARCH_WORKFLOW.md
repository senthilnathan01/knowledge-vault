---
type: workflow
status: active
visibility: private
---

# Research Workflow

Use this vault for the complete research record. Publish only refined, sourced, and publicly safe material to `/Users/tsn/Documents/workspace/research-garden`.

## Boundary

| Location | Purpose | May contain |
| --- | --- | --- |
| Knowledge vault | Private research workspace and provenance record | Raw captures, PDFs, incomplete reasoning, uncertainties, working notes, private context |
| Research garden | Public, self-contained output | Refined articles, verified citations, safe project pages, reproducible public evidence |

The public garden is a promotion target, not a mirror. Copy and rewrite selected ideas; do not move the private originals.

## Lifecycle

### 1. Brief

Start from [[templates/Research Brief|Research Brief]] and define:

- the research question;
- what evidence is in and out of scope;
- the intended output and audience;
- the stopping condition.

### 2. Collect

Create one note per paper from [[templates/Paper Note|Paper Note]].

- Prefer the publisher page, DOI, arXiv record, or another canonical primary source.
- Store downloaded PDFs under `sources/papers/_pdf/`. That folder is local-only and ignored by Git.
- Never infer missing bibliographic fields. Leave them blank and note what could not be verified.

### 3. Read

Move paper status through:

`unread` -> `reading` -> `read`

Capture the paper's claims, method, results, limitations, and evidence locations. Keep direct quotations short and include a page or section.

### 4. Synthesize

Use [[templates/Synthesis Note|Synthesis Note]] to compare sources rather than merely summarize them. Record:

- areas of agreement and disagreement;
- evidence quality and uncertainty;
- the conclusions that follow;
- open questions and useful next work.

Mark contributing paper notes `synthesized` when their relevant evidence has been integrated.

### 5. Prepare publication

Use [[templates/Publication Draft|Publication Draft]]. A candidate may move to `ready-to-publish` only when:

- every material factual claim has supporting evidence;
- citation metadata and external URLs are resolved;
- inference is clearly distinguished from source claims;
- no private commentary, personal data, secrets, local paths, or raw copyrighted material remains;
- the draft is self-contained for a reader who cannot access this vault.

### 6. Promote

Read the garden's `AGENTS.md`, then create or update:

`/Users/tsn/Documents/workspace/research-garden/content/projects/<project-slug>/<article-slug>.md`

Start public pages as `publication_status: draft` with `draft: true`. Change them to `published` and `draft: false` only after the garden validation, checks, and build succeed.

### 7. Record provenance

After publication, update the private publication draft:

```yaml
status: published
garden_path: content/projects/<project-slug>/<article-slug>.md
published_url: https://senthilnathan01.github.io/research-garden/projects/<project-slug>/<article-slug>
published_at: YYYY-MM-DD
```

Add the public URL to `published_in` on directly related paper and synthesis notes when useful. Public pages must not expose private vault paths or note names.

## Default Codex prompts

### Research

> Research [question] in the knowledge vault. Read `AGENTS.md`, `VAULT_INDEX.md`, and `vault_manifest.json` first. Search for existing related notes, prefer primary papers, create page- or section-level evidence, synthesize the findings, and do not edit the research garden.

### Publish

> Promote [vault publication draft] to [garden destination]. Treat the vault as private provenance and the garden as public output. Read both repositories' `AGENTS.md` files, preserve verified external citations, exclude private material and local paths, run the garden publication gate, check, and build, then record the public path and URL back in the vault. Do not commit, push, or deploy.

## Sources

- [[VAULT_INDEX|Vault Index]]
- [Research Garden](https://senthilnathan01.github.io/research-garden/)
