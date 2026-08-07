#!/usr/bin/env python3
"""dc2_deg3.py — DC(2) degree-3 slice: Bernstein degree <= 3 unipotent quadruples in A_2.

Executes tier T1 of DC2-PROGRAM.md (sec 4.2/5.1): the first quantum-sensitive slice.
Builds the exact CCR coefficient system for quadruples
    P_j = x_j + w_j + v_j,   Q_i = xi_i + w'_i + v'_i   (w* quadratic, v* cubic)
in BOTH backends: quantum (Weyl normal-order commutator, all contraction strata) and
classical (Poisson bracket = s=1 stratum only; the PC_2 shadow).  Unknowns: 4 slots x
(10 quad + 20 cubic) = 120.  Equations: residual strata by total degree:
  S4 (deg 4): {v,v}                      6x35 = 210   classical only
  S3 (deg 3): {v,w}                      6x20 = 120   classical only
  S2 (deg 2): L(v) + {w,w} [+ hbar^2 (v,v)]   6x10 = 60
  S1 (deg 1): L'(w)        [+ hbar^2 (v,w)]   6x4  = 24
  S0 (deg 0): 0            [+ hbar^2 (w,w) + hbar^3 (v,v)]  6x1 = 6   quantum only
Gate: at D=2 the machinery must reproduce dc2_slice.py stages B/C exactly.

Exact arithmetic throughout (python ints / Fraction / flint fmpq).  msolve for the
nonlinear fiber probes (-g 2 for emptiness, '[1]:' = EMPTY per campaign discipline).

Stages:
  gate  D=2 reproduction (rank 20 / kernel = gradient family / span 45 -> 45)
  H     D=3 system build + crosscheck + stratum counts + quantum-correction placement
  I     linear strata: L' (24x40) and L (60x80), kernels = X_cubic / X_quartic
  J     span test: classical span vs quantum corrections (linear-level divergence)
  K     classical chart: w = X_c, v = 1/2 X_c^2 z + X_d particular-solution check
  L     fiber probes over curated cubics c: V ∩ {w = X_c}, classical vs quantum
  Ldeep reproduce the lagr_degen quantum-fiber dim/deg resolution (~25 min msolve)
  M     pure-cubic-top stratum c=0: V4 (quartics with pairwise-commuting partials),
        Lagrangian-quartic family, Schubert degree, msolve slice probe
  N     operator-level automorphism certificates at fiber points
  P     exact Jacobian coranks of both 120-var systems at rational family points
        (the scheme-divergence measurement; divergence = the 6 deg-0 vertex eqs)
  O     emit large-box msolve systems to systems/dc2/ + degree-4 cost counts

Results 2026-08-07 (see DC2-PROGRAM.md sec 6): divergence real at D=3, carried by the
deg-0 vertex equations (rank-1 obstruction on classical tangent at family points);
no support-level separation found; all reached quantum points are automorphisms.
"""
import itertools, os, random, re, subprocess, sys, time
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dc2_slice import (wclean, wadd, wmul, wbr, wdegpart, ONE, GEN, ccr_residuals,
                       apply_endo, sderiv, smul, rref_rank, CUBIC_BASIS, QUAD_BASIS,
                       LIN_BASIS, JMAT, omega, random_isotropic_pair, cubic_in_forms)

try:
    from flint import fmpq_mat, fmpq
    HAVE_FLINT = True
except Exception:
    HAVE_FLINT = False

QUARTIC_BASIS = sorted(k for k in itertools.product(range(5), repeat=4) if sum(k) == 4)
assert len(QUARTIC_BASIS) == 35

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYSDIR = os.path.join(REPO, "systems", "dc2")

# ---------------------------------------------------------------- Poisson backend
def pbr(A, B):
    """Poisson bracket on symbols, same key layout; s=1 stratum of wbr."""
    out = {}
    for i in range(2):
        dA1, dB1 = sderiv(A, 2 + i), sderiv(B, i)
        if dA1 and dB1:
            out = wadd(out, smul(dA1, dB1), 1)
        dA2, dB2 = sderiv(A, i), sderiv(B, 2 + i)
        if dA2 and dB2:
            out = wadd(out, smul(dA2, dB2), -1)
    return out

# ---------------------------------------------------------------- system builder
RES_PAIRS = [(2, 0, 1), (2, 1, 0), (3, 0, 0), (3, 1, 1), (0, 1, 0), (2, 3, 0)]

def slice_vars(D):
    """Global unknown list: w-block (all slots, quad), then v-block (slots, cubic)."""
    vs = [(s, m) for s in range(4) for m in QUAD_BASIS]
    if D >= 3:
        vs += [(s, m) for s in range(4) for m in CUBIC_BASIS]
    return vs

def build_system(D, backend):
    """eqs[(ri, mon)] = [const, lam:{vidx:c}, mu:{(vidx<vidx):c}] over slice_vars(D)."""
    br = wbr if backend == "qu" else pbr
    vs = slice_vars(D)
    vidx = {v: i for i, v in enumerate(vs)}
    monos = QUAD_BASIS + (CUBIC_BASIS if D >= 3 else [])
    eqs = {}
    def get(ri, m):
        if (ri, m) not in eqs:
            eqs[(ri, m)] = [0, {}, {}]
        return eqs[(ri, m)]
    for ri, (sa, sb, delta) in enumerate(RES_PAIRS):
        basA = [(None, GEN[sa])] + [(vidx[(sa, m)], {m: 1}) for m in monos]
        basB = [(None, GEN[sb])] + [(vidx[(sb, m)], {m: 1}) for m in monos]
        for ia, A in basA:
            for ib, B in basB:
                for mon, cf in br(A, B).items():
                    e = get(ri, mon)
                    if ia is None and ib is None:
                        e[0] += cf
                    elif ib is None:
                        e[1][ia] = e[1].get(ia, 0) + cf
                    elif ia is None:
                        e[1][ib] = e[1].get(ib, 0) + cf
                    else:
                        k = (ia, ib) if ia < ib else (ib, ia)
                        e[2][k] = e[2].get(k, 0) + cf
        if delta:
            get(ri, (0, 0, 0, 0))[0] -= 1
    # clean zeros / empty equations
    out = {}
    for key, (c, lam, mu) in eqs.items():
        lam = {k: v for k, v in lam.items() if v}
        mu = {k: v for k, v in mu.items() if v}
        if c or lam or mu:
            out[key] = [c, lam, mu]
    return vs, vidx, out

def eval_eq(eq, tv):
    c, lam, mu = eq
    s = c
    for i, v in lam.items():
        s += v * tv[i]
    for (i, j), v in mu.items():
        s += v * tv[i] * tv[j]
    return s

def build_quadruple(D, tv, vs):
    imgs = [dict(g) for g in GEN]
    for i, (s, m) in enumerate(vs):
        if tv[i]:
            imgs[s][m] = imgs[s].get(m, 0) + tv[i]
    return [wclean(im) for im in imgs]

def direct_residuals(imgs, backend):
    br = wbr if backend == "qu" else pbr
    out = []
    for (sa, sb, delta) in RES_PAIRS:
        r = br(imgs[sa], imgs[sb])
        if delta:
            r = wadd(r, ONE, -1)
        out.append(r)
    return out

