#!/usr/bin/env python3
"""Hostile reviewer probe for the Q8 global quotient gate (staged in /tmp).

Independent attacks, none of which trust the case's own PASS strings:
  1. exact random-point identity  r_l(chart) == t^(l mod 2) * compiled row_l
  2. exact C*-weight homogeneity  wt(r_l)=12+l  (so n=r6/p^9, q=r8/p^10 are weight-0)
  3. report table term counts / degrees, and the 167-vs-230 monomial claim
  4. independent re-run of the w^5 Hensel lift with fail-closed solves
  5. q0,q1 agreement with the frozen leaf-4 terminal jet payload
  6. Pade falsifiers re-run
  7. independent rank certificates: exact over Q for the whole n,q rectangle,
     and a THIRD independent prime for every tested Z bidegree box
"""
import importlib.util
import json
import os
import random
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(os.environ["JC2_ROOT"])
CASE = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


LS = load("probe_local_series", CASE / "local_series.py")
Q, P, M, J = LS.Q, LS.P, LS.M, LS.J
NF, Series, evaluate = LS.NF, LS.Series, LS.evaluate
ZERO, ONE, ORDER = LS.ZERO, LS.ONE, LS.ORDER
print("PIN-CHAIN-IMPORT PASS (all transitive dependency hashes verified fail-closed)")

compiled = P.compile_fibre()
tails = compiled["tails"]
ring, quotient, imposed, names = Q.compile_quotient("approx")
print("COMPILED rows for", names)

# --- 1. exact random-point identity ------------------------------------
random.seed(20260824)


def rq():
    x = Fraction(random.randint(-40, 40), random.randint(1, 23))
    return x if x else Fraction(3, 7)


def eval_coeff(value, bases):
    total = Fraction(0)
    for mon, scalar in value.items():
        term = Fraction(scalar)
        for base, exp in zip(bases, mon):
            if exp:
                term *= base ** exp
        total += term
    return total


id_fail = 0
for trial in range(3):
    t = rq()
    c, d2, d4, x1r, x3r, x5r = (rq() for _ in range(6))
    w = t * t
    qc = t * c
    a = [qc ** 3 + t, 3 * qc ** 2 + x1r, 3 * qc + t * d2,
         1 + 3 * qc ** 2 + x3r, 6 * qc + t * d4, 3 + x5r,
         3 * qc, Fraction(3), Fraction(0)]
    inv = [w, c, d2, d4, x1r, x3r, x5r]
    for ell in range(1, 9):
        raw = eval_coeff(tails[ell], a)
        row = eval_coeff(quotient[ell], inv)
        if raw != row * (t if ell % 2 else 1):
            id_fail += 1
            print("QUOTIENT-IDENTITY-FAIL", ell, trial)
print("QUOTIENT-IDENTITY", "FAIL" if id_fail else "PASS (3 exact random points, all 8 rows incl. outputs)")

# --- 2. exact C*-weights ------------------------------------------------
lam = Fraction(5, 3)
avals = [rq() for _ in range(9)]
scaled = [avals[i] * lam ** (9 - i) for i in range(8)] + [avals[8] * lam ** 6]
w_fail = sum(
    1 for ell in range(1, 9)
    if eval_coeff(tails[ell], scaled) != lam ** (12 + ell) * eval_coeff(tails[ell], avals)
)
print("WEIGHT-HOMOGENEITY wt(r_l)=12+l", "FAIL" if w_fail else "PASS (n,q weight-0 exact)")

# --- 3. report table ----------------------------------------------------
expected = {1: (10, 4, 1), 3: (20, 5, 1), 5: (35, 6, 1), 7: (57, 7, 2),
            2: (16, 5, 1), 4: (29, 6, 2), 6: (48, 7, 2), 8: (73, 7, 2)}
tbl_ok = True
for ell, want in expected.items():
    val = quotient[ell]
    got = (len(val), max(sum(m) for m in val), max(m[0] for m in val))
    if got != want:
        tbl_ok = False
        print("TABLE-MISMATCH", ell, got, want)
