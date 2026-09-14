#!/usr/bin/env python3
from pathlib import Path
import re,json
from graded_audit import OUT,rows,TERM
for stem in ['C_n24m16_Mm12_m2_5_ell1_s4_V1_1_6','C_n18m12_M2_9_ell2_s3_V1_8']:
 a=json.loads((OUT/(stem+'_audit.json')).read_text()); d=OUT/stem
 pivots=[]
 for idx,h,b,ya,expr in rows(Path(a['rows_path'])):
  for term in TERM.findall(expr):
   match=re.fullmatch(r'([+-]?)(?:(\d+)\*)?(A\d+_\d+_\d+)',term)
   if match:
    sign,coeff,v=match.groups(); coeff=int(coeff or 1)*(-1 if sign=='-' else 1)
    if a['bidegrees'][v][0]<0:
     pivots.append((a['positive_weights'][v],idx+1,v,coeff));break
 pivots.sort()
 assert len({v for _,_,v,_ in pivots})==len(pivots)
 s=(d/'homogeneous_ideal.sing').read_text()+'\nideal PHI=maxideal(1);\npoly rel; poly value; int fail=0;\n'
 for wt,idx,v,coeff in pivots:
  s+=f'rel=I[{idx}];\nif(diff(rel,{v})!={coeff}){{print("TRIANGULAR_FAIL pivot={v}");fail=1;}}\nvalue={v}-rel/({coeff});\nI=subst(I,{v},value);\nPHI=subst(PHI,{v},value);\nprint("TRIANGULAR_PIVOT weight={wt} variable={v} value_terms="+string(size(value)));\n'
 s+='I=simplify(I,2);\nwrite(":w triangular_reduced.txt",string(I));\nwrite(":w triangular_map.txt",string(PHI));\nprint("TRIANGULAR_DONE rows="+string(size(I))+" failed="+string(fail));\nquit;\n'
 (d/'triangular.sing').write_text(s)
 (d/'triangular_pivots.json').write_text(json.dumps(pivots,indent=2)+'\n')
 print(stem,len(pivots))
