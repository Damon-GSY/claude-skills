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
| **agency** | 按需加载 [The Agency](https://github.com/msitarzewski/agency-agents) 的 184 个专业 AI agent，根据上下文智能匹配并写入 `~/.claude/agents/` | `skills/agency/` |

## Third-Party Skills (References)

These skills are installed from external sources via symlinks:

### [obra/superpowers](https://github.com/obra/superpowers)
Agentic skills framework & software development methodology (14 skills):
- `brainstorming` - Creative exploration before implementation
- `writing-skills` / `writing-plans` - Skill & plan authoring with TDD
- `using-superpowers` / `using-git-worktrees` - Workflow skills
- `finishing-a-development-branch` / `requesting-code-review` - Dev process
- `subagent-driven-development` - Parallel task execution
- `cross-platform` / `shell-scripting` - Platform & scripting patterns
- `long-running-init` / `long-running-session` - Multi-session projects
- `find-skills` - Skill discovery

### [Minimax Skills](https://github.com/nicekid1/minimax-skills)
- `shader-dev` - GLSL shader techniques
- `pptx-generator` - PowerPoint generation
- `minimax-pdf` - PDF generation
- `ios-application-dev` - iOS dev guide
- `gif-sticker-maker` - Animated GIF stickers
- `fullstack-dev` - Full-stack architecture
- `frontend-dev` - Frontend development
- `android-native-dev` - Android dev guide

### [anthropics/skills](https://github.com/anthropics/skills)
- `frontend-design` - Production-grade frontend design

### Other Third-Party Skills
| Skill | Repo | Description |
|-------|------|-------------|
| `obsidian-cli` / `obsidian-markdown` | [cwaits6/obsidian-cli-skill](https://github.com/cwaits6/obsidian-cli-skill) | Obsidian vault CLI integration |
| `ui-ux-pro-max` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX design intelligence |
| `agent-browser` | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Browser automation CLI |
| `obsidian-skills` | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | Obsidian-specific skills collection |

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
