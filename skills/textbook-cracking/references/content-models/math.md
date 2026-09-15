# Content Model: Math

For proof-based mathematics — analysis, algebra, topology, and similar.
Selected during Inspect per `README.md` in this directory; read that file
first if you haven't.

## Signals

- Formal `Definition`/`Theorem`/`Lemma`/`Proposition`/`Corollary` labels,
  numbered and typographically set off from surrounding prose.
- Proofs, explicitly bounded (often ending in □ or "Q.E.D." or similar).
- Exercises are clearly separated from the expository text, not
  interleaved as the primary teaching mechanism.

If a book has these labels but the actual "proofs" are mostly "left to the
reader" with only a handful worked in the main text, it's still the math
model — `../workflow.md`'s fidelity rules already cover representing that
honestly (never fabricate a missing proof). The signal is the book's
*structure* (definition/theorem/proof organization), not how complete its
proofs happen to be.

## Page types and templates

- `章节摘要/` — `templates/math/章节摘要-template.md`
- `概念/` — `templates/概念-template.md` (shared)
- `证明/` — `templates/math/证明-template.md`
- `练习题/` — `templates/math/练习题-template.md` (optional, on request only — see "Practice problems" below)

## Compression policy

Preserve in full:

- every formal definition and newly introduced notation;
- complete conditions and conclusions of formal results;
- every logical step of proofs that the textbook provides;
- remarks, counterexamples, and restrictions that affect validity.

Compress or omit:

- routine examples and repetitive calculations;
- exercises, exercise answers, and exam-oriented advice;
- historical asides and conversational transitions;
- repeated motivation already established earlier;
- Agent-generated teaching content from chapter summaries (belongs only in a labeled `## 🧠 理解扩展` on a concept page).

Compress by mathematical information density, not a mechanical word or percentage limit. An example is worth keeping in the chapter summary only when it's logically necessary to establish a definition's boundary, a hypothesis's necessity, or a later argument — not because it's illustrative.

## Bilingual chapter-summary blocks

Every numbered `#### Definition`/`Notation`/`Theorem`/`Lemma`/`Corollary` block in a chapter-summary page follows `../obsidian-rules.md`'s "Bilingual chapter-summary blocks" rule: bilingual header (English label + title first, Chinese title second in 全角括号), body in English sourced from the textbook's own phrasing, `**条件：**`/`**结论：**` relabeled `**Given:**`/`**Then:**`. `**章节作用：**` and everything else in the chapter summary stays Chinese — see that section for the full boundary. Concept pages and proof pages are unaffected; their own conventions (title `中文 (English)`, Chinese-primary body) are unchanged.

## Page ownership

| Page type | Owns | Must not own |
|---|---|---|
| MOC | navigation, indexes, counts, status | detailed teaching content |
| Chapter summary | chapter order, definitions, formal statements, remarks, logical progression | full proofs, exercises, routine examples |
| Concept | emphasized reusable concepts and labeled Agent explanation | full theorem statements and proofs |
| Proof | one supplied formal proof and its dependencies | chapter-wide summary |
| Practice problems | Agent-original problems one step beyond a bare theorem restatement | the textbook's own exercises, answers, hints |
| Synthesis | CourseManager cross-source material | textbook-cracking output |

## Concept admission test

Create a concept page only when both conditions hold.

### A. The textbook explicitly establishes it

Require at least one strong signal:

- a formal `Definition`;
- typographic emphasis when introduced;
- a section title centered on the term;
- dedicated notation introduced for it;
- repeated explicit use in later sections.

### B. It has independent reuse value

Require at least one:

- appears across multiple sections or later chapters;
- is a prerequisite for multiple results;
- has stable relationships with other concepts;
- has a formal construction or decision procedure;
- has multiple textbook-supported viewpoints;
- is repeatedly contrasted with a nearby concept.

## Allowed concept kinds

- `object`: eigenvalue, eigenvector, probability vector.
- `property`: diagonalizable, orthogonal, normal, self-adjoint.
- `structure`: vector space, inner product space.
- `construction`: direct sum, orthogonal complement, projection.
- `process`: Gram-Schmidt orthogonalization or another formally named reusable process.
- `notation`: only notation that has lasting independent significance.

Do not use `theorem`, `lemma`, `corollary`, `exercise`, or `example` as concept kinds.

