#!/usr/bin/env python3
"""E5-corrected td-7 class-B/C census (the post-E5 book), 2026-08-13.

Supersession chain:
  * BOOK-OFFAXIS.md s10 P4: 62-cell priced book (px5.py, BOOK pin
    kbar = (mu0*nu_U*w_U - 2)/(mu0-1) -- the mixed/px5 pin: it uses the
    ARRIVAL vertex nu_U; px5.py:244).
  * BOOK-OFFAXIS.md s11: T1 generalized zero-chain law (d_p | d_q kills)
    -> 6 cells / 53 routes (35 eq).
  * xmodel/sol-gluing-design.md s2.2: E5 preflight, cell-level 6 -> 2.
    REFUTED at cell level by xmodel/grok-gluing-preflight-review.md
    (finding 1: four recorded ARRIVALS fail (I4)=(I5), but two of those
    four CELLS are E5-realizable through other priced arrivals;
    finding 2: the class-C menu was never re-enumerated under the E5 pin).
  * THIS ENGINE: re-solves the class-B/C menu under the E5-corrected pin
        kbar = (mu0 * nu_G * w_U - 2)/(mu0 - 1)                  (I4)
    which pins the cell from (mu0, nu_G, w_U) and does NOT use nu_U.
    A cell is kept iff at least one admissible chain-2 zero-arrival
    realizes the E5 matching (I4) = (I5), i.e. the E5-required weight
        w_U^req = (kbar_cell*(mu0-1) + 2)/(mu0*nu_G),
        kbar_cell = 2*d_q/(d_q - d_p),                           (I5)
    is a priced state (w_U^req, M_U) of the filed chain-2 closure
    (px5.close_with_cells((3/2,2), budget 5)) with mu0 | M_U (St 8.4)
    and a legal arrival vertex per px5's own arrival law
    (neutral nu = -1 mod mu0 / direct stored step-cell / entry).
    Class B (mu0 = 1) pin: corrected H6 + chain-1 handshake give
    nu_G * w_U = 2 (sol-gluing-design (I5e)).

Cap-free class-C inversion (sol-gluing-design (I5a)-(I5d), conditional on
CONJECTURE H5a / promoted E5 + P3's one-orbit class-C classification):
with m = mu0 >= 2, r = w_U, g = nu_G, c = d_q - d_p, matching (I4)=(I5)
is c = 2(m-1)(m+g)/(m(gr-2)); c(g) is strictly decreasing on g >= g0 :=
max(2, floor(2/r)+1) with limit 2(m-1)/(mr), so every solution has
integer c in (2(m-1)/(mr), c(g0)] and g = 2m(c+m-1)/(cmr - 2(m-1))
is its unique candidate.  NO nu-cap, no state cap beyond the filed
closure itself.

Unchanged filters (exactly the current book's):
  * T1 zero-chain law: d_p | d_q kills (<=> M = d_p <=> kbar in {3,4});
    xmodel/sol-td7-law.md (LAW).  Scope (mu >= 1, ell >= 1) is automatic
    here: ell = (d_q-1)/nu - 1 and c >= 1 force d_q > d_p >= mu0 + 2.
  * N1/L6 primitivity gcd(kbar, nu_G) = 1 (SHEET6-III.md:121-129;
    passes on all 62 recorded cells).  Applied binding; bites reported.
  * MP2 trunk M_G >= 2; nu_G | d_q - 1 (P3); kbar integral >= 3;
    budget via px5.feasible (St 9.4 (25) + P1 psi-certificate) with
    lam_pre = lam2 = closure cost of the arrival state.

H5a readings (grok review finding 4 trichotomy):
  * 'promoted' -- H5a Q-value + E5 (g')/(h'): nu_U free (any legal vertex;
    the neutral congruence class is always available, so the gate is
    mu0 | M_U + state existence; arrival kinds are recorded).
  * 'forced'   -- printed (g)/(h) + forced nu_G = nu_U (the other coherent
    reading): the arrival vertex must BE nu_G and be legal at the state.
  * P-value reading: (H5)/(H6)/(I4) are not theorems, no zero-edge
    matching condition exists, and St 3.8 fails as printed -- no census
    is derivable at this tier (reported as a rider, not enumerated).

Route-count conventions: raw = one record per (arrival state, trunk
terminal) via px5.feasible; eq = records with total lam = budget;
dedup = px5-parity key that drops the state M_U (px5.py:254-262 ignores
M2) and, E5-specifically, carries no nu_U (the E5 pin is vertex-free).

Machinery reuse (READ-ONLY): cases/scratch_offaxis_pricing/px5.py
(close_with_cells, feasible, divisors, cls_C_cells) + px2 via px5.
Running this engine modifies no repo file.  Gates (mandatory, exit != 0
on failure):
  G1  grok six-row replay: (I3)-(I5)/BOOK pins + X-handshake on the six
      recorded arrivals reproduce grok-gluing-preflight-review.md exactly;
  G2  per-cell E5 re-solve of the six matches the review's finding-1
      table (required w_U, in-closure?, lam, route counts, N1);
  G3  BOOK-pin parity: replaying px5's own class-B/C loops in-engine
      reproduces the 62-cell book and the six-cell 53/35 record;
  G4  positive controls: (9,15,7,3)@2 and (10,15,7,5)@3 appear in the
      corrected book (both readings) with their recorded arrivals;
  G5  negative controls: none of the 56 law-dead cells appears in the
      corrected book (either reading).
"""
import os
import sys
from fractions import Fraction as Fr
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'scratch_offaxis_pricing'))
import px5  # noqa: E402  (read-only reuse)

