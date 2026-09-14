#!/usr/bin/env python3
import hashlib,json,sys
from pathlib import Path
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'g9966'/'source'))
import engine as E
from source_data import SOURCE as S
qvalues=list(range(1,32,3))
M=sp.Matrix([[sp.binomial(q,j) for q in qvalues] for j in range(13)])
assert M.rank()==len(qvalues)==11
rows=[]
for stage in (0,1,7,8):
 outer,free,meta=E.outer_state(stage)
 nonzero=[(r,q,str(v)) for (r,q),v in outer['B2'].items() if 3*r+4*q==190 and v!=0]
 image=outer['B2'].get((30,25),sp.Integer(0))
 if stage>=1: assert image==0 and not nonzero
 else: assert str(image)=='B2c_30_25'
 assert outer['B2'].get((31,24),0)==0
 rows.append({'stage':stage,'D30_q25':str(image),'D31_q24':str(outer['B2'].get((31,24),0)),
 'D31_q25':str(outer['B2'].get((31,25),0)), 'W190_nonzero_count':len(nonzero)})
out={'field':'Q','result':'PASS','engine_sha256':hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest(),
 'actual_D1_substitution':list(S['D1_substitution']),'B2_source_spec':list(S['outer_specs']['B2']),
 'W190_q_values':qvalues,'moment_order':13,'moment_matrix_rank':M.rank(),'stages':rows,
 'conclusion':'99 D<=30,C<=62 for stages>=1; stage0 keeps quartic D<=29,C<=60'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
