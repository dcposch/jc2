from pathlib import Path
import sys,json
out=Path(sys.argv[1]);N=json.loads((out/'manifest.json').read_text())['power']
rows=(out/'fast-residual-rows.txt').read_text().strip();relations=(out/'fast-substitutions.txt').read_text().strip();ev=(out/'fast-eliminated-variables.txt').read_text().strip();target=(out/'fast-target.txt').read_text().strip()
s=f'''<"{out}/input.sing";
ideal relations={relations};
ideal eliminated={ev};
ideal expected={rows};
poly expectedtarget={target};
ideal J=I;
poly target=c^{N};
poly p,v,q;
int k,i,found,ok=1;
for(k=1;k<=size(eliminated);k++)
{{
 p=relations[k];v=eliminated[k];found=0;
 if(p/v!=1){{ok=0;}}
 for(i=1;i<=size(J);i++)
 {{
  q=J[i]/v;
  if(q!=0 && q==jet(q,0) && J[i]==q*p){{found=1;break;}}
 }}
 if(found==0){{ok=0;break;}}
 J=subst(J,v,v-p);J=simplify(J,2);
 target=subst(target,v,v-p);
}}
print("ALL_RELATIONS_ARE_UNIT_COEFFICIENT_CURRENT_GENERATORS="+string(ok));
print("RESIDUAL_EXACT_MATCH="+string(J==expected));
print("TARGET_EXACT_MATCH="+string(target==expectedtarget));
print("REPLAY_STEPS="+string(size(eliminated)));
quit;
'''
(out/'replay.sing').write_text(s)
