#!/usr/bin/env python3
"""V2 source compiler for the cyclic-D1 lower-fibre gate.

The frozen parent and a self-contained implementation reconstruct F6, F12,
the inverse root, and all eight tails by different algorithms.  Every plain
coefficient dictionary must agree before the D1 character descent is
consumed.  This file emits source rows only; it does not classify components
or decide Taylor polynomiality.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import argparse
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


ROOT = Path(__file__).resolve().parents[2]
PARENT_PATH = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
INDEPENDENT_PATH = Path(__file__).with_name("independent_reconstruct.py")

# The two FREEZE files missing from the V1 deployment closure are explicit.
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
    "cases/max12_high_row_probe_20260824/FREEZE.sha256":
        "3a25edb31a53ecee9c96e039ab4a947908ebc0542123fb131447e1a661f45a28",
    "cases/max12_partial_y_preflight_20260824/FREEZE.sha256":
        "59ef0712aea2424ea57b6f1727031018e769701b0f2e2384eb4638f4286ea558",
    "cases/max12_912_order3_fibre_20260824/order3_fibre.py":
        "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf",
    "cases/max12_912_order3_terminal_belyi_classification_20260824/replay.py":
        "495844f1d51c0f230223d143f36b54679865244581fb60974c268da4c756a4bb",
    "xmodel/max12-912-order3-nu-q8-hurwitz-support-taylor-freeness-20260824.md":
        "ac8d8d4a53423255d564c6fdbecaf14b0dac3c23025a5156f4f6863a77bd4978",
    "xmodel/max12-912-order3-nu-q8-selected-contact-positive-genus-exclusion-repaired-v2-20260825.md":
        "d7e73783191d70a86e5c8786b735d0a596034c1d492559049d13433b8e889209",
    "xmodel/max12-912-order3-nu-q8-selected-contact-positive-genus-exclusion-repaired-v2-review-grok-20260825.md":
        "f8d5208d9e915f694a9df1c9ae9014612e87c172b794c94bbfcf30f98bdb7996",
    "cases/max12_912_order3_d1_passport_full_fibre_taylor_20260825/PREREGISTRATION.md":
        "41385708ea2ab969b6d08ead5a48d3be4fabe20d980167528fe45840fd5137d4",
    "cases/max12_912_order3_d1_passport_full_fibre_taylor_20260825/compile_gate.py":
        "31eb50ad836bd5306c21e64f25ec5e3f007dba0fa1b6dc00e108b962a494fd74",
    "cases/max12_912_order3_d1_passport_full_fibre_taylor_20260825/SOURCE_CLOSURE.sha256":
        "87701de7a1f602e36e87a5f59a5962936af2094e5beb125de7965721aa41575d",
    "cases/max12_912_order3_d1_passport_full_fibre_taylor_20260825/FREEZE.sha256":
        "72aef439e5816479b1ebb641496f216a51b946b49b3c0bbce53e3238a83efaf6",
}


class GateV2Failure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor_path = Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text().strip() if vendor_path.is_file() else ""
    if vendor != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def pin_inputs() -> dict[str, str]:
    pinned: dict[str, str] = {}
    for relative, expected in EXPECTED_HASHES.items():
        got = sha256((ROOT / relative).read_bytes()).hexdigest()
        if got != expected:
            raise GateV2Failure(("input hash mismatch", relative, got, expected))
        pinned[relative] = got
    return pinned


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise GateV2Failure(("cannot load", str(path)))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def build_parent_reference(parent):
    m, n = 9, 12
    names = [f"a{i}" for i in range(8)] + ["k"]
    ring = parent.M.Ring(names)
    one = ring.one
    U = {index - m: ring.var(f"a{index}") for index in range(8)}
    f6 = parent.faber(ring, m, 6, U)
    f12 = parent.faber(ring, m, 12, U)
    g = parent.M.zadd(
        f12,
        {exponent: parent.M.cmul(ring.var("k"), coefficient)
         for exponent, coefficient in f6.items()},
    )
    inverse_root = parent.inverse_root(ring, m, n + 7)
    tails = {}
    for ell in range(1, 9):
        coefficient = {}
        for z_exponent, g_coefficient in g.items():
            coefficient = parent.M.cadd(
                coefficient,
                parent.M.cmul(
                    g_coefficient,
                    parent.M.zpower_coefficient(
                        inverse_root, z_exponent, -ell, one
                    ),
                ),
            )
        tails[ell] = parent.M.cscale(-1, coefficient)
    return ring, {"F6": f6, "F12": f12, "g": g,
                  "inverse_root": inverse_root, "tails": tails}


def compare_reconstructions(parent, independent):
    ring, reference = build_parent_reference(parent)
    independent_output = independent.build()
    if tuple(ring.names) != independent_output["names"]:
        raise GateV2Failure("coefficient-ring disagreement")
    for label in ("F6", "F12", "g", "inverse_root"):
        if reference[label] != independent_output[label]:
            raise GateV2Failure(("independent reconstruction mismatch", label))
    for ell in range(1, 9):
        if reference["tails"][ell] != independent_output["tails"][ell]:
            raise GateV2Failure(("independent tail mismatch", ell))

    return ring, reference, independent_output


def compile_all():
    pinned = pin_inputs()
    parent = load_module(PARENT_PATH, "d1_v2_frozen_parent")
    independent = load_module(INDEPENDENT_PATH, "d1_v2_independent")
    parent_transitive = parent.pin_inputs()
    ring, reference, independent_output = compare_reconstructions(
        parent, independent
    )
    M = parent.M

    # D1 descent.  With sigma(u)=zeta*u and t=r8, sigma(t)=zeta^2*t.
    # Hence a_i=t^(i mod 3)A_i(s), but r_l is divided by t^(2l mod 3).
    descended_ring = M.Ring([f"A{i}" for i in range(8)]
                            + ["s", "k", "mu", "nu"])
    coefficient_exponents = tuple(index % 3 for index in range(8))
    tail_exponents = (0, 2, 1)

    def descend(value, ell: int, wrong: bool = False):
        quotient_exponent = ell % 3 if wrong else tail_exponents[ell % 3]
        out = {}
        failures = 0
        for monomial, scalar in value.items():
            t_power = sum(monomial[index] * coefficient_exponents[index]
                          for index in range(8))
            if (t_power < quotient_exponent
                    or (t_power - quotient_exponent) % 3):
                failures += 1
                continue
            s_power = (t_power - quotient_exponent) // 3
            new_monomial = tuple(monomial[:8]) + (
                s_power, monomial[8], 0, 0
            )
            out[new_monomial] = out.get(new_monomial, Fraction(0)) + scalar
        return M.cclean(out), failures

    rows = {}
    wrong_failures = 0
    for ell in range(1, 9):
        rows[ell], failures = descend(independent_output["tails"][ell], ell)
        if failures:
            raise GateV2Failure(("correct character descent failed", ell))
        _, failures = descend(independent_output["tails"][ell], ell, wrong=True)
        wrong_failures += failures
    if wrong_failures == 0:
        raise GateV2Failure("swapped-character negative did not fail")

    rows[3] = M.cadd(rows[3], M.cscale(-1, descended_ring.var("mu")))
    rows[6] = M.cadd(rows[6], M.cscale(-1, descended_ring.var("nu")))
    rows[8] = M.cadd(rows[8], M.cscale(-1, descended_ring.one))

    payload = {
        "input_hashes": pinned,
        "parent_transitive_hashes": parent_transitive,
        "independent_reconstruction": {
            "algorithms": [
                "parent frozen binomial Faber + recursive target coefficient",
                "independent differential Faber recurrence + iterative convolution",
            ],
            "F6_equal": True,
            "F12_equal": True,
            "g_equal": True,
            "inverse_root_equal": True,
            "all_eight_tails_equal": True,
            "digests": {
                "F6": independent.laurent_digest(independent_output["F6"]),
                "F12": independent.laurent_digest(independent_output["F12"]),
                "g": independent.laurent_digest(independent_output["g"]),
                "inverse_root": independent.laurent_digest(
                    independent_output["inverse_root"]
                ),
                "tails": {str(ell): independent.coefficient_digest(value)
                          for ell, value in
                          independent_output["tails"].items()},
            },
        },
        "convention": {
            "sigma": "sigma(u)=zeta*u; sigma(t)=zeta^2*t",
            "coefficient_exponents": list(coefficient_exponents),
            "tail_quotient_exponents": list(tail_exponents),
            "wrong_character_failures": wrong_failures,
        },
        "ring_names": list(descended_ring.names),
        "row_strings": {f"R{ell}": M.coeff_string(rows[ell], descended_ring.names)
                        for ell in range(1, 9)},
        "row_sha256": {f"R{ell}": M.coefficient_digest(rows[ell])
                       for ell in range(1, 9)},
        "row_supports": {f"R{ell}": len(rows[ell])
                         for ell in range(1, 9)},
        "scope": (
            "source equality and D1 incidence rows only; no component, "
            "section, Taylor, existence, or exclusion theorem"
        ),
    }
    return parent, M, descended_ring, rows, payload


def generic_singular(M, ring, rows, engine: str) -> str:
    variables = ",".join(f"A{i}" for i in range(8))
    lines = [
        'LIB "primdec.lib";',
        f"ring R=(0,s,k,mu,nu),({variables}),dp;",
        "option(redSB);",
    ]
    for ell in range(1, 9):
        lines.append(f"poly R{ell}={M.coeff_string(rows[ell], ring.names)};")
    lines.extend([
        "ideal I=R1,R2,R3,R4,R5,R6,R7,R8;",
        f"ideal G={engine}(I);",
        'print("PASS-D1-V2-GENERIC-ROW-LOAD");',
        'print("generic_dim="+string(dim(G)));',
        'print("generic_vdim="+string(vdim(G)));',
        'print("generic_degree="+string(mult(G)));',
        'print("STATUS=NAVIGATION_ONLY_ABSOLUTE_CONSTANT_FIELD_NOT_CERTIFIED");',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--singular-generic", action="store_true")
    parser.add_argument("--engine", choices=("std", "slimgb"), default="slimgb")
    args = parser.parse_args()
    tag = require_aws()
    _, M, ring, rows, payload = compile_all()
    if args.singular_generic:
        print(generic_singular(M, ring, rows, args.engine), end="")
        return
    payload["aws_tag"] = tag
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-D1-V2-INDEPENDENT-SOURCE-EQUALITY")
    print(f"payload_sha256={sha256(canonical.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
