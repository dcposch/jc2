#!/usr/bin/env python3
"""Hostile Fable5 re-audit of the exact D16--D22 active-c2 literal tail.

Fully independent standard-library checker.  Nothing is imported from the
producer probe or the upstream extension checker; the polynomial backend,
the rational A-power arithmetic, the fractional-power series recurrence,
the characteristic mode ladder, the determinant rows, and the born-row
affine solver are all re-implemented here from the defining identities.

Representation choice (deliberately different from the producer's Laurent
dictionaries): every series coefficient is a reduced rational function
N(X)/A(X)^k with N a dense Q[X] polynomial and A=X^4-1, normalized so that
A does not divide N unless k=0.

Run:  PYTHONDONTWRITEBYTECODE=1 python3 -B <this file>
"""

from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

FROZEN = {
    "xmodel/ggv-upper-endpoint-active-c2-literal-d16-d22-tail-sol-ultra-20260828.md":
        "a4bfbb1437c0e67a8f55439d6b9bd6d0a60a70340d41e6481068cf148ad50a3c",
    "cases/ggv_8_28_upper_endpoint_active_c2_literal_d16_d22_probe_20260828/probe_literal_tail.py":
        "f3371687df3584bd1dbeac9e9ad05aca8212a6dd35b63c17209916ab9d11fb45",
    "cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/verify_active_c2_extension.py":
        "112650dc27b0e13d76979d5adca9315919ee65cb8d9eaf717c1685f99d96de26",
    "cases/ggv_8_28_upper_endpoint_branch_p_20260827/compile_endpoint.py":
        "7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1",
    "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json":
        "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0",
}

RAW_JSON = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_frozen_hashes(stage: str) -> None:
    for relative, expected in FROZEN.items():
        actual = sha256(ROOT / relative)
        assert actual == expected, (stage, relative, actual)


# ---------------------------------------------------------------------------
# Dense univariate polynomials over Q (list of coefficients, low degree first)
# ---------------------------------------------------------------------------

def trim(p):
    p = list(p)
    while p and not p[-1]:
        p.pop()
    return p


def padd(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0))
                 for i in range(n)])


def pscale(c, p):
    c = Q(c)
    return trim([c * v for v in p]) if c else []


def pmul(a, b):
    if not a or not b:
        return []
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return trim(out)


def ppow(a, n):
    out = [Q(1)]
    for _ in range(n):
        out = pmul(out, a)
    return out


def pder(p):
    return trim([Q(i) * p[i] for i in range(1, len(p))])


def pdivmod(a, b):
    b = trim(b)
    assert b
    r = trim(a)
    q = [Q(0)] * max(0, len(r) - len(b) + 1)
    while r and len(r) >= len(b):
        d = len(r) - len(b)
        c = r[-1] / b[-1]
        q[d] += c
        r = padd(r, pscale(-1, [Q(0)] * d + pscale(c, b)))
    return trim(q), trim(r)


A = trim([Q(-1), Q(0), Q(0), Q(0), Q(1)])
APRIME = pder(A)


# ---------------------------------------------------------------------------
# Reduced rational functions N/A^k, as (tuple(N), k)
# ---------------------------------------------------------------------------

def rat(num, k=0):
    num = trim(num)
    if not num:
        return ((), 0)
    while k > 0:
        q, r = pdivmod(num, A)
        if r:
            break
        num, k = q, k - 1
    assert k >= 0
    return (tuple(num), k)


def rat_poly(p):
    return rat(list(p), 0)


RZERO = ((), 0)


def rnum(x):
    return list(x[0])


def riszero(x):
    return not x[0]


def rispoly(x):
    return x[1] == 0


def radd(x, y):
    K = max(x[1], y[1])
    n = padd(pmul(rnum(x), ppow(A, K - x[1])), pmul(rnum(y), ppow(A, K - y[1])))
    return rat(n, K)


