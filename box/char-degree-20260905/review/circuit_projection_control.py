#!/usr/bin/env python3
"""Independent exact graph elimination versus direct coefficient rows."""
from pathlib import Path
import hashlib,json,re,subprocess
import sympy as s
HERE=Path(__file__).resolve().parent;BASE=HERE.parent/'d108';records=[]
t,z=s.symbols('tt zz');a,b,c,d,e=s.symbols('target_a target_b target_c target_d target_e')
def parse(text):return s.sympify(text.replace('^','**'))
for label,expected in [('positive','1'),('negative','0')]:
 path=BASE/f'circuit-control-{label}-v2.sing';script=path.read_text()
 inp=json.loads((BASE/f'native-remainder-control-{label}.input.json').read_text())
 rows=script.split('ideal I=\n',1)[1].split(';',1)[0].split(',\n')
 graph={};projected=[]
 for row in rows:
  expr=parse(row);match=re.match(r'^\((cx[A-Za-z0-9_]+)-',row)
  if match:
   var=s.Symbol(match.group(1));assert var not in graph
   image=s.expand(expr.subs(graph,simultaneous=True))
   assert s.Poly(image,var).degree()==1 and s.Poly(image,var).coeff_monomial(var)==1
   graph[var]=-image.subs(var,0)
   assert not any(str(v).startswith('cx') for v in graph[var].free_symbols)
  else:
   image=s.expand(expr.subs(graph,simultaneous=True))
   assert not any(str(v).startswith('cx') for v in image.free_symbols)
   if image!=0:projected.append(image)
 h,D,C=map(parse,[inp['h_expr'],inp['D_expr'],inp['C_expr']]);k=inp['k'];depth=6*k-2-inp['target']
 H=h-b*t**k/6;v=D+(a/3+b*b/18)*t**(2*k-1)
 V=C-b*t**k*D/4+(a*b/12+b**3/54-c/2)*t**(3*k-1);U=s.expand(8*V/(3*t))
 aa=a+b*b/4;dd=d+b*c/2;p=dd-aa*aa/3;q=e+c*c/4-aa*dd/3+2*aa**3/27
 raw=s.Poly(s.expand(v*v-U*H),t,z);R=s.S.Zero;direct=list(map(parse,inp['residual_strings']))
 for (r,j),co in raw.terms():
  if j>=k:direct.append(co)
  else:R+=co*t**r*z**j
 Q=(3*R/4+p*t**(4*k-2))*H**2-t*v*U*H/8+t*v*R-9*t*t*U*U/64+p*t**(4*k-1)*v+q*t**(6*k-2)
 Q-=s.Symbol('leader3')*t**depth*parse(inp['face_expr'])*h.subs(t,0)
 direct += [co for (r,j),co in s.Poly(s.expand(Q),t,z).terms() if r<=depth]
 direct += list(map(parse,['Z3*leader3-1','Zc*c-1']))
 canon=lambda seq:sorted(s.srepr(s.expand(v)) for v in seq if s.expand(v)!=0)
 assert canon(projected)==canon(direct),(label,projected,direct)
 run=subprocess.run(['Singular','-q',str(path)],capture_output=True,text=True,timeout=60)
 output=run.stdout+run.stderr;assert run.returncode==0 and not any(line.lstrip().startswith('?') for line in output.splitlines())
 result=output.split('BEGIN_RESULT\n')[1].split('\nEND_RESULT')[0].splitlines()
 controls=output.split('BEGIN_CONTROLS\n')[1].split('\nEND_CONTROLS')[0].splitlines()
 assert result[0]==expected and controls==['0','1']
 (HERE/f'circuit_projection_{label}.out').write_text(output)
 records.append({'case':label,'monic_graphs_eliminated':len(graph),'projected_nonzero_rows':len(projected),
  'same_as_direct_full_coefficient_rows':True,'result':result,'controls':controls,
  'script_sha256':hashlib.sha256(script.encode()).hexdigest(),
  'input_sha256':hashlib.sha256((BASE/f'native-remainder-control-{label}.input.json').read_bytes()).hexdigest(),
  'output_sha256':hashlib.sha256(output.encode()).hexdigest()})
record={'status':'PASS','field':'Q','cases':records,
 'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps(record,indent=2,sort_keys=True))
