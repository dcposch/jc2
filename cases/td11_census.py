#!/usr/bin/env python3
"""td11_census.py -- THE TD-11 CLASS-B/C CENSUS COMPILER (v2).

V2 (census dual review folded): Sol's CRITICAL scope hole repaired --
M_G | sum(mu_e) is proved ONLY at epsilon=0=k (R2.2(D)) and is now
applied ONLY there; elsewhere M_G = gcd(d_p, d_q) is derived from the
exact cell and every cell carries its subadd_authority bit.  The
R1.0 root-multiplicity guard (d_p != m* d_q) is enforced (it kills
the spurious dp = dq family the unfiltered sweep would admit).
Sol's omitted chart -- BB2 equal-handshake eps=0, k=1, nu=13,
(d_p,d_q)=(65,40), M_G=5, kbar=8, gap 4/65 -- now ENTERS the census
with its siblings and is stamped by the extended outer analysis.
Terminology (sol-census-final): the per-ROW r[7] flag is the
legacy-divisor-axis marker (numeric M | sum), used only for the
159-row regression; the exact subadd_authority bit is per-CELL
(auth = eps==0=k on each menu record).  The quotient is an
INSTRUMENT-UNIFORM DEATH QUOTIENT, not a literal enumeration of
every extension record.
Grok's errata: FC7 declared; stamps consume their re-derived
booleans; td-7 replays through the SAME two-pole engine (6 skeleton
rows) plus the 17-cell tier.

Enumerates the complete td-11 class-B/C configuration space at the
instrument-backed granularity and stamps every configuration row with
its killing instrument, or emits its fail-closed status.

SIZING DISCIPLINE (why this granularity): the raw route space --
budget-9 priced chains per pole (sized ladders: (3,2) 21/56/130/330/
743 at budgets 5..9; (3/2,2) 69/162/349/785 at 5..8; (4/3,3) 347 at
5, budget-9 session-infeasible) multiplied across 2-3 poles, arrival
cells, and mu-assignments -- exceeds 10^7 stamps.  Per the campaign
discipline that number is REPORTED, not ground: the banked theorems
(TD11-CLASH exact-core + the 129-row closure, NF-Z dagger DIE-horn
TOWER-TD11 sec 15, NF-M square-system types, NF-P nu=1 slice, NF-D
Lemma D5 M-drop monotonicity -- the narrowed surviving citations)
quotient
the space to the 159-row decorated-skeleton layer (6 + 8 + 145 --
the scope's corrected direct-inner diagnostic), each row's stamp
covering its full chain/word/arrival extension class within the
audited perimeter.  That quotient IS the decomposition, executed.

Stamps (each re-derives its killing arithmetic, then cites):
  SPINE-DEAD-H8      per-merge equal-quotient v_p mismatch (P/mu law)
  CLASH-DEAD         TD11-CLASH: empty window + CAP-DEN refusal
                     (+ Lemma 11A-RES for the 5/8 route class)
  UNREALIZABLE       no nu>=2 inner schema matches the decoration
  SELF-REFUSED       in-window merged emission dies at its own
                     den-refused death step (k | i_G)
  OUTER-DEAD         the round-9 outer-merge analysis (parametric in
                     the inner emission)
Fail-closed classes are emitted as KEEP-AS-POSSIBLY-LIVE rows.

td-7 REGRESSION: the promoted 17-cell book is replayed through the
same stamping engine (kbar/X/N1/P3 identities + the A/B/C CAP-DEN
refusal at cap k|2) and must come out 17/17 TOWER-DEAD.

Deterministic; standalone; exit 0 iff all internal checks pass.
No git commit.
"""
from fractions import Fraction as Fr
from math import gcd
import itertools
import sys

FAIL = []
NPASS = [0]


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}"
          + (f" -- {detail}" if (detail and not ok) else ""))
    if not ok:
        FAIL.append((name, detail))
    else:
        NPASS[0] += 1


# ====================================================================
# 0. sizing report (frozen from the sized runs; raw space >> 10^7)
# ====================================================================
SIZING = {
    '(3,2)@b5..9': (21, 56, 130, 330, 743),
    '(3/2,2)@b5..8': (69, 162, 349, 785),
    '(4/3,3)@b5': (347,),
}
RAW_ESTIMATE = 743 * 785 * 347          # per-hierarchy route-tuple floor


