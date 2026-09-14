#!/usr/bin/env python3
"""Independent D125 source-contract gate controls (Fable lane, 2026-09-06).

stdlib only, exact Fractions, fail-closed: any mismatch raises and the
process exits nonzero.  Transforms are implemented by literal substitution
(power products), NOT by the producer's binomial-expansion routes, so the
agreement below is an independent check of the same identities.
Scope: tiny maps, exact ranks, scalar counts.  No ideal, no solve, no witness.
"""
import json, sys, time
from fractions import Fraction as F
from math import comb
from random import Random

T0 = time.time()
# ---------- exact bivariate Laurent dict arithmetic ----------
def cl(p): return {e: c for e, c in p.items() if c}
def add(p, q):
    r = dict(p)
    for e, c in q.items(): r[e] = r.get(e, 0) + c
    return cl(r)
def neg(p): return {e: -c for e, c in p.items()}
def mul(p, q):
    r = {}
    for (a, b), c in p.items():
        for (d, e), f in q.items():
            r[(a + d, b + e)] = r.get((a + d, b + e), 0) + c * f
    return cl(r)
def pw(p, n):
    r = {(0, 0): F(1)}
    for _ in range(n): r = mul(r, p)
    return r
def der(p, k):
    r = {}
    for e, c in p.items():
        if e[k]:
            f = list(e); f[k] -= 1
            r[tuple(f)] = r.get(tuple(f), 0) + c * e[k]
    return cl(r)
def jac(p, q): return add(mul(der(p, 0), der(q, 1)), neg(mul(der(p, 1), der(q, 0))))
def subst(p, img0, img1):
    """Substitute variable images (dicts) by power products; exponents must be >=0."""
    r = {}
    for (a, b), c in p.items():
        assert a >= 0 and b >= 0
        r = add(r, {e: c * v for e, v in mul(pw(img0, a), pw(img1, b)).items()})
    return r
def check(cond, msg):
    if not cond: raise AssertionError(msg)

X = {(1, 0): F(1)}; Y = {(0, 1): F(1)}
Xinv = {(-1, 0): F(1)}
def Phi(p):            # u -> X^5, v -> Y + X^-1  (ring hom Q[u,v] -> Q[X^±1,Y])
    return subst(p, pw(X, 5), add(Y, Xinv))
def untranslate(p):    # Y -> v - X^-1 in Q[X^±1][Y]
    r = {}
    for (a, b), c in p.items():
        assert b >= 0
        r = add(r, {e: c * v for e, v in mul({(a, 0): F(1)}, pw(add(Y, neg(Xinv)), b)).items()})
    return r
def in_image(p):
    q = untranslate(p)
    return all(a >= 0 and a % 5 == 0 and b >= 0 for (a, b) in q)
