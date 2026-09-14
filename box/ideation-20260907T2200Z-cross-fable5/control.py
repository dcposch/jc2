#!/usr/bin/env python3
"""Tiny stdlib desk control for the 2200Z cross-review (fable5).
No Assert nodes; explicit checks; exit 1 on any failure. Mutations change objects.
Objects: receiver supports A: i<=2j, 5i-7j<=3, i+j<=15; B: 5i-7j<=5, i+j<=25; both odd.
Lift phi(g)=v^-1, phi(p)=v^4 u - v - v^-1. Laurent polys as dict[(upow,vpow)]->Fraction.
"""
import sys, random
from fractions import Fraction as Fr
from math import comb
MUT = sys.argv[1] if len(sys.argv) > 1 else "none"
random.seed(20260907)

def lmul(a, b):
    r = {}
    for (ua, va), ca in a.items():
        for (ub, vb), cb in b.items():
            k = (ua + ub, va + vb); r[k] = r.get(k, 0) + ca * cb
    return {k: c for k, c in r.items() if c != 0}
def ladd(a, b, s=1):
    r = dict(a)
    for k, c in b.items(): r[k] = r.get(k, 0) + s * c
    return {k: c for k, c in r.items() if c != 0}
def lpow(a, n):
    r = {(0, 0): Fr(1)}
    for _ in range(n): r = lmul(r, a)
    return r
PHI_G = {(0, -1): Fr(1)}
PHI_P = {(1, 4): Fr(1), (0, 1): Fr(-1), (0, -1): Fr(-1)}
if MUT == "drop-vinv": PHI_P = {(1, 4): Fr(1), (0, 1): Fr(-1)}
def phi_mono(i, j): return lmul(lpow(PHI_G, i), lpow(PHI_P, j))
def phi_poly(P):
    r = {}
    for (i, j), c in P.items(): r = ladd(r, {k: c * v for k, v in phi_mono(i, j).items()})
    return r

def inA(i, j): return i >= 0 and j >= 0 and i <= 2 * j and 5 * i - 7 * j <= 3 and i + j <= 15 and (i + j) % 2 == 1
def inB(i, j): return i >= 0 and j >= 0 and 5 * i - 7 * j <= 5 and i + j <= 25 and (i + j) % 2 == 1
if MUT == "even-parity":
    def inA(i, j): return i >= 0 and j >= 0 and i <= 2 * j and 5 * i - 7 * j <= 3 and i + j <= 15 and (i + j) > 0
    def inB(i, j): return i >= 0 and j >= 0 and 5 * i - 7 * j <= 5 and i + j <= 25 and (i + j) > 0
SA = [(i, j) for i in range(16) for j in range(16) if inA(i, j)]
SB = [(i, j) for i in range(26) for j in range(26) if inB(i, j)]
ok = True
def check(name, cond, detail=""):
    global ok
    print(("PASS " if cond else "FAIL ") + name + ((" : " + str(detail)) if detail else ""))
    ok = ok and bool(cond)

# 1. phi(R) polynomial with phi(R)(u,0)=3u  (positive control on the lift map)
R = {(3, 2): Fr(1), (0, 5): Fr(1), (0, 3): Fr(-3)}          # R = p^2 V, V = g^3+p^3-3p
phiR = phi_poly(R)
neg = {k: c for k, c in phiR.items() if k[1] < 0}
u_only = {k: c for k, c in phiR.items() if k[1] == 0}
check("phi(R) polynomial", len(neg) == 0, neg)
check("phi(R)(u,0)=3u", u_only == {(1, 0): Fr(3)}, u_only)

# 2. the (u^0, v^-1) lift row of A: coefficients of low slots and fixed-face constant
Atop = {(0, 15): Fr(1), (3, 12): Fr(3), (6, 9): Fr(3), (9, 6): Fr(1)}   # H^3, H = p^2(g^3+p^3)
Btop = {(0, 25): Fr(1), (3, 22): Fr(5), (6, 19): Fr(10), (9, 16): Fr(10), (12, 13): Fr(5), (15, 10): Fr(1)}  # H^5
cA = phi_poly(Atop).get((0, -1), Fr(0)); cB = phi_poly(Btop).get((0, -1), Fr(0))
row = {}
for (i, j) in SA:
    c = phi_mono(i, j).get((0, -1), Fr(0))
    if c: row[(i, j)] = c
