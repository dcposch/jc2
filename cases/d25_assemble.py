#!/usr/bin/env python3
"""D25 family assembly stage (sol-round6 sect 2 spec; runs on box01).

Consumes the D25RED reduction stage (cases/d25_reduce.py; 906/906
checkpoints banked -- used here as the gated NF engine + trace bank)
plus the D25 jets bank and the 36-fiber atlas artifacts, and assembles,
per prime, the FAMILY D25 sparse quotient of xmodel/sol-round6.md
sect 2.5:

    J25^B = I23^B + <R_1..R_s>,   0 <= s <= 5,

one master object covering all 36 atlas fibers of the split etale
coefficient algebra B36 ~= F_p[A1,A2,h1,h2]/(A1^3-(3+r3), A2^3-(3-r3),
2h1^2-3, 2h2^2-3) ~= F_p^36: shared pristine Row 24, ONE rank-4 Schur
transform L24 (constant 5x9) to <= 5 residuals, one monomial skeleton,
36 coefficient components (idempotent = radical point), componentwise
NF/verdict discipline.

PIPELINE (per prime; per-fiber checkpoints, resume-safe):
  B  radkey-level Row-24 census: 90 frontier first-occurrence entries,
     digest vs the banked ab5ee038.. (recipe = cases/sol_algkill.py::
     check_row24 serialization), factorization (2) A24 = C24 diag(d_j)
     (a per-row unit W-monomial normalizer is tolerated and recorded),
     C24 mod p, deterministic RREF -> rank 4 / pivot columns {0,1,2,3},
     L24 = canonical RREF basis of the left kernel (5x9).
  C  radkey-level Row-22 census: A22 = C10 diag(u_j) (single carrier
     per column), rank C10 = 4, L10 = left kernel (6x10); solved-4 =
     (tg02_54, tg01_54, tg2_49, tg1_49), kernel-6 = (tg1_54, tg2_54,
     tf1_54, tf2_54, tf1_49, tf2_49)  [corrected sol-round6 1.3 map].
  D  per fiber (Pool): fold bands 6..24 mod p (PIN42 monomials dropped
     = the chart), 22-pivot at-use cascade -> resolved solved forms
     (G1 unit-ness at use), compat rows L10.b22 -> pivot-substituted ->
     NF -> affine split in the level-44 tails -> rank-2 gate -> RREF of
     {u.b} == banked atlas g rows (exact), unit 2x2 solve of
     (tg1_44, tg2_44); compat-closure NF == 0 (Row 22 adds nothing to
     I23); Row-22 rank-4 deep solve; the five Schur residuals
     c_nu = L24.b24 with the DAG substituted ONLY into these rows
     (spec 2.5), coefficientwise NF through the cached 509-el det23
     G23 of the fiber, membership traces saved; forward-inclusion gate
     NF(26 core rows + 3 g rows) == 0; numeric Schur check.
  E  witness-truncation regression (a00pp, banked witness JSONs): all
     folded band 6..22 rows vanish at every banked witness x band draw
     x kernel draw (corrected deep-label involution), and bands <= 22
     carry NO new-at-D25 variables (D23-truncation is trivial).
  F  shape census (22+r vars / 29+s eqs vs spec), component masks,
     interpolation of every coefficient through the 36-point radical
     algebra (evaluation/interpolation round-trip gate), emission of
     ONE union .ms per prime (+ 36 parked per-fiber .ms) per AUDIT.md
     rules (expanded/paren-free, coeffs in [0,p), independent-parser
     round trip, satisfiability smoke), manifest JSON.

STOP DISCIPLINE: every gate is a hard assert with a GATE- label; a
material shape disagreement vs the sol-round6 predictions surfaces as
StopReport/AssertionError, halts the run, and is logged -- never
silently absorbed.

Usage:  d25_assemble.py <prime> [--workers N] [--fibers a,b]
                        [--skip-emit]
Inputs (box01 layout, override root with env D25_ROOT):
  <root>/d25/directionb_tails_D25.pkl        jets bank
  <root>/d25/gbcache_p<P>_<label>.pkl        parsed 509-el det23 GBs
  <root>/d25/d23_atlas_p<P>.json             fiber values + g rows + md5s
  <root>/d25/d23_witnesses_p<P>.json         banked D23 witnesses (a00pp)
  <root>/atlas/fib_<label>_p<P>.ms           26-row D21 core per fiber
  <root>/d25/fib_a00pp_p<P>.ms               banked a00pp core (shipped)
Outputs:
  <root>/d25/asm/asm_p<P>_<label>.pkl        per-fiber checkpoint
  <root>/d25/asm/asmB_p<P>.pkl               C24/L24/C10/L10 state
  <root>/d25fam/d25fam_p<P>.ms               THE union emission
  <root>/d25fam/d25fam_p<P>_<label>.ms       36 parked specializations
  <root>/d25fam/asm_manifest_p<P>.json       manifest + gate record
  <root>/d25/asm_p<P>.log                    progress log
"""
import argparse
import hashlib
import json
import os
import pickle
import socket
import sys
import time
import zlib
from fractions import Fraction
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import d25_reduce as DR                     # ring/GB/NF machinery (gated)

P22 = DR.GBVARS                             # the 22 det23 base variables
NV, SH, IW1, IW2 = DR.NV, DR.SH, DR.IW1, DR.IW2
IUW1, IUW2 = NV - 2, NV - 1
pack, unpack, degof = DR.pack, DR.unpack, DR.degof
nf_trace = DR.nf_trace

# ---------------------------------------------------------------- registry
# x-registry <-> tail names (directionb_tails_D21.pkl vars_ x
# directionb_residual32_emit.load_rows names; extracted this session
# from the frozen banked artifacts).
X2T = {"x0": "tf1_43", "x1": "tf1_44", "x2": "tf1_45", "x3": "tf1_46",
       "x4": "tf1_47", "x5": "tf1_48", "x6": "tf1_50", "x7": "tf1_52",
       "x8": "tf2_43", "x9": "tf2_44", "x10": "tf2_45", "x11": "tf2_46",
       "x12": "tf2_47", "x13": "tf2_48", "x14": "tf2_50", "x15": "tf2_52",
       "x16": "tg1_43", "x17": "tg1_44", "x18": "tg1_45", "x19": "tg1_46",
       "x20": "tg1_47", "x21": "tg1_48", "x22": "tg1_50", "x23": "tg1_52",
       "x24": "tg2_43", "x25": "tg2_44", "x26": "tg2_45", "x27": "tg2_46",
       "x28": "tg2_47", "x29": "tg2_48", "x30": "tg2_50", "x31": "tg2_52",
       "x32": "tg01_44", "x33": "tg01_46", "x34": "tg01_48",
       "x35": "tg01_50", "x36": "tg01_52", "x37": "tg02_44",
       "x38": "tg02_46", "x39": "tg02_48", "x40": "tg02_50",
       "x41": "tg02_52", "x42": "tf1_38", "x43": "tf1_39", "x44": "tf1_40",
       "x45": "tf1_41", "x46": "tf1_42", "x47": "tf2_38", "x48": "tf2_39",
       "x49": "tf2_40", "x50": "tf2_41", "x51": "tf2_42", "x52": "tg1_38",
       "x53": "tg1_39", "x54": "tg1_40", "x55": "tg1_41", "x56": "tg1_42",
       "x57": "tg2_38", "x58": "tg2_39", "x59": "tg2_40", "x60": "tg2_41",
       "x61": "tg2_42", "x62": "tg01_38", "x63": "tg01_40",
       "x64": "tg01_42", "x65": "tg02_38", "x66": "tg02_40",
       "x67": "tg02_42", "x68": "uf18", "x69": "uf24", "x70": "vf1_34",
       "x71": "vf1_36", "x72": "vf2_34", "x73": "vf2_36"}

FRONTIER = list(DR.FRONTIER)                # 10, sol-round6 2.3 order
# sol-round6 (2): diag = (A1W1, A1^2, A2W2, A2^2, A1HW1, A1^2, A2HW2,
# A2^2, A1^2, A2^2) positionally against FRONTIER.  Radkeys
# (za,e1,e2,pw,h1,qw,h2,eB); HW_i^h folds as hw_i^h W_i^h.
DIAG24 = [(0, 1, 0, 1, 0, 0, 0, 0), (0, 2, 0, 0, 0, 0, 0, 0),
          (0, 0, 1, 0, 0, 1, 0, 0), (0, 0, 2, 0, 0, 0, 0, 0),
          (0, 1, 0, 0, 1, 0, 0, 0), (0, 2, 0, 0, 0, 0, 0, 0),
          (0, 0, 1, 0, 0, 0, 1, 0), (0, 0, 2, 0, 0, 0, 0, 0),
          (0, 2, 0, 0, 0, 0, 0, 0), (0, 0, 2, 0, 0, 0, 0, 0)]

