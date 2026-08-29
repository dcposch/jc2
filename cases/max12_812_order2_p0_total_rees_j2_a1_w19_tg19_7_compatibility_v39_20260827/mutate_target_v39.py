#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def fail(message: object) -> "None":
    raise RuntimeError(message)


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--result", type=Path, required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    raw = args.result.read_text()
    value = json.loads(raw)
    if raw != json.dumps(value, sort_keys=True, indent=2) + "\n" or args.output.exists():
        fail("mutation input/output contract")
    target = value["payload"]["target"]["polynomial"]["terms"]
    mutation = value["payload"]["negative_control"]
    wanted = mutation["deleted_monomial"]
    hits = [index for index, term in enumerate(target) if term["monomial"] == wanted]
    if len(hits) != 1 or target[hits[0]]["coefficient"] != mutation["deleted_coefficient"]:
        fail("registered deletion term")
    del target[hits[0]]
    args.output.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")
    print("MUTATED_ONE_NONZERO_TARGET_COEFFICIENT")


if __name__ == "__main__":
    main()
