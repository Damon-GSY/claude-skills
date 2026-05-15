# On-Policy Distillation (OPD) 论文系列总结

基于搜索结果和训练知识整理，聚焦 On-Policy Distillation 框架的 9 篇论文变体。

---

## 1. VETO

**核心贡献：** 用 logit 空间插值统一解决梯度爆炸和 mode collapse

**Motivation：**
- Student 模型模仿 Teacher 时，直接最小化 KL 散度可能导致梯度爆炸（logit 差异过大）或 mode collapse（Student 过早收敛到 Teacher 分布的峰值）
- 标准 KL 优化在 Teacher 输出分布很尖锐（低熵）时尤其不稳定

**Insight：**
- 在 softmax 之前的 logit 空间做插值，起到"trust region"的平滑效果
- 不直接优化 KL(π_T ‖ π_S)，而是优化一个平滑后的目标
- 这防止 Student 在有能力建模完整分布之前就过度拟合到峰值

---

## 2. EOPD

**核心贡献：** 在高熵 token 上叠加 forward KL，保住推理多样性

**Motivation：**
- 高能力 Teacher 往往产生非常尖锐的分布（低熵、高确定性）
- 如果 Student 被迫完美模仿尖锐分布，会丧失创造性和多样性
- Reverse KL 是 mode-seeking（匹配峰值），会摧毁多样性

**Insight：**
- Forward KL 是 mean-seeking，强制 Student 覆盖 Teacher 所有可能的高概率区域
- EOPD 修改目标函数，**只在 Teacher 不确定性高的 token 上应用 Forward KL 惩罚**
- Student 不仅学会了 Teacher 最可能的 token，还学会了 Teacher 的"不确定性"和"创造力"
- 结果：蒸馏后 Student 不会退化为确定性输出机器

---

## 3. REOPOLD

**核心贡献：** 将 RL 优化技巧（reward clipping、entropy masking、多阶段）移植到 on-policy distillation

**Motivation：**
- 标准蒸馏是纯监督学习（模仿概率分布），忽略了 token 的实际价值
- Teacher 生成数据的原因是它能产生更好的结果（更高 reward），但蒸馏没有利用这个信号

**Insight：**
- 为什么只模仿概率分布，不直接优化结果？
- 混合目标函数：结合 on-policy 模仿的稳定性 + RL 的性能最大化
- Teacher 提议动作（token），RL 信号验证并筛选出"最好的"那些动作，而非盲目模仿所有
- 引入 reward clipping（防止 reward 信号过强主导训练）和 entropy masking（在关键决策点保持探索）

---

## 4. OPSD

**核心贡献：** 用 (问题+正确答案) 条件化同一模型作为 teacher，8-12x token 效率优于 GRPO

**Motivation：**
- 标准 Self-Distillation 没有外部更大的 Teacher，难以找到有效的蒸馏信号
- 无条件的自蒸馏不稳定，模型容易"原地踏步"

**Insight：**
- 关键创新：**条件化正确性**。Teacher 是模型本身，但以正确答案为条件
- Prompt 构造为：(Question + Correct Answer) → Teacher 生成后续 token
- Teacher 在"知道正确答案"的条件下产生的分布，展示了"如何到达正确答案"的推理路径
- Student 模仿这个"成功条件化"的行为，而不是盲目生成
- 8-12x token 效率：因为每次蒸馏都在"正确的方向"上学习，浪费的 token 大幅减少

---

## 5. SDFT

**核心贡献：** 用自蒸馏实现持续学习，数学上等价于隐式 IRL

**Motivation：**
- 持续学习（Continual Learning）的核心问题是灾难性遗忘（Catastrophic Forgetting）
- 在新数据上微调时，模型会遗忘之前的知识
- 标准 L2 正则化对保留语言能力不够