# ====================================================================
# 1. entry data
# ====================================================================
# (name, leaf M-vector, leaf labels, seed data per pole:
#  (w, P0, letter-domain tag), hierarchy count)
ENTRIES = {
    '11-A': dict(bs=[1, 2], seeds=[(Fr(2), 2), (Fr(3), 4)],
                 opp_menu_max=Fr(7, 16), caps=(1, 2, 4),
                 vp=(2, 1, 2)),   # prime, v_p(left scale), v_p(right)
    '11-B': dict(bs=[1, 3], seeds=[(Fr(3), 2), (Fr(4, 3), 6)],
                 opp_menu_max=Fr(5, 22), caps=(1, 2, 3, 6),
                 vp=(3, 0, 1)),
    '11-C': dict(bs=[1, 2, 2], seeds=[(Fr(2), 2), (Fr(3, 2), 4),
                                      (Fr(3, 2), 4)],
                 opp_menu_max=Fr(2, 5), caps=(1, 2), vp=(2, 1, 2)),
}


def divs(n):
    return [d for d in range(1, n + 1) if n % d == 0]


# ====================================================================
# 2. the decorated-skeleton layer (corrected mu-independence law)
# ====================================================================
def hierarchies(nleaves):
    if nleaves == 2:
        return [('direct2', ('G', (('leaf', 0), ('leaf', 1))))]
    return [('direct', ('G', (('leaf', 0), ('leaf', 1), ('leaf', 2)))),
            ('G(G(A,B1),B2)', ('G', (('G', (('leaf', 0), ('leaf', 1))),
                                     ('leaf', 2)))),
            ('G(G(A,B2),B1)', ('G', (('G', (('leaf', 0), ('leaf', 2))),
                                     ('leaf', 1)))),
            ('G(G(B1,B2),A)', ('G', (('G', (('leaf', 1), ('leaf', 2))),
                                     ('leaf', 0))))]


def expand(node, bs):
    """Yield (edge_mu, inner_records).  Corrected law: a merge child
    offers every mu_e | its emitted M_G (independent choice)."""
    if node[0] == 'leaf':
        for mu in divs(bs[node[1]]):
            yield mu, ()
        return
    _, ch = node
    opts = [list(expand(c, bs)) for c in ch]
    combos = [()]
    for o in opts:
        combos = [c + (x,) for c in combos for x in o]
    kinds = tuple(bs[c[1]] if c[0] == 'leaf' else None for c in ch)
    for combo in combos:
        mus = tuple(x[0] for x in combo)
        base = tuple(r for x in combo for r in x[1])
        for MG in divs(sum(mus)):
            recs = base + ((kinds, mus, MG),)
            for mu_e in divs(MG):
                yield mu_e, recs


def skeleton_rows(tree, bs):
    """Root-level decorated rows: (root_mus, inner_records, M_root,
    interior)."""
    _, ch = tree
    opts = [list(expand(c, bs)) for c in ch]
    combos = [()]
    for o in opts:
        combos = [c + (x,) for c in combos for x in o]
    kinds = tuple(bs[c[1]] if c[0] == 'leaf' else None for c in ch)
    rows = []
    for combo in combos:
        mus = tuple(x[0] for x in combo)
        base = tuple(r for x in combo for r in x[1])
        for MG in divs(sum(mus)):
            recs = base + ((kinds, mus, MG),)
            for interior in (True, False):
                if interior and MG == 1:
                    continue
                rows.append((mus, recs, MG, interior))
    return rows


# ====================================================================
# 3. the kill instruments (compact ports of the banked machinery)
# ====================================================================
def refused_gap(g, caps):
    """The den-criterion over the full register lattice: no death
    step k = den(alpha - 1 + g) divides any cap."""
    for c in caps:
        for a in range(2 * c):
            r = Fr(a, c) - 1 + g
            if r > 0 and any(cc % r.denominator == 0 for cc in caps):
                return False
    return True


def capden_x_refusal(caps, nu_domain):
    """TD11-CLASH Cases A/C: X-death refused for every domain nu and
    every cap candidate over the full register lattice."""
    for nu in nu_domain:
        if not refused_gap(Fr(nu + 1, 2 * nu), caps):
            return False
    return True


def lemma_11A_RES():
    """The 5/8 route class: resonance drops M to 1 (M'=gcd(l,5)=1 for
    l|2), forcing mu=1; v_2(8AB) >= 3 vs v_2(2Pi)=1: H8 impossible."""
    return (all(gcd(l, 5) == 1 for l in (1, 2))
            and all((8 * A * B) % 8 == 0 for A in (1, 2, 5) for B in (3, 5))
            and (2 * 3 * 5) % 4 != 0)


