# Content Models

A content model answers one question: **what counts as an admissible,
page-worthy unit in this book, and what page type captures it?** Everything
else — fidelity discipline, page ownership, Obsidian conventions, the
Inspect/Pilot/Ingest/Update/Verify workflow, agent-managed regions — is
shared across every model and lives in the other `references/` files, not
here.

Math proof-and-theorem structure does not transfer to a programming
textbook's concept-plus-worked-code-case structure, or to a primary-source
reader's document-entry structure, or to a narrative reading's
plot/character/theme structure. Forcing one book's units into another
model's template produces either empty sections or fabricated structure —
both violate the fidelity rules in `../workflow.md`.

## Available models

| Model | File | Typical book |
|---|---|---|
| Math | `math.md` | proof-based mathematics (analysis, algebra, topology) |
| CS | `cs.md` | programming/CS textbooks organized around language concepts and worked code examples |
| Primary-source reader | `primary-source-reader.md` | an edited anthology of historical/primary documents, each with its own citation and editorial headnote |

**Not yet built: narrative reading** (a novel, memoir, or other
sustained-narrative text assigned as course reading — e.g. a historical
novel mixing fact and fiction). Confirmed in scope, not yet designed.
Likely units: chapter-by-chapter plot/character/theme summary, with an
explicit fact-vs-fiction distinction where the book blends real history
with invented characters or scenes, and links to the historical events it
dramatizes. Do not improvise this one from the table above if it comes up
— report the mismatch to the user and treat it as a real "Adding a new
model" task (below), not an on-the-fly stretch of `primary-source-reader.md`
or any other existing file.

Not every book fits an existing model, including ones not listed above at
all. If a book's actual structure doesn't match any file here, say so
during Inspect rather than forcing the nearest model — report the mismatch
and ask before inventing a new model on the spot. Building a genuinely new
content model is a deliberate step (see "Adding a new model" below), not
something to improvise mid-Ingest.

## Selecting a model (Inspect mode)

1. Read the book's actual table of contents and a representative spread of
   pages — not the filename, not the course name. A "CS textbook" filename
   proves nothing if the actual pages are a primary-source anthology
   assigned in a CS-adjacent ethics course.
2. Look for the tell — each model file's own "Signals" section below lists
   what to look for. Match on structure, not subject label: a math-adjacent
   CS-theory book that's genuinely definition/theorem/proof organized is
   the *math* model even though the course is "CS."
3. **State the detected model and the specific evidence for it, then ask
   the user to confirm before starting Ingest.** Misdetection is cheap to
   fix at this point and expensive after several chapters are already
   built on the wrong template.
4. Record the confirmed model in the book's own working notes (e.g. a line
   in the course's MOC once created) so a later session doesn't have to
   re-detect it from scratch.

## What every content-model file must define

Each `content-models/<name>.md` file owns:

- **Signals** — concrete structural tells that identify a book as this
  model, for the detection step above.
- **Admitted unit types** — the page-worthy units this model recognizes
  (math: concept/proof; CS: concept/case-study; primary-source reader:
  document-entry), each with an admission test as rigorous as math's
  two-condition test in `math.md` — admission must never be "a phrase
  occurred," it must be a structural signal actually present in the book.
- **Compression policy** — what to preserve in full vs. compress vs. omit.
  This varies more than anything else across models: math omits routine
  examples on principle, CS *keeps* worked case studies in full because
  they're often the actual teaching mechanism, a primary-source reader
  keeps editorial headnotes in full but quotes the primary text sparingly
  (copyright, not pedagogy, is the constraint there).
- **Page types and their templates** — which files in `../../templates/`
  this model uses, and any fields specific to it.
- **Chapter-summary shape** — this model's variant lives at
  `templates/<name>/章节摘要-template.md`; only `templates/MOC-template.md`
  and `templates/概念-template.md` (see below) are shared across models
  as-is.

## Shared vs. model-specific templates

- `templates/MOC-template.md` — shared. Every model's MOC counts chapters
  and its own unit types.
- `templates/概念-template.md` — shared. "Concept" (a reusable object,
  property, structure, construction, process, or notation) shows up in
  math and CS alike, with the same shape: definition, notation, role,
  key properties, relations, labeled Agent-expansion section. A model that
  doesn't use concepts at all (a primary-source reader has no reusable
  "concepts" in this sense) simply doesn't create any.
- `templates/<model>/...` — everything model-specific: math's
  `证明-template.md`, CS's `案例-template.md` and its own
  `章节摘要-template.md`, the primary-source reader's
  `文献条目-template.md`.

## Adding a new model

Only do this when a real book doesn't fit any existing model — not
speculatively. Write the new `content-models/<name>.md` covering every
bullet in "What every content-model file must define" above, add any new
templates it needs under `templates/<name>/`, add its page type(s) to
`ALLOWED_TYPES` in `../../scripts/validate_wiki.py`, and add a row to the
table above.
