"""Receipt/pin checks and two unchanged tiny independent controls, no full source."""
from pathlib import Path
import datetime, hashlib, json, subprocess, time
R=Path('/home/ubuntu/jc2'); started=time.monotonic(); pins={}; runs=[]
def need(c,m):
    if not c: raise RuntimeError(m)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
for tag in ('furter-primary-gate-fable5-20260907','d125-pure-low-alpha-gate-fable5-20260907'):
    receipt=R/'xmodel'/f'{tag}.run.v2'
    d=dict(s.split('=',1) for s in receipt.read_text().splitlines() if '=' in s)
    need(all(d[k]==v for k,v in {'final_status':'DONE','exit_code':'0','seal_boundary':'CLEAN','report_state':'BODY_SEALED','charge_basis_status':'ABSENT'}.items()),'receipt '+tag)
    pins[str(receipt.relative_to(R))]=sha(receipt)
    for i in range(1,int(d['charged_inputs'])+1):
        need(d[f'charged_input_{i}_post']=='UNCHANGED','post input')
        pins[d[f'charged_input_{i}']]=d[f'charged_input_{i}_sha256']
    pins[d['report']]=d['report_sha256']
codes=[('box/furter-primary-gate-fable5-20260907/controls.py','f4213fd136bc446e159692944844e76ce24d9d76f438af7b05153994b07986b5'),
       ('box/d125-pure-low-alpha-gate-fable5-20260907/low-jet-control.py','d75a668fdc51296adb9f1cbc9f3c9b1d22d846a26f211cc713d06be9a8063979')]
pins.update(codes)
for n,h in pins.items(): need(sha(R/n)==h,'input drift '+n)
for n,h in codes:
    for mode in ([],['-O']):
        argv=['/usr/bin/python3','-I','-B']+mode+[str(R/n)]
        p=subprocess.run(argv,capture_output=True,timeout=5)
        need(p.returncode==0 and not p.stderr,'control process')
        expected='7f79a81f1b487175ebcc70dc8c939f76ea0035ec28971e47b6dd987b84a3bf95' if 'furter' in n else '68d1527eec4791799376672a1266f9837174430fe3fd90c839f43f655151eff5'
        need(hashlib.sha256(p.stdout).hexdigest()==expected,'control output')
        if 'furter' in n:
            lines=p.stdout.decode().splitlines()
            need(sum('expected=True' in s for s in lines)==18 and sum('expected=False' in s for s in lines)==17,'corrected count')
        runs.append({'argv':argv,'rc':p.returncode,'stdout_sha256':expected,'stdout':p.stdout.decode()})
for n,h in pins.items(): need(sha(R/n)==h,'post drift '+n)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pins':pins,'runs':runs,
     'seconds':time.monotonic()-started,'scope':'Furter tiny algebra; actual degree<=3 low jets. Mathematical proofs separately whole-read. No actual full-source arithmetic.',
     'corrections':['Furter count18positive17negative, not21/14','Low-alpha producer scalar/parity toys are not actual general-source or nonconstancy proofs; independent proof supplies those claims','Low-jet control return0 alone is not gate: exact expected output hash required']}
p=Path(__file__).with_suffix('.json')
with p.open('x') as f: json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(p)}))
