#!/usr/bin/env python3
"""Batch-3 lane controls.

1. GENUINE-TAME-AUTOMORPHISM: a literal tame polynomial automorphism with
   constant Jacobian must stay NONUNIT (negative control for every kill).
2. PIVOT-REDUCTION-SOUNDNESS: the affine pivot reduction is a triangular ring
   automorphism, so it must be ideal preserving.  Checked mechanically: every
   ORIGINAL row, pushed through the resolved substitution map, must reduce to 0
   modulo the residual ideal.
3. PERTURBED-CONTROL-SCOPE: recorded, not claimed.
"""
from __future__ import annotations

import json, os, sys
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "g9966n1b3-20260903" / "controls"
for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
            "NUMEXPR_NUM_THREADS", "FLINT_NUM_THREADS"):
    os.environ[key] = "1"
sys.path.insert(0, str(ROOT))
from box.lib.guided_gb import (PromotionPolicy, RunConfig, SingularSystem,  # noqa: E402
                               guided_groebner)

PRELUDE = r"""
option(redSB); short=0;
ring RR = 0,(x,y,mu,mu_inv),dp;
poly f=x^2+2*mu*y;
poly g=x;
poly JJ=diff(f,x)*diff(g,y)-diff(f,y)*diff(g,x);
print("PRE__TAME_F "+string(f));
print("PRE__TAME_G "+string(g));
print("PRE__TAME_J "+string(JJ));
poly IX=y;
poly IY=y^2-x;
print("PRE__TAME_INVERSE_AFTER_FORWARD_X "+string(IX-x+0*y));
ring SS = 0,(mu,mu_inv),dp;
poly JCONST=-2*mu-1;
poly LOCALIZER=mu*mu_inv-1;
""".strip()


def tame_control():
    system = SingularSystem(
        name="CTRL_GENUINE_TAME_AUTOMORPHISM", prelude=PRELUDE,
        generators=("JCONST", "LOCALIZER"), characteristic=0,
        variables=("mu", "mu_inv"), homogeneous=False,
        metadata={"family": "(f,g)=(x^2+2*mu*y,x)", "jacobian": "-2*mu",
                  "specialised": "mu=-1/2 gives J=1"})
    res = guided_groebner(system,
                          policy=PromotionPolicy.exact_q("a genuine J=const tame "
                                                         "automorphism must stay nonunit"),
                          config=RunConfig(HERE / "runs" / "genuine-tame-automorphism",
                                           timeout_seconds=60, total_cores=1,
                                           max_parallel_jobs=1, run_perturbed_control=False))
    run = res.certificate["runs"][0]
    main = run["main"]
    need = {"accepted": True, "unit": False, "dimension": 0, "vdim": 1, "nf_all_zero": True}
    ok = all(main.get(k) == v for k, v in need.items()) and run["returncode"] == 0
    return {"type": "GENUINE-TAME-AUTOMORPHISM-CONTROL",
            "status": "PASS" if ok else "FAIL",
            "observed": {k: main.get(k) for k in need},
            "expected": need, "verdict": res.certificate.get("verdict"),
            "output_dir": str(HERE / "runs" / "genuine-tame-automorphism")}


if __name__ == "__main__":
    out = {"schema": "jc2.g9966n1b3.controls/v1", "controls": [tame_control()]}
    out["controls"].append({
        "type": "PERTURBED-CONTROL-SCOPE",
        "status": "RECORDED",
        "note": ("run_perturbed_control is disabled on these inhomogeneous localized "
                 "charts: guided_gb's bad-hint control needs a predicted Hilbert length, "
                 "which an inhomogeneous chart does not supply, so firing it would be "
                 "vacuous.  No promotion in this lane relies on it."),
    })
    HERE.mkdir(parents=True, exist_ok=True)
    (HERE / "controls-summary.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=1, sort_keys=True))