def rscale(c, x):
    return rat(pscale(c, rnum(x)), x[1])


def rmul(x, y):
    return rat(pmul(rnum(x), rnum(y)), x[1] + y[1])


def rneg(x):
    return rscale(-1, x)


def rder(x):
    n, k = rnum(x), x[1]
    if k == 0:
        return rat(pder(n), 0)
    return rat(padd(pmul(pder(n), A), pscale(-k, pmul(n, APRIME))), k + 1)


def rat_A_power(m):
    # A^m for integer m, possibly negative.
    if m >= 0:
        return rat(ppow(A, m), 0)
    return rat([Q(1)], -m)


# ---------------------------------------------------------------------------
# The literal specialized F (weights 0..22)
# ---------------------------------------------------------------------------

def build_F():
    one = [Q(1)]
    V0 = list(A)                      # V0 = A
    T = pscale(Q(-1, 4), A)           # T = -A/4
    Z = pscale(Q(1, 2), padd(one, pscale(-1, A)))     # Z = (1-A)/2
    R = [Q(-1)]                       # exact-D0 slice value entering F4
    F = {
        0: ppow(A, 4),
        1: pmul(ppow(A, 2), V0),                              # A^2*V0 = A^3
        2: pscale(Q(1, 4), padd(pmul(V0, V0), pmul(ppow(A, 2), Z))),
        3: pscale(Q(1, 8), padd(pmul(V0, Z), pmul(A, T))),
        4: pscale(Q(1, 64), padd(pmul(Z, Z), pmul(A, R))),    # (Z^2-A)/64
        5: pscale(Q(1, 512), padd(A, pscale(-1, one))),       # (A-1)/512
        6: [Q(1, 4096)],
    }
    for n in range(7, 23):
        F[n] = []
    # Cross-check the displayed closed forms in the frozen report.
    assert F[1] == ppow(A, 3)
    assert F[4] == pscale(Q(1, 64), padd(pmul(Z, Z), pscale(-1, A)))
    assert F[5] == pscale(Q(1, 512), padd(A, [Q(-1)]))
    return F, Z


F, ZPOLY = build_F()
FR = {n: rat_poly(F[n]) for n in F}
MAXW = 22

# Mode ladder: t^b F^((12-b)/8); base b=0, coefficient 1, exponent 3/2.
BIRTHS = list(range(2, 21, 2))
EXPONENT = {b: Q(12 - b, 8) for b in BIRTHS}
EXPONENT[0] = Q(3, 2)
# Independent confirmation of the upstream MODES table values.
assert [EXPONENT[b] for b in BIRTHS] == [
    Q(5, 4), Q(1), Q(3, 4), Q(1, 2), Q(1, 4), Q(0),
    Q(-1, 4), Q(-1, 2), Q(-3, 4), Q(-1)]


def fractional_series(e, W):
    """Coefficients y_n of F(t,X)^e from F*y_t = e*F_t*y, y_0=A^(4e)."""
    assert (4 * e).denominator == 1
    y = {0: rat_A_power(int(4 * e))}
    inv_A4 = rat([Q(1)], 4)
    for n in range(1, W + 1):
        s = RZERO
        for i in range(1, min(n, 6) + 1):
            if not F[i]:
                continue
            s = radd(s, rscale((e + 1) * i - n, rmul(FR[i], y[n - i])))
        y[n] = rscale(Q(1, n), rmul(s, inv_A4))
    return y


SER = {e: fractional_series(e, MAXW) for e in sorted(set(EXPONENT.values()))}


def verify_series_ode():
    """Re-verify F*y_t = e*F_t*y coefficientwise for every exponent."""
    for e, y in SER.items():
        for n in range(1, MAXW + 1):
            lhs = RZERO
            for i in range(0, min(n, 6) + 1):
                j = n - i
                lhs = radd(lhs, rscale(j, rmul(FR[i], y[j])))
                lhs = radd(lhs, rscale(-e * i, rmul(FR[i], y[j])))
            assert riszero(lhs), ("series ODE", e, n)


