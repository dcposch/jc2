#!/usr/bin/env python3
"""Fail-closed evaluation harness for proposed Moh-program restrictions.

Every predicate is applied only after the frozen (1)--(13) arithmetic filter.
A candidate is marked WRONG as a general restriction when it removes even one
of the six p.202 rows.  Source status is metadata, not inferred from counts.
"""

from __future__ import annotations

import json
import itertools
import sys
import time
from dataclasses import dataclass
from functools import lru_cache
from fractions import Fraction
from math import lcm
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "repro"))
import moh_skeleton_full as M  # noqa: E402
import full_tree_partition as FT  # noqa: E402


@dataclass(frozen=True)
class Candidate:
    name: str
    description: str
    source_status: str
    predicate: object


def row_key(S):
    return S.n, S.m, tuple(S.M[i] for i in range(2, S.s + 1)), tuple((i, S.V[i]) for i in range(2, S.s + 1))


def top_split_strict(S):
    return S.V[S.s] < S.d[S.s]


def top_radius(S):
    return (S.d[S.s] - S.V[S.s]) * (S.n - S.M[S.s - 1]) >= S.d[S.s]


def path_radius(S, i, path_V):
    numerator = Fraction(S.n - S.M[i], 1)
    denominator = Fraction(S.n - S.M[S.s] - 1, 1)
    for j in range(i + 1, S.s + 1):
        numerator *= path_V[j] * (S.n - S.M[j]) - S.d[j]
        denominator *= path_V[j] * (S.n - S.M[j - 1]) - S.d[j]
    return 1 - numerator / denominator


def zero_path_trace(S):
    """Universal/minimal zero-root path forced by Prop.5.6.

    At each level the zero factor has multiplicity congruent to P modulo A.
    Its minimal possible multiplicity is the canonical remainder b.  If b=0,
    zero can be absent; if b is at or below the major threshold, it is minor.
    In either case there is no forced all-zero *major* continuation.  If the
    canonical zero stays major through j=2, Prop.5.6 rejects the skeleton.
    """
    path_V = {S.s: S.V[S.s], S.s + 1: S.d[S.s + 1]}
    deltas = {S.s: path_radius(S, S.s, path_V)}
    trace = []
    for j in range(S.s - 1, 1, -1):
        delta_j = path_radius(S, j, path_V)
        deltas[j] = delta_j
        L = 1
        for i in range(j + 1, S.s + 1):
            L = lcm(L, deltas[i].denominator)
        A = (L * delta_j).denominator
        p_numerator = path_V[j + 1] * S.d[j]
        assert p_numerator % S.d[j + 1] == 0
        P = p_numerator // S.d[j + 1]
        b = P % A
        threshold = Fraction(S.d[j], S.n - S.M[j])
        is_forced_major = b > threshold
        trace.append({
            "j": j, "parent_V": path_V[j + 1], "delta": str(delta_j),
            "L": L, "A": A, "P": P, "b": b, "major_threshold": str(threshold),
            "forced_major": is_forced_major,
        })
        if b == 0 or not is_forced_major:
            return True, trace
        path_V[j] = b
    return False, trace


def zero_path(S):
    return zero_path_trace(S)[0]


