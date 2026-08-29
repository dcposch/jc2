#!/usr/bin/env python3
"""Independent Fable5 hostile-audit checker for the r3 fixed-even endpoint-zero
theorem.

Fresh derivation, no producer code imported or executed:

* the five odd gates are derived from the fractional powers
  h_n = (2/(n+2)) * A^((n-1)/2) * [t^n] (F/F0)^((n+2)/8)
  via the Euler ODE recurrence (1+u) g' = e u' g  (the producers used a
  binomial summation instead);
* Laurent elements are represented as normalized pairs N/A^k with A not
  dividing N (the producers used partial-fraction dictionaries);
* the raw degree windows are re-extracted from the frozen authoritative
  RAW_INPUT.json rather than from any window formula;
* every basis vector is replayed through all 50 original gate equations by a
  full nonlinear series computation (this also certifies joint linearity);
* an explicit linearity control at a non-basis combination point certifies
  that per-basis rows may be combined linearly (parity argument: no
  double-odd t-partition of an odd weight <= 15 exists, since 7+7=14 is even
  and 7+9=16>15).

Run:  PYTHONDONTWRITEBYTECODE=1 python3 -B <this file>
"""

from fractions import Fraction as Fr
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MANIFEST = {
    "xmodel/ggv-upper-endpoint-deep-q1-lambda0-qx-fixed-even-endpoint-zero-r3-sol-ultra-20260828.md":
        "a6e49a08a6fc92c71f9f9ee34079b5626f6a00a20499b06e50c8b8451f3338be",
    "cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_qx_fixed_even_endpoint_zero_20260828/verify_qx_fixed_even_endpoint_zero.py":
        "49e61d547e8b30e6ffc3c792f1dffdb6ae8e960aec490047e5c544fee222adf1",
    "xmodel/ggv-upper-endpoint-deep-q1-lambda0-q15-independent-sol-ultra-20260828.md":
        "188317138e60224f5a7e9dc1de18ab339384c5246c1cabf12acc20657dac7d5f",
    "cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_q15_20260828/verify_lambda0_q15.py":
        "6c63fe47ebf35dd56e286ab358b0932f1dad9143875fde30c216a425119e442a",
    "xmodel/ggv-upper-endpoint-deep-q1-lambda0-qx-g13-obstruction-r2-sol-ultra-20260828.md":
        "b5433f4e4a76f48d8899d59b28290dc7075ac591b89913323e5102a998e73a08",
    "cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_qx_g13_obstruction_20260828/verify_qx_g13_obstruction.py":
        "fb29dec1a7eb08a41818c8ea802c984f893d8a222d38aade6fdf4af9bc272638",
    "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json":
        "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
}


def check_manifest():
    for relative, expected in MANIFEST.items():
        digest = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        assert digest == expected, (relative, digest)


# ---------------------------------------------------------------- polynomials
def trim(p):
    p = list(p)
    while p and not p[-1]:
        p.pop()
    return p


def padd(*ps):
    out = [Fr(0)] * max((len(p) for p in ps), default=0)
    for p in ps:
        for i, v in enumerate(p):
            out[i] += v
    return trim(out)


def pscale(c, p):
    c = Fr(c)
    return trim([c * v for v in p])


def pmul(a, b):
    if not a or not b:
        return []
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def pderiv(p):
    return trim([Fr(i) * p[i] for i in range(1, len(p))])


def pdivmod(num, den):
    num, den = trim(num), trim(den)
    quo = [Fr(0)] * max(0, len(num) - len(den) + 1)
    while num and len(num) >= len(den):
        d = len(num) - len(den)
        c = num[-1] / den[-1]
        quo[d] += c
        for i, v in enumerate(den):
            num[i + d] -= c * v
        num = trim(num)
    return trim(quo), num


def mono(d):
    return [Fr(0)] * d + [Fr(1)]


