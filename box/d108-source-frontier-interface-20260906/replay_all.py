#!/usr/bin/env python3
"""Read-only full semantic replay; no charged file writes."""
from pathlib import Path
import runpy
import sys
root=Path(__file__).resolve().parent
for name in ('inspect_source.py','map_controls.py','edge_interface.py'):
    sys.argv=[str(root/name),'--verify']
    runpy.run_path(str(root/name),run_name='__main__')
print('D108_INTERFACE_READ_ONLY_REPLAY=PASS')
