#!/usr/bin/env python3
"""Hostile custody checks; reads the repaired bundle and writes only beside itself."""
import hashlib
import importlib.util
import inspect
import json
import os
from pathlib import Path
import subprocess
import sys

import sympy as sp

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent / "g9966-d2-precise-20260905"


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, BUNDLE / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


old = load("custody_old", "original_band_engine.py")
new = load("custody_new", "band_engine.py")
jet0 = sp.Symbol("jet0")
assert sha(BUNDLE / "original_band_engine.py") == "3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9"
assert sha(BUNDLE / "band_engine.py") == "76d8c7206f70ba190d1a21fff812c016cbde497cd64071c29c91cfe8089f3c06"
unchanged = ["h3_template", "outer_state", "raw_minor_support", "stage_spec",
             "qstar_reduce", "cumulative_rows", "build_FG", "jacobian_band",
             "outer_effective_tz", "tz_mul", "z_band_to_w"]
for name in unchanged:
    assert inspect.getsource(getattr(old, name)) == inspect.getsource(getattr(new, name))
assert old.OUTER_SPECS == new.OUTER_SPECS

report = {"status": "PASS", "field": "Q", "sympy": sp.__version__,
          "source_identical_functions": unchanged, "branches": {}}
for branch, stage, label, value in [
    ("delta2", 4, "stage4_J_d159_k35", "6264"),
    ("delta52", 8, "stage8_G_local16_coord0", "64"),
]:
    oldmap, oldfree, _ = old.h3_branch_map(branch)
    newmap, newfree, ledger = new.h3_branch_map(branch)
    assert set(newmap) == set(oldmap)
    assert set(newfree) == set(oldfree) | {jet0}
    for variable in oldmap:
        assert sp.expand(newmap[variable].subs(jet0, 0) - oldmap[variable]) == 0
    if branch == "delta52":
        assert newmap[sp.Symbol("Hc_11_0")] == 0
        assert sp.Symbol("Hc_11_0") not in newfree
    for target in ["F", "G"]:
        assert new.raw_minor_support(branch, target) == old.raw_minor_support(branch, target)

    a_path = BUNDLE / f"control/{branch}/stage{stage}.json"
    b_path = BUNDLE / f"runs/{branch}/stage{stage}.json"
    a, b = (json.loads(path.read_text()) for path in [a_path, b_path])
    x, y = a["joint_elimination"], b["joint_elimination"]
    assert a["row_accounting"] == b["row_accounting"]
    assert set(b["unresolved_quotient_generators"]) == set(a["unresolved_quotient_generators"]) | {"jet0"}
    assert len(x["pivot_ledger"]) == len(y["pivot_ledger"])
    for op, np in zip(x["pivot_ledger"], y["pivot_ledger"]):
        assert (op["row"], op["variable"], op["coefficient"]) == (np["row"], np["variable"], np["coefficient"])
        assert sp.expand(sp.sympify(np["rhs"]).subs(jet0, 0) - sp.sympify(op["rhs"])) == 0
        pivot_coefficient = sp.sympify(np["coefficient"])
        assert pivot_coefficient.is_Rational and pivot_coefficient != 0
        assert np["variable"] != ("rho" if branch == "delta2" else "c")
    assert len(x["residual_rows"]) == len(y["residual_rows"])
    for op, np in zip(x["residual_rows"], y["residual_rows"]):
        assert op["label"] == np["label"]
        assert sp.expand(sp.sympify(np["expression"]).subs(jet0, 0) - sp.sympify(op["expression"])) == 0
    for data in [x, y]:
        residual = {row["label"]: row["expression"] for row in data["residual_rows"]}
        assert residual[label] == value

    singular = {}
    for kind, data in [("control", x), ("runs", y)]:
        path = BUNDLE / f"{kind}/{branch}/stage{stage}.sing"
        script = path.read_text()
        expressions = [sp.expand(sp.sympify(row["expression"])) for row in data["residual_rows"]]
        active = set().union(*(expression.free_symbols for expression in expressions))
        loc = sp.Symbol("rho" if branch == "delta2" else "c")
        wrapper = sp.Symbol("Zrho" if branch == "delta2" else "Zc")
        active.add(loc)
        variables = sorted(active, key=str) + [wrapper]
        expected_ring = f"ring R=0,({','.join(map(str, variables))}),dp;"
        assert script.splitlines()[0] == expected_ring
        expected_ideal = "ideal I=" + ",".join(str(expression).replace("**", "^") for expression in expressions)
        expected_ideal += f",{wrapper}*{loc}-1;"
        assert script.splitlines()[1] == expected_ideal
        result = subprocess.run(["Singular", "-q", str(path)], capture_output=True, text=True, check=True, timeout=30)
        assert result.stdout == "BEGIN_DIM\n-1\nEND_DIM\nBEGIN_GB\n1\nEND_GB\nBEGIN_CONTROLS\n0\n1\n0\nEND_CONTROLS\n"
        assert not result.stderr
        output = HERE / f"custody-{kind}-{branch}-stage{stage}.singular.out"
        output.write_text(result.stdout)
        singular[kind] = {"script_sha256": sha(path), "output_sha256": sha(output),
                          "ring": expected_ring, "basis": ["1"], "controls": [0, 1, 0]}
    report["branches"][branch] = {
        "branch_map_specialized_images": len(oldmap),
        "extra_generators_exactly": ["jet0"],
        "pivot_rhs_specialized_images": len(x["pivot_ledger"]),
        "residual_specialized_images": len(x["residual_rows"]),
        "row_accounting_identical": True,
        "constant_row": {"label": label, "value": value, "inverse": str(1 / sp.Rational(value))},
        "old_json_sha256": sha(a_path), "new_json_sha256": sha(b_path),
        "singular": singular,
    }
print(json.dumps(report, indent=2, sort_keys=True))
