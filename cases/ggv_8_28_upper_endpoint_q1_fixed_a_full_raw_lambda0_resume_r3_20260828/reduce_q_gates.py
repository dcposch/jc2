#!/usr/bin/env python3
"""Exact sequential affine reduction of a compiled q1,...,q13 gate system."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
COMPILER = HERE / "compile_q_gates.py"
COMPILER_SHA256 = "b487d8b532d303421386c66638a6d7953aa5a4dcf74208cd07c6db885c511201"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_compiler():
    assert sha256(COMPILER) == COMPILER_SHA256
    spec = importlib.util.spec_from_file_location("ggv_q_gate_compiler_frozen", COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


qg = load_compiler()
ce = qg.ce
MV = ce.MV


def decode(encoded):
    return MV({tuple(mon): Q(coefficient) for mon, coefficient in encoded})


def substitute(poly, replacements):
    out = MV.zero()
    for mon, coefficient in poly.terms.items():
        term = MV.const(coefficient)
        for name in mon:
            term = term * replacements.get(name, MV.var(name))
        out = out + term
    return out


def rank_mod(matrix, prime):
    rows = [[(value.numerator % prime) * pow(value.denominator % prime, -1, prime) % prime
             for value in row] for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        chosen = next((r for r in range(rank, len(rows)) if rows[r][column]), None)
        if chosen is None:
            continue
        rows[rank], rows[chosen] = rows[chosen], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [value * inverse % prime for value in rows[rank]]
        for r in range(len(rows)):
            if r == rank or not rows[r][column]:
                continue
            scalar = rows[r][column]
            rows[r] = [(a - scalar * b) % prime for a, b in zip(rows[r], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def rref_with_rhs(matrix, rhs):
    a = [row[:] for row in matrix]
    b = list(rhs)
    row_count = len(a)
    column_count = len(a[0]) if a else 0
    pivot_row = 0
    pivots = []
    for column in range(column_count):
        chosen = next((row for row in range(pivot_row, row_count) if a[row][column]), None)
        if chosen is None:
            continue
        a[pivot_row], a[chosen] = a[chosen], a[pivot_row]
        b[pivot_row], b[chosen] = b[chosen], b[pivot_row]
        scalar = a[pivot_row][column]
        a[pivot_row] = [value / scalar for value in a[pivot_row]]
        b[pivot_row] = b[pivot_row].scale(1 / scalar)
        for row in range(row_count):
            if row == pivot_row or not a[row][column]:
                continue
            scalar = a[row][column]
            a[row] = [left - scalar * right for left, right in zip(a[row], a[pivot_row])]
            b[row] = b[row] - b[pivot_row].scale(scalar)
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return a, b, pivots


def reduce_system(system_path: Path):
    system = json.loads(system_path.read_text())
    assert system["schema"] == "GGV-8_28-UPPER-ENDPOINT-Q1-Q13-DE-RHAM-GATES-v1"
    grouped = {gate["q"]: [decode(item["terms"]) for item in gate["equations"]]
               for gate in system["gates"]}
    gates = {gate["q"]: gate for gate in system["gates"]}
    replacements = {}
    free_variables = set(system["variables"])
    pivots = []
    compatibility = []
    stats = {}
    terminal_constant = None
    primes = (65521, 65519, 65497)

    for n in range(1, 14):
        current = gates[n]["new_variables"]
        equations = [substitute(poly, replacements) for poly in grouped[n]]
        matrix = []
        rhs = []
        for poly in equations:
            row = [poly.terms.get((name,), Q(0)) for name in current]
            linear = MV.zero()
            for name, coefficient in zip(current, row):
                linear = linear + MV.var(name).scale(coefficient)
            residual = poly - linear
            assert all(not any(name in current for name in mon) for mon in residual.terms), (n, current)
            matrix.append(row)
            rhs.append(residual)
        reduced, reduced_rhs, pivot_columns = rref_with_rhs(matrix, rhs)
        exact_rank = len(pivot_columns)
        modular_ranks = {str(prime): rank_mod(matrix, prime) for prime in primes}
        assert all(rank == exact_rank for rank in modular_ranks.values()), (n, exact_rank, modular_ranks)
        pivot_set = set(pivot_columns)
        nonpivots = [column for column in range(len(current)) if column not in pivot_set]
        new_replacements = {}
        for row, column in enumerate(pivot_columns):
            expression = -reduced_rhs[row]
            for free_column in nonpivots:
                coefficient = reduced[row][free_column]
                if coefficient:
                    expression = expression - MV.var(current[free_column]).scale(coefficient)
            name = current[column]
            new_replacements[name] = expression
            free_variables.discard(name)
            encoded = expression.encode()
            pivots.append({
                "q": n, "pivot": name, "expression": encoded,
                "sha256": hashlib.sha256(ce.compact(encoded)).hexdigest(),
            })
        row_compatibility = []
        for row in range(len(pivot_columns), len(reduced)):
            assert all(not value for value in reduced[row])
            condition = reduced_rhs[row]
            if not condition.terms:
                continue
            encoded = condition.encode()
            record = {
                "q": n, "index": len(row_compatibility), "terms": encoded,
                "sha256": hashlib.sha256(ce.compact(encoded)).hexdigest(),
            }
            row_compatibility.append(record)
            compatibility.append(record)
            if set(condition.terms) == {()} and terminal_constant is None:
                terminal_constant = {"q": n, "value": str(condition.terms[()]),
                                     "compatibility_index": len(compatibility) - 1}
        replacements.update(new_replacements)
        stats[str(n)] = {
            "equations": len(equations),
            "new_variables": len(current),
            "exact_rank": exact_rank,
            "modular_ranks": modular_ranks,
            "kernel_dimension": len(nonpivots),
            "compatibility_count": len(row_compatibility),
            "new_free_variables": [current[column] for column in nonpivots],
        }
        print(json.dumps({
            "event": "Q_GATE_REDUCED", "q": n,
            "pivots_so_far": len(pivots), "compatibility_so_far": len(compatibility),
            **stats[str(n)],
        }, sort_keys=True), flush=True)
        if terminal_constant is not None:
            print(json.dumps({"event": "EXACT_CONSTANT_OBSTRUCTION", **terminal_constant},
                             sort_keys=True), flush=True)
            break

    active = sorted({name for record in compatibility for mon, _ in record["terms"] for name in mon})
    assert set(active) <= free_variables
    return {
        "schema": "GGV-8_28-UPPER-ENDPOINT-Q1-Q13-TRIANGULAR-v1",
        "source_system": str(system_path),
        "source_system_sha256": sha256(system_path),
        "method": "sequential constant-Q RREF and exact closed pivot substitution",
        "system_id": system["system_id"],
        "row_stats": stats,
        "pivot_count": len(pivots),
        "pivots": pivots,
        "free_variables": [name for name in system["variables"] if name in free_variables],
        "free_variable_count": len(free_variables),
        "active_free_variables": active,
        "active_free_variable_count": len(active),
        "compatibility": compatibility,
        "compatibility_count": len(compatibility),
        "terminal_constant_obstruction": terminal_constant,
        "scope": system["scope"],
    }


def singular_script(result, modulus, tracked=False):
    variables = result["active_free_variables"] or ["dummy"]
    expressions = [decode(item["terms"]).expression(modulus)
                   for item in result["compatibility"]]
    if not expressions:
        expressions = ["0"]
    lines = [
        f"ring qreduced={modulus},({','.join(variables)}),lp;",
        "option(redSB);",
        "ideal I=",
        ",\n".join(expressions) + ";",
        'print("QREDUCED variables="+string(nvars(basering))+" generators="+string(size(I)));',
        "int start_time=timer;",
        'print("START_GROEBNER");',
    ]
    if tracked:
        lines.extend([
            "matrix T; ideal J=liftstd(I,T);",
            "matrix basis_replay=matrix(I)*T-matrix(J);",
            'print("BASIS_REPLAY_ZERO="+string(size(module(basis_replay))==0));',
        ])
    else:
        lines.append("ideal J=std(I);")
    lines.extend([
        "int elapsed=timer-start_time;",
        'print("END_GROEBNER seconds="+string(elapsed));',
        'print("BASIS_SIZE="+string(size(J)));',
        'int is_unit=(size(J)==1 && J[1]==1);',
        'print("UNIT="+string(is_unit));',
        'if(!is_unit){print("DIM="+string(dim(J)));}',
    ])
    if tracked:
        lines.extend([
            "if(is_unit){",
            "  matrix H=lift(J,ideal(1)); matrix C=T*H;",
            "  matrix replay=matrix(I)*C-matrix(ideal(1));",
            '  print("UNIT_REPLAY_ZERO="+string(size(module(replay))==0));',
            '  write("reduced_unit_cofactors.txt",C);',
            "}",
        ])
    lines.extend(["quit;", ""])
    return "\n".join(lines)


def write_reduction(system_path: Path, output_dir: Path):
    result = reduce_system(system_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    payloads = {
        "TRIANGULAR_REDUCTION.json": ce.pretty(result),
        "reduced_p65521.sing": singular_script(result, 65521).encode(),
        "reduced_p65519.sing": singular_script(result, 65519).encode(),
        "reduced_p65497.sing": singular_script(result, 65497).encode(),
        "reduced_q.sing": singular_script(result, 0).encode(),
        "reduced_q_tracked.sing": singular_script(result, 0, tracked=True).encode(),
    }
    manifest = {}
    for name, payload in payloads.items():
        (output_dir / name).write_bytes(payload)
        manifest[name] = hashlib.sha256(payload).hexdigest()
    (output_dir / "GENERATED.sha256.json").write_bytes(ce.pretty(manifest))
    return result, manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--system", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    result, manifest = write_reduction(args.system, args.output_dir)
    print(json.dumps({
        "status": "TRIANGULAR_PASS",
        "system_id": result["system_id"],
        "pivots": result["pivot_count"],
        "free_variables": result["free_variable_count"],
        "active_free_variables": result["active_free_variable_count"],
        "compatibility": result["compatibility_count"],
        "terminal_constant_obstruction": result["terminal_constant_obstruction"],
        "sha256": manifest["TRIANGULAR_REDUCTION.json"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
