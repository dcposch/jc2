#!/usr/bin/env python3
"""row22red: FLINT pre-elimination of the 22 unit pivots from
cases/directionb_row22compat_p{105337,105673,200257}.ms (72v/54eq),
per xmodel/sol-software2.md item 2 safe order:
  3 cheap low pivots -> 16 high pivots -> 3 remaining low pivots,
pseudo-dividing the pivot coordinates out of the 6 compatibility rows
(and remaining pivot rows) only; W-strip after every update; retain
the 24 CORE2 rows and the 2 uW saturation rows verbatim.

Gates: G1 unit-ness at time of use (exact, per prime); G2 round-trip
substitution >=20 random trials per prime in the ambient chart
quotient (uW_i = W_i^-1); G3 term-count/degree cap 150k; G4 shape
reconciliation vs Sol (29v/32eq/12,654t, six rows 1218x5+1216) +
cross-prime support equality; G5 emission hygiene per AUDIT.md.
"""
import sys, os, re, time, pickle, random, json

HERE = "/Users/dc/code/math/jc2/cases"
SCRATCH = os.path.dirname(os.path.abspath(__file__))  # bank lands next to script
sys.path.insert(0, HERE)
import flint

PRIMES = (105337, 105673, 200257)
CAP_TERMS = 150000
NTRIALS = 20

# frozen pivot provenance (cases/directionb_core23_{elim,emit}.py PIV22
# + D21 registry xN mapping, verified unit-linear in mapcheck):
# (artifact pivot-block index 0..21, row label, tf-name, xN)
PIVMAP = [
    (0,  (6, 2),   "tf1_38", "x42"), (1,  (8, 0),   "tf1_40", "x44"),
    (2,  (8, 3),   "tf2_40", "x49"), (3,  (12, 2),  "tf1_44", "x1"),
    (4,  (12, 5),  "tf2_44", "x9"),  (5,  (12, 8),  "tf1_39", "x43"),
    (6,  (14, 0),  "tf1_46", "x3"),  (7,  (14, 3),  "tf2_46", "x11"),
    (8,  (14, 6),  "tf1_41", "x45"), (9,  (14, 9),  "tf2_41", "x50"),
    (10, (16, 1),  "tf1_43", "x0"),  (11, (16, 4),  "tf1_48", "x5"),
    (12, (16, 7),  "tf2_43", "x8"),  (13, (16, 10), "tf2_48", "x13"),
    (14, (18, 2),  "tf1_45", "x2"),  (15, (18, 5),  "tf1_50", "x6"),
    (16, (18, 8),  "tf2_45", "x10"), (17, (18, 11), "tf2_50", "x14"),
    (18, (20, 0),  "tf1_47", "x4"),  (19, (20, 3),  "tf1_52", "x7"),
    (20, (20, 6),  "tf2_47", "x12"), (21, (20, 9),  "tf2_52", "x15"),
]
BYLAB = {lab: (i, nm, xv) for i, lab, nm, xv in PIVMAP}
# Sol item-2 elimination order: 3 cheap low, 16 high (PIV22 order),
# 3 remaining low
ORDER_LABS = ([(6, 2), (8, 0), (8, 3)]
              + [(12, 2), (12, 5), (14, 0), (14, 3), (16, 1), (16, 4),
                 (16, 7), (16, 10), (18, 2), (18, 5), (18, 8),
                 (18, 11), (20, 0), (20, 3), (20, 6), (20, 9)]
              + [(12, 8), (14, 6), (14, 9)])
assert sorted(ORDER_LABS) == sorted(BYLAB)
PIVX = {xv for _, _, _, xv in PIVMAP}

OK = []
def chk(name, cond):
    OK.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name, flush=True)

# ---------------- independent .ms parser / evaluator (no flint) ----
def parse_ms(path):
    lines = open(path).read().strip().split("\n")
    hdr = [v.strip() for v in lines[0].split(",")]
    p = int(lines[1])
    eqs = [e.strip() for e in "\n".join(lines[2:]).split(",\n")]
    return hdr, p, eqs

