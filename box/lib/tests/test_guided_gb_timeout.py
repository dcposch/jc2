#!/usr/bin/env python3
"""Timeout-contract and control-battery tests for box/lib/guided_gb.py.

Exercises: normal completion, typed internal-timeout expiry (std and
Hilbert-seed stages), outer-watchdog suppression of the inherited cap,
PromotionPolicy.exact_q / modular-unit-not-promoted, and the census-sweep
known-empty / known-nonempty / tame-automorphism battery.
"""

from __future__ import annotations

import json
import sys
import time
import traceback
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
LIB = ROOT / "box" / "lib"
OUT = ROOT / "box" / "guided-gb-fix-20260905" / "unit"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(LIB))

from box.lib.guided_gb import (  # noqa: E402
    STAGE_HILBERT_SEED,
    STAGE_STD,
    HilbertHint,
    PromotionPolicy,
    PromotionScope,
    RunConfig,
    SingularSystem,
    Verdict,
    guided_groebner,
    resolve_stage_timeout,
    run_hilbert_seed,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def cfg(name: str, **kwargs) -> RunConfig:
    kwargs.setdefault("total_cores", 1)
    kwargs.setdefault("max_parallel_jobs", 1)
    kwargs.setdefault("run_perturbed_control", False)
    return RunConfig(OUT / name, **kwargs)


def test_resolve_stage_timeout() -> None:
    default = RunConfig(OUT / "resolve")
    require(resolve_stage_timeout(default, STAGE_STD) == 1800, "legacy std default is 1800")
    require(resolve_stage_timeout(default, STAGE_HILBERT_SEED) is None, "Hilbert seed default is none")

    gi70 = RunConfig(
        OUT / "resolve",
        timeout_seconds=9_900,
        outer_watchdog_seconds=10_200,
    )
    require(resolve_stage_timeout(gi70, STAGE_STD) is None, "outer watchdog suppresses inherited std cap")
    require(resolve_stage_timeout(gi70, STAGE_HILBERT_SEED) is None, "outer watchdog leaves seed uncapped")

    explicit = RunConfig(
        OUT / "resolve",
        timeout_seconds=9_900,
        outer_watchdog_seconds=10_200,
        std_timeout_seconds=9_600,
        hilbert_seed_timeout_seconds=1,
    )
    require(resolve_stage_timeout(explicit, STAGE_STD) == 9_600, "explicit std cap wins")
    require(resolve_stage_timeout(explicit, STAGE_HILBERT_SEED) == 1, "explicit seed cap wins")

    none = RunConfig(OUT / "resolve", timeout_seconds=None)
    require(resolve_stage_timeout(none, STAGE_STD) is None, "timeout_seconds=None means no std cap")
    zero = RunConfig(OUT / "resolve", timeout_seconds=0, std_timeout_seconds=0, hilbert_seed_timeout_seconds=0)
    require(resolve_stage_timeout(zero, STAGE_STD) is None, "nonpositive means no cap")
    require(resolve_stage_timeout(zero, STAGE_HILBERT_SEED) is None, "nonpositive seed means no cap")


def test_policy_byte_identity() -> None:
    policy = PromotionPolicy.exact_q("census_sweep: modular units are not promoted")
    require(policy.scope == PromotionScope.EXACT_Q, "exact_q scope")
    require(policy.require_controls is True, "exact_q require_controls")
    require(policy.allow_modular_unit_promotion is False, "exact_q forbids modular unit promotion")
    require(policy.note == "census_sweep: modular units are not promoted", "exact_q note passthrough")


def test_known_empty() -> None:
    system = SingularSystem(
        name="CTRL_KNOWN_EMPTY",
        prelude="ring R=0,(c,T),dp;\npoly f=c;\npoly g=T*c-1;\n",
        generators=("f", "g"),
        characteristic=0,
        variables=("c", "T"),
    )
    result = guided_groebner(
        system,
        policy=PromotionPolicy.exact_q("known-empty (c, Tc-1)=(1)"),
        config=cfg("known_empty", timeout_seconds=30),
    )
    run = result.certificate["runs"][0]
    require(result.verdict == Verdict.UNIT_IDEAL_CHAR0, f"empty verdict {result.verdict}")
    require(run["main"]["unit"] is True, "empty not unit")
    require(run["main"]["dimension"] == -1, f"empty dim {run['main']['dimension']}")
    require(run["timed_out"] is False, "empty timed out")
    require(result.certificate["timeout_stage"] is None, "empty timeout_stage")
    require(
        result.certificate["promotion_note"] == "exact Q standard basis reduced 1 to 0",
        "empty promotion note drifted",
    )
    require(result.certificate["policy"]["allow_modular_unit_promotion"] is False, "policy drifted")


def test_known_nonempty() -> None:
    system = SingularSystem(
        name="CTRL_KNOWN_NONEMPTY",
        prelude="ring R=0,(c,T),dp;\npoly f=c-1;\npoly g=T*c-1;\n",
        generators=("f", "g"),
        characteristic=0,
        variables=("c", "T"),
    )
    result = guided_groebner(
        system,
        policy=PromotionPolicy.exact_q("known-nonempty (c-1, Tc-1)"),
        config=cfg("known_nonempty", timeout_seconds=30),
    )
    run = result.certificate["runs"][0]
    require(result.verdict == Verdict.DIM0_CHAR0, f"nonempty verdict {result.verdict}")
    require(run["main"]["unit"] is False, "nonempty unexpectedly unit")
    require(run["main"]["dimension"] == 0, f"nonempty dim {run['main']['dimension']}")
    require(
        result.certificate["promotion_note"] == "exact Q standard basis has dimension zero",
        "nonempty promotion note drifted",
    )


def test_tame_automorphism() -> None:
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
print("PRE__TAME_FORWARD_AFTER_INVERSE_X "+string(CHECK_FI_X));
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
    )
    result = guided_groebner(
        system,
        policy=PromotionPolicy.exact_q("genuine tame J=1 automorphism must remain nonunit"),
        config=cfg("tame", timeout_seconds=30),
    )
    run = result.certificate["runs"][0]
    stdout = Path(run["stdout"]).read_text(encoding="utf-8")
    require(result.verdict == Verdict.DIM0_CHAR0, f"tame verdict {result.verdict}")
    require(run["main"]["unit"] is False, "tame unit")
    require(run["main"]["dimension"] == 0, f"tame dim {run['main']['dimension']}")
    require("PRE__TAME_INVERSE_AFTER_FORWARD_X 0" in stdout, "tame inverse marker")
    require("PRE__TAME_FORWARD_AFTER_INVERSE_X 0" in stdout, "tame forward marker")


