#!/usr/bin/env python3
"""Deterministic clean-room builder for the R4-00 CELL-R1 / CELL-R2 base-decide
AWS packets.

Everything is rebuilt from the two frozen sources

  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/
      output/compiled_v2/tails.json
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/
      compile_contracted_source_v20r2.py   (conventions only, never imported)

under the frozen V20R2 conventions (normalized coordinate map, load shifts
2/6/10, target rows -mu2/-mu4/-mu6/-(1/4)Jdet at shifts 14/16/18/19,
truncation Lambda^20).  The sealed producer report
xmodel/k00-r4-00-entry-solve-fable5-20260829.md is pinned and used only for
CROSS-CHECKS; no generator below is copied from it.

Exact stdlib arithmetic only.  Row expansion uses dyadic coefficients
(num, e) == num / 2^e -- every denominator in the frozen tails, coordinate
map and target rows is a power of two, asserted at load time.  Deterministic:
identical inputs give byte-identical packet output.

Full mode is a heavy exact computation and is intended for a registered AWS
host; --smoke runs the truncated generic build and entry checks only.
"""

from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TAILS_PATH = ROOT / ("cases/max12_812_order2_u2_62_strict_rees_20260825/"
                     "aws_compile_v2_jsat/run/output/compiled_v2/tails.json")
COMPILER_PATH = ROOT / ("cases/max12_812_order2_u2_62_k00_common_lambda19_"
                        "kuranishi_v20_20260827/compile_contracted_source_v20r2.py")
REPORT_PATH = ROOT / "xmodel/k00-r4-00-entry-solve-fable5-20260829.md"
EXPECTED = {
    TAILS_PATH: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    COMPILER_PATH: "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b",
    REPORT_PATH: "0ffc4f741eb2b6a8257dd90c47f194f950752150f57468d81a7779406ab60ed3",
}
EXPECTED_CANONICAL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
TAIL_WEIGHTS = [8, 7, 6, 5, 4, 3, 2, 2, 6, 10]
F0, F1 = F(0), F(1)
OUT = HERE / "packet"
PRIMES = [65521, 1048573, 2147483629]
T0 = time.time()


def note(msg: str) -> None:
    print(f"[{time.time()-T0:8.1f}s] {msg}", flush=True)


def fail(msg: object) -> None:
    raise RuntimeError(msg)


def digest_bytes(b: bytes) -> str:
    return sha256(b).hexdigest()


def digest(path: Path) -> str:
    return digest_bytes(path.read_bytes())


# ---------------------------------------------------------------- variables

VARS: list[str] = []
VIDX: dict[str, int] = {}
WEIGHT: dict[str, int] = {}


def newvar(name: str, weight: int) -> int:
    if name in VIDX:
        fail(("duplicate variable", name))
    VIDX[name] = len(VARS)
    VARS.append(name)
    WEIGHT[name] = weight
    return VIDX[name]


for nm, w in (("s", 4), ("t", 4), ("s1", 5), ("t1", 5), ("kappa", 2),
              ("az", 6), ("bz", 6), ("uz", 6), ("vz", 6), ("Az", 6), ("Bz", 6)):
    newvar(nm, w)
for m in range(7, 14):
    for p in ("a", "b", "u", "v", "A", "B"):
        newvar(f"{p}{m}", m)
for m in range(14, 20):
    for j in range(6):
        newvar(f"d{m}_{j}", m)
for j in range(1, 18):
    newvar(f"k10_{j}", 2 + j)
for j in range(1, 14):
    newvar(f"k6_{j}", 6 + j)
for j in range(1, 10):
    newvar(f"k2_{j}", 10 + j)
for j in range(1, 6):
    newvar(f"mu2_{j}", 14 + j)
for j in range(1, 4):
    newvar(f"mu4_{j}", 16 + j)
newvar("mu6_1", 19)
newvar("Jdet_0", 19)
NV = len(VARS)
WVEC = [WEIGHT[n] for n in VARS]


# ------------------------------------------------------ dyadic coefficients
# coefficient = (num, e) meaning num / 2^e, num odd or zero, canonical

def dy_norm(n: int, e: int):
    if n == 0:
        return (0, 0)
    while n % 2 == 0:
        n //= 2
        e -= 1
    return (n, e)


def dy_from_frac(c: F):
    den = c.denominator
    e = den.bit_length() - 1
    if (1 << e) != den:
        fail(("non-dyadic coefficient in row layer", c))
    return dy_norm(c.numerator, e)


def dy_to_frac(c) -> F:
    n, e = c
    return F(n, 1 << e) if e >= 0 else F(n * (1 << -e))


def dy_add(a, b):
    na, ea = a
    nb, eb = b
    if na == 0:
        return b
    if nb == 0:
        return a
    if ea == eb:
        return dy_norm(na + nb, ea)
    if ea > eb:
        return dy_norm(na + (nb << (ea - eb)), ea)
    return dy_norm((na << (eb - ea)) + nb, eb)


def dy_mul(a, b):
    na, ea = a
    nb, eb = b
    if na == 0 or nb == 0:
        return (0, 0)
    return (na * nb, ea + eb)  # odd*odd stays odd; no renormalization needed


DY0 = (0, 0)
DY1 = (1, 0)


# ------------------------------------------------------ sparse polynomials
# monomial = tuple of (var_index, exponent) pairs sorted by var_index
# poly = dict monomial -> dyadic coefficient

def mono_mul(m1, m2):
    if not m1:
        return m2
    if not m2:
        return m1
    d = dict(m1)
    for v, e in m2:
        d[v] = d.get(v, 0) + e
    return tuple(sorted(d.items()))


def padd(P, Q, sc=DY1):
    out = dict(P)
    if sc == DY1:
        for m, c in Q.items():
            c0 = out.get(m)
            nc = c if c0 is None else dy_add(c0, c)
            if nc[0]:
                out[m] = nc
            else:
                out.pop(m, None)
    else:
        for m, c in Q.items():
            c = dy_mul(sc, c)
            c0 = out.get(m)
            nc = c if c0 is None else dy_add(c0, c)
            if nc[0]:
                out[m] = nc
            else:
                out.pop(m, None)
    return out


def pmul(P, Q):
    out: dict = {}
    get = out.get
    for m1, c1 in P.items():
        for m2, c2 in Q.items():
            m = mono_mul(m1, m2)
            c = dy_mul(c1, c2)
            c0 = get(m)
            out[m] = c if c0 is None else dy_add(c0, c)
    return {m: c for m, c in out.items() if c[0]}


def pscale(P, c):
    if not c[0]:
        return {}
    return {m: dy_mul(v, c) for m, v in P.items()}


def pconst(c) -> dict:
    d = dy_from_frac(F(c))
    return {(): d} if d[0] else {}


def pvar(name: str) -> dict:
    return {((VIDX[name], 1),): DY1}


def plin(*terms) -> dict:
    out: dict = {}
    for c, name in terms:
        d = dy_from_frac(F(c))
        if d[0]:
            out = padd(out, {((VIDX[name], 1),): d})
    return out


def occ(P) -> set:
    return {v for m in P for v, _ in m}


def subzero(P, kill: set) -> dict:
    return {m: c for m, c in P.items() if not any(v in kill for v, _ in m)}


def split_var(P, name: str) -> dict:
    x = VIDX[name]
    out: dict = {}
    for m, c in P.items():
        d = 0
        rest = []
        for v, e in m:
            if v == x:
                d = e
            else:
                rest.append((v, e))
        out.setdefault(d, {})[tuple(rest)] = c
    return out


def to_frac_poly(P) -> dict:
    return {m: dy_to_frac(c) for m, c in P.items()}


def wdeg_check(P, w: int, label: str) -> None:
    for m in P:
        got = sum(e * WVEC[v] for v, e in m)
        if got != w:
            fail(("weighted homogeneity failure", label, w, got,
                  [(VARS[v], e) for v, e in m]))


def peval(P, val: list) -> F:
    """Exact evaluation of a Fraction-coefficient poly at Fraction values."""
    cache: dict = {}
    s = F0
    for m, c in P.items():
        prod = c
        for v, e in m:
            key = (v, e)
            pw = cache.get(key)
            if pw is None:
                pw = val[v] ** e
                cache[key] = pw
            prod *= pw
        s += prod
    return s


# ------------------------------------------------ Fraction-poly helpers
# (small-object cross-checks only; monomials as above, coefficients Fraction)

def fpadd(P, Q, sc=F1):
    out = dict(P)
    for m, c in Q.items():
        nc = out.get(m, F0) + sc * c
        if nc:
            out[m] = nc
        else:
            out.pop(m, None)
    return out


def fpmul(P, Q):
    out: dict = {}
    for m1, c1 in P.items():
        for m2, c2 in Q.items():
            m = mono_mul(m1, m2)
            out[m] = out.get(m, F0) + c1 * c2
    return {m: c for m, c in out.items() if c}


# ---------------------------------------------------------------- series

def series_zero(trunc: int):
    return [dict() for _ in range(trunc)]


def series_add(a, b, sc=DY1):
    return [padd(x, y, sc) for x, y in zip(a, b)]


def series_scale(a, c):
    return [pscale(x, c) for x in a]


def series_mul(a, b, trunc: int):
    out = series_zero(trunc)
    for i, x in enumerate(a):
        if not x:
            continue
        for j in range(trunc - i):
            y = b[j]
            if not y:
                continue
            out[i + j] = padd(out[i + j], pmul(x, y))
    return out


def series_pow(a, e: int, trunc: int):
    out = series_zero(trunc)
    out[0] = pconst(1)
    base = a
    while e:
        if e & 1:
            out = series_mul(out, base, trunc)
        e >>= 1
        if e:
            base = series_mul(base, base, trunc)
    return out


def series_shift(a, k: int, trunc: int):
    return [dict() for _ in range(min(k, trunc))] + a[:max(0, trunc - k)]


# ----------------------------------------------------------- frozen tails

def load_tails() -> dict:
    for path, expected in EXPECTED.items():
        got = digest(path)
        if got != expected:
            fail(("frozen input hash mismatch", str(path), got, expected))
    tails = json.loads(TAILS_PATH.read_text())
    if sorted(tails) != [str(i) for i in range(1, 8)]:
        fail(("tail key mismatch", sorted(tails)))
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if digest_bytes(canonical.encode()) != EXPECTED_CANONICAL_TAILS:
        fail("canonical tail semantic digest mismatch")
    census = 0
    for ell in range(1, 8):
        for raw_mono, raw_coeff in tails[str(ell)]:
            census += 1
            mono = [int(x) for x in raw_mono]
            if len(mono) != 10 or any(x < 0 for x in mono):
                fail(("malformed tail monomial", ell, mono))
            if sum(a * b for a, b in zip(mono, TAIL_WEIGHTS)) != 12 + ell:
                fail(("tail weight mismatch", ell, mono))
            if sum(mono[7:]) > 1 or any(x not in (0, 1) for x in mono[7:]):
                fail(("tail load nonlinearity", ell, mono))
            dy_from_frac(F(str(raw_coeff)))  # asserts dyadic
    if census != 569:
        fail(("tail census", census))
    return tails


