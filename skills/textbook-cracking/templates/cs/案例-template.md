---
type: case-study
title: "{{case_study_title}}"
aliases:
  - "{{case_study_title_original}}"
course: "{{course_id}}"
document_id: "{{document_id}}"
case_study_id: "{{case_study_id}}"
chapter: {{N}}
section: "{{section}}"
source_file: "{{source_file}}"
book_pages: "{{book_page_range}}"
pdf_pages: "{{pdf_page_range}}"
concepts:
  - "[[{{concept_page}}]]"
depends_on:
  - "[[{{prior_case_study_or_concept}}]]"
verification: {{verification}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
tags:
  - type/case-study
  - course/{{course_slug}}
---

# {{case_study_title}}

<!-- agent-managed:start id="textbook:{{document_id}}:case-study:{{case_study_id}}" -->

## 问题

{{What the textbook's case study sets out to build or solve, in the book's own framing.}}

## 完整代码

{{Faithfully reproduce the textbook's own code, verbatim — same names, same comments, same formatting. Never paraphrase code.}}

```{{language}}
{{verbatim_code_listing}}
```

## 讲解

{{Faithfully walk through the logic the way the textbook explains it — what each part does and why, following the book's own order of explanation, not a reorganized one.}}

## 输出示例

{{Reproduce the textbook's own sample output/run, if it supplies one. Delete this section if the book doesn't show one — do not fabricate expected output.}}

```text
{{sample_output}}
```

## 常见错误

> [!warning] {{pitfall_title}}
> {{A mistake or restriction the textbook itself flags in connection with this case study. Delete if the book doesn't flag one here.}}

## 🧠 理解扩展

> [!info] 内容来源
> 本节由 Agent 对该案例的结构进行整理，用于辅助理解，不属于教材原文。

{{Optional structural summary of the case study's approach, or an equivalent way to think about it. Delete when it adds no value.}}

## 🔗 教材位置

- 章节：[[{{chapter_page}}#{{case_study_heading}}|{{chapter_reference}}]]
- 书本页：pp. {{book_page_range}}
- PDF：[[../../../textbooks/{{source_file}}#page={{first_pdf_page}}|PDF p.{{first_pdf_page}}]]

> [!info] 验证状态
> {{State exactly what was checked — code reproduced verbatim and cross-checked character-for-character against the source, walkthrough matches the book's own explanation, output (if any) matches what the book shows — and list unresolved details.}}

<!-- agent-managed:end -->
