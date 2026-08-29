#!/usr/bin/env python3
"""Exact 24-axis CURRENT adjoint union and rank certificate.

This consumes the 22 V82QS single-q shards, both V82P4 dead-axis mirrors,
and both completed V82Q simultaneous q runs.  It does no source compilation;
it reconstructs the hash-printed E(C,V,U) scalars, verifies every digest and
semantic table equality, and computes the exact 24-column rank/kernel.
"""

from ast import literal_eval
import csv
import flint
from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import platform
import re
import socket
import sys


Q_EXPONENTS = tuple(range(2, 15)) + tuple(range(16, 25))
Q_AXES = tuple(f"q{exponent}" for exponent in Q_EXPONENTS)
DEAD_AXES = ("d10", "d15")
AXES = Q_AXES + DEAD_AXES
assert len(Q_AXES) == 22 and len(AXES) == 24 and "q15" not in AXES

assert platform.system() == "Linux", "REFUSED: V82QR requires Linux/AWS"
vendor = Path("/sys/devices/virtual/dmi/id/sys_vendor").read_text()
assert "Amazon EC2" in vendor, "REFUSED: V82QR requires Amazon EC2"
AWS_RUN_TAG = os.environ.get("AWS_RUN_TAG", "")
assert AWS_RUN_TAG.startswith("td6_v82qr_"), "REFUSED: registered V82QR tag required"
print(f"aws_hostname={socket.gethostname()}")
print(f"aws_run_tag={AWS_RUN_TAG}")

SOURCE_ROOT = Path(os.environ["V82QR_SOURCE_ROOT"]).resolve()
ALLQ_PATH = (
    SOURCE_ROOT / "payload" / "jc2" / "cases"
    / "td6_c1_c2_c3_all_q_vector_ad_repaired_20260825" / "replay.py"
)
ALLQ_SHA256 = "7e5ade2b0f8723e2ac502978fd8ea48470e57231a83c8e8c0a233f64948b695d"
assert sha256(ALLQ_PATH.read_bytes()).hexdigest() == ALLQ_SHA256
spec = importlib.util.spec_from_file_location("td6_v82qr_allq", ALLQ_PATH)
allq = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = allq
spec.loader.exec_module(allq)

tri, r = allq.tri, allq.r
Rat3, E3 = allq.Rat3, allq.E3
C, V, U = allq.C, allq.V, allq.U

Q_BOX03 = Path(os.environ["V82QR_Q_SHARDS_BOX03"]).resolve()
Q_R6D = Path(os.environ["V82QR_Q_SHARDS_R6D"]).resolve()
DEAD_BOX03 = Path(os.environ["V82QR_DEAD_BOX03"]).resolve()
DEAD_R6D = Path(os.environ["V82QR_DEAD_R6D"]).resolve()
MONO_BOX03 = Path(os.environ["V82QR_Q_MONOLITH_BOX03"]).resolve()
MONO_R6D = Path(os.environ["V82QR_Q_MONOLITH_R6D"]).resolve()
OUT = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
OUT.mkdir(parents=True, exist_ok=True)

SAFE_POLY = re.compile(r"^[0-9CVU+*/^(). -]+$")
RATIONAL = re.compile(r"(?<![A-Za-z0-9_])(-?[0-9]+)/([0-9]+)(?![A-Za-z0-9_])")


def digest(data):
    return sha256(data).hexdigest()


def read_text(path):
    data = path.read_bytes()
    return data, data.decode()


def assert_success(root, pass_line):
    assert (root / "rc").read_text().strip() == "0", root
    lines = (root / "stdout").read_text().splitlines()
    assert pass_line in lines, (root, pass_line)


def parse_poly(text):
    assert SAFE_POLY.fullmatch(text), text
    expression = RATIONAL.sub(r"Q(\1,\2)", text.replace("^", "**"))
    return eval(
        expression,
        {"__builtins__": {}},
        {"C": C, "V": V, "U": U, "Q": flint.fmpq},
    )


def parse_exact(text):
    data = literal_eval(text)
    expected = len(r.scalar_exact(E3(1)))
    assert isinstance(data, tuple) and len(data) == expected
    coordinates = []
    for numerator, denominator in data:
        assert isinstance(numerator, str) and isinstance(denominator, str)
        coordinates.append(Rat3(parse_poly(numerator), parse_poly(denominator)))
    value = E3(tri.FIELD.from_coordinates(tuple(coordinates)))
    assert allq.e3_exact(value) == text
    assert allq.e3_digest(value) == digest(repr(data).encode())
    return value


