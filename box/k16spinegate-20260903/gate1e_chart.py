#!/usr/bin/env python3
"""GATE 1E: the section-2 model vs the FROZEN charged generator, t=2,3,4.

Reads t_order_system.build(t, gauged=True) and checks, with no preprocessing:
  E1  Q_chart = U(h) + A R(h) + y B  exactly (syntactic, all variables kept);
  E2  P_chart = V(h) + A S(h) + B T(h) + g z + a_{e,0} gamma;
  E3  after a_{e,0}=0, every charged equation at (h-power k, tag) equals
      [X^k] of the section-2 tag polynomial;
  E4  which charged rows contain a_{e,0}, i.e. what the "constant spine" must
      still do before the section-2 model applies.
"""
from __future__ import annotations
import sys
import sympy as sp

sys.path.insert(0, "/tmp/jc2-lane.nglVmb/inputs")
import t_order_system as tos

gamma, pi = tos.gamma, tos.pi
X = sp.Symbol("X")
fails = []


def check(name, cond):
    print(("PASS  " if cond else "FAIL  ") + name)
    if not cond:
        fails.append(name)


def basis_coeff(prefix, i, j):
    return sp.Symbol("%s%d_%d" % (prefix, i, j))


for t in (2, 3, 4):
    print("--- t=%d ---" % t)
    d = tos.build(t=t, gauged=True)
    e, q, h, A, B, z = d["e"], d["q"], d["h"], d["A"], d["B"], d["z"]
    asp, bsp = d["alpha_spaces"], d["beta_spaces"]

    def idx(space, target):
        for j, bb in enumerate(space):
            if sp.expand(bb - target) == 0:
                return j
        return None

    one = sp.Integer(1)
    # section-2 blocks as polynomials in X
    U = X**q + sum((basis_coeff("q", i, idx(bsp[i], one)) * X**(q - i)
                    for i in range(2, q + 1) if idx(bsp[i], one) is not None),
                   sp.Integer(0))
    R = sum((basis_coeff("q", i, idx(bsp[i], A)) * X**(q - i)
             for i in range(2, q + 1) if idx(bsp[i], A) is not None), sp.Integer(0))
    yB = [basis_coeff("q", i, idx(bsp[i], B))
          for i in range(2, q + 1) if idx(bsp[i], B) is not None]
    V = X**e + sum((basis_coeff("a", i, idx(asp[i], one)) * X**(e - i)
                    for i in range(1, e + 1) if idx(asp[i], one) is not None),
                   sp.Integer(0))
    S = sum((basis_coeff("a", i, idx(asp[i], A)) * X**(e - i)
             for i in range(1, e + 1) if idx(asp[i], A) is not None), sp.Integer(0))
    T = sum((basis_coeff("a", i, idx(asp[i], B)) * X**(e - i)
             for i in range(1, e + 1) if idx(asp[i], B) is not None), sp.Integer(0))
    gz = [basis_coeff("a", i, idx(asp[i], z))
          for i in range(1, e + 1) if idx(asp[i], z) is not None]
    gg = [basis_coeff("a", i, idx(asp[i], gamma))
          for i in range(1, e + 1) if idx(asp[i], gamma) is not None]
    check("E0 t=%d unique B-slot in Q, unique z- and gamma-slot in P" % t,
          len(yB) == 1 and len(gz) == 1 and len(gg) == 1)
    ysym, gsym, aeg = yB[0], gz[0], gg[0]
    print("      y=%s  g=%s  gamma-coeff=%s  x=q%d_%d  deg R=%d deg S=%d deg T=%d"
          % (ysym, gsym, aeg, t + 1, idx(bsp[t + 1], A),
             sp.Poly(R, X).degree(), sp.Poly(S, X).degree(),
             sp.Poly(T, X).degree()))
    check("E0b y = q_{2t+1,1}, g = a_{3t+1,3}",
          str(ysym) == "q%d_1" % q and str(gsym) == "a%d_3" % e)
    check("E0c deg R = t, deg S = 2t, deg T = t, C monic slot x = q_{t+1,1}",
          sp.Poly(R, X).degree() == t and sp.Poly(S, X).degree() == 2 * t
          and sp.Poly(T, X).degree() == t
          and str(basis_coeff("q", t + 1, idx(bsp[t + 1], A))) == "q%d_1" % (t + 1))

    sub_hX = {X: h}
    Qm = sp.expand(U.subs(sub_hX) + A * R.subs(sub_hX) + ysym * B)
    Pm = sp.expand(V.subs(sub_hX) + A * S.subs(sub_hX) + B * T.subs(sub_hX)
                   + gsym * z + aeg * gamma)
    check("E1 Q_chart == U(h) + A R(h) + y B", sp.expand(d["Q"] - Qm) == 0)
    check("E2 P_chart == V(h)+A S(h)+B T(h)+g z + a_{e,0} gamma",
          sp.expand(d["P"] - Pm) == 0)

    # E3: charged tag rows vs section-2 tag polynomials, at a_{e,0}=0.
    Up, Rp, Vp, Sp_, Tp = (sp.diff(w, X) for w in (U, R, V, S, T))
    b1, b2, b3, b4 = sp.symbols("b1 b2 b3 b4")
    Lx = X - b4
    y, g = ysym, gsym
    C12 = (-R * T + Lx * (R * Tp - 2 * Rp * T + 2 * y * Sp_) + y * S
           - b3 * (g * Rp + y * Tp) - 3 * g * Up)
    C11 = -2 * g * R + Lx * (2 * y * Tp - 3 * g * Rp)
    C00 = (Lx**2 * (Rp * S - R * Sp_)
           + Lx * (b3 * (Rp * T - y * Sp_) + 2 * b2 * (g * Rp - y * Tp)
                   + 2 * T * Up - 2 * y * Vp)
           + g * b3**2 * Rp + g * b2 * R + g * b3 * Up + b1 * g * y)
    C01 = ((b3 * y - Lx * R) * Vp + (Lx * S - b3 * T - b2 * g) * Up + g * y
           - b2 * C12 - b1 * C11)
    model = {(1, 2): C12, (1, 1): C11, (1, 0): -y * g,
             (0, 3): -C12, (0, 2): -b1 * C12 - C11, (0, 1): C01, (0, 0): C00}
    csym = d["c"]
    zero_ae = {aeg: 0}
    chart = {}
    for hpow, mono, coeff in d["tagged"]:
        chart[(hpow, mono)] = sp.expand(coeff.subs(zero_ae))
    mism, missing = [], []
    allkeys = set(chart)
    for mono, poly in model.items():
        pol = sp.Poly(sp.expand(poly), X)
        for k in range(0, pol.degree() + 1):
            want = sp.expand(pol.coeff_monomial(X**k))
            if mono == (1, 0) and k == 0:
                want = sp.expand(want - csym)   # the -c*gamma subtraction
            got = chart.get((k, mono), sp.Integer(0))
            allkeys.discard((k, mono))
            if sp.expand(got - want) != 0:
                mism.append((k, mono))
    check("E3 every section-2 [X^k] tag == the charged row (a_{e,0}=0)",
          not mism)
    if mism:
        print("      mismatched:", mism[:10])
    check("E3b no extra charged row outside the section-2 tag support",
          all(sp.expand(chart[kk]) == 0 for kk in allkeys))
    if any(sp.expand(chart[kk]) != 0 for kk in allkeys):
        print("      extra nonzero:", sorted(kk for kk in allkeys
                                             if sp.expand(chart[kk]) != 0)[:10])
    # E4: where does a_{e,0} live before the constant spine?
    rows_with = sorted((hp, mo) for hp, mo, cf in d["tagged"]
                       if aeg in cf.free_symbols)
    lin = [(hp, mo, sp.expand(sp.diff(cf, aeg)))
           for hp, mo, cf in d["tagged"] if aeg in cf.free_symbols]
    consts = [(hp, mo, cc) for hp, mo, cc in lin if cc.free_symbols == set()]
    print("      a_{e,0} occurs in %d charged rows; rows with CONSTANT "
          "a_{e,0}-coefficient: %s" % (len(rows_with), [(hp, mo, str(cc))
                                                        for hp, mo, cc in consts]))
    check("E4 a_{e,0} is solvable by a unit (constant) pivot before section 2",
          bool(consts))

print("GATE1E_DONE fails=%d" % len(fails))
if fails:
    print("FAILED:", fails)