DEEP10 = ["tg02_54", "tg01_54", "tg2_49", "tg1_49",      # SOLVED (1.3)
          "tg1_54", "tg2_54", "tf1_54", "tf2_54", "tf1_49", "tf2_49"]
NSOLVED = 4
L44 = ["tg1_44", "tg2_44", "tg01_44", "tg02_44"]         # x17,x25,x32,x37
L44_SOLVE = ["tg1_44", "tg2_44"]                         # x17, x25
PIN42 = {"tf1_42", "tf2_42", "tg1_42", "tg2_42", "tg01_42", "tg02_42"}
# 22 pivots: at-use order (banked witness JSON pivot_order_at_use mapped
# through the registry) with their window-row labels (band, eta) from
# cases/directionb_core23_elim.py PIV22.
PIVROW = {"tf1_44": (12, 2), "tf2_44": (12, 5), "tf1_46": (14, 0),
          "tf2_46": (14, 3), "tf1_43": (16, 1), "tf1_48": (16, 4),
          "tf2_43": (16, 7), "tf2_48": (16, 10), "tf1_45": (18, 2),
          "tf1_50": (18, 5), "tf2_45": (18, 8), "tf2_50": (18, 11),
          "tf1_47": (20, 0), "tf1_52": (20, 3), "tf2_47": (20, 6),
          "tf2_52": (20, 9), "tf1_38": (6, 2), "tf1_40": (8, 0),
          "tf2_40": (8, 3), "tf1_39": (12, 8), "tf1_41": (14, 6),
          "tf2_41": (14, 9)}
ATUSE = ["tf1_38", "tf1_40", "tf2_40", "tf1_44", "tf2_44", "tf1_46",
         "tf2_46", "tf1_43", "tf1_48", "tf2_43", "tf2_48", "tf1_45",
         "tf1_50", "tf2_45", "tf2_50", "tf1_47", "tf1_52", "tf2_47",
         "tf2_52", "tf1_39", "tf1_41", "tf2_41"]
assert sorted(ATUSE) == sorted(PIVROW) and len(ATUSE) == 22
# corrected deep-label involution (sol-round6 1.3): old emission name <->
# true stream name; the banked witness deep_draws use the OLD names.
INVOL = {"tf1_49": "tg1_49", "tg1_49": "tf1_49", "tf2_49": "tg2_49",
         "tg2_49": "tf2_49", "tf1_54": "tg02_54", "tg02_54": "tf1_54",
         "tf2_54": "tg01_54", "tg01_54": "tf2_54", "tg1_54": "tg2_54",
         "tg2_54": "tg1_54"}

# emission aliases (msolve-safe, no underscores): the D21 x-registry,
# the CORRECTED x74..x83 deep registry (sol-round6 1.3), x90 = uf30.
T2X = {v: k for k, v in X2T.items()}
XALIAS = dict(T2X)
XALIAS.update({"tg02_54": "x74", "tg01_54": "x75", "tg2_54": "x76",
               "tg2_49": "x77", "tg1_54": "x78", "tg1_49": "x79",
               "tf2_54": "x80", "tf2_49": "x81", "tf1_54": "x82",
               "tf1_49": "x83", "uf30": "x90"})

TERM_WARN, TERM_STOP = 100000, 250000       # sol-round6 2.6 engineering
BANKED90 = "ab5ee038b118ba6d0b6303c6b2b55b110dc9872c203e1c6b2d60044458e69d29"

G_ROOT = os.environ.get("D25_ROOT", os.path.expanduser("~/jc72108"))


class StopReport(Exception):
    """Material disagreement with the sol-round6 predictions."""


# ------------------------------------------------------------ ext ring ops
# Extended-ring polynomial: dict {(s22, lift): coeff}; s22 = packed
# 22-var exponent int (d25_reduce encoding); lift = tuple of sorted
# (tailname, exp) over the lift/deep variables.

def lift_mul(a, b):
    if not a: return b
    if not b: return a
    d = dict(a)
    for nm, e in b:
        d[nm] = d.get(nm, 0) + e
    return tuple(sorted(d.items()))


def wcancel(s):
    """uW_i*W_i == 1 mod I23 (chart saturation): cancel mixed pairs."""
    e = None
    a = min((s >> (SH * IW1)) & 0xFF, (s >> (SH * IUW1)) & 0xFF)
    b = min((s >> (SH * IW2)) & 0xFF, (s >> (SH * IUW2)) & 0xFF)
    if not (a or b):
        return s
    e = list(unpack(s))
    e[IW1] -= a; e[IUW1] -= a; e[IW2] -= b; e[IUW2] -= b
    return pack(e)


def ext_add(dst, src, p, scale=1):
    for k, c in src.items():
        nc = (dst.get(k, 0) + scale * c) % p
        if nc: dst[k] = nc
        else: dst.pop(k, None)
    return dst


def ext_mul(a, b, p):
    out = {}
    if len(a) > len(b):
        a, b = b, a
    for (sa, la), ca in a.items():
        for (sb, lb), cb in b.items():
            k = (wcancel(sa + sb), lift_mul(la, lb))
            nc = (out.get(k, 0) + ca * cb) % p
            if nc: out[k] = nc
            else: out.pop(k, None)
    return out


def ext_nf(poly, gb, p, want_trace=False):
    """Coefficientwise NF: group by lift monomial, reduce the 22-var
    part through the fiber GB."""
    bylift = {}
    for (s, l), c in poly.items():
        bylift.setdefault(l, {})[s] = c
    out, traces = {}, {}
    for l, zpoly in bylift.items():
        nf, tr, _ = nf_trace(zpoly, gb, p)
        for s, c in nf.items():
            out[(s, l)] = c
        if want_trace and tr:
            traces[l] = tr
    return out, (traces if want_trace else None)


def ext_subst(poly, forms, p, gb=None, cap=TERM_STOP):
    """Substitute solved variables (forms: name -> RESOLVED ext poly,
    free of solved names) into poly; optional final NF."""
    out = {}
    for (s, l), c in poly.items():
        base = {(s, ()): c}
        freel = []
        for nm, e in l:
            if nm in forms:
                for _ in range(e):
                    base = ext_mul(base, forms[nm], p)
                    if len(base) > cap:
                        raise StopReport("term cap %d exceeded in subst"
                                         % cap)
            else:
                freel.append((nm, e))
        freel = tuple(sorted(freel))
        for (s2, l2), c2 in base.items():
            k = (s2, lift_mul(l2, freel))
            nc = (out.get(k, 0) + c2) % p
            if nc: out[k] = nc
            else: out.pop(k, None)
        if gb is not None and len(out) > 150000:
            out, _ = ext_nf(out, gb, p)      # interim reduction
        if len(out) > 4 * cap:
            raise StopReport("accumulated term cap exceeded in subst")
    if gb is not None:
        out, _ = ext_nf(out, gb, p)
    return out


def ext_eval(poly, val, p):
    tot = 0
    for (s, l), c in poly.items():
        m = c
        e = unpack(s)
        for i, ei in enumerate(e):
            if ei:
                m = m * pow(val[P22[i]], ei, p) % p
        for nm, ei in l:
            m = m * pow(val[nm], ei, p) % p
        tot = (tot + m) % p
    return tot


def inv_monomial(s):
    """Invert a pure W/uW monomial on the chart (W <-> uW swap)."""
    e = list(unpack(s))
    assert all(x == 0 for i, x in enumerate(e)
               if i not in (IW1, IW2, IUW1, IUW2)), \
        "inv_monomial: not a W-monomial"
    em = [0] * NV
    em[IUW1], em[IW1] = e[IW1], e[IUW1]
    em[IUW2], em[IW2] = e[IW2], e[IUW2]
    return pack(em)


def mono_scale(poly, s_mono, cscale, p):
    return {(wcancel(s + s_mono), l): c * cscale % p
            for (s, l), c in poly.items()}


