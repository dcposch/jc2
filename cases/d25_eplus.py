#!/usr/bin/env python3
"""d25_eplus.py -- the e+ LANDSCAPE on the D25 A^14 cells (9.S3 stage).

STATUS: INTERNAL TOOLING, UNREVIEWED.  FAIL-CLOSED THROUGHOUT.
Everything numeric this tool banks is E_PLUS_CANDIDATE / certified
LOWER bound per the 8.S9 gate discipline (cases/eplus_certify.py);
e_plus_certified is ALWAYS None (no section is constructed).

WHAT THIS STAGE DOES.  The 2026-08-21 AUDIT tail promoted the D25
family verdict: each of the 36 fiber systems is 16 disjoint copies of
A^14 (certificate xmodel/sol-ideas-0821.md items 1-2; replay
cases/d25_certificate_replay.json + SHEET6-DIRECTIONB 9.S2; Grok
review xmodel/grok-d25cert-review.md).  This tool computes the
corrected-e+ application gates of the PROMOTED filtered differential
Newton lemma AT POINTS OF THOSE CELLS, at depth D = 25 (germ threshold
2 e+ + 1 <= 25, i.e. e+ <= 12):

  (1) the 72 banked per-fiber witnesses (36 fibers x 2 primes,
      derived_witness of the replay: all cell coordinates zero, W from
      the fiber's quartic fourth roots);
  (2) random interior samples of the A^14 cells: the 14 free
      parameters (T = x57,x59,x60,x62,x63,x65,x66,x68,x72,x73 + lifts
      x16,x19,x24,x27) drawn uniformly, dependent coordinates solved
      through the certificate's unit-pivot structure (greedy
      Laurent-unit elimination + the numerically re-derived Cramer
      compatibility rows + the R1,R2 2x2 lift solve).

POINT RECONSTRUCTION (28-var cell point -> full chart point).  A cell
point lives in the parked 28-variable presentation; the e+ certifier
consumes a FULL chart point (witness72 + deep tails).  The banked
8.S6 reconstruction discipline is replayed FIBER-FRAME-NATIVELY on
the pristine rows: (a) the 22 shallow pivots are back-solved
groupwise from the raw D21 window rows in the banked band-triangular
groups 1+2+3+4+4+4+4 (PIV22_SEQ), every group row asserted to vanish
exactly after its square affine solve; (b) the level-44 tg pair
(tg1_44, tg2_44) -- which feeds the band >= 12 pivot rows -- is
pinned by EXACT AFFINE PROBING of the band-22 compatibility residual
c(tg) = K.b(tg) (probes (0,0),(1,0),(0,1), affinity VERIFIED at
(1,1); K = canonical left kernel of the constant deep-column matrix,
rank 2 solve; reproduces the banked row22red tg solve exactly at
a00pp); (c) the ten deep tails solve at rank 4 with kernel frees = 0;
(d) the BAND-24 FRONTIER COMPLETION: the nine k = 24 residual cells
are solved over the ten banked frontier directions (levels 51/56,
cases/d25_reduce.FRONTIER) at rank 4 with kernel frees = 0, THROUGH
THE CERTIFIER'S OWN dual-jet operator, guarded by the measured level
cap (no frontier entry below band 24; the sect-9 finding 'bands <=
22 carry no new-at-D25 variables' re-measured per point), and the
jets are rebuilt at the completed point.  All other free coordinates
are 0.  NOTE the completion therefore differs from the 8.S9 ZC_RULE
exactly in the frontier block (level-51/56 solve values instead of
zeros); it is deterministic and hashed into zc_hash; at the 72
banked witnesses the frontier solve is identically zero and the two
completions coincide.  FAIL-CLOSED VERIFICATION per point: (i) all
34 raw fiber rows vanish exactly (independent parser); (ii) the 22
pivot-group rows vanish after back-solve; (iii) all 76 raw D21
window rows vanish; (iv) all 10 pristine Row_22 rows vanish; (v) at
a00pp additionally the frozen row22compat (48/48 + six compat
zeros), row22red (32/32) and core23 (77/77) emissions vanish;
(vi) the certifier's own BRIDGE-30 b1/b2 re-derives the residual
from raw coefficients and demands nu >= 25 at the completed point.
Any failure marks the point REJECTED and is banked as such (nothing
is silently dropped).

FIBER FRAMES.  The banked evaluators are frozen at radical_point =
the a00pp selector frame.  The 36 fibers differ only through
(A1r, A2r, h1r, h2r) with A_ir^3 = 3 +/- r3, 2 h_ir^2 = 3 (d23 atlas
values; the same r3, z, chart).  The raw-row/pristine evaluators and
the dual-jet constructor carry A1, A2, HW1, HW2 as explicit point
data, so this tool generalizes them PER-SIDE (HW_i folds as
h_ir * W_i; the vexpr radkey fold pow(h,h1+h2) becomes
pow(h1r,h1)*pow(h2r,h2)) and re-verifies the a00pp specialization
EXACTLY against the unmodified banked stack (--crosscheck: byte-equal
gate results + operator hash vs cases/eplus_certify.py --file on the
same point).  The frozen a00pp-frame emissions are NOT applied to
other fibers (they fold the selector values); other fibers are gated
by (i)-(iv) + (vi) above, which are selector-explicit.

SCOPE BOX: mod p ONLY (p = 105337, 105673), residue-A B-frozen no-log
W1W2 != 0 chart with PIN42, chart-local, per the deterministic zero
completion; the EMISSION-FIDELITY caveat of SHEET6-DIRECTIONB sect 9
is inherited; gate tiers exactly as 8.S9 (PARAM-30 FAIL direction
certified; PASS only ever E_PLUS_CANDIDATE; no germ claims).

USAGE
  python3 cases/d25_eplus.py --selftest        # sampler + frame controls
  python3 cases/d25_eplus.py --crosscheck      # driver == banked tool, a00pp
  python3 cases/d25_eplus.py --run [--out cases/d25_eplus.json]
        [--witnesses-only] [--samples N] [--seed S] [--heavy]
"""
import argparse
import collections
import json
import os
import random
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import valuation_e as V
import valuation_e2 as V2
import eplus_certify as EC

TOOL = "cases/d25_eplus.py"
CAND = EC.CAND                              # "E_PLUS_CANDIDATE"
PRIMES = (105337, 105673)
D = 25
THRESH = (D - 1) // 2                       # 12
REPLAY = os.path.join(HERE, "d25_certificate_replay.json")

FREE_BASE = ["x57", "x59", "x60", "x62", "x63", "x65", "x66", "x68",
             "x72", "x73"]
FREE_LIFT = ["x16", "x19", "x24", "x27"]
DEP = ["x70", "x53", "x58", "x55", "x71", "x52", "x47", "x54",
       "x33", "x38"]
CELLX = FREE_BASE + FREE_LIFT + DEP         # the 24 x-coords of a cell
TG_PAIR = ("tg1_44", "tg2_44")              # x17, x25 (frees x32,x37 = 0)
OTHER_FIBERS_P0 = ["a00mm", "a01pp", "a10pm", "a22mp"]

_REP = None


def replay():
    global _REP
    if _REP is None:
        _REP = json.load(open(REPLAY))
    return _REP


_ATLAS = {}


