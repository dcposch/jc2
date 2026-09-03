#!/usr/bin/env python3
"""Exact first-band common-jet edge for Moh's reduced (16,12) control.

This driver is intentionally confined to the D2(delta=-1) -> D1(delta=1/4)
edge on Moh pp.207--209.  It does not run the (90,60) or D=108 cases and it
does not assert existence of a global Jacobian pair.

The p.208 formula for alpha_3 is used literally: c5*A + c5*B + c7.  In
particular, this file does not silently replace the second c5 by c6.
"""

from __future__ import annotations

import json
import resource
import signal
import time

import sympy as sp


TIME_CAP_SECONDS = 600
MEMORY_CAP_BYTES = 2 * 1024**3
VARIABLE_CAP = 30


def impose_memory_cap() -> None:
    """Impose the lane's 2 GiB address-space cap when the host supports it."""
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    new_soft = MEMORY_CAP_BYTES if soft < 0 else min(soft, MEMORY_CAP_BYTES)
    new_hard = hard
    if hard < 0 or hard >= MEMORY_CAP_BYTES:
        new_hard = MEMORY_CAP_BYTES
    resource.setrlimit(resource.RLIMIT_AS, (new_soft, new_hard))


def bounded_elimination(label, variable_count, thunk):
    """Run one exact elimination with the declared time/space bounds."""
    if variable_count > VARIABLE_CAP:
        raise RuntimeError(f"{label}: variable cap exceeded: {variable_count}")

    def alarm_handler(_signum, _frame):
        raise TimeoutError(f"{label}: exceeded {TIME_CAP_SECONDS} seconds")

    old_handler = signal.signal(signal.SIGALRM, alarm_handler)
    before = time.monotonic()
    signal.alarm(TIME_CAP_SECONDS)
    try:
        value = thunk()
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)
    elapsed = time.monotonic() - before
    max_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(
        "ELIMINATION_RESOURCE",
        json.dumps(
            {
                "label": label,
                "variables": variable_count,
                "wall_seconds": round(elapsed, 6),
                "max_rss_kib_process": max_rss_kib,
                "time_cap_seconds": TIME_CAP_SECONDS,
                "address_space_cap_bytes": MEMORY_CAP_BYTES,
            },
            sort_keys=True,
        ),
    )
    return value


def laurent_coeff(expr, uniformizer, exponent):
    return sp.expand(expr).coeff(uniformizer, exponent)


def laurent_valuation(expr, uniformizer):
    expanded = sp.expand(expr)
    if expanded == 0:
        return sp.oo
    return min(term.as_powers_dict().get(uniformizer, 0) for term in sp.Add.make_args(expanded))


def reduce_mod(expr, generator, modulus):
    num, den = sp.together(expr).as_numer_denom()
    rem = sp.rem(sp.Poly(num, generator), sp.Poly(modulus, generator)).as_expr()
    return sp.factor(rem / den)


def assert_zero(label, expr):
    value = sp.factor(expr)
    if value != 0:
        raise AssertionError(f"{label}: {value}")
    print("PASS", label)


def formula35_from_parent(parent_expr, lead_u, multiplicity, parent_var, child_var, u):
    """Formula (3.5), B=0, after u=t^(1/4), E=5."""
    edge_gap_u = 5
    target = multiplicity * edge_gap_u
    answer = 0
    samples = []
    for derivative_order in range(multiplicity + 1):
        offset = target - derivative_order * edge_gap_u
        if offset < 0:
            continue
        jet_polynomial = laurent_coeff(parent_expr, u, lead_u + offset)
        sample = sp.factor(
            sp.diff(jet_polynomial, parent_var, derivative_order).subs(parent_var, 0)
            / sp.factorial(derivative_order)
        )
        if sample != 0:
            samples.append(
                {
                    "rho_t": str(sp.Rational(offset, 4)),
                    "derivative_order": derivative_order,
                    "sample": str(sample),
                }
            )
            answer += sample * child_var**derivative_order
    return sp.expand(answer), samples


