#!/usr/bin/env python3
"""Exact graph extension of source-complete Jacobian coefficient charts.

For each Horner stage insert u_m - coeff_m(previous*h + a_i)=0.
The new u_m occur monically, in a triangular order. Thus quotienting by
these defining equations identifies the extended ring with the original
parameter ring. The final Jacobian coefficient ideal contracts to exactly
the original full chart; adjoining z*c-1 commutes with this identification.
"""
from pathlib import Path
from collections import defaultdict, Counter
from fractions import Fraction
import json,re,hashlib,subprocess,time
BASE=Path('/home/ubuntu/jc2/box/moh14-charts-20260905/hsupport-gate-20260905/source-complete')
ONE={():1}
def addto(target,expr,scale=1):
 for term,c in expr.items():
  z=target.get(term,0)+c*scale
  if z:target[term]=z
  elif term in target:del target[term]
def mul(a,b):
 out={}
 for u,c in a.items():
  for v,d in b.items():
   term=tuple(sorted(u+v));out[term]=out.get(term,0)+c*d
 return {t:c for t,c in out.items()if c}
def text(expr):
 out=[]
 for term,c in sorted(expr.items()):
  if not c:continue
  body='*'.join(v if n==1 else f'{v}^{n}' for v,n in sorted(Counter(term).items())) or '1'
  coeff='' if abs(c)==1 and term else str(abs(c))+'*' if term else str(abs(c))
  body=(coeff+body if term else coeff)
  out.append(('-' if c<0 else '+' if out else '')+body)
 return ''.join(out) or '0'
def value(expr,point):
 out=Fraction(0)
 for term,c in expr.items():
  p=Fraction(c)
  for v in term:p*=point[v]
  out+=p
 return out
def parse_poly(expr):
 out={}
 for term in expr.split(' + '):
  coord=[0,0];coef=ONE
  for token in term.split('*'):
   m=re.fullmatch(r'([xy])(?:\^(\d+))?',token)
   if m:coord[0 if m[1]=='x'else 1]+=int(m[2] or 1)
   elif token=='1':pass
   elif re.fullmatch(r'[A-Za-z_][A-Za-z_0-9]*',token):coef=mul(coef,{(token,):1})
   else:raise ValueError(('bad primitive factor',token))
  out[tuple(coord)]=coef
 return out
def conv(a,b):
 out={}
 for (x,y),f in a.items():
  for (z,w),g in b.items():
   c=(x+z,y+w)
   if c not in out:out[c]={}
   addto(out[c],mul(f,g))
 return {c:e for c,e in out.items()if e}