def test_modular_unit_not_promoted() -> None:
    system = SingularSystem(
        name="CTRL_MODULAR_UNIT",
        prelude="ring R=32003,(x),dp;\npoly one=1;\n",
        generators=("one",),
        characteristic=32003,
        variables=("x",),
    )
    result = guided_groebner(
        system,
        policy=PromotionPolicy.exact_q("modular units are not promoted"),
        config=cfg("modular_unit", timeout_seconds=30),
    )
    run = result.certificate["runs"][0]
    require(result.verdict == Verdict.MODULAR_ONLY, f"modular unit verdict {result.verdict}")
    require(run["main"]["unit"] is True, "modular unit flag")
    require(result.certificate["policy"]["allow_modular_unit_promotion"] is False, "promotion flag")
    require(
        result.certificate["promotion_note"]
        == "modular unit ideal was not promoted to characteristic zero",
        "modular-unit note drifted",
    )


def test_std_timeout_typed() -> None:
    system = SingularSystem(
        name="TO_STD",
        prelude='ring R=0,(x,y),dp;\nsystem("sh","sleep 3");\npoly f=x;\npoly g=y;\n',
        generators=("f", "g"),
        characteristic=0,
    )
    started = time.monotonic()
    result = guided_groebner(
        system,
        policy=PromotionPolicy.exact_q(),
        config=cfg("to_std", timeout_seconds=1),
    )
    elapsed = time.monotonic() - started
    require(result.verdict == Verdict.INCONCLUSIVE_TIMEOUT, f"std timeout verdict {result.verdict}")
    require(result.certificate["timeout_stage"] == STAGE_STD, "std timeout_stage")
    require(
        result.certificate["promotion_note"]
        == "no accepted result before timeout at stage std",
        "std timeout note",
    )
    require(result.certificate["runs"][0]["timed_out"] is True, "std timed_out flag")
    require(result.certificate["runs"][0]["timeout_stage"] == STAGE_STD, "run timeout_stage")
    require(elapsed < 2.5, f"std timeout took {elapsed:.2f}s")


def test_hilbert_seed_timeout_typed() -> None:
    seed = SingularSystem(
        name="TO_SEED",
        prelude='ring R=32003,(x,y,z),wp(1,1,1);\nsystem("sh","sleep 3");\n',
        generators=("x", "y", "z"),
        characteristic=32003,
        homogeneous=True,
        positive_weights=(1, 1, 1),
    )
    started = time.monotonic()
    result = guided_groebner(
        seed,
        policy=PromotionPolicy(),
        config=cfg("to_seed", timeout_seconds=1800, hilbert_seed_timeout_seconds=1),
        hilbert_seed=seed,
    )
    elapsed = time.monotonic() - started
    require(result.verdict == Verdict.INCONCLUSIVE_TIMEOUT, f"seed timeout verdict {result.verdict}")
    require(result.certificate["timeout_stage"] == STAGE_HILBERT_SEED, "seed timeout_stage")
    require(
        result.certificate["promotion_note"]
        == "no accepted result before timeout at stage hilbert_seed",
        "seed timeout note",
    )
    require(result.certificate["hilbert_seed_run"]["timed_out"] is True, "seed run timed_out")
    require(result.certificate["accepted_run_count"] == 0, "seed timeout accepted a std run")
    require(elapsed < 2.5, f"seed timeout took {elapsed:.2f}s")
    require(result.certificate["hilbert_hint"] is None, "seed timeout produced a hint")


