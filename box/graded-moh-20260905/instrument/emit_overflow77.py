#!/usr/bin/env python3
from pathlib import Path
import json,collections,hashlib
from graded_audit import OUT,sha
stem='C_n24m16_Mm12_m2_5_ell1_s4_V1_1_6';d=OUT/stem
m=json.loads((d/'triangular_N1_custody.json').read_text());vv=m['variables'];w=m['bidegrees'];B=-w['c'][0];D=w['c'][1];pos=[v for v in vv if w[v][0]<0];border=[]
def visit(start,chosen,charge):
 if charge>B:
  if charge-min(-w[v][0] for v in chosen)<=B:
   c=collections.Counter(chosen);border.append('*'.join(v+(f'^{e}' if e>1 else '') for v,e in c.items()))
  return
 for i in range(start,len(pos)):visit(i,chosen+[pos[i]],charge-w[pos[i]][0])
visit(0,[],0)
prefix=(d/'triangular_N1_ideal.sing').read_text();at=prefix.index('option(redSB);')
prefix=prefix[:at]+'ideal overflow='+',\n'.join(border)+';\nattrib(overflow,"isSB",1);\nqring Q=overflow;\n'+prefix[at:]
prefix+='print("OVERFLOW_READY variables='+str(len(vv))+' equations="+string(size(I))+" border='+str(len(border))+'");\noption(prot);\ndegBound='+str(D)+';\nideal G=std(I);\noption(noprot);\npoly nf=reduce(c,G);\nprint("OVERFLOW_TRUNCATION_DONE target=c nf_zero="+string(nf==0)+" basis_size="+string(size(G))+" nf_terms="+string(size(nf)));\nwrite(":w overflow77_normalform.txt",string(nf));\nwrite(":w overflow77_basis.txt",string(G));\nquit;\n'
(d/'overflow77.sing').write_text(prefix)
meta={'type':'EXACT-TARGET-COMPONENT-TRUNCATION','coefficient_field':'Q','variables':vv,'order':'wp('+','.join(str(w[v][1]) for v in vv)+')','target_bidegree':w['c'],'y_degree_bound':D,'overflow_minimal_generators':len(border),'rows':m['row_count'],'script_sha256':sha(d/'overflow77.sing'),'source_custody_sha256':sha(d/'triangular_N1_custody.json'),'proof':'Overflow monomial ideal has no element of xcharge<=2. Thus projection to R/M is injective in c target bidegree. I bihomogeneous; (I+M)_deg(c)=I_deg(c). Weighted Buchberger cutoff39 computes all pairs relevant to deg(c). Test normal form of c only; NEVER saturation or unit modulo overflow, since overflow makes c nilpotent.'}
(d/'overflow77_custody.json').write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps(meta))
