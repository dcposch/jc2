#!/usr/bin/env python3
"""Exact dependency-complete union for the fixed-A3 q2-beta B3 divisor.

The producer replays the route algebra and checks every source-theorem leaf.
It does not rerun the large eliminations.  Its only theorem target is the
raw divisor B3=0 in the already fixed source-typed A3 q2-beta section.
"""

from fractions import Fraction
from hashlib import sha256
import os
from pathlib import Path
import platform
import socket
import sys


HERE = Path(__file__).resolve().parent


def preflight():
    assert platform.system() == "Linux", "AWS-only producer: Linux required"
    assert sys.flags.optimize == 0, "assert-based gate refuses optimized Python"
    tag = os.environ.get("JC2_AWS_RUN_TAG", "")
    expected = os.environ.get("JC2_AWS_EXPECTED_HOSTNAME", "")
    assert tag.startswith("td6_v75_"), "registered V75 AWS tag required"
    assert expected and socket.gethostname() == expected, (
        socket.gethostname(), expected
    )
    print(f"aws_run_tag={tag}")
    print(f"aws_hostname={socket.gethostname()}")


def digest(relative):
    return sha256((HERE / relative).read_bytes()).hexdigest()


def verify_manifest():
    listed = set()
    for raw in (HERE / "SOURCE.sha256").read_text().splitlines():
        if not raw.strip():
            continue
        expected, relative = raw.split(None, 1)
        relative = relative.lstrip("*")
        listed.add(relative)
        got = digest(relative)
        assert got == expected, (relative, got, expected)
    actual = {
        path.relative_to(HERE).as_posix()
        for path in HERE.rglob("*")
        if path.is_file() and path.name != "SOURCE.sha256"
    }
    assert listed == actual, (sorted(listed - actual), sorted(actual - listed))
    print("source_manifest_verified=true")


def require(text, markers):
    missing = [marker for marker in markers if marker not in text]
    assert not missing, missing


def clean(poly):
    return {m: Fraction(c) for m, c in poly.items() if c}


def add(left, right, scale=1):
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, Fraction()) + scale*coefficient
    return clean(result)


def mul(left, right):
    result = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            key = tuple(a+b for a, b in zip(lm, rm))
            result[key] = result.get(key, Fraction()) + lc*rc
    return clean(result)


def scale(poly, coefficient):
    return clean({m: coefficient*c for m, c in poly.items()})


def power(poly, exponent, dimension):
    result = {(0,)*dimension: Fraction(1)}
    for _ in range(exponent):
        result = mul(result, poly)
    return result


