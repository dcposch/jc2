#!/usr/bin/env python3
"""D25 per-fiber decomposition emission (the RACE HEDGE vs the union lanes).

SHEET6-DIRECTIONB.md section 9 built ONE union D25 system per prime over
the 36-component split etale selector algebra (cases/d25_assemble.py);
its variety is the exact disjoint union of the 36 fiber quotients
(GATE-F1 interpolation round trips).  This stage emits the SAME 36 fiber
quotients as 36 individual plain-F_p systems in the atlas 8.S8 pattern
(det system = fiber GB VERBATIM + the new rows), so every solve starts
from the banked depth-23 Groebner basis instead of re-grinding the D23
core -- the scale that solved in ~65 s per fiber at D23:

    d25pf_p<P>_<label>.ms = 509-el det23 GB G23(label)   [the D23 part]
                          + the 5 D25 Schur residuals of the fiber
    (514 rows / 28 vars = 22 det23 base + 6 lift aliases
     x33, x38, x16, x19, x24, x27)

EQUIVALENCE (stated precisely): per fiber,
    ideal(G23 + R_1..R_5) == ideal(26 core + 3 g + R_1..R_5)
                          == the <label>-component of the union system,
because (a) G23 is the banked atlas det23 GB of ideal(26 core + 3 g)
(8.S8 stages 1-6, both primes, md5-gated), (b) NF_G23(core + g) == 0 is
re-verified HERE per fiber (GATE-PF3), and (c) the union rows specialize
dict-exactly to the parked per-fiber rows at every fiber's selector
values (GATE-PF2, independent parser).  Hence the componentwise verdicts
of the union system equal the per-fiber verdicts.

GATES (hard asserts, per-fiber checkpointed):
  PF1  md5s of the union + parked .ms match asm_manifest_p<P>.json;
       gbcache support skeleton identical across the run's fibers.
  PF2  union rows specialized at the fiber's selector values == parked
       rows dict-exact (34 rows/fiber); the 4 selector rows vanish.
  PF3  forward inclusion NF_G23(26 core + 3 g) == 0 (the D23 content of
       the per-fiber system adds nothing to I23 = <G23>); GB rows are
       22-var pure; residuals carry only the 6 lift aliases beyond P22.
  PF4  witness truncation (a00pp): every banked d23 witness draw
       annihilates all 509 G23 rows of the emitted a00pp system -- the
       banked D23 witnesses satisfy the D25 system's D23-truncation.
  PF5  emission hygiene per AUDIT.md: paren-free, coeffs in [0,p), no
       bare-constant/zero row, independent-parser reparse dict-exact on
       all 514 rows, pairwise-distinct md5s across the emitted fibers.

Usage:  d25_perfiber.py <prime> [--workers N] [--fibers a,b] [--skip-wit]
Inputs (box01 layout; override root with env D25_ROOT):
  <root>/d25/gbcache_p<P>_<label>.pkl     parsed 509-el det23 GBs (gated
                                          at parse by d25_reduce)
  <root>/d25/d23_atlas_p<P>.json          fiber selector values
  <root>/d25/d23_witnesses_p<P>.json      banked D23 witnesses (a00pp)
  <root>/d25fam/d25fam_p<P>.ms            the union emission
  <root>/d25fam/d25fam_p<P>_<label>.ms    36 parked specializations
  <root>/d25fam/asm_manifest_p<P>.json    md5s + shape
Outputs:
  <root>/d25pf/d25pf_p<P>_<label>.ms      36 per-fiber race systems
  <root>/d25pf/ck/pf_p<P>_<label>.json    per-fiber gate checkpoints
  <root>/d25pf/pf_manifest_p<P>.json      manifest + gate record
  <root>/d25pf/pf_p<P>.log                progress log
"""
import argparse
import hashlib
import json
import os
import pickle
import socket
import sys
import time
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import d25_reduce as DR

P22 = DR.GBVARS
NV = DR.NV
pack, unpack, degof = DR.pack, DR.unpack, DR.degof
nf_trace = DR.nf_trace

