#!/usr/bin/env python3
"""Independent bounded audit for the fixed-family moment question.

This does not manufacture a decorated skeleton.  It records the two canonical
linear parity models that are compatible with the charged data and exhibits
the dependence of raw tropical bases on the unspecified non-proper tree.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as F
from math import comb, factorial, lcm
from pathlib import Path


INPUT = Path("/tmp/jc2-lane.CBLhSa/inputs")
EXPECTED = {
    "ideation-20260903T1015Z-sol56.md": "20f290f7e33a3b8a4f97d303751633b9d9b2df50ca8cbd0a46498856be5d5b2f",
    "global-interpolation-sol56-20260902.md": "20d554a0b19c563093ec35caad58664f800d7517490f530a07f511d7042393b6",
    "globalinterp.py": "49ba5a019714e30a952c998fb39a88aff38505a80fcac6df3c5883bb16599588",
    "branch-orbits-v2-grok46-20260903.md": "55db4a9ef9021ef28d3a86dbd3e44d5e3a5aa1b72d61ba23043497f78ba94411",
    "knapsack.py": "aaea3c345b1d53f561798f6a3e4352722f56c50a762f141dfe5e59cf35b1f276",
    "census-rebase-opus5-20260902.md": "fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948",
    "moh_skeleton_full.py": "d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2",
    "integration17-coordinator-fable51-20260902.md": "126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5",
}


def custody() -> None:
    for name, expected in EXPECTED.items():
        actual = hashlib.sha256((INPUT / name).read_bytes()).hexdigest()
        if actual != expected:
            raise SystemExit(f"CUSTODY MISMATCH {name}: {actual}")


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    a = [[entry % prime for entry in row] for row in matrix]
    if not a:
        return 0
    nr, nc = len(a), len(a[0])
    row = 0
    for col in range(nc):
        pivot = next((r for r in range(row, nr) if a[r][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, prime)
        a[row] = [(v * inv) % prime for v in a[row]]
        for r in range(nr):
            if r != row and a[r][col]:
                q = a[r][col]
                a[r] = [(u - q * v) % prime for u, v in zip(a[r], a[row])]
        row += 1
        if row == nr:
            break
    return row


def vandermonde(rows: int, nodes: list[int], prime: int) -> list[list[int]]:
    return [[pow(node, r, prime) for node in nodes] for r in range(rows)]


def derivative_weights(count: int, prime: int) -> list[int]:
    """1/G'(i), G=X(X-1)...(X-count+1), valid for prime>count."""
    out = []
    for i in range(count):
        derivative = factorial(i) * factorial(count - 1 - i)
        if (count - 1 - i) % 2:
            derivative = -derivative
        out.append(pow(derivative % prime, -1, prime))
    return out


def weighted_vandermonde(rows: int, count: int, prime: int) -> list[list[int]]:
    weights = derivative_weights(count, prime)
    return [[pow(i, r, prime) * weights[i] % prime for i in range(count)] for r in range(rows)]


def min_cluster_extra(sizes: list[int], extras: list[F], total: int):
    dp: list[tuple[F, tuple[int, ...]] | None] = [None] * (total + 1)
    dp[0] = (F(0), ())
    for size, extra in zip(sizes, extras):
        nxt: list[tuple[F, tuple[int, ...]] | None] = [None] * (total + 1)
        for used, state in enumerate(dp):
            if state is None:
                continue
            for take in range(min(size, total - used) + 1):
                candidate = (state[0] + extra * comb(take, 2), state[1] + (take,))
                old = nxt[used + take]
                if old is None or candidate[0] < old[0]:
                    nxt[used + take] = candidate
        dp = nxt
    return dp[total]


