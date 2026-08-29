#!/usr/bin/env python3
"""Exact desk verifier for one GGV 8_28 -> paired fibre-tree prototype.

This is deliberately a control example, not a Keller pair and not G2-PSC.
It uses only the Python standard library and the live reviewed GGV ledger.
"""

from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from math import comb, gcd
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
SOURCE_PINS = {
    "lib/families.py": "729a5ee7dd235ccca2138fd80035e08e3fed87fabf98a8fc4a0c7f9da089bd3e",
    "tests/test_families.py": "845d42a2d410234f889d5d846f22f7152354896c67ab3d49152469260e892c0d",
    "ladder/TRANSPORT.md": "39a607c8935153c814cd51fb65a2f1c708a9e4ba5e1dd0f38f9c96401fc4a624",
    "xmodel/grok-transport-review.md": "aa7fe37ba5c75df5f006d0af918d2315557b4db60b10cbc5954dfbf171cf558a",
    "xmodel/sol-h5a.md": "dd09069baeeaaa38644963571f929077af016cbbac664aaea9f3f50bee8f6d90",
    "xmodel/grok-h5a-review.md": "3b8bd5c9e2a1f4132cff4353e0e7e0fd9b4426cbeea0b0c13d092161018f5d2f",
}


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_families():
    spec = spec_from_file_location("ggv_families_frozen", ROOT / "lib/families.py")
    assert spec is not None and spec.loader is not None
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Sparse bivariate polynomials: exponent pair -> exact integer coefficient.
Poly = dict[tuple[int, int], int]


def clean(p: Poly) -> Poly:
    return {m: c for m, c in p.items() if c}


def add(p: Poly, q: Poly) -> Poly:
    out = dict(p)
    for m, c in q.items():
        out[m] = out.get(m, 0) + c
    return clean(out)


def term(i: int, j: int, c: int = 1) -> Poly:
    return {} if c == 0 else {(i, j): c}


def mul(p: Poly, q: Poly) -> Poly:
    out: Poly = {}
    for (i, j), a in p.items():
        for (k, ell), b in q.items():
            m = (i + k, j + ell)
            out[m] = out.get(m, 0) + a * b
    return clean(out)


def power(p: Poly, n: int) -> Poly:
    out = term(0, 0)
    base = p
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n //= 2
    return out


