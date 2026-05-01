# CL-bench Life: Subcategory Breakdown Table

**论文**: CL-bench Life: A Benchmark for Real-Life Context Learning
**领域**: LLM Benchmarking / Context Learning
**来源**: Tencent Hunyuan & Fudan University (arXiv 2604.27043)

## 为什么收藏

这是一个**多层分组列 + 分类色系 cell shading 表格**，展示了以下高级技巧：

1. **三色分组 cell shading** — 三大类各自定义颜色：`mygreen`（Communication）、`myorange`（Fragmented Info）、`mypink`（Behavioral Records），视觉上一眼区分
2. **`\cellcolor` 强度映射** — 自定义 `\orcell` / `\grcell` / `\pkcell` 宏，根据数值大小自动计算颜色浓度（`\boost` 宏将百分比映射到 0-100 色阶）
3. **`\capval` 安全上限** — 防止 `\cellcolor` 的百分比参数超过 100（`\ifnum#1>100 100\else#1\fi`）
4. **`\multirow{2}{*}` + `\multicolumn{3}{c}` 三层表头** — 第一层：Model；第二层：3 个分类标题（跨 3 列）；第三层：9 个子分类标题
5. **`\cmidrule(lr){2-4}`** — `lr` 选项在分隔线两端留白，避免与相邻分隔线重叠
6. **`\resizebox{\textwidth}{!}{...}`** — 自动缩放到文本宽度，比 `\scalebox` 更灵活（不需要手动调比例）
7. **`\arraystretch{1.2}`** — 增加行距，配合 cell shading 提升可读性
8. **`\tabcolsep` 全局调整** — `\setlength{\tabcolsep}{5pt}` 让宽表格更紧凑

## LaTeX 源码