def mode_rows(b, e, W):
    """Determinant rows of the single mode t^b*F^e with series exponent e."""
    y = SER[e] if e in SER else fractional_series(e, W)
    rows = {}
    for n in range(W + 1):
        s = RZERO
        for i in range(0, min(n, 6) + 1):
            j = n - i
            if j < b:
                continue
            g = y[j - b]
            s = radd(s, rscale(12 - j, rmul(rat_poly(pder(F[i])), g)))
            s = radd(s, rscale(i - 8, rmul(FR[i], rder(g))))
        rows[n] = s
    return rows


def verify_mode_annihilation():
    """Each registered mode annihilates every determinant row through 22.

    This is the exact statement D(t^b F^e) = (12-8e-b) t^b F' F^e with
    12-8e-b=0 on the schedule; it certifies both the recurrence and the
    completeness of the exponent law e=(12-b)/8.
    """
    for b in [0] + BIRTHS:
        rows = mode_rows(b, EXPONENT[b], MAXW)
        for n in range(MAXW + 1):
            assert riszero(rows[n]), ("mode annihilation", b, n)
    # Sensitivity: a wrong exponent for the b=2 mode must NOT annihilate.
    bad = mode_rows(2, Q(1), 6)
    assert any(not riszero(bad[n]) for n in range(7)), "exponent mutation missed"


def char_row(n, modes):
    """Weight-n characteristic coefficient sum(c_b * t^b F^(e_b))_n."""
    s = SER[Q(3, 2)][n]
    for b in BIRTHS:
        c = modes.get(b, Q(0))
        if c and b <= n:
            s = radd(s, rscale(c, SER[EXPONENT[b]][n - b]))
    return s


def solve_born(base, m, name):
    """Unique scalar c with base + c*A^(-m) polynomial, or None.

    Writing base=N/A^K after clearing to K=max(k,m), the condition is
    A^K | N*A^(K-k) + c*A^(K-m); the remainder mod A^K is degree < 4K, and
    two distinct scalars c differ by (c-c')A^(-m) which is never polynomial
    for m>0, so any solution is automatically unique.
    """
    assert m > 0
    K = max(base[1], m)
    R0 = pdivmod(pmul(rnum(base), ppow(A, K - base[1])), ppow(A, K))[1]
    q, r = pdivmod(R0, ppow(A, K - m))
    if r or len(q) > 1:
        return None
    c = -q[0] if q else Q(0)
    solved = radd(base, rscale(c, rat_A_power(-m)))
    assert rispoly(solved), ("born solve verify", name)
    return c


def solve_linear_system(rows, rhs):
    """Exact Gaussian elimination; return a solution or None."""
    m = len(rows)
    aug = [list(map(Q, rows[i])) + [Q(rhs[i])] for i in range(m)]
    n = len(aug[0]) - 1
    pivots = []
    r = 0
    for col in range(n):
        piv = next((i for i in range(r, m) if aug[i][col]), None)
        if piv is None:
            continue
        aug[r], aug[piv] = aug[piv], aug[r]
        aug[r] = [v / aug[r][col] for v in aug[r]]
        for i in range(m):
            if i != r and aug[i][col]:
                f = aug[i][col]
                aug[i] = [a - f * b for a, b in zip(aug[i], aug[r])]
        pivots.append(col)
        r += 1
    for i in range(r, m):
        if aug[i][n]:
            return None
    x = [Q(0)] * n
    for i, col in enumerate(pivots):
        x[col] = aug[i][n]
    return x


def determinant_rows_poly(Fp, Gp, W):
    rows = {}
    for n in range(W + 1):
        s = []
        for i in range(n + 1):
            j = n - i
            fi = Fp.get(i, [])
            gj = Gp.get(j, [])
            s = padd(s, pscale(12 - j, pmul(pder(fi), gj)))
            s = padd(s, pscale(i - 8, pmul(fi, pder(gj))))
        rows[n] = s
    return rows


