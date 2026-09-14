#!/usr/bin/env python3
"""Exact finite split-window screen for a Moh principal-minor datum.

The public entry point is :func:`screen_skeleton`.  It accepts either a
``moh_skeleton_full.Skel`` object or a mapping containing the corresponding
``n, m, s, M, d, V`` fields.  No computer algebra package is required.

Mathematical scope
------------------
For an actually realised characteristic-zero Keller/Moh datum in Xu's
Section 7.3 setting, put ``u=d_s-v`` and let ``rho`` be the first order at
which the degree-u principal-minor face polynomial ``p`` has more than one
distinct root.  Moh/Xu give

    1 < rho < v/u,            denominator(rho) <= u,

and the split partition is an integer partition of u with at least two
parts.  At such a face, with

    X = u*rho-v,
    W = (-mu_s-2)/d_s,
    a = W*X-1+rho,
    deg(p)=u, deg(q)=W*u+1,

the leading Jacobian equation is

    a*q*p' - X*p*q' = (v-u)*p**(W+1).                 (F)

This module applies two consequences of (F) and Puiseux Galois stability.

``G``  If ``rho=P/Q`` is reduced and ``omega`` is a primitive Q-th root,
       the monic normalization of p obeys
       ``omega**(-u) p(omega*z) = p(z)``.  Thus non-zero roots occur in
       Q-orbits with equal multiplicity; for Q>1 only z=0 can be fixed
       (Q=1 is the trivial action).

``L``  At a p-root of multiplicity lam, the q-multiplicity nu is either
       ``nu=(W-t)*lam`` (a non-negative integer, the cancelled/low case) or
       ``nu=W*lam+1`` (the uncancelled/high case), where
       ``t=(rho-1)/(v-u*rho)``.  The total q-degree supplies an exact finite
       feasibility test.

Passing G and L is NECESSARY only.  A returned survivor is not asserted to be
attained, to lift to a joint chart, or to come from a Keller pair.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Any, Iterable, Iterator, Mapping, Sequence


Q = Fraction


def qstr(value: int | Q) -> str:
    """Stable text for an integer or rational."""
    value = Q(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _indexed(mapping: Mapping[Any, Any], index: int) -> Any:
    """Read either integer- or string-indexed serialized Moh dictionaries."""
    if index in mapping:
        return mapping[index]
    return mapping[str(index)]


def partitions(total: int) -> Iterator[tuple[int, ...]]:
    """Integer partitions in reverse lexicographic order."""
    if total < 0:
        raise ValueError("partition total must be non-negative")

    def visit(left: int, cap: int, prefix: tuple[int, ...]) -> Iterator[tuple[int, ...]]:
        if left == 0:
            yield prefix
            return
        for first in range(min(left, cap), 0, -1):
            yield from visit(left - first, first, prefix + (first,))

    yield from visit(total, total, ())


def genuine_partitions(total: int) -> list[tuple[int, ...]]:
    """Partitions with at least two blocks (one block is not a split)."""
    return [part for part in partitions(total) if len(part) >= 2]


def partition_number(total: int) -> int:
    """Euler recurrence-free dynamic-programming partition count p(total)."""
    if total < 0:
        return 0
    counts = [0] * (total + 1)
    counts[0] = 1
    for summand in range(1, total + 1):
        for value in range(summand, total + 1):
            counts[value] += counts[value - summand]
    return counts[total]


def galois_partition_count(total: int, orbit: int) -> int:
    """Number of genuine partitions compatible with a cyclic orbit of size Q.

    For Q>1, write the non-zero orbit multiplicities as a partition of r.
    They consume Q*r degrees and the remaining ``total-Q*r`` degrees form the
    optional root at zero.  The r=0 term is the nonsplit partition [total], so
    it is subtracted.  For Q=1 the action is trivial.
    """
    if total < 2 or orbit < 1:
        return 0
    if orbit == 1:
        return partition_number(total) - 1
    return sum(partition_number(r) for r in range(total // orbit + 1)) - 1


def full_distinct_is_galois_admissible(total: int, orbit: int) -> bool:
    """Whether (1,...,1) is one optional fixed root plus full Q-orbits."""
    return orbit == 1 or total % orbit in (0, 1)


def radius_window(u: int, v: int) -> list[Q]:
    """Reduced rationals rho with ``1 < rho < v/u`` and ``den(rho)<=u``.

    The numerator bound is exact: strict ``a/q < v/u`` is equivalent to
    ``a <= floor((q*v-1)/u)`` for positive integers.
    """
    if not isinstance(u, int) or not isinstance(v, int):
        raise TypeError("u and v must be integers")
    if u < 1 or v <= u:
        return []
    out: set[Q] = set()
    for denominator in range(1, u + 1):
        largest = (denominator * v - 1) // u
        for numerator in range(denominator + 1, largest + 1):
            if gcd(numerator, denominator) == 1:
                out.add(Q(numerator, denominator))
    return sorted(out)


def radius_count_formula(u: int, v: int) -> int:
    """The exact finite-window cardinality, written as the defining sum."""
    if u < 1 or v <= u:
        return 0
    return sum(
        1
        for denominator in range(1, u + 1)
        for numerator in range(
            denominator + 1, (denominator * v - 1) // u + 1
        )
        if gcd(numerator, denominator) == 1
    )


@dataclass(frozen=True)
class SkeletonView:
    """The skeleton fields used by the face equation and its audit trail."""

    n: int
    m: int
    s: int
    M: tuple[int, ...]       # M_1,...,M_s
    d: tuple[int, ...]       # d_1,...,d_(s+1)
    V: tuple[int, ...]       # V_2,...,V_s
    u: int
    v: int
    mu_s: int
    W: int

    @property
    def row_key(self) -> tuple[Any, ...]:
        return (
            self.n,
            self.m,
            self.M[1:],
            tuple((index, self.V[index - 2]) for index in range(2, self.s + 1)),
        )


def skeleton_view(skeleton: Any) -> SkeletonView:
    """Validate and copy a Moh skeleton without identifying names by accident."""
    if isinstance(skeleton, SkeletonView):
        return skeleton
    getter = skeleton.get if isinstance(skeleton, Mapping) else lambda name: getattr(skeleton, name)
    n = int(getter("n"))
    m = int(getter("m"))
    s = int(getter("s"))
    raw_M = getter("M")
    raw_d = getter("d")
    raw_V = getter("V")
    M = tuple(int(_indexed(raw_M, i)) for i in range(1, s + 1))
    d = tuple(int(_indexed(raw_d, i)) for i in range(1, s + 2))
    V = tuple(int(_indexed(raw_V, i)) for i in range(2, s + 1))
    if s <= 2:
        raise ValueError(f"Xu Section 7.3 split screen requires s>2, got s={s}")
    if M[0] != -m:
        raise ValueError(f"M_1={M[0]} does not equal -m={-m}")
    if M[-1] != n - 2:
        raise ValueError(f"Xu Section 7.3 requires M_s=n-2, got M_s={M[-1]}")
    running = n
    expected_d = [n]
    for characteristic in M:
        running = gcd(running, characteristic)
        expected_d.append(running)
    if tuple(expected_d) != d:
        raise ValueError(f"declared d={d} does not match gcd chain {tuple(expected_d)}")
    v = V[-1]
    u = d[s - 1] - v                    # d_s is tuple position s-1
    if u < 2 or not (v > u):
        raise ValueError(f"split screen requires v_s>u_s>=2, got u={u}, v={v}")

    # Moh p.150 recursion, with q_1=M_1 and q_i=M_i-M_(i-1).
    lam = M[0] * d[0]
    for index in range(2, s + 1):
        lam += (M[index - 1] - M[index - 2]) * d[index - 1]
    d_s = d[s - 1]
    if lam % d_s:
        raise ValueError(f"lambda_s={lam} is not divisible by d_s={d_s}")
    mu_s = lam // d_s
    wq = Q(-mu_s - 2, d_s)
    if wq.denominator != 1 or wq < 0:
        raise ValueError(f"W=(-mu_s-2)/d_s must be a non-negative integer, got {wq}")
    return SkeletonView(n, m, s, M, d, V, u, v, mu_s, int(wq))


def galois_condition(partition: Sequence[int], rho: Q, u: int | None = None) -> dict[str, Any]:
    """Test the normalized Puiseux Galois covariance of the face polynomial."""
    part = tuple(int(value) for value in partition)
    degree = sum(part) if u is None else int(u)
    if sum(part) != degree:
        raise ValueError("partition does not sum to deg p")
    rho = Q(rho)
    orbit = rho.denominator
    multiplicities = Counter(part)
    zero_choices: list[int | None] = [None] + sorted(multiplicities, reverse=True)
    witnesses: list[dict[str, Any]] = []
    remainders: list[dict[str, Any]] = []
    for zero_mult in zero_choices:
        counts = multiplicities.copy()
        if zero_mult is not None:
            counts[zero_mult] -= 1
            if counts[zero_mult] == 0:
                del counts[zero_mult]
        mods = {str(mult): count % orbit for mult, count in sorted(counts.items())}
        if all(remainder == 0 for remainder in mods.values()):
            witnesses.append(
                {
                    "zero_root_multiplicity": zero_mult,
                    "nonzero_orbits": [
                        {"root_multiplicity": mult, "orbit_count": count // orbit}
                        for mult, count in sorted(counts.items(), reverse=True)
                    ],
                }
            )
        else:
            remainders.append({"zero_root_multiplicity": zero_mult, "frequency_mod_Q": mods})
    allowed_degrees = [index for index in range(degree + 1) if (degree - index) % orbit == 0]
    return {
        "name": "G",
        "passes": bool(witnesses),
        "P": rho.numerator,
        "Q": orbit,
        "normalization": f"p_{degree}=1",
        "group_action": f"g.p(z)=omega^(-{degree})*p(omega*z), omega=zeta_{orbit}^{rho.numerator}",
        "canonical_coordinate": "the Galois-fixed common truncation is z=0",
        "conjugated_action": (
            "for the new coordinate w=h(z)=alpha*z+beta and "
            f"P_tilde(w)=alpha^{degree}*P((w-beta)/alpha), "
            "gamma_h(w)=h(omega*h^(-1)(w))=omega*w+(1-omega)*beta; "
            f"omega^(-{degree})*P_tilde(gamma_h(w))=P_tilde(w)"
        ),
        "coefficient_identity": f"p_i=0 unless i == {degree} (mod {orbit})",
        "allowed_coefficient_degrees": allowed_degrees,
        "orbit_witnesses": witnesses,
        "failed_zero_choices": remainders if not witnesses else [],
    }


def local_exponent_condition(
    partition: Sequence[int], rho: Q, u: int, v: int, W: int
) -> dict[str, Any]:
    """Test all local low/high choices via their monotone optimum certificate.

    An eligible root put in the low class decreases the left side of the degree
    budget and increases its right side.  Hence assigning *every* eligible root
    low is optimal; if that assignment fails, every one of the finitely many
    assignments fails.  This makes a compact exact kill certificate.
    """
    part = tuple(int(value) for value in partition)
    if sum(part) != u:
        raise ValueError("partition does not sum to u")
    rho = Q(rho)
    X = Q(u) * rho - v
    if X >= 0:
        raise ValueError("local condition is only for rho < v/u")
    t = (rho - 1) / (v - Q(u) * rho)
    k = Q(W) - t
    low: list[dict[str, Any]] = []
    high: list[dict[str, Any]] = []
    for index, lam in enumerate(part):
        nu_low = k * lam
        item = {"index": index, "lambda": lam, "nu_low": qstr(nu_low)}
        if nu_low.denominator == 1 and nu_low >= 0:
            low.append(item)
        else:
            item["nu_high"] = W * lam + 1
            item["low_rejection"] = (
                "negative" if nu_low < 0 else f"denominator={nu_low.denominator}"
            )
            high.append(item)
    low_mass = sum(item["lambda"] for item in low)
    high_count = len(high)
    bound = t * low_mass + 1
    minimum_degree = sum(int(Q(item["nu_low"])) for item in low) + sum(
        int(item["nu_high"]) for item in high
    )
    degree_q = W * u + 1
    passes = minimum_degree <= degree_q
    # Algebraically equivalent form after cancelling W*u.
    assert passes == (Q(high_count) <= bound)
    return {
        "name": "L",
        "passes": passes,
        "X": qstr(X),
        "t": qstr(t),
        "k": qstr(k),
        "W": W,
        "deg_q": degree_q,
        "optimal_low_roots": low,
        "forced_high_roots": high,
        "minimum_sum_nu": minimum_degree,
        "degree_inequality": f"{minimum_degree} <= {degree_q}",
        "cancelled_inequality": f"{high_count} <= {qstr(bound)}",
        "proof_of_exhaustion": (
            "moving any eligible root from high to low weakly improves the degree budget; "
            "the displayed all-eligible-low assignment is therefore optimal"
        ),
    }


def xu_corollary_7_5(partition: Sequence[int], rho: Q, u: int, v: int) -> dict[str, Any]:
    """Direct source filter; it addresses only the all-distinct partition."""
    part = tuple(int(value) for value in partition)
    cutoff = Q(v + 1, u + 1)
    applies = part == (1,) * u and Q(rho) < cutoff
    return {
        "name": "XU75",
        "excludes": applies,
        "scope": "only the full u_s-distinct split",
        "cutoff": qstr(cutoff),
        "strict_side": qstr(Q(rho)) + " < " + qstr(cutoff),
    }


def face_parameters(view: SkeletonView, rho: Q) -> dict[str, Any]:
    """Exact parameters and coefficient equations for the common split face."""
    rho = Q(rho)
    X = Q(view.u) * rho - view.v
    a = Q(view.W) * X - 1 + rho
    degree_q = view.W * view.u + 1
    top = view.v - view.u
    return {
        "rho": qstr(rho),
        "X": qstr(X),
        "a": qstr(a),
        "W": view.W,
        "deg_p": view.u,
        "deg_q": degree_q,
        "normalization": f"p_{view.u}=q_{degree_q}=1",
        "identity": "a*q*p_z - X*p*q_z - (v_s-u_s)*p^(W+1) = 0",
        "coefficient_equations": {
            "range": f"r=0,...,{(view.W + 1) * view.u}",
            "equation": (
                "a*sum_{i+j-1=r} i*p_i*q_j "
                "- X*sum_{i+j-1=r} j*p_i*q_j "
                "- (v_s-u_s)*sum_{i_0+...+i_W=r} prod_h p_(i_h) = 0"
            ),
            "top_coefficient": f"({top})*(q_{degree_q}-1)=0",
        },
    }


def screen_view(view: SkeletonView) -> dict[str, Any]:
    """Return every raw chart, every exact kill certificate, and survivors."""
    orders = radius_window(view.u, view.v)
    split_parts = genuine_partitions(view.u)
    charts: list[dict[str, Any]] = []
    survivors: list[dict[str, Any]] = []
    killed: list[dict[str, Any]] = []
    for rho in orders:
        face = face_parameters(view, rho)
        for part in split_parts:
            G = galois_condition(part, rho, view.u)
            L = local_exponent_condition(part, rho, view.u, view.v, view.W)
            XU = xu_corollary_7_5(part, rho, view.u, view.v)
            killed_by = [name for name, failed in (("G", not G["passes"]), ("L", not L["passes"])) if failed]
            # Xu is recorded as an independent source certificate.  L implies
            # this particular exclusion, so it does not define an extra screen.
            entry = {
                "rho": qstr(rho),
                "partition": list(part),
                "face": face,
                "G": G,
                "L": L,
                "Xu75": XU,
                "status": "KILLED" if killed_by else "SURVIVES_NECESSARY_SCREEN",
                "killed_by": killed_by,
            }
            charts.append(entry)
            compact = {
                "rho": qstr(rho),
                "partition": list(part),
                "Q": rho.denominator,
                "t": L["t"],
                "k": L["k"],
            }
            if killed_by:
                compact["killed_by"] = killed_by
                compact["certificate"] = {
                    "G": None if G["passes"] else {
                        "coefficient_identity": G["coefficient_identity"],
                        "failed_zero_choices": G["failed_zero_choices"],
                    },
                    "L": None if L["passes"] else {
                        "minimum_sum_nu": L["minimum_sum_nu"],
                        "deg_q": L["deg_q"],
                        "cancelled_inequality": L["cancelled_inequality"],
                    },
                    "Xu75_independent": XU["excludes"],
                }
                killed.append(compact)
            else:
                compact["galois_zero_choices"] = [
                    witness["zero_root_multiplicity"] for witness in G["orbit_witnesses"]
                ]
                compact["optimal_low_multiplicities"] = [
                    item["lambda"] for item in L["optimal_low_roots"]
                ]
                compact["forced_high_multiplicities"] = [
                    item["lambda"] for item in L["forced_high_roots"]
                ]
                survivors.append(compact)
    galois_pair_count = sum(galois_partition_count(view.u, order.denominator) for order in orders)
    xu_direct_count = sum(
        1
        for order in orders
        if order < Q(view.v + 1, view.u + 1)
        and full_distinct_is_galois_admissible(view.u, order.denominator)
    )
    return {
        "schema": "jc2.split-window/v1",
        "scope": "necessary screen; survival is not attainment or a joint-chart lift",
        "skeleton": {
            "n": view.n,
            "m": view.m,
            "s": view.s,
            "M": list(view.M),
            "d": list(view.d),
            "V": {str(i): view.V[i - 2] for i in range(2, view.s + 1)},
            "u_s": view.u,
            "v_s": view.v,
            "mu_s": view.mu_s,
            "W": view.W,
            "row_key": repr(view.row_key),
        },
        "finite_window": {
            "predicate": "rho=P/Q reduced, 1<rho<v_s/u_s, 1<=Q<=u_s",
            "orders": [qstr(order) for order in orders],
            "order_count": len(orders),
            "partition_count": len(split_parts),
            "raw_pair_count": len(orders) * len(split_parts),
            "size_formula": "N(u,v)*(p(u)-1)",
            "galois_admissible_pair_count": galois_pair_count,
            "galois_size_formula": (
                "sum_{rho=P/Q} A_Q(u), A_1(u)=p(u)-1, "
                "A_Q(u)=sum_{r=0}^{floor(u/Q)}p(r)-1 for Q>1"
            ),
            "xu_cor_7_5_direct_exclusions_after_G": xu_direct_count,
            "galois_and_xu_pair_count": galois_pair_count - xu_direct_count,
        },
        "survivor_count": len(survivors),
        "killed_count": len(killed),
        "survivors": survivors,
        "killed": killed,
        "charts": charts,
    }


def screen_skeleton(skeleton: Any) -> dict[str, Any]:
    """Validate ``skeleton`` and run the exact finite necessary screen."""
    return screen_view(skeleton_view(skeleton))


__all__ = [
    "SkeletonView",
    "face_parameters",
    "galois_condition",
    "galois_partition_count",
    "genuine_partitions",
    "local_exponent_condition",
    "full_distinct_is_galois_admissible",
    "partition_number",
    "partitions",
    "qstr",
    "radius_count_formula",
    "radius_window",
    "screen_skeleton",
    "screen_view",
    "skeleton_view",
    "xu_corollary_7_5",
]
