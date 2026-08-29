#!/usr/bin/env python3
"""Correct the V1 raw-cusp certificate assertions, preserving its source."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V1 = ROOT / "cases/max12_812_order2_p0_cusp_raw_g12_cech_certificate_20260826/compile_raw_cusp_g12_cech.py"
V1_FREEZE = ROOT / "cases/max12_812_order2_p0_cusp_raw_g12_cech_certificate_20260826/FREEZE.sha256"
EXPECTED = {
    V1: "feb3711636b57457069c36f79904325d901f68a3cda93742ac5dc737cc1a3c7a",
    V1_FREEZE: "213e55fe0b59b3979edd2dfe6c2265109a5739438bef7fec6c7beefe1c6b3721",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v1():
    spec = importlib.util.spec_from_file_location("raw_cusp_cech_v1", V1)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V1 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def repair_assertions(script: Path) -> None:
    text = script.read_text()
    replacements = {
        "poly ExpectedRow6=-(3/128)*rs*c1^2-(3/32)*rs*a0*c0-(3/16)*cs*c0*c1-(5/32768)*k*rs^4;":
            "poly ExpectedRow6=(15/32768)*k*rs^4-(3/64)*rs*a0*c0-(3/64)*cs*c0*c1-(3/256)*rs*c1^2;",
        "poly DirectCert=32768*g12_6-35*k*rs^4+8192*rs*g10_2+32768*cs*g10_3;":
            "poly DirectCert=32768*g12_6-35*k*rs^4+4096*rs*g10_2+8192*cs*g10_3;",
        "poly OmitNilpotentRow=32768*g12_6-35*k*rs^4+8192*rs*g10_2;":
            "poly OmitNilpotentRow=32768*g12_6-35*k*rs^4+4096*rs*g10_2;",
        "int negativeControl=(OmitNilpotentRow==-6144*cs*c0*c1 && OmitNilpotentRow!=0);":
            "int negativeControl=(OmitNilpotentRow==-1536*cs*c0*c1 && OmitNilpotentRow!=0);",
        "P0_CUSP_RAW_G12_CERTIFICATE_TEXT=32768*g12_6-35*k*rs^4=-8192*rs*g10_2-32768*cs*g10_3":
            "P0_CUSP_RAW_G12_CERTIFICATE_TEXT=32768*g12_6-35*k*rs^4=-4096*rs*g10_2-8192*cs*g10_3",
    }
    for old, new in replacements.items():
        if text.count(old) != 1:
            fail(("V1 assertion anchor missing or nonunique", old, text.count(old)))
        text = text.replace(old, new)
    script.write_text(text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()

    v1 = load_v1()
    owner = v1.load_owner()
    tag = owner.require_aws()
    for source, expected in EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen V1 mismatch", str(source), actual, expected))
    for source, expected in v1.EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen V1 transitive mismatch", str(source), actual, expected))
    for source, expected in owner.EXPECTED_STATIC.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen owner transitive mismatch", str(source), actual, expected))
    tails = json.loads(owner.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != owner.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    singular = output / f"p0_cusp_raw_g12_cech_v2_{label}.sing"
    owner.emit(singular, args.characteristic, tails)
    v1.append_certificate(singular)
    repair_assertions(singular)
    source_text = singular.read_text()
    result = {
        "status": "PASS-P0-CUSP-RAW-G12-CECH-V2-COMPILER",
        "scope": "POST_M0_FIXED_P0_D_K0_RS_RAW_CUSP_CHART_ONLY_NO_TOTAL_REES_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v1_sha256": digest(V1),
        "owner_sha256": digest(v1.OWNER),
        "tails_sha256": digest(owner.TAILS),
        "input_sha256": digest(singular),
        "source_occurrences": {
            "k6": source_text.count("k6"),
            "k2": source_text.count("k2"),
            "mu2": source_text.count("mu2"),
            "mu4": source_text.count("mu4"),
            "mu6": source_text.count("mu6"),
            "J": source_text.count("J"),
        },
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
