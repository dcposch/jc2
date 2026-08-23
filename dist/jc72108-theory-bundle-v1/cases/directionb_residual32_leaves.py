#!/usr/bin/env python3
"""SHEET6-DIRECTIONB §7.H (v2): HIERARCHICAL FIRST-NONZERO TAU-ORBIT
COVER of the nolog residual-32 decider (Sol accel2 §(b) design,
replacing the v1 broad leaves -- those paid for overlaps and the
b-leaves hard-zeroed nothing).

Design (exact; the six §7 no-log pins are SUBSTITUTED OUT everywhere,
never appended as rows -- Row_10[eta^28] = C10.6 then dies
identically):
  b1: fence tf1_38 (tau-rep of the tf38 pair);           Z = pins
  b2: tf38 pair = 0, fence tg1_38;                       Z = pins+2
  b3: tf38+tg38 pairs = 0, fence tg01_38;                Z = pins+4
  a1: all six 38s = 0, fence tf1_40;                     Z = pins+6
  a2: 38s + tf40 pair = 0, fence tg1_40;                 Z = pins+8
  a3: 38s + tf40+tg40 pairs = 0, fence tg01_40;          Z = pins+10
  a0: all twelve even lows = 0, no fence.                Z = pins+12
Up to the certified tau-involution (phase `levers`), the seven
chamber classes C_i = leaf_i U tau(leaf_i) PARTITION the support
lattice of the twelve even lows: C_i are pairwise disjoint
(first-nonzero hierarchy) and exhaust it -- machine-checked in
phase `cover` (each of the 4096 patterns lands in EXACTLY ONE
class, and satisfies that leaf's constraints directly or after tau).

Sizes are verified against Sol's predicted table (window rows /
expanded window terms / header vars incl. fence); ANY deviation is
a wrong-object alarm and blocks shipping.  Emission at p105337
(ship + launch) and p200257 (bank only, verdict-confirmation wave).

Phases: levers | emit | guards | cover | all
"""
import os, sys, time, pickle, random
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r1_experiment as R1
import r1_fullcore as FC
import directionb_window as W
import directionb_residual32_emit as E32

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "directionb_residual32_nolog_leaf"
PRIMES = (105337, 200257)          # launch first; bank second
PIN42 = ("tf1_42", "tf2_42", "tg1_42", "tg2_42", "tg01_42", "tg02_42")
TF38, TG38, TG038 = ("tf1_38", "tf2_38"), ("tg1_38", "tg2_38"), \
    ("tg01_38", "tg02_38")
TF40, TG40, TG040 = ("tf1_40", "tf2_40"), ("tg1_40", "tg2_40"), \
    ("tg01_40", "tg02_40")
# leaf -> (extra zero set beyond PIN42, fence var or None)
LEAVES = {
    "b1": ((), "tf1_38"),
    "b2": (TF38, "tg1_38"),
    "b3": (TF38 + TG38, "tg01_38"),
    "a1": (TF38 + TG38 + TG038, "tf1_40"),
    "a2": (TF38 + TG38 + TG038 + TF40, "tg1_40"),
    "a3": (TF38 + TG38 + TG038 + TF40 + TG40, "tg01_40"),
    "a0": (TF38 + TG38 + TG038 + TF40 + TG40 + TG040, None),
}
ORDER = ("b1", "b2", "b3", "a1", "a2", "a3", "a0")
SOL_TABLE = {"b1": (76, 67698, 79), "b2": (76, 50229, 77),
             "b3": (76, 36042, 75), "a1": (67, 24741, 73),
             "a2": (67, 19983, 71), "a3": (67, 15737, 69),
             "a0": (48, 12079, 66)}
TAU_NAME = {"tf1": "tf2", "tf2": "tf1", "tg1": "tg2", "tg2": "tg1",
            "tg01": "tg02", "tg02": "tg01", "vf1": "vf2", "vf2": "vf1"}

OK = []
def chk(name, cond):
    OK.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name, flush=True)

def tau_var(nm):
    if "_" in nm:
        pre, lv = nm.rsplit("_", 1)
        if pre in TAU_NAME: return TAU_NAME[pre] + "_" + lv
    return nm

# ------------------------------------------------------------ levers
def tau_ring(r):
    out = {}
    for (z, e1, e2, p_, h1, q_, h2, B), c in r.items():
        out[(z, e2, e1, q_, h2, p_, h1, B)] = W.K3(c[0], -c[1])
    return out

def phase_levers():
    byk, vars_, D = W.load()
    same = True
    for k in sorted(byk):
        for n, v in byk[k].items():
            tv = {}
            for vk, r in v.items():
                nvk = tuple(sorted(
                    vars_.index(tau_var(vars_[i])) for i in vk))
                tv[nvk] = tau_ring(r)
            same &= (tv == byk[k][n])
    chk("tau-involution: tau(Row) == Row for every banked VExpr row "
        "(chamber-class merge certification; with banked 1c.1/§2c/"
        "gate covariance)", same)

