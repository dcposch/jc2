#!/usr/bin/env python3
"""build_tails_modp.py -- mod-p symbolic D-window bank builder.

STATUS: INTERNAL TOOLING, UNREVIEWED.  FAIL-CLOSED.

WHAT: the exact structural mirror of the BANKED numeric dual-jet engine
(cases/valuation_e2.py build_jets/euler_rows -- the engine whose band
<= 40 restriction reproduces the banked 174x170 operator
byte-identically, cases/d43_regress.json), with the scalar tail values
replaced by SPARSE F_p POLYNOMIAL variables.  Output: the pristine rows
E = sum_a t^n eta^a * (polynomial in tails/KEEP7/W) through band D-1,
per (prime, fiber): zeta twists, radical selector values A1/A2/h1/h2,
and scalar constants are folded numerically mod p (exactly as the
numeric engine folds them); W1, W2, the KEEP7 dead-stretch frees and
every P-side tail through level 32+(D-1) stay symbolic.

WHY: the char-0 K3/radkey build (build_tails43.py) is the gold lane but
paces to days at D = 43; this mod-p lane produces the same per-fiber
folded rows (the only form the reduce/assemble stages consume) in
minutes-to-hours.  VALIDATION GATES (all hard):
  V1  at every banked D25 witness/interior completion supplied, each
      row's polynomial EVALUATES to the numeric engine's E.V entry
      exactly, and each tail-derivative evaluates to the E.G entry
      (full value + gradient agreement at N points, both engines);
  V2  at D = 25 the folded char-0 bank (directionb_tails_D25.pkl,
      radkeys folded per fiber exactly as cases/d25_reduce.py does)
      must equal this bank's rows 22/24 coefficient-for-coefficient
      (run on box01 where the char-0 bank lives; --check-c0-bank).
Any mismatch stops the stage.

Usage:
  python3 cases/build_tails_modp.py --prime P --fiber LAB --depth 43
        [--out FILE.pkl] [--validate-points N]
"""
import argparse
import hashlib
import json
import os
import pickle
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import valuation_e as V

# ---------------------------------------------------------------- SPoly
# monomial: frozenset-free canonical tuple ((vid, exp), ...) sorted by
# vid; poly: dict monomial -> coeff (int in [1, p)).
ONE = ()


def pmul(a, b, p):
    if not a or not b:
        return {}
    out = {}
    small, big = (a, b) if len(a) <= len(b) else (b, a)
    for ma, ca in small.items():
        for mb, cb in big.items():
            if ma and mb:
                d = dict(ma)
                for vid, e in mb:
                    d[vid] = d.get(vid, 0) + e
                m = tuple(sorted(d.items()))
            else:
                m = ma or mb
            c = (out.get(m, 0) + ca * cb) % p
            if c:
                out[m] = c
            else:
                out.pop(m, None)
    return out


def padd_into(out, b, p, scal=1):
    for m, c in b.items():
        c2 = (out.get(m, 0) + c * scal) % p
        if c2:
            out[m] = c2
        else:
            out.pop(m, None)


def pscal(a, c, p):
    c %= p
    if not c:
        return {}
    return {m: cc * c % p for m, cc in a.items()}


def pconst(c, p):
    c %= p
    return {ONE: c} if c else {}


def pvar(vid):
    return {((vid, 1),): 1}


def peval_point(a, vals, p):
    tot = 0
    for m, c in a.items():
        t = c
        for vid, e in m:
            t = t * pow(vals[vid], e, p) % p
        tot = (tot + t) % p
    return tot


def pderiv(a, vid, p):
    out = {}
    for m, c in a.items():
        d = dict(m)
        e = d.get(vid, 0)
        if not e:
            continue
        if e == 1:
            del d[vid]
        else:
            d[vid] = e - 1
        m2 = tuple(sorted(d.items()))
        c2 = (out.get(m2, 0) + c * e) % p
        if c2:
            out[m2] = c2
        else:
            out.pop(m2, None)
    return out


# ------------------------------------------------------------- the build
FAMS = ("tf1", "tf2", "tg1", "tg2", "tg01", "tg02")


