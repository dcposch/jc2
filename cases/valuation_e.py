#!/usr/bin/env python3
"""valuation_e.py -- verdict-day valuation-e pipeline for the D21/D23
residue-A window (DEPTH-STAB route B; SHEET6-DIRECTIONB 7.S3/7.S4/8.S/8.S2;
build split per xmodel/sol-software2.md item 1: 1a GO / 1b BLOCKED).

STATUS: INTERNAL TOOLING, UNREVIEWED.  No promotion claims.

SCOPE SPLIT (sol-software2.md item 1, adopted):
  1a POINT CERTIFICATE + RECONSTRUCTION (complete, hard-gated):
     msolve-GB parsing + artifact hashing, F_p point extraction with the
     7.S3 draw discipline, full D21 chart reconstruction (22 pivots
     back-solved), verification against the complete row22compat 54-row
     emission AND the 77-row D23 hybrid AND the pristine source rows,
     Row_22 deep-tail reconstruction (rank-4 solve + 6-dim kernel draws),
     machine-readable point certificates, and the 12-banked-point negative
     control (required result: NOT_IN_DOMAIN / compat failure 12/12).
  1b VALUATION e (EXPERIMENTAL ONLY, soft-gated, never promoted):
     ***EVERY e THIS TOOL PRINTS IS "E_CANDIDATE (EXPERIMENTAL)".***
     The DEPTH-STAB minor object is a SERIES-valued Jacobian; the scalar
     .ms Jacobian has no uniformizer (minors valuate 0/infinity only), and
     pivot/radical/Rabinowitsch rows carry unit derivatives that can
     manufacture a false e = 0.  The correctly specified input -- the
     original series-valued equation map, its SQUARE FUNCTION BLOCK, and
     the SURPLUS-EQUATION BRIDGE (exact proof that every surplus equation
     lies in the completed local ideal), plus the unit/t-shift
     normalization manifest -- is NOT YET BANKED anywhere
     (sol-software2.md "Required valuation-object manifest").  Until that
     manifest exists and its promotion gates pass, e <= 11 must NOT be
     reported as a LIVE verdict.  This tool therefore never prints LIVE:
     survivors get "E_CANDIDATE" lines plus the blocking prerequisite.

USAGE
  python3 cases/valuation_e.py --gates [--full] [--experimental-e]
      # hard gates = 1a only (exit 0 = 1a passes); --full adds the twin
      # primes' engine tier; --experimental-e appends the soft 1b tier
  python3 cases/valuation_e.py --report [--gb F.out] [--n 12] [--seed 2026]
      [--experimental-e] [--cert-dir DIR]     # verdict-day path
  python3 cases/valuation_e.py --selftest     # 1b arithmetic micro-checks

INPUTS (never runs msolve, never touches the fleet): banked fiber GBs
  directionb_core2_fiber_p105337.out / fiber_p105673.out / fiber_p200257.out
  (local copies; originals box01 ~/jc72108/), frozen emissions
  cases/directionb_{core2,core23,row22compat}_p*.ms, the banked D21 window
  pickle, and the fastelim CORE2 engine (cases/fastelim.py, ~4.5 min build
  per prime).  On verdict day pass the actual lane .out via --gb.

1a DESIGN
  * Parser handles the real msolve format (header + "[p1,\np2,...]:"),
    verified against all three ~10.5MB banked fiber GBs; artifact SHA256,
    variable order, monomial order, characteristic recorded in the
    certificate (solver version/command are not present in .out artifacts
    -- recorded as absent, supply lane metadata via --lane-note).
  * Sampling = the 7.S3/7.S4 discipline ported VERBATIM from
    cases/directionb_fiber_filter.py; seed 2026 at p105337 reproduces the
    banked 12-point file byte-for-byte (gate).  W^4 pins are parsed from
    the GB (W_i^2 + c*uW_i^2 rows).  FIELD LIMITATION (recorded in every
    certificate): only F_p-rational sampling is implemented; failure to
    find an F_p point is NOT emptiness (extension-field extraction is an
    open TODO per sol-software2 item 1.1 -- supply such points externally
    via a future --point-file once F_{p^d} arithmetic lands).  MEASURED
    LIVE INSTANCE: at p = 200257 the GB pins W1^4 = 50209, W2^4 = 51243
    are NOT 4th powers in F_p, so this chart has no F_p-rational point
    there at all -- the tool fail-closes with that diagnosis; verdict-day
    rational extraction runs at 105337/105673.
  * Reconstruction: aux frees at zeros + seeded draws, 22 pivots
    back-solved on the CORE2 engine (pivot rows assert-vanish), then the
    point is verified against (i) all 397 GB elements, (ii) the COMPLETE
    row22compat 54-row emission incl. saturations, (iii) all 76 raw no-log
    D21 window rows.  D23 survivors additionally get the Row_22 rank-4
    deep solve (must match the certified Schur rank 4), 6-dim kernel
    draws (e-dependence across draws is REPORTED, not assumed away), and
    verification of (iv) the 77-row hybrid incl. rad/sat rows and (v) the
    10 pristine Row_22 rows.  The 12 banked D21 points are NEGATIVE
    controls: the pipeline must return NOT_IN_DOMAIN for all 12 -- any e
    assigned to them means the wrong object was certified (gate).
  * Certificates: JSON, one per point, with chart data (prime, r3 branch,
    W-branch, radical values, h32), all reconstructed coordinates, pivot
    sequence, Schur/kernel choices, residual-tier results, artifact
    hashes.  Default --cert-dir: the session scratchpad (certificates are
    working artifacts until reviewed; nothing written outside cases/ or
    the scratchpad).

1b DESIGN (EXPERIMENTAL; see the BLOCK box above)
  t-grading MEASURED from the banked rows (not assumed): exact fit over
  all 43,574 monomial-radkey pairs gives w(tail lvl l) = l-32 (tf/tg/tg0/
  vf), l-12 (uf), w(W_i) = w(HW_i) = 5, w(A_i) = 0; every raw row
  Row_n[eta^a] is weight-n pure (rank 15, ZERO exceptions), and the ten
  pristine Row_22 rows are weight-22 pure, pinning the deep tails: six at
  level 54, four at level 49, the 49s split 2/2 by W1/W2 chart-unit
  cofactors.  (tf-vs-tg NAMING of the deep tails is label-only and not
  recoverable from the frozen artifacts; e under the implemented readings
  depends only on levels, so the naming ambiguity cannot move e.)
  MEASURED OBSTRUCTION matching sol-software2's spec gap: the partials
  dF_{(n,a)}/dc_{(b,l)} are AFFINE in the slot weight (Euler pencil
  M0 + w*M1, the (i-12)/(j-18) structure), so no per-family Toeplitz
  series matrix exists; readings implemented behind --reading:
    pencil   rows = the 29 eta-classes, columns = INDIVIDUAL variables,
             entry(a,v) = sum_n dF_{(n,a)}/dc_v t^(n-w(v)); e = truncated
             Smith valuation sum over F_p[t]/t^D, fail-closed when rank
             is short or when e is unstable under randomizing the
             beyond-window coefficients.  Reproduces the DS4/DS6a demo
             (e = 1) and the unit control (e = 0).  Closest prototype to
             the required series object, still NOT the banked spec (no
             square-block/surplus bridge) -- hence E_CANDIDATE only.
    weighted ungrouped graded reading (min over full-rank row subsets of
             sum(bands) - sum(col weights); matroid greedy).  Recorded
             for comparison; singular on the DS4 demo (known divergence).
    rank     the degenerate scalar reading (0 or infinity).  Recorded
             because sol-software2 names it as the wrong object.
  Only window rows (bands 6..22) enter the Jacobian -- never the rad/sat/
  Rabinowitsch or pivot-definition rows (false-unit guard).  W/A/radical
  rescales are t-adic units (measured invariance instrument V-W below);
  the M-fold t-ambiguity only rescales t by roots of unity and cannot
  move valuations; e is reported in chart-t units (t = x^(-1/42)), the
  same units as D, as 2e+1 <= D requires.

Wrong-object guards: B-frozen no-log W1W2 != 0 chart with PIN42 pinned
(pins are never perturbation columns); offsets are the MEASURED 32/12;
raw pristine rows only (the 38 compressed rows are Bareiss combinations,
graded-impure, and excluded from the graded object).  No git.
"""
import sys, os, re, time, json, random, hashlib, collections, argparse
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
SCRATCH = ("/private/tmp/claude-501/-Users-dc-code-math/"
           "e1e34384-b145-4ca9-819e-4d40ed280a1a/scratchpad")
