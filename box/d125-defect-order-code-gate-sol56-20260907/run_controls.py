#!/usr/bin/env python3
"""Run the independent checker normally and with -O under explicit caps."""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time


def need(condition, reason):
    if not condition:
        raise RuntimeError(reason)


def child_limits():
    resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
    resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2))
    resource.setrlimit(resource.RLIMIT_FSIZE, (64*1024**2, 64*1024**2))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    need(output == Path(__file__).resolve().parent, 'output must be owned evidence directory')
    script = output/'gate_check.py'
    records = []
    started_all = time.monotonic()
    before_all = resource.getrusage(resource.RUSAGE_CHILDREN)
    for name, mode in (('normal', []), ('optimized', ['-O'])):
        started = time.monotonic()
        before = resource.getrusage(resource.RUSAGE_CHILDREN)
        command = [sys.executable, '-I', '-B', *mode, str(script),
                   '--inputs', str(args.inputs.resolve())]
        completed = subprocess.run(command, capture_output=True, timeout=30,
                                   preexec_fn=child_limits, check=False)
        after = resource.getrusage(resource.RUSAGE_CHILDREN)
        need(completed.returncode == 0, name+' failed: '+completed.stderr.decode(errors='replace'))
        need(completed.stderr == b'', name+' emitted stderr')
        payload = json.loads(completed.stdout)
        need(payload.get('status') == 'PASS', name+' checker status')
        record = {'mode': name, 'returncode': completed.returncode,
                  'wall_seconds': time.monotonic()-started,
                  'child_cpu_seconds': (after.ru_utime+after.ru_stime)-
                                       (before.ru_utime+before.ru_stime),
                  'maxrss_kib': after.ru_maxrss, 'command': command,
                  'result': payload}
        path = output/(name+'.json')
        with path.open('xb') as stream:
            stream.write((json.dumps(record, sort_keys=True, separators=(',', ':'))+'\n').encode())
        records.append({'mode': name, 'sha256': digest(path),
                        'wall_seconds': record['wall_seconds'],
                        'child_cpu_seconds': record['child_cpu_seconds'],
                        'maxrss_kib': record['maxrss_kib'],
                        'checks': payload['checks']})
    after_all = resource.getrusage(resource.RUSAGE_CHILDREN)
    summary = {'status': 'PASS', 'runs': records,
               'total_wall_seconds': time.monotonic()-started_all,
               'total_child_cpu_seconds': (after_all.ru_utime+after_all.ru_stime)-
                                          (before_all.ru_utime+before_all.ru_stime),
               'caps': {'wall_seconds_each': 30, 'cpu_seconds_each': 25,
                        'as_bytes_each': 512*1024**2}}
    path = output/'run.json'
    with path.open('xb') as stream:
        stream.write((json.dumps(summary, sort_keys=True, separators=(',', ':'))+'\n').encode())
    print(json.dumps({**summary, 'run_sha256': digest(path),
                      'gate_check_sha256': digest(script),
                      'run_controls_sha256': digest(Path(__file__).resolve())}, sort_keys=True))


if __name__ == '__main__':
    main()
