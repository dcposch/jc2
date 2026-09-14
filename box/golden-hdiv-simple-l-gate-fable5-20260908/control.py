# Tiny exact controls for the simple-L referee gate. Finite instances only; not the proof.
# 1. Simple L root: H(-p,p)=0 and H_g(-p,p)=rho^2 p^4 in Q[rho]/(rho^2-3rho+1) (covers both embeddings).
# 2. Lower-B lemma identities on Euler-homogeneous instances, with a non-monic changed-object negative.
# 3. Monic 3/5 common-power: cube-root residual for depressed cubic (nonzero) vs (Z+p)^3 (zero, negative control).
import sys
from fractions import Fraction as Fr

MODE = sys.argv[1] if len(sys.argv) > 1 else "positive"

# --- Q(rho) as pairs (a,b) = a + b*rho, rho^2 = 3rho - 1 ---
def qm(x, y):
    a, b = x; c, d = y
    return (a*c - b*d, a*d + b*c + 3*b*d)
def qa(x, y): return (x[0]+y[0], x[1]+y[1])
ZERO = (Fr(0), Fr(0)); ONE = (Fr(1), Fr(0)); RHO = (Fr(0), Fr(1))
T = (Fr(1), Fr(-1))  # t = 1 - rho

# polynomials in (g,p): dict (i,j)->Q(rho)
def pmul(A, B):
    C = {}
    for (i, j), x in A.items():
        for (k, l), y in B.items():
            C[(i+k, j+l)] = qa(C.get((i+k, j+l), ZERO), qm(x, y))
    return {k: v for k, v in C.items() if v != ZERO}
def padd(A, B):
    C = dict(A)
    for k, v in B.items(): C[k] = qa(C.get(k, ZERO), v)
    return {k: v for k, v in C.items() if v != ZERO}
def dg(A):
    return {(i-1, j): qm((Fr(i), Fr(0)), x) for (i, j), x in A.items() if i > 0}
def at_minus_p(A):  # substitute g=-p, return dict deg->Q(rho)
    R = {}
    for (i, j), x in A.items():
        s = qm(((-1)**i * Fr(1), Fr(0)), x)
        R[i+j] = qa(R.get(i+j, ZERO), s)
    return {k: v for k, v in R.items() if v != ZERO}

g = {(1, 0): ONE}; p = {(0, 1): ONE}
L = padd(p, g); M = padd(p, pmul({(0, 0): T}, g))
if MODE == "wrong-root":
    M = padd(p, g)  # changed object: M:=L makes the L root double
H = pmul(pmul(p, p), pmul(L, pmul(M, M)))
Hval = at_minus_p(H); Hg = at_minus_p(dg(H))
rho2 = qm(RHO, RHO)
print("H(-p,p) =", Hval, "expected {}")
print("H_g(-p,p) =", Hg, "expected {4: rho^2 =", rho2, "}")
print("CHECK1", "PASS" if (Hval == {} and Hg == {4: rho2}) else "FAIL")

# --- polynomials in (Z,p) with rational coefficients: dict (zdeg,pdeg)->Fr ---
def mul(A, B):
    C = {}
    for (i, j), x in A.items():
        for (k, l), y in B.items():
            C[(i+k, j+l)] = C.get((i+k, j+l), 0) + x*y
    return {k: v for k, v in C.items() if v != 0}
def add(A, B, cB=1):
    C = dict(A)
    for k, v in B.items(): C[k] = C.get(k, 0) + cB*v
    return {k: v for k, v in C.items() if v != 0}
def dZ(A): return {(i-1, j): i*x for (i, j), x in A.items() if i != 0}
def dp(A): return {(i, j-1): j*x for (i, j), x in A.items() if j != 0}
def scal(A, c): return {k: c*v for k, v in A.items()}
def euler(A, h): return add(mul({(0, 1): Fr(1)}, dp(A)), scal(mul({(1, 0): Fr(1)}, dZ(A)), h))
def br(A, B): return add(mul(dZ(A), dp(B)), mul(dp(A), dZ(B)), -1)
def top(A):
    m = max(i for (i, j) in A); return {k: v for k, v in A.items() if k[0] == m}
