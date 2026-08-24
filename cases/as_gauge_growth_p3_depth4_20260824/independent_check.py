#!/usr/bin/env python3
"""Independent hostile check of the p=3, n=4 capped-gauge obstruction.

No producer imports.  Sparse x,y polynomials have SymPy coefficient
expressions.  The checker derives target coefficients from generic digit
polynomials on total-degree simplices and separately exhausts the surviving
top coefficients over F_3.
"""

from itertools import product
import random
import sympy as s


def add(*ps):
    out = {}
    for p in ps:
        for m, v in p.items():
            out[m] = s.expand(out.get(m, 0) + v)
    return {m: v for m, v in out.items() if v != 0}


def sc(k, p):
    return {m: s.expand(k*v) for m, v in p.items() if v != 0}


def mul(p, q):
    out = {}
    for (i,j), u in p.items():
        for (k,l), v in q.items():
            m = (i+k,j+l)
            out[m] = s.expand(out.get(m, 0) + u*v)
    return {m: v for m, v in out.items() if v != 0}


def pw(p, n):
    out = {(0,0): s.Integer(1)}
    for _ in range(n):
        out = mul(out, p)
    return out


def dx(p):
    return {(i-1,j): s.expand(i*v) for (i,j),v in p.items() if i}


def dy(p):
    return {(i,j-1): s.expand(j*v) for (i,j),v in p.items() if j}


def generic(name, cap):
    return {(i,j): s.Symbol(f"{name}_{i}_{j}")
            for t in range(cap+1) for i in range(t+1) for j in [t-i]}


def homogeneous(p, degree):
    return {m:v for m,v in p.items() if sum(m)==degree}


def substitute_poly(p, replacements):
    return {m:s.expand(v.subs(replacements)) for m,v in p.items()
            if s.expand(v.subs(replacements)) != 0}


X={(1,0):s.Integer(1)}; Y={(0,1):s.Integer(1)}


def mod_equal(p,q,modulus):
    keys=set(p)|set(q)
    return all(int(s.expand(p.get(m,0)-q.get(m,0)))%modulus==0 for m in keys)


def independent_universal_trials():
    """Compare exact compositions with the claimed digit formulas mod 81."""
    rng=random.Random(381774)
    for _ in range(24):
        def digit():
            return {m:s.Integer(rng.randrange(3)) for m in generic("t",3)}
        a,b,c,d,e,f=(digit() for _ in range(6))
        A=add(X,sc(3,a),sc(9,c),sc(27,e))
        B=add(Y,sc(3,b),sc(9,d),sc(27,f))
        actual_first=add(A,sc(-1,pw(A,3)))
        series=add({(0,0):s.Integer(1)},sc(3,pw(A,2)),sc(9,pw(A,4)),sc(27,pw(A,6)))
        actual_second=mul(B,series)
        claimed_first=add(X,sc(-1,pw(X,3)),sc(3,a),
            sc(9,add(c,sc(-1,mul(pw(X,2),a)))),
            sc(27,add(e,sc(-1,mul(pw(X,2),c)),
                      sc(-1,mul(X,pw(a,2))),sc(-1,pw(a,3)))))
        claimed_second=add(Y,sc(3,add(b,mul(pw(X,2),Y))),
            sc(9,add(d,mul(pw(X,2),b),sc(2,mul(mul(X,a),Y)),mul(pw(X,4),Y))),
            sc(27,add(f,mul(pw(X,2),d),sc(2,mul(mul(X,a),b)),
                       mul(pw(X,4),b),sc(2,mul(mul(X,c),Y)),mul(pw(a,2),Y),
                       mul(mul(pw(X,3),a),Y),mul(pw(X,6),Y))))
        actual_det=add(mul(dx(A),dy(B)),sc(-1,mul(dy(A),dx(B))))
        L1=add(dx(a),dy(b))
        L2=add(dx(c),dy(d),mul(dx(a),dy(b)),sc(-1,mul(dy(a),dx(b))))
        L3=add(dx(e),dy(f),mul(dx(a),dy(d)),sc(-1,mul(dy(a),dx(d))),
               mul(dx(c),dy(b)),sc(-1,mul(dy(c),dx(b))))
        claimed_det=add({(0,0):s.Integer(1)},sc(3,L1),sc(9,L2),sc(27,L3))
        assert mod_equal(actual_first,claimed_first,81)
        assert mod_equal(actual_second,claimed_second,81)
        assert mod_equal(actual_det,claimed_det,81)
    return 24


