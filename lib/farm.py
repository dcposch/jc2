"""Phase 3 farm driver (SECTION4-AUTOMATION): end-to-end family -> verdict.

Builds ON TOP of lib/families.py + lib/reduce4.py (neither is modified).
Per family row of the GGV5 deg<=maxdeg catalog:

 1. PRE-FILTER (SURPLUS-EXT.md section 3 = the coverage table, corner
    arithmetic only): j = ceil(b0/a0), k = j-2, y-axis flag (a0 | b0),
    d2* = a0/(j*a0-b0).  A family is settled with NO computation only when
    its cell is THEOREM-COVERED with FULL coverage.  Per SURPLUS-EXT 3.2 the
    single deg<=150 THEOREM-COVERED row is PARTIAL (the (8,28) c1-pentagon
    precedent: corner data cannot exclude non-strip siblings), so family
    skips carry partial=False only when reduction-shape certainty exists --
    currently never from corner data.  The cell is therefore re-evaluated
    per REDUCED subcase: an exact (2,2)-gap strip (SURPLUS.md vertex-gap
    theorem, char not in {2,3,5}) gets verdict EMPTY-BY-THEOREM((2,2)) and
    no emission.  SURPLUS-4 cells (2,3),(2,4),(3,3),(4,3),(5,3) are
    support-rigidity results, NOT emptiness certificates (SURPLUS-EXT 1.2
    HONEST note) -> never skipped.
 2. reduce4.reduce_family -> per reduced subcase (ordered c1..cN by
    descending polygon size = the GGV22 numbering):
    SystemA(nonorigin, fix_ones by the AUDIT.md claim-2 torus-determinant
    rule: lexmax corner pair, det = w_P+w_Q != 0, w = i-(k+1)j, fallback
    scan) -> Cascade3(level_dir=(2,1); JC_BACKEND=flint per lib/FASTCOEF.md)
    -> guarded two_chart -> emissions at p=65521 and char 0 into
    systems/farm/<family>/: _core, _chartG/_chartC, kill-splits _cC<var>
    when the pivot product is a monomial (the cCa2/cCa6 pattern, AUDIT.md
    claim 5).  Cascade abort-swell => the sound mid-cascade state is
    emitted as _partial (CAMPAIGN semantics: under-reduction is sound).
 3. manifest.json per family: reductions, cells, emitted systems,
    pre-filter outcomes, stuck/swell statuses.
 4. dispatch(): manifests -> per-box queue.txt files, jobs sorted by
    estimated size (bytes) and dealt round-robin.

Byte-compatibility gate (tests/test_farm.py): this pipeline reproduces the
archived systems/ emissions for the four GGV22 S4 families byte-for-byte
where archives exist (v6 cores, chartG/chartC, cCa2/cCa6, partial cores).
"""
import sys, os, json, time, traceback
from math import gcd
from fractions import Fraction

sys.path.insert(0, os.path.dirname(__file__))
from families import get_pllc, chain_path, enumerate_cases, corner_data, v11
from reduce4 import reduce_family
from jc import SystemA
from reduce3 import Cascade3
from reduce import _kill_var
from chartelim import Leaf, leaf_to_msolve, _subst_linear, _invred
from jc import cadd, cmul

PRIMES_DEFAULT = (65521, 0)          # p=65521 + char 0
LEVEL_DIR = (2, 1)                   # the audited campaign cascade order
SURPLUS4_CELLS = {(2, 3), (2, 4), (3, 3), (4, 3), (5, 3)}   # SURPLUS-EXT 1.3

# ---------------------------------------------------------------- catalog

class FamilyRow:
    "one deduplicated row of the GGV5 deg<=maxdeg tables + its CornerData"
    def __init__(self, name, chain, fam, j, mn, deg):
        self.name, self.chain, self.fam, self.j = name, chain, fam, j
        self.mn, self.deg = mn, deg
        self.cd = corner_data(chain, fam, j, name=name)

    @property
    def path(self):
        return chain_path(self.chain)


