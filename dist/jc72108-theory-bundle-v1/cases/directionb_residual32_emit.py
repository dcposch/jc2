#!/usr/bin/env python3
"""SHEET6-DIRECTIONB §6.V: msolve emission of the residual window
system (the "residual-32" decider) for the Groebner tier.

Object: the FULL forced-nonzero-tail window system of the D = 21
build (/tmp/directionb_tails_D21.pkl) -- all 77 window rows (bands
6..18 + Row_20 with the inhomogeneous +42), over the radical tower,
with Rabinowitsch saturation for every template-forced-nonzero scale
that exists as a datum of this chart (w_1, w_2, a_1 - a_2).  The 50
high tails (levels >= 43) enter ONLY LINEARLY and head the variable
order: `msolve -e 53` (50 highs + the 3 Rabinowitsch inverses)
projects onto the ~28 low parameters + the 7 + the radical tower --
that projection IS the 32-condition obstruction system of §6.V(4);
its closed form is not emitted directly because the generic-rank-16
elimination transform is rational in the low data (Groebner-tier by
nature).  Satisfiability screens (-g 2) need no elimination:
GB = [1] on the MAIN system <=> the forced-tail variety is EMPTY
(residue-A dies on the window); the ctl0 variant (all constant
blocks dropped) is satisfied by the origin and must be NONEMPTY --
a [1] there is a transcription error (ctlA convention, HALT).

Notes on scales NOT saturated here: c_f c_g is consumed upstream at
the (J)-derivation tier (gauge c_f = c_g = 1 banked, §6 trust (e);
nonzeroness used unconditionally to write the RHS -42) -- it is not
a variable of this chart, exactly like z and B do not occur in the
window rows (asserted).  h_i != 0 follows from 2 HW_i^2 = 3 W_i^2
and the uW_i rows.

Files (cases/):
  directionb_residual32.ms                char 0, MAIN
  directionb_residual32_p<P>.ms           3 banked primes, MAIN
  directionb_residual32_ctl0.ms           char 0, satisfiability guard
  directionb_residual32_ctl0_p<P>.ms      3 banked primes, guard
  directionb_residual32.rows.txt          variable + row legend

Phases: emit | guards | screen [secs] | all
"""
import os, sys, time, pickle, random
from fractions import Fraction as Fr
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r1_experiment as R1
import r1_fullcore as FC

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "directionb_residual32"
STATE = "/tmp/directionb_tails_D21.pkl"
PRIMES = (105337, 105673, 200257)       # §2c banked verification primes
RADROWS = ["r3^2-3", "A1^3-3-r3", "A2^3-3+r3",
           "2*HW1^2-3*W1^2", "2*HW2^2-3*W2^2"]
SATROWS = ["uW1*W1-1", "uW2*W2-1", "uA*A1-uA*A2-1"]
RADVARS = ["W1", "HW1", "W2", "HW2", "A1", "A2", "r3"]
SATVARS = ["uW1", "uW2", "uA"]

OK = []
def chk(name, cond):
    OK.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name, flush=True)

def lvl(nm): return nm.rsplit("_", 1)[-1]

def load_rows():
    """window rows in documented order + the (20,0) inhomogeneity."""
    st = pickle.load(open(STATE, "rb"))
    byk, vars_ = st["byk"], st["vars"]
    rows = []                            # (label, vex, has42)
    for k in sorted(byk):
        for n in sorted(byk[k]):
            v = dict(byk[k][n])
            has42 = (k == 20 and n == 0)
            if has42:
                v[()] = R1.radd(v.get((), R1.RZERO), R1.rC(R1.K3(42)))
            for vk, r in v.items():      # z = B = 0 on every radkey
                for rk in r:
                    assert rk[0] == 0 and rk[7] == 0, "z/B in window row"
            rows.append(("Row_%d[eta^%d]%s" % (k, n, "+42" if has42 else ""),
                         v, has42))
    occ = sorted({vid for _, v, _ in rows for vk in v for vid in vk})
    high = [i for i in occ if vars_[i][:2] in ("tf", "tg")
            and int(lvl(vars_[i])) >= 43]
    low = [i for i in occ if vars_[i][:2] in ("tf", "tg")
           and int(lvl(vars_[i])) < 43]
    seven = [i for i in occ if vars_[i][:2] not in ("tf", "tg")]
    names = {}
    ordered = high + low + seven         # highs FIRST: msolve -e block
    for j, vid in enumerate(ordered):
        names[vid] = "x%d" % j
    return rows, names, ordered, (high, low, seven), vars_

