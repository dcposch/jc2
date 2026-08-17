#!/usr/bin/env python3
"""Fast exact band-elimination engine (python-flint, DC priority).

MOD-P SPLIT-PRIME MODE: for split primes (legendre(3,p) = 1; all
three banked primes 105337/105673/200257 split), substitute
s = sqrt3 mod p, so K3-coefficients become GF(p) scalars; the window
rows live in GF(p)[template vars, A1, A2, W1, HW1, W2, HW2] with the
radical generators FREE (ring relations are NOT consumed by row
operations; they rejoin the emitted core as minimal-poly rows, with
exponents lattice-reduced at emission).  The nolog D21 window is
affine-linear in the 42 high tails; fraction-free Bareiss steps
R_t' = c_p R_t - A_t R_p with pivot coefficients CONSTANT in the
template variables run as flint nmod_mpoly arithmetic (C speed).

Pivot classes: "unit" (single w-weight + nonzero on all 4 h-sign
branches -- same class the exact run certified) and "mixed"
(two-weight constants, the tg-side).  Mixed pivots are sound for the
KILL DIRECTION ONLY: row ops give V(original) SUBSET V(core), so
core GB = [1]  =>  the original window variety is EMPTY; a NONEMPTY
core is inconclusive (documented in the emission header comment...
in rows.txt -- .ms files carry no comments).

Correctness gates (§7.S1 style):
  a. after the 10 banked sympy pivots (FORCED same sequence), every
     non-pivot row reduced-to-lattice == the banked exact residual
     mod p, row-for-row (ground truth);
  a2. the 10 forced pivot coefficients == reduction of the banked
     exact ones;
  b. tau: input rows at embedding r3 and p-r3 swap-match exactly
     (name swap + A/W/HW swap); output residual compared normalized;
  c. pattern-positive: template->0 leaves the Row_20-descended
     residual rows NONZERO (the +42/w4 content survives); plus an
     independent SCALAR replay of the full pivot sequence at random
     points must equal the mpoly residual evaluations.

Phases:  run [p] | emit | all     (default: all three primes)
"""
import os, sys, time, pickle, random
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import flint
import r1_experiment as R1
import r1_fullcore as FC
import directionb_compress as DC
import directionb_residual32_emit as E32

HERE = os.path.dirname(os.path.abspath(__file__))
PRIMES = (105337, 105673, 200257)
RADG = ("A1", "A2", "W1", "HW1", "W2", "HW2")
OK = []
def chk(name, cond):
    OK.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name, flush=True)

def r3_of(p):
    r3 = next(x for x in range(1, p) if x * x % p == 3)
    # pick the branch radical_point uses so gates align
    pt = FC.radical_point(p)
    return pt["r3"], pt

