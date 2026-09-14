"""Receipt-first metadata collection; no report text is emitted or interpreted."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess
R = Path('/home/ubuntu/jc2')
B = R / 'box/ideation-20260907T2200Z'
def need(ok, msg):
    if not ok: raise RuntimeError(msg)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def run(argv):
    c = subprocess.run(argv, capture_output=True, timeout=15)
    need(c.returncode == 0, repr((argv, c.returncode, c.stderr)))
    return c.stdout.decode()
out = {'schema': 'jc2.blind-collection/v1',
       'started_utc': datetime.now(timezone.utc).isoformat(),
       'peer_bodies_read_before_collection': False,
       'root_prior_terminal_observation': {'fable5': '2026-09-07T22:14:36Z',
         'astra': '2026-09-07T22:19:05Z', 'sol56': '2026-09-07T22:19:05Z',
         'reported_state': 'inactive/dead/exit0'}, 'lanes': {}}
for who in ('astra','fable5','sol56'):
    tag = 'ideation-20260907T2200Z-' + who
    unit = 'jc2-lane-' + tag + '.service'
    state = run(['systemctl','--user','show',unit,'--no-pager',
       '-p','Id','-p','LoadState','-p','ActiveState','-p','SubState',
       '-p','Result','-p','ExecMainPID','-p','ExecMainStatus',
       '-p','ExecMainExitTimestamp','-p','ControlGroup'])
    st = dict(line.split('=',1) for line in state.splitlines() if '=' in line)
    need(st['Id'] == unit and st['ActiveState'] == 'inactive' and
         st['SubState'] == 'dead' and st['ExecMainPID'] == '0', 'not terminal')
    receipt_path = R / ('xmodel/' + tag + '.run.v2')
    raw = receipt_path.read_text()
    rows = [line.split('=',1) for line in raw.splitlines() if '=' in line]
    v = dict(rows)
    need(len(v) == len(rows), 'duplicate receipt key')
    for key, value in {'tag':tag,'charged_inputs':'18','final_status':'DONE',
      'exit_code':'0','adapter_exit_code':'0','report_state':'BODY_SEALED',
      'seal_boundary':'CLEAN','charge_basis_status':'ABSENT'}.items():
        need(v.get(key) == value, 'receipt state ' + key)
    pins = []
    for i in range(1,19):
        key = 'charged_input_' + str(i)
        p = R / v[key]
        current = sha(p)
        need(v[key+'_post'] == 'UNCHANGED' and current == v[key+'_sha256'],
             'input drift ' + str(p))
        pins.append({'path':v[key], 'sha256':current, 'bytes':p.stat().st_size})
    for key in ('report','prompt','log'):
        p = Path(v[key]); p = p if p.is_absolute() else R/p
        current = sha(p)
        need(current == v[key+'_sha256'], key+' drift')
        pins.append({'path':str(p.relative_to(R)), 'sha256':current,
                     'bytes':p.stat().st_size})
    absence = {key: not Path('/proc/'+v[key]).exists() for key in ('pid','child_pid')}
    need(all(absence.values()), 'original PID exists; identity review required')
    out['lanes'][who] = {'unit':unit,'systemd':st,
      'fresh_state_scope':'collected/not-found is not a fresh historical exit proof'
          if st['LoadState']=='not-found' else 'terminal unit',
      'receipt_raw':raw,'receipt_sha256':sha(receipt_path),
      'current_pins':pins,'original_pid_absence':absence}
out['journal'] = run(['journalctl','--user','--since','2026-09-07 22:00:00 UTC',
 '--until','2026-09-07 22:20:00 UTC','--no-pager','-o','short-iso',
 '--grep','ideation-20260907T2200Z'])
out['root_blind_transaction'] = json.loads(run(['/usr/bin/python3','-B',
 str(R/'ops/artifact_finalize.py'),'verify','--final',
 str(R/'xmodel/ideation-20260907T2200Z-coordinator.md')]))
need(out['root_blind_transaction']['full_sha256'] ==
 'c35e775e8295f5e5f6a0e5fa630820f81da95545c0940320136c0afd39827033',
 'root blind drift')
out['completed_utc'] = datetime.now(timezone.utc).isoformat()
name = 'collection-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-astra.json'
with (B/name).open('x') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
print(json.dumps({'path':str((B/name).relative_to(R)), 'sha256':sha(B/name),
 'completed_utc':out['completed_utc'],'input_pin_checks':54,
 'report_pin_checks':3,'status':'COLLECTED_BEFORE_PEER_BODY_READS'}))