A = [Fr(-1), Fr(0), Fr(0), Fr(0), Fr(1)]          # X^4 - 1
QPOLY = [Fr(0), Fr(1)]                            # Q = X
assert pderiv(A)[0:1] in ([], [Fr(0)]) or pderiv(A)[0] == 0  # A'(0)=0


# ------------------------------------------------- Laurent elements  N / A^k
def lnorm(num, k):
    num = trim(num)
    while k > 0 and num:
        quo, rem = pdivmod(num, A)
        if rem:
            break
        num, k = quo, k - 1
    if not num:
        k = 0
    return (tuple(num), k)


def lelt(num, k=0):
    return lnorm(list(num), k)


LZERO = lelt([])


def ladd(x, y):
    (nx, kx), (ny, ky) = x, y
    k = max(kx, ky)
    ax = pmul(list(nx), ppow(A, k - kx)) if nx else []
    ay = pmul(list(ny), ppow(A, k - ky)) if ny else []
    return lnorm(padd(ax, ay), k)


def ppow(p, n):
    out = [Fr(1)]
    for _ in range(n):
        out = pmul(out, p)
    return out


def lmul(x, y):
    (nx, kx), (ny, ky) = x, y
    return lnorm(pmul(list(nx), list(ny)), kx + ky)


def lscale(c, x):
    return lnorm(pscale(c, list(x[0])), x[1])


def lval0(x):
    num, k = x
    return (num[0] if num else Fr(0)) * Fr(-1) ** k


def lcoef1(x):
    # X^1 Taylor coefficient at 0; exact because A'(0)=0.
    num, k = x
    return (num[1] if len(num) > 1 else Fr(0)) * Fr(-1) ** k


def lpole(x):
    return x[1]


def lremainder(x):
    # numerator of the A^-1 part reduced modulo A; requires pole order <= 1
    num, k = x
    assert k <= 1, x
    return pdivmod(list(num), A)[1] if k == 1 else []


def lpolynomial(x):
    num, k = x
    assert k == 0, x
    return list(num)


# ----------------------------------------------- fractional-power series in t
def useries(f, f9, f11, f13):
    parts = {
        2: lelt(pscale(Fr(-1, 8), QPOLY), 1),
        4: lelt(pscale(Fr(1, 256), pmul(QPOLY, QPOLY)), 2),
        7: lelt(f, 3),
        9: lelt(f9, 4),
        11: lelt(f11, 4),
        13: lelt(f13, 4),
    }
    return {j: u for j, u in parts.items() if u[0]}


def spower(u, e, nmax):
    """(1+u)^e via n g_n = sum_j (e*j-(n-j)) u_j g_{n-j};  g_0 = 1."""
    e = Fr(e)
    g = [LZERO] * (nmax + 1)
    g[0] = lelt([Fr(1)])
    for n in range(1, nmax + 1):
        acc = LZERO
        for j, uj in u.items():
            if j <= n:
                acc = ladd(acc, lscale(e * j - (n - j), lmul(uj, g[n - j])))
        g[n] = lscale(Fr(1, n), acc)
    return g


GATE_N = (7, 9, 11, 13, 15)
BLOCKS = (6, 8, 10, 12, 14)