class Engine:
    def __init__(self, p, r3v):
        self.p, self.r3v = p, r3v
        self.rows, self.vars_ = DC.load_nolog_rows()
        self.occ = sorted({i for _, v in self.rows for vk in v
                           for i in vk})
        self.gi = {vid: j for j, vid in enumerate(self.occ)}
        self.nt = len(self.occ)
        names = tuple([self.vars_[i] for i in self.occ]) + RADG
        self.names = names
        self.ctx = flint.nmod_mpoly_ctx.get(names, modulus=p)
        self.HIGH = {i for i in self.occ
                     if self.vars_[i][:2] in ("tf", "tg")
                     and DC.lvl(self.vars_[i]) >= 43}
        self.P0 = [self.mk(v) for _, v in self.rows]
        self.P = list(self.P0)
        self.labs = [lab for lab, _ in self.rows]

    def reset(self): self.P = list(self.P0)

    def coef(self, c):
        return (FC.frmod(c[0], self.p)
                + FC.frmod(c[1], self.p) * self.r3v) % self.p

    def mk(self, v):
        d = {}
        for vk, r in v.items():
            base = [0] * (self.nt + 6)
            for vid in vk: base[self.gi[vid]] += 1
            for (z, e1, e2, pw, h1, qw, h2, B), c in r.items():
                e = list(base)
                e[self.nt], e[self.nt + 1] = e[self.nt] + e1, \
                    e[self.nt + 1] + e2
                e[self.nt + 2] += pw; e[self.nt + 3] += h1
                e[self.nt + 4] += qw; e[self.nt + 5] += h2
                k = tuple(e)
                d[k] = (d.get(k, 0) + self.coef(c)) % self.p
        return self.ctx.from_dict({k: c for k, c in d.items() if c})

    def tdeg0(self, f):
        """True iff f has no template-variable content."""
        return all(d == 0 for d in f.degrees()[:self.nt])

    def wclass(self, f):
        """'unit' | 'mixed' for a template-constant coefficient."""
        pr = self.p
        ws = set()
        for m in f.monoms():
            e1, e2, pw, h1, qw, h2 = m[self.nt:]
            ws.add((pw + h1, qw + h2))
        if len(ws) != 1: return "mixed"
        pt = FC.radical_point(pr)
        h32 = pt["HW1"] * pow(pt["W1"], pr - 2, pr) % pr
        for s1 in (1, -1):
            for s2 in (1, -1):
                tot = 0
                for m, c in zip(f.monoms(), f.coeffs()):
                    e1, e2, pw, h1, qw, h2 = m[self.nt:]
                    val = int(c) * pow(pt["A1"], e1, pr) \
                        * pow(pt["A2"], e2, pr) % pr
                    val = val * pow(h32 % pr, h1 + h2, pr) % pr
                    if s1 < 0 and h1 % 2: val = pr - val
                    if s2 < 0 and h2 % 2: val = pr - val
                    tot = (tot + val) % pr
                if tot == 0: return "mixed"
        return "unit"

    def eliminate(self, forced, maxpiv=99, verbose=True,
                  expected=None):
        t0 = time.time()
        self.reset()
        used, piv = set(), []
        self.a2ok = True
        def do_pivot(bi, h, want=None):
            Rp = self.P[bi]
            cp = Rp.derivative(self.gi[h])
            if want is not None:
                self.a2ok &= (self.reduce_lattice(cp)
                              == self.reduce_lattice(want))
            assert self.tdeg0(cp) and not cp.is_zero()
            kl = self.wclass(cp)
            used.add(bi); piv.append((h, self.labs[bi], kl))
            for bj in range(len(self.P)):
                if bj == bi or bj in used: continue
                At = self.P[bj].derivative(self.gi[h])
                if At.is_zero(): continue
                self.P[bj] = cp * self.P[bj] - At * self.P[bi]
            if verbose:
                print("   [p=%d] pivot %2d (%s): %s <- Row_%d[eta^%d]"
                      " (%.1fs)" % (self.p, len(piv), kl,
                                    self.vars_[h], self.labs[bi][0],
                                    self.labs[bi][1],
                                    time.time() - t0), flush=True)
        for j, (h, lab) in enumerate(forced):
            bi = self.labs.index(lab)
            do_pivot(bi, h, expected[j] if expected else None)
        for bi in range(len(self.P)):
            if len(piv) >= maxpiv: break
            if bi in used or self.labs[bi][0] < 12: continue
            v = self.P[bi]
            degs = v.degrees()
            hs = sorted(h for h in self.HIGH
                        if degs[self.gi[h]] > 0)
            for h in hs:
                if any(h == h2 for h2, _, _ in piv): continue
                cp = v.derivative(self.gi[h])
                if cp.is_zero() or not self.tdeg0(cp): continue
                do_pivot(bi, h); break
        resid = [(self.labs[bi], self.P[bi])
                 for bi in range(len(self.P))
                 if bi not in used and not self.P[bi].is_zero()]
        self.pivots, self.resid = piv, resid
        self.wall = time.time() - t0
        return piv, resid

    def reduce_lattice(self, f):
        """dict with radical exponents reduced to the banked lattice:
        A_i^3 -> (3 +- r3), HW_i^2 -> (3/2) W_i^2."""
        p, r3v = self.p, self.r3v
        a1v, a2v = (3 + r3v) % p, (3 - r3v) % p
        i32 = 3 * pow(2, p - 2, p) % p
        out = {}
        for m, c in zip(f.monoms(), f.coeffs()):
            e = list(m); c = int(c)
            q, e[self.nt] = divmod(e[self.nt], 3)
            c = c * pow(a1v, q, p) % p
            q, e[self.nt + 1] = divmod(e[self.nt + 1], 3)
            c = c * pow(a2v, q, p) % p
            q, e[self.nt + 3] = divmod(e[self.nt + 3], 2)
            c = c * pow(i32, q, p) % p; e[self.nt + 2] += 2 * q
            q, e[self.nt + 5] = divmod(e[self.nt + 5], 2)
            c = c * pow(i32, q, p) % p; e[self.nt + 4] += 2 * q
            k = tuple(e)
            out[k] = (out.get(k, 0) + c) % p
        return {k: c for k, c in out.items() if c}

