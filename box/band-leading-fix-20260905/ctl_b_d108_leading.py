#!/usr/bin/env python3
"""CONTROL (b): D=108 leading stage, leading row alone, Δ-witness substitution.

Rebuild the gate's Δ-witness (cvg_t3: a_p=0 for p<32, a_32=(π²−c)^4, remaining
free → 0, jet1=jet2=c=1). On Δ, KF=K2^3 and KG=K2^2, so the engine's leading
pole rows at n=96/64 are the coefficients of a_32^3 and a_32^2. After the
patch those rows are coefficient − (π²−c)^{12 resp. 8}. Direct substitution
of the witness must annihilate every tagged leading row; the old homogeneous
emission evaluates to the target (including the constant 1 at k=0) and would
be the spurious UNIT at stage 92/60.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "d108-rekill-20260905" / "work"))
from rekill_engine import (
    SRC, minor_incidence, qstar_reduce, substitute_map, build_major_h2,
    local_rows, resolve_map, pole_coeff, raw_minor_support, tz_mul, symbol,
    leading_pole_power, leading_pole_target_table, stage_spec,
)

t0 = time.monotonic()
P = 32
jet0free = False
pi, c = sp.symbols("pi c")
jet1, jet2 = sp.symbols("jet1 jet2")

rows0, hvars, h3 = minor_incidence(SRC, SRC.k3_face, jet0free)
resid0, subs0, _, _ = qstar_reduce(rows0, hvars)
h3r = {k: v for k, v in ((k, substitute_map(v, subs0)) for k, v in h3.items()) if v != 0}
k2, k2free, _ = build_major_h2(SRC, h3r, P, jet0free)
hfree = [v for v in hvars if v not in subs0]
tab = local_rows(k2, P, jet0free)
target32 = sp.Poly(sp.expand((pi**2 - c)**4), pi)
tgt32 = {k: target32.coeff_monomial(pi**k) for k in range(9)}

raw = []
for n in range(1, P + 1):
    ks = sorted({k for (m, k) in tab if m == n})
    allk = sorted(set(ks) | (set(tgt32) if n == P else set()))
    for k in allk:
        v = sp.expand(tab.get((n, k), sp.Integer(0)))
        if n == P:
            v = sp.expand(v - tgt32.get(k, 0))
        raw.append((f"a{n}_pi{k}", v))

elig = set(k2free) | set(hfree)
residual, subs, pivots, zeros = qstar_reduce(raw, elig)

free_after = sorted(elig - set(subs), key=str)
pt = {s: sp.Integer(0) for s in free_after}
pt[jet1] = sp.Integer(1)
pt[jet2] = sp.Integer(1)
pt[c] = sp.Integer(1)
full = dict(subs)
for _ in range(4):
    full = {v: sp.expand(sp.together(r).subs(pt)) for v, r in full.items()}
full.update(pt)
resolve_map(full)

k2pt = {}
for kq, v in k2.items():
    img = sp.expand(v.subs(full)) if getattr(v, "free_symbols", set()) else v
    if img != 0:
        k2pt[kq] = img

tabw = local_rows(k2pt, P, False)
tabw = {
    kk: sp.expand(vv.subs({jet1: 1, jet2: 1, c: 1})) if hasattr(vv, "subs") else vv
    for kk, vv in tabw.items()
}
viol = [(n, k, str(v)[:60]) for (n, k), v in sorted(tabw.items()) if n < P and sp.expand(v) != 0]
a32 = sp.expand(sum(tabw.get((P, k), 0) * pi**k for k in range(0, 40)))
a32_ok = sp.expand(a32 - (pi**2 - 1)**4) == 0

# On Δ, KF = K2^3, KG = K2^2. Cube/square the specialized K2.
KF = tz_mul(tz_mul(k2pt, k2pt, 96), k2pt, 96)
KG = tz_mul(k2pt, k2pt, 64)
f_local = local_rows(KF, 96, False)
g_local = local_rows(KG, 64, False)

def eval_table(table):
    return {
        kk: sp.expand(vv.subs({jet1: 1, jet2: 1, c: 1})) if hasattr(vv, "subs") else vv
        for kk, vv in table.items()
    }

f_local = eval_table(f_local)
g_local = eval_table(g_local)

def scan(name, table, n):
    tags = raw_minor_support(name, False).get(n, ())
    old, new, old_nz = [], [], []
    for k in tags:
        raw_v = table.get((n, k), sp.Integer(0))
        if hasattr(raw_v, "subs"):
            raw_v = sp.expand(raw_v.subs(c, 1))
        fixed = pole_coeff(table, n, k, name)
        if hasattr(fixed, "subs"):
            fixed = sp.expand(fixed.subs(c, 1))
        old.append((int(k), str(raw_v)))
        new.append((int(k), str(fixed)))
        if sp.expand(raw_v) != 0:
            old_nz.append((int(k), str(sp.expand(raw_v))))
    new_all_zero = all(sp.expand(sp.sympify(v)) == 0 for _k, v in new)
    return {
        "n": n,
        "stage": n - 4,
        "n_tags": len(tags),
        "old_nonzero_at_witness": old_nz,
        "old_k0": str(table.get((n, 0), 0) if not hasattr(table.get((n, 0), 0), "subs")
                      else sp.expand(table.get((n, 0), 0).subs(c, 1))),
        "new_all_zero": new_all_zero,
        "new_nonzero": [(k, v) for k, v in new if sp.expand(sp.sympify(v)) != 0],
        "spurious_unit_k0_old_is_1": sp.expand(sp.sympify(
            table.get((n, 0), 0) if not hasattr(table.get((n, 0), 0), "subs")
            else table.get((n, 0), 0).subs(c, 1)
        ) - 1) == 0,
    }

Fscan = scan("F", f_local, 96)
Gscan = scan("G", g_local, 64)

# Polynomial identity on Δ_T: a_32 = (π²−c)^4 ⇒ F lead − p^12 ≡ 0.
ident_F = sp.expand(((pi**2 - c)**4)**3 - (pi**2 - c)**12) == 0
ident_G = sp.expand(((pi**2 - c)**4)**2 - (pi**2 - c)**8) == 0

# Leading row alone is not a unit: the patched rows vanish at the witness
# (a system of 0=0), while the old k=0 row is the constant 1.
out = {
    "h3_incidence_residual": len(resid0),
    "h2_only_rows": len(raw),
    "Qstar_pivots": len(pivots),
    "dependent_zero": zeros,
    "residual_rows": len(residual),
    "witness_violations_p_lt_32": viol,
    "witness_a32": str(sp.factor(a32)),
    "witness_a32_matches_(pi^2-1)^4": a32_ok,
    "localizer_c": str(full.get(c)),
    "leading_F": Fscan,
    "leading_G": Gscan,
    "poly_identity_F": ident_F,
    "poly_identity_G": ident_G,
    "stage_spec_F92_pole": stage_spec(92)["pole_local_power"],
    "stage_spec_G60_pole": stage_spec(60)["pole_local_power"],
    "leading_row_alone_is_unit_OLD": Fscan["spurious_unit_k0_old_is_1"]
    or Gscan["spurious_unit_k0_old_is_1"],
    "leading_row_alone_is_unit_NEW": (not Fscan["new_all_zero"]) or (not Gscan["new_all_zero"]),
    "NEW_leading_rows_satisfied_on_Delta_witness": Fscan["new_all_zero"] and Gscan["new_all_zero"],
    "secs": round(time.monotonic() - t0, 1),
}
(HERE / "ctl_b_d108_leading.json").write_text(json.dumps(out, indent=2, default=str) + "\n")
ok = (
    a32_ok
    and not viol
    and Fscan["new_all_zero"]
    and Gscan["new_all_zero"]
    and Fscan["spurious_unit_k0_old_is_1"]
    and Gscan["spurious_unit_k0_old_is_1"]
    and ident_F and ident_G
    and out["stage_spec_F92_pole"] == 96
    and out["stage_spec_G60_pole"] == 64
    and not out["leading_row_alone_is_unit_NEW"]
)
print(json.dumps(out, indent=2, default=str))
print("CTL_B_OK" if ok else "CTL_B_FAIL")
sys.exit(0 if ok else 1)
