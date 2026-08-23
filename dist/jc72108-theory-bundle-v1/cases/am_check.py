#!/usr/bin/env python3
"""am_check.py -- engine for AM-CHECK.md: Abhyankar-Moh one-place-at-infinity
semigroup instrument, run on the residue-A template's forced P-place Puiseux
characteristic data.

Pipeline (all exact, int/Fraction, no deps, < 1 s):
  1. derive the P_1/P_2 characteristic sequence from the promoted
     (kappa, nu, pi)-ladder (SHEET6-TEMPLATE.md sec 0 / sec 1a) and the chart
     registry pins (cases/r1_experiment.py:395-397, SHEET6-DIRECTIONB.md
     sec 0 / sec 7(4));
  2. forcedness sweep: the characteristic levels are invariant under every
     admissible on/off pattern of the free dead-stretch/tail coefficients;
  3. cross-anchor against every banked number: Newton pairs (7,2)(3,10)(2,5),
     cabling (2,52,317), local pairs (7,9)(3,10)(2,5), local cabling
     (9,199,1199) [SHEET6-CLASSICAL.md sec 1a, GROK-MONODROMY.md sec 1a],
     Milnor/conductor 2278 and delta 1139 [SHEET6-CLASSICAL.md sec 2a];
  4. run the AM one-place chain: divisibility d-chain, positivity
     precondition, AM inequality n_i*delta_i > delta_{i+1}, membership
     n_i*delta_i in <delta_0..delta_{i-1}>, plus the local (germ) dual axioms;
  5. fiber-tier one-place hypothesis test + AM degree corollary.
"""
from fractions import Fraction as Fr
from math import gcd

CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("%-62s %s%s" % (name, "PASS" if ok else "FAIL",
                          ("  " + detail) if detail else ""))
    return ok

def note(msg):
    print("  note: " + msg)

# ------------------------------------------------------------------ 1. derive
# Promoted ladder: SHEET6-TEMPLATE.md sec 0 (chain, pi, kappa) + sec 1a (nu):
KAPPA = 42
PI  = {"F_s": Fr(2, 7), "G_m": Fr(16, 21), "P": Fr(37, 42)}
NU  = {"F_s": 7, "G_m": 3, "P": 2}          # splitting index at each vertex
# Chart registry pins (r1_experiment.py:395-397; DIRECTIONB sec 0, sec 7(4)):
PIN_LEVELS  = (12, 32, 37)                  # coeffs eta_A(=1), alpha_i, w_i
FREE_LEVELS = (18, 24, 30, 34, 36)          # uf18/24/30, vf_i 34/36 (free)
TAIL_LO     = 38                            # free tails 38.. (registry)

lv = [KAPPA * PI[v] for v in ("F_s", "G_m", "P")]
check("C1  char levels = kappa*pi ladder -> (12, 32, 37)",
      all(x.denominator == 1 for x in lv) and tuple(int(x) for x in lv) == PIN_LEVELS,
      "kappa*pi = %s" % [str(x) for x in lv])

