#!/usr/bin/env python3
"""STAGE-2 completion check for R4-00 base-decide survivors.

Given an exact base point of a surviving component (CELL-R2: rational
(s,t,uz,vz,kappa); CELL-R1: Gaussian-rational (s,t,kappa,q,A8,B8) plus the
branch sign), this script rebuilds the frozen window (same clean-room
pipeline and checks as gen_r4_00_base_packets.py), verifies that the point
satisfies the closed base conditions and the constructible opens, then
attempts the grade-15..19 completion:

  - unique rank-2 T-solves for (A_m,B_m), m=9..13 (CELL-R2), or the rank-1
    row-1 solves for B_m with free A_m and the mu2 ladder (CELL-R1);
  - staged affine absorption of c31@17, c31@18, c31@19, D51@18-partner
    (D51@19) into (k2_1,k6_1,k2_2,k2_3);
  - target definitions mu4_1..3, mu6_1 and the grade-19 Jdet_0 value.

For each of several deterministic random draws of the remaining free window
coordinates it verifies that EVERY literal window equation G_i,n (n=8..19)
vanishes exactly and reports the defined Jdet_0 value.  A draw with
Jdet_0 != 0 is an exact grade-19 jet witness of the R4-00 packet on that
cell (field-valued finite jet only; no arc, map, or higher-grade claim).
If Jdet_0 == 0 for all draws the kill decision needs a symbolic follow-up
and is reported as JDET_ZERO_ON_SAMPLES.

Usage:
  stage2_completion_check.py --cell r2 --point s t uz vz kappa
  stage2_completion_check.py --cell r1 --eps +1 --point s t kappa qre qim
      [--a8 re im]
Rational entries as fractions like -25/9.  For r1 the base coordinates
s,t,kappa are taken rational, q Gaussian; A8 defaults to a free draw unless
--a8 is given (the row-1 line then determines B8).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "gen", HERE / "gen_r4_00_base_packets.py")
gen = importlib.util.module_from_spec(spec)
sys.modules["gen"] = gen
spec.loader.exec_module(gen)

F0, F1 = F(0), F(1)


def build():
    tails = gen.load_tails()
    rows_s = gen.build_rows(tails, 20, solved=True)
    findings = gen.structural_solved(rows_s, 20, strict=True)
    r2 = gen.derive_r2(findings)
    rrF = [[gen.to_frac_poly(rows_s[i][n]) for n in range(20)]
           for i in range(7)]
    comboF = {k: gen.to_frac_poly(v) for k, v in findings["combo"].items()}
    return tails, rows_s, findings, r2, rrF, comboF


def stage2_r2(point, findings, r2, rrF, comboF, draws=5) -> dict:
    XF = {k: gen.to_frac_poly(v) for k, v in r2["X"].items()}
    p_polF = gen.to_frac_poly(gen.p_of())
    q_polF = gen.to_frac_poly(gen.q_of())
    D_polF = gen.to_frac_poly(r2["D"])
    base = dict(zip(("s", "t", "uz", "vz", "kappa"), point))
    out: dict = {"cell": "r2", "point": {k: str(v) for k, v in base.items()}}
    val0 = [F0] * gen.NV
    for k, v in base.items():
        val0[gen.VIDX[k]] = v
    Dv = gen.peval(D_polF, val0)
    kv = base["kappa"]
    out["opens"] = {"D": str(Dv), "kappa": str(kv),
                    "st_nonzero": bool(base["s"] or base["t"])}
    if Dv == 0 or kv == 0 or not (base["s"] or base["t"]):
        out["status"] = "POINT_VIOLATES_OPENS"
        return out
    xvals = {k: str(gen.peval(P, val0)) for k, P in XF.items()}
    out["X_values"] = xvals
    if any(v != "0" for v in xvals.values()):
        out["status"] = "POINT_NOT_ON_BASE_LOCUS"
        return out
    pv, qv = gen.peval(p_polF, val0), gen.peval(q_polF, val0)
    results = []
    for draw in range(draws):
        stream = gen.det_stream(f"S2R2|{draw}")
        val = [next(stream) for _ in range(gen.NV)]
        for nm in ("Az", "Bz", "A7", "B7"):
            val[gen.VIDX[nm]] = F0
        for k, v in base.items():
            val[gen.VIDX[k]] = v

        def solve_pass():
            for n in range(14, 20):
                m = n - 6
                ai, bi = gen.VIDX[f"A{m}"], gen.VIDX[f"B{m}"]
                val[ai] = F0
                val[bi] = F0
                i1v = gen.peval(rrF[0][n], val)
                i2v = gen.peval(rrF[1][n], val)
                val[ai] = F(-2048) * (pv * i1v - 16 * qv * i2v) / Dv
                val[bi] = F(-2048) * (64 * qv * i1v + 16 * pv * i2v) / Dv
            for tname, (i, n) in (("mu4_1", (3, 17)), ("mu4_2", (3, 18)),
                                  ("mu4_3", (3, 19)), ("mu6_1", (5, 19))):
                val[gen.VIDX[tname]] = F0
                val[gen.VIDX[tname]] = gen.peval(rrF[i][n], val)
            val[gen.VIDX["Jdet_0"]] = F0
            val[gen.VIDX["Jdet_0"]] = 4 * gen.peval(comboF[("D71", 19)], val)

        rec = {"draw": draw}
        try:
            eqs = [comboF[("c31", 17)], comboF[("c31", 18)],
                   comboF[("c31", 19)], comboF[("D51", 19)]]
            uvars = ["k2_1", "k6_1", "k2_2", "k2_3"]
            solve_pass()
            b0 = [gen.peval(E, val) for E in eqs]
            M = []
            for uv in uvars:
                ci = gen.VIDX[uv]
                save = val[ci]
                val[ci] = save + 1
                solve_pass()
                M.append([gen.peval(E, val) - b0[i]
                          for i, E in enumerate(eqs)])
                val[ci] = save
            A = [[M[j][i] for j in range(4)] for i in range(4)]
            rhs = [-b for b in b0]
            for col in range(4):
                piv = next((r for r in range(col, 4) if A[r][col] != 0), None)
                if piv is None:
                    raise gen.SoftRetry("singular absorber matrix at ray")
                A[col], A[piv] = A[piv], A[col]
                rhs[col], rhs[piv] = rhs[piv], rhs[col]
                for r in range(4):
                    if r != col and A[r][col] != 0:
                        fac = A[r][col] / A[col][col]
                        A[r] = [a - fac * b for a, b in zip(A[r], A[col])]
                        rhs[r] = rhs[r] - fac * rhs[col]
            for uv, i in zip(uvars, range(4)):
                val[gen.VIDX[uv]] += rhs[i] / A[i][i]
            solve_pass()
            if any(gen.peval(E, val) != 0 for E in eqs):
                raise gen.SoftRetry("absorption did not land at ray")
            bad = [f"G{i+1}@{n}" for i in range(7) for n in range(8, 20)
                   if gen.peval(rrF[i][n], val) != 0]
            rec["window_vanishes"] = not bad
            rec["nonvanishing"] = bad[:8]
            rec["Jdet_0"] = str(val[gen.VIDX["Jdet_0"]])
        except gen.SoftRetry as exc:
            rec["soft_fail"] = str(exc)
        results.append(rec)
    out["draws"] = results
    witness = [r for r in results if r.get("window_vanishes")
               and r.get("Jdet_0") not in (None, "0")]
    allzero = [r for r in results if r.get("window_vanishes")
               and r.get("Jdet_0") == "0"]
    if witness:
        out["status"] = "GRADE19_JET_WITNESS_WITH_JDET_NONZERO"
    elif allzero and len(allzero) == len(results):
        out["status"] = "COMPLETIONS_EXIST_BUT_JDET_ZERO_ON_SAMPLES"
    else:
        out["status"] = "COMPLETION_OBSTRUCTED_OR_MIXED_SEE_DRAWS"
    return out


def stage2_r1(point, eps, a8, findings, rrF, comboF, draws=5) -> dict:
    sv, tv, kv, qre, qim = point
    out: dict = {"cell": "r1", "eps": eps,
                 "point": {"s": str(sv), "t": str(tv), "kappa": str(kv),
                           "q": f"{qre}+{qim}i"}}
    if kv == 0 or (qre, qim) == (F0, F0) or (sv == 0 and tv == 0):
        out["status"] = "POINT_VIOLATES_OPENS"
        return out
    qc = (qre, qim)

    def cadd(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def cmul(x, y):
        return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def csc(c, x):
        return (c * x[0], c * x[1])

    def cdiv(x, y):
        d = y[0] * y[0] + y[1] * y[1]
        return ((x[0] * y[0] + x[1] * y[1]) / d,
                (x[1] * y[0] - x[0] * y[1]) / d)

    results = []
    for draw in range(draws):
        stream = gen.det_stream(f"S2R1|{eps}|{draw}")
        C = []
        for i in range(gen.NV):
            C.append((next(stream), next(stream)))
        for nm in ("Az", "Bz", "A7", "B7"):
            C[gen.VIDX[nm]] = (F0, F0)
        C[gen.VIDX["s"]] = (sv, F0)
        C[gen.VIDX["t"]] = (tv, F0)
        C[gen.VIDX["kappa"]] = (kv, F0)
        uz = (F(-5, 6) * kv * sv - F(8 * eps, 6) * qim,
              F(8 * eps, 6) * qre)
        vz = (F(5, 6) * kv * tv - F(1, 6) * qre, -F(1, 6) * qim)
        C[gen.VIDX["uz"]] = uz
        C[gen.VIDX["vz"]] = vz
        if a8 is not None:
            C[gen.VIDX["A8"]] = a8

        def ceval(P):
            cache: dict = {}
            a, b = F0, F0
            for m, c in P.items():
                pr, pi = c, F0
                for v, e in m:
                    key = (v, e)
                    pw = cache.get(key)
                    if pw is None:
                        px, py = F1, F0
                        x, y = C[v]
                        for _ in range(e):
                            px, py = px * x - py * y, px * y + py * x
                        pw = (px, py)
                        cache[key] = pw
                    pr, pi = (pr * pw[0] - pi * pw[1],
                              pr * pw[1] + pi * pw[0])
                a, b = a + pr, b + pi
            return (a, b)

        epsi = (F0, F(eps))

        def solve_pass():
            for n in range(14, 20):
                m = n - 6
                bi = gen.VIDX[f"B{m}"]
                C[bi] = (F0, F0)
                i1v = ceval(rrF[0][n])
                C[bi] = cdiv(csc(F(-2048), i1v), qc)
                if n >= 15:
                    mu = gen.VIDX[f"mu2_{n-14}"]
                    C[mu] = (F0, F0)
                    r2v = ceval(rrF[1][n])
                    r1v = ceval(rrF[0][n])
                    C[mu] = cadd(r2v, cmul(csc(F(-1, 2), epsi), r1v))
            for tname, (i, n) in (("mu4_1", (3, 17)), ("mu4_2", (3, 18)),
                                  ("mu4_3", (3, 19)), ("mu6_1", (5, 19))):
                C[gen.VIDX[tname]] = (F0, F0)
                C[gen.VIDX[tname]] = ceval(rrF[i][n])
            C[gen.VIDX["Jdet_0"]] = (F0, F0)
            C[gen.VIDX["Jdet_0"]] = csc(F(4), ceval(comboF[("D71", 19)]))

        rec = {"draw": draw}
        try:
            solve_pass()
            # closed base conditions at the point (A8 free or pinned, B8 solved)
            closed = {"c21p14": ceval_named(rrF, comboF, "c21p", C, ceval,
                                            eps),
                      "conic1": ceval(comboF[("c31", 16)]),
                      "conic2": ceval(rrF[3][16]),
                      "e18a": ceval(rrF[5][18]),
                      "e18b": ceval(comboF[("D51", 18)]),
                      "e18c": ceval(comboF[("D71", 18)])}
            nz = {k: f"{v[0]}+{v[1]}i" for k, v in closed.items()
                  if v != (F0, F0)}
            if nz:
                rec["closed_conditions_nonzero"] = nz
                rec["window_vanishes"] = False
                results.append(rec)
                continue
            eqs = [comboF[("c31", 17)], comboF[("c31", 18)],
                   comboF[("c31", 19)], comboF[("D51", 19)]]
            uvars = ["k2_1", "k6_1", "k2_2", "k2_3"]
            b0 = [ceval(E) for E in eqs]
            M = []
            for uv in uvars:
                ci = gen.VIDX[uv]
                save = C[ci]
                C[ci] = cadd(save, (F1, F0))
                solve_pass()
                vals = [ceval(E) for E in eqs]
                M.append([(v[0] - b[0], v[1] - b[1])
                          for v, b in zip(vals, b0)])
                C[ci] = save
            solve_pass()
            A = [[M[j][i] for j in range(4)] for i in range(4)]
            rhs = [csc(F(-1), b) for b in b0]
            for col in range(4):
                piv = next((r for r in range(col, 4)
                            if A[r][col] != (F0, F0)), None)
                if piv is None:
                    raise gen.SoftRetry("singular absorber matrix at ray")
                A[col], A[piv] = A[piv], A[col]
                rhs[col], rhs[piv] = rhs[piv], rhs[col]
                for r in range(4):
                    if r != col and A[r][col] != (F0, F0):
                        fac = cdiv(A[r][col], A[col][col])
                        A[r] = [(a[0] - (fac[0] * b[0] - fac[1] * b[1]),
                                 a[1] - (fac[0] * b[1] + fac[1] * b[0]))
                                for a, b in zip(A[r], A[col])]
                        fb = cmul(fac, rhs[col])
                        rhs[r] = (rhs[r][0] - fb[0], rhs[r][1] - fb[1])
            for i, uv in enumerate(uvars):
                C[gen.VIDX[uv]] = cadd(C[gen.VIDX[uv]],
                                       cdiv(rhs[i], A[i][i]))
            solve_pass()
            if any(ceval(E) != (F0, F0) for E in eqs):
                raise gen.SoftRetry("absorption did not land at ray")
            bad = [f"G{i+1}@{n}" for i in range(7) for n in range(8, 20)
                   if ceval(rrF[i][n]) != (F0, F0)]
            rec["window_vanishes"] = not bad
            rec["nonvanishing"] = bad[:8]
            jd = C[gen.VIDX["Jdet_0"]]
            rec["Jdet_0"] = f"{jd[0]}+{jd[1]}i"
            rec["Jdet_zero"] = jd == (F0, F0)
        except gen.SoftRetry as exc:
            rec["soft_fail"] = str(exc)
        results.append(rec)
    out["draws"] = results
    witness = [r for r in results if r.get("window_vanishes")
               and not r.get("Jdet_zero", True)]
    allzero = [r for r in results if r.get("window_vanishes")
               and r.get("Jdet_zero")]
    if witness:
        out["status"] = "GRADE19_JET_WITNESS_WITH_JDET_NONZERO"
    elif allzero and len(allzero) == len(results):
        out["status"] = "COMPLETIONS_EXIST_BUT_JDET_ZERO_ON_SAMPLES"
    else:
        out["status"] = "COMPLETION_OBSTRUCTED_OR_MIXED_SEE_DRAWS"
    return out


def ceval_named(rrF, comboF, which, C, ceval, eps):
    if which == "c21p":
        r2v = ceval(rrF[1][14])
        r1v = ceval(rrF[0][14])
        return (r2v[0] + F(eps, 2) * r1v[1], r2v[1] - F(eps, 2) * r1v[0])
    raise ValueError(which)


def parse_frac(x: str) -> F:
    return F(x)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cell", choices=("r2", "r1"), required=True)
    ap.add_argument("--eps", type=int, default=1)
    ap.add_argument("--point", nargs="+", required=True)
    ap.add_argument("--a8", nargs=2, default=None)
    ap.add_argument("--draws", type=int, default=5)
    args = ap.parse_args()
    _, rows_s, findings, r2, rrF, comboF = build()
    if args.cell == "r2":
        if len(args.point) != 5:
            raise SystemExit("r2 point needs s t uz vz kappa")
        pt = [parse_frac(x) for x in args.point]
        out = stage2_r2(pt, findings, r2, rrF, comboF, args.draws)
    else:
        if len(args.point) != 5:
            raise SystemExit("r1 point needs s t kappa qre qim")
        pt = [parse_frac(x) for x in args.point]
        a8 = None
        if args.a8 is not None:
            a8 = (parse_frac(args.a8[0]), parse_frac(args.a8[1]))
        out = stage2_r1(pt, args.eps, a8, findings, rrF, comboF, args.draws)
    print(json.dumps(out, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