def L22(R, c40=40, c8=8):
    """Receiver operator: the (i=0,j=22) determinant contribution of G22=R.

    (12-22)*F0'*R + (0-8)*F0*R' = -10*(A^4)'*R - 8*A^4*R'
                                = -40*A^3*A'*R - 8*A^4*R'.
    """
    a3ap = rat_poly(pmul(ppow(A, 3), APRIME))
    a4 = rat_poly(ppow(A, 4))
    return radd(rscale(-c40, rmul(a3ap, R)), rscale(-c8, rmul(a4, rder(R))))


EXPECTED_WINDOWS = {
    "F": {1: (0, 15), 2: (0, 14), 3: (0, 13), 4: (0, 12), 5: (0, 11),
          6: (0, 10), 7: (0, 9), 8: (0, 8), 9: (1, 7), 10: (1, 6),
          11: (1, 5), 12: (2, 4), 13: (2, 3), 14: (2, 2)},
    "G": {1: (0, 23), 2: (0, 22), 3: (0, 21), 4: (0, 20), 5: (0, 19),
          6: (0, 18), 7: (0, 17), 8: (0, 16), 9: (0, 15), 10: (0, 14),
          11: (0, 13), 12: (0, 12), 13: (1, 11), 14: (1, 10), 15: (1, 9),
          16: (2, 8), 17: (2, 7), 18: (2, 6), 19: (3, 5), 20: (3, 4),
          21: (3, 3)},
}


def windows_match(census, expected):
    for kind in ("F", "G"):
        if set(census[kind]) != {str(w) for w in expected[kind]}:
            return False
        for w, (lo, hi) in expected[kind].items():
            rec = census[kind][str(w)]
            if (rec["lower"], rec["upper"]) != (lo, hi):
                return False
            if rec["dimension"] != hi - lo + 1 or len(rec["slots"]) != hi - lo + 1:
                return False
    return True


def in_window(poly, lo, hi):
    return all(lo <= d <= hi for d, c in enumerate(poly) if c)