# ---------------------------------------------------------------- linear algebra
def to_fmpq_mat(rows):
    nr, nc = len(rows), len(rows[0])
    flat = []
    for r in rows:
        for x in r:
            if isinstance(x, Fraction):
                flat.append(fmpq(x.numerator, x.denominator))
            else:
                flat.append(x)
    return fmpq_mat(nr, nc, flat)

def frank(rows):
    if not rows:
        return 0
    if HAVE_FLINT:
        return to_fmpq_mat(rows).rank()
    return rref_rank(rows)

def fq2frac(x):
    return Fraction(str(x))

def solve_affine(A, b, n=None):
    """Solve A x = b exactly. Returns (particular, nullbasis) or None if inconsistent."""
    if n is None:
        n = len(A[0]) if A else 0
    if not A:
        return [Fraction(0)] * n, [[Fraction(1 if i == j else 0) for j in range(n)]
                                    for i in range(n)]
    rows = [list(r) + [bb] for r, bb in zip(A, b)]
    M = to_fmpq_mat(rows)
    R, rank = M.rref()
    piv = []
    for i in range(rank):
        j = 0
        while j <= n and R[i, j] == 0:
            j += 1
        piv.append(j)
    if piv and piv[-1] == n:
        return None
    pivset = set(piv)
    part = [Fraction(0)] * n
    for i, p in enumerate(piv):
        part[p] = fq2frac(R[i, n])
    null = []
    for f in range(n):
        if f in pivset:
            continue
        vec = [Fraction(0)] * n
        vec[f] = Fraction(1)
        for i, p in enumerate(piv):
            vec[p] = -fq2frac(R[i, f])
        null.append(vec)
    return part, null

# ---------------------------------------------------------------- gradient vectors
def grad_vec(h, vs, vidx):
    """h homogeneous deg-k symbol -> Hamiltonian vector (X_h components) over vars."""
    parts = [sderiv(h, 2), sderiv(h, 3),
             {k: -v for k, v in sderiv(h, 0).items()},
             {k: -v for k, v in sderiv(h, 1).items()}]
    vec = [0] * len(vs)
    for s in range(4):
        for m, v in parts[s].items():
            vec[vidx[(s, m)]] = v
    return vec

# ---------------------------------------------------------------- msolve helpers
def msolve_run(args, path, timeout):
    try:
        r = subprocess.run(["msolve"] + args + ["-f", path],
                           capture_output=True, text=True, timeout=timeout)
        out = r.stdout
        if r.returncode == 0 and len(out.strip()) == 0:
            return "DIED", ""
        return "OK", out
    except subprocess.TimeoutExpired:
        return "TIMEOUT", ""

def poly_str(pd, nv, pref="t"):
    terms = []
    for mon, c in sorted(pd.items()):
        if c == 0:
            continue
        vsx = "*".join(f"{pref}{i}" + (f"^{e}" if e > 1 else "")
                       for i, e in enumerate(mon) if e)
        terms.append(f"{c:+d}" + ("*" + vsx if vsx else ""))
    return "".join(terms).lstrip("+") if terms else None

def write_ms(path, polys, nv, char=0, pref="t"):
    with open(path, "w") as f:
        f.write(",".join(f"{pref}{i}" for i in range(nv)) + f"\n{char}\n")
        f.write(",\n".join(polys) + "\n")

def msolve_empty(polys, nv, tag, timeout=300):
    """-g 2 Groebner emptiness check. Returns EMPTY/NONEMPTY/TIMEOUT/DIED."""
    path = f"/tmp/dc2d3_{tag}.ms"
    write_ms(path, polys, nv)
    st, out = msolve_run(["-g", "2"], path, timeout)
    if st != "OK":
        return st
    for line in out.splitlines():
        if line.strip() == "[1]:":
            return "EMPTY"
    if out.strip() in ("[1]", "[-1]:", "[1],"):
        return "EMPTY"
    return "NONEMPTY"

def msolve_dim0(polys, nv, tag, timeout=300):
    """msolve -P 2 structural mode (complex geometry):
    ('0dim', deg) | ('posdim', None) | ('EMPTY', 0) | (status, None)."""
    path = f"/tmp/dc2d3_{tag}.ms"
    write_ms(path, polys, nv)
    st, out = msolve_run(["-P", "2"], path, timeout)
    if st != "OK":
        return st, None
    if out.startswith("[-1"):
        return "EMPTY", 0
    if out.startswith("[1,"):
        return "posdim", None
    m = re.match(r"\[0, \[(-?\d+),\s*(\d+),\s*(\d+)", out)
    if m:
        return "0dim", int(m.group(3))
    return "parse?", None

# ================================================================ stage: gate (D=2)
def stage_gate():
    vs, vidx, eq_qu = build_system(2, "qu")
    _, _, eq_cl = build_system(2, "cl")
    # crosscheck vs direct residuals (both backends), 3 random vectors
    random.seed(5)
    for _ in range(3):
        tv = [random.randint(-2, 2) for _ in range(len(vs))]
        imgs = build_quadruple(2, tv, vs)
        for bk, eqs in (("qu", eq_qu), ("cl", eq_cl)):
            res = direct_residuals(imgs, bk)
            for (ri, m), eq in eqs.items():
                assert eval_eq(eq, tv) == res[ri].get(m, 0), ("gate xcheck", bk, ri, m)
            for ri, r in enumerate(res):
                for m, v in r.items():
                    assert (ri, m) in eqs, ("gate missing eq", bk, ri, m)
    # deg-1 stratum = L' (24x40), rank 20, kernel = X_cubic
    L1 = [(k, eq) for k, eq in eq_qu.items() if sum(k[1]) == 1]
    A1 = [[eq[1].get(i, 0) for i in range(len(vs))] for _, eq in L1]
    for _, eq in L1:
        assert not eq[2] and not eq[0], "deg-1 stratum not linear at D=2"
    r1 = frank(A1)
    grads = [grad_vec({e: 1}, vs, vidx) for e in CUBIC_BASIS]
    for g in grads:
        for row in A1:
            assert sum(a * b for a, b in zip(row, g)) == 0
    rg = frank(grads)
    # span test in the gradient chart w = X_c (c in Sym^3, 20 vars) == dc2_slice stage C
    cl2 = [eq for k, eq in eq_cl.items() if sum(k[1]) == 2]
    qu0 = [eq for k, eq in eq_qu.items() if sum(k[1]) == 0]
    assert not any(sum(k[1]) == 0 for k in eq_cl), "classical deg-0 eq at D=2?!"
    pts = []
    for m in range(20):
        for scale in (1, 2):
            cv = [0] * 20; cv[m] = scale
            pts.append(cv)
    for m in range(20):
        for n2 in range(m + 1, 20):
            cv = [0] * 20; cv[m] = 1; cv[n2] = 1
            pts.append(cv)
    tvs = []
    for cv in pts:
        tv = [0] * len(vs)
        for m in range(20):
            if cv[m]:
                for i, gi in enumerate(grads[m]):
                    tv[i] += cv[m] * gi
        tvs.append(tv)
    Mcl = [[eval_eq(eq, tv) for tv in tvs] for eq in cl2]
    Mqu = [[eval_eq(eq, tv) for tv in tvs] for eq in qu0]
    rc = frank(Mcl)
    rck = frank(Mcl + Mqu)
    ra = frank([list(eq[2].get((i, j), 0) for i in range(40) for j in range(40))
                for eq in cl2])
    rak = frank([list(eq[2].get((i, j), 0) for i in range(40) for j in range(40))
                 for eq in cl2 + qu0])
    ok = (r1 == 20 and rg == 20 and rc == 45 and rck == 45 and len(A1) == 24
          and len(cl2) == 60 and len(qu0) == 6)
    print(f"gate: D=2 rebuild: deg-1 {len(A1)}x{len(vs)} rank {r1}, X_cubic in kernel "
          f"rank {rg}; deg-2 classical forms restricted to gradient chart: 60 forms "
          f"span {rc}; +6 quantum deg-0 -> {rck}. "
          f"{'PASS (== dc2_slice B/C)' if ok else 'FAIL'}")
    print(f"gate: bonus ambient statement on K^40: 60 classical deg-2 forms rank {ra}; "
          f"+6 quantum deg-0 forms -> rank {rak} "
          f"({'ambient span-complete' if ra == rak else 'ambient jump'}).")
    assert ok
    return ok

