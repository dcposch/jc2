#!/usr/bin/env python3
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V23 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827"
PARSER = V23 / "census_j2_typed_v23.py"
PARSER_SHA = "14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501"
V23_RESULT = V23 / "output_r1/RESULT.json"
V23_RESULT_SHA = "ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641"
V28 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827/aws_q/compiled"
V28_RESULT = V28 / "result.json"
V28_RESULT_SHA = "7e00fc2ca8de3fee8ddf9cfa7b9adfef526cc8f1cc2efcb90fb7290e8fece3ae"
V30 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g17_v30_20260827/aws_q/compiled"
V30_RESULT = V30 / "result.json"
V30_RESULT_SHA = "6a644c20551874563d6c85cdbf81e5838ef22906e9ac7ada67b075889befb7c1"
PREREG = HERE / "PREREGISTRATION.md"
KEEP = ("ell2", "cs1", "rs2", "aa0", "ee1", "ec3")
BASE_POINT = {"a1": Fraction(48), "aa0": Fraction(48), "cs1": Fraction(8),
              "ec3": Fraction(384), "rs2": Fraction(-32)}
NEWTON_POINT = {"a1": Fraction(48), "aa0": Fraction(168, 5), "cs1": Fraction(416, 55),
                "ec3": Fraction(384), "ell2": Fraction(6, 11),
                "ee1": Fraction(-1152, 55), "rs2": Fraction(-208, 11)}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_parser():
    for path, expected in ((PARSER, PARSER_SHA), (V23_RESULT, V23_RESULT_SHA),
                           (V28_RESULT, V28_RESULT_SHA), (V30_RESULT, V30_RESULT_SHA)):
        if digest(path) != expected:
            fail(("upstream hash", str(path)))
    spec = importlib.util.spec_from_file_location("v32_parser", PARSER)
    if spec is None or spec.loader is None:
        fail("parser import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def restrict(polynomial):
    answer = {}
    for monomial, coefficient in polynomial.items():
        value = coefficient
        kept = []
        for name, exponent in monomial:
            if name == "a1":
                value *= Fraction(48) ** exponent
            elif name in KEEP:
                kept.append((name, exponent))
            else:
                value = 0
                break
        if value:
            key = tuple(kept)
            answer[key] = answer.get(key, Fraction(0)) + value
            if not answer[key]:
                del answer[key]
    return answer


def evaluate(polynomial, point):
    answer = Fraction(0)
    for monomial, coefficient in polynomial.items():
        value = coefficient
        for name, exponent in monomial:
            value *= point.get(name, Fraction(0)) ** exponent
        answer += value
    return answer


def coefficient_text(value, characteristic):
    if characteristic:
        return str((value.numerator * pow(value.denominator, -1, characteristic)) % characteristic)
    return str(value.numerator) if value.denominator == 1 else f"({value.numerator}/{value.denominator})"


def polynomial_text(polynomial, characteristic):
    if not polynomial:
        return "0"
    pieces = []
    for monomial, coefficient in sorted(polynomial.items()):
        factors = [coefficient_text(coefficient, characteristic)]
        factors += [name if exponent == 1 else f"{name}^{exponent}" for name, exponent in monomial]
        pieces.append("*".join(factors))
    return "+".join(pieces).replace("+-", "-")


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = cli.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if platform.system() != "Linux" or not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2" or not tag:
        fail("registered AWS EC2 lane required")
    output = args.output.resolve(); output.mkdir(parents=True, exist_ok=False)
    parser = load_parser(); v23 = json.loads(V23_RESULT.read_text())
    v28 = json.loads(V28_RESULT.read_text()); v30 = json.loads(V30_RESULT.read_text())

    rows = []
    source_hashes = {}
    for name, record in sorted(v23["records"].items(), key=lambda item: (item[1]["grade"], item[1]["row"])):
        chart = record["charts"]["a1_ordered"]
        path = V23 / "output_r1" / chart["output"]
        if digest(path) != chart["output_sha256"]:
            fail(("V23 row hash", name))
        rows.append((name, restrict(parser.specialize(parser.parse(path), frozenset({"rho"}), {}))))
        source_hashes[str(path.relative_to(ROOT))] = chart["output_sha256"]
    for grade, base, manifest in ((16, V28, v28), (17, V30, v30)):
        for row in range(1, 8):
            name = f"Tg{grade}_{row}"
            path = base / Path(manifest["coefficient_paths"][name]).name
            if digest(path) != manifest["coefficient_sha256"][name]:
                fail(("row hash", name))
            rows.append((name, restrict(parser.parse(path))))
            source_hashes[str(path.relative_to(ROOT))] = manifest["coefficient_sha256"][name]
    if len(rows) != 56:
        fail(("row census", len(rows)))
    base_values = {name: evaluate(polynomial, BASE_POINT) for name, polynomial in rows}
    if any(value for name, value in base_values.items() if not name.startswith("Tg17_")):
        fail("base old-row control")
    if base_values["Tg17_5"] != -20736 or any(base_values[f"Tg17_{row}"] for row in (1, 2, 3, 4, 6, 7)):
        fail("base grade17 control")
    newton_nonzero = {name: value for name, polynomial in rows if (value := evaluate(polynomial, NEWTON_POINT))}

    nonzero = [(name, polynomial) for name, polynomial in rows if polynomial]
    if not nonzero:
        fail("empty restricted ideal")
    lines = [f"ring R={args.characteristic},({','.join(KEEP)}),dp;", "option(redSB);", "option(prot);"]
    for name, polynomial in nonzero:
        lines.append(f"poly P_{name}={polynomial_text(polynomial, args.characteristic)};")
    lines.append("ideal I=" + ",".join(f"P_{name}" for name, _ in nonzero) + ";")
    lines.append("ideal G=std(I);")
    lines.append(f"if (reduce(P_{nonzero[0][0]},G)!=0) {{ print(\"FAIL_POSITIVE_CONTROL\"); quit; }}")
    lines.append('print("V32_CONTROLS=1");')
    lines.append('print("V32_STANDARD_BASIS_SIZE="+string(size(G)));')
    lines.append('print("V32_DIM="+string(dim(G)));')
    lines.append("poly nf=reduce(1,G);")
    lines.append('if (nf==0) { print("V32_UNIT_IDEAL=1"); } else { print("V32_UNIT_IDEAL=0"); }')
    lines.append(f'write(":w {output / "BASIS.txt"}",string(G));')
    lines.append(f'write(":w {output / "NF.txt"}",string(nf));')
    lines.append('print("PASS_A1_GRADE17_SPARSE_SUPPORT_V32");')
    lines.append("quit;")
    script = output / "screen.sing"; script.write_text("\n".join(lines) + "\n")
    result = {
        "status": "PASS-A1-GRADE17-SPARSE-SUPPORT-V32-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "preregistration_sha256": digest(PREREG),
        "rows": len(rows),
        "nonzero_rows": len(nonzero),
        "variables": list(KEEP),
        "base_grade17_residual": [-20736, 1],
        "newton_nonzero_residuals_q": {name: [value.numerator, value.denominator] for name, value in newton_nonzero.items()},
        "source_sha256": source_hashes,
        "script": str(script),
        "script_sha256": digest(script),
        "scope": "six-coordinate ordered-a1 rho=0 algebraic prefix through grade17",
    }
    path = output / "compile_result.json"; path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-GRADE17-SPARSE-SUPPORT-V32-COMPILER")
    print(f"NONZERO_ROWS={len(nonzero)}")
    print(f"NEWTON_NONZERO={len(newton_nonzero)}")
    print(f"SCRIPT_SHA256={digest(script)}")


if __name__ == "__main__":
    main()

