#!/usr/bin/env python3
"""Two-pole (3,3) td=6 configuration engine (SHEET6-2POLE.md).

Model (doc secs 1c, 2b, 4): two row-1 pole chains descend to a unique meet
G_m (interior, in V_{2,a}) or meet at (0,y) (root merge). Prop 8.4's M=1
kill is OFF above the meet, RESTORED at/below it. Budget: St 9.4 over the
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
               mu=2 I/IIb/III (M_F=1) children added; parametric families
               kept, merged phases use instances s <= SMAX.
  2 merge    : merged-pattern solve (doc 4a, hyp M-PAT) over instance
               pairs; child M=1 => KILLED (restored 8.4); N1; else
               single-pole suffix BFS (hiii_compose.step_e5, kills ON).
  3 rootmerge: I-like merged terminal at (0,y), needs kap < nu both edges;
               psi-at-root; type-(2,3) side conditions noted.

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
NU1MAX, L1MAX = 24, 4           # mu=1 IIa_0 child caps
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
    return out

def step_twopole(node):
    """Pre-merge step: sc.step CONT/OPEN outcomes (M=1 children KEPT),
    plus mu=2 I/IIb/III children (M_F=1), plus mu=1 IIa_0 children."""
    out = [o for o in sc.step(node) if o[0] in ('CONT', 'OPEN')]
    for mu in sc.divisors_gt1(node.M):
        if mu == 2:                       # sc.step shortcuts these as KILL_M1
            for br in ('I', 'IIb', 'III'):
                out.extend(o for o in sc.step_one_branch(node, mu, br)
                           if o[0] in ('CONT', 'OPEN'))
    na, ka = LF(node.nu)[0], LF(node.kap)[0]
    if na == 0 and ka == 0:
        out.extend(mu1_children(node))
    else:
        for s in range(0, SMAX + 1):
            out.extend(mu1_children(sc.instantiate(node, s)))
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
        if dep >= DEPTH: continue
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
    for S in range(2, 13):
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

def suffix_bash(ch, lam0, td=6):
    """Single-pole suffix from merge child: ALL kills ON (composed
    engine semantics: E5 case III, N1, psi/H3q IV dispositions)."""
    if ch.M == 1:
        return dict(verdict='KILLED(M=1 at merge; restored Prop 8.4)')
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
                if nl > BUDGET or c2.M == 1: continue
                if LF(c2.nu) == (0, 1) and LF(c2.kap) == (0, 1):
                    sf1.append((nl, why[:70]))
                sh = c2.shape()
                if sh in seen and seen[sh] <= nl: continue
                seen[sh] = nl
                dq_.append((c2, nl, dep + 1, tr + [why[:100]]))
    v = 'DEAD' if not (ivs or opens or sf1 or frontier) else 'RESIDUE'
    return dict(verdict=v, iv=ivs, open=opens, sf1=sf1, frontier=frontier)

# --------------------------------------------------------------- phase 3
def root_merges(insts):
    """I-like merged terminal at (0,y): kap_i < nu_i, n_i = nu_i - kap_i,
    child (nu,kap) = (1,1). P-free: k_f/l_f = dp/(D/i0); psi-at-root;
    budget lam1+lam2+lam_extras <= 5 - psi. Type-(2,3) parity of (k_f,l_f)
    depends on i0 (recorded as condition, not tested)."""
    cand = [p for p in insts if p[3] < p[1]]
    hits = []
    for a in range(len(cand)):
        for b in range(a, len(cand)):
            r1, nu1, M1, k1_, la, lab1 = cand[a]
            r2, nu2, M2, k2_, lb, lab2 = cand[b]
            na, nb = nu1 - k1_, nu2 - k2_
            for mu1 in divisors(M1):
                for mu2 in divisors(M2):
                    for k in range(0, KMAX + 1):
                        dp, dq = mu1 + mu2 + k, k + 2
                        if not (mu1 * dq > dp and mu2 * dq > dp): continue
                        if k > 0 and not dq < dp: continue
                        r = Fr(dp, dq)
                        if Fr(mu1) * (r1 + na) / (k1_ + na) != r: continue
                        if Fr(mu2) * (r2 + nb) / (k2_ + nb) != r: continue
                        Di_a = Fr(mu1) * (r1 + na) / nu1     # = l_f/i0
                        Di_b = Fr(mu2) * (r2 + nb) / nu2
                        if Di_a != Di_b: continue
                        ratio_kl = Fr(dp) / Di_a             # k_f/l_f
                        if ratio_kl <= 1: continue           # Thm 6.1
                        psi = ceil_fr(ratio_kl) - 1
                        gap = Di_a - 1
                        lam_r = k * max(1, ceil_fr(gap)) if k else 0
                        tot = la + lb + lam_r
                        ok = tot <= 5 - 1 - psi if psi >= 1 else tot <= 4
                        # St 9.4: sum lam <= td-1-psi = 5-psi
                        ok = tot <= 5 - psi
                        hits.append((cand[a], cand[b], mu1, mu2, k,
                                     ratio_kl, Di_a, tot, psi, ok))
    return hits

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

    print("\n== PHASE 2: interior merges + suffix ==")
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
            sfx_cache[ckey] = suffix_bash(ch, tot)
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
    ok = [h for h in hits if h[9]]
    print(f"root-merge solutions: {len(hits)}; budget-consistent: {len(ok)}")
    seenh = set()
    for h in sorted(ok, key=lambda x: x[7]):
        pa, pb, mu1, mu2, k, rkl, Di, tot, psi, _ = h
        key = (pa[5], pb[5], mu1, mu2, k)
        if key in seenh: continue
        seenh.add(key)
        print(f"  ROOT lam={tot} psi={psi} k_f/l_f={rkl} l_f=i0*{Di} "
              f"mu=({mu1},{mu2}) k={k}")
        print(f"    parents {pa[5]}(lam{pa[4]}) + {pb[5]}(lam{pb[4]})")
    ndead = [h for h in hits if not h[9]]
    print(f"root-merge budget-dead: {len(ndead)}")
    for h in sorted(ndead, key=lambda x: x[7])[:6]:
        pa, pb, mu1, mu2, k, rkl, Di, tot, psi, _ = h
        print(f"  root-dead lam={tot} psi={psi} k_f/l_f={rkl} "
              f"parents {pa[5]} + {pb[5]}")
