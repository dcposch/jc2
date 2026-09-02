#!/usr/bin/env python3
"""bmfact964_enum.py

Postprocessor for the (9,6,4) braid-monodromy job.

Pure Python 3 (no Sage required). Consumes the JSON written by
bmfact_964.sage. The REP-96 §5 (9,6,4) class list is HARD-CODED as a
CONTROL ONLY (three classes, 72 tuples after S_4-conjugacy, including
the const-4c class with Pi a 4-cycle).

DECISION PATH: the full native transposition universe 6^9 in Sage
strand order, with pruning after each local relation, certified
against the unpruned count on a deterministic subsample. Both
orientations. NO manual strand map (no adjacent-block / tubular
identification) in the decision path.

  CONTROL (a) expand the three charged (X, Y, T_1) classes to 72 tuples;
  CONTROL (b) reconstruct nine-tuples in the adjacent-block reading
      T = (T_1, T_2, T_3) with iota = (delta_3^{k_*}, 1, 1), k_* = -8;
      this reconstruction is NEVER the decision;
  POSITIVE CONTROL: drop every local ZvK relation except the product
      relation. Generating count must equal 72;
  NEGATIVE CONTROL: extra projective relation xi_1 ... xi_9 = 1.
      Count must equal 0 (every charged Pi is odd: transposition or
      4-cycle);
  DECISION: prune 6^9 against every local braid (Sage Tietze, both
      orientations). Output one of
        SURVIVOR                  (full meridian 9-tuple verbatim)
        NATIVE_ZERO_CURVE_ONLY    (this curve, this reading)
        OPEN(census mismatch)
        OPEN(API mismatch)
      Never a row-level kill.

Charged class list: REP-96-INNER §5, frozen
  SHA-256 a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401
Hostile review (class list exact 3/72): rep-96-hostile-review-grok46.

Hurwitz convention (REP-96 §2, PI1-S4-DECISION §2, left action):
  sigma_i · (..., t_i, t_{i+1}, ...)
    = (..., t_i t_{i+1} t_i^{-1}, t_i, ...)
  sigma_i^{-1} · (..., t_i, t_{i+1}, ...)
    = (..., t_{i+1}, t_{i+1}^{-1} t_i t_{i+1}, ...)
Transpositions are involutions, so t^{-1} = t.

Sage Tietze (fetched Sage 10.8 braid docs):
  BraidGroup(9)([1, 2, -1]) = s0 * s1 * s0^{-1}.
  Tietze entry k > 0 is generator s_{k-1} (strands k and k+1, 1-based).
  Left action of a product applies the RIGHTMOST letter first.

Do not name variables pi, gamma, I, or O.

Usage:
  python3 bmfact964_enum.py --selftest
  python3 bmfact964_enum.py --curve-check
  python3 bmfact964_enum.py path/to/bmfact_964.json
"""
from __future__ import annotations

import argparse
import json
import sys
from itertools import permutations, product as iproduct
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple


# ---------------------------------------------------------------------------
# S_4. Transpositions as 2-element frozensets of {1,2,3,4}.
# Permutations as 4-tuples: image of (1,2,3,4).
# ---------------------------------------------------------------------------

LETTER_SET = (1, 2, 3, 4)
PERM_IDENTITY = (1, 2, 3, 4)
TRANSPOSITIONS: List[frozenset] = [
    frozenset([1, 2]),
    frozenset([1, 3]),
    frozenset([1, 4]),
    frozenset([2, 3]),
    frozenset([2, 4]),
    frozenset([3, 4]),
]
assert len(TRANSPOSITIONS) == 6
N_STRANDS = 9
N_ARTIN = 8
KSTAR = -8  # REP-96 §1 / §2: k_* = 2d - a - beta_1 = 15 - 23 = -8
CHARGED_CLASS_LIST_SHA256 = (
    "a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401"
)
EXPECTED_GENERATING = 72
SUBSAMPLE_MOD = 1021  # prime; 6^9 // 1021 ~= 9870 tuples

# Double transpositions = V_4 \ {e}.
V4_NONID = (
    frozenset([frozenset([1, 2]), frozenset([3, 4])]),  # marker only; see DT_PERMS
)


def transposition_to_perm(support: frozenset) -> Tuple[int, int, int, int]:
    if len(support) != 2:
        raise AssertionError("transposition_to_perm: %r is not a 2-set" % (support,))
    a, b = tuple(support)
    images = [1, 2, 3, 4]
    images[a - 1] = b
    images[b - 1] = a
    return (images[0], images[1], images[2], images[3])


def compose_perm(
    first: Tuple[int, int, int, int],
    second: Tuple[int, int, int, int],
) -> Tuple[int, int, int, int]:
    """(first o second)(x) = first(second(x)). Apply second first."""
    return (
        first[second[0] - 1],
        first[second[1] - 1],
        first[second[2] - 1],
        first[second[3] - 1],
    )


def invert_perm(perm: Tuple[int, int, int, int]) -> Tuple[int, int, int, int]:
    images = [0, 0, 0, 0]
    images[perm[0] - 1] = 1
    images[perm[1] - 1] = 2
    images[perm[2] - 1] = 3
    images[perm[3] - 1] = 4
    return (images[0], images[1], images[2], images[3])


def apply_perm_to_transposition(
    perm: Tuple[int, int, int, int],
    support: frozenset,
) -> frozenset:
    a, b = tuple(support)
    return frozenset([perm[a - 1], perm[b - 1]])


def cycle_perm(*pts: int) -> Tuple[int, int, int, int]:
    images = [1, 2, 3, 4]
    seq = list(pts)
    for idx, letter in enumerate(seq):
        images[letter - 1] = seq[(idx + 1) % len(seq)]
    return (images[0], images[1], images[2], images[3])


def fmt_perm(perm: Tuple[int, int, int, int]) -> str:
    seen = [False] * 5
    cycles: List[str] = []
    for start in range(1, 5):
        if seen[start]:
            continue
        cursor = start
        cyc: List[int] = []
        while not seen[cursor]:
            seen[cursor] = True
            cyc.append(cursor)
            cursor = perm[cursor - 1]
        if len(cyc) > 1:
            cycles.append("(" + " ".join(str(v) for v in cyc) + ")")
    return "".join(cycles) if cycles else "e"


def fmt_transp(support: frozenset) -> str:
    a, b = sorted(support)
    return "(%d %d)" % (a, b)


def fmt_tuple(tuple_t: Sequence[frozenset]) -> str:
    return "(" + ", ".join(fmt_transp(s) for s in tuple_t) + ")"


def perm_from_cycles_string_not_used() -> None:
    return None


DT_PERMS = (
    compose_perm(transposition_to_perm(frozenset([1, 2])),
                 transposition_to_perm(frozenset([3, 4]))),
    compose_perm(transposition_to_perm(frozenset([1, 3])),
                 transposition_to_perm(frozenset([2, 4]))),
    compose_perm(transposition_to_perm(frozenset([1, 4])),
                 transposition_to_perm(frozenset([2, 3]))),
)
V4_PERMS = (PERM_IDENTITY,) + DT_PERMS


def is_transposition_perm(perm: Tuple[int, int, int, int]) -> bool:
    moved = [idx for idx in range(1, 5) if perm[idx - 1] != idx]
    return len(moved) == 2 and perm[moved[0] - 1] == moved[1] and perm[moved[1] - 1] == moved[0]


def transpositions_commute(left: frozenset, right: frozenset) -> bool:
    return (left == right) or left.isdisjoint(right)


