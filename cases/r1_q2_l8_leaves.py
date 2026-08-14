"""r1_q2_l8_leaves.py -- leaf decomposition of the Q2-l8 stratum
(SHEET6-R1.md sec 19.5; ADDITIVE, parent emissions untouched).

The l8 monolith is structurally GB-dead (1200 s / 12-15 GB locally,
~1.65 TB / 11 h on the 2 TB Box02).  Per the sec-13 precedent the
stratum is split by the FIRST-NONZERO pattern of the 13 free core
directions opened between l13 (PROOF-TIER dead) and l8 (slots 8..12;
bf_24 excluded: KEEPX kept back-map variable, not stratum-gated):

  order (census-fixed: ascending slot, then descending occurrence):
    d_1..d_13 = bf_20, bg42_20, bg21_20, bf_21, bg42_21, bf_22,
                bg42_22, bg21_22, bf_23, bg42_23, uf24, bg42_24,
                bg21_24
  leaf k: d_1..d_{k-1} = 0 (term-drop in every row incl. the
    bf_18/24/30 defining rows), d_k != 0 (Rabinowitsch u<d_k>*d_k-1),
    rest open.  Zero leaf (all 13 = 0) == the banked l13 object
    EXACTLY (dict-identity verified at both primes) -- no run needed.

COVER: V(l8) = V(l13) u U_k pi(V(leaf_k)), disjoint (boolean
tautology on the 13-tuple).  All leaves EMPTY <=> l8 stratum EMPTY;
leaf witnesses lift by forgetting u<d_k>.

Emissions (cases/): r1_q2_l8_leaf{k}_p{105337,105673}.ms (main, 20
eqs) + r1_q2_l8_leaf{k}_ctlB_p*.ms (E5/E6 dropped, saturations kept).
E6 literal 2^24 reduced into [0,p) per the AUDIT standing rule (the
parent carries it unreduced -- flagged obligation there); guard B'
pins value-preservation against the parent artifact bytes.

AUDIT: expanded integer monomials, no parens, coefficients in [0,p).
HARD RULE (ops/FLEET.md): no local msolve -- this engine only emits,
guards, and packs; solving happens on the fleet.

Phases: census | emit | guard | cover | pack | all
"""
import os
import re
import sys
import time
import random
import pickle

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import r1_fullcore as FC
import r1_minimal_ext as ME
import r1_q2_screen as Q2
import r1_q0_gate as Q0

SYS = FC.OUT_DIR                      # systems/r1 (parent artifacts)
CASES = HERE                          # leaf emissions live in cases/
PRIMES = (105337, 105673)
KEEPX = Q2.KEEPX
W0 = Q2.W0
BASE = "r1_q2_l8_leaf"


def log(msg):
    print("[l8leaves %s] %s" % (time.strftime("%H:%M:%S"), msg),
          flush=True)


def load_build(p):
    with open("/tmp/r1q2/build_p%d_l8.pkl" % p, "rb") as f:
        return pickle.load(f)


# ------------------------------------------------- pivot order (census)
def opened_dirs(meta):
    """the 13 stratum-gated directions opened at l8 vs l13:
    core vids at slot in [8,13), KEEPX excluded."""
    names54, vm54 = ME.core_name_map()
    lv54 = {int(xn[1:]): vm54[vid]["level"]
            for vid, xn in names54.items()}
    keep = {meta["vmap"][v] for v in KEEPX}
    out = {}
    for v, vid in meta["vmap"].items():
        sl = lv54[v] - 12
        if 8 <= sl < 13 and vid not in keep:
            out[vid] = (meta["vm84"][vid]["name"], sl)
    assert len(out) == 13, len(out)
    return out


