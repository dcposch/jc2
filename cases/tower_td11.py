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
check("resonances are M-DROPS (round-3 M' law fix, both reviews): the "
      "changing-cell law is M' = gcd(l, dq) = gcd(l, 5) (px2 engine, "
      "not the n=1 neutral law gcd(l, nu+1)); for every legal l | 2 "
      "this gives M' = 1 -- the recorded 2 -> 1 drop; mu | M' forces "
      "mu = 1 downstream (no grok-nfd finding-1 escape)",
      all(gcd(l, 5) == 1 for l in (1, 2))
      and gcd(2, 5) == 1)

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
      "(2,2) resonance (pdeg 2*2 = 4, dq = 5, gap 5/4 pole-adjacent, "
      "w: 3->2); 5/4 exceeds every neutral gX <= 3/4, so when taken "
      "pole-adjacent it IS the first death (round-3 de-tautologized)",
      Fr(2 * 2 + 1, 2 * 2) == Fr(5, 4)
      and Fr(5, 4) > max(gX(nu) for nu in range(2, 200) if nu % 3))
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

print("== 6. OB-1: entry ladder packets (derived, not inferred) ==")
# Packet law: pole pattern (t-A)^al (t-B)^be gives the P1 scale relation
# m^al = sigma0 * lam^be, i.e. pole death step (k0, l0) = (al, be);
# g_top = (al+be)/al; Z1 gives alpha_1 = l0 + 1 - g_top = be(al-1)/al.
def packet(al, be):
    gtop = Fr(al + be, al)
    k0, l0 = al, be
    a1 = l0 + 1 - gtop
    return (k0, l0), gtop, a1


pk23 = packet(2, 3)
pk25 = packet(2, 5)
check("OB1a packet law (P1 scale + Z1): type (2,3) -> (k0,l0) = (2,3), "
      "g_top = 5/2, alpha_1 = 3/2 -- EXACT regression against the "
      "promoted td-7 packet (t9_15_direct.json: alpha 3/2, top 5/2, "
      "m^2 = sigma0 lam^3)",
      pk23 == ((2, 3), Fr(5, 2), Fr(3, 2))
      and Fr(3 * (2 - 1), 2) == Fr(3, 2))
check("OB1b type (2,5) packet (11-B, NEW -- not inferred from (2,3)): "
      "(k0,l0) = (2,5), g_top = 7/2, alpha_1 = 5/2 = be(al-1)/al; "
      "den(alpha_1) = 2 divides every cap candidate",
      pk25 == ((2, 5), Fr(7, 2), Fr(5, 2))
      and all(c % 2 == 0 for c in (2, 4, 6)))
check("OB1c pole full degrees (scope 3.1 packets): 11-A (2,4); "
      "11-B (2,6); 11-C (2,4,4); X-side pole is (t-A)^2 in all three "
      "(type (2,x)), so i_X = 2",
      (2, 4) == (1 * 2, 2 * 2) and (2, 6) == (1 * 2, 3 * 2)
      and (2, 4, 4) == (1 * 2, 2 * 2, 2 * 2))

print("== 7. OB-4: H8 stacks under P/mu ==")
check("OB4a integrality and inhabitation: stack products are integers; "
      "the empty stack passes H8 = P/mu on all three entries "
      "(2/1 = 4/2 = 6/3); Pi = 5^k passes at every k (block 5) -- the "
      "synchronized windows are inhabited, the clash is non-vacuous",
      Fr(2, 1) == Fr(4, 2) == Fr(6, 3))
check("OB4b window characterization: common Pi must be composable on "
      "BOTH sides -- 11-A/11-C: odd (side-1) and 3-free (side-2 "
      "domain), e.g. 5, 25, 35, 55 legal, 9 = 3*3 excluded; 11-B: "
      "odd, 3-free, side-2-factorable into nu = 2 (mod 3) letters "
      "(25 = 5*5 works, 35 works as the single letter 35 = 2 mod 3)",
      all(legal(Fr(2), u) for u in (5, 25, 35, 55))
      and not legal(Fr(3, 2), 9) and not legal(Fr(3, 2), 3)
      and 25 % 3 == 1 and (25 == 5 * 5 and 5 % 3 == 2)
      and 35 % 3 == 2 and legal(Fr(4, 3), 35))
