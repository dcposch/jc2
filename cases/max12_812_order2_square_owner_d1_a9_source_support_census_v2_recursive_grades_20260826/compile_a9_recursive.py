#!/usr/bin/env python3
"""Compile exact recursive literal-Faber a=9 source grades; AWS only."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V1 = ROOT / "cases/max12_812_order2_square_owner_d1_a9_source_support_census_20260826/compile_a9_census.py"
V1_FREEZE = ROOT / "cases/max12_812_order2_square_owner_d1_a9_source_support_census_20260826/FREEZE.sha256"
PINS = {
    V1: "1354cc92e719aaed8daff03298aebf08d2ee3aa39c05950c6e85f523d8f36ed0",
    V1_FREEZE: "ad7fa18809c85d436ebb8f76e0af48e834c2b159ec51cca46c64dcc2cee8cade",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only a9 recursive compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only a9 recursive compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v1():
    spec = importlib.util.spec_from_file_location("a9_recursive_v1", V1)
    if spec is None or spec.loader is None:
        fail("cannot import frozen a9 V1 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen V1 ancestry mismatch", str(source), actual, expected))
    v1 = load_v1()
    for source, expected in v1.PINS.items():
        if digest(source) != expected:
            fail(("frozen V1 transitive pin mismatch", str(source)))
    a8 = v1.load_a8()
    for source, expected in a8.PINS.items():
        if digest(source) != expected:
            fail(("frozen a8 transitive pin mismatch", str(source)))
    base = a8.load_base()
    for source, expected in base.PINS.items():
        if digest(source) != expected:
            fail(("frozen base transitive pin mismatch", str(source)))
    tail_v1 = base.load_v1()
    for source, expected in tail_v1.EXPECTED.items():
        if digest(source) != expected:
            fail(("frozen tail-source mismatch", str(source)))
    tails = json.loads(tail_v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != tail_v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    tail_base = tail_v1.load_base()

    output = args.output.resolve()
    if output.exists():
        fail("a9 recursive output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_d1_a9_recursive_source_grades_{label}.sing"

    variables = ["z", "sigma", "p"]
    variables += [f"ell{i}" for i in range(1, 5)]
    for stem, count in (("a1", 5), ("a0", 5), ("c1", 5), ("c0", 5),
                        ("b1", 3), ("b0", 3)):
        variables += [stem] + [f"{stem}_{i}" for i in range(1, count)]
    variables += ["k0", "k0_1", "k0_2"]
    for stem in ("k60", "k20"):
        variables += [stem] + [f"{stem}_{i}" for i in range(1, 5)]
    variables += ["mu20", "mu20_1", "mu20_2", "mu20_3", "mu4", "mu6", "J"]

    lines = [
        f"ring R={args.characteristic},({','.join(variables)}),dp;",
        'print("A9V2_SOURCE_HASHES=PASS");',
        "ideal A9V2_Sigma=std(ideal(sigma));",
        "int A9V2_identities=1; int A9V2_nonzero_count=0; int A9V2_lower_count=0;",
    ]
    pp = "p+2*sigma*ell1+2*sigma^2*ell2+2*sigma^3*ell3+2*sigma^4*ell4"
    az = f"sigma^9*({v1.series('a1', 5)})"
    ac = f"sigma^9*({v1.series('a0', 5)})"
    cz = f"sigma^10*({v1.series('c1', 5)})"
    cc = f"sigma^10*({v1.series('c0', 5)})"
    rz = f"sigma^9*({v1.series('b1', 3)})"
    rc = f"sigma^9*({v1.series('b0', 3)})"
    coeffs = base.source_coefficients(pp, az, ac, cz, cc, rz, rc)
    loads = {
        "k10": v1.series("k0", 3),
        "k6": v1.series("k60", 5),
        "k2": v1.series("k20", 5),
    }
    targets = {
        1: "0",
        2: v1.series("mu20", 4),
        3: "0",
        4: "mu4",
        5: "0",
        6: "mu6",
        7: "J/4",
    }
    charges = [name for name in variables if name not in ("z", "sigma")]
    maximum = 31
    for row in range(1, 8):
        expression = tail_base.tail_text(tails[str(row)], row, coeffs, loads).replace(
            "Lambda", "(sigma^2)"
        )
        if targets[row] != "0":
            expression += f"-sigma^{2 * (12 + row)}*({targets[row]})"
        lines.append(f"poly A9V2_Q0_{row}={expression};")
        for grade in range(maximum + 1):
            qname = f"A9V2_Q{grade}_{row}"
            gname = f"A9V2_g{grade}_{row}"
            nz = f"A9V2_nz{grade}_{row}"
            lines += [
                f"poly {gname}=subst({qname},sigma,0);",
                f"int {nz}=0;",
                f"if ({gname}!=0) {{",
                f"  {nz}=1; A9V2_nonzero_count=A9V2_nonzero_count+1;",
                f"  if ({grade}<27) {{ A9V2_lower_count=A9V2_lower_count+1; }}",
                f'  print("A9V2_ROW_{grade}_{row}_BEGIN");',
                f"  print({gname});",
                f'  print("A9V2_ROW_{grade}_{row}_END");',
                "}",
                f'print("A9V2_ROW_{grade}_{row}_NONZERO="+string({nz}));',
            ]
            for charge in charges:
                dep = f"A9V2_d_{grade}_{row}_{charge}"
                lines += [
                    f"poly {dep}=diff({gname},{charge});",
                    f"if ({dep}!=0) {{ print(\"A9V2_DEP_{grade}_{row}_{charge}=1\"); }}",
                ]
            if grade < maximum:
                rem = f"A9V2_Rem{grade + 1}_{row}"
                nxt = f"A9V2_Q{grade + 1}_{row}"
                lines += [
                    f"poly {rem}={qname}-{gname};",
                    f"if (reduce({rem},A9V2_Sigma)!=0) {{ A9V2_identities=0; }}",
                    f"poly {nxt}={rem}/sigma;",
                    f"if (sigma*{nxt}-{rem}!=0) {{ A9V2_identities=0; }}",
                ]
    lines += [
        'print("A9V2_NONZERO_ROW_COUNT="+string(A9V2_nonzero_count));',
        'print("A9V2_LOWER_THAN_27_ROW_COUNT="+string(A9V2_lower_count));',
        'print("A9V2_RECURSIVE_QUOTIENT_IDENTITIES="+string(A9V2_identities));',
        'if (A9V2_identities!=1) { print("A9V2_FAIL=RECURSIVE_EXTRACTION"); quit; }',
        'print("A9V2_RECURSIVE_SOURCE_CENSUS_ENDPOINT=PASS_NAVIGATION_ONLY");',
        "quit;",
    ]
    target.write_text("\n".join(lines) + "\n")
    payload = {
        "status": "PASS-A9-RECURSIVE-LITERAL-FABER-COMPILER",
        "scope": "GRADES_0_31_NAVIGATION_ONLY_NO_ROW_OR_ARC_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