# ------------------------------------------------- stratum series and rows

def adapted(m: int, solved: bool) -> list:
    a, b, u, v, A, B = (f"a{m}", f"b{m}", f"u{m}", f"v{m}", f"A{m}", f"B{m}")
    drop = solved and m == 7
    return [plin((2, b), (2, u)) if drop else plin((2, b), (2, u), (1, B)),
            plin((1, a)), plin((1, b)), plin((8, a), (1, v)),
            plin((1, b), (-1, u)),
            plin((16, a), (4, v)) if drop else plin((16, a), (4, v), (1, A))]


def ell_vec(sname: str, tname: str) -> list:
    return [plin((2, sname)), plin((F(1, 8), tname)), plin((1, sname)),
            plin((1, tname)), plin((1, sname)), plin((2, tname))]


def z_vec(solved: bool) -> list:
    return [plin((2, "bz"), (2, "uz")) if solved
            else plin((2, "bz"), (2, "uz"), (1, "Bz")),
            plin((1, "az")), plin((1, "bz")), plin((8, "az"), (1, "vz")),
            plin((1, "bz"), (-1, "uz")),
            plin((16, "az"), (4, "vz")) if solved
            else plin((16, "az"), (4, "vz"), (1, "Az"))]


def build_rows(tails: dict, trunc: int, solved: bool, target_sign: int = -1,
               k6_shift: int = 6, tail_mutation: tuple | None = None) -> list:
    """Seven Lambda-series rows on the R4-00 stratum.  With solved=True the
    forced entry/grade-14 zeros Az=Bz=A7=B7=0 are substituted at source."""
    dser = [series_zero(trunc) for _ in range(6)]
    ell4 = ell_vec("s", "t")
    ell5 = ell_vec("s1", "t1")
    z6 = z_vec(solved)
    for j in range(6):
        if 4 < trunc:
            dser[j][4] = ell4[j]
        if 5 < trunc:
            dser[j][5] = ell5[j]
        if 6 < trunc:
            dser[j][6] = z6[j]
        for m in range(7, 14):
            if m < trunc:
                dser[j][m] = adapted(m, solved)[j]
        for m in range(14, 20):
            if m < trunc:
                dser[j][m] = pvar(f"d{m}_{j}")
    one = series_zero(trunc); one[0] = pconst(1)
    k10 = series_zero(trunc); k10[0] = pvar("kappa")
    for j in range(1, 18):
        if j < trunc:
            k10[j] = pvar(f"k10_{j}")
    k6 = series_zero(trunc)
    for j in range(1, 14):
        if j < trunc:
            k6[j] = pvar(f"k6_{j}")
    k2 = series_zero(trunc)
    for j in range(1, 10):
        if j < trunc:
            k2[j] = pvar(f"k2_{j}")
    slots = [
        series_scale(series_add(one, dser[0]), dy_from_frac(F(1, 256))),
        dser[1],
        series_scale(series_add(one, dser[2]), dy_from_frac(F(1, 16))),
        dser[3],
        series_scale(series_add(series_scale(one, (3, 0)), dser[4]),
                     dy_from_frac(F(1, 8))),
        dser[5],
        one,
        series_shift(k10, 2, trunc),
        series_shift(k6, k6_shift, trunc),
        series_shift(k2, 10, trunc),
    ]
    cache: dict = {}
    rows = [series_zero(trunc) for _ in range(7)]
    for ell in range(1, 8):
        for tno, (raw_mono, raw_coeff) in enumerate(tails[str(ell)]):
            coeff = F(str(raw_coeff))
            if tail_mutation is not None and (ell, tno) == tail_mutation[:2]:
                coeff += tail_mutation[2]
            term = series_zero(trunc)
            term[0] = pconst(coeff)
            for idx, e in enumerate(int(x) for x in raw_mono):
                if not e:
                    continue
                key = (idx, e)
                if key not in cache:
                    cache[key] = series_pow(slots[idx], e, trunc)
                term = series_mul(term, cache[key], trunc)
            rows[ell - 1] = series_add(rows[ell - 1], term)
    mu2 = series_zero(trunc)
    for j in range(1, 6):
        if j < trunc:
            mu2[j] = pvar(f"mu2_{j}")
    mu4 = series_zero(trunc)
    for j in range(1, 4):
        if j < trunc:
            mu4[j] = pvar(f"mu4_{j}")
    mu6 = series_zero(trunc)
    if 1 < trunc:
        mu6[1] = pvar("mu6_1")
    jdet = series_zero(trunc); jdet[0] = pvar("Jdet_0")
    sgn = dy_from_frac(F(target_sign))
    rows[1] = series_add(rows[1], series_scale(series_shift(mu2, 14, trunc), sgn))
    rows[3] = series_add(rows[3], series_scale(series_shift(mu4, 16, trunc), sgn))
    rows[5] = series_add(rows[5], series_scale(series_shift(mu6, 18, trunc), sgn))
    rows[6] = series_add(rows[6], series_scale(series_shift(jdet, 19, trunc),
                                               dy_from_frac(F(target_sign, 4))))
    return rows


# ------------------------------------------------------- structural checks

REPORT_XCHECKS = {
    "I1@14": [(F(-3, 512), {"s": 1, "t": 1, "uz": 1}),
              (F(-15, 4096), {"s": 2, "t": 1, "kappa": 1}),
              (F(3, 1024), {"s": 2, "vz": 1}),
              (F(-3, 16), {"t": 2, "vz": 1}),
              (F(5, 64), {"t": 3, "kappa": 1}),
              (F(-5, 256), {"kappa": 1, "uz": 1, "vz": 1})],
    "I2@14": [(F(-3, 128), {"s": 1, "t": 1, "vz": 1}),
              (F(15, 1024), {"s": 1, "t": 2, "kappa": 1}),
              (F(-3, 16384), {"s": 2, "uz": 1}),
              (F(-5, 65536), {"s": 3, "kappa": 1}),
              (F(3, 256), {"t": 2, "uz": 1}),
              (F(5, 8192), {"kappa": 1, "uz": 2}),
              (F(-5, 128), {"kappa": 1, "vz": 2})],
    "c31@16": [(F(3, 16384), {"A8": 1, "B8": 1}),
               (F(5, 4096), {"kappa": 1, "uz": 1, "A8": 1}),
               (F(-5, 4096), {"kappa": 1, "vz": 1, "B8": 1}),
               (F(-3, 8192), {"s": 1, "t": 1, "B8": 1}),
               (F(-3, 16384), {"s": 2, "A8": 1}),
               (F(3, 256), {"t": 2, "A8": 1}),
               (F(-3, 128), {"s": 1, "t": 3}),
               (F(3, 8192), {"s": 3, "t": 1}),
               (F(3, 1024), {"s": 1, "uz": 1, "vz": 1}),
               (F(-3, 2048), {"t": 1, "uz": 2}),
               (F(3, 32), {"t": 1, "vz": 2}),
               (F(-15, 4096), {"s": 1, "t": 1, "kappa": 1, "uz": 1}),
               (F(15, 8192), {"s": 2, "kappa": 1, "vz": 1}),
               (F(-15, 128), {"t": 2, "kappa": 1, "vz": 1})],
    "row4@16": [(F(-3, 8192), {"A8": 2}),
                (F(3, 524288), {"B8": 2}),
                (F(5, 1024), {"kappa": 1, "vz": 1, "A8": 1}),
                (F(5, 65536), {"kappa": 1, "uz": 1, "B8": 1}),
                (F(3, 2048), {"s": 1, "t": 1, "A8": 1}),
                (F(-3, 262144), {"s": 2, "B8": 1}),
                (F(3, 4096), {"t": 2, "B8": 1}),
                (F(-9, 4096), {"s": 2, "t": 2}),
                (F(3, 524288), {"s": 4}),
                (F(3, 128), {"t": 4}),
                (F(-3, 32768), {"s": 1, "uz": 2}),
                (F(3, 512), {"s": 1, "vz": 2}),
                (F(-3, 256), {"t": 1, "uz": 1, "vz": 1}),
                (F(-15, 1024), {"s": 1, "t": 1, "kappa": 1, "vz": 1}),
                (F(-15, 131072), {"s": 2, "kappa": 1, "uz": 1}),
                (F(15, 2048), {"t": 2, "kappa": 1, "uz": 1})],
}

REPORT_DA8 = [
    (F(-250, 9), {"s": 1, "t": 1, "kappa": 3, "p": 1}),
    (F(2), {"s": 1, "t": 1, "p": 2}), (F(128), {"s": 1, "t": 1, "q": 2}),
    (F(-480), {"s": 1, "t": 2, "kappa": 1, "q": 1}),
    (F(-15, 2), {"s": 2, "t": 1, "kappa": 1, "p": 1}),
    (F(125, 9), {"s": 2, "kappa": 3, "q": 1}),
    (F(5, 2), {"s": 3, "kappa": 1, "q": 1}),
    (F(50, 9), {"t": 1, "kappa": 2, "p": 2}),
    (F(3200, 9), {"t": 1, "kappa": 2, "q": 2}),
    (F(-8000, 9), {"t": 2, "kappa": 3, "q": 1}),
    (F(160), {"t": 3, "kappa": 1, "p": 1}),
    (F(-5, 9), {"kappa": 1, "p": 2, "q": 1}),
    (F(-320, 9), {"kappa": 1, "q": 3}),
]
REPORT_DB8 = [
    (F(-16000, 9), {"s": 1, "t": 1, "kappa": 3, "q": 1}),
    (F(480), {"s": 1, "t": 2, "kappa": 1, "p": 1}),
    (F(50, 9), {"s": 1, "kappa": 2, "p": 2}),
    (F(3200, 9), {"s": 1, "kappa": 2, "q": 2}),
    (F(-480), {"s": 2, "t": 1, "kappa": 1, "q": 1}),
    (F(-125, 9), {"s": 2, "kappa": 3, "p": 1}),
    (F(1), {"s": 2, "p": 2}), (F(64), {"s": 2, "q": 2}),
    (F(-5, 2), {"s": 3, "kappa": 1, "p": 1}),
    (F(8000, 9), {"t": 2, "kappa": 3, "p": 1}),
    (F(-64), {"t": 2, "p": 2}), (F(-4096), {"t": 2, "q": 2}),
    (F(10240), {"t": 3, "kappa": 1, "q": 1}),
    (F(-320, 9), {"kappa": 1, "p": 1, "q": 2}),
    (F(-5, 9), {"kappa": 1, "p": 3}),
]