SCRATCH_GB = os.path.join(SCRATCH, "fibergb")
PRIMES = (105337, 105673, 200257)
GBFILES = {
    105337: [os.path.join(SCRATCH_GB, "directionb_core2_fiber_p105337.out"),
             "/tmp/fiber_gb.out"],
    105673: [os.path.join(SCRATCH_GB, "fiber_p105673.out")],
    200257: [os.path.join(SCRATCH_GB, "fiber_p200257.out")],
}
BANKED_TXT = os.path.join(HERE, "directionb_fiber_gb_p105337.out.txt")
BANKED_PTS = os.path.join(HERE, "directionb_fiber_points_p105337.txt")
FREE = ['x53', 'x55', 'x58', 'x60', 'x62', 'x63', 'x65', 'x66', 'x68',
        'x70', 'x71', 'x72', 'x73']
BOUNDX = ['x47', 'x52', 'x54', 'x57', 'x59']
RADG = ("A1", "A2", "W1", "HW1", "W2", "HW2")
DEEPX = ["x%d" % i for i in range(74, 84)]
# 1b measured grading (see header); OFF default 32, uf = 12.
OFF = {'uf': 12}
RADW = {'A1': 0, 'A2': 0, 'W1': 5, 'HW1': 5, 'W2': 5, 'HW2': 5}
# Deep-tail map: levels + W-sides MEASURED (Row_22 weight purity);
# tf-vs-tg split is LABEL-ONLY (cannot move e under the 1b readings).
DEEPMAP = {"x74": "tf1_54", "x75": "tf2_54", "x76": "tg1_54",
           "x78": "tg2_54", "x80": "tg01_54", "x82": "tg02_54",
           "x79": "tf1_49", "x83": "tg1_49",   # W1-side cofactors
           "x77": "tf2_49", "x81": "tg2_49"}   # W2-side cofactors

EXP = "E_CANDIDATE(EXPERIMENTAL)"
BLOCKNOTE = ("1b BLOCKED FROM PROMOTION (sol-software2.md item 1): e is "
             "experimental until the series-valued equation map, its "
             "square function block, and the surplus-equation bridge are "
             "banked and their promotion gates pass; no LIVE verdict is "
             "printed by this tool.")

OK = []
def chk(name, cond, hard=True):
    OK.append((name, bool(cond), hard))
    print(("PASS " if cond else ("FAIL " if hard else "WARN ")) + name,
          flush=True)
    if hard and not cond:
        print("RESULT: VALUATION-E GATE FAILS at " + name)
        sys.exit(1)

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()

def fam_of(nm):
    return nm.split('_')[0] if '_' in nm else \
        ''.join(c for c in nm if not c.isdigit())

def lvl_of(nm):
    if '_' in nm:
        return int(nm.rsplit('_', 1)[1])
    return int(''.join(c for c in nm if c.isdigit()))

def w_of(nm):
    return lvl_of(nm) - OFF.get(fam_of(nm), 32)

# ------------------------------------------------------------ msolve parser
def parse_msolve_out(path):
    """Parse a real msolve GB .out (format of the banked fiber outputs:
    '#'-header lines, then '[poly,\npoly,...]:').  Returns (meta, gvars,
    polys) with polys = list of dicts exponent-tuple -> coeff mod p."""
    txt = open(path).read()
    ch = int(re.search(r'#field characteristic:\s*(\d+)', txt).group(1))
    gvars = [v.strip() for v in
             re.search(r'#variable order:\s*(.+)', txt).group(1).split(',')]
    mo = re.search(r'#monomial order:\s*(.+)', txt)
    nb = int(re.search(r'#length of basis:\s*(\d+)', txt).group(1))
    nv = len(gvars)
    vi = {v: i for i, v in enumerate(gvars)}
    body = txt.split('---')[-1].strip()
    assert body.startswith('[') and body.endswith(']:'), \
        "unexpected artifact tail (not a completed msolve GB print)"
    polys = []
    for s in body[1:-2].split(',\n'):
        d = {}
        for t in s.split('+'):
            fs = t.split('*')
            c = int(fs[0])
            e = [0] * nv
            for f in fs[1:]:
                m = re.match(r'([A-Za-z0-9_]+)\^(\d+)$', f)
                if m:
                    e[vi[m.group(1)]] += int(m.group(2))
                else:
                    e[vi[f]] += 1
            k = tuple(e)
            d[k] = (d.get(k, 0) + c) % ch
        polys.append({k: c for k, c in d.items() if c})
    assert len(polys) == nb, "basis count %d != stated %d" % (len(polys), nb)
    meta = {"path": os.path.abspath(path), "sha256": sha256(path),
            "characteristic": ch, "n_vars": nv, "n_basis": nb,
            "variable_order": gvars,
            "monomial_order": mo.group(1).strip() if mo else None,
            "solver_version": None, "solver_command": None,
            "note": "solver version/command absent from .out artifacts"}
    return meta, gvars, polys

def gb_w4_pins(p, gvars, polys):
    """Extract W_i^4 pins from GB rows of shape W_i^2 + c*uW_i^2."""
    vi = {v: i for i, v in enumerate(gvars)}
    pins = {}
    for d in polys:
        if len(d) != 2:
            continue
        for W, uW in (("W1", "uW1"), ("W2", "uW2")):
            kW = tuple(2 if i == vi[W] else 0 for i in range(len(gvars)))
            ku = tuple(2 if i == vi[uW] else 0 for i in range(len(gvars)))
            if set(d) == {kW, ku} and d[kW] == 1:
                pins[W] = (-d[ku]) % p     # W^4 = -c
    return pins

# --------------------------------------------------- 7.S3/7.S4 point sampler
def _ev(d, val, p):
    tot = 0
    for k, c in d.items():
        m = c
        for i, e in enumerate(k):
            if e:
                if val[i] is None:
                    return None
                m = m * pow(val[i], e, p) % p
        tot = (tot + m) % p
    return tot

def _subs(d, val, p):
    out = {}
    for k, c in d.items():
        m = c
        ke = [0] * len(k)
        for i, e in enumerate(k):
            if e:
                if val[i] is None:
                    ke[i] = e
                else:
                    m = m * pow(val[i], e, p) % p
        ke = tuple(ke)
        out[ke] = (out.get(ke, 0) + m) % p
    return {k: c for k, c in out.items() if c}

def _uniroots(d, i, p):
    cs = {}
    for k, c in d.items():
        cs[k[i]] = (cs.get(k[i], 0) + c) % p
    dg = max(cs)
    if dg == 0:
        return None
    if dg == 1:
        a, b = cs.get(1, 0), cs.get(0, 0)
        return [(-b) * pow(a, p - 2, p) % p]
    return [x for x in range(p)
            if sum(c * pow(x, e, p) for e, c in cs.items()) % p == 0]

def _r4(a, p):
    for x in range(2, p):
        if pow(x, 4, p) == a:
            return x
    return None