def pivot_order(rows, meta):
    """ascending slot, then descending quotient-row occurrence, then
    name (deterministic; census banked in sec 19.5)."""
    op = opened_dirs(meta)
    occ = {vid: 0 for vid in op}
    for v in rows.values():
        for (w, vk) in v:
            for x in set(vk):
                if x in op:
                    occ[x] += 1
    order = sorted(op, key=lambda t: (op[t][1], -occ[t], op[t][0]))
    return order, op, occ


def phase_census():
    for p in PRIMES:
        st = load_build(p)
        rows, meta = st["rows"], st["meta"]
        order, op, occ = pivot_order(rows, meta)
        tot = sum(len(v) for v in rows.values())
        log("p=%d: monolith %d terms; pivot order %s"
            % (p, tot, [op[v][0] for v in order]))
        for k in range(len(order) + 1):
            z = set(order[:k])
            qm = sum(1 for v in rows.values() for (w, vk) in v
                     if not (set(vk) & z))
            dm = sum(1 for d in meta["defs"].values() for (w, vk) in d
                     if not (set(vk) & z))
            tag = op[order[k]][0] if k < len(order) else "ALL-ZERO(l13)"
            log("  leaf%-3d pivot %-9s prefix %2d  quot %5d  def %d"
                % (k + 1, tag, k, qm, dm))


# ----------------------------------------------------------- emission
def zfilter(v, zset):
    return {kk: c for kk, c in v.items() if not (set(kk[1]) & zset)}


def leaf_eqs(p, st, k, order, op):
    """(labels, eqs, hdr, info) for leaf k (1-based) at prime p.
    Mirrors Q2.phase_emit row-for-row (243-corrected E5; E6 literal
    reduced into [0,p) -- the one deliberate byte-divergence from the
    parent, value-pinned by guard B'), then term-drops the zeroed
    prefix and adjoins the pivot Rabinowitsch row."""
    rows, meta = st["rows"], st["meta"]
    vm84 = meta["vm84"]
    zset = set(order[:k - 1])
    piv = order[k - 1]
    pnm = op[piv][0]
    pt = FC.radical_point(p)
    r3 = pt["r3"]
    cn = Q0.pattern_cn(p, r3)
    frows = {n: zfilter(v, zset) for n, v in rows.items()}
    fdefs = {v: zfilter(d, zset) for v, d in meta["defs"].items()}
    occ = sorted({vid for v in frows.values() for (w, vk) in v
                  for vid in vk} |
                 {vid for d in fdefs.values() for (w, vk) in d
                  for vid in vk} |
                 {meta["vmap"][v] for v in KEEPX} | {piv})
    assert not (set(occ) & zset)
    hdr = (["W1", "HW1", "W2", "HW2", "uW1", "uW2"] +
           [Q2.emit_name(v, vm84) for v in occ] +
           ["s1F", "HM", "tSAT", "u" + pnm])
    labels, eqs = [], []

    def add(lab, eq):
        labels.append(lab)
        eqs.append(eq)
    add("quadric 2HW1^2-3W1^2", "2*HW1^2+%d*W1^2" % (p - 3))
    add("quadric 2HW2^2-3W2^2", "2*HW2^2+%d*W2^2" % (p - 3))
    add("chart uW1*W1-1", "uW1*W1+%d" % (p - 1))
    add("chart uW2*W2-1", "uW2*W2+%d" % (p - 1))
    c1 = (9 + 5 * r3) % p * pt["A1"] % p
    c2 = (9 - 5 * r3) % p * pt["A2"] % p
    add("relation E (13.1 core residual on the UU chart)",
        "%d*W1^4+%d*W2^4" % (c1, c2))
    for v in KEEPX:
        nm = meta["corexn"][v]
        neg = {kk: (p - c) % p for kk, c in fdefs[v].items()}
        add("defining row %s (kept back-map value, leaf-restricted)"
            % nm,
            Q2.emit_vex({(W0, (meta["vmap"][v],)): 1}, p, vm84) +
            ("+" + Q2.emit_vex(neg, p, vm84) if neg else ""))
    for n in sorted(frows):
        extra = []
        if n in cn:
            extra.append("%d*s1F" % ((p - cn[n]) % p))
        assert frows[n] or extra, ("row vanished dry", n)
        add("Q2-quot n=%d s=60 (WF - s1F*c_n, leaf-restricted)" % n,
            Q2.emit_vex(frows[n], p, vm84, extra))
    SM = 7 ** 12 * pow(2 ** 6, p - 2, p) % p
    for i, (ai, Ai, Wn) in enumerate(
            (((3 + r3) % p, pt["A1"], "W1"),
             ((3 - r3) % p, pt["A2"], "W2")), 1):
        cH = 4 * (ai - 4) % p
        # 243 = 3^5: TEMPLATE 2c-E5 erratum 2026-08-12 (was 729)
        cQ = 243 * pow(SM, 3, p) % p * 144 % p * (ai * ai % p) % p \
            * Ai % p
        add("E5-quartic pole %d (HM restored, W symbolic)" % i,
            "%d*%s^4+%d*HM" % (cQ, Wn, cH))
    add("E6-tie cube form 2^24 HM^3 = 7^48 s1F^3 ([0,p)-reduced)",
        "%d*HM^3+%d*s1F^3" % (2 ** 24 % p, p - pow(7, 48, p)))
    add("SAT s1F (Rabinowitsch)", "s1F*tSAT+%d" % (p - 1))
    add("SAT pivot %s != 0 (Rabinowitsch, leaf chart)" % pnm,
        "u%s*%s+%d" % (pnm, pnm, p - 1))
    info = dict(zset=zset, piv=piv, pnm=pnm, occ=occ,
                frows=frows, fdefs=fdefs)
    return labels, eqs, hdr, info


