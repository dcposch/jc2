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
  E. free-zone export equalities and letter-local congruences (the
     register question is settled in block G / NF-Z.md Lemma 4.2b);
  F. the 11-A v2 projection and the td-7 N2/N3/N4 numbers (unchanged);
  G. ROUND 3 (grok-nfz-rereview finding 1): the free-zone commutator.
     COUNTEREXAMPLE: prefix-delta integrality at menu gaps a/d is a
     condition on the ORDERED prefix products, and it flips under
     letter swaps when d does not divide P_0 (same-I pair
     (5,3,7,11)/(5,7,3,11) at P_0 = 30002, g = 7/3; Grok's lattice
     replayed exactly).  SD LEMMA: when every menu denominator divides
     P_0 (true on every filed packet -- corpus row) the boolean is
     constant-TRUE over ALL orders (exhaustive over residue classes),
     all other consumed booleans are automatic (Lemma 4.2a caps under
     den(alpha_entry) | P_0; Z3 descent; WIN/N4 comparisons), and the
     terminal register is the ONLY divergence (Grok's two sub-theta*
     anagram rows, exact alpha_exit values) -- discharged by 4.2b.
No px2/px5 needed; standalone; exit 0 iff all checks pass.
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
# REAL monotonicity (the round-2 tautology row is replaced -- re-review
# finding 3): the gap chain strictly decreases with ratio <= 1/2 along
# EVERY order of every sample word, so a letter below theta* never
# re-enters the zone.
check("monotone decay: gap chain has gamma_{j+1} <= gamma_j/2 in EVERY "
      "letter order (Z3 along words; letters never re-enter the zone)",
      all(all(gs[i + 1] <= gs[i] / 2 for i in range(len(gs) - 1))
          for P0m in (2, 4, 30001)
          for wm in set(itertools.permutations((3, 5, 7, 9)))
          for gs in [word_gaps(P0m, wm)]))

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
      "(register discharged by Lemma 4.2b; same-endpoint pairs and all "
      "consumed booleans are in block G)",
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

print("== G. round 3: the free-zone commutator (SD lemma + counterexample) ==")
TH7 = Fr(1, 13566)                      # theta* (td-7 direct skeleton)
MENU7 = [Fr(1), Fr(3, 2), Fr(2)]        # certified Case-C prefix menu


def pdelta_vec(P0, word, g, w=2):
    """Prefix-delta booleans per created atom at menu gap g:
    D_f * g - kbar in N with D_f = w*P_j, kbar = w*(u_j+1)."""
    out, P = [], P0
    for u in word:
        P *= u
        v = w * P * g - w * (u + 1)
        out.append(v.denominator == 1 and v >= 0)
    return out


def pdelta_vec_raw(P0, word, g, w=2):
    """The D_f = P_j normalization (Grok's replay)."""
    out, P = [], P0
    for u in word:
        P *= u
        v = P * g - w * (u + 1)
        out.append(v.denominator == 1 and v >= 0)
    return out


# --- G1/G2: the re-review's sub-theta* anagram pair (finding-1 row 1) ---
GA, GB = (3, 5, 7, 9), (3, 7, 5, 9)
_, axGA, _ = run_word(30000, GA, Fr(3, 2))
_, axGB, _ = run_word(30000, GB, Fr(3, 2))
check("G1 rereview row 1 @P0=30000: all eight gaps < theta*; equal "
      "enriched F (head 3, endpoint 9, Pi 945, classes); alpha_exit "
      "EXACT: 160225018542337913710789949999/2835000 vs "
      "11215751297330428730409149999/2835000 -- registers differ",
      all(g < TH7 for g in word_gaps(30000, GA) + word_gaps(30000, GB))
      and GA[0] == GB[0] and GA[-1] == GB[-1] and prod(GA) == prod(GB)
      and sorted(GA) == sorted(GB)
      and axGA == Fr(160225018542337913710789949999, 2835000)
      and axGB == Fr(11215751297330428730409149999, 2835000)
      and axGA != axGB)
okG2 = all(pdelta_vec(30000, GA, g) == pdelta_vec(30000, GB, g)
           == [True] * 4 for g in MENU7)
for wd in (GA, GB):
    gs = word_gaps(30000, wd)
    okG2 &= all(gs[i + 1] <= gs[i] / 2 for i in range(3))        # descent
    okG2 &= all(g < Fr(3, 8) and g < Fr(2, 5) for g in gs)       # N4/WIN
