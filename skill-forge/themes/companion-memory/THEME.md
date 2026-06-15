---
title: AI 伴侣长期记忆
tags: [memory, companion, agent, cli, memgpt]
status: stable
version: "2.0"
---

# Theme: companion-memory v2

**给 Agent 用的**跨会话记忆：统一 CLI `memory_cli.py`，JSON 输出，inbox 确认流。

## Skill

| 源文件 | 作用 |
|--------|------|
| `companion-memory.skill.md` | Agent 生命周期：wakeup → search → save → wind-down |

## Scripts（安装后在 skill `scripts/`）

| 脚本 | 作用 |
|------|------|
| `memory_cli.py` | **主入口** — bootstrap, wakeup, search, save, inbox, wind-down, validate |
| `memory_lib.py` | 库：打分、sanitize、YAML store |
| `memory_search.py` | search 薄封装 |

## Agent 快速开始

```bash
python skill-core/skill.py batch build companion-memory --test
python skill-core/skill.py install examples/companion-memory --host cursor --scope project

cd {project}
python .cursor/skills/companion-memory/scripts/memory_cli.py bootstrap --root memory --json
python .cursor/skills/companion-memory/scripts/memory_cli.py wakeup --root memory --json
```

协议全文：`refs/agent-protocol.md`

## 工作区 layout

```
memory/
  index.yaml
  core/{persona,user-model,relationship,working}.yaml
  episodes/*.yaml
  inbox/*.yaml
  diary/*.md
  archive/sessions/*.md
  reflections/*.md
```

## 依赖

- Python 3.10+
- PyYAML（`pip install pyyaml`）

## 搭配

- `relationship-match` → 可选导入 profile
- MemPalace MCP → 可选；见 `mempalace-bridge.md`
