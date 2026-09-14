#!/usr/bin/env python3
from pathlib import Path
import sys
out=Path(sys.argv[1]);N=__import__('json').loads((out/'manifest.json').read_text())['power']
s=f'''<"{out}/input.sing";
print("INPUT_READ");
ideal J=I;
ideal relations;
ideal elimvars;
poly target=c^{N};
int i,j,k,besti,bestj,bestsize,step;
poly p,q,linear,v,value;
while(1)
{{
  besti=0;bestj=0;bestsize=2147483647;
  for(i=1;i<=size(J);i++)
  {{
    if(size(J[i])>=bestsize){{i++;continue;}}
    linear=jet(J[i],1)-jet(J[i],0);
    for(j=1;j<=size(linear);j++)
    {{
      v=leadmonom(linear[j]);
      q=J[i]/v;
      if(q!=0 && q==jet(q,0))
      {{
        besti=i;bestsize=size(J[i]);
        for(k=1;k<=nvars(R);k++){{if(var(k)==v){{bestj=k;break;}}}}
        break;
      }}
    }}
  }}
  if(besti==0){{break;}}
  v=var(bestj);p=J[besti]/(J[besti]/v);value=v-p;
  relations[step+1]=p;elimvars[step+1]=v;
  target=subst(target,v,value);
  J=subst(J,v,value);J=simplify(J,2);
  step++;
  print("STEP="+string(step)+" VAR="+string(v)+" ROWS="+string(size(J))+" TARGET_TERMS="+string(size(target)));
}}
ideal vars=maxideal(1);
for(i=1;i<=size(elimvars);i++){{vars=subst(vars,elimvars[i],0);}}
vars=simplify(vars,2);
write(":w {out}/fast-residual-rows.txt",string(J));
write(":w {out}/fast-residual-variables.txt",string(vars));
write(":w {out}/fast-target.txt",string(target));
write(":w {out}/fast-substitutions.txt",string(relations));
write(":w {out}/fast-eliminated-variables.txt",string(elimvars));
print("FAST_DONE ELIMINATED="+string(size(elimvars))+" RESIDUAL_ROWS="+string(size(J))+" TARGET_ZERO="+string(target==0));
quit;
'''
(out/'fast-preprocess.sing').write_text(s)
