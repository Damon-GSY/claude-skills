---
name: pdf-reader
description: >
  PDF 文档解析与知识提取。将 PDF 转为纯文本，支持分页提取、摘要生成、
  结构化整理，并可将内容持久化为 workspace 参考资料。
  当用户发送 PDF 文件，或提到"解析PDF"、"提取内容"、"PDF转文字"时激活。
metadata:
  {
    "openclaw": {
      "emoji": "📖",
      "requires": { "bins": ["python3"] },
      "tags": ["pdf", "text-extraction", "document", "knowledge"],
      "category": "tools"
    }
  }
---

# PDF Reader - 文档解析与知识提取

将 PDF 文件解析为结构化文本，并整理成可检索、可复用的知识文件。

## 能力

- **文本提取** — 从 PDF 中提取纯文本（支持中文、英文等多语言）
- **分页预览** — 逐页查看内容，快速定位关键信息
- **结构化整理** — 将提取内容按主题/章节整理为 Markdown 参考文件
- **知识持久化** — 保存到 workspace `references/` 目录，跨会话可用

## 使用流程

### Step 1: 定位 PDF 文件

飞书收到的文件存放在 `/root/.openclaw/media/inbound/`，文件名可能含乱码。
用 `ls -lt` 找到最新的文件：

```bash
ls -lt /root/.openclaw/media/inbound/*.pdf | head -5
```

### Step 2: 检查 pymupdf 是否可用

```bash
python3 -c "import fitz; print('pymupdf ready')" 2>&1
```

如果不可用，安装：

```bash
pip install --break-system-packages pymupdf
```

### Step 3: 提取文本

提取全部内容：

```python
import fitz
doc = fitz.open('/path/to/file.pdf')
print(f'Pages: {doc.page_count}')
for i in range(doc.page_count):
    text = doc[i].get_text()
    print(f'--- Page {i+1} ---')
    print(text)
```

提取指定页（快速预览）：

```python
import fitz
doc = fitz.open('/path/to/file.pdf')
for i in range(start_page, end_page):
    print(doc[i].get_text())
```

提取并保存为文本文件：

```python
import fitz
doc = fitz.open('/path/to/file.pdf')
text = ''
for i in range(doc.page_count):
    text += doc[i].get_text()
with open('/path/to/output.txt', 'w') as f:
    f.write(text)
print(f'Extracted {doc.page_count} pages, {len(text)} chars')
```

### Step 4: 结构化整理（可选）

根据 PDF 内容特点，将文本整理为：
- **思维模型手册** → 按模型分条整理，写入 `references/` 并更新 TOOLS.md
- **书籍/文章** → 按章节整理，保留目录结构
- **报告/数据** → 提取关键数据点和结论
- **通用文档** → 直接保存纯文本 + 一段摘要

### Step 5: 更新 workspace 索引

整理完成后，在 TOOLS.md 中记录新增的参考资料，确保跨会话可查。

## 输出规范

### references 目录结构

```
references/
├── 原始PDF.pdf          ← 保留原始文件
├── 文档名.txt           ← 纯文本版（用于搜索）
└── 文档名-笔记.md       ← 结构化笔记（可选，用于快速参考）
```

### TOOLS.md 索引格式

```markdown
## 参考资料库

| 来源 | 文件 | 核心内容 |
|------|------|---------|
| 刘润 | references/刘润-经典商业思维模型手册.txt | 25个商业思维模型 |
```

## 注意事项

- pymupdf 提取的是嵌入文本层，对扫描版 PDF 需要额外 OCR（暂不支持）
- 中文 PDF 通常提取效果良好
- 大文件（100页+）建议分批提取，避免一次性占用过多上下文
- 提取后务必人工审核关键内容，OCR/解析可能有细微误差
