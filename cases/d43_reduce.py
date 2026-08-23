#!/usr/bin/env python3
"""D43 base-coefficient reduction stage (D43 family compiler, step 1).

Direct adaptation of the banked cases/d25_reduce.py (the D25RED stage)
to the D43 jets bank (build_tails43.py, DBUILD 43, tails through
absolute level 74): expand each deep (Row_22..Row_42) eta-component jet
of the D = 43 full-live window build as  c(z,a) = sum_alpha h_alpha(z)
a^alpha,  z = the 22 det23 base variables, a = the unresolved deep tail
variables (now levels 43..74), and reduce every base coefficient
h_alpha through the cached 509-element det23 G23 basis of each atlas
fiber, saving normal forms AND membership traces.

CONSUMED ROWS: every even k = 22..42 (the D25 stage consumed 22/24
only).  Row eta-support gates per the proved pure-y grading + the D43
spec (xmodel/sol-xside-spec.md sect 6): k%6==2 -> {0,3,..,27},
k%6==4 -> {1,4,..,28}, k%6==0 -> {2,5,..,26} plus eta 29 exactly for
k = 36, 42 (the H29 components; H29u0/H29u1).  Odd rows must be absent
(POST41-GRADING is NOT consumed: an odd row in the bank fails the
load gate and stops the stage).  Frontier census: every provisional
first-occurrence tail of rungs 26..42 (levels k+27 / k+32) must occur.

Same checkpoint layout/discipline as d25_reduce (resume-safe, atomic),
under <root>/d43/ckpt with the D43 bank <root>/d43/
directionb_tails_D43.pkl (or --bank PATH).

Usage:  d43_reduce.py <prime> [--workers N] [--limit N]
                      [--fibers lbl1,lbl2] [--ckpt-dir NAME]
                      [--bank PATH]
"""
import argparse
import heapq
import json
import os
import pickle
import socket
import sys
import time
import zlib
from fractions import Fraction
from multiprocessing import Pool

# ----------------------------------------------------------------- ring
GBVARS = ["x68", "x70", "x71", "x72", "x73", "x47", "x52", "x53", "x54",
          "x55", "x57", "x58", "x59", "x60", "x62", "x63", "x65", "x66",
          "W1", "W2", "uW1", "uW2"]
X2TAIL = {"x68": "uf18", "x70": "vf1_34", "x71": "vf1_36",
          "x72": "vf2_34", "x73": "vf2_36", "x47": "tf2_38",
          "x52": "tg1_38", "x53": "tg1_39", "x54": "tg1_40",
          "x55": "tg1_41", "x57": "tg2_38", "x58": "tg2_39",
          "x59": "tg2_40", "x60": "tg2_41", "x62": "tg01_38",
          "x63": "tg01_40", "x65": "tg02_38", "x66": "tg02_40"}
TAIL2POS = {X2TAIL[x]: i for i, x in enumerate(GBVARS) if x in X2TAIL}
BASE18 = set(TAIL2POS)
NV = len(GBVARS)                      # 22
SH = 8
IW1, IW2 = GBVARS.index("W1"), GBVARS.index("W2")
FULL = sum(0xFF << (SH * i) for i in range(NV))
GUARD = sum(0x80 << (SH * i) for i in range(NV))
DEGSH = SH * NV                       # 176
M176 = (1 << DEGSH) - 1

FRONTIER = ("tf1_51", "tf1_56", "tf2_51", "tf2_56", "tg1_51", "tg1_56",
            "tg2_51", "tg2_56", "tg01_56", "tg02_56")

def pack(exps):
    s = 0
    for i, e in enumerate(exps):
        if e: s |= e << (SH * i)
    return s

def unpack(s):
    return tuple((s >> (SH * i)) & 0xFF for i in range(NV))

def degof(s):
    d = 0
    while s:
        d += s & 0xFF
        s >>= SH
    return d

def gkey(s, deg):
    return (deg << DEGSH) + (FULL - s)

def from_gkey(K):
    return FULL - (K & M176), K >> DEGSH

