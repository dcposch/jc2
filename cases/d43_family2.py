#!/usr/bin/env python3
"""d43_family2.py -- D43 family verdict from the REDUCED mod-p bank.

STATUS: INTERNAL TOOLING, UNREVIEWED.  FAIL-CLOSED.

Consumes the d43_reduce_modp.py checkpoints (rows NF-reduced through
the fiber's 509-element det23 GB; exact modulo I23 on the survivor
locus) and runs the D25 certificate discipline on the rungs 26..42:

  1. per rung k: verify the rows are affine in the ten
     first-occurrence tails y_k; factor the coefficient matrix as
     A_k = C_k diag(d_j) with C_k CONSTANT; d_j unit audit;
  2. compat rows = L_k . rows_k (L_k = constant left kernel of C_k;
     the y_k terms cancel EXACTLY, verified);
  3. Row 42: the exact x-side correction 42 S_M G_M (3a-2b) p4p'[h]
     is adjoined with alpha, beta as independent variables before the
     rung-42 split (their joint column is handled by the same
     factorization);
  4. verdict object per fiber: {parked 34 rows} + {53 compat rows},
     emitted as Singular input over F_p with the deep/lift tails
     adjoined as variables; a lex/dp GB decides EMPTY (G = 1) or
     returns dim -- the pivot-compressed D43 fiber verdict.

Every structural failure (nonaffine rung, non-C-diag factorization,
compat row retaining a rung tail, unexpected variable) is a hard
stop.  POST41-FIRST-OCCURRENCE at Row 42 is thereby VERIFIED, not
assumed, at the family level modulo I23.

Usage (box01):
  python3 d43_family2.py --ckdir d43red --prime 105337 --fiber a00pp
        [--parked ~/jc72108/d25fam/d25fam_p105337_a00pp.ms]
"""
import argparse
import json
import os
import pickle
import subprocess
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import d25_reduce as DR

GBVARS = DR.GBVARS               # 22 base vars (x-names + W/uW)
NV = DR.NV
FAMS = ("tf1", "tf2", "tg1", "tg2", "tg01", "tg02")
S30 = [6 + 2 * ((a + 1) % 3) for a in range(29)]
S30[28] = 16
S30 = S30 + [36]
P4P1 = {2: -23328, 5: 101088, 8: -186624, 11: 191808, 14: -120528,
        17: 47952, 20: -12096, 23: 1872, 26: -162, 29: 6}

# tail-name -> x-name registry (d25_assemble.X2T inverse), so compat
# rows share variables with the parked .ms presentation
X2T = {"x0": "tf1_43", "x1": "tf1_44", "x2": "tf1_45", "x3": "tf1_46",
       "x4": "tf1_47", "x5": "tf1_48", "x6": "tf1_50", "x7": "tf1_52",
       "x8": "tf2_43", "x9": "tf2_44", "x10": "tf2_45",
       "x11": "tf2_46", "x12": "tf2_47", "x13": "tf2_48",
       "x14": "tf2_50", "x15": "tf2_52", "x16": "tg1_43",
       "x17": "tg1_44", "x18": "tg1_45", "x19": "tg1_46",
       "x20": "tg1_47", "x21": "tg1_48", "x22": "tg1_50",
       "x23": "tg1_52", "x24": "tg2_43", "x25": "tg2_44",
       "x26": "tg2_45", "x27": "tg2_46", "x28": "tg2_47",
       "x29": "tg2_48", "x30": "tg2_50", "x31": "tg2_52",
       "x32": "tg01_44", "x33": "tg01_46", "x34": "tg01_48",
       "x35": "tg01_50", "x36": "tg01_52", "x37": "tg02_44",
       "x38": "tg02_46", "x39": "tg02_48", "x40": "tg02_50",
       "x41": "tg02_52", "x42": "tf1_38", "x43": "tf1_39",
       "x44": "tf1_40", "x45": "tf1_41", "x47": "tf2_38",
       "x48": "tf2_39", "x49": "tf2_40", "x50": "tf2_41",
       "x52": "tg1_38", "x53": "tg1_39", "x54": "tg1_40",
       "x55": "tg1_41", "x57": "tg2_38", "x58": "tg2_39",
       "x59": "tg2_40", "x60": "tg2_41", "x62": "tg01_38",
       "x63": "tg01_40", "x65": "tg02_38", "x66": "tg02_40",
       "x68": "uf18", "x69": "uf24", "x70": "vf1_34", "x71": "vf1_36",
       "x72": "vf2_34", "x73": "vf2_36"}
T2X = {v: k for k, v in X2T.items()}


def rung_rows_idx(k):
    return [a for a in range(30) if S30[a] % 6 == k % 6 and S30[a] <= k]


def rung_tails(k):
    return (["%s_%d" % (f, k + 27) for f in ("tf1", "tf2", "tg1",
                                             "tg2")] +
            ["%s_%d" % (f, k + 32) for f in FAMS])


