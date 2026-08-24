#!/usr/bin/env python3
"""Independent exact certificate for the Hamiltonian-kappa gate.

Sparse bivariate polynomials are dictionaries (i,j) -> Fraction for x^i y^j.
No third-party package and no prior campaign implementation is imported.
"""

from fractions import Fraction as F
from math import comb
import json


def clean(p):
    return {m: F(c) for m, c in p.items() if c}


def mono(i, j, c=1):
    assert i >= 0 and j >= 0
    return {} if not c else {(i, j): F(c)}


def add(*ps):
    out = {}
    for p in ps:
        for m, c in p.items():
            out[m] = out.get(m, F(0)) + c
    return clean(out)


def scale(c, p):
    return clean({m: F(c) * a for m, a in p.items()})


def sub(p, q):
    return add(p, scale(-1, q))


def mul(p, q):
    out = {}
    for (i, j), a in p.items():
        for (k, ell), b in q.items():
            m = (i + k, j + ell)
            out[m] = out.get(m, F(0)) + a * b
    return clean(out)


def deriv(p, axis):
    out = {}
    for (i, j), c in p.items():
        if axis == "x" and i:
            out[(i - 1, j)] = out.get((i - 1, j), F(0)) + i * c
        elif axis == "y" and j:
            out[(i, j - 1)] = out.get((i, j - 1), F(0)) + j * c
    return clean(out)


def power(p, n):
    assert n >= 0
    out = ONE
    for _ in range(n):
        out = mul(out, p)
    return out


def apply_field(a, b, f):
    """Apply a*d/dx+b*d/dy to f."""
    return add(mul(a, deriv(f, "x")), mul(b, deriv(f, "y")))


def divergence(a, b):
    return add(deriv(a, "x"), deriv(b, "y"))


def bracket(p, q):
    """[p,q] = p_x q_y-p_y q_x."""
    return sub(mul(deriv(p, "x"), deriv(q, "y")),
               mul(deriv(p, "y"), deriv(q, "x")))


def x_p(p, q):
    """Hamiltonian X_p(q)=[p,q]."""
    return bracket(p, q)


def delta_n(n, h):
    """X_{P_n}(h) for P_n=x+x^n*y."""
    a = add(ONE, scale(n, mul(power(X, n - 1), Y)))
    b = power(X, n)
    return sub(mul(a, deriv(h, "y")), mul(b, deriv(h, "x")))


def frac_text(c):
    c = F(c)
    return str(c.numerator) if c.denominator == 1 else f"{c.numerator}/{c.denominator}"


def poly_text(p):
    if not p:
        return "0"
    pieces = []
    for (i, j), c in sorted(p.items(), key=lambda z: (sum(z[0]), z[0]), reverse=True):
        pieces.append(f"{frac_text(c)}*x^{i}*y^{j}")
    return " + ".join(pieces)


ONE = mono(0, 0)
X = mono(1, 0)
Y = mono(0, 1)


def coordinate_controls():
    y_plus_x2 = add(Y, power(X, 2))
    two_shear_p = add(X, power(y_plus_x2, 2))
    two_shear_q = y_plus_x2

    henon_p = sub(power(Y, 2), X)
    henon_q = sub(power(henon_p, 2), Y)

    controls = [
        ("x", X, Y),
        ("x_plus_y2", add(X, power(Y, 2)), Y),
        ("two_shear", two_shear_p, two_shear_q),
        ("henon_second_iterate", henon_p, henon_q),
    ]
    result = {}
    for name, p, q in controls:
        j = bracket(p, q)
        # V_Q=Q_y*d_x-Q_x*d_y has V_Q(P)=[P,Q] and divergence zero.
        va = deriv(q, "y")
        vb = scale(-1, deriv(q, "x"))
        vp = apply_field(va, vb, p)
        div = divergence(va, vb)
        assert j == ONE and vp == ONE and div == {}
        result[name] = {
            "jacobian": poly_text(j),
            "V(P)": poly_text(vp),
            "div(V)": poly_text(div),
        }
    return result


def direct_slice_truncation(n, cap):
    """Return h_N=sum c_k*x^(k(n-1))*y^(k+1) and its terminal."""
    h = {}
    coeffs = []
    for k in range(cap + 1):
        c = F((-1) ** k * comb(n + k - 1, k), k + 1)
        # Equivalent closed form: (-1)^k (n)_k/(k+1)!.
        coeffs.append(c)
        h = add(h, mono(k * (n - 1), k + 1, c))
    terminal_c = coeffs[-1] * (n + cap)
    terminal = mono((cap + 1) * (n - 1), cap + 1, terminal_c)
    actual = delta_n(n, h)
    assert actual == add(ONE, terminal)
    return h, coeffs, terminal


