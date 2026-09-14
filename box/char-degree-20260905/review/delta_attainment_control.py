#!/usr/bin/env python3
"""Exact Q control: full four-constant cone family, not a chart kill."""
import hashlib
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
H = s.Symbol('H')
u, v, r, w = s.symbols('u v r w')
a, b, c, d, e = s.symbols('a b c d e')
L, Z = s.symbols('L Z')
F = H**3 + u*H + v
G = H**2 + r*H + w
Q = s.Poly(s.expand(G**3 - F**2 + a*G**2 + b*F*G + c*F + d*G + e), H)
mapping = {}
pivots = []
for power, variable in [(5, b), (4, a), (3, c), (2, d)]:
    row = s.expand(Q.nth(power).subs(mapping))
    leader = s.diff(row, variable)
    assert leader == 1
    rhs = s.expand(variable-row)
    mapping[variable] = rhs
    pivots.append(dict(H_power=power, variable=str(variable), leader=str(leader),
                       row=str(row), rhs=str(rhs)))
reduced = s.Poly(s.expand(Q.as_expr().subs(mapping)), H)
assert reduced.degree() <= 1
assert all(s.expand(Q.nth(k).subs(mapping)) == 0 for k in range(2, 7))
results = []
for n, m, Hdegree, target, B in [(99, 66, 33, 55, 198),
                                (108, 72, 36, 63, 216)]:
    assert Hdegree < target < 2*Hdegree
    # A monic H gives lc_y(Q(H))=the top H coefficient. Higher terms are
    # removed successively at degrees 5h,4h,3h,2h; all are above target.
    # The remaining H polynomial has y degree at most h, hence leader 0.
    attainment_row = -L
    localizer_row = Z*L-1
    unit_combination = s.expand(Z*attainment_row+localizer_row)
    assert unit_combination == -1
    results.append(dict(n=n, m=m, H_y_degree=Hdegree, characteristic_degree=target,
                        needed_higher_y_degrees=[k*Hdegree for k in range(5,1,-1)],
                        reduced_y_degree_bound=Hdegree,
                        leader_at_target='0', attainment_row=str(attainment_row),
                        localizer_row=str(localizer_row), unit_identity=str(unit_combination),
                        normalized_attainment_t_power=B-target,
                        normalized_J_constant_t_power=n+m-2))

# A negative control against the tempting but invalid assertion that the
# raw y^55 coefficient vanishes before higher-degree rows are imposed.
y=s.Symbol('y')
Hcontrol=y**33+y**22
raw = s.expand((G**3-F**2+a*G**2+b*F*G+c*F+d*G+e)
               .subs({u:0,v:0,r:0,w:0,a:0,b:0,c:0,d:1,e:0,H:Hcontrol}))
raw55=s.expand(raw).coeff(y,55)
assert raw55==2 and s.degree(raw,y)==66

# Degree upper bound does not give total-degree upper bound.
x=s.Symbol('x')
upper_control=y**55+x**100*y
assert s.degree(upper_control,y)==55 and s.total_degree(upper_control)==101

record=dict(coefficient_field='Q',
            ordered_generators=list(map(str,(u,v,r,w,a,b,c,d,e,L,Z))),
            Delta_F=str(F),Delta_G=str(G),target_polynomial=str(Q.as_expr()),
            pivot_rows=pivots,reduced_target=str(reduced.as_expr()),cases=results,
            negative_controls={
                'raw_Delta_y55_can_be_nonzero': {'H':str(Hcontrol),'Q':'H^2',
                                                'y55_coefficient':str(raw55),
                                                'y_degree':66},
                'y_degree_not_total_degree': {'Q':str(upper_control),'y_degree':55,
                                              'total_degree':101}},
            scope='UNIT only after pullback to the complete four-constant Delta family; not a full necessary-chart UNIT',
            self_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(HERE/'delta_attainment_control.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps(record,indent=2,sort_keys=True))