def sample_points(p, gvars, polys, want=12, seed=2026, maxtries=40):
    """The 7.S3 draw discipline, ported verbatim from
    directionb_fiber_filter.py (seed 2026 at p105337 reproduces the banked
    12 points exactly -- gate A2).  F_p-rational only: an empty return is
    NOT emptiness (extension fields not implemented; recorded in certs)."""
    nv = len(gvars)
    vi = {v: i for i, v in enumerate(gvars)}
    pins = gb_w4_pins(p, gvars, polys)
    if "W1" not in pins or "W2" not in pins:
        return [], 0, "W^4 pins not found in GB (unexpected shape)"
    w1r, w2r = _r4(pins["W1"], p), _r4(pins["W2"], p)
    if w1r is None or w2r is None:
        # The GB pins W_i^4 globally on the locus; if a pin is not a 4th
        # power in F_p the chart has NO F_p-rational point (W forced into
        # an extension).  Fail CLOSED with the honest diagnosis -- this is
        # NOT emptiness (sol-software2 item 1.1; F_{p^d} extraction TODO).
        missing = [W for W, r in (("W1", w1r), ("W2", w2r)) if r is None]
        return [], 0, ("W^4 pin(s) %s not 4th powers mod %d: locus "
                       "F_p-point-poor on this chart; extension-field "
                       "extraction required (not implemented)"
                       % (",".join(missing), p))
    ii = next(x for x in range(2, p) if x * x % p == p - 1)
    pts, tries = [], 0
    rng = random.Random(seed)
    while len(pts) < want and tries < maxtries:
        tries += 1
        val = [None] * nv
        for v in FREE:
            val[vi[v]] = rng.randrange(0, p)
        s1 = rng.choice([1, -1]); s2 = rng.choice([1, -1])
        i1 = rng.choice([0, 1]); i2 = rng.choice([0, 1])
        w1 = w1r * (ii if i1 else 1) * (s1 % p) % p
        w1 = w1 if s1 > 0 else (p - w1) % p
        w2 = w2r * (ii if i2 else 1) % p
        w2 = w2 if s2 > 0 else (p - w2) % p
        val[vi["W1"]] = w1; val[vi["W2"]] = w2
        val[vi["uW1"]] = pow(w1, p - 2, p)
        val[vi["uW2"]] = pow(w2, p - 2, p)
        unk = set(BOUNDX); progress = True; ok = True
        while unk and progress and ok:
            progress = False
            for d in polys:
                sd = _subs(d, val, p)
                if not sd:
                    continue
                sup = {i for k in sd for i, e in enumerate(k) if e}
                if not sup:
                    ok = False; break
                if len(sup) == 1:
                    i = next(iter(sup))
                    rs = _uniroots(sd, i, p)
                    if rs is None:
                        continue
                    if not rs:
                        ok = False; break
                    val[i] = rs[0]; unk.discard(gvars[i]); progress = True
            if not ok:
                break
        if not ok or unk:
            continue
        if all(_ev(d, val, p) == 0 for d in polys):
            pts.append(list(val))
    return pts, tries, None

# ------------------------------------------------------- engine + raw rows
_ENG = {}
def engine(p):
    """fastelim CORE2 engine (22 pivots, W-normalized); cached per prime."""
    if p not in _ENG:
        import fastelim as FE
        t0 = time.time()
        eng, resid, plog, strips, pt, census = FE.run_core2(p, verbose=False)
        print("   [p=%d] engine ready (%.0fs)" % (p, time.time() - t0),
              flush=True)
        _ENG[p] = (eng, resid, plog, strips, pt)
    return _ENG[p]

_RAW = None
def raw_rows21():
    """The 76 raw no-log D21 window rows ((band, eta) -> VExpr) + registry
    (banked pickle; restore /tmp copy from the repo root if aged out)."""
    global _RAW
    if _RAW is None:
        if not os.path.exists("/tmp/directionb_tails_D21.pkl"):
            import shutil
            src = os.path.join(HERE, "..", "directionb_tails_D21.pkl")
            shutil.copy(src, "/tmp/directionb_tails_D21.pkl")
        import directionb_compress as DC
        _RAW = DC.load_nolog_rows()
    return _RAW

def radical_env(p):
    import r1_fullcore as FC
    pt = FC.radical_point(p)
    h32 = pt["HW1"] * pow(pt["W1"], p - 2, p) % p
    return pt, pt["r3"], h32

_MSCACHE = {}
def parse_ms_rows(path, p):
    """Parse an emitted .ms (header line, char line, comma-joined rows).
    Cached (the compat/hybrid emissions are re-verified per point)."""
    if (path, p) in _MSCACHE:
        return _MSCACHE[(path, p)]
    lines = open(path).read().split('\n')
    hdr = [h.strip() for h in lines[0].split(',')]
    char = int(lines[1])
    assert char == p
    eqs = [e.strip() for e in "\n".join(lines[2:]).split(',\n') if e.strip()]
    out = []
    for e in eqs:
        d = {}
        for t in e.split('+'):
            fs = t.split('*')
            try:
                c = int(fs[0]); fs = fs[1:]
            except ValueError:
                c = 1                 # rad/sat rows print unit coefficients
            mono = {}
            for f in fs:
                m = re.match(r'([A-Za-z0-9_]+)\^(\d+)$', f)
                if m:
                    mono[m.group(1)] = mono.get(m.group(1), 0) + int(m.group(2))
                else:
                    mono[f] = mono.get(f, 0) + 1
            k = tuple(sorted(mono.items()))
            d[k] = (d.get(k, 0) + c) % p
        out.append({k: c for k, c in d.items() if c})
    _MSCACHE[(path, p)] = (hdr, out)
    return hdr, out

_R22 = {}
def row22_rows(p):
    """The 10 pristine Row_22 rows from the frozen D23-core emission,
    labels (22, eta), eta = 1,4,...,28 (emission order == sorted labs,
    verified against directionb_compress.load_nolog_rows ordering); deep
    x74..x83 renamed by the measured level/side map (label-only)."""
    if p in _R22:
        return _R22[p]
    import directionb_residual32_emit as E32
    rows21, vars_ = raw_rows21()
    _, names, _, _, _ = E32.load_rows()
    x2name = {names[vid]: vars_[vid] for vid in names}
    x2name.update(DEEPMAP)
    hdr, allrows = parse_ms_rows(
        os.path.join(HERE, "directionb_core23_p%d.ms" % p), p)
    r22 = [d for d in allrows[38:70]
           if any(nm in DEEPX for k in d for nm, _ in k)]
    assert len(r22) == 10
    out = []
    for a, d in zip(range(1, 29, 3), r22):
        nd = {}
        for k, c in d.items():
            nk = tuple(sorted((x2name.get(nm, nm), e) for nm, e in k))
            nd[nk] = (nd.get(nk, 0) + c) % p
        out.append(((22, a), {k: c for k, c in nd.items() if c}))
    _R22[p] = out
    return out

# --------------------------------------------- point assembly + back-solve
def full_point(p, fibval, gvars, draw=0, drawseed=777):
    """Reconstruct the FULL D21 chart point from a fiber point: aux frees
    at zeros (draw 0) or seeded random (draw >= 1), 22 pivots back-solved
    on the engine; asserts pivot rows vanish.  Returns dict name -> value
    (all engine-occurring vars + A1/A2/W1/W2/HW1/HW2)."""
    import directionb_residual32_emit as E32
    eng, resid, plog, strips, pt = engine(p)
    rows21, vars_ = raw_rows21()
    _, names, _, _, _ = E32.load_rows()
    name_of = {names[i]: i for i in names}
    vi = {v: i for i, v in enumerate(gvars)}
    dval = {}
    for j, gv in enumerate(gvars):
        if gv.startswith("x"):
            dval[vars_[name_of[gv]]] = fibval[j]
    W1v, W2v = fibval[vi["W1"]], fibval[vi["W2"]]
    _, r3, h32 = radical_env(p)
    FRNG = random.Random(drawseed + draw)
    occnames = {eng.vars_[vid] for vid in eng.occ}
    for nm in sorted(occnames):
        if nm in dval:
            continue
        lv = nm.rsplit("_", 1)[-1] if "_" in nm else ""
        if lv == "42":
            dval[nm] = 0                     # PIN42 (no-log pins)
        else:
            dval[nm] = FRNG.randrange(0, p) if draw else 0
    gval = [0] * (eng.nt + 6)
    for j, vid in enumerate(eng.occ):
        gval[j] = dval.get(eng.vars_[vid], 0)
    A1v, A2v = pt["A1"], pt["A2"]
    gval[eng.nt + 0] = A1v; gval[eng.nt + 1] = A2v
    gval[eng.nt + 2] = W1v; gval[eng.nt + 3] = h32 * W1v % p
    gval[eng.nt + 4] = W2v; gval[eng.nt + 5] = h32 * W2v % p
    pividx = [(gx, lab) for gx, lab, _ in plog]
    rowsP = {lab: eng.P[eng.labs.index(lab)] for _, lab in pividx}
    for gx, lab in reversed(pividx):
        P = rowsP[lab]; cp = P.derivative(gx)
        v0 = list(gval); v0[gx] = 0
        b = int(P(*v0)) % p; c = int(cp(*v0)) % p
        gval[gx] = (-b) * pow(c, p - 2, p) % p
    for j, vid in enumerate(eng.occ):
        dval[eng.vars_[vid]] = gval[j]
    assert all(int(rowsP[lab](*gval)) % p == 0 for _, lab in pividx), \
        "pivot rows nonzero after back-solve (wrong object!)"
    dval.update({"A1": A1v, "A2": A2v, "W1": W1v, "W2": W2v,
                 "HW1": h32 * W1v % p, "HW2": h32 * W2v % p})
    return dval