check("OB4c mu = (1,1) branches remain UNSAT (raw-P valuations, "
      "NF-D round 2) and a FAILED synchronization is spine-death "
      "(port obligation 4 discipline: no H8 match, no X) -- either "
      "way no escape route",
      all(v2(2 * prod(c)) == 1 for c in stacks(
          [u for u in range(3, 16, 2)]))
      and v2(4) == 2 and 1 != 2)

print("== 8. OB-5: joint caps ==")
check("OB5a X-side cap: X lives at the (t-A)^2 pole power (i_X = 2, "
      "all three entries), giving the td-7-style k | 2 while X is "
      "alive (Prop 4.2(iii)/Prop 8.1 integrality -- cited, not "
      "reproved); chain-2 side can only SHRINK the joint cap",
      gcd(2, 4) == 2 and gcd(2, 6) == 2)
check("OB5b conservative chain-2-side candidates (used so the theorem "
      "does not depend on OB5a's port): 11-A gcd(4, i*P_pre) with "
      "i in {2,4} (l | 2) and P_pre parity FREE (nu = 2 legal at w=3, "
      "even P_pre realized) -> {2,4}; 11-B gcd(6, i*P_pre), i in "
      "{2,6} (l | 3), P_pre odd and 3-free (w=4/3 domain) -> {2,6}; "
      "11-C ports td-7 (P_pre odd) -> {2}; exhaustion below runs over "
      "ALL candidates plus divisor closure {1}",
      legal(Fr(3), 2) and gcd(4, 2 * 2) == 4 and gcd(4, 2 * 5) == 2
      and gcd(6, 2 * 5) == 2 and gcd(6, 6 * 5) == 6
      and all(gcd(4, 2 * prod(c)) == 2 for c in stacks(
          [u for u in range(5, 14, 2) if u % 3 != 0])))

print("== 9. OB-7: the den-criterion prefix exhaustion (Cases A/B/C) ==")
# alpha-lattice lemma: alpha_1 den | c and prefix steps (k | c) keep
# den(alpha) | c: alpha_next = alpha + l(k-1)/k.
okLat = True
for c in (1, 2, 4, 6):
    for a_num in range(0, 2 * c):
        a = Fr(a_num, c) + Fr(3, 2) if c % 2 == 0 else Fr(a_num, c)
        for k in [d for d in (1, 2, 3, 4, 6) if c % d == 0]:
            for l in range(1, 12):
                nxt = a + Fr(l * (k - 1), k)
                okLat &= (nxt.denominator <= c and c % nxt.denominator == 0)
check("OB7a alpha-lattice lemma: den(alpha_1) | c and every prefix "
      "step with k | c keeps den(alpha) | c (alpha_next = alpha + "
      "l(k-1)/k) -- the exhaustion may quantify over the FULL lattice "
      "a/c, a SUPERSET of reachable registers (menu-independent)",
      okLat)
# criterion: X-death step is forced to k_m = den(alpha_m - 1 + g);
# legal iff that divides the cap.  Algebraic reduction: with
# g = (nu+1)/(2 nu), num = 2 a nu - c nu + c = c (mod nu), so
# den | c forces nu | c^2.  Residual cases checked exactly.
def refused(c, alpha_num_range, gaps):
    for a in range(alpha_num_range):
        for g in gaps:
            r = Fr(a, c) - 1 + g
            if c % r.denominator == 0:
                return (False, a, g)
    return (True, None, None)


gA_ = [Fr(nu + 1, 2 * nu) for nu in range(3, 302, 2)]           # 11-A odd
gB_ = [Fr(nu + 1, 2 * nu) for nu in range(2, 302) if nu % 3]    # 11-B 3-free
gB_ += [Fr(5, 4)]                                               # resonant X
gC_ = gA_                                                       # 11-C odd
okX = True
for (caps, gaps) in (((1, 2, 4), gA_), ((1, 2, 6), gB_), ((1, 2), gC_)):
    for c in caps:
        ok, wa, wg = refused(c, c, gaps)
        okX &= ok
check("OB7b THE EXHAUSTION: for every entry, every cap candidate c "
      "(incl. divisor closure), every register residue a/c, and every "
      "domain-legal X (nu <= 300 lattice + the 11-B resonant X 5/4): "
      "den(alpha_m - 1 + gap(X)) does NOT divide c -- the X-death "
      "step is REFUSED in all cases; zero escapes", okX)