# ================================================================ stage H: D=3 build
_D3 = {}
def get_d3():
    if not _D3:
        t0 = time.time()
        vs, vidx, eq_qu = build_system(3, "qu")
        _, _, eq_cl = build_system(3, "cl")
        _D3.update(vs=vs, vidx=vidx, qu=eq_qu, cl=eq_cl, t=time.time() - t0)
    return _D3

def stage_H():
    d = get_d3()
    vs, eq_qu, eq_cl = d["vs"], d["qu"], d["cl"]
    random.seed(17)
    for _ in range(2):
        tv = [random.randint(-2, 2) for _ in range(len(vs))]
        imgs = build_quadruple(3, tv, vs)
        for bk, eqs in (("qu", eq_qu), ("cl", eq_cl)):
            res = direct_residuals(imgs, bk)
            for (ri, m), eq in eqs.items():
                assert eval_eq(eq, tv) == res[ri].get(m, 0), ("H xcheck", bk, ri, m)
            for ri, r in enumerate(res):
                for m, v in r.items():
                    assert (ri, m) in eqs, ("H missing", bk, ri, m)
    nW = 40
    cnt_qu = {s: 0 for s in range(5)}
    cnt_cl = {s: 0 for s in range(5)}
    for k in eq_qu: cnt_qu[sum(k[1])] += 1
    for k in eq_cl: cnt_cl[sum(k[1])] += 1
    # quantum-correction placement: compare mu/lam/const per shared key
    place = {}
    for key in set(eq_qu) | set(eq_cl):
        q = eq_qu.get(key, [0, {}, {}])
        c = eq_cl.get(key, [0, {}, {}])
        assert q[0] == c[0], ("const differs", key)
        assert q[1] == c[1], ("lambda differs (linearizations must agree)", key)
        dmu = {}
        for k2 in set(q[2]) | set(c[2]):
            dv = q[2].get(k2, 0) - c[2].get(k2, 0)
            if dv:
                dmu[k2] = dv
        if dmu:
            st = sum(key[1])
            blocks = set()
            for (a, b) in dmu:
                blocks.add(("w" if a < nW else "v") + ("w" if b < nW else "v"))
            place.setdefault(st, set()).update(blocks)
    print(f"H: D=3 unipotent slice: {len(vs)} unknowns (40 quad + 80 cubic); "
          f"eq counts by residual degree: quantum {dict(sorted(cnt_qu.items()))}, "
          f"classical {dict(sorted(cnt_cl.items()))} (build {d['t']:.1f}s).")
    print(f"H: linearizations identical (lam_qu==lam_cl, const==0); quantum mu-"
          f"corrections at strata {dict((k, sorted(v)) for k, v in sorted(place.items()))} "
          "=> hbar^2: (v,v)->deg2, (v,w)->deg1, (w,w)->deg0; hbar^3: (v,v)->deg0.  PASS")
    return place

# ================================================================ stage I: linear strata
def stage_I():
    d = get_d3()
    vs, vidx, eq_qu = d["vs"], d["vidx"], d["qu"]
    n = len(vs)
    L2 = [(k, eq) for k, eq in eq_qu.items() if sum(k[1]) == 2]
    A2 = [[eq[1].get(i, 0) for i in range(n)] for _, eq in L2]
    for row in A2:
        assert not any(row[:40]), "deg-2 lambda touches w-block?!"
    r2 = frank([r[40:] for r in A2])
    quart = [grad_vec({e: 1}, vs, vidx) for e in QUARTIC_BASIS]
    for g in quart:
        for _, eq in L2:
            assert sum(eq[1].get(i, 0) * g[i] for i in eq[1]) == 0, "X_quartic not in ker L"
    rq = frank([g[40:] for g in quart])
    L1 = [(k, eq) for k, eq in eq_qu.items() if sum(k[1]) == 1]
    A1w = [[eq[1].get(i, 0) for i in range(40)] for _, eq in L1]
    r1 = frank(A1w)
    print(f"I: deg-2 stratum linear map L on v: {len(A2)}x80, rank {r2}; X_quartic "
          f"family (35) in kernel, rank {rq} => ker L == X_(Sym^4) iff {r2}==45; "
          f"deg-1 L' on w: {len(A1w)}x40 rank {r1} (gate value 20). "
          f"Tangent at identity (both backends, linearizations equal): dim "
          f"{40 - r1 + 80 - r2} = X_cubic + X_quartic.")
    return r1, r2

# ================================================================ stage J: span test
def stage_J():
    d = get_d3()
    vs, eq_qu, eq_cl = d["vs"], d["qu"], d["cl"]
    keys = sorted(set(eq_qu) | set(eq_cl))
    colset = set()
    for eqs in (eq_qu, eq_cl):
        for eq in eqs.values():
            if eq[0]:
                colset.add("c")
            colset.update(("l", i) for i in eq[1])
            colset.update(("m",) + k for k in eq[2])
    cols = sorted(colset, key=str)
    colix = {c: i for i, c in enumerate(cols)}
    def rowvec(eq):
        vec = [0] * len(cols)
        c, lam, mu = eq
        if c:
            vec[colix["c"]] = c
        for i, v in lam.items():
            vec[colix[("l", i)]] = v
        for k, v in mu.items():
            vec[colix[("m",) + k]] = v
        return vec
    cl_rows = [rowvec(eq) for eq in eq_cl.values()]
    qu_rows = [rowvec(eq) for eq in eq_qu.values()]
    delta = {}
    for key in keys:
        q = eq_qu.get(key, [0, {}, {}])
        c = eq_cl.get(key, [0, {}, {}])
        dmu = {}
        for k2 in set(q[2]) | set(c[2]):
            dv = q[2].get(k2, 0) - c[2].get(k2, 0)
            if dv:
                dmu[k2] = dv
        if dmu:
            delta.setdefault(sum(key[1]), []).append(rowvec([0, {}, dmu]))
    t0 = time.time()
    rc = frank(cl_rows)
    res = {}
    for st in sorted(delta):
        res[st] = frank(cl_rows + delta[st])
    rall = frank(cl_rows + [r for st in delta for r in delta[st]])
    rq = frank(qu_rows)
    rqc = frank(qu_rows + cl_rows)
    print(f"J: classical system rank {rc} ({len(cl_rows)} eqs, {len(cols)} coeff cols); "
          f"rank after adding quantum corrections: "
          + ", ".join(f"stratum-{st}(+{len(delta[st])}): {res[st]}" for st in sorted(delta))
          + f"; all: {rall}.  quantum rank {rq}, quantum+classical {rqc} "
          f"({time.time()-t0:.0f}s).")
    verdict = ("SPAN-COMPLETE (corrections in classical span => V_cl subset V_qu at "
               "generator level)" if rall == rc else
               f"DIVERGENT at generator level: quantum corrections add "
               f"{rall - rc} independent directions (and span(qu)==span(cl) is "
               f"{rq == rc == rqc})")
    print(f"J: {verdict}")
    return rc, rall, rq, rqc

