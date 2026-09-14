#!/usr/bin/env python3
"""Root-suggested post-cutoff critical-jet delta, not an independent ideation."""
import ast
import json
from pathlib import Path
import sympy as S
root=Path(__file__).resolve().parent
d=json.loads((root/'source_interface.json').read_text())
X=S.Symbol('X')
jets={k:S.expand(sum(S.sympify(r['coefficient'])*X**r['X'] for r in rows if r['W']==1)) for k,rows in d['source_maps'].items()}
eta,b,d1,d0=S.symbols('K2c_36_0 target_b B2c_70_0 B2c_71_0')
star=eta-b/6-d1/2
Delta=S.expand(d1*jets['h'].subs(X,star)+jets['D'].subs(X,star))
free=S.Symbol('B2c_70_1')
assert S.diff(Delta,free)==1
resnames=set()
for row in d['residual_rows']:
    tree=ast.parse(row['expression'].replace('^','**'),mode='eval')
    resnames.update(n.id for n in ast.walk(tree) if isinstance(n,ast.Name))
assert str(free) not in resnames
assert not any(n.startswith('B2c_') for n in resnames)
# h_X=-1,D_X=d1, so -J(h,D)=D_W+d1*h_W on W=0.
assert S.expand(Delta-(-(-jets['D']-d1*jets['h'])).subs(X,star))==0
result={'origin':'ROOT_SUGGESTED_POST1210_CUTOFF_DELTA','W1_jets':{k:str(v) for k,v in jets.items()},
 'x_star':str(star),'Delta':str(Delta),'Delta_factored':'(B2c_69_1-B2c_70_0*(K2c_9_21+5*K2c_4_25))*x_star+B2c_70_0*K2c_35_1+B2c_70_1',
 'all14residuals_B2_independent':True,'Delta_monic_in':'B2c_70_1',
 'ideal_conclusion':'Delta in ideal(14residuals) iff1 in ideal(14residuals); no source properness asserted',
 'actual_Keller_unit_identity':'Delta*(Zj*F_X(x_star,0))=1 on fullJ+Zj*J0-1',
 'last_C_evaluation_row':'J(C,G)(x_star,0)=beta*Delta',
 'no_new_inverse_variable_introduced':True,'no_extra_pivot_implemented':True}
out=root/'critical_jet.json';assert not out.exists();out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps(result,sort_keys=True))
