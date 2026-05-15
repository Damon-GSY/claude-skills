---
name: agency
description: On-demand agent loader from The Agency (msitarzewski/agency-agents). Searches 184 specialized AI agents by context, loads relevant ones into ~/.claude/agents/.
triggers: ["agency", "load agent", "agents", "activate agent", "specialist"]
tags: ["agents", "agency", "orchestration", "multi-agent"]
---

# Agency — On-Demand Agent Loader

Load specialized AI agents from [The Agency](https://github.com/msitarzewski/agency-agents) based on your current task context.

## When to Use

When the user mentions wanting specialized agents, multiple agents, or says `/agency`. Also trigger when the user describes a complex multi-domain task that would benefit from domain-specific expertise.

## Workflow

### Step 1: Read the Agent Index

Read the cached index file at `~/.omc/agency-cache/agent-index.json`. This contains 184 agents with their name, description, category, emoji, vibe, and file_path.

### Step 2: Understand the Task Context

Analyze the user's current conversation/task to identify:
- Technical domains involved (frontend, backend, devops, mobile, etc.)
- Business domains involved (marketing, finance, sales, product, etc.)
- Specific skills needed (security, testing, architecture, design, etc.)

### Step 3: Match and Rank Agents

Score each agent against the task context by matching keywords from:
- Agent `name`
- Agent `description`
- Agent `category`
- Agent `vibe`

Rank by relevance score. Return the **top 5-8 most relevant agents**.

### Step 4: Present Matches to User

Display the matched agents as a selection table:

```
## Matched Agents for: [task summary]

| # | Agent | Category | Description |
|---|-------|----------|-------------|
| 1 | 🏗️ Backend Architect | engineering | Scalable system design... |
| 2 | 🔒 Security Engineer | engineering | Security-first... |
| ... | | | |
```

Then use AskUserQuestion to let the user select which agents to load. Options:
- Select specific agents by number
- "All" to load all matched agents
- "Search again" with different keywords

### Step 5: Load Selected Agents

For each selected agent:

1. Copy the agent .md file from the local cache to `~/.claude/agents/`:
   ```bash
   cp /tmp/agency-agents/<file_path> ~/.claude/agents/
   ```

   If the local cache at `/tmp/agency-agents/` doesn't exist (e.g. after reboot), clone it first:
   ```bash
   git clone --depth 1 https://github.com/msitarzewski/agency-agents.git /tmp/agency-agents
   ```

2. Confirm each agent was loaded successfully.

### Step 6: Activate

After loading, tell the user the agents are now available. They can be activated in conversation by name:

```
"Activate Backend Architect and help me design the API."
```

### Step 7: Update Index (Optional)

If the user mentions the index might be stale, offer to rebuild:
```bash
python3 ~/.omc/agency-cache/build-index.py /tmp/agency-agents
```

## Quick Commands

The user can also use these patterns:
- `/agency` — Interactive search and load
- `/agency backend` — Search for backend-related agents
- `/agency security testing` — Search for security + testing agents
- `/agency update` — Rebuild the index cache
- `/agency list` — Show all loaded agents in ~/.claude/agents/

## Categories Available

| Category | Count | Examples |
|----------|-------|---------|
| academic | 5 | Anthropologist, Historian, Psychologist |
| design | 8 | UI Designer, UX Architect, Brand Guardian |
| engineering | 29 | Backend Architect, Security Engineer, Code Reviewer |
| finance | 5 | Financial Analyst, Tax Strategist |
| game-development | 20 | Unity Architect, Unreal World Builder |
| marketing | 30 | SEO Specialist, Content Creator |
| paid-media | 7 | PPC Strategist, Programmatic Buyer |
| product | 5 | Product Manager, Sprint Prioritizer |
| project-management | 6 | Project Shepherd, Jira Steward |
| sales | 8 | Deal Strategist, Outbound Strategist |
| spatial-computing | 6 | visionOS Engineer, XR Developer |
| specialized | 41 | Salesforce Architect, MCP Builder, Recruiter |
| support | 6 | Support Responder, Analytics Reporter |
| testing | 8 | API Tester, Performance Benchmarker |

## Notes

- Agents are loaded to `~/.claude/agents/` — this is global across all projects.
- If an agent file already exists, it will be overwritten.
- To remove a loaded agent, delete it from `~/.claude/agents/`.
- The index cache lives at `~/.omc/agency-cache/agent-index.json`.
- The local repo clone lives at `/tmp/agency-agents/` (may be cleared on reboot).