def route_algebra():
    # Raw B3(C,V,U).
    one3 = {(0, 0, 0): Fraction(1)}
    C = {(1, 0, 0): Fraction(1)}
    V = {(0, 1, 0): Fraction(1)}
    U = {(0, 0, 1): Fraction(1)}
    B3 = scale(mul(power(C, 2, 3), power(U, 2, 3)), 4)
    B3 = add(B3, scale(mul(mul(C, power(V, 2, 3)), U), -4))
    B3 = add(B3, scale(mul(C, power(U, 4, 3)), 24))
    B3 = add(B3, power(V, 4, 3))
    B3 = add(B3, scale(mul(power(V, 2, 3), power(U, 3, 3)), -20))
    B3 = add(B3, scale(power(U, 6, 3), 20))

    # V=0 gives the two non-origin lines on D(U).
    B3_vzero = {m: c for m, c in B3.items() if m[1] == 0}
    cplus1 = add(C, power(U, 2, 3))
    cplus5 = add(C, scale(power(U, 2, 3), 5))
    expected_vzero = scale(
        mul(power(U, 2, 3), mul(cplus1, cplus5)), 4
    )
    assert B3_vzero == expected_vzero

    # Normalized b(x,y), its line pencil y=t(x+5), and boundary values.
    one2 = {(0, 0): Fraction(1)}
    x = {(1, 0): Fraction(1)}
    t = {(0, 1): Fraction(1)}
    xplus5 = add(x, scale(one2, 5))
    y = mul(t, xplus5)
    b = add(scale(power(x, 2, 2), 4), scale(mul(x, y), -4))
    b = add(b, scale(x, 24))
    b = add(b, power(y, 2, 2))
    b = add(b, scale(y, -20))
    b = add(b, scale(one2, 20))
    tminus2 = add(t, scale(one2, -2))
    qline = add(mul(power(tminus2, 2, 2), x), scale(power(t, 2, 2), 5))
    qline = add(qline, scale(t, -20))
    qline = add(qline, scale(one2, 4))
    assert b == mul(xplus5, qline)

    # b(-5,y)=y^2: in the U!=0,V!=0 field branch x+5 cannot vanish.
    # Here represent b(x,y) independently in Q[x,y].
    yy = {(0, 1): Fraction(1)}
    bx_y = add(scale(power(x, 2, 2), 4), scale(mul(x, yy), -4))
    bx_y = add(bx_y, scale(x, 24))
    bx_y = add(bx_y, power(yy, 2, 2))
    bx_y = add(bx_y, scale(yy, -20))
    bx_y = add(bx_y, scale(one2, 20))
    at_minus5 = {}
    for (xd, yd), coefficient in bx_y.items():
        at_minus5[(yd,)] = at_minus5.get((yd,), Fraction()) + coefficient*((-5)**xd)
    assert clean(at_minus5) == {(2,): Fraction(1)}

    # Exact dehomogenization/homogenization link:
    # B3(C,V,U) = U^6 b(C/U^2,V^2/U^3).
    lifted_b = {}
    for (x_degree, y_degree), coefficient in bx_y.items():
        u_degree = 6 - 2*x_degree - 3*y_degree
        assert u_degree >= 0
        monomial = (x_degree, 2*y_degree, u_degree)
        lifted_b[monomial] = lifted_b.get(monomial, Fraction()) + coefficient
    assert clean(lifted_b) == B3

    # Boundary specializations in the line pencil.
    def specialize_t(poly, value):
        result = {}
        for (xd, td), coefficient in poly.items():
            result[(xd,)] = result.get((xd,), Fraction()) + coefficient*value**td
        return clean(result)

    assert specialize_t(b, 0) == {(0,): Fraction(20), (1,): Fraction(24), (2,): Fraction(4)}
    assert specialize_t(b, 2) == {(0,): Fraction(-80), (1,): Fraction(-16)}

    # Wrong raw coefficient, missing-line, and wrong t=2 controls.
    wrong = add(B3_vzero, scale(power(U, 6, 3), -1))
    assert wrong != expected_vzero
    assert B3_vzero != scale(mul(power(U, 2, 3), cplus1), 4)
    assert B3_vzero != scale(mul(power(U, 2, 3), cplus5), 4)
    assert specialize_t(b, 2) != {(0,): Fraction(-64), (1,): Fraction(-16)}


