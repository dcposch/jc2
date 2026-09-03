#!/usr/bin/env python3
"""Focused Moh p.209 (99,66) branch audit.

This driver deliberately separates what Moh prints from what is mechanically
constructible from the p.208--211 Appendix-II shape machine.
"""
from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import time
from dataclasses import asdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INPUT_DIR = Path("/tmp/jc2-lane.4zSf7l/inputs")
TWOPT = INPUT_DIR / "twopoint_order_batch.py"
OUT = ROOT / "box" / "moh9966-20260903"
SYSTEMS = OUT / "systems"
PRIMES = [32003, 32009, 32027]


def load_twopoint():
    sys.path.insert(0, str(INPUT_DIR))
    spec = importlib.util.spec_from_file_location("twopoint_order_batch_frozen", TWOPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {TWOPT}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def run_singular(path: Path, timeout: int) -> dict:
    t0 = time.time()
    try:
        r = subprocess.run(
            ["Singular", "-q", "--no-rc", str(path)],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as e:
        stdout = e.stdout.decode("utf-8", "ignore") if isinstance(e.stdout, bytes) else (e.stdout or "")
        stderr = e.stderr.decode("utf-8", "ignore") if isinstance(e.stderr, bytes) else (e.stderr or "")
        return {
            "verdict": "TIMEOUT",
            "elapsed_s": round(time.time() - t0, 3),
            "stdout_tail": (stdout + stderr)[-2000:],
        }
    out = (r.stdout or "") + (r.stderr or "")
    parsed = parse_singular(out)
    parsed.update(
        {
            "elapsed_s": round(time.time() - t0, 3),
            "returncode": r.returncode,
            "stdout_tail": out[-2000:],
        }
    )
    return parsed


def parse_singular(out: str) -> dict:
    lines = [line.strip() for line in out.splitlines()]

    def next_after(label: str):
        for i, line in enumerate(lines):
            if line == label and i + 1 < len(lines):
                return lines[i + 1]
        return None

    if "MAIN_SATURATED_EMPTY" in out:
        verdict = "SATURATED-EMPTY"
    elif "MAIN_NONTRIVIAL" in out:
        verdict = "SURVIVES"
    else:
        verdict = "ERROR"
    return {
        "verdict": verdict,
        "basis_size": next_after("MAIN_DONE basis_size="),
        "control_c_zero_pass": "CONTROL_EMPTY_PASS" in out,
        "control_c_one_pass": "CONTROL_NONEMPTY_PASS" in out,
    }


def build_branch_a_system(tp):
    """Moh branch A, constructible A/B superset.

    Moh prints "reduced ... to 10 coefficients" for this branch, but omits
    the actual ten-coefficient equations. The p.210 two-point d'=2,e'=3
    A/B chart is a source-checked predecessor of such eta reductions; emptiness
    of it is a stronger kill for any specialization contained in it.
    """
    row = tp.Row("99-branch-A-linear-power-AB-superset", 27, 18, 21, 8, 4, "MOH-p209")
    eqs, params, T, meta = tp.d2e3_ab_system(row, "fixed")
    meta = dict(meta)
    meta.update(
        {
            "source_branch": "LINEAR-POWER",
            "moh_printed_coefficients": 10,
            "constructed_coefficients_excluding_c": len(params) - 1,
            "constructed_unknowns_including_c": len(params),
            "rabinowitsch_symbol": str(T),
            "row": asdict(row),
            "interpretation": (
                "p.210 two-point A/B Jacobian system for the transformed "
                "(27,18;M2=21;V2=8;k=4) row; not Moh's omitted eta-reduced "
                "ten-coefficient display"
            ),
        }
    )
    return row, eqs, params, T, meta


def write_unsat_singular(tp, path: Path, row, eqs, params, T, char: int, meta: dict):
    """Same equations, no Rabinowitsch generator; used as a saturation control."""
    names = []
    rename = {}
    for sym in list(params) + [T]:
        base = tp.clean_name(str(sym))
        if base[0].isdigit():
            base = "v" + base
        nm = base
        n = 1
        while nm in names:
            n += 1
            nm = f"{base}_{n}"
        names.append(nm)
        rename[sym] = tp.sp.Symbol(nm)
    c_name = str(rename[params[-1]])
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as fh:
        fh.write(f"// unsaturated control for {row.src}\n")
        fh.write(f"ring R={char},({','.join(names)}),dp;\n")
        fh.write("option(redSB);\n")
        fh.write('print("UNSAT_START");\n')
        gens = [tp.sstr(e.subs(rename)) for e in eqs]
        fh.write("ideal I=%s;\n" % ",\n".join(gens))
        fh.write("ideal G=std(I);\n")
        fh.write('print("UNSAT_DONE basis_size="); size(G);\n')
        fh.write('if (reduce(1,G)==0) { print("UNSAT_EMPTY"); } else { print("UNSAT_NONTRIVIAL"); }\n')
        fh.write(f"ideal N={c_name}-1;\n")
        fh.write("ideal GN=std(N);\n")
        fh.write('if (reduce(1,GN)!=0) { print("UNSAT_CONTROL_C1_NONTRIVIAL"); }\n')
        fh.write("quit;\n")


def parse_unsat(out: str) -> dict:
    lines = [line.strip() for line in out.splitlines()]

    def next_after(label: str):
        for i, line in enumerate(lines):
            if line == label and i + 1 < len(lines):
                return lines[i + 1]
        return None

    if "UNSAT_EMPTY" in out:
        verdict = "EMPTY"
    elif "UNSAT_NONTRIVIAL" in out:
        verdict = "NONTRIVIAL"
    else:
        verdict = "ERROR"
    return {
        "verdict": verdict,
        "basis_size": next_after("UNSAT_DONE basis_size="),
        "control_c1_nontrivial": "UNSAT_CONTROL_C1_NONTRIVIAL" in out,
    }


def run_unsat(path: Path, timeout: int) -> dict:
    t0 = time.time()
    try:
        r = subprocess.run(
            ["Singular", "-q", "--no-rc", str(path)],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as e:
        stdout = e.stdout.decode("utf-8", "ignore") if isinstance(e.stdout, bytes) else (e.stdout or "")
        stderr = e.stderr.decode("utf-8", "ignore") if isinstance(e.stderr, bytes) else (e.stderr or "")
        return {"verdict": "TIMEOUT", "elapsed_s": round(time.time() - t0, 3), "stdout_tail": (stdout + stderr)[-2000:]}
    out = (r.stdout or "") + (r.stderr or "")
    ans = parse_unsat(out)
    ans.update({"elapsed_s": round(time.time() - t0, 3), "returncode": r.returncode, "stdout_tail": out[-2000:]})
    return ans


def count_only_records() -> list[dict]:
    return [
        {
            "branch": "B",
            "name": "TWO-ROOT-CUBIC",
            "moh_printed_variables": 11,
            "constructed_unknowns_including_c": None,
            "equations": None,
            "modular": [
                {"char": p, "verdict": "NOT-RUN", "reason": "Moh omits the 11-variable equations after Omega"}
                for p in PRIMES
            ],
            "exact": {
                "verdict": "COUNTING-BOUND",
                "reason": (
                    "SOURCE-OMITTED: p.209--210 prints Omega, five leading "
                    "conditions, and the count 11, but not the monomial "
                    "support or equations"
                ),
            },
        },
        {
            "branch": "C",
            "name": "THREE-SIMPLE-ROOT-CUBIC",
            "moh_printed_variables": None,
            "constructed_unknowns_including_c": None,
            "equations": None,
            "modular": [
                {"char": p, "verdict": "NOT-RUN", "reason": "not a Moh printed branch; no transform/equations supplied"}
                for p in PRIMES
            ],
            "exact": {
                "verdict": "COUNTING-BOUND",
                "reason": (
                    "MISSING-PARTITION: the 1+1+1 cubic is not excluded on "
                    "p.209, but the source supplies no corresponding Omega "
                    "normal form or coefficient system"
                ),
            },
        },
    ]


def main():
    if not TWOPT.is_file():
        raise SystemExit(f"missing frozen driver {TWOPT}")
    tp = load_twopoint()
    if subprocess.run(["which", "Singular"], capture_output=True, text=True).returncode != 0:
        raise SystemExit("Singular not found")
    SYSTEMS.mkdir(parents=True, exist_ok=True)

    row, eqs, params, T, meta = build_branch_a_system(tp)
    branch_a = {
        "branch": "A",
        "name": "LINEAR-POWER",
        "meta": meta,
        "unknowns_including_c_excluding_T": len(params),
        "unknowns_including_c_and_T": len(params) + 1,
        "equations_excluding_rabinowitsch": len(eqs),
        "modular": [],
        "exact": None,
    }

    for p in PRIMES:
        spath = SYSTEMS / f"branch_A_linear_AB_mod_{p}.sing"
        tp.write_singular(str(spath), row, eqs, params, T, p, meta)
        rec = run_singular(spath, timeout=300)
        rec.update({"char": p, "script": str(spath.relative_to(ROOT))})
        branch_a["modular"].append(rec)

    qpath = SYSTEMS / "branch_A_linear_AB_Q.sing"
    tp.write_singular(str(qpath), row, eqs, params, T, 0, meta)
    exact = run_singular(qpath, timeout=900)
    exact.update({"char": 0, "script": str(qpath.relative_to(ROOT))})
    branch_a["exact"] = exact

    upath = SYSTEMS / "branch_A_linear_AB_unsaturated_Q.sing"
    write_unsat_singular(tp, upath, row, eqs, params, T, 0, meta)
    branch_a["unsaturated_Q_control"] = run_unsat(upath, timeout=900)
    branch_a["unsaturated_Q_control"]["script"] = str(upath.relative_to(ROOT))

    result = {
        "input_dir": str(INPUT_DIR),
        "frozen_driver": str(TWOPT),
        "primes": PRIMES,
        "branches": [branch_a] + count_only_records(),
    }
    with (OUT / "moh9966_branch_results.json").open("w") as fh:
        json.dump(result, fh, indent=2, sort_keys=True)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