def tuple_generates_s4(tuple_t: Sequence[frozenset]) -> bool:
    """Transpositions generate S_4 iff the graph on {1,2,3,4} is connected."""
    parent = {1: 1, 2: 2, 3: 3, 4: 4}

    def find(letter: int) -> int:
        walk = letter
        while parent[walk] != walk:
            walk = parent[walk]
        compress = letter
        while parent[compress] != walk:
            nxt = parent[compress]
            parent[compress] = walk
            compress = nxt
        return walk

    def union(a: int, b: int) -> None:
        ra = find(a)
        rb = find(b)
        if ra != rb:
            parent[ra] = rb

    for support in tuple_t:
        a, b = tuple(support)
        union(a, b)
    roots = set(find(letter) for letter in LETTER_SET)
    return len(roots) == 1


def product_of_transpositions(tuple_t: Sequence[frozenset]) -> Tuple[int, int, int, int]:
    """Product t1 t2 ... tk, applying tk first."""
    acc = PERM_IDENTITY
    index = len(tuple_t) - 1
    while index >= 0:
        acc = compose_perm(transposition_to_perm(tuple_t[index]), acc)
        index -= 1
    # Wait: t1 t2 ... tk applying tk first means acc = t1 o t2 o ... o tk.
    # Starting from identity and composing on the left going right-to-left:
    # start acc=id; for k, k-1, ..., 1: acc = t_i o acc. Yes.
    return acc


def product_of_transpositions_left_to_right(tuple_t: Sequence[frozenset]) -> Tuple[int, int, int, int]:
    """Rebuild: apply last first."""
    acc = PERM_IDENTITY
    for support in reversed(tuple_t):
        acc = compose_perm(transposition_to_perm(support), acc)
    return acc


# ---------------------------------------------------------------------------
# Hurwitz action of B_9 on 9-tuples of transpositions.
# ---------------------------------------------------------------------------

def hurwitz_one_generator(
    tuple_t: Sequence[frozenset],
    tietze_letter: int,
) -> Tuple[frozenset, ...]:
    if tietze_letter == 0:
        raise AssertionError("hurwitz_one_generator: Tietze letter 0")
    gen_abs = abs(tietze_letter)
    if gen_abs < 1 or gen_abs > N_ARTIN:
        raise AssertionError(
            "hurwitz_one_generator: |Tietze letter| = %d outside 1..8 for B_9"
            % gen_abs
        )
    pos = gen_abs - 1
    out = list(tuple_t)
    left_entry = out[pos]
    right_entry = out[pos + 1]
    if tietze_letter > 0:
        conjugated = apply_perm_to_transposition(
            transposition_to_perm(left_entry), right_entry
        )
        out[pos] = conjugated
        out[pos + 1] = left_entry
    else:
        conjugated = apply_perm_to_transposition(
            transposition_to_perm(right_entry), left_entry
        )
        out[pos] = right_entry
        out[pos + 1] = conjugated
    return tuple(out)


def hurwitz_tietze(
    tuple_t: Sequence[frozenset],
    tietze_word: Sequence[int],
) -> Tuple[frozenset, ...]:
    """Left action of a Sage Tietze word: apply RIGHTMOST letter first."""
    current = tuple(tuple_t)
    index = len(tietze_word) - 1
    while index >= 0:
        current = hurwitz_one_generator(current, tietze_word[index])
        index -= 1
    return current


def is_fixed_by_tietze(tuple_t: Sequence[frozenset], tietze_word: Sequence[int]) -> bool:
    return hurwitz_tietze(tuple_t, tietze_word) == tuple(tuple_t)


def inverse_tietze(tietze_word: Sequence[int]) -> List[int]:
    return [-letter for letter in reversed(tietze_word)]


def concatenate_tietzes(words: Sequence[Sequence[int]]) -> List[int]:
    out: List[int] = []
    for word in words:
        out.extend(word)
    return out


# ---------------------------------------------------------------------------
# B_3 Hurwitz on a 3-tuple (one tube). delta_3 = sigma_1 sigma_2.
# ---------------------------------------------------------------------------

def hurwitz_sigma_on_triple(
    triple: Sequence[frozenset],
    pos: int,
    inverse: bool,
) -> Tuple[frozenset, ...]:
    out = list(triple)
    left_entry = out[pos]
    right_entry = out[pos + 1]
    if not inverse:
        conjugated = apply_perm_to_transposition(
            transposition_to_perm(left_entry), right_entry
        )
        out[pos] = conjugated
        out[pos + 1] = left_entry
    else:
        conjugated = apply_perm_to_transposition(
            transposition_to_perm(right_entry), left_entry
        )
        out[pos] = right_entry
        out[pos + 1] = conjugated
    return tuple(out)


def delta3_power(triple: Sequence[frozenset], power: int) -> Tuple[frozenset, ...]:
    """delta_3 = sigma_1 sigma_2. Left action: apply sigma_2 first, then sigma_1."""
    current = tuple(triple)
    if power >= 0:
        count = 0
        while count < power:
            current = hurwitz_sigma_on_triple(current, 1, False)
            current = hurwitz_sigma_on_triple(current, 0, False)
            count += 1
        return current
    count = 0
    while count < -power:
        current = hurwitz_sigma_on_triple(current, 0, True)
        current = hurwitz_sigma_on_triple(current, 1, True)
        count += 1
    return current


def entrywise_conj_triple(
    perm: Tuple[int, int, int, int],
    triple: Sequence[frozenset],
) -> Tuple[frozenset, ...]:
    return tuple(apply_perm_to_transposition(perm, t) for t in triple)


def h_of(perm_x: Tuple[int, int, int, int], perm_y: Tuple[int, int, int, int]) -> Tuple[int, int, int, int]:
    """h = Y X^2 Y (REP-96 §3)."""
    x_sq = compose_perm(perm_x, perm_x)
    return compose_perm(perm_y, compose_perm(x_sq, perm_y))


def gate3_holds(
    t1: Sequence[frozenset],
    perm_x: Tuple[int, int, int, int],
    perm_y: Tuple[int, int, int, int],
    kstar: int,
) -> bool:
    """T_1 = delta_3^{k_*} . c_h(T_1)."""
    h_elt = h_of(perm_x, perm_y)
    rhs = delta3_power(entrywise_conj_triple(h_elt, t1), kstar)
    return tuple(t1) == rhs


# ---------------------------------------------------------------------------
# REP-96 §5 class list for Delta=(9,6,4), HARD-CODED. CONTROL ONLY.
# ---------------------------------------------------------------------------
# Delta = (9,6,4)  (3 classes, each a 24-element conjugacy orbit; 72 tuples)
#   noncst-T :  X=(34) Y=(23) Pi=(24) ,
#               T_1 = ((13),(14),(13))  or  ((14),(13),(14))
#   const-4c :  X=Y=(1234) , Pi=(1432) , T_1 = ((34),(14),(12))
# The noncst-4c stratum is dead at k_*=-8 ≡ 0 (mod 4).

def fs(a: int, b: int) -> frozenset:
    return frozenset([a, b])


CLASS_REPS: List[Dict[str, object]] = [
    {
        "name": "noncst-T-a",
        "stratum": "noncst-T",
        "X": transposition_to_perm(fs(3, 4)),
        "Y": transposition_to_perm(fs(2, 3)),
        "Pi": transposition_to_perm(fs(2, 4)),
        "T1": (fs(1, 3), fs(1, 4), fs(1, 3)),
    },
    {
        "name": "noncst-T-b",
        "stratum": "noncst-T",
        "X": transposition_to_perm(fs(3, 4)),
        "Y": transposition_to_perm(fs(2, 3)),
        "Pi": transposition_to_perm(fs(2, 4)),
        "T1": (fs(1, 4), fs(1, 3), fs(1, 4)),
    },
    {
        "name": "const-4c",
        "stratum": "const-4c",
        "X": cycle_perm(1, 2, 3, 4),
        "Y": cycle_perm(1, 2, 3, 4),
        "Pi": cycle_perm(1, 4, 3, 2),
        "T1": (fs(3, 4), fs(1, 4), fs(1, 2)),
    },
]


