"""SECTION4-AUTOMATION Phase 2: the GGV22 (arXiv:2204.14178) S4 reduction engine.

Reproduces the per-family Newton-polygon reductions of GGV22 S4 (Props 4.1-4.4)
from Phase 1 CornerData (lib/families.py) alone, per SECTION4-AUTOMATION.md:

  R1  edge-power certificates  (GGV1 = arXiv:1401.1784 Cor 7.4 `fracciones de
      F1`, flipped frame; q from the (q_k) chain data, R2)
  R3  PossibleStartingPoints   (GGV22 Algorithm 1, verbatim) + Prop 3.12
      case-(1) single-root shapes + the v=0 origin-ray option
  R4  forced-multiplicity filter (GGV2 = arXiv:1605.09430 Prop 3.12
      `finitas direcciones`, all three cases checked as a consistency filter)
  R5  zero-root exclusion for the cut root (support-level)
  R6  x-degree floor (vdE Prop 10.2.6; pre-Laurent states only)
  R7  PLLC membership (families.get_pllc; used by the (8,32)-style discard)
  R8  divisibility of d (GGV1 Thm 7.6(5)/(8); (8,32)-style discard)
  R9  tail resolution (GGV1 Prop 8.2 `esquina de 83` + GGV22's opposite-vertex
      divisibility filter, aligned-branch recursion with colinearity kills)
  R10 finalization psi_j: x -> x^{-1}, y -> x^j y; bracket -> x^(j-2)

Conventions: the whole reduction runs in FLIPPED coordinates (phi1: x<->y
applied to the GGV5 start polygon), state polygons are 1/m-units lattice
corner lists, SuppP = m*state, SuppQ = n*state until R9 individuates them.
st/en of a face = its endpoints in CCW hull order (GGV1 Notation 1.2:
(rho,sigma) x (en - st) > 0).

Branch semantics (design S5): B1 root partitions, B2 st-candidates after a
full collapse, B3 aligned ends in R9.  Leaves are merged by hashing the
emitted (N(P), N(Q), rhs).  Unresolvable structure raises Stuck -> status
'stuck' with the state dumped, never a guess.
"""
import sys, os
from fractions import Fraction
from math import gcd
from collections import namedtuple

sys.path.insert(0, os.path.dirname(__file__))
from families import (CornerData, get_pllc, corner_data, section4_families,
                      enumerate_cases, chain_path, v11)

# ---------------------------------------------------------------- exceptions

class Stuck(Exception):
    "engine cannot certify/resolve; carries a state dump (design S6)"

# ---------------------------------------------------------------- direction order
# Total CCW order on directions starting at (0,-1):
# (0,-1) < (1,-K)... < (1,-1) < (1,0) < (0,1) < (-1,K)... < (-1,0).

def _dquad(d):
    r, s = d
    assert (r, s) != (0, 0)
    if r == 0:
        return 0 if s < 0 else 4
    if r > 0:
        return 1 if s < 0 else (2 if s == 0 else 3)
    return 5 if s > 0 else (6 if s == 0 else 7)

def dir_lt(d1, d2):
    "d1 strictly before d2 in the CCW sweep from (0,-1)"
    q1, q2 = _dquad(d1), _dquad(d2)
    if q1 != q2:
        return q1 < q2
    return d1[0] * d2[1] - d1[1] * d2[0] > 0

def prim(v):
    "primitive vector along v"
    g = gcd(abs(v[0]), abs(v[1]))
    return (v[0] // g, v[1] // g)

def outdir(edge_vec):
    "outward normal of a CCW polygon edge (dx,dy): (dy,-dx) primitive"
    return prim((edge_vec[1], -edge_vec[0]))

def vdir(d, p):
    return d[0] * p[0] + d[1] * p[1]

def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]

# ---------------------------------------------------------------- hull / faces

def hull(points):
    "convex hull, CCW corner list starting at the lexicographic minimum"
    pts = sorted(set(points))
    if len(pts) == 1:
        return tuple(pts)
    def half(ps):
        h = []
        for p in ps:
            while len(h) >= 2 and cross((h[-1][0]-h[-2][0], h[-1][1]-h[-2][1]),
                                        (p[0]-h[-2][0], p[1]-h[-2][1])) <= 0:
                h.pop()
            h.append(p)
        return h
    lower, upper = half(pts), half(pts[::-1])
    hp = lower[:-1] + upper[:-1]
    if not hp:                                     # collinear degenerate
        return (pts[0], pts[-1])
    i0 = hp.index(min(hp))
    return tuple(hp[i0:] + hp[:i0])

Face = namedtuple("Face", "st en dir")             # st,en in CCW order

def faces(corners):
    "list of Face for a CCW hull; st -> en is the CCW traversal (GGV1 cross rule)"
    n = len(corners)
    out = []
    for i in range(n):
        a, b = corners[i], corners[(i + 1) % n]
        out.append(Face(a, b, outdir((b[0]-a[0], b[1]-a[1]))))
    return out

def face_with_dir(corners, d):
    for f in faces(corners):
        if f.dir == d:
            return f
    return None

def flip(pts):
    return [(y, x) for x, y in pts]

# --------------------------------------- R3: Algorithm 1 (verbatim, l = 1)