# ------------------------------------------------------------ GB parse
def parse_msolve_gb(path, p):
    """msolve -g 2 GB .out -> (gvars, [(lt_s, lt_deg, tail=[(s,deg,c)..])]).
    Gates: characteristic, variable order, 509 elements, monic, and
    first-printed term == unique grevlex max (order pin, every element)."""
    txt = open(path).read()
    lines = txt.split("\n")
    ch = next(l for l in lines if l.startswith("#field characteristic"))
    assert int(ch.split(":")[1]) == p, (path, ch)
    vo = next(l for l in lines if l.startswith("#variable order"))
    gvars = [v.strip() for v in vo.split(":")[1].split(",")]
    assert gvars == GBVARS, (path, gvars)
    body = txt.split("#---")[-1].strip()
    assert body.startswith("[") and body.rstrip(":").endswith("]"), path
    body = body.lstrip("[").rstrip(":").rstrip("]")
    vi = {v: i for i, v in enumerate(gvars)}
    gb = []
    for spoly in body.split(",\n"):
        terms = []
        for t in spoly.strip().split("+"):
            fs = t.split("*")
            c = int(fs[0]) % p
            e = [0] * NV
            for f in fs[1:]:
                if "^" in f:
                    nm, ex = f.split("^")
                    e[vi[nm]] += int(ex)
                else:
                    e[vi[f]] += 1
            terms.append((pack(e), sum(e), c))
        lt_s, lt_deg, lt_c = terms[0]
        assert lt_c == 1, ("non-monic", path, spoly[:60])
        ltk = gkey(lt_s, lt_deg)
        assert all(gkey(s, d) < ltk for s, d, _ in terms[1:]), \
            ("order pin failed", path, spoly[:60])
        gb.append((lt_s, lt_deg, terms[1:]))
    assert len(gb) == 509, (path, len(gb))
    return gb

# ----------------------------------------------------------- reduction
def nf_trace(poly, gb, p):
    """Full normal form of poly (dict packed_s -> coeff) against the
    monic grevlex GB.  Returns (nf_dict, trace {gk_idx: {q_s: coeff}},
    steps).  Identity: poly == nf + sum_k trace[k]*gb[k]  in F_p[x]."""
    H = dict(poly)
    heap = [-gkey(s, degof(s)) for s in H]
    heapq.heapify(heap)
    out, trace, steps = {}, {}, 0
    nlt = len(gb)
    while heap:
        K = -heapq.heappop(heap)
        s, deg = from_gkey(K)
        c = H.get(s)
        if not c:
            continue
        gi = -1
        X = s | GUARD
        for j in range(nlt):
            lt_s, lt_deg, _ = gb[j]
            if lt_deg <= deg and ((X - lt_s) & GUARD) == GUARD:
                gi = j
                break
        if gi < 0:
            out[s] = c
            del H[s]
            continue
        lt_s, lt_deg, tail = gb[gi]
        q = s - lt_s
        qdeg = deg - lt_deg
        tr = trace.setdefault(gi, {})
        tr[q] = (tr.get(q, 0) + c) % p
        del H[s]
        for ts, tdeg, tc in tail:
            m = q + ts
            nc = (H.get(m, 0) - c * tc) % p
            if nc:
                if m not in H:
                    heapq.heappush(heap, -gkey(m, qdeg + tdeg))
                H[m] = nc
            else:
                H.pop(m, None)
        steps += 1
    assert not H
    return out, trace, steps

