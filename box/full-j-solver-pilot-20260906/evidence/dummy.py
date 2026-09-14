#!/usr/bin/env python3
"""Deliberately orphan-resistant runner regression: leader exits first."""
import os
from pathlib import Path
import subprocess
import sys
code = 'import signal,time; signal.signal(signal.SIGTERM,signal.SIG_IGN); b=bytearray(64*1024*1024); print("CHILD_ALLOCATED",flush=True); time.sleep(60)'
child = subprocess.Popen([sys.executable,'-c',code])
Path('dummy.child.json').write_text(str(child.pid)+'\n')
print('LEADER',os.getpid(),'PGID',os.getpgrp(),'CHILD',child.pid,flush=True)