def check_degree(D):
    # First cap at the p^2 digit forces a <= D-2.
    a = generic("a", D-2)
    c = generic("c", D)

    # p^3 coefficient of A-A^3: e - x^2 c - x a^2 - a^3.
    p3_no_e = add(sc(-1,mul(pw(X,2),c)),
                  sc(-1,mul(X,pw(a,2))), sc(-1,pw(a,3)))

    top = 12 if D==6 else 9
    a_top = homogeneous(a, 4 if D==6 else 3)
    expected_top = sc(-1,pw(a_top,3))
    assert homogeneous(p3_no_e, top) == expected_top

    repl = {v:0 for v in a_top.values()}
    a_reduced = substitute_poly(a,repl)
    p3_reduced = substitute_poly(p3_no_e,repl)
    if D==6:
        a3=homogeneous(a_reduced,3)
        assert homogeneous(p3_reduced,9) == sc(-1,pw(a3,3))
        repl.update({v:0 for v in a3.values()})
    a2=substitute_poly(a,repl)
    assert max(map(sum,a2)) <= 2
    p3_final=add(sc(-1,mul(pw(X,2),c)),
                 sc(-1,mul(X,pw(a2,2))), sc(-1,pw(a2,3)))

    # The p^2 coefficient of the second coordinate above the cap: once
    # a<=2, only x^2 b can occur.  This forces b<=D-2.
    b=generic("b",D)
    d=generic("d",D)
    q2_no_d=add(mul(pw(X,2),b),sc(2,mul(mul(X,a2),Y)),mul(pw(X,4),Y))
    high={m:v for m,v in q2_no_d.items() if sum(m)>D}
    expected={ (i+2,j):v for (i,j),v in b.items() if i+j>D-2 }
    assert high==expected, (D, set(high)^set(expected))
    b_bound={m:v for m,v in b.items() if sum(m)<=D-2}

    # First divergence at x^2 kills b_[x^2 y].  a_[x^3] is absent.
    L1=add(dx(a2),dy(b_bound))
    assert s.expand(L1.get((2,0),0)-b_bound[(2,1)])==0

    # x^7 of the p^3 first-coordinate digit has only -c_[x^5].
    first_x7=s.expand(p3_final.get((7,0),0))
    assert s.expand(first_x7 + c[(5,0)])==0, (D, first_x7)

    # Exact determinant ingredients after setting both forced coefficients.
    forced={b_bound[(2,1)]:0,c[(5,0)]:0}
    L1f=substitute_poly(L1,forced)
    assert L1f.get((4,0),0)==0  # hence no divided L1/3 carry at this row
    bracket=add(mul(dx(a2),dy(b_bound)),sc(-1,mul(dy(a2),dx(b_bound))))
    K=s.expand(s.sympify(bracket.get((4,0),0)).subs(forced))
    U=s.expand(s.sympify(mul(a2,b_bound).get((5,1),0)).subs(forced))
    # This is the key identity over F_3; verify by coefficient divisibility.
    KU=s.expand(K+U)
    assert KU==0 or all(int(z)%3==0 for z in s.Poly(KU).coeffs())

    L2=add(dx(c),dy(d),bracket)
    detrow=s.expand(L2.get((4,0),0).subs(forced))
    assert s.expand(detrow-(5*c[(5,0)]+d[(4,1)]+bracket.get((4,0),0)).subs(forced))==0

    q3=add(mul(pw(X,2),d),sc(2,mul(mul(X,a2),b_bound)),
           mul(pw(X,4),b_bound),sc(2,mul(mul(X,c),Y)),
           mul(pw(a2,2),Y),mul(mul(pw(X,3),a2),Y),mul(pw(X,6),Y))
    qrow=s.expand(q3.get((6,1),0).subs(forced))
    assert s.expand(qrow-(d[(4,1)]+2*U+1))==0

    # Exhaust all four surviving top coefficients and the determinant-forced
    # d coefficient.  qrow must be 1 mod 3 in every case.
    vals=[]
    effective=[]
    a20=a2[(2,0)]; a11=a2[(1,1)]
    b31=b_bound.get((3,1),s.Integer(0)); b40=b_bound.get((4,0),s.Integer(0))
    for av,ayv,bv,bxv in product(range(3),repeat=4):
        ev={a20:av,a11:ayv}
        if b31!=0: ev[b31]=bv
        if b40!=0: ev[b40]=bxv
        effective.append(tuple(sorted((str(symbol), value) for symbol, value in ev.items())))
        kv=int(K.subs(ev))%3
        uv=int(U.subs(ev))%3
        dv=(-kv)%3
        vals.append((dv+2*uv+1)%3)
    assert set(vals)=={1}
    return {
        "D":D,
        "K":str(K),
        "U":str(U),
        "enumerated_four_slot_assignments":len(vals),
        "distinct_effective_assignments":len(set(effective)),
        "q_values":sorted(set(vals)),
    }


if __name__=="__main__":
    print({"universal_exact_mod81_trials":independent_universal_trials()})
    print(check_degree(5))
    print(check_degree(6))
    print("PASS-INDEPENDENT-AS-GROWTH-HOSTILE-CHECK")