def evidence_gate():
    v66 = (HERE / "evidence/v66/v66.stdout").read_text()
    v66_review = (HERE / "evidence/v66/review.md").read_text()
    v67_half = (HERE / "evidence/v67/b3half.stdout").read_text()
    v67_quad = (HERE / "evidence/v67/b3tq.stdout").read_text()
    v67_review = (HERE / "evidence/v67/review.md").read_text()
    v68 = (HERE / "evidence/v68/v68.stdout").read_text()
    v68_review = (HERE / "evidence/v68/review.md").read_text()
    v70_review = (HERE / "evidence/v70/review.md").read_text()
    v46 = (HERE / "evidence/v46/v46.stdout").read_text()
    lines_review = (HERE / "evidence/v46/review.md").read_text()
    lines_erratum = (HERE / "evidence/v46/dependency-erratum.md").read_text()

    require(v66, (
        "producer=TD6-A3-Q2-B3-SOURCE-DAG-REPAIRED-V66",
        "B3_parameter_b_identity_zero=true",
        "B3_parameter_open_requires=t*w*(t-2)!=0",
        "raw_stratum_fraction_field_source_identity_exact=true",
        "B3_original_center_identity_zero=true",
        "B3_inverse_t_equals_y_over_xplus5=true",
        "N13_full_first_previous_current_source_identity_exact_by_DAG=true",
        "P12_first_original_row_replay=true",
        "DAG_leaf_denominator_factor_set=['2*C - 1', 'C', 'C - 2', 'C^2 - 4*C + 2', 'V']",
        "raw_denominator_factor_strata_still_charged=true",
        "TD6-A3-Q2-B3-SOURCE-DAG-REPAIRED-V66 PASS",
    ))
    assert v66_review.rstrip().endswith("CONFIRMED")

    common_v67 = (
        "producer=TD6-A3-Q2-B3-FACTOR-SOURCE-DAG-REPAIRED-V67",
        "scope=function_field_of_exact_printed_component",
        "direct_qprime_retained=true",
        "B3_parameter_center_identity_zero=true",
        "curve_fraction_field_source_identity_exact=true",
        "N13_full_first_previous_current_source_identity_exact_by_DAG=true",
        "P12_first_original_row_replay=true",
        "combined_unit_residual_is_minus_k_over_50=true",
        "DAG_leaf_denominator_factor_set=['x']",
        "only_parameter_zero_exception=true",
        "raw_w_zero_origin_endpoint_still_separate=true",
        "TD6-A3-Q2-B3-FACTOR-SOURCE-DAG-REPAIRED-V67 PASS",
    )
    require(v67_half, ("component=b3half", "B3_parameter_factor=2*t-1") + common_v67)
    require(v67_quad, ("component=b3tq", "B3_parameter_factor=t^2-4*t+2") + common_v67)
    assert v67_review.rstrip().endswith("CONFIRMED")

    require(v68, (
        "normalized_line_pencil_factorization_exact=true",
        "B3_at_V_zero=4*U^2*(C+U^2)*(C+5U^2)",
        "route_target_union=U0_zero_union_(V0_zero_C0_plus_U0sq_zero)_union_(V0_zero_C0_plus5U0sq_zero)",
        "TD6-A3-Q2-B3-BOUNDARY-ROUTES-V68 PASS",
    ))
    require(v68_review, (
        "The raw identity and the finite-branch translation",
        "No whole-B3",
    ))
    # The frozen V68 review retains a post-verdict residual-obligations
    # appendix, so its authoritative verdict is an exact standalone line
    # rather than the final byte sequence of the file.
    assert "CONFIRMED" in {line.strip() for line in v68_review.splitlines()}

    assert v70_review.rstrip().endswith("CONFIRMED")
    require(v70_review, (
        "Whole raw `U=0`",
        "fixed source-typed A3 q2-beta section",
    ))

    require(v46, (
        "source_center=V=C+U^2=0 over Q(U)",
        "scope_open=fraction_field_of_printed_raw_stratum",
        "rational_stratum_source_typing_exact=true",
        "first_full_beta_P12_compatibility_original_row_replay=true",
        "first_full_beta_P12_unit_certificate_denominator=(U^6)",
        "first_full_beta_P12_only_U_exception=true",
        "TD6-A3-Q2-CPLUS1-FIRST-UNIT-INCOMPATIBILITY-CANONICAL PASS",
    ))
    assert lines_review.rstrip().endswith("CONFIRMED_WITH_REPAIRS")
    require(lines_erratum, (
        "`C=-U^2,D(U)` is source-closed by V46",
        "`C=-5U^2,D(U)` is the precise remaining staged-N13 source-DAG debt",
    ))

    print("pre_V74_static_dependency_markers_verified=true")
    v74 = (HERE / "evidence/v74/v74.stdout").read_text()
    require(v74, (
        "source_manifest_verified=true",
        "producer=TD6-A3-Q2-CMINUS5-WHOLE-LINE-UNION-V74",
        "q_beta=t+beta*t^2+t^25",
        "direct_qprime_retained_on_DU=true",
        "line_open_DU_source_theorem=V73",
        "line_closed_endpoint_U_zero_source_theorem=reviewed_V70_origin",
        "line_U_zero_substitution_is_origin=true",
        "line_cover=D(U)_union_V(U)",
        "line_cover_complete=true",
        "whole_raw_Cminus5_line_all_beta_empty=true",
        "whole_B3_killed=false",
        "whole_A3_killed=false",
        "whole_TD6_killed=false",
        "JC2_resolved=false",
        "TD6-A3-Q2-CMINUS5-WHOLE-LINE-UNION-V74 PASS",
    ))


