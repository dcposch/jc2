#!/usr/bin/env python3
"""Independent exact ideal inclusions and no-rational-point D1 audit."""
import hashlib,json,subprocess
from pathlib import Path
import sympy as sp
N=Path(__file__).resolve().parent
src=json.loads((N/'universal_D1_control.json').read_text())
raw=(N/'universal_D1_control.out').read_text()
basis_text=raw.split('BEGIN\n',1)[1].split('\nEND',1)[0].split('\n',1)[1]
vars=sp.symbols('q0 q1 q2 q3 q4 Jnorm ZJnorm');q0,q1,q2,q3,q4,J,Z=vars
X=sp.Symbol('X');ps=sp.symbols('p0:8');mapping={}
p=X**8+sum(v*X**i for i,v in enumerate(ps));q=X**5+sum(v*X**i for i,v in enumerate(vars[:5]))
L=sp.Poly(sp.expand(p*q+3*X*p*sp.diff(q,X)-2*X*sp.diff(p,X)*q-J),X)
for rec in src['rational_pivots']:
 k=rec['power'];v=sp.Symbol(rec['variable']);row=sp.expand(L.nth(k).xreplace(mapping))
 assert row==sp.sympify(rec['row'])
 lead=sp.diff(row,v);assert lead==sp.Rational(rec['leader']) and lead!=0
 rhs=sp.expand(-(row-lead*v)/lead);assert rhs==sp.sympify(rec['rhs'])
 mapping[v]=rhs
I=[sp.expand(L.nth(k).xreplace(mapping)) for k in range(5)]+[J*Z-1]
assert I==list(map(sp.sympify,src['remaining_rows']))
assert all(sp.expand(L.nth(k).xreplace(mapping))==0 for k in range(5,14))
B=[sp.sympify(s.strip().replace('^','**')) for s in basis_text.split(',') if s.strip()]
def enc(value):
    denominator,poly=sp.Poly(value,*vars,domain=sp.QQ).clear_denoms()
    assert denominator.is_Rational and denominator!=0
    return str(poly.as_expr()).replace('**','^')
script='ring R=0,('+','.join(map(str,vars))+'),dp;\n'
script+='ideal I='+','.join(map(enc,I))+';\nideal B='+','.join(map(enc,B))+';\n'
script+='ideal SI=std(I);ideal SB=std(B);\n'
script+='print("BEGIN_VERIFY");print(size(reduce(I,SB)));print(size(reduce(B,SI)));print(dim(SI));print(size(reduce(ideal(1),SI)));print("END_VERIFY");\nquit;\n'
path=Path(__file__).with_suffix('.sing');path.write_text(script)
run=subprocess.run(['Singular','-q',str(path)],text=True,capture_output=True,check=True,timeout=120)
path.with_suffix('.sing.out').write_text(run.stdout+run.stderr)
values=run.stdout.split('BEGIN_VERIFY\n')[1].split('\nEND_VERIFY')[0].splitlines()
assert values==['0','0','1','1'],run.stdout
# Derive, rather than copy, the three graph equations from the verified basis.
graph={}
for v,idx in ((q2,4),(q1,1),(q0,2)):
 row=sp.expand(B[idx].xreplace(graph));leader=sp.diff(row,v)
 assert leader.is_Rational and leader!=0
 graph[v]=sp.expand(-(row-leader*v)/leader)
cert=json.loads((N/'universal_D1_rational-control.json').read_text())
assert {str(v):str(r) for v,r in graph.items()}==cert['coordinate_graph']
D=153664*q3**2-117584*q3*q4**2+22789*q4**4
remainders=[];has_unit_multiple=False
for row in B:
 if row.free_symbols & {J,Z}:continue
 image=sp.expand(row.xreplace(graph))
 if image==0:continue
 quotient,remainder=sp.div(image,D,q3,q4,domain=sp.QQ)
 assert remainder==0
 has_unit_multiple|=quotient.is_Rational and quotient!=0
 remainders.append({'image':str(sp.factor(image)),'quotient_by_D':str(quotient)})
assert has_unit_multiple
R=sp.Symbol('R');poly=153664*R**2-117584*R+22789
disc=sp.discriminant(poly,R);assert disc<0
assert sp.expand(graph[q0].subs(q4,0))==0
# No q4=0 point survives: graph gives q0=0 and coefficient0 gives J=p0*q0.
q4zero=sp.expand(I[0].xreplace(graph).subs(q4,0));assert q4zero==-J
# Exact converse over Q[q3,q4,J,Z] to the reduced graph model.
reduced_J=sp.expand(I[0].xreplace(graph))
model=[q0-graph[q0],q1-graph[q1],q2-graph[q2],D,reduced_J,J*Z-1]
model_script=script.split('ideal B=')[0]+'ideal M='+','.join(map(enc,model))+';\nideal SM=std(M);ideal SI=std(I);\nprint("BEGIN_MODEL");print(size(reduce(I,SM)));print(size(reduce(M,SI)));print("END_MODEL");\nquit;\n'
mp=Path(__file__).with_name('print-audit-universal-d1-model.sing');mp.write_text(model_script)
mr=subprocess.run(['Singular','-q',str(mp)],text=True,capture_output=True,check=True,timeout=120)
mp.with_suffix('.sing.out').write_text(mr.stdout+mr.stderr)
assert mr.stdout.split('BEGIN_MODEL\n')[1].split('\nEND_MODEL')[0].splitlines()==['0','0'],mr.stdout
result={'status':'PASS','field':'Q','generator_order':list(map(str,vars)),
 'original_rows_regenerated':True,'rational_pivots_verified':8,
 'stored_basis_contains_original_ideal':True,'original_ideal_contains_stored_basis':True,
 'graph_model_both_ideal_inclusions':True,'dimension':1,'negative_unit_control_remainder_nonzero':True,
 'coordinate_graph':{str(v):str(r) for v,r in graph.items()},'eliminated_relation':str(D),
 'ratio_polynomial':str(poly),'ratio_discriminant':int(disc),
 'q4_zero_implies_constant_equation_minus_J':True,'no_real_points':True,'no_rational_points':True,
 'nonempty_over_algebraic_closure':True,
 'scope':'Universal D1 face enlargement. No real/rational source-chart points, but NOT a unit or branch death over C.',
 'relation_checks':remainders,
 'custody':{name:hashlib.sha256((N/name).read_bytes()).hexdigest() for name in
 ['universal_D1_control.py','universal_D1_control.json','universal_D1_control.out','universal_D1_rational-control.json','print-audit-universal-d1-verify.py']}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('relation_checks','custody','coordinate_graph')},indent=2))