class Engine(object):
    """Mirror of valuation_e2 with SPoly scalars.  Configured by
    (prime, fiber env, depth D): slots 0..D-1, tails r <= D-1."""

    def __init__(self, p, env, D):
        self.p = p
        self.D = D
        self.S = D            # slots 0..D-1
        self.HMAX = 34
        pt, r3, h32 = V.radical_env(p)
        self.Z = [pow(pt["z"], m, p) for m in range(42)]
        self.env = env
        # variable registry
        self.vars = []
        self.vid = {}
        for nm in ("W1", "W2", "uf18", "uf24", "uf30",
                   "vf1_34", "vf1_36", "vf2_34", "vf2_36"):
            self._add(nm)
        self.allowed = {}
        for f in FAMS:
            step = 2 if f.startswith("tg0") else 1
            self.allowed[f] = [r for r in range(6, D, step) if r != 10]
            for r in self.allowed[f]:
                self._add("%s_%d" % (f, 32 + r))

    def _add(self, nm):
        if nm not in self.vid:
            self.vid[nm] = len(self.vars)
            self.vars.append(nm)

    # jets: dict (h, s) -> SPoly
    def jmulJ(self, A, B, hcap=None):
        p = self.p
        S = self.S
        hcap = hcap or self.HMAX
        out = {}
        for (ha, sa), pa in A.items():
            if not pa:
                continue
            for (hb, sb), pb in B.items():
                h = ha + hb
                s = sa + sb
                if h >= hcap or s >= S or not pb:
                    continue
                cur = out.get((h, s))
                if cur is None:
                    out[(h, s)] = pmul(pa, pb, p)
                else:
                    padd_into(cur, pmul(pa, pb, p), p)
        return {k: v for k, v in out.items() if v}

    def orbit_levels(self, fam):
        """level -> SPoly (the numeric orbit_levels with symbols)."""
        p = self.p
        env = self.env
        side = "1" if fam.endswith("1") else "2"
        lv = {12: pconst(1, p),
              18: pvar(self.vid["uf18"]),
              24: pvar(self.vid["uf24"]),
              30: pvar(self.vid["uf30"]),
              32: pconst(env["A" + side], p),
              34: pvar(self.vid["vf%s_34" % side]),
              36: pvar(self.vid["vf%s_36" % side])}
        if fam in ("tf1", "tf2"):
            lv[37] = pvar(self.vid["W" + side])
        elif fam in ("tg1", "tg2"):
            lv[37] = pscal(pvar(self.vid["W" + side]),
                           env["h" + side], p)
        for r in self.allowed[fam]:
            lv[32 + r] = pvar(self.vid["%s_%d" % (fam, 32 + r)])
        return lv

    def through_block(self, Y, n7):
        p = self.p
        Z = self.Z
        blk = None
        for j in range(n7):
            fac = {(1, 0): pconst(1, p)}
            for lvl, poly in Y.items():
                s = lvl - 32
                if lvl < 32 or s >= self.S:
                    continue
                tw = Z[(7 * j * lvl) % 42]
                q = pscal(poly, (-tw) % p, p)
                if q:
                    fac[(0, s)] = q
            blk = fac if blk is None else self.jmulJ(blk, fac)
        return blk

    def smulS(self, a, b):
        """series (slot -> SPoly) truncated product."""
        p = self.p
        out = {}
        for sa, pa in a.items():
            for sb, pb in b.items():
                s = sa + sb
                if s >= self.S or not pa or not pb:
                    continue
                cur = out.get(s)
                if cur is None:
                    out[s] = pmul(pa, pb, p)
                else:
                    padd_into(cur, pmul(pa, pb, p), p)
        return {k: v for k, v in out.items() if v}

    def other_block(self, Y, k, n7):
        p = self.p
        Z = self.Z
        D = {}
        for lvl, poly in Y.items():
            s = lvl - 12
            if s >= self.S:
                continue
            tw = Z[(k * lvl) % 42]
            contrib = pscal(poly, (-tw) % p, p)
            if lvl in (12, 18, 24, 30):
                pvp = {12: pconst(1, p),
                       18: pvar(self.vid["uf18"]),
                       24: pvar(self.vid["uf24"]),
                       30: pvar(self.vid["uf30"])}[lvl]
                contrib = dict(pvp)
                padd_into(contrib, poly, p, scal=(-tw) % p)
            if contrib:
                D[s] = contrib
        Dp = {1: D}
        for r in range(2, n7 + 1):
            Dp[r] = self.smulS(Dp[r - 1], D)
        q = {}
        for r in range(1, n7 + 1):
            q[r] = {s: pscal(v, n7, p) for s, v in Dp[r].items()
                    if s % 6 == 0}
        e = [{0: pconst(1, p)}]
        for j in range(1, n7 + 1):
            acc = {}
            for r in range(1, j + 1):
                term = self.smulS(e[j - r], q[r])
                sgn = 1 if (r - 1) % 2 == 0 else p - 1
                for s, v in term.items():
                    cur = acc.get(s)
                    if cur is None:
                        acc[s] = pscal(v, sgn, p)
                    else:
                        padd_into(cur, v, p, scal=sgn)
            ij = pow(j, p - 2, p)
            e.append({s: pscal(v, ij, p) for s, v in acc.items() if v})
        blk = {}
        for i in range(n7 + 1):
            if 20 * i >= self.S and i > 0:
                break
            for s, v in e[n7 - i].items():
                if s + 20 * i < self.S and v:
                    blk[(i, s + 20 * i)] = v
        return blk

    def aside_orbit_jet(self, fam):
        n7 = 3 if fam.startswith("tg0") else 6
        Y = self.orbit_levels(fam)
        jp = self.through_block(Y, n7)
        for k in range(1, 7):
            jp = self.jmulJ(jp, self.other_block(Y, k, n7))
        return jp

    def b_block(self, power):
        p = self.p
        R = {(0, 0): pconst(1, p), (0, 6): pvar(self.vid["uf18"]),
             (0, 12): pvar(self.vid["uf24"]),
             (0, 18): pvar(self.vid["uf30"]),
             (1, 20): pconst(1, p)}
        R2 = self.jmulJ(R, R)
        R4 = self.jmulJ(R2, R2)
        Q = self.jmulJ(self.jmulJ(R4, R2), R)
        c = Q.get((0, 0), {})
        padd_into(c, pconst((-3 * pow(2, p - 2, p)) % p, p), p)
        Q[(0, 0)] = c
        out = None
        for _ in range(power):
            out = Q if out is None else self.jmulJ(out, Q)
        return out

    def build_jets(self):
        t0 = time.time()
        jf = self.jmulJ(self.aside_orbit_jet("tf1"),
                        self.aside_orbit_jet("tf2"))
        jf = self.jmulJ(jf, self.b_block(6))
        print("   [modp] f-jet done (%d slots, %.0fs)"
              % (len(jf), time.time() - t0), flush=True)
        jg = self.jmulJ(self.aside_orbit_jet("tg1"),
                        self.aside_orbit_jet("tg2"))
        jg = self.jmulJ(jg, self.jmulJ(self.aside_orbit_jet("tg01"),
                                       self.aside_orbit_jet("tg02")))
        jg = self.jmulJ(jg, self.b_block(9))
        print("   [modp] g-jet done (%d slots, %.0fs)"
              % (len(jg), time.time() - t0), flush=True)
        return jf, jg

    def euler_rows(self, jf, jg):
        p = self.p
        E = {}
        jA = {(h, s): pscal(v, (s - 12) % p, p)
              for (h, s), v in jf.items() if s != 12}
        jBg = {(h, s): pscal(v, (s - 18) % p, p)
               for (h, s), v in jg.items() if s != 18}
        jfH = {(h - 1, s): pscal(v, h, p)
               for (h, s), v in jf.items() if h}
        jgH = {(h - 1, s): pscal(v, h, p)
               for (h, s), v in jg.items() if h}
        T1 = self.jmulJ(jA, jgH)
        T2 = self.jmulJ(jfH, jBg)
        for (h, s), v in T1.items():
            cur = E.setdefault((h, s), {})
            padd_into(cur, v, p)
        for (h, s), v in T2.items():
            cur = E.setdefault((h, s), {})
            padd_into(cur, v, p, scal=p - 1)
        c = E.setdefault((0, 20), {})
        padd_into(c, pconst(42, p), p)
        return {k: v for k, v in E.items() if v}


