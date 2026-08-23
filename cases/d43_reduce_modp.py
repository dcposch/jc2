#!/usr/bin/env python3
"""d43_reduce_modp.py -- NF-reduce the mod-p D43 bank through det23.

STATUS: INTERNAL TOOLING, UNREVIEWED.  FAIL-CLOSED.

Consumes the per-(prime, fiber) mod-p symbolic bank
(cases/build_tails_modp.py) and reduces it exactly as the banked
D25RED stage (cases/d25_reduce.py) reduced the char-0 bank: every row
(eta h, band s) is expanded as

    row = sum_alpha  deep-monomial_alpha * h_alpha(z),
    z = the 22 det23 base variables (18 template tails + uf18 + vf's
        + W1, W2; d25_reduce.GBVARS order),

and every base coefficient h_alpha is replaced by its full normal form
through the cached 509-element det23 Groebner basis of the fiber
(d25_reduce.nf_trace; the gbcache pickles on box01).  Working modulo
I23 is exact for every object supported on the D25/D43 survivor locus.

Deep variables here: uf24, uf30, every tail level 42..74 not in the
22-var base (the lift-level tails 43..56 and the nine-rung
first-occurrence tails 57..74).  PIN42 tails (level 42) are DROPPED
(the chart pin, load_nolog convention).

Output: <ckdir>/d43red_p<P>_<LAB>_band<k>.pkl per band (atomic,
resume-safe), payload {(h, s): {deep-mono: nf-poly}} with nf-poly a
dict {exp22-tuple: coeff}; plus a summary json.

Usage (box01):
  python3 d43_reduce_modp.py --bank d43modp_p105337_a00pp.pkl
      [--gbdir ~/jc72108/d25] [--workers 48] [--bands 26,28,...]
"""
import argparse
import json
import os
import pickle
import sys
import time
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import d25_reduce as DR

GBVARS = DR.GBVARS
TAIL2POS = dict(DR.TAIL2POS)
TAIL2POS["uf18"] = GBVARS.index("x68")
TAIL2POS["vf1_34"] = GBVARS.index("x70")
TAIL2POS["vf1_36"] = GBVARS.index("x71")
TAIL2POS["vf2_34"] = GBVARS.index("x72")
TAIL2POS["vf2_36"] = GBVARS.index("x73")
IW1, IW2 = DR.IW1, DR.IW2

G = {}


def _init(gb, p, vars_, ckdir):
    G.update(gb=gb, p=p, vars=vars_, ckdir=ckdir)


def classify(vars_):
    """vid -> ('base', pos22) | ('deep', name) | ('drop', None) for
    PIN42-level tails."""
    out = []
    for nm in vars_:
        if nm == "W1":
            out.append(("base", IW1))
        elif nm == "W2":
            out.append(("base", IW2))
        elif nm in TAIL2POS:
            out.append(("base", TAIL2POS[nm]))
        elif nm.endswith("_42"):
            out.append(("drop", None))          # PIN42 chart pin
        else:
            out.append(("deep", nm))
    return out


