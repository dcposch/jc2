"""GGV5 (arXiv:1708.07936) family enumeration -- Phase 1 of SECTION4-AUTOMATION.md.

Data structures for standard (m,n)-pair families and the corner data the
S4 reduction engine (Phase 2) consumes, plus a faithful port of the GGV5
generation pipeline:

  Algorithm 1  GetPossibleLastLowerCorners   (PLLC)
  Algorithm 2  GetStartingEdges
  Algorithm 3  GetGeneratedCorners
  Algorithm 4  GetCornerChildrenList
  Algorithm 5  GetChildrenAndFinalList
  Algorithm 6  GetCompleteChains
  Algorithm 7  GetIsAdmissible               (divisibility conditions, Def 2.30)
  Algorithm 8  Main algorithm
  Algorithm 9  GetmnFamilies                 (+ the (q_k) machinery, eq. (q_k))

Everything is exact integer / Fraction lattice arithmetic (JC_BACKEND-agnostic;
no dependency on lib/jc.py's coefficient backends).

Conventions (match GGV5 and SECTION4-AUTOMATION.md):
  corner  A = (a %% l, b)  <-> geometric point (a/l, b), stored Corner(a, l, b);
  v_{rho,sigma}(A) = rho*a/l + sigma*b;
  dir(v) for v = (v1, v2), v2 > 0: the coprime (rho, sigma) with
      rho*v1 + sigma*v2 = 0 and rho > 0;
  order on directions: (r1,s1) < (r2,s2)  iff  r1*s2 - s1*r2 > 0
      (counterclockwise sweep, valid on the used arc [(0,-1) .. (1,0]]).
"""
from fractions import Fraction
from math import gcd
from collections import namedtuple

# ---------------------------------------------------------------- core lattice

Corner = namedtuple("Corner", "a l b")     # geometric point (a/l, b)
Edge = namedtuple("Edge", "A Ap")          # (A, A') with A upper, A' lower
Chain = namedtuple("Chain", "edges final") # edges: tuple[Edge]; final: Corner
Family = namedtuple("Family", "k i m0 n0 d1 d2")  # (m,n) = (m0+j*d1, n0+j*d2)

def C1(a, b):
    "integral corner (a, b)"
    return Corner(a, 1, b)

def cx(A):
    "geometric x coordinate a/l"
    return Fraction(A.a, A.l)

def geom(A):
    return (cx(A), A.b)

def vdir(rho, sigma, A):
    "v_{rho,sigma}(A) as an exact Fraction"
    return Fraction(rho * A.a, A.l) + sigma * A.b

def v11(A):
    return vdir(1, 1, A)

def v1m1_sign(A):
    "sign of v_{1,-1}(A) = a/l - b, as the integer a - b*l"
    return A.a - A.b * A.l

def dir_of(v1num, v2, l=1):
    """dir of the vector (v1num/l, v2), v2 > 0 in every use here: the coprime
    (rho, sigma) with rho*v1 + sigma*v2 = 0, normalized rho > 0."""
    p, q = v1num, v2 * l           # direction orthogonal to (p/l, v2) ~ (p, q)
    g = gcd(abs(p), abs(q))
    rho, sigma = q // g, -p // g
    if rho < 0 or (rho == 0 and sigma > 0):
        rho, sigma = -rho, -sigma
    assert rho > 0, (v1num, v2, l)
    return rho, sigma

def edge_dir(e):
    "dir(A - A') for an edge (both corners share l)"
    A, Ap = e
    assert A.l == Ap.l and A.b > Ap.b
    return dir_of(A.a - Ap.a, A.b - Ap.b, A.l)

def dir_lt(d1, d2):
    "(rho1,sigma1) < (rho2,sigma2) in the direction order"
    return d1[0] * d2[1] - d1[1] * d2[0] > 0

def pq_of(rho, sigma, A):
    """The (p, q) of GGV5 eq. (q_k) / Remark 2.29:  p/q = (rho+sigma)/v_{rho,
    sigma}(A) in lowest terms.  Integer v gives the printed formulas
    p = (rho+sigma)/g, q = v/g with g = gcd(rho+sigma, v); the Fraction form
    also covers chain corners with non-integer v (e.g. (16/3,10) at (2,-1))."""
    v = vdir(rho, sigma, A)
    assert v > 0, (rho, sigma, A)
    f = Fraction(rho + sigma, 1) / v
    return f.numerator, f.denominator