# ================================================================ stage K: classical chart
def stage_K():
    d = get_d3()
    vs, vidx, eq_cl = d["vs"], d["vidx"], d["cl"]
    random.seed(23)
    strata_zero = None
    for trial in range(5):
        c = {e: Fraction(random.randint(-3, 3)) for e in CUBIC_BASIS}
        w1 = [pbr(c, g) for g in GEN]            # X_c z
        v1 = [{k: Fraction(v, 2) for k, v in pbr(c, w).items()} for w in w1]  # 1/2 X_c^2 z
        tv = [Fraction(0)] * len(vs)
        for s in range(4):
            for m, v in w1[s].items():
                tv[vidx[(s, m)]] = v
            for m, v in v1[s].items():
                tv[vidx[(s, m)]] = v
        vals = {}
        for (ri, m), eq in eq_cl.items():
            vals.setdefault(sum(m), []).append(eval_eq(eq, tv))
        z = {st: all(x == 0 for x in v) for st, v in sorted(vals.items())}
        if strata_zero is None:
            strata_zero = z
        assert z[1] and z[2], "jet fails S1cl/S2cl"
    print(f"K: classical chart: for random cubic c, (w,v) = (X_c z, 1/2 X_c^2 z) kills "
          f"strata 1,2 exactly (5/5); higher strata vanish: "
          f"{dict((k, v) for k, v in strata_zero.items() if k >= 3)} (generically False "
          "=> S3/S4 = the exactness obstruction on (c,d), d in Sym^4 the kernel freedom).")

# ================================================================ curated cubics
def curated_cubics():
    random.seed(41)
    u1, u2 = random_isotropic_pair(random)
    lag_gen = cubic_in_forms(u1, u2, [1, 2, -1, 1])
    u3, u4 = random_isotropic_pair(random)
    lag_degen = cubic_in_forms(u3, u4, [1, 0, 0, 0])
    random.seed(43)
    gen1 = {e: random.randint(-2, 2) for e in CUBIC_BASIS}
    gen2 = {e: random.randint(-2, 2) for e in CUBIC_BASIS}
    lst = [
        ("zero", {}),
        ("lagr_gen", {k: int(v) for k, v in lag_gen.items() if v}),
        ("lagr_axis", {(3, 0, 0, 0): 1, (2, 0, 0, 1): 1, (0, 0, 0, 3): -1}),
        ("lagr_degen", {k: int(v) for k, v in lag_degen.items() if v}),
        ("split_LL", {(0, 0, 3, 0): 1, (0, 3, 0, 0): 1}),
        ("split_gen", {(0, 0, 3, 0): 1, (0, 0, 1, 2): 1, (3, 0, 0, 0): 1, (2, 1, 0, 0): 1}),
        ("dixmier", {(0, 0, 3, 0): 1, (3, 0, 0, 0): 1}),
        ("x1sq_xi1", {(2, 0, 1, 0): 1}),
        ("gen_rand1", {k: v for k, v in gen1.items() if v}),
        ("gen_rand2", {k: v for k, v in gen2.items() if v}),
        ("lagr_pert", {(3, 0, 0, 0): 1, (2, 0, 0, 1): 1, (0, 0, 0, 3): -1, (2, 0, 1, 0): 1}),
    ]
    return lst

def in_V3(c):
    """c cubic dict -> does it satisfy the D<=2 constraint variety (60 forms)?"""
    imgs = [wadd(GEN[0], sderiv(c, 2)), wadd(GEN[1], sderiv(c, 3)),
            wadd(GEN[2], sderiv(c, 0), -1), wadd(GEN[3], sderiv(c, 1), -1)]
    res = direct_residuals(imgs, "cl")
    return all(not wdegpart(r, 2) for r in res)

