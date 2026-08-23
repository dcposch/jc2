"""Task 2/4: replay the Cascade3 + two_chart substitution chain on the original
equations, tracking exactly which events touch which equation.  Run for
open_8_28_c2 (collapse expected) and reg_9_24_c3 (no collapse expected).

Usage: python3 eq3_chain.py [case_name]
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
sys.path.insert(0, os.path.dirname(__file__))
from fractions import Fraction
from jc import SystemA, cadd, cmul, bracket, padd
from emit import CASES, FIX
from reduce3 import Cascade3
from reduce import _kill_var
import chartelim

name = sys.argv[1] if len(sys.argv) > 1 else "open_8_28_c2"
spec = CASES[name]
S = SystemA(name, spec["cornersP"], spec["cornersQ"], spec["rhs"],
            nonvanish="nonorigin", fix_ones=FIX[name])

# recover bracket keys (same construction as SystemA)
def coef(kind, pt):
    return {(): 1} if (kind, pt) in S.fix else {(S.varof[(kind, pt)],): 1}
E = padd(bracket({p: coef("P", p) for p in S.ptsP},
                 {q: coef("Q", q) for q in S.ptsQ}), {spec["rhs"]: {(): -1}})
keys = sorted(E.keys())
ptof = {}   # var index -> ("P"/"Q", pt)
for (kind, pt), i in S.varof.items():
    ptof[i] = (kind, pt)

timeline = []
class LogList(list):
    def __init__(self, tag):
        super().__init__(); self.tag = tag
    def append(self, x):
        super().append(x); timeline.append((self.tag, x))

class C3P(Cascade3):
    """log pivot-source equations for eliminations and M2 forcing equations"""
    def _pick_pivot(self):
        r = super()._pick_pivot()
        if r is not None:
            timeline.append(("pick", r[2], dict(self.eqs[r[1]])))
        return r
    def _m1_m2(self):
        # copy of parent with force-source logging
        acted = False
        while True:
            neweqs, force = [], set()
            for c in self.eqs:
                if not c:
                    continue
                if len(c) == 1:
                    (m, k), = c.items()
                    if m == ():
                        self.status = "EMPTY"; return None
                    nonunits = [v for v in set(m) if v not in self.units]
                    if not nonunits:
                        self.status = "EMPTY"; return None
                    if len(nonunits) == 1:
                        force.add(nonunits[0])
                        timeline.append(("force", nonunits[0], dict(c)))
                        continue
                neweqs.append(c)
            self.eqs = neweqs
            if not force:
                return acted
            for v in sorted(force):
                self.eqs = [_kill_var(c, v) for c in self.eqs]
                self.zeroed.append(v)
                self.alive.discard(v)
                self.bvars.discard(v); self.avars.discard(v)
            self.eqs = [c for c in self.eqs if c]
            acted = True

C = C3P(S, level_dir=(2, 1))
C.zeroed = LogList("zero"); C.elim = LogList("elim")
t0 = time.time()
st = C.run()
print(f"[{name}] cascade: {st} ({time.time()-t0:.0f}s); "
      f"zeroed {len(C.zeroed)}, elim {len(C.elim)}, eqs left {len(C.eqs)}")
resid_b = sorted(C.bvars)
print("residual bvars:", [(C.varnames[v], ptof.get(v)) for v in resid_b])

def replay(eq, record=None):
    cur = {m: Fraction(k) for m, k in eq.items()}
    for ent in timeline:
        tag = ent[0]
        if tag == "zero":
            v = ent[1]
            if any(v in m for m in cur):
                cur = _kill_var(cur, v)
                if record is not None:
                    record.append(("zero", v))
        elif tag == "elim":
            v, g = ent[1]
            if any(v in m for m in cur):
                cur = C._subst_linear(cur, v, g)
                if record is not None:
                    record.append(("elim", v, len(g)))
    return cur

# provenance: which original equation was the pivot source of each elim/force
def provenance_pass():
    currents = {i: {m: Fraction(k) for m, k in S.equations[i].items()}
                for i in range(len(keys))}
    src_of = {}
    for ent in timeline:
        tag = ent[0]
        if tag in ("pick", "force"):
            v, eqc = ent[1], ent[2]
            hits = [i for i, c in currents.items() if c == eqc]
            src_of.setdefault(("elim" if tag == "pick" else "zero", v), hits)
        elif tag == "zero":
            v = ent[1]
            for i in currents:
                if any(v in m for m in currents[i]):
                    currents[i] = _kill_var(currents[i], v)
        else:
            v, g = ent[1]
            for i in currents:
                if any(v in m for m in currents[i]):
                    currents[i] = C._subst_linear(currents[i], v, g)
    return src_of

src_of = provenance_pass()
def fmt_src(kindv):
    hits = src_of.get(kindv, [])
    return ",".join(str(keys[i]) for i in hits) if hits else "?"
print("elim/zero pivot-source original keys (chronological):")
for ent in timeline:
    if ent[0] == "pick":
        v = ent[1]
        print(f"  elim {C.varnames[v]}{ptof[v][1]} <- eq{fmt_src(('elim', v))}", end=";")
    elif ent[0] == "force":
        v = ent[1]
        print(f"  ZERO {C.varnames[v]}{ptof.get(v,('?','?'))[1]} <- eq{fmt_src(('zero', v))}", end=";")
print()

# replay all original bracket equations through the cascade
t0 = time.time()
after_cascade = [replay(S.equations[i]) for i in range(len(keys))]
print(f"replayed {len(keys)} originals through cascade ({time.time()-t0:.0f}s)")
n_zero = sum(1 for c in after_cascade if not c)
print(f"identically zero after cascade: {n_zero}/{len(keys)}")

# provenance: match cascade survivors in C.eqs to original indices
prov = {}
for j, c in enumerate(C.eqs):
    hits = [i for i, r in enumerate(after_cascade) if r == c]
    if len(hits) == 1:
        prov[j] = hits[0]

# ---------------- instrumented two_chart (keep-empties clone) ----------------
def two_chart_tracked(C):
    invof = dict(C.invof); varnames = list(C.varnames)
    eqs = [dict(c) for c in C.eqs]; ids = list(range(len(eqs)))
    events = []
    for b in sorted(C.bvars):
        best = None
        for ei, c in enumerate(eqs):
            coeff, rest, ok = {}, {}, True
            for m, k in c.items():
                cnt = sum(1 for i in m if i == b)
                if cnt == 0: rest[m] = k
                elif cnt == 1: coeff[tuple(i for i in m if i != b)] = k
                else: ok = False; break
            if ok and coeff:
                key = (len(coeff), len(rest))
                if best is None or key < best[0]:
                    best = (key, ei, coeff, rest)
        if best is None: continue
        _, ei, coeff, rest = best
        u = len(varnames); varnames.append(f"u{u}")
        g = {}
        for m, k in rest.items():
            g = cadd(g, cmul({m: -k}, {(u,): Fraction(1)}))
        events.append((b, u, dict(coeff), dict(rest), g, ids[ei]))
        src = eqs[ei]
        eqs = [c for j, c in enumerate(eqs) if j != ei]
        ids = [x for j, x in enumerate(ids) if j != ei]
        out = []
        for c in eqs:   # keep empties to preserve id alignment
            if any(b in m for m in c):
                r = {}
                for m, k in c.items():
                    if b in m:
                        m2 = tuple(i for i in m if i != b)
                        r = cadd(r, cmul({m2: k}, g))
                    else:
                        r = cadd(r, {m: k})
                out.append(chartelim._invred(r, invof))
            else:
                out.append(c)
        eqs = out
        eqs.append(cadd(cmul({(u,): Fraction(1)}, coeff), {(): Fraction(-1)}))
        ids.append(("sat", varnames[b]))
    return events, varnames

# cross-check against the real two_chart
leafG, leafC, info = chartelim.two_chart(C)
events, cvn = two_chart_tracked(C)
assert [ (C.varnames[b], len(co)) for b,u,co,re_,g,src in events ] == info, "tracked != real"
print("chart pivots:", info)

def mstr(m, vn):
    out = []
    i = 0
    while i < len(m):
        e = 1
        while i + e < len(m) and m[i+e] == m[i]: e += 1
        out.append(vn[m[i]] + (f"^{e}" if e > 1 else ""))
        i += e
    return "*".join(out) if out else "1"

def cstr(c, vn, maxt=12):
    if not c: return "0"
    items = sorted(c.items())
    s = " + ".join(f"({k})*{mstr(m, vn)}" for m, k in items[:maxt])
    return s + (f" ... [{len(c)} terms]" if len(c) > maxt else "")

for b, u, coeff, rest, g, src in events:
    srckey = keys[prov[src]] if src in prov else src
    print(f"  chart pivot for {C.varnames[b]} {ptof[b]}: src eq = "
          f"{'original key '+str(srckey) if src in prov else src}, "
          f"|coeff|={len(coeff)}, |rest|={len(rest)}")
    print(f"    coeff = {cstr(coeff, cvn)}")
    print(f"    rest  = {cstr(rest, cvn, 6)}")
    # cascade history of the source equation
    if src in prov:
        rec = []
        replay(S.equations[prov[src]], rec)
        touch = [(t[0], C.varnames[t[1]], ptof.get(t[1])) for t in rec]
        print(f"    cascade events touching src ({len(touch)}):",
              [f"{t}:{n}{p[1] if p else ''}" for t, n, p in touch])

def replay_chart(cur, record=None):
    cur = dict(cur)
    for b, u, coeff, rest, g, src in events:
        if any(b in m for m in cur):
            r = {}
            for m, k in cur.items():
                if b in m:
                    m2 = tuple(i for i in m if i != b)
                    r = cadd(r, cmul({m2: k}, g))
                else:
                    r = cadd(r, {m: k})
            cur = chartelim._invred(r, C.invof)
            if record is not None:
                record.append((C.varnames[b], dict(cur)))
    return cur

# full census: originals through cascade + chart
census = {"zero": 0, "const": [], "poly": 0}
t0 = time.time()
for i, r in enumerate(after_cascade):
    f = replay_chart(r)
    if not f:
        census["zero"] += 1
    elif list(f.keys()) == [()]:
        census["const"].append((i, keys[i], f[()]))
    else:
        census["poly"] += 1
print(f"census after chart ({time.time()-t0:.0f}s): {census['zero']} identically zero, "
      f"{census['poly']} polynomial, constants: {census['const']}")

# pivot constants (for denominator-prime bookkeeping)
pcs = []
for ent in timeline:
    if ent[0] == "pick":
        v, eqc = ent[1], ent[2]
        ms = [m for m in eqc if v in m]
        pcs.append(eqc[ms[0]])
print("elim pivot constants:", sorted(set(pcs)))

# step-by-step collapse of eq 3 (open case) / the rhs-key equation generally
irhs = keys.index(spec["rhs"])
rec = []
r3 = dict(after_cascade[irhs])
print(f"rhs-key eq (index {irhs}) after cascade: {cstr(r3, C.varnames)}")
f3 = replay_chart(r3, rec)
for nm, state in rec:
    print(f"  after {nm} subst: {cstr(state, cvn)}")
print(f"final rhs-key eq: {cstr(f3, cvn)}")
