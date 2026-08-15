#!/usr/bin/env python3
"""SHEET6-DIRECTIONB §6.V/§7.G: LOW-SUPPORT CASE SPLIT of the nolog
residual-32 decider (screen acceleration; DC-authorized).

Rationale: §6.V(3) proved every closed-form stratum INCONSISTENT
instantly -- F4 difficulty concentrates in the all-lows-nonzero
chamber.  SPLIT LATTICE: the 12 EVEN low tails (levels 38/40; six
per level).  The odd lows 39/41 are NOT split: they enter the bands
only w-weighted (C12/C14) and carry no unit-kill lever; splitting
them multiplies leaves without isolating difficulty.  [This is the
documented reading of the task's "level-38..41 low block, ~8-10
vars": the actionable split sub-block is the 12 even lows.]

LEAVES (a COVER of the nolog variety -- overlaps allowed; zero-pins
are hard-substituted, fences are Rabinowitsch rows; tau-conjugate
chambers merged, certified by the banked tau-covariance (1c.1, §2c,
gate) + the exact involution check in phase `levers`):
  leaf_a0: all 38s = 0, all 40s = 0
  leaf_a1/a2/a3: all 38s = 0; tf1_40 / tg1_40 / tg01_40 != 0
  leaf_b1/b2/b3: tf1_38 / tg1_38 / tg01_38 != 0
PRE-DEAD (cited, no emission; machine-checked in `levers`):
  - singleton-38 chambers (6): C6.1 (§6.T) is one E-row on the six
    38s with ALL-UNIT coefficients on every h-sign branch, no
    7/w-dependence => exactly one nonzero 38 contradicts its fence.
  - singleton-40-within-38-silent chambers (6): the C8 block
    restricted to {38s = 0} is pure-linear in the 40s; every 40-var
    carries a unit coefficient in some restricted row, every branch.
  - {all lows = 0} sits inside leaf_a0 (also §6.V(3) "levels >= 43",
    sampled-7 scope) -- listed for knowledge, not load-bearing.
COVER IDENTITY (machine-checked, phase `cover`): every one of the
2^12 support patterns of the split lattice lies in >= 1 leaf or a
tau-image of one; patterns of the unsplit vars are unconstrained by
every leaf, so the union over the full variety follows.

Emission: p105337 lane only (the plain/nolog portfolio covers the
rest), full AUDIT discipline.  Phases:
  levers | emit | guards | cover | all      (ship = scp/launch,
  separate script /tmp/ship_leaves.sh)
"""
import os, sys, time, pickle, random
from fractions import Fraction as Fr
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r1_experiment as R1
import r1_fullcore as FC
import directionb_window as W
import directionb_residual32_emit as E32

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "directionb_residual32_nolog_leaf"
P = 105337
Z38 = ("tf1_38", "tf2_38", "tg1_38", "tg2_38", "tg01_38", "tg02_38")
Z40 = ("tf1_40", "tf2_40", "tg1_40", "tg2_40", "tg01_40", "tg02_40")
LEAVES = {
    "a0": (Z38 + Z40, ()),
    "a1": (Z38, ("tf1_40",)), "a2": (Z38, ("tg1_40",)),
    "a3": (Z38, ("tg01_40",)),
    "b1": ((), ("tf1_38",)), "b2": ((), ("tg1_38",)),
    "b3": ((), ("tg01_38",)),
}
TAU_NAME = {"tf1": "tf2", "tf2": "tf1", "tg1": "tg2", "tg2": "tg1",
            "tg01": "tg02", "tg02": "tg01", "vf1": "vf2", "vf2": "vf1",
            "uf1": "uf1", "uf2": "uf2", "uf3": "uf3"}

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
    """radkey (z,a1,a2,w1,h1,w2,h2,B) swap + K3 conjugation."""
    out = {}
    for (z, e1, e2, p_, h1, q_, h2, B), c in r.items():
        out[(z, e2, e1, q_, h2, p_, h1, B)] = W.K3(c[0], -c[1])
    return out

