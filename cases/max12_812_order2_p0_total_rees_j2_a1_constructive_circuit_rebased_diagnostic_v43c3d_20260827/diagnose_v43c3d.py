#!/usr/bin/env python3
"""Capture V43C3 final assumption roots without expanding or deleting them."""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_rebased_v43c3_20260827/replay_constructive_circuit_rebased_v43c3.py"
PRODUCER_SHA256 = "aece88b6a74ac207a031c5b996e8e8d804d2efd464c83a889a91114177aedeed"
TAG_PREFIX = "max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_rebased_v43c3d_"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith(TAG_PREFIX)):
        fail("registered V43C3D AWS lane required")
    return tag


class DiagnosticStop(Exception):
    pass


def structural_record(store, root: int) -> dict:
    seen: set[int] = set()
    stack = [(root, 0)]
    census: Counter[str] = Counter()
    max_depth = 0
    while stack:
        index, depth = stack.pop()
        max_depth = max(max_depth, depth)
        if index in seen:
            continue
        seen.add(index)
        node = store.nodes[index]
        census[node["op"]] += 1
        if node["op"] in ("Add", "Mul"):
            stack.extend((child, depth + 1) for child in node["args"])
        elif node["op"] in ("Scale", "Pow"):
            stack.append((node["arg"], depth + 1))
    root_node = store.nodes[root]
    return {
        "root": root,
        "root_node": root_node,
        "reachable_unique_nodes": len(seen),
        "op_census": dict(sorted(census.items())),
        "max_dag_depth_upper_bound": max_depth,
        "root_is_canonical_zero": root == store.zero,
        "root_is_canonical_one": root == store.one,
    }


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: diagnose_v43c3d.py OUTPUT")
    tag = require_aws()
    output = Path(sys.argv[1]).resolve()
    if digest(PRODUCER) != PRODUCER_SHA256:
        fail(("V43C3 producer pin", digest(PRODUCER), PRODUCER_SHA256))
    spec = importlib.util.spec_from_file_location("frozen_v43c3_for_diagnostic", PRODUCER)
    if spec is None or spec.loader is None:
        fail("V43C3 import")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    def intercept(kernel, certificate, labels):
        if not labels:
            fail("V43C3D expected at least one final assumption label")
        if sorted(labels) != labels or len(set(labels)) != len(labels):
            fail(("noncanonical diagnostic labels", labels))
        missing = [label for label in labels if label not in certificate.terms]
        if missing:
            fail(("diagnostic absent labels", missing))
        record = {
            "status": "PASS-V43C3D-NO-EXPANSION-DIAGNOSTIC-ONLY",
            "not_a_certificate": True,
            "registered_aws_lane": tag,
            "producer_sha256": PRODUCER_SHA256,
            "expression_node_count_at_intercept": len(kernel.e.nodes),
            "labels": [
                {
                    "label": label,
                    **structural_record(kernel.e, certificate.terms[label]),
                }
                for label in labels
            ],
            "all_certificate_term_labels": sorted(certificate.terms),
        }
        output.mkdir(parents=True, exist_ok=False)
        path = output / "surviving_assumption_roots.json"
        path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
        print("PASS-V43C3D-NO-EXPANSION-DIAGNOSTIC-ONLY")
        print("DIAGNOSTIC_SHA256=" + digest(path))
        raise DiagnosticStop

    module.Kernel.prune_zero_terms = intercept
    old_argv = sys.argv
    sys.argv = [str(PRODUCER), str(output)]
    try:
        module.main()
    except DiagnosticStop:
        return
    finally:
        sys.argv = old_argv
    fail("V43C3D interception did not stop the producer")


if __name__ == "__main__":
    main()