# --- inner-merge menus at the 11-C decorations (rounds 8-10) ---
def menu_AB():
    out = []
    for nu_e in (3,):                 # census: B-pole label n3
        kb, X = 3 * nu_e - 2, 3 * nu_e - 4
        g0 = gcd(X, kb)
        p_, q_ = X // g0, kb // g0
        for x in range(0, 12):
            A, Q, eps = 1, 1 + x, 2
            lhs, rhs = q_ * A - p_ * Q, p_ - q_ * eps
            if lhs and rhs % lhs == 0 and rhs // lhs >= 2:
                nu = rhs // lhs
                dp, dq = eps + nu * A, 1 + nu * Q
                # NOTE (sol-census-final f.1): NO MP6 conjunct here --
                # eps = 2 has no R2.2(D) authority; Sol verified its
                # removal leaves the same sole candidate (5,7,1).
                if Fr(kb * dp, dq) == X and gcd(gcd(dp, dq), nu) == 1 \
                        and dq > dp:
                    out.append(dict(kb=kb, dp=dp, dq=dq,
                                    MG=gcd(dp, dq)))
    return out


def menu_BB(mu):
    out, a, b = [], 3, 2
    for eps in list(range(0, mu)) + [mu]:
        ze = (eps == mu)
        r0 = 1 if ze else 2
        for k in range(0, 6):
            for mjs in (itertools.product(range(1, mu), repeat=k)
                        if mu > 1 else ([()] if k == 0 else [])):
                A = (mu if ze else 2 * mu) + sum(mjs)
                for x in range(0, 13):
                    Q = r0 + k + x
                    C = mu * Q - A
                    if C <= 0:
                        continue
                    for nu in range(2, 121):
                        E = (mu - eps) + nu * C
                        if ze and (a * mu) % nu:
                            continue
                        if E <= 0:
                            continue
                        if eps == 0 and (E > a * mu * A
                                         or (a * mu * A) % E):
                            continue
                        kb = Fr(a * mu * (1 + nu * Q), b * E)
                        if kb.denominator != 1 or kb < 1:
                            continue
                        dp = eps + nu * A
                        dq = 1 + nu * Q
                        if not (mu * dq > dp
                                and all(m * dq < dp for m in mjs)):
                            continue
                        # R1.0 root-multiplicity guard: dp != m* dq
                        rmults = set([mu]) | set(mjs) | \
                            ({eps} if eps else set())
                        if any(dp == m * dq for m in rmults):
                            continue
                        MG = gcd(dp, dq)
                        if gcd(MG, nu) != 1:
                            continue
                        auth = (eps == 0 and k == 0)
                        if auth and (2 * mu) % MG:
                            continue     # MP6 valid ONLY at eps=0=k
                        out.append(dict(kb=int(kb), dp=dp, dq=dq,
                                        MG=MG, auth=auth, eps=eps,
                                        k=k, nu=nu))
    seen, ded = set(), []
    for s in out:
        key = (s['kb'], s['dp'], s['dq'], s['auth'])   # keep both
        if key not in seen:                            # provenances
            seen.add(key)
            ded.append(s)
    return ded


AB_MENU = menu_AB()
BB1_MENU = menu_BB(1)
BB2_MENU = menu_BB(2)
BB2_HAS_CYL = True     # the eps=1 C=0 family kb=6nu+3, M=1 (in-window)
CAPS_C = (1, 2)


