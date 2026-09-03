#!/usr/bin/env python3
"""Independent hostile-gate replay for PROP 5.5(k). Stdlib + mpmath + sympy.
Does not import prop55k.test55k for the arithmetic core (reimplemented).
"""
from fractions import Fraction as F
from math import gcd
from collections import Counter
import mpmath as mp
import sympy as sp

# ---- independent Def 5.1(3) and closed form --------------------------------
def def51(n, M, d, V, s, i):
    num = F(n - M[i]); den = F(n - M[s] - 1)
    for j in range(i + 1, s + 1):
        num *= (V[j] * (n - M[j]) - d[j])
        den *= (V[j] * (n - M[j - 1]) - d[j])
    return 1 - num / den

def phi(n, m, M2, V2, k):
    d2 = gcd(n, m)
    M = {1: -m, 2: M2}
    d = {1: n, 2: d2, 3: gcd(d2, M2)}
    V = {2: V2, 3: d[3]}
    return (k + 1) * def51(n, M, d, V, 2, 2), (k + 1) * def51(n, M, d, V, 2, 1)

def closed(n, m, M2, V2, k):
    d2 = gcd(n, m)
    Pi = (n + m) // d2
    U2 = d2 - V2
    R = n - M2 - 1
    return F(-(k + 1), R), F((k + 1) * (Pi * U2 - R), R * (Pi * V2 - 1))

def galois_test(n, m, M2, V2, k, lattice="delta2"):
    """Independent TEST-55(k). lattice in {'delta2','moh'}."""
    d2 = gcd(n, m)
    nstar, mstar = n // d2, m // d2
    Pi = nstar + mstar
    U2 = d2 - V2
    R = n - M2 - 1
    d2p, d1 = closed(n, m, M2, V2, k)
    A = d1.denominator
    L = 1 if lattice == "moh" else d2p.denominator
    Aa = A // gcd(A, L) if A else 1
    dg, dT = nstar * V2, mstar * V2
    kills = []
    notes = []
    if not (V2 > F(d2, R + 1)):
        kills.append("H-major")
    if not (V2 < d2):
        kills.append("H-strict")
    if A <= 1:
        return dict(n=n, m=m, M2=M2, V2=V2, k=k, d2=d2, nstar=nstar, mstar=mstar,
                    Pi=Pi, U2=U2, R=R, delta2=d2p, delta1=d1, A=A, L=L, Aa=Aa,
                    deg_g=dg, deg_T=dT, res=None, kills=kills, notes=["A'=1"],
                    verdict="INAPPLICABLE(A'=1)", g0=None, Psi=None)
    rg, rT = dg % Aa, dT % Aa
    if Aa > 1:
        if rg == 0 and rT == 0:
            kills.append("GALOIS-both0")
        if rg != 0 and rT != 0:
            kills.append("GALOIS-neither")
        if rg > 1:
            kills.append("A5-SIMPLE-g")
        if rT > 1:
            kills.append("A5-SIMPLE-T")
    if Aa > dg and Aa > dT and dg >= 1 and dT >= 1:
        kills.append("MONOMIAL")
    g0 = Psi = None
    g0_ge = g0_div = None
    if R % (k + 1) == 0:
        rho = R // (k + 1)
        num = Pi * U2 - R
        den = rho * (Pi * V2 - 1)
        g0 = gcd(abs(num), den) if num else den
        Psi = (rho * (k + 1) + 1) * V2 - d2
        if rho == 1 and Aa == A:
            g0_ge = g0 >= V2
            g0_div = (Psi % g0 == 0) if g0 else False
            if (rg == 0) != (rT == 0):
                if g0 < V2:
                    kills.append("DIVCHAIN")
                if V2 > Psi:
                    kills.append("MASTER")
    verdict = "KILLED" if kills else "SURVIVES"
    return dict(n=n, m=m, M2=M2, V2=V2, k=k, d2=d2, nstar=nstar, mstar=mstar,
                Pi=Pi, U2=U2, R=R, delta2=d2p, delta1=d1, A=A, L=L, Aa=Aa,
                deg_g=dg, deg_T=dT, res=(rg, rT), kills=kills, notes=notes,
                verdict=verdict, g0=g0, Psi=Psi, g0_ge=g0_ge, g0_div=g0_div)

def show(lab, r):
    print("  %-36s d2=%s n*=%s m*=%s R=%s d2'=%-6s d1'=%-7s A'=%-3s L=%s Aa=%-3s "
          "deg=(%s,%s) res=%-8s g0=%s Psi=%s | %s"
          % (lab, r["d2"], r["nstar"], r["mstar"], r["R"], r["delta2"], r["delta1"],
             r["A"], r["L"], r["Aa"], r["deg_g"], r["deg_T"], str(r["res"]),
             r["g0"], r["Psi"], r["verdict"]))
    for k in r["kills"]:
        print("        KILL:", k)

