#!/usr/bin/env python3
"""Independent hostile checker for the fixed proper-divisor D12 obstruction.

Fable 5 hostile review, 2026-08-28.  Pure standard library, exact Fraction
and Gaussian-rational arithmetic.  No campaign module is imported; every
polynomial routine here is written from scratch, so agreement with the
producer packet is a genuinely independent computation.

Verifies, for the frozen q1 proper-divisor D11 survivor:
  A. the predecessor is a legal raw point (windows, formulas, D0..D11=0,
     A=C*B, A does not divide W, q1 identity, gcd side conditions);
  B. the weight-12 characteristic recurrence (two independent routes),
     the polar reduction g12_char=Nred/(12*C^3*B^2), gcd(Nred,A)=1,
     Nred(1)=-12, the Bezout unit-mod-B certificate, and exact pole
     orders at every individual root of A (Gaussian rationals for +-i);
  C. the exact bridge  3*A*base = 2*A*N12' - 8*A'*N12,  equivalently
     base = 8*A^4*(g12_char)', so D12=0 forces
     G12 = g12_char + (3/2)*A^2*F12 + const  -- no polynomial G12 exists;
  D. the direct 28x16 system: slot inventory from RAW_INPUT, rank 12,
     augmented rank 13, four explicit null vectors, the dual functional
     20[X^0]+10[X^4]+4[X^8]+[X^12] killing all 16 legal columns with
     base pairing 11009739/16384, and the mod-4 support structure;
  E. byte-level agreement with the producer RESULT.json serializations;
  F. hostile mutations, each caught by a named check, plus two legal
     null-mutations that must NOT be caught.

Run:  python3 -B <this file>            (full suite + mutation matrix)
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
if (HERE / "cases").is_dir():
    ROOT = HERE
elif (HERE.parent / "cases").is_dir():
    ROOT = HERE.parent
else:
    ROOT = Path("/Users/dc/code/math/jc2")

CASE = ROOT / "cases/ggv_8_28_upper_endpoint_q1_post_d11_d12_obstruction_20260828"
PRED = ROOT / "cases/ggv_8_28_upper_endpoint_q1_post_d9_d11_survivor_20260828"
RAW_INPUT = ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json"

PINS = {
    CASE / "verify_q1_d12_obstruction.py":
        "24381cd505e9d507083c49f18c4eb45a3f55bee87446c2d0aa11a33b6fa203fb",
    CASE / "RESULT.json":
        "b2e0e3b9ed6ffb20328a044ae4172d0290597e5cbf088b62928ef480c24b4561",
    CASE / "TARGET.json":
        "02070d01044cdfe4c9f511d798abbd08e74d20bf28f4a98fd60d5c716cd6adb3",
    PRED / "verify_q1_post_d9_d11.py":
        "499d73d88df20c2404596f4402a46f0884b1d0703ff6e4016c8bba87a3f2e0ac",
    PRED / "RESULT.json":
        "d03a0fafdc2fde7f3e43ed53da3c631f4f3350c46dab1c1bda169de91a84eee0",
    RAW_INPUT:
        "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
}


class CheckFail(AssertionError):
    def __init__(self, name, detail=""):
        super().__init__(f"{name}: {detail}")
        self.name = name


def ensure(condition, name, detail=""):
    if not condition:
        raise CheckFail(name, detail)


# ---------------- exact polynomial layer (ascending Fraction lists) --------

def trim(p):
    p = list(p)
    while p and not p[-1]:
        p.pop()
    return p


def padd(*items):
    out = []
    for p in items:
        if len(p) > len(out):
            out += [Q(0)] * (len(p) - len(out))
        for i, c in enumerate(p):
            out[i] += c
    return trim(out)


def pscale(k, p):
    k = Q(k)
    return trim([k * c for c in p])


def pmul(a, b):
    if not a or not b:
        return []
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return trim(out)


def ppow(p, n):
    out = [Q(1)]
    for _ in range(n):
        out = pmul(out, p)
    return out


def pderiv(p):
    return trim([Q(i) * p[i] for i in range(1, len(p))])


def pdivmod(num, den):
    den = trim(den)
    assert den
    rem = trim(num)
    quo = [Q(0)] * max(0, len(rem) - len(den) + 1)
    while rem and len(rem) >= len(den):
        d = len(rem) - len(den)
        f = rem[-1] / den[-1]
        quo[d] += f
        rem = padd(rem, pscale(-f, [Q(0)] * d + den))
    return trim(quo), rem


def pmonic(p):
    p = trim(p)
    return pscale(1 / p[-1], p) if p else p


def pgcd(a, b):
    a, b = trim(a), trim(b)
    while b:
        a, b = b, pdivmod(a, b)[1]
    return pmonic(a)


def pxgcd(a, b):
    r0, r1 = trim(a), trim(b)
    s0, s1 = [Q(1)], []
    t0, t1 = [], [Q(1)]
    while r1:
        q, r = pdivmod(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, padd(s0, pscale(-1, pmul(q, s1)))
        t0, t1 = t1, padd(t0, pscale(-1, pmul(q, t1)))
    lead = r0[-1]
    return pscale(1 / lead, r0), pscale(1 / lead, s0), pscale(1 / lead, t0)


def peval(p, x):
    out = Q(0)
    for c in reversed(p):
        out = out * x + c
    return out


def geval(p, z):
    """Evaluate at a Gaussian rational z=(re,im); exact."""
    re, im = Q(0), Q(0)
    for c in reversed(p):
        re, im = re * z[0] - im * z[1] + c, re * z[1] + im * z[0]
    return (re, im)


def pencode(p):
    return {str(i): str(c) for i, c in enumerate(p) if c}


def pdecode(d):
    if not d:
        return []
    out = [Q(0)] * (max(map(int, d)) + 1)
    for k, v in d.items():
        out[int(k)] = Q(v)
    return trim(out)


def canonical_hash(obj):
    return hashlib.sha256(json.dumps(
        obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def rref_rank(matrix):
    work = [row[:] for row in matrix]
    rows, cols = len(work), len(work[0]) if matrix else 0
    rank = 0
    for col in range(cols):
        piv = next((r for r in range(rank, rows) if work[r][col]), None)
        if piv is None:
            continue
        work[rank], work[piv] = work[piv], work[rank]
        f = work[rank][col]
        work[rank] = [v / f for v in work[rank]]
        for r in range(rows):
            if r != rank and work[r][col]:
                g = work[r][col]
                work[r] = [a - g * b for a, b in zip(work[r], work[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


# ---------------- series helpers (weight expansion in s) -------------------

def series_mul(a, b, upto):
    """Coefficient lists of polynomials; a,b lists of poly; product through s^upto."""
    out = [[] for _ in range(upto + 1)]
    for i, p in enumerate(a):
        if i > upto or not p:
            continue
        for j, q in enumerate(b):
            if i + j > upto or not q:
                continue
            out[i + j] = padd(out[i + j], pmul(p, q))
    return out


# ---------------- the determinant operator --------------------------------

def determinant_row(F, G, weight, cF=12, cG=8):
    """D_w = sum_{i+j=w} (cF-j)*F_i'*G_j + (i-cG)*F_i*G_j'  (cF=12,cG=8)."""
    row = []
    for i in range(weight + 1):
        j = weight - i
        Fi = F[i] if i < len(F) else []
        Gj = G[j] if j < len(G) else []
        if not Fi or not Gj:
            continue
        row = padd(row,
                   pscale(cF - j, pmul(pderiv(Fi), Gj)),
                   pscale(i - cG, pmul(Fi, pderiv(Gj))))
    return row


# ---------------- main verification ----------------------------------------

def run(mutation=None):
    log = {}

    # -- pins --------------------------------------------------------------
    for path, want in PINS.items():
        got = hashlib.sha256(path.read_bytes()).hexdigest()
        ensure(got == want, "source_pins", f"{path.name}: {got}")

    prior = json.loads((PRED / "RESULT.json").read_text())
    fixed = prior["exact_rational_survivor"]
    result = json.loads((CASE / "RESULT.json").read_text())
    target_bytes = (CASE / "TARGET.json").read_bytes()

    # -- Stage A: predecessor is a legal raw point -------------------------
    X = [Q(0), Q(1)]
    A = pdecode(fixed["A"])
    B = pdecode(fixed["B"])
    C = pdecode(fixed["C"])
    V0 = pdecode(fixed["V0"])
    v1 = pdecode(fixed["V1"])
    u = pdecode(fixed["u"])
    Z = pdecode(fixed["Z"])
    T = pdecode(fixed["T"])
    W = pdecode(fixed["W"])

    ensure(A == padd(ppow(X, 4), [Q(-1)]), "A_is_X4_minus_1")
    ensure(C == padd(X, [Q(-1)]), "C_is_X_minus_1")
    ensure(B == [Q(1)] * 4, "B_is_1_X_X2_X3")
    ensure(pmul(C, B) == A, "A_equals_C_times_B")
    ensure(pgcd(A, pderiv(A)) == [Q(1)], "A_squarefree")
    ensure(W == B, "W_equals_B")
    qW, rW = pdivmod(W, A)
    ensure(qW == [] and rW == B and rW, "A_does_not_divide_W")
    ensure(V0 == padd(pmul(pderiv(A), C), pscale(2, pmul(A, pderiv(C)))),
           "q1_identity_V0")
    ensure(pmul(C, v1) == V0, "V0_equals_C_times_v")
    ensure(pgcd(B, v1) == [Q(1)], "gcd_B_v_is_1")
    ensure(pgcd(B, V0) == [Q(1)], "gcd_B_V0_is_1")
    ensure(pgcd(B, C) == [Q(1)], "gcd_B_C_is_1")
    ensure(pgcd(B, pderiv(B)) == [Q(1)], "B_squarefree")
    ensure(B == pmul([Q(1), Q(1)], [Q(1), Q(0), Q(1)]), "B_factorization")
    ensure(T == pmul(A, u) and u == [Q(-27, 16)] and Z == [Q(9, 2)],
           "T_u_Z_frozen_values")

    F = [pdecode(fixed["F"].get(str(w), {})) for w in range(12)]
    G = [pdecode(fixed["G"].get(str(w), {})) for w in range(12)]

    H = ppow(A, 2)
    ensure(F[0] == ppow(A, 4), "F0_is_A4")
    ensure(F[1] == pmul(H, V0), "F1_is_A2_V0")
    ensure(F[2] == pscale(Q(1, 4), padd(ppow(V0, 2), pmul(H, Z))), "F2_formula")
    ensure(F[3] == pscale(Q(1, 8), padd(pmul(V0, Z), pmul(A, T))), "F3_formula")
    ensure(F[4] == padd(pscale(Q(1, 16), pmul(V0, u)),
                        pscale(Q(1, 64), ppow(Z, 2)), pmul(A, W)), "F4_formula")
    f5 = [Q(1421, 2048), Q(5, 8), Q(7, 16), Q(9, 4), Q(-9, 16), Q(-3, 8), Q(-3, 16)]
    f6 = [Q(-16551, 65536), Q(-117, 512), Q(-45, 256), Q(-27, 256), Q(-27, 512), Q(-9, 512)]
    f7 = [Q(117, 8192), Q(-27, 2048), Q(-135, 4096), Q(-27, 2048), Q(-27, 8192)]
    ensure(F[5] == f5 and F[6] == f6 and F[7] == f7, "F5_F6_F7_frozen_lists")
    ensure(all(F[w] == [] for w in range(8, 12)), "F8_to_F11_zero")

    ensure(G[0] == ppow(A, 6), "G0_is_A6")
    ensure(G[11] == [], "G11_identically_zero")

    # characteristic identity G^2 = F^3 through weight 11 (route independent
    # of the producer's Euler/Miller recurrence); with G0=A^6 != 0 this pins
    # G1..G11 uniquely, so the frozen G *is* the truncated F^(3/2).
    G2 = series_mul(G, G, 11)
    F3 = series_mul(series_mul(F, F, 11), F, 11)
    for w in range(12):
        ensure(G2[w] == F3[w], "G_squared_equals_F_cubed", f"weight {w}")

    # raw windows from the authoritative inventory
    src = json.loads(RAW_INPUT.read_text())
    slots = src["raw_slots_through_weight_22"]
    ensure(sorted(slots) == ["F", "G"], "raw_kinds_F_G_only")
    windows = {"F": {}, "G": {}}
    slot_names = {"F": {}, "G": {}}
    for kind in windows:
        for rec in slots[kind]:
            w, d = int(rec["weight"]), int(rec["raw_exponents"]["x"])
            windows[kind].setdefault(w, set()).add(d)
            slot_names[kind].setdefault(w, {})[d] = rec["slot"]
            shift = 8 if kind == "F" else 12
            ensure(w == 3 * d - int(rec["raw_exponents"]["y"]) + shift,
                   "slot_weight_formula", rec["slot"])
    for w in range(12):
        for kind, series in (("F", F), ("G", G)):
            for d, c in enumerate(series[w]):
                ensure(not c or d in windows[kind][w],
                       "prefix_in_raw_windows", f"{kind}{w} X^{d}")

    for w in range(12):
        ensure(determinant_row(F, G, w) == [], "D0_D11_all_zero", f"D{w}")

    # -- Stage B: weight-12 characteristic certificate ---------------------
    # Euler route, derived from 2*F*(t dG/dt) = 3*(t dF/dt)*G with F_i at
    # t^(8-i), G_j at t^(12-j):  sum_{i+j=n} (3i-2j) F_i G_j = 0, so
    #   12*A^4*G12 = sum_{i=1..11} ((5/2)i-12) F_i G_(12-i)  + 18*A^6*F12.
    # First verify the same coefficient family ((5/2)i-n at weight n) at
    # every lower weight against the frozen G; this exercises the formula
    # at 66 (i,n) pairs where the fixture products are not degenerate.
    for n in range(1, 12):
        acc = []
        for i in range(1, n + 1):
            acc = padd(acc, pscale(Q(5 * i - 2 * n, 2), pmul(F[i], G[n - i])))
        ensure(acc == pscale(n, pmul(ppow(A, 4), G[n])),
               "euler_recurrence_all_weights", f"n={n}")

    # born mode at weight 12 per the frozen compiler's schedule: exponent 0,
    # i.e. c12*F^0 = c12, a constant inside the G12 window.
    modes = prior["symbolic_complete_rows"]["all_modes_retained"]
    ensure(modes.get("12") == "0", "born_mode_c12_exponent_zero")
    ensure(sorted(map(int, modes)) == list(range(2, 21, 2)),
           "mode_schedule_even_weights_2_to_20")

    N12 = []
    for i in range(1, 12):
        coeff = Q(5 * i - 24, 2) if mutation != "recurrence_sign" else Q(5 * i + 24, 2)
        N12 = padd(N12, pscale(coeff, pmul(F[i], G[12 - i])))
    A4 = ppow(A, 4)

    # quadratic route from G^2=F^3 at weight 12 (F12 excluded):
    #   2*A^6*G12 = (F^3)_12 - sum_{i=1..11} G_i G_(12-i)  + 3*A^8*F12.
    F3_12 = series_mul(series_mul(F, F, 12), F, 12)[12]
    quad = padd(F3_12, pscale(-1, series_mul(G, G, 12)[12]))
    ensure(pmul(N12, ppow(A, 2)) == pscale(6, quad),
           "euler_equals_quadratic_route")
    # F12 coefficient agreement: 18*A^6/(12*A^4) == 3*A^8/(2*A^6) == (3/2)*A^2.
    ensure(pscale(18, ppow(A, 6)) == pmul(pscale(Q(3, 2), ppow(A, 2)), pscale(12, A4)),
           "F12_regular_term_is_3half_A2")

    quotient, remainder = pdivmod(N12, A4)
    ensure(remainder != [], "N12_not_divisible_by_A4")
    common = pgcd(N12, A4)
    ensure(common == pmul(A, B), "gcd_N12_A4_is_AB")
    ensure(pmul(A, B) == pmul(C, ppow(B, 2)), "AB_equals_CB2")
    Nred = pdivmod(N12, common)[0]
    ensure(pdivmod(N12, common)[1] == [], "Nred_exact_division")
    ensure(pdivmod(A4, common)[0] == pmul(ppow(C, 3), ppow(B, 2)),
           "reduced_denominator_C3B2")
    ensure(pgcd(Nred, A) == [Q(1)], "gcd_Nred_A_is_1")
    ensure(peval(Nred, Q(1)) == Q(-12), "Nred_at_1_is_minus_12")
    ensure(peval(Nred, Q(-1)) == Q(-3969, 4096), "Nred_at_minus1")
    for root in ((Q(0), Q(1)), (Q(0), Q(-1))):
        ensure(geval(Nred, root) != (Q(0), Q(0)), "Nred_nonzero_at_pm_i")
        ensure(geval(C, root) != (Q(0), Q(0)), "C_nonzero_at_pm_i")
        ensure(geval(V0, root) != (Q(0), Q(0)), "V0_unit_at_pm_i")
    ensure(peval(V0, Q(-1)) == Q(8), "V0_at_minus1_is_8")
    ensure(peval(B, Q(1)) == Q(4) and peval(C, Q(-1)) == Q(-2),
           "B_C_cross_values")

    gB, sN, tB = pxgcd(Nred, B)
    ensure(gB == [Q(1)], "gcd_Nred_B_is_1")
    ensure(padd(pmul(sN, Nred), pmul(tB, B)) == [Q(1)], "my_bezout_identity")

    # -- Stage C: the exact bridge and the forced polar class --------------
    base = []
    for i in range(1, 12):
        j = 12 - i
        cF = 12 - j if mutation != "det_coeff_F_side" else 13 - j
        base = padd(base,
                    pscale(cF, pmul(pderiv(F[i]), G[j])),
                    pscale(i - 8, pmul(F[i], pderiv(G[j]))))
    # base = 8*A^4*(N12/(12*A^4))'  as rational functions, equivalently:
    bridge = padd(pscale(3, pmul(A, base)),
                  pscale(-2, pmul(A, pderiv(N12))),
                  pscale(8, pmul(pderiv(A), N12)))
    ensure(bridge == [], "bridge_base_equals_8A4_d_g12char")

    # F12 elimination identity: 12*(X^d)'*G0 + 4*X^d*G0' == 12*A^4*(A^2*X^d)'
    for d in range(0, 14):
        mono = [Q(0)] * d + [Q(1)]
        lhs = padd(pscale(12, pmul(pderiv(mono), G[0])),
                   pscale(4, pmul(mono, pderiv(G[0]))))
        rhs = pscale(12, pmul(A4, pderiv(pmul(ppow(A, 2), mono))))
        ensure(lhs == rhs, "F12_term_is_12A4_dA2F12", f"d={d}")

    # -- Stage D: direct 28x16 affine system -------------------------------
    ensure(sorted(windows["F"][12]) == [2, 3, 4], "F12_window_is_2_3_4")
    ensure(sorted(windows["G"][12]) == list(range(13)), "G12_window_is_0_to_12")
    ensure(len(windows["F"][12]) + len(windows["G"][12]) == 16,
           "sixteen_legal_slots")

    f12_degrees = sorted(windows["F"][12])
    g12_degrees = sorted(windows["G"][12])
    if mutation == "omit_slot_G12_X12":
        g12_degrees = g12_degrees[:-1]
    if mutation == "extra_slot_G12_X13":
        g12_degrees = g12_degrees + [13]

    columns, names = [], []
    g12_sign = Q(-8) if mutation != "det_sign_G12" else Q(8)
    f12_lead = Q(12) if mutation != "det_coeff_F12_col" else Q(11)
    for d in f12_degrees:
        mono = [Q(0)] * d + [Q(1)]
        columns.append(padd(pscale(f12_lead, pmul(pderiv(mono), G[0])),
                            pscale(4, pmul(mono, pderiv(G[0])))))
        names.append(f"F12_X{d}")
    for d in g12_degrees:
        mono = [Q(0)] * d + [Q(1)]
        columns.append(pscale(g12_sign, pmul(F[0], pderiv(mono))))
        names.append(f"G12_X{d}")

    ensure(len(columns) == 16, "column_count_16", str(len(columns)))
    ensure(columns[3] == [], "c12_column_G12_X0_is_zero")

    nrows = max([len(base)] + [len(col) for col in columns])
    ensure(nrows == 28, "coefficient_rows_28", str(nrows))
    matrix = [[col[r] if r < len(col) else Q(0) for col in columns]
              for r in range(nrows)]
    rhs = [-(base[r] if r < len(base) else Q(0)) for r in range(nrows)]
    rank = rref_rank(matrix)
    aug = rref_rank([row + [b] for row, b in zip(matrix, rhs)])
    ensure(rank == 12, "matrix_rank_12", str(rank))
    ensure(aug == 13, "augmented_rank_13", str(aug))
    ensure(aug == rank + 1, "system_infeasible_fredholm")

    # explicit nullspace: (F12=X^d, G12=(3/2)*A^2*X^d) for d=2,3,4 and G12=1.
    null_vectors = []
    for d in (2, 3, 4):
        vec = {f"F12_X{d}": Q(1)}
        comp = pscale(Q(3, 2), pmul(ppow(A, 2), [Q(0)] * d + [Q(1)]))
        ensure(len(comp) - 1 <= 12, "null_vector_G12_in_window", f"d={d}")
        for e, c in enumerate(comp):
            if c:
                vec[f"G12_X{e}"] = c
        null_vectors.append(vec)
    null_vectors.append({"G12_X0": Q(1)})
    for vec in null_vectors:
        image = []
        for name, coef in vec.items():
            col = columns[names.index(name)]
            image = padd(image, pscale(coef, col))
        ensure(image == [], "null_vectors_annihilate", json.dumps(
            {k: str(v) for k, v in vec.items()}))
    ensure(16 - rank == 4, "nullity_exactly_four")

    # dual functional
    dual = {0: Q(20), 4: Q(10), 8: Q(4), 12: Q(1)}
    if mutation == "dual_coeff_20_to_19":
        dual[0] = Q(19)

    def pair(dual_map, poly):
        return sum(c * (poly[d] if d < len(poly) else Q(0))
                   for d, c in dual_map.items())

    for name, col in zip(names, columns):
        ensure(pair(dual, col) == 0, "dual_kills_all_columns", name)
    base_pairing = pair(dual, base)
    ensure(base_pairing == Q(11009739, 16384), "dual_base_pairing_value",
           str(base_pairing))

    # mod-4 support structure: 13 of 16 columns never touch exponents
    # 0 mod 4; the three that do are G12_X1, G12_X5, G12_X9 = -8d*A^4*X^(d-1).
    touching = [name for name, col in zip(names, columns)
                if any(col[d] for d in range(0, len(col), 4))]
    ensure(touching == ["G12_X1", "G12_X5", "G12_X9"], "mod4_touching_columns",
           ",".join(touching))
    for d in (1, 5, 9):
        col = columns[names.index(f"G12_X{d}")]
        ensure(col == pscale(-8 * d, pmul(A4, [Q(0)] * (d - 1) + [Q(1)])),
               "G12_columns_are_scaled_A4_shifts", f"d={d}")
    ensure(pair(dual, pmul(A4, [Q(0)] * 12 + [Q(1)])) == Q(1),
           "dual_does_not_kill_A4_X12")

    # window sensitivity: the would-be illicit degree-13 G12 slot escapes
    # the dual functional, so the degree-12 window cap is load-bearing for
    # this particular certificate (though not for infeasibility itself,
    # which the bridge identity proves for unbounded polynomial G12).
    illicit = pscale(-8, pmul(F[0], pderiv([Q(0)] * 13 + [Q(1)])))
    ensure(pair(dual, illicit) == Q(-104), "illicit_X13_column_escapes_dual")

    # slot census against the packet serialization
    lit = result["literal_weight12_slots"]
    if mutation is None:
        ensure({int(k): v for k, v in lit["F"].items()} == slot_names["F"][12],
               "literal_F12_slot_names")
        ensure({int(k): v for k, v in lit["G"].items()} == slot_names["G"][12],
               "literal_G12_slot_names")
    ensure(len(f12_degrees) + len(g12_degrees) == 16,
           "slot_census_matches_RAW_INPUT",
           f"{len(f12_degrees)}+{len(g12_degrees)}")

    # -- Stage E: producer RESULT.json cross-validation --------------------
    if mutation is None:
        cc = result["characteristic_certificate"]
        ensure(pdecode(cc["recurrence_numerator"]) == N12, "result_N12_matches")
        ensure(cc["recurrence_numerator_sha256"] == canonical_hash(pencode(N12)),
               "result_N12_hash")
        ensure(pdecode(cc["division_quotient_mod_A4"]) == quotient,
               "result_quotient_matches")
        ensure(pdecode(cc["division_remainder_mod_A4"]) == remainder,
               "result_remainder_matches")
        ensure(cc["division_remainder_sha256"] == canonical_hash(pencode(remainder)),
               "result_remainder_hash")
        ensure(pdecode(cc["gcd_N12_A4"]) == common, "result_gcd_matches")
        ensure(pdecode(cc["reduced_numerator"]) == Nred, "result_Nred_matches")
        ensure(pdecode(cc["reduced_denominator_without_scalar_12"])
               == pmul(ppow(C, 3), ppow(B, 2)), "result_denominator_matches")
        ensure(cc["Nred_at_C_root_X1"] == "-12", "result_Nred_at_1")
        bz = cc["bezout_mod_B"]
        prod_s, prod_t = pdecode(bz["Nred_cofactor"]), pdecode(bz["B_cofactor"])
        ensure(padd(pmul(prod_s, Nred), pmul(prod_t, B)) == [Q(1)],
               "producer_bezout_identity_verifies")
        ensure(prod_s == sN and prod_t == tB, "bezout_cofactors_match_mine")

        dc = result["direct_raw_D12_certificate"]
        ensure(pdecode(dc["base_row"]) == base, "result_base_row_matches")
        ensure(dc["base_row_sha256"] == canonical_hash(pencode(base)),
               "result_base_row_hash")
        ensure((dc["coefficient_rows"], len(dc["variables"]),
                dc["matrix_rank"], dc["augmented_rank"])
               == (28, 16, 12, 13), "result_matrix_census")
        ensure(dc["variables"] == names, "result_variable_names")
        ensure(dc["homogeneous_nullity"] == 4, "result_nullity")
        ensure(Q(dc["dual_pairing_with_base"]) == base_pairing,
               "result_dual_pairing")
        ensure(dc["c12_G12_X0_column_is_zero"] is True, "result_c12_flag")

        mut = result["mutations"]["dual_weight_20_changed_to_19"]
        mut19 = dict(dual)
        mut19[0] = Q(19)
        nonzero = {name: str(pair(mut19, col))
                   for name, col in zip(names, columns) if pair(mut19, col)}
        ensure(mut["nonzero_new_column_pairings"] == nonzero,
               "result_mutated_dual_pairings", json.dumps(nonzero))
        ensure(nonzero == {"G12_X1": "8"}, "mutated_dual_hits_only_G12_X1")

        ensure(result["target_sha256"]
               == hashlib.sha256(target_bytes).hexdigest(), "target_hash_binds")
        ensure(result["status"]
               == "PASS_EXACT_Q1_D11_SURVIVOR_D12_OBSTRUCTION", "result_status")

        # legal null-mutations (must not trip anything):
        sample_f12 = [Q(0), Q(0), Q(1), Q(2), Q(3)]
        full = padd(N12, pscale(18, pmul(sample_f12, ppow(A, 6))))
        ensure(pdivmod(full, A4)[1] == remainder,
               "legal_F12_leaves_polar_remainder")
        ensure(columns[names.index("G12_X0")] == [],
               "legal_c12_has_zero_column")

    def gauss_str(z):
        return f"{z[0]}{'+' if z[1] >= 0 else ''}{z[1]}*i"

    log["rank"] = rank
    log["aug"] = aug
    log["base_pairing"] = str(base_pairing)
    log["N12_deg"] = len(N12) - 1
    log["Nred_deg"] = len(Nred) - 1
    log["quotient_deg"] = len(quotient) - 1
    log["base_deg"] = len(base) - 1
    log["Nred_at_i"] = gauss_str(geval(Nred, (Q(0), Q(1))))
    log["Nred_at_minus_i"] = gauss_str(geval(Nred, (Q(0), Q(-1))))
    log["Nred_at_minus_1"] = str(peval(Nred, Q(-1)))
    return log


MUTATIONS = {
    "det_sign_G12": {"null_vectors_annihilate"},
    "det_coeff_F12_col": {"null_vectors_annihilate"},
    "det_coeff_F_side": {"bridge_base_equals_8A4_d_g12char"},
    "recurrence_sign": {"euler_equals_quadratic_route"},
    "omit_slot_G12_X12": {"column_count_16", "slot_census_matches_RAW_INPUT"},
    "extra_slot_G12_X13": {"column_count_16", "slot_census_matches_RAW_INPUT"},
    "dual_coeff_20_to_19": {"dual_kills_all_columns"},
}


def main():
    log = run(None)
    print("CLEAN RUN OK:", json.dumps(log))
    matrix = {}
    failures = 0
    for name, acceptable in MUTATIONS.items():
        try:
            run(name)
        except CheckFail as fail:
            matrix[name] = fail.name
            status = ("DETECTED" if fail.name in acceptable
                      else "DETECTED_BY_OTHER_CHECK")
            print(f"mutation {name:22s} -> caught by {fail.name:40s} {status}")
        else:
            print(f"mutation {name:22s} -> NOT DETECTED (FAILURE)")
            failures += 1
    if failures:
        sys.exit(1)
    print("MUTATION MATRIX:", json.dumps(matrix))
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