def phase_levers():
    byk, vars_, D = W.load()
    # (1) tau-involution maps the banked row set to itself, row-for-row
    same = True
    for k in sorted(byk):
        for n, v in byk[k].items():
            tv = {}
            for vk, r in v.items():
                nvk = tuple(sorted(
                    vars_.index(tau_var(vars_[i])) for i in vk))
                tv[nvk] = tau_ring(r)
            same &= (tv == byk[k][n])
    chk("tau-involution: tau(Row_k[eta^n]) == Row_k[eta^n] as banked "
        "VExpr, every row (merge-certification, on top of banked "
        "1c.1/§2c/gate tau-covariance)", same)
    # (2) C6.1 all-unit coefficients on all 4 branches
    bank = pickle.load(open("/tmp/directionb_window_conditions.pkl", "rb"))
    ok6 = True
    for s1, s2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        st = bank[(6, s1, s2)]
        assert st["rank"] == 1 and not st["leftover"]
        er = st["echelon"][0]
        cofs = {st["cols"][c][0]: x for c, x in er.items()}
        ok6 &= set(cofs) == set(Z38) and \
            all(W.enorm_nonzero(x) for x in cofs.values())
    chk("C6.1: the single Row_6 E-condition has ALL-UNIT coefficients "
        "on the six level-38 tails, all 4 branches => singleton-38 "
        "chambers PRE-DEAD (uniform: no 7, no w)", ok6)
    # (3) C8 block restricted to {38s = 0}: pure-linear in 40s, each
    # 40-var carries a unit coefficient in some row, all branches
    ok8 = True
    for s1, s2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        st = bank[(8, s1, s2)]
        rows = []
        for er in st["echelon"]:
            row = {}
            for c, x in er.items():
                nm, pq = st["cols"][c]
                if "*" in nm:
                    assert any(z in nm.split("*") for z in Z38)
                    continue                    # dies at 38s = 0
                row[nm] = x
            if row: rows.append(row)
        for v in Z40:
            ok8 &= any(v in row and W.enorm_nonzero(row[v])
                       for row in rows)
    chk("C8|{38s=0}: pure-linear in the six 40s; every 40-var has a "
        "unit coefficient in some restricted row, all 4 branches => "
        "singleton-40-within-38-silent chambers PRE-DEAD", ok8)

# ------------------------------------------------------------- emit
def leaf_rows(byk, vars_, Z):
    """banked window rows with Z hard-substituted to 0."""
    Zs = set(Z)
    rows = []
    for k in sorted(byk):
        for n in sorted(byk[k]):
            v = dict(byk[k][n])
            if k == 20 and n == 0:
                v[()] = R1.radd(v.get((), R1.RZERO), R1.rC(R1.K3(42)))
            keep = {vk: r for vk, r in v.items()
                    if not (vk and any(vars_[i] in Zs for i in vk))}
            lab = "Row_%d[eta^%d]%s" % (k, n,
                                        "+42" if k == 20 and n == 0 else "")
            if keep: rows.append((lab, keep))
    return rows