Z = {(1, 0): Fr(1)}; P1 = {(0, 1): Fr(1)}
def mono(c, zi, pj): return {(zi, pj): Fr(c)}

# instance eta=4 (j=8), h=1: P=Z^3+uZ+v, Q=Z^5+(5/3)uZ^3+(5/3)vZ^2+lam Z+e
h = Fr(1)
P = add(add(mono(1, 3, 0), mono(2, 1, 2)), mono(3, 0, 3))
Q = add(add(add(add(mono(1, 5, 0), mono(Fr(10, 3), 3, 2)), mono(5, 2, 3)), mono(7, 1, 4)), mono(11, 0, 5))
if MODE == "nonmonic":
    P = add(P, mono(1, 3, 0), -1); P = add(P, mono(1, 3, 1))  # P = p Z^3 + uZ + v (Euler degree 4)
eP = euler(P, h); eQ = euler(Q, h)
degP = 4 if MODE == "nonmonic" else 3
print("Euler P:", eP == scal(P, degP*h), "Euler Q:", eQ == scal(Q, 5*h))
lhs = mul(P1, br(P, Q)); rhs = scal(add(scal(mul(dZ(P), Q), 5), scal(mul(P, dZ(Q)), 3), -1), h)
print("p[P,Q]==h(5P_Z Q-3P Q_Z):", lhs == rhs, "(identity needs both Euler-homogeneous with the same h)")
bt = {k: v for k, v in br(P, Q).items() if k[0] == 7}
print("Z^(m+n-1)=Z^7 part of [P,Q]:", bt, " expected {} for monic P (m q_n' = 0); non-monic gives -n p_m' q_n")
e_pos = mono(4, 0, 9)  # Lambda = 9 > 0
e_zero = mono(4, 0, 0)  # Lambda = 0
print("[P, 4p^9] Z^2 coeff:", br(P, e_pos).get((2, 8)), "(=3*e', nonzero: positive Euler degree cannot commute)")
print("[P, 4] :", br(P, e_zero), "(Lambda=0 constant commutes)")
print("CHECK2", "PASS" if (bt == {} and br(P, e_pos).get((2, 8)) == 108 and br(P, e_zero) == {}) else ("FAIL(expected in nonmonic mode)" if MODE == "nonmonic" else "FAIL"))

# --- 3/5 common power: monic cube root of P^5, top-down ---
def cube_root_residual(P):
    P5 = P
    for _ in range(4): P5 = mul(P5, P)
    Qc = mono(1, 5, 0)
    for k in range(4, -1, -1):
        Q3 = mul(mul(Qc, Qc), Qc)
        diff = add(P5, Q3, -1)
        row = {j: v for (i, j), v in diff.items() if i == 10 + k}
        for j, v in row.items(): Qc = add(Qc, mono(v / 3, k, j))  # (Z^5)^2*3*q_k Z^k p^j
    Q3 = mul(mul(Qc, Qc), Qc)
    return Qc, add(P5, Q3, -1)
Pd = add(add(mono(1, 3, 0), mono(2, 1, 2)), mono(3, 0, 3))
Pc = add(add(add(mono(1, 3, 0), mono(3, 2, 1)), mono(3, 1, 2)), mono(1, 0, 3))  # (Z+p)^3
Pz = mono(1, 3, 0)
for name, PP in (("depressed Z^3+2p^2Z+3p^3", Pd), ("(Z+p)^3 non-depressed", Pc), ("Z^3", Pz)):
    Qc, res = cube_root_residual(PP)
    print(name, ": residual P^5-Q^3 nonzero?", bool(res), " Q found:", sorted(Qc.items())[:6])
_, r1 = cube_root_residual(Pd); _, r2 = cube_root_residual(Pc); _, r3 = cube_root_residual(Pz)
print("CHECK3", "PASS" if (bool(r1) and not r2 and not r3) else "FAIL")
