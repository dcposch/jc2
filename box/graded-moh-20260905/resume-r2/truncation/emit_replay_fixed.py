from pathlib import Path
import json,hashlib
BASE=Path('/home/ubuntu/jc2/box/graded-moh-20260905')
for src in sorted((BASE/'truncation').glob('*_N1')):
 out=BASE/'resume-r2/truncation'/src.name/'replay';out.mkdir(parents=True,exist_ok=True)
 parts={n:(src/('fast-'+n+'.txt')).read_text().strip() for n in ['residual-rows','substitutions','eliminated-variables','target']}
 s=(src/'input.sing').read_text()+f'\nideal relations={parts["substitutions"]};\nideal eliminated={parts["eliminated-variables"]};\nideal expected={parts["residual-rows"]};\npoly expectedtarget={parts["target"]};\n'
 s+='''ideal J=I;
poly target=c;
poly p,v,q;
int k,i,found;
int ok=1;
for(k=1;k<=size(eliminated);k++)
{
 p=relations[k];v=eliminated[k];found=0;
 if(p/v!=1){ok=0;}
 for(i=1;i<=size(J);i++)
 {
  q=J[i]/v;
  if(q!=0 && q==jet(q,0) && J[i]==q*p){found=1;break;}
 }
 if(found==0){ok=0;break;}
 J=subst(J,v,v-p);J=simplify(J,2);
 target=subst(target,v,v-p);
 print("REPLAY_STEP="+string(k));
}
int same=1;
if(size(J)!=size(expected)){same=0;}
if(same){for(i=1;i<=size(J);i++){if(J[i]!=expected[i]){same=0;}}}
print("ALL_RELATIONS_ARE_UNIT_COEFFICIENT_CURRENT_GENERATORS="+string(ok));
print("RESIDUAL_EXACT_MATCH="+string(same));
print("TARGET_EXACT_MATCH="+string(target==expectedtarget));
print("REPLAY_STEPS="+string(size(eliminated)));
print("NEGATIVE_TARGET_CONTROL="+string(target!=expectedtarget+1));
print("DONE");quit;
'''
 (out/'replay.sing').write_text(s)
 spec=dict(ip='172.30.0.86',worker='i-02aaa996f54d2c004',work=str(out),input=str(out/'replay.sing'),command=['/usr/bin/Singular','-q',str(out/'replay.sing')],memory_gib=10,timeout_seconds=300)
 (out/'spec.json').write_text(json.dumps(spec,indent=2)+'\n')
 print(out)
