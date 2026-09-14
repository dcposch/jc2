#!/usr/bin/env python3
from pathlib import Path
import json,re,collections,hashlib
from graded_audit import weights,rows,TERM,FACTOR,sha,BASE,OUT
base=Path('box/moh14-charts-20260905/hsupport-gate-20260905/source-complete/circuit')
results=[]
for mp in sorted(BASE.glob('*/meta/*json')):
 if '_union' in mp.name:continue
 m=json.loads(mp.read_text());ww=weights(m);stem=mp.stem
 result={'stem':stem,'intrinsic_parameter_count':len(ww),'intrinsic_bidegrees':ww,'positive_weights':{v:w[1] for v,w in ww.items()},'intrinsic_min_weight':min(w[1] for w in ww.values()),'intrinsic_max_weight':max(w[1] for w in ww.values()),'metadata_sha256':sha(mp),'c_bidegree':ww['c']}
 cp=list(base.glob(f'*/meta/{stem}_circuit.json'))
 if cp:
  cm=json.loads(cp[0].read_text()); K=int(m['meta']['closed_form']['K'])
  for v in cm['variables']:
   if v not in ww:
    match=re.fullmatch(r'aux[PQ](\d+)_(\d+)_(\d+)',v);assert match,v
    i,b,a=map(int,match.groups());ww[v]=(-b,i*K-a)
  assert all(w[1]>0 for w in ww.values())
  rp=Path(cm['rows_path']); nr=nt=0;hist=collections.Counter();cd=cm['defining_equations'];crows=[]
  for idx,h,b,a,expr in rows(rp):
   observed=set();terms=0
   for term in TERM.findall(expr):
    wx=wy=0
    for factor in term.lstrip('+-').split('*'):
     f=FACTOR.fullmatch(factor)
     if f:
      v,e=f.groups();e=int(e or 1);wx+=ww[v][0]*e;wy+=ww[v][1]*e
     else: assert re.fullmatch(r'\d+(?:/\d+)?',factor),factor
    observed.add((wx,wy));terms+=1
   assert len(observed)==1,(stem,idx,observed)
   if idx>=cd:assert observed=={(-b-1,ww['c'][1]-a)},(stem,idx,observed,b,a)
   if re.search(r'\bc\b',expr):crows.append(idx);assert observed=={ww['c']}
   hist[next(iter(observed))[1]]+=1;nr+=1;nt+=terms
  assert nr==cd+cm['jacobian_equations'];assert len(crows)==1
  result.update({'circuit_rows_path':str(rp),'circuit_rows_sha256':sha(rp),'circuit_metadata_sha256':sha(cp[0]),'circuit_variables':len(ww),'circuit_auxiliary_bidegrees':{v:w for v,w in ww.items() if v.startswith('aux')},'all_circuit_monomials_checked':True,'circuit_row_count':nr,'circuit_term_count':nt,'circuit_generator_weight_histogram':dict(sorted(hist.items())),'max_circuit_generator_weight':max(hist)})
 else:result.update({'circuit_rows_path':None,'all_circuit_monomials_checked':False,'native_direct_audit':str(OUT/(stem+'_audit.json'))})
 results.append(result)
 print(stem,result.get('circuit_row_count'),'checked',result.get('circuit_term_count'),flush=True)
(OUT/'all_fibres_grading.json').write_text(json.dumps(results,indent=2)+'\n')