ENTRY = (Fr(3, 2), 2)


def floor_fr(x):
    return x.numerator // x.denominator


# ----------------------------------------------------------------------
# Recorded six-cell record (BOOK-OFFAXIS.md s11 + sol-gluing-design s2.2/2.3)
# cell -> (mu0, recorded (w_U, nu_U), recorded lam2)
SIX = {
    (9, 15, 7, 3): (2, (Fr(1, 2), 7), 4),
    (10, 15, 7, 5): (3, (Fr(2, 3), 7), 2),
    (15, 25, 8, 5): (7, (Fr(2, 21), 48), 5),
    (15, 25, 12, 5): (3, (Fr(1, 2), 8), 5),
    (18, 27, 13, 9): (5, (Fr(2, 15), 39), 5),
    (39, 65, 32, 13): (7, (Fr(2, 21), 48), 5),
}

# grok-gluing-preflight-review.md per-cell table (lines 17-22) and
# X-handshake table (lines 30-35):
# cell -> (kbar_cell, X, kbar_E5, kbar_BOOK, req_w, X_E5, X_BOOK)
GROK_ROWS = {
    (9, 15, 7, 3): (5, 3, Fr(5), Fr(5), Fr(1, 2), Fr(3), Fr(3)),
    (10, 15, 7, 5): (6, 4, Fr(6), Fr(6), Fr(2, 3), Fr(4), Fr(4)),
    (15, 25, 8, 5): (5, 3, Fr(5, 9), Fr(5), Fr(4, 7), Fr(89, 3), Fr(3)),
    (15, 25, 12, 5): (5, 3, Fr(8), Fr(5), Fr(1, 3), Fr(-3), Fr(3)),
    (18, 27, 13, 9): (6, 4, Fr(5, 3), Fr(6), Fr(2, 5), Fr(64, 3), Fr(4)),
    (39, 65, 32, 13): (5, 3, Fr(29, 9), Fr(5), Fr(1, 7), Fr(41, 3), Fr(3)),
}

# grok finding-1 E5 re-solve table (review lines 55-62):
# cell -> (in_closure, lam_min, raw_routes, eq_routes)
GROK_RESOLVE = {
    (9, 15, 7, 3): (True, 4, 4, 4),
    (10, 15, 7, 5): (True, 2, 47, 29),
    (15, 25, 8, 5): (False, None, 0, 0),
    (15, 25, 12, 5): (True, 5, 2, 2),
    (18, 27, 13, 9): (True, 3, 37, 33),
    (39, 65, 32, 13): (False, None, 0, 0),
}

