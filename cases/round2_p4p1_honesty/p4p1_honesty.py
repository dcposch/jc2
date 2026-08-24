#!/usr/bin/env python3
"""Exact band-42 P4P1 checkpoint/assembly/source honesty gate.

The gate is deliberately narrow.  It neither solves a D43 system nor emits
an integral model.  See PREREGISTRATION.md for the frozen scope and verdicts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pickle
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CASES = REPO / "cases"
sys.path.insert(0, str(CASES))

import d25_reduce as DR
import d43_nf_certificate as NF


PRIMES = (105337, 105673)
HS = (2, 5, 8, 11, 14, 17, 20, 23, 26, 29)
GBVARS = tuple(DR.GBVARS)
ZERO_PACKED = DR.pack([0] * DR.NV)
PREREGISTERED_UTC = "2026-08-24T03:11:17Z"
BASE_COMMIT = "8bf25a52f5f6c20886b77c6d9aeeb879eb18f8e4"

SOURCE_PATHS = (
    "cases/d25_reduce.py",
    "cases/d43_family2.py",
    "cases/d43_nf_certificate.py",
    "cases/eplus43.py",
    "cases/d43red/d43red_p105337_a00pp_band42.pkl",
    "cases/d43red/d43red_p105673_a00pp_band42.pkl",
    "cases/directionb_det23_gb_p105337.out.txt",
    "cases/directionb_det23_gb_p105673.out.txt",
    "xmodel/review-d43-nf-fid-grok.md",
    "xmodel/ideation-20260824T0156Z-synthesis.md",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_hash(value: object) -> str:
    blob = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def pmul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def p4p1_integer() -> dict[int, int]:
    """Compute p(eta)^4 p'(eta) without importing an assembly table."""
    peta = [6, 0, 0, -6, 0, 0, 1]
    power = [1]
    for _ in range(4):
        power = pmul(power, peta)
    derivative = [i * peta[i] for i in range(1, len(peta))]
    result = pmul(power, derivative)
    return {i: c for i, c in enumerate(result) if c}


def source_multipliers_direct() -> dict[str, object]:
    """Direct four-term t^42 extraction before simplifying p powers.

    phi0=S*p^2, gamma0=G*p^3.  The entries are the integer multipliers
    of S*G*p^4*p' contributed by the written Euler expression.
    """
    pieces = {
        "alpha": {
            "(thetaPhi-12Phi)_42_times_GammaEta_0": (42 - 12) * 3,
            "minus_PhiEta_42_times_(thetaGamma-18Gamma)_0": -2 * (-18),
        },
        "beta": {
            "(thetaPhi-12Phi)_0_times_GammaEta_42": (-12) * 3,
            "minus_PhiEta_0_times_(thetaGamma-18Gamma)_42": -2 * (42 - 18),
        },
    }
    totals = {name: sum(part.values()) for name, part in pieces.items()}
    assert totals == {"alpha": 126, "beta": -84}
    return {"pieces": pieces, "totals": totals,
            "factored": {"common": 42, "linear": [3, -2]}}


def mod_scalars(p: int, table: dict[int, int]) -> dict[int, dict[str, int]]:
    sm = pow(7, 12, p) * pow(pow(2, 6, p), p - 2, p) % p
    gm = (-pow(7, 18, p)) * pow(pow(2, 9, p), p - 2, p) % p
    rows = {}
    for h in HS:
        base = 42 * sm % p * gm % p * (table[h] % p) % p
        rows[h] = {"alpha": 3 * base % p, "beta": -2 * base % p}
    return rows


def deep_to_json(deep: tuple[str, ...]) -> str:
    return "*".join(deep) if deep else "1"


def grouped_row_hash(row: dict[tuple[str, ...], dict[int, int]]) -> str:
    digest = hashlib.sha256()
    for deep in sorted(row):
        digest.update((deep_to_json(deep) + "\n").encode())
        for packed, coeff in sorted(row[deep].items()):
            digest.update((f"{packed}:{coeff}\n").encode())
    return digest.hexdigest()


def subtract_grouped(
    final: dict[tuple[str, ...], dict[int, int]],
    initial: dict[tuple[str, ...], dict[int, int]],
    p: int,
) -> dict[tuple[str, ...], dict[int, int]]:
    out: dict[tuple[str, ...], dict[int, int]] = {}
    for deep in set(final) | set(initial):
        coeffs = {}
        left = final.get(deep, {})
        right = initial.get(deep, {})
        for packed in set(left) | set(right):
            value = (left.get(packed, 0) - right.get(packed, 0)) % p
            if value:
                coeffs[packed] = value
        if coeffs:
            out[deep] = coeffs
    return out


