#!/usr/bin/env python3
"""Custody-only R1 replay after the reviewed TRANSPORT.md errata fold.

The frozen producer is not modified.  This wrapper pins its exact verifier,
updates only the expected TRANSPORT.md digest, and requires the complete
mathematical output to remain byte-semantically equal to frozen RESULT.json.
"""

from __future__ import annotations

from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ORIGINAL = HERE / "verify.py"
ORIGINAL_SHA256 = "4dfe7c6dc1e873892f9128ac2712f319a8c85ffb051701ddafa442d779e11f28"
TRANSPORT_R1_SHA256 = "9750aa9d14650a22a410803022d42fa523e3993a21ee9a27714386fa1150047c"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> dict:
    assert digest(ORIGINAL) == ORIGINAL_SHA256
    assert digest(ROOT / "ladder/TRANSPORT.md") == TRANSPORT_R1_SHA256

    spec = spec_from_file_location("ggv_prototype_frozen_r0", ORIGINAL)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    changed = dict(module.SOURCE_PINS)
    assert changed["ladder/TRANSPORT.md"] == (
        "39a607c8935153c814cd51fb65a2f1c708a9e4ba5e1dd0f38f9c96401fc4a624"
    )
    changed["ladder/TRANSPORT.md"] = TRANSPORT_R1_SHA256
    module.SOURCE_PINS = changed

    observed = module.main()
    frozen = json.loads((HERE / "RESULT.json").read_text())
    observed_pins = observed.pop("source_pins")
    frozen_pins = frozen.pop("source_pins")
    assert set(observed_pins) == set(frozen_pins)
    assert {
        key: value for key, value in observed_pins.items()
        if key != "ladder/TRANSPORT.md"
    } == {
        key: value for key, value in frozen_pins.items()
        if key != "ladder/TRANSPORT.md"
    }
    assert observed_pins["ladder/TRANSPORT.md"] == TRANSPORT_R1_SHA256
    assert frozen_pins["ladder/TRANSPORT.md"] == (
        "39a607c8935153c814cd51fb65a2f1c708a9e4ba5e1dd0f38f9c96401fc4a624"
    )
    assert observed == frozen
    return {
        "status": "PASS",
        "scope": "custody-only TRANSPORT.md errata-fold replay",
        "original_verifier_sha256": ORIGINAL_SHA256,
        "transport_r1_sha256": TRANSPORT_R1_SHA256,
        "mathematical_result_unchanged": True,
        "frozen_result_sha256": digest(HERE / "RESULT.json"),
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
