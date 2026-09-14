#!/usr/bin/env python3
"""GATE (1): independent test that Delta = {all outer coords 0} satisfies every
row of the D=108 delta=3 saturated system AS BUILT, and that the D1 outer rows
are homogeneous linear (so Delta satisfies them)."""
import sys, json, time
sys.path.insert(0, "box/d108-rekill-20260905/work")
import sympy as sp
from rekill_engine import (SRC, minor_incidence, qstar_reduce, substitute_map,
                           build_major_h2, outer_state, build_FG, local_rows,
                           raw_minor_support, jacobian_band, outer_specs)

t0 = time.monotonic()
T, offsets, jet0free = 8, 7, False
rows0, hvars, h3 = minor_incidence(SRC, SRC.k3_face, jet0free)
resid0, subs0, piv0, _ = qstar_reduce(rows0, hvars)
h3r = {k: v for k, v in ((k, substitute_map(v, subs0)) for k, v in h3.items()) if v != 0}
k2, k2free, k2meta = build_major_h2(SRC, h3r, 40, jet0free)
outer, outer_free, outer_meta = outer_state(SRC, offsets)
print("h3_incidence residual rows:", len(resid0), flush=True)
print("outer free count:", outer_meta["outer_free_count"], flush=True)

# --- A. are the D1 outer rows homogeneous linear in outer coords only?
allouter = set()
for b, vals in outer.items():
    for p, v in vals.items(): allouter |= v.free_symbols
bad = []
for b, vals in outer.items():
    for p, v in vals.items():
        v = sp.expand(v)
        if v == 0: continue
        if sp.Poly(v, *sorted(v.free_symbols, key=str)).total_degree() != 1: bad.append((b,p,"deg"))
        if v.subs({s: 0 for s in v.free_symbols}) != 0: bad.append((b,p,"inhom"))
        if not (v.free_symbols <= allouter): bad.append((b,p,"foreign"))
print("A. resolved outer entries non-linear/inhomogeneous/foreign:", len(bad), bad[:5], flush=True)

# --- B. the four constants: position, weight, offset, free?
specs = outer_specs(SRC)
cst = {}
for b, s in specs.items():
    pos = (s["degree"], 0)
    W = SRC.W(*pos)
    sym = sp.Symbol(f"{b}c_{pos[0]}_{pos[1]}")
    kept = pos in outer[b]
    resolved = outer[b].get(pos)
    cst[b] = {"pos": pos, "W": W, "W0": s["W0"], "offset": W - s["W0"],
              "kept": kept, "is_free_symbol": bool(sym in outer_free),
              "resolved_to_self": (resolved == sym) if kept else None,
              "threshold": s["threshold"], "d1_mult_W": SRC.d1_mult*W,
              "n_D1_rows_in_its_band": max(0, s["threshold"] - SRC.d1_mult*W)}
print("B. constants:", json.dumps(cst, indent=1, default=str), flush=True)

# --- C. Delta_0: set every outer coordinate to zero, evaluate ALL saturated rows
zero = {s: sp.Integer(0) for s in allouter}
outer0 = {b: {p: sp.Integer(0) for p in vals} for b, vals in outer.items()}
KF, KG = build_FG(k2, outer0, T)
KFfull, KGfull = build_FG(k2, outer, T)
k2cube_eq = all(sp.expand(KF.get(k,0) - v) == 0 for k, v in
                __import__("rekill_engine").tz_mul(__import__("rekill_engine").tz_mul(k2,k2,T),k2,T).items())
print("C0. KF|Delta == K2^3 :", k2cube_eq, flush=True)

f_local = local_rows(KF, T, jet0free); g_local = local_rows(KG, T, jet0free)
counts = {"F":0,"G":0,"J":0}; nonzero = []
for name, table in (("F", f_local), ("G", g_local)):
    for n in range(1, T+1):
        for k in raw_minor_support(name, jet0free).get(n, ()):
            v = sp.expand(table.get((n,k), sp.Integer(0)))
            counts[name]+=1
            if v != 0: nonzero.append((f"{name}_local{n}_coord{k}", str(v)[:90]))
for tp in range(1, T+1):
    J = jacobian_band(KF, KG, tp)
    for k in range(179-tp):
        v = sp.expand(J.get(k, sp.Integer(0))); counts["J"]+=1
        if v != 0: nonzero.append((f"J_t{tp}_k{k}", str(v)[:90]))
print("C. rows evaluated:", counts, "total", sum(counts.values())+len(resid0), flush=True)
print("C. NONZERO rows on Delta_0 (excl h3 incidence):", len(nonzero), nonzero[:8], flush=True)
print("C. h3_incidence residual (independent of outer):", len(resid0), [l for l,_ in resid0][:5], flush=True)
json.dump({"outer_entry_defects": len(bad), "constants": cst, "row_counts": counts,
           "h3_incidence_rows": len(resid0), "nonzero_on_Delta0": nonzero,
           "KF_equals_K2cube": bool(k2cube_eq), "secs": round(time.monotonic()-t0,1)},
          open("box/cone-vertex-gate-20260905/t1_d108.json","w"), indent=1, default=str)
print("secs", round(time.monotonic()-t0,1))