# -------------------------------------------------------------- emit
def leaf_rows(byk, vars_, Z):
    Zs = set(Z)
    rows = []
    for k in sorted(byk):
        for n in sorted(byk[k]):
            v = dict(byk[k][n])
            if k == 20 and n == 0:
                v[()] = R1.radd(v.get((), R1.RZERO), R1.rC(R1.K3(42)))
            keep = {vk: r for vk, r in v.items()
                    if not (vk and any(vars_[i] in Zs for i in vk))}
            if keep:
                rows.append(("Row_%d[eta^%d]%s"
                             % (k, n, "+42" if k == 20 and n == 0
                                else ""), keep))
    return rows

def tp_rows(p):
    return ["r3^2+%d" % (p - 3), "A1^3+%d+%d*r3" % (p - 3, p - 1),
            "A2^3+%d+1*r3" % (p - 3), "2*HW1^2+%d*W1^2" % (p - 3),
            "2*HW2^2+%d*W2^2" % (p - 3), "uW1*W1+%d" % (p - 1),
            "uW2*W2+%d" % (p - 1), "uA*A1+%d*uA*A2+%d" % (p - 1, p - 1)]

def phase_emit():
    byk, vars_, D = W.load()
    _, names, ordered, blocks, _ = E32.load_rows()
    hdr_full, _, _ = E32.FCparse("directionb_residual32.ms")
    sizes_ok = True
    for tag in ORDER:
        Zx, F = LEAVES[tag]
        Z = PIN42 + Zx
        rows = leaf_rows(byk, vars_, Z)
        nterms = 0
        bodies = {p: [] for p in PRIMES}
        for lab, v in rows:
            terms = R1.poly_terms(v, names)
            nterms += len(terms)
            sc = E32.row_scale_terms(terms)
            for p in PRIMES:
                s = E32.emit_modp(terms, sc, p)
                assert s.count("+") + 1 == len(terms), \
                    "coefficient divisible by %d in %s" % (p, lab)
                bodies[p].append(s)
        drop = {names[i] for i in names if vars_[i] in Z}
        hdr = [h for h in hdr_full if h not in drop]
        fences = {}
        if F:
            xv = next(names[i] for i in names if vars_[i] == F)
            hdr.append("uF0")
            for p in PRIMES:
                fences[p] = ["uF0*%s+%d" % (xv, p - 1)]
        else:
            for p in PRIMES: fences[p] = []
        got = (len(rows), nterms, len(hdr))
        want = SOL_TABLE[tag]
        sizes_ok &= (got == want)
        mark = "OK" if got == want else "DEVIATION want %r" % (want,)
        for p in PRIMES:
            path = os.path.join(HERE, "%s_%s_p%d.ms" % (BASE, tag, p))
            with open(path, "w") as f:
                f.write(", ".join(hdr) + "\n%d\n" % p)
                f.write(",\n".join(bodies[p] + tp_rows(p) + fences[p])
                        + "\n")
        with open(os.path.join(HERE, "%s_%s.rows.txt" % (BASE, tag)),
                  "w") as f:
            f.write("# leaf %s (hierarchical first-nonzero, v2): "
                    "Z=0: pins(6)+%s ; fence: %s\n"
                    % (tag, ",".join(Zx) or "-", F or "-"))
            for i, (lab, _) in enumerate(rows):
                f.write("eq%d = %s\n" % (i, lab))
            f.write("then: rad+sat block (8), %s\n"
                    % ("1 fence row" if F else "no fence"))
        print("   leaf %s: %d window rows, %d window terms, %d vars "
              "[Sol table: %s]" % (tag, got[0], got[1], got[2], mark),
              flush=True)
    chk("ALL leaf sizes match Sol's predicted table EXACTLY "
        "(wrong-object alarm gate)", sizes_ok)

