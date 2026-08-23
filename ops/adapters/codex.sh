#!/bin/sh
# codex CLI adapter (account-default model). Strips any model override that a
# third-party tool wrote into the shared config before launching (ori-proofing).
pf="$1"
python3 -c "import os,re; p=os.path.expanduser('~/.codex/config.toml'); s=open(p).read(); open(p,'w').write(re.sub(r'^model = .*\n','',s,flags=re.M))"
exec codex exec "$(cat "$pf")"
