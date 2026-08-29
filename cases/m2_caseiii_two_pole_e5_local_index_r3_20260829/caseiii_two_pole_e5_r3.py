#!/usr/bin/env python3
"""Two-pole case-III merge under the promoted Q+E5 pin (R3 repair packet).

Repairs the R2 packet cases/m2_caseiii_two_pole_e5_local_index_r2_20260829
(R1 and R2 stay byte-untouched) after the Opus 5 hostile review
(xmodel/m2-caseiii-two-pole-e5-local-index-r2-hostile-review-opus5-
20260829.md, verdict REPAIR_REQUIRED, body c12bbca2...7b4c).  The review
CONFIRMED the whole theorem layer (Lemma A, Theorem B, Theorem C, the
equality laws, the 12-of-17 attainment, the no-incoming-bound proposition,
the corrected Opus adjudication) and blocked on two findings, both
repaired here:

  F1  R2's s7.4 "infinite pattern fibre at fixed (kbar, nu_G)" is FALSE.
      Three of its five named members ((38,19), (62,31), (134,67)) violate
      the strict (NE) law m_j*dq < dp; the fibre is ALWAYS FINITE.  R3
      withdraws the claim, deletes every NE-illegal example, and proves
      Theorem D: with r = kbar/(mu*w) = dq/D and u = mu - 1/r > 0,

          s * (1 + u - ceil(u)) <= (1+nu)/(r*nu) + delta/nu,

      so the fibre over a fixed (kbar, nu_G) per state is finite, each
      member pinned by its s.  The bound is SHARP (attained with exact
      equality in the census).  The s7.4 fibre is exactly
      {(20,10), (26,13)}.
  F2  R2's s8.3 T1 migration gate "dp | dq <=> kbar in {3,4}" is the
      w = 2 specialisation of BOOK-OFFAXIS s11's zero-chain law; the R2
      solver raised ValueError on legal w = 1 and w = 3 input.  R3 states
      Lemma T1': for any two-pole cell, kbar - w = w*dp/D identically, so

          dp | dq  <=>  M = dp  <=>  w/(kbar - w) in Z>=1,

      and for integer w with integer kbar (DS1(c)) the menu is
      kbar in {w + d : d | w} (w=2 recovers {3,4}).  The solver is now
      TOTAL on every legal w; the direct check dq % dp == 0 is the
      verdict and the closed form is enforced as a theorem gate.

Also repaired per the review's majors/nits: the six r0 = 2 countercells
are explicitly marked M = 1 / MP2-dead (F3), with the new arity-graded
Theorem E  dq/D <= (r0+1) + ((r0+1)*delta+1)/M  and Theorem F (no
MP2-alive violator of the two-pole constant exists at r0 in {2,3};
refuted at r0 = 4 by the (44,46) cell -- outside the campaign's
MP1/TDMAX range r0 <= 3); the nu_U = 13 gloss of the no-incoming-bound
demo (13 is NOT an arrival-legal vertex at (2/5, M5), so the mixed pin
KILLS the (18,27,13,9)@5 cell); and the (4m-2, 6m-3) family glosses
(odd m only; even m are the four recorded N1 kills; termination at
m = 25 is closure-forced, not theorem-forced).

Scope: interior two-pole case-III merges ONLY -- exactly one nonzero
arriving pole-chain edge (mu, w), one pole-chain 0-arrival (mu0, w_U),
nu_G >= 2, no inner-merge arrivals.  Exact rational arithmetic; no CAS;
the canonical engine cases/book_offaxis.py is NOT modified and NUCAP
stays.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import gcd
from typing import Iterable

SCHEMA = "m2-caseiii-two-pole-e5-local-index-r3"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def fraction_text(value: Fraction) -> str:
    value = Fraction(value)
    return (str(value.numerator) if value.denominator == 1 else
            f"{value.numerator}/{value.denominator}")


def ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


# ---------------------------------------------------------------------------
# Promoted 17-cell book, BOOK-OFFAXIS.md s11a (frozen chain-1 (mu,w)=(1,2)):
# (dp, dq, nu_G, M, mu0, kbar, w_U).
BOOK = (
    (9, 15, 7, 3, 2, 5, Fraction(1, 2)),
    (10, 15, 7, 5, 3, 6, Fraction(2, 3)),
    (15, 25, 12, 5, 3, 5, Fraction(1, 3)),
    (18, 27, 13, 9, 5, 6, Fraction(2, 5)),
    (21, 35, 17, 7, 4, 5, Fraction(1, 4)),
    (25, 35, 17, 5, 8, 7, Fraction(3, 8)),
    (26, 39, 19, 13, 7, 6, Fraction(2, 7)),
    (27, 45, 22, 9, 5, 5, Fraction(1, 5)),
    (34, 51, 25, 17, 9, 6, Fraction(2, 9)),
    (42, 63, 31, 21, 11, 6, Fraction(2, 11)),
    (50, 75, 37, 25, 13, 6, Fraction(2, 13)),
    (58, 87, 43, 29, 15, 6, Fraction(2, 15)),
    (66, 99, 49, 33, 17, 6, Fraction(2, 17)),
    (74, 111, 55, 37, 19, 6, Fraction(2, 19)),
    (82, 123, 61, 41, 21, 6, Fraction(2, 21)),
    (90, 135, 67, 45, 23, 6, Fraction(2, 23)),
    (98, 147, 73, 49, 25, 6, Fraction(2, 25)),
)
BOOK_MU, BOOK_W = 1, Fraction(2)
# The U_7C-restricted (forced-nu) sub-book, s11a.
FORCED_SUBBOOK = ((9, 15, 7, 3), (10, 15, 7, 5))
# Spot members of the 56 T1-law-dead cells (cases/td7_census_e5.py DEAD56)
# that reappear as T1-dead candidates of the E5 solve below.
DEAD56_SPOT = ((7, 21, 4, 7), (8, 16, 5, 8), (5, 15, 2, 5), (5, 10, 3, 5))
# s11a's four recorded N1 kills: the even-m members of the (4m-2, 6m-3)
# family (kbar = 6, even nu_G = 3m-2).
N1_KILLED_EVEN_M = ((14, 21, 10, 7, 4), (22, 33, 16, 11, 6),
                    (30, 45, 22, 15, 8), (38, 57, 28, 19, 10))


# ---------------------------------------------------------------------------
def gap_pattern_certificate(mu: int, mu0: int, nu: int, k: int,
                            mults: tuple[int, ...],
                            lex: int) -> dict[str, object]:
    """Certify one two-pole case-III pattern cell and both ratio bounds.

    Reading-independent: uses only the R1.0/R2.2 pattern and the (S)/(NE)/
    (R) laws -- no handshake, no w, no H5a-sensitive object.  All laws are
    hard gates: nu >= 2 (a nu_G = 1 merge is case I, out of case-III
    scope), strict NE on every non-chain orbit, 0-edge searrow, root-mult
    law.  Preserved verbatim from R2 (review-confirmed, charge 1/2/3).
    """
    require(isinstance(mu, int) and mu >= 1, "mu must be a positive integer")
    require(isinstance(mu0, int) and mu0 > mu,
            "difficult regime requires mu0 > mu")
    require(isinstance(nu, int) and nu >= 2,
            "case-III merge-local index nu_G >= 2 (nu=1 is case I)")
    require(isinstance(k, int) and k >= 0 and isinstance(lex, int)
            and lex >= 0, "invalid pattern indices")
    require(len(mults) == k, "multiplicity census mismatch")
    require(all(isinstance(m, int) and 1 <= m <= mu - 1 for m in mults),
            "NE multiplicity must lie in [1, mu-1]")

    delta = mu0 - mu
    sm = sum(mults)
    s = k + lex
    dp = mu0 + nu * (mu + sm)
    dq = 1 + nu * (1 + s)
    D = mu * dq - dp
    require(D >= 1, "nonzero arriving edge is not searrow")
    require(s >= 1, "s = 0 would force D = -delta < 0")
    A = mu * s - sm
    require(D == nu * A - delta, "degree-gap identity failed")
    require(A >= s, "A >= s consequence of m_j <= mu-1 failed")
    require(mu0 * dq > dp, "0-edge searrow failed")
    require(all(m * dq < dp for m in mults), "strict NE law failed")
    require(all(dp != m * dq for m in set(mults) | {mu, mu0}),
            "root-mult law (R) failed")

    M = gcd(dp, dq)
    require(D % M == 0, "M | D failed")
    # Lemma A bound (integer form of dq/D <= 2*delta+3).
    require(dq <= D * (2 * delta + 3), "universal dq/D bound failed")
    # Theorem B bound (integer form of dq/D <= 2 + (2*delta+1)/M).
    require(dq * M <= D * (2 * M + 2 * delta + 1),
            "M-graded dq/D bound failed")

    eq_plain = dq == D * (2 * delta + 3)
    eq_graded = dq * M == D * (2 * M + 2 * delta + 1)
    # Exact equality laws (proved in the report; enforced here).
    require(eq_plain == (nu == delta + 1 and s == 1 and A == 1),
            "plain equality law failed")
    if eq_plain:
        require(D == 1 and M == 1, "plain equality must have D = M = 1")
    require(eq_graded == (D == M and nu == delta + M and s == 1 and A == 1
                          and (2 * delta + 1) % M == 0),
            "M-graded equality law failed")
    return {
        "mu": mu, "mu0": mu0, "delta": delta, "nu_G": nu, "k": k,
        "lex": lex, "multiplicities": list(mults), "dp": dp, "dq": dq,
        "D": D, "A": A, "M": M,
        "dq_over_D": fraction_text(Fraction(dq, D)),
        "equality_plain": eq_plain, "equality_graded": eq_graded,
    }


def kbar_bound(mu: int, w: Fraction, delta: int, M: int = 1) -> Fraction:
    """kbar <= mu*w*(2 + (2*delta+1)/M); M = 1 gives mu*w*(2*delta+3)."""
    require(mu >= 1 and delta >= 1 and M >= 1, "bad kbar-bound arguments")
    require(w > 0, "w must be positive")
    return mu * w * (2 + Fraction(2 * delta + 1, M))


def ne_cap(mu: int, dp: int, dq: int) -> int:
    """The TRUE strict-(NE) multiplicity cap: m_j*dq < dp and m_j <= mu-1,
    i.e. m_j <= min(mu - 1, (dp - 1) // dq).  R2's fibre fixtures bypassed
    this with the derived proxy mu - 1 alone (review F1d) -- the proxy is
    the permanent mutation target MUT_G."""
    return min(mu - 1, (dp - 1) // dq)


# ---------------------------------------------------------------------------
def e5_eliminate_nu_g(mu: int, w: Fraction, mu0: int, w_U: Fraction,
                      kbar: Fraction) -> Fraction:
    """Solve the E5 elimination mu0*nu_G*w_U = delta*kbar + mu*w for nu_G."""
    delta = mu0 - mu
    return (delta * kbar + mu * w) / (mu0 * w_U)


def e5_regimes(mu: int, w: Fraction, mu0: int,
               w_U: Fraction) -> dict[str, object]:
    """Merge-local nu_G conclusion in all three multiplicity regimes.

    The eliminated identity is  mu0*nu_G*w_U = delta*kbar + mu*w
    (case-II handshake X = mu*(kbar - w) against the promoted E5 case-III
    handshake X = mu0*(kbar - nu_G*w_U)).  No incoming index occurs.
    Regimes are NAMED, never numbered (review F5.3): REVERSE (mu0 < mu),
    EQUAL (mu0 = mu), DIFFICULT (mu0 > mu).  Preserved from R2 otherwise.
    """
    require(isinstance(mu, int) and mu >= 1, "mu must be a positive integer")
    require(isinstance(mu0, int) and mu0 >= 1,
            "mu0 must be a positive integer")
    require(isinstance(w, Fraction) and w > 0, "w must be positive")
    require(isinstance(w_U, Fraction) and w_U > 0, "w_U must be positive")

    if mu0 < mu:
        # REVERSE: kbar > w (handshake: kbar - w = w*dp/D > 0) gives
        # mu0*nu_G*w_U = mu*w - (mu-mu0)*kbar < mu*w - (mu-mu0)*w = mu0*w,
        # hence the STRICT bound nu_G < w/w_U.
        strict = w / w_U
        top = ceil_fraction(strict) - 1
        menu = list(range(2, top + 1))
        return {
            "regime": "mu0<mu", "strict_upper_nu_G": fraction_text(strict),
            "nu_G_menu": menu,
            "reason": "kbar > w forces mu0*nu_G*w_U < mu0*w",
        }
    if mu0 == mu:
        # EQUAL: the elimination degenerates to nu_G*w_U = w exactly; kbar
        # is NOT pinned by the two handshakes (they coincide; review F5.5).
        # A finite kbar menu still exists (dq/D <= 2 + 1/y <= 3 at
        # delta = 0, so kbar in Z cap (w, 3*mu*w]) but the legacy engine
        # branch applies no cell_check here and a migration must mirror
        # that for verdict parity.
        forced = w / w_U
        legal = forced.denominator == 1 and forced >= 2
        return {
            "regime": "mu0=mu", "forced_nu_G": fraction_text(forced),
            "legal_case_iii": bool(legal),
            "kbar_pinned": False,
            "kbar_finite_menu": "Z cap (w, 3*mu*w] (delta=0 ratio <= 3)",
            "reason": ("delta = 0 degenerates the elimination to "
                       "nu_G*w_U = w exactly; nu_G = 1 is case-I "
                       "territory, not a case-III merge"),
        }
    # DIFFICULT: finite kbar menu from Lemma A, then one nu_G per kbar
    # from the elimination.  No incoming index exists.
    delta = mu0 - mu
    top = kbar_bound(mu, w, delta)
    entries = []
    kb_min = w.numerator // w.denominator + 1   # least integer kbar > w
    for kbar in range(kb_min, int(top) + 1):
        require(kbar > w, "kbar menu lower endpoint broken")
        nu_g = e5_eliminate_nu_g(mu, w, mu0, w_U, Fraction(kbar))
        if nu_g.denominator != 1 or nu_g < 2:
            continue
        entries.append({"kbar": kbar, "nu_G": int(nu_g),
                        "X": fraction_text(mu * (kbar - w))})
    bound = (delta * top + mu * w) / (mu0 * w_U)
    return {
        "regime": "mu0>mu", "delta": delta,
        "kbar_upper": fraction_text(top),
        "nu_G_upper": fraction_text(bound),
        "kbar_menu": entries,
        "reason": ("kbar = mu*w*dq/D in Z with w < kbar <= "
                   "mu*w*(2*delta+3); then nu_G = "
                   "(delta*kbar + mu*w)/(mu0*w_U) once per kbar"),
    }


# ---------------------------------------------------------------------------
# Lemma T1' (the F2 repair): the general zero-chain identification.
def t1_closed_form(kbar: Fraction, w: Fraction) -> bool:
    """At mu = 1:  dp | dq  <=>  w/(kbar - w) in Z>=1.

    Proof: kbar - w = w*(mu*dq - D)/D = w*dp/D identically (the identity
    holds at EVERY mu), so w/(kbar - w) = D/dp; and at mu = 1 one has
    dq = dp + D, hence dp | dq <=> dp | D <=> D/dp in Z>=1 (D >= dp is
    automatic from dp | D, D >= 1).  The divisibility leg is mu = 1 ONLY
    (at mu >= 2 only mu*dq = dp + D holds) -- which is exactly the T1
    zero-chain law's scope, the pinned mu = 1 solve of BOOK-OFFAXIS s11.
    The w = 2, kbar in Z specialisation is s11's kbar in {3,4}; the
    w-free leg M = dp (a tautology of gcd) is s11's other printed form."""
    kbar, w = Fraction(kbar), Fraction(w)
    if kbar <= w:
        return False
    q = w / (kbar - w)
    return q.denominator == 1 and q >= 1


def t1_divisor_menu(w: int) -> list[int]:
    """For integer w and integer kbar (DS1(c)): dp | dq <=> kbar in
    {w + d : d | w}.  w=1 -> {2}; w=2 -> {3,4}; w=3 -> {4,6};
    w=4 -> {5,6,8}; w=6 -> {7,8,9,12}."""
    require(isinstance(w, int) and w >= 1, "divisor menu needs integer w")
    return sorted(w + d for d in range(1, w + 1) if w % d == 0)


def e5_solve_mu1(w: Fraction, mu0: int, w_U: Fraction) -> list[dict]:
    """Full pinned-cell E5 solve for a mu = 1 nonzero partner.

    With mu = 1 the pattern pins dp = mu0 + nu_G exactly (k = 0 forced by
    m_j <= mu-1 = 0), so each (kbar, nu_G) menu entry yields at most one
    cell.  TOTAL on every legal input (w rational > 0, mu0 >= 2): the R2
    version hard-coded the w = 2 T1 menu {3,4} and RAISED on w = 1 and
    w = 3 (review F2); the verdict is now the direct dq % dp == 0, with
    Lemma T1's closed form enforced as a theorem gate (a disagreement
    would be a refutation of Lemma T1', not a verdict).  Post-filters are
    recorded, not silently dropped: T1 zero-chain law, N1 primitivity
    gcd(kbar, nu_G) = 1, MP2 (M >= 2), q-shape s >= 1.
    """
    w, w_U = Fraction(w), Fraction(w_U)
    require(mu0 >= 2, "difficult-regime solver needs mu0 > mu = 1")
    out = []
    for entry in e5_regimes(1, w, mu0, w_U)["kbar_menu"]:
        kbar, nu_g = entry["kbar"], entry["nu_G"]
        X = Fraction(kbar) - w
        dp = mu0 + nu_g
        dq_f = Fraction(kbar) * dp / X
        if dq_f.denominator != 1:
            continue
        dq = int(dq_f)
        if (dq - 1) % nu_g:
            continue
        s = (dq - 1) // nu_g - 1
        if s < 1:
            continue
        M = gcd(dp, dq)
        t1_dead = dq % dp == 0
        require(t1_dead == t1_closed_form(Fraction(kbar), w),
                "Lemma T1' closed form disagrees with dq % dp")
        require(t1_dead == (M == dp), "T1 w-free leg M = dp disagrees")
        out.append({
            "dp": dp, "dq": dq, "nu_G": nu_g, "M": M, "kbar": kbar,
            "s": s, "t1_dead": t1_dead, "n1_ok": gcd(kbar, nu_g) == 1,
            "mp2_ok": M >= 2,
        })
    return out


def t1_regression() -> dict[str, object]:
    """Machine regression of Lemma T1' and solver totality (review F2).

    Pins the full solver menus on legal w = 1, 2, 3 states plus broader
    regression values (w = 4, 6 and rational w = 3/2); every menu is
    computed, never raised out of.  The w=2 menu byte-matches R2's."""
    expected = {
        "w=1 mu0=3 w_U=1/3": [(8, 16, 5, 8, 2, True),
                              (10, 15, 7, 5, 3, False)],
        "w=2 mu0=3 w_U=2/3": [(7, 21, 4, 7, 3, True),
                              (8, 16, 5, 8, 4, True),
                              (10, 15, 7, 5, 6, False)],
        "w=3 mu0=3 w_U=1": [(8, 16, 5, 8, 6, True),
                            (10, 15, 7, 5, 9, False)],
        "w=4 mu0=5 w_U=1/5": [(29, 145, 24, 29, 5, True),
                              (45, 81, 40, 9, 9, False)],
        "w=6 mu0=2 w_U=1/2": [(15, 105, 13, 15, 7, True),
                              (21, 39, 19, 3, 13, False)],
        "w=3/2 mu0=2 w_U=1/2": [],
    }
    states = {
        "w=1 mu0=3 w_U=1/3": (Fraction(1), 3, Fraction(1, 3)),
        "w=2 mu0=3 w_U=2/3": (Fraction(2), 3, Fraction(2, 3)),
        "w=3 mu0=3 w_U=1": (Fraction(3), 3, Fraction(1)),
        "w=4 mu0=5 w_U=1/5": (Fraction(4), 5, Fraction(1, 5)),
        "w=6 mu0=2 w_U=1/2": (Fraction(6), 2, Fraction(1, 2)),
        "w=3/2 mu0=2 w_U=1/2": (Fraction(3, 2), 2, Fraction(1, 2)),
    }
    menus = {}
    for label, (w, mu0, w_u) in states.items():
        cells = e5_solve_mu1(w, mu0, w_u)
        got = [(c["dp"], c["dq"], c["nu_G"], c["M"], c["kbar"],
                c["t1_dead"]) for c in cells]
        require(got == expected[label],
                f"T1 regression menu changed on {label}")
        # Integer-w menus agree with the divisor closed form.
        if w.denominator == 1:
            menu = t1_divisor_menu(int(w))
            for c in cells:
                require(c["t1_dead"] == (c["kbar"] in menu),
                        "divisor menu disagrees with T1 verdict")
        menus[label] = got
    require(t1_divisor_menu(1) == [2] and t1_divisor_menu(2) == [3, 4]
            and t1_divisor_menu(3) == [4, 6]
            and t1_divisor_menu(4) == [5, 6, 8]
            and t1_divisor_menu(6) == [7, 8, 9, 12],
            "divisor menus changed")
    return {
        "law": "at mu = 1: dp | dq <=> M = dp <=> w/(kbar - w) in Z>=1; "
               "for integer w and integer kbar (DS1(c)): kbar in "
               "{w + d : d | w}.  Scope: the mu = 1 pinned zero-chain "
               "solve (s11's law home); at mu >= 2 only the identity "
               "below and the tautological M = dp leg survive",
        "identity": "kbar - w = w*dp/D at every mu (from kbar = "
                    "mu*w*dq/D and dp = mu*dq - D)",
        "w2_specialisation": "the {3,4} encoding is the w = 2 case and "
                             "must NEVER enter the engine at general w "
                             "(R2's s8.3 error; solver crashed on w=1,3)",
        "menus": {k: [list(c) for c in v] for k, v in menus.items()},
        "divisor_menus": {str(w): t1_divisor_menu(w)
                          for w in (1, 2, 3, 4, 6)},
    }


# ---------------------------------------------------------------------------
# Theorem D (the F1 repair): pattern-fibre finiteness.
def fibre_bound(mu: int, r: Fraction, nu: int, delta: int) -> Fraction:
    """The closed-form fibre bound: with r = dq/D = kbar/(mu*w) fixed and
    u = mu - 1/r > 0, every legal cell of the fibre satisfies

        s * (1 + u - ceil(u)) <= (1+nu)/(r*nu) + delta/nu.

    Proof: strict (NE) is m_j*dq < dp = mu*dq - D, i.e. m_j < mu - 1/r =
    u, so m_j <= ceil(u) - 1; with k <= s this gives A = mu*s - Sm >=
    s*(mu - ceil(u) + 1); and dq = r*D = r*(nu*A - delta) inverts to
    A = (1+nu+nu*s)/(r*nu) + delta/nu.  Subtract s/r from both sides.
    The left factor 1 + u - ceil(u) lies in (0, 1], so s is bounded and
    the fibre is finite; each member is pinned by its s (A, Sm, dp, dq
    are all determined by s once r, nu, delta, mu are fixed)."""
    require(mu >= 1 and nu >= 2 and delta >= 1 and r > 0,
            "bad fibre-bound arguments")
    u = mu - 1 / Fraction(r)
    require(u > 0, "fibre bound needs kbar > w (u > 0)")
    cu = ceil_fraction(u)
    slack = 1 + u - cu
    rhs = Fraction(1 + nu) / (r * nu) + Fraction(delta, nu)
    return rhs / slack


def fibre_solve(mu: int, w: Fraction, mu0: int, kbar: int,
                nu: int) -> dict[str, object]:
    """COMPLETE enumeration of the pattern-cell fibre over a fixed menu
    entry (kbar, nu_G) at state (mu, w, mu0), difficult regime.  Each
    member is re-certified through gap_pattern_certificate with an
    explicit witness pattern (so no NE-illegal member can enter; the R2
    fixtures bypassed exactly this gate)."""
    w = Fraction(w)
    delta = mu0 - mu
    require(delta >= 1 and nu >= 2 and Fraction(kbar) > w and w > 0,
            "fibre_solve scope: difficult regime, nu_G >= 2, kbar > w")
    r = Fraction(kbar) / (mu * w)
    bound = fibre_bound(mu, r, nu, delta)
    smax = bound.numerator // bound.denominator
    P, Q = r.numerator, r.denominator          # r = dq/D = P/Q reduced
    members = []
    for s in range(1, smax + 1):
        dq = 1 + nu * (1 + s)
        if dq % P:
            continue
        D = dq // P * Q
        dp = mu * dq - D
        rest = dp - mu0
        if rest < 0 or rest % nu:
            continue
        sm = rest // nu - mu
        if sm < 0:
            continue
        if sm == 0:
            k, mults = 0, ()
        else:
            cap = ne_cap(mu, dp, dq)
            if cap < 1 or ceil_div(sm, cap) > min(s, sm):
                continue                        # no strict-NE pattern
            k = ceil_div(sm, cap)
            mults = tuple([cap] * (sm // cap)
                          + ([sm % cap] if sm % cap else []))
        cert = gap_pattern_certificate(mu, mu0, nu, k, mults, s - k)
        require((cert["dp"], cert["dq"]) == (dp, dq),
                "fibre witness does not reproduce its cell")
        members.append({"s": s, "cell": [dp, dq], "Sm": sm,
                        "M": cert["M"]})
    return {"state": {"mu": mu, "w": fraction_text(w), "mu0": mu0},
            "kbar": kbar, "nu_G": nu, "r": fraction_text(r),
            "s_bound": fraction_text(bound), "members": members}


def fibre_box_census() -> dict[str, object]:
    """Independent replay of the review's F1c fibre census.

    Box: mu <= 7, delta <= 8, nu <= 30, k <= 5, lex <= 8; cells legal
    under (S) + strict (NE) + (R); fibre key (mu, mu0, nu_G, dq/D).
    Review-published targets, all replayed exactly: 92,772 distinct
    fibres, size histogram {1:92083, 2:486, 3:136, 4:63, 5:4}, ZERO
    violations of the Theorem D bound.  Additionally: every mu = 1 fibre
    is a singleton (at mu = 1, dq/D = (1+nu+nu*s)/(nu*s - delta) is
    strictly decreasing in s, so r pins s)."""
    fibres: dict[tuple, set] = {}
    cells = 0
    for mu in range(1, 8):
        for delta in range(1, 9):
            mu0 = mu + delta
            for nu in range(2, 31):
                for s in range(1, 14):          # k <= 5, lex <= 8
                    dq = 1 + nu * (1 + s)
                    for sm in range(0, min(5, s) * (mu - 1) + 1):
                        dp = mu0 + nu * (mu + sm)
                        D = mu * dq - dp
                        if D < 1:
                            continue
                        if sm == 0:
                            if s > 8:           # k = 0 needs lex = s <= 8
                                continue
                        else:
                            cap = ne_cap(mu, dp, dq)
                            if cap < 1:
                                continue
                            klo = max(1, s - 8, ceil_div(sm, cap))
                            if klo > min(5, s, sm):
                                continue
                        require(mu0 * dq > dp and dp != mu0 * dq,
                                "(S)/(R) 0-edge laws failed in census")
                        cells += 1
                        g = gcd(dq, D)
                        P, Q = dq // g, D // g
                        # Integer form of the Theorem D bound:
                        # s*(P + mu*P - Q - P*ceil((mu*P-Q)/P))*nu
                        #   <= (1+nu)*Q + delta*P.
                        cu = ceil_div(mu * P - Q, P)
                        slack_num = P + (mu * P - Q) - P * cu
                        require(1 <= slack_num <= P,
                                "fibre slack out of range")
                        require(s * slack_num * nu
                                <= (1 + nu) * Q + delta * P,
                                "Theorem D fibre bound violated in box")
                        fibres.setdefault((mu, mu0, nu, P, Q),
                                          set()).add(s)
    hist: dict[int, int] = {}
    for key, ss in fibres.items():
        hist[len(ss)] = hist.get(len(ss), 0) + 1
    require(cells == 93735, "box legal-cell count changed")
    require(len(fibres) == 92772,
            "fibre count must replay the review's 92,772")
    require(hist == {1: 92083, 2: 486, 3: 136, 4: 63, 5: 4},
            "fibre histogram must replay the review's F1c figures")
    require(all(len(fibres[k]) == 1 for k in fibres if k[0] == 1),
            "mu = 1 fibres must be singletons")
    summary = {
        "box": "mu<=7, delta<=8, nu<=30, k<=5, lex<=8",
        "legal_cells": cells, "fibres": len(fibres),
        "size_histogram": {str(n): hist[n] for n in sorted(hist)},
        "bound_violations": 0,
        "mu1_singletons": sum(1 for k in fibres if k[0] == 1),
    }
    return {"fibres": fibres, "summary": summary}


def fibre_complete_census(fibres: dict[tuple, set]) -> dict[str, object]:
    """CAP-FREE complete enumeration of every mu >= 2 box fibre up to its
    proved Theorem D bound (this replaces the review's s <= 400 capped
    deep search, whose 57,960 / 9 / s=27 figures did NOT replicate under
    any tested reading of its box -- see the report).  Every fibre is
    finite and fully enumerated: nothing is capped."""
    maxsize = maxs = eq_attained = 0
    argmax = argmaxs = None
    hist: dict[int, int] = {}
    keys = sorted(k for k in fibres if k[0] >= 2)
    for (mu, mu0, nu, P, Q) in keys:
        delta = mu0 - mu
        cu = ceil_div(mu * P - Q, P)
        slack_num = P + (mu * P - Q) - P * cu
        sb = ((1 + nu) * Q + delta * P) // (nu * slack_num)
        n = 0
        for s in range(1, sb + 1):
            dq = 1 + nu * (1 + s)
            if dq % P:
                continue
            D = dq // P * Q
            dp = mu * dq - D
            rest = dp - mu0
            if rest < 0 or rest % nu:
                continue
            sm = rest // nu - mu
            if sm < 0:
                continue
            if sm:
                cap = ne_cap(mu, dp, dq)
                if cap < 1 or ceil_div(sm, cap) > min(s, sm):
                    continue
            n += 1
            if s * slack_num * nu == (1 + nu) * Q + delta * P:
                eq_attained += 1
            if s > maxs:
                maxs, argmaxs = s, (mu, mu0, nu, P, Q)
        hist[n] = hist.get(n, 0) + 1
        if n > maxsize:
            maxsize, argmax = n, (mu, mu0, nu, P, Q)
    require(maxsize == 12 and argmax == (7, 15, 2, 15, 74),
            "complete-census maximum fibre changed")
    require(maxs == 1202 and argmaxs == (7, 15, 13, 170, 1019),
            "complete-census maximum member changed")
    require(eq_attained >= 1, "Theorem D bound never attained exactly")
    require(hist == {1: 79267, 2: 5261, 3: 2462, 4: 1461, 5: 950,
                     6: 642, 7: 481, 8: 251, 9: 144, 10: 25, 11: 8,
                     12: 5}, "complete-census histogram changed")
    return {
        "keys": len(keys),
        "max_fibre_size": maxsize,
        "max_fibre_key": "(mu,mu0,nu,dq/D) = (7,15,2,15/74)",
        "max_member_s": maxs,
        "max_member_key": "(7,15,13,170/1019); the Theorem D bound is "
                          "ATTAINED WITH EQUALITY there (s = 1202)",
        "bound_equality_keys": eq_attained,
        "size_histogram": {str(n): hist[n] for n in sorted(hist)},
    }


def seven4_fibre_certificate() -> dict[str, object]:
    """The repaired s7.4 record: the fibre at (mu,w,mu0) = (4,1,5),
    kbar = 2, nu_G = 3 is EXACTLY {(20,10), (26,13)} (bound s <= 3,
    attained).  R2's members (38,19) [s=5], (62,31) [s=9], (134,67)
    [s=21] and the inline s=45 member are NOT cells: dp = 2*dq forces
    m_j = 1 under strict (NE), so Sm = k <= s, but the family needs
    Sm = 2s - 3 > s for s >= 4.  Every candidate pattern of every
    withdrawn member is machine-refuted here."""
    solved = fibre_solve(4, Fraction(1), 5, 2, 3)
    require([m["cell"] for m in solved["members"]] == [[20, 10], [26, 13]],
            "s7.4 fibre must be exactly {(20,10),(26,13)}")
    require(solved["s_bound"] == "3", "s7.4 fibre bound must be 3")
    withdrawn = []
    for s in (4, 5, 9, 21, 45):
        dq = 1 + 3 * (1 + s)
        dp = 5 + 3 * (4 + 2 * s - 3)
        sm = 2 * s - 3
        require(dp == 2 * dq, "withdrawn member loses dp = 2*dq")
        # Enumerate EVERY pattern (k, mults, lex) with k + lex = s and
        # sum(mults) = Sm, mults in [1, mu-1] = [1,3]: all NE-illegal.
        patterns = legal = 0
        for k in range(1, s + 1):
            for mults in _tuples_summing(sm, k, 3):
                patterns += 1
                try:
                    gap_pattern_certificate(4, 5, 3, k, mults, s - k)
                    legal += 1
                except ValueError:
                    pass
        require(patterns >= 1 and legal == 0,
                "withdrawn fibre member admitted a legal pattern")
        withdrawn.append({"s": s, "cell": [dp, dq],
                          "candidate_patterns": patterns,
                          "legal_patterns": 0,
                          "reason": "NE forces m_j = 1, so Sm = k <= s "
                                    f"< {sm} = 2s-3"})
    return {"fibre": solved, "withdrawn_r2_members": withdrawn}


def _tuples_summing(total: int, k: int, cap: int, lo: int = 1):
    """All nondecreasing k-tuples of ints in [lo, cap] summing to total."""
    if k == 1:
        if lo <= total <= cap:
            yield (total,)
        return
    for first in range(lo, min(cap, total // k) + 1):
        for rest in _tuples_summing(total - first, k - 1, cap, first):
            yield (first,) + rest


# ---------------------------------------------------------------------------
# Theorems E and F (the F3 repair): arity-graded bound and MP2 scope.
def arity_census(r0: int, mumax: int, dmax: int, numax: int, kmax: int,
                 lexmax: int) -> dict[str, object]:
    """Equal-multiplicity r0-arrival census (r0 nonzero pole-chain edges
    of common mult mu, one 0-arrival mu0 = mu + delta, delta >= 1).

    Verifies on every legal cell:
      Theorem E   dq/D <= (r0+1) + ((r0+1)*delta + 1)/M, and
      the equality profile A' = 1, sigma = 1, nu = delta + M, D = M,
      M | (r0+1)*delta + 1;
    and collects every violator of the TWO-POLE constant 2*delta+3
    together with its M (Theorem F: at r0 in {2,3} every violator has
    M = 1, i.e. is MP2-dead as an interior merge)."""
    cells = eq_hits = 0
    violators = []
    for mu in range(1, mumax + 1):
        for delta in range(1, dmax + 1):
            mu0 = mu + delta
            for nu in range(2, numax + 1):
                for k in range(0, kmax + 1):
                    for lex in range(0, lexmax + 1):
                        sigma = k + lex
                        t = r0 - 1 + sigma
                        dq = 1 + nu * (1 + t)
                        for sm in (range(k, k * (mu - 1) + 1) if k
                                   else (0,)):
                            dp = mu0 + nu * (r0 * mu + sm)
                            D = mu * dq - dp
                            if D < 1:
                                continue
                            if sm:
                                cap = ne_cap(mu, dp, dq)
                                if cap < 1 or not k <= sm <= k * cap:
                                    continue
                            if dp == mu0 * dq:      # (R)
                                continue
                            cells += 1
                            M = gcd(dp, dq)
                            require(dq * M <= D * ((r0 + 1) * M
                                                   + (r0 + 1) * delta + 1),
                                    "Theorem E arity-graded bound failed")
                            if dq > D * (2 * delta + 3):
                                violators.append((dp, dq, M, delta))
                            if dq * M == D * ((r0 + 1) * M
                                              + (r0 + 1) * delta + 1):
                                eq_hits += 1
                                ap, rem = divmod(D + delta, nu)
                                require(rem == 0 and ap == 1
                                        and sigma == 1 and D == M
                                        and nu == delta + M
                                        and ((r0 + 1) * delta + 1) % M
                                        == 0,
                                        "Theorem E equality profile "
                                        "failed")
    return {"r0": r0, "cells": cells, "equality_hits": eq_hits,
            "violators": violators}


def arity_unequal_census() -> dict[str, object]:
    """Unequal arrival multiplicities (max mult distinguished): same
    Theorem E/F checks on a spot box; mu_i <= 5, delta <= 6, nu <= 24,
    k <= 2, lex <= 4, r0 in {2, 3}."""
    from itertools import combinations_with_replacement as cwr
    cells = 0
    violator_ms = set()
    for r0 in (2, 3):
        for mus in cwr(range(1, 6), r0):
            mumax_t, mumin_t, smu = max(mus), min(mus), sum(mus)
            for delta in range(1, 7):
                mu0 = mumax_t + delta
                for nu in range(2, 25):
                    for k in range(0, 3):
                        for lex in range(0, 5):
                            t = r0 - 1 + k + lex
                            dq = 1 + nu * (1 + t)
                            for sm in (range(k, k * (mumin_t - 1) + 1)
                                       if k else (0,)):
                                dp = mu0 + nu * (smu + sm)
                                D = mumax_t * dq - dp
                                if D < 1:
                                    continue
                                if any(m * dq <= dp for m in mus):
                                    continue          # (S) on every edge
                                if sm:
                                    cap = min(mumin_t - 1,
                                              (dp - 1) // dq)
                                    if cap < 1 or not k <= sm <= k * cap:
                                        continue
                                if dp == mu0 * dq:
                                    continue
                                cells += 1
                                M = gcd(dp, dq)
                                require(dq * M <= D * ((r0 + 1) * M
                                        + (r0 + 1) * delta + 1),
                                        "Theorem E failed (unequal box)")
                                if dq > D * (2 * delta + 3):
                                    violator_ms.add(M)
    require(cells == 75713, "unequal-box cell count changed")
    require(violator_ms == {1},
            "unequal-box two-pole violators must all be M = 1")
    return {"box": "r0 in {2,3}, mults <= 5, delta <= 6, nu <= 24, "
                   "k <= 2, lex <= 4",
            "cells": cells, "violator_M_values": [1]}


def theorem_ef_certificate() -> dict[str, object]:
    """Assemble Theorems E and F with the census evidence and the
    campaign-range scope statement."""
    wide2 = arity_census(2, 8, 12, 60, 3, 7)
    wide3 = arity_census(3, 8, 12, 60, 3, 7)
    require(wide2["cells"] == 357260 and wide3["cells"] == 439730,
            "arity census cell counts changed")
    require(len(wide2["violators"]) == 96
            and len(wide3["violators"]) == 248,
            "two-pole-constant violator counts changed")
    require(wide2["equality_hits"] == 312
            and wide3["equality_hits"] == 272,
            "Theorem E equality-hit counts changed")
    violator_ms = sorted({m for (_, _, m, _) in
                          wide2["violators"] + wide3["violators"]})
    require(all(vm == 1 for vm in violator_ms),
            "Theorem F refuted: an MP2-alive (M >= 2) cell exceeds the "
            "two-pole constant at r0 <= 3")
    unequal = arity_unequal_census()
    # r0 = 4 refutation witness (review F3): (44,46), four mu = 1
    # arrivals, mu0 = 8, nu = 9, k = 0, lex = 1.
    dp, dq, mu, mu0, nu, r0 = 44, 46, 1, 8, 9, 4
    delta = mu0 - mu
    D = mu * dq - dp
    M = gcd(dp, dq)
    require(dp == mu0 + nu * (r0 * mu) and dq == 1 + nu * (1 + r0),
            "(44,46) census identity failed")
    require(D == 2 and M == 2 and dq == 23 * D,
            "(44,46) must have D = M = 2, dq/D = 23")
    require(dq > D * (2 * delta + 3),
            "(44,46) must violate the two-pole constant (23 > 17)")
    require(dq * M == D * ((r0 + 1) * M + (r0 + 1) * delta + 1),
            "(44,46) must attain the r0 = 4 graded bound with equality")
    # Campaign range: MP1 (SHEET6-MULTIPOLE.md:82) gives r(G) <= m, and
    # the engine census (book_offaxis.py:49-54, TDMAX = 14) loops
    # m in range(2, td//3 + 1), so m <= 4 and r0 = r(G) - 1 <= 3.
    require(max(range(2, 14 // 3 + 1)) == 4,
            "campaign m-range changed")
    return {
        "theorem_E": {
            "statement": "dq/D <= (r0+1) + ((r0+1)*delta + 1)/M at an "
                         "interior merge with r0 >= 1 nonzero pole-chain "
                         "arrivals (mu = max mult, delta = mu0 - mu >= "
                         "1); r0 = 1 is Theorem B",
            "equality_necessity": "A' = 1, sigma = 1, nu_G = delta + M, "
                                  "D = M, M | (r0+1)*delta + 1 "
                                  "(verified on every equality hit)",
            "wide_equal_mu_box": "mu <= 8, delta <= 12, nu <= 60, "
                                 "k <= 3, lex <= 7",
            "r0_2": {"cells": wide2["cells"],
                     "equality_hits": wide2["equality_hits"]},
            "r0_3": {"cells": wide3["cells"],
                     "equality_hits": wide3["equality_hits"]},
            "unequal_mult_box": unequal,
        },
        "theorem_F": {
            "statement": "every (S)/(NE)/(R)-legal r0 in {2,3} cell with "
                         "dq/D > 2*delta+3 has M = 1 (MP2-dead as an "
                         "interior merge); PROVED (r0 = 2 from Theorem E "
                         "directly; r0 = 3 by the D in {2,3,4} case "
                         "analysis in the report), census-confirmed",
            "r0_2_violators_all_M1": len(wide2["violators"]),
            "r0_3_violators_all_M1": len(wide3["violators"]),
            "fails_at_r0_4": {"cell": [44, 46], "M": 2, "dq_over_D": 23,
                              "two_pole_constant": 17,
                              "graded_bound_equality": True},
            "campaign_range": "MP1 r(G) <= m (SHEET6-MULTIPOLE.md:82) "
                              "and the engine m <= td//3 <= 4 at "
                              "TDMAX = 14 (book_offaxis.py:39,49-54) "
                              "give r0 <= 3 in the campaign's range; "
                              "the no-MP2-alive-violator statement is "
                              "EXACTLY arity-graded: true at r0 in "
                              "{2,3}, false at r0 = 4",
        },
    }


# ---------------------------------------------------------------------------
def promoted_book_battery() -> dict[str, object]:
    """Recompute all 17 promoted s11a cells under the E5 pin (preserved
    from R2, review-confirmed) plus the F8.1 family qualifiers: the
    (4m-2, 6m-3) closed form covers the 12 alive kbar = 6 rows at ODD
    m = 3..25 only; the even-m members m = 4,6,8,10 are s11a's four
    recorded N1 kills (gcd(kbar, nu_G) = gcd(6, 3m-2) = 2), and the
    family terminates at m = 25 by CLOSURE EXHAUSTION (no priced state
    with w <= 2/27 at budget 5), not by any theorem here."""
    mu, w = BOOK_MU, BOOK_W
    opus_violations = []
    graded_equality_rows = []
    for (dp, dq, nu_g, M, mu0, kbar, w_U) in BOOK:
        delta = mu0 - mu
        D = mu * dq - dp
        require(gcd(dp, dq) == M and D >= 1, "book cell degrees corrupt")
        require(dp == mu0 + nu_g * mu and dq == 1 + nu_g * 2,
                "book pattern (k=0, lex=1) failed")
        cert = gap_pattern_certificate(mu, mu0, nu_g, 0, (), 1)
        require((cert["dp"], cert["dq"], cert["M"]) == (dp, dq, M),
                "pattern certificate mismatch on book cell")
        require(Fraction(kbar) == Fraction(mu * dq, 1) * w / D,
                "kbar = mu*w*dq/D failed")
        require(Fraction(kbar) <= kbar_bound(mu, w, delta),
                "Lemma A kbar bound failed on book cell")
        require(Fraction(kbar) <= kbar_bound(mu, w, delta, M),
                "Theorem B kbar bound failed on book cell")
        require(mu0 * nu_g * w_U == delta * kbar + mu * w,
                "E5 elimination identity failed on book cell")
        require(nu_g <= (delta * kbar_bound(mu, w, delta) + mu * w)
                / (mu0 * w_U), "nu_G bound failed on book cell")
        if cert["equality_graded"]:
            graded_equality_rows.append((dp, dq))
            require(kbar == 6 and nu_g == delta + M and D == M
                    and (2 * delta + 1) % M == 0,
                    "graded equality profile failed")
            require(Fraction(nu_g) == (delta * kbar_bound(mu, w, delta, M)
                                       + mu * w) / (mu0 * w_U),
                    "graded nu_G bound not tight on equality row")
        if nu_g > mu0 * w_U.numerator:
            opus_violations.append([dp, dq, nu_g, M, mu0])
        # Mixed pin on an E5 cell forces nu_U = nu_G (= CONJECTURE U_7C).
        h_mixed = (delta * kbar + mu * w) / (mu0 * w_U)
        require(h_mixed == nu_g, "mixed-pin index must equal nu_G")
        # Solver recovery.
        hits = [c for c in e5_solve_mu1(w, mu0, w_U)
                if (c["dp"], c["dq"], c["nu_G"], c["M"]) ==
                (dp, dq, nu_g, M)]
        require(len(hits) == 1 and not hits[0]["t1_dead"]
                and hits[0]["n1_ok"] and hits[0]["mp2_ok"],
                "solver failed to recover book cell alive")
    require(len(opus_violations) == 16,
            "Opus clause-4 violation count changed")
    require(len(graded_equality_rows) == 12,
            "graded equality must hold exactly on the 12 kbar=6 rows")
    # F8.1: the 12 graded rows are the ODD-m family members m = 3..25.
    require(graded_equality_rows ==
            [(4 * m - 2, 6 * m - 3) for m in range(3, 26, 2)],
            "kbar=6 family closed form must cover odd m = 3..25")
    # F8.1: even-m members are the four recorded N1 kills; the solver
    # finds them with n1_ok = False (never alive).
    for (dp, dq, nu_g, M, m) in N1_KILLED_EVEN_M:
        require((dp, dq, nu_g, M) == (4 * m - 2, 6 * m - 3, 3 * m - 2,
                                      2 * m - 1),
                "N1-killed family closed form failed")
        require(gcd(6, nu_g) == 2, "even-m N1 kill must have even nu_G")
        hits = [c for c in e5_solve_mu1(w, m, Fraction(2, m))
                if (c["dp"], c["dq"]) == (dp, dq)]
        require(len(hits) == 1 and not hits[0]["n1_ok"],
                "even-m family member must be found and N1-dead")
    # DEAD56 spot-cells reappear as T1-dead solver candidates.
    menu3 = e5_solve_mu1(w, 3, Fraction(2, 3))
    got = {(c["dp"], c["dq"], c["nu_G"], c["M"]) for c in menu3
           if c["t1_dead"]}
    require({(7, 21, 4, 7), (8, 16, 5, 8)} <= got,
            "T1-dead DEAD56 spot candidates missing from mu0=3 menu")
    return {
        "cells": len(BOOK),
        "graded_equality_rows": len(graded_equality_rows),
        "graded_equality_cells": graded_equality_rows,
        "opus_clause4_violations": len(opus_violations),
        "opus_clause4_violating_cells": opus_violations,
        "mixed_pin_index_equals_nu_G": len(BOOK),
        "solver_recovered": len(BOOK),
        "forced_subbook": [list(c) for c in FORCED_SUBBOOK],
        "family_qualifiers": {
            "alive_rows": "odd m = 3..25 of (4m-2, 6m-3); the even-m "
                          "members m = 4,6,8,10 are s11a's recorded N1 "
                          "kills (even nu_G = 3m-2)",
            "termination": "at m = 25 by closure exhaustion (no priced "
                           "state with w <= 2/27 at budget 5, s11a) -- "
                           "NOT by the theorems here",
        },
    }


def charged_slice() -> dict[str, object]:
    """The old td-7 discriminator slice (mu,w)=(1,2), (mu0,w_U)=(2,3/2),
    recomputed under BOTH pins.  Kill is reading-stable; provenance flags
    record that this slice replays RETRACTED BOOK-OFFAXIS s8 Step 3 and
    that the promoted @2 cell (9,15,7,3) lives on the untouched w_U=1/2
    slice.  Preserved verbatim from R2 (review-confirmed)."""
    mu, w, mu0, w_U = 1, Fraction(2), 2, Fraction(3, 2)
    delta = mu0 - mu
    kbar_max = kbar_bound(mu, w, delta)
    require(kbar_max == 10, "charged kbar bound must be 10")
    e5_rows = []
    for entry in e5_regimes(mu, w, mu0, w_U)["kbar_menu"]:
        kbar, nu_g = entry["kbar"], entry["nu_G"]
        require(3 * nu_g - 2 == kbar, "charged E5 slice identity failed")
        dp = mu0 + nu_g
        dq_f = Fraction(kbar * dp, kbar - 2)
        if dq_f.denominator != 1:
            e5_rows.append({"nu_G": nu_g, "kbar": kbar,
                            "verdict": "dq non-integral, DEAD"})
            continue
        dq = int(dq_f)
        M = gcd(dp, dq)
        verdict = ("T1-dead (kbar in {3,4})" if kbar in (3, 4) else
                   "M=1, MP2-dead" if M == 1 else "ALIVE")
        e5_rows.append({"nu_G": nu_g, "kbar": kbar, "cell": [dp, dq],
                        "M": M, "verdict": verdict})
    require([r["nu_G"] for r in e5_rows] == [2, 3, 4],
            "charged E5 nu_G menu must be {2,3,4}")
    require(e5_rows[0]["verdict"].startswith("T1-dead")
            and e5_rows[1]["verdict"] == "M=1, MP2-dead"
            and e5_rows[2]["verdict"].endswith("DEAD"),
            "charged E5 verdicts changed")
    require(e5_rows[1]["cell"] == [5, 7], "charged (5,7) cell lost")
    h_upper = (delta * kbar_max + mu * w) / (mu0 * w_U)
    require(int(h_upper) == 4, "mixed-pin h bound must be 4")
    mixed = {"h_upper": 4, "odd_ray_survivor": 3, "cell": [5, 7],
             "M": 1, "verdict": "MP2-dead (conditional on U_7C)"}
    return {
        "slice": {"mu": mu, "w": fraction_text(w), "mu0": mu0,
                  "w_U": fraction_text(w_U)},
        "e5_rows": e5_rows, "mixed_pin_rows": mixed,
        "kill_reading_stable": True,
        "provenance": {
            "replays": ("BOOK-OFFAXIS.md s8 Step 3 -- a RETRACTED "
                        "section; legitimate only as the w_U=3/2 "
                        "entry-state slice of class C, not as 'the' "
                        "td-7 ray"),
            "promoted_td7_slice": ("the promoted @2 cell (9,15,7,3) "
                                   "lives on w_U=1/2 and is untouched "
                                   "and unkilled by this slice"),
            "odd_ray_language": ("'h odd, h>=3' is a statement about "
                                 "nu_U; meaningful only under the mixed "
                                 "pin (nu_U free under E5)"),
        },
    }


# ---------------------------------------------------------------------------
def counterfixtures() -> dict[str, object]:
    """Exact certified reasons the two-pole theorem cannot be widened.

    R3 changes (review F1/F3): the false s7.4 'infinite pattern fibre'
    family is DELETED (its NE-illegal members are refuted in
    seven4_fibre_certificate; the true statement is Theorem D's
    finiteness); the r0 = 2 countercells now DISCLOSE that every one has
    D = 1, hence M = 1: they are MP2-dead as interior merges, exactly
    like Lemma A's sharpness witnesses.  They remain genuine engine-tier
    countercells: M_G = 1 rows reach solve_arr (expand2 yields
    MG in divisors(sum(mus)); no MP2 filter on that path; MP3 exempts
    strict ancestors of G*), so wholesale NUCAP replacement stays
    unsound -- but Theorem F now bounds the phenomenon: at r0 in {2,3}
    it is CONFINED to M_G = 1 rows."""
    r0_2 = []
    for (mu, delta) in ((2, 1), (2, 2), (3, 1), (3, 3), (5, 6), (7, 8)):
        mu0 = mu + delta
        nu = delta + 1
        m = mu - 1
        dp = mu0 + nu * (2 * mu + m)
        dq = 1 + 3 * nu
        D = mu * dq - dp
        require(D == 1 and dq == 3 * delta + 4,
                "r0=2 countercell arithmetic failed")
        require(mu * dq > dp and mu0 * dq > dp and m * dq < dp,
                "r0=2 countercell S/NE laws failed")
        require(all(dp != ms * dq for ms in {mu, m, mu0}),
                "r0=2 countercell R law failed")
        require(dq > D * (2 * delta + 3), "r0=2 cell fails to break bound")
        mg_cc = gcd(dp, dq)
        require(mg_cc == 1,
                "r0=2 countercell must be M = 1 (D = 1 forces it)")
        require(dq * mg_cc == D * (3 * mg_cc + 3 * delta + 1),
                "r0=2 countercell must attain Theorem E with equality")
        r0_2.append({"mu": mu, "mu0": mu0, "cell": [dp, dq],
                     "dq_over_D": dq, "two_pole_bound": 2 * delta + 3,
                     "M": 1, "mp2_dead_as_interior": True,
                     "theorem_E_equality": True})
    join = []
    mu, w = 3, Fraction(3)
    for nu in (4, 7, 100):
        dp, dq = 2 * mu * nu, 2 * nu + 1
        E = mu * dq - dp
        require(E == mu, "6a family E != mu")
        kbar = mu * w * Fraction(dq) / E
        require(kbar == w * dq, "6a kbar formula failed")
        M = gcd(dp, dq)
        require(M == 3 and dq % dp != 0, "6a family M/T1 profile failed")
        join.append({"nu": nu, "cell": [dp, dq],
                     "kbar": fraction_text(kbar), "M": M})
    require(Fraction(join[-1]["kbar"]) > 60 * Fraction(join[0]["kbar"]) / 10,
            "6a kbar growth not demonstrated")
    # Out-of-scope rows with M_G >= 2 that a migration gate (G-e') must
    # keep OPEN/capped (review F5.2: R2's gate set tested only M_G = 1
    # rows): r0 = 2 cell (15,9) M=3; r0 = 3 cell (12,16) M=4; r0 = 4
    # violator (44,46) M=2.
    ge_fixtures = []
    for (dp, dq, mus, mu0, nu, k, mults, lex) in (
            (15, 9, (2, 2), 3, 2, 2, (1, 1), 0),
            (12, 16, (1, 1, 1), 3, 3, 0, (), 2),
            (44, 46, (1, 1, 1, 1), 8, 9, 0, (), 1)):
        r0 = len(mus)
        smu = sum(mus)
        require(dp == mu0 + nu * (smu + sum(mults))
                and dq == 1 + nu * (r0 + k + lex),
                "G-e' fixture census identity failed")
        require(all(m * dq > dp for m in mus) and mu0 * dq > dp,
                "G-e' fixture (S) failed")
        require(all(mm * dq < dp for mm in mults),
                "G-e' fixture NE failed")
        require(dp != mu0 * dq, "G-e' fixture (R) failed")
        ge_fixtures.append({"cell": [dp, dq], "r0": r0, "M": gcd(dp, dq),
                            "mults": list(mus), "mu0": mu0, "nu": nu})
    require([f["M"] for f in ge_fixtures] == [3, 4, 2],
            "G-e' fixtures must carry M = 3, 4, 2")
    return {
        "r0_2_breaks_constant": r0_2,
        "r0_2_mp2_status": "ALL SIX are D = 1, M = 1, MP2-dead as "
                           "interior merges (review F3; same caveat as "
                           "Lemma A's sharpness witnesses); by Theorem F "
                           "no MP2-alive r0 in {2,3} violator exists",
        "equal_join_kbar_unbounded": join,
        "ge_prime_out_of_scope_fixtures": ge_fixtures,
        "inner_arrivals": ("an inner-merge edge (0-slot or partner) has "
                           "unknown w at solve time: the case-II "
                           "elimination is unavailable and no nu_G bound "
                           "is derivable from recorded data"),
        "consequence": ("wholesale replacement of NUCAP in solve_arr's "
                        "no-pin branch is UNSOUND: the branch also fires "
                        "on r0>=2 and inner-arrival rows (M_G = 1 rows "
                        "included); pattern-fibre finiteness (Theorem D) "
                        "does NOT rescue it -- the failure is arity/"
                        "inner-scope, not fibre-infinitude"),
    }


def no_incoming_bound_demo() -> dict[str, object]:
    """Prove-by-menu that no incoming nu_U bound follows or is required.

    On the promoted cell (18,27,13,9)@5 (state w_U = 2/5, M_U = 5): the
    legal arrival menu is the neutral congruence class nu_U = 4 (mod 5)
    plus the direct vertices {2, 7, 12} (s11a row; sol-h5a s6.2) -- an
    infinite menu.  The E5 pin (I4) computes kbar from (mu0, nu_G, w_U)
    only, so every sampled legal nu_U realizes the identical cell.

    GLOSS CORRECTED vs R2 (review F4 charge 5): the mixed pin reproduces
    the cell's kbar only at the VALUE nu_U = 13 = nu_G -- but 13 is NOT
    itself a legal arrival at this state (13+1 = 14 is not divisible by
    5, and 13 is not among the direct vertices {2,7,12}).  Imposing the
    mixed pin therefore KILLS this cell rather than leaving it
    U_7C-conditionally alive; exactly the s11a forced-nu sub-book, which
    keeps only (9,15,7,3)@2 and (10,15,7,5)@3.
    """
    dp, dq, nu_g, M, mu0, kbar, w_U = 18, 27, 13, 9, 5, 6, Fraction(2, 5)
    direct = (2, 7, 12)
    samples = [4, 9, 14, 10 ** 20 + 4]
    rows = []
    for nu_u in samples:
        require((nu_u + 1) % mu0 == 0, "sampled nu_U not neutral-legal")
        kbar_e5 = (mu0 * nu_g * w_U - 2) / (mu0 - 1)          # (I4)
        kbar_mixed = (mu0 * nu_u * w_U - 2) / (mu0 - 1)       # px5:244 pin
        require(kbar_e5 == kbar, "E5 kbar must not depend on nu_U")
        rows.append({"nu_U": str(nu_u),
                     "kbar_E5": fraction_text(kbar_e5),
                     "kbar_mixed": fraction_text(kbar_mixed),
                     "mixed_matches_cell": kbar_mixed == kbar})
    require(sum(1 for r in rows if r["mixed_matches_cell"]) == 0,
            "no sampled neutral nu_U != nu_G may satisfy the mixed pin")
    kbar_at_nu_g = (mu0 * nu_g * w_U - 2) / (mu0 - 1)
    require(kbar_at_nu_g == kbar, "nu_U = nu_G must reproduce the cell")
    # The F4-charge-5 legality facts, machine-checked:
    require((nu_g + 1) % mu0 != 0, "nu_G = 13 must NOT be neutral-legal")
    require(nu_g not in direct, "nu_G = 13 must NOT be a direct arrival")
    require((dp, dq, nu_g, M) not in FORCED_SUBBOOK,
            "(18,27,13,9) must be OUTSIDE the forced-nu sub-book")
    return {
        "cell": [dp, dq, nu_g, M], "mu0": mu0,
        "arrival_menu": "neutral nu_U = 4 (mod 5): infinite class; "
                        "direct {2, 7, 12}",
        "samples": rows,
        "mixed_pin_fate": ("kbar_mixed matches the cell only at nu_U = "
                           "13 = nu_G, which is NOT arrival-legal at "
                           "(2/5, M5): under the mixed pin this cell is "
                           "DEAD (forced-nu sub-book keeps only the two "
                           "equal-nu passers)"),
        "finiteness_source": ("finite priced (w_U, M_U) closure x finite "
                              "kbar menu (Lemma A) x finite pattern "
                              "fibre per menu entry (Theorem D); no "
                              "nu_U cap enters anywhere"),
        "conclusion": ("no incoming nu_U/nu_H bound follows from the "
                       "promoted laws, and none is required; the R1 "
                       "'incoming-index bound' bounded a mixed-pin "
                       "object that does not occur under E5"),
    }


# ---------------------------------------------------------------------------
def certificate() -> dict[str, object]:
    """Regenerate every certificate field from scratch and seal.

    Ordered so that cheap theorem gates run before the censuses; every
    field is rebuilt from legal cells only (no R2 field is copied)."""
    # Sharpness anchors for both bounds (delta = 1).
    eq_plain = gap_pattern_certificate(2, 3, 2, 1, (1,), 0)
    require(eq_plain["equality_plain"] and eq_plain["D"] == 1
            and eq_plain["M"] == 1, "plain sharpness fixture failed")
    eq_graded = gap_pattern_certificate(1, 2, 4, 0, (), 1)
    require(eq_graded["equality_graded"] and eq_graded["M"] == 3
            and eq_graded["D"] == 3, "graded sharpness fixture failed")
    regimes = {
        "mu0<mu": e5_regimes(3, Fraction(5), 2, Fraction(1)),
        "mu0=mu": e5_regimes(2, Fraction(3, 2), 2, Fraction(1, 2)),
        "mu0>mu": e5_regimes(1, Fraction(2), 2, Fraction(1, 2)),
    }
    require(regimes["mu0<mu"]["nu_G_menu"] == [2, 3, 4],
            "REVERSE-regime strict menu changed")
    require(regimes["mu0=mu"]["forced_nu_G"] == "3"
            and regimes["mu0=mu"]["legal_case_iii"] is True
            and regimes["mu0=mu"]["kbar_pinned"] is False,
            "EQUAL-regime record changed")
    require(any(e["nu_G"] == 7 and e["kbar"] == 5
                for e in regimes["mu0>mu"]["kbar_menu"]),
            "DIFFICULT-regime menu lost the promoted @2 entry")
    t1 = t1_regression()
    seven4 = seven4_fibre_certificate()
    fixtures = counterfixtures()
    book = promoted_book_battery()
    slice_ = charged_slice()
    demo = no_incoming_bound_demo()
    ef = theorem_ef_certificate()
    box = fibre_box_census()
    complete = fibre_complete_census(box["fibres"])
    firewall = {
        "mixed_pin_licensed": False,
        "u7c_adjudicated": False,
        "incoming_index_bounded": False,
        "nucap_removal_authorized": False,
        "canonical_engine_changed": False,
        "equal_nonzero_join_kbar_bounded": False,
        "multipole_merges": False,
        "inner_arrival_merges": False,
        "full_merge_grammar": False,
        "realizability": False,
        "landing": False,
        "degree_bound": False,
        "jc2": False,
        "aws_or_fleet_action": False,
        "r2_fibre_infinitude_reinstated": False,
        "t1_w2_encoding_reinstated": False,
    }
    require(all(v is False for v in firewall.values()),
            "claim firewall must be all-False")
    payload: dict[str, object] = {
        "schema": SCHEMA,
        "repairs": "cases/m2_caseiii_two_pole_e5_local_index_r2_20260829 "
                   "(R1 and R2 byte-untouched) after the Opus 5 R2 "
                   "hostile review (REPAIR_REQUIRED, body c12bbca2...)",
        "reading": {
            "pin": "promoted Q+E5 (H5a resolved: sol-h5a.md Props 1-2, "
                   "grok-h5a-review.md SOUND, BOOK-OFFAXIS.md s11-PRE/"
                   "s11a)",
            "case_iii_handshake": "X = mu0*(kbar - nu_G*w_U)",
            "u7c_fork": "the mixed/printed pin X = mu0*(kbar - nu_U*w_U) "
                        "is coherent only under open CONJECTURE U_7C; "
                        "imposing it on E5-realizable cells forces "
                        "nu_U = nu_G identically (and kills every cell "
                        "whose nu_G is not arrival-legal)",
        },
        "theorem_scope": "TWO-POLE CASE-III INTERIOR MERGES ONLY "
                         "(one nonzero pole-chain edge, one pole-chain "
                         "0-arrival, nu_G >= 2, no inner edges)",
        "lemma_A": {
            "statement": "dq/D <= 2*delta+3 and kbar = mu*w*dq/D <= "
                         "mu*w*(2*delta+3), reading-independent",
            "equality": "iff nu_G = delta+1, s = 1, A = 1; then D = M = 1:"
                        " every sharpness witness is MP2-dead",
            "sharpness_fixture": eq_plain,
        },
        "theorem_B": {
            "statement": "dq/D <= 2 + (2*delta+1)/M with M = gcd(dp,dq)",
            "equality": "iff M | 2*delta+1 (M odd), s = 1, A = 1, "
                        "nu_G = delta+M (then D = M exactly)",
            "book_equality_rows": book["graded_equality_rows"],
            "sharpness_fixture": eq_graded,
        },
        "theorem_C": {
            "elimination": "mu0*nu_G*w_U = delta*kbar + mu*w",
            "regimes": regimes,
            "no_incoming_bound": demo,
        },
        "theorem_D": {
            "statement": "the pattern-cell fibre over any fixed "
                         "(kbar, nu_G) menu entry at a two-pole state is "
                         "ALWAYS FINITE: s*(1 + u - ceil(u)) <= "
                         "(1+nu)/(r*nu) + delta/nu with r = dq/D = "
                         "kbar/(mu*w), u = mu - 1/r > 0; each member is "
                         "pinned by its s; the bound is SHARP (attained "
                         "with equality in the census)",
            "withdraws": "R2 s7.4 'pattern fibre can be infinite' -- "
                         "FALSE; its (38,19)/(62,31)/(134,67) members "
                         "and the inline s=45 member are NE-illegal and "
                         "are deleted from every fixture and manifest",
            "mu1_singleton_lemma": "at mu = 1, dq/D is strictly "
                                   "decreasing in s, so every fibre is "
                                   "a singleton",
            "seven4_fibre": seven4,
            "box_census": box["summary"],
            "complete_census": complete,
            "opus_deep_search_note": "the review's capped deep-search "
                                     "figures (57,960 fibres / max 9 / "
                                     "terminal s = 27) did NOT replicate "
                                     "under any tested reading of its "
                                     "box and are NOT incorporated; the "
                                     "cap-free complete census above "
                                     "supersedes them",
        },
        "theorems_E_F": ef,
        "lemma_T1prime": t1,
        "promoted_book": book,
        "charged_slice": slice_,
        "counterfixtures": fixtures,
        "notation_correction": (
            "REGENERATED (R1's field asserted the inverse): under the "
            "promoted Q+E5 pin the case-III handshake carries the "
            "merge-local nu_G; the incoming index nu_U (R1's 'h = nu_H') "
            "cancels into the state invariant w_U and is FREE -- no "
            "incoming bound exists, follows, or is required.  R1's "
            "headline bound is the mixed-pin reading, coherent only "
            "under CONJECTURE U_7C."),
        "opus_adjudication": {
            "r1_said": "Opus Thm 2.4/4 'correctly bounds nu_G' but "
                       "misnames it nu_H",
            "correction_direction_1": (
                "too generous: clause 4 nu <= mu0*num(w_0) binds NEITHER "
                "index -- as a nu_G bound 16/17 promoted cells violate "
                "it; as a nu_U bound the mixed-legal forced-subbook cell "
                "(9,15,7,3)@2 violates it (nu_U = 7 > 2); its (4a) route "
                "applies the case-II transport to the 0-edge, matching "
                "neither recorded case-III reading"),
            "correction_direction_2": (
                "too harsh: Opus did not confuse two symbols -- its s10c "
                "states the H5a fork verbatim and declines to "
                "adjudicate; the unlicensed step is Theorem 4(4a) fed "
                "the 0-edge, not the naming"),
            "sound_replacement": (
                "kbar <= mu*w*(2*delta+3) (reading-free) plus "
                "mu0*nu_G*w_U = delta*kbar + mu*w, giving nu_G <= "
                "mu*w*(delta*(2*delta+3)+1)/(mu0*w_U) per arriving "
                "state; M-graded form tight on the kbar=6 family"),
            "r2_review_adjudication": (
                "accepted and repaired: F1 (fibre infinitude refuted -> "
                "Theorem D), F2 (T1 w=2-only -> Lemma T1'), F3 (M=1 "
                "disclosure + Theorems E/F), F5/R4 (migration plan "
                "rewritten), F8 nits (family and nu_U=13 glosses); "
                "diverges: the review's capped deep-search census did "
                "not replicate and is superseded by the cap-free "
                "complete census; strengthened: Theorem F upgrades the "
                "review's empirical r0=3 no-MP2-alive claim to a "
                "proved theorem"),
        },
        "engine_consequence": {
            "nucap": "STAYS.  Honest fate is removal-by-rebuild (no nu_H "
                     "loop exists under E5), not replacement-by-cap; "
                     "wholesale cap replacement is UNSOUND on r0>=2 and "
                     "inner-arrival rows (certified countercells, all "
                     "M=1 at r0<=3 by Theorem F)",
            "migration_plan": "report s8 / README: two-pole rows solve "
                              "by the finite kbar menu x elimination "
                              "(Theorem-B graded menu licensed since "
                              "cell_check pins gcd = M_G exactly); "
                              "out-of-scope rows KEEP the legacy path "
                              "byte-identical ('bypass on the scoped "
                              "path', never 'retire'); cell_check is "
                              "retained as a CONSERVATIVE existence "
                              "gate (Theorem D makes the finite cell "
                              "book available but does not require it)",
        },
        "inventory_r2_to_r3": {
            "preserved_verbatim": [
                "Lemma A", "Theorem B", "Theorem C + no-incoming-bound "
                "proposition", "gap_pattern_certificate", "kbar_bound",
                "e5_eliminate_nu_g", "charged_slice", "BOOK/"
                "FORCED_SUBBOOK/DEAD56_SPOT", "MUT_A..MUT_F",
            ],
            "repaired": [
                "e5_solve_mu1 (general-w T1 gate; total on legal input)",
                "e5_regimes (named regimes; EQUAL-regime kbar_pinned "
                "field)",
                "counterfixtures (fibre family deleted; M=1/MP2-dead "
                "disclosure; G-e' M_G>=2 fixtures)",
                "no_incoming_bound_demo (nu_U = 13 arrival-legality "
                "gloss)",
                "promoted_book_battery (even-m N1 family; termination "
                "qualifier)",
                "certificate (rebuilt; the R2 infinite-fibre field is "
                "REMOVED and replaced by theorem_D)",
            ],
            "withdrawn": [
                "s7.4 infinite-fibre claim and its NE-illegal members "
                "(38,19), (62,31), (134,67), inline s=45",
                "s8.3 T1 gate 'dp | dq <=> kbar in {3,4}' at general w",
            ],
            "new": [
                "Theorem D (fibre finiteness + sharp bound) with "
                "fibre_bound/fibre_solve/fibre_box_census/"
                "fibre_complete_census/seven4_fibre_certificate",
                "Theorem E (arity-graded bound + equality profile)",
                "Theorem F (no MP2-alive r0<=3 violator; r0=4 witness)",
                "Lemma T1' with t1_closed_form/t1_divisor_menu/"
                "t1_regression", "ne_cap (true strict-NE cap)",
                "MUT_G/MUT_H/MUT_I/MUT_J permanent mutations",
            ],
        },
        "firewall": firewall,
    }
    body = json.dumps(payload, sort_keys=True,
                      separators=(",", ":")).encode()
    payload["certificate_sha256"] = hashlib.sha256(body).hexdigest()
    return payload


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output")
    args = parser.parse_args(list(argv) if argv is not None else None)
    blob = json.dumps(certificate(), indent=2, sort_keys=True) + "\n"
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(blob)
    else:
        print(blob, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
