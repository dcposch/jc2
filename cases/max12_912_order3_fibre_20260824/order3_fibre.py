#!/usr/bin/env python3
"""Exact order-3 invariant-fibre compiler for the (9,12) frontier.

This producer consumes the frozen shared Faber theorem, specializes to the
nontrivial cubic Kummer leaf, reconstructs r_1,...,r_8, checks their
characters and the common-cubic subfamily, and registers the corrected
terminal rational positive control.  With --singular it emits the universal
seven-equation fibre ideal for an independent CAS decomposition.

No polynomial-core branch or Taylor boundary is discarded, and no emptiness
claim is made.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import argparse
import importlib.util
import json
import sys


ROOT = Path(__file__).resolve().parents[2]
SHARED_PATH = ROOT / "cases/max12_high_row_probe_20260824/shared_faber_probe.py"
EXPECTED_HASHES = {
    "xmodel/max12-partial-y-kummer-preflight-20260824.md":
        "30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07",
    "cases/max12_partial_y_preflight_20260824/FREEZE.sha256":
        "59ef0712aea2424ea57b6f1727031018e769701b0f2e2384eb4638f4286ea558",
    "xmodel/max12-partial-y-shared-faber-probe-20260824.md":
        "d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036",
    "cases/max12_high_row_probe_20260824/shared_faber_probe.py":
        "69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f",
    "cases/max12_high_row_probe_20260824/FREEZE.sha256":
        "3a25edb31a53ecee9c96e039ab4a947908ebc0542123fb131447e1a661f45a28",
}


class FibreFailure(RuntimeError):
    pass


def load_shared():
    spec = importlib.util.spec_from_file_location("max12_shared_frozen", SHARED_PATH)
    if spec is None or spec.loader is None:
        raise FibreFailure("cannot load shared compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


M = load_shared()
Coeff = M.Coeff
ZPoly = M.ZPoly


def pin_inputs() -> dict[str, str]:
    out = {}
    for rel, expected in EXPECTED_HASHES.items():
        got = sha256((ROOT / rel).read_bytes()).hexdigest()
        if got != expected:
            raise FibreFailure(f"input hash mismatch {rel}: {got}")
        out[rel] = got
    return out


def faber(ring, m: int, j: int, U: ZPoly) -> ZPoly:
    one = ring.one
    out: ZPoly = {j: one}
    Upower: ZPoly = {0: one}
    for q in range(1, j // 2 + 1):
        Upower = M.zmul(Upower, U)
        term = {exponent + j: coeff for exponent, coeff in Upower.items()
                if exponent + j >= 0}
        out = M.zadd(
            out,
            M.zscale(M.binomial(Fraction(j, m), q), term),
        )
    return M.zclean(out)


def inverse_root(ring, m: int, max_q: int) -> ZPoly:
    one = ring.one
    out: ZPoly = {1: one}
    for q in range(1, max_q + 1):
        target = m - 1 - q
        residual = M.zpower_coefficient(out, m, target, one)
        for i in range(m - 1):
            residual = M.cadd(
                residual,
                M.cmul(
                    ring.var(f"a{i}"),
                    M.zpower_coefficient(out, i, target, one),
                ),
            )
        correction = M.cscale(Fraction(-1, m), residual)
        if correction:
            out[-q] = correction

    # Fail closed on every coefficient used to solve the inverse.
    for q in range(1, max_q + 1):
        target = m - 1 - q
        residual = M.zpower_coefficient(out, m, target, one)
        for i in range(m - 1):
            residual = M.cadd(
                residual,
                M.cmul(
                    ring.var(f"a{i}"),
                    M.zpower_coefficient(out, i, target, one),
                ),
            )
        if residual:
            raise FibreFailure(("inverse root residual", target))
    return out


def substitute_coeff(value: Coeff, images: list[Coeff], target_ring) -> Coeff:
    out: Coeff = {}
    for mon, scalar in value.items():
        term = M.cscale(scalar, target_ring.one)
        for exponent, image in zip(mon, images):
            for _ in range(exponent):
                term = M.cmul(term, image)
        out = M.cadd(out, term)
    return out


def poly_add(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    out = dict(a)
    for exponent, coeff in b.items():
        out[exponent] = out.get(exponent, Fraction(0)) + coeff
    return {exponent: coeff for exponent, coeff in out.items() if coeff}


def poly_scale(scalar: Fraction | int, a: dict[int, Fraction]) -> dict[int, Fraction]:
    scalar = Fraction(scalar)
    return {exponent: scalar * coeff for exponent, coeff in a.items()
            if scalar * coeff}


def poly_mul(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for i, left in a.items():
        for j, right in b.items():
            out[i + j] = out.get(i + j, Fraction(0)) + left * right
    return {exponent: coeff for exponent, coeff in out.items() if coeff}


def poly_derivative(a: dict[int, Fraction]) -> dict[int, Fraction]:
    return {exponent - 1: exponent * coeff for exponent, coeff in a.items()
            if exponent}


def class_order(d: int, valuations: list[int]) -> int:
    for exponent in range(1, d + 1):
        if all(exponent * value % d == 0 for value in valuations):
            return exponent
    raise FibreFailure((d, valuations))


def terminal_positive_control() -> dict[str, object]:
    # h=x^2(x-1)^4 and R=C/[x(x-1)^3].  Clearing d^2 from
    # 9*h*R'+6*h'*R gives C*(-9*h*d'+6*h'*d).
    x = {1: Fraction(1)}
    xm1 = {1: Fraction(1), 0: Fraction(-1)}
    h = poly_mul(poly_mul(x, x), poly_mul(poly_mul(xm1, xm1), poly_mul(xm1, xm1)))
    denominator = poly_mul(x, poly_mul(poly_mul(xm1, xm1), xm1))
    numerator = poly_add(
        poly_scale(-9, poly_mul(h, poly_derivative(denominator))),
        poly_scale(6, poly_mul(poly_derivative(h), denominator)),
    )
    expected = poly_scale(-3, poly_mul(denominator, denominator))
    if numerator != expected:
        raise FibreFailure((numerator, expected))
    # Divisor residues modulo three: 2 at 0, 4 at 1, -6 at infinity.
    if class_order(3, [2, 4, -6]) != 3:
        raise FibreFailure("positive control is not order three")
    return {
        "h": "x^2*(x-1)^4",
        "R": "C/(x*(x-1)^3)",
        "Kummer_class_order": 3,
        "identity": "9*h*R'+6*h'*R=-3*C",
        "Keller_choice": "C=-j/3",
        "terminal_ODE_alone_contradictory": False,
    }


def spectral_identity() -> dict[str, object]:
    # Formal elimination identity and its g-derivative.
    ring = M.Ring(["f", "g", "k"])
    f = ring.var("f")
    g = ring.var("g")
    k = ring.var("k")
    f2 = M.cmul(f, f)
    W = M.cadd(
        M.cadd(
            M.cmul(M.cmul(g, g), g),
            M.cscale(-1, M.cmul(f2, f2)),
        ),
        M.cadd(
            M.cscale(-3, M.cmul(M.cmul(k, f2), g)),
            M.cscale(-1, M.cmul(M.cmul(M.cmul(k, k), k), f2)),
        ),
    )
    Wg = M.cpartial(W, 1)
    expected_Wg = M.cscale(
        3, M.cadd(M.cmul(g, g), M.cscale(-1, M.cmul(k, f2)))
    )
    if Wg != expected_Wg:
        raise FibreFailure("spectral g derivative")

    # Check W=0 at f=t^3, g=t^4+k*t^2.
    kr = M.Ring(["k"])
    kt = kr.var("k")
    ft: ZPoly = {3: kr.one}
    gt: ZPoly = {4: kr.one, 2: kt}
    spectral_t = M.zadd(
        M.zadd(
            M.zpower(gt, 3, kr.one),
            M.zscale(-1, M.zpower(ft, 4, kr.one)),
        ),
        M.zadd(
            M.zscale(-3, M.zmul({0: kt}, M.zmul(M.zpower(ft, 2, kr.one), gt))),
            M.zscale(-1, M.zmul({0: M.cmul(M.cmul(kt, kt), kt)},
                                M.zpower(ft, 2, kr.one))),
        ),
    )
    if spectral_t:
        raise FibreFailure("spectral elimination identity")

    # With g=H-T, H=w^12+k*w^6, recover the exact tail identity.
    tr = M.Ring(["k", "T"])
    kv = tr.var("k")
    Tv = tr.var("T")
    H: ZPoly = {12: tr.one, 6: kv}
    gtail = M.zadd(H, {0: M.cscale(-1, Tv)})
    fw: ZPoly = {9: tr.one}
    Wtail = M.zadd(
        M.zadd(
            M.zpower(gtail, 3, tr.one),
            M.zscale(-1, M.zpower(fw, 4, tr.one)),
        ),
        M.zadd(
            M.zscale(-3, M.zmul({0: kv},
                                M.zmul(M.zpower(fw, 2, tr.one), gtail))),
            M.zscale(-1, M.zmul(
                {0: M.cmul(M.cmul(kv, kv), kv)},
                M.zpower(fw, 2, tr.one),
            )),
        ),
    )
    H2_minus = M.zadd(M.zpower(H, 2, tr.one), {18: M.cscale(-1, kv)})
    expected_tail = M.zadd(
        M.zadd(
            {exponent: M.cscale(-3, M.cmul(coeff, Tv))
             for exponent, coeff in H2_minus.items()},
            {exponent: M.cscale(3, M.cmul(coeff, M.cmul(Tv, Tv)))
             for exponent, coeff in H.items()},
        ),
        {0: M.cscale(-1, M.cmul(M.cmul(Tv, Tv), Tv))},
    )
    if Wtail != expected_tail:
        raise FibreFailure("spectral tail identity")

    return {
        "W": "g^3-f^4-3*k*f^2*g-k^3*f^2",
        "common_spectral_parametrization": "f=t^3,g=t^4+k*t^2",
        "Jacobian_identity": "J(f,W)=3*(g^2-k*f^2)*J(f,g)",
        "tail_identity": (
            "W=-3*(H^2-k*w^18)*T+3*H*T^2-T^3, "
            "H=w^12+k*w^6"
        ),
        "first_possible_degrees": {"mu_r3": 21, "nu_r6": 18, "r8": 16},
        "k0_mu0_nu0_Mason_gate": {
            "identity": "W=g^3-f^4",
            "if_gcd_f_g_one": "deg(W)>=16",
            "terminal_nonzero_r8": "deg(W)=16, hence Mason equality",
            "consequence": "squarefree/coprime equality case, not contradiction",
        },
    }


def compile_fibre() -> dict[str, object]:
    m, n = 9, 12
    names = [f"a{i}" for i in range(m - 1)] + ["k"]
    ring = M.Ring(names)
    one = ring.one

    f: ZPoly = {m: one}
    U: ZPoly = {}
    for i in range(m - 1):
        ai = ring.var(f"a{i}")
        f[i] = ai
        U[i - m] = ai

    F6 = faber(ring, m, 6, U)
    F12 = faber(ring, m, 12, U)
    g = M.zadd(
        F12,
        {exponent: M.cmul(ring.var("k"), coeff)
         for exponent, coeff in F6.items()},
    )

    # r_8 requires z(w) through q=n+8-1=19.
    z_of_w = inverse_root(ring, m, n + 7)
    tails: dict[int, Coeff] = {}
    for ell in range(1, 9):
        coefficient: Coeff = {}
        for z_exponent, g_coefficient in g.items():
            coefficient = M.cadd(
                coefficient,
                M.cmul(
                    g_coefficient,
                    M.zpower_coefficient(z_of_w, z_exponent, -ell, one),
                ),
            )
        tails[ell] = M.cscale(-1, coefficient)

    # sigma(z)=zeta*z, hence wt(a_i)=-i and wt(k)=0 mod 3.
    variable_weights = [(-i) % 3 for i in range(m - 1)] + [0]
    for ell, value in tails.items():
        expected_weight = ell % 3
        for mon in value:
            got = sum(exponent * weight
                      for exponent, weight in zip(mon, variable_weights)) % 3
            if got != expected_weight:
                raise FibreFailure(("weight mismatch", ell, mon, got))

    # Exact common-cubic subfamily K=z^3+p*z+q, f=K^3,
    # g=K^4+k*K^2.  Every negative tail must vanish identically.
    target_ring = M.Ring(["p", "q", "k"])
    K: ZPoly = {
        3: target_ring.one,
        1: target_ring.var("p"),
        0: target_ring.var("q"),
    }
    K3 = M.zpower(K, 3, target_ring.one)
    images = [K3.get(i, {}) for i in range(m - 1)] + [target_ring.var("k")]
    transverse_tails: dict[int, Coeff] = {}
    for ell, value in tails.items():
        if substitute_coeff(value, images, target_ring):
            raise FibreFailure(("common cubic tail", ell))

    # Reintroduce transverse coefficients x_0,...,x_5 in
    # f=K^3+sum x_i z^i.  This triangular change exposes the normal
    # Kuranishi map while retaining p,q,k as boundary parameters.
    transverse_ring = M.Ring([f"x{i}" for i in range(6)] + ["p", "q", "k"])
    K_transverse: ZPoly = {
        3: transverse_ring.one,
        1: transverse_ring.var("p"),
        0: transverse_ring.var("q"),
    }
    K3_transverse = M.zpower(K_transverse, 3, transverse_ring.one)
    transverse_images = []
    for i in range(m - 1):
        image = K3_transverse.get(i, {})
        if i <= 5:
            image = M.cadd(image, transverse_ring.var(f"x{i}"))
        transverse_images.append(image)
    transverse_images.append(transverse_ring.var("k"))
    transverse_tails = {
        ell: substitute_coeff(tails[ell], transverse_images, transverse_ring)
        for ell in range(1, 9)
    }

    def transverse_degree_part(value: Coeff, wanted: int) -> Coeff:
        return {mon: coeff for mon, coeff in value.items()
                if sum(mon[:6]) == wanted}

    linear = {ell: transverse_degree_part(transverse_tails[ell], 1)
              for ell in range(1, 8)}
    p_var = transverse_ring.var("p")
    q_var = transverse_ring.var("q")
    alpha = M.cadd(
        M.cscale(
            Fraction(2, 81), M.cmul(M.cmul(p_var, p_var), p_var)
        ),
        M.cscale(Fraction(-1, 9), M.cmul(q_var, q_var)),
    )
    beta = M.cscale(Fraction(-1, 9), M.cmul(p_var, q_var))

    linear_relations = {
        "L4": M.cadd(
            linear[4],
            M.cadd(
                M.cscale(Fraction(2, 3), M.cmul(q_var, linear[1])),
                M.cscale(Fraction(1, 3), M.cmul(p_var, linear[2])),
            ),
        ),
        "L5": M.cadd(
            linear[5],
            M.cadd(
                M.cscale(Fraction(-1, 9),
                         M.cmul(M.cmul(p_var, p_var), linear[1])),
                M.cscale(Fraction(1, 3), M.cmul(q_var, linear[2])),
            ),
        ),
        "L6": linear[6],
        "L7": M.cadd(
            linear[7],
            M.cadd(
                M.cscale(-1, M.cmul(alpha, linear[1])),
                M.cscale(-1, M.cmul(beta, linear[2])),
            ),
        ),
    }
    if any(linear_relations.values()):
        raise FibreFailure("normal linear relations failed")

    # The x2,x1,x0 columns of L1,L2,L3 form a diagonal minor
    # ((2/3)k)^3, so the normal rank is exactly three on k!=0.
    expected_pivots = {
        (1, 2): "2/3*k", (2, 1): "2/3*k", (3, 0): "2/3*k"
    }
    for (ell, xi), expected in expected_pivots.items():
        derivative = M.cpartial(linear[ell], xi)
        if M.coeff_string(derivative, transverse_ring.names) != expected:
            raise FibreFailure((ell, xi, derivative))

    # Exact cokernel combinations before restricting to the normal kernel.
    E4 = M.cadd(
        transverse_tails[4],
        M.cadd(
            M.cscale(Fraction(2, 3), M.cmul(q_var, transverse_tails[1])),
            M.cscale(Fraction(1, 3), M.cmul(p_var, transverse_tails[2])),
        ),
    )
    E5 = M.cadd(
        transverse_tails[5],
        M.cadd(
            M.cscale(Fraction(-1, 9),
                     M.cmul(M.cmul(p_var, p_var), transverse_tails[1])),
            M.cscale(Fraction(1, 3), M.cmul(q_var, transverse_tails[2])),
        ),
    )
    E6 = transverse_tails[6]
    E7 = M.cadd(
        transverse_tails[7],
        M.cadd(
            M.cscale(-1, M.cmul(alpha, transverse_tails[1])),
            M.cscale(-1, M.cmul(beta, transverse_tails[2])),
        ),
    )

    # ker(L) is phi=K*(A+B*z+C*(z^2-p)).
    kernel_ring = M.Ring(["A", "B", "C", "p", "q", "k"])
    A_var = kernel_ring.var("A")
    B_var = kernel_ring.var("B")
    C_var = kernel_ring.var("C")
    pk = kernel_ring.var("p")
    qk = kernel_ring.var("q")
    kk = kernel_ring.var("k")
    kernel_images = [
        M.cadd(M.cmul(qk, A_var),
               M.cscale(-1, M.cmul(M.cmul(pk, qk), C_var))),
        M.cadd(M.cadd(M.cmul(pk, A_var), M.cmul(qk, B_var)),
               M.cscale(-1, M.cmul(M.cmul(pk, pk), C_var))),
        M.cadd(M.cmul(pk, B_var), M.cmul(qk, C_var)),
        A_var,
        B_var,
        C_var,
        pk,
        qk,
        kk,
    ]
    restricted = {
        4: substitute_coeff(E4, kernel_images, kernel_ring),
        5: substitute_coeff(E5, kernel_images, kernel_ring),
        6: substitute_coeff(E6, kernel_images, kernel_ring),
        7: substitute_coeff(E7, kernel_images, kernel_ring),
    }
    quadrics = {
        index: {mon: coeff for mon, coeff in value.items()
                if sum(mon[:3]) == 2}
        for index, value in restricted.items()
    }
    expected_quad_digests = {
        4: "04664d2e6ad2f3879799a02166e7b700695d8397e959f7ba04921b84f6d41982",
        5: "cc5ba8e37e857ad062099679a68b67f6a6446b0f62ed0f484b44594b1ce59498",
        6: "c9bc9e2f7959fe5ff18b24899a3e55c15e103c6de8543a2d1718de52b0879da8",
        7: "117142538c12b42fdc484601e4d27ed241af792861676d9de47f2601716ea3c7",
    }
    for index, expected in expected_quad_digests.items():
        if M.coefficient_digest(quadrics[index]) != expected:
            raise FibreFailure(("quadratic digest", index))

    # Projective chart C=1, Q4=0 gives A=(3p-B^2)/2.  Verify
    # Q5=(k/9)(B^3+pB+q), Q7=-(kp/27)(B^3+pB+q), and
    # Q6=-(k/36)(3B^2+p)^2 exactly.
    chart_ring = M.Ring(["B", "p", "q", "k"])
    Bc = chart_ring.var("B")
    pc = chart_ring.var("p")
    qc = chart_ring.var("q")
    kc = chart_ring.var("k")
    A_chart = M.cscale(
        Fraction(1, 2),
        M.cadd(M.cscale(3, pc), M.cscale(-1, M.cmul(Bc, Bc))),
    )
    chart_images = [A_chart, Bc, chart_ring.one, pc, qc, kc]
    chart_quadrics = {
        index: substitute_coeff(quadrics[index], chart_images, chart_ring)
        for index in quadrics
    }
    cubic = M.cadd(
        M.cadd(M.cmul(M.cmul(Bc, Bc), Bc), M.cmul(pc, Bc)), qc
    )
    if chart_quadrics[4]:
        raise FibreFailure("Q4 chart does not vanish")
    if M.cadd(chart_quadrics[5],
              M.cscale(Fraction(-1, 9), M.cmul(kc, cubic))):
        raise FibreFailure("Q5 chart identity")
    if M.cadd(chart_quadrics[7],
              M.cscale(Fraction(1, 27),
                       M.cmul(M.cmul(kc, pc), cubic))):
        raise FibreFailure("Q7 chart identity")
    derivative_square = M.cmul(
        M.cadd(M.cscale(3, M.cmul(Bc, Bc)), pc),
        M.cadd(M.cscale(3, M.cmul(Bc, Bc)), pc),
    )
    if M.cadd(
        M.cadd(chart_quadrics[6],
               M.cscale(Fraction(1, 36), M.cmul(kc, derivative_square))),
        M.cscale(Fraction(-2, 9), M.cmul(M.cmul(kc, Bc), cubic)),
    ):
        raise FibreFailure("Q6 chart identity")

    # On disc(K)=0 write p=-3b^2, q=2b^3.  The unique quadratic survivor is
    # (A,B,C)=(-5b^2,b,1).  Solve the image rows at order two with three free
    # kernel corrections and check the first remaining E6 coefficient at
    # order three.  It is k/81, independent of b and of all free corrections.
    lift_ring = M.Ring(["t", "U", "V", "W", "b", "k"])
    tv = lift_ring.var("t")
    Uv = lift_ring.var("U")
    Vv = lift_ring.var("V")
    Wv = lift_ring.var("W")
    bv = lift_ring.var("b")
    kl = lift_ring.var("k")

    def cpow(value: Coeff, exponent: int) -> Coeff:
        out = lift_ring.one
        for _ in range(exponent):
            out = M.cmul(out, value)
        return out

    def csum(*values: Coeff) -> Coeff:
        out: Coeff = {}
        for value in values:
            out = M.cadd(out, value)
        return out

    p_lift = M.cscale(-3, cpow(bv, 2))
    q_lift = M.cscale(2, cpow(bv, 3))
    direction = [
        M.cscale(-4, cpow(bv, 5)),
        M.cscale(8, cpow(bv, 4)),
        M.cscale(-1, cpow(bv, 3)),
        M.cscale(-5, cpow(bv, 2)),
        bv,
        lift_ring.one,
    ]
    correction = [
        csum(M.cscale(2, M.cmul(cpow(bv, 3), Uv)),
             M.cscale(6, M.cmul(cpow(bv, 5), Wv)),
             M.cscale(Fraction(1, 3), bv)),
        csum(M.cscale(-3, M.cmul(cpow(bv, 2), Uv)),
             M.cscale(2, M.cmul(cpow(bv, 3), Vv)),
             M.cscale(-9, M.cmul(cpow(bv, 4), Wv)),
             M.cscale(Fraction(1, 6), lift_ring.one)),
        csum(M.cscale(-3, M.cmul(cpow(bv, 2), Vv)),
             M.cscale(2, M.cmul(cpow(bv, 3), Wv))),
        Uv,
        Vv,
        Wv,
    ]
    t2 = M.cmul(tv, tv)
    lift_images = [
        csum(M.cmul(value, tv), M.cmul(second, t2))
        for value, second in zip(direction, correction)
    ] + [p_lift, q_lift, kl]
    lifted_E6 = substitute_coeff(E6, lift_images, lift_ring)
    cubic_E6 = {
        mon: coeff for mon, coeff in lifted_E6.items() if mon[0] == 3
    }
    expected_cubic = M.cscale(Fraction(1, 81), M.cmul(kl, cpow(tv, 3)))
    if cubic_E6 != expected_cubic:
        raise FibreFailure(("discriminant cubic obstruction", cubic_E6))

    constants = {
        1: "0", 2: "0", 3: "mu", 4: "0",
        5: "0", 6: "nu", 7: "0",
    }
    equations = [1, 2, 3, 4, 5, 6, 7]
    return {
        "ring_names": names,
        "tails": tails,
        "transverse_ring_names": transverse_ring.names,
        "transverse_tails": transverse_tails,
        "payload": {
            "degrees": [9, 12],
            "Kummer_order": 3,
            "normalized_H": "w^12+k*w^6",
            "tail_character": "wt(r_l)=l mod 3",
            "constant_invariant_fibre": constants,
            "fibre_equation_count": len(equations),
            "dynamic_coefficient_count_for_fixed_k_mu_nu": 8,
            "expected_curve_dimension_if_independent": 1,
            "tail_supports": {f"r{ell}": len(tails[ell])
                              for ell in range(1, 9)},
            "tail_sha256": {f"r{ell}": M.coefficient_digest(tails[ell])
                            for ell in range(1, 9)},
            "common_cubic_subfamily": {
                "K": "z^3+p*z+q",
                "f": "K^3",
                "g": "K^4+k*K^2",
                "all_r1_through_r8": 0,
                "lies_over": "mu=nu=0",
                "terminal_Keller_row": "fails because r8'=0 when j!=0",
            },
            "common_cubic_normal_gate": {
                "coordinates": "f=K^3+phi, K=z^3+p*z+q",
                "discriminant": "disc(K)=-4*p^3-27*q^2",
                "linear_rank_on_k_nonzero": 3,
                "linear_kernel": "phi=K*(A+B*z+C*(z^2-p))",
                "cokernel_combinations": {
                    "E4": "r4+(2q/3)r1+(p/3)r2",
                    "E5": "r5-(p^2/9)r1+(q/3)r2",
                    "E6": "r6",
                    "E7": "r7-((2p^3-9q^2)/81)r1+(pq/9)r2",
                },
                "quadrics": {
                    f"Q{index}": M.coeff_string(quadrics[index], kernel_ring.names)
                    for index in (4, 5, 6, 7)
                },
                "projective_directions": {
                    "C=0": "[A:B:C]=[1:0:0], Q6=-k/9",
                    "C_nonzero": (
                        "C=1, B^3+pB+q=0, A=(3p-B^2)/2, "
                        "Q6=-k*(3B^2+p)^2/36"
                    ),
                    "squarefree_fixed_mu_nu_zero": (
                        "no transverse leading direction when k!=0 and K squarefree"
                    ),
                },
                "discriminant_lift": {
                    "parameterization": "p=-3*b^2,q=2*b^3",
                    "quadratic_survivor": "[A:B:C]=[-5*b^2:b:1]",
                    "first_higher_cokernel": "E6=(k/81)*t^3+O(t^4)",
                    "consequence": "no nonzero transverse formal lift when k!=0",
                },
                "formal_trapping_consequence": (
                    "for fixed mu=nu=0 and k!=0, every reduced formal fibre "
                    "arc meeting phi=0 stays in phi=0: squarefree K is blocked "
                    "quadratically and disc(K)=0 cubically"
                ),
                "nilpotent_warning": (
                    "the quadratic gate identifies reduced formal support, "
                    "not reducedness of the completed local scheme"
                ),
                "first_cokernel_load": "nu in E6; mu is in the linear image",
                "mandatory_boundary_strata": ["k=0"],
            },
            "terminal_descent": {
                "r8": "u^2*R",
                "equation": "9*h*R'+6*h'*R=j",
                "positive_control": terminal_positive_control(),
            },
            "spectral_identity": spectral_identity(),
            "scope": {
                "universal_fibre_components": "NOT_YET_CLASSIFIED",
                "Taylor_boundaries": "ALL_RETAINED_NOT_YET_RECONSTRUCTED",
                "polynomial_core_order1": "SEPARATE_NOT_CONSUMED",
                "frontier_empty": False,
                "JC2": "NOT_CLAIMED",
            },
        },
    }


def singular_source(compiled: dict[str, object], transverse: bool = False,
                    stratum: str = "universal") -> str:
    if transverse:
        names = compiled["transverse_ring_names"]
        tails = compiled["transverse_tails"]
    else:
        names = compiled["ring_names"]
        tails = compiled["tails"]

    fixed_mu_nu_zero = False
    if transverse and stratum != "universal":
        if stratum not in ("k1", "k1_mu0_nu0", "k0_mu0_nu0"):
            raise FibreFailure(f"unknown Singular stratum {stratum}")
        source_names = names
        target_names = [name for name in names if name != "k"]
        target_ring = M.Ring(target_names)
        kval = 0 if stratum == "k0_mu0_nu0" else 1
        images = [
            M.cscale(kval, target_ring.one) if name == "k"
            else target_ring.var(name)
            for name in source_names
        ]
        tails = {
            ell: substitute_coeff(value, images, target_ring)
            for ell, value in tails.items()
        }
        names = target_names
        fixed_mu_nu_zero = stratum.endswith("mu0_nu0")

    variables = names if fixed_mu_nu_zero else names + ["mu", "nu"]
    lines = [
        'LIB "primdec.lib";',
        f"ring R=0,({','.join(variables)}),dp;",
        "option(redSB);",
    ]
    for ell in range(1, 8):
        polynomial = M.coeff_string(tails[ell], names)
        if ell == 3 and not fixed_mu_nu_zero:
            polynomial += "-mu"
        elif ell == 6 and not fixed_mu_nu_zero:
            polynomial += "-nu"
        lines.append(f"poly r{ell}={polynomial};")
    lines.extend([
        "ideal I=r1,r2,r3,r4,r5,r6,r7;",
        "ideal G=std(I);",
        f'print("PASS-SINGULAR-(9,12)-ORDER3-FIBRE-{stratum}");',
        'print("groebner_size="+string(size(G)));',
        'print("universal_dimension="+string(dim(G)));',
        'print("universal_degree="+string(mult(G)));',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--singular", action="store_true")
    parser.add_argument("--singular-transverse", action="store_true")
    parser.add_argument(
        "--singular-stratum",
        choices=("universal", "k1", "k1_mu0_nu0", "k0_mu0_nu0"),
        default="universal",
    )
    args = parser.parse_args()
    inputs = pin_inputs()
    compiled = compile_fibre()
    if args.singular or args.singular_transverse:
        print(singular_source(
            compiled,
            transverse=args.singular_transverse,
            stratum=args.singular_stratum,
        ), end="")
        return

    payload = {"input_hashes": inputs, **compiled["payload"]}
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-MAX12-(9,12)-ORDER3-FIBRE-COMPILER")
    print("constant_rows=r1=r2=r4=r5=r7=0;r3=mu;r6=nu")
    print("terminal=9*h*R'+6*h'*R=j")
    print("terminal_positive_control_constant=-3*C")
    print("components=NOT_YET_CLASSIFIED")
    print(f"payload_sha256={sha256(canonical.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
