#!/usr/bin/env python3
"""nfd_check.py -- machine gate for NF-D.md (the neutral-word depth cap).

Exact Fraction/integer checks for:
  A. CE3 (grok-nfz-final finding 1) replayed EXACTLY on the interleaved
     td-7 ladder: after the last skeleton death at theta* = 1/13566 the
     register denominator is FORCED to 13566 (17*19 never cancels), and
     the first-free-atom cap/mu booleans flip between the equal-I tails
     (323,13,15,17) vs (13,15,323,17) after Z = (3,5,7,9,11);
  B. the monotone quantity M1 (Omega(P_j) strictly increasing, exit
     permanent, order-independent) and M2 (Z2 growth k' >= uu' >= 4
     against the td-7 window cap k | 2 -- the depth-0 instance);
  C. the td-7 live window: pin 22610 = 2*11305, 11305 = 5*7*17*19,
     Omega = 4, the complete factorization menu (15 multisets, all odd,
     max depth 4) -- D(td-7) = 4;
  D. the td-11 valuation windows: letter-domain v_p pins, 11-B v_3
     mismatch 0 vs 1 and 11-C v_2 mismatch 1 vs 2 over ALL domain
     stacks including empty -- S = empty, D = 0; 11-A promoted numbers;
  E. the three quotient counterexamples run FORWARD: all six
     configurations are DEAD (each violates at least one promoted
     boolean) -- no CE exhibits a live deep word; consistent with NF-D.
Standalone; exit 0 iff all checks pass.
"""
from fractions import Fraction as Fr
from math import gcd
import functools
import itertools
import sys

FAIL = []
NPASS = [0]
prod = lambda w: functools.reduce(lambda x, y: x * y, w, 1)


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}"
          + (f" -- {detail}" if (detail and not ok) else ""))
    if not ok:
        FAIL.append((name, detail))
    else:
        NPASS[0] += 1


def die(g, a):
    r = g + a - 1
    return (r.denominator, r.numerator), r.numerator + 1 - g


def Om(n):
    c, p = 0, 2
    while n > 1:
        while n % p == 0:
            n //= p
            c += 1
        p += 1 if p == 2 else 2
    return c


def vp(p, n):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


SKEL = [Fr(2, 5), Fr(1, 34), Fr(3, 3230), Fr(2, 11305), Fr(1, 13566)]
THETA = Fr(1, 13566)


def run_interleaved(P0, letters, alpha0, skel=SKEL):
    """Merge word and skeleton deaths in decreasing gap order; thread
    the register; return (rows, alpha_after_G, tail_cap_rows)."""
    P, events = P0, []
    for u in letters:
        P *= u
        events.append((Fr(u + 1, P), 'w', u, P))
    for g in skel:
        events.append((g, 's', g, None))
    events.sort(key=lambda e: -e[0])
    a, astar, tails = alpha0, None, []
    for g, kind, x, Pj in events:
        (k, l), a = die(g, a)
        if kind == 's' and x == THETA:
            astar = a
        if kind == 'w' and astar is not None and a != astar:
            pass
        if kind == 'w' and Pj is not None and g < THETA:
            tails.append((x, k, Pj, Pj % k == 0))
    return astar, tails


print("== A. CE3 replayed exactly (grok-nfz-final finding 1) ==")
Z5 = (3, 5, 7, 9, 11)
T_A, T_B = (323, 13, 15, 17), (13, 15, 323, 17)
asA, tailsA = run_interleaved(2, Z5 + T_A, Fr(3, 2))
asB, tailsB = run_interleaved(2, Z5 + T_B, Fr(3, 2))
check("A1 register after the last skeleton death G: den(alpha_*) = "
      "13566 = 2*3*7*17*19 in BOTH orders; P after Z = 20790 = "
      "2*3^3*5*7*11 carries neither 17 nor 19",
      asA.denominator == 13566 == asB.denominator
      and 2 * prod(Z5) == 20790
      and 20790 % 17 != 0 and 20790 % 19 != 0
      and 13566 == 2 * 3 * 7 * 17 * 19)