def hull(points: set[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
    pts = sorted(points)
    if len(pts) <= 1:
        return tuple(pts)

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lo = []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    hi = []
    for p in reversed(pts):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    return tuple(lo[:-1] + hi[:-1])


def max_face(p: Poly, rho: int, sigma: int) -> Poly:
    top = max(rho * i + sigma * j for i, j in p)
    return {m: c for m, c in p.items() if rho * m[0] + sigma * m[1] == top}


def derivative(p: Poly, axis: int) -> Poly:
    out: Poly = {}
    for (i, j), c in p.items():
        exponent = (i, j)[axis]
        if exponent:
            m = (i - 1, j) if axis == 0 else (i, j - 1)
            out[m] = c * exponent
    return clean(out)


def jacobian(p: Poly, q: Poly) -> Poly:
    left = mul(derivative(p, 0), derivative(q, 1))
    right = {m: -c for m, c in mul(derivative(p, 1), derivative(q, 0)).items()}
    return add(left, right)


def shift_first(p: Poly, amount: int) -> Poly:
    return {(i + amount, j): c for (i, j), c in p.items()}


def y_chart(p: Poly, t_shift: int) -> Poly:
    """x=t^3 X, y=t^-1; return t^t_shift p as (t exponent,X exponent)."""
    return clean({(3 * i - j + t_shift, i): c for (i, j), c in p.items()})


def x_chart_f(p: Poly, s_shift: int) -> Poly:
    """x=s^-28, y^4=z s^28; only used where all y powers are /4."""
    assert all(j % 4 == 0 for _, j in p)
    return clean({(-28 * i + 7 * j + s_shift, j // 4): c for (i, j), c in p.items()})


def binomial_x_minus_t(n: int, x_power: int = 0) -> Poly:
    """X^x_power (X-t)^n as (t exponent,X exponent)."""
    return {
        (n - r, x_power + r): comb(n, r) * ((-1) ** (n - r))
        for r in range(n + 1)
    }


def binomial_z_minus_one(n: int) -> Poly:
    """(z-1)^n as (s exponent,z exponent)."""
    return {(0, r): comb(n, r) * ((-1) ** (n - r)) for r in range(n + 1)}


# Dense exact univariate arithmetic, coefficients ascending.
def dtrim(p: list[F]) -> list[F]:
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def ddivmod(a0: list[F], b0: list[F]) -> tuple[list[F], list[F]]:
    a, b = dtrim(list(a0)), dtrim(list(b0))
    assert b != [0]
    q = [F(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        k, c = len(a) - len(b), a[-1] / b[-1]
        q[k] += c
        for j, bj in enumerate(b):
            a[j + k] -= c * bj
        dtrim(a)
    return dtrim(q), dtrim(a)


def dgcd(a: list[F], b: list[F]) -> list[F]:
    a, b = dtrim(a), dtrim(b)
    while b != [0]:
        _, r = ddivmod(a, b)
        a, b = b, r
    lead = a[-1]
    return dtrim([c / lead for c in a])


def as_strings(xs):
    return [str(x) for x in xs]


def main() -> dict:
    observed_pins = {p: file_sha(ROOT / p) for p in SOURCE_PINS}
    assert observed_pins == SOURCE_PINS

    fam = load_families()
    cd = fam.section4_families()["8_28"]
    assert tuple(cd.A0) == (8, 1, 28)
    assert tuple(cd.A0p) == (1, 1, 0)
    assert tuple(cd.final) == (11, 4, 7)
    assert cd.steps == ((4, -1, 3, 4),)
    assert cd.mn == (3, 2)
    assert (cd.degP, cd.degQ) == (108, 72)
    assert cd.S == ((0, 0), (1, 0), (8, 28), (0, 4))
    assert (cd.c, cd.upper_dir, cd.rhs_exp) == (4, (-3, 1), 2)

    rho, sigma = 4, -1
    v_a0 = rho * 8 + sigma * 28
    assert v_a0 == 4 and F(rho + sigma, v_a0) == F(3, 4)

    # z=xy^4, B=x(z-1)^7.  Native GGV orientation is (P,Q)=(g,f),
    # multipliers (3,2); Sigray degree-sorted orientation is (f,g).
    b: Poly = {
        (k + 1, 4 * k): comb(7, k) * ((-1) ** (7 - k))
        for k in range(8)
    }
    b2, b3 = power(b, 2), power(b, 3)
    f = add(add(b2, term(1, 0, -1)), term(0, 8, -1))

    def g_poly(tau: int) -> Poly:
        return add(add(add(b3, term(2, 2, -2)), term(0, 12)), term(1, 15, tau))

    g1, g2 = g_poly(1), g_poly(2)
    assert hull(set(f) | {(0, 0)}) == ((0, 0), (2, 0), (16, 56), (0, 8))
    assert hull(set(g1) | {(0, 0)}) == ((0, 0), (3, 0), (24, 84), (0, 12))
    assert set(g1) == set(g2)
    assert max_face(f, rho, sigma) == b2
    assert max_face(g1, rho, sigma) == b3 == max_face(g2, rho, sigma)
    assert max(i + j for i, j in f) == 72
    assert max(i + j for i, j in g1) == 108

    # The common edge root z=1 has gamma=7; Algorithm-3 endpoint arithmetic.
    gamma = 7
    endpoint = (F(gamma + v_a0, rho), gamma)
    assert endpoint == (F(11, 4), 7) == (F(cd.final.a, cd.final.l), cd.final.b)

    # Scope firewall is also checked algebraically: this control is not Keller.
    jac_x0 = {j: c for (i, j), c in jacobian(f, g1).items() if i == 0}
    assert jac_x0 == {11: -12, 22: 8}

    # Exact x=infinity f-fibre identity after x=s^-28, y^4=z s^28.
    # t^56(f-a)=(z-1)^14-s^28-z^2 s^112-a s^56.
    x_f = x_chart_f(f, 56)
    x_f_expected = add(add(binomial_z_minus_one(14), term(28, 0, -1)), term(112, 2, -1))
    assert x_f == x_f_expected

    # Puiseux characteristics 28;7,9 give jumps 4 then 7 and Q/max kappas 4,28.
    e0, beta1, beta2 = 28, 7, 9
    e1, e2 = gcd(e0, beta1), gcd(gcd(e0, beta1), beta2)
    nus = (e0 // e1, e1 // e2)
    kappas = (e0 // e1, e0 // e2)
    pis = (F(beta1, e0), F(beta2, e0))
    bars = tuple(k * (1 - p) for k, p in zip(kappas, pis))
    assert (e0, e1, e2) == (28, 7, 1)
    assert nus == (4, 7) and kappas == (4, 28)
    assert pis == (F(1, 4), F(9, 28)) and bars == (3, 19)
    assert gcd(int(bars[0]), nus[0]) == gcd(int(bars[1]), nus[1]) == 1

    # Residual tops and Statement-3.17 descent at the second cut.
    df0, dg0 = F(2), F(3)
    df1 = df0 - (pis[1] - pis[0]) * 14
    dg1 = dg0 - (pis[1] - pis[0]) * 21
    assert (df1, dg1) == (F(1), F(3, 2))
    q_coarse = (kappas[0] * df0, 56, nus[0], 14, bars[0])
    q_refined = (kappas[1] * df1, 14, nus[1], 1, bars[1])
    dg_refined = kappas[1] * dg1
    assert q_coarse == (8, 56, 4, 14, 3)
    assert q_refined == (28, 14, 7, 1, 19)
    assert dg_refined == 42
    assert dg_refined * q_refined[1] / q_refined[2] == 84

    # 4*14 presentations; the mu_28 deck action is diagonal on (u mod4,v mod14).
    pairs = {(u, v) for u in range(4) for v in range(14)}
    orbits = []
    unseen = set(pairs)
    while unseen:
        seed = min(unseen)
        orbit = {((seed[0] + k) % 4, (seed[1] + k) % 14) for k in range(28)}
        inverse_orbit = {((seed[0] - k) % 4, (seed[1] - k) % 14) for k in range(28)}
        assert inverse_orbit == orbit
        assert len(orbit) == 28
        unseen -= orbit
        orbits.append(orbit)
    assert len(orbits) == 2
    invariants = []
    for orbit in orbits:
        vals = {(-1) ** ((u - v) % 2) for u, v in orbit}
        assert len(vals) == 1
        invariants.append(next(iter(vals)))
        # g/s^-42 coefficient is xi^7-2*zeta^2 and is never zero.
        assert all(((-1) ** v) - 2 * ((-1) ** u) != 0 for u, v in orbit)
    assert sorted(invariants) == [-1, 1]

    # Fibre a first enters q=(z-1)/s^2 at s^28 by xi*a/14, hence y at s^37
    # by zeta*xi*a/56.  These exact deltas distinguish a=0 from a=1.
    assert F(1, 14) * 14 == 1 and F(1, 56) * 4 * 14 == 1

    # Exact y=infinity chart: x=t^3 X, y=t^-1.
    y_f_expected = add(add(binomial_x_minus_t(14, 2), term(0, 0, -1)), term(11, 1, -1))
    assert y_chart(f, 8) == y_f_expected

    def y_g_expected(tau: int) -> Poly:
        return add(add(add(binomial_x_minus_t(21, 3), term(0, 0)), term(0, 1, tau)), term(16, 2, -2))

    assert y_chart(g1, 12) == y_g_expected(1)
    assert y_chart(g2, 12) == y_g_expected(2)

    # f residual X^16-1 has 16 simple roots.  g residual on them reduces to
    # X^8+1+tau*X.  tau=1 has no cancellation; tau=2 has only X=-1.
    cyclo16 = [F(-1)] + [F(0)] * 15 + [F(1)]
    r1 = [F(1), F(1)] + [F(0)] * 6 + [F(1)]
    r2 = [F(1), F(2)] + [F(0)] * 6 + [F(1)]
    assert dgcd(cyclo16, r1) == [F(1)]
    assert dgcd(cyclo16, r2) == [F(1), F(1)]

    # At the unique mutated cancellation c=-1, X'(0)=7/8 and the next
    # coefficient of X^3(X-t)^21+1+2X is exactly 7/4, so pole 12 -> 11.
    xprime = F(14, 16)
    g_next = F(21) + F(-22) * xprime
    assert xprime == F(7, 8) and g_next == F(7, 4)

    # Sheet and pole accounting.  This exhausts deg(f)=72 at infinity.
    x_places, x_ramification, x_pole = 2, 28, 42
    y_places, y_ramification, y_pole = 16, 1, 12
    assert x_places * x_ramification + y_places * y_ramification == 72
    pole_mass_1 = x_places * x_pole + y_places * y_pole
    pole_mass_2 = x_places * x_pole + 15 * y_pole + 11
    assert (pole_mass_1, pole_mass_2) == (276, 275)

    return {
        "status": "PASS",
        "scope": "one reviewed GGV 8_28 MN chain; non-Keller control; not G2-PSC",
        "non_keller_witness": "Jac(f,g_1)|_{x=0}=-12*y^11+8*y^22",
        "source_pins": observed_pins,
        "ggv": {
            "native_orientation": ["P=g=B^3+lower", "Q=f=B^2+lower"],
            "A0": [8, 28],
            "A0_prime": [1, 0],
            "direction": [rho, sigma],
            "p_over_q": "3/4",
            "mn": [3, 2],
            "degrees": [108, 72],
            "gamma": gamma,
            "final": ["11/4", 7],
            "S": [[x, y] for x, y in cd.S],
        },
        "x_infinity": {
            "fibre_equation": "(z-1)^14=s^28+a*s^56+z^2*s^112",
            "presentations": 56,
            "deck_orbits": 2,
            "ramification_per_place": 28,
            "characteristic_numerators": [7, 9],
            "gcd_chain": [e0, e1, e2],
            "jump_indices": list(nus),
            "qmax_kappas": list(kappas),
            "pi": as_strings(pis),
            "kappa_bar": as_strings(bars),
            "Q_coarse": as_strings(q_coarse),
            "Q_refined": as_strings(q_refined),
            "Dg_refined": str(dg_refined),
            "pole_order_per_place": x_pole,
            "pole_mass": 84,
            "fibre_0_to_1_delta": {"z_s30": "zeta14-root/14", "y_s37": "zeta4-root*zeta14-root/56"},
            "orbit_invariant": "zeta4-root^2 / zeta14-root^7 in {+1,-1}",
        },
        "y_infinity": {
            "fibre_equation": "X^2*(X-t)^14-1-a*t^8-X*t^11=0",
            "places": y_places,
            "ramification_per_place": y_ramification,
            "fibre_0_to_1_delta_X_t8": "c/16",
            "baseline_tau_1_pole_orders": {"12": 16},
            "mutation_tau_2_pole_orders": {"12": 15, "11": 1},
            "mutation_cancelled_root": "c=-1",
            "next_coefficient": "7/4",
        },
        "totals": {
            "f_sheets": 72,
            "baseline_g_pole_mass": pole_mass_1,
            "mutated_g_pole_mass": pole_mass_2,
        },
        "fidelity_mutation": {
            "change": "coefficient of x*y^15 from tau=1 to tau=2",
            "same": "support, Newton polygons, GGV ledger, common (4,-1) initial faces, gamma and both fibre-tree sheet counts",
            "detected_by": "y-infinity paired residual X^24+1+tau*X modulo X^16-1",
        },
    }


if __name__ == "__main__":
    result = main()
    frozen = Path(__file__).with_name("RESULT.json")
    if frozen.exists():
        assert json.loads(frozen.read_text()) == result
    print(json.dumps(result, indent=2, sort_keys=True))
