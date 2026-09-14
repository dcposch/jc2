#!/usr/bin/env python3
"""Emit the four frozen GI70 long-solve jobs and their custody metadata."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "box/gi70-longsolve-20260905"
CLASS = "C_n24m16_Mm12_m2_5_ell1_s4"
STEM = CLASS + "_G"
SOURCE = ROOT / "box/gi-only-20260905/classes" / CLASS
ROWS = SOURCE / "rows" / f"{STEM}_rows.tsv"
META = SOURCE / "meta" / f"{STEM}.json"

# Exact N^2 degrees in the metadata variable order.  The scalar wp degree is
# the positive functional (b,d) -> 17*b+d; hence every coefficient row stays
# homogeneous, while the Rabinowitsch relation lives in its own dp block.
X_CHARGE = (
    0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
    0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
    0,1,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,1,2,
    0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,2,
)
Y_DEFICIT = (
    1,2,3,4,5,6,7,8, 1,2,3,4,5,6,7,8,
    9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,
    17,17,18,18,18,19,19,19,20,20,20,21,21,21,22,22,22,23,23,23,24,24,
    9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,39,
)


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def write(path: Path, text: str, executable: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    if executable:
        path.chmod(0o755)


def term_count(poly: str) -> int:
    # Rows are fully expanded and contain no negative exponents.
    return poly.count("+") + poly.count("-") + (0 if poly.startswith("-") else 1)


def singular_ring(characteristic: int, variables: list[str], weights: list[int]) -> str:
    return f"ring r={characteristic},({','.join(variables)}),wp({','.join(map(str, weights))});"


def ideal_text(name: str, rows: list[str]) -> str:
    return f"ideal {name}=\n" + ",\n".join(rows) + ";\n"


def sat_prelude(characteristic: int, variables: list[str], weights: list[int], rows: list[str]) -> str:
    return "\n".join([
        'LIB "elim.lib";',
        singular_ring(characteristic, variables, weights),
        "option(redSB);",
        f'int EXPECT_NVARS=70; if (nvars(basering)!=EXPECT_NVARS) {{ ERROR("ring arity mismatch"); }}',
        ideal_text("I", rows).rstrip(),
        'list GG_SAT_RAW=sat(I,ideal(c));',
        'if (size(GG_SAT_RAW)!=1) { ERROR("sat wrapper size mismatch"); }',
        'if (typeof(GG_SAT_RAW[1])!="ideal") { ERROR("sat component is not ideal"); }',
        'ideal S=GG_SAT_RAW[1];',
        'print("GG__SAT_COMPONENT ideal ring_nvars="+string(nvars(basering)));',
        'list GG_POS_RAW=sat(ideal(c),ideal(c));',
        'if (size(GG_POS_RAW)!=1 or typeof(GG_POS_RAW[1])!="ideal") { ERROR("sat positive wrapper"); }',
        'ideal GG_POS=GG_POS_RAW[1];',
        'int GG_POS_OK=(reduce(1,std(GG_POS))==0);',
        'print("GG__SAT_POS_CONTROL "+string(GG_POS_OK));',
        'list GG_NEG_RAW=sat(ideal(c*h_0_7),ideal(c));',
        'if (size(GG_NEG_RAW)!=1 or typeof(GG_NEG_RAW[1])!="ideal") { ERROR("sat negative wrapper"); }',
        'ideal GG_NEG=GG_NEG_RAW[1];',
        'ideal GG_NEG_G=std(GG_NEG);',
        'int GG_NEG_OK=(reduce(h_0_7,GG_NEG_G)==0 and reduce(1,GG_NEG_G)!=0);',
        'print("GG__SAT_NEG_CONTROL "+string(GG_NEG_OK));',
        'if (GG_POS_OK!=1 or GG_NEG_OK!=1) { ERROR("sat controls failed"); }',
        '',
    ])


def main() -> None:
    meta = json.loads(META.read_text(encoding="utf-8"))
    variables = list(meta["variables"])
    assert len(variables) == len(X_CHARGE) == len(Y_DEFICIT) == 70
    assert variables[-1] == "c" and meta["equations"] == 66
    weights = [17 * b + d for b, d in zip(X_CHARGE, Y_DEFICIT)]
    with ROWS.open(encoding="utf-8", newline="") as fh:
        records = list(csv.DictReader(fh, delimiter="|"))
    assert [int(r["source_index"]) for r in records] == list(range(66))
    rows = [r["expr"] for r in records]
    assert sum("c" in re.findall(r"[A-Za-z_][A-Za-z_0-9]*", f) for f in rows) == 1
    assert rows[22].endswith("-c")
    terms = sum(term_count(f) for f in rows)
    assert terms == 65990

    # (a) Exact Q, Rabinowitsch variable in a separate block; coefficient rows
    # retain their positive homogeneous wp block.
    a = [
        "// exact-Q chart: 70 coefficient variables plus Rabinowitsch T",
        "// wp scalarizes the exact bidegree by (b,d) -> 17*b+d",
        f"ring r=0,(T,{','.join(variables)}),(dp(1),wp({','.join(map(str, weights))}));",
        "option(redSB);",
        'print("GI70_A_RING nvars="+string(nvars(basering)));',
        'ideal CTRL_UNIT=c,T*c-1; ideal CTRL_UNIT_G=std(CTRL_UNIT);',
        'ideal CTRL_NONUNIT=c-1,T*c-1; ideal CTRL_NONUNIT_G=std(CTRL_NONUNIT);',
        'print("GI70_A_CTRL_UNIT "+string(reduce(1,CTRL_UNIT_G)==0));',
        'print("GI70_A_CTRL_NONUNIT "+string(reduce(1,CTRL_NONUNIT_G)!=0));',
        ideal_text("I", rows + ["T*c-1"]).rstrip(),
        'print("GI70_A_STD_BEGIN"); timer=1; int START=timer;',
        "ideal G=std(I);",
        'print("GI70_A_STD_SECONDS "+string(timer-START));',
        'int UNIT=(reduce(1,G)==0);',
        'print("GI70_A_UNIT "+string(UNIT));',
        'print("GI70_A_BASIS_SIZE "+string(size(G)));',
        'print("GI70_A_DIM "+string(dim(G)));',
        'if (UNIT==0) { print("GI70_A_MULT "+string(mult(G))); write("results/a_exact_std/basis.txt",G); }',
        'if (UNIT==1) {',
        '  matrix LIG=lift(I,G); matrix LG1=lift(G,ideal(1)); matrix LI1=LIG*LG1;',
        '  matrix IA[1][size(I)]=I; matrix VV=IA*LI1; poly VERIFY=VV[1,1]-1;',
        '  print("GI70_A_IDENTITY_VERIFIED "+string(VERIFY==0));',
        '  write("results/a_exact_std/original_ring_identity_matrix.txt",LI1);',
        '}',
        'print("GI70_A_DONE"); quit;',
        "",
    ]
    write(OUT / "inputs/a_exact_std.sing", "\n".join(a))

    # (d) Exact c=1 torus section.  c is token-substituted, never substring
    # replaced, and T is absent.
    section_vars = variables[:-1]
    token = re.compile(r"\b(?:" + "|".join(map(re.escape, sorted(variables, key=len, reverse=True))) + r")\b")
    rows_c1 = [token.sub(lambda m: "1" if m.group(0) == "c" else m.group(0), f) for f in rows]
    d = [
        "// exact-Q c=1 section; cone lemma identifies its unit test with c-saturation",
        f"ring r=0,({','.join(section_vars)}),dp;",
        "option(redSB);",
        'print("GI70_D_RING nvars="+string(nvars(basering)));',
        'ideal CTRL_UNIT=h_0_7,1-h_0_7; ideal CTRL_UNIT_G=slimgb(CTRL_UNIT);',
        'ideal CTRL_NONUNIT=h_0_7; ideal CTRL_NONUNIT_G=slimgb(CTRL_NONUNIT);',
        'print("GI70_D_CTRL_UNIT "+string(reduce(1,CTRL_UNIT_G)==0));',
        'print("GI70_D_CTRL_NONUNIT "+string(reduce(1,CTRL_NONUNIT_G)!=0));',
        ideal_text("I", rows_c1).rstrip(),
        'print("GI70_D_SLIMGB_BEGIN"); timer=1; int START=timer;',
        "ideal G=slimgb(I);",
        'print("GI70_D_SLIMGB_SECONDS "+string(timer-START));',
        'int UNIT=(reduce(1,G)==0);',
        'print("GI70_D_UNIT "+string(UNIT));',
        'print("GI70_D_BASIS_SIZE "+string(size(G)));',
        'print("GI70_D_DIM "+string(dim(G)));',
        'if (UNIT==0) { print("GI70_D_MULT "+string(mult(G))); write("results/d_c1_slimgb/basis.txt",G); }',
        'if (UNIT==1) {',
        '  matrix LIG=lift(I,G); matrix LG1=lift(G,ideal(1)); matrix LI1=LIG*LG1;',
        '  matrix IA[1][size(I)]=I; matrix VV=IA*LI1; poly VERIFY=VV[1,1]-1;',
        '  print("GI70_D_C1_IDENTITY_VERIFIED "+string(VERIFY==0));',
        '  write("results/d_c1_slimgb/c1_identity_matrix.txt",LI1);',
        '}',
        'print("GI70_D_DONE"); quit;',
        "",
    ]
    write(OUT / "inputs/d_c1_slimgb.sing", "\n".join(d))

    # (c) Fully expanded msolve section with a bijective safe-name map.
    safe = {name: f"v{i+1}" for i, name in enumerate(section_vars)}
    section_token = re.compile(r"\b(?:" + "|".join(map(re.escape, sorted(section_vars, key=len, reverse=True))) + r")\b")
    rows_ms = [section_token.sub(lambda m: safe[m.group(0)], f) for f in rows_c1]
    assert not any("(" in f or ")" in f or "/" in f for f in rows_ms)
    ms_lines = [",".join(safe[v] for v in section_vars), "1073741827"]
    ms_lines += [f + ("," if i + 1 < len(rows_ms) else "") for i, f in enumerate(rows_ms)]
    write(OUT / "inputs/c_c1_p1073741827.ms", "\n".join(ms_lines) + "\n")
    write(OUT / "inputs/c_variable_map.json", json.dumps({
        "direction": "source coefficient name -> msolve safe name",
        "source_ring_characteristic": 0,
        "target_characteristic": 1073741827,
        "specialization": {"c": "1", "T": "dropped"},
        "map": safe,
    }, indent=2, sort_keys=True) + "\n")

    guard = {
        "variables": 69,
        "generators": 66,
        "expanded_terms": terms,
        "exponent_slots": terms * 69,
        "signed_int32_max": 2_147_483_647,
        "passes_signed_int32_guard": terms * 69 <= 2_147_483_647,
        "margin_ratio": 2_147_483_647 / (terms * 69),
        "parenthesized_subexpressions": False,
    }
    write(OUT / "inputs/c_guard_expected.json", json.dumps(guard, indent=2, sort_keys=True) + "\n")

    # (b) First compute the modular Hilbert numerator of the homogeneous
    # saturation, then use the frozen helper's Hilbert-driven std at two fresh
    # primes in parallel.  It remains a modular screen: no unit promotion.
    prelude_template = sat_prelude(0, variables, weights, rows).replace("ring r=0,", "ring r=__PRIME__,", 1)
    write(OUT / "inputs/b_sat_prelude.template.sing", prelude_template)
    seed = prelude_template.replace("__PRIME__", "32003") + "\n" + "\n".join([
        'print("GI70_B_HILB_STD_BEGIN"); timer=1; int START=timer;',
        'ideal HG=std(S);',
        'print("GI70_B_HILB_STD_SECONDS "+string(timer-START));',
        f'intvec HW={','.join(map(str, weights))};',
        'intvec HNUM=hilb(HG,1,HW);',
        'print("GI70_B_HNUM_BEGIN"); print(string(HNUM)); print("GI70_B_HNUM_END");',
        'print("GI70_B_SEED_UNIT "+string(reduce(1,HG)==0));',
        'print("GI70_B_SEED_DIM "+string(dim(HG)));',
        'print("GI70_B_SEED_BASIS_SIZE "+string(size(HG)));',
        'print("GI70_B_HILB_DONE"); quit;',
        '',
    ])
    write(OUT / "inputs/b_hilbert_seed_p32003.sing", seed)

    custody = {
        "class_id": CLASS,
        "source_rows": str(ROWS.relative_to(ROOT)),
        "source_rows_sha256": sha(ROWS),
        "source_meta": str(META.relative_to(ROOT)),
        "source_meta_sha256": sha(META),
        "variables_with_c": variables,
        "variables_without_c": section_vars,
        "x_charge": X_CHARGE,
        "y_deficit": Y_DEFICIT,
        "wp_functional": "17*x_charge+y_deficit",
        "wp_weights": weights,
        "rows": 66,
        "expanded_terms": terms,
        "unique_c_row_source_index": 22,
        "c1_rule": "token c -> 1; drop c and T",
    }
    write(OUT / "custody/chart.json", json.dumps(custody, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