def row_scale_terms(terms):
    L = 1
    for q, _ in terms:
        L = L * q.denominator // gcd(L, q.denominator)
    G = 0
    for q, _ in terms:
        G = gcd(G, abs((q * L).numerator))
    return Fr(L, G) if G > 1 else Fr(L)

def emit_modp(terms, scale, p):
    parts = []
    for q, m in terms:
        c = q * scale
        assert c.denominator == 1
        c = c.numerator % p
        if not c: continue
        parts.append("%d%s" % (c, "*" + m if m else ""))
    assert parts, "row vanished mod %d" % p
    return "+".join(parts)

def phase_emit():
    rows, names, ordered, (high, low, seven), vars_ = load_rows()
    hdr = [names[v] for v in ordered] + SATVARS + RADVARS
    # NOTE var order: x0..x{49} = the 50 high tails, then uW1,uW2,uA
    # sit AFTER the low block?  no -- elimination block = highs + u's:
    hdr = ([names[v] for v in high] + SATVARS
           + [names[v] for v in low] + [names[v] for v in seven]
           + RADVARS)
    nelim = len(high) + len(SATVARS)
    t0 = time.time()
    body0, bodyp = [], {p: [] for p in PRIMES}
    body0c, bodypc = [], {p: [] for p in PRIMES}
    labels = []
    for lab, v, has42 in rows:
        terms = R1.poly_terms(v, names)
        sc = row_scale_terms(terms)
        body0.append(R1.emit_expanded(v, names))
        for p in PRIMES:
            bodyp[p].append(emit_modp(terms, sc, p))
        labels.append(lab)
        # ctl0: drop the ENTIRE constant block (var-free part)
        vc = {vk: r for vk, r in v.items() if vk}
        if vc:
            tc = R1.poly_terms(vc, names)
            sc2 = row_scale_terms(tc)
            body0c.append(R1.emit_expanded(vc, names))
            for p in PRIMES:
                bodypc[p].append(emit_modp(tc, sc2, p))
    tailrows = RADROWS + SATROWS
    def write(path, char, eqs):
        with open(path, "w") as f:
            f.write(", ".join(hdr) + "\n%d\n" % char)
            f.write(",\n".join(eqs) + "\n")
        return os.path.getsize(path)
    sz = write(os.path.join(HERE, BASE + ".ms"), 0, body0 + tailrows)
    print("   %s.ms: %d eqs (%d window + %d rad + %d sat), %d vars, "
          "%.1f MB (%.1fs)" % (BASE, len(body0) + len(tailrows),
                               len(body0), len(RADROWS), len(SATROWS),
                               len(hdr), sz / 1e6, time.time() - t0))
    for p in PRIMES:
        # mod-p tail rows: same strings with coefficients already in
        # [0,p) -- rewrite the signed ones explicitly
        tp = ["r3^2+%d" % (p - 3), "A1^3+%d+%d*r3" % (p - 3, p - 1),
              "A2^3+%d+1*r3" % (p - 3),
              "2*HW1^2+%d*W1^2" % (p - 3), "2*HW2^2+%d*W2^2" % (p - 3),
              "uW1*W1+%d" % (p - 1), "uW2*W2+%d" % (p - 1),
              "uA*A1+%d*uA*A2+%d" % (p - 1, p - 1)]
        szp = write(os.path.join(HERE, "%s_p%d.ms" % (BASE, p)), p,
                    bodyp[p] + tp)
        szc = write(os.path.join(HERE, "%s_ctl0_p%d.ms" % (BASE, p)), p,
                    bodypc[p] + tp)
        print("   p=%d: main %.1f MB, ctl0 %.1f MB" % (p, szp / 1e6,
                                                       szc / 1e6))
    write(os.path.join(HERE, BASE + "_ctl0.ms"), 0, body0c + tailrows)
    with open(os.path.join(HERE, BASE + ".rows.txt"), "w") as f:
        f.write("# %s emission legend (%s)\n" % (BASE, time.ctime()))
        f.write("# state: %s\n" % STATE)
        f.write("# ELIMINATION BLOCK: first %d vars (= %d high tails "
                "levels>=43 + uW1,uW2,uA); msolve -e %d projects onto "
                "the low+7+radical space = the residual-32 system\n"
                % (nelim, len(high), nelim))
        for blk, vids in (("HIGH", high), ("LOW", low), ("SEVEN", seven)):
            for v in vids:
                f.write("%s = %s (%s)\n" % (names[v], vars_[v], blk))
        for i, lab in enumerate(labels):
            f.write("eq%d = %s\n" % (i, lab))
        f.write("then: %s\n" % " ; ".join(RADROWS + SATROWS))
        f.write("# ctl0 variant: same rows with the whole constant "
                "block dropped -- satisfied by the origin; GB=[1] "
                "there = transcription error (ctlA convention)\n")
        f.write("# NOT saturated: c_f c_g (consumed at the (J) tier, "
                "gauge=1 banked, not a chart datum); z, B (absent "
                "from all window radkeys, asserted)\n")
    print("   legend: %s.rows.txt; elimination block %d" % (BASE, nelim))
    return hdr, labels