def termlist_fpoly(terms) -> dict:
    out: dict = {}
    for c, mono in terms:
        m = tuple(sorted((VIDX[n], e) for n, e in mono.items()))
        out[m] = out.get(m, F0) + c
    return {m: c for m, c in out.items() if c}


def p_of() -> dict:
    return padd(pscale(pvar("uz"), (3, -1)), pmul(pvar("kappa"), pvar("s")),
                (5, 0))


def q_of() -> dict:
    return padd(pscale(pvar("vz"), (-3, -1)), pmul(pvar("kappa"), pvar("t")),
                (5, 0))


def tsplit(P, m):
    top = {VIDX[f"A{m}"], VIDX[f"B{m}"]}
    tpart, rest = {}, {}
    for mo, c in P.items():
        (tpart if any(v in top for v, _ in mo) else rest)[mo] = c
    return tpart, rest


def t_pattern_checks(P_list, n, check) -> None:
    """Verify the single-matrix T-ladder at grade n on the given rows."""
    m = n - 6
    p_pol, q_pol = p_of(), q_of()
    pat1 = pscale(padd(pmul(p_pol, pvar(f"A{m}")), pmul(q_pol, pvar(f"B{m}"))),
                  dy_from_frac(F(1, 2048)))
    pat2 = pscale(padd(pscale(pmul(q_pol, pvar(f"A{m}")), (-1, -2)),
                       pmul(p_pol, pvar(f"B{m}")), dy_from_frac(F(1, 16))),
                  dy_from_frac(F(1, 2048)))
    for i in range(7):
        tpart, rest = tsplit(P_list[i], m)
        if i == 0:
            check(tpart == pat1, f"T:G1@{n}")
        elif i == 1:
            check(tpart == pat2, f"T:G2@{n}")
        elif i in (2, 4, 6):
            sc = {2: F(-1, 8), 4: F(-1, 128), 6: F(-1, 1024)}[i]
            check(tpart == pscale(pat1, dy_from_frac(sc)), f"T:G{i+1}@{n}")
        else:
            check(not tpart, f"T:G{i+1}@{n} empty")
        newer = set()
        for mm in range(m + 1, 14):
            newer |= {VIDX[f"A{mm}"], VIDX[f"B{mm}"]}
        cone_top = ({VIDX[f"{pfx}{m}"] for pfx in ("a", "b", "u", "v")}
                    if m <= 13 else set())
        check(not (occ(rest) & (newer | cone_top)), f"T:G{i+1}@{n} rest vars")


def make_checker(strict: bool, findings: dict):
    def check(cond: bool, label: str) -> bool:
        if not cond:
            findings["failures"].append(label)
            if strict:
                fail(("structural check failed", label))
        return cond
    return check


def structural_generic(rows_g, trunc16: int, strict=True) -> dict:
    """Entry-block checks on the generic (Az,Bz,A7,B7 symbolic) build,
    truncated at Lambda^16."""
    findings: dict = {"failures": []}
    check = make_checker(strict, findings)
    for i in range(7):
        for n in range(trunc16):
            wdeg_check(rows_g[i][n], n, f"G{i+1}@{n}")
    # CHECK-A: grades 0..11 vanish identically on the stratum
    for i in range(7):
        for n in range(12):
            check(not rows_g[i][n], f"A:G{i+1}@{n}=0")
    # CHECK-B: grade-12 entry system and certificates
    g12 = [rows_g[i][12] for i in range(7)]
    allowed12 = {VIDX[n] for n in ("s", "t", "kappa", "uz", "vz", "Az", "Bz")}
    for i in range(7):
        check(occ(g12[i]) <= allowed12, f"B:G{i+1}@12 vars")
    AzBz = pmul(pvar("Az"), pvar("Bz"))
    check(padd(g12[2], g12[0], dy_from_frac(F(1, 8)))
          == pscale(AzBz, dy_from_frac(F(3, 16384))), "B:c31@12")
    check(padd(g12[4], g12[0], dy_from_frac(F(1, 128)))
          == pscale(AzBz, dy_from_frac(F(-3, 131072))), "B:c51@12")
    check(padd(g12[6], g12[0], dy_from_frac(F(1, 1024)))
          == pscale(AzBz, dy_from_frac(F(-3, 2097152))), "B:c71@12")
    pure4 = padd(pscale(pmul(pvar("Bz"), pvar("Bz")), dy_from_frac(F(3, 524288))),
                 pmul(pvar("Az"), pvar("Az")), dy_from_frac(F(-3, 8192)))
    check(g12[3] == pure4, "B:row4@12")
    check(not g12[5], "B:row6@12=0")
    for i in range(7):
        check(not subzero(g12[i], {VIDX["Az"], VIDX["Bz"]}),
              f"B:G{i+1}@12 in (Az,Bz)")
    if findings["failures"] and not strict:
        return findings
    # cone-killed rows for the T/entry checks
    kill_z = {VIDX["Az"], VIDX["Bz"]}
    rcone = [[subzero(rows_g[i][n], kill_z) for n in range(trunc16)]
             for i in range(7)]
    for n in (13, 14, 15):
        t_pattern_checks([rcone[i][n] for i in range(7)], n, check)
    # CHECK-D: grade 13 exactness
    for i in range(7):
        check(not tsplit(rcone[i][13], 7)[1], f"D:G{i+1}@13 rest=0")
    # CHECK-E: grade-14 combos are the pure (A7,B7) pair
    A7B7 = pmul(pvar("A7"), pvar("B7"))
    check(padd(rcone[2][14], rcone[0][14], dy_from_frac(F(1, 8)))
          == pscale(A7B7, dy_from_frac(F(3, 16384))), "E:c31@14 pure")
    check(padd(rcone[4][14], rcone[0][14], dy_from_frac(F(1, 128)))
          == pscale(A7B7, dy_from_frac(F(-3, 131072))), "E:c51@14 pure")
    check(padd(rcone[6][14], rcone[0][14], dy_from_frac(F(1, 1024)))
          == pscale(A7B7, dy_from_frac(F(-3, 2097152))), "E:c71@14 pure")
    pure4b = padd(pscale(pmul(pvar("B7"), pvar("B7")), dy_from_frac(F(3, 524288))),
                  pmul(pvar("A7"), pvar("A7")), dy_from_frac(F(-3, 8192)))
    check(rcone[3][14] == pure4b, "E:row4@14 pure")
    check(not rcone[5][14], "E:row6@14=0")
    # CHECK-E2: target arrival -mu2_1 in row 2 at grade 15
    sp = split_var(rows_g[1][15], "mu2_1")
    check(sorted(sp) == [0, 1] and sp[1] == {(): (-1, 0)},
          "E2:row2@15 target -mu2_1")
    return findings


def structural_solved(rows_s, trunc: int, strict=True) -> dict:
    """Window checks on the solved-stratum build (Az=Bz=A7=B7=0 at source)."""
    findings: dict = {"failures": []}
    check = make_checker(strict, findings)
    for i in range(7):
        for n in range(trunc):
            wdeg_check(rows_s[i][n], n, f"S:G{i+1}@{n}")
    for i in range(7):
        for n in range(14):
            check(not rows_s[i][n], f"S:G{i+1}@{n}=0")
    for n in range(14, trunc):
        t_pattern_checks([rows_s[i][n] for i in range(7)], n, check)
    base_ids = {VIDX[n] for n in ("s", "t", "uz", "vz", "kappa")}
    i1_14 = tsplit(rows_s[0][14], 8)[1]
    i2_14 = tsplit(rows_s[1][14], 8)[1]
    check(occ(i1_14) <= base_ids, "F:I1@14 base")
    check(occ(i2_14) <= base_ids, "F:I2@14 base")
    check(to_frac_poly(i1_14) == termlist_fpoly(REPORT_XCHECKS["I1@14"]),
          "F:I1@14 report-crosscheck")
    check(to_frac_poly(i2_14) == termlist_fpoly(REPORT_XCHECKS["I2@14"]),
          "F:I2@14 report-crosscheck")
    findings["I1@14"] = i1_14
    findings["I2@14"] = i2_14
    # grade-15 combos vanish identically
    for lbl, idx, c in (("c31", 2, F(1, 8)), ("c51", 4, F(1, 128)),
                        ("c71", 6, F(1, 1024))):
        check(not padd(rows_s[idx][15], rows_s[0][15], dy_from_frac(c)),
              f"G:{lbl}@15=0")
    check(not rows_s[3][15], "G:row4@15=0")
    check(not rows_s[5][15], "G:row6@15=0")
    combo: dict = {}
    for n in range(16, trunc):
        combo[("c31", n)] = padd(rows_s[2][n], rows_s[0][n], dy_from_frac(F(1, 8)))
        combo[("c51", n)] = padd(rows_s[4][n], rows_s[0][n], dy_from_frac(F(1, 128)))
        combo[("c71", n)] = padd(rows_s[6][n], rows_s[0][n], dy_from_frac(F(1, 1024)))
        combo[("D51", n)] = padd(combo[("c51", n)], combo[("c31", n)],
                                 dy_from_frac(F(1, 8)))
        combo[("D71", n)] = padd(combo[("c71", n)], combo[("c31", n)],
                                 dy_from_frac(F(1, 128)))
    findings["combo"] = combo
    closed16 = base_ids | {VIDX["A8"], VIDX["B8"]}
    check(occ(combo[("c31", 16)]) <= closed16, "H:c31@16 vars")
    check(occ(rows_s[3][16]) <= closed16, "H:row4@16 vars")
    check(not combo[("D51", 16)], "H:c51@16=-c31/8")
    check(not combo[("D71", 16)], "H:c71@16=-c31/128")
    check(not rows_s[5][16], "H:row6@16=0")
    check(to_frac_poly(combo[("c31", 16)]) == termlist_fpoly(REPORT_XCHECKS["c31@16"]),
          "H:c31@16 report-crosscheck")
    check(to_frac_poly(rows_s[3][16]) == termlist_fpoly(REPORT_XCHECKS["row4@16"]),
          "H:row4@16 report-crosscheck")
    if trunc <= 17:
        return findings
    check(not combo[("D51", 17)], "I:c51@17=-c31/8")
    check(not combo[("D71", 17)], "I:c71@17=-c31/128")
    check(not rows_s[5][17], "I:row6@17=0")
    sp = split_var(rows_s[3][17], "mu4_1")
    check(sorted(sp) == [0, 1] and sp[1] == {(): (-1, 0)}, "I:row4@17 defines mu4_1")
    check(occ(rows_s[5][18]) <= closed16, "J:row6@18 vars")
    check(occ(combo[("D51", 18)]) <= closed16, "J:D51@18 vars")
    check(occ(combo[("D71", 18)]) <= closed16, "J:D71@18 vars")
    check(len(rows_s[5][18]) == 21, "J:row6@18 21 terms")
    check(len(combo[("D51", 18)]) == 19, "J:D51@18 19 terms")
    check(len(combo[("D71", 18)]) == 18, "J:D71@18 18 terms")
    sp = split_var(rows_s[3][18], "mu4_2")
    check(sorted(sp) == [0, 1] and sp[1] == {(): (-1, 0)}, "J:row4@18 defines mu4_2")
    sp = split_var(rows_s[3][19], "mu4_3")
    check(sorted(sp) == [0, 1] and sp[1] == {(): (-1, 0)}, "K:row4@19 defines mu4_3")
    sp = split_var(rows_s[5][19], "mu6_1")
    check(sorted(sp) == [0, 1] and sp[1] == {(): (-1, 0)}, "K:row6@19 defines mu6_1")
    sp = split_var(combo[("D71", 19)], "Jdet_0")
    check(sorted(sp) == [0, 1] and sp[1] == {(): (-1, 2)}, "K:D71@19 defines Jdet_0")
    window_occ: set = set()
    for i in range(7):
        for n in range(8, trunc):
            window_occ |= occ(rows_s[i][n])
    findings["window_occurrence"] = sorted(VARS[v] for v in window_occ)
    absent = sorted(set(VARS) - {VARS[v] for v in window_occ}
                    - {"Az", "Bz", "A7", "B7"})
    findings["window_absent"] = absent
    forbidden = ([f"d{m}_{j}" for m in range(14, 20) for j in range(6)]
                 + [f"k10_{j}" for j in range(10, 18)]
                 + [f"k6_{j}" for j in range(10, 14)]
                 + [f"k2_{j}" for j in range(6, 10)])
    leaking = sorted(n for n in forbidden if VIDX[n] in window_occ)
    check(not leaking, f"L:beyond-serialization columns occur {leaking}")
    for tname, where in [("mu2_1", (1, 15)), ("mu2_2", (1, 16)), ("mu2_3", (1, 17)),
                         ("mu2_4", (1, 18)), ("mu2_5", (1, 19)), ("mu4_1", (3, 17)),
                         ("mu4_2", (3, 18)), ("mu4_3", (3, 19)), ("mu6_1", (5, 19)),
                         ("Jdet_0", (6, 19))]:
        sites = [(i, n) for i in range(7) for n in range(8, trunc)
                 if VIDX[tname] in occ(rows_s[i][n])]
        check(sites == [where], f"K:{tname} single site {sites}")
        spl = split_var(rows_s[where[0]][where[1]], tname)
        cexp = (-1, 2) if tname == "Jdet_0" else (-1, 0)
        check(sorted(spl) == [0, 1] and spl[1] == {(): cexp},
              f"K:{tname} linear coeff")
    findings["rows_solved"] = rows_s
    return findings


