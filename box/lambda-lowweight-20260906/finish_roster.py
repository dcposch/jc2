#!/usr/bin/env python3
"""Stop the inherited batch at R002 completion, alias R003, then run R004."""
import json,os,signal,time
from pathlib import Path
import run_truncated as runner
import receiver_alias
HERE=Path(__file__).resolve().parent
pid=1782258
while not (HERE/'R002.N3.json').exists(): time.sleep(.05)
try: os.kill(pid,signal.SIGSTOP)
except ProcessLookupError: pass
try:
    children=Path(f'/proc/{pid}/task/{pid}/children').read_text().split()
    for child in children:
        try: os.killpg(int(child),signal.SIGKILL)
        except ProcessLookupError: pass
except FileNotFoundError: pass
try: os.kill(pid,signal.SIGKILL)
except ProcessLookupError: pass
receiver_alias.alias()
for p in Path('/dev/shm').glob('lambda-lowweight-live-R003.N*.log'):p.unlink()
cases=json.loads((HERE/'run_cases.json').read_text());d=next(c for c in cases if c['id']=='R004')
for N in (1,2,3):runner.run(d,N,240)
print('ROSTER_NATIVE_CHECKS_FINISHED',flush=True)
