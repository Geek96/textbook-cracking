# Obsidian Publishing Rules

## Structure

Use one H1 per page. Use H2 for stable page sections and original textbook sections; use H3 for definitions and formal results. Keep emoji limited to consistent H1/H2 navigation anchors.

Recommended anchors:

- `🗺️` MOC or global knowledge structure
- `📚` chapter index
- `📋` chapter structure
- `🧩` concepts
- `🧾` the content model's own detail pages (proofs for math; case studies for CS; document entries for a primary-source reader)
- `🧠` clearly labeled Agent expansion
- `⚠️` verification or limitations
- `🔗` related pages

Do not decorate every heading or theorem.

## Chapter-summary abstracts

The `> [!abstract] 章节概述` callout at the top of every chapter summary is the one place a reader decides whether to keep reading — it must be scannable in a few seconds, not a single run-on paragraph walking through every section in prose. A dense paragraph that mentions "§2.2 ... §2.3 ... §2.4–§2.8 ... §2.9–§2.11 ..." in sequence is exactly the failure mode to avoid, even though every fact in it may be accurate.

Structure it as short labeled blocks inside the callout (remember: every line inside a callout, including blank lines, needs the leading `>`):

```markdown
> [!abstract] 章节概述
> **一句话**：{{one sentence capturing what the chapter teaches you to do}}
>
> **核心概念**：
> - **{{concept name}} ({{English}})** — {{one-line explanation}}
> - **{{concept name}} ({{English}})** — {{one-line explanation}}
>
> **{{proofs/案例研究/文献}}**（use whichever label the content model's own detail-page type calls for）：
> - **{{unit name}}**（§{{n}}）— {{one-line role}}
>
> **学完本章能做什么**：{{one or two sentences of concrete capability, not a restatement of the concept list}}
```

Omit any block that would be empty (a thin chapter with no concepts skips "核心概念" entirely rather than printing a heading over nothing). This same shape applies regardless of content model — swap "案例研究" for "证明" (math) or "文献" (primary-source reader), and skip the concept block entirely for a model that doesn't use concepts. Detailed prose — the actual per-section explanation, the logical flow between sections — belongs further down the page in the per-section subsections and the `🔗 本章逻辑结构` diagram, not crammed into the abstract.

## Bilingual terminology

Prose defaults to Chinese (see `workflow.md`), but a term's English is not something to state once in a page title and then drop — pair it inline on the term's **first mention in each major section of running prose** (each H2, and each H3 sub-unit within it), not only in the concept page's own title and its wikilink. Repeat mentions later in the *same* section can drop the English; a new section re-mentioning the same term pairs it again, since a reader may jump straight to that section without reading from the top.

This applies to more than concept-page-worthy terms — a piece of terminology a student needs to recognize in English (an error category, a named technique, a named operator) still gets paired on first mention per section even if it never earns its own concept page:

```markdown
标识符（identifier）必须以字母、下划线或美元符号开头...
```

not

```markdown
标识符必须以字母、下划线或美元符号开头...
```

This is layered on top of, not a replacement for, the existing rule to preserve actual language keywords/API names/notation verbatim in code font rather than translating them (`Scanner`, `switch`, `\operatorname{rank}`) — those were never the gap; the gap is Chinese jargon that silently drops the English a reader would need to look the term up, cite it, or recognize it in the textbook/exam/documentation.

## Bilingual chapter-summary blocks