def fiber_env(p, lab):
    """(A1r, A2r, h1r, h2r) of the fiber from the banked d23 atlas;
    legitimacy re-verified against the chart radicals."""
    if p not in _ATLAS:
        _ATLAS[p] = json.load(open(
            os.path.join(HERE, "d23_atlas_p%d.json" % p)))
    f = _ATLAS[p]["fibers"][lab]["fiber"]
    pt, r3, h32 = V.radical_env(p)
    env = {"label": lab, "A1": int(f["A1"]), "A2": int(f["A2"]),
           "h1": int(f["HW1_over_W1"]), "h2": int(f["HW2_over_W2"])}
    assert pow(env["A1"], 3, p) == (3 + r3) % p, "A1r not a cube root"
    assert pow(env["A2"], 3, p) == (3 - r3) % p, "A2r not a cube root"
    for h in (env["h1"], env["h2"]):
        assert 2 * h * h % p == 3 % p, "h_ir not a root of 3/2"
    env["is_radical_frame"] = (env["A1"] == pt["A1"] and
                               env["A2"] == pt["A2"] and
                               env["h1"] == h32 and env["h2"] == h32)
    return env


# ------------------------------------------------- cell sampling (34 rows)
def parse_fiber_ms(p, lab):
    path = os.path.join(HERE, "d25fam_p%d_%s.ms" % (p, lab))
    lines = open(path).read().split("\n")
    hdr = [h.strip() for h in lines[0].split(",")]
    assert int(lines[1]) == p
    body = "\n".join(lines[2:])
    rows_txt = [r.strip().rstrip(",") for r in body.split(",\n")
                if r.strip()]
    assert len(rows_txt) == 34, (p, lab, len(rows_txt))
    rows = []
    for rt in rows_txt:
        terms = []
        for t in rt.split("+"):
            fs = t.strip().split("*")
            try:
                c = int(fs[0])
                fs = fs[1:]
            except ValueError:
                c = 1
            mono = []
            for f in fs:
                if "^" in f:
                    nm, e = f.split("^")
                    mono.append((nm, int(e)))
                else:
                    mono.append((f, 1))
            terms.append((c, tuple(mono)))
        rows.append(terms)
    return hdr, rows


def row_support(row):
    return {nm for _, mono in row for nm, _ in mono}


def eval_row(row, val, p):
    tot = 0
    for c, mono in row:
        m = c
        for nm, e in mono:
            m = m * pow(val[nm], e, p) % p
        tot = (tot + m) % p
    return tot


def row_as_poly(row, val, unknowns, p):
    """Row with all vars outside `unknowns` substituted from val ->
    {exponent tuple over unknowns: coeff}."""
    out = {}
    ui = {u: i for i, u in enumerate(unknowns)}
    for c, mono in row:
        m = c
        ev = [0] * len(unknowns)
        for nm, e in mono:
            if nm in ui:
                ev[ui[nm]] += e
            else:
                m = m * pow(val[nm], e, p) % p
        k = tuple(ev)
        out[k] = (out.get(k, 0) + m) % p
    return {k: c for k, c in out.items() if c}


def compat_rows(p, rows, val, unknown):
    """Cramer/Schur compatibility rows of the residuals (file rows
    29..33), derived numerically: residuals affine in (x33,x38) with
    Laurent-UNIT coefficients (asserted); the 3-dim left kernel of the
    5x2 lift-column matrix gives base-only rows (rank 2 = the banked
    hcore/hlin span)."""
    unk = sorted(unknown)
    ia, ib = unk.index("x33"), unk.index("x38")
    polys, ab = [], []
    for ri in range(29, 34):
        po = row_as_poly(rows[ri], val, unk, p)
        a = b = 0
        for k, c in po.items():
            if k[ia] or k[ib]:
                assert sum(k) == 1, "lift coefficient not a known unit"
                if k[ia]:
                    a = c
                else:
                    b = c
        polys.append(po)
        ab.append((a, b))
    M = [[ab[i][0], ab[i][1]] + [1 if j == i else 0 for j in range(5)]
         for i in range(5)]
    r = 0
    for c in range(2):
        piv = next((i for i in range(r, 5) if M[i][c]), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][c], p - 2, p)
        M[r] = [x * iv % p for x in M[r]]
        for i in range(5):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        r += 1
    assert r == 2, "lift column rank != 2"
    out = []
    for i in range(2, 5):
        kvec = M[i][2:]
        comb = {}
        for ki, po in zip(kvec, polys):
            if not ki:
                continue
            for k, c in po.items():
                comb[k] = (comb.get(k, 0) + ki * c) % p
        comb = {k: c for k, c in comb.items() if c}
        assert all(k[ia] == 0 and k[ib] == 0 for k in comb), \
            "lift terms did not cancel in compat row"
        terms = []
        for k, c in comb.items():
            mono = tuple((unk[j], e) for j, e in enumerate(k) if e)
            terms.append((c, mono))
        out.append(terms)
    return out


def solve_cell_point(p, hdr, rows, freeval, W1, W2):
    """freeval: the 14 free vars -> full verified 28-var cell point."""
    val = dict(freeval)
    val["W1"], val["W2"] = W1 % p, W2 % p
    val["uW1"] = pow(W1, p - 2, p)
    val["uW2"] = pow(W2, p - 2, p)
    unknown = [v for v in hdr if v not in val]
    assert sorted(unknown) == sorted(DEP), unknown
    rows = list(rows)
    live = list(range(34))
    added_compat = False
    guard = 0
    while unknown:
        guard += 1
        assert guard < 200, "cell solver did not terminate"
        progress = False
        for ri in live:
            sup = [u for u in row_support(rows[ri]) if u in unknown]
            if len(sup) != 1:
                continue
            u = sup[0]
            po = row_as_poly(rows[ri], val, [u], p)
            if max((k[0] for k in po), default=0) != 1 or \
                    po.get((1,), 0) == 0:
                continue
            val[u] = (-po.get((0,), 0)) * pow(po[(1,)], p - 2, p) % p
            unknown.remove(u)
            progress = True
            break
        if progress:
            continue
        done = False
        pairs = {}
        for ri in live:
            sup = tuple(sorted(u for u in row_support(rows[ri])
                               if u in unknown))
            if len(sup) == 2:
                pairs.setdefault(sup, []).append(ri)
        for sup, ris in pairs.items():
            u, v = sup
            aff = []
            for ri in ris:
                po = row_as_poly(rows[ri], val, [u, v], p)
                if all(k in ((0, 0), (1, 0), (0, 1)) for k in po):
                    aff.append(po)
            for i in range(len(aff)):
                for j in range(i + 1, len(aff)):
                    pa, pb = aff[i], aff[j]
                    a, b, rr = (pa.get((1, 0), 0), pa.get((0, 1), 0),
                                pa.get((0, 0), 0))
                    d, e, s = (pb.get((1, 0), 0), pb.get((0, 1), 0),
                               pb.get((0, 0), 0))
                    det = (a * e - b * d) % p
                    if det == 0:
                        continue
                    idet = pow(det, p - 2, p)
                    val[u] = (b * s - e * rr) * idet % p
                    val[v] = (d * rr - a * s) * idet % p
                    unknown.remove(u)
                    unknown.remove(v)
                    done = True
                    break
                if done:
                    break
            if done:
                break
        if not done and not added_compat:
            for cr in compat_rows(p, rows, val, unknown):
                live.append(len(rows))
                rows.append(cr)
            added_compat = True
            done = True
        assert done, "cell solver stuck; unknowns left: %s" % unknown
    bad = [ri for ri in range(34) if eval_row(rows[ri], val, p) != 0]
    assert not bad, ("D25 fiber rows nonvanishing at sample", bad)
    return val


