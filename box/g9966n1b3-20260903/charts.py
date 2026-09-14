#!/usr/bin/env python3
"""Chart preparation / native emission / guided decision for the batch-3 lane."""
from __future__ import annotations

import argparse, hashlib, importlib.util, json, os, subprocess, sys, time
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "g9966n1b3-20260903"
INPUTS = Path("/tmp/jc2-lane.g0hNAR/inputs")
ORDER_BASIS = ROOT / "box" / "orderbasis-20260903" / "order_basis_full.py"

THREAD_ENV = {"OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1",
              "NUMEXPR_NUM_THREADS": "1", "FLINT_NUM_THREADS": "1"}


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


ob = load_module("b3_ob", ORDER_BASIS)
gg = load_module("b3_gg", INPUTS / "guided_gb.py")
bands = load_module("b3_bands", INPUTS / "staged_band_emitter.py")

# Prop 6.3(3): ell = v_s-u_s-1 (Moh 1983 p.197).  Same rows as the charged batch-2 driver.
ROWS = {
    "S1": ob.Row("S1_n18_m12_Mm4_V1_k6", "S1 corrected", 18, 12, -4, 1, 6),
    "S2": ob.Row("S2_n36_m24_M8_V1_k2", "S2 corrected", 36, 24, 8, 1, 2),
    "S3": ob.Row("S3_n36_m24_M8_V5_k2", "S3 corrected", 36, 24, 8, 5, 2),
    "S4": ob.Row("S4_n27_m18_M6_V1_k4", "S4 corrected", 27, 18, 6, 1, 4),
    "S5": ob.Row("S5_n9_m6_M2_V1_k8", "S5 corrected", 9, 6, 2, 1, 8),
    "S6": ob.Row("S6_n9_m6_M5_V2_k8", "S6 corrected", 9, 6, 5, 2, 8),
    "S7": ob.Row("S7_n36_m24_M28_V8_k2", "S7 corrected", 36, 24, 28, 8, 2),
    "S8": ob.Row("S8_n27_m18_M21_V8_k4", "S8 corrected", 27, 18, 21, 8, 4),
}


def sha256(path):
    d = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(1 << 20), b""):
            d.update(blk)
    return d.hexdigest()


def atomic_write(path, payload):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp"); tmp.write_text(payload, encoding="utf-8")
    tmp.replace(path)


def run_call(command, out_path, err_path, timeout):
    env = os.environ.copy(); env.update(THREAD_ENV)
    wrapped = ["timeout", str(timeout), "stdbuf", "-oL", "-eL", *command]
    t0 = time.monotonic()
    with open(out_path, "w") as o, open(err_path, "w") as e:
        r = subprocess.run(wrapped, cwd=ROOT, env=env, stdout=o, stderr=e, text=True, check=False)
    return {"command": wrapped, "returncode": r.returncode, "timed_out": r.returncode == 124,
            "elapsed_seconds": round(time.monotonic() - t0, 3),
            "stdout": str(out_path), "stdout_sha256": sha256(out_path)}


def parse_part(text):
    return tuple(int(p) for p in text.replace(",", "+").split("+") if p)