def num_factors(n):
    "Omega(n): number of prime factors counted with multiplicity"
    assert n >= 1
    cnt, d = 0, 2
    while d * d <= n:
        while n % d == 0:
            n //= d
            cnt += 1
        d += 1
    return cnt + (1 if n > 1 else 0)

# ------------------------------------------- Algorithm 1: possible last lower
# corners.  PLLC = dict (a,b) -> best direction (rho,sigma)_{a,b}.

def get_pllc(xmax):
    """GetPossibleLastLowerCorners(xmax): all possible last lower corners (a,b)
    with a <= xmax.  b-range b < a and b <= (a-b-1)^2 (integer-exact form of
    the paper's b <= (2a - sqrt(4a-3) - 1)/2)."""
    pfl = []       # ((r,s), (rho,sigma)_{r,s}) in insertion order
    pllc = {}
    for a in range(1, xmax + 1):
        b = 0
        while b < a and b <= (a - b - 1) ** 2:
            if b == 0:
                d = (0, -1)
                pfl.append(((a, b), d)); pllc[(a, b)] = d
            elif a > 2 * b > 0:
                d = (1, -2)
                pfl.append(((a, b), d)); pllc[(a, b)] = d
            else:
                best = (1, -1)
                for (r, s), drs in pfl:
                    if not (r < a and s < b and r - s < a - b):
                        continue
                    n1 = gcd(a - r, b - s)
                    n2 = gcd(r, s)
                    rho, sigma = (b - s) // n1, (r - a) // n1
                    v = rho * a + sigma * b
                    if v < rho:                       # v_{rho,sigma}(a,b) >= rho
                        continue
                    if not (dir_lt(drs, (rho, sigma))
                            and dir_lt((rho, sigma), best)):
                        continue
                    g = gcd(abs(rho + sigma), v)
                    tbar = v // g
                    if tbar <= n1 or (n2 % tbar == 0):
                        best = (rho, sigma)
                if dir_lt(best, (1, -1)):
                    pfl.append(((a, b), best)); pllc[(a, b)] = best
            b += 1
    return pllc

# ------------------------------------------------ Algorithm 2: starting edges

