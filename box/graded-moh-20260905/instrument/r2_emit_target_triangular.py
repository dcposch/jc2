#!/usr/bin/env python3
"""N1 finite target-only computation; no saturation in xcharge quotient."""
import json,hashlib,collections,re
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2/box/graded-moh-20260905')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for n in (77,136):
 ap=next(p for p in (ROOT/'instrument').glob('*_audit.json') if json.loads(p.read_text()).get('parameter_count')==n)
 a=json.loads(ap.read_text()); stem=ap.name[:-len('_audit.json')]; X=-a['c_weight'][0];D=a['c_weight'][1]
 w={v:(-x,y) for v,(x,y) in a['bidegrees'].items() if -x<=X}; vv=list(w);pos=[v for v in vv if w[v][0]>0];border=[]
 def visit(start,chosen,charge):
  if charge>X:
   if charge-min(w[v][0] for v in chosen)<=X:
    counts=collections.Counter(chosen);border.append('*'.join(v+(f'^{e}' if e>1 else '') for v,e in counts.items()))
   return
  for i in range(start,len(pos)): visit(i,chosen+[pos[i]],charge+w[pos[i]][0])
 visit(0,[],0)
 selected=[];source=Path(a['rows_path']);source=source if source.is_absolute() else Path('/home/ubuntu/jc2')/source
 for line in source.read_text().splitlines()[1:]:
  ix,h,x,y,expr=line.split('|',4)
  if int(x)+1<=X:
   used=set(re.findall(r'[AB]\d+_\d+_\d+|h_\d+_\d+|\bc\b',expr));assert used<=set(vv)
   selected.append((int(ix),int(h),int(x),int(y),expr))
 out=ROOT/'resume-r2'/'triangular'/str(n);out.mkdir(parents=True,exist_ok=True)
 order='wp('+','.join(str(w[v][1]) for v in vv)+')'
 s='ring R=0,('+','.join(vv)+'),'+order+';\nideal overflow='+',\n'.join(border)+';\nattrib(overflow,"isSB",1);\nqring Q=overflow;\nideal I='+',\n'.join(x[-1] for x in selected)+';\n'
 s+=f'print("N1_INPUT_READY PARAMS={len(vv)} ROWS={len(selected)} BORDER={len(border)} X={X} Y={D}");\noption(redSB);option(prot);degBound={D};\nideal G=std(I);\noption(noprot);poly nf=reduce(c,G);\nprint("N1_FINISHED NF_ZERO="+string(nf==0)+" NF_TERMS="+string(size(nf))+" BASIS_SIZE="+string(size(G)));\nwrite(":w basis.txt",string(G));\nwrite(":w normalform.txt",string(nf));\nquit;\n'
 inp=out/'n1_direct_Q.sing';inp.write_text(s)
 manifest={'fibre':n,'source_rows':str(source),'source_sha256':sha(source),'source_audit_sha256':sha(ap),'target':'c','target_bidegree':[X,D],'field':'Q','variables':vv,'omitted_free_parameters':sorted(set(a['variables'])-set(vv)),'variable_map':{v:v for v in vv},'weights':w,'source_generator_order':[r[0] for r in selected],'rows':len(selected),'overflow_minimal_generators':len(border),'order':order,'degree_bound':D,'script_sha256':sha(inp),'custody':'The selected native ordinary rows are precisely xcharge<=X; all relevant c-target generators are retained. Variables omitted have xcharge>X and remain arbitrary. Monomial ideal overflow consists of all monomials of xcharge>X, and its c-bidegree component is zero. Thus I_c=(I+overflow)_c; this computes only c membership, never UNIT or saturation in qring. Global positive wp weights with std and degBound=D process every pair affecting the target. NF zero is a target-membership signal pending explicit rational witness; completed nonzero NF is exact c nonmembership under verified bounded-std controls.'}
 (out/'custody.json').write_text(json.dumps(manifest,indent=2)+'\n')
 work=ROOT/'runs'/f'r2_{n}_direct_n1_Q';work.mkdir(parents=True,exist_ok=True)
 spec={'input':str(inp),'work':str(work),'command':['/usr/bin/Singular','--cpus=1','--threads=1','--flint-threads=1','-q','--no-rc',str(inp)],'memory_gib':64,'timeout_seconds':2400,'kind':'singular','chart':stem,'field':0,'order':order,'representation':'r2_exact_target_component_xcharge_quotient_N1','worker':'i-05bbedf0197e8eee3','ip':'172.30.0.67'}
 (work/'spec.json').write_text(json.dumps(spec,indent=2)+'\n')
 print(n,len(vv),len(selected),len(border),len(s),work/'spec.json')
