#!/usr/bin/env python3
"""LL-1 (td=6, m=2) corrected landing-ledger compiler -- R2 packet, 2026-08-29.

Repairs the sealed LL-1 design (xmodel/landing-ledger-primary-research-
fable5-20260829.md, body 83fe2312...) at its first exact discriminator, per
the hostile review (xmodel/landing-ledger-primary-research-fable5-hostile-
review-grok46-20260829.md, body 88c1d66f...):

  R-1  At nu=1 the eta slot `eps_q` is NOT a degree slot.  The legacy record
       `(l, eps_q=1)` is identified with MP6 family I at extra-count
       L = l+1 (with the location flag s(0)=0) BEFORE classification.
       At nu>=2 the slot is forced (R1.0: eta || q).
  R-2  The old Section 5.4 UNCOVERED row and the l<=4 machine-only row are
       replaced by the exact family-I split: odd L => M = gcd(2,L) = 1,
       MP2-dead; even L => D9 log-obstruction, every even L, td-uniform,
       including s(0)=0 (D9's residues sit at the two p-roots and never use
       s(0) != 0).  No td-7 zero-chain extension is invoked.
  R-3  M is derived as gcd(dp,dq) of the CHILD shape at every vertex; the
       clean-axis R1/R2 gcd lines are never cached off the clean axis.
  R-4  One coherent w_cert token set; the admitted IIa merge child is
       W-CLOSED-FORM (DS4 handshake of two W-CLOSED-FORM arrivals against a
       determined cell), not W-PRICED.
  R-5  A2 corrected: UNCOVERED may be empty; failure is an unclassified
       candidate, or an UNCOVERED row already killed by a cited promoted
       theorem.  Caps may only ever produce UNCOVERED.

Arithmetic is exact (int / fractions.Fraction).  No web, no CAS, no
canonical edits.  Everything below is bounded desk-scale computation.

Scope firewall (also emitted into the book): this packet tests the corrected
LL-1 quotient and hand-run at td=6, m=2 only.  It is not a proof that the
candidate grammar equals all geometric configurations, does not bound depth,
and proves no source landing, ceiling, Keller, or JC2 statement.
"""

from fractions import Fraction
import hashlib
import json
import math
import os
import sys

TD = 6
M_POLES = 2

# --------------------------------------------------------------------------
# Frozen trust snapshot (statement-level; per-record cert_chain entries must
# resolve here).  Tiers: printed (thesis statement under promoted reading),
# H1 (Prop 9.3 printed-step arithmetic), promoted (reviewed campaign file).
# The tier `CAP` exists only as a *forbidden* tier: any COVERED/REJECTED/DEAD
# record citing a CAP-tier source must fail validation (caps may only ever
# produce UNCOVERED).
# --------------------------------------------------------------------------
TRUST = {
    "MP1":  {"tier": "promoted", "source": "SHEET6-MULTIPOLE.md MP1 (merge counting; single merge at m=2)"},
    "MP2":  {"tier": "promoted", "source": "SHEET6-MULTIPOLE.md MP2 (nonroot trunk M!=1; root exempt)"},
    "MP4":  {"tier": "promoted", "source": "SHEET6-MULTIPOLE.md MP4/D4 (entry pin; b=1 forced at prime/beta-minimal Lambda)"},
    "MP5":  {"tier": "promoted", "source": "SHEET6-MULTIPOLE.md MP5/D5 (M=1 chain propagation, mu=1 arrivals)"},
    "MP6":  {"tier": "promoted", "source": "SHEET6-MULTIPOLE.md MP6/D6 (merge anatomy; (c) eta absorbed at nu=1; (d) gcd menu; (e) lam=0)"},
    "MP7":  {"tier": "promoted", "source": "SHEET6-MULTIPOLE.md MP7/D7 (l=0 kill; q=p forces deg p=1)"},
    "MP9":  {"tier": "promoted", "source": "SHEET6-MULTIPOLE.md MP9/D9 (m=2 sharpening; interior nu=1 layer)"},
    "D9-LOG": {"tier": "promoted", "source": "SHEET6-MULTIPOLE.md D9 (exact log-obstruction: 2ps'-Lp's=c', residues C(-n,n-1)(a1-a2)^{1-2n}, n=(L+2)/2, all even L, td-uniform)"},
    "St 8.4": {"tier": "printed", "source": "Sigray St 8.4 p.42 (mu_e | M; dirty l | current M)"},
    "St 8.5": {"tier": "printed", "source": "Sigray St 8.5 p.42 (M divisibility down merge-free segments off V_2)"},
    "St 3.16-iff": {"tier": "printed", "source": "Sigray St 3.16 p.17 (V_a iff >1 root; nu=1 chain children excluded)"},
    "Not 3.4": {"tier": "printed", "source": "Sigray Not 3.4 p.12 (nu>=2 => V_1; kbar integral via Not 3.5)"},
    "Prop 8.1(v)": {"tier": "printed", "source": "Sigray Prop 8.1(v) pp.39-41 (M = gcd(dp,dq))"},
    "R1.0": {"tier": "promoted", "source": "BOOK-OFFAXIS.md R1.0 (q-multiplicity rigidity; eta||q at nu>=2 only)"},
    "DS1": {"tier": "promoted", "source": "SHEET6-DEPTH.md DS1 (characteristic rigidity; case II; kbar in Z at nu>=2; depth not (m,td)-bounded)"},
    "DS2": {"tier": "promoted", "source": "SHEET6-DEPTH.md DS2 (w_F = w_G * n/Delta; neutral steps conserve w)"},
    "DS3": {"tier": "promoted", "source": "SHEET6-DEPTH.md DS3 (resonance Delta | num(w); finite closure W(w0))"},
    "DS4": {"tier": "promoted", "source": "SHEET6-DEPTH.md DS4 5a-5b (handshake kbar-D/i=w; cells finite per w; child data from (w,cell))"},
    "DEPTH-5c": {"tier": "promoted", "source": "SHEET6-DEPTH.md 5c (ZCH 0-edge is case III; join w_other = nu_e * w_0chain, nu_e>=2)"},
    "DEPTH-5d": {"tier": "promoted", "source": "SHEET6-DEPTH.md 5d (root merge case I; X=mu(1-w); all-mu=1: w=l/(r+l) in (0,1); root M=1 legal)"},
    "MRW": {"tier": "promoted", "source": "BOOK-OFFAXIS.md header 2026-08-28 + MULTIPOLE header (mixed-root window: X_R=mu_e(1-w_e), 0<w_e<1, no mu=1 hypothesis)"},
    "R2.1": {"tier": "promoted", "source": "BOOK-OFFAXIS.md R2.1 (generalized handshake; equal-mu equal-w; case-III form)"},
    "R2.2": {"tier": "promoted", "source": "BOOK-OFFAXIS.md R2.2 (searrow law; NE strict; root-mult law; M=gcd)"},
    "P0": {"tier": "promoted", "source": "BOOK-OFFAXIS.md sec.10 P0 (priced step menu; AF2 lam rule; finiteness E <= l*num(w)*T; pure-b collapse; menu completeness per state CITED, not re-proved here)"},
    "P1": {"tier": "promoted", "source": "BOOK-OFFAXIS.md sec.10 P1 / H3-psi (terminal psi = ceil(1/(1-w))-1; j = M(1-w) in N*; shared St 9.4 budget)"},
    "St 9.4": {"tier": "printed", "source": "Sigray St 9.4 (25)/(26) p.49 (Sum lam <= td-1-psi)"},
    "AF2": {"tier": "promoted", "source": "SHEET6-AF2 sec.2 as consumed by BOOK-OFFAXIS P0 (lam price per NE orbit / free 0-root)"},
    "T7": {"tier": "promoted", "source": "REDUCTION.md T7 (entry menu; Lambda = a b alpha beta / nu; nu-menu; SOL-PROP58/Chau every-fibre)"},
    "OFFAXIS-EMPTY-TD6": {"tier": "promoted", "source": "BOOK-OFFAXIS.md sec.4 (td=6: off-axis sector EMPTY, 0 raw entries) + MP4 (Lambda=3 prime forces b=1)"},
    "MP6(b)": {"tier": "promoted", "source": "SHEET6-MULTIPOLE.md MP6(b) (equal-quotient law deg p_H = i*mu_e)"},
    "St 3.18": {"tier": "printed", "source": "Sigray St 3.18 p.18 (one continuation per orbit; q-extras carry no tree vertex)"},
    "SYN-1": {"tier": "CAP", "source": "SYNTHETIC probe hypothesis -- deliberately absent from the promoted perimeter"},
}
ALLOWED_TIERS = ("printed", "H1", "promoted")

