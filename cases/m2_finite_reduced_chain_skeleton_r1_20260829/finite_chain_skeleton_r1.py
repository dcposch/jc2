#!/usr/bin/env python3
"""Cap-free reduced-state closure for the BOOK-OFFAXIS P0 chain grammar.

This program implements only the chain fragment of P0 at fixed initial
``(w,M)`` and fixed numerical lambda budget.  It replaces the historical
global loop caps on ``k``, ``lex``, numerator, and ``M`` by bounds derived
from the printed P0 identities.  It does not enumerate merges and makes no
landing, realizability, degree-bound, or JC2 claim.

For a dirty step P0 gives

    C = l*(k+lex)-Sm >= 1,
    T = Sm+l-eps*(1+k+lex) >= 1,
    E = (l-eps)+nu*C,
    E | l*num(w)*T,                 nu >= 2.

If eps>0, T>=1 bounds lex directly.  If eps=0, T=Sm+l and
``(l+2*C) <= E <= l*num(w)*T`` bounds C and hence lex.  The number ``k`` of
NE p-orbits is at most the remaining lambda budget because each costs at
least one.  Pure-epsilon steps are the only dirty-looking family with free
nu; their reduced outputs and exact nu congruence classes are finite.
"""

from __future__ import annotations

import argparse
import hashlib
import heapq
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