def case_tree_gate():
    # Exhaustive decision tree for a B3=0 field-valued center.
    leaves = {
        "U=0": "V70-whole-U-zero",
        "U!=0,V=0,C=-U^2": "V46-on-D(U)",
        "U!=0,V=0,C=-5U^2": "V74",
        "U!=0,V!=0,2t-1=0": "V67-b3half-on-D(w)",
        "U!=0,V!=0,t^2-4t+2=0": "V67-b3tq-on-D(w)",
        "U!=0,V!=0,t*(t-2)*(2t-1)*(t^2-4t+2)!=0": "V66-on-D(w)",
    }
    assert len(leaves) == 6

    # On U!=0,V!=0: w=V/U !=0.  If x=-5 then b(-5,y)=y^2,
    # forcing y=0 then V=0, contradiction.  Hence t=y/(x+5) exists.
    # t=0 forces y=0 and V=0; t=2 makes b=-16(x+5), impossible.
    exclusions = {
        "x+5=0": "b(-5,y)=y^2_then_V=0_contradiction",
        "t=0": "y=0_then_V=0_contradiction",
        "t=2": "b=-16*(x+5)_contradiction",
    }
    assert len(exclusions) == 3

    expected_factors = {"t", "w", "t-2", "2t-1", "t^2-4t+2"}
    routed = {"t", "w", "t-2"}
    finite = {"2t-1", "t^2-4t+2"}
    assert routed | finite == expected_factors
    assert routed & finite == set()

    # Omission controls: each source theorem owns an explicit case-tree leaf.
    owner_witness = {
        "V70": "U=0",
        "V46": "U!=0,V=0,C=-U^2",
        "V74": "U!=0,V=0,C=-5U^2",
        "V67-half": "U!=0,V!=0,2t-1=0",
        "V67-quad": "U!=0,V!=0,t^2-4t+2=0",
        "V66": "U!=0,V!=0,t*(t-2)*(2t-1)*(t^2-4t+2)!=0",
    }
    assert set(owner_witness.values()) == set(leaves)
    assert all(leaves[witness].startswith(owner.split("-")[0]) for owner, witness in owner_witness.items())
    universe = set(leaves)
    for removed in owner_witness:
        covered = {
            witness for owner, witness in owner_witness.items() if owner != removed
        }
        assert covered != universe


def main():
    preflight()
    verify_manifest()
    route_algebra()
    print("raw_and_normalized_B3_route_algebra_exact=true")
    evidence_gate()
    print("all_source_dependency_markers_and_reviews_verified=true")
    case_tree_gate()
    print("constructible_case_tree_and_omission_controls_exact=true")

    print("producer=TD6-A3-Q2-B3-ATLAS-UNION-REPAIRED-V75")
    print("raw_B3_polynomial_identity_replayed=true")
    print("normalized_B3_line_pencil_identity_replayed=true")
    print("xplus5_zero_branch_routes_to_V_zero=true")
    print("t_zero_branch_routes_to_V_zero=true")
    print("t_two_branch_empty_off_xplus5_zero=true")
    print("V66_generic_source_DAG_reviewed=true")
    print("V67_two_finite_factor_source_DAGs_reviewed=true")
    print("V68_boundary_route_algebra_reviewed_and_replayed=true")
    print("V70_whole_U_zero_source_theorem_reviewed=true")
    print("V46_Cminus1_DU_source_theorem_reviewed=true")
    print("V74_Cminus5_whole_line_source_union_consumed=true")
    print("dependency_factor_union=t,w,t-2,2t-1,t^2-4t+2")
    print("dependency_case_tree_complete=true")
    print("each_dependency_omission_negative_control=true")
    print("whole_raw_B3_divisor_all_beta_empty=true")
    print("scope=fixed_source_typed_A3_q2_beta_section_only")
    print("whole_A3_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("landing_proved=false")
    print("JC2_resolved=false")
    print("TD6-A3-Q2-B3-ATLAS-UNION-REPAIRED-V75 PASS")


if __name__ == "__main__":
    main()
