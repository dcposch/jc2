#!/usr/bin/env python3
"""
box/g9966hurwitz-20260903/rh_driver.py -- Riemann-Hurwitz for f on the fibre C_c = {g = c}
evaluated on the g_c-root contact trees of (99,66) branch B, (99,66) delta = 5/2, and Moh's (64,48).

Lane g9966-hurwitz-fable5-20260903.  Exact arithmetic (fractions).  Standard library + mpmath (calibration only).

Conventions (Xu 1604.07683v4 p.1-2, Moh 1983): x = t^-1; roots alpha of g - c in K<<t>>; ord = ord_t;
contact(alpha, beta) = ord_t(alpha - beta); S_g(alpha) = -ord_t g_y(alpha) = -sum_{beta != alpha} contact(alpha, beta).
Lemma E (report Sec.1): at a root alpha of g - c of a Keller pair, ord_t(f(alpha) - a_0) = S_g(alpha) - 1 exactly
(Lemma 4.1 with g(alpha)' = 0), so at the place P of ramification e (over x) the f-ramification is
e_P = e*|S_g(alpha) - 1|; proper (pole) iff S_g < 1, non-proper iff S_g > 1; S_g = 1 impossible.

Tree encoding: node = (level, [children]) where level = mutual contact of the roots of distinct children;
leaf = ('leaf', count, e) = `count` roots with identical contact profile, each of ramification e.
"""
from fractions import Fraction as F
import json, sys

def leaves(node, path=()):
    """yield (leaf_id, count, e, ancestor-levels tuple)"""
    if node[0] == 'leaf':
        yield (path, node[1], node[2], ())
        return
    level, kids = node
    for i, k in enumerate(kids):
        for (lid, cnt, e, anc) in leaves(k, path + (i,)):
            yield (lid, cnt, e, (level,) + anc)

def contact_of(anc_a, anc_b, la, lb):
    """contact between a root in leaf la and a root in leaf lb: level of the lowest common ancestor.
       Same leaf: the deepest level (the level of the leaf's parent)."""
    if la == lb:
        return anc_a[-1]
    k = 0
    while k < len(la) and k < len(lb) and la[k] == lb[k]:
        k += 1
    return anc_a[k]

def analyse(name, n, tree, expected_N=None):
    L = list(leaves(tree))
    rows = []
    for (la, ca, ea, anca) in L:
        S = F(0)
        for (lb, cb, eb, ancb) in L:
            c = contact_of(anca, ancb, la, lb)
            mult = cb - 1 if la == lb else cb
            S -= mult * c
        if S > 1:
            assert S == anca[-1], ('non-proper packet must separate exactly at ord g = 0: S_g = final level', la, S, anca[-1])
        rows.append(dict(leaf=la, count=ca, e=ea, S=S))
    tot = sum(r['count'] for r in rows)
    assert tot == n, (tot, n)
    N = sum(r['count'] * (1 - r['S']) for r in rows if r['S'] < 1)
    r_prop = sum(F(r['count'], r['e']) for r in rows if r['S'] < 1)
    r_np = sum(F(r['count'], r['e']) for r in rows if r['S'] > 1)
    assert all(r['S'] != 1 for r in rows)
    r_tot = r_prop + r_np
    sum_np = sum(r['count'] * (r['S'] - 1) for r in rows if r['S'] > 1) - r_np       # sum over np places (e_P - 1)
    sumS = sum(r['count'] * r['S'] for r in rows)                                    # = deg_x Disc_y(g - c) = I(g_c, g_y)
    # three genus routes
    g_fRH = (sum_np + 2 - N - r_prop) / 2
    g_xRH = (sumS - n - r_tot + 2) / 2
    # adjunction via delta-invariants at the points at infinity (children of the root node)
    delta_total = F(0)
    root_level, pts = tree
    assert root_level == -1
    for pt in pts:
        Lp = list(leaves(pt))
        npt = sum(c for (_, c, _, _) in Lp); rpt = sum(F(c, e) for (_, c, e, _) in Lp)
        s = F(0)
        for (la, ca, ea, anca) in Lp:
            for (lb, cb, eb, ancb) in Lp:
                c = contact_of(anca, ancb, la, lb)
                mult = ca * (cb - 1) if la == lb else ca * cb
                s += mult * (1 + c)
        delta_total += s / 2 - F(npt - rpt, 2)
    g_adj = F((n - 1) * (n - 2), 2) - delta_total
    per_place = []
    for r in rows:
        eP = r['e'] * abs(r['S'] - 1)
        per_place.append(dict(leaf=str(r['leaf']), roots=r['count'], e=r['e'], S_g=str(r['S']),
                              places=str(F(r['count'], r['e'])), kind='proper' if r['S'] < 1 else 'non-proper',
                              e_P=str(eP), e_P_integer=(eP.denominator == 1)))
    out = dict(name=name, n=n, N=str(N), N_integer=(N.denominator == 1), r_prop=str(r_prop), r_np=str(r_np),
               sum_np_eP_minus_1=str(sum_np), sumS=str(sumS), sumS_integer=(sumS.denominator == 1),
               g_fRH=str(g_fRH), g_xRH=str(g_xRH), g_adjunction=str(g_adj),
               consistent=(g_fRH == g_xRH == g_adj and g_fRH.denominator == 1 and g_fRH >= 0),
               kaliman_ge_1=(g_fRH >= 1), places=per_place)
    if expected_N is not None:
        out['N_matches_expected'] = (N == expected_N)
    return out

