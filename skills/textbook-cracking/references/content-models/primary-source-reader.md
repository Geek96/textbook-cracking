# Content Model: Primary-Source Reader

For an edited anthology of primary documents — a documentary history
reader, a sourcebook — organized into era/theme chapters, each containing
numbered document entries with their own citation and editorial framing.
Selected during Inspect per `README.md` in this directory; read that file
first if you haven't.

## Signals

- Chapters correspond to historical eras or themes, not to a single
  author's expository argument.
- Within each chapter, a numbered list of discrete documents (a
  petition, a speech, a law, a letter, a testimony), each with its own
  title and date.
- Each document entry has a fixed shape: a "Source:" citation line, an
  editorial headnote giving context and explaining why it's included,
  the primary text itself (often excerpted, not printed in full), and
  frequently a "Questions" prompt at the end.
- No definitions/theorems/proofs, no code, no worked examples — the
  content *is* the documents themselves plus the editor's framing.

## Page types and templates

- `章节摘要/` — `templates/primary-source-reader/章节摘要-template.md`
- `概念/` — `templates/概念-template.md` (shared, optional — see "Theme
  admission" below; most chapters won't produce any)
- `文献/` — `templates/primary-source-reader/文献条目-template.md`

## Compression policy

Preserve in full:

- the editor's own headnote for every document — this is short, and it's
  the actual analytical value the reader adds beyond the raw document;
- the citation line (author, date, source archive/publication) — this is
  the traceability anchor for a primary source and must never be dropped
  or paraphrased away;
- the "Questions" prompt, if the book supplies one — it's a study aid the
  student will actually use.

Preserve sparingly, by deliberate policy rather than pedagogical judgment:

- **the primary document's own text.** Quote enough to convey the
  document's actual content and a few of its most load-bearing sentences
  — not a full reproduction. This constraint exists for a different
  reason than math's or CS's compression rules: it isn't about routine
  filler, it's that reproducing an entire historical document (which may
  itself carry its own copyright, translation, or the reader's editorial
  transcription rights, independent of the underlying historical event's
  public-domain status) at wiki scale is a different act than quoting a
  sentence from a math proof. Summarize the document's content
  accurately in your own words for anything beyond the load-bearing
  quotes, and always keep the citation so a reader can go find the full
  text themselves.

Omit or fold into the chapter summary:

- the anthology's own general front-matter essays *not* tied to a
  specific chapter (a general preface on method) — mention once in the
  book-level MOC, don't repeat per chapter;
- editorial footnotes that are purely bibliographic (an archive call
  number with no interpretive content) — keep in the citation line only.

## Document-entry sections

A document entry's shape, in order: `出处` → `背景` → `🎯 Core Information（核心信息）` → `📌 Main Points and Key Facts（主要观点与重要事实）` → `原文节选` → `👤 关键人物与术语` → `讨论问题` → `👨‍🏫 讲师笔记`（optional, see below）→ `🔗 相关文献` → `🧠 理解扩展` → `🔗 教材位置`. See `templates/primary-source-reader/文献条目-template.md` for the full per-section instructions.

