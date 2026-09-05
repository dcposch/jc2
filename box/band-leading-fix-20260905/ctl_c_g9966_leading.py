#!/usr/bin/env python3
"""CONTROL (c): (99,66) δ=2 corrected engine at its leading stage.

Rebuild the gate's h2-only Δ-witness (cvg_t5: a_p=0 for p<27,
a_27=(ζ²(ζ+3ρ))^3). On Δ with ord_t K2 = 27 exactly, the leading F/G
coefficients are a_27^3 / a_27^2 (no lower-power cross terms). Those
are the engine table entries at n=81/54; after the patch they subtract
(ζ²(ζ+3ρ))^9 / ^6. Direct substitution of the witness must annihilate
every tagged leading row; the old emission is a nonzero constant
(spurious UNIT at stage 77/50).
"""
from __future__ import annotations

import importlib.util
import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "cfe", HERE.parent / "g9966-repair-gate-20260905" / "corrected_face_engine.py"
)
E = importlib.util.module_from_spec(spec)
sys.modules["cfe"] = E
spec.loader.exec_module(E)

def log(msg):
    print(msg, flush=True)


t0 = time.monotonic()
P, branch = 27, "delta2"
zeta, rho = sp.symbols("zeta rho")
jet0 = sp.Symbol("jet0")

log(f"[c] build_major_h2({branch}, {P})")
k2, inner_free, _ = E.build_major_h2(branch, P)
log(f"[c] local_rows K2, {len(k2)} slots")
tab = E.local_rows(k2, branch, P)
lead3 = zeta**2 * (zeta + 3 * rho)
tgt_poly = sp.expand(lead3**3)
tgt = {k: sp.expand(tgt_poly.coeff(zeta, k)) for k in range(0, 28)}

rows = []
for n in range(1, P + 1):
    ks = sorted({k for (m, k) in tab if m == n})
    allk = sorted(set(ks) | (set(tgt) if n == P else set()))
    for k in allk:
        v = sp.expand(tab.get((n, k), sp.Integer(0)))
        if n == P:
            v = sp.expand(v - tgt.get(k, 0))
        rows.append((f"a{n}_z{k}", v))

loc = sp.Symbol("rho")
elig = set(inner_free) - {loc}
log(f"[c] qstar_reduce {len(rows)} h2-only rows, eligible={len(elig)}")
residual, subs, pivots, zeros = E.qstar_reduce(rows, elig)
log(f"[c] pivots={len(pivots)} zeros={zeros} residual={len(residual)}")

free_after = sorted(elig - set(subs), key=str)
pt = {s: sp.Integer(0) for s in free_after}
pt[loc] = sp.Integer(1)
if jet0 in pt:
    pt[jet0] = sp.Integer(1)
full = dict(subs)
for _ in range(4):
    full = {v: sp.expand(sp.together(r).subs(pt)) for v, r in full.items()}
full.update(pt)
E.resolve_map(full)

k2pt = {}
for kq, v in k2.items():
    img = sp.expand(v.subs(full)) if getattr(v, "free_symbols", set()) else v
    if img != 0:
        k2pt[kq] = img

log(f"[c] specialized K2 slots={len(k2pt)}; local_rows at {P}")
# Fable's Δ-witness (and cvg_t5) is the minor arc with u=0, jet0=1, ρ=1.
# `u` is the local_rows dummy for the t^2 coefficient, not a Q* pivot.
u = sp.Symbol("u")
arc = {jet0: 1, u: 0, rho: 1}
tabw = E.local_rows(k2pt, branch, P)
tabw = {
    kk: sp.expand(vv.subs(arc)) if hasattr(vv, "subs") else vv
    for kk, vv in tabw.items()
}
viol = [(n, k, str(v)[:60]) for (n, k), v in sorted(tabw.items()) if n < P and sp.expand(v) != 0]
a27 = sp.expand(sum(tabw.get((P, k), 0) * zeta**k for k in range(0, 40)))
want = sp.expand((zeta**2 * (zeta + 3))**3)
a27_ok = sp.expand(a27 - want) == 0
log(f"[c] a27_ok={a27_ok} viol_below={len(viol)}")