def prepare(name, part):
    row = ROWS[name]
    spec = ob.build_full_spec(row, part)
    stem = ob.stem_for(row, part)
    rows_path = HERE / "rows" / f"{stem}_rows.tsv"
    builder = HERE / "builders" / f"{stem}_builder.sing"
    meta = HERE / "meta" / f"{stem}.json"
    atomic_write(builder, ob.native_builder_text(spec, rows_path))
    payload = {"schema": "jc2.g9966n1b3.order-chart/v1",
               "source_correction": {"target": f"c*x^{row.k}", "formula": "ell=v_s-u_s-1",
                                     "citation": "Moh 1983 Prop 6.3(3), p.197"},
               "meta": spec["meta"], "variables": [str(s) for s in spec["params"]],
               "sat": ob.sstr(spec["sat"]), "builder": str(builder),
               "builder_sha256": sha256(builder), "rows_path": str(rows_path)}
    atomic_write(meta, json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return meta, payload


def build(meta_path, timeout):
    payload = json.loads(Path(meta_path).read_text())
    builder = Path(payload["builder"])
    run = run_call(["Singular", "--cpus=1", "--threads=1", "--flint-threads=1", "--no-rc",
                    "-q", str(builder)], builder.with_suffix(".sing.out"),
                   builder.with_suffix(".sing.err"), timeout)
    text = Path(run["stdout"]).read_text(errors="replace")
    rows_path = Path(payload["rows_path"])
    run.update({"native_done": "NATIVE_DONE" in text and "? error occurred" not in text,
                "target_gate": "NATIVE_GATE target_xk_level0_nonzero=1" in text,
                "rows_exists": rows_path.exists(),
                "rows_sha256": sha256(rows_path) if rows_path.exists() else None,
                "row_count": (sum(1 for _ in open(rows_path)) - 1) if rows_path.exists() else None})
    atomic_write(HERE / "build-runs" / f"{Path(meta_path).stem}.json",
                 json.dumps(run, indent=2, sort_keys=True) + "\n")
    if run["native_done"] and run["target_gate"]:
        payload["builder_run"] = run
        atomic_write(meta_path, json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return run


def read_rows(path):
    exprs = []
    with open(path) as src:
        header = src.readline().rstrip("\n")
        if header != "source_index|h_power|x_power|y_power|expr":
            raise ValueError(f"unexpected row header in {path}")
        for line in src:
            if line.strip():
                exprs.append(line.rstrip("\n").split("|", 4)[4])
    return exprs


def solve(meta_path, characteristic, timeout, order="coefficient-first", extras=(),
          coeff_var=None, minpoly=None, monomial_order="dp", drop=()):
    payload = json.loads(Path(meta_path).read_text())
    variables = list(payload["variables"])
    for name in drop:
        if name in variables:
            variables.remove(name)
    if coeff_var is not None:
        variables.remove(coeff_var)
    if order == "coefficient-first":
        variables.sort(key=lambda n: (0 if n.startswith("A1_") else 1 if n.startswith("A2_")
                                      else 2 if n.startswith("A3_") else 3 if n.startswith("B")
                                      else 4 if n.startswith("h_") else 5, n))
    variables.append("T")
    generators = read_rows(payload["rows_path"]) + list(extras) + [f"T*({payload['sat']})-1"]
    if coeff_var is None:
        prelude = f"ring R={characteristic},({','.join(variables)}),{monomial_order};\noption(redSB);\n"
    else:
        prelude = (f"ring R=({characteristic},{coeff_var}),({','.join(variables)}),{monomial_order};\n"
                   f"minpoly={minpoly};\noption(redSB);\n")
    mat = list(extras) + ([f"COEFF:{coeff_var}:{minpoly}"] if coeff_var else []) \
        + ([f"ORDER:{monomial_order}"] if monomial_order != "dp" else []) \
        + ([f"DROP:{','.join(drop)}"] if drop else [])
    tag = "" if not mat else "_branch_" + hashlib.sha256("\n".join(mat).encode()).hexdigest()[:10]
    stem = Path(meta_path).stem
    system = gg.SingularSystem(
        name=f"{stem}_{order}{tag}", prelude=prelude, generators=tuple(generators),
        characteristic=characteristic, variables=tuple(variables), homogeneous=False,
        metadata={"meta": str(meta_path), "rows_sha256": sha256(payload["rows_path"]),
                  "target": payload["source_correction"]["target"], "variable_order": order,
                  "extra_generators": list(extras), "coefficient_variable": coeff_var,
                  "minpoly": minpoly, "monomial_order": monomial_order, "dropped": list(drop)})
    res = gg.guided_groebner(
        system, policy=gg.PromotionPolicy.exact_q("inhomogeneous localized chart; exact Q required"),
        config=gg.RunConfig(HERE / "guided" / stem / (order + tag), timeout_seconds=timeout,
                            total_cores=1, max_parallel_jobs=1, run_perturbed_control=False))
    return res.to_json()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=["prepare", "build", "solve"])
    ap.add_argument("--row", required=True)
    ap.add_argument("--part", required=True)
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--char", type=int, default=32003)
    ap.add_argument("--order", default="coefficient-first")
    ap.add_argument("--monomial-order", default="dp")
    ap.add_argument("--extra", action="append", default=[])
    args = ap.parse_args()
    part = parse_part(args.part)
    meta, payload = prepare(args.row, part)
    print(json.dumps({"meta": str(meta), "params_without_T": payload["meta"]["params_without_T"],
                      "partition": payload["meta"]["partition_label"]}))
    if args.action == "build":
        print(json.dumps(build(meta, args.timeout), indent=1, sort_keys=True))
    elif args.action == "solve":
        r = solve(meta, args.char, args.timeout, args.order, tuple(args.extra),
                  monomial_order=args.monomial_order)
        print(json.dumps({"verdict": r.get("verdict"), "name": r.get("name"),
                          "runs": [{"char": x.get("characteristic"), "accepted": x.get("accepted"),
                                    "dim": x.get("dimension"), "elapsed": x.get("elapsed_seconds"),
                                    "timed_out": x.get("timed_out")}
                                   for x in r.get("runs", [])]}, indent=1))