# The 56 law-dead cells (xmodel/sol-td7-law.md, exact census): class-B
# (3,9,2,3) + 30 class-C kbar=3 + 25 class-C kbar=4.  (dp,dq,nu,M).
DEAD56 = [(3, 9, 2, 3)] + [
    # kbar = 3
    (5, 15, 2, 5), (7, 21, 2, 7), (7, 21, 4, 7), (7, 21, 5, 7),
    (9, 27, 2, 9), (11, 33, 2, 11), (11, 33, 4, 11), (11, 33, 8, 11),
    (12, 36, 5, 12), (12, 36, 7, 12),
    (15, 45, 2, 15), (15, 45, 4, 15), (15, 45, 11, 15),
    (17, 51, 10, 17), (19, 57, 8, 19), (19, 57, 14, 19),
    (22, 66, 13, 22),
    (27, 81, 10, 27), (27, 81, 16, 27), (27, 81, 20, 27),
    (32, 96, 19, 32), (35, 105, 26, 35), (42, 126, 25, 42),
    (43, 129, 32, 43), (51, 153, 38, 51), (52, 156, 31, 52),
    (62, 186, 37, 62), (67, 201, 50, 67), (83, 249, 62, 83),
    (99, 297, 74, 99),
    # kbar = 4
    (5, 10, 3, 5), (8, 16, 3, 8), (8, 16, 5, 8), (11, 22, 7, 11),
    (13, 26, 5, 13), (14, 28, 3, 14), (14, 28, 9, 14),
    (17, 34, 11, 17), (18, 36, 5, 18), (18, 36, 7, 18),
    (20, 40, 13, 20), (23, 46, 15, 23), (26, 52, 17, 26),
    (28, 56, 11, 28), (29, 58, 19, 29),
    (32, 64, 9, 32), (32, 64, 21, 32),
    (38, 76, 15, 38), (38, 76, 25, 38),
    (44, 88, 29, 44), (50, 100, 33, 50), (56, 112, 37, 56),
    (62, 124, 41, 62), (68, 136, 45, 68), (74, 148, 49, 74),
]
assert len(DEAD56) == 56 and len(set(DEAD56)) == 56


# ----------------------------------------------------------------------
# E5-corrected candidate cells
def e5_cells_C(m, r):
    """All class-C cells (g, c, dp, dq, kbar, MG, w_tr) whose E5 matching
    (I4)=(I5) is realized at arrival weight r = w_U with mult m = mu0 >= 2.
    Cap-free inversion (I5a)-(I5d); pre-T1/N1/arrival/budget gates only:
    kbar integral >= 3, nu_G | dq - 1, MP2 M_G >= 2."""
    assert m >= 2 and r > 0
    out = []
    g0 = max(2, floor_fr(Fr(2) / r) + 1)          # g >= 2 and g*r > 2
    den0 = m * (g0 * r - 2)
    assert den0 > 0
    cmax = floor_fr(Fr(2 * (m - 1) * (m + g0)) / den0)   # c(g0), (I5c/d)
    for c in range(1, cmax + 1):
        den = c * m * r - 2 * (m - 1)
        if den <= 0:                               # c > 2(m-1)/(mr) strict
            continue
        gg = Fr(2 * m * (c + m - 1)) / den         # (I5b)
        if gg.denominator != 1:
            continue
        g = int(gg)
        if g < g0:
            continue
        dp, dq = m + g, m + g + c
        kb = Fr(2 * dq, c)                         # kbar_cell, (I5)
        if kb.denominator != 1:
            continue
        kbar = int(kb)
        # matching identity (I4) == (I5) holds by construction; assert it
        assert Fr(m * g * r - 2, m - 1) == kbar
        if kbar < 3:
            continue
        if (m + c - 1) % g:                        # nu_G | mu0 + c - 1 (I5a)
            continue
        MG = gcd(dp, dq)
        if MG < 2:                                 # MP2
            continue
        w_tr = (Fr(kbar) - Fr(kbar - 2, dp)) / g
        out.append((g, c, dp, dq, kbar, MG, w_tr))
    return out