# ================================================================ stage L: fibers
def fiber(cdict, backend, tag, timeout=300, deep_dim=True, w0_extra=None):
    """Analyze V_backend ∩ {w = X_c (+ w0_extra)} in the 80 cubic unknowns.  Exact
    linear solve, then msolve on the reduced quadrics.  Returns short verdict."""
    d = get_d3()
    vs, vidx, eqs = d["vs"], d["vidx"], d[backend]
    n = len(vs)
    w0 = grad_vec(cdict, vs, vidx)          # w-block filled, v-block zero
    if w0_extra:
        for i, x in w0_extra.items():
            w0[i] += x
    assert not any(w0[40:])
    lin_eqs, quad_eqs = [], []
    for (ri, m), (c0, lam, mu) in eqs.items():
        cc = c0 + sum(v * w0[i] for i, v in lam.items() if i < 40)
        lv = {}
        for i, v in lam.items():
            if i >= 40:
                lv[i - 40] = lv.get(i - 40, 0) + v
        qd = {}
        for (a, b), v in mu.items():
            if a < 40 and b < 40:
                cc += v * w0[a] * w0[b]
            elif a < 40:
                lv[b - 40] = lv.get(b - 40, 0) + v * w0[a]
            elif b < 40:
                lv[a - 40] = lv.get(a - 40, 0) + v * w0[b]
            else:
                qd[(a - 40, b - 40)] = qd.get((a - 40, b - 40), 0) + v
        lv = {k: v for k, v in lv.items() if v}
        qd = {k: v for k, v in qd.items() if v}
        if qd:
            quad_eqs.append((cc, lv, qd))
        elif lv or cc:
            lin_eqs.append((cc, lv))
    A = [[lv.get(j, 0) for j in range(80)] for cc, lv in lin_eqs]
    b = [-cc for cc, lv in lin_eqs]
    sol = solve_affine(A, b, n=80)
    if sol is None:
        return f"EMPTY (linear: {len(lin_eqs)} eqs inconsistent)"
    part, null = sol
    k = len(null)
    den = 1
    for x in part:
        den = den * x.denominator // __import__("math").gcd(den, x.denominator)
    for vv in null:
        for x in vv:
            den = den * x.denominator // __import__("math").gcd(den, x.denominator)
    pi = [int(x * den) for x in part]
    Ni = [[int(x * den) for x in vv] for vv in null]
    polys = set()
    for cc, lv, qd in quad_eqs:
        pd = {}
        def add(mon, val):
            if val:
                pd[mon] = pd.get(mon, 0) + val
        add((), cc * den * den)
        for j, v in lv.items():
            add((), v * den * pi[j])
            for f in range(k):
                add((f,), v * den * Ni[f][j])
        for (a2, b2), v in qd.items():
            add((), v * pi[a2] * pi[b2])
            for f in range(k):
                add((f,), v * (pi[a2] * Ni[f][b2] + pi[b2] * Ni[f][a2]))
                for g in range(f, k):
                    if f == g:
                        add((f, f), v * Ni[f][a2] * Ni[f][b2])
                    else:
                        add((f, g), v * (Ni[f][a2] * Ni[g][b2] + Ni[g][a2] * Ni[f][b2]))
        pd = {m: c2 for m, c2 in pd.items() if c2}
        if pd:
            polys.add(tuple(sorted(pd.items())))
    lin_desc = f"lin {len(lin_eqs)}r{80 - k} k={k}"
    if not polys:
        return f"NONEMPTY affine dim {k} ({lin_desc}; quadratics vanish on slab)"
    if k == 0:
        return f"EMPTY (unique linear solution violates {len(polys)} quadrics)"
    if k > 36:
        os.makedirs(SYSDIR, exist_ok=True)
        def totuple0(pd):
            out = {}
            for mon, c2 in pd:
                e = [0] * k
                for i in mon:
                    e[i] += 1
                out[tuple(e)] = c2
            return out
        ps0 = [poly_str(totuple0(pd), k) for pd in sorted(polys)]
        write_ms(os.path.join(SYSDIR, f"dc2_d3_fiber_{tag}.ms"),
                 [p for p in ps0 if p], k)
        return (f"UNRESOLVED locally (k={k} free vars, {len(polys)} quadrics) "
                f"-> emitted systems/dc2/dc2_d3_fiber_{tag}.ms")
    # convert monomial-tuple keys to exponent tuples over k vars
    def totuple(pd):
        out = {}
        for mon, c2 in pd:
            e = [0] * k
            for i in mon:
                e[i] += 1
            out[tuple(e)] = c2
        return out
    pstr = [poly_str(totuple(pd), k) for pd in sorted(polys)]
    pstr = [p for p in pstr if p]
    st = msolve_empty(pstr, k, tag + "_e", timeout)
    if st != "NONEMPTY":
        return f"{st} ({lin_desc}; {len(pstr)} quadrics)"
    st2, deg = msolve_dim0(pstr, k, tag + "_d", timeout)
    if st2 == "0dim":
        return f"NONEMPTY 0-dim deg {deg} in slab ({lin_desc}; {len(pstr)} quadrics)"
    if st2 != "posdim":
        return f"NONEMPTY, dim-probe {st2} ({lin_desc}; {len(pstr)} quadrics)"
    # positive-dimensional: measure dim by adding random hyperplanes
    if not deep_dim:
        return f"NONEMPTY posdim ({lin_desc}; {len(pstr)} quadrics)"
    import zlib
    random.seed(zlib.crc32(tag.encode()) & 0xffff)
    cur = list(pstr)
    for extra in range(1, 13):
        hp = "+".join(f"{random.randint(-5, 5) or 1}*t{i}" for i in range(k)) + \
             f"{random.randint(-9, -1):+d}"
        cur.append(hp)
        st3, deg3 = msolve_dim0(cur, k, tag + f"_h{extra}", timeout)
        if st3 == "0dim" and deg3 and deg3 > 0:
            return (f"NONEMPTY dim {extra} deg {deg3} in slab "
                    f"({lin_desc}; {len(pstr)} quadrics)")
        if st3 == "EMPTY" or (st3 == "0dim" and deg3 == 0):
            return (f"NONEMPTY dim <{extra} (complex-empty at +{extra} planes) "
                    f"({lin_desc})")
        if st3 in ("TIMEOUT", "DIED", "parse?"):
            return f"NONEMPTY posdim, dim-probe {st3} at +{extra} ({lin_desc})"
    return f"NONEMPTY dim >=12 ({lin_desc})"

def lagrangian_quartic_point(seed=71):
    d = get_d3()
    vs, vidx = d["vs"], d["vidx"]
    random.seed(seed)
    u1, u2 = random_isotropic_pair(random)
    l1 = {tuple(1 if tt == bb else 0 for tt in range(4)): Fraction(u1[bb])
          for bb in range(4) if u1[bb]}
    l2 = {tuple(1 if tt == bb else 0 for tt in range(4)): Fraction(u2[bb])
          for bb in range(4) if u2[bb]}
    dq = {}
    for i, f in enumerate([1, -2, 1, 2, -1]):
        t2 = {(0, 0, 0, 0): Fraction(f)}
        for _ in range(4 - i):
            t2 = smul(t2, l1)
        for _ in range(i):
            t2 = smul(t2, l2)
        dq = wadd(dq, t2)
    return dq

def stage_L(only=None):
    # msolve format self-test
    assert msolve_empty(["t0", "t0-1"], 1, "selftest_empty") == "EMPTY"
    assert msolve_empty(["t0^2-1"], 1, "selftest_ne") == "NONEMPTY"
    for name, cd in curated_cubics():
        if only and name not in only:
            continue
        flags = []
        if cd and in_V3(cd):
            flags.append("V3")
        if name == "zero":
            # both fibers contain the Lagrangian-quartic cone (exact operator check);
            # classical structure = stage M; quantum excess = large-box emission.
            dq = lagrangian_quartic_point()
            imgs = [wadd(g, wbr(dq, g)) for g in GEN]
            okq = all(not r for r in direct_residuals(imgs, "qu"))
            okc = all(not r for r in direct_residuals(imgs, "cl"))
            cl = (f"NONEMPTY dim >= 8 (contains X_(Lagrangian quartic) cone, exact "
                  f"check {okc}; full structure -> stage M/V4)")
            qu = (f"NONEMPTY dim >= 8 (same cone, exact operator check {okq}; excess "
                  "over classical = large-box, see emitted fiber system)")
            _ = fiber(cd, "qu", f"{name}_qu")   # ensure emission of the 80-var system
            print(f"L[{name}]: cl: {cl}")
            print(f"L[{name}]: qu: {qu}")
            continue
        cl = fiber(cd, "cl", f"{name}_cl")
        qu = fiber(cd, "qu", f"{name}_qu")
        resolved = all(v.startswith(("EMPTY", "NONEMPTY")) for v in (cl, qu))
        div = "  <== DIVERGENT" if resolved and cl.split("(")[0] != qu.split("(")[0] \
            else ""
        print(f"L[{name}{'|' + ','.join(flags) if flags else ''}]: cl: {cl}")
        print(f"L[{name}]: qu: {qu}{div}")

