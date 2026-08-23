#!/usr/bin/env python3
"""valuation_e2.py -- CORRECTED valuation-e computation: the Euler/Ore
operator of xmodel/sol-round5.md section 1, evaluated on the banked
depth-23 witnesses (cases/d23_witnesses_p105337.json / _p105673.json).

STATUS: INTERNAL TOOLING, UNREVIEWED.
***EVERY e THIS TOOL PRINTS OR BANKS IS "E_CANDIDATE (EXPERIMENTAL)".***
PROMOTION GATE NOT PROVED (sol-round5.md "THEOREM STATUS -- CONJECTURE
E-HENSEL"): neither the Euler-term-eliminating change of coordinates nor
the filtered differential Newton lemma (completed-ideal bridge + delayed-
parametrix derivative loss + quadratic remainder => lifting for
D >= 2e+1) is banked.  No exact Ore-Popov/Smith normal form or causal
periodic-recurrence closure is implemented here either, so NO block ever
promotes under sec 1.3 step 5: strictly, "no DEPTH e" is reported, and
every numeric e below is the UNPROMOTED index diagnostic (V), tagged
E_CANDIDATE.  No germ claims regardless of values.  DEPTH-STAB e <= 11
is the eventual criterion only.

THE OBJECT (sol-round5.md sec 1, implemented exactly):
  * Source point: a banked witness (draws[0].witness72 through the
    x-registry) + one recorded deep-kernel draw (10 deep tails, levels
    49/54), with the deterministic ZERO COMPLETION: uf30 = 0, the four
    level-51 tails = 0, the four level-53 tails = 0, every later
    coefficient = 0; the choice is hashed.  No random fill anywhere.
  * Held fixed: radical branch, A_i, v_{i,34}, v_{i,36}, W_i, HW_i
    (base/chart units), B-side data (frozen), dead-stretch uf's.
    PIN42 = 0 (r = 10) is never a tangent direction.  Column mode is
    `tails`: W columns never enter (tailsW is the wrong object).
  * The six variable tail functions are exactly the six streams of
    build_generators in cases/r1_experiment.py (tf1 tf2 tg1 tg2 r >= 6
    r != 10; tg01 tg02 even r >= 6, r != 10).
  * E(Phi,Gamma) = (theta*Phi - 12 Phi) Gamma_eta
                   - Phi_eta (theta*Gamma - 18 Gamma) + 42 t^20,
    Phi/Gamma the exact normalized cyclic-orbit products (3 f-orbits /
    6 g-orbits, B-orbits frozen), rebuilt here NUMERICALLY mod p over
    dual numbers (value + gradient in the 6 tail streams) through the
    same construction as r1_experiment.gm_jet2 + directionb_strike.jrows.
    Pure-y truncation is EXACT below t^42 (x-side corrections first
    enter at t^42), so DBUILD = 42 and every quantity computed here
    (bands <= 40) is exact -- the t^42 omission caveat only concerns an
    all-depth parametrix, which is not claimed.
  * Grading (all-depth cyclic-character lemma, regressed here to band
    41, NOT proved all-depth): E = sum_{a=0}^{28} t^{s_a} H_a(t^6)
    eta^a, s_a = 6 + 2((a+1) mod 3), s_28 = 16 (sole exception),
    E_29 = 0; sum s_a = 240.  Inputs split into 30 residue streams
    (4*6 + 2*3), shifts r_rho = 6 + rho except r_4 = 16; sum = 288.
  * For each candidate free stream c (fixed family order tf1 tf2 tg1
    tg2 tg01 tg02, then ascending residue): B_c = 29 outputs x other
    29 input streams; over k[[u]]<Theta>, theta(t^r Z(u)) =
    t^r (r + 6 Theta) Z(u) -- the scalar entries dRow_(n,a)/dc_(q,r)
    are affine in r (gate G7) and are used directly.
  * Diagnostics per block (sec 1.3 steps 4-5): causal 29N x 29N
    truncations M_c(N), defect delta_c(N) = 29N - rank; delayed-loss
    lower bound / window estimate ell_c from the global-t filtration
    coverage test on the full band<=40 window (in-window coverage
    failures are CERTIFIED lower bounds: inputs with r > 40 cannot
    reach bands <= 40); index diagnostic e_c^idx = 6 d_c + r_c - 48
    when the defect has stabilized.  Bounded/stable delta does NOT
    prove (P); nothing here promotes.

USAGE
  python3 cases/valuation_e2.py --selftest
  python3 cases/valuation_e2.py --gates  [--prime 105337]
  python3 cases/valuation_e2.py --point 105337 0 0
  python3 cases/valuation_e2.py --run [--out cases/d23_ecandidates.json]
        [--light]   # --light: skip zeta2 + path-A rebuilds per point
                    # (they remain in --gates); default runs them per point
"""
import sys, os, re, json, time, hashlib, argparse, collections

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import valuation_e as V                      # banked 1a plumbing (reused)
import directionb_residual32_emit as E32     # x-registry

EXP = "E_CANDIDATE(EXPERIMENTAL)"
BLOCKNOTE = ("PROMOTION BLOCKED: CONJECTURE E-HENSEL (sol-round5.md sec 1) "
             "is unproved -- no admissible Theta-eliminating coordinate "
             "change and no filtered differential Newton lemma are banked; "
             "no exact Ore-Popov normal form / causal recurrence closure is "
             "implemented.  Strictly (sec 1.3 step 5) NO block promotes and "
             "there is NO DEPTH e; every numeric value is the unpromoted "
             "index diagnostic (V) tagged E_CANDIDATE(EXPERIMENTAL).  "
             "DEPTH-STAB e <= 11 is the eventual criterion only; no germ "
             "claims.")

PRIMES = (105337, 105673)
FAMS = ("tf1", "tf2", "tg1", "tg2", "tg01", "tg02")
FAM_RES = {"tf1": (0, 1, 2, 3, 4, 5), "tf2": (0, 1, 2, 3, 4, 5),
           "tg1": (0, 1, 2, 3, 4, 5), "tg2": (0, 1, 2, 3, 4, 5),
           "tg01": (0, 2, 4), "tg02": (0, 2, 4)}
def r_start(rho):
    return 16 if rho == 4 else 6 + rho
STREAMS = [(f, rho) for f in FAMS for rho in FAM_RES[f]]      # 30, spec order
S_A = [6 + 2 * ((a + 1) % 3) for a in range(29)]
S_A[28] = 16                                                   # sole exception
DBUILD = 42            # slots 0..41; pure-y exact below t^42
HMAX = 34              # eta powers 0..33 (E degree <= 33; 29..33 must vanish)
NMAX = 5               # causal truncations N = 1..5 (bands <= 40 suffice)
RMAX = 40              # tangent coords r <= 40 can reach bands <= 41

def allowed_r(fam):
    step = 2 if fam.startswith("tg0") else 1
    return [r for r in range(6, RMAX + 1, step) if r != 10]

GIDX = {}
for _f in FAMS:
    for _r in allowed_r(_f):
        GIDX[(_f, _r)] = len(GIDX)
GD = len(GIDX)                                                 # 170