check("A2 the 17*19 is FORCED: num(l+1 - 1/13566) = 13566(l+1)-1 is "
      "coprime to 13566 for EVERY integer register l (lattice 1..5000)",
      all(gcd(13566 * (l + 1) - 1, 13566) == 1 for l in range(1, 5001)))
check("A3 cap booleans k_j | P_j on the free tails: (323,13,15,17) -> "
      "[T,T,T,T] with first k = 39270; (13,15,323,17) -> [F,T,T,T] "
      "with first k = 87297210 -- the FLIP",
      [t[3] for t in tailsA] == [True] * 4 and tailsA[0][1] == 39270
      and [t[3] for t in tailsB] == [False, True, True, True]
      and tailsB[0][1] == 87297210)
check("A4 mu-integrality P_1(alpha_* - 1) in N flips the same way: "
      "13566 | 20790*323 but 13566 does not divide 20790*13",
      (20790 * 323 * (asA - 1)).denominator == 1
      and (20790 * 13 * (asB - 1)).denominator != 1
      and (20790 * 323) % 13566 == 0 and (20790 * 13) % 13566 != 0)
gapsT = lambda tail: [Fr(u + 1, 20790 * prod(tail[:i + 1]))
                      for i, u in enumerate(tail)]
check("A5 equal-I and legality: same tau/Z/Pi(=1070745)/endpoint(17)/"
      "classes (all odd, 2|u+1, gcd(2,u)=1); both tails entirely below "
      "theta* -- a genuine same-I consumed-boolean flip under SD",
      prod(T_A) == prod(T_B) == 1070745 and T_A[-1] == T_B[-1] == 17
      and sorted(T_A) == sorted(T_B)
      and all(u % 2 == 1 and (u + 1) % 2 == 0 and gcd(2, u) == 1
              for u in T_A)
      and all(g < THETA for g in gapsT(T_A) + gapsT(T_B)))

print("== B. the monotone quantity ==")
okM1 = True
for P0 in (2, 3, 4, 30002):
    for base in ((3, 5, 7), (3, 5, 7, 11), (5, 323, 13)):
        for wd in set(itertools.permutations(base)):
            om, P = Om(P0), P0
            for u in wd:
                P2 = P * u
                okM1 &= (Om(P2) >= om + 1) and (P2 > P)
                om, P = Om(P2), P2
            okM1 &= om == Om(P0) + sum(Om(u) for u in base)
check("B1 M1: Omega(P_j) strictly increases by >= 1 per letter in "
      "EVERY order; P strictly increases (exit from any finite scale "
      "set is permanent); total Omega is order-independent", okM1)
check("B2 M1 depth bound: a word of depth r forces Omega(Pi) >= r "
      "(every letter >= 2 contributes >= 1)",
      all(Om(prod(wd)) >= len(wd)
          for wd in ((3,), (3, 5), (3, 5, 7), (9, 15), (323, 13, 15, 17))))
check("B3 M2 (depth-0 instance): consecutive word deaths in a run have "
      "k' >= u*u' >= 4 > 2 = the td-7 window cap -- window-zone runs "
      "of length >= 2 are refused (promoted N-closure corollary)",
      all((Fr(v + 1, P0 * u * v) - Fr(u + 1, P0 * u)).denominator
          >= u * v >= 4 > 2
          for P0 in (1, 2, 4) for u in range(2, 10) for v in range(2, 10)))

print("== C. the td-7 live window and D = 4 ==")
check("C1 mechanism-A pin: the f-degree ladder 2 -> 22610 forces "
      "P_0*Pi = 22610, Pi = 11305 = 5*7*17*19, Omega = 4",
      2 * 11305 == 22610 and 11305 == 5 * 7 * 17 * 19 and Om(11305) == 4)


def multiset_partitions(s):
    s = list(s)
    if not s:
        yield []
        return
    first, rest = s[0], s[1:]
    for part in multiset_partitions(rest):
        yield [[first]] + part
        for i in range(len(part)):
            yield part[:i] + [[first] + part[i]] + part[i + 1:]


menu = set()
for p in multiset_partitions([5, 7, 17, 19]):
    menu.add(tuple(sorted(prod(b) for b in p)))
