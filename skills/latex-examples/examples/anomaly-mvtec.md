# MVTec Continual Anomaly Detection (CDAD)

**论文**: CDAD — Continual Defect Anomaly Detection
**领域**: 异常检测 / 工业质检
**来源**: MVTec AD benchmark

## 为什么收藏

这是一个**宽表格（table*）的典范**，展示了以下高级技巧：

1. **`\scalebox{0.80}` 整体缩放** — 比 `\resizebox` 更适合 `table*`（双栏表格），保持宽高比
2. **`multirow` + `multicolumn` 双层表头** — 第一层是实验设置名称，第二层是指标名
3. **`\cmidrule{2-9}` 部分线** — 只画中间列的分割线，不横跨整个表格
4. **Best / Second-best 双重标注** — `\textbf` 粗体 = best，`\underline` 下划线 = second-best
5. **`\rowcolor{RGB}{230,230,230}` 灰色底** — 自己的方法用灰色行高亮
6. **`\hline` vs `\midrule` 混用** — 表头用 `\toprule/\cmidrule/\bottomrule`，方法分组用 `\hline` + `\midrule`
7. **双数值格式** — 每个单元格显示 "image-level / pixel-level" 两个结果
8. **标记符号** — `$\dag$` 表示 diffusion model，`$*$` 表示 memory-limited
9. **`\uparrow` / `$\downarrow$`** — 在列标题中标注指标方向（越高越好 / 越低越好）
10. **`\setlength{\tabcolsep}{2mm}`** — 微调列间距，让宽表格更紧凑

## LaTeX 源码

```latex
\begin{table*}[]
\centering
\scalebox{0.80}{
\setlength{\tabcolsep}{2mm}
\begin{tabular}{c|cc|cc|cc|cc}
\toprule
\multicolumn{1}{c|}{\multirow{2}{*}{Method}}             & \multicolumn{2}{c|}{\textbf{14 -- 1 with 1 Step}} & \multicolumn{2}{c|}{\textbf{10 -- 5 with 1 Step}} & \multicolumn{2}{c|}{\textbf{3 × 5 with 5 Steps}} & \multicolumn{2}{c}{\textbf{10 -- 1 × 5 with 5 Steps}} \\ \cmidrule{2-9} 
                              & \textbf{A-AUROC ($\uparrow$)}            & \textbf{FM ($\downarrow$)}                 & \textbf{A-AUROC ($\uparrow$)}              & \textbf{FM ($\downarrow$)}                 & \textbf{A-AUROC ($\uparrow$)}              & \textbf{FM ($\downarrow$)}                 & \textbf{A-AUROC ($\uparrow$)}                & \textbf{FM ($\downarrow$)}                   \\ \hline
UniAD\cite{uniad}                 & 85.7 / 89.6        & 18.3 / 13.3          & 86.7 / 91.5          & 14.9 / 10.6          & 81.3 / 88.7          & 7.4 / 10.6           & 76.6 / 82.3            & 21.1 / 17.3            \\
UniAD  + EWC\cite{ewc}  & 92.8 / 95.4        & 4.1 / 1.9            & 90.5 / 93.6          & 7.3 / 4.2            & 79.6 / 89.0          & 9.5 / 10.1           & 89.6 / 93.8            & 5.4 / 3.6              \\
UniAD  + SI\cite{si}   & 85.7 / 89.5        & 18.4 / 13.4          & 84.1 / 88.3          & 20.2 / 17.0          & 81.9 / 88.5          & 7.0 / 10.8           & 77.9 / 82.0            & 19.5 / 17.7            \\
UniAD  + MAS\cite{mas}   & 85.8 / 89.6        & 18.1 / 13.3          & 86.8 / 91.0          & 14.9 / 11.6          & 81.5 / 89.0          & 7.2 / 10.2           & 77.9 / 82.0            & 19.5 / 17.7            \\
UniAD  + LVT\cite{lvt} & 80.4 / 86.0        & 29.1 / 20.6          & 87.1 / 90.6          & 14.1 / 12.3          & 80.4 / 88.6          & 8.6 / 10.6           & 78.2 / 88.3            & 19.1 / 16.1            \\

UCAD$*$\cite{ucad}                          & {93.8} / 95.7        & 1.8 / 0.3            & 88.7 / 93.1          & 5.2 / \underline{3.7}            & \underline{84.8} / {90.1}          & {10.3} / 9.2           & {91.2} / {94.0}            & {6.3} / {3.0}              \\ 

IUF\cite{iuf}                          & \underline{96.0} / 96.3        & \underline{1.0} / 0.6            & 92.2 / \underline{94.4}          & 9.3 / 4.3            & {84.2} / \underline{91.1}          & \underline{10.0} / 8.4           & \underline{94.2} / \underline{95.1}            & \underline{3.2} / \underline{1.0}              \\ 

\midrule
DiAD$\dag$\cite{diad}                          & 93.5 / \underline{96.5}        & 1.7 / \underline{0.1}           & 91.9 / {93.9}          & 3.2 / 3.9           & {80.5} / 89.0          & {11.8} / \underline{7.2}           & 83.3 / 92.7            & 12.2 / 3.6             \\
ControlNet$\dag$\cite{controlnet}                    & 92.6 / 96.4        & 3.6 / \underline{0.1}            & \underline{92.7} / 93.8          & \underline{2.9} / 4.0            & 79.2 / {89.6}          & 13.9 / 7.3           & 82.6 / 91.8            & 13.5 / 4.5             \\ \midrule 
\rowcolor[RGB]{230,230,230}
\textbf{CDAD}$\dag$                         & \textbf{96.4} / \textbf{96.6}        & \textbf{-0.57} / \textbf{-0.04}        & \textbf{94.2} / \textbf{95.3}          & \textbf{2.05} / \textbf{2.40}          & \textbf{89.1} / \textbf{92.2}          & \textbf{3.69} / \textbf{4.65}          & \textbf{94.9} / \textbf{95.7}            & \textbf{1.01} / \textbf{0.74}            \\ \bottomrule
\end{tabular}
}
\caption{Image-level/pixel-level results of our method on MVTec under 4 continual anomaly detection settings. The best and second-best results are marked in \textbf{blod} and \underline{underline}. $\dag$ indicates DM-based methods, and $*$ indicates memory-limited.}
\vspace{-5pt}
\label{mvtec}
\end{table*}
```

## 可复用的设计模式

### Pattern: 多设置 × 多指标宽表格
- 使用 `table*` 跨双栏
- 双层表头：`\multirow{2}{*}` + `\multicolumn{2}{c|}`
- `\cmidrule(lr){2-9}` 局部分割线
- `\scalebox{0.80}` 整体缩放
- `\setlength{\tabcolsep}{2mm}` 紧凑列间距
- Best/2nd: `\textbf` / `\underline`
- 自己的方法：`\rowcolor` + `\textbf`
- 标记能力差异：`$\dag$`、`$*$` 在方法名后标注
- 指标方向：`($\uparrow$)` / `($\downarrow$)` 在表头