# MEASURED DEEP-LABEL IDENTIFICATION (this tool, 2026-08-19).  The
# emission's x74..x83 deep-tail names (valuation_e.DEEPMAP) carried a
# tf-vs-tg split that valuation_e.py documents as "label-only and not
# recoverable from the frozen artifacts".  Rebuilding the exact source
# constructor over dual numbers recovers it: comparing dRow_22/dc of the
# frozen core23 emission against the constructor's band-22 derivative
# rows fixes the unique bijection emission-label -> true stream slot:
DEEP_RELABEL = {"tf1_49": "tg1_49", "tg1_49": "tf1_49",
                "tf2_49": "tg2_49", "tg2_49": "tf2_49",
                "tf1_54": "tg02_54", "tg02_54": "tf1_54",
                "tf2_54": "tg01_54", "tg01_54": "tf2_54",
                "tg1_54": "tg2_54", "tg2_54": "tg1_54"}
# (levels and W1/W2-side cofactor split of DEEPMAP were correct; only the
# tf-vs-tg / tg1-vs-tg2 assignment permutes.  Gates G5/G6 re-verify: with
# this relabeling the banked witnesses satisfy every band <= 22 row of
# the reconstructed operator and all 86 banked window-row derivative
# rows match the emissions exactly.)

# MEASURED REFUTATION (this tool, 2026-08-19; confirmed in char 0 by the
# exact symbolic machinery r1_experiment.gm_jet2 + directionb_strike.
# jrows at depth 37): the all-depth cyclic-character lemma of
# sol-round5.md sec 1.2 FAILS at eta^29: E_29 is NOT identically zero.
# Its first occurrence is band t^36, with derivative support exactly the
# six residue-4 streams (u^0 coefficients, level 48 = the C7-invariant
# levels == 0 mod 6); at the all-zero-tails configuration the exact
# tf1_48-coefficient of eta^29 t^36 is the RATIONAL number
# -147880611647231905314470776689/1024 (trivial radkey).  eta^30..33
# DO vanish identically to band 41, as do all odd bands, and the a<=28
# congruences/support starts hold, so the refutation is confined to the
# single extra output stream H_29 with start s_29 = 36.
ETA29_NUM = -147880611647231905314470776689
ETA29_DEN = 1024
S_29 = 36

# ---------------------------------------------------------------- helpers
_S = DBUILD
_AR = np.arange(_S)
_TIDX = _AR[:, None] - _AR[None, :]
_TMSK = _TIDX >= 0
_TIDXc = np.where(_TMSK, _TIDX, 0)

def toep(v):
    """Lower-triangular Toeplitz of a length-S coefficient vector: T @ x =
    truncated series product v*x."""
    return np.where(_TMSK, v[_TIDXc], 0.0)

class Jet(object):
    """Truncated eta-jet with dual (gradient) part.  V: (H, S) float64
    holding exact ints in [0, p); G: (H, S, GD) or None."""
    __slots__ = ("V", "G", "h")
    def __init__(self, h, grad):
        self.h = h
        self.V = np.zeros((h, _S))
        self.G = np.zeros((h, _S, GD)) if grad else None

def jmul(A, B, p, hcap=HMAX):
    """Exact truncated product of dual jets (mod p).  float64 is exact:
    products < p^2 ~ 1.1e10, accumulation < 34*42*p^2 < 2^53."""
    h = min(hcap, A.h + B.h - 1)
    C = Jet(h, A.G is not None or B.G is not None)
    BVt = B.V.T                       # (S, HB)
    BG2 = None
    if B.G is not None:
        BG2 = B.G.transpose(1, 0, 2).reshape(_S, -1)   # (S, HB*GD)
    for ha in range(A.h):
        if not A.V[ha].any():
            continue
        hb_lim = min(B.h, h - ha)
        if hb_lim <= 0:
            continue
        TA = toep(A.V[ha])
        C.V[ha:ha + hb_lim] += (TA @ BVt[:, :hb_lim]).T
        if BG2 is not None:
            R = (TA @ BG2[:, :hb_lim * GD]).reshape(_S, hb_lim, GD)
            C.G[ha:ha + hb_lim] += R.transpose(1, 0, 2)
    if A.G is not None:
        for hb in range(B.h):
            if not B.V[hb].any():
                continue
            ha_lim = min(A.h, h - hb)
            if ha_lim <= 0:
                continue
            TB = toep(B.V[hb])
            AG2 = A.G[:ha_lim].transpose(1, 0, 2).reshape(_S, -1)
            R = (TB @ AG2).reshape(_S, ha_lim, GD)
            C.G[hb:hb + ha_lim] += R.transpose(1, 0, 2)
    C.V %= p
    if C.G is not None:
        C.G %= p
    return C

def smul(a, b, p):
    """Dual series product: a = (v, g), g (S, GD) or None."""
    va, ga = a
    vb, gb = b
    Ta = toep(va)
    v = np.mod(Ta @ vb, p)
    g = None
    if gb is not None or ga is not None:
        g = np.zeros((_S, GD))
        if gb is not None:
            g += Ta @ gb
        if ga is not None:
            g += toep(vb) @ ga
        g %= p
    return (v, g)

def sscal(a, c, p):
    va, ga = a
    return (np.mod(va * c, p), None if ga is None else np.mod(ga * c, p))

def sadd(a, b, p):
    va, ga = a
    vb, gb = b
    g = None
    if ga is not None or gb is not None:
        g = np.zeros((_S, GD))
        if ga is not None:
            g += ga
        if gb is not None:
            g += gb
        g %= p
    return (np.mod(va + vb, p), g)

# ------------------------------------------------------------ source point
def x_registry():
    rows21, vars_ = V.raw_rows21()
    _, names, _, _, _ = E32.load_rows()
    return {names[vid]: vars_[vid] for vid in names}

ZC_RULE = ("deterministic zero completion (sol-round5.md 1.3 step 1): "
           "uf30 = 0; tf1_51 = tf2_51 = tg1_51 = tg2_51 = 0; "
           "tf1_53 = tf2_53 = tg1_53 = tg2_53 = 0; every unspecified "
           "later coefficient (levels >= 55) = 0; PIN42 = 0 (never a "
           "tangent direction); no random fill")

def build_point(p, wit72, deep_tails):
    """Witness + deep draw -> numeric source point.  Returns dict with
    per-family tail values {fam: {r: val}}, fixed data, completion hash."""
    x2tf = x_registry()
    pt, r3, h32 = V.radical_env(p)
    tails = {f: {} for f in FAMS}
    fixed = {"uf30": 0}
    for xn, val in wit72.items():
        val = int(val)
        if xn in ("W1", "W2"):
            fixed[xn] = val
            continue
        if xn in ("uW1", "uW2"):
            assert val == pow(int(wit72[xn.replace("u", "")]), p - 2, p), \
                "chart saturation broken (uW != W^-1)"
            continue
        nm = x2tf[xn]
        if nm.startswith("uf") or nm.startswith("vf"):
            fixed[nm] = val
            continue
        fam, lvl = nm.rsplit("_", 1)
        tails[fam][int(lvl) - 32] = val
    for nm, val in deep_tails.items():
        nm2 = DEEP_RELABEL.get(nm, nm)         # measured identification
        fam, lvl = nm2.rsplit("_", 1)
        tails[fam][int(lvl) - 32] = int(val)
    for f in FAMS:
        assert 10 not in tails[f], "PIN42 slot carries a value (wrong point)"
        assert all(6 <= r <= 22 for r in tails[f]), "tail r out of range"
    fixed.update({"A1": pt["A1"], "A2": pt["A2"], "r3": r3, "h32": h32,
                  "HW1": h32 * fixed["W1"] % p, "HW2": h32 * fixed["W2"] % p})
    blob = json.dumps({"prime": p, "tails": {f: sorted(tails[f].items())
                                             for f in FAMS},
                       "fixed": sorted((k, v) for k, v in fixed.items()),
                       "completion": ZC_RULE,
                       "deep_relabel": sorted(DEEP_RELABEL.items())},
                      sort_keys=True)
    zc_hash = hashlib.sha256(blob.encode()).hexdigest()
    return {"tails": tails, "fixed": fixed, "zc_hash": zc_hash}