S4_ELEMENTS: List[Tuple[int, int, int, int]] = [
    tuple(p) for p in permutations(range(1, 5))  # type: ignore[misc]
]
assert len(S4_ELEMENTS) == 24


def conjugate_class_rep(rep: Dict[str, object], g_elt: Tuple[int, int, int, int]) -> Dict[str, object]:
    perm_x = conjugate_perm(g_elt, rep["X"])  # type: ignore[arg-type]
    perm_y = conjugate_perm(g_elt, rep["Y"])  # type: ignore[arg-type]
    perm_pi = conjugate_perm(g_elt, rep["Pi"])  # type: ignore[arg-type]
    t1 = tuple(
        apply_perm_to_transposition(g_elt, s) for s in rep["T1"]  # type: ignore[union-attr]
    )
    return {
        "name": rep["name"],
        "stratum": rep["stratum"],
        "X": perm_x,
        "Y": perm_y,
        "Pi": perm_pi,
        "T1": t1,
        "conjugator": g_elt,
    }


def conjugate_perm(
    g_elt: Tuple[int, int, int, int],
    perm: Tuple[int, int, int, int],
) -> Tuple[int, int, int, int]:
    return compose_perm(g_elt, compose_perm(perm, invert_perm(g_elt)))


def expand_72() -> List[Dict[str, object]]:
    """S_4-conjugacy expansion of the three charged classes. CONTROL ONLY."""
    out: List[Dict[str, object]] = []
    seen: Set[Tuple] = set()
    for rep in CLASS_REPS:
        for g_elt in S4_ELEMENTS:
            item = conjugate_class_rep(rep, g_elt)
            key = (item["X"], item["Y"], item["T1"])
            if key in seen:
                raise AssertionError(
                    "expand_72: collision inside class %s" % rep["name"]
                )
            seen.add(key)
            out.append(item)
    if len(out) != EXPECTED_GENERATING:
        raise AssertionError(
            "expand_72: got %d, expected %d" % (len(out), EXPECTED_GENERATING)
        )
    return out


def reconstruct_nine(
    item: Dict[str, object],
    kstar: int = KSTAR,
) -> Tuple[frozenset, ...]:
    """Fill T_2, T_3 from T_1 by iota = (delta_3^{k_*}, 1, 1).

    From CABLE-3 (REP-96 §3), with iota_1 = delta_3^{k_*}, iota_2 = iota_3 = 1:
      T_3 = iota_1 . T_1 = delta_3^{k_*} . T_1
      T_2 = (iota_3 iota_1) . c_{XY}(T_1) = delta_3^{k_*} . c_{XY}(T_1)
    OPEN[BMFACT-IOTA-SPLIT]: other splits of iota with the same ordered
    product are a variant; this split is the one declared here.
    Adjacent-block identification: strands 1..3 = T_1, 4..6 = T_2, 7..9 = T_3.
    OPEN[BMFACT-TUBE-EMBEDDING]: residue-mod-3 tubes are a second reading.
    """
    t1: Tuple[frozenset, ...] = item["T1"]  # type: ignore[assignment]
    perm_x: Tuple[int, int, int, int] = item["X"]  # type: ignore[assignment]
    perm_y: Tuple[int, int, int, int] = item["Y"]  # type: ignore[assignment]
    perm_xy = compose_perm(perm_x, perm_y)
    t3 = delta3_power(t1, kstar)
    t2 = delta3_power(entrywise_conj_triple(perm_xy, t1), kstar)
    return tuple(t1) + tuple(t2) + tuple(t3)


def allowed_tau(perm_pi: Tuple[int, int, int, int]) -> List[frozenset]:
    """Pi tau in V_4, tau a transposition: tau = Pi or tau disjoint from Pi."""
    out: List[frozenset] = []
    for tau in TRANSPOSITIONS:
        prod = compose_perm(perm_pi, transposition_to_perm(tau))
        if prod in V4_PERMS:
            out.append(tau)
    return out


def assert_pi_types(expanded: Sequence[Dict[str, object]]) -> Dict[str, object]:
    """ASSERTION, not a filter. Pi is odd on every class; 4-cycle on const-4c."""
    failures: List[str] = []
    n_transp = 0
    n_fourcycle = 0
    for item in expanded:
        perm_pi = item["Pi"]  # type: ignore[assignment]
        name = str(item["name"])
        stratum = str(item["stratum"])
        moved = [idx for idx in range(1, 5) if perm_pi[idx - 1] != idx]  # type: ignore[index]
        is_transp = is_transposition_perm(perm_pi)  # type: ignore[arg-type]
        is_four = len(moved) == 4 and not is_transp
        if is_transp:
            n_transp += 1
        if is_four:
            n_fourcycle += 1
        if stratum == "const-4c":
            if not is_four:
                failures.append(
                    "%s: expected Pi a 4-cycle, got %s"
                    % (name, fmt_perm(perm_pi))  # type: ignore[arg-type]
                )
        elif stratum == "noncst-T":
            if not is_transp:
                failures.append(
                    "%s: expected Pi a transposition, got %s"
                    % (name, fmt_perm(perm_pi))  # type: ignore[arg-type]
                )
        else:
            failures.append("%s: unexpected stratum %s" % (name, stratum))
        if perm_pi == PERM_IDENTITY:  # type: ignore[comparison-overlap]
            failures.append("%s: Pi is the identity (even)" % name)
    return {
        "passed": len(failures) == 0,
        "n_checked": len(expanded),
        "n_pi_transposition": n_transp,
        "n_pi_fourcycle": n_fourcycle,
        "failures": failures,
        "note": (
            "ASSERTION, not a filter. On (9,6,4) Pi is a transposition on "
            "the two noncst-T classes and a 4-cycle on const-4c; never in "
            "V_4. The (9,6,2) Pi-tau pin (two of six transpositions) is "
            "NOT applied to const-4c and is not a decision filter."
        ),
    }


def classify_nine_block(
    nine: Sequence[frozenset],
    expanded_index: Dict[Tuple, str],
) -> Optional[str]:
    """Identify a 9-tuple in adjacent-block order with a charged class name."""
    t1 = tuple(nine[0:3])
    t2 = tuple(nine[3:6])
    perm_x = product_of_transpositions_left_to_right(t1)
    perm_y = product_of_transpositions_left_to_right(t2)
    key = (perm_x, perm_y, t1)
    return expanded_index.get(key)


# ---------------------------------------------------------------------------
# CABLE-3 product action on adjacent-block 9-tuples, for the selftest.
# ---------------------------------------------------------------------------

def prod3_perm(triple: Sequence[frozenset]) -> Tuple[int, int, int, int]:
    return product_of_transpositions_left_to_right(triple)


def c3_delta3_blocks(
    blocks: Tuple[Tuple[frozenset, ...], Tuple[frozenset, ...], Tuple[frozenset, ...]],
) -> Tuple[Tuple[frozenset, ...], Tuple[frozenset, ...], Tuple[frozenset, ...]]:
    """C_3(delta_3) . (B1,B2,B3) = (c_{P1 P2}(B3), B1, B2)  (REP-96 (2.4))."""
    b1, b2, b3 = blocks
    perm_w = compose_perm(prod3_perm(b1), prod3_perm(b2))
    new_b1 = entrywise_conj_triple(perm_w, b3)
    return (tuple(new_b1), tuple(b1), tuple(b2))


def rho_inf_block_act(
    nine: Sequence[frozenset],
    kstar: int = KSTAR,
) -> Tuple[frozenset, ...]:
    """rho_inf = C_3(delta_3^2) · iota with iota = (delta_3^{k_*}, 1, 1)."""
    b1 = tuple(nine[0:3])
    b2 = tuple(nine[3:6])
    b3 = tuple(nine[6:9])
    s1 = delta3_power(b1, kstar)
    s2 = b2
    s3 = b3
    after = c3_delta3_blocks(c3_delta3_blocks((tuple(s1), tuple(s2), tuple(s3))))
    return after[0] + after[1] + after[2]