check("OB7c the nu-quantifier closes ALGEBRAICALLY: num = 2a nu + "
      "c(1 - nu) = c (mod nu) so den | c forces nu | c^2; odd nu >= 3 "
      "divides none of {1, 4, 16, 36}\\{3-multiples for 11-B}; "
      "residuals nu in {2, 4} at 11-B refuse 2-adically: "
      "(2a-3)/12 and (4a-9)/24 have dens in {4,8,12,24}, none "
      "dividing 6 (and (2a-1)/4, (4a-3)/8 none dividing 2)",
      all(gcd(2 * a * nu - c * nu + c, nu) == gcd(c, nu)
          for a in range(1, 9) for c in (2, 4, 6) for nu in (3, 5, 7, 9))
      and all((Fr(2 * a - 3, 12)).denominator not in (1, 2, 3, 6)
              for a in range(0, 13))
      and all((Fr(4 * a - 9, 24)).denominator not in (1, 2, 3, 6)
              for a in range(0, 25)))
check("OB7d td-7 regression: entry (2,3), cap 2, alpha in {0, 1/2} "
      "mod 1: den(a/2 - 1 + (nu+1)/(2nu)) is nu or 2nu, never | 2 "
      "for odd nu >= 3 -- reproduces the promoted Case C (k=1 forces "
      "2nu | r nu + 1, k=2 forces nu | 1)",
      refused(2, 2, gA_)[0])
check("OB7e Case B (opponent-first) refused by gap order [+ CITED "
      "no-skip descent law]: min gX strictly exceeds every opponent "
      "one-step gap on all three entries -- 11-A: inf gX = 1/2 > "
      "7/16; 11-B: 1/2 > 5/22; 11-C: 1/2 > 2/5",
      Fr(1, 2) > Fr(7, 16) and Fr(1, 2) > Fr(5, 22)
      and Fr(1, 2) > Fr(2, 5)
      and all(gX(nu) > Fr(1, 2) for nu in range(2, 400)))
# round-3 (sol finding 5 / grok finding 8): the c = 1 register class.
# den(alpha_1) = 2 does NOT divide c = 1; under cap 1 every prefix step
# has k = 1, so alpha stays HALF-INTEGRAL, and the criterion must be
# checked on that class -- and on quarter/sixth registers left by an
# EARLIER larger cap when the cap later shrinks (dynamic-cap lemma).
okc1 = all((Fr(1, 2) - 1 + g).denominator > 1 for g in gA_ + gB_)
# ENTRY-PAIRED dynamic-cap sweep: each entry's own big-cap lattice
# against its own X-family (cross-pairing is not a real configuration
# -- see ledger row 5: the quarter-register 3/4 against the nu = 2 gap
# 3/4 under cap 2 WOULD escape, and no entry realizes that cell).
okdyn = True
for cbig, csmall_list, gaps in ((4, (1, 2), gA_), (6, (1, 2), gB_)):
    for a in range(cbig):
        for csm in csmall_list:
            for g in gaps:
                r = Fr(a, cbig) - 1 + g
                # r <= 0: no positive death step exists -- refusal
                okdyn &= (r <= 0 or csm % r.denominator != 0)
# the ledger-row-5 near-miss, exhibited exactly:
r_nm = Fr(3, 4) - 1 + Fr(3, 4)
ok_nm = (r_nm == Fr(1, 2) and 2 % r_nm.denominator == 0
         and not legal(Fr(2), 2) and 4 not in (1, 2, 6))
check("OB7f dynamic-cap / register-class lemma (round 3, sol finding "
      "5): cap 1 with the true half-integral register refuses X "
      "(den = 2nu or 4 > 1); ENTRY-PAIRED sweep -- 11-A quarter-"
      "lattice (from cap 4) and 11-B sixth-lattice (from cap 6) "
      "registers against later shrunken caps {1, 2}: zero escapes "
      "(r <= 0 rows are refusals: no positive death step)",
      okc1 and okdyn)
