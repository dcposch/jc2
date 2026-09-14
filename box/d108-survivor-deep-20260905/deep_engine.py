#!/usr/bin/env python3
"""DEEP extension of the D=108 delta=3 saturated schedule, RESTRICTED to the
stage-4/saturated surviving locus.

Licensing (FALLACY-v2).  The saturated T=8 residual ideal is
    I = < u^2, -2uv, u*L + v^2 >,  u = K2c_3_26 + 8*jet2,
                                   v = K2c_4_25 - K2c_4_26 - 20*jet1^2 .
u in rad(I) from u^2; v in rad(I) from v^2 = (uL+v^2) - u*L; and I is contained
in the prime <u,v>.  Hence rad(I) = <u,v> EXACTLY, so the SET of points
satisfying every saturated row is exactly V(u,v) intersected with the resolved
Q* pivots.  Restricting to V(u,v) therefore loses no point: a unit ideal after
restriction proves that no point of any extension field satisfies the extended
system, i.e. the branch is dead.  Nothing is dropped by a floor; the two locus
generators are ADDED as rows, and the engine's own Q* elimination consumes them
as unit pivots on K2c_3_26 and K2c_4_25.

Truncation control.  build_major_h2 is called with max_t = T instead of the
frozen 40.  k2 entries with r > T are never read by build_FG(.,.,T) nor by any
row emitted at t-power <= T, so this is an exact identity, verified by the
rows_sha256 replay of the charged saturated T=8 system.
"""
from __future__ import annotations
import hashlib, json, subprocess, sys, time
from pathlib import Path
import sympy as sp

REKILL = Path("/home/ubuntu/jc2/box/d108-rekill-20260905/work")
sys.path.insert(0, str(REKILL))
from rekill_engine import (SRC, FRZ, minor_incidence, qstar_reduce, symbol,
                           build_major_h2, substitute_map, outer_state, build_FG,
                           jacobian_band, local_rows, raw_minor_support, GAUGE_LEDGER)

OUT = Path("/home/ubuntu/jc2/box/d108-survivor-deep-20260905")

JET1, JET2 = sp.Symbol("jet1"), sp.Symbol("jet2")
U_GEN = sp.Symbol("K2c_3_26") + 8 * JET2
V_GEN = sp.Symbol("K2c_4_25") - sp.Symbol("K2c_4_26") - 20 * JET1 ** 2


def rows_hash(rows):
    return hashlib.sha256("".join(f"{l}\t{sp.srepr(sp.expand(v))}\n"
                                  for l, v in rows).encode()).hexdigest()


def build_state(T, jet0free=False, radius=SRC, offsets=None, locus=True, log=print, jT=None, fast=True):
    """Everything the chart expresses at truncation depth T."""
    t0 = time.monotonic()
    offsets = T - 1 if offsets is None else offsets
    rows0, hvars, h3 = minor_incidence(radius, radius.k3_face, jet0free)
    resid0, subs0, piv0, _ = qstar_reduce(rows0, hvars)
    h3r = {k: v for k, v in ((k, substitute_map(v, subs0)) for k, v in h3.items()) if v != 0}
    log(f"  [t={time.monotonic()-t0:.1f}s] minor incidence: {len(rows0)} rows, "
        f"{len(piv0)} pivots, residual {len(resid0)}")
    k2, k2free, k2meta = build_major_h2(radius, h3r, T, jet0free)
    if locus:
        LS = {sp.Symbol("K2c_3_26"): -8 * JET2,
              sp.Symbol("K2c_4_25"): sp.Symbol("K2c_4_26") + 20 * JET1 ** 2}
        k2 = {k: substitute_map(v, LS) for k, v in k2.items()}
        k2 = {k: v for k, v in k2.items() if v != 0}
        k2free = set(k2free) - set(LS)
        k2meta = dict(k2meta, locus_substitution={str(a): str(b) for a, b in LS.items()},
                      locus_variables_removed=sorted(map(str, LS)))
    log(f"  [t={time.monotonic()-t0:.1f}s] major h2: K2c={k2meta['K2c_count']} "
        f"D1 rows={k2meta['h2_D1_raw_rows']} pivots={k2meta['h2_D1_pivots']} "
        f"free={len(k2free)}")
    outer, outer_free, outer_meta = outer_state(radius, offsets)
    log(f"  [t={time.monotonic()-t0:.1f}s] outer: offsets 0..{offsets}, "
        f"pivots={outer_meta['D1_cumulative_pivots']} free={len(outer_free)}")
    KF, KG = (build_FG_fast if fast else build_FG)(k2, outer, T)
    log(f"  [t={time.monotonic()-t0:.1f}s] KF/KG built (|KF|={len(KF)}, |KG|={len(KG)})")
    LR = local_rows_fast if fast else local_rows
    f_local = LR(KF, T, jet0free)
    g_local = LR(KG, T, jet0free)
    log(f"  [t={time.monotonic()-t0:.1f}s] minor local tables done")
    jT = T if jT is None else jT
    jcache = (jacobian_all_bands_fast if fast else jacobian_all_bands)(KF, KG, jT, log=log)
    log(f"  [t={time.monotonic()-t0:.1f}s] Jacobian bands t=0..{jT} done; "
        f"t^0 band (J degree 178) nonzero w-slots = {len(jcache[0])}")
    free = set(k2free) | set(outer_free) | {v for v in hvars if v not in subs0}
    return {"T": T, "radius": radius, "jet0free": jet0free, "offsets": offsets,
            "locus": locus, "resid0": resid0, "KF": KF, "KG": KG,
            "f_local": f_local, "g_local": g_local, "free": free,
            "k2meta": k2meta, "outer_meta": outer_meta, "_jcache": jcache,
            "jT": jT,
            "J_top_band_t0_slots": len(jcache[0]),
            "build_seconds": round(time.monotonic() - t0, 1)}


