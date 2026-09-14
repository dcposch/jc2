#!/usr/bin/env python3
import json,re,collections,hashlib
from pathlib import Path
from fractions import Fraction
R=Path('/home/ubuntu/jc2/box/graded-moh-20260905');d=R/'resume-r2'/'triangular'/'77'/'curve';d.mkdir(exist_ok=True);m=json.loads((d.parent/'custody.json').read_text());W=m['weights'];X,D=m['target_bidegree'];L=D+1;vv=['t']+[v for v in m['variables'] if W[v][0]>0];idx={v:i for i,v in enumerate(vv)};weight=[1]+[W[v][1]+L*W[v][0] for v in vv[1:]];rows=[];source=Path(m['source_rows']);terms=re.compile(r'[+-]?[^+-]+');fac=re.compile(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?');indices=[]
for line in source.read_text().splitlines()[1:]:
 ix,h,x,y,expr=line.split('|',4)
 if int(x)+1>X:continue
 result={}
 for term in terms.findall(expr):
  q=Fraction(-1 if term.startswith('-') else 1);mm=[0]*len(vv)
  for f in term.lstrip('+-').split('*'):
   ma=fac.fullmatch(f)
   if ma:
    v,e=ma.groups();e=int(e or 1)
    if W[v][0]==0:mm[0]+=W[v][1]*e
    else:mm[idx[v]]+=e
   else:q*=Fraction(f)
  mm=tuple(mm);result[mm]=result.get(mm,Fraction(0))+q
 chunks=[]
 for mon,q in result.items():
  if not q:continue
  pol='*'.join(v+(f'^{e}' if e!=1 else '') for v,e in zip(vv,mon) if e)
  chunks.append(('+' if q>=0 else '-')+str(abs(q))+('*'+pol if pol else ''))
 rows.append(''.join(chunks).lstrip('+') or '0');indices.append(int(ix))
order='wp('+','.join(map(str,weight))+')';Y=D+L*X;s='ring R=0,('+','.join(vv)+'),'+order+';\nideal I='+',\n'.join(rows)+';\nI=simplify(I,2);\n';s+=f'option(redSB);degBound={Y};\nprint("CURVE_READY VARS={len(vv)} ROWS="+string(size(I))+" BOUND={Y}");\nideal G=std(I);poly nf=reduce(c,G);\nprint("CURVE_DONE NF_ZERO="+string(nf==0)+" NF_TERMS="+string(size(nf))+" BASIS_SIZE="+string(size(G)));\nwrite(":w {d}/basis.txt",string(G));\nwrite(":w {d}/nf.txt",string(nf));\nquit;\n';inp=d/'input.sing';inp.write_text(s);meta={'fibre':77,'source_rows':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'source_indices':indices,'field':'Q','source_variable_order':m['variables'],'receiver_variable_order':vv,'source_variable_map':{v:(f't^{W[v][1]}' if W[v][0]==0 else v) for v in m['variables']},'receiver_weights':dict(zip(vv,weight)),'receiver_bidegrees':{'t':[0,1],**{v:W[v] for v in vv[1:]}},'combined_weight_multiplier':L,'target_bidegree':[X,D],'combined_target_degree':Y,'source_generator_order_preserved':True,'script_sha256':hashlib.sha256(s.encode()).hexdigest(),'scope':'Only nonmembership pulls back through the monomial-curve specialization fixing c. No UNIT or target-zero may be promoted to source membership. L=D+1 means any xcharge>=X+1 has combined weight greater than target, so no overflow quotient is required.'};(d/'custody.json').write_text(json.dumps(meta,indent=2)+'\n');print(len(vv),len(rows),len(s),Y)