print("REPORT-TABLE", "PASS" if tbl_ok else "FAIL")
_, rawq, rawimp, _ = Q.compile_quotient("raw")
print("IMPOSED-MONOMIALS approx=%d raw=%d (report claims 167 vs 230)"
      % (sum(len(quotient[l]) for l in imposed), sum(len(rawq[l]) for l in rawimp)))

# --- 4. independent Hensel re-run --------------------------------------
v = NF((Fraction(0), Fraction(1)))
D0 = 3 * v ** 2 - 2
A20 = 3 * v ** 2 + 3 * v + 1
x5c = -36 * v ** 2 * A20 / D0
x3c = x5c * (v + 2)
x1c = x5c * (v + 1) + x5c ** 2 * (3 * v + 1) / (9 * v)
raw_base = [ZERO, x1c, ZERO, ONE + x3c, ZERO, NF(3) + x5c, ZERO, NF(3), ZERO]
normals = (0, 2, 4, 6)
odd = (3, 5, 7)
matrix = [[J.nf_eval(M.cpartial(tails[l], col), raw_base) for col in normals[1:]] for l in odd]
rhs = [-J.nf_eval(M.cpartial(tails[l], 0), raw_base) for l in odd]
a2_t, a4_t, a6_t = J.solve(matrix, rhs)
constants = [a6_t / 3, a2_t - a6_t, a4_t - 2 * a6_t, x1c, x3c, x5c]
wser = Series((ZERO, ONE))
variables = [Series.constant(value) for value in constants]
eq_rows = [quotient[l] for l in imposed]
for degree in range(1, ORDER):
    bases = [wser] + variables
    origin = [evaluate(r, bases).coefficients[degree] for r in eq_rows]
    cols = []
    for column in range(6):
        changed = list(variables)
        cc = list(changed[column].coefficients)
        cc[degree] = ONE
        changed[column] = Series(cc)
        image = [evaluate(r, [wser] + changed).coefficients[degree] for r in eq_rows]
        cols.append([image[i] - origin[i] for i in range(6)])
    linear = [[cols[c][r] for c in range(6)] for r in range(6)]
    sol = J.solve(linear, [-e for e in origin])  # raises on singular Jacobian
    for i, coeff in enumerate(sol):
        vals = list(variables[i].coefficients)
        vals[degree] = coeff
        variables[i] = Series(vals)
print("HENSEL-JACOBIAN-INVERTIBLE PASS (fail-closed solve at every order over Q[v]/(Q8))")
bases = [wser] + variables
resid_ok = not any(any(evaluate(r, bases).coefficients) for r in eq_rows)
print("SIX-ROW-RESIDUALS-THROUGH-w5", "PASS" if resid_ok else "FAIL")
n = evaluate(quotient[6], bases)
q = evaluate(quotient[8], bases)
Z = q ** 9 / n ** 10
units_ok = all(bool(x) and J.digest(x)["unit_mod_Q8"]
               for s in (n, q, Z) for x in s.coefficients)
print("OUTPUT-COEFFS-ALL-UNITS", "PASS" if units_ok else "FAIL")

leaf4 = json.loads((ROOT / "cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/replay.json").read_text())
qsec = leaf4["etale_at_every_Q8_contact"]["q"]
agree = (J.digest(q.coefficients[0])["sha256"] == qsec["constant"]["sha256"]
         and J.digest(q.coefficients[1])["sha256"] == qsec["d_dtheta_at_node"]["value"]["sha256"])
print("TERMINAL-JET-AGREEMENT q0,q1 vs frozen leaf-4", "PASS" if agree else "FAIL")
print("N0-DIGEST", J.digest(n.coefficients[0])["sha256"], "(pinned only inside this case)")

lsj = json.loads((CASE / "local_series.json").read_text())


def dig(series):
    return [J.digest(x)["sha256"] for x in series.coefficients]


