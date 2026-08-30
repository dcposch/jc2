# Hostile review assignment: quartic one-cusp function-pair reduction

You are GPT-5.5, acting as an independent hostile mathematical referee. Work
only from the exact charged files below, plus narrow primary-source checks for
the explicitly named Miyanishi, Chau, and Orevkov results if needed. Do not
inspect any sibling model report, `.log`, `.run`, receipt, live ledger,
uncharged file, or excluded nested workspace. Do not modify Git or any
repository file except the single required report.

Write your complete report to exactly:

`xmodel/block-descent-a1-quartic-cycle1-function-pair-hostile-review-gpt55-20260830.md`

and write no other file. End the mathematical body with a standalone
`<!-- BODY-END -->` line. Do not add a seal; the coordinator will custody-seal
the returned bytes after exit.

## Charged files

```text
0a6272060a03c0071ad8b4c71aef00f3c724284d9590dcab61a2e75169a8713f
  xmodel/block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md
70c1e16270564af7138cdc9f4b4ef396a17b398698694330ee5146ec8a273f5d
  xmodel/block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md.artifact.json
7d40e7ee6d5970c51d62f73bafaf11670cb32c06bd51859876ab526f0fdf8bab
  xmodel/block-descent-a1-quartic-cycle1-pseudoplane-companion-threat-map-sol56-20260830.md
2e6d82035df6717d1a39f31dc19b23b7c727bb940d4730d2c7ea9400e5433cce
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-sol56-20260830.md
ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7
  refs/chau1999_apm71_full.pdf
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
```

First reproduce every hash and the producer seal/manifest. If any charged
byte differs, stop with `CUSTODY_FAIL`.

## Review obligations

Reconstruct rather than paraphrase every major step and assign `CONFIRMED`,
`REFUTED`, or `GAP`.

1. Audit the exact pseudo-plane hypotheses and Miyanishi Lemma 2.5.2. Verify
   that the cyclic base change, normalization, deletion of `mu-1` lines, and
   retained open really give `A2`, a surjective etale map `f_mu:A2->U` of
   degree `mu`, and a genuine coordinate `x` with
   `rho o f_mu=a+c*x^mu`. Identify every needed normality/smoothness or
   trivial-bundle hypothesis.
2. Verify that `H=pi o f_mu` is a polynomial Keller map of geometric degree
   `4mu` with image exactly `A2-{n}`. Audit whether either factor is actually
   etale on its stated domain and whether a nowhere-zero polynomial Jacobian
   is necessarily constant.
3. Check the minimal-counterexample argument `mu=d1`, including the direction
   of the degree inequality, tower-degree multiplication, and the scope of
   the `d1=1` corollary.
4. Reconstruct the finite completion and the claim that the nonproper-value
   set of `H` is exactly `B union C0`, where `C0=pi(Phi)`. Check whether any
   hidden boundary divisor or image component can occur, and whether
   `n notin C0` follows as stated.
5. This is the highest-priority obligation: audit the Orevkov--Chau
   degree-at-infinity budget from the primary formula. Justify or refute each
   lower bound `2mu*r`, the additional cusp cost `mu`, and the deleted-line
   cost `mu-1`; decide whether contributions can overlap when `C0` initially
   coincides with a component of `B`, whether ramification-boundary curves
   are dicritical lines counted by the formula, and whether the `(2,2)` node
   is truly budget-free. Determine if inequality (0.7), `r=1`, and saturation
   actually follow.
6. If saturation survives, audit every equality consequence: degree-one
   normalization maps from deleted lines, immersivity, `C0!=B`, applicability
   and exact content of Chau's singularity theorem, and the forced same-fibre
   self-identification away from `c,n`. Distinguish singular image from
   critical parametrization.
7. Recompute the Euler identity for `D=V(b o H)` and the cyclic-orbit deficit
   formula. Check quasi-finiteness, flat-completion claims, the zero fibre,
   deletion signs, deck orbits, cusp alternatives, and all finiteness
   assumptions. Try small symbolic controls independently.
8. Audit the all-`mu` polynomial firewall: singularities, normalization genus,
   Euler number, fibre deficits, and precisely which stronger structures it
   fails to realize.
9. Seek a decisive successor. Determine whether the quartic algebra,
   `K_U=0`, saturation, or the two-component link at infinity forces the
   `C0` self-collision onto `B`, a critical jump, an extra bad ruling fibre,
   or a contradiction. If no theorem follows, state the smallest exact
   counter-control or missing lemma.
10. Give a maximum-safe theorem, every correction, exact blast radius, and
    the cheapest next attack. Do not infer exclusion of the whole one-cusp
    horn, a proper block, a counterexample, or JC2 unless actually proved.

No `charge_basis` line is expected unless you assert a genuinely new rational
exit price under the campaign schema; ordinary input hashes and geometry are
not a charge basis.
