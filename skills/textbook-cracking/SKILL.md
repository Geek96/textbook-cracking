---
name: textbook-cracking
description: Deconstruct textbooks and textbook-like PDFs into a faithful, traceable Obsidian wiki. Use when the user wants to inspect or ingest a textbook, summarize chapters in the book's original order, create pages for textbook-emphasized concepts or reusable units, extract every formal proof or worked case the book supplies, build or update a textbook MOC, verify notation and source pages, or incrementally maintain an existing textbook wiki. Covers proof-based math/science textbooks, programming/CS textbooks built around concepts and worked code cases, and primary-source document readers — see references/content-models/ for the full list and how a book gets matched to one. Agent-first PDF reading, no required external API, subscription, MCP server, Dataview plugin, or document-parsing service.
---

# Textbook Cracking

Turn a textbook into a compact evidence-backed wiki without rewriting it as a new textbook. Preserve the author's structure, order, and the substance of what the book actually establishes. Omit exercises and routine filler by default — what counts as "filler" is content-model-specific, see below.

## Read the applicable rules

Before acting, read:

1. `references/workflow.md` for every ingestion or update.
2. `references/content-models/README.md` before classifying pages or creating files — it explains how a book is matched to a content model and what every model file must define, then read the selected model's own file (e.g. `references/content-models/math.md`).
3. `references/obsidian-core.md` before writing any Obsidian artifact.
4. `references/obsidian-rules.md` before writing Markdown. These domain rules take precedence over the Core when they are more specific; a content model's own rules take precedence over both when they are more specific still.
5. `references/course-manager-integration.md` when the source came from CanvasManager, the output will later feed CourseManager, or the course directory already has a CanvasManager layout (`wiki/course_content/`, `wiki/info/`) — that file also defines which `wiki/...` root applies before you write anything.

Read only the templates needed for the current operation — `templates/MOC-template.md` and `templates/概念-template.md` are shared across models; everything else lives under `templates/<model>/` (e.g. `templates/math/证明-template.md`, `templates/cs/案例-template.md`) — see the selected content model's file for its exact list.

## Protect boundaries

- Treat every source under `raw/` as immutable. Never rename, edit, move, or delete it.
- Write only `MOC.md`, `章节摘要/`, `概念/` (when the selected model uses concepts), and the selected model's own additional page-type folder(s) — see that model's file for the exact list (math: `证明/`, and `练习题/` when explicitly requested; CS: `案例/`, `周次/` when in use, and `选择题练习/`, `编程练习/` when explicitly requested; primary-source reader: `文献/`) — all relative to `wiki/`, or to `wiki/textbook_breakdown/` when the course directory has a CanvasManager layout; see `references/course-manager-integration.md`'s "Wiki root".
- Do not write `wiki/综合/` (or `wiki/info/` in a CanvasManager-managed course); reserve that for CourseManager/CanvasManager.
- Preserve all user-authored text outside matching `agent-managed` markers.
- Do not require or silently install external parsers, model weights, plugins, accounts, or API keys.
- Do not upload textbook content to another service unless the user explicitly requests and approves it.

## Select an operating mode

### Inspect

Use when the source is new or its quality is unknown. Identify:

- title, authors, edition, language, and discipline;
- table of contents and chapter boundaries;
- printed-page to PDF-page mapping;
- whether a usable text layer exists;
- formulas, code blocks, multi-column layouts, scans, figures, and other difficult pages;
- **which content model fits** — read `references/content-models/README.md`'s detection procedure, state the match and the specific structural evidence for it, and get the user to confirm before Ingest;
- a representative chapter range for a pilot.

Report findings before processing a large range.

### Pilot

Use before the first full chapter. Read representative pages directly with the current Agent. Verify headings, the selected model's admitted-unit boundaries (theorem/proof for math; concept/case-study for CS; document entries for a primary-source reader), formulas or code, and page mapping. Prefer the Agent-only path. Use an already-installed local parser only when direct reading demonstrably fails; ask before installing anything.

