#!/usr/bin/env python3
"""Independent exact-Q t=2 reconstruction and quotient controls.

No generated residuals are imported. F3 is entered literally from the
hash-verified frozen report; all CAS work runs in this foreground process.
"""
import json
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
x, c, b, BB, s, u, z = sp.symbols('x c b BB s u z')
ws = sp.symbols('w1:5')

def coeff(f, n):
    return sp.Poly(sp.expand(f), x).coeff_monomial(x**n)

def is_unit(rows, variables):
    gb = sp.groebner(rows, *variables, domain=sp.QQ)
    return list(gb) == [1]

out = []
for d in (-1, 1):
    t, q = 2, 5
    y = sp.Rational(d + t + 1, 2*q)
    om = 3*(2*d-1)/(4*y*y*(4*t+1))
    C = x+c
    W = om*x**q-BB+sum(ws[i-1]*x**i for i in range(1,q))
    alphaC = 3*x**3*C**2/(4*y*y)
    D = 3*b*x*C/(2*y)
    K = x*x*C-y*b
    eta0 = ws[0]
    rhs = (W**2+(BB-2*alphaC+D)*W+alphaC*(alphaC-D)/3
           -BB*(alphaC-D)-b*eta0*K/(2*y)-BB*eta0*x
           +(b*b*alphaC/2-b*b*(BB+W))/x)
    F = sp.expand(2*(x*W-b*b/4)*sp.diff(W,x)-rhs)
    assert coeff(F,2*q) == 0
    pivots = []
    for var, degree in zip(list(reversed(ws))+[BB],range(2*q-1,q-1,-1)):
        row = coeff(F,degree)
        pivot = sp.diff(row,var)
        assert not pivot.free_symbols and pivot != 0
        val = sp.expand(-row.subs(var,0)/pivot)
        F = sp.expand(F.subs(var,val))
        W = sp.expand(W.subs(var,val))
        pivots.append(str(pivot))
        if var == BB:
            B = val
    eta = coeff(W,1)
    assert all(coeff(F,k)==0 for k in [0,1,*range(q,2*q+1)])
    rows = [coeff(F,k) for k in range(2,q)]
    M, N = sp.expand(B.subs(b,0)), sp.diff(B,b)
    rho, sigma = sp.expand(eta.subs(b,0)), sp.diff(eta,b)
    assert not N.has(b) and not sigma.has(b)
    Delta = sp.expand(N-sigma)
    A = sp.expand(rho-M)
    H = sp.expand(N*rho-M*sigma)
    assert sp.expand(B-eta-(b*Delta-A)) == 0
    assert sp.cancel(B.subs(b,A/Delta)-H/Delta) == 0
    assert sp.cancel(eta.subs(b,A/Delta)-H/Delta) == 0
    Frows = [sp.cancel(Delta**sp.degree(E,b)*E.subs(b,A/Delta)) for E in rows]
    assert all(sp.denom(E)==1 for E in Frows)
    target = sp.expand(B*eta)
    aa = sp.symbols('a0:4')
    weights_basis = [c*rows[0],c*c*rows[1],c**3*rows[2],b*rows[2]]
    residual = sp.Poly(target-sum(ai*Ei for ai,Ei in zip(aa,weights_basis)),c,b)
    solution = sp.solve(residual.coeffs(),aa,dict=True)[0]
    # Choose zero for any free coefficient in the linear certificate family.
    cert = [sp.expand(solution.get(ai,ai)).subs({a:0 for a in aa}) for ai in aa]
    assert sp.expand(target-sum(ai*Ei for ai,Ei in zip(cert,weights_basis)))==0
    arows = [cert[0]*c,cert[1]*c*c,cert[2]*c**3+cert[3]*b]
    certsum = sum(ai*Ei for ai,Ei in zip(arows,rows))
    # A displayed exact certificate, independent of the Groebner checks.
    unit_cert = s*s*certsum+(1+s*B)*(1-s*B)+s*s*B*(B-eta)
    assert sp.expand(unit_cert-1)==0
    boundary_cert = s*s*certsum+(1+s*B)*(1-s*B)+s*s*B*b*Delta-s*s*B*A
    assert sp.expand(boundary_cert-1)==0
    full_unit = is_unit(rows+[B-eta,1-s*B],[c,b,s])
    main_unit = is_unit(Frows+[1-u*Delta*H],[c,u])
    boundary_unit = is_unit(rows+[Delta,A,1-s*B],[c,b,s])
    U_unit = is_unit(rows+[1-z*target],[c,b,z])
    cone_nonunit = not is_unit(rows,[c,b])
    unlinked_nonunit = not is_unit([B-eta,1-s*B],[c,b,s])
    assert full_unit and main_unit and boundary_unit and U_unit
    assert cone_nonunit and unlinked_nonunit
    axis_rows = [sp.expand(E.subs(c,0)) for E in rows]
    assert B.subs(c,0)==eta.subs(c,0)==0
    if d == -1:
        assert axis_rows == [0,0,0]
        assert W.subs(c,0) == -sp.Rational(25,4)*x**5+sp.Rational(5,2)*b*x*x
        frozen_cert = (sp.Rational(6,5)*c*rows[0]
                       -sp.Rational(72,1025)*c*c*rows[1]
                       +sp.Rational(171,5125)*c**3*rows[2])
        assert sp.expand(target-frozen_cert)==0
        relaxed_point = {c:1,b:-sp.Rational(13,425),s:sp.Rational(425,69)}
        assert (B-eta).subs(relaxed_point)==(1-s*B).subs(relaxed_point)==0
        assert B.subs(relaxed_point)==sp.Rational(69,425)
        assert any(E.subs(relaxed_point)!=0 for E in rows)
        assert sp.groebner(rows,c,b,domain=sp.QQ) == sp.groebner(
            [59*c**6-275*c**3*b,c**4*b,c**2*b*b],c,b,domain=sp.QQ)
    else:
        assert any(E!=0 for E in axis_rows)
    out.append(dict(d=d,y=str(y),pivots=pivots,W=str(W),B=str(B),eta=str(eta),
                    E=[str(E) for E in rows],Delta=str(Delta),A=str(A),H=str(H),
                    F=[str(E) for E in Frows],certificate_coefficients=[str(a) for a in arows],
                    U_unit=U_unit,X_unit=full_unit,main_unit=main_unit,boundary_unit=boundary_unit,
                    cone_nonunit=cone_nonunit,rows_deleted_nonunit=unlinked_nonunit,
                    cone_gb=[str(E) for E in sp.groebner(rows,c,b,domain=sp.QQ)],
                    axis_rows=[str(E) for E in axis_rows]))
(HERE/'audit_t2.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2),flush=True)
print('AUDIT_T2_ALL_EXACT_ASSERTIONS_PASS',flush=True)
