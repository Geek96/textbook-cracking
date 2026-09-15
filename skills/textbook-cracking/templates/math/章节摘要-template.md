---
type: chapter-summary
title: "Chapter {{N}} - {{chapter_title_zh}}"
aliases:
  - "{{chapter_title_original}}"
course: "{{course_id}}"
document_id: "{{document_id}}"
chapter_id: "ch{{NN}}"
chapter_number: {{N}}
source_file: "{{source_file}}"
book_pages: "{{book_page_range}}"
pdf_pages: "{{pdf_page_range}}"
sections:
  - "{{N}}.1"
concepts:
  - "[[{{concept_page}}]]"
verification: {{verification}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
tags:
  - type/chapter-summary
  - course/{{course_slug}}
---

# Chapter {{N}} — {{chapter_title_zh}}

<!-- agent-managed:start id="textbook:{{document_id}}:chapter-{{NN}}" -->

> [!abstract] 章节概述
> **一句话**：{{one sentence capturing the chapter's central question and outcome}}
>
> **核心概念**：
> - **{{concept_name}} ({{English}})** — {{one-line explanation}}
>
> **主要结果**：
> - **{{result_label}}**（§{{n}}）— {{one-line statement of what it establishes}}
>
> **学完本章能做什么**：{{one or two sentences of concrete capability}}
>
> {{Omit the 核心概念/主要结果 block entirely if this chapter admits none — do not print an empty heading. See ../../references/obsidian-rules.md's "Chapter-summary abstracts" for the full rule.}}

> [!info] 教材范围
> 书本 pp. {{book_page_range}}；PDF pp. {{pdf_page_range}}。

## 📋 章节结构

| 节 | 原章节标题 | 主要内容 |
|---|---|---|
| §{{N}}.1 | {{section_title}} | {{section_role}} |

## {{N}}.1 {{section_title}}

{{Faithfully explain how this section advances the chapter.}}

### 定义与记号

#### Definition {{label}}: {{definition_name_en}}（{{definition_name_zh}}）

{{Complete definition with all conditions and original notation, in English, phrased the way the source textbook itself would state it — not a machine translation of a Chinese draft. See ../../references/obsidian-rules.md's "Bilingual chapter-summary blocks" for the full rule and its scope.}}

> [!info] 教材出处
> §{{section}}，书本 p.{{book_page}}，PDF p.{{pdf_page}}。

### 定理、引理与推论

#### Theorem {{label}} — {{result_title_en}}（{{result_title_zh}}）

**Given:** {{all assumptions, in English}}

**Then:** {{complete conclusion, in English}}

**章节作用：** {{how the result advances the book's argument — this is the Agent's own commentary, stays Chinese}}

- [[{{proof_page}}|完整证明]]

> [!info] 教材出处
> §{{section}}，书本 pp. {{book_range}}，PDF pp. {{pdf_range}}。

### 备注、限制与反例

> [!warning] {{restriction_title}}
> {{Textbook-grounded restriction, counterexample, or necessary condition.}}

### 本节结论

{{State what has now been established and how the next section follows.}}

## 🧩 本章概念索引

| 概念 | 本章中的作用 | 首次位置 |
|---|---|---|
| [[{{concept_page}}]] | {{role}} | §{{section}} |

## 🔗 本章逻辑结构

```text
{{definition_or_prior_result}}
→ {{intermediate_result}}
→ {{main_result}}
→ {{consequence}}
```

## 📌 本章结论

{{Compress the chapter's established results in the author's order without adding exam advice.}}

## ⚠️ 摘要范围与验证

- 定义：{{status}}
- 定理编号与条件：{{status}}
- 公式：{{status}}
- 证明链接：{{status}}
- 页码映射：{{status}}
- 默认省略：常规例题、练习、重复计算、历史旁白
- 待复核：{{exact_items_or_none}}

## 🔗 相关

- 上一章：[[{{previous_chapter}}]]
- 下一章：[[{{next_chapter}}]]
- 核心概念：[[{{concept_1}}]]、[[{{concept_2}}]]

<!-- agent-managed:end -->

