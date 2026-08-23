#!/usr/bin/env python3
"""D25PF verdict extraction: the per-fiber EMPTY/NONEMPTY/TIMEOUT table.

Reads <root>/d25pf/out/d25pf_p<P>_<label>.out plus the pilot.log rc
markers ("D25PF <label>: rc=.. size=.. secs=.. p<P>") and decides per
fiber, under the sol-round6 sect-3 discrimination logic quoted in
SHEET6-DIRECTIONB.md section 9 (36-bit mask semantics):

  EMPTY     the reduced GB is [1]  (1 in the ideal; no point over
            the algebraic closure of F_p)
  NONEMPTY  proper GB; dimension by the exact LT-staircase
            min-hitting-set (the 8.S6/8.S8 machinery): dim = nvars -
            minimum number of variables meeting every GB leading-term
            support (exact branch-and-bound, greedy-seeded, singleton
            edges forced, disjoint-matching lower bound)
  TIMEOUT   rc=124 marker or 0-byte .out (0-byte is NEVER read as a
            verdict -- R6 sect 19.2 hygiene)

The grevlex order pin (first-printed term of every element is the
unique grevlex max) is asserted on every element of every GB read.

Usage: d25pf_verdict.py <prime>   (box01; writes
       <root>/d25pf/verdicts_p<P>.json)
"""
import hashlib
import json
import os
import sys
import time


G_ROOT = os.environ.get("D25_ROOT", os.path.expanduser("~/jc72108"))


def grevlex_key(e):
    """Tuple key: a > b in grevlex iff key(a) > key(b)."""
    return (sum(e),) + tuple(-x for x in reversed(e))


def parse_gb_out(path, p):
    """-> (gvars, n_elements, [LT exponent tuples], is_empty)."""
    txt = open(path).read()
    lines = txt.split("\n")
    ch = next(l for l in lines if l.startswith("#field characteristic"))
    assert int(ch.split(":")[1]) == p, (path, ch)
    vo = next(l for l in lines if l.startswith("#variable order"))
    gvars = [v.strip() for v in vo.split(":")[1].split(",")]
    body = txt.split("#---")[-1].strip()
    assert body.startswith("[") and body.rstrip(":").rstrip() \
        .endswith("]"), (path, body[-40:])
    body = body.lstrip("[").rstrip().rstrip(":").rstrip("]")
    vi = {v: i for i, v in enumerate(gvars)}
    nv = len(gvars)
    lts = []
    polys = body.split(",\n")
    for spoly in polys:
        best = None
        first = None
        for t in spoly.strip().split("+"):
            fs = t.strip().split("*")
            try:
                int(fs[0]); fs = fs[1:]
            except ValueError:
                pass
            e = [0] * nv
            for f in fs:
                if not f:
                    continue
                if "^" in f:
                    nm, ex = f.split("^")
                    e[vi[nm]] += int(ex)
                else:
                    e[vi[f]] += 1
            k = grevlex_key(e)
            if first is None:
                first = (k, tuple(e))
            if best is None or k > best[0]:
                best = (k, tuple(e))
        assert first == best, ("order pin failed", path, spoly[:60])
        lts.append(best[1])
    if len(polys) == 1 and sum(lts[0]) == 0:
        return gvars, 1, lts, True          # GB == [1]: EMPTY
    assert all(sum(e) > 0 for e in lts), \
        ("constant element in proper-looking GB", path)
    return gvars, len(polys), lts, False


def staircase_dim(lts, nv):
    """Exact Krull dimension of the LT staircase: nv - min hitting set
    of the LT supports.  Returns (dim, one max independent var set)."""
    edges = {frozenset(i for i, x in enumerate(e) if x) for e in lts}
    minimal = []
    for e in sorted(edges, key=len):
        if not any(m <= e for m in minimal):
            minimal.append(e)
    # greedy seed (most-frequent variable first)
    def greedy(eds):
        cov = set()
        eds = list(eds)
        while eds:
            cnt = {}
            for e in eds:
                for v in e:
                    cnt[v] = cnt.get(v, 0) + 1
            v = max(sorted(cnt), key=lambda x: cnt[x])
            cov.add(v)
            eds = [e for e in eds if v not in e]
        return cov
    best = [greedy(minimal)]

    def lower_bound(eds):
        used, m = set(), 0
        for e in sorted(eds, key=len):
            if not (e & used):
                used |= e
                m += 1
        return m

    def bb(eds, chosen):
        forced = True
        while forced:
            forced = False
            for e in eds:
                if len(e) == 1:
                    (v,) = e
                    chosen = chosen | {v}
                    eds = [f for f in eds if v not in f]
                    forced = True
                    break
        if not eds:
            if len(chosen) < len(best[0]):
                best[0] = chosen
            return
        if len(chosen) + lower_bound(eds) >= len(best[0]):
            return
        e = min(eds, key=len)
        for v in sorted(e):
            bb([f for f in eds if v not in f], chosen | {v})

    bb(minimal, frozenset())
    cover = best[0]
    assert all(e & cover for e in minimal)
    indep = [i for i in range(nv) if i not in cover]
    assert not any(e <= set(indep) for e in minimal)
    return nv - len(cover), indep