def l5_completion_optimum(kind: str):
    """Minimise complement-pair contacts for a 34-column raw basis.

    Common data: 18 proper triples at 7/12; seven residual-major triples
    with between-triple contact 47/120 and internal contact 19/48 (both
    strictly between delta2=7/18 and 2/5); cross-contact 7/18 elsewhere
    inside the 75-root D2; and outer/D2 contact -1.
    A: ten outer non-proper triples, mutually at 0 and internally at 2.
    B: the same ten triples, mutually at 3/2 and internally at 2.

    These are contact-tree completions only; no polynomial/Keller
    realisability claim is made.
    """
    delta2, delta1 = F(7, 18), F(7, 12)
    alpha_major, beta_major, beta_outer = F(47, 120), F(19, 48), F(2)
    proper_states = [
        min_cluster_extra([3] * 18, [delta1 - delta2] * 18, x)
        for x in range(55)
    ]
    residual_states = [
        min_cluster_extra([3] * 7, [beta_major - alpha_major] * 7, x)
        for x in range(22)
    ]
    d2_states = []
    for total in range(76):
        choices = []
        for residual_take in range(max(0, total - 54), min(21, total) + 1):
            proper_take = total - residual_take
            proper_extra, proper_allocation = proper_states[proper_take]  # type: ignore[misc]
            residual_extra, residual_allocation = residual_states[residual_take]  # type: ignore[misc]
            extra = (
                proper_extra
                + (alpha_major - delta2) * comb(residual_take, 2)
                + residual_extra
            )
            choices.append((extra, proper_allocation, residual_allocation))
        d2_states.append(min(choices, key=lambda item: item[0]))
    best = None
    for outer_omitted in range(31):
        d2_omitted = 71 - outer_omitted
        if not 0 <= d2_omitted <= 75:
            continue
        d2_extra, proper_allocation, residual_allocation = d2_states[d2_omitted]
        value = delta2 * comb(d2_omitted, 2) - d2_omitted * outer_omitted + d2_extra
        outer_allocation: tuple[int, ...]
        outer_base = F(0) if kind == "A" else F(3, 2)
        outer_extra, outer_allocation = min_cluster_extra(
            [3] * 10, [beta_outer - outer_base] * 10, outer_omitted
        )  # type: ignore[misc]
        value += outer_base * comb(outer_omitted, 2) + outer_extra
        candidate = (
            value,
            d2_omitted,
            outer_omitted,
            proper_allocation,
            residual_allocation,
            outer_allocation,
        )
        if best is None or candidate[0] < best[0]:
            best = candidate
    assert best is not None

    total_d2 = (
        delta2 * comb(75, 2)
        + 18 * (delta1 - delta2) * comb(3, 2)
        + (alpha_major - delta2) * comb(21, 2)
        + 7 * (beta_major - alpha_major) * comb(3, 2)
    )
    total_cross = -75 * 30
    outer_base = F(0) if kind == "A" else F(3, 2)
    total_outer = (
        outer_base * (comb(30, 2) - 10 * comb(3, 2))
        + 10 * beta_outer * comb(3, 2)
    )
    total_contacts = total_d2 + total_cross + total_outer
    return best, -total_contacts + best[0]


def driver_controls_and_custody() -> tuple[int, int]:
    spec = importlib.util.spec_from_file_location("frozen_globalinterp", INPUT / "globalinterp.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    checks = module.run_controls(verbose=False)
    if checks.failures:
        raise AssertionError(checks.failures)
    partial = json.loads(
        (Path(__file__).with_name("independent_partial_orbit.json")).read_text(encoding="utf-8")
    )
    result = module.GlobalInterpolationSystem(partial).result(rank_method="none")
    return checks.count, len(result["direct_conditions"]["no_log"]["verified_orbits"])


def main() -> None:
    custody()
    control_count, accepted_partial = driver_controls_and_custody()
    print(f"custody=PASS controls={control_count}/40 partial_verified_orbits_accepted={accepted_partial}")
    print("ell n m K rows k N proper_roots nonproper_roots R J12 rawP_rank macroP_rank macroFull_rank Schur_rank")
    for ell in (5, 13, 21, 29):
        n, m, K = 21 * ell, 14 * ell, 7 * ell
        rows = K - 1
        k = 3 * (5 * ell - 1) // 4
        delta2 = F(2 * (3 * ell - 1), 3 * (5 * ell - 1))
        R = lcm(12, delta2.denominator)
        J12 = R * (F(7, 12) - delta2)
        macro_ranks = []
        schur_ranks = []
        for prime in (211, 223, 227):
            macro = weighted_vandermonde(rows, K, prime)
            macro_ranks.append((rank_mod([row[:k] for row in macro], prime), rank_mod(macro, prime)))
            nonproper_count = K - k
            schur = weighted_vandermonde(nonproper_count - 1, nonproper_count, prime)
            schur_ranks.append(rank_mod(schur, prime))
        raw_ranks = []
        for prime in (1009, 1013, 1019):
            raw_ranks.append(rank_mod(vandermonde(rows, list(range(3 * k)), prime), prime))
        assert len(set(raw_ranks)) == 1
        assert len(set(macro_ranks)) == 1
        assert len(set(schur_ranks)) == 1
        print(
            ell,
            n,
            m,
            K,
            rows,
            k,
            k // 2 if k % 2 == 0 else f"{k}/2",
            3 * k,
            3 * (K - k),
            R,
            J12,
            raw_ranks[0],
            macro_ranks[0][0],
            macro_ranks[0][1],
            schur_ranks[0],
        )
    for kind in ("A", "B"):
        best, basis_weight = l5_completion_optimum(kind)
        cost, d2_omit, outer_omit, proper_alloc, residual_alloc, outer_alloc = best
        print(
            f"completion_{kind}: complement_contact={cost}, basis_weight={basis_weight}, "
            f"omit_D2={d2_omit}, omit_outer={outer_omit}, "
            f"proper_omit={sorted(proper_alloc)}, residual_omit={sorted(residual_alloc)}, "
            f"outer_omit_profile={sorted(outer_alloc)}"
        )


if __name__ == "__main__":
    main()
