#!/usr/bin/env python3
"""Validate frozen R005 rows and stream the three bounded-probe inputs."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import re
import resource
import sys
import time
from fractions import Fraction as F
from pathlib import Path

SCRATCH = Path(os.environ.get("JC2_SCRATCH", "/home/ubuntu/classA-smallest-20260906.xpXroy"))
ROOT = SCRATCH / "repo"
ROWS = Path(os.environ.get("JC2_ROWS", "/dev/shm/lambda-lowweight-R005-rows.tsv"))
EXPECTED_ROWS_SHA = os.environ.get("JC2_ROWS_SHA", "")
EXPECTED_COORD_SHA = "9758dedb763696c99ee72d3cd7345d7dc336637fb65909731811a6e5afe37c89"
EXPECTED_PROGRAM_SHA = "8353325956564822d62c676bb8776f09bad015be709e966d58fa48767f632bd5"
MAX_EXPANDED = 20_000_000_000
IDENT = re.compile(r"([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?\Z")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 24), b""):
            h.update(block)
    return h.hexdigest()


def import_at(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def bidegree(name: str, K: int, ell: int, n: int, m: int) -> tuple[int, int]:
    if name == "c":
        return ell + 1, n + m - 1
    hit = re.fullmatch(r"h_(\d+)_(\d+)", name)
    if hit:
        b, a = map(int, hit.groups())
        return b, K - a
    hit = re.fullmatch(r"[AB](\d+)_(\d+)_(\d+)", name)
    if hit:
        i, b, a = map(int, hit.groups())
        return b, i * K - a
    raise AssertionError(f"unparsed variable {name!r}")


def parse_expression(expr: str, degrees: dict[str, tuple[int, int]], mapping: dict[str, str]):
    """Return c=1 safe-name text, term count, and the common source bidegree."""
    translated: list[str] = []
    common = None
    term_count = 0
    position = 0
    while position < len(expr):
        sign = ""
        if expr[position] in "+-":
            sign = expr[position]
            position += 1
        end = position
        while end < len(expr) and expr[end] not in "+-":
            end += 1
        body = expr[position:end]
        if not body:
            raise AssertionError("empty polynomial term")
        numeric: list[str] = []
        safe: list[str] = []
        db = dd = 0
        for factor in body.split("*"):
            if factor.isdigit():
                numeric.append(factor)
                continue
            hit = IDENT.fullmatch(factor)
            if hit is None or hit.group(1) not in degrees:
                raise AssertionError(f"bad factor {factor!r}")
            name = hit.group(1)
            power = int(hit.group(2) or 1)
            wb, wd = degrees[name]
            db += power * wb
            dd += power * wd
            if name != "c":
                mapped = mapping[name]
                safe.append(mapped if power == 1 else f"{mapped}^{power}")
        degree = (db, dd)
        if common is None:
            common = degree
        elif degree != common:
            raise AssertionError(f"nonhomogeneous row: {common} versus {degree}")
        mapped_body = "*".join(numeric + safe) or "1"
        translated.append(sign + mapped_body)
        term_count += 1
        position = end
    return "".join(translated), term_count, common


def emitted_program(row: dict, rc: dict) -> tuple[str, dict]:
    cc = import_at("r005_counts", ROOT / "box/residual66-20260905/chart_counts.py")
    compiler, emitter, fix, custody = cc.production_emitter_runtime()
    child = row["own_child"]
    K, e, q, ell, d = rc["K"], rc["e"], rc["q"], child["ell"], F(rc["d"])
    C = dict(K=K, e=e, q=q, u=0, R=0, Pi=0, d3prime=1, delta1=F(0),
             delta2=F(0), delta_s=-d, B=F(-1), B_safe=F(-1), B_tight=F(-1),
             lambda_P=F(0), lambda_Q=F(0), s=2, ell=ell, two_point=False,
             support_basis="proved_outer_disc_G_only_H1_H2_H3_v1")
    inventory = emitter.supports(compiler, C)
    key = (child["n_prime"], child["m_prime"], child["M_prime"][-1], ell)
    name = cc.receiver_key_string(key)
    rr = compiler.OB.Row(key=name, label=f"residual66 dry production {name}",
                         n=key[0], m=key[1], M2=key[2], V2=0, k=ell)
    spec = compiler.build_spec(C, inventory["h"], inventory["alpha_pre"],
                               inventory["beta_pre"], rr,
                               "proved_G_only_class_uniform_count_only")
    spec["low_terms"], spec["high_terms"] = list(spec["high_terms"]), list(spec["low_terms"])
    raw = compiler.OB.native_builder_text(spec, Path("/tmp/residual66-production-count-only-rows.tsv"))
    program, fixinfo = fix.fix_text(raw)
    assert hashlib.sha256(program.encode()).hexdigest() == EXPECTED_PROGRAM_SHA
    model = cc.parse_emitted_row_program(program, e=e, q=q,
                                         expected_program_sha256=EXPECTED_PROGRAM_SHA)
    return program, {"variables": model["parameters"], "custody": custody,
                     "fix": fixinfo, "key": name,
                     "coordinate_digest": cc.coordinate_digest}


def main() -> None:
    started = time.monotonic()
    input_rows = [json.loads(line) for line in (SCRATCH / "inputs/roster.jsonl").read_text().splitlines()]
    row = next(value for value in input_rows if value["row_id"] == "R005")
    rc = row["receiver_chart"]
    chart = json.loads((SCRATCH / "inputs/chart-counts.json").read_text())
    match = next(value for value in chart["classes"] if value["receiver_key_string"] == rc["receiver_key_string"])
    assert match["coefficient_coordinate_sha256"] == rc["coefficient_coordinate_sha256"] == EXPECTED_COORD_SHA
    assert match["coefficient_generators"] == rc["coefficient_generators"] == 484
    assert match["unknowns_without_T"] == rc["unknowns_without_T"] == 307
    if EXPECTED_ROWS_SHA:
        actual_rows_sha = sha256(ROWS)
        assert actual_rows_sha == EXPECTED_ROWS_SHA, (actual_rows_sha, EXPECTED_ROWS_SHA)
    else:
        actual_rows_sha = sha256(ROWS)

    program, production = emitted_program(row, rc)
    variables = [str(value) for value in production["variables"]]
    assert len(variables) == 307 and variables[-1] == "c"
    class_id = "C_n27m18_M20_ell2_s2"
    program_path = ROOT / f"box/gi-only-20260905/classes/{class_id}/builders/{class_id}_G_builder.sing"
    program_path.parent.mkdir(parents=True, exist_ok=True)
    program_path.write_text(program)
    assert sha256(program_path) == EXPECTED_PROGRAM_SHA

    n, m, K, ell = 27, 18, 9, 2
    degrees = {name: bidegree(name, K, ell, n, m) for name in variables}
    weights = {name: 19 * pair[0] + pair[1] for name, pair in degrees.items()}
    assert all(weight > 0 for weight in weights.values())
    safe_source = [name for name in variables if name != "c"]
    mapping = {name: f"v{index}" for index, name in enumerate(safe_source, 1)}
    data = SCRATCH / "data"
    data.mkdir(parents=True, exist_ok=True)
    msolve = data / "R005_c1_p1073741827.ms"
    prelude_q = data / "R005_sat_Q.prelude.sing"
    prelude_p = data / "R005_sat_p32003.prelude.sing"
    exact = data / "R005_full_Tblock_Q.sing"
    var_text = ",".join(variables)
    weight_text = ",".join(str(weights[name]) for name in variables)
    coords: list[tuple[int, int, int]] = []
    row_degrees: list[tuple[int, int]] = []
    total_terms = 0
    with (ROWS.open(encoding="utf-8") as source,
          prelude_q.open("w") as q_out, prelude_p.open("w") as p_out,
          exact.open("w") as exact_out, msolve.open("w") as msolve_out):
        assert source.readline().rstrip("\n") == "source_index|h_power|x_power|y_power|expr"
        q_out.write(f'LIB "elim.lib";\nring r=0,({var_text}),wp({weight_text});\noption(redSB);\nideal I=\n')
        p_out.write(f'LIB "elim.lib";\nring r=32003,({var_text}),wp({weight_text});\noption(redSB);\nideal I=\n')
        exact_out.write(f'ring r=0,(T,{var_text}),(dp(1),wp({weight_text}));\noption(redSB);\noption(prot);\nideal I=\n')
        msolve_out.write(",".join(mapping[name] for name in safe_source) + "\n1073741827\n")
        for ordinal, line in enumerate(source):
            fields = line.rstrip("\n").split("|", 4)
            assert len(fields) == 5 and int(fields[0]) == ordinal
            coords.append(tuple(map(int, fields[1:4])))
            translated, terms, degree = parse_expression(fields[4], degrees, mapping)
            total_terms += terms
            row_degrees.append(degree)
            delimiter = ";\n" if ordinal == 483 else ",\n"
            rendered = "(" + fields[4] + ")" + delimiter
            q_out.write(rendered)
            p_out.write(rendered)
            exact_out.write(rendered)
            msolve_out.write(translated + ("\n" if ordinal == 483 else ",\n"))
            if q_out.tell() + p_out.tell() + exact_out.tell() + msolve_out.tell() > MAX_EXPANDED:
                raise RuntimeError("PREPARATION_DISK_GUARD_GT_20GB")
        sat_trailer = "\n".join([
            'ideal PC=c; list PL=sat(PC,ideal(c)); ideal PG=PL[1];',
            'if (typeof(PG)!="ideal" or reduce(1,PG)!=0) { ERROR("positive sat control failed"); }',
            f'ideal NC=c*{safe_source[0]}; list NL=sat(NC,ideal(c)); ideal NG=NL[1];',
            f'if (typeof(NG)!="ideal" or reduce({safe_source[0]},NG)!=0 or reduce(1,NG)==0) {{ ERROR("negative sat control failed"); }}',
            'list SL=sat(I,ideal(c)); ideal S=SL[1];',
            'if (typeof(S)!="ideal") { ERROR("target sat component is not ideal"); }',
            'print("R005__SAT_PRELUDE_READY "+string(size(S)));', ''
        ])
        q_out.write(sat_trailer)
        p_out.write(sat_trailer)
        exact_out.write("\n".join([
            'ideal PC=c,T*c-1; ideal PG=std(PC);',
            'if (reduce(1,PG)!=0) { ERROR("positive T-block control failed"); }',
            f'ideal NC={safe_source[0]},T*c-1; ideal NG=std(NC);',
            'if (reduce(1,NG)==0) { ERROR("negative T-block control failed"); }',
            'I[size(I)+1]=T*c-1;',
            'print("R005__STD_BEGIN"); timer=1; int R005_T0=timer;',
            'ideal G=std(I);',
            'print("R005__STD_SECONDS "+string(timer-R005_T0));',
            'int R005_UNIT=(reduce(1,G)==0);',
            'print("R005__UNIT "+string(R005_UNIT));',
            'print("R005__BASIS_SIZE "+string(size(G)));',
            'print("R005__DIM "+string(dim(G)));',
            'print("R005__DONE 1");',
            'quit;', ''
        ]))
    assert len(coords) == 484
    assert production["coordinate_digest"](coords) == EXPECTED_COORD_SHA
    assert total_terms == 53_209_262
    assert len(set(row_degrees)) >= 1

    files = {}
    for name, path in {"rows": ROWS, "program": program_path, "msolve": msolve, "prelude_q": prelude_q,
                       "prelude_p32003": prelude_p, "exact_Tblock": exact}.items():
        files[name] = {"path": str(path), "bytes": path.stat().st_size, "sha256": sha256(path)}
    scratch_bytes = sum(path.stat().st_size for path in data.iterdir() if path.is_file())
    if scratch_bytes > MAX_EXPANDED:
        raise RuntimeError("PREPARATION_DISK_GUARD_GT_20GB")
    result = {
        "status": "PASS_EXACT_ROWS_COORDINATES_HOMOGENEITY_AND_INPUTS",
        "row_id": "R005", "receiver_key": rc["receiver_key_string"],
        "class_id": class_id, "unknowns_without_T": len(variables),
        "coefficient_generators": len(coords), "full_generators": len(coords) + 1,
        "coefficient_coordinate_sha256": production["coordinate_digest"](coords),
        "production_program_sha256": EXPECTED_PROGRAM_SHA,
        "rows_sha256": actual_rows_sha, "total_terms": total_terms,
        "all_rows_bihomogeneous": True,
        "distinct_row_bidegrees": sorted([list(pair) for pair in set(row_degrees)]),
        "scalar_weight_rule": "19*b+d", "weights_positive": True,
        "weight_min": min(weights.values()), "weight_max": max(weights.values()),
        "msolve_c1_variable_count": len(safe_source),
        "msolve_integer_slot_product": total_terms * len(safe_source),
        "msolve_integer_slot_product_lt_2pow31": total_terms * len(safe_source) < 2**31,
        "scratch_data_bytes": scratch_bytes, "files": files,
        "wall_seconds": round(time.monotonic() - started, 3),
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    }
    (SCRATCH / "results/input_manifest.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