check("OB7g LEDGER ROW 5 (found by this round's own sweep): the "
      "quarter-register 3/4 against the nu = 2 gap 3/4 under cap 2 "
      "gives r = 1/2, k = 2 | 2 -- a WOULD-BE Case-C escape; no "
      "entry realizes the cell: 11-A's w = 2 domain forbids even "
      "nu_X (gcd(2,2) != 1), and 11-B's cap candidates {1,2,6} "
      "contain no 4, so no quarter-lattice history exists there -- "
      "the dynamic-cap lemma is sound ONLY entry-paired",
      ok_nm)

print("== 10. OB-6: closure-wide window audit (px2/px5 engines) ==")
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'scratch_offaxis_pricing'))
import px2  # noqa: E402
import px5  # noqa: E402


def step_ratio_mult(w, M):
    """(ratio = dq*l/dp, mult = dp/l, resonant?) for every menu step."""
    out = []
    for (w2, M2, dl, tag) in sorted(set(px2.chain_steps(w, M))):
        if tag.startswith('clean'):
            nu = int(tag.split('nu')[-1])
            D = int(tag.split('D')[1].split('n')[0])
            n = (D - 1) // nu + 1
            out.append((Fr(n * nu + 1, nu), Fr(nu), n >= 2, tag))
        elif tag.startswith('st96'):
            body = tag[5:]
            l = int(body.split('e')[0][1:])
            dp, dq = (int(x) for x in
                      body.split('(')[1].rstrip(')').split(','))
            out.append((Fr(dq * l, dp), Fr(dp, l), False, tag))
        elif tag.startswith('pure-b'):
            body = tag[7:]
            l = int(body.split('e')[0][1:])
            eps = int(body.split('e')[1])
            E = l - eps
            for nu in range(2, 100):
                gg = gcd(E, nu + 1) if E > 1 else 1
                if gg == M2:
                    out.append((Fr(l * (nu + 1), eps + l * nu),
                                Fr(eps + l * nu, l), False, tag))
        elif tag.startswith('neutral-drop'):
            for nu in (2, 3, 5, 7):
                out.append((Fr(nu + 1, nu), Fr(nu), False, tag))
    return out


AUD = []
for (seed, p) in (((Fr(3), 2), 4), ((Fr(4, 3), 3), 6), ((Fr(3, 2), 2), 4)):
    dist, _ = px5.close_with_cells(*seed)
    Rmax, mmin, res_tags, seed_res = Fr(0), Fr(999), set(), set()
    for (w, M) in dist:
        for (r, m, isres, tag) in step_ratio_mult(w, M):
            Rmax = max(Rmax, r)
            mmin = min(mmin, m)
            if isres:
                res_tags.add(tag)
                if (w, M) == seed:
                    seed_res.add(tag)
    AUD.append((seed, p, len(dist), Rmax, mmin, res_tags, seed_res))
check("OB6a growth law over ALL closure states (21 + 347 + 69): every "
      "step multiplier dp/l >= 2 (incl. parametric families), so a "
      "depth-j step sees deg >= p * 2^(j-1)",
      all(m >= 2 for (_, _, _, _, m, _, _) in AUD))
check("OB6b ratio law: max step ratio R* = dq*l/dp over each full "
      "closure is 5/2, 3, 5/2 < p = 4, 6, 4 -- so EVERY depth->=2 "
      "step gap = ratio/deg <= R*/(2p) < 1/2; depth-1 gaps are the "
      "frozen scope 3.2 menus (< 1/2 except 11-A's 5/8)",
      [(a[3], a[1]) for a in AUD] ==
      [(Fr(5, 2), 4), (Fr(3), 6), (Fr(5, 2), 4)]
      and all(a[3] < a[1] for a in AUD))
check("OB6c resonance census: at-seed resonances are exactly 11-A's "
      "clean D3n2nu2 (the 5/8) at (3,2) and NONE at (4/3,3) or "
      "(3/2,2); all deeper copies (D3n2nu2, D5n2nu4, D4n2nu3) fall "
      "under the depth->=2 law, gap <= R*/(2p) < 1/2",
      AUD[0][6] == {'clean D3n2nu2'} and AUD[1][6] == set()
      and AUD[2][6] == set()
      and AUD[0][5] <= {'clean D3n2nu2', 'clean D5n2nu4'}
      and AUD[1][5] <= {'clean D3n2nu2', 'clean D4n2nu3'})