def kappa_correction_truncation(n, cap):
    """Solve X_P(h)=div(V_0) along the only relevant weight chain."""
    h = {}
    coeffs = []
    for k in range(cap + 1):
        c = F((-1) ** k * comb(n + k + 1, k + 2))
        coeffs.append(c)
        h = add(h, mono((n - 1) * k + n - 2, k + 2, c))
    target = mono(n - 2, 1, n * (n + 1))
    terminal_c = coeffs[-1] * (cap + n + 2)
    terminal = mono((n - 1) * (cap + 1) + n - 2,
                    cap + 2, terminal_c)
    actual = delta_n(n, h)
    assert actual == add(target, terminal)
    return h, coeffs, target, terminal


def rational_slice_cleared_identity(n):
    """Verify X_P(Q)=1 after clearing the rational denominator.

    Q=y*(1-(1+Z)^(1-n))/((n-1)Z).  To stay in polynomials, write
    Q=N/D with D=(n-1)*Z*(1+Z)^(n-1) and
    N=y*((1+Z)^(n-1)-1), then check
    X_P(N)D-N X_P(D)=D^2.
    """
    z = mul(power(X, n - 1), Y)
    one_plus_z = add(ONE, z)
    numerator = mul(Y, sub(power(one_plus_z, n - 1), ONE))
    denominator = scale(n - 1, mul(z, power(one_plus_z, n - 1)))
    lhs = sub(mul(delta_n(n, numerator), denominator),
              mul(numerator, delta_n(n, denominator)))
    rhs = power(denominator, 2)
    assert lhs == rhs
    return numerator, denominator


def family_check(n, cap=6):
    p = add(X, mul(power(X, n), Y))
    px = deriv(p, "x")
    py = deriv(p, "y")

    # Explicit Bezout lift V_0(P)=1.
    va = sub(ONE, scale(n, mul(power(X, n - 1), Y)))
    vb = scale(n * n, mul(power(X, n - 2), power(Y, 2)))
    assert apply_field(va, vb, p) == ONE
    kappa_rep = mono(n - 2, 1, n * (n + 1))
    assert divergence(va, vb) == kappa_rep

    # D_P=P_y*d_x-P_x*d_y=-X_P is divergence-free.
    assert divergence(py, scale(-1, px)) == {}

    direct_h, direct_coeffs, direct_terminal = direct_slice_truncation(n, cap)
    corr_h, corr_coeffs, corr_target, corr_terminal = (
        kappa_correction_truncation(n, cap)
    )
    assert corr_target == kappa_rep
    rat_num, rat_den = rational_slice_cleared_identity(n)

    # Finite enumeration check for the relevant weights.  The report proves
    # these parametrizations for all exponents; this is only an independent
    # bounded replay.
    bound = 40
    direct_enum = {(i, j) for i in range(bound + 1) for j in range(bound + 1)
                   if i - (n - 1) * j == 1 - n}
    direct_chain = {(k * (n - 1), k + 1) for k in range(bound + 1)
                    if k * (n - 1) <= bound and k + 1 <= bound}
    assert direct_enum == direct_chain

    corr_enum = {(i, j) for i in range(bound + 1) for j in range(bound + 1)
                 if i - (n - 1) * j == -n}
    corr_chain = {((n - 1) * k + n - 2, k + 2) for k in range(bound + 1)
                  if (n - 1) * k + n - 2 <= bound and k + 2 <= bound}
    assert corr_enum == corr_chain

    return {
        "P": f"x+x^{n}*y",
        "V0(P)": "1",
        "kappa_representative": poly_text(kappa_rep),
        "weight": f"w(i,j)=i-{n-1}*j; X_P shift={n-1}",
        "direct_slice_coefficients_k0_to_6": [frac_text(c) for c in direct_coeffs],
        "direct_terminal_at_N6": poly_text(direct_terminal),
        "kappa_correction_coefficients_k0_to_6": [frac_text(c) for c in corr_coeffs],
        "kappa_terminal_at_N6": poly_text(corr_terminal),
        "rational_slice_numerator": poly_text(rat_num),
        "rational_slice_denominator": poly_text(rat_den),
    }


def main():
    families = {str(n): family_check(n) for n in (2, 3, 4, 7)}
    assert families["3"]["direct_slice_coefficients_k0_to_6"][:6] == [
        "1", "-3/2", "2", "-5/2", "3", "-7/2"
    ]
    assert families["3"]["kappa_correction_coefficients_k0_to_6"][:6] == [
        "6", "-10", "15", "-21", "28", "-36"
    ]
    result = {
        "arithmetic": "exact fractions / sparse bivariate polynomials",
        "controls": coordinate_controls(),
        "family_checks": families,
        "scope": "finite replay plus symbolic formulas; exhaustiveness is the report's weight proof",
        "verdict": "PASS: GENERAL-N TERMINAL OBSTRUCTION REPLAYED",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