def e5_cells_B(r):
    """Class B (mu0 = 1): corrected H6 + chain-1 handshake give
    nu_G * w_U = 2, so g = 2/r must be an integer >= 2; then d_p = 1+g,
    g | c, and kbar = 2 + 2(1+g)/c integral => c | 2(1+g) (I5e).
    (g | c and c | 2(1+g) force g | 2, so only w_U = 1 states can carry
    the M >= 2 cell (3,9,2,3); all other states return [].)"""
    gg = Fr(2) / r
    if gg.denominator != 1 or gg < 2:
        return []
    g = int(gg)
    out = []
    for c in px5.divisors(2 * (1 + g)):
        if c % g:
            continue
        dp, dq = 1 + g, 1 + g + c
        kb = Fr(2 * dq, c)
        assert kb.denominator == 1 and kb >= 3
        kbar = int(kb)
        MG = gcd(dp, dq)
        if MG < 2:                                 # MP2 (kills (3,5))
            continue
        w_tr = (Fr(kbar) - Fr(kbar - 2, dp)) / g
        out.append((g, c, dp, dq, kbar, MG, w_tr))
    return out


# ----------------------------------------------------------------------
# Arrival law (px5's own, verbatim semantics; superset-safe rider (v))
def nu_legal(nu, state, mu0, cellmap):
    """Kind of legality of arrival vertex nu for mult mu0 at state (w,M),
    or None.  px5.py:236-242: neutral nu = -1 (mod mu0) / direct stored
    step-cell (nu, Mc) with mu0 | Mc / entry (nu=3, mu0 | 2, seed state)."""
    w, M = state
    if (nu + 1) % mu0 == 0:
        return 'neutral'
    for (nuc, Mc) in cellmap.get((w, M), ()):
        if nuc == nu and Mc % mu0 == 0:
            return 'direct'
    if nu == 3 and (w, M) == ENTRY and 2 % mu0 == 0:
        return 'entry'
    return None


def arrival_menu(state, mu0, cellmap):
    """Compact description of ALL legal arrival vertices at (state, mu0)."""
    w, M = state
    kinds = ['neutral nu=%d(mod %d)' % ((mu0 - 1) % mu0, mu0)]
    direct = sorted((nuc, Mc) for (nuc, Mc) in cellmap.get((w, M), ())
                    if Mc % mu0 == 0)
    if direct:
        kinds.append('direct ' + ','.join('(%d,%d)' % d for d in direct))
    if (w, M) == ENTRY and 2 % mu0 == 0:
        kinds.append('entry nu=3')
    return kinds


# ----------------------------------------------------------------------
def enumerate_book(reading, dist, cellmap):
    """E5-corrected class-B/C enumeration under one H5a reading.
    Returns {cellkey: record}; cellkey = (dp, dq, nu_G, M_G); record has
    mu0, kbar, w_req, per-state arrival/route data, and T1/N1 flags."""
    assert reading in ('promoted', 'forced')
    book = {}
    for (w2, M2), lam2 in sorted(dist.items(),
                                 key=lambda kv: (kv[1], kv[0][0], kv[0][1])):
        for mu0 in px5.divisors(M2):        # 1 always present: class B
            cands = (e5_cells_B(w2) if mu0 == 1 else e5_cells_C(mu0, w2))
            for (g, c, dp, dq, kbar, MG, w_tr) in cands:
                # arrival gate at this state
                if reading == 'forced':
                    kind = nu_legal(g, (w2, M2), mu0, cellmap)
                    if kind is None:
                        continue
                    menu = ['forced nu_U=nu_G=%d (%s)' % (g, kind)]
                else:
                    menu = arrival_menu((w2, M2), mu0, cellmap)
                    # neutral class is always nonempty: gate is mu0 | M_U
                routes = []
                ctx = ('C mu0=%d w2=%s(lam%d) cell(%d,%d)nu%dM%d'
                       % (mu0, w2, lam2, dp, dq, g, MG)) if mu0 >= 2 else \
                      ('B w2=%s(lam%d) cell(%d,%d)nu%dM%d'
                       % (w2, lam2, dp, dq, g, MG))
                px5.feasible(lam2, w_tr, MG, ctx, routes)
                if not routes:
                    continue
                key = (dp, dq, g, MG)
                rec = book.setdefault(key, {
                    'mu0': mu0, 'kbar': kbar, 'X': kbar - 2, 'c': c,
                    'w_req': w2, 'w_tr': w_tr, 'states': [], 'raw': [],
                    'T1_alive': dq % dp != 0, 'N1_ok': gcd(kbar, g) == 1,
                    'cls': 'B' if mu0 == 1 else 'C'})
                assert rec['mu0'] == mu0 and rec['kbar'] == kbar \
                    and rec['w_req'] == w2
                rec['states'].append((M2, lam2, menu, len(routes),
                                      sum(1 for (t, b, _, _) in routes
                                          if t == b)))
                rec['raw'] += routes
    # route summaries (px5-parity dedup: drop M_U; E5 pin is nu_U-free)
    for key, rec in book.items():
        seen = {}
        for (tot, bud, ctx, t) in sorted(rec['raw']):
            k2 = (ctx, t.split('->')[-1])
            if k2 not in seen:
                seen[k2] = (tot, bud)
        rec['n_raw'] = len(rec['raw'])
        rec['n_eq'] = sum(1 for (t, b, _, _) in rec['raw'] if t == b)
        rec['n_dedup'] = len(seen)
        rec['n_dedup_eq'] = sum(1 for (t, b) in seen.values() if t == b)
    return book


