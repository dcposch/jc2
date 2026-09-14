#!/usr/bin/env python3
"""Exact-Q positive control: a genuine tame automorphism survives guided_gb."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import sys

ROOT = Path("/home/ubuntu/jc2")
sys.path.insert(0, str(ROOT))

from box.lib.guided_gb import (  # noqa: E402
    PromotionPolicy,
    RunConfig,
    SingularSystem,
    guided_groebner,
)


FROZEN = Path("/tmp/jc2-lane.HDMqeS/inputs/guided_gb.py")
LIVE = ROOT / "box/lib/guided_gb.py"
OUT = ROOT / "box/k4rayk89-20260903/controls-artifacts/genuine-tame-automorphism"
EXPECTED_GUIDED_SHA256 = (
    "501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def atomic_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def main() -> None:
    for key in (
        "OMP_NUM_THREADS",
        "OPENBLAS_NUM_THREADS",
        "MKL_NUM_THREADS",
        "NUMEXPR_NUM_THREADS",
        "FLINT_NUM_THREADS",
    ):
        os.environ[key] = "1"

    frozen_hash = sha256(FROZEN)
    live_hash = sha256(LIVE)
    if frozen_hash != EXPECTED_GUIDED_SHA256 or live_hash != frozen_hash:
        raise RuntimeError("frozen/live guided_gb.py hash mismatch")

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
    result = guided_groebner(
        system,
        policy=PromotionPolicy.exact_q(
            "genuine tame J=1 automorphism must remain nonunit"
        ),
        config=RunConfig(
            OUT,
            timeout_seconds=30,
            total_cores=1,
            max_parallel_jobs=1,
            run_perturbed_control=False,
        ),
    )

    if result.verdict.value != "DIM0_CHAR0":
        raise RuntimeError(f"unexpected verdict {result.verdict.value}")
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
            raise RuntimeError(
                f"control mismatch for {key}: {main_result[key]!r} != {expected!r}"
            )
    if run["returncode"] != 0 or run["timed_out"]:
        raise RuntimeError("unclean Singular exit")

    stdout = Path(run["stdout"]).read_text(encoding="utf-8")
    for marker in (
        "PRE__TAME_F x^2+2*y*mu",
        "PRE__TAME_G x",
        "PRE__TAME_J -2*mu",
        "PRE__TAME_INVERSE_AFTER_FORWARD_X 0",
        "PRE__TAME_INVERSE_AFTER_FORWARD_Y 0",
        "PRE__TAME_FORWARD_AFTER_INVERSE_X 0",
        "PRE__TAME_FORWARD_AFTER_INVERSE_Y 0",
    ):
        if marker not in stdout:
            raise RuntimeError(f"missing exact map marker: {marker}")

    summary = {
        "type": "K4RAY-GENUINE-TAME-AUTOMORPHISM-CONTROL",
        "status": "PASS",
        "field": "Q",
        "construction": {
            "h": "x",
            "beta": "mu*y",
            "alpha": "(2/3)*(x-x^3-3*mu*x*y)",
            "family": "(f,g)=(x^2+2*mu*y,x)",
            "jacobian": "-2*mu",
            "normalization": "-2*mu=1",
            "point": {"mu": "-1/2", "mu_inv": "-2"},
            "specialized_map": "(f,g)=(x^2-y,x)",
            "polynomial_inverse": "(u,v)->(v,v^2-u)",
            "specialized_jacobian": "1",
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
        "source": {
            "frozen_guided_gb": str(FROZEN),
            "guided_gb_sha256": frozen_hash,
            "driver": str(Path(__file__).resolve()),
        },
        "limits": {
            "outer_timeout_expected_seconds": 60,
            "internal_timeout_seconds": 30,
            "cores": 1,
        },
    }
    atomic_json(OUT / "summary.json", summary)
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
