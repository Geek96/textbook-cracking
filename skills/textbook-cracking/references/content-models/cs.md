# Content Model: CS

For programming/CS textbooks organized around language concepts and
worked code examples — introductory programming texts, data structures
texts, and similar. Selected during Inspect per `README.md` in this
directory; read that file first if you haven't.

## Signals

- Numbered sections introduce language features and OOP concepts by name
  (encapsulation, inheritance, a specific syntax construct), not
  definition/theorem/proof triples.
- Named, dedicated worked examples — often literally labeled "Case Study:
  X" or similar — each with a complete code listing, not just a one-line
  syntax illustration.
- "Key Point," "Caution," "Pitfall," or similarly-boxed callouts flagging
  common mistakes, distinct from the exercises.
- No formal proofs; if the book does contain occasional formal proofs (a
  complexity-theory or algorithms text proving a bound), that's a signal
  toward the *math* model instead, or occasionally a book genuinely mixes
  both — say so during Inspect rather than picking one and hiding the rest.

## Reading method

Many CS textbooks lay out marginal icons/labels (a "Key Point" or "Check
Point" or "VideoNote" flag sitting in a side margin next to the relevant
paragraph) that a linear text-layer extraction does not preserve in
reading order — the label's vocabulary shows up somewhere it doesn't
belong even though the PDF has a perfectly real text layer. This is a
layout-complexity problem, not a scan-quality problem, and it will not
show up as an obviously broken PDF. The exact failure shape depends on the
extraction tool: it can land mid-sentence, but a validated real case
(PyMuPDF against a Liang textbook) instead consistently *appended* the
stray vocabulary ("Point Check Point Key," "VideoNote") as a block right
after a paragraph or page boundary, with the actual sentences staying
intact — don't assume mid-sentence corruption is the only shape this
takes.

Default to text extraction (it's fast and normally accurate for prose and
code). Watch for the tell: fragments of marginal-label vocabulary
("Point," "Check," "Key," "VideoNote," or similar short repeated tokens)
sitting somewhere with no grammatical reason to be there — mid-sentence or
tacked onto a boundary. The moment you see that on a page, treat
neighboring pages with the same layout as suspect and render at least one
as an image to confirm reading order — in the validated case this
confirmed the text was actually fine (the scrambled tokens were isolated
noise, not lost content), so a confirmed-clean run doesn't necessarily mean
you must re-render every subsequent page of the same layout; re-escalate
if the pattern changes. Confirm the actual pattern during Pilot rather than
assuming every book behaves the same way.

## Box-out taxonomy

Map the textbook's own labeled boxes to wiki structure by their actual
label, not by guessing intent:

- **`Common Error N: <title>`** (or similarly explicitly labeled mistake
  boxes) → a `[!warning]` pitfall, tied to the concept or case study it's
  attached to. This is real content — preserve it per the compression
  policy below.
