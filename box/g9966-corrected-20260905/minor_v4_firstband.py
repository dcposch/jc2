#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json,sys,time
import sympy as sp
ap=argparse.ArgumentParser();ap.add_argument('--code',type=Path,required=True);ap.add_argument('--source',type=Path,required=True);ap.add_argument('--input',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();sys.path.insert(0,str(a.code.resolve()))
import minor_final_verify as M
import minor_flint_quotient_direct as Q
state=json.loads(a.input.read_text());branch=state['branch'];E=M.load_code(a.source,gauge=True);v=M.Verifier(E,branch)
v.extra_generators={sp.Symbol(name) for name in state['initial_complete_free_ring'] if name.startswith('Zface_')};v.locals.update({str(x):x for x in v.extra_generators})
before=v.mapping(state['cumulative_map']);tp=state['last_completed_t']+1;cfg=state['coefficient_quotient'];q=v.expr(cfg['polynomial']);d=v.locals[cfg['d']]
h,c2,c3=[v.apply(poly,before,tp) for poly in [v.h,v.c2,v.c3]];outer={name:v.apply(poly,before,tp) for name,poly in v.outer.items()}
rows,meta=Q.band(h,c2,c3,outer,tp,v.S,q,d)
out={'status':'REGENERATED','branch':branch,'tp':tp,'input_sha256':M.digest(a.input),'map_before':state['cumulative_map'],'rows':{str(k):str(sp.expand(value)) for k,value in rows.items()},'metadata':meta,'driver_sha256_at_start':M.digest(__file__),'core_sha256_at_import':M.VERIFIER_SHA256_AT_IMPORT}
a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'REGENERATED','branch':branch,'tp':tp,'rows':len(rows),'seconds':meta['elapsed_seconds']}))
