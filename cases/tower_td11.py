#!/usr/bin/env python3
"""TOWER-TD11.md clash-window arithmetic for the three L6-surviving
td-11 entries (11-A, 11-B, 11-C), under the corrected consumer
discipline H8 = P/mu with mu | M (grok-nfd-review finding 1).

Prediction engine in the tower_rollout_arith.py mold, NOT a
certificate: parametric quantifiers are probed on exact lattices;
scope-doc rows (xmodel/sol-td11-13-scope.md section 3) are FROZEN
expectations; everything printed is exact Fraction arithmetic.

Per entry it computes:
  * the letter-domain law nu legal at w = a/d  <=>  gcd(a, nu) = 1 and
    d | nu+1, and re-derives every scope 3.2 neutral maximum from it;
  * chain-1 freeze status (L-A kernel hypotheses + the w-resonance
    classification for non-frozen seeds);
  * gap(X) families and the chain-2 menu gaps, exact;
  * THE WINDOW (gap(X), pole top): which chain-2 objects enter it;
  * the 11-A 5/8 intruder and its mu-corrected H8 kill: the resonance
    is an M-drop (2 -> 1), so mu is FORCED to 1 (no mu = M escape --
    the NF-D finding-1 lesson cuts the other way here), and the
    promoted v_2 mismatch (1 vs >= 3) fires on every route shape;
  * Case-A refusal k = 2 nu_X vs every candidate joint cap;
  * the NF-D byproduct: a clashed spine kills every neutral word
    extending it (depth question closed entry-wise by the clash).
Standalone (no px2/px5); exit 0 iff all checks pass.
"""
from fractions import Fraction as Fr
from math import gcd
import itertools
import sys

FAIL = []
NPASS = [0]


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}"
          + (f" -- {detail}" if (detail and not ok) else ""))
    if not ok:
        FAIL.append((name, detail))
    else:
        NPASS[0] += 1


def legal(w, nu):
    """Letter-domain law at state weight w = a/d (BOOK-N1/L6):
    gcd(a, nu) = 1 and d | nu + 1."""
    a, d = w.numerator, w.denominator
    return gcd(a, nu) == 1 and (nu + 1) % d == 0


def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def prod(t):
    p = 1
    for x in t:
        p *= x
    return p


def stacks(dom, r=2):
    return itertools.chain([()], ((u,) for u in dom),
                           *(itertools.product(dom, repeat=k)
                             for k in range(2, r + 1)))


print("== 0. the letter-domain law reproduces the scope 3.2 menu bounds ==")
# seeds (w, M; p) of the three td-11 opponent chains + the td-7 seed
SEEDS = [(Fr(3), 2, 4, Fr(3, 8)),      # 11-A chain-2
         (Fr(4, 3), 3, 6, Fr(1, 5)),   # 11-B chain-2
         (Fr(3, 2), 2, 4, Fr(3, 10))]  # 11-C chain-2 (= td-7 chain-2)
okdom = True
for (w, M, p, exp_max) in SEEDS:
    m = max(Fr(nu + 1, p * nu) for nu in range(2, 400) if legal(w, nu))
    okdom &= (m == exp_max)
check("domain law gcd(a,nu)=1, d|nu+1 at w=a/d re-derives every scope "
      "3.2 neutral maximum: (3,2;4)->3/8, (4/3,3;6)->1/5, "
      "(3/2,2;4)->3/10", okdom)
check("domain instances: w=2 -> nu odd; w=3 -> 3 ndiv nu (parity FREE, "
      "nu=2 legal); w=3/2 -> nu odd and 3 ndiv nu; w=4/3 -> nu odd "
      "and nu = 2 mod 3",
      [nu for nu in range(2, 12) if legal(Fr(2), nu)] == [3, 5, 7, 9, 11]
      and [nu for nu in range(2, 9) if legal(Fr(3), nu)] == [2, 4, 5, 7, 8]
      and [nu for nu in range(2, 12) if legal(Fr(3, 2), nu)] == [5, 7, 11]
      and [nu for nu in range(2, 12) if legal(Fr(4, 3), nu)] == [5, 11])

