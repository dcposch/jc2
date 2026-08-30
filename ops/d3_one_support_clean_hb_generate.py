#!/usr/bin/env python3
"""Generate the clean-infinity twisted-cubic jet ideal for the fixed P18 chart.

The generated Singular input is a *screening* computation.  It works on the
open chart where the second localized Hilbert--Burch coordinate has a
nonzero z-derivative, and asks whether the inverse image of the twisted cubic
has local length at least ``--jet-order`` at the prescribed infinity point.

Heavy invocations belong on AWS.  ``--self-test`` deliberately avoids the
interior jet expansion and is suitable for a small deterministic replay.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass

import sympy as sp


def require(condition: bool, message: str) -> None:
    """Optimization-safe invariant check."""
    if not condition:
        raise RuntimeError(message)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def singular_text(expr: sp.Expr) -> str:
    """Render an integral SymPy polynomial in Singular syntax."""
    expr = sp.expand(expr)
    require(sp.denom(expr) == 1, "unexpected symbolic denominator")
    return sp.sstr(expr, order="lex").replace("**", "^")


def integer_is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


@dataclass(frozen=True)
class Chart:
    t: sp.Symbol
    x: sp.Symbol
    y: sp.Symbol
    z: sp.Symbol
    tau: sp.Symbol
    kappa: sp.Symbol
    d1: sp.Symbol
    d2: sp.Symbol
    h: sp.Symbol
    pv: sp.Symbol
    qv: sp.Symbol
    rv: sp.Symbol
    boundary: sp.Expr
    coefficients: tuple[sp.Expr, ...]
    basis: tuple[sp.Expr, ...]
    cubic: sp.Expr


def build_chart(*, mutate_boundary_lift: bool = False) -> Chart:
    t, x, y, z = sp.symbols("t x y z")
    tau, kappa, d1, d2 = sp.symbols("tau kappa d1 d2")
    h, pv, qv, rv = sp.symbols("h pv qv rv")
    ell = y - x

    factors = tuple(
        (t - tau) * x + (kappa + delta * (t - tau)) * ell
        for delta in (d1, d2, sp.Integer(1))
    )
    boundary = sp.expand(sp.prod(factors))
    boundary_poly = sp.Poly(boundary, t, x, y)

    def coefficient(t_degree: int, x_degree: int, y_degree: int) -> sp.Expr:
        return boundary_poly.coeff_monomial(
            t**t_degree * x**x_degree * y**y_degree
        )

    a: list[sp.Expr] = [sp.Integer(0)] * 19
    a[0] = coefficient(0, 0, 3)
    a[1] = coefficient(0, 1, 2)
    a[2] = coefficient(1, 0, 3)
    a[3] = coefficient(1, 1, 2)
    a[4] = coefficient(0, 2, 1)
    a[5] = pv
    a[6] = coefficient(2, 0, 3)
    a[7] = h
    a[8] = coefficient(2, 1, 2)
    a[9] = coefficient(2, 2, 1)
    a[10] = coefficient(0, 3, 0)
    a[11] = h - coefficient(1, 2, 1)
    if mutate_boundary_lift:
        # Negative control: reverse the sole B7-B11 cancellation.
        a[11] = h + coefficient(1, 2, 1)
    a[12] = qv
    a[13] = coefficient(3, 0, 3)
    a[14] = coefficient(1, 3, 0)
    a[15] = rv
    a[16] = coefficient(3, 1, 2)
    a[17] = coefficient(2, 3, 0)
    a[18] = coefficient(3, 2, 1)

    basis = (
        y**3,
        t * y**2 * z + x * y**2,
        t * y**3,
        t * x * y**2,
        t**2 * y * z**2 + 2 * t * x * y * z + x**2 * y,
        t**2 * y**2 * z,
        t**2 * y**3,
        t**2 * x * y * z + t * x**2 * y,
        t**2 * x * y**2,
        t**2 * x**2 * y,
        t**3 * z**3 + 3 * t**2 * x * z**2 + 3 * t * x**2 * z + x**3,
        t**3 * y * z**2 - t * x**2 * y,
        t**3 * y**2 * z,
        t**3 * y**3,
        t**3 * x * z**2 + 2 * t**2 * x**2 * z + t * x**3,
        t**3 * x * y * z,
        t**3 * x * y**2,
        t**3 * x**2 * z + t**2 * x**3,
        t**3 * x**2 * y,
    )
    cubic = sp.expand(sum(value * vector for value, vector in zip(a, basis)))

    # These checks are small enough for the replay and protect the unique
    # four-dimensional lift of the prescribed boundary polynomial.
    require(len(basis) == 19, "P18 basis cardinality drift")
    require(
        sp.expand(cubic.subs(z, 0) - boundary) == 0,
        "P18 boundary lift mismatch",
    )
    require(
        sp.expand(cubic.subs({x: -t, y: 0, z: 1})) == 0,
        "moving-section equation failed",
    )

    return Chart(
        t=t,
        x=x,
        y=y,
        z=z,
        tau=tau,
        kappa=kappa,
        d1=d1,
        d2=d2,
        h=h,
        pv=pv,
        qv=qv,
        rv=rv,
        boundary=boundary,
        coefficients=tuple(sp.expand(value) for value in a),
        basis=basis,
        cubic=cubic,
    )


def boundary_discriminant_formula(chart: Chart) -> sp.Expr:
    expected = (
        chart.kappa**6
        * (chart.d1 - chart.d2) ** 2
        * (chart.d1 - 1) ** 2
        * (chart.d2 - 1) ** 2
        * (chart.x - chart.y) ** 12
    )
    observed = sp.factor(sp.discriminant(chart.boundary, chart.t))
    require(sp.expand(observed - expected) == 0, "boundary discriminant drift")
    return sp.expand(expected)


def self_test(*, mutate_boundary_lift: bool) -> None:
    chart = build_chart(mutate_boundary_lift=mutate_boundary_lift)
    discriminant = boundary_discriminant_formula(chart)

    c0, c1, c2, c3 = sp.symbols("c0 c1 c2 c3")
    h0 = c1**2 - 3 * c0 * c2
    h1 = c1 * c2 - 9 * c0 * c3
    h2 = c2**2 - 3 * c1 * c3
    syzygy_0 = sp.expand(3 * c0 * h2 - c1 * h1 + c2 * h0)
    syzygy_1 = sp.expand(c1 * h2 - c2 * h1 + 3 * c3 * h0)
    localized_u = -h2
    localized_v = sp.expand(-3 * c3 * h1 + 2 * c2 * h2)
    require(syzygy_0 == 0 and syzygy_1 == 0, "Hilbert--Burch syzygy drift")
    require(
        localized_v
        == sp.expand(27 * c0 * c3**2 - 9 * c1 * c2 * c3 + 2 * c2**3),
        "localized Hilbert--Burch coordinate drift",
    )

    Y = sp.symbols("Y")

    def vanishes_below(poly: sp.Expr, order: int) -> bool:
        candidate = sp.Poly(poly, Y)
        return all(candidate.coeff_monomial(Y**degree) == 0 for degree in range(order))

    require(vanishes_below(Y**27, 27), "length-27 positive control failed")
    require(not vanishes_below(Y**26, 27), "length-26 mutation was accepted")

    payload = {
        "boundary_discriminant_sha256": sha256_text(sp.sstr(discriminant, order="lex")),
        "boundary_sha256": sha256_text(sp.sstr(chart.boundary, order="lex")),
        "coefficient_vector_sha256": sha256_text(
            "\n".join(sp.sstr(value, order="lex") for value in chart.coefficients)
        ),
        "hb_local_u": singular_text(localized_u),
        "hb_local_v": singular_text(localized_v),
        "hb_syzygies": True,
        "jet_positive_control_order": 27,
        "jet_truncation_mutation_rejected": True,
        "moving_section": True,
        "p18_boundary_lift": True,
        "schema": "D3_ONE_SUPPORT_CLEAN_HB_SELFTEST_V1",
    }
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))


def polynomial_in_yz(expr: sp.Expr, Y: sp.Symbol, Z: sp.Symbol) -> dict[tuple[int, int], sp.Expr]:
    poly = sp.Poly(sp.expand(expr), Y, Z)
    result: dict[tuple[int, int], sp.Expr] = {}
    for powers, coefficient in poly.terms():
        result[(powers[0], powers[1])] = sp.expand(coefficient)
    return result


def truncated_product(
    left: list[sp.Expr], right: list[sp.Expr], maximum: int
) -> list[sp.Expr]:
    answer: list[sp.Expr] = [sp.Integer(0)] * (maximum + 1)
    for i, left_value in enumerate(left):
        if left_value == 0:
            continue
        upper = min(maximum - i, len(right) - 1)
        for j in range(upper + 1):
            right_value = right[j]
            if right_value != 0:
                answer[i + j] += left_value * right_value
    return [sp.expand(value) for value in answer]


def compose_z_series(
    terms: dict[tuple[int, int], sp.Expr],
    z_coefficients: tuple[sp.Symbol, ...],
    maximum: int,
) -> list[sp.Expr]:
    z_series = [sp.Integer(0)] * (maximum + 1)
    for index, symbol in enumerate(z_coefficients, start=1):
        z_series[index] = symbol
    largest_z_power = max((z_power for _, z_power in terms), default=0)
    powers: list[list[sp.Expr]] = [[sp.Integer(0)] * (maximum + 1)]
    powers[0][0] = sp.Integer(1)
    for _ in range(largest_z_power):
        powers.append(truncated_product(powers[-1], z_series, maximum))

    coefficients: list[sp.Expr] = [sp.Integer(0)] * (maximum + 1)
    for (y_power, z_power), scalar in terms.items():
        if y_power > maximum:
            continue
        for series_degree in range(maximum - y_power + 1):
            value = powers[z_power][series_degree]
            if value != 0:
                coefficients[y_power + series_degree] += scalar * value
    return [sp.expand(value) for value in coefficients]


def generate_singular(*, jet_order: int, prime: int, engine: str) -> None:
    chart = build_chart()
    boundary_discriminant_formula(chart)
    Y, Z = sp.symbols("Y Z")

    local_cubic = sp.Poly(
        sp.expand(chart.cubic.subs({chart.x: 1, chart.y: 1 + Y, chart.z: Z})),
        chart.t,
    )
    c = tuple(
        sp.expand(local_cubic.coeff_monomial(chart.t**degree)) for degree in range(4)
    )
    c0, c1, c2, c3 = c

    h0 = sp.expand(c1**2 - 3 * c0 * c2)
    h1 = sp.expand(c1 * c2 - 9 * c0 * c3)
    h2 = sp.expand(c2**2 - 3 * c1 * c3)
    require(
        sp.expand(3 * c0 * h2 - c1 * h1 + c2 * h0) == 0,
        "first pulled-back Hilbert--Burch syzygy failed",
    )
    require(
        sp.expand(c1 * h2 - c2 * h1 + 3 * c3 * h0) == 0,
        "second pulled-back Hilbert--Burch syzygy failed",
    )

    # On c3 != 0 these generate the same local ideal as all three twisted-
    # cubic minors.  The combination V removes the order-four multiple of U
    # along the three tangent boundary sections.
    U = sp.expand(-h2)
    V = sp.expand(-3 * c3 * h1 + 2 * c2 * h2)
    require(
        V == sp.expand(27 * c0 * c3**2 - 9 * c1 * c2 * c3 + 2 * c2**3),
        "localized V identity failed",
    )
    point_substitution = {Y: 0, Z: 0}
    require(sp.expand(c3.subs(point_substitution) - 1) == 0, "c3 chart is not a unit")
    require(U.subs(point_substitution) == 0, "U does not vanish at the clean point")
    require(V.subs(point_substitution) == 0, "V does not vanish at the clean point")

    infinity_u = sp.Poly(sp.expand(U.subs(Z, 0)), Y)
    infinity_v = sp.Poly(sp.expand(V.subs(Z, 0)), Y)
    require(
        all(infinity_u.coeff_monomial(Y**degree) == 0 for degree in range(4)),
        "boundary U has order below four",
    )
    require(
        all(infinity_v.coeff_monomial(Y**degree) == 0 for degree in range(6)),
        "boundary V has order below six",
    )
    require(infinity_u.coeff_monomial(Y**4) != 0, "generic boundary U order exceeds four")
    require(infinity_v.coeff_monomial(Y**6) != 0, "generic boundary V order exceeds six")

    uz = sp.expand(sp.diff(U, Z).subs(point_substitution))
    require(uz != 0, "U_Z is identically zero on the normalized slice")

    z_coefficients = sp.symbols(" ".join(f"z{degree}" for degree in range(1, jet_order)))
    if jet_order == 2:
        z_coefficients = (z_coefficients,) if isinstance(z_coefficients, sp.Symbol) else tuple(z_coefficients)
    else:
        z_coefficients = tuple(z_coefficients)
    maximum = jet_order - 1
    u_coefficients = compose_z_series(polynomial_in_yz(U, Y, Z), z_coefficients, maximum)
    v_coefficients = compose_z_series(polynomial_in_yz(V, Y, Z), z_coefficients, maximum)
    require(u_coefficients[0] == 0, "composed U constant term drift")
    require(v_coefficients[0] == 0, "composed V constant term drift")

    equations = tuple(u_coefficients[1:]) + tuple(v_coefficients[1:])
    require(len(equations) == 2 * (jet_order - 1), "jet equation count drift")
    open_factor = sp.expand(
        chart.kappa
        * (chart.d1 - chart.d2)
        * (chart.d1 - 1)
        * (chart.d2 - 1)
        * uz
    )

    variables = (
        chart.tau,
        chart.kappa,
        chart.d1,
        chart.d2,
        chart.h,
        chart.pv,
        chart.qv,
        chart.rv,
        *z_coefficients,
        sp.Symbol("oinv"),
    )
    equation_digest = sha256_text(
        "\n".join(sp.sstr(value, order="lex") for value in equations)
        + "\nOPEN="
        + sp.sstr(open_factor, order="lex")
    )

    print("// D3_ONE_SUPPORT_CLEAN_HB_SINGULAR_V1")
    print(f"// jet_order={jet_order}")
    print(f"// characteristic={prime}")
    print(f"// engine={engine}")
    print(f"// equation_sha256={equation_digest}")
    print(f"ring R={prime},({','.join(str(value) for value in variables)}),dp;")
    print("option(redSB);")
    rendered_equations = [singular_text(value) for value in equations]
    rendered_equations.append(f"oinv*({singular_text(open_factor)})-1")
    print("ideal J=" + ",\n".join(rendered_equations) + ";")
    print(f'print("D3_CLEAN_HB_INPUT_ORDER={jet_order}");')
    print(f'print("D3_CLEAN_HB_INPUT_CHARACTERISTIC={prime}");')
    print(f'print("D3_CLEAN_HB_INPUT_ENGINE={engine}");')
    print(f'print("D3_CLEAN_HB_EQUATION_SHA256={equation_digest}");')
    print("ideal CONTROL_UNIT=1;")
    print("ideal CONTROL_UNIT_G=std(CONTROL_UNIT);")
    print("if (reduce(1,CONTROL_UNIT_G)==0) { print(\"D3_CLEAN_HB_CONTROL_UNIT=PASS\"); }")
    print("else { print(\"D3_CLEAN_HB_CONTROL_UNIT=FAIL\"); quit; }")
    print("ideal CONTROL_PROPER=tau;")
    print("ideal CONTROL_PROPER_G=std(CONTROL_PROPER);")
    print("if (reduce(1,CONTROL_PROPER_G)!=0) { print(\"D3_CLEAN_HB_CONTROL_PROPER=PASS\"); }")
    print("else { print(\"D3_CLEAN_HB_CONTROL_PROPER=FAIL\"); quit; }")
    print(f"ideal G={engine}(J);")
    print("poly NF_ONE=reduce(1,G);")
    print("if (NF_ONE==0) { print(\"D3_CLEAN_HB_SCREEN=UNIT\"); }")
    print("else { print(\"D3_CLEAN_HB_SCREEN=NONUNIT\"); }")
    print('print("D3_CLEAN_HB_BASIS_SIZE="+string(size(G)));')
    print('print("D3_CLEAN_HB_BASIS_DIM="+string(dim(G)));')
    print("quit;")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jet-order", type=int, default=8)
    parser.add_argument("--prime", type=int, default=32003)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="slimgb")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--mutate-boundary-lift", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    require(2 <= args.jet_order <= 27, "jet order must lie in [2,27]")
    require(
        args.prime == 0 or (args.prime > 3 and integer_is_prime(args.prime)),
        "characteristic must be zero or a prime greater than three",
    )
    if args.self_test:
        self_test(mutate_boundary_lift=args.mutate_boundary_lift)
        return 0
    require(not args.mutate_boundary_lift, "mutation is available only with --self-test")
    generate_singular(jet_order=args.jet_order, prime=args.prime, engine=args.engine)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError) as error:
        print(f"D3_ONE_SUPPORT_CLEAN_HB_ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
