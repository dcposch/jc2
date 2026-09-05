#!/usr/bin/env python3
"""Audit emitted s'=3 charts against the full Theorem-1.2 D1 inventory.

Writes box/moh14-charts-20260905/fullorder_audit.json.
Does not solve.  Prime marks are labels.
"""
from __future__ import annotations

import json
import sys
from math import floor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "orderbasis-20260903"))

import order_basis_full as OB
import sprime3_compiler as S


def jdefault(obj):
    from fractions import Fraction
    if isinstance(obj, Fraction):
        return S.qstr(obj)
    if isinstance(obj, Path):
        return str(obj)
    raise TypeError(type(obj))


def main() -> int:
    enum = S.enumerate_12()
    classes = []
    n_sub = 0
    n_full = 0
    for key in sorted(enum["classes"]):
        rows = enum["classes"][key]
        cid = S.class_id_of(key)
        fibres = []
        for r in rows:
            C = r["C"]
            vtag = "_".join(str(r["V"][i]) for i in range(2, r["s"] + 1))
            h = S.h_inventory_necessary(C)
            row_ob = OB.Row(key="t", label="t", n=C["n"], m=C["m"],
                            M2=r["M"][r["s"]], V2=C["V2"], k=C["ell"])
            h_ob = OB.h_inventory(row_ob, C)
            a_full = {i: S.coeff_inventory_necessary(C, i) for i in range(1, C["e"] + 1)}
            a_env = {i: S.coeff_inventory_envelope(C, i) for i in range(1, C["e"] + 1)}
            b_full = {i: S.coeff_inventory_necessary(C, i) for i in range(2, C["q"] + 1)}
            b_env = {i: S.coeff_inventory_envelope(C, i) for i in range(2, C["q"] + 1)}
            a_ob = {i: OB.coeff_inventory(C, i) for i in range(1, C["e"] + 1)}
            total_coker = r["envelope_cokernel"]["total_coker"]
            already = total_coker == 0
            if already:
                n_full += 1
            else:
                n_sub += 1
            am, bm, gauges, notes, audit = S.apply_gauges(C["e"], C["q"], a_full, b_full)
            nunk = (len(h) + sum(len(v) for v in am.values())
                    + sum(len(v) for v in bm.values()) + 1)
            fibres.append({
                "stem": "%s_V%s" % (cid, vtag),
                "V": {str(i): r["V"][i] for i in range(2, r["s"] + 1)},
                "delta1": S.qstr(C["delta1"]),
                "delta2": S.qstr(C["delta2"]),
                "delta_s": S.qstr(C["delta_s"]),
                "B_safe": S.qstr(C["B_safe"]),
                "B_tight": S.qstr(C["B_tight"]),
                "K": C["K"], "e": C["e"], "q": C["q"], "u": C["u"],
                "delta1_zero": C["delta1"] == 0,
                "delta2_zero": C["delta2"] == 0,
                "h_count": len(h),
                "h_ob_count": len(h_ob),
                "h_superset_of_ob": set(h_ob) <= set(h),
                "alpha_full_dims": [len(a_full[i]) for i in sorted(a_full)],
                "alpha_env_dims": [len(a_env[i]) for i in sorted(a_env)],
                "beta_full_dims": [len(b_full[i]) for i in sorted(b_full)],
                "beta_env_dims": [len(b_env[i]) for i in sorted(b_env)],
                "ob_coeff_equals_envelope": all(
                    set(a_ob[i]) == set(a_env[i]) for i in a_env),
                "envelope_coker_total": total_coker,
                "envelope_is_strict_subslice": total_coker > 0,
                "alpha_coker_sample": {
                    str(i): [list(m) for m in r["envelope_cokernel"]["alpha_omitted"][str(i)][:12]]
                    for i in a_full if r["envelope_cokernel"]["alpha_coker_dim"][str(i)]
                },
                "shear_scalar": audit["alpha_shear_scalar"],
                "shear_dim": audit["alpha_shear_dim"],
                "gauges": gauges,
                "nunk_full": nunk,
                "nunk_old_envelope": r["nunk"] if False else (
                    len(h) + sum(len(S.apply_gauges(C["e"], C["q"], a_env, b_env)[0][i])
                                 for i in a_env)
                    + sum(len(S.apply_gauges(C["e"], C["q"], a_env, b_env)[1][i])
                          for i in b_env) + 1
                ),
            })
        classes.append({
            "class_id": cid,
            "n_prime": key[0], "m_prime": key[1],
            "M_prime": list(key[2]), "ell": key[3], "s_prime": key[4],
            "fibre_size": len(rows),
            "any_strict_subslice": any(f["envelope_is_strict_subslice"] for f in fibres),
            "all_already_full": all(not f["envelope_is_strict_subslice"] for f in fibres),
            "fibres": fibres,
        })
    payload = {
        "n_live": enum["n_live"],
        "n_classes": len(classes),
        "fibres_already_full_thm12": n_full,
        "fibres_envelope_strict_subslice": n_sub,
        "diagnosis": (
            "The tot-degree cut r+s <= jK in order_basis_full.coeff_inventory "
            "(the 17(nnnnn) 'full' envelope) is a strict sub-slice of the "
            "Theorem-1.2 order-allowed D1 inventory on some fibres.  The "
            "sprime3 emitter now drops that cut.  Shear is omitted on all 12 "
            "(alpha_{e-q} is never scalar).  None of the 12 has delta1'=0; "
            "the zero-slope centre-support is the same loop (r <= -j B)."
        ),
        "classes": classes,
    }
    out = HERE / "fullorder_audit.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True, default=jdefault) + "\n")
    print("WROTE", out)
    print("already_full", n_full, "strict_subslice", n_sub)
    for c in classes:
        flag = "SUBSLICE" if c["any_strict_subslice"] else "ALREADY_FULL"
        print(" ", c["class_id"], flag, "fibres", c["fibre_size"])
        for f in c["fibres"]:
            print("    %s coker=%d nunk_full=%d shear_sc=%s d1=%s" % (
                f["stem"], f["envelope_coker_total"], f["nunk_full"],
                f["shear_scalar"], f["delta1"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
