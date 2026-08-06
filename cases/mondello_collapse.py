"""Run the vertex-gap collapse machinery over Q on Mondello's polygon data
(arXiv:2608.02634) and log every pivot constant, to locate the exact char-2
failure.  Generic coefficients on the exact support:
  P = a1 x + a2 x^2 y + a3 x^4 + a4 x^6 y^2
  Q = b0 y + b1 x^5 + b2 x^6 y + b3 x^7 y^2 + b4 x^8 y^3
System: [P,Q] = 1 (Keller), corners a1, b0 saturated (vertex eq a1 b0 = 1).
Machinery: level-ordered M2 zeroings / unit-pivot eliminations exactly as in
LEMMA.md sec.2 / SURPLUS.md Prop. B, over Q; every division is recorded.
Run:  python3 cases/mondello_collapse.py
"""
import sys, os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
import jc

if "hull" in sys.argv[1:]:   # generic member of the full Newton polygons
    HP = jc.lattice_points([(0, 0), (4, 0), (6, 2), (2, 1)])
    HQ = jc.lattice_points([(0, 0), (5, 0), (8, 3), (0, 1)])
    SUPP_P = {m: "a%d_%d" % m for m in HP if m != (0, 0)}
    SUPP_Q = {m: "b%d_%d" % m for m in HQ if m != (0, 0)}
    SUPP_P[(1, 0)] = "a1"
    SUPP_Q[(0, 1)] = "b0"
else:                        # Mondello's exact support
    SUPP_P = {(1, 0): "a1", (2, 1): "a2", (4, 0): "a3", (6, 2): "a4"}
    SUPP_Q = {(0, 1): "b0", (5, 0): "b1", (6, 1): "b2", (7, 2): "b3",
              (8, 3): "b4"}
P = {m: {(s,): 1} for m, s in SUPP_P.items()}
Q = {m: {(s,): 1} for m, s in SUPP_Q.items()}

BR = jc.bracket(P, Q)
RHS = {(0, 0): {(): 1}}
EQS = jc.padd(BR, jc.pneg(RHS))          # every key must vanish

print("System [P,Q] - 1 = 0 on Mondello supports: %d keys" % len(EQS))
for key in sorted(EQS, key=lambda k: (k[0] + k[1], k)):   # level l = i+j (d=(1,1))
    print("  key %-7s:" % (key,), jc_str(EQS[key]) if False else
          " + ".join("%d*%s" % (v, "*".join(m) if m else "1")
                     for m, v in sorted(EQS[key].items())))

# ------------------------------------------------- machinery elimination over Q
# state: values[sym] = Coef-dict (polynomial in remaining syms, Fraction values)
UNITS = {"a1", "b0"}
values = {}          # substitutions
pivots = []          # (step, eq_key, pivot_int, action)

def cancel(mon):
    """cancel a1*ia1 pairs inside a monomial tuple."""
    mon = list(mon)
    while "a1" in mon and "ia1" in mon:
        mon.remove("a1")
        mon.remove("ia1")
    return tuple(mon)

def csub1(c, values):
    """one substitution pass of values (sym -> Coef) into Coef c."""
    out = {}
    for mon, v in c.items():
        term = {(): Fraction(v)}
        for s in mon:
            term = jc.cmul(term, values.get(s, {(s,): Fraction(1)}))
        red = {}
        for m, w in term.items():
            m = cancel(m)
            red[m] = red.get(m, 0) + w
        out = jc.cadd(out, {m: w for m, w in red.items() if w})
    return out

def csub(c, values):
    """substitute to fixpoint (definitions may reference later-set symbols)."""
    for _ in range(len(values) + 2):
        nxt = csub1(c, values)
        if nxt == c:
            return c
        c = nxt
    return c

def show(c):
    return " + ".join("%s*%s" % (v, "*".join(m) if m else "1")
                      for m, v in sorted(c.items())) or "0"

# vertex normalization first: key (0,0) is det((1,0),(0,1)) a1 b0 - 1
vkey = (0, 0)
print("\nVertex equation, key (0,0):", show(EQS[vkey]),
      "  -> normalization b0 := 1/a1 (det = +1, ODD - survives char 2)")
values["b0"] = {("ia1",): Fraction(1)}   # ia1 = 1/a1, unit
pivots.append(("V", vkey, +1, "b0 := ia1 (vertex normalization)"))

work = {k: EQS[k] for k in EQS if k != vkey}
step = 0
changed = True
while changed:
    changed = False
    for key in sorted(work, key=lambda k: (k[0] + k[1], k)):
        c = csub(work[key], values)
        c = {m: v for m, v in c.items() if v}
        if not c:
            continue
        # M2: single monomial, exactly one non-unit symbol (with multiplicity 1)
        if len(c) == 1:
            (mon, v), = c.items()
            nonunits = [s for s in mon if s not in UNITS and s != "ia1"
                        and s not in values]
            if len(set(nonunits)) == 1:
                s = nonunits[0]
                mult = mon.count(s)
                step += 1
                values[s] = {}
                pivots.append((step, key, v, "M2 zero: %s := 0 (pivot %s%s)"
                               % (s, v, ", radical deg %d" % mult
                                  if mult > 1 else "")))
                changed = True
                continue
        # linear elimination: some free sym appears in exactly one monomial, deg 1
        syms = {}
        for mon, v in c.items():
            for s in set(mon):
                if s not in UNITS and s != "ia1" and s not in values:
                    syms.setdefault(s, []).append(mon)
        for s, mons in syms.items():
            if len(mons) == 1 and mons[0].count(s) == 1 and len(c) > 1:
                mon = mons[0]
                piv = c[mon]
                cof = tuple(x for x in mon if x != s)  # unit cofactor required
                if all(x in UNITS or x == "ia1" for x in cof):
                    rest = {m: v for m, v in c.items() if m != mon}
                    icof = tuple("ia1" if x == "a1" else "a1" if x == "ia1"
                                 else x for x in cof)   # invert unit cofactor
                    expr = {}
                    for m, v in rest.items():
                        expr[tuple(sorted(m + icof))] = Fraction(-v, piv)
                    step += 1
                    values[s] = expr
                    pivots.append((step, key, piv,
                                   "eliminate %s (pivot %d): %s := %s"
                                   % (s, piv, s, show(expr))))
                    changed = True
                    break
        if changed:
            break

print("\n--- elimination log (over Q) ---")
for st, key, piv, act in pivots:
    print("  [%s] key %-7s pivot %+d %s  %s"
          % (st, key, piv, "(EVEN -> dies in char 2)" if piv % 2 == 0 else
             "(odd  -> survives char 2)", act))

print("\n--- final state over Q ---")
allsyms = sorted(set(SUPP_P.values()) | set(SUPP_Q.values()) - {"a1", "b0"})
for s in allsyms:
    if s in values:
        print("  %s = %s" % (s, show(csub({(s,): 1}, values))))
    else:
        print("  %s (free)" % s)
res = []
for key in sorted(work, key=lambda k: (k[0] + k[1], k)):
    c = {m: v for m, v in csub(work[key], values).items() if v}
    if c:
        res.append((key, show(c)))
print("residual equations:", res if res else "NONE - system fully collapsed")

# --------------------------------------------- char-2 comparison, per equation
print("\n--- same equations mod 2 (Mondello's escape) ---")
for key in sorted(EQS, key=lambda k: (k[0] + k[1], k)):
    c2 = {m: v % 2 for m, v in EQS[key].items() if v % 2}
    tag = "IDENTICALLY 0 mod 2" if not c2 else show(c2)
    print("  key %-7s mod 2: %s" % (key, tag))
