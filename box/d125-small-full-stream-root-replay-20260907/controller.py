"""One root-authorized dummy regression and one full-source verification."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import replay as r

ROOT = r.ROOT
RUNNER = '4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2'

def absent(pgid):
    for attempt in range(20):
        lines = subprocess.check_output(['ps', '-eo', 'pid=,pgid=,stat='], text=True).splitlines()
        if not any(int(line.split()[1]) == pgid for line in lines):
            return True
        time.sleep(.1)
    return False

def run(mode, seconds, cpu, rss):
    command = [sys.executable, '-B', str(ROOT/'run_capped.py'), '--cwd', str(ROOT),
               '--wall-seconds', str(seconds), '--cpu-seconds', str(cpu), '--rss-bytes', str(rss),
               '--term-grace-seconds', '.25', '--rss-sample-seconds', '.05',
               '--stdout-file', mode+'.stdout', '--stderr-file', mode+'.stderr',
               '--telemetry-file', mode+'.telemetry.json', '--', sys.executable, '-B', str(ROOT/'replay.py'), mode]
    r.save(mode+'.launch.json', {'command': command, 'utc': time.time()})
    result = subprocess.run(command, capture_output=True, text=True)
    telemetry = json.loads(Path(mode+'.telemetry.json').read_bytes())
    quiet = absent(telemetry['pgid'])
    receipt = {'runner_rc': result.returncode, 'runner_stdout': result.stdout, 'runner_stderr': result.stderr,
               'telemetry': telemetry, 'group_absent': quiet, 'outputs': {suffix: r.sha(mode+'.'+suffix)
               for suffix in ('stdout', 'stderr', 'telemetry.json')}}
    r.save(mode+'.receipt.json', receipt)
    r.need(quiet, 'group remains')
    r.need(telemetry['error'] is None, 'runner error')
    if mode == 'dummy':
        child = json.loads(Path('dummy.descendant.json').read_bytes())
        r.need(telemetry['status'] == 'WALL_TIMEOUT' and result.returncode == 124, 'dummy cap')
        r.need(child['pgid'] == telemetry['pgid'] and child['boot'] == r.BOOT, 'dummy namespace/PGID')
        r.need(child['pid_namespace'] == os.readlink('/proc/self/ns/pid'), 'dummy PID namespace')
        r.need(telemetry['max_observed_group_rss_bytes'] >= 32*1024**2, 'descendant RSS absent')
        r.need(telemetry['termination']['kill_sent'] and telemetry['termination']['cleanup_complete'], 'dummy cleanup')
    else:
        r.need(telemetry['status'] == 'NORMAL_EXIT' and result.returncode == 0 and telemetry['child_returncode'] == 0, 'verification failed')
        r.need(Path(mode+'.stderr').stat().st_size == 0, 'verification stderr')
    return receipt

def main():
    r.save('controller.identity.json', r.identity())
    r.need(r.sha(ROOT/'run_capped.py') == RUNNER, 'runner pin')
    manifest = json.loads((ROOT/'code-pins.json').read_bytes())
    for name, digest in manifest.items():
        r.need('/' not in name and r.sha(ROOT/name) == digest, 'code pin '+name)
    run('dummy', 2, 5, 512*1024**2)
    run('verify', 600, 600, 8*1024**3)
    for name, digest in manifest.items():
        r.need(r.sha(ROOT/name) == digest, 'post code pin '+name)
    r.save('complete.json', {'status': 'PASS', 'utc': time.time(), 'code_pins': manifest})

if __name__ == '__main__':
    main()