# ------------------------------------------------------------- bank folding
def fold_cell(vex, vars_, fv, r3v, p, pinstats=None):
    """One bank cell -> ext poly mod p at the fiber (PIN42 dropped)."""
    A1, A2 = fv["A1"], fv["A2"]
    hw1, hw2 = fv["HW1_over_W1"], fv["HW2_over_W2"]
    out = {}
    for key, r in vex.items():
        epos = [0] * NV
        lift = {}
        pinned = False
        for i in key:
            nm = vars_[i]
            if nm in PIN42:
                pinned = True
                break
            if nm in DR.BASE18:
                epos[DR.TAIL2POS[nm]] += 1
            else:
                lift[nm] = lift.get(nm, 0) + 1
        if pinned:
            if pinstats is not None:
                pinstats[0] += 1
            continue
        lt = tuple(sorted(lift.items()))
        for (za, e1, e2, pw, h1, qw, h2, eB), c in r.items():
            assert za == 0 and eB == 0, "unexpected za/eB in bank"
            c0, c1 = Fraction(c[0]), Fraction(c[1])
            cm = (c0.numerator % p * pow(c0.denominator % p, p - 2, p)
                  + c1.numerator % p * pow(c1.denominator % p, p - 2, p)
                  * r3v) % p
            cm = cm * pow(A1, e1, p) % p * pow(A2, e2, p) % p
            cm = cm * pow(hw1, h1, p) % p * pow(hw2, h2, p) % p
            if not cm:
                continue
            e = list(epos)
            e[IW1] += pw + h1
            e[IW2] += qw + h2
            k = (pack(e), lt)
            nc = (out.get(k, 0) + cm) % p
            if nc: out[k] = nc
            else: out.pop(k, None)
    return out


def add_nolog_pin(rows, p):
    """The jets bank omits the +42 t^20 no-log pin constant (the
    Keller action residue; sol-round5 E-object '+ 42 t^20').  Verified
    this session: the folded bank cell (20,0) at a00pp/p105337 equals
    the frozen core23 pristine pivot row (20,0) dict-exactly at scale
    1 EXCEPT for the bare constant 42.  Restore it (fiber-independent)."""
    k = (0, ())
    row = rows[(20, 0)]
    row[k] = (row.get(k, 0) + 42) % p
    if not row[k]:
        del row[k]


def fold_radmono(rk, fv, p):
    """radkey -> (packed W-monomial, scalar) at the fiber."""
    za, e1, e2, pw, h1, qw, h2, eB = rk
    assert za == 0 and eB == 0
    c = pow(fv["A1"], e1, p) * pow(fv["A2"], e2, p) % p
    c = c * pow(fv["HW1_over_W1"], h1, p) % p \
        * pow(fv["HW2_over_W2"], h2, p) % p
    e = [0] * NV
    e[IW1] = pw + h1
    e[IW2] = qw + h2
    return pack(e), c


def frac_mod(c, r3v, p):
    c0, c1 = Fraction(c[0]), Fraction(c[1])
    return (c0.numerator % p * pow(c0.denominator % p, p - 2, p)
            + c1.numerator % p * pow(c1.denominator % p, p - 2, p)
            * r3v) % p


# ------------------------------------------------------------ linear algebra
def rref_full(M, p):
    """Deterministic Gauss-Jordan: scan columns left->right, pick the
    topmost unused row with a nonzero entry.  Returns (rows-in-pivot-
    order, pivot_cols, rank); non-pivot rows are dropped."""
    n = len(M)
    m = len(M[0]) if n else 0
    A = [list(r) for r in M]
    piv, used = [], []
    for col in range(m):
        sel = next((r for r in range(n)
                    if r not in used and A[r][col] % p), None)
        if sel is None:
            continue
        used.append(sel); piv.append(col)
        inv = pow(A[sel][col], p - 2, p)
        A[sel] = [x * inv % p for x in A[sel]]
        for r in range(n):
            if r != sel and A[r][col] % p:
                f = A[r][col]
                A[r] = [(x - f * y) % p for x, y in zip(A[r], A[sel])]
    return [A[r] for r in used], piv, len(piv)


def rref_leftkernel(M, p):
    """(rank, pivot_cols, kernel_rows): kernel = canonical RREF basis
    of the left null space, via row-reducing [M | I]."""
    n = len(M)
    m = len(M[0]) if n else 0
    A = [list(M[i]) + [1 if j == i else 0 for j in range(n)]
         for i in range(n)]
    piv, used = [], set()
    for col in range(m):
        sel = next((r for r in range(n)
                    if r not in used and A[r][col] % p), None)
        if sel is None:
            continue
        used.add(sel); piv.append(col)
        inv = pow(A[sel][col], p - 2, p)
        A[sel] = [x * inv % p for x in A[sel]]
        for r in range(n):
            if r != sel and A[r][col] % p:
                f = A[r][col]
                A[r] = [(x - f * y) % p for x, y in zip(A[r], A[sel])]
    ker = [A[r][m:] for r in range(n) if r not in used]
    if ker:
        ker, _, _ = rref_full(ker, p)
    return len(piv), piv, ker


def mat_inv(M, p):
    n = len(M)
    A = [list(M[i]) + [1 if j == i else 0 for j in range(n)]
         for i in range(n)]
    for col in range(n):
        sel = next(r for r in range(col, n) if A[r][col] % p)
        A[col], A[sel] = A[sel], A[col]
        inv = pow(A[col][col], p - 2, p)
        A[col] = [x * inv % p for x in A[col]]
        for r in range(n):
            if r != col and A[r][col] % p:
                f = A[r][col]
                A[r] = [(x - f * y) % p for x, y in zip(A[r], A[col])]
    return [row[n:] for row in A]


def rref_poly_rows(rows, p):
    """RREF a list of packed z-poly dicts as vectors over the union
    support (deterministic grevlex-descending column order)."""
    sup = sorted({s for d in rows for s in d},
                 key=lambda s: -DR.gkey(s, degof(s)))
    M = [[d.get(s, 0) for s in sup] for d in rows]
    R, piv, rank = rref_full(M, p)
    return [{sup[i]: c for i, c in enumerate(r) if c} for r in R], rank


# --------------------------------------------------- radkey-level phase B/C
def lift_of_key(key, vars_):
    lift = {}
    for i in key:
        nm = vars_[i]
        if nm not in DR.BASE18:
            lift[nm] = lift.get(nm, 0) + 1
    return tuple(sorted(lift.items()))


def base_part_nonzero(key, vars_):
    return any(vars_[i] in DR.BASE18 for i in key)


def phaseB(byk, vars_, p, r3v, log):
    """Row-24 frontier census, digest, factorization (2), C24, L24."""
    etas = sorted(byk[24])
    assert etas == [2, 5, 8, 11, 14, 17, 20, 23, 26], "GATE-B0 eta support"
    entries = {}
    serial = []
    for q in etas:
        cell = byk[24][q]
        bykey = {}
        for key, r in cell.items():
            lt = lift_of_key(key, vars_)
            fr = [nm for nm, _ in lt if nm in DR.FRONTIER]
            if not fr:
                continue
            assert lt == ((fr[0], 1),), \
                ("GATE-B1 frontier nonlinearity/mixing", q, lt)
            assert not base_part_nonzero(key, vars_), \
                ("GATE-B1b frontier term carries base vars", q, fr[0])
            bykey.setdefault(fr[0], {}).update(r)
        for fname in FRONTIER:
            ring = bykey.get(fname, {})
            entries[(q, fname)] = ring
            serial.append((q, fname, tuple(sorted(
                (rk, repr(c)) for rk, c in ring.items()))))
    payload = repr(serial).encode()
    digest = hashlib.sha256(payload).hexdigest()
    dig_ok = digest == BANKED90
    log("B: 90-entry first-occurrence digest %s.. len=%d -> %s"
        % (digest[:16], len(payload),
           "MATCH banked ab5ee038" if dig_ok else "MISMATCH (recipe"
           " drift?) -- semantic factorization gates below still bind"))
    # factorization (2): entry(i,j) = C24[i][j]*DIAG24[j]*rowmono_i
    rowex = [None] * 9
    C24 = [[0] * 10 for _ in range(9)]
    for i, q in enumerate(etas):
        for j, fname in enumerate(FRONTIER):
            ring = entries[(q, fname)]
            if not ring:
                continue
            assert len(ring) == 1, ("GATE-B2 multi-radkey A24 entry",
                                    q, fname, len(ring))
            (rk, c), = ring.items()
            ex = tuple(a - b for a, b in zip(rk, DIAG24[j]))
            assert all(x == 0 for xi, x in enumerate(ex)
                       if xi not in (3, 5)) and min(ex[3], ex[5],
                                                    0) == 0, \
                ("GATE-B2 factorization (2) fails", q, fname, rk)
            wmono = (ex[3], ex[5])
            if rowex[i] is None:
                rowex[i] = wmono
            assert rowex[i] == wmono, \
                ("GATE-B2b row W-normalizer not uniform", q, fname,
                 wmono, rowex[i])
            C24[i][j] = frac_mod(c, r3v, p)
    rowex = [x if x is not None else (0, 0) for x in rowex]
    rank, piv, L = rref_leftkernel(C24, p)
    assert rank == 4, ("GATE-B3 rank C24 != 4", rank)
    assert piv == [0, 1, 2, 3], ("GATE-B3 pivot columns", piv)
    assert len(L) == 5, "GATE-B3 left kernel dim != 5"
    for row in L:
        for j in range(10):
            assert sum(row[i] * C24[i][j] for i in range(9)) % p == 0, \
                "GATE-B4 L24 C24 != 0"
    log("B: factorization (2) PASS (row normalizers %s); C24 rank 4 "
        "pivots [0,1,2,3]; L24 = 5x9 canonical RREF left kernel"
        % (rowex,))
    return {"C24": C24, "L24": L, "digest": digest, "digest_ok": dig_ok,
            "etas24": etas, "rowex24": rowex}


