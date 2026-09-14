#!/usr/bin/env python3
"""Fail-closed classical admissibility gate for new JC2 compute lanes.

Scope: characteristic-zero polynomial counterexample candidates P, Q in
K[x,y] whose Jacobian [P,Q] is a nonzero constant.  ``--total-degrees`` and
``--total-cap`` declare actual total degrees of that original polynomial pair,
not partial-y, weighted, Newton-polygon, normalized-representative, Laurent,
or transformed-chart degrees.  In particular, nonconstant-Jacobian ``J=x^k``
charts are outside this gate's actual-total-degree theorem scopes.

The gate implements two independently reported necessary conditions:

* the primary-source-checked Guccione--Guccione--Valqui/Heitmann condition
  ``gcd(deg_total(P), deg_total(Q)) >= 16``; and
* the cited external GGHV consequence that a counterexample's actual maximum
  total degree is at least 108.

The legacy ``theorem``, ``source``, ``verdict``, and ``reason`` output fields
retain their gcd-only meaning.  ``overall_verdict`` is the effective result
and refuses frontier compute when either implemented theorem excludes the
honestly registered scope.  An inconclusive result asserts neither openness
nor existence.  The external chain is trusted as cited, not internally
replayed, and this overlay is unreviewed pending a different-model gate.
"""

from __future__ import annotations

import argparse
import json
import math
import sys


THEOREM = "GGV-Heitmann-gcd16"
SOURCE = "https://arxiv.org/abs/1401.1784"

EXTERNAL_MIN_ACTUAL_MAX_DEGREE = 109
EXTERNAL_THEOREM = "GGHV-actual-max-total-degree-108"
EXTERNAL_SOURCE = "https://arxiv.org/abs/2204.14178v1"
EXTERNAL_SOURCE_PDF_SHA256 = (
    "ac18e80cc2391f204f73b908a6a6557eb1141d9fbb5ebdb9f6e0a22121db80bd"
)
TOOL_VERSION = "frontier-gate-external108-overlay-v1"
TOOL_REVIEW_STATUS = "UNREVIEWED_PENDING_DIFFERENT_MODEL_GATE"


def external_max_bound_excludes(actual_max_degree: int) -> bool:
    """Return whether the strict externally trusted <108 bound excludes it."""

    return actual_max_degree < EXTERNAL_MIN_ACTUAL_MAX_DEGREE