A chapter summary's numbered definition/theorem-family blocks (math: `#### Definition/Theorem/Notation/Lemma/Corollary`; CS: `#### Concept:` blocks and `Common Error`/`Common Pitfall` callouts) are a *direct restatement* of the textbook's own formal content, not the Agent's synthesis — so, unlike the rest of a chapter-summary page, these go **English**, sourced from the source textbook's own actual phrasing (recall or reconstruct how the book itself states it — don't machine-translate a Chinese draft):

- **Header**: bilingual, English label + English title first, Chinese title second in 全角括号 — e.g. `Definition 1.20: Vector Space（向量空间）`, `Theorem 8.2 — Schur's Theorem（舒尔定理）`, `Concept: Java Program Structure — Class and the main Method（Java 程序结构：类与 main 方法）`. The chapter/section headings above these blocks (`## §N.N ...`, `### 定义与记号`, `### 定理、引理与推论`, `### 语言特性与概念`) stay Chinese-only — only the numbered block headers themselves get the bilingual treatment.
- **Body**: the definitional/theorem prose itself goes English. For a Theorem-family block, the `**条件：**`/`**结论：**` labels become `**Given:**`/`**Then:**`, content in English.
- **Stays Chinese, unchanged**: everything that is the Agent's own organization or commentary rather than a restatement of the book — `**章节作用：**` lines, `> [!abstract] 章节概述`, `📋 章节结构` tables, `### 本节结论`, `🧩 本章概念索引`, `🔗 本章逻辑结构`, `📌 本章结论`, `⚠️ 摘要范围与验证`, and the prose walking through what a section covers (the `## §N.N ...` intro paragraphs). A `Common Error`/`Common Pitfall` callout whose body is just a cross-reference to another page (e.g. "已在 XX 概念页记录") is Agent-organizational, not a restatement — it stays Chinese; only a callout that actually restates the book's own mistake-description goes English.
- Inside a `[!note]`/`[!warning]` remark that restates a specific textbook Example's concrete mathematical claim or construction, translate just that restated content to English; the callout's own title and the Agent's interpretive/concluding sentence stay Chinese.
- This is narrower than the general "Bilingual terminology" rule above (which governs ordinary running prose everywhere, always Chinese-primary with English paired inline) — inside these specific blocks, the *default* language flips to English because the content itself *is* the textbook's formal statement, not prose about it.
- Applies to chapter-summary pages under the math and CS content models (see their own files for the exact block-type mapping — CS's version is deliberately lighter-touch, since most `Concept:` blocks are just a bare link with no independent prose to translate). Concept pages, proof pages, and case-study pages are **not** in scope for this rule — their own bilingual conventions (title `中文 (English)`, Chinese-primary body per the "Bilingual terminology" rule above) are unchanged. Week pages and primary-source-reader document entries already quote source material in its original language by construction (see each model's own file) and don't need this rule applied separately.

## Bilingual document-entry blocks

A primary-source-reader document entry's `🎯 Core Information（核心信息）` and `📌 Main Points and Key Facts（主要观点与重要事实）` sections go **English-primary**, the same direction-flip as "Bilingual chapter-summary blocks" above but for a different reason: these two blocks distill the document's own argument in the course's own working language (the documents themselves are English-language American historical sources), so English is the natural default rather than a translation layer over Chinese synthesis.

- **Header**: bilingual, English label first, Chinese second in 全角括号 — `## 🎯 Core Information（核心信息）`, `## 📌 Main Points and Key Facts（主要观点与重要事实）`.
- **Body**: English prose/table content. Gloss a specific term, event, or proper noun in Chinese in 全角括号 immediately after it where that aids recognition (`Gilded Age（镀金时代）`, `the Homestead strike（霍姆斯特德大罢工）`) — don't translate the whole sentence or cell; this is targeted glossing, not the full-parallel-pair pattern used for practice problems. A headline quote already given in the original English in `原文节选` may carry its Chinese rendering alongside it in these two blocks, matching how `104. Andrew Carnegie, The Gospel of Wealth (1889).md` handles its closing epigram.
- **Stays Chinese, unchanged**: every other section on a document-entry page — `出处`, `背景`, `原文节选`'s own summary prose, `👤 关键人物与术语`, `讨论问题`, `👨‍🏫 讲师笔记`, `🔗 相关文献`, `🧠 理解扩展`, `🔗 教材位置`, and the verification note. Only these two specific blocks flip.
- Applies to the `document-entry` page type under the primary-source-reader content model only (see `content-models/primary-source-reader.md`). Does not extend to chapter-summary or week pages under this content model.

## Bilingual practice problems

`练习题/` pages (math model, optional — see `content-models/math.md`) use a third, distinct bilingual pattern: **every problem is a full parallel pair**, a complete Chinese statement immediately followed by a complete English translation on its own line (`*English: ...*`) — not paired terminology (the "Bilingual terminology" rule above), and not a switch to English-as-default for a whole block (the "Bilingual chapter-summary blocks" rule above).

The reason it's a separate rule: both rules above key off whether content is a *restatement of the textbook's own formal wording* (chapter-summary blocks) versus *ordinary Agent prose about the material* (everywhere else, paired-terminology rule). A practice problem is neither — it's original Agent composition end to end, so there's no "source phrasing" to translate faithfully; both language versions are equally Agent-authored, need equal full statements, and must express exactly the same problem (same hypotheses, same question, same notation/LaTeX in both) so a reader working in either language gets an identical exercise.

## Frontmatter

- Start YAML on the first line.
- Use flat properties; Obsidian does not natively support nested properties well.
- Use `tags`, `aliases`, and `cssclasses`, not deprecated singular forms.
- Use ISO dates: `YYYY-MM-DD`.
- Quote wikilinks stored as property values.
- Keep each property type consistent across the vault.
- Use the verification values `extracted`, `needs-review`, or `source-checked`.
- **Frontmatter integrity check on a multi-machine synced vault.** Before editing any page that lives in a Syncthing-synced vault (per the machine's own `AGENTS.md`), confirm its frontmatter still starts with `---` and still carries this project's own required keys (`type:` at minimum) before trusting or extending it — a real incident on this project (2026-09) found a third-party tool on one machine had **replaced** (not appended to) the frontmatter of several files with an unrelated AI-content-labeling metadata block (fields like `Label`/`ContentProducer`/`ProduceID`), silently breaking `validate_wiki.py` and losing every expected property while leaving the page body untouched. If a file's frontmatter doesn't parse as this project's own schema, do not silently regenerate the page or guess values — the body content is very likely still intact (verify by reading it), so treat this as a frontmatter-only repair (rebuild the expected keys from a same-type sibling file's schema, preserve the body byte-for-byte) and flag it to the user rather than working around it quietly.

## Links

Use wikilinks for vault content:

```markdown
[[特征值 (Eigenvalue)]]
[[特征值 (Eigenvalue)|特征值]]
[[Chapter 5 - 对角化#Theorem 5.8 — 可对角化判据|Theorem 5.8]]
```

Use Markdown links for external URLs. Link to source PDF pages when the source is inside the vault:

```markdown
[[raw/Linear Algebra.pdf#page=291|PDF p.291]]
```

Do not create speculative wikilinks for ordinary terms that fail the concept admission test.

## Callouts

Use only native callout types unless the user explicitly supplies CSS:

- `[!abstract]` overview or optional collapsed explanatory structure;
- `[!info]` textbook source and provenance;
- `[!note]` textbook remarks;
- `[!warning]` restrictions, counterexamples, OCR uncertainty;
- `[!tip]` labeled Agent understanding aid.

Do not use unsupported `[!source]`. Use:

```markdown
> [!info] 教材出处
> §5.2，书本 p.283，PDF p.297。
```

If a formula is inside a callout, prefix every line, including blank lines and `$$`, with `>`.

## MathJax

Applies whenever a page carries math notation, regardless of content model — a CS textbook's Big-O analysis or a primary-source document quoting a formula still follows these rules. Skip this section entirely for a page with no math in it.

- Use `$...$` for inline math.
- Put block delimiters `$$` on their own lines with blank lines around the block.
- Use semantic operators such as `\operatorname{rank}`, `\operatorname{span}`, `\ker`, `\dim`, and `\det`.
- Use `\lVert x\rVert`, `\lvert x\rvert`, and `\langle x,y\rangle` instead of ambiguous ASCII forms.
- Use `pmatrix`, `bmatrix`, `cases`, `aligned`, or `array` for structured formulas.
- Avoid complex formulas in headings and Markdown tables.
- Preserve the textbook's notation even when a newer notation is more common.
- Do not silently normalize `N(T)` to `\ker T`, or `R(T)` to `\operatorname{im}T`, when the textbook uses the former.
- Do not depend on custom MathJax packages or vault-specific macros.

## Code blocks

Applies whenever a page reproduces the textbook's own code (a CS case study, a formula-adjacent snippet in any other model).

- Fence every listing with the language tag the textbook's own code actually is (` ```java `, ` ```python `, ...) — never a bare ` ``` `, which loses syntax highlighting and signals "unidentified" to a reader.
- Reproduce the textbook's code verbatim: same variable names, same formatting choices, same comments. This is the one place in the wiki where "faithful paraphrase" does not apply — code is copied exactly, because a paraphrased program is a different program.
- Preserve the textbook's own file/class name if it names one (`// GuessNumber.java`) as a comment on the first line of the block, matching how the textbook itself presents it.
- If the textbook's own text has a typo or a bug the book later corrects, keep the block as printed and note the discrepancy in a `[!warning]` rather than silently fixing it.

## Agent-managed regions

Wrap every generated body region in stable namespaced markers:

```markdown
<!-- agent-managed:start id="textbook:document-id:chapter-05" -->
...
<!-- agent-managed:end -->
```

Before updating:

1. Read the whole file.
2. Replace only the matching managed region.
3. Preserve all text outside it byte-for-byte.
4. Preserve unknown user-added frontmatter properties.
5. Never rebuild the entire file merely to update one managed section.

## Dependency policy

Generate static Markdown tables and lists. Do not require Dataview, custom CSS, an Obsidian MCP server, or another plugin. Optional enhancements must not be necessary for navigation or correctness.

