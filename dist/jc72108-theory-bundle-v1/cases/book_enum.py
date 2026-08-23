#!/usr/bin/env python3
"""BOOK(m, td) enumeration -- the reviewed final book spec, run mechanically.

Spec authority: SHEET6-DEPTH-REVIEW.md sec 6 (closing BOOK(m,td) spec), with
SHEET6-MULTIPOLE.md MP4/MP6/MP7/MP8, SHEET6-DEPTH.md (w-arithmetic, DS1-DS4,
d0 <= 2*gen+2 as promoted), SHEET6-TDUNIFORM.md tdu_rows (promoted entry table).

Spec-to-code map
  E  entry layer   -> entries(td, m): global type (alpha,beta), 2<=alpha<beta,
                      gcd=1, m*beta <= td; partitions td = Sigma Lambda_i,
                      Lambda_i >= beta; per pole REUSE sheet6_campaign.tdu_rows
                      (Lambda_i) filtered to the type -- rows carry (a_i,b_i,nu_i)
                      with the q-shape pin (okA: nu|alpha & nu|b*beta-1; okB
                      symmetric) already inline; MP4 pin M_i = b_i applied inline
                      (b_i = 1 forced at Lambda_i = beta / prime is automatic in
                      the row arithmetic).  Entries with any b_i >= 2 are OFF the
                      all-M=1 axis (MP7 hypothesis fails; M>=2 chains are outside
                      the closed lemma): counted + banked, not cell-expanded.
  T  tree layer    -> set partitions, recursively: the final merge takes r >= 2
                      branches; multi-pole branches are headed by M=1-emitting
                      cascade merges.  Sigma(r-1) = m-1 holds automatically for
                      every hierarchy on m leaves (MP1), so the merge budget --
                      cascades only above G*, jump/root cell = G* -- is exact.
  C' chain layer   -> w0_of: w0 = a(b(alpha+beta)-1)/(b*nu); w_closure: resonant
                      steps w -> w*n/Delta, Delta=(n-1)nu+1 >= 3, Delta | num(w)
                      (verbatim from cases/depth_closure_check.py, promoted);
                      cascade transitions merge_cascade_ws: M=1-emitting cells,
                      IIa child w*(r+l)/(l*nu+1) (= r*w at l=0), exact ZCH/I
                      analogues w*(r-1+l)/(l*nu) and w*(r+l-1)/l from DS4;
                      depth cap d0 <= 2*gen(W)+2 recorded per entry (the
                      promoted DEPTH-REVIEW constant; content is depth-free).
  J' jump layer    -> window_cells(w, r): kap_m in (w, (r+1)w] cap Z (St 9.1 +
                      corrected St 3.8 integrality); Di := kap_m - w; nu
                      DETERMINED per (kap_m, l): IIa nu(wr - Di*l) = Di,
                      ZCH nu(l*Di - w(r-1)) = w, I l = wr/Di (nu = 1); child
                      datum (kap, D/i, rho) = w*(dq_c, dp_c, 1)/Delta_c.
                      Inline mechanical kills:
                        mp7_l0_M1        l=0 IIa emits M=1 -> at G* MP2-dead
                        mp7_l0_impossible l=0 ZCH / nu=1 (Prop 8.1(iv))
                        M1_mp2           l>=1 gcd menu M=1 at G* (MP2)
                        mp9_nu1_even_l   family I, r=2: even-l exact
                                         log-obstruction (promoted, all l)
                        zch_w_ratio      ZCH 0-edge is case (III): join needs
                                         arriving w's in integer ratio nu_e>=2
                      Survivors keep M = gcd menu >= 2, gcd(M,nu)=1 and M | r
                      (outside ZCH) asserted.
  R  root layer    -> case (IV): w_e = 1 - l_f/i0 < 1 NECESSARY (engine filter;
                      (j) kap<nu is the per-edge form).  Kills: root_w_window
                      (W cap (0,1) empty), root_even_l (log-obstruction),
                      root_st94 (l > td - r from Sigma-lambda >= 0 in St 9.4
                      (25) with psi = r+l-1; printed l <= td-2 is the r=2 form).
                      Survivor data: M = gcd(r,l), k_f = (r+l)l_f, psi = r+l-1,
                      l_f/i0 = 1 - w.
  S  suffix layer  -> NOT enumerated here (per-cell bash next): MP2 restored
                      kill + single-pole engine + St 9.4 budget.  MP8
                      transparency encoded: lambda_spent = 0 through every M=1
                      chain and all-mu=1 merge; each survivor carries
                      suffix_budget = td - 2 (the campaign budget).

GATE (mandatory): td=6, m=2 reproduces the promoted record EXACTLY -- the
unique IIa (r,nu,l) = (2,3,1), M = 2, kap_m = 5, child (5, 3, 1/2) at w = 2
(residue-A configuration, a1/a2 = 2+-sqrt(3)), R empty (w = 2 >= 1).

Output: systems/book/book_m{m}_td{td}.json + summary.json; human table on
stdout.  Exact arithmetic (int/Fraction) throughout.
"""
import json
import os
import sys
from fractions import Fraction as Fr
from itertools import combinations_with_replacement
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sheet6_campaign import tdu_rows          # promoted entry table (TDU gate)

OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      '..', 'systems', 'book')

def fstr(x):
    return str(x) if isinstance(x, (int, str)) else \
        (str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}")

# ------------------------------------------------------------ E. entries
def pole_options(Lam, al, be):
    """(a, b, nu) rows of the promoted leaf table at Lambda = Lam, type (al,be).
    MP4 pin M_i = b_i; q-shape pin lives in tdu_rows' okA/okB."""
    out = []
    for (a2, b2), (D, Dg), (P, Pg), nu, L in tdu_rows(Lam):
        if (a2, b2) == (al, be):
            out.append((D // al, P // al, nu))
    return out

def partitions(n, m, lo):
    """Ascending partitions of n into m parts, each >= lo."""
    if m == 1:
        return [(n,)] if n >= lo else []
    out = []
    for first in range(lo, n // m + 1):
        for rest in partitions(n - first, m - 1, first):
            out.append((first,) + rest)
    return out

def entries(td, m):
    """All entry multisets: (al, be, poles) with poles a sorted tuple of
    (Lambda_i, a_i, b_i, nu_i).  Multiset semantics for equal Lambda parts."""
    out = []
    for be in range(3, td // m + 1):
        for al in range(2, be):
            if gcd(al, be) != 1:
                continue
            for part in partitions(td, m, be):
                opts = {L: pole_options(L, al, be) for L in set(part)}
                if any(not opts[L] for L in set(part)):
                    continue
                groups = [list(combinations_with_replacement(
                    [(L,) + o for o in opts[L]], part.count(L)))
                    for L in sorted(set(part))]
                combos = [()]
                for g in groups:
                    combos = [c + gc for c in combos for gc in g]
                for poles in combos:
                    out.append((al, be, tuple(sorted(poles))))
    return out

# ------------------------------------------------------ C'. w-arithmetic
def w0_of(al, be, a, b, nu):
    """Entry invariant w0 = a(b(alpha+beta)-1)/(b nu)  (DEPTH sec 4)."""
    return Fr(a * (b * (al + be) - 1), b * nu)

def w_closure(w0):
    """Resonant closure (verbatim from cases/depth_closure_check.py, promoted):
    w -> w*npat/Delta, Delta | num(w), Delta = (npat-1)*nu+1 >= 3, npat,nu >= 2."""
    W, frontier, gen = {w0}, {w0}, 0
    while frontier:
        nxt = set()
        for w in frontier:
            a = w.numerator
            for Delta in range(3, a + 1):
                if a % Delta:
                    continue
                for nu in range(2, Delta):
                    if (Delta - 1) % nu:
                        continue
                    wn = w * Fr((Delta - 1) // nu + 1, Delta)
                    if wn not in W:
                        nxt.add(wn)
        W |= nxt
        frontier = nxt
        gen += 1 if nxt else 0
    return W, gen

# ------------------------------------------------------- J'. window cells
def window_cells(w, r):
    """All solvable l>=1 cells at (w, r): (fam, nu, l, M, kap_m, Di).
    kap_m in (w, (r+1)w] cap Z; nu determined per (kap_m, l) [DS4/5b]."""
    cells = []
    km = int(w) + 1
    while km <= (r + 1) * w:
        Di = km - w
        l = 1                                       # IIa: nu(wr - Di l) = Di
        while Di * l < w * r:
            nu = Di / (w * r - Di * l)
            if nu.denominator == 1 and nu >= 2:
                v = int(nu)
                M = gcd(r * v, (r + l) * v + 1)
                assert M == gcd(r, l * v + 1) and M % 1 == 0 and gcd(M, v) == 1
                assert r % M == 0                   # M | r (IIa)
                cells.append(('IIa', v, l, M, km, Di))
            l += 1
        lI = w * r / Di                             # I: nu = 1, l = wr/Di
        if lI.denominator == 1 and lI >= 1:
            cells.append(('I', 1, int(lI), gcd(r, int(lI)), km, Di))
        lmax = int((w * (2 * r - 1) / 2) / Di)      # ZCH: nu(l Di - w(r-1)) = w
        for l in range(1, lmax + 1):
            den = l * Di - w * (r - 1)
            if den <= 0:
                continue
            nu = w / den
            if nu.denominator == 1 and nu >= 2:
                v = int(nu)
                M = gcd((r - 1) * v + 1, l)
                assert gcd(M, v) == 1
                cells.append(('ZCH', v, l, M, km, Di))
        km += 1
    return cells

def child_datum(fam, r, v, l, w):
    """Merged-child (kap, D/i, rho) = w*(dq_c, dp_c, 1)/Delta_c  (DS4 5a)."""
    dp, dq = {'IIa': (r * v, (r + l) * v + 1),
              'ZCH': ((r - 1) * v + 1, (r - 1 + l) * v + 1),
              'I': (r, r + l)}[fam]
    Dc = dq - dp
    return w * dq / Dc, w * dp / Dc, w / Dc

# --------------------------------------------------- C'. cascade closure
def zch_reachable(w, balphs):
    """ZCH cell at (non-0-edge) w: needs a 0-chain branch z with w_z in A_z,
    w = nu_e * w_z, nu_e >= 2 integer, and w in every other branch (sec 5c)."""
    for z, Az in enumerate(balphs):
        if any(w not in A for j, A in enumerate(balphs) if j != z):
            continue
        for wz in Az:
            q = w / wz
            if q.denominator == 1 and q >= 2:
                return True
    return False

def merge_cascade_ws(balphs):
    """M=1-emitting merge of the given branch alphabets: child w's (C' (ii))."""
    r = len(balphs)
    joint = set(balphs[0]).intersection(*balphs[1:])
    kids = set()
    for w in joint:
        if gcd(r, w.denominator) == 1:
            kids.add(w * r)                          # IIa l=0 (MP7 cascade)
        for fam, v, l, M, km, Di in window_cells(w, r):
            if M != 1:
                continue
            if fam == 'IIa':
                kids.add(w * Fr(r + l, l * v + 1))
            elif fam == 'I' and not (r == 2 and l % 2 == 0):
                kids.add(w * Fr(r + l - 1, l))       # r=2 even-l: log-dead
            elif fam == 'ZCH' and zch_reachable(w, balphs):
                kids.add(w * Fr(r - 1 + l, l * v))
    for z in range(r):                               # ZCH twisted joins
        others = [set(A) for j, A in enumerate(balphs) if j != z]
        for w in set.intersection(*others) - joint:
            for fam, v, l, M, km, Di in window_cells(w, r):
                if fam == 'ZCH' and M == 1 and zch_reachable(w, balphs):
                    kids.add(w * Fr(r - 1 + l, l * v))
    return kids

ALPH_MEMO = {}

def branch_alph(ws):
    """Attainable arriving-w alphabet of a branch holding the pole-w0 multiset
    ws: leaf = resonant closure; multi-pole = cascade children over every
    internal hierarchy, re-closed.  Budget exact: one merge per internal node."""
    ws = tuple(sorted(ws))
    if ws in ALPH_MEMO:
        return ALPH_MEMO[ws]
    if len(ws) == 1:
        out = frozenset(w_closure(ws[0])[0])
    else:
        kids = set()
        for blocks in block_partitions(ws):
            kids |= merge_cascade_ws([branch_alph(b) for b in blocks])
        out = set()
        for k in kids:
            out |= w_closure(k)[0]
        out = frozenset(out)
    ALPH_MEMO[ws] = out
    return out

def set_partitions(items):
    """All set partitions of a list (as lists of lists)."""
    if len(items) == 1:
        yield [items]
        return
    first, rest = items[0], items[1:]
    for part in set_partitions(rest):
        for i in range(len(part)):
            yield part[:i] + [[first] + part[i]] + part[i + 1:]
        yield [[first]] + part

def block_partitions(ws):
    """Partitions of the w0 multiset into >= 2 blocks, deduped by signature."""
    seen, out = set(), []
    for part in set_partitions(list(range(len(ws)))):
        if len(part) < 2:
            continue
        blocks = tuple(sorted(tuple(sorted(ws[i] for i in blk)) for blk in part))
        if blocks not in seen:
            seen.add(blocks)
            out.append(blocks)
    return out

# ------------------------------------------------------------ cell engine
KILL_ORDER = ['mp7_l0_impossible', 'mp7_l0_M1', 'M1_mp2', 'mp9_nu1_even_l',
              'zch_w_ratio', 'root_w_window', 'root_even_l', 'root_st94']

def note(cellmap, key, verdict, data, etag):
    c = cellmap.setdefault(key, {'verdicts': set(), 'entries': set(),
                                 'contexts': 0, 'data': data})
    c['verdicts'].add(verdict)
    c['entries'].add(etag)
    c['contexts'] += 1

def enum_context(m, td, w, r, balphs, cellmap, etag, zch_only=False):
    """All J' cells at one join context (w shared by the r branches)."""
    if not zch_only:                                  # l = 0 anatomy (MP7)
        note(cellmap, ('IIa', r, fstr(w), None, 0, None), 'mp7_l0_M1',
             {'fam': 'IIa', 'r': r, 'w': fstr(w), 'l': 0}, etag)
        for fam in ('ZCH', 'I'):
            note(cellmap, (fam, r, fstr(w), None, 0, None), 'mp7_l0_impossible',
                 {'fam': fam, 'r': r, 'w': fstr(w), 'l': 0}, etag)
    for fam, v, l, M, km, Di in window_cells(w, r):
        if zch_only and fam != 'ZCH':
            continue
        key = (fam, r, fstr(w), v, l, km)
        kap, dio, rho = child_datum(fam, r, v, l, w)
        data = {'fam': fam, 'r': r, 'w': fstr(w), 'nu': v, 'l': l, 'M': M,
                'kap_m': km, 'Di': fstr(Di), 'child_kap': fstr(kap),
                'child_D_over_i': fstr(dio), 'child_rho': fstr(rho),
                'lambda_spent': 0, 'suffix_budget': td - 2}
        if M == 1:
            note(cellmap, key, 'M1_mp2', data, etag)
        elif fam == 'I' and r == 2:
            note(cellmap, key, 'mp9_nu1_even_l', data, etag)
        elif fam == 'ZCH' and not zch_reachable(w, balphs):
            note(cellmap, key, 'zch_w_ratio', data, etag)
        else:
            note(cellmap, key, 'SURVIVE', data, etag)

def enum_root(m, td, r, joint, cellmap, etag):
    """R layer at one final-merge context: case (IV), w = 1 - l_f/i0 < 1."""
    wlow = sorted(w for w in joint if 0 < w < 1)
    for l in range(1, td - 1):                        # printed l <= td-2
        if not wlow:
            note(cellmap, ('ROOT', r, '-', 1, l, None), 'root_w_window',
                 {'fam': 'ROOT', 'r': r, 'l': l, 'w': None}, etag)
            continue
        for w in wlow:
            key = ('ROOT', r, fstr(w), 1, l, None)
            data = {'fam': 'ROOT', 'r': r, 'w': fstr(w), 'nu': 1, 'l': l,
                    'M': gcd(r, l), 'lf_over_i0': fstr(1 - w),
                    'psi': r + l - 1, 'kf': f'({r}+{l})*lf',
                    'lambda_spent': 0, 'suffix_budget': td - 1 - (r + l - 1)}
            if l % 2 == 0:
                note(cellmap, key, 'root_even_l', data, etag)
            elif l > td - r:
                note(cellmap, key, 'root_st94', data, etag)
            else:
                note(cellmap, key, 'SURVIVE', data, etag)

def run_cell(m, td):
    """Full BOOK(m, td) enumeration; returns the result dict."""
    ents = entries(td, m)
    cellmap, stats = {}, {
        'entries_total': len(ents), 'entries_all_b1': 0,
        'entries_offaxis': 0, 'offaxis_tags': [], 'contexts': 0,
        'alphabet': {}, 'entry_w0': {}}
    for al, be, poles in ents:
        etag = f"({al},{be})" + "+".join(
            f"L{L}a{a}b{b}n{nu}" for (L, a, b, nu) in poles)
        if any(b >= 2 for (L, a, b, nu) in poles):
            stats['entries_offaxis'] += 1
            stats['offaxis_tags'].append(etag)        # M>=2 entry: off-axis
            continue
        stats['entries_all_b1'] += 1
        ws = tuple(sorted(w0_of(al, be, a, b, nu) for (L, a, b, nu) in poles))
        for w0 in ws:
            if fstr(w0) not in stats['entry_w0']:
                W, gen = w_closure(w0)
                stats['entry_w0'][fstr(w0)] = {
                    'W': sorted(map(fstr, W)), 'gen': gen, 'd0': 2 * gen + 2}
        for blocks in block_partitions(ws):
            balphs = [branch_alph(b) for b in blocks]
            r = len(balphs)
            joint = frozenset(balphs[0]).intersection(*balphs[1:])
            stats['contexts'] += 1
            for w in sorted(joint):
                enum_context(m, td, w, r, balphs, cellmap, etag)
            for z in range(r):                        # ZCH twisted contexts
                others = [set(A) for j, A in enumerate(balphs) if j != z]
                for w in sorted(set.intersection(*others) - joint):
                    enum_context(m, td, w, r, balphs, cellmap, etag,
                                 zch_only=True)
            enum_root(m, td, r, joint, cellmap, etag)
        for w in {x for w in ws for x in branch_alph((w,))}:
            stats['alphabet'][fstr(w)] = stats['alphabet'].get(fstr(w), 0) + 1
    # aggregate verdicts: any-context survival wins (conservative book)
    hist, survivors = {}, []
    for key, c in sorted(cellmap.items(), key=lambda kv: str(kv[0])):
        if 'SURVIVE' in c['verdicts']:
            d = dict(c['data'])
            d['n_entries'] = len(c['entries'])
            d['entries'] = sorted(c['entries'])[:6]
            survivors.append(d)
            hist['SURVIVE'] = hist.get('SURVIVE', 0) + 1
        else:
            v = next(k for k in KILL_ORDER if k in c['verdicts'])
            hist[v] = hist.get(v, 0) + 1
    return {'m': m, 'td': td, 'stats': stats, 'total_cells': len(cellmap),
            'histogram': hist, 'survivors': survivors}

# ------------------------------------------------------------------ gate
def gate():
    """td=6, m=2 must reproduce the promoted record cell-for-cell."""
    res = run_cell(2, 6)
    surv = res['survivors']
    want = {'fam': 'IIa', 'r': 2, 'w': '2', 'nu': 3, 'l': 1, 'M': 2,
            'kap_m': 5, 'child_kap': '5', 'child_D_over_i': '3',
            'child_rho': '1/2'}
    okc = (len(surv) == 1 and
           all(surv[0][k] == v for k, v in want.items()) and
           not any(s['fam'] == 'ROOT' for s in surv))
    print(f"GATE td=6 m=2: survivors={len(surv)} "
          f"{[ (s['fam'], s['r'], s['nu'], s['l'], s['M'], s['kap_m']) for s in surv ]}")
    print(f"  histogram: {res['histogram']}")
    print("GATE " + ("PASS: unique IIa (2,3,1) M=2 kap=5 child (5,3,1/2) "
                     "at w=2 (residue-A), R empty" if okc else "FAIL"))
    return okc, res

# ------------------------------------------------------------------ main
def main():
    os.makedirs(OUTDIR, exist_ok=True)
    okc, _ = gate()
    if not okc:
        sys.exit(1)
    summary = []
    print(f"\n{'(m,td)':8s} {'entries':>7s} {'b1':>4s} {'off':>4s} "
          f"{'cells':>6s} {'killed':>6s} {'surv':>5s}  histogram")
    for td in range(6, 15):
        for m in range(2, td // 3 + 1):
            res = run_cell(m, td)
            ns = res['histogram'].get('SURVIVE', 0)
            nk = res['total_cells'] - ns
            st = res['stats']
            row = {'m': m, 'td': td, 'entries': st['entries_total'],
                   'all_b1': st['entries_all_b1'],
                   'offaxis': st['entries_offaxis'],
                   'cells': res['total_cells'], 'killed': nk, 'survivors': ns,
                   'histogram': res['histogram']}
            summary.append(row)
            hkill = {k: v for k, v in sorted(res['histogram'].items())
                     if k != 'SURVIVE'}
            print(f"m={m} td={td:2d} {st['entries_total']:7d} "
                  f"{st['entries_all_b1']:4d} {st['entries_offaxis']:4d} "
                  f"{res['total_cells']:6d} {nk:6d} {ns:5d}  {hkill}")
            with open(os.path.join(OUTDIR, f'book_m{m}_td{td}.json'), 'w') as f:
                json.dump(res, f, indent=1, default=str)
    with open(os.path.join(OUTDIR, 'summary.json'), 'w') as f:
        json.dump(summary, f, indent=1)
    tot = sum(r['cells'] for r in summary)
    tsv = sum(r['survivors'] for r in summary)
    print(f"\nTOTAL: {tot} cells, {tot - tsv} killed, {tsv} survivors "
          f"across {len(summary)} (m,td) panels")

if __name__ == '__main__':
    main()