def write_ms(path, hdr, eqs, p):
    with open(path, "w") as f:
        f.write(", ".join(hdr) + "\n%d\n" % p)
        f.write(",\n".join(eqs) + "\n")


def phase_emit():
    order = None
    for p in PRIMES:
        st = load_build(p)
        rows, meta = st["rows"], st["meta"]
        o, op, occ = pivot_order(rows, meta)
        assert order is None or order == o, "order drift between primes"
        order = o
        for k in range(1, 14):
            labels, eqs, hdr, info = leaf_eqs(p, st, k, order, op)
            fn = "%s%d_p%d" % (BASE, k, p)
            write_ms(os.path.join(CASES, fn + ".ms"), hdr, eqs, p)
            # ctlB: drop the E5 x2 + E6 rows, keep both saturations
            keep = [i for i, lab in enumerate(labels)
                    if not (lab.startswith("E5") or
                            lab.startswith("E6"))]
            hh = [h for h in hdr if h != "HM"]
            write_ms(os.path.join(CASES, fn.replace(
                "_p%d" % p, "_ctlB_p%d" % p) + ".ms"),
                hh, [eqs[i] for i in keep], p)
            with open(os.path.join(CASES, fn + ".rows.txt"), "w") as f:
                f.write(
                    "# Q2-l8 leaf %d/13 (SHEET6-R1.md 19.5): parent = "
                    "systems/r1/r1_q2_l8_p%d.ms (243-corrected)\n"
                    "# first-nonzero cascade, order %s\n"
                    "# ZEROED prefix (%d): %s\n"
                    "# PIVOT (!= 0, Rabinowitsch u%s): %s (slot %d)\n"
                    "# rows = the 19 parent rows with zeroed-prefix "
                    "terms dropped (defining rows restricted the same "
                    "way) + the pivot saturation; E6 literal reduced "
                    "into [0,p) (AUDIT standing rule).\n"
                    % (k, p, [op[v][0] for v in order], k - 1,
                       [op[v][0] for v in order[:k - 1]] or "-",
                       info["pnm"], info["pnm"], op[info["piv"]][1]))
                for i, lab in enumerate(labels):
                    f.write("eq%d = %s\n" % (i, lab))
            log("emitted leaf%d p=%d: %d eqs, %d vars, %.1f kB "
                "(+ctlB)" % (k, p, len(eqs), len(hdr),
                             os.path.getsize(
                                 os.path.join(CASES, fn + ".ms")) / 1e3))