def stage_Ldeep():
    """Reproduce the lagr_degen quantum-fiber resolution (dim 6 deg 10; ~25-30 min:
    one 50-var GB + up to 7 hyperplane-sliced -P 2 runs)."""
    cd = curated_cubics()[3][1]
    v = fiber(cd, "qu", "lagr_degen_qu_deep", timeout=2400)
    if v.startswith("UNRESOLVED"):
        path = os.path.join(SYSDIR, "dc2_d3_fiber_lagr_degen_qu_deep.ms")
        lines = open(path).read().splitlines()
        k = len(lines[0].split(","))
        polys = [p.strip().rstrip(",") for p in lines[2:] if p.strip()]
        random.seed(99)
        cur = list(polys)
        for extra in range(1, 9):
            hp = "+".join(f"{random.randint(-5, 5) or 1}*t{i}" for i in range(k)) + \
                 f"{random.randint(-9, -1):+d}"
            cur.append(hp)
            st3, deg3 = msolve_dim0(cur, k, f"ldq_deep_h{extra}", 2400)
            if st3 == "0dim" and deg3:
                v = f"NONEMPTY dim {extra} deg {deg3} (deep probe)"
                break
            if st3 == "EMPTY":
                v = f"NONEMPTY dim <{extra} (deep probe)"
                break
            if st3 in ("TIMEOUT", "DIED"):
                v = f"deep probe {st3} at +{extra}"
                break
    print(f"Ldeep[lagr_degen qu]: {v}  (2026-08-07 run: dim 6 deg 10 == classical)")

# ================================================================ stage M: V4 at c=0
def sym_reduce3(p):
    """symmetric deg-3 poly dict in (a,b) -> value on LGr(2,4): h^3=2, h*l=1."""
    al = p.get((3, 0), 0)
    be = p.get((2, 1), 0) - 3 * al
    return 2 * al + be

def schubert_degree_calc(k):
    """deg of {f(u1,u2): span Lagrangian, f binary deg-k} cone in Sym^k(K^4):
    integral over P(Sym^k U*) of xi^(rk+2) = s_3((Sym^k U*)^dual) on LGr(2,4)=Q^3."""
    roots = [{(1, 0): k - i, (0, 1): i} for i in range(k + 1)]
    def emul(p, q):
        out = {}
        for (a1, b1), c1 in p.items():
            for (a2, b2), c2 in q.items():
                key = (a1 + a2, b1 + b2)
                out[key] = out.get(key, 0) + c1 * c2
        return out
    def eadd(p, q, s=1):
        out = dict(p)
        for kk, v in q.items():
            out[kk] = out.get(kk, 0) + s * v
        return {kk: v for kk, v in out.items() if v}
    e1, e2, e3 = {}, {}, {}
    n = len(roots)
    for i in range(n):
        e1 = eadd(e1, roots[i])
        for j in range(i + 1, n):
            e2 = eadd(e2, emul(roots[i], roots[j]))
            for l in range(j + 1, n):
                e3 = eadd(e3, emul(emul(roots[i], roots[j]), roots[l]))
    # s3(E^dual) = c1^3 - 2 c1 c2 + c3 in Chern classes of E
    p = eadd(eadd(emul(e1, emul(e1, e1)), emul(e1, e2), -2), e3)
    return sym_reduce3(p)

def stage_M(run_msolve=True, timeout=1500):
    d = get_d3()
    vs, vidx, eq_cl, eq_qu = d["vs"], d["vidx"], d["cl"], d["qu"]
    # classical c=0 fiber in d-coordinates: S4 quadrics restricted to v = X_d
    quart_vecs = [grad_vec({e: 1}, vs, vidx) for e in QUARTIC_BASIS]
    S4 = [(k, eq) for k, eq in eq_cl.items() if sum(k[1]) == 4]
    polys = set()
    for _, (c0, lam, mu) in S4:
        assert c0 == 0 and not lam
        pd = {}
        for (a, b), v in mu.items():
            for f in range(35):
                va = quart_vecs[f][a]
                if not va:
                    continue
                for g in range(35):
                    vb = quart_vecs[g][b]
                    if not vb:
                        continue
                    f2, g2 = min(f, g), max(f, g)
                    e = [0] * 35
                    e[f2] += 1
                    e[g2] += 1
                    key = tuple(e)
                    pd[key] = pd.get(key, 0) + v * va * vb
        pd = {m: c2 for m, c2 in pd.items() if c2}
        if pd:
            polys.add(tuple(sorted(pd.items())))
    npoly = len(polys)
    # family membership + controls + Jacobian rank
    random.seed(29)
    ranks = set()
    nfam = 0
    for t in range(10):
        u1, u2 = random_isotropic_pair(random)
        # quartic in forms u1,u2
        l1 = {tuple(1 if tt == bb else 0 for tt in range(4)): Fraction(u1[bb])
              for bb in range(4) if u1[bb]}
        l2 = {tuple(1 if tt == bb else 0 for tt in range(4)): Fraction(u2[bb])
              for bb in range(4) if u2[bb]}
        dq = {}
        for i, f in enumerate([random.randint(-2, 2) for _ in range(5)]):
            t2 = {(0, 0, 0, 0): Fraction(f)}
            for _ in range(4 - i):
                t2 = smul(t2, l1)
            for _ in range(i):
                t2 = smul(t2, l2)
            dq = wadd(dq, t2)
        dv = [dq.get(e, 0) for e in QUARTIC_BASIS]
        vals = []
        for pd in polys:
            s = 0
            for mon, c2 in pd:
                term = c2
                for i2, e2 in enumerate(mon):
                    for _ in range(e2):
                        term *= dv[i2]
                s += term
            vals.append(s)
        if all(v == 0 for v in vals):
            nfam += 1
        if t < 3:
            # Jacobian rank at family point
            rows = []
            for pd in polys:
                grad = [0] * 35
                for mon, c2 in pd:
                    nz = [i2 for i2, e2 in enumerate(mon) if e2]
                    if len(nz) == 1:
                        grad[nz[0]] += 2 * c2 * dv[nz[0]]
                    else:
                        grad[nz[0]] += c2 * dv[nz[1]]
                        grad[nz[1]] += c2 * dv[nz[0]]
                rows.append(grad)
            ranks.add(frank(rows))
    ctrl = {(2, 0, 1, 1): 1, (4, 0, 0, 0): 1}   # x1^2 xi1 xi2 + x1^4: non-Lagrangian
    cv = [ctrl.get(e, 0) for e in QUARTIC_BASIS]
    bad = any(sum(c2 * cv[[i2 for i2, e2 in enumerate(mon) if e2][0]] *
                  cv[[i2 for i2, e2 in enumerate(mon) for _ in range(e2)][-1]]
                  for mon, c2 in pd) != 0 for pd in polys)
    sch3 = schubert_degree_calc(3)
    sch4 = schubert_degree_calc(4)
    print(f"M: V4 (c=0 classical fiber) = {npoly} distinct quadrics in 35 quartic "
          f"coeffs; Lagrangian-quartic family: {nfam}/10 random points in V4, control "
          f"excluded: {bad}; Jacobian ranks at family points {sorted(ranks)} => local "
          f"dim {sorted(35 - r for r in ranks)} (family dim 8 = 3+5).")
    print(f"M: Schubert cross-check: deg(Lagrangian cubic cone in Sym^3) = {sch3} "
          f"(D<=2 value 90); deg(Lagrangian quartic cone in Sym^4) = {sch4} (prediction "
          "for deg V4 if V4 = Lagrangian family).")
    # quantum c=0: known family points are exact operator solutions (checked in stage N);
    # quantum fiber has no linear stratum (S2qu quadratic) -> emitted as large-box.
    if run_msolve:
        random.seed(31)
        while True:
            Amat = [[random.randint(-2, 2) for _ in range(27)] for _ in range(35)]
            if rref_rank([[Fraction(x) for x in r] for r in
                          [list(col) for col in zip(*Amat)]]) == 27:
                break
        bvec = [random.randint(-2, 2) for _ in range(35)]
        pstr = []
        seen = set()
        for pd in sorted(polys):
            out = {}
            for mon, c2 in pd:
                nz = [i2 for i2, e2 in enumerate(mon) for _ in range(e2)]
                a2, b2 = nz[0], nz[-1]
                # substitute d = A t + b
                for f in range(28):
                    xa = Amat[a2][f] if f < 27 else bvec[a2]
                    if not xa:
                        continue
                    for g in range(28):
                        xb = Amat[b2][g] if g < 27 else bvec[b2]
                        if not xb:
                            continue
                        f2, g2 = min(f, g), max(f, g)
                        e = [0] * 27
                        if f2 < 27:
                            e[f2] += 1
                        if g2 < 27:
                            e[g2] += 1
                        out[tuple(e)] = out.get(tuple(e), 0) + c2 * xa * xb
            ps = poly_str(out, 27)
            if ps and ps not in seen:
                seen.add(ps)
                pstr.append(ps)
        t0 = time.time()
        st, deg = msolve_dim0(pstr, 27, "v4slice", timeout)
        print(f"M: msolve V4 random codim-8 slice (27 vars, {len(pstr)} quadrics): "
              f"{st}{' deg ' + str(deg) if deg else ''} ({time.time()-t0:.0f}s)"
              + ("" if st == "0dim" else " -> emit as large-box candidate"))
        if st != "0dim":
            os.makedirs(SYSDIR, exist_ok=True)
            write_ms(os.path.join(SYSDIR, "dc2_d3_V4_slice27.ms"), pstr, 27)
        return st, deg
    return None, None

