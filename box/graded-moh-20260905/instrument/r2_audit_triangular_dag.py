#!/usr/bin/env python3
"""Verify constant-unit triangular elimination as a rational straight-line map.
No expression expansion is needed for the quotient isomorphism. Every source
identity, source index and variable dependency is checked term by term over Q.
"""
import json,re,hashlib,collections
from fractions import Fraction
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2/box/graded-moh-20260905');TERM=re.compile(r'[+-]?[^+-]+');FAC=re.compile(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def parse(expr):
 result=[]
 for raw in TERM.findall(expr):
  sign=-1 if raw.startswith('-') else 1;coef=Fraction(sign);mon={}
  for fac in raw.lstrip('+-').split('*'):
   m=FAC.fullmatch(fac)
   if m:
    v,p=m.groups();assert v not in mon;mon[v]=int(p or 1)
   else:coef*=Fraction(fac)
  result.append((coef,mon))
 return result

def check_pivot(terms,v,coef,ordered,index):
 containing=[(q,m) for q,m in terms if v in m]
 assert containing==[(Fraction(coef),{v:1})],(v,'pivot is not a constant unit coefficient')
 dependencies=set().union(*(set(m) for q,m in terms))&set(ordered)-{v}
 assert all(ordered[z]<index for z in dependencies),(v,'future-pivot dependency')
 return sorted(dependencies,key=ordered.get)

controls={}
check_pivot(parse('3*A1_1_0-2*h_1_0^2'),'A1_1_0',3,{'A1_1_0':0},0);controls['rational_unit_positive']=True
for name,expr,ordered in [('nonlinear_pivot_rejected','3*A1_1_0+A1_1_0^2',{'A1_1_0':0}),('variable_coefficient_rejected','3*A1_1_0+h_1_0*A1_1_0',{'A1_1_0':0}),('future_dependency_rejected','3*A1_1_0-A2_1_0',{'A1_1_0':0,'A2_1_0':1})]:
 try:check_pivot(parse(expr),'A1_1_0',3,ordered,0)
 except AssertionError:controls[name]=True
 else:raise AssertionError(name)
summary={'controls':controls,'fibres':[]}
for n in (77,136):
 ap=next(p for p in (ROOT/'instrument').glob('*_audit.json') if json.loads(p.read_text()).get('parameter_count')==n);a=json.loads(ap.read_text());stem=ap.name[:-len('_audit.json')];pp=ROOT/'instrument'/stem/'triangular_pivots.json';piv=json.loads(pp.read_text());ordered={p[2]:i for i,p in enumerate(piv)}
 source=Path(a['rows_path']);source=source if source.is_absolute() else ROOT.parent.parent/source
 source_rows=[]
 for line in source.read_text().splitlines()[1:]:
  ix,h,x,y,expr=line.split('|',4);source_rows.append({'source_index':int(ix),'h':int(h),'x':int(x),'y':int(y),'expr':expr})
 W={v:(-x,y) for v,(x,y) in a['bidegrees'].items()};X,D=W['c'];dag=[];hist=collections.Counter();low_rows=[]
 for row in source_rows:
  terms=parse(row['expr']);degree=(row['x']+1,D-row['y']-row['h']*int(json.loads(Path(a['metadata_path']).read_text())['meta']['closed_form']['K']))
  for q,m in terms:
   assert q
   assert tuple(sum(W[v][k]*e for v,e in m.items()) for k in (0,1))==degree
  if degree[1]<D:
   assert all('c' not in mon and mon for _,mon in terms)
   low_rows.append(row['source_index'])
 for j,(wt,idx,v,coef) in enumerate(piv):
  row=source_rows[idx-1];terms=parse(row['expr']);deps=check_pivot(terms,v,coef,ordered,j)
  assert W[v][1]==wt and 'c'!=v
  normalized=[]
  for q,m in terms:
   if m=={v:1}:continue
   normalized.append({'coefficient':str(-q/Fraction(coef)),'monomial':m})
  assert all('c' not in t['monomial'] for t in normalized)
  dag.append({'step':j+1,'source_index':row['source_index'],'source_position':idx,'pivot':v,'coefficient':coef,'bidegree':list(W[v]),'prior_pivot_dependencies':deps,'image_expression_before_recursion':normalized,'source_expression':row['expr']});hist[wt]+=1
 remaining=[v for v in a['variables'] if v not in ordered];selected=[v for v in a['variables'] if W[v][0]<=X];n1p=[p for p in dag if W[p['pivot']][0]<=X];n1remaining=[v for v in selected if v not in {p['pivot'] for p in n1p}]
 B=X;arr=[[0]*(D+1) for _ in range(B+1)];arr[0][0]=1
 for v in n1remaining:
  bx,wy=W[v]
  for b in range(bx,B+1):
   for y in range(wy,D+1):arr[b][y]+=arr[b-bx][y-wy]
 out=ROOT/'resume-r2'/'triangular'/str(n);out.mkdir(parents=True,exist_ok=True)
 data={'fibre':n,'source_rows_path':str(source),'source_rows_sha256':sha(source),'source_pivots_sha256':sha(pp),'source_audit_sha256':sha(ap),'field':'Q','source_variable_order':a['variables'],'pivot_dag':dag,'remaining_free_coordinates':remaining,'pivot_count':len(piv),'weight_histogram':dict(sorted(hist.items())),'pivot_relation_ring':'Q[all declared source parameters]','map':'Recursively map each pivot v to -(1/k)*phi(row-k*v), fixing every nonpivot variable. Each row contains pivot exactly as k*v, k a nonzero rational; all other pivot dependencies precede v. The reverse map sends each remaining variable to its quotient class. These are inverse algebra maps between the pivot quotient and a polynomial ring in remaining variables. Full chart becomes the images of every nonpivot row.','all_constant_unit_and_triangular_checks_pass':True,'low_weight_test':{'threshold':D-1,'row_count':len(low_rows),'source_indices':low_rows,'point':{v:1 if v=='c' else 0 for v in a['variables']},'all_rows_evaluate_to_zero':True,'reason':'Each row of weight<D is c-free and has positive degree. The exact displayed rational point satisfies the entire low-weight subsystem and has c=1.'},'N1':{'target_bidegree':[X,D],'selected_parameter_count':len(selected),'selected_pivot_count':len(n1p),'remaining_parameter_count':len(n1remaining),'remaining_parameters':n1remaining,'ambient_target_component_after_pivot_elimination':arr[X][D],'no_arbitrary_specialization':True,'image_map_preserves_c':True},'scope':'The triangular subsystem itself never forces c=0. This DAG quotient isomorphism is complete even where explicit polynomial expansion timed out. No conclusion about the remaining full chart equations is claimed.'}
 (out/'triangular-dag-custody.json').write_text(json.dumps(data,indent=2)+'\n')
 summary['fibres'].append({k:data[k] for k in ('fibre','pivot_count','weight_histogram','N1')});print(n,len(piv),len(remaining),len(low_rows),len(n1p),len(n1remaining),arr[X][D])
(ROOT/'resume-r2'/'triangular'/'dag-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
