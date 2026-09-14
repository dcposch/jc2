#!/usr/bin/env python3
"""Run both frozen tiny suites in normal and optimized modes under one deadline."""
import ast
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

LANE = Path('/tmp/jc2-lane.8nFKkf/inputs').resolve()
HERE = Path(__file__).resolve().parent


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def cap():
    resource.setrlimit(resource.RLIMIT_CPU, (12, 12))
    resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main(output):
    started = time.monotonic()
    targets = [('producer', LANE/'test_construct.py', 13), ('caller', LANE/'test_once.py', 6)]
    pins_before = {p.name: digest(p) for p in LANE.iterdir() if p.is_file()}
    runs = []
    for label, script, methods in targets:
        for optimized in (False, True):
            remaining = 30-(time.monotonic()-started)
            need(remaining > 0, 'aggregate wall deadline')
            command = [sys.executable]+(['-O'] if optimized else [])+[str(script), '-v']
            result = subprocess.run(command, cwd=HERE, capture_output=True,
                                    timeout=remaining, preexec_fn=cap,
                                    env={'PATH': '/usr/bin:/bin', 'PYTHONDONTWRITEBYTECODE': '1'})
            stdout = result.stdout.decode('utf-8')
            stderr = result.stderr.decode('utf-8')
            combined = stdout+stderr
            need(result.returncode == 0 and f'Ran {methods} tests' in combined and 'OK' in combined,
                 'frozen suite failed: '+label)
            runs.append({'suite': label, 'mode': 'optimized' if optimized else 'normal',
                         'methods': methods, 'returncode': result.returncode,
                         'stdout_sha256': hashlib.sha256(result.stdout).hexdigest(),
                         'stderr_sha256': hashlib.sha256(result.stderr).hexdigest()})
    checked = ('construct.py', 'replay.py', 'run_once.py', 'test_construct.py', 'test_once.py')
    assert_nodes = sum(sum(isinstance(n, ast.Assert) for n in ast.walk(ast.parse((LANE/name).read_bytes())))
                       for name in checked)
    need(assert_nodes == 0, 'Assert node found')
    pins_after = {p.name: digest(p) for p in LANE.iterdir() if p.is_file()}
    need(pins_after == pins_before, 'frozen inputs changed')
    record = {'status': 'PASS', 'scope': 'frozen tiny suites only; no production paths',
              'runs': runs, 'assert_nodes': assert_nodes,
              'elapsed_seconds': format(time.monotonic()-started, '.6f'),
              'input_pins_before': pins_before, 'input_pins_after': pins_after}
    with (HERE/output).open('x', encoding='utf-8') as stream:
        json.dump(record, stream, sort_keys=True, separators=(',', ':'))
        stream.write('\n')
    print(json.dumps(record, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    need(len(sys.argv) == 2 and Path(sys.argv[1]).name == sys.argv[1], 'one evidence basename')
    main(sys.argv[1])
