#!/usr/bin/env python3
"""Exact augmented-rank/dual-functional successor to the H16 rank-12 gate."""

from fractions import Fraction
from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
H16_PATH = HERE / "replay_v89h16_p12_p13_compatibility_point.py"
H16_SHA = "751d53520afec42e73e81dc90534180e2b0a446ab212fdd7e8198c0dc6f22a2c"
assert sha256(H16_PATH.read_bytes()).hexdigest() == H16_SHA
spec = importlib.util.spec_from_file_location("td6_v89h16_parent", H16_PATH)
h16 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = h16
spec.loader.exec_module(h16)


def rref_with_transform(matrix, rhs):
    nrow, ncol = len(matrix), len(matrix[0])
    work = [list(matrix[row]) + [rhs[row]] for row in range(nrow)]
    transform = [
        [Fraction(int(row == column)) for column in range(nrow)]
        for row in range(nrow)
    ]
    pivots = []
    active = 0
    for column in range(ncol):
        pivot = next((row for row in range(active, nrow) if work[row][column]), None)
        if pivot is None:
            continue
        work[active], work[pivot] = work[pivot], work[active]
        transform[active], transform[pivot] = transform[pivot], transform[active]
        pivot_value = work[active][column]
        work[active] = [entry / pivot_value for entry in work[active]]
        transform[active] = [entry / pivot_value for entry in transform[active]]
        for row in range(nrow):
            if row == active or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                work[row][entry] - factor * work[active][entry]
                for entry in range(ncol + 1)
            ]
            transform[row] = [
                transform[row][entry] - factor * transform[active][entry]
                for entry in range(nrow)
            ]
        pivots.append(column)
        active += 1
        if active == nrow:
            break
    return work, transform, tuple(pivots)


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith("td6_v89h16r1_p12_p13_")
    p12 = h16.load_records(h16.P12, 166)
    p13 = h16.load_records(h16.P13, 238)
    row_specs = [
        *(("P12", coordinate, p12) for coordinate in range(2, 8)),
        *(("P13", coordinate, p13) for coordinate in range(2, 18)),
    ]
    matrix = [
        [
            h16.value(records, (), (exponent,), coordinate)
            for exponent in h16.Q_EXPONENTS
        ]
        for _, coordinate, records in row_specs
    ]
    constants = [
        h16.value(records, (), (), coordinate)
        for _, coordinate, records in row_specs
    ]
    rhs = [-entry for entry in constants]
    matrix_lines = [
        "source\tcoordinate\tconstant\t"
        + "\t".join(f"q{e}" for e in h16.Q_EXPONENTS)
    ]
    for (source, coordinate, _), constant, row in zip(row_specs, constants, matrix):
        matrix_lines.append(
            f"{source}\t{coordinate}\t{h16.fraction_text(constant)}\t"
            + "\t".join(h16.fraction_text(entry) for entry in row)
        )
    matrix_text = "\n".join(matrix_lines) + "\n"
    matrix_sha = sha256(matrix_text.encode()).hexdigest()
    assert matrix_sha == "98a4a005a993971d794a46c6156531019ff5d8ab5490e8e579420c4fa314b489"

    work, transform, pivots = rref_with_transform(matrix, rhs)
    rank_coefficient = len(pivots)
    rank_augmented = h16.rank([[*row, rhs_entry] for row, rhs_entry in zip(matrix, rhs)])
    assert rank_coefficient == 12
    contradictory_rows = [
        row for row in range(22)
        if not any(work[row][column] for column in range(22)) and work[row][-1]
    ]
    assert (rank_augmented > rank_coefficient) == bool(contradictory_rows)

    if contradictory_rows:
        contradiction_row = contradictory_rows[0]
        functional = transform[contradiction_row]
        constant_residual = sum(
            functional[row] * constants[row] for row in range(22)
        )
        assert constant_residual and constant_residual == -work[contradiction_row][-1]
        functional = tuple(entry / constant_residual for entry in functional)
        assert sum(functional[row] * constants[row] for row in range(22)) == 1
        assert all(
            sum(functional[row] * matrix[row][column] for row in range(22)) == 0
            for column in range(22)
        )
        active = tuple(row for row, entry in enumerate(functional) if entry)
        assert active
        active_q_rows = tuple(
            row for row in active
            if any(matrix[row][column] for column in range(22))
        )
        omission_row = next(
            row for row in active if functional[row] * constants[row]
        )
        omitted = list(functional)
        omitted[omission_row] = Fraction(0)
        assert (
            sum(omitted[row] * constants[row] for row in range(22)) != 1
            or any(
                sum(omitted[row] * matrix[row][column] for row in range(22))
                for column in range(22)
            )
        )
        functional_lines = ["source\tcoordinate\tmultiplier"]
        functional_lines.extend(
            f"{row_specs[row][0]}\t{row_specs[row][1]}\t{h16.fraction_text(functional[row])}"
            for row in range(22)
        )
        functional_text = "\n".join(functional_lines) + "\n"
        (outdir / "P12_P13_COMPATIBILITY_DUAL_U1V3.tsv").write_text(functional_text)
        functional_sha = sha256(functional_text.encode()).hexdigest()
        result = (
            "base_point_U=1\nbase_point_V=3\nbase_point_C=8\n"
            "base_point_F=0\nbase_point_H=5\nbase_point_B3=81\n"
            "registered_open_nonzero=true\n"
            f"compatibility_matrix_sha256={matrix_sha}\n"
            f"coefficient_rank={rank_coefficient}\n"
            f"augmented_rank={rank_augmented}\n"
            "affine_compatibility_consistent=false\n"
            f"dual_functional_sha256={functional_sha}\n"
            f"dual_functional_active_rows={len(active)}\n"
            f"dual_functional_active_q_rows={len(active_q_rows)}\n"
            "dual_annihilates_all_22_q_columns=true\n"
            "dual_constant_value=1\n"
            "active_row_omission_negative_control=true\n"
            "rational_point_found=false\n"
            "single_base_fibre_only=true\nsource_point_claim=false\n"
            "whole_TD6_killed=false\nJC2_resolved=false\n"
        )
        (outdir / "P12_P13_AUGMENTED_GATE_RESULT.txt").write_text(result)
        print(result, end="")
        print(f"result_sha256={sha256(result.encode()).hexdigest()}")
        print("TD6-V89H16R1-P12-P13-DUAL-OBSTRUCTION PASS")
        return

    # Consistent singular case: emit the exact affine q space and leave the
    # y-dependent successor to a separately frozen client.
    free_columns = tuple(column for column in range(22) if column not in pivots)
    particular = [Fraction(0) for _ in range(22)]
    for row, column in enumerate(pivots):
        particular[column] = work[row][-1]
    assert all(
        sum(matrix[row][column] * particular[column] for column in range(22)) == rhs[row]
        for row in range(22)
    )
    affine_lines = ["kind\tindex\tvalue"]
    affine_lines.extend(
        f"particular\tq{h16.Q_EXPONENTS[column]}\t{h16.fraction_text(particular[column])}"
        for column in range(22)
    )
    for basis_index, free_column in enumerate(free_columns):
        vector = [Fraction(0) for _ in range(22)]
        vector[free_column] = Fraction(1)
        for row, pivot_column in enumerate(pivots):
            vector[pivot_column] = -work[row][free_column]
        assert all(
            sum(matrix[row][column] * vector[column] for column in range(22)) == 0
            for row in range(22)
        )
        affine_lines.extend(
            f"null_{basis_index}\tq{h16.Q_EXPONENTS[column]}\t{h16.fraction_text(vector[column])}"
            for column in range(22)
        )
    affine_text = "\n".join(affine_lines) + "\n"
    (outdir / "P12_P13_COMPATIBILITY_AFFINE_Q_SPACE_U1V3.tsv").write_text(affine_text)
    affine_sha = sha256(affine_text.encode()).hexdigest()
    result = (
        "base_point_U=1\nbase_point_V=3\nbase_point_C=8\n"
        f"compatibility_matrix_sha256={matrix_sha}\n"
        f"coefficient_rank={rank_coefficient}\n"
        f"augmented_rank={rank_augmented}\n"
        "affine_compatibility_consistent=true\n"
        f"affine_q_space_dimension={len(free_columns)}\n"
        f"affine_q_space_sha256={affine_sha}\n"
        "remaining_y_stage_deferred=true\n"
        "rational_point_found=false\nsource_point_claim=false\n"
        "whole_TD6_killed=false\nJC2_resolved=false\n"
    )
    (outdir / "P12_P13_AUGMENTED_GATE_RESULT.txt").write_text(result)
    print(result, end="")
    print(f"result_sha256={sha256(result.encode()).hexdigest()}")
    print("TD6-V89H16R1-P12-P13-AFFINE-Q-SPACE PASS")


if __name__ == "__main__":
    main()