# w_cert: ONE coherent token set (repair R-4).  R7 root kills fire only on
# ROOT_KILL_CERTS; W-SYMBOLIC never kills.
W_CLOSED_FORM = "W-CLOSED-FORM"
W_PRICED_COMPLETE = "W-PRICED-COMPLETE"
W_SYMBOLIC = "W-SYMBOLIC"
W_CERT_TOKENS = (W_CLOSED_FORM, W_PRICED_COMPLETE, W_SYMBOLIC)
ROOT_KILL_CERTS = (W_CLOSED_FORM, W_PRICED_COMPLETE)

CLASSIFICATIONS = ("COVERED", "TERMINAL", "UNCOVERED")
VERDICTS = ("ADMITTED", "REJECTED", "DEAD", "UNREACHABLE", "ALIVE",
            "ALIVE_FRAGILE", "NA")


class LLError(Exception):
    """Fail-closed error (raised, never assert-based: survives python -O)."""


def frac(x, y=1):
    return Fraction(x, y)


def is_pos_int(x):
    return isinstance(x, Fraction) and x.denominator == 1 and x > 0


def ceil_frac(x):
    return -((-x.numerator) // x.denominator)


def cert(*rule_ids):
    """Build a cert_chain from TRUST; unknown id -> fail closed."""
    out = []
    for rid in rule_ids:
        if rid not in TRUST:
            raise LLError("cert id not in frozen trust snapshot: %r" % rid)
        out.append({"rule": rid, "tier": TRUST[rid]["tier"],
                    "source": TRUST[rid]["source"]})
    return out


# ==========================================================================
# R0: entry layer (T7 arithmetic, exact; MP4 forcing)
# ==========================================================================

def entry_menu(td=TD, m=M_POLES):
    """Derive the complete entry menu at (td, m) from the T7 arithmetic.

    Returns (entries, offaxis_entries).  At td=6, m=2 the on-axis menu has
    exactly one member and the off-axis menu is empty (Lambda=3 prime forces
    b=1 by MP4; cross-checked against BOOK-OFFAXIS sec.4's recorded 0 raw
    entries).
    """
    entries = []
    offaxis = []
    # partitions td = sum Lambda_i, Lambda_i >= beta >= 3, m parts (ordered
    # multisets; here m=2)
    if m != 2:
        raise LLError("packet is fixed at m=2")
    for lam1 in range(3, td - 2):
        lam2 = td - lam1
        if lam2 < 3 or lam1 > lam2:
            continue
        # type (alpha,beta): 2 <= alpha < beta coprime, Lambda_i >= beta
        for beta in range(3, min(lam1, lam2) + 1):
            for alpha in range(2, beta):
                if math.gcd(alpha, beta) != 1:
                    continue
                # per-pole (a,b,nu): Lambda = a*b*alpha*beta/nu ; T7 nu-menu
                pole_rows = []
                for lam in (lam1, lam2):
                    rows = []
                    for b in range(1, td + 1):
                        for a in range(1, td + 1):
                            for nu in range(1, a * b * alpha * beta + 1):
                                if a * b * alpha * beta != lam * nu:
                                    continue
                                menu1 = (alpha % nu == 0) and ((b * beta - 1) % nu == 0)
                                menu2 = (beta % nu == 0) and ((b * alpha - 1) % nu == 0)
                                if not (menu1 or menu2):
                                    continue
                                # MP4 forcing: beta-minimal (Lambda == beta)
                                # or prime Lambda forces b = 1
                                lam_prime = lam > 1 and all(lam % p for p in range(2, lam))
                                if (lam == beta or lam_prime) and b != 1:
                                    continue
                                rows.append((a, b, nu))
                    pole_rows.append(rows)
                for r1 in pole_rows[0]:
                    for r2 in pole_rows[1]:
                        e = {"Lambda": (lam1, lam2), "type": (alpha, beta),
                             "poles": (r1, r2)}
                        if r1[1] >= 2 or r2[1] >= 2:
                            offaxis.append(e)
                        else:
                            entries.append(e)
    return entries, offaxis


def entry_frame(entry):
    """R0 output frame per pole: kbar = a(alpha+beta); derived M=b, rho=a/b,
    w0 = a(b(alpha+beta)-1)/(b nu); w_cert = W-CLOSED-FORM."""
    alpha, beta = entry["type"]
    frames = []
    for (a, b, nu) in entry["poles"]:
        kbar = frac(a * (alpha + beta))
        M = b
        rho = frac(a, b)
        w0 = frac(a * (b * (alpha + beta) - 1), b * nu)
        frames.append({"a": a, "b": b, "nu": nu, "kbar": kbar, "M": M,
                       "rho": rho, "w0": w0, "w_cert": W_CLOSED_FORM})
    return frames


# ==========================================================================
# DS3: finite w-closure
# ==========================================================================

def w_closure(w0):
    """W(w0): closure of {w0} under w -> w*n/Delta, Delta | num(w),
    Delta >= 3, Delta = (n-1)nu+1, n >= 2, nu >= 2 (DS3, exact)."""
    seen = set()
    todo = [Fraction(w0)]
    while todo:
        w = todo.pop()
        if w in seen:
            continue
        seen.add(w)
        a = w.numerator
        for Delta in range(3, a + 1):
            if a % Delta:
                continue
            # factor Delta - 1 = (n-1)*nu, n >= 2, nu >= 2
            for nu in range(2, Delta):
                if (Delta - 1) % nu:
                    continue
                n = (Delta - 1) // nu + 1
                if n < 2:
                    continue
                todo.append(w * n / Delta)
    return sorted(seen)


# ==========================================================================
# Repair R-1: nu=1 normalization (the corrected quotient)
# ==========================================================================

def normalize_nu1_merge(r, l=None, eps_q=None, L=None, q0_zero=None,
                        dp=None, dq=None):
    """Normalize any nu=1 all-mu=1 interior-merge presentation to the family-I
    normal form (r, L, q0_zero).

    Accepted presentations (exactly the duplicate parametrizations of the
    sealed grammar, plus raw degrees):
      * legacy (l, eps_q):    q = eta^eps_q * p * s~, deg s~ = l
                              => family I with L = l + eps_q, q0_zero = eps_q=1
      * family I (L, q0_zero): q = p * s, deg s = L, s(0)=0 iff q0_zero
      * raw (dp, dq):          L = dq - dp  (location flag unknown -> None)

    One-line degree identification (MP6(c): eta absorbed at nu=1): the legacy
    eta-factor record IS family I at extra-count L = l + 1 with s(0) = 0;
    whether q(0)=0 is a root-location predicate on the extras, not a degree
    increment.
    """
    if l is not None:
        if eps_q not in (0, 1):
            raise LLError("legacy nu=1 record needs eps_q in {0,1}")
        Lval, flag = l + eps_q, bool(eps_q)
    elif L is not None:
        Lval, flag = L, bool(q0_zero) if q0_zero is not None else False
    elif dp is not None and dq is not None:
        if dp != r:
            raise LLError("family I has dp = r")
        Lval, flag = dq - dp, None
    else:
        raise LLError("no recognizable nu=1 presentation")
    if Lval < 0:
        raise LLError("negative extra-count")
    return {"family": "I", "r": r, "L": Lval, "q0_zero": flag,
            "dp": r, "dq": r + Lval}


# ==========================================================================
# Repair R-2: the D9 log-obstruction, reconstructed from the licensed source
# (SHEET6-MULTIPOLE.md D9), with exact machine verification.
# ==========================================================================

def binom_neg(n, k):
    """C(-n, k) as an exact integer-valued Fraction."""
    out = Fraction(1)
    for i in range(k):
        out *= Fraction(-n - i, i + 1)
    return out


def poly_mul(p, q):
    out = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def poly_deriv(p):
    return [c * i for i, c in enumerate(p)][1:] or [Fraction(0)]


def d9_operator(L, a1, a2, s):
    """T(s) = 2 p s' - L p' s  with p = (t-a1)(t-a2), coefficients exact."""
    p = poly_mul([Fraction(-a1), Fraction(1)], [Fraction(-a2), Fraction(1)])
    pp = poly_deriv(p)
    t1 = poly_mul(p, poly_deriv(s))
    t2 = poly_mul(pp, s)
    n = max(len(t1), len(t2))
    t1 += [Fraction(0)] * (n - len(t1))
    t2 += [Fraction(0)] * (n - len(t2))
    return [2 * x - L * y for x, y in zip(t1, t2)]


def solve_linear(rows, rhs):
    """Exact Gaussian elimination over Q.  rows: list of coefficient lists.
    Returns (solvable, one_solution_or_None, kernel_dim)."""
    m = len(rows)
    n = len(rows[0]) if m else 0
    A = [list(r) + [rhs[i]] for i, r in enumerate(rows)]
    piv_cols = []
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, m):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        piv_cols.append(c)
        r += 1
        if r == m:
            break
    for i in range(r, m):
        if A[i][n] != 0:
            return False, None, n - len(piv_cols)
    sol = [Fraction(0)] * n
    for i, c in enumerate(piv_cols):
        sol[c] = A[i][n]
    return True, sol, n - len(piv_cols)