SCHEMA = "m2-finite-reduced-chain-skeleton-r1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def divisors(n: int) -> list[int]:
    require(isinstance(n, int) and n >= 1, "divisors requires n>=1")
    low: list[int] = []
    high: list[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            low.append(d)
            if d * d != n:
                high.append(n // d)
        d += 1
    return low + list(reversed(high))


def ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def fraction_text(value: Fraction) -> str:
    return (str(value.numerator) if value.denominator == 1 else
            f"{value.numerator}/{value.denominator}")


def sha256_bytes(blob: bytes) -> str:
    return hashlib.sha256(blob).hexdigest()


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True).encode("ascii")


def min_ne_lambda(X: Fraction, kbar: Fraction, k: int, Sm: int,
                  max_mult: int) -> int | None:
    """Minimum P0 price over partitions Sm=m_1+...+m_k.

    Every m_j lies in [1,max_mult].  Returning None means no legal
    partition, including a nonpositive NE gap.
    """
    if k == 0:
        return 0 if Sm == 0 else None
    if max_mult < 1 or Sm < k or Sm > k * max_mult:
        return None
    best: int | None = None

    def visit(index: int, left: int, cost: int) -> None:
        nonlocal best
        if best is not None and cost >= best:
            return
        if index == k:
            if left == 0:
                best = cost if best is None else min(best, cost)
            return
        remaining_slots = k - index - 1
        for mult in range(1, max_mult + 1):
            after = left - mult
            if after < remaining_slots or after > remaining_slots * max_mult:
                continue
            gap = X / mult - kbar
            if gap <= 0:
                continue
            visit(index + 1, after,
                  cost + max(1, ceil_fraction(gap)))

    visit(0, Sm, 0)
    return best


@dataclass(frozen=True)
class Step:
    w: Fraction
    M: int
    cost: int
    family: str
    witness: tuple[tuple[str, object], ...]

    def key(self) -> tuple[Fraction, int, int, str, bytes]:
        return (self.w, self.M, self.cost, self.family,
                canonical(dict(self.witness)))

    def as_json(self) -> dict[str, object]:
        return {
            "w": fraction_text(self.w),
            "M": self.M,
            "lambda": self.cost,
            "family": self.family,
            "witness": dict(self.witness),
        }


def witness(**values: object) -> tuple[tuple[str, object], ...]:
    return tuple(sorted(values.items()))


def pure_epsilon_classes(w: Fraction, l: int, eps: int) -> dict[int, dict[str, object]]:
    """Exact possible M' and nu residue classes for a pure-(b) step.

    Put N=nu+1.  P0 requires d*(l-eps) | l*a*N, where w=a/d, and
    M'=gcd(l-eps,N).  Both conditions depend only on N modulo the lcm
    below.  Each accepted residue has a representative N>=3, hence nu>=2.
    """
    require(1 <= eps < l, "pure epsilon requires 1<=eps<l")
    E = l - eps
    divisor = w.denominator * E
    required_multiple = divisor // math.gcd(divisor, l * w.numerator)
    modulus = math.lcm(E, required_multiple)
    by_M: dict[int, list[int]] = {}
    for residue in range(modulus):
        if residue % required_multiple != 0:
            continue
        M2 = math.gcd(E, residue)
        by_M.setdefault(M2, []).append(residue)
    require(bool(by_M), "pure epsilon congruence census is empty")
    return {
        M2: {"nu_plus_one_modulus": modulus,
             "nu_plus_one_residues": residues}
        for M2, residues in sorted(by_M.items())
    }


def dirty_lex_bound(w: Fraction, l: int, eps: int, k: int, Sm: int) -> int:
    """Largest lex not excluded by P0's proved inequalities; -1 if none."""
    require(0 <= eps < l and k >= 0 and Sm >= 0, "bad dirty parameters")
    if eps > 0:
        numerator = Sm + l - eps * (1 + k) - 1
        return numerator // eps if numerator >= 0 else -1
    T = Sm + l
    Cmax = (l * w.numerator * T - l) // 2
    if Cmax < 1:
        return -1
    return (Cmax + Sm) // l - k


def one_step(w: Fraction, M: int, budget_remaining: int) -> list[Step]:
    """Complete reduced P0 one-step menu at the charged remaining budget."""
    require(w > 0 and M >= 1 and budget_remaining >= 0, "bad state")
    out: dict[tuple[object, ...], Step] = {}

    def add(step: Step) -> None:
        require(step.w > 0 and step.M >= 1 and step.cost >= 0,
                "invalid emitted step")
        if step.cost <= budget_remaining:
            out[step.key()] = step

    # Clean resonance: Delta=(n-1)*nu+1 divides num(w), Delta>=3.
    for Delta in divisors(w.numerator):
        if Delta < 3:
            continue
        for nu in range(2, Delta):
            if (Delta - 1) % nu:
                continue
            n = (Delta - 1) // nu + 1
            if n < 2:
                continue
            dq = n * nu + 1
            if dq % w.denominator:
                continue
            for l in divisors(M):
                add(Step(w * Fraction(n, Delta), math.gcd(l, dq), 0,
                         "clean-resonant",
                         witness(l=l, Delta=Delta, n=n, nu=nu,
                                 dp=l * nu, dq=dq)))

    # Neutral n=1: every divisor of M occurs as gcd(l,nu+1) for some
    # l|M and a congruence class of nu; reduced w is unchanged.
    for M2 in divisors(M):
        add(Step(w, M2, 0, "clean-neutral",
                 witness(M_parent=M, M_child=M2,
                         existence="nu-plus-one gcd class")))

    for l in divisors(M):
        if l < 2:
            continue

        # Pure epsilon: nu is free, but reduced outputs and congruence
        # classes are finite and computed exactly rather than guessed.
        for eps in range(1, l):
            E = l - eps
            cost = ceil_fraction(Fraction(l, eps) * w)
            if cost > budget_remaining:
                continue
            for M2, congruence in pure_epsilon_classes(w, l, eps).items():
                add(Step(Fraction(l, E) * w, M2, cost, "pure-epsilon",
                         witness(l=l, eps=eps, E=E, **congruence)))

        # Dirty P0 families.  k is budget-bounded because each of its NE
        # p-orbits costs at least one; an epsilon root costs another unit.
        for eps in range(0, l):
            kmax = budget_remaining - (1 if eps else 0)
            if kmax < 0:
                continue
            for k in range(kmax + 1):
                if eps == 0 and k == 0:
                    continue  # exactly the clean family handled above
                for Sm in range(k, k * (l - 1) + 1):
                    lexmax = dirty_lex_bound(w, l, eps, k, Sm)
                    for lex in range(max(-1, lexmax) + 1):
                        C = l * (k + lex) - Sm
                        if C <= 0:
                            continue
                        T = Sm + l - eps * (1 + k + lex)
                        if T <= 0:
                            continue
                        dividend = l * w.numerator * T
                        for E in divisors(dividend):
                            numerator = E - (l - eps)
                            if numerator < 2 * C or numerator % C:
                                continue
                            nu = numerator // C
                            dq = (1 + k + lex) * nu + 1
                            dp = eps + nu * (l + Sm)
                            require(l * dq - dp == E,
                                    "P0 E reconstruction failed")
                            kbar = Fraction(l, 1) * w * dq / E
                            if kbar.denominator != 1 or kbar < 1:
                                continue
                            if eps and eps * dq >= dp:
                                continue
                            X = kbar * Fraction(dp, dq)
                            max_mult = min(l - 1, (dp - 1) // dq) if k else 0
                            price = min_ne_lambda(X, kbar, k, Sm, max_mult)
                            if price is None:
                                continue
                            if eps:
                                gap0 = (X / eps - kbar) / nu
                                if gap0 <= 0:
                                    continue
                                price += max(1, ceil_fraction(gap0))
                            if price > budget_remaining:
                                continue
                            w2 = Fraction(l, 1) * w * (dq - 1) / (nu * E)
                            M2 = math.gcd(dp, dq)
                            require(M2 == math.gcd(E, dq),
                                    "M-child/E identity failed")
                            add(Step(w2, M2, price, "dirty",
                                     witness(l=l, eps=eps, k=k, Sm=Sm,
                                             lex=lex, C=C, T=T, E=E,
                                             nu=nu, dp=dp, dq=dq,
                                             kbar=int(kbar), X=fraction_text(X),
                                             derived_lex_bound=lexmax)))

    return sorted(out.values(), key=lambda s:
                  (s.cost, s.w, s.M, s.family, s.witness))


def close_reduced_skeleton(w0: Fraction, M0: int, budget: int) -> dict[str, object]:
    """Dijkstra closure; no numerical search cap occurs anywhere."""
    require(w0 > 0 and M0 >= 1 and budget >= 0, "bad closure input")
    distance: dict[tuple[Fraction, int], int] = {}
    predecessor: dict[tuple[Fraction, int], dict[str, object]] = {}
    queue: list[tuple[int, Fraction, int]] = [(0, w0, M0)]
    menus: dict[tuple[Fraction, int, int], list[Step]] = {}
    expanded_edges = 0
    max_k = max_lex = max_derived_lex = 0

    while queue:
        spent, w, M = heapq.heappop(queue)
        key = (w, M)
        if key in distance and distance[key] <= spent:
            continue
        distance[key] = spent
        remaining = budget - spent
        menu = one_step(w, M, remaining)
        menus[(w, M, remaining)] = menu
        for step in menu:
            expanded_edges += 1
            if step.family == "dirty":
                data = dict(step.witness)
                max_k = max(max_k, int(data["k"]))
                max_lex = max(max_lex, int(data["lex"]))
                max_derived_lex = max(max_derived_lex,
                                      int(data["derived_lex_bound"]))
            child = (step.w, step.M)
            child_spent = spent + step.cost
            if child not in distance or child_spent < distance[child]:
                heapq.heappush(queue, (child_spent, step.w, step.M))
                predecessor.setdefault(child, {
                    "parent": {"w": fraction_text(w), "M": M,
                               "lambda": spent},
                    "step": step.as_json(),
                })

    states = [
        {"w": fraction_text(w), "M": M, "lambda_min": spent}
        for (w, M), spent in sorted(distance.items(),
                                    key=lambda item: (item[1], item[0][0],
                                                      item[0][1]))
    ]
    zero_cost_graph = {
        (w, M): {(s.w, s.M) for s in menus[(w, M, budget - spent)]
                 if s.cost == 0}
        for (w, M), spent in distance.items()
    }
    zero_cost_nonincrease = all(
        child_w <= parent_w and child_M <= parent_M
        for (parent_w, parent_M), children in zero_cost_graph.items()
        for child_w, child_M in children)
    require(zero_cost_nonincrease,
            "a zero-cost transition increased reduced w or M")

    payload: dict[str, object] = {
        "schema": SCHEMA,
        "scope": "BOOK-OFFAXIS P0 REDUCED CHAIN STATES ONLY",
        "input": {"w": fraction_text(w0), "M": M0,
                  "lambda_budget": budget},
        "cap_free": True,
        "hard_loop_caps": [],
        "proof_obligations_used": [
            "P0 clean resonance Delta divides num(w)",
            "P0 dirty E divides l*num(w)*T",
            "P0 T positive and nu at least 2 derive lex bounds",
            "each NE p-orbit and epsilon root costs at least one lambda",
            "pure-epsilon free-nu family reduced by exact congruence classes",
        ],
        "state_count": len(states),
        "expanded_edge_count": expanded_edges,
        "max_reduced_w_numerator": max(w.numerator for w, _ in distance),
        "max_M": max(M for _, M in distance),
        "max_k_observed": max_k,
        "max_lex_observed": max_lex,
        "max_derived_lex_bound": max_derived_lex,
        "zero_cost_reduced_nonincrease": zero_cost_nonincrease,
        "states": states,
        "first_predecessor": {
            f"{fraction_text(w)}|{M}": value
            for (w, M), value in sorted(predecessor.items())
        },
        "firewall": {
            "merges_enumerated": False,
            "full_configuration_landing": False,
            "realizability": False,
            "degree_bound": False,
            "jc2": False,
        },
    }
    payload["state_table_sha256"] = sha256_bytes(canonical(states))
    return payload


def parse_fraction(text: str) -> Fraction:
    try:
        value = Fraction(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc
    if value <= 0:
        raise argparse.ArgumentTypeError("w must be positive")
    return value


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--w", type=parse_fraction, default=Fraction(3, 2))
    parser.add_argument("--M", type=int, default=2)
    parser.add_argument("--budget", type=int, default=5)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(list(argv) if argv is not None else None)
    payload = close_reduced_skeleton(args.w, args.M, args.budget)
    blob = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(blob, end="")
    else:
        args.output.write_text(blob)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