## Exclusions from the concept directory

- named theorems and inequalities;
- lemmas, propositions, corollaries, and local conclusions;
- temporary variables or proof-local constructions;
- generic chapter themes;
- exercise-specific methods;
- routine examples;
- terms used once without formal emphasis.

Place named theorem statements in the chapter summary and their supplied proofs in `证明/`.

## Proof page admission

Create a proof page for every theorem, lemma, proposition, or corollary proof the textbook actually supplies, including one-line proofs and results called immediate. Do not create a textbook proof page for a proof that the textbook omits or leaves as an exercise.

Use one page per formal result. If a theorem has parts, keep all parts on the same page. If the textbook provides separate proofs for different directions or cases, preserve those divisions on that page.

## Practice problems (optional, on request only)

This is not part of the default Ingest pipeline — the skill still "omits
exercises and routine filler by default." Only produce `练习题/` pages
when the user explicitly asks for practice problems, separately from a
normal Ingest/Update run.

### What this is, and isn't

- **Is**: original problems composed by the Agent, one level harder than
  a bare restatement of a chapter's own definitions/theorems — proving a
  fact from definitions without citing the just-established result,
  constructing a counterexample or boundary case, or combining two
  results into one argument.
- **Is not**: the textbook's own exercises. Never reproduce, closely
  paraphrase, or renumber a problem the textbook itself poses — that is
  "teacher-selected exercises," which belongs to CourseManager's exercise
  handoff (`references/course-manager-integration.md`), not this skill.
  If asked to "extract the textbook's exercises," decline that specific
  framing and point to CourseManager instead; composing new problems on
  the same material is still in scope.

### Scope grounding

Before writing, determine whether this run has course context:

- **Course context available** (a CanvasManager-synced course directory
  sits alongside this textbook wiki): read the course's own syllabus
  material first — `课程政策`/`课程主页`/a downloaded syllabus PDF under
  `raw/files/` — for the actual assigned chapter/section range. Scope the
  problem set to that range, not the full textbook-cracking ingestion
  (a whole-book Ingest commonly covers more than any single course
  assigns — verify from the syllabus, don't assume the MOC's declared
  range equals the course's). State the source of the range in the
  page's `scope_source` frontmatter field and in the abstract callout.
- **No course context** (a standalone textbook wiki, or the user asks for
  problems independent of any course): scope to the chapter(s) requested,
  and say plainly in the abstract callout that this covers the textbook's
  own range, not a specific course's syllabus.

Never silently guess a course's assigned range from the chapter's
position in the book — read the actual syllabus source or say the range
is textbook-wide.

### Calibration

- Not "too basic": don't just ask to restate a theorem's hypotheses and
  conclusion.
- Not needlessly obscure: stay inside what the ingested chapter summaries
  and proof pages actually establish plus ordinary undergraduate technique
  — don't require outside results the wiki hasn't covered.
- One idea per problem, concisely stated. No multi-part exam-style
  scaffolding unless the concept genuinely needs the setup.
- Order problems by the section in which the relevant material was
  introduced, matching the chapter summary's own section order.

### Format

- One file per chapter: `templates/math/练习题-template.md`.
- No answers, no hints, no worked solutions — statements only.
- Every problem gets a full bilingual pair: Chinese statement, then an
  `*English: ...*` line with the complete English translation immediately
  below it — not just paired terminology. This is a different bilingual
  convention from `../obsidian-rules.md`'s "Bilingual chapter-summary
  blocks" (that rule applies to direct restatements of the textbook's own
  formal content; practice problems are entirely Agent-composed, so both
  full-sentence versions are Agent-authored, not sourced from the book).
- Keep the same LaTeX/notation across both language versions of a
  problem.

## Stable names

Use bilingual concept filenames when useful, following the established form:

```text
特征值 (Eigenvalue).md
```

Use result label plus descriptive title for proof files:

```text
Theorem 5.8 - 可对角化判据 - 证明.md
Cayley-Hamilton 定理 - 证明.md
```

Avoid filenames consisting only of a theorem number.

## Single source of truth

- Chapter summary: authoritative theorem statement in chapter context.
- Proof page: authoritative full textbook proof.
- Concept page: authoritative definition and concept relationships.
- MOC: authoritative navigation index.

Link rather than duplicate across these boundaries.

