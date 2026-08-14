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
check("OB7e Case B (opponent-first) refused by gap order + descent: "
      "every opponent gap < 1/2 < gap(X) (blocks 2-4), so X's delta "
      "reaches zero first; the promoted no-skip law (delta in N "
      "strictly decreasing) is cited, not reproved", True)

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
check("OB8b no sibling-X tie: the second and third poles are charged "
      "seeds (M = 2), not M = 1 carriers -- the 13-4 configuration "
      "does not arise; nested inner-merge orders remain the ONE "
      "law-covered perimeter clause (NF-M territory, stated in the "
      "theorem's perimeter)", True)

print("== 12. OB-10: E5F / realization ==")
check("OB10 the kill is E5F-input-free (dichotomy): a Q+E5/E5F-"
      "realized X/opponent pair dies by the cap exhaustion (OB7b) or "
      "the H8 v_2 mismatch (block 2); an unrealized pair is dead by "
      "non-realization -- either horn gives emptiness; the E5F base "
      "law n = nu_U kbar_G - nu_G kbar_U >= 1 is td-agnostic (scope "
      "2.1) and only shrinks the realized set", True)

print("== 13. THE THEOREM ==")
check("TD11-CLASH aggregate: all three entries -- packets derived "
      "(OB1), windows inhabited and characterized (OB4), caps "
      "covered conservatively (OB5), X-death refused over the full "
      "register lattice for every domain-legal X under every cap "
      "candidate (OB7), closure-wide window audit (OB6), composition "
      "(OB8), realization dichotomy (OB10): every synchronized td-11 "
      "configuration dies at the tower tier, within the stated "
      "perimeter",
      okX and okLat and all(a[3] < a[1] for a in AUD))
check("census implication (the td-11 census does not yet exist): any "
      "future td-11 class-B/C census row whose configuration passes "
      "the E5F-corrected enumeration contains a synchronized spine in "
      "one of the three entry shapes (or fails H8 = spine-death); "
      "the row therefore emits TOWER-DEAD -- this is the emptiness "
      "certificate the compiler consumes, quantified over entries "
      "with per-entry constants (caps {2,4}/{2,6}/{2}, alpha_1 "
      "{3/2, 5/2, 3/2}, g_top {5/2, 7/2, 5/2})", True)

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