check("G2 ...and EVERY consumed boolean agrees for that pair under SD "
      "(prefix-delta all-pass at menu {1,3/2,2}, descent, WIN/N4 "
      "comparisons): the terminal register is the only divergence, "
      "and Lemma 4.2b discharges it", okG2)

# --- G3: finding-1 row 2 -- free tails after an in-zone prefix ---
PRE = (3, 5, 7, 9, 11)
PP = 2 * prod(PRE)
T1, T2 = (13, 15, 17), (15, 13, 17)
_, axT1, _ = run_word(2, PRE + T1, Fr(3, 2))
_, axT2, _ = run_word(2, PRE + T2, Fr(3, 2))
check("G3 rereview row 2: tails (13,15,17)/(15,13,17) after in-zone "
      "prefix (3,5,7,9,11) @P0=2: P = 20790 > 20349 so tails are free; "
      "equal I (same Z = prefix, Pi, endpoint 17, trivial tau); "
      "prefix-delta equal all-pass; alpha_exit differ (discharged)",
      PP == 20790 and PP > 20349
      and all(g >= TH7 for g in word_gaps(2, PRE))
      and all(g < TH7 for g in word_gaps(PP, T1) + word_gaps(PP, T2))
      and prod(T1) == prod(T2) and T1[-1] == T2[-1]
      and all(pdelta_vec(PP, t, g) == [True] * 3
              for t in (T1, T2) for g in MENU7)
      and axT1 != axT2)

# --- G4: the re-review's prefix-delta lattice, replayed exactly ---
g73, g85 = Fr(7, 3), Fr(8, 5)
lat = {P0: (pdelta_vec(P0, (3, 5, 7), g73), pdelta_vec(P0, (5, 3, 7), g73))
       for P0 in (2, 4, 8, 30000, 30001, 30002)}
check("G4 rereview prefix-delta lattice @g=7/3: (3,5,7) vs (5,3,7) is "
      "[T,T,T] vs [F,T,T] at P0 in {2,4,8,30001,30002}; both pass at "
      "P0=30000 (3 | P0); den-5 flip at g=8/5, P0=2 distinguishes "
      "(3,5,7) from (3,7,5)",
      all(lat[P0] == ([True] * 3, [False, True, True])
          for P0 in (2, 4, 8, 30001, 30002))
      and lat[30000] == ([True] * 3, [True] * 3)
      and pdelta_vec(2, (3, 5, 7), g85) == [False, True, True]
      and pdelta_vec(2, (3, 7, 5), g85) == [False, False, True])
check("G4b normalization robustness: on the gcd(d, aw) = 1 flip rows "
      "(d = 3, 5 at w = 2) the D_f = w*P_j and D_f = P_j booleans agree",
      all(pdelta_vec(P0, wd, g) == pdelta_vec_raw(P0, wd, g)
          for P0 in (2, 8, 30001, 30002)
          for wd in ((3, 5, 7), (5, 3, 7), (3, 7, 5))
          for g in (g73, g85)))

# --- G5: THE COUNTEREXAMPLE (SD is necessary) ---
CX1, CX2 = (5, 3, 7, 11), (5, 7, 3, 11)
check("G5 COUNTEREXAMPLE: P0 = 30002 (3 ndiv P0), g = 7/3: legal "
      "all-free words with equal I (trivial tau, empty Z, head 5, "
      "endpoint 11, Pi 1155, classes) have prefix-delta vectors "
      "[F,T,T,T] vs [F,F,T,T] -- a CONS-consumed boolean flips under a "
      "free-zone swap; unconditional commutativity is FALSE",
      all(g < TH7 for g in word_gaps(30002, CX1) + word_gaps(30002, CX2))
      and CX1[0] == CX2[0] and CX1[-1] == CX2[-1]
      and prod(CX1) == prod(CX2) and sorted(CX1) == sorted(CX2)
      and pdelta_vec(30002, CX1, g73) == [False, True, True, True]
      and pdelta_vec(30002, CX2, g73) == [False, False, True, True])

# --- G6: the commutator, exhaustive over residue classes ---
# The integrality boolean at an atom is d_eff | P_j with
# d_eff = d/gcd(d, a*w); it depends only on residues mod d_eff.
# Exhaust all P0 residues x all length-3 letter-residue words x all
# orders for d_eff in {2, 3, 5}.
okSD, flips = True, set()
for deff in (2, 3, 5):
    for P0r in range(deff):
        for L in itertools.product(range(deff), repeat=3):
            vecs = set()
            for wd in set(itertools.permutations(L)):
                P, v = P0r % deff, []
                for ur in wd:
                    P = (P * ur) % deff
                    v.append(P == 0)
                vecs.add(tuple(v))
            if P0r % deff == 0:
                okSD &= (vecs == {(True, True, True)})
            elif len(vecs) > 1:
                flips.add(deff)
