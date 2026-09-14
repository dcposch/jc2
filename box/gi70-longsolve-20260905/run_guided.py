#!/usr/bin/env python3
"""Seed a modular Hilbert series, then run two guided/CRT screens."""

from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent
RESULT = HERE / "results/b_guided_hilbert"
INPUT = HERE / "inputs"
HELPER = HERE / "lib/guided_gb.py"


def load_helper():
    spec = importlib.util.spec_from_file_location("gi70_guided_gb", HELPER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen guided_gb.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def run_seed() -> tuple[list[int], dict[str, object]]:
    RESULT.mkdir(parents=True, exist_ok=True)
    script = INPUT / "b_hilbert_seed_p32003.sing"
    out = RESULT / "seed_p32003.out"
    err = RESULT / "seed_p32003.err"
    started = time.monotonic()
    with out.open("w") as stdout, err.open("w") as stderr:
        proc = subprocess.run(
            ["stdbuf", "-oL", "Singular", "--no-rc", "-q", str(script)],
            stdout=stdout,
            stderr=stderr,
            text=True,
            timeout=9_900,
            env={**os.environ, "OMP_NUM_THREADS": "2"},
        )
    text = out.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"GI70_B_HNUM_BEGIN\s*\n([^\n]+)\s*\nGI70_B_HNUM_END", text)
    if proc.returncode != 0 or not match:
        raise RuntimeError(f"Hilbert seed failed rc={proc.returncode}; markers={bool(match)}")
    numerator = [int(x) for x in re.findall(r"-?\d+", match.group(1))]
    if not numerator or numerator[-1] != 0 or (len(numerator) > 1 and numerator[-2] == 0):
        raise RuntimeError("Hilbert numerator must carry exactly one trailing bookkeeping zero")
    if "GG__SAT_POS_CONTROL 1" not in text or "GG__SAT_NEG_CONTROL 1" not in text:
        raise RuntimeError("sat controls missing or failed in seed")
    meta = {
        "returncode": proc.returncode,
        "elapsed_seconds": time.monotonic() - started,
        "numerator": numerator,
        "one_trailing_zero": True,
        "stdout": str(out),
        "stderr": str(err),
    }
    (RESULT / "hilbert_hint.json").write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")
    return numerator, meta


def main() -> int:
    gb = load_helper()
    numerator, seed_meta = run_seed()
    custody = json.loads((HERE / "custody/chart.json").read_text())
    weights = tuple(custody["wp_weights"])
    variables = tuple(custody["variables_with_c"])
    template = (INPUT / "b_sat_prelude.template.sing").read_text()
    systems = []
    for prime in (32009, 32027):
        prelude = template.replace("__PRIME__", str(prime))
        systems.append(gb.SingularSystem(
            name=f"gi70_sat_p{prime}",
            prelude=prelude,
            generators=("S",),
            characteristic=prime,
            variables=variables,
            homogeneous=True,
            positive_weights=weights,
            metadata={
                "scope": "homogeneous saturation (I:c^infinity)",
                "hilbert_seed_prime": 32003,
                "unit_promotion": "forbidden; modular screen only",
            },
        ))
    hint = gb.HilbertHint(tuple(numerator), weights, predicted_length=None)
    policy = gb.PromotionPolicy(
        scope=gb.PromotionScope.NONE,
        require_controls=True,
        allow_modular_unit_promotion=False,
        note="CRT reconstructs scalar invariants only; modular UNIT is not a Q certificate",
    )
    config = gb.RunConfig(
        output_dir=RESULT / "guided",
        timeout_seconds=9_600,
        total_cores=4,
        max_parallel_jobs=2,
        run_perturbed_control=False,
    )
    result = gb.guided_groebner(systems, hint=hint, policy=policy, config=config)
    payload = result.to_json()
    payload["hilbert_seed"] = seed_meta
    payload["interpretation"] = {
        "scope": "modular Hilbert-driven standard bases of homogeneous (I:c^infinity)",
        "crt_limit": "scalar invariants only; no basis coefficients or rational identity",
        "unit_rule": "never promote a modular unit",
    }
    (RESULT / "guided_result_augmented.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("GI70_B_GUIDED_VERDICT", result.verdict.value, flush=True)
    for run in payload["certificate"]["runs"]:
        print(
            "GI70_B_RUN",
            run["characteristic"],
            "rc", run["returncode"],
            "timeout", int(run["timed_out"]),
            "unit", int(run["main"]["unit"]),
            "dim", run["main"]["dimension"],
            "basis", run["main"]["basis_size"],
            flush=True,
        )
    print("GI70_B_DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