def fraction_literal(v):return str(v.numerator) if v.denominator==1 else f'({v.numerator}/{v.denominator})'
def emit(job):
 started=time.time();stem=job['stem'];cls=stem.rsplit('_V',1)[0];src=BASE/'classes'/cls
 native=src/'builders'/(stem+'_builder.sing');raw=native.read_text();original=json.loads((src/'meta'/(stem+'.json')).read_text())
 definitions=dict(re.findall(r'^poly (h|AA\d+|BB\d+) = (.*?);$',raw,re.M))
 poly={name:parse_poly(expr)for name,expr in definitions.items()};h=poly['h'];q=original['meta']['closed_form']['q'];e=original['meta']['closed_form']['e'];ell=original['meta']['row']['k']
 variables=list(original['variables']);gens=[];definitions_seq=[];maps={}
 for family,n,prefix in [('P',e,'AA'),('Q',q,'BB')]:
  current={(0,0):ONE}
  for k in range(1,n+1):
   expanded=conv(current,h)
   for coord,f in poly.get(prefix+str(k),{}).items():
    if coord not in expanded:expanded[coord]={}
    addto(expanded[coord],f)
   nextmap={}
   for (x,y),f in sorted(expanded.items()):
    # Existing constants or a single original parameter need no new symbol.
    if len(f)==1 and next(iter(f.values()))==1 and len(next(iter(f)))<=1:
     nextmap[(x,y)]=f;continue
    u=f'aux{family}{k}_{x}_{y}';variables.append(u);definition={(u,):1};addto(definition,f,-1)
    gens.append((0,x,y,definition));definitions_seq.append((u,f));nextmap[(x,y)]={(u,):1}
   current=nextmap
  maps[family]=current
 jac={}
 for (x,y),a in maps['Q'].items():
  for (z,w),b in maps['P'].items():
   factor=x*w-y*z
   if not factor:continue
   coord=(x+z-1,y+w-1)
   assert min(coord)>=0
   if coord not in jac:jac[coord]={}
   addto(jac[coord],mul(a,b),factor)
 if (ell,0) not in jac:jac[(ell,0)]={}
 addto(jac[(ell,0)],{('c',):1},-1)
 jac={c:f for c,f in jac.items()if f};definition_count=len(gens)
 for (x,y),f in sorted(jac.items()):gens.append((1,x,y,f))
 dest=BASE/'circuit'/cls; (dest/'rows').mkdir(parents=True,exist_ok=True);(dest/'meta').mkdir(exist_ok=True);(dest/'controls').mkdir(exist_ok=True)
 rows=dest/'rows'/(stem+'_circuit_rows.tsv');meta=dest/'meta'/(stem+'_circuit.json')
 with rows.open('w')as fh:
  fh.write('source_index|h_power|x_power|y_power|expr\n')
  for i,(part,x,y,g)in enumerate(gens):fh.write(f'{i}|{part}|{x}|{y}|{text(g)}\n')
 payload=dict(original);payload.update(variables=variables,parameter_count=len(variables),rows_path=str(rows),intrinsic_parameter_count=original['parameter_count'],auxiliary_count=len(definitions_seq),representation='monic_triangular_Horner_graph_extension',defining_equations=definition_count,jacobian_equations=len(jac),builder=str(native),circuit_emitter=str(Path(__file__).resolve()))
 meta.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
 controls=[]
 for seed in (1,7):
  point={v:Fraction(((i+seed)*17)%13-6,1+((i+seed)*7)%3)for i,v in enumerate(original['variables'])}
  # Avoid c=0 in the localization control.
  point['c']=Fraction(seed+1,seed+2)
  for u,f in definitions_seq:point[u]=value(f,point)
  assert all(value(g,point)==0 for _,_,_,g in gens[:definition_count])
  defsub=lambda s:re.sub(r'\b[A-Za-z_][A-Za-z0-9_]*\b',lambda m:fraction_literal(point[m.group()])if m.group()in point else m.group(),s)
  ctrl='ring R=0,(y,x),lp;\n'+'\n'.join('poly '+name+' = '+defsub(expr)+';'for name,expr in definitions.items())+'\n'
  qexpr=f'h^{q}'+''.join(f'+BB{i}*h^{q-i}'for i in range(2,q+1)if 'BB'+str(i)in poly)
  pexpr=f'h^{e}'+''.join(f'+AA{i}*h^{e-i}'for i in range(1,e+1)if 'AA'+str(i)in poly)
  ctrl+=f'poly Q={qexpr};\npoly P={pexpr};\npoly J=diff(Q,x)*diff(P,y)-diff(Q,y)*diff(P,x)-{fraction_literal(point["c"])}*x^{ell};\n'
  expected=[]
  for (x,y),expr in sorted(jac.items()):
   v=value(expr,point)
   if v:expected.append(f'({fraction_literal(v)})*x^{x}*y^{y}')
  ctrl+='poly CIRCUIT='+'+'.join(expected)+';\nif(J==CIRCUIT){print("CIRCUIT_CONTROL independent_differential_identity=1");}else{print("CIRCUIT_CONTROL independent_differential_identity=0");}\nif(J!=CIRCUIT+1){print("CIRCUIT_CONTROL negative=1");}else{print("CIRCUIT_CONTROL negative=0");}\nquit;\n'
  cpath=dest/'controls'/(stem+f'_seed{seed}.sing');cpath.write_text(ctrl)
  proc=subprocess.run(['Singular','--cpus=1','--threads=1','--flint-threads=1','-q','--no-rc',str(cpath)],capture_output=True,text=True,timeout=60)
  log=cpath.with_suffix('.log');log.write_text(proc.stdout+proc.stderr)
  ok=proc.returncode==0 and 'independent_differential_identity=1'in proc.stdout and 'negative=1'in proc.stdout and not re.search(r'CIRCUIT_CONTROL \w+=0|\?',proc.stdout)
  assert ok,(stem,seed,proc.stdout)
  controls.append(dict(seed=seed,passed=ok,recurrence_equations_vanish=True,log=str(log)))
 return dict(stem=stem,host=job['host'],intrinsic_unknowns=original['parameter_count'],auxiliary_unknowns=len(definitions_seq),extended_unknowns=len(variables),defining_equations=definition_count,jacobian_equations=len(jac),total_equations=len(gens),rows=str(rows),rows_bytes=rows.stat().st_size,rows_sha256=hashlib.sha256(rows.read_bytes()).hexdigest(),meta=str(meta),builder=str(native),builder_sha256=hashlib.sha256(raw.encode()).hexdigest(),controls=controls,elapsed_seconds=round(time.time()-started,3))
if __name__=='__main__':
 jobs=json.loads((BASE/'ops/launched-native.json').read_text());results=[]
 for job in jobs:
  result=emit(job);results.append(result);print(json.dumps(result),flush=True);(BASE/'ops/circuit-emission.json').write_text(json.dumps(results,indent=2)+'\n')
