"""Branch-complete elimination of the residual b-variables from a Cascade3 core.

Each remaining b occurs linearly.  To eliminate b via equation  c(a)*b + rest = 0
we split completely:
   branch INV : c invertible  -> adjoin u with u*c = 1, substitute b = -u*rest
   branch ZERO: c = 0         -> adjoin the equation c = 0 and retry with a
                                 different pivot equation for this b (or leave b
                                 free if no equation mentions it any more)
The leaves partition the original (corner-saturated) variety, so:
   original empty  <=>  every leaf system is empty.
Leaves live in the a-variables (+ units/inverses + branch inverses) only.
"""
from fractions import Fraction
from jc import cadd, cmul

MAXBRANCH = 200

class Leaf:
    def __init__(self, eqs, varnames, alive, note):
        self.eqs, self.varnames, self.alive, self.note = eqs, varnames, alive, note

def _subst_linear(eqs, v, g, invof):
    out = []
    for c in eqs:
        if any(v in m for m in c):
            r = {}
            for m, k in c.items():
                if v in m:
                    m2 = tuple(i for i in m if i != v)
                    r = cadd(r, cmul({m2: k}, g))
                else:
                    r = cadd(r, {m: k})
            out.append(_invred(r, invof))
        else:
            out.append(c)
    return [c for c in out if c]

def _invred(c, invof):
    out = {}
    for m, k in c.items():
        cnt = {}
        for i in m:
            cnt[i] = cnt.get(i, 0) + 1
        for i in list(cnt):
            j = invof.get(i)
            if j is not None and j in cnt and j > i:
                d = min(cnt[i], cnt[j])
                cnt[i] -= d
                cnt[j] -= d
        mm = tuple(sorted(i for i, e in cnt.items() for _ in range(e)))
        out = cadd(out, {mm: k})
    return out

def two_chart(C):
    """Exact 2-piece decomposition:
       V(core) = V(generic leaf: all chosen pivots inverted)  ∪  V(core + prod(pivots)=0)
    Returns (leafG, leafC, pivot_info)."""
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
            for m, k in c.items():
                cnt = sum(1 for i in m if i == b)
                if cnt == 0:
                    rest[m] = k
                elif cnt == 1:
                    coeff[tuple(i for i in m if i != b)] = k
                else:
                    ok = False
                    break
            if ok and coeff:
                key = (len(coeff), len(rest))
                if best is None or key < best[0]:
                    best = (key, ei, coeff, rest)
        if best is None:
            continue                        # b no longer occurs
        _, ei, coeff, rest = best
        u = len(varnames)
        varnames.append(f"u{u}")
        g = {}
        for m, k in rest.items():
            g = cadd(g, cmul({m: -k}, {(u,): Fraction(1)}))
        eqs = [c for j, c in enumerate(eqs) if j != ei]
        eqs = _subst_linear(eqs, b, g, invof)
        eqs.append(cadd(cmul({(u,): Fraction(1)}, coeff), {(): Fraction(-1)}))
        alive.add(u)
        alive.discard(b)
        prod = cmul(prod, coeff)
        info.append((C.varnames[b], len(coeff)))
    leafG = Leaf(eqs, varnames, alive, "generic:" + ",".join(n for n, _ in info))
    eqsC = [dict(c) for c in C.eqs] + [prod]
    leafC = Leaf(eqsC, list(C.varnames), set(C.alive), "complement")
    return leafG, leafC, info