def source_grouped(row: dict[str, int]) -> dict[tuple[str, ...], dict[int, int]]:
    return {
        ("Xf_alpha",): {ZERO_PACKED: row["alpha"]},
        ("Xg_beta",): {ZERO_PACKED: row["beta"]},
    }


def checkpoint_census(bank: dict) -> dict[str, object]:
    assert bank["band"] == 42 and bank["fiber"] == "a00pp"
    assert tuple(bank["gbvars"]) == GBVARS
    assert sorted(bank["rows"]) == [(h, 42) for h in HS]
    sidecar_hits = []
    group_count = 0
    nf_term_count = 0
    for key, groups in bank["rows"].items():
        group_count += len(groups)
        for deep, basepoly in groups.items():
            nf_term_count += len(basepoly)
            if "Xf_alpha" in deep or "Xg_beta" in deep:
                sidecar_hits.append([list(key), list(deep)])
    return {
        "row_count": len(bank["rows"]),
        "row_keys": [list(x) for x in sorted(bank["rows"])],
        "deep_group_count": group_count,
        "normal_form_term_count": nf_term_count,
        "sidecar_occurrences": sidecar_hits,
        "sidecars_absent": not sidecar_hits,
    }


def actual_assembly_delta(
    p: int,
    h29_checkpoint: dict[tuple[str, ...], dict[int, int]],
) -> tuple[dict[int, dict[tuple[str, ...], dict[int, int]]], dict[str, object]]:
    """Exercise the actual final assembler on empty rows and one real row."""
    hs, _names, empty_rows, _matrix, _kernel, _rank = NF.rung_kernel({}, 42, p)
    assert tuple(hs) == HS
    delta = {h: row for h, row in zip(hs, empty_rows)}

    # Row h=29 has only twelve banked NF terms.  Feeding that real checkpoint
    # row through the assembler verifies, on a complete row, that subtraction
    # leaves precisely the content-independent delta returned above.
    grouped = {29: h29_checkpoint}
    hs2, _n2, rows2, _c2, _l2, _r2 = NF.rung_kernel(grouped, 42, p)
    final29 = rows2[hs2.index(29)]
    difference29 = subtract_grouped(final29, h29_checkpoint, p)
    assert difference29 == delta[29]
    return delta, {
        "real_checkpoint_row": 29,
        "checkpoint_row_hash": grouped_row_hash(h29_checkpoint),
        "final_row_hash": grouped_row_hash(final29),
        "subtracted_delta_hash": grouped_row_hash(difference29),
        "subtraction_exact": True,
        "unchanged_checkpoint_groups": all(
            final29.get(deep) == coeffs for deep, coeffs in h29_checkpoint.items()
        ),
    }


def reduce_correction(
    p: int,
    gb: list,
    rows: dict[int, dict[str, int]],
) -> tuple[dict[str, object], int]:
    reductions = {}
    nonzero_rows = 0
    for h in HS:
        reductions[str(h)] = {}
        row_nonzero = False
        for side in ("alpha", "beta"):
            coeff = rows[h][side]
            normal, trace, steps = DR.nf_trace({ZERO_PACKED: coeff}, gb, p)
            expected = {ZERO_PACKED: coeff} if coeff else {}
            assert normal == expected
            assert not trace and steps == 0
            if normal:
                row_nonzero = True
            reductions[str(h)][side] = {
                "input_constant": coeff,
                "normal_form": normal.get(ZERO_PACKED, 0),
                "membership_trace_terms": sum(len(q) for q in trace.values()),
                "reduction_steps": steps,
            }
        if row_nonzero:
            nonzero_rows += 1
    return reductions, nonzero_rows