- **🎯 Core Information（核心信息）** — a small fixed-dimension table (historical context / intended audience / purpose / author's standpoint) giving a reader the HIPP-style framing before they read the excerpt — where the document sits, who it was for, what it's trying to do, and whether the author has a stake in it. Agent synthesis grounded in the headnote and document, not the editor's own words.
- **📌 Main Points and Key Facts（主要观点与重要事实）** — an itemized extraction of the document's own main claims and the load-bearing facts a reader needs, replacing what used to be folded into prose summary. This is the section a student actually reviews before a discussion or exam; keep it a scannable list, not a restatement of 背景.
- **👤 关键人物与术语** — a short glossary table for any name/term/event the document assumes the reader already knows. Omit entirely when nothing in the document needs glossing beyond common knowledge.
- **🔗 相关文献** — structured links to other documents (ingested or not) worth reading alongside this one, each with a one-clause stated relationship rather than a bare link list. Link to the containing chapter's 📋 文献索引 anchor for a document not yet ingested. This replaces ad hoc mentions of other documents inside 理解扩展 prose.

Both 🎯 Core Information and 📌 Main Points and Key Facts go English-primary — see "Bilingual document-entry blocks" in `obsidian-rules.md`. Every other section on the page stays Chinese-primary as before.

## Document-entry admission

Unlike a concept or a case study, a document entry does **not** need an
admission test beyond "the editor included it" — the editor has already
done the curation, and admission is never about which documents are
"important enough." What varies is the **unit of Ingest**:

### Full chapter (default)

Ingest every numbered document in the requested era/theme chapter, matching
how every other content model processes one full chapter at a time —
appropriate when the course (or your own reading plan) is working through
the anthology's own chapter structure.

### Selective, by referenced document number (when the course cites specific documents)

Some courses don't assign a reader by chapter at all — they cite specific
document numbers per week/topic, scattered across the anthology's own
chapters, often because each document stands alone (no argument or proof
carries over from #100 to #101 the way a math or CS chapter's content
builds cumulatively). When that's how the course actually uses the book,
Ingest **only the cited documents**, not the rest of their containing
chapter — forcing a full-chapter batch when only 2 of its 7 documents were
ever assigned produces mostly-unused pages for no benefit.

When ingesting selectively:

- Still create/update that chapter's `章节摘要/` file, but its 📋 文献索引
  table lists every document the chapter actually contains (from the
  book's own table of contents), marking which ones have a page yet and
  which don't — so the index is honest about what's been done versus what
  the book contains, and a later selective or full pass can extend it
  without redoing work.
- Do not fabricate a reason a document was skipped; "not yet requested" is
  a fine, honest status.

## Edition risk

A documentary reader with more than one edition frequently **renumbers or
adds documents between editions** — the book's own preface may say so
directly (e.g. "this edition includes documents not in the previous
edition"). Never assume a document number a course or citation gives you
refers to the same document in whatever edition you actually have on
hand.

If the edition on hand doesn't match the edition a course assignment
cites, and the course (or an instructor) has supplied the actual assigned
document's text some other way (an excerpt PDF, a quoted passage in
lecture notes), **cross-reference by that actual text/title/date against
your edition's own table of contents or index** to find the corresponding
entry — never by trusting that the same number lands on the same document
across editions. Record which edition you actually used, and if you had
to remap a cited number to a different one in your edition, say so
explicitly on the document-entry page (`edition_note` in frontmatter, and
a line in the 🔗 教材位置 section) rather than silently substituting.

If no reliable way to identify the corresponding document exists, say so
and flag it `needs-review` rather than guessing.

## Supplementary course materials (optional)

Some courses provide their own material tied to a specific document — an
instructor's own commentary/notes on that document, not the editor's. This
is not standard for this content model and stays **off by default**; use
it only when the course actually supplies such material and grading is
built around it (e.g. exams draw on the instructor's own notes, not just
the book) — confirm this with the user rather than assuming.

When it applies: a document-entry page may add a clearly separate,
explicitly labeled section for it — distinct heading, distinct callout,
and a citation of exactly where it came from (file name, course, whether
it's the instructor's own words or a paraphrase). Never let non-textbook
material blend into the book's own headnote/excerpt sections, and never
present the instructor's phrasing as the editor's or the reverse. See
`templates/primary-source-reader/文献条目-template.md`'s optional
"讲师笔记" section.

## Theme admission (optional, rare)

Some readers explicitly track a recurring theme across many documents (a
preface that says the anthology is organized around evolving ideas of
"freedom" or "who is an American," and individual headnotes that
cross-reference each other by that theme). Create a `概念` page with
kind `theme` only when both hold:

### A. The editor explicitly names and discusses it

Not "many documents happen to be thematically related" — the book's own
preface or headnotes must name the thread and discuss how it develops.

### B. It's tracked across multiple chapters

A theme confined to headnotes within a single chapter belongs in that
chapter's summary, not a standalone concept page — the reuse-across-time
is what earns it independent page status here.

Most primary-source readers will produce zero theme pages per chapter,
some none at all. Do not force one to make the concept index look
populated.

## Stable names

Document-entry filenames use the book's own document number, title, and
date — the same identifier a citation to this book would use:

```text
96. Petition of Black Residents of Nashville (1865).md
```

Theme concept filenames follow the shared bilingual form when useful:

```text
自由的定义演变 (The Evolving Definition of Freedom).md
```

## Single source of truth

- Chapter summary: authoritative era/theme framing and the list of documents it contains, in the editor's own order.
- Document-entry page: authoritative citation, headnote, excerpt, and questions for that one document.
- Concept (theme) page, when one exists: authoritative account of how the theme develops across chapters.
- MOC: authoritative navigation index.

Link rather than duplicate across these boundaries.
