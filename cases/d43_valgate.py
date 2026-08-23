#!/usr/bin/env python3
"""d43_valgate.py -- FRESH independent validation gate for the rung-28
C-diag adjudication (xmodel/sol-d43-adjudication.md sects 1-3).

Deliberately does NOT import d43_family.py / d43_family2.py /
d25_reduce.py: no shared helper with the patched checker.  Reads the
d43red band checkpoints directly and verifies, per prime:

  RUNG 28 (the adjudicated rung):
   * every selected row is exactly affine in the ten first-occurrence
     tails {tf1,tf2,tg1,tg2}_55 + {tf*,tg*,tg0*}_60;
   * each coefficient column factors EXACTLY as col_i = lam_i * d_j
     with d_j = first nonzero entry -- verified by full dict-equality
     reconstruction, INCLUDING lam = 0 at the empty h=28 entries of
     the four level-55 columns (a zero polynomial IS 0 * d_j);
   * C_28 has the repeated-column shape [v1 v2 v1 v2 w1 w2 w1 w2 w1
     w2]; the v/w columns equal the published tables; the level-55
     subblock has rank 2, the level-60 subblock rank 2, C_28 rank 4;
   * the (h=1,4,7,10) x (tf1_55,tf2_55,tf1_60,tf2_60) minor and the
     canonical sha256 of the normalized 10x10 matrix match the doc;
   * the d_j leading coefficients match the doc's unit table.

  RUNG 26 (regression): the same exact A = C.diag verification;
  rank C = 4 (so 6 compat rows), unchanged from the first pass.

Exit 0 = VALIDATION GATE PASS (both rungs, this prime).
"""
import hashlib
import json
import pickle
import sys

# ---- spec data (independent transcription, sol-xside-spec / 10.4) ----
S30 = [6 + 2 * ((a + 1) % 3) for a in range(29)]
S30[28] = 16
S30 = S30 + [36]
FAMS = ("tf1", "tf2", "tg1", "tg2", "tg01", "tg02")


def rung_rows(k):
    return [a for a in range(30) if S30[a] % 6 == k % 6 and S30[a] <= k]


def rung_tails(k):
    return (["%s_%d" % (f, k + 27) for f in ("tf1", "tf2", "tg1",
                                             "tg2")] +
            ["%s_%d" % (f, k + 32) for f in FAMS])


# ---- adjudication tables (sol-d43-adjudication.md sect 3) ----
VW = {
    105337: {
        "v1": [1, 104665, 91384, 45723, 97268, 43475, 95047, 35469,
               30243, 0],
        "v2": [1, 653, 84229, 41991, 13970, 70619, 55161, 2081, 968,
               0],
        "w1": [1, 104995, 54755, 74317, 75532, 18568, 9539, 48746,
               30997, 14263],
        "w2": [1, 52989, 103316, 83592, 38664, 95506, 46556, 61953,
               101406, 65837],
    },
    105673: {
        "v1": [1, 75813, 101337, 51337, 47392, 14288, 44465, 5169,
               136, 0],
        "v2": [1, 29841, 74836, 36657, 99425, 100170, 24032, 91208,
               42916, 0],
        "w1": [1, 90737, 82002, 81599, 75320, 89143, 105388, 41195,
               41604, 4561],
        "w2": [1, 67751, 76573, 76814, 39240, 25295, 33076, 93340,
               55997, 22958],
    },
}
MINOR = {105337: 37062, 105673: 84146}
CHASH = {105337: "a9c13cbacf0e79f90cc5aab2aedd51b943bd8298"
                 "a8d308aff14c07898247e438",
         105673: "29db80727bee33eb74606e4f691bb60b2f5cce94"
                 "37505af16bbb4fba86992e06"}
DLEAD = {105337: [76028, 59451, 56593, 61740, 45896, 27173, 4515,
                  16997, 54926, 61167],
         105673: [76645, 3, 30669, 35567, 30444, 59009, 85377,
                  101558, 95525, 50779]}

FAILS = []


def check(label, ok, extra=""):
    tag = "PASS" if ok else "FAIL"
    print("  [%s] %s%s" % (tag, label, (" -- " + extra) if extra
                           else ""), flush=True)
    if not ok:
        FAILS.append(label)


def load_band(ckdir, p, lab, k):
    path = "%s/d43red_p%d_%s_band%d.pkl" % (ckdir, p, lab, k)
    with open(path, "rb") as fh:
        d = pickle.load(fh)
    rows = {}
    for (h, _s), groups in d["rows"].items():
        poly = {}
        for deep, nf in groups.items():
            for pk, c in nf.items():
                poly[(pk, deep)] = int(c)
        rows[h] = poly
    return rows


def affine_split(poly, ynames, p):
    yset = set(ynames)
    cols = {nm: {} for nm in ynames}
    const = {}
    for (pk, deep), c in poly.items():
        hits = [nm for nm in deep if nm in yset]
        if not hits:
            const[(pk, deep)] = c % p
            continue
        if len(hits) != 1:
            raise AssertionError(("NONAFFINE", hits))
        d2 = list(deep)
        d2.remove(hits[0])
        cols[hits[0]][(pk, tuple(d2))] = c % p
    return const, cols


def factor_column(col_by_row, p):
    """col_i = lam_i * d for scalars lam_i, d = first nonzero entry.
    Exact dict-equality reconstruction.  Returns (lams, d) or None."""
    i0 = next((i for i, c in enumerate(col_by_row) if c), None)
    if i0 is None:
        return [0] * len(col_by_row), None
    d = col_by_row[i0]
    m0 = sorted(d)[0]
    inv0 = pow(d[m0], p - 2, p)
    lams = []
    for c in col_by_row:
        if not c:
            # lambda = 0: the zero polynomial IS 0 * d.  Reconstruct:
            # {m: 0*d[m] mod p} == {} exactly.
            lams.append(0)
            continue
        if m0 not in c:
            return None
        lam = c[m0] * inv0 % p
        recon = {}
        for m, dc in d.items():
            v = dc * lam % p
            if v:
                recon[m] = v
        if recon != {m: cc % p for m, cc in c.items() if cc % p}:
            return None
        lams.append(lam)
    return lams, d


