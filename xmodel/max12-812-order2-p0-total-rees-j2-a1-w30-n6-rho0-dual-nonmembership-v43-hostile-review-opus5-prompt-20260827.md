# Hostile review prompt: V43 exact-Q rho-zero dual at exponent six

Date: 2026-08-27

Act as an adversarial commutative-algebra and exact-CAS reviewer.  Review the
new exponent-six nonmembership result independently from producer verdict
strings.  Use shell scripts and exact desk-scale checks where useful, but run
no heavy local computation and launch no AWS job.  Do not edit canonical
ledgers.

## Claim under review

Producer report:

`xmodel/max12-812-order2-p0-total-rees-j2-a1-w30-n6-rho0-dual-nonmembership-v43-sol-20260827.md`

SHA-256:

`7345d4a8dda7afd9f45dd6b938a5ec0e15ff642e4809da5434ef35eb505f446d`.

It claims an exact rational functional `Lambda` with

```text
Lambda(a1^6)=1,
Lambda(m*Tg_g_j|_(rho=0))=0
```

for every complementary-weight product through grade 19.  It concludes
`a1^6 notin J0`, hence no literal-total identity
`a1^6 U(rho^2) in J` with `U(0)=1` (indeed no factor `1+rho W`) exists.

## Frozen evidence

Compiler/matrix harvest:

`cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827/aws_r6d_rho0_dual_compiler_20260827T085739Z/`

with `HARVEST.sha256` SHA
`3ddea4ae8b172fcc43136494f1080756f5d04f183ac61a7a8dcd13b1d4e2f737`.

Exact solve/replay harvest:

`cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827/aws_r6d_rho0_dual_exact_resume_20260827T091000Z/`

with `HARVEST.sha256` SHA
`98b41d273b8a4ab20749e702ad14490f52ac772908a6d7b9df29a6302cbee0ab`
and `EVIDENCE.sha256` SHA
`acb72647ac1e0a9e6adfdd802a3769f6beb211033b1b93aa4fb67bbe63ea529f`.

Launched compiler:

`cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827/compile_total_dvr_w30_v43.py`

SHA
`0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00`.

Compiler-delta review:

`xmodel/max12-812-order2-p0-total-rees-j2-a1-v43-compiler-postreview-delta-hostile-review-fable5-20260827.md`

SHA
`ae8ecf1887a62afd873fc795d0eeec50ff0aac6e4954813931d09a34c8bfc31a`.

Trace every additional theorem/compiler pin from these artifacts.  Recompute
all manifest and evidence hashes.  Never treat `PASS`, `ENDPOINT`, stdout, or
JSON outcome fields as proof.

## Mandatory attacks

1. Reconstruct the exact rings and alphabet.  Confirm 66 positive total
   variables, 65 on `rho=0`, `ez9` as the sole added literal variable and a
   spectator after specialization, 70 named rows/59 nonzero rows, their
   sigma weights, and `wt(a1^6)=30`.
2. Prove or refute completeness of the unrestricted weight-30 Macaulay span:
   every homogeneous multiplier of complementary weight, no total-degree or
   support cutoff, no omitted zero-weight variable, and no row beyond grade 19
   needed for a weight-30 representation.  Audit the passage from homogeneous
   component membership to polynomial-ideal membership.
3. Independently inspect/reconstruct the literal rows and products.  Verify
   the claimed 284,766 nonzero products; target component census 26,200
   products, 66,076 monomials, 66,075 unknowns, 616,678 nonzeros; all frozen
   row and product hashes; and that component restriction is used only to
   solve, never to weaken final replay.
4. Parse the exact solution and certificate without trusting the validator.
   Verify common denominator
   `34670334774018800828908752076800000`, support 3,395 including target,
   exact value one on `a1^6`, and exact annihilation of the serialized target
   component.  Use an independent sparse replay if it remains desk-scale.
5. Audit the independent validator source byte by byte around reconstruction,
   certificate decoding, full-product iteration, and failure handling.
   Establish whether it truly evaluates all 284,766 freshly reconstructed
   products rather than a cached/subselected set.  Check the deliberate
   `Tg15_3` coefficient corruption gives residual exactly one and cannot be a
   vacuous mutation.
6. Verify compiler/solver/validator source custody, remote-source manifest,
   normal termination, absence of failure/timeout/OOM markers, and exact-Q
   arithmetic.  Search for transposed matrix conventions, target-column sign
   errors, one-based indexing, duplicate product collapse, stale coordinates,
   wrong RHS, or a certificate replayed against the same faulty serializer
   that generated it.
7. Independently prove the logical conclusion from specialization
   `rho -> 0`.  Check that it needs no saturation-flatness converse, parity,
   localization, or Hensel assertion.  State precisely whether it excludes
   only exponent six or, together with earlier reviewed work, all exponents
   at most six.
8. Search for the smallest failing identity or missing hypothesis.  Preserve
   the firewall: no higher-power, selected-row dehomogenized, chart-closure,
   Gate-T, order-two, maximum-twelve, or JC2 verdict follows.

Give line-item verdicts `PASS`, `REPAIRABLE`, or `FAIL`, with exact file,
hash, and equation citations.  State the strongest theorem that survives and
the cheapest next computation or review obligation.

Write the complete report to exactly
`xmodel/max12-812-order2-p0-total-rees-j2-a1-w30-n6-rho0-dual-nonmembership-v43-hostile-review-opus5-20260827.md`.
Touch no other campaign artifact.  Do not enter, read, build, status-inspect,
or modify `jc2-lean`.  No web sweep and no canonical-ledger edits.
