# 多数据集多指标宽表格（Multi-Dataset Wide Table）

从 anomaly-mvtec 提炼。适用于多个实验设置 × 多个指标的宽表。

## 适用场景
- 同一方法在多个设置下测试（如 different continual learning settings）
- 多个数据集 × 多个指标
- 单元格内显示复合结果（如 "image / pixel"）

## 核心技巧

### 1. 双层表头

```latex
\multicolumn{1}{c|}{\multirow{2}{*}{Method}} 
  & \multicolumn{2}{c|}{\textbf{Setting A}} 
  & \multicolumn{2}{c|}{\textbf{Setting B}} \\ 
\cmidrule{2-5}
  & Metric1 ($\uparrow$) & Metric2 ($\downarrow$)
  & Metric1 ($\uparrow$) & Metric2 ($\downarrow$) \\ 
```

### 2. 复合数值（image-level / pixel-level）

```latex
& 85.7 / 89.3 & 18.3 / 13.1 \\
```

在 caption 中说明顺序：*"Image-level / Pixel-level results..."*

### 3. 竖线分组 + booktabs 表头

```latex
\begin{tabular}{c|cc|cc}
\toprule
...
\cmidrule{2-5}
...
\hline        % 方法分隔（不同于 booktabs 的 \midrule，用于方法行间分隔）
```

规则：**表头用 booktabs（`\toprule/\cmidrule/\bottomrule`），方法行间用 `\hline` + `\midrule` 分组。**

### 4. \scalebox 而非 \resizebox

```latex
\scalebox{0.80}{   % 保持宽高比，比 \resizebox{\textwidth}{!} 更适合宽表
\setlength{\tabcolsep}{2mm}  % 先缩列间距，再 scale
```

### 5. 特殊标注紧凑化

```latex
UCAD$*$\cite{ucad}        % 方法名后紧跟标记符号
```

在 caption 底部解释：*"$*$ indicates memory-limited"*

## Best/Second-best 混合标注

同一单元格可能在不同指标上分别是 best 和 second-best：

```latex
\textbf{96.4} / \textbf{96.6}        % 两个都是 best
\underline{93.8} / 95.7              % 左边 second-best，右边普通
93.5 / \underline{96.5}              % 左边普通，右边 second-best
```

**注意**：`{93.8}` 用花括号保护数值，防止 `\underline` 溢出到相邻列。
