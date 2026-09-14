#!/usr/bin/env python3
"""Read-only exact checks of the three hash-bound semantic source maps.

Only the adjacent JSON result is written. No full polynomial expansion or
imports of campaign emitters are used. Run with python3 -B.
"""
import hashlib
import json
import re
from pathlib import Path

import sympy as S

ROOT = Path(__file__).resolve().parents[2]
PI = S.Symbol("pi")
SPECS = [
    ("99-delta2", "box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json",
     "778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea", 33, 3, 4, 96, 8),
    ("99-delta52", "box/char-degree-20260905/active-gauge/inputs/delta52_stage8.strongest.json",
     "3f81dc99770d235099249a818a55b19f0c828d36109e30aa738995177f97dc46", 33, 3, 4, 96, 8),
    ("108-free-mean", "box/char-degree-20260905/d108/selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json",
     "1c927d83aa4684ae91bfffc8d03500fbabb73a500faa222fa349a6d129a10814", 36, 4, 5, 140, 7),
]


def string_table(text):
    depth = start = 0
    pieces = []
    for i, ch in enumerate(text):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif ch == "+" and depth == 0:
            pieces.append(text[start:i])
            start = i + 1
    pieces.append(text[start:])
    assert depth == 0
    rows = []
    for piece in pieces:
        match = re.fullmatch(r"\((.*)\)\*tt\^(\d+)\*zz\^(\d+)", piece)
        assert match, piece
        expression, r, z = match.groups()
        rows.append((int(r), int(z), expression))
    return rows


def run():
    out = {
        "schema": "T2T3_MAJOR_D2_SOURCE_MAP_AUDIT/v1",
        "field": "Q with symbolic semantic parameters",
        "normalization": "t=1/x; z=ty-1; h=K_h2, D=K_B2, C=K_A3",
        "physical_reconstruction": {
            "F": "h_phys^3+(3*D_phys+target_a)*h_phys/2+C_phys",
            "G": "h_phys^2-target_b*h_phys/3+D_phys",
        },
        "normalized_reconstruction": {
            "KF": "h^3+3*t*D*h/2+target_a*t^(2*k)*h/2+t*C",
            "KG": "h^2-target_b*t^k*h/3+t*D",
        },
        "reconstruction_source": "box/char-degree-20260905/source-audit.md:377-415; 99 input degree_premap",
        "cases": [],
    }
    for tag, rel, expected_sha, k, wt, wz, hweight, hp in SPECS:
        path = ROOT / rel
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == expected_sha, (tag, digest)
        data = json.loads(raw)
        if tag.startswith("99"):
            maps = {key: value for key, value in data["maps"].items()}
            norm_bounds = {"h3": 11, "C2": 22, "C3": 33, "B2": 65, "A3": 98}
            assert data["degree_premap"]["A2c_65_0"] == "3*B2c_65_0/2 + target_a/2"
            assert data["degree_premap"]["B1c_32_0"] == "-target_b/3"
        else:
            maps = {key: string_table(data[value]) for key, value in
                    [("h", "h_expr"), ("B2", "D_expr"), ("A3", "C_expr")]}
            norm_bounds = {"h": 36, "B2": 71, "A3": 107}
        for key, rows in maps.items():
            assert len({(r, z) for r, z, _ in rows}) == len(rows)
            assert all(r >= 0 and z >= 0 and r + z <= norm_bounds[key] for r, z, _ in rows)

        def weight(row):
            r, z, _ = row
            return wt * r + wz * z

        def face(key, level):
            return S.Add(*(S.sympify(e) * PI**z for r, z, e in maps[key]
                           if wt * r + wz * z == level))

        def top(key):
            return S.Add(*(S.sympify(e) * PI**z for r, z, e in maps[key] if r == 0))

        minima = {key: min(map(weight, rows)) for key, rows in maps.items()}
        faces = {key: face(key, minima[key]) for key in maps}
        if tag.startswith("99"):
            assert minima["h3"] * 3 == hweight
            assert minima["C2"] + minima["h3"] == hweight
            assert minima["C3"] == hweight
            hface = S.expand(faces["h3"]**3 + faces["C2"] * faces["h3"] + faces["C3"])
            htop = S.expand(top("h3")**3 + top("C2") * top("h3") + top("C3"))
            expected_top = PI**24 * (1 + PI)**9
        else:
            assert minima["h"] == hweight
            hface = S.expand(faces["h"])
            htop = S.expand(top("h"))
            expected_top = PI**28 * (1 + PI)**8
        target = (PI**wt - 1)**hp
        assert S.expand(hface - target) == 0
        assert S.expand(htop - expected_top) == 0
        assert hface != 0
        fcor = {"3*t*D*h/2": wt + minima["B2"] + hweight,
                "target_a*t^(2*k)*h/2": wt * 2 * k + hweight,
                "t*C": wt + minima["A3"]}
        gcor = {"-target_b*t^k*h/3": wt * k + hweight,
                "t*D": wt + minima["B2"]}
        assert all(value > 3 * hweight for value in fcor.values())
        assert all(value > 2 * hweight for value in gcor.values())
        assert all(z < k for key in ["B2", "A3"] for r, z, e in maps[key])
        out["cases"].append({
            "case": tag, "input": rel, "input_sha256": digest,
            "weight": [wt, wz], "map_row_counts": {key: len(rows) for key, rows in maps.items()},
            "normalized_polynomial_support_checks": True,
            "map_minimum_weights": minima,
            "map_leading_faces": {key: str(S.expand(value)) for key, value in faces.items()},
            "h_exact_weight": hweight, "h_exact_face": str(hface),
            "h_face_target": str(target), "h_face_exact_match": True,
            "h_t0_top_exact_match": True, "h_t0_top": str(expected_top),
            "F_leading_weight": 3 * hweight, "G_leading_weight": 2 * hweight,
            "F_correction_weight_lower_bounds": fcor,
            "G_correction_weight_lower_bounds": gcor,
            "all_corrections_strictly_above_leading_weight": True,
            "F_actual_major_face": f"(pi^{wt}-1)^{3*hp}",
            "G_actual_major_face": f"(pi^{wt}-1)^{2*hp}",
            "F_physical_cover_valuation": 3 * hweight - wt * 3 * k,
            "G_physical_cover_valuation": 2 * hweight - wt * 2 * k,
            "source_residual_rows_needed_for_major_face_check": False,
        })
    result = Path(__file__).with_suffix(".json")
    result.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "cases": len(out["cases"]),
                      "output": str(result), "bytes": result.stat().st_size}))


if __name__ == "__main__":
    run()