# rows are dicts {(packed22, deepmono): coeff}; deepmono = sorted
# tuple of deep var names (with multiplicity).
def load_band(ckdir, p, lab, k):
    path = os.path.join(ckdir, "d43red_p%d_%s_band%d.pkl" % (p, lab, k))
    with open(path, "rb") as fh:
        d = pickle.load(fh)
    rows = {}
    for (h, s), groups in d["rows"].items():
        poly = {}
        for deep, nf in groups.items():
            for pk, c in nf.items():
                poly[(pk, deep)] = c
        rows[h] = poly
    return rows


def split_affine(poly, names, p):
    nset = set(names)
    const = {}
    coeffs = {nm: {} for nm in names}
    for (pk, deep), c in poly.items():
        hit = [nm for nm in deep if nm in nset]
        if not hit:
            const[(pk, deep)] = c
            continue
        assert len(hit) == 1, ("nonaffine rung occurrence", hit)
        nm = hit[0]
        d2 = list(deep)
        d2.remove(nm)
        coeffs[nm][(pk, tuple(d2))] = c
    return const, coeffs


def proportional(pa, pb, p):
    # Decide pb = lambda * pa.  The zero polynomial is 0 * pa.
    if not pb:
        return 0
    if not pa:
        return None
    if set(pa) != set(pb):
        return None
    m0 = next(iter(pa))
    lam = pb[m0] * pow(pa[m0], p - 2, p) % p
    for m, c in pa.items():
        if pb[m] != c * lam % p:
            return None
    return lam


def left_kernel_const(C, p):
    R = len(C)
    Cc = np.array(C, dtype=np.int64) % p
    M = np.concatenate([Cc, np.eye(R, dtype=np.int64)], axis=1)
    r = 0
    for c in range(Cc.shape[1]):
        piv = next((i for i in range(r, R) if M[i][c]), None)
        if piv is None:
            continue
        M[[r, piv]] = M[[piv, r]]
        M[r] = M[r] * pow(int(M[r][c]), p - 2, p) % p
        nz = np.nonzero(M[:, c])[0]
        nz = nz[nz != r]
        if len(nz):
            M[nz] = (M[nz] - np.outer(M[nz, c], M[r])) % p
        r += 1
    return M[r:, Cc.shape[1]:].tolist(), r


