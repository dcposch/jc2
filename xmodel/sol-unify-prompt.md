You are GPT-5.6 Sol, senior co-researcher on a plane-Jacobian-Conjecture
campaign. Repo: /Users/dc/code/math/jc72108. Deep-read xmodel/sol-rooftop.md
and xmodel/sol-bdelay.md IN FULL, plus TDBOUND.md and SHEET6-DEPTH.md. Then
attack ONE precise question. Write your deliverable to xmodel/sol-unify.md.

CONTEXT — both foundational walls of the campaign have just been sharpened to a
single Keller-specific arithmetic bound each, and the SAME local invariant ν_P
appears in both:

  * G2 (transport / bounded-delay) ⟸ CONJECTURE UCD (sol-bdelay §5):
    the pole Puiseux denominator satisfies κ_i = ∏_j ν_j ≤ K, uniformly
    (K independent of coefficient cutoff and of the chosen compatible
    continuation). Sufficient because ∏_j ν_j ≤ κ_i with ν_j≥2 gives
    sheet-depth d_sh ≤ log2(κ_i) = log2(K), i.e. bounded delay B=⌊log2 K⌋.

  * G5 (td-ceiling) ⟺ CONJECTURE KJN(C) (sol-rooftop §7):
    deg Ψ = αβ·td ≤ C(αβ)², equivalently the EXACT rooftop energy
    E_MR = td/(αβ) = Σ_P a_P b_P / ν_P ≤ C.

THE QUESTION. Are these two bounds the SAME bound, or genuinely independent?
Specifically, decide (with proof or explicit counterexample, not hand-waving):

  Q1. Are the ν_P in the rooftop energy Σ_P a_P b_P/ν_P the SAME ν's (or
      determined by / determining) the characteristic multiplicities ν_j
      whose product is the pole Puiseux denominator κ_i in the depth bound?
      Nail the precise relationship on the residue-A pole branch: is
      κ_i = ∏ ν_P over the places P lying on that branch, or is the relation
      looser? Use the banked residue-A data (ρ,ν,κ̄)=(1,2,5), w=2, the
      Belyi β(u)=u(u−2/3)³/(u²−u+1/6)² passport ((3,1),(2,2),(3,1)), and the
      D21→D25 exact records to make this concrete, not just formal.

  Q2. Does KJN(C) ⇒ UCD? I.e., does an upper bound on Σ_P a_P b_P/ν_P (with
      a_P,b_P≥1 integers) force an upper bound on ∏ ν_P = κ_i on the pole
      branch? Be careful about the direction: an UPPER bound on a sum of
      1/ν_P terms does NOT obviously cap ∏ν_P (large ν_P shrink the sum but
      blow up the product). BUT td itself = αβ·E_MR is the sheet count, and a
      bounded td bounds the NUMBER of characteristic places; combined with any
      per-place size control this could still cap κ_i. Determine whether
      KJN(C) plus the residue-A structural constraints (w=2 forces ν_j via
      the merged-emission law; the fixed A_4 passport pins local ramification
      to {2,3}) is ENOUGH to bound κ_i. If yes, give the implication chain
      KJN(C) ⇒ UCD explicitly. If no, give the obstruction / a family where
      td stays bounded but κ_i → ∞.

  Q3. Converse: does UCD ⇒ KJN(C)? (bounded pole denominator ⇒ bounded td?)
      Likely NO in general, but check whether it holds under the residue-A
      passport constraints.

DELIVERABLE (xmodel/sol-unify.md):
  - A verdict: UNIFIED (one bound closes both walls, with the implication
    proved), PARTIALLY UNIFIED (one direction under residue-A constraints), or
    INDEPENDENT (explicit obstruction / counterexample family).
  - The exact ν_P ↔ ν_j dictionary on the residue-A branch (Q1), with the
    Belyi passport {2,3} ramification data made explicit.
  - Whichever implication(s) hold, stated as clean lemmas with proofs; label
    every new inequality CONJECTURE unless proved from the stated identities.
  - If UNIFIED even partially: state the SINGLE Keller-specific bound that
    would close both G2 and G5, in its sharpest form. This is the headline —
    a single lemma retiring two foundational walls at once.
Exact arithmetic only; no floating point. Terse, technical, honest about tiers.
