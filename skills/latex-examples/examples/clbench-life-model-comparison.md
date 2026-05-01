# CL-bench Life: Model Comparison Table

**论文**: CL-bench Life: A Benchmark for Real-Life Context Learning
**领域**: LLM Benchmarking / Context Learning
**来源**: Tencent Hunyuan & Fudan University (arXiv 2604.27043)

## 为什么收藏

这是一个**TikZ 内嵌渐变条 leaderboard 表格**，展示了以下高级技巧：

1. **`\gradientcellstd` 自定义 TikZ 宏** — 每个单元格内嵌一个灰度渐变条，宽度按数值比例缩放，同时显示 mean±std
2. **`tikzpicture[baseline]` 内联图形** — 将 TikZ 绘图嵌入表格单元格，保持与文本基线对齐
3. **`\makebox` 精确排版数值** — `\makebox[1.2em][r]{#1}` 和 `\makebox[0.8em][l]{#2}` 对齐 mean 和 std 的数字位
4. **`\makecell` 多行表头** — 列标题需要两行时使用 `\makecell{\textbf{...}\\ \textbf{...}}`
5. **`p{2cm}` 固定宽度列** — 每列用 `p{width}` 控制宽度，避免长标题溢出
6. **`\scalebox{0.84}` 整体缩放** — 适配双栏 `table*` 布局
7. **`\arraystretch` 行距控制** — 配合 TikZ 内嵌图形确保行高足够
8. **booktabs 三线表** — `\toprule` / `\midrule` / `\bottomrule` 保持干净

## LaTeX 源码

```latex
\newcommand{\gradientcellstd}[2]{%
    \begin{tikzpicture}[baseline]
        \fill[gray!25] (0,0) rectangle (0.9,0.3);
        \fill[gray!100] (0,0) rectangle ({0.9*#1/100},0.3);
        \node[anchor=west, font=\scriptsize] at (0.95,0.15) {
            \textbf{\makebox[1.2em][r]{#1}}\,{\tiny$\pm$}\,\makebox[0.8em][l]{#2}
        };
    \end{tikzpicture}%
}

\begin{table*}[t]
    \caption{
    Task solving rate of ten frontier LMs on CL-bench Life. 
    All models are evaluated in reasoning mode, with results reported as mean $\pm$ std (\%) across three runs.
    }
    \centering
    \small
    \scalebox{0.84}{
    \begin{tabular}{@{}l|>{\centering\arraybackslash}p{2cm}|>{\centering\arraybackslash}p{2.4cm}|>{\centering\arraybackslash}p{2.8cm}|>{\centering\arraybackslash}p{2.4cm}@{}}
    \toprule
    \multicolumn{1}{l|}{\textbf{Model Names}} &
    \multicolumn{1}{c|}{\textbf{Overall}} &
    \multicolumn{1}{c|}{\makecell{\textbf{Communication \&} \\ \textbf{Social Interactions}}} &
    \multicolumn{1}{c|}{\makecell{\textbf{Fragmented} \\ \textbf{Information \& Revisions}}} &
    \multicolumn{1}{c}{\makecell{\textbf{Behavioral Records \&} \\ \textbf{Activity Trails}}} \\
    \midrule

    GPT 5.4 (High) & \gradientcellstd{19.3}{0.5} & \gradientcellstd{22.2}{0.7} & \gradientcellstd{15.8}{0.9} & \gradientcellstd{20.0}{0.7} \\

    Claude Opus 4.6 (High) & \gradientcellstd{17.0}{1.3} & \gradientcellstd{21.7}{3.3} & \gradientcellstd{16.5}{0.9} & \gradientcellstd{12.8}{1.5} \\

    Gemini 3.1 Pro (High) & \gradientcellstd{16.9}{1.2} & \gradientcellstd{18.8}{1.7} & \gradientcellstd{13.6}{1.9} & \gradientcellstd{18.3}{1.5} \\

    Hy3 preview (High) & \gradientcellstd{15.7}{0.9} & \gradientcellstd{17.0}{2.1} & \gradientcellstd{15.9}{1.6} & \gradientcellstd{14.1}{2.1} \\

    Seed 2.0 Pro (High) & \gradientcellstd{15.5}{1.7} & \gradientcellstd{19.8}{2.3} & \gradientcellstd{12.1}{2.4} & \gradientcellstd{14.6}{1.1} \\

    Kimi K2.5 (High) & \gradientcellstd{13.2}{0.8} & \gradientcellstd{15.3}{1.1} & \gradientcellstd{11.4}{1.5} & \gradientcellstd{12.8}{0.4} \\

    Qwen 3.5 Plus (High) & \gradientcellstd{12.4}{0.1} & \gradientcellstd{13.1}{0.9} & \gradientcellstd{10.1}{1.1} & \gradientcellstd{14.1}{0.7} \\

    Grok 4.20 & \gradientcellstd{11.9}{0.4} & \gradientcellstd{12.8}{0.9} & \gradientcellstd{11.9}{1.5} & \gradientcellstd{10.9}{2.6} \\

    DeepSeek V3.2 Thinking & \gradientcellstd{9.5}{0.4} & \gradientcellstd{12.3}{1.1} & \gradientcellstd{7.7}{1.1} & \gradientcellstd{8.6}{1.7} \\

    MiniMax M2.5 & \gradientcellstd{6.3}{1.0} & \gradientcellstd{8.6}{2.1} & \gradientcellstd{5.2}{1.3} & \gradientcellstd{5.2}{1.3} \\

    \bottomrule
    \end{tabular}
    }
    \vspace{-1em}
    \label{tab:main_results}
\end{table*}
```

## 可复用的设计模式

### Pattern: TikZ 内嵌渐变条单元格
- 自定义 `\newcommand` 封装 TikZ 绘图逻辑，保持表格源码简洁
- `[baseline]` 选项确保 TikZ 图形与文本基线对齐
- 渐变条宽度按百分比缩放：`{0.9*#1/100}`
- 灰度双色方案：`gray!25`（背景条）+ `gray!100`（填充条）
- 数值与 std 使用 `\makebox` 对齐，保持列内数字整齐

### Pattern: 多行表头 + 固定列宽
- `\makecell{\textbf{...}\\ \textbf{...}}` 实现多行表头
- `>{\centering\arraybackslash}p{2cm}` 固定宽度 + 居中
- `\scalebox{0.84}` 配合 `table*` 控制整体大小

### 需要的宏包
```latex
\usepackage{tikz}
\usepackage{booktabs}
\usepackage{makecell}
\usepackage{graphicx}  % for \scalebox
```
