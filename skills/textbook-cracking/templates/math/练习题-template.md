---
type: practice-problems
title: "{{chapter_title}} - 练习题"
course: "{{course_id}}"
document_id: "{{document_id}}"
chapter: {{N}}
sections: ["{{section}}", "{{section}}"]
scope_source: "{{course-syllabus | full-chapter}}"
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
tags:
  - type/practice-problems
  - course/{{course_slug}}
---

# {{chapter_title}}：练习题

<!-- agent-managed:start id="textbook:{{document_id}}:practice-problems:{{chapter_id}}" -->

> [!abstract] 用法
> 每题都比章节摘要里直接陈述的定理多一步——要么要求从定义直接证（不许套用刚证过的结论），要么要求构造反例/边界情形，要么要求把两个结果接起来做一步综合。**不是教材自带习题**：全部由 Agent 原创，不逐字或近似照抄教材自己的习题（教材习题的处理属于 CourseManager 的 exercise handoff，见 `references/course-manager-integration.md`）。不含答案和提示，按章节顺序排列。
>
> **范围依据**：{{说明这份题目是按哪门课的实际大纲范围生成的，引用具体来源文件（如 CanvasManager 同步的课程政策页/PDF syllabus），还是没有课程语境、按本 Wiki 已摄取的教材全部范围生成——两种情况都要如实声明，不能含糊。}}

## §{{section}} {{section_title}}

1. {{中文题目}}
   *English: {{English translation}}*

2. {{中文题目}}
   *English: {{English translation}}*

<!-- agent-managed:end -->
