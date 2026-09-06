#!/usr/bin/env python3
"""After the current C455 prefix attempt, switch subsequent runs to packed storage."""
import json,os,signal,time
from pathlib import Path
import run_truncated as runner
HERE=Path(__file__).resolve().parent
pid=1948504
while not (HERE/'C455.frontier12.N1.json').exists():time.sleep(.05)
try:os.kill(pid,signal.SIGSTOP)
except ProcessLookupError:pass
try:
    for child in Path(f'/proc/{pid}/task/{pid}/children').read_text().split():
        try:os.killpg(int(child),signal.SIGKILL)
        except ProcessLookupError:pass
except FileNotFoundError:pass
try:os.kill(pid,signal.SIGKILL)
except ProcessLookupError:pass
for p in Path('/dev/shm').glob('lambda-lowweight-live-C455.frontier12.N[23].log'):p.unlink()
runner.CAP=int(15.5*1024**3);runner.AS_CAP=int(15.8*1024**3)
case=next(c for c in json.loads((HERE/'run_cases.json').read_text()) if c['id']=='C455')
for N in (1,2,3):runner.run(case,N,900,std_seconds=240,packed=True)
print('PACKED_HEAVY_BASELINES_DONE',flush=True)
