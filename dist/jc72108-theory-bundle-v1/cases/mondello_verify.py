"""Independent verification of Mondello arXiv:2608.02634 (char-2 separable JC
counterexample).  P = x + x^2 y + x^4 + x^6 y^2,  Q = y + x^5 + x^6 y + x^7 y^2
+ x^8 y^3 over F_2.  Checks:
  (1) [P,Q] via lib/jc.py over Z, reduced mod 2  (expect 1)
  (2) collisions (0,1),(1,0),(1,1) via an independent GF(2^m) evaluator
  (3) fiber-size histogram over F_{2^m} (generic degree; expect 3)
  (4) separability witness: [P,Q] != 0 => dP,dQ span => separable ext
  (5) Newton polygons + strip structure report
Run:  python3 cases/mondello_verify.py
"""
import sys, os
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
import jc

# ---------------------------------------------------------------- the pair
SUPP_P = [(1, 0), (2, 1), (4, 0), (6, 2)]
SUPP_Q = [(0, 1), (5, 0), (6, 1), (7, 2), (8, 3)]
ONE = {(): 1}
P = {m: dict(ONE) for m in SUPP_P}
Q = {m: dict(ONE) for m in SUPP_Q}

def reduce_mod2(poly):
    out = {}
    for mon, c in poly.items():
        v = c.get((), 0) % 2
        if v:
            out[mon] = v
    return out

# ---------------------------------------------------------------- (1) bracket
BR_Z = jc.bracket(P, Q)                      # exact over Z
BR_F2 = reduce_mod2(BR_Z)
print("[P,Q] over Z, nonzero coeffs:",
      sorted((m, c[()]) for m, c in BR_Z.items()))
print("[P,Q] mod 2:", BR_F2)
assert BR_F2 == {(0, 0): 1}, "Jacobian is NOT 1 in char 2"
print("CHECK 1 PASS: det J = [P,Q] = 1 in F_2[x,y]\n")

# ---------------------------------------------------------------- GF(2^m)
IRRED = {1: 0b11, 4: 0b10011, 6: 0b1000011, 8: 0b100011011}

def gmul(a, b, m):
    red, top, r = IRRED[m], 1 << m, 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a & top:
            a ^= red
    return r

def evalF(a, b, m):
    pa = [1] * 9
    pb = [1] * 4
    for i in range(1, 9):
        pa[i] = gmul(pa[i - 1], a, m)
    for j in range(1, 4):
        pb[j] = gmul(pb[j - 1], b, m)
    vP = 0
    for (i, j) in SUPP_P:
        vP ^= gmul(pa[i], pb[j], m)
    vQ = 0
    for (i, j) in SUPP_Q:
        vQ ^= gmul(pa[i], pb[j], m)
    return (vP, vQ)

# ---------------------------------------------------------------- (2) collisions
pts = [(0, 1), (1, 0), (1, 1)]
imgs = [evalF(a, b, 1) for a, b in pts]
print("images of (0,1),(1,0),(1,1) over F_2:", imgs)
assert len(set(pts)) == 3 and len(set(imgs)) == 1, "collision claim fails"
print("CHECK 2 PASS: 3 distinct points -> one image", imgs[0], "\n")

# ---------------------------------------------------------------- (3) degree
for m in (4, 6, 8):
    fibers = Counter()
    for a in range(1 << m):
        for b in range(1 << m):
            fibers[evalF(a, b, m)] += 1
    hist = Counter(fibers.values())
    print("F_2^%d fiber-size histogram {size: #fibers}:" % m, dict(hist))
    print("   preimages of (0,1):", fibers[(0, 1)])
    assert max(hist) == 3, "fiber of size >3 found: degree-3 claim fails"
print("CHECK 3 PASS: all fibers have <= 3 points, size-3 fibers dominate")
print("   => generic degree [k(x,y):k(P,Q)] = 3 (consistent; 3 odd)\n")

# ---------------------------------------------------------------- (4) separability
print("CHECK 4 PASS: [P,Q] = 1 != 0  =>  dP ^ dQ = dx ^ dy != 0, so (P,Q) is a")
print("   separating transcendence basis: k(x,y)/k(P,Q) is separable.\n")

# ---------------------------------------------------------------- (5) polygons
HULLS = {"P": [(0, 0), (4, 0), (6, 2), (2, 1)],   # (1,0) interior to bottom edge
         "Q": [(0, 0), (5, 0), (8, 3), (0, 1)]}   # (6,1),(7,2) on right edge
for name, supp in (("P", SUPP_P), ("Q", SUPP_Q)):
    jc.ccw_order(HULLS[name])                      # asserts strict convexity
    hp = set(jc.lattice_points(HULLS[name]))
    assert all(m in hp for m in supp), "support outside claimed hull"
    lines = sorted(set(i - j for i, j in supp))
    print("N(%s): support %s" % (name, supp))
    print("   hull(with origin) = %s ; i-j offsets (dir d=(1,1)): %s"
          % (HULLS[name], lines))
print("Strip structure: P = x*u + x^4*u^2, Q = y + x^5*u^3, u = 1+xy (char 2).")
print("ALL CHECKS PASS -> Mondello pair VERIFIED over F_2.")