def d9_ode_status(L, a1, a2, force_s0_zero=False, max_extra_deg=2):
    """Exact status of  2 p s' - L p' s = c'  (c' a nonzero constant) over
    polynomial s, deg s <= L + max_extra_deg, p = (t-a1)(t-a2), a1 != a2.

    Returns dict with:
      solvable_nonzero_c : bool  (does some s give a NONZERO constant RHS?)
      witness            : (s coeffs, c) if solvable else None
    D9's log-obstruction asserts solvable_nonzero_c == False for every even
    L >= 2 (and the root/interior l=1 case is solvable -- positive control).
    The s(0)=0 restriction (force_s0_zero) is a subspace, hence automatically
    covered when the unrestricted problem is unsolvable; it is exposed here
    so the mutation battery can test it explicitly.
    """
    if a1 == a2:
        raise LLError("p must have distinct roots")
    deg = L + max_extra_deg
    ncols = deg + 1
    # unknowns: s_0..s_deg ; equation T(s) = c  <=>  T(s) - c = 0 in each
    # coefficient; c is an extra unknown pinned to 1 (solve T(s) = 1: any
    # nonzero c rescales).
    rows = []
    rhs = []
    outlen = deg + 2  # deg of T(s) <= deg+1
    basis_images = []
    for j in range(ncols):
        e = [Fraction(0)] * ncols
        e[j] = Fraction(1)
        img = d9_operator(L, a1, a2, e)
        img += [Fraction(0)] * (outlen - len(img))
        basis_images.append(img)
    for k in range(outlen):
        row = [basis_images[j][k] for j in range(ncols)]
        rows.append(row)
        rhs.append(Fraction(1) if k == 0 else Fraction(0))
    if force_s0_zero:
        rows.append([Fraction(1)] + [Fraction(0)] * (ncols - 1))
        rhs.append(Fraction(0))
    ok, sol, kdim = solve_linear(rows, rhs)
    return {"solvable_nonzero_c": ok,
            "witness": sol if ok else None,
            "kernel_dim": kdim}


