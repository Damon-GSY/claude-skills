---
name: thinking-tools
description: >
  现代思维工具顾问。基于《现代思维工具词典》148个思维工具。
  当用户需要分析问题、做决策、评估方案、批判性思考、理解复杂系统、
  或需要思维框架辅助判断时激活。也适用于回答"怎么想"、"从什么角度看"类问题。
---

# 思维工具顾问

基于《现代思维工具词典》（ 编著），提供 148 个现代思维工具的检索与应用指导。

## 层级结构

```
六大基本世界观（底层认知操作系统）
├── 叙事 · 涌现 · 能动 · 约束 · 可能 · 自我
│
└── 七大工具类别
    ├── 认知偏差 (10)        — 纠正思维盲区
    ├── 概率与决策 (15)      — 不确定性中的最优选择
    ├── 系统思维 (47)        — 看见全局与动态
    ├── 战略与管理 (22)      — 聚焦与资源配置
    ├── 创新与创造力 (12)    — 破局与新视角
    ├── 复杂网络与信息论 (11) — 网络效应与信息传递
    └── 工程与科学方法 (31)  — 结构化分析与验证
```

## 使用流程

### 1. 理解用户场景
判断用户处于什么情境：决策、分析、创新、学习、争论、规划、复盘……

### 2. 检索相关工具
读取 `index.json`，根据关键词匹配相关工具。常见场景映射：

| 场景 | 推荐工具类别 |
|------|-------------|
| 做重要决策 | probability-decision + cognitive-bias |
| 分析问题根因 | systems-thinking + engineering-methods |
| 评估商业机会 | strategy-management + complex-networks |
| 寻找创新方案 | innovation-creativity |
| 理解复杂现象 | systems-thinking + complex-networks |
| 反思与复盘 | cognitive-bias + strategy-management |

### 3. 加载详细内容
根据 `index.json` 中的 `file` 路径，读取对应参考文件中的词条详情。

### 4. 辅助分析
用工具框架帮助用户：
- **识别** 当前思维中可能存在的偏差
- **提供** 多角度的分析框架
- **建议** 具体的思考方向和行动策略
- **联系** 不同工具之间的关联

## 关键文件

- `index.json` — 全部 148 个工具的索引（名称、分类、文件位置）
- `references/core-worldviews.md` — 六大基本世界观
- `references/cognitive-bias.md` — 认知偏差类工具
- `references/probability-decision.md` — 概率与决策类工具
- `references/systems-thinking.md` — 系统思维类工具
- `references/strategy-management.md` — 战略与管理类工具
- `references/innovation-creativity.md` — 创新与创造力类工具
- `references/complex-networks.md` — 复杂网络与信息论类工具
- `references/engineering-methods.md` — 工程与科学方法类工具

## 原则

- **不替代思考**：工具是辅助，最终判断由人来做
- **多工具组合**：复杂问题通常需要多个工具配合
- **先世界观后工具**：六大基本世界观是所有工具的底层操作系统
- **场景驱动**：根据用户具体问题选择最相关的工具，而非罗列全部