d_from_nu = [KAPPA]
for v in ("F_s", "G_m", "P"):
    assert d_from_nu[-1] % NU[v] == 0
    d_from_nu.append(d_from_nu[-1] // NU[v])
B = list(PIN_LEVELS)                        # characteristic t-levels
d_from_gcd = [KAPPA]
for b in B:
    d_from_gcd.append(gcd(d_from_gcd[-1], b))
check("C2  d-chain from nu-ladder == gcd-chain -> (42, 6, 2, 1)",
      d_from_nu == d_from_gcd == [42, 6, 2, 1], str(d_from_nu))

# ---------------------------------------------------- 2. forcedness sweep
def charlevels(support):
    d, out = KAPPA, []
    for l in sorted(support):
        if l % d:
            out.append(l)
            d = gcd(d, l)
    return tuple(out), d

ok = True
from itertools import combinations
free_pats = [frozenset(c) for r in range(6) for c in combinations(FREE_LEVELS, r)]
tail_pats = [frozenset(), frozenset(range(TAIL_LO, 61)), frozenset({38, 39, 43, 47})]
for fp in free_pats:
    for tp in tail_pats:
        cl, dfin = charlevels(set(PIN_LEVELS) | fp | tp)
        ok &= (cl == PIN_LEVELS and dfin == 1)
check("C3  char levels invariant over all free/tail on-off patterns",
      ok, "%d patterns" % (len(free_pats) * len(tail_pats)))
# counterfactuals (why the nonzero pins are load-bearing):
note("counterfactual alpha_i=0 (level 32 off): char levels -> %s" %
     (charlevels(set(PIN_LEVELS + FREE_LEVELS) - {32}),))
note("counterfactual w_i=0 (level 37 off):     char levels -> %s" %
     (charlevels(set(PIN_LEVELS + FREE_LEVELS) - {37}),))

# --------------------------------------- 3. Newton pairs / cabling anchors
e = d_from_gcd                              # e_0..e_3 = 42,6,2,1
p = [e[i] // e[i + 1] for i in range(3)]    # (7,3,2)
q = [B[0] // e[1]] + [(B[i + 1] - B[i]) // e[i + 2] for i in range(2)]
check("C4a Newton pairs (p,q) = (7,2)(3,10)(2,5) [banked CLASSICAL 1a]",
      (list(zip(p, q)) == [(7, 2), (3, 10), (2, 5)]), str(list(zip(p, q))))
# EN round-trip (GROK-MONODROMY 1a): m_1=p_1, m_{i+1}=m_i p_{i+1};
# beta_1=q_1, beta_{i+1}=beta_i p_{i+1}+q_{i+1}; char exps = beta_i/m_i.
m_en, b_en = [p[0]], [q[0]]
for i in (1, 2):
    m_en.append(m_en[-1] * p[i]); b_en.append(b_en[-1] * p[i] + q[i])
check("C4b EN round-trip m=(7,21,42), beta=(2,16,37), exps 12<32<37 /42",
      m_en == [7, 21, 42] and b_en == [2, 16, 37] and
      [Fr(b_en[i], m_en[i]) for i in range(3)] == [Fr(x, 42) for x in B])
a_cab = [q[0]]
for i in (1, 2):
    a_cab.append(q[i] + p[i - 1] * p[i] * a_cab[-1])
check("C5a cabling weights (2, 52, 317) [banked CLASSICAL 1a]",
      a_cab == [2, 52, 317], str(a_cab))
# local chart at [1:0:0] ((1/x, y/x): every contact +1 => levels +42):
Bl = [b + 42 for b in B]                    # (54, 74, 79)
ql = [Bl[0] // e[1]] + [(Bl[i + 1] - Bl[i]) // e[i + 2] for i in range(2)]
al_cab = [ql[0]]
for i in (1, 2):
    al_cab.append(ql[i] + p[i - 1] * p[i] * al_cab[-1])
check("C5b local pairs (7,9)(3,10)(2,5), cabling (9,199,1199) [banked]",
      list(zip(p, ql)) == [(7, 9), (3, 10), (2, 5)] and al_cab == [9, 199, 1199],
      "%s %s" % (list(zip(p, ql)), al_cab))

# ------------------------------------- 4. delta/value sequences, both charts
def delta_seq(d0, m):                       # AM approximate-root recursion
    """delta_0 = d0; delta_1 = m[0]; delta_{i+1} = n_i delta_i + m[i+1]-m[i]."""
    ds = [d0, m[0]]
    dd = [d0, gcd(d0, abs(m[0]))]
    for i in range(1, len(m)):
        n_i = dd[i - 1] // dd[i] if i > 1 else dd[0] // dd[1]
        # recompute n_i from the d-chain at step i:
        n_i = dd[i - 1] // dd[i]
        ds.append(n_i * ds[i] + (m[i] - m[i - 1]))
        dd.append(gcd(dd[i], abs(m[i])))
    return ds, dd

# at-infinity value form: T = x^{1/42} large parameter, w = T-degree;
# w(x) = 42, characteristic terms of y at T-degrees (-12, -32, -37):
r_inf, d_inf = delta_seq(42, [-12, -32, -37])
check("C6a value ladder at infinity r = (42, -12, -104, -317)",
      r_inf == [42, -12, -104, -317], str(r_inf))
check("C6b splice anchor |r_i| = a_i * d_{i+1} (ties delta to banked cabling)",
      [abs(r_inf[i + 1]) for i in range(3)] ==
      [a_cab[i] * d_from_gcd[i + 1] for i in range(3)])
# local germ form (center [1:0:0]): char exponents (54, 74, 79):
dl, d_loc = delta_seq(42, [54, 74, 79])
check("C6c local delta-sequence (42, 54, 398, 1199)",
      dl == [42, 54, 398, 1199], str(dl))
check("C6d local splice anchor |delta_i| = a_i^loc * d_{i+1}",
      dl[1:] == [al_cab[i] * d_from_gcd[i + 1] for i in range(3)])

cond = sum((d_from_gcd[i] - d_from_gcd[i + 1]) * Bl[i] for i in range(3)) - 42 + 1
check("C7  conductor/Milnor anchor mu = 2278, delta-inv = 1139, mu even",
      cond == 2278 and cond % 2 == 0 and cond // 2 == 1139, "mu = %d" % cond)

# --------------------------------------------- 5. the AM one-place chain
check("C8a divisibility chain d_{i+1} = gcd(d_i, delta_i), both charts",
      d_inf == d_loc == [42, 6, 2, 1])
check("C8b d-chain strictly decreasing to 1 (n_i = 7,3,2 all >= 2)",
      all(d_from_gcd[i] > d_from_gcd[i + 1] for i in range(3))
      and d_from_gcd[-1] == 1)

# binding one-place-at-infinity form needs all delta_i > 0:
pos_ok = all(x > 0 for x in r_inf)
check("C9a one-place positivity precondition on the actual value data",
      not pos_ok, "delta_1 = w(y) = -12 < 0: y -> 0 along the place; "
      "EXPECTED failure = the wrong-object certificate")

def semi_member(t, gens):
    reach = [False] * (t + 1); reach[0] = True
    for g in gens:
        for v in range(g, t + 1):
            reach[v] = reach[v] or reach[v - g]
    return reach[t]

# reflected |value| ladder (the only positive reading of the exponent data):
dp = [42, 12, 104, 317]
n = [d_from_gcd[i] // d_from_gcd[i + 1] for i in range(3)]     # n_1,n_2,n_3=7,3,2
marg_inf = [n[i - 1] * dp[i] - dp[i + 1] for i in (1, 2)]      # AM: need > 0
check("C9b AM inequality n_i*delta_i > delta_{i+1} on reflected ladder",
      not any(x > 0 for x in marg_inf),
      "margins (84-104, 312-317) = (%d, %d): VIOLATED at BOTH steps" %
      tuple(marg_inf))
marg_loc = [dl[i + 1] - n[i - 1] * dl[i] for i in (1, 2)]      # local: need > 0
check("C9c local germ axioms delta_{i+1} > n_i*delta_i (dual side)",
      all(x > 0 for x in marg_loc), "margins = (+%d, +%d)" % tuple(marg_loc))
check("C9d local membership n_i*delta_i in <delta_0..delta_{i-1}>",
      semi_member(n[0] * dl[1], [42]) and semi_member(n[1] * dl[2], [42, 54]),
      "378 = 9*42; 1194 = 22*42 + 5*54")
# margin identity: |margins| = exponent gaps = template edge lengths:
gaps = [B[1] - B[0], B[2] - B[1]]
edges = [10 * (42 // 21), 5 * (42 // 42)]   # TEMPLATE 1c: n=10 at 1/21, n=5 at 1/42
check("C9e |margins| = exponent gaps = edge lengths (20, 5)",
      [-x for x in marg_inf] == marg_loc == gaps == edges, str(gaps))

# --------------------------------- 6. fiber-tier hypothesis + AM corollary
# P1 != P2 as places: level-32 coefficients alpha_i, alpha_i^3 = a_i = 3+-sqrt3
a1 = (Fr(3), Fr(1))     # (rational, sqrt3-coefficient) exact in Q(sqrt3)
a2 = (Fr(3), Fr(-1))
diff = (a1[0] - a2[0], a1[1] - a2[1])
check("C10 fiber one-place hypothesis FALSE: P1 != P2 pinned (a1-a2 = 2*sqrt3)",
      diff != (0, 0) and diff == (0, 2),
      ">= 2 places forced; >= 4 per CLASSICAL sec 0; 2+r_B+42 generic")
check("C11 AM degree corollary: 168 !| 252, 252 !| 168, gcd = 84, type (2,3)",
      252 % 168 != 0 and 168 % 252 != 0 and gcd(168, 252) == 84
      and (168 // 84, 252 // 84) == (2, 3))

# ------------------------------------------------------------------ summary
fails = [nm for nm, ok in CHECKS if not ok]
print("\n%d checks, %d FAIL%s" % (len(CHECKS), len(fails),
      ("" if not fails else ": " + ", ".join(fails))))
print("characteristic sequence (P-place, forced): kappa = 42; "
      "t-levels (12, 32, 37); d-chain (42, 6, 2, 1)")
print("Newton pairs (7,2)(3,10)(2,5); value ladder (42, -12, -104, -317); "
      "local delta-seq <42, 54, 398, 1199>")
print("AM one-place inequality: inapplicable (delta_1 < 0), reflected form "
      "violated by (20, 5) = the edge lengths; local dual PASSES by (20, 5)")