def parser_preflight():
    coordinates = [("15625/3*V*U", "1")] + [("0", "1")] * 17
    text = repr(tuple(coordinates))
    value = parse_exact(text)
    assert value and allq.e3_exact(value) == text
    assert parse_poly("-1/2*V^4+3*C*U") == -flint.fmpq(1, 2)*V**4 + 3*C*U
    print("exact_scalar_parser_positive_control=true")
    print("exact_rational_coefficient_and_power_control=true")


def read_table(path, axis_kind, required_axis=None):
    with path.open(newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        rows = list(reader)
    expected_columns = [
        "compatibility", "key", "coordinate", axis_kind,
        "coefficient_sha256", "coefficient_exact",
    ]
    assert reader.fieldnames == expected_columns
    out = {}
    for row in rows:
        raw_axis = row[axis_kind]
        axis = f"q{raw_axis}" if axis_kind == "exponent" else raw_axis
        if required_axis is not None:
            assert axis == required_axis
        assert axis in AXES
        key = (int(row["compatibility"]), row["key"], row["coordinate"])
        value = parse_exact(row["coefficient_exact"])
        assert allq.e3_digest(value) == row["coefficient_sha256"]
        assert key not in out
        out[key] = (axis, value, row["coefficient_exact"], row["coefficient_sha256"])
    return out


def tag_table(table):
    return {(key, record[0]): record for key, record in table.items()}


def semantic_tagged(table):
    return {tagged: (record[2], record[3]) for tagged, record in table.items()}


def read_q_shards():
    combined = {}
    for exponent in Q_EXPONENTS:
        root = (Q_BOX03 if exponent <= 12 else Q_R6D) / f"q{exponent}"
        assert_success(root, "TD6-V82QS-SINGLE-Q-CURRENT-ADJOINT PASS")
        table = read_table(
            root / "output" / "CURRENT_CONORMAL.tsv", "exponent", f"q{exponent}"
        )
        for key, record in table.items():
            tagged = (key, record[0])
            assert tagged not in combined
            combined[tagged] = record
    assert {axis for _, axis in combined} <= set(Q_AXES)
    return combined


def read_q_monolith(root):
    assert_success(root, "TD6-A3-ALL-Q-VECTOR-AD-STAGED PASS")
    table = read_table(root / "output" / "CURRENT_CONORMAL.tsv", "exponent")
    return tag_table(table)


def read_dead_axis(axis):
    level = axis[1:]
    left = DEAD_BOX03 / "lanes" / axis
    right = DEAD_R6D / "lanes" / axis
    pass_line = "TD6-A3-KERNEL-DEAD-CURRENT-ADJOINT-SHARD-V82P4 PASS"
    assert_success(left, pass_line)
    assert_success(right, pass_line)
    name = f"D{level}_CURRENT_ADJOINT.tsv"
    left_bytes, _ = read_text(left / "evidence" / name)
    right_bytes, _ = read_text(right / "evidence" / name)
    assert left_bytes == right_bytes
    left_table = read_table(left / "evidence" / name, "axis", axis)
    right_table = read_table(right / "evidence" / name, "axis", axis)
    left_tagged, right_tagged = tag_table(left_table), tag_table(right_table)
    assert semantic_tagged(left_tagged) == semantic_tagged(right_tagged)
    return left_tagged


def rref_kernel(matrix):
    reduced, pivots = allq.matrix_rref(matrix)
    free = [column for column in range(len(AXES)) if column not in pivots]
    kernel = []
    for free_column in free:
        vector = [E3() for _ in AXES]
        vector[free_column] = E3(1)
        for row_index, pivot_column in enumerate(pivots):
            vector[pivot_column] = -reduced[row_index][free_column]
        kernel.append(vector)
    for row in matrix:
        for vector in kernel:
            assert not sum(
                (coefficient * entry for coefficient, entry in zip(row, vector)),
                E3(),
            )
    return pivots, kernel


def main():
    parser_preflight()
    if "--parser-preflight" in sys.argv:
        print("TD6-V82QR-EXACT-PARSER-PREFLIGHT PASS")
        return
    print("producer=TD6-V82QR-CURRENT-24D-EXACT-UNION")
    print("source_compiler_open=D(U*H*B3)")
    print("stageA_rank_open_for_composition=D(U*H*B3*R38)")
    print("R38_zero_rank_drop_fibre_remains_debt=true")
    print("scope=fixed_A3_common_principal_open_current_adjoint_scheduling")
    print("base_current_system_already_inconsistent=true")
    print("no_tangent_family_TD6_SP2_landing_or_JC2_claim=true", flush=True)

    q_shards = read_q_shards()
    q_mono_box03 = read_q_monolith(MONO_BOX03)
    q_mono_r6d = read_q_monolith(MONO_R6D)
    assert semantic_tagged(q_mono_box03) == semantic_tagged(q_mono_r6d)
    assert semantic_tagged(q_shards) == semantic_tagged(q_mono_box03)
    print("all_22_q_shards_complete_disjoint_and_q15_excluded=true")
    print("q_shard_union_matches_both_simultaneous_monoliths_exact=true")

    combined = dict(q_shards)
    for axis in DEAD_AXES:
        dead = read_dead_axis(axis)
        for tagged, record in dead.items():
            assert tagged not in combined
            combined[tagged] = record
    assert {axis for _, axis in combined} <= set(AXES)
    print("dead_d10_d15_dual_host_tables_byte_and_expression_equal=true")

    row_keys = sorted({key for key, _ in combined})
    matrix = []
    for key in row_keys:
        matrix.append([
            combined.get((key, axis), (axis, E3(), "", ""))[1]
            for axis in AXES
        ])
    pivots, kernel = rref_kernel(matrix)

    table_lines = [
        "compatibility\tkey\tcoordinate\taxis\tcoefficient_sha256\t"
        "coefficient_exact"
    ]
    for key in row_keys:
        for axis in AXES:
            record = combined.get((key, axis))
            if record is not None:
                table_lines.append(
                    f"{key[0]}\t{key[1]}\t{key[2]}\t{axis}\t"
                    f"{record[3]}\t{record[2]}"
                )
    table_text = "\n".join(table_lines) + "\n"
    table_path = OUT / "CURRENT_24D_ADJOINT.exact.tsv"
    table_path.write_text(table_text)

    kernel_lines = ["kernel_vector\taxis\tcoefficient_sha256\tcoefficient_exact"]
    for index, vector in enumerate(kernel):
        for axis, value in zip(AXES, vector):
            if value:
                kernel_lines.append(
                    f"{index}\t{axis}\t{allq.e3_digest(value)}\t{allq.e3_exact(value)}"
                )
    kernel_text = "\n".join(kernel_lines) + "\n"
    kernel_path = OUT / "CURRENT_24D_KERNEL.exact.tsv"
    kernel_path.write_text(kernel_text)

    pivot_text = "\n".join(AXES[column] for column in pivots) + "\n"
    pivot_path = OUT / "CURRENT_24D_PIVOT_AXES.txt"
    pivot_path.write_text(pivot_text)

    charged = [record[1] for record in combined.values()]
    charged.extend(value for vector in kernel for value in vector)
    denominator = allq.denominator_for(charged) if charged else tri.ONE
    assert allq.factors_only_allowed(denominator)
    denominator_text = repr(denominator.factor()) + "\n"
    denominator_path = OUT / "CURRENT_24D.denominator.factor.txt"
    denominator_path.write_text(denominator_text)

    print(f"current_24d_coordinate_count={len(row_keys)}")
    print(f"current_24d_nonzero_entry_count={len(combined)}")
    print(f"current_24d_rank={len(pivots)}/24")
    print(f"current_24d_kernel_dimension={len(kernel)}")
    print("current_24d_pivot_axes=" + ",".join(AXES[column] for column in pivots))
    print(f"current_24d_denominator_factor={denominator.factor()}")
    print(f"current_24d_table_sha256={digest(table_text.encode())}")
    print(f"current_24d_kernel_sha256={digest(kernel_text.encode())}")
    print(f"current_24d_pivots_sha256={digest(pivot_text.encode())}")
    print(f"current_24d_denominator_sha256={digest(denominator_text.encode())}")
    print("conormal_at_empty_base_is_scheduling_only=true")
    print("TD6-V82QR-CURRENT-24D-EXACT-UNION PASS")


if __name__ == "__main__":
    main()