def main():
    p = int(sys.argv[1])
    pfdir = os.path.join(G_ROOT, "d25pf")
    outdir = os.path.join(pfdir, "out")
    # rc markers from pilot.log
    marks = {}
    plog = os.path.join(G_ROOT, "pilot.log")
    if os.path.exists(plog):
        for line in open(plog):
            if line.startswith("D25PF ") and (" p%d" % p) in line:
                try:
                    lab = line.split()[1].rstrip(":")
                    kv = dict(t.split("=") for t in line.split()[2:]
                              if "=" in t)
                    marks[lab] = kv
                except Exception:
                    pass
    labs = sorted(fn[len("d25pf_p%d_" % p):-3]
                  for fn in os.listdir(pfdir)
                  if fn.startswith("d25pf_p%d_" % p)
                  and fn.endswith(".ms"))
    fibers = {}
    counts = {"EMPTY": 0, "NONEMPTY": 0, "TIMEOUT": 0, "PENDING": 0}
    dims = {}
    for lab in labs:
        opath = os.path.join(outdir, "d25pf_p%d_%s.out" % (p, lab))
        mk = marks.get(lab, {})
        rc = int(mk.get("rc", -1))
        rec = {"rc": rc, "secs": int(mk.get("secs", -1)),
               "size": int(mk.get("size", -1))}
        if rc == 124 or (rc >= 0 and rc != 0):
            rec["verdict"] = "TIMEOUT" if rc == 124 else "ERROR(rc=%d)" % rc
            counts["TIMEOUT"] += 1
        elif rc == 0 and os.path.exists(opath) \
                and os.path.getsize(opath) > 0:
            gvars, n, lts, empty = parse_gb_out(opath, p)
            rec["gb_n"] = n
            rec["out_md5"] = hashlib.md5(
                open(opath, "rb").read()).hexdigest()
            if empty:
                rec["verdict"] = "EMPTY"
                counts["EMPTY"] += 1
            else:
                dim, indep = staircase_dim(lts, len(gvars))
                rec["verdict"] = "NONEMPTY"
                rec["dim"] = dim
                rec["max_indep_set"] = [gvars[i] for i in indep]
                counts["NONEMPTY"] += 1
                dims[dim] = dims.get(dim, 0) + 1
        else:
            rec["verdict"] = "PENDING"
            counts["PENDING"] += 1
        fibers[lab] = rec
        print("%-7s %-10s %s" % (lab, rec["verdict"],
                                 "dim=%d gb_n=%d" % (rec["dim"],
                                                     rec["gb_n"])
                                 if rec.get("dim") is not None else ""),
              flush=True)
    out = {
        "prime": p,
        "date": time.strftime("%Y-%m-%d"),
        "object": "36 per-fiber D25 race systems d25pf_p%d_<label>.ms "
                  "= 509-el det23 GB + 5 D25 Schur residuals (514 rows "
                  "/ 28 vars); verdicts under sol-round6 sect 3 "
                  "componentwise mask semantics" % p,
        "equivalence": "componentwise verdicts of the section-9 union "
                       "system == these per-fiber verdicts (GATE-PF2 "
                       "specialization + GATE-PF3 forward inclusion + "
                       "banked 8.S8 det23 GB identity; see "
                       "d25pf/pf_manifest_p%d.json)" % p,
        "dimension_method": "exact LT-staircase min-hitting-set "
                            "(branch-and-bound, order pin asserted on "
                            "every GB element)",
        "counts": counts, "dims_histogram": dims,
        "fibers": fibers,
        "scope": "INTERNAL/UNREVIEWED; mod p, chart-local (residue-A "
                 "B-frozen no-log PIN42 W1W2!=0 chart, fixed r3 "
                 "embedding); NOT char 0",
    }
    vpath = os.path.join(pfdir, "verdicts_p%d.json" % p)
    with open(vpath + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    os.replace(vpath + ".tmp", vpath)
    print("counts:", counts, "dims:", dims)
    print("wrote", vpath)
    return 0


if __name__ == "__main__":
    sys.exit(main())
