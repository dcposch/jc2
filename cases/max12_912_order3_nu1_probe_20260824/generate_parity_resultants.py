#!/usr/bin/env python3
"""Emit the first fail-closed triangular resultants on the parity chart.

For ``nu=1`` the coefficient of ``x1`` in ``r2`` is proportional to
``A=x3-2*p*x5``.  On ``A=0``, the equations ``r2=r4=0`` force ``r6=0``;
hence every normalized parity solution lies in the reversible chart A!=0.
The emitted resultants eliminate x1 only.  Later eliminations must retain
their leading-coefficient factors until the A=0 unit certificate is checked.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
PARENT_SHA256 = "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"


def load_parent():
    if sha256(PARENT.read_bytes()).hexdigest() != PARENT_SHA256:
        raise RuntimeError("parent compiler hash mismatch")
    spec = importlib.util.spec_from_file_location("max12_order3_parity_res_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load parent compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--characteristic", type=int, default=32003)
    parser.add_argument(
        "--stage",
        choices=("first", "second", "third", "sparse"),
        default="first",
    )
    args = parser.parse_args()
    parent = load_parent()
    M = parent.M
    compiled = parent.compile_fibre()
    source_names = compiled["transverse_ring_names"]
    names = ["x1", "x3", "x5", "p"]
    ring = M.Ring(names)
    images = [
        ring.var(name) if name in names else M.cscale(0, ring.one)
        for name in source_names
    ]
    tails = {
        ell: parent.substitute_coeff(value, images, ring)
        for ell, value in compiled["transverse_tails"].items()
    }
    for ell in (1, 3, 5, 7):
        if tails[ell]:
            raise RuntimeError(("odd tail survives", ell))

    lines = [
        f"ring R={args.characteristic},(x1,x3,x5,p,rho),dp;",
    ]
    for ell in (2, 4, 6, 8):
        lines.append(f"poly r{ell}={M.coeff_string(tails[ell], names)};")
    lines.extend([
        "poly A=x3-2*p*x5;",
        "poly P4=resultant(r2,r4,x1);",
        "poly P6=resultant(r2,r6-1,x1);",
        "poly P8=resultant(r2,r8-rho,x1);",
    ])
    if args.stage == "first":
        lines.extend([
            'print("PASS-PARITY-FIRST-RESULTANTS");',
            'print("P4_terms="+string(size(P4)));',
            'print("P6_terms="+string(size(P6)));',
            'print("P8_terms="+string(size(P8)));',
            'print("P4_factorization="); factorize(P4);',
            'print("P6_factorization="); factorize(P6);',
            'print("P8_factorization="); factorize(P8);',
        ])
    else:
        lines.extend([
            # P4 has the already classified factor x5.  Division is exact;
            # this stage is licensed only on A*x5!=0.
            "poly Q4=P4/x5;",
            "poly R46=resultant(Q4,P6,x3);",
            "poly R48=resultant(Q4,P8,x3);",
        ])
        if args.stage == "second":
            lines.extend([
                'print("PASS-PARITY-SECOND-RESULTANTS");',
                'print("R46_terms="+string(size(R46)));',
                'print("R48_terms="+string(size(R48)));',
                'print("R46_factorization="); factorize(R46);',
                'print("R48_factorization="); factorize(R48);',
            ])
        elif args.stage == "third":
            lines.extend([
                # Both second resultants contain p^4*x5^10.  x5=0 is
                # terminally excluded, while p=0 remains a separate exact
                # boundary and is not consumed by this division.
                "poly S46=R46/(p^4*x5^10);",
                "poly S48=R48/(p^4*x5^10);",
                "poly H=resultant(S46,S48,x5);",
                'print("PASS-PARITY-THIRD-RESULTANT");',
                'print("H_terms="+string(size(H)));',
                'print("H_factorization="); factorize(H);',
            ])
        else:
            lines.extend([
                # A direct three-polynomial sparse resultant avoids matching
                # unrelated x3 roots from the two pairwise second resultants.
                'LIB "solve.lib";',
                (
                    f"ring S=({args.characteristic},p,rho),(x3,x5),lp;"
                ),
                "poly q4=imap(R,Q4);",
                "poly p6=imap(R,P6);",
                "poly p8=imap(R,P8);",
                "module RM=mp_res_mat(ideal(q4,p6,p8),0);",
                "poly hr=det(RM);",
                "number hn=numerator(leadcoef(hr));",
                f"ring T={args.characteristic},(p,rho),dp;",
                "poly H=imap(S,hn);",
                'print("PASS-PARITY-SPARSE-RESULTANT");',
                'print("H_terms="+string(size(H)));',
                'print("H_factorization="); factorize(H);',
            ])
    lines.append("quit;")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
