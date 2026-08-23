#!/usr/bin/env python3
"""d43_slices.py -- multi-slice pointwise D43 emptiness census.

For each (prime, fiber, cell, slice seed): freeze the 10 base T
coordinates at random values, interpolate ALL canonical kernel
pairings K_i . b of the D43 joint completion system (census-90 + the
two legal x-side columns, bands 26..42) as validated quadratics in the
4 lift coordinates, reduce the span, and test the resulting quadric
system for solvability over the algebraic closure (Singular lex GB;
unit ideal <=> the whole 4-dim lift slice carries NO D43-prolongable
point).  Fail-closed: unvalidated fits abort the slice (recorded).

POINTWISE evidence only: unit-ideal slices support (never prove) the
family-level EMPTY verdict, which belongs to the symbolic D43
compat-ideal computation (jets bank -> reduce -> assemble).
"""
import json, os, random, subprocess, sys, time, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import d43_hunt as H
import d25_eplus as DE
import eplus43 as X

LIFTS = ["x16", "x19", "x24", "x27"]
BASIS = [e for e in itertools.product(range(3), repeat=4) if sum(e) <= 2]

def slice_verdict(p, lab, ci, seed, nsamp=24):
    env = DE.fiber_env(p, lab)
    hdr, rows = DE.parse_fiber_ms(p, lab)
    cells = DE.cells_of_fiber(p, lab)
    rng = random.Random(seed)
    base_fv = {v: rng.randrange(p) for v in H.FREE14}
    samples = []
    for i in range(nsamp):
        fv = dict(base_fv)
        for c in LIFTS:
            fv[c] = rng.randrange(p)
        try:
            cv = DE.solve_cell_point(p, hdr, rows, fv, *cells[ci])
            ok, pairs = H.kernel_pairings(p, env, cv)
        except AssertionError:
            continue
        if ok:
            return {"verdict": "CONSISTENT_SAMPLE", "fv": fv}
        samples.append(([fv[c] for c in LIFTS], pairs))
    npair = len(samples[0][1])
    nb = len(BASIS)
    Mrows = [[int(np.prod([pow(tv[j], e[j], p) for j in range(4)]) % p)
              for e in BASIS] for tv, _ in samples]
    fits = []
    for i in range(npair):
        y = [pr[i] for _, pr in samples]
        A = [Mrows[r][:] + [y[r]] for r in range(nb)]
        rr = 0; piv = []
        for c2 in range(nb):
            pr_ = next((r for r in range(rr, nb) if A[r][c2] % p), None)
            if pr_ is None: continue
            A[rr], A[pr_] = A[pr_], A[rr]
            iv = pow(A[rr][c2] % p, p - 2, p)
            A[rr] = [x * iv % p for x in A[rr]]
            for r2 in range(nb):
                if r2 != rr and A[r2][c2] % p:
                    f = A[r2][c2] % p
                    A[r2] = [(x - f * z) % p for x, z in zip(A[r2], A[rr])]
            piv.append(c2); rr += 1
        coef = [0] * nb
        for j, c2 in enumerate(piv):
            coef[c2] = A[j][nb]
        okfit = all(sum(coef[c2] * Mrows[r][c2] for c2 in range(nb)) % p
                    == y[r] for r in range(nb, len(samples)))
        if not okfit:
            return {"verdict": "FIT_FAILED", "pairing": i}
        fits.append(coef)
    V = np.array([[c % p for c in f] for f in fits], dtype=np.int64)
    M = V.copy(); r = 0
    for c in range(M.shape[1]):
        pv = next((i for i in range(r, M.shape[0]) if M[i][c]), None)
        if pv is None: continue
        M[[r, pv]] = M[[pv, r]]
        M[r] = M[r] * pow(int(M[r][c]), p - 2, p) % p
        nz = np.nonzero(M[:, c])[0]; nz = nz[nz != r]
        if len(nz): M[nz] = (M[nz] - np.outer(M[nz, c], M[r])) % p
        r += 1
    Q = M[:r]
    names = ["a", "b", "c", "d"]
    polys = []
    for row in Q:
        terms = []
        for coef, mono in zip(row, BASIS):
            if coef:
                t = str(int(coef))
                for nm, e in zip(names, mono):
                    if e:
                        t += "*%s%s" % (nm, "^%d" % e if e > 1 else "")
                terms.append(t)
        polys.append("+".join(terms))
    sing = ("ring R = %d, (a,b,c,d), lp;\nideal I = %s;\n"
            "ideal G = std(I);\ndim(G);\nquit;\n" % (p, ",".join(polys)))
    out = subprocess.run(["Singular", "-q"], input=sing,
                         capture_output=True, text=True,
                         env={**os.environ, "ESINGULAR_BROWSER": "cat",
                              "BROWSER": "cat"}).stdout.strip()
    dim = out.split()[-1] if out else "?"
    return {"verdict": ("EMPTY_SLICE" if dim == "-1" else
                        "NONEMPTY_SLICE_dim%s" % dim),
            "span_rank": int(r), "n_pairings": npair, "gb_dim": dim}

def main():
    jobs = []
    for p in (105337, 105673):
        for lab, ci in (("a00pp", 3), ("a00pp", 11), ("a11mp", 5),
                        ("a22pm", 0), ("a10pm", 7), ("a01pp", 13)):
            jobs.append((p, lab, ci))
    # exhaustive-flavor pass: every cell of the pilot fiber at p1
    for ci in range(16):
        jobs.append((105337, "a00pp", ci))
    results = []
    ck = os.path.join(HERE, "d43_slices.json")
    done = {}
    if os.path.exists(ck):
        prev = json.load(open(ck))
        results = prev["slices"]
        done = {(r["prime"], r["fiber"], r["cell"], r["seed"]) for r in results}
    for (p, lab, ci) in jobs:
        for seed in (101, 202):
            key = (p, lab, ci, seed)
            if key in done:
                continue
            t0 = time.time()
            try:
                v = slice_verdict(p, lab, ci, seed)
            except Exception as e:
                v = {"verdict": "ERROR", "error": str(e)[:200]}
            v.update({"prime": p, "fiber": lab, "cell": ci, "seed": seed,
                      "seconds": round(time.time() - t0)})
            results.append(v)
            print("p%d %s cell%02d seed%d: %s (%.0fs)"
                  % (p, lab, ci, seed, v["verdict"], time.time() - t0),
                  flush=True)
            with open(ck, "w") as f:
                json.dump({"tool": "cases/d43_slices.py",
                           "date": time.strftime("%Y-%m-%d"),
                           "note": ("pointwise lift-slice census of the "
                                    "D43 prolongation compat system; "
                                    "EMPTY_SLICE = the quadric system of "
                                    "all kernel pairings restricted to "
                                    "the 4 lifts is the unit ideal"),
                           "slices": results}, f, indent=1)
    cnt = {}
    for r in results:
        cnt[r["verdict"]] = cnt.get(r["verdict"], 0) + 1
    print("CENSUS:", cnt)

if __name__ == "__main__":
    main()