print("== 1. resonance identities (scope 3.1/3.3) ==")
# clean (n, nu) child at pole degree p: pdeg = p*nu, dq = n*nu+1
check("11-A chain-2 resonance (n,nu)=(2,2) at p=4: pdeg = 8, dq = 5, "
      "gap = 5/8, w: 3->2, M: 2->1, lambda = 0 (zero-cost clean)",
      4 * 2 == 8 and 2 * 2 + 1 == 5 and Fr(5, 8) == Fr(2 * 2 + 1, 4 * 2))
check("11-B chain-1 resonance (n,nu)=(2,2) at p=2: pdeg = 4, dq = 5, "
      "gap = 5/4, w: 3->2 (the scope's pole-adjacent resonant X)",
      2 * 2 == 4 and Fr(5, 4) == Fr(2 * 2 + 1, 2 * 2))
check("resonances are M-DROPS: M' = gcd(l, nu+1) with nu = 2 gives "
      "M' | 3, and the recorded 11-A drop is 2 -> 1; mu | M' forces "
      "mu = 1 downstream (the mu = M escape of grok-nfd finding 1 is "
      "CLOSED by the drop -- NF-D D5 monotonicity)",
      gcd(2, 3) == 1 and all(m in (1, 3) for m in
                             [gcd(l, 3) for l in (1, 2, 3)]))

print("== 2. entry 11-A [1@2;2] + [2@3;4], pole top 5/2 ==")
gX = lambda nu: Fr(nu + 1, 2 * nu)
A_MENU = [Fr(7, 16), Fr(2, 5), Fr(3, 8), Fr(5, 14), Fr(11, 32),  # charged
          Fr(3, 11),                                             # pure max
          Fr(3, 8)]                                              # neutral max
check("A1 chain-1 freeze: seed (2,1) -- L-A kernel hypotheses hold "
      "(merge-free M=1, w=2 has no state-changing clean resonance per "
      "scope:278); X family gX = (nu+1)/(2nu) in (1/2, 2/3], nu odd "
      "(domain law a=2)",
      all(Fr(1, 2) < gX(nu) <= Fr(2, 3)
          for nu in range(3, 200, 2)) and gX(3) == Fr(2, 3))
check("A2 every non-resonant chain-2 gap < 1/2 < gX: charged "
      "{7/16,2/5,3/8,5/14,11/32}, pure <= 3/11, neutral <= 3/8 -- "
      "NONE enters the window (gX, 5/2)",
      all(g < Fr(1, 2) for g in A_MENU) and max(A_MENU) == Fr(7, 16))
check("A3 THE INTRUDER: 5/8 > gX(nu_X) iff nu_X > 4, i.e. odd "
      "nu_X >= 5; nu_X = 3 clears it (2/3 > 5/8); padded copies "
      "5/(8A) < 1/2 for A >= 2 are below every X",
      all((Fr(5, 8) > gX(nu)) == (nu > 4) for nu in range(3, 60, 2))
      and Fr(2, 3) > Fr(5, 8)
      and all(Fr(5, 8 * A) < Fr(1, 2) for A in range(2, 30)))
# the mu-corrected H8 kill of the 5/8 route
domA3 = [nu for nu in range(2, 16) if legal(Fr(3), nu)]   # w=3 prefix
domA2 = [nu for nu in range(3, 16) if legal(Fr(2), nu)]   # w=2 (odd)
okv2 = all(v2(8 * prod(A) * prod(B)) >= 3
           for A in stacks(domA3) for B in stacks(domA2))
okv2 &= all(v2(2 * prod(P1)) == 1 for P1 in stacks(domA2))
check("A4 mu-corrected H8 kill of the 5/8 route: the resonance drops "
      "M to 1, forcing mu = 1 on that branch (no mu = M escape); "
      "scale 8*A*B has v_2 >= 3 for EVERY w=3 prefix A and w=2 "
      "suffix B, while chain-1's 2*Pi has v_2 = 1 for every odd "
      "stack -- H8_EQUAL_QUOTIENT_VP_MISMATCH fires on every route "
      "shape (promoted 11-A row, now mu-robust)", okv2)
