#!/usr/bin/env python3
"""Run bounded positive and actual-object mutation controls into this new box."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time


LIMIT_AS = 512 * 1024**2
resource.setrlimit(resource.RLIMIT_AS, (LIMIT_AS, LIMIT_AS))
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
signal.alarm(30)

ROOT = Path(__file__).resolve().parents[2]
OWN = Path(__file__).resolve().parent
AUDIT = OWN / 'audit.py'
PRODUCER_TEST = Path('/tmp/jc2-lane.MAp4nm/inputs/test_client.py')
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(name: str, args: list[str], expect_zero: bool):
    started = time.monotonic()
    completed = subprocess.run(args, cwd=ROOT, env=ENV, capture_output=True,
                               text=True, timeout=30, check=False)
    elapsed = time.monotonic() - started
    accepted = completed.returncode == 0
    if accepted != expect_zero:
        raise RuntimeError(f'{name}: unexpected exit {completed.returncode}')
    return {
        'name': name,
        'command': args,
        'expected': 'zero' if expect_zero else 'nonzero',
        'returncode': completed.returncode,
        'elapsed_seconds': elapsed,
        'stdout': completed.stdout,
        'stderr': completed.stderr,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    commands = []
    for mode, optimized in (('normal', False), ('O', True)):
        prefix = [sys.executable, '-B'] + (['-O'] if optimized else [])
        own_output = OWN / f'audit-{mode}-final-v2.json'
        commands.append(run('independent-positive-'+mode,
                            prefix+[str(AUDIT), '--output', str(own_output)], True))
        producer_output = OWN / f'producer-{mode}-v2.json'
        commands.append(run('producer-positive-'+mode,
                            prefix+[str(PRODUCER_TEST), '--output', str(producer_output)], True))
        for mutation in ('target', 'missing_row', 'footer', 'field', 'split_row',
                         'vertex', 'face'):
            commands.append(run('independent-'+mutation+'-'+mode,
                                prefix+[str(AUDIT), '--inject', mutation], False))
        for mutation in ('target', 'face'):
            unused_output = OWN / f'producer-{mutation}-{mode}-must-not-exist.json'
            commands.append(run('producer-'+mutation+'-'+mode,
                                prefix+[str(PRODUCER_TEST), '--output', str(unused_output),
                                        '--mutate', mutation], False))
    products = [OWN/'audit-normal-final-v2.json', OWN/'audit-O-final-v2.json',
                OWN/'producer-normal-v2.json', OWN/'producer-O-v2.json']
    receipt = {
        'status': 'PASS',
        'commands': commands,
        'command_count': len(commands),
        'positive_count': sum(item['returncode'] == 0 for item in commands),
        'negative_count': sum(item['returncode'] != 0 for item in commands),
        'product_sha256': {path.name: sha256(path) for path in products},
        'limits_per_child': {'wall_seconds': 30, 'cpu_seconds': 25,
                             'AS_bytes': LIMIT_AS},
        'producer_runner_used': False,
        'production_J_expanded': False,
        'production_lift_expanded': False,
        'adapter_or_solver_used': False,
    }
    output = Path(args.output)
    with output.open('x') as handle:
        json.dump(receipt, handle, sort_keys=True, indent=2)
        handle.write('\n')
    print(json.dumps({'status': 'PASS', 'commands': len(commands),
                      'positive': receipt['positive_count'],
                      'negative': receipt['negative_count']}, sort_keys=True))


if __name__ == '__main__':
    main()
