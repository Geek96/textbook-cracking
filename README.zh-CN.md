<p align="center">
  <img src="https://img.shields.io/badge/AI_Agent-Skill-7C3AED?style=for-the-badge" alt="AI Agent Skill"/>
  <img src="https://img.shields.io/badge/version-0.2.1-10B981?style=for-the-badge" alt="Version 0.2.1"/>
  <img src="https://img.shields.io/github/license/Geek96/textbook-cracking?style=for-the-badge&color=6B7280" alt="MIT License"/>
</p>

<h1 align="center">📖 textbook-cracking</h1>

<p align="center">
  <strong>把教材和类教材 PDF 拆解成一份忠实、可溯源的 Obsidian wiki</strong>
  <br/>
  <code>PDF → 探查 → 试点 → 章节摘要 + 详情页 → MOC</code>
  <br/><br/>
  Agent 直接读 PDF——不需要 API、订阅、MCP server 或文档解析服务
</p>

<p align="center">
  <a href="README.md">English</a> | <strong>简体中文</strong>
</p>

---

## ✨ 特性

- **内容模型驱动** —— 数学（以证明为主）、CS（概念 + 实操案例研究）、原始文献读本（文献选集）各自有自己的收录标准和压缩策略，所以 wiki 映射的是**书本自身**的实际组织方式，而不是一个生搬硬套到所有学科的通用模板
- **忠实原著，而不是压缩到失真** —— 保留作者的章节顺序、正式表述、备注、反例与警示；压缩依据的是"教学密度"，而不是死板的字数/百分比限制
- **有据可查** —— 每一条内容都能追溯到具体章节、印刷页码，以及（相关时）经核实的 PDF 页码偏移
- **教材原文与 Agent 补充清晰分离** —— 任何补充的直觉解释或澄清性反例都放在标注清楚的 `## 🧠 理解扩展` 小节里，绝不和教材原文混在一起
- **从不发布教材自身的习题** —— 只提取习题的*位置*元数据用于交叉引用，绝不提取习题正文本身。Agent 原创的练习题/周练习生成是另一个独立的 [course-manager](https://github.com/Geek96/course-manager) skill 的职责（以课程为范围：读教学大纲或课件来确定范围/难度），不是本 skill 的工作——见 `references/course-manager-integration.md`
- **Agent 管理区域标记规则** —— 只触碰它自己生成的那部分内容；同一文件里你自己手写的笔记永远不会被碰
- **结构校验器，仅用标准库** —— `scripts/validate_wiki.py` 在每次 Ingest 之后检查页面类型、frontmatter、callout、wikilink 和管理区域标记
- **可选的 CanvasManager 集成** —— 当在一个已经由 [canvas-manager](https://github.com/Geek96/canvas-manager) 管理的课程目录里使用时，会把输出嵌套到 `wiki/textbook_breakdown/` 下，而不是和 CanvasManager 自己的 `wiki/course_content/`/`wiki/info/` 文件夹冲突——见 `references/course-manager-integration.md`。完全也可以独立使用，不涉及任何 CanvasManager。

---

## 🧱 CourseOS

在一个由 canvas-manager 管理的课程里，本 skill 承担的是 [CourseOS](https://github.com/Geek96/course-manager) 里可选的**内容驱动（Content Driver）**角色（见该仓库的 `FRAMEWORK.md`）——任何能读教材并产出 `references/course-manager-integration.md` 所定义的 `wiki/textbook_breakdown/` 结构的工具都可以顶替这个角色。这里的一切都不依赖于身处 CourseOS 之中；这层集成纯属可选。

---

## 📦 安装

所有文件都是纯 `.md` 格式的 skill 指令。根据你用的 agent 选择下面的方式。

### Claude Code

```bash
npx skills add Geek96/textbook-cracking
```

### 其他 Agent

任何能直接读 Markdown skill 和 PDF 文件的 agent 都可以使用这个仓库：

1. 克隆仓库：`git clone https://github.com/Geek96/textbook-cracking.git`
2. 让 agent 指向 `skills/textbook-cracking/SKILL.md` 作为入口。

---

## 🔧 依赖与前置条件

> **必需**：一个能直接读取 PDF 文件的 agent（Claude Code 可以）。
> 仅此而已——不需要 API key、不需要订阅、不需要 MCP server、不需要 Obsidian 插件、不需要文档解析服务。

```
☐ 一个能直接读取 PDF 文件的 agent
☐ 你已经合法拥有的源 PDF —— 本 skill 从不代你下载或获取教材，
   即使是免费/合法发布的版本也不例外
```

**可选，仅当某本书直接读取失败时才需要**（扫描页、异常排版）：一个已经装好的本地解析器（MinerU、Marker、Docling、OCRFlux 或类似工具）。本 skill 从不自动安装任何解析器——如果试点章节显示直接读取行不通，会先问过你再使用或安装任何东西。

---

## 🧩 工作流

```
┌─────────────────────────────────────────────────────────────┐
│                     textbook-cracking                        │
│                                                               │
│   探查(Inspect) ──▶ 试点(Pilot) ──▶ 摄取(Ingest，逐章) ──▶ 核验(Verify) │
│   识别内容模型      在样本章节上      章节摘要 +           对照原文    │
│                     确认结构          详情页 +              核对       │
│                                       更新 MOC                        │
│                                                               │
│                         ▼                                     │
│              scripts/validate_wiki.py                         │
│              （结构性检查，仅用标准库）                         │
└─────────────────────────────────────────────────────────────┘
```

| 模式 | 使用场景 |
|------|----------|
| **探查 Inspect** | 来源是新的，或者质量/结构还不确定 |
| **试点 Pilot** | 第一个完整章节之前——在样本上验证内容模型是否匹配 |
| **摄取 Ingest** | 一次处理一个要求的章节 |
| **更新 Update** | 增量维护一份已存在的教材 wiki |
| **核验 Verify** | 把已摄取的章节和原文核对 |

---

## 📚 内容模型

| 模型 | 典型书籍 | 收录单元 |
|-------|-------------|-----------------|
| **数学 Math** | 以证明为主的数学教材（分析、代数、拓扑） | concept、proof |
| **CS** | 围绕概念和实操代码案例组织的编程/CS 教材 | concept、case-study |
| **原始文献读本 Primary-source reader** | 历史/原始文献的编辑选集 | document-entry |

*尚未做的：叙事类阅读（小说、回忆录，或其他以连续叙事为主的课程文本）——确认在计划范围内，但还没设计。*

见 `references/content-models/README.md` 了解一本书是怎么被匹配到某个模型的，以及每个模型自己的文件了解其具体收录标准和压缩策略。

---

## 📖 示例提示词

```text
> 探查这份 PDF，告诉我它属于哪种内容模型
> 把这本教材的第 3 章摄取进我的 Obsidian vault
> 我重新读完第 5 章了，更新一下概念页
> 把第 2 章和原文 PDF 核对一下
```

---

## 📁 项目结构

```text
textbook-cracking/
├── skills/textbook-cracking/
│   ├── SKILL.md                          # skill 入口
│   ├── agents/openai.yaml                # 非 Claude Code agent 的配置
│   ├── references/
│   │   ├── workflow.md                   # Inspect/Pilot/Ingest/Update/Verify
│   │   ├── content-models/
│   │   │   ├── README.md                 # 一本书如何被匹配到某个模型
│   │   │   ├── math.md
│   │   │   ├── cs.md
│   │   │   └── primary-source-reader.md
│   │   ├── obsidian-core.md              # 可移植的 Obsidian 创作基线
│   │   ├── obsidian-rules.md             # 领域专属的创作规则
│   │   └── course-manager-integration.md # 可选的 CanvasManager/CourseManager 对接
│   ├── templates/
│   │   ├── MOC-template.md               # 所有模型共用
│   │   ├── 概念-template.md               # 所有模型共用
│   │   ├── math/                         # 章节摘要, 证明
│   │   ├── cs/                           # 章节摘要, 案例, 周次
│   │   └── primary-source-reader/        # 章节摘要, 文献条目
│   └── scripts/validate_wiki.py          # 结构校验器，仅用标准库
├── .claude-plugin/plugin.json
└── README.md
```

---

## 📄 License

MIT © [Geek96](https://github.com/Geek96)
