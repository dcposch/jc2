#!/usr/bin/env python3
import sys
sys.dont_write_bytecode=True
import hashlib,importlib.util,json,os,re,resource,time
from collections import defaultdict
from pathlib import Path
ROOT=Path('/home/ubuntu/classA-compressor-20260906')
OUT=ROOT/'R005'
START=time.monotonic()
def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def stat(phase,**kw):
 print(json.dumps(dict(phase=phase,wall_seconds=round(time.monotonic()-START,3),peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**kw)),flush=True)
assert sha(ROOT/'inputs/roster.jsonl')=='cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf'
rows=[json.loads(s) for s in (ROOT/'inputs/roster.jsonl').read_text().splitlines()]
row=next(r for r in rows if r['row_id']=='R005');rc=row['receiver_chart']
source=OUT/'pinned-builder.sing';source_sha=sha(source)
assert source_sha==rc['production_emitter_dry_run']['emitted_program_sha256']=='8353325956564822d62c676bb8776f09bad015be709e966d58fa48767f632bd5'
module=ROOT/'vendor/box/gi-only-20260905/experiments/fast-extract/sparse_hadic_extract.py'
assert sha(module)=='a1c24fc7b7b4732ec3a78efe968763abe9846418bab80fff8e7128a224386516'
s=importlib.util.spec_from_file_location('sp',module);sp=importlib.util.module_from_spec(s);s.loader.exec_module(sp)
program=source.read_text()
m=re.search(r'^ring R=0,\((.*?)\),\(lp\(1\),dp\((\d+)\)\);$',program,re.M)
assert m
allvars=m[1].split(',');assert allvars[:2]==['y','x'] and allvars[-1]=='c'
names=allvars[2:];assert len(names)==rc['unknowns_without_T']==307
assert names==json.loads((OUT/'meta.json').read_text())['variables']
nums={v:i for i,v in enumerate(names)};assert len(nums)==len(names)
setup=dict(re.findall(r'^poly (h|AA\d+|BB\d+) = (.*);$',program,re.M))
base={k:sp.parse_base_polynomial(v,nums) for k,v in setup.items()}
K,e,q,ell=rc['K'],rc['e'],rc['q'],row['own_child']['ell']
assert (K,e,q,ell)==(9,3,2,2) and set(base)=={'h','AA1','AA2','AA3','BB2'}
one={(0,0):{():1}}
P=[(one,e)]+[(base[f'AA{i}'],e-i) for i in range(1,e+1)]
Q=[(one,q)]+[(base[f'BB{i}'],q-i) for i in range(2,q+1)]
levels=defaultdict(dict)
for left,r in P:
 for right,s in Q:
  sp.bp_addto(levels[r+s],sp.bp_jac(left,right))
  if r+s:
   lower={}
   if s:sp.bp_addto(lower,sp.bp_scaled_product(right,sp.bp_jac(left,base['h']),s))
   if r:sp.bp_addto(lower,sp.bp_scaled_product(left,sp.bp_jac(base['h'],right),r))
   sp.bp_addto(levels[r+s-1],lower)
stat('initial',level_terms={str(k):sp.count_terms(v) for k,v in sorted(levels.items())})
output=OUT/'sparse-native.tsv';partial=OUT/'sparse-native.tsv.partial'
assert not output.exists() and not partial.exists()
coords=[];total=0;last=max(levels);level=0
with partial.open('w',buffering=1<<20) as f:
 f.write('source_index|h_power|x_power|y_power|expr\n')
 while level<=last or levels.get(level):
  before=levels.pop(level,{})
  stat('division_begin',level=level,input_terms=sp.count_terms(before))
  quotient,remainder=sp.monic_y_division(before,base['h'],K)
  if quotient:sp.bp_addto(levels[level+1],quotient)
  if level==0:sp.pp_addto(remainder.setdefault((ell,0),{}),{(nums['c'],):1},-1)
  stat('write_begin',level=level,remainder_terms=sp.count_terms(remainder),quotient_terms=sp.count_terms(quotient))
  for (x,y),poly in sorted(remainder.items()):
   if not poly:continue
   f.write(f'{len(coords)}|{level}|{x}|{y}|{sp.pp_text(poly,names)}\n')
   coords.append((level,x,y));total+=len(poly)
  f.flush()
  stat('level_complete',level=level,rows=len(coords),total_terms=total,bytes=f.tell())
  level+=1
coordsha=hashlib.sha256(''.join(f'{h}|{x}|{y}\n' for h,x,y in sorted(coords)).encode('ascii')).hexdigest()
assert len(coords)==rc['coefficient_generators']==484
assert coordsha==rc['coefficient_coordinate_sha256']=='9758dedb763696c99ee72d3cd7345d7dc336637fb65909731811a6e5afe37c89'
assert total==53209262
outsha=sha(partial)
assert outsha=='b4a4160ccef95d28490da264704ec8b272110222f8438d62d91ef62a9eccaf78',outsha
assert partial.stat().st_size==2179919994
os.replace(partial,output)
result=dict(schema='classA-sparse-native/v1',row_id='R005',status='EXACT_Z_LITERAL_FROZEN_BASELINE_MATCH',source_program_sha256=source_sha,sparse_extractor_sha256=sha(module),row_count=len(coords),term_count=total,coefficient_coordinate_sha256=coordsha,output_path=str(output),output_bytes=output.stat().st_size,output_sha256=outsha,wall_seconds=round(time.monotonic()-START,3),peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,worker_script_sha256=sha(__file__))
(OUT/'sparse-native.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result),flush=True)
