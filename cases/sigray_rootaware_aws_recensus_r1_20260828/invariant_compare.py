#!/usr/bin/env python3
"""Strict equality gate for the before/after invariant inventories."""

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--before", required=True, type=Path)
    parser.add_argument("--after", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    before = json.loads(args.before.read_text())
    after = json.loads(args.after.read_text())
    keys = (
        "tdu_entry_inventory",
        "pinned_entry_inventory",
        "monodromy_rows",
        "ordinary_nonroot_graph",
        "af2_nonroot_graph",
        "hiii_nonroot_graph",
    )
    equality = {key: before[key] == after[key] for key in keys}
    controls = after["root_controls"]
    control_pass = controls == {
        "available": True,
        "root_unqualified": "TERMINAL_ROOT_M1",
        "root_certified_pole": "KILL_NR_M1",
        "nonroot_unqualified": "UNRESOLVED_M1_SCOPE",
        "nonroot_constructed": "KILL_NR_M1",
    }
    verdict = {
        "equality": equality,
        "root_pole_negative_control_pass": control_pass,
        "pass": all(equality.values()) and control_pass,
        "scope": (
            "CERTIFIED_NONROOT_TRANSITION_AND_SINGLETON_POLE_ENTRY_INVARIANT_ONLY; "
            "root terminals and OPEN/frontier ledgers deliberately excluded"
        ),
    }
    args.output.write_text(json.dumps(verdict, indent=2, sort_keys=True) + "\n")
    print(json.dumps(verdict, indent=2, sort_keys=True))
    if verdict["pass"]:
        print("BEFORE_AFTER_CERTIFIED_NONROOT_POLE_ENTRY_EXACT_PASS")
        return 0
    print("BEFORE_AFTER_INVARIANT_MISMATCH_NO_VERDICT")
    return 3


if __name__ == "__main__":
    raise SystemExit(main())

