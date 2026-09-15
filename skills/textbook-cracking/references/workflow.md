# Workflow

## 1. Establish the course boundary

Confirm the course directory, source PDF, textbook identity, requested chapter, output language, and whether an existing wiki must be updated. Default prose to Chinese while preserving official English titles, author names, formal labels, notation, and formulas/code as the source actually writes them.

Never infer that every file in `raw/` belongs to the textbook. Canvas announcements, syllabi, review guides, and ordinary assignments belong to CanvasManager.

Determine your wiki root before writing anything: if the course directory
already has `wiki/course_content/` or `wiki/info/` (a CanvasManager-managed
course), your root is `wiki/textbook_breakdown/`, not `wiki/` itself —
create that folder if this is the first textbook content synced for the
course. Otherwise `wiki/` is your root. See
`references/course-manager-integration.md`'s "Wiki root" for the full
rule; every `wiki/...` path elsewhere in this file means "under whichever
root applies here."

## 2. Inspect the source

Record:

- source path and stable content hash when available;
- title, edition, authors, and language;
- PDF page count;
- printed-page mapping using at least two verified points;
- table of contents structure;
- text-layer quality;
- scan, rotation, multi-column, formula, code-block, and image issues;
- **which content model fits** — per `content-models/README.md`'s detection procedure. State the match and the specific structural evidence, then get the user to confirm before Ingest.

For a constant offset, record the relation explicitly, for example `PDF page = printed page + 14`. Do not assume the offset remains constant across front matter, inserts, or appendices.

## 3. Run a representative pilot

Select pages containing a chapter heading, ordinary prose, and the selected model's admitted-unit types (math: a definition, a theorem, a proof; CS: a concept introduction, a worked case study; primary-source reader: a full document entry), plus dense formulas/code and any atypical layout. Read them directly with the Agent.

Pass when:

- reading order is correct;
- the model's admitted-unit boundaries are recoverable (theorem/proof; concept/case-study; document-entry — whichever the selected model uses);
- formulas or code are legible enough to verify;
- printed and PDF page references are stable.

If the pilot fails, check for already-installed local tools. Do not install or download anything without approval. Treat MinerU, Marker, Docling, OCRFlux, and similar systems as optional adapters, never required dependencies.

## 4. Read one full chapter

Read the full requested range before writing. Build an internal outline containing:

- section sequence;
- every unit the selected content model admits (see that model's file for the exact list — formal definitions/theorem labels/proof boundaries for math; concept introductions/case-study boundaries for CS; document entries and their citations for a primary-source reader);
- remarks, counterexamples, restrictions, or editorial framing that affects how a unit should be read;
- cross-references to earlier material.

Do not construct the chapter from search snippets or the table of contents alone.

## 5. Write the chapter summary

Copy the selected model's own `templates/<model>/章节摘要-template.md` and replace placeholders. Preserve the original section order. Include complete statements of what the chapter establishes, but replace full detail (proof bodies, case-study walkthroughs, document text) with links to that model's own detail pages.

Apply the selected model's compression policy (see that model's file) — what's routine filler versus load-bearing content is not the same call in every model.

## 6. Admit concepts conservatively

Only if the selected model uses concepts at all (a primary-source reader typically doesn't). Apply that model's admission test. Re-read an existing concept page before updating it. Add the textbook-grounded material to its managed core and place any teaching expansion in the labeled expansion section.

Do not create a concept page merely because a phrase occurs, a named result or worked case uses a technique, or an exercise references it.

## 7. Extract every other admitted unit the model defines

For every unit type the selected model owns beyond concepts (math: proofs; CS: case studies; primary-source reader: document entries):

1. Create one page from that model's own template (`templates/<model>/...`).
2. Reproduce the textbook's actual content faithfully, per that model's compression policy — full logical steps for a proof, a full working code listing plus walkthrough for a case study, editorial headnote in full plus sparing quotation for a document entry.
3. Preserve internal structure the textbook itself uses (direction/case splits for a proof; setup/output/explanation for a case study; source citation/date for a document).
4. Link prerequisites and the source chapter.
5. State accurately when the textbook omits, defers, or only partially supplies something — never fabricate the missing part.

Never add Agent-composed content to a section that's supposed to be the textbook's own. Optional explanation belongs under a labeled Agent expansion section.

## 8. Update the MOC

Maintain static Markdown indexes; do not require Dataview. Update totals, chapter status, concept entries, and entries for whichever other unit type(s) the selected model uses, plus unresolved verification items.

## 9. Verify before handoff

Check against the source:

- chapter and section titles;
- printed and PDF page references;
- the selected model's admitted-unit conditions (definition conditions for math; a case study's actual code/output for CS; a document's actual citation and text for a primary-source reader);
- every displayed formula or code block;
- every proof step / case-study walkthrough step / document excerpt, as applicable;
- the textbook's own notation or terminology;
- links among chapter, concept, and detail pages.

Use `verification: needs-review` whenever any substantive element is uncertain. List exact uncertainties in the page and final report.

## 10. Run structural validation

Run `scripts/validate_wiki.py`. Fix structural errors without changing source meaning. Report warnings that need human or source review.