# ---------------------------------------------------------------------------
# Controls
# ---------------------------------------------------------------------------

def run_positive_control(nines: Sequence[Tuple[frozenset, ...]]) -> Dict[str, object]:
    """Drop every local relation except the product relation. Expect 72 generating."""
    n_fixed = 0
    n_generating = 0
    generating: List[Tuple[frozenset, ...]] = []
    for nine in nines:
        if rho_inf_block_act(nine, KSTAR) == tuple(nine):
            n_fixed += 1
            if tuple_generates_s4(nine):
                n_generating += 1
                generating.append(tuple(nine))
    passed = n_generating == EXPECTED_GENERATING
    return {
        "name": "POSITIVE_CONTROL_PRODUCT_ONLY",
        "description": (
            "Drop all local ZvK relations except rho_inf-fixedness, with "
            "rho_inf = C_3(delta_3^2) · (delta_3^{k_*}, 1, 1), k_* = -8, "
            "adjacent-block identification (CONTROL ONLY, not the decision). "
            "Count generating 9-tuples."
        ),
        "n_input": len(nines),
        "n_product_fixed": n_fixed,
        "n_generating": n_generating,
        "expected_generating": EXPECTED_GENERATING,
        "passed": passed,
        "citation": (
            "REP-96-INNER §5: 3 classes, each a 24-element conjugacy orbit; "
            "72 tuples in all. Frozen SHA-256 " + CHARGED_CLASS_LIST_SHA256
        ),
    }


def run_negative_control(nines: Sequence[Tuple[frozenset, ...]]) -> Dict[str, object]:
    """Extra projective relation xi_1 ... xi_9 = 1. Provably empties: Pi is odd."""
    n_hit = 0
    for nine in nines:
        if not tuple_generates_s4(nine):
            continue
        if rho_inf_block_act(nine, KSTAR) != tuple(nine):
            continue
        prod = product_of_transpositions_left_to_right(nine)
        if prod == PERM_IDENTITY:
            n_hit += 1
    passed = n_hit == 0
    return {
        "name": "NEGATIVE_CONTROL_PROJECTIVE",
        "description": (
            "Fake extra relation: the product of the nine meridians is 1 "
            "(the relation that presents pi_1(P^2 - Dbar), not pi_1(C^2 - D)). "
            "On every charged (9,6,4) class Pi is odd (a transposition or a "
            "4-cycle), so the extra relation empties the set."
        ),
        "n_generating_product_fixed_and_total_product_one": n_hit,
        "expected": 0,
        "passed": passed,
    }


def run_gate3_on_reps() -> Dict[str, object]:
    rows = []
    all_ok = True
    for rep in CLASS_REPS:
        ok = gate3_holds(rep["T1"], rep["X"], rep["Y"], KSTAR)  # type: ignore[arg-type]
        prod_t1 = product_of_transpositions_left_to_right(rep["T1"])  # type: ignore[arg-type]
        ok_prod = prod_t1 == rep["X"]
        rows.append(
            {
                "name": rep["name"],
                "gate3_at_kstar_%d" % KSTAR: ok,
                "T1_product_equals_X": ok_prod,
                "X": fmt_perm(rep["X"]),  # type: ignore[arg-type]
                "Y": fmt_perm(rep["Y"]),  # type: ignore[arg-type]
                "Pi": fmt_perm(rep["Pi"]),  # type: ignore[arg-type]
                "T1": fmt_tuple(rep["T1"]),  # type: ignore[arg-type]
            }
        )
        if not (ok and ok_prod):
            all_ok = False
    return {"passed": all_ok, "kstar": KSTAR, "reps": rows}


def brute_generating_product_fixed(kstar: int = KSTAR) -> Dict[str, object]:
    """All 6^9 transposition 9-tuples, adjacent-block CABLE-3 product relation.

    Lookup-table scan: 216^3. Used as an independent check that 72 is the
    complete generating count, not only the class-list reconstruction.
    """
    all_triples = list(iproduct(TRANSPOSITIONS, repeat=3))
    assert len(all_triples) == 216
    index_of = {triple: idx for idx, triple in enumerate(all_triples)}
    products = [prod3_perm(triple) for triple in all_triples]

    def dmap(power: int) -> List[int]:
        return [index_of[delta3_power(triple, power)] for triple in all_triples]

    map_iota = dmap(kstar)
    # C3_one(i,j,k) = (idx[c_{Pi Pj}(triple_k)], i, j)
    conj_table: List[List[List[int]]] = []
    # Too big if fully materialised as 216^3. Build a 216x216 map:
    # for each (i,j), the permutation of k.
    pair_map: List[List[List[int]]] = [[None] * 216 for _ in range(216)]  # type: ignore[list-item]
    for i in range(216):
        for j in range(216):
            perm_w = compose_perm(products[i], products[j])
            row = [index_of[entrywise_conj_triple(perm_w, all_triples[k])] for k in range(216)]
            pair_map[i][j] = row  # type: ignore[assignment]

    n_fixed = 0
    n_gen = 0
    for i in range(216):
        i1 = map_iota[i]
        for j in range(216):
            j1 = j  # iota_2 = 1
            for k in range(216):
                k1 = k  # iota_3 = 1
                # C3 twice
                a_idx = pair_map[i1][j1][k1]
                a, b, c = a_idx, i1, j1
                a2 = pair_map[a][b][c]
                a, b, c = a2, a, b
                if a == i and b == j and c == k:
                    n_fixed += 1
                    nine = all_triples[i] + all_triples[j] + all_triples[k]
                    if tuple_generates_s4(nine):
                        n_gen += 1
    return {
        "kstar": kstar,
        "iota": "(delta_3^{k_*}, 1, 1)",
        "n_product_fixed": n_fixed,
        "n_generating": n_gen,
        "expected_generating": EXPECTED_GENERATING,
        "passed": n_gen == EXPECTED_GENERATING,
    }


# ---------------------------------------------------------------------------
# Sage JSON path
# ---------------------------------------------------------------------------

def load_bundle(path: str) -> dict:
    with open(path, "r") as handle:
        first = handle.read(1)
        handle.seek(0)
        if first == "{":
            return json.load(handle)
        # JSONL: assemble a bundle.
        meta = None
        braids = []
        product = None
        census = None
        for line in handle:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            kind = rec.get("type")
            if kind == "meta":
                meta = rec
            elif kind == "braid":
                braids.append(rec)
            elif kind == "product":
                product = rec
            elif kind == "census":
                census = rec
        return {
            "braids": braids,
            "product": product,
            "census": census,
            **(meta or {}),
        }


def node_fibre_leftover_strand(braids: Sequence[dict]) -> Optional[int]:
    """1-based leftover strand of the unique node-fibre braid, if CPF splits it."""
    node_recs = [b for b in braids if str(b.get("census_class", "")).startswith("node_fibre")]
    if len(node_recs) != 1:
        return None
    rec = node_recs[0]
    pieces = rec.get("conjugate_positive_form") or []
    involved: Set[int] = set()
    for piece in pieces:
        alpha = piece.get("alpha_tietze") or []
        for letter in alpha:
            gen_abs = abs(int(letter))
            involved.add(gen_abs)
            involved.add(gen_abs + 1)
        # conjugators move the band; the support of tau = g sigma_i^2 g^{-1}
        # is the image of {i,i+1} under the conjugator's permutation. For the
        # leftover-strand computation we use the permutation of the whole
        # fibre braid: identity, so leftover is the unique unmoved strand
        # of the four pairs after conjugating. FLAG if conjugators present.
        conjugators = piece.get("conjugator_tietzes") or []
        if conjugators:
            # Apply conjugator permutation to {gen of alpha}.
            # permutation of a Tietze word, 1-based.
            images = list(range(1, N_STRANDS + 1))
            # product of conjugators, rightmost first
            flat: List[int] = []
            for conj in conjugators:
                flat.extend(conj)
            idx = len(flat) - 1
            while idx >= 0:
                letter = flat[idx]
                g = abs(int(letter))
                tmp = images[g - 1]
                images[g - 1] = images[g]
                images[g] = tmp
                idx -= 1
            # alpha support {a, a+1} mapped
            if alpha:
                a0 = abs(int(alpha[0]))
                involved.add(images[a0 - 1])
                involved.add(images[a0])
    leftover = [s for s in range(1, N_STRANDS + 1) if s not in involved]
    if len(leftover) == 1:
        return leftover[0]
    return None


