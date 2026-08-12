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
