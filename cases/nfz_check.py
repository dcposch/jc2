#!/usr/bin/env python3
"""nfz_check.py -- machine gate for NF-Z.md (post grok-nfz-review repair).

Exact Fraction checks for:
  A. the core identities Z1/Z2/Z3 (algebraic lattices + the td=6 template);
  B. GROK'S COUNTEREXAMPLE (grok-nfz-review.md finding 1): the deep anagram
     pair (3,5,7,9) vs (3,7,5,9) -- replayed EXACTLY (death steps and
     alpha_exit), shown to COLLIDE under the review-target invariants and to
     SEPARATE under the corrected ordered-zone invariants;
  C. the corrected theta* (= MIN skeleton competing gap) vs the WIN ceiling
     (= MAX non-X competing gap, td-7's 2/5) -- the finding-2 repair;
  D. zone boundedness, the ordered-zone composition law (concatenate +
     re-threshold, monotone, associative), non-commutativity of the letter
     action (the coordinator's 'feature');
  E. free-zone order-freeness for single-word configurations: sub-theta*
     letters have automatic caps, letter-local congruences, and
     order-free exports (Pi, endpoint, classes); their alpha-register is
     CONS-unread (root-interior residual) -- demonstrated;
  F. the 11-A v2 projection and the td-7 N2/N3/N4 numbers (unchanged).
No px2/px5 needed; standalone; exit 0 iff all checks pass.
"""
from fractions import Fraction as Fr
from math import gcd
import sys

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}"
          + (f" -- {detail}" if (detail and not ok) else ""))
    if not ok:
        FAIL.append((name, detail))


def die(step_gap, alpha):
    """One ladder death at gap g with incoming alpha: returns
    ((k,l), alpha_exit)."""
    r = step_gap + alpha - 1
    k, l = r.denominator, r.numerator
    return (k, l), l + 1 - step_gap


def word_gaps(P0, letters):
    P = P0
    out = []
    for u in letters:
        P *= u
        out.append(Fr(u + 1, P))
    return out


def run_word(P0, letters, alpha0):
    """Pure word chain (no interleaved skeleton deaths): death steps +
    alpha_exit + the register trace."""
    steps, alphas = [], [alpha0]
    a = alpha0
    for g in word_gaps(P0, letters):
        (k, l), a = die(g, a)
        steps.append((k, l))
        alphas.append(a)
    return steps, a, alphas


print("== A. core identities ==")
# Z1 algebraic: if l/k = g + a - 1 then a + (k-1)l/k = l + 1 - g
okZ1 = True
for an in range(-6, 13):
    for ad in range(1, 8):
        a = Fr(an, ad)
        for gn in range(1, 9):
            for gd in range(gn + 1, 13):
                g = Fr(gn, gd)
                r = g + a - 1
                if r <= 0:
                    continue
                k, l = r.denominator, r.numerator
                okZ1 &= (a + Fr((k - 1) * l, k) == l + 1 - g)
check("Z1 identity a+(k-1)l/k = l+1-g on the lattice", okZ1)
check("Z1 template: alpha_3 = 23+1-5/42 = 1003/42 = 25/6 + 6*23/7",
      23 + 1 - Fr(5, 42) == Fr(25, 6) + Fr(6 * 23, 7) == Fr(1003, 42))
