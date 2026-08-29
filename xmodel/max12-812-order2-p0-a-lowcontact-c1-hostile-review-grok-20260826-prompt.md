# Hostile review: fixed-`p=0` residual `A` chart, `C` contact one

Act as an independent hostile mathematical reviewer.  Work read-only except
for the one report below.  Do not edit case packages, shared ledgers, any
other `xmodel` artifact, or `jc2-lean`.

Write exactly:

`xmodel/max12-812-order2-p0-a-lowcontact-c1-hostile-review-grok-20260826.md`

The producer is provisional.  Verify these custody hashes before reviewing
the mathematics:

- `cases/max12_812_order2_p0_a_lowcontact_c1_20260826/RESULT.md`
  `162a279615931f93bd15e3ea176e46c30669449cae9e35dd41305d174559fd23`;
- its `RESULTS.sha256`
  `958dd6b3336d024f3b575420413ffa26b0b7811a6972a3e955c9ea2804810de1`;
- its `FREEZE.sha256`
  `c0b77f7effb05ec973ce367477246d6f42ca035099553a0732392064eb4059d4`;
- its compiler
  `acc9e10081725594d66c27b1a9c20fa9880efb37bee6c8441dcff4d1b274e38e`;
- the frozen high-contact predecessor theorem
  `xmodel/max12-812-order2-p0-a-highcontact-cech-elimination-promotion-20260826.md`
  `4aeee7980586fc4c7c5456c04b84b02527251f6bd68e10f5a028cc5d19ef1f16`;
- the imported complete raw-cusp V2 compiler and freeze
  `8abeda327a7362e0cd5bdc8b73135bc59e1883664e3824783e34c9182743686d` /
  `9616ff0af8d551a6becb482d95ea1ca7d899a3b9d04df05c7f2cc04af863de7c`.

Audit from the complete frozen seven-tail source, not printed PASS tokens:

1. Verify that the compiler sets every moving-`p` jet and the leading `R,C`
   coordinates to zero, retains arbitrary first `R` correction, and inserts
   `C=sigma*(e1*z+e0)/2+O(sigma^2)` with `A0=a1*z+a0`.
2. Recompute the complete absolute grade-eleven rows
   `g11_2=(3/8)*a0*e0` and
   `g11_1=(3/8)*(a1*e0+a0*e1)` in exact Q.  Check the Laurent/Faber row
   indexing and coefficient extractor independently.
3. On `D(a0)`, verify the raw triangular deduction `e0=e1=0`.  On
   `V(a0) intersect D(a1)`, use only the grade-eleven equation to set `e0=0`
   and then recompute the complete grade-twelve row
   `g12_2=(3/32)*e1^2`; verify that this is a registered unit only on
   `D(a1*e1)`.
4. Verify symbolically that all displayed rows are independent of every
   retained first `R` correction, so the contact-raising conclusion covers
   all `ord(R)>=1`, but no `R` contact zero direction.
5. Check that all seven tails, available corrections, `k10,k6,k2`, all four
   targets, and their exact grades remain in the compiler.  Determine rather
   than assume that later loads/targets do not enter grades eleven/twelve.
6. Check exact-Q evidence independently of the `F_65521` control, including
   compiled inputs, validators, AWS tags, resource records, and manifest.
7. Explicitly quarantine the generic V12/unbounded-`d=1` and eight-form fan:
   those sources omit lower-load terms at larger contact.  Decide whether
   this fixed-`p=0`, grades-eleven/twelve replay is independent of that defect.
8. Enforce the exact scope: this proves only fixed-`p=0`, leading `A!=0`,
   `C` contact one contact-raising.  It does not cover `C` contact two or
   three, `R` contact zero, the mixed `R`-contact-one sheets, the high-contact
   cone except through its separate theorem, total-Rees/base-change glue,
   moving `p`, the all-zero Pell/Chebyshev receiver, `k0=0`, all order two,
   maximum twelve, or JC2.

End with exactly one verdict token on its own line: `CONFIRMED`, `REPAIR`, or
`QUARANTINE`.  If not confirmed, give the smallest exact correction and all
downstream quarantine.  If confirmed, state the maximal source theorem and
the remaining low-contact/glue debt precisely.
