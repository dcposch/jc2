#!/usr/bin/env python3
"""Replay tiny inverse controls in every actual D108 production coefficient ring."""
import subprocess
from pathlib import Path

REMOTE=r"""
import datetime,hashlib,json,subprocess,time
from pathlib import Path
root=Path('/home/ubuntu/jc2/box/char-degree-20260905/d108')
out=root.parent/'resume-r2/d108-ring-controls';out.mkdir(parents=True,exist_ok=True)
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while b:=f.read(1024*1024):h.update(b)
 return h.hexdigest()
paths=sorted(root.glob('d108*circuit_stage*.sing'))+sorted(root.glob('selected/*/augmented.sing'))
records=[]
for i,source in enumerate(paths):
 with source.open() as f:ring=f.readline()
 assert ring.startswith('ring R=0,(') and ring.endswith('),dp;\n')
 names=ring.split('ring R=0,(',1)[1].split('),dp;',1)[0].split(',')
 assert all(n in names for n in ['leader63','Z63','c','Zc'])
 body='''ideal negLeader=leader63,Z63*leader63-1;
ideal posLeader=leader63-1,Z63*leader63-1;
ideal negSeparation=c,Zc*c-1;
ideal posSeparation=c-1,Zc*c-1;
print("ALL_CONTROL_ROWS_PARSED");print("BEGIN_CONTROLS");
print(reduce(1,std(negLeader)));print(reduce(1,std(posLeader)));
print(reduce(1,std(negSeparation)));print(reduce(1,std(posSeparation)));
print("END_CONTROLS");quit;
'''
 script=out/f'ring-{i:02d}.sing';log=out/f'ring-{i:02d}.out';timing=out/f'ring-{i:02d}.time'
 script.write_text(ring+body)
 start=time.monotonic()
 run=subprocess.run(['/usr/bin/time','-f','wall_seconds=%e\npeak_RSS_KiB=%M\nreturncode=%x','-o',str(timing),'Singular','-q',str(script)],capture_output=True,text=True,timeout=30)
 elapsed=time.monotonic()-start;text=run.stdout+run.stderr;log.write_text(text)
 errors=[s for s in text.splitlines() if s.lstrip().startswith('?') or 'error occurred' in s or 'Singular error:' in s]
 vals=text.split('BEGIN_CONTROLS\n',1)[1].split('\nEND_CONTROLS',1)[0].splitlines() if 'BEGIN_CONTROLS\n' in text and '\nEND_CONTROLS' in text else []
 rec=dict(source_script=str(source.relative_to(root)),source_script_sha256=sha(source),field='Q',monomial_order='dp',ring_generator_count=len(names),ring_generator_order_sha256=hashlib.sha256(('\n'.join(names)+'\n').encode()).hexdigest(),control_script=str(script),control_script_sha256=sha(script),output_sha256=sha(log),returncode=run.returncode,wall_seconds=round(elapsed,6),time_receipt=timing.read_text(),parser_all_rows='ALL_CONTROL_ROWS_PARSED' in text,parser_errors=errors,controls=vals,control_order=['leader_zero_with_inverse','leader_one_with_inverse','separation_zero_with_inverse','separation_one_with_inverse'],passed=run.returncode==0 and not errors and vals==['0','1','0','1'] and 'ALL_CONTROL_ROWS_PARSED' in text)
 records.append(rec)
result=dict(audit_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='Tiny inverse controls in actual production coefficient rings; no production ideal rerun or verdict',records=records,all_passed=all(r['passed'] for r in records))
(out/'actual-ring-controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
"""
run=subprocess.run(['ssh','-i',str(Path.home()/'.ssh/jc2-fleet'),'ubuntu@172.30.0.40','python3','-'],input=REMOTE,text=True,capture_output=True)
if run.returncode:
    print(run.stderr)
    run.check_returncode()
out=Path(__file__).resolve().parent/'audit-d108-actual-ring-controls.json'
out.write_text(run.stdout)
print(out,len(run.stdout),'bytes')
