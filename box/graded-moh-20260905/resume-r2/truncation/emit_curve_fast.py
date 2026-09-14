from pathlib import Path
from fractions import Fraction as F
import json,re,hashlib
BASE=Path('/home/ubuntu/jc2/box/graded-moh-20260905');src=BASE/'truncation/C_n24m18_Mm15_14_ell1_s3_V1_9_N1';m=json.loads((src/'manifest.json').read_text());baseout=BASE/'resume-r2/truncation'/src.name/'curve-specialization';cust=json.loads((baseout/'custody.json').read_text());out=baseout.parent/'curve-fast';out.mkdir(exist_ok=True)
vs=cust['variables'];vi={v:i for i,v in enumerate(vs)};W=m['weights'];zero={v for v in W if W[v][0]==0};nv=len(vs);selected={r['source'] for r in m['selected_rows']};inputrows=[]
for line in Path(m['source_rows']).read_text().splitlines()[1:]:
 idx,j,b,a,expr=line.split('|',4)
 if int(idx) not in selected:continue
 terms=[]
 for t in re.findall(r'[+-]?[^+-]+',expr.replace(' ','').strip('()')):
  coeff=F(1);powers={}
  for fact in t.split('*'):
   if fact.startswith('-') and fact[1:] in W:coeff=-coeff;fact=fact[1:]
   if fact.startswith('-') and '^' in fact and fact[1:].split('^')[0] in W:coeff=-coeff;fact=fact[1:]
   if fact.startswith('+'):fact=fact[1:]
   f=fact.split('^');v=f[0];e=int(f[1]) if len(f)>1 else 1
   if v in W:powers[v]=powers.get(v,0)+e
   else:coeff*=F(fact)
  terms.append((coeff,powers))
 inputrows.append(terms)
def image(terms,ass):
 p={}
 for co,po in terms:
  mon=[0]*nv;c=co
  for v,e in po.items():
   if v in zero:c*=ass[v]**e;mon[-1]+=W[v][1]*e
   else:mon[vi[v]]+=e
  if c:
   k=tuple(mon);p[k]=p.get(k,F(0))+c
 return {k:c for k,c in p.items() if c}
def expr(p):
 return '+'.join(str(c)+'*'+'*'.join(v+(('^'+str(e)) if e>1 else '') for v,e in zip(vs,k) if e) for k,c in sorted(p.items())).replace('+-','-') or '0'
s='ring S=0,('+','.join(vs)+'),wp('+','.join(map(str,cust['weights']))+');\nintvec CW='+','.join(map(str,cust['weights']))+';\nint i,j,good;\npoly lc,sp,nf;\nideal J,G;\noption(redSB);\n'
images=[]
for a,ass in enumerate(cust['assignments']):
 rows=[expr(image(r,ass)) for r in inputrows];images.append(rows)
 s+='J='+',\n'.join(rows)+';\n'
 s+=f'degBound={cust["combined_degree_bound"]};\nprint("ASSIGNMENT_START={a}");\nG=std(J);\nattrib(G,"isSB",1);\nnf=reduce(c,G);\n'
 s+='good=1;for(i=1;i<=size(J);i++){if(reduce(J[i],G)!=0){good=0;}}\n'
 s+='for(i=1;i<=size(G);i++){for(j=i+1;j<=size(G);j++){lc=lcm(leadmonom(G[i]),leadmonom(G[j]));if(deg(lc,CW)<='+str(cust['combined_degree_bound'])+'){sp=(lc/leadmonom(G[i]))*G[i]/leadcoef(G[i])-(lc/leadmonom(G[j]))*G[j]/leadcoef(G[j]);if(reduce(sp,G)!=0){good=0;}}}}\n'
 s+=f'print("ASSIGNMENT={a} C_NF_NONZERO="+string(nf!=0)+" NF_TERMS="+string(size(nf))+" INPUT_AND_TRUNCATED_SPAIRS_ZERO="+string(good)+" BASIS_SIZE="+string(size(G)));\n'
 s+=f'write(":w {out}/basis-{a}.txt",string(G));\nwrite(":w {out}/normalform-{a}.txt",string(nf));\n'
s+='print("DONE");quit;\n'
(out/'curve-fast.sing').write_text(s)
spec=dict(ip='172.30.0.86',worker='i-02aaa996f54d2c004',work=str(out),input=str(out/'curve-fast.sing'),command=['/usr/bin/Singular','-q',str(out/'curve-fast.sing')],memory_gib=40,timeout_seconds=900)
(out/'spec.json').write_text(json.dumps(spec,indent=2)+'\n');cust['source_rows_sha256']=hashlib.sha256(Path(m['source_rows']).read_bytes()).hexdigest();cust['input_sha256']=hashlib.sha256(s.encode()).hexdigest();cust['image_rows']=images;cust['emitter_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();(out/'custody.json').write_text(json.dumps(cust,indent=2)+'\n');print(out,len(s),[sum(len(r) for r in rows) for rows in images])