def rank_modp(M, p):
    M = [[x % p for x in row] for row in M]
    nr = len(M)
    nc = len(M[0]) if nr else 0
    r = 0
    for c in range(nc):
        piv = next((i for i in range(r, nr) if M[i][c]), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [x * inv % p for x in M[r]]
        for i in range(nr):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
    return r


def det_modp(M, p):
    M = [[x % p for x in row] for row in M]
    n = len(M)
    det = 1
    for c in range(n):
        piv = next((i for i in range(c, n) if M[i][c]), None)
        if piv is None:
            return 0
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            det = -det % p
        det = det * M[c][c] % p
        inv = pow(M[c][c], p - 2, p)
        for i in range(c + 1, n):
            if M[i][c]:
                f = M[i][c] * inv % p
                M[i] = [(a - f * b) % p for a, b in
                        zip(M[i], M[c])]
    return det % p


def verify_rung(ckdir, p, lab, k, expect):
    print("prime %d rung %d:" % (p, k), flush=True)
    rows = load_band(ckdir, p, lab, k)
    hs = rung_rows(k)
    check("row census within selection", set(rows) <= set(hs),
          "rows %s" % sorted(rows))
    ynames = rung_tails(k)
    colmat = []           # [row][col] -> poly dict
    for h in hs:
        _const, cols = affine_split(rows.get(h, {}), ynames, p)
        colmat.append([cols[nm] for nm in ynames])
    C = []
    dlead = []
    nzero_lam = 0
    allfac = True
    for j, nm in enumerate(ynames):
        col = [colmat[i][j] for i in range(len(hs))]
        fac = factor_column(col, p)
        if fac is None:
            allfac = False
            check("column %s factors as lam_i * d_j" % nm, False)
            C.append([0] * len(hs))
            dlead.append(None)
            continue
        lams, d = fac
        nzero_lam += lams.count(0)
        C.append(lams)
        if d is not None and len(d) == 1:
            dlead.append(next(iter(d.values())) % p)
        else:
            dlead.append("POLY(%d)" % (0 if d is None else len(d)))
    check("A_%d = C.diag(d_j) EXACT, all %d columns" % (k,
          len(ynames)), allfac)
    Crows = [[C[j][i] for j in range(len(ynames))]
             for i in range(len(hs))]
    rk = rank_modp([list(r) for r in Crows], p)
    check("rank C_%d == %d" % (k, expect["rank"]),
          rk == expect["rank"], "got %d" % rk)
    check("n_compat == %d" % (len(hs) - expect["rank"]),
          len(hs) - rk == len(hs) - expect["rank"],
          "%d rows - rank %d" % (len(hs), rk))
    if k != 28:
        return
    # ---- rung-28 adjudication cross-checks ----
    check("zero-lambda entries present (the adjudicated case)",
          nzero_lam > 0, "%d zero lambdas" % nzero_lam)
    t = VW[p]
    v1, v2, w1, w2 = t["v1"], t["v2"], t["w1"], t["w2"]
    shape = [v1, v2, v1, v2, w1, w2, w1, w2, w1, w2]
    check("C_28 == [v1 v2 v1 v2 w1 w2 w1 w2 w1 w2] published table",
          all(C[j] == shape[j] for j in range(10)))
    check("boundary row h=28: level-55 columns all zero",
          all(C[j][9] == 0 for j in range(4)))
    check("boundary row h=28: level-60 columns nonzero",
          all(C[j][9] != 0 for j in range(4, 10)))
    r55 = rank_modp([[C[j][i] for j in range(4)]
                     for i in range(10)], p)
    r60 = rank_modp([[C[j][i] for j in range(4, 10)]
                     for i in range(10)], p)
    check("level-55 subblock rank == 2", r55 == 2, "got %d" % r55)
    check("level-60 subblock rank == 2", r60 == 2, "got %d" % r60)
    sub = [[C[j][i] for j in (0, 1, 4, 5)] for i in (0, 1, 2, 3)]
    dv = det_modp(sub, p)
    check("(1,4,7,10)x(tf1_55,tf2_55,tf1_60,tf2_60) minor == %d"
          % MINOR[p], dv == MINOR[p], "got %d" % dv)
    blobs = {
        "nested": json.dumps(Crows, separators=(",", ":")),
        "flat": json.dumps([x for r in Crows for x in r],
                           separators=(",", ":")),
    }
    hits = [nm for nm, b in blobs.items()
            if hashlib.sha256(b.encode()).hexdigest() == CHASH[p]]
    check("canonical sha256 of normalized C_28 matches doc",
          bool(hits), "form %s" % (hits or "none"))
    check("d_j leading coefficients match doc unit table",
          dlead == DLEAD[p], "got %s" % dlead)


def main():
    ckdir, p, lab = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    verify_rung(ckdir, p, lab, 28, {"rank": 4})
    verify_rung(ckdir, p, lab, 26, {"rank": 4})
    if FAILS:
        print("VALIDATION GATE: FAIL (%d): %s" % (len(FAILS), FAILS),
              flush=True)
        sys.exit(1)
    print("VALIDATION GATE: PASS (prime %d, rungs 28 + 26)" % p,
          flush=True)


if __name__ == "__main__":
    main()