```latex
\definecolor{mygreen}{HTML}{DCE6F2}
\definecolor{myorange}{HTML}{FBE3C6}
\definecolor{mypink}{HTML}{F6D0D0}

\newcommand{\capval}[1]{\ifnum#1>100 100\else#1\fi}
\newcommand{\boost}[1]{\number\numexpr (#1*11)/10 \relax}

\newcommand{\orcell}[2]{\cellcolor{myorange!\capval{\boost{#1}}}#2}
\newcommand{\grcell}[2]{\cellcolor{mygreen!\capval{\boost{#1}}}#2}
\newcommand{\pkcell}[2]{\cellcolor{mypink!\capval{\boost{#1}}}#2}

\begin{table*}[t]
\caption{
Task solving rates across nine subcategories for all models. Columns are grouped by category. Cell shading indicates relative accuracy within each subcategory column, with darker cells indicating stronger performance.
}
\centering

\normalsize
\setlength{\tabcolsep}{5pt}
\renewcommand{\arraystretch}{1.2}

\resizebox{\textwidth}{!}{%
\begin{tabular}{@{}l*{9}{>{\centering\arraybackslash}p{2.0cm}}@{}}
\toprule
\multirow{2}{*}{\textbf{Model}}
& \multicolumn{3}{c}{\textbf{\makecell{Communication \&\\Social Interactions}}}
& \multicolumn{3}{c}{\textbf{\makecell{Fragmented Information\&\\Revisions}}}
& \multicolumn{3}{c}{\textbf{\makecell{Behavioral Records\&\\Activity Trails}}} \\

\cmidrule(lr){2-4} \cmidrule(lr){5-7} \cmidrule(lr){8-10}

 & \textbf{\makecell{Comm.\\Inter.}} & \textbf{\makecell{Group\\Conv.}} & \textbf{\makecell{Private\\Conv.}} & \textbf{\makecell{Pers. Info.\\Frag.}} & \textbf{\makecell{Pub. Info.\\Frag.}} & \textbf{\makecell{Create \&\\ Rev.}} & \textbf{\makecell{Game\\Logs}} & \textbf{\makecell{Digital FP\\\& Daily}} & \textbf{\makecell{Self-Trk.\\Traj.}} \\

\midrule

GPT 5.4 (High)
& \grcell{60}{20.7} & \grcell{65}{30.4} & \grcell{40}{15.6}
& \orcell{45}{14.8} & \orcell{65}{20.0} & \orcell{40}{12.6}
& \pkcell{60}{30.4} & \pkcell{65}{19.3} & \pkcell{65}{10.4} \\

Claude Opus 4.6 (High)
& \grcell{45}{16.3} & \grcell{60}{28.1} & \grcell{65}{20.7}
& \orcell{45}{14.8} & \orcell{50}{14.8} & \orcell{65}{20.0}
& \pkcell{35}{17.8} & \pkcell{40}{13.3} & \pkcell{45}{7.4} \\

Gemini 3.1 Pro (High)
& \grcell{30}{10.4} & \grcell{60}{28.9} & \grcell{50}{17.0}
& \orcell{30}{10.4} & \orcell{40}{11.9} & \orcell{60}{18.5}
& \pkcell{65}{34.1} & \pkcell{50}{15.6} & \pkcell{30}{5.2} \\

Hy3 preview (High)
& \grcell{40}{14.4} & \grcell{45}{22.2} & \grcell{35}{14.4}
& \orcell{65}{20.0} & \orcell{45}{13.3} & \orcell{45}{14.4}
& \pkcell{45}{23.3} & \pkcell{35}{12.2} & \pkcell{40}{6.7} \\

Seed 2.0 Pro (High)
& \grcell{65}{23.0} & \grcell{55}{26.7} & \grcell{15}{9.6}
& \orcell{30}{10.4} & \orcell{45}{14.1} & \orcell{40}{11.9}
& \pkcell{50}{24.4} & \pkcell{30}{11.1} & \pkcell{50}{8.1} \\

Kimi K2.5 (High)
& \grcell{30}{9.6} & \grcell{50}{23.7} & \grcell{30}{12.6}
& \orcell{30}{11.1} & \orcell{30}{9.6} & \orcell{45}{13.3}
& \pkcell{35}{17.8} & \pkcell{35}{11.9} & \pkcell{55}{8.9} \\

Qwen 3.5 Plus (High)
& \grcell{40}{13.3} & \grcell{25}{14.8} & \grcell{20}{11.1}
& \orcell{30}{11.1} & \orcell{25}{7.4} & \orcell{40}{11.9}
& \pkcell{40}{20.7} & \pkcell{50}{15.6} & \pkcell{35}{5.9} \\

Grok 4.20
& \grcell{30}{10.4} & \grcell{30}{16.3} & \grcell{25}{11.9}
& \orcell{40}{13.3} & \orcell{40}{12.6} & \orcell{30}{9.6}
& \pkcell{35}{15.6} & \pkcell{40}{13.3} & \pkcell{20}{3.7} \\

DeepSeek V3.2 Thinking
& \grcell{25}{7.4} & \grcell{30}{17.0} & \grcell{30}{12.6}
& \orcell{20}{8.1} & \orcell{25}{8.1} & \orcell{20}{6.7}
& \pkcell{30}{12.6} & \pkcell{15}{7.4} & \pkcell{35}{5.9} \\

MiniMax M2.5
& \grcell{15}{4.4} & \grcell{15}{10.4} & \grcell{20}{11.1}
& \orcell{15}{6.7} & \orcell{15}{4.4} & \orcell{15}{4.4}
& \pkcell{15}{5.2} & \pkcell{15}{7.4} & \pkcell{15}{3.0} \\

\bottomrule
\end{tabular}%
}
\vspace{-1em}
\label{tab:subcategory_breakdown}
\end{table*}
```

## 可复用的设计模式

### Pattern: 分组色系 cell shading
- 为每个分组定义独立颜色（HTML 色值）：`mygreen`、`myorange`、`mypink`
- 自定义宏接收 **色阶值 + 显示值**：`\grcell{60}{20.7}` — 60 是色阶（决定颜色深浅），20.7 是显示数值
- `\boost` 宏将原始百分比线性映射到色阶范围（这里用了 `*11/10` 放大差异）
- `\capval` 防御性编程，确保 `\cellcolor` 百分比不超过 100

### Pattern: 三层分组列头
- 第一层：`\multirow{2}{*}{Model}`
- 第二层：`\multicolumn{3}{c}{...}` 分类标题
- 第三层：各子分类标题
- `\cmidrule(lr){2-4}` 带 `lr` 间距的多段分隔线

### Pattern: 自适应宽表格
- `\resizebox{\textwidth}{!}{...}` 自动缩放到文本宽度
- `\setlength{\tabcolsep}{5pt}` + `\renewcommand{\arraystretch}{1.2}` 控制紧凑度和可读性

### 需要的宏包
```latex
\usepackage{tikz}
\usepackage{booktabs}
\usepackage{makecell}
\usepackage{multirow}
\usepackage{graphicx}  % for \resizebox
\usepackage{colortbl}   % for \cellcolor
\usepackage{xcolor}     % for \definecolor
```
