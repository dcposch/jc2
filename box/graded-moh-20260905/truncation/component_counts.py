#!/usr/bin/env python3
from pathlib import Path
import json,re,hashlib,sys
VAR=re.compile(r'([A-Za-z]\w*)(?:\^(\d+))?')
def degree(term,W):
 x=y=0
 for var,pow in VAR.findall(term):
  b,w=W[var];n=int(pow or 1);x+=b*n;y+=w*n
 return x,y
def counts(vs,W,X,Y):
 H=[[0]*(Y+1) for _ in range(X+1)];H[0][0]=1
 for v in vs:
  b,w=W[v]
  for i in range(b,X+1):
   for j in range(w,Y+1): H[i][j]+=H[i-b][j-w]
 return H
for root in sys.argv[1:]:
 out=Path(root);meta=json.loads((out/'manifest.json').read_text());X,Y=meta['target_bidegree'];W=meta['weights']
 report={}
 H=counts(meta['variables'],W,X,Y)
 report['source']={'variables':len(meta['variables']),'component_monomials':H[X][Y],'macaulay_rows':sum(H[X-r['x']][Y-r['y']] for r in meta['selected_rows'])}
 vs=(out/'fast-residual-variables.txt').read_text().strip().split(',');H=counts(vs,W,X,Y)
 rows=(out/'fast-residual-rows.txt').read_text().strip().split(',');degrees=[];term_count=0;bad=[]
 for i,row in enumerate(rows):
  terms=re.split(r'(?=[+-])',row.lstrip('+'));ds=set(degree(t,W) for t in terms if t);term_count+=sum(bool(t) for t in terms)
  if len(ds)!=1:bad.append([i,list(ds)])
  degrees.append(list(ds)[0])
 target=(out/'fast-target.txt').read_text().strip();tds=set(degree(t,W) for t in re.split(r'(?=[+-])',target.lstrip('+')) if t)
 report['residual']={'variables':len(vs),'component_monomials':H[X][Y],'macaulay_rows':sum(H[X-b][Y-w] for b,w in degrees),'equations':len(rows),'term_count':term_count,'row_bidegrees':degrees,'inhomogeneous_rows':bad,'target_bidegrees':list(tds),'target_bidegree_ok':tds=={(X,Y)}}
 report['all_rows_homogeneous']=not bad
 for filename in ['fast-residual-rows.txt','fast-target.txt','fast-substitutions.txt','fast-eliminated-variables.txt','fast-residual-variables.txt']:
  report[filename+'_sha256']=hashlib.sha256((out/filename).read_bytes()).hexdigest()
 (out/'component-counts.json').write_text(json.dumps(report,indent=2)+'\n')
 print(out.name,{k:{a:v for a,v in val.items() if a not in ['row_bidegrees']} for k,val in report.items() if k in ['source','residual']})