def catalog(maxdeg):
    """Deduplicated family rows (34 at maxdeg=150), deterministic order and
    names a0_b0mnMNdDEG (+ _rI on path collisions, I by sorted chain path)."""
    rows = {}
    for ch, fam, j, mn, deg in enumerate_cases(maxdeg):
        key = (chain_path(ch), mn, deg)
        if key not in rows:
            rows[key] = (ch, fam, j)
    base = {}
    for (path, mn, deg), (ch, fam, j) in rows.items():
        a0, b0 = ch.edges[0].A.a, ch.edges[0].A.b
        name = f"{a0}_{b0}mn{mn[0]}{mn[1]}d{deg}"
        base.setdefault(name, []).append((path, mn, deg, ch, fam, j))
    out = []
    for name, group in base.items():
        group.sort(key=lambda g: (str(g[0]),))
        for i, (path, mn, deg, ch, fam, j) in enumerate(group):
            nm = name if len(group) == 1 else f"{name}_r{i}"
            out.append(FamilyRow(nm, ch, fam, j, mn, deg))
    out.sort(key=lambda r: (r.deg, r.cd.A0.a, r.cd.A0.b, r.mn, str(r.path)))
    return out


S4_ALIAS = {"9_27": (9, 27, (2, 3)), "9_24": (9, 24, (2, 3)),
            "8_28": (8, 28, (3, 2)), "7_21": (7, 21, (2, 3))}

def find_family(spec, maxdeg=150):
    "resolve a family spec: S4 alias ('9_24') or catalog name ('11_33mn23d132')"
    cat = catalog(maxdeg)
    if spec in S4_ALIAS:
        a0, b0, mn = S4_ALIAS[spec]
        hits = [r for r in cat
                if (r.cd.A0.a, r.cd.A0.b) == (a0, b0) and r.mn == mn
                and len(r.chain.edges) == (2 if spec == "9_27" else 1)]
        assert len(hits) == 1, (spec, [h.name for h in hits])
        return hits[0]
    hits = [r for r in cat if r.name == spec]
    if not hits:
        raise KeyError(f"family {spec!r} not in catalog(maxdeg={maxdeg})")
    return hits[0]

# ---------------------------------------------------------------- pre-filter