- **`Note`** → usually a meta/pacing aside about the book itself ("this
  section may be skipped"), not technical content. Skip it unless it
  actually states a technical restriction or caveat, in which case treat
  it like any other textbook remark.
- **`Key Point` / `Check Point` / `VideoNote`** or similar bare marginal
  tags with no attached explanatory sentence of their own → these are
  print-layout navigation aids (they point at a paragraph, or point to an
  external video), not content. Do not create a page section for the tag
  itself; if a "Check Point" turns out to be a numbered self-check
  question (see below), handle it as an exercise, not as content.

## Page types and templates

- `章节摘要/` — `templates/cs/章节摘要-template.md`
- `概念/` — `templates/概念-template.md` (shared)
- `案例/` — `templates/cs/案例-template.md`
- `周次/` (optional — see "Week pages" below) — `templates/cs/周次-template.md`
- `选择题练习/` (optional, on request only — see "Week practice" below) — `templates/cs/选择题练习-template.md` + `templates/cs/选择题答案-template.md`
- `编程练习/` (optional, on request only — see "Week practice" below) — `templates/cs/编程练习-template.md`

## Compression policy

Preserve in full — this is where CS differs most from math:

- every case study's actual code listing and its explanatory walkthrough.
  A worked example here is not a "routine example" to compress — it is
  frequently *the* teaching mechanism, the thing a student is expected to
  reproduce and adapt. Compressing it away removes the actual content.
- concept definitions and their syntax rules;
- "Common Error"/"Caution"/"Pitfall"-style labeled mistake callouts (see
  Box-out taxonomy above) — these carry real information density (what a
  student will actually get wrong) even though they read like asides.

Compress or omit:

- a one-off syntax illustration with no dedicated worked-example status —
  fold a brief mention into the relevant concept page instead of giving it
  its own case-study page;
- end-of-chapter exercises, review questions, and answer keys;
- **numbered self-check questions embedded mid-section**, not just
  end-of-chapter problem sets — many CS textbooks interleave a short
  numbered question after every subsection (e.g. "2.12.1 How would you
  write..."), not only in a clearly separated exercises block. These are
  still exercises; recognize them by pattern (a numbered prompt asking the
  reader to do something, immediately following expository content) and
  exclude them even mid-paragraph;
- figures/screenshots that are purely illustrative (an IDE dialog, a UI
  screenshot) — these are typically vendor-copyrighted (watch for a
  "Source: Copyright © ... Used with permission" line) and add no content
  beyond what the surrounding prose already states; mention their existence
  in prose only if the chapter's explanation actually depends on what they
  show, never reproduce or describe the image itself;
- language-history trivia unrelated to how the feature is actually used;
- repeated motivation already established earlier in the book;
- bare "Note" asides about the book's own pacing (see Box-out taxonomy).

Compress by *teaching* density, not code-line count — a 40-line case study
that's the chapter's central worked example stays in full; a 3-line
snippet used only to show syntax does not need its own page even though
it's short enough to "fit."

## Bilingual chapter-summary blocks

A chapter summary's `#### Concept: ...` blocks and `Common Error`/`Common
Pitfall` callouts follow `../obsidian-rules.md`'s "Bilingual chapter-summary
blocks" rule, applied lighter-touch than the math model's: bilingual header
(`Concept: English Title（中文标题）`), and body prose in English **only
when there's independent prose actually restating the book** — many
`Concept:` blocks in this model are just a bare wikilink with no prose of
their own, in which case only the header changes. A `Common Error`/`Common
Pitfall` callout whose body is a bare cross-reference ("已在 XX 概念页记录")
stays Chinese — it's Agent bookkeeping, not a restatement; only a callout
that actually restates the book's own mistake-description in prose goes
English, with a Chinese gloss added to its title if the title was
English-only to begin with. Section-overview prose under a `## §N.N ...`
heading — the Agent's own walkthrough of what a section covers — stays
Chinese regardless, same as `**章节作用：**` and every other organizational
element; see `../obsidian-rules.md` for the full boundary. Week pages get
this naturally already (source-quoted slide/book content in English,
`📝 Agent 补充讲解` boxes in Chinese) rather than needing the rule applied
separately — see "Week pages" below.

## Concept admission test

Create a concept page only when both conditions hold.

### A. The textbook explicitly establishes it

Require at least one strong signal:

- a formal definition or a boxed "Key Point" introducing it;
- a section title centered on the term;
- consistent, repeated use by name in later sections;
- explicit contrast with a nearby concept (e.g. the book explicitly
  discusses "abstract class vs. interface").

### B. It has independent reuse value

Require at least one:

- appears across multiple sections or later chapters;
- is a prerequisite for understanding later case studies;
- has a stable set of syntax rules or an API surface worth recording on
  its own;
- is repeatedly contrasted with a nearby concept;
- has a named, recurring pitfall associated with it worth recording
  alongside the concept itself.

## Allowed concept kinds

- `syntax`: a language construct with its own grammar/rules — a loop form,
  `switch`, `try`/`catch`, generics syntax.
- `oop-principle`: encapsulation, inheritance, polymorphism, abstraction —
  the book's own named organizing ideas, not a generic OOP glossary term
  it never actually names or discusses.
- `api`: a specific class/library facility the book treats as a reusable
  tool across multiple case studies (e.g. `ArrayList`, `Scanner`) — not
  every class mentioned once in passing.
- `pattern`: a reusable coding pattern or idiom the book names and reuses
  (e.g. "loop-and-a-half," a specific recursion template) — distinct from
  a one-off case study's local logic.
- `terminology`: a classification or vocabulary scheme the book itself sets
  up and reuses — e.g. "syntax error / runtime error / logic error" as a
  named three-way distinction it keeps referring back to. Reserve this for
  a genuine reused classification, not any definition that happens not to
  fit the other four kinds; if in doubt, it probably belongs in the
  chapter summary's prose instead of a page of its own.

Do not use `case-study`, `exercise`, or `example` as concept kinds — those
are covered by the `案例/` page type or omitted per the compression policy
above.

**Granularity**: this admission test doesn't by itself say how finely to
split closely-coupled micro-syntax rules (e.g. identifiers vs. naming
conventions, or assignment vs. augmented assignment). Default to merging
them onto one concept page when the book itself treats them as one
continuous topic (same subsection, immediately adjacent, no independent
treatment later) — split them only when the book itself later treats them
independently (separate later sections, separately reused, separately
contrasted). When genuinely unsure, merge and say so in the page's
verification note rather than silently picking one without comment.

## Exclusions from the concept directory

- one-off variable/method names local to a single case study;
- a class or method mentioned once without the book treating it as a
  reusable tool;
- exercise-specific techniques;
- generic chapter themes ("this chapter is about loops");
- terms used once without the book's own emphasis.

## Case-study page admission

Create a case-study page for every named, dedicated worked example the
textbook supplies with a complete code listing — typically the book's own
"Case Study," "Example," or similarly labeled subsections that include
full runnable (or near-runnable) code plus explanation, not a bare syntax
snippet. **The literal label is illustrative, not required**: a subsection
with its own heading, a stated problem, a complete listing, and a
multi-step walkthrough is admissible on that structure alone even if the
book calls it something else entirely (a validated real case: Liang's
"2.17 Software Development Process" isn't labeled "Case Study" but is
structurally identical to the ones that are — full 5-stage build-up plus
complete listing — and was rightly admitted). Do not create one for a
one-off illustration with no dedicated subsection of its own; those stay
inline in the chapter summary or fold into the relevant concept page's own
brief illustration.

Use one page per case study. If the textbook builds one running example
across several sections (revisiting and extending the same program), keep
that on one page with clearly dated/labeled stages rather than splitting
into disconnected fragments — mirror how the book itself presents it.

Many CS textbooks label their own code listings explicitly (e.g. "Listing
2.6 FahrenheitToCelsius.java") — when the book does this, use that exact
label as the code block's leading comment in the case-study page, per
`../obsidian-rules.md`'s Code blocks section. It's a ready-made, unambiguous
citation back to the source.

## Chapter scope, independent of course pacing

A course's own week-by-week schedule frequently does **not** match the
book's chapter order, and often revisits pieces of the same chapter across
several non-adjacent weeks (a "Ch9" that first appears in an early week
and gets referenced again two or three weeks later once inheritance
depends on it). Ingest by the book's own complete chapter regardless — do
not fragment a chapter into per-week partial pages to match the syllabus,
even when Week pages (below) are in use.

**Sequencing** (which chapter to Ingest next) is a separate question from
scope (how much of it to Ingest at once), and when the course actually
supplies its own weekly teaching material (see "Week pages" below),
sequencing is driven by that: Ingest whichever chapter the *current or
next* week's material actually needs, first — not the book's front-to-back
order. If a week's material doesn't require any not-yet-ingested chapter
(everything it touches is already built), there's nothing to sequence;
proceed straight to building that week's page. Absent real weekly
material to key off, fall back to the course's own due-date/schedule
pacing per the general rule, or book order if neither exists.

## Week pages (optional — only when the course supplies its own weekly teaching material)

Off by default. Use only when a course actually publishes its own
weekly lecture material (slide decks, lecture PDFs) with real technical
content — not merely a syllabus schedule saying which chapters a week
covers (that's just a sequencing input, handled above, not a Week page).

### What a Week page is for

The professor's own slide deck is the second source this content model
formally supports (alongside the textbook itself) — same spirit as the
primary-source-reader model's "Supplementary course materials," but Week
pages are a first-class page type here rather than an optional section
bolted onto an existing page, because a single week's slides typically
span multiple concepts/chapters and don't belong inside any one of them.

### Scope: technical content only

A Week page covers what the slides actually **teach** — the same test as
everything else in this content model. It does **not** cover
administrative content the slides may also carry (schedule, grading
breakdown, office hours, policy) — that belongs to CanvasManager's own
course-dashboard/info pages, not here. A "Course Overview" style deck that
is entirely administrative produces no Week page at all.

### Structure: link where the book already covers it, explain where it doesn't

Every real topic the slides raise gets addressed — like primary-source
reader's document entries, the professor already did the curation by
choosing to teach it, so there's no separate admission test. For each
topic:

- **Already covered by an existing (or newly Ingested, per the
  sequencing rule above) concept/case-study page** — link to it, plus a
  short bridging note only if the professor's slides frame it differently
  from the book (a different example, a different emphasis, an anecdote
  the book doesn't have) — don't restate what the linked page already
  says in full.
- **Not covered by the book, or the slide is a bare outline bullet with
  no real elaboration of its own** (e.g. a "Material Covered" slide that
  just lists topic names) — write the explanation yourself, sourced from
  whatever the slide does say plus your own domain knowledge to fill the
  gap. This is a real departure from this Skill's normal fidelity
  discipline (which never fills gaps from memory) — **it must be visibly
  labeled as Agent-authored, not attributed to the professor's slide**,
  using a dedicated `📝 Agent 补充讲解` callout so a reader can never
  mistake your filled-in explanation for what the professor actually said
  in class.

### Sourcing discipline

Read the actual slide deck's real text content (per-slide), not just its
title/table-of-contents slide — a "Material Covered" outline slide is not
the content itself, it's a pointer to slides later in the same deck that
may or may not actually elaborate. Cross-check before deciding a topic
needs Agent-authored filling.

### Language

When a slide states its own formal definition of a term (a dictionary-style
definition, a "bookish definition" box, a named rule stated as a sentence),
quote it in English — the slide's own wording, not a Chinese paraphrase —
the same principle as `../obsidian-rules.md`'s "Bilingual chapter-summary
blocks" rule applied to slide-sourced content instead of book-sourced
content. The bridging/comparison prose around it (how the slide's framing
relates to the book's, what's new versus already covered) stays Chinese,
same as everywhere else on this page — it's the Agent's own synthesis, not
a restatement. A `📝 Agent 补充讲解` box is always Chinese in full, including
any part of it that organizes material the slide itself stated, because the
whole box's function is "flagged as not textbook/slide-original" — mixing
in an English quote there would blur that boundary rather than sharpen it.

### MOC integration

`MOC.md` gets a `## 🗓️ 周次索引` section (a new H2, not a subsection of
the chapter/concept/case-study indexes — a reader hitting it for the first
time doesn't know what a Week page is, so give it its own one-line
explainer callout the first time this section is created). One table row
per week, same table style as the chapter/concept indexes. State plainly
in that row (or the week page's own abstract) whether the week required
Ingesting a not-yet-done chapter or worked entirely off pages that already
existed — this is exactly the kind of "did this week move the sequencing
queue" fact a reader of the MOC wants at a glance, not something to bury
in prose.

Don't add reverse links from every touched concept page back to each Week
page that references it — a popular concept will accumulate many such
backlinks over a semester with no real navigational payoff, and the MOC's
own Week index already serves as the reverse-lookup surface.

## Week practice (optional, on request only)

Off by default, and independent of whether Week pages are in use — this is
a further opt-in on top of that opt-in. Only build these when the user
explicitly asks for practice material for one or more weeks; never as part
of a normal Ingest run. Requires Week pages to already exist for the weeks
being covered (practice questions are sourced per-week, not per-chapter).

### What this is, and isn't

Two independent sub-types, both Agent-original, neither the professor's or
a third party's own copyrighted material republished:

- **`选择题练习/`** — multiple-choice questions testing that week's syntax
  and concept material. Some are *modeled on* the professor's own slide
  deck's Review/Practice self-check questions (the ones `cs.md`'s
  compression policy already excludes from the Week page itself) — same
  knowledge point, same rough difficulty, **never the professor's actual
  question reworded or lightly edited**. Write a new question from
  scratch that tests the same thing. The rest are fully original,
  authored from what the Week page and its linked concept/case-study
  pages establish. Answers live on a **separate page**
  (`选择题答案/`-suffixed filename, or a matching file in a sibling
  `选择题答案/` folder — pick one convention and use it consistently
  within a course) — never inline with the questions.
- **`编程练习/`** — a short curated list of classic problems matching that
  week's topics, each a **link only** (typically to LeetCode or a
  similar judge) plus a one-line reason it's relevant to the week — never
  the problem statement, constraints, examples, or a solution reproduced
  into the wiki page. This is not a "practice problems" page in the
  proof-writing sense (see the math content model) — it curates pointers
  to external judged problems, it doesn't compose them.

### Sourcing discipline for MCQs

Read the week's actual source slide deck(s) (`raw/files/...` per the Week
page's own `source_files`) for the professor's Review/Practice questions
before writing the "modeled on" subset — don't guess at what they probably
asked. If a week's slides carry no such self-check questions, that subset
is simply zero for that week; make the rest fully original rather than
inventing a fake "modeled on" provenance.

### Volume and workload

There's no fixed skill-wide default — agree the per-lecture/per-week count
and the modeled-vs-original split with the user for the specific course,
and record it in the week's practice page (e.g. "10 道参考幻灯片自带
Review 题的知识点改写，20 道原创，共 30 道"). Keep `编程练习/` short
enough not to compete with the course's own graded workload for that
week — a handful of problems, not a long list; ask the user for a
per-week ceiling rather than assuming one.

### Frontmatter and page ownership

`选择题练习/`, `选择题答案/`, and `编程练习/` pages set `week_number` and
link back to the corresponding `周次/` page (`week_page:
"[[Week 0N - ...]]"`) — they extend that week's material, they don't
duplicate its own explanatory content. A `选择题练习/` page never restates
concept/case-study content from linked pages, only the question stems
(and, for MCQ, the answer options) themselves.

### MOC integration

Add a `## 📝 周练习索引` section to `MOC.md` (own H2, own one-line
explainer on first creation, same as the Week index) once any practice
page exists — one row per week covered, linking the MCQ set, its answer
key, and the coding-practice page, plus the agreed volume as a quick
per-row fact.

## Stable names

Concept filenames follow the shared bilingual form:

```text
封装 (Encapsulation).md
```

Case-study filenames use the book's own case-study title:

```text
案例 - 猜数字游戏 (Guessing Numbers).md
```

Week page filenames use the course's own week numbering:

```text
Week 01 - Intro to Java; Variables, Primitives, Literals.md
```

Week practice filenames use the same week numbering plus a fixed suffix:

```text
Week 03 - 选择题.md
Week 03 - 选择题答案.md
Week 03 - 编程练习.md
```

Avoid filenames that are just a section number.

## Single source of truth

- Chapter summary: authoritative account of what the chapter covers and how the sections connect.
- Case-study page: authoritative full code + walkthrough for that worked example.
- Concept page: authoritative definition, syntax, and relationships.
- Week page (when used): authoritative record of what the professor's own slides taught that week, and how it maps onto the book's concepts/case-studies — never duplicates a concept page's full content, only links to it plus whatever the slides added on top.
- Week practice page (when used): authoritative set of Agent-original MCQs/answer key/curated external-problem links for that week — never duplicates the Week page's explanatory content, and never republishes the professor's or a judge site's own problem text.
- MOC: authoritative navigation index.

Link rather than duplicate across these boundaries.
