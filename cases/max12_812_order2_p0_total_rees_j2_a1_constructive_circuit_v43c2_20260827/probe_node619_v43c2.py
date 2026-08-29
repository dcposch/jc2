#!/usr/bin/env python3
"""Exact AWS probe of the geometric factor in the final crossed coefficient."""

from __future__ import annotations

from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PRODUCER = HERE / "replay_constructive_circuit_v43c2.py"
PRODUCER_SHA256 = "7d8c9635c16c0642341bd446745300b7bd8ec9dce3dd6d402f50660340ee5a90"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


class ProbeComplete(Exception):
    pass


def main() -> None:
    if len(sys.argv) != 2:
        raise RuntimeError("one output directory required")
    if digest(PRODUCER) != PRODUCER_SHA256:
        raise RuntimeError(("producer pin", digest(PRODUCER), PRODUCER_SHA256))
    spec = importlib.util.spec_from_file_location("frozen_v43c2_probe_source", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("producer import")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    output = Path(sys.argv[1]).resolve()

    def probe(kernel, certificate, labels):
        if labels != ["assume:e1"]:
            raise RuntimeError(("unexpected prune probe", labels))
        root = certificate.terms[labels[0]]
        root_node = kernel.e.nodes[root]
        if root_node.get("op") != "Mul":
            raise RuntimeError(("cross root op", root, root_node))
        candidates = [
            index for index in root_node["args"]
            if kernel.e.nodes[index].get("op") == "Add"
            and len(kernel.e.nodes[index].get("args", [])) == 3
        ]
        if len(candidates) != 1:
            raise RuntimeError(("geometric-factor isolation", root, candidates,
                                root_node))
        factor = candidates[0]
        polynomial, telemetry = kernel.e.expand_exact(factor)
        ell_zero = kernel.p.substitute(polynomial, {"ell1": {}})
        expected = kernel.p.power(kernel.p.variable("a1"), 36)
        kernel.p.assert_equal("node619 ell1-zero specialization", ell_zero,
                              expected)
        is_zero = not polynomial
        if is_zero:
            raise RuntimeError("node619 unexpectedly zero despite a1^36 specialization")
        result = {
            "status": "PASS-V43C2-NODE619-EXACT-NONZERO-DIAGNOSTIC",
            "conclusion": "the final crossed assume:e1 coefficient is not zero",
            "crossed_label": labels[0],
            "crossed_root": root,
            "crossed_root_node": root_node,
            "geometric_factor_root": factor,
            "geometric_factor_node": kernel.e.nodes[factor],
            "semantic_factor": "K=a1^36+a1^18*m*ell1+(m*ell1)^2",
            "specialization": "K|_(ell1=0)=a1^36",
            "factor_zero": False,
            "exact_expansion": telemetry,
            "producer_sha256": PRODUCER_SHA256,
        }
        path = output / "node619_probe.json"
        path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
        print("V43C2_NODE619_ZERO=0")
        print("V43C2_NODE619_TERMS=" + str(telemetry["expanded_term_count"]))
        print("PASS-V43C2-NODE619-EXACT-NONZERO-DIAGNOSTIC")
        print("RESULT_SHA256=" + digest(path))
        raise ProbeComplete

    module.Kernel.prune_zero_terms = probe
    old_argv = sys.argv
    sys.argv = [str(PRODUCER), str(output)]
    try:
        module.main()
    except ProbeComplete:
        return
    finally:
        sys.argv = old_argv
    raise RuntimeError("producer reached theorem output before node619 probe")


if __name__ == "__main__":
    main()

