#!/usr/bin/env python3
"""Exact, compact size certificates for the residual G_i-only charts.

The proved support is

    G_i = {(b,a): 0 <= a < K, 0 <= b <= floor(d*(i*K-a))},

where ``K=gcd(n',m')`` and
``d=(ell+1)/(n'-M_terminal'-1)``.  Unknown counts are therefore direct
finite arithmetic after applying the same gauges as the charged G-only
emitter.

Generator counts are *not* guessed from a bounding polygon.  For every
receiver this driver runs the actual production path

``gi_only_emit.supports -> sprime3_compiler.build_spec ->``
``order_basis_full.native_builder_text -> builder_fix.fix_text``.

It then interprets that emitted P-first H-level/division program in two small
coefficient semirings, without asking Singular to materialize coefficient
expressions:

* interval supports give an a priori upper set of ``(h-power,x-power,y-power)``
  coefficient rows emitted by the production program;
* a deterministic specialization of every emitted independent coefficient
  modulo a large prime gives a subset of the genuinely nonzero rows.

If the two sets agree, every upper-set coordinate has a nonzero modular
specialization.  Hence its integer coefficient polynomial, and therefore its
coefficient over Q, is nonzero.  Equality is an exact certificate, not a
probabilistic inference.  No coefficient expressions or solver jobs are
emitted.

The receiver key has FOUR entries ``(n',m',M_terminal',ell)``.  Although one
individual G_i is fixed by K and d, the complete chart also has e=n'/K alpha
blocks and q=m'/K beta blocks; omitting m' can conflate different charts.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import sys
from fractions import Fraction
from math import floor, gcd
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DEFAULT_ROWS = ROOT / "box/child-own-v-20260905/own-rows.jsonl"
DEFAULT_OUTPUT = HERE / "chart-counts.json"
GI_MANIFEST = ROOT / "box/gi-only-20260905/classes_manifest.json"
GI_EMITTER = ROOT / "box/gi-only-20260905/gi_only_emit.py"
GI_COMPILER = ROOT / "box/moh14-charts-20260905/sprime3_compiler.py"
GI_BUILDER_FIX = ROOT / "box/moh14-charts-20260905/builder_fix.py"
GI_EMITTER_SHA256 = "05e7e2bb7619024b72b8b7b84ea2c39cbfa46e772687762f3c610f42328788f4"
GI_EMITTER_COMPILER_SHA256 = "7e6cfeedcee999a0163df9a23fd03fea695ca55a5de64e2e85b883a2fd4e1833"
GI_BUILDER_FIX_SHA256 = "d6662abfec114a443712600f87e3e7b7064071f445d9b177d2f0ea13c9d3836b"
GI_ROW_GENERATOR_SHA256 = "f4e0e98e930f5b4ac9f54c8d3660fb8ca9c58dfd20a0500a456df77b47191639"
WITNESS_PRIME = 1_000_000_007
WITNESS_SEEDS = (1729, 65537, 104729)

Interval = tuple[int, int]
Profile = dict[int, tuple[Interval, ...]]  # y-power -> x-power intervals
NumericPoly = dict[tuple[int, int], int]
ReceiverKey = tuple[int, int, int, int]
_EMITTER_RUNTIME: tuple[Any, Any, Any, dict[str, Any]] | None = None
_PARSER_NEGATIVE_CONTROLS: dict[str, Any] | None = None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + f".tmp.{os.getpid()}")
    temporary.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def import_at(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def production_emitter_runtime() -> tuple[Any, Any, Any, dict[str, Any]]:
    """Load the exact production emitter/compiler/fix path once per process."""

    global _EMITTER_RUNTIME
    if _EMITTER_RUNTIME is not None:
        return _EMITTER_RUNTIME
    if sha256_file(GI_COMPILER) != GI_EMITTER_COMPILER_SHA256:
        raise AssertionError("G_i emitter compiler content changed")
    if sha256_file(GI_BUILDER_FIX) != GI_BUILDER_FIX_SHA256:
        raise AssertionError("G_i emitter builder_fix content changed")
    if sha256_file(GI_EMITTER) != GI_EMITTER_SHA256:
        raise AssertionError("G_i production emitter content changed")
    for path in (
        ROOT / "box",
        ROOT / "box/orderbasis-20260903",
        ROOT / "box/mohprog-drivers-20260903",
        ROOT / "box/xuscreen-20260903",
        ROOT / "box/lib",
        ROOT / "box/moh14-charts-20260905",
    ):
        value = str(path)
        if value not in sys.path:
            sys.path.insert(0, value)
    compiler = import_at("residual66_gi_sprime3_compiler", GI_COMPILER)
    emitter = import_at("residual66_gi_only_emit", GI_EMITTER)
    builder_fix = import_at("residual66_gi_builder_fix", GI_BUILDER_FIX)
    orientation = emitter.orientation_control()
    if orientation.get("status") != "PASS":
        raise AssertionError("G_i emitter orientation control failed")
    row_generator = Path(compiler.OB.__file__).resolve()
    if sha256_file(row_generator) != GI_ROW_GENERATOR_SHA256:
        raise AssertionError("G_i production row generator content changed")
    custody = {
        "gi_only_emitter": str(GI_EMITTER.relative_to(ROOT)),
        "gi_only_emitter_sha256": sha256_file(GI_EMITTER),
        "charged_compiler": str(GI_COMPILER.relative_to(ROOT)),
        "charged_compiler_sha256": sha256_file(GI_COMPILER),
        "production_row_generator": str(row_generator.relative_to(ROOT)),
        "production_row_generator_sha256": sha256_file(row_generator),
        "charged_builder_fix": str(GI_BUILDER_FIX.relative_to(ROOT)),
        "charged_builder_fix_sha256": sha256_file(GI_BUILDER_FIX),
        "orientation_control": "PASS",
    }
    _EMITTER_RUNTIME = compiler, emitter, builder_fix, custody
    return _EMITTER_RUNTIME


def normalize_intervals(intervals: Iterable[Interval]) -> tuple[Interval, ...]:
    ordered = sorted((int(lo), int(hi)) for lo, hi in intervals if lo <= hi)
    merged: list[Interval] = []
    for lo, hi in ordered:
        if merged and lo <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], hi))
        else:
            merged.append((lo, hi))
    return tuple(merged)


def profile_union(*profiles: Profile) -> Profile:
    buckets: dict[int, list[Interval]] = {}
    for profile in profiles:
        for ypow, intervals in profile.items():
            buckets.setdefault(ypow, []).extend(intervals)
    return {
        ypow: normalized
        for ypow, values in buckets.items()
        if (normalized := normalize_intervals(values))
    }


def profile_derivative(profile: Profile, axis: int) -> Profile:
    if axis not in (0, 1):
        raise ValueError("derivative axis must be x=0 or y=1")
    if axis == 1:
        return {ypow - 1: intervals for ypow, intervals in profile.items() if ypow > 0}
    answer: Profile = {}
    for ypow, intervals in profile.items():
        shifted = normalize_intervals(
            (max(1, lo) - 1, hi - 1) for lo, hi in intervals if hi >= 1
        )
        if shifted:
            answer[ypow] = shifted
    return answer


def profile_multiply(left: Profile, right: Profile) -> Profile:
    buckets: dict[int, list[Interval]] = {}
    for left_y, left_intervals in left.items():
        for right_y, right_intervals in right.items():
            target = buckets.setdefault(left_y + right_y, [])
            target.extend(
                (left_lo + right_lo, left_hi + right_hi)
                for left_lo, left_hi in left_intervals
                for right_lo, right_hi in right_intervals
            )
    return {
        ypow: normalized
        for ypow, values in buckets.items()
        if (normalized := normalize_intervals(values))
    }


def profile_jacobian(left: Profile, right: Profile) -> Profile:
    return profile_union(
        profile_multiply(
            profile_derivative(left, 0), profile_derivative(right, 1)
        ),
        profile_multiply(
            profile_derivative(left, 1), profile_derivative(right, 0)
        ),
    )


def profile_count(profile: Profile) -> int:
    return sum(hi - lo + 1 for intervals in profile.values() for lo, hi in intervals)


def profile_subset_coordinates(profile: Profile) -> set[tuple[int, int]]:
    return {
        (xpow, ypow)
        for ypow, intervals in profile.items()
        for lo, hi in intervals
        for xpow in range(lo, hi + 1)
    }


def gi_profile(K: int, d: Fraction, deficit: int) -> Profile:
    if K < 1 or d <= 0 or deficit < 1:
        raise ValueError("G_i needs K>=1, d>0, and deficit>=1")
    return {
        ypow: ((0, floor(d * (deficit * K - ypow))),)
        for ypow in range(K)
    }


def remove_constant(profile: Profile) -> Profile:
    answer = dict(profile)
    intervals = list(answer.get(0, ()))
    adjusted: list[Interval] = []
    for lo, hi in intervals:
        if lo <= 0 <= hi:
            if lo <= -1:
                adjusted.append((lo, -1))
            if hi >= 1:
                adjusted.append((1, hi))
        else:
            adjusted.append((lo, hi))
    normalized = normalize_intervals(adjusted)
    if normalized:
        answer[0] = normalized
    else:
        answer.pop(0, None)
    return answer


def profile_is_scalar(profile: Profile) -> bool:
    return profile == {0: ((0, 0),)}


def profile_is_subset(left: Profile, right: Profile) -> bool:
    return profile_subset_coordinates(left) <= profile_subset_coordinates(right)


def gauged_profiles(
    K: int, d: Fraction, e: int, q: int
) -> tuple[Profile, dict[int, Profile], dict[int, Profile], list[str]]:
    """Reproduce ``sprime3_compiler.apply_gauges`` on the exact G supports."""

    h = gi_profile(K, d, 1)
    alpha = {i: gi_profile(K, d, i) for i in range(1, e + 1)}
    beta = {i: gi_profile(K, d, i) for i in range(2, q + 1)}
    gauges: list[str] = []

    shear = e - q
    scalar = profile_is_scalar(alpha.get(shear, {}))
    embeds = scalar and all(
        profile_is_subset(support, alpha.get(deficit + shear, {}))
        for deficit, support in beta.items()
    )
    if embeds:
        alpha[shear] = {}
        gauges.append(f"P -> P - alpha_{shear} Q")
    if (0, 0) in profile_subset_coordinates(beta.get(q, {})):
        beta[q] = remove_constant(beta[q])
        gauges.append(f"Q -> Q - const(beta_{q})")
    if (0, 0) in profile_subset_coordinates(alpha.get(e, {})):
        alpha[e] = remove_constant(alpha[e])
        gauges.append(f"P -> P - const(alpha_{e})")
    return h, alpha, beta, gauges


def profile_monic_division(
    dividend: Profile, h: Profile, K: int
) -> tuple[Profile, Profile]:
    """Support upper bound for determinate division by monic y^K+h_lower."""

    if h.get(K) != ((0, 0),):
        raise AssertionError("h profile is not monic with unique y^K term")
    lower_h = {ypow: intervals for ypow, intervals in h.items() if ypow != K}
    work = dict(dividend)
    quotient: Profile = {}
    while work:
        degree_y = max(work)
        if degree_y < K:
            break
        top = {degree_y: work.pop(degree_y)}
        quotient_term = {degree_y - K: top[degree_y]}
        quotient = profile_union(quotient, quotient_term)
        # The leading product cancels exactly.  Forgetting coefficients in the
        # remaining subtraction can only enlarge support, hence gives an upper set.
        work = profile_union(work, profile_multiply(quotient_term, lower_h))
    return quotient, work


def structural_rows(
    K: int, d: Fraction, e: int, q: int, ell: int,
    h_lower: Profile, alpha: Mapping[int, Profile], beta: Mapping[int, Profile],
) -> set[tuple[int, int, int]]:
    h = dict(h_lower)
    h[K] = ((0, 0),)
    A: dict[int, Profile] = {0: {0: ((0, 0),)}, **dict(alpha)}
    B: dict[int, Profile] = {0: {0: ((0, 0),)}, 1: {}, **dict(beta)}
    levels: dict[int, Profile] = {}

    for i in range(e + 1):
        p_power = e - i
        for j in range(q + 1):
            q_power = q - j
            if not A.get(i) or not B.get(j):
                continue
            same_level = p_power + q_power
            levels[same_level] = profile_union(
                levels.get(same_level, {}), profile_jacobian(A[i], B[j])
            )
            lower_terms: list[Profile] = []
            if q_power:
                lower_terms.append(
                    profile_multiply(B[j], profile_jacobian(A[i], h))
                )
            if p_power:
                lower_terms.append(
                    profile_multiply(A[i], profile_jacobian(h, B[j]))
                )
            if lower_terms:
                lower_level = same_level - 1
                levels[lower_level] = profile_union(
                    levels.get(lower_level, {}), *lower_terms
                )

    rows: set[tuple[int, int, int]] = set()
    level = 0
    last_initial = max(levels, default=0)
    while level <= last_initial or levels.get(level):
        quotient, remainder = profile_monic_division(
            levels.pop(level, {}), h, K
        )
        if quotient:
            levels[level + 1] = profile_union(levels.get(level + 1, {}), quotient)
        if level == 0:
            remainder = profile_union(remainder, {0: ((ell, ell),)})
        rows.update(
            (level, xpow, ypow)
            for xpow, ypow in profile_subset_coordinates(remainder)
        )
        level += 1
    return rows


def parameter_value(name: str, prime: int, seed: int) -> int:
    raw = hashlib.sha256(f"{seed}:{name}".encode("ascii")).digest()
    value = int.from_bytes(raw[:8], "big") % prime
    return value or 1


def numeric_addto(
    target: NumericPoly, source: Mapping[tuple[int, int], int],
    prime: int, scale: int = 1,
) -> None:
    scale %= prime
    if not scale:
        return
    for coordinate, coefficient in source.items():
        value = (target.get(coordinate, 0) + scale * coefficient) % prime
        if value:
            target[coordinate] = value
        else:
            target.pop(coordinate, None)


def numeric_derivative(
    poly: Mapping[tuple[int, int], int], axis: int, prime: int
) -> NumericPoly:
    answer: NumericPoly = {}
    for (xpow, ypow), coefficient in poly.items():
        exponent = xpow if axis == 0 else ypow
        if exponent:
            coordinate = (
                xpow - (1 if axis == 0 else 0),
                ypow - (1 if axis == 1 else 0),
            )
            answer[coordinate] = coefficient * exponent % prime
    return answer


def numeric_multiply(
    left: Mapping[tuple[int, int], int],
    right: Mapping[tuple[int, int], int],
    prime: int,
) -> NumericPoly:
    # Iterating over the smaller input outside improves the large residual cases.
    if len(left) > len(right):
        left, right = right, left
    answer: NumericPoly = {}
    for (left_x, left_y), left_coefficient in left.items():
        for (right_x, right_y), right_coefficient in right.items():
            coordinate = (left_x + right_x, left_y + right_y)
            value = (
                answer.get(coordinate, 0)
                + left_coefficient * right_coefficient
            ) % prime
            if value:
                answer[coordinate] = value
            else:
                answer.pop(coordinate, None)
    return answer


def numeric_jacobian(
    left: Mapping[tuple[int, int], int],
    right: Mapping[tuple[int, int], int],
    prime: int,
) -> NumericPoly:
    answer = numeric_multiply(
        numeric_derivative(left, 0, prime),
        numeric_derivative(right, 1, prime),
        prime,
    )
    numeric_addto(
        answer,
        numeric_multiply(
            numeric_derivative(left, 1, prime),
            numeric_derivative(right, 0, prime),
            prime,
        ),
        prime,
        -1,
    )
    return answer


def numeric_from_profile(
    profile: Profile, prefix: str, prime: int, seed: int,
    assignment_lines: list[str],
) -> NumericPoly:
    answer: NumericPoly = {}
    for xpow, ypow in sorted(profile_subset_coordinates(profile), key=lambda z: (z[1], z[0])):
        name = f"{prefix}_{xpow}_{ypow}"
        value = parameter_value(name, prime, seed)
        answer[(xpow, ypow)] = value
        assignment_lines.append(f"{name}={value}\n")
    return answer


def numeric_monic_division(
    dividend: Mapping[tuple[int, int], int],
    h: Mapping[tuple[int, int], int],
    K: int,
    prime: int,
) -> tuple[NumericPoly, NumericPoly]:
    if h.get((0, K)) != 1:
        raise AssertionError("numeric h is not monic y^K")
    lower_h = dict(h)
    lower_h.pop((0, K))
    work = dict(dividend)
    quotient: NumericPoly = {}
    while work:
        degree_y = max(ypow for _, ypow in work)
        if degree_y < K:
            break
        top = [
            ((xpow, ypow), coefficient)
            for (xpow, ypow), coefficient in work.items()
            if ypow == degree_y
        ]
        for coordinate, _ in top:
            del work[coordinate]
        for (xpow, _), coefficient in top:
            q_coordinate = (xpow, degree_y - K)
            q_value = (quotient.get(q_coordinate, 0) + coefficient) % prime
            if q_value:
                quotient[q_coordinate] = q_value
            else:
                quotient.pop(q_coordinate, None)
            for (h_x, h_y), h_coefficient in lower_h.items():
                coordinate = (xpow + h_x, degree_y - K + h_y)
                value = (
                    work.get(coordinate, 0) - coefficient * h_coefficient
                ) % prime
                if value:
                    work[coordinate] = value
                else:
                    work.pop(coordinate, None)
    return quotient, work


def numeric_rows(
    K: int, e: int, q: int, ell: int,
    h_profile: Profile, alpha_profiles: Mapping[int, Profile],
    beta_profiles: Mapping[int, Profile], prime: int, seed: int,
) -> tuple[set[tuple[int, int, int]], str, int]:
    assignments: list[str] = []
    h = numeric_from_profile(h_profile, "h", prime, seed, assignments)
    h[(0, K)] = 1
    A: dict[int, NumericPoly] = {0: {(0, 0): 1}}
    A.update(
        {
            i: numeric_from_profile(profile, f"A{i}", prime, seed, assignments)
            for i, profile in alpha_profiles.items()
        }
    )
    B: dict[int, NumericPoly] = {0: {(0, 0): 1}, 1: {}}
    B.update(
        {
            i: numeric_from_profile(profile, f"B{i}", prime, seed, assignments)
            for i, profile in beta_profiles.items()
        }
    )
    c_value = parameter_value("c", prime, seed)
    assignments.append(f"c={c_value}\n")

    levels: dict[int, NumericPoly] = {}
    for i in range(e + 1):
        p_power = e - i
        for j in range(q + 1):
            q_power = q - j
            if not A.get(i) or not B.get(j):
                continue
            same_level = p_power + q_power
            numeric_addto(
                levels.setdefault(same_level, {}),
                numeric_jacobian(A[i], B[j], prime),
                prime,
            )
            lower: NumericPoly = {}
            if q_power:
                numeric_addto(
                    lower,
                    numeric_multiply(B[j], numeric_jacobian(A[i], h, prime), prime),
                    prime,
                    q_power,
                )
            if p_power:
                numeric_addto(
                    lower,
                    numeric_multiply(A[i], numeric_jacobian(h, B[j], prime), prime),
                    prime,
                    p_power,
                )
            if lower:
                numeric_addto(
                    levels.setdefault(same_level - 1, {}), lower, prime
                )

    rows: set[tuple[int, int, int]] = set()
    level = 0
    last_initial = max(levels, default=0)
    while level <= last_initial or levels.get(level):
        quotient, remainder = numeric_monic_division(
            levels.pop(level, {}), h, K, prime
        )
        if quotient:
            numeric_addto(levels.setdefault(level + 1, {}), quotient, prime)
        if level == 0:
            coordinate = (ell, 0)
            value = (remainder.get(coordinate, 0) - c_value) % prime
            if value:
                remainder[coordinate] = value
            else:
                remainder.pop(coordinate, None)
        rows.update((level, xpow, ypow) for xpow, ypow in remainder)
        level += 1
    assignment_digest = hashlib.sha256("".join(assignments).encode("ascii")).hexdigest()
    return rows, assignment_digest, len(assignments)


def profile_from_coordinates(coordinates: Iterable[tuple[int, int]]) -> Profile:
    buckets: dict[int, list[Interval]] = {}
    for xpow, ypow in coordinates:
        buckets.setdefault(int(ypow), []).append((int(xpow), int(xpow)))
    return {
        ypow: normalized
        for ypow, values in buckets.items()
        if (normalized := normalize_intervals(values))
    }


def parse_emitted_primitive(expr: str) -> list[tuple[int, int, str | None, int]]:
    """Parse the linear setup grammar produced by the charged compiler."""

    expr = expr.strip()
    if expr == "0":
        return []
    normalized = expr.replace(" - ", " + -")
    terms: list[tuple[int, int, str | None, int]] = []
    for raw_term in normalized.split(" + "):
        raw_term = raw_term.strip()
        if not raw_term:
            continue
        scalar = 1
        if raw_term.startswith("-"):
            scalar, raw_term = -1, raw_term[1:]
        xpow = ypow = 0
        parameter: str | None = None
        for token in raw_term.split("*"):
            token = token.strip()
            if not token or token == "1":
                continue
            variable = re.fullmatch(r"([xy])(?:\^(\d+))?", token)
            if variable:
                power = int(variable.group(2) or 1)
                if variable.group(1) == "x":
                    xpow += power
                else:
                    ypow += power
                continue
            if re.fullmatch(r"\d+", token):
                scalar *= int(token)
                continue
            if re.fullmatch(r"[A-Za-z_][A-Za-z_0-9]*", token):
                if parameter is not None:
                    raise ValueError(f"nonlinear emitted setup term: {raw_term!r}")
                parameter = token
                continue
            raise ValueError(f"unsupported emitted setup token {token!r}")
        if scalar:
            terms.append((xpow, ypow, parameter, scalar))
    return terms


def emitted_profile(terms: Sequence[tuple[int, int, str | None, int]]) -> Profile:
    return profile_from_coordinates((xpow, ypow) for xpow, ypow, _, scalar in terms if scalar)


def emitted_numeric_poly(
    terms: Sequence[tuple[int, int, str | None, int]],
    assignments: Mapping[str, int],
    prime: int,
) -> NumericPoly:
    answer: NumericPoly = {}
    for xpow, ypow, parameter, scalar in terms:
        coefficient = scalar if parameter is None else scalar * assignments[parameter]
        coordinate = (xpow, ypow)
        value = (answer.get(coordinate, 0) + coefficient) % prime
        if value:
            answer[coordinate] = value
        else:
            answer.pop(coordinate, None)
    return answer


def parse_emitted_row_program(
    program: str, *, e: int, q: int, expected_program_sha256: str
) -> dict[str, Any]:
    """Parse and strictly verify the row program emitted by native_builder_text."""

    actual_program_sha256 = hashlib.sha256(program.encode("utf-8")).hexdigest()
    if actual_program_sha256 != expected_program_sha256:
        raise AssertionError("fixed emitted program differs from producer-derived digest")

    ring = re.search(
        r"^ring R=0,\(y,x,(.*)\),\(lp\(1\),dp\((\d+)\)\);$", program, re.M
    )
    if ring is None:
        raise AssertionError("dry production emitter did not make a fixed y-first ring")
    parameters = ring.group(1).split(",")
    if not parameters or parameters[-1] != "c":
        raise AssertionError("dry production emitter ring does not end in c")
    if len(parameters) != len(set(parameters)):
        raise AssertionError("dry production emitter ring repeats a parameter")
    if int(ring.group(2)) != len(parameters) + 1:
        raise AssertionError("dry production emitter ring block size mismatch")

    lines = program.splitlines()
    definition_matches = re.findall(
        r"^poly (h|AA\d+|BB\d+) = (.*);$", program, re.M
    )
    definitions = dict(definition_matches)
    expected_names = (
        {"h"}
        | {f"AA{i}" for i in range(1, e + 1)}
        | {f"BB{i}" for i in range(2, q + 1)}
    )
    if (
        len(definition_matches) != len(expected_names)
        or set(definitions) != expected_names
        or "BB1" in program
    ):
        raise AssertionError("dry production emitter setup block mismatch")
    definition_terms = {
        name: parse_emitted_primitive(expr) for name, expr in definitions.items()
    }
    setup_parameters = {
        parameter
        for terms in definition_terms.values()
        for _, _, parameter, _ in terms
        if parameter is not None
    }
    if setup_parameters != set(parameters) - {"c"}:
        raise AssertionError("dry production emitter setup/ring variables differ")

    allocated = [int(value) for value in re.findall(r"^poly H(\d+) = 0;$", program, re.M)]
    if not allocated or allocated != list(range(allocated[-1] + 1)):
        raise AssertionError("dry production emitter H allocation is not consecutive")
    divided = [
        (int(left), int(right))
        for left, right in re.findall(
            r"^  list LD(\d+) = native_y_div_fast\(H(\d+), HDIV\);$",
            program,
            re.M,
        )
    ]
    if divided != [(level, level) for level in allocated[:-1]]:
        raise AssertionError("dry production emitter division schedule mismatch")
    appended = [
        (int(level), int(argument))
        for level, argument in re.findall(
            r"^native_append_coeffs\(H(\d+), (\d+), rowsfile, WX, WY\);$",
            program,
            re.M,
        )
    ]
    if appended != [(level, level) for level in allocated]:
        raise AssertionError("dry production emitter row append schedule mismatch")

    k_values = re.findall(r"lead\(h\) == y\^(\d+)", program)
    target_values = re.findall(r"^H0 = H0 - c\*x\^(\d+);$", program, re.M)
    if len(k_values) != 1 or len(target_values) != 1:
        raise AssertionError("dry production emitter lost divisor/target metadata")
    K, target_ell = int(k_values[0]), int(target_values[0])
    if program.count("ideal HDIV = h;") != 1:
        raise AssertionError("dry production emitter HDIV declaration mismatch")
    h_terms = definition_terms["h"]
    h_leaders = [term for term in h_terms if term[:2] == (0, K)]
    if h_leaders != [(0, K, None, 1)]:
        raise AssertionError("dry production emitter h is not uniquely monic y^K")
    for name, terms in definition_terms.items():
        seen_coordinates: set[tuple[int, int]] = set()
        for xpow, ypow, parameter, scalar in terms:
            if (xpow, ypow) in seen_coordinates:
                raise AssertionError(f"duplicate primitive setup coordinate in {name}")
            seen_coordinates.add((xpow, ypow))
            if name == "h" and (xpow, ypow) == (0, K):
                continue
            if parameter is None or scalar != 1 or (name == "h" and ypow >= K):
                raise AssertionError(f"non-primitive emitted coefficient in {name}")

    consumed_H_lines = {
        index
        for index, line in enumerate(lines)
        if re.fullmatch(r"poly H\d+ = 0;", line)
    }
    same_pattern = re.compile(
        r"tmpSame = diff\(\(([^)]+)\),x\)\*diff\(\(([^)]+)\),y\)"
        r"-diff\(\(([^)]+)\),y\)\*diff\(\(([^)]+)\),x\);"
    )
    same_target_pattern = re.compile(
        r"if \(tmpSame != 0\) \{ H(\d+) = H(\d+) \+ tmpSame; \}"
    )
    lower_target_pattern = re.compile(
        r"if \(tmpLower != 0\) \{ H(\d+) = H(\d+) \+ tmpLower; \}"
    )
    pairs: list[tuple[str, str, int, int, int, int | None]] = []
    consumed_dynamic_lines: set[int] = set()
    for index, line in enumerate(lines):
        match = same_pattern.fullmatch(line)
        if match is None:
            continue
        left, right, left_again, right_again = match.groups()
        if left != left_again or right != right_again:
            raise AssertionError("dry production emitter tmpSame orientation mismatch")
        if left == "1":
            left_power = e
        else:
            left_index = re.fullmatch(r"AA(\d+)", left)
            if left_index is None:
                raise AssertionError(f"unexpected P block in emitted program: {left}")
            left_power = e - int(left_index.group(1))
        if right == "1":
            right_power = q
        else:
            right_index = re.fullmatch(r"BB(\d+)", right)
            if right_index is None:
                raise AssertionError(f"unexpected Q block in emitted program: {right}")
            right_power = q - int(right_index.group(1))
        same_level = left_power + right_power
        same_target = same_target_pattern.fullmatch(lines[index + 1])
        if (
            same_target is None
            or int(same_target.group(1)) != same_level
            or same_target.group(1) != same_target.group(2)
        ):
            raise AssertionError("dry production emitter tmpSame target mismatch")
        consumed_dynamic_lines.update((index, index + 1))
        consumed_H_lines.add(index + 1)
        lower_level: int | None = None
        if same_level:
            expected_lower = (
                f"tmpLower = ({right_power})*({right})*"
                f"(diff(({left}),x)*diff(h,y)-diff(({left}),y)*diff(h,x))"
                f"+({left_power})*({left})*"
                f"(diff(h,x)*diff(({right}),y)-diff(h,y)*diff(({right}),x));"
            )
            if lines[index + 2] != expected_lower:
                raise AssertionError("dry production emitter tmpLower formula mismatch")
            lower_level = same_level - 1
            lower_target = lower_target_pattern.fullmatch(lines[index + 3])
            if (
                lower_target is None
                or int(lower_target.group(1)) != lower_level
                or lower_target.group(1) != lower_target.group(2)
            ):
                raise AssertionError("dry production emitter tmpLower target mismatch")
            consumed_dynamic_lines.update((index + 2, index + 3))
            consumed_H_lines.add(index + 3)
        pairs.append(
            (left, right, left_power, right_power, same_level, lower_level)
        )
    expected_pairs = [
        (left, right)
        for left in ["1", *(f"AA{i}" for i in range(1, e + 1))]
        for right in ["1", *(f"BB{i}" for i in range(2, q + 1))]
    ]
    if [(left, right) for left, right, *_ in pairs] != expected_pairs:
        raise AssertionError("dry production emitter P/Q pair iteration mismatch")
    all_dynamic_lines = {
        index
        for index, line in enumerate(lines)
        if line.startswith(("tmpSame =", "if (tmpSame", "tmpLower =", "if (tmpLower"))
    }
    if consumed_dynamic_lines != all_dynamic_lines:
        raise AssertionError("unconsumed dynamic statement in emitted row program")
    division_block_starts: list[int] = []
    for level in allocated[:-1]:
        division_block = "\n".join(
            [
                f"if (H{level} != 0) {{",
                f"  list LD{level} = native_y_div_fast(H{level}, HDIV);",
                f"  H{level} = LD{level}[2];",
                f"  if (LD{level}[1] != 0) {{ H{level + 1} = H{level + 1} + LD{level}[1]; }}",
                "}",
            ]
        )
        division_lines = division_block.splitlines()
        block_starts = [
            index
            for index in range(len(lines) - len(division_lines) + 1)
            if lines[index : index + len(division_lines)] == division_lines
        ]
        if len(block_starts) != 1:
            raise AssertionError("emitted quotient/remainder propagation block mismatch")
        start = block_starts[0]
        division_block_starts.append(start)
        consumed_H_lines.update((start, start + 1, start + 2, start + 3))
    singleton_H_lines = ["poly level0_before = H0;", f"H0 = H0 - c*x^{target_ell};"]
    for expected_line in singleton_H_lines:
        positions = [index for index, line in enumerate(lines) if line == expected_line]
        if len(positions) != 1:
            raise AssertionError(f"emitted singleton H statement mismatch: {expected_line}")
        consumed_H_lines.add(positions[0])
    for level in allocated:
        expected_line = f"native_append_coeffs(H{level}, {level}, rowsfile, WX, WY);"
        positions = [index for index, line in enumerate(lines) if line == expected_line]
        if len(positions) != 1:
            raise AssertionError("emitted H append statement multiplicity mismatch")
        consumed_H_lines.add(positions[0])
    all_H_lines = {
        index
        for index, line in enumerate(lines)
        if not line.lstrip().startswith("//") and re.search(r"\bH\d+\b", line)
    }
    if consumed_H_lines != all_H_lines:
        extras = sorted(all_H_lines - consumed_H_lines)
        missing = sorted(consumed_H_lines - all_H_lines)
        raise AssertionError(
            f"unconsumed or missing H mutation/reference: extras={extras[:3]} "
            f"missing={missing[:3]}"
        )
    def unique_line_position(expected_line: str) -> int:
        positions = [index for index, line in enumerate(lines) if line == expected_line]
        if len(positions) != 1:
            raise AssertionError(f"emitted semantic line multiplicity mismatch: {expected_line}")
        return positions[0]

    ring_position = unique_line_position(ring.group(0))
    setup_order = [
        "h",
        *(f"AA{i}" for i in range(1, e + 1)),
        *(f"BB{i}" for i in range(2, q + 1)),
    ]
    setup_positions = [
        unique_line_position(f"poly {name} = {definitions[name]};")
        for name in setup_order
    ]
    if setup_positions != sorted(setup_positions):
        raise AssertionError("emitted primitive setup order mismatch")
    hdiv_position = unique_line_position("ideal HDIV = h;")
    lead_positions = [
        index for index, line in enumerate(lines) if f"lead(h) == y^{K}" in line
    ]
    if len(lead_positions) != 1:
        raise AssertionError("emitted lead-gate line multiplicity mismatch")
    allocation_positions = [
        unique_line_position(f"poly H{level} = 0;") for level in allocated
    ]
    target_position = unique_line_position(f"H0 = H0 - c*x^{target_ell};")
    append_positions = [
        unique_line_position(
            f"native_append_coeffs(H{level}, {level}, rowsfile, WX, WY);"
        )
        for level in allocated
    ]
    if not (
        ring_position
        < setup_positions[0]
        <= setup_positions[-1]
        < hdiv_position
        < lead_positions[0]
        < allocation_positions[0]
        <= allocation_positions[-1]
        < min(consumed_dynamic_lines)
        <= max(consumed_dynamic_lines)
        < division_block_starts[0]
        <= division_block_starts[-1]
        < unique_line_position("poly level0_before = H0;")
        < target_position
        < append_positions[0]
        <= append_positions[-1]
    ):
        raise AssertionError("emitted semantic phase order mismatch")
    if sorted(consumed_dynamic_lines) != list(
        range(min(consumed_dynamic_lines), max(consumed_dynamic_lines) + 1)
    ):
        raise AssertionError("emitted pair-update phase is not contiguous")
    if append_positions != list(
        range(append_positions[0], append_positions[0] + len(append_positions))
    ):
        raise AssertionError("emitted append phase is not contiguous")
    semantic_plan = {
        "parameters": parameters,
        "definition_terms": definition_terms,
        "pairs": pairs,
        "allocated_levels": allocated,
        "K": K,
        "ell": target_ell,
    }
    semantic_plan_text = json.dumps(semantic_plan, sort_keys=True, separators=(",", ":"))
    setup_text = json.dumps(definition_terms, sort_keys=True, separators=(",", ":"))
    ring_order_text = "\n".join(parameters) + "\n"
    return {
        "parameters": parameters,
        "definition_terms": definition_terms,
        "pairs": pairs,
        "allocated_levels": allocated,
        "K": K,
        "ell": target_ell,
        "ring": ring.group(0),
        "semantic_plan_sha256": hashlib.sha256(
            semantic_plan_text.encode("utf-8")
        ).hexdigest(),
        "setup_sha256": hashlib.sha256(setup_text.encode("utf-8")).hexdigest(),
        "ring_parameter_order_sha256": hashlib.sha256(
            ring_order_text.encode("utf-8")
        ).hexdigest(),
    }


def validate_emitted_parser_negative_controls(
    program: str, *, e: int, q: int, ell: int, expected_program_sha256: str
) -> dict[str, Any]:
    """Demand rejection of representative semantic mutations and reorderings."""

    global _PARSER_NEGATIVE_CONTROLS
    if _PARSER_NEGATIVE_CONTROLS is not None:
        return _PARSER_NEGATIVE_CONTROLS
    target = f"H0 = H0 - c*x^{ell};"
    if program.count(target) != 1:
        raise AssertionError("negative-control source target is not unique")
    hdiv = "ideal HDIV = h;"
    first_division = "if (H0 != 0) {"
    append_lines = [
        line for line in program.splitlines() if line.startswith("native_append_coeffs(H")
    ]
    append_block = "\n".join(append_lines)
    if not append_lines or program.count(append_block) != 1:
        raise AssertionError("negative-control source append phase is not unique")
    moved_append = program.replace(append_block + "\n", "", 1).replace(
        first_division, append_block + "\n" + first_division, 1
    )
    mutations = {
        "reject_unrecognized_H_mutation": program.replace(
            target, f"H0 = H0 + 1;\n{target}", 1
        ),
        "reject_duplicated_target_subtraction": program.replace(
            target, f"{target}\n{target}", 1
        ),
        "reject_h_mutation": program.replace(hdiv, f"h = h + 1;\n{hdiv}", 1),
        "reject_alpha_mutation": program.replace(
            hdiv, f"AA1 = AA1 + 1;\n{hdiv}", 1
        ),
        "reject_beta_mutation": program.replace(
            hdiv, f"BB2 = BB2 + 1;\n{hdiv}", 1
        ),
        "reject_c_mutation": program.replace(target, f"c = 0;\n{target}", 1),
        "reject_HDIV_rewrite": program.replace(hdiv, "ideal HDIV = h+x;", 1),
        "reject_extra_append": program.replace(
            append_lines[-1],
            append_lines[-1] + "\nnative_append_coeffs(h, 999, rowsfile, WX, WY);",
            1,
        ),
        "reject_append_before_division": moved_append,
    }
    results: dict[str, bool] = {}
    for name, mutated in mutations.items():
        try:
            parse_emitted_row_program(
                mutated,
                e=e,
                q=q,
                expected_program_sha256=expected_program_sha256,
            )
        except (AssertionError, ValueError):
            results[name] = True
        else:
            raise AssertionError(f"emitted-program parser accepted negative control: {name}")
    _PARSER_NEGATIVE_CONTROLS = {
        "status": "PASS",
        **results,
    }
    return _PARSER_NEGATIVE_CONTROLS


def emitted_program_structural_rows(model: Mapping[str, Any]) -> set[tuple[int, int, int]]:
    named: dict[str, Profile] = {"1": {0: ((0, 0),)}}
    named.update(
        {
            name: emitted_profile(terms)
            for name, terms in model["definition_terms"].items()
        }
    )
    h = named["h"]
    levels: dict[int, Profile] = {}
    for left, right, left_power, right_power, same_level, lower_level in model["pairs"]:
        left_poly, right_poly = named[left], named[right]
        levels[same_level] = profile_union(
            levels.get(same_level, {}), profile_jacobian(left_poly, right_poly)
        )
        if lower_level is not None:
            lower_terms: list[Profile] = []
            if right_power:
                lower_terms.append(
                    profile_multiply(right_poly, profile_jacobian(left_poly, h))
                )
            if left_power:
                lower_terms.append(
                    profile_multiply(left_poly, profile_jacobian(h, right_poly))
                )
            levels[lower_level] = profile_union(
                levels.get(lower_level, {}), *lower_terms
            )

    rows: set[tuple[int, int, int]] = set()
    allocated = model["allocated_levels"]
    for level in allocated:
        before = levels.pop(level, {})
        if level == allocated[-1]:
            quotient, remainder = {}, before
            if any(ypow >= model["K"] for ypow in remainder):
                raise AssertionError("dry production emitter final H cap is not reduced")
        else:
            quotient, remainder = profile_monic_division(before, h, model["K"])
            if quotient:
                levels[level + 1] = profile_union(levels.get(level + 1, {}), quotient)
        if level == 0:
            remainder = profile_union(remainder, {0: ((model["ell"], model["ell"]),)})
        rows.update(
            (level, xpow, ypow)
            for xpow, ypow in profile_subset_coordinates(remainder)
        )
    if any(levels.values()):
        raise AssertionError("dry production emitter H allocation was too short")
    return rows


def emitted_program_numeric_rows(
    model: Mapping[str, Any], prime: int, seed: int
) -> tuple[set[tuple[int, int, int]], str, int]:
    parameter_names = model["parameters"]
    assignments = {
        name: parameter_value(name, prime, seed) for name in parameter_names
    }
    assignment_text = "".join(
        f"{name}={assignments[name]}\n" for name in parameter_names
    )
    named: dict[str, NumericPoly] = {"1": {(0, 0): 1}}
    named.update(
        {
            name: emitted_numeric_poly(terms, assignments, prime)
            for name, terms in model["definition_terms"].items()
        }
    )
    h = named["h"]
    levels: dict[int, NumericPoly] = {}
    for left, right, left_power, right_power, same_level, lower_level in model["pairs"]:
        left_poly, right_poly = named[left], named[right]
        numeric_addto(
            levels.setdefault(same_level, {}),
            numeric_jacobian(left_poly, right_poly, prime),
            prime,
        )
        if lower_level is not None:
            lower: NumericPoly = {}
            if right_power:
                numeric_addto(
                    lower,
                    numeric_multiply(
                        right_poly, numeric_jacobian(left_poly, h, prime), prime
                    ),
                    prime,
                    right_power,
                )
            if left_power:
                numeric_addto(
                    lower,
                    numeric_multiply(
                        left_poly, numeric_jacobian(h, right_poly, prime), prime
                    ),
                    prime,
                    left_power,
                )
            numeric_addto(levels.setdefault(lower_level, {}), lower, prime)

    rows: set[tuple[int, int, int]] = set()
    allocated = model["allocated_levels"]
    for level in allocated:
        before = levels.pop(level, {})
        if level == allocated[-1]:
            quotient, remainder = {}, before
            if any(ypow >= model["K"] for _, ypow in remainder):
                raise AssertionError("numeric dry emitter final H cap is not reduced")
        else:
            quotient, remainder = numeric_monic_division(
                before, h, model["K"], prime
            )
            if quotient:
                numeric_addto(levels.setdefault(level + 1, {}), quotient, prime)
        if level == 0:
            coordinate = (model["ell"], 0)
            value = (remainder.get(coordinate, 0) - assignments["c"]) % prime
            if value:
                remainder[coordinate] = value
            else:
                remainder.pop(coordinate, None)
        rows.update((level, xpow, ypow) for xpow, ypow in remainder)
    if any(levels.values()):
        raise AssertionError("numeric dry emitter H allocation was too short")
    return (
        rows,
        hashlib.sha256(assignment_text.encode("ascii")).hexdigest(),
        len(parameter_names),
    )


def dry_production_emitter_count(
    key: ReceiverKey,
    K: int,
    e: int,
    q: int,
    d: Fraction,
    compact_h: Profile,
    compact_alpha: Mapping[int, Profile],
    compact_beta: Mapping[int, Profile],
    compact_gauges: Sequence[str],
    compact_rows: set[tuple[int, int, int]],
    *,
    certify: bool,
) -> dict[str, Any]:
    """Run and count the real production emitter program without writing it."""

    compiler, emitter, builder_fix, custody = production_emitter_runtime()
    n_prime, m_prime, terminal_M, ell = key
    # Only K,e,q,delta_s and ell enter support/setup/row generation.  The
    # remaining fields are metadata placeholders required by build_spec.
    C = {
        "K": K,
        "e": e,
        "q": q,
        "u": 0,
        "R": 0,
        "Pi": 0,
        "d3prime": 1,
        "delta1": Fraction(0),
        "delta2": Fraction(0),
        "delta_s": -d,
        "B": Fraction(-1),
        "B_safe": Fraction(-1),
        "B_tight": Fraction(-1),
        "lambda_P": Fraction(0),
        "lambda_Q": Fraction(0),
        "s": 2,
        "ell": ell,
        "two_point": False,
        "support_basis": "proved_outer_disc_G_only_H1_H2_H3_v1",
    }
    emitted = emitter.supports(compiler, C)
    if set(emitted["h"]) != profile_subset_coordinates(compact_h):
        raise AssertionError(f"production emitter h mismatch at {receiver_key_string(key)}")
    for i in range(1, e + 1):
        if set(emitted["alpha"][i]) != profile_subset_coordinates(compact_alpha[i]):
            raise AssertionError(
                f"production emitter alpha_{i} mismatch at {receiver_key_string(key)}"
            )
    for i in range(2, q + 1):
        if set(emitted["beta"][i]) != profile_subset_coordinates(compact_beta[i]):
            raise AssertionError(
                f"production emitter beta_{i} mismatch at {receiver_key_string(key)}"
            )
    if emitted["gauges"] != list(compact_gauges):
        raise AssertionError(f"production emitter gauge mismatch at {receiver_key_string(key)}")

    row = compiler.OB.Row(
        key=receiver_key_string(key),
        label=f"residual66 dry production {receiver_key_string(key)}",
        n=n_prime,
        m=m_prime,
        M2=terminal_M,
        V2=0,
        k=ell,
    )
    spec = compiler.build_spec(
        C,
        emitted["h"],
        emitted["alpha_pre"],
        emitted["beta_pre"],
        row,
        "proved_G_only_class_uniform_count_only",
    )
    # gi_only_emit.emit_class performs exactly this swap before invoking the
    # production row generator: charged build_spec names low=Q and high=P.
    P_terms = list(spec["high_terms"])
    Q_terms = list(spec["low_terms"])
    spec["low_terms"] = P_terms
    spec["high_terms"] = Q_terms
    if spec["meta"]["gauges"] != emitted["gauges"]:
        raise AssertionError("production build_spec changed the emitter gauges")
    dry_rows_path = Path("/tmp/residual66-production-count-only-rows.tsv")
    raw_program = compiler.OB.native_builder_text(spec, dry_rows_path)
    fixed_program, fix_info = builder_fix.fix_text(raw_program)
    program_sha256 = hashlib.sha256(fixed_program.encode("utf-8")).hexdigest()
    model = parse_emitted_row_program(
        fixed_program,
        e=e,
        q=q,
        expected_program_sha256=program_sha256,
    )
    parser_negative_controls = validate_emitted_parser_negative_controls(
        fixed_program,
        e=e,
        q=q,
        ell=ell,
        expected_program_sha256=program_sha256,
    )
    if model["K"] != K or model["ell"] != ell:
        raise AssertionError("production emitted program receiver metadata mismatch")
    spec_parameters = [str(parameter) for parameter in spec["params"]]
    if model["parameters"] != spec_parameters:
        raise AssertionError("production emitted program parameter order mismatch")

    emitted_rows = emitted_program_structural_rows(model)
    if emitted_rows != compact_rows:
        raise AssertionError(
            f"production emitter/compact coordinate mismatch at {receiver_key_string(key)}"
        )
    witness: dict[str, Any] | None = None
    if certify:
        attempts = []
        for seed in WITNESS_SEEDS:
            evaluated, assignment_sha256, assignment_count = emitted_program_numeric_rows(
                model, WITNESS_PRIME, seed
            )
            outside = evaluated - emitted_rows
            if outside:
                raise AssertionError(
                    "emitted-program modular evaluation escaped its structural upper set"
                )
            attempts.append(
                {
                    "seed": seed,
                    "assignment_sha256": assignment_sha256,
                    "assignment_count": assignment_count,
                    "nonzero_coordinates": len(evaluated),
                    "nonzero_coordinate_sha256": coordinate_digest(evaluated),
                    "covers_structural_upper_set": evaluated == emitted_rows,
                }
            )
            if evaluated == emitted_rows:
                witness = {
                    "status": "PASS",
                    "prime": WITNESS_PRIME,
                    "selected_seed": seed,
                    "assignment_rule": "sha256(seed:name)[0:8] mod p, with 0 replaced by 1",
                    "assignment_sha256": assignment_sha256,
                    "assignment_count": assignment_count,
                    "nonzero_coordinates": len(evaluated),
                    "nonzero_coordinate_sha256": coordinate_digest(evaluated),
                    "equals_structural_upper_set": True,
                    "attempts": attempts,
                    "logic": (
                        "nonzero reduction mod p implies the emitted integer/Q "
                        "coefficient polynomial is nonzero; equality with the emitted "
                        "structural upper set makes its row count exact"
                    ),
                }
                break
        if witness is None:
            raise RuntimeError(
                "deterministic modular attempts did not fill the emitted structural upper set"
            )
        if witness["assignment_count"] != len(spec_parameters):
            raise AssertionError("emitted-program assignment did not cover every unknown")

    raw_program_sha256 = hashlib.sha256(raw_program.encode("utf-8")).hexdigest()
    return {
        "rows": emitted_rows,
        "witness": witness,
        "unknowns_without_T": len(spec_parameters),
        "evidence": {
            "status": "PASS",
            "mode": "production_gi_only_emitter_count_only_dry_run_v1",
            "path": (
                "gi_only_emit.supports -> sprime3_compiler.build_spec -> "
                "emit_class P/Q swap -> order_basis_full.native_builder_text -> "
                "builder_fix.fix_text -> count-only emitted-program interpreter"
            ),
            "literal_orientation": "J(P,Q)-c*x^ell",
            "beta_1_absent": True,
            "supports_equal_compact_crosscheck": True,
            "gauges_equal_compact_crosscheck": True,
            "all_coordinate_rows_equal_compact_crosscheck": True,
            "unknowns_without_T": len(spec_parameters),
            "coefficient_generators": len(emitted_rows),
            "coefficient_coordinate_sha256": coordinate_digest(emitted_rows),
            "raw_emitted_program_sha256": raw_program_sha256,
            "emitted_program_sha256": program_sha256,
            "emitted_program_bytes": len(fixed_program.encode("utf-8")),
            "semantic_plan_sha256": model["semantic_plan_sha256"],
            "ring_parameter_order_sha256": model["ring_parameter_order_sha256"],
            "setup_sha256": model["setup_sha256"],
            "emitted_pair_blocks": len(model["pairs"]),
            "emitted_H_levels": len(model["allocated_levels"]),
            "final_H_cap_sufficient": True,
            "all_dynamic_statements_consumed": True,
            "semantic_phase_order_verified": True,
            "fixed_program_digest_verified_before_interpretation": True,
            "full_producer_sources_hash_pinned": True,
            "procedure_WX_WY_append_division_custody": (
                "covered by fixed-program digest plus pinned row generator and builder_fix"
            ),
            "parser_negative_controls": parser_negative_controls,
            "builder_fix": fix_info,
            **custody,
        },
    }


def coordinate_digest(rows: Iterable[tuple[int, int, int]]) -> str:
    text = "".join(f"{hpow}|{xpow}|{ypow}\n" for hpow, xpow, ypow in sorted(rows))
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def receiver_key_string(key: ReceiverKey) -> str:
    n, m, terminal_M, ell = key
    m_tag = f"m{abs(terminal_M)}" if terminal_M < 0 else str(terminal_M)
    return f"n{n}_m{m}_Mlast{m_tag}_ell{ell}"


def chart_counts_for_receiver(
    n_prime: int,
    m_prime: int,
    M_terminal_prime: int,
    ell: int,
    *,
    certify: bool = True,
) -> dict[str, Any]:
    n_prime = int(n_prime)
    m_prime = int(m_prime)
    M_terminal_prime = int(M_terminal_prime)
    ell = int(ell)
    if not (n_prime > m_prime > 0 and ell >= 0):
        raise ValueError("receiver requires n'>m'>0 and ell>=0")
    denominator = n_prime - M_terminal_prime - 1
    if denominator <= 0:
        raise ValueError("effective terminal datum requires M_terminal'<=n'-2")
    K = gcd(n_prime, m_prime)
    e, q = n_prime // K, m_prime // K
    if q < 2:
        raise ValueError("source-support receiver requires q>=2")
    d = Fraction(ell + 1, denominator)
    h, alpha, beta, gauges = gauged_profiles(K, d, e, q)
    compact_structural = structural_rows(K, d, e, q, ell, h, alpha, beta)

    unknowns_without_T = (
        profile_count(h)
        + sum(profile_count(profile) for profile in alpha.values())
        + sum(profile_count(profile) for profile in beta.values())
        + 1  # c
    )
    key = (n_prime, m_prime, M_terminal_prime, ell)
    production = dry_production_emitter_count(
        key,
        K,
        e,
        q,
        d,
        h,
        alpha,
        beta,
        gauges,
        compact_structural,
        certify=certify,
    )
    structural = production["rows"]
    witness = production["witness"]
    if production["unknowns_without_T"] != unknowns_without_T:
        raise AssertionError("production emitter/compact unknown count mismatch")
    return {
        "receiver_key": {
            "n_prime": n_prime,
            "m_prime": m_prime,
            "M_terminal_prime": M_terminal_prime,
            "ell": ell,
        },
        "receiver_key_string": receiver_key_string(key),
        "K": K,
        "e": e,
        "q": q,
        "d": str(d),
        "support_formula": "G_i={(b,a):0<=a<K,0<=b<=floor(d*(i*K-a))}",
        "gauges": gauges,
        "G_h_count": profile_count(h),
        "G_alpha_dims": [profile_count(alpha[i]) for i in range(1, e + 1)],
        "G_beta_dims": [profile_count(beta[i]) for i in range(2, q + 1)],
        "unknowns_without_T": unknowns_without_T,
        "unknowns_with_T": unknowns_without_T + 1,
        "coefficient_generators": len(structural),
        "generators_including_Tc_minus_1": len(structural) + 1,
        "coefficient_coordinate_sha256": coordinate_digest(structural),
        "count_status": "EXACT" if certify else "STRUCTURAL_UPPER_BOUND",
        "generator_count_source": "production_gi_only_emitter_count_only_dry_run_v1",
        "production_emitter_dry_run": production["evidence"],
        "compact_reconstruction_crosscheck": {
            "status": "PASS",
            "role": "crosscheck_not_authoritative_generator_source",
            "all_coordinate_rows_equal": structural == compact_structural,
            "coefficient_generators": len(compact_structural),
            "coefficient_coordinate_sha256": coordinate_digest(compact_structural),
        },
        "modular_nonzero_witness": witness,
    }


def chart_counts_for_child(child: Mapping[str, Any], *, certify: bool = True) -> dict[str, Any]:
    s_prime = int(child["s"])
    M = child["M"]
    terminal = M.get(str(s_prime), M.get(s_prime))
    if terminal is None:
        raise ValueError(f"child M has no terminal entry {s_prime}")
    return chart_counts_for_receiver(
        int(child["n"]), int(child["m"]), int(terminal), int(child["ell"]),
        certify=certify,
    )


def load_nonempty_rows(path: Path) -> list[tuple[int, dict[str, Any]]]:
    rows: list[tuple[int, dict[str, Any]]] = []
    with path.open(encoding="utf-8", errors="strict") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("own", {}).get("route_state") == "NONEMPTY":
                rows.append((line_number, row))
    return rows


def child_key(child: Mapping[str, Any]) -> ReceiverKey:
    s_prime = int(child["s"])
    M = child["M"]
    terminal = M.get(str(s_prime), M.get(s_prime))
    if terminal is None:
        raise ValueError(f"child M has no terminal entry {s_prime}")
    return int(child["n"]), int(child["m"]), int(terminal), int(child["ell"])


def read_canonical_coordinates(path: Path) -> set[tuple[int, int, int]]:
    rows: set[tuple[int, int, int]] = set()
    with path.open(encoding="utf-8", errors="strict") as handle:
        header = handle.readline().rstrip("\n")
        if header != "source_index|h_power|x_power|y_power|expr":
            raise ValueError(f"bad canonical row header: {path}: {header!r}")
        for line_number, line in enumerate(handle, start=2):
            if not line.strip():
                continue
            pieces = line.rstrip("\n").split("|", 4)
            if len(pieces) != 5:
                raise ValueError(f"bad canonical row {path}:{line_number}")
            coordinate = tuple(int(value) for value in pieces[1:4])
            if coordinate in rows:
                raise ValueError(f"duplicate canonical coordinate {coordinate}: {path}")
            rows.add(coordinate)
    return rows


def validate_canonical_six(cache: dict[ReceiverKey, dict[str, Any]]) -> dict[str, Any]:
    manifest = json.loads(GI_MANIFEST.read_text(encoding="utf-8"))
    if len(manifest) != 6:
        raise AssertionError("expected six canonical G_i classes")
    checks = []
    for cls in manifest:
        key: ReceiverKey = (
            int(cls["n_prime"]),
            int(cls["m_prime"]),
            int(cls["M_prime"][-1]),
            int(cls["ell"]),
        )
        if key not in cache:
            cache[key] = chart_counts_for_receiver(*key)
        count = cache[key]
        rows_path = ROOT / cls["rows_path"]
        canonical_coordinates = read_canonical_coordinates(rows_path)
        expected = {
            "unknowns_without_T": int(cls["unknowns_without_T"]),
            "unknowns_with_T": int(cls["unknowns_with_T"]),
            "coefficient_generators": int(cls["jacobian_coefficient_generator_count"]),
            "generators_including_Tc_minus_1": int(cls["generator_count_including_inverse"]),
        }
        actual = {name: int(count[name]) for name in expected}
        structural_digest = count["coefficient_coordinate_sha256"]
        canonical_digest = coordinate_digest(canonical_coordinates)
        passed = (
            actual == expected
            and len(canonical_coordinates) == count["coefficient_generators"]
            and canonical_digest == structural_digest
            and count["modular_nonzero_witness"]["equals_structural_upper_set"] is True
        )
        if not passed:
            raise AssertionError(
                f"canonical G_i validation failed for {cls['class_id']}: "
                f"expected={expected} actual={actual} "
                f"digest={canonical_digest}/{structural_digest}"
            )
        checks.append(
            {
                "class_id": cls["class_id"],
                "receiver_key": count["receiver_key"],
                "expected": expected,
                "actual": actual,
                "canonical_rows": str(rows_path.relative_to(ROOT)),
                "canonical_rows_sha256": sha256_file(rows_path),
                "coordinate_set_equal": True,
                "modular_nonzero_witness": "PASS",
                "status": "PASS",
            }
        )
    return {
        "status": "PASS",
        "classes": len(checks),
        "all_counts_equal": True,
        "all_coordinate_sets_equal": True,
        "checks": checks,
        "manifest": str(GI_MANIFEST.relative_to(ROOT)),
        "manifest_sha256": sha256_file(GI_MANIFEST),
    }


def validate_emitter_inventories(classes: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Aggregate the per-class production-emitter dry-run certificates."""
    _, _, _, custody = production_emitter_runtime()
    blocks = 0
    coordinates = 0
    generators = 0
    program_digests: list[str] = []
    for item in classes:
        evidence = item.get("production_emitter_dry_run", {})
        crosscheck = item.get("compact_reconstruction_crosscheck", {})
        if (
            item.get("generator_count_source")
            != "production_gi_only_emitter_count_only_dry_run_v1"
            or evidence.get("status") != "PASS"
            or evidence.get("mode")
            != "production_gi_only_emitter_count_only_dry_run_v1"
            or not evidence.get("all_coordinate_rows_equal_compact_crosscheck")
            or not evidence.get("all_dynamic_statements_consumed")
            or not evidence.get("final_H_cap_sufficient")
            or not evidence.get("semantic_phase_order_verified")
            or not evidence.get("fixed_program_digest_verified_before_interpretation")
            or not evidence.get("full_producer_sources_hash_pinned")
            or evidence.get("parser_negative_controls", {}).get("status") != "PASS"
            or crosscheck.get("status") != "PASS"
            or crosscheck.get("role") != "crosscheck_not_authoritative_generator_source"
            or not crosscheck.get("all_coordinate_rows_equal")
        ):
            raise AssertionError(
                f"incomplete production-emitter count certificate at "
                f"{item['receiver_key_string']}"
            )
        for name, value in custody.items():
            if evidence.get(name) != value:
                raise AssertionError(
                    f"production-emitter custody mismatch at {item['receiver_key_string']}: {name}"
                )
        if (
            evidence["unknowns_without_T"] != item["unknowns_without_T"]
            or evidence["coefficient_generators"] != item["coefficient_generators"]
            or evidence["coefficient_coordinate_sha256"]
            != item["coefficient_coordinate_sha256"]
            or item["modular_nonzero_witness"]["equals_structural_upper_set"] is not True
        ):
            raise AssertionError(
                f"production-emitter size mismatch at {item['receiver_key_string']}"
            )
        e, q = int(item["e"]), int(item["q"])
        blocks += 1 + e + (q - 1)
        coordinates += item["unknowns_without_T"] - 1
        generators += item["coefficient_generators"]
        program_digests.append(
            f"{item['receiver_key_string']}|{evidence['emitted_program_sha256']}\n"
        )
    return {
        "status": "PASS",
        "classes": len(classes),
        "blocks": blocks,
        "coefficient_coordinates_excluding_c": coordinates,
        "h_adic_coefficient_generators": generators,
        "all_support_sets_equal": True,
        "all_gauges_equal": True,
        "all_unknown_counts_equal": True,
        "all_generator_counts_from_production_emitted_programs": True,
        "all_emitted_coordinate_sets_equal_compact_crosscheck": True,
        "all_dynamic_statements_consumed": True,
        "all_final_H_caps_sufficient": True,
        "all_semantic_phase_orders_verified": True,
        "all_fixed_program_digests_verified_before_interpretation": True,
        "all_producer_sources_hash_pinned": True,
        "parser_negative_controls": _PARSER_NEGATIVE_CONTROLS,
        "emitted_program_manifest_sha256": hashlib.sha256(
            "".join(sorted(program_digests)).encode("ascii")
        ).hexdigest(),
        **custody,
        "generator_count_scope": (
            "authoritative count-only interpretation of every fixed production "
            "emitted row program; compact reconstruction is an all-coordinate "
            "crosscheck; canonical six additionally equal materialized h-adic rows"
        ),
    }