def purpose_verdict(closed: bool, purpose: str) -> tuple[str, int]:
    """Apply the lane purpose to one theorem or to their effective union."""

    if closed and purpose == "frontier":
        return "REFUSE_CLASSICALLY_CLOSED", 3
    if closed:
        return "METHOD_CONTROL_ONLY", 0
    return "NOT_CLOSED_BY_THIS_GATE", 0


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

    gcd_closed = False
    reason: str
    registered_scope: dict[str, object]
    actual_max_degree: int | None
    degree_context_measure: str

    if args.total_degrees:
        deg_p, deg_q = args.total_degrees
        degree_gcd = math.gcd(deg_p, deg_q)
        gcd_closed = degree_gcd < 16
        actual_max_degree = max(deg_p, deg_q)
        degree_context_measure = (
            "declared fixed actual total degrees of the original polynomial pair"
        )
        registered_scope = {
            "kind": "fixed_actual_total_degrees",
            "deg_total_P": deg_p,
            "deg_total_Q": deg_q,
            "gcd": degree_gcd,
        }
        reason = (
            f"gcd({deg_p},{deg_q})={degree_gcd}<16"
            if gcd_closed
            else f"gcd({deg_p},{deg_q})={degree_gcd}; this gate is inconclusive"
        )
    elif args.total_cap is not None:
        cap = args.total_cap
        gcd_closed = cap < 16
        actual_max_degree = cap
        degree_context_measure = (
            "declared inclusive cap on both actual total degrees of the original "
            "polynomial pair"
        )
        registered_scope = {"kind": "common_total_degree_cap", "cap": cap}
        reason = (
            f"both total degrees are <= {cap}<16, hence their gcd is <16"
            if gcd_closed
            else f"the cap {cap} permits gcd >=16; this gate is inconclusive"
        )
    else:
        deg_y_p, deg_y_q = args.partial_y_degrees
        actual_max_degree = None  # Partial-y values are not actual-total bounds.
        degree_context_measure = "no finite actual-total bound supplied"
        registered_scope = {
            "kind": "partial_y_only_total_unbounded",
            "deg_y_P": deg_y_p,
            "deg_y_Q": deg_y_q,
        }
        reason = (
            "partial-y bounds do not bound actual total degrees; "
            "the total-degree gcd theorem is inconclusive"
        )

    verdict, _legacy_exit_code = purpose_verdict(gcd_closed, args.purpose)

    if actual_max_degree is None:
        external_closed = False
        external_scope: dict[str, object] = {
            "criterion": (
                "actual_max_total_degree "
                f"< {EXTERNAL_MIN_ACTUAL_MAX_DEGREE}"
            ),
            "applicability": "OUT_OF_SCOPE_ACTUAL_TOTAL_UNBOUNDED",
            "registered_actual_max_total_degree": None,
        }
        external_conclusion = "OUT_OF_SCOPE_ACTUAL_TOTAL_UNBOUNDED"
        external_reason = (
            "partial-y bounds with unbounded total degree supply no actual "
            "maximum total-degree bound"
        )
    else:
        external_closed = external_max_bound_excludes(actual_max_degree)
        external_scope = {
            "criterion": (
                "actual_max_total_degree "
                f"< {EXTERNAL_MIN_ACTUAL_MAX_DEGREE}"
            ),
        }
        if args.total_degrees:
            external_scope["applicability"] = (
                "IN_SCOPE_FIXED_ACTUAL_TOTAL_DEGREES"
            )
            external_scope["registered_actual_max_total_degree"] = actual_max_degree
            if external_closed:
                external_conclusion = "EXCLUDED_BY_EXTERNAL_LT108"
                external_reason = (
                    "declared fixed actual maximum total degree "
                    f"{actual_max_degree}<108; the registered counterexample "
                    "scope is excluded"
                )
            else:
                external_conclusion = "INCONCLUSIVE_BY_EXTERNAL_MAX_BOUND"
                external_reason = (
                    "declared fixed actual maximum total degree "
                    f"{actual_max_degree} is not strictly below 108"
                )
        else:
            external_scope["applicability"] = (
                "IN_SCOPE_COMMON_ACTUAL_TOTAL_DEGREE_CAP"
            )
            external_scope["registered_actual_max_total_degree_upper_bound"] = (
                actual_max_degree
            )
            external_scope["upper_bound_inclusive"] = True
            if external_closed:
                external_conclusion = "EXCLUDED_BY_EXTERNAL_LT108"
                external_reason = (
                    f"the inclusive actual-total cap {actual_max_degree}<108; "
                    "every counterexample candidate in the registered scope is "
                    "excluded"
                )
            else:
                external_conclusion = "INCONCLUSIVE_BY_EXTERNAL_MAX_BOUND"
                external_reason = (
                    f"the inclusive actual-total cap {actual_max_degree} is not "
                    "strictly below 108, so the bound does not exclude the entire "
                    "registered scope"
                )

    overall_closed = gcd_closed or external_closed
    overall_verdict, exit_code = purpose_verdict(overall_closed, args.purpose)
    excluded_by = []
    if gcd_closed:
        excluded_by.append("GGV-Heitmann-gcd16")
    if external_closed:
        excluded_by.append(EXTERNAL_THEOREM)

    if overall_closed and args.purpose == "method-control":
        overall_reason = (
            "one or more implemented theorems exclude the registered "
            "counterexample scope; explicitly labelled method-control only"
        )
    elif overall_closed:
        overall_reason = (
            "frontier compute refused because one or more implemented theorems "
            "exclude the registered counterexample scope"
        )
    else:
        overall_reason = (
            "implemented theorem checks are inconclusive for this registration; "
            "this asserts neither openness nor existence"
        )

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
                "external_theorem": {
                    "name": EXTERNAL_THEOREM,
                    "statement": (
                        "every characteristic-zero polynomial counterexample "
                        "has actual maximum total degree at least 108"
                    ),
                    "source": EXTERNAL_SOURCE,
                    "source_pdf_sha256": EXTERNAL_SOURCE_PDF_SHA256,
                },
                "trust": {
                    "level": "CITED_EXTERNAL_THEOREM",
                    "interface": "AUDIT17(jjjjjjjjjjjj)",
                    "external_chain_internally_replayed": False,
                },
                "actual_degree_context": {
                    "ambient": "P,Q in K[x,y] over a characteristic-zero field",
                    "jacobian": "nonzero constant",
                    "degree_measure": degree_context_measure,
                    "declaration_verified_by_gate": False,
                    "transformed_chart_degrees_supported": False,
                },
                "scope": external_scope,
                "conclusion": external_conclusion,
                "external_reason": external_reason,
                "overall_verdict": overall_verdict,
                "overall_reason": overall_reason,
                "excluded_by": excluded_by,
                "tool_metadata": {
                    "version": TOOL_VERSION,
                    "review_status": TOOL_REVIEW_STATUS,
                    "manual_external_check_required": True,
                },
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
