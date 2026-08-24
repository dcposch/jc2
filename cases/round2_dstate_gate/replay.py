#!/usr/bin/env python3.14
"""Independent replay of D-STATE-GATE; does not import dstate_gate.py."""

from __future__ import annotations

import argparse
import hashlib
import inspect
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import numpy as np


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CASES = REPO / "cases"
sys.path.insert(0, str(CASES))
sys.path.insert(0, str(CASES / "round1_dtransition"))

import transition_symbol as TS  # noqa: E402
import valuation_e2 as V2       # noqa: E402


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def object_hash(value: object) -> str:
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":")).encode("ascii")).hexdigest()


def clone(point):
    return {"tails": {f: dict(point["tails"][f]) for f in V2.FAMS},
            "fixed": dict(point["fixed"]), "zc_hash": point["zc_hash"]}


def build(point, prime, roots):
    f, g = V2.build_jets(point, prime, roots)
    return f, g, V2.euler_rows(f, g, prime)


def coords(band: int) -> List[Tuple[str, int]]:
    ordinary = ("tf1", "tf2", "tg1", "tg2")
    return [(f, band - 5) for f in ordinary] + [(f, band) for f in V2.FAMS]


def replay_prime(prime: int, stored: Dict[str, object]) -> Dict[str, object]:
    point, e0, roots, meta = TS.d25_sample(prime, "witness")
    f, g, e1 = build(point, prime, roots)
    values = e1.V.astype(np.int64) % prime
    gradient = e1.G.astype(np.int64) % prime
    grouped = V2.path_A_rows(f, g, prime).astype(np.int64) % prime
    if not np.array_equal(grouped[:, :41], gradient[:, :41]):
        raise AssertionError("independent grouped derivative mismatch")

    s30 = list(V2.S_A) + [V2.S_29]
    matrices = []
    matrix_hashes = []
    for band, banked_layer in zip((26, 32, 38), stored["layers"]):
        cc = coords(band)
        rr = [a for a, start in enumerate(s30)
              if start <= band and start % 6 == band % 6]
        first = sorted(label for label, column in V2.GIDX.items()
                       if next((n for n in range(V2._S)
                                if gradient[:, n, column].any()), None) == band)
        if first != sorted(cc) or len(rr) != 10:
            raise AssertionError(f"independent layer registry mismatch at {band}")
        matrix = [[int(gradient[a, band, V2.GIDX[label]])
                   for label in cc] for a in rr]
        digest = object_hash(matrix)
        if digest != banked_layer["matrix_sha256"]:
            raise AssertionError(f"banked matrix hash mismatch at {band}")
        matrices.append(np.array(matrix, dtype=np.int64) % prime)
        matrix_hashes.append(digest)

    if (matrices[2] - 2 * matrices[1] + matrices[0]).astype(np.int64).any():
        # Reduce before deciding; written this way to keep the implementation
        # visibly separate from the producer.
        if ((matrices[2] - 2 * matrices[1] + matrices[0]) % prime).any():
            raise AssertionError("independent Ore second difference mismatch")

    # Independently replay the commuting projection at the last banked layer.
    moved = clone(point)
    for family, r in coords(38):
        moved["tails"][family][r] = 1
    _fm, _gm, em = build(moved, prime, roots)
    delta = (em.V.astype(np.int64) - values) % prime
    expected = sum((gradient[:, :, V2.GIDX[label]] for label in coords(38)),
                   np.zeros_like(values)) % prime
    if delta[:, :38].any() or not np.array_equal(delta[:, :39], expected[:, :39]):
        raise AssertionError("independent band-38 projection square mismatch")

    if stored["completed_point_sha256"] != meta["completed_point_sha256"]:
        raise AssertionError("completed source point hash mismatch")
    return {"prime": prime, "matrix_hashes_26_32_38": matrix_hashes,
            "written_product_rule_equal": True,
            "ore_second_difference_zero": True,
            "band38_projection_square": True,
            "completed_point_sha256": meta["completed_point_sha256"]}


# Separate bivariate polynomial engine: keys are (t exponent, eta exponent).
Bi = Dict[Tuple[int, int], Fraction]


def norm(poly: Bi) -> Bi:
    return {mon: value for mon, value in poly.items() if value}


def plus(*polys: Bi) -> Bi:
    out: Bi = {}
    for poly in polys:
        for mon, value in poly.items():
            out[mon] = out.get(mon, Fraction(0)) + value
    return norm(out)


def times(left: Bi, right: Bi) -> Bi:
    out: Bi = {}
    for (t, eta), a in left.items():
        for (u, zeta), b in right.items():
            key = (t + u, eta + zeta)
            out[key] = out.get(key, Fraction(0)) + a * b
    return norm(out)


def scalar(poly: Bi, value: int | Fraction) -> Bi:
    return norm({mon: coefficient * Fraction(value) for mon, coefficient in poly.items()})


def theta(poly: Bi) -> Bi:
    return norm({(t, eta): coefficient * t for (t, eta), coefficient in poly.items()})


def deta(poly: Bi) -> Bi:
    return norm({(t, eta - 1): coefficient * eta
                 for (t, eta), coefficient in poly.items() if eta})


def euler(phi: Bi, gamma: Bi) -> Bi:
    return plus(times(plus(theta(phi), scalar(phi, -12)), deta(gamma)),
                scalar(times(deta(phi), plus(theta(gamma), scalar(gamma, -18))), -1))


