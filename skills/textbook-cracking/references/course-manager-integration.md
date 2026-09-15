# CourseManager Integration

## Wiki root

Everywhere else in this skill, a `wiki/...` path is written as if `wiki/`
is the root. When the course directory already has CanvasManager's
`wiki/course_content/` + `wiki/info/` split, that's no longer true — use
`wiki/textbook_breakdown/` as your root instead, creating it if this is the
first textbook content synced for that course. So `wiki/MOC.md` becomes
`wiki/textbook_breakdown/MOC.md`, `wiki/概念/` becomes
`wiki/textbook_breakdown/概念/`, and so on for every path in this file and
in `SKILL.md`'s "Protect boundaries" section. Detect which root applies by
checking whether the course directory already has `wiki/course_content/`
or `wiki/info/` — if so, nest under `textbook_breakdown/`; if the course
directory has neither (a standalone vault with no CanvasManager involved
at all), `wiki/` itself stays the root.

## Responsibility boundary

Textbook Cracking owns textbook-derived pages only, under whichever wiki
root applies per above:

- `MOC.md`
- `章节摘要/`
- `概念/` (when the selected content model uses concepts)
- the selected content model's own detail-page folder(s) — `证明/` for math, `案例/` for CS, `文献/` for a primary-source reader; see `content-models/README.md`

CanvasManager owns Canvas evidence and course-source summaries. CourseManager owns `wiki/综合/`, deadline-aware synthesis, teacher-selected exercises, and cross-source study views.

## Source compatibility

Accept either a user-placed immutable file or a CanvasManager-downloaded attachment. Do not depend on Canvas-specific fields. At minimum identify:

- stable `source_id`;
- course directory;
- local file path;
- content hash when available;
- origin provider (`local` or `canvas`);
- immutable status.

Use namespaced identifiers such as:

```text
local:sha256:abc123
canvas:course-42:file-801
```

## Managed-region compatibility

Use the same `agent-managed` protocol as CanvasManager but with `textbook:` IDs. Multiple managers may contribute to one concept page only through distinct managed regions.

## Exercise handoff

Do not publish the textbook's own exercises. If chapter inspection detects exercise ranges, retain only enough internal location metadata for future matching. CourseManager may connect a Canvas assignment such as `§5.2 Exercises 2aceg` to the corresponding textbook range and publish the result under `wiki/综合/`.

This is separate from the optional `练习题/` practice-problems page type (math model — see `content-models/math.md`). Those pages are Agent-*original* problems, not the textbook's own exercises, so publishing them under `wiki/练习题/` doesn't violate "do not publish exercises." When generating them for a specific course, read that course's own syllabus material (CanvasManager-synced `课程政策`/`课程主页`, or a downloaded syllabus PDF under `raw/files/`) to find the actually assigned chapter/section range before writing — a whole-book Ingest routinely covers more than any one course's syllabus assigns, and the difference matters for what gets generated. Record the source of that range in the page's `scope_source` field.

## No planning behavior

Do not create calendar events, reminders, due dates, study schedules, or priority judgments. Those belong to CourseManager or PlanVault.