# ------------------------------------------------------------- guards
def eval_vex_modp(v, wv, xv, p):
    tot = 0
    for (w, vk), c in v.items():
        m = c
        for nm, e in zip(("W1", "HW1", "W2", "HW2"), w):
            b = wv[nm] if e >= 0 else pow(wv[nm], p - 2, p)
            m = m * pow(b, abs(e), p) % p
        for vid in vk:
            m = m * xv[vid] % p
        tot = (tot + m) % p
    return tot


def rand_point(p, hdr, seed, zero=()):
    rng = random.Random(seed)
    val = {nm: rng.randrange(1, p) for nm in hdr}
    # respect the two quadrics + chart inverses so structural rows
    # can vanish when they should: not needed for value-identity
    # guards (both sides get the SAME point), keep fully generic.
    for nm in zero:
        val[nm] = 0
    for nm in list(val):
        if nm.startswith("uW"):
            val[nm] = pow(val["W" + nm[2:]], p - 2, p)
        elif nm.startswith("u") and nm[1:] in val:
            val[nm] = pow(val[nm[1:]], p - 2, p)
    return val


def phase_guard():
    ok = 0
    for p in PRIMES:
        st = load_build(p)
        rows, meta = st["rows"], st["meta"]
        vm84 = meta["vm84"]
        order, op, occ = pivot_order(rows, meta)
        names = {vid: Q2.emit_name(vid, vm84) for vid in
                 {x for v in rows.values() for (w, vk) in v for x in vk}
                 | {x for d in meta["defs"].values()
                    for (w, vk) in d for x in vk}
                 | set(order) | {meta["vmap"][v] for v in KEEPX}}
        # parent artifact rows (the banked bytes)
        ptxt = open(os.path.join(
            SYS, "r1_q2_l8_p%d.ms" % p)).read()
        phdr = ptxt.split("\n", 1)[0].split(", ")
        peqs = ptxt.split("\n", 2)[2].strip().rstrip(",").split(",\n")
        assert len(peqs) == 19
        for k in range(1, 14):
            labels, eqs, hdr, info = leaf_eqs(p, st, k, order, op)
            fn = "%s%d_p%d" % (BASE, k, p)
            mtxt = open(os.path.join(CASES, fn + ".ms")).read()
            ctxt = open(os.path.join(
                CASES, "%s%d_ctlB_p%d.ms" % (BASE, k, p))).read()
            # guard A: paren sweep + every integer token < p
            for txt, tag in ((mtxt, "main"), (ctxt, "ctlB")):
                assert "(" not in txt and ")" not in txt, (k, p, tag)
                body = txt.split("\n", 2)[2]
                toks = [int(t) for t in
                        re.findall(r"(?<!\^)\b\d+\b", body)]
                assert max(toks) < p, (k, p, tag, max(toks))
            # emitted == constructed
            assert mtxt.split("\n", 2)[2].strip().rstrip(",") \
                .split(",\n") == eqs, (k, p)
            zero_nms = [op[v][0] for v in order[:k - 1]]
            for t in range(2):
                val = rand_point(p, set(hdr) | set(phdr),
                                 8800 + p * 10 + k * 100 + t,
                                 zero=zero_nms)
                got = FC.parse_eval(eqs, val, p)
                # guard B: independent parser == internal evaluation
                wv = {nm: val[nm] for nm in ("W1", "HW1", "W2", "HW2")}
                xv = {vid: val[nm] for vid, nm in names.items()}
                for j, lab in enumerate(labels):
                    if lab.startswith("Q2-quot"):
                        n = int(lab.split("n=")[1].split(" ")[0])
                        want = eval_vex_modp(info["frows"][n], wv, xv, p)
                        cn = Q0.pattern_cn(p, FC.radical_point(p)["r3"])
                        if n in cn:
                            want = (want - cn[n] * val["s1F"]) % p
                        assert got[j] == want, ("B", k, p, lab)
                    elif lab.startswith("defining"):
                        nm = lab.split()[2]
                        v = [x for x in KEEPX
                             if meta["corexn"][x] == nm][0]
                        want = (xv[meta["vmap"][v]] - eval_vex_modp(
                            info["fdefs"][v], wv, xv, p)) % p
                        assert got[j] == want, ("Bdef", k, p, nm)
                # guard B': leaf rows == parent artifact rows at the
                # SAME point with the zeroed prefix imposed (E6 row
                # value-equal despite the [0,p) reduction)
                pgot = FC.parse_eval(peqs, val, p)
                assert got[:19] == pgot, ("Bparent", k, p)
                # guard D: no emitted row identically zero (generic pt)
                if t == 0:
                    dead = [j for j, g in enumerate(got)
                            if g == 0 and labels[j].startswith("Q2")]
                    assert not dead, ("D", k, p, dead)
            # guard C: satisfiability smoke -- constant-bearing rows
            # are exactly the four saturations; no bare-constant row
            consts = [lab for lab, eq in zip(labels, eqs)
                      if re.search(r"(?:^|\+)\d+$", eq)]
            assert sorted(consts) == sorted(
                ["chart uW1*W1-1", "chart uW2*W2-1",
                 "SAT s1F (Rabinowitsch)",
                 "SAT pivot %s != 0 (Rabinowitsch, leaf chart)"
                 % info["pnm"]]), (k, p, consts)
            assert not [e for e in eqs if e.isdigit()], (k, p)
            ok += 1
        log("guards A/B/B'/C/D PASS p=%d: 13 leaves x (paren+[0,p), "
            "round-trip, parent-identity, smoke, residual)" % p)
    log("guard total: %d leaf/prime combos PASS" % ok)


