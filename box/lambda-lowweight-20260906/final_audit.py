#!/usr/bin/env python3
"""Read-only evidence checks, then atomic receipt; run only after seal/shutdown."""
import datetime
import gzip
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPORT = ROOT / 'xmodel/lambda-lowweight-astra-20260906.md'
RUN_RECEIPT = ROOT / 'xmodel/lambda-lowweight-astra-20260906.run.v2'
FINAL = HERE / 'final-audit.json'
FROZEN = Path('/tmp/jc2-lane.IZAvbL/inputs')
EXPECTED_DRIVER = 'b6e7f6aab8b6e6711031bcb0da4dcd32961b9ae0384566e1bd331729257abc1f'
EXPECTED_CHARGE_AUDIT = 'ed7496e3b52f2fcfd82c86b46aca20943c595c54eef59581ace6d8f98461c6df'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_json(name):
    return json.loads((HERE / name).read_text())


def timestamp(value):
    return datetime.datetime.fromisoformat(value.replace('Z', '+00:00'))


def check_formulas(cases):
    """Check compressed custody AND every decompressed formula, without CAS."""
    leaders = {r['id']: r for r in read_json('leaders.json')}
    ux = {r['id']: r for r in read_json('UX.json')['cases']}
    assert len(cases) == len(leaders) == len(ux) == 10
    normalized = {}
    for case in cases:
        leader = leaders[case.get('class_id', case['id'])]
        for key in ('lambda_path', 'lambda_sha256', 'lambda_compressed_sha256',
                    'K', 'e', 'q', 'n', 'm', 'D2', 'W', 'J', 'a'):
            assert case[key] == leader[key], (case['id'], key)
        packed = (ROOT / leader['lambda_path']).read_bytes()
        assert sha(packed) == leader['lambda_compressed_sha256'], case['id']
        assert len(packed) == leader['lambda_compressed_bytes'], case['id']
        raw = gzip.decompress(packed)
        assert sha(raw) == leader['lambda_sha256'], case['id']
        assert len(raw) == leader['lambda_bytes'], case['id']
        normalized[case['id']] = sha(raw.decode().strip().encode())
        reduced = ux[case['id']]
        assert reduced['original_lambda_sha256'] == leader['lambda_sha256']
        assert reduced['original_lambda_path'] == leader['lambda_path']
        packed = (ROOT / reduced['reduced_lambda_path']).read_bytes()
        assert sha(packed) == reduced['reduced_lambda_compressed_sha256']
        assert sha(gzip.decompress(packed)) == reduced['reduced_lambda_sha256']
    return normalized


def process_snapshot():
    result = {}
    for entry in Path('/proc').iterdir():
        if not entry.name.isdecimal():
            continue
        try:
            fields = (entry / 'stat').read_text().rsplit(')', 1)[1].split()
            argv = (entry / 'cmdline').read_bytes().split(b'\0')
            result[int(entry.name)] = {
                'state': fields[0], 'ppid': int(fields[1]), 'pgid': int(fields[2]),
                'argv': [a.decode(errors='replace') for a in argv if a],
            }
        except (FileNotFoundError, ProcessLookupError, PermissionError):
            pass
    return result