# ---------------------------------------------------- CELL-R2 derivation

def derive_r2(findings) -> dict:
    p_pol, q_pol = p_of(), q_of()
    D_pol = padd(pmul(p_pol, p_pol), pmul(q_pol, q_pol), (1, -6))
    i1, i2 = findings["I1@14"], findings["I2@14"]
    combo = findings["combo"]
    rows_s = findings["rows_solved"]
    ahat = pscale(padd(pmul(p_pol, i1), pmul(q_pol, i2), (-1, -4)), (-1, -11))
    bhat = pscale(padd(pscale(pmul(q_pol, i1), (1, -6)), pmul(p_pol, i2), (1, -4)),
                  (-1, -11))
    lhs1 = padd(pscale(padd(pmul(p_pol, ahat), pmul(q_pol, bhat)),
                       dy_from_frac(F(1, 2048))), pmul(D_pol, i1))
    lhs2 = padd(pscale(padd(pscale(pmul(q_pol, ahat), (-1, -2)),
                            pmul(p_pol, bhat), dy_from_frac(F(1, 16))),
                       dy_from_frac(F(1, 2048))), pmul(D_pol, i2))
    if lhs1 or lhs2:
        fail("R2 solve identity failed")
    # report cross-check of the shifted-coordinate display of D*A8, D*B8
    pf = to_frac_poly(p_pol)
    qf = to_frac_poly(q_pol)
    for hat, disp, lbl in ((ahat, REPORT_DA8, "DA8"), (bhat, REPORT_DB8, "DB8")):
        acc: dict = {}
        cachepow: dict = {}
        for c, mono in disp:
            term = {(): c}
            for nm, e in mono.items():
                base = pf if nm == "p" else qf if nm == "q" else {
                    ((VIDX[nm], 1),): F1}
                key = (nm, e)
                if key not in cachepow:
                    pw = {(): F1}
                    for _ in range(e):
                        pw = fpmul(pw, base)
                    cachepow[key] = pw
                term = fpmul(term, cachepow[key])
            acc = fpadd(acc, term)
        if acc != to_frac_poly(hat):
            fail(f"R2 {lbl} report-crosscheck failed")

    def substitute(P, label: str) -> dict:
        sp = split_var(P, "A8")
        out: dict = {}
        for da, Pa in sp.items():
            for db, Pb in split_var(Pa, "B8").items():
                if da + db > 2:
                    fail((label, "degree>2 in (A8,B8)"))
                piece = Pb
                for _ in range(da):
                    piece = pmul(piece, ahat)
                for _ in range(db):
                    piece = pmul(piece, bhat)
                for _ in range(2 - da - db):
                    piece = pmul(piece, D_pol)
                out = padd(out, piece)
        return out

    X = {
        "X1": substitute(combo[("c31", 16)], "c31@16"),
        "X2": substitute(rows_s[3][16], "row4@16"),
        "X3": substitute(rows_s[5][18], "row6@18"),
        "X4": substitute(combo[("D51", 18)], "D51@18"),
        "X5": substitute(combo[("D71", 18)], "D71@18"),
    }
    base_ids = {VIDX[n] for n in ("s", "t", "uz", "vz", "kappa")}
    for k, v in X.items():
        if not v:
            fail((k, "vanished identically"))
        if not occ(v) <= base_ids:
            fail((k, "non-base variable"))
        wdeg_check(v, 40 if k in ("X1", "X2") else 42, k)
    return {"X": X, "Ahat8": ahat, "Bhat8": bhat, "D": D_pol}


# ---------------------------------------------------- CELL-R1 derivation

R1VARS = ["s", "t", "kappa", "q", "A8", "B8"]
R1IDX = {n: i for i, n in enumerate(R1VARS)}
R1WEIGHT = {"s": 4, "t": 4, "kappa": 2, "q": 6, "A8": 8, "B8": 8}


def gadd(P, Q, sc=(F1, F0)):
    out = dict(P)
    a, b = sc
    for m, (x, y) in Q.items():
        nx, ny = a * x - b * y, a * y + b * x
        ox, oy = out.get(m, (F0, F0))
        rx, ry = ox + nx, oy + ny
        if rx or ry:
            out[m] = (rx, ry)
        else:
            out.pop(m, None)
    return out


def gmul(P, Q):
    out: dict = {}
    for m1, (a, b) in P.items():
        for m2, (c, d) in Q.items():
            m = mono_mul(m1, m2)
            x, y = a * c - b * d, a * d + b * c
            ox, oy = out.get(m, (F0, F0))
            out[m] = (ox + x, oy + y)
    return {m: v for m, v in out.items() if v[0] or v[1]}


def branch_substitute(P, eps: int) -> dict:
    """uz -> (8*eps*i*q - 5*kappa*s)/6, vz -> (5*kappa*t - q)/6."""
    UZ = {((R1IDX["q"], 1),): (F0, F(8 * eps, 6)),
          tuple(sorted(((R1IDX["kappa"], 1), (R1IDX["s"], 1)))): (F(-5, 6), F0)}
    VZ = {tuple(sorted(((R1IDX["kappa"], 1), (R1IDX["t"], 1)))): (F(5, 6), F0),
          ((R1IDX["q"], 1),): (F(-1, 6), F0)}
    pow_cache: dict = {}

    def gpow(key0, base, e):
        key = (key0, e)
        if key not in pow_cache:
            out = {(): (F1, F0)}
            for _ in range(e):
                out = gmul(out, base)
            pow_cache[key] = out
        return pow_cache[key]

    out: dict = {}
    for m, c in P.items():
        eu = ev = 0
        rest = []
        for v, e in m:
            nm = VARS[v]
            if nm == "uz":
                eu = e
            elif nm == "vz":
                ev = e
            elif nm in R1IDX:
                rest.append((R1IDX[nm], e))
            else:
                fail(("branch substitution: foreign variable", nm))
        term = {tuple(sorted(rest)): (dy_to_frac(c), F0)}
        if eu:
            term = gmul(term, gpow("uz", UZ, eu))
        if ev:
            term = gmul(term, gpow("vz", VZ, ev))
        out = gadd(out, term)
    return out


def derive_r1(findings, eps: int) -> dict:
    rows_s = findings["rows_solved"]
    combo = findings["combo"]
    g1_14 = branch_substitute(rows_s[0][14], eps)
    g2_14 = branch_substitute(rows_s[1][14], eps)
    c21p = gadd(g2_14, g1_14, (F0, F(-eps, 2)))
    a8v, b8v = R1IDX["A8"], R1IDX["B8"]
    if any(v in (a8v, b8v) for m in c21p for v, _ in m):
        fail("R1 c21' still contains the top jet")
    kap, sv, tv = R1IDX["kappa"], R1IDX["s"], R1IDX["t"]

    def gterm(re, im, *pairs):
        return {tuple(sorted(pairs)): (F(re), F(im))}

    f1: dict = {}
    for cc, mono in ((27, ((sv, 2),)), (100, ((sv, 1), (kap, 2))),
                     (-576, ((tv, 2),))):
        f1 = gadd(f1, gterm(cc, 0, *mono))
    f2: dict = {}
    for cc, mono in ((9, ((sv, 3),)), (50, ((sv, 2), (kap, 2))),
                     (-1728, ((sv, 1), (tv, 2))), (-3200, ((tv, 2), (kap, 2)))):
        f2 = gadd(f2, gterm(cc, 0, *mono))
    expect = gadd(f2, gmul(gterm(0, -8 * eps, (tv, 1)), f1))
    expect = gmul({((kap, 1),): (F(5, 589824), F0)}, expect)
    if c21p != expect:
        fail("R1 c21'@14 report-crosscheck failed")
    gens = {
        "c21p14": c21p,
        "row1line14": g1_14,
        "conic1_c31at16": branch_substitute(combo[("c31", 16)], eps),
        "conic2_row4at16": branch_substitute(rows_s[3][16], eps),
        "e18a_row6at18": branch_substitute(rows_s[5][18], eps),
        "e18b_D51at18": branch_substitute(combo[("D51", 18)], eps),
        "e18c_D71at18": branch_substitute(combo[("D71", 18)], eps),
    }
    for k, v in gens.items():
        if not v:
            fail((k, "vanished identically on the branch"))
        want = {"c21p14": 14, "row1line14": 14, "conic1_c31at16": 16,
                "conic2_row4at16": 16}.get(k, 18)
        for m in v:
            w = sum(e * R1WEIGHT[R1VARS[vv]] for vv, e in m)
            if w != want:
                fail((k, "weighted inhomogeneity", w, want))
    return gens