def build_payload(rows_path: Path, expected_rows: int = 66) -> dict[str, Any]:
    survivors = load_nonempty_rows(rows_path)
    if expected_rows and len(survivors) != expected_rows:
        raise AssertionError(
            f"expected {expected_rows} NONEMPTY residual rows, found {len(survivors)}"
        )
    grouped: dict[ReceiverKey, list[tuple[int, dict[str, Any]]]] = {}
    for line_number, row in survivors:
        grouped.setdefault(child_key(row["own"]), []).append((line_number, row))

    cache: dict[ReceiverKey, dict[str, Any]] = {}
    canonical_validation = validate_canonical_six(cache)
    classes = []
    for key, members in grouped.items():
        if key not in cache:
            cache[key] = chart_counts_for_receiver(*key)
        count = dict(cache[key])
        count["residual_row_count"] = len(members)
        count["own_rows_jsonl_lines"] = [line_number for line_number, _ in members]
        count["source_degrees"] = sorted(
            {
                (int(row["source_row"]["n"]), int(row["source_row"]["m"]))
                for _, row in members
            }
        )
        count["descent_licenses"] = sorted(
            {str(row["own"]["descent_license"]) for _, row in members}
        )
        count["terminal_scopes"] = sorted(
            {str(row["own"]["characteristic_scope"]) for _, row in members}
        )
        classes.append(count)
    classes.sort(
        key=lambda item: (
            item["unknowns_without_T"],
            item["coefficient_generators"],
            item["receiver_key_string"],
        )
    )
    emitter_validation = validate_emitter_inventories(classes)
    return {
        "schema": "jc2.residual66.gi-chart-counts/v1",
        "status": "PASS",
        "scope": (
            "sizes of necessary G_i receiver charts; a residual row is a "
            "necessary configuration, and chart size is not a difficulty proof"
        ),
        "input": str(rows_path.resolve().relative_to(ROOT)),
        "input_sha256": sha256_file(rows_path),
        "residual_rows": len(survivors),
        "distinct_receiver_classes": len(classes),
        "receiver_key_fields": [
            "n_prime", "m_prime", "M_terminal_prime", "ell"
        ],
        "minimum_unknowns_without_T": min(
            (item["unknowns_without_T"] for item in classes), default=None
        ),
        "maximum_unknowns_without_T": max(
            (item["unknowns_without_T"] for item in classes), default=None
        ),
        "exact_q_demo_threshold": 60,
        "exact_q_demo_triggered": any(
            item["unknowns_without_T"] <= 60 for item in classes
        ),
        "count_method": {
            "authoritative_generator_source": (
                "count-only interpretation of the fixed row program rendered "
                "through the production G_i-only emitter path for every class"
            ),
            "structural_upper_set": (
                "interval-support interpretation of the emitted formal Jacobian "
                "and determinate monic h-adic division program"
            ),
            "exactness_certificate": (
                "deterministic modular interpretation of the same emitted program "
                "is nonzero at every emitted structural coordinate"
            ),
            "compact_reconstruction_role": "all-coordinate crosscheck only",
            "prime": WITNESS_PRIME,
            "no_coefficient_expression_emission": True,
            "no_solver_run": True,
        },
        "emitter_inventory_validation": emitter_validation,
        "canonical_six_validation": canonical_validation,
        "classes": classes,
    }


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_ROWS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--expected-rows", type=int, default=66,
        help="refuse stale residual input; use 0 to disable the count gate",
    )
    parser.add_argument(
        "--stdout", action="store_true", help="also print the complete JSON payload"
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    rows_path = args.input.resolve()
    output_path = args.output.resolve()
    payload = build_payload(rows_path, args.expected_rows)
    atomic_json(output_path, payload)
    try:
        output_label = str(output_path.relative_to(ROOT))
    except ValueError:
        output_label = str(output_path)
    summary = {
        "status": payload["status"],
        "output": output_label,
        "residual_rows": payload["residual_rows"],
        "distinct_receiver_classes": payload["distinct_receiver_classes"],
        "minimum_unknowns_without_T": payload["minimum_unknowns_without_T"],
        "maximum_unknowns_without_T": payload["maximum_unknowns_without_T"],
        "exact_q_demo_triggered": payload["exact_q_demo_triggered"],
        "canonical_six_validation": payload["canonical_six_validation"]["status"],
    }
    print(json.dumps(payload if args.stdout else summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
