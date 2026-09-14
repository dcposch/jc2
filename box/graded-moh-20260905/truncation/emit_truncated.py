#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import json,sys,hashlib,re
out=Path(sys.argv[1]);m=json.loads((out/'manifest.json').read_text());X,Y=m['target_bidegree']
vs=(out/'fast-residual-variables.txt').read_text().strip().split(',');weights=m['weights'];W=[weights[v][1] for v in vs]
assert len(vs)==len(set(vs))
# Build precisely the minimal monomial generators of the xcharge overflow ideal.
pos=[v for v in vs if weights[v][0]>0];borders=[]
def visit(start,chosen,charge):
 if charge>X:
  if charge-min(weights[v][0] for v in chosen)<=X:
   c=Counter(chosen);borders.append('*'.join(v+(f'^{n}' if n>1 else '') for v,n in c.items()))
  return
 for i in range(start,len(pos)):visit(i,chosen+[pos[i]],charge+weights[pos[i]][0])
visit(0,[],0)
rows=(out/'fast-residual-rows.txt').read_text().strip();target=(out/'fast-target.txt').read_text().strip()
raw='ring R=0,('+','.join(vs)+'),wp('+','.join(map(str,W))+');\n'
raw+='ideal overflow='+',\n'.join(borders)+';\nattrib(overflow,"isSB",1);\nqring Q=overflow;\n'
raw+='ideal J='+rows+';\npoly target='+target+';\n'
raw+='print("INPUT_READY VARS='+str(len(vs))+' ROWS="+string(size(J))+" BORDER='+str(len(borders))+' TARGET_TERMS="+string(size(target)));\n'
raw+='option(redSB);\noption(prot);\ndegBound='+str(Y)+';\nideal G=std(J);\noption(noprot);\n'
raw+='print("TRUNCATED_STD_DONE BASIS="+string(size(G)));\npoly nf=reduce(target,G);\nprint("TARGET_ZERO="+string(nf==0)+" NF_TERMS="+string(size(nf)));\n'
raw+=f'write(":w {out}/truncated-basis.txt",string(G));\nwrite(":w {out}/normalform.txt",string(nf));\n'
raw+='print("DONE");\nquit;\n'
(out/'truncated.sing').write_text(raw)
c=dict(selected_variables=len(vs),residual_rows=rows.count(',')+1,overflow_minimal_generators=len(borders),target_bidegree=[X,Y],ring_order='wp('+','.join(map(str,W))+')',coefficient_field='Q',x_truncation='R/M_{>X}; target component unchanged',y_degree_bound=Y,script_sha256=hashlib.sha256(raw.encode()).hexdigest())
(out/'truncation-manifest.json').write_text(json.dumps(c,indent=2)+'\n');print(json.dumps(c))
