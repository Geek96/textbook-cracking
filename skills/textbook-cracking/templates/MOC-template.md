---
title: "{{textbook_title}} — Map of Content"
type: moc
course: "{{course_id}}"
document_id: "{{document_id}}"
source_file: "{{source_file}}"
edition: "{{edition}}"
language: "{{language}}"
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
tags:
  - type/moc
  - course/{{course_slug}}
---

# 🗺️ {{textbook_title}} — Map of Content

<!-- agent-managed:start id="textbook:{{document_id}}:moc" -->

> [!abstract] 教材 Wiki
> 本 Wiki 基于 {{authors}}《{{textbook_title}}》{{edition_label}}，当前包含 **{{chapter_count}} 篇章节摘要**、**{{concept_count}} 个概念页面**和 **{{proof_count}} 篇教材证明**。
> 最近更新：{{YYYY-MM-DD}}

## 📚 章节索引

| 章节 | 主题 | 教材范围 | 摘要 | 核心概念 | 证明 | 状态 |
|---|---|---|---|---|---:|---|
| Chapter {{N}} | {{chapter_title}} | pp. {{book_range}} | [[{{chapter_page}}]] | [[{{concept_1}}]]、[[{{concept_2}}]] | {{proof_total}} | {{status}} |

## 🧩 概念索引

| 概念 | 类型 | 首次定义 | 相关章节 |
|---|---|---|---|
| [[{{concept_page}}]] | {{concept_kind}} | §{{section}} | [[{{chapter_page}}]] |

## 🧾 证明索引

> [!abstract]- Chapter {{N}} — {{chapter_title}}
> - [[{{proof_page}}]]

## 🗺️ 知识结构

### {{knowledge_area}}

- [[{{concept_a}}]]
- [[{{concept_b}}]]

## ✅ Wiki 状态

| 项目 | 数量 |
|---|---:|
| 教材章节 | {{total_chapters}} |
| 已解析章节 | {{parsed_chapters}} |
| 已核验章节 | {{verified_chapters}} |
| 概念页面 | {{concept_count}} |
| 证明页面 | {{proof_count}} |
| 待复核项 | {{review_count}} |

## ⚠️ 待复核

- {{exact_review_item_or_none}}

<!-- agent-managed:end -->

