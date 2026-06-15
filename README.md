# Companion Memory

面向 **AI 伴侣跨会话长期记忆** 的 Cursor Agent Skill。文件存储 + CLI 驱动，对齐 MemGPT 分层、Generative Agents 反思与 inbox 确认流。

| 组件 | 作用 |
|------|------|
| **companion-memory** | Agent 生命周期：bootstrap → wakeup → search → save → wind-down |
| `memory_cli.py` | 主 CLI（`--json` 输出） |
| `memory_lib.py` | 打分、sanitize、YAML store |
| `memory_search.py` | search 薄封装 |

## 快速开始

```bash
git clone https://github.com/azhimiao/memory.git
cd memory
pip install -r requirements.txt

# 安装 skill（Cursor 项目级）
python skill-core/skill.py install examples/companion-memory/companion-memory --host cursor --scope project

# 初始化工作区
python .cursor/skills/companion-memory/scripts/memory_cli.py bootstrap --root memory --json
python .cursor/skills/companion-memory/scripts/memory_cli.py wakeup --root memory --json
```

Windows 可用 `./skill install examples/companion-memory/companion-memory --host cursor --scope project`。

## CLI 命令

| 命令 | 说明 |
|------|------|
| `bootstrap` | 创建 `memory/` 目录树与模板 |
| `wakeup` | 会话启动：加载 core + 近期 episodes |
| `search` | 按 query 检索记忆 |
| `save` | 写入 episode / working |
| `inbox-promote` | 将 inbox 草稿提升为正式记忆 |
| `invalidate` | 标记记忆失效 |
| `wind-down` | 会话结束：归档 + 反思提示 |
| `validate` | 校验 schema 与一致性 |

全局 flag 须放在子命令前：`memory_cli.py --root memory --json wakeup`

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

协议与分层规则见 `skill-forge/themes/companion-memory/refs/agent-protocol.md`、`memory-tiers.md`。

## 从源码编译

```bash
python skill-core/skill.py batch build companion-memory --test
python skill-core/skill.py install skill-forge/built/companion-memory/companion-memory --host cursor --scope project
```

## 仓库结构

| 路径 | 说明 |
|------|------|
| `examples/companion-memory/` | 可安装 skill |
| `skill-forge/themes/companion-memory/` | 主题源 |
| `skill-forge/built/companion-memory/` | 编译输出 |
| `skill-core/` | 编译、测试、安装 CLI |

完整工具链见 [azhimiao/skillforskill](https://github.com/azhimiao/skillforskill)。