# ------------------------------------------------- numeric orbit products
def orbit_levels(point, fam, p):
    """Level -> (value, grad-col-or-None) for one Aside orbit's series Y,
    zero-completed.  fam in FAMS; the paired fixed data follows
    r1_experiment.build_generators exactly (g shares uf/vf with f)."""
    fx = point["fixed"]
    side = "1" if fam.endswith("1") else "2"
    lv = {12: (1, None), 18: (fx["uf18"], None), 24: (fx["uf24"], None),
          30: (fx["uf30"], None), 32: (fx["A" + side], None),
          34: (fx["vf%s_34" % side], None), 36: (fx["vf%s_36" % side], None)}
    if fam in ("tf1", "tf2"):
        lv[37] = (fx["W" + side], None)
    elif fam in ("tg1", "tg2"):
        lv[37] = (fx["HW" + side], None)
    vals = point["tails"][fam]
    for r in allowed_r(fam):
        lv[32 + r] = (vals.get(r, 0), GIDX[(fam, r)])
    return lv

def through_block(Y, n7, p, Z):
    """prod_{j<n7} (eta - C_{7j} ytilde), ytilde slot s = Y[32+s]; the
    C_{7j} twist multiplies level lv by Z[(7 j lv) % 42]."""
    blk = None
    for j in range(n7):
        fac = Jet(2, True)
        fac.V[1][0] = 1
        for lvl, (val, gc) in Y.items():
            s = lvl - 32
            if lvl < 32 or s >= _S:
                continue
            tw = Z[(7 * j * lvl) % 42]
            fac.V[0][s] = (-tw * val) % p
            if gc is not None:
                fac.G[0][s][gc] = (-tw) % p
        blk = fac if blk is None else jmul(blk, fac, p)
    return blk

def other_block(Y, k, n7, p, Z):
    """Suborbit-Newton block for direction k != 0 (gm_jet2): Delta =
    P - C_k Y rel level 12; q_r = n7 [6|s] (Delta^r)_s; e_j Newton;
    block = sum_i e_{n7-i} (eta t^20)^i."""
    dv = np.zeros(_S)
    dg = np.zeros((_S, GD))
    for lvl, (val, gc) in Y.items():
        s = lvl - 12
        if s >= _S:
            continue
        tw = Z[(k * lvl) % 42]
        contrib = (-tw * val) % p
        if lvl in (12, 18, 24, 30):                    # P - C_k Y overlap
            pv = {12: 1, 18: Y[18][0], 24: Y[24][0], 30: Y[30][0]}[lvl]
            contrib = (pv - tw * val) % p
        dv[s] = contrib
        if gc is not None:
            dg[s][gc] = (-tw) % p
    D = (dv, dg)
    Dp = {1: D}
    for r in range(2, n7 + 1):
        Dp[r] = smul(Dp[r - 1], D, p)
    msk = (np.arange(_S) % 6 == 0).astype(np.float64)
    q = {}
    for r in range(1, n7 + 1):
        vr, gr = Dp[r]
        q[r] = (np.mod(vr * msk * n7, p),
                np.mod(gr * msk[:, None] * n7, p))
    e = [(np.zeros(_S), np.zeros((_S, GD)))]
    e[0][0][0] = 1
    for j in range(1, n7 + 1):
        acc = (np.zeros(_S), np.zeros((_S, GD)))
        for r in range(1, j + 1):
            term = smul(e[j - r], q[r], p)
            acc = sadd(acc, sscal(term, (-1) ** (r - 1) % p, p), p)
        e.append(sscal(acc, pow(j, p - 2, p), p))
    blk = Jet(n7 + 1, True)
    for i in range(n7 + 1):
        if 20 * i >= _S and i > 0:
            break
        v, g = e[n7 - i]
        blk.V[i][20 * i:] = v[:_S - 20 * i]
        blk.G[i][20 * i:] = g[:_S - 20 * i]
    return blk

def aside_orbit_jet(point, fam, p, Z):
    n7 = 3 if fam.startswith("tg0") else 6
    Y = orbit_levels(point, fam, p)
    jp = through_block(Y, n7, p, Z)
    for k in range(1, 7):
        jp = jmul(jp, other_block(Y, k, n7, p, Z), p)
    return jp

def b_block(point, power, p):
    """Frozen B-orbit closed form: Q = (Phat + eta t^20)^7 - B, B = 3/2;
    the C42 orbit of eta_B t^12 degenerates to ((...)^7 - B)^6 (f-side,
    B + GB42 give ^6 each... f uses ^6; g-side GB42*GB21 = ^9).  V-only."""
    fx = point["fixed"]
    R = Jet(2, False)
    R.V[0][0] = 1
    R.V[0][6] = fx["uf18"]
    R.V[0][12] = fx["uf24"]
    R.V[0][18] = fx["uf30"]
    R.V[1][20] = 1
    R2 = jmul(R, R, p)                                  # R^7 = R^4 * R^2 * R
    R4 = jmul(R2, R2, p)
    Q = jmul(jmul(R4, R2, p), R, p)
    Q.V[0][0] = (Q.V[0][0] - 3 * pow(2, p - 2, p)) % p
    out = None
    for _ in range(power):
        out = Q if out is None else jmul(out, Q, p)
    return out

def build_jets(point, p, Z):
    """Phi (f-side: P1 P2 B) and Gamma (g-side: Gp1 Gp2 G0p1 G0p2 GB42
    GB21) as dual jets."""
    jf = jmul(aside_orbit_jet(point, "tf1", p, Z),
              aside_orbit_jet(point, "tf2", p, Z), p)
    jf = jmul(jf, b_block(point, 6, p), p)
    jg = jmul(aside_orbit_jet(point, "tg1", p, Z),
              aside_orbit_jet(point, "tg2", p, Z), p)
    jg = jmul(jg, jmul(aside_orbit_jet(point, "tg01", p, Z),
                       aside_orbit_jet(point, "tg02", p, Z), p), p)
    jg = jmul(jg, b_block(point, 9, p), p)
    return jf, jg

def theta_shift(J, off, p):
    """(theta - off) on a lead-normalized jet: slot s multiplier (s-off)."""
    m = np.mod(_AR - off, p).astype(np.float64)
    K = Jet(J.h, J.G is not None)
    K.V = np.mod(J.V * m[None, :], p)
    if J.G is not None:
        K.G = np.mod(J.G * m[None, :, None], p)
    return K

def eta_deriv(J, p):
    K = Jet(max(J.h - 1, 1), J.G is not None)
    for h in range(1, J.h):
        K.V[h - 1] = np.mod(J.V[h] * h, p)
        if J.G is not None:
            K.G[h - 1] = np.mod(J.G[h] * h, p)
    return K

