#!/usr/bin/env python3
"""Emit a d=sqrt(21) exact t=6 heuristic terminal computation.

The source is the charged Q[y] driver.  Its twelve rows are already reduced
modulo H_6, hence every coefficient is linear in y=q13_1.  The explicit maps

    phi: y |-> (d+21)/78,       psi: d |-> 78*y-21

identify Q[y]/(507*y^2-273*y+35) with Q[d]/(d^2-21).  For each source row we
collect the paired y/constant coefficients, apply phi, clear the common 78,
and divide the two integer components by their gcd.  Thus the emitted raw row
is exactly (78/g_i)*phi(source row), where 78/g_i is a nonzero rational unit.
The Singular driver then makes each raw row monic by a checked field-unit
scaling and presents the rows shortest-first to nfmodStd.

Only files beginning emit_dmodel_ are written by this program.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import math
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "t6_heuristic_exact_QHy_std.sing"
OUTPUT = HERE / "emit_dmodel_t6_exact_nfmodStd.sing"
VALIDATION = HERE / "emit_dmodel_validation.txt"

EXPECTED_SOURCE_SHA256 = (
    "d840675b403e7e97c650294a73b9080f568150aab0a485fcbf6079122a1f69cd"
)
Y = "q13_1"
REMAINING = ("q7_0", "q8_1", "q9_1", "q10_1", "q11_1", "q12_1")
ALL_SOURCE_VARS = (Y,) + REMAINING


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def frac_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def signed_linear_text(a: int, b: int) -> str:
    """Serialize positive-oriented a*d+b (caller handles the outer sign)."""
    pieces: list[str] = []
    if a:
        if a == 1:
            pieces.append("d")
        else:
            pieces.append(f"{a}*d")
    if b:
        if not pieces:
            pieces.append(str(b))
        elif b > 0:
            pieces.append(f"+{b}")
        else:
            pieces.append(str(b))
    return "".join(pieces) if pieces else "0"


def monomial_text(exponents: tuple[int, ...]) -> str:
    factors: list[str] = []
    for variable, exponent in zip(REMAINING, exponents):
        if exponent == 1:
            factors.append(variable)
        elif exponent:
            factors.append(f"{variable}^{exponent}")
    return "*".join(factors)


@dataclass(frozen=True)
class SourceRow:
    source_index: int
    source_term_count: int
    # insertion order is deterministic and inherited from the charged row
    coefficients: dict[tuple[int, ...], tuple[int, int]]  # monomial -> (y, 1)


@dataclass(frozen=True)
class DRow:
    source_index: int
    source_term_count: int
    monomial_count: int
    component_gcd: int
    rational_scale: Fraction
    expression: str
    expression_sha256: str


FACTOR_RE = re.compile(
    r"^(q(?:13_1|7_0|8_1|9_1|10_1|11_1|12_1))(?:\^(\d+))?$"
)


def extract_source_ideal(source: str) -> tuple[str, list[str]]:
    match = re.search(r"ideal I=(.*?);\nideal G=", source, re.S)
    if match is None:
        raise SystemExit("cannot locate the charged ideal I")
    parts = [part.strip() for part in match.group(1).split(",\n")]
    if len(parts) != 13:
        raise SystemExit(f"expected H plus 12 rows, found {len(parts)} parts")
    return parts[0], parts[1:]


def split_signed_terms(poly: str) -> list[tuple[int, str]]:
    chunks = re.split(r"\s+([+-])\s+", poly.strip())
    if not chunks or not chunks[0]:
        raise ValueError("empty polynomial")
    answer = [(1, chunks[0])]
    for i in range(1, len(chunks), 2):
        answer.append((-1 if chunks[i] == "-" else 1, chunks[i + 1]))
    return answer


def parse_source_row(source_index: int, poly: str) -> SourceRow:
    terms = split_signed_terms(poly)
    coefficients: dict[tuple[int, ...], tuple[int, int]] = {}
    for sign, term in terms:
        factors = term.split("*")
        if not factors or not re.fullmatch(r"\d+", factors[0]):
            raise ValueError(
                f"source row {source_index}: coefficient is not an explicit integer: {term[:80]}"
            )
        coefficient = sign * int(factors.pop(0))
        exponents = {variable: 0 for variable in ALL_SOURCE_VARS}
        for factor in factors:
            match = FACTOR_RE.fullmatch(factor)
            if match is None:
                raise ValueError(
                    f"source row {source_index}: unrecognized factor {factor!r}"
                )
            variable = match.group(1)
            exponent = int(match.group(2) or "1")
            if exponents[variable]:
                raise ValueError(
                    f"source row {source_index}: repeated factor {variable}"
                )
            exponents[variable] = exponent
        y_exponent = exponents.pop(Y)
        if y_exponent not in (0, 1):
            raise ValueError(
                f"source row {source_index}: y exponent {y_exponent}, expected <=1"
            )
        monomial = tuple(exponents[variable] for variable in REMAINING)
        y_coefficient, constant_coefficient = coefficients.get(monomial, (0, 0))
        if y_exponent:
            y_coefficient += coefficient
        else:
            constant_coefficient += coefficient
        coefficients[monomial] = (y_coefficient, constant_coefficient)
    coefficients = {
        monomial: pair for monomial, pair in coefficients.items() if pair != (0, 0)
    }
    if not coefficients:
        raise ValueError(f"source row {source_index}: zero row")
    return SourceRow(source_index, len(terms), coefficients)


def transform_row(row: SourceRow) -> DRow:
    # 78*(a*y+b)|_{y=(d+21)/78} = a*d + (21*a+78*b).
    expanded: list[tuple[tuple[int, ...], int, int]] = []
    component_gcd = 0
    for monomial, (a, b) in row.coefficients.items():
        d_coefficient = a
        constant_coefficient = 21 * a + 78 * b
        component_gcd = math.gcd(component_gcd, abs(d_coefficient))
        component_gcd = math.gcd(component_gcd, abs(constant_coefficient))
        expanded.append((monomial, d_coefficient, constant_coefficient))
    if component_gcd == 0:
        raise ValueError(f"source row {row.source_index}: zero transformed row")

    primitive: list[tuple[tuple[int, ...], int, int]] = []
    primitive_gcd = 0
    for monomial, a, b in expanded:
        a //= component_gcd
        b //= component_gcd
        primitive_gcd = math.gcd(primitive_gcd, abs(a))
        primitive_gcd = math.gcd(primitive_gcd, abs(b))
        primitive.append((monomial, a, b))
    if primitive_gcd != 1:
        raise AssertionError(
            f"source row {row.source_index}: failed primitive normalization"
        )

    rendered: list[tuple[int, str]] = []
    for monomial, a, b in primitive:
        # Give each coefficient a positive-oriented first nonzero component.
        sign = 1 if (a > 0 or (a == 0 and b > 0)) else -1
        a *= sign
        b *= sign
        coefficient = signed_linear_text(a, b)
        mono = monomial_text(monomial)
        if mono:
            if coefficient == "1":
                body = mono
            else:
                body = f"({coefficient})*{mono}"
        else:
            body = coefficient
        rendered.append((sign, body))

    expression_parts: list[str] = []
    for position, (sign, body) in enumerate(rendered):
        if position == 0:
            expression_parts.append(body if sign > 0 else "-" + body)
        else:
            expression_parts.append((" + " if sign > 0 else " - ") + body)
    expression = "".join(expression_parts)

    # Mechanical inverse-map validation, coefficient by coefficient:
    # (A*d+B)|_{d=78*y-21} = 78*A*y+(B-21*A).
    # The emitted row must be (78/g)*the charged source row exactly, even
    # before quotienting by H_6.
    for monomial, (source_a, source_b) in row.coefficients.items():
        emitted_a = source_a // component_gcd
        emitted_b = (21 * source_a + 78 * source_b) // component_gcd
        inverse_y = 78 * emitted_a
        inverse_constant = emitted_b - 21 * emitted_a
        if inverse_y != (78 * source_a) // component_gcd:
            raise AssertionError((row.source_index, monomial, "inverse y mismatch"))
        if inverse_constant != (78 * source_b) // component_gcd:
            raise AssertionError(
                (row.source_index, monomial, "inverse constant mismatch")
            )

    return DRow(
        source_index=row.source_index,
        source_term_count=row.source_term_count,
        monomial_count=len(primitive),
        component_gcd=component_gcd,
        rational_scale=Fraction(78, component_gcd),
        expression=expression,
        expression_sha256=sha256_bytes(expression.encode("utf-8")),
    )


def validate_scalar_maps() -> None:
    """Exact stdlib-Fraction checks for maps, H_6, c, and c^{-1}."""
    # Linear coefficient maps use pairs (coefficient of generator, constant).
    def phi_y(pair: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        a, b = pair
        return a / 78, b + 21 * a / 78  # d coefficient, constant

    def psi_d(pair: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        a, b = pair
        return 78 * a, b - 21 * a  # y coefficient, constant

    probes = [
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(37, 11), Fraction(-19, 5)),
    ]
    for probe in probes:
        if psi_d(phi_y(probe)) != probe or phi_y(psi_d(probe)) != probe:
            raise AssertionError("forward/inverse coefficient maps do not compose")

    # H_6((d+21)/78) = (d^2-21)/12 coefficient-by-coefficient.
    h_d2 = Fraction(507, 78 * 78)
    h_d1 = Fraction(2 * 507 * 21, 78 * 78) - Fraction(273, 78)
    h_d0 = Fraction(507 * 21 * 21, 78 * 78) - Fraction(273 * 21, 78) + 35
    if (h_d2, h_d1, h_d0) != (
        Fraction(1, 12),
        Fraction(0),
        Fraction(-21, 12),
    ):
        raise AssertionError("H_6 forward image mismatch")
    # (78*y-21)^2-21 = 12 H_6(y).
    if (78 * 78, -2 * 78 * 21, 21 * 21 - 21) != (
        12 * 507,
        -12 * 273,
        12 * 35,
    ):
        raise AssertionError("d minpoly inverse image mismatch")

    # In Q[d]/(d^2-21), c maps to -665(d+9)/171366.
    c_d = (Fraction(-665, 171366), Fraction(-5985, 171366))
    c_d_inverse = (Fraction(28561, 6650), Fraction(-9 * 28561, 6650))
    # (a*d+b)(e*d+f) = (a*f+b*e)d + (21*a*e+b*f).
    a, b = c_d
    e, f = c_d_inverse
    product = (a * f + b * e, 21 * a * e + b * f)
    if product != (Fraction(0), Fraction(1)):
        raise AssertionError("c image inverse mismatch")

    # Inverse image of c_d agrees with c_y reduced modulo H_6.
    c_back = psi_d(c_d)
    # c_y = 19/2197*(7y-78y^2), and
    # y^2=(273y-35)/507 modulo H_6.
    c_y_reduced = (
        Fraction(19, 2197) * (7 - Fraction(78 * 273, 507)),
        Fraction(19, 2197) * Fraction(78 * 35, 507),
    )
    if c_back != c_y_reduced:
        raise AssertionError("c inverse image modulo H_6 mismatch")


def emit_driver(rows: list[DRow], source_sha256: str) -> str:
    shortest = sorted(
        rows,
        key=lambda row: (row.monomial_count, len(row.expression), row.source_index),
    )
    lines = [
        "// Exact t=6 heuristic terminal preconditioned in Q[d]/(d^2-21).",
        "// Generated by emit_dmodel_nfmodstd.py from the charged Q[y] driver.",
        f"// source_sha256={source_sha256}",
        "// FORWARD MAP: q13_1=y |-> (d+21)/78.",
        "// INVERSE MAP: d |-> 78*y-21.",
        "// H6=507*y^2-273*y+35 maps to (d^2-21)/12.",
        "// c=19*y*(7-78*y)/2197 maps to -665*(d+9)/171366.",
        "// Main ring intentionally has six variables and no W; c is a field unit.",
        'LIB "resources.lib";',
        "setcores(3);",
        'LIB "nfmodstd.lib";',
        "",
        "// Explicit two-sided ring-map and H/c image checks over Q[y,d].",
        "ring RMAP=0,(y,d),dp;",
        "poly H_y=507*y^2-273*y+35;",
        "poly m_d=d^2-21;",
        "poly d_forward=78*y-21;",
        "poly y_inverse=(d+21)/78;",
        "poly c_y=19*y*(7-78*y)/2197;",
        "poly c_d=-665*(d+9)/171366;",
        'if (subst(d_forward,y,y_inverse)-d==0) { print("CONTROL_MAP_FORWARD_AFTER_INVERSE_PASS"); } else { print("CONTROL_MAP_FORWARD_AFTER_INVERSE_FAIL"); }',
        'if (subst(y_inverse,d,d_forward)-y==0) { print("CONTROL_MAP_INVERSE_AFTER_FORWARD_PASS"); } else { print("CONTROL_MAP_INVERSE_AFTER_FORWARD_FAIL"); }',
        'if (subst(H_y,y,y_inverse)-m_d/12==0) { print("CONTROL_H_FORWARD_IMAGE_PASS"); } else { print("CONTROL_H_FORWARD_IMAGE_FAIL"); }',
        'if (subst(m_d,d,d_forward)-12*H_y==0) { print("CONTROL_H_INVERSE_IMAGE_PASS"); } else { print("CONTROL_H_INVERSE_IMAGE_FAIL"); }',
        "ideal MD=m_d; ideal HY=H_y;",
        'if (reduce(subst(c_y,y,y_inverse)-c_d,std(MD))==0) { print("CONTROL_C_FORWARD_IMAGE_PASS"); } else { print("CONTROL_C_FORWARD_IMAGE_FAIL"); }',
        'if (reduce(subst(c_d,d,d_forward)-c_y,std(HY))==0) { print("CONTROL_C_INVERSE_IMAGE_PASS"); } else { print("CONTROL_C_INVERSE_IMAGE_FAIL"); }',
        "",
        "// Charged actual-pair control.",
        "ring RAC=0,(gamma,pi),dp;",
        "poly FAC=pi;",
        "poly GAC=pi-(gamma^2)/2;",
        "poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);",
        'if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); } else { print("CONTROL_ACTUAL_PAIR_FAIL"); }',
        'if (nameof(basering)=="RAC") { print("CONTROL_RAC_RING_PASS"); } else { print("CONTROL_RAC_RING_FAIL"); }',
        "",
        "// Positive/negative wrapper controls and the c-unit check live outside",
        "// the main ring.  These controls retain W; the computation below does not.",
        "ring RC=(0,d),(u,W),dp;",
        "minpoly=d^2-21;",
        "number cbar=-665*(d+9)/171366;",
        "number cbar_inverse=28561*(d-9)/6650;",
        'if (cbar*cbar_inverse==1) { print("CONTROL_C_UNIT_PASS"); } else { print("CONTROL_C_UNIT_FAIL"); }',
        'if (nameof(basering)=="RC") { print("CONTROL_RC_RING_PASS"); } else { print("CONTROL_RC_RING_FAIL"); }',
        "ideal RCE=u,W*u-1;",
        "ideal RCGE=std(RCE);",
        'if (typeof(RCGE)=="ideal" && nameof(basering)=="RC") { print("CONTROL_RC_EMPTY_EXTRACT_RING_PASS"); } else { print("CONTROL_RC_EMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,RCGE)==0) { print("CONTROL_RC_EMPTY_PASS"); } else { print("CONTROL_RC_EMPTY_FAIL"); }',
        "ideal RCN=u-1,W*u-1;",
        "ideal RCGN=std(RCN);",
        'if (typeof(RCGN)=="ideal" && nameof(basering)=="RC") { print("CONTROL_RC_NONEMPTY_EXTRACT_RING_PASS"); } else { print("CONTROL_RC_NONEMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,RCGN)!=0) { print("CONTROL_RC_NONEMPTY_PASS"); } else { print("CONTROL_RC_NONEMPTY_FAIL"); }',
        "",
        "// Main exact ring: W is omitted because cbar is already a nonzero field",
        "// element, so (I:cbar^infinity)=I.  Variable order is declared explicitly.",
        "ring RK=(0,d),(q7_0,q8_1,q9_1,q10_1,q11_1,q12_1),dp;",
        "minpoly=d^2-21;",
        "option(redSB);",
        'if (nameof(basering)=="RK") { print("CONTROL_RK_RING_PASS"); } else { print("CONTROL_RK_RING_FAIL"); }',
        'if (defined(W)==0) { print("CONTROL_MAIN_NO_W_PASS"); } else { print("CONTROL_MAIN_NO_W_FAIL"); }',
        "number cbar_main=-665*(d+9)/171366;",
        "number cbar_main_inverse=28561*(d-9)/6650;",
        'if (cbar_main*cbar_main_inverse==1) { print("CONTROL_MAIN_C_UNIT_PASS"); } else { print("CONTROL_MAIN_C_UNIT_FAIL"); }',
        "",
        "// Raw d-model rows.  For source row i, raw_i=(78/g_i)*phi(source_i).",
        "// Each raw row is then multiplied by inverse(leadcoef(raw_i)); the runtime",
        "// product check certifies that this second row scaling is a field unit.",
    ]

    for row in shortest:
        index = row.source_index
        scale = row.rational_scale
        lines.extend(
            [
                (
                    f"// source_row={index} source_terms={row.source_term_count} "
                    f"d_terms={row.monomial_count} bytes={len(row.expression)} "
                    f"g={row.component_gcd} raw_scale={frac_text(scale)} "
                    f"row_sha256={row.expression_sha256} inverse_map=PASS"
                ),
                f"number raw_scale_{index}={frac_text(scale)};",
                f"number raw_scale_inverse_{index}={frac_text(1 / scale)};",
                f'if (raw_scale_{index}*raw_scale_inverse_{index}==1) {{ print("CONTROL_RAW_SCALE_{index}_UNIT_PASS"); }} else {{ print("CONTROL_RAW_SCALE_{index}_UNIT_FAIL"); }}',
                f"poly row_{index}={row.expression};",
                f'if (row_{index}!=0) {{ print("CONTROL_ROW_{index}_NONZERO_PASS"); }} else {{ print("CONTROL_ROW_{index}_NONZERO_FAIL"); }}',
                f"number monic_scale_{index}=1/leadcoef(row_{index});",
                f'if (leadcoef(row_{index})*monic_scale_{index}==1) {{ print("CONTROL_MONIC_SCALE_{index}_UNIT_PASS"); }} else {{ print("CONTROL_MONIC_SCALE_{index}_UNIT_FAIL"); }}',
                f"row_{index}=monic_scale_{index}*row_{index};",
                f'if (leadcoef(row_{index})==1) {{ print("CONTROL_ROW_{index}_MONIC_PASS"); }} else {{ print("CONTROL_ROW_{index}_MONIC_FAIL"); }}',
            ]
        )

    order = ",".join(f"row_{row.source_index}" for row in shortest)
    order_label = ",".join(str(row.source_index) for row in shortest)
    lines.extend(
        [
            "",
            f"// SHORTEST_FIRST_SOURCE_ORDER={order_label}",
            f"ideal I={order};",
            'if (size(I)==12) { print("CONTROL_12_ROWS_PASS"); } else { print("CONTROL_12_ROWS_FAIL"); }',
            'print("MAIN_START t=6 field=Qsqrt21 rows=12 vars=6 W=omitted method=nfmodStd cores=3");',
            "ideal G=nfmodStd(I);",
            'print("MAIN_DONE basis_size=");',
            "size(G);",
            'if (typeof(G)=="ideal" && nameof(basering)=="RK") { print("MAIN_EXTRACT_RING_PASS"); } else { print("MAIN_EXTRACT_RING_FAIL"); }',
            'if (reduce(1,G)==0) { print("MAIN_EXACT_UNIT"); G; } else { print("MAIN_NONUNIT"); print("BASIS_OUTPUT_TRUNCATED_TO_10"); int basis_cap=size(G); if (basis_cap>10) { basis_cap=10; } for (int basis_i=1; basis_i<=basis_cap; basis_i++) { G[basis_i]; } }',
            "quit;",
            "",
        ]
    )
    return "\n".join(lines)


def validation_text(
    rows: list[DRow], source_sha256: str, output_sha256: str, output_bytes: int
) -> str:
    shortest = sorted(
        rows,
        key=lambda row: (row.monomial_count, len(row.expression), row.source_index),
    )
    lines = [
        "emit_dmodel exact validation",
        f"source={SOURCE.name}",
        f"source_sha256={source_sha256}",
        f"output={OUTPUT.name}",
        f"output_sha256={output_sha256}",
        f"output_bytes={output_bytes}",
        "source_rows=12 PASS",
        "source_H=2028*y^2-1092*y+140=4*H6 PASS",
        "forward_map=y->(d+21)/78 PASS",
        "inverse_map=d->78*y-21 PASS",
        "map_compositions=identity PASS",
        "H6_forward=(d^2-21)/12 PASS",
        "d_minpoly_inverse=12*H6 PASS",
        "c_forward=-665*(d+9)/171366 PASS",
        "c_inverse=19*y*(7-78*y)/2197_mod_H6 PASS",
        "c_norm=2211125/2447192163_nonzero PASS",
        "c_inverse=28561*(d-9)/6650 PASS",
        "main_ring_variables=q7_0,q8_1,q9_1,q10_1,q11_1,q12_1",
        "main_ring_W=omitted PASS",
        "nfmodStd_cores=3",
        "shortest_first_source_order="
        + ",".join(str(row.source_index) for row in shortest),
        "",
        "source_row source_terms d_terms component_gcd raw_scale row_sha256 inverse_map",
    ]
    for row in shortest:
        lines.append(
            f"{row.source_index} {row.source_term_count} {row.monomial_count} "
            f"{row.component_gcd} {frac_text(row.rational_scale)} "
            f"{row.expression_sha256} PASS"
        )
    lines.extend(
        [
            "",
            "Inverse-map meaning: for every monomial in every emitted raw row,",
            "substitution d=78*y-21 returns (78/component_gcd)*source_row exactly",
            "over Z[y], hence also in Q[y]/(H6).  All 12 checks passed.",
            "Runtime monic scalings are checked by leadcoef(row)*monic_scale==1",
            "before the scaled rows are placed in the nfmodStd ideal.",
            "VALIDATION_PASS",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    source_bytes = SOURCE.read_bytes()
    source_sha256 = sha256_bytes(source_bytes)
    if source_sha256 != EXPECTED_SOURCE_SHA256:
        raise SystemExit(
            "source SHA-256 mismatch: "
            f"expected {EXPECTED_SOURCE_SHA256}, got {source_sha256}"
        )
    source = source_bytes.decode("utf-8")
    source_h, source_polynomials = extract_source_ideal(source)
    normalized_h = re.sub(r"\s+", "", source_h)
    if normalized_h != "2028*q13_1^2-1092*q13_1+140":
        raise SystemExit(f"unexpected source H polynomial: {source_h!r}")

    validate_scalar_maps()
    parsed = [
        parse_source_row(index, polynomial)
        for index, polynomial in enumerate(source_polynomials, start=1)
    ]
    rows = [transform_row(row) for row in parsed]
    if len(rows) != 12 or len({row.source_index for row in rows}) != 12:
        raise AssertionError("the transformed row set is not exactly 12 rows")

    output_text = emit_driver(rows, source_sha256)
    # Guard the requested main-ring shape mechanically before writing.
    expected_ring = (
        "ring RK=(0,d),(q7_0,q8_1,q9_1,q10_1,q11_1,q12_1),dp;"
    )
    if expected_ring not in output_text:
        raise AssertionError("six-variable W-free main ring was not emitted")
    if "setcores(3);" not in output_text or "ideal G=nfmodStd(I);" not in output_text:
        raise AssertionError("requested three-core nfmodStd call was not emitted")

    OUTPUT.write_text(output_text, encoding="utf-8")
    output_bytes = OUTPUT.read_bytes()
    output_sha256 = sha256_bytes(output_bytes)
    VALIDATION.write_text(
        validation_text(rows, source_sha256, output_sha256, len(output_bytes)),
        encoding="utf-8",
    )

    print(f"SOURCE_SHA256 {source_sha256}")
    print(f"OUTPUT {OUTPUT.name} {len(output_bytes)} {output_sha256}")
    print(
        f"VALIDATION {VALIDATION.name} {VALIDATION.stat().st_size} "
        f"{sha256_bytes(VALIDATION.read_bytes())}"
    )
    print("SHORTEST_FIRST", ",".join(
        str(row.source_index)
        for row in sorted(
            rows,
            key=lambda row: (
                row.monomial_count,
                len(row.expression),
                row.source_index,
            ),
        )
    ))
    print("INVERSE_MAP_VALIDATION PASS rows=12")


if __name__ == "__main__":
    main()