# ------------------------------------------------------------- guards
def _tiny_parse_eval(eq, val, p):
    """independent minimal parser: sums of INTEGER-coeff monomials
    with * and ^ only (guard-A guarantees no parens)."""
    s = eq.replace("-", "+-")
    tot = 0
    for t in s.split("+"):
        if not t: continue
        neg = t.startswith("-")
        if neg: t = t[1:]
        c = 1
        for f in t.split("*"):
            if not f: continue
            if f.isdigit(): c = c * int(f) % p
            else:
                nm, _, e = f.partition("^")
                c = c * pow(val[nm], int(e) if e else 1, p) % p
        tot = (tot + (-c if neg else c)) % p
    return tot

def phase_guards():
    rows, names, ordered, (high, low, seven), vars_ = load_rows()
    files = [BASE + ".ms", BASE + "_ctl0.ms"] + \
        ["%s_p%d.ms" % (BASE, p) for p in PRIMES] + \
        ["%s_ctl0_p%d.ms" % (BASE, p) for p in PRIMES]
    for fn in files:                                       # guard A
        txt = open(os.path.join(HERE, fn)).read()
        assert "(" not in txt and ")" not in txt, ("PAREN", fn)
    chk("guard A: paren sweep, %d files" % len(files), True)
    hdr, char0, eqs0 = FCparse(BASE + ".ms")
    nwin = len(rows)
    scales = []
    for lab, v, _ in rows:
        scales.append(row_scale_terms(R1.poly_terms(v, names)))
    for p in PRIMES[:2]:                                   # guard B
        pt = FC.radical_point(p)
        assert pt, "banked prime %d lost radical point" % p
        _, _, eqsp = FCparse("%s_p%d.ms" % (BASE, p))
        okall = True
        for t in range(2):
            rng = random.Random(4200 + p + 97 * t)
            val = dict(pt)
            val["uW1"] = pow(pt["W1"], p - 2, p)
            val["uW2"] = pow(pt["W2"], p - 2, p)
            val["uA"] = pow((pt["A1"] - pt["A2"]) % p, p - 2, p)
            for h in hdr:
                if h.startswith("x"): val[h] = rng.randrange(1, p)
            xval = {vid: val[nm] for vid, nm in names.items()}
            for i, (lab, v, _) in enumerate(rows):
                want = 0
                for vk, r in v.items():
                    m = 1
                    for vid in vk: m = m * xval[vid] % p
                    want = (want + m * FC.ring_modp(r, pt, p)) % p
                want = want * FC.frmod(scales[i], p) % p
                g0 = _tiny_parse_eval(eqs0[i], val, p)
                gp = _tiny_parse_eval(eqsp[i], val, p)
                okall &= (g0 == want == gp)
            for j in range(nwin, len(eqs0)):               # rad+sat rows
                okall &= (_tiny_parse_eval(eqs0[j], val, p) == 0)
                okall &= (_tiny_parse_eval(eqsp[j], val, p) == 0)
        chk("guard B: independent-parser round-trip char0+p vs "
            "internal ring eval, %d rows x 2 pts, p=%d" % (len(eqs0), p),
            okall)
    # guard C: pattern-positive anchor at tails = 0
    p = PRIMES[0]; pt = FC.radical_point(p)
    ds = pickle.load(open("/tmp/directionb_dsys.pkl", "rb"))
    val = dict(pt, uW1=pow(pt["W1"], p - 2, p),
               uW2=pow(pt["W2"], p - 2, p),
               uA=pow((pt["A1"] - pt["A2"]) % p, p - 2, p))
    rng = random.Random(9000)
    for vid, nm in names.items():
        val[nm] = 0 if vars_[vid][:2] in ("tf", "tg") \
            else rng.randrange(1, p)
    ok, nz = True, 0
    for i, (lab, v, has42) in enumerate(rows):
        g = _tiny_parse_eval(eqs0[i], val, p)
        kk, nn = lab.split("[")[0], int(lab.split("^")[1].split("]")[0])
        if kk != "Row_20" or nn not in ds["byk"][20]:
            ok &= (g == 0); continue
        want = FC.ring_modp(ds["byk"][20][nn].get((), {}), pt, p)
        if nn == 0: want = (want + 42) % p
        want = want * FC.frmod(scales[i], p) % p
        ok &= (g == want); nz += g != 0
    chk("guard C: pattern-positive anchor -- at tails=0 all rows die "
        "except the 9 zero-tail Row_20 comps, which equal the BANKED "
        "dsys constants (+42 at eta^0) exactly mod %d; %d/9 nonzero "
        "at the generic radical point" % (p, nz), ok and nz >= 8)
    # guard D: ctl0 satisfied by the origin (all x = 0)
    _, _, eqsc = FCparse("%s_ctl0_p%d.ms" % (BASE, p))
    val0 = dict(val)
    for h in hdr:
        if h.startswith("x"): val0[h] = 0
    g = [j for j, e in enumerate(eqsc[:len(eqsc) - 8])
         if _tiny_parse_eval(e, val0, p)]
    chk("guard D: ctl0 window rows all vanish at the origin "
        "(satisfiability control is honestly satisfiable)", not g)

