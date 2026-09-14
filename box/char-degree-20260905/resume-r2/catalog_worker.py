#!/usr/bin/env python3
"""Compact status inventory; hash large artifacts in place, never export them."""
import collections,datetime,hashlib,json
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2/box/char-degree-20260905')
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(1048576),b''): h.update(chunk)
 return h.hexdigest()
records=[]
for p in sorted(ROOT.rglob('*.json')):
 if p.stat().st_size>2_000_000 or 'resume-r2' in p.parts: continue
 try: o=json.loads(p.read_text())
 except (ValueError,OSError): continue
 if not isinstance(o,dict) or not isinstance(o.get('status'),str): continue
 cas=o.get('cas',{})
 if not isinstance(cas,dict): cas={}
 r=dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,metadata_sha256=sha(p),status=o['status'],control='control' in str(p).lower(),quarantined='invalid-pre-control' in p.parts,cas=cas)
 for k in ('field','coefficient_field','script','script_sha256','input','input_sha256','driver_sha256','returncode','rc','elapsed_seconds','wall_seconds','timeout','last_progress','log_sha256','wall_limit_seconds','memory_limit_gib','script_hash_unchanged','parser_or_cas_errors','started_unix'):
  if k in o:r[k]=o[k]
 for k in ('ring_generator_order','ring_generators','variables'):
  if isinstance(o.get(k),list):
   r['ordered_generators']=dict(source_field=k,count=len(o[k]),sha256=hashlib.sha256(json.dumps(o[k],separators=(',',':')).encode()).hexdigest(),encoding='compact JSON list, UTF-8')
   break
 for k in ('counts','row_counts','localizers','localizer_rows','ring_order','monomial_order'):
  if k in o:r[k]=o[k]
 def resolve(v):
  if not isinstance(v,str):return None
  q=Path(v)
  for x in (q if q.is_absolute() else p.parent/q,ROOT/q,ROOT.parent.parent/q):
   if x.is_file():return x
  return None
 sp=resolve(o.get('script'))
 if sp is None:
  name=str(p)
  for suffix in ('.circuit.json','.native.json','.map.json'):
   if name.endswith(suffix):
    q=Path(name[:-len(suffix)]+'.sing')
    if q.is_file():sp=q
  if sp is None and p.name=='result.json':
   q=p.parent/'augmented.sing'
   if q.is_file():sp=q
 if sp is not None:
  digest=sha(sp)
  r['current_script_artifact']=dict(path=str(sp),bytes=sp.stat().st_size,sha256=digest,matches_reported=digest==o.get('script_sha256') if o.get('script_sha256') else None)
 ip=resolve(o.get('input'))
 if ip is not None:
  digest=sha(ip)
  r['current_input_artifact']=dict(path=str(ip),bytes=ip.stat().st_size,sha256=digest,matches_reported=digest==o.get('input_sha256') if o.get('input_sha256') else None)
 for k in ('stdout','output','log'):
  if k in r['cas']:
   v=r['cas'].pop(k)
   if isinstance(v,str): r['cas'][k+'_embedded_sha256']=hashlib.sha256(v.encode()).hexdigest()
 candidates=[p.with_suffix('.out')]
 if p.name=='result.json': candidates.append(p.parent/'singular.out')
 logs=[]
 for q in candidates:
  if q.is_file(): logs.append(dict(path=str(q.relative_to(ROOT)),bytes=q.stat().st_size,sha256=sha(q)))
 r['output_artifacts']=logs
 r['final_peak_rss_kib']=None
 r['rss_note']='Not invented from address-space limits; measured sidecars and resume resource observations are separately retained.'
 records.append(r)
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),worker='172.30.0.40',record_count=len(records),status_counts=dict(collections.Counter(r['status'] for r in records)),records=records)
print(json.dumps(out,separators=(',',':')))
