#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SUMS=ROOT/'SHA256SUMS.txt'

def digest(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):
            h.update(block)
    return h.hexdigest()

def main() -> int:
    bad=[]
    for line in SUMS.read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        claimed, rel=line.split(maxsplit=1)
        p=ROOT/rel
        actual=digest(p)
        ok=(claimed==actual)
        print(('OK  ' if ok else 'BAD ')+rel)
        if not ok: bad.append(rel)
    run=json.loads((ROOT/'machine_certificate/plane_jacobian_mesh80_run.json').read_text(encoding='utf-8'))
    replay=json.loads((ROOT/'machine_certificate/replay_report.json').read_text(encoding='utf-8'))
    print('run_state:',run.get('run_state'))
    print('run_hash:',run.get('run_hash'))
    print('bidirectional_roundtrip:',all(x.get('valid') for x in run.get('bidirectional_roundtrip',[])))
    print('replay_valid:',replay.get('valid'))
    return 1 if bad or not replay.get('valid') else 0

if __name__=='__main__':
    raise SystemExit(main())
