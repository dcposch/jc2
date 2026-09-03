#!/usr/bin/env python3
"""Exact arithmetic for the descended K=16 ray.

This driver deliberately separates three layers:
  * characteristic/Def. 5.1 arithmetic;
  * Newton-face and order-filtration arithmetic;
  * the tiny monomial-Jacobian control, which is not in the ray's 4-tuple.

It does not assert existence of a polynomial pair with the ray data.
"""

from fractions import Fraction as F
from math import gcd
import sympy as sp


def def51(n, M, d, V, s, i):
    """Moh Definition 5.1(3), with one-based dictionaries."""
    num = F(n - M[i])
    den = F(n - M[s] - 1)
    for j in range(i + 1, s + 1):
        num *= V[j] * (n - M[j]) - d[j]
        den *= V[j] * (n - M[j - 1]) - d[j]
    return 1 - num / den


def major_support(delta, index):
    """Monomials gamma^a*pi^b allowed by ord C_i(sigma)>=-i*delta."""
    out = []
    for b in range(4):
        for a in range(32):
            if F(a) <= delta * (b + index) and a + b <= 4 * index:
                out.append((a, b))
    return out


def symbolic_ray():
    """Sympy derivation with t left symbolic (positive integral)."""
    t = sp.symbols("t", integer=True, positive=True)
    n, m, M2 = 12 * t + 4, 8 * t + 4, 12 * t + 1
    d2, d3, V2, kjac = 4, 1, 3, 1
    e, q = sp.cancel(n / d2), sp.cancel(m / d2)

    # Definition 5.1(3), first at i=2 and then at i=1 with M1=-m.
    raw2 = sp.simplify(1 - (n - M2) / (n - M2 - 1))
    raw1 = sp.simplify(
        1 - ((n + m) * (V2 * (n - M2) - d2))
        / ((n - M2 - 1) * (V2 * (n + m) - d2))
    )
    phi2, phi1 = sp.simplify((kjac + 1) * raw2), sp.simplify((kjac + 1) * raw1)
    reciprocal_N = sp.expand(M2 - (n - m))

    # Theorem 1.2: accuracy divided by the approximate-root exponent.
    lambda_P = sp.simplify(3 * e * phi1 + e * phi2)
    lambda_Q = sp.simplify(3 * q * phi1 + q * phi2)
    bounds = (sp.simplify(lambda_P / e), sp.simplify(lambda_Q / q))
    uniform_count = sp.expand((6 * t + 5) + (3 * t + 2) + 4 + 1)

    assert sp.simplify(raw2 + sp.Rational(1, 2)) == 0
    assert sp.simplify(raw1 - t / (2 * (3 * t + 1))) == 0
    assert sp.simplify(phi2 + 1) == 0
    assert sp.simplify(phi1 - t / (3 * t + 1)) == 0
    assert sp.simplify(n - M2 - 1 - 2) == 0
    assert sp.simplify(reciprocal_N - (m - 3)) == 0
    assert sp.simplify(bounds[0] + 1 / e) == 0
    assert sp.simplify(bounds[1] + 1 / e) == 0
    assert sp.simplify((3 * e) / e - 3) == 0
    assert sp.simplify((3 * q - 1) / e - 2) == 0
    assert uniform_count == 9 * t + 12
    return {
        "t": t, "n": n, "m": m, "M2": M2, "e": e, "q": q,
        "raw": (raw2, raw1), "phi": (phi2, phi1),
        "reciprocal_N": reciprocal_N, "lambdas": (lambda_P, lambda_Q),
        "bounds": bounds, "uniform_count": uniform_count,
    }