def reduce_cell(task):
    (h, s), poly = task
    p = G["p"]
    gb = G["gb"]
    cls = G["cls"]
    t0 = time.time()
    groups = {}
    ndrop = 0
    for m, c in poly.items():
        e22 = [0] * DR.NV
        deep = []
        drop = False
        for vid, e in m:
            kind, val = cls[vid]
            if kind == "base":
                e22[val] += e
            elif kind == "deep":
                deep.extend([val] * e)
            else:
                drop = True
                break
        if drop:
            ndrop += 1
            continue
        key = tuple(sorted(deep))
        gpoly = groups.setdefault(key, {})
        pk = DR.pack(e22)
        c2 = (gpoly.get(pk, 0) + c) % p
        if c2:
            gpoly[pk] = c2
        else:
            gpoly.pop(pk, None)
    out = {}
    tin = tnf = 0
    for key, gpoly in groups.items():
        gpoly = {k: c for k, c in gpoly.items() if c}
        if not gpoly:
            continue
        tin += len(gpoly)
        nf, _trace, _steps = DR.nf_trace(gpoly, gb, p)
        if nf:
            out[key] = nf
            tnf += len(nf)
    return (h, s), out, tin, tnf, ndrop, time.time() - t0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bank", required=True)
    ap.add_argument("--gbdir", default=os.path.expanduser(
        "~/jc72108/d25"))
    ap.add_argument("--workers", type=int, default=48)
    ap.add_argument("--bands", default=None,
                    help="comma list; default all")
    ap.add_argument("--ckdir", default=None)
    a = ap.parse_args()
    t0 = time.time()
    with open(a.bank, "rb") as fh:
        B = pickle.load(fh)
    p = B["prime"]
    lab = B["fiber"]
    vars_ = B["vars"]
    cls = classify(vars_)
    ckdir = a.ckdir or os.path.join(os.path.dirname(
        os.path.abspath(a.bank)), "d43red")
    os.makedirs(ckdir, exist_ok=True)
    cache = os.path.join(a.gbdir, "gbcache_p%d_%s.pkl" % (p, lab))
    with open(cache, "rb") as fh:
        gb = pickle.load(fh)
    assert len(gb) == 509
    print("bank p=%d %s: %d vars; GB 509 els; ckdir %s"
          % (p, lab, len(vars_), ckdir), flush=True)
    bands = ([int(x) for x in a.bands.split(",")] if a.bands
             else sorted(B["byk"]))
    summary = {}
    for s in bands:
        ck = os.path.join(ckdir, "d43red_p%d_%s_band%d.pkl"
                          % (p, lab, s))
        if os.path.exists(ck):
            print("band %d: checkpoint exists, skip" % s, flush=True)
            continue
        comps = B["byk"][s]
        tasks = [((h, s), poly) for h, poly in sorted(comps.items())]
        res = {}
        stats = []
        G.update(gb=gb, p=p, vars=vars_, cls=cls, ckdir=ckdir)
        if a.workers > 1 and len(tasks) > 1:
            with Pool(min(a.workers, len(tasks)), _init,
                      (gb, p, vars_, ckdir)) as pool:
                pool_G = None
                for (hs, out, tin, tnf, nd, dt) in pool.imap_unordered(
                        _reduce_cell_mp, tasks, chunksize=1):
                    res[hs] = out
                    stats.append((hs, tin, tnf, nd, dt))
                    print("  band %d eta %d: %d deep-monos, in %d -> "
                          "nf %d terms, drop %d, %.0fs"
                          % (s, hs[0], len(out), tin, tnf, nd, dt),
                          flush=True)
        else:
            for task in tasks:
                hs, out, tin, tnf, nd, dt = reduce_cell(task)
                res[hs] = out
                stats.append((hs, tin, tnf, nd, dt))
                print("  band %d eta %d: %d deep-monos, in %d -> nf "
                      "%d, drop %d, %.0fs"
                      % (s, hs[0], len(out), tin, tnf, nd, dt),
                      flush=True)
        tmp = ck + ".tmp.%d" % os.getpid()
        with open(tmp, "wb") as fh:
            pickle.dump({"prime": p, "fiber": lab, "band": s,
                         "gbvars": GBVARS, "rows": res}, fh,
                        protocol=4)
        os.replace(tmp, ck)
        summary[s] = [[list(hs), tin, tnf, nd, round(dt, 1)]
                      for hs, tin, tnf, nd, dt in stats]
        print("band %d banked (%.0fs total)" % (s, time.time() - t0),
              flush=True)
    sp = os.path.join(ckdir, "d43red_p%d_%s_summary.json" % (p, lab))
    with open(sp, "w") as f:
        json.dump({"prime": p, "fiber": lab, "bands": summary,
                   "seconds": round(time.time() - t0)}, f, indent=1)
    print("DONE %.0fs -> %s" % (time.time() - t0, sp), flush=True)


def _reduce_cell_mp(task):
    # worker-side: G filled by _init but cls must be recomputed
    if "cls" not in G:
        G["cls"] = classify(G["vars"])
    return reduce_cell(task)


if __name__ == "__main__":
    main()