def euler_rows(jf, jg, p):
    """E = (theta Phi - 12 Phi) Gamma_eta - Phi_eta (theta Gamma - 18
    Gamma) + 42 t^20  (gauge c_f c_g = 1; directionb_strike.jrows)."""
    jA = theta_shift(jf, 12, p)
    jBg = theta_shift(jg, 18, p)
    jfH = eta_deriv(jf, p)
    jgH = eta_deriv(jg, p)
    T1 = jmul(jA, jgH, p)
    T2 = jmul(jfH, jBg, p)
    E = Jet(HMAX, True)
    h1 = min(T1.h, HMAX)
    E.V[:h1] += T1.V[:h1]
    E.G[:h1] += T1.G[:h1]
    h2 = min(T2.h, HMAX)
    E.V[:h2] -= T2.V[:h2]
    E.G[:h2] -= T2.G[:h2]
    E.V %= p
    E.G %= p
    E.V[0][20] = (E.V[0][20] + 42) % p
    return E

def path_A_rows(jf, jg, p):
    """Second direct differentiation path (gate G9): assemble (L) of
    sol-round5.md by hand -- (theta dPhi - 12 dPhi) Gamma_eta + (theta
    Phi - 12 Phi) (dGamma)_eta - (dPhi)_eta (theta Gamma - 18 Gamma)
    - Phi_eta (theta dGamma - 18 dGamma) -- multiplying VALUE-only jets
    against GRADIENT-only jets (a different product-rule grouping than
    the dual-jet path)."""
    def vonly(J):
        K = Jet(J.h, False)
        K.V = J.V.copy()
        return K
    def gonly(J):
        K = Jet(J.h, True)
        K.G = J.G.copy()
        return K
    fV, gV = vonly(jf), vonly(jg)
    fD, gD = gonly(jf), gonly(jg)
    terms = [jmul(theta_shift(fD, 12, p), eta_deriv(gV, p), p),
             jmul(theta_shift(fV, 12, p), eta_deriv(gD, p), p)]
    neg = [jmul(eta_deriv(fD, p), theta_shift(gV, 18, p), p),
           jmul(eta_deriv(fV, p), theta_shift(gD, 18, p), p)]
    DG = np.zeros((HMAX, _S, GD))
    for T in terms:
        h = min(T.h, HMAX)
        DG[:h] += T.G[:h]
    for T in neg:
        h = min(T.h, HMAX)
        DG[:h] -= T.G[:h]
    return np.mod(DG, p)

# ------------------------------------------------------- structural gates
def operator_hash(E, p):
    h = hashlib.sha256()
    Vv = E.V.astype(np.int64)
    Gg = E.G.astype(np.int64)
    h.update(json.dumps({"p": p, "V": Vv.tolist()}).encode())
    nz = np.argwhere(Gg)
    h.update(json.dumps([[int(x) for x in row] + [int(Gg[tuple(row)])]
                         for row in nz]).encode())
    return h.hexdigest()

def structure_gates(E, p, chk):
    """sol-round5.md 1.3 step 2 assertions (band <= 41 regression of the
    all-depth cyclic-character lemma; NOT an all-depth proof).  The
    lemma's eta29 == 0 assert is MEASURED-REFUTED (see ETA29_* above):
    it is recorded, warned, and the spec-literal 29-row object proceeds
    with the refutation attached to every output."""
    Vv = E.V.astype(np.int64)
    Gg = E.G.astype(np.int64)
    chk("G2a eta^30..33 components vanish identically (value and "
        "derivative)", not Vv[30:].any() and not Gg[30:].any())
    inv_gidx = {v: k for k, v in GIDX.items()}
    e29_bands = sorted({int(n) for n in range(_S)
                        if Vv[29][n] or Gg[29][n].any()})
    e29_entries = {}
    for n in e29_bands:
        cols = {("%s_%d" % (f, 32 + r)): int(Gg[29][n][GIDX[(f, r)]])
                for (f, r) in GIDX if Gg[29][n][GIDX[(f, r)]]}
        e29_entries[str(n)] = {"value": int(Vv[29][n]), "d/dc": cols}
    chk("G2b SPEC LEMMA eta29 == 0 (sol-round5 1.2/1.3): "
        "%s -- REFUTED: E_29 support %s, six residue-4 columns"
        % ("holds" if not e29_bands else "FAILS", e29_bands),
        not e29_bands, hard=False)
    chk("G2c eta^29 confinement: support exactly {t^36}, value 0 at the "
        "witness, derivative only in the six (fam, r=16) columns",
        e29_bands == [S_29] and Vv[29][S_29] == 0 and
        all(set(d["d/dc"]) <= {"%s_48" % f for f in FAMS}
            for d in e29_entries.values()))
    odd = [n for n in range(_S) if n % 2 == 1]
    chk("G3a all odd bands vanish (value and derivative)",
        not Vv[:, odd].any() and not Gg[:, odd].any())
    ok_cong = True
    starts = []
    for a in range(29):
        nz = [n for n in range(_S)
              if Vv[a][n] or Gg[a][n].any()]
        bad = [n for n in nz if n % 6 != S_A[a] % 6 or n < S_A[a]]
        if bad:
            ok_cong = False
        gstart = next((n for n in range(_S) if Gg[a][n].any()), None)
        starts.append(gstart)
    cong29 = all(n % 6 == S_29 % 6 and n >= S_29 for n in e29_bands)
    chk("G3b raw-label bijection: nonzero (n,a) only at n == s_a mod 6, "
        "n >= s_a  [(n,a) <-> (a,(n-s_a)/6)]; extra row a=29 graded at "
        "s_29 = 36", ok_cong and cong29)
    chk("G4 the 29 support starts: derivative support of class a starts "
        "exactly at s_a (s_a = 6+2((a+1)%%3), s_28 = 16); sum = 240",
        starts == S_A and sum(S_A) == 240)
    chk("G5 witness rows vanish: E value = 0 at every band <= 22 "
        "(re-verifies the banked D23 witness through the measured "
        "deep-label identification, incl. +42 t^20 gauge row)",
        not Vv[:, :23].any())
    b24 = sorted(a for a in range(29) if Vv[a][24])
    return {"starts": starts, "band24_nonzero_etas": b24,
            "value_residual_bands": sorted({int(n) for n in range(_S)
                                            if Vv[:, n].any()}),
            "eta29_refutation": {
                "spec_assert": "eta29 == 0 (sol-round5 1.2/1.3 step 2)",
                "measured": "FAILS: E_29 != 0, first occurrence t^36",
                "support_bands": e29_bands,
                "entries": e29_entries,
                "char0_exact_tf1_48_coeff":
                    "%d/%d (r1_experiment+directionb_strike, depth 37, "
                    "all-zero-tails configuration, trivial radkey)"
                    % (ETA29_NUM, ETA29_DEN),
            }}

def zero_config_crosscheck(p):
    """Gate G2d: at the all-zero-tails configuration (uf = vf = tails =
    0) the numeric engine's d(eta^29 t^36)/d(tf1_48) must equal the
    banked char-0 exact coefficient -147880611647231905314470776689/1024
    mod p (measured through r1_experiment + directionb_strike; trivial
    radkey, so independent of A/W/zeta branches)."""
    pt, r3, h32 = V.radical_env(p)
    Z = [pow(pt["z"], m, p) for m in range(42)]
    fixed = {"uf18": 0, "uf24": 0, "uf30": 0, "vf1_34": 0, "vf1_36": 0,
             "vf2_34": 0, "vf2_36": 0, "A1": pt["A1"], "A2": pt["A2"],
             "W1": pt["W1"], "W2": pt["W2"], "HW1": pt["HW1"],
             "HW2": pt["HW2"], "r3": r3, "h32": h32}
    point = {"tails": {f: {} for f in FAMS}, "fixed": fixed, "zc_hash": ""}
    jf, jg = build_jets(point, p, Z)
    E = euler_rows(jf, jg, p)
    got = int(E.G[29][S_29][GIDX[("tf1", 16)]])
    want = ETA29_NUM % p * pow(ETA29_DEN, p - 2, p) % p
    return got, want