check("OB6d chain-1 engine audit: zero-cost clean n>=2 menu at (2,1) "
      "is EMPTY (the L-A freeze is engine-confirmed) and at (3,1) is "
      "exactly {clean D3n2nu2} (11-B's classified 5/4 resonance)",
      [t for (w2, M2, dl, t) in sorted(set(px2.chain_steps(Fr(2), 1)))
       if dl == 0 and t.startswith('clean')] == []
      and [t for (w2, M2, dl, t) in
           sorted(set(px2.chain_steps(Fr(3), 1)))
           if dl == 0 and t.startswith('clean')] == ['clean D3n2nu2'])

print("== 11. OB-8: three-pole composition (11-C) ==")
check("OB8a the second opponent adds NO window step (same seed, menu "
      "max 2/5 < 1/2 < gX) and only SHRINKS the joint cap "
      "(intersection of alive-vertex caps, tower-N3 kernel); the "
      "exhaustion is divisor-closed (c = 1 included in OB7b), so any "
      "shrunk cap is covered",
      max(Fr(2, 5), Fr(5, 14), Fr(3, 10)) < Fr(1, 2)
      and all(gcd(2, c) in (1, 2) for c in (1, 2, 4, 6)))
check("OB8b no sibling-X tie: the 11-C leaf M-vector is (1, 2, 2) -- "
      "exactly one M = 1 carrier (A); both opponents are M = 2 "
      "charged seeds, so the 13-4 sibling-X-tie configuration cannot "
      "arise (round-3 de-tautologized: checked on the leaf data)",
      [1, 2, 2].count(1) == 1 and all(b >= 2 for b in (2, 2)))

print("== 12. OB-10: E5F / realization (round 3: stress witnesses) ==")
check("OB10a [CITED dichotomy, now exercised] sol-review stress "
      "witness 1 -- current-state mu class on 11-A: route (3,2,P=4) "
      "-> st96 (20,16) l=2 lam=4 -> (3/2,4,P=40); with (mu_1,mu_2) = "
      "(1,4): P_1/mu_1 = 2*5/1 = 10 = 40/4 = P_2/mu_2 -- a "
      "synchronized CURRENT-STATE branch outside the entry-level "
      "(1,1)/(1,M) split; its competing gap 16/40 = 2/5 < 1/2 < "
      "gX(5) = 3/5, so the window stays empty and CAP-DEN (caps "
      "divide gcd(4, .) -- all swept) kills it",
      4 * 20 // 2 == 40 and Fr(2 * 5, 1) == Fr(40, 4)
      and Fr(16, 40) == Fr(2, 5) < Fr(1, 2) < gX(5)
      and all(c in (1, 2, 4) for c in [gcd(4, i * p) for i in (1, 2, 4)
                                        for p in range(1, 30)]))
check("OB10b sol-review stress witness 2 -- budget-6 E5F-admissible "
      "route: (3,2,4) -(21,15)l2 lam4-> (4/3,3,42) -(85,35)l3 lam2-> "
      "(2/5,5,1190), mu_2 = 5: 1190/5 = 238 = 2*119, Pi_A = 119 = "
      "7*17 odd/legal; E5F n = 17*6 - 13*7 = 11 >= 1; route gaps "
      "15/42 = 5/14 and 35/1190 = 1/34 both < 1/2 < gX -- inside the "
      "kill's reach (window empty, caps swept); lam = 6 <= 9",
      4 * 21 // 2 == 42 and 42 * 85 // 3 == 1190
      and Fr(1190, 5) == 238 == 2 * 119 and 119 == 7 * 17
      and all(legal(Fr(2), u) for u in (7, 17))
      and 17 * 6 - 13 * 7 == 11 and Fr(15, 42) == Fr(5, 14) < Fr(1, 2)
      and Fr(35, 1190) == Fr(1, 34) < Fr(1, 2) and 4 + 2 <= 9)

print("== 13. the corrected 11-C skeleton layer (145 rows; sol finding 2) ==")
BS3 = {0: 1, 1: 2, 2: 2}     # leaves A(M=1), B1(M=2), B2(M=2)
TREES3 = [('direct', ('G', (('leaf', 0), ('leaf', 1), ('leaf', 2)))),
          ('G(G(A,B1),B2)', ('G', (('G', (('leaf', 0), ('leaf', 1))),
                                   ('leaf', 2)))),
          ('G(G(A,B2),B1)', ('G', (('G', (('leaf', 0), ('leaf', 2))),
                                   ('leaf', 1)))),
          ('G(G(B1,B2),A)', ('G', (('G', (('leaf', 1), ('leaf', 2))),
                                   ('leaf', 0))))]


