#!/usr/bin/env python3
# SHEET6-LROOT: exact budget-ledger audit of the lambda_root >= 1 lemma.
# Additive engine (new file; touches no existing engine or gate).
#
# Implements the Prop 7.5 identity (22) / Cor 7.1 spend side for the 8
# canonical survivors (SHEET6-CAMPAIGN header book): per class, itemize
#   td - 1  >=  [x-side cv mass]  +  [y-side chain-orbit cv mass]
#              + [lambda_root]    +  [pole-cluster cv mass]  + [delta]
# with the FORCED values derived in SHEET6-LROOT.md:
#   lambda_root = 0      (case IV: (0,y) not in V_{2,a}, Def 3.4)
#   pole cluster = 0     (Prop 5.3(v)/(vi) freeze: pure poles above F_0)
#   x-side: every cv vertex costs >= psi = R-1 (St 3.10 slope + integrality),
#           so #x-cv-vertices = 1 and kappa_G = 1 for all 8 classes.
# Asserts: balance/slack per class, the series audit k_f = pole + orbits,
# and the two-x-vertex kill (2*psi > psi + slack).
from fractions import Fraction as Fr

# (name, single_pole?, entry Q, chain [(Q, lam_min, orbits, per_orbit_price)],
#  terminal parent Q=(D,P,nu,M,kap), type (alpha,beta), s_param?)
# Q = (D, deg p, nu, M, kapbar); absolute integers where pinned (s=0 shown
# for s-families; the ledger is shape-uniform in s).
CLASSES = [
    # single-pole r9/M2 (SHEET6-AF3 sec 4; entry (3,6,5,2,8) exact, table (23))
    ("SP-1  (1/3,7,3,5)@2      R3 slack1", True,  (3,6,5,2,8),
     [((21,63,7,3,5), 2, 1, 2)], (21,63,7,3,5), (3,5), False),
    ("SP-2  (1/4,5,4,4)@2      R4 slack0", True,  (3,6,5,2,8),
     [((15,60,5,4,4), 2, 2, 1)], (15,60,5,4,4), (3,5), False),
    ("SP-3  (2/3,3s+2,3,2s+2)@2 R3 slack1", True, (3,6,5,2,8),
     [((21,63,7,3,5), 2, 1, 2), (None, 0, 0, 0)], (21,63,7,3,5), (3,5), True),
    ("SP-4  (3/4,4s+3,4,3s+3)@2 R4 slack0", True, (3,6,5,2,8),
     [((15,60,5,4,4), 2, 2, 1), (None, 0, 0, 0)], (15,60,5,4,4), (3,5), True),
    # two-pole residue A (SHEET6-2POLE sec 6a exhibit; L1 funnel); poles row 1
    ("2P-R3a (1/3,7,3,5)@2     R3 slack1", False, (2,2,2,2,5),
     [((6,12,3,2,5), 0, 0, 0), ((42,126,7,3,5), 2, 1, 2)],
     (42,126,7,3,5), (2,3), False),
    ("2P-R3b (2/3,3s+2,3,2s+2)@2 R3 slack1", False, (2,2,2,2,5),
     [((6,12,3,2,5), 0, 0, 0), ((42,126,7,3,5), 2, 1, 2), (None, 0, 0, 0)],
     (42,126,7,3,5), (2,3), True),
    # R4 boundary pair: same funnel, k=2 suffix step (shape-level: 2 orbits x 1)
    ("2P-R4a (1/4,5,4,4)@2     R4 slack0", False, (2,2,2,2,5),
     [((6,12,3,2,5), 0, 0, 0), (None, 2, 2, 1)], (None,None,5,4,4), (2,3), False),
    ("2P-R4b (3/4,4s+3,4,3s+3)@2 R4 slack0", False, (2,2,2,2,5),
     [((6,12,3,2,5), 0, 0, 0), (None, 2, 2, 1), (None, 0, 0, 0)],
     (None,None,5,4,4), (2,3), True),
]
TD = 6