def parse_poly(e, p):
    d = {}
    for t in e.split("+"):
        fs = t.split("*")
        try:
            c = int(fs[0]); fs = fs[1:]
        except ValueError:
            c = 1
        mono = {}
        for f in fs:
            m = re.match(r"^([A-Za-z][A-Za-z0-9_]*)\^(\d+)$", f)
            if m:
                mono[m.group(1)] = mono.get(m.group(1), 0) + int(m.group(2))
            else:
                assert re.match(r"^[A-Za-z][A-Za-z0-9_]*$", f), f
                mono[f] = mono.get(f, 0) + 1
        k = tuple(sorted(mono.items()))
        d[k] = (d.get(k, 0) + c) % p
    return {k: c for k, c in d.items() if c}

def ev_dict(d, val, p):
    tot = 0
    for k, c in d.items():
        m = c
        for nm, e in k:
            m = m * pow(val[nm], e, p) % p
        tot = (tot + m) % p
    return tot

def tostr(d):
    parts = []
    for k in sorted(d):
        mono = [nm + ("^%d" % e if e > 1 else "") for nm, e in k]
        parts.append("%d%s" % (d[k], "*" + "*".join(mono) if mono else ""))
    return "+".join(parts)

# ------------------------------------------------------- per prime
def run_prime(p):
    t0 = time.time()
    src = "%s/directionb_row22compat_p%d.ms" % (HERE, p)
    hdr, pp, eqs = parse_ms(src)
    assert pp == p and len(hdr) == 72 and len(eqs) == 54
    art = [parse_poly(e, p) for e in eqs]
    nt_all = sum(len(d) for d in art)
    blocks = (sum(len(d) for d in art[:24]),
              sum(len(d) for d in art[24:46]),
              sum(len(d) for d in art[46:52]),
              sum(len(d) for d in art[52:]))
    chk("[p=%d] artifact census 72v/54eq/%d terms, blocks "
        "core/piv/compat/uW = %s" % (p, nt_all, blocks),
        nt_all == 48621 and blocks == (5344, 17017, 26256, 4))
    corex = {nm for d in art[:24] for k in d for nm, _ in k
             if nm.startswith("x")}
    chk("[p=%d] CORE2 rows contain no pivot vars (retained verbatim)"
        % p, not (corex & PIVX)
        and not any(nm in PIVX for d in art[52:] for k in d
                    for nm, _ in k))

    gi = {nm: j for j, nm in enumerate(hdr)}
    NV = len(hdr)
    ctx = flint.nmod_mpoly_ctx.get(tuple(hdr), modulus=p)
    def mk(d):
        out = {}
        for k, c in d.items():
            e = [0] * NV
            for nm, ex in k: e[gi[nm]] = ex
            out[tuple(e)] = c
        return ctx.from_dict(out)
    def todict(f):
        return dict(zip([tuple(m) for m in f.monoms()],
                        [int(c) for c in f.coeffs()]))
    def toname(dd):
        out = {}
        for k, c in dd.items():
            key = tuple(sorted((hdr[j], k[j]) for j in range(NV) if k[j]))
            out[key] = c
        return out
    iW1, iW2 = gi["W1"], gi["W2"]

    # working rows: 22 pivot rows + 6 compat rows
    P = {lab: mk(art[24 + i]) for i, lab, _, _ in PIVMAP}
    C = [mk(art[46 + j]) for j in range(6)]
    g1 = []           # (step, lab, nm, xv, pristine(a,b,c), atuse(a,b,c))
    atuse = []        # (lab, xv, name-dict of at-time-of-use row)
    multC = [[0] * 22 for _ in range(6)]   # pseudo-div counts, compat
    stripC = [[0, 0] for _ in range(6)]    # accumulated W-strips
    cplog = []        # (a, b, c) at-use unit monomials, order of use

    def coef_of(f, gx, want_deg=1):
        """terms with exact degree want_deg in gx, gx removed."""
        out = {}
        for k, c in todict(f).items():
            if k[gx] == want_deg:
                e = list(k); e[gx] = 0
                out[tuple(e)] = c
        return out

    def unit_mono(cd):
        """(a,b,c) if cd is a single monomial c*W1^a*W2^b else None"""
        if len(cd) != 1: return None
        (k, c), = cd.items()
        if any(k[j] for j in range(NV) if j not in (iW1, iW2)):
            return None
        return (k[iW1], k[iW2], c % p)

    def wstrip(f, acc):
        dd = todict(f)
        if not dd: return f
        a = min(k[iW1] for k in dd); b = min(k[iW2] for k in dd)
        if not a and not b: return f
        out = {}
        for k, c in dd.items():
            e = list(k); e[iW1] -= a; e[iW2] -= b
            out[tuple(e)] = c
        acc[0] += a; acc[1] += b
        return ctx.from_dict(out)

    used = []
    checkpoints = {}
    for step, lab in enumerate(ORDER_LABS):
        i, nm, xv = BYLAB[lab]
        gx = gi[xv]
        R0 = P[lab]
        assert R0.degrees()[gx] == 1, (lab, xv)
        cd = coef_of(R0, gx, 1)
        um = unit_mono(cd)
        pr_um = unit_mono(coef_of(mk(art[24 + i]), gx, 1))
        assert um is not None and um[2] % p != 0, (lab, xv, cd)
        g1.append((step, lab, nm, xv, pr_um, um))
        atuse.append((lab, xv, toname(todict(R0))))
        cplog.append(um)
        cp = ctx.from_dict({tuple(um[0] if j == iW1 else
                                  um[1] if j == iW2 else 0
                                  for j in range(NV)): um[2]})
        targets = ([("piv", l2) for l2 in P if l2 not in
                    [u for u in used] + [lab]]
                   + [("com", j) for j in range(6)])
        for kind, tj in targets:
            R = P[tj] if kind == "piv" else C[tj]
            if R.degrees()[gx] == 0: continue
            nmul = 0
            while (dg := R.degrees()[gx]) > 0:
                Ad = ctx.from_dict(coef_of(R, gx, dg))
                xm = [0] * NV; xm[gx] = dg - 1
                R = cp * R - Ad * ctx.from_dict({tuple(xm): 1}) * R0
                nmul += 1
            if kind == "com":
                R = wstrip(R, stripC[tj])
                multC[tj][step] += nmul
                C[tj] = R
            else:
                acc = [0, 0]
                R = wstrip(R, acc)   # pivot-row strips don't feed U
                P[tj] = R
        used.append(lab)
        if len(used) in (3, 19, 22):
            checkpoints[len(used)] = sum(
                len(todict(c)) for c in C)
    chk("[p=%d] G1 unit-ness: all 22 pivot coefficients single "
        "W-monomials, coef != 0 mod p, rows linear AT TIME OF USE "
        "(pristine == at-use for all: %s)" % (
            p, all(a[4] == a[5] for a in g1)),
        all(a[5] is not None and a[5][2] % p for a in g1))
    chk("[p=%d] Sol trajectory checkpoints (compat terms after "
        "3/19/22 pivots) = %s vs Sol 16458/10794/7306" % (
            p, [checkpoints[3], checkpoints[19], checkpoints[22]]),
        (checkpoints[3], checkpoints[19], checkpoints[22])
        == (16458, 10794, 7306))

    # residual pivot content must be zero everywhere
    cdicts = [toname(todict(c)) for c in C]
    okabs = not any(nm in PIVX for d in cdicts for k in d for nm, _ in k)
    chk("[p=%d] removed-variable absence: no pivot var in the 6 "
        "reduced rows" % p, okabs)

    # U_j unit multipliers (exact monomials, W-exponents may be < 0)
    U = []
    for j in range(6):
        cc = 1; e1 = 0; e2 = 0
        for s, (a, b, c) in enumerate(cplog):
            m = multC[j][s]
            if m:
                cc = cc * pow(c, m, p) % p
                e1 += m * a; e2 += m * b
        e1 -= stripC[j][0]; e2 -= stripC[j][1]
        U.append((cc, e1, e2))

    # census + emission
    nt6 = [len(d) for d in cdicts]
    xocc = sorted({nm for d in cdicts for k in d for nm, _ in k
                   if nm.startswith("x")}, key=lambda s: int(s[1:]))
    degx = max(sum(e for nm, e in k if nm.startswith("x"))
               for d in cdicts for k in d)
    degt = max(sum(e for _, e in k) for d in cdicts for k in d)
    degp = {}
    for d in cdicts:
        for k in d:
            td = sum(e for nm, e in k if nm.startswith("x"))
            degp[td] = degp.get(td, 0) + 1
    core_str = eqs[:24]; uw_str = eqs[52:]
    body = core_str + [tostr(d) for d in cdicts] + uw_str
    occ = sorted({nm for e in body
                  for nm in re.findall(r"[A-Za-z][A-Za-z0-9_]*", e)})
    allv = [v for v in occ if v not in ("uW1", "uW2")] + ["uW1", "uW2"]
    ntot = sum(len(parse_poly(e, p)) for e in body)
    shape = (len(allv), len(body), ntot)
    chk("[p=%d] G3 fill-in cap: %d terms <= %d" % (p, ntot, CAP_TERMS),
        ntot <= CAP_TERMS)
    chk("[p=%d] G4 SHAPE vs Sol: %s == (29, 32, 12654); six-row "
        "sizes %s == [1218 x5, 1216]; %d x-vars == 25 (contains "
        "core's 18: %s); deg_x=%d deg_tot=%d (Sol: degree 9)" % (
            p, shape, sorted(nt6), len(xocc),
            corex <= set(xocc), degx, degt),
        shape == (29, 32, 12654) and sorted(nt6) == [1216] + [1218] * 5
        and len(xocc) == 25 and corex <= set(xocc))

    path = "%s/directionb_row22red_p%d.ms" % (HERE, p)
    with open(path, "w") as f:
        f.write(", ".join(allv) + "\n%d\n" % p)
        f.write(",\n".join(body) + "\n")
    txt = open(path).read()
    sz = os.path.getsize(path)
    # G5 hygiene
    coefs_ok = True
    for e in body:
        for t in e.split("+"):
            tok = t.split("*")[0]
            if tok[0].isdigit():
                coefs_ok &= (0 <= int(tok) < p)
        for m in re.finditer(r"\^(\d+)", e):
            coefs_ok &= int(m.group(1)) < 64
    h2, p2, e2 = parse_ms(path)
    rt = (p2 == p and len(e2) == 32 and h2 == allv
          and e2[:24] == core_str and e2[30:] == uw_str
          and all(parse_poly(e2[24 + j], p) == cdicts[j]
                  for j in range(6)))
    noconst = not any(len(d) == 1 and next(iter(d)) == ()
                      for d in [parse_poly(e, p) for e in body])
    chk("[p=%d] G5 emission hygiene: paren-free, coeffs in [0,p), "
        "independent re-parse round-trip (24 core + 2 uW byte-"
        "identical to parent, 6 reduced exact), no bare-constant "
        "row, %d bytes" % (p, sz),
        "(" not in txt and ")" not in txt and coefs_ok and rt
        and noconst)

    # ---- G2 round-trip, NTRIALS random points in the chart quotient
    art_piv = [art[24 + i] for i, _, _, _ in PIVMAP]
    surv_idx = list(range(24)) + list(range(46, 52)) + [52, 53]
    red_parsed = [parse_poly(e, p) for e in e2]
    ok2 = True
    rng = random.Random(72108 + p)
    for t in range(NTRIALS):
        val = {nm: rng.randrange(p) for nm in hdr}
        for w in ("W1", "W2"):
            while val[w] == 0: val[w] = rng.randrange(p)
        val["uW1"] = pow(val["W1"], p - 2, p)
        val["uW2"] = pow(val["W2"], p - 2, p)
        # back-solve pivot coords, reverse at-time-of-use order
        for (lab, xv, rd), (a, b, c) in zip(reversed(atuse),
                                            reversed(cplog)):
            v0 = dict(val); v0[xv] = 0
            rest = ev_dict({k: cc for k, cc in rd.items()
                            if dict(k).get(xv, 0) == 0}, v0, p)
            cpv = c * pow(val["W1"], a, p) * pow(val["W2"], b, p) % p
            ok2 &= (cpv != 0)
            val[xv] = (-rest) * pow(cpv, p - 2, p) % p
        # (i) unique lift satisfies ALL 22 pristine artifact pivot rows
        ok2 &= all(ev_dict(d, val, p) == 0 for d in art_piv)
        # (ii) equivalence identity on the 32 surviving rows:
        # reduced_j(y) == U_j(pt) * full_j(lift), U_j != 0
        for jj, ai in enumerate(surv_idx):
            full = ev_dict(art[ai], val, p)
            red = ev_dict(red_parsed[jj], val, p)
            if 24 <= jj < 30:
                cc, ee1, ee2 = U[jj - 24]
                u = cc * pow(val["W1"] if ee1 >= 0 else val["uW1"],
                             abs(ee1), p) \
                       * pow(val["W2"] if ee2 >= 0 else val["uW2"],
                             abs(ee2), p) % p
            else:
                u = 1
            ok2 &= (u != 0 and red == u * full % p)
        if not ok2:
            print("   trial %d FAILED" % t); break
    chk("[p=%d] G2 round-trip: %d random chart-quotient trials -- "
        "unique unit back-solve of 22 pivots, all pristine pivot "
        "rows vanish at lift, reduced == unit * full on all 32 "
        "surviving rows (both directions of the correspondence)"
        % (p, NTRIALS), ok2)

    print("   [p=%d] wall %.1fs" % (p, time.time() - t0), flush=True)
    return {"shape": shape, "nt6": nt6, "xocc": xocc, "degx": degx,
            "degt": degt, "degp": dict(sorted(degp.items())),
            "g1": g1, "U": U, "strips": stripC, "sz": sz,
            "support": [tuple(sorted(d)) for d in cdicts],
            "core_support": [tuple(sorted(parse_poly(e, p)))
                             for e in core_str],
            "checkpoints": checkpoints}

res = {}
for p in PRIMES:
    res[p] = run_prime(p)
# cross-prime support equality (coefficients differ, supports must not)
s0 = res[PRIMES[0]]
oksup = all(res[p]["support"] == s0["support"]
            and res[p]["core_support"] == s0["core_support"]
            and res[p]["xocc"] == s0["xocc"]
            for p in PRIMES[1:])
chk("cross-prime support equality: identical monomial support of all "
    "30 nontrivial rows + identical 25 x-vars at 105337/105673/200257",
    oksup)
okg1 = all(tuple((a[1], a[3]) for a in res[p]["g1"])
           == tuple((a[1], a[3]) for a in res[PRIMES[0]]["g1"])
           for p in PRIMES)
chk("cross-prime pivot log: same (label, var) sequence at all primes",
    okg1)
pickle.dump(res, open(SCRATCH + "/row22red_bank.pkl", "wb"))
bad = [n for n, c in OK if not c]
print("\nROW22RED TOTAL: %d checks, %d FAIL %s" % (len(OK), len(bad),
                                                   bad or ""))
sys.exit(1 if bad else 0)