def eval_ms_row(d, xval, p):
    tot = 0
    for k, c in d.items():
        m = c
        for nm, e in k:
            m = m * pow(xval[nm], e, p) % p
        tot = (tot + m) % p
    return tot

def _xval_from_point(p, dval):
    """x-registry + radical/saturation valuation of a chart point, for
    evaluating the frozen emissions."""
    import directionb_residual32_emit as E32
    rows21, vars_ = raw_rows21()
    _, names, _, _, _ = E32.load_rows()
    xval = {names[vid]: dval[vars_[vid]] for vid in names
            if vars_[vid] in dval}
    name2deep = {v: k for k, v in DEEPMAP.items()}
    for nm, xv in name2deep.items():
        if nm in dval:
            xval[xv] = dval[nm]
    for nm in ("A1", "A2", "W1", "W2", "HW1", "HW2"):
        xval[nm] = dval[nm]
    xval["uW1"] = pow(dval["W1"], p - 2, p)
    xval["uW2"] = pow(dval["W2"], p - 2, p)
    xval["uA"] = pow((dval["A1"] - dval["A2"]) % p, p - 2, p)
    return xval

def verify_row22compat(p, dval):
    """1a tier (ii): the point against the COMPLETE row22compat emission
    (24 fiber-core + 22 pivot + 6 compat + 2 uW = 54 rows).  The 46 core/
    pivot rows + 2 saturations MUST vanish at any reconstructed D21 point;
    the 6 compat rows are the D23 domain test (nonzero <=> NOT_IN_DOMAIN).
    Returns (n_zero_membership, 48, compat_vals[6])."""
    hdr, allrows = parse_ms_rows(
        os.path.join(HERE, "directionb_row22compat_p%d.ms" % p), p)
    assert len(allrows) == 54
    xval = _xval_from_point(p, dval)
    vals = [eval_ms_row(d, xval, p) for d in allrows]
    member = vals[:46] + vals[52:]
    return sum(1 for v in member if v == 0), len(member), vals[46:52]

def verify_core23(p, dval):
    """1a tier (iv): a D23-extended point against the 77-row hybrid
    (38 compressed + 22 pivot + 10 Row_22 + 7 rad/sat)."""
    hdr, allrows = parse_ms_rows(
        os.path.join(HERE, "directionb_core23_p%d.ms" % p), p)
    assert len(allrows) == 77
    xval = _xval_from_point(p, dval)
    vals = [eval_ms_row(d, xval, p) for d in allrows]
    return sum(1 for v in vals if v == 0), len(vals)

# ---------------------------------------------------- partials of raw rows
def vexpr_value_and_partials(v, vars_, dval, p, r3, pt, h32, wscale=None):
    """One raw VExpr row: (value, {name: dF/dname}, {W_i: dF/dW_i}).
    Radkeys (z,e1,e2,pw,h1,qw,h2,B): z = B = 0 on tail rows (asserted);
    HW_i folds to h32*W_i on the branch.  wscale = optional (r1, r2)
    W-unit row rescale (the AMB-W instrument)."""
    import r1_fullcore as FC
    W1v, W2v = dval["W1"], dval["W2"]
    val = 0
    acc = collections.defaultdict(int)
    accW = {"W1": 0, "W2": 0}
    s1, s2 = (wscale or (0, 0))
    for vk, r in v.items():
        cW1 = cW2 = cv = 0
        for rk, c in r.items():
            z, e1, e2, pw, h1, qw, h2, B = rk
            assert z == 0 and B == 0, "non-tail radkey on window row"
            x = (FC.frmod(c[0], p) + FC.frmod(c[1], p) * r3) % p
            x = x * pow(pt["A1"], e1, p) % p * pow(pt["A2"], e2, p) % p
            x = x * pow(h32, h1 + h2, p) % p
            m1, m2 = pw + h1 + s1, qw + h2 + s2
            x = x * pow(W1v, m1, p) % p * pow(W2v, m2, p) % p
            cv = (cv + x) % p
            cW1 = (cW1 + x * m1) % p
            cW2 = (cW2 + x * m2) % p
        if not (cv or cW1 or cW2):
            continue
        cnt = collections.Counter(vk)
        mono = 1
        for v2, m2 in cnt.items():
            mono = mono * pow(dval[vars_[v2]], m2, p) % p
        val = (val + cv * mono) % p
        accW["W1"] = (accW["W1"] + cW1 * mono % p * pow(W1v, p - 2, p)) % p
        accW["W2"] = (accW["W2"] + cW2 * mono % p * pow(W2v, p - 2, p)) % p
        for vid, m in cnt.items():
            pr = cv * m % p
            for v2, m2 in cnt.items():
                e = m2 - (1 if v2 == vid else 0)
                if e:
                    pr = pr * pow(dval[vars_[v2]], e, p) % p
            acc[vars_[vid]] = (acc[vars_[vid]] + pr) % p
    return val, {k: c for k, c in acc.items() if c}, \
        {k: c for k, c in accW.items() if c}

def msrow_value_and_partials(d, dval, p, pt, h32, wscale=None):
    """Same for a parsed name-keyed pristine row (Row_22)."""
    W1v, W2v = dval["W1"], dval["W2"]
    s1, s2 = (wscale or (0, 0))
    val = 0
    acc = collections.defaultdict(int)
    accW = {"W1": 0, "W2": 0}
    for k, c in d.items():
        v = c
        wpow = {"W1": s1, "W2": s2}
        tails = []
        for nm, e in k:
            if nm == "A1":
                v = v * pow(pt["A1"], e, p) % p
            elif nm == "A2":
                v = v * pow(pt["A2"], e, p) % p
            elif nm == "HW1":
                v = v * pow(h32, e, p) % p; wpow["W1"] += e
            elif nm == "HW2":
                v = v * pow(h32, e, p) % p; wpow["W2"] += e
            elif nm in ("W1", "W2"):
                wpow[nm] += e
            elif nm in ("uW1", "uW2", "uA"):
                raise AssertionError("saturation var on a pristine row")
            else:
                tails.append((nm, e))
        v = v * pow(W1v, wpow["W1"], p) % p * pow(W2v, wpow["W2"], p) % p
        mono = 1
        for nm, e in tails:
            mono = mono * pow(dval[nm], e, p) % p
        val = (val + v * mono) % p
        for W, Wv in (("W1", W1v), ("W2", W2v)):
            if wpow[W]:
                accW[W] = (accW[W] + v * wpow[W] % p * mono % p *
                           pow(Wv, p - 2, p)) % p
        for nm, e in tails:
            pr = v * e % p
            for nm2, e2 in tails:
                ee = e2 - (1 if nm2 == nm else 0)
                if ee:
                    pr = pr * pow(dval[nm2], ee, p) % p
            acc[nm] = (acc[nm] + pr) % p
    return val, {k: c for k, c in acc.items() if c}, \
        {k: c for k, c in accW.items() if c}

def window_partials(p, dval, D, wscales=None):
    """All WINDOW-row partials at the point (bands 6..20; + Row_22 for
    D >= 23).  Never includes rad/sat/pivot-definition rows (false-unit
    guard).  rowdata[(band, eta)] = (value, partials, Wpartials)."""
    rows21, vars_ = raw_rows21()
    pt, r3, h32 = radical_env(p)
    out = {}
    for lab, v in rows21:
        ws = (wscales or {}).get(lab)
        out[lab] = vexpr_value_and_partials(v, vars_, dval, p, r3, pt, h32,
                                            wscale=ws)
    if D >= 23:
        for lab, d in row22_rows(p):
            ws = (wscales or {}).get(lab)
            out[lab] = msrow_value_and_partials(d, dval, p, pt, h32,
                                                wscale=ws)
    return out

# ------------------------------------------ 1b (EXPERIMENTAL) e machinery
def series_mul(a, b, N, p):
    out = [0] * N
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj and i + j < N:
                    out[i + j] = (out[i + j] + ai * bj) % p
    return out

def series_val(a):
    for i, c in enumerate(a):
        if c:
            return i
    return None