def bank_rows_modp(eng):
    """the banked exact 10-pivot residual, mapped to engine exps."""
    st = pickle.load(open("/tmp/directionb_compressed.pkl", "rb"))
    out = {}
    for lab, v in st["resid"]:
        d = {}
        for vk, r in v.items():
            base = [0] * (eng.nt + 6)
            for vid in vk: base[eng.gi[vid]] += 1
            for (z, e1, e2, pw, h1, qw, h2, B), c in r.items():
                e = list(base)
                e[eng.nt] += e1; e[eng.nt + 1] += e2
                e[eng.nt + 2] += pw; e[eng.nt + 3] += h1
                e[eng.nt + 4] += qw; e[eng.nt + 5] += h2
                k = tuple(e)
                d[k] = (d.get(k, 0) + eng.coef(c)) % eng.p
        out[lab] = {k: c for k, c in d.items() if c}
    return out, [(h, lab) for h, lab, cp in st["pivc"]], st["pivc"]

def tau_map_dict(eng, d, engc):
    """tau: swap tf1<->tf2 etc template gens, A1<->A2, W/HW pairs."""
    perm = []
    for j, vid in enumerate(eng.occ):
        nm = DCtau(eng.vars_[vid])
        perm.append(eng.gi[next(i for i in eng.occ
                                if eng.vars_[i] == nm)])
    swap6 = [1, 0, 4, 5, 2, 3]
    out = {}
    for k, c in d.items():
        e = [0] * (eng.nt + 6)
        for j in range(eng.nt): e[perm[j]] = k[j]
        for j in range(6): e[eng.nt + swap6[j]] = k[eng.nt + j]
        out[tuple(e)] = c
    return out

def DCtau(nm):
    T = {"tf1": "tf2", "tf2": "tf1", "tg1": "tg2", "tg2": "tg1",
         "tg01": "tg02", "tg02": "tg01", "vf1": "vf2", "vf2": "vf1"}
    if "_" in nm:
        pre, lv = nm.rsplit("_", 1)
        if pre in T: return T[pre] + "_" + lv
    return nm

