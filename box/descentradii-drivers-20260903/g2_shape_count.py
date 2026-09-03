#!/usr/bin/env python3
"""G2/G3 Appendix-II style shape from Phi(delta1') and the V2=1 subdisc split.

G2: (15,10), k=4, M2'=4, V2'=1, d2'=5, u'=4, v'=1, delta1'=5/4, delta2'=-1/2.
Leading form of h (deg_y=5=K'): y (y-x)^4  [1 h-root at 0 = major D1; 4 at x = minor].
Clone of Moh p.208: lower terms of h are a polynomial in y only; beta is a linear
combination of A=(h-const)/y and {1,x,y}.

Count unknowns; if <=30, attempt a Groebner kill of J(f,g)-c x^4 together with
deg_y constraints, saturating at c != 0.
"""
import sympy as sp

x, y = sp.symbols('x y')

def count_and_maybe_solve():
    b0,b1,b2,b3,b4 = sp.symbols('b0:5')
    p, q, r, s = sp.symbols('p q r s')
    d1, d2 = sp.symbols('d1 d2')
    e1, e2, e3, e4 = sp.symbols('e1:5')
    c = sp.symbols('c')
    T = sp.symbols('T')  # Rabinowitsch

    # h = y(y-x)^4 + b4 y^4 + b3 y^3 + b2 y^2 + b1 y + b0
    h_top = sp.expand(y * (y - x)**4)
    h = sp.expand(h_top + b4*y**4 + b3*y**3 + b2*y**2 + b1*y + b0)
    print("h =", h)
    print("deg_y h", sp.degree(h, y), "deg_x h", sp.degree(h, x), "total", sp.total_degree(h))

    A = sp.expand(sp.together((h - b0)/y))  # h = A y + b0
    print("A deg_y", sp.degree(A, y), "deg_x", sp.degree(A, x))
    B = sp.expand(sp.together((A - A.subs(y, 0))/y)) if True else None

    beta = sp.expand(p*A + q*y + r*x + s)
    print("beta deg_y", sp.degree(beta, y), "deg_x", sp.degree(beta, x))

    f = sp.expand(h**2 + 2*beta)
    print("f deg_y", sp.degree(f, y), "total", sp.total_degree(f), "deg_x", sp.degree(f, x))

    # G1, G0 in the (16,12) style
    G1 = sp.expand(d1*A + d2)
    # B from h = y^2 B + (linear in y?); use A = (y-x)^4 + b4 y^3 + ... so
    # a second quotient:
    # h = y^2 * Bpoly + lin*y + b0
    # For simplicity G0 = e1 A + e2 (y-x) + e3 x + e4  (4)
    G0 = sp.expand(e1*A + e2*(y-x) + e3*x + e4)
    g = sp.expand(h**3 + G1*h + G0)
    print("g deg_y", sp.degree(g, y), "total", sp.total_degree(g), "deg_x", sp.degree(g, x))

    unknowns = [b0,b1,b2,b3,b4, p,q,r,s, d1,d2, e1,e2,e3,e4, c]
    print("unknowns", len(unknowns), unknowns)

    J = sp.expand(sp.diff(f, x)*sp.diff(g, y) - sp.diff(f, y)*sp.diff(g, x))
    print("J total_degree", sp.total_degree(J), "deg_x", sp.degree(J, x), "deg_y", sp.degree(J, y))

    # J - c x^4 == 0 as a polynomial in x,y
    R = sp.expand(J - c*x**4)
    PR = sp.Poly(R, x, y)
    eqs = [sp.expand(co) for co in PR.coeffs() if sp.expand(co) != 0]
    print("number of coefficient equations from J = c x^4 :", len(eqs))
    print("sample eqs:", eqs[:8])

    # fail-closed: if too many, don't groebner the 172-unknown problem
    if len(unknowns) > 30:
        print("COUNTING-BOUND: too many unknowns")
        return

    # Try groebner of the J-equations only first (the cheapest test)
    # Saturate at c != 0 via T*c - 1
    print("\n-- Groebner of J-eqs + (T*c-1), lex, on", len(unknowns)+1, "vars --")
    print("  (this is the Jacobian slice only; M2/Lemma 2.1 not yet imposed)")
    gens = eqs + [T*c - 1]
    vars_ = unknowns + [T]
    # degree-reverse-lex is faster; we only care about 1 in ideal
    try:
        Gb = sp.groebner(gens, *vars_, order='grevlex', field=True)
        Gbl = list(Gb)
        print("  basis size", len(Gbl), "  EMPTY?" , Gbl == [1] or (len(Gbl)==1 and Gbl[0]==1))
        if Gbl != [1] and not (len(Gbl)==1 and Gbl[0]==1):
            print("  first gens:", [sp.factor(t)[:200] if False else t for t in Gbl[:8]])
            # Does c appear as a unit? Check if 1 in the ideal by seeing constant
            print("  leading monomials:", [sp.LM(t, order='grevlex') for t in Gbl[:12]])
    except Exception as e:
        print("  groebner exception:", type(e), e)

if __name__ == '__main__':
    count_and_maybe_solve()
