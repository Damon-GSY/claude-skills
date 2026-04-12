# Claude Code Skills

Personal skill collection for [Claude Code](https://claude.ai/code).

## Own Skills

| Skill | Description | Path |
|-------|-------------|------|
| **llm-wiki** | 将对话知识渐进式沉淀到 Obsidian wiki，支持 RAG 检索 | `skills/llm-wiki/` |
| **thinking-tools** | 现代思维工具顾问，基于《现代思维工具词典》148 个思维工具 | `skills/thinking-tools/` |
| **decision-basics** | 决策基本 Skill，基于《决策的54个基本》54 个决策法则 | `skills/decision-basics/` |
| **business-models** | 商业思维模型顾问，基于刘润《经典商业思维模型手册》25 个模型 | `skills/business-models/` |
| **latex-examples** | LaTeX 高质量表格与展示风格参考库，从顶会论文中提炼生成模板 | `skills/latex-examples/` |

## Third-Party Skills (References)

These skills are installed from external sources via symlinks:

### [Minimax Skills](https://github.com/minimax-skills)
- `shader-dev` - GLSL shader techniques
- `pptx-generator` - PowerPoint generation
- `minimax-pdf` - PDF generation
- `ios-application-dev` - iOS dev guide
- `gif-sticker-maker` - Animated GIF stickers
- `fullstack-dev` - Full-stack architecture
- `frontend-dev` - Frontend development
- `android-native-dev` - Android dev guide

### [cc-switch Skills](https://github.com/nicekid1/cc-switch)
- `obsidian-cli` / `obsidian-markdown` - Obsidian integration
- `writing-skills` / `writing-plans` - Skill & plan authoring
- `brainstorming` - Creative exploration
- `using-superpowers` / `using-git-worktrees` - Workflow skills
- `finishing-a-development-branch` / `requesting-code-review` - Dev process
- `subagent-driven-development` - Parallel task execution
- `frontend-design` / `ui-ux-pro-max` - UI/UX design

### [Agents Skills](https://github.com/anthropics/agents)
- `cross-platform` / `shell-scripting` - Platform & scripting
- `long-running-init` / `long-running-session` - Multi-session projects
- `find-skills` - Skill discovery

## Installation

```bash
# Clone this repo
git clone https://github.com/Damon-GSY/claude-skills.git ~/claude-skills

# Symlink own skills into Claude Code skills directory
for skill in ~/claude-skills/skills/*/; do
  name=$(basename "$skill")
  ln -s "$skill" ~/.claude/skills/"$name"
done
```

## Skill Structure

Each skill follows the standard Claude Code skill format:

```
skill-name/
├── SKILL.md          # Main reference (required)
├── index.json        # Metadata
├── references/       # Supporting reference files (optional)
└── README.md         # Description (optional)
```
