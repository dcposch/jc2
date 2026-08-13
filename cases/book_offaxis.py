#!/usr/bin/env python3
"""BOOK-OFFAXIS engine: off-axis (some b_i >= 2) entry census + mixed-merge
cells.  Additive over cases/book_enum.py (reuses entries/tdu_rows verbatim);
exact integer/Fraction arithmetic throughout.

Sector: BOOK-ENUM.md erratum — the book enumerated only the all-b=1 axis;
entries with b_i >= 2 carry M = b_i (MP4) down their chains (mu_e | M by
St 8.4) and can meet in mixed merges (all mu_e >= 2), never enumerated.

Step-1 census filters (all printed/promoted tier):
  - layer E reused: global type (al,be), td = sum Lambda_i, per-pole
    (a,b,nu) from tdu_rows(Lambda_i) (St 5.2 + Prop 5.6), MP4 pin M_i = b_i.
  - L6 primitivity (TEMPLATE-ATTACK 1a, on-page verified, cap-free):
    gcd(kbar_P, nu_P) = 1 with kbar_P = a(al+be).  At entries this is
    equivalent to N1 gcd(a, nu) = 1 (TDUNIFORM 2: al+be is coprime to nu
    by R2) — asserted below.

GATE: book_enum.gate() must PASS (on-axis td=6 record unchanged) before
any off-axis output is produced.

Stage R (2026-08-12, BOOK-OFFAXIS 6-9): R1 off-axis w-law (clean +
dirty transport, per-pole alphabet w_closure_off) and R2 general-mu
merge handshakes (cases I/II/III/IV of Prop 9.3) applied to every merge
cell; exact shape solve at pinned joins.  Recount: 2251/2691 DEAD,
440 alive, 0 open; td=7 CLOSED (asserted).
"""
from math import gcd
from fractions import Fraction as Fr
from itertools import product
import book_enum as BE

TDMAX = 14


def l6_pole_ok(al, be, a, nu):
    """L6 at a pole: gcd(a(al+be), nu) = 1.  Assert N1-equivalence."""
    ok = gcd(a * (al + be), nu) == 1
    assert ok == (gcd(a, nu) == 1), "L6/N1 equivalence broken (R2 violated?)"
    return ok


