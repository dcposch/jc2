#!/usr/bin/env python3
"""Exact desk-scale D3 raw-to-global interface prototype.

The first frozen input deliberately lacks a raw-to-Morse cleanup DAG.  The
compiler therefore stops before producing a typed E22, while independently
replaying quarantined polynomial reducer controls.  It uses only Fraction
arithmetic and sparse dictionaries; no CAS or probabilistic checks occur.
"""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASE = Path(__file__).resolve().parent

PINS = {
    "preregistration": (
        "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/PREREGISTRATION.md",
        "87fd708fa0e6d1a554724489d3b3b6065e2c6f89c1c1a11414a2ac0b147d4541",
    ),
    "r0_verifier": (
        "cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/verify.py",
        "ef9acfa90935b32e244367dada67ab35d6454f431f6d43dc35d144b3d08fe46c",
    ),
    "r0_result": (
        "cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/RESULT.json",
        "46e1b3434badcea007a914ec71bf60d9758ee76d312dc00d252342d52beed76d",
    ),
    "r0_freeze": (
        "cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/FREEZE.sha256",
        "6928428f9cc46641a80275e2bbfa62e784c4290ff041f5089ae789507fa8804f",
    ),
    "r0_review": (
        "xmodel/ggv-8_28-keller-face-cusp-jet-pinning-hostile-review-grok-20260827.md",
        "171ff47c844331da8971a731c1ffaf20c31ed5b2ba86fdee2d0d81219eb002b0",
    ),
    "r1_result": (
        "cases/ggv_8_28_keller_face_cusp_jet_pinning_r1_20260827/RESULT_R1.json",
        "392f6c0c3ca70a35b9b466944c243a927430838abe022eb960d7f2315e1684f3",
    ),
    "r1_freeze": (
        "cases/ggv_8_28_keller_face_cusp_jet_pinning_r1_20260827/FREEZE.sha256",
        "05cbb5c046f9aa4b89e1104448e77fd38ec3a146d2422bf84773f81d668bfe3c",
    ),
    "r1_review": (
        "xmodel/ggv-8_28-keller-face-cusp-jet-pinning-r1-hostile-review-grok-20260827.md",
        "d40cd78f4f0afc12d09f8d1e99724de9fd5125fddc064089d6ca0870c7d777e0",
    ),
    "r2_result": (
        "cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/RESULT_R2.json",
        "0dffbb36c20d0b80498d765168a47cdb9ed2889ffc7bd105dce7ec835f600b1d",
    ),
    "r2_freeze": (
        "cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/FREEZE.sha256",
        "453f7821f88add5d97b65cee41fe3a4df225db5768526746cf4ff1431aa73aa6",
    ),
    "r2_review": (
        "xmodel/ggv-8_28-keller-face-cusp-unit-carrier-classification-r2-hostile-review-grok-20260827.md",
        "b271a2958138d8e85c0a8cab068efd7bfa59227a56e5252eb27310a50fb11e24",
    ),
    "r3_result_scope_firewall": (
        "cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/RESULT_R3.json",
        "3d69dfbd6c0e28afafdfc7bbb0cf4ebe57d8522938ddd46b418f71123c1da006",
    ),
    "r3_review_scope_firewall": (
        "xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-hostile-review-grok-20260827.md",
        "27fcd25640f62a92c147863e7a8ef8ca4b7b004f05d54450c8d2d8811c97cdc6",
    ),
    "m_cokernel_audit": (
        "xmodel/ggv-8_28-M-cokernel-seven-vector-hostile-audit-sol2-20260827.md",
        "2803b705d41b332cabd12249b0a0be17cdd18e8f2f251fe7b242bf55fc9bb289",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def qstr(x: Q) -> str:
    return str(Q(x))


# Sparse univariate Q[X], exponent -> coefficient.
def clean(p):
    return {int(i): Q(c) for i, c in p.items() if Q(c)}


def padd(a, b):
    out = dict(a)
    for i, c in b.items():
        out[i] = out.get(i, Q(0)) + c
        if not out[i]:
            del out[i]
    return out


def pscale(a, c):
    return clean({i: Q(c) * x for i, x in a.items()})


def psub(a, b):
    return padd(a, pscale(b, -1))


def pmul(a, b):
    out = {}
    for i, a_i in a.items():
        for j, b_j in b.items():
            out[i + j] = out.get(i + j, Q(0)) + a_i * b_j
    return clean(out)


def pder(a):
    return clean({i - 1: Q(i) * c for i, c in a.items() if i})


def pencode(a):
    return [{"X_degree": i, "coefficient": qstr(a[i])} for i in sorted(a)]


H = {0: Q(-1), 8: Q(1)}
HP = pder(H)


def M(y):
    return padd(pscale(pmul(H, pder(y)), 4), pscale(pmul(HP, y), 6))


def reduce_mod_M(p):
    work = clean(p)
    quotient = {}
    trace = []
    while work and max(work) >= 7:
        m = max(work)
        c = work[m] / Q(4 * (m + 5))
        y_degree = m - 7
        quotient[y_degree] = quotient.get(y_degree, Q(0)) + c
        before = work[m]
        work = psub(work, pscale(M({y_degree: Q(1)}), c))
        trace.append(
            {
                "cancelled_X_degree": m,
                "leading_coefficient": qstr(before),
                "subtract_M_of": {"X_degree": y_degree, "coefficient": qstr(c)},
            }
        )
    quotient = clean(quotient)
    remainder = clean(work)
    assert padd(M(quotient), remainder) == clean(p)
    assert all(i <= 6 for i in remainder)
    vector = [qstr(remainder.get(i, Q(0))) for i in range(7)]
    return {
        "input": pencode(p),
        "preimage_Y": pencode(quotient),
        "remainder": pencode(remainder),
        "seven_vector_X0_through_X6": vector,
        "steps": trace,
        "replay": "P == M(Y) + remainder",
    }


# Sparse Q[x,y], pair -> coefficient, used only for the frozen R0 face.
def xyadd(a, b):
    out = dict(a)
    for ij, c in b.items():
        out[ij] = out.get(ij, Q(0)) + c
        if not out[ij]:
            del out[ij]
    return out


def xymul(a, b):
    out = {}
    for (i, j), a_ij in a.items():
        for (k, l), b_kl in b.items():
            out[i + k, j + l] = out.get((i + k, j + l), Q(0)) + a_ij * b_kl
    return {ij: c for ij, c in out.items() if c}


def xypow(a, n):
    out = {(0, 0): Q(1)}
    for _ in range(n):
        out = xymul(out, a)
    return out


def ceil_div(a, b):
    return -((-a) // b)


def raw_slice(kind, n):
    if kind == "F":
        shift, max_i, prefix = 8, 16, "f"
    elif kind == "G":
        shift, max_i, prefix = 12, 24, "g"
    else:
        raise AssertionError(kind)
    lo = max(0, ceil_div(n - shift, 3))
    hi = max_i - n
    out = []
    if lo <= hi:
        for i in range(lo, hi + 1):
            j = shift + 3 * i - n
            assert i >= 0 and j >= max(0, 4 * i - shift) and j <= 3 * i + shift
            out.append(
                {
                    "slot": f"{prefix}_{i}_{j}",
                    "weight": n,
                    "raw_exponents": {"x": i, "y": j},
                    "raw_monomial": f"x^{i}*y^{j}",
                    "chart_image": f"t^{n}*X^{i}",
                }
            )
    return out


def polygon_slots_through_22(kind):
    """Independent literal lattice enumeration, used to audit raw_slice."""
    if kind == "F":
        shift, max_i, prefix = 8, 16, "f"
    elif kind == "G":
        shift, max_i, prefix = 12, 24, "g"
    else:
        raise AssertionError(kind)
    out = set()
    for i in range(max_i + 1):
        for j in range(max(0, 4 * i - shift), 3 * i + shift + 1):
            n = shift + 3 * i - j
            if 0 <= n <= 22:
                out.add((n, f"{prefix}_{i}_{j}", i, j))
    return out


def artificial_face_assignment():
    z_minus_1 = {(1, 4): Q(1), (0, 0): Q(-1)}
    Bxy = xymul({(1, 0): Q(1)}, xypow(z_minus_1, 7))
    B2, B3 = xypow(Bxy, 2), xypow(Bxy, 3)
    fface = xyadd(B2, {(8, 32): Q(-2), (0, 8): Q(1)})
    gface = xyadd(B3, {(16, 60): Q(-3), (8, 36): Q(3), (0, 12): Q(-1)})

    def encode(kind, poly, shift):
        out = []
        for (i, j), c in sorted(poly.items()):
            n = shift + 3 * i - j
            assert 0 <= n <= 22
            expected = {s["slot"]: s for s in raw_slice(kind, n)}
            slot = ("f" if kind == "F" else "g") + f"_{i}_{j}"
            assert slot in expected
            out.append(
                {
                    "slot": slot,
                    "coefficient": qstr(c),
                    "weight": n,
                    "raw_exponents": {"x": i, "y": j},
                    "chart_image": f"{qstr(c)}*t^{n}*X^{i}",
                }
            )
        return out

    return {
        "scope": "literal artificial R0 face assignment; separate from the local cusp fixture",
        "formula": {
            "B": "x*(x*y^4-1)^7",
            "f": "B^2-2*x^8*y^32+y^8",
            "g": "B^3-3*x^16*y^60+3*x^8*y^36-y^12",
        },
        "F_nonzero_slots": encode("F", fface, 8),
        "G_nonzero_slots": encode("G", gface, 12),
        "join_to_local_cusp_fixture": "ABSENT: no serialized raw-to-Morse cleanup map",
    }


FACTORS = [
    {"factor_id": "fac_X_minus_1", "polynomial": "X-1", "degree": 1},
    {"factor_id": "fac_X_plus_1", "polynomial": "X+1", "degree": 1},
    {"factor_id": "fac_X2_plus_1", "polynomial": "X^2+1", "degree": 2},
    {"factor_id": "fac_X4_plus_1", "polynomial": "X^4+1", "degree": 4},
]


def build_source():
    raw = {kind: [s for n in range(23) for s in raw_slice(kind, n)] for kind in ("F", "G")}
    for kind in ("F", "G"):
        sliced = {
            (s["weight"], s["slot"], s["raw_exponents"]["x"], s["raw_exponents"]["y"])
            for s in raw[kind]
        }
        assert sliced == polygon_slots_through_22(kind)
    assert len(raw["F"]) == 141
    assert len(raw["G"]) == 301
    f14 = raw_slice("F", 14)
    assert [(s["raw_exponents"]["x"], s["raw_exponents"]["y"]) for s in f14] == [(2, 0)]
    assert raw_slice("G", 22) == []

    return {
        "schema": "GGV-8_28-D3-RAW-TO-GLOBAL-v1",
        "control_id": "R0_ARTIFICIAL_CUSP_CONTROL",
        "scope": "artificial frozen control only; symbolic raw 2S/3S slots through weight 22",
        "ambient": {
            "raw": "Q[f_i_j,g_i_j] on the listed 2S/3S slots",
            "chart": "Q[t,X]",
            "local": "kappa_p[[t,u]] for each listed factor p",
            "global_endpoint": "Q[X]",
            "cokernel": "Q[X]/im(M) as a Q-vector-space quotient, represented by Q[X]_{<=6}",
        },
        "maps": {
            "F_raw_to_chart": "x^i*y^j -> t^(8+3*i-j)*X^i",
            "G_raw_to_chart": "x^i*y^j -> t^(12+3*i-j)*X^i",
            "local_orientation": "u=H mod t",
            "local_determinant": "u_X(c,0)=H'(c)",
            "M": "Y -> 4*(X^8-1)*Y' + 48*X^7*Y",
        },
        "factor_registry": FACTORS,
        "raw_slots_through_weight_22": raw,
        "literal_artificial_raw_face": artificial_face_assignment(),
        "formal_root_sign_packets": {
            "scope": "R0 formal packets, retained only as factor/deck-tag controls; polynomial source rejected in R0",
            "S_plus": {
                "factor_signs": {"fac_X_minus_1": 1, "fac_X_plus_1": -1, "fac_X2_plus_1": 1, "fac_X4_plus_1": 1},
                "deck_tag": "R0:S_plus",
                "orientation_tag": "u=H mod t",
                "polynomial_source_status": "REJECTED",
            },
            "S_minus": {
                "factor_signs": {"fac_X_minus_1": 1, "fac_X_plus_1": -1, "fac_X2_plus_1": 1, "fac_X4_plus_1": -1},
                "deck_tag": "R0:S_minus",
                "orientation_tag": "u=H mod t",
                "polynomial_source_status": "REJECTED",
            },
        },
        "local_carrier_fixture": {
            "scope": "R0 hand-specified rootwise fixture; not a raw descendant",
            "V8": "1/48",
            "U11": "UNSPECIFIED_AND_INACTIVE_IN_THIS_V8_NONZERO_FIXTURE",
            "U14": "X",
            "higher_u_sidecars": "UNSERIALIZED",
            "branch_by_factor": {f["factor_id"]: "V8_NONZERO__V8_U14" for f in FACTORS},
            "orientation_tag": "u=H mod t",
            "determinant_tag": "H'(c)",
            "deck_tag": "ORIENTED_PLUS_H",
            "raw_to_morse": {
                "status": "ABSENT_IN_FROZEN_R0_R1_R2_INPUT",
                "required_but_absent": "cleanup_DAG",
            },
        },
        "quarantined_global_polynomial_control": {
            "scope": "hand-specified R0/R1 polynomial identity; reducer positive control only",
            "E22": "1+(13/12)*(X^8-1)",
            "preimage": "X/48",
            "raw_descendant": False,
        },
        "firewalls": {
            "branch_bits": "do not determine E22 or its seven-vector",
            "H_multiple": "fully live; r o (H*) is an isomorphism on Q[X]_{<=6}",
            "r3": "scope firewall only; not consumed as a source pair",
            "claims_not_made": ["8_28 face/family exclusion", "G2-PSC", "G2-BD", "Keller pair", "JC2"],
        },
    }


def validate_source(source):
    expected = build_source()
    assert source == expected, "source differs from the deterministic frozen artificial control"
    ids = {f["factor_id"] for f in source["factor_registry"]}
    assert ids == {"fac_X_minus_1", "fac_X_plus_1", "fac_X2_plus_1", "fac_X4_plus_1"}
    fixture = source["local_carrier_fixture"]
    assert fixture["orientation_tag"] == "u=H mod t"
    assert fixture["determinant_tag"] == "H'(c)"
    assert fixture["deck_tag"] == "ORIENTED_PLUS_H"
    assert set(fixture["branch_by_factor"]) == ids
    for packet in source["formal_root_sign_packets"].values():
        if isinstance(packet, dict) and "factor_signs" in packet:
            assert set(packet["factor_signs"]) == ids
            assert packet["orientation_tag"] == "u=H mod t"


def first_type_failure(source):
    fixture = source.get("local_carrier_fixture", {})
    raw_to_morse = fixture.get("raw_to_morse", {})
    if "cleanup_DAG" not in raw_to_morse:
        return {
            "path": "local_carrier_fixture.raw_to_morse.cleanup_DAG",
            "expected_type": "serialized exact derivation DAG from named raw slots through formal cleanup",
            "observed": raw_to_morse.get("status", "MISSING"),
            "smallest_concrete_witness": {
                "local_value": "U14=X",
                "literal_raw_F14_slice": [s["chart_image"] for s in raw_slice("F", 14)],
                "R1_conclusion": "raw F14 contains only X^2; U14=X is not a direct raw row",
                "needed_repair": "a source-pinned nonlinear cleanup DAG (including sidecars) deriving U14, or a proof that no such derivation exists",
            },
        }
    # Future versions must add an evaluator before this path can promote.
    return {
        "path": "compiler.cleanup_DAG_evaluator",
        "expected_type": "exact evaluator plus gluing replay",
        "observed": "NOT_IMPLEMENTED_IN_v1",
    }


def mutation_controls(source):
    # Slice mutation: X is not a legal raw F14 monomial.
    legal_f14 = {(s["raw_exponents"]["x"], s["raw_exponents"]["y"]) for s in raw_slice("F", 14)}
    assert (1, -3) not in legal_f14

    bad_orientation = copy.deepcopy(source)
    del bad_orientation["local_carrier_fixture"]["orientation_tag"]
    orientation_rejected = "orientation_tag" not in bad_orientation["local_carrier_fixture"]
    assert orientation_rejected

    bad_factor = copy.deepcopy(source)
    del bad_factor["local_carrier_fixture"]["branch_by_factor"]["fac_X4_plus_1"]
    factor_rejected = set(bad_factor["local_carrier_fixture"]["branch_by_factor"]) != {
        f["factor_id"] for f in FACTORS
    }
    assert factor_rejected

    bad_fixture = padd({0: Q(1)}, H)  # coefficient 1 instead of 13/12.
    bad_reduction = reduce_mod_M(bad_fixture)
    assert bad_reduction["seven_vector_X0_through_X6"] != ["0"] * 7

    return {
        "illegal_raw_F14_X": "REJECTED: would require raw x*y^-3, not a 2S lattice point",
        "dropped_orientation_tag": "REJECTED" if orientation_rejected else "FAILED_TO_REJECT",
        "dropped_factor_tag": "REJECTED" if factor_rejected else "FAILED_TO_REJECT",
        "changed_13_over_12_to_1": {
            "status": "NONZERO_REMAINDER_DETECTED",
            "seven_vector": bad_reduction["seven_vector_X0_through_X6"],
        },
    }


def compile_result(source_bytes, source):
    validate_source(source)
    observed_pins = {}
    for key, (rel, expected) in PINS.items():
        got = sha256(ROOT / rel)
        assert got == expected, (key, got, expected)
        observed_pins[key] = {"path": rel, "sha256": got}

    failure = first_type_failure(source)
    assert failure["path"] == "local_carrier_fixture.raw_to_morse.cleanup_DAG"

    fixture_E22 = padd({0: Q(1)}, pscale(H, Q(13, 12)))
    fixture_reduction = reduce_mod_M(fixture_E22)
    assert fixture_reduction["seven_vector_X0_through_X6"] == ["0"] * 7
    assert fixture_reduction["preimage_Y"] == [{"X_degree": 1, "coefficient": "1/48"}]
    one_reduction = reduce_mod_M({0: Q(1)})
    assert one_reduction["seven_vector_X0_through_X6"] == ["1", "0", "0", "0", "0", "0", "0"]

    h_basis = []
    for i in range(7):
        red = reduce_mod_M(pmul(H, {i: Q(1)}))
        expected = ["0"] * 7
        expected[i] = qstr(Q(-12, i + 13))
        assert red["seven_vector_X0_through_X6"] == expected
        h_basis.append({"input": f"H*X^{i}", "seven_vector": expected})

    result = {
        "status": "STOP-FIRST-MISSING-PROVENANCE",
        "scope": "artificial frozen R0 control only; interface/type obstruction, not a face exclusion",
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "pins": observed_pins,
        "raw_census": {
            "F_slots_through_weight_22": len(source["raw_slots_through_weight_22"]["F"]),
            "G_slots_through_weight_22": len(source["raw_slots_through_weight_22"]["G"]),
            "total_slots": sum(len(source["raw_slots_through_weight_22"][k]) for k in ("F", "G")),
            "F14": [s["chart_image"] for s in raw_slice("F", 14)],
            "G21": [s["chart_image"] for s in raw_slice("G", 21)],
            "G22": [s["chart_image"] for s in raw_slice("G", 22)],
            "literal_face_nonzero_F": len(source["literal_artificial_raw_face"]["F_nonzero_slots"]),
            "literal_face_nonzero_G": len(source["literal_artificial_raw_face"]["G_nonzero_slots"]),
        },
        "typed_compilation": {
            "global_E22": None,
            "seven_vector": None,
            "first_missing_provenance_field": failure,
            "reason_no_output": "the explicit R0 polynomial control is quarantined and cannot substitute for a raw-to-Morse derivation",
        },
        "preserved_tags": {
            "factors": source["factor_registry"],
            "orientation": source["local_carrier_fixture"]["orientation_tag"],
            "determinant": source["local_carrier_fixture"]["determinant_tag"],
            "deck": source["local_carrier_fixture"]["deck_tag"],
            "factorwise_branches": source["local_carrier_fixture"]["branch_by_factor"],
        },
        "quarantined_reducer_controls": {
            "fixture_1_plus_13H_over_12": fixture_reduction,
            "one": one_reduction,
            "H_times_basis": h_basis,
            "H_action_matrix": {
                "basis": [f"X^{i}" for i in range(7)],
                "diagonal": [qstr(Q(-12, i + 13)) for i in range(7)],
                "determinant_nonzero": True,
                "consequence": "the global H-multiple can move every cokernel coordinate",
            },
        },
        "mutations": mutation_controls(source),
        "firewall": {
            "sixteen_branch_bits_determine_E22": False,
            "H_multiple_status": "FULLY_LIVE",
            "r3_consumed_as_source": False,
            "claims_not_made": ["8_28 face/family exclusion", "G2-PSC", "G2-BD", "Keller pair", "counterexample", "JC2"],
        },
    }
    assert result["raw_census"] == {
        "F_slots_through_weight_22": 141,
        "G_slots_through_weight_22": 301,
        "total_slots": 442,
        "F14": ["t^14*X^2"],
        "G21": ["t^21*X^3"],
        "G22": [],
        "literal_face_nonzero_F": len(source["literal_artificial_raw_face"]["F_nonzero_slots"]),
        "literal_face_nonzero_G": len(source["literal_artificial_raw_face"]["G_nonzero_slots"]),
    }
    return result


def dump(obj):
    return json.dumps(obj, sort_keys=True, indent=2) + "\n"


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--print-source":
        print(dump(build_source()), end="")
        return
    if len(sys.argv) == 3 and sys.argv[1] == "--print-result":
        source_path = Path(sys.argv[2])
        source_bytes = source_path.read_bytes()
        source = json.loads(source_bytes)
        print(dump(compile_result(source_bytes, source)), end="")
        return
    if len(sys.argv) == 4 and sys.argv[1] == "--check":
        source_path, result_path = Path(sys.argv[2]), Path(sys.argv[3])
        source_bytes = source_path.read_bytes()
        source = json.loads(source_bytes)
        expected_source = dump(build_source()).encode()
        assert source_bytes == expected_source
        expected_result = dump(compile_result(source_bytes, source)).encode()
        assert result_path.read_bytes() == expected_result
        print("PASS D3 exact source/result replay")
        return
    raise SystemExit("usage: compile_d3.py --print-source | --print-result SOURCE | --check SOURCE RESULT")


if __name__ == "__main__":
    main()
