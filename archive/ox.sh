#!/bin/sh
# Ox Alpha lane runner (OpenRouter). Usage: ops/ox.sh "prompt" [outfile]
# Key: $OPENROUTER_API_KEY or ~/.config/openrouter/key
# Model: $OX_MODEL (default openrouter/ox-alpha; verify slug via
#   curl -s https://openrouter.ai/api/v1/models | jq '.data[].id' | grep -i ox)
KEY="${OPENROUTER_API_KEY:-$(cat ~/.config/openrouter/key 2>/dev/null)}"
[ -z "$KEY" ] && { echo "ERROR: no OpenRouter key (env OPENROUTER_API_KEY or ~/.config/openrouter/key)" >&2; exit 1; }
MODEL="${OX_MODEL:-openrouter/ox-alpha}"
PROMPT="$1"; OUT="${2:-/dev/stdout}"
python3 - "$MODEL" "$PROMPT" "$OUT" << 'PYEOF'
import sys, json, os, urllib.request
model, prompt, out = sys.argv[1], sys.argv[2], sys.argv[3]
key = os.environ.get("OPENROUTER_API_KEY") or open(os.path.expanduser("~/.config/openrouter/key")).read().strip()
req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions",
    data=json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}],
                     "max_tokens": 32000}).encode(),
    headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
r = json.load(urllib.request.urlopen(req, timeout=1200))
text = r["choices"][0]["message"]["content"]
open(out, "w").write(text) if out != "/dev/stdout" else print(text)
PYEOF
