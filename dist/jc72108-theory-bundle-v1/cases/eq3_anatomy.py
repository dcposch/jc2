"""Task 1: identify which bracket coefficient original equation #3 is
(open_8_28_c2 normalized system), and locate it geometrically."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from jc import SystemA, lattice_points, bracket, padd
from emit import CASES, FIX

n = "open_8_28_c2"
S = SystemA(n, CASES[n]["cornersP"], CASES[n]["cornersQ"], CASES[n]["rhs"],
            nonvanish="nonorigin", fix_ones=FIX[n])

# rebuild E to recover the key ordering (SystemA discards keys)
def coef(kind, pt):
    if (kind, pt) in S.fix:
        return {(): 1}
    return {(S.varof[(kind, pt)],): 1}
P = {pt: coef("P", pt) for pt in S.ptsP}
Q = {pt: coef("Q", pt) for pt in S.ptsQ}
E = padd(bracket(P, Q), {CASES[n]["rhs"]: {(): -1}})
keys = sorted(E.keys())
assert len(keys) == len(S.equations) - 1
print("n_eqs(bracket) =", len(keys), " first 8 keys:", keys[:8])
k3 = keys[3]
print("KEY of equation index 3:", k3)
eq3 = S.equations[3]
print("equation 3 (raw):", {tuple(S.varnames[i] for i in m): v for m, v in eq3.items()})

# decompositions p+q = key+(1,1)
tgt = (k3[0] + 1, k3[1] + 1)
sp, sq = set(S.ptsP), set(S.ptsQ)
dec = [(p, (tgt[0]-p[0], tgt[1]-p[1])) for p in sp if (tgt[0]-p[0], tgt[1]-p[1]) in sq]
print("Minkowski point", tgt, "decompositions:",
      [(p, q, p[0]*q[1]-p[1]*q[0]) for p, q in dec])

# var identities
for kind, pt in [("P", (1, 0)), ("Q", (2, 1)), ("Q", (12, 21))]:
    print(kind, pt, "->", S.varnames[S.varof[(kind, pt)]])

# strip descriptions (w = 2i - j)
for name, pts in (("P", S.ptsP), ("Q", S.ptsQ)):
    ws = sorted({2*p[0]-p[1] for p in pts if p != (0, 0)})
    print(f"{name}: {len(pts)} pts, w=2i-j range {ws[0]}..{ws[-1]}")

# w-value of each early key; rhs key w
print("keys 0-5 with w=2i-j:", [(k, 2*k[0]-k[1]) for k in keys[:6]])
print("rhs monomial:", CASES[n]["rhs"], "is key index", keys.index(CASES[n]["rhs"]))

# Minkowski sum vertex check: is tgt a vertex of N(P)+N(Q)?
mink = sorted({(p[0]+q[0], p[1]+q[1]) for p in sp for q in sq})
from jc import ccw_order
cornersM = []
# convex hull of mink via monotone chain
def hull(pts):
    pts = sorted(set(pts))
    def half(ps):
        h = []
        for p in ps:
            while len(h) >= 2 and (h[-1][0]-h[-2][0])*(p[1]-h[-2][1]) - (h[-1][1]-h[-2][1])*(p[0]-h[-2][0]) <= 0:
                h.pop()
            h.append(p)
        return h
    lo, up = half(pts), half(pts[::-1])
    return lo[:-1] + up[:-1]
H = hull(mink)
print("Minkowski hull vertices:", H)
print("tgt on hull:", tgt in H)
