#!/usr/bin/env python3
"""Exact complete-mode continuation from D18 through the D22 endpoint."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from functools import reduce
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREDECESSOR = (ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828"
               / "verify_uniform_d16_d17.py")
PREDECESSOR_RESULT = PREDECESSOR.with_name("RESULT.json")
RAW = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
RESULT = HERE / "RESULT.json"

PREDECESSOR_SHA256 = "5904d7b19dc5d46d31a781150c4b6de9e62e32812b554006e92f78f9d76fd5d9"
PREDECESSOR_RESULT_SHA256 = "2a6f363df8fb4aef94f01d7a938e3bfcff15f6db49af3164e36367c9a6d1929a"
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_dependencies():
    assert digest(PREDECESSOR) == PREDECESSOR_SHA256
    assert digest(PREDECESSOR_RESULT) == PREDECESSOR_RESULT_SHA256
    specification = importlib.util.spec_from_file_location("uniform_d16_frozen", PREDECESSOR)
    assert specification is not None and specification.loader is not None
    prior = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(prior)
    replay = prior.calculate_result()
    assert replay["status"] == "PASS_EXACT_FIELD_POINT_CHARACTERISTIC_CASCADE_THROUGH_D17"
    _, desk = prior.load_dependencies()
    desk.DERIVATIVES.update({
        name: f"{name}_x"
        for name in ("b", "d", "e", "h", "j", "k", "ell",
                     "m", "n", "o", "p", "s", "u")
    })
    return prior, desk


def characteristic_calculation(desk):
    term, add, scale, mul, shift = (
        desk.la_term, desk.la_add, desk.la_scale, desk.la_mul, desk.la_shift)

    def product(*items):
        return reduce(mul, items)

    z, v, r, q, t, y = (term(1, 0, name)
                         for name in ("z", "v", "r", "q", "t", "y"))
    b, d, e, h, j, k, ell = (term(1, 0, name)
                              for name in ("b", "d", "e", "h", "j", "k", "ell"))
    c8 = term(1, 0, "c8")

    F = desk.common_F_prefix()
    F[4] = add(scale(Q(1, 16), v), scale(Q(1, 64), mul(z, z)), term(1, 2, "r"))
    F[5] = add(scale(Q(1, 2), r), scale(Q(1, 64), mul(z, v)), term(1, 2, "q"))
    F[6] = add(scale(Q(1, 2), q), scale(Q(1, 8), mul(r, z)),
               scale(Q(1, 256), mul(v, v)), term(1, 2, "t"))
    F[7] = add(scale(Q(1, 2), t), scale(Q(1, 8), mul(q, z)),
               scale(Q(1, 16), mul(r, v)), term(1, 2, "y"))
    for weight in range(8, 15):
        F[weight] = term(1, 0, f"f{weight}")
    for weight in range(15, 23):
        F[weight] = {}
    _, g = desk.continuation(F, 22)

    base8 = add(scale(Q(1, 2), y), scale(Q(1, 8), mul(t, z)),
                scale(Q(1, 16), mul(q, v)), scale(Q(1, 4), mul(r, r)))
    base9 = add(scale(Q(1, 2), mul(q, r)), scale(Q(1, 16), mul(t, v)),
                scale(Q(1, 8), mul(y, z)))
    base10 = add(scale(Q(1, 4), mul(d, z)), scale(Q(1, 4), mul(q, q)),
                 scale(Q(1, 2), mul(r, t)), scale(Q(1, 16), mul(v, y)))
    base11 = add(scale(Q(1, 2), mul(e, z)), scale(Q(1, 2), mul(q, t)),
                 scale(Q(1, 2), mul(r, y)), scale(Q(1, 8), mul(d, v)))
    base12 = add(mul(d, r), scale(Q(1, 4), mul(e, v)),
                 scale(Q(1, 16), product(e, z, z)), scale(Q(3, 4), mul(h, z)),
                 scale(Q(1, 2), mul(q, y)), scale(Q(1, 4), mul(t, t)))
    base13 = add(mul(d, q), scale(2, mul(e, r)),
                 scale(Q(1, 16), product(e, v, z)), scale(Q(3, 8), mul(h, v)),
                 scale(Q(3, 16), product(h, z, z)), mul(j, z),
                 scale(Q(1, 2), mul(t, y)))
    base14 = add(
        mul(d, t), scale(2, mul(e, q)), scale(Q(1, 2), product(e, r, z)),
        scale(Q(1, 64), product(e, v, v)), scale(3, mul(h, r)),
        scale(Q(3, 16), product(h, v, z)), scale(Q(1, 64), product(h, z, z, z)),
        scale(Q(1, 2), mul(j, v)), scale(Q(3, 8), product(j, z, z)),
        scale(Q(5, 4), mul(k, z)), scale(Q(1, 4), mul(y, y)))

    kills = {"c6": {}, "c10": {}, "c14": {}}
    relation16 = {
        "f8": add(base8, b),
        "c16": add(term(1, 2, "m"), scale(Q(-3, 8), mul(b, b)),
                    scale(Q(-1, 2), mul(c8, b))),
    }
    relation17 = {
        "f9": add(base9, d),
        "m": add(scale(Q(3, 2), mul(b, d)), mul(c8, d),
                 scale(-2, term(1, 2, "n"))),
    }

    def substitute_through(item, relations):
        for relation in relations:
            item = desk.la_substitute(item, relation)
        return item

    prefix = [kills, relation16, relation17]

    p18 = add(
        mul(add(scale(Q(3, 4), b), scale(Q(1, 2), c8)),
            add(term(1, 0, "f10"), scale(-1, base10))),
        scale(Q(3, 8), mul(d, d)), scale(Q(-1, 2), term(1, 0, "n")))
    g18_before = substitute_through(g[18], prefix)
    expected_g18 = add(term(1, -3, "c18"), shift(-2, p18))
    assert desk.la_negative(g18_before) == expected_g18
    assert desk.la_operator(18, term(1, -3, "c18")) == {}

    relation18 = {
        "c18": {},
        "f10": add(base10, e),
        "n": add(scale(Q(3, 2), mul(b, e)), mul(c8, e),
                 scale(Q(3, 4), mul(d, d)), scale(-2, term(1, 2, "o"))),
    }
    assert desk.la_negative(substitute_through(g18_before, [relation18])) == {}

    # The complete born c18 mode is homogeneous at D19: predecessor and
    # same-row pieces cancel.  D18 polynomial-window compatibility, not D19,
    # is what kills c18.
    f1 = term(1, 2)
    c18_g18 = term(1, -3, "c18")
    c18_g19 = term(Q(-3, 4), -5, "c18")
    c18_predecessor = add(
        scale(-6, mul(desk.la_derivative(f1), c18_g18)),
        scale(-7, mul(f1, desk.la_derivative(c18_g18))))
    c18_same_row = desk.la_operator(19, c18_g19)
    assert c18_predecessor == term(9, -2, "a_x", "c18")
    assert c18_same_row == term(-9, -2, "a_x", "c18")
    assert add(c18_predecessor, c18_same_row) == {}

    p19 = add(
        mul(add(scale(Q(3, 4), b), scale(Q(1, 2), c8)),
            add(term(1, 0, "f11"), scale(-1, base11))),
        scale(Q(3, 4), mul(d, e)), scale(Q(-1, 2), term(1, 0, "o")))
    g19_before = substitute_through(g[19], prefix + [relation18])
    assert desk.la_negative(g19_before) == shift(-2, p19)
    relation19 = {
        "f11": add(base11, h),
        "o": add(scale(Q(3, 2), mul(b, h)), mul(c8, h),
                 scale(Q(3, 2), mul(d, e)), scale(-2, term(1, 2, "p"))),
    }
    assert desk.la_negative(substitute_through(g19_before, [relation19])) == {}

    p20 = add(
        mul(add(scale(Q(3, 4), b), scale(Q(1, 2), c8)),
            add(term(1, 0, "f12"), scale(-1, base12))),
        scale(Q(3, 4), mul(d, h)), scale(Q(3, 8), mul(e, e)),
        scale(Q(-1, 2), term(1, 0, "p")))
    g20_before = substitute_through(g[20], prefix + [relation18, relation19])
    expected_g20 = add(term(1, -4, "c20"), shift(-2, p20))
    assert desk.la_negative(g20_before) == expected_g20
    assert desk.la_operator(20, term(1, -4, "c20")) == {}

    relation20 = {
        "c20": {},
        "f12": add(base12, j),
        "p": add(scale(Q(3, 2), mul(b, j)), mul(c8, j),
                 scale(Q(3, 2), mul(d, h)), scale(Q(3, 4), mul(e, e)),
                 scale(-2, term(1, 2, "s"))),
    }
    assert desk.la_negative(substitute_through(g20_before, [relation20])) == {}

    c20_g20 = term(1, -4, "c20")
    c20_g21 = term(-1, -6, "c20")
    c20_predecessor = add(
        scale(-8, mul(desk.la_derivative(f1), c20_g20)),
        scale(-7, mul(f1, desk.la_derivative(c20_g20))))
    c20_same_row = desk.la_operator(21, c20_g21)
    assert c20_predecessor == term(12, -3, "a_x", "c20")
    assert c20_same_row == term(-12, -3, "a_x", "c20")
    assert add(c20_predecessor, c20_same_row) == {}

    p21 = add(
        mul(add(scale(Q(3, 4), b), scale(Q(1, 2), c8)),
            add(term(1, 0, "f13"), scale(-1, base13))),
        scale(Q(3, 4), mul(d, j)), scale(Q(3, 4), mul(e, h)),
        scale(Q(-1, 2), term(1, 0, "s")))
    g21_before = substitute_through(
        g[21], prefix + [relation18, relation19, relation20])
    assert desk.la_negative(g21_before) == shift(-2, p21)
    relation21 = {
        "f13": add(base13, k),
        "s": add(scale(Q(3, 2), mul(b, k)), mul(c8, k),
                 scale(Q(3, 2), mul(d, j)), scale(Q(3, 2), mul(e, h)),
                 scale(-2, term(1, 2, "u"))),
    }
    assert desk.la_negative(substitute_through(g21_before, [relation21])) == {}

    p22 = add(
        mul(add(scale(Q(3, 4), b), scale(Q(1, 2), c8)),
            add(term(1, 0, "f14"), scale(-1, base14))),
        scale(Q(3, 4), mul(d, k)), scale(Q(3, 4), mul(e, j)),
        scale(Q(3, 8), mul(h, h)), scale(Q(-1, 2), term(1, 0, "u")))
    all_relations = prefix + [relation18, relation19, relation20, relation21]
    g22_after = substitute_through(g[22], all_relations)
    assert desk.la_negative(g22_after) == shift(-2, p22)

    # Raw G22 is absent.  Since the characteristic coefficient would make
    # the homogeneous row vanish, the literal raw endpoint is -L22(g22).
    # Every term of g22 has A-exponent >= -2, so every term of this image is
    # divisible by A.  An optional homogeneous c22/A^5 is annihilated by L22
    # and cannot alter the conclusion.
    d22_raw = scale(-1, desk.la_operator(22, g22_after))
    assert desk.la_mod_a(1, d22_raw) == {}
    a_support_g22 = sorted({a_power for a_power, _ in g22_after})
    assert min(a_support_g22) == -2

    return {
        "defects": {
            "E": "F10-C*Z/4-Q^2/4-R*T/2-V*Y/16",
            "H": "F11-E*Z/2-Q*T/2-R*Y/2-C*V/8",
            "J": "F12-C*R-E*V/4-E*Z^2/16-3*H*Z/4-Q*Y/2-T^2/4",
            "K": "F13-C*Q-2*E*R-E*V*Z/16-3*H*V/8-3*H*Z^2/16-J*Z-T*Y/2",
            "ELL": (
                "F14-C*T-2*E*Q-E*R*Z/2-E*V^2/64-3*H*R-3*H*V*Z/16"
                "-H*Z^3/64-J*V/2-3*J*Z^2/8-5*K*Z/4-Y^2/4"
            ),
        },
        "relations": {
            "D18": "c18=0; (3*B+2*c8)*E/4+3*C^2/8-N/2=A^2*O",
            "D19": "(3*B+2*c8)*H/4+3*C*E/4-O/2=A^2*P",
            "D20": "c20=0; (3*B+2*c8)*J/4+3*C*H/4+3*E^2/8-P/2=A^2*S",
            "D21": "(3*B+2*c8)*K/4+3*C*J/4+3*E*H/4-S/2=A^2*U",
        },
        "polar_coefficients": {
            "g18_before_relation": desk.la_encode(expected_g18),
            "g19_before_relation": desk.la_encode(shift(-2, p19)),
            "g20_before_relation": desk.la_encode(expected_g20),
            "g21_before_relation": desk.la_encode(shift(-2, p21)),
            "g22_after_D21": desk.la_encode(shift(-2, p22)),
        },
        "linked_mode_firewalls": {
            "c18_at_D19": {
                "predecessor": desk.la_encode(c18_predecessor),
                "same_row": desk.la_encode(c18_same_row),
                "sum": desk.la_encode(add(c18_predecessor, c18_same_row)),
            },
            "c20_at_D21": {
                "predecessor": desk.la_encode(c20_predecessor),
                "same_row": desk.la_encode(c20_same_row),
                "sum": desk.la_encode(add(c20_predecessor, c20_same_row)),
            },
        },
        "endpoint": {
            "complete_g22_A_exponents": a_support_g22,
            "minimum_A_exponent": min(a_support_g22),
            "raw_identity": "D22_raw=-L22(g22)",
            "D22_raw_mod_A": desk.la_encode(desk.la_mod_a(1, d22_raw)),
            "conclusion": "D22_raw is in (A), so it cannot equal the target polynomial 1",
            "optional_c22_note": "L22(c22/A^5)=0, so an unrecorded endpoint homogeneous scalar changes nothing",
        },
    }


def calculate_result():
    assert digest(RAW) == RAW_SHA256
    prior, desk = load_dependencies()
    raw = json.loads(RAW.read_text())
    assert raw["variable_count"] == 303
    assert raw["generator_count"] == len(raw["generators"]) == 513
    assert raw["per_row"]["22"]["target"] == 1
    assert raw["windows"]["G"].get("22") is None
    assert raw["windows"]["F"].get("22") is None
    calculation = characteristic_calculation(desk)
    windows = {
        f"G{weight}": prior.literal_window_certificate(desk, raw, weight)
        for weight in range(18, 22)
    }
    assert [windows[f"G{weight}"]["rank"] for weight in range(18, 22)] == [5, 3, 2, 1]
    assert [windows[f"G{weight}"]["nullity"] for weight in range(18, 22)] == [0, 0, 0, 0]
    return {
        "schema": "jc2.ggv.upper_endpoint.uniform_d18_d22_fullmodes.result.v1",
        "status": "PASS_FIXED_UPPER_BRANCH_P_ENDPOINT_EMPTY_OVER_CHARACTERISTIC_ZERO_FIELDS",
        "source": {
            "authoritative_raw_system": str(RAW.relative_to(ROOT)),
            "authoritative_raw_system_sha256": RAW_SHA256,
            "predecessor_checker": str(PREDECESSOR.relative_to(ROOT)),
            "predecessor_checker_sha256": PREDECESSOR_SHA256,
            "predecessor_result": str(PREDECESSOR_RESULT.relative_to(ROOT)),
            "predecessor_result_sha256": PREDECESSOR_RESULT_SHA256,
            "raw_variable_count": 303,
            "raw_generator_count": 513,
            "row_sha256": {str(weight): raw["per_row"][str(weight)]["row_sha256"]
                            for weight in range(18, 23)},
            "row_targets": {str(weight): raw["per_row"][str(weight)]["target"]
                            for weight in range(18, 23)},
        },
        "calculation": calculation,
        "literal_raw_window_certificates": windows,
        "theorem": {
            "hypotheses": [
                "characteristic-zero field point of the complete fixed 303-variable branch-P fixture",
                "the independently checked D8--D17 complete-mode prefix",
                "all nine characteristic modes c4,c6,c8,c10,c12,c14,c16,c18,c20 retained causally",
                "literal raw G18--G21 degree windows and absent raw G22",
            ],
            "conclusion": (
                "no field point satisfies the fixed upper branch-P endpoint system: "
                "D4=...=D21=0 and D22=1"
            ),
            "proof_core": (
                "D18 and D20 kill c18 and c20 before their successor cancellations; "
                "D18--D21 give four exact A^2 quotient relations; the resulting complete "
                "g22 has pole order at most two, so the literal endpoint -L22(g22) lies "
                "in (A), contradicting target 1"
            ),
        },
        "scope_firewall": [
            "field-valued emptiness in characteristic zero, not scheme-theoretic ideal membership",
            "the fixed upper branch-P fixture only; no claim about other GGV branches or global JC2",
            "the result depends on the reviewed D8--D17 prefix and literal polynomial degree windows",
            "no truncated characteristic schedule is used; c16 is retained and may be nonzero",
            "c18 and c20 are killed by their birth-row polynomial windows, never by successor rows",
            "positive lower-window equations can only strengthen emptiness and are not discarded as existence evidence",
            "standard-library exact arithmetic only; no CAS, AWS, or jc2-lean state",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--dump", action="store_true")
    arguments = parser.parse_args()
    result = calculate_result()
    encoded = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if arguments.write:
        RESULT.write_bytes(encoded)
    if arguments.check:
        assert RESULT.read_bytes() == encoded
    if arguments.dump:
        print(encoded.decode(), end="")
    else:
        print(json.dumps({
            "status": result["status"],
            "relations": result["calculation"]["relations"],
            "endpoint": result["calculation"]["endpoint"],
            "check": arguments.check,
        }, sort_keys=True))


if __name__ == "__main__":
    main()
