"""Replay both byte-copied checkers under direct prlimit + subprocess(timeout=30).
Compare rc, stdout bytes, and terminal error line against the charged replay JSONs."""
import hashlib, json, subprocess, sys, time
from pathlib import Path
BOX = Path('/home/ubuntu/jc2/box/golden-nonh-composition-gate-fable5-20260908')
LANE = Path('/tmp/jc2-lane.mRFR0l/inputs')
def sha(b): return hashlib.sha256(b).hexdigest()
def last_line(s):
    lines = [l for l in s.splitlines() if l.strip()]
    return lines[-1] if lines else ''
plan = [
  ('source', BOX/'scratch'/'source-check.py', json.loads((LANE/'source-replay.json').read_text()),
   ['positive','--wrong-critical-shift','--drop-constant','--drop-half-loss','--drop-split-sign']),
  ('consumer', BOX/'scratch'/'consumer-check.py', json.loads((LANE/'consumer-replay.json').read_text()),
   ['positive','wrong-quintic-factor','wrong-face-sign','wrong-target-factor','drop-resonant-target']),
]
out = {'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'runs': [], 'all_match': True}
t0 = time.time()
for name, script, expected_json, modes in plan:
    exp_runs = expected_json['runs']
    for opt in ([], ['-O']):
        for mode in modes:
            argv = ['/usr/bin/prlimit', '--cpu=25', '--as=536870912', '--', '/usr/bin/python3', '-I', '-B'] + opt + [str(script), mode]
            t1 = time.time()
            try:
                cp = subprocess.run(argv, capture_output=True, timeout=30)
                rc, so, se, timed_out = cp.returncode, cp.stdout, cp.stderr, False
            except subprocess.TimeoutExpired as ex:
                rc, so, se, timed_out = None, ex.stdout or b'', ex.stderr or b'', True
            dt = time.time() - t1
            # locate the charged expectation: same mode and same -O presence
            exp = None
            for r in exp_runs:
                a = r['argv']
                if a[-1] == mode and (('-O' in a) == bool(opt)):
                    exp = r; break
            so_s, se_s = so.decode('utf-8', 'replace'), se.decode('utf-8', 'replace')
            match_rc = (exp is not None and rc == exp['rc'])
            match_stdout = (exp is not None and so_s == exp['stdout'])
            match_err = (exp is not None and last_line(se_s) == last_line(exp['stderr']))
            ok = match_rc and match_stdout and match_err and not timed_out
            out['all_match'] &= ok
            out['runs'].append({'checker': name, 'mode': mode, 'optimize': bool(opt), 'argv': argv,
                'rc': rc, 'seconds': round(dt, 4), 'timed_out': timed_out,
                'stdout_sha256': sha(so), 'stderr_sha256': sha(se),
                'stdout': so_s, 'stderr_last_line': last_line(se_s),
                'expected_rc': None if exp is None else exp['rc'],
                'expected_stdout_sha256': None if exp is None else sha(exp['stdout'].encode()),
                'expected_stderr_last_line': None if exp is None else last_line(exp['stderr']),
                'match_rc': match_rc, 'match_stdout_bytes': match_stdout, 'match_terminal_error': match_err, 'ok': ok})
out['elapsed_seconds'] = round(time.time() - t0, 3)
out['scratch_pins'] = {p.name: sha(p.read_bytes()) for p in [BOX/'scratch'/'source-check.py', BOX/'scratch'/'consumer-check.py']}
(BOX/'replay'/'replay.json').write_text(json.dumps(out, indent=1, sort_keys=True))
for r in out['runs']:
    print(f"{r['checker']:8s} {r['mode']:24s} -O={int(r['optimize'])} rc={r['rc']} exp_rc={r['expected_rc']} stdout_match={int(r['match_stdout_bytes'])} err_match={int(r['match_terminal_error'])} ok={int(r['ok'])} {r['seconds']}s")
print('ALL_MATCH', out['all_match'], 'elapsed', out['elapsed_seconds'])