def post_filter(book):
    """Apply the unchanged T1 law and N1 primitivity; return
    (alive, t1_killed, n1_killed) cell-key lists."""
    alive, t1k, n1k = [], [], []
    for key in sorted(book):
        rec = book[key]
        if not rec['T1_alive']:
            t1k.append(key)
        elif not rec['N1_ok']:
            n1k.append(key)
        else:
            alive.append(key)
    return alive, t1k, n1k


# ----------------------------------------------------------------------
# G1 + G2: grok replay
def gate_grok_replay(dist, cellmap, failures):
    print('--- G1: grok six-row replay (recorded arrivals) ---')
    for cell, (mu0, (wU, nuU), lam_rec) in sorted(SIX.items()):
        dp, dq, nuG, MG = cell
        kcell = Fr(2 * dq, dq - dp)
        assert kcell.denominator == 1
        kcell = int(kcell)
        X = kcell - 2
        kE5 = Fr(mu0 * nuG * wU - 2, mu0 - 1)
        kBOOK = Fr(mu0 * nuU * wU - 2, mu0 - 1)
        req = Fr(kcell * (mu0 - 1) + 2, 1) / (mu0 * nuG)
        XE5 = mu0 * (kcell - nuG * wU)
        XBOOK = mu0 * (kcell - nuU * wU)
        got = (kcell, X, kE5, kBOOK, req, XE5, XBOOK)
        exp = GROK_ROWS[cell]
        ok = got == exp
        verdict = 'PASS' if kE5 == kcell else 'REJECT'
        print('  %-16s mu0=%d kcell=%d X=%d kE5=%-5s kBOOK=%-2s req_w=%-4s'
              ' XE5=%-5s XBOOK=%s  arrival-verdict=%s  [%s]'
              % (str(cell), mu0, kcell, X, kE5, kBOOK, req, XE5, XBOOK,
                 verdict, 'match' if ok else 'MISMATCH'))
        if not ok:
            failures.append('G1 %s: got %s expected %s' % (cell, got, exp))

    print('--- G2: per-cell E5 re-solve of the six (review finding 1) ---')
    for cell, (mu0, _, _) in sorted(SIX.items()):
        dp, dq, nuG, MG = cell
        kcell = 2 * dq // (dq - dp)
        req = Fr(kcell * (mu0 - 1) + 2, 1) / (mu0 * nuG)
        states = sorted((M, lam) for (w, M), lam in dist.items()
                        if w == req and M % mu0 == 0)
        w_tr = (Fr(kcell) - Fr(kcell - 2, dp)) / nuG
        raw = []
        for (M, lam) in states:
            px5.feasible(lam, w_tr, MG, 'g2 M=%d lam=%d' % (M, lam), raw)
        n_raw = len(raw)
        n_eq = sum(1 for (t, b, _, _) in raw if t == b)
        inc = bool(states)
        lam_min = min((lam for (_, lam) in states), default=None)
        # lam reported by the review = min over route-contributing states
        contrib = sorted(set(l for (_, _, cx, _) in raw
                             for l in [int(cx.split('lam=')[1])]))
        lam_rep = contrib[0] if contrib else lam_min
        got = (inc, lam_rep, n_raw, n_eq)
        exp = GROK_RESOLVE[cell]
        ok = got == exp
        n1 = gcd(kcell, nuG)
        print('  %-16s req_w=%-4s states=%s routes=%d(%d eq) N1-gcd=%d [%s]'
              % (str(cell), req,
                 states if states else 'ABSENT from closure',
                 n_raw, n_eq, n1, 'match' if ok else 'MISMATCH'))
        if not ok:
            failures.append('G2 %s: got %s expected %s' % (cell, got, exp))


