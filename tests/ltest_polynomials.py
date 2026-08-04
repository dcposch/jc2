#!/usr/bin/env python3
"""Falsification test for Lemma L:polynomials, arXiv:2410.06959 v5 (DC5.tex:1721-1731).

Claim under test: let g in C[x] have >=2 distinct roots, deg g = l; let A,d,z be
positive integers with z=(A-1)d (so A>=2 since z>=1). If the ODE
    c * g^A = H'*g - ((z+1)/d) * H * g'      (c in C*)
has a polynomial solution H, then l/d is an integer > 1, and deg H = l*(z+1)/d.

Test: exact linear algebra over Q. T(H) = H'g - lam*H*g' with lam=(z+1)/d is
Q-linear; solvability of T(H)=g^A over C equals solvability over Q (rank is
field-independent), and c!=0 can be scaled to 1. Degree bound completeness: if
deg H = h != lam*l, the top coefficient of T(H) is (h-lam*l)*lc(H)*lc(g) != 0,
so deg T(H) = h+l-1 = A*l forces h=(A-1)*l+1; else h = lam*l (needs d|l). Hence
solving with deg H <= Dmax = max((A-1)*l+1, floor(lam*l)) + 2 captures every
polynomial solution.
"""
import random
import sys
from fractions import Fraction as F

# ---------- exact univariate polynomial helpers (coeff list, index=degree) ----------

def pnorm(p):
    while p and p[-1] == 0:
        p.pop()
    return p