def matrix_smith(M, N, p, maxrank=None):
    """t-adic elimination on rows x cols of length-N coefficient lists over
    F_p[t]/t^N; returns (rank, [pivot valuations]).  Truncated Smith /
    rank-profile in the sense of sol-software2 (but on the EXPERIMENTAL
    pencil object, not the not-yet-banked square block)."""
    M = [[col[:] for col in row] for row in M]
    R, C = len(M), len(M[0]) if M else 0
    if maxrank is None:
        maxrank = min(R, C)
    vals = []
    usedr, usedc = set(), set()
    for _ in range(maxrank):
        best = None
        for i in range(R):
            if i in usedr:
                continue
            for j in range(C):
                if j in usedc:
                    continue
                v = series_val(M[i][j])
                if v is not None and (best is None or v < best[0]):
                    best = (v, i, j)
        if best is None:
            break
        v0, pi, pj = best
        vals.append(v0)
        usedr.add(pi); usedc.add(pj)
        piv = M[pi][pj]
        lead = pow(piv[v0], p - 2, p)
        for i in range(R):
            if i in usedr or series_val(M[i][pj]) is None:
                continue
            tv = M[i][pj]
            q = [0] * N
            for m in range(N - v0):
                cm = tv[m + v0] if m + v0 < N else 0
                qm = cm * lead % p
                if qm:
                    q[m] = qm
                    for jj in range(N - m - v0):
                        tv[m + v0 + jj] = (tv[m + v0 + jj]
                                           - qm * piv[v0 + jj]) % p
            for j in range(C):
                if j == pj:
                    M[i][j] = [0] * N
                    continue
                M[i][j] = [(a - b) % p for a, b in
                           zip(M[i][j], series_mul(q, M[pi][j], N, p))]
    return len(vals), vals

def build_pencil(p, rowdata, D, cols_mode="tails", unk_fill=0,
                 fillseed=4242):
    """EXPERIMENTAL pencil matrix: 29 eta-class rows x per-variable
    columns; entry(a, v)[m] = dF_{(m + w(v), a)}/dc_v.  Coefficients
    beyond a column's window cap (m > D-1-w(v)) are UNKNOWN: 0 or seeded
    random for the stability check."""
    N = D
    classes = sorted({a for (n, a) in rowdata})
    colnames = sorted({nm for lab, (val, pr, prW) in rowdata.items()
                       for nm in pr})
    if cols_mode == "tailsW":
        colnames += ["W1", "W2"]
    rng = random.Random(fillseed)
    M = []
    for a in classes:
        row = []
        for nm in colnames:
            w = 5 if nm in ("W1", "W2") else w_of(nm)
            ser = [0] * N
            cap = D - 1 - w
            for m in range(N):
                n = m + w
                if (n, a) in rowdata:
                    val, pr, prW = rowdata[(n, a)]
                    ser[m] = (prW.get(nm, 0) if nm in ("W1", "W2")
                              else pr.get(nm, 0))
                if m > cap and unk_fill:
                    ser[m] = rng.randrange(0, p)
            row.append(ser)
        M.append(row)
    return M, classes, colnames

def e_pencil(p, rowdata, D, cols_mode="tails"):
    """EXPERIMENTAL e under the pencil reading, with the fail-closed
    stability check (unknown-beyond-window coefficients at 0 AND at two
    random fills; certified-at-window-depth only if all agree)."""
    res = []
    shape = None
    for fill in (0, 1, 2):
        M, classes, cols = build_pencil(p, rowdata, D, cols_mode,
                                        unk_fill=(1 if fill else 0),
                                        fillseed=4242 + fill)
        shape = (len(M), len(M[0]))
        maxrank = min(shape)
        rk, vals = matrix_smith(M, D, p, maxrank=maxrank)
        res.append((rk, sum(vals) if rk == maxrank else None, vals))
    (rk0, e0, v0) = res[0]
    stable = all(r[0] == rk0 and r[1] == e0 for r in res)
    if rk0 < min(shape):
        return None, {"why": "rank %d < %d at window depth "
                      "(fail-closed)" % (rk0, min(shape)), "vals": v0,
                      "stable": stable, "shape": shape}
    if not stable:
        return None, {"why": "e unstable under unknown-tail fill "
                      "(window depth insufficient, fail-closed)",
                      "vals": v0, "stable": False, "shape": shape}
    return e0, {"vals": v0, "stable": True, "rank": rk0, "shape": shape}

def e_weighted(p, rowdata, D, cols_mode="tails"):
    """EXPERIMENTAL ungrouped graded reading (matroid greedy)."""
    labs = sorted(rowdata)
    colnames = sorted({nm for lab in labs for nm in rowdata[lab][1]})
    if cols_mode == "tailsW":
        colnames += ["W1", "W2"]
    C = len(colnames)
    rows = []
    for (n, a) in labs:
        val, pr, prW = rowdata[(n, a)]
        vec = [(prW.get(nm, 0) if nm in ("W1", "W2") else pr.get(nm, 0))
               for nm in colnames]
        rows.append((n, vec))
    rows.sort(key=lambda t: t[0])
    basis = []
    wsum = 0; got = 0
    for n, vec in rows:
        v = vec[:]
        for li, bv in basis:
            if v[li]:
                f = v[li]
                v = [(a - f * b) % p for a, b in zip(v, bv)]
        li = next((i for i, x in enumerate(v) if x), None)
        if li is None:
            continue
        iv = pow(v[li], p - 2, p)
        v = [x * iv % p for x in v]
        basis.append((li, v))
        wsum += n; got += 1
        if got == C:
            break
    colw = sum(5 if nm in ("W1", "W2") else w_of(nm) for nm in colnames)
    if got < C:
        return None, {"why": "column rank %d < %d: no nonvanishing "
                      "maximal minor (fail-closed)" % (got, C)}
    return wsum - colw, {"rowsum": wsum, "colsum": colw, "ncols": C}

def e_rank(p, rowdata, D, cols_mode="tails"):
    """The degenerate scalar reading (recorded as the named WRONG object:
    sol-software2 -- minors valuate 0/infinity only)."""
    ew, det = e_weighted(p, rowdata, D, cols_mode)
    return (0 if ew is not None else None), det

READINGS = {"pencil": e_pencil, "weighted": e_weighted, "rank": e_rank}

# ------------------------------------------------ D23 extension (survivors)
def compat_c_values(p, dval):
    """The six 8.S2 compatibility rows c = L b at a D21 point (from the
    frozen row22compat emission).  Survivor <=> all six vanish."""
    nz, nr, cvals = verify_row22compat(p, dval)
    return cvals

def solve_deep(p, dval, draw=0, drawseed=555):
    """Row_22 affine system A y = -b on the ten deep tails at a D21 point;
    rank must equal the certified Schur rank 4.  Returns (extended point,
    rank) or (None, rank) when inconsistent (NOT_IN_DOMAIN)."""
    pt, r3, h32 = radical_env(p)
    deepn = [DEEPMAP[x] for x in DEEPX]
    dv = dict(dval)
    for nm in deepn:
        dv[nm] = 0
    rows = row22_rows(p)
    A = []; b = []
    for lab, d in rows:
        val0, pr, _ = msrow_value_and_partials(d, dv, p, pt, h32)
        A.append([pr.get(nm, 0) for nm in deepn])
        b.append((-val0) % p)
    M = [r[:] + [bb] for r, bb in zip(A, b)]
    rk = 0
    pivcols = []
    for cidx in range(10):
        prw = next((i for i in range(rk, 10) if M[i][cidx]), None)
        if prw is None:
            continue
        M[rk], M[prw] = M[prw], M[rk]
        iv = pow(M[rk][cidx], p - 2, p)
        M[rk] = [x * iv % p for x in M[rk]]
        for i in range(10):
            if i != rk and M[i][cidx]:
                f = M[i][cidx]
                M[i] = [(a - f * bb) % p for a, bb in zip(M[i], M[rk])]
        pivcols.append(cidx); rk += 1
    for i in range(rk, 10):
        if M[i][10]:
            return None, rk          # inconsistent: NOT_IN_DOMAIN at D23
    rng = random.Random(drawseed + draw)
    sol = [0] * 10
    for j in range(10):
        if j not in pivcols:
            sol[j] = rng.randrange(0, p) if draw else 0
    for i, cidx in enumerate(pivcols):
        sol[cidx] = (M[i][10] - sum(M[i][j] * sol[j] % p
                                    for j in range(10)
                                    if j != cidx and M[i][j])) % p
    out = dict(dval)
    for nm, v in zip(deepn, sol):
        out[nm] = v
    for lab, d in rows:
        val0, _, _ = msrow_value_and_partials(d, out, p, pt, h32)
        assert val0 == 0, "Row_22 nonzero after deep solve"
    return out, rk

