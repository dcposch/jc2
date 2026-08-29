#!/usr/bin/env python3
"""Exact sequential q-gate reduction and endpoint-membership compiler."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
COMPILER = HERE / "compile_origin_q15.py"
COMPILER_SHA256 = "9c90e6d6cca8e99d08eba3c68c2ff948e93822062a40dde1af5448c2908d84bf"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_compiler():
    assert sha256(COMPILER) == COMPILER_SHA256
    spec = importlib.util.spec_from_file_location("ggv_origin_q15_compiler_frozen", COMPILER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


oq = load_compiler()
ce = oq.ce
MV = ce.MV


def decode(encoded):
    return MV({tuple(monomial): Q(coefficient)
               for monomial, coefficient in encoded})


def substitute(poly, replacements):
    return oq.mv_substitute(poly, replacements)


def rank_mod(matrix, prime):
    rows = [[(value.numerator % prime)
             * pow(value.denominator % prime, -1, prime) % prime
             for value in row] for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [value * inverse % prime for value in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][column]:
                scalar = rows[r][column]
                rows[r] = [(a - scalar * b) % prime
                           for a, b in zip(rows[r], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def rref(matrix, rhs):
    a = [row[:] for row in matrix]
    b = list(rhs)
    pivot_row = 0
    pivots = []
    columns = len(a[0]) if a else 0
    for column in range(columns):
        chosen = next((r for r in range(pivot_row, len(a)) if a[r][column]), None)
        if chosen is None:
            continue
        a[pivot_row], a[chosen] = a[chosen], a[pivot_row]
        b[pivot_row], b[chosen] = b[chosen], b[pivot_row]
        scalar = a[pivot_row][column]
        a[pivot_row] = [value / scalar for value in a[pivot_row]]
        b[pivot_row] = b[pivot_row].scale(1 / scalar)
        for r in range(len(a)):
            if r == pivot_row or not a[r][column]:
                continue
            scalar = a[r][column]
            a[r] = [left - scalar * right
                    for left, right in zip(a[r], a[pivot_row])]
            b[r] = b[r] - b[pivot_row].scale(scalar)
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(a):
            break
    return a, b, pivots


def record(poly, kind, **metadata):
    encoded = poly.encode()
    return {
        "kind": kind, "terms": encoded,
        "sha256": hashlib.sha256(ce.compact(encoded)).hexdigest(),
        **metadata,
    }


def reduce_system(system_path: Path):
    system = json.loads(system_path.read_text())
    assert system["schema"] == "GGV-8_28-UPPER-LAMBDA0-ORIGIN-Q5-Q15-v1"
    gates = {gate["q"]: gate for gate in system["gates"]}
    grouped = {gate["q"]: [decode(item["terms"])
                           for item in gate["equations"]]
               for gate in system["gates"]}
    replacements = {}
    free_variables = set(system["variables"])
    pivots = []
    q_compatibility = []
    stats = {}
    primes = (65521, 65519, 65497)

    for n in range(5, 16):
        current = gates[n]["new_variables"]
        equations = [substitute(poly, replacements) for poly in grouped[n]]
        matrix, rhs = [], []
        for poly in equations:
            row = [poly.terms.get((name,), Q(0)) for name in current]
            linear = MV.zero()
            for name, coefficient in zip(current, row):
                linear = linear + MV.var(name).scale(coefficient)
            residual = poly - linear
            assert all(not any(name in current for name in monomial)
                       for monomial in residual.terms), (n, current)
            matrix.append(row)
            rhs.append(residual)
        reduced, reduced_rhs, pivot_columns = rref(matrix, rhs)
        exact_rank = len(pivot_columns)
        modular_ranks = {str(p): rank_mod(matrix, p) for p in primes}
        assert all(value == exact_rank for value in modular_ranks.values()), (
            n, exact_rank, modular_ranks
        )
        nonpivots = [column for column in range(len(current))
                     if column not in set(pivot_columns)]
        new_replacements = {}
        for row_index, column in enumerate(pivot_columns):
            expression = -reduced_rhs[row_index]
            for free_column in nonpivots:
                coefficient = reduced[row_index][free_column]
                if coefficient:
                    expression = expression - MV.var(current[free_column]).scale(coefficient)
            name = current[column]
            new_replacements[name] = expression
            free_variables.discard(name)
            pivots.append(record(expression, "pivot", q=n, pivot=name))
        row_records = []
        for row_index in range(len(pivot_columns), len(reduced)):
            assert all(not value for value in reduced[row_index])
            condition = reduced_rhs[row_index]
            if condition.terms:
                item = record(condition, "q_compatibility", q=n,
                              index=len(row_records))
                row_records.append(item)
                q_compatibility.append(item)
        replacements.update(new_replacements)
        stats[str(n)] = {
            "equations": len(equations), "new_variables": len(current),
            "exact_rank": exact_rank, "modular_ranks": modular_ranks,
            "kernel_dimension": len(nonpivots),
            "compatibility_count": len(row_records),
            "new_free_variables": [current[column] for column in nonpivots],
        }
        print(json.dumps({"event": "Q_GATE_REDUCED", "q": n,
                          "pivots_so_far": len(pivots),
                          "compatibility_so_far": len(q_compatibility),
                          **stats[str(n)]}, sort_keys=True), flush=True)

    def reduce_records(items, group):
        out = []
        for index, item in enumerate(items):
            poly = substitute(decode(item["terms"]), replacements)
            if poly.terms:
                out.append(record(poly, group, source_kind=item["kind"],
                                  source_index=index,
                                  x_degree=item.get("x_degree"),
                                  row=item.get("row")))
        return out

    g_rows = {
        weight: reduce_records(
            system["G8_G15_polynomial_windows"][str(weight)]["equations"],
            f"G{weight}_raw",
        )
        for weight in range(8, 16)
    }
    g11 = g_rows[11]
    g15 = g_rows[15]
    all_g = [item for weight in range(8, 16) for item in g_rows[weight]]
    open_condition = record(
        substitute(decode(system["open_equation"]["terms"]), replacements),
        "c2_open",
    )
    endpoint_value = substitute(decode(system["endpoint_value"]), replacements)
    endpoint_residual = substitute(
        decode(system["endpoint_equation"]["terms"]), replacements
    )
    assert endpoint_residual == endpoint_value - MV.const(1)
    endpoint_value_record = record(endpoint_value, "D22_X0_value")
    endpoint_record = record(endpoint_residual, "D22_X0_equals_1")

    base = q_compatibility + all_g + [open_condition]
    g15_membership_base = q_compatibility + g15 + [open_condition]
    active = sorted({name for item in base + [endpoint_record]
                     for monomial, _ in item["terms"] for name in monomial})
    assert set(active) <= free_variables
    constant_obstructions = [
        {"kind": item["kind"], "value": str(decode(item["terms"]).terms[()])}
        for item in base + [endpoint_record]
        if set(decode(item["terms"]).terms) == {()}
        and decode(item["terms"]).terms[()]
    ]
    return {
        "schema": "GGV-8_28-UPPER-LAMBDA0-ORIGIN-Q5-Q15-REDUCED-v1",
        "system_id": system["system_id"],
        "slice_kind": system["slice_kind"],
        "source_system": str(system_path),
        "source_system_sha256": sha256(system_path),
        "method": "sequential constant-Q RREF with three-prime rank agreement and closed exact substitution",
        "row_stats": stats,
        "pivots": pivots, "pivot_count": len(pivots),
        "free_variables": [name for name in system["variables"]
                           if name in free_variables],
        "q_compatibility": q_compatibility,
        "G8_G15_raw_constraints": {str(weight): g_rows[weight]
                                    for weight in range(8, 16)},
        "G11_raw_constraints": g11,
        "G15_raw_constraints": g15,
        "open_condition": open_condition,
        "base_constraints": base,
        "G15_membership_base": g15_membership_base,
        "endpoint_value": endpoint_value_record,
        "endpoint_residual": endpoint_record,
        "active_variables": active,
        "constant_obstructions": constant_obstructions,
        "scope": system["scope"],
    }


def singular_script(result, modulus, task, tracked=False):
    assert task in ("full", "membership_g15", "membership_base")
    if task == "full":
        generators = result["base_constraints"] + [result["endpoint_residual"]]
        target = None
    elif task == "membership_g15":
        generators = result["G15_membership_base"]
        target = result["endpoint_value"]
    else:
        generators = result["base_constraints"]
        target = result["endpoint_value"]
    names = sorted({name for item in generators + ([target] if target else [])
                    for monomial, _ in item["terms"] for name in monomial})
    variables = names or ["dummy"]
    expressions = [decode(item["terms"]).expression(modulus)
                   for item in generators] or ["0"]
    lines = [
        f"ring originq15={modulus},({','.join(variables)}),lp;",
        "option(redSB);", "ideal I=", ",\n".join(expressions) + ";",
        f'print("TASK={task} VARIABLES="+string(nvars(basering))+" GENERATORS="+string(size(I)));',
        "int start_time=timer;",
    ]
    if tracked:
        lines += [
            "matrix T; ideal J=liftstd(I,T);",
            "matrix basis_replay=matrix(I)*T-matrix(J);",
            'print("BASIS_REPLAY_ZERO="+string(size(module(basis_replay))==0));',
        ]
    else:
        lines.append("ideal J=std(I);")
    lines += [
        "int elapsed=timer-start_time;",
        'print("SECONDS="+string(elapsed));',
        'int is_unit=(size(J)==1 && J[1]==1);',
        'print("UNIT="+string(is_unit));',
        'print("BASIS_SIZE="+string(size(J)));',
        'if(!is_unit){print("DIM="+string(dim(J)));}',
    ]
    if target is not None:
        target_expression = decode(target["terms"]).expression(modulus)
        lines += [
            f"poly target={target_expression};",
            "poly target_nf=reduce(target,J);",
            'print("TARGET_NF_ZERO="+string(target_nf==0));',
            'if(target_nf!=0){print("TARGET_NF="); print(target_nf);}',
        ]
        if tracked:
            lines += [
                "if(target_nf==0){",
                "  matrix H=lift(J,ideal(target)); matrix C=T*H;",
                "  matrix replay=matrix(I)*C-matrix(ideal(target));",
                '  print("TARGET_REPLAY_ZERO="+string(size(module(replay))==0));',
                f'  write("{task}_cofactors.txt",C);',
                "}",
            ]
    elif tracked:
        lines += [
            "if(is_unit){",
            "  matrix H=lift(J,ideal(1)); matrix C=T*H;",
            "  matrix replay=matrix(I)*C-matrix(ideal(1));",
            '  print("UNIT_REPLAY_ZERO="+string(size(module(replay))==0));',
            '  write("full_unit_cofactors.txt",C);',
            "}",
        ]
    lines += ["quit;", ""]
    return "\n".join(lines)


def write_outputs(system_path: Path, output_dir: Path):
    result = reduce_system(system_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    payloads = {"REDUCTION.json": ce.pretty(result)}
    for prime in (65521, 65519, 65497):
        for task in ("membership_g15", "membership_base", "full"):
            payloads[f"{task}_p{prime}.sing"] = singular_script(
                result, prime, task
            ).encode()
    for task in ("membership_g15", "membership_base", "full"):
        payloads[f"{task}_q_tracked.sing"] = singular_script(
            result, 0, task, tracked=True
        ).encode()
    manifest = {}
    for name, payload in payloads.items():
        (output_dir / name).write_bytes(payload)
        manifest[name] = hashlib.sha256(payload).hexdigest()
    (output_dir / "GENERATED.sha256.json").write_bytes(ce.pretty(manifest))
    print(json.dumps({
        "status": "REDUCTION_PASS", "system_id": result["system_id"],
        "pivots": result["pivot_count"],
        "q_compatibility": len(result["q_compatibility"]),
        "G8_G15_constraints": {
            weight: len(items)
            for weight, items in result["G8_G15_raw_constraints"].items()
        },
        "active_variables": len(result["active_variables"]),
        "constant_obstructions": result["constant_obstructions"],
        "sha256": manifest["REDUCTION.json"],
    }, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--system", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    write_outputs(args.system, args.output_dir)


if __name__ == "__main__":
    main()
