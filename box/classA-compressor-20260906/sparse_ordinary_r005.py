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

assert json.loads((OUT/'sparse-native.json').read_text())['output_sha256']=='b4a4160ccef95d28490da264704ec8b272110222f8438d62d91ef62a9eccaf78'
RUN=OUT/'sparse-ordinary-run';RUN.mkdir(exist_ok=False)
hpowers={0:one}
for i in range(1,e+q):hpowers[i]=sp.bp_mul(hpowers[i-1],base['h'])
ordinary={}
for level in sorted(levels):
 if levels[level]:sp.bp_addto(ordinary,sp.bp_mul(levels[level],hpowers[level]))
sp.pp_addto(ordinary.setdefault((ell,0),{}),{(nums['c'],):1},-1)
stat('ordinary_expanded',rows=len(ordinary),terms=sp.count_terms(ordinary))
assert sp.count_terms(ordinary)==2902778
# Independent direct derivative identity, exactly in the same sparse Z ring.
pp={};qq={}
for coeff,level in P:sp.bp_addto(pp,sp.bp_mul(coeff,hpowers[level]))
for coeff,level in Q:sp.bp_addto(qq,sp.bp_mul(coeff,hpowers[level]))
control=sp.bp_jac(pp,qq)
sp.pp_addto(control.setdefault((ell,0),{}),{(nums['c'],):1},-1)
assert control==ordinary
stat('independent_direct_derivative_identity_pass',terms=sp.count_terms(control))
del control,pp,qq,hpowers,levels
ring=re.search(r'^ring R=.*;$',program,re.M)[0]
original_compressor=(OUT/'compress.sing').read_text()
loop=original_compressor[original_compressor.index('proc termsum'):]
assert loop.count('proc termsum')==1 and 'COMPRESSION_COMPLETE=1' in loop
loop=loop.replace(str(OUT),str(RUN))
coords=[];terms=0
with (RUN/'ordinary.tsv').open('w',buffering=1<<20) as tf,(RUN/'compress.sing').open('w',buffering=1<<20) as sf:
 tf.write('index|x_power|y_power|expr\n')
 sf.write(ring+'\noption(redSB);\nideal I=\n')
 for (x,y),poly in sorted(ordinary.items()):
  if not poly:continue
  expr=sp.pp_text(poly,names)
  tf.write(f'{len(coords)+1}|{x}|{y}|{expr}\n')
  if coords:sf.write(',\n')
  sf.write(expr);coords.append((x,y));terms+=len(poly)
 sf.write(';\nprint("DIRECT_J_TERMS='+str(terms)+'");\nprint("DIRECT_ORIENTATION=PASS");\n')
 sf.write(loop)
assert terms==2902778
# Reparse physical labels and counts without holding the presentation as text.
physical_rows=physical_terms=0
with (RUN/'ordinary.tsv').open() as f:
 assert next(f).strip()=='index|x_power|y_power|expr'
 for line in f:
  idx,x,y,expr=line.rstrip().split('|',3)
  assert int(idx)==physical_rows+1 and (int(x),int(y))==coords[physical_rows]
  physical_rows+=1;physical_terms+=sum(1 for _ in re.finditer(r'[+-]?[^+-]+',expr))
assert physical_rows==len(coords) and physical_terms==terms
meta=json.loads((OUT/'meta.json').read_text())
meta.update(compression_program_sha256=sha(RUN/'compress.sing'),ordinary_sparse_script_sha256=sha(__file__),ordinary_sparse_extractor_sha256=sha(module),ordinary_rows=physical_rows,ordinary_terms=physical_terms,ordinary_row_stream_sha256=sha(RUN/'ordinary.tsv'),ordinary_coordinate_sha256=hashlib.sha256(''.join(f'{x}|{y}\n' for x,y in coords).encode()).hexdigest(),exact_orientation_check='independent sparse direct derivative equality PASS',parent_compression_program_sha256=sha(OUT/'compress.sing'))
(RUN/'meta.json').write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n')
(RUN/'pinned-builder.sing').write_text(program)
result=dict(schema='classA-sparse-ordinary/v1',status='EXACT_Z_PAIR_LEVELS_AND_DIRECT_DERIVATIVE_EQUAL',row_id='R005',rows=physical_rows,terms=physical_terms,ordinary_stream_bytes=(RUN/'ordinary.tsv').stat().st_size,ordinary_stream_sha256=sha(RUN/'ordinary.tsv'),compression_program_sha256=sha(RUN/'compress.sing'),worker_script_sha256=sha(__file__),wall_seconds=round(time.monotonic()-START,3),peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
(OUT/'sparse-ordinary.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result),flush=True)
