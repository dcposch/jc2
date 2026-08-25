#!/usr/bin/env python3
"""AWS-only source adapter for the cyclic-D1 order-three realization gate.

This file performs no component classification.  It pins the reviewed Faber
lineage, imports the frozen eight-tail producer only as a source generator,
and converts the eight tails to the invariant D1 incidence rows.  Heavy CAS
consumers must use the emitted rows under PREREGISTRATION.md.
"""

from __future__ import annotations

from hashlib import sha256
import argparse
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


if platform.system() != "Linux":
    raise SystemExit("REFUSE_NON_LINUX")
AWS_TAG = os.environ.get("JC2_AWS_TAG", "")
if not AWS_TAG.startswith("max12_912_order3_d1_"):
    raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")


ROOT = Path(__file__).resolve().parents[2]
PARENT_PATH = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
EXPECTED_HASHES = {
    "xmodel/max12-partial-y-kummer-preflight-20260824.md":
        "30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07",
    "xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md":
        "2951856cabe309fe07f564693a6b48a38cd7108616ffe41305d9583611da90fe",
    "xmodel/max12-partial-y-shared-faber-probe-20260824.md":
        "d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036",
    "xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md":
        "e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c",
    "xmodel/max12-912-order3-global-terminal-belyi-classification-audit-20260825.md":
        "28f33b993726b4bd7441a79a8f4208983dbbd0c5e4113d839a78af1b8cc7b6c6",
    "xmodel/max12-912-order3-global-terminal-belyi-classification-review-grok-20260825.md":
        "5da99825e099232832b0cf91fc02b29cb9460a2f675e2a69ab1769f204cf9fc9",
    "cases/max12_high_row_probe_20260824/shared_faber_probe.py":
        "69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f",
    "cases/max12_912_order3_fibre_20260824/order3_fibre.py":
        "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf",
    "cases/max12_912_order3_terminal_belyi_classification_20260824/replay.py":
        "495844f1d51c0f230223d143f36b54679865244581fb60974c268da4c756a4bb",
}


class GateFailure(RuntimeError):
    pass


def pin_inputs() -> dict[str, str]:
    out: dict[str, str] = {}
    for rel, expected in EXPECTED_HASHES.items():
        got = sha256((ROOT / rel).read_bytes()).hexdigest()
        if got != expected:
            raise GateFailure(f"input hash mismatch {rel}: {got}")
        out[rel] = got
    return out


def load_parent():
    spec = importlib.util.spec_from_file_location("d1_frozen_order3_parent", PARENT_PATH)
    if spec is None or spec.loader is None:
        raise GateFailure("cannot load order-three parent")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def clean(coeff):
    return {mon: scalar for mon, scalar in coeff.items() if scalar}


