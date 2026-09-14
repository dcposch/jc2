"""Ordinary-only metadata replay of the named runtime gate's digest/count doubt.

No polynomial work, child processes, network, worker control or file writes.
Read exact retained files only. Initial review output used the wrong encoding;
the final output corrected it. This independently replays that correction.
"""
import hashlib
import json
import resource
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
resource.setrlimit(resource.RLIMIT_AS, (128 * 1024**2, 128 * 1024**2))
base = Path('/home/ubuntu/jc2/box/f10-r1-engineering-v2-execution-20260909/remote')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read(name):
    return json.loads((base / name).read_bytes())

assert digest(base / 'batch.PASS.json') == 'cb811b3463b412a04d8d32c6a475499940c5fd9f531ebeec9035c7b8ca0ddd47'
records = read('batch.PASS.json')['records']
assert len(records) == 16
mathematical = []
for record in records:
    name = record['name']
    assert record == read(name + '.dispatch.json')
    assert record['authority_sha256'] == digest(base / (name + '.authority.json'))
    assert record['telemetry_sha256'] == digest(base / (name + '.telemetry.json'))
    authority = read(name + '.authority.json')
    telemetry = read(name + '.telemetry.json')
    payload = json.dumps(authority['child_argv'], ensure_ascii=False, separators=(',', ':')).encode('utf-8') + b'\n'
    assert hashlib.sha256(payload).hexdigest() == telemetry['argv_sha256']
    assert len(authority['child_argv']) == telemetry['argv_count']
    for stream in ('stdout', 'stderr'):
        file = base / Path(telemetry[stream]['path']).name
        assert digest(file) == telemetry[stream]['sha256']
        assert file.stat().st_size == telemetry[stream]['bytes']
    assert record['remaining_group_live'] == []
    assert telemetry['termination']['group_live_before_reap'] == []
    assert telemetry['pid'] == telemetry['pgid']
    for path, sha in authority['file_sha256'].items():
        local = Path('/usr/bin/python3') if path == '/usr/bin/python3' else base / Path(path).name
        assert digest(local) == sha
    if record['mathematical']:
        mathematical.append(name)
        assert record['returncode'] == telemetry['runner_exit_code'] == 0
        assert telemetry['status'] == 'NORMAL_EXIT'
        assert record['hard_cutoff_epoch'] == 1788960900.0
        assert record['returned_epoch'] < record['hard_cutoff_epoch']
        assert authority['enabled'] is True
        assert authority['hostname'] == 'ip-172-30-0-72'
        assert authority['instance_id'] == 'i-08d2a40f272ee9fa2'
        if name != 'build':
            assert authority['file_sha256'][authority['cwd'] + '/exact.json'] == '168bdfd3a791f24a6631de66ae4e71c3f209ee9eb0d21fc466f9aa802f5ad576'
    print(name, 'DIGEST_AND_BINDINGS_PASS')
assert len(mathematical) == 9
assert mathematical[0] == 'build' and mathematical[-1] == 'precision'
assert sum(name.startswith('check-') for name in mathematical) == 7
print('PASS: 16 argv digests; 9 mathematical operations = 1 build + 7 checks + 1 precision')
