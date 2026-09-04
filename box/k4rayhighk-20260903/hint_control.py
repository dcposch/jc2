#!/usr/bin/env python3
"""Hilbert-hint run + guided_gb perturbed-series negative control (K=4 homogeneous chart)."""
import json, sys
from pathlib import Path
ROOT = Path("/home/ubuntu/jc2")
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "box" / "k4rayhighk-20260903"))
from box.lib.guided_gb import (HilbertHint, PromotionPolicy, RunConfig,
                               SingularSystem, guided_groebner)
import gen_hk
from drive import prelude_rowcount, RUNS

K, Bdeg = 4, 3
NUM = (1,0,-21,29,159,-566,546,558,-2037,2408,-1485,429,13,-42,8,0)
pre, names, wts = gen_hk.direct(K, Bdeg, 0, 4)
info = prelude_rowcount(pre, f"HINT_K{K}_B{Bdeg}")
gens = tuple(f"ROWS[{i}]" for i in range(1, info["n"] + 1))
hint = HilbertHint(NUM, tuple(wts), None)
sysm = SingularSystem(name=f"HINT_K{K}_B{Bdeg}", prelude=pre, generators=gens,
                      characteristic=0, variables=tuple(names),
                      homogeneous=True, positive_weights=tuple(wts))
cfg = RunConfig(output_dir=RUNS / f"HINT_K{K}_B{Bdeg}", timeout_seconds=600,
                total_cores=1, run_perturbed_control=True)
res = guided_groebner(sysm, hint=hint,
                      policy=PromotionPolicy.homogeneous_properness(
                          "weighted-homogeneous positive-weight chart cone"),
                      config=cfg)
out = (RUNS / f"HINT_K{K}_B{Bdeg}" / f"HINT_K{K}_B{Bdeg}_Q.out")
txt = out.read_text() if out.exists() else ""
marks = [l for l in txt.splitlines() if l.startswith("GG__") and
         any(t in l for t in ("NF_ALL_ZERO", "PERTURBED_FAILED", "BASIS_SIZE", "DIM ", "TARGET_HNUM"))]
print(json.dumps({"verdict": res.verdict.value,
                  "accepted": res.certificate["accepted_run_count"],
                  "note": res.certificate["promotion_note"],
                  "marks": marks}, indent=1))
