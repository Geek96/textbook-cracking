---
type: chapter-summary
title: "Chapter {{N}} - {{chapter_title_zh}}"
aliases:
  - "{{chapter_title_original}}"
course: "{{course_id}}"
document_id: "{{document_id}}"
chapter_id: "ch{{NN}}"
chapter_number: {{N}}
era: "{{era_or_date_range}}"
source_file: "{{source_file}}"
book_pages: "{{book_page_range}}"
pdf_pages: "{{pdf_page_range}}"
documents:
  - "[[{{document_entry_page}}]]"
concepts:
  - "[[{{theme_concept_page}}]]"
verification: {{verification}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
tags:
  - type/chapter-summary
  - course/{{course_slug}}
---

# Chapter {{N}} — {{chapter_title_zh}}

<!-- agent-managed:start id="textbook:{{document_id}}:chapter-{{NN}}" -->

> [!abstract] 时代/主题概述
> **一句话**：{{one sentence capturing the era/theme this chapter covers}}
>
> **本章文献**：
> - **{{doc_title}}**（{{date}}）— {{one-line significance}}
>
> **主题概念**（如有）：
> - **{{theme_concept}} ({{English}})** — {{one-line explanation}}
>
> {{Omit the 主题概念 block entirely when this chapter admits none — most will. See ../../references/obsidian-rules.md's "Chapter-summary abstracts" for the full rule.}}

> [!info] 教材范围
> 书本 pp. {{book_page_range}}；PDF pp. {{pdf_page_range}}。

## 📋 文献索引

来自本书目录的这一章完整篇目列表——`状态` 列如实反映哪些已经拆解、哪些还没有（"尚未摄取"是诚实状态，不是缺陷；见 `content-models/primary-source-reader.md` 的"Selective, by referenced document number"一节）。

| 编号 | 标题 | 年代 | 类型 | 状态 |
|---|---|---|---|---|
| {{doc_number}} | [[{{document_entry_page}}\|{{doc_title}}]] | {{date}} | {{doc_type}} | 已摄取 |
| {{doc_number}} | {{doc_title}} | {{date}} | {{doc_type}} | 尚未摄取 |

## 本章文献综述

{{Faithfully convey what this chapter's set of documents collectively shows about the era/theme, in the editor's own framing where one is given — not an Agent-invented thesis. If the book's chapter intro is thin, say so rather than padding it.}}

## 🧩 本章主题概念（如有）

{{Only include this section if a theme concept page was actually admitted per content-models/primary-source-reader.md's theme-admission test — most chapters will have none. Delete the section entirely rather than leaving it empty.}}

| 主题 | 在本章的体现 |
|---|---|
| [[{{theme_concept_page}}]] | {{role}} |

## 📌 本章结论

{{Compress what the chapter's documents collectively establish about the era/theme, in the editor's own order, without adding an Agent-invented historical thesis.}}

## ⚠️ 摘要范围与验证

- 文献条目：{{status}}
- 出处引文：{{status}}
- 编者导读：{{status}}
- 页码映射：{{status}}
- 默认省略：与本章无关的通用前言、纯文献目录性质的脚注
- 待复核：{{exact_items_or_none}}

## 🔗 相关

- 上一章：[[{{previous_chapter}}]]
- 下一章：[[{{next_chapter}}]]
- 主题概念（如有）：[[{{concept_1}}]]

<!-- agent-managed:end -->
