#!/bin/sh
# Generic research-lane runner (model-agnostic).
# Usage: ops/lane.sh <adapter> <tag> <promptfile>
# Adapters live in ops/adapters/<adapter>.sh and encapsulate one model CLI.
adapter="$1"; tag="$2"; pf="$3"
[ -f "ops/adapters/$adapter.sh" ] || { echo "unknown adapter: $adapter" >&2; exit 2; }
sh "ops/adapters/$adapter.sh" "$pf" > "xmodel/$tag.log" 2>&1
echo "$tag done rc=$? $(date +%H:%M)" >> pilot-local.log