# ----------------------------------------------------------------------
# G3: BOOK-pin parity regression (px5's own loops replayed in-engine)
def gate_book_parity(dist, cellmap, failures):
    print('--- G3: BOOK-pin parity (px5 class-B/C loops replayed) ---')
    surv = []
    # class B, px5.main:217-228 verbatim logic
    lamB = None
    for (w, M), lam in dist.items():
        rr = Fr(2) / w
        if rr.denominator == 1 and rr >= 2:
            lamB = lam if lamB is None else min(lamB, lam)
    if lamB is not None:
        px5.feasible(lamB, Fr(4, 3), 3, 'B c2at0 cell (3,9)M3', surv)
    nB = len(surv)
    # class C, px5.main:229-252 verbatim logic (BOOK pin, nu_U-based)
    cells_seen = set()
    for (w2, M2), lam2 in sorted(dist.items(), key=lambda kv: kv[1]):
        for mu0 in px5.divisors(M2):
            if mu0 < 2:
                continue
            numax = ((4 * mu0 + 2) * (mu0 - 1) + 2) / (mu0 * w2) + 1
            nu2 = 2
            while nu2 <= numax:
                ok = ((nu2 + 1) % mu0 == 0)
                for (nuc, Mc) in cellmap.get((w2, M2), ()):
                    if nuc == nu2 and Mc % mu0 == 0:
                        ok = True
                if nu2 == 3 and (w2, M2) == ENTRY and 2 % mu0 == 0:
                    ok = True
                if ok:
                    kb = Fr(mu0 * nu2 * w2 - 2, mu0 - 1)
                    if kb.denominator == 1 and kb >= 3:
                        for (dp, dq, nuG, MG, w_tr) in px5.cls_C_cells(
                                int(kb), mu0):
                            n0 = len(surv)
                            px5.feasible(
                                lam2, w_tr, MG,
                                'C mu0=%d w2=%s(lam%d) nu2=%d '
                                'cell(%d,%d)nu%dM%d'
                                % (mu0, w2, lam2, nu2, dp, dq, nuG, MG),
                                surv)
                            if len(surv) > n0:
                                cells_seen.add((dp, dq, nuG, MG))
                nu2 += 1
    book62 = cells_seen | ({(3, 9, 2, 3)} if nB else set())
    exp62 = set(DEAD56) | set(SIX)
    ok = book62 == exp62
    print('  class-C cells: %d, +class-B: %d -> %d (expect 62)  [%s]'
          % (len(cells_seen), 1 if nB else 0, len(book62),
             'match' if ok else 'MISMATCH'))
    if not ok:
        failures.append('G3 62-cell set: missing %s extra %s'
                        % (sorted(exp62 - book62), sorted(book62 - exp62)))
    # six-cell 53/35 record (px5 dedup key, px5.py:254-262)
    seen = {}
    for (tot, bud, ctx, t) in sorted(surv):
        k = (ctx.split(' lam')[0], t.split('->')[-1])
        if k not in seen:
            seen[k] = (tot, bud, ctx)
    per = {}
    for (tot, bud, ctx) in seen.values():
        for cell in SIX:
            if 'cell(%d,%d)nu%dM%d' % cell in ctx:
                d, e = per.get(cell, (0, 0))
                per[cell] = (d + 1, e + (1 if tot == bud else 0))
    tot_d = sum(d for (d, e) in per.values())
    tot_e = sum(e for (d, e) in per.values())
    ok2 = (tot_d, tot_e) == (53, 35)
    print('  six-cell record: %d dedup / %d eq (expect 53/35)  [%s]'
          % (tot_d, tot_e, 'match' if ok2 else 'MISMATCH'))
    for cell in sorted(per):
        print('    %-16s %d dedup / %d eq'
              % (str(cell), per[cell][0], per[cell][1]))
    if not ok2:
        failures.append('G3 six-cell record: got %d/%d expected 53/35'
                        % (tot_d, tot_e))