def intersect_block_with_braids(
    nines_with_class: Sequence[Tuple[Tuple[frozenset, ...], str, Tuple[int, int, int, int]]],
    braids: Sequence[dict],
    invert: bool,
) -> Dict[str, object]:
    words = []
    for rec in braids:
        tietze = rec.get("tietze") or []
        if invert:
            tietze = inverse_tietze(tietze)
        words.append(list(tietze))
    per_class: Dict[str, int] = {rep["name"]: 0 for rep in CLASS_REPS}  # type: ignore[misc]
    survivors: List[dict] = []
    for nine, class_name, perm_pi in nines_with_class:
        ok = True
        for word in words:
            if not is_fixed_by_tietze(nine, word):
                ok = False
                break
        if not ok:
            continue
        if not tuple_generates_s4(nine):
            continue
        per_class[class_name] = per_class.get(class_name, 0) + 1
        survivors.append(
            {
                "class": class_name,
                "xi": [fmt_transp(s) for s in nine],
                "Pi": fmt_perm(perm_pi),
            }
        )
    total = sum(per_class.values())
    return {
        "variant": "BLOCK-inverse" if invert else "BLOCK",
        "per_class": per_class,
        "total_survivors": total,
        "survivors": survivors,
    }


# ---------------------------------------------------------------------------
# Native 6^9 universe, integer-encoded, prune after each relation.
# NO strand map. This is the decision path.
# ---------------------------------------------------------------------------

def _conj_table() -> List[List[int]]:
    table: List[List[int]] = [[0] * 6 for _ in range(6)]
    index_of = {support: idx for idx, support in enumerate(TRANSPOSITIONS)}
    for i, left in enumerate(TRANSPOSITIONS):
        perm_left = transposition_to_perm(left)
        for j, right in enumerate(TRANSPOSITIONS):
            conjugated = apply_perm_to_transposition(perm_left, right)
            table[i][j] = index_of[conjugated]
    return table


CONJ_TABLE: List[List[int]] = _conj_table()


def hurwitz_one_int(tup: Sequence[int], tietze_letter: int) -> Tuple[int, ...]:
    if tietze_letter == 0:
        raise AssertionError("hurwitz_one_int: Tietze letter 0")
    gen_abs = abs(tietze_letter)
    if gen_abs < 1 or gen_abs > N_ARTIN:
        raise AssertionError(
            "hurwitz_one_int: |Tietze letter| = %d outside 1..8" % gen_abs
        )
    pos = gen_abs - 1
    out = list(tup)
    left_entry = out[pos]
    right_entry = out[pos + 1]
    if tietze_letter > 0:
        out[pos] = CONJ_TABLE[left_entry][right_entry]
        out[pos + 1] = left_entry
    else:
        out[pos] = right_entry
        out[pos + 1] = CONJ_TABLE[right_entry][left_entry]
    return tuple(out)


def is_fixed_int(tup: Sequence[int], tietze_word: Sequence[int]) -> bool:
    current = tuple(tup)
    index = len(tietze_word) - 1
    while index >= 0:
        current = hurwitz_one_int(current, tietze_word[index])
        index -= 1
    return current == tuple(tup)


def generates_int(tup: Sequence[int]) -> bool:
    parent = {1: 1, 2: 2, 3: 3, 4: 4}

    def find(letter: int) -> int:
        walk = letter
        while parent[walk] != walk:
            walk = parent[walk]
        return walk

    for idx in tup:
        a, b = tuple(TRANSPOSITIONS[idx])
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    return len(set(find(letter) for letter in LETTER_SET)) == 1


def product_int(tup: Sequence[int]) -> Tuple[int, int, int, int]:
    acc = PERM_IDENTITY
    for idx in reversed(tup):
        acc = compose_perm(transposition_to_perm(TRANSPOSITIONS[idx]), acc)
    return acc


def combo_id(tup: Sequence[int]) -> int:
    acc = 0
    for val in tup:
        acc = 6 * acc + int(val)
    return acc


def int_tuple_to_transp(tup: Sequence[int]) -> Tuple[frozenset, ...]:
    return tuple(TRANSPOSITIONS[idx] for idx in tup)


def words_from_braids(braids: Sequence[dict], invert: bool, product_only: bool) -> List[List[int]]:
    if product_only:
        product_word: List[int] = []
        for rec in braids:
            product_word.extend(rec.get("tietze") or [])
        if invert:
            return [inverse_tietze(product_word)]
        return [product_word]
    words: List[List[int]] = []
    for rec in braids:
        tietze = list(rec.get("tietze") or [])
        if invert:
            tietze = inverse_tietze(tietze)
        words.append(tietze)
    return words


def prune_native(
    words: Sequence[Sequence[int]],
    subsample_mod: Optional[int] = None,
) -> Tuple[List[Tuple[int, ...]], List[Dict[str, object]]]:
    """Filter the native universe through each relation in order."""
    current: Optional[List[Tuple[int, ...]]] = None
    counts: List[Dict[str, object]] = []
    for word_index, word in enumerate(words):
        nxt: List[Tuple[int, ...]] = []
        if current is None:
            n_in = 0
            for combo in iproduct(range(6), repeat=N_STRANDS):
                if subsample_mod is not None and combo_id(combo) % subsample_mod != 0:
                    continue
                n_in += 1
                if is_fixed_int(combo, word):
                    nxt.append(combo)
        else:
            n_in = len(current)
            for combo in current:
                if is_fixed_int(combo, word):
                    nxt.append(combo)
        counts.append(
            {
                "word_index": int(word_index),
                "word_len": int(len(word)),
                "n_in": int(n_in),
                "n_out": int(len(nxt)),
            }
        )
        print(
            "PRUNE word %d len=%d n_in=%d n_out=%d"
            % (word_index, len(word), n_in, len(nxt))
        )
        sys.stdout.flush()
        current = nxt
    if current is None:
        current = []
    return current, counts


def unpruned_native(
    words: Sequence[Sequence[int]],
    subsample_mod: int,
) -> Tuple[List[Tuple[int, ...]], int]:
    """Check every subsample tuple against ALL words at once."""
    survivors: List[Tuple[int, ...]] = []
    n_seen = 0
    for combo in iproduct(range(6), repeat=N_STRANDS):
        if combo_id(combo) % subsample_mod != 0:
            continue
        n_seen += 1
        ok = True
        for word in words:
            if not is_fixed_int(combo, word):
                ok = False
                break
        if ok:
            survivors.append(combo)
    return survivors, n_seen