def possible_starting_points(a, b):
    """GGV22 Algorithm 1 `PossibleStartingPoints` for the corner (a,b), l=1.
    Returns [(c,d)] with the paper's test (s | N2 and d>0) or s <= N1."""
    out = []
    for d in range(0, b):
        for c in range(d * a // b + 1, d + a - b):
            n1 = gcd(a - c, b - d)
            n2 = gcd(c, d)
            rho, sigma = prim((b - d, -(a - c)))   # dir((a,b)-(c,d)), rho>0
            v = rho * a + sigma * b
            assert v > 0, (a, b, c, d)
            s = v // gcd(v, abs(rho + sigma)) if rho + sigma != 0 else v
            if (d > 0 and s > 0 and n2 % s == 0) or s <= n1:
                out.append((c, d))
    return out

def case1_singles(en):
    """GGV2 Prop 3.12 case (1) shapes missed by Algorithm 1: st=(c,0) with a
    single nonzero root, direction (1,-K), K>=2, plus the l=1 addendum
    v_{1,-2}(en) > 0."""
    a, b = en
    out = []
    if b >= 1 and a - 2 * b > 0:                   # v_{1,-2}(en) > 0
        for K in range(2, (a - 1) // b + 1):
            c = a - K * b
            if c >= 1:
                out.append((c, 0))
    return out

# --------------------------------------- R4: GGV2 Prop 3.12 consistency filter

def prop312_consistent(st_E, en_E, d, mults_nonzero, zero_mult):
    """GGV2 Prop 3.12 (`finitas direcciones`) as a filter, applied to the
    1/m edge form E with st(E)=st_E, en(E)=en_E, direction d=(rho,sigma) in
    ](0,-1),(1,-1)[, nonzero-root multiplicities mults_nonzero (list, at the
    E level) and z-power zero_mult = nu_2.  Returns (ok, why)."""
    rho, sigma = d
    u = vdir(d, en_E)
    if u <= 0:
        return True, "312-na (u<=0)"              # hypotheses fail: no filter
    if not (rho >= 1 and sigma <= -rho - 1):
        return True, "312-na (dir outside ](0,-1),(1,-1)[)"
    nu1 = en_E[1] - st_E[1]
    N1 = nu1 // rho                                # gap(rho, l=1) = rho; N1 = nu1/gap
    N2 = gcd(st_E[0], st_E[1])
    # case (1): rho | l(=1), single nonzero root, no zero root; and l=1 =>
    # v_{1,-2}(en) > 0
    if rho == 1 and zero_mult == 0 and len(mults_nonzero) == 1:
        if en_E[0] - 2 * en_E[1] > 0:
            return True, "312-case1"
    # theta candidates: t' = -theta(rho+sigma)/u must be a positive integer
    def tprime_ok(theta):
        t = Fraction(-theta * (rho + sigma), u)
        return t > 0 and t.denominator == 1
    # case (2): some nonzero-root multiplicity theta <= N1 with the direction eq
    for theta in set(mults_nonzero):
        if theta <= N1 and tprime_ok(theta):
            return True, f"312-case2 theta={theta}"
    # case (3): nu_2 > 0 and exists theta | N2 with the direction equation
    if zero_mult > 0 and N2 > 0:
        for theta in range(1, N2 + 1):
            if N2 % theta == 0 and tprime_ok(theta):
                return True, f"312-case3 theta={theta}"
    return False, (f"312-kill st={st_E} en={en_E} dir={d} mults={mults_nonzero} "
                   f"z^{zero_mult}: no case of GGV2 Prop 3.12 is consistent")

# --------------------------------------- continuation derivation (R1+R3+R6)

def continuations(enR, q, dir_bound, laurent, log, tag):
    """Candidate (stR, dir) for the next boundary face below the vertex
    q*enR, with the incoming direction bound (strict).  Sources: Algorithm 1
    + Prop 3.12 case-(1) singles + the v=0 origin-ray option.  Kills: strict
    direction decrease, v_{dir}(enR) > 0 for certified candidates, R6
    axis-reachability (pre-Laurent only).  Appends to log."""
    cand = []
    seen = set()
    for (c, d) in possible_starting_points(*enR) + case1_singles(enR):
        if (c, d) in seen or (c, d) == enR:
            continue
        seen.add((c, d))
        dd = outdir((enR[0]-c, enR[1]-d))          # dir of the face (c,d)->(enR)
        if not dir_lt(dd, dir_bound):
            log.append(f"{tag}: st(R)={(c,d)} dir={dd} rejected (not < {dir_bound})")
            continue
        if vdir(dd, enR) <= 0:
            log.append(f"{tag}: st(R)={(c,d)} dir={dd} rejected (v<=0: Cor 7.4 "
                       "certificate requires v>0 on the face)")
            continue
        if not laurent and not reaches_axis((c, d), dd, log, tag):
            log.append(f"{tag}: st(R)={(c,d)} dir={dd} KILLED by R6 (vdE 10.2.6: "
                       "no boundary continuation reaches (x,0), x>=1)")
            continue
        cand.append(((c, d), dd))
    # v=0 ray through the origin: the face [ (0,0), enR ] (no certificate use)
    dray = outdir(enR)
    if dir_lt(dray, dir_bound):
        if laurent:
            cand.append(((0, 0), dray))
        else:
            log.append(f"{tag}: st(R)=(0,0) dir={dray} KILLED by R6 "
                       "(deg_x P(x,0) = 0, vdE 10.2.6; state still polynomial)")
    log.append(f"{tag}: continuations of en(R)={enR} below {dir_bound}: "
               f"{[(c, d) for c, d in cand]}")
    return cand

def reaches_axis(V, dbound, log, tag, _depth=0):
    """R6 recursion: can the (pre-Laurent) lower boundary continue from the
    corner V (R-units) with directions strictly below dbound until it reaches
    some (c,0), c>=1?  Candidate corners per Algorithm 1 + case-(1) singles;
    faces must keep v_{dir} >= 0 (the support contains (0,0))."""
    c, d = V
    if d == 0:
        return c >= 1
    if _depth > 12:
        raise Stuck(f"reaches_axis recursion overflow at {V}")
    for (c2, d2) in possible_starting_points(c, d) + case1_singles((c, d)):
        if (c2, d2) == V:
            continue
        dd = outdir((c - c2, d - d2))
        if dir_lt(dd, dbound) and vdir(dd, V) >= 0 and \
           reaches_axis((c2, d2), dd, log, tag, _depth + 1):
            return True
    return False

def lower_boundary(stR, dbound, laurent, log, tag):
    """Boundary corners strictly below a face-start stR (R-units), derived by
    the same continuation machinery; returns the list of corner chains
    (each a list of further corners ending on the x-axis or at (0,0)).
    Unique in all S4 uses; branches would multiply states."""
    c, d = stR
    if d == 0:
        return [[]]
    out = []
    for (c2, d2) in possible_starting_points(c, d) + case1_singles((c, d)):
        if (c2, d2) == stR:
            continue
        dd = outdir((c - c2, d - d2))
        if not dir_lt(dd, dbound) or vdir(dd, stR) < 0:
            continue
        if not laurent and not reaches_axis((c2, d2), dd, log, tag):
            continue
        for rest in lower_boundary((c2, d2), dd, laurent, log, tag):
            out.append([(c2, d2)] + rest)
    dray = outdir(stR)
    if dir_lt(dray, dbound):
        # face straight to (0,0) along the ray (v=0)
        out.append([(0, 0)])
    if not out:
        log.append(f"{tag}: no boundary continuation below {stR} "
                   f"(bound {dbound}) -- corner impossible")
    # dedupe
    ded = []
    for ch in out:
        if ch not in ded:
            ded.append(ch)
    return ded

# ---------------------------------------------------------------- state

State = namedtuple("State", "corners prov laurent log label")
# corners: CCW hull tuple, 1/m units, flipped frame; prov: frozenset of
# provisional Laurent-tail corners (discarded by R9); log: tuple of strings.

def mkstate(pts, prov, laurent, log, label):
    h = hull(pts)
    pv = frozenset(p for p in prov if p in h)
    return State(h, pv, laurent, tuple(log), label)

# ---------------------------------------------------------------- e_K cut

def apply_cut(state, fst, fen, K, q, shape, root_label):
    """T-shift e_K on the certified face [fst, fen] (1/m units, direction
    (1,-K)) with 1/m form x^c y^d z^(q*z0) prod_i (z-lam_i)^(q*t_i), cutting a
    root of R-multiplicity t1 = max part.  shape = (z0, parts, t1).
    Exact rewrite on the face; naive images elsewhere.  Returns
    (new_points, new_prov, new_face_st or None-if-collapsed, residual)."""
    z0, parts, t1 = shape
    d_pref = fst[1]                                # y-exponent of the 1/m st
    stv = (fst[0] + q * z0 * K, fst[1] + q * z0)   # actual st of this shape
    new_stE = (stv[0] + q * t1 * K, stv[1] + q * t1)
    rest = sorted(parts)[:-1]                      # roots left after cutting t1
    pts, prov = [], set(list(state.prov))
    # exact face image
    if rest:                                       # face survives, shortened
        pts += [new_stE, fen]
        collapsed = False
    elif z0 > 0 or d_pref > 0:
        # full nonzero-root collapse; the y/z prefactor spans down from en
        dtail = q * z0 + d_pref
        pts += [fen, (fen[0] - dtail * K, fen[1] - dtail)]
        collapsed = True
    else:
        pts.append(fen)
        collapsed = True
    # naive images of all off-face corners
    onface = set()
    seg = prim((fen[0] - fst[0], fen[1] - fst[1]))
    for c in state.corners:
        w = (c[0] - fst[0], c[1] - fst[1])
        if cross(seg, w) == 0 and 0 <= vdir(seg, w) <= vdir(seg, (fen[0]-fst[0], fen[1]-fst[1])):
            onface.add(c)                          # consumed by the rewrite
    for c in state.corners:
        if c in onface:
            continue
        pts.append(c)
        if c[1] > 0:
            t = (c[0] - K * c[1], 0)
            if t[0] <= 0:
                pts.append(t)
                if t[0] < 0:
                    prov.add(t)                    # provisional Laurent tail
            # else: a spread toward +x is excluded: the Cor 7.4 powers at the
            # intermediate directions force lattice en(R) there and the
            # boundary below the apex is re-derived by R3 (design R1 note)
    return pts, prov, (None if collapsed else new_stE), collapsed

# --------------------------------------- B1: root shapes of a certified face

def face_shapes(stR, enR, K, q, z0_allowed, log, tag):
    """Enumerate (z0, partition) shapes of the certified face, R-level:
    R = x^c' y^(d'+z0-ish) z^z0 prod (z-lam_i)^(t_i), sum t_i = zdeg - z0,
    lam_i distinct nonzero.  Filter by R4 (GGV2 Prop 3.12 at the E level) and
    R5 (the cut root cannot be zero).  Returns [(z0, parts)] sorted by
    decreasing cut strength."""
    dx, dy = enR[0] - stR[0], enR[1] - stR[1]
    assert (dx, dy) == (K * dy, dy) and dy >= 1, (stR, enR, K)
    zdeg = dy
    out = []
    for z0 in sorted(z0_allowed):
        free = zdeg - z0
        if free < 1:
            continue
        for parts in _partitions(free):
            stv = (stR[0] + z0 * K, stR[1] + z0)
            st_E = (q * stv[0], q * stv[1])
            en_E = (q * enR[0], q * enR[1])
            mults_E = [q * t for t in parts]
            # nu_2 = the z-power of the edge form = the y-part of its start
            ok, why = prop312_consistent(st_E, en_E, (1, -K), mults_E, st_E[1])
            if not ok:
                log.append(f"{tag}: shape z^{z0}*{parts} KILLED by R4: {why}")
                continue
            # R5 bookkeeping: if the cut root (max part t1) were zero, the true
            # face start would sit z0+t1 steps up; that scenario is either an
            # admitted sibling shape / covered by the post-collapse B2
            # continuations (so cutting the token root is WLOG sound), or it
            # was killed above, proving lambda_1 != 0 as in the paper.
            t1 = max(parts)
            zt = z0 + t1
            if zt >= zdeg:
                r5 = "degenerate face, covered by the B2 continuations"
            elif zt in z0_allowed:
                r5 = f"covered by the admitted sibling shape z^{zt}"
            else:
                r5 = f"st(R) {zt} steps up was excluded => lambda_1 != 0 proven"
            log.append(f"{tag}: shape z^{z0}*{parts} admitted ({why}); R5 "
                       f"(zero cut root): {r5}")
            out.append((z0, tuple(parts)))
    return out

def _partitions(n, most=None):
    if n == 0:
        return [[]]
    most = most or n
    out = []
    for k in range(min(n, most), 0, -1):
        for rest in _partitions(n - k, k):
            out.append([k] + rest)
    return out

# --------------------------------------- R9: tail resolution (GGV1 Prop 8.2)

def tail_resolve(V, incoming, m, n, log, depth=0):
    """GGV1 Prop 8.2 at the residual vertex V=(a,b) (1/m units) whose face of
    direction `incoming` = (rho1,sigma1) has en/m = V, plus GGV22's aligned
    opposite-vertex analysis.  Returns list of outcomes
    (extra_corners, endP, endQ, facedir): extra_corners = aligned corners
    accepted on the way (none in all S4 cases)."""
    a, b = V
    assert a > b >= 1 and m != n, (V, m, n)
    if depth > 6:
        raise Stuck(f"R9 aligned recursion overflow at {V}")
    out = []
    # --- non-aligned: Prop 8.2(2): ends {(-k,0),(k+1,1)}, (k+1)b < a
    for k in range(1, (a - 1) // b):
        if (k + 1) * b >= a:
            break
        ends = [(-k, 0), (k + 1, 1)]
        for eP, eQ in (ends, ends[::-1]):
            wP = (eP[0] - m * a, eP[1] - m * b)
            wQ = (eQ[0] - n * a, eQ[1] - n * b)
            if cross(wP, wQ) != 0:
                log.append(f"R9 at {V}: k={k} ends P->{eP} Q->{eQ} killed: "
                           f"P,Q edges not parallel (cross {cross(wP, wQ)})")
                continue
            fd = outdir(wP)                        # outward normal (CCW st->en)
            if fd == incoming:
                log.append(f"R9 at {V}: k={k} ends P->{eP} Q->{eQ} killed: "
                           f"its direction equals the incoming edge direction "
                           f"{fd} -- different end for the same direction "
                           "(GGV22 colinearity contradiction)")
                continue
            if not (dir_lt(incoming, fd) and dir_lt(fd, (-1, 1))):
                log.append(f"R9 at {V}: k={k} ends P->{eP} Q->{eQ} killed: "
                           f"direction {fd} outside ]{incoming},(-1,1)[")
                continue
            out.append(((), eP, eQ, fd, f"k={k}"))
            log.append(f"R9 at {V}: k={k} survives with en(P*)={eP}, "
                       f"en(Q*)={eQ}, direction {fd} (P*=the m-fold polygon)")
    # --- aligned: Prop 8.2(1) candidates (a',b'): ab'-ba'>0,
    #     v_incoming(a',b') < v_incoming(V); filtered by the GGV22
    #     divisibility (a b' - b a') | (a-b) gcd(a-a', b-b') and the diagonal
    vV = vdir(incoming, V)
    table = []
    for b2 in range(0, 2 * b + 2):
        for a2 in range(-3 * b - 3, 3 * (a + b)):
            if (a2, b2) == V:
                continue
            D = a * b2 - b * a2
            if D <= 0 or vdir(incoming, (a2, b2)) >= vV:
                continue
            g = gcd(a - a2, abs(b - b2))
            need = (a - b) * g
            if a2 == b2:
                table.append(((a2, b2), D, need, "diagonal"))
                log.append(f"R9 at {V}: aligned (a',b')={(a2,b2)} killed: "
                           "on the diagonal")
                continue
            if need % D != 0:
                table.append(((a2, b2), D, need, "div-fail"))
                log.append(f"R9 at {V}: aligned (a',b')={(a2,b2)} killed: "
                           f"{D} does not divide {need} "
                           f"(= v_(-b,a)(1,1)*gcd, GGV22 divisibility table)")
                continue
            table.append(((a2, b2), D, need, "pass"))
            # aligned corner accepted: recurse at W with the new incoming dir
            W = (a2, b2)
            dW = outdir((a2 - a, b2 - b))          # CCW edge V -> W
            if b2 == 0:
                # aligned end on the x-axis: both polygons close there
                log.append(f"R9 at {V}: aligned (a',b')={W} on the x-axis: "
                           "terminal aligned end (both polygons close)")
                out.append(((), (m * a2, 0), (n * a2, 0), dW,
                            f"aligned-end{W}"))
                continue
            log.append(f"R9 at {V}: aligned (a',b')={W} passes divisibility "
                       f"({D} | {need}); recursing with incoming {dW}")
            for extra, eP, eQ, fd, lbl in tail_resolve(W, dW, m, n, log,
                                                       depth + 1):
                if fd == dW:
                    log.append(f"R9 at {V}: aligned branch via {W} killed: "
                               f"its final direction {fd} equals the aligned "
                               "edge direction (different end for the same "
                               "direction -- GGV22 colinearity contradiction)")
                    continue
                out.append(((W,) + extra, eP, eQ, fd, f"aligned{W};{lbl}"))
    return out

# --------------------------------------- R10: finalization psi_j

def finalize(state, mn, residual_ends, cdname):
    """Apply psi_j: (i,j') -> (j*j'-i, j'), j = ceil(max i/j'), to the P,Q
    polygons; returns (NP, NQ, j-2, log-lines).  P := the min(m,n) multiple
    (GGV22 emits deg P < deg Q)."""
    m, n = mn
    lines = []
    if residual_ends is None:
        kept = list(state.corners)                 # tails stay: no R9 ran
    else:
        kept = [c for c in state.corners if c not in state.prov]
    if residual_ends is not None:
        V, eP, eQ = residual_ends
        kept = [c for c in kept if c[1] > 0 or c[0] >= 0 or c == (0, 0)]
        # provisional tails already dropped via state.prov; also drop any
        # remaining Laurent tail (i<0,0): superseded by the exact ends
        kept = [c for c in kept if not (c[1] == 0 and c[0] < 0)]
        polyM = hull([(m * x, m * y) for x, y in kept] + [eP])
        polyN = hull([(n * x, n * y) for x, y in kept] + [eQ])
        lines.append(f"R9: exact ends set: en={eP} on the {m}-fold polygon, "
                     f"en={eQ} on the {n}-fold; provisional tails discarded")
    else:
        polyM = hull([(m * x, m * y) for x, y in kept])
        polyN = hull([(n * x, n * y) for x, y in kept])
    js = [(-(-i // jy)) for i, jy in list(polyM) + list(polyN) if jy > 0]
    j = max(js)
    for i, jy in list(polyM) + list(polyN):
        if jy == 0 and i > 0:
            raise Stuck(f"{cdname}: psi_j precondition fails: support point "
                        f"({i},0) with i>0 in {polyM} / {polyN}")
    psi = lambda p: (j * p[1] - p[0], p[1])
    NP_M = hull([psi(p) for p in polyM])
    NP_N = hull([psi(p) for p in polyN])
    lines.append(f"R10: psi_{j} applied; bracket [psiP,psiQ] = -x^{j-2}[P,Q] "
                 f"=> RHS x^{j-2} after scaling")
    NP, NQ = (NP_M, NP_N) if m < n else (NP_N, NP_M)
    return NP, NQ, j - 2, lines

# --------------------------------------- R8+R7: the (8,32)-style discard

def discard_check(cd, pllc, log):
    """GGV22 S2 (8,32) discard: chain with vertical first edge (1,0); GGV1
    Thm 7.6(5)/(8) forces d0 (q1 | d0, d0 | gcd(A1), d0 | b0-b1); if the top
    edge then carries a single root ((b0-b1)/d0 = 1), the automorphism
    y -> y+lambda makes A0' = (a1, b0-b1) the last lower corner of P, which
    must lie in PLLC (GGV2 Prop 3.29 / Rem 3.31)."""
    if len(cd.chain) < 2:
        return False
    e0 = cd.chain[0]
    if (cd.steps[0][0], cd.steps[0][1]) != (1, 0):
        return False
    a0, b0 = cd.A0.a, cd.A0.b
    a1, b1 = e0.Ap.a, e0.Ap.b
    q1 = cd.steps[1][3]
    g = gcd(gcd(a1, b1), b0 - b1)
    d0s = [d for d in range(1, g + 1) if g % d == 0 and d % q1 == 0]
    if len(d0s) != 1:
        return False
    d0 = d0s[0]
    log.append(f"R8: q1={q1} | d0 (GGV1 Thm 7.6(5)/(8)) and d0 | "
               f"gcd({a1},{b1},{b0 - b1}) force d0={d0}")
    if (b0 - b1) // d0 != 1:
        log.append(f"R8: top edge has {(b0 - b1) // d0} roots; no forced "
                   "last-corner move, discard check inconclusive")
        return False
    corner = (a1, b0 - b1)
    log.append(f"R8: l_(1,0)(P) = (x^{a1 // d0} y^{b1 // d0} (y-lam))^{d0}m; "
               f"y -> y+lam makes A0' = {corner} the last lower corner")
    if corner in pllc:
        log.append(f"R7: {corner} is a possible last lower corner; no discard")
        return False
    log.append(f"R7: {corner} is NOT a possible last lower corner "
               "(GGV2 Prop 3.29 / Rem 3.31, families.get_pllc) -- DISCARDED")
    return True

# ---------------------------------------------------------------- orchestrator

Emitted = namedtuple("Emitted", "label NP NQ rhs_exp path")
Result = namedtuple("Result", "name status cases log")

def _axis_ok(corners, allowed_axis, log, tag):
    "G3: every positive-x axis corner of the hull must be a derived boundary corner"
    for c in corners:
        if c[1] == 0 and c[0] > 0 and c not in allowed_axis:
            log.append(f"{tag}: hull corner {c} on the positive x-axis is not "
                       "an admitted boundary corner (post-cut Algorithm-1 "
                       "consistency) -- branch KILLED")
            return False
    return True

def _chain_pts(chain_pts, q):
    "corners of a lower-boundary chain in E units, plus its axis corners"
    pts = [(q * c, q * d) for c, d in chain_pts]
    axis = {p for p in pts if p[1] == 0 and p[0] > 0}
    return pts, axis

def reduce_family(cd, pllc=None):
    "run the full S4 reduction for one CornerData; Result(status, cases, log)"
    name = cd.name or f"{cd.A0.a}_{cd.A0.b}"
    log = [f"family {name}: A0={tuple(cd.A0)} A0'={tuple(cd.A0p)} "
           f"(m,n)={cd.mn} steps={cd.steps} k={cd.k}"]
    if pllc is None:
        pllc = get_pllc(4 * max(cd.A0.a, cd.A0.b))
    if discard_check(cd, pllc, log):
        return Result(name, "discarded", (), tuple(log))
    try:
        cases = _reduce(cd, log)
    except Stuck as e:
        log.append(f"STUCK: {e}")
        return Result(name, "stuck", (), tuple(log))
    return Result(name, "reduced", tuple(cases), tuple(log))

def _reduce(cd, log):
    m, n = cd.mn
    q0 = cd.steps[0][3]
    apexE = (cd.A0.b, cd.A0.a)                     # flipped A0
    d0f = (cd.steps[0][1], cd.steps[0][0])         # flipped chain-edge-0 dir
    if apexE[0] % q0 or apexE[1] % q0:
        raise Stuck(f"first certificate: en(R) = {apexE}/{q0} not a lattice "
                    "point (R1 lattice test fails)")
    enR = (apexE[0] // q0, apexE[1] // q0)
    log.append(f"R1/R2: Cor 7.4 at flipped chain edge 0, dir {d0f}, q={q0}: "
               f"l(P) = lam R^{q0}m on the Pred faces, en(R) = {enR} (lattice ok)")
    # ---- (0,c) re-derivation (design S2): candidates for st(R)
    cands = continuations(enR, q0, d0f, False, log, "c-derivation")
    if not cands:
        raise Stuck("no admissible start for the first certified face")
    cs = sorted({q0 * st[0] for st, dd in cands if st[1] == 0})
    log.append(f"c-derivation: (c,0) candidates {cs}; GGV5 table value c={cd.c}"
               + ("" if len(cands) == 1 else
                  " (non-unique: all candidates carried as branches)"))
    # ---- base corners: origin, flipped A0' and integral chain corners
    base = [(0, 0), apexE]
    for e in cd.chain:
        for A in (e.A, e.Ap):
            if A.l == 1:
                base.append((A.b, A.a))
    # ---- last chain edge data (the one that gets cut, GGV5 single root)
    ce = _chain_edge_data(cd, log)
    # The chain-edge cut is sound only if the apex monomial's e_K spread ends
    # at x <= 0: otherwise the cut re-materializes the certified level through
    # the apex on the positive axis (same-level interference), Prop 8.2's
    # exactness hypothesis at the residual vertex fails, and psi_j is blocked.
    # In that case the chain edge is left uncut: a sound partial reduction.
    if ce is not None and apexE[0] - ce["K"] * apexE[1] > 0:
        log.append(f"chain edge kept UNCUT: its e_{ce['K']} cut would respawn "
                   f"the apex level at x = {apexE[0] - ce['K'] * apexE[1]} > 0 "
                   "(interference with the Pred-side certificate); partial "
                   "reduction emitted")
        ce = None
    # ---- branch over start candidates
    leaves = []
    for stR, fdir in cands:
        blog = list(log)
        tag = f"branch st(R)={stR}@{fdir}"
        if stR == (0, 0):
            chains = [[]]
        else:
            chains = lower_boundary(stR, fdir, False, blog, tag)
            if not chains:
                continue
        for chain_pts in chains:
            cpts, axis = _chain_pts([stR] + chain_pts, q0)
            state = mkstate(base + cpts, set(), False, blog,
                            f"{stR}@{fdir}")
            allowed = set(axis)
            if not _axis_ok(state.corners, allowed, blog, tag):
                continue
            for s2, ax2 in _stage_a(cd, state, q0, enR, stR, fdir, allowed,
                                    blog, 0, log):
                if ce is not None:
                    s3, resid = _cut_chain(cd, ce, s2, list(s2.log))
                    leaves.append((s3, resid))
                else:
                    leaves.append((s2, None))
    if not leaves:
        raise Stuck("all branches were killed before emission")
    # ---- R9 + finalize + merge
    emitted = {}
    for state, resid in leaves:
        llog = list(state.log)
        outcomes = []
        if resid is not None:
            V, incoming = resid
            ros = tail_resolve(V, incoming, m, n, llog)
            if not ros:
                llog.append(f"R9 at {V}: every end configuration killed -- "
                            "branch dies")
                continue
            for extra, eP, eQ, fd, lbl in ros:
                outcomes.append((extra, (V, eP, eQ), lbl))
        else:
            outcomes.append(((), None, ""))
        for extra, ends, lbl in outcomes:
            flog = list(llog)
            st2 = state
            if extra:
                st2 = mkstate(list(state.corners) + [e for e in extra],
                              state.prov, state.laurent, flog, state.label)
            NP, NQ, rhs, lines = finalize(st2, cd.mn, ends, cd.name)
            flog += lines
            key = (NP, NQ, rhs)
            if key not in emitted:
                emitted[key] = (st2.label + ("/" + lbl if lbl else ""), flog)
            else:
                emitted[key] = (emitted[key][0], emitted[key][1] +
                                [f"merged branch {st2.label}/{lbl} "
                                 "(identical emitted case)"])
    cases = []
    for i, ((NP, NQ, rhs), (path, flog)) in enumerate(emitted.items(), 1):
        cases.append(Emitted(f"c{i}", NP, NQ, rhs, path))
        log.extend([f"--- emitted case c{i} (branch {path}):",
                    f"    N(P) = {list(NP)}", f"    N(Q) = {list(NQ)}",
                    f"    rhs  = x^{rhs}"] + flog[len(log):])
    return cases

def _chain_edge_data(cd, log):
    "the last chain edge, if it is cuttable with a justified single root"
    e = cd.chain[-1]
    stE, enE = (e.Ap.b, e.Ap.a), (e.A.b, e.A.a)
    if e.A.l != 1 or e.Ap.l != 1:
        log.append("chain edge: fractional corners, not cuttable here")
        return None
    vec = (enE[0] - stE[0], enE[1] - stE[1])
    p = prim(vec)
    if p[1] != 1:
        log.append(f"chain edge {stE}->{enE}: direction step {p} is not "
                   "(K,1); e_K cut impossible (stays as boundary)")
        return None
    K = p[0]
    zdeg = vec[1]
    if cd.final.b != zdeg:
        log.append(f"chain edge {stE}->{enE}: final corner {tuple(cd.final)} "
                   f"has gamma={cd.final.b} != zdeg={zdeg}: multi-root chain "
                   "edge, not supported")
        raise Stuck("multi-root chain edge")
    log.append(f"chain edge {stE}->{enE}: single root of multiplicity {zdeg} "
               f"(final corner {tuple(cd.final)} generated at full gamma, "
               "GGV5 S2); form x^c y^d (z-alpha)^zdeg, z = x^K y, "
               f"K={K}; alpha != 0 since st(P) = m*A0' exactly")
    return dict(stE=stE, enE=enE, K=K, zdeg=zdeg)

def _cut_chain(cd, ce, state, blog):
    "stage B: cut the last chain edge; returns (state, residual or None)"
    stE, enE, K, zdeg = ce["stE"], ce["enE"], ce["K"], ce["zdeg"]
    fs = [f for f in faces(state.corners)
          if {f.st, f.en} == {stE, enE}]
    if not fs:
        raise Stuck(f"chain edge {stE}->{enE} is not a face of "
                    f"{state.corners}")
    pts, prov, contE, collapsed = apply_cut(state, stE, enE, K, 1,
                                            (0, (zdeg,), zdeg), "alpha")
    blog.append(f"T-shift e_{K}(alpha) cuts the chain edge {stE}->{enE} "
                f"(z-alpha)^{zdeg} -> z^{zdeg}; y^{stE[1]} prefactor spawns "
                f"the tail down to {(enE[0] - stE[1] * K, enE[1] - stE[1])}")
    st2 = mkstate(pts, prov, True, blog, state.label)
    resid = None
    if stE[1] > 0:
        V = (enE[0] - stE[1] * K, enE[1] - stE[1])
        resid = (V, outdir((V[0] - enE[0], V[1] - enE[1])))
        blog.append(f"residual vertex {V} with unknown following edge "
                    f"(incoming direction {resid[1]}) -- R9 will run")
    return st2, resid

def _stage_a(cd, state, q, enR, stR, fdir, allowed_axis, blog, depth,
             sink=None):
    """Cut loop on the certified Pred-side face [q*stR, q*enR]; returns a list
    of (state, allowed_axis) leaves.  Recursion: B1 shapes, then either the
    shortened face stays (stop) or B2 continuations (possibly cut again)."""
    if depth > 8:
        raise Stuck("stage A recursion overflow")
    tag = f"stageA[{depth}] face {stR}->{enR} @{fdir}"
    K = -fdir[1] if fdir[0] == 1 else None
    fE, sE = (q * enR[0], q * enR[1]), (q * stR[0], q * stR[1])
    if stR == (0, 0) or K is None or vdir(fdir, enR) <= 0:
        blog.append(f"{tag}: face not cuttable "
                    f"({'v=0 ray' if stR == (0, 0) else 'direction'}) -- kept")
        return [(state, allowed_axis)]
    zdeg = enR[1] - stR[1]
    if zdeg < 1:
        return [(state, allowed_axis)]
    shapes = face_shapes(stR, enR, K, q, {0}, blog, tag)
    out = []
    for z0, parts in shapes:
        t1 = max(parts)
        pts, prov, contE, collapsed = apply_cut(state, sE, fE, K, q,
                                                (z0, parts, t1), "lam")
        blog2 = list(blog)
        blog2.append(f"{tag}: T-shift e_{K}(lam_1) cuts (z-lam_1)^{q * t1}m "
                     f"of the certified form; "
                     + ("face collapses to the apex" if collapsed and contE is None
                        else f"face now starts at {contE}"))
        # everything below the cut face is superseded: its boundary is
        # re-derived, so previously admitted axis corners lose justification
        ax2 = set()
        if contE is None and collapsed and (sE[1] > 0 or z0 > 0):
            contE = (fE[0] - (q * z0 + sE[1]) * K, fE[1] - (q * z0 + sE[1]))
        if contE is not None:
            # shortened face or full collapse with a prefactor tail: derive
            # the boundary below contE
            contR = _to_R(contE, q)
            for st3, ax3 in _below(cd, pts, prov, blog2, state.label, q, contR,
                                   fdir, ax2, tag, sink):
                out.append((st3, ax3))
        else:
            # clean full collapse: B2 continuations at the apex, may cut again
            cands = continuations(enR, q, fdir, True, blog2,
                                  f"{tag} B2 at apex")
            if not cands:
                raise Stuck(f"{tag}: no continuation after full collapse")
            for stR2, fdir2 in cands:
                blog3 = list(blog2)
                blog3.append(f"{tag}: B2 continuation st(R)={stR2}@{fdir2}")
                st3 = mkstate(list(pts) + [(q * stR2[0], q * stR2[1])],
                              prov, True, blog3, state.label + f"|{stR2}@{fdir2}")
                ax3 = set(ax2)
                if stR2[1] == 0 and stR2[0] > 0:
                    ax3.add((q * stR2[0], q * stR2[1]))
                if not _axis_ok(st3.corners, ax3, blog3, tag):
                    if sink is not None:
                        sink.append(blog3[-1])
                    continue
                out.extend(_stage_a(cd, st3, q, enR, stR2, fdir2, ax3,
                                    blog3, depth + 1, sink))
    return out

def _to_R(pE, q):
    if pE[0] % q or pE[1] % q:
        raise Stuck(f"continuation corner {pE} not divisible by q={q}")
    return (pE[0] // q, pE[1] // q)

def _below(cd, pts, prov, blog, label, q, contR, dbound, ax, tag, sink=None):
    "derive the boundary below the corner q*contR and build the states"
    out = []
    if contR == (0, 0) or contR[1] == 0:
        st = mkstate(pts, prov, True, blog, label)
        ax2 = set(ax) | ({(q * contR[0], 0)} if contR[0] > 0 else set())
        if _axis_ok(st.corners, ax2, blog, tag):
            out.append((st, ax2))
        elif sink is not None:
            sink.append(blog[-1])
        return out
    cands = continuations(contR, q, dbound, True, blog, f"{tag} below {contR}")
    if not cands:
        raise Stuck(f"{tag}: no boundary below {contR}")
    for stR2, fdir2 in cands:
        blog2 = list(blog)
        chains = [[stR2]] if stR2 == (0, 0) else \
                 [[stR2] + c for c in lower_boundary(stR2, fdir2, True, blog2,
                                                     tag)]
        for ch in chains:
            cpts, axis = _chain_pts(ch, q)
            blog3 = list(blog2)
            st = mkstate(list(pts) + cpts, prov, True, blog3,
                         label + f"|below{stR2}")
            ax2 = set(ax) | axis
            if _axis_ok(st.corners, ax2, blog3, tag):
                out.append((st, ax2))
            elif sink is not None:
                sink.append(blog3[-1])
    return out

# ---------------------------------------------------------------- runner

def run_section4(verbose=False):
    out = {}
    pllc = get_pllc(60)
    for key, cd in section4_families().items():
        out[key] = reduce_family(cd, pllc)
    return out

# -------------------------- Phase 2c: families above maxdeg 125 (GGV5 S6)

def family_case(a0, b0, mn, deg, final=None):
    "CornerData for the GGV5 S6 row (A0=(a0,b0), (m,n), maxdeg), by final corner"
    from families import chain_path
    for ch, fam, j, mn2, d2 in enumerate_cases(150):
        p0 = chain_path(ch)[0]
        if (int(p0[0]), p0[1], mn2, d2) != (a0, b0, mn, deg):
            continue
        if final is not None and (ch.final.a, ch.final.l, ch.final.b) != final:
            continue
        return corner_data(ch, fam, j, name=f"{a0}_{b0}mn{mn[0]}{mn[1]}d{deg}")
    raise KeyError((a0, b0, mn, deg, final))

# Engine outputs for the first genuinely new reductions (families above
# maxdeg 125, never reduced in the literature).  Status: UNVALIDATED -- these
# are banked regression data produced by this engine, pending independent
# checking (e.g. the design's G4 cross-check lane).  Corner lists are CCW.
ABOVE125_UNVALIDATED = {
    # (11,33)+(2,3), maxdeg 132, chain (11,33)->(19/4,8): full pipeline
    # (one cut, R9 tail resolution), RHS x.
    ("11_33", (2, 3), 132): dict(
        final=(19, 4, 8), cases=[
            (((0, 0), (1, 1), (6, 16), (0, 22)),
             ((0, 0), (1, 0), (9, 24), (0, 33)), 1)]),
    # (9,36)+(2,3), maxdeg 135, chain (9,36)->(9,24)->(11/3,8): partial
    # reduction (the (0,1)->(24,9) chain edge stays uncut: its e_3 would
    # interfere with the Pred-side e_3 certificate), RHS x^2.
    ("9_36", (2, 3), 135): dict(
        final=(11, 3, 8), cases=[
            (((0, 0), (6, 0), (24, 18), (0, 18)),
             ((0, 0), (9, 0), (36, 27), (0, 27)), 2),
            (((0, 0), (4, 0), (8, 2), (24, 18), (0, 18)),
             ((0, 0), (6, 0), (12, 3), (36, 27), (0, 27)), 2)]),
    # (8,40)+(3,2), maxdeg 144, chain (8,40)->(8,28)->(11/4,7): partial
    # reduction (chain edge kept for the same reason), RHS x^3.
    ("8_40", (3, 2), 144): dict(
        final=(11, 4, 7), cases=[
            (((0, 0), (8, 0), (24, 16), (0, 16)),
             ((0, 0), (12, 0), (36, 24), (0, 24)), 3),
            (((0, 0), (6, 0), (10, 2), (24, 16), (0, 16)),
             ((0, 0), (9, 0), (15, 3), (36, 24), (0, 24)), 3),
            (((0, 0), (4, 0), (10, 2), (24, 16), (0, 16)),
             ((0, 0), (6, 0), (15, 3), (36, 24), (0, 24)), 3)]),
}

def run_above125():
    "reduce the banked above-125 families; returns {key: Result}"
    pllc = get_pllc(90)
    out = {}
    for (name, mn, deg), spec in ABOVE125_UNVALIDATED.items():
        a0, b0 = map(int, name.split("_"))
        cd = family_case(a0, b0, mn, deg, spec["final"])
        out[(name, mn, deg)] = reduce_family(cd, pllc)
    return out

if __name__ == "__main__":
    for key, res in sorted(run_section4().items()):
        print(f"== S4 {key}: {res.status}, {len(res.cases)} case(s)")
        for c in res.cases:
            print(f"   {c.label}: N(P)={list(c.NP)}")
            print(f"       N(Q)={list(c.NQ)}  rhs=x^{c.rhs_exp}  [{c.path}]")
    for key, res in run_above125().items():
        print(f"== above-125 {key}: {res.status}, {len(res.cases)} case(s) "
              "[UNVALIDATED]")
        for c in res.cases:
            print(f"   {c.label}: N(P)={list(c.NP)}")
            print(f"       N(Q)={list(c.NQ)}  rhs=x^{c.rhs_exp}")