# On Δ with ord_t K2 = 27, KF lead = a27^3 and KG lead = a27^2.
# Feeding those coefficients through pole_coeff is the engine emission
# of the leading row (the TZ-cube of the full series is the same
# polynomial and is not needed to read the leading tag).
Flead = sp.expand(a27**3)
Glead = sp.expand(a27**2)
f_table = {(81, k): sp.expand(Flead.coeff(zeta, k)) for k in range(0, 28)}
g_table = {(54, k): sp.expand(Glead.coeff(zeta, k)) for k in range(0, 19)}


def scan(name, table, n, var=zeta):
    tags = E.raw_minor_support(branch, name).get(n, ())
    old_nz, new_nz, const_old = [], [], []
    for k in tags:
        raw_v = table.get((n, k), sp.Integer(0))
        if hasattr(raw_v, "subs"):
            raw_v = sp.expand(raw_v.subs(rho, 1))
        raw_v = sp.expand(raw_v)
        fixed = E.pole_coeff(table, n, k, branch, name)
        if hasattr(fixed, "subs"):
            fixed = sp.expand(fixed.subs(rho, 1))
        fixed = sp.expand(fixed)
        if raw_v != 0:
            old_nz.append((int(k), str(raw_v)[:80]))
            if raw_v.is_number:
                const_old.append((int(k), str(raw_v)))
        if fixed != 0:
            new_nz.append((int(k), str(fixed)[:80]))
    k0 = table.get((n, 0), 0)
    if hasattr(k0, "subs"):
        k0 = sp.expand(k0.subs(rho, 1))
    return {
        "n": n,
        "stage": n - 4,
        "n_tags": len(tags),
        "old_nonzero_at_witness": old_nz,
        "old_k0": str(k0),
        "new_all_zero": not new_nz,
        "new_nonzero": new_nz,
        "old_constant_nonzero": const_old,
        "spurious_unit_from_old_constant": bool(const_old),
    }


Fscan = scan("F", f_table, 81)
Gscan = scan("G", g_table, 54)
ident_F = sp.expand((lead3**3)**3 - lead3**9) == 0
ident_G = sp.expand((lead3**3)**2 - lead3**6) == 0
stF = E.stage_spec(branch, 77)
stG = E.stage_spec(branch, 50)

out = {
    "branch": branch,
    "depth": P,
    "h2_only_rows": len(rows),
    "Qstar_pivots": len(pivots),
    "dependent_zero": zeros,
    "residual_rows": len(residual),
    "witness_violations_p_lt_27": viol,
    "witness_a27": str(sp.factor(a27)),
    "witness_a27_matches_(zeta^2*(zeta+3))^3": a27_ok,
    "localizer_rho": str(full.get(loc)),
    "leading_F": Fscan,
    "leading_G": Gscan,
    "poly_identity_F": ident_F,
    "poly_identity_G": ident_G,
    "stage_spec_F77_pole": stF["pole_local_power"],
    "stage_spec_G50_pole": stG["pole_local_power"],
    "leading_row_alone_is_unit_OLD": Fscan["spurious_unit_from_old_constant"]
    or Gscan["spurious_unit_from_old_constant"],
    "leading_row_alone_is_unit_NEW": (not Fscan["new_all_zero"]) or (not Gscan["new_all_zero"]),
    "NEW_leading_rows_satisfied_on_Delta_witness": Fscan["new_all_zero"] and Gscan["new_all_zero"],
    "secs": round(time.monotonic() - t0, 1),
}
(HERE / "ctl_c_g9966_leading.json").write_text(json.dumps(out, indent=2, default=str) + "\n")
ok = (
    a27_ok
    and not viol
    and Fscan["new_all_zero"]
    and Gscan["new_all_zero"]
    and out["leading_row_alone_is_unit_OLD"]
    and not out["leading_row_alone_is_unit_NEW"]
    and ident_F and ident_G
    and out["stage_spec_F77_pole"] == 81
    and out["stage_spec_G50_pole"] == 54
    and len(residual) == 0
)
print(json.dumps(out, indent=2, default=str), flush=True)
print("CTL_C_OK" if ok else "CTL_C_FAIL", flush=True)
sys.exit(0 if ok else 1)
