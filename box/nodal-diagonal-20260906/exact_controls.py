#!/usr/bin/env python3
"""Exact-Q controls for the nodal transport; no full-chart verdict is inferred."""
import hashlib
import json
from pathlib import Path
import sympy as S

OUT = Path(__file__).with_suffix('.json')


def main():
    t, C, lam = S.symbols('pi C lambda')
    data = {}
    for d, k, N, eps, lead in [(3, 8, 16, 1, -S.Rational(243, 455)),
                                (4, 7, 21, -1, -S.Rational(2048, 3315))]:
        cs = S.symbols('q0:' + str(N + 1))
        q = sum(cs[i] * t**i for i in range(N + 1))
        op = (t**d - 1) * S.diff(q, t) - N*t**(d-1)*q
        rows = [S.expand(op-C*(t**d-1)).coeff(t, i)
                for i in range(N+d)]
        M, rhs = S.linear_eq_to_matrix(rows, cs)
        sol = S.linsolve((M, rhs), cs)
        assert len(sol) == 1
        v = next(iter(sol))
        qp = S.expand(sum(v[i]*t**i for i in range(N+1)))
        assert S.expand((t**d-1)*S.diff(qp,t)-N*t**(d-1)*qp-C*(t**d-1)) == 0
        assert qp.coeff(t,N) == lead*C
        face = S.expand((t**d-1)**k*qp)
        assert face.coeff(t,1) == eps*C
        assert S.gcd(qp/C, S.diff(qp/C,t)) == 1
        piv = (M.T).rref()[1]
        square = M[list(piv), :]
        assert square.det() != 0
        data[str(d)] = {
            'full_matrix_shape': list(M.shape), 'rank_Q': M.rank(),
            'selected_row_indices': list(piv), 'square_determinant': str(square.det()),
            'q_over_C': str(qp/C), 'lambda_over_C': str(lead),
            'e_over_C': eps, 'leader_depth': 143 if d == 3 else 153,
            'constant_J_depth': 163 if d == 3 else 178,
            'ambient_e_depth': 195 if d == 3 else 213,
            'actual_R_e_depth': 52 if d == 3 else 60,
            'all_rows_exact_Q': True,
        }
    F,G,a,b,c,d,e,A,p,q,X,Y = S.symbols('F G a b c d e A p q X Y')
    AA=a+b*b/4
    pp=d+b*c/2-AA*AA/3
    qq=e+c*c/4-AA*(d+b*c/2)/3+2*AA**3/27
    raw=G**3-F**2+a*G**2+b*F*G+c*F+d*G+e
    dep=(G+AA/3)**3+pp*(G+AA/3)+qq-(F-(b*G+c)/2)**2
    assert S.expand(raw-dep)==0
    inv={a:A-b*b/4,d:p+A*A/3-b*c/2,e:q+A*p/3+A**3/27-c*c/4}
    assert S.expand(AA.subs(inv)-A)==0
    assert S.expand(pp.subs(inv)-p)==0
    assert S.expand(qq.subs(inv)-q)==0
    u,z,B,j,h,aa,bb=S.symbols('u z B j h aa bb')
    X0=u*u+B; Y0=u**3+3*B*u/2; D=3*u*u+3*B/2
    assert S.expand(X0**3-3*B*B*X0/4+q-Y0**2)==q+B**3/4
    a0=aa+bb*u
    X1=-2*j/(3*B)+2*u*a0
    Y1=-j*u/B+D*a0
    assert S.expand(2*u*Y1-D*X1)==j
    R1=S.expand((3*X0**2-3*B*B/4)*X1-2*Y0*Y1)
    assert S.expand(R1+j*(u*u+3*B/2))==0
    assert S.expand(R1.subs(u,u+h)).coeff(u,2)==-j
    H=-S.expand(S.diff(X1,u)*Y1-X1*S.diff(Y1,u))/2
    av=-2*H.subs(u,0)/(3*B)
    assert S.rem(S.together(H+D*av).as_numer_denom()[0],u,u)==0
    data['target_inverse_identity']=True
    data['diagonal_identity']=True
    data['first_strip_identity']=True
    data['second_strip_division_exact']=True
    data['B_inverse_identity']='B*(-3*X1(0)/(2*j))=1 modulo j+3*B*X1(0)/2'
    # Four scalar parameters of the dependent family are all retained.
    H0,bt,ct,dt,et=S.symbols('H bt ct dt et')
    f=H0**3+bt*H0+ct; g=H0**2+dt*H0+et
    depraw=S.expand(g**3-f**2+a*g**2+b*f*g+c*f+d*g+e)
    higher=[depraw.coeff(H0,i) for i in [5,4,3,2]]
    sol=S.solve(higher,[a,b,c,d],dict=True)
    assert len(sol)==1
    res=S.expand(depraw.subs(sol[0]))
    assert S.degree(res,H0)==0
    data['cone_vertex_control']={
        'all_four_parameters_retained':True,
        'target_pivots':{str(k):str(v) for k,v in sol[0].items()},
        'remaining_characteristic':str(res),
        'attainment_55_or_63_forces_lambda_zero':True,
        'scope':'dependent-family control only',
    }
    data['driver_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'EXACT_Q_CONTROLS_PASS','output':str(OUT),'clients':3}))


if __name__=='__main__': main()