def main() -> None:
    impose_memory_cap()

    # Source ring.  Moh p.208 literally repeats c5 in alpha_3 and has no c6.
    x, y, u = sp.symbols("x y u")
    X, Pmaj, Pbar = sp.symbols("X P_M P_bar")
    a0, a1p, a2p = sp.symbols("a0 a1_prefix a2_prefix")
    b1, b2, b3, b4 = sp.symbols("b1 b2 b3 b4")
    alpha1 = sp.symbols("alpha1")
    c1, c2, c3, c4, c5 = sp.symbols("c1 c2 c3 c4 c5")
    c7, c8, c9, c10, c11, c12, c13 = sp.symbols(
        "c7 c8 c9 c10 c11 c12 c13"
    )
    source_coefficients = (
        b1,
        b2,
        b3,
        b4,
        alpha1,
        c1,
        c2,
        c3,
        c4,
        c5,
        c7,
        c8,
        c9,
        c10,
        c11,
        c12,
        c13,
    )
    assert len(source_coefficients) == 17

    h = sp.expand(y**3 * (y - x) + b1 * y**3 + b2 * y**2 + b3 * y + b4)
    A = sp.expand((h - b4) / y)
    B = sp.expand((h - b3 * y - b4) / y**2)
    assert_zero("A is polynomial and h=y*A+b4", h - (y * A + b4))
    assert_zero("B is polynomial and h=y^2*B+b3*y+b4", h - (y**2 * B + b3 * y + b4))

    alpha2 = c1 * A + c2
    beta2 = c3 * A + c4
    alpha3 = c5 * A + c5 * B + c7
    beta3 = c8 * A + c9 * B + c10
    alpha4 = c11 * A + c12 * B + c13 * (y - x)
    bar_g = sp.expand(h**4 + alpha1 * h**3 + alpha2 * h**2 + alpha3 * h + alpha4)
    bar_f = sp.expand(h**3 + beta2 * h + beta3)

    print("SOURCE_LITERAL alpha3 = c5*A + c5*B + c7; c6 is absent")
    print(
        "SOURCE_RING",
        "S=QQ[" + ",".join(str(v) for v in source_coefficients + (x, y)) + "]",
    )
    print("SOURCE_GENERATOR_ORDER", [str(v) for v in source_coefficients + (x, y)])
    parent_target_generators = source_coefficients + (X, u)
    major_target_generators = source_coefficients + (Pmaj, u)
    minor_target_generators = source_coefficients + (a0, a1p, a2p, Pbar, u)
    print(
        "TARGET_RING_PARENT",
        "R2=QQ[" + ",".join(map(str, source_coefficients + (X,))) + "][u,u^-1]",
    )
    print("TARGET_GENERATOR_ORDER_PARENT", [str(v) for v in parent_target_generators])
    print(
        "TARGET_RING_MAJOR",
        "RM=QQ[" + ",".join(map(str, source_coefficients + (Pmaj,))) + "][u,u^-1]",
    )
    print("TARGET_GENERATOR_ORDER_MAJOR", [str(v) for v in major_target_generators])
    print(
        "TARGET_RING_COMPATIBLE_MINOR",
        "Rbar=QQ["
        + ",".join(map(str, source_coefficients + (a0, a1p, a2p, Pbar)))
        + "][u,u^-1]",
    )
    print("TARGET_GENERATOR_ORDER_COMPATIBLE_MINOR", [str(v) for v in minor_target_generators])
    print("RAMIFICATION u=t^(1/4); t=u^4; edge gap E=4*(1/4-(-1))=5")
    print("MAP_PARENT phi_2: x->u^-4, y->X*u^-4")
    print("MAP_MAJOR phi_M: x->u^-4, y->P_M*u")
    print(
        "MAP_COMPATIBLE_MINOR phi_bar: x->u^-4, "
        "y->u^-4+a0+a1_prefix*u^4+a2_prefix*u^8+P_bar*u^11"
    )
    print("MAP_COEFFICIENTS all source coefficient generators map identically")

    parent_sub = {**{v: v for v in source_coefficients}, x: u**-4, y: X * u**-4}
    major_sub = {**{v: v for v in source_coefficients}, x: u**-4, y: Pmaj * u}
    minor_sub = {
        **{v: v for v in source_coefficients},
        x: u**-4,
        y: u**-4 + a0 + a1p * u**4 + a2p * u**8 + Pbar * u**11,
    }
    if parent_sub[x] != u**-4 or parent_sub[y] != X * u**-4:
        raise AssertionError("parent generator-image map mismatch")
    if major_sub[x] != u**-4 or major_sub[y] != Pmaj * u:
        raise AssertionError("major generator-image map mismatch")
    expected_minor_y = u**-4 + a0 + a1p * u**4 + a2p * u**8 + Pbar * u**11
    if minor_sub[x] != u**-4 or sp.expand(minor_sub[y] - expected_minor_y) != 0:
        raise AssertionError("compatible-minor generator-image map mismatch")
    if any(parent_sub[v] != v or major_sub[v] != v or minor_sub[v] != v for v in source_coefficients):
        raise AssertionError("coefficient generator-image map mismatch")
    print("PASS all declared source-generator images equal implemented substitutions")
    h_parent = sp.expand(h.subs(parent_sub))
    g_parent = sp.expand(bar_g.subs(parent_sub))
    f_parent = sp.expand(bar_f.subs(parent_sub))
    h_major = sp.expand(h.subs(major_sub))
    g_major = sp.expand(bar_g.subs(major_sub))
    f_major = sp.expand(bar_f.subs(major_sub))

    parent_h0 = laurent_coeff(h_parent, u, -16)
    assert_zero("parent h initial K0=X^3(X-1)", parent_h0 - X**3 * (X - 1))
    assert_zero("typed parent p2 gives g initial p2^4", laurent_coeff(g_parent, u, -64) - parent_h0**4)
    assert_zero("typed parent p2 gives f initial p2^3", laurent_coeff(f_parent, u, -48) - parent_h0**3)
    h_cofactor = sp.cancel(parent_h0 / X**3).subs(X, 0)
    assert h_cofactor == -1
    print("PARENT_FACTOR_TYPED p2=in_phi2(h)=X^3*(X-1); C=0; u_factor=3; d2=gcd(16,12)=4; hC=-1")

    h_edge, h_samples = formula35_from_parent(h_parent, -16, 3, X, Pmaj, u)
    g_edge, g_samples = formula35_from_parent(g_parent, -64, 12, X, Pmaj, u)
    f_edge, f_samples = formula35_from_parent(f_parent, -48, 9, X, Pmaj, u)
    h_direct = laurent_coeff(h_major, u, -1)
    g_direct = laurent_coeff(g_major, u, -4)
    f_direct = laurent_coeff(f_major, u, -3)
    assert_zero("formula(3.5) h edge equals direct major initial", h_edge - h_direct)
    assert_zero("formula(3.5) g edge equals direct major initial", g_edge - g_direct)
    assert_zero("formula(3.5) f edge equals direct major initial", f_edge - f_direct)
    assert_zero("major h initial", h_edge + Pmaj**3)
    assert_zero(
        "major g initial",
        g_edge - (Pmaj**12 - c1 * Pmaj**8 + c5 * Pmaj**4 - c13),
    )
    assert_zero(
        "major f initial",
        f_edge - (-Pmaj**9 + c3 * Pmaj**5 - c9 * Pmaj),
    )
    print("JET_SAMPLES_H", json.dumps(h_samples, sort_keys=True))
    print("JET_SAMPLES_G", json.dumps(g_samples, sort_keys=True))
    print("JET_SAMPLES_F", json.dumps(f_samples, sort_keys=True))
    print("EDGE_INITIAL_H", h_edge)
    print("EDGE_INITIAL_G", g_edge)
    print("EDGE_INITIAL_F_RAW", f_edge)
    print("ACTIVE_COMMON_JET_VARIABLES", ["c1", "c3", "c5", "c9", "c13"])
    print("ACTIVE_COMMON_JET_VARIABLE_COUNT", 5)
    print("SHARED_LOWER_WITNESS coeff(P_M^8, G_child)=-c1=jet(G,rho=5,k=8)")

    # Compatible minor chart: a coherent second restriction, not a claim that
    # a minor factor carries another recursive child ODE.
    h_bar = sp.expand(h.subs(minor_sub))
    tail_exponents = (-12, -8, -4)
    tail_equations = [laurent_coeff(h_bar, u, exponent) for exponent in tail_exponents]
    tail_solution = {a0: -b1, a1p: -b2, a2p: -b1 * b2 - b3}
    for exponent, equation in zip(tail_exponents, tail_equations):
        assert_zero(f"compatible-minor cancellation u^{exponent}", equation.subs(tail_solution))
    h_bar_reduced = sp.expand(h_bar.subs(tail_solution))
    assert_zero("compatible-minor h initial", laurent_coeff(h_bar_reduced, u, -1) - Pbar)
    H0 = b1**2 * b2 + 2 * b1 * b3 + b2**2 + b4
    assert_zero("compatible-minor next coefficient H0", laurent_coeff(h_bar_reduced, u, 0) - H0)

    # Avoid expanding the irrelevant full powers.  The exact component
    # valuations prove that only h^4 and h^3 can reach weights -4 and -3.
    A_bar = sp.expand(A.subs(minor_sub).subs(tail_solution))
    B_bar = sp.expand(B.subs(minor_sub).subs(tail_solution))
    ymx_bar = sp.expand((y - x).subs(minor_sub).subs(tail_solution))
    component_valuations = {
        "h": laurent_valuation(h_bar_reduced, u),
        "A": laurent_valuation(A_bar, u),
        "B": laurent_valuation(B_bar, u),
        "y-x": laurent_valuation(ymx_bar, u),
    }
    if component_valuations != {"h": -1, "A": 3, "B": 4, "y-x": 0}:
        raise AssertionError(f"minor component valuations: {component_valuations}")
    g_bar_initial = Pbar**4
    f_bar_initial = Pbar**3
    print("PASS compatible-minor component valuations force g initial=h^4")
    print("PASS compatible-minor component valuations force f initial=h^3")
    print(
        "COMPATIBLE_MINOR_TAIL_MAP",
        "a0=-b1; a1_prefix=-b2; a2_prefix=-b1*b2-b3",
    )
    print("COMPATIBLE_MINOR_NEXT_COEFF H0=", H0)
    print("COMPATIBLE_MINOR_COMPONENT_VALUATIONS", component_valuations)
    print("COMPATIBLE_MINOR_INITIALS", {"h": str(Pbar), "g": str(Pbar**4), "f": str(Pbar**3)})

    # Raw leading-unit powers.  This is the bottom specialization (3.8).
    assert_zero("(3.8) g raw leader hC^(16/4)", sp.LC(sp.Poly(g_edge, Pmaj)) - h_cofactor**4)
    assert_zero("(3.8) f raw leader hC^(12/4)", sp.LC(sp.Poly(f_edge, Pmaj)) - h_cofactor**3)
    print(
        "LEADER_RECIPE_3_7 GENERAL_OUTER_POWER_LEMMA_ONLY; "
        "NOT_APPLICABLE to this bottom endpoint"
    )
    print("LEADER_RECIPE_3_8 lc(g_child)=(-1)^4=1; lc(f_child)=(-1)^3=-1")

    # Uniformizer action.  zeta is primitive: coefficient field Q[zeta]/(zeta^2+1).
    zeta = sp.symbols("zeta")
    cyclo4 = zeta**2 + 1
    assert_zero(
        "action major g character 1",
        reduce_mod(g_edge.subs(Pmaj, zeta * Pmaj) - g_edge, zeta, cyclo4),
    )
    assert_zero(
        "action major f character zeta",
        reduce_mod(f_edge.subs(Pmaj, zeta * Pmaj) - zeta * f_edge, zeta, cyclo4),
    )
    assert_zero(
        "action compatible-minor g character 1",
        reduce_mod(g_bar_initial.subs(Pbar, zeta**3 * Pbar) - g_bar_initial, zeta, cyclo4),
    )
    assert_zero(
        "action compatible-minor f character zeta",
        reduce_mod(f_bar_initial.subs(Pbar, zeta**3 * Pbar) - zeta * f_bar_initial, zeta, cyclo4),
    )
    print("ACTION_FIELD K=QQ[zeta]/(zeta^2+1), zeta primitive fourth root")
    print("ACTION_CONVENTION covariant u->zeta*u; coefficient symbols fixed")
    print("ACTION_MATRIX_CHART [[zeta,0],[0,zeta^3]] on column(P_M,P_bar)")
    print("ACTION_MATRIX_INITIALS diag(1,zeta,1,zeta) on column(g_M,f_M,g_bar,f_bar)")
    print("ACTION_PASSIVE inverse matrices if the physical series is held fixed")

    # Compare, before any elimination, with charged report (5.2).
    svar, rho, z = sp.symbols("s rho z")
    monic_f_edge = -f_edge
    G = z**3 - c1 * z**2 + c5 * z - c13
    F = z**2 - c3 * z + c9
    family_map = {
        c1: -svar,
        c3: -sp.Rational(3, 4) * svar,
        c5: svar**2 * (sp.Rational(3, 8) - rho / 24),
        c9: svar**2 * (6 - rho) / 32,
        c13: -svar**3 * (4 - rho) / 96,
    }
    charged_G = z**3 + svar * z**2 + svar**2 * (sp.Rational(3, 8) - rho / 24) * z + svar**3 * (4 - rho) / 96
    charged_F = z**2 + sp.Rational(3, 4) * svar * z + svar**2 * (6 - rho) / 32
    assert_zero("pre-elimination charged G(z) comparison", G.subs(family_map) - charged_G)
    assert_zero("pre-elimination charged F(z) comparison", F.subs(family_map) - charged_F)
    assert_zero("cyclic lift g=G(P_M^4)", g_edge - G.subs(z, Pmaj**4))
    assert_zero("cyclic lift monic f=P_M*F(P_M^4)", monic_f_edge - Pmaj * F.subs(z, Pmaj**4))
    print("PRE_ELIMINATION_COMPARE PASS charged report (5.2), rho^2=6, s!=0")
    print("PRE_ELIMINATION_FAMILY_MAP", {str(k): str(v) for k, v in family_map.items()})
    charged_invariants = {
        "Disc(G)": sp.factor(sp.discriminant(charged_G, z)),
        "Disc(F)": sp.factor(sp.discriminant(charged_F, z)),
        "Res(G,F)": sp.factor(sp.resultant(charged_G, charged_F, z)),
    }
    for label, invariant in charged_invariants.items():
        reduced = reduce_mod(invariant, rho, rho**2 - 6)
        if reduced == 0:
            raise AssertionError(f"charged invariant vanished modulo rho^2-6: {label}")
        print("PASS charged open-locus invariant nonzero", label, "=", invariant)

    # Exact bottom ODE in the monic normalization used by the charged family.
    kappa, T = sp.symbols("kappa T")
    D = sp.expand(4 * g_edge * sp.diff(monic_f_edge, Pmaj) - 3 * monic_f_edge * sp.diff(g_edge, Pmaj))
    Dpoly = sp.Poly(D, Pmaj)
    ode_equations = []
    for (degree,), coefficient in zip(Dpoly.monoms(), Dpoly.coeffs()):
        if degree == 0:
            ode_equations.append(sp.expand(coefficient - kappa))
        else:
            ode_equations.append(sp.expand(coefficient))
    expected_ode = [
        3 * c1 - 4 * c3,
        c1 * c3 - 6 * c5 + 8 * c9,
        5 * c1 * c9 - 9 * c13 - 2 * c3 * c5,
        5 * c13 * c3 - 2 * c5 * c9,
        kappa + 4 * c13 * c9,
    ]
    # Coefficients differ from expected_ode only by nonzero rational units.
    for equation in expected_ode:
        rem = sp.groebner(ode_equations, c13, c9, c5, c3, kappa, c1).reduce(equation)[1]
        assert_zero("ODE expected generator is in coefficient ideal", rem)

    kappa_family = -sp.Rational(5, 384) * svar**5 * (rho - 3)
    for equation in expected_ode:
        check = reduce_mod(equation.subs(family_map).subs(kappa, kappa_family), rho, rho**2 - 6)
        assert_zero("charged family satisfies bottom ODE modulo rho^2-6", check)
    assert_zero(
        "charged kappa agrees with constant Wronskian",
        reduce_mod((Dpoly.coeff_monomial(1).subs(family_map) - kappa_family), rho, rho**2 - 6),
    )

    # Elimination 1: the compatible-minor triangular cancellation map.
    tail_generators = (a2p, a1p, a0, b3, b2, b1)
    print("TAIL_ELIM_RING QQ[" + ",".join(map(str, tail_generators)) + "] order=lex")
    tail_gb = bounded_elimination(
        "compatible_minor_tail",
        len(tail_generators),
        lambda: sp.groebner(tail_equations, *tail_generators, order="lex"),
    )
    tail_basis = [sp.factor(poly.as_expr()) for poly in tail_gb.polys]
    expected_tail_basis = [a2p + b1 * b2 + b3, a1p + b2, a0 + b1]
    if tail_basis != expected_tail_basis:
        raise AssertionError(f"tail basis mismatch: {tail_basis}")
    print("TAIL_ELIM_BASIS", [str(value) for value in tail_basis])

    # Elimination 2: local bottom ODE, localized at kappa*c1 != 0.
    ode_generators = (T, c13, c9, c5, c3, kappa, c1)
    saturation_equation = T * kappa * c1 - 1
    print("ODE_ELIM_RING QQ[" + ",".join(map(str, ode_generators)) + "] order=lex")
    print("ODE_LOCALIZATION Rabinowitsch T*kappa*c1-1; kappa is bottom openness, c1 selects s!=0 chart")
    ode_gb = bounded_elimination(
        "bottom_ode_saturated_chart",
        len(ode_generators),
        lambda: sp.groebner(expected_ode + [saturation_equation], *ode_generators, order="lex"),
    )
    if list(ode_gb) == [1]:
        raise AssertionError("positive local-family control unexpectedly empty")
    print("ODE_POSITIVE_CONTROL NONUNIT basis_size=", len(ode_gb.polys))
    print("ODE_ELIM_BASIS", [str(sp.factor(poly.as_expr())) for poly in ode_gb.polys])

    negative_kappa = bounded_elimination(
        "negative_kappa_zero",
        len(ode_generators),
        lambda: sp.groebner(expected_ode + [saturation_equation, kappa], *ode_generators, order="lex"),
    )
    if list(negative_kappa) != [1]:
        raise AssertionError("negative kappa=0 control should be the unit ideal")
    print("ODE_NEGATIVE_CONTROL_KAPPA_ZERO UNIT (localization-wiring control)")

    negative_scale = bounded_elimination(
        "negative_scale_zero",
        len(ode_generators),
        lambda: sp.groebner(expected_ode + [saturation_equation, c1], *ode_generators, order="lex"),
    )
    if list(negative_scale) != [1]:
        raise AssertionError("negative c1=0 chart control should be the unit ideal")
    print("ODE_NEGATIVE_CONTROL_C1_ZERO UNIT (selected-chart localization-wiring control)")

    # Elimination 3: name the quadratic branch by rho; localization at c1.
    Tr = sp.symbols("T_rho")
    rho_generators = (Tr, c5, c1, rho)
    quadratic = 25 * c1**4 - 144 * c1**2 * c5 + 192 * c5**2
    rho_definition = rho * c1**2 - 9 * c1**2 + 24 * c5
    print("RHO_ELIM_RING QQ[" + ",".join(map(str, rho_generators)) + "] order=lex")
    rho_gb = bounded_elimination(
        "recover_rho_branch",
        len(rho_generators),
        lambda: sp.groebner(
            [quadratic, rho_definition, Tr * c1 - 1],
            *rho_generators,
            order="lex",
        ),
    )
    rho_basis = [sp.factor(poly.as_expr()) for poly in rho_gb.polys]
    if rho**2 - 6 not in rho_basis:
        raise AssertionError(f"rho^2-6 not recovered: {rho_basis}")
    print("RHO_ELIM_BASIS", [str(value) for value in rho_basis])
    print("RHO_BRANCH_RECOVERED rho^2-6=0")

    print(
        "VARIABLE_COUNTS",
        json.dumps(
            {
                "source_literal_coefficients": 17,
                "active_D2_D1_common_jet_variables": 5,
                "tail_elimination_variables": len(tail_generators),
                "ode_elimination_variables": len(ode_generators),
                "rho_elimination_variables": len(rho_generators),
                "largest_elimination_variables": max(
                    len(tail_generators), len(ode_generators), len(rho_generators)
                ),
                "cap": VARIABLE_CAP,
            },
            sort_keys=True,
        ),
    )
    print(
        "READINESS first-band kernel exposes parent_expr/lead/multiplicity; "
        "a new edge must also supply its ramification, gap, prefix B, and approximate roots; "
        "no 90/60 or D=108 run performed"
    )
    print("ALL_JET_EDGE_1612_CHECKS_PASSED")


if __name__ == "__main__":
    main()