# ------------------------------------------------------------ guards
def phase_guards():
    byk, vars_, D = W.load()
    _, names, ordered, blocks, _ = E32.load_rows()
    files = ["%s_%s_p%d.ms" % (BASE, t, p) for t in ORDER
             for p in PRIMES]
    for fn in files:
        txt = open(os.path.join(HERE, fn)).read()
        assert "(" not in txt and ")" not in txt, fn
    chk("guard A: paren sweep, %d leaf files (both primes)"
        % len(files), True)
    okall = True
    for tag in ORDER:
        Zx, F = LEAVES[tag]
        Z = set(PIN42 + Zx)
        rows = leaf_rows(byk, vars_, tuple(Z))
        scales = [E32.row_scale_terms(R1.poly_terms(v, names))
                  for _, v in rows]
        for p in PRIMES:
            pt = FC.radical_point(p)
            hdr, char, eqs = E32.FCparse("%s_%s_p%d.ms" % (BASE, tag, p))
            assert char == p
            for t in range(2):
                rng = random.Random(6200 + t + p + hash(tag) % 997)
                val = dict(pt, uW1=pow(pt["W1"], p - 2, p),
                           uW2=pow(pt["W2"], p - 2, p),
                           uA=pow((pt["A1"] - pt["A2"]) % p, p - 2, p))
                for i, nm in names.items():
                    val[nm] = 0 if vars_[i] in Z \
                        else rng.randrange(1, p)
                if F:
                    xv = next(names[i] for i in names
                              if vars_[i] == F)
                    val["uF0"] = pow(val[xv], p - 2, p)
                xval = {i: val[names[i]] for i in names}
                for i, (lab, v) in enumerate(rows):
                    want = 0
                    for vk, r in v.items():
                        m = 1
                        for vid in vk: m = m * xval[vid] % p
                        want = (want + m * FC.ring_modp(r, pt, p)) % p
                    want = want * FC.frmod(scales[i], p) % p
                    okall &= (E32._tiny_parse_eval(eqs[i], val, p)
                              == want)
                for e in eqs[len(rows):]:
                    okall &= (E32._tiny_parse_eval(e, val, p) == 0)
    chk("guard B: independent-parser round-trip vs internal ring "
        "eval, 7 leaves x 2 primes x 2 fence-consistent points",
        okall)
    # guard C: pattern-positive anchor where the support matches:
    # tails = 0 lies in leaf a0 ONLY (every fenced leaf excludes it)
    ds = pickle.load(open("/tmp/directionb_dsys.pkl", "rb"))
    p = PRIMES[0]; pt = FC.radical_point(p)
    Zx, F = LEAVES["a0"]
    rows = leaf_rows(byk, vars_, PIN42 + Zx)
    scales = [E32.row_scale_terms(R1.poly_terms(v, names))
              for _, v in rows]
    hdr, _, eqs = E32.FCparse("%s_a0_p%d.ms" % (BASE, p))
    rng = random.Random(9000)
    val = dict(pt, uW1=pow(pt["W1"], p - 2, p),
               uW2=pow(pt["W2"], p - 2, p),
               uA=pow((pt["A1"] - pt["A2"]) % p, p - 2, p))
    for i, nm in names.items():
        val[nm] = 0 if vars_[i][:2] in ("tf", "tg") \
            else rng.randrange(1, p)
    ok = True
    for i, (lab, v) in enumerate(rows):
        g = E32._tiny_parse_eval(eqs[i], val, p)
        kk, nn = lab.split("[")[0], int(lab.split("^")[1].split("]")[0])
        if kk != "Row_20" or nn not in ds["byk"][20]:
            ok &= (g == 0); continue
        want = FC.ring_modp(ds["byk"][20][nn].get((), {}), pt, p)
        if nn == 0: want = (want + 42) % p
        ok &= (g == want * FC.frmod(scales[i], p) % p)
    chk("guard C: pattern-positive anchor on leaf a0 (the only "
        "support-matching leaf): 9 zero-tail Row_20 comps == banked "
        "dsys constants (+42 at eta^0), all other rows die", ok)

# ------------------------------------------------------------- cover
def phase_cover():
    lat = TF38 + TG38 + TG038 + TF40 + TG40 + TG040
    ok, census = True, {}
    for m in range(4096):
        supp = {lat[i] for i in range(12) if (m >> i) & 1}
        hits = []
        for tag in ORDER:
            Zx, F = LEAVES[tag]
            if set(Zx) & supp: continue          # zero-pins violated
            if F is None:
                if not supp: hits.append(tag)
            elif F in supp or tau_var(F) in supp:
                hits.append(tag)
        ok &= (len(hits) == 1)
        if hits: census[hits[0]] = census.get(hits[0], 0) + 1
    chk("COVER = PARTITION: each of the 4096 support patterns of the "
        "twelve even lows satisfies EXACTLY ONE chamber class "
        "C_i = leaf_i U tau(leaf_i) (first-nonzero hierarchy); "
        "unsplit vars unconstrained => the 7 classes partition the "
        "full nolog variety", ok)
    print("   chamber census: %s" % {t: census.get(t, 0)
                                     for t in ORDER})

if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "all"
    t0 = time.time()
    if ph in ("levers", "all"): phase_levers()
    if ph in ("emit", "all"): phase_emit()
    if ph in ("guards", "all"): phase_guards()
    if ph in ("cover", "all"): phase_cover()
    bad = [n for n, c in OK if not c]
    print("\nTOTAL: %d checks, %d FAIL %s  (%.1fs)"
          % (len(OK), len(bad), bad or "", time.time() - t0))