def FCparse(fn):
    lines = open(os.path.join(HERE, fn)).read().split("\n", 2)
    hdr = [h.strip() for h in lines[0].split(",")]
    return hdr, int(lines[1].strip()), \
        [e.strip() for e in lines[2].strip().rstrip(",").split(",\n")]

def phase_screen(secs=1200):
    import subprocess
    for tag in (["%s_ctl0_p%d" % (BASE, PRIMES[0])]
                + ["%s_p%d" % (BASE, p) for p in PRIMES]):
        fin = os.path.join(HERE, tag + ".ms")
        fout = os.path.join(HERE, tag + ".out")
        t0 = time.time()
        try:
            r = subprocess.run(["msolve", "-g", "2", "-t", "4",
                                "-f", fin, "-o", fout],
                               timeout=secs, capture_output=True)
            txt = open(fout).read() if os.path.exists(fout) else ""
            one = txt.strip().rstrip(":").endswith("[1]:") or \
                txt.replace("\n", "").strip() in ("[1]:", "[1]")
            print("   screen %s: rc=%d %.1fs out=%dB %s"
                  % (tag, r.returncode, time.time() - t0,
                     len(txt), "GB=[1] (EMPTY)" if one else
                     ("GB!=[1] (NONEMPTY certificate-free)" if txt
                      else "NO OUTPUT")), flush=True)
        except subprocess.TimeoutExpired:
            print("   screen %s: TIMEOUT %ds (bank emission for the "
                  "fleet)" % (tag, secs), flush=True)

# ---------------------------------------------------- no-log pins (§7)
# GATE 2 of the avenues sweep: the six live level-42 no-log pins
# (SHEET6-DIRECTIONB.md §7 — Keller action residues; exact, pure
# variable pins).  Append-only discipline: every _nolog file is the
# banked file + the 6 pin rows, prefix byte-identical (regression
# gate).  Files: directionb_residual32_nolog[_ctl0][_p<P>].ms
PINS42 = (("x46", "tf1_42"), ("x51", "tf2_42"), ("x56", "tg1_42"),
          ("x61", "tg2_42"), ("x64", "tg01_42"), ("x67", "tg02_42"))

def nolog_name(fn):
    return fn.replace(BASE, BASE + "_nolog", 1)

