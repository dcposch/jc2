#!/usr/bin/env python3
"""Run one immutable reviewer script with relocated inputs; normal mode only.

This is a replay runner, not a fail-closed mathematical verifier: several
reviewer diagnostics print predicates which require inspection.
"""
import argparse
from pathlib import Path
import resource

parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=('census', 'hlift', 'controls'))
args = parser.parse_args()
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (45, 45))
root = Path(__file__).resolve().parents[2]
reviewer = root / 'box/linear-c-transverse-gate-fable5-20260906' / (args.mode + '.py')
source = reviewer.read_text()
for old, new in {
    '/tmp/jc2-lane.rM5Jkj/inputs/delta2_stage8.strongest.json': root / 'box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json',
    '/tmp/jc2-lane.rM5Jkj/inputs/complete_export.json': root / 'box/factored-jacobian-pilot-20260906/complete_export.json',
}.items():
    source = source.replace(old, str(new))
exec(compile(source, str(reviewer), 'exec'), {'__name__': '__main__'})
