#!/usr/bin/env python3
"""Desk replay for the remaining cubic-branch monodromy distinction.

The geometric theorem says that the companion sheet gives one common
order-two subgroup on a formal/analytic neighbourhood of the connected
affine branch.  This replay checks the finite-group warning needed at the
next gate: that subgroup is intransitive, but its normal closure in S3 is
all of S3.  Thus normal generation by meridians is not the same as
generation by the branch-neighbourhood group.

No plane-curve realization or compactification theorem is encoded here.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import permutations


Permutation = tuple[int, int, int]
IDENTITY: Permutation = (0, 1, 2)


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[i]] for i in range(3))  # type: ignore[return-value]


def inverse(perm: Permutation) -> Permutation:
    result = [0, 0, 0]
    for index, value in enumerate(perm):
        result[value] = index
    return tuple(result)  # type: ignore[return-value]


def generated(generators: set[Permutation]) -> set[Permutation]:
    closure = {IDENTITY}
    changed = True
    while changed:
        changed = False
        for left in tuple(closure | generators):
            for right in tuple(closure | generators):
                product = compose(left, right)
                if product not in closure:
                    closure.add(product)
                    changed = True
    return closure


def orbit(group: set[Permutation], point: int) -> set[int]:
    return {element[point] for element in group}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutate-common-inertia-to-normal",
        action="store_true",
        help="deliberately identify the local subgroup with its normal closure",
    )
    args = parser.parse_args()

    s3 = set(permutations(range(3)))
    transposition: Permutation = (1, 0, 2)
    local = generated({transposition})
    conjugates = {
        compose(compose(element, transposition), inverse(element)) for element in s3
    }
    normal_closure = generated(conjugates)

    if args.mutate_common_inertia_to_normal:
        local = set(normal_closure)

    require(len(s3) == 6, "the ambient permutation group must be S3")
    require(len(local) == 2, "the common companion-fixing subgroup must have order two")
    require(
        len(orbit(local, 0)) < 3,
        "the common companion-fixing subgroup must be intransitive",
    )
    require(
        normal_closure == s3,
        "the normal closure of a transposition in S3 must be all of S3",
    )

    payload = {
        "status": "PASS-CUBIC-REDUCIBLE-BRANCH-NORMAL-CLOSURE-WARNING",
        "s3_order": len(s3),
        "common_local_subgroup_order": len(local),
        "common_local_subgroup_transitive": len(orbit(local, 0)) == 3,
        "transposition_conjugate_count": len(conjugates),
        "normal_closure_order": len(normal_closure),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
