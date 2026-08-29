#!/usr/bin/env python3
"""Two-pole (3,3) td=6 configuration engine (SHEET6-2POLE.md).

Model (doc secs 1c, 2b, 4): two row-1 pole chains descend to a unique meet
G_m (interior, in V_{2,a}) or meet at (0,y) (root merge). Corrected Prop
8.4's M=1 kill is OFF above the meet and applies only at certified nonroot
vertices at/below an interior meet. The budget screen is conditional on the
currently accepted Section 7 weighted budget / first-separation ledger over the
UNION of the chains: lam1 + lam2 + lam_merge + lam_suffix <= 4 (psi=1);
psi-upgrades at terminals (h3_check dispositions / psi-at-root).

Shape space: Q mod the unit = (rho, nu, M, kap); the merge equations are
P-free given (mu_1, mu_2) [doc 5a]: i-consistency P_1/mu_1 = P_2/mu_2
makes every child datum a shape function. P-realizability of a pair is NOT
tracked (conservative: survivor-friendly; any surviving witness must then
be checked for realizable absolute degrees).

Phases:
  1 premerge : shape BFS from Q=(1,2,2,5), M in {2,1}, M=1 kill OFF;
               mu=1 IIa_0 children added (only mu=1 shape, doc 4c.1);
               the common engine supplies root-capable mu=2 I, while this
               engine adds certified-nonroot mu=2 IIb/III; parametric families
               are kept, and merged phases use instances s <= SMAX.
  2 merge    : merged-pattern solve (doc 4a, hyp M-PAT) over instance
               pairs; certified-nonroot child M=1 => KILLED; N1; else
               single-pole suffix BFS (hiii_compose.step_e5, kills ON).
  3 rootmerge: merged terminal at (0,y), including l>=1, needs kap < nu
               on both parents; psi-at-root; root ODE status recorded.

Caps: SMAX instances of parametric shapes, DEPTH, KMAX, NUMAX as below.
Exact arithmetic (int/Fraction). ~run time: a few minutes.
"""
import os, sys, re
from fractions import Fraction as Fr
from math import gcd
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sheet6_campaign as sc
import hiii_compose as hx
import h3_check as hc

sc.IIB_DERIVED = True   # SHEET6-A2P-REVIEW fix (1): derived IIb pricing is the default here


Node, LF = sc.Node, sc.LF
SMAX, DEPTH, KMAX, NUMAX = 5, 6, 4, 48
SMULT_MAX = 12                    # diagnostic merge multiplicity-sum cap
NU1MAX, L1MAX = 24, 4           # mu=1 IIa_0 child caps
L1_MERGE_LMAX = 8               # diagnostic only; zero-charge l has no bound
BUDGET = 4                      # td-1-psi with psi=1 (Thm 6.1)

