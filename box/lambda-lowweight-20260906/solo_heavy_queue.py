#!/usr/bin/env python3
"""Continue solo full-memory heavy chart attempts after the C341 batch exits."""
import json,os,time
from pathlib import Path
import run_truncated as runner
HERE=Path(__file__).resolve().parent
pid=1941265
while True:
    try:os.kill(pid,0)
    except ProcessLookupError:break
    time.sleep(2)
runner.CAP=int(15.5*1024**3);runner.AS_CAP=int(15.8*1024**3)
cases=json.loads((HERE/'run_cases.json').read_text());d=next(c for c in cases if c['id']=='C455')
for N in (1,2,3):runner.run(d,N,900,frontier=12,std_seconds=240)
print('SOLO_HEAVY_BASELINES_DONE',flush=True)
