#!/usr/bin/env python3
"""Send independent acceptance reader via SSH stdin; worker remains read-only."""
from pathlib import Path
import hashlib,json,subprocess,sys
HERE=Path(__file__).resolve().parent
control=HERE/'strict_acceptance_control.py'
remote='__name__="strict_acceptance_remote"\n'+control.read_text()+r'''
import datetime
ROOT=Path('/home/ubuntu/jc2/box/char-degree-20260905')
def sha_path(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while b:=f.read(1048576):h.update(b)
 return h.hexdigest()
def readj(p):return json.loads(p.read_text())
def run_record(metadata,log,script,category,base_metadata=None):
 m=readj(metadata); mm=readj(base_metadata) if base_metadata else m;cas=m if base_metadata else m.get('cas',{})
 before=log.stat() if log.exists() else None;raw=log.read_bytes() if log.exists() else b'';text=raw.decode('utf8','replace');after=log.stat() if log.exists() else None
 loghash=hashlib.sha256(raw).hexdigest();scripthash=sha_path(script) if script.exists() else None
 script_bound=scripthash==m.get('script_sha256');output_bound=loghash==cas.get('log_sha256')
 unchanged=before is not None and (before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns)
 result=inspect_log(text,cas.get('returncode'),script_bound and output_bound and unchanged,sum(mm['counts'].values()))
 return {'category':category,'metadata':str(metadata.relative_to(ROOT)),'metadata_sha256':sha_path(metadata),'raw_status':m.get('status'),'output':str(log.relative_to(ROOT)),'output_bytes':len(raw),'output_sha256':loghash,'output_matches_receipt':output_bound,'output_stable_during_read':unchanged,'script_sha256':scripthash,'script_matches_receipt':script_bound,'expected_rows':sum(mm['counts'].values()),'acceptance':result}
records=[]
for metadata in sorted((ROOT/'g9966/circuit-runs').glob('*/augmented.circuit.json')):
 records.append(run_record(metadata,metadata.with_suffix('.out'),metadata.with_suffix('').with_suffix('.sing'),'99 schedule'))
for metadata in sorted((ROOT/'d108').glob('d108*circuit_stage*.circuit.json')):
 records.append(run_record(metadata,metadata.with_suffix('.out'),metadata.with_suffix('').with_suffix('.sing'),'D108 schedule'))
for base,pattern,category in [(ROOT/'g9966','circuit-selected/*/result.json','99 selected'),(ROOT/'d108','selected/*/result.json','D108 selected')]:
 for metadata in sorted(base.glob(pattern)):
  m=readj(metadata);script=Path(m['script']);script=script if script.is_absolute() else (ROOT.parents[1]/script if script.parts[0]=='box' else base/script)
  records.append(run_record(metadata,metadata.parent/'singular.out',script,category,metadata.parent/'base.circuit.json'))
print(json.dumps({'audit_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Independent read-only acceptance parsing of actual worker output bytes; no solver rerun and no source-chart adequacy inference. Missing completion, parser/CAS/termination errors, rc!=0, or missing custody cannot become unit/proper.','worker':'172.30.0.40','counts':{'records':len(records),'complete_clean_candidates':sum(r['acceptance']['verdict'].startswith('COMPLETE_CLEAN_') for r in records)},'records':records},indent=2))
'''
p=subprocess.run(['ssh','-i',str(Path.home()/'.ssh/jc2-fleet'),'ubuntu@172.30.0.40','env','PYTHONDONTWRITEBYTECODE=1','python3','-'],input=remote,text=True,capture_output=True,timeout=60)
if p.returncode:raise RuntimeError(p.stderr)
result=json.loads(p.stdout);result['reader_source_sha256']=hashlib.sha256(control.read_bytes()).hexdigest();result['remote_executed_source_sha256']=hashlib.sha256(remote.encode()).hexdigest()
(HERE/'strict-acceptance-remote.executed.py').write_text(remote)
name=sys.argv[1] if len(sys.argv)>1 else 'strict-acceptance-production.json'
(HERE/name).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'output':name,'audit_utc':result['audit_utc'],'counts':result['counts']}))
