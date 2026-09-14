#!/usr/bin/env python3
"""Independent exact symbolic checks for every semantic patch hunk."""
from __future__ import annotations

import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import sys

import sympy as sp


HERE = Path(__file__).resolve().parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


original = load("g9966_original_patchcheck", HERE / "original_band_engine.py")
precise = load("g9966_precise_patchcheck", HERE / "band_engine.py")
jet0 = sp.Symbol("jet0")

unchanged_functions = ["h3_template", "outer_state", "raw_minor_support", "stage_spec"]
unchanged = {}
for name in unchanged_functions:
    old_source = inspect.getsource(getattr(original, name))
    new_source = inspect.getsource(getattr(precise, name))
    assert old_source == new_source
    unchanged[name] = digest(old_source)
assert original.OUTER_SPECS == precise.OUTER_SPECS

branches = {}
for branch, expected_inner in (("delta2", 105), ("delta52", 103)):
    old_map, old_free, _ = original.h3_branch_map(branch)
    new_map, new_free, centre = precise.h3_branch_map(branch)
    assert set(old_map) == set(new_map)
    assert all(sp.expand(new_map[var].subs(jet0, 0) - old_map[var]) == 0 for var in old_map)
    assert set(new_free) == set(old_free) | {jet0}
    assert centre["released_pin"] == "jet0=0"
    if branch == "delta52":
        hconst = sp.Symbol("Hc_11_0")
        assert new_map[hconst] == 0
        assert hconst not in new_free
        assert centre["Hc_11_0"] == "fixed_zero_retained"

    # Independently regenerate the generic face equations from h3_template and
    # the repaired local series, then solve them with the same rational-only
    # pivot rule.  This checks every displayed branch-map formula, not just its
    # jet0=0 specialization.
    generic_h3, hvars = precise.h3_template()
    if branch == "delta2":
        cap = 9
        expected_face = {(9, 2): 3 * sp.Symbol("rho"), (9, 3): sp.Integer(1)}
    else:
        cap = 21
        expected_face = {(21, 1): -sp.Symbol("c"), (21, 3): sp.Integer(1)}
    generic_rows = precise.local_rows(generic_h3, branch, cap, exact_only=False)
    face_equations = []
    for tag in sorted(set(generic_rows) | set(expected_face)):
        equation = sp.expand(generic_rows.get(tag, 0) - expected_face.get(tag, 0))
        if equation != 0:
            face_equations.append((f"face_{tag[0]}_{tag[1]}", equation))
    if branch == "delta52":
        face_equations.append(("retained_Hc_11_0", sp.Symbol("Hc_11_0")))
    face_residual, derived_map, face_pivots, _ = precise.qstar_reduce(
        face_equations, set(hvars)
    )
    assert not face_residual
    assert set(derived_map) == set(new_map)
    assert all(sp.expand(derived_map[var] - new_map[var]) == 0 for var in new_map)
    assert all(pivot.coefficient in {sp.Integer(-1), sp.Integer(1)} for pivot in face_pivots)

    _, inner_free, major = precise.build_major_h2(branch, 4)
    assert len(inner_free) == expected_inner and jet0 in inner_free
    assert major["h3_control"]["verified"] is True
    for stage in range(9 if branch == "delta52" else 5):
        assert original.stage_spec(branch, stage) == precise.stage_spec(branch, stage)
    branches[branch] = {
        "old_branch_free": sorted(map(str, old_free)),
        "new_branch_free": sorted(map(str, new_free)),
        "jet0_zero_recovers_old_branch_map": True,
        "inner_free": len(inner_free),
        "h3_target": major["h3_control"]["target"],
        "centre_ledger": centre,
        "independent_face_equations": len(face_equations),
        "independent_Qstar_pivots": len(face_pivots),
        "independent_pivot_coefficients": sorted({str(p.coefficient) for p in face_pivots}),
        "derived_map_equals_patched_map": True,
    }

toy = {(0, 3): sp.Symbol("A"), (1, 2): sp.Symbol("B"), (2, 1): sp.Symbol("C")}
for branch, cap in (("delta2", 12), ("delta52", 24)):
    old_rows = original.local_rows(toy, branch, cap)
    specialized = {
        tag: sp.expand(value.subs(jet0, 0))
        for tag, value in precise.local_rows(toy, branch, cap).items()
    }
    specialized = {tag: value for tag, value in specialized.items() if value != 0}
    assert old_rows == specialized

raw_counts = {
    f"{branch}_{name}": sum(map(len, precise.raw_minor_support(branch, name).values()))
    for branch in ("delta2", "delta52")
    for name in ("F", "G")
}
assert raw_counts == {"delta2_F": 1134, "delta2_G": 513, "delta52_F": 1316, "delta52_G": 594}
for branch in ("delta2", "delta52"):
    for name in ("F", "G"):
        assert precise.raw_minor_support(branch, name) == original.raw_minor_support(branch, name)

print(json.dumps({
    "status": "PASS",
    "coefficient_field": "Q",
    "original_engine_sha256": hashlib.sha256((HERE / "original_band_engine.py").read_bytes()).hexdigest(),
    "patched_engine_sha256": hashlib.sha256((HERE / "band_engine.py").read_bytes()).hexdigest(),
    "unchanged_function_source_hashes": unchanged,
    "outer_specs_unchanged": True,
    "local_rows_jet0_zero_specialization": True,
    "raw_minor_support_counts_unchanged": raw_counts,
    "raw_minor_support_label_sets_unchanged": True,
    "branches": branches,
}, indent=2, sort_keys=True))
