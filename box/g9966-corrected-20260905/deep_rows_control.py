#!/usr/bin/env python3
"""Independent exact controls for factored normalized Jacobian and radical roots."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import sympy as sp

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import deep_rows as d

source=HERE/"frozen"/"band_engine.py"
if not source.exists():
    source=Path("/tmp/jc2-lane.qdzvDy/inputs/band_engine.py")
spec=importlib.util.spec_from_file_location("deep_rows_frozen_control",source)
e=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=e
spec.loader.exec_module(e)

x,y,a,b,c,dv,e0,f=sp.symbols("x y a b c dv e0 f")
H={(0,2):sp.Integer(1),(0,3):sp.Integer(1),(1,1):x,(2,0):y}
outer={"A2":{(0,1):a,(1,0):b},"A3":{(1,2):c},
       "B1":{(0,1):dv,(2,0):e0},"B2":{(1,0):f}}
T=5
F,G=e.build_FG(H,outer,T)
fast=d.all_w_bands(d.jacobian_factored(H,outer,T),T)
band_controls=[]
for tp in range(T+1):
    old=e.jacobian_band(F,G,tp)
    keys=set(old)|set(fast[tp])
    assert all(sp.expand(old.get(k,0)-fast[tp].get(k,0))==0 for k in keys)
    band_controls.append({"t_power":tp,"nonzero_rows":len(old),"all_match":True})
local_controls=[]
for branch in ("delta2","delta52"):
    direct=d.local_FG(e,H,outer,branch,T)
    for name,poly,fastlocal in (("F",F,direct[0]),("G",G,direct[1])):
        old=e.local_rows(poly,branch,T)
        keys=set(old)|set(fastlocal)
        assert all(sp.expand(old.get(key,0)-fastlocal.get(key,0))==0 for key in keys)
        local_controls.append({"branch":branch,"polynomial":name,"all_match":True,"rows":len(old)})
zero={name:{} for name in outer}
assert d.jacobian_factored(H,zero,T)=={}
radical,certificates=d.pure_power_radical_rows([
    ("square",3*(x+y)**2),("product",x*y),("cubic",sp.Rational(2,3)*(x-y)**3)])
assert len(radical)==2
assert all(c["source_row"]!="product" for c in certificates)
record={"status":"PASS","field":"Q","frozen_source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
        "factored_vs_frozen_J":band_controls,"factored_vs_frozen_local":local_controls,"pure_power_J_zero":True,
        "radical_root_certificates":certificates,"distinct_factor_product_was_not_restricted":True}
(HERE/"deep_rows_control.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps(record,indent=2))