def eta_poly_to_bi(coefficients: Sequence[Fraction], t: int = 0) -> Bi:
    return {(t, degree): value for degree, value in enumerate(coefficients) if value}


def one_var_mul(left: Sequence[Fraction], right: Sequence[Fraction]) -> List[Fraction]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def one_var_pow(poly: Sequence[Fraction], exponent: int) -> List[Fraction]:
    out = [Fraction(1)]
    for _ in range(exponent):
        out = one_var_mul(out, poly)
    return out


def encode_t42(poly: Bi) -> List[List[int]]:
    return [[eta, value.numerator, value.denominator]
            for (t, eta), value in sorted(poly.items()) if t == 42 and value]


def independent_xside(stored: Dict[str, object]) -> Dict[str, object]:
    p = [Fraction(6), 0, 0, Fraction(-6), 0, 0, Fraction(1)]
    f0_coeff = [Fraction(7 ** 12, 2 ** 6) * c for c in one_var_pow(p, 2)]
    g0_coeff = [Fraction(-(7 ** 18), 2 ** 9) * c for c in one_var_pow(p, 3)]
    f0 = eta_poly_to_bi(f0_coeff)
    g0 = eta_poly_to_bi(g0_coeff)
    base = euler(f0, g0)
    if base:
        raise AssertionError("independent leading row is not zero")

    # Add one t^42 copy of F0 or G0 and subtract the baseline.  This directly
    # extracts the alpha/beta partials without using the producer's formula.
    f_alpha = plus(f0, eta_poly_to_bi(f0_coeff, 42))
    g_beta = plus(g0, eta_poly_to_bi(g0_coeff, 42))
    alpha = plus(euler(f_alpha, g0), scalar(base, -1))
    beta = plus(euler(f0, g_beta), scalar(base, -1))
    aa, bb = encode_t42(alpha), encode_t42(beta)
    if aa != stored["derivation_direct"]["d_row42_d_alpha"]:
        raise AssertionError("independent alpha sidecar differs")
    if bb != stored["derivation_direct"]["d_row42_d_beta"]:
        raise AssertionError("independent beta sidecar differs")
    if not aa or not bb:
        raise AssertionError("independent x-side partial vanished")

    signature = str(inspect.signature(V2.build_jets))
    labels = [family for family, _rho in V2.STREAMS]
    spec = (REPO / "xmodel/sol-xside-spec.md").read_text(encoding="utf-8")
    markers = ["CONJECTURE X-SIDE-DERIVATION", "CONJECTURE X-SIDE-30",
               "held fixed", "derived", "independent"]
    if not all(marker in spec for marker in markers):
        raise AssertionError("x-side typing specification markers changed")
    if signature != "(point, p, Z)" or any(name in labels for name in ("alpha", "beta")):
        raise AssertionError("pure-y registered interface unexpectedly changed")
    return {"alpha_sha256": object_hash(aa), "beta_sha256": object_hash(bb),
            "two_variable_direct_expansion": True,
            "partials_nonzero": True,
            "pure_y_signature": signature,
            "typing_markers_present": markers,
            "typed_alpha_beta_map_found": False}


def replay(path: Path) -> Dict[str, object]:
    results = json.loads(path.read_text(encoding="utf-8"))
    if results["verdict"] != "NO-TYPED-STATIONARITY":
        raise AssertionError("unexpected producer verdict")
    provenance = json.loads((HERE / "provenance.json").read_text(encoding="utf-8"))
    for relative, expected in provenance["sources"].items():
        if file_hash(REPO / relative) != expected:
            raise AssertionError(f"provenance source hash mismatch: {relative}")

    # Re-derive the registries from literal formulas.
    families = {"tf1": range(6), "tf2": range(6), "tg1": range(6),
                "tg2": range(6), "tg01": (0, 2, 4), "tg02": (0, 2, 4)}
    starts = [16 if residue == 4 else 6 + residue
              for family, residues in families.items() for residue in residues]
    s30 = [6 + 2 * ((a + 1) % 3) for a in range(29)]
    s30[28] = 16
    s30.append(36)
    if len(starts) != 30 or sum(starts) != 288 or len(s30) != 30 or sum(s30) != 276:
        raise AssertionError("independent registry constants failed")
    if results["input_registry"]["sum_starts"] != 288 or results["output_registry"]["starts"] != s30:
        raise AssertionError("producer registry differs")

    banked = []
    for stored in results["banked_source_tests"]:
        banked.append(replay_prime(int(stored["prime"]), stored))
    xside = independent_xside(results["full_source_interface"])
    core = {"gate": "D-STATE-GATE", "producer_verdict": results["verdict"],
            "registry_constants": {"inputs": 30, "sum_r": 288,
                                   "outputs": 30, "sum_s": 276},
            "banked": banked, "xside": xside,
            "review_verdict": "PASS"}
    return {"schema_version": 1, **core,
            "core_sha256": object_hash(core),
            "producer_results_sha256": file_hash(path),
            "producer_core_sha256": results["core_sha256"],
            "preregistration_sha256": file_hash(HERE / "PREREGISTRATION.md"),
            "provenance_sha256": file_hash(HERE / "provenance.json")}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=HERE / "results.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = replay(args.input)
    payload = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