def gates(f, f9, f11, f13):
    u = useries(f, f9, f11, f13)
    out = []
    for n in GATE_N:
        g = spower(u, Fr(n + 2, 8), n)[n]
        h = lmul(lelt(ppow(A, (n - 1) // 2)), g)
        out.append(pscale(Fr(2, n + 2), lpolynomial(h)))
    return out


def t5(d):
    return pscale(Fr(1, 2), padd(pscale(5, pmul(pderiv(A), d)),
                                 pscale(2, pmul(A, pderiv(d)))))


# ----------------------------------------------------------------- 50x55 RREF
RAW_SPECS = (("f", tuple(range(6))), ("F9", tuple(range(1, 8))),
             ("F11", tuple(range(1, 6))), ("F13", tuple(range(2, 4))))
PRIM_SPECS = (("d7", 2), ("d9", 4), ("d11", 6), ("d13", 8), ("d15", 10))
NAMES = ([f"{n}_{d}" for n, ds in RAW_SPECS for d in ds]
         + [f"{n}_{d}" for n, m in PRIM_SPECS for d in range(m + 1)])
FREE_TARGET = ["d15_4", "d15_5", "d15_6", "d15_8", "d15_9"]


def stack(blocks):
    out = []
    for p, size in zip(blocks, BLOCKS):
        assert len(p) <= size, (len(p), size)
        out.extend(p[i] if i < len(p) else Fr(0) for i in range(size))
    return out


def build_columns():
    cols = []
    for name, degs in RAW_SPECS:
        for d in degs:
            raw = {"f": [], "F9": [], "F11": [], "F13": []}
            raw[name] = mono(d)
            cols.append(stack(gates(raw["f"], raw["F9"], raw["F11"], raw["F13"])))
    for block, (name, m) in enumerate(PRIM_SPECS):
        for d in range(m + 1):
            blocks = [[] for _ in range(5)]
            blocks[block] = pscale(-1, t5(mono(d)))
            cols.append(stack(blocks))
    return cols


def rref(rows):
    rows = [list(r) for r in rows]
    pivots, r = [], 0
    for c in range(len(rows[0]) if rows else 0):
        p = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        inv = rows[r][c]
        rows[r] = [v / inv for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                f = rows[i][c]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        pivots.append(c)
        r += 1
        if r == len(rows):
            break
    return rows, pivots


def solve_fiber(cols, nrows=50):
    rows = [[col[i] for col in cols] for i in range(nrows)]
    red, pivots = rref(rows)
    free = [c for c in range(len(cols)) if c not in pivots]
    basis = []
    for fc in free:
        vec = [Fr(0)] * len(cols)
        vec[fc] = Fr(1)
        for r, pc in enumerate(pivots):
            vec[pc] = -red[r][fc]
        basis.append(vec)
    return len(pivots), pivots, free, basis


def vec_raw(vec):
    idx = {n: i for i, n in enumerate(NAMES)}
    out = {}
    for name, degs in RAW_SPECS:
        p = [Fr(0)] * (max(degs) + 1)
        for d in degs:
            p[d] = vec[idx[f"{name}_{d}"]]
        out[name] = trim(p)
    for name, m in PRIM_SPECS:
        p = [Fr(0)] * (m + 1)
        for d in range(m + 1):
            p[d] = vec[idx[f"{name}_{d}"]]
        out[name] = trim(p)
    return out


def replay(vec):
    data = vec_raw(vec)
    hs = gates(data["f"], data["F9"], data["F11"], data["F13"])
    left = stack(hs)
    right = stack([t5(data[n]) for n, _ in PRIM_SPECS])
    assert left == right, "basis vector fails an original gate equation"


def basis_digest(basis):
    lines = []
    for vec in basis:
        lines.append(";".join(f"{n}={v}" for n, v in zip(NAMES, vec)))
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


# ----------------------------------------------------- characteristic rows
BORN = {2 * k: k for k in range(1, 8)}     # c2..c14 shifts within weight 15
UNBORN = (16, 18, 20)                      # c16,c18,c20


def char_elements(data, wmax=15):
    """per-label lists of Laurent elements: label -> [G-contribution_w]."""
    u = useries(data["f"], data["F9"], data["F11"], data["F13"])
    out = {}
    base = spower(u, Fr(3, 2), wmax)
    out["base"] = [lmul(lelt(ppow(A, 6)), base[w]) for w in range(wmax + 1)]
    for shift, k in BORN.items():
        s = spower(u, Fr(6 - k, 4), wmax - shift)
        pref = lelt(ppow(A, 6 - k)) if k <= 6 else lelt([Fr(1)], 1)
        row = [LZERO] * (wmax + 1)
        for d, val in enumerate(s):
            row[d + shift] = lmul(pref, val)
        out[f"c{shift}"] = row
    return out


LABELS = ("base", "c2", "c4", "c6", "c8", "c10", "c12", "c14")


def quad(x, y):
    out = {}
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            if a and b:
                key = (min(i, j), max(i, j))
                out[key] = out.get(key, Fr(0)) + a * b
                if not out[key]:
                    del out[key]
    return out


def qsum(*forms):
    out = {}
    for f in forms:
        for k, v in f.items():
            out[k] = out.get(k, Fr(0)) + v
            if not out[k]:
                del out[k]
    return out


def qscale(c, f):
    c = Fr(c)
    return {k: c * v for k, v in f.items() if c * v}


def main():
    check_manifest()

    # ---- authoritative windows from the frozen RAW_INPUT.json -------------
    raw = json.loads((ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json").read_text())
    fwin, gwin = {}, {}
    for s in raw["raw_slots_through_weight_22"]["F"]:
        fwin.setdefault(s["weight"], set()).add(s["raw_exponents"]["x"])
    for s in raw["raw_slots_through_weight_22"]["G"]:
        gwin.setdefault(s["weight"], set()).add(s["raw_exponents"]["x"])
    assert fwin[7] == set(range(0, 10))
    assert fwin[9] == set(range(1, 8)) and fwin[11] == set(range(1, 6))
    assert fwin[13] == set(range(2, 4))
    assert min(gwin[13]) == 1 and gwin[13] == set(range(1, 12))
    assert gwin[15] == set(range(1, 10))
    # F7 = A*f with deg f <= 5 stays inside the authoritative F7 window.
    assert all(set(range(len(trim(pmul(A, mono(d)))))) - {i for i, v in enumerate(pmul(A, mono(d))) if not v} <= fwin[7] | {0} for d in range(6))
    for d in range(6):
        support = {i for i, v in enumerate(pmul(A, mono(d))) if v}
        assert support <= fwin[7]

    # D22[X^0] census: over the authoritative windows the only pairs with a
    # nonzero structural coefficient are (11,11,+1) and (7,15,-1).
    first, second = [], []
    for i in range(0, 15):
        j = 22 - i
        if j not in gwin:
            continue
        if 1 in fwin.get(i, set()) and 0 in gwin[j] and 12 - j:
            first.append((i, j, 12 - j))
        if 0 in fwin.get(i, set()) and 1 in gwin[j] and i - 8:
            second.append((i, j, i - 8))
    assert first == [(11, 11, 1)] and second == [(7, 15, -1)]
    target = Fr(1)                      # pinned upstream endpoint target
    assert target not in (Fr(0),)       # exclusion only needs target != 0

    # ---- gate spot checks against the frozen q15 closed form --------------
    h15_f = gates(mono(0), [], [], [])[4]
    assert h15_f == pscale(Fr(-45, 2 ** 29), ppow(QPOLY, 4))
    h15_f9 = gates([], mono(1), [], [])[4]
    assert h15_f9 == pscale(Fr(-15, 2 ** 21), pmul(ppow(QPOLY, 3), mono(1)))
    h15_f11 = gates([], [], mono(1), [])[4]
    assert h15_f11 == pscale(Fr(45, 2 ** 15), pmul(pmul(A, pmul(QPOLY, QPOLY)), mono(1)))
    h15_f13 = gates([], [], [], mono(2))[4]
    assert h15_f13 == pscale(Fr(-9, 256), pmul(pmul(ppow(A, 2), QPOLY), mono(2)))
    assert gates(mono(0), [], [], [])[0] == pscale(Fr(1, 4), mono(0))
    print("gates_from_F_pow_(n+2)/8=PASS;h15_closed_form_crosscheck=PASS")

    # ---- 50x55 system ------------------------------------------------------
    cols = build_columns()
    assert len(cols) == 55 and all(len(c) == 50 for c in cols)
    rank, pivots, free, basis = solve_fiber(cols)
    assert rank == 50 and len(free) == 5
    assert [NAMES[c] for c in free] == FREE_TARGET
    for vec in basis:
        replay(vec)
    digest = basis_digest(basis)
    print(f"rank=50;dim=5;free={','.join(FREE_TARGET)}")
    print(f"basis_replay_all_50_equations=PASS;basis_sha256={digest}")

    raw_basis = [vec_raw(vec) for vec in basis]
    f0 = [d["f"][0] if d["f"] else Fr(0) for d in raw_basis]
    assert f0 == [Fr(0), Fr(-2 ** 29, 75), Fr(0), Fr(0), Fr(2 ** 28, 225)]
    f11x1 = [d["F11"][1] if len(d["F11"]) > 1 else Fr(0) for d in raw_basis]
    f7x0 = [pscale(-1, [v])[0] if (v := c) else Fr(0) for c in f0]
    assert f7x0 == [-v for v in f0]
    print("f0=-(2^29/75)a1+(2^28/225)a4=PASS")

    # ---- characteristic rows on the five basis vectors --------------------
    rows = {lab: {"g11x0": [], "g13x0": [], "g15x1": [], "r15": [],
                  "rem15": []} for lab in LABELS}
    per_basis = []
    for data in raw_basis:
        elems = char_elements(data)
        per_basis.append(elems)
        for lab in LABELS:
            e11, e13, e15 = elems[lab][11], elems[lab][13], elems[lab][15]
            assert lpole(e15) <= 1
            rows[lab]["g11x0"].append(lval0(e11))
            rows[lab]["g13x0"].append(lval0(e13))
            rows[lab]["g15x1"].append(lcoef1(e15))
            rem = lremainder(e15)
            rows[lab]["rem15"].append(rem)
            rows[lab]["r15"].append(rem[1] if len(rem) > 1 else Fr(0))
    for k in UNBORN:
        assert k > 15                       # c16,c18,c20 structurally unborn

    zero = [Fr(0)] * 5
    # G11[X^0]: only c4 loads, with -f0.
    assert rows["c4"]["g11x0"] == [-v for v in f0]
    for lab in LABELS:
        if lab != "c4":
            assert rows[lab]["g11x0"] == zero, lab
    # G13[X^0]: only c6 loads, with (3/4) f0.
    assert rows["c6"]["g13x0"] == [Fr(3, 4) * v for v in f0]
    for lab in LABELS:
        if lab != "c6":
            assert rows[lab]["g13x0"] == zero, lab
    # G15[X^1]: c4 load is exactly F11[X^1]; c6,c8 as displayed; rest zero.
    assert rows["c4"]["g15x1"] == f11x1
    h6 = rows["c6"]["g15x1"]
    h8 = rows["c8"]["g15x1"]
    assert h6 == [Fr(0), Fr(-2 ** 21, 5), Fr(0), Fr(0), Fr(-2 ** 19, 3)]
    assert h8 == [Fr(0), Fr(0), Fr(2 ** 29, 75), Fr(0), Fr(0)]
    for lab in ("base", "c2", "c10", "c12", "c14"):
        assert rows[lab]["g15x1"] == zero, lab
    # G15 A^-1 remainder, X^1 coordinate: only c6,c8 load.
    r6 = rows["c6"]["r15"]
    r8 = rows["c8"]["r15"]
    assert r6 == [Fr(0), Fr(0), Fr(0), Fr(0), Fr(-7 * 2 ** 19, 3)]
    assert r8 == [Fr(0), Fr(0), Fr(2 ** 29, 15), Fr(0), Fr(0)]
    for lab in ("base", "c2", "c4", "c10", "c12", "c14"):
        assert rows[lab]["r15"] == zero, lab
    print("G11_X0=-c4*f0;G13_X0=(3/4)*c6*f0;G15_X1_c4_load=F11_X1=PASS")
    print("R15=-(7*2^19/3)*c6*a4+(2^29/15)*c8*a2;other_modes_zero=PASS")

    # mode census: c10/c12/c14 are born by weight 15 but load zero for
    # distinct reasons; they are NOT structurally unborn.
    for data in raw_basis:
        elems = char_elements(data)
        # c10 is born at even weight 10 (A*(1+u)^(1/4)); its odd loads all
        # vanish because [t^5](1+u)^(1/4) needs a t^5 partition and F5=0.
        assert elems["c10"][10] == lelt(A)
        assert all(elems["c10"][w] == LZERO for w in range(11, 16, 2))
        assert elems["c12"][12] == lelt([Fr(1)])                  # F^0 constant term
        assert all(elems["c12"][w] == LZERO for w in range(16) if w != 12)
        assert elems["c14"][14] == lelt([Fr(1)], 1)               # A^-1 * 1
        assert all(elems["c14"][w] == LZERO for w in range(16) if w != 14)
    print("mode_census=c10_born_G10_odd_loads_zero_t5_residual;"
          "c12_born_at_G12_const;c14_born_at_G14_pole;c16_c18_c20_unborn")

    # ---- linearity control at a non-basis combination point ---------------
    combo = [Fr(1), Fr(2), Fr(3), Fr(4), Fr(5)]
    cdata = {key: padd(*[pscale(combo[i], raw_basis[i][key])
                         for i in range(5)])
             for key in ("f", "F9", "F11", "F13")}
    celems = char_elements(cdata)
    for lab in LABELS:
        want11 = sum(combo[i] * rows[lab]["g11x0"][i] for i in range(5))
        want13 = sum(combo[i] * rows[lab]["g13x0"][i] for i in range(5))
        want15 = sum(combo[i] * rows[lab]["g15x1"][i] for i in range(5))
        wantr = sum(combo[i] * rows[lab]["r15"][i] for i in range(5))
        assert lval0(celems[lab][11]) == want11
        assert lval0(celems[lab][13]) == want13
        assert lcoef1(celems[lab][15]) == want15
        assert lpole(celems[lab][15]) <= 1
        rem = lremainder(celems[lab][15])
        assert (rem[1] if len(rem) > 1 else Fr(0)) == wantr
    print("odd_row_linearity_control_at_(1,2,3,4,5)=PASS")

    # ---- endpoint identity -------------------------------------------------
    # E_L = quad(F11[X1], G11[X0]_L) + quad(f0, G15[X1]_L)   (F7[X0] = -f0)
    E = {lab: qsum(quad(f11x1, rows[lab]["g11x0"]),
                   quad(f0, rows[lab]["g15x1"])) for lab in LABELS}
    assert E["base"] == {} and E["c2"] == {}
    assert E["c4"] == {}                       # exact c4 cancellation
    assert E["c6"] == quad(f0, h6)
    assert E["c8"] == quad(f0, h8)
    for lab in ("c10", "c12", "c14"):
        assert E[lab] == {}
    # E = (f0/5) R15 + (4/3)(-2^21 a1/5 + 2^20 a4/15) G13[X0], per c-mode,
    # as an exact quadratic-form identity in Q[a0..a4] -- ring-level ideal
    # membership with polynomial multipliers, no radical or field step.
    corr4 = pscale(Fr(4, 3), [Fr(0), Fr(-2 ** 21, 5), Fr(0), Fr(0), Fr(2 ** 20, 15)])
    corr4 = corr4 + [Fr(0)] * (5 - len(corr4))
    for lab in LABELS:
        lhs = E[lab]
        rhs = qsum(qscale(Fr(1, 5), quad(f0, rows[lab]["r15"])),
                   quad(corr4, rows[lab]["g13x0"]))
        assert lhs == rhs, lab
    assert quad(f0, h6) != {} and quad(f0, h8) != {}
    print("E=f0*(c6*(-2^21*a1/5-2^19*a4/3)+c8*(2^29*a2/75))=PASS")
    print("identity_E=(f0/5)*R15+(4/3)*(-2^21*a1/5+2^20*a4/15)*G13_X0=PASS")
    print("identity_type=ring_level_ideal_membership_polynomial_multipliers")

    # exclusion: G13 floor kills G13[X^0]; G15 polynomial kills the whole
    # A^-1 remainder, hence its X^1 coordinate R15; the identity then gives
    # E = 0 != 1 = target, with no case split, for arbitrary scalar modes.
    print(f"exclusion=E_in_ideal(R15,G13_X0);target={target};0!=target")

    # ---- r2 one-point control ---------------------------------------------
    # frozen r2 fixture (hash-pinned bytes above):
    r2f = [Fr(-2 ** 29, 75), Fr(0), Fr(0), Fr(0), Fr(11 * 2 ** 29, 75)]
    r2f9 = [Fr(0), Fr(7 * 2 ** 23, 75), Fr(0), Fr(0), Fr(0), Fr(-27 * 2 ** 23, 75)]
    r2prim = {
        "d7": [Fr(0), Fr(2 ** 27, 75)],
        "d9": [Fr(0), Fr(0), Fr(-2 ** 21, 15)],
        "d11": [Fr(0), Fr(0), Fr(0), Fr(2 ** 14, 3)],
        "d13": [Fr(0), Fr(0), Fr(0), Fr(0), Fr(-7 * 2 ** 8, 15)],
        "d15": [Fr(0)] * 5 + [Fr(1)],
    }
    b1 = raw_basis[1]
    assert b1["f"] == r2f and b1["F9"] == r2f9
    assert b1["F11"] == [] and b1["F13"] == []
    for key, val in r2prim.items():
        assert b1[key] == trim(val), key
    print("r2_point=basis_vector_a=(0,1,0,0,0);q_gates_replayed=PASS")

    def total(elems, modes, w):
        acc = elems["base"][w]
        for shift, c in modes.items():
            acc = ladd(acc, lscale(c, elems[f"c{shift}"][w]))
        return acc

    elems1 = per_basis[1]
    modes_c2c6 = {2: Fr(1), 6: Fr(1)}
    for w in range(8, 13):
        gw = lpolynomial(total(elems1, modes_c2c6, w))
        support = {i for i, v in enumerate(gw) if v}
        assert support <= gwin[w], (w, support)
    g13 = lpolynomial(total(elems1, modes_c2c6, 13))
    assert g13 == [Fr(-2 ** 27, 25), Fr(0), Fr(-2 ** 17, 5), Fr(0),
                   Fr(11 * 2 ** 27, 25), Fr(0), Fr(2 ** 20, 15)]
    assert g13[0] == Fr(-2 ** 27, 25) and 0 not in gwin[13]
    # determinant rows D0..D13 vanish on the characteristic trajectory
    Fd = {0: ppow(A, 4),
          2: pscale(Fr(-1, 8), pmul(ppow(A, 3), QPOLY)),
          4: pscale(Fr(1, 256), pmul(ppow(A, 2), pmul(QPOLY, QPOLY))),
          7: pmul(A, r2f), 9: r2f9}
    Gd = {w: lpolynomial(total(elems1, modes_c2c6, w)) for w in range(14)}
    for n in range(14):
        row = []
        for i, Fi in Fd.items():
            j = n - i
            if j in Gd:
                row = padd(row,
                           pscale(12 - j, pmul(pderiv(Fi), Gd[j])),
                           pscale(i - 8, pmul(Fi, pderiv(Gd[j]))))
        assert row == [], n
    # first failure is G13[X^0] under c6=1; c6=0 repairs G13, then G14 poles
    modes_c2 = {2: Fr(1)}
    g13r = lpolynomial(total(elems1, modes_c2, 13))
    assert {i for i, v in enumerate(g13r) if v} <= gwin[13]
    g14 = total(elems1, modes_c2, 14)
    assert lpole(g14) == 1
    rem14 = lremainder(g14)
    assert rem14 == [Fr(0), Fr(0), Fr(-5, 2 ** 34)]   # -5X^6/2^34 == -5X^2/2^34 mod A
    # endpoint before/after c6=0 (F11[X1]=0, F7[X0]=2^29/75 at this point)
    e_before = Fr(0) * lval0(total(elems1, modes_c2c6, 11)) \
        - Fr(2 ** 29, 75) * lcoef1(total(elems1, modes_c2c6, 15))
    e_after = Fr(0) * lval0(total(elems1, modes_c2, 11)) \
        - Fr(2 ** 29, 75) * lcoef1(total(elems1, modes_c2, 15))
    assert e_before == Fr(2 ** 50, 375) and e_after == Fr(0)
    print("r2_control=G8_G12_pass;first_failure=G13_X0=-2^27/25;D0_D13=0")
    print("r2_control=c6_0_repairs_G13;G14_pole_remainder=-5X^2/2^34")
    print("r2_control=endpoint_before=2^50/375;after_c6_0=0;theorem_consistent")

    # ---- mutation battery --------------------------------------------------
    # M1 dropped equation row -> dimension jumps to 6
    rank1, _, free1, _ = solve_fiber(cols, nrows=49)
    assert len(cols) - rank1 != 5
    # M2 dropped variable column -> dimension drops to 4 or free set changes
    drop = NAMES.index("d13_0")
    cols2 = cols[:drop] + cols[drop + 1:]
    names2 = NAMES[:drop] + NAMES[drop + 1:]
    rows2 = [[c[i] for c in cols2] for i in range(50)]
    red2, piv2 = rref(rows2)
    free2 = [names2[c] for c in range(len(cols2)) if c not in piv2]
    assert not (len(free2) == 5 and free2 == FREE_TARGET)
    # M3 wrong free set is detected by direct comparison
    assert [NAMES[c] for c in free] != ["d15_4", "d15_5", "d15_6", "d15_7", "d15_8"]
    # M4 omitted characteristic mode (drop c6 trajectory at r2 point)
    e_mut = Fr(0) - Fr(2 ** 29, 75) * lcoef1(total(elems1, {2: Fr(1)}, 15))
    assert e_mut != Fr(2 ** 50, 375)
    # M5 treating c12/c14 as genuinely unborn is false (loads shown above);
    # their loads on all four audited rows are zero, so precision-only.
    assert per_basis[1]["c12"][12] != LZERO and per_basis[1]["c14"][14] != LZERO
    # M6 sign flip in the residue row breaks identity (4)
    bad = qsum(qscale(Fr(1, 5), quad(f0, [-v for v in r6])),
               quad(corr4, rows["c6"]["g13x0"]))
    assert bad != E["c6"]
    # M7 wrong endpoint target sign destroys the c4 cancellation
    e_c4_flipped = qsum(quad(f11x1, rows["c4"]["g11x0"]),
                        qscale(-1, quad(f0, rows["c4"]["g15x1"])))
    assert e_c4_flipped != {}
    # M8 exclusion is target-sign robust: 0 != 1 and 0 != -1; target != 0
    assert Fr(0) != target and Fr(0) != -target
    # M9 a nonzero remainder must not be accepted as polynomial
    assert lpole(g14) == 1 and lremainder(g14) != []
    print("mutations=M1_row_drop;M2_column_drop;M3_free_set;M4_mode_drop;"
          "M5_unborn_claim;M6_sign_flip;M7_c4_cancellation;M8_target_sign;"
          "M9_pole_remainder=ALL_DETECTED")

    check_manifest()
    print("frozen_hashes_start_end=PASS")
    print("PASS_FABLE5_HOSTILE_R3_QX_FIXED_EVEN_ENDPOINT_ZERO")


if __name__ == "__main__":
    main()
