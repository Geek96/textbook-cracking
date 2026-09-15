---
type: document-entry
title: "{{doc_number}}. {{doc_title}} ({{date}})"
aliases:
  - "{{doc_title_alt}}"
course: "{{course_id}}"
document_id: "{{document_id}}"
entry_id: "{{entry_id}}"
chapter: {{N}}
doc_number: {{doc_number}}
date: "{{date}}"
author: "{{author_or_speaker}}"
doc_type: "{{speech|petition|law|letter|testimony|other}}"
source_file: "{{source_file}}"
book_pages: "{{book_page_range}}"
pdf_pages: "{{pdf_page_range}}"
edition_note: "{{optional — fill in only when the document number had to be remapped across editions; state which edition was cited vs. which was used and how the match was confirmed. Delete this field entirely when no remapping was needed.}}"
concepts:
  - "[[{{theme_concept_page}}]]"
verification: {{verification}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
tags:
  - type/document-entry
  - course/{{course_slug}}
---

# {{doc_number}}. {{doc_title}} ({{date}})

<!-- agent-managed:start id="textbook:{{document_id}}:document-entry:{{entry_id}}" -->

## 出处

> [!info] Source
> {{Faithfully reproduce the book's own citation line — archive, publication, collection, date — exactly as printed.}}

## 背景

{{Faithfully convey the editor's own headnote: who wrote/spoke this, the circumstances, and why the editor included it. Close paraphrase is fine; do not invent context the headnote doesn't supply.}}

## 🎯 Core Information（核心信息）

{{English-primary, per "Bilingual document-entry blocks" in obsidian-rules.md — this is the Agent's own HIPP-style analysis of the document, not book text, but goes English-primary to match how a reader would discuss the document in the course's own (English) terms; gloss a term in Chinese in 全角括号 only where it aids recognition, don't translate the whole cell.}}

| Dimension | Content |
|---|---|
| **Historical Context** | {{the broader situation/debate the document responds to}} |
| **Intended Audience** | {{who the document was written/spoken for}} |
| **Purpose** | {{what the author was trying to accomplish by producing this document}} |
| **Author's Standpoint** | {{the author's own position/stake relative to the document's subject — note it explicitly when the author is themselves an interested party}} |

## 📌 Main Points and Key Facts（主要观点与重要事实）

{{English-primary bullet list — see "Bilingual document-entry blocks" in obsidian-rules.md. Extract the document's own main claims/arguments and the load-bearing facts a reader needs, not a restatement of 背景. Gloss proper nouns/events/named concepts in Chinese where useful; keep any headline quote's Chinese rendering alongside it.}}

- {{main point or key fact}}
- {{main point or key fact}}

## 原文节选

> {{A load-bearing quoted passage or two from the document — not a full reproduction. Quote the sentences that actually carry the document's substance; summarize the rest in your own words below rather than quoting at length.}}

{{Accurate prose summary of the remainder of the document's content, for anything not directly quoted above.}}

## 👤 关键人物与术语

{{A short glossary table for names/terms/events a reader needs to recognize to follow the document — not a full dictionary; only what actually appears or is presupposed by the text. Delete this section if the document introduces nothing beyond common knowledge.}}

| 术语/人物 | 简注 |
|---|---|
| {{term or name}} | {{one-line gloss}} |

## 讨论问题

{{Reproduce the book's own "Questions" prompt for this document, if it supplies one. Delete this section if the book doesn't include questions for this entry.}}

1. {{question}}

## 👨‍🏫 讲师笔记（可选，非教材内容）

> [!warning] 内容来源与边界
> 本节内容来自**课程材料**（{{exact file name / course source}}），**不是** {{editor_name}} 编者原文。这是本课程的特例用法（见 `content-models/primary-source-reader.md`"Supplementary course materials"一节）——仅在课程实际提供且考试依赖此类材料时使用，默认不启用。

{{Faithfully convey the instructor's own notes/commentary on this specific document, attributed and kept visually/structurally separate from the 背景/原文节选 sections above. Delete this entire section (heading + callout) when the course provides no such material for this document.}}

## 🔗 相关文献

{{Structured cross-references to other documents in this chapter (or an adjacent one) that are worth reading alongside this one — not every document in the chapter, only ones with a real relationship (shared theme, direct rebuttal, contrasting position, same author/movement). For a document not yet ingested, link to the chapter summary's 📋 文献索引 anchor instead of a page that doesn't exist yet, and mark it "（尚未摄取）". State the relationship in one clause, not just the link. Delete this section if no other document in the vault has a real relationship to this one yet.}}

- {{[[link]] or chapter-index anchor}}——{{one-clause relationship}}

## 🧠 理解扩展

> [!info] 内容来源
> 本节由 Agent 基于上述文献内容生成，用于辅助理解，不属于教材原文。

{{Optional: how this document connects to broader historical debates beyond what 🔗 相关文献 and 背景 already cover, or a clarifying note. Keep this short — cross-references now live in 🔗 相关文献, so this section should not duplicate them. Delete when it adds no value.}}

## 🔗 教材位置

- 章节：[[{{chapter_page}}#📋-文献索引|{{chapter_reference}}]]
- 书本页：pp. {{book_page_range}}
- PDF：[[../../../textbooks/{{source_file}}#page={{first_pdf_page}}|PDF p.{{first_pdf_page}}]]

> [!info] 验证状态
> {{State exactly what was checked — citation matches the book verbatim, headnote faithfully conveyed, quoted passage matches the source text exactly, core information/main points/key terms are grounded in the document and headnote with nothing introduced from outside them — and list unresolved details.}}

<!-- agent-managed:end -->