OCCX = ["x33", "x38", "x16", "x19", "x24", "x27"]   # occ_lift aliases,
# sorted-tail order tg01_46, tg02_46, tg1_43, tg1_46, tg2_43, tg2_46
SELVARS = ["A1r", "A2r", "h1r", "h2r"]
HDR_F = OCCX + P22                                   # 28-var parked hdr
HDR_U = OCCX + P22 + SELVARS                         # 32-var union hdr
G_ROOT = os.environ.get("D25_ROOT", os.path.expanduser("~/jc72108"))


# ------------------------------------------------------------- parsing
def parse_ms_rows(path, p, expect_vars):
    """Generic .ms parser -> (row_dicts keyed by exp tuple, row_texts)."""
    lines = open(path).read().split("\n")
    hdr = [h.strip() for h in lines[0].split(",")]
    assert hdr == expect_vars, ("var order mismatch", path, hdr)
    assert int(lines[1]) == p, (path, lines[1])
    body = "\n".join(lines[2:])
    rows = [r.strip().rstrip(",") for r in body.split(",\n") if r.strip()]
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
            k = tuple(e)
            d[k] = (d.get(k, 0) + c) % p
        out.append({k: c for k, c in d.items() if c})
    return out, rows


def gb_row_poly(el, p):
    """gbcache element (lt_s, lt_deg, tail) -> {packed22: coeff} incl LT."""
    lt_s, lt_deg, tail = el
    d = {lt_s: 1}
    for s, _, c in tail:
        d[s] = (d.get(s, 0) + c) % p
    return {s: c for s, c in d.items() if c}


def gb_row_txt(el):
    """Render a gbcache element as an .ms row (LT first, stored tail
    order = grevlex-descending; explicit coefficients; paren-free)."""
    lt_s, lt_deg, tail = el
    terms = [mono22(lt_s, 1)]
    for s, _, c in tail:
        terms.append(mono22(s, c))
    return "+".join(terms)


def mono22(s, c):
    e = unpack(s)
    fs = ["%s^%d" % (P22[i], ex) if ex > 1 else P22[i]
          for i, ex in enumerate(e) if ex]
    if not fs:
        return "%d" % c
    return "%d*%s" % (c, "*".join(fs))


def emit_ms(path, hdr, rows_txt, p):
    with open(path + ".tmp", "w") as fh:
        fh.write(", ".join(hdr) + "\n%d\n" % p)
        fh.write(",\n".join(rows_txt) + "\n")
    os.replace(path + ".tmp", path)


# --------------------------------------------------------------- worker
G = {}


def _init(shared):
    G.update(shared)


def specialize_union(rowd, selpow, p):
    """Union row dict (32-tuple exps) -> 28-tuple dict at the fiber."""
    out = {}
    for e, c in rowd.items():
        m = c
        for j in range(4):
            ex = e[28 + j]
            if ex:
                m = m * selpow[j][ex] % p
        if not m:
            continue
        k = e[:28]
        nc = (out.get(k, 0) + m) % p
        if nc: out[k] = nc
        else: out.pop(k, None)
    return out


