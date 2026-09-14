#!/usr/bin/env python3
"""GATE (3) for (99,66): independent rerun of the h2-only pole system on the
CORRECTED face engine to full depth (delta2: p<=27, delta52: p<=63), with the
leading target computed independently as (K3 minor leading form)^3."""
import sys, json, time, importlib.util
import sympy as sp
spec = importlib.util.spec_from_file_location("cfe", "box/g9966-repair-gate-20260905/corrected_face_engine.py")
E = importlib.util.module_from_spec(spec); sys.modules["cfe"] = E; spec.loader.exec_module(E)

BR = {"delta2": (27, 9, 27), "delta52": (63, 21, 63)}   # (K2 depth, K3 lead, K2 lead)
out, t0 = {}, time.monotonic()
for branch, (P, LEAD3, LEAD2) in BR.items():
    ts = time.monotonic()
    # ---- independent target: cube the K3 minor leading form
    h3, hvars = E.h3_template()
    hmap, hfree, centre = E.h3_branch_map(branch)
    h3s = {k: E.substitute_map(v, hmap) for k, v in h3.items()}
    k3rows = E.local_rows(h3s, branch, LEAD3, exact_only=False)
    zeta = sp.Symbol("zeta")
    lead3 = sp.expand(sum(v*zeta**k for (n, k), v in k3rows.items() if n == LEAD3))
    below3 = {(n, k): str(v)[:40] for (n, k), v in k3rows.items() if n < LEAD3 and sp.expand(v) != 0}
    tgt_poly = sp.expand(lead3**3)
    tgt = {k: sp.expand(tgt_poly.coeff(zeta, k)) for k in range(0, sp.degree(tgt_poly, zeta)+1)}
    print(f"{branch}: K3 lead(t^{LEAD3}) = {sp.factor(lead3)} | K3 rows below lead: {len(below3)}", flush=True)

    k2, inner_free, major = E.build_major_h2(branch, P)
    tab = E.local_rows(k2, branch, P)
    loc = sp.Symbol("rho" if branch == "delta2" else "c")
    rows = []
    for n in range(1, P+1):
        ks = sorted({k for (m, k) in tab if m == n})
        allk = sorted(set(ks) | (set(tgt) if n == LEAD2 else set()))
        for k in allk:
            v = sp.expand(tab.get((n, k), sp.Integer(0)))
            if n == LEAD2: v = sp.expand(v - tgt.get(k, 0))
            rows.append((f"a{n}_z{k}", v))
    nz = [(l, v) for l, v in rows if sp.expand(v) != 0]
    elig = set(inner_free) - {loc}
    residual, subs, pivots, zeros = E.qstar_reduce(rows, elig)
    const = [(l, str(v)) for l, v in residual if sp.expand(v).is_number]
    out[branch] = {"depth": P, "K3_lead_power": LEAD3, "K3_lead": str(sp.factor(lead3)),
                   "K3_rows_below_lead_nonzero": len(below3),
                   "raw_rows": len(rows), "nonzero_raw_rows": len(nz),
                   "Qstar_pivots": len(pivots), "dependent_zero": zeros,
                   "residual_rows": len(residual),
                   "residual": [(l, str(v)[:120]) for l, v in residual[:8]],
                   "CONSTANT_residual": const,
                   "free_after": sorted(map(str, elig - set(subs)))[:40],
                   "n_free_after": len(elig - set(subs)),
                   "eligible": len(elig), "localizer_excluded": str(loc),
                   "secs": round(time.monotonic()-ts, 1)}
    print(f"{branch}: rows={len(rows)} nonzero={len(nz)} pivots={len(pivots)} "
          f"zeros={zeros} RESIDUAL={len(residual)} CONST={const} "
          f"free_after={len(elig-set(subs))} [{round(time.monotonic()-ts,1)}s]", flush=True)
json.dump(out, open("box/cone-vertex-gate-20260905/t5_g9966_depth.json","w"), indent=1, default=str)
print("secs", round(time.monotonic()-t0,1))
