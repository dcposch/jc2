#!/usr/bin/env python3
"""Global accepted-chart formula with all 18 raw Q7 digits."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path

import z3

ROOT = Path(os.environ["JC2_ROOT"])
V1 = (ROOT / "cases/as_fonly_d7_global_chart_qfbv_20260825"
      / "solve_global_chart.py")
EXPECTED_V1_SHA = (
    "d4d4c17dcab32088ef0e76f618cb4fee08fd7ce3cdf44db1ea16b0226dffc3ad")
payload = V1.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_V1_SHA
source = payload.decode()
matrix_marker = "\ndef affine_matrix(function, variable_count):\n"
forced_marker = "\nforced = {10: 0, 11: 0, 12: 0, 13: 0, 15: 0, 17: 1}\n"
components_marker = "\ndef components(restoration):\n"
reduction_marker = "\nb7_symbolic = q7_residual([bv(0)] * 18)\n"
for marker in (matrix_marker, forced_marker, components_marker, reduction_marker):
    assert source.count(marker) == 1

# Execute only the hash-pinned source/compiler prefix.  In particular, skip
# V1's sampled constant-matrix block entirely.
prefix_scope = {"__file__": str(V1), "__name__": "__raw_q7_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(matrix_marker, 1)[0], str(V1), "exec"),
         prefix_scope)

solver = prefix_scope["solver"]
bv = prefix_scope["bv"]
badd = prefix_scope["badd"]
bmul = prefix_scope["bmul"]
padd = prefix_scope["padd"]
pscale = prefix_scope["pscale"]
pmul = prefix_scope["pmul"]
pderivative = prefix_scope["pderivative"]
pbracket = prefix_scope["pbracket"]
degree_part = prefix_scope["degree_part"]
lift_poly = prefix_scope["lift_poly"]
homogeneous = prefix_scope["homogeneous"]
divide_three = prefix_scope["divide_three"]
constrain_row_zero = prefix_scope["constrain_row_zero"]
source_data = prefix_scope["source_data"]
source_rows_numeric = prefix_scope["source_rows"]
transition_rows_numeric = prefix_scope["transition_rows_numeric"]
q9_origin = prefix_scope["q9_origin"]
q9_kernel = prefix_scope["q9_kernel"]
add_vector = prefix_scope["add_vector"]
q7_rows_numeric = prefix_scope["q7_rows_numeric"]
recursive_high_numeric = prefix_scope["recursive_high_numeric"]
direct_high_numeric = prefix_scope["direct_high_numeric"]
parent_scope = prefix_scope["parent_scope"]
WIDTH = prefix_scope["WIDTH"]
MODULUS = prefix_scope["MODULUS"]
timeout_ms = prefix_scope["timeout_ms"]

tvars = [z3.BitVec(f"t{index}", WIDTH) for index in range(13)]
yvars = [z3.BitVec(f"y{index}", WIDTH) for index in range(32)]
rvars = [z3.BitVec(f"r{index}", WIDTH) for index in range(18)]
for variable in tvars + yvars + rvars:
    solver.add(z3.ULE(variable, bv(2)))

# Reuse only V1's symbolic chart construction and exact Q8 rows.
chart_fragment = (forced_marker
                  + source.split(forced_marker, 1)[1]
                  .split(components_marker, 1)[0])
exec(compile(chart_fragment, str(V1), "exec"), globals())

# Add the 23 exact Q9 source rows explicitly, even though the origin+kernel
# parameterization makes them redundant.  This mirrors source_rows_numeric.
Cq9 = padd(lift_poly(source_data["Cbase"]), C2, C4)
Dq9 = padd(lift_poly(source_data["Dbase"]), D2, D4)
Eq9 = padd(lift_poly(source_data["L1"]), lift_poly(source_data["K"]),
            pderivative(Cq9, 0), pderivative(Dq9, 1))
cxq, cyq = pderivative(Cq9, 0), pderivative(Cq9, 1)
dxq, dyq = pderivative(Dq9, 0), pderivative(Dq9, 1)
Mq9 = padd(pmul(A, dyq), pmul(cxq, vy), pscale(-1, pmul(uy, dxq)),
            pscale(-1, pmul(cyq, vx)))
F6q9 = padd(lift_poly(source_data["E1_6"]), degree_part(Mq9, 6),
             pderivative(W7, 0), pderivative(Z7, 1))
N9q9 = degree_part(pbracket(Cq9, Dq9), 9)
Tq9 = padd(pmul(A, pderivative(Z7, 1)),
            pmul(pderivative(W7, 0), vy),
            pscale(-1, pmul(uy, pderivative(Z7, 0))),
            pscale(-1, pmul(pderivative(W7, 1), vx)))
G9q9 = padd(lift_poly(source_data["F1_9"]), N9q9,
             degree_part(Tq9, 9))
constrain_row_zero(Eq9, 1)
constrain_row_zero(Eq9, 3)
constrain_row_zero(F6q9, 6)
constrain_row_zero(G9q9, 9)

# Reuse only the source-honest raw restoration constructors.
function_fragment = (components_marker
                     + source.split(components_marker, 1)[1]
                     .split(reduction_marker, 1)[0])
exec(compile(function_fragment, str(V1), "exec"), globals())

restoration = list(rvars)
q7_residuals = q7_residual(restoration)
assert len(q7_residuals) == 19
for residual in q7_residuals:
    solver.add(z3.URem(residual, bv(3)) == bv(0))

C, D, W, Z = components(restoration)
E, M, N, T, Rmix = core_intermediates(C, D, W, Z)
divWZ = padd(pderivative(W, 0), pderivative(Z, 1))
for degree in range(9, 13):
    E1 = divide_three(degree_part(E, degree))
    F = padd(E1, degree_part(M, degree), degree_part(divWZ, degree))
    F1 = divide_three(F)
    G = padd(F1, degree_part(N, degree), degree_part(T, degree))
    G1 = divide_three(G)
    constrain_row_zero(padd(G1, degree_part(Rmix, degree)), degree)

smt2 = solver.to_smt2().encode()
Path(os.environ["SMT2_OUTPUT"]).write_bytes(smt2)
check = solver.check()
status = str(check)
result = {
    "solver_status": status,
    "solver_timeout_ms": timeout_ms,
    "z3_version": z3.get_version_string(),
    "bit_width": WIDTH,
    "residue_modulus": MODULUS,
    "largest_product_bound": 728 * 728,
    "q9_chart_dimension": 13,
    "q9_explicit_source_row_count": 23,
    "q8_raw_variable_count": 32,
    "q8_explicit_source_row_count": 22,
    "q7_raw_variable_count": 18,
    "q7_explicit_source_row_count": 19,
    "division_constraint_count": prefix_scope["base_scope"]["division_constraint_count"],
    "smt2_sha256": hashlib.sha256(smt2).hexdigest(),
    "unsat_is_theorem_without_checked_proof": False,
    "uses_constant_q7_matrix": False,
    "scope": "complete accepted 13-trit Q9 chart with raw Q8/Q7 digits",
}

if check == z3.sat:
    model = solver.model()
    tvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in tvars]
    yvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in yvars]
    rvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in rvars]
    assert all(0 <= value <= 2 for value in tvalues + yvalues + rvalues)
    full_t = [forced.get(index, 0) for index in range(19)]
    for chart_index, kernel_index in enumerate(free_q9):
        full_t[kernel_index] = tvalues[chart_index]
    xvalues = add_vector(q9_origin, q9_kernel, full_t, reduce=True)
    assert source_rows_numeric(source_data, xvalues) == [0] * 23
    assert transition_rows_numeric(xvalues, yvalues) == [0] * 22
    parent_scope["xvalues"] = xvalues
    parent_scope["yvalues"] = yvalues
    assert q7_rows_numeric(rvalues) == [0] * 19
    Cn, Dn, Wn, Zn, recursive = recursive_high_numeric(rvalues)
    direct = direct_high_numeric(Cn, Dn, Wn, Zn)
    assert recursive == direct
    high = [value for degree in range(12, 8, -1)
            for value in recursive[degree]]
    assert not any(high)
    result.update({
        "tvalues": tvalues,
        "xvalues": list(xvalues),
        "yvalues": yvalues,
        "rvalues": rvalues,
        "direct_integer_source_replay": "PASS",
        "recursive_literal_div243_agreement": "PASS",
        "high_row_vector": high,
    })
elif check == z3.unknown:
    result["unknown_reason"] = solver.reason_unknown()

result["solver_statistics"] = str(solver.statistics())
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("solver_status", status)
print("uses_constant_q7_matrix", False)
print("explicit_source_rows", 23, 22, 19)
print("division_constraint_count", result["division_constraint_count"])
print("smt2_sha256", result["smt2_sha256"])
print("sat_direct_replay", result.get("direct_integer_source_replay"))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-GLOBAL-RAWQ7-QFBV")

