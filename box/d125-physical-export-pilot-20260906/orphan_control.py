#!/usr/bin/env python3
"""Tiny actual orphan/cap control: leader exits, TERM-ignoring child stays."""
import json,os,subprocess,sys
from pathlib import Path
child=subprocess.Popen([sys.executable,'-c','import os,signal,time; signal.signal(signal.SIGTERM,signal.SIG_IGN); print("ORPHAN_CHILD",os.getpid(),flush=True); time.sleep(20)'])
with Path('orphan.child.json').open('x') as f:json.dump({'pid':child.pid,'leader':os.getpid(),'pgid':os.getpgrp()},f)
print('LEADER_EXITS',os.getpid(),'CHILD',child.pid,flush=True)