def fiber_task(lab):
    t0 = time.time()
    p = G["p"]
    ckp = os.path.join(G["ckdir"], "pf_p%d_%s.json" % (p, lab))
    msp = os.path.join(G["pfdir"], "d25pf_p%d_%s.ms" % (p, lab))
    if os.path.exists(ckp) and os.path.exists(msp):
        return lab, "skip", 0.0, json.load(open(ckp))["ms_md5"]
    try:
        rec = build_fiber(lab, msp)
    except AssertionError as e:
        return lab, "STOP: %r" % (e,), time.time() - t0, ""
    rec["secs"] = round(time.time() - t0, 1)
    rec["host"] = socket.gethostname()
    rec["ts"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    tmp = ckp + ".tmp.%d" % os.getpid()
    with open(tmp, "w") as fh:
        json.dump(rec, fh, indent=1, sort_keys=True)
    os.replace(tmp, ckp)
    return lab, "done", time.time() - t0, rec["ms_md5"]


def build_fiber(lab, msp):
    p = G["p"]
    fv = G["fvals"][lab]
    gates = {}

    # ---- parked file: md5 vs manifest (PF1) + parse
    fpath = os.path.join(G["famdir"], "d25fam_p%d_%s.ms" % (p, lab))
    md5 = hashlib.md5(open(fpath, "rb").read()).hexdigest()
    assert md5 == G["per_fiber_md5"][lab], \
        ("GATE-PF1 parked md5 mismatch", lab)
    parked, parked_txt = parse_ms_rows(fpath, p, HDR_F)
    assert len(parked) == 34, ("parked rows != 34", lab, len(parked))
    gates["pf1_parked_md5"] = md5

    # ---- PF2: union specialized at the fiber == parked, dict-exact
    selvals = [fv["A1"], fv["A2"], fv["HW1_over_W1"], fv["HW2_over_W2"]]
    selpow = [[pow(v, e, p) for e in range(9)] for v in selvals]
    for i in range(34):
        spec = specialize_union(G["union"][i], selpow, p)
        assert spec == parked[i], \
            ("GATE-PF2 union component != parked row", lab, i)
    for i in range(34, 38):                     # selector rows vanish
        spec = specialize_union(G["union"][i], selpow, p)
        assert spec == {}, ("GATE-PF2 selector row nonzero at fiber",
                            lab, i)
    gates["pf2_union_vs_fiber"] = "PASS 34/34 dict-exact + 4/4 selector"

    # ---- gbcache
    with open(os.path.join(G["d25dir"],
                           "gbcache_p%d_%s.pkl" % (p, lab)), "rb") as fh:
        gb = pickle.load(fh)
    assert len(gb) == 509, ("gbcache != 509 els", lab, len(gb))

    # ---- PF3: forward inclusion NF_G23(26 core + 3 g) == 0; purity
    for i in range(29):
        e6 = {e[:6] for e in parked[i]}
        assert e6 == {(0,) * 6} or not parked[i], \
            ("GATE-PF3 core/g row carries lift vars", lab, i)
        z = {}
        for e, c in parked[i].items():
            s = pack(e[6:])
            z[s] = (z.get(s, 0) + c) % p
        nf, _, _ = nf_trace({s: c for s, c in z.items() if c}, gb, p)
        assert not nf, ("GATE-PF3 core/g row not in <G23>", lab, i)
    for i in range(29, 34):                     # residual lift support
        for e in parked[i]:
            pass                                # lift exps allowed
    gates["pf3_forward_inclusion"] = "PASS 29/29 NF == 0"

    # ---- emit: 509 GB rows + the 5 residual rows VERBATIM
    gb_txt = [gb_row_txt(el) for el in gb]
    rows_txt = gb_txt + parked_txt[29:34]
    emit_ms(msp, HDR_F, rows_txt, p)

    # ---- PF5: hygiene + independent reparse
    body = open(msp).read()
    assert "(" not in body and ")" not in body, "GATE-PF5 parens"
    reparsed, _ = parse_ms_rows(msp, p, HDR_F)
    assert len(reparsed) == 514, ("GATE-PF5 row count", len(reparsed))
    for j, el in enumerate(gb):
        want = {}
        for s, c in gb_row_poly(el, p).items():
            want[(0,) * 6 + unpack(s)] = c
        assert reparsed[j] == want, ("GATE-PF5 GB row reparse", lab, j)
    for j in range(5):
        assert reparsed[509 + j] == parked[29 + j], \
            ("GATE-PF5 residual row reparse", lab, j)
    for row in rows_txt:
        assert row and row != "0", "GATE-PF5 zero row"
        allconst = all("*" not in t and t.strip().isdigit()
                       for t in row.split("+"))
        assert not allconst, "GATE-PF5 bare-constant row"
        for t in row.split("+"):
            head = t.strip().split("*")[0]
            if head.isdigit():
                assert int(head) < p, "GATE-PF5 coefficient >= p"
    gates["pf5_hygiene"] = "PASS 514 rows reparse dict-exact"

    nterm = sum(t.count("+") + 1 for t in rows_txt)
    return {"label": lab, "prime": p, "rows": 514, "vars": 28,
            "terms": nterm, "gates": gates,
            "ms_md5": hashlib.md5(open(msp, "rb").read()).hexdigest()}


# ------------------------------------------------- witness truncation
def witness_gate(p, log):
    """PF4: banked a00pp D23 witnesses annihilate the emitted a00pp
    system's D23 part (all 509 G23 rows) -- the D25 system's
    D23-truncation is satisfied by every banked witness draw."""
    with open(os.path.join(G_ROOT, "d25",
                           "gbcache_p%d_a00pp.pkl" % p), "rb") as fh:
        gb = pickle.load(fh)
    W = json.load(open(os.path.join(G_ROOT, "d25",
                                    "d23_witnesses_p%d.json" % p)))
    assert W["prime"] == p
    # pre-expand rows once: (coeff, ((vi, ex), ...))
    rows = []
    for el in gb:
        terms = []
        for s, c in gb_row_poly(el, p).items():
            e = unpack(s)
            terms.append((c, tuple((i, ex) for i, ex in enumerate(e)
                                   if ex)))
        rows.append(terms)
    npts = nrows = 0
    for wit in W["witnesses"]:
        for draw in wit["draws"]:
            val = draw["witness72"]
            vv = [val[nm] % p for nm in P22]
            pw = [None] * NV
            for j, terms in enumerate(rows):
                tot = 0
                for c, mono in terms:
                    m = c
                    for i, ex in mono:
                        if pw[i] is None:
                            pw[i] = [1, vv[i]]
                        t = pw[i]
                        while len(t) <= ex:
                            t.append(t[-1] * vv[i] % p)
                        m = m * t[ex] % p
                    tot = (tot + m) % p
                assert tot == 0, \
                    ("GATE-PF4 witness fails G23 row of the emitted "
                     "a00pp D25 system", wit["index"], draw["draw"], j)
                nrows += 1
            npts += 1
    log("PF4 witness truncation PASS: %d G23-row evaluations == 0 "
        "over %d banked witness draws (a00pp)" % (nrows, npts))
    return {"points": npts, "row_evals": nrows, "status": "PASS"}


# ----------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prime", type=int)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--fibers", default="")
    ap.add_argument("--skip-wit", action="store_true")
    a = ap.parse_args()
    p = a.prime
    root = G_ROOT
    d25dir = os.path.join(root, "d25")
    famdir = os.path.join(root, "d25fam")
    pfdir = os.path.join(root, "d25pf")
    ckdir = os.path.join(pfdir, "ck")
    os.makedirs(ckdir, exist_ok=True)
    logp = os.path.join(pfdir, "pf_p%d.log" % p)
    t0 = time.time()

    def log(m):
        line = "%s p%d %s" % (time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                            time.gmtime()), p, m)
        print(line, flush=True)
        with open(logp, "a") as fh:
            fh.write(line + "\n")

    with open(os.path.join(pfdir, "d25pf_p%d.pid" % p), "w") as fh:
        fh.write("%d\n" % os.getpid())
    log("PERFIBER start host=%s pid=%d" % (socket.gethostname(),
                                           os.getpid()))

    manifest_asm = json.load(open(os.path.join(
        famdir, "asm_manifest_p%d.json" % p)))
    upath = os.path.join(famdir, "d25fam_p%d.ms" % p)
    umd5 = hashlib.md5(open(upath, "rb").read()).hexdigest()
    assert umd5 == manifest_asm["union_ms"]["md5"], "GATE-PF1 union md5"
    union, _ = parse_ms_rows(upath, p, HDR_U)
    assert len(union) == 38, ("union rows != 38", len(union))
    assert manifest_asm["shape"]["lift_alias"] and \
        [manifest_asm["shape"]["lift_alias"][nm]
         for nm in manifest_asm["shape"]["occ_lift"]] == OCCX, \
        "GATE-PF1 lift alias order"
    log("PF1 union md5 %s MATCH manifest; 38 rows parsed" % umd5)

    atlas = json.load(open(os.path.join(d25dir,
                                        "d23_atlas_p%d.json" % p)))
    assert atlas["meta"]["prime"] == p
    labels = sorted(atlas["fibers"])
    assert len(labels) == 36
    fvals = {l: atlas["fibers"][l]["fiber"] for l in labels}
    todo = labels if not a.fibers else [l for l in labels
                                        if l in a.fibers.split(",")]

    shared = dict(p=p, fvals=fvals, union=union, famdir=famdir,
                  d25dir=d25dir, pfdir=pfdir, ckdir=ckdir,
                  per_fiber_md5=manifest_asm["per_fiber_md5"])
    G.update(shared)

    halted = False
    md5s = {}
    if a.workers > 1 and len(todo) > 1:
        with Pool(min(a.workers, len(todo)), _init, (shared,)) as pool:
            for lab, st, dt, m5 in pool.imap_unordered(fiber_task, todo):
                log("  fiber %-6s %-4s %.1fs %s" % (lab, st, dt, m5))
                if st.startswith("STOP"):
                    halted = True
                md5s[lab] = m5
    else:
        for lab in todo:
            lab, st, dt, m5 = fiber_task(lab)
            log("  fiber %-6s %-4s %.1fs %s" % (lab, st, dt, m5))
            if st.startswith("STOP"):
                halted = True
            md5s[lab] = m5
    if halted:
        log("HALT: gate failure -- see STOP lines above")
        return 2

    # cross-fiber: gbcache support skeleton identical (full runs)
    if len(todo) == 36:
        skel = None
        for l in todo:
            with open(os.path.join(d25dir, "gbcache_p%d_%s.pkl"
                                   % (p, l)), "rb") as fh:
                gbl = pickle.load(fh)
            sk = [(lt, tuple(s for s, _, _ in tail))
                  for lt, _, tail in gbl]
            if skel is None:
                skel = sk
            assert sk == skel, ("GATE-PF1 gbcache skeleton", l)
        log("PF1 gbcache support skeleton identical x36")
        assert len(set(md5s.values())) == 36, \
            "GATE-PF5 emissions not pairwise distinct"
        log("PF5 36 pairwise-distinct emission md5s")

    wit = None
    if not a.skip_wit and "a00pp" in todo:
        wit = witness_gate(p, log)

    recs = {l: json.load(open(os.path.join(
        ckdir, "pf_p%d_%s.json" % (p, l)))) for l in todo}
    manifest = {
        "prime": p, "date": time.strftime("%Y-%m-%d"),
        "construction": "per-fiber race decomposition of the section-9 "
                        "union D25 family: d25pf_p<P>_<label>.ms = 509-el "
                        "det23 GB (gbcache, = banked atlas det GB) + the "
                        "5 D25 Schur residuals of the parked "
                        "d25fam_p<P>_<label>.ms, 514 rows / 28 vars",
        "equivalence": "ideal(G23 + R1..R5) == ideal(26 core + 3 g + "
                       "R1..R5) == the label-component of the union "
                       "system: (a) G23 = banked atlas det23 GB of "
                       "<core+g> (8.S8); (b) GATE-PF3 NF_G23(core+g)==0 "
                       "re-verified per fiber; (c) GATE-PF2 union rows "
                       "specialize dict-exactly to the parked rows at "
                       "every fiber. Componentwise union verdicts == "
                       "per-fiber verdicts.",
        "union_md5": umd5,
        "witness_truncation": wit,
        "fibers": recs,
        "scope": "INTERNAL/UNREVIEWED; mod p, chart-local (residue-A "
                 "B-frozen no-log PIN42 W1W2!=0 chart, fixed r3 "
                 "embedding)",
    }
    with open(os.path.join(pfdir, "pf_manifest_p%d.json" % p),
              "w") as fh:
        json.dump(manifest, fh, indent=1, sort_keys=True)
    log("DONE fibers=%d wall=%.0fs" % (len(todo), time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
