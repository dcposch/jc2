#!/usr/bin/env python3
"""Compile literal-Faber a=9 support rows; execute only on registered AWS."""

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
A8 = ROOT / "cases/max12_812_order2_square_owner_d1_a8_k6_mu2_fullsupport_20260826/compile_a8.py"
A8_FREEZE = ROOT / "cases/max12_812_order2_square_owner_d1_a8_k6_mu2_fullsupport_20260826/FREEZE.sha256"
PINS = {
    A8: "0230ca443d49e47b5d6ebae8c0f8a88d31a793d13b1df59e3698e166226d177b",
    A8_FREEZE: "c18bdd9f55a108470ef166e6c0cfa243ab61b63f45742537046fdb6e583b5dc8",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only a9 census compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only a9 census compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_a8():
    spec = importlib.util.spec_from_file_location("a9_census_a8", A8)
    if spec is None or spec.loader is None:
        fail("cannot import frozen a8 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def series(prefix: str, count: int) -> str:
    return "+".join(prefix if i == 0 else f"sigma^{i}*{prefix}_{i}" for i in range(count))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen ancestry mismatch", str(source), actual, expected))
    a8 = load_a8()
    for source, expected in a8.PINS.items():
        if digest(source) != expected:
            fail(("frozen a8 transitive pin mismatch", str(source)))
    base = a8.load_base()
    for source, expected in base.PINS.items():
        if digest(source) != expected:
            fail(("frozen base transitive pin mismatch", str(source)))
    v1 = base.load_v1()
    for source, expected in v1.EXPECTED.items():
        if digest(source) != expected:
            fail(("frozen tail-source mismatch", str(source)))
    tails = json.loads(v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    tail_base = v1.load_base()

    output = args.output.resolve()
    if output.exists():
        fail("a9 census output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_d1_a9_source_support_census_{label}.sing"

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
        'print("A9_SOURCE_HASHES=PASS");',
    ]
    pp = "p+2*sigma*ell1+2*sigma^2*ell2+2*sigma^3*ell3+2*sigma^4*ell4"
    az = f"sigma^9*({series('a1', 5)})"
    ac = f"sigma^9*({series('a0', 5)})"
    cz = f"sigma^10*({series('c1', 5)})"
    cc = f"sigma^10*({series('c0', 5)})"
    rz = f"sigma^9*({series('b1', 3)})"
    rc = f"sigma^9*({series('b0', 3)})"
    coeffs = base.source_coefficients(pp, az, ac, cz, cc, rz, rc)
    loads = {
        "k10": series("k0", 3),
        "k6": series("k60", 5),
        "k2": series("k20", 5),
    }
    targets = {
        1: "0",
        2: series("mu20", 4),
        3: "0",
        4: "mu4",
        5: "0",
        6: "mu6",
        7: "J/4",
    }
    minimum, maximum = 27, 31
    lines += [
        f"ideal A9_Sigma=std(ideal(sigma^{minimum}));",
        "ideal A9_Sigma1=std(ideal(sigma));",
        "int A9_divisible=1; int A9_identities=1;",
    ]
    row_names: dict[tuple[int, int], str] = {}
    for row in range(1, 8):
        expression = tail_base.tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")
        if targets[row] != "0":
            expression += f"-sigma^{2 * (12 + row)}*({targets[row]})"
        lines += [
            f"poly A9_Phi{row}={expression};",
            f"if (reduce(A9_Phi{row},A9_Sigma)!=0) {{ A9_divisible=0; }}",
            f"poly A9_Q{minimum}_{row}=A9_Phi{row}/sigma^{minimum};",
            f"if (sigma^{minimum}*A9_Q{minimum}_{row}-A9_Phi{row}!=0) {{ A9_identities=0; }}",
        ]
        for grade in range(minimum, maximum + 1):
            qname = f"A9_Q{grade}_{row}"
            gname = f"A9_g{grade}_{row}"
            row_names[(grade, row)] = gname
            lines += [
                f"poly {gname}=subst({qname},sigma,0);",
                f'print("A9_ROW_{grade}_{row}_BEGIN");',
                f"print({gname});",
                f'print("A9_ROW_{grade}_{row}_END");',
            ]
            if grade < maximum:
                rem = f"A9_Rem{grade + 1}_{row}"
                nxt = f"A9_Q{grade + 1}_{row}"
                lines += [
                    f"poly {rem}={qname}-{gname};",
                    f"if (reduce({rem},A9_Sigma1)!=0) {{ A9_identities=0; }}",
                    f"poly {nxt}={rem}/sigma;",
                    f"if (sigma*{nxt}-{rem}!=0) {{ A9_identities=0; }}",
                ]
    charges = [
        "ell1", "ell2", "ell3", "ell4",
        "k0", "k0_1", "k0_2",
        "k60", "k60_1", "k60_2", "k60_3", "k60_4",
        "k20", "k20_1", "k20_2", "k20_3", "k20_4",
        "mu20", "mu20_1", "mu20_2", "mu20_3", "mu4", "mu6", "J",
    ]
    for grade in range(minimum, maximum + 1):
        for charge in charges:
            flag = f"A9_dep_{grade}_{charge}"
            lines.append(f"int {flag}=0;")
            for row in range(1, 8):
                lines.append(f"if (diff({row_names[(grade, row)]},{charge})!=0) {{ {flag}=1; }}")
            lines.append(f'print("A9_DEP_{grade}_{charge}="+string({flag}));')
    lines += [
        'print("A9_SOURCE_DIVISIBLE="+string(A9_divisible));',
        'print("A9_SOURCE_QUOTIENT_IDENTITIES="+string(A9_identities));',
        'if (A9_divisible*A9_identities!=1) { print("A9_FAIL=SOURCE_EXTRACTION"); quit; }',
        'print("A9_SOURCE_SUPPORT_CENSUS_ENDPOINT=PASS_NAVIGATION_ONLY");',
        "quit;",
    ]
    target.write_text("\n".join(lines) + "\n")
    payload = {
        "status": "PASS-A9-LITERAL-FABER-SOURCE-CENSUS-COMPILER",
        "scope": "GRADES_27_31_SUPPORT_NAVIGATION_ONLY_NO_ROW_OR_ARC_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
