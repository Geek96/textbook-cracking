# Changelog

## 0.2.1

Documented this skill's role in **CourseOS**: the optional Content Driver
component (see [course-manager](https://github.com/Geek96/course-manager)'s
`FRAMEWORK.md`). Docs-only — also fixed a stale README example prompt
("generate practice problems...") left over from before that moved to
course-manager in 0.2.0.

## 0.2.0

**Breaking**: Agent-original practice-content generation moved to the
separate [`course-manager`](https://github.com/Geek96/course-manager)
skill — `练习题/` (math) and `选择题练习/`+`选择题答案/`+`编程练习/` (CS,
week-scoped) are no longer produced by this skill. That work is inherently
course-scoped (reading a specific course's syllabus or a professor's slide
deck to ground range and difficulty), not textbook deconstruction, so it
belongs with `course-manager`, which already sits at the intersection of
this skill's textbook coverage and canvas-manager's course evidence.

- Removed `templates/math/练习题-template.md`,
  `templates/cs/选择题练习-template.md`,
  `templates/cs/选择题答案-template.md`,
  `templates/cs/编程练习-template.md`.
- Removed the corresponding page types (`practice-problems`,
  `mcq-practice`, `mcq-answers`, `coding-practice`) from
  `scripts/validate_wiki.py`'s `ALLOWED_TYPES`.
- Removed the "Practice problems"/"Week practice" sections from
  `content-models/math.md` and `content-models/cs.md`, and the "Bilingual
  practice problems" section from `obsidian-rules.md`.
- `references/course-manager-integration.md`'s "Exercise handoff" section
  now documents the full ported rule set (scope grounding, calibration,
  bilingual/MCQ/coding-practice format) instead of a passing mention.

If you were relying on this skill to generate practice problems or week
practice, install `course-manager` alongside it — it reads this skill's
`wiki/textbook_breakdown/` read-only to generate the same content.

Week pages (`周次/`, mapping a professor's slides onto the book's
structure) are unaffected — that stays this skill's job.

## 0.1.0

Initial release: math, CS, and primary-source-reader content models;
Inspect/Pilot/Ingest/Update/Verify workflow; `scripts/validate_wiki.py`
structural validator; optional wiki-root nesting under a
CanvasManager-managed course's `wiki/textbook_breakdown/`.
