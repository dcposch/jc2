"""Toy verification of Wilson (arXiv:2607.23887) Lemma 7 mechanics (moment world).

P = Z^2 W + Z W^2 + t Z^5,  support S = {a1=(2,1), a2=(1,2), a3=(5,0)}.
Face for l(a,b)=a+b (c=d=1): F = {a1,a2}, lambda=3, lambda/(c+d)=3/2, B=2.
Face weight polynomial R(z) = z + z^-1 (weights wt = a-b on F are +1,-1: MIXED).

Wilson: at m = qp with q=Bn, good prime p (here p=7 > R0 = q*lambda/(c+d) = 3):
  - pure-face strata (k3=0) sum to (p*R0)! * CT(R^{qp}), 7-adic valuation exactly R0;
  - every mixed stratum (k3>0) has valuation >= R0+1.
E(P^m) = sum over k=(k1,k2,k3), |k|=m, balanced (A(k)=B(k) i.e. k1+5k3=k2) of
  multinom(m;k) * t^{k3} * A(k)!   with A(k)=2k1+k2+5k3.
"""
from math import comb, factorial

def multinom(m, ks):
    out, rem = 1, m
    for k in ks:
        out *= comb(rem, k); rem -= k
    return out

def vp(n, p):
    if n == 0: return None  # +infinity
    v = 0
    while n % p == 0: n //= p; v += 1
    return v

def strata(m):
    """balanced strata for support {(2,1),(1,2),(5,0)}: k1 + 5*k3 = k2."""
    out = []
    for k3 in range(m + 1):
        for k1 in range(m + 1 - k3):
            k2 = k1 + 5 * k3
            if k1 + k2 + k3 == m:
                A = 2 * k1 + k2 + 5 * k3
                out.append(((k1, k2, k3), multinom(m, (k1, k2, k3)) * factorial(A)))
    return out

q, p = 2, 7           # B=2, n=1; good prime: p unramified/integral (Z), p>R0=3, p not| c+d=2
R0 = q * 3 // 2       # q*lambda/(c+d) = 3
m = q * p             # 14
print(f"m = qp = {m},  R0 = {R0},  p = {p}")
pure, mixed = [], []
for (k, val) in strata(m):
    (pure if k[2] == 0 else mixed).append((k, val, vp(val, p)))
for k, val, v in pure + mixed:
    tag = "PURE-FACE" if k[2] == 0 else "mixed    "
    print(f"  {tag} k={k}: multinom*A! = {val}  v_7 = {v}")

# Wilson's identity for the pure-face total: (p*R0)! * CT(R^{qp}), R = z + 1/z
ct = comb(m, m // 2)  # CT((z+1/z)^14) = C(14,7)
pf_total = sum(val for k, val, v in pure)
print(f"pure-face total = {pf_total}; (pR0)!*CT(R^qp) = {factorial(p*R0)*ct}; "
      f"equal: {pf_total == factorial(p*R0)*ct}; v_7(pure)={vp(pf_total,p)} (=R0), "
      f"v_7(mixed) >= {min(v for _,_,v in mixed)} (claim: >= R0+1={R0+1})")

# Bad prime (violates G4: p <= R0) for contrast
pb = 3; mb = q * pb
print(f"\ncontrast, bad prime p={pb} (fails G4: p <= R0), m={mb}:")
for (k, val) in strata(mb):
    print(f"  {'PURE-FACE' if k[2]==0 else 'mixed    '} k={k}: v_3 = {vp(val, pb)}")

# and the theorem's content on this toy: mixed-sign face => moments can't all vanish
E2 = sum(val for _, val in strata(2))  # t-free (k3=0 stratum only at m=2)
print(f"\nE(P^2) = {E2} (t-free, nonzero) => no t makes all moments vanish, "
      f"as forced by mixed-sign R: CT(R^2) = {comb(2,1)} != 0")