def d9_kernel_is_p_power(L, a1, a2):
    """For even L the kernel of T is exactly span{p^{L/2}} (c=0 branch)."""
    p = poly_mul([Fraction(-a1), Fraction(1)], [Fraction(-a2), Fraction(1)])
    pk = [Fraction(1)]
    for _ in range(L // 2):
        pk = poly_mul(pk, p)
    img = d9_operator(L, a1, a2, pk)
    return all(c == 0 for c in img)


def d9_residue_check(n, a1, a2):
    """Residue of p^{-n} at a1 equals C(-n, n-1) (a1-a2)^{1-2n} and is
    nonzero for n >= 2 (exact; this is the licensed D9 residue law)."""
    # residue = (1/(n-1)!) d^{n-1}/dt^{n-1} (t-a2)^{-n} at t=a1
    # computed exactly from falling factorials:
    val = Fraction(1)
    for i in range(n - 1):
        val *= Fraction(-n - i, i + 1)
    direct = val * Fraction(1) * (Fraction(a1 - a2)) ** (1 - 2 * n)
    closed = binom_neg(n, n - 1) * (Fraction(a1 - a2)) ** (1 - 2 * n)
    sign_form = ((-1) ** (n - 1)) * math.comb(2 * n - 2, n - 1)
    return {"direct": direct, "closed": closed,
            "match": direct == closed,
            "binom_sign_form": sign_form,
            "nonzero": closed != 0 and sign_form != 0}


def classify_family_I(r, L, q0_zero=None):
    """Corrected family-I classifier at an interior nu=1 all-mu=1 merge,
    r=2 (this header).  Returns a record fragment (no UNCOVERED rows: the
    split is exact and theorem-backed for every L >= 0)."""
    if r != 2:
        raise LLError("packet header has r=2")
    nf = {"family": "I", "r": r, "L": L, "q0_zero": q0_zero,
          "dp": r, "dq": r + L}
    M = math.gcd(r, r + L)  # = gcd(2, L)
    if L == 0:
        return {"normal_form": nf, "M": M, "classification": "COVERED",
                "verdict": "REJECTED",
                "why": "l=0: q=p forces p'=const!=0 i.e. deg p=1, contradiction",
                "cert_chain": cert("MP7")}
    if L % 2 == 1:
        return {"normal_form": nf, "M": M, "classification": "COVERED",
                "verdict": "DEAD",
                "why": "odd L: M=gcd(2,L)=1 at an interior trunk vertex",
                "cert_chain": cert("MP6", "Prop 8.1(v)", "MP2")}
    # even L: D9 log-obstruction, td-uniform, s(0)=0 included
    n = (L + 2) // 2
    return {"normal_form": nf, "M": M, "classification": "COVERED",
            "verdict": "DEAD",
            "why": ("even L: exact log-obstruction; (s p^{-L/2})' = "
                    "(c'/2) p^{-(L+2)/2} has nonzero residue "
                    "C(-n,n-1)(a1-a2)^{1-2n}, n=%d, at each p-root; "
                    "s(0)=0 included (D9 never uses s(0)!=0)" % n),
            "d9_n": n,
            "cert_chain": cert("MP6", "D9-LOG")}


# ==========================================================================
# Merge layer: IIa uniqueness (theorem, not sweep), ZCH, root, mixed
# ==========================================================================

def iia_cell(nu, l, w):
    """IIa cell data at r=2, all-mu=1: dp=2nu, dq=(2+l)nu+1; child from
    (w, cell) alone (DS4 5a)."""
    dp = 2 * nu
    dq = (2 + l) * nu + 1
    Delta = dq - dp
    kbar = Fraction(w) * dq / Delta
    X = Fraction(w) * dp / Delta
    M = math.gcd(dp, dq)
    return {"nu": nu, "l": l, "dp": dp, "dq": dq, "kbar": kbar, "X": X,
            "M": M}


def iia_admitted(w=Fraction(2)):
    """The complete IIa survivor list at w=2 with the exact uniqueness
    derivation:  M=2 needs l*nu odd; kbar = 2 + 4nu/d, d = l*nu+1;
    kbar in Z (DS1(c)) => d | 4nu, gcd(d,nu)=1 => d | 4; l*nu odd => d even
    >= 4 => d = 4 => l*nu = 3 => (nu,l) = (3,1) (nu >= 3 odd).  Returns
    (admitted_cells, derivation_string, spot_failures)."""
    if w != 2:
        raise LLError("header alphabet is W={2}")
    admitted = []
    cell = iia_cell(3, 1, w)
    if cell["kbar"].denominator != 1 or cell["M"] != 2:
        raise LLError("IIa (2,3,1) recomputation failed")
    child = {
        "Q": (6, 12, 3, 2, 5),  # (D, deg p, nu, M, kbar) at i=2
        "i": 2,
        "w_trunk": (cell["kbar"] - cell["X"] / cell["dp"]) / cell["nu"],
        "w_cert": W_CLOSED_FORM,  # repair R-4: DS4 handshake of two
                                  # W-CLOSED-FORM arrivals, NOT W-PRICED
    }
    if child["w_trunk"] != Fraction(3, 2):
        raise LLError("w_trunk recomputation failed")
    if (child["Q"][0] != child["i"] * cell["X"]
            or child["Q"][1] != child["i"] * cell["dp"]
            or child["Q"][4] != cell["kbar"]):
        raise LLError("Q-datum recomputation failed")
    admitted.append({"cell": cell, "child": child})
    derivation = ("M=gcd(2,l*nu+1)=2 <=> l*nu odd; kbar=2+4nu/(l*nu+1) in Z "
                  "(DS1(c)) <=> (l*nu+1)|4nu <=> (l*nu+1)|4 (coprime) "
                  "=> l*nu+1=4 => (nu,l)=(3,1)")
    spot = []
    for (nu, l) in ((5, 1), (3, 3), (7, 1), (5, 3)):
        c = iia_cell(nu, l, w)
        spot.append({"nu": nu, "l": l, "kbar": str(c["kbar"]),
                     "integral": c["kbar"].denominator == 1})
    if any(s["integral"] for s in spot):
        raise LLError("spot-check found an unexpected integral IIa cell")
    return admitted, derivation, spot


def join_handshake(w_arrivals):
    """DS4 5a / R2.1(i): every non-0 mu=1 edge satisfies kbar_G - D_G/i =
    w_e, so a join is admissible only when all arriving certified w agree.
    Raises LLError on an unequal equal-mu join (negative control R4(a))."""
    ws = {Fraction(w) for w in w_arrivals}
    if len(ws) != 1:
        raise LLError("equal-mu join with unequal w %s rejected (R2.1(i))"
                      % sorted(map(str, ws)))
    return ws.pop()


def step_legal(l, M_current):
    """St 8.4: a priced (dirty) step's arriving mult l must divide the
    CURRENT M-state (never the entry b -- the l|b conflation produced the
    refuted W_off alphabet)."""
    return l >= 2 and M_current % l == 0


def zch_join(w_alphabet):
    """DEPTH 5c corrected case-III join: w_other = nu_e * w_0chain with
    nu_e >= 2.  Returns solutions over the (finite) alphabet."""
    sols = []
    for w0 in w_alphabet:
        for wo in w_alphabet:
            q = Fraction(wo) / Fraction(w0)
            if q.denominator == 1 and q >= 2:
                sols.append((w0, wo, int(q)))
    return sols


def root_meet(w_arrivals):
    """Case-I root meet (DEPTH 5d + mixed-root window): every actual searrow
    parent edge requires 0 < w_e < 1; kills fire only on ROOT_KILL_CERTS.
    l=0 at the root is impossible (0 = theta*p).  Root M=1 is legal."""
    rows = []
    for (w, wc) in w_arrivals:
        if wc not in W_CERT_TOKENS:
            raise LLError("unknown w_cert token %r" % wc)
        killed = (wc in ROOT_KILL_CERTS) and not (0 < Fraction(w) < 1)
        rows.append({"w": Fraction(w), "w_cert": wc, "window_kill": killed})
    return rows


def root_local_cell(r, l):
    """All-mu=1 r-way root meet local record: (dp,dq)=(r,r+l), l>=1,
    w = l/(r+l) in (0,1), M_root = gcd(r,r+l) (M=1 LEGAL at the root)."""
    if l < 1:
        raise LLError("l=0 impossible at the root (0 = theta*p, D9 root clause)")
    return {"dp": r, "dq": r + l, "w": Fraction(l, r + l),
            "M_root": math.gcd(r, r + l), "root_M1_legal": True}


# ==========================================================================
# Suffix layer: P0 priced steps (menu completeness per state cited to P0),
# terminals (P1), budget (St 9.4)
# ==========================================================================

def af2_price(X, kbar, nu, eps, mults):
    """AF2 lam price: sum_j max(1, ceil(X/m_j - kbar)) +
    [eps>=1] * max(1, ceil((X/eps - kbar)/nu))."""
    lam = 0
    for m in mults:
        lam += max(1, ceil_frac(Fraction(X) / m - kbar))
    if eps >= 1:
        lam += max(1, ceil_frac((Fraction(X) / eps - kbar) / nu))
    return lam


def dirty_cells(w, l, lam_cap):
    """Complete priced non-neutral step menu at a chain vertex of state w
    with arriving mult l (l >= 2, l | current M checked by caller).

    Soundness of every emitted cell is first-principles (kbar in Z at nu>=2,
    strict NE laws, root-mult law, searrow, dq = 1 mod nu).  COMPLETENESS of
    the enumeration window is the cited P0 certificate: extras-present cells
    have C = l(k+lex) - Sum m >= 1 (P0; C=0 with k+lex>=1 contradicts the
    strict NE law), T = Sum m + l - eps(1+k+lex) >= 1 (T=0 is dp=eps*dq,
    excluded by root-mult (R)), and E = nu*C + (l-eps) <= l*num(w)*T.
    Pure-(b) (C=0) is returned separately as a parametric family.

    lam_cap prunes only by the budget (k + [eps>=1] <= lam <= lam_cap);
    this is a budget bound, not an engine cap.
    """
    w = Fraction(w)
    a = w.numerator
    cells = []
    pure_b = []
    for eps in range(0, l):
        # pure-(b): k = lex = Sum m = 0, 1 <= eps <= l-1  (P0(ii))
        if eps >= 1:
            lam_min = ceil_frac(l * w / eps)
            wF = l * w / Fraction(l - eps) if l != eps else None
            pure_b.append({"eps": eps, "w_child": wF,
                           "lam_min": lam_min,
                           "M_menu": "gcd(l-eps, nu+1) over nu>=2 "
                                     "(= every divisor of l-eps)",
                           "M_divisors": sorted(
                               d for d in range(1, l - eps + 1)
                               if (l - eps) % d == 0)})
        for k in range(0, lam_cap + 2):
            if k + (1 if eps >= 1 else 0) > lam_cap:
                break
            # multisets of k NE mults, each 1..l-1 (m_j < dp/dq < l)
            def multisets(kk, lo):
                if kk == 0:
                    yield ()
                    return
                for m0 in range(lo, l):
                    for rest in multisets(kk - 1, m0):
                        yield (m0,) + rest
            for mults in multisets(k, 1):
                Sm = sum(mults)
                for lex in range(0, 3 * l * a + 4):
                    C = l * (k + lex) - Sm
                    if C < 1:
                        continue
                    T = Sm + l - eps * (1 + k + lex)
                    if T < 1:
                        break  # T decreases in lex (eps>=1); eps=0 has T fixed>0
                    numax = l * a * T - (l - eps)
                    if numax < 2 * C:
                        continue
                    for nu in range(2, numax // C + 1):
                        E = nu * C + (l - eps)
                        dq = (1 + k + lex) * nu + 1
                        dp = eps + nu * (l + Sm)
                        if l * dq - dp != E or E <= 0:
                            raise LLError("E bookkeeping failure")
                        kbar = l * w * dq / E
                        if kbar.denominator != 1 or kbar < 1:
                            continue
                        # strict NE laws + root-mult law (R)
                        if eps >= 1 and not eps * dq < dp:
                            continue
                        if any(not m * dq < dp for m in mults):
                            continue
                        if any(dp == mu * dq for mu in (l,) + mults):
                            continue
                        X = kbar * dp / Fraction(dq)
                        lam = af2_price(X, kbar, nu, eps, mults)
                        if lam > lam_cap:
                            continue
                        wF = l * w * (dq - 1) / (nu * E)
                        M = math.gcd(dp, dq)  # repair R-3: gcd of CHILD shape
                        cells.append({
                            "l": l, "eps": eps, "k": k, "mults": list(mults),
                            "lex": lex, "nu": nu, "dp": dp, "dq": dq,
                            "E": E, "kbar": kbar, "X": X, "lam": lam,
                            "w_child": wF, "M_child": M,
                            "rule": "R2" if (k == 0 and eps == 0) else "R3",
                        })
    cells.sort(key=lambda c: (c["dp"], c["dq"], c["nu"], c["eps"], c["lex"]))
    return cells, pure_b


def neutral_reachable_M(M):
    """Neutral thick steps l | M, n=1: child M' = gcd(l, nu+1) (gcd of the
    clean CHILD shape (l*nu, nu+1)); over nu >= 2 this reaches exactly the
    divisors of each l | M, i.e. every divisor of M.  w is conserved (DS2)."""
    return sorted(d for d in range(1, M + 1) if M % d == 0)


def terminal(w, M, td=TD):
    """R8/R9 terminal record: needs w < 1, M >= 2, j = M(1-w) in N*;
    psi = ceil(1/(1-w)) - 1; budget RHS td - 1 - psi."""
    w = Fraction(w)
    if not w < 1:
        return {"ok": False, "why": "w >= 1 (case IV needs w < 1)"}
    if M < 2:
        return {"ok": False, "why": "M=1 trunk (MP2)"}
    j = M * (1 - w)
    if not is_pos_int(j):
        return {"ok": False, "why": "j = M(1-w) = %s not in N*" % j}
    psi = ceil_frac(1 / (1 - w)) - 1
    psi2 = ceil_frac(Fraction(M) / j) - 1
    if psi != psi2:
        raise LLError("psi cross-check failed")
    return {"ok": True, "j": int(j), "psi": psi, "budget": td - 1 - psi}


def budget_verdict(lam, budget):
    if lam < budget:
        return "ALIVE", budget - lam
    if lam == budget:
        return "ALIVE_FRAGILE", 0
    return "DEAD", lam - budget


# ==========================================================================
# Sub-boundary residue: exhaust the St 9.4 budget from the boundary (3/2, 2)
# ==========================================================================

def residue_enumeration(td=TD):
    """BFS over trunk states (w, M, lam) from the boundary (3/2, 2, 0).
    Priced edges: dirty/pure-b cells (l | current M).  Neutral edges: M ->
    any divisor (w conserved, lam unchanged).  Global prune: psi >= 1 always,
    so lam <= td - 2 (= 4).  Terminal attempted at every state.

    Returns (terminal_rows, step_rows, states_seen).  Deterministic order.
    """
    lam_max = td - 2
    start = (Fraction(3, 2), 2, 0)
    seen = set()
    todo = [(start, ("BOUNDARY",))]
    terminals = []
    steps = []
    while todo:
        (w, M, lam), path = todo.pop(0)
        key = (w, M, lam)
        if key in seen:
            continue
        seen.add(key)
        t = terminal(w, M, td)
        if t["ok"]:
            verdict, slack = budget_verdict(lam, t["budget"])
            terminals.append({
                "state": [str(w), M, lam], "path": list(path),
                "j": t["j"], "psi": t["psi"], "budget": t["budget"],
                "verdict": verdict, "slack_or_overrun": slack})
        else:
            terminals.append({
                "state": [str(w), M, lam], "path": list(path),
                "verdict": "TERMINAL-REJECTED", "why": t["why"]})
        # neutral divisor shrink (w conserved; M'=1 recorded as DEAD row)
        for d in neutral_reachable_M(M):
            if d == M:
                continue
            lab = "NEUTRAL(M %d->%d)" % (M, d)
            if d == 1:
                steps.append({"from": [str(w), M, lam], "step": lab,
                              "verdict": "DEAD", "why": "M=1 trunk (MP2/R6)"})
            else:
                steps.append({"from": [str(w), M, lam], "step": lab,
                              "to": [str(w), d, lam],
                              "verdict": "STEP", "neutral": True})
                todo.append(((w, d, lam), path + (lab,)))
        # priced steps for each l | M, l >= 2 (St 8.4 legality gate)
        for l in range(2, M + 1):
            if not step_legal(l, M):
                continue
            cells, pure_b = dirty_cells(w, l, lam_max - lam)
            for c in cells:
                lab = "%s l=%d (%d,%d) nu=%d lam=%d" % (
                    c["rule"], l, c["dp"], c["dq"], c["nu"], c["lam"])
                row = {"from": [str(w), M, lam], "step": lab,
                       "cell": {kk: (str(vv) if isinstance(vv, Fraction)
                                     else vv) for kk, vv in c.items()}}
                if c["lam"] == 0:
                    # clean resonant candidate that passed integrality
                    row["verdict"] = "STEP"
                    row["to"] = [str(c["w_child"]), c["M_child"], lam]
                    todo.append(((c["w_child"], c["M_child"], lam),
                                 path + (lab,)))
                elif c["M_child"] == 1:
                    row["verdict"] = "DEAD"
                    row["why"] = "M=1 trunk (MP2/R6)"
                else:
                    row["verdict"] = "STEP"
                    row["to"] = [str(c["w_child"]), c["M_child"],
                                 lam + c["lam"]]
                    todo.append(((c["w_child"], c["M_child"],
                                  lam + c["lam"]), path + (lab,)))
                steps.append(row)
            for pb in pure_b:
                if pb["lam_min"] > lam_max - lam or pb["w_child"] is None:
                    continue
                for d in pb["M_divisors"]:
                    lab = "PURE-B l=%d eps=%d M'=%d lam=%d" % (
                        l, pb["eps"], d, pb["lam_min"])
                    row = {"from": [str(w), M, lam], "step": lab,
                           "w_child": str(pb["w_child"])}
                    if d == 1:
                        row["verdict"] = "DEAD"
                        row["why"] = "M=1 trunk (MP2/R6)"
                    else:
                        row["verdict"] = "STEP"
                        row["to"] = [str(pb["w_child"]), d,
                                     lam + pb["lam_min"]]
                        todo.append(((pb["w_child"], d,
                                      lam + pb["lam_min"]), path + (lab,)))
                    steps.append(row)
        # resonant steps are inside dirty_cells (k=eps=Sm=0, lam=0 rows);
        # none exist at these alphabets beyond integrality rejects.
    # Route-death fixpoint (derived, fail-closed): a state CAN COMPLETE iff
    # it has an in-budget admissible terminal (ALIVE / ALIVE_FRAGILE) or an
    # outgoing edge to a state that can complete.  A state that cannot
    # complete is route-dead: every continuation either violates St 9.4 or
    # never reaches a case-IV terminal.  Marked explicitly, never implicit.
    edges = {}
    for r in steps:
        if r["verdict"] == "STEP":
            edges.setdefault(tuple(r["from"]), set()).add(tuple(r["to"]))
    can_complete = {tuple(t["state"]) for t in terminals
                    if t.get("verdict") in ("ALIVE", "ALIVE_FRAGILE")}
    changed = True
    while changed:
        changed = False
        for src, dsts in edges.items():
            if src not in can_complete and dsts & can_complete:
                can_complete.add(src)
                changed = True
    for t in terminals:
        if t.get("verdict") in ("TERMINAL-REJECTED", "DEAD"):
            t["route_dead"] = tuple(t["state"]) not in can_complete
            if t["route_dead"]:
                t["route_dead_why"] = ("cannot complete: no in-budget "
                                       "admissible terminal is reachable "
                                       "(St 9.4 RHS <= %d, psi >= 1)"
                                       % lam_max)
    terminals.sort(key=lambda r: (r["state"][2] if isinstance(r["state"][2], int) else 0,
                                  r["state"][0], r["state"][1],
                                  tuple(r["path"])))
    steps.sort(key=lambda r: (r["from"][2], r["from"][0], r["from"][1], r["step"]))
    return terminals, steps, sorted((str(w), M, lam) for (w, M, lam) in seen)


# ==========================================================================
# Synthetic UNCOVERED probe (A2/A4 machinery demonstration; NOT a td=6 row)
# ==========================================================================

def synthetic_cap_probe():
    """A genuinely capped synthetic family: its classification hypothesis
    SYN-1 is deliberately absent from the promoted perimeter (tier CAP), so
    the fail-closed classifier must emit UNCOVERED with the exact missing
    hypothesis, smallest instance, and blocked consumers -- never a
    rejection."""
    hyp = "SYN-1"
    tier = TRUST[hyp]["tier"]
    if tier in ALLOWED_TIERS:
        raise LLError("synthetic probe hypothesis must not be promoted")
    return {
        "record_id": "SYNTHETIC/CAP-PROBE",
        "synthetic": True,
        "family_spec": {"param": "s", "range": "s >= 1",
                        "note": "synthetic family, engine swept s <= 4 only"},
        "classification": "UNCOVERED",
        "verdict": "NA",
        "uncovered": {
            "h": "SYN-1: uncapped exclusion of the synthetic probe family "
                 "(hypothesis absent from the frozen trust snapshot)",
            "smallest_instance": "s = 5",
            "blocked_consumers": ["SYNTHETIC-CONSUMER (probe only; no td=6 "
                                  "consumer exists)"],
        },
    }


# ==========================================================================
# Book assembly
# ==========================================================================

def _f(x):
    """JSON-safe rendering of Fractions."""
    if isinstance(x, Fraction):
        return str(x)
    if isinstance(x, dict):
        return {k: _f(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_f(v) for v in x]
    return x


def compile_book(td=TD, m=M_POLES):
    unused_registry = []
    records = {"entry": [], "chain": [], "merge": [], "suffix": [],
               "residue_terminals": [], "residue_steps": []}

    # ---- entry (R0) ----
    entries, offaxis = entry_menu(td, m)
    if len(entries) != 1 or offaxis:
        raise LLError("entry menu drift: expected exactly one on-axis entry "
                      "and empty off-axis at td=6,m=2")
    entry = entries[0]
    frames = entry_frame(entry)
    for i, fr in enumerate(frames):
        if (fr["kbar"], fr["M"], fr["rho"], fr["w0"]) != (Fraction(5), 1, Fraction(1), Fraction(2)):
            raise LLError("entry frame drift at pole %d" % (i + 1))
    records["entry"].append({
        "record_id": "ENTRY/unique",
        "header_key": {"td": td, "m": m, "Lambda": list(entry["Lambda"]),
                       "type": list(entry["type"])},
        "poles": [{"pole_id": "P%d" % (i + 1), **_f(fr)}
                  for i, fr in enumerate(frames)],
        "classification": "COVERED", "verdict": "ADMITTED",
        "why": "T7 arithmetic: Lambda=(3,3) prime => b=1 (MP4); nu-menu "
               "forces (a,b,nu)=(1,1,2) at both poles; off-axis empty",
        "cert_chain": cert("T7", "MP4", "OFFAXIS-EMPTY-TD6"),
    })

    # ---- pre-merge chains (R1/DS1-DS3) ----
    W = w_closure(Fraction(2))
    if W != [Fraction(2)]:
        raise LLError("W(2) drift")
    for pole_id in ("P1", "P2"):
        records["chain"].append({
            "record_id": "CHAIN/%s/parametric" % pole_id,
            "pole_id": pole_id,
            "family_spec": {"frames": "(w,nu,kbar) = (2, nu, 2nu+2)",
                            "nu": "free >= 2", "depth": "unbounded (DS1 R1)"},
            "classification": "COVERED", "verdict": "ADMITTED",
            "why": "W(2)={2}: no Delta>=3 divides 2, so no resonant step; "
                   "every step neutral (w conserved); mu=1 arrival at the "
                   "single merge; lam=0",
            "closure_certificate": {"W": [str(w) for w in W], "gen": 0,
                                    "d0_safe": 2},
            "cert_chain": cert("DS1", "DS2", "DS3", "MP5", "MP1"),
        })
        unused_registry.append({
            "vertex": "CHAIN/%s/every-step" % pole_id,
            "orbit_spec": "nu-1 conjugate orbit roots (parametric per step)",
            "fate": "DECK_CONJUGATE",
            "cert_chain": cert("St 3.18")})

    # ---- merge partition (complete; prohibition 1) ----
    mrows = []
    # (1) root meet, l >= 1 parametric
    root_rows = root_meet([(Fraction(2), W_CLOSED_FORM),
                           (Fraction(2), W_CLOSED_FORM)])
    if not all(r["window_kill"] for r in root_rows):
        raise LLError("root window kill failed to fire on certified w=2")
    lc = root_local_cell(2, 1)
    mrows.append({
        "record_id": "MERGE/ROOT/parametric-l>=1",
        "family_spec": {"arrangement": "G*=(0,y)", "l": ">=1 parametric",
                        "local_cell_example": _f(lc)},
        "classification": "COVERED", "verdict": "DEAD",
        "why": "case-I mixed-root window: every actual searrow parent edge "
               "needs 0<w<1; both arrivals carry certified w=2 "
               "(W-CLOSED-FORM).  Root M=1 itself is LEGAL (the local "
               "r=2,l=1 cell has w=1/3, M_root=1); the kill is the window, "
               "never root-M=1.",
        "arrivals": [_f(r) for r in root_rows],
        "cert_chain": cert("DEPTH-5d", "MRW", "MP5"),
    })
    mrows.append({
        "record_id": "MERGE/ROOT/l=0",
        "family_spec": {"arrangement": "G*=(0,y)", "l": 0},
        "classification": "COVERED", "verdict": "REJECTED",
        "why": "l=0 at the root: q=p gives 0 = theta*p, impossible",
        "cert_chain": cert("MP7", "MP9"),
    })
    # (2) ZCH: either chain at the 0-direction (two provenance-distinct rows)
    if zch_join(W):
        raise LLError("ZCH join unexpectedly solvable at W={2}")
    for pole_id in ("P1", "P2"):
        mrows.append({
            "record_id": "MERGE/ZCH/0-edge=%s" % pole_id,
            "family_spec": {"arrangement": "interior, %s at 0-direction"
                                           % pole_id, "nu_G": ">=2"},
            "classification": "COVERED", "verdict": "REJECTED",
            "why": "case-III join needs w_other = nu_e * w_0chain, nu_e>=2; "
                   "sole alphabet value 2 gives 2 = nu_e*2 => nu_e=1: "
                   "impossible (DEPTH machine check 7: 403 solves, none "
                   "joinable)",
            "cert_chain": cert("DEPTH-5c", "R2.1"),
        })
    # (3) IIa
    admitted, derivation, spot = iia_admitted(Fraction(2))
    mrows.append({
        "record_id": "MERGE/IIA/l-or-nu-even",
        "family_spec": {"family": "IIa", "constraint": "l*nu even"},
        "classification": "COVERED", "verdict": "DEAD",
        "why": "M = gcd(2, l*nu+1) = 1 at an interior trunk vertex",
        "cert_chain": cert("MP6", "Prop 8.1(v)", "MP2", "MP9"),
    })
    mrows.append({
        "record_id": "MERGE/IIA/l-nu-odd-nonintegral",
        "family_spec": {"family": "IIa", "constraint": "l,nu odd, (nu,l)!=(3,1)"},
        "classification": "COVERED", "verdict": "REJECTED",
        "why": "kbar = 2 + 4nu/(l*nu+1) not integral: " + derivation,
        "spot_checks": spot,
        "cert_chain": cert("DS1", "DS4", "MP6"),
    })
    adm = admitted[0]
    mrows.append({
        "record_id": "MERGE/IIA/admitted-(2,3,1)",
        "family_spec": {"family": "IIa", "r": 2, "nu": 3, "l": 1},
        "classification": "COVERED", "verdict": "ADMITTED",
        "cell": _f(adm["cell"]), "child": _f(adm["child"]),
        "why": "unique integral M=2 cell; child Q=(6,12,3,2,5) at i=2, "
               "w_trunk=3/2, w_cert=W-CLOSED-FORM (DS4)",
        "cert_chain": cert("MP6", "MP6(b)", "DS4", "MP9"),
    })
    unused_registry.append({
        "vertex": "MERGE/IIA/admitted-(2,3,1)",
        "orbit_spec": "the l=1 extra simple q-orbit (q-extra)",
        "fate": "NO_TREE_VERTEX",
        "cert_chain": cert("St 3.18", "MP6")})
    # (4) family I (nu_G = 1): the corrected split -- replaces the sealed
    # 5.4 UNCOVERED row and the l<=4 machine-only row.
    for spec, pres in (
            ({"L": "odd >= 1"}, classify_family_I(2, 1)),
            ({"L": "even >= 2 (s(0)=0 included)"}, classify_family_I(2, 2)),
            ({"L": 0}, classify_family_I(2, 0))):
        mrows.append({
            "record_id": "MERGE/FAMILY-I/L-%s" % (
                "odd" if spec["L"] == "odd >= 1" else
                ("even" if isinstance(spec["L"], str) else "0")),
            "family_spec": {"family": "I", "nu_G": 1, "r": 2, **spec},
            "classification": pres["classification"],
            "verdict": pres["verdict"], "why": pres["why"],
            "normal_form_representative": _f(pres["normal_form"]),
            "cert_chain": pres["cert_chain"],
            "identification": "legacy (l, eps_q=1) records are family I at "
                              "L = l+1 with s(0)=0 (MP6(c): eta absorbed at "
                              "nu=1); normalized BEFORE classification",
        })
    # (5) mixed all-mu>=2: unreachable (not silently covered)
    mrows.append({
        "record_id": "MERGE/MIXED/all-mu>=2",
        "family_spec": {"mu": "all >= 2"},
        "classification": "COVERED", "verdict": "UNREACHABLE",
        "why": "mu_e | M_{H_e} = 1 (St 8.4 + MP5) forces mu=(1,1); the "
               "general mixed emission menu remains OPEN at other headers "
               "(BOOK-OFFAXIS sec.3) and is NOT decided here",
        "cert_chain": cert("St 8.4", "MP5"),
    })
    records["merge"] = mrows

    # ---- suffix: first P0 step from (3/2, 2) ----
    cells, pure_b = dirty_cells(Fraction(3, 2), 2, TD - 2)
    priced = [c for c in cells if c["lam"] > 0]
    resonant = [c for c in cells if c["lam"] == 0]
    if resonant:
        raise LLError("unexpected lam=0 resonant survivor from (3/2,2)")
    got = sorted((c["dp"], c["dq"]) for c in priced)
    if got != [(7, 5), (20, 16), (21, 15)]:
        raise LLError("P0 first-step dirty menu drift: %r" % got)
    srows = [{
        "record_id": "SUFFIX/neutral-thick-l2-nu-odd",
        "family_spec": {"l": 2, "n": 1, "nu": "odd >= 3 parametric"},
        "classification": "COVERED", "verdict": "ADMITTED",
        "why": "w=3/2 conserved; M_child = gcd(2nu, nu+1) = gcd(2,nu+1) = 2 "
               "(derived from the CHILD shape, never cached)",
        "cert_chain": cert("DS2", "Prop 8.1(v)"),
    }, {
        "record_id": "SUFFIX/neutral-thick-l2-nu-even",
        "family_spec": {"l": 2, "n": 1, "nu": "even parametric"},
        "classification": "COVERED", "verdict": "DEAD",
        "why": "M_child = gcd(2, nu+1) = 1 on the nonroot trunk",
        "cert_chain": cert("Prop 8.1(v)", "MP2"),
    }, {
        "record_id": "SUFFIX/thin-l1",
        "family_spec": {"l": 1, "n": ">=1"},
        "classification": "COVERED", "verdict": "DEAD",
        "why": "M = gcd(nu, n*nu+1) = 1 on the nonroot trunk",
        "cert_chain": cert("Prop 8.1(v)", "MP2"),
    }, {
        "record_id": "SUFFIX/clean-resonant",
        "family_spec": {"Delta": 3, "n": 2, "nu": 2},
        "classification": "COVERED", "verdict": "REJECTED",
        "why": "Delta|num(3/2)=3 forces (n,nu)=(2,2), dq=5; kbar = "
               "(3/2)*5/3 = 5/2 not integral (den(w)=2 does not divide "
               "dq=5)",
        "cert_chain": cert("DS3", "DS1"),
    }]
    for c in priced:
        dead = c["M_child"] == 1
        srows.append({
            "record_id": "SUFFIX/dirty-(%d,%d)" % (c["dp"], c["dq"]),
            "family_spec": {k: _f(v) for k, v in c.items()},
            "classification": "COVERED",
            "verdict": "DEAD" if dead else "ADMITTED",
            "why": ("M=1 on the trunk (lam moot)" if dead else
                    "-> (w,M) = (%s,%d), lam >= %d; W-PRICED-COMPLETE"
                    % (c["w_child"], c["M_child"], c["lam"])),
            "w_cert_child": None if dead else W_PRICED_COMPLETE,
            "cert_chain": cert("P0", "AF2", "St 8.4"),
        })
    for pb in pure_b:
        srows.append({
            "record_id": "SUFFIX/pure-b-eps%d" % pb["eps"],
            "family_spec": _f(pb),
            "classification": "COVERED", "verdict": "DEAD",
            "why": "w -> 3, M = gcd(1, nu+1) = 1 on the trunk; lam >= 3",
            "cert_chain": cert("P0", "MP2"),
        })
    records["suffix"] = srows

    # ---- residue to budget exhaustion ----
    terms, steps, states = residue_enumeration(TD)
    records["residue_terminals"] = terms
    records["residue_steps"] = steps

    # boundary terminal parity (A3): the two recorded budgets
    t23 = [t for t in terms if t["state"] == ["2/3", 3, 2]
           and t.get("verdict") == "ALIVE"]
    t34 = [t for t in terms if t["state"] == ["3/4", 4, 2]
           and t.get("verdict") == "ALIVE_FRAGILE"]
    if not (t23 and t23[0]["psi"] == 2 and t23[0]["j"] == 1
            and t23[0]["slack_or_overrun"] == 1):
        raise LLError("(2/3,3) terminal budget drift")
    if not (t34 and t34[0]["psi"] == 3 and t34[0]["j"] == 1):
        raise LLError("(3/4,4) terminal budget drift")

    book = {
        "packet": "LL1-R2 (td=6, m=2)",
        "date": "2026-08-29",
        "trust_snapshot": TRUST,
        "w_cert_tokens": list(W_CERT_TOKENS),
        "root_kill_certs": list(ROOT_KILL_CERTS),
        "sections": records,
        "unused_registry": unused_registry,
        "uncovered": [],  # corrected A2: EMPTY at this header, and that is
                          # a pass, not a failure
        "synthetic_probes": [synthetic_cap_probe()],
        "scope_firewall": [
            "This packet tests the corrected LL-1 quotient and hand-run at "
            "td=6, m=2 only.",
            "It is NOT a proof that the candidate grammar equals the set of "
            "all geometric configurations (Cand(s) vs CFG).",
            "It does NOT bound segment depth (DS1 R1: depth is not "
            "(m,td)-bounded).",
            "It proves NO source landing, ceiling, Keller, or JC2 "
            "statement; no output touches G2-PSC, G2-BD, RPMC(C), or the "
            "cofinal degree ceiling.",
            "Single-pole composite configurations (REDUCTION HIGH 1) and "
            "realizability are out of scope; ALIVE families are "
            "conservative supersets.",
            "The mixed all-mu>=2 emission menu is OPEN in general "
            "(BOOK-OFFAXIS sec.3); at this header it is unreachable, which "
            "is a divisibility fact, not a completeness theorem.",
        ],
        "obligations_ll2": [
            "LL-2 = td=7, m=2 including the off-axis entry (2,3), "
            "Lambda=(3,4), (a,b,nu)=(1,1,2)+(1,2,3): first header where "
            "W-PRICED certification, dirty pre-merge steps, case-III/E5, "
            "and the H5a 17-vs-2 conditional books all fire.",
            "Carry the H5a_reading pin explicitly; the Q-reading 17-cell "
            "census is the A1 baseline (BOOK-OFFAXIS sec.11a).",
            "The mixed all-mu>=2 emission menu completeness remains an "
            "open obligation for any header where it is reachable.",
            "No td-7 zero-chain-law extension is queued for the nu=1 "
            "family-I layer: D9 as printed plus the one-line degree "
            "identification closes it (this packet).",
        ],
    }
    return book


# ==========================================================================
# Deterministic emission
# ==========================================================================

def canonical_json(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True)


def derive_summary(book):
    """Derived (never hand-written) summary; the validator recomputes this
    independently from the records."""
    counts = {}
    for sec, rows in book["sections"].items():
        c = {}
        for r in rows:
            v = r.get("verdict", "NA")
            c[v] = c.get(v, 0) + 1
        counts[sec] = dict(sorted(c.items()))
    return {
        "packet": book["packet"],
        "section_verdict_counts": counts,
        "uncovered_count": len(book["uncovered"]),
        "synthetic_uncovered_count": sum(
            1 for p in book["synthetic_probes"]
            if p["classification"] == "UNCOVERED"),
        "admitted_merge_cells": sorted(
            r["record_id"] for r in book["sections"]["merge"]
            if r["verdict"] == "ADMITTED"),
        "boundary_terminals": sorted(
            "%s psi=%s %s" % (t["state"], t.get("psi"), t["verdict"])
            for t in book["sections"]["residue_terminals"]
            if t["state"][2] == 2 and t.get("verdict") in
            ("ALIVE", "ALIVE_FRAGILE")),
        "residue_alive_terminals": sorted(
            "%s psi=%s %s slack=%s" % (t["state"], t.get("psi"),
                                       t["verdict"],
                                       t.get("slack_or_overrun"))
            for t in book["sections"]["residue_terminals"]
            if t.get("verdict") in ("ALIVE", "ALIVE_FRAGILE")),
    }


def main(outdir=None):
    here = os.path.dirname(os.path.abspath(__file__))
    outdir = outdir or os.path.join(here, "out")
    os.makedirs(outdir, exist_ok=True)
    book = compile_book()
    summary = derive_summary(book)
    for name, obj in (("ll1_book.json", book), ("ll1_summary.json", summary)):
        path = os.path.join(outdir, name)
        with open(path, "w") as f:
            f.write(canonical_json(obj) + "\n")
    digest = {name: hashlib.sha256(
        open(os.path.join(outdir, name), "rb").read()).hexdigest()
        for name in ("ll1_book.json", "ll1_summary.json")}
    print("LL1-R2 compile OK")
    for k in sorted(digest):
        print("  %s  %s" % (digest[k], k))
    return 0


if __name__ == "__main__":
    sys.exit(main())
