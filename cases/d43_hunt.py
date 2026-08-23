#!/usr/bin/env python3
"""d43_hunt.py -- hunt for D43-prolongable base points on the D25 cells.

STATUS: INTERNAL TOOLING, UNREVIEWED.  FAIL-CLOSED.

MEASURED CONTEXT (this session): at every sampled D25 cell point
(witness + random interiors, both primes), the joint affine D43
completion system over the 90 first-occurrence coordinates (even bands
26..40 + 42) is INCONSISTENT with defect exactly 1, and the defect is
not absorbed by re-opening the band-24 frontier or the deep-tail kernel
freedom.  So the D43 prolongation imposes (at least) ONE scalar
compatibility condition c on the 14 free cell parameters
(T = x57,x59,x60,x62,x63,x65,x66,x68,x72,x73; lifts x16,x19,x24,x27).

THIS TOOL: fixes all free parameters but one, samples the canonical
compat scalar c(t) along the line, interpolates it as a polynomial
(holdout-validated; rational fallback), finds its roots in F_p, and
verifies each root by the full defect test + the full two-stage
prolongation of eplus43.prolong_point (final jet replay nu >= 43).

The compat scalar is canonical-normalized: c = lambda . b where lambda
is the first RREF-canonical left-kernel functional of A with
lambda . b != 0 at the reference point, recomputed per sample point
(so c is a piecewise-rational function of t; holdout validation
rejects branch mixing).  A root candidate is accepted ONLY if the full
system A u = b becomes consistent there (defect 0) and prolong_point
replays to nu >= 43.

Usage:
  python3 cases/d43_hunt.py --measure          # per-coordinate degrees
  python3 cases/d43_hunt.py --hunt [--prime P --fiber LAB --cell N]
        [--coord x59] [--samples N] [--seed S] [--out FILE]
"""
import argparse
import json
import os
import random
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import valuation_e as V
import eplus43 as X
import d25_eplus as DE

V43 = X.V43
FREE14 = DE.FREE_BASE + DE.FREE_LIFT


def joint_system(p, env, cellval):
    """Completed D25 point -> (A, b) of the census-90 joint system
    (even bands 26..40 and band 42; the prolong_point stage-A/B rows)."""
    dval, _dg = DE.reconstruct_point(p, cellval, env)
    wit72, deep = DE.witness72_of(p, dval)
    point_v2, _E, frontier = X.completed_point_v2(p, wit72, deep, env)
    extra = {}
    for labl, v in frontier.items():
        fam, lvl = labl.rsplit("_", 1)
        extra[(fam, int(lvl) - 32)] = v
    point = X.point43_from_v2(p, wit72, deep, env, extra_tails=extra)
    pt, _r3, _h = V.radical_env(p)
    Z = [pow(pt["z"], m, p) for m in range(42)]
    E = X._build_E(point, p, Z)
    Vv = E.V.astype(np.int64)
    Gg = E.G.astype(np.int64)
    unk = X.prolong_unknowns()
    cidx = [V43.GIDX[c] for c in unk]
    cidx += [X.XCOL_A, X.XCOL_B]      # legal x-side completion columns
    rows = []
    for k in range(26, 43, 2):
        rows += [(a, k) for a in X.rung_rows(k)]
    A = np.array([[int(Gg[a][n][c]) for c in cidx] for (a, n) in rows],
                 dtype=np.int64)
    b = np.array([(-int(Vv[a][n])) % p for (a, n) in rows],
                 dtype=np.int64)
    return A, b


def compat_scalar(p, env, cellval):
    """(c, defect): canonical compat scalar of the joint system."""
    A, b = joint_system(p, env, cellval)
    K, rk = X.left_kernel_np(A, p)
    cs = [(int(k @ b % p.__index__()) if False else int((k @ b) % p))
          for k in K]
    bad = [c for c in cs if c]
    defect = V43.rankp(np.concatenate([A, b[:, None]], axis=1).copy(),
                       p) - rk
    if not bad:
        return 0, defect
    return bad[0], defect


def cell_point_on_line(p, hdr, rows, cells, ci, base_fv, coord, t):
    fv = dict(base_fv)
    fv[coord] = t % p
    return DE.solve_cell_point(p, hdr, rows, fv, *cells[ci])