def conj_gens(gens: dict) -> dict:
    return {k: {m: (re, -im) for m, (re, im) in v.items()}
            for k, v in gens.items()}


# ------------------------------------------------------------- controls

class SoftRetry(Exception):
    pass


def det_stream(label: str):
    counter = 0
    while True:
        raw = int.from_bytes(sha256(f"R400BD|{label}|{counter}".encode())
                             .digest()[:6], "big")
        counter += 1
        num = raw % 41 - 20
        den = raw // 41 % 7 + 1
        yield F(num, den)


def control_r2(findings, r2, rrF, comboF) -> dict:
    last = None
    for attempt in range(8):
        try:
            return _control_r2_once(findings, r2, rrF, comboF, attempt)
        except SoftRetry as exc:
            last = exc
    fail(("R2 control: all attempts soft-failed", str(last)))


def _control_r2_once(findings, r2, rrF, comboF, attempt: int) -> dict:
    p_polF = to_frac_poly(p_of())
    q_polF = to_frac_poly(q_of())
    D_polF = to_frac_poly(r2["D"])
    stream = det_stream(f"R2CTRL{attempt}")
    for _ in range(50):
        val = [next(stream) for _ in range(NV)]
        for nm in ("Az", "Bz", "A7", "B7"):
            val[VIDX[nm]] = F0
        if val[VIDX["kappa"]] == 0:
            continue
        Dv = peval(D_polF, val)
        if Dv == 0 or val[VIDX["s"]] == 0 or val[VIDX["t"]] == 0:
            continue
        break
    else:
        raise SoftRetry("no admissible point")
    pv, qv = peval(p_polF, val), peval(q_polF, val)

    def solve_pass():
        for n in range(14, 20):
            m = n - 6
            ai, bi = VIDX[f"A{m}"], VIDX[f"B{m}"]
            val[ai] = F0; val[bi] = F0
            i1v = peval(rrF[0][n], val)
            i2v = peval(rrF[1][n], val)
            val[ai] = F(-2048) * (pv * i1v - 16 * qv * i2v) / Dv
            val[bi] = F(-2048) * (64 * qv * i1v + 16 * pv * i2v) / Dv
        for tname, (i, n) in (("mu4_1", (3, 17)), ("mu4_2", (3, 18)),
                              ("mu4_3", (3, 19)), ("mu6_1", (5, 19))):
            val[VIDX[tname]] = F0
            val[VIDX[tname]] = peval(rrF[i][n], val)
        val[VIDX["Jdet_0"]] = F0
        val[VIDX["Jdet_0"]] = 4 * peval(comboF[("D71", 19)], val)

    # Staged affine absorption following the dependency levels.
    # Stage 1: {c31@17, D51@19} contain grade-9 jets only linearly (their
    #   quadratic jet pairs pair a level-dependent jet with the k2/k6-free
    #   A8,B8), so both are jointly affine in (k2_1, k6_1).
    # Stage 2: with those fixed, c31@18 is affine in k2_2 (its A9*B9 pair is
    #   now constant, A10,B10 enter linearly and are affine in k2_2).
    # Stage 3: with those fixed, c31@19 is affine in k2_3 via A11,B11.
    # Later stages cannot disturb earlier ones: k2_2,k2_3 are outside the
    # dependency closures of stage-1, and k2_3 outside stage-2's.
    # Each stage verifies its exact landing; the final full-window check
    # re-verifies everything.
    def affine_stage(eq_list, var_list, label):
        solve_pass()
        base = [peval(E, val) for E in eq_list]
        k = len(var_list)
        cols = []
        for uv in var_list:
            ci = VIDX[uv]
            save = val[ci]
            val[ci] = save + 1
            solve_pass()
            cols.append([peval(E, val) - base[i]
                         for i, E in enumerate(eq_list)])
            val[ci] = save
        A = [[cols[j][i] for j in range(k)] for i in range(k)]
        rhs = [-b for b in base]
        for col in range(k):
            piv = next((r for r in range(col, k) if A[r][col] != 0), None)
            if piv is None:
                raise SoftRetry(f"singular absorber stage {label}")
            A[col], A[piv] = A[piv], A[col]
            rhs[col], rhs[piv] = rhs[piv], rhs[col]
            for r in range(k):
                if r != col and A[r][col] != 0:
                    f = A[r][col] / A[col][col]
                    A[r] = [a - f * b for a, b in zip(A[r], A[col])]
                    rhs[r] = rhs[r] - f * rhs[col]
        for uv, i in zip(var_list, range(k)):
            val[VIDX[uv]] += rhs[i] / A[i][i]
        solve_pass()
        if any(peval(E, val) != 0 for E in eq_list):
            raise SoftRetry(f"absorption stage {label} did not land")

    affine_stage([comboF[("c31", 17)], comboF[("D51", 19)]],
                 ["k2_1", "k6_1"], "1:E17+E19b")
    affine_stage([comboF[("c31", 18)]], ["k2_2"], "2:E18")
    affine_stage([comboF[("c31", 19)]], ["k2_3"], "3:E19")
    solve_pass()
    for lbl, E in (("E17", comboF[("c31", 17)]), ("E18", comboF[("c31", 18)]),
                   ("E19", comboF[("c31", 19)]), ("E19b", comboF[("D51", 19)])):
        if peval(E, val) != 0:
            raise SoftRetry(f"staged absorption reopened {lbl}")
    used = {"E17+E19b": "k2_1,k6_1", "E18": "k2_2", "E19": "k2_3"}

    xvals = {k: peval(to_frac_poly(v), val) for k, v in r2["X"].items()}
    residual_map = {(2, 16): xvals["X1"] / Dv ** 2,
                    (3, 16): xvals["X2"] / Dv ** 2,
                    (4, 16): -xvals["X1"] / (8 * Dv ** 2),
                    (6, 16): -xvals["X1"] / (128 * Dv ** 2),
                    (5, 18): xvals["X3"] / Dv ** 2,
                    (4, 18): xvals["X4"] / Dv ** 2,
                    (6, 18): xvals["X5"] / Dv ** 2}
    bad = []
    for i in range(7):
        for n in range(8, 20):
            g = peval(rrF[i][n], val)
            if (i, n) in residual_map:
                if g != residual_map[(i, n)]:
                    bad.append((f"G{i+1}@{n}", "wrong closed residual"))
            elif g != 0:
                bad.append((f"G{i+1}@{n}", str(g)[:40]))
    if bad:
        fail(("R2 control: literal window mismatch", bad[:6]))
    if any(v == 0 for v in xvals.values()):
        raise SoftRetry("degenerate point: some X vanished")
    return {"absorbers": used,
            "point_sha256": digest_bytes(json.dumps(
                [str(v) for v in val], separators=(",", ":")).encode())}


def geval(P, val) -> tuple:
    a, b = F0, F0
    for m, (re, im) in P.items():
        pr, pi = re, im
        for v, e in m:
            for _ in range(e):
                x, y = val[v]
                pr, pi = pr * x - pi * y, pr * y + pi * x
        a, b = a + pr, b + pi
    return a, b


def control_r1(findings, gens, eps, rrF, comboF) -> dict:
    last = None
    for attempt in range(8):
        try:
            return _control_r1_once(findings, gens, eps, rrF, comboF, attempt)
        except SoftRetry as exc:
            last = exc
    fail(("R1 control: all attempts soft-failed", eps, str(last)))


