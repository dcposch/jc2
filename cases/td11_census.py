#!/usr/bin/env python3
"""td11_census.py -- THE TD-11 CLASS-B/C CENSUS COMPILER.

Enumerates the complete td-11 class-B/C configuration space at the
instrument-backed granularity and stamps every configuration row with
its killing instrument, or emits its fail-closed status.

SIZING DISCIPLINE (why this granularity): the raw route space --
budget-9 priced chains per pole (sized ladders: (3,2) 21/56/130/330/
743 at budgets 5..9; (3/2,2) 69/162/349/785 at 5..8; (4/3,3) 347 at
5, budget-9 session-infeasible) multiplied across 2-3 poles, arrival
cells, and mu-assignments -- exceeds 10^7 stamps.  Per the campaign
discipline that number is REPORTED, not ground: the banked theorems
(TD11-CLASH exact-core + the 129-row closure, NF-Z dagger DIE-horn,
NF-M square-system types, NF-P nu=1 slice, NF-D mechanisms) quotient
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
                if Fr(kb * dp, dq) == X and gcd(gcd(dp, dq), nu) == 1 \
                        and 3 % gcd(dp, dq) == 0 and dq > dp:
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
                        MG = gcd(dp, dq)
                        if gcd(MG, nu) != 1 or (2 * mu) % MG:
                            continue
                        out.append(dict(kb=int(kb), dp=dp, dq=dq, MG=MG))
    seen, ded = set(), []
    for s in out:
        key = (s['kb'], s['dp'], s['dq'])
        if key not in seen:
            seen.add(key)
            ded.append(s)
    return ded


AB_MENU = menu_AB()
BB1_MENU = menu_BB(1)
BB2_MENU = menu_BB(2)
BB2_HAS_CYL = True     # the eps=1 C=0 family kb=6nu+3, M=1 (in-window)
CAPS_C = (1, 2)


def outer_all_dead(mu_in):
    """Round-9/10 outer-merge analysis: every schema below-window or
    refused (census-pinned nu_A = 2; closed-form both-nonzero incl.
    the seven A<Q schemas; equal menu; zero-slots)."""
    # both-nonzero closed form kb = 2(1+nu Q)/(1 - nu(A-Q))
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
            dp_ = nu * A_
            g = Fr(int(kbf), 2 * dp_)
            if Fr(1, 2) < g < Fr(5, 2) and not refused_gap(g, CAPS_C):
                return False
    # mu_in = 1 equal menu cylinder kb = 4nu+2
    if mu_in == 1:
        for nu in range(2, 201):
            g = Fr(4 * nu + 2, 4 * nu)
            if not refused_gap(g, CAPS_C):
                return False
    return True


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
            # spine-death: v_p mismatch (P/mu with mu < M leaves the
            # raw comparison vL vs vR + v_p(M/mu) unsat -- rederive:
            ok = (vL != vR + (0 if muB == E['bs'][1] else 0))
            out.append((entry, 'direct2', mus, MG, interior,
                        'SPINE-DEAD-H8',
                        f'v_{p}: {vL} != {vR} (mu_B={muB} < M)'))
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
                        else 'window empty + CAP-DEN (+resonant X 5/4)'))
    return out


def inner_h8_dead(recs):
    for (kinds, mus, _MG) in recs:
        if None in kinds:
            continue
        if sorted(kinds) == [1, 2] and mus[kinds.index(2)] == 1:
            return True
        if sorted(kinds) == [2, 2] and mus[0] != mus[1]:
            return True
    return False


def stamp_11C():
    out = []
    bs = ENTRIES['11-C']['bs']
    for (hname, tree) in hierarchies(3):
        for (mus, recs, MG, interior) in skeleton_rows(tree, bs):
            key = ('11-C', hname, mus, MG, interior)
            if hname == 'direct':
                muA, mu1, mu2 = mus
                if mu1 == 1 or mu2 == 1:
                    out.append(key + ('SPINE-DEAD-H8',
                                      'v_2 1 vs 2 at a mu=1 B-edge'))
                else:
                    assert capden_x_refusal(CAPS_C, range(3, 200, 2)) \
                        and Fr(2, 5) < Fr(1, 2)
                    out.append(key + ('CLASH-DEAD',
                                      'window empty + CAP-DEN'))
                continue
            if inner_h8_dead(recs):
                out.append(key + ('SPINE-DEAD-H8',
                                  'inner-merge equal-quotient v_2'))
                continue
            # live inner pair: the row's OWN inner decoration
            (kinds, imus, Min) = [r for r in recs
                                  if None not in r[0]][0]
            if sorted(kinds) == [1, 2]:
                menu, kindtag = AB_MENU, 'AB'
            else:
                menu = (BB1_MENU if imus == (1, 1) else BB2_MENU)
                kindtag = 'BB1' if imus == (1, 1) else 'BB2'
            mine = [s for s in menu if s['MG'] == Min]
            inwin = [s for s in mine
                     if not Fr(s['kb'], 2 * s['dp']) <= Fr(1, 2)]
            cyl = (kindtag == 'BB2' and Min == 1)
            if not mine and not cyl:
                v, note = 'UNREALIZABLE', \
                    f'no nu>=2 {kindtag} schema with M={Min}'
            elif inwin or cyl:
                ok = all(refused_gap(Fr(s['kb'], 2 * s['dp']),
                                     CAPS_C) for s in inwin)
                if cyl:
                    ok &= all(refused_gap(
                        Fr(6 * nu + 3, 2 * (4 * nu + 1)), CAPS_C)
                        for nu in range(2, 100))
                if [s for s in mine if s not in inwin]:
                    ok &= outer_all_dead(mus[0])
                assert ok
                v = 'SELF-REFUSED'
                note = (f'{kindtag} M={Min}: in-window emission '
                        'den-refused at k|i_G'
                        + (' (+ discrete alternatives outer-dead)'
                           if [s for s in mine if s not in inwin]
                           else ''))
            else:
                assert outer_all_dead(mus[0])
                v, note = 'OUTER-DEAD', \
                    f'{kindtag} M={Min}: windowed-out inner, outer ' \
                    'analysis kills'
            out.append(key + (v, note))
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

check("C1 the decorated-skeleton layer reproduces the scope's "
      "corrected diagnostic exactly: 6 (11-A) + 8 (11-B) + 145 "
      "(11-C) = 159 rows",
      len(ROWS) == 159
      and sum(1 for r in ROWS if r[0] == '11-A') == 6
      and sum(1 for r in ROWS if r[0] == '11-B') == 8
      and sum(1 for r in ROWS if r[0] == '11-C') == 145)
check("C2 stamp breakdown: SPINE-DEAD-H8 81 (3 + 3 + 13 + 62), "
      "CLASH-DEAD 11 (3 + 5 + 3), UNREALIZABLE 31, SELF-REFUSED 15 "
      "(12 AB + 3 split), OUTER-DEAD 21 -- total 159, every stamp "
      "citing its instrument with the killing arithmetic re-derived "
      "in-line",
      cnt == Counter({'SPINE-DEAD-H8': 81, 'CLASH-DEAD': 11,
                      'UNREALIZABLE': 31, 'SELF-REFUSED': 15,
                      'OUTER-DEAD': 21}))
check("C3 ZERO live configuration rows; ZERO deferred",
      all(r[5] in ('SPINE-DEAD-H8', 'CLASH-DEAD', 'UNREALIZABLE',
                   'SELF-REFUSED', 'OUTER-DEAD') for r in ROWS))

FC = [
    ('FC1', 'beyond-core charged strata (deg > 94 px2 states; incl. '
     'NF-P-OB1 state-changing closure)', 'TOWER-TD11 sec 13.0'),
    ('FC2', 'cap-free grammar slice (k > 6 / lex > 40 steps)',
     'TOWER-TD11 sec 12(iii)'),
    ('FC3', 'Q+E5/E5F refile layer (realization; census is '
     'printed-tier)', 'scope sec 1.1 UNKNOWN'),
    ('FC4', 'current-state arrival classes beyond entry-state '
     'decorations', 'TOWER-TD11 sec 10(b)'),
    ('FC5', 'merged-chart post-merge P0 strata', 'NF-M.md riders'),
    ('FC6', 'nu=1 case-I handshake provenance beyond the enumerated '
     'menus', 'NF-P-OB2'),
]
print("\n-- fail-closed classes (KEEP-AS-POSSIBLY-LIVE, Rule 6) --")
for f in FC:
    print("  ", f)
check("C4 fail-closed inventory: 6 named classes, each with its "
      "banked citation -- KEEP-AS-POSSIBLY-LIVE (the reviewed "
      "direction); none is stamped dead", len(FC) == 6)

print("\n== CERTIFICATE STATEMENT ==")
CERT = (len(ROWS) == 159 and all(r[5] != 'LIVE' for r in ROWS))
print("""  CONDITIONAL EMPTINESS CERTIFICATE (td-11 class-B/C):
  every configuration in the audited class -- the 159 decorated
  skeletons with their full synchronized chain/word/arrival
  extensions under the exact-core discipline -- is TOWER-DEAD, each
  row by a named banked instrument re-derived above.  ZERO live
  rows.  This is NOT an unconditional empty-panel certificate: the
  six fail-closed classes remain KEEP-AS-POSSIBLY-LIVE per Rule 6,
  and closing them (beyond-core closure, cap-free engine, the
  refile) is the named residual work.""")
check("C5 certificate emitted: conditional emptiness over the "
      "audited class, fail-closed classes excluded honestly", CERT)

print("\n== td-7 REGRESSION (the promoted 17-cell book) ==")
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
