# CL-bench Life: Error Analysis Table

**论文**: CL-bench Life: A Benchmark for Real-Life Context Learning
**领域**: LLM Benchmarking / Context Learning
**来源**: Tencent Hunyuan & Fudan University (arXiv 2604.27043)

## 为什么收藏

这是一个**TikZ 渐变条 + 描述性统计表**的简洁范例，展示了以下技巧：

1. **`\gradientcellerror` 渐变条宏** — 与 model comparison 表类似但更简洁，只显示单值（无 std），渐变条更宽（1.9 vs 0.9）
2. **`\makebox[\linewidth][c]{...}`** — 在 `p{}` 列中居中 TikZ 图形，确保渐变条在固定宽度列内完美居中
3. **`\addlinespace` 额外间距** — 在表头上下添加额外空白（`\addlinespace[0.7em]` / `\addlinespace[0.3em]`），提升视觉呼吸感
4. **简洁描述性表格风格** — 无 bold/underline 竞争性标注，因为这是描述性统计而非对比排行
5. **`\scalebox{0.86}` 适度缩放** — 比 model comparison 表更宽的列（p{2.3cm}），需要更小的缩放比例

## LaTeX 源码

```latex
\newcommand{\gradientcellerror}[1]{%
  \makebox[\linewidth][c]{%
    \begin{tikzpicture}[baseline]
      \fill[gray!25] (0,0) rectangle (1.9,0.3);
      \fill[gray!100] (0,0) rectangle ({1.9*#1/100},0.3);
      \node[anchor=west, font=\scriptsize] at (2,0.15) {%
        \textbf{\makebox[1.2em][r]{#1}}%
      };
    \end{tikzpicture}%
  }%
}

\begin{table*}[t]
\caption{
Distribution of error types across models.
Error types are non-mutually exclusive, a single failed solution may exhibit multiple error types.
The majority of solving failures are attributed to misusing knowledge in the context.
}
\centering
\small
\scalebox{0.86}{
\begin{tabular}{@{}l|>{\centering\arraybackslash}p{2.3cm}|>{\centering\arraybackslash}p{2.3cm}|>{\centering\arraybackslash}p{2.3cm}|>{\centering\arraybackslash}p{2.3cm}@{}}
\toprule
\addlinespace[0.7em]
\multicolumn{1}{l|}{\textbf{Model Names}} &
\multicolumn{1}{c|}{\makecell{\textbf{Context} \\ \textbf{Ignored(\%)}}} &
\multicolumn{1}{c|}{\makecell{\textbf{Context} \\ \textbf{Misused (\%)}}} &
\multicolumn{1}{c|}{\makecell{\textbf{Format} \\ \textbf{Error (\%)}}} &
\multicolumn{1}{c}{\textbf{Refusal (\%)}} \\
\addlinespace[0.3em]
\midrule

GPT 5.4 (High) & \gradientcellerror{36.0} & \gradientcellerror{79.7} & \gradientcellerror{13.2} & \gradientcellerror{1.5} \\

Claude Opus 4.6 (High) & \gradientcellerror{38.9} & \gradientcellerror{76.0} & \gradientcellerror{16.2} & \gradientcellerror{0.9} \\

Gemini 3.1 Pro (High) & \gradientcellerror{44.4} & \gradientcellerror{77.8} & \gradientcellerror{14.3} & \gradientcellerror{2.3} \\

Hy3 preview (High) & \gradientcellerror{35.2} & \gradientcellerror{84.2} & \gradientcellerror{10.9} & \gradientcellerror{0.9} \\

Seed 2.0 Pro (High) & \gradientcellerror{41.4} & \gradientcellerror{80.2} & \gradientcellerror{13.8} & \gradientcellerror{1.4} \\

Kimi K2.5 (High) & \gradientcellerror{45.3} & \gradientcellerror{80.2} & \gradientcellerror{12.7} & \gradientcellerror{1.1} \\

Qwen 3.5 Plus (High) & \gradientcellerror{45.1} & \gradientcellerror{76.9} & \gradientcellerror{13.0} & \gradientcellerror{2.0} \\

Grok 4.20 & \gradientcellerror{40.0} & \gradientcellerror{83.7} & \gradientcellerror{12.4} & \gradientcellerror{2.5} \\

DeepSeek V3.2 Thinking & \gradientcellerror{39.1} & \gradientcellerror{83.1} & \gradientcellerror{15.3} & \gradientcellerror{1.6} \\

MiniMax M2.5 & \gradientcellerror{43.5} & \gradientcellerror{84.4} & \gradientcellerror{13.4} & \gradientcellerror{0.8} \\

\bottomrule
\end{tabular}
}
\vspace{-1em}
\label{tab:error_types}
\end{table*}
```

## 可复用的设计模式

### Pattern: TikZ 渐变条（单值版）
- 与 mean±std 版本类似，但省略 std 显示，渐变条更宽
- `\makebox[\linewidth][c]{...}` 确保在 `p{}` 列内居中
- 渐变条宽度比例：`{1.9*#1/100}`，数值文字起始位置：`(2, 0.15)`

### Pattern: 描述性表格（非竞争性）
- 不使用 bold/underline 标注最优，因为这是分布统计而非排行榜
- 渐变条提供直观的大小对比，比纯数字更易读
- Caption 明确标注数据互斥性：non-mutually exclusive

### Pattern: `\addlinespace` 控制间距
- `\addlinespace[0.7em]` 在 caption 和表头之间留出呼吸空间
- `\addlinespace[0.3em]` 在表头和 `\midrule` 之间微调

### 需要的宏包
```latex
\usepackage{tikz}
\usepackage{booktabs}
\usepackage{makecell}
\usepackage{graphicx}  % for \scalebox
```
