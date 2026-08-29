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
OLD_POINT = {
    "aa0": Fraction(1), "cs1": Fraction(1, 6),
    "ec3": Fraction(1, 6), "rs2": Fraction(-2, 3),
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_parser():
    if digest(PARSER) != PARSER_SHA or digest(V23_RESULT) != V23_RESULT_SHA or digest(V28_RESULT) != V28_RESULT_SHA:
        fail("upstream manifest hash")
    spec = importlib.util.spec_from_file_location("v29_parser", PARSER)
    if spec is None or spec.loader is None:
        fail("parser import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def specialize(polynomial, killed, values):
    answer = {}
    for monomial, coefficient in polynomial.items():
        value = coefficient
        powers = []
        for name, exponent in monomial:
            if name in killed:
                value = 0
                break
            if name in values:
                value *= values[name] ** exponent
            else:
                powers.append((name, exponent))
        if value:
            key = tuple(powers)
            answer[key] = answer.get(key, Fraction(0)) + value
            if not answer[key]:
                del answer[key]
    return answer


def evaluate(polynomial, point):
    return sum(
        coefficient * __import__("functools").reduce(
            lambda value, item: value * point.get(item[0], Fraction(0)) ** item[1],
            monomial,
            Fraction(1),
        )
        for monomial, coefficient in polynomial.items()
    )


def coefficient_text(value, characteristic):
    if characteristic:
        return str((value.numerator * pow(value.denominator, -1, characteristic)) % characteristic)
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def polynomial_text(polynomial, characteristic):
    if not polynomial:
        return "0"
    pieces = []
    for monomial, coefficient in sorted(polynomial.items()):
        factors = [coefficient_text(coefficient, characteristic)]
        factors += [name if exponent == 1 else f"{name}^{exponent}" for name, exponent in monomial]
        pieces.append("*".join(factors))
    return "+".join(pieces)


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = cli.parse_args()
    if platform.system() != "Linux" or not os.environ.get("JC2_REGISTERED_AWS_LANE"):
        fail("registered AWS lane required")
    if Path("/sys/class/dmi/id/sys_vendor").read_text().strip() != "Amazon EC2":
        fail("Amazon EC2 required")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    parser = load_parser()
    v23 = json.loads(V23_RESULT.read_text())
    v28 = json.loads(V28_RESULT.read_text())

    rows = []
    source_hashes = {}
    old_zero = 0
    for name, record in sorted(v23["records"].items(), key=lambda item: (item[1]["grade"], item[1]["row"])):
        chart = record["charts"]["a1_ordered"]
        path = V23 / "output_r1" / chart["output"]
        if digest(path) != chart["output_sha256"]:
            fail(("V23 row hash", name))
        polynomial = specialize(parser.parse(path), {"rho"}, {"a1": Fraction(1)})
        if evaluate(polynomial, OLD_POINT):
            fail(("old-point negative control", name, evaluate(polynomial, OLD_POINT)))
        old_zero += 1
        rows.append((name, polynomial))
        source_hashes[str(path.relative_to(ROOT))] = chart["output_sha256"]

    grade16_control = None
    for row in range(1, 8):
        name = f"Tg16_{row}"
        raw_path = Path(v28["coefficient_paths"][name])
        path = raw_path if raw_path.is_file() else V28 / raw_path.name
        if digest(path) != v28["coefficient_sha256"][name]:
            fail(("V28 row hash", name))
        polynomial = specialize(parser.parse(path), set(), {"a1": Fraction(1)})
        value = evaluate(polynomial, OLD_POINT)
        if row == 4:
            grade16_control = value
        elif value:
            fail(("unexpected point grade16 value", name, value))
        rows.append((name, polynomial))
        source_hashes[str(path.relative_to(ROOT))] = v28["coefficient_sha256"][name]
    if old_zero != 42 or grade16_control != Fraction(-47, 384):
        fail(("point controls", old_zero, grade16_control))

    nonzero = [(name, polynomial) for name, polynomial in rows if polynomial]
    variables = sorted({name for _, polynomial in nonzero for monomial in polynomial for name, _ in monomial})
    if not variables:
        fail("empty variable set")
    lines = [f"ring R={args.characteristic},({','.join(variables)}),dp;", "option(redSB);", "option(prot);"]
    for name, polynomial in nonzero:
        lines.append(f"poly P_{name}={polynomial_text(polynomial, args.characteristic)};")
    lines.append("ideal I=" + ",".join(f"P_{name}" for name, _ in nonzero) + ";")
    lines.append("ideal G=std(I);")
    positive = nonzero[0][0]
    lines.append(f"if (reduce(P_{positive},G)!=0) {{ print(\"FAIL_POSITIVE_CONTROL\"); quit; }}")
    lines.append('print("V29_CONTROLS=1");')
    lines.append('print("V29_STANDARD_BASIS_SIZE="+string(size(G)));')
    lines.append("poly one=1;")
    lines.append("poly nf=reduce(one,G);")
    lines.append("if (nf==0) { print(\"V29_UNIT_IDEAL=1\"); } else { print(\"V29_UNIT_IDEAL=0\"); }")
    lines.append(f'write(":w {output / "NF.txt"}",string(nf));')
    lines.append('print("PASS_A1_RHO0_UNIT_SCREEN_G16_V29");')
    lines.append("quit;")
    script = output / "screen.sing"
    script.write_text("\n".join(lines) + "\n")
    result = {
        "status": "PASS-A1-RHO0-UNIT-SCREEN-G16-V29-COMPILER",
        "characteristic": args.characteristic,
        "input_rows": len(rows),
        "nonzero_rows": len(nonzero),
        "variables": variables,
        "old_point_zero_rows": old_zero,
        "grade16_point_control": [-47, 384],
        "source_sha256": source_hashes,
        "script": str(script),
        "script_sha256": digest(script),
        "scope": "ordered-a1 rho=0 a1=1 actual-total rows through grade16",
    }
    result_path = output / "compile_result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-RHO0-UNIT-SCREEN-G16-V29-COMPILER")
    print(f"INPUT_ROWS={len(rows)}")
    print(f"NONZERO_ROWS={len(nonzero)}")
    print(f"VARIABLES={len(variables)}")
    print(f"SCRIPT_SHA256={digest(script)}")


if __name__ == "__main__":
    main()

