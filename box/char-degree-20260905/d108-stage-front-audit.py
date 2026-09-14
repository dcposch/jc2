#!/usr/bin/env python3
import hashlib,json,sys
from pathlib import Path
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'d108'))
import rekill_engine_snapshot as E
R=E.SRC
qvalues=list(range(1,34,4))
M=sp.Matrix([[sp.binomial(q,j) for q in qvalues] for j in range(12)])
assert M.rank()==len(qvalues)==9
rows=[]
for stage in (0,1,8):
 outer,free,meta=E.outer_state(R,stage)
 nonzero=[(r,q,str(v)) for (r,q),v in outer['B2'].items() if 4*r+5*q==277 and v!=0]
 image=outer['B2'].get((33,29),sp.Integer(0))
 if stage>=1: assert image==0 and not nonzero
 else: assert str(image)=='B2c_33_29'
 assert outer['B2'].get((34,28),0)==0
 rows.append({'stage':stage,'D33_q29':str(image),'D34_q28':str(outer['B2'].get((34,28),0)),
 'D34_q29':str(outer['B2'].get((34,29),0)), 'W277_nonzero_count':len(nonzero)})
out={'field':'Q','result':'PASS','engine_sha256':hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest(),
 'B2_source_spec':E.outer_specs(R)['B2'],'W277_q_values':qvalues,'moment_order':12,
 'moment_matrix_rank':M.rank(),'stages':rows,
 'conclusion':'108 D<=33,C<=68 for stages>=1; stage0 keeps D<=32,C<=66'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