def descend(p):
    q = untranslate(p)
    check(all(a >= 0 and a % 5 == 0 and b >= 0 for (a, b) in q), "not in translated image")
    return {(a // 5, b): c for (a, b), c in q.items()}
def naive_in_image(p):  # WRONG test: trivial X characters BEFORE untranslation
    return all(a >= 0 and a % 5 == 0 and b >= 0 for (a, b) in p)
def to_tz(p):           # X = t z, Y = z^-1  : X^a Y^b -> t^a z^(a-b)
    return cl({(a, a - b): c for (a, b), c in p.items()})

out = {}
rng = Random(20260906)
def rand_poly(box, den=7):
    return cl({(i, j): F(rng.randint(-9, 9), rng.randint(1, den)) for (i, j) in box})

# ---------- Arrow 1: injectivity on a random sample, untranslate-first, chart bracket ----------
box = [(i, j) for i in range(4) for j in range(5)]
p = rand_poly(box); q = rand_poly(box)
check(descend(Phi(p)) == p and descend(Phi(q)) == q, "descend(Phi) != id")
check(Phi(add(p, neg(p))) == {} and Phi(p) != {}, "Phi zero/nonzero")
# untranslate-first is the right test; the naive character test fails both ways
phiv = Phi({(0, 1): F(1)})                       # Y + X^-1
check(in_image(phiv) and not naive_in_image(phiv), "Phi(v) must pass only the untranslated test")
bad = {(5, 1): F(1)}                             # X^5 Y : naive passes, untranslate gives -X^4 term
check(naive_in_image(bad) and not in_image(bad), "X^5 Y must be rejected only after untranslation")
out["arrow1_untranslate_first"] = {"Phi(v)": "image, naive rejects", "X^5*Y": "not image, naive accepts"}
# chain rule J_{X,Y}(Phi P,Phi Q) = 5 X^4 Phi(J_{u,v}(P,Q)) on random P,Q
lhs = jac(Phi(p), Phi(q)); rhs = mul({(4, 0): F(5)}, Phi(jac(p, q)))
check(lhs == rhs, "chain rule factor 5 X^4 failed")
check(lhs != mul({(4, 0): F(-5)}, Phi(jac(p, q))), "sign mutation not detected")
check(lhs != mul({(4, 0): F(1)}, Phi(jac(p, q))), "factor-5 mutation not detected")
# chart t=XY, z=1/Y: J_{X,Y}(F,G) = (-z) * J_{t,z}(F,G) for F,G the images written in (t,z)
Ftz, Gtz = to_tz(Phi(p)), to_tz(Phi(q))
check(to_tz(lhs) == mul({(0, 1): F(-1)}, jac(Ftz, Gtz)), "chart bracket is not -z")
check(to_tz(lhs) != mul({(0, 1): F(1)}, jac(Ftz, Gtz)), "chart bracket sign mutation not detected")
# band formula Phi(u^i v^j) = t^l (1+t)^j z^l, l=5i-j, by substitution
for i in range(0, 6):
    for j in range(0, 8):
        l = 5 * i - j
        closed = cl({(l + k, l): F(comb(j, k)) for k in range(j + 1)})
        check(to_tz(Phi({(i, j): F(1)})) == closed, f"band formula failed at {(i, j)}")
# bilinear contribution and multiplier identity
for (i, j, k, s) in [(1, 2, 2, 1), (0, 3, 1, 0), (3, 4, 2, 3), (2, 0, 0, 5), (0, 0, 3, 3), (4, 1, 1, 4), (0, 0, 0, 0)]:
    l, m = 5 * i - j, 5 * k - s
    direct = to_tz(jac(Phi({(i, j): F(1)}), Phi({(k, s): F(1)})))
    fac = l * s - m * j
    check(fac == 5 * (i * s - k * j), "multiplier identity failed")
    pred = cl({(l + m + r, l + m): F(fac * comb(j + s - 1, r)) for r in range(max(j + s, 0))}) if fac else {}
    check(direct == pred, f"bilinear contribution failed at {(i, j, k, s)}")
out["arrow1_chart_and_band_formula"] = "PASS (substitution route)"
# Roy terminal edge: P=X^4 y(1+s), Q=-X(1+3s+9/5 s^2), s=X^17 y^5 has bracket X^4 (own arithmetic)
s = {(17, 5): F(1)}
Pt = mul({(4, 1): F(1)}, add({(0, 0): F(1)}, s))
Qt = mul({(1, 0): F(-1)}, add(add({(0, 0): F(1)}, {e: 3 * c for e, c in s.items()}), {e: F(9, 5) * c for e, c in mul(s, s).items()}))
check(jac(Pt, Qt) == {(4, 0): F(1)}, "terminal edge bracket != X^4")
check(sorted({(a, a - b) for (a, b) in Pt}) == [(4, 3), (21, 15)] and sorted({(a, a - b) for (a, b) in Qt}) == [(1, 1), (18, 13), (35, 25)], "normalization slots")
out["arrow1_terminal_edge_and_normalization_slots"] = "PASS"

# ---------- Arrow 3: explicit inverse on a NONZERO H, both containments ----------
p = rand_poly([(i, j) for i in range(3) for j in range(4)]); q = rand_poly([(i, j) for i in range(3) for j in range(4)])
H = add(jac(p, q), {(0, 0): F(-1, 5)})
check(len(H) >= 5, "H too small to be a meaningful test")
resid = add(jac(Phi(p), Phi(q)), {(4, 0): F(-1)})       # = 5 X^4 Phi(H)
check(resid == mul({(4, 0): F(5)}, Phi(H)), "residual != 5X^4 Phi(H)")
c = to_tz(resid)                                        # c_{e,L}
Ibox = {(I, J) for I in range(0, 6) for J in range(0, 8)}
def inverse(I, J, sign=-1, scale=F(1, 5)):
    L = 5 * I - J + 4
    return scale * sum(((sign) ** (e - L - J)) * comb(e - L, J) * v for (e, LL), v in c.items() if LL == L and e >= L + J)
for (I, J) in Ibox:
    check(inverse(I, J) == H.get((I, J), 0), f"inverse formula failed at {(I, J)}")
# alternative route: divide by 5X^4, untranslate, read coefficient
alt = descend(mul({(-4, 0): F(1, 5)}, resid))
check(alt == H, "division+untranslation route disagrees")
# other containment: each c_{e,L} is 5 * sum_J binom(J, e-L) h_{I,J}
for (e, L), v in c.items():
    acc = F(0)
    for (I, J), h in H.items():
        if 5 * I - J + 4 == L and 0 <= e - L <= J:
            acc += 5 * comb(J, e - L) * h
    check(acc == v, "forward containment failed")
# mutations of the inverse fail closed
def mutated(**kw):
    try:
        for (I, J) in Ibox:
            check(inverse(I, J, **kw) == H.get((I, J), 0), "mismatch")
    except AssertionError:
        return True
    return False
check(mutated(sign=1), "sign-mutated inverse not rejected")
check(mutated(scale=F(1)), "unscaled inverse not rejected")
out["arrow3_inverse_and_both_containments"] = {"H_terms": len(H), "residual_terms": len(c), "mutations_rejected": ["sign", "no 1/5"]}

# ---------- Arrow 3 counts: independent double loops, no band parametrisation ----------
def rank(rows):
    M = [[F(x) for x in r] for r in rows]; rk = 0
    for col in range(len(M[0]) if M else 0):
        piv = next((r for r in range(rk, len(M)) if M[r][col] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        pv = M[rk][col]; M[rk] = [x / pv for x in M[rk]]
        for r in range(len(M)):
            if r != rk and M[r][col] != 0:
                f = M[r][col]; M[r] = [a - f * b for a, b in zip(M[r], M[rk])]
        rk += 1
    return rk
def ceil_div(a, b): return -((-a) // b)
counts = {}
supports = {}
for side, D, U, h in [("P", 75, 15, 3), ("Q", 125, 25, 5)]:
    S = [(i, j) for i in range(D + 1) for j in range(D + 1) if i + j <= D and 5 * i - j <= U]
    supports[side] = S
    bands = sorted({5 * i - j for (i, j) in S})
    check(bands == list(range(-D, U + 1)), "band interval")
    jets = 0; jets_roy = 0
    for l in bands:
        js = sorted(j for (i, j) in S if 5 * i - j == l)
        r1 = max(0, ceil_div(5 * l - h, 12)); r2 = max(0, ceil_div(17 * l - h, 12) - l)
        check(r1 == r2, "two jet-order forms disagree")
        check(r1 < len(js), "jet kills band")
        check(rank([[comb(j, o) for j in js] for o in range(r1)]) == r1 if r1 else True, "jet rank")
        jets += r1
    counts[side] = {"bands": len(bands), "source_coefficients": len(S), "jet_rows": jets, "dimension": len(S) - jets}
check(counts["P"] == {"bands": 91, "source_coefficients": 706, "jet_rows": 53, "dimension": 653}, counts)
check(counts["Q"] == {"bands": 151, "source_coefficients": 1901, "jet_rows": 136, "dimension": 1765}, counts)
out["arrow3_counts"] = counts
# physical row-index bound by direct enumeration
phys = sum(1 for I in range(199) for J in range(199) if I + J <= 198 and 5 * I - J <= 36)
check(phys == 4572, phys)
out["arrow3_physical_row_index_bound"] = phys
# public metadata recount from the formula (active generators / raw scalar rows / incidences)
act = 0; maxdeg = {}
for (i, j) in supports["P"]:
    l = 5 * i - j
    for (k, s) in supports["Q"]:
        if i * s - k * j:
            act += 1; L = l + 5 * k - s
            if j + s - 1 > maxdeg.get(L, -1): maxdeg[L] = j + s - 1
raw_rows = sum(dg + 1 for dg in maxdeg.values())
out["public_metadata_recount"] = {"band_pair_incidences": 91 * 151, "active_generators": act, "raw_scalar_rows": raw_rows,
                                  "layers_with_rows": len(maxdeg), "advertised": [13741, 1327026, 41685]}

# ---------- Endpoint guard is NOT implied by jets + five normalizations (exact rank) ----------
guard = {}
for side, l, D, h, norm_exp, top_i in [("P", 15, 75, 3, 21, 15), ("Q", 25, 125, 5, 35, 25)]:
    js = [5 * i - l for i in range(max(0, ceil_div(l, 5)), (D + l) // 6 + 1)]
    r = max(0, ceil_div(5 * l - h, 12))
    check(norm_exp == l + r, "normalization is not the first post-jet coefficient")
    rows = [[comb(j, o) for j in js] for o in range(r + 1)]      # r jets + the normalization row
    full = rank(rows)
    without_top = rank([row[:-1] for row in rows])               # impose alpha_top = 0 (drop its column)
    check(js[-1] == 5 * top_i - l and (top_i + js[-1]) == D, "top slot is not the degree-D endpoint")
    check(full == r + 1 and without_top == r + 1, "guard implied by linear rows?!")
    guard[side] = {"columns": len(js), "jets": r, "rank_with_norm": full, "rank_top_set_to_zero": without_top,
                   "verdict": "alpha_top=0 is consistent with all linear rows; guard is an explicit addition"}
out["guard_not_implied_by_linear_rows"] = guard
# toy contract mutation: guard naming a zero coefficient makes the ideal contain -1
Pk = {(1, 0): F(1), (0, 2): F(1)}; Qk = {(0, 1): F(1, 5)}
check(jac(Pk, Qk) == {(0, 0): F(1, 5)}, "toy Keller pair")
g_ok = Pk.get((1, 0), 0) * Qk.get((0, 1), 0)      # Z*g_ok-1=0 solvable iff g_ok != 0
g_bad = Pk.get((0, 1), 0) * Qk.get((0, 1), 0)     # names a zero slot
check(g_ok != 0 and g_bad == 0, "toy guard mutation")
out["toy_guard_mutation"] = "guard on a zero slot yields the unit -1: rejected (fail closed)"

out["elapsed_s"] = round(time.time() - T0, 2)
out["status"] = "PASS"
print(json.dumps(out, indent=1, sort_keys=True))