# ---------------------------------------------------- poly interpolation
def lagrange_fit(ts, cs, p):
    """Newton-form interpolation through the points; returns coeff list
    (low->high) of the unique poly of degree < len(ts)."""
    n = len(ts)
    dd = list(cs)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            num = (dd[i] - dd[i - 1]) % p
            den = (ts[i] - ts[i - j]) % p
            dd[i] = num * pow(den, p - 2, p) % p
    coef = [0] * n
    poly = [0] * n
    poly[0] = 1
    deg = 0
    coef[0] = dd[0]
    cur = [1]
    for j in range(1, n):
        # cur *= (x - ts[j-1])
        new = [0] * (len(cur) + 1)
        for i, cv in enumerate(cur):
            new[i + 1] = (new[i + 1] + cv) % p
            new[i] = (new[i] - cv * ts[j - 1]) % p
        cur = new
        for i, cv in enumerate(cur):
            coef[i] = (coef[i] + dd[j] * cv) % p
    while len(coef) > 1 and coef[-1] == 0:
        coef.pop()
    return coef


def peval(coef, t, p):
    acc = 0
    for c in reversed(coef):
        acc = (acc * t + c) % p
    return acc


def poly_roots(coef, p):
    """All roots in F_p of the poly (low->high), via gcd(x^p - x, f)
    and Cantor-Zassenhaus splitting."""
    def pmod(a, m):
        a = [c % p for c in a]
        dm = len(m) - 1
        inv = pow(m[-1], p - 2, p)
        while len(a) - 1 >= dm and any(a):
            if a[-1] == 0:
                a.pop()
                continue
            f = a[-1] * inv % p
            sh = len(a) - 1 - dm
            for i, c in enumerate(m):
                a[sh + i] = (a[sh + i] - f * c) % p
            while len(a) > 1 and a[-1] == 0:
                a.pop()
        return a

    def pmulmod(a, b, m):
        r = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        r[i + j] = (r[i + j] + x * y) % p
        return pmod(r, m)

    def ppowmod(a, e, m):
        r = [1]
        a = pmod(list(a), m)
        while e:
            if e & 1:
                r = pmulmod(r, a, m)
            a = pmulmod(a, a, m)
            e >>= 1
        return r

    def pgcd(a, b):
        a = [c % p for c in a]
        b = [c % p for c in b]
        while any(b):
            a = pmod(a, b + [0] * 0) if len(a) >= len(b) else a
            a, b = b, pmod(a, b)
        while len(a) > 1 and a[-1] == 0:
            a.pop()
        if any(a):
            inv = pow(a[-1], p - 2, p)
            a = [c * inv % p for c in a]
        return a

    f = [c % p for c in coef]
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    if len(f) <= 1:
        return []
    # x^p mod f
    xp = ppowmod([0, 1], p, f)
    xp_minus_x = list(xp) + [0] * max(0, 2 - len(xp))
    xp_minus_x[1] = (xp_minus_x[1] - 1) % p
    g = pgcd(f, xp_minus_x)
    roots = []
    rng = random.Random(20260843)
    stack = [g]
    while stack:
        h = stack.pop()
        while len(h) > 1 and h[-1] == 0:
            h.pop()
        d = len(h) - 1
        if d == 0:
            continue
        if d == 1:
            roots.append((-h[0]) * pow(h[1], p - 2, p) % p)
            continue
        # random split
        for _ in range(60):
            a = rng.randrange(p)
            s = ppowmod([a, 1], (p - 1) // 2, h)
            s = list(s) + [0]
            s[0] = (s[0] - 1) % p
            u = pgcd(h, s)
            du = len(u) - 1
            if 0 < du < d:
                # h / u
                q = polydiv(h, u, p)
                stack.append(u)
                stack.append(q)
                break
        else:
            raise RuntimeError("CZ split failed")
    return sorted(set(roots))


def polydiv(a, b, p):
    a = [c % p for c in a]
    b = [c % p for c in b]
    out = [0] * (len(a) - len(b) + 1)
    inv = pow(b[-1], p - 2, p)
    while len(a) >= len(b) and any(a):
        if a[-1] == 0:
            a.pop()
            continue
        f = a[-1] * inv % p
        sh = len(a) - len(b)
        out[sh] = f
        for i, c in enumerate(b):
            a[sh + i] = (a[sh + i] - f * c) % p
        while len(a) > 1 and a[-1] == 0:
            a.pop()
    return out


# ------------------------------------------------------------- drivers
def measure(p=105337, lab="a00pp", ci=3, seed=20260843, nsamp=9):
    """Per-coordinate degree probe: fit degree d = nsamp-2 through
    nsamp-1 points, validate on the last; report the apparent degree."""
    env = DE.fiber_env(p, lab)
    hdr, rows = DE.parse_fiber_ms(p, lab)
    cells = DE.cells_of_fiber(p, lab)
    rng = random.Random(seed)
    base_fv = {v: rng.randrange(p) for v in FREE14}
    print("reference point: cell %d, fiber %s, p=%d" % (ci, lab, p))
    for coord in FREE14:
        ts, cs = [], []
        t0 = time.time()
        for i in range(nsamp):
            t = rng.randrange(p)
            while t in ts:
                t = rng.randrange(p)
            try:
                cv = cell_point_on_line(p, hdr, rows, cells, ci,
                                        base_fv, coord, t)
                c, defect = compat_scalar(p, env, cv)
            except AssertionError as e:
                print("  %s: pipeline failed at t=%d (%s)" %
                      (coord, t, str(e)[:60]))
                break
            ts.append(t)
            cs.append(c)
        else:
            deg = None
            for d in range(0, nsamp - 1):
                coef = lagrange_fit(ts[:d + 1], cs[:d + 1], p)
                if all(peval(coef, ts[j], p) == cs[j]
                       for j in range(d + 1, nsamp)):
                    deg = len(coef) - 1
                    break
            print("  %s: apparent degree %s (%d samples, %.0fs)"
                  % (coord, deg if deg is not None else
                     ">%d" % (nsamp - 2), nsamp, time.time() - t0),
                  flush=True)


def hunt(p, lab, ci, coord, nsamp, seed, out_path, max_lines=6):
    env = DE.fiber_env(p, lab)
    hdr, rows = DE.parse_fiber_ms(p, lab)
    cells = DE.cells_of_fiber(p, lab)
    rng = random.Random(seed)
    found = []
    lines_tried = 0
    while lines_tried < max_lines and not found:
        lines_tried += 1
        base_fv = {v: rng.randrange(p) for v in FREE14}
        print("line %d: coord %s, base seed drawn" % (lines_tried,
                                                      coord), flush=True)
        ts, cs = [], []
        t0 = time.time()
        bad = False
        for i in range(nsamp):
            t = rng.randrange(p)
            while t in ts:
                t = rng.randrange(p)
            try:
                cv = cell_point_on_line(p, hdr, rows, cells, ci,
                                        base_fv, coord, t)
                c, _d = compat_scalar(p, env, cv)
            except AssertionError:
                continue
            ts.append(t)
            cs.append(c)
            if len(ts) >= 8 and len(ts) % 4 == 0:
                # try fits of increasing degree with 3 holdouts
                for d in range(0, len(ts) - 4):
                    coef = lagrange_fit(ts[:d + 1], cs[:d + 1], p)
                    if all(peval(coef, ts[j], p) == cs[j]
                           for j in range(d + 1, len(ts))):
                        print("   fit: degree %d after %d samples "
                              "(%.0fs)" % (len(coef) - 1, len(ts),
                                           time.time() - t0),
                              flush=True)
                        rts = poly_roots(coef, p)
                        print("   roots in F_p: %s" % rts, flush=True)
                        for rt in rts:
                            try:
                                cvr = cell_point_on_line(
                                    p, hdr, rows, cells, ci, base_fv,
                                    coord, rt)
                                cr, dr = compat_scalar(p, env, cvr)
                            except AssertionError as e:
                                print("   root %d: pipeline failed "
                                      "(%s)" % (rt, str(e)[:60]),
                                      flush=True)
                                continue
                            print("   root %d: compat=%d defect=%d"
                                  % (rt, cr, dr), flush=True)
                            if dr == 0:
                                fv = dict(base_fv)
                                fv[coord] = rt
                                found.append({
                                    "prime": p, "fiber": lab,
                                    "cell": ci, "coord": coord,
                                    "root": int(rt), "free14": fv,
                                    "line": lines_tried})
                        bad = True
                        break
                if bad:
                    break
        if not found and not bad:
            print("   no stable fit within %d samples on this line"
                  % nsamp, flush=True)
    if out_path and found:
        with open(out_path, "w") as f:
            json.dump({"found": found, "seed": seed}, f, indent=1)
        print("-> wrote %s" % out_path)
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--measure", action="store_true")
    ap.add_argument("--hunt", action="store_true")
    ap.add_argument("--prime", type=int, default=105337)
    ap.add_argument("--fiber", default="a00pp")
    ap.add_argument("--cell", type=int, default=3)
    ap.add_argument("--coord", default="x16")
    ap.add_argument("--samples", type=int, default=64)
    ap.add_argument("--seed", type=int, default=20260843)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    if a.measure:
        measure(a.prime, a.fiber, a.cell, a.seed)
        return
    if a.hunt:
        hunt(a.prime, a.fiber, a.cell, a.coord, a.samples, a.seed,
             a.out or os.path.join(HERE, "d43_hunt.json"))
        return
    ap.print_help()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "peel":
        pass          # dispatched by the peel block at module end
    else:
        main()


# ------------------------------------------------------ nested peel hunt
def kernel_pairings(p, env, cellval):
    """(consistent, pairs): pairs = [K_i . b] over the RREF-canonical
    left-kernel basis of A (fixed canonical row order); consistent
    <=> all pairings zero <=> b in colspan(A)."""
    A, b = joint_system(p, env, cellval)
    K, rk = X.left_kernel_np(A, p)
    pairs = [int((k @ b) % p) for k in K]
    return (not any(pairs)), pairs


def blackbox_roots(g, p, rng, tag="", min_samp=5, max_samp=13):
    """Zeros of a black-box F_p function via adaptive polynomial then
    rational fitting with 2 holdouts.  g(t) -> value or None."""
    ts, vs = [], []
    tries = 0
    while len(ts) < max_samp and tries < 3 * max_samp:
        tries += 1
        t = rng.randrange(p)
        if t in ts:
            continue
        v = g(t)
        if v is None:
            continue
        ts.append(t)
        vs.append(v % p)
        n = len(ts)
        if n < min_samp:
            continue
        # polynomial fits, 2 holdouts
        for d in range(0, n - 3):
            coef = lagrange_fit(ts[:d + 1], vs[:d + 1], p)
            if len(coef) - 1 > d:
                continue
            if all(peval(coef, ts[j], p) == vs[j] for j in range(d + 1, n)):
                rts = poly_roots(coef, p)
                return rts, ("poly deg %d, %d samples" % (len(coef) - 1,
                                                         n))
        # rational fits P/Q, 2 holdouts
        for tot in range(2, n - 3):
            for dn in range(0, tot + 1):
                dd = tot - dn
                m = dn + dd + 2
                Mm = []
                for i in range(m):
                    row = [pow(ts[i], e, p) for e in range(dn + 1)]
                    row += [(-vs[i] * pow(ts[i], e, p)) % p
                            for e in range(dd + 1)]
                    Mm.append(row)
                Mm = np.array(Mm, dtype=np.int64)
                K2, rk2 = X.left_kernel_np(Mm.T % p, p)
                if not len(K2):
                    continue
                sol = K2[0]
                P = [int(c) for c in sol[:dn + 1]]
                Q = [int(c) for c in sol[dn + 1:]]
                if not any(Q):
                    continue
                okv = True
                for j in range(m, n):
                    qv = peval(Q, ts[j], p)
                    if qv == 0 or peval(P, ts[j], p) != vs[j] * qv % p:
                        okv = False
                        break
                if okv and n - m >= 2:
                    rts = [r for r in poly_roots(P, p)
                           if peval(Q, r, p) != 0]
                    return rts, ("rational (%d/%d), %d samples"
                                 % (dn, dd, n))
    return None, "no stable fit (%d samples)" % len(ts)


def peel_hunt(p, lab, ci, coords, seed=20260843, max_depth=4,
              verbose=True):
    """Zero the kernel pairings K_i . b one at a time (fixed canonical
    indices, chosen adaptively) by nested adjustment of coords;
    success = ALL pairings zero (b in colspan)."""
    env = DE.fiber_env(p, lab)
    hdr, rows = DE.parse_fiber_ms(p, lab)
    cells = DE.cells_of_fiber(p, lab)
    rng = random.Random(seed)
    fv0 = {v: rng.randrange(p) for v in FREE14}
    cache = {}
    stats = {"evals": 0}

    def dc(fv):
        key = tuple(sorted((k, int(v) % p) for k, v in fv.items()))
        if key in cache:
            return cache[key]
        try:
            cv = DE.solve_cell_point(p, hdr, rows, dict(fv), *cells[ci])
            out = kernel_pairings(p, env, cv)
        except AssertionError:
            out = None
        stats["evals"] += 1
        cache[key] = out
        return out

    def zero_chain(fv, idxs, rng2):
        """Adjust coords[0..len(idxs)-1] so pairs[idxs[j]] == 0 for all
        j; nested (innermost = idxs[0]).  Returns fv' or None."""
        k = len(idxs)
        if k == 0:
            return fv
        coord = coords[k - 1]

        def g(t):
            fv2 = zero_chain({**fv, coord: t}, idxs[:-1], rng2)
            if fv2 is None:
                return None
            r = dc(fv2)
            if r is None:
                return None
            return r[1][idxs[-1]]

        rts, how = blackbox_roots(g, p, rng2)
        if verbose:
            print("   level %d (%s, K[%d]): %s -> roots %s"
                  % (k, coord, idxs[-1], how, rts), flush=True)
        if not rts:
            return None
        for rt in rts:
            fv2 = zero_chain({**fv, coord: rt}, idxs[:-1], rng2)
            if fv2 is None:
                continue
            r = dc(fv2)
            if r is None:
                continue
            if all(r[1][i] == 0 for i in idxs):
                return fv2
        return None

    idxs = []
    fv_cur = dict(fv0)
    for depth in range(1, max_depth + 1):
        r = dc(fv_cur)
        if r is None:
            print("pipeline failed at the chain point", flush=True)
            return None, depth - 1, stats
        if r[0]:
            print("CONSISTENT after zeroing %d pairings (%d evals)"
                  % (len(idxs), stats["evals"]), flush=True)
            return fv_cur, len(idxs), stats
        nz = [i for i, c in enumerate(r[1]) if c]
        print("depth %d: %d/%d pairings still nonzero; targeting K[%d]"
              % (depth, len(nz), len(r[1]), nz[0]), flush=True)
        idxs.append(nz[0])
        t0 = time.time()
        rng2 = random.Random(seed + 1000 * depth)
        fv_new = zero_chain(dict(fv0), idxs, rng2)
        if fv_new is None:
            print("depth %d: chain not zeroable on this line (%d evals,"
                  " %.0fs)" % (depth, stats["evals"], time.time() - t0),
                  flush=True)
            return None, depth, stats
        fv_cur = fv_new
        print("depth %d: chain zeroed (%d evals, %.0fs)"
              % (depth, stats["evals"], time.time() - t0), flush=True)
    r = dc(fv_cur)
    if r is not None and r[0]:
        return fv_cur, len(idxs), stats
    if r is not None:
        nz = [i for i, c in enumerate(r[1]) if c]
        print("MAX DEPTH reached; %d pairings still nonzero" % len(nz),
              flush=True)
    return None, max_depth, stats


def main_peel():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime", type=int, default=105337)
    ap.add_argument("--fiber", default="a00pp")
    ap.add_argument("--cell", type=int, default=3)
    ap.add_argument("--depth", type=int, default=3)
    ap.add_argument("--seed", type=int, default=20260843)
    ap.add_argument("--coords", default="x19,x27,x63,x73")
    ap.add_argument("--out", default=None)
    a = ap.parse_args(sys.argv[2:])
    fv, k, stats = peel_hunt(a.prime, a.fiber, a.cell,
                             a.coords.split(","), a.seed, a.depth)
    if fv is not None:
        print("SUCCESS at depth %d: %s" % (k, json.dumps(
            {kk: int(vv) for kk, vv in fv.items()})))
        if a.out:
            json.dump({"prime": a.prime, "fiber": a.fiber,
                       "cell": a.cell, "free14":
                       {kk: int(vv) for kk, vv in fv.items()},
                       "depth": k}, open(a.out, "w"), indent=1)
            print("-> wrote %s" % a.out)
    else:
        print("NO SUCCESS through depth %d (%d evals): obstruction "
              "depth exceeds the tried chain on this line"
              % (a.depth, stats["evals"]))


if len(sys.argv) > 1 and sys.argv[1] == "peel":
    main_peel()
    sys.exit(0)