def min_bins(items, cap):
    """exact minimum number of bins of capacity cap for the multiset items (small instance, DFS with pruning)."""
    items = sorted(items, reverse=True)
    best = [len(items)]
    lb = -(-sum(items) // cap)
    def rec(i, bins):
        if len(bins) >= best[0]: return
        if i == len(items):
            best[0] = len(bins); return
        it = items[i]
        seen = set()
        for j in range(len(bins)):
            if bins[j] + it <= cap and bins[j] not in seen:
                seen.add(bins[j]); bins[j] += it; rec(i + 1, bins); bins[j] -= it
                if best[0] == lb: return
        bins.append(it); rec(i + 1, bins); bins.pop()
    rec(0, [])
    return best[0], lb

# ---------------------------------------------------------------- trees (g_c-roots, generic c)
# (99,66): major point 72 g-roots: 3 conjugate D_2 discs at contact 1/3 (Moh (10) at j=2, a != 0), each 24 roots
# separating completely at 4/9 with all pi != 0 (Moh (12): 3 | 24, 3 | 16-1) -> e = 9 each.
MAJOR_9966 = (F(1, 3), [(F(4, 9), [('leaf', 24, 9)])] * 3)
# principal point 27 g-roots. Branch B: split at 2 into 18 + 9; ord g = 0 at 3 resp. 4 (Opus review Sec.4).
PRIN_B = (F(2), [(F(3), [('leaf', 18, 1)]), (F(4), [('leaf', 9, 1)])])
# delta = 5/2: split at 5/2 into 9 + 9 + 9 (p = pi(pi^2 - c)); pi = 0 packet e = 1; pi = +-sqrt(c) packets e = 2.
PRIN_52 = (F(5, 2), [(F(3), [('leaf', 9, 1)]), (F(3), [('leaf', 9, 2)]), (F(3), [('leaf', 9, 2)])])
TREE_B = (F(-1), [MAJOR_9966, PRIN_B])
TREE_52 = (F(-1), [MAJOR_9966, PRIN_52])
# (64,48): major 48 g-roots: 4 conjugate D_2 discs at 1/4 (Moh (10): TRI_2 = 3 = V_2), 12 roots each, separate at
# 9/16 with pi != 0 (Moh (12): 4 | 12, 4 | 9-1) -> e = 16.  Principal: u_s = 1, single packet, ord g = 16(delta-3)
# = 0 at delta = 3 (Moh Prop 6.1 order identity with V_r = u_s = 1), 16 roots separate at 3, e = 1.
TREE_6448 = (F(-1), [(F(1, 4), [(F(9, 16), [('leaf', 12, 16)])] * 4), (F(3), [('leaf', 16, 1)])])

# f_xi-trees (for IM = I(f_xi, g) and Im, Xu Thm 5.1 / Cor 5.3), same contacts:
FTREE_B = (F(-1), [(F(1, 3), [(F(4, 9), [('leaf', 16, 9)])] * 3), (F(2), [(F(3), [('leaf', 12, 1)]), (F(4), [('leaf', 6, 1)])])])
FTREE_52 = (F(-1), [(F(1, 3), [(F(4, 9), [('leaf', 16, 9)])] * 3), (F(5, 2), [(F(3), [('leaf', 6, 1)]), (F(3), [('leaf', 6, 2)]), (F(3), [('leaf', 6, 2)])])])
FTREE_6448 = (F(-1), [(F(1, 4), [(F(9, 16), [('leaf', 9, 16)])] * 4), (F(3), [('leaf', 12, 1)])])

def xu_IM_Im(ftree, m):
    """IM = sum_{major alpha}(1 - S_f(alpha)); Im = 1 + sum_{final minor pi-roots}(delta_sigma - 1), delta_sigma = S_f."""
    L = list(leaves(ftree)); IM = F(0); Im = F(1)
    for (la, ca, ea, anca) in L:
        S = F(0)
        for (lb, cb, eb, ancb) in L:
            c = contact_of(anca, ancb, la, lb); S -= (cb - 1 if la == lb else cb) * c
        if S < 1: IM += ca * (1 - S)
        else:
            assert S == anca[-1]          # final order = S_f (Xu p.6)
            Im += (S - 1)                 # one final minor pi-root per leaf packet
    assert sum(c for (_, c, _, _) in L) == m
    return IM, Im

# ---------------------------------------------------------------- numeric calibration of Lemma E
def numeric_calibration():
    import mpmath as mp
    mp.mp.dps = 60
    res = {}
    # (A) automorphism (f,g) = (x + y^2, y + (x + y^2)^2): J = 1.  deg_y g = 4, monic.  c = 1.
    def roots_g(X, c):
        # g - c = y^4 + 2X y^2 + y + X^2 - c
        return mp.polyroots([1, 0, 2 * X, 1, X**2 - c], maxsteps=200, extraprec=200)
    def exps(X1, X2, c, fy, gy, f):
        r1 = roots_g(X1, c); r2 = roots_g(X2, c)
        # match roots between X1 and X2 by continuity is unreliable; instead use one X and log-slopes from two X's
        # via sorted-by-argument matching (roots are a Galois orbit; slopes are common to the orbit).
        def profile(X, r):
            out = []
            for i, a in enumerate(r):
                cs = sorted([mp.log(abs(a - b)) / mp.log(X) for j, b in enumerate(r) if j != i], key=lambda v: float(v))
                out.append((cs, mp.log(abs(gy(X, a))) / mp.log(X), mp.log(abs(f(X, a))) / mp.log(X)))
            return out
        p1 = profile(X1, r1); p2 = profile(X2, r2)
        # exponent estimates: ord_t = -(log|.|)/log X; take the difference quotient between X1 and X2 for each root
        # (sorted contact lists are orbit-invariant, so pair by index)
        est = []
        for i in range(len(r1)):
            cs1, g1, f1 = p1[i]; cs2, g2, f2 = p2[i]
            L1, L2 = mp.log(X1), mp.log(X2)
            contacts = [-( (c2 * L2 - c1 * L1) / (L2 - L1) ) for c1, c2 in zip(cs1, cs2)]
            ordgy = -((g2 * L2 - g1 * L1) / (L2 - L1)); ordf = -((f2 * L2 - f1 * L1) / (L2 - L1))
            est.append((contacts, ordgy, ordf))
        return est
    X1, X2 = mp.mpf(10)**12, mp.mpf(10)**16
    est = exps(X1, X2, 1, None, lambda X, y: 1 + 4 * y * (X + y**2), lambda X, y: X + y**2)
    rowsA = []
    for (contacts, ordgy, ordf) in est:
        S = -sum(contacts)
        rowsA.append(dict(contacts=[round(float(c), 4) for c in contacts], S_g=round(float(S), 4),
                          ord_gy=round(float(ordgy), 4), ord_f=round(float(ordf), 4), S_minus_1=round(float(S - 1), 4)))
    res['automorphism'] = dict(pair='(x + y^2, y + (x + y^2)^2)', c=1, e=4, expected=dict(S_g='3/4', ord_gy='-3/4', ord_f='-1/4', e_P='4*(1/4)=1'), rows=rowsA)
    # (B) non-Keller control (f,g) = (y, y^3 + x y + 1), J = -y: general Lemma 4.1 gives
    # ord(f(alpha) - a0) = S_g(alpha) - 1 + ord J(alpha).
    def roots_gB(X, c): return mp.polyroots([1, 0, X, 1 - c], maxsteps=200, extraprec=200)
    rB = []
    for X in (mp.mpf(10)**12, mp.mpf(10)**16):
        r = roots_gB(X, 2)
        prof = []
        for i, a in enumerate(r):
            cs = sorted([mp.log(abs(a - b)) / mp.log(X) for j, b in enumerate(r) if j != i], key=lambda v: float(v))
            prof.append((cs, mp.log(abs(3 * a**2 + X)) / mp.log(X), mp.log(abs(a)) / mp.log(X)))
        rB.append((mp.log(X), prof))
    (L1, p1), (L2, p2) = rB
    rowsB = []
    # sort roots by |a| growth so index pairing is stable (two big roots, one small root)
    for i in range(3):
        cs1, g1, a1 = p1[i]; cs2, g2, a2 = p2[i]
        contacts = [-((c2 * L2 - c1 * L1) / (L2 - L1)) for c1, c2 in zip(cs1, cs2)]
        ordgy = -((g2 * L2 - g1 * L1) / (L2 - L1)); orda = -((a2 * L2 - a1 * L1) / (L2 - L1))
        S = -sum(contacts)
        rowsB.append(dict(contacts=[round(float(c), 4) for c in contacts], S_g=round(float(S), 4), ord_gy=round(float(ordgy), 4),
                          ord_f=round(float(orda), 4), ord_J=round(float(orda), 4), predicted_ord_f=round(float(S - 1 + orda), 4)))
    res['non_keller_control'] = dict(pair='(y, y^3 + x y + 1)', J='-y', c=2, rows=rowsB,
                                     note='predicted = S_g - 1 + ord J(alpha); Keller case has ord J = 0')
    return res

if __name__ == '__main__':
    out = {}
    out['branch_B'] = analyse('(99,66) branch B: delta=2 [2,1], finals (3,4)', 99, TREE_B, expected_N=16)
    out['delta_52'] = analyse('(99,66) delta=5/2 [1,1,1], finals (3,3,3)', 99, TREE_52, expected_N=16)
    out['moh_6448'] = analyse('(64,48) Moh row: u_s=1, principal final 3', 64, TREE_6448, expected_N=9)
    # dead control tree: (99,66) delta=2 [1,1,1] (killed by Xu Cor 7.5) -- the identity is still consistent (tree-blind)
    PRIN_C = (F(2), [(F(4), [('leaf', 9, 1)])] * 3)
    out['control_dead_[1,1,1]_at_2'] = analyse('(99,66) delta=2 [1,1,1] (DEAD control)', 99, (F(-1), [MAJOR_9966, PRIN_C]), expected_N=16)
    for key, ft, m in (('branch_B', FTREE_B, 66), ('delta_52', FTREE_52, 66), ('moh_6448', FTREE_6448, 48)):
        IM, Im = xu_IM_Im(ft, m); out[key]['xu_IM'] = str(IM); out[key]['xu_Im'] = str(Im)
    # escape-value bin packing: non-proper e_P's into fibres of size N
    for key in ('branch_B', 'delta_52', 'moh_6448'):
        d = out[key]; N = int(F(d['N']))
        items = []
        for p in d['places']:
            if p['kind'] == 'non-proper':
                items += [int(F(p['e_P']))] * int(F(p['places']))
        mb, lb = min_bins(items, N)
        d['escape_values_min'] = mb; d['escape_values_lb_ceil'] = lb; d['np_items'] = sorted(items, reverse=True)
    try:
        out['calibration'] = numeric_calibration()
    except Exception as ex:
        out['calibration'] = dict(error=repr(ex))
    json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else '/dev/stdout', 'w'), indent=1)
    for key in ('branch_B', 'delta_52', 'moh_6448', 'control_dead_[1,1,1]_at_2'):
        d = out[key]
        print('%-45s N=%s r_prop=%s r_np=%s sum_np(e_P-1)=%s sumS=%s g(fRH)=%s g(xRH)=%s g(adj)=%s consistent=%s g>=1=%s IM=%s Im=%s escape>=%s'
              % (d['name'], d['N'], d['r_prop'], d['r_np'], d['sum_np_eP_minus_1'], d['sumS'], d['g_fRH'], d['g_xRH'],
                 d['g_adjunction'], d['consistent'], d['kaliman_ge_1'], d.get('xu_IM'), d.get('xu_Im'), d.get('escape_values_min')))
        for p in d['places']:
            print('    %-12s roots=%3d e=%2d S_g=%-5s places=%-3s %-10s e_P=%s int=%s' % (p['leaf'], p['roots'], p['e'], p['S_g'], p['places'], p['kind'], p['e_P'], p['e_P_integer']))
    cal = out['calibration']
    if 'error' in cal: print('CALIBRATION ERROR', cal['error'])
    else:
        print('automorphism', cal['automorphism']['pair'], 'expected', cal['automorphism']['expected'])
        for r in cal['automorphism']['rows']: print('   ', r)
        print('non-Keller control', cal['non_keller_control']['pair'])
        for r in cal['non_keller_control']['rows']: print('   ', r)