def phaseC(byk, vars_, p, r3v, log):
    """Row-22 deep-tail block at radkey level: A22 = C10 diag(u_j)."""
    etas = sorted(byk[22])
    assert etas == [1, 4, 7, 10, 13, 16, 19, 22, 25, 28], "GATE-C0"
    carriers = [None] * 10
    C10 = [[0] * 10 for _ in range(10)]
    for i, q in enumerate(etas):
        cell = byk[22][q]
        bykey = {}
        for key, r in cell.items():
            lt = lift_of_key(key, vars_)
            dp = [nm for nm, _ in lt if nm in DEEP10]
            if not dp:
                continue
            assert lt == ((dp[0], 1),), \
                ("GATE-C1 Row22 not affine in deep tails", q, lt)
            assert not base_part_nonzero(key, vars_), \
                ("GATE-C1b A22 entry carries base vars", q, dp[0])
            bykey.setdefault(dp[0], {}).update(r)
        for nm, ring in bykey.items():
            j = DEEP10.index(nm)
            assert len(ring) == 1, ("GATE-C2 multi-radkey A22 entry",
                                    q, nm, len(ring))
            (rk, c), = ring.items()
            if carriers[j] is None:
                carriers[j] = rk
            assert carriers[j] == rk, \
                ("GATE-C2 column carrier not single", nm, rk,
                 carriers[j])
            C10[i][j] = frac_mod(c, r3v, p)
    assert all(x is not None for x in carriers), \
        ("GATE-C2c empty deep column", carriers)
    rank, piv, L10 = rref_leftkernel(C10, p)
    assert rank == 4, ("GATE-C3 rank C10 != 4", rank)
    assert len(L10) == 6, "GATE-C3 left kernel dim != 6"
    sub = [[C10[i][j] for j in range(NSOLVED)] for i in range(10)]
    _, _, r4 = rref_full(sub, p)
    assert r4 == 4, "GATE-C4 solved-4 columns rank != 4"
    log("C: A22 = C10 diag(u) PASS; rank C10 = 4; solved-4 %s rank 4"
        % (DEEP10[:NSOLVED],))
    return {"C10": C10, "L10": L10, "carriers": carriers,
            "etas22": etas}


# ------------------------------------------------------------ .ms parsing
def parse_ms(path, p, expect_vars=None):
    lines = open(path).read().split("\n")
    hdr = [h.strip() for h in lines[0].split(",")]
    assert int(lines[1]) == p, (path, lines[1])
    if expect_vars is not None:
        assert hdr == expect_vars, ("var order mismatch", path, hdr)
    body = "\n".join(lines[2:])
    rows = [r.strip().rstrip(",") for r in body.split(",\n")
            if r.strip()]
    vi = {v: i for i, v in enumerate(hdr)}
    out = []
    for row in rows:
        d = {}
        for t in row.split("+"):
            fs = t.strip().split("*")
            try:
                c = int(fs[0]); fs = fs[1:]
            except ValueError:
                c = 1
            e = [0] * len(hdr)
            for f in fs:
                if "^" in f:
                    nm, ex = f.split("^")
                    e[vi[nm]] += int(ex)
                else:
                    e[vi[f]] += 1
            k = pack(e) if hdr == P22 else tuple(e)
            d[k] = (d.get(k, 0) + c) % p
        out.append({k: c for k, c in d.items() if c})
    return out


def parse_grow(row_str, p):
    """Atlas JSON g-row string (x-name space, the 22 vars) -> packed."""
    vi = {v: i for i, v in enumerate(P22)}
    d = {}
    for t in row_str.split("+"):
        fs = t.strip().split("*")
        c = int(fs[0]) % p
        e = [0] * NV
        for f in fs[1:]:
            if "^" in f:
                nm, ex = f.split("^")
                e[vi[nm]] += int(ex)
            else:
                e[vi[f]] += 1
        k = pack(e)
        d[k] = (d.get(k, 0) + c) % p
    return {k: c for k, c in d.items() if c}


# --------------------------------------------------------------- worker
G = {}


def _init(shared):
    G.update(shared)


def fiber_task(lab):
    t0 = time.time()
    p = G["p"]
    path = os.path.join(G["asmdir"], "asm_p%d_%s.pkl" % (p, lab))
    if os.path.exists(path):
        return lab, "skip", 0.0
    try:
        payload = assemble_fiber(lab)
    except (StopReport, AssertionError) as e:
        return lab, "STOP: %r" % (e,), time.time() - t0
    tmp = path + ".tmp.%d" % os.getpid()
    with open(tmp, "wb") as fh:
        pickle.dump(payload, fh, protocol=4)
    os.replace(tmp, path)
    return lab, "done", time.time() - t0


def subst_atuse(row, forms, p, cap=4 * TERM_STOP):
    """Substitute (possibly unresolved) forms into a row, any power."""
    out = {}
    for (s, l), c in row.items():
        base = {(s, ()): c}
        freel = []
        for nm, e in l:
            if nm in forms:
                for _ in range(e):
                    base = ext_mul(base, forms[nm], p)
            else:
                freel.append((nm, e))
        if len(base) > cap:
            raise StopReport("cascade term cap exceeded")
        freel = tuple(sorted(freel))
        for (s2, l2), c2 in base.items():
            k = (s2, lift_mul(l2, freel))
            nc = (out.get(k, 0) + c2) % p
            if nc: out[k] = nc
            else: out.pop(k, None)
    return out


