#!/usr/bin/env python3
"""Materialize the complete gauge source images and declared generator order."""
import argparse,hashlib,json,sys
from pathlib import Path
import sympy as sp
sys.dont_write_bytecode=True
ap=argparse.ArgumentParser();ap.add_argument('--code',type=Path,required=True);ap.add_argument('--branch',required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
args.code=args.code.resolve();sys.path.insert(0,str(args.code))
import deep_gauge_accelerated as G
import engine as E
from source_data import SOURCE as S,jsonable
h,c2,c3,free,meta=E.inner_state(args.branch);outer,ofree,_=E.outer_state(-1)
polys={'h3':h,'C2':c2,'C3':c3,**outer}
images={name:[[r,q,str(sp.expand(value))] for (r,q),value in sorted(poly.items())] for name,poly in polys.items()}
ring=sorted(map(str,set(free)|set(ofree)))
payload={'field':'Q','branch':args.branch,'ordered_generators':ring,'source_images':images,
    'initial_residue':[(label,str(sp.expand(value))) for label,value in meta['additional_rows']],
    'outer_specs':jsonable(S['outer_specs']),'gauge':{'jet0':'0'}}
serialized=json.dumps(payload,sort_keys=True,separators=(',',':'))
result={'payload':payload,'payload_sha256':hashlib.sha256(serialized.encode()).hexdigest(),
    'code_directory':str(args.code),'code_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(args.code.glob('*.py'))},
    'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'MATERIALIZED','branch':args.branch,'source_image_sha256':result['payload_sha256'],'generator_count':len(ring)}),flush=True)
