#!/usr/bin/env python3.14
"""Bounded source-stationarity typing gate for the D transition.

The finite regressions use only the unreduced pure-y constructor through band
40.  The stopping boundary is then derived algebraically from the first
omitted full-source factors at t^42; no band-42 point is built or solved.
"""

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


PRIMES = (105337, 105673)
ORDINARY = ("tf1", "tf2", "tg1", "tg2")
S30 = list(V2.S_A) + [V2.S_29]
BANKED_SHIFT_BANDS = (26, 32, 38)


class SourceMismatch(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SourceMismatch(message)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def json_sha256(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def layer_coordinates(band: int) -> List[Tuple[str, int]]:
    return [(family, band - 5) for family in ORDINARY] + [
        (family, band) for family in V2.FAMS
    ]


def layer_rows(band: int) -> List[int]:
    return [a for a, start in enumerate(S30)
            if start <= band and start % 6 == band % 6]


def point_copy(point: Dict[str, object]) -> Dict[str, object]:
    return {
        "tails": {family: dict(point["tails"][family]) for family in V2.FAMS},
        "fixed": dict(point["fixed"]),
        "zc_hash": point["zc_hash"],
    }


def rebuild(point: Dict[str, object], prime: int, roots: Sequence[int]):
    phi, gamma = V2.build_jets(point, prime, roots)
    return phi, gamma, V2.euler_rows(phi, gamma, prime)


def first_support(gradient: np.ndarray) -> Dict[Tuple[str, int], int | None]:
    out = {}
    for label, column in V2.GIDX.items():
        out[label] = next((band for band in range(V2._S)
                           if gradient[:, band, column].any()), None)
    return out


def input_registry() -> Dict[str, object]:
    streams = []
    seen = []
    for family, residue in V2.STREAMS:
        ladder = sorted(r for r in V2.allowed_r(family) if r % 6 == residue)
        require(bool(ladder), f"empty registered ladder {(family, residue)}")
        require(ladder[0] == V2.r_start(residue),
                f"wrong source start for {(family, residue)}")
        require(all(right - left == 6 for left, right in zip(ladder, ladder[1:])),
                f"non-six-step source ladder {(family, residue)}")
        streams.append({"family": family, "residue": residue,
                        "start": ladder[0], "window_levels": ladder})
        seen.extend((family, r) for r in ladder)
    require(sorted(seen) == sorted(V2.GIDX),
            "30 source ladders do not partition the registered coordinates")
    return {
        "count": len(streams),
        "sum_starts": sum(stream["start"] for stream in streams),
        "streams": streams,
        "shift": "(family,r) -> (family,r+6)",
    }


def output_registry() -> Dict[str, object]:
    require(len(S30) == 30 and sum(S30) == 276,
            "corrected 30-output constants changed")
    return {
        "count": 30,
        "starts": S30,
        "sum_starts": sum(S30),
        "shift": "(a,n) -> (a,n+6)",
        "transient": {"H29_start": 36},
    }


def audit_banked_prime(prime: int) -> Dict[str, object]:
    point, source, roots, meta = TS.d25_sample(prime, "witness")
    values = source.V.astype(np.int64) % prime
    gradient = source.G.astype(np.int64) % prime

    # Independent written product-rule grouping, not a row fit.
    phi, gamma, rebuilt = rebuild(point, prime, roots)
    grouped = V2.path_A_rows(phi, gamma, prime).astype(np.int64) % prime
    require(np.array_equal(rebuilt.V.astype(np.int64) % prime, values),
            "second source build changed the residual values")
    require(np.array_equal(grouped[:, :41], gradient[:, :41]),
            "dual source and written product-rule derivatives differ through band 40")

    starts = first_support(gradient)
    layer_records = []
    matrices = []
    for band in BANKED_SHIFT_BANDS:
        coordinates = layer_coordinates(band)
        rows = layer_rows(band)
        require(len(coordinates) == 10 and len(rows) == 10,
                f"layer {band} is not the registered 10-by-10 type")
        require(all(label in V2.GIDX for label in coordinates),
                f"layer {band} has an unregistered coordinate")
        exact_first = sorted(label for label, first in starts.items() if first == band)
        require(exact_first == sorted(coordinates),
                f"first-occurrence registry mismatch at band {band}")
        outside_rows = [a for a in range(V2.HMAX)
                        if (values[a, band] or
                            gradient[a, band, [V2.GIDX[x] for x in coordinates]].any())
                        and a not in rows]
        require(not outside_rows, f"undeclared output at band {band}: {outside_rows}")
        matrix = np.array([[int(gradient[a, band, V2.GIDX[label]])
                            for label in coordinates] for a in rows], dtype=np.int64)
        matrices.append(matrix % prime)

        # Exact source-causality square: a combined unit perturbation in the
        # new layer cannot alter its projected lower source rows.  At its
        # first band it equals the source differential; no solve occurs.
        moved = point_copy(point)
        for family, r in coordinates:
            moved["tails"][family][r] = (moved["tails"][family].get(r, 0) + 1) % prime
        _p1, _g1, shifted = rebuild(moved, prime, roots)
        delta = (shifted.V.astype(np.int64) - values) % prime
        expected = np.zeros_like(delta)
        for label in coordinates:
            expected += gradient[:, :, V2.GIDX[label]]
        expected %= prime
        require(not delta[:, :band].any(),
                f"projection square changes a lower row at band {band}")
        require(np.array_equal(delta[:, :band + 1], expected[:, :band + 1]),
                f"first-layer finite difference is not the source derivative at {band}")
        layer_records.append({
            "band": band,
            "rows": rows,
            "coordinates": [[family, r, 32 + r] for family, r in coordinates],
            "matrix_sha256": json_sha256(matrix.tolist()),
            "lower_projection_unchanged": True,
            "finite_difference_equals_derivative": True,
        })

    # The source-derived Euler/Ore rule is affine in the simultaneously
    # shifted scalar r: M(r)=A_d+r B_d for fixed output label, family, and
    # offset d=n-r.  Hence the exact second six-shift difference must vanish.
    ore_second = (matrices[2] - 2 * matrices[1] + matrices[0]) % prime
    require(not ore_second.any(),
            "source-derived simultaneous six-shift Ore second difference is nonzero")

    # Corrected transient: the residue-zero layer gains H29 at 36.  It is
    # explicitly part of S30, not silently fitted away.
    require(len(layer_rows(30)) == 9 and len(layer_rows(36)) == 10
            and 29 in layer_rows(36), "H29 transient registry changed")

    return {
        "prime": prime,
        "completed_point_sha256": meta["completed_point_sha256"],
        "dual_vs_written_product_rule_through_40": True,
        "layers": layer_records,
        "ore_second_difference_zero": True,
        "ore_second_difference_sha256": json_sha256(ore_second.tolist()),
        "H29_transient": {"band30_rows": len(layer_rows(30)),
                           "band36_rows": len(layer_rows(36)),
                           "H29_enters_at_36": True},
        "source_values_through_40_sha256": json_sha256(values[:, :41].tolist()),
        "source_gradient_through_40_sha256": json_sha256(gradient[:, :41].tolist()),
    }


# Independent exact eta-polynomial arithmetic for the first full-source
# sidecar.  Lists are low degree first and use Fraction coefficients.
Poly = List[Fraction]


def trim(poly: Poly) -> Poly:
    out = list(poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def padd(left: Poly, right: Poly) -> Poly:
    size = max(len(left), len(right))
    return trim([(left[i] if i < len(left) else 0) +
                 (right[i] if i < len(right) else 0) for i in range(size)])


def pscale(poly: Poly, scalar: Fraction | int) -> Poly:
    return trim([Fraction(scalar) * coefficient for coefficient in poly])


def pmul(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def ppow(poly: Poly, exponent: int) -> Poly:
    out = [Fraction(1)]
    base = poly
    power = exponent
    while power:
        if power & 1:
            out = pmul(out, base)
        base = pmul(base, base)
        power //= 2
    return out


def pder(poly: Poly) -> Poly:
    return trim([Fraction(i) * poly[i] for i in range(1, len(poly))] or [Fraction(0)])


def encode_fraction_poly(poly: Poly) -> List[List[int]]:
    return [[degree, coefficient.numerator, coefficient.denominator]
            for degree, coefficient in enumerate(trim(poly)) if coefficient]


def xside_interface() -> Dict[str, object]:
    p_eta = [Fraction(6), 0, 0, Fraction(-6), 0, 0, Fraction(1)]
    sm = Fraction(7 ** 12, 2 ** 6)
    gm = Fraction(-(7 ** 18), 2 ** 9)
    f0 = pscale(ppow(p_eta, 2), sm)
    g0 = pscale(ppow(p_eta, 3), gm)
    f0p, g0p = pder(f0), pder(g0)

    # Derivation I: factor the full product rule.
    common = pscale(pmul(ppow(p_eta, 4), pder(p_eta)), 42 * sm * gm)
    alpha_factored = pscale(common, 3)
    beta_factored = pscale(common, -2)

    # Derivation II: directly extract the t^42 coefficient from the four
    # unreduced Euler terms, before using the p-power identities.
    alpha_direct = padd(pscale(pmul(f0, g0p), 30),
                        pscale(pmul(g0, f0p), 18))
    beta_direct = padd(pscale(pmul(f0, g0p), -12),
                       pscale(pmul(g0, f0p), -24))
    row0 = padd(pscale(pmul(f0, g0p), -12),
                pscale(pmul(g0, f0p), 18))
    require(not any(row0), "leading row-zero identity failed")
    require(alpha_direct == alpha_factored and beta_direct == beta_factored,
            "two exact row-42 source derivations disagree")
    require(any(alpha_direct) and any(beta_direct),
            "x-side coordinates do not actually enter the first omitted source row")

    candidate_labels = {(family, residue) for family, residue in V2.STREAMS}
    constructor_signature = str(inspect.signature(V2.build_jets))
    registered_alpha = any("alpha" in family.lower() or "beta" in family.lower()
                           for family, _residue in candidate_labels)
    point_fields = {"tails", "fixed", "zc_hash"}
    typed_classification = None
    # This is a fail-closed inventory statement: the source constructor has
    # no alpha/beta input and the registered 30 stream labels contain neither.
    # The repository specification explicitly leaves their classification as
    # X-SIDE-DERIVATION / X-SIDE-30, so no shift map may be manufactured here.
    require(not registered_alpha and constructor_signature == "(point, p, Z)",
            "registered source interface unexpectedly changed")

    modular = {}
    for prime in PRIMES:
        def reduce_fraction(value: Fraction) -> int:
            return value.numerator % prime * pow(value.denominator % prime, -1, prime) % prime
        aa = [[degree, reduce_fraction(Fraction(num, den))]
              for degree, num, den in encode_fraction_poly(alpha_direct)]
        bb = [[degree, reduce_fraction(Fraction(num, den))]
              for degree, num, den in encode_fraction_poly(beta_direct)]
        require(any(coefficient for _degree, coefficient in aa)
                and any(coefficient for _degree, coefficient in bb),
                f"x-side derivative collapsed at prime {prime}")
        modular[str(prime)] = {"d_row42_d_alpha": aa,
                               "d_row42_d_beta": bb}

    return {
        "first_full_source_level": 42,
        "full_factors": {
            "U_f": "1 + alpha_1*t^42 + ... + alpha_42*t^1764",
            "U_g": "1 + beta_1*t^42 + ... + beta_63*t^2646",
        },
        "row42_identity": (
            "[t^42]E_full=[t^42]E_y+"
            "42*S_M*G_M*(3*alpha_1-2*beta_1)*p(eta)^4*p'(eta)"
        ),
        "p_eta": encode_fraction_poly(p_eta),
        "derivation_factored": {
            "d_row42_d_alpha": encode_fraction_poly(alpha_factored),
            "d_row42_d_beta": encode_fraction_poly(beta_factored),
        },
        "derivation_direct": {
            "d_row42_d_alpha": encode_fraction_poly(alpha_direct),
            "d_row42_d_beta": encode_fraction_poly(beta_direct),
        },
        "two_derivations_agree": True,
        "nonzero_at_registered_primes": modular,
        "registered_y_stream_count": len(candidate_labels),
        "registered_y_stream_contains_alpha_beta": registered_alpha,
        "pure_y_constructor_signature": constructor_signature,
        "pure_y_point_top_fields": sorted(point_fields),
        "alpha_beta_classification": typed_classification,
        "classification_required": ["held-fixed", "derived-with-chain-rule",
                                    "independent-with-source-level"],
        "typed_shift_projection_map_present": False,
    }


def run() -> Dict[str, object]:
    registry_in = input_registry()
    registry_out = output_registry()
    try:
        banked = [audit_banked_prime(prime) for prime in PRIMES]
        sidecar = xside_interface()
    except SourceMismatch as error:
        return {
            "schema_version": 1,
            "gate": "D-STATE-GATE",
            "verdict": "SOURCE-MISMATCH",
            "stop_reason": str(error),
            "input_registry": registry_in,
            "output_registry": registry_out,
            "preregistration_sha256": sha256_file(HERE / "PREREGISTRATION.md"),
            "provenance_sha256": sha256_file(HERE / "provenance.json"),
        }

    # The finite source checks pass, but the first full-source sidecar has
    # two effective coefficients and no sourced status/relabel/projection.
    # The coordinator explicitly required a fail-closed typing verdict here.
    if (not sidecar["typed_shift_projection_map_present"] and
            sidecar["alpha_beta_classification"] is None):
        verdict = "NO-TYPED-STATIONARITY"
        reason = (
            "the pure-y 30-state relabeling passes through band 40, but the "
            "unreduced full source first consumes alpha_1,beta_1 at t^42; "
            "their held/derived/independent status and six-shift projection "
            "map are not sourced"
        )
    else:
        verdict = "STATIONARY-SOURCE-SIGNAL"
        reason = "all frozen full-source state and commuting-square checks pass"

    core = {
        "gate": "D-STATE-GATE",
        "verdict": verdict,
        "input_registry": registry_in,
        "output_registry": registry_out,
        "banked_source_tests": banked,
        "full_source_interface": sidecar,
        "stop_reason": reason,
    }
    return {
        "schema_version": 1,
        **core,
        "core_sha256": json_sha256(core),
        "perimeter": (
            "source typing only; no syzygy, band28, D43 point, integral, "
            "inverse-limit, germ, or characteristic-zero inference"
        ),
        "preregistration_sha256": sha256_file(HERE / "PREREGISTRATION.md"),
        "provenance_sha256": sha256_file(HERE / "provenance.json"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    payload = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