def certify_prune_against_unpruned(
    words: Sequence[Sequence[int]],
    subsample_mod: int = SUBSAMPLE_MOD,
) -> Dict[str, object]:
    """Pruned subsample survivor set must equal the unpruned subsample set."""
    pruned, prune_counts = prune_native(words, subsample_mod=subsample_mod)
    unpruned, n_seen = unpruned_native(words, subsample_mod)
    pruned_set = set(pruned)
    unpruned_set = set(unpruned)
    passed = pruned_set == unpruned_set
    return {
        "passed": passed,
        "subsample_mod": int(subsample_mod),
        "n_subsample_seen": int(n_seen),
        "n_pruned_survivors": int(len(pruned)),
        "n_unpruned_survivors": int(len(unpruned)),
        "n_symmetric_difference": int(len(pruned_set.symmetric_difference(unpruned_set))),
        "prune_counts": prune_counts,
    }


def summarise_native(
    survivors: Sequence[Tuple[int, ...]],
    prune_counts: Sequence[Dict[str, object]],
    invert: bool,
    product_only: bool,
) -> Dict[str, object]:
    n_fixed = len(survivors)
    gen_survivors = [tup for tup in survivors if generates_int(tup)]
    n_id_product = 0
    verbatim: List[List[str]] = []
    for tup in gen_survivors:
        if product_int(tup) == PERM_IDENTITY:
            n_id_product += 1
        verbatim.append([fmt_transp(TRANSPOSITIONS[idx]) for idx in tup])
    result: Dict[str, object] = {
        "variant": (
            ("SAGE-NATIVE-inverse" if invert else "SAGE-NATIVE")
            + ("-PRODUCT-ONLY" if product_only else "-FULL-ZVK")
        ),
        "n_fixed": int(n_fixed),
        "n_generating": int(len(gen_survivors)),
        "n_generating_with_total_product_one": int(n_id_product),
        "n_words": int(len(prune_counts)),
        "prune_counts": list(prune_counts),
        "decision_path": "native_transposition_universe_prune_after_each_relation",
        "strand_map": None,
    }
    if product_only:
        result["expected_generating"] = EXPECTED_GENERATING
        result["passed_positive_control"] = len(gen_survivors) == EXPECTED_GENERATING
        result["passed_negative_control"] = n_id_product == 0
    else:
        result["survivors_verbatim"] = verbatim
        result["total_survivors"] = int(len(gen_survivors))
    return result


def run_native_scan(
    braids: Sequence[dict],
    invert: bool,
    product_only: bool,
    certify_subsample: bool,
) -> Dict[str, object]:
    words = words_from_braids(braids, invert=invert, product_only=product_only)
    if not words:
        raise AssertionError("run_native_scan: no Tietze words")
    cert: Optional[Dict[str, object]] = None
    if certify_subsample:
        print(
            "CERTIFY prune vs unpruned on subsample mod=%d (%s) ..."
            % (SUBSAMPLE_MOD, "inverse" if invert else "as-written")
        )
        sys.stdout.flush()
        cert = certify_prune_against_unpruned(words, SUBSAMPLE_MOD)
        print(
            "CERTIFY passed=%s pruned=%s unpruned=%s"
            % (cert["passed"], cert["n_pruned_survivors"], cert["n_unpruned_survivors"])
        )
        sys.stdout.flush()
        if not cert["passed"]:
            raise AssertionError(
                "pruner disagrees with unpruned subsample: %s" % cert
            )
    print(
        "PRUNE full 6^9 (%s, %s) ..."
        % (
            "inverse" if invert else "as-written",
            "product-only" if product_only else "full-ZvK",
        )
    )
    sys.stdout.flush()
    survivors, counts = prune_native(words, subsample_mod=None)
    out = summarise_native(survivors, counts, invert=invert, product_only=product_only)
    if cert is not None:
        out["subsample_certification"] = cert
    return out


def synthetic_pruner_selftest() -> Dict[str, object]:
    """Two short words: sigma_1 then sigma_3^2. Prune vs unpruned on the subsample."""
    words = [[1], [3, 3]]
    cert = certify_prune_against_unpruned(words, SUBSAMPLE_MOD)
    return {"name": "SYNTHETIC_PRUNER", **cert}


def run_curve_check() -> Dict[str, object]:
    """Sympy replay of the (9,6,4) identity, resultant, discriminant census."""
    try:
        import sympy as sp
    except ImportError as err:
        return {"passed": False, "error": "sympy missing: %s" % err}

    t, x, y, z = sp.symbols("t x y z")
    poly_p = (
        t**9
        + 3 * t**7
        + sp.Rational(21, 4) * t**5
        + sp.Rational(35, 8) * t**3
        + sp.Rational(63, 32) * t
    )
    poly_q0 = t**6 + 2 * t**4 + sp.Rational(5, 2) * t**2
    poly_q = poly_q0 + sp.Rational(3, 4)
    ident = sp.expand(
        poly_p**2
        - poly_q0**3
        - sp.Rational(9, 4) * poly_q0**2
        - sp.Rational(27, 16) * poly_q0
        - sp.Rational(27, 64)
    )
    rhs = -sp.Rational(27, 1024) * (8 * t**4 + 13 * t**2 + 16)
    ident_ok = sp.expand(ident - rhs) == 0
    y3_minus_p2 = sp.factor(sp.expand(poly_q**3 - poly_p**2))
    gcd_pq = sp.gcd(sp.diff(poly_p, t), sp.diff(poly_q, t))

    f_raw = sp.resultant(poly_p - x, poly_q - y, t)
    f_poly = sp.Poly(sp.expand(f_raw), x, y, domain=sp.QQ)
    f_prim = sp.Poly(f_poly.as_expr() / f_poly.content(), x, y, domain=sp.QQ)
    w_expr = y**3 - x**2
    poly_a = 1024 * w_expr - 27 * (8 * z**2 + 13 * z + 16)
    poly_b = 4 * y - 3 - (4 * z**3 + 8 * z**2 + 10 * z)
    g_raw = sp.resultant(poly_a, poly_b, z)
    g_poly = sp.Poly(sp.expand(g_raw), x, y, domain=sp.QQ)
    g_prim = sp.Poly(g_poly.as_expr() / g_poly.content(), x, y, domain=sp.QQ)
    closed_ok = (f_prim == -g_prim) or (f_prim == g_prim)
    on_curve = sp.expand(f_prim.as_expr().subs({x: poly_p, y: poly_q})) == 0

    disc = sp.discriminant(sp.Poly(f_prim.as_expr(), y, domain=sp.QQ[x]))
    disc_poly = sp.Poly(sp.together(disc), x, domain=sp.QQ)
    sqf = sp.sqf_list(disc_poly.as_expr())
    omega = (
        42268920643584 * x**8
        + 32085100199936 * x**6
        + 7694037614592 * x**4
        + 614771555328 * x**2
        + 16209796869
    )
    node_quad = 134217728 * x**2 + 3087315
    factors = {str(fac): int(mult) for fac, mult in sqf[1]}
    census_ok = (
        disc_poly.degree() == 20
        and factors.get("x", 0) == 8
        and any("134217728" in key and mult == 2 for key, mult in factors.items())
        and any("42268920643584" in key and mult == 1 for key, mult in factors.items())
        and sp.gcd(omega, sp.diff(omega, x)) == 1
        and sp.gcd(omega, node_quad) == 1
    )
    tang = sp.resultant(poly_p - x, sp.diff(poly_p, t), t)
    tang_poly = sp.Poly(sp.expand(tang), x, domain=sp.QQ)
    tang_ok = tang_poly.degree() == 8 and sp.gcd(
        tang_poly.as_expr(), sp.diff(tang_poly.as_expr(), x)
    ) == 1

    passed = bool(
        ident_ok
        and gcd_pq == 1
        and f_poly.degree(x) == 6
        and f_poly.degree(y) == 9
        and f_poly.total_degree() == 9
        and f_poly.is_irreducible is True
        and closed_ok
        and on_curve
        and census_ok
        and tang_ok
    )
    return {
        "passed": passed,
        "identity_ok": bool(ident_ok),
        "identity_rhs": str(rhs),
        "y3_minus_p2": str(y3_minus_p2),
        "gcd_p_prime_q_prime": str(gcd_pq),
        "deg_x": int(f_poly.degree(x)),
        "deg_y": int(f_poly.degree(y)),
        "total_degree": int(f_poly.total_degree()),
        "irreducible": bool(f_poly.is_irreducible),
        "closed_form_matches_resultant": bool(closed_ok),
        "F_vanishes_on_parametrisation": bool(on_curve),
        "disc_degree": int(disc_poly.degree()),
        "disc_sqf": str(sqf),
        "tangency_degree": int(tang_poly.degree()),
        "census_ok": bool(census_ok),
        "tangency_squarefree": bool(tang_ok),
        "lc_y": str(sp.Poly(f_prim.as_expr(), y, domain=sp.QQ[x]).LC()),
    }


