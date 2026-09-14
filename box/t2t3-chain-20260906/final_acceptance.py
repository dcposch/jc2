#!/usr/bin/env python3
"""Strict, read-only acceptance audit for the three capped production receipts."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / "strict-acceptance.json"
CASES = {
    "99-delta2": {
        "result": "singular-full-graph-99-delta2.rss-retry.result.json",
        "driver": "singular_full_graph_rss_retry.py",
        "audit": "acyclic-graph-delta2.json",
        "audit_driver": "acyclic_graph_audit.py",
        "variables": 7585,
        "graph": 7136,
        "rows": 11606,
        "source_residuals": 0,
    },
    "99-delta52": {
        "result": "singular-full-graph-99-delta52.result.json",
        "driver": "singular_full_graph_remaining.py",
        "audit": "acyclic-graph-delta52.json",
        "audit_driver": "acyclic_graph_audit_remaining.py",
        "variables": 7583,
        "graph": 7136,
        "rows": 11606,
        "source_residuals": 0,
    },
    "108-free-mean": {
        "result": "singular-full-graph-108-free-mean.result.json",
        "driver": "singular_full_graph_remaining.py",
        "audit": "acyclic-graph-d108-free-mean.json",
        "audit_driver": "acyclic_graph_audit_remaining.py",
        "variables": 17815,
        "graph": 17308,
        "rows": 24330,
        "source_residuals": 14,
    },
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_case(tag: str, spec: dict) -> dict:
    result_path = HERE / spec["result"]
    audit_path = HERE / spec["audit"]
    result = json.loads(result_path.read_text())
    audit = json.loads(audit_path.read_text())
    assert result["case"] == tag
    assert result["decision"] == "COMPUTE_BOUND_OPEN"
    assert result["termination_reason"] == "AGGREGATE_RSS_CAP"
    assert result["strict_completion"] is False
    assert result["generator_count"] == spec["variables"]
    assert result["graph_generator_count"] == spec["graph"]
    assert result["row_count"] == spec["rows"]
    assert result["streamed_row_count"] < result["row_count"]
    assert result["peak_aggregate_RSS_bytes"] < 12 * 1024**3
    assert result.get("child_RLIMIT_AS") is None
    assert result.get("address_space_limit_set_by_retry", False) is False
    for marker in ["ALL_ROWS_PARSED", "BEGIN_GB", "BEGIN_RESULT", "END_RESULT", "BEGIN_CONTROLS", "END_CONTROLS"]:
        assert result["marker_counts"].get(marker, 0) == 0
    assert not result["result_lines"] and not result["controls_lines"]
    assert result["driver_sha256"] == sha(HERE / spec["driver"])
    assert audit["driver_sha256"] == sha(HERE / spec["audit_driver"])
    assert audit["presentation_generator_count"] == spec["variables"]
    assert audit["graph_generator_count"] == spec["graph"]
    assert audit["total_row_count"] == spec["rows"]
    assert audit["source_residual_rows"] == spec["source_residuals"]
    assert audit["all_graph_roundtrips_exact_zero"] is True
    if tag == "99-delta2":
        target = result["attained_target_row_audit"]
        assert target["complete_face_labels_exact"] is True
        assert target["raw_row_scalar_coefficients_exact"] is True
        assert target["primitive_rows_proportional_exact"] is True
        assert target["one_slot_perturbations_rejected"] is True
    else:
        assert result["emitted_face_rows_target_link_host_check"] is True
        assert result["target_vectors_host_check"] is True
        assert result["perturbed_target_rejected_host_check"] is True
        assert result["reverse_acyclic_order_host_check"] is True
    return {
        "decision": result["decision"],
        "termination_reason": result["termination_reason"],
        "rows_streamed": result["streamed_row_count"],
        "rows_total": result["row_count"],
        "peak_aggregate_RSS_MiB": result["peak_aggregate_RSS_MiB"],
        "result_sha256": sha(result_path),
        "driver_sha256": result["driver_sha256"],
        "audit_sha256": sha(audit_path),
        "audit_driver_sha256": audit["driver_sha256"],
        "target_row_link_host_check": True,
        "no_completion_markers": True,
    }


def main() -> None:
    checks = {tag: check_case(tag, spec) for tag, spec in CASES.items()}
    manifest_entries = []
    for line in (HERE / "inputs.sha256").read_text().splitlines():
        expected, name = line.split(None, 1)
        path = Path(name.strip())
        assert sha(path) == expected
        manifest_entries.append({"path": str(path), "sha256": expected})
    assert len(manifest_entries) == 6
    chart_path = HERE / "chart-spec.json"
    chart = json.loads(chart_path.read_text())
    assert chart["field"] == "Q"
    assert chart["no_raw_jacobian_tail"] is True
    assert chart["sub_100_active_variable_gate_met"] is False
    assert chart["canonical_triangular_map_status"] == "OPEN_NOT_SUPPLIED"
    for tag, spec in CASES.items():
        case = chart["cases"][tag]
        audit = json.loads((HERE / spec["audit"]).read_text())
        assert case["presentation_variables"] == spec["variables"]
        assert case["total_rows"] == spec["rows"]
        assert sum(case["row_blocks"].values()) == spec["rows"]
        assert case["T2_face_slots"] == audit["T2_face_slots"]
        assert case["T3_face_slots"] == audit["T3_face_slots"]
        assert case["T2_face_vector_sha256"] == audit["T2_face_vector_sha256"]
        assert case["T3_face_vector_sha256"] == audit["T3_face_vector_sha256"]
        assert case["source_input_sha256"] == audit["input_sha256"]
        assert case["full_unknowns_after_unit_equality_pivot"] == (
            case["semantic_variables_before_constraint_pivots"]
            - 1 + case["passive_affine_extension_dimension"]
        )
    report = ROOT / "xmodel/t2t3-chain-sol56-20260906.md"
    body = report.read_bytes()
    assert 12_000 <= len(body) <= 25_000
    assert body.count(b"<!-- BODY-END -->") == 1
    record = {
        "status": "PASS_THREE_COMPUTE_BOUND_OPEN_NO_PROMOTION",
        "field": "Q",
        "cases": checks,
        "report_bytes_at_audit": len(body),
        "report_sha256": sha(report),
        "report_unique_body_end": True,
        "frozen_input_manifest_checks": manifest_entries,
        "chart_spec_sha256": sha(chart_path),
        "chart_spec_cross_checks": "PASS",
        "driver_sha256": sha(Path(__file__)),
    }
    OUT.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