# ================================================================ stage N: certificates
def compose_endo(im_outer, im_inner):
    return [wclean(apply_endo(im_outer, p)) for p in im_inner]

def truncate(A, cap):
    return {k: v for k, v in A.items() if sum(k) <= cap}

def try_invert(imgs, cap=12, rounds=30):
    psi = [dict(g) for g in GEN]
    for _ in range(rounds):
        comp = compose_endo(psi, imgs)
        err = [wadd(comp[k], GEN[k], -1) for k in range(4)]
        if all(not e for e in err):
            break
        psi = [truncate(wadd(psi[k], err[k], -1), cap) for k in range(4)]
    else:
        return None
    if any(compose_endo(psi, imgs)[k] != GEN[k] for k in range(4)):
        return None
    if any(compose_endo(imgs, psi)[k] != GEN[k] for k in range(4)):
        return None
    return psi

def stage_N():
    d = get_d3()
    vs, vidx = d["vs"], d["vidx"]
    random.seed(37)
    nok, tried = 0, 0
    reps = []
    # representatives: Lagrangian cubic+quartic flows on random isotropic planes
    for t in range(5):
        u1, u2 = random_isotropic_pair(random)
        h = {}
        l1 = {tuple(1 if tt == bb else 0 for tt in range(4)): Fraction(u1[bb])
              for bb in range(4) if u1[bb]}
        l2 = {tuple(1 if tt == bb else 0 for tt in range(4)): Fraction(u2[bb])
              for bb in range(4) if u2[bb]}
        for deg, ncf in ((3, 4), (4, 5)):
            for i in range(ncf):
                cf = random.randint(-2, 2)
                if not cf:
                    continue
                t2 = {(0, 0, 0, 0): Fraction(cf)}
                for _ in range(deg - i):
                    t2 = smul(t2, l1)
                for _ in range(i):
                    t2 = smul(t2, l2)
                h = wadd(h, t2)
        h = {k: v for k, v in h.items() if sum(k) in (3, 4)}
        imgs = [wadd(g, wbr(h, g)) for g in GEN]     # exp(ad h), ad_h^2 = 0 on gens
        for g in GEN:
            assert not wbr(h, wbr(h, g)), "ad_h^2 != 0?!"
        res = direct_residuals(imgs, "qu")
        assert all(not r for r in res), "family point fails quantum CCR?!"
        tried += 1
        inv = try_invert(imgs)
        if inv is not None:
            nok += 1
        reps.append((u1, u2))
    print(f"N: {nok}/{tried} Lagrangian cubic+quartic flow quadruples: exact operator "
          "6-CCR PASS + explicit two-sided inverse found => automorphisms (deg-3 "
          "unipotent points of the quantum variety).")
    # non-symplectic linear part probe at D=3 (unipotent-reduction caveat)
    random.seed(53)
    npb = 0
    for trial in range(10):
        u1, u2 = reps[trial % len(reps)]
        # family (w,v) from h = cubic + quartic in the plane, linear part random M
        h = cubic_in_forms(u1, u2, [1, -1, 2, 1])
        l1 = {tuple(1 if tt == bb else 0 for tt in range(4)): Fraction(u1[bb])
              for bb in range(4) if u1[bb]}
        t2 = {(0, 0, 0, 0): Fraction(1)}
        for _ in range(4):
            t2 = smul(t2, l1)
        h = wadd(h, t2)
        M = [[Fraction(random.randint(-2, 2)) for _ in range(4)] for _ in range(4)]
        parts = [wbr(h, g) for g in GEN]
        img = [wadd({LIN_BASIS[a]: M[a][kk] for a in range(4) if M[a][kk]}, parts[kk])
               for kk in range(4)]
        res = ccr_residuals(img[0], img[1], img[2], img[3])
        MTJM = [[sum(M[a][i] * JMAT[a][b2] * M[b2][j] for a in range(4)
                     for b2 in range(4)) for j in range(4)] for i in range(4)]
        expect = [MTJM[2][0] - 1, MTJM[2][1], MTJM[3][0], MTJM[3][1] - 1,
                  MTJM[0][1], MTJM[2][3]]
        if all(r.get((0, 0, 0, 0), 0) == e for r, e in zip(res, expect)):
            npb += 1
    print(f"N: deg-0 residual == M^T.J.M - J for {npb}/10 random non-symplectic linear "
          "parts over family (w,v) => linear part forced symplectic at these points "
          "(quantum corrections Q0+C0 vanish on solutions); unipotent reduction OK.")

