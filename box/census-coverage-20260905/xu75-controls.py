#!/usr/bin/env python3
"""Boundary and caller-scope controls for the snapshotted direct Xu 7.5 helper."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util
import json
import sys

OUT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('coverage_split', OUT / 'op-split_window.snapshot.py')
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

cases = [
    ((1, 1, 1), Q(2), 3, 8, True, 'full split strictly below cutoff'),
    ((2, 1), Q(2), 3, 8, False, 'partial split untouched'),
    ((1, 1, 1), Q(9, 4), 3, 8, False, 'equality untouched'),
    ((1, 1, 1), Q(5, 2), 3, 8, False, 'above cutoff untouched'),
    ((1, 1), Q(2), 2, 5, False, 'integer equality inside early-split window'),
]
result = []
for part, rho, u, v, expected, label in cases:
    actual = module.xu_corollary_7_5(part, rho, u, v)
    assert actual['excludes'] == expected, (label, actual)
    result.append(dict(label=label, partition=part, rho=str(rho), u=u, v=v,
                       excludes=actual['excludes'], cutoff=actual['cutoff']))
assert module.genuine_partitions(1) == []
result.append(dict(label='u=1 has no genuine partition in actual caller', passes=True))
print(json.dumps(result, indent=2))
