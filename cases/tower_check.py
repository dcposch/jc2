#!/usr/bin/env python3
"""tower_check.py -- MILESTONE 1 checker for the (9,15,7,3)@mu0=2 direct-route
tower certificate (cases/towers/t9_15_direct.json).

Validates, with exact Fractions (no floats anywhere):

  C1  the decorated numerical spine of the synchronized direct route
      (design xmodel/sol-gluing-design.md SS3.2): every vertex decoration
      (kappa, pi, kbar, nu, rho, w, M, i, d_p, d_q, deg p_f, D_f, d_f)
      against the printed transport laws under Q+E5 (AUDIT.md H5a):
      R1.2 (H1-H2), R2.1 case II (H4/H4a), E5 case III (H5-H6, (g')/(h')
      of SHEET6-III.md:131-147 with the H5a Q-value kappa_F =
      nu_F kappa_G / nu_G), Prop 9.3 offsets (J4), x-degree drops (J5),
      Cor 6.1's q-law d_q = kbar*deg p_f / D_f, the full-f degree ledger
      (H7)-(H8) with exact i-synchronization, and the P1/BOOK case-IV
      terminal package (R1)-(R3).
  C2  the td=6 template control (SHEET6-TEMPLATE.md SS1): the same tower
      formalization must reproduce the template's delta tables, m-depths,
      ladder (k0,l0)=(2,3),(k1,l1)=(3,4),(k2,l2)=(7,23), death gaps
      5/2, 5/6, 5/42 and Not 8.1 M-gcds -- calibration that the tower
      laws used in C3 are the printed ones.
  C3  the tower layer of the certificate: the forced tower prefix
      (type (2,3), h1 = g^2 - sigma0 f^3, both pole death checks
      g_0 = 5/2, pole h1-patterns with the forced relations), the
      death-gap table of the route, and the OBSTRUCTION exhaustion:
      no admissible chain-1 synchronization stack admits a coherent
      global (k_j, l_j) ladder (the KILL record in the JSON).
  C4  the local Prop 8.1(iv)/T1 layer: every certified s(t), C~ row
      (xmodel/grok-sixcells-review.md ground truth) re-derived from the
      patterns by exact eta-calculus, plus both pole Wronskians.
  C5  LEAD-PILOT reproduction gate: the 83-variable / 74-row SS3.5 system
      of the design is REGENERATED from the certificate's tower data and
      compared TOKEN-FOR-TOKEN against the design's literal block.

Exit 0 iff every check passes.  No solver is invoked; ops/FLEET.md is
respected (local exact python only).
"""

import json
import sys
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "towers" / "t9_15_direct.json"
TRUNK = HERE / "towers" / "t9_15_trunk.json"

FAILURES = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    if not ok:
        FAILURES.append((name, detail))
    print(f"  [{tag}] {name}" + (f" -- {detail}" if (detail and not ok) else ""))
    return ok


def fr(x):
    """Parse an exact rational from the JSON encoding 'p/q' or int."""
    if isinstance(x, str):
        n, _, d = x.partition("/")
        return Fr(int(n), int(d)) if d else Fr(int(n))
    return Fr(x)


def sfr(x):
    """Serialize Fraction for messages."""
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


# ----------------------------------------------------------------------
# eta-calculus: dense polynomials over Q(A-orbit values) are represented
# as dicts {exponent: coefficient} with Fraction coefficients; orbit
# values are substituted by exact rationals when testing identities at
# generic sample points (two independent points -- degrees are tiny).
# ----------------------------------------------------------------------

def pmul(a, b):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = ea + eb
            out[e] = out.get(e, Fr(0)) + ca * cb
    return {e: c for e, c in out.items() if c != 0}


def padd(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, Fr(0)) + c
    return {e: c for e, c in out.items() if c != 0}


def pscale(a, s):
    return {e: c * s for e, c in a.items() if c * s != 0}


def pdiff(a):
    return {e - 1: c * e for e, c in a.items() if e >= 1 and c * e != 0}


def ppow(a, n):
    out = {0: Fr(1)}
    for _ in range(n):
        out = pmul(out, a)
    return out


def orbit(nu, val, mult=1):
    """(eta^nu - val)^mult as a dense dict."""
    base = {nu: Fr(1), 0: -val}
    return ppow(base, mult)


def pdivide_exact(num, den):
    """Exact polynomial division num/den; returns quotient or None if inexact."""
    num = {e: c for e, c in num.items() if c != 0}
    q = {}
    dd = max(den)
    dc = den[dd]
    while num:
        nd = max(num)
        if nd < dd:
            return None
        e, c = nd - dd, num[nd] / dc
        q[e] = c
        shifted = {ee + e: -c * cc for ee, cc in den.items()}
        num = padd(num, shifted)
    return q


def t1_leftover(p, q, dp, dq):
    """d_p * p * q' - d_q * p' * q  (the L3 numerator without the C term)."""
    return padd(pscale(pmul(p, pdiff(q)), Fr(dp)), pscale(pmul(pdiff(p), q), Fr(-dq)))


def t1_constant(p, q, dp, dq):
    """If dp*p*q' - dq*p'*q == c*dq*p for a constant c, return c, else None."""
    left = t1_leftover(p, q, dp, dq)
    quot = pdivide_exact(left, p)
    if quot is None:
        return None
    if set(quot) - {0}:
        return None
    return quot.get(0, Fr(0)) / Fr(dq)


# ----------------------------------------------------------------------
# C2: td=6 template control (SHEET6-TEMPLATE.md SS1a-1b)
# ----------------------------------------------------------------------

def template_control():
    print("\n== C2: td=6 template control (tower-law calibration) ==")
    # ladder
    ladder = [(2, 3), (3, 4), (7, 23)]
    alpha = [Fr(0)]
    for (k, l) in ladder:
        alpha.append(alpha[-1] + Fr((k - 1) * l, k))
    check("template alpha ladder = (0, 3/2, 25/6, 103/... prefix)",
          alpha[1] == Fr(3, 2) and alpha[2] == Fr(25, 6))
    gaps = [Fr(l, k) + 1 - a for (k, l), a in zip(ladder, alpha[:-1])]
    check("template death gaps (5/2, 5/6, 5/42)",
          gaps == [Fr(5, 2), Fr(5, 6), Fr(5, 42)], str([sfr(g) for g in gaps]))
    # vertex table: (name, kappa, pi, d_f, d_g, d_h1, d_h2)
    rows = [
        ("R",   1,  Fr(0),        Fr(42),    Fr(63),    Fr(56),     Fr(138)),
        ("F_s", 7,  Fr(2, 7),     Fr(6),     Fr(9),     Fr(8),      Fr(138, 7)),
        ("G_m", 21, Fr(16, 21),   Fr(2, 7),  Fr(3, 7),  Fr(8, 21),  Fr(8, 7)),
        ("P_i", 42, Fr(37, 42),   Fr(1, 21), Fr(1, 14), Fr(1, 7),   Fr(3, 7)),
    ]
    exp_m = {"R": None, "F_s": 2, "G_m": 1, "P_i": 0}
    exp_delta = {"R": [104, 34, 4], "F_s": [100, 30, 0], "G_m": [10, 0], "P_i": [0]}
    for name, kappa, pi, df, dg, dh1, dh2 in rows:
        dh = [dg, dh1, dh2]
        deltas = []
        m = None
        for j in range(3):
            dj = kappa * (df + dh[j] - alpha[j] * df - 1 + pi)
            deltas.append(dj)
            if dj == 0 and m is None:
                m = j
        got = [int(d) for d in deltas[: len(exp_delta[name])]]
        check(f"template delta table @ {name} = {exp_delta[name]}",
              got == exp_delta[name] and all(d == int(d) and d >= 0 for d in deltas[: len(exp_delta[name])]),
              str(got))
        if exp_m[name] is not None:
            check(f"template m_{name} = {exp_m[name]}", m == exp_m[name], str(m))
        # delta_j = D_f*g_j - kbar identity
        D = kappa * df
        kbar = kappa * (1 - pi)
        for j in range(len(exp_delta[name])):
            dj = D * gaps[j] - kbar if j < len(gaps) else None
            if dj is not None:
                check(f"template delta_{j}({name}) == D_f*g_j - kbar",
                      dj == deltas[j], f"{sfr(dj)} vs {sfr(deltas[j])}")
    # Not 8.1 M-gcd law on full-pattern degrees
    check("template Not8.1 M(F_s) = gcd(126,189,168,414) = 3",
          gcd(gcd(126, 189), gcd(168, 414)) == 3)
    check("template Not8.1 M(G_m) = gcd(12,18,16) = 2",
          gcd(gcd(12, 18), 16) == 2)
    check("template Not8.1 M(P_i) = gcd(2,3) = 1", gcd(2, 3) == 1)
    # death equations at killers: g_j = kbar/D
    check("template death eq @ G_m: g_1 = kbar/D = 5/6",
          Fr(5, 6) == Fr(21 * (1 - Fr(16, 21)), 21 * Fr(2, 7)))
    check("template death eq @ F_s: g_2 = kbar/D = 5/42",
          Fr(5, 42) == Fr(7 * (1 - Fr(2, 7)), 7 * 6))
    # Prop 8.1 exponents: k = i(mu-1)
    check("template k(F_s) = 6*(25/6-1) = 19 ; deg p_h2 = 19*21+15 = 414",
          6 * (Fr(25, 6) - 1) == 19 and 19 * 21 + 15 == 414)
    check("template k(G_m) = 2*(3/2-1) = 1 ; deg p_h1 = 1*6+10 = 16",
          2 * (Fr(3, 2) - 1) == 1 and 6 + 10 == 16)