def fourth_roots(p, c, w_hint):
    assert pow(w_hint, 4, p) == c % p, "witness root does not match c"
    i4, g = None, 2
    while i4 is None:
        cand = pow(g, (p - 1) // 4, p)
        if cand != 1 and pow(cand, 2, p) == p - 1:
            i4 = cand
        g += 1
    roots = sorted({w_hint * pow(i4, k, p) % p for k in range(4)})
    assert len(roots) == 4 and all(pow(r, 4, p) == c % p for r in roots)
    return roots


def cells_of_fiber(p, lab):
    f = replay()["parked_fibers"][str(p)][lab]
    dw = f["derived_witness"]
    r1 = fourth_roots(p, int(f["W1^4"]), int(dw["W1"]))
    r2 = fourth_roots(p, int(f["W2^4"]), int(dw["W2"]))
    return [(a, b) for a in r1 for b in r2]


# ------------------------------------- fiber-frame pristine-row evaluators
def vexpr_vp_f(v, vars_, dval, p, r3, env):
    """valuation_e.vexpr_value_and_partials generalized per-side:
    A_i -> env selector cube roots, HW_i^h folds as h_ir^h W_i^h."""
    W1v, W2v = dval["W1"], dval["W2"]
    val = 0
    acc = collections.defaultdict(int)
    import r1_fullcore as FC
    for vk, r in v.items():
        cv = 0
        for rk, c in r.items():
            z, e1, e2, pw, h1, qw, h2, B = rk
            assert z == 0 and B == 0, "non-tail radkey on window row"
            x = (FC.frmod(c[0], p) + FC.frmod(c[1], p) * r3) % p
            x = x * pow(env["A1"], e1, p) % p * pow(env["A2"], e2, p) % p
            x = x * pow(env["h1"], h1, p) % p * pow(env["h2"], h2, p) % p
            x = x * pow(W1v, pw + h1, p) % p * pow(W2v, qw + h2, p) % p
            cv = (cv + x) % p
        if not cv:
            continue
        cnt = collections.Counter(vk)
        mono = 1
        for v2, m2 in cnt.items():
            mono = mono * pow(dval[vars_[v2]], m2, p) % p
        val = (val + cv * mono) % p
        for vid, m in cnt.items():
            pr = cv * m % p
            for v2, m2 in cnt.items():
                e = m2 - (1 if v2 == vid else 0)
                if e:
                    pr = pr * pow(dval[vars_[v2]], e, p) % p
            acc[vars_[vid]] = (acc[vars_[vid]] + pr) % p
    return val, {k: c for k, c in acc.items() if c}


def msrow_vp_f(d, dval, p, env):
    """valuation_e.msrow_value_and_partials generalized per-side."""
    W1v, W2v = dval["W1"], dval["W2"]
    val = 0
    acc = collections.defaultdict(int)
    for k, c in d.items():
        v = c
        wpow = {"W1": 0, "W2": 0}
        tails = []
        for nm, e in k:
            if nm == "A1":
                v = v * pow(env["A1"], e, p) % p
            elif nm == "A2":
                v = v * pow(env["A2"], e, p) % p
            elif nm == "HW1":
                v = v * pow(env["h1"], e, p) % p
                wpow["W1"] += e
            elif nm == "HW2":
                v = v * pow(env["h2"], e, p) % p
                wpow["W2"] += e
            elif nm in ("W1", "W2"):
                wpow[nm] += e
            else:
                assert nm not in ("uW1", "uW2", "uA"), \
                    "saturation var on a pristine row"
                tails.append((nm, e))
        v = v * pow(W1v, wpow["W1"], p) % p * pow(W2v, wpow["W2"], p) % p
        mono = 1
        for nm, e in tails:
            mono = mono * pow(dval[nm], e, p) % p
        val = (val + v * mono) % p
        for nm, e in tails:
            pr = v * e % p
            for nm2, e2 in tails:
                ee = e2 - (1 if nm2 == nm else 0)
                if ee:
                    pr = pr * pow(dval[nm2], ee, p) % p
            acc[nm] = (acc[nm] + pr) % p
    return val, {k: c for k, c in acc.items() if c}


def window_partials_f(p, dval, Dw, env):
    """Fiber-frame window rows: 76 raw D21 + (D >= 23) 10 pristine
    Row_22; rowdata[(band, eta)] = (value, partials)."""
    rows21, vars_ = V.raw_rows21()
    _, r3, _ = V.radical_env(p)
    out = {}
    for lab, v in rows21:
        out[lab] = vexpr_vp_f(v, vars_, dval, p, r3, env)
    if Dw >= 23:
        for lab, d in V.row22_rows(p):
            out[lab] = msrow_vp_f(d, dval, p, env)
    return out


# --------------------------------------- full chart point reconstruction
# The banked 22-pivot back-solve (valuation_e.PIV22_SEQ) grouped by its
# band-triangular affine groups 1+2+3+4+4+4+4 (8.S6 T4 discipline):
# within a group the pristine window rows are affine in the group's
# pivots (verified per point by the exact vanishing assert after the
# square solve; any hidden nonlinearity or triangularity failure fires
# it), and every earlier-band pivot is already substituted.
PIV_GROUPS = [
    [("tf1_38", (6, 2))],
    [("tf1_40", (8, 0)), ("tf2_40", (8, 3))],
    [("tf1_44", (12, 2)), ("tf2_44", (12, 5)), ("tf1_39", (12, 8))],
    [("tf1_46", (14, 0)), ("tf2_46", (14, 3)), ("tf1_41", (14, 6)),
     ("tf2_41", (14, 9))],
    [("tf1_43", (16, 1)), ("tf1_48", (16, 4)), ("tf2_43", (16, 7)),
     ("tf2_48", (16, 10))],
    [("tf1_45", (18, 2)), ("tf1_50", (18, 5)), ("tf2_45", (18, 8)),
     ("tf2_50", (18, 11))],
    [("tf1_47", (20, 0)), ("tf1_52", (20, 3)), ("tf2_47", (20, 6)),
     ("tf2_52", (20, 9))],
]

_OCC = {}
_X2TF = None


def x2tf_cached():
    """x-registry (x-name -> tail name), computed once: V2.x_registry
    re-unpickles the frozen state on every call."""
    global _X2TF
    if _X2TF is None:
        _X2TF = V2.x_registry()
    return _X2TF


def _occ_names(p):
    """All tail names occurring in the pristine rows (raw D21 VExpr +
    Row_22), for the deterministic zero fill of aux frees."""
    if p not in _OCC:
        rows21, vars_ = V.raw_rows21()
        occ = set()
        for _lab, v in rows21:
            for vk in v:
                for vid in vk:
                    occ.add(vars_[vid])
        for _lab, d in V.row22_rows(p):
            for k in d:
                for nm, _e in k:
                    if nm not in ("A1", "A2", "W1", "W2", "HW1", "HW2"):
                        occ.add(nm)
        _OCC[p] = occ
    return _OCC[p]


def full_point_f(p, cellval, env, tg=(0, 0)):
    """28-var cell point -> full chart dval (tail names), fiber frame:
    the 22 shallow pivots back-solved GROUPWISE from the PRISTINE raw
    D21 window rows through the fiber-frame evaluator (vexpr_vp_f with
    A1r, A2r, h1r W1, h2r W2); every group row is asserted to vanish
    exactly after its square affine solve, and PIV22_SEQ coverage is
    asserted against the banked sequence.  Aux frees = 0 (draw 0 zero
    completion), PIN42 = 0.  tg = the (tg1_44, tg2_44) pair: the
    level-44 tangent coordinates feed the band >= 12 pivot rows, so
    the pivots are (affine) functions of tg; reconstruct_point solves
    the pair by exact affine probing of the band-22 compatibility."""
    seq = {nm: lab for nm, lab in V.PIV22_SEQ()}
    grp = {nm: lab for g in PIV_GROUPS for nm, lab in g}
    assert grp == seq, "pivot groups do not match the banked PIV22_SEQ"
    rows21, vars_ = V.raw_rows21()
    rowmap = {lab: v for lab, v in rows21}
    _, r3, _ = V.radical_env(p)
    x2tf = x2tf_cached()
    dval = {}
    for xn, x in cellval.items():
        if xn.startswith("x"):
            dval[x2tf[xn]] = int(x)
    for nm in _occ_names(p):
        dval.setdefault(nm, 0)              # PIN42 + aux frees (draw 0)
    dval["uf30"] = 0
    dval["tg1_44"], dval["tg2_44"] = int(tg[0]) % p, int(tg[1]) % p
    W1v, W2v = int(cellval["W1"]) % p, int(cellval["W2"]) % p
    dval.update({"A1": env["A1"], "A2": env["A2"], "W1": W1v, "W2": W2v,
                 "HW1": env["h1"] * W1v % p, "HW2": env["h2"] * W2v % p})
    for group in PIV_GROUPS:
        unk = [nm for nm, _lab in group]
        assert all(dval[nm] == 0 for nm in unk)
        A, b = [], []
        for _nm, lab in group:
            v0, pr = vexpr_vp_f(rowmap[lab], vars_, dval, p, r3, env)
            A.append([pr.get(u, 0) for u in unk])
            b.append((-v0) % p)
        n = len(unk)
        M = [row[:] + [bb] for row, bb in zip(A, b)]
        for c in range(n):
            piv = next((i for i in range(c, n) if M[i][c]), None)
            assert piv is not None, \
                "pivot group singular at band %d" % group[0][1][0]
            M[c], M[piv] = M[piv], M[c]
            iv = pow(M[c][c], p - 2, p)
            M[c] = [x * iv % p for x in M[c]]
            for i in range(n):
                if i != c and M[i][c]:
                    f = M[i][c]
                    M[i] = [(x - f * y) % p for x, y in zip(M[i], M[c])]
        for j, nm in enumerate(unk):
            dval[nm] = M[j][n]
        for _nm, lab in group:
            v0, _pr = vexpr_vp_f(rowmap[lab], vars_, dval, p, r3, env)
            assert v0 == 0, ("pivot row nonzero after group solve "
                             "(affinity/triangularity broken)", lab)
    return dval


def band22_system(p, dval, env):
    """The 10 PRISTINE Row_22 rows as an affine system A y = b on the
    ten deep tails (evaluated at deep = 0; tg already in dval)."""
    deepn = [V.DEEPMAP[x] for x in V.DEEPX]
    dv = dict(dval)
    for nm in deepn:
        dv[nm] = 0
    A, b = [], []
    for _lab, d in V.row22_rows(p):
        val0, pr = msrow_vp_f(d, dv, p, env)
        A.append([pr.get(nm, 0) for nm in deepn])
        b.append((-val0) % p)
    return A, b


def left_kernel(A, p):
    """Canonical left kernel of the 10x10 deep matrix (RREF of A^T with
    identity carried): rows k with k.A = 0."""
    n = len(A)
    m = len(A[0])
    M = []
    for i in range(n):
        M.append(A[i][:] + [1 if j == i else 0 for j in range(n)])
    r = 0
    for c in range(m):
        piv = next((i for i in range(r, n) if M[i][c]), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][c], p - 2, p)
        M[r] = [x * iv % p for x in M[r]]
        for i in range(n):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        r += 1
    K = [row[m:] for row in M[r:]]
    return K, r