def phase_emit():
    byk, vars_, D = W.load()
    _, names, ordered, (high, low, seven), _ = E32.load_rows()
    hdr_full, _, eqs_nolog = E32.FCparse("directionb_residual32_nolog"
                                         "_p%d.ms" % P)
    pins = eqs_nolog[-6:]
    for tag, (Z, F) in LEAVES.items():
        Zids = {i for i, nm in names.items() if vars_[i] in Z}
        rows = leaf_rows(byk, vars_, Z)
        body, labs = [], []
        for lab, v in rows:
            terms = R1.poly_terms(v, names)
            sc = E32.row_scale_terms(terms)
            body.append(E32.emit_modp(terms, sc, P))
            labs.append(lab)
        drop = {names[i] for i in Zids}
        hdr = [h for h in hdr_full if h not in drop]
        fences = []
        for j, fv in enumerate(F):
            u = "uF%d" % j
            hdr.append(u)
            xv = next(names[i] for i, nm in names.items()
                      if vars_[i] == fv)
            fences.append("%s*%s+%d" % (u, xv, P - 1))
        tp = ["r3^2+%d" % (P - 3), "A1^3+%d+%d*r3" % (P - 3, P - 1),
              "A2^3+%d+1*r3" % (P - 3), "2*HW1^2+%d*W1^2" % (P - 3),
              "2*HW2^2+%d*W2^2" % (P - 3), "uW1*W1+%d" % (P - 1),
              "uW2*W2+%d" % (P - 1),
              "uA*A1+%d*uA*A2+%d" % (P - 1, P - 1)]
        eqs = body + tp + pins + fences
        path = os.path.join(HERE, "%s_%s_p%d.ms" % (BASE, tag, P))
        with open(path, "w") as f:
            f.write(", ".join(hdr) + "\n%d\n" % P)
            f.write(",\n".join(eqs) + "\n")
        with open(path.replace(".ms", ".rows.txt"), "w") as f:
            f.write("# leaf %s: Z=0: %s ; fences!=0: %s\n"
                    % (tag, ",".join(Z) or "-", ",".join(F) or "-"))
            for i, lab in enumerate(labs): f.write("eq%d = %s\n" % (i, lab))
            f.write("then: rad(6)+sat(3) block, 6 nolog pins, "
                    "%d fence row(s)\n" % len(F))
        print("   leaf %s: %d window rows (of 77 -- %d died under Z), "
              "%d eqs, %d vars, %.2f MB"
              % (tag, len(body), 77 - len(body), len(eqs), len(hdr),
                 os.path.getsize(path) / 1e6), flush=True)
    # ctl0-analogue for the ONLY origin-satisfiable leaf (a0)
    Z, F = LEAVES["a0"]
    rows = leaf_rows(byk, vars_, Z)
    bodyc = []
    for lab, v in rows:
        vc = {vk: r for vk, r in v.items() if vk}
        if not vc: continue
        tc = R1.poly_terms(vc, names)
        bodyc.append(E32.emit_modp(tc, E32.row_scale_terms(tc), P))
    drop = {names[i] for i, nm in names.items() if vars_[i] in Z}
    hdr = [h for h in hdr_full if h not in drop]
    tp = ["r3^2+%d" % (P - 3), "A1^3+%d+%d*r3" % (P - 3, P - 1),
          "A2^3+%d+1*r3" % (P - 3), "2*HW1^2+%d*W1^2" % (P - 3),
          "2*HW2^2+%d*W2^2" % (P - 3), "uW1*W1+%d" % (P - 1),
          "uW2*W2+%d" % (P - 1), "uA*A1+%d*uA*A2+%d" % (P - 1, P - 1)]
    path = os.path.join(HERE, "%s_a0_ctl0_p%d.ms" % (BASE, P))
    with open(path, "w") as f:
        f.write(", ".join(hdr) + "\n%d\n" % P)
        f.write(",\n".join(bodyc + tp + pins) + "\n")
    print("   leaf a0 ctl0 (satisfiability guard, origin-satisfiable):"
          " %d eqs" % (len(bodyc) + len(tp) + 6))