def ray(t):
    assert isinstance(t, int) and t >= 1
    n, m, M2, V2, kjac = 12 * t + 4, 8 * t + 4, 12 * t + 1, 3, 1
    d2, d3 = gcd(n, m), gcd(gcd(n, m), M2)
    assert (d2, d3) == (4, 1)
    M = {1: -m, 2: M2}
    d = {1: n, 2: d2, 3: d3}
    V = {2: V2, 3: d3}
    raw = (def51(n, M, d, V, 2, 2), def51(n, M, d, V, 2, 1))
    phi = tuple((kjac + 1) * z for z in raw)
    e, q = n // d2, m // d2
    anchor_gap = n - M2 - 1
    reciprocal_N = M2 - (n - m)
    A1 = phi[1].denominator

    assert raw == (F(-1, 2), F(t, 2 * (3 * t + 1)))
    assert phi == (F(-1), F(t, 3 * t + 1))
    assert anchor_gap == 2 and reciprocal_N == m - 3
    assert F(d2, n - M2) < V2 <= F(V[3] * d2, d3)

    cond12 = ((e * V2) % A1 == 0 and (q * V2 - 1) % A1 == 0)
    cond13 = ((q * V2) % A1 == 0 and (e * V2 - 1) % A1 == 0)
    assert A1 == 3 * t + 1 and cond12 and not cond13

    face_P = ((0, n), (e, 3 * e))
    face_Q = ((0, m), (q, 3 * q))
    h_support = major_support(phi[1], 1)
    assert h_support == [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3)]

    alpha_counts = [len(major_support(phi[1], i)) for i in range(1, e + 1)]
    beta_counts = [len(major_support(phi[1], i)) for i in range(2, q + 1)]
    return {
        "t": t, "n": n, "m": m, "M2": M2, "V2": V2,
        "d2": d2, "d3": d3, "e": e, "q": q,
        "raw": raw, "phi": phi, "anchor_gap": anchor_gap,
        "reciprocal_N": reciprocal_N, "A1": A1,
        "cond12": cond12, "cond13": cond13,
        "face_P": face_P, "face_Q": face_Q,
        "h_support": h_support,
        "alpha_counts": alpha_counts, "beta_counts": beta_counts,
    }


def monomial_control():
    gamma, pi = sp.symbols("gamma pi")
    f, g = pi, pi - gamma**2 / 2
    jac = sp.expand(sp.diff(f, gamma) * sp.diff(g, pi)
                    - sp.diff(f, pi) * sp.diff(g, gamma))
    # With g=eta^{-1}, f=eta^{-1}+gamma^2/2.  In the reciprocal parameter
    # f=tilde_eta^{-1}, g=tilde_eta^{-1}-gamma^2/2.  Thus both anchors are
    # at index 0 and have gamma-degree 2=k+1.  Both polynomials are monic
    # of pi-degree 1, but this is not a (12t+4,8t+4) pair.
    anchor_degrees = (sp.degree(gamma**2 / 2, gamma),
                      sp.degree(-gamma**2 / 2, gamma))
    return jac, anchor_degrees, sp.degree(f, pi), sp.degree(g, pi)


def main():
    print("K16 RAY: exact symbolic audit")
    sr = symbolic_ray()
    print("SYMPY SYMBOLIC (t positive integral):")
    print("  (n,m;M2)=(%s,%s;%s); (e,q)=(%s,%s)" %
          (sr["n"], sr["m"], sr["M2"], sr["e"], sr["q"]))
    print("  Def51(raw)=%s; Phi=%s; reciprocal N=%s" %
          (sr["raw"], sr["phi"], sr["reciprocal_N"]))
    print("  Theorem-1.2 accuracies=%s; coefficient bounds=%s" %
          (sr["lambdas"], sr["bounds"]))
    print("  ungauged both-disc necessary-chart upper bound=%s" %
          sr["uniform_count"])
    for t in (1, 2, 3, 10):
        r = ray(t)
        print(
            "t={t}: (n,m;M2,V2)=({n},{m};{M2},{V2}), "
            "d=(4,1), (e,q)=({e},{q})".format(**r)
        )
        print("  Def51(raw)=%s; Phi=%s; anchor gap=%d; reciprocal N=%d" %
              (r["raw"], r["phi"], r["anchor_gap"], r["reciprocal_N"]))
        print("  top-face endpoints P=%s Q=%s" % (r["face_P"], r["face_Q"]))
        print("  A1=%d: (12)=%s, (13)=%s; h support=%s" %
              (r["A1"], r["cond12"], r["cond13"], r["h_support"]))
        if t == 2:
            print("  WEAK major-only counts (not the post-order chart): alpha=%s -> %d; beta=%s -> %d" %
                  (r["alpha_counts"], sum(r["alpha_counts"]),
                   r["beta_counts"], sum(r["beta_counts"])))
            print("  WEAK major-only necessary-superset unknowns = 5+60+32+1 = %d" %
                  (5 + sum(r["alpha_counts"]) + sum(r["beta_counts"]) + 1))

    jac, anchor_degrees, dfpi, dgpi = monomial_control()
    print("negative 4-tuple control: (f,g)=(pi,pi-gamma^2/2)")
    print("  J(f,g)=%s; reciprocal Lemma anchor degrees=%s; pi-degrees=(%s,%s)" %
          (jac, anchor_degrees, dfpi, dgpi))
    print("  Lemma-shape PASS; K16 4-tuple classifier FAIL")
    assert (jac == sp.Symbol("gamma") and anchor_degrees == (2, 2)
            and (dfpi, dgpi) == (1, 1))


if __name__ == "__main__":
    main()
