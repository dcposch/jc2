#!/usr/bin/env python3
"""SHEET6 pilot: machine-rederivation of Sigray thesis (sigray_full.pdf) Prop 9.1
table (23) and Statement 9.6 Diophantine propagation from Q(G) = (j,2j,3,2,5).

Constraints transcribed verbatim (see SHEET6-PILOT.md extraction, pp. 26-27, 45-53):
  Notation 5.3 multiplicity data: {type (alpha,beta); (D_gF,D_F); nu_F; (deg pF, deg p_gF)}
  St 5.2(i):  deg(pF)/deg(p_gF) = D_F/D_gF = alpha/beta
  St 5.2(ii): [nu|alpha and nu|deg(p_gF)-1]  OR  [nu|beta and nu|deg(pF)-1]
  (19)/Prop 5.6: Lambda(F) = D_gF*deg(pF)/nu_F  (sum of pole orders => positive integer)
  Prop 5.7:  Lambda(F) >= beta;  type: 1 < alpha < beta, gcd(alpha,beta)=1
  Stmt 9.6 core (p. 52), case mult(p,c)=2, II(a), k!=0 (l=0 by St 8.2):
      (k+2)nu/((k+1)nu+1) = deg(p)/deg(q) = (D_G+n*deg p_G)/(i*(kappa_G(1-v)+n)) = (1+2n)/(5+n)
      k,n in N*, nu in N*\\{1}, n = 3m+1 (m in N)  [integrality of 9.3(d): (5+n)/3 in N]
  k=0 sub-case: deg p = 2nu, deg q = (l+1)nu+1, same RHS.
Exact integer arithmetic only; every branch has a completeness certificate.
"""
from math import gcd

# ---------------- Part 1: Prop 9.1 table (23) ----------------
THESIS_TABLE = {  # ((alpha,beta),(D_F,D_gF),(deg pF,deg p_gF),nu,Lambda)
    ((2,3),(2,3),(2,3),2,3), ((2,3),(2,3),(2,3),1,6), ((2,3),(4,6),(2,3),2,6),
    ((2,3),(2,3),(4,6),3,4), ((3,4),(3,4),(3,4),3,4), ((3,4),(3,4),(3,4),2,6),
    ((2,5),(2,5),(2,5),2,5), ((2,5),(2,5),(6,15),5,6), ((3,5),(3,5),(6,10),5,6),
    ((4,5),(4,5),(4,5),4,5), ((5,6),(5,6),(5,6),5,6),
}

def prop91(Lmax=6, BETA_SWEEP=60, AB_SWEEP=40):
    """All multiplicity data with Lambda(F) <= Lmax.
    Bounds: nu | alpha or nu | beta => nu <= beta. Lambda = a*beta*b*alpha/nu >= ab*alpha
    => ab <= Lmax/alpha <= Lmax/2 (a,b sweep safe). Prop 5.7 proof (from St 5.2(ii))
    gives Lambda >= beta => beta <= Lmax; oversweep to BETA_SWEEP re-verifies."""
    rows = set()
    for beta in range(3, BETA_SWEEP + 1):
        for alpha in range(2, beta):
            if gcd(alpha, beta) != 1:
                continue
            for a in range(1, AB_SWEEP + 1):
                for b in range(1, AB_SWEEP + 1):
                    P, Pg = b * alpha, b * beta
                    for nu in range(1, beta + 1):
                        ok1 = alpha % nu == 0 and (Pg - 1) % nu == 0
                        ok2 = beta % nu == 0 and (P - 1) % nu == 0
                        if not (ok1 or ok2):
                            continue
                        num = (a * beta) * P
                        assert num % nu == 0, "Lambda integrality is automatic"
                        Lam = num // nu
                        if Lam > Lmax:
                            continue
                        assert Lam >= beta, "Prop 5.7 check"
                        rows.add(((alpha, beta), (a*alpha, a*beta), (P, Pg), nu, Lam))
    return rows

# ---------------- Part 2: Stmt 9.6, k != 0 branch ----------------
def stmt96_knonzero(K_SWEEP=2000, NU_SWEEP=2000):
    """All (k,nu,n), k>=1, nu>=2, n>=1 with (k+2)nu(5+n) == ((k+1)nu+1)(1+2n).
    Closed form n(k*nu+2) = nu(4k+9)-1, i.e. n = 4 + 9(nu-1)/(k*nu+2).
    Completeness: (k*nu+2) | 9(nu-1) and k*9(nu-1) = 9(k*nu+2) - 9(k+2)*2/2... precisely
    9k(nu-1) = 9(k*nu+2) - 9(k+2) - 9  => (k*nu+2) | 9(k+2)+9 - is checked directly:
    9k(nu-1) = 9k*nu - 9k = 9(k*nu+2) - (9k+18) => (k*nu+2) | 9(k+2) => nu <= 9+16/k <= 25;
    n>=1 => 9(nu-1) >= k*nu+2 => nu(9-k) >= 11 => k <= 8. Oversweep asserts the box."""
    sols = []
    for k in range(1, K_SWEEP + 1):
        for nu in range(2, NU_SWEEP + 1):
            num, den = nu * (4 * k + 9) - 1, k * nu + 2
            if num % den:
                continue
            n = num // den
            if n < 1:
                continue
            assert (k + 2) * nu * (5 + n) == ((k + 1) * nu + 1) * (1 + 2 * n)
            sols.append((k, nu, n))
    assert all(k <= 8 and nu <= 25 for k, nu, _ in sols), "solution outside proven box"
    return sols

