#!/usr/bin/env python3
"""Integer-only census of numerical Keller boundary-cluster profiles.

This program intentionally proves only a necessary numerical condition.  A
successful row has type

    artifact=NUMERICAL_PROFILE, attainment=NECESSARY.

For an exactly replayed forest, ``m_C>=0`` and ``c_C=Z.C>=0`` do certify global
nefness: the recurrences give ``Z=sum m_C C`` on the actual blown-up surface;
a non-boundary irreducible curve has non-negative intersection with each
distinct boundary curve.  This does not certify existence of a pencil,
existence of a polynomial map, or a Keller counterexample.

No CAS or non-standard Python package is used.  Run ``self-test`` before a
census; use ``plan`` to inspect the profile-row count without enumerating
clusters.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from hashlib import sha256
import json
from math import isfinite, isqrt
import os
from pathlib import Path
import sys
import tempfile
import time
from typing import Sequence


sys.setrecursionlimit(max(sys.getrecursionlimit(), 10_000))


SCHEMA = "keller-cluster-census/v1"
ENGINE_REVISION = "20260902.8"
ARTIFACT = "NUMERICAL_PROFILE"
ATTAINMENT = "NECESSARY"
GENERATED_PROFILE_CORPUS_ID = f"generated:H2-common-n@{ENGINE_REVISION}"
MAX_AXIS_VALUES = 1_000_000
MAX_ND_CELLS = 2_000_000
LINE = -1


class InputError(ValueError):
    """An input is ambiguous or lies outside the declared mode."""


class InternalInvariantError(RuntimeError):
    """A supposedly exhaustive engine path violated its own invariants."""


def _reject_duplicate_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise InputError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json_loads(text: str) -> object:
    return json.loads(text, object_pairs_hook=_reject_duplicate_pairs)


def _canonical_json(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    )


def _json_exact_equal(left: object, right: object) -> bool:
    """JSON-tree equality which keeps booleans, integers, and floats distinct."""

    try:
        return _canonical_json(left) == _canonical_json(right)
    except (TypeError, ValueError):
        return False


@dataclass(frozen=True, order=True)
class DicriticalDatum:
    """One H2 dicritical: covering degree s and ramification length mu."""

    s: int
    mu: int

    @property
    def supported_sheets(self) -> int:
        return self.s * self.mu


@dataclass(frozen=True)
class Profile:
    N: int
    D: int
    fixed_sheets: int
    W: int
    dicriticals: tuple[DicriticalDatum, ...]
    S: int
    n: int
    kappa: int
    T: int
    sum_a: int
    n_floor: int
    n_upper: int
    window: str
    f_cap: int | None
    mode: str = "H2-common-n"
    component_degrees: tuple[int, ...] = ()

    @property
    def expected_dicritical_degrees(self) -> tuple[int, ...]:
        degrees = self.component_degrees or (self.n,) * len(self.dicriticals)
        return tuple(sorted(d.s * degree for d, degree in zip(self.dicriticals, degrees)))

    @property
    def id(self) -> str:
        ds = ",".join(f"{d.s}x{d.mu}" for d in self.dicriticals)
        degree_tag = (
            str(self.n)
            if self.mode == "H2-common-n"
            else "[" + ",".join(map(str, self.component_degrees)) + "]"
        )
        return (
            f"N{self.N}-D{self.D}-a{self.fixed_sheets}-W{self.W}-"
            f"dic[{ds}]-n{degree_tag}-k{self.kappa}-T{self.T}"
        )

    def as_dict(self) -> dict[str, object]:
        return {
            "id": self.id,
            "N": self.N,
            "D": self.D,
            "a": self.fixed_sheets,
            "W": self.W,
            "dicritical_multiset": [
                {"s": d.s, "mu": d.mu} for d in self.dicriticals
            ],
            "S": self.S,
            "n": self.n if self.mode == "H2-common-n" else None,
            "component_degrees": (
                list(self.component_degrees) if self.component_degrees else None
            ),
            "kappa": self.kappa,
            "T": self.T,
            "sum_a": self.sum_a,
            "sum_a2": self.D * self.D - self.N,
            "n_floor": self.n_floor,
            "n_upper": self.n_upper,
            "f_cap": self.f_cap if self.f_cap is not None else "unbounded",
            "window": self.window,
            "mode": self.mode,
        }


def _profile_invariant_failures(profile: Profile) -> list[str]:
    """Return semantic failures which an exhaustive census must never ignore."""

    failures: list[str] = []
    exact_ints = {
        "N": profile.N,
        "D": profile.D,
        "a": profile.fixed_sheets,
        "W": profile.W,
        "S": profile.S,
        "n": profile.n,
        "kappa": profile.kappa,
        "T": profile.T,
        "sum_a": profile.sum_a,
        "n_floor": profile.n_floor,
        "n_upper": profile.n_upper,
    }
    if any(not isinstance(value, int) or isinstance(value, bool) for value in exact_ints.values()):
        failures.append("profile scalar is not an exact integer")
        return failures
    if profile.N < 2 or profile.D < 1:
        failures.append("N>=2 and D>=1 required")
    if not 0 <= profile.fixed_sheets <= profile.N - 2:
        failures.append("a lies outside 0..N-2")
    if profile.W != profile.N - profile.fixed_sheets:
        failures.append("W+a=N failed")
    if not profile.dicriticals:
        failures.append("dicritical multiset is empty")
    if any(
        not isinstance(item.s, int)
        or isinstance(item.s, bool)
        or item.s < 1
        or not isinstance(item.mu, int)
        or isinstance(item.mu, bool)
        or item.mu < 2
        for item in profile.dicriticals
    ):
        failures.append("invalid dicritical (s,mu)")
    if sum(item.supported_sheets for item in profile.dicriticals) != profile.W:
        failures.append("dicritical multiplicities do not account for W")
    if profile.S != sum(item.s for item in profile.dicriticals):
        failures.append("S is not sum s_l")
    if profile.S < 1 or 2 * profile.S > profile.W:
        failures.append("2S<=W failed")
    if not 1 <= profile.kappa <= profile.N or profile.T < 0:
        failures.append("kappa or T outside its range")

    ramification = 0
    if profile.mode == "H2-common-n":
        denominator = profile.W - profile.S
        if denominator <= 0:
            failures.append("W-S must be positive")
        else:
            expected_floor = ceil_div(profile.N - 1, denominator) + 1
            if profile.n_floor != expected_floor or profile.n < expected_floor:
                failures.append("MERIDIAN-FLOOR+ metadata failed")
            split_upper = (profile.D - profile.kappa) // profile.S
            if profile.f_cap is None:
                expected_upper = split_upper
            elif not isinstance(profile.f_cap, int) or isinstance(profile.f_cap, bool):
                failures.append("f cap is not an exact integer")
                expected_upper = profile.n_upper
            else:
                expected_upper = min(
                    split_upper,
                    (3 * profile.N + profile.f_cap) // denominator,
                )
            if profile.n_upper != expected_upper or profile.n > profile.n_upper:
                failures.append("n upper-endpoint metadata failed")
        if profile.component_degrees:
            failures.append("common-n profile has component degree overrides")
        if profile.window not in {"strict", "legacy-inclusive", "all-h2", "explicit"}:
            failures.append("unknown H2 window")
        elif profile.window == "strict" and not (
            2 * profile.fixed_sheets > profile.N
            and profile.fixed_sheets <= profile.N - 2
        ):
            failures.append("strict fixed-sheet window failed")
        elif profile.window == "legacy-inclusive" and not (
            2 * profile.fixed_sheets >= profile.N
            and profile.fixed_sheets <= profile.N - 2
        ):
            failures.append("legacy-inclusive fixed-sheet window failed")
        degrees = (profile.n,) * len(profile.dicriticals)
        ramification = profile.n * (profile.W - profile.S)
    elif profile.mode == "explicit-component-degrees":
        if profile.window != "explicit-component-degrees" or profile.f_cap is not None:
            failures.append("explicit-component mode metadata failed")
        if profile.n != 0 or profile.n_floor != 0 or profile.n_upper != 0:
            failures.append("explicit-component sentinel fields failed")
        if len(profile.component_degrees) != len(profile.dicriticals) or any(
            not isinstance(value, int) or isinstance(value, bool) or value < 2
            for value in profile.component_degrees
        ):
            failures.append("invalid component-degree tuple")
        degrees = profile.component_degrees
        ramification = sum(
            (item.mu - 1) * item.s * degree
            for item, degree in zip(profile.dicriticals, degrees)
        )
    else:
        failures.append("unknown profile mode")
        degrees = ()

    polar_dic_sum = sum(
        item.s * degree for item, degree in zip(profile.dicriticals, degrees)
    )
    if profile.D != polar_dic_sum + profile.kappa + profile.T:
        failures.append("DEG-SPLIT failed")
    if profile.sum_a != 3 * profile.D - 2 * profile.N - profile.kappa + ramification:
        failures.append("NOETHER-K sum failed")
    if profile.sum_a <= 0:
        failures.append("sum a_i is nonpositive")
    return failures


def explicit_profile_corpus_id(profiles: Sequence[Profile]) -> str:
    """Hash a validated semantic corpus, independent of file order/spacing."""

    if not profiles:
        raise InputError("explicit component profile corpus is empty")
    duplicate_ids = [
        profile_id
        for profile_id, count in Counter(profile.id for profile in profiles).items()
        if count > 1
    ]
    if duplicate_ids:
        raise InputError(f"duplicate explicit profiles: {sorted(duplicate_ids)}")
    for profile in profiles:
        failures = _profile_invariant_failures(profile)
        if failures:
            raise InputError(f"invalid explicit profile {profile.id}: {failures}")
    payload = {
        "schema": SCHEMA,
        "engine_revision": ENGINE_REVISION,
        "mode": "explicit-component-degrees",
        "dicritical_neighbour": True,
        "profiles": [profile.as_dict() for profile in sorted(profiles, key=lambda p: p.id)],
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return "sha256:" + sha256(canonical.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class State:
    """A partial chronological blow-up cluster.

    Component 0 is the strict transform of L_infty.  Point i (zero based in
    public output) creates component i+1.  ``parents`` stores component ids,
    hence 0 denotes L_infty and j+1 denotes point j.
    """

    multiplicities: tuple[int, ...]
    parents: tuple[tuple[int, ...], ...]
    adjacency: tuple[frozenset[int], ...]
    m: tuple[int, ...]
    c: tuple[int, ...]
    free_sum: int
    satellite_sum: int
    square_sum: int

    @property
    def total_sum(self) -> int:
        return self.free_sum + self.satellite_sum

    @property
    def last_multiplicity(self) -> int:
        return self.multiplicities[-1] if self.multiplicities else 10**30


@dataclass
class SearchStats:
    expanded_states: int = 0
    generated_states: int = 0
    symmetry_duplicates: int = 0
    terminal_states: int = 0
    point_cap_prunes: int = 0
    resource_stop: str | None = None


def ceil_div(a: int, b: int) -> int:
    if b <= 0:
        raise InputError("ceiling denominator must be positive")
    return -((-a) // b)


def dicritical_multisets(W: int) -> tuple[tuple[DicriticalDatum, ...], ...]:
    """All unlabeled multisets with mu>=2 and sum(s*mu)=W."""

    if W < 0:
        return ()
    if W == 0:
        return ((),)
    kinds = [
        DicriticalDatum(s, mu)
        for s in range(1, W // 2 + 1)
        for mu in range(2, W // s + 1)
        if s * mu <= W
    ]
    kinds.sort()
    out: list[tuple[DicriticalDatum, ...]] = []
    stack: list[tuple[int, int, tuple[DicriticalDatum, ...]]] = [(W, 0, ())]
    while stack:
        remaining, start, chosen = stack.pop()
        if remaining == 0:
            out.append(chosen)
            continue
        for pos in range(len(kinds) - 1, start - 1, -1):
            datum = kinds[pos]
            weight = datum.supported_sheets
            if weight <= remaining:
                stack.append((remaining - weight, pos, chosen + (datum,)))
    out.sort()
    return tuple(out)


def fixed_sheet_values(N: int, window: str, explicit: Sequence[int]) -> tuple[int, ...]:
    """Return declared values of the covering fixed-sheet count a."""

    if window != "explicit" and explicit:
        raise InputError("explicit a-values require the explicit H2 window")
    if window == "strict":
        start, stop = N // 2 + 1, N - 1  # 2a>N and a<=N-2
        count = max(0, stop - start)
        if count > MAX_AXIS_VALUES:
            raise InputError(
                "fixed-sheet window is too large to materialize; "
                "use --window explicit --a-values"
            )
        values = range(start, stop)
    elif window == "legacy-inclusive":
        start, stop = ceil_div(N, 2), N - 1
        count = max(0, stop - start)
        if count > MAX_AXIS_VALUES:
            raise InputError(
                "fixed-sheet window is too large to materialize; "
                "use --window explicit --a-values"
            )
        values = range(start, stop)
    elif window == "all-h2":
        count = max(0, N - 1)
        if count > MAX_AXIS_VALUES:
            raise InputError(
                "fixed-sheet window is too large to materialize; "
                "use --window explicit --a-values"
            )
        values = range(0, N - 1)
    elif window == "explicit":
        if not explicit:
            raise InputError("--window explicit requires --a-values")
        values = explicit
    else:
        raise InputError(f"unknown profile window: {window}")
    clean = tuple(sorted(set(int(v) for v in values)))
    if any(v < 0 or v > N - 2 for v in clean):
        raise InputError("each a must satisfy 0 <= a <= N-2 in H2 mode")
    return clean


def generate_profiles(
    N: int,
    D: int,
    *,
    window: str = "strict",
    a_values: Sequence[int] = (),
    f_cap: int | None = None,
    arithmetic_prefilter: bool = True,
) -> tuple[Profile, ...]:
    """Enumerate every promoted common-n/H2 parameter row at fixed (N,D)."""

    if N < 2:
        raise InputError("noninvertible profile generation requires N>=2")
    if D < 1:
        raise InputError("D must be positive")
    rows: list[Profile] = []
    for fixed in fixed_sheet_values(N, window, a_values):
        W = N - fixed
        for dic in dicritical_multisets(W):
            if not dic:
                continue
            S = sum(d.s for d in dic)
            if S <= 0 or 2 * S > W:
                continue
            denominator = W - S
            floor = ceil_div(N - 1, denominator) + 1
            for kappa in range(1, N + 1):
                split_upper = (D - kappa) // S
                if f_cap is None:
                    upper = split_upper
                else:
                    # This is the coarse upper endpoint requested in the charge.
                    # It is never silently enabled: f_cap is serialized per row.
                    defect_upper = (3 * N + f_cap) // denominator
                    upper = min(split_upper, defect_upper)
                for n in range(floor, upper + 1):
                    T = D - S * n - kappa
                    if T < 0:
                        continue
                    sum_a = 3 * D - 2 * N - kappa + n * denominator
                    if sum_a <= 0:
                        continue
                    # Every positive integer x has x^2 == x (mod 2).
                    if arithmetic_prefilter and (D * D - N - sum_a) % 2:
                        continue
                    rows.append(
                        Profile(
                            N=N,
                            D=D,
                            fixed_sheets=fixed,
                            W=W,
                            dicriticals=dic,
                            S=S,
                            n=n,
                            kappa=kappa,
                            T=T,
                            sum_a=sum_a,
                            n_floor=floor,
                            n_upper=upper,
                            window=window,
                            f_cap=f_cap,
                        )
                    )
    rows.sort(key=lambda p: p.id)
    return tuple(rows)


def load_explicit_component_profiles(path: Path) -> tuple[Profile, ...]:
    """Load fail-closed non-common-n rows with every missing datum declared.

    The file may be one JSON array or JSON Lines.  Each row must contain N, D,
    a, kappa, ``dicritical_neighbour=true``, and dicritical objects with positive
    integer s, mu>=2, and integer n_c>=2.  This mode uses the general
    DEG-SPLIT and NOETHER ramification sums; it does not apply MERIDIAN-FLOOR+.
    """

    text = path.read_text(encoding="utf-8")
    try:
        decoded = strict_json_loads(text)
        raw_rows = decoded if isinstance(decoded, list) else [decoded]
    except json.JSONDecodeError:
        raw_rows = [strict_json_loads(line) for line in text.splitlines() if line.strip()]
    if not raw_rows:
        raise InputError("explicit component profile file contains no rows")
    profiles: list[Profile] = []

    def integer(row: dict[str, object], key: str, *, minimum: int) -> int:
        value = row.get(key)
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise InputError(f"explicit profile {key} must be an integer >= {minimum}")
        return value

    for raw in raw_rows:
        if not isinstance(raw, dict):
            raise InputError("each explicit profile must be a JSON object")
        allowed = {"N", "D", "a", "kappa", "dicritical_neighbour", "dicriticals"}
        unknown = set(raw) - allowed
        if unknown:
            raise InputError(f"unknown explicit profile keys: {sorted(unknown)}")
        N = integer(raw, "N", minimum=2)
        D = integer(raw, "D", minimum=1)
        fixed = integer(raw, "a", minimum=0)
        kappa = integer(raw, "kappa", minimum=1)
        if kappa > N:
            raise InputError("explicit profile must satisfy kappa<=N")
        if raw.get("dicritical_neighbour") is not True:
            raise InputError(
                "explicit component profile must declare dicritical_neighbour=true"
            )
        raw_dic = raw.get("dicriticals")
        if not isinstance(raw_dic, list) or not raw_dic:
            raise InputError("explicit profile dicriticals must be a nonempty array")
        paired_data: list[tuple[DicriticalDatum, int]] = []
        for item in raw_dic:
            if not isinstance(item, dict):
                raise InputError("each explicit dicritical must be an object")
            unknown_item = set(item) - {"s", "mu", "n_c"}
            if unknown_item:
                raise InputError(f"unknown explicit dicritical keys: {sorted(unknown_item)}")
            s = integer(item, "s", minimum=1)
            mu = integer(item, "mu", minimum=2)
            n_c = integer(item, "n_c", minimum=2)
            paired_data.append((DicriticalDatum(s, mu), n_c))
        paired_data.sort(key=lambda pair: (pair[0], pair[1]))
        dic = [pair[0] for pair in paired_data]
        component_degrees = [pair[1] for pair in paired_data]
        W = sum(item.supported_sheets for item in dic)
        if fixed + W != N:
            raise InputError("explicit profile violates W+a=N")
        S = sum(item.s for item in dic)
        Lambda = sum(item.s * degree for item, degree in zip(dic, component_degrees))
        T = D - Lambda - kappa
        if T < 0:
            raise InputError("explicit profile has negative T")
        ramification = sum(
            (item.mu - 1) * item.s * degree
            for item, degree in zip(dic, component_degrees)
        )
        sum_a = 3 * D - 2 * N - kappa + ramification
        if sum_a <= 0:
            raise InputError("explicit profile has nonpositive sum a_i")
        profiles.append(
            Profile(
                N=N,
                D=D,
                fixed_sheets=fixed,
                W=W,
                dicriticals=tuple(dic),
                S=S,
                n=0,
                kappa=kappa,
                T=T,
                sum_a=sum_a,
                n_floor=0,
                n_upper=0,
                window="explicit-component-degrees",
                f_cap=None,
                mode="explicit-component-degrees",
                component_degrees=tuple(component_degrees),
            )
        )
    profiles.sort(key=lambda profile: profile.id)
    duplicate_ids = [
        profile_id
        for profile_id, count in Counter(profile.id for profile in profiles).items()
        if count > 1
    ]
    if duplicate_ids:
        raise InputError(f"duplicate explicit profiles: {sorted(duplicate_ids)}")
    result = tuple(profiles)
    # Validate all derived equations before this user-supplied corpus can enter
    # an exhaustive row.  The same canonical semantics are hashed at run time.
    explicit_profile_corpus_id(result)
    return result


def _normalise_parent(parent: object, point_index: int) -> int:
    if isinstance(parent, str) and parent in {"L", "L_inf"}:
        return 0
    if parent == -1 and isinstance(parent, int) and not isinstance(parent, bool):
        return 0
    if not isinstance(parent, int) or isinstance(parent, bool):
        raise InputError(f"point {point_index}: non-integer parent {parent!r}")
    if parent < 0 or parent >= point_index:
        raise InputError(f"point {point_index}: parent {parent} is not earlier")
    return parent + 1


def validate_cluster(
    D: int,
    multiplicities: Sequence[int],
    parents: Sequence[Sequence[object]],
    *,
    expected_N: int | None = None,
) -> dict[str, object]:
    """Validate an infinity cluster and derive the complete polar labeling."""

    errors: list[str] = []
    if not isinstance(D, int) or isinstance(D, bool) or D < 1:
        errors.append("D must be a positive integer")
    if (
        expected_N is not None
        and (
            not isinstance(expected_N, int)
            or isinstance(expected_N, bool)
            or expected_N < 1
        )
    ):
        errors.append("expected N must be a positive integer")
    if len(multiplicities) != len(parents):
        errors.append("multiplicities/parents length mismatch")
    if any(not isinstance(v, int) or isinstance(v, bool) or v < 1 for v in multiplicities):
        errors.append("all base multiplicities must be positive integers")
    if errors:
        return {"ok": False, "errors": errors}

    adjacency: list[set[int]] = [set()]
    m: list[int] = [D]
    internal_parents: list[tuple[int, ...]] = []
    for i, raw in enumerate(parents):
        if not isinstance(raw, (list, tuple)):
            errors.append(f"point {i}: parent row must be an array")
            raw = ()
        try:
            pp = tuple(_normalise_parent(v, i) for v in raw)
        except InputError as exc:
            errors.append(str(exc))
            pp = ()
        if len(pp) not in {1, 2}:
            errors.append(f"point {i}: an infinity center must meet one or two components")
        if len(set(pp)) != len(pp):
            errors.append(f"point {i}: duplicate center component")
        if len(pp) == 2 and pp[1] not in adjacency[pp[0]]:
            errors.append(f"point {i}: satellite parents were not adjacent")
        ai = multiplicities[i]
        mi = sum(m[q] for q in pp) - ai if pp else -ai
        m.append(mi)
        new_id = i + 1
        adjacency.append(set(pp))
        if len(pp) == 2:
            adjacency[pp[0]].discard(pp[1])
            adjacency[pp[1]].discard(pp[0])
        for q in pp:
            adjacency[q].add(new_id)
        internal_parents.append(pp)

    c = [D] + list(multiplicities)
    for i, pp in enumerate(internal_parents):
        ai = multiplicities[i]
        for q in pp:
            c[q] -= ai
    square_sum = sum(v * v for v in multiplicities)
    N = D * D - square_sum
    T = sum(
        multiplicities[i]
        for i, pp in enumerate(internal_parents)
        if len(pp) == 2
    )
    sheets = [i for i, (mm, cc) in enumerate(zip(m, c)) if mm > 0 and cc > 0]
    dicriticals = [i for i, (mm, cc) in enumerate(zip(m, c)) if mm == 0 and cc > 0]
    contracted = [i for i, cc in enumerate(c) if cc == 0]
    kappa = sum(c[i] for i in sheets)
    Lambda = sum(c[i] for i in dicriticals)
    i2 = sum(m[i] * c[i] for i in sheets)
    if any(v < 0 for v in m):
        errors.append("a polar multiplicity m_C is negative")
    if any(v < 0 for v in c):
        errors.append("a boundary intersection c_C is negative")
    if expected_N is not None and N != expected_N:
        errors.append(f"Z^2={N}, expected {expected_N}")
    if i2 != N:
        errors.append(f"I2 gives {i2}, while Z^2 gives {N}")
    if kappa + Lambda + T != D:
        errors.append("DEG-SPLIT boundary identity failed")

    def public_component(component: int) -> str | int:
        return "L" if component == 0 else component - 1

    result: dict[str, object] = {
        "ok": not errors,
        "errors": errors,
        "D": D,
        "N": N,
        "sum_a": sum(multiplicities),
        "sum_a2": square_sum,
        "multiplicities": list(multiplicities),
        "forest_shape": [
            [public_component(q) for q in pp] for pp in internal_parents
        ],
        "m": m,
        "c": c,
        "boundary_nef": all(v >= 0 for v in c),
        "global_nef_certified": all(v >= 0 for v in m) and all(v >= 0 for v in c),
        "effective_polar_boundary": all(v >= 0 for v in m),
        "kappa": kappa,
        "Lambda": Lambda,
        "T": T,
        "sheets": [
            {"component": public_component(i), "m": m[i], "k": c[i]}
            for i in sheets
        ],
        "dicritical_components": [
            {
                "component": public_component(i),
                "degree": c[i],
                "positive_m_neighbours": [
                    public_component(j) for j in sorted(adjacency[i]) if m[j] > 0
                ],
            }
            for i in dicriticals
        ],
        "contracted_components": [public_component(i) for i in contracted],
        "adjacency": [
            [public_component(j) for j in sorted(neighbours)]
            for neighbours in adjacency
        ],
        "artifact": ARTIFACT,
        "attainment": ATTAINMENT,
    }
    return result


def match_profile(
    cluster: dict[str, object],
    profile: Profile,
    *,
    affine_ramification: int = 0,
    enforce_meridian_floor: bool = True,
) -> tuple[bool, list[str], list[dict[str, object]]]:
    """Check NOETHER-K, H2 dicritical data, DN, and all aggregates."""

    failures: list[str] = []
    if not cluster.get("ok"):
        failures.append("polar cluster failed")
        return False, failures, []
    if cluster["D"] != profile.D or cluster["N"] != profile.N:
        failures.append("(D,N) mismatch")
    if cluster["kappa"] != profile.kappa:
        failures.append("derived kappa mismatch")
    if cluster["T"] != profile.T:
        failures.append("derived satellite mass mismatch")
    if cluster["sum_a"] != profile.sum_a + affine_ramification:
        failures.append("NOETHER-K affine-residual mismatch")
    polar_dic_sum = sum(profile.expected_dicritical_degrees)
    if profile.D != polar_dic_sum + profile.kappa + profile.T:
        failures.append("profile DEG-SPLIT mismatch")
    if profile.W != profile.N - profile.fixed_sheets:
        failures.append("W+a=N failed")
    if sum(d.supported_sheets for d in profile.dicriticals) != profile.W:
        failures.append("dicritical multiplicities do not account for W")
    if (
        enforce_meridian_floor
        and profile.mode == "H2-common-n"
        and profile.n < profile.n_floor
    ):
        failures.append("MERIDIAN-FLOOR+ failed")

    actual = sorted(cluster["dicritical_components"], key=lambda row: int(row["degree"]))
    component_degrees = profile.component_degrees or (profile.n,) * len(profile.dicriticals)
    data = sorted(
        zip(profile.dicriticals, component_degrees),
        key=lambda pair: pair[0].s * pair[1],
    )
    expected_degrees = [datum.s * degree for datum, degree in data]
    if [int(row["degree"]) for row in actual] != expected_degrees:
        failures.append("dicritical boundary degrees mismatch")
        return False, failures, []
    groups: list[dict[str, object]] = []
    m_values = cluster["m"]
    by_degree_actual: dict[int, list[dict[str, object]]] = defaultdict(list)
    by_degree_data: dict[int, list[tuple[DicriticalDatum, int]]] = defaultdict(list)
    for row in actual:
        by_degree_actual[int(row["degree"])].append(row)
    for datum, component_degree in data:
        by_degree_data[datum.s * component_degree].append((datum, component_degree))
    for degree in sorted(by_degree_actual):
        rows = by_degree_actual[degree]
        declared = by_degree_data[degree]
        rendered_rows = []
        for row in rows:
            neighbours = row["positive_m_neighbours"]
            if len(neighbours) != 1:
                failures.append("DICRITICAL-NEIGHBOUR uniqueness failed")
                neighbour: object = None
            else:
                neighbour = neighbours[0]
                internal = 0 if neighbour == "L" else int(neighbour) + 1
                if int(m_values[internal]) != degree:
                    failures.append("DICRITICAL-NEIGHBOUR m=s*n_c failed")
            rendered_rows.append(
                {
                    "component": row["component"],
                    "positive_m_neighbour": neighbour,
                }
            )
        declarations = [
            {"s": datum.s, "mu": datum.mu, "n_c": component_degree}
            for datum, component_degree in declared
        ]
        groups.append(
            {
                "degree": degree,
                "components": rendered_rows,
                "profile_multiset": declarations,
                "mu_attachment": (
                    "UNIQUE" if len(rows) == 1 else "UNPINNED_WITHIN_EQUAL_DEGREE_GROUP"
                ),
            }
        )
    return not failures, failures, groups


def _max_square_with_sum(total: int, maximum: int) -> int:
    if total == 0:
        return 0
    if maximum <= 0:
        return -1
    count, remainder = divmod(total, maximum)
    return count * maximum * maximum + remainder * remainder


def _partition_feasible(
    free_sum: int, satellite_sum: int, square_sum: int, maximum: int
) -> bool:
    total = free_sum + satellite_sum
    if min(free_sum, satellite_sum, square_sum) < 0:
        return False
    if total == 0:
        return square_sum == 0
    if maximum < 1 or square_sum < total or (square_sum - total) % 2:
        return False
    max_square = _max_square_with_sum(free_sum, maximum)
    max_square += _max_square_with_sum(satellite_sum, maximum)
    return square_sum <= max_square


def _add_point(state: State, center: tuple[int, ...], a: int) -> State:
    new_id = len(state.multiplicities) + 1
    adjacency = [set(v) for v in state.adjacency]
    if len(center) == 2:
        adjacency[center[0]].remove(center[1])
        adjacency[center[1]].remove(center[0])
    adjacency.append(set(center))
    for q in center:
        adjacency[q].add(new_id)
    c = list(state.c)
    for q in center:
        c[q] -= a
    c.append(a)
    return State(
        multiplicities=state.multiplicities + (a,),
        parents=state.parents + (center,),
        adjacency=tuple(frozenset(v) for v in adjacency),
        m=state.m + (sum(state.m[q] for q in center) - a,),
        c=tuple(c),
        free_sum=state.free_sum + (a if len(center) == 1 else 0),
        satellite_sum=state.satellite_sum + (a if len(center) == 2 else 0),
        square_sum=state.square_sum + a * a,
    )


def _state_from_public_cluster(
    D: int,
    multiplicities: Sequence[int],
    parents: Sequence[Sequence[object]],
) -> State:
    """Reconstruct the exact colored state after a successful validation."""

    state = State((), (), (frozenset(),), (D,), (D,), 0, 0, 0)
    for point_index, (value, raw_parents) in enumerate(zip(multiplicities, parents)):
        center = tuple(
            _normalise_parent(parent, point_index) for parent in raw_parents
        )
        state = _add_point(state, center, value)
    return state


def _vertex_attributes(state: State) -> tuple[tuple[int, ...], ...]:
    children: list[list[int]] = [[] for _ in state.m]
    for child, pp in enumerate(state.parents, 1):
        for parent in pp:
            children[parent].append(child)
    attrs = []
    for v in range(len(state.m)):
        attrs.append(
            (
                int(v == 0),
                0 if v == 0 else state.multiplicities[v - 1],
                state.m[v],
                state.c[v],
                0 if v == 0 else len(state.parents[v - 1]),
                len(children[v]),
                len(state.adjacency[v]),
            )
        )
    return tuple(attrs)


def _joint_colors(a: State, b: State) -> tuple[tuple[int, ...], tuple[int, ...]] | None:
    attrs_a, attrs_b = _vertex_attributes(a), _vertex_attributes(b)
    universe = {value for value in attrs_a + attrs_b}
    ids = {value: i for i, value in enumerate(sorted(universe))}
    ca = tuple(ids[v] for v in attrs_a)
    cb = tuple(ids[v] for v in attrs_b)

    def signatures(state: State, colors: tuple[int, ...]) -> tuple[tuple[object, ...], ...]:
        children: list[list[int]] = [[] for _ in colors]
        for child, pp in enumerate(state.parents, 1):
            for parent in pp:
                children[parent].append(child)
        values = []
        for v in range(len(colors)):
            pp = () if v == 0 else state.parents[v - 1]
            values.append(
                (
                    colors[v],
                    tuple(sorted(colors[q] for q in pp)),
                    tuple(sorted(colors[q] for q in children[v])),
                    tuple(sorted(colors[q] for q in state.adjacency[v])),
                )
            )
        return tuple(values)

    while True:
        sa, sb = signatures(a, ca), signatures(b, cb)
        all_signatures = {value for value in sa + sb}
        mapping = {value: i for i, value in enumerate(sorted(all_signatures))}
        na = tuple(mapping[v] for v in sa)
        nb = tuple(mapping[v] for v in sb)
        if Counter(na) != Counter(nb):
            return None
        if na == ca and nb == cb:
            return na, nb
        ca, cb = na, nb


def _relation(state: State, u: int, v: int) -> tuple[bool, bool, bool]:
    u_parents = () if u == 0 else state.parents[u - 1]
    v_parents = () if v == 0 else state.parents[v - 1]
    return (v in u_parents, u in v_parents, v in state.adjacency[u])


def isomorphic(a: State, b: State) -> bool:
    """Exact colored directed-graph isomorphism; never hash-only deduplication."""

    if len(a.m) != len(b.m):
        return False
    colored = _joint_colors(a, b)
    if colored is None:
        return False
    ca, cb = colored
    by_color: dict[int, list[int]] = defaultdict(list)
    for v, color in enumerate(cb):
        by_color[color].append(v)
    mapping: dict[int, int] = {}
    used: set[int] = set()

    def compatible(u: int, v: int) -> bool:
        for old_u, old_v in mapping.items():
            if _relation(a, u, old_u) != _relation(b, v, old_v):
                return False
            if _relation(a, old_u, u) != _relation(b, old_v, v):
                return False
        return True

    def rec() -> bool:
        if len(mapping) == len(ca):
            return True
        choices: list[tuple[int, int, list[int]]] = []
        for u, color in enumerate(ca):
            if u in mapping:
                continue
            candidates = [v for v in by_color[color] if v not in used and compatible(u, v)]
            if not candidates:
                return False
            choices.append((len(candidates), u, candidates))
        _, u, candidates = min(choices, key=lambda row: (row[0], row[1]))
        for v in candidates:
            mapping[u] = v
            used.add(v)
            if rec():
                return True
            used.remove(v)
            del mapping[u]
        return False

    return rec()


def _isomorphism_bucket(state: State) -> tuple[object, ...]:
    """A broad invariant: isomorphic states always share it."""

    return (
        len(state.m),
        tuple(sorted(Counter(_vertex_attributes(state)).items())),
    )


def _state_to_public(state: State, D: int, N: int) -> dict[str, object]:
    parents = [
        ["L" if q == 0 else q - 1 for q in pp]
        for pp in state.parents
    ]
    return validate_cluster(D, state.multiplicities, parents, expected_N=N)


def enumerate_group(
    D: int,
    N: int,
    target_sum: int,
    target_T: int,
    profiles: Sequence[Profile],
    *,
    max_states: int | None,
    deadline: float | None,
    max_points: int | None,
) -> tuple[list[dict[str, object]], SearchStats, bool]:
    """Exhaust one (sum a, T) group, modulo exact forest isomorphism."""

    target_square = D * D - N
    target_free = target_sum - target_T
    stats = SearchStats()
    if not _partition_feasible(target_free, target_T, target_square, D):
        return [], stats, True
    initial = State((), (), (frozenset(),), (D,), (D,), 0, 0, 0)
    queue: deque[State] = deque([initial])
    seen: dict[tuple[object, ...], list[State]] = defaultdict(list)
    seen[_isomorphism_bucket(initial)].append(initial)
    records: list[dict[str, object]] = []
    complete = True

    while queue:
        if max_states is not None and stats.expanded_states >= max_states:
            stats.resource_stop = "max_states"
            complete = False
            break
        if deadline is not None and time.monotonic() >= deadline:
            stats.resource_stop = "deadline"
            complete = False
            break
        state = queue.pop()
        stats.expanded_states += 1
        rem_free = target_free - state.free_sum
        rem_sat = target_T - state.satellite_sum
        rem_square = target_square - state.square_sum
        if rem_free == rem_sat == rem_square == 0:
            stats.terminal_states += 1
            cluster = _state_to_public(state, D, N)
            if (
                cluster.get("ok") is not True
                or cluster.get("sum_a") != target_sum
                or cluster.get("T") != target_T
                or cluster.get("sum_a2") != target_square
                or cluster.get("global_nef_certified") is not True
            ):
                raise InternalInvariantError(
                    "terminal replay violated the enumerator invariants: "
                    + repr(cluster.get("errors"))
                )
            for profile in profiles:
                ok, failures, assignment = match_profile(cluster, profile)
                if ok:
                    records.append(
                        {
                            "profile": profile.as_dict(),
                            "tuple": {
                                "D": D,
                                "n": (
                                    profile.n if profile.mode == "H2-common-n" else None
                                ),
                                "component_degrees": (
                                    list(profile.component_degrees)
                                    if profile.component_degrees else None
                                ),
                                "S": profile.S,
                                "kappa": profile.kappa,
                                "T": profile.T,
                                "W": profile.W,
                                "a": profile.fixed_sheets,
                                "forest_shape": cluster["forest_shape"],
                                "multiplicities": cluster["multiplicities"],
                            },
                            "sheets": cluster["sheets"],
                            "dicriticals": assignment,
                            "boundary_nef": True,
                            "global_nef_certified": True,
                            "artifact": ARTIFACT,
                            "attainment": ATTAINMENT,
                        }
                    )
            continue
        if rem_free < 0 or rem_sat < 0 or rem_square < 0:
            continue
        if max_points is not None and len(state.multiplicities) >= max_points:
            stats.point_cap_prunes += 1
            complete = False
            continue
        maximum = min(state.last_multiplicity, isqrt(rem_square))
        if not _partition_feasible(rem_free, rem_sat, rem_square, maximum):
            continue

        centers: list[tuple[int, ...]] = []
        if rem_free:
            centers.extend((v,) for v in range(len(state.m)))
        if rem_sat:
            centers.extend(
                (u, v)
                for u in range(len(state.m))
                for v in sorted(state.adjacency[u])
                if u < v
            )
        for center in centers:
            category_remaining = rem_free if len(center) == 1 else rem_sat
            center_cap = min(state.c[q] for q in center)
            polar_cap = sum(state.m[q] for q in center)
            upper = min(maximum, category_remaining, center_cap, polar_cap)
            for value in range(upper, 0, -1):
                child = _add_point(state, center, value)
                child_rem_free = target_free - child.free_sum
                child_rem_sat = target_T - child.satellite_sum
                child_rem_square = target_square - child.square_sum
                if not _partition_feasible(
                    child_rem_free,
                    child_rem_sat,
                    child_rem_square,
                    value,
                ):
                    continue
                stats.generated_states += 1
                bucket = _isomorphism_bucket(child)
                if any(isomorphic(child, old) for old in seen[bucket]):
                    stats.symmetry_duplicates += 1
                    continue
                seen[bucket].append(child)
                queue.append(child)
    return records, stats, complete


def census_row(
    N: int,
    D: int,
    *,
    window: str,
    a_values: Sequence[int],
    f_cap: int | None,
    max_states: int | None,
    deadline_seconds: float | None,
    max_points: int | None,
    explicit_profiles: Sequence[Profile] = (),
    profile_corpus_id: str | None = None,
) -> dict[str, object]:
    explicit_mode = bool(explicit_profiles)
    profiles = (
        tuple(
            profile
            for profile in explicit_profiles
            if profile.N == N and profile.D == D
        )
        if explicit_mode
        else generate_profiles(N, D, window=window, a_values=a_values, f_cap=f_cap)
    )
    if explicit_mode:
        expected_corpus_id = explicit_profile_corpus_id(explicit_profiles)
        if profile_corpus_id is not None and profile_corpus_id != expected_corpus_id:
            raise InternalInvariantError("explicit profile corpus id changed in memory")
        profile_corpus_id = expected_corpus_id
    elif profile_corpus_id not in {None, GENERATED_PROFILE_CORPUS_ID}:
        raise InternalInvariantError("generated H2 row received an alien corpus id")
    else:
        profile_corpus_id = GENERATED_PROFILE_CORPUS_ID
    for profile in profiles:
        failures = _profile_invariant_failures(profile)
        if failures:
            raise InternalInvariantError(
                f"self-inconsistent census profile {profile.id}: {failures}"
            )
    grouped: dict[tuple[int, int], list[Profile]] = defaultdict(list)
    for profile in profiles:
        grouped[(profile.sum_a, profile.T)].append(profile)
    all_records: list[dict[str, object]] = []
    aggregate = SearchStats()
    complete = True
    started = time.monotonic()
    deadline = None if deadline_seconds is None else started + deadline_seconds
    for (target_sum, target_T), rows in sorted(grouped.items()):
        remaining_cap = None
        if max_states is not None:
            remaining_cap = max(0, max_states - aggregate.expanded_states)
        records, stats, group_complete = enumerate_group(
            D,
            N,
            target_sum,
            target_T,
            rows,
            max_states=remaining_cap,
            deadline=deadline,
            max_points=max_points,
        )
        all_records.extend(records)
        for field in (
            "expanded_states",
            "generated_states",
            "symmetry_duplicates",
            "terminal_states",
            "point_cap_prunes",
        ):
            setattr(aggregate, field, getattr(aggregate, field) + getattr(stats, field))
        if stats.resource_stop:
            aggregate.resource_stop = stats.resource_stop
        complete = complete and group_complete
        if not group_complete and stats.resource_stop:
            break
    unique_clusters = {
        json.dumps(
            (record["tuple"]["forest_shape"], record["tuple"]["multiplicities"]),
            sort_keys=True,
            separators=(",", ":"),
        )
        for record in all_records
    }
    for record in all_records:
        record["profile_corpus_id"] = profile_corpus_id
    return {
        "schema": SCHEMA,
        "engine_revision": ENGINE_REVISION,
        "N": N,
        "D": D,
        "window": (
            "explicit-component-degrees" if explicit_mode else window
        ),
        "profile_mode": (
            "explicit-component-degrees" if explicit_mode else "H2-common-n"
        ),
        "profile_corpus_id": profile_corpus_id,
        "a_values": list(a_values),
        "f_cap": f_cap if f_cap is not None else "unbounded",
        "profile_rows": len(profiles),
        "aggregate_groups": len(grouped),
        "complete": complete,
        "count": len(all_records) if complete else None,
        "observed_lower_bound": len(all_records),
        "unique_cluster_count": len(unique_clusters) if complete else None,
        "solutions": all_records,
        "stats": {
            "expanded_states": aggregate.expanded_states,
            "generated_states": aggregate.generated_states,
            "symmetry_duplicates": aggregate.symmetry_duplicates,
            "terminal_states": aggregate.terminal_states,
            "point_cap_prunes": aggregate.point_cap_prunes,
            "resource_stop": aggregate.resource_stop,
            "elapsed_seconds": round(time.monotonic() - started, 6),
        },
        "moh_compatible_actual_map": D >= 101,
        "nef_check": "certified_per_emitted_solution",
        "global_nef_certified": (
            all(bool(record["global_nef_certified"]) for record in all_records)
            if all_records else None
        ),
        "artifact": ARTIFACT,
        "attainment": ATTAINMENT,
        "warning": "A numerical cluster is not a map.",
    }


def validate_homaloidal_control(
    D: int,
    multiplicities: Sequence[int],
    parents: Sequence[Sequence[int]],
) -> dict[str, object]:
    """Separate general-plane Cremona control (no distinguished L_infty)."""

    errors: list[str] = []
    if not isinstance(D, int) or isinstance(D, bool) or D < 1:
        return {
            "ok": False,
            "errors": ["D must be a positive integer"],
            "artifact": ARTIFACT,
            "attainment": ATTAINMENT,
        }
    if len(multiplicities) != len(parents):
        return {
            "ok": False,
            "errors": ["length mismatch"],
            "artifact": ARTIFACT,
            "attainment": ATTAINMENT,
        }
    if any(not isinstance(v, int) or isinstance(v, bool) or v < 1 for v in multiplicities):
        return {
            "ok": False,
            "errors": ["all base multiplicities must be positive integers"],
            "artifact": ARTIFACT,
            "attainment": ATTAINMENT,
        }
    adjacency: list[set[int]] = []
    clean_parents: list[tuple[int, ...]] = []
    for i, pp_raw in enumerate(parents):
        if not isinstance(pp_raw, (list, tuple)):
            errors.append(f"point {i}: parent row must be an array")
            pp = ()
        else:
            pp = tuple(pp_raw)
        malformed = (
            len(pp) > 2
            or any(not isinstance(q, int) or isinstance(q, bool) or q < 0 or q >= i for q in pp)
            or len(set(pp)) != len(pp)
        )
        if malformed:
            errors.append(f"point {i}: malformed proper/infinitely-near center")
            pp = ()
        if len(pp) == 2 and pp[1] not in adjacency[pp[0]]:
            errors.append(f"point {i}: satellite parents were not adjacent")
        adjacency.append(set(pp))
        if len(pp) == 2:
            adjacency[pp[0]].discard(pp[1])
            adjacency[pp[1]].discard(pp[0])
        for q in pp:
            adjacency[q].add(i)
        clean_parents.append(pp)
    excess = list(multiplicities)
    for i, pp in enumerate(clean_parents):
        for q in pp:
            excess[q] -= multiplicities[i]
    if any(v < 0 for v in excess):
        errors.append("proximity inequality failed")
    if sum(multiplicities) != 3 * D - 3:
        errors.append("first Cremona-Noether equation failed")
    if sum(v * v for v in multiplicities) != D * D - 1:
        errors.append("second Cremona-Noether equation failed")
    return {
        "ok": not errors,
        "errors": errors,
        "D": D,
        "multiplicities": list(multiplicities),
        "parents": [list(v) for v in parents],
        "artifact": ARTIFACT,
        "attainment": ATTAINMENT,
    }


# Frozen control corpus from box/nvm-drivers-20260902/final.py, resolved there
# over Q.  This is data, not executable CAS input.  Each row is
# (name, D, ((a_i, parents), ...), N, kappa, Lambda, T, sum_a).
POLAR_FIXTURES = (
    ('(x, xy)', 2, ((1, ('L',)), (1, ('L',)), (1, (1,))), 1, 1, 1, 0, 3),
    ('(x, y^2)', 2, ((1, ('L',)), (1, ('L', 0))), 2, 1, 0, 1, 2),
    ('(x, xy^2)', 3, ((2, ('L',)), (1, ('L',)), (1, (1,)), (1, (2,))), 2, 2, 1, 0, 5),
    ('(x, xy^3)', 4, ((3, ('L',)), (1, ('L',)), (1, (1,)), (1, (2,)), (1, (3,))), 3, 3, 1, 0, 7),
    ('(x, y+x^2)', 2, ((1, ('L',)), (1, ('L', 0)), (1, (1,))), 1, 1, 0, 1, 3),
    ('(x, y+x^3)', 3, ((2, ('L',)), (1, ('L', 0)), (1, (0, 1)), (1, (2,)), (1, (3,))), 1, 1, 0, 2, 6),
    ('(x, y+x^4)', 4, ((3, ('L',)), (1, ('L', 0)), (1, (0, 1)), (1, (0, 2)), (1, (3,)), (1, (4,)), (1, (5,))), 1, 1, 0, 3, 9),
    ('(x, y+x^5)', 5, ((4, ('L',)), (1, ('L', 0)), (1, (0, 1)), (1, (0, 2)), (1, (0, 3)), (1, (4,)), (1, (5,)), (1, (6,)), (1, (7,))), 1, 1, 0, 4, 12),
    ('(x+y^2, y)', 2, ((1, ('L',)), (1, ('L', 0)), (1, (1,))), 1, 1, 0, 1, 3),
    ('(x+y^3, y)', 3, ((2, ('L',)), (1, ('L', 0)), (1, (0, 1)), (1, (2,)), (1, (3,))), 1, 1, 0, 2, 6),
    ('(x, x^2y)', 3, ((1, ('L',)), (2, ('L',)), (1, (0,)), (1, (1,)), (1, (1, 3))), 1, 1, 1, 1, 6),
    ('(x, x^3y)', 4, ((1, ('L',)), (3, ('L',)), (1, (0,)), (1, (1,)), (1, (2,)), (1, (1, 3)), (1, (1, 5))), 1, 1, 1, 2, 9),
    ('(x, x^4y)', 5, ((1, ('L',)), (4, ('L',)), (1, (0,)), (1, (1,)), (1, (2,)), (1, (1, 3)), (1, (4,)), (1, (1, 5)), (1, (1, 7))), 1, 1, 1, 3, 12),
    ('(x, x^2y^2)', 4, ((2, ('L',)), (2, ('L',)), (1, (0,)), (2, (1,)), (1, (0, 2))), 2, 1, 2, 1, 8),
    ('(x, x^3y^2)', 5, ((2, ('L',)), (3, ('L',)), (2, (0,)), (2, (1,)), (1, (1, 3)), (1, (3, 4))), 2, 2, 1, 2, 11),
    ('(x, x^4y^2)', 6, ((2, ('L',)), (4, ('L',)), (2, (0,)), (2, (1,)), (1, (2,)), (2, (1, 3)), (1, (2, 4))), 2, 1, 2, 3, 14),
    ('(x, x^2y^3)', 5, ((3, ('L',)), (2, ('L',)), (1, (0,)), (2, (1,)), (1, (0, 2)), (1, (3,)), (1, (0, 4)), (1, (3, 5))), 3, 1, 1, 3, 12),
    ('(x, x^3y^3)', 6, ((3, ('L',)), (3, ('L',)), (2, (0,)), (3, (1,)), (1, (0, 2)), (1, (2, 4))), 3, 1, 3, 2, 13),
    ('(x, x^4y^3)', 7, ((3, ('L',)), (4, ('L',)), (3, (0,)), (3, (1,)), (1, (1, 3)), (1, (3, 4)), (1, (3, 5))), 3, 3, 1, 3, 16),
    ('(x^2, y)', 2, ((1, ('L',)), (1, ('L', 0))), 2, 1, 0, 1, 2),
    ('(x^2y, y)', 3, ((1, ('L',)), (2, ('L',)), (1, (0,)), (1, (2,))), 2, 2, 1, 0, 5),
    ('(x, xy+y^2)', 2, ((1, ('L',)), (1, ('L',))), 2, 2, 0, 0, 2),
    ('(x^2,y^4)', 4, ((2, ('L',)), (2, ('L', 0))), 8, 2, 0, 2, 4),
    ('(x^3,y^6)', 6, ((3, ('L',)), (3, ('L', 0))), 18, 3, 0, 3, 6),
    ('(x^4,y^8)', 8, ((4, ('L',)), (4, ('L', 0))), 32, 4, 0, 4, 8),
    ('(x^5,y^10)', 10, ((5, ('L',)), (5, ('L', 0))), 50, 5, 0, 5, 10),
    ('(x, xy^2+y)', 3, ((2, ('L',)), (1, ('L',)), (1, (1,)), (1, (2,))), 2, 2, 1, 0, 5),
    ('(xy, xy^2)', 3, ((2, ('L',)), (1, ('L',)), (1, (0,)), (1, (1,)), (1, (3,))), 1, 1, 2, 0, 6),
    ('(x, y^3+xy)', 3, ((2, ('L',)), (1, ('L', 0)), (1, (1,))), 3, 2, 0, 1, 4),
    ('psi_1 o (x,xy)', 2, ((1, ('L',)), (1, ('L',)), (1, (1,))), 1, 1, 1, 0, 3),
    ('psi_2 o (x,xy)', 4, ((2, ('L',)), (2, ('L',)), (1, (0,)), (2, (1,)), (1, (0, 2)), (1, (4,))), 1, 1, 2, 1, 9),
    ('psi_3 o (x,xy)', 6, ((3, ('L',)), (3, ('L',)), (2, (0,)), (3, (1,)), (1, (0, 2)), (1, (2, 4)), (1, (5,)), (1, (6,))), 1, 1, 3, 2, 15),
    ('psi_4 o (x,xy)', 8, ((4, ('L',)), (4, ('L',)), (3, (0,)), (4, (1,)), (1, (0, 2)), (1, (2, 4)), (1, (2, 5)), (1, (6,)), (1, (7,)), (1, (8,))), 1, 1, 4, 3, 21),
    ('psi_5 o (x,xy)', 10, ((5, ('L',)), (5, ('L',)), (4, (0,)), (5, (1,)), (1, (0, 2)), (1, (2, 4)), (1, (2, 5)), (1, (2, 6)), (1, (7,)), (1, (8,)), (1, (9,)), (1, (10,))), 1, 1, 5, 4, 27),
    ('psi_1 o (x,xy^2)', 3, ((2, ('L',)), (1, ('L',)), (1, (1,)), (1, (2,))), 2, 2, 1, 0, 5),
    ('psi_2 o (x,xy^2)', 6, ((4, ('L',)), (2, ('L',)), (1, (0,)), (2, (1,)), (1, (0, 2)), (2, (3,)), (1, (0, 4)), (1, (0, 6)), (1, (7,)), (1, (8,))), 2, 1, 2, 3, 16),
    ('psi_3 o (x,xy^2)', 9, ((6, ('L',)), (3, ('L',)), (2, (0,)), (3, (1,)), (2, (0, 2)), (3, (3,)), (2, (0, 4)), (1, (6,)), (1, (6,)), (1, (7,)), (1, (8,))), 2, 2, 3, 4, 25),
    ('psi_4 o (x,xy^2)', 12, ((8, ('L',)), (4, ('L',)), (3, (0,)), (4, (1,)), (3, (0, 2)), (4, (3,)), (2, (0, 4)), (1, (4, 6)), (1, (6, 7)), (1, (8,)), (1, (9,)), (1, (10,)), (1, (11,)), (1, (12,)), (1, (13,))), 2, 1, 4, 7, 36),
    ('psi_2 o (x,x^2y)', 6, ((2, ('L',)), (4, ('L',)), (2, (0,)), (2, (1,)), (1, (2,)), (2, (1, 3)), (1, (2, 4)), (1, (6,))), 1, 1, 2, 3, 15),
    ('psi_3 o (x,x^2y)', 9, ((3, ('L',)), (6, ('L',)), (3, (0,)), (3, (1,)), (2, (2,)), (3, (1, 3)), (1, (2, 4)), (1, (4, 6)), (1, (7,)), (1, (8,))), 1, 1, 3, 5, 24),
    ('psi_cusp o (x,xy)', 6, ((3, ('L',)), (3, ('L',)), (2, (0,)), (3, (1,)), (1, (0, 2)), (1, (2, 4))), 3, 1, 3, 2, 13),
)


KELLER_AUTOMORPHISM_NAMES = {
    '(x, y+x^2)', '(x, y+x^3)', '(x, y+x^4)', '(x, y+x^5)',
    '(x+y^2, y)', '(x+y^3, y)',
}


# (N,c,D,kappa,Lambda,T,sum_a,sum_a2) for the 35 saved NEG-GEN controls
# (x,x^c y^N), N=2..8 and c=1..5.  The general-dominant control declares
# n=1, W=N, S=Lambda; unlike Keller/H2 data it may contain length-one cycles.
NEG_GEN_METRICS = (
    (2,1,3,2,1,0,5,7),(2,2,4,1,2,1,8,14),(2,3,5,2,1,2,11,23),(2,4,6,1,2,3,14,34),(2,5,7,2,1,4,17,47),
    (3,1,4,3,1,0,7,13),(3,2,5,1,1,3,12,22),(3,3,6,1,3,2,13,33),(3,4,7,3,1,3,16,46),(3,5,8,1,1,6,21,61),
    (4,1,5,4,1,0,9,21),(4,2,6,1,2,3,14,32),(4,3,7,2,1,4,17,45),(4,4,8,1,4,3,18,60),(4,5,9,4,1,4,21,77),
    (5,1,6,5,1,0,11,31),(5,2,7,1,1,5,18,44),(5,3,8,1,1,6,21,59),(5,4,9,1,1,7,24,76),(5,5,10,1,5,4,23,95),
    (6,1,7,6,1,0,13,43),(6,2,8,1,2,5,20,58),(6,3,9,2,3,4,21,75),(6,4,10,3,2,5,24,94),(6,5,11,2,1,8,29,115),
    (7,1,8,7,1,0,15,57),(7,2,9,1,1,7,24,74),(7,3,10,1,1,8,27,93),(7,4,11,1,1,9,30,114),(7,5,12,1,1,10,33,137),
    (8,1,9,8,1,0,17,73),(8,2,10,1,2,7,26,92),(8,3,11,2,1,8,29,113),(8,4,12,1,4,7,30,136),(8,5,13,4,1,8,33,161),
)


def _fixture_cluster(row: tuple[object, ...]) -> dict[str, object]:
    _, D, points, N, *_ = row
    multiplicities = [point[0] for point in points]
    parents = [point[1] for point in points]
    return validate_cluster(D, multiplicities, parents, expected_N=N)


def _legacy_profile_completions(cluster: dict[str, object]) -> list[tuple[int, int, int, int]]:
    """Exact weak completion loop used by the saved ceiling-lane ram.py."""

    N = int(cluster['N'])
    Lambda = int(cluster['Lambda'])
    found: list[tuple[int, int, int, int]] = []
    for n in range(1, Lambda + 1):
        if Lambda % n:
            continue
        S = Lambda // n
        for fixed in range(ceil_div(N, 2), N - 1):
            W = N - fixed
            if W < 2 * S:
                continue
            rhs = 3 * int(cluster['D']) - 2 * N - int(cluster['kappa']) + n * (W - S)
            if int(cluster['sum_a']) == rhs:
                found.append((n, S, W, fixed))
    return found


def run_self_tests() -> dict[str, object]:
    failures: list[str] = []
    fixture_passes = 0
    dn_passes = 0
    legacy_completions = 0
    automorphism_passes = 0
    unique_clusters: set[str] = set()
    for row in POLAR_FIXTURES:
        name, D, points, N, kappa, Lambda, T, sum_a = row
        cluster = _fixture_cluster(row)
        expected = (
            cluster.get('ok')
            and cluster.get('kappa') == kappa
            and cluster.get('Lambda') == Lambda
            and cluster.get('T') == T
            and cluster.get('sum_a') == sum_a
        )
        if expected:
            fixture_passes += 1
        else:
            failures.append(f"polar fixture failed: {name}: {cluster.get('errors')}")
        dn_ok = all(
            len(dic['positive_m_neighbours']) == 1
            and cluster['m'][0 if dic['positive_m_neighbours'][0] == 'L' else int(dic['positive_m_neighbours'][0]) + 1]
            == dic['degree']
            for dic in cluster.get('dicritical_components', [])
        )
        if dn_ok:
            dn_passes += 1
        else:
            failures.append(f"DN fixture failed: {name}")
        legacy_completions += len(_legacy_profile_completions(cluster))
        if name in KELLER_AUTOMORPHISM_NAMES:
            if (
                N == 1
                and cluster['Lambda'] == 0
                and cluster['kappa'] == 1
                and cluster['sum_a'] == 3 * D - 3
                and cluster['sum_a2'] == D * D - 1
            ):
                automorphism_passes += 1
            else:
                failures.append(f"automorphism Noether control failed: {name}")
        unique_clusters.add(json.dumps((D, points), sort_keys=True))

    quadratic = validate_homaloidal_control(2, (1, 1, 1), ((), (), ()))
    if not quadratic['ok']:
        failures.append("quadratic Cremona control failed")

    neg_row = next(row for row in POLAR_FIXTURES if row[0] == '(x, x^3y^2)')
    neg = _fixture_cluster(neg_row)
    neg_profile = Profile(
        N=2, D=5, fixed_sheets=0, W=2,
        dicriticals=(DicriticalDatum(1, 2),), S=1, n=1,
        kappa=2, T=2, sum_a=10, n_floor=2, n_upper=1,
        window='NEG-GEN-control', f_cap=None,
    )
    neg_keller, _, _ = match_profile(
        neg, neg_profile, affine_ramification=0, enforce_meridian_floor=False
    )
    neg_general, _, _ = match_profile(
        neg, neg_profile, affine_ramification=1, enforce_meridian_floor=False
    )
    if neg_keller or not neg_general:
        failures.append("NEG-GEN affine-ramification control failed")
    neg_family_passes = 0
    for N, c_power, D, kappa, Lambda, T, sum_a, sum_a2 in NEG_GEN_METRICS:
        keller_rhs = 3 * D - 2 * N - kappa + (N - Lambda)
        residual = sum_a - keller_rhs
        if (
            D == N + c_power
            and sum_a2 == D * D - N
            and D == Lambda + kappa + T
            and residual == N - 1
            and residual > 0
        ):
            neg_family_passes += 1
        else:
            failures.append(f"NEG-GEN metric failed at N={N}, c={c_power}")

    malformed = validate_cluster(2, (1, 1), (('L',), ('L', 0)), expected_N=2)
    # This shape is valid; the negative canary uses non-adjacent satellite parents.
    malformed2 = validate_cluster(
        3, (1, 1, 1), (('L',), ('L',), (0, 1)), expected_N=6
    )
    if not malformed['ok'] or malformed2['ok']:
        failures.append("forest chronology positive/negative controls failed")

    strict_cells = sum(
        len(generate_profiles(N, D, window='strict'))
        for N in range(2, 5)
        for D in range(1, 41)
    )
    if strict_cells != 0:
        failures.append("strict N<=4 window is not empty")
    if fixture_passes != 41 or dn_passes != 41:
        failures.append("41-map control count mismatch")
    if legacy_completions != 0:
        failures.append("legacy 41-map completion count must be zero")
    if automorphism_passes != 6:
        failures.append("six Keller automorphism controls were not reproduced")
    if neg_family_passes != 35:
        failures.append("35-member NEG-GEN control count mismatch")
    if len(unique_clusters) != 34:
        failures.append(f"expected 34 distinct fixture clusters, got {len(unique_clusters)}")

    # Positive end-to-end census regression: this exercises profile generation,
    # DFS, exact isomorphism deduplication, terminal matching, nef output, and
    # summary/count semantics (the N<=4 desk range is profile-vacuous).
    e2e = census_row(
        5, 10,
        window='strict', a_values=(), f_cap=None,
        max_states=None, deadline_seconds=None, max_points=None,
    )
    expected_mults = [5, 5, 5, 4, 1, 1, 1, 1]
    expected_shape = [['L'], [0], ['L'], [2], [2, 3], [3, 4], [3, 5], [6]]
    e2e_ok = (
        e2e['complete'] is True
        and e2e['count'] == 1
        and e2e['unique_cluster_count'] == 1
        and e2e['solutions'][0]['tuple']['multiplicities'] == expected_mults
        and e2e['solutions'][0]['tuple']['forest_shape'] == expected_shape
        and e2e['solutions'][0]['global_nef_certified'] is True
    )
    if not e2e_ok:
        failures.append('positive N=5,D=10 end-to-end census regression failed')
    capped = census_row(
        5, 10,
        window='strict', a_values=(), f_cap=None,
        max_states=1, deadline_seconds=None, max_points=None,
    )
    cap_ok = (
        capped['complete'] is False
        and capped['count'] is None
        and capped['stats']['resource_stop'] == 'max_states'
    )
    if not cap_ok:
        failures.append('resource-incomplete census semantics failed')

    explicit_profile = Profile(
        N=5, D=10, fixed_sheets=3, W=2,
        dicriticals=(DicriticalDatum(1, 2),), S=1, n=0,
        kappa=2, T=3, sum_a=23, n_floor=0, n_upper=0,
        window='explicit-component-degrees', f_cap=None,
        mode='explicit-component-degrees', component_degrees=(5,),
    )
    e2e_tuple = e2e['solutions'][0]['tuple'] if e2e_ok else {
        'multiplicities': expected_mults, 'forest_shape': expected_shape,
    }
    explicit_cluster = validate_cluster(
        10, e2e_tuple['multiplicities'], e2e_tuple['forest_shape'], expected_N=5
    )
    explicit_ok, _, _ = match_profile(explicit_cluster, explicit_profile)
    if not explicit_ok:
        failures.append('explicit component-degree terminal match failed')
    explicit_profile_2 = Profile(
        N=5, D=11, fixed_sheets=3, W=2,
        dicriticals=(DicriticalDatum(1, 2),), S=1, n=0,
        kappa=2, T=4, sum_a=26, n_floor=0, n_upper=0,
        window='explicit-component-degrees', f_cap=None,
        mode='explicit-component-degrees', component_degrees=(5,),
    )
    explicit_digest = explicit_profile_corpus_id(
        (explicit_profile, explicit_profile_2)
    )
    explicit_digest_ok = (
        explicit_digest.startswith('sha256:')
        and explicit_digest == explicit_profile_corpus_id(
            (explicit_profile_2, explicit_profile)
        )
        and explicit_digest != explicit_profile_corpus_id((explicit_profile,))
    )
    if not explicit_digest_ok:
        failures.append('semantic explicit-corpus digest control failed')
    try:
        fixed_sheet_values(5, 'strict', (3,))
        ignored_a_values_rejected = False
    except InputError:
        ignored_a_values_rejected = True
    if not ignored_a_values_rejected:
        failures.append('ignored a-values option was not rejected')
    try:
        fixed_sheet_values(5, 'explicit', (999,))
        out_of_range_a_values_rejected = False
    except InputError:
        out_of_range_a_values_rejected = True
    try:
        _resolve_range(
            argparse.Namespace(
                Ns=None,
                n_min=2,
                n_max=10**20,
                Ds=[2],
                d_min=2,
                d_max=2,
                allow_any_N=False,
            )
        )
        huge_range_rejected_before_expansion = False
    except InputError:
        huge_range_rejected_before_expansion = True
    if not out_of_range_a_values_rejected or not huge_range_rejected_before_expansion:
        failures.append('range preflight controls failed')

    local_summary = _summary([e2e], (5,), (10,))
    try:
        _validate_merged_cell(
            e2e, local_summary,
            N=5, D=10, expected_window='strict', expected_f_cap=None,
            expected_profile_mode='H2-common-n', expected_a_values=(),
            expected_profile_corpus_id=GENERATED_PROFILE_CORPUS_ID,
            expected_profiles=generate_profiles(5, 10, window='strict'),
        )
        merge_contract_ok = True
    except InputError:
        merge_contract_ok = False
    try:
        _validate_merged_cell(
            capped, _summary([capped], (5,), (10,)),
            N=5, D=10, expected_window='strict', expected_f_cap=None,
            expected_profile_mode='H2-common-n', expected_a_values=(),
            expected_profile_corpus_id=GENERATED_PROFILE_CORPUS_ID,
            expected_profiles=generate_profiles(5, 10, window='strict'),
        )
        incomplete_merge_contract_ok = True
    except InputError:
        incomplete_merge_contract_ok = False
    poisoned = dict(e2e)
    poisoned['complete'] = 'true'
    try:
        _validate_merged_cell(
            poisoned, local_summary,
            N=5, D=10, expected_window='strict', expected_f_cap=None,
            expected_profile_mode='H2-common-n', expected_a_values=(),
            expected_profile_corpus_id=GENERATED_PROFILE_CORPUS_ID,
            expected_profiles=generate_profiles(5, 10, window='strict'),
        )
        merge_poison_rejected = False
    except InputError:
        merge_poison_rejected = True
    resource_poison = dict(e2e)
    resource_poison['stats'] = dict(e2e['stats'])
    resource_poison['stats']['resource_stop'] = 'max_states'
    try:
        _validate_merged_cell(
            resource_poison, local_summary,
            N=5, D=10, expected_window='strict', expected_f_cap=None,
            expected_profile_mode='H2-common-n', expected_a_values=(),
            expected_profile_corpus_id=GENERATED_PROFILE_CORPUS_ID,
            expected_profiles=generate_profiles(5, 10, window='strict'),
        )
        merge_resource_poison_rejected = False
    except InputError:
        merge_resource_poison_rejected = True
    resource_type_poison = dict(e2e)
    resource_type_poison['stats'] = dict(e2e['stats'])
    resource_type_poison['stats']['resource_stop'] = []
    try:
        _validate_merged_cell(
            resource_type_poison, local_summary,
            N=5, D=10, expected_window='strict', expected_f_cap=None,
            expected_profile_mode='H2-common-n', expected_a_values=(),
            expected_profile_corpus_id=GENERATED_PROFILE_CORPUS_ID,
            expected_profiles=generate_profiles(5, 10, window='strict'),
        )
        merge_resource_type_poison_rejected = False
    except InputError:
        merge_resource_type_poison_rejected = True
    nested_bool_poison = strict_json_loads(_canonical_json(e2e))
    if not isinstance(nested_bool_poison, dict):
        raise InternalInvariantError('self-test JSON round trip changed object type')
    nested_bool_poison['solutions'][0]['tuple']['S'] = True
    try:
        _validate_merged_cell(
            nested_bool_poison, local_summary,
            N=5, D=10, expected_window='strict', expected_f_cap=None,
            expected_profile_mode='H2-common-n', expected_a_values=(),
            expected_profile_corpus_id=GENERATED_PROFILE_CORPUS_ID,
            expected_profiles=generate_profiles(5, 10, window='strict'),
        )
        merge_nested_bool_poison_rejected = False
    except InputError:
        merge_nested_bool_poison_rejected = True
    zero_stats_poison = strict_json_loads(_canonical_json(e2e))
    if not isinstance(zero_stats_poison, dict):
        raise InternalInvariantError('self-test JSON round trip changed object type')
    for key in (
        'expanded_states', 'generated_states', 'symmetry_duplicates',
        'terminal_states', 'point_cap_prunes',
    ):
        zero_stats_poison['stats'][key] = 0
    try:
        _validate_merged_cell(
            zero_stats_poison, local_summary,
            N=5, D=10, expected_window='strict', expected_f_cap=None,
            expected_profile_mode='H2-common-n', expected_a_values=(),
            expected_profile_corpus_id=GENERATED_PROFILE_CORPUS_ID,
            expected_profiles=generate_profiles(5, 10, window='strict'),
        )
        merge_zero_stats_poison_rejected = False
    except InputError:
        merge_zero_stats_poison_rejected = True
    alternate_shape = [
        ['L'], ['L'], [1], [0], [0, 3], [3, 4], [3, 5], [6]
    ]
    alternate_cluster = validate_cluster(
        10, expected_mults, alternate_shape, expected_N=5
    )
    e2e_profile = next(
        profile
        for profile in generate_profiles(5, 10, window='strict')
        if profile.id == e2e['solutions'][0]['profile']['id']
    )
    alternate_match, _, alternate_assignment = match_profile(
        alternate_cluster, e2e_profile
    )
    alternate_solution = {
        'profile': e2e_profile.as_dict(),
        'tuple': {
            'D': 10,
            'n': e2e_profile.n,
            'component_degrees': None,
            'S': e2e_profile.S,
            'kappa': e2e_profile.kappa,
            'T': e2e_profile.T,
            'W': e2e_profile.W,
            'a': e2e_profile.fixed_sheets,
            'forest_shape': alternate_cluster['forest_shape'],
            'multiplicities': alternate_cluster['multiplicities'],
        },
        'sheets': alternate_cluster['sheets'],
        'dicriticals': alternate_assignment,
        'boundary_nef': True,
        'global_nef_certified': True,
        'artifact': ARTIFACT,
        'attainment': ATTAINMENT,
        'profile_corpus_id': GENERATED_PROFILE_CORPUS_ID,
    }
    isomorphic_poison = dict(e2e)
    isomorphic_poison['solutions'] = [*e2e['solutions'], alternate_solution]
    isomorphic_poison['observed_lower_bound'] = 2
    isomorphic_poison['count'] = 2
    isomorphic_poison['unique_cluster_count'] = 2
    try:
        _validate_merged_cell(
            isomorphic_poison,
            _summary([isomorphic_poison], (5,), (10,)),
            N=5, D=10, expected_window='strict', expected_f_cap=None,
            expected_profile_mode='H2-common-n', expected_a_values=(),
            expected_profile_corpus_id=GENERATED_PROFILE_CORPUS_ID,
            expected_profiles=generate_profiles(5, 10, window='strict'),
        )
        merge_isomorphic_poison_rejected = False
    except InputError:
        merge_isomorphic_poison_rejected = True
    if (
        not merge_contract_ok
        or not incomplete_merge_contract_ok
        or not merge_poison_rejected
        or not merge_resource_poison_rejected
        or not merge_resource_type_poison_rejected
        or not merge_nested_bool_poison_rejected
        or not merge_zero_stats_poison_rejected
        or not alternate_match
        or not merge_isomorphic_poison_rejected
    ):
        failures.append('strict merge contract positive/negative control failed')
    return {
        'schema': SCHEMA,
        'engine_revision': ENGINE_REVISION,
        'ok': not failures,
        'failures': failures,
        'checks': {
            'polar_fixtures_passed': fixture_passes,
            'dicritical_neighbour_fixtures_passed': dn_passes,
            'legacy_noninvertible_completions': legacy_completions,
            'keller_automorphism_noether_passed': automorphism_passes,
            'distinct_numerical_fixture_clusters': len(unique_clusters),
            'quadratic_cremona': quadratic['ok'],
            'neg_gen_keller_rejected': not neg_keller,
            'neg_gen_general_plus_affine_accepted': neg_general,
            'neg_gen_family_residual_N_minus_1_passed': neg_family_passes,
            'strict_N2_to_N4_D40_profile_rows': strict_cells,
            'positive_N5_D10_end_to_end_count': e2e['count'] if e2e_ok else None,
            'resource_cap_marks_incomplete': cap_ok,
            'explicit_component_degree_match': explicit_ok,
            'explicit_corpus_digest': explicit_digest_ok,
            'ignored_a_values_rejected': ignored_a_values_rejected,
            'range_preflight_rejections': (
                out_of_range_a_values_rejected
                and huge_range_rejected_before_expansion
            ),
            'strict_merge_contract': (
                merge_contract_ok
                and incomplete_merge_contract_ok
                and merge_poison_rejected
                and merge_resource_poison_rejected
                and merge_resource_type_poison_rejected
                and merge_nested_bool_poison_rejected
                and merge_zero_stats_poison_rejected
                and alternate_match
                and merge_isomorphic_poison_rejected
            ),
        },
        'artifact': ARTIFACT,
        'attainment': ATTAINMENT,
    }


def _parse_f_cap(text: str) -> int | None:
    if text.lower() == "unbounded":
        return None
    try:
        return int(text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("f cap must be an integer or 'unbounded'") from exc


def _parse_a_values(text: str) -> tuple[int, ...]:
    if not text.strip():
        return ()
    try:
        return tuple(int(value) for value in text.split(','))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("a values must be comma-separated integers") from exc


def _add_profile_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '--window',
        choices=('strict', 'legacy-inclusive', 'all-h2', 'explicit'),
        default='strict',
        help=(
            "fixed-sheet window: strict is the charged 2a>N window; "
            "legacy-inclusive reproduces the old lane; all-h2 and explicit "
            "are declared other-window modes"
        ),
    )
    parser.add_argument('--a-values', type=_parse_a_values, default=())
    parser.add_argument(
        '--f-cap',
        type=_parse_f_cap,
        default=None,
        metavar='INTEGER|unbounded',
        help='declared coarse anticanonical cap; default is unbounded',
    )
    parser.add_argument(
        '--explicit-component-profiles',
        type=Path,
        help=(
            'JSON/JSONL profiles with per-dicritical n_c; activates the '
            'reducible/other-component-degree mode'
        ),
    )


def _add_range_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument('--N', dest='Ns', action='append', type=int)
    parser.add_argument('--n-min', type=int, default=2)
    parser.add_argument('--n-max', type=int, default=8)
    parser.add_argument('--D', dest='Ds', action='append', type=int)
    parser.add_argument('--d-min', type=int, default=2)
    parser.add_argument('--d-max', type=int, default=40)
    parser.add_argument(
        '--allow-any-N',
        action='store_true',
        help='permit N outside the campaign default 2..8',
    )


def _resolve_range(args: argparse.Namespace) -> tuple[tuple[int, ...], tuple[int, ...]]:
    if args.Ns:
        Ns = tuple(sorted(set(args.Ns)))
    else:
        if args.n_min > args.n_max:
            raise InputError('N range is empty')
        if args.n_min < 2:
            raise InputError('census N must be >=2; N=1 is a separate control mode')
        if not args.allow_any_N and args.n_max > 8:
            raise InputError('N outside 2..8 requires --allow-any-N')
        n_count = args.n_max - args.n_min + 1
        if n_count > MAX_AXIS_VALUES:
            raise InputError(
                f'N range has {n_count} values; maximum is {MAX_AXIS_VALUES}'
            )
        Ns = tuple(range(args.n_min, args.n_max + 1))
    if args.Ds:
        Ds = tuple(sorted(set(args.Ds)))
    else:
        if args.d_min > args.d_max:
            raise InputError('D range is empty')
        if args.d_min < 1:
            raise InputError('D must be positive')
        d_count = args.d_max - args.d_min + 1
        if d_count > MAX_AXIS_VALUES:
            raise InputError(
                f'D range has {d_count} values; maximum is {MAX_AXIS_VALUES}'
            )
        Ds = tuple(range(args.d_min, args.d_max + 1))
    if not Ns or not Ds:
        raise InputError('N and D ranges must be nonempty')
    if any(N < 2 for N in Ns):
        raise InputError('census N must be >=2; N=1 is a separate control mode')
    if not args.allow_any_N and any(N < 2 or N > 8 for N in Ns):
        raise InputError('N outside 2..8 requires --allow-any-N')
    if any(D < 1 for D in Ds):
        raise InputError('D must be positive')
    if len(Ns) * len(Ds) > MAX_ND_CELLS:
        raise InputError(
            f'N-D selection exceeds the {MAX_ND_CELLS}-cell safety limit'
        )
    return Ns, Ds


def _load_optional_profiles(args: argparse.Namespace) -> tuple[Profile, ...]:
    if args.explicit_component_profiles is None:
        if args.window != 'explicit' and args.a_values:
            raise InputError('--a-values is only valid with --window explicit')
        if args.window == 'explicit' and not args.a_values:
            raise InputError('--window explicit requires --a-values')
        return ()
    if args.window != 'strict' or args.a_values or args.f_cap is not None:
        raise InputError(
            '--explicit-component-profiles cannot be combined with generated H2 window options'
        )
    return load_explicit_component_profiles(args.explicit_component_profiles)


def plan_rows(args: argparse.Namespace) -> dict[str, object]:
    Ns, Ds = _resolve_range(args)
    explicit = _load_optional_profiles(args)
    corpus_id = (
        explicit_profile_corpus_id(explicit)
        if explicit
        else GENERATED_PROFILE_CORPUS_ID
    )
    raw = kept = active = raw_active = 0
    per_N: dict[str, dict[str, int]] = {}
    for N in Ns:
        n_raw = n_kept = n_active = n_raw_active = 0
        for D in Ds:
            if explicit:
                rows = tuple(p for p in explicit if p.N == N and p.D == D)
                raw_rows = rows
            else:
                raw_rows = generate_profiles(
                    N, D, window=args.window, a_values=args.a_values,
                    f_cap=args.f_cap, arithmetic_prefilter=False,
                )
                rows = generate_profiles(
                    N, D, window=args.window, a_values=args.a_values,
                    f_cap=args.f_cap, arithmetic_prefilter=True,
                )
            n_raw += len(raw_rows)
            n_kept += len(rows)
            n_active += int(bool(rows))
            n_raw_active += int(bool(raw_rows))
        raw += n_raw
        kept += n_kept
        active += n_active
        raw_active += n_raw_active
        per_N[str(N)] = {
            'raw_scalar_profile_rows': n_raw,
            'parity_feasible_profile_rows': n_kept,
            'active_ND_cells': n_active,
            'raw_active_ND_cells': n_raw_active,
        }
    return {
        'schema': SCHEMA,
        'engine_revision': ENGINE_REVISION,
        'mode': 'plan',
        'N_values': list(Ns),
        'D_values': [min(Ds), max(Ds)] if Ds == tuple(range(min(Ds), max(Ds) + 1)) else list(Ds),
        'ND_cells': len(Ns) * len(Ds),
        'active_ND_cells': active,
        'raw_active_ND_cells': raw_active,
        'raw_scalar_profile_rows': raw,
        'parity_feasible_profile_rows': kept,
        'per_N': per_N,
        'window': 'explicit-component-degrees' if explicit else args.window,
        'profile_mode': (
            'explicit-component-degrees' if explicit else 'H2-common-n'
        ),
        'profile_corpus_id': corpus_id,
        'a_values': list(args.a_values),
        'f_cap': args.f_cap if args.f_cap is not None else 'unbounded',
        'artifact': ARTIFACT,
        'attainment': ATTAINMENT,
    }


def _summary(rows: Sequence[dict[str, object]], Ns: Sequence[int], Ds: Sequence[int]) -> dict[str, object]:
    smallest: dict[str, object] = {}
    for N in Ns:
        by_D = {row['D']: row for row in rows if row['N'] == N}
        answer: object = None
        for D in sorted(Ds):
            row = by_D.get(D)
            if row is None:
                answer = 'OPEN_INCOMPLETE'
                break
            if row['complete'] is not True:
                answer = 'OPEN_INCOMPLETE'
                break
            if row['count'] > 0:
                answer = D
                break
        smallest[str(N)] = 'NONE_IN_SCANNED_RANGE' if answer is None else answer
    ordered_Ds = tuple(sorted(Ds))
    contiguous = ordered_Ds == tuple(range(min(ordered_Ds), max(ordered_Ds) + 1))
    return {
        'schema': SCHEMA,
        'engine_revision': ENGINE_REVISION,
        'row_type': 'summary',
        'smallest_D_in_scanned_range_by_N': smallest,
        'scanned_D_domain': (
            {'min': min(ordered_Ds), 'max': max(ordered_Ds), 'contiguous': True}
            if contiguous
            else {'values': list(ordered_Ds), 'contiguous': False}
        ),
        'all_rows_complete': (
            len(rows) == len(Ns) * len(Ds)
            and all(row['complete'] is True for row in rows)
        ),
        'artifact': ARTIFACT,
        'attainment': ATTAINMENT,
        'warning': 'A numerical cluster is not a map.',
    }


def _atomic_write(path: Path, text: str, *, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise InputError(f'output already exists (use --overwrite explicitly): {path}')
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        mode='w',
        encoding='utf-8',
        dir=path.parent,
        prefix=f'.{path.name}.tmp-',
        delete=False,
    )
    temporary = Path(handle.name)
    try:
        with handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        if overwrite:
            os.replace(temporary, path)
        else:
            try:
                os.link(temporary, path)
            except FileExistsError as exc:
                raise InputError(
                    f'output already exists (use --overwrite explicitly): {path}'
                ) from exc
    finally:
        if temporary.exists():
            temporary.unlink()


def run_census_command(args: argparse.Namespace) -> tuple[list[dict[str, object]], dict[str, object]]:
    Ns, Ds = _resolve_range(args)
    explicit = _load_optional_profiles(args)
    corpus_id = (
        explicit_profile_corpus_id(explicit)
        if explicit
        else GENERATED_PROFILE_CORPUS_ID
    )
    max_states = None if args.max_states == 0 else args.max_states
    deadline = None if args.deadline_seconds == 0 else args.deadline_seconds
    if max_states is not None and max_states < 1:
        raise InputError('--max-states must be 0 (unbounded) or positive')
    if deadline is not None and (not isfinite(deadline) or deadline <= 0):
        raise InputError('--deadline-seconds must be finite positive, or 0 (unbounded)')
    if args.max_points is not None and args.max_points < 1:
        raise InputError('--max-points must be positive')
    rows: list[dict[str, object]] = []
    for N in Ns:
        for D in Ds:
            rows.append(
                census_row(
                    N, D,
                    window=args.window,
                    a_values=args.a_values,
                    f_cap=args.f_cap,
                    max_states=max_states,
                    deadline_seconds=deadline,
                    max_points=args.max_points,
                    explicit_profiles=explicit,
                    profile_corpus_id=corpus_id,
                )
            )
    return rows, _summary(rows, Ns, Ds)


def _exact_nonnegative_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _validate_merged_cell(
    row: object,
    local_summary: object,
    *,
    N: int,
    D: int,
    expected_window: str,
    expected_f_cap: int | None,
    expected_profile_mode: str,
    expected_a_values: Sequence[int],
    expected_profile_corpus_id: str,
    expected_profiles: Sequence[Profile],
) -> dict[str, object]:
    if not isinstance(row, dict) or not isinstance(local_summary, dict):
        raise InputError('cell shard documents must be JSON objects')
    expected_row_keys = {
        'schema', 'engine_revision', 'N', 'D', 'window', 'profile_mode',
        'profile_corpus_id', 'a_values', 'f_cap', 'profile_rows',
        'aggregate_groups', 'complete', 'count', 'observed_lower_bound',
        'unique_cluster_count', 'solutions', 'stats',
        'moh_compatible_actual_map', 'nef_check', 'global_nef_certified',
        'artifact', 'attainment', 'warning',
    }
    if set(row) != expected_row_keys:
        raise InputError(
            'cell keys mismatch; '
            f'missing={sorted(expected_row_keys - set(row))}, '
            f'unknown={sorted(set(row) - expected_row_keys)}'
        )
    expected_f: object = expected_f_cap if expected_f_cap is not None else 'unbounded'
    identity = {
        'schema': SCHEMA,
        'engine_revision': ENGINE_REVISION,
        'N': N,
        'D': D,
        'window': expected_window,
        'profile_mode': expected_profile_mode,
        'profile_corpus_id': expected_profile_corpus_id,
        'a_values': list(expected_a_values),
        'f_cap': expected_f,
        'artifact': ARTIFACT,
        'attainment': ATTAINMENT,
        'moh_compatible_actual_map': D >= 101,
        'nef_check': 'certified_per_emitted_solution',
        'warning': 'A numerical cluster is not a map.',
    }
    for key, value in identity.items():
        if not _json_exact_equal(row.get(key), value):
            raise InputError(f'cell identity/config mismatch at {key}')
    for key in (
        'profile_rows', 'aggregate_groups', 'observed_lower_bound'
    ):
        if not _exact_nonnegative_integer(row.get(key)):
            raise InputError(f'cell {key} must be an exact nonnegative integer')
    profile_by_id = {profile.id: profile for profile in expected_profiles}
    if len(profile_by_id) != len(expected_profiles):
        raise InternalInvariantError('expected profile sequence has duplicate ids')
    if row['profile_rows'] != len(expected_profiles):
        raise InputError('cell profile-row count differs from the expected corpus')
    expected_groups = len({(profile.sum_a, profile.T) for profile in expected_profiles})
    if row['aggregate_groups'] != expected_groups:
        raise InputError('cell aggregate-group count differs from expected profiles')
    if not isinstance(row.get('complete'), bool):
        raise InputError('cell complete must be boolean')
    solutions = row.get('solutions')
    if not isinstance(solutions, list):
        raise InputError('cell solutions must be an array')
    if row['observed_lower_bound'] != len(solutions):
        raise InputError('observed lower bound does not equal serialized solutions')
    serialized_solutions: set[str] = set()
    profile_state_buckets: dict[
        str, dict[tuple[object, ...], list[State]]
    ] = defaultdict(lambda: defaultdict(list))
    unique_state_buckets: dict[tuple[object, ...], list[State]] = defaultdict(list)
    unique_cluster_count = 0
    for index, solution in enumerate(solutions):
        if not isinstance(solution, dict) or not isinstance(solution.get('tuple'), dict):
            raise InputError(f'malformed solution {index}')
        tuple_row = solution['tuple']
        expected_tuple_keys = {
            'D', 'n', 'component_degrees', 'S', 'kappa', 'T', 'W', 'a',
            'forest_shape', 'multiplicities',
        }
        if set(tuple_row) != expected_tuple_keys:
            raise InputError(f'solution {index} tuple keys mismatch')
        if not isinstance(tuple_row['multiplicities'], list) or not isinstance(
            tuple_row['forest_shape'], list
        ):
            raise InputError(f'solution {index} cluster arrays are malformed')
        profile_row = solution.get('profile')
        if not isinstance(profile_row, dict) or not isinstance(profile_row.get('id'), str):
            raise InputError(f'solution {index} profile is malformed')
        profile = profile_by_id.get(profile_row['id'])
        if profile is None or not _json_exact_equal(profile_row, profile.as_dict()):
            raise InputError(f'solution {index} profile is outside the expected corpus')
        cluster = validate_cluster(
            D,
            tuple_row['multiplicities'],
            tuple_row['forest_shape'],
            expected_N=N,
        )
        if cluster.get('ok') is not True:
            raise InputError(f'solution {index} cluster replay failed')
        state = _state_from_public_cluster(
            D, tuple_row['multiplicities'], tuple_row['forest_shape']
        )
        bucket = _isomorphism_bucket(state)
        same_profile_states = profile_state_buckets[profile.id][bucket]
        if any(isomorphic(state, old) for old in same_profile_states):
            raise InputError(
                f'solution {index} duplicates an isomorphic cluster for its profile'
            )
        same_profile_states.append(state)
        global_states = unique_state_buckets[bucket]
        if not any(isomorphic(state, old) for old in global_states):
            global_states.append(state)
            unique_cluster_count += 1
        matched, _, assignment = match_profile(cluster, profile)
        if not matched:
            raise InputError(f'solution {index} no longer matches its profile')
        expected_solution = {
            'profile': profile.as_dict(),
            'tuple': {
                'D': D,
                'n': profile.n if profile.mode == 'H2-common-n' else None,
                'component_degrees': (
                    list(profile.component_degrees)
                    if profile.component_degrees else None
                ),
                'S': profile.S,
                'kappa': profile.kappa,
                'T': profile.T,
                'W': profile.W,
                'a': profile.fixed_sheets,
                'forest_shape': cluster['forest_shape'],
                'multiplicities': cluster['multiplicities'],
            },
            'sheets': cluster['sheets'],
            'dicriticals': assignment,
            'boundary_nef': True,
            'global_nef_certified': True,
            'artifact': ARTIFACT,
            'attainment': ATTAINMENT,
            'profile_corpus_id': expected_profile_corpus_id,
        }
        if not _json_exact_equal(solution, expected_solution):
            raise InputError(f'solution {index} is not the exact replayed record')
        serialized = _canonical_json(solution)
        if serialized in serialized_solutions:
            raise InputError('duplicate solution record in cell')
        serialized_solutions.add(serialized)
    if row['complete']:
        if (
            not _exact_nonnegative_integer(row.get('count'))
            or row['count'] != len(solutions)
            or not _exact_nonnegative_integer(row.get('unique_cluster_count'))
            or row['unique_cluster_count'] != unique_cluster_count
        ):
            raise InputError('complete-cell count invariants failed')
    elif row.get('count') is not None or row.get('unique_cluster_count') is not None:
        raise InputError('incomplete cell must have null count fields')
    if not isinstance(row.get('stats'), dict):
        raise InputError('cell stats must be an object')
    expected_stats_keys = {
        'expanded_states', 'generated_states', 'symmetry_duplicates',
        'terminal_states', 'point_cap_prunes', 'resource_stop',
        'elapsed_seconds',
    }
    if set(row['stats']) != expected_stats_keys:
        raise InputError('cell stats keys mismatch')
    for key in (
        'expanded_states', 'generated_states', 'symmetry_duplicates',
        'terminal_states', 'point_cap_prunes',
    ):
        if not _exact_nonnegative_integer(row['stats'].get(key)):
            raise InputError(f'cell stats.{key} must be a nonnegative integer')
    if row['stats']['symmetry_duplicates'] > row['stats']['generated_states']:
        raise InputError('cell symmetry-duplicate count exceeds generated states')
    if row['stats']['terminal_states'] > row['stats']['expanded_states']:
        raise InputError('cell terminal count exceeds expanded states')
    if row['stats']['point_cap_prunes'] > row['stats']['expanded_states']:
        raise InputError('cell point-cap prunes exceed expanded states')
    if unique_cluster_count > row['stats']['terminal_states']:
        raise InputError('serialized unique clusters exceed terminal states')
    if row['stats']['expanded_states'] > (
        row['stats']['generated_states']
        - row['stats']['symmetry_duplicates']
        + row['aggregate_groups']
    ):
        raise InputError('expanded-state count exceeds generated-state supply')
    elapsed = row['stats']['elapsed_seconds']
    if (
        not isinstance(elapsed, (int, float))
        or isinstance(elapsed, bool)
        or not isfinite(elapsed)
        or elapsed < 0
    ):
        raise InputError('cell elapsed time must be finite and nonnegative')
    if row['stats']['resource_stop'] not in (None, 'max_states', 'deadline'):
        raise InputError('cell resource stop has an unknown value')
    if row['complete'] and (
        row['stats']['resource_stop'] is not None
        or row['stats']['point_cap_prunes'] != 0
    ):
        raise InputError('complete cell retains evidence of a resource cut')
    if (
        not row['complete']
        and row['stats']['resource_stop'] is None
        and row['stats']['point_cap_prunes'] == 0
    ):
        raise InputError('incomplete cell has no serialized cut witness')
    expected_global_nef = True if solutions else None
    if (
        row.get('global_nef_certified') != expected_global_nef
        or type(row.get('global_nef_certified')) is not type(expected_global_nef)
    ):
        raise InputError('cell global-nef aggregate is inconsistent')

    if not _json_exact_equal(local_summary, _summary([row], (N,), (D,))):
        raise InputError('cell-local summary is not the exact derived summary')
    return row


def merge_row_files(args: argparse.Namespace) -> tuple[list[dict[str, object]], dict[str, object]]:
    Ns, Ds = _resolve_range(args)
    if args.expected_window != 'explicit' and args.expected_a_values:
        raise InputError(
            '--expected-a-values is only valid with --expected-window explicit'
        )
    if args.expected_window == 'explicit' and not args.expected_a_values:
        raise InputError('--expected-window explicit requires --expected-a-values')
    if args.expected_profile_mode == 'explicit-component-degrees':
        if args.expected_window != 'explicit-component-degrees':
            raise InputError(
                'explicit merge mode requires '
                '--expected-window explicit-component-degrees'
            )
        if args.expected_explicit_component_profiles is None:
            raise InputError(
                'explicit merge mode requires '
                '--expected-explicit-component-profiles FILE'
            )
        if args.expected_f_cap is not None or args.expected_a_values:
            raise InputError('explicit merge mode has no H2 f-cap or a-values')
        expected_explicit = load_explicit_component_profiles(
            args.expected_explicit_component_profiles
        )
        expected_corpus_id = explicit_profile_corpus_id(expected_explicit)
    else:
        if args.expected_explicit_component_profiles is not None:
            raise InputError(
                'an expected explicit corpus requires explicit-component merge mode'
            )
        if args.expected_window == 'explicit-component-degrees':
            raise InputError('generated H2 merge mode cannot use an explicit window')
        for N in Ns:
            fixed_sheet_values(N, args.expected_window, args.expected_a_values)
        expected_corpus_id = GENERATED_PROFILE_CORPUS_ID
    rows: list[dict[str, object]] = []
    missing: list[str] = []
    invalid: list[dict[str, str]] = []
    for N in Ns:
        for D in Ds:
            name = f'N{N:03d}-D{D:03d}.jsonl'
            path = args.input_dir / name
            if not path.is_file():
                missing.append(name)
                continue
            try:
                with path.open('r', encoding='utf-8') as handle:
                    first = handle.readline()
                    second = handle.readline()
                    extra = handle.readline()
                if not first or not second or extra:
                    raise InputError('cell shard must contain exactly two compact JSONL records')
                row = _validate_merged_cell(
                    strict_json_loads(first),
                    strict_json_loads(second),
                    N=N,
                    D=D,
                    expected_window=args.expected_window,
                    expected_f_cap=args.expected_f_cap,
                    expected_profile_mode=args.expected_profile_mode,
                    expected_a_values=args.expected_a_values,
                    expected_profile_corpus_id=expected_corpus_id,
                    expected_profiles=(
                        tuple(
                            profile for profile in expected_explicit
                            if profile.N == N and profile.D == D
                        )
                        if args.expected_profile_mode == 'explicit-component-degrees'
                        else generate_profiles(
                            N,
                            D,
                            window=args.expected_window,
                            a_values=args.expected_a_values,
                            f_cap=args.expected_f_cap,
                        )
                    ),
                )
                rows.append(row)
            except (
                IndexError, KeyError, TypeError, ValueError,
                UnicodeError, OSError,
            ) as exc:
                invalid.append({'file': name, 'error': str(exc)})
    summary = _summary(rows, Ns, Ds)
    summary['missing_row_files'] = missing
    summary['invalid_row_files'] = invalid
    summary['all_rows_complete'] = (
        bool(summary['all_rows_complete']) and not missing and not invalid
    )
    return rows, summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)

    self_test = sub.add_parser('self-test', help='run all frozen controls')
    self_test.add_argument('--pretty', action='store_true')

    plan = sub.add_parser('plan', help='count scalar parameter rows only')
    _add_range_arguments(plan)
    _add_profile_arguments(plan)
    plan.add_argument('--pretty', action='store_true')

    census = sub.add_parser('census', help='enumerate exact numerical forests')
    _add_range_arguments(census)
    _add_profile_arguments(census)
    census.add_argument(
        '--max-states', type=int, default=2_000_000,
        help='per-(N,D) resource cap; 0 means unbounded',
    )
    census.add_argument(
        '--deadline-seconds', type=float, default=840.0,
        help='per-(N,D) wall cap; 0 means unbounded',
    )
    census.add_argument(
        '--max-points', type=int,
        help='optional artificial cap; any prune marks the row incomplete',
    )
    census.add_argument('--output', type=Path, help='atomic JSONL output path')
    census.add_argument('--overwrite', action='store_true')
    census.add_argument('--pretty', action='store_true')

    merge = sub.add_parser('merge', help='fail-closed merge of per-cell JSONL files')
    _add_range_arguments(merge)
    merge.add_argument('input_dir', type=Path)
    merge.add_argument('--output', type=Path, required=True)
    merge.add_argument('--overwrite', action='store_true')
    merge.add_argument(
        '--expected-window',
        choices=(
            'strict', 'legacy-inclusive', 'all-h2', 'explicit',
            'explicit-component-degrees',
        ),
        default='strict',
    )
    merge.add_argument(
        '--expected-f-cap', type=_parse_f_cap, default=None,
        metavar='INTEGER|unbounded',
    )
    merge.add_argument(
        '--expected-profile-mode',
        choices=('H2-common-n', 'explicit-component-degrees'),
        default='H2-common-n',
    )
    merge.add_argument('--expected-a-values', type=_parse_a_values, default=())
    merge.add_argument(
        '--expected-explicit-component-profiles',
        type=Path,
        help=(
            'validated JSON/JSONL corpus used to derive the expected semantic '
            'SHA-256 in explicit-component merge mode'
        ),
    )

    validate = sub.add_parser('validate', help='validate one cluster JSON object')
    validate.add_argument('input', type=Path, help="JSON file, or '-' for stdin")
    validate.add_argument('--pretty', action='store_true')
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == 'self-test':
            result = run_self_tests()
            print(json.dumps(result, indent=2 if args.pretty else None, sort_keys=True))
            return 0 if result['ok'] else 1
        if args.command == 'plan':
            print(json.dumps(plan_rows(args), indent=2 if args.pretty else None, sort_keys=True))
            return 0
        if args.command == 'validate':
            text = sys.stdin.read() if str(args.input) == '-' else args.input.read_text(encoding='utf-8')
            raw = strict_json_loads(text)
            if not isinstance(raw, dict):
                raise InputError('cluster input must be a JSON object')
            required = {'D', 'N', 'multiplicities', 'forest_shape'}
            unknown = set(raw) - required
            missing = required - set(raw)
            if unknown or missing:
                raise InputError(
                    f'cluster keys mismatch; missing={sorted(missing)}, unknown={sorted(unknown)}'
                )
            result = validate_cluster(
                raw['D'], raw['multiplicities'], raw['forest_shape'],
                expected_N=raw['N'],
            )
            print(json.dumps(result, indent=2 if args.pretty else None, sort_keys=True))
            return 0 if result['ok'] else 1
        if args.output is not None and getattr(args, 'pretty', False):
            raise InputError(
                '--pretty is stdout-only; output shards must remain compact JSONL'
            )
        if args.output is not None and args.output.exists() and not args.overwrite:
            raise InputError(
                f'output already exists (use --overwrite explicitly): {args.output}'
            )
        if args.command == 'merge':
            rows, summary = merge_row_files(args)
        else:
            rows, summary = run_census_command(args)
        documents = [*rows, summary]
        if getattr(args, 'pretty', False):
            rendered = '\n'.join(json.dumps(row, indent=2, sort_keys=True) for row in documents) + '\n'
        else:
            rendered = '\n'.join(json.dumps(row, sort_keys=True, separators=(',', ':')) for row in documents) + '\n'
        if args.output:
            _atomic_write(args.output, rendered, overwrite=args.overwrite)
        else:
            sys.stdout.write(rendered)
        return 0 if summary['all_rows_complete'] else 2
    except (
        KeyError, TypeError, ValueError, UnicodeError, OSError,
    ) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 64
    except InternalInvariantError as exc:
        print(f'INTERNAL_ERROR: {exc}; no complete result emitted', file=sys.stderr)
        return 70
    except (MemoryError, RecursionError, OverflowError) as exc:
        print(f'RESOURCE_ERROR: {type(exc).__name__}; no complete result emitted', file=sys.stderr)
        return 70


if __name__ == '__main__':
    raise SystemExit(main())
