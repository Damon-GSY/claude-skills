# 方法对比表（Comparison Table）

从 stereo-eth3d 和 anomaly-mvtec 提炼的通用方法对比表模板。

## 适用场景
- SOTA 对比实验
- 排行榜式结果展示
- 多个方法在相同 benchmark 上的比较

## 模板

### 窄表（单栏，方法数 ≤ 12）

```latex
\begin{table}[tbh]
\centering
\def\mywidth{0.4\textwidth}
\resizebox{\mywidth}{!}{
\begin{tabular}{lcccc}
\toprule
Method & Metric1 ($\downarrow$) & Metric2 ($\downarrow$) & Metric3 ($\downarrow$) & Metric4 ($\downarrow$) \\
\midrule
MethodA~\cite{a} & 5.94 & 1.83 & 0.19 & 92.1 \\
MethodB~\cite{b} & 3.58 & 0.98 & 0.13 & 95.2 \\
...
\rowcolor[rgb]{0.886,0.937,0.855} \textbf{Ours} & \textbf{1.26} & \textbf{0.26} & \textbf{0.09} & \textbf{98.7} \\
\bottomrule
\end{tabular}
}
\vspace{-8pt}
\caption{Results on Benchmark. Our method achieves the best performance.}
\vspace{-15pt}
\end{table}
```

### 宽表（双栏，方法数多或多指标）

```latex
\begin{table*}[]
\centering
\scalebox{0.80}{
\setlength{\tabcolsep}{2mm}
\begin{tabular}{c|cc|cc|cc}
\toprule
\multicolumn{1}{c|}{\multirow{2}{*}{Method}} 
  & \multicolumn{2}{c|}{\textbf{Dataset A}} 
  & \multicolumn{2}{c|}{\textbf{Dataset B}} 
  & \multicolumn{2}{c}{\textbf{Dataset C}} \\ 
\cmidrule{2-7}
  & Metric1 ($\uparrow$) & Metric2 ($\downarrow$)
  & Metric1 ($\uparrow$) & Metric2 ($\downarrow$)
  & Metric1 ($\uparrow$) & Metric2 ($\downarrow$) \\ 
\hline
MethodA~\cite{a} & 85.7 & 18.3 & 86.7 & 14.9 & 81.3 & 7.4 \\
MethodB~\cite{b} & \underline{93.8} & \underline{1.8} & 88.7 & 5.2 & \underline{84.8} & \underline{10.0} \\
\midrule
\rowcolor[RGB]{230,230,230}
\textbf{Ours} & \textbf{96.4} & \textbf{1.0} & \textbf{94.2} & \textbf{2.1} & \textbf{89.1} & \textbf{3.7} \\
\bottomrule
\end{tabular}
}
\caption{...}
\label{tab:xxx}
\end{table*}
```

## 关键设计决策清单

| 决策 | 推荐 | 理由 |
|------|------|------|
| 最佳结果标注 | `\textbf` + `\rowcolor` | 视觉突出 |
| 次佳标注 | `\underline` | 与最佳区分 |
| 表宽控制 | 窄表用 `\resizebox`，宽表用 `\scalebox` | 避免溢出 |
| 双层表头 | `\multirow` + `\multicolumn` + `\cmidrule` | 多数据集时必需 |
| 列间距 | `\setlength{\tabcolsep}{2mm}` | 宽表更紧凑 |
| 垂直间距 | `\vspace{-8pt}` after table, `\vspace{-15pt}` after caption | 节省空间 |
| 自己的方法位置 | 表格最后一行 + `\midrule` 分隔 | 读者先看到 baseline，最后看到 ours |
| 分组线 | 同类方法无分隔，跨类用 `\midrule` | 清晰但不杂乱 |
| 标记符号 | `$\dag$`、`$*$` 在方法名后，caption 中解释 | 不占列 |
| 指标方向 | `($\uparrow$)` / `($\downarrow$)` 在表头 | 读者不需要猜 |
| 负数显示 | 直接显示如 `-0.57`，不是 `0.57 ↓` | 更专业 |

## 常用 LaTeX 包

```latex
\usepackage{booktabs}     % \toprule, \midrule, \bottomrule, \cmidrule
\usepackage{multirow}     % \multirow
\usepackage{graphicx}     % \resizebox, \scalebox
\usepackage{colortbl}     % \rowcolor, \cellcolor
\usepackage{xcolor}       % \definecolor
\usepackage{amssymb}      % \checkmark
```

## 避免

- ❌ 不要用 `\hline` 代替 `\toprule/\midrule/\bottomrule`（booktabs 更专业）
- ❌ 不要在 `table*` 中用 `\resizebox`（变形严重，用 `\scalebox`）
- ❌ 不要用竖线 `|` 在窄表中（booktabs 风格不用竖线），但宽表分组时 `c|cc|cc` 是可接受的
- ❌ 不要把 caption 写太长，控制在 2 行内
- ❌ 不要在每个数字后加 `\\` 以外的多余空格
