#!/usr/bin/env python3
import json,re,hashlib
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2/box/graded-moh-20260905');TOKEN=re.compile(r'[AB]\d+_\d+_\d+|h_\d+_\d+|\bc\b');TERM=re.compile(r'[+-]?[^+-]+')
for n in (77,136):
 d=ROOT/'resume-r2'/'triangular'/str(n);meta=json.loads((d/'custody.json').read_text());w=meta['weights'];X,D=meta['target_bidegree'];vv=[v for v in meta['variables'] if w[v][0]>0];zs={v for v in meta['variables'] if w[v][0]==0};rows=[];source=Path(meta['source_rows']);used=set();indices=[]
 for line in source.read_text().splitlines()[1:]:
  ix,h,x,y,expr=line.split('|',4)
  if int(x)+1>X:continue
  terms=[t for t in TERM.findall(expr) if not set(TOKEN.findall(t))&zs]
  result=''.join(terms).lstrip('+') or '0';used|=set(TOKEN.findall(result));rows.append(result);indices.append(int(ix))
 vv=[v for v in vv if v in used];order='wp('+','.join(str(w[v][0]) for v in vv)+')';s='ring R=0,('+','.join(vv)+'),'+order+';\nideal I='+',\n'.join(rows)+';\nI=simplify(I,2);\n';s+=f'option(redSB);degBound={X};\nprint("PROJECTION_READY PARAMS={len(vv)} ROWS="+string(size(I)));\nideal G=std(I);poly nf=reduce(c,G);\nprint("PROJECTION_DONE NF_ZERO="+string(nf==0)+" NF_TERMS="+string(size(nf))+" BASIS_SIZE="+string(size(G)));\nwrite(":w {d}/projection-basis.txt",string(G));\nwrite(":w {d}/projection-nf.txt",string(nf));\n'
 s+='int i,j;int checked=0;int failed=0;poly ll,ss;\nfor(i=1;i<=size(G);i++){for(j=1;j<i;j++){ll=leadmonom(G[i])*leadmonom(G[j])/gcd(leadmonom(G[i]),leadmonom(G[j]));if(deg(ll)<='+str(X)+'){ss=(ll/leadmonom(G[i]))*G[i]/leadcoef(G[i])-(ll/leadmonom(G[j]))*G[j]/leadcoef(G[j]);if(reduce(ss,G)!=0){failed++;}checked++;}}}\n'
 s+='int genfails=0;for(i=1;i<=size(I);i++){if(reduce(I[i],G)!=0){genfails++;}}\nprint("BOUNDED_BUCHBERGER_CHECK PAIRS="+string(checked)+" FAILED="+string(failed)+" GENERATORS_FAILED="+string(genfails));\nquit;\n'
 inp=d/'zerocharge_projection_Q.sing';inp.write_text(s);m={'fibre':n,'source_rows':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'coefficient_field':'Q','source_variable_map':{v:('0' if v in zs else v) for v in meta['variables']},'source_generator_indices':indices,'source_generator_order_preserved':True,'receiver_variable_order':vv,'unused_positive_parameters':[v for v in meta['variables'] if w[v][0]>0 and v not in vv],'receiver_weights':{v:w[v][0] for v in vv},'degree_bound':X,'target':'c','map_fixes_c':True,'script_sha256':hashlib.sha256(s.encode()).hexdigest(),'scope':'Only NONMEMBERSHIP can pull back through this specialization: if c not in image(I), c not in I. Zero/UNIT after arbitrary b0=0 specialization cannot kill full chart. All rows of xcharge<=X are included; source rows above X cannot affect homogeneous c target. Source variables above X and unused positive variables remain irrelevant free parameters.'};(d/'projection-custody.json').write_text(json.dumps(m,indent=2)+'\n');print(n,len(vv),len(rows),len(s))
