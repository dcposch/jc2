#!/usr/bin/env python3
"""Exactly expand the distinct direct factors of V43C3 final zero roots."""

from __future__ import annotations

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
DIAGNOSTIC_SHA256 = "bb7d8b9752362714a6f2694ac068ca5486e533bab8de17d910e0fb90fc30b2eb"
TAG_PREFIX = "max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_rebased_v43c3_factor_v43c3f_"
EXPECTED = {
    "assume:ee1": (721, [118, 118, 153, 153, 174, 371, 371, 427, 428, 428, 666]),
    "assume:rs2": (722, [118, 118, 153, 153, 174, 371, 371, 371, 399, 428, 428, 666]),
    "assume:ez3": (723, [118, 118, 153, 153, 174, 371, 371, 371, 401, 428, 428, 666]),
}


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
        fail("registered V43C3F AWS lane required")
    return tag


class DiagnosticStop(Exception):
    pass


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: diagnose_factors_v43c3f.py OUTPUT")
    tag = require_aws()
    output = Path(sys.argv[1]).resolve()
    if digest(PRODUCER) != PRODUCER_SHA256:
        fail(("V43C3 producer pin", digest(PRODUCER), PRODUCER_SHA256))
    spec = importlib.util.spec_from_file_location("frozen_v43c3_for_factor_diagnostic", PRODUCER)
    if spec is None or spec.loader is None:
        fail("V43C3 import")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    def intercept(kernel, certificate, labels):
        observed = {}
        for label in labels:
            root = certificate.terms[label]
            node = kernel.e.nodes[root]
            if node.get("op") != "Mul":
                fail(("expected direct Mul root", label, root, node))
            observed[label] = (root, node["args"])
        if observed != EXPECTED:
            fail(("registered root/factor mismatch", observed, EXPECTED))
        factors = sorted({factor for _, args in observed.values() for factor in args})
        record = {
            "status": "IN_PROGRESS-V43C3F-EXACT-FACTOR-DIAGNOSTIC-ONLY",
            "not_a_certificate": True,
            "registered_aws_lane": tag,
            "producer_sha256": PRODUCER_SHA256,
            "v43c3d_diagnostic_sha256": DIAGNOSTIC_SHA256,
            "registered_roots": {
                label: {"root": root, "factors": args}
                for label, (root, args) in sorted(observed.items())
            },
            "factor_results": [],
        }
        path = output / "factor_expansions.json"
        for factor in factors:
            polynomial, telemetry = kernel.e.expand_exact(factor)
            item = {
                "factor": factor,
                "node": kernel.e.nodes[factor],
                "is_zero": not polynomial,
                **telemetry,
            }
            record["factor_results"].append(item)
            path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
            print("FACTOR", factor, "ZERO" if not polynomial else "NONZERO",
                  telemetry["expanded_term_count"], telemetry["expanded_sha256"],
                  flush=True)
        record["status"] = "PASS-V43C3F-EXACT-TOP-LEVEL-FACTOR-DIAGNOSTIC-ONLY"
        path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
        print(record["status"])
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
    fail("V43C3F interception did not stop the producer")


if __name__ == "__main__":
    main()
