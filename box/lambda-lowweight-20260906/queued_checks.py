#!/usr/bin/env python3
"""After first baseline batch exits, run exact target components."""
import json, os, sys, time
from pathlib import Path
import run_truncated as runner

HERE=Path(__file__).resolve().parent
pid=int(sys.argv[1])
while True:
    try: os.kill(pid,0)
    except ProcessLookupError: break
    time.sleep(5)
cases=json.loads((HERE/'run_cases.json').read_text())
for case in cases:
    for N in (1,2,3): runner.run(case,N,240,charge_zero=True)
print('ALL_CHARGE_ZERO_CHECKS_DONE',flush=True)
