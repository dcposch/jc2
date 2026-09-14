#!/usr/bin/env python3
"""Machine-readable summary of the batch-3 lane."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "g9966n1b3-20260903"


def load(p):
    p = HERE / p
    return json.loads(p.read_text()) if p.exists() else None


def sha(p):
    p = Path(p)
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None


custody = load("charged-inputs-check.json")
enum = load("enumeration.json")
face = load("face-screen.json")
faceb = load("face-screen-banked.json")
resolve = load("face-resolve.json")
duty = load("duty-ledger.json")
controls = load("controls/controls-summary.json")

builds = {}
for p in sorted((HERE / "build-runs").glob("*.json")):
    d = json.loads(p.read_text())
    builds[p.stem] = {"native_done": d["native_done"], "target_gate": d["target_gate"],
                      "row_count": d["row_count"], "rows_sha256": d["rows_sha256"],
                      "elapsed_seconds": d["elapsed_seconds"]}

reductions = {}
for p in sorted((HERE / "reduced").glob("*/reduce_*.json")):
    d = json.loads(p.read_text())
    if "cap_bytes" not in d:
        continue                     # superseded pre-patch run
    gate = p.parent / f"replay_{p.stem}.json"
    g = json.loads(gate.read_text()) if gate.exists() else None
    reductions[f"{p.parent.name}/{p.stem}"] = {
        "characteristic": d["characteristic"], "cap_bytes": d["cap_bytes"],
        "rows_used": d["rows_used"], "input_rows": d["input_rows"],
        "pivots": d["pivots"], "residual_rows": d["residual_rows"],
        "variables_in": d["variables_in"],
        "surviving_variable_count": d["surviving_variable_count"],
        "residual_sha256": d["residual_sha256"],
        "replay_gate": (g or {}).get("status"),
        "replay_multisets_equal": (g or {}).get("multisets_equal"),
    }

fullmaps = {}
for p in sorted((HERE / "reduced").glob("*/full_map_*.json")):
    d = json.loads(p.read_text())
    fullmaps[f"{p.parent.name}/{p.stem}"] = {
        "characteristic": d["characteristic"], "big_rows": d["big_rows"],
        "total_reduced_rows": d["total_reduced_rows"],
        "surviving_variable_count": d["surviving_variable_count"],
        "residual_full_sha256": d["residual_full_sha256"], "done": d["done"]}

decisions = {}
for p in sorted(HERE.glob("reduced/*/fullgb_*.log")):
    text = p.read_text(errors="replace")
    get = lambda k: next((ln.split("=", 1)[1] for ln in text.splitlines()
                          if ln.startswith(k + "=")), None)
    decisions[f"{p.parent.name}/{p.stem}"] = {
        "generators": get("GENS"), "unit": get("UNIT"), "dim": get("DIM"),
        "basis_size": get("SIZE"), "finished": "FULLGB_DONE" in text}

payload = {
    "schema": "jc2.g9966n1b3.results/v1",
    "lane": "g9966-n1-batch3-opus5-20260903",
    "verdict": "PARTIAL",
    "census": {"dead": ["S5", "S6", "S8"], "open": ["S1", "S2", "S3", "S4", "S7"],
               "total": 8, "changed_this_lane": False},
    "claims": {
        "no_keller_pair_9966": False,
        "n1_closed": False,
        "new_skeleton_death": False,
        "split_leaf_enumeration_certified": True,
        "s8_branch_exhaustiveness_certified": True,
    },
    "charged_inputs_ok": (custody or {}).get("ok"),
    "charged_inputs_count": (custody or {}).get("count"),
    "enumeration_rows": (enum or {}).get("count"),
    "face_screen": {
        "charts_examined": sum(len(v["charts"]) for v in face["rows"].values()) if face else None,
        "dead": sum(1 for v in face["rows"].values() for c in v["charts"]
                    if c["verdict"] == "DEAD") if face else None,
        "survivors_per_row_closed_form_only": {k: len(v["survivors"])
                                               for k, v in face["rows"].items()} if face else None,
        "survivors_per_row_after_mixed_resolve": {k: v["split_leaf_count"]
                                                  for k, v in duty["rows"].items()}
        if duty else None,
        "note": ("face-screen.json counts only the leaves whose q has the closed form "
                 "w^A*(C+c0*int w^B); the four mixed low/high leaves are decided in "
                 "face-resolve.json and are included in the duty ledger"),
        "charged_comparison": (face or {}).get("charged_comparison"),
        "mixed_branch_resolved": [c["verdict"] for c in resolve["cases"]] if resolve else None,
        "banked_rows": {k: v["survivors"] for k, v in faceb["rows"].items()} if faceb else None,
    },
    "duty": {
        "split_leaves_total": sum(v["split_leaf_count"] for v in duty["rows"].values())
        if duty else None,
        "no_split_charts_total": sum(v["no_split_chart_count"] for v in duty["rows"].values())
        if duty else None,
        "per_row": {k: {"split_leaves": v["split_leaf_count"],
                        "no_split_charts": v["no_split_chart_count"]}
                    for k, v in duty["rows"].items()} if duty else None,
    },
    "builds": builds,
    "reductions": reductions,
    "full_maps": fullmaps,
    "decisions": decisions,
    "controls": controls,
    "artifact_sha256": {
        "enumeration.json": sha(HERE / "enumeration.json"),
        "face-screen.json": sha(HERE / "face-screen.json"),
        "face-screen-banked.json": sha(HERE / "face-screen-banked.json"),
        "face-resolve.json": sha(HERE / "face-resolve.json"),
        "duty-ledger.json": sha(HERE / "duty-ledger.json"),
        "charged-inputs.sha256": sha(HERE / "charged-inputs.sha256"),
    },
}
out = HERE / "results-summary.json"
out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print(json.dumps({"verdict": payload["verdict"], "charged_inputs_ok": payload["charged_inputs_ok"],
                  "face_screen": {k: v for k, v in payload["face_screen"].items()
                                  if k in ("charts_examined", "dead",
                                           "survivors_per_row_after_mixed_resolve")},
                  "duty": {k: v for k, v in payload["duty"].items() if k != "per_row"},
                  "builds_with_gate": sum(1 for b in builds.values() if b["target_gate"]),
                  "reductions": len(reductions),
                  "results_summary_sha256": sha(out)}, indent=1))