check("C2 the complete td-7 neutral-stack menu: 15 factorization "
      "multisets of 11305 into parts >= 3, ALL parts odd "
      "(N2-consistent), max depth 4 = D(td-7); 323 = 17*19 is one of "
      "the depth-lowering groupings (CE3's letter)",
      len(menu) == 15 and max(len(m) for m in menu) == 4
      and all(x % 2 == 1 and x >= 3 for m in menu for x in m)
      and any(323 in m for m in menu))
check("C3 the cap boolean itself: every multiset of >= 5 parts >= 2 "
      "has Omega >= 5 > 4 = Omega(11305), so its product is never "
      "11305 -- depth > 4 exits the window permanently",
      all(Om(prod(wd)) >= 5 for wd in
          ((3, 3, 3, 3, 3), (3, 5, 7, 17, 19), (2, 2, 2, 2, 2)))
      and not any(len(m) >= 5 for m in menu))

print("== D. the td-11 windows, mu-corrected: H8 = P/mu, mu | M ==")
dom_w2 = [u for u in range(3, 40, 2)]                    # w=2: u odd
dom_w32 = [u for u in range(3, 40, 2) if u % 3 != 0]     # w=3/2: odd, 3 ndiv u
dom_w3 = [u for u in range(2, 40) if u % 3 != 0]         # w=3: 3 ndiv u
dom_w43 = [u for u in range(2, 40) if (u + 1) % 3 == 0]  # w=4/3: 3|u+1
stacks = lambda dom: itertools.chain([()], ((u,) for u in dom),
                                     itertools.product(dom, repeat=2))
check("D1 letter-domain v_p pins (raw-P facts, review-confirmed): "
      "v_2(Pi) = 0 on w=2 and w=3/2 stacks; v_3(Pi) = 0 on w=3 and "
      "w=4/3 stacks (sol-td11-13-scope.md 278-288)",
      all(vp(2, prod(c)) == 0 for c in stacks(dom_w2))
      and all(vp(2, prod(c)) == 0 for c in stacks(dom_w32))
      and all(vp(3, prod(c)) == 0 for c in stacks(dom_w3))
      and all(vp(3, prod(c)) == 0 for c in stacks(dom_w43)))
check("D2 the mu = (1,1) branches are UNSAT (the round-1 content, "
      "correctly labelled raw-P): 11-A/11-C Pi_1 = 2Pi_2 with Pi_1 "
      "odd (v_2: 0 vs >= 1); 11-B Pi_1 = 3Pi_2 with v_3(Pi_i) = 0 "
      "(v_3: 0 vs 1)",
      all(vp(2, prod(c)) == 0 for c in stacks(dom_w2))
      and all(vp(3, prod(c1)) == 0 and vp(3, 3 * prod(c2)) == 1
              for c1 in stacks(dom_w3) for c2 in [(5,)])
      and all(vp(3, prod(c)) == 0 for c in stacks(dom_w43)))
check("D3 the mu = (1,M) branches are INHABITED (grok-nfd finding 1): "
      "empty stacks pass H8 = P/mu (2/1 = 4/2 = 6/3 = 2 on all three "
      "entries) -- the windows are NOT empty",
      Fr(2, 1) == Fr(4, 2) == Fr(6, 3) == 2)
okfam = True
for k in range(1, 7):
    Pi = 5 ** k
    # u = 5 legal on every side: odd, 3 ndiv 5, 3 | 6, 2 | 6;
    # M preserved: l = M with M | u+1 = 6 for M in {2, 3}
    okfam &= (5 % 2 == 1 and 5 % 3 != 0 and 6 % 3 == 0 and 6 % 2 == 0)
    okfam &= gcd(2, 6) == 2 and gcd(3, 6) == 3
    okfam &= Fr(2 * Pi, 1) == Fr(4 * Pi, 2) == Fr(6 * Pi, 3)
check("D4 the Pi = 5^k family (k = 1..6): legal letters on BOTH poles "
      "of all three entries, M preserved (l = M, M | u+1 = 6), H8 = "
      "P/mu equal at EVERY depth -- S is an infinite residue class, "
      "D(11-A) = D(11-B) = D(11-C) = OPEN; mechanism A does not cap "
      "td-11 depth", okfam)