def eliminate_bs(C):
    """C: a finished reduce3.Cascade3. Returns list of Leaf."""
    leaves, work = [], []
    invof = dict(C.invof)
    varnames = list(C.varnames)
    state0 = ([dict(c) for c in C.eqs], sorted(C.bvars), set(C.alive), "root")
    work.append(state0)
    while work:
        if len(leaves) + len(work) > MAXBRANCH:
            raise RuntimeError("branch explosion")
        eqs, bs, alive, note = work.pop()
        # find a b with a usable pivot equation
        target, pivot = None, None
        for b in bs:
            cands = []
            for ei, c in enumerate(eqs):
                ms = [m for m in c if b in m]
                if not ms:
                    continue
                if len(ms) == 1 and sum(1 for i in ms[0] if i == b) == 1:
                    coeff = {tuple(i for i in ms[0] if i != b): c[ms[0]]}
                    # full coefficient of b in this equation (may span monomials)
                # collect complete linear coefficient of b in eq
            # build full coefficient/rest split for each equation containing b
            for ei, c in enumerate(eqs):
                coeff, rest = {}, {}
                ok = True
                for m, k in c.items():
                    cnt = sum(1 for i in m if i == b)
                    if cnt == 0:
                        rest[m] = k
                    elif cnt == 1:
                        coeff[tuple(i for i in m if i != b)] = k
                    else:
                        ok = False
                        break
                if ok and coeff:
                    cands.append((len(coeff) + len(rest), ei, coeff, rest))
            if cands:
                cands.sort(key=lambda x: x[0])
                target, pivot = b, cands[0]
                break
        if target is None:
            # no b appears any more (all fell out) -> leaf in a-space
            leaves.append(Leaf(eqs, varnames, alive, note))
            continue
        _, ei, coeff, rest = pivot
        b = target
        # ----- branch ZERO: coeff = 0 adjoined, pivot equation becomes rest = 0
        eqsZ = [dict(c) for c in eqs]
        eqsZ[ei] = dict(rest) if rest else {}
        eqsZ.append(dict(coeff))
        eqsZ = [c for c in eqsZ if c]
        work.append((eqsZ, bs, set(alive), note + f"|{varnames[b]}:Z"))
        # ----- branch INV: adjoin u*coeff = 1, b := -u*rest
        u = len(varnames)
        varnames.append(f"u{len(varnames)}")
        invC = dict(coeff)
        g = {}
        for m, k in rest.items():
            g = cadd(g, cmul({m: -k}, {(u,): Fraction(1)}))
        eqsI = [c for j, c in enumerate(eqs) if j != ei]
        eqsI = _subst_linear(eqsI, b, g, invof)
        sat = cadd(cmul({(u,): Fraction(1)}, invC), {(): Fraction(-1)})
        eqsI.append(sat)
        aliveI = set(alive) | {u}
        aliveI.discard(b)
        bsI = [x for x in bs if x != b]
        work.append((eqsI, bsI, aliveI, note + f"|{varnames[b]}:I"))
    return leaves

def leaf_to_msolve(leaf, path, char):
    import math
    names = {}
    used = sorted({i for c in leaf.eqs for m in c for i in m})
    for v in used:
        names[v] = leaf.varnames[v]
    strs = []
    for c in leaf.eqs:
        den = 1
        for k in c.values():
            den = den * k.denominator // math.gcd(den, k.denominator)
        cc = {m: int(k * den) for m, k in c.items()}
        terms = []
        for m in sorted(cc):
            k = cc[m]
            parts = []
            i = 0
            while i < len(m):
                e = 1
                while i + e < len(m) and m[i + e] == m[i]:
                    e += 1
                parts.append(names[m[i]] if e == 1 else f"{names[m[i]]}^{e}")
                i += e
            ms = "*".join(parts)
            if ms == "":
                terms.append(f"{'+' if k>0 else '-'}{abs(k)}")
            elif abs(k) == 1:
                terms.append(f"{'+' if k>0 else '-'}{ms}")
            else:
                terms.append(f"{'+' if k>0 else '-'}{abs(k)}*{ms}")
        s = "".join(terms)
        strs.append(s[1:] if s.startswith("+") else s)
    with open(path, "w") as f:
        f.write(",".join(names[v] for v in used) + "\n")
        f.write(f"{char}\n")
        f.write(",\n".join(strs) + "\n")
    return len(used), len(strs)
