---
name: llm-wiki
description: Use when the user says /wiki, /digest, or asks to save/ingest/digest conversation knowledge into the persistent wiki. Also use when conversation contains valuable insights worth preserving for future sessions.
---

# LLM Wiki

将对话中的知识渐进式沉淀到 Obsidian wiki（`Area/My-wiki/`），让知识跨会话复利增长。

## 核心记录哲学：好奇心与意外感

**最重要的事：记录好奇心，而非仅仅记录知识。**

客观知识到处都能查到，但以下内容是真正属于你的、不可替代的：
- **什么让你感到意外**——某个事实打破了你的直觉，某个结果出乎意料
- **什么引发了你的好奇心**——你追问了"为什么？"、"怎么会这样？"的时刻
- **什么改变了你的认知**——对话前你以为 A，对话后你意识到其实是 B

在执行任何 wiki 操作时，优先捕捉这些维度。一个页面如果只记录了"XX 是什么"而缺少"为什么这让我意外/好奇"，那它是不完整的。

具体做法：
1. 对话摘要中必须有"**意外的发现**"段落——记录认知被刷新的瞬间
2. 概念页中必须有"**为什么值得关注**"——记录好奇心驱动的原因
3. 当你说"原来如此"、"没想到"、"有意思"这类反应时，这就是信号，必须捕捉

## Wiki 位置

```
Documents/myNotes/Area/My-wiki/
├── index.md           # 内容索引（每次操作后更新）
├── log.md             # 操作日志（append-only）
├── conversations/     # 对话摘要页
├── concepts/          # 概念页（原子级知识点）
├── topics/            # 主题页（领域/问题集合）
├── entities/          # 实体页（人、组织、工具）
└── synthesis/         # 综合分析页（跨话题深度合成）
```

## Properties 模板

每个页面必须包含以下 frontmatter：

```yaml
---
title: 页面标题
type: conversation | concept | topic | entity | synthesis
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [wiki/类型, 其他标签]
sources: "[[conversation-YYYY-MM-DD-简短标识]]"  # 来源对话
related: ["[[相关页面]]"]  # 双向链接
summary: 一句话摘要，供 index 和快速检索用
---
```

规则：
- `sources` 对于 conversation 页留空（它本身就是源）
- `related` 使用 Obsidian wikilinks，列出所有相关页面
- `summary` 不超过两行，必须能独立理解

## 调用时的操作流程

### Step 1: 分析对话

扫描当前对话，识别：
- 讨论了哪些**概念**（可独立理解的原子知识）
- 涉及哪些**主题**（多概念组成的领域/问题）
- 提到哪些**实体**（具体的人、工具、组织）
- 是否产生了**综合性洞察**（跨领域的发现或合成）
- **好奇心时刻**：用户在哪些地方表现出意外、好奇、认知被刷新（这是最高优先级的记录对象）

### Step 2: 生成对话摘要页

在 `conversations/` 下创建文件，命名格式：`YYYY-MM-DD-简短标识.md`

内容结构：
```markdown
# 对话主题

## 背景
为什么聊这个话题

## 关键讨论
- 要点1
- 要点2

## 结论与洞察
得出的核心结论

## 意外的发现
- [记录让你意外、好奇、认知被刷新的具体时刻]
- [对话前以为 X，实际是 Y 的认知转变]

## 衍生概念
- [[提取出的概念1]]
- [[提取出的概念2]]
```

### Step 3: 创建/更新概念、主题、实体页

**概念页**（`concepts/`）：用概念名做文件名。每个概念一页，内容包含定义、关键要点、与其他概念的关系。必须包含"**为什么值得关注**"段落——记录好奇心驱动的原因，为什么这个概念让你意外或产生追问。

**主题页**（`topics/`）：用主题名做文件名。聚合多个相关概念，形成领域视图。

**实体页**（`entities/`）：用实体名做文件名。记录关键属性和与知识体系的关系。

**如果页面已存在**：在末尾追加 `## 更新 [日期]` 段落，补充新信息，修正过时内容。**不要删除旧内容**——保留知识演变的轨迹。更新 `updated` 字段。

### Step 4: 更新 index.md

在对应分类下追加新页面条目，格式：
```markdown
- [[页面标题]] - summary 内容
```

更新统计数字。

### Step 5: 追加 log.md

在 `log.md` 末尾追加：
```markdown
## [YYYY-MM-DD] ingest | 对话标题

- 新建：[[conversations/...]], [[concepts/...]]
- 更新：[[existing-page]]
- 涉及 N 个概念，N 个主题
```

## 渐进式总结原则

知识有不同成熟度：

1. **对话摘要**（conversations/）：原始记录，保留讨论过程
2. **概念提炼**（concepts/）：从对话中提取的原子知识
3. **主题聚合**（topics/）：跨对话的概念整合
4. **综合分析**（synthesis/）：跨主题的深度合成，最高层

每次 ingest 时，检查是否需要将已有概念提升到更高层。例如：
- 同一概念在 3+ 次对话中出现 → 考虑创建/丰富对应的 topic 页
- 同一主题积累了足够深度 → 考虑写 synthesis

## 交叉引用规则

- 概念页之间用 `related` 互链
- 主题页链接其包含的概念
- 实体页链接相关概念和主题
- 对话摘要页链接提取出的所有概念/主题/实体
- 所有子页面通过 `sources` 指回来源对话

## 注意事项

- 使用 Obsidian wikilinks `[[页面名]]` 语法
- 文件名用英文或拼音，title 用中文
- summary 要写好——这是未来 RAG 检索的主要依据
- 不要过度拆分：一个概念如果太小不值得独立页面，就留在对话摘要里
- 先读 index.md 了解现有页面，避免重复创建
