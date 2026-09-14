#!/usr/bin/env python3
"""Compact replay for the full-ideal counterexample gate (Fable, 2026-09-06).

Read-only checks: (A) exact T2 identity Q = Q_* + q with h,D,C symbolic;
(B) T3 recurrence monomial census and derivative degrees; (C) source-map
data checks on the three hash-bound frozen inputs named by build_direct.py.
Writes only replay_checks.json next to this file.  Run with python3 -B.
"""
import hashlib, json, re
from pathlib import Path
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
OUT = {"schema": "FULL_IDEAL_COUNTEREXAMPLE_GATE_REPLAY/v1"}

# (A) exact identity, physical coordinates, h,D,C as free symbols
h, D, C, a, b, c, d, e0 = S.symbols("h D C a b c d e0")
F = h**3 + (3*D + a)*h/2 + C
G = h**2 - b*h/3 + D
Q = G**3 - F**2 + a*G**2 + b*F*G + c*F + d*G + e0
H = h - b/6
v = D + a/3 + b**2/18
V = C - b*D/4 + (a*b/12 + b**3/54 - c/2)
U = S.Rational(8, 3)*V
Rraw = v**2 - U*H
p = d + b*c/2 - (a + b**2/4)**2/3
Qstar = (S.Rational(3, 4)*Rraw*H**2 - S.Rational(1, 8)*v*U*H + v*Rraw
         - S.Rational(9, 64)*U**2 + p*H**2 + p*v)
diff = S.expand(Q - Qstar)
OUT["identity"] = {
    "Q_minus_Qstar_free_of_h_D_C": not ({h, D, C} & diff.free_symbols),
    "q_scalar": str(diff),
    "h_adic_coeffs_h6_h5_h4": [str(S.Poly(S.expand(Q), h).coeff_monomial(h**k)) for k in (6, 5, 4)],
}

# (B) T3 recurrence census (disproof direction: passive monomials dropped)
census = {}
for (n, m, D2, n1, n2, D3) in [(99, 66, 55, 3, 3, 145), (108, 72, 63, 3, 4, 227)]:
    top = n2*D2; defect = top - D3
    mons = [(j, aa, bb, n*j + m*aa + D2*bb) for j in range(3) for aa in range(n1) for bb in range(n2)
            if n*j + m*aa + D2*bb <= top]
    eq = [x for x in mons if x[3] == top]
    active = [(x, top - x[3]) for x in mons if 0 < top - x[3] <= defect]
    passive = [x for x in mons if top - x[3] > defect]
    census[f"({n},{m})"] = {
        "n2*D2": top, "defect": defect, "equality_monomials_F^j_G^a_Q^b": eq,
        "active_with_depth": active, "passive_count": len(passive),
        "passive_max_degree": max(x[3] for x in passive), "D3": D3,
        "deg_B2": 2*m, "T2_bound_deg_j": n + D2 - 2 - 2*m,
        "deg_B3_leading_term": (n2 - 1)*D2 + 2*m, "n+D3-2": n + D3 - 2,
        "compressor_equality": (n2 - 1)*D2 + 2*m == n + D3 - 2,
    }
OUT["t3_census"] = census

# (C) source maps
SPECS = [("99-delta2", "box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json",
          "778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea", 33, 3, 4, 20),
         ("99-delta52", "box/char-degree-20260905/active-gauge/inputs/delta52_stage8.strongest.json",
          "3f81dc99770d235099249a818a55b19f0c828d36109e30aa738995177f97dc46", 33, 3, 4, 20),
         ("108-free-mean", "box/char-degree-20260905/d108/selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json",
          "1c927d83aa4684ae91bfffc8d03500fbabb73a500faa222fa349a6d129a10814", 36, 4, 5, 25)]
IDENT = re.compile(r"[A-Za-z_][A-Za-z_0-9]*")
PI = S.Symbol("pi")

def split_top(text):
    pieces, start, depth = [], 0, 0
    for i, ch in enumerate(text):
        if ch == "(": depth += 1
        elif ch == ")": depth -= 1
        elif ch == "+" and depth == 0:
            pieces.append(text[start:i]); start = i + 1
    pieces.append(text[start:]); return [q for q in pieces if q]

