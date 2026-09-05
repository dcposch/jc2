#!/usr/bin/env python3
"""Decide a reduced order chart with guided_gb (3 primes + exact Q).

Soundness of using a capped reduction: eliminating a pivot v from a row
c*v+w (w free of v, c a nonzero constant) is the isomorphism
R/(c*v+w) = k[other vars], so the residual ideal J_S built from a SUBSET S of
the chart rows satisfies J_S subset image(I) for the full chart ideal I.
Hence J_S = (1) implies I = (1) and the chart is dead.  A nonunit J_S decides
nothing and is typed OPEN.
"""
from __future__ import annotations
import argparse, json, os, sys
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "g9966n1b3-20260903"
for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
          "NUMEXPR_NUM_THREADS", "FLINT_NUM_THREADS"):
    os.environ[k] = "1"
sys.path.insert(0, str(ROOT))
from box.lib.guided_gb import (PromotionPolicy, RunConfig, SingularSystem,  # noqa: E402
                               guided_groebner)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reduce-json", required=True)
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--monomial-order", default="dp")
    a = ap.parse_args()
    rec = json.loads(Path(a.reduce_json).read_text())
    gens = [ln.rstrip(";") for ln in Path(rec["residual_file"]).read_text().splitlines()
            if ln.strip()]
    variables = list(rec["surviving_variables"])
    stem = Path(rec["meta"]).stem
    name = f"{stem}_reduced_cap{rec['cap_bytes']}"
    system = SingularSystem(
        name=name,
        prelude=f"ring R=0,({','.join(variables)}),{a.monomial_order};\noption(redSB);\n",
        generators=tuple(gens), characteristic=0, variables=tuple(variables),
        homogeneous=False,
        metadata={"meta": rec["meta"], "rows_sha256": rec["rows_sha256"],
                  "residual_sha256": rec["residual_sha256"],
                  "reduction_script_sha256": rec["script_sha256"],
                  "pivots": rec["pivots"], "cap_bytes": rec["cap_bytes"],
                  "rows_used": rec["rows_used"], "input_rows": rec["input_rows"],
                  "soundness": "sub-ideal after a triangular ring automorphism; "
                               "unit implies the full chart is unit"})
    res = guided_groebner(
        system,
        policy=PromotionPolicy.exact_q("inhomogeneous localized chart; exact Q required"),
        config=RunConfig(HERE / "guided" / stem / f"reduced_cap{rec['cap_bytes']}",
                         timeout_seconds=a.timeout, total_cores=1, max_parallel_jobs=1,
                         run_perturbed_control=False))
    cert = res.to_json()
    out = {"chart": stem, "name": name, "generators": len(gens),
           "variables": len(variables), "verdict": cert.get("verdict"),
           "runs": [{"char": r.get("characteristic"), "accepted": r.get("accepted"),
                     "unit": (r.get("main") or {}).get("unit"),
                     "dim": (r.get("main") or {}).get("dimension"),
                     "elapsed": r.get("elapsed_seconds"), "timed_out": r.get("timed_out")}
                    for r in cert.get("runs", [])]}
    print(json.dumps(out, indent=1))
    (HERE / "guided" / stem / f"decide_cap{rec['cap_bytes']}.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