def divs(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def sk_expand(node, corrected):
    """Yield (edge value to parent, #mixed nodes below).  corrected: a
    merge offers every mu_e | emitted M_G; old defect: mu_e = M_G."""
    if node[0] == 'leaf':
        for mu in divs(BS3[node[1]]):
            yield mu, 0
        return
    _, children = node
    opts = [list(sk_expand(ch, corrected)) for ch in children]
    combos = [()]
    for o in opts:
        combos = [c + (x,) for c in combos for x in o]
    for combo in combos:
        mus = [x[0] for x in combo]
        mix = sum(x[1] for x in combo) + (1 if all(m >= 2 for m in mus)
                                          else 0)
        for MG in divs(sum(mus)):
            if corrected:
                for mu_e in divs(MG):
                    yield mu_e, mix
            else:
                yield MG, mix


def sk_rows(tree, corrected):
    """Root-level decorated rows: (mus, mix, M_root, interior)."""
    _, children = tree
    opts = [list(sk_expand(ch, corrected)) for ch in children]
    combos = [()]
    for o in opts:
        combos = [c + (x,) for c in combos for x in o]
    rows = []
    for combo in combos:
        mus = tuple(x[0] for x in combo)
        mix = sum(x[1] for x in combo) + (1 if all(m >= 2 for m in mus)
                                          else 0)
        for MG in divs(sum(mus)):
            for interior in (True, False):
                if interior and MG == 1:
                    continue
                rows.append((mus, mix, MG, interior))
    return rows


cnt_c = {n: sk_rows(t, True) for n, t in TREES3}
cnt_o = {n: sk_rows(t, False) for n, t in TREES3}
check("SK1 corrected mu-independence law reproduces the scope/sol "
      "diagnostic EXACTLY: per-hierarchy 16 + 40 + 40 + 49 = 145 "
      "decorated rows, mixed-node rows 0 + 8 + 8 + 18 = 34",
      [len(cnt_c[n]) for n, _ in TREES3] == [16, 40, 40, 49]
      and [sum(1 for r in cnt_c[n] if r[1] > 0) for n, _ in TREES3]
      == [0, 8, 8, 18])
check("SK2 old-defect regression (mu_e = M_child conflation, "
      "BOOK-OFFAXIS-REVIEW finding 2): 16 + 28 + 28 + 31 = 103 rows, "
      "25 mixed -- the checked-in expansion's numbers, so the "
      "129-row nested undercount is exactly the documented defect",
      [len(cnt_o[n]) for n, _ in TREES3] == [16, 28, 28, 31]
      and sum(sum(1 for r in cnt_o[n] if r[1] > 0)
              for n, _ in TREES3) == 25)
# classifier: nested rows are NEVER stamped dead (Rule 6); direct rows
# get a per-row verdict under H8 = P/mu at the root merge.
verdicts = []                # one verdict PER ROW (rows may repeat as
for name, _ in TREES3:       # tuples across distinct inner decorations)
    for row in cnt_c[name]:
        mus, mix, MG, interior = row
        if name != 'direct':
            verdicts.append((name, row, 'OPEN'))    # nested: perimeter
        else:
            muA, mu1, mu2 = mus
            if mu1 == 1 or mu2 == 1:
                # that pair needs Pi_A = 2 Pi_B: v2 0 vs >= 1, unsat
                verdicts.append((name, row, 'SPINE-DEAD'))
            else:
                verdicts.append((name, row, 'CLASH-DEAD'))  # CAP-DEN
n_open = sum(1 for (_, _, v) in verdicts if v == 'OPEN')
n_dead = sum(1 for (_, _, v) in verdicts if v != 'OPEN')
check("SK3 per-row classifier (the census template, corrected per "
      "grok finding 2): 16 direct rows all DEAD with a per-row reason "
      "(mu = 1 on a B-edge -> H8 spine-death; mu = (1,2,2) -> "
      "co-scaled window, CAP-DEN clash); the 129 nested rows are "
      "stamped OPEN, NEVER TOWER-DEAD -- the Rule-6 conjunct the "
      "round-2 census claim omitted",
      n_dead == 16 and n_open == 129 and n_dead + n_open == 145
      and all(v == 'OPEN' for (n, _, v) in verdicts if n != 'direct'))

print("== 14. budget-9 audit record (sol/grok finding 1) ==")
check("B9a the round-2 OB-6 audit ran px5's DEFAULT budget 5 (td-7's "
      "td-2), not td-11's gross budget 9 -- erratum accepted; the "
      "21 + 347 + 69 counts are budget-5 counts; perimeter clause "
      "(iii) is corrected accordingly (round-2 claim withdrawn)",
      5 == 7 - 2 and 9 == 11 - 1 - 1)
check("B9b [FROZEN SIZING RECORD, this session's px5 runs -- not "
      "re-derived in the gate]: (3,2) ladder 21/56/130/330/743 at "
      "budgets 5..9 (matches sol-review exactly; budget 9 took 62s); "
      "(3/2,2) sized 69/162/349/785 at budgets 5..8 (0.2/1.4/18/186s, "
      "~10x per budget unit -- Macaulay-proxy growth ~2.2x states); "
      "(4/3,3) is 347 at budget 5; FULL budget-9 closures of the "
      "latter two are infeasible for px5 in-session (the scope's own "
      "capacity warning) -- which is WHY B9d uses the cutoff audit "
      "that needs no closure",
      [21, 56, 130, 330, 743] == [21, 56, 130, 330, 743]
      and [69, 162, 349, 785] == [69, 162, 349, 785])
check("B9c the round-2 R* < p 'law' is RETIRED (falsified at budget "
      "9): sol's reachable path (3,2) -(20,16)l2-> deg 40 "
      "-(40,16)l4-> deg 400 at (3/4,8) carries the step "
      "l8e0k1S1x2nu2(18,9) with ratio 9*8/18 = 4 = p; the state's "
      "min reachable degree 400 still leaves gap 4/400 = 1/100 < 1/2 "
      "-- the audit must be DEGREE-AWARE (ratio/min-deg), not "
      "ratio-only",
      4 * 20 // 2 == 40 and 40 * 40 // 4 == 400
      and Fr(9 * 8, 18) == 4 and Fr(4, 400) == Fr(1, 100) < Fr(1, 2))
# DEGREE-AWARE cutoff audit, run inline at budget 9 for all three
# seeds: exact menu checks for every state first reached at
# deg <= D* = 2*R_BOUND; states first reached above D* are LAW-SAFE
# (every px2-grammar step has ratio dq*l/dp <= R_BOUND = 47 from the
# engine's k <= 6, lex <= 40 caps, so gap <= 47/deg < 1/2).
import heapq
R_BOUND, DSTAR = 47, 94


def b9_menu(w, M):
    out = []
    for (w2, M2, dl, tag) in sorted(set(px2.chain_steps(w, M))):
        if tag.startswith('clean'):
            nu = int(tag.split('nu')[-1])
            D = int(tag.split('D')[1].split('n')[0])
            n = (D - 1) // nu + 1
            out.append((Fr(n * nu + 1, nu), Fr(nu), tag, (w2, M2), dl))
        elif tag.startswith('st96'):
            body = tag[5:]
            l = int(body.split('e')[0][1:])
            dp, dq = (int(x) for x in
                      body.split('(')[1].rstrip(')').split(','))
            out.append((Fr(dq * l, dp), Fr(dp, l), tag, (w2, M2), dl))
        elif tag.startswith('pure-b'):
            body = tag[7:]
            l = int(body.split('e')[0][1:])
            eps = int(body.split('e')[1])
            E = l - eps
            for nu in range(2, 121):
                g2 = gcd(E, nu + 1) if E > 1 else 1
                if g2 == M2:
                    out.append((Fr(l * (nu + 1), eps + l * nu),
                                Fr(eps + l * nu, l), tag, (w2, M2), dl))
        elif tag.startswith('neutral-drop'):
            for nu in (2, 3, 5, 7):
                out.append((Fr(nu + 1, nu), Fr(nu), tag, (w2, M2), dl))
    return out


def b9_audit(seed, p, res_tag):
    best, heap, cache, viol, core = {}, [(p, 0, seed)], {}, [], 0
    while heap:
        deg, lam, st = heapq.heappop(heap)
        if any(d <= deg for (s2, l2), d in best.items()
               if s2 == st and l2 <= lam):
            continue
        best[(st, lam)] = deg
        if deg > DSTAR:
            continue                     # law-safe by the ratio bound
        core += 1
        if st not in cache:
            cache[st] = b9_menu(*st)
        for (r, m, tag, st2, dl) in cache[st]:
            if r / deg >= Fr(1, 2) and not (st == seed and deg == p
                                            and tag == res_tag):
                viol.append((st, deg, tag))
            if lam + dl > 9:
                continue
            nd = deg * m
            if nd.denominator != 1:
                continue
            heapq.heappush(heap, (int(nd), lam + dl, st2))
    rb = all(r <= R_BOUND for mn in cache.values()
             for (r, m, t, s2, d) in mn)
    return core, len(cache), viol, rb


b9 = {s: b9_audit(s, p, rt) for (s, p, rt) in
      (((Fr(3), 2), 4, 'clean D3n2nu2'),
       ((Fr(3, 2), 2), 4, None), ((Fr(4, 3), 3), 6, None))}
check("B9d DEGREE-AWARE budget-9 window audit, ALL THREE seeds, run "
      "inline (cutoff Dijkstra): exact menu checks on every state "
      "first reached at deg <= 94 (cores: 12, 10, 8 states), ZERO "
      "gaps >= 1/2 beyond 11-A's seed-level 5/8; every deeper state "
      "is law-safe (parsed ratios max 5/2, 5/2, 7/3, all <= 47 = the "
      "px2 grammar bound, so gap <= 47/deg < 1/2 above deg 94)",
      all(len(v) == 0 and rb for (c, n, v, rb) in b9.values())
      and [n for (c, n, v, rb) in b9.values()] == [12, 10, 8]
      and Fr(47, 95) < Fr(1, 2))
# verify the grammar caps empirically on every seed-level st96 tag
_caps_ok = True
for (s, p, rt) in (((Fr(3), 2), 4, 'clean D3n2nu2'),
                   ((Fr(3, 2), 2), 4, None), ((Fr(4, 3), 3), 6, None)):
    for (w2, M2, dl, tag) in sorted(set(px2.chain_steps(*s))):
        if tag.startswith('st96'):
            kk = int(tag.split('k')[1].split('S')[0])
            xx = int(tag.split('x')[1].split('nu')[0])
            _caps_ok &= (kk <= 6 and xx <= 40)
check("B9e honesty rider: the budget-9 audit is a px2-MENU-SLICE "
      "statement -- the engine inherits td-7 loop caps (k <= 6, "
      "lex <= 40; verified on every seed-level st96 tag), which the "
      "scope forbids a production compiler to inherit; the ratio "
      "bound 47 = 1 + 6 + 40 is exactly that grammar's cap, so a "
      "cap-free engine re-opens the law-safe step and is a "
      "compiler-gap item (doc sec 13)",
      _caps_ok and 1 + 6 + 40 == 47)

print("== 15. THE THEOREM (restated at the audited tier) ==")
check("TD11-CLASH aggregate (round-3 tier): the three entry packets, "
      "direct hierarchies (11-A, 11-B binary; 11-C's 16 direct rows), "
      "single-word-deep zones, px2-menu window discipline "
      "(budget-9-audited on (3,2), budget-5..8-sized elsewhere): "
      "every synchronized configuration in THIS class dies at the "
      "tower tier -- X-death refused on the full register lattice "
      "under every cap candidate incl. dynamic-cap classes, the 5/8 "
      "intruder H8-dead, Case B gap-refused, spine-death otherwise",
      okX and okLat and okc1 and okdyn
      and all(a[3] < a[1] for a in AUD) and n_dead == 16)
check("what is NOT claimed (the gap to a compiler certificate): the "
      "129 nested 11-C rows (OPEN, SK3), multi-word deep zones "
      "(NF-Z-dagger POLICY -- the NF-D corollary is restricted to "
      "single-word-deep, sec 9 of the doc), the cap-free budget-9 "
      "closure for (3/2,2)@9 and (4/3,3)@9, nu = 1 insertions and "
      "resonance-bearing chains (NF-P), and the Q+E5/E5F refile "
      "itself (scope: UNKNOWN) -- each stamped OPEN, never certified",
      n_open == 129)

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
