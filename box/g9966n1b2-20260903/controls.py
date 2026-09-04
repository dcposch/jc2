#!/usr/bin/env python3
"""Replay the charged tame-form, genuine automorphism, and Hilbert controls."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys


ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "g9966n1b2-20260903" / "controls"
SOURCE = ROOT / "box" / "k4raypinned-20260903" / "pinned_chart.py"
FROZEN_GUIDED = Path("/tmp/jc2-lane.y07qTi/inputs/guided_gb.py")
LIVE_GUIDED = ROOT / "box" / "lib" / "guided_gb.py"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def genuine_tame_automorphism_control() -> dict:
    """Run the literal J=1 tame polynomial automorphism over exact Q."""
    sys.path.insert(0, str(ROOT))
    from box.lib.guided_gb import (  # noqa: PLC0415
        PromotionPolicy,
        RunConfig,
        SingularSystem,
        guided_groebner,
    )

    for key in (
        "OMP_NUM_THREADS",
        "OPENBLAS_NUM_THREADS",
        "MKL_NUM_THREADS",
        "NUMEXPR_NUM_THREADS",
        "FLINT_NUM_THREADS",
    ):
        os.environ[key] = "1"

    prelude = r"""
option(redSB); short=0;
ring RR = 0,(x,y,mu,mu_inv),dp;
poly h=x;
poly beta=mu*y;
poly alpha=(2/3)*(x-x^3-3*mu*x*y);
poly f=h^2+2*beta;
poly g=h^3+3*beta*h+(3/2)*alpha;
poly JJ=diff(f,x)*diff(g,y)-diff(f,y)*diff(g,x);
print("PRE__TAME_F "+string(f));
print("PRE__TAME_G "+string(g));
print("PRE__TAME_J "+string(JJ));
poly F0=x^2-y;
poly G0=x;
poly CHECK_IF_X=G0-x;
poly CHECK_IF_Y=G0^2-F0-y;
poly IX=y;
poly IY=y^2-x;
poly CHECK_FI_X=IX^2-IY-x;
poly CHECK_FI_Y=IX-y;
print("PRE__TAME_INVERSE_AFTER_FORWARD_X "+string(CHECK_IF_X));
print("PRE__TAME_INVERSE_AFTER_FORWARD_Y "+string(CHECK_IF_Y));
print("PRE__TAME_FORWARD_AFTER_INVERSE_X "+string(CHECK_FI_X));
print("PRE__TAME_FORWARD_AFTER_INVERSE_Y "+string(CHECK_FI_Y));
ring SS = 0,(mu,mu_inv),dp;
poly JCONST=-2*mu-1;
poly LOCALIZER=mu*mu_inv-1;
""".strip()
    system = SingularSystem(
        name="CTRL_GENUINE_TAME_AUTOMORPHISM",
        prelude=prelude,
        generators=("JCONST", "LOCALIZER"),
        characteristic=0,
        variables=("mu", "mu_inv"),
        homogeneous=False,
        metadata={
            "specialized_map": "(f,g)=(x^2-y,x)",
            "inverse": "(u,v)->(v,v^2-u)",
            "jacobian": "1",
        },
    )
    out = HERE / "runs" / "genuine-tame-automorphism"
    result = guided_groebner(
        system,
        policy=PromotionPolicy.exact_q(
            "genuine tame J=1 automorphism must remain nonunit"
        ),
        config=RunConfig(
            out,
            timeout_seconds=30,
            total_cores=1,
            max_parallel_jobs=1,
            run_perturbed_control=False,
        ),
    )
    run = result.certificate["runs"][0]
    main_result = run["main"]
    required = {
        "accepted": True,
        "unit": False,
        "dimension": 0,
        "vdim": 1,
        "nf_all_zero": True,
        "missing_markers": [],
    }
    for key, expected in required.items():
        if main_result[key] != expected:
            raise AssertionError((key, main_result[key], expected))
    if run["returncode"] != 0 or run["timed_out"]:
        raise AssertionError("unclean genuine tame control")
    stdout = Path(run["stdout"])
    stdout_text = stdout.read_text(encoding="utf-8")
    markers = (
        "PRE__TAME_F x^2+2*y*mu",
        "PRE__TAME_G x",
        "PRE__TAME_J -2*mu",
        "PRE__TAME_INVERSE_AFTER_FORWARD_X 0",
        "PRE__TAME_INVERSE_AFTER_FORWARD_Y 0",
        "PRE__TAME_FORWARD_AFTER_INVERSE_X 0",
        "PRE__TAME_FORWARD_AFTER_INVERSE_Y 0",
    )
    if not all(marker in stdout_text for marker in markers):
        raise AssertionError("missing genuine tame exact-map marker")
    return {
        "type": "GENUINE-TAME-AUTOMORPHISM-CONTROL",
        "status": "PASS",
        "construction": {
            "family": "(f,g)=(x^2+2*mu*y,x)",
            "jacobian": "-2*mu",
            "point": {"mu": "-1/2", "mu_inv": "-2"},
            "specialized_map": "(f,g)=(x^2-y,x)",
            "specialized_jacobian": "1",
            "polynomial_inverse": "(u,v)->(v,v^2-u)",
            "tame_factorization": "(x,y)->(x,y-x^2)->(-y,x)",
        },
        "guided_gb": {
            "verdict": result.verdict.value,
            "accepted": main_result["accepted"],
            "unit": main_result["unit"],
            "dimension": main_result["dimension"],
            "vdim": main_result["vdim"],
            "basis_size": main_result["basis_size"],
            "nf_all_zero": main_result["nf_all_zero"],
            "returncode": run["returncode"],
            "timed_out": run["timed_out"],
            "elapsed_seconds": run["elapsed_seconds"],
            "script": run["script"],
            "script_sha256": run["script_sha256"],
            "stdout": run["stdout"],
            "stdout_sha256": run["stdout_sha256"],
            "stderr": run["stderr"],
            "stderr_sha256": run["stderr_sha256"],
        },
        "exact_map_markers": list(markers),
    }


def main() -> None:
    if sha256(FROZEN_GUIDED) != sha256(LIVE_GUIDED):
        raise RuntimeError("frozen/live guided_gb.py mismatch")
    spec = importlib.util.spec_from_file_location("n1b2_pinned_controls", SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {SOURCE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.HERE = HERE
    module.RUNS = HERE / "runs"

    tame_form = module.positive_control(timeout=60, cores=1)
    genuine_tame = genuine_tame_automorphism_control()
    hint = module.perturbed_hint_control(timeout=180, cores=1)
    assertions = {
        "tame_form_exact_nonunit": (
            tame_form["verdict"] == "DIM0_CHAR0"
            and tame_form["runs"][0]["unit"] is False
            and tame_form["runs"][0]["dimension"] == 0
            and tame_form["runs"][0]["vdim"] == 2
        ),
        "tame_form_jacobian_marker": tame_form["counts"]["markers"].get("PRE__CTRL_J") == "6*x*mu^2",
        "genuine_tame_automorphism_survives": (
            genuine_tame["guided_gb"]["verdict"] == "DIM0_CHAR0"
            and genuine_tame["guided_gb"]["unit"] is False
            and genuine_tame["guided_gb"]["vdim"] == 1
        ),
        "genuine_tame_exact_inverse": len(genuine_tame["exact_map_markers"]) == 7,
        "hint_main_passes": hint["main_accepted"] is True,
        "perturbed_hint_fails": hint["perturbed_accepted"] is False,
    }
    if not all(assertions.values()):
        raise AssertionError(assertions)
    payload = {
        "schema": "jc2.g9966n1b2.controls/v1",
        "status": "PASS",
        "sources": {
            "tame_form_and_hilbert": str(SOURCE.relative_to(ROOT)),
            "tame_form_and_hilbert_sha256": sha256(SOURCE),
            "genuine_tame_formula": "charged k4ray-K89 report, controls section",
        },
        "frozen_guided_sha256": sha256(FROZEN_GUIDED),
        "tame_form": tame_form,
        "genuine_tame_automorphism": genuine_tame,
        "perturbed_hilbert": hint,
        "assertions": assertions,
        "reuse_scope": "shared algorithmic controls attached to every exact-Q kill in this lane",
    }
    output = HERE / "controls-summary.json"
    atomic_write(output, json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "output": str(output.relative_to(ROOT)), "assertions": assertions}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
