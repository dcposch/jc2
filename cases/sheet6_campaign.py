#!/usr/bin/env python3
"""SHEET6 campaign driver: systematic td=6 case enumeration + bash (Sigray engine).

Builds on cases/sheet6_pilot.py (gated below). Extraction, hypotheses H1-H4, AF2-AF3
and the assembly reading (Prop 5.8 (20): td = sum of Lambda over pole vertices) are
documented in SHEET6-CAMPAIGN.md sec 0a-0c. Exact arithmetic only.

Node = Q(G) modulo the j-unit: (rho = D/P in Q, nu, M, kap = kappa(1-pi)); nu, kap
may be linear forms a*s+b (family parameter s >= 0). pcontent = integer content of
the deg(p_G) coefficient (mu must divide it: deg(p) = P/mu-scaled must be integral).

Step template (Prop 9.3 + root patterns of St 9.6-9.11 proofs; St 8.4 mu | M_G;
regularity => mu = max mult; i := deg(p_G)/mu):
  mu=1                  -> M_F = gcd(nu, n nu+1) = 1            KILL (Prop 8.4)
  case I   (nu_F=1)     : deg p = k+mu, deg q = k+1, k>=1; mu=2 -> M_F=1 KILL;
                          mu>=3: ratio eq RATIO_II, M_F = gcd(mu-1, k+1)
  case IIa (nu_F=nu>=2) : deg p = (k+mu)nu, deg q = (k+l+1)nu+1; k>0 => l=0 (St 8.2)
  case IIb              : deg p = (k+mu)nu+1, deg q = (k+1)nu+1; mu=2 -> M_F=1 KILL
  case III (nu_F=nu>=2) : deg p = mu+k nu, deg q = 1+k nu; k=0 -> M_F=1 KILL;
                          ratio eq RATIO_III; M_F = gcd(mu-1, 1+k nu)
  case IV  (terminal)   : possible iff kap < nu_G ((j)); killed iff H3
  RATIO_II : deg(p)/deg(q) = mu (rho+n)/(kap+n),   n = n0 + nu_G m  (n == -kap mod nu_G)
  RATIO_III: deg(p)/deg(q) = mu (rho+m)/(kap+m),   n = nu_F m  (from (h)-integrality)
  Q(F): kap_F = (kap+n)/nu_G [(d); III: kap+m], D_F/i = mu(rho+n)/nu_G [III: mu(rho+m)],
  rho_F = (D_F/i)/deg(p), M_F = gcd(deg p, deg q), pcontent_F = (pcontent/mu)*deg(p).
  lambda >= k * max(1, D_F/i - kap_F) over the k extra roots [AF2, reverse-engineered,
  matches all six thesis lemmas]; IIb adds root 0: lambda >= max(that, 1).
"""
import os, sys
from fractions import Fraction as Fr
from math import gcd
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sheet6_pilot import prop91, THESIS_TABLE, stmt96_knonzero, stmt96_k0

# ---------------------------------------------------------------- linear forms
def LF(x):    return x if isinstance(x, tuple) else (0, x)
def lf_eval(u, s):  u = LF(u); return u[0]*s + u[1]
def lf_is_const(u): return LF(u)[0] == 0
def lf_str(u):
    a, b = LF(u)
    if a == 0: return str(b)
    return f"{a}s{b:+d}" if b else f"{a}s"

def lf_mod_reduce(kap, nu):
    """n0 = (-kap) mod nu as linear form: n0 = -kap + q*nu with 0 <= n0(s) < nu(s)
    for all s >= 0 (coefficient conditions). Returns form or None."""
    ka, kb = LF(kap); na, nb = LF(nu)
    for q in range(-12, 13):
        a, b = -ka + q*na, -kb + q*nb
        if (a > 0 or (a == 0 and b >= 0)) and b >= 0 or (a > 0 and b >= 0):
            pass
        lo = (a >= 0 and b >= 0)                       # n0(s) >= 0 for all s>=0
        hi = (na - a >= 0 and nb - b > 0) or (na - a > 0 and nb - b >= 0)
        if lo and hi:
            return (a, b)
    return None