def census(tdmax=TDMAX):
    """Off-axis entry census: {(m, td): {'raw': n, 'l6': [entries...]}}.
    Each surviving entry: (al, be, poles) with poles = ((L,a,b,nu), ...)."""
    out = {}
    for td in range(6, tdmax + 1):
        for m in range(2, td // 3 + 1):
            raw, l6 = 0, []
            for al, be, poles in BE.entries(td, m):
                if not any(b >= 2 for (L, a, b, nu) in poles):
                    continue                       # on-axis: already booked
                raw += 1
                if all(l6_pole_ok(al, be, a, nu) for (L, a, b, nu) in poles):
                    l6.append((al, be, poles))
            out[(m, td)] = {'raw': raw, 'l6': l6}
    return out


def mp4_sanity(tdmax=TDMAX):
    """MP4 forcing is arithmetic: at prime Lambda or Lambda == beta all
    tdu_rows have b = 1 (checked for every Lambda <= tdmax - 3)."""
    for L in range(3, tdmax - 2):
        for (al, be), (D, Dg), (P, Pg), nu, _ in BE.tdu_rows(L):
            b = P // al
            if any(L % k == 0 for k in range(2, L)) is False:   # L prime
                assert b == 1, f"MP4 prime pin fails at Lambda={L}"
            if L == be:
                assert b == 1, f"MP4 beta-minimal pin fails at Lambda={L}"


def fmt_entry(al, be, poles):
    return (f"({al},{be})" + "+".join(
        f"L{L}a{a}b{b}n{nu}" for (L, a, b, nu) in poles))


# ---------------------------------------------------- step 3: merge cells
def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def hierarchies(leaves):
    """All rooted merge hierarchies on the given leaf tuple: nested tuples,
    internal nodes = frozensets of >= 2 children (MP1: sum(r-1) = m-1)."""
    leaves = list(leaves)
    if len(leaves) == 1:
        return [leaves[0]]
    # choose the root's r >= 2 child-subtrees = set partition into >= 2
    # blocks, each singleton block a leaf, each larger block a sub-merge
    out = []
    for blocks in BE.set_partitions(leaves):
        if len(blocks) < 2:
            continue
        subs = []
        for blk in blocks:
            if len(blk) == 1:
                subs.append([('leaf', blk[0])])
            else:
                subs.append([h for h in hierarchies(tuple(blk))
                             if h[0] == 'G'])
        combos = [()]
        for s in subs:
            combos = [c + (x,) for c in combos for x in s]
        for c in combos:
            out.append(('G', tuple(sorted(c, key=repr))))
    return out


def merge_cells(bs):
    """All (hierarchy, mu-assignment, emitted-M) cells for pole M-vector bs
    (indexed leaves).  Constraints used (printed tier only):
      St 8.4/8.5: leaf arrival mu | b_i (M non-increasing in divisibility);
      MP6(d)/subadditivity (valid incl. mixed, MP-REVIEW l.120): M_G | sum mu_e;
      inner-merge arrival mu_e | emitted M of the child merge;
      MP2: interior G* emits M >= 2 (root-merge G* = (0,y) cells kept, tagged).
    Returns list of dicts {tree, mus, Ms, classes, root_interior}."""
    leaves = tuple(range(len(bs)))
    cells = []

    def expand(node):
        """Yield (emitted_M, class_list, desc) for a subtree."""
        if node[0] == 'leaf':
            for mu in divisors(bs[node[1]]):
                yield mu, [], f"P{node[1]}mu{mu}"
            return
        _, children = node
        child_opts = [list(expand(ch)) for ch in children]
        combos = [()]
        for co in child_opts:
            combos = [c + (o,) for c in combos for o in co]
        for combo in combos:
            mus = [o[0] for o in combo]          # arriving mu_e at this merge
            klass = 'MIXED' if all(mu >= 2 for mu in mus) else 'MP6'
            inner = [k for o in combo for k in o[1]]
            desc = "(" + ",".join(o[2] for o in combo) + ")"
            for MG in divisors(sum(mus)):        # M_G | sum mu_e
                yield MG, inner + [klass], f"{desc}->M{MG}"

    for tree in set(hierarchies(leaves)):
        if tree[0] != 'G':
            continue
        for MG, classes, desc in expand(tree):
            for root_interior in (True, False):
                if root_interior and MG == 1:
                    continue                     # MP2: trunk M != 1
                cells.append({'desc': desc, 'classes': classes,
                              'M_out': MG, 'interior': root_interior})
    return cells


# ------------------- stage R (2026-08-12): R1/R2 filters, BOOK-OFFAXIS 6-9
NUCAP = 500      # nu_H loop cap; proven bounds are far smaller (doc 9)


def w_closure_off(w0, b):
    """R1.5 off-axis w-alphabet: closure of {w0} under clean resonant
    steps (R1.2: Delta | num, den | dq) and dirty steps (R1.4, l | b)."""
    W, frontier = {w0}, {w0}
    while frontier:
        nxt = set()
        for w in frontier:
            a, d = w.numerator, w.denominator
            for Delta in range(3, a + 1):           # clean resonance
                if a % Delta:
                    continue
                for nu in range(2, Delta):
                    if (Delta - 1) % nu:
                        continue
                    n = (Delta - 1) // nu + 1
                    if n < 2 or (n * nu + 1) % d:
                        continue
                    w2 = Fr(w * n, Delta)
                    if w2 not in W:
                        nxt.add(w2)
            for l in divisors(b):                   # dirty steps (R1.4)
                if l < 2:
                    continue
                cap = l * a * b                      # E <= l*num*M_G <= lab
                for nu in range(2, cap - l + 1):
                    # E = nu*c + l, c = l*k + l*lex - Sm in [k+l*lex, ...]
                    for c in range(1, (cap - l) // nu + 1):
                        for k in range(1, c + 1):
                            for lex in range(0, (c - k) // l + 1):
                                Sm = l * k + l * lex - c
                                if not (k <= Sm <= k * (l - 1)):
                                    continue
                                dq = (1 + k + lex) * nu + 1
                                dp = nu * (l + Sm)
                                E = l * dq - dp
                                assert E == nu * c + l
                                if -(-Sm // k) * dq >= dp:   # ceil(Sm/k)
                                    continue                 # NE law R2.2(S)
                                if b % gcd(dp, dq):          # M_G | b
                                    continue
                                kb = Fr(l * w * dq, E)
                                if kb.denominator != 1 or kb < 1:
                                    continue                 # kbar in Z
                                w2 = Fr(w * l * (dq - 1), nu * E)
                                if w2 not in W:
                                    nxt.add(w2)
        W |= nxt
        frontier = nxt
    return W


def cell_check(kbar, X, mus_non0, mu0, M_G):
    """R2.1(b)-consistency: does ANY pattern cell (nu_G, eps, NE, extras)
    realize X/kbar = dp/dq with the given arrivals?  R2.2 laws (S),(R),
    q-shape R1.0, gcd law.  Superset-true: returns False only on proof."""
    kbar, X = Fr(kbar), Fr(X)
    if kbar <= 0 or X <= 0:
        return False
    ratio = X / kbar
    d0, q0 = ratio.numerator, ratio.denominator
    dp, dq = M_G * d0, M_G * q0
    allmus = list(mus_non0) + ([mu0] if mu0 else [])
    if any(mu * dq <= dp for mu in allmus):          # searrow law (S)
        return False
    r0, smu = len(mus_non0), sum(mus_non0)
    if mu0:
        eps_opts = [mu0]
    elif dq < dp:
        eps_opts = [0] + list(range(1, (dp - 1) // dq + 1))
    else:
        eps_opts = [0]
    for eps in eps_opts:
        rest = dp - eps
        if rest < smu:
            continue
        nus = [1] + [n for n in range(2, dq) if (dq - 1) % n == 0]
        for nu in nus:
            if nu >= 2 and kbar.denominator != 1:
                continue                              # kbar in Z (V_{1,a})
            if rest % nu:
                continue
            Sm = rest // nu - smu
            if Sm < 0:
                continue
            Q = (dq - 1) // nu if nu >= 2 else dq
            if Sm == 0:
                if Q >= r0:
                    return True
                continue
            if dq >= dp:                              # NE needs dq < dp
                continue
            mm = (dp - 1) // dq                       # max NE mult
            if mm < 1:
                continue
            kmin = -(-Sm // mm)
            if Q >= r0 + kmin:
                return True
    return False


def nu_ok(nu, mu, nu_i):
    """R1.5 arrival law: nu_H = nu_i (depth 0) or nu >= 2, gcd(nu,mu)=1."""
    return nu == nu_i or (nu >= 2 and gcd(nu, mu) == 1)


def solve_arr(non0, zero, inner_mus, M_G, inner0_mu=None):
    """One arrangement at an interior merge.  non0 = [(mu, w)] pole edges
    not at the 0-direction; zero = (mu0, w0, nu_i) or None; inner0_mu =
    mult of an inner edge sitting at the 0-direction (its w unknown);
    returns 'DEAD' / 'ALIVE' / 'OPEN'.  R2.1 handshakes; kills are
    proofs (BOOK-OFFAXIS 6-9 for the loop bounds)."""
    cc_mu0 = inner0_mu if inner0_mu else (zero[0] if zero else 0)
    for (ma, wa) in non0:                    # equal-mu join (R2.1(i))
        for (mb, wb) in non0:
            if ma == mb and wa != wb:
                return 'DEAD'
    pin = None                               # R2.1(ii) distinct-mu pin
    for i in range(len(non0)):
        for j in range(i + 1, len(non0)):
            (ma, wa), (mb, wb) = non0[i], non0[j]
            if ma != mb:
                pin = Fr(ma * wa - mb * wb, ma - mb)
                break
        if pin is not None:
            break
    if pin is not None:
        kbar = pin
        X = non0[0][0] * (kbar - non0[0][1])
        for (mu, w) in non0:                 # all non-0 eqs must agree
            if mu * (kbar - w) != X:
                return 'DEAD'
        if kbar <= 0 or X <= 0:
            return 'DEAD'
        if any(kbar - Fr(X, mu) <= 0 for mu in inner_mus):
            return 'DEAD'                    # inner w_e > 0 (R2.1)
        if inner0_mu and kbar - Fr(X, inner0_mu) <= 0:
            return 'DEAD'                    # case III: nu_e*w_e > 0
        if zero is not None:
            mu0, w0, nu_i = zero
            nuH = (kbar - Fr(X, mu0)) / w0   # case III solved for nu_H
            if nuH.denominator != 1 or not nu_ok(int(nuH), mu0, nu_i):
                return 'DEAD'
        mus_all = [mu for (mu, w) in non0] + list(inner_mus)
        return ('ALIVE' if cell_check(kbar, X, mus_all, cc_mu0, M_G)
                else 'DEAD')
    # no pin: all non-0 pole edges share (mu, w) (or none exist)
    if zero is None:
        return 'ALIVE'                       # kbar free: open family
    mu0, w0, nu_i = zero
    if not non0:
        return 'ALIVE'
    mu, w = non0[0]
    if mu0 == mu:
        nuH = w / w0
        return ('ALIVE' if nuH.denominator == 1
                and nu_ok(int(nuH), mu0, nu_i) else 'DEAD')
    # kbar pinned per nu_H: loop the R1.5 menu (bounds: BOOK-OFFAXIS 9)
    if mu0 < mu:
        # kbar = (mu0*w0*nuH - mu*w)/(mu0-mu) > 0 iff nuH < mu*w/(mu0*w0):
        # provably finite menu -- the loop below is exhaustive.
        ncap = int(mu * w / (mu0 * w0)) + 1
    elif mu == 1:
        # doc 9 bound: dq-dp <= num(w)*M_G, nu_G <= mu0+num*M_G-1,
        # dp <= mu0+nu_G*smu, kbar <= w*dq, nuH = (kbar(mu0-1)+w)/(mu0*w0)
        smu = sum(m for (m, _) in non0) + sum(inner_mus)
        nGmax = mu0 + w.numerator * M_G - 1
        dqmax = mu0 + nGmax * smu + w.numerator * M_G
        ncap = int((Fr(w * dqmax) * (mu0 - mu) + mu * w)
                   / (mu0 * w0)) + 1
    else:
        ncap = NUCAP                          # honest cap: OPEN if dead
    alive = False
    for nuH in range(1, ncap + 1):
        if not nu_ok(nuH, mu0, nu_i):
            continue
        kbar = Fr(mu0 * nuH * w0 - mu * w, mu0 - mu)
        X = mu * (kbar - w)
        if kbar <= 0 or X <= 0:
            continue
        if any(kbar - Fr(X, mi) <= 0 for mi in inner_mus):
            continue
        if inner0_mu and kbar - Fr(X, inner0_mu) <= 0:
            continue
        mus_all = [m for (m, _) in non0] + list(inner_mus)
        if cell_check(kbar, X, mus_all, cc_mu0, M_G):
            alive = True
            break
    if alive:
        return 'ALIVE'
    return 'DEAD' if (mu0 < mu or mu == 1) else 'OPEN'


def expand2(node, bs):
    """expand() with tree structure retained: yields (emitted_M, struct),
    struct = ('leaf', i, mu) | ('G', children_structs, M_G)."""
    if node[0] == 'leaf':
        for mu in divisors(bs[node[1]]):
            yield mu, ('leaf', node[1], mu)
        return
    _, children = node
    opts = [list(expand2(ch, bs)) for ch in children]
    combos = [()]
    for co in opts:
        combos = [c + (o,) for c in combos for o in co]
    for combo in combos:
        mus = [o[0] for o in combo]
        for MG in divisors(sum(mus)):
            yield MG, ('G', tuple(o[1] for o in combo), MG)


def node_solve(chinfo, MG, pdata):
    leaves = [(mu, idx) for (k, mu, idx) in chinfo if k == 'leaf']
    inner_mus = [mu for (k, mu, idx) in chinfo if k == 'inner']
    best = 'DEAD'
    Ws = [pdata[idx]['W'] for (mu, idx) in leaves]
    slots = ([None] + [('L', j) for j in range(len(leaves))]
             + [('I', j) for j in range(len(inner_mus))])
    for wsel in (product(*Ws) if leaves else [()]):
        for zi in slots:
            zero, in0, imus = None, None, list(inner_mus)
            keep = range(len(leaves))
            if zi is not None and zi[0] == 'L':
                mu0, idx = leaves[zi[1]]
                zero = (mu0, wsel[zi[1]], pdata[idx]['nu'])
                keep = [j for j in keep if j != zi[1]]
            elif zi is not None:
                in0 = imus.pop(zi[1])
            non0 = [(leaves[j][0], wsel[j]) for j in keep]
            r = solve_arr(non0, zero, imus, MG, inner0_mu=in0)
            if r == 'ALIVE':
                return 'ALIVE'
            if r == 'OPEN':
                best = 'OPEN'
    return best


def cell_verdict(struct, interior, pdata):
    """Walk all merge nodes of one cell; DEAD > OPEN > ALIVE."""
    def walk(node, is_top):
        _, children, MG = node
        chinfo, verdicts = [], []
        for ch in children:
            if ch[0] == 'leaf':
                chinfo.append(('leaf', ch[2], ch[1]))
            else:
                chinfo.append(('inner', ch[2], None))
                verdicts.append(walk(ch, False))
        if is_top and not interior:          # root merge = (0,y): R2.1 IV
            v = 'ALIVE'
            for (k, mu, idx) in chinfo:
                if k == 'leaf' and all(w >= 1 for w in pdata[idx]['W']):
                    v = 'DEAD'
                    break
        else:
            v = node_solve(chinfo, MG, pdata)
        verdicts.append(v)
        if 'DEAD' in verdicts:
            return 'DEAD'
        return 'OPEN' if 'OPEN' in verdicts else 'ALIVE'
    return walk(struct, True)


def stage_r_census(cen):
    """R1/R2 recount: per (m, td) per entry, verdicts over ALL merge
    cells of the step-3 census (same enumeration, structure retained)."""
    out = {}
    for (m, td), d in sorted(cen.items()):
        rows = []
        for al, be, poles in d['l6']:
            bs = [b for (L, a, b, nu) in poles]
            pdata = [{'W': sorted(w_closure_off(
                BE.w0_of(al, be, a, b, nu), b)), 'nu': nu}
                for (L, a, b, nu) in poles]
            counts = {'DEAD': 0, 'ALIVE': 0, 'OPEN': 0}
            for tree in set(hierarchies(tuple(range(len(bs))))):
                if tree[0] != 'G':
                    continue
                for MG, struct in expand2(tree, bs):
                    for inter in (True, False):
                        if inter and MG == 1:
                            continue
                        counts[cell_verdict(struct, inter, pdata)] += 1
            rows.append({'entry': fmt_entry(al, be, poles), 'bs': bs,
                         'W': [p['W'] for p in pdata], 'counts': counts})
        out[(m, td)] = rows
    return out


def merge_census(cen):
    """Per (m,td): classify all merge cells of the L6-surviving entries."""
    out = {}
    for (m, td), d in sorted(cen.items()):
        rows = []
        for al, be, poles in d['l6']:
            bs = [b for (L, a, b, nu) in poles]
            cells = merge_cells(bs)
            nmix = sum(1 for c in cells if 'MIXED' in c['classes'])
            allmp6 = sum(1 for c in cells if 'MIXED' not in c['classes'])
            rows.append({'entry': fmt_entry(al, be, poles), 'bs': bs,
                         'cells': len(cells), 'mixed': nmix, 'mp6': allmp6})
        out[(m, td)] = rows
    return out


def report(cen):
    print("== OFF-AXIS ENTRY CENSUS (td<=%d): raw -> L6 survivors ==" % TDMAX)
    tot_raw = tot_l6 = 0
    for (m, td), d in sorted(cen.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        tot_raw += d['raw']; tot_l6 += len(d['l6'])
        star = ' PRIME-td' if td in (7, 11, 13) else ''
        print(f"m={m} td={td:2d}: raw={d['raw']:3d} l6={len(d['l6']):3d}{star}")
        for al, be, poles in d['l6']:
            ws = [BE.fstr(BE.w0_of(al, be, a, b, nu)) for (L, a, b, nu) in poles]
            Ms = [b for (L, a, b, nu) in poles]
            print(f"    {fmt_entry(al, be, poles)}  M={Ms} w0={ws}")
    print(f"TOTAL raw={tot_raw} l6-surviving={tot_l6}")
    pr = {td: sum(len(d['l6']) for (m, t), d in cen.items() if t == td)
          for td in (7, 11, 13)}
    print(f"PRIME-td L6 survivors: {pr}")
    return pr


# =====================================================================
# STAGE P — lambda-budget pricing (BOOK-OFFAXIS 10; the review's repair
# route).  Additive.  Sources: St 9.3 (24) via promoted AF2 (SHEET6-AF2
# 2, E6-corrected), St 9.4 (25)/(26) + H3-psi (SHEET6-H3 4a), St 8.4,
# MP2/MP5/MP8, R1.0-R1.2 + R2 (confirmed by BOOK-OFFAXIS-REVIEW).
# Replaces the REFUTED R1.3-R1.5 menu: G1 M-law removed, G2 eps-cells
# included, every non-clean step priced.  Kills only on budget proof.
# =====================================================================

def ceil_fr(x):
    x = Fr(x)
    return -((-x.numerator) // x.denominator)


def fdiv(n):
    out, d = [], 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d != n // d:
                out.append(n // d)
        d += 1
    return sorted(out)


def _min_ne_lam(X, kb, k, Sm, mm):
    """min over NE-mult partitions of sum ceil(gap_j); gap>0 (NE) or None."""
    if k == 0:
        return 0
    best = [None]
    def rec(j, left, acc):
        if j == k:
            if left == 0 and (best[0] is None or acc < best[0]):
                best[0] = acc
            return
        rem = k - j - 1
        for m in range(1, mm + 1):
            if left - m < rem or left - m > rem * mm:
                continue
            g = Fr(X, m) - kb
            if g <= 0:
                return
            rec(j + 1, left - m, acc + max(1, ceil_fr(g)))
    rec(0, Sm, 0)
    return best[0]


_PSTEPS = {}
def chain_steps_p(w, M):
    """P0 priced one-step menu from chain state (w, M).  Complete at
    printed tier + R1.0 (doc 10 P0): clean/neutral lam=0; pure-(b)
    (C=0, nu-free, w -> lw/(l-eps), lam >= ceil(lw/eps)); dirty (a) and
    (b)-with-extras via the finite Diophantine E | l*num(w)*T."""
    if (w, M) in _PSTEPS:
        return _PSTEPS[(w, M)]
    out = []
    a = w.numerator
    for Delta in fdiv(a):                            # clean resonant
        if Delta < 3:
            continue
        for nu in range(2, Delta):
            if (Delta - 1) % nu:
                continue
            n = (Delta - 1) // nu + 1
            if n < 2:
                continue
            dq = n * nu + 1
            if dq % w.denominator:
                continue
            for l in fdiv(M):
                out.append((Fr(w * n, Delta), gcd(l, dq), 0, nu))
    for M2 in fdiv(M):                               # neutral / M-drop
        out.append((w, M2, 0, None))
    for l in fdiv(M):
        if l < 2:
            continue
        for eps in range(1, l):                      # pure (b)
            E = l - eps
            out.append((Fr(l * w, E), None, ceil_fr(Fr(l * w, eps)), E))
            # M' ranges over divisors of E: expanded by caller (None tag)
        for eps in range(0, l):                      # (a) / (b)+extras
            for k in range(0, 7):
                if eps == 0 and k == 0:
                    continue                         # clean shape covered
                for Sm in range(k, k * (l - 1) + 1):
                    for lex in range(0, 41):
                        C = l * (k + lex) - Sm
                        if C <= 0:
                            continue
                        T = Sm + l - eps * (1 + k + lex)
                        if T <= 0:
                            continue                 # dp <= eps*dq: (R)
                        if 2 * C > l * a * T:
                            break
                        for E in fdiv(l * a * T):
                            nuq, rem = divmod(E - (l - eps), C)
                            if rem or nuq < 2:
                                continue
                            nu = nuq
                            dq = (1 + k + lex) * nu + 1
                            dp = eps + nu * (l + Sm)
                            kb = Fr(l * w * dq, E)
                            if kb.denominator != 1 or kb < 1:
                                continue
                            if eps and eps * dq >= dp:
                                continue
                            X = kb * Fr(dp, dq)
                            mm = min(l - 1, (dp - 1) // dq) if k else 0
                            if k and (mm < 1 or Sm > k * mm):
                                continue
                            lam = _min_ne_lam(X, kb, k, Sm, mm)
                            if lam is None:
                                continue
                            if eps:
                                lam += max(1, ceil_fr((Fr(X, eps) - kb)
                                                      / nu))
                            out.append((Fr(l * w * (dq - 1), nu * E),
                                        gcd(dp, dq), lam, nu))
    _PSTEPS[(w, M)] = out
    return out


PCAP_BUDGET = 5      # closure budget cap (exact for td = 7: budget 5)
PCAP_STATES = 4000   # state cap: hit => capped (no DEAD verdicts allowed)


def close_p(w0, M0, budget, forbid_M1=False):
    """Dijkstra closure of priced states; returns ({(w,M): lam_min},
    vertex-realizations {(w,M): {(nu, M)}}, capped-flag).  capped=True
    means the closure was truncated (budget or state cap): downstream
    verdicts may only be ALIVE/OPEN, never DEAD."""
    import heapq
    capped = budget > PCAP_BUDGET
    budget = min(budget, PCAP_BUDGET)
    dist, cells = {}, {}
    pq = [(0, w0, M0)]
    while pq:
        lam, w, M = heapq.heappop(pq)
        if (w, M) in dist and dist[(w, M)] <= lam:
            continue
        if len(dist) >= PCAP_STATES:
            capped = True
            break
        dist[(w, M)] = lam
        if w.numerator > 10 ** 4 or M > 200:
            capped = True                # numerator/M cap: no expansion
            continue
        for st in chain_steps_p(w, M):
            w2, M2, dl, nu = st
            l2 = lam + dl
            if l2 > budget:
                continue
            M2s = fdiv(st[3]) if M2 is None else [M2]   # pure-b: M' | E
            for M2x in M2s:
                if forbid_M1 and M2x == 1:
                    continue
                if nu is not None and M2 is not None:
                    cells.setdefault((w2, M2x), set()).add((nu, M2x))
                if (w2, M2x) not in dist or dist[(w2, M2x)] > l2:
                    heapq.heappush(pq, (l2, w2, M2x))
    return dist, cells, capped


def terminal_psi(w, M):
    """P1: case-IV terminal legality + certified psi (H3-psi,
    R = 1/(1-w)); returns psi or None."""
    if w >= 1 or w <= 0 or M < 2:
        return None
    j = M * (1 - w)
    if j.denominator != 1 or j < 1:
        return None                                  # 9.3(m)
    return ceil_fr(Fr(M, int(j))) - 1


_POLES = {}
def priced_pole(w0, b, budget):
    """corrected per-pole priced alphabet (l | M closure; G1 removed,
    G2 included).  W' = state w's, MU' = all mu | some state M."""
    key = (w0, b, min(budget, PCAP_BUDGET))
    if key not in _POLES:
        dist, cells, capped = close_p(w0, b, budget)
        W = sorted({w for (w, M) in dist})
        MU = sorted({mu for (w, M) in dist for mu in fdiv(M)})
        _POLES[key] = (dist, cells, W, MU, capped)
    dist, cells, W, MU, capped = _POLES[key]
    return dist, cells, W, MU, capped or budget > PCAP_BUDGET


def stage_rp_census(cen):
    """Stage R' : the honest grid recount under the CORRECTED alphabets.
    Finding (doc 10 P5): with the refuted M-law removed and the printed
    eps-cells included, the per-pole alphabet is bounded ONLY by the
    St 9.4 budget (R1.5's finiteness is gone) and contains post-jump
    states of unbounded numerator/M; the stage-R grid solve (whose loop
    bounds scale with num(w)*M) is therefore NOT certifiably complete
    for ANY b >= 2 entry.  Sound consequence: no grid cell may be
    declared DEAD at this level -- every off-axis cell is OPEN at grid
    tier, and per-panel decisions must come from per-route pricing
    (adjudicate_td7 for td = 7).  This function reports that recount."""
    out = {}
    for (m, td), d in sorted(cen.items()):
        rows = []
        for al, be, poles in d['l6']:
            bs = [b for (L, a, b, nu) in poles]
            n = 0
            for tree in set(hierarchies(tuple(range(len(bs))))):
                if tree[0] != 'G':
                    continue
                for MG, struct in expand2(tree, bs):
                    for inter in (True, False):
                        if not (inter and MG == 1):
                            n += 1
            rows.append({'entry': fmt_entry(al, be, poles), 'bs': bs,
                         'counts': {'DEAD': 0, 'ALIVE': 0, 'OPEN': n},
                         'capped': True})
        out[(m, td)] = rows
    return out


def expand2_p(node, bs, mus):
    """expand2 with post-jump leaf mu menus (mu | M of ANY priced state,
    independent-pairing superset)."""
    if node[0] == 'leaf':
        for mu in mus[node[1]]:
            yield mu, ('leaf', node[1], mu)
        return
    _, children = node
    opts = [list(expand2_p(ch, bs, mus)) for ch in children]
    combos = [()]
    for co in opts:
        combos = [c + (o,) for c in combos for o in co]
    for combo in combos:
        ms = [o[0] for o in combo]
        for MG in divisors(sum(ms)):
            yield MG, ('G', tuple(o[1] for o in combo), MG)


def w_closure_review_patch(w0, b):
    """GATE ONLY: w_closure_off with the refuted M-law removed -- must
    reproduce the review's W_off(3/2,2) and the 4 DEAD / 2 ALIVE td-7
    pre-pricing state (BOOK-OFFAXIS-REVIEW 3a)."""
    W, frontier = {w0}, {w0}
    while frontier:
        nxt = set()
        for w in frontier:
            a, d = w.numerator, w.denominator
            for Delta in range(3, a + 1):
                if a % Delta:
                    continue
                for nu in range(2, Delta):
                    if (Delta - 1) % nu:
                        continue
                    n = (Delta - 1) // nu + 1
                    if n < 2 or (n * nu + 1) % d:
                        continue
                    w2 = Fr(w * n, Delta)
                    if w2 not in W:
                        nxt.add(w2)
            for l in divisors(b):
                if l < 2:
                    continue
                cap = l * a * b
                for nu in range(2, cap - l + 1):
                    for c in range(1, (cap - l) // nu + 1):
                        for k in range(1, c + 1):
                            for lex in range(0, (c - k) // l + 1):
                                Sm = l * k + l * lex - c
                                if not (k <= Sm <= k * (l - 1)):
                                    continue
                                dq = (1 + k + lex) * nu + 1
                                dp = nu * (l + Sm)
                                E = l * dq - dp
                                if -(-Sm // k) * dq >= dp:
                                    continue
                                kb = Fr(l * w * dq, E)
                                if kb.denominator != 1 or kb < 1:
                                    continue
                                w2 = Fr(w * l * (dq - 1), nu * E)
                                if w2 not in W:
                                    nxt.add(w2)
        W |= nxt
        frontier = nxt
    return W


def gate_review_42(cen):
    """Pre-pricing gate: the review's patched engine state at td = 7."""
    d = cen[(2, 7)]
    al, be, poles = d['l6'][0]
    bs = [b for (L, a, b, nu) in poles]
    pdata = [{'W': sorted(w_closure_review_patch(
        BE.w0_of(al, be, a, b, nu), b)), 'nu': nu}
        for (L, a, b, nu) in poles]
    assert pdata[1]['W'] == sorted([Fr(3, 16), Fr(3, 8), Fr(4, 9),
                                    Fr(2, 3), Fr(3, 4), Fr(3, 2)]), \
        "review W_off(3/2,2) not reproduced"
    counts = {'DEAD': 0, 'ALIVE': 0, 'OPEN': 0}
    for tree in set(hierarchies(tuple(range(len(bs))))):
        if tree[0] != 'G':
            continue
        for MG, struct in expand2(tree, bs):
            for inter in (True, False):
                if inter and MG == 1:
                    continue
                counts[cell_verdict(struct, inter, pdata)] += 1
    assert counts == {'DEAD': 4, 'ALIVE': 2, 'OPEN': 0}, counts
    return counts


# ---- td = 7 exact priced adjudication (doc 10 P3/P4) ----------------

_TRK = {}
TRUNK_CAP_HITS = []


def _trunk_routes(w0, M0, bleft):
    if M0 < 2 or bleft < 0:
        return []
    key = (w0, M0, bleft)
    if key not in _TRK:
        dist, _, capped = close_p(w0, M0, bleft, forbid_M1=True)
        if capped:
            TRUNK_CAP_HITS.append((w0, M0, bleft))
        out = []
        for (w, M), lam in dist.items():
            p = terminal_psi(w, M)
            if p is not None:
                out.append((lam, p, w, M))
        _TRK[key] = sorted(out)
    return _TRK[key]


def _feasible(lam_pre, w_tr, M_G, ctx, out):
    for (lt, psi, wt, Mt) in _trunk_routes(w_tr, M_G, max(0, 5 - lam_pre)):
        if lam_pre + lt <= 6 - psi:
            out.append((lam_pre + lt, 6 - psi, ctx,
                        (w_tr, M_G, lt, wt, Mt, psi)))


def _cls_C_cells(kbar, mu0):
    """P3 class C: X = kbar-2, eps = mu0, one mu=1 edge, Sm = 0 forced,
    nu_G >= 2; complete via nu_G | (mu0 + c - 1)."""
    X = kbar - 2
    cells = []
    if X <= 0:
        return cells
    cmax = 40 * mu0 if kbar <= 4 else (4 * mu0 - 2) // (kbar - 4)
    for c in range(1, cmax + 1):
        num = c * (kbar - 2)
        if num % 2:
            continue
        dp = num // 2
        nu = dp - mu0
        if nu < 2 or (mu0 + c - 1) % nu:
            continue
        dq = dp + c
        if (dq - 1) % nu:
            continue
        M = gcd(dp, dq)
        if M >= 2:
            cells.append((dp, dq, nu, M,
                          (Fr(kbar) - Fr(X, dp)) / nu))
    return cells


def adjudicate_td7():
    """Exhaustive priced adjudication of the single td-7 off-axis entry
    (P3 classes; complete at printed tier + R1.0 + promoted budget).
    Returns list of budget-fitting routes."""
    dist, cells, capped = close_p(Fr(3, 2), 2, 5)
    assert not capped
    surv = []
    lamA = dist.get((Fr(2), 1))
    if lamA is not None:                     # class A: only (6,10) nu>=2;
        _feasible(lamA, Fr(3, 2), 2, 'A(6,10)', surv)
        _tail_first_steps(lamA, surv)        # (2,2t) nu_G=1 tail
    lamB = min((lam for (w, M), lam in dist.items()
                if (Fr(2) / w).denominator == 1 and Fr(2) / w >= 2),
               default=None)
    if lamB is not None:                     # class B: only (3,9)
        _feasible(lamB, Fr(4, 3), 3, 'B(3,9)', surv)
        _tail_first_steps(lamB, surv)
    for (w2, M2), lam2 in sorted(dist.items(), key=lambda kv: kv[1]):
        for mu0 in fdiv(M2):                 # class C
            if mu0 < 2:
                continue
            numax = int(((4 * mu0 + 2) * (mu0 - 1) + 2) / (mu0 * w2)) + 2
            for nu2 in range(2, numax + 1):
                ok = (nu2 + 1) % mu0 == 0
                ok = ok or any(nuc == nu2 and Mc % mu0 == 0
                               for (nuc, Mc) in cells.get((w2, M2), ()))
                ok = ok or (nu2 == 3 and (w2, M2) == (Fr(3, 2), 2)
                            and mu0 <= 2)
                if not ok:
                    continue
                kb = Fr(mu0 * nu2 * w2 - 2, mu0 - 1)
                if kb.denominator != 1 or kb < 3:
                    continue
                for (dp, dq, nuG, MG, w_tr) in _cls_C_cells(int(kb), mu0):
                    _feasible(lam2, w_tr, MG,
                              f'C mu0={mu0} w2={w2} nu2={nu2} '
                              f'({dp},{dq})nu{nuG}M{MG}', surv)
    return surv


def stage_p_report():
    surv = adjudicate_td7()
    cellsB = {t[4 - 4] for (tot, bud, ctx, t) in surv
              if ctx.startswith('B')}
    ccells = {ctx.split(' ')[-1].split('nu')[0]
              for (tot, bud, ctx, t) in surv if ctx.startswith('C')}
    nA = sum(1 for r in surv if r[2].startswith(('A', 'tail')))
    exact = sum(1 for (tot, bud, ctx, t) in surv if tot == bud)
    best = min(surv)[0] if surv else None
    print(f"td-7 priced adjudication: {len(surv)} budget-fitting routes; "
          f"A/tail routes: {nA}; B-cell routes: "
          f"{sum(1 for r in surv if r[2].startswith('B'))}; distinct "
          f"C-cells: {len(ccells)}; exact-fit: {exact}; min lambda: {best}")
    if nA == 0:
        print("  G2/eps reopening (review star cell): PRICED OUT "
              "(0 class-A/tail routes)")
    print("  VERDICT td=7: " + ("NOT closed by the lambda budget; "
          "survivors are pinned T1-rigidity targets (doc 10 P4)"
          if surv else "CLOSED (every route overruns St 9.4)"))
    if TRUNK_CAP_HITS:
        print(f"  RIDER: {len(TRUNK_CAP_HITS)} trunk closures hit caps "
              f"(survivor list = within-cap superset)")
    return surv


def _tail_first_steps(lam_pre, out):
    """(2,2t) nu_G=1 family, seeds w_u = 2 + 1/u, M = 2: complete
    first-step inversion (u | 2dq; clean: u | dq, Delta | 2u+1)."""
    for k in range(0, 4):                    # dirty/eps l=2 (Sm = k)
        for eps in (0, 1):
            if k == 0:
                continue                     # pure-b costs >= 5: overruns
            for lex in range(0, 7):
                for nu in range(2, 401):
                    dq = (1 + k + lex) * nu + 1
                    dp = eps + nu * (2 + k)
                    E = 2 * dq - dp
                    if E <= 0 or dq >= dp or (eps and eps * dq >= dp):
                        continue
                    for u in fdiv(2 * dq):
                        kb = Fr(2 * (2 * u + 1) * dq, u * E)
                        if kb.denominator != 1 or kb < 1:
                            continue
                        X = kb * Fr(dp, dq)
                        lam = _min_ne_lam(X, kb, k, k, 1)
                        if lam is None:
                            continue
                        if eps:
                            lam += max(1, ceil_fr((Fr(X, eps) - kb) / nu))
                        M2 = gcd(dp, dq)
                        if M2 < 2 or lam_pre + lam > 5:
                            continue
                        w2 = Fr(2 * (2 * u + 1) * (dq - 1), u * nu * E)
                        _feasible(lam_pre + lam, w2, M2,
                                  f'tail u={u}', out)
    for nu in range(3, 301, 2):              # clean l=2 (dq even)
        for n in range(3, 301, 2):
            dq = n * nu + 1
            D = (n - 1) * nu + 1
            for u in fdiv(dq):
                if (2 * u + 1) % D:
                    continue
                w_u = Fr(2 * u + 1, u)
                w2 = w_u * n / D
                if w2 < w_u:
                    _feasible(lam_pre, w2, 2, f'tail-clean u={u}', out)


if __name__ == '__main__':
    okc, _ = BE.gate()
    assert okc, "ON-AXIS GATE FAIL: aborting off-axis census"
    mp4_sanity()
    print("MP4 sanity (prime/beta-minimal Lambda force b=1): PASS")
    cen = census()
    report(cen)
    print("\n== MERGE-CELL CENSUS (hierarchies x mu x M, printed-tier) ==")
    mc = merge_census(cen)
    tot_mix = tot_mp6 = 0
    for (m, td), rows in sorted(mc.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        for r in rows:
            tot_mix += r['mixed']; tot_mp6 += r['mp6']
            star = ' PRIME-td' if td in (7, 11, 13) else ''
            print(f"m={m} td={td:2d} {r['entry']}: cells={r['cells']} "
                  f"mixed={r['mixed']} mp6-anatomy={r['mp6']}{star}")
    print(f"TOTAL cells: mixed={tot_mix} mp6-anatomy={tot_mp6}")

    print("\n== STAGE R RECOUNT (R1 w-law + R2 handshakes, BOOK-OFFAXIS "
          "6-8) ==")
    rc = stage_r_census(cen)
    tD = tA = tO = 0
    per_td = {}
    for (m, td), rows in sorted(rc.items(), key=lambda kv: (kv[0][1],
                                                            kv[0][0])):
        for r in rows:
            c = r['counts']
            tD += c['DEAD']; tA += c['ALIVE']; tO += c['OPEN']
            p = per_td.setdefault(td, [0, 0, 0])
            p[0] += c['DEAD']; p[1] += c['ALIVE']; p[2] += c['OPEN']
            star = ' PRIME-td' if td in (7, 11, 13) else ''
            ws = ";".join("{" + ",".join(BE.fstr(w) for w in W) + "}"
                          for W in r['W'])
            print(f"m={m} td={td:2d} {r['entry']} W={ws}: "
                  f"dead={c['DEAD']} alive={c['ALIVE']} "
                  f"open={c['OPEN']}{star}")
    print(f"TOTAL: dead={tD} alive={tA} open={tO} of {tD + tA + tO} "
          f"cells (prior tier killed none beyond MP2/L6)")
    for td in sorted(per_td):
        D, A, O = per_td[td]
        stat = 'CLOSED' if A + O == 0 else f'open({A}+{O})'
        print(f"  td={td:2d}: {stat}" +
              (' PRIME-td' if td in (7, 11, 13) else ''))
    assert per_td.get(7, [0, 0, 0])[1:] == [0, 0], \
        "td=7 kill (BOOK-OFFAXIS 8) not reproduced!"
    print("GATE td=7: all off-axis cells DEAD -- doc 8 kill reproduced")
    print("  [SUPERSEDED by review + stage P below: the stage-R alphabet",
          "embeds the refuted M-law and omits the eps-cells]")

    print("\n== STAGE P (lambda-budget pricing, BOOK-OFFAXIS 10) ==")
    g42 = gate_review_42(cen)
    print(f"GATE review-3a: patched pre-pricing td-7 state reproduced: {g42}")

    print("\n== STAGE R' RECOUNT (corrected priced alphabets; capped "
          "closures => OPEN) ==")
    rp = stage_rp_census(cen)
    tD = tA = tO = 0
    per_td = {}
    for (m, td), rows in sorted(rp.items(), key=lambda kv: (kv[0][1],
                                                            kv[0][0])):
        for r in rows:
            c = r['counts']
            tD += c['DEAD']; tA += c['ALIVE']; tO += c['OPEN']
            p = per_td.setdefault(td, [0, 0, 0])
            p[0] += c['DEAD']; p[1] += c['ALIVE']; p[2] += c['OPEN']
            cap = ' CAPPED' if r['capped'] else ''
            print(f"m={m} td={td:2d} {r['entry']}: dead={c['DEAD']} "
                  f"alive={c['ALIVE']} open={c['OPEN']}{cap}")
    print(f"STAGE R' TOTAL: dead={tD} alive={tA} open={tO} of "
          f"{tD + tA + tO} cells (superset semantics; alive != existent)")
    for td in sorted(per_td):
        D, A, O = per_td[td]
        print(f"  td={td:2d}: dead={D} alive={A} open={O}" +
              (' PRIME-td' if td in (7, 11, 13) else ''))

    stage_p_report()