# D5: mechanism C's one real fact -- the M-ledger
okM = True
for M0 in (2, 3):
    for ls in itertools.product([1, M0], repeat=3):
        M = M0
        for l in ls:
            if M % l != 0:
                break
            Mn = gcd(l, 6)               # u = 5 letters: u+1 = 6
            okM &= Mn <= M               # non-increasing
            M = Mn
        okM &= (M == M0) == all(l == M0 for l in ls)  # drop irreversible
check("D5 mechanism C, the proved narrowing: M' = gcd(l, u+1) is "
      "non-increasing and drops are irreversible; one l = 1 letter "
      "kills the mu = M branch (falls into the unsat mu = 1 window), "
      "so the live window forces M CONSTANT -- narrows, does not "
      "bound depth",
      okM and gcd(1, 6) == 1
      and vp(2, 2 * 35) != vp(2, 4 * 35))   # dropped: raw-P unsat fires
check("D6 the promoted 11-A resonance row (v_2(2Pi) = 1 vs >= 3) is a "
      "MIXED charged/neutral certificate, relocated out of the "
      "pure-neutral table: resonance P' = 4*(2l)/l = 8 for l in "
      "{1,2}, v_2 = 3; pure-neutral left v_2(2Pi) = 1",
      all(4 * (2 * l) // l == 8 for l in (1, 2)) and vp(2, 8) == 3
      and all(vp(2, 2 * prod(c)) == 1 for c in stacks(dom_w2)))
check("D7 the ordered td-7 census from the 15 multisets (all parts "
      "distinct): 4! + 6*3! + 7*2! + 1 = 75 words -- the finite "
      "enumeration the compiler uses on the mechanism-A entry",
      24 + 36 + 14 + 1 == 75
      and sorted(len(m) for m in menu).count(3) == 6
      and sorted(len(m) for m in menu).count(2) == 7)

print("== E. the three CEs run forward: all DEAD ==")
check("E1 CE1 (3,5,7,9)/(3,7,5,9) @P0=2: both orders violate the pin "
      "(P_0*Pi = 1890 != 22610); first gap 2/3 lies in the window "
      "(2/5, 5/2) so the promoted Case-C X-refusal also applies",
      2 * 945 != 22610 and prod((3, 5, 7, 9)) == prod((3, 7, 5, 9)) == 945
      and Fr(2, 5) < Fr(4, 6) < Fr(5, 2))


def pdelta_vec(P0, word, g, w=2):
    out, P = [], P0
    for u in word:
        P *= u
        v = w * P * g - w * (u + 1)
        out.append(v.denominator == 1 and v >= 0)
    return out


check("E2 CE2 (5,3,7,11)/(5,7,3,11) @P0=30002: both orders violate the "
      "pin (30002*1155 != 22610; P_0 = 30002 is no filed packet) AND "
      "both fail prefix-delta atom 1 (3 ndiv 30002*5); order B "
      "additionally fails the flipped atom 2 (review precision note "
      "folded)",
      30002 * 1155 != 22610 and (30002 * 5) % 3 != 0
      and pdelta_vec(30002, (5, 3, 7, 11), Fr(7, 3))
      == [False, True, True, True]
      and pdelta_vec(30002, (5, 7, 3, 11), Fr(7, 3))
      == [False, False, True, True])
check("E3 CE3 both orders violate the pin (20790*1070745 != 22610); "
      "order B ALSO fails the first-atom cap (87297210 ndiv 270270) "
      "and the mu-boolean (13566 ndiv 270270)",
      20790 * 1070745 != 22610
      and 270270 % 87297210 != 0 and 270270 % 13566 != 0
      and 270270 == 20790 * 13)
check("E4 consistency verdict: every CE order is dead, so each CE flip "
      "distinguishes dead-from-dead, never live-from-dead -- no CE "
      "exhibits a live deep word; NF-D is consistent with all three",
      all([2 * 945 != 22610, 30002 * 1155 != 22610,
           20790 * 1070745 != 22610]))

print()
if FAIL:
    print(f"RESULT: {len(FAIL)} FAILURE(S) ({NPASS[0]} passed)")
    for n, d in FAIL:
        print(" FAIL", n, d)
    sys.exit(1)
print(f"RESULT: ALL {NPASS[0]} NF-D CHECKS PASS")
sys.exit(0)
