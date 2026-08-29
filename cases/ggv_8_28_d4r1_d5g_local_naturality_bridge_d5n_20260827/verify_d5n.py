#!/usr/bin/env python3
"""Exact typed D4R1 -> D5G local-naturality bridge D5N."""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASE = Path(__file__).resolve().parent

PINS = {
    "preregistration": (
        "cases/ggv_8_28_d4r1_d5g_local_naturality_bridge_d5n_20260827/PREREGISTRATION.md",
        "a510494e8c0862e0886f9c1c31ff2e042be5e26ca5c8f4b42c6bdb96b1f5d6de",
    ),
    "d3_raw": (
        "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json",
        "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
    ),
    "d4r1_freeze": (
        "cases/ggv_8_28_raw_to_morse_cleanup_dag_d4r1_20260827/FREEZE.sha256",
        "6beafdb470ec9c4c88fd8c6e3d2ccaf3b4312c477ddabc4576203f7e9c19c954",
    ),
    "d4r1_result": (
        "cases/ggv_8_28_raw_to_morse_cleanup_dag_d4r1_20260827/RESULT.json",
        "83c107b77af8aa395fa38199af84f37aba44b262e01ac397a554c7f1dfdba0f2",
    ),
    "d4r1_review": (
        "xmodel/ggv-8_28-raw-to-morse-cleanup-dag-d4r1-hostile-review-fable5-20260827.md",
        "971816d00b50070cb32f3069a06303f1aea0c02e87efeb54447310bf110ec004",
    ),
    "d5_design_freeze": (
        "cases/ggv_8_28_factor_etale_global_e22_gluing_d5_design_20260827/FREEZE.sha256",
        "9954063b99931a37dc7df2bd56e82570d6a2d0f036d995d2a95e19d109cf47ce",
    ),
    "d5g_freeze": (
        "cases/ggv_8_28_raw_global_determinant_d5g_20260827/FREEZE.sha256",
        "838b1160f3ddf38fcbf360bd200ee2057e72da2b1b0ba8788d43b83720cdd043",
    ),
    "d5g_direct": (
        "cases/ggv_8_28_raw_global_determinant_d5g_20260827/DIRECT_DETERMINANT.json",
        "069ab7a5fdb133aa2ffb0063e5f36c5664a070798de6ea00520698207e24838d",
    ),
    "d5g_certificate": (
        "cases/ggv_8_28_raw_global_determinant_d5g_20260827/D22_CERTIFICATE.json",
        "6346ab6afb307fea83516f742ca53b90e5eb8d42c2e1d5bef083920de23e434a",
    ),
    "d5g_review": (
        "xmodel/ggv-8_28-raw-global-determinant-d5g-hostile-audit-sol-ultra-20260827.md",
        "14913814fce76629836da359f630727b92167d3a23912c9fa265ac8d71f800d2",
    ),
    "d5g_review_freeze": (
        "cases/ggv_8_28_raw_global_determinant_d5g_hostile_audit_20260827/FREEZE.sha256",
        "e51084fbc89e97b5184ff5b2538afc46135f0c295ba243fffe3f3c008560afa3",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compact(obj) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode()


def pretty(obj) -> bytes:
    return (json.dumps(obj, sort_keys=True, indent=2) + "\n").encode()


# Sparse Q-polynomial in named differential indeterminates.  A monomial is a
# sorted tuple with repetition; this is used only for the universal chain-rule
# certificate and is independent of either producer implementation.
def fadd(a, b):
    out = dict(a)
    for monomial, coefficient in b.items():
        out[monomial] = out.get(monomial, Q(0)) + coefficient
        if not out[monomial]:
            del out[monomial]
    return out


def fscale(a, scalar):
    return {m: Q(scalar) * c for m, c in a.items() if Q(scalar) * c}


def fmul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            monomial = tuple(sorted(ma + mb))
            out[monomial] = out.get(monomial, Q(0)) + ca * cb
    return {m: c for m, c in out.items() if c}


def fvar(name):
    return {(name,): Q(1)}


def fencode(poly):
    return [[list(monomial), str(coefficient)] for monomial, coefficient in sorted(poly.items())]


def specialize_zero(poly, variable):
    return {m: c for m, c in poly.items() if variable not in m}


def universal_chain_rule_certificate():
    t, u, ux, ut = map(fvar, ("t", "u", "u_X", "u_t"))
    U, Ud = map(fvar, ("U", "U_t"))
    G, Gu, Gt = map(fvar, ("G", "G_u", "G_t_at_u"))

    F = fadd(U, fmul(u, u))
    Fx = fscale(fmul(u, ux), 2)
    Ft = fadd(Ud, fscale(fmul(u, ut), 2))
    Gx = fmul(Gu, ux)
    Gt_at_x = fadd(Gt, fmul(Gu, ut))
    E = fadd(
        fadd(fscale(fmul(Fx, G), 12), fscale(fmul(F, Gx), -8)),
        fscale(fmul(t, fadd(fmul(Fx, Gt_at_x), fscale(fmul(Ft, Gx), -1))), -1),
    )
    local_bracket = fadd(
        fadd(fscale(fmul(u, G), 24), fscale(fmul(F, Gu), -8)),
        fscale(fmul(t, fadd(fscale(fmul(u, Gt), 2), fscale(fmul(Ud, Gu), -1))), -1),
    )
    factored = fmul(ux, local_bracket)
    assert E == factored

    at_u0 = specialize_zero(E, "u")
    expected_at_u0 = fmul(fmul(ux, Gu), fadd(fmul(t, Ud), fscale(U, -8)))
    assert at_u0 == expected_at_u0
    return {
        "ring": "Q[t,u,u_X,u_t,U,U_t,G,G_u,G_t_at_u]",
        "identity": "E=u_X*(24*u*G-8*(U+u^2)*G_u-t*(2*u*G_t_at_u-U_t*G_u))",
        "constant_channel": "E|_(u=0)=u_X*G_u*(t*U_t-8*U)",
        "expanded_E": fencode(E),
        "expanded_E_sha256": hashlib.sha256(compact(fencode(E))).hexdigest(),
        "u_t_cancellation": "PASS-EXACT-FREE-RING",
        "constant_channel_replay": "PASS-EXACT-FREE-RING",
    }


# Sparse C[X], with C-monomials represented by sorted raw-slot tuples.
def decode_x(items):
    out = {}
    for raw_vars, x_degree, coefficient in items:
        key = (tuple(raw_vars), int(x_degree))
        out[key] = out.get(key, Q(0)) + Q(coefficient)
        if not out[key]:
            del out[key]
    return out


def xadd(a, b):
    out = dict(a)
    for key, coefficient in b.items():
        out[key] = out.get(key, Q(0)) + coefficient
        if not out[key]:
            del out[key]
    return out


def xscale(a, scalar):
    return {key: Q(scalar) * coefficient for key, coefficient in a.items() if Q(scalar) * coefficient}


def xmul(a, b):
    out = {}
    for (va, xa), ca in a.items():
        for (vb, xb), cb in b.items():
            key = (tuple(sorted(va + vb)), xa + xb)
            out[key] = out.get(key, Q(0)) + ca * cb
    return {key: coefficient for key, coefficient in out.items() if coefficient}


H = {((), 0): Q(-1), ((), 8): Q(1)}


def coefficient_groups(terms):
    groups = {}
    for raw_vars, x_degree, coefficient in terms:
        groups.setdefault(int(x_degree), []).append([raw_vars, str(Q(coefficient))])
    return {degree: sorted(items) for degree, items in groups.items()}


def lower_gate(direct, raw_alphabet):
    rows = []
    total_generators = 0
    total_terms = 0
    for n in range(22):
        item = direct["D"][n]
        assert item["weight"] == n
        assert item["term_count"] == len(item["terms"])
        for raw_vars, _, _ in item["terms"]:
            assert set(raw_vars) <= raw_alphabet
        groups = coefficient_groups(item["terms"])
        generators = []
        for degree in sorted(groups):
            encoded = groups[degree]
            generators.append({
                "X_degree": degree,
                "term_count": len(encoded),
                "coefficient_sha256": hashlib.sha256(compact(encoded)).hexdigest(),
                "source_pointer": f"DIRECT_DETERMINANT.json:D[{n}].terms[X_degree={degree}]",
            })
        total_generators += len(generators)
        total_terms += len(item["terms"])
        rows.append({
            "weight": n,
            "identically_zero_in_CX": not item["terms"],
            "term_count": len(item["terms"]),
            "coefficient_generator_count": len(generators),
            "terms_sha256": hashlib.sha256(compact(item["terms"])).hexdigest(),
            "coefficient_generators": generators,
        })
    assert rows[0]["identically_zero_in_CX"]
    assert all(not row["identically_zero_in_CX"] for row in rows[1:])
    return {
        "ideal": "I_<22=(all X-coefficients of D0,...,D21) in C",
        "rows": rows,
        "row_count": 22,
        "nontrivial_row_count": 21,
        "coefficient_generator_count": total_generators,
        "source_term_count": total_terms,
        "current_generic_status": "UNSATISFIED: D1,...,D21 are nonzero generic polynomials",
        "allowed_use": "formal base change C -> Cbar=C/I_<22; no point or properness is asserted",
        "endpoint_simplification_guard": "REQUIRE all listed coefficient generators map to zero",
    }


def local_recipe(d4_result):
    outputs = d4_result["outputs"]
    required = ["critical_shift_s", "U", "coordinate_q0", "inverse_alpha", "V"]
    for name in required:
        assert sorted(map(int, outputs[name].keys())) == list(range(23))
    C_coefficients = []
    for n in range(23):
        terms = []
        for i in range(n + 1):
            j = n - i
            scalar = j - 8
            if scalar:
                terms.append({
                    "V_weight": i,
                    "V_node": outputs["V"][str(i)],
                    "U_weight": j,
                    "U_node": outputs["U"][str(j)],
                    "scalar": scalar,
                })
        C_coefficients.append({"weight": n, "terms": terms})
    local_product = []
    for n in range(23):
        local_product.append({
            "weight": n,
            "convolution": [
                {"q0_weight": i, "q0_node": outputs["coordinate_q0"][str(i)], "C_weight": n - i}
                for i in range(n + 1)
            ],
        })
    return {
        "source_output_roots": {name: outputs[name] for name in required},
        "C_definition": "C=V*(t*U'-8*U)",
        "C_coefficients": C_coefficients,
        "q0_times_C_coefficients": local_product,
        "closed_fibre": {
            "s0": d4_result["closed_fibre_checks"]["s0"],
            "U0": d4_result["closed_fibre_checks"]["U0"],
            "V0": d4_result["closed_fibre_checks"]["V0"],
            "q0_0": "H'(c)=8*c^7 (reviewed D4R1 orientation)",
        },
    }


def build_result():
    observed = {}
    for key, (relative, expected) in PINS.items():
        got = sha256(ROOT / relative)
        assert got == expected, (key, got, expected)
        observed[key] = {"path": relative, "sha256": got}

    source = json.loads((ROOT / PINS["d3_raw"][0]).read_bytes())
    d4_result = json.loads((ROOT / PINS["d4r1_result"][0]).read_bytes())
    direct = json.loads((ROOT / PINS["d5g_direct"][0]).read_bytes())
    certificate = json.loads((ROOT / PINS["d5g_certificate"][0]).read_bytes())

    raw_slots = sorted(
        slot["slot"]
        for kind in ("F", "G")
        for slot in source["raw_slots_through_weight_22"][kind]
        if slot["weight"] > 0
    )
    assert len(raw_slots) == 400 and len(set(raw_slots)) == 400
    raw_alphabet = set(raw_slots)
    assert d4_result["dag"]["raw_leaf_count"] == 400
    assert direct["ring"] == "C[X], C=Q[400 positive-weight D3 raw slots]"
    direct_visible = {
        slot
        for item in direct["D"]
        for raw_vars, _, _ in item["terms"]
        for slot in raw_vars
    }
    determinant_kernel_slots = sorted(raw_alphabet - direct_visible)
    assert len(direct_visible) == 398
    assert determinant_kernel_slots == ["f_0_0", "g_0_0"]

    # Exact direct quotient/remainder replay, independently of D5G's compiler.
    D22 = decode_x(direct["D"][22]["terms"])
    assert D22 == decode_x(certificate["D22"])
    Q22 = decode_x(certificate["H_division"]["Q22"])
    R22 = decode_x(certificate["H_division"]["R22"])
    assert xadd(xmul(H, Q22), R22) == D22
    assert max(x_degree for _, x_degree in R22) < 8
    mutated = xadd(D22, H)
    Qmut = decode_x(certificate["H_mutation"]["Q22_mutated"])
    Rmut = decode_x(certificate["H_mutation"]["R22_mutated"])
    assert mutated == decode_x(certificate["H_mutation"]["mutated_D22"])
    assert Rmut == R22
    assert Qmut == xadd(Q22, {((), 0): Q(1)})

    factor_registry = source["factor_registry"]
    assert [(item["factor_id"], item["polynomial"]) for item in factor_registry] == [
        ("fac_X_minus_1", "X-1"),
        ("fac_X_plus_1", "X+1"),
        ("fac_X2_plus_1", "X^2+1"),
        ("fac_X4_plus_1", "X^4+1"),
    ]
    factor_polynomials = [
        {((), 1): Q(1), ((), 0): Q(-1)},
        {((), 1): Q(1), ((), 0): Q(1)},
        {((), 2): Q(1), ((), 0): Q(1)},
        {((), 4): Q(1), ((), 0): Q(1)},
    ]
    factor_product = {((), 0): Q(1)}
    for factor in factor_polynomials:
        factor_product = xmul(factor_product, factor)
    assert factor_product == H
    assert d4_result["tags"]["factor_ids"] == [item["factor_id"] for item in factor_registry]
    assert d4_result["tags"]["orientation"] == "u=H mod t"
    assert d4_result["tags"]["deck"] == "ORIENTED_PLUS_H"
    assert not d4_result["tags"]["global_polynomial_automorphism_claim"]

    chain = universal_chain_rule_certificate()
    gate = lower_gate(direct, raw_alphabet)
    local = local_recipe(d4_result)

    return {
        "status": "PASS-D5N-EXACT-TYPED-LOCAL-NATURALITY-BRIDGE-NO-TARGET-VERDICT",
        "scope": "reviewed D4R1 factor-local outputs mapped to reviewed D5G direct determinant through weight 22, with complete lower-row quotient gate and global H-multiple custody",
        "pins": observed,
        "rings": {
            "raw": "C=Q[400 named positive-weight D3 raw slots]",
            "direct": "S=C[X,t]/(t^23)",
            "factor_etale": "A=C[c]/(c^8-1)",
            "lower_quotient": "Cbar=C/I_<22",
        },
        "maps": {
            "ev_xi": {
                "domain": "C[X,t]/(t^23)",
                "codomain": "A[[t]]/(t^23)",
                "raw_slot": "same named D4R1 raw leaf",
                "t": "t",
                "X": "c+s(t)",
                "s_roots": d4_result["outputs"]["critical_shift_s"],
            },
            "reduction_mod_H": "C[X] -> C[c]/(c^8-1), X |-> c",
            "tagged_factor_projection": factor_registry,
            "monic_division": "D22 |-> (R22,Q22), D22=H*Q22+R22, deg R22<8",
        },
        "raw_alphabet": {
            "count": len(raw_slots),
            "sha256": hashlib.sha256(compact(raw_slots)).hexdigest(),
            "D4R1_leaf_count": d4_result["dag"]["raw_leaf_count"],
            "D5G_ring_count": 400,
            "D5G_visible_slot_count": len(direct_visible),
            "determinant_kernel_slots": determinant_kernel_slots,
            "kernel_explanation": "f_0_0 has weight i=8 and coefficient (i-8)=0; g_0_0 has weight j=12 and coefficient (12-j)=0",
            "status": "EXACT-NAME-PRESERVING-COMMON-SOURCE",
        },
        "universal_chain_rule": chain,
        "local_constant_channel": local,
        "full_naturality": {
            "identity": "ev_xi(sum_(n=0)^22 D_n(X)t^n)=q0*V*(t*U'-8*U) mod t^23",
            "derivation": [
                "reviewed D5G identifies sum D_n t^n with E(F,G)",
                "ev_xi is the same-raw-leaf substitution X=c+s(t)",
                "reviewed D4R1 gives F=U+u^2, q0=u_X|u=0, V=G_u|u=0",
                "the independently replayed free-ring chain rule gives E|u=0=q0*V*(t*U'-8*U)",
            ],
            "status": "PASS-EXACT-THEOREM-COMPOSITION",
        },
        "generic_weight22_bridge": {
            "lower_shift_correction": "K22=sum_(n=0)^21 [t^(22-n)] D_n(c+s(t))",
            "components": [
                {
                    "direct_weight": n,
                    "required_shift_coefficient": 22 - n,
                    "direct_terms_sha256": hashlib.sha256(compact(direct["D"][n]["terms"])).hexdigest(),
                }
                for n in range(22)
            ],
            "identity": "R22(c)=[t^22](q0*C)-K22 in A",
            "reason": "[t^22]ev_xi(D)=D22(c)+K22 and D22(c)=R22(c) because H(c)=0",
            "status": "PASS-EXACT-GENERIC-REMAINDER-MAP; K22 RETAINED",
        },
        "lower_row_gate": gate,
        "endpoint_after_gate": {
            "base_change": "C -> Cbar=C/I_<22",
            "identity": "D22(c)=R22(c)=H'(c)*C22 in Cbar[c]/(c^8-1)",
            "reason": "all Taylor-shift contributions from D0,...,D21 vanish coefficientwise; q0*C vanishes below 22; the unit q0_0=H'(c) forces C0=...=C21=0 recursively; and s0=0",
            "triangular_unit_step": "[t^n](q0*C)=q0_0*C_n+sum_(i=1)^n q0_i*C_(n-i), with q0_0=8*c^7 a unit",
            "factor_remainder_recovery": "R22(c)=H'(c)*C22",
            "global_quotient_recovery_from_local_data": "IMPOSSIBLE; Q22 is retained only by direct monic division",
            "status": "CONDITIONAL-IDENTITY; LOWER GATE NOT SOLVED HERE",
        },
        "global_custody": {
            "D22_terms": len(D22),
            "Q22_terms": len(Q22),
            "R22_terms": len(R22),
            "D22_sha256": hashlib.sha256(compact(certificate["D22"])).hexdigest(),
            "Q22_sha256": hashlib.sha256(compact(certificate["H_division"]["Q22"])).hexdigest(),
            "R22_sha256": hashlib.sha256(compact(certificate["H_division"]["R22"])).hexdigest(),
            "target_criterion": "R22=1 AND Q22=0 after an actual lower-gated raw specialization",
            "current_target_status": "NOT EVALUATED; NO RAW SPECIALIZATION OR GATE SOLUTION",
        },
        "controls": {
            "lower_row_shift": {
                "fixture": "D21=X, s=t gives t^21*D21(c+s)=c*t^21+t^22",
                "verdict": "ENDPOINT SIMPLIFICATION REJECTED WITHOUT LOWER GATE",
            },
            "add_H": {
                "mutation": "D22 -> D22+H",
                "local_factor_values": "UNCHANGED",
                "R22": "UNCHANGED",
                "Q22": "INCREMENTS BY 1",
                "target_from_local_only": "REJECTED",
            },
            "missing_Q22": "FAIL-CLOSED: no global target verdict",
            "deleted_factor_tag": "FAIL-CLOSED: exact four-tag registry required",
        },
        "verdict": {
            "local_naturality": "PASS",
            "lower_gate": "DEFINED EXACTLY BUT NOT SOLVED",
            "factor_remainder_map": "PASS AFTER LOWER-GATE BASE CHANGE",
            "global_H_multiple": "PRESERVED BY DIRECT Q22",
            "target": "NO VERDICT",
            "face_or_family": "NO VERDICT",
        },
        "claims_not_made": [
            "existence or properness of the lower-gate quotient",
            "R22=1",
            "Q22=0",
            "Keller specialization",
            "8_28 face/family exclusion",
            "GGV landing",
            "G2-PSC",
            "G2-BD",
            "counterexample",
            "JC2",
        ],
    }


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--write-result":
        out = Path(sys.argv[2])
        out.write_bytes(pretty(build_result()))
        print(f"WROTE {out} {out.stat().st_size} bytes")
        return
    if len(sys.argv) == 3 and sys.argv[1] == "--check":
        result = Path(sys.argv[2])
        assert result.read_bytes() == pretty(build_result())
        print("PASS D5N exact typed local-naturality bridge replay")
        return
    raise SystemExit("usage: verify_d5n.py --write-result RESULT.json | --check RESULT.json")


if __name__ == "__main__":
    main()