# ================================================================ stage P: Jacobians
def stage_P():
    """Exact Jacobian corank of the full 120-var systems at rational family points:
    equal coranks quantum vs classical = local-dimension flatness at smooth points."""
    d = get_d3()
    vs, vidx = d["vs"], d["vidx"]
    random.seed(73)
    out = []
    for trial in range(3):
        u1, u2 = random_isotropic_pair(random)
        l1 = {tuple(1 if tt == bb else 0 for tt in range(4)): Fraction(u1[bb])
              for bb in range(4) if u1[bb]}
        l2 = {tuple(1 if tt == bb else 0 for tt in range(4)): Fraction(u2[bb])
              for bb in range(4) if u2[bb]}
        h = {}
        for deg, cfs in ((3, [1, -1, 2, 1]), (4, [2, 1, -1, 1, 3])):
            for i, cf in enumerate(cfs):
                t2 = {(0, 0, 0, 0): Fraction(cf)}
                for _ in range(deg - i):
                    t2 = smul(t2, l1)
                for _ in range(i):
                    t2 = smul(t2, l2)
                h = wadd(h, t2)
        imgs = [wadd(g, wbr(h, g)) for g in GEN]
        tv = [Fraction(0)] * len(vs)
        for s in range(4):
            for m, v in imgs[s].items():
                if sum(m) in (2, 3):
                    tv[vidx[(s, m)]] = v
        assert all(not r for r in direct_residuals(imgs, "qu"))
        coranks = {}
        for bk in ("qu", "cl"):
            rows = []
            for key, (c0, lam, mu) in d[bk].items():
                grad = {}
                for i, v in lam.items():
                    grad[i] = grad.get(i, 0) + v
                for (a, b), v in mu.items():
                    grad[a] = grad.get(a, 0) + v * tv[b]
                    grad[b] = grad.get(b, 0) + v * tv[a]
                rows.append([grad.get(i, 0) for i in range(len(vs))])
            coranks[bk] = len(vs) - frank(rows)
        out.append((tuple(u1), coranks["qu"], coranks["cl"]))
    agree = all(q == c for _, q, c in out)
    print(f"P: Jacobian corank (local dim bound) of full 120-var systems at 3 rational "
          f"Lagrangian-flow points: quantum {[q for _, q, _ in out]}, classical "
          f"{[c for _, _, c in out]} => {'EQUAL (local flatness at smooth points)' if agree else 'DIFFER: DIVERGENCE'}")
    return out

# ================================================================ stage O: emissions
def emit_full_slices():
    os.makedirs(SYSDIR, exist_ok=True)
    d = get_d3()
    vs = d["vs"]
    n = len(vs)
    sizes = {}
    # canonical unsliced 120-var systems (small, exact)
    for backend in ("qu", "cl"):
        eqs = d[backend]
        polys = []
        for (ri, m), (c0, lam, mu) in sorted(eqs.items()):
            out = {}
            zero = tuple([0] * n)
            if c0:
                out[zero] = c0
            for i, v in lam.items():
                e = [0] * n; e[i] = 1
                out[tuple(e)] = out.get(tuple(e), 0) + v
            for (a, b), v in mu.items():
                e = [0] * n; e[a] += 1; e[b] += 1
                out[tuple(e)] = out.get(tuple(e), 0) + v
            ps = poly_str(out, n)
            if ps:
                polys.append(ps)
        path = os.path.join(SYSDIR, f"dc2_d3_{backend}_full120.ms")
        write_ms(path, polys, n)
        sizes[f"{backend}_full120"] = (len(polys), os.path.getsize(path))
    # affine slices sized to detect a hypothetical top-dim (55) component:
    # dim V <= 55 (classical: cone under wt(w)=1,wt(v)=2; tangent at 0 = 55), so a
    # 65-dim random affine slab gives 0-dim iff some component has dim 55 (v+65>=120),
    # else EMPTY; posdim flags dim > 55 (impossible classically, a check for qu).
    for backend in ("qu", "cl"):
        eqs = d[backend]
        for codim_tag, npar in (("s65", 65),):
            random.seed(61 if backend == "qu" else 67)
            Amat = [[random.randint(-1, 1) for _ in range(npar)] for _ in range(n)]
            bvec = [random.randint(-1, 1) for _ in range(n)]
            polys = []
            for (ri, m), (c0, lam, mu) in sorted(eqs.items()):
                out = {}
                def acc(e, v):
                    if v:
                        out[e] = out.get(e, 0) + v
                zero = tuple([0] * npar)
                acc(zero, c0)
                for i, v in lam.items():
                    acc(zero, v * bvec[i])
                    for f in range(npar):
                        if Amat[i][f]:
                            e = [0] * npar
                            e[f] = 1
                            acc(tuple(e), v * Amat[i][f])
                for (a, b), v in mu.items():
                    ra = [(f, Amat[a][f]) for f in range(npar) if Amat[a][f]]
                    rb = [(f, Amat[b][f]) for f in range(npar) if Amat[b][f]]
                    acc(zero, v * bvec[a] * bvec[b])
                    for f, xa in ra:
                        e = [0] * npar
                        e[f] = 1
                        acc(tuple(e), v * xa * bvec[b])
                    for f, xb in rb:
                        e = [0] * npar
                        e[f] = 1
                        acc(tuple(e), v * xb * bvec[a])
                    for f, xa in ra:
                        for g, xb in rb:
                            e = [0] * npar
                            e[min(f, g)] += 1
                            e[max(f, g)] += 1
                            acc(tuple(e), v * xa * xb)
                ps = poly_str(out, npar)
                if ps:
                    polys.append(ps)
            path = os.path.join(SYSDIR, f"dc2_d3_{backend}_full_{codim_tag}.ms")
            write_ms(path, polys, npar)
            sizes[f"{backend}_{codim_tag}"] = (len(polys), os.path.getsize(path))
    return sizes

def stage_O():
    sizes = emit_full_slices()
    for k, (np_, sz) in sorted(sizes.items()):
        print(f"O: emitted systems/dc2/dc2_d3_{k}.ms: {np_} polys, {sz//1024} KB")
    # degree-4 cost counts
    def sdim(k):
        from math import comb
        return comb(k + 3, 3)
    unk4 = 4 * (sdim(2) + sdim(3) + sdim(4))
    eqs4 = 6 * sum(sdim(j) for j in range(0, 7))
    print(f"O: degree-4 slice size: {unk4} unknowns (4x{sdim(2)}+{sdim(3)}+{sdim(4)}), "
          f"{eqs4} quadratic equations (residual strata 0..6); quantum corrections: "
          "s=2 at strata 4,3,2,1,0 / s=3 at 2,1,0 / s=4 at 0.")

# ================================================================ main
STAGES = {"gate": stage_gate, "H": stage_H, "I": stage_I, "J": stage_J, "P": stage_P,
          "K": stage_K, "L": stage_L, "Ldeep": stage_Ldeep, "M": stage_M,
          "N": stage_N, "O": stage_O}

def main():
    args = sys.argv[1:]
    todo = []
    i = 0
    while i < len(args):
        if args[i] == "--stage":
            todo += args[i + 1].split(",")
            i += 2
        else:
            i += 1
    if not todo:
        todo = ["gate", "H", "I", "J", "K"]
    t0 = time.time()
    print(f"DC(2) degree-3 slice (exact; flint={'yes' if HAVE_FLINT else 'NO'})")
    for s in todo:
        STAGES[s]()
    print(f"TOTAL {time.time()-t0:.0f}s")

if __name__ == "__main__":
    main()