# ----------------------------------------------------- 1a point certificate
def point_certificate(p, gbmeta, gvars, fibval, idx, draw, seed,
                      cert_dir=None, experimental_e=False,
                      cols_mode="tails", lane_note=None):
    """The 1a deliverable: reconstruct, verify every tier, emit JSON.
    Verdict field: NOT_IN_DOMAIN (compat failure: no D23 object exists
    over this point) or D23_POINT (fully reconstructed + verified).
    e-fields appear ONLY under experimental_e and ONLY tagged
    E_CANDIDATE(EXPERIMENTAL) with the 1b block note."""
    pt, r3, h32 = radical_env(p)
    dval = full_point(p, fibval, gvars, draw=draw)
    # tier (i): the GB itself
    # (sampler asserted this; recompute residual count for the record)
    cert = {
        "tool": "cases/valuation_e.py", "tier": "1a point certificate",
        "status": "INTERNAL TOOLING, UNREVIEWED",
        "field": "F_p (extension-field extraction not implemented; "
                 "no-point != emptiness)",
        "prime": p, "point_index": idx, "aux_draw": draw,
        "sampler_seed": seed,
        "chart": {"stratum": "residue-A B-frozen no-log W1W2!=0, PIN42",
                  "uniformizer": "t = x^(-1/42) (chart-t units)",
                  "r3": r3, "A1": pt["A1"], "A2": pt["A2"],
                  "W1": dval["W1"], "W2": dval["W2"], "h32": h32,
                  "W_branch": "4th-root branch as drawn (recorded via "
                              "W1/W2 values)"},
        "gb_artifact": gbmeta, "lane_note": lane_note,
        "fiber_coordinates": dict(zip(gvars, fibval)),
        "pivot_sequence": [[nm, list(lab)] for nm, lab in PIV22_SEQ()],
        "deep_map_note": "levels/W-sides measured; tf-vs-tg labels "
                         "conventional (cannot move e under the "
                         "experimental readings)",
    }
    rows_files = {}
    for fn in ("directionb_row22compat_p%d.ms" % p,
               "directionb_core23_p%d.ms" % p,
               "directionb_core2_fiber_p%d.ms" % p):
        fp = os.path.join(HERE, fn)
        if os.path.exists(fp):
            rows_files[fn] = sha256(fp)
    cert["row_file_hashes"] = rows_files
    # tier (ii): complete row22compat emission
    nz, nr, cvals = verify_row22compat(p, dval)
    cert["row22compat_zero_rows"] = [nz, nr]
    cert["compat_c_values"] = cvals
    # tier (iii): raw D21 window rows
    rowdata21 = window_partials(p, dval, 21)
    raw_nz = [list(lab) for lab, (v, _, _) in rowdata21.items() if v]
    cert["raw_D21_rows_vanish"] = not raw_nz
    assert not raw_nz, "raw D21 rows nonzero at reconstructed point"
    assert nz == nr, "row22compat rows nonzero at reconstructed point"
    if any(cvals):
        cert["verdict"] = "NOT_IN_DOMAIN"
        cert["verdict_detail"] = ("Row_22 compatibility failure: no D23 "
                                  "extension exists over this D21 point")
    else:
        ext, rk = solve_deep(p, dval, draw=draw)
        assert ext is not None and rk == 4, \
            "compat rows vanish but deep solve rank %d != 4" % rk
        dval = ext
        cert["schur_rank"] = rk
        cert["kernel_draw"] = draw
        nz23, nr23 = verify_core23(p, dval)
        assert nz23 == nr23, "77-row hybrid nonzero at extended point"
        cert["core23_zero_rows"] = [nz23, nr23]
        pr22 = window_partials(p, dval, 23)
        r22nz = [list(lab) for lab, (v, _, _) in pr22.items()
                 if lab[0] == 22 and v]
        cert["pristine_row22_vanish"] = not r22nz
        assert not r22nz
        cert["verdict"] = "D23_POINT"
    cert["coordinates"] = {nm: v for nm, v in sorted(dval.items())}
    if experimental_e and cert["verdict"] == "D23_POINT":
        rowdata = window_partials(p, dval, 23)
        evals = {}
        for rname, fn in READINGS.items():
            e, det = fn(p, rowdata, 23, cols_mode)
            evals[rname] = {"e": e, "detail": {k: v for k, v in
                                               det.items() if k != "vals"}}
        cert["e_experimental"] = {
            "tag": EXP, "block_note": BLOCKNOTE, "readings": evals,
            "decision_if_promoted": None if evals["pencil"]["e"] is None
            else ("would be 2e+1 = %d <= 23 test; NOT claimed" %
                  (2 * evals["pencil"]["e"] + 1))}
    if cert_dir:
        os.makedirs(cert_dir, exist_ok=True)
        fn = os.path.join(cert_dir, "point_p%d_i%d_d%d.json" %
                          (p, idx, draw))
        with open(fn, "w") as f:
            json.dump(cert, f, indent=1, sort_keys=True)
        cert["_written"] = fn
    return cert, dval

def PIV22_SEQ():
    return [("tf1_44", (12, 2)), ("tf2_44", (12, 5)), ("tf1_46", (14, 0)),
            ("tf2_46", (14, 3)), ("tf1_43", (16, 1)), ("tf1_48", (16, 4)),
            ("tf2_43", (16, 7)), ("tf2_48", (16, 10)), ("tf1_45", (18, 2)),
            ("tf1_50", (18, 5)), ("tf2_45", (18, 8)), ("tf2_50", (18, 11)),
            ("tf1_47", (20, 0)), ("tf1_52", (20, 3)), ("tf2_47", (20, 6)),
            ("tf2_52", (20, 9)), ("tf1_38", (6, 2)), ("tf1_40", (8, 0)),
            ("tf2_40", (8, 3)), ("tf1_39", (12, 8)), ("tf1_41", (14, 6)),
            ("tf2_41", (14, 9))]

# ----------------------------------------------------------- 1b diagnostics
def demo_pipeline(p=105337):
    """DS4/DS6a micro-regression THROUGH the pencil code path: the banked
    demo F = x^2 - t^2(1+t) at s = t must give e = 1; a unit row e = 0."""
    global OFF
    rowdata = {(0, 0): (0, {"d_0": 0}, {}),
               (1, 0): (0, {"d_0": 2, "d_1": 0}, {}),
               (2, 0): (0, {"d_0": 0, "d_1": 2, "d_2": 0}, {})}
    OFF = dict(OFF); OFF["d"] = 0
    e1, det1 = e_pencil(p, rowdata, 3)
    e0, det0 = e_pencil(p, {(0, 0): (0, {"d_0": 1}, {})}, 1)
    del OFF["d"]
    return e1, e0

def grading_fit():
    """The exact grading fit over the banked D21 rows (measured 1b input;
    also a 1a structural regression on the banked pickle)."""
    rows21, vars_ = raw_rows21()
    FAMS = ['uf', 'vf1', 'vf2', 'tf1', 'tf2', 'tg1', 'tg2', 'tg01', 'tg02']
    rowsM, rhs = [], []
    for (k, n), v in rows21:
        for vk, r in v.items():
            if not vk:
                continue                      # the +42 constant
            fc = collections.Counter(fam_of(vars_[i]) for i in vk)
            L = sum(lvl_of(vars_[i]) for i in vk)
            for radk in r:
                z, e1, e2, pw, h1, qw, h2, B = radk
                rowsM.append([-fc.get(f, 0) for f in FAMS] +
                             [e1, e2, pw, h1, qw, h2])
                rhs.append(k - L)
    M = [[Fr(x) for x in row] + [Fr(b)] for row, b in zip(rowsM, rhs)]
    ncol = 15
    r = 0; piv = []
    for c in range(ncol):
        pr = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        pv = M[r][c]; M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
    bad = sum(1 for i in range(r, len(M))
              if all(x == 0 for x in M[i][:ncol]) and M[i][ncol] != 0)
    names = ['OFF_' + f for f in FAMS] + \
        ['w_A1', 'w_A2', 'w_W1', 'w_HW1', 'w_W2', 'w_HW2']
    sol = {names[piv[i]]: M[i][ncol] for i in range(r)}
    return sol, bad, len(rowsM)