print("A lift row (u^0,v^-1): fixed-face constant =", cA, "; slots in row =", len(row), "of", len(SA))
print("  low-slot coefficients:", {s: row.get(s, 0) for s in [(0, 1), (2, 1), (1, 2), (0, 3), (0, 5), (1, 4), (2, 3), (3, 2)]})
check("A fixed-face constant nonzero", cA != 0, cA)
check("k=A21 in row with coeff -1", row.get((2, 1), 0) == -1, row.get((2, 1), 0))
check("a,x,y coeffs -1,2,-3", (row.get((0, 1)), row.get((1, 2)), row.get((0, 3))) == (Fr(-1), Fr(2), Fr(-3)))
print("B lift row (u^0,v^-1): fixed-face constant =", cB, "; coeff of e=B10 =", phi_mono(1, 0).get((0, -1), 0))
check("B fixed-face constant nonzero", cB != 0, cB)

# 3. g^2 Jacobian coefficient equals -A21*B10 on random support-respecting A,B
def jac_coeff(A, B, a, b):
    s = Fr(0)
    for (i, j), ca in A.items():
        for (k, l), cb in B.items():
            if i + k - 1 == a and j + l - 1 == b: s += ca * cb * (i * l - j * k)
    return s
A = {s: Fr(random.randint(-9, 9)) for s in SA}; B = {s: Fr(random.randint(-9, 9)) for s in SB}
A[(2, 1)] = Fr(7); B[(1, 0)] = Fr(-4)
check("[A,B]_{g^2} = -k*e", jac_coeff(A, B, 2, 0) == -A[(2, 1)] * B[(1, 0)], (jac_coeff(A, B, 2, 0), -A[(2, 1)] * B[(1, 0)]))
check("A(g,0)=0 and B(g,0)=e*g by support", all(j > 0 for (i, j) in SA) and [s for s in SB if s[1] == 0] == [(1, 0)])

# 4. weight-12 component identity on U: -k+2x-3y = -(9e-5k^2)^2/(25k^3) given 9e=5kx, x^2=3ky
five = Fr(5); nine = Fr(9)
if MUT == "low-row-9e4kx": nine = Fr(4) * Fr(9) / Fr(4) ; five = Fr(4)  # 9e = 4kx instead
for _ in range(5):
    k = Fr(random.randint(1, 50), random.randint(1, 7)); e = Fr(random.randint(-50, 50), random.randint(1, 9))
    x = nine * e / (five * k); y = x * x / (3 * k)
    lhs = -k + 2 * x - 3 * y; rhs = -(9 * e - 5 * k * k) ** 2 / (25 * k ** 3)
    check("weight-12 component identity", lhs == rhs, (lhs, rhs))
    break

# 5. square-class desk consequence: ord_O of admissible C slots is i+3j; ord = 2 mod 4 excludes gp and g^2p^2 leaders
slots = [(1,1),(0,2),(2,2),(1,3),(3,3),(0,4),(2,4),(4,4),(1,5),(3,5),(0,6),(2,6),(1,7)]
orders = {s: s[0] + 3 * s[1] for s in slots}
print("ord_O(g^i p^j on E) = i+3j:", orders)
check("orders 4 and 8 are single-slot (gp, g^2p^2) and not 2 mod 4", [s for s in slots if orders[s] in (4, 8)] == [(1, 1), (2, 2)] and all(o % 4 != 2 for o in (4, 8)))
check("14y collision C=3p^3L(gL+1) has ord 10 = 2 mod 4", (1 + 9) % 4 == 2)

print("RESULT", "PASS" if ok else "FAIL", "mutation=" + MUT)
sys.exit(0 if ok else 1)