# ----------------------------------------------------------------------
def print_book(name, book, alive, t1k, n1k):
    print('=== E5-corrected book [%s reading]: %d alive cells '
          '(pre-filter %d; T1-killed %d; N1-killed %d) ==='
          % (name, len(alive), len(book), len(t1k), len(n1k)))
    for key in alive:
        rec = book[key]
        print('  %s@%d  kbar=%d X=%d w_req=%s w_tr=%s  routes raw=%d(%d eq)'
              ' dedup=%d(%d eq)'
              % (key, rec['mu0'], rec['kbar'], rec['X'], rec['w_req'],
                 rec['w_tr'], rec['n_raw'], rec['n_eq'], rec['n_dedup'],
                 rec['n_dedup_eq']))
        for (M2, lam2, menu, n, neq) in rec['states']:
            print('      state (%s,%d) lam=%d routes=%d(%d eq): %s'
                  % (rec['w_req'], M2, lam2, n, neq, '; '.join(menu)))
    tots = tuple(sum(book[k][f] for k in alive)
                 for f in ('n_raw', 'n_eq', 'n_dedup', 'n_dedup_eq'))
    print('  TOTALS [%s]: %d cells; routes raw=%d(%d eq) '
          'dedup=%d(%d eq)' % ((name, len(alive)) + tots))
    if t1k:
        print('  T1-killed (d_p | d_q), pre-T1 E5-realizable:')
        for key in t1k:
            rec = book[key]
            print('    %s@%d kbar=%d w_req=%s routes raw=%d [%s]'
                  % (key, rec['mu0'], rec['kbar'], rec['w_req'],
                     rec['n_raw'],
                     'in DEAD56' if key in set(DEAD56) else 'NEW pre-T1'))
    if n1k:
        print('  N1-killed (gcd(kbar,nu_G) > 1):')
        for key in n1k:
            rec = book[key]
            print('    %s@%d kbar=%d w_req=%s' % (key, rec['mu0'],
                                                  rec['kbar'], rec['w_req']))


def report_class_B(name, book, dist):
    """Class B (mu0=1) under E5: nu_G*w_U = 2 and g|2 force nu_G = 2,
    w_U = 1 for the sole M>=2 cell (3,9,2,3).  Report its E5 status."""
    bcells = [k for k, r in book.items() if r['cls'] == 'B']
    states = sorted((M, lam) for (w, M), lam in dist.items() if w == 1)
    routes = []
    for (M, lam) in states:
        px5.feasible(lam, Fr(4, 3), 3, 'B probe', routes)
    print('  class B [%s]: E5 pin nu_G*w_U=2 => only cell (3,9,2,3) at '
          'w_U=1; w=1 states %s; budget-fitting routes %d => %s'
          % (name, states or 'ABSENT', len(routes),
             ('IN BOOK (pre-T1): %s' % bcells) if bcells else
             'not E5-realizable even pre-T1 (T1-dead regardless, kbar=3)'))


def gate_controls(name, book, alive, dist, cellmap, failures):
    aset = set(alive)
    # G4 positive controls with recorded arrivals
    for cell in ((9, 15, 7, 3), (10, 15, 7, 5)):
        mu0, (wU, nuU), lam_rec = SIX[cell]
        ok = cell in aset
        if ok:
            rec = book[cell]
            st = [(M2, lam2) for (M2, lam2, _, _, _) in rec['states']]
            ok = rec['w_req'] == wU and any(lam2 == lam_rec
                                            for (_, lam2) in st)
            ok = ok and any(
                nu_legal(nuU, (wU, M2), mu0, cellmap) is not None
                for (M2, _) in st)
        print('  G4[%s] %s@%d with recorded arrival (w=%s, nu=%d, lam=%d):'
              ' %s' % (name, cell, mu0, wU, nuU, lam_rec,
                       'PASS' if ok else 'FAIL'))
        if not ok:
            failures.append('G4[%s] %s' % (name, cell))
    # G5 negative controls
    bad = aset & set(DEAD56)
    print('  G5[%s] law-dead cells in corrected book: %d (expect 0): %s'
          % (name, len(bad), 'PASS' if not bad else 'FAIL ' + str(sorted(bad))))
    if bad:
        failures.append('G5[%s] %s' % (name, sorted(bad)))