def solve_deep_zero_completion(A, b, p):
    """A y = b on the ten deep tails, kernel frees = 0 (the banked zero
    completion); returns y or None on inconsistency."""
    n = len(A[0])
    M = [A[i][:] + [b[i]] for i in range(len(A))]
    rk, pivcols = 0, []
    for cidx in range(n):
        prw = next((i for i in range(rk, len(M)) if M[i][cidx]), None)
        if prw is None:
            continue
        M[rk], M[prw] = M[prw], M[rk]
        iv = pow(M[rk][cidx], p - 2, p)
        M[rk] = [x * iv % p for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][cidx]:
                f = M[i][cidx]
                M[i] = [(a - f * bb) % p for a, bb in zip(M[i], M[rk])]
        pivcols.append(cidx)
        rk += 1
    for i in range(rk, len(M)):
        if M[i][n]:
            return None, rk
    y = [0] * n
    for i, cidx in enumerate(pivcols):
        y[cidx] = M[i][n]
    return y, rk


def reconstruct_point(p, cellval, env):
    """Cell point -> full chart point (fiber frame), the exact affine
    tg-probe pipeline: the (tg1_44, tg2_44) pair feeds the band >= 12
    pivot rows, so the band-22 compatibility residual c(tg) = K.b(tg)
    (K = the canonical left kernel of the CONSTANT deep-column matrix)
    is an affine function of tg -- measured at probes (0,0), (1,0),
    (0,1) and VERIFIED at (1,1); the rank-2 affine solve pins tg, the
    pipeline reruns at tg*, the deep tails solve with kernel frees = 0
    (zero completion), and every band <= 22 row is re-verified exactly.
    Returns (dval, diag) or raises (fail-closed)."""
    probes = {}
    A0 = None
    for t in ((0, 0), (1, 0), (0, 1), (1, 1)):
        dv = full_point_f(p, cellval, env, tg=t)
        A, b = band22_system(p, dv, env)
        if A0 is None:
            A0 = A
        else:
            assert A == A0, "deep-column matrix depends on tg (!)"
        probes[t] = b
    K, deep_rank = left_kernel(A0, p)
    assert deep_rank == 4, "deep Schur rank %d != 4" % deep_rank
    assert len(K) == 6
    c = {t: [sum(kk * bb for kk, bb in zip(krow, probes[t])) % p
             for krow in K] for t in probes}
    # exact affinity check at (1,1)
    aff11 = [(c[(1, 0)][i] + c[(0, 1)][i] - c[(0, 0)][i]) % p
             for i in range(6)]
    assert aff11 == c[(1, 1)], \
        "band-22 compat residual is NOT affine in tg (fail-closed)"
    # rank-2 affine solve: [c10-c00 | c01-c00] t = -c00
    col1 = [(c[(1, 0)][i] - c[(0, 0)][i]) % p for i in range(6)]
    col2 = [(c[(0, 1)][i] - c[(0, 0)][i]) % p for i in range(6)]
    rhs = [(-c[(0, 0)][i]) % p for i in range(6)]
    M = [[col1[i], col2[i], rhs[i]] for i in range(6)]
    r = 0
    for cc in range(2):
        piv = next((i for i in range(r, 6) if M[i][cc]), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][cc], p - 2, p)
        M[r] = [x * iv % p for x in M[r]]
        for i in range(6):
            if i != r and M[i][cc]:
                f = M[i][cc]
                M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        r += 1
    assert r == 2, "tg system rank %d != 2" % r
    assert all(M[i][2] == 0 for i in range(2, 6)), \
        "tg system inconsistent: NOT_IN_DOMAIN at band 22"
    t1, t2 = M[0][2], M[1][2]
    dval = full_point_f(p, cellval, env, tg=(t1, t2))
    A, b = band22_system(p, dval, env)
    assert A == A0
    ck = [sum(kk * bb for kk, bb in zip(krow, b)) % p for krow in K]
    assert not any(ck), "compat residual nonzero at solved tg"
    y, rk = solve_deep_zero_completion(A, b, p)
    assert y is not None and rk == 4, "deep solve failed at solved tg"
    deepn = [V.DEEPMAP[x] for x in V.DEEPX]
    for nm, vv in zip(deepn, y):
        dval[nm] = vv
    for _lab, d in V.row22_rows(p):
        val0, _ = msrow_vp_f(d, dval, p, env)
        assert val0 == 0, "Row_22 nonzero after deep solve"
    diag = {"tg1_44": t1, "tg2_44": t2, "deep_rank": rk,
            "tg_rank": r}
    return dval, diag


