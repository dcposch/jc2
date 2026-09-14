from pathlib import Path
from fractions import Fraction as F
import json,re,hashlib
BASE=Path('/home/ubuntu/jc2/box/graded-moh-20260905')
for stem in ['C_n18m12_M2_9_ell2_s3_V3_8','C_n24m18_Mm15_14_ell1_s3_V1_9']:
 old=json.loads((BASE/'truncation'/(stem+'_N1')/'manifest.json').read_text());D=old['target_bidegree'][1];p=old['target_bidegree'][0];X=2*p;Y=2*D;L=Y+1;builder=Path(old['builder']);fullvs=re.search(r'ring R=0,\((.*?)\),',builder.read_text()).group(1).split(',')[2:]
 def wt(v):
  if v=='c':return(p,D)
  k,b,a=v.split('_');i=1 if k=='h' else int(k[1:]);return(int(b),i*6-int(a))
 fullW={v:wt(v) for v in fullvs};originalvs=[v for v in fullvs if fullW[v][0]<=X and fullW[v][1]<=Y];W={v:fullW[v] for v in originalvs};zero={v for v in W if W[v][0]==0};positive=[v for v in originalvs if W[v][0]>0];is111=p==3;vs=positive+([] if is111 else ['curve_t']);vi={v:i for i,v in enumerate(vs)};nv=len(vs);ass={v:0 if is111 else int(v.startswith('A1_')) for v in zero}
 cw=[W[v][0] if is111 else W[v][1]+L*W[v][0] for v in positive]+([] if is111 else [1]);cut=X if is111 else Y+L*X
 source=Path(old['source_rows']);selected=[];rows=[]
 for line in source.read_text().splitlines()[1:]:
  idx,j,b,a,expr=line.split('|',4);bf=int(b)+1;wf=D-int(a)
  if bf>X or wf>Y:continue
  selected.append(dict(source=int(idx),B=bf,w=wf));poly={}
  for t in re.findall(r'[+-]?[^+-]+',expr.replace(' ','').strip('()')):
   coeff=F(1);mon=[0]*nv
   for fact in t.split('*'):
    if fact.startswith('-') and fact[1:].split('^')[0] in fullW:coeff=-coeff;fact=fact[1:]
    if fact.startswith('+'):fact=fact[1:]
    q=fact.split('^');v=q[0];e=int(q[1]) if len(q)>1 else 1
    if v in zero:
     coeff*=ass[v]**e
     if not is111:mon[-1]+=W[v][1]*e
    elif v in vi:mon[vi[v]]+=e
    elif v in fullW:raise AssertionError(('omitted used variable',v))
    else:coeff*=F(fact)
   if coeff:
    k=tuple(mon);poly[k]=poly.get(k,F(0))+coeff
  rows.append('+'.join(str(c)+'*'+'*'.join(v+(('^'+str(e)) if e>1 else '') for v,e in zip(vs,k) if e) for k,c in sorted(poly.items()) if c).replace('+-','-') or '0')
 out=BASE/'resume-r2/truncation'/(stem+'_N2_specialized');out.mkdir(exist_ok=True)
 s='ring S=0,('+','.join(vs)+'),wp('+','.join(map(str,cw))+');\nideal J='+',\n'.join(rows)+';\noption(redSB);\ndegBound='+str(cut)+';\nprint("INPUT_READY_ROWS="+string(size(J)));\noption(prot);\nideal G=std(J);\noption(noprot);\nattrib(G,"isSB",1);\npoly nf=reduce(c^2,G);\nprint("TRUNCATED_STD_COMPLETE=1");\nprint("N2_NONZERO="+string(nf!=0)+" NF_TERMS="+string(size(nf))+" BASIS_SIZE="+string(size(G)));\n'
 s+=f'write(":w {out}/basis.txt",string(G));\nwrite(":w {out}/normalform.txt",string(nf));\nprint("DONE");quit;\n'
 (out/'input.sing').write_text(s);cust=dict(source_rows=str(source),source_rows_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),builder=str(builder),builder_sha256=hashlib.sha256(builder.read_bytes()).hexdigest(),source_original_variable_order=fullvs,selected_source_variables=originalvs,original_weights=fullW,variables=vs,weights=cw,weight_formula='B' if is111 else 'w+83B',degree_bound=cut,target_bidegree=[X,Y],selected_source_rows=selected,source_row_count=len(selected),coefficient_field='Q',assignments=ass,ring_map='B0 variables map to zero' if is111 else 'B0 A1 variables map to curve_t^w; all other B0 variables map to0; positiveB variables identity',image_rows=rows,input_sha256=hashlib.sha256(s.encode()).hexdigest());(out/'custody.json').write_text(json.dumps(cust,indent=2)+'\n')
 spec=dict(ip='172.30.0.86',worker='i-02aaa996f54d2c004',work=str(out),input=str(out/'input.sing'),command=['/usr/bin/Singular','-q',str(out/'input.sing')],memory_gib=40,timeout_seconds=600);(out/'spec.json').write_text(json.dumps(spec,indent=2)+'\n');print(out,len(rows),len(vs),cut)