def phase_cover():
    p = PRIMES[0]
    st = load_build(p)
    rows, meta = st["rows"], st["meta"]
    order, op, occ = pivot_order(rows, meta)
    rng = random.Random(1955)
    for _ in range(500):
        tup = [rng.choice([0, 0, rng.randrange(p)]) for _ in order]
        pats = sum(1 for k in range(14)
                   if (all(x == 0 for x in tup) if k == 13 else
                       (all(x == 0 for x in tup[:k]) and tup[k] != 0)))
        assert pats == 1
    log("cover (i): 500 random 13-tuples each match EXACTLY ONE "
        "pattern (l13 or unique first-nonzero leaf) PASS")
    for p in PRIMES:
        st = load_build(p)
        with open("/tmp/r1q2/build_p%d_l13.pkl" % p, "rb") as f:
            st13 = pickle.load(f)
        z = set(order)
        zr = {n: zfilter(v, z) for n, v in st["rows"].items()}
        zd = {v: zfilter(d, z) for v, d in st["meta"]["defs"].items()}
        assert zr == st13["rows"] and zd == st13["meta"]["defs"]
        log("cover (ii) p=%d: l8 rows+defs with ALL 13 dirs zeroed == "
            "banked l13 build DICT-EXACT (zero leaf = the PROOF-TIER "
            "dead l13 object)" % p)
    log("cover (iii): unit side lifts uniquely (u = d_k^-1, field); "
        "zero side is closed-pattern restriction on free polynomial "
        "coordinates; leaf rows are the stratum rows verbatim under "
        "the pattern (guard B') -- no elimination bank, nothing to "
        "back-map beyond forgetting u<d_k>.")


if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "census"
    if ph in ("census", "all"):
        phase_census()
    if ph in ("emit", "all"):
        phase_emit()
    if ph in ("guard", "all"):
        phase_guard()
    if ph in ("cover", "all"):
        phase_cover()