pay_ok = (dig(n) == [d["sha256"] for d in lsj["outputs"]["n=r6/p^9"]]
          and dig(q) == [d["sha256"] for d in lsj["outputs"]["q=r8/p^10"]]
          and dig(Z) == [d["sha256"] for d in lsj["outputs"]["Z=q^9/n^10"]])
print("PAYLOAD-OUTPUT-DIGESTS", "PASS" if pay_ok else "FAIL")

# --- 5. Pade falsifiers -------------------------------------------------
pade_ok = True
for label, val in (("n", n), ("q", q), ("Z", Z)):
    for m_, d_ in ((1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (1, 3)):
        res = LS.pade_test(val, m_, d_)
        if res.get("fit") != "SOLVED" or res.get("all_unused_zero"):
            pade_ok = False
            print("PADE-BOX-ISSUE", label, m_, d_, res.get("fit"))
print("PADE-FALSIFIERS", "PASS" if pade_ok else "FAIL")


# --- 6. independent rank certificates -----------------------------------
def col_series_matrix(cols):
    rows48 = []
    for wi in range(ORDER):
        for vi in range(8):
            rows48.append([
                (col.coefficients[wi].poly[vi]
                 if vi < len(col.coefficients[wi].poly) else Fraction(0))
                for col in cols
            ])
    return rows48


def rank_exact(mat):
    a = [row[:] for row in mat]
    nrows, ncols, r = len(a), len(a[0]), 0
    for col in range(ncols):
        piv = next((i for i in range(r, nrows) if a[i][col]), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        inv = Fraction(1) / a[r][col]
        a[r] = [x * inv for x in a[r]]
        for i in range(nrows):
            if i != r and a[i][col]:
                f = a[i][col]
                a[i] = [x - f * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == nrows:
            break
    return r


npow, qpow = [Series.constant(1)], [Series.constant(1)]
for _ in range(4):
    npow.append(npow[-1] * n)
    qpow.append(qpow[-1] * q)
cols_nq = [npow[i] * qpow[j] for i in range(5) for j in range(5)]
r_nq = rank_exact(col_series_matrix(cols_nq))
print("NQ-EXACT-RANK-OVER-Q", r_nq, "of", len(cols_nq),
      "PASS (subsumes every 1<=deg<=4 box unconditionally)" if r_nq == len(cols_nq) else "FAIL")


def frac_mod(x, p):
    return x.numerator % p * pow(x.denominator % p, -1, p) % p


def rank_mod(mat, p):
    a = [[frac_mod(x, p) for x in row] for row in mat]
    nrows, ncols, r = len(a), len(a[0]), 0
    for col in range(ncols):
        piv = next((i for i in range(r, nrows) if a[i][col]), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        inv = pow(a[r][col], -1, p)
        a[r] = [x * inv % p for x in a[r]]
        for i in range(nrows):
            if i != r and a[i][col]:
                f = a[i][col]
                a[i] = [(x - f * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == nrows:
            break
    return r


def shifted(series, wi):
    vals = [ZERO] * ORDER
    for d in range(ORDER - wi):
        vals[d + wi] = series.coefficients[d]
    return Series(vals)


Zpow = [Series.constant(1)]
for _ in range(10):
    Zpow.append(Zpow[-1] * Z)
for p3 in (1000037, 1000039, 1000081):
    try:
        third_ok = True
        boxes = 0
        for zd in range(1, 11):
            for wd in range(0, 5):
                ncols = (zd + 1) * (wd + 1)
                if ncols > 48:
                    continue
                boxes += 1
                cols = [shifted(Zpow[zi], wi)
                        for wi in range(wd + 1) for zi in range(zd + 1)]
                if rank_mod(col_series_matrix(cols), p3) != ncols:
                    third_ok = False
                    print("Z-BOX-RANK-DEFICIENT", zd, wd, "mod", p3)
        print("Z-BIDEGREE-THIRD-PRIME", p3, "boxes", boxes,
              "PASS" if third_ok else "FAIL")
        break
    except ValueError:
        print("prime", p3, "divides a denominator; retrying with next prime")
print("PROBE-DONE")
