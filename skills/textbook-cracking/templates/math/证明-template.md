---
type: proof
title: "{{result_label}} - {{result_title}} - 证明"
aliases:
  - "{{result_title}}的证明"
course: "{{course_id}}"
document_id: "{{document_id}}"
proof_id: "{{proof_id}}"
result_type: {{theorem_lemma_proposition_corollary}}
result_label: "{{result_label}}"
chapter: {{N}}
section: "{{section}}"
source_file: "{{source_file}}"
book_pages: "{{book_page_range}}"
pdf_pages: "{{pdf_page_range}}"
concepts:
  - "[[{{concept_page}}]]"
depends_on:
  - "[[{{prior_proof_or_concept}}]]"
verification: {{verification}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
tags:
  - type/proof
  - course/{{course_slug}}
---

# {{result_label}} — {{result_title}}

<!-- agent-managed:start id="textbook:{{document_id}}:proof:{{proof_id}}" -->

## 定理陈述

**条件：** {{all assumptions}}

**结论：** {{complete conclusion}}

## 证明

{{Faithfully reproduce every logical step of the textbook proof. Preserve direction splits, cases, constructions, equations, and cited earlier results. Do not add a missing proof from memory.}}

$$
{{verified_formula}}
$$

## 证明依赖

- [[{{prerequisite_concept}}]]
- [[{{prior_result_proof}}]]

## 🧠 证明结构

> [!info] 内容来源
> 本节由 Agent 对教材证明的结构进行整理，用于辅助理解，不属于教材原文。

1. {{optional_structural_step}}
2. {{optional_structural_step}}

## 🔗 教材位置

- 章节：[[{{chapter_page}}#{{result_heading}}|{{chapter_reference}}]]
- 书本页：pp. {{book_page_range}}
- PDF：[[{{source_file}}#page={{first_pdf_page}}|PDF p.{{first_pdf_page}}]]

> [!info] 验证状态
> {{State exactly what was checked and list unresolved details.}}

<!-- agent-managed:end -->

