#!/bin/sh
# grok CLI adapter.
set -u
pf=$1
echo "cli=$(grok -v 2>&1 | head -1) permission=bypassPermissions output=plain" >&2
exec grok --permission-mode bypassPermissions --output-format plain \
  --prompt-file "$pf"