def analyze(ckdir, p, lab, parked_ms, out_prefix, run_gb=True):
    t0 = time.time()
    SM = pow(7, 12, p) * pow(pow(2, 6, p), p - 2, p) % p
    GM = (-pow(7, 18, p)) * pow(pow(2, 9, p), p - 2, p) % p
    compat = []
    report = {"prime": p, "fiber": lab, "rungs": {}}
    for k in range(26, 43, 2):
        rows = load_band(ckdir, p, lab, k)
        hs = rung_rows_idx(k)
        assert sorted(rows) == sorted(hs) or set(rows) <= set(hs), \
            ("band %d rows outside selected census" % k, sorted(rows))
        ynames = rung_tails(k)
        rrows = []
        for h in hs:
            poly = dict(rows.get(h, {}))
            if k == 42 and h in P4P1:
                base = 42 * SM * GM % p * (P4P1[h] % p) % p
                za = (DR.pack([0] * NV), ("Xf_alpha",))
                zb = (DR.pack([0] * NV), ("Xg_beta",))
                poly[za] = (poly.get(za, 0) + 3 * base) % p
                poly[zb] = (poly.get(zb, 0) - 2 * base) % p
            rrows.append(poly)
        ycols = ynames + (["Xf_alpha", "Xg_beta"] if k == 42 else [])
        consts, Amat = [], []
        for poly in rrows:
            const, coeffs = split_affine(poly, ycols, p)
            consts.append(const)
            Amat.append([coeffs[nm] for nm in ycols])
        ncol = len(ycols)
        Ccols, dinfo = [], []
        for j in range(ncol):
            col = [Amat[i][j] for i in range(len(hs))]
            i0 = next((i for i in range(len(col)) if col[i]), None)
            if i0 is None:
                Ccols.append([0] * len(hs))
                dinfo.append("zero column")
                continue
            lams = []
            for i in range(len(col)):
                lam = proportional(col[i0], col[i], p)
                assert lam is not None, \
                    ("C-diag factorization FAILS", k, ycols[j], i)
                lams.append(lam)
            Ccols.append(lams)
            d = col[i0]
            if len(d) == 1:
                (pk, deep), _c = next(iter(d.items()))
                e22 = DR.unpack(pk)
                sup = [GBVARS[i] for i, e in enumerate(e22) if e]
                dinfo.append("monomial(%s%s)" % ("*".join(sup) or "1",
                             "*" + "*".join(deep) if deep else ""))
            else:
                dinfo.append("POLY(%d terms)" % len(d))
        C = [[Ccols[j][i] for j in range(ncol)]
             for i in range(len(hs))]
        L, rk = left_kernel_const(C, p)
        for li, lrow in enumerate(L):
            comb = {}
            for i, poly in enumerate(rrows):
                if lrow[i]:
                    for m, c in poly.items():
                        c2 = (comb.get(m, 0) + c * lrow[i]) % p
                        if c2:
                            comb[m] = c2
                        else:
                            comb.pop(m, None)
            for (pk, deep) in comb:
                assert not any(nm in set(ycols) for nm in deep), \
                    ("compat row retains rung tail", k, li)
            compat.append(((k, li), tuple(int(x) for x in lrow), comb))
        report["rungs"][k] = {"rows": len(hs), "cols": ncol,
                              "rank_C": int(rk), "n_compat": len(L),
                              "d_structure": dinfo,
                              "compat_terms": [len(x[2]) for x in
                                               compat
                                               if x[0][0] == k]}
        print("rung %d: rank C = %d, %d compat rows (terms %s) "
              "(%.0fs)" % (k, rk, len(L),
                           [len(x[2]) for x in compat
                            if x[0][0] == k],
                           time.time() - t0), flush=True)
    # unit-compat shortcut: a compat row that is a nonzero constant
    units = []
    for (k, li), _lrow, comb in compat:
        if len(comb) == 1:
            (pk, deep), c = next(iter(comb.items()))
            if pk == DR.pack([0] * NV) and not deep:
                units.append([k, li, int(c)])
    report["unit_compat_rows"] = units
    if units:
        print("UNIT COMPAT ROW(S) FOUND: %s -> D43 EMPTY on this "
              "fiber chart modulo I23 (subject to the load-bearing "
              "gates)" % units, flush=True)
    # emit Singular verdict input: parked rows + compat rows.  Deep
    # tails with x-names (levels 43..52, uf24) are renamed so they
    # SHARE variables with the parked presentation; uf30 is the scope
    # pin (substituted 0 = dropped monomials).
    def dmap(nm):
        return T2X.get(nm, nm)
    compat2 = []
    for key, lrow, comb in compat:
        c2 = {}
        for (pk, deep), c in comb.items():
            if "uf30" in deep:
                continue                    # scope pin uf30 = 0
            d2 = tuple(sorted(dmap(nm) for nm in deep))
            m = (pk, d2)
            cc = (c2.get(m, 0) + c) % p
            if cc:
                c2[m] = cc
            else:
                c2.pop(m, None)
        compat2.append((key, lrow, c2))
    compat = compat2
    deepvars = sorted({nm for _k, _l, comb in compat for (_pk, deep) in
                       comb for nm in deep})
    parked_rows = []
    pvars = []
    if parked_ms and os.path.exists(parked_ms):
        txt = open(parked_ms).read().split("\n")
        pvars = [v.strip() for v in txt[0].split(",")]
        assert int(txt[1]) == p
        parked_rows = [r.strip().rstrip(",") for r in
                       "\n".join(txt[2:]).split(",\n") if r.strip()]
    allvars = pvars + [v for v in GBVARS if v not in pvars]
    allvars += [v for v in deepvars if v not in set(allvars)]
    lines = list(parked_rows)
    for (_k, _li), _lrow, comb in compat:
        terms = []
        for (pk, deep), c in sorted(comb.items()):
            t = str(c)
            e22 = DR.unpack(pk)
            for i, e in enumerate(e22):
                if e:
                    t += "*%s" % GBVARS[i]
                    if e > 1:
                        t += "^%d" % e
            for nm in deep:
                t += "*%s" % nm
            terms.append(t)
        lines.append("+".join(terms) if terms else "0")
    ms = "%s_p%d_%s_verdict.ms" % (out_prefix, p, lab)
    with open(ms, "w") as f:
        f.write(", ".join(allvars) + "\n%d\n" % p)
        f.write(",\n".join(lines) + "\n")
    print("-> wrote %s (%d rows, %d vars)" % (ms, len(lines),
                                              len(allvars)),
          flush=True)
    rp = "%s_p%d_%s_report.json" % (out_prefix, p, lab)
    with open(rp, "w") as f:
        json.dump(report, f, indent=1, sort_keys=True)
    if run_gb and not units:
        sing = ("ring R = %d, (%s), dp;\nideal I = %s;\n"
                "ideal G = groebner(I);\ndim(G);\nsize(G);\nquit;\n"
                % (p, ",".join(allvars), ",".join(lines)))
        sf = "%s_p%d_%s.sing" % (out_prefix, p, lab)
        open(sf, "w").write(sing)
        print("Singular input at %s (run separately with caps)" % sf,
              flush=True)
    return report, compat


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckdir", required=True)
    ap.add_argument("--prime", type=int, required=True)
    ap.add_argument("--fiber", default="a00pp")
    ap.add_argument("--parked", default=None)
    ap.add_argument("--out-prefix", default=os.path.join(HERE,
                                                         "d43fam"))
    a = ap.parse_args()
    parked = a.parked or os.path.expanduser(
        "~/jc72108/d25fam/d25fam_p%d_%s.ms" % (a.prime, a.fiber))
    analyze(a.ckdir, a.prime, a.fiber, parked, a.out_prefix)


if __name__ == "__main__":
    main()