def decide_native(
    census_ok: Optional[bool],
    api_ok: bool,
    native_full: Optional[Dict[str, object]],
    native_full_inv: Optional[Dict[str, object]],
    native_prod: Optional[Dict[str, object]],
    native_prod_inv: Optional[Dict[str, object]],
) -> Tuple[str, str]:
    """Return (token, reason). Never a row-level kill."""
    if not api_ok:
        return "OPEN(API mismatch)", "Sage JSON missing braids, nstrands, or Tietze words"
    if census_ok is False:
        return (
            "OPEN(census mismatch)",
            "Sage census disagrees with 8 tangency + 1 four-node + 2 one-node, ledger 20",
        )
    if native_prod is None or native_prod_inv is None:
        return "OPEN(API mismatch)", "native product-only scan was not run"
    prod_fwd = int(native_prod.get("n_generating") or 0)
    prod_inv = int(native_prod_inv.get("n_generating") or 0)
    if prod_fwd != EXPECTED_GENERATING and prod_inv != EXPECTED_GENERATING:
        return (
            "OPEN(API mismatch)",
            "product-only generating count is %d (as-written) and %d (inverse), "
            "neither equals the charged 72" % (prod_fwd, prod_inv),
        )
    if native_full is None or native_full_inv is None:
        return "OPEN(API mismatch)", "native full-ZvK scan was not run"
    n_fwd = int(native_full.get("n_generating") or 0)
    n_inv = int(native_full_inv.get("n_generating") or 0)
    if n_fwd > 0:
        return (
            "SURVIVOR",
            "native as-written full ZvK has %d generating 9-tuple(s); "
            "listed verbatim under variant_SAGE_NATIVE_full.survivors_verbatim. "
            "This is a representation of pi_1(C^2-D) on this curve, not a "
            "Keller map and not FULL_ACTUAL_EXIT of the census row."
            % n_fwd,
        )
    if n_inv > 0:
        return (
            "SURVIVOR",
            "native inverse full ZvK has %d generating 9-tuple(s); "
            "listed verbatim under variant_SAGE_NATIVE_full_inverse.survivors_verbatim. "
            "Orientation reading OPEN[BMFACT-ORIENTATION] is live. "
            "This is a representation of pi_1(C^2-D) on this curve, not a "
            "Keller map and not FULL_ACTUAL_EXIT of the census row."
            % n_inv,
        )
    return (
        "NATIVE_ZERO_CURVE_ONLY",
        "native full ZvK generating count is 0 in both orientations, with "
        "product-only generating count matching 72 on at least one orientation. "
        "This decides the realized (9,6,4) curve only. It is not a row-level kill.",
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="ZvK enumeration for the realized (9,6,4) curve"
    )
    parser.add_argument(
        "json_path",
        nargs="?",
        default=None,
        help="JSON (or JSONL) produced by bmfact_964.sage",
    )
    parser.add_argument(
        "--selftest",
        action="store_true",
        help="class list + CABLE-3 controls + synthetic pruner; no Sage JSON",
    )
    parser.add_argument(
        "--curve-check",
        action="store_true",
        help="sympy identity / resultant / discriminant census (no Sage JSON)",
    )
    parser.add_argument(
        "--brute-block",
        action="store_true",
        help="scan all 6^9 adjacent-block tuples against CABLE-3 rho_inf (control only)",
    )
    parser.add_argument(
        "--skip-subsample-cert",
        action="store_true",
        help="skip prune-vs-unpruned subsample certification (debug only)",
    )
    parser.add_argument("--out", default=None, help="write JSON report to this path")
    return parser.parse_args(list(argv))


