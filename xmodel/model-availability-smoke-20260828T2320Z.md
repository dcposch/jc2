# Model availability smoke — 2026-08-28T23:20Z

Prompt:
`xmodel/model-availability-smoke-prompt-20260828.md`, SHA-256
`f9c86a8f07deed5c24d65222dec52f175f3a3eca251ba208981ecd5a8c8dcd67`.
The prompt forbade repository inspection and requested one shell command with
sentinel `JC2_MODEL_SHELL_OK_20260828`.

| adapter | pinned/runtime model evidence | rc | wall | shell sentinel |
|---|---|---:|---:|---|
| `ops/adapters/claude.sh` | `claude-fable-5`; adapter pin `--model fable` | 0 | 12.18 s | PASS |
| `ops/adapters/opus.sh` | `claude-opus-5`; adapter pin `--model opus` | 0 | 9.35 s | PASS |
| `ops/adapters/codex.sh` | launcher header `model: gpt-5.6-sol`, provider OpenAI | 0 | 9.58 s | PASS |
| `ops/adapters/grok.sh` | `Grok 4.6` | 0 | 10.02 s | PASS |

Operational verdict: all four independent adapters can presently complete a
fresh inference and shell tool call. This is direct evidence that the paid
execution paths are usable now; it is not a guarantee about future provider
ceilings. Codex collaboration subagents separately returned a subscription
usage-limit error in the same interval, so adapter availability and in-product
subagent availability must be tested and routed independently.

