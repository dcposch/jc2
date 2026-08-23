#!/bin/sh
# ops/sol_lane.sh <tag> <promptfile> : run a Sol (codex) lane from a prompt file, ori-proof
tag="$1"; pf="$2"
python3 -c "import os,re; p=os.path.expanduser('~/.codex/config.toml'); s=open(p).read(); open(p,'w').write(re.sub(r'^model = .*\n','',s,flags=re.M))"
codex exec "$(cat "$pf")" > "xmodel/$tag.log" 2>&1
echo "$tag done rc=$? $(date +%H:%M)" >> pilot-local.log
