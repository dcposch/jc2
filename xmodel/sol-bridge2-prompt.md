You are GPT-5.6 Sol, senior co-researcher on the plane-Jacobian-Conjecture
campaign. Repo: /Users/dc/code/math/jc72108. Deep-read xmodel/sol-pc.md (the G5
terminal: DIR(C), the polar-excess defect Delta_P, the canonical differential
omega=dg/j) and xmodel/sol-ucda.md (the G2 terminal: A-SCALE, the branch
conductor c(P_i)=2 delta(P_i) >= 2(kappa_i-1), ord_t f_y = 3-kappa_i) IN FULL;
also xmodel/sol-rpmc.md §0-§4 (the exact intersection-defect identity) and
xmodel/sol-unify.md §1 (the residue-A ladder 1->7->21->42, prod nu_j=kappa_i).
Accept all as EXACT/PROVED. Write to xmodel/sol-bridge2.md. Char 0.

CONTEXT. Both foundational walls have bottomed out at ONE terminal conjecture
each, and BOTH are local invariants of the SAME residue-A germ:
  * G5 terminal DIR(C): the polar-excess intersection defect
    Delta_P = sum_{gamma|P} max{0, ord_gamma F_X - (d-2)m_gamma} <= C alpha beta mu/B.
  * G2 terminal A-SCALE: bound the pole Puiseux denominator kappa_i (equiv. the
    Sigray rectangle base a+b), for which sol-ucda proved the branch conductor
    c(P_i) = 2 delta(P_i) >= 2(kappa_i - 1).

THE QUESTION (a genuine new connection, not another reduction). Delta_P (polar
excess, G5) and delta(P_i) (delta-invariant/conductor, G2) are BOTH classical
local invariants of the residue-A branch. Decide their relationship precisely:

  Q1. On the residue-A pole branch, express BOTH Delta_P and delta(P_i) in the
      same local coordinates (the Puiseux/approximate-root data nu_1..nu_s,
      kappa_i = prod nu_j, and the pole orders m_gamma). Use ord_gamma F_X on
      the branch: since J=f_x g_y - f_y g_x = j and ord_t f_y = 3 - kappa_i
      (sol-ucda 0.3), relate ord_gamma F_X to the branch data. Is there an
      EXACT identity or inequality linking Delta_P and delta(P_i)? E.g. is
      Delta_P a linear function of the same nu_j that build kappa_i, so that a
      bound on one constrains the other?

  Q2. If delta(P_i) (hence kappa_i via the conductor) grows, does Delta_P
      necessarily grow (making DIR the STRONGER wall, so DIR => A-SCALE), or can
      Delta_P stay bounded while kappa_i -> inf (walls genuinely independent
      even at the germ level)? Test on the exact residue-A ladder and on the
      formal l=0, nu=2 insertion tower (kappa_i = 42*2^r): compute how Delta_P
      behaves as r grows. Does the polar excess of the r-fold tower diverge
      with kappa_i, or not?

  Q3. THE NO-DECOY KEYSTONE. Is there a SINGLE local rigidity statement about a
      degree-minimal noninvertible residue-A Keller germ -- e.g. a bound
      coupling Delta_P and delta(P_i) via the constant-Jacobian relation -- that
      implies BOTH DIR(C) and A-SCALE? Or a proof that no such coupling exists
      (they are independent local invariants, so the two walls need two separate
      proofs even locally)? The Henon tower (td=1 automorphism, kappa->inf) and
      the non-Keller class-kill family (extra Jacobian curve) are the two decoys
      each wall must exclude; does one invariant exclude both decoys?

DELIVERABLE (xmodel/sol-bridge2.md): a verdict -- LINKED (with the exact
identity/inequality and which wall implies which), or INDEPENDENT (with the
germ-level separating example) -- and, if linked, the sharpest single
no-decoy invariant. Label every unproved inequality CONJECTURE. Exact
arithmetic; use the banked residue-A numbers (kappa=42, nu ladder 7,3,2,
passport {2,3}, w=2) concretely. Terse, technical, honest tiers.
