#!/usr/bin/env python3
"""Two-pole case-III merge under the promoted Q+E5 pin (R2 repair packet).

Supersedes the READING of cases/m2_caseiii_two_pole_nuh_bound_r1_20260829
(R1 stays byte-untouched).  R1 proved correct merge arithmetic but pinned
the case-III handshake as X = mu0*(kbar - nu_H*w0) -- the printed
Prop 9.3(g),(h)/"mixed" reading, refuted by the promoted H5a resolution
(xmodel/sol-h5a.md Props 1-2, hostile-reviewed SOUND, BOOK-OFFAXIS.md
s11-PRE/s11a) unless open CONJECTURE U_7C holds.  Under the promoted
Q+E5 pin the handshake i-normalizes to

    X = mu0*(kbar - nu_G*w_U),

so the eliminated index is the MERGE-LOCAL nu_G, and the incoming index
nu_U is FREE (infinite neutral congruence menus).  This module re-founds
every R1 object on that pin:

  * Lemma A  (reading-independent): at a two-pole case-III merge with
    delta = mu0 - mu >= 1,  dq/D <= 2*delta + 3  and
    kbar = mu*w*dq/D <= mu*w*(2*delta+3); equality forces D = M = 1
    (every sharpness witness is MP2-dead).
  * Theorem B (M-graded refinement, new): dq/D <= 2 + (2*delta+1)/M with
    M = gcd(dp,dq); equality iff M | 2*delta+1 (hence M odd) and the
    cell is the s=1, A=1, nu_G = delta+M pattern (then D = M exactly).
    12 of the 17 promoted s11a cells (the whole kbar=6 family) attain it.
  * Theorem C (E5 elimination): mu0*nu_G*w_U = delta*kbar + mu*w, with
    sharp merge-local nu_G bounds in all three multiplicity regimes and
    a proof-by-menu that no incoming nu_U/nu_H bound follows or is
    required.

Scope: interior two-pole case-III merges ONLY -- exactly one nonzero
arriving pole-chain edge (mu, w), one pole-chain 0-arrival (mu0, w_U),
nu_G >= 2, no inner-merge arrivals.  Counterfixtures certify that every
widening fails.  Exact rational arithmetic throughout; no CAS; the
canonical engine cases/book_offaxis.py is NOT modified and NUCAP stays.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import gcd
from typing import Iterable

SCHEMA = "m2-caseiii-two-pole-e5-local-index-r2"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def fraction_text(value: Fraction) -> str:
    value = Fraction(value)
    return (str(value.numerator) if value.denominator == 1 else
            f"{value.numerator}/{value.denominator}")


def ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


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
# that reappear as kbar in {3,4} candidates of the E5 solve below.
DEAD56_SPOT = ((7, 21, 4, 7), (8, 16, 5, 8), (5, 15, 2, 5), (5, 10, 3, 5))


# ---------------------------------------------------------------------------
def gap_pattern_certificate(mu: int, mu0: int, nu: int, k: int,
                            mults: tuple[int, ...],
                            lex: int) -> dict[str, object]:
    """Certify one two-pole case-III pattern cell and both ratio bounds.

    Reading-independent: uses only the R1.0/R2.2 pattern and the (S)/(NE)/
    (R) laws -- no handshake, no w, no H5a-sensitive object.  All laws are
    hard gates (repairing R1's acceptance of NE-illegal and nu=1 inputs):
    nu >= 2 (a nu_G = 1 merge is case I, out of case-III scope), strict NE
    on every non-chain orbit, 0-edge searrow, root-mult law.
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
    """
    require(isinstance(mu, int) and mu >= 1, "mu must be a positive integer")
    require(isinstance(mu0, int) and mu0 >= 1,
            "mu0 must be a positive integer")
    require(isinstance(w, Fraction) and w > 0, "w must be positive")
    require(isinstance(w_U, Fraction) and w_U > 0, "w_U must be positive")

    if mu0 < mu:
        # kbar > w (handshake: kbar - w = w*dp/D > 0) gives
        # mu0*nu_G*w_U = mu*w - (mu-mu0)*kbar < mu*w - (mu-mu0)*w = mu0*w,
        # hence the STRICT bound nu_G < w/w_U (sharper than the R1-form
        # mu*w/(mu0*w_U), which only used kbar > 0).
        strict = w / w_U
        top = ceil_fraction(strict) - 1
        menu = list(range(2, top + 1))
        return {
            "regime": "mu0<mu", "strict_upper_nu_G": fraction_text(strict),
            "nu_G_menu": menu,
            "reason": "kbar > w forces mu0*nu_G*w_U < mu0*w",
        }
    if mu0 == mu:
        forced = w / w_U
        legal = forced.denominator == 1 and forced >= 2
        return {
            "regime": "mu0=mu", "forced_nu_G": fraction_text(forced),
            "legal_case_iii": bool(legal),
            "reason": ("delta = 0 degenerates the elimination to "
                       "nu_G*w_U = w exactly; nu_G = 1 is case-I "
                       "territory, not a case-III merge"),
        }
    # Difficult regime: finite kbar menu from Lemma A, then one nu_G per
    # kbar from the elimination.  This finite menu is the cap-free
    # replacement of the legacy nu_H loop: no incoming index exists.
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


def e5_solve_mu1(w: Fraction, mu0: int, w_U: Fraction) -> list[dict]:
    """Full pinned-cell E5 solve for a mu = 1 nonzero partner.

    With mu = 1 the pattern pins dp = mu0 + nu_G exactly (P = 1, k = 0
    forced by m_j <= mu-1 = 0), so each (kbar, nu_G) menu entry yields at
    most one cell.  Post-filters are recorded, not silently dropped:
    T1 zero-chain law (dp | dq  <=>  kbar in {3,4}), N1 primitivity
    gcd(kbar, nu_G) = 1, MP2 (M >= 2), q-shape s >= 1.
    """
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
        require(t1_dead == (kbar in (3, 4)),
                "T1 encodings dp|dq and kbar in {3,4} disagree")
        out.append({
            "dp": dp, "dq": dq, "nu_G": nu_g, "M": M, "kbar": kbar,
            "s": s, "t1_dead": t1_dead, "n1_ok": gcd(kbar, nu_g) == 1,
            "mp2_ok": M >= 2,
        })
    return out


# ---------------------------------------------------------------------------
def promoted_book_battery() -> dict[str, object]:
    """Recompute all 17 promoted s11a cells under the E5 pin.

    Verifies per cell: the pattern (k=0, lex=1 forced at mu=1), the
    reading-independent kbar law and both Lemma A / Theorem B bounds, the
    E5 elimination identity, the transplanted nu_G bound, the M-graded
    equality census (exactly the 12 kbar=6 rows), the solver recovery,
    the Opus clause-4 violation count (16/17), and that the mixed pin's
    required incoming index equals nu_G identically (imposing the mixed
    pin on E5 cells = CONJECTURE U_7C).
    """
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
    }


def charged_slice() -> dict[str, object]:
    """The old td-7 discriminator slice (mu,w)=(1,2), (mu0,w_U)=(2,3/2),
    recomputed under BOTH pins.  Kill is reading-stable; provenance flags
    record that this slice replays RETRACTED BOOK-OFFAXIS s8 Step 3 and
    that the promoted @2 cell (9,15,7,3) lives on the untouched w_U=1/2
    slice."""
    mu, w, mu0, w_U = 1, Fraction(2), 2, Fraction(3, 2)
    delta = mu0 - mu
    kbar_max = kbar_bound(mu, w, delta)
    require(kbar_max == 10, "charged kbar bound must be 10")
    # E5 side: 3*nu_G = kbar + 2 <= 12 => nu_G in {2,3,4}.
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
    # Mixed side (R1's computation, conditional on U_7C): h <= 4, odd ray
    # h >= 3 leaves h = 3, same (5,7) cell, M = 1, MP2-dead.
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
    """Exact certified reasons the two-pole theorem cannot be widened."""
    # (i) r0 = 2: two equal-mu nonzero arrivals + 0-edge.  nu = delta+1,
    # k = 1, m = mu-1, lex = 0 gives D = 1 and dq/D = 3*delta+4 > 2*delta+3
    # while satisfying (S) on all three edges, strict (NE), and (R).
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
        r0_2.append({"mu": mu, "mu0": mu0, "cell": [dp, dq],
                     "dq_over_D": dq, "two_pole_bound": 2 * delta + 3})
    # (ii) Equal-(mu,w) join with NO 0-edge (Opus 6a family): kbar is
    # affine-unbounded in nu -- no constant exists at all.  Members pass
    # (S) [vacuous], (R), T1, MP2 (3 | 2nu+1).
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
    # (iii) Pattern-fibre caveat (new): at FIXED (kbar, nu_G) with a
    # mu >= 2 partner and kbar < mu*w, the cell fibre can be infinite.
    # Family: mu=4, w=1, mu0=5 (delta=1), nu_G=3, kbar=2; s free with
    # A = 3+2s, Sm = 2s-3; members (20,10),(26,13),(38,19),(62,31),...
    fibre = []
    for s in (2, 3, 5, 9, 21):
        A = 3 + 2 * s
        sm = 2 * s - 3
        dq = 1 + 3 * (1 + s)
        dp = 5 + 3 * (4 + sm)
        D = 4 * dq - dp
        require(D == 2 * dq, "fibre family D identity failed")
        require(Fraction(4 * 1 * dq, D) == 2, "fibre kbar != 2")
        require(4 * dq > dp and 5 * dq > dp, "fibre searrow failed")
        require(sm == 0 or any(k <= sm <= 3 * k for k in range(1, s + 1)),
                "fibre NE census infeasible")
        fibre.append({"s": s, "cell": [dp, dq], "M": gcd(dp, dq)})
    require(len({f["M"] for f in fibre}) == len(fibre),
            "fibre family M values must grow")
    return {
        "r0_2_breaks_constant": r0_2,
        "equal_join_kbar_unbounded": join,
        "pattern_fibre_infinite_at_fixed_kbar_nu_G": fibre,
        "inner_arrivals": ("an inner-merge edge (0-slot or partner) has "
                           "unknown w at solve time: the case-II "
                           "elimination is unavailable and no nu_G bound "
                           "is derivable from recorded data"),
        "consequence": ("wholesale replacement of NUCAP in solve_arr's "
                        "no-pin branch is UNSOUND: the branch also fires "
                        "on r0>=2 and inner-arrival rows"),
    }


def no_incoming_bound_demo() -> dict[str, object]:
    """Prove-by-menu that no incoming nu_U bound follows or is required.

    On the promoted cell (18,27,13,9)@5 (state w_U = 2/5, M_U = 5): the
    legal arrival menu contains the full neutral congruence class
    nu_U = -1 (mod 5) -- infinite.  The E5 pin (I4) computes kbar from
    (mu0, nu_G, w_U) only, so every sampled nu_U realizes the identical
    cell; the mixed pin varies with nu_U and reproduces the cell's kbar
    exactly at nu_U = nu_G = 13, i.e. imposing it is CONJECTURE U_7C.
    """
    dp, dq, nu_g, M, mu0, kbar, w_U = 18, 27, 13, 9, 5, 6, Fraction(2, 5)
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
    return {
        "cell": [dp, dq, nu_g, M], "mu0": mu0,
        "arrival_menu": "neutral nu_U = 4 (mod 5): infinite class",
        "samples": rows,
        "finiteness_source": ("finite priced (w_U, M_U) closure x finite "
                              "kbar menu (Lemma A); no nu_U cap enters"),
        "conclusion": ("no incoming nu_U/nu_H bound follows from the "
                       "promoted laws, and none is required; the R1 "
                       "'incoming-index bound' bounded a mixed-pin "
                       "object that does not occur under E5"),
    }


# ---------------------------------------------------------------------------
def certificate() -> dict[str, object]:
    """Regenerate every certificate field from scratch and seal."""
    book = promoted_book_battery()
    slice_ = charged_slice()
    fixtures = counterfixtures()
    demo = no_incoming_bound_demo()
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
            "regime-1 strict menu changed")
    require(regimes["mu0=mu"]["forced_nu_G"] == "3"
            and regimes["mu0=mu"]["legal_case_iii"] is True,
            "regime-2 forced value changed")
    require(any(e["nu_G"] == 7 and e["kbar"] == 5
                for e in regimes["mu0>mu"]["kbar_menu"]),
            "regime-3 menu lost the promoted @2 entry")
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
    }
    require(all(v is False for v in firewall.values()),
            "claim firewall must be all-False")
    payload: dict[str, object] = {
        "schema": SCHEMA,
        "supersedes_reading_of":
            "cases/m2_caseiii_two_pole_nuh_bound_r1_20260829 (R1 "
            "byte-untouched)",
        "reading": {
            "pin": "promoted Q+E5 (H5a resolved: sol-h5a.md Props 1-2, "
                   "grok-h5a-review.md SOUND, BOOK-OFFAXIS.md s11-PRE/"
                   "s11a)",
            "case_iii_handshake": "X = mu0*(kbar - nu_G*w_U)",
            "u7c_fork": "the mixed/printed pin X = mu0*(kbar - nu_U*w_U) "
                        "is coherent only under open CONJECTURE U_7C; "
                        "imposing it on E5-realizable cells forces "
                        "nu_U = nu_G identically",
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
        },
        "engine_consequence": {
            "nucap": "STAYS.  Honest fate is removal-by-rebuild (no nu_H "
                     "loop exists under E5), not replacement-by-cap; "
                     "wholesale cap replacement is UNSOUND on r0>=2 and "
                     "inner-arrival rows (certified countercells)",
            "migration_plan": "report s8 / README: two-pole rows solve "
                              "by the finite kbar menu x elimination "
                              "(td7_census_e5.py style); out-of-scope "
                              "rows keep NUCAP + OPEN",
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