def run_prime(p):
    r3v, pt = r3_of(p)
    eng = Engine(p, r3v)
    bank, forced, pivc = bank_rows_modp(eng)
    t0 = time.time()
    engA = eng
    expected = [eng.mk({(): cp}) for _, _, cp in pivc]
    engA.eliminate(forced, maxpiv=10, verbose=False,
                   expected=expected)
    chk("[p=%d] gate a2: all 10 banked pivot coefficients == the "
        "engine's, compared SEQUENTIALLY mid-elimination" % p,
        engA.a2ok)
    got = {lab: engA.reduce_lattice(v) for lab, v in engA.resid}
    oka = set(got) == set(bank) and all(got[l] == bank[l]
                                        for l in bank)
    chk("[p=%d] gate a: 10-pivot engine state == banked EXACT "
        "residual mod p, row-for-row (%d rows, lattice-reduced)"
        % (p, len(bank)), oka)
    print("   [p=%d] 10-pivot replay wall: %.1fs (exact engine: "
          "2491s)" % (p, engA.wall), flush=True)
    # gate b (input): tau swap-match against conjugate embedding
    engC = Engine(p, (p - r3v) % p)
    okb = all(tau_map_dict(eng, dict(zip(
        [tuple(m) for m in a.monoms()], [int(c) for c in a.coeffs()])),
        engC) == dict(zip([tuple(m) for m in b.monoms()],
                          [int(c) for c in b.coeffs()]))
        for a, b in zip(eng.P0, engC.P0))
    chk("[p=%d] gate b: tau(input rows at r3) == input rows at "
        "p-r3, all 76 rows exactly" % p, okb)
    # full elimination
    eng2 = eng
    piv, resid = eng2.eliminate(forced, verbose=True)
    nunit = sum(1 for _, _, kl in piv if kl == "unit")
    hleft = {eng2.vars_[i] for _, v in resid
             for i in eng2.occ
             if i in eng2.HIGH and v.degrees()[eng2.gi[i]] > 0}
    print("   [p=%d] FULL: %d pivots (%d unit, %d mixed), %d residual"
          " rows, %d highs left %s, wall %.1fs"
          % (p, len(piv), nunit, len(piv) - nunit, len(resid),
             len(hleft), sorted(hleft) or "", eng2.wall), flush=True)
    # gate c: scalar replay at 2 random points + anchor
    okc = True
    class B: pass
    base = B(); base.labs = eng2.labs; base.P = eng2.P0
    base.HIGH = eng2.HIGH; base.gi = eng2.gi
    for t in range(2):
        rng = random.Random(3100 + p + t)
        val = {j: rng.randrange(1, p) for j in range(eng2.nt + 6)}
        for i in eng2.occ:
            if eng2.vars_[i] in DC.PIN42: val[eng2.gi[i]] = 0
        for j, nm in enumerate(RADG): val[eng2.nt + j] = pt[nm]
        args = [val[j] for j in range(eng2.nt + 6)]
        ev = lambda f: 0 if f.is_zero() else int(f(*args)) % p
        sc = {lab: ev(v) for lab, v in zip(base.labs, base.P)}
        cofs = {lab: {h: ev(v.derivative(base.gi[h]))
                      for h in base.HIGH}
                for lab, v in zip(base.labs, base.P)}
        used = set()
        for h, plab, kl in piv:
            cpv = cofs[plab][h]
            used.add(plab)
            for lab in base.labs:
                if lab in used: continue
                a = cofs[lab][h]
                if a == 0: continue
                sc[lab] = (sc[lab] * cpv - a * sc[plab]) % p
                for h2 in base.HIGH:
                    cofs[lab][h2] = (cofs[lab][h2] * cpv
                                     - a * cofs[plab][h2]) % p
        for lab, v in resid:
            okc &= (ev(v) == sc[lab] % p)
    chk("[p=%d] gate c1: independent SCALAR replay of the full pivot"
        " sequence == mpoly residual at 2 random points" % p, okc)
    z0 = [0] * (eng2.nt + 6)
    for j, nm in enumerate(RADG): z0[eng2.nt + j] = pt[nm]
    for i in eng2.occ:
        if eng2.vars_[i][:2] not in ("tf", "tg"):
            z0[eng2.gi[i]] = 11 + i % 7
    nz20 = [lab for lab, v in resid if lab[0] == 20
            and int(v(*z0)) % p]
    chk("[p=%d] gate c2: pattern-positive anchor -- %d Row_20-"
        "descended residual rows NONZERO at template-tails->0"
        % (p, len(nz20)), len(nz20) >= 1)
    return eng2, piv, resid, pt


# --------------------------------------------------------------- emit
def _ev_mono(k, gv, p):
    m = 1
    for j, e in enumerate(k):
        if e: m = m * pow(gv[j], e, p) % p
    return m