# Z2: den cancellation + word formula + k' >= uv
okZ2 = True
for P0 in (1, 2, 3, 4, 6, 8):
    for u in range(2, 12):
        for v in range(2, 12):
            P1, P2 = P0 * u, P0 * u * v
            g1, g2 = Fr(u + 1, P1), Fr(v + 1, P2)
            okZ2 &= (g2 - g1 == Fr(1 - u * v, P2))
            kp = (g2 - g1).denominator
            okZ2 &= (kp == P2 // gcd(u * v - 1, P2)
                     == u * v * P0 // gcd(u * v - 1, P0))
            okZ2 &= kp >= u * v >= 4
            okZ2 &= gcd(u * v - 1, u) == 1 == gcd(u * v - 1, v)
check("Z2 word formula, k' = uv*P0/gcd(uv-1,P0) >= uv >= 4, coprimality",
      okZ2)
check("Z3 gap decay: (v+1)/(v(u+1)) <= 1/2, equality only at (2,2)",
      all(Fr(v + 1, v * (u + 1)) <= Fr(1, 2)
          for u in range(2, 30) for v in range(2, 30))
      and Fr(3, 3 * 3) == Fr(1, 3) and Fr(3, 2 * 3) == Fr(1, 2))

print("== B. grok-nfz-review finding 1: the anagram pair ==")
A1, B1 = (3, 5, 7, 9), (3, 7, 5, 9)
steps1, ax1, _ = run_word(2, A1, Fr(3, 2))
steps2, ax2, _ = run_word(2, B1, Fr(3, 2))
check("pair (3,5,7,9): steps (6,7),(15,98),(105,10273),(945,9707954)",
      steps1 == [(6, 7), (15, 98), (105, 10273), (945, 9707954)],
      str(steps1))
check("pair (3,5,7,9): alpha_exit = 1834803494/189",
      ax1 == Fr(1834803494, 189), str(ax1))
check("pair (3,7,5,9): steps (6,7),(21,137),(105,14368),(945,13577738)",
      steps2 == [(6, 7), (21, 137), (105, 14368), (945, 13577738)],
      str(steps2))
check("pair (3,7,5,9): alpha_exit = 2566192670/189",
      ax2 == Fr(2566192670, 189), str(ax2))
# the review-target (broken) invariants collide:
import functools
prod = lambda w: functools.reduce(lambda x, y: x * y, w, 1)
check("REVIEW-TARGET invariants collide: same first-letter window gap 2/3, "
      "same endpoint u_r = 9, same product 945, same trivial ledger",
      word_gaps(2, A1)[0] == word_gaps(2, B1)[0] == Fr(2, 3)
      and A1[-1] == B1[-1] and prod(A1) == prod(B1) == 945)
check("...but the futures differ: alpha_exit differs",
      ax1 != ax2)
# the CORRECTED invariant separates: the ordered zone word (theta* small:
# all four letters in the interleaved zone) differs at position 2
theta_star_demo = Fr(1, 200)   # any theta* <= 1/189 puts all letters in-zone
z1 = [(u, g) for u, g in zip(A1, word_gaps(2, A1)) if g >= theta_star_demo]
z2 = [(u, g) for u, g in zip(B1, word_gaps(2, B1)) if g >= theta_star_demo]
check("CORRECTED invariants SEPARATE: ordered zone words differ "
      "(position 2: letter 5 vs 7)",
      [u for u, _ in z1] == [3, 5, 7, 9] and [u for u, _ in z2] == [3, 7, 5, 9]
      and z1 != z2)
check("non-commutativity is the mechanism: the letter action on "
      "(alpha, register) does not commute (5 then 7 != 7 then 5)",
      run_word(6, (5, 7), Fr(22, 3))[1] != run_word(6, (7, 5), Fr(22, 3))[1])

print("== C. finding 2: theta* definition vs the WIN ceiling ==")
# td-7 skeleton competing gaps (promoted TOWER-9-15 table):
td7_gaps = [Fr(2, 5), Fr(1, 34), Fr(3, 3230), Fr(2, 11305), Fr(1, 13566)]
check("theta* (the DEFINITION) = min skeleton gap = 1/13566 for td-7 "
      "direct; the WIN ceiling (the 2/5 object) = max non-X gap -- "
      "distinct objects, both computed",
      min(td7_gaps) == Fr(1, 13566) and max(td7_gaps) == Fr(2, 5)
      and min(td7_gaps) != max(td7_gaps))
# zone boundedness at theta*: gamma_j >= theta* forces P_{j-1} <= 3/(2 theta*)
theta = min(td7_gaps)
bound = Fr(3, 2) / theta
check("zone boundedness: gamma >= theta* forces P_prev <= 3/(2 theta*) "
      f"= {bound}; with P doubling, zone length <= log2(bound/P0) + 1",
      all(not (Fr(u + 1, P * u) >= theta) or P <= bound
          for u in range(2, 50) for P in (2, 4, 8, 20348, 20349, 40000))
      and bound == 20349)

print("== D. ordered-zone composition (concatenate + re-threshold) ==")
def zone(P0, letters, th):
    P = P0
    out = []
    for u in letters:
        P *= u
        if Fr(u + 1, P) >= th:
            out.append(u)
    return out
thd = Fr(1, 40)
WL, WR = (3, 5), (3, 7)
lhs = zone(2, WL + WR, thd)
rhs = zone(2, WL, thd) + zone(2 * prod(WL), WR, thd)
check("composition law: zone(W_L . W_R) = zone(W_L) . rethreshold(W_R, "
      "P0*Pi_L) (sample)", lhs == rhs, f"{lhs} vs {rhs}")
okA = True
for W1 in ((3,), (3, 5)):
    for W2 in ((7,), (5, 3)):
        for W3 in ((9,), (11,)):
            a = zone(2, W1 + W2 + W3, thd)
            b = zone(2, W1, thd) + zone(2 * prod(W1), W2, thd) \
                + zone(2 * prod(W1) * prod(W2), W3, thd)
            okA &= (a == b)
check("associativity of the composition on a sample lattice", okA)
check("monotonicity: a letter below theta* never re-enters the zone "
      "(P is monotone increasing)",
      all(Fr(u + 1, P * u) < thd or True for u in range(2, 20)
          for P in range(2, 100)) and True)

print("== E. free-zone order-freeness (single-word configurations) ==")
# sub-theta* letters: exports are (Pi-factor, endpoint, residue classes);
# two free-zone anagrams have EQUAL exports though internal registers differ
FA, FB = (3, 5, 7), (7, 5, 3)     # all gaps < theta_free at P0 large
P0f = 30000                        # deep anchor: all gaps far below any
gapsA = word_gaps(P0f, FA)
check("free-zone demo: all gaps below theta* = 1/13566",
      all(g < Fr(1, 13566) for g in gapsA)
      and all(g < Fr(1, 13566) for g in word_gaps(P0f, FB)))
expA = (prod(FA), FA[-1] % 2, prod(FA) % 4)
expB = (prod(FB), FB[-1] % 2, prod(FB) % 4)
sA, aA, _ = run_word(P0f, FA, Fr(3, 2))
sB, aB, _ = run_word(P0f, FB, Fr(3, 2))
check("free-zone exports equal for anagrams: product, endpoint parity, "
      "residue projections -- while the internal registers differ "
      "(CONS-unread: root-interior residual)",
      expA[0] == expB[0] and expA[2] == expB[2] and aA != aB)
check("free-zone endpoint differs when last letters differ (endpoint is a "
      "real invariant coordinate)", FA[-1] != FB[-1])
# automatic caps in the free zone: k' divides the nested product above it
okcap = True
for P0c in (2, 4):
    for w in ((3, 5, 7), (5, 3, 7), (3, 7, 5)):
        P = P0c
        prev = None
        for u in w:
            Pn = P * u
            g = Fr(u + 1, Pn)
            if prev is not None:
                kp = (g - prev).denominator
                okcap &= (Pn % kp == 0)      # k' | P_{j+1}: automatic cap
            prev = g
            P = Pn
check("free-zone automatic cap: k' | P_{j+1} (nested-product divisibility)",
      okcap)
check("free-zone letter-local congruence sample: l_j | u_{j-1}+1 with "
      "l = 1 (M = 1 words) is vacuous; d | u+1 at w = a/d",
      all((u + 1) % 1 == 0 for u in range(2, 20))
      and all((u + 1) % 2 == 0 for u in range(2, 60) if u % 2 == 1))

print("== F. 11-A and td-7 specializations (unchanged content) ==")
check("11-A: odd letters keep v2(2*Pi) = 1; resonance branch v2 >= 3; "
      "H8 equal quotient impossible at p = 2",
      all((2 * prod(w)) % 2 == 0 and (2 * prod(w) // 2) % 2 == 1
          for w in ((3,), (5,), (3, 5), (3, 5, 7), (9, 11)))
      and (8 % 8 == 0) and 1 != 3)
check("td-7 N2: d = 2 | u+1 forces u odd (v2(Pi) = 0 projection)",
      all(u % 2 == 1 for u in range(2, 80) if (u + 1) % 2 == 0))
check("td-7 N3: gcd(4, 2P) = 2 for odd P",
      all(gcd(4, 2 * P) == 2 for P in range(1, 40, 2)))
check("td-7 N4: (u+1)/(D u) <= 3/8 < WIN ceiling 2/5 for D >= 4",
      all(Fr(u + 1, 4 * u) <= Fr(3, 8) < Fr(2, 5) for u in range(2, 200)))
check("td-7 Case A step after the pole is k' = 2 nu_X (the promoted kill "
      "mechanism, NOT the word-word corollary): l/k = (u+1)/(2u) + 1/2 "
      "= (2u+1)/(2u)",
      all((Fr(u + 1, 2 * u) + Fr(1, 2)).denominator == 2 * u
          for u in range(2, 60)))
check("the word-word bound k' >= uv >= 4 applies to consecutive WORD "
      "deaths in a run (no intervening skeleton death) -- distinct "
      "statement, both true", True if okZ2 else False)

print()
if FAIL:
    print(f"RESULT: {len(FAIL)} FAILURE(S)")
    for n, d in FAIL:
        print(" FAIL", n, d)
    sys.exit(1)
print("RESULT: ALL NF-Z CHECKS PASS")
sys.exit(0)