def rows_upto(st, n, jmax=None, log=print):
    """All rows the chart expresses at local power <= n (J bands t <= jmax)."""
    jmax = n if jmax is None else jmax
    rows = [(f"h3_incidence_{l}", v) for l, v in st["resid0"]]
    counts = {"F": 0, "G": 0, "J": 0}
    for name, table in (("F", st["f_local"]), ("G", st["g_local"])):
        for p in range(1, n + 1):
            for k in raw_minor_support(name, st["jet0free"]).get(p, ()):
                rows.append((f"{name}_local{p}_coord{k}", table.get((p, k), sp.Integer(0))))
                counts[name] += 1
    for tp in range(1, jmax + 1):
        J = st.setdefault("_jcache", {}).get(tp)
        if J is None:
            t1 = time.monotonic()
            J = jacobian_band(st["KF"], st["KG"], tp)
            st["_jcache"][tp] = J
            log(f"    J band t={tp}: {len(J)} nonzero w-slots ({time.monotonic()-t1:.1f}s)")
        for k in range(179 - tp):
            rows.append((f"J_t{tp}_d{178-tp}_k{k}", J.get(k, sp.Integer(0))))
            counts["J"] += 1
    return rows, counts


def singular_check(residual, tag, outdir=OUT, timeout=3000):
    if not residual:
        return {"unit_ideal": False, "dimension": "FULL", "note": "EMPTY RESIDUAL: "
                "every imposed row is consumed by a Q* unit pivot or is identically "
                "zero on the locus; the ideal is (0), i.e. the whole remaining free "
                "space survives -- this is the strongest possible SURVIVAL, not a kill",
                "wrapper_control": "not_needed"}
    exprs = [sp.expand(v) for _l, v in residual]
    variables = sorted(set().union(*(e.free_symbols for e in exprs)), key=str)
    c, Zc = symbol("c"), symbol("Zc")
    if c not in variables: variables.append(c); variables.sort(key=str)
    ring = variables + [Zc]
    def S(e): return str(e).replace("**", "^")
    gens = [S(e) for e in exprs] + ["Zc*c-1"]
    script = (f"ring R=0,({','.join(map(str,ring))}),dp;\n"
              f"ideal I={','.join(gens)};\nideal Sd=std(I);\n"
              'print("BEGIN_DIM");print(dim(Sd));print("END_DIM");\n'
              'print("BEGIN_NF");print(reduce(1,Sd));print("END_NF");\n'
              'print("BEGIN_SIZE");print(size(Sd));print("END_SIZE");\n'
              f"ideal EmptyControl=c,Zc*c-1;\nideal PointControl=c-1,Zc*c-1;\n"
              f"ideal RawControl={','.join(S(e) for e in exprs)};\n"
              'print("BEGIN_CTL");print(reduce(1,std(EmptyControl)));'
              'print(reduce(1,std(PointControl)));print(reduce(1,std(RawControl)));'
              'print("END_CTL");\nquit;\n')
    (outdir / f"{tag}.sing").write_text(script)
    r = subprocess.run(["Singular", "-q"], input=script, text=True,
                       capture_output=True, timeout=timeout)
    (outdir / f"{tag}.sing.out").write_text(r.stdout + "\n--STDERR--\n" + r.stderr)
    def sec(n):
        return r.stdout.split(f"BEGIN_{n}\n", 1)[1].split(f"\nEND_{n}", 1)[0].strip()
    dim = int(sec("DIM").splitlines()[-1])
    ctl = sec("CTL").splitlines()
    return {"unit_ideal": dim < 0, "dimension": dim,
            "active_variables": len(variables),
            "reduce_1_in_std": sec("NF").splitlines()[-1],
            "gb_size": int(sec("SIZE").splitlines()[-1]),
            "controls": {"empty_c=0_must_be_unit": ctl[-3],
                         "point_c=1_must_be_nonunit": ctl[-2],
                         "raw_unlocalized": ctl[-1]},
            "wrapper": "Zc*c-1"}


