# Hostile cross-review charge: cutoff-four upper-endpoint field obstruction

You are Fable 5 in an independent hostile mathematical-review lane.  Work in
`/Users/dc/code/math/jc2`.  Audit the claimed exact result in

```text
cases/ggv_8_28_upper_endpoint_tail4_desk_20260828/
RESULT.md sha256 f5b3b6ec80648972f66b0bd057f0128bffba6682dc84d9348ded49093205ca9e
analyze_tail4.py sha256 2e4edbaded44a53eee1f4639f55617fbb94159c68be98d1c45f8b350b55d663c
TAIL4_DESK_ANALYSIS.json sha256 3a1dc7eff0598e76cf0a284e2b4bc93d6e887b1069079cb0ecc5035783221fe5
```

The upstream authority is the literal branch-P raw determinant system,
whose expected SHA is printed in the packet.  The producer claims that the
fixed square-baseline specialization obtained by setting every raw
deformation parameter of weight below four to zero has no
characteristic-zero field-valued endpoint point.  This is deliberately a
field-radical statement, not scheme emptiness or a JC2 theorem.

Do a clean-room audit, not a prose plausibility check.  You may run the
producer replay, but every load-bearing identity must also be reconstructed
with fresh code or independent hand algebra.  No heavy local CAS; ordinary
standard-library exact arithmetic is allowed.  Do not access `jc2-lean`.
Write only the final report

```text
xmodel/ggv-upper-endpoint-tail4-field-obstruction-crossreview-fable5-20260828.md
```

and temporary files outside the repository.  Do not edit campaign ledgers.

At minimum, charge all of the following:

1. Verify both manifests and source hashes, then replay `analyze_tail4.py
   --check`.  Independently reconstruct the cutoff-four specialization from
   the frozen recurrence/raw data: retained-variable census, prefix
   rank/nullity, remaining constraints, and literal endpoint signs and
   carrier lifts.  Detect any stale specialization or row rescaling.
2. Independently reconstruct every D8--D15 compatibility step.  Check the
   exact remainder models, degree windows, progressive substitutions, and
   provenance to literal determinant rows.  Distinguish the eight
   square-to-divisibility field-radical steps from ideal equalities.  Look
   especially for a missed scalar equation, an unjustified cumulative-span
   use at D14/D15, or an illicit carrier division.
3. Verify the monic scalar eliminations, the displayed `E13,E14,E15`, the
   carrier formula, and absence/licensing of the `p161=F8[X^0]` additive
   gauge.  Confirm no endpoint carrier was normalized.
4. Reconstruct the D18 invariant
   `v*(b*v+r^2)` from charged compatibility rows and trace its witness back
   to raw source rows.
5. On `v=0`, expand the frozen six-generator cofactor packet independently
   and require the literal constant `1`.  Check that the endpoint and
   carrier signs are the actual ones and that no localization is hidden.
6. On `v!=0`, independently derive—not merely substitute—the formulas
   `b=-tau^2*v`, `h=(3/8)*v*tau^2*(4*tau-1)`,
   `x=(tau^2/2)*(12*tau^2+6*tau+1)`, and
   `v=-(3/4)*tau^2*P3(tau)`, with
   `P3=(4*tau+1)*(16*tau^2+6*tau+1)`.  Verify exactly that the serialized
   D20 compatibility combination is `tau^9*P3^3`, including all staged and
   literal-source provenance.  Confirm that `v!=0` forces
   `tau*P3!=0`, so the D20 equation is a contradiction, and that the
   apparent roots are only `v=0` boundary points.  Check that neither the
   endpoint nor D21/D22 is silently used on this branch.
7. Run hostile mutations that touch load-bearing source coefficients,
   radical shifts, endpoint signs, `P3`, D20 cofactors, and the localization
   hypothesis.  Separate a broken frozen witness from a genuinely changed
   conclusion.
8. Search actively for alternate surviving field points, a missing branch,
   denominator loss, characteristic assumption, or overclaim.  State the
   exact strongest justified theorem and all firewalls.

Return `PASS`, `REPAIR`, or `FAIL`, rank every issue by mathematical impact,
and give an unambiguous promotion recommendation.  Include enough exact
identities, ranks, and mutation residuals that another coordinator can
check your audit without trusting the producer.