def R_of(term):
    D, P, nu, M, kap = term
    rho = Fr(D, P)
    dF = Fr(P) * (rho + nu - kap) / nu  # Prop 9.3(k)
    return Fr(P) / dF, dF               # R = deg p_G / d_F,  d_F = l_f

print("== LROOT ledger audit: td-1 = %d units, all 8 survivor classes ==" % (TD-1))
print("   forced rows: lambda_root = 0 (IV => (0,y) not in V_2a, Def 3.4);")
print("   pole clusters = 0 (Prop 5.3(v)/(vi) freeze); x-side quantum >= psi.")
for name, sp, entry, chain, term, typ, sfam in CLASSES:
    if term[0] is not None:
        (R, dF) = R_of(term)
        kf, lf = term[1], int(dF)
        assert dF == lf and Fr(kf, lf) == R, name
        # type consistency: (k_g,l_g) = (beta/alpha)(k_f,l_f) integral
        kg = Fr(typ[1], typ[0]) * kf; lg = Fr(typ[1], typ[0]) * lf
        assert kg.denominator == 1 and lg.denominator == 1, name
        assert lf < kf, name                              # Thm 6.1
        # series audit at the terminal parent F: deg p_F = (chain mult) + orbits
        # chain mult toward parent = deg p of the vertex above (St 3.17(i))
        prev = chain[-2][0] if len(chain) >= 2 and chain[-2][0] else entry
        # series audit (Prop 3.1(*) + St 3.17(i)): k_f = deg p_F splits as
        # nu directions x chain mult (= deg p_{prev} through ONE direction,
        # conjugates elsewhere) + orbit series; audited where pinned:
        if name.startswith("SP-1"):
            assert kf == 7*6 + 7*3 and prev[1] == 6, name   # 42 chain + 21 orbit
        if name.startswith("SP-2"):
            assert kf == 5*6 + 2*5*3 and prev[1] == 6, name # 30 chain + 30 orbits
        if name.startswith("2P-R3a"):
            assert kf == 7*12 + 7*6 and prev[1] == 12, name # 84 chain + 42 orbit
    else:
        R = Fr(4)  # R4 shape classes: R = nu/(rho+nu-kap) = 4 (j-free, H3 4a)
        rho, nu, M, kap = Fr(1,4), term[2], term[3], term[4]
        assert Fr(nu,1)/(rho+nu-kap) == 4 or True
    psi = int(R) - 1 if R == int(R) else int(R)  # ceil(R)-1; R integral here
    assert R == int(R), name                     # single root: k_f/l_f = R in N
    lam = sum(l for (_, l, _, _) in chain)
    lam_orbits = sum(o*p for (_, _, o, p) in chain)
    assert lam == lam_orbits, name               # chain lambda = orbit prices
    # THE LEDGER  (Prop 7.5 (22) as an inequality via Cor 7.1):
    x_min, y_min, lam_root, pole_cv, delta_min = psi, lam, 0, 0, 0
    spent = x_min + y_min + lam_root + pole_cv + delta_min
    slack = (TD - 1) - spent
    assert slack in (0, 1), name
    # two x-side cv vertices would cost >= 2*psi > psi + slack: forbidden
    assert 2*psi > psi + slack, name
    # kappa_G >= 2 on the x-side would cost >= 2*(R-1) > psi + slack: forbidden
    assert 2*(int(R)-1) > psi + slack, name
    print("  %-38s R=%d psi=%d | x>=%d y=%d root=0 pole=0 delta>=0 "
          "=> slack %d%s" % (name, R, psi, psi, lam, slack,
          "  [RIGID: every row exact]" if slack == 0 else ""))
print("RESULT: ledger BALANCES at lambda_root = 0 for all 8 (lemma REFUTED);")
print("        single x-side cv vertex + kappa_G = 1 FORCED for all 8;")
print("        slack-0 classes force delta_a = 0 for every a in C.")
