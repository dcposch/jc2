#!/usr/bin/env python3
"""GATE (1)-localizers + (5): (a) Hc_5_3 and the K3 D2 face at MY witness;
(b) the h3-on-D1 probe row 2*jet1*jet2+1=0 imposed at FULL h2-only depth;
(c) what the engine literally emits at the leading pole power."""
import sys, json, time
sys.path.insert(0, "box/d108-rekill-20260905/work")
import sympy as sp
import rekill_engine as RE
from rekill_engine import (SRC, minor_incidence, qstar_reduce, substitute_map,
                           build_major_h2, local_rows, resolve_map, raw_minor_support)

pi, c, jet1, jet2 = sp.symbols("pi c jet1 jet2")
P = 32

def depth_run(extra_pin):
    """extra_pin: dict of forced substitutions applied to the chart before rows."""
    rows0, hvars, h3 = minor_incidence(SRC, SRC.k3_face, False)
    resid0, subs0, piv0, _ = qstar_reduce(rows0, hvars)
    h3r = {k: v for k, v in ((k, substitute_map(v, subs0)) for k, v in h3.items()) if v != 0}
    if extra_pin:
        h3r = {k: sp.expand(v.subs(extra_pin)) if hasattr(v,"subs") else v for k, v in h3r.items()}
        h3r = {k: v for k, v in h3r.items() if v != 0}
    k2, k2free, _ = build_major_h2(SRC, h3r, P, False)
    hfree = [v for v in hvars if v not in subs0]
    tab = local_rows(k2, P, False)
    tp = sp.Poly(sp.expand((pi**2 - c)**4), pi)
    tgt = {k: tp.coeff_monomial(pi**k) for k in range(9)}
    rows = []
    for n in range(1, P+1):
        ks = sorted({k for (m,k) in tab if m == n} | (set(tgt) if n == P else set()))
        for k in ks:
            v = sp.expand(tab.get((n,k), sp.Integer(0)))
            if n == P: v = sp.expand(v - tgt.get(k,0))
            rows.append((f"a{n}_pi{k}", v))
    elig = set(k2free) | set(hfree)
    residual, subs, piv, zeros = qstar_reduce(rows, elig)
    return dict(subs0=subs0, hvars=hvars, k2=k2, rows=len(rows), pivots=len(piv),
                zeros=zeros, residual=residual, elig=elig, subs=subs)

t0 = time.monotonic()
res = {}
# ---- (a) Hc_5_3 and the K3 D2 face at the witness jet1=jet2=c=1, free->0
base = depth_run(None)
pt = {s: sp.Integer(0) for s in base["elig"] - set(base["subs"])}
pt.update({jet1: 1, jet2: 1, c: 1})
full = dict(base["subs0"]); full.update(base["subs"])
for _ in range(4):
    full = {v: sp.expand(sp.together(r).subs(pt)) if hasattr(r,"subs") else r for v, r in full.items()}
full.update(pt); resolve_map(full)
hc53 = sp.expand(sp.Symbol("Hc_5_3").subs(full))
# K3 D2 face: the lowest-weight band of h3 at W = k3_face, in pi with t=s^4,z=pi*s^5
rows0, hvars, h3 = minor_incidence(SRC, SRC.k3_face, False)
h3w = {k: sp.expand(substitute_map(v, base["subs0"]).subs(full)) for k, v in h3.items()}
face3 = sp.expand(sum(v * pi**q for (r,q), v in h3w.items() if SRC.W(r,q) == SRC.k3_face))
k2w = {kk: (sp.expand(vv.subs(full)) if hasattr(vv,"subs") else vv) for kk, vv in base["k2"].items()}
face2 = sp.expand(sum(v * pi**kq[1] for kq, v in k2w.items() if SRC.W(*kq) == SRC.k2_face))
res["a_localizers"] = {"Hc_5_3": str(hc53), "equals_2_jet1_jet2": str(sp.expand(hc53-2)),
    "K3_D2_face": str(sp.factor(face3)), "K2_D2_face": str(sp.factor(face2)),
    "c": "1", "base_residual": len(base["residual"]), "base_pivots": base["pivots"]}
print("(a) Hc_5_3 =", hc53, "| K3 D2 face =", sp.factor(face3), "| K2 D2 face =", sp.factor(face2), flush=True)

# ---- (b) h3-on-D1 probe at FULL depth: 2*jet1*jet2 + 1 = 0  -> jet1=1, jet2=-1/2
probe = depth_run({jet1: sp.Integer(1), jet2: sp.Rational(-1,2)})
res["b_h3D1_probe_full_depth"] = {
    "pin": "jet1=1, jet2=-1/2 (2*jet1*jet2+1=0)", "rows": probe["rows"],
    "pivots": probe["pivots"], "dependent_zero": probe["zeros"],
    "residual_rows": len(probe["residual"]),
    "residual": [(l, str(v)[:120]) for l, v in probe["residual"][:6]],
    "CONSTANT_residual": [(l, str(v)) for l, v in probe["residual"] if sp.expand(v).is_number]}
print("(b) h3D1-probe full depth: rows", probe["rows"], "pivots", probe["pivots"],
      "RESIDUAL", len(probe["residual"]),
      [(l,str(v)) for l,v in probe["residual"] if sp.expand(v).is_number], flush=True)

# ---- (c) what does the engine literally emit at the leading pole powers?
res["c_leading_target_rows"] = {
  "F_leading_local_power": max(raw_minor_support("F", False)),
  "G_leading_local_power": max(raw_minor_support("G", False)),
  "engine_row_form": "rows.append((label, table.get((n,k), 0)))  -- imposes = 0, "
                     "no target subtraction (step4_saturated.py:44-46, step3_joint.py)",
  "consequence": "at n=96 (F) / 64 (G) the emitted row would demand a_32=0, "
                 "contradicting the branch datum a_32=(pi^2-c)^4; never reached (T<=22)"}
print("(c) F/G leading local powers:", res["c_leading_target_rows"]["F_leading_local_power"],
      res["c_leading_target_rows"]["G_leading_local_power"], flush=True)
json.dump(res, open("box/cone-vertex-gate-20260905/t6_localizers.json","w"), indent=1, default=str)
print("secs", round(time.monotonic()-t0,1))
