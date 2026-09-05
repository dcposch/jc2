#!/usr/bin/env python3
"""Step 3: the FULL staged joint elimination for the D=108 delta=3 split branch
at the Moh Def 5.1(3) D2 radius.  Stage schedule is the frozen charged
continuation_schedule(); the chart is the corrected one."""
import argparse, hashlib, json, subprocess, sys, time
from collections import defaultdict
from pathlib import Path
import sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
import rekill_engine as E
from rekill_engine import (SRC, FRZ, minor_incidence, qstar_reduce, symbol,
                           build_major_h2, substitute_map, outer_state, build_FG,
                           jacobian_band, local_rows, raw_minor_support, stage_spec,
                           pole_coeff, GAUGE_LEDGER)

OUT = Path(__file__).resolve().parent


def rows_hash(rows):
    return hashlib.sha256("".join(f"{l}\t{sp.srepr(sp.expand(v))}\n"
                                  for l, v in rows).encode()).hexdigest()


def singular_check(residual, tag, extra_localizations=()):
    """Exact-Q dimension + controls on the localized residual ideal."""
    if not residual:
        return {"unit_ideal": False, "dimension": None, "note": "empty residual",
                "wrapper_control": "not_needed"}
    exprs = [sp.expand(v) for _l, v in residual]
    variables = sorted(set().union(*(e.free_symbols for e in exprs)), key=str)
    c, Zc = symbol("c"), symbol("Zc")
    if c not in variables: variables.append(c); variables.sort(key=str)
    ring = variables + [Zc]
    def S(e): return str(e).replace("**", "^")
    gens = [S(e) for e in exprs] + [f"Zc*c-1"]
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
    (OUT / f"{tag}.sing").write_text(script)
    r = subprocess.run(["Singular", "-q"], input=script, text=True,
                       capture_output=True, timeout=3000)
    (OUT / f"{tag}.sing.out").write_text(r.stdout + "\n--STDERR--\n" + r.stderr)
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


def run(stage, jet0free, radius=SRC, tag=None):
    t0 = time.monotonic()
    tag = tag or f"joint_wz{radius.wz}_jet0{'free' if jet0free else 'pinned'}_stage{stage}"
    cutoff = radius.k3_face          # face RETAINED = the weakest sourced chart
    rows0, hvars, h3 = minor_incidence(radius, cutoff, jet0free)
    resid0, subs0, piv0, _z0 = qstar_reduce(rows0, hvars)
    h3r = {k: v for k, v in ((k, substitute_map(v, subs0)) for k, v in h3.items()) if v != 0}
    k2, k2free, k2meta = build_major_h2(radius, h3r, 40, jet0free)

    spec = stage_spec(stage)
    max_pole = max(stage_spec(i)["pole_local_power"] for i in range(stage + 1))
    max_j = max(stage_spec(i)["jacobian"]["t_power"] for i in range(stage + 1))
    max_t = max(max_pole, max_j, 3)
    outer, outer_free, outer_meta = outer_state(radius, stage)
    KF, KG = build_FG(k2, outer, max_t)

    f_local = local_rows(KF, max_pole, jet0free)
    g_local = local_rows(KG, max_pole, jet0free)
    rows, accounting = [], {"prior": {}, "stages": []}
    # The stage-0 common-h3 incidence residual is a necessary row set at
    # every stage; it is empty at the corrected radius and is the frozen kill
    # at the frozen radius, so it must be carried explicitly.
    rows += [(f"h3_incidence_{l}", v) for l, v in resid0]

    for name, table in (("F", f_local), ("G", g_local)):
        n_rows = 0
        for n in (1, 2, 3):
            tags = raw_minor_support(name, jet0free).get(n, ())
            assert tags, (name, n)
            for k in tags:
                rows.append((f"prior_{name}_local{n}_coord{k}", pole_coeff(table, n, k, name)))
                n_rows += 1
        accounting["prior"][name] = n_rows
    J1 = jacobian_band(KF, KG, 1)
    for k in range(15, 25):
        rows.append((f"prior_J_d177_k{k}", J1.get(k, sp.Integer(0))))
    accounting["prior"]["J177"] = 10

    for cur in range(stage + 1):
        sc = stage_spec(cur)
        n = sc["pole_local_power"]
        counts = {"stage": cur, "F": 0, "G": 0, "J": 0}
        for name, table in (("F", f_local), ("G", g_local)):
            for k in raw_minor_support(name, jet0free).get(n, ()):
                rows.append((f"stage{cur}_{name}_local{n}_coord{k}",
                             pole_coeff(table, n, k, name)))
                counts[name] += 1
        js = sc["jacobian"]
        J = jacobian_band(KF, KG, js["t_power"])
        for k in js["w_powers"]:
            rows.append((f"stage{cur}_J_d{js['degree']}_k{k}", J.get(k, sp.Integer(0))))
            counts["J"] += 1
        accounting["stages"].append(counts)

    free = set(k2free) | set(outer_free) | {v for v in hvars if v not in subs0}
    residual, subs, pivots, zeros = qstar_reduce(rows, free)
    sing = singular_check(residual, tag)
    rec = {"tag": tag, "radius": {"z_s_order": radius.wz, "weight": f"4*r+{radius.wz}*q",
                                  "K3_face": radius.k3_face, "K2_face": radius.k2_face,
                                  "K2_D1_leading_e_exponent": radius.k2_d1,
                                  "D1_line": f"s=e^2, t=e^8, z=e^{2*radius.k2_face//28*1 if False else radius.wz*2}*(1+Pi*e)"},
           "chart": {"h3_cutoff": cutoff, "jet0_free": jet0free,
                     "h3_stage0_pivots": len(piv0), "h3_stage0_residual": len(resid0),
                     "h3_free": [str(v) for v in hvars if v not in subs0],
                     "minor_free": (["jet0"] if jet0free else []) + ["jet1", "jet2", "c"]},
           "gauge_ledger": GAUGE_LEDGER,
           "major": {k: v for k, v in k2meta.items() if k != "K2_face_sites"},
           "K2_face_sites": k2meta["K2_face_sites"],
           "outer": outer_meta, "stage_spec": spec, "max_t": max_t,
           "row_accounting": accounting, "raw_row_count": len(rows),
           "rows_sha256": rows_hash(rows),
           "free_unknowns": len(free),
           "Qstar_pivots": len(pivots), "dependent_zero_rows": zeros,
           "residual_row_count": len(residual),
           "residual": {l: str(v) for l, v in residual},
           "residual_variables": sorted({str(s) for _l, v in residual
                                         for s in v.free_symbols}),
           "singular": sing,
           "wall_seconds": round(time.monotonic() - t0, 1)}
    (OUT / f"{tag}.json").write_text(json.dumps(rec, indent=2, default=str) + "\n")
    print(f"{tag}: rows={len(rows)} free={len(free)} piv={len(pivots)} zero={zeros} "
          f"resid={len(residual)} dim={sing.get('dimension')} "
          f"UNIT={sing.get('unit_ideal')} ({rec['wall_seconds']}s)", flush=True)
    return rec


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", type=int, required=True)
    ap.add_argument("--jet0free", action="store_true")
    ap.add_argument("--frozen-radius", action="store_true")
    a = ap.parse_args()
    run(a.stage, a.jet0free, FRZ if a.frozen_radius else SRC)