def ore_affinity_gate(E, p):
    """(O): entries dRow_(n,a)/dc_(fam,r) affine in r within each
    (a, fam, d = n - r) bin -- the action of A + B*Theta.  Returns
    (#bins with >= 3 samples, #affine, support pattern set)."""
    Gg = E.G.astype(np.int64)
    bins = collections.defaultdict(dict)
    for (fam, r), col in GIDX.items():
        rho = r % 6
        arr = Gg[:, :, col]
        for a, n in zip(*np.nonzero(arr)):
            bins[(int(a), fam, rho, int(n) - r)][r] = int(arr[a][n])
    n3 = naff = 0
    support = set()
    for key, ent in bins.items():
        support.add(key)
        if len(ent) < 3:
            continue
        n3 += 1
        rs = sorted(ent)
        aff = True
        s0 = (ent[rs[1]] - ent[rs[0]]) * pow(rs[1] - rs[0], p - 2, p) % p
        for i in range(1, len(rs) - 1):
            si = (ent[rs[i + 1]] - ent[rs[i]]) * \
                pow(rs[i + 1] - rs[i], p - 2, p) % p
            if si != s0:
                aff = False
        naff += aff
    return n3, naff, support

def banked_row_match(E, p, dval23):
    """Gate G6: the dual-jet rows against the INDEPENDENT banked pipeline
    (valuation_e.window_partials: 76 raw D21 pickle rows exact + 10
    pristine Row_22 emission rows up to a recorded per-row unit)."""
    rowdata = V.window_partials(p, dval23, 23)
    Gg = E.G.astype(np.int64)
    n_exact = n_rows = 0
    ratios = {}
    ok = True
    for (n, a), (val, pr, prW) in rowdata.items():
        n_rows += 1
        mine = {}
        for (fam, r), col in GIDX.items():
            c = int(Gg[a][n][col])
            if c:
                mine["%s_%d" % (fam, 32 + r)] = c
        theirs = {DEEP_RELABEL.get(k, k): v for k, v in pr.items()
                  if k[:3] in ("tf1", "tf2", "tg1", "tg2") or
                  k[:4] in ("tg01", "tg02")}
        if val != 0:
            ok = False
        if mine == theirs:
            n_exact += 1
            continue
        if set(mine) != set(theirs) or not mine:
            ok = False
            continue
        ks = sorted(mine)
        r0 = theirs[ks[0]] * pow(mine[ks[0]], p - 2, p) % p
        if all(theirs[k] == mine[k] * r0 % p for k in ks):
            ratios[str((n, a))] = r0
        else:
            ok = False
    return ok, n_exact, n_rows, ratios

# --------------------------------------------------- linear algebra mod p
def rankp(M, p):
    M = np.mod(M.astype(np.int64), p)
    R, C = M.shape
    r = 0
    for c in range(C):
        if r == R:
            break
        piv = None
        for i in range(r, R):
            if M[i][c]:
                piv = i
                break
        if piv is None:
            continue
        M[[r, piv]] = M[[piv, r]]
        M[r] = M[r] * pow(int(M[r][c]), p - 2, p) % p
        nz = np.nonzero(M[:, c])[0]
        nz = nz[nz != r]
        if len(nz):
            M[nz] = (M[nz] - np.outer(M[nz, c], M[r])) % p
        r += 1
    return r

class Colspace(object):
    """Incremental reduced column-echelon basis mod p with unit-vector
    membership via one matmul (for the filtered coverage test)."""
    def __init__(self, R, p):
        self.R = R
        self.p = p
        self.basis = []          # list of (pivot_row, vector)
        self.pivots = []
    def add(self, v):
        p = self.p
        v = v % p
        for pr, b in self.basis:
            c = v[pr]
            if c:
                v = (v - c * b) % p
        nzr = np.nonzero(v)[0]
        if not len(nzr):
            return False
        pr = int(nzr[0])
        v = v * pow(int(v[pr]), p - 2, p) % p
        for i, (pr2, b2) in enumerate(self.basis):
            c = b2[pr]
            if c:
                self.basis[i] = (pr2, (b2 - c * v) % p)
        self.basis.append((pr, v))
        self.pivots.append(pr)
        return True
    def covered_rows(self):
        """Boolean per row o: e_o in the column space."""
        p = self.p
        if not self.basis:
            return np.zeros(self.R, dtype=bool)
        B = np.stack([b for _, b in self.basis], axis=1)     # (R, k)
        piv = np.array([pr for pr, _ in self.basis])
        Res = np.eye(self.R, dtype=np.int64)
        Res = (Res - B.astype(np.int64) @ Res[piv, :]) % p
        return ~Res.any(axis=0)

