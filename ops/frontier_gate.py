#!/usr/bin/env python3
"""Fail-closed classical admissibility gate for new JC2 compute lanes.

This gate deliberately implements only the primary-source-checked
Guccione--Guccione--Valqui/Heitmann necessary condition

    gcd(deg_total(P), deg_total(Q)) >= 16

for a characteristic-zero counterexample.  Passing means only that this
single classical theorem does not close the registered degree scope.
"""

from __future__ import annotations

import argparse
import json
import math
import sys


THEOREM = "GGV-Heitmann-gcd16"
SOURCE = "https://arxiv.org/abs/1401.1784"


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    scope = p.add_mutually_exclusive_group(required=True)
    scope.add_argument(
        "--total-degrees",
        nargs=2,
        type=int,
        metavar=("DEG_P", "DEG_Q"),
        help="fixed actual total-degree pair",
    )
    scope.add_argument(
        "--total-cap",
        type=int,
        metavar="D",
        help="both actual total degrees are at most D",
    )
    scope.add_argument(
        "--partial-y-degrees",
        nargs=2,
        type=int,
        metavar=("DEGY_P", "DEGY_Q"),
        help="partial-y degree pair; requires --total-unbounded",
    )
    p.add_argument(
        "--total-unbounded",
        action="store_true",
        help="certify that no finite total/x-degree cap is imposed",
    )
    p.add_argument(
        "--purpose",
        choices=("frontier", "method-control"),
        default="frontier",
        help="frontier lanes fail if classically closed; controls are labelled",
    )
    p.add_argument("--tag", required=True, help="registered unique lane tag")
    return p


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)

    supplied = args.total_degrees or args.partial_y_degrees
    values = supplied if supplied is not None else [args.total_cap]
    if any(value is None or value <= 0 for value in values):
        parser().error("all degrees and caps must be positive integers")
    if args.partial_y_degrees and not args.total_unbounded:
        parser().error("--partial-y-degrees requires --total-unbounded")
    if args.total_unbounded and not args.partial_y_degrees:
        parser().error("--total-unbounded is valid only with --partial-y-degrees")

    closed = False
    reason: str
    registered_scope: dict[str, object]

    if args.total_degrees:
        deg_p, deg_q = args.total_degrees
        degree_gcd = math.gcd(deg_p, deg_q)
        closed = degree_gcd < 16
        registered_scope = {
            "kind": "fixed_actual_total_degrees",
            "deg_total_P": deg_p,
            "deg_total_Q": deg_q,
            "gcd": degree_gcd,
        }
        reason = (
            f"gcd({deg_p},{deg_q})={degree_gcd}<16"
            if closed
            else f"gcd({deg_p},{deg_q})={degree_gcd}; this gate is inconclusive"
        )
    elif args.total_cap is not None:
        cap = args.total_cap
        closed = cap < 16
        registered_scope = {"kind": "common_total_degree_cap", "cap": cap}
        reason = (
            f"both total degrees are <= {cap}<16, hence their gcd is <16"
            if closed
            else f"the cap {cap} permits gcd >=16; this gate is inconclusive"
        )
    else:
        deg_y_p, deg_y_q = args.partial_y_degrees
        registered_scope = {
            "kind": "partial_y_only_total_unbounded",
            "deg_y_P": deg_y_p,
            "deg_y_Q": deg_y_q,
        }
        reason = (
            "partial-y bounds do not bound actual total degrees; "
            "the total-degree gcd theorem is inconclusive"
        )

    if closed and args.purpose == "frontier":
        verdict = "REFUSE_CLASSICALLY_CLOSED"
        exit_code = 3
    elif closed:
        verdict = "METHOD_CONTROL_ONLY"
        exit_code = 0
    else:
        verdict = "NOT_CLOSED_BY_THIS_GATE"
        exit_code = 0

    print(
        json.dumps(
            {
                "tag": args.tag,
                "purpose": args.purpose,
                "registered_scope": registered_scope,
                "theorem": THEOREM,
                "source": SOURCE,
                "verdict": verdict,
                "reason": reason,
                "warning": (
                    "NOT_CLOSED_BY_THIS_GATE is not evidence that the scope "
                    "contains a counterexample or is otherwise viable"
                ),
            },
            sort_keys=True,
        )
    )
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