def check_shutdown(receipts, driver_sha):
    """Inspect identities only: no signals and no writes to /proc."""
    shutdown = read_json('shutdown-owned.json')
    assert shutdown['status'] == 'STOPPED'
    assert shutdown['driver_sha256'] == driver_sha
    assert not shutdown.get('active_pids') and not shutdown.get('active_process_groups')
    assert set(shutdown['queue_receipts']) == {'postheavy-owned.json', 'final-c455-owned.json'}
    known_pids = set(shutdown.get('historical_pids', []))
    groups = set()
    for _, data in receipts:
        for key in ('runner_pid', 'process_pid'):
            if isinstance(data.get(key), int):
                known_pids.add(data[key])
        if isinstance(data.get('process_group'), int):
            groups.add(data['process_group'])
    queues = []
    for name in shutdown['queue_receipts']:
        queue = read_json(name)
        assert queue['driver_sha256'] == driver_sha, name
        assert not queue.get('active_driver_pids') and not queue.get('active_driver_pid'), name
        assert not queue.get('halted_for_unit_candidate') and not queue.get('halted_for_review'), name
        known_pids.add(queue['scheduler_pid'])
        for job in queue['finished_jobs']:
            assert job['status'] not in ('OPEN_QUEUE_ERROR', 'OPEN_QUEUE_DRIVER_ERROR',
                                         'OPEN_DRIVER_ERROR', 'UNIT_CANDIDATE_NEEDS_COFACTORS'), job
            result = read_json(job['receipt'])
            assert result['status'] == job['status'], job
            assert result['driver_sha256'] == driver_sha, job
            assert result.get('process_pid') == job.get('process_pid'), job
            assert result.get('process_group') == job.get('process_group'), job
            if isinstance(job.get('driver_pid'), int):
                known_pids.add(job['driver_pid'])
            if isinstance(job.get('process_group'), int):
                groups.add(job['process_group'])
        queues.append({'receipt': name, 'sha256': sha((HERE / name).read_bytes()),
                       'finished_jobs': len(queue['finished_jobs'])})
    snapshot = process_snapshot()
    # The caller shell may name this audit; ancestors are not compute workers.
    ancestors = set()
    pid = os.getpid()
    while pid in snapshot and pid not in ancestors:
        ancestors.add(pid)
        pid = snapshot[pid]['ppid']
    # Include every retained lane wrapper, including schedulers added after this helper.
    worker_names = {path.name for path in HERE.glob('*.py')}
    live_owned, reused_or_unrelated = [], []
    for pid, proc in snapshot.items():
        if pid in ancestors or proc['state'] == 'Z':
            continue
        names = {Path(arg).name for arg in proc['argv']}
        lane_named = any(str(HERE) in arg or 'box/lambda-lowweight-20260906/' in arg
                         for arg in proc['argv'])
        worker = bool(worker_names & names)
        singular = any(name.lower() == 'singular' for name in names)
        recorded = pid in known_pids or proc['pgid'] in groups
        if (lane_named and worker) or (recorded and (worker or singular)):
            live_owned.append({'pid': pid, 'pgid': proc['pgid'], 'argv': proc['argv']})
        elif pid in known_pids:
            reused_or_unrelated.append(pid)
    assert not live_owned, ('lane-owned work remains alive', live_owned)
    return {'status': 'STOPPED', 'checked_recorded_pids': len(known_pids),
            'checked_recorded_cas_groups': len(groups), 'live_owned_workers': 0,
            'unrelated_or_reused_pids_not_signalled': reused_or_unrelated,
            'queues': queues, 'shutdown_receipt_sha256': sha((HERE / 'shutdown-owned.json').read_bytes()),
            'limitation': 'Read-only /proc identity inspection at audit time; historical PID reuse is not treated as lane ownership.'}


