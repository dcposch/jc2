#!/usr/bin/env python3
"""Hash-checked relocation of the sole witness path in the sealed Fable code.
Optional repaired witness is checked against Fable's independently recomputed
exact minors, not against an old imprecise serialization.
"""
import argparse
import hashlib
from pathlib import Path
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--witness', required=True)
parser.add_argument('--witness-sha256', required=True)
args, remainder = parser.parse_known_args()
witness = Path(args.witness).resolve()
if hashlib.sha256(witness.read_bytes()).hexdigest() != args.witness_sha256:
    raise RuntimeError('witness hash mismatch')
audit = Path(__file__).with_name('gate_own.py')
source = audit.read_bytes()
if hashlib.sha256(source).hexdigest() != 'e0c01f7b01976ce24292c64f92dc4fbe6acb80388150c98c6f62ef21db2bec6f':
    raise RuntimeError('reviewer source changed')
old = "open('/tmp/jc2-lane.jF2rfq/inputs/exact-witnesses.json')"
text = source.decode('utf-8')
if text.count(old) != 1:
    raise RuntimeError('not the declared single relocation site')
sys.argv = [str(audit)] + remainder
exec(compile(text.replace(old, 'open(ROOT_WITNESS_PATH)', 1), str(audit), 'exec'),
     {'__name__': '__main__', '__file__': str(audit),
      'ROOT_WITNESS_PATH': str(witness)})