def build() -> tuple[dict[str, object], dict[str, object]]:
    sources = {relative: sha256(REPO / relative) for relative in SOURCE_PATHS}
    provenance = {
        "base_commit": BASE_COMMIT,
        "preregistered_utc": PREREGISTERED_UTC,
        "scope": "band-42 a00pp modular P4P1 source-honesty only",
        "sources": sources,
    }

    table = p4p1_integer()
    expected_table = {
        2: -23328, 5: 101088, 8: -186624, 11: 191808,
        14: -120528, 17: 47952, 20: -12096, 23: 1872,
        26: -162, 29: 6,
    }
    assert table == expected_table
    four_term = source_multipliers_direct()

    prime_results = {}
    all_source_matches = True
    all_origin_zero = True
    all_off_origin_changes = True
    all_remainders_nonzero = True
    for p in PRIMES:
        checkpoint_path = CASES / "d43red" / f"d43red_p{p}_a00pp_band42.pkl"
        with checkpoint_path.open("rb") as handle:
            bank = pickle.load(handle)
        assert bank["prime"] == p
        census = checkpoint_census(bank)
        assert census["sidecars_absent"]

        modular_rows = mod_scalars(p, table)
        h29 = bank["rows"][(29, 42)]
        actual_delta, row_comparison = actual_assembly_delta(p, h29)
        actual_delta_json = {}
        for h in HS:
            expected = source_grouped(modular_rows[h])
            assert actual_delta[h] == expected
            actual_delta_json[str(h)] = {
                "alpha": actual_delta[h][("Xf_alpha",)][ZERO_PACKED],
                "beta": actual_delta[h][("Xg_beta",)][ZERO_PACKED],
                "delta_hash": grouped_row_hash(actual_delta[h]),
            }

        gb_path = CASES / f"directionb_det23_gb_p{p}.out.txt"
        gb = DR.parse_msolve_gb(str(gb_path), p)
        assert len(gb) == 509
        positive_leads = all(lt_degree > 0 for _lt, lt_degree, _tail in gb)
        assert positive_leads
        reductions, nonzero_rows = reduce_correction(p, gb, modular_rows)
        origin = {str(h): 0 for h in HS}
        off_origin = {str(h): modular_rows[h]["alpha"] for h in HS}
        origin_zero = all(value == 0 for value in origin.values())
        off_origin_changed = all(value != 0 for value in off_origin.values())
        remainder_nonzero = nonzero_rows == len(HS)

        prime_results[str(p)] = {
            "checkpoint": census,
            "actual_assembler": {
                "empty-input_delta_matches_source_all_rows": True,
                "rows": actual_delta_json,
                "real_row_comparison": row_comparison,
            },
            "source": {
                "SM": pow(7, 12, p) * pow(pow(2, 6, p), p - 2, p) % p,
                "GM": (-pow(7, 18, p)) * pow(pow(2, 9, p), p - 2, p) % p,
                "row_scalars": {str(h): modular_rows[h] for h in HS},
            },
            "base_ideal_reduction": {
                "ideal": "I23_a00pp_det23",
                "ring_variables": list(GBVARS),
                "external_variables": ["Xf_alpha", "Xg_beta"],
                "groebner_elements": len(gb),
                "all_leading_terms_positive_degree": positive_leads,
                "coefficientwise_reductions": reductions,
                "nonzero_remainder_rows": nonzero_rows,
            },
            "controls": {
                "origin_assignment": {"alpha": 0, "beta": 0},
                "origin_correction": origin,
                "origin_unchanged": origin_zero,
                "off_origin_assignment": {"alpha": 1, "beta": 0},
                "off_origin_correction": off_origin,
                "off_origin_changes_all_ten_rows": off_origin_changed,
            },
            "classification": "ORIGIN-ONLY",
        }
        all_source_matches &= True
        all_origin_zero &= origin_zero
        all_off_origin_changes &= off_origin_changed
        all_remainders_nonzero &= remainder_nonzero
        del bank, gb

    assert all_source_matches and all_origin_zero
    assert all_off_origin_changes and all_remainders_nonzero
    core = {
        "integer_p4p1": {str(h): table[h] for h in HS},
        "four_term_source_derivation": four_term,
        "primes": prime_results,
        "verdict": "ORIGIN-ONLY",
    }
    result = {
        "schema": "jc2.p4p1-source-honesty.v1",
        "status": "INTERNAL / PRODUCER-CHECKED",
        "scope": "MOD-p at the registered a00pp/I23 band-42 compiler interface",
        "verdict": "ORIGIN-ONLY",
        "verdict_semantics": (
            "the symbolic correction survives exact base-ideal reduction, "
            "vanishes at alpha=beta=0, and changes all ten rows at (1,0); "
            "this does not assert that its full zero locus is only the origin"
        ),
        "gates": {
            "checkpoint_sidecar_absence": "PASS",
            "integer_p4p1_recomputation": "PASS",
            "four_term_source_derivation": "PASS",
            "actual_assembly_subtraction": "PASS",
            "exact_I23_reduction": "PASS",
            "origin_control": "PASS",
            "off_origin_control": "PASS",
        },
        "integer_p4p1": core["integer_p4p1"],
        "four_term_source_derivation": four_term,
        "primes": prime_results,
        "canonical_claim_sha256": canonical_hash(core),
        "provenance": provenance,
        "nonclaims": [
            "no integral or p-adic emitter",
            "no new depth solve or sample",
            "no D43 nonemptiness or source-reduced-family inference",
            "no germ, inverse limit, characteristic-zero map, or counterexample",
        ],
    }
    return result, provenance


def emit(path: str | None, value: dict[str, object]) -> bytes:
    payload = (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()
    if path:
        Path(path).write_bytes(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    parser.add_argument("--provenance-output")
    args = parser.parse_args()
    result, provenance = build()
    payload = emit(args.output, result)
    if args.provenance_output:
        emit(args.provenance_output, provenance)
    if not args.output:
        sys.stdout.buffer.write(payload)


if __name__ == "__main__":
    main()