def prefilter_family(cd):
    """SURPLUS-EXT 3.1/3.2 family-level coverage cell from corner arithmetic.
    skip=True (no computation) requires THEOREM-COVERED with partial=False;
    corner data alone can never certify all reduced subcases are strips
    (the (8,28) c1 precedent), so partial=True whenever a covered cell is
    assigned -- family-level skips are currently impossible, faithfully to
    SURPLUS-EXT 3.2 ('THEOREM-COVERED 1 row -- PARTIAL')."""
    a, b = cd.A0.a, cd.A0.b
    j = -((-b) // a)                       # ceil(b0/a0)
    k = j - 2                              # == cd.rhs_exp
    yaxis = (b % a == 0)                   # A0 maps onto the y-axis under psi_j
    d2star = None
    if not yaxis:
        d2 = Fraction(a, j * a - b)
        d2star = int(d2) if d2.denominator == 1 else str(d2)
    out = dict(k=k, j=j, yaxis=yaxis, d2star=d2star, partial=True, skip=False)
    if k <= 0:
        out.update(cell="MECHANISM-ABSENT", detail=f"k={k}<=0: no gap")
    elif k == 1:
        out.update(cell="MECHANISM-ABSENT",
                   detail="no-gap k=1: both bottom corners at x=1, "
                          "condition (ii) fails (SURPLUS-EXT 3.2)")
    elif yaxis:
        if k >= 3:
            out.update(cell="MECHANISM-ABSENT",
                       detail=f"k={k}>=3 conditional: y-axis flagged; strip "
                              "shape would be d2=2-covered (SURPLUS-EXT 2)")
        else:
            out.update(cell="UNKNOWN",
                       detail="k=2, y-axis flag: strip impossible where A0 "
                              "survives; expected OUT-OF-SCOPE shape")
    elif d2star == 2 and k == 2:
        out.update(cell="THEOREM-COVERED", cellkd=(2, 2),
                   detail="(2,2) gap regime (SURPLUS.md theorem); PARTIAL: "
                          "strip subcases only, pentagon siblings possible "
                          "-- subcase-level re-check decides")
    elif isinstance(d2star, int) and (k, d2star) in SURPLUS4_CELLS:
        out.update(cell="SURPLUS-4-COVERED", cellkd=(k, d2star),
                   detail="support-rigidity cell (SURPLUS-EXT 1): NOT an "
                          "emptiness certificate; compute proceeds")
    elif d2star == 2 and k >= 3:
        out.update(cell="MECHANISM-ABSENT",
                   detail=f"k={k}>=3, d2*=2: no near-origin obstruction "
                          "(SURPLUS-EXT 2.2 theorem); compute proceeds")
    else:
        out.update(cell="UNKNOWN", detail=f"cell (k,d2*)=({k},{d2star}) "
                                          "outside the classified regimes")
    return out


def _strip_data(corners):
    """If hull `corners` is a strip along primitive (1,d2) with top edge
    through the origin, return (d2, width, bottom corner p0); else None.
    p0 = the v-max corner with minimal x (adjacent to the origin)."""
    C = [tuple(p) for p in corners]
    if (0, 0) not in C or any(x == 0 and y > 0 for x, y in C):
        return None                        # y-axis support -> not a strip
    cands = {Fraction(y, x) for x, y in C if x > 0 and y > 0 and y % x == 0}
    for d2f in sorted(cands):
        if d2f.denominator != 1:
            continue
        d2 = int(d2f)
        vals = {d2 * x - y for x, y in C}
        if len(vals) == 2 and min(vals) == 0 and max(vals) > 0:
            w = max(vals)
            bottom = sorted((x, y) for x, y in C if d2 * x - y == w)
            return d2, w, bottom[0]
    return None


def prefilter_subcase(NP, NQ, rhs_exp):
    """SURPLUS-EXT 3.2 cell of one REDUCED subcase (ground-truth rules).
    skip=True <=> exact THEOREM-COVERED (2,2)-gap strip: verdict
    EMPTY-BY-THEOREM((2,2)) needs no computation."""
    k = rhs_exp
    sP, sQ = _strip_data(NP), _strip_data(NQ)
    out = dict(k=k, skip=False)
    if sP is None or sQ is None:
        out.update(cell="OUT-OF-SCOPE", shape="y-axis/pentagon",
                   detail="y-axis support or non-strip shape: gap-kill "
                          "fails (SURPLUS note 5)")
        return out
    d2P, wP, p0 = sP
    d2Q, wQ, q0 = sQ
    out.update(shape="strip", d2=(d2P, d2Q), wP=wP, wQ=wQ, p0=p0, q0=q0)
    hyp_i = ({p0, q0} == {(1, 0), (k, 1)}) and d2P == d2Q
    if k <= 1:
        out.update(cell="MECHANISM-ABSENT",
                   detail=f"strip, k={k}, d=(1,{d2P}): no gap")
    elif not hyp_i:
        out.update(cell="UNKNOWN",
                   detail=f"strip but hypothesis (i) fails: bottom corners "
                          f"{p0},{q0} != {{(1,0),({k},1)}}")
    elif k == 2 and d2P == 2 and max(x for x, _ in NP) >= 2 \
            and max(x for x, _ in NQ) >= k + 1:
        out.update(cell="THEOREM-COVERED", cellkd=(2, 2), skip=True,
                   detail="(2,2)-gap strip: SURPLUS.md vertex-gap theorem "
                          "(char not in {2,3,5}); the open_8_28_c2 cell")
    elif (k, d2P) in SURPLUS4_CELLS:
        out.update(cell="SURPLUS-4-COVERED", cellkd=(k, d2P),
                   detail="support rigidity only (SURPLUS-EXT 1.2): "
                          "not an emptiness certificate; compute proceeds")
    elif d2P == 2 and k >= 3:
        out.update(cell="MECHANISM-ABSENT",
                   detail=f"k={k}>=3, d2=2: no near-origin obstruction "
                          "(SURPLUS-EXT 2.2); compute proceeds")
    else:
        out.update(cell="NEEDS-COMPUTATION",
                   detail=f"strip cell ({k},{d2P}) unclassified")
    return out

# ------------------------------------------------- torus fix (AUDIT claim 2)

def torus_fix(cornersP, cornersQ, k):
    """fix_ones by the AUDIT.md claim-2 determinant rule: weight
    w(i,j) = i - (k+1)*j; need det = w(pP)+w(pQ) != 0.  Selection: the
    lexicographically maximal corner of each polygon (reproduces emit.py FIX
    on all S4 cases); fallback: scan corner pairs in (-x,-y) order.
    Returns (fix_list, det) -- ([], 0) if no admissible pair exists."""
    w = lambda p: p[0] - (k + 1) * p[1]
    nzP = sorted((tuple(p) for p in cornersP if tuple(p) != (0, 0)),
                 key=lambda p: (-p[0], -p[1]))
    nzQ = sorted((tuple(p) for p in cornersQ if tuple(p) != (0, 0)),
                 key=lambda p: (-p[0], -p[1]))
    pP, pQ = max(map(tuple, cornersP)), max(map(tuple, cornersQ))
    if w(pP) + w(pQ) != 0:
        return [("P", pP), ("Q", pQ)], w(pP) + w(pQ)
    for a in nzP:
        for b in nzQ:
            if w(a) + w(b) != 0:
                return [("P", a), ("Q", b)], w(a) + w(b)
    return [], 0

# ------------------------------------------------- guarded two_chart

class ChartSwell(Exception):
    "two_chart would exceed the term cap; carries (pivot var, estimate)"


def guarded_two_chart(C, maxterms=None):
    """chartelim.two_chart with a swell guard: identical pivot choices and
    byte-identical output when under the cap; raises ChartSwell when a
    substitution is estimated (or measured) to exceed `maxterms` terms in
    one equation.  Default cap: JC_MAXTERMS or 20000 (Cascade3's)."""
    if maxterms is None:
        maxterms = int(os.environ.get("JC_MAXTERMS", 20000))
    invof = dict(C.invof)
    varnames = list(C.varnames)
    eqs = [dict(c) for c in C.eqs]
    alive = set(C.alive)
    prod = {(): Fraction(1)}
    info = []
    for b in sorted(C.bvars):
        best = None
        for ei, c in enumerate(eqs):
            coeff, rest, ok = {}, {}, True
            for m, kk in c.items():
                cnt = sum(1 for i in m if i == b)
                if cnt == 0:
                    rest[m] = kk
                elif cnt == 1:
                    coeff[tuple(i for i in m if i != b)] = kk
                else:
                    ok = False
                    break
            if ok and coeff:
                key = (len(coeff), len(rest))
                if best is None or key < best[0]:
                    best = (key, ei, coeff, rest)
        if best is None:
            continue
        _, ei, coeff, rest = best
        est = max((sum(1 for m in c if b in m) * max(len(rest), 1) + len(c)
                   for c in eqs), default=0)
        if est > maxterms:
            raise ChartSwell((varnames[b], est))
        u = len(varnames)
        varnames.append(f"u{u}")
        g = {}
        for m, kk in rest.items():
            g = cadd(g, cmul({m: -kk}, {(u,): Fraction(1)}))
        eqs = [c for j, c in enumerate(eqs) if j != ei]
        eqs = _subst_linear(eqs, b, g, invof)
        big = max((len(c) for c in eqs), default=0)
        if big > maxterms:
            raise ChartSwell((C.varnames[b], big))
        eqs.append(cadd(cmul({(u,): Fraction(1)}, coeff), {(): Fraction(-1)}))
        alive.add(u)
        alive.discard(b)
        prod = cmul(prod, coeff)
        info.append((C.varnames[b], len(coeff)))
    leafG = Leaf(eqs, varnames, alive, "generic:" + ",".join(n for n, _ in info))
    eqsC = [dict(c) for c in C.eqs] + [prod]
    leafC = Leaf(eqsC, list(C.varnames), set(C.alive), "complement")
    return leafG, leafC, prod, info

# ------------------------------------------------- emission helpers

def _mono_str(mon, varnames):
    if not mon:
        return "1"
    parts, i = [], 0
    while i < len(mon):
        e = 1
        while i + e < len(mon) and mon[i + e] == mon[i]:
            e += 1
        parts.append(varnames[mon[i]] if e == 1 else f"{varnames[mon[i]]}^{e}")
        i += e
    return "*".join(parts)


def _leaf_modp_ok(leaf, p):
    "prime hygiene (AUDIT claim-6 obligation): no cleared coeff vanishes mod p"
    import math
    for c in leaf.eqs:
        den = 1
        for k in c.values():
            den = den * k.denominator // math.gcd(den, k.denominator)
        if any(int(k * den) % p == 0 for k in c.values()):
            return False
    return True


def _emit(records, outdir, relroot, name, kind, chars, writer):
    "run writer(path, char) per char; append system records; skip on p-hygiene"
    out = []
    for ch in chars:
        suffix = f"p{ch}.ms" if ch else "q.ms"
        path = os.path.join(outdir, f"{name}.{suffix}")
        try:
            res = writer(path, ch)
        except AssertionError as e:            # Cascade write_msolve p-guard
            records.append(dict(name=name, kind=kind, char=ch,
                                status=f"skipped: {e}"))
            if os.path.exists(path):
                os.remove(path)
            continue
        rec = dict(name=name, kind=kind, char=ch,
                   path=os.path.relpath(path, relroot),
                   bytes=os.path.getsize(path))
        if isinstance(res, tuple):
            rec["nvars"], rec["neqs"] = res
        records.append(rec)
        out.append(rec)
    return out

# ------------------------------------------------- per-family plan + execute

def plan_family(row, prefilter=True, pllc=None):
    """Cheap (integer-only) half of the pipeline: pre-filter + reduce4 +
    per-subcase decisions.  Returns the manifest skeleton with, per case,
    decision 'emit' | 'empty-by-theorem'."""
    cd = row.cd
    man = dict(family=row.name, mn=list(row.mn), deg=row.deg,
               generated=time.strftime("%Y-%m-%d"),
               corner=dict(A0=[cd.A0.a, cd.A0.b], A0p=[cd.A0p.a, cd.A0p.b],
                           path=[[str(Fraction(x)), y] for x, y in row.path],
                           j=row.j, k=cd.rhs_exp, steps=[list(s) for s in cd.steps],
                           degP=cd.degP, degQ=cd.degQ),
               prefilter=prefilter_family(cd), cases=[], statuses=[])
    if prefilter and man["prefilter"]["skip"]:
        man["verdict"] = f"EMPTY-BY-THEOREM({man['prefilter'].get('cellkd')})"
        man["settled_without_compute"] = True
        man["polygons"] = dict(S=[list(p) for p in cd.S])
        return man
    man["settled_without_compute"] = False
    if pllc is None:
        pllc = get_pllc(4 * max(cd.A0.a, cd.A0.b))
    r = reduce_family(cd, pllc)
    man["reduction"] = dict(status=r.status, ncases=len(r.cases),
                            log_lines=len(r.log), log_tail=list(r.log[-3:]))
    if r.status == "discarded":
        man["verdict"] = "DISCARDED"
        return man
    if r.status == "stuck":
        man["verdict"] = "REDUCE4-STUCK"
        man["statuses"].append("reduce4 stuck: " + r.log[-1][:200])
        return man
    area = lambda cs: abs(sum(cs[i][0] * cs[(i + 1) % len(cs)][1]
                              - cs[(i + 1) % len(cs)][0] * cs[i][1]
                              for i in range(len(cs))))
    cases = sorted(r.cases, key=lambda c: (-(area(list(c.NP)) + area(list(c.NQ))),
                                           tuple(c.NP), tuple(c.NQ)))
    for i, c in enumerate(cases):
        cname = f"{row.name}_c{i + 1}"
        cell = prefilter_subcase(list(c.NP), list(c.NQ), c.rhs_exp)
        entry = dict(name=cname, reduce4_label=c.label,
                     NP=[list(p) for p in c.NP], NQ=[list(p) for p in c.NQ],
                     rhs_exp=c.rhs_exp, cell=cell)
        if prefilter and cell["skip"]:
            entry["verdict"] = f"EMPTY-BY-THEOREM({cell['cellkd']})"
            entry["decision"] = "empty-by-theorem"
        else:
            entry["decision"] = "emit"
        man["cases"].append(entry)
    return man


def execute_case(entry, outdir, relroot, chars=PRIMES_DEFAULT,
                 chart_maxterms=None):
    "SystemA -> Cascade3(flint) -> charts/splits -> .ms files; mutates entry"
    NP = [tuple(p) for p in entry["NP"]]
    NQ = [tuple(p) for p in entry["NQ"]]
    k = entry["rhs_exp"]
    fix, det = torus_fix(NP, NQ, k)
    entry["fix_ones"] = dict(fix=[[kind, list(pt)] for kind, pt in fix], det=det)
    S = SystemA(entry["name"], NP, NQ, (k, 0), nonvanish="nonorigin",
                fix_ones=fix)
    C = Cascade3(S, level_dir=LEVEL_DIR)
    t0 = time.time()
    st = C.run()
    records = entry["systems"] = []
    entry["cascade"] = dict(
        status=st, backend=C.backend, level_dir=list(LEVEL_DIR),
        seconds=round(time.time() - t0, 1), core_vars=len(C.alive),
        core_eqs=len(C.eqs), elim=len(C.elim), zeroed=len(C.zeroed),
        maxterms=max((len(c) for c in C.eqs), default=0))
    if st == "EMPTY":
        entry["verdict"] = "EMPTY-BY-CASCADE"
        return entry
    if st == "aborted-swell":
        # sound mid-cascade state; probe lane only -> mod-p chars (the
        # archived reg_9_27/reg_7_21 partial convention)
        pchars = tuple(c for c in chars if c) or chars
        _emit(records, outdir, relroot, f"{entry['name']}_partial", "partial",
              pchars, C.write_msolve)
        entry["verdict"] = "PARTIAL-EMITTED"
        return entry
    assert st == "reduced", st
    _emit(records, outdir, relroot, f"{entry['name']}_core", "core", chars,
          C.write_msolve)
    try:
        G, Cm, prod, info = guarded_two_chart(C, chart_maxterms)
    except ChartSwell as e:
        entry["chart"] = dict(status="skipped-swell", trip=list(e.args[0]))
        entry["verdict"] = "EMITTED-CORE-ONLY"
        return entry
    chart = entry["chart"] = dict(status="ok",
                                  pivots=[[n, ln] for n, ln in info])
    for tag, L in (("chartG", G), ("chartC", Cm)):
        pruned = [ch for ch in chars if ch == 0 or _leaf_modp_ok(L, ch)]
        if len(pruned) < len([c for c in chars]):
            entry.setdefault("hygiene", []).append(
                f"{tag}: coeff vanishes mod dropped prime(s)")
        _emit(records, outdir, relroot, f"{entry['name']}_{tag}", tag, pruned,
              lambda p, ch, L=L: leaf_to_msolve(L, p, ch))
    chart["prod_terms"] = len(prod)
    if len(prod) == 1:
        (mon, kk), = prod.items()
        chart["prod"] = f"{kk} * {_mono_str(mon, C.varnames)}"
        nonunits = sorted({v for v in mon if v not in C.units})
        chart["prod_nonunits"] = [C.varnames[v] for v in nonunits]
        chart["splits"] = []
        for v in nonunits:
            eqs = [_kill_var(dict(c), v) for c in C.eqs]
            eqs = [c for c in eqs if c]
            L = Leaf(eqs, list(C.varnames), set(C.alive) - {v},
                     f"kill {C.varnames[v]}")
            tag = f"cC{C.varnames[v]}"
            pruned = [ch for ch in chars if ch == 0 or _leaf_modp_ok(L, ch)]
            _emit(records, outdir, relroot, f"{entry['name']}_{tag}", "split",
                  pruned, lambda p, ch, L=L: leaf_to_msolve(L, p, ch))
            chart["splits"].append(C.varnames[v])
    entry["verdict"] = "EMITTED"
    return entry


def run_family(row, farm_root, relroot=None, prefilter=True,
               chars=PRIMES_DEFAULT, chart_maxterms=None, pllc=None,
               verbose=True):
    "full pipeline for one FamilyRow; writes systems + manifest.json"
    relroot = relroot or os.path.dirname(farm_root)
    outdir = os.path.join(farm_root, row.name)
    os.makedirs(outdir, exist_ok=True)
    man = plan_family(row, prefilter=prefilter, pllc=pllc)
    for entry in man["cases"]:
        if entry["decision"] != "emit":
            continue
        try:
            execute_case(entry, outdir, relroot, chars, chart_maxterms)
        except Exception as e:
            entry["verdict"] = f"ERROR({type(e).__name__})"
            entry["error"] = traceback.format_exc(limit=3)
            man["statuses"].append(f"{entry['name']}: {e}")
        if verbose:
            cas = entry.get("cascade", {})
            print(f"  {entry['name']}: {entry['verdict']}"
                  f" [{entry['cell']['cell']}]"
                  + (f" cascade {cas.get('status')} {cas.get('seconds')}s"
                     if cas else ""), flush=True)
    for entry in man["cases"]:
        if entry["decision"] == "empty-by-theorem" and verbose:
            print(f"  {entry['name']}: {entry['verdict']} (no computation)",
                  flush=True)
        if entry.get("verdict", "").startswith(("PARTIAL", "EMITTED-CORE",
                                                "ERROR", "REDUCE4")):
            man["statuses"].append(f"{entry['name']}: {entry['verdict']}")
        if entry.get("chart", {}).get("status") == "skipped-swell":
            man["statuses"].append(f"{entry['name']}: chart skipped (swell)")
        if entry.get("cascade", {}).get("status") == "aborted-swell":
            man["statuses"].append(f"{entry['name']}: cascade aborted-swell")
    if "verdict" not in man:
        vs = sorted({e.get("verdict", "?") for e in man["cases"]})
        man["verdict"] = ("NO-CASES" if not vs else
                          vs[0] if len(vs) == 1 else "MIXED")
    with open(os.path.join(outdir, "manifest.json"), "w") as f:
        json.dump(man, f, indent=1, sort_keys=True)
    return man

# ---------------------------------------------------------------- dispatch

def dispatch(farm_root, nboxes, queue_dir=None, chars=None):
    """manifests -> per-box queue.txt files.  Jobs = emitted .ms systems
    (optionally filtered to `chars`), sorted by estimated size (bytes)
    descending and dealt round-robin, so each box gets an even mix of big
    and small jobs.  Returns per-box (count, bytes) summary."""
    queue_dir = queue_dir or os.path.join(farm_root, "queue")
    jobs = []
    for fam in sorted(os.listdir(farm_root)):
        mpath = os.path.join(farm_root, fam, "manifest.json")
        if not os.path.isfile(mpath):
            continue
        with open(mpath) as f:
            man = json.load(f)
        for entry in man.get("cases", []):
            for rec in entry.get("systems", []):
                if "path" not in rec:
                    continue
                if chars is not None and rec["char"] not in chars:
                    continue
                jobs.append((rec["bytes"], rec["path"], man["family"],
                             rec["name"], rec["kind"], rec["char"]))
    jobs.sort(key=lambda j: (-j[0], j[1]))
    boxes = [[] for _ in range(nboxes)]
    for i, job in enumerate(jobs):
        boxes[i % nboxes].append(job)
    summary = []
    for i, box in enumerate(boxes):
        bdir = os.path.join(queue_dir, f"box{i + 1:02d}")
        os.makedirs(bdir, exist_ok=True)
        total = sum(j[0] for j in box)
        with open(os.path.join(bdir, "queue.txt"), "w") as f:
            f.write(f"# farm queue box{i + 1:02d}: {len(box)} jobs, "
                    f"{total} bytes est\n")
            for est, path, fam, name, kind, ch in box:
                f.write(f"{path}\n")
        summary.append((len(box), total))
    return summary