def atomic_receipt(output, report_bytes):
    """Include this receipt in the disk budget and preserve any old valid file."""
    base = sum(p.stat().st_size for p in HERE.rglob('*') if p.is_file() and p != FINAL)
    output['lane_bytes_including_this_receipt'] = 0
    output['report_and_lane_bytes'] = 0
    for _ in range(10):
        blob = (json.dumps(output, indent=2) + '\n').encode()
        lane_bytes = base + len(blob)
        if output['lane_bytes_including_this_receipt'] == lane_bytes:
            break
        output['lane_bytes_including_this_receipt'] = lane_bytes
        output['report_and_lane_bytes'] = lane_bytes + report_bytes
    else:
        raise AssertionError('receipt byte-size fixed point did not converge')
    assert output['report_and_lane_bytes'] <= 2_000_000, output['report_and_lane_bytes']
    fd, temporary = tempfile.mkstemp(prefix='.final-audit.', suffix='.tmp', dir=HERE)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(blob)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, FINAL)
        directory = os.open(HERE, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        Path(temporary).unlink(missing_ok=True)
    assert FINAL.read_bytes() == blob
    assert sum(p.stat().st_size for p in HERE.rglob('*') if p.is_file()) == lane_bytes


def main():
    run_meta = dict(line.split('=', 1) for line in RUN_RECEIPT.read_text().splitlines() if '=' in line)
    expected_manifest = ''.join(
        f'{run_meta[f"charged_input_{i}_sha256"]}  {FROZEN / run_meta[f"charged_input_{i}_basename"]}\n'
        for i in range(1, 9))
    assert (HERE / 'inputs.sha256').read_text() == expected_manifest
    checked = subprocess.run(['sha256sum', '-c', str(HERE / 'inputs.sha256')],
                             text=True, capture_output=True, check=True)
    assert checked.stdout.count(': OK') == 8
    driver_sha = sha((HERE / 'run_truncated.py').read_bytes())
    assert driver_sha == EXPECTED_DRIVER
    assert sha((HERE / 'chargezero-independent-audit.json').read_bytes()) == EXPECTED_CHARGE_AUDIT
    independent = read_json('chargezero-independent-audit.json')
    assert independent['status'] == 'PASS' and independent['run_count'] == 30
    assert independent['driver_sha256'] == driver_sha
    assert independent['fresh_final_driver_replay'] and independent['all_loaded_driver_hashes_equal_current']
    assert independent['run_cases_sha256'] == sha((HERE / 'run_cases.json').read_bytes())
    cases = read_json('run_cases.json')
    normalized = check_formulas(cases)
    receipts, receipt_hashes = [], {}
    for path in sorted(HERE.glob('*.json')):
        if path == FINAL:
            continue
        raw = path.read_bytes()
        data = json.loads(raw)
        if not isinstance(data, dict):
            continue
        peak, elapsed = data.get('peak_rss_bytes'), data.get('wall_seconds')
        if isinstance(peak, (int, float)):
            assert 0 <= peak <= 16 * 1024**3, (path.name, peak)
        if isinstance(elapsed, (int, float)):
            assert 0 <= elapsed <= 2400, (path.name, elapsed)
        if 'cutoff' not in data or 'N' not in data:
            continue
        status = data.get('status', '')
        assert status != 'UNIT_CANDIDATE_NEEDS_COFACTORS', ('unresolved unit candidate', path.name)
        if status.startswith('OPEN_'):
            assert data.get('completed_homogeneous_weight') is None, path.name
        if status == 'COMPLETE_TRUNCATED_NONUNIT':
            assert data['input_ready'] and data['run_complete'] and data['std_done'], path.name
            assert data['returncode'] == 0 and not data['singular_errors'], path.name
            assert not data['emitter_errors'] and data['stop_reason'] is None, path.name
            assert data['nf_is_zero'] == 0, path.name
            assert data['completed_homogeneous_weight'] == data['cutoff'], path.name
        if status == 'EXACT_TARGET_BOUND_BELOW_KELLER_ROW':
            source = read_json(data['source_receipt'])
            assert source['charge_zero_target_component'] and source['nf_is_query'] == 1
            assert data['cutoff'] == source['cutoff'] < data['keller_row_weight']
            assert not data['std_done'] and not data['full_std_done']
        if status == 'REUSED_IDENTICAL_PRESENTATION':
            source_raw = (HERE / data['source_receipt']).read_bytes()
            assert sha(source_raw) == data['source_receipt_sha256'], path.name
            assert sha((HERE / data['identity_receipt']).read_bytes()) == data['identity_receipt_sha256'], path.name
            source = json.loads(source_raw)
            assert source['status'] == data['source_status'], path.name
            for key in ('cutoff', 'N', 'W', 'completed_homogeneous_weight', 'std_done',
                        'run_complete', 'input_ready', 'rows_sha256', 'lambda_sha256'):
                assert source.get(key) == data.get(key), (path.name, key)
        receipts.append((path.name, data))
        receipt_hashes[path.name] = sha(raw)
    bundle = hashlib.sha256()
    for case in cases:
        for power in (1, 2, 3):
            name = f'{case["id"]}.charge0.N{power}.json'
            raw = (HERE / name).read_bytes()
            bundle.update(name.encode() + b'\0' + raw)
            data = json.loads(raw)
            assert data['status'] == 'COMPLETE_TRUNCATED_NONUNIT'
            assert data['driver_sha256'] == driver_sha
            assert data['basis_size'] == 1 and data['nf_is_query'] == 1
            assert data['cutoff'] == power * case['W'] + 3
            assert data['selected_rows'] == 0 and data['charge_zero_target_component']
            assert not data['keller_localizer'] and not data['necessary_attainment_UX']
            assert data['lambda_sha256'] == normalized[case['id']]
    assert bundle.hexdigest() == independent['ordered_result_bundle_sha256']
    best = read_json('best-results.json')
    assert best['driver_sha256'] == driver_sha
    assert best['record_count'] == len(best['records'])
    for record in best['records']:
        assert record['receipt_sha256'] == receipt_hashes[record['receipt']], record['receipt']
    shutdown = check_shutdown(receipts, driver_sha)
    assert sha((ROOT / run_meta['seal_tool']).read_bytes()) == run_meta['seal_tool_sha256']
    report = REPORT.read_bytes()
    seal = subprocess.run([sys.executable, str(ROOT / run_meta['seal_tool']), 'verify',
                           '--expected-basis', run_meta['basis'], str(REPORT)],
                          text=True, capture_output=True, check=True)
    assert seal.stdout.startswith('PASS '), seal.stdout
    assert REPORT.read_bytes() == report, 'report changed during seal verification'
    assert 12000 <= len(report) <= 25000, len(report)
    assert b'@@' not in report
    now = datetime.datetime.now(datetime.timezone.utc)
    shutdown_time = timestamp(read_json('shutdown-owned.json')['checked_utc'])
    assert shutdown_time <= now
    assert shutdown_time.timestamp() <= REPORT.stat().st_mtime + 1, 'shutdown receipt must precede sealing'
    elapsed = (now - timestamp(run_meta['start_utc'])).total_seconds()
    assert 0 <= elapsed <= 200 * 60, elapsed
    output = {
        'status': 'PASS', 'checked_utc': now.isoformat().replace('+00:00', 'Z'),
        'frozen_inputs_verified': 8, 'checked_run_receipts': len(receipts),
        'chargezero_completed_runs': 30, 'chargezero_bundle_sha256': bundle.hexdigest(),
        'chargezero_independent_audit_sha256': EXPECTED_CHARGE_AUDIT,
        'driver_sha256': driver_sha, 'audit_driver_sha256': sha(Path(__file__).read_bytes()),
        'campaign_run_receipt_sha256': sha(RUN_RECEIPT.read_bytes()),
        'best_results_sha256': sha((HERE / 'best-results.json').read_bytes()),
        'original_and_UX_gzip_formulas_verified': 20,
        'report_bytes': len(report), 'report_sha256': sha(report),
        'canonical_seal_verification': seal.stdout.strip(), 'expected_frozen_basis': run_meta['basis'],
        'elapsed_from_receipt_start_seconds': round(elapsed, 3), 'shutdown': shutdown,
        'resource_checks': 'Retained numerical run peaks <=16 GiB and durations <=2400 s; missing historical metrics remain unknown. Overall audit before 200 min from receipt start.',
        'boundary': 'Evidence consistency and completed target-component checks; no source realization or class exclusion is asserted.',
        'run_receipt_sha256': receipt_hashes,
    }
    assert REPORT.read_bytes() == report and sha((HERE / 'run_truncated.py').read_bytes()) == driver_sha
    atomic_receipt(output, len(report))
    print(json.dumps({k: v for k, v in output.items() if k != 'run_receipt_sha256'}))


if __name__ == '__main__':
    main()