# ------------------------------------------------------------ guards
def phase_guards():
    byk, vars_, D = W.load()
    _, names, ordered, blocks, _ = E32.load_rows()
    files = ["%s_%s_p%d.ms" % (BASE, t, P) for t in LEAVES] + \
        ["%s_a0_ctl0_p%d.ms" % (BASE, P)]
    for fn in files:
        txt = open(os.path.join(HERE, fn)).read()
        assert "(" not in txt and ")" not in txt, fn
    chk("guard A: paren sweep, %d leaf files" % len(files), True)
    pt = FC.radical_point(P)
    okall, okanchor = True, True
    for tag, (Z, F) in LEAVES.items():
        hdr, char, eqs = E32.FCparse("%s_%s_p%d.ms" % (BASE, tag, P))
        assert char == P
        rows = leaf_rows(byk, vars_, Z)
        scales = [E32.row_scale_terms(R1.poly_terms(v, names))
                  for _, v in rows]
        for t in range(2):
            rng = random.Random(5100 + t + hash(tag) % 997)
            val = dict(pt, uW1=pow(pt["W1"], P - 2, P),
                       uW2=pow(pt["W2"], P - 2, P),
                       uA=pow((pt["A1"] - pt["A2"]) % P, P - 2, P))
            P42 = {"tf1_42", "tf2_42", "tg1_42", "tg2_42",
                   "tg01_42", "tg02_42"}          # pin-consistent point
            for i, nm in names.items():
                val[nm] = 0 if (vars_[i] in Z or vars_[i] in P42)                     else rng.randrange(1, P)
            for j, fv in enumerate(F):
                xv = next(names[i] for i, nm2 in names.items()
                          if vars_[i] == fv)
                val["uF%d" % j] = pow(val[xv], P - 2, P)
            xval = {i: val[names[i]] for i in names}
            for i, (lab, v) in enumerate(rows):
                want = 0
                for vk, r in v.items():
                    m = 1
                    for vid in vk: m = m * xval[vid] % P
                    want = (want + m * FC.ring_modp(r, pt, P)) % P
                want = want * FC.frmod(scales[i], P) % P
                okall &= (E32._tiny_parse_eval(eqs[i], val, P) == want)
            for e in eqs[len(rows):]:
                okall &= (E32._tiny_parse_eval(e, val, P) == 0)
    chk("guard B: independent-parser round-trip vs internal ring eval "
        "(hard-substituted rows + rad/sat/pins/fences), 7 leaves x "
        "2 fence-consistent points, p=%d" % P, okall)
    # guard C: pattern-positive anchor on leaf a0 (support matches:
    # tails = 0 satisfies Z-pins, the 6 nolog pins, no fences)
    ds = pickle.load(open("/tmp/directionb_dsys.pkl", "rb"))
    hdr, _, eqs = E32.FCparse("%s_a0_p%d.ms" % (BASE, P))
    Z, F = LEAVES["a0"]
    rows = leaf_rows(byk, vars_, Z)
    scales = [E32.row_scale_terms(R1.poly_terms(v, names))
              for _, v in rows]
    rng = random.Random(9000)
    val = dict(pt, uW1=pow(pt["W1"], P - 2, P),
               uW2=pow(pt["W2"], P - 2, P),
               uA=pow((pt["A1"] - pt["A2"]) % P, P - 2, P))
    for i, nm in names.items():
        val[nm] = 0 if vars_[i][:2] in ("tf", "tg") \
            else rng.randrange(1, P)
    ok = True
    for i, (lab, v) in enumerate(rows):
        g = E32._tiny_parse_eval(eqs[i], val, P)
        kk, nn = lab.split("[")[0], int(lab.split("^")[1].split("]")[0])
        if kk != "Row_20" or nn not in ds["byk"][20]:
            ok &= (g == 0); continue
        want = FC.ring_modp(ds["byk"][20][nn].get((), {}), pt, P)
        if nn == 0: want = (want + 42) % P
        ok &= (g == want * FC.frmod(scales[i], P) % P)
    chk("guard C: pattern-positive anchor on leaf a0 -- zero-tail "
        "point satisfies Z-pins + nolog pins; the 9 zero-tail Row_20 "
        "comps == banked dsys constants (+42 at eta^0)", ok)
    # guard D: a0 ctl0 satisfied at the origin
    hdr, _, eqsc = E32.FCparse("%s_a0_ctl0_p%d.ms" % (BASE, P))
    val0 = dict(val)
    for h in hdr:
        if h.startswith("x"): val0[h] = 0
    nwin = len(eqsc) - 8 - 6
    bad = [j for j in range(nwin)
           if E32._tiny_parse_eval(eqsc[j], val0, P)]
    chk("guard D: leaf-a0 ctl0 window rows vanish at the origin "
        "(satisfiability control honest; fenced leaves have no "
        "origin-tier control -- documented)", not bad)

# ------------------------------------------------------------- cover
def phase_cover():
    lat = Z38 + Z40
    tau_class = lambda v: min(v, tau_var(v))
    reps_b = {tau_class(v): "b" for v in Z38}
    covered_by = []
    ok = True
    for m in range(4096):
        supp = {lat[i] for i in range(12) if (m >> i) & 1}
        s38, s40 = supp & set(Z38), supp & set(Z40)
        hit = None
        if s38:
            v = sorted(s38)[0]; c = tau_class(v)
            hit = {"tf1_38": "b1", "tg1_38": "b2", "tg01_38": "b3"}[c]
        elif s40:
            v = sorted(s40)[0]; c = tau_class(v)
            hit = {"tf1_40": "a1", "tg1_40": "a2", "tg01_40": "a3"}[c]
        else:
            hit = "a0"
        # verify the pattern satisfies the leaf's constraints (or the
        # tau-image's): zero-pins outside supp; fences inside supp-or-tau
        Z, F = LEAVES[hit]
        okz = not (set(Z) & supp)
        okf = all(f in supp or tau_var(f) in supp for f in F)
        ok &= okz and okf
        covered_by.append(hit)
    chk("COVER IDENTITY: all 4096 support patterns of the split "
        "lattice (38/40 blocks) land in a leaf or a tau-image "
        "(zero-pins respected, fences witnessed); unsplit vars "
        "unconstrained by every leaf => union(leaves + tau-images) "
        "+ pre-dead chambers = the full nolog variety", ok)
    from collections import Counter
    print("   chamber census: %s" % dict(Counter(covered_by)))

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