def verify_full_point(p, dval, env, a00pp_frozen):
    """The fail-closed verification block.  Returns dict of checks;
    every entry must be True for the point to be accepted."""
    checks = {}
    wp = window_partials_f(p, dval, 21, env)
    checks["raw_D21_rows_vanish"] = not any(v for v, _ in wp.values())
    r22 = [msrow_vp_f(d, dval, p, env)[0] for _, d in V.row22_rows(p)]
    checks["pristine_row22_vanish"] = not any(r22)
    if a00pp_frozen:
        nz, nr, cvals = V.verify_row22compat(p, dval)
        checks["row22compat_48"] = (nz == nr == 48)
        checks["compat_c_zero"] = not any(cvals)
        nz23, nr23 = V.verify_core23(p, dval)
        checks["core23_77"] = (nz23 == nr23 == 77)
        # frozen row22red emission (32 rows, x-named)
        hdr, rr = V.parse_ms_rows(
            os.path.join(HERE, "directionb_row22red_p%d.ms" % p), p)
        xval = V._xval_from_point(p, dval)
        vals = [V.eval_ms_row(d, xval, p) for d in rr]
        checks["row22red_32"] = not any(vals)
    return checks


def witness72_of(p, dval):
    """dval -> (witness72 dict, deep_tails dict) in the banked d23
    JSON shapes (x-registry + conventional deep names); cached-registry
    equivalent of valuation_e._xval_from_point."""
    x2tf = x2tf_cached()
    xs = ["x%d" % i for i in range(74)
          if i not in (46, 51, 56, 61, 64, 67)]
    wit72 = {x: int(dval[x2tf[x]]) for x in xs}
    wit72["W1"], wit72["W2"] = int(dval["W1"]), int(dval["W2"])
    wit72["uW1"] = pow(int(dval["W1"]), p - 2, p)
    wit72["uW2"] = pow(int(dval["W2"]), p - 2, p)
    deep = {V.DEEPMAP[x]: int(dval[V.DEEPMAP[x]]) for x in V.DEEPX}
    return wit72, deep


# ----------------------------------------------- fiber-frame certification
def build_point_f(p, wit72, deep_tails, env):
    """valuation_e2.build_point with the fiber's selector frame in the
    fixed data (A_i = A_ir, HW_i = h_ir W_i)."""
    point = V2.build_point(p, wit72, deep_tails)
    fx = point["fixed"]
    fx["A1"], fx["A2"] = env["A1"], env["A2"]
    fx["HW1"] = env["h1"] * fx["W1"] % p
    fx["HW2"] = env["h2"] * fx["W2"] % p
    blob = json.dumps({"prime": p, "base_zc": point["zc_hash"],
                       "fiber": {k: env[k] for k in
                                 ("label", "A1", "A2", "h1", "h2")}},
                      sort_keys=True)
    import hashlib
    point["zc_hash"] = hashlib.sha256(blob.encode()).hexdigest()
    return point


def banked_row_match_f(E, p, point, env):
    """valuation_e2.banked_row_match against the FIBER-frame pristine
    pipeline (window_partials_f), same exact/unit-ratio discipline."""
    dval23 = V2.dval_for_banked(p, point)
    rowdata = window_partials_f(p, dval23, 23, env)
    Gg = E.G.astype(np.int64)
    n_exact = n_rows = 0
    ratios = {}
    ok = True
    for (n, a), (val, pr) in rowdata.items():
        n_rows += 1
        mine = {}
        for (fam, r), col in V2.GIDX.items():
            c = int(Gg[a][n][col])
            if c:
                mine["%s_%d" % (fam, 32 + r)] = c
        theirs = {V2.DEEP_RELABEL.get(k, k): v for k, v in pr.items()
                  if k[:3] in ("tf1", "tf2", "tg1", "tg2") or
                  k[:4] in ("tg01", "tg02")}
        if val != 0:
            ok = False
        if mine == theirs:
            n_exact += 1
            continue
        if set(mine) != set(theirs) or not mine:
            ok = False
            continue
        ks = sorted(mine)
        r0 = theirs[ks[0]] * pow(mine[ks[0]], p - 2, p) % p
        if all(theirs[k] == mine[k] * r0 % p for k in ks):
            ratios[str((n, a))] = r0
        else:
            ok = False
    return ok, n_exact, n_rows, ratios


def gate_bridge30_f(E, p, point, env):
    """eplus_certify.gate_bridge30 with the fiber-frame banked match."""
    Vv = E.V.astype(np.int64)
    Gg = E.G.astype(np.int64)
    checks = {}
    below = sorted({int(n) for n in range(min(D, V2._S))
                    if Vv[:30, n].any()})
    checks["b1_residual_below_D_vanishes"] = bool(not below)
    val_bands = sorted({int(n) for n in range(V2._S) if Vv[:30, n].any()})
    nu_window = val_bands[0] if val_bands else None
    checks["b2_nu_window_ge_D"] = bool(nu_window is None or
                                       nu_window >= D)
    ok6, nex, nrows, ratios = banked_row_match_f(E, p, point, env)
    checks["b3_banked_86row_match"] = bool(ok6 and nrows == 86)
    deepcols = [(f, 17) for f in ("tf1", "tf2", "tg1", "tg2")] + \
               [(f, 22) for f in V2.FAMS]
    rows22 = [a for a in range(29) if V2.S_A[a] == 10] + [28]
    M22 = np.zeros((10, 10), dtype=np.int64)
    for i, a in enumerate(rows22):
        for j, (f, r) in enumerate(deepcols):
            M22[i][j] = Gg[a][22][V2.GIDX[(f, r)]]
    checks["b4_deep_schur_rank_4"] = bool(V2.rankp(M22, p) == 4)
    ok = all(checks.values())
    return {"checks": checks, "check_pass": ok,
            "status": CAND if ok else "FAIL",
            "pending": EC.PENDING["BRIDGE-30"],
            "banked_match": {"rows": nrows, "exact": nex,
                             "unit_rescaled": len(ratios)},
            "nu_window": nu_window,
            "value_bands_le41": val_bands}