def qtuple_from(k, nu, n):
    """Q(F) via Prop 9.3 (a)-(d) with Q(G)=(j,2j,3,2,5), i=j. Coefficients of j
    where applicable: D_F=(1+2n)j/3, deg p_F=deg(p)*j, nu_F=nu, M_F=gcd(degp,degq),
    kappa_F(1-pi(F))=(5+n)/3. Returns None marker if an integrality filter fails."""
    degp, degq = (k + 2) * nu, (k + 1) * nu + 1
    DF3, kap3 = 1 + 2 * n, 5 + n
    ok = DF3 % 3 == 0 and kap3 % 3 == 0  # both <=> n = 3m+1
    return (degp, degq, DF3 // 3 if ok else None, nu, gcd(degp, degq),
            kap3 // 3 if ok else None, ok)

# ---------------- Part 3: Stmt 9.6, k = 0 branch ----------------
def stmt96_k0(L_SWEEP=60, NU_SWEEP=5000):
    """All (l,nu,n), l>=0, nu>=2, n>=1 with 2nu(5+n) == ((l+1)nu+1)(1+2n).
    Closed form 2n(l*nu+1) = nu(9-l)-1. Completeness: n>=1 => nu(9-3l) >= 3 => l <= 2;
    l=1: RHS odd, LHS even -> none; l=2: 2(7nu-1) = 7(2nu+1)-9 => (2nu+1)|9 => nu in {1,4},
    nu=4 -> 2n=3 odd -> none; l=0: 2n = 9nu-1 -> nu odd = 2s+1, n = 9s+4 (infinite family).
    Sweep verifies the finite l-range; the l=0 family is an identity in s."""
    found = []
    for l in range(0, L_SWEEP + 1):
        for nu in range(2, NU_SWEEP + 1):
            num, den = nu * (9 - l) - 1, 2 * (l * nu + 1)
            if num <= 0 or num % den:
                continue
            n = num // den
            if n < 1:
                continue
            assert 2 * nu * (5 + n) == ((l + 1) * nu + 1) * (1 + 2 * n)
            found.append((l, nu, n))
    for l, nu, n in found:
        s = (nu - 1) // 2
        assert l == 0 and nu % 2 == 1 and nu >= 3 and n == 9 * s + 4 and n % 3 == 1
        # thesis family (v): Q(F) = ((6s+3)j,(4s+2)j,2s+1,2,3s+3), M_F=2, all j
        assert (1 + 2 * n) // 3 == 6 * s + 3 and 2 * nu == 4 * s + 2
        assert (5 + n) // 3 == 3 * s + 3 and gcd(2 * nu, nu + 1) == 2
    return found

# ---------------- Verdicts ----------------
if __name__ == "__main__":
    got = prop91()
    print(f"[Prop 9.1] enumerated {len(got)} rows; thesis table has {len(THESIS_TABLE)}")
    extra, missing = got - THESIS_TABLE, THESIS_TABLE - got
    for r in sorted(extra):   print("  EXTRA  :", r)
    for r in sorted(missing): print("  MISSING:", r)
    p91 = "PASS (exact match)" if not extra and not missing else "DISCREPANCY"
    print(f"[Prop 9.1] {p91}")

    print("\n[Stmt 9.6 k!=0] all solutions of (k+2)nu(5+n)=((k+1)nu+1)(1+2n), k>=1,nu>=2,n>=1:")
    all_sols = stmt96_knonzero()
    kept = []
    for k, nu, n in all_sols:
        degp, degq, DF, nuF, MF, kap, ok = qtuple_from(k, nu, n)
        tag = "KEPT  (n=3m+1)" if n % 3 == 1 else "KILLED (n%3!=1 => (1+2n)/3,(5+n)/3 not in N)"
        q = f"Q(F)=({DF}j,{degp}j,{nuF},{MF},{kap})" if ok else f"M_F={MF}"
        print(f"  k={k:>2} nu={nu:>2} n={n:>2}  (deg p,deg q)=({degp},{degq})  {q}  {tag}")
        if n % 3 == 1:
            kept.append((degp, degq))
    expected = [(21, 15), (75, 51), (20, 16)]
    print(f"  admissible pairs under thesis's stated constraints: {kept}")
    print(f"  thesis claims (A),(B),(C): {expected}")
    # thesis-internal check of printed (B) k=1,n=13,nu=25:
    b_eq = (1 + 2) * 25 * (5 + 13) == ((1 + 1) * 25 + 1) * (1 + 2 * 13)
    print(f"  printed (B) k=1,n=13,nu=25 satisfies equation: {b_eq}"
          f"  [75*18={75*18} vs 51*27={51*27}]")
    print(f"  corrected (B)-branch (k=1,nu=25) forces n={ (25*13-1)//27 }"
          f" (27n={25*13-1}), n%3={((25*13-1)//27)%3} -> fails n=3m+1")

    print("\n[Stmt 9.6 k=0] sweep: all solutions have l=0, nu=2s+1, n=9s+4 "
          f"({len(stmt96_k0())} in sweep box; infinite family (v) verified, M_F=2)")

    verdict = ("PASS" if sorted(kept) == sorted(expected) else "DISCREPANCY")
    print(f"\n[Stmt 9.6] {verdict}: enumeration gives {sorted(kept)}, "
          f"thesis lists {sorted(expected)}")