def compile_rows():
    pinned = pin_inputs()
    parent = load_parent()
    # The parent's own transitive pins live in main(), so call them explicitly.
    parent_pins = parent.pin_inputs()
    compiled = parent.compile_fibre()
    M = parent.M
    ring = M.Ring([f"A{i}" for i in range(8)] + ["s", "k", "mu", "nu"])

    # sigma(u)=zeta*u and t=r8, so sigma(t)=zeta^2*t.
    # a_i=t^(i mod 3) A_i(s), while r_l/t^(2l mod 3) is invariant.
    a_exponents = tuple(i % 3 for i in range(8))
    tail_exponents = {0: 0, 1: 2, 2: 1}

    def descend(value, ell: int):
        eta = tail_exponents[ell % 3]
        out = {}
        for mon, scalar in value.items():
            if len(mon) != 9:
                raise GateFailure(("unexpected source monomial width", ell, mon))
            t_power = sum(mon[i] * a_exponents[i] for i in range(8))
            if t_power < eta or (t_power - eta) % 3:
                raise GateFailure(("character descent failure", ell, mon, t_power, eta))
            s_power = (t_power - eta) // 3
            new_mon = tuple(mon[:8]) + (s_power, mon[8], 0, 0)
            out[new_mon] = out.get(new_mon, 0) + scalar
        return clean(out)

    rows = {ell: descend(compiled["tails"][ell], ell) for ell in range(1, 9)}
    rows[3] = M.cadd(rows[3], M.cscale(-1, ring.var("mu")))
    rows[6] = M.cadd(rows[6], M.cscale(-1, ring.var("nu")))
    rows[8] = M.cadd(rows[8], M.cscale(-1, ring.one))

    # Fail-closed control: the incorrect same-index quotient must not pass.
    wrong_failures = 0
    for ell, value in compiled["tails"].items():
        wrong_eta = ell % 3
        for mon in value:
            t_power = sum(mon[i] * a_exponents[i] for i in range(8))
            if t_power < wrong_eta or (t_power - wrong_eta) % 3:
                wrong_failures += 1
    if wrong_failures == 0:
        raise GateFailure("swapped-character negative control did not fail")

    payload = {
        "aws_tag": AWS_TAG,
        "input_hashes": pinned,
        "parent_transitive_hashes": parent_pins,
        "convention": {
            "campaign_generator": "sigma(u)=zeta*u",
            "t": "t=r8; sigma(t)=zeta^2*t",
            "a_exponents_mod3": list(a_exponents),
            "tail_quotient_exponents_by_l_mod3": [0, 2, 1],
            "equivalent_generator": (
                "tau=sigma^2: tau(t)=zeta*t, tau(u)=zeta^2*u, "
                "tau(a_i)=zeta^i*a_i, tau(r_l)=zeta^(2l)*r_l"
            ),
        },
        "passport": {
            "D": 1,
            "e": 1,
            "s": "t^3=x/(x-1)",
            "x": "t^3/(t^3-1)",
            "r8": "t",
            "u": "t^2/(t^3-1)^2",
            "h": "x^2*(x-1)^4",
            "j": -3,
            "terminal_identity": "9*d(t)/dx=-3/u",
        },
        "ring_names": list(ring.names),
        "row_strings": {f"R{ell}": M.coeff_string(rows[ell], ring.names)
                        for ell in range(1, 9)},
        "row_sha256": {f"R{ell}": M.coefficient_digest(rows[ell])
                       for ell in range(1, 9)},
        "row_supports": {f"R{ell}": len(rows[ell]) for ell in range(1, 9)},
        "targets": {"R1": 0, "R2": 0, "R3": "mu", "R4": 0,
                    "R5": 0, "R6": "nu", "R7": 0, "R8": 1},
        "negative_control_wrong_character_failures": wrong_failures,
        "scope": (
            "source rows for the D1 incidence; no component, section, Taylor, "
            "existence, or exclusion result"
        ),
    }
    return parent, M, ring, rows, payload


def singular_generic(M, ring, rows) -> str:
    variables = ",".join(f"A{i}" for i in range(8))
    lines = [
        f"ring R=(0,s,k,mu,nu),({variables}),dp;",
        "option(redSB);",
    ]
    for ell in range(1, 9):
        lines.append(f"poly R{ell}={M.coeff_string(rows[ell], ring.names)};")
    lines.extend([
        "ideal I=R1,R2,R3,R4,R5,R6,R7,R8;",
        "ideal G=std(I);",
        'print("PASS-D1-GENERIC-ROW-LOAD");',
        'print("dimension="+string(dim(G)));',
        'print("vdimension="+string(vdim(G)));',
        'print("gb_size="+string(size(G)));',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--singular-generic", action="store_true")
    args = parser.parse_args()
    _, M, ring, rows, payload = compile_rows()
    if args.singular_generic:
        print(singular_generic(M, ring, rows), end="")
    else:
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        print(json.dumps(payload, sort_keys=True, indent=2))
        print("PASS-D1-PASSPORT-SOURCE-ADAPTER")
        print(f"payload_sha256={sha256(canonical.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