def strict_upper(S, levels):
    return all(S.V[j] < S.V[j + 1] * S.d[j] // S.d[j + 1] for j in levels)


def q_degree(S, j):
    numerator = S.V[j + 1] * (S.n - S.M[j])
    assert numerator % S.d[j + 1] == 0
    return numerator // S.d[j + 1]


def selected_ode_nondegenerate(S):
    for j in range(2, S.s):
        P = S.V[j + 1] * S.d[j] // S.d[j + 1]
        Q = q_degree(S, j)
        if P - Q * S.V[j] == 0:
            return False
    return True


def q_residue_01(S):
    return all(q_degree(S, j) % S.A(j) in {0, 1 % S.A(j)} for j in range(2, S.s))


def q_residue_1(S):
    return all((q_degree(S, j) - 1) % S.A(j) == 0 for j in range(2, S.s))


def q_branch_compatible(S, include_overlap_as_zero=False):
    """Existentially assign a nonzero or zero factor at every printed level.

    A q-degree has only free A-orbits and optionally one simple fixed zero.
    If a zero branch is chosen, its q residue must therefore be one.  By
    default a level satisfying both (10) and (11) may choose the nonzero branch.
    The ``include_overlap_as_zero`` variant forces every (11)-compatible level,
    including overlap, to satisfy residue one.
    """
    for j in range(2, S.s):
        residue = q_degree(S, j) % S.A(j)
        if residue not in {0, 1 % S.A(j)}:
            return False
        _, by10, by11 = S.cond1011(j)
        if include_overlap_as_zero:
            if by11 and residue != 1 % S.A(j):
                return False
        elif not (by10 or (by11 and residue == 1 % S.A(j))):
            return False
    return True


def p_partition_canonical_zero(S):
    """Stronger inferred factor partition: bound the fixed-zero exponent < A.

    Nonzero selection consumes A*V_j.  Zero selection is allowed only when
    V_j is the canonical remainder, rather than merely congruent to it.
    """
    for j in range(2, S.s):
        tri, square, _, _ = S.div9(j)
        if not (S.V[j] <= tri or S.V[j] == square):
            return False
    return True


def p_partition_nontrivial_remainder(S):
    """Require a selected p-factor and a positive complementary p-degree."""
    for j in range(2, S.s):
        tri, square, A, P = S.div9(j)
        nonzero = S.V[j] <= tri and P - A * S.V[j] > 0
        zero = (S.V[j] - square) % A == 0 and P - S.V[j] > 0
        if not (nonzero or zero):
            return False
    return True


def pq_partition_untyped(S):
    """Existential orbit partition without guessing which polynomial owns zero.

    The p-side existence is precisely printed (10)/(11); the only new scalar
    test is q-degree residue 0/1.  This is expected to collapse to q_residue_01.
    """
    return q_residue_01(S) and all(S.cond1011(j)[0] for j in range(2, S.s)) and top_split_strict(S)


def pq_partition_no_common_zero(S):
    """Over-strong trial: canonical p/q partitions may not share a zero root."""
    for j in range(2, S.s):
        tri, square, A, P = S.div9(j)
        qres = q_degree(S, j) % A
        if qres not in {0, 1 % A}:
            return False
        choices = []
        # Select a nonzero p-orbit.  The remaining p-degree has a canonical
        # fixed-zero exponent congruent to P mod A.
        if S.V[j] <= tri:
            p_has_zero = square != 0
            choices.append(not (p_has_zero and qres == 1 % A))
        # Select p's zero factor.  Coprimeness then demands no q zero.
        if (S.V[j] - square) % A == 0:
            choices.append(qres == 0)
        if not any(choices):
            return False
    return True


def mu_and_r(S):
    mu = {1: S.M[1]}
    for i in range(2, S.s + 1):
        mu[i] = (S.d[i - 1] // S.d[i]) * mu[i - 1] + S.M[i] - S.M[i - 1]
    r = {0: S.n, **{i: -mu[i] for i in range(1, S.s + 1)}}
    return mu, r


@lru_cache(maxsize=None)
def in_semigroup(target, generators):
    if target < 0 or any(g <= 0 for g in generators):
        return False
    reachable = bytearray(target + 1)
    reachable[0] = 1
    for value in range(target + 1):
        if not reachable[value]:
            continue
        for generator in generators:
            nxt = value + generator
            if nxt <= target:
                reachable[nxt] = 1
    return bool(reachable[target])


def semigroup_test(S, *, terminal=True, approximate=True, alternative_index=False, local_orientation=False):
    _, r = mu_and_r(S)
    end = S.s if terminal else S.s - 1
    for i in range(1, end + 1):
        if alternative_index and i >= 2:
            multiplier = S.d[i - 1] // S.d[i]
        else:
            multiplier = S.d[i] // S.d[i + 1]
        if not in_semigroup(multiplier * r[i], tuple(r[k] for k in range(i))):
            return False
    if not approximate:
        return True
    if not (r[0] > r[1]):
        return False
    for i in range(2, end + 1):
        bound = (S.d[i - 1] // S.d[i]) * r[i - 1]
        if local_orientation:
            if not r[i] > bound:
                return False
        elif not r[i] < bound:
            return False
    return True


def prop31_bounded_semigroup(S, terminal=True):
    """Moh Prop.3.1 p.159 (13), including the digit bounds.

    For each effective r, find j>=0 and 0<=alpha_i<n_i (i<r) with
    j*n + sum R_i alpha_i = n_r R_r, where R_i=-mu_i.
    """
    _, R = mu_and_r(S)
    end = S.s if terminal else S.s - 1
    for r in range(1, end + 1):
        if not S.M[r] < S.n - 1:
            continue
        nr = S.d[r] // S.d[r + 1]
        target = nr * R[r]
        digit_ranges = [range(S.d[i] // S.d[i + 1]) for i in range(1, r)]
        found = False
        for digits in itertools.product(*digit_ranges):
            remainder = target - sum(R[i] * digits[i - 1] for i in range(1, r))
            if remainder >= 0 and remainder % S.n == 0:
                found = True
                break
        if not found:
            return False
    return True


def candidates():
    return [
        Candidate("base_printed_1_13", "No added restriction", "baseline", lambda S: True),
        Candidate("top_split_strict", "V_s < d_s (both top factors occur)", "PROVED-IN-SOURCE p.194,p.200; already in enumerator", top_split_strict),
        Candidate("top_radius", "(d_s-V_s)(n-M_{s-1}) >= d_s", "PROVED-IN-SOURCE Lemma 6.1 p.194", top_radius),
        Candidate("strict_upper_top_previous", "V_{s-1} < V_s d_{s-1}/d_s", "RETRACTED/INDEX-ERROR probe, not source-backed", lambda S: strict_upper(S, [S.s - 1])),
        Candidate("strict_upper_all_levels", "V_j < V_{j+1}d_j/d_{j+1} for every j=2..s-1", "exploratory strengthening of (7)", lambda S: strict_upper(S, range(2, S.s))),
        Candidate("q_orbit_residue_01", "Qq_j mod A_j is 0 or 1", "orbit-partition candidate", q_residue_01),
        Candidate("q_A3_residue_1", "A_j divides Qq_j-1 at every level", "source-derived from Prop.5.3 q plus A.3", q_residue_1),
        Candidate("q_branch_existential", "q residue 0/1 and a compatible nonzero/zero selected branch exists", "inferred typed factor-choice candidate", q_branch_compatible),
        Candidate("q_every_11_means_zero", "force q residue 1 whenever (11) is arithmetically available", "known type-confusion stress test", lambda S: q_branch_compatible(S, include_overlap_as_zero=True)),
        Candidate("p_canonical_zero_partition", "fixed-zero p multiplicity is the canonical remainder < A", "inferred stronger p-factor partition", p_partition_canonical_zero),
        Candidate("p_positive_complement", "selected p factor leaves positive complementary p-degree", "inferred factor-partition probe", p_partition_nontrivial_remainder),
        Candidate("pq_untyped_partition", "existential p partition + q 0/1 residue + top minor", "inferred full-factor partition without zero ownership", pq_partition_untyped),
        Candidate("pq_no_common_zero_canonical", "canonical p/q partitions have no common zero", "over-strong inferred probe", pq_partition_no_common_zero),
        Candidate("C_ZERO_PATH", "reject iff the canonical zero multiplicity is forced major at every level through j=2", "PROVED-IN-SOURCE universal Prop.5.6 zero-path application", zero_path),
        Candidate("C_FULL_TREE", "exact orbit-factor partition with every major child recursively feasible and selected path embedded", "source-motivated finite model of Prop.5.3/5.6; global sufficiency remains OPEN", FT.full_tree_ok),
        Candidate("ode_selected_nondegenerate", "P-Q*V_j is nonzero on the one selected path", "PROVED-IN-SOURCE local consequence of the A.3 differential equation", selected_ode_nondegenerate),
        Candidate("C_FULL_TREE_ODE", "full orbit-factor tree with P-Q*u nonzero at every p-root", "PROVED-IN-SOURCE local A.3 consequence inside an inferred global tree model", FT.full_tree_ode_ok),
        Candidate("C_FULL_TREE_PASSPORT", "full tree plus the cyclic-quotient weighted-tree passport inequality", "SOURCE-DERIVED from A.3 ODE plus elementary rational-map degree; necessary, not Moh-stated", FT.full_tree_passport_ok),
        Candidate("C_FULL_TREE_POLYNOMIAL", "full tree, with nonzero integral-radius factors still dangerous under polynomial recentering", "inferred Prop.5.4 coupling; source equivalence remains OPEN", FT.full_tree_polynomial_ok),
        Candidate("C_FULL_TREE_POLYNOMIAL_ODE", "full tree plus polynomial recentering and P-Q*u nonvanishing at every p-root", "necessary ODE consequence of Prop.4.6/5.3; full ODE realizability remains OPEN", FT.full_tree_polynomial_ode_ok),
        Candidate("C_FULL_TREE_POLYNOMIAL_PASSPORT", "full tree plus polynomial recentering and the cyclic-quotient weighted-tree passport inequality", "passport is SOURCE-DERIVED necessary; polynomial danger propagation remains INFERRED/OPEN", FT.full_tree_polynomial_passport_ok),
        Candidate("not_all_11_shadow", "at least one level also satisfies numerical (10)", "OPEN numerical shadow of Prop.5.6; branch type not encoded", lambda S: S.any10()),
        Candidate("all_levels_10", "force printed (10) at every level", "falsification probe; drops branch (11)", lambda S: all(S.cond1011(j)[1] for j in range(2, S.s))),
        Candidate("semigroup_membership_all", "n_i r_i lies in prior semigroup, through terminal M_s", "standard characteristic-semigroup candidate", lambda S: semigroup_test(S, terminal=True, approximate=False)),
        Candidate("semigroup_standard_all", "membership plus infinity approximate-root inequalities, through M_s", "standard characteristic-semigroup candidate", lambda S: semigroup_test(S, terminal=True, approximate=True)),
        Candidate("semigroup_standard_preterminal", "standard test excluding appended M_s=n-2", "explicit terminal-index alternative", lambda S: semigroup_test(S, terminal=False, approximate=True)),
        Candidate("C_SEMIGROUP_ALL", "Prop.3.1 bounded-digit semigroup equation for every effective r", "PROVED-IN-SOURCE Prop.3.1 pp.157-159, eq.(13)", lambda S: prop31_bounded_semigroup(S, terminal=True)),
        Candidate("C_SEMIGROUP_PRETERMINAL", "Prop.3.1 bounded-digit equation excluding appended M_s", "explicit terminal-index alternative", lambda S: prop31_bounded_semigroup(S, terminal=False)),
        Candidate("semigroup_alt_multiplier_all", "use shifted d_{i-1}/d_i multiplier", "explicit alternative indexing; expected fail-closed rejection", lambda S: semigroup_test(S, terminal=True, approximate=True, alternative_index=True)),
        Candidate("semigroup_alt_multiplier_preterminal", "shifted multiplier, exclude M_s", "explicit alternative indexing; expected fail-closed rejection", lambda S: semigroup_test(S, terminal=False, approximate=True, alternative_index=True)),
        Candidate("semigroup_local_inequality", "reverse approximate-root inequality orientation", "explicit local-orientation stress test", lambda S: semigroup_test(S, terminal=True, approximate=True, local_orientation=True)),
        Candidate("source_scalar_conjunction", "top radius + q A.3 + standard semigroup", "conjunction of source-derived scalar candidates", lambda S: top_radius(S) and q_residue_1(S) and semigroup_test(S, terminal=True, approximate=True)),
    ]


def groups_and_uni(rows):
    groups = {}
    for S in rows:
        key = (S.n, S.m, tuple(S.M[i] for i in range(2, S.s + 1)), S.V[S.s])
        groups.setdefault(key, []).append((S.V[2], S.q(), S.u))
    alive = {key for key, items in groups.items() if M.uni_hits(items, 6, None)}
    return groups, alive


def evaluate(candidate, small_rows, degree_rows, printed_keys, baseline_active):
    selected_small = [S for S in small_rows if candidate.predicate(S)]
    selected_keys = {row_key(S) for S in selected_small}
    killed = sorted(printed_keys - selected_keys)
    rows75 = [S for S in selected_small if (S.n, S.m) == (75, 50)]

    selected_degree = [S for S in degree_rows if candidate.predicate(S)]
    groups, alive = groups_and_uni(selected_degree)
    active_degrees = {key[0] for key in groups}
    alive_degrees = {key[0] for key in alive}

    def range_stats(lo, hi):
        base = {n for n in baseline_active if lo <= n <= hi}
        rrows = sum(lo <= S.n <= hi for S in selected_degree)
        rgroups = {key for key in groups if lo <= key[0] <= hi}
        ralive = {key for key in alive if lo <= key[0] <= hi}
        ractive_degrees = {key[0] for key in rgroups}
        ralive_degrees = {key[0] for key in ralive}
        return {
            "V_assignments": rrows,
            "groups": len(rgroups),
            "pinned_N_ge_6_alive_groups": len(ralive),
            "candidate_zero_degrees_among_baseline_active": sorted(base - ractive_degrees),
            "pinned_N_empty_degrees_among_candidate_active": sorted(ractive_degrees - ralive_degrees),
            "all_empty_after_pinned_N_among_baseline_active": sorted(base - ralive_degrees),
        }
    per_degree = {}
    for n in (105, 108, 112, 117, 120):
        nrows = [S for S in selected_degree if S.n == n]
        ngroups = {key for key in groups if key[0] == n}
        nalive = {key for key in alive if key[0] == n}
        per_degree[str(n)] = {"V_assignments": len(nrows), "groups": len(ngroups), "pinned_N_ge_6_alive_groups": len(nalive)}

    return {
        "name": candidate.name,
        "description": candidate.description,
        "source_status": candidate.source_status,
        "fail_closed": len(killed) == 0,
        "verdict": "SURVIVES-FAIL-CLOSED" if not killed else "WRONG-AS-GENERAL-RESTRICTION",
        "n_le_100": {
            "rows": len(selected_small),
            "groups": len({(S.n, S.m, tuple(S.M[i] for i in range(2, S.s + 1)), S.V[S.s]) for S in selected_small}),
            "nm_classes": len({(S.n, S.m) for S in selected_small}),
            "printed_rows_killed": len(killed),
            "printed_keys_killed": [repr(key) for key in killed],
            "at_75_50": [
                {"M": [S.M[i] for i in range(2, S.s + 1)], "V": {str(i): S.V[i] for i in range(2, S.s + 1)}}
                for S in sorted(rows75, key=row_key)
            ],
            "at_75_50_M2": sorted({S.M[2] for S in rows75}),
            "at_75_50_M2_V2": sorted({(S.M[2], S.V[2]) for S in rows75}),
        },
        "D_48_200": {
            "V_assignments": len(selected_degree),
            "groups": len(groups),
            "pinned_N_ge_6_alive_groups": len(alive),
            "baseline_active_degrees": sorted(baseline_active),
            "candidate_zero_degrees_among_baseline_active": sorted(baseline_active - active_degrees),
            "pinned_N_empty_degrees_among_candidate_active": sorted(active_degrees - alive_degrees),
            "all_empty_after_pinned_N_among_baseline_active": sorted(baseline_active - alive_degrees),
            "selected_degree_counts": per_degree,
            "ranges": {
                "48_120": range_stats(48, 120),
                "121_200": range_stats(121, 200),
                "48_200": range_stats(48, 200),
            },
        },
    }


def render_markdown(results, elapsed):
    lines = [
        "# Candidate restriction evaluation",
        "",
        "All rows start in the frozen printed-(1)--(13) arithmetic space. `WRONG` means the candidate kills at least one of Moh's six printed rows. Counts cannot establish source provenance or actual characteristic-data realizability.",
        "",
        "| candidate | n<=100 rows/classes | printed killed | (75,50) M2/V2 | D48-200 V/groups/UNI | verdict |",
        "|---|---:|---:|---|---:|---|",
    ]
    for result in results:
        s = result["n_le_100"]
        d = result["D_48_200"]
        pairs = " ".join(f"{a}/{b}" for a, b in s["at_75_50_M2_V2"])
        lines.append(f"| `{result['name']}` | {s['rows']}/{s['nm_classes']} | {s['printed_rows_killed']} | {pairs or '-'} | {d['V_assignments']}/{d['groups']}/{d['pinned_N_ge_6_alive_groups']} | {result['verdict']} |")
    lines += ["", f"Wall time: {elapsed:.2f}s.", "", "Per-degree counts and exact killed-row keys are in `candidate-results.json`.", ""]
    return "\n".join(lines)


def main():
    t0 = time.time()
    small_rows = [
        M.Skel(n, m, list(Ms), V)
        for n in range(4, 101)
        for m, Ms, V in M.census(n, Kmin=2, full=True)
    ]
    degree_rows = [
        M.Skel(n, m, list(Ms), V)
        for n in range(48, 201)
        for m, Ms, V in M.census(n, Kmin=16, full=True)
    ]
    assert len(small_rows) == 658 and len({(S.n, S.m) for S in small_rows}) == 63
    assert len(degree_rows) == 23720
    printed_keys = {
        (n, m, tuple(Ms), tuple(sorted(Vs.items())))
        for n, m, Ms, Vs, *_ in M.MOH_TABLE
    }
    got_keys = {row_key(S) for S in small_rows}
    assert printed_keys <= got_keys
    baseline_active = {S.n for S in degree_rows}

    results = [evaluate(candidate, small_rows, degree_rows, printed_keys, baseline_active) for candidate in candidates()]
    elapsed = time.time() - t0
    payload = {
        "frozen_module_sha256": "d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2",
        "scope": {"small": "4<=n<=100,Kmin=2", "degree": "48<=D<=200,Kmin=16", "pinned_N": "UNI, integer N>=6"},
        "baseline": {"small_rows": len(small_rows), "small_nm_classes": 63, "degree_rows": len(degree_rows)},
        "elapsed_seconds": elapsed,
        "results": results,
    }
    (HERE / "candidate-results.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    (HERE / "candidate-results.md").write_text(render_markdown(results, elapsed))
    print(render_markdown(results, elapsed))


if __name__ == "__main__":
    main()
