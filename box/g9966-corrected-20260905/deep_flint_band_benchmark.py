#!/usr/bin/env python3
"""Compare all-prefix and terminal-convolution native engines at one exact locus."""
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path
import sympy as sp
sys.dont_write_bytecode=True
p=argparse.ArgumentParser();p.add_argument('--code',type=Path,required=True);p.add_argument('--checkpoint',type=Path,required=True);p.add_argument('--full',type=Path,required=True);p.add_argument('--band',type=Path,required=True);p.add_argument('--t',type=int,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
sys.path.insert(0,str(a.code.resolve()));import deep_gauge_accelerated as G;import engine as E;import deep_rows as R
from source_data import SOURCE as S
q=json.loads(a.checkpoint.read_text());mapping={sp.Symbol(v):sp.sympify(x) for v,x in q['map_after'].items()};branch=q['branch']
h,c2,c3,free,_=E.inner_state(branch);outer,_,_=E.outer_state(-1)
def current(poly):
 return {(r,k):v for r,band in R.all_w_bands(poly,a.t).items() for k,expression in band.items() if r<=a.t and (v:=E.substitute_map(expression,mapping))!=0}
h,c2,c3=map(current,(h,c2,c3));outer={name:current(poly) for name,poly in outer.items()}
results=[];outputs=[]
for path in [a.full,a.band]:
 spec=importlib.util.spec_from_file_location(path.stem,path);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
 t=time.monotonic();band,meta=mod.jacobian_band(h,c2,c3,outer,a.t,S,progress=lambda m:print(m,flush=True));elapsed=time.monotonic()-t
 results.append({'helper':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'elapsed':elapsed,'metadata':meta});outputs.append(band)
assert all(sp.expand(outputs[0].get(k,0)-outputs[1].get(k,0))==0 for k in set(outputs[0])|set(outputs[1]))
result={'status':'PASS','exact_current_locus_band_images_equal':True,'branch':branch,'t':a.t,'checkpoint_sha256':hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),'benchmarks':results,'speedup':results[0]['elapsed']/results[1]['elapsed']}
a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps(result,indent=2),flush=True)