def removal_reason(cell, mu0, reading, book, dist, cellmap):
    dp, dq, nuG, MG = cell
    if cell in book:
        return 'E5-realizable but killed by post-filter (T1/N1)'
    kcell = 2 * dq // (dq - dp)
    req = Fr(kcell * (mu0 - 1) + 2, 1) / (mu0 * nuG)
    states = [(M, lam) for (w, M), lam in dist.items()
              if w == req and M % mu0 == 0]
    if not states:
        return ('E5-required w_U=%s absent from the priced closure' % req)
    if reading == 'forced' and not any(
            nu_legal(nuG, (req, M), mu0, cellmap) for (M, _) in states):
        return ('w_U=%s priced (states %s) but nu_U=nu_G=%d is illegal at '
                'every state (arrival law)' % (req, sorted(states), nuG))
    return ('w_U=%s priced but no budget-fitting completion' % req)


def print_diff(name, book, alive, dist, cellmap):
    aset = set(alive)
    print('--- diff vs the s11 six-cell record [%s reading] ---' % name)
    for cell in sorted(SIX):
        mu0, (wU, nuU), lam_rec = SIX[cell]
        if cell not in aset:
            why = removal_reason(cell, mu0, name, book, dist, cellmap)
            print('  REMOVED %-16s@%d  recorded arrival (w=%s,nu=%d): %s'
                  % (str(cell), mu0, wU, nuU, why))
        else:
            rec = book[cell]
            if rec['w_req'] == wU:
                print('  KEPT    %-16s@%d  arrival unchanged (w=%s;'
                      ' recorded nu=%d still legal)'
                      % (str(cell), mu0, wU, nuU))
            else:
                print('  KEPT    %-16s@%d  ARRIVAL REPLACED: recorded'
                      ' (w=%s,nu=%d) fails (I4)=(I5); E5 arrival w=%s'
                      % (str(cell), mu0, wU, nuU, rec['w_req']))
    for cell in alive:
        if cell not in SIX:
            rec = book[cell]
            print('  ADDED   %-16s@%d  kbar=%d w_req=%s routes raw=%d(%d eq)'
                  % (str(cell), rec['mu0'], rec['kbar'], rec['w_req'],
                     rec['n_raw'], rec['n_eq']))


# ----------------------------------------------------------------------
def main():
    failures = []
    dist, cellmap = px5.close_with_cells(*ENTRY)   # filed closure, budget 5
    print('chain-2 priced closure: %d states (budget 5, seed %s)'
          % (len(dist), ENTRY))
    print()
    gate_grok_replay(dist, cellmap, failures)
    print()
    gate_book_parity(dist, cellmap, failures)
    print()
    books = {}
    for reading in ('promoted', 'forced'):
        book = enumerate_book(reading, dist, cellmap)
        alive, t1k, n1k = post_filter(book)
        books[reading] = (book, alive)
        print_book(reading, book, alive, t1k, n1k)
        report_class_B(reading, book, dist)
        gate_controls(reading, book, alive, dist, cellmap, failures)
        print_diff(reading, book, alive, dist, cellmap)
        print()
    pa = set(books['promoted'][1])
    fa = set(books['forced'][1])
    print('H5a conditionality: promoted book %d cells; forced book %d cells;'
          ' %s' % (len(pa), len(fa),
                   'IDENTICAL (caveat evaporates)' if pa == fa else
                   'DIFFERENT (both books recorded, conditionality stands): '
                   'promoted-only=%s' % sorted(pa - fa)))
    print('P-value H5a reading: (H5)/(H6)/(I4) are not theorems there; no '
          'zero-edge matching census is derivable at this tier (and St 3.8 '
          'fails as printed) -- rider only, not enumerated.')
    print()
    if failures:
        print('GATE FAILURES (%d):' % len(failures))
        for f in failures:
            print('  ' + f)
        return 1
    print('ALL GATES PASS (G1 grok replay, G2 six-cell E5 re-solve, '
          'G3 BOOK-pin parity 62/53/35, G4 positive controls, '
          'G5 negative controls x2 readings)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