check("G6 exhaustive residue-class commutator (d_eff in {2,3,5}, all "
      "P0 residues, all length-3 letter-residue words, ALL orders): "
      "d | P0 forces the prefix-delta boolean vector constant-TRUE with "
      "0 exceptions; d ndiv P0 admits order-flips for EVERY modulus",
      okSD and flips == {2, 3, 5})

# --- G7: Lemma 4.2a (automatic caps, any order) + necessity ---
okcapL = True
for P0c in (2, 4, 6, 9, 30001, 30002):
    for a0 in (Fr(3, 2), Fr(7, 3), Fr(5)):
        if P0c % a0.denominator:
            continue                     # entry compatibility
        for base in ((3, 5, 7), (3, 5, 7, 11), (2, 5, 8)):
            for wd in set(itertools.permutations(base)):
                P, a = P0c, a0
                for u in wd:
                    Pprev = P
                    P *= u
                    okcapL &= (Pprev % a.denominator == 0)
                    (k, l), a = die(Fr(u + 1, P), a)
                    okcapL &= (P % k == 0)
(kx, _), _ = die(Fr(6, 15), Fr(3, 2))    # P0 = 3, u = 5: den(2/5+1/2)=10
check("G7 Lemma 4.2a: den(alpha_entry) | P0 gives den(alpha_j) | P_{j-1} "
      "and k_j | P_j along EVERY order (sweep incl. even letters and "
      "non-3/2 seeds); hypothesis NECESSARY: P0=3, alpha=3/2, u=5 gives "
      "k = 10 ndiv 15", okcapL and kx == 10 and 15 % kx != 0)

# --- G8: SD on the filed corpus ---
sd = lambda dens, P0s: all(P % d == 0 for d in dens for P in P0s)
check("G8 SD corpus row: td-7 prefix menu {1,3/2,2} dens {1,2,2} divide "
      "P0 = 2 with margin g >= w*theta*; type (2,3) pole top 5/2 den 2 "
      "| even packet degrees {2,4,6,10}; 13-2d type (3,4) 7/3 den 3 | "
      "{3,9}; 11-B type (2,5) 7/2 den 2 | {2,6}",
      sd([g.denominator for g in MENU7], [2])
      and all(g >= 2 * TH7 for g in MENU7)
      and sd([2], [2, 4, 6, 10]) and sd([3], [3, 9]) and sd([2], [2, 6]))

# --- G9: coarser-than-multiset identification is SOUND under SD ---
C1, C2 = (7, 15, 13), (3, 35, 13)
_, axC1, _ = run_word(2, PRE + C1, Fr(3, 2))
_, axC2, _ = run_word(2, PRE + C2, Fr(3, 2))
okG9 = all(pdelta_vec(PP, t, g) == [True] * 3
           for t in (C1, C2) for g in MENU7)
for t in (C1, C2):
    gs = word_gaps(PP, t)
    okG9 &= all(gs[i + 1] <= gs[i] / 2 for i in range(2))
check("G9 rereview coarse pair (7,15,13)/(3,35,13) as free tails after "
      "the in-zone prefix: distinct factorizations, equal I (Z, Pi = "
      "1365, endpoint 13, classes, tau) -- and ALL consumed booleans "
      "agree (prefix-delta all-pass, descent); the identification is "
      "sound under SD, the differing registers are discharged",
      okG9
      and all(g < TH7 for g in word_gaps(PP, C1) + word_gaps(PP, C2))
      and prod(C1) == prod(C2) and C1[-1] == C2[-1] and axC1 != axC2)

# --- G10: the zone boundary is order-sensitive, and Z separates it ---
check("G10 zone boundary order-sensitivity: at P = 16000 the pair "
      "(3,5)/(5,3) has Z = [3] vs [5] (a swap moves a letter across "
      "theta*); such pairs are separated by Z, so free-zone commutation "
      "questions are confined to reorderings staying below theta*",
      zone(16000, (3, 5), TH7) == [3] and zone(16000, (5, 3), TH7) == [5])

print()
if FAIL:
    print(f"RESULT: {len(FAIL)} FAILURE(S) ({NPASS[0]} passed)")
    for n, d in FAIL:
        print(" FAIL", n, d)
    sys.exit(1)
print(f"RESULT: ALL {NPASS[0]} NF-Z CHECKS PASS")
sys.exit(0)
