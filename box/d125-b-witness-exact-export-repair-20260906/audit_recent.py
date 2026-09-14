#!/usr/bin/env python3
"""Read-only numeric-type inventory over four named terminal owned boxes."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NAMES = (
    'd125-published-chain-discriminator-20260906',
    'd125-minimal-monomial-receiver-composition-20260906',
    'd125-small-receiver-polynomial-lift-contract-20260906',
    'd125-minimal-receiver-b-reconstruction-20260906',
)

def inventory(value, path='$'):
    if type(value) is float:
        yield ('float', path)
    elif type(value) is int and abs(value) > 2**53:
        yield ('large_int', path)
    elif isinstance(value, dict):
        for key, item in value.items():
            yield from inventory(item, path + '.' + key)
    elif isinstance(value, list):
        for i, item in enumerate(value):
            yield from inventory(item, path + '[' + str(i) + ']')

records = []
for name in NAMES:
    for path in sorted((ROOT / 'box' / name).glob('*.json')):
        raw = path.read_bytes()
        fields = list(inventory(json.loads(raw)))
        records.append({
            'path': str(path.relative_to(ROOT)),
            'sha256': hashlib.sha256(raw).hexdigest(),
            'float_paths': [p for kind, p in fields if kind == 'float'],
            'large_integer_count': sum(kind == 'large_int' for kind, _ in fields),
        })
print(json.dumps({'schema': 'jc2.bounded-serialization-inventory/v1',
                  'scope': list(NAMES), 'files': records}, indent=2, sort_keys=True))