# ------------------------------------------------- s-free reduction of the ratio
def reduce_ratio(rho, nu_G, kap, mu, style):
    """style 'II': RHS = mu(rho+n)/(kap+n), n = n0 + nu_G*m, m >= 0 (n>=1 checked
    downstream via n0; if n0 == 0 identically, m >= 1). style 'III': RHS =
    mu(rho+m)/(kap+m), m >= 1. Returns dict with integer (a,b,c,e): RHS=(am+b)/(cm+e)
    s-free, m0, n0-form, or None if no s-free reduction (flag upstream).
    Soundness: 6x4-point PIT asserts the reduction identity."""
    if style == 'III':
        n0, nuG = (0, 0), (0, 1)
        m_lo = 1
    else:
        n0 = lf_mod_reduce(kap, nu_G)
        if n0 is None: return None
        nuG = LF(nu_G)
        m_lo = 1 if n0 == (0, 0) else 0
    L = rho.denominator
    A = (nuG[0]*mu*L, nuG[1]*mu*L)                     # num m-coeff (s-form)
    B = (n0[0]*mu*L, n0[1]*mu*L + mu*rho.numerator)    # num const
    C = (nuG[0]*L, nuG[1]*L)                           # den m-coeff
    ka, kb = LF(kap)
    E = ((ka + n0[0])*L, (kb + n0[1])*L)               # den const
    forms = [f for f in (A, B, C, E) if not lf_is_const(f)]
    if not forms:
        a, b, c, e = A[1], B[1], C[1], E[1]
    else:
        fa, fb = forms[0]; g = gcd(fa, fb); ca, cb = fa//g, fb//g
        def dv(f):
            fa2, fb2 = f
            if ca != 0 and fa2 % ca == 0 and (fa2//ca)*cb == fb2: return fa2//ca
            if ca == 0 and cb != 0 and fb2 % cb == 0 and fa2 == 0: return fb2//cb
            return None
        q = [dv(f) for f in (A, B, C, E)]
        if any(x is None for x in q): return None
        a, b, c, e = q
    g = gcd(gcd(abs(a), abs(b)), gcd(abs(c), abs(e))) or 1
    a, b, c, e = a//g, b//g, c//g, e//g
    if c*0 + e < 0 or (c < 0):                          # normalize signs
        a, b, c, e = -a, -b, -c, -e
    for s in range(0, 6):
        for m in range(m_lo, m_lo + 4):
            n = lf_eval(n0, s) + lf_eval(nuG, s)*m if style == 'II' else m
            num = Fr(mu) * (rho + n)
            den = lf_eval(kap, s) + n if style == 'II' else lf_eval(kap, s) + m
            assert num * (c*m + e) == Fr(a*m + b) * den, "reduction PIT failure"
    return dict(a=a, b=b, c=c, e=e, m0=m_lo, n0=n0, style=style)

# ------------------------------------------------------------ Diophantine solver
def solve_pattern(red, mu, branch, KMAX=48, NUSWEEP=1200, MSWEEP=1200):
    """Solve deg(p)*(c m+e) == deg(q)*(a m+b) over the branch shape:
      'IIa_k': dp=(k+mu)nu, dq=(k+1)nu+1, k>=1, nu>=2      (l=0 St 8.2)
      'IIa_0': dp=mu nu,    dq=(l+1)nu+1, l>=0, nu>=2      (k=0)
      'I'    : dp=k+mu,     dq=k+1,       k>=1, nu=1
      'IIb'  : dp=(k+mu)nu+1, dq=(k+1)nu+1, k>=0, nu>=2
      'III'  : dp=mu+k nu,  dq=1+k nu,    k>=1, nu>=2
    Returns (points [(kl,nu,m)], families [(kl,(dn,n1),(dm,m1),modulus-checked)],
    cert string). Completeness: per (kl,nu) exact m-solve; per (kl,m) exact nu-solve;
    families detected from the alpha1=0 congruence structure and slope==|Am| checked;
    kl-range certified via ratio-vs-1 monotone bound when derivable, else flagged."""
    a, b, c, e, m0 = red['a'], red['b'], red['c'], red['e'], red['m0']
    def degs(kl, nu):
        if branch == 'IIa_k': return (kl+mu)*nu, (kl+1)*nu + 1
        if branch == 'IIa_0': return mu*nu, (kl+1)*nu + 1
        if branch == 'I':     return kl+mu, kl+1
        if branch == 'IIb':   return (kl+mu)*nu + 1, (kl+1)*nu + 1
        if branch == 'III':   return mu + kl*nu, 1 + kl*nu
        raise ValueError(branch)
    lo = 0 if branch in ('IIa_0', 'IIb') else 1
    pts, fams, notes = [], [], []
    # kl-bound certificate: dp/dq > 1 always (mu>=2); dp/dq <= 1+(mu-1)/(kl+1)-type
    # => ratio(m) - 1 <= (mu-1)/(kl+1) ... derive klmax when ratio has positive gap:
    # ratio-1 = ((a-c)m + b-e)/(cm+e); if a<c: solutions need (a-c)m+b-e>0 => m-bound.
    mbound = None
    if a < c:
        mbound = (e - b) // (c - a) if (e - b) > 0 else m0 - 1
        notes.append(f"a<c => m <= {mbound} certified")
    elif a == c and b <= e:
        notes.append("a==c,b<=e => ratio<=1<LHS: NO solutions (certified)")
        return [], [], "; ".join(notes)
    nurange = (1, 1) if branch == 'I' else (2, NUSWEEP)
    for kl in range(lo, KMAX + 1):
        for nu in range(nurange[0], nurange[1] + 1):
            dp, dq = degs(kl, nu)
            Am, Bm = dp*c - dq*a, dq*b - dp*e
            if Am == 0:
                if Bm == 0: fams.append((branch, kl, nu, f"ALL m>={m0} degenerate"))
                continue
            if Bm % Am == 0:
                m = Bm // Am
                if m >= m0 and (mbound is None or m <= mbound):
                    assert dp*(c*m+e) == dq*(a*m+b)
                    pts.append((kl, nu, m))
        if branch != 'I':
            for m in range(m0, MSWEEP + 1):
                am, cm = a*m + b, c*m + e
                if branch == 'IIa_k':  D_, N_ = (kl+mu)*cm - (kl+1)*am, am
                elif branch == 'IIa_0': D_, N_ = mu*cm - (kl+1)*am, am
                elif branch == 'IIb':  D_, N_ = (kl+mu)*cm - (kl+1)*am, am - cm
                elif branch == 'III':  D_, N_ = kl*(cm - am), am - mu*cm
                if D_ != 0 and N_ % D_ == 0:
                    nu = N_ // D_
                    if nu >= 2 and (kl, nu, m) not in pts:
                        dp, dq = degs(kl, nu)
                        assert dp*cm == dq*am
                        pts.append((kl, nu, m))
    pts = sorted(set(pts))
    cert = (f"box kl<={KMAX},nu<={NUSWEEP},m<={MSWEEP}; exact per-cell m-solve + "
            f"per-(kl,m) nu-solve; " + "; ".join(notes))
    return pts, fams, cert

def detect_families(pts):
    """Collinear (nu,m)-progressions at fixed kl (>=3 points, all swept points on
    the line). Returns [(kl,(dn,n1),(dm,m1),count)] and the residual isolated pts."""
    from collections import defaultdict
    by_kl = defaultdict(list)
    for kl, nu, m in pts: by_kl[kl].append((nu, m))
    fams, iso = [], []
    for kl, lst in sorted(by_kl.items()):
        lst = sorted(set(lst))
        if len(lst) >= 3:
            (n1, m1), (n2, m2) = lst[0], lst[1]
            dn, dm = n2 - n1, m2 - m1
            on = all((n - n1)*dm == (m - m1)*dn and (dn == 0 or (n - n1) % dn == 0)
                     for n, m in lst)
            if on and (dn, dm) != (0, 0):
                fams.append((kl, (dn, n1), (dm, m1), len(lst)))
                continue
        iso.extend((kl, n, m) for n, m in lst)
    return fams, iso

# ------------------------------------------------------------------ node algebra
class Node:
    def __init__(self, rho, nu, M, kap, pcontent, tag=""):
        self.rho, self.nu, self.M, self.kap = Fr(rho), LF(nu), M, LF(kap)
        self.pc, self.tag = pcontent, tag
    def key(self): return (self.rho, self.nu, self.M, self.kap, self.pc)
    def shape(self): return (self.rho, self.nu, self.M, self.kap)
    def __repr__(self):
        return (f"Q[rho={self.rho},nu={lf_str(self.nu)},M={self.M},"
                f"kap={lf_str(self.kap)},pc={self.pc}]")

def divisors_gt1(n):
    return [d for d in range(2, abs(n)+1) if n % d == 0]

def lf_content(u):
    a, b = LF(u); return gcd(a, b) if (a or b) else 0

def child_from(node, red, mu, branch, kl, nu_form, m_form, tmax=6):
    """Q(F) for solution family nu=nu_form(t), m=m_form(t), t=0..: samples t and s,
    requires s-independent kap_F/rho_F/M_F/lambda and linear-in-t forms; on periodic
    M_F variation returns 'SPLIT' marker so caller re-calls on residue classes."""
    rho, nuG, kap = node.rho, node.nu, node.kap
    recs = []
    for t in range(tmax):
        nu_ = nu_form[0]*t + nu_form[1]; m_ = m_form[0]*t + m_form[1]
        if nu_ < (1 if branch == 'I' else 2) or m_ < red['m0']: return None
        if branch == 'IIa_k': dp, dq = (kl+mu)*nu_, (kl+1)*nu_ + 1
        elif branch == 'IIa_0': dp, dq = mu*nu_, (kl+1)*nu_ + 1
        elif branch == 'I': dp, dq = kl+mu, kl+1
        elif branch == 'IIb': dp, dq = (kl+mu)*nu_ + 1, (kl+1)*nu_ + 1
        elif branch == 'III': dp, dq = mu + kl*nu_, 1 + kl*nu_
        svals = []
        for s in range(0, 4):
            if red['style'] == 'II':
                n = lf_eval(red['n0'], s) + lf_eval(nuG, s)*m_
                if n < 1: return ('SKIP', f"n<1 at s={s} (n0=0 edge)", None, None)
                kapF = Fr(lf_eval(kap, s) + n, lf_eval(nuG, s))
                DFi = Fr(mu) * (rho + n) / lf_eval(nuG, s)
            else:
                kapF = Fr(lf_eval(kap, s) + m_)
                DFi = Fr(mu) * (rho + m_)
            svals.append((kapF, DFi))
        if len({v for v in svals}) != 1:
            return ('OPEN', f"mu={mu} {branch} kl={kl}: kap_F/D_F s-dependent", None, None)
        kapF, DFi = svals[0]
        if kapF.denominator != 1: return None          # (d)-integrality kills family
        MF = gcd(dp, dq)
        gap = DFi - kapF
        gapc = -((-gap.numerator) // gap.denominator) if isinstance(gap, Fr) else gap
        lam = kl * max(1, gapc) if branch in ('IIa_k', 'I', 'III') else 0
        if branch == 'IIb': lam = max(lam, 1)
        recs.append((t, nu_, m_, dp, dq, kapF, DFi, MF, lam))
    MFs = {r[7] for r in recs}
    if len(MFs) != 1:
        return ('SPLIT', f"M_F varies {sorted(MFs)}", None, None)
    rhoFs = {r[6]/r[3] for r in recs}
    if len(rhoFs) != 1:
        return ('OPEN', f"mu={mu} {branch} kl={kl}: rho_F varies over t", None, None)
    lams = {r[8] for r in recs}
    if len(lams) != 1:
        return ('OPEN', f"mu={mu} {branch} kl={kl}: lambda varies over t", None, None)
    lam = lams.pop()
    if isinstance(lam, Fr):
        if lam.denominator != 1: return ('OPEN', f"nonintegral lambda {lam}", None, None)
        lam = int(lam)
    kaps = [r[5] for r in recs]; dkap = int(kaps[1] - kaps[0]) if len(recs) > 1 else 0
    assert all(kaps[i+1]-kaps[i] == dkap for i in range(len(recs)-1)), "kap_F not linear in t"
    dps = [r[3] for r in recs]; ddp = dps[1]-dps[0] if len(recs) > 1 else 0
    pcF = (node.pc // mu) * (gcd(ddp, dps[0]) if ddp else dps[0])
    child = Node(rhoFs.pop(), nu_form, MFs.pop(), (dkap, int(kaps[0])), pcF,
                 tag=f"<-{branch}mu{mu}k{kl}")
    why = (f"mu={mu} {branch} k/l={kl} nu={lf_str(nu_form)} m={lf_str(m_form)} "
           f"dp={dps[0]}{'+%dt' % ddp if ddp else ''} -> {child} lam>={lam}")
    return ('CONT', lam, child, why)

def split_residues(nu_form, m_form, r):
    """Refine t -> r*t+i families."""
    return [((nu_form[0]*r, nu_form[0]*i + nu_form[1]),
             (m_form[0]*r, m_form[0]*i + m_form[1])) for i in range(r)]

def instantiate(node, s):
    """Concrete node at family parameter value s."""
    return Node(node.rho, lf_eval(node.nu, s), node.M, lf_eval(node.kap, s),
                node.pc, tag=node.tag + f"@s={s}")

def step_one_branch(node, mu, branch):
    """Outcomes of one (mu, branch) pair on `node` (must reduce s-free)."""
    out = []
    red = reduce_ratio(node.rho, node.nu, node.kap, mu,
                       'III' if branch == 'III' else 'II')
    lam_min = 0 if branch == 'IIa_0' else 1      # all other branches cost lambda>=1
    if red is None:
        return [('OPEN', f"mu={mu} {branch}: no s-free reduction (inner) at {node}", lam_min)]
    pts, fams, cert = solve_pattern(red, mu, branch)
    for f in fams:
        out.append(('OPEN', f"mu={mu} {branch}: degenerate family {f} at {node}", lam_min))
    famlist, iso = detect_families(pts)
    queue = [(kl, nf, mf) for kl, nf, mf, _ in famlist]
    queue += [(kl, (0, nu_), (0, m_)) for kl, nu_, m_ in iso]
    for kl, nf, mf in queue:
        res = child_from(node, red, mu, branch, kl, nf, mf)
        if res is None: continue
        if res[0] == 'SPLIT':
            done = False
            for r in (2, 3, 4, 5, 6, 8, 12):
                subs = [child_from(node, red, mu, branch, kl, nf2, mf2)
                        for nf2, mf2 in split_residues(nf, mf, r)]
                if all(x is None or x[0] not in ('SPLIT',) for x in subs):
                    out.extend(x for x in subs if x and x[0] != 'SKIP')
                    done = True; break
            if not done:
                out.append(('OPEN', f"mu={mu} {branch} kl={kl}: M_F aperiodic mod<=12 at {node}", lam_min))
        elif res[0] == 'SKIP': pass
        elif res[0] == 'OPEN':
            out.append(('OPEN', res[1] + f" at {node}", lam_min))
        else: out.append(res)
    return out

def step(node):
    """All outcomes of one propagation step from `node`. Returns list of tuples
    ('KILL_M1'|'CONT'|'TERMINAL_IV'|'OPEN', ...)."""
    out = []
    ka, kb = LF(node.kap); na, nb = LF(node.nu)
    if not (ka - na >= 0 and kb - nb >= 0):            # kap < nu possible somewhere
        cond = "all s" if (ka - na <= 0 and kb - nb < 0) else f"some s (kap-nu={lf_str((ka-na, kb-nb))})"
        out.append(('TERMINAL_IV', f"case IV possible ({cond}); killed iff H3"))
    out.append(('KILL_M1', "mu=1 => M_F=1"))
    for mu in divisors_gt1(node.M):                    # St 8.4: mu | M only; the
        # j-unit absorbs deg(p_G)-content divisibility (i = P/mu rescales j)
        if mu == 2:
            out.append(('KILL_M1', "mu=2: I, IIb, III => M_F=1"))
        branches = ['IIa_k', 'IIa_0'] + (['I', 'IIb', 'III'] if mu >= 3 else [])
        for branch in branches:
            style = 'III' if branch == 'III' else 'II'
            done = False
            for shift in range(0, 4):
                nu_s = (LF(node.nu)[0], LF(node.nu)[0]*shift + LF(node.nu)[1])
                kap_s = (LF(node.kap)[0], LF(node.kap)[0]*shift + LF(node.kap)[1])
                if reduce_ratio(node.rho, nu_s, kap_s, mu, style) is not None:
                    shifted = Node(node.rho, nu_s, node.M, kap_s, node.pc,
                                   tag=node.tag + (f">>s+{shift}" if shift else ""))
                    for s in range(0, shift):
                        out.extend(step_one_branch(instantiate(node, s), mu, branch))
                    out.extend(step_one_branch(shifted, mu, branch))
                    done = True; break
            if not done:
                for s in range(0, 6):
                    out.extend(step_one_branch(instantiate(node, s), mu, branch))
                out.append(('OPEN', f"mu={mu} {branch}: s-dependent; s<=5 instantiated, "
                            f"s>=6 tail unproven at {node}",
                            0 if branch == 'IIa_0' else 1))
    return out

# ------------------------------------------------------------------ chain search
def bash(entry, budget, maxdepth=7, sinst=3):
    """BFS over chains from entry Node. Kills: M_F=1 (Prop 8.4, single-pole only),
    lambda-budget (St 9.4), IV-terminal iff H3. Survivor = IV-terminal reached
    (reported; dies under H3) or OPEN outcome or depth/loop frontier residue.
    Family nodes are chased as parametric shapes; revisited shapes (loop) noted.
    Returns dict verdict + traces."""
    seen = {}
    iv_hits, opens, loops, frontier = [], [], [], []
    dq_ = deque([(entry, 0, [f"ENTRY {entry}"])])
    seen[entry.shape()] = 0
    while dq_:
        node, lam, trace = dq_.popleft()
        if len(trace) - 1 >= maxdepth:
            frontier.append((node, lam, trace)); continue
        for o in step(node):
            kind = o[0]
            if kind == 'KILL_M1': continue
            if kind == 'TERMINAL_IV':
                iv_hits.append((trace + [o[1]], lam)); continue
            if kind == 'OPEN':
                lmin = o[2] if len(o) > 2 else 0
                if lam + lmin > budget: continue    # budget-killed open branch
                opens.append((trace + [o[1]], lam)); continue
            _, dl, child, why = o
            nl = lam + dl
            if nl > budget: continue                    # St 9.4 kill
            if child.M == 1: continue                   # Prop 8.4 kill (single-pole)
            sh = child.shape()
            if sh in seen and seen[sh] <= nl:
                loops.append((trace + [why + " [LOOP->seen shape]"], nl)); continue
            seen[sh] = nl
            dq_.append((child, nl, trace + [why]))
    verdict = ("EXCLUDED (conditional on H1-H4+H3)" if not opens and not frontier
               else "OPEN branches remain")
    return dict(verdict=verdict, iv=iv_hits, open=opens, loops=loops,
                frontier=frontier)

# ------------------------------------------------------------------ campaign runs
def gate():
    got = prop91(Lmax=6)
    assert got == THESIS_TABLE and len(got) == 11, "GATE FAIL: Prop 9.1"
    sols = stmt96_knonzero()
    pairs = sorted(((k+2)*nu, (k+1)*nu+1) for k, nu, n in sols if n % 3 == 1)
    assert pairs == [(20, 16), (21, 15)], "GATE FAIL: Stmt 9.6 corrected pairs"
    assert (1, 25, 12) in sols, "GATE FAIL: erratum row (k,nu,n)=(1,25,12)"
    assert all(l == 0 for l, nu, n in stmt96_k0()), "GATE FAIL: k=0 family"
    # engine-level gate: St 9.6 via the generic engine must reproduce (iii),(iv),(v)
    outs = step(Node(Fr(1, 2), 3, 2, 5, pcontent=2))
    conts = sorted(str(o[2].shape()) for o in outs if o[0] == 'CONT')
    exp = [str((Fr(1, 3), (0, 7), 3, (0, 5))), str((Fr(1, 4), (0, 5), 4, (0, 4))),
           str((Fr(3, 2), (2, 3), 2, (3, 6)))]
    assert conts == sorted(exp), f"GATE FAIL: engine St 9.6 shapes {conts}"
    lams = sorted((o[2].shape()[0], o[1]) for o in outs if o[0] == 'CONT')
    assert lams == [(Fr(1, 4), 2), (Fr(1, 3), 2), (Fr(3, 2), 0)], f"GATE FAIL lam {lams}"
    return ("GATE PASS: Prop 9.1 11/11; Stmt 9.6 pairs {(21,15),(20,16)} + erratum "
            "(75,51) reproduced; engine reproduces St 9.6 (iii),(iv),(v) with lambdas 2,2,0")

# thesis nodes (engine-native s>=0 forms; V911 = 9.6(v) output form):
V96 = Node(Fr(1, 2), 3, 2, 5, 2)
V97 = Node(Fr(1, 3), 7, 3, 5, 3)
V98 = Node(Fr(1, 4), 5, 4, 4, 4)
V99 = Node(Fr(3, 4), (4, 3), 4, (3, 3), 4)
V910 = Node(Fr(2, 3), (3, 2), 3, (2, 2), 3)
V911 = Node(Fr(3, 2), (2, 3), 2, (3, 6), 2)

def run_validation():
    for name, node in [("St9.6", V96), ("St9.7", V97), ("St9.8", V98),
                       ("St9.9", V99), ("St9.10", V910), ("St9.11", V911)]:
        print(f"[{name}] {node}")
        for o in step(node):
            print("   ", o[0], o[3] if o[0] == 'CONT' else o[1])

def entry_nodes(lam_target=6):
    """Single-pole entries with Lambda == lam_target from the Prop 9.1 table
    (Lmax=7 sweep, so also usable for Lambda=7/td=7 estimates). Q per St 9.1:
    kap = D+Dg. M-branch: thesis-sanctioned M | gcd(D,P) (AF3) + superset mu | P."""
    rows = sorted(prop91(Lmax=7), key=lambda r: (r[4], r[0], r[1], r[2], r[3]))
    ent = []
    for (al, be), (D, Dg), (P, Pg), nu, Lam in rows:
        if Lam != lam_target: continue
        for Mv in divisors_gt1(P):
            sanct = (gcd(D, P) % Mv == 0)
            ent.append((f"({al},{be})D{D}P{P}nu{nu}M{Mv}", Lam, sanct,
                        Node(Fr(D, P), nu, Mv, D + Dg, P)))
    return ent

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument("phase", nargs="?", default="all")
    ap.add_argument("--budget", type=int, default=4)
    ap.add_argument("--lam", type=int, default=6)
    args = ap.parse_args()
    ph = args.phase
    if ph in ("gate", "all"):
        print(gate())
    if ph in ("table",):
        for r in sorted(prop91(Lmax=7), key=lambda r: (r[4], r[0])): print(r)
    if ph in ("validate", "all"):
        run_validation()
    if ph in ("bash5", "all"):
        print("\n=== td<=5 validation chains (single-pole, budget=Lambda-2) ===")
        for lam_t in (3, 4, 5):
            for name, Lam, sanct, node in entry_nodes(lam_t):
                r = bash(node, lam_t - 2)
                print(f"[td={lam_t} {name}] {'SANC' if sanct else 'ext '} "
                      f"verdict={r['verdict']} iv={len(r['iv'])} open={len(r['open'])} "
                      f"loops={len(r['loops'])} frontier={len(r['frontier'])}")
                for tr, lam in r['open'][:4]:
                    print("    OPEN lam", lam, "|", tr[-1][:100])
    if ph == "report":
        import re as _re
        print("== td=6 campaign digest ==")
        tot_cont = 0
        for name, Lam, sanct, node in entry_nodes(6):
            r = bash(node, 4)
            od = {}
            for tr, lam in r['open']:
                key = _re.sub(r" at Q\[.*", "", tr[-1])
                nd = _re.search(r"at (Q\[[^]]*\])", tr[-1])
                od.setdefault((key, nd.group(1) if nd else "?"), []).append(lam)
            ivshapes = {}
            for tr, lam in r['iv']:
                m = _re.search(r"-> (Q\[[^]]*\])", tr[-2]) if len(tr) > 1 else None
                ivshapes.setdefault(m.group(1) if m else tr[-2][:60], []).append(lam)
            print(f"\n[{name}] {'SANCTIONED' if sanct else 'superset'} verdict={r['verdict']}")
            print(f"  iv_terminals={len(r['iv'])} distinct_shapes={len(ivshapes)} "
                  f"opens={len(r['open'])} distinct={len(od)} loops={len(r['loops'])}")
            for (k, nd), lams in sorted(od.items()):
                print(f"  OPEN minlam={min(lams)} x{len(lams)} {k[:80]} | {nd[:70]}")
            for k, lams in sorted(ivshapes.items())[:8]:
                print(f"  IVSHAPE minlam={min(lams)} x{len(lams)} {k[:95]}")
    if ph in ("bash", "all"):
        print(f"\n=== td=6 bash: single-pole entries Lambda={args.lam}, budget={args.budget} ===")
        for name, Lam, sanct, node in entry_nodes(args.lam):
            r = bash(node, args.budget)
            print(f"[{name}] {'SANC' if sanct else 'ext '} verdict={r['verdict']} "
                  f"iv={len(r['iv'])} open={len(r['open'])} loops={len(r['loops'])} "
                  f"frontier={len(r['frontier'])}")
            for tr, lam in r['open'][:6]:
                print("    OPEN lam", lam, "|", tr[-1][:110])
            for tr, lam in r['iv'][:4]:
                print("    IV   lam", lam, "|", " => ".join(t[:60] for t in tr[-2:]))