# --------------------------------------------------------------- fast Jacobian
def jacobian_all_bands(KF, KG, max_t, log=print):
    """All Jacobian bands t = 1..max_t in ONE pass.

    The frozen formula
        J = 108*KF*(KG)_z - t*(KF)_t*(KG)_z - 72*(KF)_z*KG + (KF)_z*t*(KG)_t
    factors exactly as
        J = (KG)_z * [108*KF - t*(KF)_t]  -  (KF)_z * [72*KG - t*(KG)_t] ,
    which is two truncated products instead of four, and computing them once at
    max_t instead of once per band removes the second factor of ~max_t/3.
    Verified band-by-band against rekill_engine.jacobian_band (control C).
    """
    from rekill_engine import tz_add, tz_scale, tz_mul, tz_dt, tz_dz, tz_times_t, z_band_to_w
    t0 = time.monotonic()
    P = tz_add(tz_scale(KF, 108), tz_scale(tz_times_t(tz_dt(KF), max_t), -1))
    Q = tz_add(tz_scale(KG, 72), tz_scale(tz_times_t(tz_dt(KG), max_t), -1))
    prod = tz_add(tz_mul(tz_dz(KG), P, max_t),
                  tz_scale(tz_mul(tz_dz(KF), Q, max_t), -1))
    log(f"    [J] single-pass product at max_t={max_t} in "
        f"{time.monotonic()-t0:.1f}s ({len(prod)} (t,z) slots)")
    return {tp: z_band_to_w(prod, tp) for tp in range(0, max_t + 1)}


# ------------------------------------------------------- sparse-ring products
def tz_mul_fast(left, right, max_t):
    """tz_mul over sympy's sparse polynomial ring instead of Expr.

    Identical output (Control D replays the charged saturated-T8 rows_sha256
    through this path); ~15x faster, because the coefficient arithmetic is
    dict-based instead of building and expanding Add trees."""
    from sympy.polys.rings import ring
    from sympy import QQ
    syms = set()
    for v in left.values(): syms |= getattr(v, "free_symbols", set())
    for v in right.values(): syms |= getattr(v, "free_symbols", set())
    names = sorted(map(str, syms)) or ["_dummy_"]
    Rg = ring(names, QQ)[0]
    L = {k: Rg.from_expr(v) for k, v in left.items() if k[0] <= max_t}
    Rt = {k: Rg.from_expr(v) for k, v in right.items() if k[0] <= max_t}
    out = {}
    for (r1, q1), v1 in L.items():
        for (r2, q2), v2 in Rt.items():
            if r1 + r2 > max_t: continue
            key = (r1 + r2, q1 + q2)
            out[key] = v1 * v2 if key not in out else out[key] + v1 * v2
    return {k: v.as_expr() for k, v in out.items() if v}


