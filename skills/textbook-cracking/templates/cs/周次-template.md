---
type: week
title: "Week {{N}} - {{week_topic_zh}}"
aliases:
  - "{{week_topic_original}}"
course: "{{course_id}}"
document_id: "{{document_id}}"
week_number: {{N}}
date_range: "{{date_range}}"
source_files:
  - "{{slide_deck_filename}}"
chapters:
  - "[[{{chapter_page}}]]"
concepts:
  - "[[{{concept_page}}]]"
case_studies:
  - "[[{{case_study_page}}]]"
verification: {{verification}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
tags:
  - type/week
  - course/{{course_slug}}
---

# Week {{N}} — {{week_topic_zh}}

<!-- agent-managed:start id="textbook:{{document_id}}:week-{{NN}}" -->

> [!abstract] 本周概述
> **一句话**：{{one sentence capturing what this week's slides actually teach}}
>
> **本周技术要点**：
> - **{{topic}} ({{English}})** — {{one-line, and whether it's covered by an existing book page or newly explained here}}
>
> **对应书本**：{{chapter_page links}}（{{note if this week required newly ingesting a chapter}}）

> [!info] 来源
> 幻灯片：{{slide deck filename(s)}}（`raw/files/{{file_id}}/`）。本页只收录技术/知识内容——课程行政信息（日程、评分、Office Hours 等）见课程自己的 info 页面，不在这里重复。

## 📋 幻灯片大纲

| 主题 | 幻灯片是否详细讲解 | 处理方式 |
|---|---|---|
| {{topic}} | {{详细 / 仅列标题}} | {{链接到 [[concept_page]] / 本页 Agent 补充讲解}} |

## {{topic_1}}

{{If covered by the book: a short bridging note on how the professor's framing compares to/extends the book, then the link. If not covered BY THE BOOK, OR the slide is bare-outline only (see content-models/cs.md's Week pages section — it's an OR, not an AND: either condition alone is enough), write the explanation here directly instead.}}

- [[{{concept_page}}]]（{{仅当本主题确实由这个概念页覆盖时才放这行；如果本主题一部分有链接、一部分需要 Agent 补写，两块可以在同一个 H2 下分成两段并存——不必强行只选一种处理方式，见下方 Agent 补充讲解框}}）

> [!important] 📝 Agent 补充讲解
> {{当本主题（或本主题的一部分）不属于书本已覆盖内容，或者幻灯片只列了标题没有展开时，都需要这个框——两个条件满足一个就够，不要求同时成立。清楚说明：这段内容不是教授幻灯片原文，是 Agent 根据幻灯片提到的主题名 + 自身知识补写的，帮助理解，仅供参考——不能当作教授课堂上实际讲过的原话。}}

## 🔗 对应书本章节与概念

| 幻灯片主题 | 对应章节 | 对应概念/案例 |
|---|---|---|
| {{topic}} | [[{{chapter_page}}]] | [[{{concept_or_case_study_page}}]] |

## 🔗 相关

- 上一周：[[{{previous_week}}]]
- 下一周：[[{{next_week}}]]
- 涉及章节：[[{{chapter_1}}]]、[[{{chapter_2}}]]

<!-- agent-managed:end -->