def euler_pencil_check(p):
    """The AMB instrument that matches sol-software2's spec gap: family
    bins are AFFINE in slot weight (Euler pencil), so no naive per-family
    series matrix exists -- the square-block spec is genuinely required."""
    rows21, vars_ = raw_rows21()
    pt, r3, h32 = radical_env(p)
    rng = random.Random(99)
    dval = {nm: rng.randrange(0, p) for nm in vars_}
    dval.update({"A1": pt["A1"], "A2": pt["A2"], "W1": pt["W1"],
                 "W2": pt["W2"], "HW1": pt["HW1"], "HW2": pt["HW2"]})
    rowdata = {lab: vexpr_value_and_partials(v, vars_, dval, p, r3, pt,
                                             h32) for lab, v in rows21}
    bins = collections.defaultdict(dict)
    for (n, a), (val, pr, prW) in rowdata.items():
        for nm, c in pr.items():
            bins[(a, fam_of(nm), n - w_of(nm))][w_of(nm)] = c
    n3 = naff = 0
    for key, entr in bins.items():
        if len(entr) >= 3:
            n3 += 1
            ws = sorted(entr)
            c0, c1, c2 = entr[ws[0]], entr[ws[1]], entr[ws[2]]
            lhs = (c1 - c0) * pow(ws[1] - ws[0], p - 2, p) % p
            rhs = (c2 - c1) * pow(ws[2] - ws[1], p - 2, p) % p
            naff += (lhs == rhs)
    return n3, naff

def synthetic_deep_solver_control(p):
    """Mechanics control for solve_deep on a SYNTHETIC consistent system:
    replace b by A*y0 (random y0) at a banked point, so the affine solve
    must succeed at rank 4 and reproduce a solution.  (No genuine D23
    survivor exists in the banked data -- 12/12 die -- so the success
    path gets a synthetic-only test, clearly labeled.)"""
    pt, r3, h32 = radical_env(p)
    deepn = [DEEPMAP[x] for x in DEEPX]
    rows = row22_rows(p)
    rng = random.Random(7)
    dv = {nm: rng.randrange(0, p) for nm in
          {n for _, d in rows for k, _ in [(0, 0)] for n, _ in []}}
    # build A at a random chart valuation (values only enter A's cofactors)
    rows21, vars_ = raw_rows21()
    dv = {nm: rng.randrange(0, p) for nm in vars_}
    dv.update({"A1": pt["A1"], "A2": pt["A2"], "W1": pt["W1"],
               "W2": pt["W2"], "HW1": pt["HW1"], "HW2": pt["HW2"]})
    for nm in deepn:
        dv[nm] = 0
    A = []
    for lab, d in rows:
        _, pr, _ = msrow_value_and_partials(d, dv, p, pt, h32)
        A.append([pr.get(nm, 0) for nm in deepn])
    y0 = [rng.randrange(0, p) for _ in range(10)]
    rhs = [sum(A[i][j] * y0[j] for j in range(10)) % p for i in range(10)]
    # rank of A must be 4 (Schur); A y = A y0 must be solvable
    M = [A[i][:] + [rhs[i]] for i in range(10)]
    rk = 0
    for cidx in range(10):
        prw = next((i for i in range(rk, 10) if M[i][cidx]), None)
        if prw is None:
            continue
        M[rk], M[prw] = M[prw], M[rk]
        iv = pow(M[rk][cidx], p - 2, p)
        M[rk] = [x * iv % p for x in M[rk]]
        for i in range(10):
            if i != rk and M[i][cidx]:
                f = M[i][cidx]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[rk])]
        rk += 1
    incons = any(M[i][10] for i in range(rk, 10))
    return rk, not incons

# =============================================================== gate suite
def run_gates(full=False, experimental_e=False, cols_mode="tails"):
    t00 = time.time()
    print("== VALUATION-E GATE SUITE ==")
    print("   hard gates = 1a (extraction/reconstruction/certificates);")
    print("   " + BLOCKNOTE)
    # ---------------- A: parser + artifact tier (all three primes)
    GB = {}
    for p in PRIMES:
        path = next((f for f in GBFILES[p] if os.path.exists(f)), None)
        chk("A1-p%d GB artifact present (%s)" % (p, path and
            os.path.basename(path)), path is not None)
        meta, gvars, polys = parse_msolve_out(path)
        GB[p] = (meta, gvars, polys)
        chk("A1-p%d parse: char OK, 397 elements, 22 vars, grevlex header,"
            " sha256 recorded" % p,
            meta["characteristic"] == p and len(polys) == 397 and
            len(gvars) == 22 and "reverse lexicographical"
            in (meta["monomial_order"] or ""))
        pins = gb_w4_pins(p, gvars, polys)
        chk("A1-p%d W^4 pins parsed from GB: W1^4=%d W2^4=%d" %
            (p, pins.get("W1", -1), pins.get("W2", -1)),
            "W1" in pins and "W2" in pins)
        if p == 105337:
            chk("A1 banked p105337 pins == 7.S4 record (57673, 53212)",
                pins == {"W1": 57673, "W2": 53212})
    if os.path.exists(BANKED_TXT):
        same = open(BANKED_TXT).read() == open(
            next(f for f in GBFILES[105337] if os.path.exists(f))).read()
        chk("A1 banked cases/ GB copy byte-identical to box01 artifact",
            same)
    # ---------------- A2: sampler regression
    meta, gvars, polys = GB[105337]
    pts, tries, diag = sample_points(105337, gvars, polys, 12, 2026)
    bank = [tuple(int(x) for x in l.strip().split(","))
            for l in open(BANKED_PTS) if l.strip() and not l.startswith('#')]
    chk("A2 sampler: 12/12 points in %d tries; seed-2026 replay == the "
        "banked point file exactly" % tries,
        len(pts) == 12 and [tuple(v) for v in pts] == bank)
    chk("A2 all 12 points vanish on all 397 GB elements",
        all(_ev(d, v, 105337) == 0 for v in pts for d in polys))
    # ---------------- A3: structural regressions on the frozen artifacts
    sol, bad, neq = grading_fit()
    want = {'OFF_uf': 12, 'OFF_vf1': 32, 'OFF_vf2': 32, 'OFF_tf1': 32,
            'OFF_tf2': 32, 'OFF_tg1': 32, 'OFF_tg2': 32, 'OFF_tg01': 32,
            'OFF_tg02': 32, 'w_A1': 0, 'w_A2': 0, 'w_W1': 5, 'w_HW1': 5,
            'w_W2': 5, 'w_HW2': 5}
    chk("A3 t-grading measured: %d monomial-eqs, 0 violations, offsets "
        "32/12, W-weight 5, A-weight 0 (unique fit)" % neq,
        bad == 0 and {k: int(v) for k, v in sol.items()} == want)
    for p in (PRIMES if full else (105337,)):
        rows = row22_rows(p)
        okp = len(rows) == 10
        for (n, a), d in rows:
            for k, c in d.items():
                w = sum((RADW[nm] if nm in RADW else w_of(nm)) * e
                        for nm, e in k)
                okp &= (w == 22)
        chk("A3-p%d 10 pristine Row_22 rows weight-22 pure; deep levels "
            "54x6 / 49x4 with W1/W2-split unit cofactors (measured)" % p,
            okp)
    rk, cons = synthetic_deep_solver_control(105337)
    chk("A4 deep-solve mechanics on a SYNTHETIC consistent system: "
        "rank == 4 (certified Schur rank), solvable", rk == 4 and cons)
    # ---------------- A5: the negative control (engine tier)
    eprimes = PRIMES if full else (105337,)
    cert_dir = os.path.join(SCRATCH, "certs")
    for p in eprimes:
        meta, gvars, polys = GB[p]
        pts, tries, diag = sample_points(p, gvars, polys, 12, 2026)
        if diag is not None:
            # A prime where the chart is provably F_p-point-poor: the
            # required behavior is the fail-closed diagnosis, and the
            # engine/negative-control tier has no rational points to run
            # on.  (Observed live at p=200257: W^4 pins 50209/51243 are
            # not 4th powers.)
            chk("A5-p%d sampler fail-closed with diagnosis (no F_p-"
                "rational W on this chart): %s" % (p, diag),
                "not 4th powers" in diag)
            continue
        chk("A5-p%d sampler: %d/12 points (%d tries)" % (p, len(pts),
            tries), len(pts) == 12)
        n_nid = 0
        certs = []
        for i, v in enumerate(pts):
            for draw in (0, 1, 2):
                cert, dval = point_certificate(
                    p, meta, gvars, v, i, draw, 2026,
                    cert_dir=(cert_dir if draw == 0 else None),
                    experimental_e=False)
                certs.append(cert)
                n_nid += (cert["verdict"] == "NOT_IN_DOMAIN")
        chk("A5-p%d chart reconstruction verified at 12 points x 3 draws:"
            " pivots vanish, all 48 row22compat membership rows vanish, "
            "all 76 raw D21 rows vanish" % p, len(certs) == 36)
        chk("A5-p%d NEGATIVE CONTROL (required): NOT_IN_DOMAIN for all "
            "banked D21 points, %d/36 point-draws (an e here would mean "
            "the wrong object)" % (p, n_nid), n_nid == 36)
        chk("A5-p%d certificates written (%s)" % (p, cert_dir),
            all("_written" in c or c["aux_draw"] != 0 for c in certs))
    # ---------------- E: 1b EXPERIMENTAL tier (soft; opt-in)
    if experimental_e:
        print("-- 1b EXPERIMENTAL tier (soft gates; every e is %s) --"
              % EXP)
        e1, e0 = demo_pipeline()
        chk("E1 DS4 demo through the pencil path: e = 1 (= banked DS6a); "
            "unit control e = 0 (DS6b)", e1 == 1 and e0 == 0, hard=False)
        n3, naff = euler_pencil_check(105337)
        chk("E2 spec-gap instrument: %d/%d 3+-source bins affine in slot "
            "weight (Euler pencil; per-family Toeplitz refuted => the "
            "square-block manifest is genuinely required)" % (naff, n3),
            n3 > 100 and naff == n3, hard=False)
        for p in eprimes:
            meta, gvars, polys = GB[p]
            pts, _, diag = sample_points(p, gvars, polys, 12, 2026)
            if diag is not None:
                print("   [p=%d] experimental tier skipped: %s"
                      % (p, diag), flush=True)
                continue
            es = collections.defaultdict(set)
            for i, v in enumerate(pts[:3]):
                dval = full_point(p, v, gvars, draw=0)
                rowdata = window_partials(p, dval, 21)
                for rname, fn in READINGS.items():
                    e, det = fn(p, rowdata, 21, cols_mode)
                    es[rname].add(e)
            print("   [p=%d] D21-tier diagnostic e over 3 banked points "
                  "(%s): %s" % (p, EXP,
                                {k: sorted(v, key=lambda x: (x is None, x))
                                 for k, v in es.items()}), flush=True)
            dval = full_point(p, pts[0], gvars, draw=0)
            rowdata = window_partials(p, dval, 21)
            ebase, _ = e_pencil(p, rowdata, 21, cols_mode)
            rng = random.Random(1234)
            stable = True
            for t in range(3):
                rows21, _ = raw_rows21()
                wsc = {lab: (rng.randrange(0, 3), rng.randrange(0, 3))
                       for lab, _ in rows21}
                e2, _ = e_pencil(p, window_partials(p, dval, 21,
                                                    wscales=wsc), 21,
                                 cols_mode)
                stable &= (e2 == ebase)
            chk("E3-p%d W-unit row rescales leave e(pencil) unchanged "
                "(units must not move valuations)" % p, stable, hard=False)
    hard_bad = [n for n, c, h in OK if h and not c]
    soft_bad = [n for n, c, h in OK if not h and not c]
    npass = sum(1 for _, c, _ in OK if c)
    print("RESULT: %d/%d gates pass; 1a HARD GATES %s%s (%.0fs)" %
          (npass, len(OK), "ALL PASS" if not hard_bad else
           "FAIL %s" % hard_bad,
           "" if not soft_bad else "; experimental soft-warns: %s"
           % soft_bad, time.time() - t00))
    print(BLOCKNOTE)
    return not hard_bad