def get_starting_edges(a, b, pllc):
    """GetStartingEdges((a,b), PLLC): all valid edges (A, A') with A = (a,b),
    a < b (l = 1 at chain start).

    Extra guard vs the printed pseudocode: an edge with v_{1,-1}(A') > 0 is of
    type II.b), and for a standard (m,n)-pair a type II.b) regular corner
    cannot have direction (1,0) (GGV5, proof of Theorem 2.19: "This implies
    that (rho_t,sigma_t) != (1,0), because (P,Q) is standard"; rho = 1 in I
    forces (1,0)).  Without it, vertical first edges such as ((6,18),(6,0)) or
    ((9,27),(9,0)) spawn shadow chains absent from the GGV5 S5/S6 tables."""
    assert a < b
    d = gcd(a, b)
    A = C1(a, b)
    out = []
    for mu in range(1, d):
        f1, f2 = mu * (a // d), mu * (b // d)       # enF = (mu/d)(a,b)
        rho, sigma = dir_of(f1 - 1, f2 - 1)         # dir(enF - (1,1)); f2 >= 2
        for i in range(1, b // rho + 1):
            ap, bp = a + i * sigma, b - i * rho     # A' = A - i(-sigma, rho)
            v = ap - bp
            if v < 0 or (v > 0 and (rho, sigma) != (1, 0) and (ap, bp) in pllc):
                out.append(Edge(A, C1(ap, bp)))
    return out

# --------------------------------------------- Algorithm 3: generated corners

def _edge_f2(e, rho, sigma):
    "v_01(enF) for the edge form enF = (mu/d) A with v_{rho,sigma}(enF)=rho+sigma"
    A = e.A
    f2 = A.b * Fraction(rho + sigma, 1) / vdir(rho, sigma, A)   # = mu*b/d
    assert f2.denominator == 1, (e, rho, sigma)
    return int(f2)

def is_simple(e, rho=None, sigma=None):
    "Definition 2.5: v_01(enF) - 1 = gap(rho,l) and (gap > 1 or v_01(A') > 0)"
    if rho is None:
        rho, sigma = edge_dir(e)
    gap = rho // gcd(rho, e.A.l)
    return _edge_f2(e, rho, sigma) - 1 == gap and (gap > 1 or e.Ap.b > 0)

def get_generated_corners(e):
    """GetGeneratedCorners(A, A'): corners generated by a valid edge.  Faithful
    to Definitions 2.6-2.8 (admissibility of A_(gamma) checked in the simple
    branch as well -- Definition 2.8 requires it; the pseudocode elides it as
    automatic)."""
    A, Ap = e
    if v1m1_sign(Ap) < 0:
        return [Ap]
    rho, sigma = edge_dir(e)
    l = A.l
    l1 = l * rho // gcd(l, rho)                    # lcm(rho, l)
    gap = rho // gcd(rho, l)
    assert (A.b - Ap.b) % gap == 0
    gmax = min((A.b - Ap.b) // gap, A.b - 1)
    gammas = [gmax] if is_simple(e, rho, sigma) else range(Ap.b + 1, gmax + 1)
    out = []
    for b1 in gammas:
        if b1 < 1:
            continue
        a1 = A.a * (l1 // l) + (b1 - A.b) * (-sigma) * (l1 // rho)
        A1 = Corner(a1, l1, b1)
        if v1m1_sign(A1) < 0 and (l1 * b1 - a1 > b1 or gcd(a1, b1) > 1):
            out.append(A1)                         # Definition 2.6 admissible
    return out

# ----------------------------------------------- Algorithm 4: corner children

def get_corner_children(e, A1, pllc):
    """GetCornerChildrenList((A,A'), A1): all children (A1, A1') of the valid
    edge (A, A') at the generated corner A1."""
    rho, sigma = edge_dir(e)
    a1, l1, b1 = A1
    d1 = gcd(a1, b1)
    if d1 == 1:
        return []
    lo_f = 1 + Fraction(d1 * (rho + sigma), 1) / vdir(rho, sigma, A1)
    lo = lo_f.numerator // lo_f.denominator         # floor
    hi = d1 if l1 == 1 else l1 * (b1 * l1 - a1) + d1 // b1
    out = []
    for mu in range(max(lo, 1), hi + 1):
        if mu % d1 == 0:                            # need d1 does not divide mu
            continue
        fa, fb = mu * (a1 // d1), mu * (b1 // d1)   # enF = (mu/d1) A1
        if fb <= 1:                                 # Remark 2.3: f2 > 1 forced
            continue
        rho1, sigma1 = dir_of(fa - l1, fb - 1, l1)
        if sigma1 > 0:                              # (rho1,sigma1) must lie in I
            continue
        g1 = gcd(rho1, l1)
        gap = rho1 // g1
        if gap > b1:
            continue
        for j in range(1, b1 // gap + 1):
            a1p = a1 + j * sigma1 * (l1 // g1)
            b1p = b1 - j * gap
            assert a1p >= 1
            Ap1 = Corner(a1p, l1, b1p)
            v = v1m1_sign(Ap1)
            if l1 > 1:
                ok = v != 0
            else:
                ok = v < 0 or (v > 0 and (a1p, b1p) in pllc)
            if ok:
                out.append(Edge(A1, Ap1))
    return out

# --------------------------------- Algorithm 5: children + final corners of e

def is_final(A):
    "Definition 2.11: l - a/b > 1"
    return A.b >= 1 and A.l * A.b - A.a > A.b

def get_children_and_finals(e, pllc, _memo={}):
    key = e
    if key in _memo:
        return _memo[key]
    children, finals = [], []
    for A1 in get_generated_corners(e):
        if is_final(A1):
            finals.append(A1)
        # children are computed for final corners too: intermediate chain
        # corners may satisfy the final-corner inequality (e.g. (16/3,10) in
        # the deg<=150 length-3 chain)
        children.extend(get_corner_children(e, A1, pllc))
    _memo[key] = (children, finals)
    return children, finals

# ------------------------------------------------ Algorithm 6: complete chains

def get_complete_chains(e0, pllc):
    """GetCompleteChains(C0): complete chains starting at the valid edge C0,
    length bounded by NumberOfFactors(gcd(b, (b-b')/rho)) + 1."""
    rho, _ = edge_dir(e0)
    assert (e0.A.b - e0.Ap.b) % rho == 0
    lmax = num_factors(gcd(e0.A.b, (e0.A.b - e0.Ap.b) // rho)) + 1
    complete = []
    open_chains = [(e0,)]
    for _ in range(lmax):
        nxt = []
        for ch in open_chains:
            children, finals = get_children_and_finals(ch[-1], pllc)
            for A1 in finals:
                complete.append(Chain(ch, A1))
            for e in children:
                nxt.append(ch + (e,))
        open_chains = nxt
    return complete

# ------------------------------------------------- Algorithm 7: admissibility

def chain_dirs_pq(chain):
    "[(rho_h, sigma_h, p_h, q_h)] per edge h (the (q_k) machinery)"
    out = []
    for e in chain.edges:
        rho, sigma = edge_dir(e)
        p, q = pq_of(rho, sigma, e.A)
        out.append((rho, sigma, p, q))
    return out

def is_admissible(chain):
    """GetIsAdmissible: q_i | D_h^(i), q_h does not divide q_i, and
    Omega(D_h^(i)) >= i - h, for all 0 <= h < i <= j (Definition 2.30)."""
    edges = chain.edges
    j = len(edges) - 1
    if j < 1:
        return True
    data = chain_dirs_pq(chain)
    for h in range(j):
        rho, sigma, _, qh = data[h]
        Ah, Ahp = edges[h]
        gap = rho // gcd(rho, Ah.l)
        assert (Ah.b - Ahp.b) % gap == 0
        for i in range(h + 1, j + 1):
            _, _, _, qi = data[i]
            li = edges[i].A.l
            assert (Ah.a * li) % Ah.l == 0 and (Ahp.a * li) % Ah.l == 0
            D = gcd(gcd((Ah.b - Ahp.b) // gap, gcd(Ah.b, edges[h + 1].A.b)),
                    gcd(Ah.a * li // Ah.l, Ahp.a * li // Ah.l))
            if not (num_factors(D) >= i - h and D % qi == 0 and qi % qh != 0):
                return False
    return True

# ------------------------------------------------- Algorithm 8: main algorithm

def admissible_complete_chains(M):
    "All admissible complete chains with v11(A0) <= M."
    pllc = get_pllc(M // 2)
    chains = []
    for a in range(2, M // 2 + 1):
        for b in range(a + 1, M - a + 1):
            for e0 in get_starting_edges(a, b, pllc):
                for ch in get_complete_chains(e0, pllc):
                    if is_admissible(ch):
                        chains.append(ch)
    return chains

def chain_path(chain):
    "corner path (A0, A1, ..., A_{j+1}) as geometric points"
    return tuple([geom(chain.edges[0].A)]
                 + [geom(e.A) for e in chain.edges[1:]] + [geom(chain.final)])

# ---------------------------------------------- Algorithm 9: (m,n)-families

def bezout_min(x, y):
    "coprime x,y >= 1: the (M, N) with M*x - N*y = 1, N >= 1 minimal"
    M = pow(x, -1, y) if y > 1 else 1
    N = (M * x - 1) // y
    if N < 1:
        M, N = M + y, N + x
    assert M * x - N * y == 1 and N >= 1
    return M, N

def get_mn_families(A):
    """GetmnFamilies(final corner A): the (m,n)-families MN(A) of Definition
    3.4, as Family(k, i, m0, n0, d1, d2) with members (m0+j*d1, n0+j*d2),
    j in N_0 (all coprime; the paper's (kbar*d1, kbar*d1) misprint fixed)."""
    a, l, b = A
    assert is_final(A)
    fams = []
    k = 1
    while k * b < l * b - a:                        # k < l - a/b
        e = gcd(k, b * l - a)
        y = (b * l - a) // e
        if gcd(b, y) == 1:
            M, N = bezout_min(b, y)
            n = N * k // e
            m = M - n
            d1, d2 = (b * l - a - b * k) // e, b * k // e
            if m == 1 or n == 1:
                m, n = m + d1, n + d2
            kbar = k // e
            if kbar == 1:
                fams.append(Family(k, 0, m, n, d1, d2))
            else:
                for i in range(kbar):
                    mi, ni = m + i * d1, n + i * d2
                    if gcd(mi, ni) == 1:
                        fams.append(Family(k, i, mi, ni, kbar * d1, kbar * d2))
        k += 1
    return fams

def family_members(fam, s, maxdeg):
    "[(j, m, n)] with max(m,n)*s <= maxdeg (s = v11(A0)); coprime by Lemma 3.5"
    out = []
    j = 0
    while True:
        m, n = fam.m0 + j * fam.d1, fam.n0 + j * fam.d2
        if max(m, n) * s > maxdeg:
            return out
        assert gcd(m, n) == 1
        out.append((j, m, n))
        j += 1

# ------------------------------------------------------------- table builders

def enumerate_families(M):
    "[(chain, family)] for all admissible complete chains with v11(A0) <= M"
    return [(ch, fam) for ch in admissible_complete_chains(M)
            for fam in get_mn_families(ch.final)]

def enumerate_cases(maxdeg):
    """All (chain, family, j, (m,n), maxdeg) with max(deg P, deg Q) =
    max(m,n) * v11(A0) <= maxdeg.  GGV5 lists each case once, in the
    orientation of eq. (3.1) [ecuacion diofantica]; the (n,m) swaps are
    implicit.  M = maxdeg // 3 suffices: m,n > 1 coprime forces max(m,n) >= 3."""
    out = []
    for ch, fam in enumerate_families(maxdeg // 3):
        s = int(v11(ch.edges[0].A))
        for (j, m, n) in family_members(fam, s, maxdeg):
            out.append((ch, fam, j, (m, n), max(m, n) * s))
    return out

def case_rows(maxdeg):
    "deduplicated printable rows {(corner path, (m,n), maxdeg)} as in GGV5 S6"
    return {(chain_path(ch), mn, d) for ch, fam, j, mn, d in enumerate_cases(maxdeg)}

# -------------------------------------- S4 corner data (SECTION4-AUTOMATION.md)

def _hull(points):
    "convex hull (Andrew monotone chain), CCW corner list starting at (0,0)"
    pts = sorted(set(points))
    def half(ps):
        h = []
        for p in ps:
            while len(h) >= 2 and \
                  (h[-1][0]-h[-2][0])*(p[1]-h[-2][1]) - (h[-1][1]-h[-2][1])*(p[0]-h[-2][0]) <= 0:
                h.pop()
            h.append(p)
        return h
    lower, upper = half(pts), half(pts[::-1])
    hull = lower[:-1] + upper[:-1]
    i0 = hull.index(min(hull))
    return tuple(hull[i0:] + hull[:i0])

CornerData = namedtuple(
    "CornerData",
    "name A0 A0p chain final steps k family mn j degP degQ S c upper_dir rhs_exp")

def corner_data(chain, fam, j=0, name=""):
    """The per-family record the Phase-2 reduction engine consumes
    (SECTION4-AUTOMATION.md S2):
      A0, A0', chain edges + final corner, per-step (rho,sigma,p,q) from (q_k),
      family k, instantiated (m,n), start polygon S (1/m units) =
      conv({(0,0)} + integral chain corners + {(0,c)}), c = v_{rho*,sigma*}(A0)
      for the upper-left direction (rho*,sigma*) = (1 - ceil(b0/a0), 1),
      bracket RHS exponent ceil(b0/a0) - 2."""
    A0 = chain.edges[0].A
    m, n = fam.m0 + j * fam.d1, fam.n0 + j * fam.d2
    s = int(v11(A0))
    jpsi = -((-A0.b) // A0.a)                       # ceil(b0/a0)
    c = (1 - jpsi) * A0.a + A0.b                    # v_{1-jpsi,1}(A0), integer
    pts = [(0, 0), (0, c)]
    for e in chain.edges:
        for A in (e.A, e.Ap):
            if A.l == 1 or A.a % A.l == 0:
                pts.append((A.a // A.l if A.l > 1 else A.a, A.b))
    if chain.final.a % chain.final.l == 0:
        pts.append((chain.final.a // chain.final.l, chain.final.b))
    return CornerData(
        name=name, A0=A0, A0p=chain.edges[0].Ap, chain=chain.edges,
        final=chain.final, steps=tuple(chain_dirs_pq(chain)), k=fam.k,
        family=fam, mn=(m, n), j=j, degP=m * s, degQ=n * s,
        S=_hull(pts), c=c, upper_dir=(1 - jpsi, 1), rhs_exp=jpsi - 2)

def supports(cd):
    """(SuppP, SuppQ) corner lists of the unreduced standard pair: m*S and n*S
    (SECTION4-AUTOMATION.md S3: while P,Q are proportional the state is one
    1/m-polygon S with SuppP = m*S, SuppQ = n*S)."""
    m, n = cd.mn
    return ([(m * x, m * y) for x, y in cd.S],
            [(n * x, n * y) for x, y in cd.S])

_S4_KEYS = {                                        # path, (m,n) per GGV22 S4
    "9_27": ([(9, 27), (9, 24), (Fraction(11, 3), 8)], (2, 3)),
    "9_24": ([(9, 24), (Fraction(11, 3), 8)], (2, 3)),
    "8_28": ([(8, 28), (Fraction(11, 4), 7)], (3, 2)),
    "7_21": ([(7, 21), (Fraction(11, 7), 2)], (2, 3)),
}

def section4_families():
    """The four GGV22 S4 families (Props 4.1-4.4) as CornerData, keyed
    '9_27', '9_24', '8_28', '7_21' -- regression gate B."""
    out = {}
    for ch, fam, j, mn, d in enumerate_cases(150):
        path = tuple((Fraction(x), y) for x, y in chain_path(ch))
        for key, (wpath, wmn) in _S4_KEYS.items():
            if mn == wmn and path == tuple((Fraction(a), b) for a, b in wpath):
                assert key not in out, f"duplicate S4 family {key}"
                out[key] = corner_data(ch, fam, j, name=key)
    assert set(out) == set(_S4_KEYS), sorted(out)
    return out

if __name__ == "__main__":  # smoke: PLLC facts + the four S4 chains
    P = get_pllc(25)
    assert (1, 0) in P and (6, 2) in P and (3, 1) in P
    assert (2, 1) not in P     # kills Moh's ((7,21),(2,1)) case, GGV5 S6
    assert (6, 3) not in P and (4, 2) not in P
    print(f"PLLC(25): {len(P)} corners OK")
    chains = admissible_complete_chains(36)
    paths = {chain_path(c) for c in chains}
    for want in [((Fraction(9), 27), (Fraction(9), 24), (Fraction(11, 3), 8)),
                 ((Fraction(9), 24), (Fraction(11, 3), 8)),
                 ((Fraction(8), 28), (Fraction(11, 4), 7)),
                 ((Fraction(7), 21), (Fraction(11, 7), 2))]:
        assert want in paths, want
    print(f"chains(M=36): {len(chains)} admissible complete chains OK")
    fams35 = enumerate_families(35)
    print(f"families(M=35): {len(fams35)} (GGV5 S5 tables: 24)")
    rows = sorted(case_rows(150), key=lambda r: (r[2], r[0]))
    print(f"cases(maxdeg<=150): {len(rows)} rows (GGV5 S6: 34)")
    lt125 = [r for r in rows if r[2] < 125]
    print(f"cases(maxdeg<125): {len(lt125)} rows (GGV22 S2: 10)")
    for cd in section4_families().values():
        print(f"  S4 {cd.name}: (m,n)={cd.mn} degs=({cd.degP},{cd.degQ}) "
              f"S={cd.S} rhs=x^{cd.rhs_exp} steps={cd.steps}")
