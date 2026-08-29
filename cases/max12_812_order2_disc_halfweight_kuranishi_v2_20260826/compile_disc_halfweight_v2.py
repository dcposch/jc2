#!/usr/bin/env python3
"""Immutable V2: per-generator source/analytic ideal containment checks."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V1 = ROOT / "cases/max12_812_order2_disc_halfweight_kuranishi_20260826/compile_disc_halfweight.py"
V1_SHA = "4114c4aec72f710c138d49eb7b2d51cbbce14377b7e228526911219902ad3f9d"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v1():
    if digest(V1) != V1_SHA:
        fail(("V1 compiler hash mismatch", digest(V1), V1_SHA))
    spec = importlib.util.spec_from_file_location("disc_halfweight_v1", V1)
    if spec is None or spec.loader is None:
        fail("cannot load V1 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 32003, 65521), required=True)
    args = parser.parse_args()
    v1 = load_v1()
    tag = v1.require_aws()
    for source, expected in v1.EXPECTED.items():
        actual = v1.digest(source)
        if actual != expected:
            fail(("frozen V1 source mismatch", source, actual, expected))
    tails = json.loads(v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    target = output / f"disc_halfweight_v2_p{args.characteristic}.sing"
    v1.emit(target, args.characteristic, tails)
    text = target.read_text()
    old = '''int analytic_in_source=(reduce(IH,GE)==0);
int source_in_analytic=(reduce(IE,GH)==0);
print("DISC_HALF_ANALYTIC_IN_SOURCE="+string(analytic_in_source));
print("DISC_HALF_SOURCE_IN_ANALYTIC="+string(source_in_analytic));
if (analytic_in_source!=1 || source_in_analytic!=1) { print("DISC_HALF_FAIL=IDEAL_COMPARE"); quit(84); }'''
    new = '''int analytic_in_source=1;
int source_in_analytic=1;
for (int ci=1; ci<=size(IH); ci++) { if (reduce(IH[ci],GE)!=0) { analytic_in_source=0; print("DISC_HALF_ANALYTIC_REMAINDER_INDEX="+string(ci)); print(reduce(IH[ci],GE)); } }
for (ci=1; ci<=size(IE); ci++) { if (reduce(IE[ci],GH)!=0) { source_in_analytic=0; print("DISC_HALF_SOURCE_REMAINDER_INDEX="+string(ci)); print(reduce(IE[ci],GH)); } }
print("DISC_HALF_ANALYTIC_IN_SOURCE="+string(analytic_in_source));
print("DISC_HALF_SOURCE_IN_ANALYTIC="+string(source_in_analytic));
if (analytic_in_source!=1 || source_in_analytic!=1) { print("DISC_HALF_FAIL=IDEAL_COMPARE"); quit; }'''
    if text.count(old) != 1:
        fail(("V1 delta anchor count", text.count(old)))
    text = text.replace(old, new)
    text = text.replace(
        'print("DISC_HALF_ENDPOINT=PASS_SOURCE_ANALYTIC_IDEAL_EQUALITY");',
        'print("DISC_HALF_V2_PER_GENERATOR_CHECK=1");\nprint("DISC_HALF_ENDPOINT=PASS_SOURCE_ANALYTIC_IDEAL_EQUALITY");',
    )
    target.write_text(text)
    payload = {
        "status": "PASS-DISC-HALFWEIGHT-V2-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v1_compiler_sha256": digest(V1),
        "theorem_sha256": v1.digest(v1.THEOREM),
        "input_sha256": digest(target),
        "delta": "PER_GENERATOR_TWO_SIDED_REDUCTIONS_AND_VALID_QUIT",
        "scope": "SOURCE_ANALYTIC_HALFWEIGHT_KURANISHI_ONLY_NO_ARC_OR_ORDER2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
