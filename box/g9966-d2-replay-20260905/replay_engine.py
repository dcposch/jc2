#!/usr/bin/env python3
"""D2-floor replay of the (99,66) joint band engine.

The charged engine (original_band_engine.py, SHA-256
3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9)
zeros unknowns by a raw D2 weight floor that is exact only for a centered
D2 generic point.  This driver keeps the SOUND pieces — the face z^8 w^3,
the total-degree cap (G_i at d=1), the branch-map assignments that come
from the face equations, the seven charged h2 D1 pivots, and the outer D1
bands — and FREES every coordinate the floor had set to zero.

qstar_reduce is imported from the pinned original engine (rational pivots
only).  Dropping ROWS would be safe; dropping UNKNOWNS by a weight floor
is not (FALLACY-v2).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
import resource
from math import comb
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import original_band_engine as orig  # noqa: E402

ORIGINAL_ENGINE_SHA256 = "3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9"
H2_D1_THRESHOLD = 296  # e-exponents 3W+k < 296; original W=97,k=0..4 and W=98,k=0..1
EQUALITY_FACE = {(4 * k, 24 - 3 * k): sp.Integer((-1) ** k * comb(8, k)) for k in range(1, 9)}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_our_inputs() -> dict:
    receipt = HERE / "receipt.run.v2"
    frozen = HERE / "frozen"
    fields: dict[str, str] = {}
    for line in receipt.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    count = int(fields["charged_inputs"])
    checked = []
    for index in range(1, count + 1):
        name = fields[f"charged_input_{index}_basename"]
        expected = fields[f"charged_input_{index}_sha256"]
        actual = sha256(frozen / name)
        assert actual == expected, f"charged input mismatch: {name}"
        checked.append((name, actual))
    engine_sha = sha256(HERE / "original_band_engine.py")
    assert engine_sha == ORIGINAL_ENGINE_SHA256
    return {
        "receipt": str(receipt),
        "frozen_dir": str(frozen),
        "count": count,
        "all_hashes_match": True,
        "original_engine_sha256": engine_sha,
        "replay_engine_sha256": sha256(Path(__file__)),
        "lane_inputs_dir_on_receipt": fields.get("lane_inputs_dir"),
        "manifest_sha256": hashlib.sha256(
            "".join(f"{h}  {name}\n" for name, h in checked).encode()
        ).hexdigest(),
    }


def old_vmin(r: int) -> int:
    return max(0, (33 - 3 * r + 3) // 4)


def h3_template() -> tuple[orig.TZ, list[sp.Symbol], dict]:
    """Face z^8 w^3 and cap=11-r kept; D2 vmin floor freed as z-monomials."""
    out: orig.TZ = {(0, 8): 1, (0, 9): 3, (0, 10): 3, (0, 11): 1}
    variables: list[sp.Symbol] = []
    floor_freed: list[sp.Symbol] = []
    surviving: list[sp.Symbol] = []
    for r in range(1, 12):
        cap = 11 - r
        vmin_orig = old_vmin(r)
        for q in range(vmin_orig):
            variable = orig.symbol(f"Hc_{r}_{q}")
            variables.append(variable)
            floor_freed.append(variable)
            out[(r, q)] = out.get((r, q), 0) + variable
        for degree in range(vmin_orig, cap + 1):
            variable = orig.symbol(f"Hc_{r}_{degree}")
            variables.append(variable)
            surviving.append(variable)
            for j in range(degree - vmin_orig + 1):
                out[(r, vmin_orig + j)] = (
                    out.get((r, vmin_orig + j), 0) + variable * comb(degree - vmin_orig, j)
                )
    assert len(surviving) == 21
    assert len(floor_freed) == 45
    assert len(variables) == 66
    meta = {
        "face": "z^8 w^3",
        "cap": "11-r (G_1 at d=1, SOUND)",
        "old_vmin_formula": "ceil((33-3r)/4)",
        "floor_freed_count": 45,
        "surviving_original_count": 21,
        "h3_template_variables": 66,
        "floor_freed": [str(v) for v in floor_freed],
        "surviving": [str(v) for v in surviving],
    }
    return (
        {key: sp.expand(value) for key, value in out.items() if value != 0},
        variables,
        meta,
        floor_freed,
        surviving,
    )


def h3_face_rows(branch: str, h3: orig.TZ) -> tuple[list[tuple[str, sp.Expr]], dict]:
    rho, u, v, c = map(orig.symbol, ("rho", "u", "v", "c"))
    if branch == "delta2":
        max_power = 9
        expected = {9: {2: 3 * rho, 3: 1}}
        target = "t^9*zeta^2*(zeta+3*rho)"
    else:
        max_power = 21
        expected = {21: {1: -c, 3: 1}}
        target = "s^21*pi*(pi^2-c)"
    table = orig.local_rows(h3, branch, max_power, exact_only=False)
    rows: list[tuple[str, sp.Expr]] = []
    for n in range(max_power + 1):
        ks = {k for (power, k) in table if power == n} | set(expected.get(n, {}))
        for k in sorted(ks):
            got = table.get((n, k), 0)
            want = expected.get(n, {}).get(k, 0)
            diff = sp.expand(got - want)
            if diff != 0:
                rows.append((f"h3_face_local{n}_coord{k}", diff))
    return rows, {
        "target": target,
        "max_power": max_power,
        "face_row_count": len(rows),
        "note": "face equations on the enlarged h3; original 21 still match after extras=0",
    }


def build_major_h2(branch: str, max_t: int) -> tuple[orig.TZ, set[sp.Symbol], dict, list]:
    h3, hvars, h3meta, floor_freed, surviving = h3_template()
    hmap, hfree, centre = orig.h3_branch_map(branch)
    # Branch map assigns only the original 21 (face-proved). Floor-freed stay free.
    h3_mapped = {key: orig.substitute_map(value, hmap) for key, value in h3.items()}

    extras_zero = {var: sp.Integer(0) for var in floor_freed}
    h3_original_specialization = {
        key: orig.substitute_map(value, extras_zero) for key, value in h3_mapped.items()
    }
    control = orig.h3_minor_control(branch, h3_original_specialization)
    face_rows, face_meta = h3_face_rows(branch, h3_mapped)

    h3cube = orig.tz_mul(orig.tz_mul(h3_mapped, h3_mapped, max_t), h3_mapped, max_t)

    dvars: dict[tuple[int, int], sp.Symbol] = {}
    for r in range(1, 34):
        for q in range(34 - r):
            if q <= 21 and (r, q) not in EQUALITY_FACE:
                dvars[(r, q)] = orig.symbol(f"K2c_{r}_{q}")
    original_dvars = {
        pos for pos in dvars if 3 * pos[0] + 4 * pos[1] >= 97
    }
    assert len(original_dvars) == 106

    def raw_coefficient(r: int, q: int) -> sp.Expr:
        if (r, q) in EQUALITY_FACE:
            return EQUALITY_FACE[(r, q)]
        if (r, q) in dvars:
            return dvars[(r, q)]
        return h3cube.get((r, q), sp.Integer(0))

    # Keep the original SOUND h2 D1 rows (W=97,98) and the charged 7-pivot
    # chart.  Newly freed W<97 coordinates are not given a new D1 family:
    # that would add ROWS the original staged elimination did not carry.
    rows: list[tuple[str, sp.Expr]] = []
    for W, kmax in ((97, 4), (98, 1)):
        positions = [
            (r, q) for r in range(1, 34) for q in range(34 - r) if 3 * r + 4 * q == W
        ]
        for k in range(kmax + 1):
            row = sum(comb(q, k) * raw_coefficient(r, q) for r, q in positions if q >= k)
            rows.append((f"h2_D1_W{W}_k{k}", sp.expand(row)))
    pivot_order = [
        dvars[(11, 16)],
        dvars[(15, 13)],
        dvars[(19, 10)],
        dvars[(23, 7)],
        dvars[(27, 4)],
        dvars[(10, 17)],
        dvars[(14, 14)],
    ]
    work = list(rows)
    h2map: dict[sp.Symbol, sp.Expr] = {}
    pivots = []
    for variable in pivot_order:
        selected = None
        for index, (label, row) in enumerate(work):
            row = orig.substitute_map(row, h2map)
            coefficient = sp.diff(row, variable)
            if coefficient.is_Rational and coefficient != 0:
                selected = (index, label, row, sp.Rational(coefficient))
                break
        assert selected is not None, f"missing charged h2 D1 pivot {variable}"
        index, label, row, coefficient = selected
        rhs = sp.cancel(-(row - coefficient * variable) / coefficient)
        h2map[variable] = rhs
        pivots.append((label, str(variable), str(coefficient)))
        del work[index]
        work = [(lab, sp.expand(rr.subs(variable, rhs))) for lab, rr in work]
    h2map = orig.resolve_map(h2map)
    assert all(orig.substitute_map(row, h2map) == 0 for _label, row in rows)

    dfree = set(dvars.values()) - set(h2map)
    k2: orig.TZ = {}
    for j in range(10):
        k2[(0, 24 + j)] = sp.Integer(comb(9, j))
    for r in range(1, max_t + 1):
        for q in range(34 - r):
            value = raw_coefficient(r, q)
            value = orig.substitute_map(sp.expand(value), h2map)
            if value != 0:
                k2[(r, q)] = value

    centres = set(hfree) - set(surviving)
    inner_free = (set(hvars) - set(hmap)) | centres | dfree
    major = {
        "h3_control": control,
        "h3_face": face_meta,
        "centre": centre,
        "h3_free": [str(v) for v in sorted(set(hfree), key=str)],
        "h3_floor_freed": h3meta["floor_freed"],
        "h3_template": {k: v for k, v in h3meta.items() if k not in {"floor_freed", "surviving"}},
        "major_output_coordinate_count_before_D1": len(dvars),
        "original_major_output_coordinate_count_before_D1": 106,
        "d2_floor_freed_K2c_count": len(dvars) - 106,
        "major_h2_D1_pivots": pivots,
        "major_output_free_count": len(dfree),
        "inner_dimension_including_centres": len(inner_free),
        "coordinate_change": "K2c low-q coordinates have unit leading C3/C2 columns; q<=21 is the chart, not a D2 floor",
        "equality_face_kept": True,
        "h2_D1_extended_below_W97": False,
        "h2_D1_scope": "original W=97,98 rows only; newly freed W<97 coordinates remain unknowns",
    }
    return k2, inner_free, major, face_rows


def outer_state(max_offset: int) -> tuple[dict, set[sp.Symbol], dict]:
    coordinates: dict[str, dict[tuple[int, int], sp.Symbol]] = {}
    ambient = 0
    for block, (degree, W0, threshold) in orig.OUTER_SPECS.items():
        all_positions = [
            (r, q) for r in range(degree + 1) for q in range(min(32, degree - r) + 1)
        ]
        ambient += len(all_positions)
        coordinates[block] = {
            (r, q): orig.symbol(f"{block}c_{r}_{q}") for r, q in all_positions
        }
    assert ambient == 6600

    substitutions: dict[sp.Symbol, sp.Expr] = {}
    below_ledger = []
    below_pivots = 0
    # Below-W0 D1 rows at distinct W use disjoint (r,q) slots.  Reduce each
    # weight independently and merge the maps once; do not resolve_map after
    # every W (that is quadratic in the 5598 previously deleted coordinates).
    for block, (_degree, W0, threshold) in orig.OUTER_SPECS.items():
        progress(f"outer_below_W0 block={block} W0={W0}")
        weights = sorted({3 * r + 4 * q for r, q in coordinates[block] if 3 * r + 4 * q < W0})
        block_pivots = 0
        block_rows = 0
        block_map: dict[sp.Symbol, sp.Expr] = {}
        for W in weights:
            positions = [p for p in coordinates[block] if 3 * p[0] + 4 * p[1] == W]
            rows = []
            band_variables: set[sp.Symbol] = set()
            for k in range(max(0, threshold - 3 * W)):
                row = sum(
                    comb(q, k) * coordinates[block][(r, q)]
                    for r, q in positions
                    if q >= k
                )
                row = sp.expand(row)
                if row != 0:
                    rows.append((f"{block}_D1_belowW0_W{W}_k{k}", row))
                    band_variables.update(row.free_symbols)
            if not rows:
                continue
            residual, band_map, pivots, zero_rows = orig.qstar_reduce(
                rows, set(band_variables)
            )
            assert not residual, f"non-Q* D1 residual below W0 on {block} W={W}"
            block_map.update(band_map)
            block_pivots += len(pivots)
            block_rows += len(rows)
        substitutions.update(block_map)
        below_pivots += block_pivots
        below_ledger.append(
            {
                "block": block,
                "W0": W0,
                "Qstar_pivots": block_pivots,
                "raw_rows": block_rows,
            }
        )
        progress(f"outer_below_W0_done block={block} pivots={block_pivots} rows={block_rows}")
    if substitutions and all(rhs == 0 for rhs in substitutions.values()):
        substitutions = {var: sp.Integer(0) for var in substitutions}
        progress(f"outer_below_W0_total_pivots={below_pivots} all_rhs_zero=True")
    else:
        substitutions = orig.resolve_map(substitutions) if substitutions else substitutions
        progress(f"outer_below_W0_total_pivots={below_pivots} all_rhs_zero=False")

    ledger = []
    all_boundary_rows = []
    for offset in range(max_offset + 1):
        band_rows = []
        band_variables = set()
        by_block = {}
        for block, (_degree, W0, threshold) in orig.OUTER_SPECS.items():
            W = W0 + offset
            positions = [p for p in coordinates[block] if 3 * p[0] + 4 * p[1] == W]
            rows = []
            for k in range(max(0, threshold - 3 * W)):
                row = sum(
                    comb(q, k) * coordinates[block][(r, q)]
                    for r, q in positions
                    if q >= k
                )
                row = orig.substitute_map(sp.expand(row), substitutions)
                if row != 0:
                    rows.append((f"{block}_D1_s{offset}_k{k}", row))
                    band_variables.update(row.free_symbols)
            band_rows.extend(rows)
            by_block[block] = {"raw_rows": len(rows), "positions": len(positions)}
        residual, band_map, pivots, zero_rows = orig.qstar_reduce(
            band_rows, set(band_variables)
        )
        assert not residual
        substitutions.update(band_map)
        substitutions = orig.resolve_map(substitutions)
        all_boundary_rows.extend(band_rows)
        ledger.append(
            {
                "offset": offset,
                "raw_rows": len(band_rows),
                "Qstar_pivots": len(pivots),
                "dependent_zero": zero_rows,
                "by_block": by_block,
                "pivot_variables": [str(p.variable) for p in pivots],
            }
        )
    expected_boundary = [41, 38, 33, 25, 19, 11, 6, 3]
    got_boundary = [item["Qstar_pivots"] for item in ledger]
    assert got_boundary == expected_boundary[: max_offset + 1], (
        f"SOUND D1 offsets changed after freeing the D2 floor: {got_boundary}"
    )

    resolved_coordinates = {
        block: {
            pos: substitutions[var] if var in substitutions else var
            for pos, var in values.items()
        }
        for block, values in coordinates.items()
    }
    all_vars = set().union(*(set(values.values()) for values in coordinates.values()))
    free = all_vars - set(substitutions)
    cumulative_pivots = sum(item["Qstar_pivots"] for item in ledger)
    return resolved_coordinates, free, {
        "basis": "K_Q=t^D Q(t^-1,w/t)=sum c_(r,q)t^r(w-1)^q",
        "weight": "W=3*r+4*q",
        "preblock": {
            "imposed_D2_coordinate_rows": 0,
            "Qstar_pivots": 0,
            "surviving_coordinates": 6600,
            "redundant_D1_labels_on_deleted_coordinates": 0,
            "repair": "D2 unit rows dropped; SOUND D1 imposed on the previously deleted slots instead",
            "below_W0_D1_Qstar_pivots": below_pivots,
            "below_W0_by_block": below_ledger,
            "original_D2_unit_rows": 5598,
            "slots_a_center_admits": 5598 - below_pivots,
        },
        "D1_offsets": ledger,
        "D1_cumulative_pivots": cumulative_pivots,
        "D1_offsets_match_original": True,
        "outer_free_count": len(free),
        "outer_ambient": 6600,
    }


def progress(msg: str) -> None:
    print(f"PROGRESS {msg}", file=sys.stderr, flush=True)


def run(branch: str, stage: int, emit_singular: Path | None = None, inventory_only: bool = False) -> dict:
    started = time.perf_counter()
    custody = verify_our_inputs()
    progress("custody_ok")
    jac_control = orig.jacobian_normalization_control()
    raw_counts = {
        "delta2_F": sum(map(len, orig.raw_minor_support("delta2", "F").values())),
        "delta2_G": sum(map(len, orig.raw_minor_support("delta2", "G").values())),
        "delta52_F": sum(map(len, orig.raw_minor_support("delta52", "F").values())),
        "delta52_G": sum(map(len, orig.raw_minor_support("delta52", "G").values())),
    }
    assert raw_counts == {
        "delta2_F": 1134,
        "delta2_G": 513,
        "delta52_F": 1316,
        "delta52_G": 594,
    }
    spec = orig.stage_spec(branch, stage)
    max_j = max(orig.stage_spec(branch, i)["jacobian"]["t_power"] for i in range(stage + 1))
    max_pole = spec["pole_local_power"] if branch == "delta2" else (spec["pole_local_power"] + 1) // 2
    max_t = max(max_j, max_pole, 4)
    progress(f"build_major_h2 branch={branch} max_t={max_t}")
    k2, inner_free, major, prefix_rows = build_major_h2(branch, max_t)
    progress(
        f"major_done inner_free={len(inner_free)} face_prefix_rows={len(prefix_rows)}"
    )
    progress(f"outer_state max_offset={min(stage, 7)}")
    outer, outer_free, outer_meta = outer_state(min(stage, 7))
    progress(
        f"outer_done free={len(outer_free)} below_W0_pivots="
        f"{outer_meta['preblock']['below_W0_D1_Qstar_pivots']}"
    )
    if inventory_only:
        elapsed = time.perf_counter() - started
        rss_self = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        return {
            "type": "INVENTORY-ONLY D2-FLOOR REPLAY / FALLACY-v2",
            "branch": branch,
            "stage_spec": spec,
            "custody": custody,
            "major": major,
            "outer_major": {
                k: v
                for k, v in outer_meta.items()
                if k != "D1_offsets"
            },
            "outer_D1_offsets_pivot_counts": [item["Qstar_pivots"] for item in outer_meta["D1_offsets"]],
            "counts": {
                "inner_free": len(inner_free),
                "outer_free": len(outer_free),
                "prefix_rows": len(prefix_rows),
            },
            "prefix_row_labels": [lab for lab, _ in prefix_rows],
            "resources": {"wall_seconds": elapsed, "peak_rss_kib": rss_self},
            "verdict": "INVENTORY",
        }

    progress("build_FG")
    KF, KG = orig.build_FG(k2, outer, max_t)
    progress("cumulative_rows")
    rows, accounting = orig.cumulative_rows(branch, stage, KF, KG)
    rows = prefix_rows + rows
    accounting["h3_face_and_extra_h2_D1_residual"] = len(prefix_rows)
    all_free = set(inner_free) | set(outer_free)
    localized = orig.symbol("rho" if branch == "delta2" else "c")
    progress(f"qstar_reduce n_rows={len(rows)} n_eligible={len(all_free)-1}")
    residual, linear_map, pivots, zero_rows = orig.qstar_reduce(
        rows, set(all_free) - {localized}
    )
    remaining = all_free - set(linear_map)
    assert localized in remaining
    residual_symbols = (
        set().union(*(row.free_symbols for _label, row in residual)) if residual else set()
    )
    assert residual_symbols.issubset(remaining)
    progress(f"qstar_done pivots={len(pivots)} residual={len(residual)} remaining={len(remaining)}")
    singular = orig.singular_dimension(residual, branch, emit_singular)
    if singular["unit_ideal"]:
        dimension = None
        verdict = "DEAD"
        marker = "GG_UNIT"
    else:
        dimension = len(remaining) - singular["codimension"]
        verdict = "COUNTING-BOUND"
        marker = "GG_NONUNIT"
    progress(f"VERDICT {verdict} {marker} dimension={dimension}")
    print(f"VERDICT: {verdict}", file=sys.stderr, flush=True)
    print(f"{marker}", file=sys.stderr, flush=True)
    print(f"dimension = {dimension}", file=sys.stderr, flush=True)
    if residual:
        constants = [lab for lab, row in residual if row.free_symbols == set() and row != 0]
        if constants:
            print(
                f"constant_residual {constants[0]} = {residual[0][1]}",
                file=sys.stderr,
                flush=True,
            )
    elapsed = time.perf_counter() - started
    rss_self = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_children = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    rss = max(rss_self, rss_children)
    return {
        "type": "EXACT-Q JOINT GLOBAL BAND D2-FLOOR REPLAY / FALLACY-v2",
        "branch": branch,
        "stage_spec": spec,
        "filtration_convention": {
            "outer": "SOUND D1 on all W including W<W0; D2 unit-row preblock NOT imposed",
            "pole": "next occupied local exponent (branch-specific)",
            "Jacobian": "named d162,k27; finish d162; then total degrees downward",
            "h3": "face z^8 w^3 and branch-map face assignments kept; vmin floor freed",
            "warning": "synchronization is a driver convention, not a source theorem",
        },
        "repair": {
            "h3_floor": "freed 45 z-monomials below old vmin; kept face and original 21 branch-map assignments",
            "h2_floor": "freed K2c for all q<=21 except the P^3 equality face; kept charged W=97,98 D1 pivots; did not add a new W<97 D1 family",
            "outer_D2_preblock": "freed 5598 unit-row coordinates; imposed SOUND D1 on them",
            "fallacy": "dropping UNKNOWNS by a weight floor is not safe; D1 rows kept",
            "qstar_reduce": "imported from pinned original_band_engine.py; rational pivots only",
        },
        "custody": custody,
        "driver_sha256": sha256(Path(__file__)),
        "major": major,
        "outer_major": outer_meta,
        "row_accounting": accounting,
        "jacobian_normalization_control": jac_control,
        "raw_minor_support_control": raw_counts,
        "joint_elimination": {
            "input_row_labels_excluding_preeliminated_major_rows": len(rows),
            "all_labeled_rows_hash": orig.rows_hash(rows),
            "raw_nonzero_count": sum(row != 0 for _label, row in rows),
            "Qstar_pivots": len(pivots),
            "dependent_or_zero_rows": zero_rows,
            "pivot_ledger": [
                {
                    "row": p.label,
                    "variable": str(p.variable),
                    "coefficient": str(p.coefficient),
                    "rhs": orig.expr_text(p.rhs),
                }
                for p in pivots
            ],
            "residual_count": len(residual),
            "residual_rows": [
                {"label": label, "expression": orig.expr_text(row)} for label, row in residual
            ],
            "residual_hash": orig.rows_hash(residual),
            "singular": singular,
        },
        "counts": {
            "inner_free_before_outer": len(inner_free),
            "outer_free_after_current_major_band": len(outer_free),
            "linear_free_before_residue": len(remaining),
            "exact_Krull_dimension_localized": dimension,
            "original_inner_free": 104 if branch == "delta2" else 102,
            "original_outer_D2_unit_rows": 5598,
        },
        "verdict": verdict,
        "nonlinear_residue_appears": bool(residual),
        "resources": {
            "wall_seconds": elapsed,
            "peak_rss_kib": rss,
            "self_peak_rss_kib": rss_self,
            "children_peak_rss_kib": rss_children,
        },
        "unresolved_quotient_generators": sorted(map(str, remaining)),
        "free_coordinate_list_is_valid": not residual,
        "next_stage": orig.stage_spec(branch, stage + 1),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--branch", choices=["delta2", "delta52"], required=True)
    parser.add_argument("--stage", type=int, required=True)
    parser.add_argument("--emit-singular", type=Path)
    parser.add_argument("--inventory-only", action="store_true")
    args = parser.parse_args()
    assert args.stage >= 0
    result = run(args.branch, args.stage, args.emit_singular, args.inventory_only)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
