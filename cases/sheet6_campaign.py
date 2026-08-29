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
  mu=1                  -> M_F = gcd(nu, n nu+1) = 1; KILL only when F is
                           certified nonroot (the nu_F=1 root menu is retained)
  case I   (nu_F=1)     : deg p = k+mu, deg q = k+1, k>=1; mu=2 gives M_F=1,
                           but is retained until the root signature is tested;
                          mu>=3: ratio eq RATIO_II, M_F = gcd(mu-1, k+1)
  case IIa (nu_F=nu>=2) : deg p = (k+mu)nu, deg q = (k+l+1)nu+1; k>0 => l=0 (St 8.2)
  case IIb              : deg p = (k+mu)nu+1, deg q = (k+1)nu+1; mu=2 ->
                          certified nonroot M_F=1 KILL
  case III (nu_F=nu>=2) : deg p = mu+k nu, deg q = 1+k nu; k=0 -> certified
                          nonroot M_F=1 KILL;
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
from math import gcd, isqrt
from collections import deque

# SHEET6-AF2.md: price case IIb by the derived rule (St 9.3 (24), sign-fixed
# E6): lambda >= k*max(1, ceil(D_F/i - kap_F))  [k extra orbits, c* != 0]
#              + max(1, ceil((D_F/i - kap_F)/nu_F))  [extra root 0, c* = 0].
# Default False = legacy flat lambda>=1 (the thesis's printed IIb practice);
# gate/validate phases run with the default and are unchanged.
IIB_DERIVED = False
PATTERN_KMAX = 48
PATTERN_NUSWEEP = 1200
PATTERN_MSWEEP = 1200

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
    for all s >= 0 (coefficient conditions). Returns form or None.
    [tduniform: q-window widened +-12 -> +-160 (kap up to ~a(alpha+beta) at
    td<=40 needs q ~ kap/nu > 12); pure search-space widening, OPEN->solved.]"""
    ka, kb = LF(kap); na, nb = LF(nu)
    for q in range(-160, 161):
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
def solve_mu1_exact(red):
    """Solve the zero-cost MU1 branch for every ``l>=0`` and ``m>=m0``.

    For MU1, ``dp=1``, ``dq=l+2`` and the II reduction has ``a=c``. Put
    ``r=l+1`` and ``X=a*m+b``. The ratio equation is exactly

        r * X = e - b.

    Thus, when ``a>0``, all solutions are obtained from the positive divisors
    ``X`` of ``e-b`` satisfying ``X == b (mod a)``. If ``a=0``, the equation
    is independent of m; the exact all-m tail is returned as a degenerate
    family so callers must report OPEN rather than silently close it.
    """
    a, b, c, e, m0 = red['a'], red['b'], red['c'], red['e'], red['m0']
    assert a == c and a >= 0, "MU1 II reduction must have a=c>=0"
    # The reduced numerator a*m+b is a positive scalar multiple of
    # mu*(rho+n) on the admissible ray.  Recording positivity at its first
    # admissible point makes the positive-divisor enumeration below explicit;
    # a>=0 then propagates it to every m>=m0.
    assert a*m0 + b > 0, "MU1 reduction must have a*m+b>0 for m>=m0"
    delta = e - b
    if delta <= 0:
        return [], [], f"EXACT MU1: e-b={delta}<=0, no r*X solution"
    if a == 0:
        if b <= 0 or delta % b:
            return [], [], "EXACT MU1 constant ratio: no integral r>=1"
        r = delta // b
        if r < 1:
            return [], [], "EXACT MU1 constant ratio: r<1"
        l = r - 1
        fam = ('MU1', l, 1, f"ALL m>={m0} exact constant-ratio family")
        return [], [fam], f"EXACT MU1 degenerate: l={l}, all m>={m0}"

    factors = set()
    for d in range(1, isqrt(delta) + 1):
        if delta % d == 0:
            factors.add(d)
            factors.add(delta // d)
    pts = []
    for X in sorted(factors):
        if (X - b) % a:
            continue
        m = (X - b) // a
        if m < m0:
            continue
        r = delta // X
        if r < 1:
            continue
        l = r - 1
        assert (l + 1) * (a*m + b) == delta
        assert (c*m + e) == (l + 2) * (a*m + b)
        pts.append((l, 1, m))
    return sorted(set(pts)), [], \
        f"EXACT MU1 divisor solve: (l+1)(a*m+b)=e-b={delta}"


def solve_pattern(red, mu, branch, KMAX=PATTERN_KMAX,
                  NUSWEEP=PATTERN_NUSWEEP, MSWEEP=PATTERN_MSWEEP):
    """Solve deg(p)*(c m+e) == deg(q)*(a m+b) over the branch shape:
      'IIa_k': dp=(k+mu)nu, dq=(k+1)nu+1, k>=1, nu>=2      (l=0 St 8.2)
      'IIa_0': dp=mu nu,    dq=(l+1)nu+1, l>=0, nu>=2      (k=0)
      'I'    : dp=k+mu,     dq=k+1,       k>=1, nu=1
      'MU1'  : dp=1,        dq=l+2,       l>=0, nu=1 (single orbit/root menu)
      'IIb'  : dp=(k+mu)nu+1, dq=(k+1)nu+1, k>=0, nu>=2
      'III'  : dp=mu+k nu,  dq=1+k nu,    k>=1, nu>=2
    Returns (points [(kl,nu,m)], families [(kl,(dn,n1),(dm,m1),modulus-checked)],
    cert string). Completeness: per (kl,nu) exact m-solve; per (kl,m) exact nu-solve;
    families detected from the alpha1=0 congruence structure and slope==|Am| checked;
    kl-range certified via ratio-vs-1 monotone bound when derivable, else flagged."""
    a, b, c, e, m0 = red['a'], red['b'], red['c'], red['e'], red['m0']
    if branch == 'MU1':
        # KMAX is deliberately ignored: solve_mu1_exact is unbounded in l.
        return solve_mu1_exact(red)
    def degs(kl, nu):
        if branch == 'IIa_k': return (kl+mu)*nu, (kl+1)*nu + 1
        if branch == 'IIa_0': return mu*nu, (kl+1)*nu + 1
        if branch == 'I':     return kl+mu, kl+1
        if branch == 'MU1':   return 1, kl+2
        if branch == 'IIb':   return (kl+mu)*nu + 1, (kl+1)*nu + 1
        if branch == 'III':   return mu + kl*nu, 1 + kl*nu
        raise ValueError(branch)
    lo = 0 if branch in ('IIa_0', 'IIb', 'MU1') else 1
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
    nurange = (1, 1) if branch in ('I', 'MU1') else (2, NUSWEEP)
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
        if branch not in ('I', 'MU1'):
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


# Root/nonroot M=1 scope. Corrected Proposition 8.4 applies only to a
# certified nonroot down vertex. The numerical root signature is tested
# before any M-filter; explicit geometric metadata (for example, a pole
# entry) may still certify a numerically root-like fixture as nonroot.
KEEP = "KEEP"
KILL_NR_M1 = "KILL_NR_M1"
TERMINAL_ROOT_M1 = "TERMINAL_ROOT_M1"
TERMINAL_ROOT_M_GT1 = "TERMINAL_ROOT_M_GT1"
UNRESOLVED_M1_SCOPE = "UNRESOLVED_M1_SCOPE"


def has_root_signature(node):
    """Whether Q(node) has the Statement 9.2 root signature."""
    return LF(node.nu) == (0, 1) and LF(node.kap) == (0, 1)


def dispose_m1(node, *, certified_nonroot=False):
    """Classify a down vertex without applying Proposition 8.4 at root.

    Callers pass ``certified_nonroot=True`` only when the transition or
    external metadata supplies that geometric certificate. Without it, a
    root signature is terminal and an M=1 nonroot-looking record is left
    unresolved instead of being silently killed.
    """
    if certified_nonroot:
        return KILL_NR_M1 if node.M == 1 else KEEP
    if has_root_signature(node):
        return TERMINAL_ROOT_M1 if node.M == 1 else TERMINAL_ROOT_M_GT1
    return UNRESOLVED_M1_SCOPE if node.M == 1 else KEEP


def dispose_constructed_child(node):
    """Root-first disposition for a characteristic-transition child.

    In this engine a constructed child missing the unique root signature is
    a certified nonroot down vertex. Keeping that fact here prevents each
    BFS from reintroducing the old ``child.M == 1`` shortcut.
    """
    disposition = dispose_m1(node)
    if disposition == UNRESOLVED_M1_SCOPE:
        disposition = dispose_m1(node, certified_nonroot=True)
    return disposition

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
        if nu_ < (1 if branch in ('I', 'MU1') else 2) or m_ < red['m0']: return None
        if branch == 'IIa_k': dp, dq = (kl+mu)*nu_, (kl+1)*nu_ + 1
        elif branch == 'IIa_0': dp, dq = mu*nu_, (kl+1)*nu_ + 1
        elif branch == 'I': dp, dq = kl+mu, kl+1
        elif branch == 'MU1': dp, dq = 1, kl+2
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
        if branch == 'IIb':
            if IIB_DERIVED:                    # SHEET6-AF2 sec 2-3 pricing
                g0 = Fr(gap) / nu_             # (24) c*=0 branch: gap/nu_F
                g0c = -((-g0.numerator) // g0.denominator)
                lam = kl * max(1, gapc) + max(1, g0c)
            else:
                lam = max(lam, 1)              # legacy: printed lambda>=1 floor
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
    lam_min = 0 if branch in ('IIa_0', 'MU1') else 1
    if red is None:
        return [('OPEN', f"mu={mu} {branch}: no s-free reduction (inner) at {node}", lam_min)]
    pts, fams, cert = solve_pattern(red, mu, branch)
    if branch == 'IIa_0':
        # k=0 gives no automatic exit charge, so the finite l/nu/m box is
        # never a no-solution certificate. Keep a mandatory residue until an
        # analytic completeness bound or an exact unbounded solver replaces it.
        out.append(('OPEN',
                    f"mu={mu} IIa_0 zero-charge tail beyond "
                    f"l<={PATTERN_KMAX},nu<={PATTERN_NUSWEEP},"
                    f"m<={PATTERN_MSWEEP}: NO_VERDICT at {node}",
                    0))
    for f in fams:
        out.append(('OPEN', f"mu={mu} {branch}: degenerate family {f} at {node}", lam_min))
    famlist, iso = detect_families(pts)
    queue = [(kl, nf, mf) for kl, nf, mf, _ in famlist]
    queue += [(kl, (0, nu_), (0, m_)) for kl, nu_, m_ in iso]
    for kl, nf, mf in queue:
        res = child_from(node, red, mu, branch, kl, nf, mf)
        if res is None:
            if lam_min == 0:
                out.append(('OPEN',
                            f"mu={mu} {branch} kl={kl}: zero-charge child "
                            f"realization not analytically excluded: "
                            f"NO_VERDICT at {node}", 0))
            continue
        if res[0] == 'SPLIT':
            done = False
            for r in (2, 3, 4, 5, 6, 8, 12):
                subs = [child_from(node, red, mu, branch, kl, nf2, mf2)
                        for nf2, mf2 in split_residues(nf, mf, r)]
                if all(x is None or x[0] not in ('SPLIT',) for x in subs):
                    out.extend(x for x in subs if x and x[0] != 'SKIP')
                    if lam_min == 0 and any(
                            x is None or x[0] == 'SKIP' for x in subs):
                        out.append(('OPEN',
                                    f"mu={mu} {branch} kl={kl}: unresolved "
                                    f"zero-charge residue after mod-{r} split: "
                                    f"NO_VERDICT at {node}", 0))
                    done = True; break
            if not done:
                out.append(('OPEN', f"mu={mu} {branch} kl={kl}: M_F aperiodic mod<=12 at {node}", lam_min))
        elif res[0] == 'SKIP':
            if lam_min == 0:
                out.append(('OPEN',
                            f"mu={mu} {branch} kl={kl}: {res[1]}; "
                            f"zero-charge parameter tail NO_VERDICT at {node}", 0))
        elif res[0] == 'OPEN':
            out.append(('OPEN', res[1] + f" at {node}", lam_min))
        else: out.append(res)
    return out

def step(node):
    """All outcomes of one propagation step from `node`. Returns list of tuples
    ('CONT'|'TERMINAL_IV'|'OPEN', ...). M=1 is disposed only after a child
    exists, so a root-signature child cannot be hidden by an abstract kill."""
    out = []
    ka, kb = LF(node.kap); na, nb = LF(node.nu)
    if not (ka - na >= 0 and kb - nb >= 0):            # kap < nu possible somewhere
        cond = "all s" if (ka - na <= 0 and kb - nb < 0) else f"some s (kap-nu={lf_str((ka-na, kb-nb))})"
        out.append(('TERMINAL_IV', f"case IV possible ({cond}); killed iff H3"))
    # The single-orbit mu=1 branch has M_F=1. It is normally NR-M1, but its
    # nu_F=1 member can be the root and therefore must be constructed.
    branch_menu = [(1, ['MU1'])]
    for mu in divisors_gt1(node.M):                    # St 8.4: mu | M only; the
        # j-unit absorbs deg(p_G)-content divisibility (i = P/mu rescales j).
        # For mu=2, IIb and III have nu_F>=2 and M_F=1, hence are certified
        # NR-M1. Case I can have the root signature and must be enumerated.
        branches = ['IIa_k', 'IIa_0', 'I']
        if mu >= 3:
            branches += ['IIb', 'III']
        branch_menu.append((mu, branches))
    for mu, branches in branch_menu:
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
                            0 if branch in ('IIa_0', 'MU1') else 1))
    return out

# ------------------------------------------------------------------ chain search
def bash(entry, budget, maxdepth=7, sinst=3):
    """BFS over chains from entry Node. Kills: M_F=1 only at certified nonroot
    down vertices (corrected Prop 8.4, single-pole only),
    lambda-budget (conditional on the accepted Section 7 weighted budget /
    first-separation ledger), IV-terminal iff H3. Survivor = IV-terminal reached
    (reported; dies under H3) or OPEN outcome or depth/loop frontier residue.
    Family nodes are chased as parametric shapes; revisited shapes (loop) noted.
    Returns dict verdict + traces."""
    seen = {}
    iv_hits, root_hits, opens, loops, frontier = [], [], [], [], []
    dq_ = deque([(entry, 0, [f"ENTRY {entry}"])])
    seen[entry.shape()] = 0
    while dq_:
        node, lam, trace = dq_.popleft()
        if len(trace) - 1 >= maxdepth:
            frontier.append((node, lam, trace)); continue
        for o in step(node):
            kind = o[0]
            if kind == 'TERMINAL_IV':
                iv_hits.append((trace + [o[1]], lam)); continue
            if kind == 'OPEN':
                lmin = o[2] if len(o) > 2 else 0
                if lam + lmin > budget: continue    # budget-killed open branch
                opens.append((trace + [o[1]], lam)); continue
            _, dl, child, why = o
            nl = lam + dl
            if nl > budget: continue                    # St 9.4 kill
            disposition = dispose_constructed_child(child)  # recognize root first
            if disposition in (TERMINAL_ROOT_M1, TERMINAL_ROOT_M_GT1):
                root_hits.append((trace + [why + f" [{disposition}]"], nl))
                continue
            if disposition == KILL_NR_M1:
                continue
            assert disposition == KEEP
            sh = child.shape()
            if sh in seen and seen[sh] <= nl:
                loops.append((trace + [why + " [LOOP->seen shape]"], nl)); continue
            seen[sh] = nl
            dq_.append((child, nl, trace + [why]))
    verdict = ("EXCLUDED (conditional on H1-H4+H3 and Section 7 budget)"
               if not opens and not frontier and not root_hits
               else "OPEN branches remain")
    return dict(verdict=verdict, iv=iv_hits, open=opens, loops=loops,
                frontier=frontier, root=root_hits)

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
    # The historical gate compares the certified-nonroot survivor graph.
    # Root terminals are reported separately and NR-M1 children are pruned.
    kept = [o for o in outs if o[0] == 'CONT'
            and dispose_constructed_child(o[2]) == KEEP]
    conts = sorted(str(o[2].shape()) for o in kept)
    exp = [str((Fr(1, 3), (0, 7), 3, (0, 5))), str((Fr(1, 4), (0, 5), 4, (0, 4))),
           str((Fr(3, 2), (2, 3), 2, (3, 6)))]
    assert conts == sorted(exp), f"GATE FAIL: engine St 9.6 shapes {conts}"
    lams = sorted((o[2].shape()[0], o[1]) for o in kept)
    assert lams == [(Fr(1, 4), 2), (Fr(1, 3), 2), (Fr(3, 2), 0)], f"GATE FAIL lam {lams}"
    return ("GATE PASS: Prop 9.1 11/11; Stmt 9.6 pairs {(21,15),(20,16)} + erratum "
            "(75,51) reproduced; engine reproduces St 9.6 (iii),(iv),(v) with lambdas 2,2,0")

# ---------------------------------------------- tails3: III structural filter
# SHEET6-III.md: St 3.16/3.18 + Def 3.1/Not 3.4/3.5/3.8 extraction. Facts used:
#   N1: any vertex with nu >= 2 is I_P(alpha_j), kap-bar = (kappa-beta_j)/e_j,
#       nu = e_{j-1}/e_j => gcd(kap-bar, nu) = gcd(beta_j, e_{j-1})/e_j = 1.
#   E5: printed Prop 9.3 (g)/(h) [den nu_F] are Notation-3.5-consistent only if
#       nu_F = nu_G; corrected (g')/(h') have den nu_G:
#       kapF = (nuF*kapG + n)/nuG, DF/i = mu(nuF*rho + n)/nuG,
#       ratio (f) unchanged: (mu+k*nuF)/(1+k*nuF) = mu(nuF*rho+n)/(nuF*kapG+n).
#   => gap = DF/i - kapF = mu(kapG - rho)/(k*nuG); with AF2
#      lambda_III >= k*max(1, ceil(gap/1)) >= ceil(Lam), Lam := mu(kapG-rho)/nuG.
#   Locked tails (kapG = rho(nuG+1) identically): Lam = mu*rho (s-free), and
#      rhoF = mu*rho/(k(mu-1)), kapF = rhoF(1+k*nuF), DF/i = rhoF(mu+k*nuF).
import re as _re2

def parse_node(msg):
    m = _re2.search(r"at Q\[rho=([-\d/]+),nu=([^,\]]+),M=(\d+),kap=([^,\]]+),"
                    r"pc=(\d+)\]", msg)
    if not m: return None
    def pf(t):
        mm = _re2.fullmatch(r"(?:(-?\d+)s)?([+-]?\d+)?", t)
        if not mm or (mm.group(1) is None and mm.group(2) is None): return None
        return (int(mm.group(1) or 0), int(mm.group(2) or 0))
    nu, kap = pf(m.group(2)), pf(m.group(4))
    if nu is None or kap is None: return None
    return Node(Fr(m.group(1)), nu, int(m.group(3)), kap, int(m.group(5)))

def is_locked(node):
    """kap(s) == rho*(nu(s)+1) identically (lambda=0-family lock)."""
    r = node.rho; ka, kb = LF(node.kap); na, nb = LF(node.nu)
    return Fr(ka) == r*na and Fr(kb) == r*(nb + 1)

def budget_kill_all_s(node, mu, B, smin=0):
    """Certify mu*(kap(s)-rho) > B*nu(s) for all integer s >= smin (exact)."""
    L = node.rho.denominator
    ka, kb = LF(node.kap); na, nb = LF(node.nu)
    a = mu*L*ka - B*L*na
    b = mu*L*(ka*smin + kb) - mu*node.rho.numerator - B*L*(na*smin + nb)
    return a >= 0 and b > 0

def n1_residues(nu, kap):
    """Killed residues {r mod R : gcd(nu(s),kap(s)) > 1 for s == r}, R the
    resultant |a*d - b*c| (any common prime divides R; s-dependence mod p only,
    p | R => set periodic mod R). Sample-asserted out to 3R."""
    (a, b), (c, d) = LF(nu), LF(kap)
    R = abs(a*d - b*c)
    assert R != 0, "proportional nu/kap forms"
    killed = [r for r in range(R) if gcd(a*r + b, c*r + d) > 1]
    for s in range(R, 3*R):
        assert (gcd(a*s + b, c*s + d) > 1) == ((s % R) in killed)
    return R, killed

def cong_survivors(node, mu, B, numax=600):
    """Locked node, E5 arithmetic. Enumerate k (lambda(k) <= B) and nu_F:
    require kapF = rhoF(1+k*nuF) in N [(h') <=> n-congruence], M_F =
    gcd(mu-1, 1+k*nuF) >= 2 [corrected Prop 8.4 at nuF>=2, hence nonroot],
    gcd(kapF, nuF) = 1 [N1@F], and an
    s-window with n(s) = kapF*nu(s) - nuF*kap(s) >= 1. Returns (witnesses,
    certified_none): certified_none=True iff no nu_F in a full period passes
    even the periodic conditions (then the empty result is exact, not bounded).
    PIT: each witness's (f)/(h') consistency asserted at 3 sample s."""
    assert is_locked(node)
    Lam = mu*node.rho
    wits, any_periodic_pass = [], False
    for k in range(1, B + 1):
        lam_k = k*max(1, -(-Lam.numerator // (Lam.denominator*k)))
        if lam_k > B: continue
        rF = Fr(mu, k*(mu - 1))*node.rho
        period = rF.denominator*(mu - 1)
        for nuF in range(2, numax + 1):
            assert nuF >= 2                     # explicit nonroot scope
            kapF = rF*(1 + k*nuF)
            MF = gcd(mu - 1, 1 + k*nuF)
            if kapF.denominator == 1 and MF >= 2 and nuF <= 2 + period:
                any_periodic_pass = True
            if kapF.denominator != 1 or MF < 2: continue
            if gcd(int(kapF), nuF) != 1: continue
            na, nb = LF(node.nu); ka, kb = LF(node.kap)
            n_a = int(kapF)*na - nuF*ka
            n_bq = Fr(int(kapF)*nb) - Fr(nuF)*Fr(kb)     # kap form is integer
            if not (n_a > 0 or (n_a == 0 and n_bq >= 1) or
                    Fr(n_a*6) + n_bq >= 1):              # some s >= 6 has n>=1
                continue
            for s in (6, 7, 9):                          # PIT on (f)+(h')
                nuG, kapG = lf_eval(node.nu, s), lf_eval(node.kap, s)
                n = int(kapF)*nuG - nuF*kapG
                if n < 1: continue
                assert (mu + k*nuF)*(nuF*kapG + n) == \
                       (1 + k*nuF)*mu*(nuF*node.rho + n), "E5 ratio PIT"
                assert (nuF*kapG + n) % nuG == 0 and \
                       (nuF*kapG + n)//nuG == int(kapF), "E5 (h') PIT"
            wits.append((k, nuF, MF, int(kapF), lam_k))
            if len(wits) >= 4: return wits, False
    return wits, (not any_periodic_pass)

def run_tails3():
    print("== tails3: case-III structural admissibility (SHEET6-III.md) ==")
    print("filters: N1 gcd(kap,nu)=1 [Def 3.1+Not 3.4/3.5]; E5-corrected "
          "(g')/(h') => lambda_III >= ceil(mu(kap-rho)/nu) [H5a/H5b + AF2]")
    rows = []
    for lam_t, budget in [(3, 1), (4, 2), (5, 3), (6, 4)]:
        for name, Lam, sanct, node in entry_nodes(lam_t):
            r = bash(node, budget)
            for tr, lam in r['open']:
                mm = _re2.match(r"mu=(\d+) III: s-dependent", tr[-1])
                if not mm: continue
                nd = parse_node(tr[-1])
                if nd is None: continue
                tag = f"td{lam_t}:{name}" + ("" if sanct else "/ext")
                rows.append((tag, budget, nd, int(mm.group(1)), lam))
    seen, summary = set(), {}
    for tag, budget, nd, mu, lam in sorted(rows, key=lambda x: (str(x[2].shape()), x[3], x[1]-x[4])):
        key = (nd.shape(), mu, budget - lam, tag)
        if key in seen: continue
        seen.add(key)
        B = budget - lam
        lock = is_locked(nd)
        Lam3 = mu*nd.rho if lock else None
        shp = f"({nd.rho},{lf_str(nd.nu)},{nd.M},{lf_str(nd.kap)})"
        head = f"[{tag}] {shp} mu={mu} spent={lam} B_rem={B} " \
               f"{'LOCK Lam=' + str(Lam3) if lock else 'UNLOCKED'}"
        if budget_kill_all_s(nd, mu, B, smin=0):
            verdict = f"KILL-BUDGET-E5 (lambda_III >= ceil({Lam3 if lock else 'Lam(s)'}) > {B} for all s)"
        else:
            R, killed = n1_residues(nd.nu, nd.kap)
            n1txt = f"N1 kills s mod {R} in {killed}" if killed else "N1 silent"
            if len(killed) == R:
                verdict = f"KILL-N1 (all residues mod {R})"
            elif lock:
                wits, certified = cong_survivors(nd, mu, B)
                if not wits and certified:
                    verdict = f"KILL-CONG (no (k,nuF) class; certified); {n1txt}"
                elif not wits:
                    verdict = f"NO-WITNESS<=600 (uncertified); {n1txt}"
                else:
                    w = ", ".join(f"k={k},nuF={nf},MF={mf},kapF={kf},lam={lk}"
                                  for k, nf, mf, kf, lk in wits[:2])
                    verdict = f"SURVIVES-EXTRACTION ({n1txt}; residual: {w}, ...)"
            else:
                verdict = f"UNLOCKED-OPEN; {n1txt}"
        print(f"{head}\n    -> {verdict}")
        skey = (nd.shape(), mu)
        best = summary.get(skey)
        if best is None or B > best[0]:
            summary[skey] = (B, verdict.split(' ')[0], tag)
    kb = sum(1 for v in summary.values() if v[1].startswith('KILL'))
    sv = sum(1 for v in summary.values() if v[1].startswith('SURVIVES'))
    print(f"\n== shape summary (weakest-budget occurrence) == "
          f"{len(summary)} (shape,mu) pairs: {kb} KILLED, {sv} SURVIVE, "
          f"{len(summary)-kb-sv} other")
    for (shp, mu), (B, v, tag) in sorted(summary.items(), key=lambda x: str(x)):
        rho, nu, M, kap = shp
        print(f"  ({rho},{lf_str(nu)},{M},{lf_str(kap)}) mu={mu} maxB={B}: {v}  [{tag}]")

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

# ------------------------------------- tduniform: general-td stage (additive)
# SHEET6-TDUNIFORM.md. Leaf table at arbitrary td (single pole: Lambda = td):
#   (D,Dg) = a(alpha,beta), (P,Pg) = b(alpha,beta), a,b in N*   [St 5.2(i)]
#   (A) nu|alpha, nu|b*beta-1  or  (B) nu|beta, nu|b*alpha-1    [St 5.2(ii)]
#   Lambda = a*b*alpha*beta/nu                                  [Prop 5.6 (19)]
# Entry pin (AF3): M = gcd(b*alpha, b*beta) = b; b=1 => Prop 8.4 entry-death.
# N1 at entry (SHEET6-III, H5a): gcd(a, nu) = 1.

def tdu_rows(td):
    """All multiplicity data with Lambda == td. Bounds: beta <= td (Prop 5.7),
    b*alpha <= td (Lambda >= a*b*alpha since nu <= beta), nu <= beta."""
    rows = set()
    for beta in range(3, td + 1):
        for alpha in range(2, beta):
            if gcd(alpha, beta) != 1:
                continue
            for b in range(1, td // alpha + 1):
                for nu in range(1, beta + 1):
                    okA = alpha % nu == 0 and (b * beta - 1) % nu == 0
                    okB = beta % nu == 0 and (b * alpha - 1) % nu == 0
                    if not (okA or okB):
                        continue
                    num = b * alpha * beta
                    assert num % nu == 0, "Lambda integrality"
                    lam1 = num // nu
                    if lam1 > td or td % lam1:
                        continue
                    a = td // lam1
                    rows.add(((alpha, beta), (a * alpha, a * beta),
                              (b * alpha, b * beta), nu, td))
    return sorted(rows)

def tdu_gate():
    """tdu_rows must reproduce prop91's table sliced by Lambda for td <= 7,
    and the prime-td closed form (SHEET6-TDUNIFORM §2): rows at prime p are
    exactly {(alpha,p): alpha | p-1, nu=alpha, a=b=1}, all with b=1."""
    full = prop91(Lmax=7)
    for td in range(3, 8):
        want = sorted(r for r in full if r[4] == td)
        got = tdu_rows(td)
        assert got == want, f"TDU GATE FAIL at td={td}: {got} vs {want}"
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        want = [((al, p), (al, p), (al, p), al, p)
                for al in range(2, p) if (p - 1) % al == 0]
        assert tdu_rows(p) == want, f"TDU GATE FAIL: prime menu at {p}"
    return ("TDU GATE PASS: tdu_rows == prop91 slices td=3..7; prime-td "
            "closed form verified for the 11 primes <= 40")

def tdu_entry_nodes(td):
    """(tag, row, verdict, node|None): pin + N1 entry filter at Lambda=td."""
    out = []
    for (al, be), (D, Dg), (P, Pg), nu, Lam in tdu_rows(td):
        a, b = D // al, P // al
        assert gcd(P, Pg) == b * gcd(al, be) == b, "pin arithmetic"
        tag = f"({al},{be})a{a}b{b}nu{nu}"
        pole_node = Node(Fr(D, P), nu, b, D + Dg, P)
        # Pole metadata certifies nonroot independently of its Q-signature.
        if dispose_m1(pole_node, certified_nonroot=True) == KILL_NR_M1:
            out.append((tag, (al, be, a, b, nu), 'DEAD_PIN', None))
        elif gcd(a, nu) != 1:
            out.append((tag, (al, be, a, b, nu), 'DEAD_N1', None))
        else:
            out.append((tag, (al, be, a, b, nu), 'LIVE',
                        pole_node))
    return out

def tdu_scan(tdmax=40, bashmax=0, step1=True):
    """Per-td census: pin/N1 deaths + live entries; optional step-1 pricing
    (min continuation cost under the promoted kill set) and full compose-run
    for td <= bashmax (see tdu_bash)."""
    import hiii_compose as hcmp          # lazy: hiii_compose imports us
    # TDU-REVIEW C1 fix: under `python3 cases/sheet6_campaign.py` this module
    # is __main__, but hiii_compose re-imports it as 'sheet6_campaign' -- a
    # second copy whose IIB_DERIVED stays False. Set the flag on BOTH.
    import sys as _sys
    for _m in (_sys.modules.get('sheet6_campaign'), _sys.modules.get('__main__')):
        if _m is not None and hasattr(_m, 'IIB_DERIVED'):
            _m.IIB_DERIVED = True
    globals()['IIB_DERIVED'] = True      # AF2-derived IIb pricing (promoted)
    grand = {}
    for td in range(3, tdmax + 1):
        ents = tdu_entry_nodes(td)
        dead_pin = sum(1 for e in ents if e[2] == 'DEAD_PIN')
        dead_n1 = sum(1 for e in ents if e[2] == 'DEAD_N1')
        live = [e for e in ents if e[2] == 'LIVE']
        print(f"td={td:2d}: rows={len(ents):3d} pin_dead={dead_pin:3d} "
              f"n1_dead={dead_n1:2d} live={len(live):2d}"
              + ("  <== ALL DEAD AT ENTRY" if not live else ""))
        grand[td] = (len(ents), dead_pin, dead_n1, len(live))
        if not step1:
            continue
        budget = td - 2
        hcmp.KMAX = budget               # k extra roots cost >= k
        hcmp.BUDGET_CAP = budget         # III-child lambda cap
        for tag, row, _, node in live:
            outs = hcmp.step_e5(node)
            affordable = [o for o in outs if o[0] == 'CONT' and o[1] <= budget]
            roots = [o for o in affordable if dispose_constructed_child(o[2])
                     in (TERMINAL_ROOT_M1, TERMINAL_ROOT_M_GT1)]
            conts = [(o[1], o[2]) for o in affordable
                     if dispose_constructed_child(o[2]) == KEEP]
            opens = [o for o in outs if o[0] in ('OPEN', 'OPEN_E5U')]
            ivs = [o for o in outs if o[0] == 'TERMINAL_IV']
            minlam = min((l for l, _ in conts), default=None)
            free = sum(1 for l, _ in conts if l == 0)
            print(f"    [{tag}] M={node.M} kap={lf_str(node.kap)} "
                  f"budget={budget}: cont={len(conts)} minlam={minlam} "
                  f"free={free} root={len(roots)} opens={len(opens)} "
                  f"iv@entry={len(ivs)}"
                  + ("  STEP1-DEAD" if not conts and not roots and not opens else ""))
    print("\n== census == td: rows / pin-dead / n1-dead / live")
    for td, (r, p, n, l) in grand.items():
        print(f"  {td:2d}: {r:3d} {p:3d} {n:2d} {l:2d}")
    return grand

def tdu_bash(td, maxdepth=7, show=10):
    """Full promoted-kill-set chain run (compose-style: E5 III + N1 + AF2 IIb
    + H3q IV dispositions) for every live entry at Lambda=td, budget td-2.
    Budget dispositions are conditional on the accepted Section 7 weighted
    inequality / first-separation ledger."""
    import hiii_compose as hcmp
    import h3_check as hc
    import sys as _sys
    for _m in (_sys.modules.get('sheet6_campaign'), _sys.modules.get('__main__')):
        if _m is not None and hasattr(_m, 'IIB_DERIVED'):
            _m.IIB_DERIVED = True
    globals()['IIB_DERIVED'] = True
    budget = td - 2
    hcmp.KMAX = budget
    hcmp.BUDGET_CAP = budget
    live = [(t, r, n) for t, r, v, n in tdu_entry_nodes(td) if v == 'LIVE']
    print(f"\n=== tdu_bash td={td}: {len(live)} live entries, "
          f"conditional-Section7 budget={budget}, "
          f"depth<={maxdepth} ===")
    all_surv = {}
    for tag, row, node in live:
        seen = {node.shape(): 0}
        dq_ = deque([(node, 0, [f"ENTRY {node}"])])
        hits, root_hits, opens, frontier, nnodes = [], [], [], 0, 0
        while dq_:
            nd, lam, tr = dq_.popleft()
            nnodes += 1
            if len(tr) - 1 >= maxdepth:
                frontier += 1
                continue
            for o in hcmp.step_e5(nd):
                if o[0] == 'TERMINAL_IV':
                    hits.append((nd, lam, tr))
                elif o[0] == 'OPEN_E5U':
                    _, msg, lmin, mu = o
                    if lam + lmin > budget:
                        continue
                    if budget_kill_all_s(nd, mu, budget - lam):
                        continue
                    opens.append((msg, lam))
                elif o[0] == 'OPEN':
                    lmin = o[2] if len(o) > 2 else 0
                    if lam + lmin > budget:
                        continue
                    opens.append((o[1], lam))
                elif o[0] == 'CONT':
                    _, dl, child, why = o
                    nl = lam + dl
                    if nl > budget:
                        continue
                    disposition = dispose_constructed_child(child)
                    if disposition in (TERMINAL_ROOT_M1, TERMINAL_ROOT_M_GT1):
                        root_hits.append((child.shape(), nl, why, disposition))
                        continue
                    if disposition == KILL_NR_M1:
                        continue
                    assert disposition == KEEP
                    sh = child.shape()
                    if sh in seen and seen[sh] <= nl:
                        continue
                    seen[sh] = nl
                    dq_.append((child, nl, tr + [why]))
        seen_h, n_surv = set(), 0
        for nd, lam, tr in hits:
            key = (nd.shape(), lam)
            if key in seen_h:
                continue
            seen_h.add(key)
            rows, _ = hc.iv_dispositions(nd, lam, td)
            if any(v == 'OPEN_s_tail' for _, v, _ in rows):
                opens.append((f"IV parametric s>{hc.SMAX}: NO_VERDICT at {nd}", lam))
            surv = [(s, R) for s, v, R in rows if v == 'SURVIVOR']
            if surv:
                n_surv += 1
                sk = (str(nd.shape()), lam)
                if sk not in all_surv:
                    all_surv[sk] = (tag, sorted({str(R) for _, R in surv}))
        od = {}
        for msg, lam in opens:
            od.setdefault(_re2.sub(r" at Q\[.*", "", msg), []).append(lam)
        print(f"  [{tag}] nodes={nnodes} iv_hits={len(seen_h)} "
              f"iv_SURV={n_surv} root_hits={len(set(root_hits))} "
              f"open_kinds={len(od)} frontier={frontier}")
        for kmsg, lams in sorted(od.items())[:4]:
            print(f"      OPEN minlam={min(lams)} x{len(lams)} {kmsg[:80]}")
    print(f"  --- td={td} composed IV-survivor (shape,lam) classes: "
          f"{len(all_surv)}")
    for i, (sk, (tag, Rset)) in enumerate(sorted(all_surv.items())):
        if i >= show:
            break
        print(f"    IVSURV[{tag}] lam={sk[1]} shape={sk[0]} R={Rset}")
    return all_surv

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument("phase", nargs="?", default="all")
    ap.add_argument("--budget", type=int, default=4)
    ap.add_argument("--lam", type=int, default=6)
    ap.add_argument("--tdmax", type=int, default=40)
    ap.add_argument("--td", type=int, default=0)
    args = ap.parse_args()
    ph = args.phase
    if ph == "tduniform":
        print(tdu_gate())
        if args.td:
            tdu_bash(args.td)
        else:
            tdu_scan(args.tdmax)
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
                      f"verdict={r['verdict']} iv={len(r['iv'])} root={len(r['root'])} "
                      f"open={len(r['open'])} "
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
                  f"root_terminals={len(r['root'])} opens={len(r['open'])} "
                  f"distinct={len(od)} loops={len(r['loops'])}")
            for (k, nd), lams in sorted(od.items()):
                print(f"  OPEN minlam={min(lams)} x{len(lams)} {k[:80]} | {nd[:70]}")
            for k, lams in sorted(ivshapes.items())[:8]:
                print(f"  IVSHAPE minlam={min(lams)} x{len(lams)} {k[:95]}")
    if ph == "tails3":
        run_tails3()
    if ph in ("bash", "all"):
        print(f"\n=== td=6 bash: single-pole entries Lambda={args.lam}, budget={args.budget} ===")
        for name, Lam, sanct, node in entry_nodes(args.lam):
            r = bash(node, args.budget)
            print(f"[{name}] {'SANC' if sanct else 'ext '} verdict={r['verdict']} "
                  f"iv={len(r['iv'])} root={len(r['root'])} open={len(r['open'])} "
                  f"loops={len(r['loops'])} "
                  f"frontier={len(r['frontier'])}")
            for tr, lam in r['open'][:6]:
                print("    OPEN lam", lam, "|", tr[-1][:110])
            for tr, lam in r['iv'][:4]:
                print("    IV   lam", lam, "|", " => ".join(t[:60] for t in tr[-2:]))