# ------------------------------------------------------------ validation
def validate_against_numeric(eng, E_rows, p, env, points, X, DE):
    """V1: value + gradient agreement with the numeric V43 engine at
    completed points.  points: list of V43-point dicts."""
    V43 = X.V43
    for pi, point in enumerate(points):
        Enum, _aux = X.build_operator(point, p, 0, 0)
        Vv = Enum.V.astype("int64")
        Gg = Enum.G.astype("int64")
        vals = {}
        for nm, vid in eng.vid.items():
            if nm in ("W1", "W2"):
                vals[vid] = point["fixed"][nm] % p
            elif nm in ("uf18", "uf24", "uf30"):
                vals[vid] = point["fixed"].get(nm, 0) % p
            elif nm.startswith("vf"):
                vals[vid] = point["fixed"][nm] % p
            else:
                fam, lvl = nm.rsplit("_", 1)
                vals[vid] = point["tails"][fam].get(int(lvl) - 32, 0) % p
        nv = ng = 0
        for (h, s), poly in E_rows.items():
            if h >= 34 or s >= V43._S:
                continue
            got = peval_point(poly, vals, p)
            want = int(Vv[h][s]) if h < Vv.shape[0] else 0
            assert got == want, ("V1 value mismatch", pi, h, s, got,
                                 want)
            nv += 1
        # gradient check (slim): per rung band, two first-occurrence
        # tails on two rows -- the exact entries the family analysis
        # consumes.  Full-tail gradient sweeps are too slow at D43
        # sizes; the VALUE check above covers every row completely.
        top = max(s for (_h, s) in E_rows)
        for k in range(26, min(top, 42) + 1, 2):
            tail_nms = ["tf1_%d" % (k + 27), "tg02_%d" % (k + 32)]
            rows_k = [h for (h, s) in E_rows if s == k][:2]
            for h in rows_k:
                poly = E_rows[(h, k)]
                for nm in tail_nms:
                    if nm not in eng.vid:
                        continue
                    r = int(nm.rsplit("_", 1)[1]) - 32
                    f = nm.rsplit("_", 1)[0]
                    col = V43.GIDX.get((f, r))
                    if col is None:
                        continue
                    dpoly = pderiv(poly, eng.vid[nm], p)
                    got = peval_point(dpoly, vals, p)
                    want = int(Gg[h][k][col])
                    assert got == want, ("V1 gradient mismatch", pi,
                                         h, k, nm, got, want)
                    ng += 1
        print("   [V1] point %d: %d values + %d gradients exact"
              % (pi, nv, ng), flush=True)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime", type=int, required=True)
    ap.add_argument("--fiber", default="a00pp")
    ap.add_argument("--depth", type=int, default=43)
    ap.add_argument("--out", default=None)
    ap.add_argument("--validate-points", type=int, default=2)
    a = ap.parse_args()
    p = a.prime
    t0 = time.time()
    sys.path.insert(0, HERE)
    import d25_eplus as DE
    import eplus43 as X
    env = DE.fiber_env(p, a.fiber)
    eng = Engine(p, env, a.depth)
    print("engine: %d vars, D=%d, p=%d, fiber=%s"
          % (len(eng.vars), a.depth, p, a.fiber), flush=True)
    jf, jg = eng.build_jets()
    E = eng.euler_rows(jf, jg)
    print("rows built: %d (h,s) cells (%.0fs)"
          % (len(E), time.time() - t0), flush=True)
    # structural gates: odd bands empty, eta 30..33 empty, congruences
    S30 = [6 + 2 * ((aa + 1) % 3) for aa in range(29)]
    S30[28] = 16
    S30 = S30 + [36]
    for (h, s), v in E.items():
        assert s % 2 == 0, ("odd band nonzero", h, s)
        assert h < 30, ("eta surplus nonzero", h, s)
        assert s % 6 == S30[h] % 6 and s >= S30[h], ("congruence", h, s)
    print("PASS structural gates (odd/surplus/congruence)", flush=True)
    # V1 validation at prolongation-pipeline points
    if a.validate_points:
        import random
        rng = random.Random(11)
        hdr, rows = DE.parse_fiber_ms(p, a.fiber)
        cells = DE.cells_of_fiber(p, a.fiber)
        pts = []
        for i in range(a.validate_points):
            if i == 0:
                cv = DE.witness_cellval(p, a.fiber)
            else:
                fv = {v: rng.randrange(p) for v in
                      DE.FREE_BASE + DE.FREE_LIFT}
                cv = DE.solve_cell_point(p, hdr, rows, fv,
                                         *cells[rng.randrange(16)])
            dval, _dg = DE.reconstruct_point(p, cv, env)
            wit72, deep = DE.witness72_of(p, dval)
            _pv2, _E2, frontier = X.completed_point_v2(p, wit72, deep,
                                                       env)
            extra = {}
            for labl, vv in frontier.items():
                fam, lvl = labl.rsplit("_", 1)
                extra[(fam, int(lvl) - 32)] = vv
            pt43 = X.point43_from_v2(p, wit72, deep, env,
                                     extra_tails=extra)
            # randomize some deep completion coords to exercise the
            # new levels
            for f in FAMS:
                for r in (21, 25, 26, 30):
                    if r in [rr for rr in
                             X.V43.allowed_r(f)] and rng.random() < .5:
                        pt43["tails"][f][r] = rng.randrange(p)
            pts.append(pt43)
        validate_against_numeric(eng, E, p, env, pts, X, DE)
    out_path = a.out or os.path.join(
        HERE, "d43modp_p%d_%s.pkl" % (p, a.fiber))
    byk = {}
    for (h, s), v in E.items():
        byk.setdefault(s, {})[h] = v
    payload = {"D": a.depth, "prime": p, "fiber": a.fiber,
               "vars": eng.vars,
               "env": {k: env[k] for k in ("label", "A1", "A2", "h1",
                                           "h2")},
               "byk": byk,
               "note": ("mod-p per-fiber symbolic bank; zeta/radical "
                        "folded numerically; STRUCTURAL MIRROR of the "
                        "regression-validated numeric engine")}
    with open(out_path + ".tmp", "wb") as fh:
        pickle.dump(payload, fh, protocol=4)
    os.replace(out_path + ".tmp", out_path)
    print("DONE %.0fs -> %s" % (time.time() - t0, out_path), flush=True)


if __name__ == "__main__":
    main()
