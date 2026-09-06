#!/usr/bin/env python3
"""Bind completed temporary UX caches to original cases without changing variables."""
import pathlib,json,hashlib
O=pathlib.Path(__file__).resolve().parent;ROOT=O.parents[1]
cs=json.loads((O/'run_cases.json').read_text());ux={c['id']:c for c in json.loads((O/'UX.json').read_text())['cases']}
updated=[]
for c in cs:
 alias='R002' if c['id']=='R003' else c['id'];rp=O/f'UX-cache-{alias}.json'
 if rp.exists():
  d=json.loads(rp.read_text());assert d['status']=='PASS';assert d['UX_generators']==ux[c['id']]['zero_variables'];cp=pathlib.Path(d['cache_path']);assert cp.is_file() and cp.stat().st_size==d['cache_bytes']
  c.update(original_rows_path=c['rows_path'],original_rows_sha256=d['source_actual_sha256'],original_coefficient_rows=d['original_rows'],rows_path=d['cache_path'],rows_sha256=d['cache_sha256'],coefficient_rows=d['cached_rows'],rows_bytes=d['cache_bytes'],ux_cache_receipt=str(rp.relative_to(ROOT)),ux_cache_receipt_sha256=hashlib.sha256(rp.read_bytes()).hexdigest(),ux_cache_alias=alias,ux_cache_requires_coordinate_generators=d['UX_generators'],ux_cache_congruence='I_original+UX = I_cached+UX; cachealoneisnotoriginalideal')
  updated.append(c['id'])
p=O/'ux_cached_cases.json';tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(cs,indent=2)+'\n');tmp.replace(p)
print(json.dumps({'status':'PASS','cached_case_ids':updated,'path':str(p)}))
