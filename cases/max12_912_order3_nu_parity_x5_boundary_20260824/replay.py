#!/usr/bin/env python3
"""Exact replay for the nu-loaded parity x5=0 boundary and A chart."""

from __future__ import annotations

from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
PARENT_SHA256 = "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"


def load_parent():
    if sha256(PARENT.read_bytes()).hexdigest() != PARENT_SHA256:
        raise RuntimeError("parent compiler hash mismatch")
    spec = importlib.util.spec_from_file_location("max12_parity_x5_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load parent compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parent = load_parent()
    M = parent.M
    compiled = parent.compile_fibre()
    source_names = compiled["transverse_ring_names"]

    parity_names = ["x1", "x3", "x5", "p"]
    parity_ring = M.Ring(parity_names)
    parity_images = [
        parity_ring.var(name)
        if name in parity_names
        else M.cscale(0, parity_ring.one)
        for name in source_names
    ]
    tails = {
        ell: parent.substitute_coeff(value, parity_images, parity_ring)
        for ell, value in compiled["transverse_tails"].items()
    }
    assert all(not tails[ell] for ell in (1, 3, 5, 7))

    # x5=0 and nu!=0.  If x3=0, r4=(2/9)x1^2 forces x1=0,
    # and then r6=0.  Hence x3!=0, and r2=0 solves x1=p*x3.
    zero_x3_ring = M.Ring(["x1", "p"])
    zero_x3_images = [
        zero_x3_ring.var("x1"),
        M.cscale(0, zero_x3_ring.one),
        M.cscale(0, zero_x3_ring.one),
        zero_x3_ring.var("p"),
    ]
    zero_x3_r4 = parent.substitute_coeff(tails[4], zero_x3_images, zero_x3_ring)
    zero_x3_r6 = parent.substitute_coeff(tails[6], zero_x3_images, zero_x3_ring)
    assert M.coeff_string(zero_x3_r4, zero_x3_ring.names) == "2/9*x1^2"
    assert M.coeff_string(zero_x3_r6, zero_x3_ring.names) == "-4/27*x1^2*p"

    branch_ring = M.Ring(["x3", "p"])
    branch_images = [
        M.cmul(branch_ring.var("p"), branch_ring.var("x3")),
        branch_ring.var("x3"),
        M.cscale(0, branch_ring.one),
        branch_ring.var("p"),
    ]
    branch_tails = {
        ell: parent.substitute_coeff(value, branch_images, branch_ring)
        for ell, value in tails.items()
    }
    assert all(not branch_tails[ell] for ell in (1, 2, 3, 4, 5, 7, 8))
    assert M.coeff_string(branch_tails[6], branch_ring.names) == "-4/81*x3^3"

    # The coefficient of x1 in r2 is (4/9)A, A=x3-2*p*x5.
    # On A=0, r2=-(4/81)*p*x5^3.  Its two branches are incompatible
    # with nu!=0, so elimination of x1 on A!=0 is reversible.
    a_ring = M.Ring(["x1", "x5", "p"])
    a_images = [
        a_ring.var("x1"),
        M.cscale(2, M.cmul(a_ring.var("p"), a_ring.var("x5"))),
        a_ring.var("x5"),
        a_ring.var("p"),
    ]
    a_r2 = parent.substitute_coeff(tails[2], a_images, a_ring)
    assert M.coeff_string(a_r2, a_ring.names) == "-4/81*x5^3*p"

    a_p0_ring = M.Ring(["x1", "x5"])
    a_p0_images = [
        a_p0_ring.var("x1"),
        M.cscale(0, a_p0_ring.one),
        a_p0_ring.var("x5"),
        M.cscale(0, a_p0_ring.one),
    ]
    a_p0_r6 = parent.substitute_coeff(tails[6], a_p0_images, a_p0_ring)
    assert not a_p0_r6

    payload = {
        "case": "max12_912_order3_nu_parity_x5_boundary_20260824",
        "parent_compiler_sha256": PARENT_SHA256,
        "parity_specialization": "q=x0=x2=x4=k=0",
        "odd_tail_rows": {f"r{ell}": 0 for ell in (1, 3, 5, 7)},
        "x5_zero_branch": {
            "forced_relation": "x1=p*x3",
            "r6": "-4/81*x3^3=nu",
            "r8": "0",
            "terminal_contradiction": "9*r8'=0 != j/u",
        },
        "reversible_next_chart": {
            "A": "x3-2*p*x5",
            "r2_on_A_zero": "-4/81*p*x5^3",
            "A_zero_consequence": "nu=0",
            "nu_nonzero_route": "A!=0; after x5=0 is killed, retain A*x5!=0",
        },
        "scope": (
            "exact parity x5=0 trajectory exclusion and A-chart reversal only; "
            "no parity exhaustion, generic fibre, Taylor, all-(9,12), or JC2 claim"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