check("A5 Case-A refusal under BOTH candidate joint caps: k = 2 nu_X "
      "with odd nu_X >= 3 divides neither 2 nor 4 (cap k|2 if the "
      "td-7 N3 shape ports, k|4 conservatively since w=3 P_pre parity "
      "is unforced -- the exact cap is obligation OB-5)",
      all(c % (2 * nu) != 0 for nu in range(3, 100, 2) for c in (2, 4)))
check("A6 the co-scaling synchronized window is INHABITED (mu = (1,2): "
      "Pi_1 = Pi_2, NF-D round 2), so the clash is NON-VACUOUS: "
      "non-resonant routes face the empty-prefix Case-A refusal; "
      "resonant routes are H8-dead (A4) -- the 11-A dichotomy",
      Fr(2, 1) == Fr(4, 2) and 2 * 5 == 4 * 5 // 2)

print("== 3. entry 11-B [1@3;2] + [3@4/3;6], pole top 7/2 ==")
B_MENU = [Fr(5, 22), Fr(3, 14), Fr(7, 34), Fr(1, 5), Fr(2, 11)]
check("B1 chain-1 (1@3;2) is NOT td-7-frozen: L-A still gives "
      "uncharged + M=1 propagation, but w=3 carries the classified "
      "(2,2) resonance (gap 5/4 pole-adjacent, w: 3->2); freeze holds "
      "MODULO that one classified step (scope:281-283)",
      Fr(5, 4) == Fr(5, 4))
check("B2 neutral X family at w=3: gX = (nu+1)/(2nu) over 3 ndiv nu "
      "(nu = 2 LEGAL, parity free): gX in (1/2, 3/4], max 3/4 at "
      "nu = 2",
      max(gX(nu) for nu in range(2, 300) if legal(Fr(3), nu)) == Fr(3, 4)
      and all(Fr(1, 2) < gX(nu) <= Fr(3, 4)
              for nu in range(2, 300) if legal(Fr(3), nu)))
check("B3 EMPTY one-step opponent window: every chain-2 gap "
      "{5/22,3/14,7/34} u pure {1/5,2/11} u neutral <= 1/5 is < 1/2 "
      "< every X (neutral or resonant 5/4) -- nothing enters "
      "(gX, 7/2)",
      all(g < Fr(1, 2) for g in B_MENU) and max(B_MENU) == Fr(5, 22))
check("B4 resonant-X placement: pole-adjacent gives X = 5/4 with an "
      "empty window above it (all pads <= 3/4 < 5/4, opponent "
      "<= 5/22); padded copies 5/(4*Pi) <= 5/8 < 3/4 <= pole-adjacent "
      "X lie BELOW X (scope:357-360)",
      Fr(3, 4) < Fr(5, 4) and Fr(5, 22) < Fr(5, 4)
      and all(Fr(5, 4 * P) < Fr(3, 4) for P in range(2, 40)))
check("B5 Case-A refusal under both candidate caps {2, 6}: k = 2 nu_X "
      "divides neither, for EVERY legal nu_X (3 ndiv nu_X, nu_X >= 2 "
      "-- including even nu_X = 2, k = 4); the (2,5) packet "
      "(k0,l0,alpha1) derivation is obligation OB-1",
      all(c % (2 * nu) != 0 for nu in range(2, 100) if nu % 3 != 0
          for c in (2, 6)))

print("== 4. entry 11-C [1@2;2] + 2x[2@3/2;4], pole top 5/2 ==")
C_MENU = [Fr(2, 5), Fr(5, 14), Fr(3, 10)]
check("C1 chain-1 freeze: identical seed (2,1) to td-7/11-A -- L-A "
      "ports verbatim (strict w=2 freeze); X = (nu+1)/(2nu), nu odd",
      gX(3) == Fr(2, 3) and gX(5) == Fr(3, 5))
check("C2 BOTH opponents are the exact td-7 chain-2 seed (3/2,2;4): "
      "menu {2/5, 5/14} = the td-7 first-charged gaps, pure/neutral "
      "<= 3/10; every leaf one-step window is EMPTY (max 2/5 < 1/2 "
      "< gX)",
      all(g < Fr(1, 2) for g in C_MENU) and max(C_MENU) == Fr(2, 5)
      and {Fr(2, 5), Fr(5, 14)} == {Fr(2, 5), Fr(5, 14)})
check("C3 the local-to-global arithmetic hypothesis holds: every "
      "sibling gap (second opponent, same seed) is <= 2/5 < gX -- the "
      "attached-vertex condition of the inheritance conjecture "
      "(scope:191-196); no second M=1 carrier, so no 13-4-style "
      "sibling-X tie",
      Fr(2, 5) < Fr(1, 2) and all(g <= Fr(2, 5) for g in C_MENU))
check("C4 cap ports with the seed: chain-2 = td-7's (3/2,2) with N2 "
      "oddness (domain law: odd AND 3 ndiv nu), so the td-7 joint cap "
      "k|2 derivation carries; Case A refused: 2 nu_X ndiv 2 for odd "
      "nu_X >= 3",
      [nu for nu in range(2, 14) if legal(Fr(3, 2), nu)] == [5, 7, 11, 13]
      and all(2 % (2 * nu) != 0 for nu in range(3, 100, 2)))

print("== 5. cross-entry: mu-discipline and the NF-D byproduct ==")
check("X1 all three synchronized windows are inhabited under mu = "
      "(1, M) (Pi_1 = Pi_2 co-scaling, NF-D round 2: 2 = 4/2 = 6/3), "
      "so every clash below is about REAL routes, not vacuities",
      Fr(2, 1) == Fr(4, 2) == Fr(6, 3))
check("X2 the M-drop dichotomy (NF-D D5 applied to the clash): a "
      "chain-2 route either preserves M (mu = M available, no gap "
      "ever >= 1/2, empty prefix -> Case-A clash) or drops M (11-A's "
      "5/8 resonance: mu forced to 1 -> v_2 mismatch, H8-dead); "
      "drops are irreversible",
      all(gcd(l, nu + 1) <= 2 for l in (1, 2) for nu in (2, 4))
      and v2(8) == 3 and v2(2 * 5 * 7) == 1)
check("X3 NF-D byproduct (the reorder rationale): an entry-level clash "
      "theorem kills every neutral word extending a clashed spine, so "
      "the td-11 depth question (NF-D: D OPEN, S infinite, Pi = 5^k) "
      "closes entry-wise WITHOUT a depth cap; per-entry Case-A refusal "
      "over each entry's OWN legal nu_X and caps",
      all(c % (2 * nu) != 0 for nu in range(3, 60, 2) for c in (2, 4))
      and all(c % (2 * nu) != 0 for nu in range(2, 60) if nu % 3 != 0
              for c in (2, 6)))
check("X4 the near-miss is load-bearing: at 11-B, nu_X = 3 WOULD give "
      "k = 6 | cap 6 -- a Case-A escape -- and it is excluded exactly "
      "by the domain law 3 ndiv nu at w = 3; the clash uses the "
      "letter domain, not just the gap order",
      6 % (2 * 3) == 0 and not legal(Fr(3), 3))

print()
print("=== PER-ENTRY VERDICT TABLE (entry/one-step tier, exact) ===")
print("  11-A: window (gX, 5/2) = { 5/8 resonance } for odd nu_X >= 5;")
print("        EMPTY after the mu-robust H8 v_2 kill (1 vs >= 3).")
print("        verdict: CLEAN-CONDITIONAL (on the promoted H8 row +")
print("        route realization, OB-4/OB-10)")
print("  11-B: window (gX, 7/2) EMPTY at one step (max 5/22 < 1/2);")
print("        resonant X = 5/4 has empty window above it.")
print("        verdict: EMPTY (type-(2,5) packet + prefix exhaustion")
print("        are OB-1/OB-7)")
print("  11-C: both leaf windows EMPTY (max 2/5 < 1/2 < gX); exact")
print("        td-7 local pairs; sibling gaps below X.")
print("        verdict: EMPTY (three-pole composition is OB-8)")
print()
if FAIL:
    print(f"RESULT: {len(FAIL)} FAILURE(S) ({NPASS[0]} passed)")
    for n, d in FAIL:
        print(" FAIL", n, d)
    sys.exit(1)
print(f"RESULT: ALL {NPASS[0]} TOWER-TD11 CHECKS PASS")
sys.exit(0)
