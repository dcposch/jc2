"""Opaque custody and lifecycle checks only; never parse Singular algebra."""
from pathlib import Path
import datetime, hashlib, json
B=Path(__file__).resolve().parent
E=B/'evidence'
def need(c,m):
    if not c: raise RuntimeError(m)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
t=json.loads((E/'decision.telemetry.json').read_bytes())
need(t['status']=='WALL_TIMEOUT' and t['runner_exit_code']==124,'terminal status')
need(t['termination']['cleanup_complete'] and t['termination']['leader_reaped'],'cleanup')
need(not t['termination']['group_live_before_reap'],'surviving group')
r=json.loads((E/'decision.result.json').read_bytes())
need(r['phase']=='decision' and r['runner_rc']==124,'result status')
need(r['authority_sha256']==sha(B/'solver.authority.json'),'authority')
need(r['source_pins_after']=={'jsonl':'4ea526b2680ef41154332be3059ae5543c2678fdf8fb6a95d02176e8eb929272'},'source custody')
for suffix,h in (r['artifacts']|r['outputs']).items():
    need(sha(E/('decision.'+suffix))==h,'copied output '+suffix)
i=json.loads((E/'decision.identity.json').read_bytes())
need(i['pid']==i['pgid']==t['pid']==t['pgid']==2784,'identity')
need(i['start_ticks']=='87251' and i['host']['boot']=='886172be-22d4-42e8-939c-0fc0475346fa','boot/start')
need(i['host']['instance']=='i-0da0cebfc97c9fd54','instance')
pins={str(p.relative_to(B)):sha(p) for p in sorted(E.iterdir()) if p.is_file()}
need(len(pins)==7,'seven closed artifacts')
out={'schema':'jc2.root-terminal-harvest/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'result':'CLOSED_INCONCLUSIVE','no_verification_or_retry':True,'opaque_algebra_only':True,
     'fresh_remote_group_absence_observed_utc':'2026-09-07T22:25:40Z','pins':pins,
     'generated_bytes':(E/'decision.sing').stat().st_size,'stdout_bytes':(E/'decision.stdout').stat().st_size,
     'wall_seconds':t['wall_elapsed_seconds'],'max_observed_group_rss_bytes':t['max_observed_group_rss_bytes']}
with (B/'terminal-harvest.json').open('x') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
print(json.dumps(out,sort_keys=True))
print('receipt_sha256='+sha(B/'terminal-harvest.json'))
