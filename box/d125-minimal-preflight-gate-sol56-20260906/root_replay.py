#!/usr/bin/env python3
"""Relocate only a vanished private input directory; never edit sealed review.
All mathematical code is the hash-pinned reviewer source, recompiled unchanged
except one INPUT assignment. Inputs map to already rehashed canonical files.
"""
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = Path(__file__).with_name('audit.py')
EXPECTED = '3e9558712b480c7506afbabf05d85383a7c50a0554661ec1bce1aeed41bf5187'
source = AUDIT.read_bytes()
if hashlib.sha256(source).hexdigest() != EXPECTED:
    raise RuntimeError('reviewer source changed')
old = "INPUT = Path('/tmp/jc2-lane.MAp4nm/inputs')"
text = source.decode('utf-8')
if text.count(old) != 1:
    raise RuntimeError('not the exact declared relocation site')


class InputPaths:
    def __truediv__(self, name):
        if name in ('client.py', 'test_client.py'):
            return ROOT / 'box/d125-minimal-receiver-client-preflight-20260906' / name
        if name == 'FALLACY-v2.md':
            return ROOT / name
        allowed = {
            'd125-minimal-receiver-client-preflight-astra-20260906.md',
            'd125-minimal-receiver-gate-fable5-20260906.md',
            'd125-minimal-monomial-receiver-composition-astra-20260906.md',
            'd125-small-receiver-polynomial-lift-contract-astra-20260906.md',
        }
        if name not in allowed:
            raise RuntimeError('unregistered relocated input')
        return ROOT / 'xmodel' / name


exec(compile(text.replace(old, 'INPUT = ROOT_RELOCATED_INPUT', 1), str(AUDIT), 'exec'),
     {'__name__': '__main__', '__file__': str(AUDIT),
      'ROOT_RELOCATED_INPUT': InputPaths()})