def assemble_fiber(lab):
    p, r3v = G["p"], G["r3"]
    fv = G["fvals"][lab]
    gb = G["gbs"][lab]
    vars_, byk = G["vars"], G["byk"]
    B = G["B"]
    L10, L24, C10 = B["L10"], B["L24"], B["C10"]
    carriers = B["carriers"]
    etas22, etas24 = B["etas22"], B["etas24"]
    gates = {}
    pinstats = [0]

    # ---- fold all bands
    rows = {}
    for k in sorted(byk):
        for n in byk[k]:
            rows[(k, n)] = fold_cell(byk[k][n], vars_, fv, r3v, p,
                                     pinstats)
    add_nolog_pin(rows, p)
    gates["pin42_dropped_monomials"] = pinstats[0]

    # ---- forward inclusion: NF(core rows + g rows) == 0
    for i, d in enumerate(G["core_rows"][lab]):
        nf, _, _ = nf_trace(dict(d), gb, p)
        assert not nf, ("GATE-D0 core row not in I23", lab, i)
    bank_g = [parse_grow(s, p) for s in G["atlas"][lab]["g_rows"]]
    for i, d in enumerate(bank_g):
        nf, _, _ = nf_trace(dict(d), gb, p)
        assert not nf, ("GATE-D0 g row not in I23", lab, i)
    gates["forward_inclusion"] = "PASS 29/29"

    # ---- 22-pivot cascade: TRUE forward elimination (working rows
    # updated at every step, NF after every update -- the full_point /
    # 8.S4 discipline) followed by one reverse back-substitution pass.
    work = {nm: dict(rows[PIVROW[nm]]) for nm in ATUSE}
    forms = {}
    for ki, nm in enumerate(ATUSE):
        row = work.pop(nm)
        coefpoly, rest = {}, {}
        maxdeg = 0
        for (s, l), c in row.items():
            e = dict(l).get(nm, 0)
            maxdeg = max(maxdeg, e)
            if e == 0:
                rest[(s, l)] = c
            else:
                l2 = tuple(sorted((n2, e2) for n2, e2 in l
                                  if n2 != nm))
                k = (s, l2)
                coefpoly[k] = (coefpoly.get(k, 0) + c) % p
        coefpoly = {k: c for k, c in coefpoly.items() if c}
        assert maxdeg == 1, ("GATE-D1 pivot row nonlinear at use",
                             lab, nm, maxdeg)
        assert len(coefpoly) == 1, ("GATE-D1 pivot coeff not a single"
                                    " monomial", lab, nm,
                                    len(coefpoly))
        (s, l), = coefpoly.keys()
        assert l == (), ("GATE-D1 pivot coeff carries lift vars",
                         lab, nm)
        c = coefpoly[(s, l)]
        sm = inv_monomial(s)                 # asserts W-monomial
        form = mono_scale(rest, sm, (p - 1) * pow(c, p - 2, p) % p, p)
        form, _ = ext_nf(form, gb, p)
        forms[nm] = form
        one = {nm: form}
        for nm2 in ATUSE[ki + 1:]:
            if any(n2 == nm for (s2, l2) in work[nm2]
                   for n2, _ in l2):
                w2 = subst_atuse(work[nm2], one, p)
                w2, _ = ext_nf(w2, gb, p)
                work[nm2] = w2
    for nm in reversed(ATUSE):               # back-substitution
        f = forms[nm]
        need = {n2 for (s2, l2) in f for n2, _ in l2 if n2 in PIVROW}
        if need:
            f = subst_atuse(f, {n2: forms[n2] for n2 in need}, p)
            f, _ = ext_nf(f, gb, p)
            forms[nm] = f
    for nm in ATUSE:
        assert not any(n2 in PIVROW for (s2, l2) in forms[nm]
                       for n2, _ in l2), \
            ("GATE-D1c unresolved pivot", lab, nm)
    gates["cascade_form_terms"] = {nm: len(forms[nm]) for nm in ATUSE}

    # ---- Row-22 b-part (deep-tail terms removed)
    b22 = []
    for q in etas22:
        row = {k: c for k, c in rows[(22, q)].items()
               if not any(n2 in DEEP10 for n2, _ in k[1])}
        b22.append(row)

    # ---- compat rows L10 . b22 (pivot-substituted, NF'd)
    compat = []
    b22sub = [None] * 10
    for r6 in range(6):
        acc = {}
        for i in range(10):
            if L10[r6][i]:
                if b22sub[i] is None:
                    b22sub[i] = ext_subst(b22[i], forms, p, gb=gb)
                ext_add(acc, b22sub[i], p, L10[r6][i])
        compat.append(acc)
    # affine split in the level-44 tails
    C44 = [[0] * 4 for _ in range(6)]
    b44 = []
    carriers44 = [None] * 4
    for r6, row in enumerate(compat):
        rest = {}
        for (s, l), c in row.items():
            names = [n2 for n2, _ in l]
            if any(n2 in L44 for n2 in names):
                assert len(l) == 1 and l[0][1] == 1 and l[0][0] in L44, \
                    ("GATE-D2 compat not affine in level-44", lab, r6,
                     l)
                j = L44.index(l[0][0])
                if carriers44[j] is None:
                    carriers44[j] = s
                assert carriers44[j] == s, \
                    ("GATE-D2 level-44 carrier not single", lab, r6, j)
                assert C44[r6][j] == 0, "GATE-D2 dup entry"
                C44[r6][j] = c
            else:
                assert not l, ("GATE-D2b compat carries other lift "
                               "vars", lab, r6, l)
                rest[s] = c
        b44.append(rest)
    rank2, piv2, ker4 = rref_leftkernel(C44, p)
    assert rank2 == 2, ("GATE-D3 rank C44 != 2", lab, rank2)
    assert len(ker4) == 4, "GATE-D3 leftker dim != 4"
    assert piv2 == [0, 1], ("GATE-D3 level-44 pivot cols", lab, piv2)
    # kernel compat closure: u.b44 is a linear combination of normal
    # forms (hence itself a normal form); membership u.b44 in I23 --
    # the D23 g-content is already inside the det23 GB, so the normal
    # form must be EXACTLY ZERO.  (The direct g-row reproduction is
    # banked at the atlas tier, 8.S8, both primes; here g in I23 is
    # separately certified by GATE-D0.)
    for ui, u in enumerate(ker4):
        acc = {}
        for i in range(6):
            if u[i]:
                for s, c in b44[i].items():
                    nc = (acc.get(s, 0) + u[i] * c) % p
                    if nc: acc[s] = nc
                    else: acc.pop(s, None)
        assert not acc, ("GATE-D4 Row-22 kernel compat not closed "
                         "mod I23", lab, ui, len(acc))
    gates["kernel_compat"] = "PASS 4/4 u.b44 == 0 mod I23"

    # ---- unit 2x2 solve of (tg1_44, tg2_44); (tg01_44, tg02_44) free
    R2 = None
    for i in range(6):
        if R2: break
        for j in range(i + 1, 6):
            if (C44[i][0] * C44[j][1] - C44[i][1] * C44[j][0]) % p:
                R2 = (i, j); break
    assert R2, ("GATE-D5 no invertible 2x2 minor on (tg1_44, tg2_44)",
                lab)
    a_, b_, c_, d_ = (C44[R2[0]][0], C44[R2[0]][1],
                      C44[R2[1]][0], C44[R2[1]][1])
    idet = pow((a_ * d_ - b_ * c_) % p, p - 2, p)
    inv2 = [[d_ * idet % p, (p - b_) * idet % p],
            [(p - c_) * idet % p, a_ * idet % p]]
    l44forms = {}
    for t in range(2):
        icar = inv_monomial(carriers44[t])
        acc = {}
        for u in range(2):
            r6 = R2[u]
            coef = (p - inv2[t][u]) % p
            for s, c in b44[r6].items():           # b-part
                k = (wcancel(s + icar), ())
                nc = (acc.get(k, 0) + coef * c) % p
                if nc: acc[k] = nc
                else: acc.pop(k, None)
            for j in (2, 3):                        # free tg01/tg02_44
                if C44[r6][j]:
                    k = (wcancel(carriers44[j] + icar), ((L44[j], 1),))
                    nc = (acc.get(k, 0) + coef * C44[r6][j]) % p
                    if nc: acc[k] = nc
                    else: acc.pop(k, None)
        acc, _ = ext_nf(acc, gb, p)
        l44forms[L44_SOLVE[t]] = acc
    # compat closure: all 6 compat rows -> 0 after the l44 solve
    for r6, row in enumerate(compat):
        chk = ext_subst(row, l44forms, p, gb=gb)
        assert not chk, ("GATE-D6 compat closure fails (Row 22 adds "
                         "content beyond I23)", lab, r6, len(chk))
    gates["compat_closure"] = "PASS 6/6 == 0 mod I23"

    # ---- resolve level-44 inside the cascade forms; merge
    for nm in ATUSE:
        forms[nm] = ext_subst(forms[nm], l44forms, p, gb=gb)
    forms.update(l44forms)

    # ---- Row-22 rank-4 deep solve (solved-4 via kernel-6)
    R4, have = [], []
    for i in range(10):
        cand = have + [[C10[i][j] for j in range(NSOLVED)]]
        _, _, rk = rref_full(cand, p)
        if rk > len(have):
            have = cand; R4.append(i)
        if len(R4) == 4:
            break
    assert len(R4) == 4, ("GATE-D7 solved-4 rows", lab)
    Minv = mat_inv([[C10[i][j] for j in range(NSOLVED)] for i in R4],
                   p)
    browR = {i: ext_subst(b22[i], forms, p, gb=gb) for i in R4}
    deepforms = {}
    for t in range(NSOLVED):
        acc = {}
        for u in range(4):
            i = R4[u]
            coef = (p - Minv[t][u]) % p
            ext_add(acc, browR[i], p, coef)
            for j in range(NSOLVED, 10):
                if C10[i][j]:
                    sm, cf = fold_radmono(carriers[j], fv, p)
                    k = (sm, ((DEEP10[j], 1),))
                    nc = (acc.get(k, 0) + coef * C10[i][j] * cf) % p
                    if nc: acc[k] = nc
                    else: acc.pop(k, None)
        sm, cf = fold_radmono(carriers[t], fv, p)
        acc = mono_scale(acc, inv_monomial(sm), pow(cf, p - 2, p), p)
        acc, _ = ext_nf(acc, gb, p)
        deepforms[DEEP10[t]] = acc
    forms.update(deepforms)
    gates["deep_solve_terms"] = {nm: len(deepforms[nm])
                                 for nm in DEEP10[:NSOLVED]}

    # ---- the five Schur residuals c_nu = L24 . b24 (DAG substituted)
    rowex = B["rowex24"]
    b24 = []
    for i, q in enumerate(etas24):
        row = {k: c for k, c in rows[(24, q)].items()
               if not any(n2 in DR.FRONTIER for n2, _ in k[1])}
        if rowex[i] != (0, 0):               # strip the row normalizer
            e = [0] * NV
            e[IUW1], e[IUW2] = rowex[i]
            row = mono_scale(row, pack(e), 1, p)
        b24.append(row)
    residuals, traces = [], []
    for nu in range(5):
        acc = {}
        for i in range(9):
            if L24[nu][i]:
                ext_add(acc, b24[i], p, L24[nu][i])
        raw = dict(acc)
        acc = ext_subst(acc, forms, p, gb=gb)
        # membership data for identity (5): trace of the raw L24.b24
        # combination against the fiber GB (pre-DAG part); the per-
        # alpha traces live in the banked d25_reduce checkpoints and
        # the DAG replay is this committed script.
        _, tr = ext_nf(raw, gb, p, want_trace=True)
        residuals.append(acc)
        traces.append(tr)
    mx = max((len(r) for r in residuals), default=0)
    if mx > TERM_WARN:
        gates["residual_warn"] = "max residual %d terms > %d" \
            % (mx, TERM_WARN)

    # ---- numeric Schur check: L24 kills the frontier block of the
    # FOLDED rows (not only the radkey-level A24) at random points
    import random
    rng = random.Random(20260819)
    ok = 0
    for _ in range(2):
        val = {}
        for i, nm2 in enumerate(P22):
            val[nm2] = rng.randrange(1, p)
        val["uW1"] = pow(val["W1"], p - 2, p)
        val["uW2"] = pow(val["W2"], p - 2, p)
        names = {n2 for (k, n) in rows for (s, l) in rows[(k, n)]
                 for n2, _ in l}
        for n2 in names:
            val[n2] = rng.randrange(0, p)
        F24v, b24v = [], []
        for i, q in enumerate(etas24):
            full = dict(rows[(24, q)])
            if rowex[i] != (0, 0):
                e = [0] * NV
                e[IUW1], e[IUW2] = rowex[i]
                full = mono_scale(full, pack(e), 1, p)
            F24v.append(ext_eval(full, val, p))
            b24v.append(ext_eval(b24[i], val, p))
        lhs = [sum(L24[nu][i] * F24v[i] for i in range(9)) % p
               for nu in range(5)]
        rhs = [sum(L24[nu][i] * b24v[i] for i in range(9)) % p
               for nu in range(5)]
        if lhs == rhs:
            ok += 1
    assert ok == 2, ("GATE-D8 Schur transform does not kill the "
                     "frontier block on folded rows", lab)
    gates["schur_roundtrip"] = "PASS 2/2 random points"

    occ = sorted({n2 for rr in residuals for (s, l) in rr
                  for n2, _ in l})
    return {"label": lab, "prime": p, "residuals": residuals,
            "res_terms": [len(r) for r in residuals],
            "occ_lift": occ, "gates": gates,
            "traces_z": zlib.compress(pickle.dumps(traces, 4), 6),
            "host": socket.gethostname(),
            "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


# ---------------------------------------------------- witness regression
def witness_regression(prime, rows_a00pp, log):
    wpath = os.path.join(G_ROOT, "d25",
                         "d23_witnesses_p%d.json" % prime)
    W = json.load(open(wpath))
    assert W["prime"] == prime
    p = prime
    d23names = set(X2T.values()) | set(DEEP10) | {"W1", "W2", "uW1",
                                                 "uW2"}
    # bands <= 22 must be D23-pure (level-cap structure): no new vars
    for (k, n), row in rows_a00pp.items():
        if k > 22:
            continue
        for (s, l) in row:
            for n2, _ in l:
                assert n2 in d23names, \
                    ("GATE-E0 band<=22 carries new-at-D25 var", k, n,
                     n2)
    # NOTE: the banked deep_draws are Row-22 rank-4 solves ON TOP OF
    # draws[0] (8.S7: "draws[0].witness72 + each recorded deep-kernel
    # draw"), so band-22 rows are checked on draw 0 x 3 kernel draws;
    # bands <= 20 (deep-tail-free -- asserted) on all 3 band draws.
    nrows = ncombo = 0
    for wit in W["witnesses"]:
        for di, draw in enumerate(wit["draws"]):
            val = dict(draw["witness72"])     # x-names (the 22 + W)
            for xn, v in draw["witness72"].items():
                if xn in X2T:
                    val[X2T[xn]] = v          # tail-name aliases
            for nm in PIN42:
                val[nm] = 0
            for (k, n), row in rows_a00pp.items():
                if k > 20:
                    continue
                assert not any(n2 in DEEP10 for (s, l) in row
                               for n2, _ in l), \
                    ("GATE-E0b deep tail below band 22", k, n)
                v = ext_eval(row, val, p)
                nrows += 1
                assert v == 0, \
                    ("GATE-E1 witness fails the D25 system's "
                     "D23-truncation (band<=20)", wit["index"],
                     draw["draw"], (k, n), v)
            ncombo += 1
            if di != 0:
                continue
            for dd in wit["deep_draws"]:
                for nm in DEEP10:
                    val[nm] = dd["deep_tails"][INVOL[nm]]
                for (k, n), row in rows_a00pp.items():
                    if k != 22:
                        continue
                    v = ext_eval(row, val, p)
                    nrows += 1
                    assert v == 0, \
                        ("GATE-E1 witness fails the D25 system's "
                         "D23-truncation (band 22)", wit["index"],
                         dd["kernel_draw"], (k, n), v)
                ncombo += 1
    log("E: witness regression PASS: %d row evaluations == 0 over %d "
        "combos (bands <= 20 x 3 band draws + band 22 x 3 kernel "
        "draws on draw 0); bands <= 22 are D23-pure" % (nrows, ncombo))
    return {"row_evals": nrows, "combos": ncombo, "status": "PASS"}


# ----------------------------------------------------------- emission (F)
def interp_matrix(fvals, p):
    labs = sorted(fvals)
    basis = [(e1, e2, u1, u2) for e1 in range(3) for e2 in range(3)
             for u1 in range(2) for u2 in range(2)]
    M = [[pow(fvals[lb]["A1"], e1, p) * pow(fvals[lb]["A2"], e2, p)
          * pow(fvals[lb]["HW1_over_W1"], u1, p)
          * pow(fvals[lb]["HW2_over_W2"], u2, p) % p
          for (e1, e2, u1, u2) in basis] for lb in labs]
    return labs, basis, mat_inv(M, p)


def interpolate_rows(perfiber, labs, basis, Minv, p):
    """perfiber: {label: extpoly} -> {key: {bexp: c}} over basis."""
    sup = sorted({k for d in perfiber.values() for k in d})
    out = {}
    n = len(labs)
    for k in sup:
        v = [perfiber[lb].get(k, 0) for lb in labs]
        coeffs = [sum(Minv[i][j] * v[j] for j in range(n)) % p
                  for i in range(n)]
        d = {basis[i]: c for i, c in enumerate(coeffs) if c}
        if d:
            out[k] = d
    return out


def eval_interp(urow, fv, p):
    got = {}
    for k, bd in urow.items():
        v = sum(c * pow(fv["A1"], e1, p) * pow(fv["A2"], e2, p)
                * pow(fv["HW1_over_W1"], u1, p)
                * pow(fv["HW2_over_W2"], u2, p)
                for (e1, e2, u1, u2), c in bd.items()) % p
        if v:
            got[k] = v
    return got


SELVARS = ["A1r", "A2r", "h1r", "h2r"]


def mono_str(s22, lift, bexp, hdrpos):
    fs = []
    for nm, ex in lift:
        xn = XALIAS.get(nm, nm)
        fs.append((hdrpos[xn], xn, ex))
    e = unpack(s22)
    for i, ex in enumerate(e):
        if ex:
            fs.append((hdrpos[P22[i]], P22[i], ex))
    if bexp:
        for nm, ex in zip(SELVARS, bexp):
            if ex:
                fs.append((hdrpos[nm], nm, ex))
    fs.sort()
    return "*".join("%s^%d" % (nm, ex) if ex > 1 else nm
                    for _, nm, ex in fs)


def expected_exp_dict(row, hdrpos, nvars, p, interp=False):
    """Row (ext or interp form) -> {exponent-tuple over hdr: coeff},
    for the dict-exact independent-parser round trip."""
    out = {}
    items = ([(s, l, b, c) for (s, l), bd in row.items()
              for b, c in bd.items()] if interp else
             [(s, l, (), c) for (s, l), c in row.items()])
    for s, l, b, c in items:
        e = [0] * nvars
        for nm, ex in l:
            e[hdrpos[XALIAS.get(nm, nm)]] += ex
        for i, ex in enumerate(unpack(s)):
            if ex:
                e[hdrpos[P22[i]]] += ex
        for nm, ex in zip(SELVARS, b):
            if ex:
                e[hdrpos[nm]] += ex
        k = tuple(e)
        nc = (out.get(k, 0) + c) % p
        if nc: out[k] = nc
        else: out.pop(k, None)
    return out


def row_to_txt(row, hdrpos, p, interp=False):
    items = []
    if interp:
        for (s22, lift), bd in row.items():
            for bexp, c in bd.items():
                items.append((s22, lift, bexp, c % p))
    else:
        for (s22, lift), c in row.items():
            items.append((s22, lift, (), c % p))
    items = [t for t in items if t[3]]
    items.sort(key=lambda t: (-(degof(t[0]) + sum(e for _, e in t[1])
                                + sum(t[2])), str((t[0], t[1], t[2]))))
    terms = []
    for s22, lift, bexp, c in items:
        m = mono_str(s22, lift, bexp, hdrpos)
        terms.append("%d*%s" % (c, m) if m else "%d" % c)
    return "+".join(terms) if terms else "0"


def emit_ms(path, hdr, rows_txt, p):
    with open(path + ".tmp", "w") as fh:
        fh.write(", ".join(hdr) + "\n%d\n" % p)
        fh.write(",\n".join(rows_txt) + "\n")
    os.replace(path + ".tmp", path)


def audit_checks(path, p, nrows_expect, nvars_expect, log):
    body = open(path).read()
    assert "(" not in body and ")" not in body, "GATE-F2 parens"
    lines = body.split("\n")
    rows = [r.strip().rstrip(",") for r in "\n".join(lines[2:])
            .split(",\n") if r.strip()]
    assert len(rows) == nrows_expect, \
        ("GATE-F2 row count", len(rows), nrows_expect)
    assert len(lines[0].split(",")) == nvars_expect
    for row in rows:
        allconst = True
        for t in row.split("+"):
            head = t.strip().split("*")[0]
            if head.isdigit():
                assert int(head) < p, ("GATE-F2 coefficient >= p",
                                       head)
            if "*" in t or not head.isdigit():
                allconst = False
        assert not (allconst and row not in ("0",)), \
            "GATE-F2 bare-constant row (unsatisfiable smoke)"
        assert row != "0", "GATE-F2 zero row emitted"
    log("F: AUDIT hygiene PASS on %s (paren-free, coeffs < p, %d "
        "rows, no bare-constant row)" % (os.path.basename(path),
                                         len(rows)))


def emit_all(p, labels, fvals, core_rows, atlasf, results, occ,
             famdir, r3v, manifest, log):
    for nm in occ:
        assert nm in XALIAS, ("GATE-F0 no msolve alias for lift var",
                              nm)
    occx = [XALIAS[nm] for nm in occ]
    assert len(set(occx) & set(P22)) == 0 and len(set(occx)) == len(occ)
    hdr = occx + P22 + SELVARS
    hdrpos = {nm: i for i, nm in enumerate(hdr)}
    labs, basis, Minv = interp_matrix(fvals, p)

    fiber_polys = []                          # (kind, {label: extpoly})
    for i in range(26):
        fiber_polys.append(("core%d" % i,
                            {l: {(s, ()): c for s, c in
                                 core_rows[l][i].items()}
                             for l in labels}))
    for gi in range(3):
        fiber_polys.append(("g%d" % (gi + 1),
                            {l: {(s, ()): c for s, c in
                                 parse_grow(atlasf[l]["g_rows"][gi],
                                            p).items()}
                             for l in labels}))
    for nu in range(5):
        if any(results[l]["residuals"][nu] for l in labels):
            fiber_polys.append(("R%d" % (nu + 1),
                                {l: results[l]["residuals"][nu]
                                 for l in labels}))
    union_rows = []
    for kind, perf in fiber_polys:
        urow = interpolate_rows(perf, labs, basis, Minv, p)
        for l in labs:                        # round-trip gate
            assert eval_interp(urow, fvals[l], p) == perf[l], \
                ("GATE-F1 interpolation round trip", kind, l)
        union_rows.append((kind, urow))
    log("F: interpolation round trips PASS (%d family rows x 36 "
        "labels)" % len(union_rows))

    sel_rows = ["%s^3+%d" % (SELVARS[0], (p - (3 + r3v)) % p),
                "%s^3+%d" % (SELVARS[1], (p - (3 - r3v)) % p),
                "2*%s^2+%d" % (SELVARS[2], p - 3),
                "2*%s^2+%d" % (SELVARS[3], p - 3)]
    rows_txt = [row_to_txt(u, hdrpos, p, interp=True)
                for _, u in union_rows] + sel_rows
    out = os.path.join(famdir, "d25fam_p%d.ms" % p)
    emit_ms(out, hdr, rows_txt, p)
    nterm = sum(t.count("+") + 1 for t in rows_txt)
    log("F: union emission %s: %d rows / %d vars / %d terms / %.2f MB"
        % (out, len(rows_txt), len(hdr), nterm,
           os.path.getsize(out) / 1e6))
    audit_checks(out, p, len(rows_txt), len(hdr), log)
    chk = parse_ms(out, p)                    # independent re-parse
    assert len(chk) == len(rows_txt), "GATE-F2 reparse row count"
    for ridx, (kind, urow) in enumerate(union_rows):
        want = expected_exp_dict(urow, hdrpos, len(hdr), p,
                                 interp=True)
        assert chk[ridx] == want, ("GATE-F2 reparse dict mismatch",
                                   kind)
    for si in range(4):                       # selector rows
        d = chk[len(union_rows) + si]
        e3 = [0] * len(hdr)
        e3[hdrpos[SELVARS[si]]] = 3 if si < 2 else 2
        cst = ((p - (3 + r3v)) % p, (p - (3 - r3v)) % p,
               p - 3, p - 3)[si]
        lead = 1 if si < 2 else 2
        want = {tuple(e3): lead, tuple([0] * len(hdr)): cst}
        assert d == want, ("GATE-F2 selector row mismatch", si)
    log("F: independent-parser round trip dict-exact on all %d rows"
        % len(rows_txt))
    manifest["union_ms"] = {
        "path": out, "rows": len(rows_txt), "vars": len(hdr),
        "row_kinds": [k for k, _ in union_rows] + ["sel"] * 4,
        "terms": nterm,
        "md5": hashlib.md5(open(out, "rb").read()).hexdigest()}

    # 36 parked per-fiber specializations
    hdr_f = occx + P22
    hp_f = {nm: i for i, nm in enumerate(hdr_f)}
    permd5 = {}
    for l in labels:
        rows_f = [row_to_txt({(s, ()): c for s, c in
                              core_rows[l][i].items()}, hp_f, p)
                  for i in range(26)]
        rows_f += [row_to_txt({(s, ()): c for s, c in
                               parse_grow(atlasf[l]["g_rows"][gi],
                                          p).items()}, hp_f, p)
                   for gi in range(3)]
        for nu in range(5):
            if results[l]["residuals"][nu]:
                rows_f.append(row_to_txt(results[l]["residuals"][nu],
                                         hp_f, p))
        fpath = os.path.join(famdir, "d25fam_p%d_%s.ms" % (p, l))
        emit_ms(fpath, hdr_f, rows_f, p)
        permd5[l] = hashlib.md5(open(fpath, "rb").read()).hexdigest()
    assert len(set(permd5.values())) == 36, \
        "GATE-F3 per-fiber emissions not pairwise distinct"
    manifest["per_fiber_md5"] = permd5
    log("F: 36 per-fiber specializations parked (pairwise-distinct "
        "md5)")


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prime", type=int)
    ap.add_argument("--workers", type=int, default=28)
    ap.add_argument("--fibers", default="")
    ap.add_argument("--skip-emit", action="store_true")
    a = ap.parse_args()
    p = a.prime
    root = G_ROOT
    d25 = os.path.join(root, "d25")
    asmdir = os.path.join(d25, "asm")
    famdir = os.path.join(root, "d25fam")
    os.makedirs(asmdir, exist_ok=True)
    os.makedirs(famdir, exist_ok=True)
    logp = os.path.join(d25, "asm_p%d.log" % p)
    t0 = time.time()

    def log(m):
        line = "%s p%d %s" % (time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                            time.gmtime()), p, m)
        print(line, flush=True)
        with open(logp, "a") as fh:
            fh.write(line + "\n")

    with open(os.path.join(d25, "d25asm_p%d.pid" % p), "w") as fh:
        fh.write("%d\n" % os.getpid())
    log("ASSEMBLE start host=%s pid=%d" % (socket.gethostname(),
                                           os.getpid()))

    # selector algebra: 36 distinct evaluations + radical laws
    atlas = json.load(open(os.path.join(d25,
                                        "d23_atlas_p%d.json" % p)))
    assert atlas["meta"]["prime"] == p
    labels = sorted(atlas["fibers"])
    assert len(labels) == 36, "GATE-1 component count != 36"
    fvals = {l: atlas["fibers"][l]["fiber"] for l in labels}
    assert len({tuple(sorted(fv.items()))
                for fv in fvals.values()}) == 36, \
        "GATE-1 selector evaluations not distinct"
    ref = fvals["a00pp"]
    r3v = (pow(ref["A1"], 3, p) - 3) % p
    assert pow(r3v, 2, p) == 3
    for l in labels:
        fv = fvals[l]
        assert pow(fv["A1"], 3, p) == (3 + r3v) % p
        assert pow(fv["A2"], 3, p) == (3 - r3v) % p
        for hk in ("HW1_over_W1", "HW2_over_W2"):
            assert 2 * pow(fv[hk], 2, p) % p == 3
    log("selector algebra: 36 distinct evaluations, radical laws PASS")

    with open(os.path.join(d25, "directionb_tails_D25.pkl"),
              "rb") as fh:
        bank = pickle.load(fh)
    assert bank["D"] == 25
    vars_, byk = bank["vars"], bank["byk"]
    assert not any(k % 2 for k in byk), "Row 23 != 0"

    gbs = {}
    for l in labels:
        with open(os.path.join(d25, "gbcache_p%d_%s.pkl" % (p, l)),
                  "rb") as fh:
            gbs[l] = pickle.load(fh)
    log("GBs: 36 x 509 loaded from the reduction-stage caches")

    core_rows = {}
    for l in labels:
        path = (os.path.join(d25, "fib_a00pp_p%d.ms" % p)
                if l == "a00pp" else
                os.path.join(root, "atlas", "fib_%s_p%d.ms" % (l, p)))
        md5 = hashlib.md5(open(path, "rb").read()).hexdigest()
        assert md5 == atlas["fibers"][l]["fiber_ms_md5"], \
            ("GATE-2 fiber .ms md5 mismatch", l)
        rows = parse_ms(path, p, expect_vars=P22)
        assert len(rows) == 26, ("GATE-2 core rows != 26", l,
                                 len(rows))
        core_rows[l] = rows
    sk0 = [sorted(d) for d in core_rows[labels[0]]]
    for l in labels[1:]:
        assert [sorted(d) for d in core_rows[l]] == sk0, \
            ("GATE-2 core support skeleton mismatch", l)
    log("core rows: 36 x 26 ingested; md5 + support-skeleton PASS")

    B = phaseB(byk, vars_, p, r3v, log)
    B.update(phaseC(byk, vars_, p, r3v, log))
    with open(os.path.join(asmdir, "asmB_p%d.pkl" % p), "wb") as fh:
        pickle.dump(B, fh, protocol=4)

    todo = labels if not a.fibers else [l for l in labels
                                       if l in a.fibers.split(",")]
    shared = dict(p=p, r3=r3v, fvals=fvals, gbs=gbs, vars=vars_,
                  byk=byk, B=B, asmdir=asmdir,
                  atlas=atlas["fibers"], core_rows=core_rows)
    G.update(shared)
    pend = [l for l in todo if not os.path.exists(
        os.path.join(asmdir, "asm_p%d_%s.pkl" % (p, l)))]
    log("fibers: %d todo (%d checkpointed)"
        % (len(pend), len(todo) - len(pend)))
    halted = False
    if pend:
        with Pool(min(a.workers, len(pend)), _init,
                  (shared,)) as pool:
            for lab, st, dt in pool.imap_unordered(fiber_task, pend):
                log("  fiber %-6s %-4s %.1fs" % (lab, st, dt))
                if st.startswith("STOP"):
                    halted = True
    if halted:
        log("HALT: material disagreement -- see STOP lines above")
        return 2
    results = {}
    for l in todo:
        with open(os.path.join(asmdir, "asm_p%d_%s.pkl" % (p, l)),
                  "rb") as fh:
            results[l] = pickle.load(fh)
    if len(todo) < 36:
        log("partial fiber run (--fibers); stopping before E/F")
        return 0

    rows_a00 = {}
    for k in sorted(byk):
        for n in byk[k]:
            rows_a00[(k, n)] = fold_cell(byk[k][n], vars_,
                                         fvals["a00pp"], r3v, p)
    add_nolog_pin(rows_a00, p)
    wit = witness_regression(p, rows_a00, log)

    s_masks = {}
    for nu in range(5):
        mask = "".join("1" if results[l]["residuals"][nu] else "0"
                       for l in labels)
        if "1" in mask:
            s_masks["R%d" % (nu + 1)] = mask
    s_count = len(s_masks)
    occ = sorted({n2 for l in labels for n2 in results[l]["occ_lift"]})
    r_count = len(occ)
    res_terms = {l: results[l]["res_terms"] for l in labels}
    maxterms = max(max(v) if v else 0 for v in res_terms.values())
    log("SHAPE: s = %d residuals (masks %s); r = %d lift vars %s; "
        "max residual %d terms; quotient = %d vars / %d eqs "
        "(prediction (22+r)/(29+s), s <= 5)"
        % (s_count, s_masks, r_count, occ, maxterms, 22 + r_count,
           29 + s_count))
    assert s_count <= 5, "GATE-S residual count > 5"

    manifest = {
        "prime": p, "r3": r3v,
        "date": time.strftime("%Y-%m-%d"),
        "spec": "xmodel/sol-round6.md sect 2 (assembly) / sect 3 "
                "(discrimination)",
        "shape": {"vars": 22 + r_count, "eqs": 29 + s_count,
                  "r": r_count, "s": s_count, "occ_lift": occ,
                  "lift_alias": {nm: XALIAS.get(nm) for nm in occ},
                  "component_masks": s_masks,
                  "res_terms_per_fiber": res_terms,
                  "prediction": "(22+r) vars / (29+s) eqs; 26 core + "
                                "3 g + s residuals; s <= 5"},
        "digest90": {"value": B["digest"],
                     "match_banked_ab5ee038": B["digest_ok"]},
        "C24": B["C24"], "L24": B["L24"], "rowex24": B["rowex24"],
        "C24_sha256": hashlib.sha256(repr(B["C24"]).encode())
        .hexdigest(),
        "L24_sha256": hashlib.sha256(repr(B["L24"]).encode())
        .hexdigest(),
        "serialization": "repr(list of lists of ints in [0,p)), "
                         "row-major; RREF rule: scan columns left-to-"
                         "right, topmost unused nonzero row, full "
                         "Gauss-Jordan; L24/L10 = RREF bases of left "
                         "kernels",
        "C10": B["C10"], "L10": B["L10"],
        "carriers22": [list(x) for x in B["carriers"]],
        "solved4": DEEP10[:NSOLVED], "kernel6": DEEP10[NSOLVED:],
        "witness_regression": wit,
        "gates_per_fiber": {l: results[l]["gates"] for l in labels},
        "scope": "INTERNAL/UNREVIEWED; mod p, chart-local (residue-A "
                 "B-frozen no-log PIN42 W1W2!=0 chart, fixed r3 "
                 "embedding); union system = 36-component split "
                 "etale selector flattening (sol-round6 2.5/2.6)",
    }
    if not a.skip_emit:
        emit_all(p, labels, fvals, core_rows, atlas["fibers"],
                 results, occ, famdir, r3v, manifest, log)
    with open(os.path.join(famdir, "asm_manifest_p%d.json" % p),
              "w") as fh:
        json.dump(manifest, fh, indent=1, sort_keys=True)
    log("DONE wall=%.0fs" % (time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
