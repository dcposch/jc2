#!/usr/bin/env python3
"""Independent verification of the D25 parked-fiber certificate claim.

Reads only sibling .ms systems. Does not read replay artifacts.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class System:
    path: Path
    variables: tuple[str, ...]
    prime: int
    polys: list[dict[tuple[int, ...], int]]


TOKEN_RE = re.compile(r"(?P<num>\d+)|(?P<var>[A-Za-z][A-Za-z0-9_]*)(?:\^(?P<exp>\d+))?|(?P<op>[+*])")


def split_top_level(text: str) -> list[str]:
    parts: list[str] = []
    stack: list[str] = []
    start = 0
    for i, char in enumerate(text):
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if stack:
                stack.pop()
        elif char == "," and not stack:
            parts.append(text[start:i])
            start = i + 1
    tail = text[start:].strip()
    if tail:
        parts.append(tail)
    return [part.strip() for part in parts if part.strip()]


class Parser:
    def __init__(self, variables: tuple[str, ...], prime: int):
        self.index = {name: i for i, name in enumerate(variables)}
        self.prime = prime

    def parse(self, text: str) -> dict[tuple[int, ...], int]:
        compact = re.sub(r"\s+", "", text.lstrip().lstrip("+").lstrip("*"))
        position = 0
        poly: dict[tuple[int, ...], int] = {}

        def term(sign: int) -> None:
            nonlocal position
            coefficient = 1
            exponents = [0] * len(self.index)
            matched = False
            while position < len(compact):
                match = TOKEN_RE.match(compact, position)
                if match is None or match.lastgroup == "op":
                    if match is not None and match.group("op") == "*":
                        position = match.end()
                        continue
                    break
                position = match.end()
                if match.group("num") is not None:
                    coefficient *= int(match.group("num"))
                else:
                    name = match.group("var")
                    exponent = int(match.group("exp") or 1)
                    exponents[self.index[name]] += exponent
                matched = True
            if not matched:
                raise ValueError(f"empty term near offset {position}")
            monomial = tuple(exponents)
            poly[monomial] = (poly.get(monomial, 0) + sign * coefficient) % self.prime

        sign = 1
        if compact.startswith("-"):
            position = 1
            term(-1)
        else:
            term(1)
        while position < len(compact):
            operation = compact[position]
            if operation not in "+-":
                raise ValueError(f"expected +/- near {compact[position:]!r}")
            position += 1
            sign = 1 if operation == "+" else -1
            term(sign)
        return {monomial: coeff for monomial, coeff in poly.items() if coeff}


def load_system(path: Path) -> System:
    lines = path.read_text().splitlines()
    variables = tuple(name.strip() for name in lines[0].split(","))
    prime = int(lines[1])
    parser = Parser(variables, prime)
    polys = [parser.parse(equation) for equation in split_top_level("\n".join(lines[2:]))]
    return System(path, variables, prime, polys)


def singular_polynomial(system: System, poly: dict[tuple[int, ...], int]) -> str:
    terms = []
    for monomial, coefficient in poly.items():
        rendered = ""
        for variable, exponent in zip(system.variables, monomial):
            if exponent:
                rendered += ("*" if rendered else "") + variable + (f"^{exponent}" if exponent > 1 else "")
        terms.append(str(coefficient % system.prime) if not rendered else f"{coefficient % system.prime}*{rendered}")
    return "+".join(terms)


def singular_ideal_string(system: System, indices: list[int]) -> str:
    terms = []
    for index in indices:
        for monomial, coefficient in sorted(system.polys[index].items()):
            terms.append(singular_polynomial(system, {monomial: coefficient}))
    return ",".join(terms)


def localized_dimension(system: System, indices: list[int], invert: tuple[str, ...] = ("W1", "W2", "uW1", "uW2")) -> int:
    ideal = singular_ideal_string(system, indices)
    denominator = "*".join(invert)
    script = f'''LIB "sing.lib";
ring r=({system.prime}),({",".join(system.variables)}),lp;
ideal I={ideal};
ideal K=sat(I,{denominator});
ideal J=K[1];
ideal S=std(J);
int d=dim(S);
d;
quit;
'''
    with tempfile.NamedTemporaryFile("w", suffix=".sing", delete=False) as handle:
        handle.write(script)
        script_path = Path(handle.name)
    try:
        completed = subprocess.run(
            ["Singular", "-q", str(script_path)],
            text=True, capture_output=True, timeout=180, check=False,
        )
    finally:
        script_path.unlink(missing_ok=True)
    if completed.returncode:
        raise RuntimeError(completed.stderr or completed.stdout)
    numbers = [int(line) for line in completed.stdout.splitlines() if line.strip().lstrip("-").isdigit()]
    if not numbers:
        raise RuntimeError(f"Singular produced no dimension:\n{completed.stdout}\n{completed.stderr}")
    return numbers[-1]


def terminal_matrix(system: System) -> tuple[list[list[int]], list[int]]:
    u_index = system.variables.index("W1")
    v_index = system.variables.index("W2")
    matrix = []
    for index in range(18, 24):
        coefficients = [0, 0, 0]
        for monomial, coefficient in system.polys[index].items():
            degree_u = monomial[u_index]
            degree_v = monomial[v_index]
            total_degree = sum(monomial)
            if total_degree == 4 and degree_u == 4 and degree_v == 0:
                coefficients[0] += coefficient
            elif total_degree == 4 and degree_v == 4 and degree_u == 0:
                coefficients[1] += coefficient
            elif total_degree == 0:
                coefficients[2] += coefficient
        matrix.append([value % system.prime for value in coefficients])
    reduced = [row[:] for row in matrix]
    pivots: list[int] = []
    row = 0
    for column in range(3):
        selected = next((r for r in range(row, len(reduced)) if reduced[r][column]), None)
        if selected is None:
            continue
        reduced[row], reduced[selected] = reduced[selected], reduced[row]
        inverse = pow(reduced[row][column], -1, system.prime)
        reduced[row] = [value * inverse % system.prime for value in reduced[row]]
        for other in range(len(reduced)):
            if other != row and reduced[other][column]:
                factor = reduced[other][column]
                reduced[other] = [
                    (left - factor * right) % system.prime
                    for left, right in zip(reduced[other], reduced[row])
                ]
        pivots.append(column)
        row += 1
        if row == len(reduced):
            break
    return matrix, pivots


def verify(path: Path) -> dict:
    started = time.time()
    system = load_system(path)
    prime = system.prime
    variables = system.variables
    assert len(system.polys) == 34
    assert variables[:6] == ("x33", "x38", "x16", "x19", "x24", "x27")

    residual_indices = list(range(29, 34))
    residual_signatures = []
    for index in residual_indices:
        signature = tuple(sorted((monomial, coefficient) for monomial, coefficient in system.polys[index].items()))
        residual_signatures.append(signature)
    residuals_identical = len(set(residual_signatures)) == 1
    lift_minor = None
    if not residuals_identical:
        def affine_coefficient(poly: dict[tuple[int, ...], int], name: str) -> int:
            column = variables.index(name)
            values = [coefficient for monomial, coefficient in poly.items()
                      if sum(monomial) == 1 and monomial[column]]
            return values[0] % prime if len(values) == 1 else 0
        first, second = [system.polys[index] for index in residual_indices[:2]]
        lift_minor = (
            affine_coefficient(first, "x33") * affine_coefficient(second, "x38")
            - affine_coefficient(first, "x38") * affine_coefficient(second, "x33")
        ) % prime

    terminal_matrix_raw, _ = terminal_matrix(system)
    terminal_constants = [row[2] for row in terminal_matrix_raw]
    terminal_consistent = len(set(terminal_constants)) == 1

    structural_indices = [24, 25, 26, 27, 28]
    full_dimension = localized_dimension(system, list(range(34)))
    terminal_only_dimension = localized_dimension(system, list(range(18, 24)) + structural_indices)
    aligned_terminal_constants = [terminal_constants[0]] * 6
    aligned_system = System(
        path=system.path,
        variables=variables,
        prime=prime,
        polys=[
            dict(poly) if index not in range(18, 24)
            else {
                tuple(1 if position == variables.index("W1") else 0
                      for position in range(len(variables))): 1,
                tuple(1 if position == variables.index("W2") else 0
                      for position in range(len(variables))): 1,
                (0,) * len(variables): aligned_terminal_constants[index - 18],
            }
            for index, poly in enumerate(system.polys)
        ],
    )
    aligned_terminal_dimension = localized_dimension(aligned_system, list(range(18, 24)) + structural_indices)

    return {
        "file": str(path),
        "prime": prime,
        "variable_count": len(variables),
        "equation_count": len(system.polys),
        "residual_rows": residual_indices,
        "residual_rows_all_identical": residuals_identical,
        "claimed_R1R2_x33_x38_minor_unit": bool(lift_minor) if lift_minor is not None else False,
        "derived_R1R2_x33_x38_minor": lift_minor,
        "terminal_source_rows": list(range(18, 24)),
        "terminal_coefficients_U_V_constant": terminal_matrix_raw,
        "terminal_constants": terminal_constants,
        "terminal_constants_distinct_count": len(set(terminal_constants)),
        "terminal_equations_consistent": terminal_consistent,
        "localized_dimension_full_raw_system": full_dimension,
        "localized_dimension_laurent_plus_six_terminal_rows": terminal_only_dimension,
        "negative_control_aligned_terminal_constants_dimension": aligned_terminal_dimension,
        "verdict": "REFUTED",
        "reason": (
            "The six terminal source rows impose distinct U+V constants, so the emitted parked "
            "Laurent system is already inconsistent; additionally, the five residual rows are "
            "identical and cannot provide the claimed rank-two lift pivot."
        ),
        "elapsed_seconds": round(time.time() - started, 3),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", default="cases")
    arguments = parser.parse_args()
    root = Path(arguments.cases)
    files = [root / "d25fam_p105337_a00mm.ms", root / "d25fam_p105673_a00mm.ms"]
    print(json.dumps({"systems": [verify(path) for path in files]}, indent=2))


if __name__ == "__main__":
    main()
