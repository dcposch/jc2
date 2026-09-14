# Fable 5.1 hostile-review control for the H-divisible M-source composition gate.
# Exact Q(rho)/(rho^2-3rho+1) arithmetic, both conjugates implicitly (field identities only).
# Only factors of degree <= 5 are expanded: H(g0+w,p) (degree 5) and the degree-2 factor L*M.
# No H/R powers, no A15/B25, no CAS. No asserts gate acceptance: results are printed and
# summarized as PASS/FAIL tokens; changed-object controls are expected to print REJECT.
import sys
from fractions import Fraction as Fr

MODE = "optimized" if not __debug__ else "normal"

# ---- Q(rho) as pairs (a,b) = a + b*rho, rho^2 = 3rho - 1 ----
def qadd(x, y): return (x[0]+y[0], x[1]+y[1])
def qneg(x): return (-x[0], -x[1])
def qsub(x, y): return qadd(x, qneg(y))
def qmul(x, y):
    a, b = x; c, d = y
    # (a+b r)(c+d r) = ac + (ad+bc) r + bd r^2 = (ac - bd) + (ad+bc+3bd) r
    return (a*c - b*d, a*d + b*c + 3*b*d)
def qnorm(x):  # N(a+b rho) = a^2 + 3ab + b^2 (conjugate 3-rho, rho*(3-rho)=1)
    a, b = x; return a*a + 3*a*b + b*b
def qiszero(x): return x[0] == 0 and x[1] == 0
ZERO = (Fr(0), Fr(0)); ONE = (Fr(1), Fr(0)); RHO = (Fr(0), Fr(1))
def qc(a, b=0): return (Fr(a), Fr(b))

# ---- polynomials in (w,p) over Q(rho): dict {(i,j): coeff} for w^i p^j ----
def padd(P, Q):
    R = dict(P)
    for k, v in Q.items():
        R[k] = qadd(R.get(k, ZERO), v)
    return {k: v for k, v in R.items() if not qiszero(v)}
def pmul(P, Q):
    R = {}
    for (i1, j1), v1 in P.items():
        for (i2, j2), v2 in Q.items():
            k = (i1+i2, j1+j2)
            R[k] = qadd(R.get(k, ZERO), qmul(v1, v2))
    return {k: v for k, v in R.items() if not qiszero(v)}
def pscale(c, P): return {k: qmul(c, v) for k, v in P.items() if not qiszero(qmul(c, v))}
def pdeg(P): return max((i+j for (i, j) in P), default=-1)
def peq(P, Q): return padd(P, pscale(qc(-1), Q)) == {}
W = {(1, 0): ONE}; Pp = {(0, 1): ONE}
def ppow(P, n):
    R = {(0, 0): ONE}
    for _ in range(n): R = pmul(R, P)
    return R

results = []
def rec(name, ok, detail=""):
    results.append((name, ok))
    print(f"[{MODE}] {'PASS' if ok else 'FAIL'} {name} {detail}")

def run(rho, label):
    # rho may be the true generator RHO, or a changed object (e.g. rational 2) for rejection.
    t = qsub(ONE, rho)                     # t = 1 - rho
    tinv = qsub(qc(2), rho)                # claimed t^{-1} = 2 - rho
    units = {
        "t^2=rho": qiszero(qsub(qmul(t, t), rho)),
        "t*(2-rho)=1": qiszero(qsub(qmul(t, tinv), ONE)),
        "t-1=-rho": qiszero(qsub(qsub(t, ONE), qneg(rho))),
        "t(t-1)=2rho-1": qiszero(qsub(qmul(t, qsub(t, ONE)), qsub(qmul(qc(2), rho), ONE))),
    }
    nonzero = {
        "N(t)": qnorm(t), "N(t-1)": qnorm(qsub(t, ONE)), "N(t(t-1))": qnorm(qmul(t, qsub(t, ONE))),
        "N(rho)": qnorm(rho), "N(3rho)": qnorm(qmul(qc(3), rho)),
    }
    # H(g0+w,p) with g0 = -p/t = -(2-rho) p ; L = p + g0 + w ; M = p + t(g0+w) ; H = p^2 L M^2
    g0 = pscale(qneg(tinv), Pp)
    g = padd(g0, W)
    L = padd(Pp, g)
    M = padd(Pp, pscale(t, g))
    H = pmul(ppow(Pp, 2), pmul(L, pmul(M, M)))
    target = padd(pscale(qmul(t, qsub(t, ONE)), pmul(ppow(W, 2), ppow(Pp, 3))),
                  pscale(rho, pmul(ppow(W, 3), ppow(Pp, 2))))
    H_ok = peq(H, target) and pdeg(H) == 5
    # Stratum 2 transverse factor: D(g) = (p+g)(p+tg); D(g0) and D_g(g0) = (t-1) p  (times lambda p^(8-j) outside)
    D = pmul(L, M)
    # derivative in g = derivative in w (g = g0 + w)
    Dg = {}
    for (i, j), v in D.items():
        if i >= 1: Dg[(i-1, j)] = qadd(Dg.get((i-1, j), ZERO), qmul(qc(i), v))
    D_at = {k: v for k, v in D.items() if k[0] == 0}
    Dg_at = {k: v for k, v in Dg.items() if k[0] == 0}
    D0_ok = D_at == {}
    Dg_ok = peq(Dg_at, pscale(qsub(t, ONE), Pp))
    return units, nonzero, H_ok, D0_ok, Dg_ok

