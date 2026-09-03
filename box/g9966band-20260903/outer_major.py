#!/usr/bin/env python3
"""Exact-Q structural certificate for the (99,66) outer major block.

This driver treats only the four outer coefficient blocks A2, A3, B1, B2.
It uses the invertible shifted basis

    t^D A(t^-1,w/t) = sum A_s(r,q) t^r (w-1)^q

and the canonical filtration W=3*r+4*q.  The D2 preblock kills W<W0.
For the D1 child it uses t=e^9 and w-1=e^12*(1+Pi*e), so a shifted
coordinate contributes binomial(q,k) to row (E,k), E=3*W+k.  All ranks
are computed by sparse Gaussian elimination over fractions.Fraction.

The certificate is structural: it records the homogeneous outer-coordinate
matrices and their Q* pivots.  It does not claim compatibility of any omitted
inner forcing, a minor-incidence system, or a Jacobian system.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from math import comb
from pathlib import Path
import resource
import time
from typing import Iterable


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RECEIPT = ROOT / "xmodel/g9966-global-band-sol56-20260903.run.v2"


@dataclass(frozen=True)
class Block:
    name: str
    degree: int
    y_cap: int
    pole_loss: int

    @property
    def d2_weight_cutoff(self) -> int:
        # t^D A has required t-order D-pole_loss at the denominator-3 node.
        return 3 * (self.degree - self.pole_loss)

    @property
    def d1_e_cutoff(self) -> int:
        # At t=e^9, ord(A)>=-pole_loss/9 becomes E>=9D-pole_loss.
        return 9 * self.degree - self.pole_loss


BLOCKS = (
    Block("A2", 65, 32, 2),
    Block("A3", 98, 32, 3),
    Block("B1", 32, 32, 1),
    Block("B2", 65, 32, 2),
)

# Audited values are assertions, never inputs to the enumeration or rank.
EXPECTED = {
    "A2": {"ambient": 1650, "d2_raw": 3934, "d2_rank": 1386,
           "d2_survivors": 264, "d1_raw": 51, "d1_rank": 44,
           "full_rank": 1430, "free": 220},
    "A3": {"ambient": 2739, "d2_raw": 7034, "d2_rank": 2442,
           "d2_survivors": 297, "d1_raw": 108, "d1_rank": 73,
           "full_rank": 2515, "free": 224},
    "B1": {"ambient": 561, "d2_raw": 1032, "d2_rank": 384,
           "d2_survivors": 177, "d1_raw": 15, "d1_rank": 15,
           "full_rank": 399, "free": 162},
    "B2": {"ambient": 1650, "d2_raw": 3934, "d2_rank": 1386,
           "d2_survivors": 264, "d1_raw": 51, "d1_rank": 44,
           "full_rank": 1430, "free": 220},
}
EXPECTED_TOTAL = {
    "ambient": 6600,
    "d2_raw": 15934,
    "d2_rank": 5598,
    "d2_survivors": 1002,
    "d1_raw": 225,
    "d1_rank": 176,
    "full_raw": 16159,
    "full_rank": 5774,
    "free": 826,
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_lines(lines: Iterable[str]) -> str:
    digest = hashlib.sha256()
    for line in lines:
        digest.update(line.encode("utf-8"))
        digest.update(b"\n")
    return digest.hexdigest()


def verify_frozen_inputs() -> dict:
    fields: dict[str, str] = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value

    count = int(fields["charged_inputs"])
    assert count == 20
    frozen = Path(fields["lane_inputs_dir"])
    entries = []
    manifest_lines = []
    for index in range(1, count + 1):
        basename = fields[f"charged_input_{index}_basename"]
        expected = fields[f"charged_input_{index}_sha256"]
        assert Path(basename).name == basename
        path = frozen / basename
        actual = sha256_file(path)
        assert actual == expected
        manifest_lines.append(f"{expected}  {path}")
        entries.append({
            "index": index,
            "basename": basename,
            "sha256": expected,
        })
    return {
        "receipt": str(RECEIPT),
        "receipt_sha256": sha256_file(RECEIPT),
        "lane_inputs_dir": str(frozen),
        "charged_inputs": count,
        "all_hashes_match": True,
        "mechanical_manifest_sha256": sha256_lines(manifest_lines),
        "entries": entries,
    }


def weight(position: tuple[int, int]) -> int:
    r, q = position
    return 3 * r + 4 * q


def shifted_name(block: Block, position: tuple[int, int]) -> str:
    r, q = position
    return f"{block.name}s_{r}_{q}"


def standard_name(block: Block, position: tuple[int, int]) -> str:
    r, q = position
    i = block.degree - r - q
    return f"{block.name}_{i}_{q}"


def position_key(position: tuple[int, int]) -> tuple[int, int, int]:
    r, q = position
    return weight(position), q, r


def positions(block: Block) -> tuple[tuple[int, int], ...]:
    # r=D-i-j is the total-degree deficit and q is the shifted-basis degree.
    return tuple(sorted(
        (
            (r, q)
            for r in range(block.degree + 1)
            for q in range(min(block.y_cap, block.degree - r) + 1)
        ),
        key=position_key,
    ))


def build_recenter_rows(
    block: Block,
    source_positions: Iterable[tuple[int, int]],
) -> dict[tuple[int, int], dict[str, Fraction]]:
    """Return rows keyed by (W,k), equivalently (E=3W+k, Pi-degree k)."""
    rows: dict[tuple[int, int], dict[str, Fraction]] = {}
    for position in source_positions:
        _, q = position
        W = weight(position)
        name = shifted_name(block, position)
        for k in range(q + 1):
            E = 3 * W + k
            if E >= block.d1_e_cutoff:
                continue
            row = rows.setdefault((W, k), {})
            assert name not in row
            row[name] = Fraction(comb(q, k), 1)
    return rows


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def canonical_row_lines(
    block: Block,
    rows: dict[tuple[int, int], dict[str, Fraction]],
    name_order: dict[str, int],
) -> Iterable[str]:
    for W, k in sorted(rows):
        E = 3 * W + k
        entries = sorted(rows[(W, k)].items(), key=lambda item: name_order[item[0]])
        encoded = ";".join(f"{name}:{fraction_text(value)}" for name, value in entries)
        yield f"{block.name}|W={W}|E={E}|k={k}|{encoded}"


def sparse_qstar(
    rows: list[tuple[tuple[int, int], dict[str, Fraction]]],
    column_names: list[str],
) -> tuple[list[dict], int]:
    """Deterministic exact row echelon; returned rows are a rank witness."""
    column_index = {name: index for index, name in enumerate(column_names)}
    basis: list[tuple[str, dict[str, Fraction]]] = []
    pivots: list[dict] = []
    dependent_zero = 0

    for (W, k), source in rows:
        vector = dict(source)
        for pivot_name, pivot_row in basis:
            scalar = vector.get(pivot_name, Fraction(0))
            if scalar == 0:
                continue
            for name, coefficient in pivot_row.items():
                value = vector.get(name, Fraction(0)) - scalar * coefficient
                if value:
                    vector[name] = value
                else:
                    vector.pop(name, None)
        if not vector:
            dependent_zero += 1
            continue
        pivot_name = min(vector, key=column_index.__getitem__)
        diagonal = vector[pivot_name]
        assert diagonal != 0
        normalized = {name: coefficient / diagonal for name, coefficient in vector.items()}
        basis.append((pivot_name, normalized))
        pivots.append({
            "row": f"e{3 * W}_plus_{k}__Pi{k}",
            "weight": W,
            "e_power": 3 * W + k,
            "offset": k,
            "pivot": pivot_name,
            "diagonal": fraction_text(diagonal),
        })
    return pivots, dependent_zero


def analyze_stage(
    block: Block,
    stage_positions: tuple[tuple[int, int], ...],
    name_order: dict[str, int],
    include_offsets: bool,
) -> dict:
    rows = build_recenter_rows(block, stage_positions)
    positions_by_weight: dict[int, list[tuple[int, int]]] = {}
    rows_by_weight: dict[int, list[tuple[tuple[int, int], dict[str, Fraction]]]] = {}
    for position in stage_positions:
        W = weight(position)
        if 3 * W < block.d1_e_cutoff:
            positions_by_weight.setdefault(W, []).append(position)
    for label, row in rows.items():
        rows_by_weight.setdefault(label[0], []).append((label, row))

    all_pivots = []
    dependent_total = 0
    bands = []
    for W in sorted(rows_by_weight):
        group_positions = sorted(positions_by_weight[W], key=lambda item: (item[1], item[0]))
        group_columns = [shifted_name(block, item) for item in group_positions]
        group_rows = sorted(rows_by_weight[W], key=lambda item: item[0][1])
        pivots, dependent = sparse_qstar(group_rows, group_columns)
        # At fixed W the admissible q-values are an arithmetic progression
        # of step three.  The binomial-evaluation matrix therefore has the
        # Newton diagonal 1,3,3^2,... for the selected rows k=0,1,... .
        q_values = [q for _, q in group_positions]
        assert all(right - left == 3 for left, right in zip(q_values, q_values[1:]))
        assert [item["diagonal"] for item in pivots] == [
            str(3 ** index) for index in range(len(pivots))
        ]
        all_pivots.extend(pivots)
        dependent_total += dependent
        offsets = [label[1] for label, _ in group_rows]
        band = {
            "weight": W,
            "baseline_e_power": 3 * W,
            "raw_rows": len(group_rows),
            "source_columns": len(group_columns),
            "rank": len(pivots),
            "dependent_zero_rows": dependent,
            "qstar_diagonal": [item["diagonal"] for item in pivots],
        }
        if include_offsets:
            band["offsets"] = offsets
            band["source_q_values"] = [q for _, q in group_positions]
            band["pivot_names"] = [item["pivot"] for item in pivots]
        bands.append(band)

    row_hash = sha256_lines(canonical_row_lines(block, rows, name_order))
    pivot_hash = sha256_lines(
        f"{item['row']}|{item['pivot']}|{item['diagonal']}" for item in all_pivots
    )
    return {
        "raw_row_count": len(rows),
        "raw_rows_sha256": row_hash,
        "rank": len(all_pivots),
        "dependent_zero_rows": dependent_total,
        "pivot_names": [item["pivot"] for item in all_pivots],
        "pivot_names_sha256": sha256_lines(item["pivot"] for item in all_pivots),
        "qstar_witness_sha256": pivot_hash,
        "qstar_all_nonzero": all(Fraction(item["diagonal"]) != 0 for item in all_pivots),
        "qstar_max_denominator": max(
            (Fraction(item["diagonal"]).denominator for item in all_pivots), default=1
        ),
        "weight_bands": bands,
    }


def shifted_basis_inverse_control() -> bool:
    # s_q=sum_{j>=q} C(j,q)a_j and
    # a_j=sum_{q>=j} (-1)^(q-j)C(q,j)s_q.  Check both products at cap 32.
    size = 33
    transform = [[0] * size for _ in range(size)]
    inverse = [[0] * size for _ in range(size)]
    for q in range(size):
        for j in range(q, size):
            transform[q][j] = comb(j, q)
            inverse[q][j] = (-1) ** (j - q) * comb(j, q)
    for left, right in ((transform, inverse), (inverse, transform)):
        for row in range(size):
            for column in range(size):
                value = sum(left[row][mid] * right[mid][column] for mid in range(size))
                if value != int(row == column):
                    return False
    return True


def analyze_block(block: Block) -> dict:
    ambient_positions = positions(block)
    names = [shifted_name(block, item) for item in ambient_positions]
    assert len(names) == len(set(names))
    name_order = {name: index for index, name in enumerate(names)}

    d2_pivots = tuple(
        item for item in ambient_positions if weight(item) < block.d2_weight_cutoff
    )
    d2_survivors = tuple(
        item for item in ambient_positions if weight(item) >= block.d2_weight_cutoff
    )
    assert set(d2_pivots).isdisjoint(d2_survivors)
    assert set(d2_pivots) | set(d2_survivors) == set(ambient_positions)

    d2 = analyze_stage(block, d2_pivots, name_order, include_offsets=False)
    d1 = analyze_stage(block, d2_survivors, name_order, include_offsets=True)
    d2_pivot_names = d2["pivot_names"]
    survivor_names = [shifted_name(block, item) for item in d2_survivors]
    d1_pivot_names = d1["pivot_names"]
    d1_pivot_set = set(d1_pivot_names)
    free_names = [name for name in survivor_names if name not in d1_pivot_set]

    expected = EXPECTED[block.name]
    actual = {
        "ambient": len(ambient_positions),
        "d2_raw": d2["raw_row_count"],
        "d2_rank": d2["rank"],
        "d2_survivors": len(d2_survivors),
        "d1_raw": d1["raw_row_count"],
        "d1_rank": d1["rank"],
        "full_rank": d2["rank"] + d1["rank"],
        "free": len(free_names),
    }
    assert actual == expected
    assert d2["rank"] == len(d2_pivots)
    assert d2["dependent_zero_rows"] == d2["raw_row_count"] - d2["rank"]
    assert d1["dependent_zero_rows"] == d1["raw_row_count"] - d1["rank"]
    assert len(set(d2_pivot_names)) == len(d2_pivot_names)
    assert set(d2_pivot_names) == {
        shifted_name(block, item) for item in d2_pivots
    }
    assert set(d2_pivot_names).isdisjoint(d1_pivot_names)
    assert set(d2_pivot_names).isdisjoint(free_names)
    assert set(d1_pivot_names).isdisjoint(free_names)
    assert set(d2_pivot_names) | set(d1_pivot_names) | set(free_names) == set(names)

    # An independent set comprehension re-enumerates the literal row labels.
    independent_d2_labels = {
        (3 * weight(item) + k, k)
        for item in d2_pivots
        for k in range(item[1] + 1)
        if 3 * weight(item) + k < block.d1_e_cutoff
    }
    independent_d1_labels = {
        (3 * weight(item) + k, k)
        for item in d2_survivors
        for k in range(item[1] + 1)
        if 3 * weight(item) + k < block.d1_e_cutoff
    }
    assert len(independent_d2_labels) == d2["raw_row_count"]
    assert len(independent_d1_labels) == d1["raw_row_count"]

    # Avoid repeating thousands of names inside the stage objects.
    d2.pop("pivot_names")
    d1.pop("pivot_names")
    return {
        "block": block.name,
        "polynomial_degree_cap": block.degree,
        "y_degree_cap": block.y_cap,
        "order_data": {
            "D2_required_order": f">=-{block.pole_loss}/3",
            "D2_weight_cutoff": block.d2_weight_cutoff,
            "D2_rule": "pivot iff W < D2_weight_cutoff",
            "D1_required_order": f">=-{block.pole_loss}/9",
            "D1_e_cutoff": block.d1_e_cutoff,
            "D1_rule": "kill every [e^E Pi^k] row with E < D1_e_cutoff",
        },
        "ambient": {
            "count": len(names),
            "names_sha256": sha256_lines(names),
        },
        "D2_preblock": {
            **d2,
            "literal_raw_definition": (
                "unique (E,k) hit by W<W0 shifted coordinates, "
                "E=9r+12q+k=3W+k<M"
            ),
            "pivot_count": len(d2_pivot_names),
            "pivot_names": d2_pivot_names,
            "survivor_count": len(survivor_names),
            "survivor_names": survivor_names,
            "survivor_names_sha256": sha256_lines(survivor_names),
        },
        "D1_boundary_mod_D2": {
            **d1,
            "raw_definition": (
                "unique (E,k) hit by W>=W0 survivors, "
                "E=9r+12q+k=3W+k<M"
            ),
            "pivot_count": len(d1_pivot_names),
            "pivot_names": d1_pivot_names,
            "free_count": len(free_names),
            "free_names": free_names,
            "free_names_sha256": sha256_lines(free_names),
        },
        "full": {
            "raw_rows": d2["raw_row_count"] + d1["raw_row_count"],
            "rank": len(d2_pivot_names) + len(d1_pivot_names),
            "free": len(free_names),
            "all_pivot_names_sha256": sha256_lines(d2_pivot_names + d1_pivot_names),
        },
        "controls": {
            "audited_counts_match": True,
            "D2_Qstar_rank_equals_forbidden_coordinate_count": True,
            "D2_and_D1_pivots_disjoint": True,
            "pivots_and_free_partition_ambient": True,
            "literal_raw_labels_independently_reenumerated": True,
            "zero_assignment_satisfies_homogeneous_rows": True,
            "every_selected_Qstar_diagonal_nonzero": (
                d2["qstar_all_nonzero"] and d1["qstar_all_nonzero"]
            ),
            "binomial_Newton_diagonal_is_1_3_3sq_etc_in_every_weight_band": True,
        },
    }


def main() -> None:
    started = time.perf_counter()
    custody = verify_frozen_inputs()
    basis_control = shifted_basis_inverse_control()
    assert basis_control

    block_results = [analyze_block(block) for block in BLOCKS]
    all_d2_pivots = [
        name
        for result in block_results
        for name in result["D2_preblock"]["pivot_names"]
    ]
    all_survivors = [
        name
        for result in block_results
        for name in result["D2_preblock"]["survivor_names"]
    ]
    all_d1_pivots = [
        name
        for result in block_results
        for name in result["D1_boundary_mod_D2"]["pivot_names"]
    ]
    all_free = [
        name
        for result in block_results
        for name in result["D1_boundary_mod_D2"]["free_names"]
    ]
    total = {
        "ambient": sum(result["ambient"]["count"] for result in block_results),
        "d2_raw": sum(result["D2_preblock"]["raw_row_count"] for result in block_results),
        "d2_rank": len(all_d2_pivots),
        "d2_survivors": len(all_survivors),
        "d1_raw": sum(
            result["D1_boundary_mod_D2"]["raw_row_count"] for result in block_results
        ),
        "d1_rank": len(all_d1_pivots),
        "full_raw": sum(result["full"]["raw_rows"] for result in block_results),
        "full_rank": len(all_d2_pivots) + len(all_d1_pivots),
        "free": len(all_free),
    }
    assert total == EXPECTED_TOTAL
    assert len(set(all_d2_pivots)) == len(all_d2_pivots)
    assert len(set(all_survivors)) == len(all_survivors)
    assert len(set(all_d1_pivots)) == len(all_d1_pivots)
    assert len(set(all_free)) == len(all_free)
    assert set(all_d2_pivots).isdisjoint(all_survivors)
    assert set(all_d1_pivots).issubset(all_survivors)
    assert set(all_free) == set(all_survivors) - set(all_d1_pivots)

    output = {
        "schema": "jc2.g9966.outer-major-exact-Q/v1",
        "type": "EXACT-Q-STRUCTURAL-CERTIFICATE / OUTER-FG-MAJOR",
        "scope": {
            "proved": [
                "outer A2/A3/B1/B2 shifted-basis D2 coefficient-matrix ranks",
                "canonical D1 boundary row-matrix ranks modulo the D2 pivots",
                "the exact 6600 -> 826 outer-coordinate structural count",
            ],
            "not_proved": [
                "compatibility with omitted inner affine forcing",
                "either minor-incidence branch",
                "any Jacobian band",
                "a Keller representative",
            ],
        },
        "field": "Q",
        "basis_and_map": {
            "normalization": "t^D A(t^-1,w/t)",
            "standard_coordinate": "A_i_j = [x^i y^j]A",
            "position": "r=D-i-j, 0<=q<=min(32,D-r)",
            "shifted_coordinate": "As_r_q = [t^r (w-1)^q] t^D A(t^-1,w/t)",
            "forward_map": "As_r_q=sum_{j=q}^{min(32,D-r)} binom(j,q) A_(D-r-j)_j",
            "inverse_map": "A_(D-r-j)_j=sum_{q=j}^{min(32,D-r)} (-1)^(q-j) binom(q,j) As_r_q",
            "filtration": "W=3r+4q",
            "D1_recenter": "t=e^9, w-1=e^12(1+Pi*e)",
            "map_bijective_over_Q": basis_control,
        },
        "frozen_input_verification": custody,
        "blocks": block_results,
        "totals": {
            **total,
            "outer_free_names": all_free,
            "outer_free_names_sha256": sha256_lines(all_free),
            "D2_pivot_names_sha256": sha256_lines(all_d2_pivots),
            "D2_survivor_names_sha256": sha256_lines(all_survivors),
            "D1_pivot_names_sha256": sha256_lines(all_d1_pivots),
            "all_pivot_names_sha256": sha256_lines(all_d2_pivots + all_d1_pivots),
        },
        "controls": {
            "current_receipt_has_20_verified_inputs": True,
            "shifted_basis_forward_inverse_products_are_identity": basis_control,
            "all_four_block_audited_counts_match": True,
            "audited_preblock_raw_rank": [15934, 5598],
            "audited_boundary_raw_rank": [225, 176],
            "audited_full_raw_rank": [16159, 5774],
            "audited_outer_free": 826,
            "no_nonlinear_rows_in_structural_outer_system": True,
            "homogeneous_system_consistent_at_zero": True,
        },
        "runtime": {
            "wall_seconds": time.perf_counter() - started,
            "max_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
