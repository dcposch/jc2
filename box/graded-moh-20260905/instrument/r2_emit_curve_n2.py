#!/usr/bin/env python3
"""Higher-power necessary images of complete source ideals along weight curves."""
import json,re,hashlib
from pathlib import Path
from fractions import Fraction
ROOT=Path('/home/ubuntu/jc2/box/graded-moh-20260905');TERM=re.compile(r'[+-]?[^+-]+');FAC=re.compile(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?')
for n in (77,136):
 ap=next(p for p in (ROOT/'instrument').glob('*_audit.json') if json.loads(p.read_text()).get('parameter_count')==n);a=json.loads(ap.read_text());W={v:(-x,y) for v,(x,y) in a['bidegrees'].items()};B,D=W['c'];N=2;X=N*B;Y=N*D;L=Y+1;bound=Y+L*X;d=ROOT/'resume-r2'/'triangular'/str(n)/'curve_n2';d.mkdir(exist_ok=True);source=Path(a['rows_path']);source=source if source.is_absolute() else ROOT.parent.parent/source
 selected=[v for v in a['variables'] if W[v][0]<=X];vv=['t']+[v for v in selected if W[v][0]>0];idx={v:i for i,v in enumerate(vv)};weights=[1]+[W[v][1]+L*W[v][0] for v in vv[1:]];rows=[];indices=[]
 for line in source.read_text().splitlines()[1:]:
  ix,h,x,y,expr=line.split('|',4)
  if int(x)+1>X:continue
  result={}
  for term in TERM.findall(expr):
   q=Fraction(-1 if term.startswith('-') else 1);mon=[0]*len(vv)
   for f in term.lstrip('+-').split('*'):
    ma=FAC.fullmatch(f)
    if ma:
     v,e=ma.groups();e=int(e or 1)
     if W[v][0]==0:mon[0]+=W[v][1]*e
     else:mon[idx[v]]+=e
    else:q*=Fraction(f)
   mon=tuple(mon);result[mon]=result.get(mon,Fraction(0))+q
  chunks=[]
  for mon,q in result.items():
   if not q:continue
   pol='*'.join(v+(f'^{e}' if e!=1 else '') for v,e in zip(vv,mon) if e);chunks.append(('+' if q>=0 else '-')+str(abs(q))+('*'+pol if pol else ''))
  rows.append(''.join(chunks).lstrip('+') or '0');indices.append(int(ix))
 order='wp('+','.join(map(str,weights))+')';s='ring R=0,('+','.join(vv)+'),'+order+';\nideal I='+',\n'.join(rows)+';\nI=simplify(I,2);\n';s+=f'option(redSB);option(prot);degBound={bound};\nprint("CURVE_N2_READY VARS={len(vv)} ROWS="+string(size(I))+" BOUND={bound}");\nideal G=std(I);option(noprot);poly nf=reduce(c^2,G);\nprint("CURVE_N2_DONE NF_ZERO="+string(nf==0)+" NF_TERMS="+string(size(nf))+" BASIS_SIZE="+string(size(G)));\nwrite(":w basis.txt",string(G));\nwrite(":w nf.txt",string(nf));\nquit;\n';inp=d/'input.sing';inp.write_text(s)
 meta={'fibre':n,'power':N,'source_rows':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'source_indices':indices,'field':'Q','source_variable_order':a['variables'],'receiver_variable_order':vv,'source_variable_map':{v:(f't^{W[v][1]}' if W[v][0]==0 else v) for v in selected},'omitted_free_parameters':[v for v in a['variables'] if v not in selected],'receiver_weights':dict(zip(vv,weights)),'receiver_bidegrees':{'t':[0,1],**{v:W[v] for v in vv[1:]}},'combined_weight_multiplier':L,'target_bidegree':[X,Y],'combined_target_degree':bound,'source_generator_order_preserved':True,'script_sha256':hashlib.sha256(s.encode()).hexdigest(),'scope':'Only nonmembership pulls back through this monomial-curve specialization fixing c. No UNIT or target-zero may be promoted to source membership. L=N*D+1 means any xcharge>=X+1 has combined weight greater than target, so no overflow quotient is required.'};(d/'custody.json').write_text(json.dumps(meta,indent=2)+'\n')
 work=ROOT/'runs'/f'r2_{n}_curve_n2_Q';work.mkdir(exist_ok=True);spec={'input':str(inp),'work':str(work),'command':['/usr/bin/Singular','--cpus=1','--threads=1','--flint-threads=1','-q','--no-rc',str(inp)],'memory_gib':40,'timeout_seconds':600,'kind':'singular','chart':ap.name[:-len('_audit.json')],'field':0,'order':order,'representation':'r2_necessary_monomial_curve_image_c2','worker':'i-05bbedf0197e8eee3','ip':'172.30.0.67'};(work/'spec.json').write_text(json.dumps(spec,indent=2)+'\n');print(n,len(vv),len(rows),bound)