cases = []
for tag, rel, sha, k, wt, wz, defect in SPECS:
    raw = (ROOT / rel).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    assert digest == sha, (tag, digest)
    data = json.loads(raw)
    if tag.startswith("99"):
        names = list(data["full_free_coordinates"])
        maps = {key: [(int(r), int(z), e) for r, z, e in val] for key, val in data["maps"].items()}
        bounds = {"h3": 11, "C2": 22, "C3": 33, "B2": 65, "A3": 98}
    else:
        names = list(data["names"]); maps = {}
        for key, field in [("h", "h_expr"), ("B2", "D_expr"), ("A3", "C_expr")]:
            rows = []
            for piece in split_top(data[field]):
                mt = re.fullmatch(r"\((.*)\)\*tt\^(\d+)\*zz\^(\d+)", piece); assert mt
                e, r, z = mt.groups(); rows.append((int(r), int(z), e))
            maps[key] = rows
        bounds = {"h": 36, "B2": 71, "A3": 107}
    syms = {nm: S.Symbol(nm) for nm in names}
    rec = {"case": tag, "input": rel, "input_sha256": digest, "frozen_names": len(names),
           "target_e_in_names_and_rowless": "target_e" in names, "maps": {}}
    nonpoly = 0; unknown = set()
    for key, rows in maps.items():
        for _, _, e in rows:
            unknown |= set(IDENT.findall(e)) - set(names) - {"tt", "zz"}
            ex = S.sympify(e, locals=syms)
            if not ex.is_polynomial(*[syms[nm] for nm in names if nm in e]): nonpoly += 1
        rec["maps"][key] = {"rows": len(rows), "min_r": min(r for r, _, _ in rows),
                            "max_z": max(z for _, z, _ in rows),
                            "max_r_plus_z": max(r + z for r, z, _ in rows), "bound": bounds[key],
                            "support_ok": all(r >= 0 and z >= 0 and r + z <= bounds[key] for r, z, _ in rows),
                            "distinct_sites": len({(r, z) for r, z, _ in rows}) == len(rows)}
    rec["nonpolynomial_expressions"] = nonpoly; rec["unknown_symbols"] = sorted(unknown)
    def part(key, pred): return S.Add(*(S.sympify(e, locals=syms)*PI**z for r, z, e in maps[key] if pred(r, z)))
    if tag.startswith("99"):
        htop = S.expand(part("h3", lambda r, z: r == 0)**3 + part("C2", lambda r, z: r == 0)*part("h3", lambda r, z: r == 0) + part("C3", lambda r, z: r == 0))
        expected = S.expand(PI**24*(1 + PI)**9)
        hface = S.expand(part("h3", lambda r, z: wt*r + wz*z == 32)**3 + part("C2", lambda r, z: wt*r + wz*z == 64)*part("h3", lambda r, z: wt*r + wz*z == 32) + part("C3", lambda r, z: wt*r + wz*z == 96))
        target = S.expand((PI**3 - 1)**8)
    else:
        htop = S.expand(part("h", lambda r, z: r == 0)); expected = S.expand(PI**28*(1 + PI)**8)
        hface = S.expand(part("h", lambda r, z: wt*r + wz*z == 140)); target = S.expand((PI**4 - 1)**7)
    minD = rec["maps"]["B2"]["min_r"]; minC = rec["maps"]["A3"]["min_r"]
    rec.update({"h_top_row_numeric_match": S.expand(htop - expected) == 0, "h_top_row": str(htop),
                "h_major_face_match": S.expand(hface - target) == 0, "h_major_face_target": str(target),
                "min_weights": {key: min(wt*r + wz*z for r, z, _ in rows) for key, rows in maps.items()},
                "F_correction_min_depths": {"t*D*h": 1 + minD, "t*C": 1 + minC, "a*t^(2k)*h/2": 2*k},
                "G_correction_min_depths": {"b*t^k*h/3": k, "t*D": 1 + minD},
                "defect": defect, "corrections_exceed_defect": min(1 + minD, 1 + minC, k) > defect,
                "D_and_C_ydegree_below_k": rec["maps"]["B2"]["max_z"] < k and rec["maps"]["A3"]["max_z"] < k,
                "C_min_r_ge_1_for_U_shift": minC >= 1})
    cases.append(rec)
OUT["source_maps"] = cases
Path(__file__).with_name("replay_checks.json").write_text(json.dumps(OUT, indent=1, sort_keys=True, default=str) + "\n")
print(json.dumps({"status": "DONE", "identity_ok": OUT["identity"]["Q_minus_Qstar_free_of_h_D_C"],
                  "cases": [(x["case"], x["h_top_row_numeric_match"], x["h_major_face_match"], x["corrections_exceed_defect"], x["nonpolynomial_expressions"]) for x in cases]}))