# ================================================================== driver
def run_report(gbpath, prime, n, seed, experimental_e, cols_mode,
               cert_dir, lane_note):
    print("== VALUATION-E REPORT (verdict-day path; INTERNAL TOOLING, "
          "UNREVIEWED) ==")
    print(BLOCKNOTE)
    if gbpath is None:
        gbpath = next(f for f in GBFILES[prime] if os.path.exists(f))
    meta, gvars, polys = parse_msolve_out(gbpath)
    p = meta["characteristic"]
    print("GB: %s  sha256=%s...  (char %d, %d elements, %d vars)" %
          (os.path.basename(gbpath), meta["sha256"][:16], p,
           len(polys), len(gvars)))
    pts, tries, diag = sample_points(p, gvars, polys, n, seed)
    print("sampled %d/%d F_p points (%d tries, seed %d)" %
          (len(pts), n, tries, seed))
    if not pts:
        print("NO F_p-rational point sampled%s.  NOT emptiness "
              "(positive-dimensional loci can be F_p-poor; extension "
              "fields not implemented) -- no verdict, fail-closed."
              % (": " + diag if diag else ""))
        return
    nsurv = ndie = 0
    for i, v in enumerate(pts):
        for draw in (0, 1, 2):
            cert, dval = point_certificate(p, meta, gvars, v, i, draw,
                                           seed, cert_dir=cert_dir,
                                           experimental_e=experimental_e,
                                           cols_mode=cols_mode,
                                           lane_note=lane_note)
            if cert["verdict"] == "NOT_IN_DOMAIN":
                ndie += 1
                print("  point %d draw%d: NOT_IN_DOMAIN (compat rows "
                      "nonzero; dies at depth 23)" % (i, draw))
            else:
                nsurv += 1
                msg = ("  point %d draw%d: D23_POINT certified (54+77 "
                       "rows vanish; Schur rank 4)" % (i, draw))
                if experimental_e and "e_experimental" in cert:
                    es = {k: v["e"] for k, v in
                          cert["e_experimental"]["readings"].items()}
                    msg += "  %s e=%s" % (EXP, es)
                print(msg)
    print("summary: %d/%d point-draws NOT_IN_DOMAIN, %d D23 points" %
          (ndie, ndie + nsurv, nsurv))
    if nsurv == 0:
        print("all sampled points die at D23 -- consistent with the "
              "banked 0/12; sampling is NOT a variety kill (the lanes "
              "decide emptiness).")
    else:
        print("D23 point certificates written%s.  NO LIVE VERDICT: e is "
              "%s until the 1b manifest (series map + square block + "
              "surplus bridge) is banked and its promotion gates pass."
              % (" to %s" % cert_dir if cert_dir else "", EXP))

def main():
    ap = argparse.ArgumentParser(
        description="verdict-day valuation-e pipeline (1a certified, "
                    "1b experimental)")
    ap.add_argument("--gates", action="store_true")
    ap.add_argument("--full", action="store_true",
                    help="gates: engine tier at all three primes")
    ap.add_argument("--experimental-e", action="store_true",
                    help="enable the 1b EXPERIMENTAL e tier (E_CANDIDATE "
                         "only; blocked from promotion)")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--gb", default=None,
                    help="msolve .out to consume (default: banked fiber GB)")
    ap.add_argument("--prime", type=int, default=105337)
    ap.add_argument("--n", type=int, default=12)
    ap.add_argument("--seed", type=int, default=2026)
    ap.add_argument("--reading", default="all",
                    choices=["pencil", "weighted", "rank", "all"])
    ap.add_argument("--cols", default="tails", choices=["tails", "tailsW"])
    ap.add_argument("--cert-dir", default=os.path.join(SCRATCH, "certs"))
    ap.add_argument("--lane-note", default=None,
                    help="free-text lane metadata for the certificate "
                         "(solver version/command)")
    args = ap.parse_args()
    if args.selftest:
        e1, e0 = demo_pipeline()
        print("demo e = %s (want 1), unit e = %s (want 0) -- %s"
              % (e1, e0, EXP))
        sys.exit(0 if (e1, e0) == (1, 0) else 1)
    if args.gates:
        ok = run_gates(full=args.full, experimental_e=args.experimental_e,
                       cols_mode=args.cols)
        sys.exit(0 if ok else 1)
    if args.report:
        run_report(args.gb, args.prime, args.n, args.seed,
                   args.experimental_e, args.cols, args.cert_dir,
                   args.lane_note)
        sys.exit(0)
    ap.print_help()

if __name__ == "__main__":
    main()