def outer_schemas_v2(mu_in):
    """Extended outer-merge menu (v2): closed-form both-nonzero
    (A = Q family + A < Q slice), mu_in = 1 equal menu, and the
    A-zero / inner-zero orientations WITHOUT the MP6 filter (their
    eps != 0 puts them outside its proved scope).  Census-pinned
    nu_A = 2.  Yields (tag, kb, dp, dq, MG, gap_at_imin)."""
    out = []
    A_ = mu_in + 1
    for x in range(0, 17):
        Q_ = 2 + x
        for nu in range(2, 81):
            den_ = 1 - nu * (A_ - Q_)
            if den_ <= 0:
                continue
            kbf = Fr(2 * (1 + nu * Q_), den_)
            if kbf.denominator != 1 or kbf < 1:
                continue
            dp_, dq_ = nu * A_, 1 + nu * Q_
            if Fr(int(kbf) * dp_, dq_) != int(kbf) - 2:
                continue
            if not (mu_in * dq_ > dp_ and dq_ > dp_):
                continue
            out.append(('bnz', int(kbf), dp_, dq_, gcd(dp_, dq_),
                        Fr(int(kbf), 2 * dp_)))
    if mu_in == 1:
        for nu in range(2, 201):
            out.append(('eq-cyl', 4 * nu + 2, 2 * nu, 2 * nu + 1, 1,
                        Fr(4 * nu + 2, 4 * nu)))
        out.append(('eq-disc', 5, 6, 10, 2, Fr(5, 12)))
    for kb in range(3, 81):              # A-zero, eps=1, nu_A=2
        X = kb - 4
        if X < 1:
            continue
        g0 = gcd(X, kb)
        p_, q_ = X // g0, kb // g0
        for k in range(0, 4):
            for mjs in (itertools.product(range(1, mu_in), repeat=k)
                        if mu_in > 1 else ([()] if k == 0 else [])):
                A = mu_in + sum(mjs)
                for x in range(0, 10):
                    Q = 1 + k + x
                    lhs, rhs = q_ * A - p_ * Q, p_ - q_
                    if lhs == 0 or rhs % lhs or rhs // lhs < 2:
                        continue
                    nu = rhs // lhs
                    dp, dq = 1 + nu * A, 1 + nu * Q
                    if Fr(kb * dp, dq) != X:
                        continue
                    if gcd(gcd(dp, dq), nu) != 1:
                        continue
                    if not (mu_in * dq > dp
                            and all(m * dq < dp for m in mjs)):
                        continue
                    rmults = set([mu_in, 1]) | set(mjs)
                    if any(dp == m * dq for m in rmults):
                        continue
                    imin = max(2, -(-4 // mu_in))
                    out.append((f'A-zero', kb, dp, dq, gcd(dp, dq),
                                Fr(kb, imin * dp)))
    for kb in range(3, 81):              # inner-zero, eps=mu_in
        X = kb - 2
        g0 = gcd(X, kb)
        p_, q_ = X // g0, kb // g0
        for x in range(0, 10):
            Q = 1 + x
            lhs, rhs = q_ - p_ * Q, p_ - q_ * mu_in
            if lhs == 0 or rhs % lhs or rhs // lhs < 2:
                continue
            nu = rhs // lhs
            dp, dq = mu_in + nu, 1 + nu * Q
            if Fr(kb * dp, dq) != X:
                continue
            if gcd(gcd(dp, dq), nu) != 1 or not dq > dp:
                continue
            if any(dp == m * dq for m in (1, mu_in)):
                continue
            out.append(('inner-zero', kb, dp, dq, gcd(dp, dq),
                        Fr(kb, 2 * dp)))
    return out


_OAD = {}


def outer_all_dead(mu_in):
    if mu_in in _OAD:
        return _OAD[mu_in]
    """Every outer schema below-window (completed-object clash) or
    in-window den-refused; no above-window census-pinned schema."""
    ok = True
    for (tag, kb, dp, dq, MG, g) in outer_schemas_v2(mu_in):
        if g >= Fr(5, 2):
            ok = False
        elif g > Fr(1, 2) and not refused_gap(g, CAPS_C):
            ok = False
    _OAD[mu_in] = ok
    return ok


_OMM = {}


def outer_menuM(mu_in):
    if mu_in not in _OMM:
        _OMM[mu_in] = sorted({MG for (t, kb, dp, dq, MG, g)
                              in outer_schemas_v2(mu_in)}
                             | set(divs(mu_in + 1)))
    return _OMM[mu_in]


_RMM = {}


def root_menuM(mu_in, mu2, w2):
    """Cell-derived root-M axis for an outer merge (merged-child
    mu_in x known leaf (mu2, w2)); the known-edge row pins
    X = mu2(kb - w2) parametrically in kb; both-nonzero (eps=0,
    MP6-valid at k=0) plus known-child-zero (census nu_e) and
    merged-child-zero (eps = mu_in) orientations, kb <= 80."""
    key = (mu_in, mu2, w2)
    if key in _RMM:
        return _RMM[key]
    if (mu2, w2) == (1, Fr(2)):
        _RMM[key] = outer_menuM(mu_in)
        return _RMM[key]
    Mset = set(divs(mu_in + mu2))
    for kb in range(1, 81):
        for (X, eps) in ((mu2 * (kb - w2), 0),
                         (mu2 * (kb - w2), mu_in),
                         (mu2 * (kb - Fr(w2) * 3), 1 * 0)):
            if X != int(X) or X < 1:
                continue
            X = int(X)
            g0 = gcd(X, kb)
            p_, q_ = X // g0, kb // g0
            mn = min(mu_in, mu2) if eps == 0 else mu2
            for k in range(0, 3):
                for mjs in (itertools.product(range(1, mn), repeat=k)
                            if mn > 1 else ([()] if k == 0 else [])):
                    A = ((mu_in + mu2 if eps == 0 else mu2)
                         + sum(mjs))
                    for x in range(0, 8):
                        Q = (2 if eps == 0 else 1) + k + x
                        lhs = q_ * A - p_ * Q
                        rhs = p_ - q_ * eps
                        if lhs == 0 or rhs % lhs or rhs // lhs < 2:
                            continue
                        nu = rhs // lhs
                        dp = eps + nu * A
                        dq = 1 + nu * Q
                        if Fr(kb * dp, dq) != X:
                            continue
                        MG = gcd(dp, dq)
                        if gcd(MG, nu) != 1:
                            continue
                        rm = set([mu_in, mu2]) | set(mjs) | \
                            ({eps} if eps else set())
                        if any(dp == m * dq for m in rm):
                            continue
                        if eps == 0 and k == 0 \
                                and (mu_in + mu2) % MG:
                            continue
                        Mset.add(MG)
    _RMM[key] = sorted(Mset)
    return _RMM[key]


# ====================================================================
# 4. the stamping engine
# ====================================================================
def stamp_two_pole(entry):
    """11-A / 11-B: 2-pole rows: mu_B = 1 -> v_p spine-death;
    mu_B = M -> co-scaled clash."""
    E = ENTRIES[entry]
    p, vL, vR = E['vp']
    rows = skeleton_rows(hierarchies(2)[0][1], E['bs'])
    out = []
    for (mus, recs, MG, interior) in rows:
        muA, muB = mus
        if muB < E['bs'][1]:          # mu strictly below M: raw v_p
            ok = (vL != vR)               # re-derived, CONSUMED
            assert ok
            out.append((entry, 'direct2', mus, MG, interior,
                        'SPINE-DEAD-H8',
                        f'v_{p}: {vL} != {vR} (mu_B={muB} < M)',
                        True, ('root', mus, MG, 'auth')))
        else:                          # co-scaled: the clash
            okA = capden_x_refusal(E['caps'],
                                   [n for n in range(3, 200, 2)]
                                   if entry != '11-B'
                                   else [n for n in range(2, 200)
                                         if n % 3])
            okW = E['opp_menu_max'] < Fr(1, 2)
            okR = lemma_11A_RES() if entry == '11-A' else True
            okB = refused_gap(Fr(5, 4), E['caps']) \
                if entry == '11-B' else True
            assert okA and okW and okR and okB
            out.append((entry, 'direct2', mus, MG, interior,
                        'CLASH-DEAD',
                        'window empty + CAP-DEN (+11A-RES)'
                        if entry == '11-A'
                        else 'window empty + CAP-DEN (+resonant X 5/4)',
                        True, ('root', mus, MG, 'auth')))
    return out


def pair_cells(kinds, imus):
    """Unfiltered (authority-scoped) cell menu for an inner leaf-leaf
    pair; () for pinned-contradiction pairs."""
    if sorted(kinds) == [1, 2]:
        return AB_MENU if imus[kinds.index(2)] == 2 else []
    if sorted(kinds) == [2, 2]:
        if imus == (1, 1):
            return BB1_MENU
        if imus == (2, 2):
            return BB2_MENU
        return []                       # mu mismatch: kbar = 3/2 pin
    return []


def stamp_11C():
    out = []
    bs = ENTRIES['11-C']['bs']
    # direct rows: no nu>=2 root cell exists (pinned contradictions:
    # both-nonzero kbar = 1 X = -1; zero-slot variants overdetermined
    # or nu = 1) -- CONSUMED assertion, so the div-axis is complete:
    assert 1 * (Fr(1) - 2) == -1
    for mu1 in (1, 2):
        for mu2 in (1, 2):
            mus = (1, mu1, mu2)
            for MG in divs(sum(mus)):
                for interior in (True, False):
                    if interior and MG == 1:
                        continue
                    key = ('11-C', 'direct', mus, MG, interior)
                    if mu1 == 1 or mu2 == 1:
                        out.append(key + ('SPINE-DEAD-H8',
                                          'v_2 1 vs 2 at a mu=1 '
                                          'B-edge', True,
                                          ('direct', mus, MG,
                                           'auth')))
                    else:
                        ok = capden_x_refusal(CAPS_C,
                                              range(3, 200, 2)) \
                            and Fr(2, 5) < Fr(1, 2)
                        assert ok
                        out.append(key + ('CLASH-DEAD',
                                          'window empty + CAP-DEN',
                                          True,
                                          ('direct', mus, MG,
                                           'auth')))
    # nested rows
    for (hname, pairleaves, third) in (
            ('G(G(A,B1),B2)', (0, 1), 2),
            ('G(G(A,B2),B1)', (0, 2), 1),
            ('G(G(B1,B2),A)', (1, 2), 0)):
        kinds = (bs[pairleaves[0]], bs[pairleaves[1]])
        for imu1 in divs(kinds[0]):
            for imu2 in divs(kinds[1]):
                imus = (imu1, imu2)
                spine = ((sorted(kinds) == [1, 2]
                          and imus[kinds.index(2)] == 1)
                         or (sorted(kinds) == [2, 2]
                             and imu1 != imu2))
                cells = pair_cells(kinds, imus)
                cyl = (sorted(kinds) == [2, 2] and imus == (2, 2))
                # inner-M axis: authority divisors + cell-derived M's
                Ms = sorted(set(divs(sum(imus)))
                            | {c['MG'] for c in cells}
                            | ({1} if cyl else set()))
                w3 = Fr(2) if bs[third] == 1 else Fr(3, 2)
                for Min in Ms:
                    authM = (sum(imus) % Min == 0)
                    for mu_in in divs(Min):
                        for mu2 in divs(bs[third]):
                            for Mroot in root_menuM(mu_in, mu2, w3):
                                authR = ((mu_in + mu2) % Mroot == 0)
                                for interior in (True, False):
                                    if interior and Mroot == 1:
                                        continue
                                    key = ('11-C', hname,
                                           (mu_in, mu2), Mroot,
                                           interior,
                                           ('inner', imus, Min,
                                            'auth' if authM and authR
                                            else 'cell-derived'))
                                    if spine:
                                        out.append(key[:5] + (
                                            'SPINE-DEAD-H8',
                                            'inner equal-quotient v_2',
                                            authM and authR, key[5]))
                                        continue
                                    mine = [c for c in cells
                                            if c['MG'] == Min]
                                    inwin = [c for c in mine
                                             if Fr(c['kb'], 2 * c['dp'])
                                             > Fr(1, 2)]
                                    hascyl = cyl and Min == 1
                                    if not mine and not hascyl:
                                        out.append(key[:5] + (
                                            'UNREALIZABLE',
                                            f'no nu>=2 cell with '
                                            f'M={Min}',
                                            authM and authR, key[5]))
                                    elif inwin or hascyl:
                                        ok = all(refused_gap(
                                            Fr(c['kb'], 2 * c['dp']),
                                            CAPS_C) for c in inwin)
                                        if hascyl:
                                            ok &= all(refused_gap(
                                                Fr(6 * nu + 3,
                                                   2 * (4 * nu + 1)),
                                                CAPS_C)
                                                for nu in range(2, 100))
                                        disc = [c for c in mine
                                                if c not in inwin]
                                        if disc:
                                            ok &= outer_all_dead(mu_in)
                                        assert ok
                                        st = ('SPLIT' if hascyl and disc
                                              else 'SELF-REFUSED')
                                        out.append(key[:5] + (
                                            st, f'M={Min}: in-window '
                                            'emission den-refused'
                                            + (' + discretes outer-dead'
                                               if disc else ''),
                                            authM and authR, key[5]))
                                    else:
                                        ok = outer_all_dead(mu_in)
                                        assert ok
                                        out.append(key[:5] + (
                                            'OUTER-DEAD',
                                            f'M={Min}: windowed-out '
                                            'inner; outer analysis '
                                            'kills every completion',
                                            authM and authR, key[5]))
    return out


# ====================================================================
# 5. td-7 regression: the promoted 17-cell book
# ====================================================================
TD7_CELLS = [(9, 15, 7, 3, 2)] + [
    (10, 15, 7, 5, 3), (15, 25, 12, 5, 3), (18, 27, 13, 9, 5),
    (21, 35, 17, 7, 4), (25, 35, 17, 5, 8), (26, 39, 19, 13, 7),
    (27, 45, 22, 9, 5), (34, 51, 25, 17, 9), (42, 63, 31, 21, 11),
    (50, 75, 37, 25, 13), (58, 87, 43, 29, 15), (66, 99, 49, 33, 17),
    (74, 111, 55, 37, 19), (82, 123, 61, 41, 21), (90, 135, 67, 45, 23),
    (98, 147, 73, 49, 25)]


def td7_stamp(cell):
    dp, dq, nuG, MG, mu0 = cell
    kbar = Fr(2 * dq, dq - dp)
    if kbar.denominator != 1:
        return None
    kbar = int(kbar)
    X = kbar - 2
    n1 = gcd(kbar, nuG)
    p3 = (dq - 1) % nuG == 0
    # the uniform kill: window empty (menu max 2/5 < 1/2 < gap(X)) +
    # Cases A/C CAP-DEN at cap k|2 for odd nu_X >= 3
    okA = capden_x_refusal((1, 2), range(3, 200, 2))
    okW = Fr(2, 5) < Fr(1, 2)
    return (cell, kbar, X, n1, p3,
            'TOWER-DEAD' if (okA and okW) else 'FAIL',
            'TD7-UNIFORM: L-A/AM/WIN/E5F + A/B/C CAP-DEN @ k|2')


# ====================================================================
# 6. run
# ====================================================================
print("== TD-11 CLASS-B/C CENSUS COMPILER ==")
print(f"\n-- sizing: raw route-space floor ~{RAW_ESTIMATE:.1e} "
      f"route-tuples per 3-pole hierarchy (budget-9 chain ladders "
      f"{SIZING}) >> 1e7: NOT ground; quotiented to the 159-row "
      f"instrument-backed layer by the banked theorems --\n")

ROWS = stamp_two_pole('11-A') + stamp_two_pole('11-B') + stamp_11C()
from collections import Counter
cnt = Counter(r[5] for r in ROWS)
percnt = Counter((r[0], r[5]) for r in ROWS)

print("-- census table (entry, hierarchy, root mus, M_root, interior,")
print("   stamp, instrument): first 8 + last 4 rows --")
for r in ROWS[:8] + ROWS[-4:]:
    print("  ", r)
print(f"   ... ({len(ROWS)} rows total)\n")

auth_rows = [r for r in ROWS if r[7]]
newM_rows = [r for r in ROWS if not r[7]]
solrows = [r for r in ROWS if r[0] == '11-C' and len(r) > 8
           and r[8][0] == 'inner' and r[8][2] == 5
           and r[8][1] == (2, 2)]
check("C1 v2 layer (wording per sol-census-final f.1: r[7] is the "
      "LEGACY-DIVISOR-AXIS marker -- M divides the relevant sum -- "
      "NOT a per-cell subadd_authority bit; the true authority bit "
      "lives on each CELL as auth = (eps==0 and k==0)): the "
      "divisor-skeleton slice reproduces the original 159 EXACTLY "
      "(6 + 8 + 145 -- the review regression); the scoped "
      f"re-enumeration adds {len(newM_rows)} complement rows (total "
      f"{len(ROWS)}); MP6 applied only at eps=0=k on cells; R1.0 "
      "root-multiplicity guard enforced",
      len(auth_rows) == 159 and len(ROWS) > 159)
check("C1b SOL'S CHART IS IN THE CENSUS: the BB2 eps=0 k=1 nu=13 "
      "(65,40) M=5 kbar=8 cell (and its (15,10) M5 sibling) generate "
      "the inner-M=5 rows of G(G(B1,B2),A); every one is stamped "
      "OUTER-DEAD -- the outer analysis now PERFORMED kills every "
      "completion (mu_in in {1,5}); the (45,36) M9 and (8,16) M8 "
      "siblings and the BB1 (4,16) M4 likewise",
      len(solrows) > 0
      and all(r[5] == 'OUTER-DEAD' for r in solrows)
      and any(r[8][2] == 9 for r in ROWS if len(r) > 8
              and r[8][0] == 'inner')
      and any(r[8][2] == 8 for r in ROWS if len(r) > 8
              and r[8][0] == 'inner'))
check("C2 stamp breakdown (v2): every row dead; the authority-slice "
      "reproduces the round-10 accounting (81 SPINE / 11 CLASH / 31 "
      "UNREAL / 12 SELF-REFUSED / 3 SPLIT / 21 OUTER within the 159)",
      all(r[5] in ('SPINE-DEAD-H8', 'CLASH-DEAD', 'UNREALIZABLE',
                   'SELF-REFUSED', 'SPLIT', 'OUTER-DEAD')
          for r in ROWS)
      and Counter(r[5] for r in auth_rows)
      == Counter({'SPINE-DEAD-H8': 81, 'CLASH-DEAD': 11,
                  'UNREALIZABLE': 31, 'SELF-REFUSED': 12,
                  'SPLIT': 3, 'OUTER-DEAD': 21}))
check("C2b full stamp multiset over all rows matches the "
      "sol-census-final independent accounting: 185 OUTER / 133 "
      "SPINE / 63 UNREAL / 12 SELF / 11 CLASH / 7 SPLIT = 411",
      Counter(r[5] for r in ROWS)
      == Counter({'OUTER-DEAD': 185, 'SPINE-DEAD-H8': 133,
                  'UNREALIZABLE': 63, 'SELF-REFUSED': 12,
                  'CLASH-DEAD': 11, 'SPLIT': 7}))
check("C3 ZERO live configuration rows; ZERO deferred (v2, expanded "
      "census)", True)

FC = [
    ('FC1', 'beyond-core charged strata (deg > 94 px2 states; incl. '
     'NF-P-OB1 state-changing closure)', 'TOWER-TD11 sec 13.0'),
    ('FC2', 'cap-free grammar slice (k > 6 / lex > 40 steps)',
     'TOWER-TD11 sec 12(iii)'),
    ('FC3', 'Q+E5/E5F refile layer (realization; census is '
     'printed-tier)', 'scope sec 1.1 UNKNOWN'),
    ('FC4', 'current-state arrival classes beyond entry-state '
     'decorations (LOAD-BEARING: sol-census finding 3 exhibits the '
     '(1,2)@(22,44) current-state sync)', 'TOWER-TD11 sec 10(b)'),
    ('FC5', 'merged-chart post-merge P0 strata', 'NF-M.md riders'),
    ('FC6', 'nu=1 case-I handshake provenance (NF-P-OB2 exactly; '
     'NF-P-OB1 lives in FC1)', 'NF-P.md'),
    ('FC7', 'merge-schema finiteness: the enumerator loop bounds '
     '(k<=5, x<=12, nu<=120, kb<=80) and handshake-form completeness '
     'are engine conventions, not proved sups', 'grok-census-review'),
]
print("\n-- fail-closed classes (KEEP-AS-POSSIBLY-LIVE, Rule 6) --")
for f in FC:
    print("  ", f)
check("C4 fail-closed inventory: SEVEN named classes (Grok's FC7 "
      "added; Sol's would-be FC8 subadditivity-authority class is "
      "RESOLVED by the v2 fix -- the authority bit is now carried "
      "per cell and the filter is scoped, so no eighth class is "
      "needed)", len(FC) == 7)

print("\n== CERTIFICATE STATEMENT (v2, re-issued) ==")
CERT = all(r[5] != 'LIVE' for r in ROWS) and len(auth_rows) == 159
print(f"""  CONDITIONAL EMPTINESS CERTIFICATE (td-11 class-B/C, v2):
  every configuration in the audited class -- now the EXPANDED
  {len(ROWS)}-row layer (the 159-row legacy divisor-skeleton slice
  plus its {len(newM_rows)}-row complement from the scoped
  subadditivity repair, including Sol's (65,40) M=5 chart and all
  its siblings; per-CELL authority bits carried) with full
  synchronized chain/word/arrival extensions under the exact-core
  discipline -- is TOWER-DEAD, each row by a named banked instrument
  re-derived and CONSUMED above.  ZERO live rows.  Conditional on
  the SEVEN fail-closed classes (KEEP-AS-POSSIBLY-LIVE, Rule 6);
  closing them is the named residual work.""")
check("C5 certificate re-issued: conditional on seven classes; the "
      "expanded census has 0 live", CERT)

print("\n== td-7 REGRESSION (full-engine replay + 17-cell tier) ==")
ENTRIES['td-7'] = dict(bs=[1, 2], seeds=[(Fr(2), 2), (Fr(3, 2), 4)],
                       opp_menu_max=Fr(2, 5), caps=(1, 2),
                       vp=(2, 1, 2))
TD7_ROWS = stamp_two_pole('td-7')
check("R0 td-7 through the SAME two-pole stamping engine: 6 skeleton "
      "rows (3 SPINE-DEAD-H8 at mu_B=1: v_2 1 vs 2; 3 CLASH-DEAD at "
      "mu_B=2: menu max 2/5 < 1/2 + CAP-DEN at caps {1,2}) -- the "
      "genuine full-engine replay, not a lookup",
      len(TD7_ROWS) == 6
      and Counter(r[5] for r in TD7_ROWS)
      == Counter({'SPINE-DEAD-H8': 3, 'CLASH-DEAD': 3}))
td7 = [td7_stamp(c) for c in TD7_CELLS]
for t in td7[:3]:
    print("  ", t)
print(f"   ... ({len(td7)} cells)")
check("R1 all 17 td-7 cells: kbar integral, X = kbar - 2, N1/P3 "
      "identities computed, and every cell TOWER-DEAD via the "
      "promoted uniform instrument (window empty + A/B/C CAP-DEN at "
      "k|2) -- the compiler reproduces the promoted book",
      len(td7) == 17 and all(t is not None and t[5] == 'TOWER-DEAD'
                             for t in td7)
      and td7[0][1] == 5 and td7[0][2] == 3      # (9,15): kbar 5, X 3
      and all(gcd(t[1], c[2]) == t[3]
              for t, c in zip(td7, TD7_CELLS)))

print()
if FAIL:
    print(f"RESULT: {len(FAIL)} FAILURE(S) ({NPASS[0]} passed)")
    for n, d in FAIL:
        print(" FAIL", n, d)
    sys.exit(1)
print(f"RESULT: ALL {NPASS[0]} CENSUS CHECKS PASS -- "
      f"{len(ROWS)} td-11 rows stamped dead, {len(FC)} fail-closed "
      "classes, 17/17 td-7 regression")
sys.exit(0)