def ceil_fr(x):
    x = Fr(x); return -((-x.numerator) // x.denominator)

def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

# --------------------------------------------------------------- phase 1
def mu1_children(node):
    """mu=1 IIa_0-like (doc 4c.1): dp=nu_F, dq=(l+1)nu_F+1, lam=0, M_F=1,
    kap_F=(kap+n)/nu_G, rho_F=(rho+n)/(nu_G nu_F)  [P_F = P_G nu_F].
    Concrete nodes only (parametric callers instantiate first)."""
    rho, (na, nb), (ka, kb) = node.rho, LF(node.nu), LF(node.kap)
    assert na == 0 and ka == 0
    nu, kap = nb, kb
    out = []
    for nuF in range(2, NU1MAX + 1):
        for l in range(0, L1MAX + 1):
            dp, dq = nuF, (l + 1) * nuF + 1
            n = (Fr(dp) * kap - Fr(dq) * rho) / (dq - dp)
            if n.denominator != 1 or n < 1: continue
            n = int(n)
            if (n + kap) % nu: continue
            kapF = (kap + n) // nu
            rhoF = Fr(rho + n, nu * nuF)
            ch = Node(rhoF, nuF, 1, kapF, dp, tag="<-mu1IIa0")
            out.append(('CONT', 0, ch, f"mu=1 IIa_0 l={l} n={n} -> {ch} lam>=0"))
    # This branch costs no lambda, so neither cap is a completeness bound.
    out.append(('OPEN',
                f"mu=1 IIa_0 premerge tail nuF>{NU1MAX} or l>{L1MAX}: "
                f"NO_VERDICT at {node}", 0))
    return out

def step_twopole(node):
    """Pre-merge step: sc.step CONT/OPEN outcomes (M=1 children KEPT),
    plus the certified-nonroot mu=2 IIb/III children (M_F=1), plus mu=1
    IIa_0 children. sc.step itself now retains the root-capable mu=2 I path."""
    out = [o for o in sc.step(node) if o[0] in ('CONT', 'OPEN')]
    for mu in sc.divisors_gt1(node.M):
        if mu == 2:                       # certified nonroot: nu_F >= 2
            for br in ('IIb', 'III'):
                out.extend(o for o in sc.step_one_branch(node, mu, br)
                           if o[0] in ('CONT', 'OPEN'))
    na, ka = LF(node.nu)[0], LF(node.kap)[0]
    if na == 0 and ka == 0:
        out.extend(mu1_children(node))
    else:
        for s in range(0, SMAX + 1):
            out.extend(mu1_children(sc.instantiate(node, s)))
        out.append(('OPEN', f"mu=1 premerge parametric instances s>{SMAX}: "
                    f"NO_VERDICT at {node}", 0))
    return out

def premerge():
    """Reachable pre-merge shapes with min lambda (M=1 kill OFF)."""
    seen, opens = {}, []
    dq_ = deque()
    for M in (2, 1):
        nd = Node(Fr(1), 2, M, 5, 2)
        if nd.shape() not in seen:
            seen[nd.shape()] = (0, 0, f"ENTRY M={M}", nd)
            dq_.append((nd, 0, 0))
    while dq_:
        node, lam, dep = dq_.popleft()
        if dep >= DEPTH:
            opens.append((lam, f"NO_VERDICT premerge depth>{DEPTH} at {node}"))
            continue
        for o in step_twopole(node):
            if o[0] == 'OPEN':
                lmin = o[2] if len(o) > 2 else 0
                if lam + lmin <= BUDGET: opens.append((lam, o[1][:90]))
                continue
            _, dl, ch, why = o
            nl = lam + dl
            if nl > BUDGET: continue
            sh = ch.shape()
            if sh in seen and seen[sh][0] <= nl: continue
            seen[sh] = (nl, dep + 1, why, ch)
            dq_.append((ch, nl, dep + 1))
    return seen, opens

def instances(seen):
    """Concrete instances (s <= SMAX) of the reachable shapes:
    [(rho, nu, M, kap, lam, label)]."""
    out, dedup = [], set()
    for sh, (lam, dep, why, nd) in seen.items():
        na, ka = LF(nd.nu)[0], LF(nd.kap)[0]
        svals = range(0, SMAX + 1) if (na or ka) else (0,)
        for s in svals:
            c = sc.instantiate(nd, s)
            key = (c.rho, LF(c.nu)[1], c.M, LF(c.kap)[1])
            if key in dedup: continue
            dedup.add(key)
            out.append((c.rho, LF(c.nu)[1], c.M, LF(c.kap)[1], lam,
                        f"{sh}@s={s}" if (na or ka) else str(sh)))
    return out

# --------------------------------------------------------------- phase 2
def edge_n(rho, nu, M, kap, mu, r):
    """mu(rho+n)/(kap+n) = r; n>=1, n == -kap mod nu; else None."""
    if Fr(mu) == r: return None
    n = (r * kap - mu * rho) / (mu - r)
    if n.denominator != 1 or n < 1: return None
    n = int(n)
    if (n + kap) % nu: return None
    return n

def merge_shapes_S(S):
    """(branch, nu_child, k, dp, dq) per doc 4a (hyp M-PAT) for total
    searrow multiplicity S = mu1 + mu2. The IIa shape carries the resonant
    q-orbit family l >= 0 (single-pole IIa_0 analogue; allowed for all k =
    conservative over-generation)."""
    for k in range(0, KMAX + 1):
        yield ('I', 1, k, S + k, k + 2)
        for nu in range(2, NUMAX + 1):
            for l in range(0, L1MAX + 1):
                yield (f'IIa(l={l})', nu, k, (S + k) * nu, (k + l + 2) * nu + 1)
            yield ('IIb', nu, k, (S + k) * nu + 1, (k + 2) * nu + 1)
            yield ('III', nu, k, S + k * nu, 2 + k * nu)

def all_merges(insts):
    """All merge children over instance pairs, factorized: per merge shape,
    solve each (parent, mu) edge ONCE, join edges on (kap_m, D/i0).
    P-free; i-consistency absorbed into mu-choice (P_1/P_2 = mu_1/mu_2,
    realizability not tracked: conservative).
    Yields (a_idx, b_idx, lam_merge, child Node, why)."""
    for S in range(2, SMULT_MAX + 1):
        for br, nu, k, dp, dq in merge_shapes_S(S):
            r = Fr(dp, dq)
            if k > 0 and not dq < dp: continue                  # NE extras
            bucket = {}
            for idx, (rho, nug, M, kapg, lam, lab) in enumerate(insts):
                for mu in divisors(M):
                    if mu >= S: continue
                    if not mu * dq > dp: continue               # searrow
                    n = edge_n(rho, nug, M, kapg, mu, r)
                    if n is None: continue
                    kap_m = Fr(kapg + n, nug)
                    if kap_m.denominator != 1: continue
                    Di = Fr(mu) * (rho + n) / nug
                    bucket.setdefault((kap_m, Di), []).append((idx, mu, n))
            for (kap_m, Di), edges in bucket.items():
                kap_m = int(kap_m)
                gap = Di - kap_m
                lam_m = k * max(1, ceil_fr(gap)) if k else 0
                rho_m = Di / dp
                M_m = gcd(dp, dq)
                for x in range(len(edges)):
                    for y in range(x, len(edges)):
                        ia, mua, na = edges[x]
                        ib, mub, nb = edges[y]
                        if mua + mub != S: continue
                        ch = Node(rho_m, nu, M_m, kap_m, dp, tag="<-MERGE")
                        yield (ia, ib, lam_m, ch,
                               f"{br} mu=({mua},{mub}) k={k} nu={nu} "
                               f"n=({na},{nb}) dp/dq={dp}/{dq}")

def suffix_bash(ch, lam0, td=6, *, certified_nonroot):
    """Single-pole suffix from a merge child.

    ``certified_nonroot`` is mandatory: an interior meet passes True; a root
    candidate passes False and is recorded before any M-filter.
    """
    disposition = sc.dispose_m1(ch, certified_nonroot=certified_nonroot)
    if disposition in (sc.TERMINAL_ROOT_M1, sc.TERMINAL_ROOT_M_GT1):
        return dict(verdict='RESIDUE', iv=[], open=[],
                    sf1=[(lam0, str(ch), disposition)], frontier=0)
    if disposition == sc.KILL_NR_M1:
        return dict(verdict='KILLED(NR-M1 at certified nonroot merge)')
    if disposition == sc.UNRESOLVED_M1_SCOPE:
        return dict(verdict='RESIDUE', iv=[], open=[],
                    sf1=[(lam0, str(ch), disposition)], frontier=0)
    assert disposition == sc.KEEP
    nu0, kap0 = LF(ch.nu)[1], LF(ch.kap)[1]
    if LF(ch.nu)[0] == 0 and nu0 >= 2 and gcd(nu0, kap0) > 1:
        return dict(verdict='KILLED(N1)')
    seen = {ch.shape(): lam0}
    dq_ = deque([(ch, lam0, 0, [])])
    ivs, opens, sf1, frontier = [], [], [], 0
    while dq_:
        nd, lam, dep, tr = dq_.popleft()
        if dep >= DEPTH:
            frontier += 1; continue
        for o in hx.step_e5(nd):
            if o[0] == 'TERMINAL_IV':
                rows, _ = hc.iv_dispositions(nd, lam, td)
                if any(v == 'OPEN_s_tail' for _, v, _ in rows):
                    opens.append((lam, f"IV parametric s>{hc.SMAX}: "
                                  f"NO_VERDICT at {nd}"))
                surv = [(s, R) for s, v, R in rows if v == 'SURVIVOR']
                if surv: ivs.append((nd.shape(), lam, surv[:2], tr))
            elif o[0] == 'OPEN_E5U':
                _, msg, lmin, mu = o
                if lam + lmin > BUDGET: continue
                if sc.budget_kill_all_s(nd, mu, BUDGET - lam): continue
                opens.append((lam, msg[:80]))
            elif o[0] == 'OPEN':
                lmin = o[2] if len(o) > 2 else 0
                if lam + lmin > BUDGET: continue
                opens.append((lam, o[1][:80]))
            elif o[0] == 'CONT':
                _, dl, c2, why = o
                nl = lam + dl
                if nl > BUDGET: continue
                disposition = sc.dispose_constructed_child(c2)
                if disposition in (sc.TERMINAL_ROOT_M1,
                                   sc.TERMINAL_ROOT_M_GT1):
                    sf1.append((nl, why[:70], disposition))
                    continue
                if disposition == sc.KILL_NR_M1:
                    continue
                assert disposition == sc.KEEP
                sh = c2.shape()
                if sh in seen and seen[sh] <= nl: continue
                seen[sh] = nl
                dq_.append((c2, nl, dep + 1, tr + [why[:100]]))
    v = 'DEAD' if not (ivs or opens or sf1 or frontier) else 'RESIDUE'
    return dict(verdict=v, iv=ivs, open=opens, sf1=sf1, frontier=frontier)

# --------------------------------------------------------------- phase 3
def root_pattern_menu(mu1, mu2, *, kmax=KMAX, lmax=L1MAX):
    """Root pattern menu, generated before any parent-reach test.

    The old menu fixed l=0. The l>=1 family has
    ``dp=mu1+mu2+k, dq=k+2+l``. For the all-mu=1, k=0 family, even l is
    logarithmically obstructed while odd l has no such obstruction; l=1 is
    the exact locally solvable ``(dp,dq)=(2,3)`` cell.

    For the td=6 phase-3 budget screen, ``ratio_kl=dq``, hence
    ``psi=dq-1=k+l+1``. Nonnegative lambda and ``tot<=5-psi`` force
    ``k+l<=4``, so KMAX=L1MAX=4 is complete for budget-consistent td=6
    phase-3 hits. Outside that conditional screen, lmax is diagnostic only.
    """
    for k in range(0, kmax + 1):
        for l in range(0, lmax + 1):
            dp, dq = mu1 + mu2 + k, k + 2 + l
            if mu1 == mu2 == 1 and k == 0 and l >= 1:
                ode = ('ROOT_ODE_LOG_DEAD_EVEN' if l % 2 == 0 else
                       'ROOT_ODE_EXACT_SOLVABLE_L1' if l == 1 else
                       'ROOT_ODE_NO_LOG_OBSTRUCTION_ODD')
            else:
                ode = 'ROOT_ODE_UNCHECKED'
            yield k, l, dp, dq, ode


def root_parent_reachable(parent):
    """Prop. 9.3(d) reach test for a child with (nu,kap)=(1,1)."""
    return parent[3] < parent[1]


def root_merges(insts):
    """Merged terminal at (0,y), including the formerly omitted l-family.

    Each pattern is generated before Proposition 9.3(d)'s parent test
    ``kap_i < nu_i``. P-free: k_f/l_f = dp/(D/i0); psi-at-root; budget
    lam1+lam2+lam_extras <= 5-psi. Returns tuples ending in
    ``(budget_ok, root_ode_status)``.
    """
    hits = []
    for a in range(len(insts)):
        for b in range(a, len(insts)):
            pa, pb = insts[a], insts[b]
            r1, nu1, M1, k1_, la, lab1 = pa
            r2, nu2, M2, k2_, lb, lab2 = pb
            for mu1 in divisors(M1):
                for mu2 in divisors(M2):
                    for k, l, dp, dq, ode in root_pattern_menu(mu1, mu2):
                        # The l-family is present before this reach gate. In
                        # particular (mu1,mu2,l)=(1,1,1) reaches this line.
                        if not (root_parent_reachable(pa) and
                                root_parent_reachable(pb)):
                            continue
                        na, nb = nu1 - k1_, nu2 - k2_
                        if not (mu1 * dq > dp and mu2 * dq > dp): continue
                        if k > 0 and not dq < dp: continue
                        r = Fr(dp, dq)
                        if Fr(mu1) * (r1 + na) / (k1_ + na) != r: continue
                        if Fr(mu2) * (r2 + nb) / (k2_ + nb) != r: continue
                        Di_a = Fr(mu1) * (r1 + na) / nu1     # = l_f/i0
                        Di_b = Fr(mu2) * (r2 + nb) / nu2
                        if Di_a != Di_b: continue
                        ratio_kl = Fr(dp) / Di_a             # k_f/l_f
                        assert ratio_kl == dq, "root identity k_f/l_f=deg(q)"
                        if ratio_kl <= 1: continue           # Thm 6.1
                        psi = ceil_fr(ratio_kl) - 1
                        gap = Di_a - 1
                        lam_r = k * max(1, ceil_fr(gap)) if k else 0
                        tot = la + lb + lam_r
                        # Conditional Section 7 budget: sum lam<=td-1-psi.
                        ok = tot <= 5 - psi
                        hits.append((pa, pb, mu1, mu2, k, l, ratio_kl,
                                     Di_a, tot, psi, ok, ode))
    return hits

# ------------------------------------------------ phase 4: L1 stage (new)
def l1_premerge(*, with_no_verdict=False):
    """Printed-forced pre-merge tree (SHEET6-L1.md L1a): entry M = 1
    [M_pole = gcd(deg p, deg p_g) = gcd(2,3) = 1: Not 8.1 + Prop 5.1(i)
    (m=0 at poles) + table (23) row 1]; every pre-merge step is the thesis's
    own mult(p,c)=1 case (St 9.6 proof, p. 52): p = single simple nu-orbit,
    deg q = n*nu+1, M_child = 1, lam = 0 (no NE root can exist: dq > dp)."""
    def zch_children(node):
        """Chain-at-0 mu=1 child: p = eta (dp=1, nu_F=1), q = eta*s,
        dq = 1+l, M=1; same (d)-form edge equation. The l-menu is solved
        exactly through sc.solve_mu1_exact, not truncated at L1MAX."""
        rho, nu, kap = node.rho, LF(node.nu)[1], LF(node.kap)[1]
        out = []
        red = sc.reduce_ratio(rho, nu, kap, 1, 'II')
        if red is None:
            return [('OPEN', f"mu=1 zch reduction unavailable: NO_VERDICT at {node}", 0)]
        pts, fams, cert = sc.solve_mu1_exact(red)
        for fam in fams:
            out.append(('OPEN', f"mu=1 zch degenerate {fam}: NO_VERDICT at {node}", 0))
        for kl, nuF, m in pts:
            assert nuF == 1
            l = kl + 1                    # MU1 dq=kl+2 = 1+l
            n = LF(red['n0'])[1] + nu * m
            assert n >= 1 and (n + kap) % nu == 0
            assert edge_n(rho, nu, 1, kap, 1, Fr(1, 1 + l)) == n
            ch = Node((rho + n) / nu, 1, 1, (kap + n) // nu, 1, tag="<-mu1z")
            out.append(('CONT', 0, ch, f"mu=1 zch l={l} n={n}"))
        return out
    seen, no_verdict, dq_ = {}, [], deque()
    nd = Node(Fr(1), 2, 1, 5, 2)
    seen[nd.shape()] = (0, "ENTRY M=1 (printed)", nd)
    dq_.append((nd, 0))
    while dq_:
        node, dep = dq_.popleft()
        if dep >= DEPTH:
            no_verdict.append(f"zero-charge L1 depth>{DEPTH} at {node}")
            continue
        for outcome in mu1_children(node) + zch_children(node):
            if outcome[0] == 'OPEN':
                no_verdict.append(outcome[1])
                continue
            _, dl, ch, why = outcome
            sh = ch.shape()
            if sh in seen: continue
            seen[sh] = (dep + 1, why, ch)
            dq_.append((ch, dep + 1))
    return (seen, no_verdict) if with_no_verdict else seen

def l1_merges(insts, LMAX=L1_MERGE_LMAX):
    """mu=(1,1), k=0 merged menu (all that survives L1a):
      nu>=2: dp=2nu, dq=(l+2)nu+1    [IIa(l), both chains at nonzero orbits;
             an eta EXTRA in p excluded: third searrow branch -> third pole
             via Prop 6.8]
      nu>=2: dp=nu+1, dq=(l+1)nu+1   [ZCH(l): one CHAIN at the 0-direction,
             p = eta(eta^nu - c^nu); l=0 impossible (rho=1 kills 8.1(iv));
             M = gcd(nu+1, l)]
      nu=1 : dp=2, dq=2+l            [I(l); coefficient-IMPOSSIBLE by the
             nonroot Prop 8.1(iv) Wronskian/log analysis. At the root, even
             l is log-obstructed while odd l reaches the parent filter; l=1
             is locally solvable]
    """
    menu = [(1, 1, l, 2, 2 + l) for l in range(1, LMAX + 1)]
    for nu in range(2, NUMAX + 1):
        for l in range(0, LMAX + 1):
            menu.append((0, nu, l, 2 * nu, (l + 2) * nu + 1))
        for l in range(1, LMAX + 1):
            menu.append((2, nu, l, nu + 1, (l + 1) * nu + 1))
    for is1, nu, l, dp, dq in menu:
        if not dq > dp: continue                    # searrow, mu=1
        r = Fr(dp, dq)
        bucket = {}
        for idx, (rho, nug, M, kapg, lam, lab) in enumerate(insts):
            n = edge_n(rho, nug, M, kapg, 1, r)
            if n is None: continue
            kap_m = Fr(kapg + n, nug)
            if kap_m.denominator != 1: continue
            Di = (rho + n) / nug
            bucket.setdefault((kap_m, Di), []).append((idx, n))
        for (kap_m, Di), edges in bucket.items():
            for x in range(len(edges)):
                for y in range(x, len(edges)):
                    ia, na = edges[x]
                    ib, nb = edges[y]
                    ch = Node(Di / dp, nu, gcd(dp, dq), int(kap_m), dp,
                              tag="<-L1MERGE")
                    br = {1: 'I', 0: 'IIa', 2: 'ZCH'}[is1]
                    yield (ia, ib, ch, is1, l,
                           f"{br}(l={l}) nu={nu} "
                           f"n=({na},{nb}) dp/dq={dp}/{dq}")

def l1_stage():
    print("\n== PHASE 4 (L1 stage): printed-forced M=1 chains, mu=(1,1) ==")
    seen, premerge_no_verdict = l1_premerge(with_no_verdict=True)
    print(f"pre-merge shapes (all M=1, lam=0): {len(seen)}")
    print(f"pre-merge NO_VERDICT cap/tail kinds: {len(set(premerge_no_verdict))}")
    insts = [(nd.rho, LF(nd.nu)[1], 1, LF(nd.kap)[1], 0, str(sh))
             for sh, (dep, why, nd) in seen.items()]
    tried = killed_m1 = nonroot_ode_dead = root_ode_dead = root_candidates = 0
    res, kills = {}, {}
    sfx = {}
    for ia, ib, ch, is1, l, why in l1_merges(insts):
        tried += 1
        disposition = sc.dispose_constructed_child(ch)
        if disposition in (sc.TERMINAL_ROOT_M1, sc.TERMINAL_ROOT_M_GT1):
            # Root ODE is not the nonroot L1b calculation: even l has the
            # logarithmic obstruction, while odd l (especially l=1) remains
            # a genuine terminal candidate after the already-applied parent
            # edge/reach equations in l1_merges.
            if l % 2 == 0:
                root_ode_dead += 1
                res.setdefault(('ROOT-ODE-DEAD-EVEN', str(ch.shape())), []).append(
                    (insts[ia][5], insts[ib][5], why, disposition))
            else:
                root_candidates += 1
                status = ('ROOT-EXACT-SOLVABLE-L1' if l == 1 else
                          'ROOT-ODD-NO-LOG-OBSTRUCTION')
                res.setdefault((status, str(ch.shape())), []).append(
                    (insts[ia][5], insts[ib][5], why, disposition))
            continue
        if disposition == sc.KILL_NR_M1:
            killed_m1 += 1
            continue
        assert disposition == sc.KEEP
        if is1 == 1:
            nonroot_ode_dead += 1
            res.setdefault(('NU1-NONROOT-ODE-DEAD', str(ch.shape())), []).append(
                (insts[ia][5], insts[ib][5], why))
            continue
        key = (str(ch.shape()), 0)
        if key not in sfx:
            sfx[key] = suffix_bash(ch, 0, certified_nonroot=True)
        r = sfx[key]
        if r['verdict'].startswith('KILLED') or r['verdict'] == 'DEAD':
            kills[r['verdict']] = kills.get(r['verdict'], 0) + 1
        else:
            res.setdefault(('RESIDUE', str(ch.shape())), []).append(
                (insts[ia][5], insts[ib][5], why, r))
    # l and nu carry no automatic charge in parts of this merge menu. The
    # finite display is diagnostic outside a separately proved budget bound.
    res.setdefault(('NO_VERDICT-L1-MERGE-CAPS',
                    f"nu>{NUMAX} or l>{L1_MERGE_LMAX} unenumerated"), [])
    if premerge_no_verdict:
        res.setdefault(('NO_VERDICT-L1-PREMERGE-TAILS',
                        f"{len(set(premerge_no_verdict))} distinct tails"), [])
    print(f"merge children: {tried}; nonroot M=1 killed: {killed_m1}; "
          f"nu=1 nonroot ODE-dead: {nonroot_ode_dead}; "
          f"root even-l ODE-dead: {root_ode_dead}; "
          f"root odd-l candidates: {root_candidates}")
    for v, c in sorted(kills.items(), key=lambda x: -x[1]):
        print(f"    suffix kill: {v} x{c}")
    for (kind, shp), items in sorted(res.items()):
        print(f"  {kind} child={shp} ({len(items)} parent pairs)")
        for it in items[:3]:
            print(f"    parents {it[0]} + {it[1]} via {it[2]}")
        if kind == 'RESIDUE':
            r = items[0][3]
            ivded = {}
            for sh, lam, surv, tr in r.get('iv', []):
                ivded.setdefault((str(sh), lam), surv)
            for (sh, lam), surv in sorted(ivded.items(), key=lambda x: x[0][1]):
                print(f"      IVSURV lam={lam} {sh} (s,R)={surv}")
            for kind2 in ('open', 'sf1'):
                for item in r.get(kind2, [])[:3]:
                    print(f"      {kind2}: {item}")
    return res

if __name__ == "__main__" and 'l1only' in sys.argv:
    l1_stage()
    sys.exit(0)

# ------------------------------------------------------------------ main
if __name__ == "__main__":
    print("== PHASE 1: pre-merge reachable shapes (M=1 kill OFF) ==")
    seen, opens = premerge()
    print(f"shapes: {len(seen)} (caps: depth<={DEPTH}, lam<={BUDGET}, "
          f"mu1 nuF<={NU1MAX}, l<={L1MAX})")
    bylam = {}
    for sh, (lam, dep, why, nd) in seen.items():
        bylam.setdefault(lam, []).append((sh, dep, why))
    for lam in sorted(bylam):
        print(f"  lam={lam}: {len(bylam[lam])} shapes")
        for sh, dep, why in sorted(bylam[lam], key=str)[:14]:
            print(f"    {sh} dep={dep} <- {why[:76]}")
    om = {}
    for lam, msg in opens:
        om.setdefault(msg, []).append(lam)
    print(f"  OPEN pre-merge branches (distinct): {len(om)}")
    for msg, lams in sorted(om.items()):
        print(f"    minlam={min(lams)} x{len(lams)} {msg[:90]}")

    insts = instances(seen)
    print(f"\ninstances for merge phases: {len(insts)}")
    if any(LF(nd.nu)[0] or LF(nd.kap)[0]
           for _, (_, _, _, nd) in seen.items()):
        print(f"  NO_VERDICT: parametric premerge instances s>{SMAX} "
              "are not represented in the finite merge join")

    print("\n== PHASE 2: interior merges + suffix ==")
    print(f"  NO_VERDICT rider: general zero-charge merge tails beyond "
          f"S>{SMULT_MAX}, nu>{NUMAX}, or l>{L1MAX} are unenumerated; "
          "this phase is a capped diagnostic")
    tried = mdead = mres = 0
    residues, kills = [], {}
    sfx_cache = {}
    for ia, ib, lam_m, ch, why in all_merges(insts):
        la, lb = insts[ia][4], insts[ib][4]
        tot = la + lb + lam_m
        if tot > BUDGET: continue
        tried += 1
        ckey = (ch.shape(), tot)
        if ckey not in sfx_cache:
            sfx_cache[ckey] = suffix_bash(ch, tot, certified_nonroot=True)
        r = sfx_cache[ckey]
        v = r['verdict']
        if v.startswith('KILLED') or v == 'DEAD':
            mdead += 1
            kills[v] = kills.get(v, 0) + 1
        else:
            mres += 1
            residues.append((tot, insts[ia], insts[ib], why, ch, r))
    print(f"merge children solved: {tried}; dead: {mdead}; residue: {mres}; "
          f"distinct (child,lam): {len(sfx_cache)}")
    for v, c in sorted(kills.items(), key=lambda x: -x[1]):
        print(f"    kill kind: {v}  x{c}")
    kd = {}
    for tot, pa, pb, why, ch, r in residues:
        kd.setdefault((str(ch.shape()), tot), (pa, pb, why, r))
    print(f"distinct residue (shape,lam) classes: {len(kd)}")
    for (shp, tot), (pa, pb, why, r) in sorted(kd.items(), key=lambda x: x[0][1]):
        print(f"  RESIDUE lam={tot} child={shp} via {why}")
        print(f"    parents {pa[5]}(lam{pa[4]}) + {pb[5]}(lam{pb[4]})")
        ivded = {}
        for sh, lam, surv, tr in r.get('iv', []):
            ivded.setdefault((str(sh), lam), (surv, tr))
        for (sh, lam), (surv, tr) in sorted(ivded.items(), key=lambda x: x[0][1]):
            print(f"      IVSURV lam={lam} {sh} (s,R)={surv}")
            for t in tr: print(f"        | {t}")
        for kind in ('open', 'sf1'):
            for item in r.get(kind, [])[:4]:
                print(f"      {kind}: {item}")
        if r.get('frontier'): print(f"      frontier={r['frontier']}")

    print("\n== PHASE 3: root merges ==")
    hits = root_merges(insts)
    ok = [h for h in hits if h[10] and h[11] != 'ROOT_ODE_LOG_DEAD_EVEN']
    ode_dead = sum(1 for h in hits if h[11] == 'ROOT_ODE_LOG_DEAD_EVEN')
    print(f"root-merge solutions after parent reach within "
          f"k<={KMAX}, l<={L1MAX}: {len(hits)}; "
          f"ODE-dead-even: {ode_dead}; budget/ODE-consistent: {len(ok)}")
    seenh = set()
    for h in sorted(ok, key=lambda x: x[8]):
        pa, pb, mu1, mu2, k, l, rkl, Di, tot, psi, _, ode = h
        key = (pa[5], pb[5], mu1, mu2, k, l)
        if key in seenh: continue
        seenh.add(key)
        print(f"  ROOT lam={tot} psi={psi} k_f/l_f={rkl} l_f=i0*{Di} "
              f"mu=({mu1},{mu2}) k={k} l={l} ode={ode}")
        print(f"    parents {pa[5]}(lam{pa[4]}) + {pb[5]}(lam{pb[4]})")
    ndead = [h for h in hits if not h[10]]
    print(f"root-merge budget-dead (conditional on Section 7 budget): {len(ndead)}")
    for h in sorted(ndead, key=lambda x: x[8])[:6]:
        pa, pb, mu1, mu2, k, l, rkl, Di, tot, psi, _, ode = h
        print(f"  root-dead lam={tot} psi={psi} k_f/l_f={rkl} "
              f"k={k} l={l} ode={ode} parents {pa[5]} + {pb[5]}")

    l1_stage()
