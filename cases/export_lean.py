"""Tier-1 Lean export: extract the 10-event collapse of original key (3,6)
for open_8_28_c2 and emit lean/Jc/Culprit.lean.

Identity (B): orig_(3,6), after the recorded eliminations (hypotheses
v = g_v for the 7 elims, v = 0 for the 3 zeroings), equals
(-1/5)*a2^2*a6*ia1^2*b3 modulo the unit relations iv*v = 1.

We verify (B) here symbolically, compute the linear_combination cofactors
for the unit relations, and write the Lean file.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
sys.path.insert(0, os.path.dirname(__file__))
from fractions import Fraction
from jc import SystemA, cadd, cmul, bracket, padd
from emit import CASES, FIX
from reduce3 import Cascade3
from reduce import _kill_var

name = "open_8_28_c2"
spec = CASES[name]
S = SystemA(name, spec["cornersP"], spec["cornersQ"], spec["rhs"],
            nonvanish="nonorigin", fix_ones=FIX[name])

def coef(kind, pt):
    return {(): 1} if (kind, pt) in S.fix else {(S.varof[(kind, pt)],): 1}
E = padd(bracket({p: coef("P", p) for p in S.ptsP},
                 {q: coef("Q", q) for q in S.ptsQ}), {spec["rhs"]: {(): -1}})
keys = sorted(E.keys())

timeline = []
class LogList(list):
    def __init__(self, tag):
        super().__init__(); self.tag = tag
    def append(self, x):
        super().append(x); timeline.append((self.tag, x))

C = Cascade3(S, level_dir=(2, 1))
C.zeroed = LogList("zero"); C.elim = LogList("elim")
st = C.run()
assert st == "reduced", st
vn = C.varnames

# ---- replay orig key (3,6), recording the events that touch it -------------
i36 = keys.index((3, 6))
orig = {m: Fraction(k) for m, k in S.equations[i36].items()}
events = []          # ("zero", v) or ("elim", v, g)  in chronological order
cur = dict(orig)
for ent in timeline:
    tag = ent[0]
    if tag == "zero":
        v = ent[1]
        if any(v in m for m in cur):
            cur = _kill_var(cur, v)
            events.append(("zero", v, None))
    elif tag == "elim":
        v, g = ent[1]
        if any(v in m for m in cur):
            cur = C._subst_linear(cur, v, g)
            events.append(("elim", v, {m: Fraction(k) for m, k in g.items()}))
final = cur
print("events:", [(t, vn[v]) for t, v, _ in events])
print("final:", final)
tgt = {tuple(sorted([S.varof[("P",(1,1))]]*2 + [S.varof[("P",(2,4))],
        C.invof[S.varof[("P",(1,0))]], C.invof[S.varof[("P",(1,0))]],
        S.varof[("Q",(2,1))]])): Fraction(-1, 5)}
assert final == tgt, (final, tgt)
print("final == (-1/5)*a2^2*a6*ia1^2*b3  OK")

# ---- verify identity WITHOUT inv-reduction, computing unit cofactors -------
# plain substitution (no _inv_reduce):
def subst_plain(c, v, g):
    out = {}
    for m, k in c.items():
        if v in m:
            assert m.count(v) == 1
            m2 = tuple(i for i in m if i != v)
            out = cadd(out, cmul({m2: k}, g))
        else:
            out = cadd(out, {m: k})
    return {m: k for m, k in out.items() if k}

cur = dict(orig)
for tag, v, g in events:
    cur = subst_plain(cur, v, g if tag == "elim" else {})
# D := cur - tgt must lie in ideal (iv*v - 1 : pairs).  Reduce, track cofactors.
D = cadd(cur, {m: -k for m, k in tgt.items()})
D = {m: k for m, k in D.items() if k}
inv_pairs = sorted(set(  # (base var, inverse var) with base < inverse index
    (min(i, C.invof[i]), max(i, C.invof[i]))
    for m in list(D) for i in m if i in C.invof))
cof = {}                 # (b, iv) -> cofactor poly
changed = True
while changed:
    changed = False
    for m, k in sorted(D.items()):
        for b, iv in inv_pairs:
            if b in m and iv in m:
                m2 = list(m); m2.remove(b); m2.remove(iv)
                m2 = tuple(m2)
                # k*m = k*m2*(b*iv - 1) + k*m2
                cof[(b, iv)] = cadd(cof.get((b, iv), {}), {m2: k})
                D = cadd(D, {m: -k, m2: k})
                D = {mm: kk for mm, kk in D.items() if kk}
                changed = True
                break
        if changed:
            break
assert not D, D
print("unit-relation cofactors:", {(vn[b], vn[iv]): c for (b, iv), c in cof.items()})

# unit relations of the generic-chart localization: state them as hypotheses
# whether or not the reduction consumed them (ia1 backs the cascade pivots,
# ib43 the vacuous chart pivot; cf. LEMMA.md §2 step 4, AUDIT.md prod(pivots)).
va1 = S.varof[("P", (1, 0))]
vb43 = S.varof[("Q", (12, 21))]
unit_pairs = sorted(set(inv_pairs) |
                    {(min(v, C.invof[v]), max(v, C.invof[v])) for v in (va1, vb43)})

# ---- name map & free variables --------------------------------------------
ptof = {i: (kind, pt) for (kind, pt), i in S.varof.items()}
def lname(i):
    return vn[i]                      # a1, b3, ia1, ... already good Lean ids

used = set()
def scan(c):
    for m in c:
        used.update(m)
scan(orig); scan(tgt)
for _, v, g in events:
    if g: scan(g)
for c in cof.values(): scan(c)
for b, iv in unit_pairs:
    used.add(b); used.add(iv)
elimvars = [v for _, v, _ in events]
freevars = sorted(used - set(elimvars))
print("eliminated:", [lname(v) for v in elimvars])
print("free:", [(lname(v), ptof.get(v) or ("inv", vn[C.invof[v]])) for v in freevars])

# ---- emit Lean -------------------------------------------------------------
def lmon(m):
    out = []
    i = 0
    while i < len(m):
        e = 1
        while i + e < len(m) and m[i + e] == m[i]:
            e += 1
        out.append(lname(m[i]) + (f"^{e}" if e > 1 else ""))
        i += e
    return "*".join(out) if out else "1"

def lpoly(c):
    if not c:
        return "0"
    terms = []
    for m, k in sorted(c.items()):
        assert k.denominator >= 1
        kk = f"({k.numerator}/{k.denominator})" if k.denominator != 1 else f"({k.numerator})"
        terms.append(f"{kk}*{lmon(m)}" if m else f"{kk}")
    return " + ".join(terms)

lines = []
w = lines.append
w("import Mathlib.Tactic.LinearCombination")
w("import Mathlib.Tactic.Ring")
w("")
w("/-!  Tier-1 machine check for LEMMA.md (open_8_28_c2, generic chart).")
w("")
w("Generated by cases/export_lean.py from the recorded Cascade3 event log")
w("(cases/eq3_chain.py machinery).  Variables are named as in LEMMA.md:")
w("`aN`/`bN` are the P/Q coefficient unknowns, `iaN` the formal localization")
w("inverse of `aN`.")
w("-/")
w("")
w("/-- (A) the final substitution: the untouched vertex equation")
w("`eq #3 = a1*b3 - 1` evaluates at `b3 = 0` to the unit `-1`.")
w("A plain commutative-ring identity. -/")
w("theorem eq3_at_b3_zero {K : Type*} [CommRing K] (a1 b3 : K) (h : b3 = 0) :")
w("    a1*b3 - 1 = -1 := by subst h; ring")
w("")
w("set_option linter.unusedVariables false in  -- hu1/hu2 stated, not consumed")
w("/-- (B) the culprit reduction: the original key-(3,6) bracket coefficient,")
w("after the 10 recorded collapse events (3 zeroings, 7 unit-pivot")
w("eliminations, hypotheses `h1`..`h10` in chronological order), equals the")
w("single monomial `(-1/5)*a2^2*a6*ia1^2*b3` in the localized ring of the")
w("generic chart: `hu1`/`hu2` are the adjoined unit relations `ia1*a1 = 1`,")
w("`ib43*b43 = 1` under which that ring lives.  The closing `ring` does not")
w("in fact consume `hu1`/`hu2` — `a1` and `b43` never occur in the chain, so")
w("the identity already holds in the free (polynomial) commutative ring,")
w("which is strictly stronger and specializes to the localization")
w("`Q[a,b][ia1,ib43]/(ia1*a1-1, ib43*b43-1)` of LEMMA.md.  Stated over a")
w("field of characteristic 0 so the literal rational coefficients elaborate;")
w("the denominators are exactly the pivot-constant primes {2,3,5} (LEMMA.md")
w("denominator hygiene). -/")
hyps = []
hn = 0
for tag, v, g in events:
    hn += 1
    rhs = "0" if tag == "zero" else lpoly(g)
    hyps.append((f"h{hn}", f"{lname(v)} = {rhs}"))
un = 0
unit_hyps = []
for b, iv in unit_pairs:
    un += 1
    unit_hyps.append((f"hu{un}", f"{lname(iv)}*{lname(b)} = 1", (b, iv)))

w("theorem culprit_key36_reduction {K : Type*} [Field K] [CharZero K]")
w(f"    ({' '.join(lname(v) for v in freevars)}")
w(f"     {' '.join(lname(v) for v in elimvars)} : K)")
for nm, s, _ in unit_hyps:
    w(f"    ({nm} : {s})")
for nm, s in hyps:
    w(f"    ({nm} : {s})")
w(f"    : {lpoly(orig)}")
w(f"      = {lpoly(tgt)} := by")
w("  subst " + " ".join(nm for nm, _ in hyps))
lc = " + ".join(f"({lpoly(cof[key])}) * {nm}" for nm, _, key in unit_hyps
                if key in cof and cof[key])
w(f"  linear_combination {lc}" if lc else "  ring")
w("")

out = os.path.join(os.path.dirname(__file__), "..", "lean", "Jc", "Culprit.lean")
with open(out, "w") as f:
    f.write("\n".join(lines))
print(f"wrote {out} ({len(lines)} lines)")