def main():
    check_frozen_hashes("start")

    # ---- authoritative raw windows -------------------------------------
    raw = json.loads(RAW_JSON.read_text())
    assert raw["slotless"] == {
        "F_max_weight": 14, "G_max_weight": 21, "G22_present": False}
    assert raw["charged_rows"]["affine_target"] == {"row": 22, "value": 1}
    assert windows_match(raw["windows"], EXPECTED_WINDOWS)
    # No raw variable resembles an F15+ or G22 slot: every slot name in the
    # census is g_/f_ indexed by (X-degree, position); collect them all.
    slot_names = {s for kind in ("F", "G") for rec in raw["windows"][kind].values()
                  for s in rec["slots"]}
    extra = set(raw["variables"]) - slot_names
    assert all(v.startswith(("tt_", "z_")) for v in extra)
    assert len(raw["variables"]) == raw["variable_count"] == 303
    # Window-mutation sensitivity: a shifted G19 window must be rejected.
    mutated_windows = {k: dict(v) for k, v in EXPECTED_WINDOWS.items()}
    mutated_windows["G"] = dict(mutated_windows["G"])
    mutated_windows["G"][19] = (2, 5)
    assert not windows_match(raw["windows"], mutated_windows)

    # ---- series and mode ladder ----------------------------------------
    verify_series_ode()
    verify_mode_annihilation()

    # ---- frozen prefix point D0..D15 -----------------------------------
    C14 = Q(-6139, 17179869184)
    modes = {2: Q(1), 6: Q(1), 14: C14}
    # c14 is genuinely forced: the c14=0 base row 14 has a pole and the
    # unique polynomiality solution is the frozen value.
    base14 = char_row(14, {2: Q(1), 6: Q(1)})
    assert not rispoly(base14), "row 14 should be pole-obstructed before c14"
    assert solve_born(base14, 1, "c14") == C14

    raw_G = {}
    for n in range(16):
        g = char_row(n, modes)
        assert rispoly(g), ("prefix polynomiality", n)
        raw_G[n] = rnum(g)
        lo, hi = EXPECTED_WINDOWS["G"].get(n, (0, 24 - n))
        assert in_window(raw_G[n], 0 if n == 0 else lo, hi if n else 24), \
            ("prefix window", n)
    assert raw_G[0] == ppow(A, 6)
    assert raw_G[12] == [Q(4093, 268435456)]
    assert raw_G[13] == raw_G[14] == raw_G[15] == []

    raw_F = {n: F[n] for n in range(23)}
    for n in range(4, 15):
        lo, hi = EXPECTED_WINDOWS["F"][n]
        assert in_window(raw_F[n], lo, hi), ("F window", n)

    prefix_D = determinant_rows_poly(raw_F, raw_G, 15)
    assert all(not prefix_D[n] for n in range(16)), "prefix determinant"

    # ---- tail: born rows, windows, and G16..G21 ------------------------
    solved = {}
    for w in range(16, 22):
        if w in (16, 18, 20):
            base = char_row(w, modes)
            m = -int(4 * EXPONENT[w])          # mode enters as c*A^(-m)
            c = solve_born(base, m, f"c{w}")
            assert c is not None, f"c{w} unsolvable"
            modes[w] = c
            solved[w] = c
        g = char_row(w, modes)
        assert rispoly(g), ("tail polynomiality", w)
        lo, hi = EXPECTED_WINDOWS["G"][w]
        assert in_window(rnum(g), lo, hi), ("tail window", w)
        assert riszero(g), ("tail row must vanish identically", w)
        raw_G[w] = []
    assert solved == {16: Q(0), 18: Q(16369, 140737488355328), 20: Q(0)}

    # ---- weight-22 class and the absent receiver -----------------------
    g22 = char_row(22, modes)
    assert g22 == ((Q(9207, 144115188075855872),), 5), g22

    # Receiver operator: kernel is exactly the scalar line A^-5, because
    # L22(R)=0 is the first-order equation R'/R = -5*A'/A over Q(X).
    assert riszero(L22(rat([Q(1)], 5)))
    assert riszero(L22(g22))
    d22_raw_from_operator = rneg(L22(g22))
    assert riszero(d22_raw_from_operator)

    # ---- literal full determinant replay D0..D22 -----------------------
    raw_G[22] = []                      # no receiver slot exists
    full_D = determinant_rows_poly(raw_F, raw_G, 22)
    assert all(not full_D[n] for n in range(23)), "full determinant replay"
    assert full_D[22] == []             # homogeneous D22 = 0
    assert full_D[22] != [Q(1)]         # endpoint equation D22 = 1 FAILS
    # Structural identity: D22_char = D22_raw + L22(g22), all three zero.
    d22_char = radd(rat_poly(full_D[22]), L22(g22))
    assert riszero(d22_char)

    # ---- mutations ------------------------------------------------------
    failures = {}

    # (a) c18 = 0 leaves a genuine weight-18 pole.
    m1 = dict(modes)
    m1[18] = Q(0)
    r18 = char_row(18, m1)
    assert not rispoly(r18) and r18[1] > 0
    failures["c18_zero"] = f"row18 pole order {r18[1]}"

    # (b) wrong c18 (off by 2^-47) leaves a pole as well.
    m2 = dict(modes)
    m2[18] = modes[18] + Q(1, 140737488355328)
    assert not rispoly(char_row(18, m2))
    failures["c18_wrong"] = "row18 non-polynomial"

    # (c) dropping predecessor c6: the frozen c14 no longer clears row 14,
    #     and the re-solved value differs from the frozen one.
    m3 = dict(modes)
    m3[6] = Q(0)
    assert not rispoly(char_row(14, m3))
    resolved = solve_born(char_row(14, {2: Q(1)}), 1, "c14_no_c6")
    assert resolved is not None and resolved != C14
    failures["c6_dropped"] = f"row14 pole; re-solved c14={resolved}"

    # (d) dropping predecessor c14: rows 16+ lose their pole cancellation.
    m4 = dict(modes)
    m4[14] = Q(0)
    first_bad = next(w for w in range(14, 23)
                     if not rispoly(char_row(w, m4)))
    assert first_bad <= 18
    failures["c14_dropped"] = f"first non-polynomial row {first_bad}"

    # (e) receiver coefficient -40 -> -39: residual -k*A'/A^2 on the kernel.
    k22 = Q(9207, 144115188075855872)
    residual = rneg(L22(g22, c40=39))
    assert residual == rat(pscale(-k22, APRIME), 2) and not riszero(residual)
    failures["L22_minus39"] = "residual -k*A'/A^2 != 0"

    # (f) g22 mutations.  Sign and numerator mutations stay in the kernel
    #     (L22 still annihilates them) and are caught ONLY by the exact
    #     identity comparison with the recomputed g22; the denominator
    #     mutation A^-5 -> A^-4 is additionally caught by the operator.
    for tag, mutant in (
        ("sign", rat([-k22], 5)),
        ("numerator", rat([k22 + Q(1, 144115188075855872)], 5)),
    ):
        assert mutant != g22
        assert riszero(L22(mutant))     # kernel blindness, made explicit
        failures[f"g22_{tag}"] = "caught by identity comparison only"
    denom_mut = rat([k22], 4)
    assert denom_mut != g22 and not riszero(L22(denom_mut))
    assert rneg(L22(denom_mut)) == rat(pscale(8 * k22, APRIME), 1)
    failures["g22_denominator"] = "operator residual 8k*A'/A != 0"

    # ---- q1 status of the point (informational) ------------------------
    # V0 = A' * R0 + 2*A*R0' with deg R0 <= 4 is exactly solvable iff the
    # 8x5 linear system below is consistent; it is not (6*r1=1 vs -2*r1=-1).
    rows, rhs = [], []
    target = list(A)                    # V0 = A
    for d in range(8):
        row = []
        for i in range(5):
            c = Q(0)
            if 3 + i == d:
                c += Q(4)               # from A'=4X^3 times X^i
            if i >= 1 and 4 + i - 1 == d:
                c += Q(2 * i)           # from 2*X^4*R0'
            if i >= 1 and i - 1 == d:
                c += Q(-2 * i)          # from 2*(-1)*R0'
            row.append(c)
        rows.append(row)
        rhs.append(target[d] if d < len(target) else Q(0))
    assert solve_linear_system(rows, rhs) is None, "point unexpectedly q1"

    check_frozen_hashes("end")

    print(json.dumps({
        "status": "HOSTILE_TAIL_REVIEW_PASS",
        "solved_modes": {f"c{w}": str(c) for w, c in sorted(solved.items())},
        "resolved_c14": str(C14),
        "g22": "9207/144115188075855872 * A^-5",
        "G16_to_G21": "identically zero (windows vacuously satisfied)",
        "D_rows_zero": "D0..D21 and homogeneous D22",
        "endpoint_D22_equals_1": False,
        "L22": "-40*A^3*A'*R - 8*A^4*R'; kernel = Q * A^-5",
        "q1_representation_V0": "none with deg R0<=4 (system inconsistent)",
        "mutations_caught": failures,
    }, indent=2, sort_keys=True))
    print("PASS_HOSTILE_FABLE5_ACTIVE_C2_LITERAL_D16_D22_TAIL")


if __name__ == "__main__":
    main()