# ----------------------------------------------------- block diagnostics
def block_diagnostics(E, p, nmax=NMAX):
    """The deterministic square-block scan of sol-round5.md 1.2/1.3:
    for each candidate free stream c, the 29x29 operator block B_c;
    causal truncations M_c(N), defect profile, filtered delayed-loss
    window bound, index diagnostic (V).  NOTHING PROMOTES (no Ore
    normal form here); all outputs are E_CANDIDATE diagnostics."""
    Gg = E.G.astype(np.int64)
    out_rows_all = [(a, j) for a in range(29)
                    for j in range((RMAX - S_A[a]) // 6 + 1)]
    def entry(a, n, fam, r):
        return int(Gg[a][n][GIDX[(fam, r)]])
    blocks = []
    for ci, (cf, crho) in enumerate(STREAMS):
        rc = r_start(crho)
        instreams = [s for s in STREAMS if s != (cf, crho)]
        # causal truncations
        deltas = []
        for N in range(1, nmax + 1):
            rows = [(a, j) for a in range(29) for j in range(N)]
            cols = [(f, rho, i) for (f, rho) in instreams
                    for i in range(N)]
            M = np.zeros((len(rows), len(cols)), dtype=np.int64)
            for ri, (a, j) in enumerate(rows):
                n = S_A[a] + 6 * j
                for cj, (f, rho, i) in enumerate(cols):
                    r = r_start(rho) + 6 * i
                    if n >= r:
                        M[ri][cj] = entry(a, n, f, r)
            assert M.shape == (29 * N, 29 * N), "block not square"
            deltas.append(29 * N - rankp(M, p))
        d_c = deltas[-1] if len(deltas) >= 2 and \
            deltas[-1] == deltas[-2] else None
        stable3 = len(deltas) >= 3 and deltas[-1] == deltas[-2] == deltas[-3]
        # filtered coverage on the full band<=40 window
        cols_full = []
        for (f, rho) in instreams:
            for r in range(r_start(rho), RMAX + 1, 6):
                cols_full.append((f, r))
        col_lv = np.array([r for (f, r) in cols_full])
        row_lv = np.array([S_A[a] + 6 * j for (a, j) in out_rows_all])
        Mw = np.zeros((len(out_rows_all), len(cols_full)), dtype=np.int64)
        for ri, (a, j) in enumerate(out_rows_all):
            n = S_A[a] + 6 * j
            for cj, (f, r) in enumerate(cols_full):
                if n >= r:
                    Mw[ri][cj] = entry(a, n, f, r)
        order = np.argsort(-col_lv, kind="stable")
        cs = Colspace(len(out_rows_all), p)
        ell_need = []
        prev_n = None
        oi = 0
        for n in sorted(set(col_lv), reverse=True):
            while oi < len(order) and col_lv[order[oi]] >= n:
                cs.add(Mw[:, order[oi]].copy())
                oi += 1
            cov = cs.covered_rows()
            bad = row_lv[~cov]
            f_n = int(bad.max()) + 1 if len(bad) else 0
            ell_need.append((int(n), max(0, f_n - int(n))))
        ell_window = max(l for _, l in ell_need) if ell_need else 0
        # weighted-pivot checksum on M_c(NMAX): greedy min-loss pivots
        rowsN = [(a, j) for a in range(29) for j in range(nmax)]
        colsN = [(f, rho, i) for (f, rho) in instreams for i in range(nmax)]
        rlv = [S_A[a] + 6 * j for (a, j) in rowsN]
        clv = [r_start(rho) + 6 * i for (f, rho, i) in colsN]
        MN = np.zeros((len(rowsN), len(colsN)), dtype=np.int64)
        for ri, (a, j) in enumerate(rowsN):
            n = S_A[a] + 6 * j
            for cj, (f, rho, i) in enumerate(colsN):
                r = r_start(rho) + 6 * i
                if n >= r:
                    MN[ri][cj] = entry(a, n, f, r)
        loss_sum, npiv = weighted_pivot_checksum(MN, rlv, clv, p)
        # eta29 augmentation (beyond spec; the refuted lemma excluded
        # this row): defect of [M_c(N); eta29 row] -- the extra measured
        # output H_29 (band 36 = its only in-window coefficient row).
        aug = []
        for N in range(1, nmax + 1):
            cols = [(f, rho, i) for (f, rho) in instreams
                    for i in range(N)]
            M = np.zeros((29 * N + 1, len(cols)), dtype=np.int64)
            for ri, (a, j) in enumerate([(a, j) for a in range(29)
                                         for j in range(N)]):
                n = S_A[a] + 6 * j
                for cj, (f, rho, i) in enumerate(cols):
                    r = r_start(rho) + 6 * i
                    if n >= r:
                        M[ri][cj] = entry(a, n, f, r)
            for cj, (f, rho, i) in enumerate(cols):
                r = r_start(rho) + 6 * i
                if S_29 >= r:
                    M[29 * N][cj] = entry(29, S_29, f, r)
            aug.append(29 * N + 1 - rankp(M, p))
        e_idx = None if d_c is None else 6 * d_c + rc - 48
        consistent = (d_c is not None and e_idx is not None and
                      e_idx >= 0 and ell_window <= e_idx)
        blocks.append({
            "stream": "%s/r%d" % (cf, crho), "order": ci, "r_c": rc,
            "delta_profile_N1..%d" % nmax: deltas,
            "delta_plus_eta29_N1..%d" % nmax: aug,
            "d_c_stabilized": d_c, "delta_stable_3win": bool(stable3),
            "e_index_V": e_idx,
            "e_index_note": "UNPROMOTED E_INDEX diagnostic (V): "
                            "6*d_c + r_c - 48; not a theorem",
            "ell_window": int(ell_window),
            "ell_note": "E_LOSS window bound: certified lower bound AND "
                        "in-window estimate for (P) on bands<=40; not an "
                        "all-depth certificate",
            "ell_profile": ell_need,
            "pivot_checksum": {"loss_sum": int(loss_sum),
                               "n_pivots": int(npiv)},
            "stopped_gt11": bool(ell_window > 11 or
                                 (e_idx is not None and e_idx > 11)),
            "consistent_diagnostics": bool(consistent),
            "promoted": False,
        })
    return blocks

def weighted_pivot_checksum(M, rlv, clv, p):
    """Greedy global-t filtered elimination: repeatedly pivot on the
    entry minimizing (row level - col level), levels ascending; returns
    (sum of losses, #pivots).  Recorded diagnostic only."""
    M = np.mod(M.astype(np.int64), p)
    R, C = M.shape
    usedr = np.zeros(R, dtype=bool)
    usedc = np.zeros(C, dtype=bool)
    order = sorted(((rlv[i] - clv[j], rlv[i], i, j)
                    for i in range(R) for j in range(C)
                    if rlv[i] >= clv[j]))
    loss = npiv = 0
    for lo, _, i, j in order:
        if usedr[i] or usedc[j] or not M[i][j]:
            continue
        usedr[i] = usedc[j] = True
        loss += lo
        npiv += 1
        inv = pow(int(M[i][j]), p - 2, p)
        row = M[i] * inv % p
        nz = np.nonzero(M[:, j])[0]
        nz = nz[~usedr[nz]]
        if len(nz):
            M[nz] = (M[nz] - np.outer(M[nz, j], row)) % p
    return loss, npiv

# ------------------------------------------------------------- per point
GATES = []
def chk(name, cond, hard=True):
    GATES.append((name, bool(cond), hard))
    print(("PASS " if cond else ("FAIL " if hard else "WARN ")) + name,
          flush=True)
    if hard and not cond:
        raise SystemExit("EULER-E GATE FAILS at " + name)

def dval_for_banked(p, point):
    """EMISSION-name valuation for valuation_e.window_partials: the
    banked rows carry the conventional DEEPMAP deep labels, so the ten
    deep slots are presented through the inverse of DEEP_RELABEL
    (an involution); PIN42 names set to 0 defensively."""
    dval = {}
    for f in FAMS:
        for r, v in point["tails"][f].items():
            dval["%s_%d" % (f, 32 + r)] = v
        dval["%s_42" % f] = 0
    for X, Y in list(DEEP_RELABEL.items()):
        dval[X] = point["tails"][Y.rsplit("_", 1)[0]].get(
            int(Y.rsplit("_", 1)[1]) - 32, 0)
    fx = point["fixed"]
    for k in ("uf18", "uf24", "vf1_34", "vf1_36", "vf2_34", "vf2_36",
              "A1", "A2", "W1", "W2", "HW1", "HW2"):
        dval[k] = fx[k]
    dval["uf30"] = 0
    return dval

def run_point(p, wit72, deep_tails, tag="", light=False, quiet=False):
    t0 = time.time()
    pt, r3, h32 = V.radical_env(p)
    Zroot = pt["z"]
    assert pow(Zroot, 42, p) == 1 and all(
        pow(Zroot, 42 // q, p) != 1 for q in (2, 3, 7)), \
        "banked z is not a primitive 42nd root"
    Z = [pow(Zroot, m, p) for m in range(42)]
    point = build_point(p, wit72, deep_tails)
    jf, jg = build_jets(point, p, Z)
    E = euler_rows(jf, jg, p)
    op_hash = operator_hash(E, p)
    res = {"zc_hash": point["zc_hash"], "operator_hash": op_hash,
           "zeta": Zroot}
    def qchk(name, cond, hard=True):
        if quiet:
            if not cond:
                chk(tag + name, cond, hard)
            else:
                GATES.append((tag + name, True, hard))
        else:
            chk(tag + name, cond, hard)
    # structure gates (sec 1.3 step 2)
    def _chk(name, cond, hard=True):
        qchk(name, cond, hard)
    st = structure_gates(E, p, _chk)
    res.update(st)
    n3, naff, support = ore_affinity_gate(E, p)
    qchk("G7 Ore structure (O): all %d (a,fam,d) bins with >=3 stream "
         "samples affine in r (A + B*Theta action)" % n3, naff == n3)
    res["ore_bins_3plus"] = [n3, naff]
    res["ore_support_hash"] = hashlib.sha256(
        json.dumps(sorted(map(list, support))).encode()).hexdigest()
    ok6, nex, nrows, ratios = banked_row_match(E, p, dval_for_banked(p, point))
    qchk("G6 banked-pipeline cross-check: %d/%d window rows match "
         "(%d exact, %d up to a recorded per-row unit)"
         % (nrows, nrows, nex, len(ratios)), ok6)
    res["banked_match"] = {"rows": nrows, "exact": nex,
                           "unit_rescaled": ratios}
    # G10: the certified Row_22 Schur rank through the new operator
    Gg = E.G.astype(np.int64)
    deepcols = [(f, 17) for f in ("tf1", "tf2", "tg1", "tg2")] + \
               [(f, 22) for f in FAMS]
    rows22 = [a for a in range(29) if S_A[a] == 10] + [28]
    M22 = np.zeros((10, 10), dtype=np.int64)
    for i, a in enumerate(rows22):
        for j, (f, r) in enumerate(deepcols):
            M22[i][j] = Gg[a][22][GIDX[(f, r)]]
    rk22 = rankp(M22, p)
    qchk("G10 band-22 deep block rank == 4 (the certified Schur rank)",
         rk22 == 4)
    res["deep_schur_rank"] = int(rk22)
    if not light:
        # G8 zeta-branch invariance (second primitive 42nd root)
        Z2r = pow(Zroot, 5, p)
        Z2 = [pow(Z2r, m, p) for m in range(42)]
        jf2, jg2 = build_jets(point, p, Z2)
        E2 = euler_rows(jf2, jg2, p)
        qchk("G8 zeta-branch invariance: operator identical under "
             "zeta -> zeta^5 rebuild", operator_hash(E2, p) == op_hash)
        # G9 second direct differentiation path: (L) assembled by hand
        DG = path_A_rows(jf, jg, p)
        qchk("G9 second differentiation path: hand-assembled (L) == "
             "dual-jet derivative", np.array_equal(DG, E.G))
    blocks = block_diagnostics(E, p)
    cands = [b for b in blocks if b["consistent_diagnostics"]]
    e_cand = min((b["e_index_V"] for b in cands), default=None)
    argmin = next((b["stream"] for b in cands
                   if b["e_index_V"] == e_cand), None)
    res["blocks"] = blocks
    res["depth_e_strict"] = None
    res["depth_e_strict_note"] = ("no block promotes (no Ore certificate; "
                                  "CONJECTURE E-HENSEL unproved): strictly "
                                  "NO DEPTH e")
    res["e_candidate"] = {"tag": EXP, "value": e_cand,
                          "argmin_stream": argmin,
                          "n_consistent_blocks": len(cands),
                          "promoted": False}
    res["seconds"] = round(time.time() - t0, 1)
    return res, E

# ------------------------------------------------------------ full runs
def witness_file(p):
    return os.path.join(HERE, "d23_witnesses_p%d.json" % p)

def iter_points(p):
    W = json.load(open(witness_file(p)))
    for w in W["witnesses"]:
        wit72 = w["draws"][0]["witness72"]
        for dd in w["deep_draws"]:
            yield (w["index"], dd["kernel_draw"], wit72, dd["deep_tails"])

def run_gates(primes):
    print("== VALUATION-E2 GATE SUITE (Euler/Ore operator, sol-round5 "
          "sec 1) ==")
    print("   " + BLOCKNOTE)
    chk("G1a input streams: 30 = 4*6 + 2*3, shifts r_rho = 6+rho "
        "(r_4 = 16), sum = 288",
        len(STREAMS) == 30 and
        sum(r_start(rho) for _, rho in STREAMS) == 288)
    chk("G1b output streams: 29 classes, s_a = 6+2((a+1)%3), s_28 = 16, "
        "sum = 240", len(S_A) == 29 and sum(S_A) == 240)
    chk("G1c square block: every B_c is 29 outputs x 29 input streams "
        "(one free stream); M_c(N) is 29N x 29N (asserted per block)",
        all(len([s for s in STREAMS if s != c]) == 29 for c in STREAMS))
    for p in primes:
        got, want = zero_config_crosscheck(p)
        chk("G2d-p%d char-0 crosscheck: numeric d(eta29 t^36)/d(tf1_48) "
            "at the zero configuration == exact %d/%d mod p (= %d)"
            % (p, ETA29_NUM, ETA29_DEN, want), got == want)
    per_prime = {}
    for p in primes:
        print("-- p = %d: witness 0 / kernel draw 0 full battery --" % p)
        w0 = next(iter_points(p))
        res, E = run_point(p, w0[2], w0[3], tag="p%d " % p)
        per_prime[p] = res
        print("   operator %s...  zc %s...  (%.0fs)"
              % (res["operator_hash"][:16], res["zc_hash"][:16],
                 res["seconds"]))
    if len(per_prime) == 2:
        a, b = (per_prime[p] for p in primes)
        chk("G11a cross-prime: support starts identical",
            a["starts"] == b["starts"])
        chk("G11b cross-prime: Ore support pattern identical "
            "(same (a,fam,rho,d) bins)",
            a["ore_support_hash"] == b["ore_support_hash"])
        chk("G11c cross-prime: per-block defect profiles + e-index "
            "diagnostics identical on witness 0/draw 0",
            [(bl["delta_profile_N1..%d" % NMAX], bl["e_index_V"],
              bl["ell_window"]) for bl in a["blocks"]] ==
            [(bl["delta_profile_N1..%d" % NMAX], bl["e_index_V"],
              bl["ell_window"]) for bl in b["blocks"]], hard=False)
    bad = [n for n, c, h in GATES if h and not c]
    print("RESULT: %d/%d gates pass%s" % (
        sum(1 for _, c, _ in GATES if c), len(GATES),
        "" if not bad else "; HARD FAIL %s" % bad))
    print(BLOCKNOTE)
    return not bad

def run_all(primes, out_path, light=False):
    print("== VALUATION-E2 FULL RUN (%s) ==" % EXP)
    print("   " + BLOCKNOTE)
    t00 = time.time()
    results = []
    for p in primes:
        for widx, kdraw, wit72, deep in iter_points(p):
            tag = "p%d w%d k%d " % (p, widx, kdraw)
            res, E = run_point(p, wit72, deep, tag=tag, light=light,
                               quiet=True)
            ec = res["e_candidate"]
            print("%s: e_cand=%s (%s; %d consistent blocks) "
                  "delta5[min..max over blocks]=%s ell[max]=%s %s (%.0fs)"
                  % (tag.strip(), ec["value"], ec["argmin_stream"],
                     ec["n_consistent_blocks"],
                     [min(b["delta_profile_N1..%d" % NMAX][-1]
                          for b in res["blocks"]),
                      max(b["delta_profile_N1..%d" % NMAX][-1]
                          for b in res["blocks"])],
                     max(b["ell_window"] for b in res["blocks"]),
                     EXP, res["seconds"]), flush=True)
            slim = dict(res)
            results.append({"prime": p, "witness": widx,
                            "kernel_draw": kdraw, **slim})
    gate_fail = [n for n, c, h in GATES if h and not c]
    dist = collections.Counter(str(r["e_candidate"]["value"])
                               for r in results)
    n_le11 = sum(1 for r in results
                 if r["e_candidate"]["value"] is not None and
                 r["e_candidate"]["value"] <= 11)
    out = {
        "tool": "cases/valuation_e2.py",
        "object": ("Euler/Ore valuation-e operator per xmodel/sol-round5.md "
                   "sec 1 (mod-6 residue streams, 29x29 square block, "
                   "column mode tails, PIN42 pinned, dual-jet rebuild of "
                   "gm_jet2/jrows at DBUILD=42, deterministic zero "
                   "completion)"),
        "status": "INTERNAL / UNREVIEWED; " + EXP + " ONLY",
        "tag": EXP,
        "block_note": BLOCKNOTE,
        "depth_stab_note": ("DEPTH-STAB e <= 11 is the eventual criterion; "
                            "counts below are E_CANDIDATE counts, not "
                            "verdicts"),
        "primes": list(primes),
        "n_points": len(results),
        "gates_all_pass": not gate_fail,
        "gate_failures": gate_fail,
        "e_candidate_distribution": dict(dist),
        "n_e_candidates_le_11": n_le11,
        "spec_constants": {"streams": [["%s" % f, rho, r_start(rho)]
                                       for f, rho in STREAMS],
                           "s_a": S_A, "sum_s_a": sum(S_A),
                           "sum_r_c": 288, "DBUILD": DBUILD, "NMAX": NMAX},
        "deep_label_identification": {
            "note": ("MEASURED this run: the frozen core23 emission's "
                     "x74..x83 deep-tail labels (valuation_e.DEEPMAP, "
                     "documented there as conventional) map to the true "
                     "build_generators stream slots by this involution; "
                     "levels and W-side splits were already correct"),
            "emission_to_true": DEEP_RELABEL},
        "eta29_refutation_summary": {
            "claim_refuted": ("sol-round5.md sec 1.2 all-depth "
                              "cyclic-character lemma, the E_29 = 0 "
                              "clause"),
            "measurement": ("E_29 != 0: first occurrence t^36 (s_29 = "
                            "36), derivative support exactly the six "
                            "residue-4 streams' u^0 coefficients (level "
                            "48 = C7-invariant); value 0 at every banked "
                            "witness; entries constant across points "
                            "within a prime"),
            "char0_confirmation": ("r1_experiment + directionb_strike "
                                   "exact build, depth 37, all-zero-"
                                   "tails: eta^29 t^36 coefficient of "
                                   "tf1_48 = %d/%d, trivial radkey"
                                   % (ETA29_NUM, ETA29_DEN)),
            "consequence": ("the 29-output premise of the square-block "
                            "design fails beyond band 22: the operator "
                            "has 30 output streams (sum s_a = 276) "
                            "against 30 input streams (sum r_c = 288); "
                            "the spec-literal 29x29 blocks are computed "
                            "as commissioned with delta_plus_eta29 "
                            "augmented defects recorded per block")},
        "artifact_hashes": {os.path.basename(witness_file(p)):
                            V.sha256(witness_file(p)) for p in primes},
        "points": results,
        "seconds": round(time.time() - t00),
    }
    if out_path:
        with open(out_path, "w") as f:
            json.dump(out, f, indent=1, sort_keys=True)
        print("-> wrote %s" % out_path)
    print("distribution (%s): %s ; %d/%d points with e_cand <= 11"
          % (EXP, dict(dist), n_le11, len(results)))
    print(BLOCKNOTE)
    return out

# -------------------------------------------------------------- selftest
def selftest():
    p = 105337
    rng = np.random.default_rng(7)
    # conv identity: toep(v) @ w == truncated polymul
    v = rng.integers(0, p, _S).astype(np.float64)
    w = rng.integers(0, p, _S).astype(np.float64)
    c1 = np.mod(toep(v) @ w, p)
    c2 = np.mod(np.convolve(v, w)[:_S], p)
    assert np.array_equal(c1, c2), "toeplitz conv broken"
    # jmul against a naive reference on tiny random dual jets
    A = Jet(3, True)
    B = Jet(2, True)
    A.V = rng.integers(0, p, (3, _S)).astype(np.float64)
    B.V = rng.integers(0, p, (2, _S)).astype(np.float64)
    A.G = np.zeros((3, _S, GD))
    B.G = np.zeros((2, _S, GD))
    A.G[:, :, :4] = rng.integers(0, p, (3, _S, 4))
    B.G[:, :, :4] = rng.integers(0, p, (2, _S, 4))
    C = jmul(A, B, p)
    for h in range(C.h):
        for s in range(_S):
            vv = 0
            gg = np.zeros(GD)
            for ha in range(A.h):
                hb = h - ha
                if not (0 <= hb < B.h):
                    continue
                for sa in range(s + 1):
                    vv += A.V[ha][sa] * B.V[hb][s - sa]
                    gg = gg + A.V[ha][sa] * B.G[hb][s - sa] \
                        + B.V[hb][s - sa] * A.G[ha][sa]
            assert C.V[h][s] == vv % p
            assert np.array_equal(C.G[h][s], np.mod(gg, p))
        if h > 2:
            break
    # rank + coverage machinery
    M = np.array([[1, 0, 0], [0, 0, 0], [2, 3, 0]], dtype=np.int64)
    assert rankp(M.copy(), p) == 2
    cs = Colspace(3, p)
    cs.add(np.array([1, 0, 2], dtype=np.int64))
    cs.add(np.array([0, 0, 3], dtype=np.int64))
    cov = cs.covered_rows()
    assert list(cov) == [True, False, True]
    # dual-number derivative control: d/dc of (x + c t^r)^2 at c=c0 is
    # 2 t^r (x + c0 t^r) -- exercised through smul
    r = 5
    c0 = 1234
    x = rng.integers(0, p, _S).astype(np.float64)
    g = np.zeros((_S, GD))
    g[r][0] = 1
    xv = x.copy()
    xv[r] = (xv[r] + c0) % p
    sq = smul((xv, g), (xv, g), p)
    ref = np.mod(2 * toep(xv)[:, r], p)
    assert np.array_equal(sq[1][:, 0], ref), "dual derivative broken"
    print("PASS selftest: toeplitz conv, dual jmul vs naive, rankp, "
          "coverage, dual derivative")

def main():
    ap = argparse.ArgumentParser(description="corrected Euler/Ore "
                                 "valuation-e (E_CANDIDATE only)")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--gates", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--light", action="store_true",
                    help="skip per-point zeta2/path-A rebuilds on --run")
    ap.add_argument("--point", nargs=3, type=int, metavar=("P", "W", "K"))
    ap.add_argument("--prime", type=int, default=None)
    ap.add_argument("--out", default=os.path.join(HERE,
                                                  "d23_ecandidates.json"))
    args = ap.parse_args()
    primes = (args.prime,) if args.prime else PRIMES
    if args.selftest:
        selftest()
        return
    if args.gates:
        ok = run_gates(primes)
        sys.exit(0 if ok else 1)
    if args.point:
        p, widx, k = args.point
        for w, kd, wit72, deep in iter_points(p):
            if w == widx and kd == k:
                res, E = run_point(p, wit72, deep,
                                   tag="p%d w%d k%d " % (p, w, kd))
                print(json.dumps({k2: v for k2, v in res.items()
                                  if k2 != "blocks"}, indent=1,
                                 sort_keys=True, default=str))
                for b in res["blocks"]:
                    print(b["stream"], b["delta_profile_N1..%d" % NMAX],
                          "d_c", b["d_c_stabilized"], "e_idx",
                          b["e_index_V"], "ell", b["ell_window"],
                          "consistent", b["consistent_diagnostics"])
                return
        raise SystemExit("point not found")
    if args.run:
        run_all(primes, args.out, light=args.light)
        return
    ap.print_help()

if __name__ == "__main__":
    main()