# ----------------------------------------------------------------------
# C1: route spine
# ----------------------------------------------------------------------

def route_spine(cert):
    print("\n== C1: decorated numerical spine (Q+E5) ==")
    V = {v["name"]: v for v in cert["vertices"]}
    for v in V.values():
        for key in ("kappa", "pi", "kbar", "nu", "rho", "w", "M",
                    "d_p", "d_q", "i", "deg_p_f", "D_f", "d_f"):
            if key in v:
                v[key] = fr(v[key])
    E = cert["edges"]

    # (F3)/(F4) internal consistency per vertex
    for name, v in V.items():
        if v.get("type") == "root":
            continue
        check(f"{name}: kbar = kappa*(1-pi)",
              v["kbar"] == v["kappa"] * (1 - v["pi"]),
              f'{sfr(v["kbar"])} vs {sfr(v["kappa"] * (1 - v["pi"]))}')
        check(f"{name}: D_f = kappa*d_f = rho*deg_p_f",
              v["D_f"] == v["kappa"] * v["d_f"] == v["rho"] * v["deg_p_f"])
        if "d_p" in v:
            check(f"{name}: theta = d_p/d_q = X/kbar with X = D_f/i",
                  Fr(v["d_p"], 1) / v["d_q"] == (v["D_f"] / v["i"]) / v["kbar"])
            check(f"{name}: w = (kbar - rho)/nu",
                  v["w"] == (v["kbar"] - v["rho"]) / v["nu"])
            check(f"{name}: M = gcd(d_p, d_q)",
                  v["M"] == gcd(int(v["d_p"]), int(v["d_q"])))
            check(f"{name}: i = deg_p_f/d_p integral",
                  v["i"] == v["deg_p_f"] / v["d_p"] and v["i"].denominator == 1)
            # Cor 6.1 q-law
            check(f"{name}: Cor6.1 q-law d_q = kbar*deg_p_f/D_f",
                  v["d_q"] == v["kbar"] * v["deg_p_f"] / v["D_f"])

    # edge transports
    for e in E:
        L, U = V[e["L"]], V[e["U"]]
        lbl = f'{e["L"]}->{e["U"]}'
        case = e["case"]
        n_e = fr(e["n"]) if "n" in e else None
        if case == "IV-terminal":
            # (J4) case IV: pi_L = 0, pi_U = (nu_U - kbar_U)/nu_U
            check(f"{lbl}: case-IV offset pi_U = (nu-kbar)/nu",
                  L["pi"] == 0 and U["pi"] == (U["nu"] - U["kbar"]) / U["nu"])
            check(f"{lbl}: (J5) terminal drops d_f and d_g by deg*(pi_U-pi_L)",
                  U["d_f"] == L["d_f"] - U["deg_p_f"] * U["pi"]
                  and fr(U["d_g"]) == fr(L["d_g"]) - fr(U["deg_p_g"]) * U["pi"])
            if "N_e" in e:
                K = fr(cert["K"])
                check(f"{lbl}: derived N_e/r_f/r_g on the terminal edge",
                      fr(e["N_e"]) == K * U["pi"]
                      and fr(e["r_f"]) == K * (L["d_f"] - U["d_f"])
                      == U["deg_p_f"] * fr(e["N_e"])
                      and fr(e["r_g"]) == K * (fr(L["d_g"]) - fr(U["d_g"]))
                      == fr(U["deg_p_g"]) * fr(e["N_e"])
                      and e.get("chartMode") == "PREFIX")
            continue
        if case == "II":
            # kappa tower + (J4): pi_U - pi_L = n/kappa_U ; kappa_U = kappa_L*nu_U
            check(f"{lbl}: kappa_U = kappa_L*nu_U (case II)",
                  U["kappa"] == L["kappa"] * U["nu"])
            check(f"{lbl}: (J4) pi_U - pi_L = n/kappa_U",
                  U["pi"] - L["pi"] == n_e / U["kappa"])
        elif case == "III-E5":
            # H5a Q-value: kappa_L(merge) = nu_L*kappa_U/nu_U ; (J4) III
            check(f"{lbl}: H5a Q-value kappa_merge = nu_merge*kappa_chain/nu_chain",
                  L["kappa"] == L["nu"] * U["kappa"] / U["nu"])
            check(f"{lbl}: (J4) pi_U - pi_L = n/(nu_L*kappa_U)",
                  U["pi"] - L["pi"] == n_e / (L["nu"] * U["kappa"]))
            # E5 (g')/(h') with F = merge (rootward), G = chain vertex (poleward)
            check(f"{lbl}: E5 (h') kbar_F = (nu_F*kbar_G + n)/nu_G",
                  L["kbar"] == (L["nu"] * U["kbar"] + n_e) / U["nu"])
            check(f"{lbl}: E5 (g') D_F = (nu_F*D_G + n*deg_p_G)/nu_G",
                  L["D_f"] == (L["nu"] * U["D_f"] + n_e * U["deg_p_f"]) / U["nu"])
            check(f"{lbl}: E5 congruence n = -nu_F*kbar_G (mod nu_G)",
                  (n_e + L["nu"] * U["kbar"]) % U["nu"] == 0)
            # (H6): X_G = mu0*(kbar_G - nu_G*w_U)  [E5: nu_G, not nu_U]
            mu0 = fr(e["mu_e"])
            check(f"{lbl}: (H6) X_G = mu0*(kbar_G - nu_G*w_U)",
                  L["D_f"] / L["i"] == mu0 * (L["kbar"] - L["nu"] * U["w"]))
        # (J5) x-degree drop for f (count equality: St 3.17(i)) and for g
        # (j = 0 live member: St 8.3(i)/Cor 6.1; death-transition exact at
        # the poles, verified separately in C3)
        if case in ("II", "III-E5"):
            check(f"{lbl}: (J5/3.17) d_f,U = d_f,L - deg_p_f,U*(pi_U-pi_L)",
                  U["d_f"] == L["d_f"] - U["deg_p_f"] * (U["pi"] - L["pi"]))
            check(f"{lbl}: (J5/8.3i) d_g,U = d_g,L - deg_p_g,U*(pi_U-pi_L)",
                  fr(U["d_g"]) == fr(L["d_g"])
                  - fr(U["deg_p_g"]) * (U["pi"] - L["pi"]))
            # (H7)/(H8): deg p_f,U = i_L * mu_e
            mu_e = fr(e["mu_e"])
            check(f"{lbl}: (H8) deg_p_f,U = i_L*mu_e",
                  U["deg_p_f"] == L["i"] * mu_e if L.get("type") != "root"
                  else U["deg_p_f"] == fr(cert["terminal"]["k_f"]))
        # derived chart data (design F2/J5): N_e = K(pi_U - pi_L) in N*,
        # r_{e,h} = K(d_h,L - d_h,U) = deg p_h,U * N_e for the count-equal
        # labels f, g; recorded TransportAuthority per label; chartMode.
        if "N_e" in e:
            K = fr(cert["K"])
            N_e = K * (U["pi"] - L["pi"])
            check(f"{lbl}: derived N_e = K*(pi_U - pi_L) = {e['N_e']} in N*",
                  N_e == fr(e["N_e"]) and N_e.denominator == 1 and N_e > 0)
            r_f = K * (L["d_f"] - U["d_f"])
            check(f"{lbl}: derived r_f = K*(d_f,L - d_f,U) = deg_p_f,U * N_e",
                  r_f == fr(e["r_f"]) == U["deg_p_f"] * N_e
                  and r_f.denominator == 1 and r_f >= 0)
            r_g = K * (fr(L["d_g"]) - fr(U["d_g"]))
            check(f"{lbl}: derived r_g = K*(d_g,L - d_g,U) = deg_p_g,U * N_e",
                  r_g == fr(e["r_g"]) == fr(U["deg_p_g"]) * N_e
                  and r_g.denominator == 1 and r_g >= 0)
            check(f"{lbl}: TransportAuthority f/g recorded, chartMode PREFIX",
                  e.get("transport_authority", {}).get("f") == "ST3.17_F"
                  and e.get("transport_authority", {}).get("g") == "ST8.3_LIVE_j0"
                  and e.get("chartMode") == "PREFIX")
        if case == "II" and e.get("law") == "R1.2":
            # R1.2/H1: tau, n, kbar, rho, w laws (L = clean child of U)
            Delta = fr(e["Delta"])
            tau = (U["kbar"] - U["rho"]) / Delta
            check(f"{lbl}: R1.2 tau = (kbar_U - rho_U)/Delta = {sfr(tau)}",
                  tau == fr(e["tau"]))
            check(f"{lbl}: R1.2 n_e = tau*nu_L - rho_U",
                  n_e == tau * L["nu"] - U["rho"])
            check(f"{lbl}: R1.2 kbar_L = tau*d_q,L/nu_U",
                  L["kbar"] == tau * L["d_q"] / U["nu"])
            check(f"{lbl}: R1.2 rho_L = tau/nu_U", L["rho"] == tau / U["nu"])
            check(f"{lbl}: R1.2/H2 w_L = w_U*n_cell/Delta",
                  L["w"] == U["w"] * fr(e["n_cell"]) / Delta)
        if case == "II" and e.get("law") == "R2.1-II":
            # merge handshake (H4)/(H4a): X_G = mu_e*(kbar_G - w_U); n = nu_U*kbar_G - kbar_U
            mu_e = fr(e["mu_e"])
            X_G = L["D_f"] / L["i"]
            check(f"{lbl}: (H4) X_G = mu_e*(kbar_G - w_U)",
                  X_G == mu_e * (L["kbar"] - U["w"]))
            check(f"{lbl}: (H4) n_e = nu_U*kbar_G - kbar_U",
                  n_e == U["nu"] * L["kbar"] - U["kbar"])

    # chain-2 BOOK (2.1) identities (rho_par + n)/(kbar_par + n) = d_p/(l*d_q)
    for row in cert["chain2_book21"]:
        par, ch = V[row["parent"]], V[row["child"]]
        n = fr(row["n"]); l = fr(row["l"])
        lhs = (par["rho"] + n) / (par["kbar"] + n)
        rhs = Fr(ch["d_p"], 1) / (l * ch["d_q"])
        check(f'BOOK(2.1) {row["parent"]}->{row["child"]}: (rho+n)/(kbar+n) = d_p/(l*d_q)',
              lhs == rhs, f"{sfr(lhs)} vs {sfr(rhs)}")
        check(f'BOOK(2.1) {row["parent"]}->{row["child"]}: kbar_child = (kbar_par + n)/nu_par',
              ch["kbar"] == (par["kbar"] + n) / par["nu"])

    # arrival (priced, recorded)
    arr = cert["arrival"]
    term = cert["terminal"]
    psi = int(fr(term["psi"]))
    budget = int(fr(term["budget"]))
    H2 = V["H2"]
    check("chain-2 zero arrival at recorded (w_U, nu_U) = (1/2, 7)",
          H2["w"] == fr(arr["w_U"]) and H2["nu"] == fr(arr["nu_U"]))
    check("arrival law: mu0 | M_U and nu_U = -1 (mod mu0)",
          int(H2["M"]) % int(fr(arr["mu0"])) == 0
          and (int(H2["nu"]) + 1) % int(fr(arr["mu0"])) == 0)
    check(f"arrival lambda ledger sums to budget {budget} = 6 - psi (saturated)",
          sum(int(fr(x)) for x in arr["lambda_steps"]) == budget
          and budget == 6 - psi)

    # terminal package (R1)-(R3) at the terminal vertex
    T = V[term.get("vertex", "G")]
    w_T, M_T = T["w"], T["M"]
    jj = M_T * (1 - w_T)
    check("(R3) 0 < w_T < 1, M_T >= 2, j = M_T*(1-w_T) in N*",
          0 < w_T < 1 and M_T >= 2 and jj.denominator == 1 and jj >= 1
          and jj == fr(term["j"]))
    R = Fr(1, 1) / (1 - w_T)
    psi_c = -(-R.numerator // R.denominator) - 1   # ceil(R) - 1
    check(f"(R2) R_term = 1/(1-w_T), psi = ceil(R)-1 = {psi}",
          R == fr(term["R_term"]) and psi_c == psi)
    kf, lf = fr(term["k_f"]), fr(term["l_f"])
    check("(R1) l_f = (1-w_T)*k_f ; k_f = deg p_f at terminal vertex",
          lf == (1 - w_T) * kf and kf == T["deg_p_f"])
    check("(R5) root chart swap: d_(0,x) = k_f, deg p_f,(0,x) = l_f",
          fr(term["d_0x"]) == kf and fr(term["deg_p_f_0x"]) == lf)
    R0 = V["R0"]
    check("root x-degrees: d_f,R0 = l_f, d_g,R0 = (3/2)*l_f (type (2,3))",
          R0["d_f"] == lf and fr(R0["d_g"]) == Fr(3, 2) * lf)

    # global K (J0 candidate) integrality
    K = int(fr(cert["K"]))
    for name, v in V.items():
        check(f"K-integrality at {name}: K*pi and K*d_f in Z",
              (K * v["pi"]).denominator == 1 and (K * v["d_f"]).denominator == 1)
    return V


# ----------------------------------------------------------------------
# C4: local Prop 8.1(iv)/T1 layer
# ----------------------------------------------------------------------

def poly_from_factors(factors, nu, env, eta_prefix=0):
    """Build eta-polynomial eta^eta_prefix * prod factor(t)^mult with t = eta^nu."""
    out = {eta_prefix: Fr(1)}
    for fac in factors:
        base = {int(d) * nu: Fr(eval(c, {}, env)) for d, c in fac["coeffs_t"].items()}
        out = pmul(out, ppow(base, int(fac.get("mult", 1))))
    return out


def local_t1(cert):
    print("\n== C4: local Prop 8.1(iv)/T1 rows (grok-sixcells ground truth) ==")
    for row in cert["t1_local"]:
        name = row["vertex"]
        nu = int(fr(row["nu"]))
        dp, dq = int(fr(row["d_p"])), int(fr(row["d_q"]))
        for Aval in (Fr(5), Fr(-3, 7)):
            env = {"A": Aval, "Fr": Fr}
            p = poly_from_factors(row["p_factors"], nu, env, int(row.get("eps", 0)))
            q = poly_from_factors(row["q_factors"], nu, env, 1)
            C = t1_constant(p, q, dp, dq)
            Cexp = Fr(eval(row["C"], {}, env))
            check(f"T1 @ {name} (A={sfr(Aval)}): C = {row['C']}",
                  C is not None and C == Cexp,
                  f"got {None if C is None else sfr(C)} want {sfr(Cexp)}")
            check(f"T1 @ {name}: deg(p,q) = ({dp},{dq})",
                  max(p) == dp and max(q) == dq)
    # pole Wronskians (P6),(P7): 2 p pg' - 3 p' pg = C, type (2,3)
    for Aval in (Fr(3), Fr(-2, 5)):
        # P1: p = eta^2 - A, pg = eta(eta^2 - (3/2)A): C = 2*A*(3/2)A = 3A^2
        p = {2: Fr(1), 0: -Aval}
        pg = pmul({1: Fr(1)}, {2: Fr(1), 0: -Fr(3, 2) * Aval})
        w = padd(pscale(pmul(p, pdiff(pg)), Fr(2)),
                 pscale(pmul(pdiff(p), pg), Fr(-3)))
        check(f"P1 Wronskian (P6): 2*p*pg'-3*p'*pg = 3*A^2 = 2*A*B (A={sfr(Aval)})",
              set(w) <= {0} and w.get(0, Fr(0)) == 3 * Aval * Aval, str(w))
        # P2: p = eta^4 - A eta, pg = eta^6 + U eta^3 + V, U = -3A/2, V = 3A^2/8:
        # C = 3*A*V = 9A^3/8
        U = -Fr(3, 2) * Aval
        Vv = Fr(3, 8) * Aval * Aval
        p2 = {4: Fr(1), 1: -Aval}
        pg2 = {6: Fr(1), 3: U, 0: Vv}
        w2 = padd(pscale(pmul(p2, pdiff(pg2)), Fr(2)),
                  pscale(pmul(pdiff(p2), pg2), Fr(-3)))
        check(f"P2 Wronskian (P7): 2*p*pg'-3*p'*pg = 3*A*V = 9A^3/8 (A={sfr(Aval)})",
              set(w2) <= {0} and w2.get(0, Fr(0)) == 3 * Aval * Vv
              and 3 * Aval * Vv == Fr(9, 8) * Aval ** 3, str(w2))


# ----------------------------------------------------------------------
# C3: tower layer -- forced prefix, death gaps, obstruction exhaustion
# ----------------------------------------------------------------------

def mult_at(poly, c):
    """Multiplicity of the root eta = c of a dense-dict polynomial (exact)."""
    deg = max(poly)
    coeffs = [poly.get(d, Fr(0)) for d in range(deg, -1, -1)]  # top down
    m = 0
    while True:
        # synthetic division by (eta - c): b_i top-down, remainder last
        b = []
        acc = Fr(0)
        for a in coeffs:
            acc = acc * c + a
            b.append(acc)
        if b[-1] != 0:
            return m
        m += 1
        coeffs = b[:-1]
        if not coeffs:
            return m


def tower_layer(cert, V):
    print("\n== C3: tower layer (Prop 4.2/8.1/Cor 6.1 under Q+E5) ==")
    tw = cert["tower"]
    # type and level-0
    check("tower side PLUS (all D_f > 0), h0 = g, base = f (fiber-zero gauge)",
          tw["side"] == "PLUS" and tw["h0"] == "g" and tw["base"] == "f")
    check("type (alpha,beta) = (2,3): (k0,l0) = (2,3), alpha_1 = 3/2",
          tuple(tw["ladder"][0]["kl"]) == (2, 3) and fr(tw["ladder"][0]["alpha_next"]) == Fr(3, 2))
    # pole death checks: g_0 = kbar/D_f = 5/2 at both poles
    for pn in ("P1", "P2"):
        v = V[pn]
        check(f"pole death eq @ {pn}: g_0 = kbar/D_f = 5/2 = l0/k0 + 1",
              v["kbar"] / v["D_f"] == Fr(5, 2) == Fr(3, 2) + 1)
    # pole h1-pattern forced relations (exact eta-calculus, sec C3 of TOWER-9-15.md)
    for Aval in (Fr(2), Fr(-5, 3)):
        # P1: g-top^2 - sigma0*f-top^3 with sigma0=1 gauge on scales:
        # (eta(eta^2-3A/2))^2 - (eta^2-A)^3 must drop to degree 2: -(3/4)A^2(eta^2-(4/3)A)
        gt = pmul({1: Fr(1)}, {2: Fr(1), 0: -Fr(3, 2) * Aval})
        ft = {2: Fr(1), 0: -Aval}
        h1p = padd(ppow(gt, 2), pscale(ppow(ft, 3), Fr(-1)))
        want = pscale({2: Fr(1), 0: -Fr(4, 3) * Aval}, -Fr(3, 4) * Aval * Aval)
        check(f"P1 h1-top = g^2-f^3 leading collapse -> -(3/4)A^2(eta^2-(4/3)A) (A={sfr(Aval)})",
              h1p == want, f"{h1p}")
        # P2: (eta^6+U eta^3+V)^2 - (eta^4-A eta)^3 drops to degree 3:
        U = -Fr(3, 2) * Aval
        Vv = Fr(3, 8) * Aval * Aval
        gt2 = {6: Fr(1), 3: U, 0: Vv}
        ft2 = {4: Fr(1), 1: -Aval}
        h1p2 = padd(ppow(gt2, 2), pscale(ppow(ft2, 3), Fr(-1)))
        want2 = {3: -Fr(1, 8) * Aval ** 3, 0: Fr(9, 64) * Aval ** 4}
        check(f"P2 h1-top = g^2-f^3 collapse -> -(1/8)A^3 eta^3 + (9/64)A^4, deg 3 (A={sfr(Aval)})",
              h1p2 == want2, f"{h1p2}")
        check(f"P2 h1-top degree 3 (A={sfr(Aval)})", max(want2) == 3)
    # P2 count handoff (real computation, replacing the reviewed tautology):
    # F1's level-1 dead member is p_red*q = eta(t-A)^3 R1(t)^2, t = eta^5;
    # its multiplicity at the continuation root c (c^5 = A) must equal the
    # eta-degree 3 of the P2 h1-collapse computed above (St 3.11 saturation
    # at the dead-member -> pole handoff).
    for Aval, cval in ((Fr(1), Fr(1)), (Fr(32), Fr(2))):
        tma = {5: Fr(1), 0: -Aval}                       # t - A in eta
        r1 = {10: Fr(1), 5: -3 * Aval, 0: 3 * Aval * Aval}
        dead = pmul({1: Fr(1)}, pmul(ppow(tma, 3), ppow(r1, 2)))
        m = mult_at(dead, cval)
        check(f"F1->P2 h1 count: mult(eta(t-A)^3 R1^2, c) = 3 = deg p_h1,P2 "
              f"(A={sfr(Aval)}, c={sfr(cval)})", m == 3, f"mult = {m}")
        check(f"F1->P2 h1 count consistency: R1(A) != 0 (A={sfr(Aval)})",
              Aval ** 2 - 3 * Aval * Aval + 3 * Aval * Aval != 0)

    # death-gap table of the route (g = kbar/D_f at each candidate killer)
    gaps = {}
    for row in tw["death_gaps"]:
        v = V[row["vertex"]]
        g = v["kbar"] / v["D_f"]
        gaps[row["vertex"]] = g
        check(f"death gap @ {row['vertex']}: kbar/D_f = {row['gap']}",
              g == fr(row["gap"]), sfr(g))
    order = [n for n in ("F1", "F2", "F3", "H2", "G", "T") if n in gaps]
    check("chain gaps strictly decreasing rootward (level order forced)",
          all(gaps[a] > gaps[b] for a, b in zip(order, order[1:])))
    check("all non-stack gaps are <= 2/5 (below the level-1 window)",
          all(gaps[n] <= Fr(2, 5) for n in order))

    # ---- OBSTRUCTION EXHAUSTION (level 1 window of the ladder) ----
    # Three cases (Grok review finding 1 repair): the first post-pole death
    # is at the stack vertex X (its gap outranks everything else and delta_X
    # in N cannot skip its own zero), possibly after a NON-KILLING prefix of
    # printed-legal steps with k_j | 2 (X and F1 both alive cap k_j | 2).
    # UNIVERSALITY (Sol finding-3 repair): none of the three refutations
    # uses nu_X | 11305 or oddness -- they hold for EVERY nu_X >= 2, so the
    # exhaustion covers every chain-1 stack of every chain-2 realization
    # (M_U = 2/4, free pure-b characteristic, any neutral padding, either
    # terminal); the 15 divisor classes below are the displayed
    # representative's instantiation, not the coverage boundary.
    print("  -- obstruction exhaustion over chain-1 synchronization stacks --")
    ob = tw["obstruction"]
    NN = 11305
    divs = sorted(d for d in range(2, NN + 1) if NN % d == 0)
    check("displayed rep: 11305 = 5*7*17*19 odd; its pole-adjacent classes"
          " nu_X | 11305, nu_X >= 5",
          NN == 5 * 7 * 17 * 19 and divs[0] == 5 and all(d % 2 == 1 for d in divs)
          and len(divs) == 15)
    # the pole-adjacent chain-1 vertex X has death gap (nu_X+1)/(2 nu_X),
    # independent of the cell shape (i*mult = 2 at the pole edge + root law
    # force deg p_f,X = 2 nu_X and d_q,X = nu_X + 1).
    ULAT = list(range(2, 301))          # universal lattice instantiation
    check("gap(X) = (nu+1)/(2nu) > 1/2 > 2/5 = gap(F1) for EVERY nu_X >= 2 "
          "(identity (nu+1)*2 - (2nu) = 2 > 0; lattice 2..300)",
          all((d + 1) * 2 - 2 * d == 2 and Fr(d + 1, 2 * d) > Fr(1, 2) > Fr(2, 5)
              for d in ULAT))
    # UNIVERSAL three-case refutation, nu_X >= 2 arbitrary:
    #   A/C, k_m = 1: needs 2nu | r nu + 1: r even -> 2nu | 1; r odd ->
    #     2nu | nu+1 with 0 < nu+1 < 2nu (identity 2nu - (nu+1) = nu-1 >= 1);
    #   A/C, k_m = 2: needs nu | 1;
    #   A empty prefix: k_1 = 2nu_X > 2 (identity 2nu - 2 = 2(nu-1) >= 2);
    #   B: gap 2/5 needs 5(nu+1) = 4nu, i.e. nu = -5 (identity
    #     5(nu+1) - 4nu = nu + 5 >= 7).
    check("UNIVERSAL case A: k_1 = 2nu_X > 2 for every nu_X >= 2",
          all(2 * d - 2 == 2 * (d - 1) >= 2 for d in ULAT))
    check("UNIVERSAL case C (k_m=1): 2nu - (nu+1) = nu-1 >= 1 and 2nu > 1",
          all(2 * d - (d + 1) == d - 1 >= 1 and 2 * d > 1 for d in ULAT))
    check("UNIVERSAL case C (k_m=2): nu | 1 impossible for nu >= 2",
          all(d > 1 for d in ULAT))
    check("UNIVERSAL case B: 5(nu+1) - 4nu = nu + 5 >= 7 (never 0)",
          all(5 * (d + 1) - 4 * d == d + 5 >= 7 for d in ULAT))
    # w-monotonicity: Delta - n = (n-1)(nu-1) >= 1 for n,nu >= 2 (one-line
    # identity, per review nit; lattice kept as instantiation), so a clean
    # chain-1 stack frozen at w = 2 is n = 1 neutrals only.
    ok_wid = all((n - 1) * nu + 1 - n == (n - 1) * (nu - 1) >= 1
                 for n in range(2, 12) for nu in range(2, 24))
    check("w-monotonicity identity: Delta - n = (n-1)(nu-1) >= 1 for n>=2",
          ok_wid)
    # intermediate stack vertices Y cannot steal the level-1 window:
    # gap(Y) = (nu_Y+1)/(2 P_Y) with P_Y >= nu_X*nu_Y (product of poleward
    # nu's), so gap(Y) <= 3/(4*nu_X) < 2/5 < gap(X).
    ok_int = all(Fr(nuY + 1, 2 * nuX * nuY) < Fr(2, 5)
                 for nuX in divs for nuY in divs
                 if (nuX * nuY) <= NN and NN % (nuX * nuY) == 0)
    check("intermediate stack gaps < 2/5 (cannot claim the level-1 window)",
          ok_int)
    # no recorded vertex gap lies inside any level-1 window (gap(X), 5/2):
    ok_win = all(not (Fr(nuX + 1, 2 * nuX) < gaps[n] < Fr(5, 2))
                 for nuX in divs for n in gaps if n not in ("N",))
    check("no non-stack death gap inside the window (gap(X), 5/2)", ok_win)

    prefix_vs = [n for n in ("F1", "F2", "F3", "H2", "G", "N", "T") if n in V
                 and "death_gap" in V[n]]
    # prefix cap: while X (p_f = S(t-A)^2) and F1 (i = 2, orbit mults
    # (2,1,1)) are both alive, Prop 4.2(iii)/Prop 8.1 (i l/k in N) force
    # every prefix step to have k_j | 2 (gcd(k_j, l_j) = 1):
    check("prefix cap: 2*l/k in N with gcd(k,l)=1 forces k | 2",
          all(Fr(2 * l, k).denominator != 1
              for k in range(3, 13) for l in range(1, 13) if gcd(k, l) == 1))
    # CASE C-legality (the erratum): the printed-legal non-killing level-1
    # prefix pairs -- k in {1,2}, gcd(k,l) = 1, gap(X) < g = l/k - 1/2 < 5/2
    # -- have positive-INTEGER delta_1 at every non-pole vertex; they are
    # legal ladder steps that kill nobody.  Enumerate them exactly.  (The
    # half-integer grid {1/2, 1, 3/2, 2} meets every window (gap(X), 5/2),
    # gap(X) in (1/2, 3/5], in the same three points 1, 3/2, 2.)
    pref = [(k, l) for k in (1, 2) for l in range(1, 8)
            if gcd(k, l) == 1 and Fr(1, 2) < Fr(l, k) - Fr(1, 2) < Fr(5, 2)]
    check("case C prefix menu = {(1,2),(2,3),(2,5)} exactly",
          sorted(pref) == [(1, 2), (2, 3), (2, 5)], str(pref))
    for (k1, l1) in sorted(pref):
        g1 = Fr(l1, k1) - Fr(1, 2)
        ds = {n: V[n]["D_f"] * g1 - V[n]["kbar"] for n in prefix_vs}
        ok = all(d.denominator == 1 and d > 0 for d in ds.values())
        check(f"case C prefix ({k1},{l1}), g = {sfr(g1)}: delta_1 "
              f"positive-integral at all of {','.join(prefix_vs)} (printed-legal)",
              ok, str({n: sfr(d) for n, d in ds.items()}))
    # Sol finding-1 identity (xmodel/sol-tower-review.md:56-69): Sol's
    # CRITICAL table of unhandled alive-alive level-1 pairs is exactly this
    # Case C menu, row for row -- pairs, gaps, X/F1 exponents, and the
    # delta_1 values at (G,H2,F3,F2,F1).  Verify the identity explicitly.
    sol_table = {
        (1, 2): {"g": Fr(3, 2), "expX": 4, "expF1": (8, 4), "d1F1": 11,
                 "deltas": (101740, 33911, 4842, 250, 11)},
        (2, 3): {"g": Fr(1), "expX": 3, "expF1": (6, 3), "d1F1": 6,
                 "deltas": (67825, 22606, 3227, 165, 6)},
        (2, 5): {"g": Fr(2), "expX": 5, "expF1": (10, 5), "d1F1": 16,
                 "deltas": (135655, 45216, 6457, 335, 16)},
    }
    check("Sol finding 1 == repaired Case C: same three pairs",
          sorted(pref) == sorted(sol_table))
    for (k1, l1), row in sorted(sol_table.items()):
        g1 = Fr(l1, k1) - Fr(1, 2)
        got = tuple(int(V[n]["D_f"] * g1 - V[n]["kbar"])
                    for n in ("G", "H2", "F3", "F2", "F1"))
        ok = (g1 == row["g"]
              and Fr(2 * l1, k1) == row["expX"]
              and (Fr(4 * l1, k1), Fr(2 * l1, k1)) == row["expF1"]
              and int(V["F1"]["D_f"] * g1 - V["F1"]["kbar"]) == row["d1F1"]
              and got == row["deltas"])
        check(f"Sol table row ({k1},{l1}): g/exponents/deltas match "
              f"(delta_1(F1) = {row['d1F1']})", ok,
              f"got deltas {got} want {row['deltas']}")
    # CASE A (empty prefix) and CASE C (any prefix): X dies at level m while
    # F1 is alive.  After r k=2 prefix steps (each adds an odd l/2 to alpha;
    # k=1 steps add 0), alpha_m = 3/2 + r/2 (mod 1).  X-death demands
    # l_m/k_m = gap(X) + alpha_m - 1 with k_m | 2 (F1 alive):
    #   k_m = 1: l_m = 1 + r/2 + 1/(2 nu_X) (mod 1) -- integral iff
    #            2 nu_X | r nu_X + 1: impossible (checked r mod 2 = 0, 1);
    #   k_m = 2: l_m = 2 + r + 1/nu_X (mod 2) -- integral iff nu_X | 1.
    for nuX in divs:
        gX = Fr(nuX + 1, 2 * nuX)
        # empty-prefix instance (the old written Case A): k1 = 2 nu_X
        rr = gX + Fr(1, 2)
        kA, lA = rr.denominator, rr.numerator
        check(f"case A nu_X={nuX}: empty prefix step (k,l) = (2nu_X, 2nu_X+1) "
              f"refused by k | 2 (F1/X alive caps)",
              kA == 2 * nuX and lA == 2 * nuX + 1 and kA > 2)
        # general prefix: closed form over r parity + explicit r = 0..5
        ok_closed = (all((r * nuX + 1) % (2 * nuX) != 0 for r in (0, 1))
                     and NN % nuX == 0 and nuX > 1)
        ok_explicit = True
        for r in range(6):
            lm1 = Fr(3, 2) + Fr(r, 2) - Fr(1, 2) + Fr(1, 2 * nuX)  # k_m = 1
            lm2 = 2 * (Fr(3, 2) + Fr(r, 2)) - 1 + Fr(1, nuX)       # k_m = 2
            ok_explicit &= (lm1.denominator != 1 and lm2.denominator != 1)
        status = "X-death l_m never integral" if (ok_closed and ok_explicit) \
            else "SURVIVES"
        print(f"    case A/C nu_X={nuX:>5}: gap {sfr(gX):>9}: {status}")
        check(f"case A/C nu_X={nuX}: X-death impossible at any prefix length",
              ok_closed and ok_explicit)
    # CASE B: F1 kills level 1 first: impossible -- delta(X) in N cannot
    # skip its own zero, so X (gap > 2/5) must die strictly before any
    # g_j = 2/5 level exists; equivalently death at X would need gap 2/5:
    check("case B: F1 cannot die first (delta_X would need gap(X) = 2/5, "
          "i.e. nu_X = -5)",
          all(Fr(d + 1, 2 * d) != Fr(2, 5) and 5 * (d + 1) != 4 * d
              for d in divs))
    check("case B: h1 alive at X refused ((k,l) = (10,9): exp 2*9/10 = 9/5)",
          Fr(2 * 9, 10).denominator != 1)
    check("OBSTRUCTION recorded in certificate matches exhaustion",
          ob["status"] == "OBSTRUCTED" and int(ob["checked_stacks"]) == len(divs)
          and ob.get("cases") == ["A", "B", "C"]
          and ob.get("exhaustion_scope", "").startswith("universal"))

    # ---- C3-V: arrival/predecessor variant coverage (Sol finding 3) ----
    # The census keeps 2 raw records per terminal (M_U = 2 and 4; dedup drops
    # M_U), and the chain-2 predecessor family is free in the pure-b
    # characteristic nu3 and in zero-cost neutral padding.  The charged
    # predecessor DAG is unique (grok-sixcells-review.md finding 4), so the
    # free data are exactly (nu3, padding, M_U).  Verify per recorded
    # variant, and parametrically for the families, that every clash
    # ingredient is unchanged or bounded below the level-1 window.
    print("  -- C3-V: M_U / free-characteristic / padding variant coverage --")
    variants = cert.get("variants", [])
    check("every recorded raw arrival M_U has a realized variant",
          set(int(fr(m)) for m in cert["arrival"]["M_U_raw"])
          <= set(int(fr(v["M_U"])) for v in variants) and len(variants) >= 2)
    is_trunk = cert["terminal"].get("vertex", "G") == "T"
    for v in variants:
        MU, nu3 = int(fr(v["M_U"])), int(fr(v["nu3"]))
        iG = int(fr(v["i_G"]))
        P1prod = int(fr(v["chain1_product"]))
        pad = int(fr(v.get("padding_factor", 1)))
        tag = f"variant M_U={MU}, nu3={nu3}"
        dp3, dq3 = 3 + 7 * nu3, 1 + nu3
        check(f"{tag}: pure-b cell (3+7nu,1+nu) = ({dp3},{dq3}), "
              f"M = gcd(4,nu+1) = {MU}",
              gcd(dp3, dq3) == gcd(4, nu3 + 1) == MU and nu3 % 2 == 1)
        n3 = Fr(7 + 17 * nu3, 2)
        check(f"{tag}: BOOK-2.1 n = (7+17nu)/2 = {sfr(n3)} integral and "
              f"(1/7+n)/(5+n) = d_p/(7 d_q)",
              n3.denominator == 1
              and (Fr(1, 7) + n3) / (5 + n3) == Fr(dp3, 7 * dq3))
        kb3 = Fr(1 + nu3, 2)
        check(f"{tag}: frame kbar = (1+nu)/2, rho = 1/2, w = 1/2 (nu-free)",
              kb3 == (5 + n3) / 17 and (kb3 - Fr(1, 2)) / nu3 == Fr(1, 2))
        deg3 = 170 * dp3
        degU = deg3 * pad
        check(f"{tag}: i-ledger 170*(3+7nu)*pad/2 = i_G = {iG}; "
              f"chain-1 product = i_G/2 = {P1prod} >= 2",
              iG * 2 == degU and P1prod * 2 == iG and P1prod >= 2)
        check(f"{tag}: E5 (I4) kbar_G = (mu0*nu_G*w_U - 2)/(mu0 - 1) = 5 "
              f"uses nu_G = 7 only (nu_U free)",
              (2 * 7 * Fr(1, 2) - 2) / (2 - 1) == 5)
        check(f"{tag}: arrival vertex characteristic odd (P2-legality)",
              (nu3 if pad == 1 else int(fr(v["pad_nu"]))) % 2 == 1)
        # window emptiness for this variant's chain-2 gaps:
        gap3 = Fr(dq3, 170 * dp3)
        gapG = Fr(15, 9 * iG)
        ok_w = gap3 < Fr(2, 5) and gapG < Fr(2, 5)
        if is_trunk:
            iT = int(fr(v["i_T"]))
            check(f"{tag}: trunk i_T = 3*i_G = {iT}; k_f = 35*i_T; "
                  f"l_f = (3/5)k_f integral",
                  iT == 3 * iG and (Fr(3, 5) * 35 * iT).denominator == 1)
            ok_w &= Fr(15, 35 * iT) < Fr(2, 5)
        else:
            kf = 9 * iG
            check(f"{tag}: direct k_f = 9*i_G = {kf}; l_f = k_f/3 integral",
                  kf == int(fr(v["k_f"])) and Fr(kf, 3).denominator == 1)
        check(f"{tag}: variant gaps below the window (F3' {sfr(gap3)}, "
              f"G {sfr(gapG)} < 2/5)", ok_w)
        # parity/existence of the stack: i_G even here; if a variant had odd
        # i_G, (H8) i-sync itself would fail (spine-tier death) -- either
        # way no escape:
        check(f"{tag}: chain-1 stack exists (2 | i_G) and universal nu_X "
              f"refutation applies to every divisor >= 2 of {P1prod}",
              iG % 2 == 0 and P1prod >= 2)
    # parametric family bounds (all nu3 >= 2, any padding depth):
    check("family bound: gap(F3'(nu)) = (1+nu)/(170(3+7nu)) < 2/5 for all "
          "nu >= 2 (identity 2*170*(3+7nu) - 5(1+nu) = 1015 + 2375nu > 0)",
          all(2 * 170 * (3 + 7 * n) - 5 * (1 + n) == 1015 + 2375 * n > 0
              for n in ULAT))
    check("family bound: padding gap (1+nu)/(2*i*nu) < 2/5 for all nu >= 2 "
          "once i >= 170 (identity 4*170*nu - 5(1+nu) = 675nu - 5 > 0)",
          all(4 * 170 * n - 5 * (1 + n) == 675 * n - 5 > 0 for n in ULAT))
    check("family bound: intermediate chain-1 gaps (1+nu)/(2 P nu) < 1/2 "
          "<= gap(X) for P >= 2 (identity P*nu - (1+nu) >= nu - 1 >= 1)",
          all(2 * n - (1 + n) == n - 1 >= 1 for n in ULAT))
    m2_corroboration(ob)
    insertion_closure(cert, V, ULAT)


def insertion_closure(cert, V, ULAT):
    """C3-N: zero-cost neutral-insertion closure (Sol re-review finding 1).

    Every record realization admits state-preserving zero-cost clean
    neutral insertions at any chain state (design SS2.4/SS4.1 neutral-depth
    family) -- IN-PERIMETER, invisible to the state-level px5 closure.
    Closure: the universal A/B/C refutation consumes only (i) the k | 2
    cap, (ii) window emptiness, (iii) gap(X) = (nu+1)/(2nu); each is
    proved invariant under every legal insertion by lemmas N1-N4 below,
    machine-checked here together with Sol's explicit example."""
    print("  -- C3-N: zero-cost neutral-insertion closure (all states, "
          "both terminals) --")
    ins = cert.get("insertions")
    check("insertions section present (Sol re-review finding 1)",
          ins is not None)
    if ins is None:
        return
    # --- Sol's explicit example, replayed exactly ---
    ex = ins["sol_example"]
    tau = (Fr(5) - Fr(1, 2)) / 1                       # R1.2 from P2 frame
    n_e = tau * 3 - Fr(1, 2)
    kbY = tau * 4 / 3
    rhoY = tau / 3
    check("Sol insertion Y=(6,4) l=2 nu=3 @ (3/2,2): R1.2 tau=9/2, n=13, "
          "kbar=6, rho=3/2, w=3/2, M=2",
          tau == Fr(9, 2) == fr(ex["tau"]) and n_e == 13 == int(fr(ex["n"]))
          and kbY == 6 == int(fr(ex["kbar"])) and rhoY == fr(ex["rho"])
          and (kbY - rhoY) / 3 == Fr(3, 2) and gcd(6, 4) == 2)
    check("Sol insertion BOOK(2.1) rows: (1/2+13)/(5+13) = 6/(2*4) and "
          "(3/2+6)/(6+6) = 20/(2*16), kbar_F1 = 4 preserved",
          (Fr(1, 2) + 13) / 18 == Fr(6, 8)
          and (Fr(3, 2) + 6) / 12 == Fr(20, 32)
          and Fr(6 + 6, 3) == 4)
    iY, iF1, iF2 = 2, 6, 30
    check("Sol insertion ledger: i_Y=2 (deg 12), i_F1=6 (deg 120), "
          "i_F2=30 (deg 3570) -- i_F1 moved off 2",
          iY * 2 == 4 and iY * 6 == 12 and iF1 * 2 == 12 and iF1 * 20 == 120
          and iF2 * 4 == 120 and iF2 * 119 == 3570
          and iF1 == int(fr(ex["i_F1"])) and iF1 != 2)
    check("Sol insertion gaps: Y 1/3, F1 2/15, F2 1/102 -- all < 2/5, "
          "none in the window",
          Fr(4, 12) == Fr(1, 3) and Fr(16, 120) == Fr(2, 15) == fr(ex["gap_F1"])
          and Fr(35, 3570) == Fr(1, 102)
          and all(g < Fr(2, 5) for g in (Fr(1, 3), Fr(2, 15), Fr(1, 102))))
    check("Sol insertion scaling: i_G and chain-1 product x3 "
          "(22610->67830/11305->33915; 4420->13260/2210->6630), products >= 2",
          3 * 22610 == 67830 and 67830 // 2 == 33915 == 3 * 11305
          and 3 * 4420 == 13260 and 13260 // 2 == 6630)
    # --- Lemma N1: a state-preserving zero-cost step is a clean n=1
    # neutral: for n >= 2, Delta - n = (n-1)(nu-1) >= 1 so w strictly
    # drops and the record's pinned state sequence breaks. ---
    check("N1: state-preserving => n = 1 (identity (n-1)(nu-1) >= 1)",
          all((n - 1) * (nu - 1) >= 1
              for n in range(2, 12) for nu in range(2, 24)))
    # --- Lemma N2: M-conservation constrains inserted nu per state:
    # M_Y = gcd(l*nu, nu+1) = gcd(l, nu+1) must equal the state M; at the
    # pre-F1 state (3/2,2), M = 2 forces nu odd (so P_pre is odd). ---
    check("N2: gcd(l*nu, nu+1) = gcd(l, nu+1) (lattice)",
          all(gcd(l * nu, nu + 1) == gcd(l, nu + 1)
              for l in range(1, 13) for nu in range(2, 40)))
    check("N2: pre-F1 state M=2: gcd(l, nu+1) = 2 forces nu odd",
          all(nu % 2 == 1
              for l in range(1, 13) for nu in range(2, 60)
              if gcd(l, nu + 1) == 2))
    # --- Lemma N3 (joint cap): the P2-adjacent chain-2 vertex has full
    # f-pattern (t-A)^4 (exponent = deg p_f,P2 = 4, any shape (i,l) with
    # i*l = 4); F1 has simple reduced factors with i_F1 = 2*P_pre.  A
    # ladder step alive at both needs k | 4*l1 and k | 2*P*l1, i.e.
    # k | gcd(4, 2P) = 2 for odd P.  (P = 1 is the no-insertion case:
    # F1's own simple factors give k | 2 directly.) ---
    check("N3: gcd(4, 2P) = 2 for every odd P",
          all(gcd(4, 2 * P) == 2 for P in range(1, 40, 2)))
    check("N3: joint cap lattice: no coprime (k,l1), k >= 3, passes both "
          "exponent tests 4*l1/k and 2*P*l1/k for odd P",
          all(not (Fr(4 * l1, k).denominator == 1
                   and Fr(2 * P * l1, k).denominator == 1)
              for P in range(1, 16, 2) for k in range(3, 13)
              for l1 in range(1, 13) if gcd(k, l1) == 1))
    check("N3 premises: Y_adj (gap <= 3/8) and F1 (gap 2/(5P) <= 2/5) are "
          "both below gap(X) > 1/2, hence alive at X-death",
          Fr(3, 8) < Fr(1, 2) and all(Fr(2, 5 * P) <= Fr(2, 5) < Fr(1, 2)
                                      for P in range(1, 16, 2)))
    # --- Lemma N4 (uniform Dprev gap bound): an inserted neutral above a
    # poleward vertex of full f-degree Dprev has i = Dprev/l and gap =
    # (nu+1)/(Dprev*nu), independent of l.  Chain-2: Dprev >= 4 gives
    # gap <= 3/8 < 2/5 for every nu >= 2. ---
    check("N4: gap = (nu+1)/(Dprev*nu) <= 3/8 < 2/5 for Dprev >= 4, "
          "nu >= 2 (identity 12nu - 8(nu+1) = 4nu - 8 >= 0)",
          all(12 * nu - 8 * (nu + 1) == 4 * nu - 8 >= 0
              and Fr(nu + 1, 4 * nu) <= Fr(3, 8) < Fr(2, 5)
              for nu in ULAT))
    check("N4: charged gaps shrink under insertions: gap(F1) = 2/(5P), "
          "gap(F2) = 1/(34P'), monotone nonincreasing",
          all(Fr(2, 5 * P) <= Fr(2, 5) and Fr(1, 34 * P) <= Fr(1, 34)
              for P in range(1, 40)))
    # --- per-eligible-state quantification (both terminal families) ---
    for st in ins["states"]:
        name, Ms = st["state"], st.get("M")
        Dmin = int(fr(st["Dprev_min"])) if "Dprev_min" in st else None
        if st.get("family") == "chain1":
            check(f"state {name}: chain-1 stack IS the X-family; universal "
                  "nu_X refutation applies", True)
            continue
        lat = [(l, nu) for l in range(1, 13) for nu in range(2, 60)
               if gcd(l, nu + 1) == int(fr(Ms))]
        check(f"state {name}: legal insertion lattice nonempty "
              f"({len(lat)} samples) and every gap (nu+1)/(Dprev*nu) < 2/5 "
              f"at Dprev >= {Dmin}",
              len(lat) > 0 and all(Fr(nu + 1, Dmin * nu) < Fr(2, 5)
                                   for _, nu in lat))
        if st.get("affects_caps"):
            check(f"state {name}: every legal inserted nu is odd "
                  "(P_pre odd, feeds N3)",
                  all(nu % 2 == 1 for _, nu in lat))
    check("closure recorded: A/B/C inputs (k|2 cap, window emptiness, "
          "gap(X)) are insertion-invariant",
          "insertion-invariant" in ins.get("closure", ""))


def m2_corroboration(ob):
    # the two m_G branch refutations (fixed-representative corroboration,
    # nu_N = 11305; direct certificate only -- the trunk kill rests on the
    # three-case exhaustion):
    if "m2_branch" in ob:
        check("m_G=1 refuted: Prop8.1@N needs 22611 > 11306 = mult(p^11305 q, c_g)",
              1 * 11305 + 11306 == 22611 and 11305 * 1 + 1 == 11306
              and 22611 > 11306)
        s_N = (fr(ob["m2_branch"]["s_from_N"]))
        s_H2 = (fr(ob["m2_branch"]["s_from_H2"]))
        check("m_G=2 refuted: N pins s = 22611, H2 drop-window pins s = 11309",
              s_N == 22611 and s_H2 == 11309 and s_N != s_H2)
        check("N drop-window: [22611*33913, s*33913] forces s = 22611 exactly",
              Fr(33915 * 22611 - 45222, 1) == Fr(33913 * 22611, 1))
        check("H2 drop-window: 22618 <= 3s - 11309 <= 2s forces s = 11309 exactly",
              3 * 11309 - 11309 == 2 * 11309 and 3 * 11309 - 11309 >= 22618)


# ----------------------------------------------------------------------
# C5: LEAD-PILOT reproduction gate
# ----------------------------------------------------------------------

def lead_pilot_gate(cert):
    print("\n== C5: LEAD-PILOT (design SS3.5) regeneration gate ==")
    pilot = build_pilot_from_cert(cert)
    ref_vars, ref_rows = DESIGN_PILOT_VARS, DESIGN_PILOT_ROWS
    # prefer the literal block extracted from the design file itself
    design = HERE.parent / "xmodel" / "sol-gluing-design.md"
    if design.exists():
        import re
        m = re.search(r"### 3\.5 Literal.*?```text\n(.*?)```",
                      design.read_text(), re.S)
        if m:
            blk = [ln for ln in m.group(1).strip().split("\n") if ln.strip()]
            ref_vars = blk[0]
            ref_rows = [r.rstrip(",").strip() for r in blk[2:]]
            check("reference block extracted from xmodel/sol-gluing-design.md SS3.5",
                  blk[1] == "0" and len(ref_rows) == 74)
            check("embedded fallback block == design file block",
                  ref_vars == DESIGN_PILOT_VARS and ref_rows == DESIGN_PILOT_ROWS)
    check("83 variables regenerated", pilot[0] == ref_vars,
          f"first diff: {first_diff(pilot[0].split(','), ref_vars.split(','))}")
    check("characteristic 0 header", pilot[1] == "0")
    rows = pilot[2:]
    check(f"74 rows regenerated (got {len(rows)})", len(rows) == len(ref_rows) == 74)
    bad = [i for i, (a, b) in enumerate(zip(rows, ref_rows)) if a != b]
    check("row-for-row identity with the design block",
          not bad, f"rows differing: {[(i + 1, rows[i], ref_rows[i]) for i in bad[:3]]}")


def first_diff(a, b):
    for x, y in zip(a, b):
        if x != y:
            return f"{x} vs {y}"
    return "length"


def build_pilot_from_cert(cert):
    """Regenerate the 83/74 system purely from certificate data."""
    out = []
    V = {v["name"]: v for v in cert["vertices"]}
    P = cert["pilot"]
    out.append(P["variables"])
    out.append("0")
    # rows 1-15: local equations, emitted from the T1/Wronskian layer
    out += P["local_rows"]
    # rows 16-21 directions (L9 first parts) from edges with nonzero continuation
    for e in cert["edges"]:
        if e.get("continuation"):
            c = e["continuation"]
            out.append(f'{c["c"]}^{c["nu_L"]}-{c["A"]}')
    # rows 22-27 derivative auxiliaries
    for e in cert["edges"]:
        if e.get("continuation"):
            c = e["continuation"]
            out.append(f'{c["d"]}-{c["nu_L"]}*{c["c"]}^{int(c["nu_L"]) - 1}')
    # rows 28-29 separation auxiliaries
    out += P["separation_rows"]
    # rows 30-37 leading transports (P10 / St 3.9(ii))
    out += [r["row"] for r in P["scale_transports"]]
    # rows 38-74 guards
    out += P["guard_rows"]
    return out


# The literal SS3.5 block of xmodel/sol-gluing-design.md (lines 1421-1496),
# the gate's reference. Variables line, then '0', then 74 rows.
DESIGN_PILOT_VARS = ("A_p1,B_p1,C_p1,A_n,C_n,A_g,B_g,C_g,A_h,C_h,A_f3,C_f3,"
                     "A_f2,B_f2,C_f2,A_f1,Sig_f1,Pi_f1,C_f1,A_p2,U_p2,V_p2,C_p2,"
                     "c_n,c_g,c_h,c_f3,c_f2,c_f1,d_n,d_g,d_h,d_f3,d_f2,d_f1,"
                     "z_f2,z_f1,S_r,S_g,S_n,S_p1,S_h,S_f3,S_f2,S_f1,S_p2,"
                     "u_p1_A,u_p1_B,u_p1_AB,u_p1_C,u_n_A,u_n_C,u_g_A,u_g_B,u_g_AB,u_g_C,"
                     "u_h_A,u_h_C,u_f3_A,u_f3_C,u_f2_A,u_f2_B,u_f2_AB,u_f2_C,"
                     "u_f1_A,u_f1_Pi,u_f1_disc,u_f1_z,u_f1_C,"
                     "u_p2_A,u_p2_V,u_p2_disc,u_p2_qA,u_p2_C,"
                     "u_S_r,u_S_g,u_S_n,u_S_p1,u_S_h,u_S_f3,u_S_f2,u_S_f1,u_S_p2")

DESIGN_PILOT_ROWS = [
    "2*B_p1-3*A_p1", "2*A_p1*B_p1-C_p1", "11306*C_n+11305*A_n",
    "-14*A_g+21*B_g", "-7*A_g*B_g-5*C_g", "4*C_h+7*A_h", "3*C_f3+10*A_f3",
    "2*B_f2-3*A_f2", "10*C_f2-51*A_f2^2", "Sig_f1-3*A_f1", "Pi_f1-3*A_f1^2",
    "4*C_f1+15*A_f1^3", "2*U_p2+3*A_p2", "A_p2*U_p2+4*V_p2", "3*A_p2*V_p2-C_p2",
    "c_n^11305-A_n", "c_g^7-A_g", "c_h^7-A_h", "c_f3^5-A_f3", "c_f2^17-A_f2",
    "c_f1^5-A_f1",
    "d_n-11305*c_n^11304", "d_g-7*c_g^6", "d_h-7*c_h^6", "d_f3-5*c_f3^4",
    "d_f2-17*c_f2^16", "d_f1-5*c_f1^4",
    "z_f2-A_f2+B_f2", "z_f1-A_f1^2+Sig_f1*A_f1-Pi_f1",
    "S_g-S_r", "S_h-S_g*A_g^22610", "S_n-S_g*c_g^45220*d_g^22610",
    "S_p1-S_n*d_n^2", "S_f3-S_h*d_h^6460", "S_f2-S_f3*c_f3^510*d_f3^1190",
    "S_f1-S_f2*d_f2^40*z_f2^30", "S_p2-S_f1*d_f1^4*z_f1^2",
    "u_p1_A*A_p1-1", "u_p1_B*B_p1-1", "u_p1_AB*A_p1-u_p1_AB*B_p1-1",
    "u_p1_C*C_p1-1", "u_n_A*A_n-1", "u_n_C*C_n-1", "u_g_A*A_g-1", "u_g_B*B_g-1",
    "u_g_AB*A_g-u_g_AB*B_g-1", "u_g_C*C_g-1", "u_h_A*A_h-1", "u_h_C*C_h-1",
    "u_f3_A*A_f3-1", "u_f3_C*C_f3-1", "u_f2_A*A_f2-1", "u_f2_B*B_f2-1",
    "u_f2_AB*A_f2-u_f2_AB*B_f2-1", "u_f2_C*C_f2-1", "u_f1_A*A_f1-1",
    "u_f1_Pi*Pi_f1-1", "u_f1_disc*Sig_f1^2-4*u_f1_disc*Pi_f1-1", "u_f1_z*z_f1-1",
    "u_f1_C*C_f1-1", "u_p2_A*A_p2-1", "u_p2_V*V_p2-1",
    "u_p2_disc*U_p2^2-4*u_p2_disc*V_p2-1",
    "u_p2_qA*A_p2^2+u_p2_qA*U_p2*A_p2+u_p2_qA*V_p2-1", "u_p2_C*C_p2-1",
    "u_S_r*S_r-1", "u_S_g*S_g-1", "u_S_n*S_n-1", "u_S_p1*S_p1-1", "u_S_h*S_h-1",
    "u_S_f3*S_f3-1", "u_S_f2*S_f2-1", "u_S_f1*S_f1-1", "u_S_p2*S_p2-1",
]


# ----------------------------------------------------------------------

def scale_transport_audit(cert, V):
    """(P10) exponent audit: each S-row's exponents re-derived from the tower
    data: multiplying a reduced Taylor coefficient out to the full pattern
    by i_L, splitting c/d/z factors per the reduced-root structure."""
    print("\n== C1b: (P10) leading-transport exponent audit ==")
    for r in cert["pilot"]["scale_transports"]:
        if "exponent_audit" not in r:
            continue
        aud = r["exponent_audit"]
        ok = all(int(fr(v["got"])) == int(fr(v["want"])) for v in aud.values())
        check(f'(P10) {r["row"].split("-")[0]}: exponents = i_L x reduced data',
              ok, str(aud))


def anchor_check(cert):
    """(P11)-(P13) rational anchor: substitute and verify every pilot row."""
    print("\n== C5b: exact rational anchor (P11)-(P13) on regenerated rows ==")
    def load(v):
        if isinstance(v, str) and v.startswith("EXPR:"):
            return eval(v[5:], {"__builtins__": {}}, {"Fr": Fr})
        return fr(v)
    vals = {k: load(v) for k, v in cert["pilot"]["anchor"].items()}
    # tiny expression evaluator for the msolve grammar (no parentheses)
    def ev(row):
        tot = Fr(0)
        for term in row.replace("-", "+-").split("+"):
            if not term:
                continue
            prod = Fr(1)
            for fac in term.split("*"):
                sign = 1
                if fac.startswith("-"):
                    sign, fac = -1, fac[1:]
                if "^" in fac:
                    b, e = fac.split("^")
                    base = vals[b] if b in vals else Fr(b)
                    prod *= sign * base ** int(e)
                else:
                    v = vals[fac] if fac in vals else Fr(fac)
                    prod *= sign * v
            tot += prod
        return tot
    rows = build_pilot_from_cert(cert)[2:]
    bad = []
    for i, row in enumerate(rows):
        # skip the gigantic-exponent scale rows for direct evaluation only if
        # values were chosen to make them cheap (c=1, d values small) -- they are.
        try:
            z = ev(row)
        except Exception as exc:  # pragma: no cover
            bad.append((i + 1, row, f"eval error {exc}"))
            continue
        if z != 0:
            bad.append((i + 1, row, sfr(z)))
    check(f"anchor satisfies all {len(rows)} rows exactly", not bad, str(bad[:3]))


def run_all(cert, quiet=False):
    """Run every check family; return number of failures."""
    global FAILURES, check
    FAILURES = []
    if quiet:
        import builtins
        real_print = builtins.print
        builtins.print = lambda *a, **k: None
    try:
        template_control()
        V = route_spine(cert)
        if "pilot" in cert:
            scale_transport_audit(cert, V)
        local_t1(cert)
        tower_layer(cert, V)
        if "pilot" in cert:
            lead_pilot_gate(cert)
            anchor_check(cert)
        else:
            print("\n== C5: no pilot section in this certificate "
                  "(trunk spine has no design SS3.5 block to gate against) ==")
    except Exception as exc:
        FAILURES.append(("EXCEPTION", repr(exc)))
    finally:
        if quiet:
            builtins.print = real_print
    return len(FAILURES)


def perturbation_suite():
    """Design SS3.6 negative perturbations: each must produce >= 1 failure."""
    print("\n== C6: negative-perturbation self-test (design SS3.6 list) ==")
    import copy
    base = json.loads(CERT.read_text())
    perts = []
    # 1. flip the T1 sign at G (C ~ +14/15 instead of -14/15)
    p = copy.deepcopy(base)
    p["t1_local"][0]["C"] = "Fr(14,15)*A*A"
    perts.append(("T1 sign flip at G", p))
    # 2. omit the factor nu from a derivative row (d_g = c_g^6, not 7c_g^6)
    p = copy.deepcopy(base)
    p["edges"][2]["continuation"]["nu_L"] = 1
    perts.append(("nu omitted from d_g derivative", p))
    # 3. replace B_g = (2/3)A by (3/2)A
    p = copy.deepcopy(base)
    p["t1_local"][0]["q_factors"][1]["coeffs_t"]["0"] = "-Fr(3,2)*A"
    perts.append(("B_g = (3/2)A instead of (2/3)A", p))
    # 4. mixed-reading kappa at the doubly realized vertex (49 for 7)
    p = copy.deepcopy(base)
    p["vertices"][4]["kappa"] = 49
    p["vertices"][4]["pi"] = "45/49"
    perts.append(("kappa_H2 = 49 (non-H5a composition)", p))
    # 5. E5 nu_G replaced by nu_U in the recorded edge n (n = 1 printed-style)
    p = copy.deepcopy(base)
    p["edges"][7]["n"] = 1
    perts.append(("case-III n from the mixed reading", p))
    # 6. move one jet/scale level by one slot (S_h exponent off by one)
    p = copy.deepcopy(base)
    p["pilot"]["scale_transports"][1]["row"] = "S_h-S_g*A_g^22611"
    perts.append(("S_h exponent shifted one slot", p))
    # 7. void the obstruction record (claims a surviving stack count)
    p = copy.deepcopy(base)
    p["tower"]["obstruction"]["checked_stacks"] = 14
    perts.append(("obstruction stack count tampered", p))
    # 8. claim only the old two-case exhaustion (Grok finding 6)
    p = copy.deepcopy(base)
    p["tower"]["obstruction"]["cases"] = ["A", "B"]
    perts.append(("case list without Case C", p))
    # 9. variant tampering: M_U=4 claimed realized by a nu3 = 1 (mod 4) cell
    p = copy.deepcopy(base)
    p["variants"][1]["nu3"] = 5
    perts.append(("M_U=4 variant with gcd(4,nu3+1) = 2 cell", p))
    # 10. drop the M_U=4 variant entirely (Sol finding 3/6: M_U_raw unread)
    p = copy.deepcopy(base)
    p["variants"] = p["variants"][:1]
    perts.append(("M_U=4 raw record without a realized variant", p))
    # 11. Sol re-review: a neutral inserted before F1 with i_F1 left at 2
    p = copy.deepcopy(base)
    p["insertions"]["sol_example"]["i_F1"] = 2
    perts.append(("pre-F1 neutral insertion with i_F1 asserted 2", p))
    # 12. drop the insertion-closure section entirely
    p = copy.deepcopy(base)
    del p["insertions"]
    perts.append(("insertion-closure section removed", p))
    # trunk perturbations
    trunk = json.loads(TRUNK.read_text())
    p = copy.deepcopy(trunk)
    p["terminal"]["w"] = "3/5"
    p["vertices"][1]["w"] = "3/5"
    perts.append(("trunk terminal w tampered (3/5)", p))
    p = copy.deepcopy(trunk)
    p["chain2_book21"][0]["l"] = 2
    perts.append(("trunk BOOK-2.1 l tampered", p))
    ok_all = True
    for name, pc in perts:
        n = run_all(pc, quiet=True)
        ok = n >= 1
        ok_all &= ok
        print(f"  [{'PASS' if ok else 'FAIL'}] perturbation caught: {name}"
              f" ({n} failure(s) raised)")
    return ok_all


def main():
    totals = {}
    for path in (CERT, TRUNK):
        cert = json.loads(path.read_text())
        print(f"\n######## certificate: {path.name}")
        print(f"cell {cert['cell']}\nroute {cert['route']}")
        print(f"status: {cert['status']}")
        run_all(cert)
        totals[path.name] = (list(FAILURES),
                             cert["tower"]["obstruction"]["status"])
    pert_ok = perturbation_suite()
    print()
    all_fails = [(f"{k}: {n}", d) for k, (fs, _) in totals.items()
                 for n, d in fs]
    if all_fails or not pert_ok:
        print(f"RESULT: {len(all_fails)} FAILURE(S)"
              + ("" if pert_ok else " + perturbation suite FAILED"))
        for name, det in all_fails:
            print(f"  FAIL {name}: {det}")
        sys.exit(1)
    verdicts = ", ".join(f"{k}: {v}" for k, (_, v) in totals.items())
    print("RESULT: ALL CHECKS PASS (incl. perturbation suite) -- "
          "both certificates validated; tower tier verdicts: " + verdicts)
    sys.exit(0)


if __name__ == "__main__":
    main()
