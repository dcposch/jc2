#!/usr/bin/env python3
"""Materialize a separately imported antecedent's actual source images."""
from pathlib import Path
import argparse,hashlib,json,sys
import sympy as sp
OWN_SHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
ap=argparse.ArgumentParser();ap.add_argument('--code',type=Path,required=True);ap.add_argument('--branch',required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
sys.path.insert(0,str(a.code.resolve()))
import deep_gauge_accelerated as G
import engine as E
from source_data import SOURCE as S,jsonable
assert Path(E.__file__).resolve().parent==a.code.resolve() and E.inner_state is G.gauge_inner
h,c2,c3,inner,meta=E.inner_state(a.branch);outer,outerfree,_=E.outer_state(-1)
images={'h3':h,'C2':c2,'C3':c3,**outer}
payload={'field':'Q','branch':a.branch,'ordered_generators':sorted(map(str,set(inner)|set(outerfree))),
         'source_images':{name:[[r,q,str(sp.expand(value))] for (r,q),value in sorted(poly.items())] for name,poly in images.items()},
         'initial_residue':[[label,str(sp.expand(value))] for label,value in meta['additional_rows']],
         'outer_specs':jsonable(S['outer_specs']),'gauge':{'jet0':'0'}}
out={'payload':payload,'payload_sha256':hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
     'helper_sha256_at_start':OWN_SHA256,
     'engine_sha256':hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest(),
     'gauge_wrapper_sha256':hashlib.sha256(Path(G.__file__).read_bytes()).hexdigest()}
a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
