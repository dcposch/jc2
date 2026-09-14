#!/usr/bin/env python3
from pathlib import Path
import json
from graded_audit import OUT
for stem in ['C_n24m16_Mm12_m2_5_ell1_s4_V1_1_6']:
 a=json.loads((OUT/(stem+'_audit.json')).read_text());d=OUT/stem;pivots=json.loads((d/'triangular_pivots.json').read_text())
 s=(d/'homogeneous_ideal.sing').read_text()+'\nideal PHI=maxideal(1);\npoly rel; poly value; int fail=0;\nideal LOW=0; ideal G=0; int j;\n'
 weights=sorted({x[0] for x in pivots})
 for wt in weights:
  for _,idx,v,coeff in (p for p in pivots if p[0]==wt):
   s+=f'rel=I[{idx}];\nif(diff(rel,{v})!={coeff}){{print("STAGED_FAIL pivot={v}");fail=1;}}\nvalue={v}-rel/({coeff});\nI=subst(I,{v},value);\nPHI=subst(PHI,{v},value);\nprint("STAGED_PIVOT weight={wt} variable={v} value_terms="+string(size(value)));\n'
  if wt<=12:
   s+=f'LOW=G; for(j=1;j<=size(I);j++){{if(I[j]!=0 && deg(I[j])<={wt}){{LOW=LOW,I[j];}}}}\ndegBound={wt};\nG=std(LOW);\nI=reduce(I,G);\nprint("STAGED_GB degree={wt} basis="+string(size(G)));\n'
 s+='I=simplify(I+G,2);\nwrite(":w staged_triangular_reduced.txt",string(I));\nwrite(":w staged_triangular_map.txt",string(PHI));\nprint("STAGED_DONE rows="+string(size(I))+" failed="+string(fail));\nquit;\n'
 (d/'staged_triangular.sing').write_text(s)
