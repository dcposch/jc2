# Hostile review assignment: affine-Faber `A` H17 open relative cone

Work in `/Users/dc/code/math/jc2`.  Produce an independent hostile review at
exactly

```text
xmodel/max12-812-order2-affine-faber-a-h17-open-relative-cone-direct-unit-hostile-review-grok-20260826.md
```

Do not edit any charged artifact, producer, shared top-level ledger, or
`jc2-lean`.  Recompute all SHA-256 pins before reading verdict prose.  Exact Q
is mathematical evidence; the finite-field support is only a software
control.  V7 has a displayed-label bug and V8 is a fail-closed negative; V9
alone is controlling.

## Charged theorem and custody

```text
513d11901c09046abbeb41f9c5f2441e023b27925fde861d4c873306c9fa1f63
  xmodel/max12-812-order2-affine-faber-a-h17-open-relative-cone-direct-unit-theorem-20260826.md

1244a648d3bc761ae6fe9dbc1be72cad3e09b650d3d98109ebd2b4081ac1bb15
  cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v9_20260826/RESULT.md
3c8f207fc7522b58835758126a1a15841e76c92e3bc8beacebb6e22c55c81f06
  cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v9_20260826/EVIDENCE.sha256
8bf9aa5e7485555fbeb0a19c0b9ae2dc106715b6c13da850c4bfdfe22925e237
  cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v9_20260826/FREEZE.sha256
6aec97c6b03eaca66e6a3df9d80da41884ae5225836b96a5ab269962dcfe4365
  cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v9_20260826/RESULTS.sha256
60658fb670ea1435e35655d86dc577472ab3213993461837819c1733a673c3df
  cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v9_20260826/evidence/Box02/aws_qcone/output/hseries_exact_support.json

9ee52ed12c5ca75b0f36fdaf4292be6165d6a4380550c87faab3a654b23306bc
  cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_sparse_dag_v4_20260826/evidence/Box02/aws_qdag/output/abstract_functional_support.json
357829d292056e823c102446b8e95f5822dad961859e832a689160bca1e3fbcd
  cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_secondary_odd_dag_v6_20260826/evidence/Box02/aws_qsecondary/output/abstract_secondary_support.json
```

Read the actual frozen analyzer, registrations, evidence, and original sparse
support producers.  Do not infer validity from PASS text.

## Required attacks

1. Reconstruct `Hseries=G-32F` directly from the complete abstract exact-Q
   supports and check all 630 resulting monomials and coefficients, including
   the unique coefficient `-2` of `lambda^3*M^3*E^2`.  Check the F65521
   reduction, but do not use it to prove the Q result.
2. Independently derive the affine weight of every variable for H17:

   ```text
   lambda:17; X,Y:q; R0,R1,S0,S1:2q; a:17-2q;
   K10,K6,K2:42; J:57; E,M:0.
   ```

   Intersect all 629 strict inequalities against grade 51.  Confirm or refute
   that the exact interval is `17/4<q<7`, inside `4<q<17/2`.  Rational q must
   be legitimate after common ramification; do not silently assume q integral.
3. Check the boundary bookkeeping rather than trusting labels.  The lower
   block must consist of exactly five terms, each with line `34+4q`; the upper
   block exactly three loaded `a^3` terms, each with line `93-6q`.  Identify
   the smallest omitted competitor if either count is wrong.
4. Audit the inference from unique abstract monomial to a raw-row unit.
   Verify the definitions of `F,G,Hseries`, all signs and factors, and that
   vanishing raw rows through valuation 51 kills the moving-`E` convolutions.
   Check target/load completeness: J starts at57; all K10/K6/K2 terms at42
   must be in the 630-term support; no mu-target belongs to P1,P3,P5,P7.
5. Attack coordinate/scope claims.  Decide whether moving jets of a,E,M,
   loads, complements, or the ramified base can lower a term or cancel the
   unique initial coefficient.  The strongest licensed claim should remain
   an internal normalized graph-support theorem, not literal source,
   normalized-Rees/total-Rees, factor-degenerate, whole order-two, max12, or
   JC2 coverage.
6. State the strongest correct theorem and the smallest wrong coefficient,
   missing hypothesis, or scope repair if any.

## Verdict format

Start with a table listing charged target/pins, recomputed hashes,
reviewer/model, smallest failing identity or missing hypothesis, and one
overall verdict: `CONFIRMED`, `REPAIR`, or `REFUTED`.  Supply enough exact
algebra and inequality calculation to audit without producer prose.  End
with the verdict token alone.