### Ingest

Process one requested chapter at a time:

1. Map its printed and PDF pages.
2. Read the full chapter, not isolated search hits.
3. Reconstruct the author's section order.
4. Create or update one chapter summary, using the selected model's own chapter-summary template.
5. Create concept pages only for concepts admitted by the selected content model's admission test (skip this step entirely for a model that doesn't use concepts).
6. Create one page per other admitted unit the model defines and the textbook actually supplies (math: one proof page per supplied proof; CS: one case-study page per worked case; primary-source reader: one document-entry page per included document).
7. Update `MOC.md`.
8. Run the validator and report unresolved source ambiguities.

### Update

Read existing pages before editing. Update only matching managed regions. Recompile indexes when templates or links change; do not re-read the PDF unnecessarily when the source and extracted facts have not changed.

### Verify

Check the selected model's admitted-unit conditions/steps, formulas or code, page references, wikilinks, frontmatter, and managed markers. Mark uncertainty explicitly. Never fill a missing proof, case detail, or document excerpt from memory and present it as the textbook's own content.

### Practice content generation — not this skill's job

Agent-original practice problems (math) and week-scoped MCQ/coding practice
(CS) are **not** generated by this skill, even though the math and CS
content models used to describe them — that work moved to the separate
[`course-manager`](https://github.com/Geek96/course-manager) skill as of
v0.2.0, because it's inherently course-scoped (reading a specific course's
syllabus or a professor's slide deck to ground the range and difficulty),
not textbook deconstruction. If a user asks for practice problems or week
practice here, point them at `course-manager` instead — it reads this
skill's `wiki/textbook_breakdown/` (concepts, proofs, case studies, and
Week pages) read-only to generate them, same as it reads canvas-manager's
evidence for deadline synthesis. See
`references/course-manager-integration.md`'s "Exercise handoff" section.

## Apply the fidelity rules

Preserve, regardless of model:

- the author's chapter and section order;
- every formally established definition, notation, or named unit the book itself sets apart from ordinary prose;
- remarks, counterexamples, restrictions, and caveats that affect validity or correctness;
- explicit optional or starred status.

What else to preserve in full vs. compress vs. omit is **content-model-specific** — see that model's own "Compression policy." They differ on purpose: math omits routine examples by principle, CS keeps worked case studies in full because they're often the actual teaching mechanism rather than repetition, a primary-source reader keeps editorial framing in full but quotes primary text sparingly for copyright reasons rather than pedagogical ones. Do not import one model's compression instinct into another's book.

Do not impose a mechanical word or percentage limit in any model. Compress by the density of what's actually being taught.

## Separate textbook content from Agent expansion

Keep chapter summaries and any page reproducing the textbook's own supplied content (a proof, a case-study walkthrough, a document excerpt) textbook-faithful. Concept pages may add intuition, equivalent viewpoints, or clarifying counterexamples only under a visibly labeled `## 🧠 理解扩展` section stating that the material is Agent-generated and not textbook prose.

## Publish the page types

- `MOC.md`: central navigation, counts, chapter index, concept index (if used), other unit-type index, and verification status.
- `章节摘要/`: chapter order, formal statements/summary of what the chapter establishes, remarks, and links to the model's own detail pages (proof/case-study/document-entry) rather than duplicating their content.
- `概念/`: only textbook-emphasized reusable units, when the model uses concepts at all.
- The model's own additional folder(s) (`证明/`, `案例/`, `文献/`, ...): one page per admitted unit the textbook actually supplies.

Keep summary-level statements in chapter summaries and full detail (a proof, a case walkthrough, a document's text) in the model's own detail pages. Concept pages may reference them but must not duplicate their full content.

## Validate

Run:

```bash
python3 scripts/validate_wiki.py /path/to/course/wiki
```

Treat validator success as structural evidence only. It does not prove that the reproduced content or page attribution is correct; perform source verification separately.