# ------------------------------------------------------- bank -> exprs
def load_exprs(pkl_path, p):
    """Jets bank -> {name: {(k,n): [(s_item, e1,e2,h1,h2, c0m,c1m)..]}}.
    Spec-2.3-adjacent gates on the bank are asserted here."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(pkl_path)))
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    with open(pkl_path, "rb") as fh:
        d = pickle.load(fh)
    assert d["D"] == 43, "not the D43 bank"
    vars_, byk = d["vars"], d["byk"]
    assert all(k % 2 == 0 for k in byk), \
        "odd row present (pure-y grading violated; POST41 not consumed)"
    for k in range(22, 43, 2):
        assert k in byk, "Row %d missing from the D43 bank" % k
        want = {2: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27],
                4: [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],
                0: [2, 5, 8, 11, 14, 17, 20, 23, 26]}[k % 6]
        if k in (36, 42):
            want = sorted(want + [29])
        assert sorted(byk[k]) == want, \
            ("Row %d eta support mismatch" % k, sorted(byk[k]), want)
    exprs = {}
    deepseen = set()
    for k in range(22, 43, 2):
        for n, vex in byk[k].items():
            for key, r in vex.items():
                epos = [0] * NV
                deep = []
                for i in key:
                    nm = vars_[i]
                    if nm in BASE18:
                        epos[TAIL2POS[nm]] += 1
                    else:
                        deep.append(nm)
                deep = tuple(sorted(deep))
                deepseen.update(deep)
                name = "*".join(deep) if deep else "const"
                items = exprs.setdefault(name, {}).setdefault((k, n), [])
                for (za, e1, e2, pw, h1, qw, h2, eB), c in r.items():
                    assert za == 0 and eB == 0, "unexpected z/EB content"
                    e = list(epos)
                    e[IW1] += pw + h1
                    e[IW2] += qw + h2
                    c0, c1 = Fraction(c[0]), Fraction(c[1])
                    c0m = c0.numerator % p * pow(c0.denominator % p,
                                                 p - 2, p) % p
                    c1m = c1.numerator % p * pow(c1.denominator % p,
                                                 p - 2, p) % p
                    items.append((pack(e), e1, e2, h1, h2, c0m, c1m))
    for nm in FRONTIER:                       # D25 frontier census
        assert nm in deepseen, "frontier var %s absent from deep set" % nm
    for k in range(26, 43, 2):                # D43 rung frontier census
        for f in ("tf1", "tf2", "tg1", "tg2"):
            nm = "%s_%d" % (f, k + 27)
            assert nm in deepseen, "rung-%d var %s absent" % (k, nm)
        for f in ("tf1", "tf2", "tg1", "tg2", "tg01", "tg02"):
            nm = "%s_%d" % (f, k + 32)
            assert nm in deepseen, "rung-%d var %s absent" % (k, nm)
    return exprs

# ----------------------------------------------------------- workers
G = {}

def _init(gbs, fvals, r3v, p, ckdir, logpath):
    G.update(gbs=gbs, fvals=fvals, r3=r3v, p=p, ckdir=ckdir, log=logpath)

def _logline(msg):
    fd = os.open(G["log"], os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
    try:
        os.write(fd, (msg + "\n").encode())
    finally:
        os.close(fd)

def reduce_expr(task):
    name, cells = task
    p, r3v = G["p"], G["r3"]
    t0 = time.time()
    fname = "red_p%d_%s.pkl" % (p, name.replace("*", "."))
    path = os.path.join(G["ckdir"], fname)
    if os.path.exists(path):
        return (name, "skip", 0, 0, 0, 0.0)
    fibers = {}
    tin = tnf = tst = 0
    for lab in sorted(G["gbs"]):
        gb = G["gbs"][lab]
        fv = G["fvals"][lab]
        A1, A2 = fv["A1"], fv["A2"]
        hw1, hw2 = fv["HW1_over_W1"], fv["HW2_over_W2"]
        out = {}
        for (k, n), items in sorted(cells.items()):
            poly = {}
            for s, e1, e2, h1, h2, c0m, c1m in items:
                c = (c0m + c1m * r3v) % p
                c = c * pow(A1, e1, p) % p * pow(A2, e2, p) % p
                c = c * pow(hw1, h1, p) % p * pow(hw2, h2, p) % p
                if c:
                    nc = (poly.get(s, 0) + c) % p
                    if nc: poly[s] = nc
                    else: poly.pop(s, None)
            nf, trace, steps = nf_trace(poly, gb, p)
            out[(k, n)] = {
                "nf": {unpack(s): c for s, c in nf.items()},
                "in_terms": len(poly), "steps": steps,
                "trace_z": zlib.compress(pickle.dumps(
                    trace, protocol=4), 6)}
            tin += len(poly); tnf += len(nf); tst += steps
        fibers[lab] = out
    payload = dict(prime=p, name=name,
                   alpha=tuple(name.split("*")) if name != "const" else (),
                   gbvars=GBVARS, r3=r3v, fiber_vals=G["fvals"],
                   fibers=fibers, elapsed=time.time() - t0,
                   host=socket.gethostname(),
                   ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    tmp = path + ".tmp.%d" % os.getpid()
    with open(tmp, "wb") as fh:
        pickle.dump(payload, fh, protocol=4)
    os.replace(tmp, path)
    dt = time.time() - t0
    _logline("%s p%d REDUCED %-28s cells=%2d fibers=%2d in=%6d nf=%6d "
             "steps=%7d secs=%.1f"
             % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), p,
                name, len(cells), len(fibers), tin, tnf, tst, dt))
    return (name, "done", tin, tnf, tst, dt)

# --------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prime", type=int)
    ap.add_argument("--workers", type=int, default=28)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--fibers", default="")
    ap.add_argument("--ckpt-dir", default="ckpt")
    ap.add_argument("--bank", default=None)
    a = ap.parse_args()
    p = a.prime
    root = os.environ.get("D25_ROOT", os.path.expanduser("~/jc72108"))
    d25 = os.path.join(root, "d43")
    d25gb = os.path.join(root, "d25")
    ckdir = os.path.join(d25, a.ckpt_dir)
    os.makedirs(ckdir, exist_ok=True)
    logp = os.path.join(d25, "reduce_p%d.log" % p)
    t0 = time.time()

    def log(m):
        line = "%s p%d %s" % (time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                            time.gmtime()), p, m)
        print(line, flush=True)
        with open(logp, "a") as fh:
            fh.write(line + "\n")

    with open(os.path.join(d25, "d43red_p%d.pid" % p), "w") as fh:
        fh.write("%d\n" % os.getpid())
    jpath = os.path.join(d25gb, "d23_atlas_p%d.json" % p)
    if not os.path.exists(jpath):
        jpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "d23_atlas_p%d.json" % p)
    atlas = json.load(open(jpath))
    assert atlas["meta"]["prime"] == p
    labels = sorted(atlas["fibers"])
    if a.fibers:
        labels = [l for l in labels if l in a.fibers.split(",")]
    else:
        assert len(labels) == 36, labels
    fvals = {l: atlas["fibers"][l]["fiber"] for l in labels}

    # r3 + radical-law gates from the banked fiber values (no
    # convention re-derivation; sol-round6 gate-1 adjacent)
    ref = atlas["fibers"]["a00pp"]["fiber"]
    r3v = (pow(ref["A1"], 3, p) - 3) % p
    assert pow(r3v, 2, p) == 3, "r3 branch"
    for l in labels:
        fv = fvals[l]
        assert pow(fv["A1"], 3, p) == (3 + r3v) % p, ("A1 law", l)
        assert pow(fv["A2"], 3, p) == (3 - r3v) % p, ("A2 law", l)
        for hk in ("HW1_over_W1", "HW2_over_W2"):
            assert 2 * pow(fv[hk], 2, p) % p == 3, ("h32 law", l, hk)
    log("start host=%s pid=%d root=%s r3=%d fibers=%d workers=%d"
        % (socket.gethostname(), os.getpid(), root, r3v, len(labels),
           a.workers))

    # GBs (cached parse; gates inside parse_msolve_gb)
    gbs = {}
    for l in labels:
        src = (os.path.join(d25gb, "det_a00pp_p%d.out" % p)
               if l == "a00pp"
               else os.path.join(root, "atlas", "det_%s_p%d.out" % (l, p)))
        cache = os.path.join(d25gb, "gbcache_p%d_%s.pkl" % (p, l))
        if os.path.exists(cache):
            with open(cache, "rb") as fh:
                gbs[l] = pickle.load(fh)
        else:
            gbs[l] = parse_msolve_gb(src, p)
            tmp = cache + ".tmp.%d" % os.getpid()
            with open(tmp, "wb") as fh:
                pickle.dump(gbs[l], fh, protocol=4)
            os.replace(tmp, cache)
    skel = [(lt, [s for s, _, _ in tail])
            for lt, _, tail in gbs[labels[0]]]
    for l in labels[1:]:                    # cross-fiber support identity
        assert [(lt, [s for s, _, _ in tail])
                for lt, _, tail in gbs[l]] == skel, \
            ("det-GB support skeleton mismatch", l)
    log("GBs loaded: %d fibers x 509 els; support skeleton identical"
        % len(labels))
    # G4: NF(G_el) == 0 and NF(1) == 1 on a sample fiber
    gtest = gbs[labels[0]]
    for j in (0, 254, 508):
        lt_s, lt_deg, tail = gtest[j]
        poly = {lt_s: 1}
        for ts, _, tc in tail:
            poly[ts] = (poly.get(ts, 0) + tc) % p
        nf0, _, _ = nf_trace({s: c for s, c in poly.items() if c},
                             gtest, p)
        assert not nf0, ("NF(G[%d]) != 0" % j)
    nf1, _, _ = nf_trace({0: 1}, gtest, p)
    assert nf1 == {0: 1}, "NF(1) != 1"
    log("gates: order pin x%d els, monic, NF(G)=0 x3, NF(1)=1 PASS"
        % (509 * len(labels)))

    exprs = load_exprs(a.bank or os.path.join(d25,
                       "directionb_tails_D43.pkl"), p)
    sizes = {nm: sum(len(it) for it in cells.values())
             for nm, cells in exprs.items()}
    todo = sorted(exprs, key=lambda nm: -sizes[nm])
    if a.limit:
        todo = todo[:a.limit]
    done0 = [nm for nm in todo if os.path.exists(os.path.join(
        ckdir, "red_p%d_%s.pkl" % (p, nm.replace("*", "."))))]
    todo = [nm for nm in todo if nm not in set(done0)]
    log("exprs=%d (bank total %d) already-done=%d todo=%d biggest=%s(%d)"
        % (len(todo) + len(done0), len(exprs), len(done0), len(todo),
           todo[0] if todo else "-", sizes[todo[0]] if todo else 0))

    tasks = [(nm, exprs[nm]) for nm in todo]
    nred = nfail = 0
    if tasks:
        with Pool(a.workers, _init,
                  (gbs, fvals, r3v, p, ckdir, logp)) as pool:
            for nm, st, tin, tnf, tst, dt in pool.imap_unordered(
                    reduce_expr, tasks, chunksize=1):
                if st == "done": nred += 1
    log("DONE reduced=%d skipped=%d failed=%d wall=%.0fs"
        % (nred, len(done0), nfail, time.time() - t0))
    return 0

if __name__ == "__main__":
    sys.exit(main())