def _emit(report: dict, out_path: Optional[str]) -> None:
    text = json.dumps(report, indent=2, sort_keys=False)
    if out_path:
        with open(out_path, "w") as handle:
            handle.write(text)
            handle.write("\n")
        print("WROTE %s" % out_path)
    print(text)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    report: Dict[str, object] = {
        "script": "bmfact964_enum.py",
        "kstar": KSTAR,
        "n_classes_hardcoded": len(CLASS_REPS),
        "charged_class_list_sha256": CHARGED_CLASS_LIST_SHA256,
        "charged_class_list_citation": (
            "REP-96-INNER §5, frozen copy hashed before reading; "
            "three classes / 72 tuples including const-4c with Pi a 4-cycle. "
            "CONTROL ONLY; the decision is the native 6^9 universe."
        ),
        "iota_split": "(delta_3^{k_*}, 1, 1)",
        "tube_embedding_control_only": "adjacent blocks (1,2,3), (4,5,6), (7,8,9)",
        "decision_path": "native_transposition_universe_no_strand_map",
        "OPEN": [
            "OPEN[BMFACT-ORIENTATION]: Sage product vs inverse (both run)",
            "OPEN[BMFACT-BASEPOINT]: Sage 4-tuple omits the geometric-basis base point",
        ],
    }

    if args.curve_check and args.json_path is None and not args.selftest:
        print("=== sympy curve check ===")
        curve = run_curve_check()
        report["mode"] = "curve-check"
        report["curve_check"] = curve
        print(json.dumps(curve, indent=2))
        if not curve.get("passed"):
            report["fatal"] = "curve-check failed"
            _emit(report, args.out)
            return 2
        print("CURVE-CHECK-OK")
        _emit(report, args.out)
        return 0

    print("=== hard-coded class list (CONTROL ONLY) ===")
    gate = run_gate3_on_reps()
    report["gate3_on_reps"] = gate
    print(json.dumps(gate, indent=2))
    if not gate["passed"]:
        report["fatal"] = "GATE-3 failed on a hard-coded representative at k_*=-8"
        _emit(report, args.out)
        return 2

    expanded = expand_72()
    report["n_expanded"] = len(expanded)
    print("expanded conjugacy orbits: %d (expect 72)" % len(expanded))

    pin = assert_pi_types(expanded)
    report["pi_type_assertion"] = {
        "passed": pin["passed"],
        "n_checked": pin["n_checked"],
        "n_pi_transposition": pin["n_pi_transposition"],
        "n_pi_fourcycle": pin["n_pi_fourcycle"],
        "failures": pin["failures"],
        "note": pin["note"],
    }
    print(
        "Pi-type assertion passed=%s (NOT used as a filter); "
        "n_transposition=%s n_fourcycle=%s"
        % (pin["passed"], pin["n_pi_transposition"], pin["n_pi_fourcycle"])
    )
    if not pin["passed"]:
        print("PI-TYPE-ASSERTION-FAIL %s" % pin["failures"])

    nines: List[Tuple[frozenset, ...]] = []
    nines_with_class: List[Tuple[Tuple[frozenset, ...], str, Tuple[int, int, int, int]]] = []
    for item in expanded:
        nine = reconstruct_nine(item, KSTAR)
        nines.append(nine)
        nines_with_class.append((nine, str(item["name"]), item["Pi"]))  # type: ignore[arg-type]
    report["n_reconstructed_nines"] = len(set(nines))
    if len(set(nines)) != EXPECTED_GENERATING:
        print(
            "WARNING reconstructed 9-tuples collapsed: %d unique"
            % len(set(nines))
        )

    pos = run_positive_control(nines)
    report["positive_control"] = pos
    print(
        "POSITIVE CONTROL generating=%s expected=72 passed=%s"
        % (pos["n_generating"], pos["passed"])
    )
    neg = run_negative_control(nines)
    report["negative_control"] = neg
    print(
        "NEGATIVE CONTROL projective-product=1 count=%s expected=0 passed=%s"
        % (neg["n_generating_product_fixed_and_total_product_one"], neg["passed"])
    )

    run_brute = bool(args.brute_block or (args.selftest and args.json_path is None))
    if run_brute:
        print("BRUTE adjacent-block 6^9 against CABLE-3 rho_inf (control) ...")
        brute = brute_generating_product_fixed(KSTAR)
        report["brute_block_6pow9"] = brute
        print(
            "BRUTE n_generating=%s passed=%s"
            % (brute["n_generating"], brute["passed"])
        )
        if not brute["passed"]:
            pos = dict(pos)
            pos["passed"] = False

    print("=== synthetic pruner (subsample cert) ===")
    synth = synthetic_pruner_selftest()
    report["synthetic_pruner"] = synth
    print(
        "SYNTHETIC_PRUNER passed=%s pruned=%s unpruned=%s"
        % (synth["passed"], synth["n_pruned_survivors"], synth["n_unpruned_survivors"])
    )

    controls_ok = (
        bool(pos["passed"])
        and bool(neg["passed"])
        and bool(gate["passed"])
        and bool(pin["passed"])
        and bool(synth["passed"])
    )
    report["controls_passed"] = controls_ok
    if not controls_ok:
        report["fatal"] = (
            "self-controls failed: positive=%s negative=%s gate3=%s pi_type=%s "
            "synthetic_pruner=%s. Refusing to interpret Sage output."
            % (
                pos["passed"],
                neg["passed"],
                gate["passed"],
                pin["passed"],
                synth["passed"],
            )
        )
        _emit(report, args.out)
        return 2

    if args.curve_check:
        print("=== sympy curve check ===")
        curve = run_curve_check()
        report["curve_check"] = curve
        print(json.dumps({k: curve[k] for k in curve if k != "disc_sqf"}, indent=2))
        if not curve.get("passed"):
            report["fatal"] = "curve-check failed"
            _emit(report, args.out)
            return 2
        print("CURVE-CHECK-OK")

    if args.selftest and args.json_path is None:
        report["mode"] = "selftest"
        report["decision"] = None
        report["decision_note"] = (
            "selftest has no Sage JSON; native decision not run. "
            "Token is not SURVIVOR / NATIVE_ZERO_CURVE_ONLY / OPEN."
        )
        print("SELFTEST-OK")
        _emit(report, args.out)
        return 0

    if args.json_path is None:
        print("no JSON path; ran class-list controls only. pass --selftest to be explicit.")
        report["mode"] = "controls-only"
        _emit(report, args.out)
        return 0

    bundle = load_bundle(args.json_path)
    report["mode"] = "with-json"
    report["json_path"] = args.json_path
    report["sage_nstrands"] = bundle.get("nstrands")
    report["sage_n_factors"] = bundle.get("n_factors")
    report["sage_census"] = bundle.get("census")
    report["sage_unpack_shape"] = bundle.get("unpack_shape")
    report["sage_base_point"] = bundle.get("base_point")
    report["sage_strand_order_FLAG"] = bundle.get("strand_order_FLAG")
    braids = bundle.get("braids") or []
    census = bundle.get("census") or {}
    api_ok = True
    api_reasons: List[str] = []
    if not braids:
        api_ok = False
        api_reasons.append("JSON has no braids")
    if bundle.get("nstrands") not in (None, 9, N_STRANDS):
        api_ok = False
        api_reasons.append("nstrands = %s, expected 9" % bundle.get("nstrands"))
    for rec in braids:
        if not rec.get("tietze"):
            api_ok = False
            api_reasons.append("braid index %s has empty Tietze" % rec.get("index"))
            break
    census_ok: Optional[bool]
    if not census:
        census_ok = None
        api_ok = False
        api_reasons.append("JSON has no census record")
    else:
        census_ok = bool(census.get("ok")) and (
            int(census.get("n_tangency") or -1) == 8
            and int(census.get("n_four_node_fibre") or census.get("n_four_node_fibres") or -1) == 1
            and int(census.get("n_one_node_fibre") or census.get("n_one_node_fibres") or -1) == 2
            and int(census.get("exponent_ledger") or -1) == 20
        )
        if census.get("ok") and not census_ok:
            census_ok = False

    # BLOCK intersection is diagnostic only and is not the decision.
    if braids:
        block_as_written = intersect_block_with_braids(
            nines_with_class, braids, invert=False
        )
        block_inverse = intersect_block_with_braids(
            nines_with_class, braids, invert=True
        )
        report["diagnostic_BLOCK_not_decision"] = {
            "per_class": block_as_written["per_class"],
            "total_survivors": block_as_written["total_survivors"],
            "note": (
                "Adjacent-block identification is CONTROL / diagnostic. "
                "It is not the decision path and must not be read as a "
                "row-level kill."
            ),
        }
        report["diagnostic_BLOCK_inverse_not_decision"] = {
            "per_class": block_inverse["per_class"],
            "total_survivors": block_inverse["total_survivors"],
        }
        print(
            "DIAGNOSTIC BLOCK (not decision) total_survivors=%s"
            % block_as_written["total_survivors"]
        )

    native_full: Optional[Dict[str, object]] = None
    native_full_inv: Optional[Dict[str, object]] = None
    native_prod: Optional[Dict[str, object]] = None
    native_prod_inv: Optional[Dict[str, object]] = None
    if api_ok:
        certify = not args.skip_subsample_cert
        print("SAGE-NATIVE product-only (as-written) ...")
        native_prod = run_native_scan(
            braids, invert=False, product_only=True, certify_subsample=certify
        )
        print("SAGE-NATIVE product-only (inverse) ...")
        native_prod_inv = run_native_scan(
            braids, invert=True, product_only=True, certify_subsample=certify
        )
        print("SAGE-NATIVE full ZvK (as-written) ...")
        native_full = run_native_scan(
            braids, invert=False, product_only=False, certify_subsample=certify
        )
        print("SAGE-NATIVE full ZvK (inverse) ...")
        native_full_inv = run_native_scan(
            braids, invert=True, product_only=False, certify_subsample=certify
        )
        report["variant_SAGE_NATIVE_product_only"] = native_prod
        report["variant_SAGE_NATIVE_product_only_inverse"] = native_prod_inv
        report["variant_SAGE_NATIVE_full"] = native_full
        report["variant_SAGE_NATIVE_full_inverse"] = native_full_inv
        print(
            "SAGE-NATIVE product-only generating as-written=%s inverse=%s"
            % (native_prod["n_generating"], native_prod_inv["n_generating"])
        )
        print(
            "SAGE-NATIVE full generating as-written=%s inverse=%s"
            % (native_full["n_generating"], native_full_inv["n_generating"])
        )

    token, reason = decide_native(
        census_ok=census_ok,
        api_ok=api_ok,
        native_full=native_full,
        native_full_inv=native_full_inv,
        native_prod=native_prod,
        native_prod_inv=native_prod_inv,
    )
    report["decision"] = token
    report["decision_reason"] = reason
    report["api_ok"] = api_ok
    report["api_reasons"] = api_reasons
    report["census_ok"] = census_ok
    print("DECISION %s" % token)
    print(reason)
    if token.startswith("OPEN"):
        report["OPEN_token"] = token

    _emit(report, args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
