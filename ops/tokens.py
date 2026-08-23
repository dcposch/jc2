#!/usr/bin/env python3
"""Campaign token usage from the CLIs' own session logs (exact counters).

Sums provider-logged usage — no byte heuristics:
  - Claude:  per-message "usage" objects in ~/.claude/projects/<proj>/**/*.jsonl
  - Codex:   final "total_token_usage" per rollout in ~/.codex/sessions/**/*.jsonl
  - Grok:    max cumulative "totalTokens" per session under ~/.grok/sessions/
             (project-scoped dirs; filtered to this campaign's paths)

Run weekly; paste the summary line into PROGRESS.md. Deltas come from
consecutive entries. All-time totals; cache split shown where the CLI logs it.
"""
import json, os, re, glob, sys

HOME = os.path.expanduser("~")
CLAUDE_PROJ = os.path.join(HOME, ".claude", "projects", "-Users-dc-code-math")
CODEX_SESS = os.path.join(HOME, ".codex", "sessions")
GROK_SESS = os.path.join(HOME, ".grok", "sessions")
CAMPAIGN_PAT = re.compile(r"math", re.I)  # grok/codex dirs are project-scoped


def claude():
    tot = {"input_tokens": 0, "cache_creation_input_tokens": 0,
           "cache_read_input_tokens": 0, "output_tokens": 0}
    n = 0
    for path in glob.glob(os.path.join(CLAUDE_PROJ, "**", "*.jsonl"), recursive=True):
        with open(path, errors="replace") as fh:
            for line in fh:
                if '"usage"' not in line:
                    continue
                try:
                    msg = json.loads(line)
                except json.JSONDecodeError:
                    continue
                u = (msg.get("message") or {}).get("usage") or msg.get("usage")
                if not isinstance(u, dict) or "output_tokens" not in u:
                    continue
                for k in tot:
                    tot[k] += u.get(k) or 0
                n += 1
    return tot, n


def codex():
    tot = {"input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0,
           "reasoning_output_tokens": 0, "total_tokens": 0}
    n = 0
    for path in glob.glob(os.path.join(CODEX_SESS, "**", "*.jsonl"), recursive=True):
        last = None
        with open(path, errors="replace") as fh:
            for line in fh:
                if '"total_token_usage"' not in line:
                    continue
                m = re.search(r'"total_token_usage":({[^{}]*})', line)
                if m:
                    try:
                        last = json.loads(m.group(1))
                    except json.JSONDecodeError:
                        pass
        if last:
            for k in tot:
                tot[k] += last.get(k) or 0
            n += 1
    return tot, n


def grok():
    total = 0
    n = 0
    for proj in glob.glob(os.path.join(GROK_SESS, "*")):
        if not CAMPAIGN_PAT.search(os.path.basename(proj)):
            continue
        for path in glob.glob(os.path.join(proj, "**", "*.jsonl"), recursive=True):
            best = 0
            with open(path, errors="replace") as fh:
                for line in fh:
                    for m in re.finditer(r'"totalTokens":(\d+)', line):
                        v = int(m.group(1))
                        if v > best:
                            best = v
            if best:
                total += best
                n += 1
    return total, n


def fmt(x):
    return f"{x/1e6:.1f}M"


if __name__ == "__main__":
    c, cn = claude()
    c_total = sum(c.values())
    x, xn = codex()
    g, gn = grok()
    print(f"Claude  ({cn} msgs): output {fmt(c['output_tokens'])}, fresh-in "
          f"{fmt(c['input_tokens'])}, cache-write {fmt(c['cache_creation_input_tokens'])}, "
          f"cache-read {fmt(c['cache_read_input_tokens'])}, TOTAL {fmt(c_total)}")
    print(f"Codex   ({xn} rollouts): output {fmt(x['output_tokens'])} "
          f"(reasoning {fmt(x['reasoning_output_tokens'])}), input {fmt(x['input_tokens'])} "
          f"(cached {fmt(x['cached_input_tokens'])}), TOTAL {fmt(x['total_tokens'])}")
    print(f"Grok    ({gn} sessions): TOTAL {fmt(g)} (cumulative session counters)")
    print(f"SUMMARY line for PROGRESS.md: tokens(all-time): "
          f"Claude out {fmt(c['output_tokens'])} / total {fmt(c_total)}; "
          f"Codex total {fmt(x['total_tokens'])}; Grok total {fmt(g)}")