def gate_filter30_f(E, p, point, wit72, env):
    """eplus_certify.gate_filter30 with the PER-SIDE HW law (the only
    fiber-dependent audit): HW_i = h_ir W_i with 2 h_ir^2 = 3."""
    Gg = E.G.astype(np.int64)
    checks = {}
    viol = 0
    for (f, r), col in V2.GIDX.items():
        if Gg[:30, :min(r, V2._S), col].any():
            viol += 1
    checks["f1_causality_no_entry_below_r"] = bool(viol == 0)
    first = next((n for n in range(V2._S) if Gg[:30, n].any()), None)
    checks["f2_no_negative_shift"] = bool(first is None or
                                          first >= min(EC.S30))
    pt, r3, h32 = V.radical_env(p)
    fx = point["fixed"]
    u = {}
    u["r3_sq_3"] = pow(r3, 2, p) == 3 % p
    u["h32_2h2_3"] = (2 * h32 * h32 - 3) % p == 0
    u["A1_cube"] = pow(fx["A1"], 3, p) == (3 + r3) % p
    u["A2_cube"] = pow(fx["A2"], 3, p) == (3 - r3) % p
    u["W_units"] = fx["W1"] % p != 0 and fx["W2"] % p != 0
    u["uW_saturation"] = all(
        int(wit72["uW%d" % i]) * int(wit72["W%d" % i]) % p == 1
        for i in (1, 2))
    u["HW_law_per_side"] = all(
        fx["HW%d" % i] == env["h%d" % i] * fx["W%d" % i] % p and
        2 * env["h%d" % i] ** 2 % p == 3 % p for i in (1, 2))
    u["z_order_42"] = (pow(pt["z"], 42, p) == 1 and
                       all(pow(pt["z"], 42 // q, p) != 1
                           for q in (2, 3, 7)))
    u["scalar_denoms_units"] = all(p % q for q in (2, 3, 5, 7)) and p > 7
    checks["f3_unit_audit"] = all(u.values())
    n3, naff, support = V2.ore_affinity_gate(E, p)
    checks["f4_ore_affinity"] = bool(naff == n3)
    checks["f5_pin42_never_tangent"] = bool(
        all(r != 10 for (_f, r) in V2.GIDX))
    ok = all(checks.values())
    return {"checks": checks, "check_pass": ok,
            "status": CAND if ok else "FAIL",
            "pending": EC.PENDING["FILTER-30"],
            "unit_audit": u, "ore_bins_3plus": [n3, naff]}


# The banked band-24 frontier (cases/d25_reduce.FRONTIER, sol-round6
# 2.3 order): the ten first-occurrence tangent directions of Row 24.
FRONTIER10 = [("tf1", 19), ("tf1", 24), ("tf2", 19), ("tf2", 24),
              ("tg1", 19), ("tg1", 24), ("tg2", 19), ("tg2", 24),
              ("tg01", 24), ("tg02", 24)]
ROWS24 = [a for a in range(30) if EC.S30[a] == 6]      # the nine k=24


def frontier_solve(E, p):
    """The band-24 rank-4 frontier completion: solve the nine k = 24
    residual cells over the ten frontier columns (A24 y = -b24, kernel
    frees = 0).  Guarded by the measured level-cap: the frontier
    columns must carry NO operator entry below band 24 (the promoted
    9.S2/sect-9 finding 'bands <= 22 carry no new-at-D25 variables',
    re-measured here); returns (y dict or None, diag)."""
    Vv = E.V.astype(np.int64)
    Gg = E.G.astype(np.int64)
    cols = [V2.GIDX[fr] for fr in FRONTIER10]
    belowcap = int(Gg[:30, :24, :][:, :, cols].any())
    diag = {"frontier_entries_below_band24": bool(belowcap)}
    if belowcap:
        return None, diag
    A = [[int(Gg[a][24][c]) for c in cols] for a in ROWS24]
    b = [(-int(Vv[a][24])) % p for a in ROWS24]
    y, rk = solve_deep_zero_completion(A, b, p)
    diag["frontier_rank"] = rk
    if y is None:
        diag["frontier_inconsistent"] = True
        return None, diag
    if rk != 4:
        return None, diag
    diag["frontier_nonzero"] = sum(1 for v in y if v)
    return {FRONTIER10[j]: v for j, v in enumerate(y)}, diag


def certify_point_f(p, wit72, deep_tails, env, heavy=False):
    """eplus_certify.certify_point in the fiber frame, D = 25, with the
    band-24 frontier completion stage.  At the radical (a00pp) frame
    on a zero-frontier point this reproduces the banked tool exactly
    (--crosscheck asserts it)."""
    t0 = time.time()
    pt, r3, h32 = V.radical_env(p)
    Z = [pow(pt["z"], m, p) for m in range(42)]
    point = build_point_f(p, wit72, deep_tails, env)
    jf, jg = V2.build_jets(point, p, Z)
    E = V2.euler_rows(jf, jg, p)
    # --- band-24 frontier completion (levels 51/56; deterministic) ---
    Vv0 = E.V.astype(np.int64)
    frontier_diag = {"applied": False}
    if Vv0[:30, 24].any():
        y, fdiag = frontier_solve(E, p)
        frontier_diag.update(fdiag)
        if y is not None:
            for (fam, r), v in y.items():
                if v:
                    point["tails"][fam][r] = v
            import hashlib
            blob = json.dumps(
                {"base_zc": point["zc_hash"],
                 "frontier": sorted(("%s_%d" % k, v)
                                    for k, v in y.items())},
                sort_keys=True)
            point["zc_hash"] = hashlib.sha256(blob.encode()).hexdigest()
            jf, jg = V2.build_jets(point, p, Z)
            E = V2.euler_rows(jf, jg, p)
            frontier_diag["applied"] = True
            frontier_diag["band24_killed"] = bool(
                not E.V.astype(np.int64)[:30, :25].any())
    res = {"tool": TOOL, "prime": p, "depth_D": D, "fiber": env["label"],
           "zc_hash": point["zc_hash"],
           "frontier_completion": frontier_diag,
           "operator_hash": V2.operator_hash(E, p)}
    gates = {}
    gates["CYCLIC-30"] = EC.gate_cyclic30(E, p)
    gates["BRIDGE-30"] = gate_bridge30_f(E, p, point, env)
    gates["FILTER-30"] = gate_filter30_f(E, p, point, wit72, env)
    gates["PARAM-30"] = EC.gate_param30(E, p, D)
    if heavy:
        Z2r = pow(pt["z"], 5, p)
        Z2 = [pow(Z2r, m, p) for m in range(42)]
        jf2, jg2 = V2.build_jets(point, p, Z2)
        E2 = V2.euler_rows(jf2, jg2, p)
        gates["FILTER-30"]["checks"]["f6_zeta_branch_invariance"] = bool(
            V2.operator_hash(E2, p) == res["operator_hash"])
        DG = V2.path_A_rows(jf, jg, p)
        gates["FILTER-30"]["checks"]["f7_second_diff_path"] = bool(
            np.array_equal(DG, E.G))
        ok = all(gates["FILTER-30"]["checks"].values())
        gates["FILTER-30"]["check_pass"] = ok
        gates["FILTER-30"]["status"] = CAND if ok else "FAIL"
    res["gates"] = gates
    pr = gates["PARAM-30"]
    nu = gates["BRIDGE-30"]["nu_window"]
    ell_lb = pr["ell_lb_certified"]
    res["residual"] = {"nu_window": nu,
                       "nu_ge_D": bool(nu is None or nu >= D)}
    res["e_plus"] = {
        "certified": None,
        "certified_note": ("fail-closed: no exact all-depth causal "
                           "section is constructed (PARAM-30 pending); "
                           "there is NO promoted e+ at this point"),
        "candidate_window_floor": ell_lb,
        "tag": CAND,
        "threshold_2e1_le_D": THRESH,
        "at_or_below_threshold": bool(ell_lb <= THRESH)}
    blockers = [k for k, g in gates.items() if g["status"] != "PROVED"]
    res["certification"] = {
        "formal_germ_certified": False,
        "blockers": blockers,
        "param30_refuted_at_completion": bool(ell_lb > THRESH),
        "executable_checks_all_pass": bool(
            all(g["check_pass"] for g in gates.values()))}
    res["seconds"] = round(time.time() - t0, 1)
    return res, E


# ------------------------------------------------------------ per point
def process_point(p, lab, env, cell_idx, sample_idx, cellval,
                  heavy=False, quiet=False):
    """Cell point -> full chart point -> fiber-frame certification.
    Returns the bank record; rejection reasons are recorded, never
    silently dropped."""
    rec = {"prime": p, "fiber": lab, "cell": cell_idx,
           "sample": sample_idx,
           "W1": int(cellval["W1"]), "W2": int(cellval["W2"]),
           "kind": "witness" if sample_idx == 0 else "interior"}
    try:
        dval, diag = reconstruct_point(p, cellval, env)
        rec["reconstruction"] = diag
        checks = verify_full_point(p, dval, env,
                                   a00pp_frozen=env["is_radical_frame"])
        rec["reconstruction_checks"] = checks
        if not all(checks.values()):
            rec["verdict"] = "REJECTED"
            rec["reject_reason"] = "reconstruction checks failed"
            return rec
        wit72, deep = witness72_of(p, dval)
        res, E = certify_point_f(p, wit72, deep, env, heavy=heavy)
        rec["certify"] = EC.slim(res)
        rec["certify"]["gates"]["PARAM-30"].pop("ell_scan_profile", None)
        rec["nu_window"] = res["residual"]["nu_window"]
        rec["ell_lb_certified"] = \
            res["gates"]["PARAM-30"]["ell_lb_certified"]
        rec["window_rank"] = \
            res["gates"]["PARAM-30"]["window_rank_174x170"]
        rec["delta_plus_N1"] = res["gates"]["PARAM-30"]["delta_plus_N1"]
        rec["at_or_below_threshold"] = \
            res["e_plus"]["at_or_below_threshold"]
        rec["executable_checks_all_pass"] = \
            res["certification"]["executable_checks_all_pass"]
        rec["verdict"] = ("ACCEPTED" if
                          res["gates"]["BRIDGE-30"]["checks"]
                          ["b2_nu_window_ge_D"] else "REJECTED")
        if rec["verdict"] == "REJECTED":
            rec["reject_reason"] = ("certifier residual nu = %s < %d"
                                    % (rec["nu_window"], D))
        if not quiet:
            gs = {k: ("cand" if g["status"] == CAND else
                      ("REFUTED" if "FAIL-CERTIFIED" in g["status"]
                       else g["status"]))
                  for k, g in res["gates"].items()}
            print("p%d %s cell%02d s%d [%s]: ell+>=%d nu=%s rank=%d/174 "
                  "d+(1)=%d gates[C/B/F/P]=%s/%s/%s/%s%s (%.0fs)"
                  % (p, lab, cell_idx, sample_idx, rec["kind"],
                     rec["ell_lb_certified"], rec["nu_window"],
                     rec["window_rank"], rec["delta_plus_N1"],
                     gs["CYCLIC-30"], gs["BRIDGE-30"], gs["FILTER-30"],
                     gs["PARAM-30"],
                     "  ** <= %d **" % THRESH
                     if rec["at_or_below_threshold"] else "",
                     res["seconds"]), flush=True)
    except AssertionError as e:
        rec["verdict"] = "REJECTED"
        rec["reject_reason"] = "assert: %s" % e
        print("p%d %s cell%02d s%d: REJECTED (%s)"
              % (p, lab, cell_idx, sample_idx, e), flush=True)
    return rec


def witness_cellval(p, lab):
    """The banked derived_witness of the fiber as a 28-var cell point
    (all cell coordinates zero), verified against the raw rows."""
    hdr, rows = parse_fiber_ms(p, lab)
    dw = replay()["parked_fibers"][str(p)][lab]["derived_witness"]
    val = {x: 0 for x in CELLX}
    for k in ("W1", "W2", "uW1", "uW2"):
        val[k] = int(dw[k])
    assert val["uW1"] * val["W1"] % p == 1
    assert val["uW2"] * val["W2"] % p == 1
    bad = [ri for ri in range(34) if eval_row(rows[ri], val, p) != 0]
    assert not bad, ("banked witness fails fiber rows", lab, bad)
    return val


# ------------------------------------------------------------- stages
def selftest():
    p = 105337
    hdr, rows = parse_fiber_ms(p, "a00pp")
    cells = cells_of_fiber(p, "a00pp")
    assert len(cells) == 16
    rng = random.Random(1)
    fv = {v: rng.randrange(p) for v in FREE_BASE + FREE_LIFT}
    val = solve_cell_point(p, hdr, rows, fv, *cells[3])
    val2 = dict(val)
    val2["x57"] = (val2["x57"] + 1) % p
    nz = sum(1 for ri in range(34) if eval_row(rows[ri], val2, p) != 0)
    assert nz > 0, "negative control failed"
    env = fiber_env(p, "a00pp")
    assert env["is_radical_frame"], "a00pp is not the radical frame?"
    envx = fiber_env(p, "a11mp")
    assert not envx["is_radical_frame"]
    # frame control: fiber evaluators == banked evaluators at a00pp
    w = replay()["parked_fibers"][str(p)]["a00pp"]["derived_witness"]
    cv = witness_cellval(p, "a00pp")
    dval = full_point_f(p, cv, env)
    pt, r3, h32 = V.radical_env(p)
    rows21, vars_ = V.raw_rows21()
    for lab, v in rows21[:8]:
        v1, p1 = vexpr_vp_f(v, vars_, dval, p, r3, env)
        v0, p0, _ = V.vexpr_value_and_partials(v, vars_, dval, p, r3,
                                               pt, h32)
        assert v1 == v0 and p1 == p0, "vexpr frame mismatch at a00pp"
    for lab, d in V.row22_rows(p)[:4]:
        dv = dict(dval)
        for nm in [V.DEEPMAP[x] for x in V.DEEPX]:
            dv.setdefault(nm, 0)
        v1, p1 = msrow_vp_f(d, dv, p, env)
        v0, p0, _ = V.msrow_value_and_partials(d, dv, p, pt, h32)
        assert v1 == v0 and p1 == p0, "msrow frame mismatch at a00pp"
    print("PASS selftest: sampler (34/34 + negative control), 16 cells, "
          "fiber env legitimacy, a00pp == radical frame, fiber "
          "evaluators == banked evaluators at a00pp")


def crosscheck(out_path=None):
    """Driver fidelity: at the a00pp banked witness, certify_point_f
    must equal the UNMODIFIED cases/eplus_certify.py --file result."""
    import subprocess
    import tempfile
    ok_all = True
    for p in PRIMES:
        env = fiber_env(p, "a00pp")
        cv = witness_cellval(p, "a00pp")
        rec = process_point(p, "a00pp", env, 0, 0, cv, heavy=True)
        assert rec["verdict"] == "ACCEPTED", rec
        dval, _diag = reconstruct_point(p, cv, env)
        wit72, deep = witness72_of(p, dval)
        wf = {"prime": p, "witnesses": [{"index": 0,
              "draws": [{"witness72": wit72}],
              "deep_draws": [{"kernel_draw": 0, "deep_tails": deep}]}]}
        with tempfile.NamedTemporaryFile("w", suffix=".json",
                                         delete=False) as f:
            json.dump(wf, f)
            wfn = f.name
        with tempfile.NamedTemporaryFile(suffix=".json",
                                         delete=False) as f:
            ofn = f.name
        subprocess.run([sys.executable,
                        os.path.join(HERE, "eplus_certify.py"), "--run",
                        "--depth", "25", "--file", wfn, "--out", ofn],
                       check=True, capture_output=True)
        banked = json.load(open(ofn))["points"][0]
        mine = rec["certify"]
        same = {
            "operator_hash": banked["operator_hash"] ==
            mine["operator_hash"],
            "ell_lb": banked["gates"]["PARAM-30"]["ell_lb_certified"] ==
            mine["gates"]["PARAM-30"]["ell_lb_certified"],
            "window_rank": banked["gates"]["PARAM-30"]
            ["window_rank_174x170"] ==
            mine["gates"]["PARAM-30"]["window_rank_174x170"],
            "delta1": banked["gates"]["PARAM-30"]["delta_plus_N1"] ==
            mine["gates"]["PARAM-30"]["delta_plus_N1"],
            "nu": banked["residual"]["nu_window"] ==
            mine["gates"]["BRIDGE-30"]["nu_window"],
            "cyclic_checks": banked["gates"]["CYCLIC-30"]["checks"] ==
            mine["gates"]["CYCLIC-30"]["checks"],
            "bridge_checks": banked["gates"]["BRIDGE-30"]["checks"] ==
            mine["gates"]["BRIDGE-30"]["checks"],
            "param_checks": banked["gates"]["PARAM-30"]["checks"] ==
            mine["gates"]["PARAM-30"]["checks"],
        }
        print("crosscheck p%d vs banked eplus_certify --file: %s"
              % (p, same), flush=True)
        ok_all = ok_all and all(same.values())
        os.unlink(wfn)
        os.unlink(ofn)
    assert ok_all, "driver does not reproduce the banked tool at a00pp"
    print("PASS crosscheck: driver == banked eplus_certify at the "
          "a00pp banked witnesses, both primes (operator hash + all "
          "gate checks + ell+/rank/delta/nu)")
    return ok_all


def run_all(out_path, n_samples=3, seed=20260821, heavy_witness=False,
            witnesses_only=False):
    t00 = time.time()
    rng = random.Random(seed)
    results = []

    def checkpoint():
        if out_path:
            with open(out_path + ".ck", "w") as f:
                json.dump({"n_done": len(results),
                           "seconds": round(time.time() - t00),
                           "points": results}, f)

    # (1) the 72 banked per-fiber witnesses
    labs = sorted(replay()["parked_fibers"]["105337"])
    for p in PRIMES:
        for lab in labs:
            env = fiber_env(p, lab)
            cv = witness_cellval(p, lab)
            results.append(process_point(p, lab, env, 0, 0, cv,
                                         heavy=heavy_witness))
            if len(results) % 20 == 0:
                checkpoint()
    # (2) interior samples: a00pp x 16 cells x n at both primes,
    #     + 4 other fibers x 16 cells x n at PRIMES[0]
    if not witnesses_only:
        targets = [(p, "a00pp") for p in PRIMES] + \
                  [(PRIMES[0], lab) for lab in OTHER_FIBERS_P0]
        for p, lab in targets:
            env = fiber_env(p, lab)
            hdr, rows = parse_fiber_ms(p, lab)
            cells = cells_of_fiber(p, lab)
            for ci, (W1, W2) in enumerate(cells):
                for s in range(1, n_samples + 1):
                    fv = {v: rng.randrange(p)
                          for v in FREE_BASE + FREE_LIFT}
                    try:
                        cellval = solve_cell_point(p, hdr, rows, fv,
                                                   W1, W2)
                    except AssertionError as e:
                        results.append({
                            "prime": p, "fiber": lab, "cell": ci,
                            "sample": s, "verdict": "REJECTED",
                            "reject_reason": "sampler: %s" % e})
                        continue
                    results.append(process_point(p, lab, env, ci, s,
                                                 cellval))
                    if len(results) % 20 == 0:
                        checkpoint()
    acc = [r for r in results if r.get("verdict") == "ACCEPTED"]
    rej = [r for r in results if r.get("verdict") != "ACCEPTED"]
    ell = collections.Counter(r["ell_lb_certified"] for r in acc)
    rank = collections.Counter(r["window_rank"] for r in acc)
    nu = collections.Counter(str(r["nu_window"]) for r in acc)
    d1 = collections.Counter(r["delta_plus_N1"] for r in acc)
    n_at = sum(1 for r in acc if r["at_or_below_threshold"])
    by_fiber = {}
    for r in acc:
        key = "%d %s" % (r["prime"], r["fiber"])
        by_fiber.setdefault(key, collections.Counter())[
            r["ell_lb_certified"]] += 1
    out = {
        "tool": TOOL,
        "date": time.strftime("%Y-%m-%d"),
        "status": "INTERNAL / UNREVIEWED; fail-closed; %s only" % CAND,
        "banner": EC.BANNER,
        "depth_D": D,
        "threshold_e_le": THRESH,
        "object": ("D25 A^14 cell points (certificate sol-ideas-0821 "
                   "items 1-2; replay d25_certificate_replay.json / "
                   "9.S2) fed through the 8.S9 e+ certifier gates at "
                   "D = 25; full chart points reconstructed via the "
                   "banked CORE2 pivot back-solve + joint band-22 "
                   "tg/deep zero-completion solve; fiber frames from "
                   "the d23 atlas selector values"),
        "scope": ("mod p ONLY (105337, 105673); residue-A B-frozen "
                  "no-log W1W2 != 0 chart with PIN42; chart-local; "
                  "per the deterministic zero completion; emission-"
                  "fidelity caveat inherited; frozen a00pp emissions "
                  "applied only in the radical frame"),
        "promotion_condition": (
            "Theorem 6.1 (sol-newton-lemma.md): all four gates PROVED "
            "+ legal completion + nu >= 25 + certified e+ with "
            "2 e+ + 1 <= 25 (e+ <= 12). %s-tier results do NOT "
            "promote." % CAND),
        "sampling": {"seed": seed, "n_samples_per_cell": n_samples,
                     "witness_points": "72 = 36 fibers x 2 primes",
                     "interior_targets":
                     ["a00pp x 16 cells x both primes"] +
                     ["%s x 16 cells x p%d" % (lab, PRIMES[0])
                      for lab in OTHER_FIBERS_P0]},
        "n_points": len(results),
        "n_accepted": len(acc),
        "n_rejected": len(rej),
        "rejections": [{k: r.get(k) for k in
                        ("prime", "fiber", "cell", "sample",
                         "reject_reason")} for r in rej],
        "ell_lb_certified_distribution": {str(k): v for k, v in
                                          sorted(ell.items())},
        "window_rank_distribution": {str(k): v for k, v in
                                     sorted(rank.items())},
        "nu_window_distribution": dict(nu),
        "delta_plus_N1_distribution": {str(k): v for k, v in
                                       sorted(d1.items())},
        "n_points_at_or_below_threshold": n_at,
        "n_formal_germs_certified": 0,
        "e_plus_certified_all_points": None,
        "per_fiber_ell": {k: {str(e): n for e, n in sorted(c.items())}
                          for k, c in sorted(by_fiber.items())},
        "points": results,
        "seconds": round(time.time() - t00),
    }
    if out_path:
        with open(out_path, "w") as f:
            json.dump(out, f, indent=1, sort_keys=True)
        print("-> wrote %s" % out_path)
    print("accepted %d / rejected %d; ell+ floor distribution: %s; "
          "nu distribution: %s; at/below e+ <= %d: %d; germs "
          "certified: 0" % (len(acc), len(rej),
                            dict(sorted(ell.items())), dict(nu),
                            THRESH, n_at))
    print(EC.BANNER)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--crosscheck", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--witnesses-only", action="store_true")
    ap.add_argument("--samples", type=int, default=3)
    ap.add_argument("--seed", type=int, default=20260821)
    ap.add_argument("--heavy", action="store_true")
    ap.add_argument("--out", default=os.path.join(HERE,
                                                  "d25_eplus.json"))
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return
    if args.crosscheck:
        crosscheck()
        return
    if args.run:
        run_all(args.out, n_samples=args.samples, seed=args.seed,
                heavy_witness=args.heavy,
                witnesses_only=args.witnesses_only)
        return
    ap.print_help()


if __name__ == "__main__":
    main()