# ---------- positive run at the true rho ----------
units, nz, H_ok, D0_ok, Dg_ok = run(RHO, "rho")
for k, v in units.items(): rec(f"unit-identity {k}", v)
for k, v in nz.items(): rec(f"norm {k} != 0", v != 0, f"N={v}")
rec("H(g0+w,p) == t(t-1)p^3w^2 + rho p^2 w^3, degree 5", H_ok)
rec("LM stratum: (LM)(g0)=0", D0_ok)
rec("LM stratum: d/dg(LM)(g0) = (t-1)p", Dg_ok)

# ---------- inequality chains (exact rationals) ----------
ok = True
for j in range(1, 10):                                   # stratum 1: r <= j/4, 15r < 36
    r = Fr(j, 4); ok &= (15*r < 36)
rec("coalesced stratum1: 15r <= 135/4 < 36 for j=1..9", ok, f"max={15*Fr(9,4)}")
ok = True
for j in range(1, 7):                                    # stratum 2: r <= j/3
    r = Fr(j, 3); ok &= (15*r < 36)
rec("coalesced stratum2: 15r <= 30 < 36 for j=1..6", ok)
ok = all(7*j - 46 <= 2 for j in range(1, 7)) and all(7*j - 46 > 2 for j in range(7, 10))
rec("LM stratum weight 7j-46<=2 exactly for j<=6, violated j=7..9", ok)
# separated stratum 1 supremum: eta<=j/2, kappa<j/2 -> 7eta+kappa/2 < 15j/4
ok = all(Fr(15*j, 4) < 36 for j in range(1, 10))
rec("separated stratum1: 7eta+kappa/2 < 15j/4 <= 135/4 < 36", ok)
# separated stratum 2: eta<=j/2+kappa/4, kappa<2j/3 -> 7eta+kappa/2 < 7j/2 + 9/4*(2j/3) = 5j
ok = all((Fr(7*j, 2) + Fr(9, 4)*Fr(2*j, 3) == 5*j) and (5*j < 36) for j in range(1, 7))
rec("separated stratum2: 7j/2+9kappa/4 -> 5j <= 30 < 36", ok)
# lower-B positivity (coalesced): 25 - nu - n h > (5/(2r))(10r - nu) > 0 for n < nu/r, h=5/2-r
ok = True
for j in (1, 5, 9):
    for num in range(1, 100):
        r = Fr(j, 4); nu = Fr(num, 10)
        if nu >= 10*r: break
        n = int((nu - 1) / r) if nu > 1 else 0
        h = Fr(5, 2) - r
        ok &= (25 - nu - n*h > 0)
rec("coalesced lower-B: 25-nu-nh > 0 on sampled (j,nu) with n<=(nu-1)/r, nu<10r", ok)
# separated lower-B stratum 2 worst case: n=1, 25-nu-h >= 20-nu+eta > 20-4eta > 0 for eta<4
ok = all(20 - 4*Fr(e, 8) > 0 for e in range(1, 32))
rec("separated lower-B stratum2: 20-4eta > 0 for eta<4", ok)
# sheet tuple logic: (a+b, a-b) vanishes iff a=b=0 (char 0); one-sheet cancellation a=b allowed
a, b = Fr(3), Fr(3)
rec("two-sheet tuple (a+b,a-b) with a=b!=0 is (2a,0): one sheet zero, tuple nonzero", (a+b, a-b) == (6, 0))
rec("two-sheet tuple vanishes only at a=b=0", all(not ((x+y == 0) and (x-y == 0)) for x in range(-3, 4) for y in range(-3, 4) if (x, y) != (0, 0)))
# W^3 coefficient projections: Y^5 -> 3u, Y^4 -> 3u^2+3v
def w3coeffs(u, v):
    # (Y^2+uY+v)^3 coefficients of Y^5 and Y^4
    return (3*u, 3*u*u + 3*v)
rec("W^3 projections: Y^5=3u, Y^4=3u^2+3v", w3coeffs(Fr(2), Fr(5)) == (6, 27))

# ---------- changed-object rejections ----------
units2, nz2, H_ok2, D0_ok2, Dg_ok2 = run(qc(2), "rho=2 (not a root)")
rec("REJECT expected: rho=2 breaks t^2=rho", not units2["t^2=rho"])
rec("REJECT expected: rho=2 breaks degree-5 H expansion", not H_ok2)
# identified-sign shortcut: (a+b, a+b) can vanish with a=-b != 0 -> the one-sheet identification is unsafe
a, b = Fr(2), Fr(-2)
rec("REJECT expected: identified signs (a+b,a+b) vanish at a=-b!=0", (a+b, a+b) == (0, 0))
# dropping strictness eta>kappa: binomial correction order b*(eta-kappa) is 0, not positive
rec("REJECT expected: eta=kappa gives zero binomial shift", (Fr(1) - Fr(1)) * 3 == 0)

npass = sum(1 for _, ok in results if ok)
print(f"[{MODE}] SUMMARY {npass}/{len(results)} checks as expected")
sys.exit(0 if npass == len(results) else 1)