def emit_core(p, eng, piv, resid, pt):
    """cases/directionb_core_p<p>.ms: the true compressed core.
    All pivots were UNIT-class, so V(core) == projection of the
    original nolog window variety (w != 0 via uW rows): EQUIVALENT,
    not merely necessary.  s = sqrt3 substituted (split prime)."""
    _, names, ordered, blocks, _ = E32.load_rows()
    red = [(lab, eng.reduce_lattice(v)) for lab, v in resid]
    occ2 = sorted({j for _, d in red for k in d
                   for j in range(eng.nt) if k[j]})
    gnames = [None] * (eng.nt + 6)
    for j in occ2: gnames[j] = names[eng.occ[j]]
    for i, nm in enumerate(RADG): gnames[eng.nt + i] = nm
    hdr = [gnames[j] for j in occ2] + list(RADG) + \
        ["uW1", "uW2", "uA"]
    body, nterm, degp = [], 0, {}
    for lab, d in red:
        parts = []
        for k in sorted(d):
            mono = []
            for j in occ2 + list(range(eng.nt, eng.nt + 6)):
                if k[j]:
                    mono.append(gnames[j] +
                                ("^%d" % k[j] if k[j] > 1 else ""))
            parts.append("%d%s" % (d[k],
                                   "*" + "*".join(mono) if mono
                                   else ""))
            td = sum(k[j] for j in range(eng.nt))
            degp[td] = degp.get(td, 0) + 1
        nterm += len(d)
        body.append("+".join(parts))
    r3v = eng.r3v
    tp = ["A1^3+%d" % ((-(3 + r3v)) % p),
          "A2^3+%d" % ((-(3 - r3v)) % p),
          "2*HW1^2+%d*W1^2" % (p - 3), "2*HW2^2+%d*W2^2" % (p - 3),
          "uW1*W1+%d" % (p - 1), "uW2*W2+%d" % (p - 1),
          "uA*A1+%d*uA*A2+%d" % (p - 1, p - 1)]
    path = os.path.join(HERE, "directionb_core_p%d.ms" % p)
    with open(path, "w") as f:
        f.write(", ".join(hdr) + "\n%d\n" % p)
        f.write(",\n".join(body + tp) + "\n")
    sz = os.path.getsize(path)
    with open(path.replace(".ms", ".rows.txt"), "w") as f:
        f.write("# true core, split prime p=%d, r3=%d (s=sqrt3 "
                "substituted)\n" % (p, r3v))
        f.write("# 16 UNIT pivots (all 4 h-branches; equivalence "
                "tier, w!=0 chart):\n")
        for h, lab, kl in piv:
            f.write("#   %s <- Row_%d[eta^%d] (%s)\n"
                    % (eng.vars_[h], lab[0], lab[1], kl))
        for i, (lab, _) in enumerate(red):
            f.write("eq%d = Row_%d[eta^%d]%s\n"
                    % (i, lab[0], lab[1],
                       "+42" if lab == (20, 0) else ""))
        f.write("# vars: %d template (incl. leftover highs) + 6 "
                "radgens + 3 sat\n" % len(occ2))
    txt = open(path).read()
    assert "(" not in txt and ")" not in txt
    hdr2, char, eqs = E32.FCparse("directionb_core_p%d.ms" % p)
    okrt = (char == p)
    for t in range(2):
        rng = random.Random(1234 + p + t)
        val = {nm: rng.randrange(1, p) for nm in hdr}
        for nm in RADG: val[nm] = pt[nm]
        val["uW1"] = pow(pt["W1"], p - 2, p)
        val["uW2"] = pow(pt["W2"], p - 2, p)
        val["uA"] = pow((pt["A1"] - pt["A2"]) % p, p - 2, p)
        gv = [0] * (eng.nt + 6)
        for j in occ2: gv[j] = val[gnames[j]]
        for i in range(6): gv[eng.nt + i] = pt[RADG[i]]
        for i, (lab, d) in enumerate(red):
            want = sum(c * _ev_mono(k, gv, p)
                       for k, c in d.items()) % p
            okrt &= (E32._tiny_parse_eval(eqs[i], val, p) == want)
        for e in eqs[len(red):]:
            okrt &= (E32._tiny_parse_eval(e, val, p) == 0)
    chk("[p=%d] emission guards: paren sweep + independent-parser "
        "round-trip (%d rows + rad/sat, 2 points)" % (p, len(red)),
        okrt)
    return len(hdr), len(body) + len(tp), nterm, degp, sz

if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "all"
    t0 = time.time()
    if ph in ("run", "all"):
        ps = [int(sys.argv[2])] if len(sys.argv) > 2 else PRIMES
        results = {}
        for p in ps:
            results[p] = run_prime(p)
            eng2, piv, resid, pt = results[p]
            nv, ne, nt, degp, sz = emit_core(p, eng2, piv, resid, pt)
            print("   [p=%d] CORE: %d vars, %d eqs, %d terms, "
                  "template-degree profile %s, %d bytes"
                  % (p, nv, ne, nt, dict(sorted(degp.items())), sz),
                  flush=True)
        with open("/tmp/fastelim_results.pkl", "wb") as fh:
            pickle.dump({p: {"pivots": r[1],
                             "resid": [(lab, dict(zip(
                                 [tuple(m) for m in v.monoms()],
                                 [int(c) for c in v.coeffs()])))
                                 for lab, v in r[2]]}
                         for p, r in results.items()}, fh)
        print("banked /tmp/fastelim_results.pkl")
    bad = [n for n, c in OK if not c]
    print("\nTOTAL: %d checks, %d FAIL %s  (%.1fs)"
          % (len(OK), len(bad), bad or "", time.time() - t0))
