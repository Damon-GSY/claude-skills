---
name: latex-examples
description: LaTeX 高质量表格与展示风格参考库。收集顶级论文中的表格 LaTeX 源码，提炼通用模式，教 AI 按照这些风格生成论文级别的 LaTeX 代码。当用户要求生成论文表格、对比实验表、消融实验表、排行榜表、或者提到"按论文风格生成 LaTeX"、"参考论文表格"时激活。也适用于用户发来 LaTeX 表格要求学习/收藏时。
---

# LaTeX 高质量表格与展示风格参考库

从 Damon 收藏的顶会论文中提取的 LaTeX 表格最佳实践。按这些模式生成论文级表格。

## 核心原则

1. **学习真实论文风格** — 每个 example 来自真实发表的论文，不是教科书示例
2. **提炼通用模式** — 从多个例子中抽象出可复用的模板
3. **按需加载** — 只在生成 LaTeX 表格时读取对应 example

## 文件结构

```
examples/       — 原始论文表格收藏（LaTeX 源码 + 点评）
patterns/       — 从 examples 中提炼的通用模板
```

## 何时读取哪个文件

| 用户需求 | 读取文件 |
|----------|---------|
| 方法对比表 / 排行榜表 | `patterns/comparison-table.md` |
| 消融实验表 | `patterns/ablation-table.md` |
| 多数据集多指标表（wide table） | `patterns/multi-dataset-table.md` |
| 收藏新的 LaTeX 表格 | `examples/` 目录 |
| 生成任何论文表格 | 先读对应 pattern，再参考具体 example |

## 收藏新表格的流程

1. 在 `examples/` 下创建 `{领域}-{简称}.md`
2. 包含：论文名称、领域、LaTeX 源码、**哪些设计决策值得学习**
3. 如果该表格体现了新的 pattern，在 `patterns/` 中添加对应模板

## 质量标准

收藏的表格应满足以下至少 3 条：
- ✅ 信息密度高（一眼看出关键结论）
- ✅ 视觉层次清晰（粗体、下划线、底色突出最优结果）
- ✅ 列数适中（不会横向溢出）
- ✅ 使用了高级 LaTeX 特性（multirow、multicolumn、rowcolor、resizebox、cmidrule）
- ✅ 最佳结果标注方式优雅（bold + underline + rowcolor）
