#!/usr/bin/env python3
"""One raw-variable formula over the complete aligned vertical predecessor locus.

All substantive execution is AWS-only.  The solver uses widened unsigned
bit-vectors for canonical integer residues modulo 729, with explicit exact
division constraints before each quotient by three.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path

import z3


ROOT = Path(os.environ["JC2_ROOT"])
Q9 = (ROOT / "cases/as_fonly_d7_vertical_q9_state_gate_20260825"
      / "compile_shard.py")
EXPECTED_Q9_SHA = (
    "54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2")
q9_payload = Q9.read_bytes()
assert hashlib.sha256(q9_payload).hexdigest() == EXPECTED_Q9_SHA
q9_source = q9_payload.decode()
q9_marker = '\nshard_count = int(os.environ.get("SHARD_COUNT", "27"))\n'
assert q9_source.count(q9_marker) == 1
qscope = {"__file__": str(Q9), "__name__": "__global_predecessor_q9_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(q9_source.split(q9_marker, 1)[0], str(Q9), "exec"), qscope)

structural = tuple(qscope["structural"])
frob = tuple(qscope["frob"])
unknowns = tuple(qscope["unknowns"])
spectators = tuple(qscope["spectators"])
matrix = qscope["matrix"]
rhs = qscope["rhs"]
N12 = qscope["N12"]
Q11 = qscope["Q11"]
Q10 = qscope["Q10"]
transformed_coefficient = qscope["transformed_coefficient"]
eval_expr = qscope["eval_expr"]
canonical_source_numeric = qscope["canonical_source"]
source_rows_numeric = qscope["source_rows"]
new_polynomials_numeric = qscope["new_polynomials"]
nadd = qscope["nadd"]
nscale = qscope["nscale"]
nmul = qscope["nmul"]
nderivative = qscope["nderivative"]
nbracket = qscope["nbracket"]
degree_part_numeric = qscope["degree_part"]
divide_exact = qscope["divide_exact"]
homogeneous_numeric = qscope["homogeneous_numeric"]
row_numeric = qscope["row"]

predecessor_names = structural + frob + unknowns
expected_predecessor_names = (
    "Pp", "Qq", "Rr", "Tt", "s", "w", "h",
    "fua", "fa", "fb", "fc", "fd", "fvb",
    "d7_1", "d7_4", "d7_7", "d6_1", "d6_4",
    "c5_0", "c5_1", "c5_2", "c5_3", "c5_4", "c5_5",
    "d5_0", "d5_1", "d5_2", "d5_3", "d5_4", "d5_5",
)
assert predecessor_names == expected_predecessor_names
assert len(predecessor_names) == 30
assert len(structural) == 7 and len(frob) == 6 and len(unknowns) == 17
assert len(matrix) == len(rhs) == 20
assert (len(N12), len(Q11), len(Q10)) == (5, 12, 11)
assert spectators == ("c6_0", "c6_3", "c6_6", "d6_0", "d6_3", "d6_6")


WIDTH = 32
MODULUS = 729
assert 728 * 728 == 529984 < 2 ** 20 < 2 ** WIDTH
BV_MOD = z3.BitVecVal(MODULUS, WIDTH)
BV_THREE = z3.BitVecVal(3, WIDTH)


def bv(value):
    if isinstance(value, int):
        return z3.BitVecVal(value % MODULUS, WIDTH)
    assert z3.is_bv(value) and value.size() == WIDTH
    return value


def bred(value):
    return z3.URem(bv(value), BV_MOD)


def badd(*values):
    total = bv(0)
    for value in values:
        total = bred(total + bv(value))
    return total


def bmul(left, right):
    return bred(bv(left) * bv(right))


def bscale(scalar, value):
    return bmul(scalar, value)


def f3(value):
    return z3.URem(bv(value), BV_THREE)


def fadd(*values):
    total = bv(0)
    for value in values:
        total = z3.URem(total + f3(value), BV_THREE)
    return total


def fmul(left, right):
    return z3.URem(f3(left) * f3(right), BV_THREE)


def fscale(scalar, value):
    return fmul(scalar, value)


def padd(*polys):
    keys = set().union(*(poly.keys() for poly in polys))
    return {key: badd(*(poly.get(key, 0) for poly in polys)) for key in keys}


def pscale(scalar, poly):
    return {key: bscale(scalar, value) for key, value in poly.items()}


def pmul(left, right):
    answer = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            key = (i + k, j + ell)
            answer[key] = badd(answer.get(key, 0), bmul(a, b))
    return answer


def pderivative(poly, axis):
    answer = {}
    for (i, j), value in poly.items():
        exponent = i if axis == 0 else j
        if exponent:
            key = (i - 1, j) if axis == 0 else (i, j - 1)
            answer[key] = badd(answer.get(key, 0), bscale(exponent, value))
    return answer


def pbracket(left, right):
    return padd(pmul(pderivative(left, 0), pderivative(right, 1)),
                pscale(-1, pmul(pderivative(left, 1),
                                pderivative(right, 0))))


def degree_part(poly, total):
    return {key: value for key, value in poly.items() if sum(key) == total}


def homogeneous(degree, values):
    assert len(values) == degree + 1
    return {(index, degree - index): bv(value)
            for index, value in enumerate(values)}


solver = z3.Solver()
solver.set(timeout=int(os.environ.get("SOLVER_TIMEOUT_MS", "1")))
solver.set(random_seed=0)
division_constraint_count = 0


def divide_three(poly):
    global division_constraint_count
    answer = {}
    for key, value in poly.items():
        solver.add(z3.URem(value, BV_THREE) == bv(0))
        division_constraint_count += 1
        answer[key] = z3.UDiv(value, BV_THREE)
    return answer


def constrain_row_zero(poly, total):
    for index in range(total + 1):
        solver.add(z3.URem(poly.get((index, total - index), bv(0)),
                          BV_THREE) == bv(0))


def expression_names(expression):
    return {name for monomial in expression for name in monomial}


def eval_expression_symbolic(expression, assignment):
    answer = f3(0)
    for monomial, scalar in expression.items():
        term = f3(scalar)
        for name in monomial:
            term = fmul(term, assignment[name])
        answer = fadd(answer, term)
    return answer


pred_vars = {name: z3.BitVec(f"pred_{name}", WIDTH)
             for name in predecessor_names}
xvars = [z3.BitVec(f"q9_{index}", WIDTH) for index in range(32)]
yvars = [z3.BitVec(f"q8_{index}", WIDTH) for index in range(32)]
rvars = [z3.BitVec(f"q7_{index}", WIDTH) for index in range(18)]
all_input_vars = list(pred_vars.values()) + xvars + yvars + rvars
for variable in all_input_vars:
    solver.add(z3.ULE(variable, bv(2)))

expression_assignment = dict(pred_vars)
expression_assignment.update({name: bv(0) for name in spectators})
allowed_expression_names = set(expression_assignment)
charged_expressions = ([entry for line in matrix for entry in line] + list(rhs)
                       + list(N12) + list(Q11) + list(Q10))
assert all(expression_names(expression) <= allowed_expression_names
           for expression in charged_expressions)

# All 20 predecessor rows, reconstructed from the frozen affine matrix and
# affine right column without any RREF or rank-stratum choice.
for row_entries, affine in zip(matrix, rhs):
    residual = eval_expression_symbolic(affine, expression_assignment)
    for entry, name in zip(row_entries, unknowns):
        residual = fadd(residual, fmul(
            eval_expression_symbolic(entry, expression_assignment),
            pred_vars[name]))
    solver.add(residual == bv(0))

# The exact corrected top rows in their frozen expression-ring form.
for expression in list(N12) + list(Q11) + list(Q10):
    solver.add(eval_expression_symbolic(expression,
                                        expression_assignment) == bv(0))


def parse_pin(name, width):
    raw = os.environ.get(name, "").strip()
    if not raw:
        return None
    values = tuple(int(part) for part in raw.split(","))
    assert len(values) == width and all(0 <= value <= 2 for value in values)
    return values


pinned_predecessor = parse_pin("PIN_PREDECESSOR", len(predecessor_names))
if pinned_predecessor is not None:
    for name, value in zip(predecessor_names, pinned_predecessor):
        solver.add(pred_vars[name] == bv(value))
pinned_structural = parse_pin("PIN_STRUCTURAL", len(structural))
if pinned_structural is not None:
    for name, value in zip(structural, pinned_structural):
        solver.add(pred_vars[name] == bv(value))


def recorded_homogeneous_symbolic(prefix, degree):
    values = []
    for index in range(degree + 1):
        expression = transformed_coefficient(f"{prefix}{degree}_{index}")
        assert expression_names(expression) <= allowed_expression_names
        values.append(eval_expression_symbolic(expression,
                                               expression_assignment))
    return homogeneous(degree, values)


def canonical_source_symbolic():
    h, s, w = (pred_vars[name] for name in ("h", "s", "w"))
    Rr, Tt = (pred_vars[name] for name in ("Rr", "Tt"))
    Pp, Qq = (pred_vars[name] for name in ("Pp", "Qq"))
    r = fadd(Rr, fmul(s, h))
    t = fadd(Tt, fmul(w, h))
    p = fadd(Pp, fmul(Rr, h), fscale(2, fmul(s, fmul(h, h))))
    q = fadd(Qq, fmul(Tt, h), fscale(2, fmul(w, fmul(h, h))))
    U0 = {(2, 1): h, (0, 4): p, (1, 3): fscale(2, r),
          (3, 1): q, (4, 0): fscale(2, t)}
    V0 = {(1, 2): fscale(2, h), (2, 1): bv(1), (0, 4): r,
          (1, 3): s, (3, 1): t, (4, 0): w}
    UF = {(0, 6): pred_vars["fua"], (3, 3): pred_vars["fa"],
          (6, 0): pred_vars["fb"]}
    VF = {(0, 6): pred_vars["fc"], (3, 3): pred_vars["fd"],
          (6, 0): pred_vars["fvb"]}
    U, V = padd(U0, UF), padd(V0, VF)
    Cbase = padd(*(recorded_homogeneous_symbolic("c", degree)
                   for degree in (5, 6, 7)))
    Dbase = padd(*(recorded_homogeneous_symbolic("d", degree)
                   for degree in (5, 6, 7)))

    ux, uy = pderivative(U, 0), pderivative(U, 1)
    vx, vy = pderivative(V, 0), pderivative(V, 1)
    A = padd(ux, {(2, 0): bv(-1)})
    L = padd(A, vy)
    L1 = divide_three(L)
    K = padd(pmul(A, vy), pscale(-1, pmul(uy, vx)))
    Ebase = padd(L1, K, pderivative(Cbase, 0), pderivative(Dbase, 1))
    E1_6 = divide_three(degree_part(Ebase, 6))

    cx, cy = pderivative(Cbase, 0), pderivative(Cbase, 1)
    dx, dy = pderivative(Dbase, 0), pderivative(Dbase, 1)
    Mbase = padd(pmul(A, dy), pmul(cx, vy),
                 pscale(-1, pmul(uy, dx)),
                 pscale(-1, pmul(cy, vx)))
    F1_9 = divide_three(degree_part(Mbase, 9))

    # Source-honest exact controls for the already accepted top rows.  The
    # frozen Q9 census established their equivalence on all corrected-Q10
    # states; retaining both forms here makes a mismatch fail closed.
    Nbase = pbracket(Cbase, Dbase)
    constrain_row_zero(degree_part(Nbase, 12), 12)
    M11q = divide_three(degree_part(Mbase, 11))
    constrain_row_zero(padd(M11q, degree_part(Nbase, 11)), 11)
    E10q = divide_three(degree_part(Ebase, 10))
    F10q = divide_three(padd(E10q, degree_part(Mbase, 10)))
    constrain_row_zero(padd(F10q, degree_part(Nbase, 10)), 10)

    return {"U": U, "V": V, "A": A, "uy": uy, "vx": vx, "vy": vy,
            "L1": L1, "K": K, "Cbase": Cbase, "Dbase": Dbase,
            "E1_6": E1_6, "F1_9": F1_9}


source_data = canonical_source_symbolic()

# All 32 Q9 restoration digits and all 23 source rows.
C2 = homogeneous(2, xvars[0:3])
D2 = homogeneous(2, xvars[3:6])
C4 = homogeneous(4, xvars[6:11])
D4 = homogeneous(4, xvars[11:16])
W7 = homogeneous(7, xvars[16:24])
Z7 = homogeneous(7, xvars[24:32])
Cq9 = padd(source_data["Cbase"], C2, C4)
Dq9 = padd(source_data["Dbase"], D2, D4)
Eq9 = padd(source_data["L1"], source_data["K"],
            pderivative(Cq9, 0), pderivative(Dq9, 1))
cxq, cyq = pderivative(Cq9, 0), pderivative(Cq9, 1)
dxq, dyq = pderivative(Dq9, 0), pderivative(Dq9, 1)
Mq9 = padd(pmul(source_data["A"], dyq),
            pmul(cxq, source_data["vy"]),
            pscale(-1, pmul(source_data["uy"], dxq)),
            pscale(-1, pmul(cyq, source_data["vx"])))
F6q9 = padd(source_data["E1_6"], degree_part(Mq9, 6),
             pderivative(W7, 0), pderivative(Z7, 1))
N9q9 = degree_part(pbracket(Cq9, Dq9), 9)
Tq9 = padd(pmul(source_data["A"], pderivative(Z7, 1)),
            pmul(pderivative(W7, 0), source_data["vy"]),
            pscale(-1, pmul(source_data["uy"], pderivative(Z7, 0))),
            pscale(-1, pmul(pderivative(W7, 1), source_data["vx"])))
G9q9 = padd(source_data["F1_9"], N9q9, degree_part(Tq9, 9))
constrain_row_zero(Eq9, 1)
constrain_row_zero(Eq9, 3)
constrain_row_zero(F6q9, 6)
constrain_row_zero(G9q9, 9)

# All 32 Q8 restoration digits and all 22 source rows.
C3 = homogeneous(3, yvars[0:4])
D3 = homogeneous(3, yvars[4:8])
W4 = homogeneous(4, yvars[8:13])
Z4 = homogeneous(4, yvars[13:18])
W6 = homogeneous(6, yvars[18:25])
Z6 = homogeneous(6, yvars[25:32])
C0 = padd(source_data["Cbase"], C2, C3, C4)
D0 = padd(source_data["Dbase"], D2, D3, D4)
W0 = padd(W4, W6, W7)
Z0 = padd(Z4, Z6, Z7)


def core_intermediates(C, D, W, Z):
    E = padd(source_data["L1"], source_data["K"],
              pderivative(C, 0), pderivative(D, 1))
    cx, cy = pderivative(C, 0), pderivative(C, 1)
    dx, dy = pderivative(D, 0), pderivative(D, 1)
    M = padd(pmul(source_data["A"], dy),
              pmul(cx, source_data["vy"]),
              pscale(-1, pmul(source_data["uy"], dx)),
              pscale(-1, pmul(cy, source_data["vx"])))
    N = pbracket(C, D)
    T = padd(pmul(source_data["A"], pderivative(Z, 1)),
              pmul(pderivative(W, 0), source_data["vy"]),
              pscale(-1, pmul(source_data["uy"], pderivative(Z, 0))),
              pscale(-1, pmul(pderivative(W, 1), source_data["vx"])))
    Rmix = padd(pmul(cx, pderivative(Z, 1)),
                pmul(pderivative(W, 0), dy),
                pscale(-1, pmul(cy, pderivative(Z, 0))),
                pscale(-1, pmul(pderivative(W, 1), dx)))
    return E, M, N, T, Rmix


E0, M0, N0, T0, _ = core_intermediates(C0, D0, W0, Z0)
E1_3 = divide_three(degree_part(E0, 3))
E1_5 = divide_three(degree_part(E0, 5))
F3 = padd(E1_3, degree_part(M0, 3), pderivative(W4, 0),
           pderivative(Z4, 1))
F5 = padd(E1_5, degree_part(M0, 5), pderivative(W6, 0),
           pderivative(Z6, 1))
F1_8 = divide_three(degree_part(M0, 8))
G8 = padd(F1_8, degree_part(N0, 8), degree_part(T0, 8))
constrain_row_zero(E0, 2)
constrain_row_zero(F3, 3)
constrain_row_zero(F5, 5)
constrain_row_zero(G8, 8)

# All 18 Q7 restoration digits and all 19 source rows.
C6 = homogeneous(6, [rvars[0], 0, 0, rvars[1], 0, 0, rvars[2]])
D6 = homogeneous(6, [rvars[3], 0, 0, rvars[4], 0, 0, rvars[5]])
W5 = homogeneous(5, rvars[6:12])
Z5 = homogeneous(5, rvars[12:18])
C = padd(C0, C6)
D = padd(D0, D6)
W = padd(W0, W5)
Z = padd(Z0, Z5)
E, M, N, T, Rmix = core_intermediates(C, D, W, Z)
divWZ = padd(pderivative(W, 0), pderivative(Z, 1))
E1_4 = divide_three(degree_part(E, 4))
E1_5q = divide_three(degree_part(E, 5))
E1_7 = divide_three(degree_part(E, 7))
F4 = padd(E1_4, degree_part(M, 4), degree_part(divWZ, 4))
F5q = padd(E1_5q, degree_part(M, 5), degree_part(divWZ, 5))
F1_7 = divide_three(padd(E1_7, degree_part(M, 7)))
G7 = padd(F1_7, degree_part(N, 7), degree_part(T, 7))
constrain_row_zero(F5q, 5)
constrain_row_zero(F4, 4)
constrain_row_zero(G7, 7)

terminal_rows_omitted = os.environ.get("OMIT_TERMINAL", "0") == "1"
terminal_polys = {}
for degree in range(9, 13):
    E1 = divide_three(degree_part(E, degree))
    F = padd(E1, degree_part(M, degree), degree_part(divWZ, degree))
    F1 = divide_three(F)
    G = padd(F1, degree_part(N, degree), degree_part(T, degree))
    G1 = divide_three(G)
    terminal_polys[degree] = padd(G1, degree_part(Rmix, degree))
    if not terminal_rows_omitted:
        constrain_row_zero(terminal_polys[degree], degree)

smt2 = solver.to_smt2().encode()
Path(os.environ["SMT2_OUTPUT"]).write_bytes(smt2)
check = solver.check()
status = str(check)
result = {
    "solver_status": status,
    "solver_timeout_ms": int(os.environ.get("SOLVER_TIMEOUT_MS", "1")),
    "z3_version": z3.get_version_string(),
    "bit_width": WIDTH,
    "residue_modulus": MODULUS,
    "largest_product_bound": 728 * 728,
    "predecessor_variable_count": len(predecessor_names),
    "predecessor_row_counts": [len(matrix), len(N12), len(Q11), len(Q10)],
    "q9_raw_variable_count": len(xvars),
    "q9_explicit_source_row_count": 23,
    "q8_raw_variable_count": len(yvars),
    "q8_explicit_source_row_count": 22,
    "q7_raw_variable_count": len(rvars),
    "q7_explicit_source_row_count": 19,
    "terminal_row_count": 46,
    "terminal_rows_omitted": terminal_rows_omitted,
    "division_constraint_count": division_constraint_count,
    "pinned_predecessor": list(pinned_predecessor)
        if pinned_predecessor is not None else None,
    "pinned_structural": list(pinned_structural)
        if pinned_structural is not None else None,
    "smt2_sha256": hashlib.sha256(smt2).hexdigest(),
    "unsat_is_theorem_without_checked_proof_and_source_review": False,
    "scope": ("complete aligned vertical predecessor formula with raw "
              "Q9/Q8/Q7 variables"),
}

if check == z3.sat:
    model = solver.model()
    pred_values = [model.eval(pred_vars[name], model_completion=True).as_long()
                   for name in predecessor_names]
    xvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in xvars]
    yvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in yvars]
    rvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in rvars]
    assert all(0 <= value <= 2
               for value in pred_values + xvalues + yvalues + rvalues)
    result.update({
        "predecessor_values": pred_values,
        "q9_values": xvalues,
        "q8_values": yvalues,
        "q7_values": rvalues,
        "direct_integer_replay_required": True,
    })
elif check == z3.unknown:
    result["unknown_reason"] = solver.reason_unknown()

result["solver_statistics"] = str(solver.statistics())
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("solver_status", status)
print("predecessor_shapes", len(predecessor_names), len(matrix),
      len(N12), len(Q11), len(Q10))
print("raw_variable_shapes", len(xvars), len(yvars), len(rvars))
print("explicit_source_rows", 23, 22, 19, 46)
print("division_constraint_count", division_constraint_count)
print("terminal_rows_omitted", terminal_rows_omitted)
print("pinned_predecessor", pinned_predecessor)
print("pinned_structural", pinned_structural)
print("smt2_sha256", result["smt2_sha256"])
print("sat_model_emitted", check == z3.sat)
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-GLOBAL-PREDECESSOR-RAWQ7-EMITTER")
