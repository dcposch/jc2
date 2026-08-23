#!/usr/bin/env python3
"""Decode, verify, and floor a graph-preserving D43 witness.

INTERNAL / UNREVIEWED.  The witness comes from an 89-variable slice of
the 89 pristine rung rows at one certified point of a parked A^14 cell.
All omitted D43 graph variables are zero; no completion reconstruction is
imposed beyond the equations of the requested 34+52+89 family itself.
"""

import argparse
import hashlib
import json
import os
import pickle
import re
import sys

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import d25_eplus as DE
import d43_family2 as F
import d43_nf_certificate as NF
import d43_raw_point_system as RAW
import eplus43 as X
import valuation_e as V


RUNG_SIZES = (10, 10, 9, 10, 10, 10, 10, 10, 10)
RUNGS = tuple(range(26, 43, 2))


def sha256_path(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_linear_gb(path, p, expected):
    text = open(path).read()
    match = re.search(r"#variable order:\s*(.+)\n", text)
    assert match, "missing variable order"
    order = [name.strip() for name in match.group(1).split(",")]
    assert len(order) == len(set(order)) == expected
    match = re.search(r"\[([^\]]*)\]:\s*$", text, re.S)
    assert match, "missing printed Groebner basis"
    polynomials = [item.strip() for item in match.group(1).split(",")
                   if item.strip()]
    assert len(polynomials) == expected
    pattern = re.compile(r"1\*([A-Za-z0-9_]+)\^1(?:\+([0-9]+))?$")
    solved = {}
    for polynomial in polynomials:
        parsed = pattern.fullmatch(polynomial)
        assert parsed, ("nonlinear GB element", polynomial)
        name, constant = parsed.groups()
        assert name in order and name not in solved
        solved[name] = (-int(constant or 0)) % p
    assert set(solved) == set(order)
    return order, solved


def jacobian_rank(rows, variables, assignment, p):
    matrix = []
    for row in rows:
        gradient = []
        for variable in variables:
            value = 0
            for mono, coeff in row.items():
                multiplicity = mono.count(variable)
                if not multiplicity:
                    continue
                term = coeff * multiplicity % p
                removed = False
                for name in mono:
                    if name == variable and not removed:
                        removed = True
                    else:
                        term = term * assignment[name] % p
                value = (value + term) % p
            gradient.append(value)
        matrix.append(gradient)
    return NF.matrix_rank(matrix, p)


def build_operator_point(p, parked_point, external):
    env = DE.fiber_env(p, "a00pp")
    dval, diag = DE.reconstruct_point(p, parked_point, env)
    wit72, deep = DE.witness72_of(p, dval)
    _point_v2, _E_v2, frontier = X.completed_point_v2(
        p, wit72, deep, env)
    extra = {}
    for label, value in frontier.items():
        family, level = label.rsplit("_", 1)
        extra[(family, int(level) - 32)] = value
    point = X.point43_from_v2(p, wit72, deep, env, extra_tails=extra)
    alpha = external["Xf_alpha"]
    beta = external["Xg_beta"]
    for name, value in external.items():
        semantic = F.X2T.get(name, name)
        if semantic in ("Xf_alpha", "Xg_beta"):
            continue
        if semantic == "uf24":
            point["fixed"]["uf24"] = value
            continue
        family, level = semantic.rsplit("_", 1)
        assert family in X.FAMS and level.isdigit(), (name, semantic)
        r = int(level) - 32
        if value:
            point["tails"][family][r] = value
        else:
            point["tails"][family].pop(r, None)
    point["zc_hash"] = hashlib.sha256(json.dumps({
        "base": point["zc_hash"], "graph_external": sorted(external.items())
    }, sort_keys=True).encode()).hexdigest()
    provenance = {}
    for family in X.FAMS:
        for r, value in point["tails"][family].items():
            if value:
                provenance["%s_%d" % (family, 32 + int(r))] = \
                    "exact_graph_witness_from_linear_GB"
    return point, env, alpha, beta, provenance, diag


def floor_gate(p, parked_point, external):
    point, env, alpha, beta, provenance, diag = build_operator_point(
        p, parked_point, external)
    checks, info, E, aux = X.gate_suite(
        point, p, env, alpha, beta, provenance, "D43_SURVIVOR")
    values = E.V.astype(np.int64)
    selected_nonzero = [
        {"eta": a, "copy": j, "band": X.S30[a] + 6 * j,
         "value": int(values[a][X.S30[a] + 6 * j]) % p}
        for (a, j) in X.ROWS_CANON
        if int(values[a][X.S30[a] + 6 * j]) % p]
    checks["s9_d43_residual_184_zero"] = not selected_nonzero
    checks["s9_nu_ge_43"] = info["nu_window"] is None
    ptv, r3, _h32 = V.radical_env(p)
    fixed = point["fixed"]
    checks["s9_chart_unit_audit"] = bool(
        pow(r3, 2, p) == 3 % p and
        pow(fixed["A1"], 3, p) == (3 + r3) % p and
        pow(fixed["A2"], 3, p) == (3 - r3) % p and
        fixed["W1"] % p and fixed["W2"] % p and
        all(p % q for q in (2, 3, 5, 7)))
    failed = [name for name, value in checks.items() if not value]

    # Point and matrix perturbations must break their respective gates.
    control_name = next(name for name, value in external.items()
                        if value and name not in ("Xf_alpha", "Xg_beta"))
    changed = dict(external)
    changed[control_name] = (changed[control_name] + 1) % p
    bad_point, _env, bad_alpha, bad_beta, _prov, _diag = build_operator_point(
        p, parked_point, changed)
    bad_E, _ = X.build_operator(bad_point, p, bad_alpha, bad_beta,
                                Z=aux["Z"])
    residual_control = any(
        int(bad_E.V[a][X.S30[a] + 6 * j]) % p
        for (a, j) in X.ROWS_CANON)

    eligible = not failed
    return {
        "status": "INTERNAL / UNREVIEWED",
        "prime": p, "mode": "D43_SURVIVOR", "depth_D": 43,
        "checks": {name: bool(value) for name, value in checks.items()},
        "checks_all_pass": eligible,
        "floor_eligible": eligible,
        "failed_checks": failed,
        "selected_residual_nonzero_count": len(selected_nonzero),
        "selected_residual_nonzero_by_band": {
            str(band): sum(item["band"] == band for item in selected_nonzero)
            for band in sorted({item["band"] for item in selected_nonzero})
        },
        "selected_residual_nonzero_sample": selected_nonzero[:12],
        "alpha": alpha, "beta": beta,
        "nu_window": info["nu_window"],
        "window_rank_184x182": info["window_rank_184x182"],
        "ell_lb_certified": info["ell_lb_certified"] if eligible else None,
        "diagnostic_window_floor_not_reportable":
            info["ell_lb_certified"] if not eligible else None,
        "ell_profile": info["ell_profile"],
        "maximizers": info["maximizers"],
        "delta_plus_N1": info["delta_plus_N1"],
        "delta_plus_N2": info["delta_plus_N2"],
        "M2_rank": info["M2_rank"],
        "threshold_floor_Dm1_2": X.THRESH43,
        "e_plus": {
            "certified": None,
            "candidate_window_floor":
                info["ell_lb_certified"] if eligible else None,
            "tag": X.CAND,
            "at_or_below_threshold":
                eligible and info["ell_lb_certified"] <= X.THRESH43,
        },
        "manifest_sha256": info["manifest_sha256"],
        "matrix_sha256": info["matrix_hash"],
        "value_array_sha256": info["value_array_hash"],
        "negative_control": {
            "perturbed_external_coordinate": control_name,
            "residual_breaks": bool(residual_control),
        },
        "d25_reconstruction_diag": diag,
    }


def verify(bank_path, gb_path, parked_path, compat_path, out_path,
           floor_path):
    with open(bank_path, "rb") as fh:
        bank = pickle.load(fh)
    p = int(bank["prime"])
    order, solved = parse_linear_gb(gb_path, p, 89)
    external = {name: 0 for name in bank["variables"]}
    external.update(solved)
    assert set(external) == set(bank["variables"])
    graph_values = [RAW.evaluate(row, external, p) for row in bank["rows"]]
    assert graph_values == [0] * 89

    parked_point = {name: int(value) % p
                    for name, value in bank["cell"].items()}
    parked_names, parked_prime, parked_rows = NF.parse_ms(parked_path)
    assert parked_prime == p
    parked_values = [NF.eval_named_poly(row, parked_names, parked_point, p)
                     for row in parked_rows]
    assert parked_values == [0] * 34

    with open(compat_path, "rb") as fh:
        compat_bank = pickle.load(fh)
    assert int(compat_bank["prime"]) == p
    assert int(compat_bank["W1"]) == parked_point["W1"]
    assert int(compat_bank["W2"]) == parked_point["W2"]
    assert all(int(compat_bank["free"][name]) == parked_point[name]
               for name in NF.FREE)
    compat_rows = compat_bank["rows"]
    compat_values = [NF.eval_external(row, external, p)
                     for row in compat_rows]
    assert compat_values == [0] * 52

    graph_rank = jacobian_rank(bank["rows"], bank["variables"], external, p)
    parked_rank = 14
    assert graph_rank == 89
    offset = 0
    rung_ranks = {}
    prefix_rows = []
    for k, size in zip(RUNGS, RUNG_SIZES):
        current = bank["rows"][offset:offset + size]
        prefix_rows.extend(current)
        current_y = list(bank["rung_unknowns"][str(k)]["variables"])
        A, b = NF.affine_numeric(current, set(current_y), external, p)
        rank_A = NF.matrix_rank(A, p)
        rank_augmented = NF.matrix_rank(
            [row + [rhs] for row, rhs in zip(A, b)], p)
        prefix_rank = jacobian_rank(prefix_rows, bank["variables"],
                                    external, p)
        prefix_used = {name for row in prefix_rows for mono in row
                       for name in mono}
        ambient_used = len(parked_point) + len(prefix_used)
        assert rank_A == rank_augmented == \
            int(bank["rung_unknowns"][str(k)]["rank"])
        assert prefix_rank == len(prefix_rows)
        rung_ranks[str(k)] = {
            "current_reconstruction_rank_A": rank_A,
            "current_reconstruction_rank_augmented": rank_augmented,
            "prefix_graph_jacobian_rank": prefix_rank,
            "prefix_graph_rows": len(prefix_rows),
            "prefix_used_external_variables": len(prefix_used),
            "prefix_ambient_variables_with_parked": ambient_used,
            "prefix_smooth_component_dimension_in_used_ring":
                ambient_used - parked_rank - prefix_rank,
        }
        offset += size
    assert offset == 89

    # A solved graph coordinate is a direct negative control.
    negative = None
    for name in order:
        bad = dict(external)
        bad[name] = (bad[name] + 1) % p
        nbad_graph = sum(RAW.evaluate(row, bad, p) != 0
                         for row in bank["rows"])
        nbad_compat = sum(NF.eval_external(row, bad, p) != 0
                          for row in compat_rows)
        if nbad_graph:
            negative = {"coordinate": name,
                        "nonzero_graph_rows": nbad_graph,
                        "nonzero_compatibility_rows": nbad_compat}
            break
    assert negative is not None

    full_point = dict(parked_point)
    assert not (set(full_point) & set(external))
    full_point.update(external)
    assert len(full_point) == 184
    floor = floor_gate(p, parked_point, external)
    with open(floor_path, "w") as fh:
        json.dump(floor, fh, indent=1, sort_keys=True)
        fh.write("\n")

    report = {
        "status": "INTERNAL / UNREVIEWED",
        "verdict": "NONEMPTY",
        "prime": p, "fiber": "a00pp",
        "scope": "residue-A, B-frozen, no-log, PIN42, W1W2 != 0",
        "source": {
            "raw_graph_bank": bank_path,
            "raw_graph_bank_sha256": sha256_path(bank_path),
            "linear_gb": gb_path, "linear_gb_sha256": sha256_path(gb_path),
            "parked": parked_path, "parked_sha256": sha256_path(parked_path),
            "compatibility_nf": compat_path,
            "compatibility_nf_sha256": sha256_path(compat_path),
        },
        "slice": {"kept_variables": 89, "omitted_graph_variables_zero": 67,
                  "linear_gb_elements": 89},
        "point": {"parked": parked_point, "external": external,
                  "full_184": full_point},
        "gates": {
            "parked_rows_zero": "34/34",
            "compatibility_rows_zero": "52/52",
            "reconstruction_graph_rows_zero": "89/89",
            "total_audit_rows_zero": "175/175",
            "parked_jacobian_rank": parked_rank,
            "graph_external_jacobian_rank": graph_rank,
            "combined_jacobian_rank": parked_rank + graph_rank,
            "negative_control": negative,
            "eplus43_floor_gate": ("PASS" if floor["floor_eligible"]
                                   else "REJECTED: " +
                                   ",".join(floor["failed_checks"])),
        },
        "rung_ranks": rung_ranks,
        "dimension": {
            "ambient_variables": 184,
            "smooth_local_codimension": 103,
            "smooth_component_dimension": 81,
            "argument": "parked rank 14 + graph external rank 89",
        },
        "floor_report": floor_path,
        "candidate_window_floor": floor["ell_lb_certified"],
    }
    with open(out_path, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("D43 GRAPH WITNESS p=%d: PASS 34+52+89; rank 14+89; dim 81; "
          "floor %s -> %s" % (p, (floor["ell_lb_certified"]
                                  if floor["floor_eligible"] else "REJECTED"),
                               out_path),
          flush=True)
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", required=True)
    parser.add_argument("--gb", required=True)
    parser.add_argument("--parked", required=True)
    parser.add_argument("--compat", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--floor-out", required=True)
    args = parser.parse_args()
    verify(args.bank, args.gb, args.parked, args.compat, args.out,
           args.floor_out)


if __name__ == "__main__":
    main()
