#!/usr/bin/env python3
"""LL-1 (td=6, m=2) full-actual-floor landing ledger -- R4, 2026-08-29.

R4 is a narrow carrier-typing and price upgrade of the reviewed R3 packet.
It preserves the R3 grammar, merge classification, exact-Q arithmetic, and
legacy representative prices, while adding one independently reviewed input:
the two-pole ``FULL_ACTUAL_FIRST_SEPARATION`` theorem.  Its exact delta is:

  R-8  Every nonzero actual up direction emitted by this LL-1 two-pole
       consumer is explicitly typed ``FULL_ACTUAL_FIRST_SEPARATION`` (the
       floor-valued canonical alias of ``FULL_ACTUAL_EXIT``).  Its complete
       distinct cv carrier is priced by ``delta`` for positive integral
       ``delta`` and ``ceil(2*delta)`` otherwise.  This is a lower floor only,
       never attainment.  The representative AF2 function remains available
       under its own ``REPRESENTATIVE`` type and is emitted beside the applied
       floor for audit.  The epsilon/zero direction keeps the old AF2 rule.
  R-9  Exactly four nonzero ``delta=2/3`` cells rise by one; the deterministic
       reduced-superset inventory changes from 13 to 7.  The packet emits and
       validates the exact four movers, seven survivors, and six removed rows,
       while preserving ``ALIVE`` as a conservative superset predicate.
  R-10 The carrier theorem, stable hostile review, legacy reprice evidence,
       frozen R3 input, and current canonical carrier riders are hash-pinned.
       Canonical source anchors and theorem body seals fail closed on drift.

R3 was the narrow provenance/test-quality repair of the R2 packet
(cases/landing_ledger_ll1_r2_20260829/, report body 29e892da...), per the
R2 hostile review (xmodel/landing-ledger-ll1-r2-hostile-review-grok46-
20260829.md, body 3673da47..., verdict PASS_AT_LL1_SCOPE).  The R2
mathematics and all reviewed LL-1 decisions are preserved verbatim; R3
changes ONLY the provenance layer and the A1 engine-parity gate:

  R-6  Source pins re-issued against the exact CURRENT bytes of
       ladder/BOOK-OFFAXIS.md and ladder/REDUCTION.md (the two R2 pins
       that failed to reproduce), alongside the two pins that already
       match (SHEET6-MULTIPOLE.md, SHEET6-DEPTH.md) and one new fixture
       pin (SHEET6-DEPTH-REVIEW.md).  compile_book() and the validator
       verify all five pins and the consumed clause anchors against the
       byte-exact files and FAIL CLOSED on any drift.
  R-7  The R2 A1 check `all(2*nu+2 == 2*nu+2 ...)` (a tautology) is
       replaced by an honest frozen-fixture parity gate: the charged
       26-shape / 351-route figures are PARSED from the pinned bytes of
       SHEET6-DEPTH.md and SHEET6-DEPTH-REVIEW.md (count-free regexes:
       no expected count is baked into the parser), cross-checked for
       internal consistency, and compared against the packet's own
       derived data (entry w0, W(2), the IIa child Q=(6,12,3,2,5), the
       DS4 identity w*(dq,dp,1)/(dq-dp)).  The engine
       (cases/twopole_check.py phase 4) is NOT re-run and the counts
       are NOT re-derived: they stay fixture-cited, and the book says
       so explicitly.  Parity is never manufactured: a drifted or
       missing charged sentence aborts the compile.

R2/R3 lineage (unchanged, still enforced by this compiler and its tests) --
repairs R-1..R-5 of the sealed LL-1 design (xmodel/landing-ledger-primary-
research-fable5-20260829.md, body 83fe2312...), per the first hostile
review (xmodel/landing-ledger-primary-research-fable5-hostile-review-
grok46-20260829.md, body 88c1d66f...):

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
import re
import sys

TD = 6
M_POLES = 2

REPRESENTATIVE = "REPRESENTATIVE"
FULL_ACTUAL_FIRST_SEPARATION = "FULL_ACTUAL_FIRST_SEPARATION"
FULL_ACTUAL_EXIT = "FULL_ACTUAL_EXIT"
LOWER_FLOOR_ONLY = "LOWER_FLOOR_ONLY"

# Exact immutable evidence consumed by the R4 carrier/price promotion.  Full
# hashes are verified on every compile.  For sealed mathematical reports the
# byte-prefix body seal is verified independently as well.
EVIDENCE_PINS = {
    "xmodel/m2-two-pole-full-actual-first-separation-theorem-r1-sol56-20260829.md":
        "82d2f6c3eb2c3985569da428def3d5c2e125ca5b0aa29ebfc7973b68ee843a7a",
    "xmodel/m2-two-pole-full-exit-attachment-primary-opus5-76c-20260829.md":
        "f7853d39a17fd7329feaec101f1767ef5edddd07a2f0d5f8030a0cb023f95efe",
    "xmodel/m2-two-pole-full-actual-first-separation-cross-comparison-sol56-opus5-76c-20260829.md":
        "32402983a357ef25de363a9532a47fa9a2cb4b4e8e1bab918d6f6e07a3fb3a10",
    "xmodel/m2-two-pole-full-actual-first-separation-hostile-review-grok46-76c-20260829b.md":
        "1b3be27da8ba495d80cbf473d844055583a672d136ccea40611dfe9fc0b7023e",
    "xmodel/m2-exit-safe-floor-legacy-reprice-r1-sol56-20260829.md":
        "aaa7496bd6182bd124935b8534307ad3167fffe9393efad3e56cf349942ddeb7",
    "xmodel/m2-exit-safe-floor-legacy-reprice-r1-stable-hostile-rereview-opus5-20260829b.md":
        "3e3cea4aa6e0bda907dd291a0f1e62e1ffa744e84463e5596c2e0e0e408a166b",
    "cases/landing_ledger_ll1_r3_20260829/out/ll1_book.json":
        "205e7f5825604e0e334d1a822b13a595dfe6b9ce06d0f011b199a0ddcb725a1e",
    "cases/m2_exit_safe_floor_legacy_reprice_r1_20260829/check.py":
        "6ca098b8145f091884d7f11ab1d6aac49dadaab91a6ba7ed18f7c022efce99b5",
}

EVIDENCE_BODY_PINS = {
    "xmodel/m2-two-pole-full-actual-first-separation-theorem-r1-sol56-20260829.md":
        (21235, "0c808734cf2f0c98d085503e8d0aaf8e0ca645c34adfb925c757d0beb6223428"),
    "xmodel/m2-two-pole-full-exit-attachment-primary-opus5-76c-20260829.md":
        (61389, "2fe6a14ca8a04033d176547704de20ccd7d1c7e5dd19599970dffab3a60cbe18"),
    "xmodel/m2-two-pole-full-actual-first-separation-cross-comparison-sol56-opus5-76c-20260829.md":
        (9484, "1026e3a240b93563a3f521acd07ab139f329a6658568f8dc2c83a4634c58ec22"),
    "xmodel/m2-two-pole-full-actual-first-separation-hostile-review-grok46-76c-20260829b.md":
        (32456, "3be6ab6b8db8ba7c89c0f382f201a17b2bae6000720d2c04ef2de3925b90a47a"),
    "xmodel/m2-exit-safe-floor-legacy-reprice-r1-sol56-20260829.md":
        (12149, "2d873e680cfdc464fc0bc707aec5c072ba9310ee0600a98786643c0ca8c93ac5"),
    "xmodel/m2-exit-safe-floor-legacy-reprice-r1-stable-hostile-rereview-opus5-20260829b.md":
        (34525, "7b23f8cadfc8e4afcbebd64add68449bd8e08f2cacfc6dede26d651dc681e302"),
}

EXPECTED_CHANGED_CELLS = (
    (17, 5, 2),
    (51, 15, 7),
    (85, 25, 12),
    (119, 35, 17),
)
EXPECTED_REMOVED_ALIVE = (
    ("2/7", 7, 3, "ALIVE"),
    ("1/2", 2, 4, "ALIVE_FRAGILE"),
    ("1/2", 4, 4, "ALIVE_FRAGILE"),
    ("2/11", 11, 4, "ALIVE_FRAGILE"),
    ("2/13", 13, 4, "ALIVE_FRAGILE"),
    ("2/5", 5, 4, "ALIVE_FRAGILE"),
)
EXPECTED_FULL_ALIVE = (
    ("2/3", 3, 2, "ALIVE"),
    ("3/4", 4, 2, "ALIVE_FRAGILE"),
    ("2/5", 5, 3, "ALIVE"),
    ("2/7", 7, 4, "ALIVE_FRAGILE"),
    ("2/9", 9, 4, "ALIVE_FRAGILE"),
    ("3/10", 10, 4, "ALIVE_FRAGILE"),
    ("3/8", 8, 4, "ALIVE_FRAGILE"),
)

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
    "FULL-ACTUAL-FIRST-SEPARATION": {
        "tier": "promoted",
        "source": ("BOOK-OFFAXIS 2026-08-29 full-exit correction + stable "
                   "Grok review 1b3be27d (one fixed fibre, two-pole path "
                   "union; complete distinct carrier; floor only)"),
    },
    "T7": {"tier": "promoted", "source": "REDUCTION.md T7 (entry menu; Lambda = a b alpha beta / nu; nu-menu; SOL-PROP58/Chau every-fibre)"},
    "OFFAXIS-EMPTY-TD6": {"tier": "promoted", "source": "BOOK-OFFAXIS.md sec.4 (td=6: off-axis sector EMPTY, 0 raw entries) + MP4 (Lambda=3 prime forces b=1)"},
    "MP6(b)": {"tier": "promoted", "source": "SHEET6-MULTIPOLE.md MP6(b) (equal-quotient law deg p_H = i*mu_e)"},
    "St 3.18": {"tier": "printed", "source": "Sigray St 3.18 p.18 (one continuation per orbit; q-extras carry no tree vertex)"},
    "ENGINE-REC": {"tier": "promoted", "source": "SHEET6-DEPTH.md sec.6/check 6 + SHEET6-DEPTH-REVIEW.md l1only re-run record (26 phase-4 shapes at w=2 / 351 parent pairs on the single residue child (1/2,3,2,5)); FIXTURE-CITED: parsed from the pinned bytes, engine NOT re-run by this packet"},
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
# R-6: source provenance -- exact byte pins + consumed-clause anchors
# (fail closed on any drift; R2's two stale pins are superseded, recorded
# below for the provenance trail only and never verified)
# ==========================================================================

SOURCE_PINS = {
    # Canonical carrier integration frozen for the R4 build:
    "ladder/SHEET6-MULTIPOLE.md":
        "f11cbe1fcad375fdd722be979731f7c30f989889bfeb33232ab86e64deee1774",
    "ladder/SHEET6-2POLE.md":
        "c66ff941d3954143b51f4dc2ac0dd77d6e1d5be81c0d6cdca3e1bd2a058b9a64",
    "ladder/BOOK-OFFAXIS.md":
        "b3993495eff1913b09f1fc6750b2af08ecf90a9f9f38c97f85be47ba9c9a54d0",
    "FALLACY.md":
        "c63bd1673b2b180173799f5bee07f7fc0e51047945a41010a28a0aeeeeb92253",
    # R3 structural sources, re-pinned at the integration checkpoint:
    "ladder/REDUCTION.md":
        "29270ff6192fcee2eecb4ba68578010b2b3f0c5519feb71dc67baa7f68bb784b",
    "ladder/SHEET6-DEPTH.md":
        "ad9ced6c0420902f8cf63edf3636bed8633be511e925f208d24a24c35d71036d",
    "ladder/SHEET6-DEPTH-REVIEW.md":
        "841fa120fa2ae801578834c7b52c5aad600eb48df73b683e1db5c954caf7f7ac",
}

R2_SUPERSEDED_PINS = {
    # What the R2 report printed.  Neither value matches HEAD
    # (26f0c64e... / f0fca498...) nor the current bytes: R2 hashed
    # intermediate uncommitted working-tree states that no longer exist.
    # Recorded for the audit trail; NOT consumed by any check.
    "ladder/BOOK-OFFAXIS.md":
        "34f5ea9db62caf1da8b436733752e86402ff3f3ee08bc5096f13f8bf0c80eb17",
    "ladder/REDUCTION.md":
        "6b9376e0f479545f012cd7451bd3eb1a9271fc312b9996c5848c5db159ebdb31",
}

# Consumed-clause anchors: exact substrings of the pinned bytes.  Presence
# is verified at compile AND validate time (a canonical edit that touches a
# consumed sentence fails the packet closed even before the hash is
# re-pinned).  The mathematical re-derivation of each clause is the R2/R3
# machinery itself (entry_menu, dirty_cells, terminal, residue_enumeration,
# classify_family_I), which re-runs on every compile.
CONSUMED_ANCHORS = (
    # --- ladder/REDUCTION.md : T7 entry layer ---
    ("T7/mass-formula", "ladder/REDUCTION.md",
     r"\Lambda(F)&=\frac{a_Fb_F\alpha\beta}{\nu_F}"),
    ("T7/M=b-pin", "ladder/REDUCTION.md", r"M_F&=b_F,"),
    ("T7/nu-menu-alpha", "ladder/REDUCTION.md",
     r"\nu_F\mid\alpha,\quad \nu_F\mid b_F\beta-1"),
    ("T7/nu-menu-beta", "ladder/REDUCTION.md",
     r"\nu_F\mid\beta,\quad \nu_F\mid b_F\alpha-1"),
    ("T7/beta-floor", "ladder/REDUCTION.md", r"\Lambda(F)\ge\beta\ge3"),
    ("T7/finite-menu", "ladder/REDUCTION.md",
     "only finitely many entry data \\(E\\) occur"),
    ("T7/prop58-chau", "ladder/REDUCTION.md",
     "whose external input is Chau's published"),
    ("CRIT5/s>=3-false", "ladder/REDUCTION.md",
     r"merge requires \(s\ge3\) is **false**"),
    ("HIGH1/single-pole-open", "ladder/REDUCTION.md",
     "### HIGH 1 — composite single-pole configurations remain open"),
    # --- ladder/BOOK-OFFAXIS.md : sec.4 / P0 / P1 / R-laws ---
    ("OFFAXIS-EMPTY-TD6/sec4", "ladder/BOOK-OFFAXIS.md",
     "**td 6, 9 (all m); m=4 td 12**: off-axis sector EMPTY (0 raw entries)."),
    ("P0/transport-kbar", "ladder/BOOK-OFFAXIS.md",
     "κ̄_F = l·w_G·dq/E ∈ ℤ (ν ≥ 2)"),
    ("P0/transport-w", "ladder/BOOK-OFFAXIS.md", "w_F = l·w_G(dq−1)/(νE)"),
    ("P0/M-derived", "ladder/BOOK-OFFAXIS.md", "M_F = gcd(dp, dq)."),
    ("P0/AF2-price", "ladder/BOOK-OFFAXIS.md",
     "λ_F ≥ Σ_j max(1, ⌈X_F/m_j − κ̄_F⌉) + [ε ≥ 1]·max(1, ⌈(X_F/ε − κ̄_F)/ν⌉)"),
    ("P0/finiteness-bound", "ladder/BOOK-OFFAXIS.md", "E | l·num(w_G)·T"),
    ("P0/T-definition", "ladder/BOOK-OFFAXIS.md",
     "T := Sm + l − ε(1+k+lex) ≥ 1"),
    ("P0/pure-b-collapse", "ladder/BOOK-OFFAXIS.md",
     "w_F = l·w_G/(l−ε) (expansion), M_F = gcd(l−ε, ν+1) | l−ε"),
    ("P0/menu-(A)", "ladder/BOOK-OFFAXIS.md",
     "(A) (21,15): w → 2/3, M → 3, λ ≥ 2"),
    ("P0/menu-(C)", "ladder/BOOK-OFFAXIS.md",
     "(C) (20,16): w → 3/4, M → 4, λ ≥ 2"),
    ("P0/menu-four-escapes", "ladder/BOOK-OFFAXIS.md",
     "the review's four escapes, now all priced"),
    ("R4/full-actual-alias", "ladder/BOOK-OFFAXIS.md",
     "`FULL_ACTUAL_EXIT=FULL_ACTUAL_FIRST_SEPARATION`: complete distinct actual cv"),
    ("R4/four-cell-totals", "ladder/BOOK-OFFAXIS.md",
     "`3,3,3,2` and the reduced-superset inventory `13 -> 7`"),
    ("P1/psi-certificate", "ladder/BOOK-OFFAXIS.md", "ψ = ⌈1/(1−w_G)⌉ − 1"),
    ("P1/shared-budget", "ladder/BOOK-OFFAXIS.md", "Σ λ ≤ td − 1 − ψ"),
    ("P1/j-law", "ladder/BOOK-OFFAXIS.md", "j := M_G·(1 − w_G) ∈ ℕ*"),
    ("R1.0/eta-slot", "ladder/BOOK-OFFAXIS.md",
     "dq ≡ 1 (mod ν) and gcd(M_F, ν_F) = 1 always"),
    ("R2.1/handshake-I-II", "ladder/BOOK-OFFAXIS.md",
     "X_G = μ_e·(κ̄_G − w_e)"),
    ("R2.1/handshake-III", "ladder/BOOK-OFFAXIS.md",
     "X_G = μ₀·(κ̄_G − ν_e·w_e)"),
    ("MRW/root-window", "ladder/BOOK-OFFAXIS.md",
     "X_R = μ_e(1−w_e) = A/B,"),
    ("MRW/root-window-open", "ladder/BOOK-OFFAXIS.md",
     "w_e = 1 − A/(μ_e B) in (0,1)."),
    ("MRW/header-2026-08-28", "ladder/BOOK-OFFAXIS.md",
     "`X_R=mu_e(1-w_e)=A/B` and hence `0<w_e<1`, with no `mu_e=1`"),
    ("R2.2/searrow", "ladder/BOOK-OFFAXIS.md",
     "μ_e·dq > dp for every arriving edge"),
    ("R2.2/root-mult", "ladder/BOOK-OFFAXIS.md",
     "dp ≠ μ★·dq for every mult μ★ of p"),
    ("R2.2/M-gcd", "ladder/BOOK-OFFAXIS.md",
     "M_G = gcd(dp, dq); subadditivity"),
    ("R2.2/dq-mod-nu", "ladder/BOOK-OFFAXIS.md",
     "dq = (r₀ + k + l)ν + 1"),
    ("SEC3/mixed-menu-open", "ladder/BOOK-OFFAXIS.md",
     "mixed rows impose `M_G | sum(mu_e)`, which is justified only on the"),
    ("SEC11/quarantined-band", "ladder/BOOK-OFFAXIS.md",
     "(mu+nu) | (mu(l+1)-1)"),
    ("SEC11/kbar-band", "ladder/BOOK-OFFAXIS.md", "kbar in {3,4}"),
    ("SEC11A/17-vs-2", "ladder/BOOK-OFFAXIS.md",
     "promoted H5a: 17 cells; forced-ν: 2 cells"),
    ("SEC1A/td7-witness", "ladder/BOOK-OFFAXIS.md",
     "Λ = (3,4), poles (a,b,ν) = (1,1,2) ⊕ (1,2,3), M = (1,2),"),
    # --- ladder/SHEET6-MULTIPOLE.md : the cap flag the packet refuses to
    #     inherit as a decision (cap firewall; unchanged pin) ---
    ("MP9-CAP-FLAG/present-not-inherited", "ladder/SHEET6-MULTIPOLE.md",
     "is excluded only for l ≤ 4"),
    ("R4/generic-MP8-representative", "ladder/SHEET6-MULTIPOLE.md",
     "Generic MP8/MFE remains `REPRESENTATIVE`"),
    ("R4/multipole-two-pole-scope", "ladder/SHEET6-MULTIPOLE.md",
     "`FULL_ACTUAL_FIRST_SEPARATION=FULL_ACTUAL_EXIT`, meaning a lower floor only"),
    ("R4/two-pole-carrier", "ladder/SHEET6-2POLE.md",
     "`FULL_ACTUAL_FIRST_SEPARATION=FULL_ACTUAL_EXIT` means complete carrier plus"),
    ("R4/fallacy-no-attainment", "FALLACY.md",
     "latter aliases `FULL_ACTUAL_FIRST_SEPARATION` and supplies only a floor"),
    # --- fixture files : charged engine-record sentences (count-free) ---
    ("ENG/depth-frame-family", "ladder/SHEET6-DEPTH.md",
     "reachable frames are exactly"),
    ("ENG/depth-check6", "ladder/SHEET6-DEPTH.md",
     "promoted twopole_check phase-4 shapes"),
    ("ENG/depth-review-l1only", "ladder/SHEET6-DEPTH-REVIEW.md",
     "l1only (byte-match:"),
    ("ENG/depth-review-predict", "ladder/SHEET6-DEPTH-REVIEW.md",
     "the w-formula PREDICTS the child:"),
)


def _repo_read(relpath):
    """Read a pinned source file relative to the repository root (the
    packet sits at cases/<packet>/, so the root is two levels up).  No
    absolute path ever enters the emitted book."""
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.normpath(os.path.join(here, "..", ".."))
    with open(os.path.join(root, *relpath.split("/")), "rb") as f:
        return f.read()


def load_sources(readers=None):
    """Return {relpath: bytes} for every pinned source.  `readers` (used
    only by the mutation battery) substitutes byte content; the real book
    is always compiled from disk."""
    out = {}
    for path in SOURCE_PINS:
        out[path] = readers[path] if readers is not None else _repo_read(path)
    return out


def verify_source_pins(sources):
    """SHA-256 every pinned source and fail closed on any drift.  Returns
    {relpath: hexdigest} (all verified equal to SOURCE_PINS)."""
    got = {}
    for path, want in sorted(SOURCE_PINS.items()):
        h = hashlib.sha256(sources[path]).hexdigest()
        if h != want:
            raise LLError("SOURCE DRIFT (fail closed): %s hashes %s, "
                          "pinned %s" % (path, h, want))
        got[path] = h
    return got


def verify_clause_anchors(texts):
    """Every consumed-clause anchor must be present verbatim in the pinned
    text of its file; fail closed otherwise.  Returns the clause table for
    the book."""
    rows = []
    for clause, path, anchor in CONSUMED_ANCHORS:
        if anchor not in texts[path]:
            raise LLError("CONSUMED CLAUSE MISSING (fail closed): %s "
                          "anchor %r not found in %s" % (clause, anchor, path))
        rows.append({"clause": clause, "file": path, "anchor": anchor,
                     "status": "PRESENT"})
    return rows


# Count-free parse of the charged engine-record figures.  NO expected count
# appears in any pattern: every number in the emitted engine_record is a
# regex group captured from the pinned bytes (parity is never manufactured).
_RX_DEPTH_FAMILY = re.compile(
    r"reachable frames are exactly \{\((\d+), ν, (\d+)ν\+(\d+)\) : ν ≥ (\d+)\}")
_RX_DEPTH_MU1 = re.compile(r"phase-4 record's (\d+) μ1-shapes")
_RX_DEPTH_PAIRINV = re.compile(r"(\d+)/(\d+) pair depth-invariance")
_RX_DEPTH_CHECK6 = re.compile(
    r"all (\d+) promoted twopole_check phase-4 shapes\s+have w = (\d+) "
    r"at every instance")
_RX_DR_HEADER = re.compile(
    r"l1only \(byte-match: (\d+) pre-merge shapes, "
    r"(\d+)/(\d+)/(\d+)/(\d+) merge ledger,\s+"
    r"RESIDUE child \((\d+)/(\d+), (\d+), (\d+), (\d+)\) at "
    r"\*\*(\d+) parent pairs\*\*")
_RX_DR_RERUN = re.compile(
    r"(\d+)/(\d+): twopole_check\.py l1only re-run \S+ (\d+) shapes, "
    r"RESIDUE child\s+\((\d+)/(\d+), (\d+), (\d+), (\d+)\) at (\d+) parent "
    r"pairs, ZCH suffix-DEAD ×(\d+), ν=1 ODE-dead\s+(\d+)")
_RX_DR_PREDICT = re.compile(
    r"the w-formula PREDICTS the child: (\d+)·\((\d+), (\d+), (\d+)\)/(\d+) "
    r"=\s+\(κ[^,]*, D/i, ρ\) = \((\d+), (\d+), (\d+)/(\d+)\)")


def _search(rx, text, what, path):
    m = rx.search(text)
    if not m:
        raise LLError("ENGINE FIXTURE PARSE FAILED (fail closed): %s not "
                      "found in %s" % (what, path))
    return tuple(int(g) for g in m.groups())


def parse_engine_fixture(texts):
    """Parse the charged 26-shape / 351-route engine record from the pinned
    fixture bytes and enforce internal cross-consistency.  Fail closed on
    any miss or disagreement."""
    depth = texts["ladder/SHEET6-DEPTH.md"]
    dr = texts["ladder/SHEET6-DEPTH-REVIEW.md"]
    fam = _search(_RX_DEPTH_FAMILY, depth, "frame family", "SHEET6-DEPTH.md")
    mu1 = _search(_RX_DEPTH_MU1, depth, "mu1-shape count", "SHEET6-DEPTH.md")
    inv = _search(_RX_DEPTH_PAIRINV, depth, "pair depth-invariance",
                  "SHEET6-DEPTH.md")
    c6 = _search(_RX_DEPTH_CHECK6, depth, "check-6 sentence",
                 "SHEET6-DEPTH.md")
    hdr = _search(_RX_DR_HEADER, dr, "l1only byte-match record",
                  "SHEET6-DEPTH-REVIEW.md")
    rr = _search(_RX_DR_RERUN, dr, "l1only re-run record",
                 "SHEET6-DEPTH-REVIEW.md")
    pred = _search(_RX_DR_PREDICT, dr, "w-formula prediction identity",
                   "SHEET6-DEPTH-REVIEW.md")
    # cross-consistency between the two independent fixture records
    shapes, ledger, child_h, pairs_h = hdr[0], hdr[1:5], hdr[5:10], hdr[10]
    inv2, shapes_r, child_r, pairs_r, zch_r, ode_r = (
        rr[0:2], rr[2], rr[3:8], rr[8], rr[9], rr[10])
    checks = (
        (shapes == shapes_r == c6[0], "shape count agreement"),
        (pairs_h == pairs_r == inv[0] == inv[1] == inv2[0] == inv2[1],
         "parent-pair / depth-invariance agreement"),
        (child_h == child_r, "residue-child tuple agreement"),
        (ledger[2] == ode_r and ledger[3] == zch_r,
         "merge-ledger vs named-count agreement"),
        (mu1[0] <= shapes, "mu1-shapes bounded by total shapes"),
        (fam[0] == c6[1], "family w equals check-6 w"),
        # the recorded DS4 prediction identity must be arithmetically true
        # exactly as printed: w*(dq, dp, 1)/Delta = (kbar, D/i, rho)
        (Fraction(pred[0] * pred[1], pred[4]) == pred[5]
         and Fraction(pred[0] * pred[2], pred[4]) == pred[6]
         and Fraction(pred[0] * pred[3], pred[4])
         == Fraction(pred[7], pred[8]),
         "printed prediction identity arithmetic"),
    )
    for ok, what in checks:
        if not ok:
            raise LLError("ENGINE FIXTURE INCONSISTENT (fail closed): %s"
                          % what)
    return {
        "shapes": shapes,
        "mu1_shapes": mu1[0],
        "nu1_zch_shapes": shapes - mu1[0],
        "parent_pairs": pairs_h,
        "pair_invariance": [inv[0], inv[1]],
        "merge_ledger": list(ledger),
        "zch_suffix_dead": zch_r,
        "nu1_ode_dead": ode_r,
        "residue_child": {"rho": "%d/%d" % (child_h[0], child_h[1]),
                          "nu": child_h[2], "M": child_h[3],
                          "kbar": child_h[4]},
        "prediction_identity": {
            "w": pred[0], "dq": pred[1], "dp": pred[2], "one": pred[3],
            "Delta": pred[4],
            "kbar": pred[5], "Di": pred[6],
            "rho": "%d/%d" % (pred[7], pred[8])},
        "frame_family": {"w": fam[0], "kbar_nu_coeff": fam[1],
                         "kbar_const": fam[2], "nu_min": fam[3]},
        "cited_from": ["ladder/SHEET6-DEPTH.md",
                       "ladder/SHEET6-DEPTH-REVIEW.md"],
        "scope": ("FIXTURE-CITED engine history (cases/twopole_check.py "
                  "l1only / phase 4, as recorded in the pinned bytes). "
                  "The engine is NOT re-run by this packet and the counts "
                  "26/24/351/276/601 and 18427/17199 are NOT re-derived "
                  "here; the packet proves parity between its own derived "
                  "data (entry w0, W(2), IIa child Q=(6,12,3,2,5), DS4 "
                  "identity) and the parsed frozen record, nothing more."),
    }


def engine_parity_checks(record):
    """Honest parity between the parsed frozen engine record and the
    packet's own derived data.  Every comparison is derived-vs-parsed
    (never constant-vs-itself).  Fail closed on any mismatch; returns the
    check table for the book."""
    admitted, _, _ = iia_admitted(Fraction(2))
    cell = admitted[0]["cell"]
    child = admitted[0]["child"]
    entries, offaxis = entry_menu(TD, M_POLES)
    if len(entries) != 1 or offaxis:
        raise LLError("entry menu drift inside parity gate")
    fr = entry_frame(entries[0])[0]
    W = w_closure(fr["w0"])
    rc = record["residue_child"]
    pi = record["prediction_identity"]
    ff = record["frame_family"]
    rows = []

    def par(ok, what):
        if not ok:
            raise LLError("ENGINE PARITY FAILED (fail closed): %s" % what)
        rows.append({"check": what, "status": "OK"})

    # 1. the frozen residue child equals the derived admitted IIa child
    par(rc["nu"] == cell["nu"] and Fraction(rc["rho"]) ==
        Fraction(child["Q"][0], child["Q"][1])
        and rc["M"] == cell["M"] == math.gcd(cell["dp"], cell["dq"])
        and rc["kbar"] == cell["kbar"],
        "parsed residue child (rho,nu,M,kbar)=(%s,%d,%d,%d) equals the "
        "derived IIa child Q=(6,12,3,2,5) in shape space"
        % (rc["rho"], rc["nu"], rc["M"], rc["kbar"]))
    # 2. the recorded DS4 prediction identity inputs are the derived cell
    par(pi["dq"] == cell["dq"] and pi["dp"] == cell["dp"]
        and pi["Delta"] == cell["dq"] - cell["dp"] and pi["one"] == 1
        and Fraction(pi["w"]) in W,
        "parsed prediction inputs w*(dq,dp,1)/Delta match the derived "
        "cell (dp,dq)=(6,10), Delta=4, w in W(2)")
    # 3. re-run the DS4 identity on the parsed inputs; outputs must equal
    #    both the parsed outputs and the derived child data
    kbar = Fraction(pi["w"] * pi["dq"], pi["Delta"])
    Di = Fraction(pi["w"] * pi["dp"], pi["Delta"])
    rho = Fraction(pi["w"], pi["Delta"])
    par(kbar == pi["kbar"] == cell["kbar"]
        and Di == pi["Di"] == cell["X"]
        and rho == Fraction(pi["rho"]) == cell["X"] / cell["dp"],
        "DS4 identity recomputed on parsed inputs: (kbar,D/i,rho)="
        "(5,3,1/2) equals parsed outputs and derived (kbar,X,X/dp)")
    # 4. the frozen frame family is the fixed-w family at the derived w0:
    #    (w, nu, a*nu+b) with a == w == w0 and constant rho = b
    par(ff["w"] == fr["w0"] == W[0] and len(W) == 1
        and ff["kbar_nu_coeff"] == ff["w"] and ff["nu_min"] == 2,
        "parsed frame family w equals derived entry w0=2 with W(2)={2}, "
        "and the parsed kbar formula has nu-coefficient w (fixed-w family)")
    par(all(Fraction(ff["kbar_nu_coeff"] * nu + ff["kbar_const"]
            - ff["kbar_const"], nu) == ff["w"] for nu in range(2, 27))
        and (fr["kbar"] - fr["rho"]) / entries[0]["poles"][0][2] == ff["w"],
        "w-map consistency: parsed family gives (kbar-rho)/nu == w for "
        "nu=2..26 at chain rho=%d, and the derived entry frame (rho,nu,"
        "kbar)=(1,2,5) gives w=2 under the same map" % ff["kbar_const"])
    # 5. the counts stay fixture-cited (scope honesty)
    par("NOT re-run" in record["scope"]
        and set(record["cited_from"]) ==
        {"ladder/SHEET6-DEPTH.md", "ladder/SHEET6-DEPTH-REVIEW.md"},
        "counts remain fixture-cited with explicit not-re-run scope")
    return rows


def load_evidence(readers=None):
    """Load immutable theorem/review/software evidence from declared paths."""
    return {
        path: (readers[path] if readers is not None else _repo_read(path))
        for path in EVIDENCE_PINS
    }


def verify_evidence_pins(evidence):
    """Verify full-file hashes and every declared sealed-body prefix."""
    full = {}
    bodies = {}
    for path, want in sorted(EVIDENCE_PINS.items()):
        got = hashlib.sha256(evidence[path]).hexdigest()
        if got != want:
            raise LLError("EVIDENCE DRIFT (fail closed): %s hashes %s, "
                          "pinned %s" % (path, got, want))
        full[path] = got
    for path, (nbytes, want) in sorted(EVIDENCE_BODY_PINS.items()):
        blob = evidence[path]
        if len(blob) < nbytes:
            raise LLError("EVIDENCE BODY TRUNCATED (fail closed): %s has "
                          "%d bytes, needs %d" % (path, len(blob), nbytes))
        got = hashlib.sha256(blob[:nbytes]).hexdigest()
        if got != want:
            raise LLError("EVIDENCE BODY DRIFT (fail closed): %s prefix %d "
                          "hashes %s, pinned %s" %
                          (path, nbytes, got, want))
        bodies[path] = {"bytes": nbytes, "sha256": got}
    return full, bodies


def build_provenance(readers=None, evidence_readers=None):
    """The full R-6--R-10 provenance object for the book.  Fail-closed at
    every layer: canonical pins, evidence/body pins, clause anchors, fixture
    parse, and parity."""
    sources = load_sources(readers)
    pins = verify_source_pins(sources)
    evidence_pins, evidence_bodies = verify_evidence_pins(
        load_evidence(evidence_readers))
    texts = {p: b.decode("utf-8") for p, b in sources.items()}
    clauses = verify_clause_anchors(texts)
    record = parse_engine_fixture(texts)
    parity = engine_parity_checks(record)
    return {
        "source_pins": pins,
        "evidence_pins": evidence_pins,
        "evidence_body_pins": evidence_bodies,
        "carrier_theorem": {
            "claim": "PROVED_FULL_TWO_POLE_ATTACHMENT",
            "carrier": FULL_ACTUAL_FIRST_SEPARATION,
            "canonical_alias": FULL_ACTUAL_EXIT,
            "semantics": LOWER_FLOOR_ONLY,
            "attainment": False,
            "scope": "one-fixed-fibre/two-pole-path-union",
            "review_verdict": "PASS_WITH_REPAIR",
            "repair": ("FULL_ACTUAL_EXIT is the floor-valued alias of "
                       "FULL_ACTUAL_FIRST_SEPARATION; it does not add "
                       "attainment"),
        },
        "r2_superseded_pins": dict(sorted(R2_SUPERSEDED_PINS.items())),
        "consumed_clauses": clauses,
        "engine_record": record,
        "engine_parity": parity,
        "rederivation": {
            "clauses": "P0, P1, BOOK-OFFAXIS sec.4, REDUCTION T7 (plus "
                       "R1.0/R2.1/R2.2/MRW/sec.3/sec.11/sec.11a/sec.1a and "
                       "CRIT5/HIGH1 scope cites) re-derived against the "
                       "pinned current bytes by this compiler's own "
                       "machinery (entry_menu, dirty_cells, terminal, "
                       "residue_enumeration, classify_family_I)",
            "decision_changes": [],
        },
    }


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

def representative_nonzero_floor(delta):
    """Legacy AF2 floor for one selected nonzero ray/witness."""
    delta = Fraction(delta)
    return max(1, ceil_frac(delta))


def full_actual_nonzero_floor(delta):
    """Reviewed full-actual total floor for one nonzero direction.

    This function is intentionally unavailable for non-positive defects and
    carries no attainment semantics.
    """
    delta = Fraction(delta)
    if delta <= 0:
        raise LLError("FULL_ACTUAL_FIRST_SEPARATION requires delta > 0")
    if delta.denominator == 1:
        return int(delta)
    return ceil_frac(2 * delta)


def representative_epsilon_zero_floor(X, kbar, nu, eps):
    """Legacy epsilon/zero-direction AF2 floor; never passed to L_safe."""
    if eps < 1:
        return 0
    return max(1, ceil_frac((Fraction(X) / eps - kbar) / nu))


def typed_exit_price(X, kbar, nu, eps, mults, nonzero_carrier):
    """Return explicit component pricing under one declared carrier type."""
    if nonzero_carrier not in (REPRESENTATIVE,
                               FULL_ACTUAL_FIRST_SEPARATION):
        raise LLError("unknown nonzero carrier %r" % nonzero_carrier)
    nonzero = []
    rep_total = 0
    full_total = 0
    applied_total = 0
    for m in mults:
        delta = Fraction(X) / m - kbar
        if delta <= 0:
            raise LLError("nonzero up direction has non-positive defect")
        rep = representative_nonzero_floor(delta)
        full = full_actual_nonzero_floor(delta)
        applied = rep if nonzero_carrier == REPRESENTATIVE else full
        nonzero.append({
            "direction": "NONZERO_UP",
            "multiplicity": m,
            "delta": str(delta),
            "carrier": nonzero_carrier,
            "certificate": ("AF2" if nonzero_carrier == REPRESENTATIVE
                            else "FULL-ACTUAL-FIRST-SEPARATION"),
            "representative_floor": rep,
            "full_actual_floor": full,
            "applied_floor": applied,
            "semantics": LOWER_FLOOR_ONLY,
            "attainment": False,
        })
        rep_total += rep
        full_total += full
        applied_total += applied
    eps_floor = representative_epsilon_zero_floor(X, kbar, nu, eps)
    epsilon_zero = None
    if eps >= 1:
        epsilon_zero = {
            "direction": "EPSILON_ZERO",
            "multiplicity": eps,
            "carrier": REPRESENTATIVE,
            "applied_floor": eps_floor,
            "rule": "legacy-AF2-epsilon-zero",
            "semantics": LOWER_FLOOR_ONLY,
            "attainment": False,
        }
    return {
        "nonzero_carrier": nonzero_carrier,
        "canonical_full_alias": FULL_ACTUAL_EXIT,
        "semantics": LOWER_FLOOR_ONLY,
        "attainment": False,
        "nonzero": nonzero,
        "epsilon_zero": epsilon_zero,
        "representative_total": rep_total + eps_floor,
        "full_actual_total": full_total + eps_floor,
        "applied_total": applied_total + eps_floor,
    }


def representative_af2_price(X, kbar, nu, eps, mults):
    """The legacy AF2 total, kept separate and explicitly representative."""
    return typed_exit_price(X, kbar, nu, eps, mults,
                            REPRESENTATIVE)["applied_total"]


def dirty_cells(w, l, lam_cap, *, nonzero_carrier):
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
                           "pricing": {
                               "direction": "EPSILON_ZERO",
                               "carrier": REPRESENTATIVE,
                               "rule": "legacy-P0-pure-epsilon",
                               "applied_floor": lam_min,
                               "semantics": LOWER_FLOOR_ONLY,
                               "attainment": False,
                           },
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
                        pricing = typed_exit_price(
                            X, kbar, nu, eps, mults, nonzero_carrier)
                        lam = pricing["applied_total"]
                        if lam > lam_cap:
                            continue
                        wF = l * w * (dq - 1) / (nu * E)
                        M = math.gcd(dp, dq)  # repair R-3: gcd of CHILD shape
                        cells.append({
                            "l": l, "eps": eps, "k": k, "mults": list(mults),
                            "lex": lex, "nu": nu, "dp": dp, "dq": dq,
                            "E": E, "kbar": kbar, "X": X, "lam": lam,
                            "lam_representative":
                                pricing["representative_total"],
                            "pricing": pricing,
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

def residue_enumeration(td=TD, *, nonzero_carrier):
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
            cells, pure_b = dirty_cells(
                w, l, lam_max - lam,
                nonzero_carrier=nonzero_carrier)
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
                           "w_child": str(pb["w_child"]),
                           "pricing": pb["pricing"]}
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


def _alive_inventory(terminals):
    return tuple(sorted(
        (t["state"][0], int(t["state"][1]), int(t["state"][2]),
         t["verdict"])
        for t in terminals
        if t.get("verdict") in ("ALIVE", "ALIVE_FRAGILE")
    ))


def _legacy_r3_alive_inventory():
    blob = _repo_read(
        "cases/landing_ledger_ll1_r3_20260829/out/ll1_book.json")
    want = EVIDENCE_PINS[
        "cases/landing_ledger_ll1_r3_20260829/out/ll1_book.json"]
    got = hashlib.sha256(blob).hexdigest()
    if got != want:
        raise LLError("legacy R3 book drift: %s != %s" % (got, want))
    book = json.loads(blob.decode("utf-8"))
    return _alive_inventory(book["sections"]["residue_terminals"])


def repricing_audit():
    """Exact old/new replay and exhaustive changed-cell certificate."""
    old_terms, old_steps, _ = residue_enumeration(
        TD, nonzero_carrier=REPRESENTATIVE)
    new_terms, _, _ = residue_enumeration(
        TD, nonzero_carrier=FULL_ACTUAL_FIRST_SEPARATION)
    old_alive = _alive_inventory(old_terms)
    new_alive = _alive_inventory(new_terms)
    if old_alive != _legacy_r3_alive_inventory():
        raise LLError("representative replay differs from frozen LL1-R3")

    unique = {}
    for row in old_steps:
        cell = row.get("cell")
        if cell is None:
            continue
        key = (
            int(cell["dp"]), int(cell["dq"]), int(cell["nu"]),
            int(cell["l"]), int(cell["eps"]), int(cell["k"]),
            tuple(cell["mults"]), str(cell["kbar"]), str(cell["X"]),
        )
        signature = int(cell["lam"])
        if key in unique and unique[key] != signature:
            raise LLError("cell key collision at %r" % (key,))
        unique[key] = signature
    if len(unique) != 16:
        raise LLError("legacy unique-cell count drift: %d != 16" %
                      len(unique))

    rows = []
    for key, old_total in sorted(unique.items()):
        dp, dq, nu, l, eps, _k, mults, kbar, X = key
        pricing = typed_exit_price(
            Fraction(X), Fraction(kbar), nu, eps, mults,
            FULL_ACTUAL_FIRST_SEPARATION)
        new_total = pricing["applied_total"]
        if pricing["representative_total"] != old_total:
            raise LLError("representative total drift at %r" % (key,))
        if new_total != old_total:
            rows.append({
                "cell": [dp, dq, nu],
                "l": l,
                "eps": eps,
                "mults": list(mults),
                "X": X,
                "kbar": kbar,
                "delta": pricing["nonzero"][0]["delta"],
                "representative_total": old_total,
                "full_actual_total": new_total,
                "zero_epsilon_floor": (
                    pricing["epsilon_zero"]["applied_floor"]
                    if pricing["epsilon_zero"] is not None else 0),
                "carrier": FULL_ACTUAL_FIRST_SEPARATION,
                "semantics": LOWER_FLOOR_ONLY,
                "attainment": False,
            })

    changed = tuple(tuple(r["cell"]) for r in rows)
    if changed != EXPECTED_CHANGED_CELLS:
        raise LLError("changed-cell set drift: %r" % (changed,))
    if tuple(r["full_actual_total"] for r in rows) != (3, 3, 3, 2):
        raise LLError("changed-cell full totals drift")
    if tuple(r["zero_epsilon_floor"] for r in rows) != (1, 1, 1, 0):
        raise LLError("zero/epsilon floors drift")
    if old_alive.__len__() != 13 or new_alive.__len__() != 7:
        raise LLError("alive inventory count drift: %d -> %d" %
                      (len(old_alive), len(new_alive)))
    removed = tuple(sorted(set(old_alive) - set(new_alive)))
    added = tuple(sorted(set(new_alive) - set(old_alive)))
    if set(removed) != set(EXPECTED_REMOVED_ALIVE) or added:
        raise LLError("alive inventory delta drift: removed=%r added=%r" %
                      (removed, added))
    if set(new_alive) != set(EXPECTED_FULL_ALIVE):
        raise LLError("full-actual alive inventory drift: %r" %
                      (new_alive,))
    return {
        "legacy_carrier": REPRESENTATIVE,
        "promoted_carrier": FULL_ACTUAL_FIRST_SEPARATION,
        "canonical_alias": FULL_ACTUAL_EXIT,
        "semantics": LOWER_FLOOR_ONLY,
        "attainment": False,
        "unique_cells_checked": len(unique),
        "changed_cells": rows,
        "unchanged_cell_count": len(unique) - len(rows),
        "old_alive_count": len(old_alive),
        "new_alive_count": len(new_alive),
        "old_alive": [list(x) for x in old_alive],
        "new_alive": [list(x) for x in new_alive],
        "removed_alive": [list(x) for x in removed],
        "added_alive": [list(x) for x in added],
    }


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


def compile_book(td=TD, m=M_POLES, readers=None, evidence_readers=None):
    # R-6/R-7 provenance gate FIRST: pins, clause anchors, fixture parse,
    # engine parity -- any drift aborts the compile (fail closed).
    provenance = build_provenance(readers, evidence_readers)
    price_audit = repricing_audit()

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
                   "single merge; lam=0; family-level parity with the "
                   "frozen 26-shape/351-route engine record is gated in "
                   "provenance.engine_parity (R-7), fixture-cited via "
                   "ENGINE-REC, engine not re-run",
            "closure_certificate": {"W": [str(w) for w in W], "gen": 0,
                                    "d0_safe": 2},
            "cert_chain": cert("DS1", "DS2", "DS3", "MP5", "MP1",
                               "ENGINE-REC"),
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
    cells, pure_b = dirty_cells(
        Fraction(3, 2), 2, TD - 2,
        nonzero_carrier=FULL_ACTUAL_FIRST_SEPARATION)
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
        price_rules = ["P0", "AF2", "St 8.4"]
        if c["mults"]:
            price_rules.append("FULL-ACTUAL-FIRST-SEPARATION")
        srows.append({
            "record_id": "SUFFIX/dirty-(%d,%d)" % (c["dp"], c["dq"]),
            "family_spec": {k: _f(v) for k, v in c.items()},
            "classification": "COVERED",
            "verdict": "DEAD" if dead else "ADMITTED",
            "why": ("M=1 on the trunk (lam moot)" if dead else
                    "-> (w,M) = (%s,%d), lam >= %d; W-PRICED-COMPLETE"
                    % (c["w_child"], c["M_child"], c["lam"])),
            "w_cert_child": None if dead else W_PRICED_COMPLETE,
            "cert_chain": cert(*price_rules),
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
    terms, steps, states = residue_enumeration(
        TD, nonzero_carrier=FULL_ACTUAL_FIRST_SEPARATION)
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
        "packet": "LL1-R4 (td=6, m=2; full-actual floor)",
        "date": "2026-08-29",
        "provenance": provenance,
        "pricing_policy": {
            "nonzero_carrier": FULL_ACTUAL_FIRST_SEPARATION,
            "canonical_alias": FULL_ACTUAL_EXIT,
            "representative_carrier": REPRESENTATIVE,
            "nonzero_floor": ("delta if delta is a positive integer; "
                              "ceil(2*delta) otherwise"),
            "epsilon_zero_rule": "legacy representative AF2",
            "semantics": LOWER_FLOOR_ONLY,
            "attainment": False,
        },
        "repricing_audit": price_audit,
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
            "FULL_ACTUAL_FIRST_SEPARATION is a complete-carrier lower-floor "
            "license on this fixed-fibre two-pole consumer. It does NOT "
            "assert attainment or occurrence of any row.",
            "Generic MP8/MFE remains REPRESENTATIVE and is not repriced by "
            "analogy. Epsilon/zero directions retain their legacy rule.",
            "The mixed all-mu>=2 emission menu is OPEN in general "
            "(BOOK-OFFAXIS sec.3); at this header it is unreachable, which "
            "is a divisibility fact, not a completeness theorem.",
            "The 26-shape / 351-route figures are FIXTURE-CITED frozen "
            "engine history (twopole_check.py phase 4 as recorded in the "
            "pinned bytes of SHEET6-DEPTH.md and SHEET6-DEPTH-REVIEW.md); "
            "this packet does not re-run the engine, does not re-derive "
            "those counts, and claims only the parity checks listed in "
            "provenance.engine_parity.",
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
        "source_pins": [
            "%s %s" % (p, h)
            for p, h in sorted(book["provenance"]["source_pins"].items())],
        "evidence_pins": [
            "%s %s" % (p, h)
            for p, h in sorted(book["provenance"]["evidence_pins"].items())],
        "nonzero_carrier": book["pricing_policy"]["nonzero_carrier"],
        "canonical_alias": book["pricing_policy"]["canonical_alias"],
        "pricing_semantics": book["pricing_policy"]["semantics"],
        "attainment": book["pricing_policy"]["attainment"],
        "changed_cells": book["repricing_audit"]["changed_cells"],
        "unchanged_cell_count":
            book["repricing_audit"]["unchanged_cell_count"],
        "old_alive_count": book["repricing_audit"]["old_alive_count"],
        "new_alive_count": book["repricing_audit"]["new_alive_count"],
        "removed_alive": book["repricing_audit"]["removed_alive"],
        "consumed_clauses_present": sum(
            1 for c in book["provenance"]["consumed_clauses"]
            if c["status"] == "PRESENT"),
        "engine_record_headline": "%d shapes / %d parent pairs "
            "(fixture-cited)" % (
                book["provenance"]["engine_record"]["shapes"],
                book["provenance"]["engine_record"]["parent_pairs"]),
        "rederivation_decision_changes": len(
            book["provenance"]["rederivation"]["decision_changes"]),
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
    print("LL1-R4 compile OK (%d canonical source pins + %d evidence pins "
          "verified, %d consumed-clause anchors present, carrier typed, "
          "13->7 replay exact)" %
          (len(SOURCE_PINS), len(EVIDENCE_PINS), len(CONSUMED_ANCHORS)))
    for p, h in sorted(book["provenance"]["source_pins"].items()):
        print("  pin %s  %s" % (h, p))
    for p, h in sorted(book["provenance"]["evidence_pins"].items()):
        print("  evidence %s  %s" % (h, p))
    for k in sorted(digest):
        print("  %s  %s" % (digest[k], k))
    return 0


if __name__ == "__main__":
    sys.exit(main())