def padd(p, q):
    n = max(len(p), len(q))
    return pnorm([(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
                  for i in range(n)])

def pscale(p, c):
    return pnorm([c * a for a in p])

def pmul(p, q):
    if not p or not q:
        return []
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                out[i + j] += a * b
    return pnorm(out)

def ppow(p, n):
    out = [F(1)]
    for _ in range(n):
        out = pmul(out, p)
    return out

def pdiff(p):
    return pnorm([p[i] * i for i in range(1, len(p))])

def pdeg(p):
    return len(p) - 1 if p else None  # None = zero polynomial

def T_apply(H, g, gp, lam):
    return padd(pmul(pdiff(H), g), pscale(pmul(H, gp), -lam))

# ---------- exact linear solve: particular solution + kernel basis ----------

def solve_affine(M, b):
    """Solve M h = b over Q. M: list of rows. Returns (particular|None, kernel_basis)."""
    nr, nc = len(M), len(M[0]) if M else 0
    aug = [row[:] + [b[i]] for i, row in enumerate(M)]
    piv_cols = []
    r = 0
    for c in range(nc):
        pr = next((i for i in range(r, nr) if aug[i][c] != 0), None)
        if pr is None:
            continue
        aug[r], aug[pr] = aug[pr], aug[r]
        inv = F(1) / aug[r][c]
        aug[r] = [v * inv for v in aug[r]]
        for i in range(nr):
            if i != r and aug[i][c] != 0:
                f = aug[i][c]
                aug[i] = [vi - f * vr for vi, vr in zip(aug[i], aug[r])]
        piv_cols.append(c)
        r += 1
        if r == nr:
            break
    # inconsistency check
    for i in range(r, nr):
        if aug[i][nc] != 0:
            return None, []
    part = [F(0)] * nc
    for i, c in enumerate(piv_cols):
        part[c] = aug[i][nc]
    free = [c for c in range(nc) if c not in piv_cols]
    kernel = []
    for fc in free:
        v = [F(0)] * nc
        v[fc] = F(1)
        for i, c in enumerate(piv_cols):
            v[c] = -aug[i][fc]
        kernel.append(v)
    return part, kernel

def achievable_degrees(part, kernel):
    """Degrees of elements of part + span(kernel). Kernel echelonized by top index."""
    part = list(part)
    kern = [list(k) for k in kernel]
    # echelonize kernel by distinct leading (highest) nonzero index
    ech = []
    for v in kern:
        v = pnorm(list(v))
        for e in ech:
            if v and pdeg(v) == pdeg(e):
                v = padd(v, pscale(e, -v[pdeg(v)] / e[pdeg(e)]))
        if v:
            ech.append(pscale(v, F(1) / v[-1]))
        ech.sort(key=lambda e: -pdeg(e))
    # reduce particular against kernel leading positions -> minimal degree rep
    part = pnorm(part)
    for e in ech:
        if part and pdeg(part) is not None and len(part) > pdeg(e) and part[pdeg(e)] != 0:
            part = padd(part, pscale(e, -part[pdeg(e)]))
    dmin = pdeg(part)
    degs = {dmin} | {pdeg(e) for e in ech if dmin is None or pdeg(e) > dmin}
    return degs, part, ech

# ---------- instance construction (hypothesis enforcement) ----------

def rand_fraction(rng, nonzero=False):
    while True:
        v = F(rng.randint(-9, 9), rng.randint(1, 5))
        if not nonzero or v != 0:
            return v

def build_g(rng, l, kdist):
    """g = c * prod (x - r_i)^{m_i}: kdist >= 2 DISTINCT roots, mults sum to l."""
    assert 2 <= kdist <= l
    roots = set()
    while len(roots) < kdist:
        roots.add(rand_fraction(rng))
    roots = sorted(roots)
    # random composition of l into kdist positive parts
    cuts = sorted(rng.sample(range(1, l), kdist - 1))
    mults = [b - a for a, b in zip([0] + cuts, cuts + [l])]
    assert all(m >= 1 for m in mults) and sum(mults) == l
    c = rand_fraction(rng, nonzero=True)
    g = [c]
    for r, m in zip(roots, mults):
        g = pmul(g, ppow([-r, F(1)], m))
    assert pdeg(g) == l and len(set(roots)) >= 2  # hypotheses: degree, >=2 distinct roots
    return g, roots, mults, c

def run_instance(g, l, A, d):
    assert A >= 2 and d >= 1                      # A,d in N and z=(A-1)d in N (z>=1)
    z = (A - 1) * d
    assert z >= 1
    lam = F(z + 1, d)
    laml = lam * l
    Dmax = max((A - 1) * l + 1, laml.numerator // laml.denominator) + 2
    rhs_poly = ppow(g, A)
    gp = pdiff(g)
    nrows = Dmax + l  # coefficient degrees 0 .. Dmax+l-1  (covers deg T(H) and A*l)
    assert A * l <= nrows - 1
    cols = []
    for j in range(Dmax + 1):
        Tx = T_apply([F(0)] * j + [F(1)], g, gp, lam)
        cols.append([Tx[i] if i < len(Tx) else F(0) for i in range(nrows)])
    M = [[cols[j][i] for j in range(Dmax + 1)] for i in range(nrows)]
    b = [rhs_poly[i] if i < len(rhs_poly) else F(0) for i in range(nrows)]
    part, kernel = solve_affine(M, b)
    if part is None:
        return {"solvable": False}
    degs, hmin, ech = achievable_degrees(part, kernel)
    # independent verification by direct polynomial arithmetic
    assert T_apply(hmin, g, gp, lam) == rhs_poly, "solver bug: solution fails substitution"
    return {"solvable": True, "degrees": degs, "kerdim": len(ech),
            "Hmin": hmin, "laml": laml}

# ---------- regimes ----------

def classify_expected(l, d):
    ratio_int = (l % d == 0)
    return ratio_int and (l // d) > 1   # True iff necessary condition holds

def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 72108
    print(f"seed={seed}")
    rng = random.Random(seed)
    R1 = [(l, l) for l in (2, 3, 4, 5, 6)]                                   # l = d
    R2 = [(3,2),(5,2),(7,2),(5,3),(4,3),(7,3),(5,4),(7,4),(6,4),(7,5),(8,3),(8,5)]  # l>d, d∤l
    R3 = [(2,3),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6),(4,5),(4,6),(4,7),(5,6),(5,7)]  # l<d
    R4 = [(4,2),(6,2),(8,2),(6,3),(9,3),(8,4),(2,1),(3,1),(4,1),(5,1),(6,1)]        # d|l, l/d>=2
    plan = [("R1 l=d", R1, 80), ("R2 l>d,d∤l", R2, 80), ("R3 l<d", R3, 80),
            ("R4 d|l,l/d>=2", R4, 80)]
    counts = {}
    failures = []
    r4_vacuous = r4_solvable = 0
    r4_examples = []
    for name, pairs, n in plan:
        p = f = 0
        for i in range(n):
            l, d = pairs[i % len(pairs)]
            A = rng.choice([2, 3] if l >= 8 else [2, 3, 4])  # cap system size for l>=8
            kdist = rng.randint(2, min(l, 6))
            g, roots, mults, c = build_g(rng, l, kdist)
            res = run_instance(g, l, A, d)
            nec = classify_expected(l, d)
            if not nec:  # regimes R1-R3: lemma says UNSOLVABLE
                ok = not res["solvable"]
            else:        # regime R4: if solvable, every solution degree must equal lam*l
                if res["solvable"]:
                    r4_solvable += 1
                    ok = (res["degrees"] == {int(res["laml"])})
                    r4_examples.append((l, d, A, mults, [str(r) for r in roots],
                                        sorted(res["degrees"]), res["kerdim"]))
                else:
                    r4_vacuous += 1
                    ok = True
            if ok:
                p += 1
            else:
                f += 1
                failures.append(dict(regime=name, l=l, d=d, A=A, roots=roots,
                                     mults=mults, c=c, res={k: v for k, v in res.items()
                                                            if k != "Hmin"},
                                     Hmin=res.get("Hmin")))
        counts[name] = (p, f)
        print(f"{name}: pass={p} fail={f}")
    # controls: one-root g (hypothesis deliberately violated) -> known answers
    ctrl_p = ctrl_f = 0
    for i in range(24):
        l = rng.randint(2, 6)
        d = rng.choice([x for x in range(1, 8)])
        A = rng.choice([2, 3])
        alpha = rand_fraction(rng)
        c = rand_fraction(rng, nonzero=True)
        g = pscale(ppow([-alpha, F(1)], l), c)
        res = run_instance(g, l, A, d)
        if l == d:
            ok = not res["solvable"]
        else:
            # exact prediction: T diagonal in basis (x-a)^j; base solution degree
            # (A-1)l+1. Kernel of T = span((x-a)^{lam*l}) iff lam*l in Z, i.e. d|l,
            # adding achievable degree lam*l = (A-1)l + l//d.
            want = {(A - 1) * l + 1}
            kd = 0
            if l % d == 0:
                want.add((A - 1) * l + l // d)
                kd = 1
            ok = res["solvable"] and res["degrees"] == want and res["kerdim"] == kd
        ctrl_p, ctrl_f = ctrl_p + ok, ctrl_f + (not ok)
    print(f"CONTROL one-root (solver validation): pass={ctrl_p} fail={ctrl_f}")
    print(f"R4 detail: solvable={r4_solvable} vacuous(unsolvable)={r4_vacuous}")
    for ex in r4_examples:
        print("  R4 solvable (l,d,A,mults,roots,degs,kerdim):", ex)
    total_p = sum(p for p, _ in counts.values())
    total_f = sum(f for _, f in counts.values())
    print(f"TOTAL lemma instances: {total_p + total_f}  pass={total_p} fail={total_f}")
    if failures:
        print("\n=== FAILURES (REFUTATION CANDIDATES) ===")
        for x in failures[:10]:
            print(x)
        sys.exit(1)
    if ctrl_f:
        print("CONTROL FAILURE: solver invalid, results unreliable")
        sys.exit(2)

if __name__ == "__main__":
    main()
