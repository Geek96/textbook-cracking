<p align="center">
  <img src="https://img.shields.io/badge/AI_Agent-Skill-7C3AED?style=for-the-badge" alt="AI Agent Skill"/>
  <img src="https://img.shields.io/badge/version-0.1.0-10B981?style=for-the-badge" alt="Version 0.1.0"/>
  <img src="https://img.shields.io/github/license/Geek96/textbook-cracking?style=for-the-badge&color=6B7280" alt="MIT License"/>
</p>

<h1 align="center">📖 textbook-cracking</h1>

<p align="center">
  <strong>Deconstruct textbooks and textbook-like PDFs into a faithful, traceable Obsidian wiki</strong>
  <br/>
  <code>PDF → inspect → pilot → chapter summaries + detail pages → MOC</code>
  <br/><br/>
  Agent-first PDF reading — no required API, subscription, MCP server, or document-parsing service
</p>

<p align="center">
  <strong>English</strong>
</p>

---

## ✨ Features

- **Content-model driven** — math (proof-based), CS (concept + worked case
  study), and primary-source reader (document anthology) each get their own
  admission tests and compression policy, so the wiki mirrors how the
  *book itself* is actually organized instead of one generic template
  forced onto every subject
- **Faithful, not summarized-to-death** — preserves the author's chapter
  order, formal statements, remarks, counterexamples, and caveats; compresses
  by teaching density, never a mechanical word/percentage limit
- **Evidence-backed** — every claim traces back to a specific chapter,
  printed-page reference, and (when relevant) a verified PDF-page offset
- **Textbook content vs. agent expansion, clearly separated** — any added
  intuition or clarifying counterexample lives under a labeled
  `## 🧠 理解扩展` section, never mixed into what the textbook itself says
- **Never publishes the textbook's own exercises** — extracts exercise
  *location* metadata for cross-referencing, never the exercise text itself;
  optional Agent-*original* practice problems are a clearly separate,
  on-request-only page type
- **Agent-managed-region marker discipline** — only ever touches the
  sections of a wiki file it generated; your own handwritten notes in the
  same file are never touched
- **Structural validator, stdlib only** — `scripts/validate_wiki.py` checks
  page types, frontmatter, callouts, wikilinks, and managed-region markers
  after every Ingest
- **Optional CanvasManager integration** — when used inside a course
  directory already managed by
  [canvas-manager](https://github.com/Geek96/canvas-manager), nests its
  output under `wiki/textbook_breakdown/` instead of colliding with
  CanvasManager's own `wiki/course_content/`/`wiki/info/` folders — see
  `references/course-manager-integration.md`. Fully usable standalone too,
  with no CanvasManager involved at all.

---

## 📦 Installation

All files are plain `.md` skill instructions. Pick your agent below.

### Claude Code

```bash
npx skills add Geek96/textbook-cracking
```

### Other Agents

Any agent that can read Markdown skills and PDF files directly can use this
repository:

1. Clone the repo: `git clone https://github.com/Geek96/textbook-cracking.git`
2. Point the agent to `skills/textbook-cracking/SKILL.md` as the entry point.

---

## 🔧 Dependencies & Prerequisites

> **Required**: an agent that can read PDF files directly (Claude Code can).
> That's it — no API key, no subscription, no MCP server, no Obsidian
> plugin, no document-parsing service.

```
☐ An agent that can read PDF files directly
☐ The source PDF(s) you already legally have — this skill never downloads
   or sources a textbook on your behalf, free/legal releases included
```

**Optional, only if direct PDF reading fails on a specific book** (scanned
pages, unusual layout): an already-installed local parser (MinerU, Marker,
Docling, OCRFlux, or similar). The skill never installs one automatically —
if the pilot chapter shows direct reading isn't working, it will ask before
using or installing anything.

---

## 🧩 Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                     textbook-cracking                        │
│                                                               │
│   Inspect ──▶ Pilot ──▶ Ingest (per chapter) ──▶ Verify       │
│   detect        confirm    chapter summary +        check     │
│   content       structure  detail pages +        against      │
│   model         on a       MOC update             source      │
│                 sample                                        │
│                                                               │
│                         ▼                                     │
│              scripts/validate_wiki.py                         │
│              (structural check, stdlib only)                  │
└─────────────────────────────────────────────────────────────┘
```

| Mode | Use when |
|------|----------|
| **Inspect** | Source is new or its quality/structure is unknown |
| **Pilot** | Before the first full chapter — verify the content-model match on a sample |
| **Ingest** | Process one requested chapter at a time |
| **Update** | Incrementally maintain an existing textbook wiki |
| **Verify** | Check an already-ingested chapter against the source |

---

## 📚 Content Models

| Model | Typical book | Admitted units |
|-------|-------------|-----------------|
| **Math** | Proof-based mathematics (analysis, algebra, topology) | concept, proof |
| **CS** | Programming/CS textbooks built around concepts and worked code | concept, case-study |
| **Primary-source reader** | An edited anthology of historical/primary documents | document-entry |

*Not yet built: narrative reading (a novel, memoir, or other
sustained-narrative course text) — confirmed in scope, not yet designed.*

See `references/content-models/README.md` for how a book gets matched to a
model, and each model's own file for its exact admission tests and
compression policy.

---

## 📖 Example Prompts

```text
> Inspect this PDF and tell me what content model it fits
> Ingest chapter 3 of this textbook into my Obsidian vault
> Update the concept pages after I re-read chapter 5
> Verify chapter 2 against the source PDF
> Generate practice problems for the sections my course syllabus actually assigned
```

---

## 📁 Project Structure

```text
textbook-cracking/
├── skills/textbook-cracking/
│   ├── SKILL.md                          # skill entrypoint
│   ├── agents/openai.yaml                # non-Claude-Code agent config
│   ├── references/
│   │   ├── workflow.md                   # Inspect/Pilot/Ingest/Update/Verify
│   │   ├── content-models/
│   │   │   ├── README.md                 # how a book is matched to a model
│   │   │   ├── math.md
│   │   │   ├── cs.md
│   │   │   └── primary-source-reader.md
│   │   ├── obsidian-core.md              # portable Obsidian authoring baseline
│   │   ├── obsidian-rules.md             # domain-specific authoring rules
│   │   └── course-manager-integration.md # optional CanvasManager wiring
│   ├── templates/
│   │   ├── MOC-template.md               # shared across all models
│   │   ├── 概念-template.md               # shared across all models
│   │   ├── math/                         # 章节摘要, 证明, 练习题
│   │   ├── cs/                           # 章节摘要, 案例, 周次, 选择题*, 编程练习
│   │   └── primary-source-reader/        # 章节摘要, 文献条目
│   └── scripts/validate_wiki.py          # structural validator, stdlib only
├── .claude-plugin/plugin.json
└── README.md
```

---

## 📄 License

MIT © [Geek96](https://github.com/Geek96)