def phase_nolog():
    legend = open(os.path.join(HERE, BASE + ".rows.txt")).read()
    for nm, tv in PINS42:                     # hard mapping guard
        assert "%s = %s (LOW)" % (nm, tv) in legend, (nm, tv)
    chk("nolog: pin mapping x-name == registry name, 6/6 against "
        "rows.txt", True)
    pins = [nm for nm, _ in PINS42]
    srcs = [BASE + ".ms", BASE + "_ctl0.ms"] + \
        ["%s_p%d.ms" % (BASE, p) for p in PRIMES] + \
        ["%s_ctl0_p%d.ms" % (BASE, p) for p in PRIMES]
    for src in srcs:
        hdr, char, eqs = FCparse(src)
        assert all(nm in hdr for nm in pins), src
        dst = nolog_name(src)
        with open(os.path.join(HERE, dst), "w") as f:
            f.write(", ".join(hdr) + "\n%d\n" % char)
            f.write(",\n".join(eqs + pins) + "\n")
        h2, c2, e2 = FCparse(dst)
        assert e2[:len(eqs)] == eqs and e2[len(eqs):] == pins \
            and h2 == hdr and c2 == char, ("REGRESSION", dst)
        txt = open(os.path.join(HERE, dst)).read()
        assert "(" not in txt and ")" not in txt, ("PAREN", dst)
        print("   %s: %d eqs (+6 pins), prefix byte-identical, "
              "paren-free, %.1f MB" % (dst, len(e2),
                                       os.path.getsize(
                                           os.path.join(HERE, dst)) / 1e6))
    # pattern-positive anchor on the nolog main: tails=0 satisfies the
    # pins trivially and the 9 zero-tail Row_20 comps are unchanged
    rows, names, ordered, blocks, vars_ = load_rows()
    p = PRIMES[0]; pt = FC.radical_point(p)
    ds = pickle.load(open("/tmp/directionb_dsys.pkl", "rb"))
    hdr, _, eqs = FCparse(nolog_name(BASE + ".ms"))
    val = dict(pt, uW1=pow(pt["W1"], p - 2, p),
               uW2=pow(pt["W2"], p - 2, p),
               uA=pow((pt["A1"] - pt["A2"]) % p, p - 2, p))
    rng = random.Random(9000)
    for vid, nm in names.items():
        val[nm] = 0 if vars_[vid][:2] in ("tf", "tg") \
            else rng.randrange(1, p)
    scales = [row_scale_terms(R1.poly_terms(v, names))
              for _, v, _ in rows]
    ok = True
    for i, (lab, v, has42) in enumerate(rows):
        g = _tiny_parse_eval(eqs[i], val, p)
        kk, nn = lab.split("[")[0], int(lab.split("^")[1].split("]")[0])
        if kk != "Row_20" or nn not in ds["byk"][20]:
            ok &= (g == 0); continue
        want = FC.ring_modp(ds["byk"][20][nn].get((), {}), pt, p)
        if nn == 0: want = (want + 42) % p
        ok &= (g == want * FC.frmod(scales[i], p) % p)
    ok &= all(_tiny_parse_eval(e, val, p) == 0 for e in eqs[-6:])
    chk("nolog guard: pattern-positive anchor STILL passes on the "
        "_nolog main (tails=0 satisfies the 6 pins; 9 zero-tail "
        "Row_20 comps == banked dsys constants, +42 at eta^0)", ok)
    with open(os.path.join(HERE, BASE + ".rows.txt"), "a") as f:
        f.write("# --- §7 level-42 no-log pins (Keller action "
                "residues; SHEET6-DIRECTIONB.md §7) ---\n")
        f.write("# _nolog systems append these 6 exact pin rows "
                "(pure variable pins, one per live place):\n")
        for nm, tv in PINS42:
            f.write("# pin: %s = 0   (= %s = [t^42] of its root "
                    "series)\n" % (nm, tv))
        f.write("# frozen-stratum pins (not rows here): bf_42 = "
                "bg42_42 = bg21_42 = 0 (B frozen in D21)\n")
    print("   pins appended as comment block to %s.rows.txt" % BASE)

def phase_screen_nolog(secs=43200):
    import subprocess
    for tag in (["%s_nolog_ctl0_p%d" % (BASE, PRIMES[0])]
                + ["%s_nolog_p%d" % (BASE, p) for p in PRIMES]):
        fin = os.path.join(HERE, tag + ".ms")
        fout = os.path.join(HERE, tag + ".out")
        t0 = time.time()
        try:
            r = subprocess.run(["nice", "-n", "5", "msolve", "-g", "2",
                                "-t", "4", "-f", fin, "-o", fout],
                               timeout=secs, capture_output=True)
            txt = open(fout).read() if os.path.exists(fout) else ""
            one = txt.replace("\n", "").strip().rstrip(":") == "[1]"
            print("   screen %s: rc=%d %.1fs out=%dB %s"
                  % (tag, r.returncode, time.time() - t0, len(txt),
                     "GB=[1] (EMPTY)" if one else
                     ("GB!=[1] (alive mod p)" if txt else "NO OUTPUT")),
                  flush=True)
        except subprocess.TimeoutExpired:
            print("   screen %s: TIMEOUT %ds (bank for the fleet)"
                  % (tag, secs), flush=True)
    print("ALL NOLOG SCREENS DONE", flush=True)


if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "all"
    t0 = time.time()
    if ph in ("emit", "all"): phase_emit()
    if ph in ("guards", "all"): phase_guards()
    if ph == "screen":
        phase_screen(int(sys.argv[2]) if len(sys.argv) > 2 else 1200)
    if ph == "nolog": phase_nolog()
    if ph == "nolog_screen":
        phase_screen_nolog(int(sys.argv[2]) if len(sys.argv) > 2
                           else 43200)
    bad = [n for n, c in OK if not c]
    print("\nTOTAL: %d checks, %d FAIL %s  (%.1fs)"
          % (len(OK), len(bad), bad or "", time.time() - t0))
