#!/usr/bin/env python3
"""Fail-closed validator for the dual-host V43 total-DVR experiment."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V42_RESULT = (
    ROOT
    / "cases/max12_812_order2_p0_total_rees_j2_a1_radical_cascade_closure_v42_20260827/RESULT.json"
)
V42_RESULT_SHA256 = "01b8edd2b699d7c4b65452ea6eba47a98bf25c1cd5a18022a035e2346c973566"
MODES = ("exact", "modp")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_clean_resource(path: Path) -> str:
    text = path.read_text()
    if text.count("Command being timed:") != 1 or text.count("Exit status: 0") != 1:
        fail(("resource contract", str(path)))
    if any(token in text for token in ("Traceback", "FAIL_", "Killed", "out of memory")):
        fail(("resource diagnostic", str(path)))
    return text


def require_no_diagnostics(*texts: str) -> None:
    bad = ("Traceback", "FAIL_", "Killed", "out of memory", "error occurred")
    for token in bad:
        if any(token in text for text in texts):
            fail(("diagnostic token", token))


def one_token(text: str, token: str) -> None:
    if text.count(token) != 1:
        fail(("token count", token, text.count(token)))


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--compiler-result", type=Path, required=True)
    cli.add_argument("--compiler-stdout", type=Path, required=True)
    cli.add_argument("--compiler-stderr", type=Path, required=True)
    cli.add_argument("--cascade-stdout", type=Path, required=True)
    cli.add_argument("--cascade-stderr", type=Path, required=True)
    cli.add_argument("--singular-stdout", type=Path)
    cli.add_argument("--singular-stderr", type=Path)
    cli.add_argument("--mode", choices=MODES, required=True)
    cli.add_argument("--prime", type=int, choices=(65519, 65521), required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()

    if digest(V42_RESULT) != V42_RESULT_SHA256:
        fail(("V42 result hash", digest(V42_RESULT), V42_RESULT_SHA256))
    expected_cascade = json.loads(V42_RESULT.read_text())
    cascade_text = args.cascade_stdout.read_text()
    cascade = json.loads(cascade_text)
    if cascade != expected_cascade:
        fail("V42 positive-control replay differs from frozen result")
    if (cascade.get("status") != "PASS-ORDERED-A1-RHO0-RAW-D-A1-EMPTY-THROUGH-G19"
            or cascade.get("named_row_count") != 70
            or cascade.get("mutation", {}).get("residual_term_count") != 1
            or cascade.get("mutation", {}).get("residual_sha256")
            != "bdbc1c36e9784a362722b59d51aae231baa0b0c878e0b97a36178b8cb1aa7cef"):
        fail("V42 original/corrupted-row control contract")
    cascade_resource = require_clean_resource(args.cascade_stderr)

    result = json.loads(args.compiler_result.read_text())
    if (result.get("status") != "PASS-A1-TOTAL-DVR-W30-V43-COMPILER"
            or result.get("mode") != args.mode
            or result.get("phase") != "solve"
            or result.get("selector_prime_requested") != args.prime):
        fail("compiler result contract")
    census = result.get("census", {})
    fixed_census = {
        "weight": 30,
        "exponent": 6,
        "named_rows": 70,
        "rho0_positive_variables": 65,
    }
    if any(census.get(key) != value for key, value in fixed_census.items()):
        fail(("fixed census", census))
    if (census.get("positive_variables", 0) < census["rho0_positive_variables"]
            or not isinstance(census.get("general_only_variables"), list)
            or census.get("total_component_products", 0) <= 0
            or census.get("total_component_monomials", 0) <= 0
            or census.get("rho0_component_monomials", 0) <= 0):
        fail(("structural census", census))

    compiler_text = args.compiler_stdout.read_text()
    compiler_resource = require_clean_resource(args.compiler_stderr)
    one_token(compiler_text, "V43_PREFLIGHT=")
    one_token(compiler_text, f"V43_RHO0_OUTCOME={result['rho0']['outcome']}")
    one_token(compiler_text, "PASS-A1-TOTAL-DVR-W30-V43-COMPILER")
    require_no_diagnostics(cascade_text, cascade_resource, compiler_text, compiler_resource)

    rho0 = result.get("rho0", {})
    if rho0.get("outcome") not in {"member", "nonmember"}:
        fail(("rho0 outcome", rho0))
    expected_tier = "exact-Q-leaf-dual" if args.mode == "exact" else "finite-field-screen"
    if rho0.get("evidence_tier") != expected_tier:
        fail(("rho0 tier", rho0))

    final = {
        "status": "PASS-A1-TOTAL-DVR-W30-V43",
        "mode": args.mode,
        "selector_prime": args.prime,
        "compiler_result_sha256": digest(args.compiler_result),
        "compiler_stdout_sha256": digest(args.compiler_stdout),
        "compiler_resource_sha256": digest(args.compiler_stderr),
        "v42_positive_control_stdout_sha256": digest(args.cascade_stdout),
        "v42_positive_control_resource_sha256": digest(args.cascade_stderr),
        "v42_corrupted_row_residual_sha256": cascade["mutation"]["residual_sha256"],
        "census": census,
        "rho0_outcome": rho0["outcome"],
        "total_dvr_outcome": "not-run-rho0-nonmember",
        "conclusion_strength": (
            "exact-Q exponent-six total certificate excluded already on rho=0"
            if args.mode == "exact" and rho0["outcome"] == "nonmember"
            else "finite-field screen only; no characteristic-zero conclusion"
        ),
    }

    if rho0["outcome"] == "nonmember":
        if result.get("total_dvr_required") or result.get("singular_script") is not None:
            fail("unexpected DVR script after rho0 nonmembership")
        if args.singular_stdout is not None or args.singular_stderr is not None:
            fail("unexpected Singular evidence after rho0 nonmembership")
    else:
        if (not result.get("total_dvr_required") or not result.get("singular_script")
                or args.singular_stdout is None or args.singular_stderr is None):
            fail("missing required DVR evidence")
        singular_script = Path(result["singular_script"])
        if digest(singular_script) != result.get("singular_script_sha256"):
            fail("Singular source hash")
        singular_text = args.singular_stdout.read_text()
        singular_resource = require_clean_resource(args.singular_stderr)
        require_no_diagnostics(singular_text, singular_resource)
        one_token(singular_text, "V43_DVR_TOY_CONTROLS=1")
        one_token(singular_text, "PASS_A1_TOTAL_DVR_W30_V43_SINGULAR")
        outcomes = re.findall(r"^V43_DVR_OUTCOME=(member|nonmember)$", singular_text,
                              flags=re.MULTILINE)
        if len(outcomes) != 1:
            fail(("DVR outcome token", outcomes))
        dvr_outcome = outcomes[0]
        final.update({
            "total_dvr_outcome": dvr_outcome,
            "singular_script_sha256": digest(singular_script),
            "singular_stdout_sha256": digest(args.singular_stdout),
            "singular_resource_sha256": digest(args.singular_stderr),
        })
        if dvr_outcome == "member":
            one_token(singular_text, "V43_DVR_UNIT_CONSTANT=1")
            certificate = args.compiler_result.parent / "dvr_syzygy_certificate.txt"
            unit = args.compiler_result.parent / "dvr_unit_factor.poly"
            if not certificate.is_file() or not unit.is_file():
                fail("missing exact DVR certificate files")
            final.update({
                "dvr_syzygy_certificate_sha256": digest(certificate),
                "dvr_unit_factor_sha256": digest(unit),
                "conclusion_strength": (
                    "exact-Q certificate a1^6*U(rho^2) with U(0)=1 in the literal total rows"
                    if args.mode == "exact"
                    else "finite-field corroboration only; no characteristic-zero conclusion"
                ),
            })
        else:
            final["conclusion_strength"] = (
                "exact-Q exponent-six total DVR certificate excluded"
                if args.mode == "exact"
                else "finite-field screen only; no characteristic-zero conclusion"
            )

    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-TOTAL-DVR-W30-V43-VALIDATOR")


if __name__ == "__main__":
    main()