**Insight：**
- 冻结一份初始模型的副本作为"Teacher"，让微调后的模型（Student）与初始模型保持 KL 散度最小
- **数学等价性：** 最小化 KL(current_model ‖ initial_model) 等价于隐式逆强化学习（Implicit IRL）
- 在 IRL 中，我们恢复一个专家正在优化的 reward function
- 这里"初始模型"充当专家，隐式学到的 reward function 把模型锚定在原始行为上
- 不需要额外的 reward 函数设计，KL 散度本身就是隐式 reward

---

## 6. SDPO

**核心贡献：** 用环境文字反馈做 token 级自蒸馏，超越 Claude Sonnet 4

**Motivation：**
- DPO 依赖成对的 (chosen/rejected) 数据，收集成本高
- 标准 DPO 基于整个序列的 reward 做优化，粒度太粗
- 模型在某一步犯错，但整个序列被一起更新，效率低

**Insight：**
- 用环境/评判者提供的**文字反馈**（如"这一步是错的，因为…"）替代二元偏好
- 文字反馈被转化为 **token 级别的 reward 信号**
- 从序列级优化转向 token 级优化
- 模型可以在错误发生的具体步骤修正，而不是基于最终结果更新整个序列
- 这本质上是一种细粒度的"自蒸馏"——从被批评增强后的自身版本中学习
- 据称效果超越了 Claude Sonnet 4

---

## 7. OPSDC

**核心贡献：** 蒸馏"简洁"行为，token 减少 40-58% 的同时准确率提升

**Motivation：**
- LLM 往往过于冗长，生成大量填充词
- 标准的 RLHF 让模型变简洁，但容易矫枉过正（信息丢失）
- 需要一种方法让模型学会"信息密度"

**Insight：**
- 蒸馏"简洁策略"：训练 Student 在 Teacher 被过滤/修改为简洁版本的样本上学习
- 或者使用对 token 数量施加重惩罚的 reward，同时保持准确率
- **40-58% token 减少 + 准确率提升**：这说明模型学到的是去掉"幻觉填充"，而非丢失有价值的信息
- 本质上蒸馏了"信息密度"这个能力，大幅降低推理成本

---

## 8. OPCD

**核心贡献：** 把 system prompt 和历史经验"烧进"参数，跨尺寸蒸馏可行

**Motivation：**
- 在聊天场景中，system prompt 和长对话历史每轮都要重新处理，消耗大量 context window 和计算
- 长历史导致推理延迟高

**Insight：**
- **"烧入"上下文**：把 system prompt 和对话历史蒸馏进模型权重（或小 adapter）
- 运行时不再需要读取"You are a helpful assistant…"，这个指令已经被烘焙进模型
- 创建了针对特定任务或对话风格的**专用模型**
- 跨尺寸蒸馏可行：大模型的"知识"可以蒸馏到小模型的参数中
- 推理时节省 memory、加速生成

---

## 9. Video-OPD

**核心贡献：** 把 on-policy distillation 扩展到视频生成

**Motivation：**
- 视频扩散模型（如 Sora）需要多步去噪（sampling），每步计算量巨大
- 训练视频模型成本极高，不重新训练的前提下提升质量/速度是关键

**Insight：**
- 把 LLM 中的 on-policy distillation 技术迁移到视频扩散模型的去噪轨迹
- Teacher = 高步数采样器（慢、高质量）
- Student = 低步数采样器（快、要学 Teacher 的输出质量）
- 关键挑战：**时间一致性**（temporal consistency）——Student 需要蒸馏 Teacher 的时序连贯性
- 实现用更少采样步数生成高质量视频

---

## 总览：一个统一框架

这 9 篇论文可以看作 **On-Policy Distillation (OPD)** 的不同维度扩展：

```
                    OPD (On-Policy Distillation)
                           │
        ┌──────────┬───────┴───────┬──────────┐
        │          │               │          │
    稳定性      多样性          效率提升      应用扩展
        │          │               │          │
    VETO        EOPD          OPSD/OPSDC    Video-OPD
    REOPOLD     SDPO          OPCD
                SDFT
```

**核心 tension 始终是同一个：**
- **模仿得太像** → mode collapse（丢失多样性）
- **模仿得不够** → 性能下降
- **每篇论文都在不同的维度上找平衡点**