def test_outer_watchdog_suppresses_inherited_cap() -> None:
    system = SingularSystem(
        name="OUTER_OK",
        prelude='ring R=0,(x,y),dp;\nsystem("sh","sleep 2");\npoly f=x;\npoly g=y;\n',
        generators=("f", "g"),
        characteristic=0,
    )
    started = time.monotonic()
    result = guided_groebner(
        system,
        policy=PromotionPolicy.exact_q(),
        config=cfg(
            "outer_ok",
            timeout_seconds=1,
            outer_watchdog_seconds=30,
        ),
    )
    elapsed = time.monotonic() - started
    require(result.verdict == Verdict.DIM0_CHAR0, f"outer-watchdog verdict {result.verdict}")
    require(result.certificate["timeout_stage"] is None, "outer-watchdog timeout_stage")
    require(result.certificate["runs"][0]["timed_out"] is False, "outer-watchdog timed_out")
    require(elapsed >= 1.5, f"sleep was skipped ({elapsed:.2f}s)")
    require(elapsed < 8, f"outer-watchdog hung {elapsed:.2f}s")
    require(result.certificate["stage_timeouts"]["std"] is None, "inherited std cap not suppressed")


def test_explicit_std_timeout_with_outer_watchdog() -> None:
    system = SingularSystem(
        name="OUTER_EXPLICIT",
        prelude='ring R=0,(x,y),dp;\nsystem("sh","sleep 3");\npoly f=x;\npoly g=y;\n',
        generators=("f", "g"),
        characteristic=0,
    )
    result = guided_groebner(
        system,
        policy=PromotionPolicy.exact_q(),
        config=cfg(
            "outer_explicit",
            timeout_seconds=1800,
            outer_watchdog_seconds=30,
            std_timeout_seconds=1,
        ),
    )
    require(result.verdict == Verdict.INCONCLUSIVE_TIMEOUT, f"explicit std verdict {result.verdict}")
    require(result.certificate["timeout_stage"] == STAGE_STD, "explicit std stage")


def test_hilbert_seed_then_std_completes() -> None:
    seed = SingularSystem(
        name="SEED_OK",
        prelude="ring R=32003,(x,y,z),wp(1,1,1);\n",
        generators=("x", "y", "z"),
        characteristic=32003,
        homogeneous=True,
        positive_weights=(1, 1, 1),
    )
    result = guided_groebner(
        seed,
        policy=PromotionPolicy.homogeneous_properness("synthetic dim-0 cone"),
        config=cfg("seed_ok", timeout_seconds=30),
        hilbert_seed=seed,
    )
    require(result.verdict == Verdict.DIM0_CHAR0, f"seed+std verdict {result.verdict}")
    require(result.certificate["timeout_stage"] is None, "seed+std timeout_stage")
    require(result.certificate["hilbert_hint"] is not None, "seed+std missing hint")
    require(result.certificate["hilbert_seed_run"]["timed_out"] is False, "seed+std seed timed_out")
    require(result.certificate["runs"][0]["main"]["dimension"] == 0, "seed+std dim")
    require(result.certificate["runs"][0]["main"]["unit"] is False, "seed+std unit")


def test_run_hilbert_seed_does_not_raise() -> None:
    seed = SingularSystem(
        name="SEED_NO_RAISE",
        prelude='ring R=32003,(x,y,z),wp(1,1,1);\nsystem("sh","sleep 3");\n',
        generators=("x", "y", "z"),
        characteristic=32003,
        homogeneous=True,
        positive_weights=(1, 1, 1),
    )
    hint, run = run_hilbert_seed(seed, cfg("seed_no_raise", hilbert_seed_timeout_seconds=1), cpus=1)
    require(hint is None, "timed-out seed returned a hint")
    require(run.timed_out is True, "timed-out seed not flagged")
    require(run.timeout_stage == STAGE_HILBERT_SEED, "run_hilbert_seed stage")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    tests = [
        test_resolve_stage_timeout,
        test_policy_byte_identity,
        test_known_empty,
        test_known_nonempty,
        test_tame_automorphism,
        test_modular_unit_not_promoted,
        test_std_timeout_typed,
        test_hilbert_seed_timeout_typed,
        test_outer_watchdog_suppresses_inherited_cap,
        test_explicit_std_timeout_with_outer_watchdog,
        test_hilbert_seed_then_std_completes,
        test_run_hilbert_seed_does_not_raise,
    ]
    results = []
    failed = 0
    for fn in tests:
        name = fn.__name__
        started = time.monotonic()
        try:
            fn()
            elapsed = time.monotonic() - started
            line = f"PASS {name} {elapsed:.2f}s"
            print(line, flush=True)
            results.append({"name": name, "ok": True, "elapsed": round(elapsed, 3)})
        except Exception as exc:
            elapsed = time.monotonic() - started
            line = f"FAIL {name} {elapsed:.2f}s {exc}"
            print(line, flush=True)
            traceback.print_exc()
            results.append({"name": name, "ok": False, "elapsed": round(elapsed, 3), "error": str(exc)})
            failed += 1
    payload = {"failed": failed, "passed": len(tests) - failed, "results": results}
    (OUT.parent / "unit-test-results.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print("ALL PASS" if failed == 0 else f"{failed} FAILED", flush=True)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
