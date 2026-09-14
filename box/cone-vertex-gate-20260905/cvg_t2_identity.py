#!/usr/bin/env python3
"""GATE (1) deep: ENGINE's own build_FG + jacobian_band on Delta with the four
constants SWITCHED ON, at the t-powers where they act (36,72,108 +/-), with
generic-integer K2 and symbolic constants.  Plus two negative controls."""
import sys, json, time
sys.path.insert(0, "box/d108-rekill-20260905/work")
import sympy as sp
import rekill_engine as RE

t0 = time.monotonic()
out = {}
for (label, nF, nG, degh2) in [("D108", 108, 72, 36), ("G9966", 99, 66, 33)]:
    RE.N_F, RE.N_G = nF, nG
    MAXT = nF + 2
    k2 = {(0, 2*degh2-8): sp.Integer(1), (0, 2*degh2-7): sp.Integer(3),
          (1, 5): sp.Integer(-7), (2, 3): sp.Integer(5), (7, 11): sp.Integer(2),
          (degh2, 1): sp.Integer(-3), (degh2+5, 0): sp.Integer(11)}
    b, cp, d, e = sp.symbols("bb cp dd ee")
    specs = {"A2": nF-degh2-1, "A3": nF-1, "B1": nG-degh2-1, "B2": nG-1}
    outer = {"A2": {(specs["A2"],0): b}, "A3": {(specs["A3"],0): cp},
             "B1": {(specs["B1"],0): d}, "B2": {(specs["B2"],0): e}}
    KF, KG = RE.build_FG(k2, outer, MAXT)
    sites = {}
    for nm, K in (("KF",KF),("KG",KG)):
        for s in (b,cp,d,e):
            hits = sorted({r for (r,q),v in K.items() if s in v.free_symbols})
            if hits: sites[f"{nm}:{s}"] = hits[:3]
    probes = sorted({1,2,3,7,degh2-1,degh2,degh2+1,degh2+2,2*degh2,
                     nG-degh2, nG-degh2+1, nG-degh2+2, nG, nG+1, nG+2,
                     nF-degh2, nF-degh2+1, nF, nF+1, nF+2, MAXT})
    probes = [p for p in probes if 1 <= p <= MAXT]
    bad = []
    for tp in probes:
        J = RE.jacobian_band(KF, KG, tp)
        nz = {k: str(v)[:70] for k, v in J.items() if sp.expand(v) != 0}
        if nz: bad.append((tp, nz))
        print(f"  {label} tp={tp} nonzero={len(nz)}", flush=True)
    # CTRL A: one extra outer coordinate off Delta -> J must be nonzero somewhere
    outer_p = {k: dict(v) for k, v in outer.items()}
    outer_p["B1"][(0, 0)] = sp.Symbol("pert")
    KFp, KGp = RE.build_FG(k2, outer_p, 12)
    ctlA = [tp for tp in range(1, 13)
            if any(sp.expand(v)!=0 for v in RE.jacobian_band(KFp,KGp,tp).values())]
    # CTRL B: wrong degree pairing (m -> m-1) must FAIL to cancel on Delta
    RE.N_F, RE.N_G = nF, nG-1
    ctlB = [tp for tp in range(1, 13)
            if any(sp.expand(v)!=0 for v in RE.jacobian_band(KF,KG,tp).values())]
    RE.N_F, RE.N_G = nF, nG
    out[label] = {"n": nF, "m": nG, "degh2": degh2, "max_t": MAXT,
                  "constant_sites_in_KF_KG": sites, "probed_t_powers": probes,
                  "nonzero_J_bands_on_Delta": bad, "n_nonzero_probes": len(bad),
                  "CTRL_A_offDelta_nonzero_tp": ctlA[:6],
                  "CTRL_B_wrong_m_nonzero_tp": ctlB[:6]}
    print(label, "SITES", sites, flush=True)
    print(label, "nonzero probes:", len(bad), "| CTRL_A:", ctlA[:6], "| CTRL_B:", ctlB[:6], flush=True)
json.dump(out, open("box/cone-vertex-gate-20260905/t2_identity.json","w"), indent=1, default=str)
print("secs", round(time.monotonic()-t0,1))