def _control_r1_once(findings, gens, eps, rrF, comboF, attempt: int) -> dict:
    stream = det_stream(f"R1CTRL{eps}|{attempt}")
    C = []
    for i in range(NV):
        C.append((next(stream), next(stream)))
    for nm in ("Az", "Bz", "A7", "B7"):
        C[VIDX[nm]] = (F0, F0)
    for nm in ("s", "t", "s1", "t1", "kappa"):
        C[VIDX[nm]] = (C[VIDX[nm]][0], F0)
    if C[VIDX["kappa"]][0] == 0:
        C[VIDX["kappa"]] = (F(3), F0)
    if C[VIDX["s"]][0] == 0 or C[VIDX["t"]][0] == 0:
        raise SoftRetry("zero base coordinate")
    qc = (F(5, 2) + attempt, F(1, 3))
    kv, sv, tv = C[VIDX["kappa"]], C[VIDX["s"]], C[VIDX["t"]]
    uz = (F(-5, 6) * kv[0] * sv[0] - F(8 * eps, 6) * qc[1],
          F(8 * eps, 6) * qc[0])
    vz = (F(5, 6) * kv[0] * tv[0] - F(1, 6) * qc[0], -F(1, 6) * qc[1])
    C[VIDX["uz"]] = uz
    C[VIDX["vz"]] = vz

    def cadd(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def cmul(x, y):
        return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def csc(c, x):
        return (c * x[0], c * x[1])

    def cdiv(x, y):
        d = y[0] * y[0] + y[1] * y[1]
        if d == 0:
            fail("R1 control: division by zero")
        return ((x[0] * y[0] + x[1] * y[1]) / d, (x[1] * y[0] - x[0] * y[1]) / d)

    def ceval(P):
        cache: dict = {}
        a, b = F0, F0
        for m, c in P.items():
            pr, pi = c, F0
            for v, e in m:
                key = (v, e)
                pw = cache.get(key)
                if pw is None:
                    px, py = F1, F0
                    x, y = C[v]
                    for _ in range(e):
                        px, py = px * x - py * y, px * y + py * x
                    pw = (px, py)
                    cache[key] = pw
                pr, pi = pr * pw[0] - pi * pw[1], pr * pw[1] + pi * pw[0]
            a, b = a + pr, b + pi
        return (a, b)

    epsi = (F0, F(eps))

    def solve_pass():
        for n in range(14, 20):
            m = n - 6
            bi = VIDX[f"B{m}"]
            C[bi] = (F0, F0)
            i1v = ceval(rrF[0][n])
            C[bi] = cdiv(csc(F(-2048), i1v), qc)
            if n >= 15:
                mu = VIDX[f"mu2_{n-14}"]
                C[mu] = (F0, F0)
                r2v = ceval(rrF[1][n])
                r1v = ceval(rrF[0][n])
                C[mu] = cadd(r2v, cmul(csc(F(-1, 2), epsi), r1v))
        for tname, (i, n) in (("mu4_1", (3, 17)), ("mu4_2", (3, 18)),
                              ("mu4_3", (3, 19)), ("mu6_1", (5, 19))):
            C[VIDX[tname]] = (F0, F0)
            C[VIDX[tname]] = ceval(rrF[i][n])
        C[VIDX["Jdet_0"]] = (F0, F0)
        C[VIDX["Jdet_0"]] = csc(F(4), ceval(comboF[("D71", 19)]))

    # Staged affine absorption over Q(i); same level structure as CELL-R2.
    def affine_stage(eq_list, var_list, label):
        solve_pass()
        base = [ceval(E) for E in eq_list]
        k = len(var_list)
        cols = []
        for uv in var_list:
            ci = VIDX[uv]
            save = C[ci]
            C[ci] = cadd(save, (F1, F0))
            solve_pass()
            vals = [ceval(E) for E in eq_list]
            cols.append([(v[0] - b[0], v[1] - b[1])
                         for v, b in zip(vals, base)])
            C[ci] = save
        A = [[cols[j][i] for j in range(k)] for i in range(k)]
        rhs = [csc(F(-1), b) for b in base]
        for col in range(k):
            piv = next((r for r in range(col, k) if A[r][col] != (F0, F0)),
                       None)
            if piv is None:
                raise SoftRetry(f"singular absorber stage {label} (R1)")
            A[col], A[piv] = A[piv], A[col]
            rhs[col], rhs[piv] = rhs[piv], rhs[col]
            for r in range(k):
                if r != col and A[r][col] != (F0, F0):
                    f = cdiv(A[r][col], A[col][col])
                    A[r] = [(a[0] - (f[0] * b[0] - f[1] * b[1]),
                             a[1] - (f[0] * b[1] + f[1] * b[0]))
                            for a, b in zip(A[r], A[col])]
                    fb = cmul(f, rhs[col])
                    rhs[r] = (rhs[r][0] - fb[0], rhs[r][1] - fb[1])
        for i, uv in enumerate(var_list):
            C[VIDX[uv]] = cadd(C[VIDX[uv]], cdiv(rhs[i], A[i][i]))
        solve_pass()
        if any(ceval(E) != (F0, F0) for E in eq_list):
            raise SoftRetry(f"absorption stage {label} did not land (R1)")

    affine_stage([comboF[("c31", 17)], comboF[("D51", 19)]],
                 ["k2_1", "k6_1"], "1:E17+E19b")
    affine_stage([comboF[("c31", 18)]], ["k2_2"], "2:E18")
    affine_stage([comboF[("c31", 19)]], ["k2_3"], "3:E19")
    solve_pass()
    for lbl, E in (("E17", comboF[("c31", 17)]), ("E18", comboF[("c31", 18)]),
                   ("E19", comboF[("c31", 19)]), ("E19b", comboF[("D51", 19)])):
        if ceval(E) != (F0, F0):
            raise SoftRetry(f"staged absorption reopened {lbl} (R1)")
    used = {"E17+E19b": "k2_1,k6_1", "E18": "k2_2", "E19": "k2_3"}

    gval = [(F0, F0)] * len(R1VARS)
    gval[R1IDX["s"]] = sv; gval[R1IDX["t"]] = tv
    gval[R1IDX["kappa"]] = kv; gval[R1IDX["q"]] = qc
    gval[R1IDX["A8"]] = C[VIDX["A8"]]; gval[R1IDX["B8"]] = C[VIDX["B8"]]
    gv = {k: geval(P, gval) for k, P in gens.items()}
    if gv["row1line14"] != (F0, F0):
        fail("R1 control: row1 line not satisfied by the solve")
    residual_map = {
        (1, 14): gv["c21p14"],
        (2, 16): gv["conic1_c31at16"],
        (3, 16): gv["conic2_row4at16"],
        (4, 16): csc(F(-1, 8), gv["conic1_c31at16"]),
        (6, 16): csc(F(-1, 128), gv["conic1_c31at16"]),
        (5, 18): gv["e18a_row6at18"],
        (4, 18): gv["e18b_D51at18"],
        (6, 18): gv["e18c_D71at18"],
    }
    bad = []
    for i in range(7):
        for n in range(8, 20):
            g = ceval(rrF[i][n])
            want = residual_map.get((i, n), (F0, F0))
            if g != want:
                bad.append(f"G{i+1}@{n}")
    if bad:
        fail(("R1 control: literal window mismatch", eps, bad[:6]))
    if any(v == (F0, F0) for k, v in gv.items() if k != "row1line14"):
        raise SoftRetry(f"R1 degenerate point eps={eps}")
    return {"absorbers": used}


def mutation_controls(tails: dict) -> dict:
    def detect(rows_m) -> list:
        try:
            return structural_generic(rows_m, 16, strict=False)["failures"]
        except RuntimeError as exc:
            return ["EXCEPTION:" + str(exc.args[0])[:120]]

    out = {}
    target = None
    for tno, (mono, coeff) in enumerate(tails["4"]):
        if [int(x) for x in mono] == [0, 0, 0, 0, 0, 2, 5, 0, 0, 0]:
            if F(str(coeff)) != F(-63, 1024):
                fail("mutation control: expected row-4 tail coefficient changed")
            target = tno
    if target is None:
        fail("mutation control: row-4 tail [0,0,0,0,0,2,5,0,0,0] not found")
    hits = detect(build_rows(tails, 16, False, tail_mutation=(4, target, F(1))))
    if not hits:
        fail("mutation control (tail +1) NOT detected")
    out["tail_plus1_detected_at"] = hits[:4]
    hits = detect(build_rows(tails, 16, False, target_sign=1))
    if not hits:
        fail("mutation control (target sign) NOT detected")
    out["target_sign_detected_at"] = hits[:4]
    hits = detect(build_rows(tails, 16, False, k6_shift=5))
    if not hits:
        fail("mutation control (k6 shift) NOT detected")
    out["k6_shift_detected_at"] = hits[:4]
    return out


# ------------------------------------------------------------- emission

def q_poly_text(P, allowed: list, clear=True):
    PF = {m: dy_to_frac(c) for m, c in P.items()} if P and isinstance(
        next(iter(P.values())), tuple) and isinstance(
        next(iter(P.values()))[0], int) else dict(P)
    idx_map = {VIDX[n]: n for n in allowed}
    pos = {VIDX[n]: i for i, n in enumerate(allowed)}
    for m in PF:
        for v, _ in m:
            if v not in idx_map:
                fail(("emission: foreign variable", VARS[v]))
    from math import gcd
    denl = 1
    for c in PF.values():
        denl = denl * c.denominator // gcd(denl, c.denominator)
    numg = 0
    for c in PF.values():
        numg = gcd(numg, abs(c.numerator * (denl // c.denominator)))
    scale = F(denl, numg if (clear and numg) else 1) if clear else F1

    def mono_key(m):
        exps = [0] * len(allowed)
        for v, e in m:
            exps[pos[v]] = e
        return (-sum(exps), tuple(-x for x in exps))

    items = sorted(PF.items(), key=lambda kv: mono_key(kv[0]))
    if clear and items and (items[0][1] * scale) < 0:
        scale = -scale
    parts = []
    for m, c in items:
        c = c * scale
        if clear and c.denominator != 1:
            fail("emission: clearing failed")
        factors = []
        for v, e in sorted(m, key=lambda ve: pos[ve[0]]):
            factors.append(f"{idx_map[v]}^{e}" if e > 1 else idx_map[v])
        body = "*".join(factors)
        cn = c.numerator if clear else c
        if body:
            cs = "" if cn == 1 else ("-" if cn == -1 else f"{cn}*")
        else:
            cs = f"{cn}"
        term = f"{cs}{body}"
        if parts and not term.startswith("-"):
            parts.append("+")
        parts.append(term)
    return "".join(parts) if parts else "0", scale


def g_poly_text(P, clear=True):
    from math import gcd
    denl = 1
    for re, im in P.values():
        for c in (re, im):
            denl = denl * c.denominator // gcd(denl, c.denominator)
    numg = 0
    for re, im in P.values():
        for c in (re, im):
            numg = gcd(numg, abs(c.numerator * (denl // c.denominator)))
    scale = F(denl, numg if (clear and numg) else 1) if clear else F1

    def mono_key(m):
        exps = [0] * len(R1VARS)
        for v, e in m:
            exps[v] = e
        return (-sum(exps), tuple(-x for x in exps))

    items = sorted(P.items(), key=lambda kv: mono_key(kv[0]))
    if items:
        re0, im0 = items[0][1]
        lead = re0 if re0 else im0
        if lead * scale < 0:
            scale = -scale
    parts = []
    for m, (re, im) in items:
        re, im = re * scale, im * scale
        if clear and (re.denominator != 1 or im.denominator != 1):
            fail("emission: Gaussian clearing failed")
        rn = re.numerator if clear else re
        imn = im.numerator if clear else im
        if imn == 0:
            cs = f"({rn})"
        elif rn == 0:
            cs = f"({imn}*ii)"
        else:
            sign = "+" if imn > 0 else "-"
            cs = f"({rn}{sign}{abs(imn)}*ii)"
        factors = []
        for v, e in sorted(m):
            factors.append(f"{R1VARS[v]}^{e}" if e > 1 else R1VARS[v])
        body = "*".join(factors)
        term = f"{cs}*{body}" if body else cs
        parts.append("+" if parts else "")
        parts.append(term)
    return "".join(parts) if parts else "0", scale


def _int_clear_q(P: dict) -> dict:
    from math import gcd
    PF = to_frac_poly(P)
    denl = 1
    for c in PF.values():
        denl = denl * c.denominator // gcd(denl, c.denominator)
    return {m: c * denl for m, c in PF.items()}


def _int_clear_g(P: dict) -> dict:
    from math import gcd
    denl = 1
    for re, im in P.values():
        for c in (re, im):
            denl = denl * c.denominator // gcd(denl, c.denominator)
    return {m: (re * denl, im * denl) for m, (re, im) in P.items()}


def modp_text(P, allowed: list, p: int, isub: int | None = None,
              gaussian=False) -> str:
    idx_map = ({VIDX[n]: n for n in allowed if n in VIDX}
               if not gaussian else None)
    acc: dict = {}
    for m, c in P.items():
        if gaussian:
            re, im = c
            cv = (re.numerator * pow(re.denominator, -1, p)
                  + (im.numerator * pow(im.denominator, -1, p)) * isub) % p
        else:
            cv = (c.numerator * pow(c.denominator, -1, p)) % p
        if cv:
            acc[m] = (acc.get(m, 0) + cv) % p
    acc = {m: c for m, c in acc.items() if c}

    def nm(v):
        return R1VARS[v] if gaussian else idx_map[v]

    def order_pos(v):
        return v if gaussian else allowed.index(idx_map[v])

    def mono_key(m):
        exps = {}
        for v, e in m:
            exps[order_pos(v)] = e
        vec = [exps.get(i, 0) for i in range(len(allowed))]
        return (-sum(vec), tuple(-x for x in vec))

    parts = []
    for m, c in sorted(acc.items(), key=lambda kv: mono_key(kv[0])):
        factors = [f"{nm(v)}^{e}" if e > 1 else nm(v)
                   for v, e in sorted(m, key=lambda ve: order_pos(ve[0]))]
        body = "*".join(factors)
        term = f"{c}*{body}" if body else f"{c}"
        if parts:
            parts.append("+")
        parts.append(term)
    return "".join(parts) if parts else "0"


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for sp in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % sp == 0:
            return n == sp
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2; r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def sqrt_minus_one(p: int) -> int:
    if p % 4 != 1:
        fail((p, "not 1 mod 4"))
    for a in range(2, p):
        if pow(a, (p - 1) // 2, p) == p - 1:
            r = pow(a, (p - 1) // 4, p)
            if r * r % p == p - 1:
                return min(r, p - r)
    fail((p, "no sqrt(-1)"))


def rabinowitsch_r2(chart: str, p: int) -> str:
    prod = pmul(pmul(padd(pmul(p_of(), p_of()),
                          pmul(q_of(), q_of()), (1, -6)), pvar("kappa")),
                pvar(chart))
    txt = modp_text(_int_clear_q(prod), ["s", "t", "uz", "vz", "kappa", "w"], p)
    terms = []
    for term in txt.split("+"):
        head, sep, tail = term.partition("*")
        terms.append(f"{head}*w*{tail}" if sep else f"{term}*w")
    return "+".join(terms) + f"+{p-1}"


SING_CONTROLS = r"""// version-independent saturation: stabilized quotient chain.
// satur(I,J) returns list(I:J^infinity as a std ideal, iteration count e);
// every g in the saturation satisfies g*J^e subset I.
proc satur(ideal II, ideal JJ)
{
  ideal cur=std(II);
  ideal nxt;
  int e;
  while (1)
  {
    nxt=std(quotient(cur,JJ));
    if (size(reduce(nxt,cur))==0) { return(list(cur,e)); }
    cur=nxt;
    e=e+1;
  }
}
// fail-closed machinery controls (satur / lift / reduce semantics)
poly one=1;
list c1=satur(ideal(var(1)^2),ideal(var(1)));
if (reduce(one,std(c1[1]))!=0) { print("R400_FAIL=CONTROL_SAT_UNIT"); quit; }
if (c1[2]<1) { print("R400_FAIL=CONTROL_SAT_EXPONENT"); quit; }
list c2=satur(ideal(var(1)*var(2)),ideal(var(2)));
if (reduce(one,std(c2[1]))==0) { print("R400_FAIL=CONTROL_SAT_NONUNIT"); quit; }
if (reduce(var(1),std(c2[1]))!=0) { print("R400_FAIL=CONTROL_SAT_VALUE"); quit; }
ideal cg=var(1),var(2);
poly ct=3*var(1)+5*var(2);
matrix cl=lift(cg,ct);
if (ct-cg[1]*cl[1,1]-cg[2]*cl[2,1]!=0) { print("R400_FAIL=CONTROL_LIFT"); quit; }
print("R400_MACHINERY_CONTROLS=PASS");
"""


def sing_r2_script(gens_text: list) -> str:
    glines = ",\n  ".join(gens_text)
    return f"""// R4-00-R2-BASE-DECIDE / Singular exact characteristic-zero driver v1
// ring map: base coordinates (s,t,uz,vz,kappa) of the R4-00 CELL-R2 residual;
// weights (4,4,6,6,2); generators X1..X5 are the D^2-cleared closed window
// content (c31@16,row4@16,row6@18,D51@18,D71@18 after the unique rank-2 solve).
// Constructible cell: V(X1..X5) with D!=0, kappa!=0, (s,t)!=(0,0).
// EMPTY means: unit saturation chain + explicit lift certificates
//   (D*kappa)^a*s^N and (D*kappa)^a*t^N in (X1..X5), independently checkable.
// NONUNIT means: surviving base components; STAGE-2 completion required
//   before any nonemptiness statement about CELL-R2 itself.
LIB "primdec.lib";
ring r=0,(s,t,uz,vz,kappa),wp(4,4,6,6,2);
{SING_CONTROLS}
poly pp=6*uz+5*kappa*s; poly qq=-6*vz+5*kappa*t; poly DD=pp^2+64*qq^2;
ideal I=
  {glines};
if (size(I)!=5) {{ print("R400_FAIL=GEN_COUNT"); quit; }}
int hg=1; int k;
for (k=1;k<=5;k++) {{ if (homog(I[k])==0) {{ hg=0; }} }}
if (hg==0) {{ print("R400_FAIL=INPUT_NOT_WEIGHTED_HOMOGENEOUS"); quit; }}
int t0=rtimer;
list SL=satur(I,ideal(DD*kappa));
ideal J1=SL[1];
print("R400R2_SAT1_ITER="+string(SL[2]));
list SL2=satur(J1,ideal(s,t));
ideal J2=SL2[1];
print("R400R2_SAT2_ITER="+string(SL2[2]));
ideal SJ2=std(J2);
poly one2=1;
if (reduce(one2,SJ2)==0)
{{
  print("R400R2_BASE=UNIT_AFTER_SATURATION");
  ideal SJ1=std(J1);
  int N=1;
  while ((reduce(s^N,SJ1)!=0)||(reduce(t^N,SJ1)!=0))
  {{ N=N+1; if (N>80) {{ print("R400_FAIL=NO_ST_POWER"); quit; }} }}
  ideal SI=std(I);
  int a=0;
  while ((reduce((DD*kappa)^a*s^N,SI)!=0)||(reduce((DD*kappa)^a*t^N,SI)!=0))
  {{ a=a+1; if (a>80) {{ print("R400_FAIL=NO_SAT_EXPONENT"); quit; }} }}
  print("R400R2_CERT_A="+string(a));
  print("R400R2_CERT_N="+string(N));
  poly gs=(DD*kappa)^a*s^N; poly gt=(DD*kappa)^a*t^N;
  matrix Cs=lift(I,gs); matrix Ct=lift(I,gt);
  poly chks=gs; poly chkt=gt;
  for (k=1;k<=5;k++) {{ chks=chks-Cs[k,1]*I[k]; chkt=chkt-Ct[k,1]*I[k]; }}
  if ((chks!=0)||(chkt!=0)) {{ print("R400_FAIL=LIFT_VERIFY"); quit; }}
  link ls=":w R2_CERT_S.txt";
  write(ls,"R4-00-R2 certificate: (DD*kappa)^a*s^N = sum_k C[k]*X[k]");
  write(ls,"a="+string(a)); write(ls,"N="+string(N));
  for (k=1;k<=5;k++) {{ write(ls,"C"+string(k)+"="+string(Cs[k,1])); }}
  close(ls);
  link lt=":w R2_CERT_T.txt";
  write(lt,"R4-00-R2 certificate: (DD*kappa)^a*t^N = sum_k C[k]*X[k]");
  write(lt,"a="+string(a)); write(lt,"N="+string(N));
  for (k=1;k<=5;k++) {{ write(lt,"C"+string(k)+"="+string(Ct[k,1])); }}
  close(lt);
  print("R400R2_RESULT=EMPTY_WITH_LIFT_CERTIFICATE");
}}
else
{{
  print("R400R2_BASE=NONUNIT_SURVIVOR");
  print("R400R2_DIM="+string(dim(SJ2)));
  list PD=primdecGTZ(J2);
  print("R400R2_COMPONENTS="+string(size(PD)));
  link lc=":w R2_COMPONENTS.txt";
  int j;
  for (j=1;j<=size(PD);j++)
  {{
    write(lc,"COMPONENT "+string(j));
    write(lc,"PRIMARY="+string(PD[j][1]));
    write(lc,"PRIME="+string(PD[j][2]));
    ideal SP=std(PD[j][2]);
    write(lc,"dim="+string(dim(SP)));
    write(lc,"D_in_prime="+string(reduce(DD,SP)==0));
    write(lc,"kappa_in_prime="+string(reduce(kappa,SP)==0));
    write(lc,"s_in_prime="+string(reduce(s,SP)==0));
    write(lc,"t_in_prime="+string(reduce(t,SP)==0));
  }}
  close(lc);
  print("R400R2_RESULT=SURVIVING_BASE_COMPONENTS_STAGE2_REQUIRED");
}}
print("R400R2_RTIMER_MS="+string(rtimer-t0));
print("R400R2_DONE=1");
quit;
"""


def sing_r1_script(gens_text: list, eps_label: str) -> str:
    glines = ",\n  ".join(gens_text)
    return f"""// R4-00-R1-BASE-DECIDE ({eps_label}) / Singular exact Q(i) driver v1
// ring map: (s,t,kappa,q,A8,B8), weights (4,4,2,6,8,8), over Q(ii), ii^2=-1;
// branch uz=(8*eps*ii*q-5*kappa*s)/6, vz=(5*kappa*t-q)/6 substituted.
// Generators: c21'@14, row1@14 line, c31@16, row4@16, row6@18, D51@18,
// D71@18 (raw grade-18 forms; L18,L51,L71 are unimodular combinations of
// these with the grade-16 conics -- same ideal).
// Constructible cell: V(gens) with q!=0, kappa!=0, (s,t)!=(0,0).
// EMPTY: unit saturation + lift certificates (q*kappa)^a*s^N, (q*kappa)^a*t^N.
// NONUNIT: surviving components; STAGE-2 completion required.
LIB "primdec.lib";
ring r=(0,ii),(s,t,kappa,q,A8,B8),wp(4,4,2,6,8,8);
minpoly=ii^2+1;
{SING_CONTROLS}
ideal I=
  {glines};
if (size(I)!=7) {{ print("R400_FAIL=GEN_COUNT"); quit; }}
int hg=1; int k;
for (k=1;k<=7;k++) {{ if (homog(I[k])==0) {{ hg=0; }} }}
if (hg==0) {{ print("R400_FAIL=INPUT_NOT_WEIGHTED_HOMOGENEOUS"); quit; }}
int t0=rtimer;
list SL=satur(I,ideal(q*kappa));
ideal J1=SL[1];
print("R400R1_SAT1_ITER="+string(SL[2]));
list SL2=satur(J1,ideal(s,t));
ideal J2=SL2[1];
print("R400R1_SAT2_ITER="+string(SL2[2]));
ideal SJ2=std(J2);
poly one2=1;
if (reduce(one2,SJ2)==0)
{{
  print("R400R1_BASE=UNIT_AFTER_SATURATION");
  ideal SJ1=std(J1);
  int N=1;
  while ((reduce(s^N,SJ1)!=0)||(reduce(t^N,SJ1)!=0))
  {{ N=N+1; if (N>80) {{ print("R400_FAIL=NO_ST_POWER"); quit; }} }}
  ideal SI=std(I);
  int a=0;
  while ((reduce((q*kappa)^a*s^N,SI)!=0)||(reduce((q*kappa)^a*t^N,SI)!=0))
  {{ a=a+1; if (a>80) {{ print("R400_FAIL=NO_SAT_EXPONENT"); quit; }} }}
  print("R400R1_CERT_A="+string(a));
  print("R400R1_CERT_N="+string(N));
  poly gs=(q*kappa)^a*s^N; poly gt=(q*kappa)^a*t^N;
  matrix Cs=lift(I,gs); matrix Ct=lift(I,gt);
  poly chks=gs; poly chkt=gt;
  for (k=1;k<=7;k++) {{ chks=chks-Cs[k,1]*I[k]; chkt=chkt-Ct[k,1]*I[k]; }}
  if ((chks!=0)||(chkt!=0)) {{ print("R400_FAIL=LIFT_VERIFY"); quit; }}
  link ls=":w R1_{eps_label}_CERT_S.txt";
  write(ls,"R4-00-R1 {eps_label} certificate: (q*kappa)^a*s^N = sum C[k]*gen[k]");
  write(ls,"a="+string(a)); write(ls,"N="+string(N));
  for (k=1;k<=7;k++) {{ write(ls,"C"+string(k)+"="+string(Cs[k,1])); }}
  close(ls);
  link lt=":w R1_{eps_label}_CERT_T.txt";
  write(lt,"R4-00-R1 {eps_label} certificate: (q*kappa)^a*t^N = sum C[k]*gen[k]");
  write(lt,"a="+string(a)); write(lt,"N="+string(N));
  for (k=1;k<=7;k++) {{ write(lt,"C"+string(k)+"="+string(Ct[k,1])); }}
  close(lt);
  print("R400R1_RESULT=EMPTY_WITH_LIFT_CERTIFICATE");
}}
else
{{
  print("R400R1_BASE=NONUNIT_SURVIVOR");
  print("R400R1_DIM="+string(dim(SJ2)));
  list PD=primdecGTZ(J2);
  print("R400R1_COMPONENTS="+string(size(PD)));
  link lc=":w R1_{eps_label}_COMPONENTS.txt";
  int j;
  for (j=1;j<=size(PD);j++)
  {{
    write(lc,"COMPONENT "+string(j));
    write(lc,"PRIMARY="+string(PD[j][1]));
    write(lc,"PRIME="+string(PD[j][2]));
    ideal SP=std(PD[j][2]);
    write(lc,"dim="+string(dim(SP)));
    write(lc,"q_in_prime="+string(reduce(q,SP)==0));
    write(lc,"kappa_in_prime="+string(reduce(kappa,SP)==0));
    write(lc,"s_in_prime="+string(reduce(s,SP)==0));
    write(lc,"t_in_prime="+string(reduce(t,SP)==0));
  }}
  close(lc);
  print("R400R1_RESULT=SURVIVING_BASE_COMPONENTS_STAGE2_REQUIRED");
}}
print("R400R1_RTIMER_MS="+string(rtimer-t0));
print("R400R1_DONE=1");
quit;
"""


def emit(findings, r2, r1p, r1m, controls) -> None:
    OUT.mkdir(exist_ok=True)
    files: dict = {}
    prov: dict = {"inputs": {str(k.relative_to(ROOT)): v
                             for k, v in EXPECTED.items()},
                  "controls": controls, "scales": {}}

    r2order = ["s", "t", "uz", "vz", "kappa"]
    r2texts = []
    for k in ("X1", "X2", "X3", "X4", "X5"):
        txt, sc = q_poly_text(r2["X"][k], r2order)
        prov["scales"][f"R2:{k}"] = str(sc)
        r2texts.append(txt)
    files["R2_GENS.txt"] = "".join(
        f"{k}={t};\n" for k, t in zip(("X1", "X2", "X3", "X4", "X5"), r2texts))
    files["R4_00_R2_BASE_DECIDE.sing"] = sing_r2_script(r2texts)

    r1_order = ["c21p14", "row1line14", "conic1_c31at16", "conic2_row4at16",
                "e18a_row6at18", "e18b_D51at18", "e18c_D71at18"]
    for eps_label, gens in (("epsP", r1p), ("epsM", r1m)):
        texts = []
        for k in r1_order:
            txt, sc = g_poly_text(gens[k])
            prov["scales"][f"R1{eps_label}:{k}"] = str(sc)
            texts.append(txt)
        files[f"R1_{eps_label}_GENS.txt"] = "".join(
            f"{k}={t};\n" for k, t in zip(r1_order, texts))
        files[f"R4_00_R1_BASE_DECIDE_{eps_label}.sing"] = sing_r1_script(
            texts, eps_label)

    shard_note = ("# SCREENING-TIER modular shard: a [1] Groebner basis mod p\n"
                  "# is evidence only for this prime; it is NOT char-0\n"
                  "# emptiness.  Twin charts jointly cover (s,t)!=(0,0).\n")
    prov["shard_note"] = shard_note
    for p in PRIMES:
        if not is_prime(p):
            fail((p, "not prime"))
        for chart in ("s", "t"):
            polys = [modp_text(_int_clear_q(r2["X"][k]), r2order + ["w"], p)
                     for k in ("X1", "X2", "X3", "X4", "X5")]
            body = ",\n".join(polys + [rabinowitsch_r2(chart, p)])
            files[f"shard_r2_chart{chart}_p{p}.ms"] = (
                f"{','.join(r2order + ['w'])}\n{p}\n{body}\n")
        r = sqrt_minus_one(p)
        prov.setdefault("sqrt_minus_one", {})[str(p)] = r
        for eps_label, gens in (("epsP", r1p), ("epsM", r1m)):
            for chart in ("s", "t"):
                polys = [modp_text(_int_clear_g(gens[k]), R1VARS + ["w"], p,
                                   isub=r, gaussian=True) for k in r1_order]
                body = ",\n".join(polys + [f"w*q*kappa*{chart}+{p-1}"])
                files[f"shard_r1{eps_label}_chart{chart}_p{p}.ms"] = (
                    f"{','.join(R1VARS + ['w'])}\n{p}\n{body}\n")

    rows_s = findings["rows_solved"]
    combo = findings["combo"]
    stage2 = ["# STAGE-2 raw window material on the solved R4-00 stratum",
              "# (z on cone, A7=B7=0; all remaining unknowns literal).",
              "# Exact Q coefficients (a/b); variables named as in the report."]
    full_order = [n for n in VARS if n not in ("Az", "Bz", "A7", "B7")]
    for lbl, P in (("c31at17", combo[("c31", 17)]), ("c31at18", combo[("c31", 18)]),
                   ("c31at19", combo[("c31", 19)]), ("D51at19", combo[("D51", 19)]),
                   ("row4at17", rows_s[3][17]), ("row4at18", rows_s[3][18]),
                   ("row4at19", rows_s[3][19]), ("row6at19", rows_s[5][19]),
                   ("D71at19", combo[("D71", 19)]),
                   ("I1at14", findings["I1@14"]), ("I2at14", findings["I2@14"]),
                   ("Ahat8", r2["Ahat8"]), ("Bhat8", r2["Bhat8"])):
        txt, _ = q_poly_text(P, full_order, clear=False)
        stage2.append(f"{lbl}={txt};")
    files["STAGE2_WINDOW_MATERIAL.txt"] = "\n".join(stage2) + "\n"

    prov["window_absent_variables"] = findings["window_absent"]
    prov["window_occurring_variables"] = findings["window_occurrence"]
    files["PROVENANCE.json"] = json.dumps(prov, sort_keys=True, indent=1) + "\n"

    manifest = []
    for name in sorted(files):
        path = OUT / name
        path.write_text(files[name])
        manifest.append(f"{digest(path)}  {name}")
    (OUT / "MANIFEST.sha256").write_text("\n".join(manifest) + "\n")
    print("PACKET_MANIFEST_SHA256=" + digest(OUT / "MANIFEST.sha256"))
    for line in manifest:
        print("PACKET " + line)


# ---------------------------------------------------------------- main

def main() -> None:
    smoke = "--smoke" in sys.argv
    tails = load_tails()
    note("tails loaded and censused (569, weights, load linearity, dyadic)")
    rows_g = build_rows(tails, 16, solved=False)
    note("generic build (trunc 16) done")
    structural_generic(rows_g, 16, strict=True)
    note("generic entry checks A-E2 PASS")
    controls: dict = {}
    controls["mutations"] = mutation_controls(tails)
    note("mutation controls PASS: " + json.dumps(controls["mutations"],
                                                 sort_keys=True))
    if smoke:
        print("R400_BASE_DECIDE_SMOKE=PASS")
        return
    rows_s = build_rows(tails, 20, solved=True)
    note("solved-stratum build (trunc 20) done; sizes " + str(
        [len(rows_s[i][19]) for i in range(7)]))
    # cross-build consistency: generic build with the four zeros killed must
    # agree with the solved build on all common grades
    kill = {VIDX[n] for n in ("Az", "Bz", "A7", "B7")}
    for i in range(7):
        for n in range(16):
            if subzero(rows_g[i][n], kill) != rows_s[i][n]:
                fail(("cross-build mismatch", i + 1, n))
    note("cross-build consistency PASS")
    findings = structural_solved(rows_s, 20, strict=True)
    note("solved window checks C..L PASS")
    r2 = derive_r2(findings)
    note("R2 generators derived; terms " + str(
        {k: len(v) for k, v in r2["X"].items()}))
    r1p = derive_r1(findings, +1)
    r1m = derive_r1(findings, -1)
    if conj_gens(r1p) != r1m:
        fail("R1 eps branches are not exact conjugates")
    note("R1 generators derived (both branches, conjugacy exact); terms " + str(
        {k: len(v) for k, v in r1p.items()}))
    rrF = [[to_frac_poly(rows_s[i][n]) for n in range(20)] for i in range(7)]
    comboF = {k: to_frac_poly(v) for k, v in findings["combo"].items()}
    controls["r2_literal_row"] = control_r2(findings, r2, rrF, comboF)
    note("R2 literal-row completeness control PASS: "
         + json.dumps(controls["r2_literal_row"]["absorbers"], sort_keys=True))
    controls["r1_literal_row_epsP"] = control_r1(findings, r1p, +1, rrF, comboF)
    controls["r1_literal_row_epsM"] = control_r1(findings, r1m, -1, rrF, comboF)
    note("R1 literal-row completeness controls PASS (both branches)")
    emit(findings, r2, r1p, r1m, controls)
    print("R400_BASE_DECIDE_SELFCHECK=PASS")
    print("WINDOW_ABSENT=" + ",".join(findings["window_absent"]))


if __name__ == "__main__":
    main()
