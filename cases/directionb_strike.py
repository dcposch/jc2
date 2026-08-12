#!/usr/bin/env python3
"""J-jet strike at the residue-A merge vertex (SHEET6-DIRECTIONB.md).

Chart: t = x^{-1/42}, y = P(t) + eta t^32, P = t^12 + uf18 t^18 +
uf24 t^24 + uf30 t^30 (prefix arc through d0 = 1).  With
f - a = c_f t^-12 Phi (1+O(t^42)), g = c_g t^-18 Gamma (1+O(t^42)),
J(f,g) = 1 is EXACTLY

  (t Phi_t - 12 Phi) Gamma_eta - Phi_eta (t Gamma_t - 18 Gamma)
      = -(42/(c_f c_g)) t^20.                                    (J)

Rows k = 0..41 are pure y-side; k != 20 homogeneous.  Machinery reused
READ-ONLY from cases/r1_experiment.py (ring, VExpr, gm_jet2 chart
products); VDEG_CAP raised so all rows k < D are EXACT (var degree <=
slot; no sentinel loss — asserted).

Phases: gate | rows [D] | all      (default D = 7)
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r1_experiment as R1
from r1_experiment import (K3, mk, Fr, K0, K1, SQ3, rmono, rC, radd, rmul,
                           rscal, RZERO, RONE, rk3, vC, vscal, vadd,
                           jmul, jadd, jscal, JONE, eta_poly_ref)

OK = []
def chk(name, cond):
    OK.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name, flush=True)

S_M, G_M = R1.S_M, R1.G_M

def fresh_registry():
    R1.VARS.clear(); R1.VSTAT.clear(); R1.PINS = {}

def build_jets(D, tag=""):
    """G_m-chart jets of f and g to slot < D, all template frees symbolic.
    Exactness: every var sits at slot >= 1, so var-degree <= slot < D;
    VDEG_CAP = D keeps everything exact (no HIVAR sentinel may appear)."""
    fresh_registry()
    R1.VDEG_CAP = D
    orbs = R1.build_generators(32 + D)
    jf = R1.gm_jet2(R1.FORB, orbs, D, tag + "f")
    jg = R1.gm_jet2(R1.GORB, orbs, D, tag + "g")
    for jp in (jf, jg):
        for (n, s), v in jp.items():
            assert not any(k and k[-1] == R1.HIVAR for k in v), \
                "sentinel loss at (%d,%d)" % (n, s)
    return orbs, jf, jg

def jrows(jf, jg, D):
    """LHS of (J) as a JetPoly: jmul(tPhi_t - 12Phi, Gamma_eta)
    - jmul(Phi_eta, tGamma_t - 18Gamma)."""
    jA  = {(n, s): vscal(v, K3(s - 12)) for (n, s), v in jf.items() if s != 12}
    jBg = {(n, s): vscal(v, K3(s - 18)) for (n, s), v in jg.items() if s != 18}
    jfH = {(n - 1, s): vscal(v, K3(n)) for (n, s), v in jf.items() if n}
    jgH = {(n - 1, s): vscal(v, K3(n)) for (n, s), v in jg.items() if n}
    return jadd(jmul(jA, jgH, D), jscal(jmul(jfH, jBg, D), K3(-1)))

def gate():
    print("== GATE: promoted top-order identities in the chart ==")
    t0 = time.time()
    orbs, jf, jg = build_jets(1, "g0")
    chk("E6: f-jet slot-0 = S_M [(e3-a1)(e3-a2)]^2, S_M = 7^12/2^6",
        R1.jet_matches_etapoly(jf, eta_poly_ref([(R1.A1c, 2), (R1.A2c, 2)],
                                                S_M)))
    chk("E6: g-jet slot-0 = G_M [(e3-a1)(e3-a2)]^3, G_M = -7^18/2^9",
        R1.jet_matches_etapoly(jg, eta_poly_ref([(R1.A1c, 3), (R1.A2c, 3)],
                                                G_M)))
    # E1/tower: G_0^2 - F_0^3 = 0 (slot-0 of g^2 - f^3 cancels: h1 lives
    # 20 slots lower).  Constant VExprs -> ring polys in eta.
    F0 = [RZERO] * 13; G0 = [RZERO] * 19
    for (n, s), v in jf.items():
        if s == 0: F0[n] = v.get((), RZERO)
    for (n, s), v in jg.items():
        if s == 0: G0[n] = v.get((), RZERO)
    def rpmul(a, b):
        r = [RZERO] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y: r[i + j] = radd(r[i + j], rmul(x, y))
        return r
    g2 = rpmul(G0, G0); f3 = rpmul(rpmul(F0, F0), F0)
    diff = [radd(a, rscal(b, K3(-1))) for a, b in
            zip(g2 + [RZERO] * (len(f3) - len(g2)),
                f3 + [RZERO] * (len(g2) - len(f3)))]
    chk("E1 transported: G_0^2 - F_0^3 = 0 identically (h1 drops to slot 20)",
        all(not c for c in diff))
    # Row_0 == 0 identically (the pinned-top gate for (J))
    R = jrows(jf, jg, 1)
    chk("Row_0 == 0 identically: -12 F_0 G_0' + 18 G_0 F_0' = 0",
        not any(v for v in R.values()))
    print("   gate done in %.1fs" % (time.time() - t0))

def rows_phase(D):
    print("== ROWS: J-jet system, chart depth D = %d (rows k = 1..%d) =="
          % (D, D - 1))
    t0 = time.time()
    orbs, jf, jg = build_jets(D)
    R = jrows(jf, jg, D)
    print("   jets: f %d terms, g %d terms; rows built in %.1fs"
          % (len(jf), len(jg), time.time() - t0), flush=True)
    byk = {}
    for (n, k), v in R.items():
        if v: byk.setdefault(k, {})[n] = v
    for k in sorted(byk):
        if k == 0:
            chk("Row_0 == 0 identically (depth-%d rebuild)" % D, not byk[0])
            continue
        comp = byk[k]
        print("-- Row_%d: %d nonzero eta-components" % (k, len(comp)))
        for n in sorted(comp):
            v = comp[n]
            names = sorted(set(
                "*".join(R1.VARS[i]["name"] for i in key)
                for key in v if key))
            const = v.get((), RZERO)
            print("   eta^%-3d const=%s  vars: %s"
                  % (n, "0" if not const else "NONZERO(%d keys)" % len(const),
                     ", ".join(names) if names else "-"))
    return orbs, jf, jg, byk

KEEP7 = ("uf18", "uf24", "uf30", "vf1_34", "vf1_36", "vf2_34", "vf2_36")

def build_frozen(D, keep, tag=""):
    """Jets at depth D with only `keep` vars free; every other template
    free (B-side + P-side tails) pinned to 0 (frozen stratum)."""
    fresh_registry()
    R1.VDEG_CAP = D
    R1.build_generators(32 + D)                 # dry: collect names
    names = [v["name"] for v in R1.VARS]
    fresh_registry()
    R1.PINS = {n: RZERO for n in names if n not in keep}
    R1.VDEG_CAP = D
    orbs = R1.build_generators(32 + D)
    jf = R1.gm_jet2(R1.FORB, orbs, D, tag + "f")
    jg = R1.gm_jet2(R1.GORB, orbs, D, tag + "g")
    for jp in (jf, jg):
        for (n, s), v in jp.items():
            assert not any(k and k[-1] == R1.HIVAR for k in v), "sentinel"
    return orbs, jf, jg

def vname(key):
    return "*".join(R1.VARS[i]["name"] for i in key) if key else "1"

def rshow(r, maxk=6):
    """compact ring element print."""
    its = list(r.items())
    s = " + ".join("%s*z%d.a1^%d.a2^%d.w1^%d.h1^%d.w2^%d.h2^%d.B^%d"
                   % ((repr(c),) + k) for k, c in its[:maxk])
    return s + (" +...(%d keys)" % len(its) if len(its) > maxk else "")

def dsys(D=21):
    print("== DSYS: dead-stretch J-system, frozen stratum, D = %d ==" % D)
    t0 = time.time()
    orbs, jf, jg = build_frozen(D, KEEP7)
    print("   jets: f %d, g %d terms (%.1fs); assembling rows" %
          (len(jf), len(jg), time.time() - t0), flush=True)
    R = jrows(jf, jg, D)
    byk = {}
    for (n, k), v in R.items():
        if v: byk.setdefault(k, {})[n] = v
    import pickle
    with open("/tmp/directionb_dsys.pkl", "wb") as fh:
        pickle.dump({"byk": byk, "vars": [v["name"] for v in R1.VARS],
                     "D": D}, fh)
    for k in range(D):
        comp = byk.get(k, {})
        if not comp:
            print("-- Row_%d: identically 0" % k); continue
        print("-- Row_%d: %d eta-components" % (k, len(comp)))
        for n in sorted(comp):
            v = comp[n]
            const = v.get((), RZERO)
            parts = ["const=" + (rshow(const, 3) if const else "0")]
            for key in sorted((k2 for k2 in v if k2), key=vname):
                parts.append("%s: %s" % (vname(key), rshow(v[key], 2)))
            print("   eta^%-3d %s" % (n, "  |  ".join(parts)))
    print("   dsys done in %.1fs (state /tmp/directionb_dsys.pkl)"
          % (time.time() - t0))
    return byk

def flatten_rows(byk, ks):
    """K3-linear rows: split every eta-component over its radical
    monomial basis (free K3-module); columns = var-monomial keys."""
    cols, rows = {}, []
    for k in ks:
        for n, v in sorted(byk.get(k, {}).items()):
            radkeys = set()
            for vk, r in v.items(): radkeys |= set(r)
            for rk in sorted(radkeys):
                row = {}
                for vk, r in v.items():
                    c = r.get(rk)
                    if c and not c.iszero():
                        col = cols.setdefault(vk, len(cols))
                        row[col] = c
                if row: rows.append(((k, n, rk), row))
    return cols, rows

def solve_rows(byk, ks, tag):
    cols, rows = flatten_rows(byk, ks)
    print("   [%s] %d K3-rows over %d var-monomial columns" %
          (tag, len(rows), len(cols)))
    NC = len(cols)
    rr = [dict(r) for _, r in rows]           # homogeneous: no RHS col
    rank, piv, red, bad = R1.row_reduce(rr, NC + 1, tag, quiet=True)
    inv = {i: k for k, i in cols.items()}
    print("   [%s] rank %d; pivot columns:" % (tag, rank))
    for c in piv: print("      %s" % vname(inv[c]))
    free = [vname(inv[c]) for c in range(NC) if c not in piv]
    print("   [%s] free columns: %s" % (tag, ", ".join(free) if free else "-"))
    return rank, piv, cols

def solve6():
    print("== SOLVE6: Row_6 rank, full frees, D = 7 ==")
    orbs, jf, jg = build_jets(7)
    R = jrows(jf, jg, 7)
    byk = {}
    for (n, k), v in R.items():
        if v: byk.setdefault(k, {})[n] = v
    for k in range(1, 6):
        chk("Row_%d == 0 identically" % k, not byk.get(k))
    solve_rows(byk, [6], "row6")

def dsys_tails(D=21):
    """Full-window system: the 7 dead-stretch + ALL P-side tails free
    (tf1/tf2/tg1/tg2/tg01/tg02 to level 32+D); B-side frozen."""
    print("== DSYS-TAILS: J-window, P-side tails free, D = %d ==" % D)
    t0 = time.time()
    fresh_registry(); R1.VDEG_CAP = D
    R1.build_generators(32 + D)
    keep = tuple(v["name"] for v in R1.VARS
                 if v["name"] in KEEP7 or v["name"][:2] in ("tf", "tg"))
    print("   free vars (%d): %s" % (len(keep), " ".join(keep)))
    orbs, jf, jg = build_frozen(D, keep, "T")
    print("   jets: f %d, g %d terms (%.1fs); assembling rows" %
          (len(jf), len(jg), time.time() - t0), flush=True)
    R = jrows(jf, jg, D)
    byk = {}
    for (n, k), v in R.items():
        if v: byk.setdefault(k, {})[n] = v
    import pickle
    with open("/tmp/directionb_tails.pkl", "wb") as fh:
        pickle.dump({"byk": byk, "vars": [v["name"] for v in R1.VARS],
                     "D": D}, fh)
    for k in range(D):
        comp = byk.get(k, {})
        if not comp:
            print("-- Row_%d: identically 0" % k); continue
        print("-- Row_%d: %d eta-components" % (k, len(comp)))
        for n in sorted(comp):
            v = comp[n]
            const = v.get((), RZERO)
            vk = sorted(set(vname(k2) for k2 in v if k2))
            print("   eta^%-3d const %s; vars: %s" %
                  (n, "0" if not const else "NZ(%d)" % len(const),
                   ", ".join(vk)[:160]))
    print("   done in %.1fs (state /tmp/directionb_tails.pkl)"
          % (time.time() - t0))

def danal():
    """Analyze the banked frozen-stratum system (/tmp/directionb_dsys.pkl):
    const-part census per row, then rank of the homogeneous part."""
    import pickle
    with open("/tmp/directionb_dsys.pkl", "rb") as fh:
        st = pickle.load(fh)
    byk, D = st["byk"], st["D"]
    print("== DANAL: frozen-stratum J-rows, D = %d ==" % D)
    for k in range(D):
        comp = byk.get(k, {})
        if not comp:
            print("-- Row_%d: identically 0" % k); continue
        print("-- Row_%d: %d eta-components" % (k, len(comp)))
        for n in sorted(comp):
            v = comp[n]
            const = v.get((), RZERO)
            vk = [k2 for k2 in v if k2]
            print("   eta^%-3d const %s; %d var-terms: %s" %
                  (n, "== 0" if not const else "NONZERO " + rshow(const, 4),
                   len(vk), ", ".join(sorted(set(map(vname, vk))))[:200]))
    if D > 20:
        r20 = byk.get(20, {})
        v0 = r20.get(0)
        if v0 is None:
            chk("Row_20 eta^0 present (must equal -42: S_R=G_R=1 fixes "
                "c_f = c_g = 1)", False)
        else:
            const = v0.get((), RZERO)
            print("   Row_20 eta^0: const = %s ; var-terms: %s"
                  % (rshow(const, 8),
                     ", ".join(sorted(set(vname(k2) for k2 in v0 if k2)))
                     or "-"))
            chk("Row_20 eta^0 const == -42 exactly (zero-extension "
                "satisfies the inhomogeneous J-row)",
                const == rC(K3(-42)))
    hom = {k: {n: v for n, v in comp.items() if not (k == 20 and n == 0)}
           for k, comp in byk.items()}
    ks = [k for k in sorted(hom) if hom[k]]
    if ks: solve_rows(hom, ks, "dsys-hom")

def w4():
    """Row_20 = 9 rows on X_i = alpha_i w_i^4 alone.  Check ratio
    consistency of the 8 homogeneous rows, solve with eta^0 = -42,
    compare against the E5 quartic pin (E6-transported H_M)."""
    import pickle
    with open("/tmp/directionb_dsys.pkl", "rb") as fh:
        st = pickle.load(fh)
    byk = st["byk"]; assert st["D"] == 21
    for k in range(20):
        chk("Row_%d == 0 identically (7 dead-stretch frees symbolic)" % k,
            not byk.get(k))
    r20 = byk[20]
    K1M = (0, 1, 0, 4, 0, 0, 0, 0)   # alpha1 * w1^4
    K2M = (0, 0, 1, 0, 0, 4, 0, 0)   # alpha2 * w2^4
    sysr = {}
    for n, v in sorted(r20.items()):
        chk("Row_20 eta^%d: no var-terms, support {a1w1^4, a2w2^4}" % n,
            all(not k2 for k2 in v) and
            set(v.get((), {})) <= {K1M, K2M})
        c = v.get((), RZERO)
        sysr[n] = (c.get(K1M, K0), c.get(K2M, K0))
    kconj = lambda c: K3(c[0], -c[1])
    # tau-covariance: coefficient of X2 = conj of coefficient of X1
    chk("tau-covariance: c2 = conj(c1) in every row",
        all(c2 == kconj(c1) for c1, c2 in sysr.values()))
    # ratio consistency of the homogeneous rows (n != 0)
    ratios = {n: (-(c2 / c1)) for n, (c1, c2) in sysr.items()
              if n != 0 and not c1.iszero()}
    vals = list(ratios.values())
    for n, r in sorted(ratios.items()):
        print("   eta^%-3d ratio pin X1/X2 = %r" % (n, r))
    distinct = len({(r[0], r[1]) for r in vals})
    chk("THE KILL: the 8 homogeneous ratio pins are NOT all equal "
        "(%d distinct) => X1 = X2 = 0 forced" % distinct, distinct > 1)
    chk("2x2 witness: det(eta^3, eta^6 rows) != 0",
        not (sysr[3][0] * sysr[6][1] - sysr[6][0] * sysr[3][1]).iszero())
    c1, c2 = sysr[0]
    chk("eta^0 row nonzero (0 = -42/(c_f c_g) is then absurd: "
        "INCONSISTENT, zero-tail locus DEAD)",
        not c1.iszero() and not c2.iszero())
    # w_i = 0 is independently absurd: template-forced w_i^4 != 0
    # (TEMPLATE 2c-E5 lead; Prop 5.3 squarefree pole pattern).

if __name__ == "__main__":
    args = sys.argv[1:]
    phase = args[0] if args else "all"
    D = int(args[1]) if len(args) > 1 else 7
    if phase in ("gate", "all"): gate()
    if phase in ("rows", "all"): rows_phase(D)
    if phase == "dsys": dsys(D if len(args) > 1 else 21)
    if phase == "solve6": solve6()
    if phase == "danal": danal()
    if phase == "w4": w4()
    if phase == "tails": dsys_tails(D if len(args) > 1 else 21)
    bad = [n for n, c in OK if not c]
    print("\nTOTAL: %d checks, %d FAIL %s" % (len(OK), len(bad), bad or ""))