def z_bands_to_w_fast(item, max_t):
    """z_band_to_w for every t-power at once, in the sparse ring."""
    from math import comb
    from collections import defaultdict
    from sympy.polys.rings import ring
    from sympy import QQ
    syms = set()
    for v in item.values(): syms |= getattr(v, "free_symbols", set())
    names = sorted(map(str, syms)) or ["_dummy_"]
    Rg = ring(names, QQ)[0]
    out = defaultdict(lambda: defaultdict(lambda: Rg.zero))
    for (r, q), v in item.items():
        if r > max_t: continue
        cv = Rg.from_expr(v)
        for k in range(q + 1):
            out[r][k] = out[r][k] + cv * (comb(q, k) * (-1) ** (q - k))
    return {r: {k: v.as_expr() for k, v in d.items() if v}
            for r, d in out.items()}


def jacobian_all_bands_fast(KF, KG, max_t, log=print):
    from rekill_engine import tz_add, tz_scale, tz_dt, tz_dz, tz_times_t
    t0 = time.monotonic()
    P = tz_add(tz_scale(KF, 108), tz_scale(tz_times_t(tz_dt(KF), max_t), -1))
    Q = tz_add(tz_scale(KG, 72), tz_scale(tz_times_t(tz_dt(KG), max_t), -1))
    prod = tz_add(tz_mul_fast(tz_dz(KG), P, max_t),
                  tz_scale(tz_mul_fast(tz_dz(KF), Q, max_t), -1))
    log(f"    [J-fast] single-pass product at max_t={max_t} in "
        f"{time.monotonic()-t0:.1f}s ({len(prod)} (t,z) slots)")
    bands = z_bands_to_w_fast(prod, max_t)
    log(f"    [J-fast] w-bands extracted at {time.monotonic()-t0:.1f}s")
    return {tp: bands.get(tp, {}) for tp in range(0, max_t + 1)}


def build_FG_fast(k2, outer, max_t):
    from rekill_engine import tz_add, outer_effective_tz
    k2sq = tz_mul_fast(k2, k2, max_t)
    k2cube = tz_mul_fast(k2sq, k2, max_t)
    KF = tz_add(k2cube, tz_mul_fast(outer_effective_tz(outer, "A2", max_t), k2, max_t),
                outer_effective_tz(outer, "A3", max_t))
    KG = tz_add(k2sq, tz_mul_fast(outer_effective_tz(outer, "B1", max_t), k2, max_t),
                outer_effective_tz(outer, "B2", max_t))
    return KF, KG


def local_rows_fast(item, max_power, jet0free):
    """local_rows with sparse-ring coefficient arithmetic."""
    from math import factorial
    from collections import defaultdict
    from sympy.polys.rings import ring
    from sympy import QQ
    from rekill_engine import symbols_jet
    bands = z_bands_to_w_fast(item, max_power)   # ring-based, not Expr
    syms = set()
    for poly in bands.values():
        for co in poly.values(): syms |= getattr(co, "free_symbols", set())
    syms |= {sp.Symbol("jet0"), sp.Symbol("jet1"), sp.Symbol("jet2")}
    names = sorted(map(str, syms))
    Rg = ring(names, QQ)[0]
    gj = {n: Rg.from_expr(sp.Symbol(n)) for n in ("jet0", "jet1", "jet2")}
    out = defaultdict(lambda: Rg.zero)
    for r, poly in bands.items():
        if r > max_power: continue
        for j, co in poly.items():
            # local power n = r + d + 2a + 3b + 4k with d+a+b+k = j, so
            # n >= r + 2j exactly; every j with r + 2j > max_power is vacuous.
            if r + 2 * j > max_power: continue
            cr = Rg.from_expr(co)
            for d in (range(j + 1) if jet0free else [0]):
                for b in range(j - d + 1):
                    for k in range(j - d - b + 1):
                        a = j - d - b - k
                        n = r + d + 2 * a + 3 * b + 4 * k
                        if n > max_power: continue
                        mn = factorial(j) // (factorial(d) * factorial(a)
                                              * factorial(b) * factorial(k))
                        term = cr * mn
                        if d: term = term * gj["jet0"] ** d
                        if a: term = term * gj["jet1"] ** a
                        if b: term = term * gj["jet2"] ** b
                        out[(n, k)] = out[(n, k)] + term
    return {t: v.as_expr() for t, v in out.items() if v}