if __name__ == "__main__":
    # ---- A. ten p.207 rationals ------------------------------------------------
    print("=" * 72)
    print("A. CLOSED FORM vs (k+1)*Def5.1(3) vs printed p.207 (SOURCE-READ table)")
    P207 = [
        ("(16,12) V2=3 k=1", 16, 12, 13, 3, 1, F(-1), F(1, 4)),
        ("(21,14) V2=2 k=1", 21, 14, 16, 2, 1, F(-1, 2), F(7, 6)),
        ("(21,14) V2=5 k=1", 21, 14, 18, 5, 1, F(-1), F(1, 3)),
        ("(15,10) V2=3 k=2", 15, 10, 11, 3, 2, F(-1), F(1, 2)),
        ("(15,10) V2=2 k=2", 15, 10, 11, 2, 2, F(-1), F(4, 3)),
    ]
    okA = True
    for lab, n, m, M2, V2, k, p2, p1 in P207:
        c, f = closed(n, m, M2, V2, k), phi(n, m, M2, V2, k)
        match = (c == f == (p2, p1))
        okA &= match
        print("  %-22s closed=%-16s phi=%-16s printed=%-16s %s"
              % (lab, str(c), str(f), str((p2, p1)), "MATCH" if match else "FAIL"))
    print("  all 10 rationals MATCH:", okA)

    # ---- B. (21,14;16;2;X) under A' vs 𝔄 --------------------------------------
    print("\n" + "=" * 72)
    print("B. REPLAY Moh p.207 row (21,14; 16; 2; X) under A' vs 𝔄")
    r_moh = galois_test(21, 14, 16, 2, 1, lattice="moh")
    r_cor = galois_test(21, 14, 16, 2, 1, lattice="delta2")
    show("A'=denom(d1')  L=1 (Moh p.188)", r_moh)
    show("𝔄=A'/gcd(A',L) L=denom(d2')", r_cor)
    print("  XOR under A': res=%s  (exactly one zero? %s)"
          % (r_moh["res"], (r_moh["res"][0] == 0) != (r_moh["res"][1] == 0)))
    print("  NOTE: Moh p.188 XOR uses only {A|deg or not}; A5-SIMPLE is extra.")
    print("  A5-SIMPLE kill under A'?", any(x.startswith("A5") for x in r_moh["kills"]))
    print("  XOR-only would kill?", (r_moh["res"][0] == 0) == (r_moh["res"][1] == 0)
          and r_moh["Aa"] > 1)

    # ---- C. G2/G3 both moduli --------------------------------------------------
    print("\n" + "=" * 72)
    print("C. G2 / G3 under A' vs 𝔄")
    for lab, n, m, M2, V2, k in [
        ("G2 (15,10;4;1;X^4)", 15, 10, 4, 1, 4),
        ("G3 (21,14;8;1;X^2)", 21, 14, 8, 1, 2),
    ]:
        show(lab + " L=1", galois_test(n, m, M2, V2, k, "moh"))
        show(lab + " L=d2den", galois_test(n, m, M2, V2, k, "delta2"))

    # ---- D. K=16 ray descendants ----------------------------------------------
    print("\n" + "=" * 72)
    print("D. K=16 ray descendants (12t+4, 8t+4; M2'=12t+1, V2'=3, k=1) t=1..6")
    any_killed = False
    for t in range(1, 7):
        n, m, M2, V2, k = 12 * t + 4, 8 * t + 4, 12 * t + 1, 3, 1
        r = galois_test(n, m, M2, V2, k, "delta2")
        show("t=%d (n',m')=(%d,%d)" % (t, n, m), r)
        if r["verdict"] == "KILLED":
            any_killed = True
    print("  any killed under 𝔄?", any_killed)

    # ---- E. existing-pair controls killed by A' --------------------------------
    print("\n" + "=" * 72)
    print("E. Existing controls: A' vs 𝔄  (claimed killed by A', live under 𝔄)")
    for lab, n, m, M2, V2, k in [
        ("P=pi^4-g^2 Q=P^2+pi (8,4) k=1", 8, 4, 3, 1, 1),
        ("P=pi^6-g^3 Q=P^2+pi (12,6) k=2", 12, 6, 5, 1, 2),
        ("P=pi^4-g^2 Q=P^3+pi (12,4) k=1", 12, 4, 7, 1, 1),
    ]:
        show(lab + " A'", galois_test(n, m, M2, V2, k, "moh"))
        show(lab + " 𝔄 ", galois_test(n, m, M2, V2, k, "delta2"))

    # ---- F. sharpness family: exact J and (ii) saturation ----------------------
    print("\n" + "=" * 72)
    print("F. SHARPNESS family P=pi^{k+1}-g^{k+1}, Q=P^q + a pi : exact J + d2'=(k+1)V2'")
    g, p, a = sp.symbols("gamma pi a")
    sharp_ok = True
    for kk, q in [(1, 2), (2, 2), (2, 3), (3, 3), (4, 2), (4, 3)]:
        P = p ** (kk + 1) - g ** (kk + 1)
        Q = P ** q + a * p
        J = sp.expand(sp.diff(P, g) * sp.diff(Q, p) - sp.diff(P, p) * sp.diff(Q, g))
        Jsimp = sp.simplify(J)
        expect = -a * (kk + 1) * g ** kk
        jmatch = sp.expand(Jsimp - expect) == 0
        n, m = q * (kk + 1), kk + 1
        M2 = n - kk - 2
        V2 = 1
        r = galois_test(n, m, M2, V2, kk, "delta2")
        eq = (r["d2"] == (kk + 1) * V2)
        sat = (r["g0"] == V2) and (r["Psi"] == r["g0"])
        sharp_ok &= jmatch and eq and r["verdict"] != "KILLED"
        print("  k=%d q=%d (n',m')=(%d,%d) J=%s == -a(k+1)g^k: %s  d2'=%d (k+1)V2'=%d eq=%s  g0=%s Psi=%s sat=%s %s"
              % (kk, q, n, m, Jsimp, jmatch, r["d2"], (kk + 1) * V2, eq, r["g0"], r["Psi"], sat, r["verdict"]))
    print("  sharpness J exact + equality + SURVIVES:", sharp_ok)

    # extra composition J check
    print("\n  composition J checks:")
    for desc, Pc, Qc, kk in [
        ("pi^4-g^2, P^2+pi", p ** 4 - g ** 2, (p ** 4 - g ** 2) ** 2 + p, 1),
        ("pi^6-g^3, P^2+pi", p ** 6 - g ** 3, (p ** 6 - g ** 3) ** 2 + p, 2),
        ("pi^5+pi^3+7-g^5, P^2+3P+pi",
         p ** 5 + p ** 3 + 7 - g ** 5,
         (p ** 5 + p ** 3 + 7 - g ** 5) ** 2 + 3 * (p ** 5 + p ** 3 + 7 - g ** 5) + p, 4),
    ]:
        J = sp.expand(sp.diff(Pc, g) * sp.diff(Qc, p) - sp.diff(Pc, p) * sp.diff(Qc, g))
        J = sp.simplify(J)
        is_mon = (J.as_poly(g, p) is not None
                  and set(J.as_poly(g, p).gens).issubset({g}) or J.free_symbols <= {g, a})
        # monomial in g of degree kk?
        poly = sp.Poly(sp.expand(J), g, p)
        mons = poly.as_dict()
        okJ = (len(mons) == 1 and list(mons.keys())[0] == (kk, 0))
        print("    %s  J=%s  monomial g^%d: %s" % (desc, J, kk, okJ))

    # ---- G. census k=0..8 n'<=60 (independent) ---------------------------------
    print("\n" + "=" * 72)
    print("G. CENSUS delta2'=-1, n'<=60 (independent galois_test, lattice=delta2)")
    print("  k  rows  A'=1  live  killed   %     survivors")
    census_rows = {}
    for kk in range(0, 9):
        tot = triv = live = killed = 0
        for n in range(3, 61):
            for m in range(2, n):
                d2 = gcd(n, m)
                if d2 < 2:
                    continue
                M2 = n - kk - 2
                if M2 <= -m:
                    continue
                for V2 in range(1, d2 + 1):
                    r = galois_test(n, m, M2, V2, kk, "delta2")
                    if r["kills"] and r["kills"][0].startswith("H-"):
                        continue
                    tot += 1
                    if r["verdict"].startswith("INAPPLIC"):
                        triv += 1
                        continue
                    live += 1
                    if r["verdict"] == "KILLED":
                        killed += 1
        surv = live - killed
        pct = 100.0 * killed / max(live, 1)
        census_rows[kk] = (tot, triv, killed, pct, surv)
        print("  %2d %5d %5d %5d %6d %6.1f%%  %5d"
              % (kk, tot, triv, live, killed, pct, surv))

    print("\nDONE arithmetic core")
