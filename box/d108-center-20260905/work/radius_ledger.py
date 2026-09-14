#!/usr/bin/env python3
"""Def 5.1(3) radius ledger for the D=108 and (99,66) D1/D2 generic points,
plus an exact rational witness for the D=108 delta=3 stage-0 incidence block
at the Def 5.1(3) D2 radius."""
import importlib.util, json
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

spec = importlib.util.spec_from_file_location("skel", "box/moh14-20260905/moh_skeleton_full.py")
sk = importlib.util.module_from_spec(spec); spec.loader.exec_module(sk)
OUT = Path("box/d108-center-20260905/work")

def ledger(name, n, m, Ms, V, degK3, degK2, engine):
    S = sk.Skel(n, m, list(Ms), V)
    d = {i: S.d[i] for i in range(1, S.s + 2)}
    delta = {i: S.delta[i] for i in range(1, S.s + 1)}
    # z = w-1 = t*y-1 ; ord_t(z1-z2) = 1 + ord_t(y1-y2) = 1 + delta_i
    zrad = {i: 1 + delta[i] for i in range(1, S.s + 1)}
    ram2, ram1 = zrad[2].denominator, zrad[1].denominator
    # ord of K3 at the D2 generic point: roots of K3 in D2 = V_3 (Def 5.1(1)),
    # the remaining degK3-V_3 roots sit at distance delta_s.
    v3 = V[3]
    ordK3 = degK3 + v3 * delta[2] + (degK3 - v3) * delta[S.s]
    # K2 D2-face degree in pi and the multiplicity forced by V_2 (D1 packet)
    faceK2 = (degK2 // degK3) * v3
    rec = {"row": {"n": n, "m": m, "M": list(Ms), "V": {str(k): v for k, v in V.items()},
                   "d": [d[i] for i in range(1, S.s + 2)],
                   "delta": {str(i): str(delta[i]) for i in delta}},
           "z_radius_1_plus_delta": {str(i): str(zrad[i]) for i in zrad},
           "uniformizers": {"D2": f"t = s^{ram2}, z = pi*s^{int(zrad[2]*ram2)}",
                            "D1": f"t = e^{ram1}, z = ...+ Pi*e^{int(zrad[1]*ram1)}"},
           "D2_weight_source": f"{ram2}*r + {int(zrad[2]*ram2)}*q",
           "D2_weight_engine": engine["D2_weight"],
           "D1_engine": engine["D1"],
           "ord_t_K3_at_D2": str(ordK3), "K3_D2_face_weight_source": str(ordK3 * ram2),
           "K3_D2_face_weight_engine": engine["K3_face_weight"],
           "K2_D2_face_degree_in_pi": faceK2,
           "K2_D2_face_multiplicity_forced_by_V2": V[2],
           "MATCH": engine["D2_weight"] == f"{ram2}*r + {int(zrad[2]*ram2)}*q"}
    return rec

d108 = ledger("D108", 108, 72, [81, 106], {2: 7, 3: 7}, 9, 36,
              {"D2_weight": "4*r + 6*q", "D1": "t=e^8, z=e^12*(1+Pi*e)", "K3_face_weight": 42})
g9966 = ledger("G9966", 99, 66, [77, 97], {2: 8, 3: 8}, 11, 33,
               {"D2_weight": "3*r + 4*q", "D1": "t=e^9, z=e^12+Pi*e^13", "K3_face_weight": 32})

# --- exact rational witness of the D=108 delta=3 stage-0 incidence block -----
t, z, pi, s = sp.symbols("t z pi s")
K3 = z**7 * (1 + z)**2 - t**8 * z                    # Hc_8_1 = -1, all others 0
major = sp.expand(K3.subs({t: s**4, z: pi * s**5}))  # Def 5.1(3) D2 generic point
minor = sp.expand(K3.subs(z, pi * t**4 - 1))         # jet0=jet1=jet2=0, w = pi*t^4
ord_major = min(m[0] for m in sp.Poly(major, s).monoms())
resid = sp.expand(minor - (-t**8 * (pi**2 - 1)))
ord_resid = min(m[0] for m in sp.Poly(resid, t).monoms())
witness = {"K3": str(K3),
           "chart_coordinates": {"Hc_8_1": -1, "all_other_lower": 0},
           "D2_weight_of_t8z": 4 * 8 + 5 * 1,
           "D2_floor_source": "4*r+5*q >= 35 (face weight), strict variant 36",
           "in_chart_at_cutoff_35_and_36": True,
           "ord_s_at_D2_generic_point": int(ord_major),
           "leading_D2_face": str(sp.LT(sp.Poly(major, s).as_expr(), s)),
           "minor_image": str(sp.expand(minor)),
           "target": "-t^8*(pi^2-c) + O(t^9) with c = 1",
           "residual_after_target_ord_t": int(ord_resid),
           "localization_c": 1, "c_nonzero": True,
           "claim": "rational point of the NECESSARY common-h3 incidence block "
                    "at the Def 5.1(3) D2 radius; NOT a claim of a Jacobian pair"}
assert ord_major == 35 and ord_resid >= 9

payload = {"D108": d108, "G9966_delta2_and_delta52_major_block": g9966, "witness_D108": witness}
(OUT / "radius-ledger.json").write_text(json.dumps(payload, indent=2) + "\n")
print(json.dumps(payload, indent=2))
