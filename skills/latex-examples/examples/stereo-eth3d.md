# ETH3D Stereo Matching Leaderboard

**论文**: Stereo Foundation Model (finetuned version)
**领域**: 立体匹配 / Stereo Matching
**来源**: ETH3D benchmark test set

## 为什么收藏

这是一个**简洁的排行榜式对比表**，展示了以下优秀设计：

1. **`\resizebox` 控制宽度** — 用 `\def\mywidth{0.4\textwidth}` 定义，确保表格不超页
2. **最佳结果三重标注** — `\rowcolor` 高亮行 + `\textbf` 粗体 + 逻辑分组
3. **Zero-Shot vs Fine-tuned 分组** — 用 `\midrule` 分隔，同一方法两个版本相邻排列
4. **`✓/✗` 符号标注能力** — Zero-Shot 用 `\redxmark`，Fine-tuned 全是 ✗（统一标记 unavailable）
5. **多指标对比** — BP-0.5、BP-1.0、EPE 三个指标，全是越低越好
6. **caption 信息丰富** — 说明了哪些方法用了训练集、排名情况、zero-shot 说明

## LaTeX 源码

```latex
\begin{table}[tbh]
\centering
\def\mywidth{0.4\textwidth} 
\definecolor{green}{RGB}{0,200,0}
\resizebox{\mywidth}{!}{

\begin{tabular}{lcccc}
\toprule
Method                         & Zero-Shot                      & BP-0.5                         & BP-1.0                         & EPE \\
\midrule
GMStereo~\cite{gmstereo}       & \redxmark                      & 5.94                           & 1.83                           & 0.19 \\
HITNet~\cite{tankovich2021hitnet} & \redxmark                      & 7.83                           & 2.79                           & 0.20 \\
EAI-Stereo~\cite{zhao2022eai}  & \redxmark                      & 5.21                           & 2.31                           & 0.21 \\
RAFT-Stereo~\cite{lipson2021raft} & \redxmark                      & 7.04                           & 2.44                           & 0.18 \\
CREStereo~\cite{crestereo}     & \redxmark                      & 3.58                           & 0.98                           & 0.13 \\
IGEV-Stereo~\cite{igev}        & \redxmark                      & 3.52                           & 1.12                           & 0.14 \\
CroCo-Stereo~\cite{weinzaepfel2023croco} & \redxmark                      & 3.27                           & 0.99                           & 0.14 \\
MoCha-Stereo~\cite{chen2024mocha} & \redxmark                      & 3.20                           & 1.41                           & 0.13 \\
Selective-IGEV~\cite{selective_stereo} & \redxmark                      & 3.06                           & 1.23                           & 0.12 \\
\rowcolor[rgb]{ .886,  .937,  .855} Ours (finetuned)               & \redxmark                      & \textbf{1.26}                  & \textbf{0.26}                  & \textbf{0.09} \\
\midrule
\rowcolor[rgb]{ .886,  .937,  .855} Ours                           & \greencheckmark                & 2.31                           & 1.52                           & 0.13 \\
\bottomrule
\end{tabular}%

}
\vspace{-8pt}
\caption{Results on ETH3D leaderboard (test set). All methods except for the last row have used ETH3D training set for fine-tuning. Our fine-tuned version ranks 1st on leaderboard at the time of submission. Last row is obtained via zero-shot inference from our foundation model.}
\label{tab:eth_finetune}
\vspace{-15pt}
\end{table}
```

## 可复用的设计模式

### Pattern: 带高亮行的排行榜表
- 列结构：`lcccc`（方法名 + 多个数值指标）
- 最佳行：`\rowcolor` + `\textbf`
- 方法分组：同类方法之间无分隔线，不同类之间用 `\midrule`
- 宽度控制：`\resizebox{\mywidth}{!}` 自适应缩放
- 间距微调：`\vspace{-8pt}` / `\vspace{-15pt}` 紧凑排版
