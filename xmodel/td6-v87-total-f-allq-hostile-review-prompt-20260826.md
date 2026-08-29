# Independent hostile review charge: TD6 V87 total-`(F,all licensed q)`

Date: 2026-08-26

You are an independent hostile mathematical/software reviewer. Do not edit the
producer package, any campaign ledger/top-level coordination file, or
`jc2-lean`. Your only allowed repository write is the required report:

```text
xmodel/td6-v87-total-f-allq-hostile-review-20260826.md
```

Write that report even if the verdict is negative or execution is blocked.
The first substantive line must be exactly one of `CONFIRMED`, `REPAIR`, or
`BLOCKED`. State the smallest exact repair for every defect. Do not promote a
producer assertion merely because two executions agree.

## Frozen producer

Package:

```text
cases/td6_c1_c2_c3_total_f_allq_raw_p12_source_v87tfaq_aws_20260826/
```

Custody pins:

- `RESULT.md`:
  `6e22c6ac16f9e164b760367cf65b970649e9235f185e8ec82f8e28dbd6859bda`;
- `AWS_LAUNCH.md`:
  `e11b19e69fbe816a49592225e79dbba0a9acc504d9c249ef00c010a51205c19e`;
- `EVIDENCE.sha256`:
  `074072f04a88b2e74e1545afdbdd173e8dbc0d68bd2052b6ea37ebad05e754c5`;
- `FREEZE.sha256`:
  `ef39fef7983ed3251bc21b3dd4f53db075f816cd95ffb7a38511956d7d9c60b9`;
- `SOURCE.sha256`:
  `f82ebe8ef8018542c02d9cbe3654c84b2c6336f442d5e8b83633cdeebbf3e874`;
- source archive:
  `e80b1cba7b4a1749c7f12ecd7b6a8d9418e73b6b01d8f82081dbb76f113669d3`;
- V87 client:
  `7c0890abbce996a221f9389372fa3705742d6ecd72531891bfeb5dfc2f1b9463`.

Validate `EVIDENCE.sha256`, `FREEZE.sha256`, and `SOURCE.sha256` before using
the producer prose. Use the two frozen AWS evidence trees. A bounded exact
independent replay is welcome, but a second execution of unchanged producer
code is not by itself review.

## Claim under review

Let

```text
F = C*U - V^2 + U^3,
H = C - 3*U^2,
E = {2,...,14,16,...,24},
q(t) = t + sum_{e in E} q_e*t^e + t^25.
```

With all 132 transport-free coordinates retained, V87 claims an exact
identity in `Q[C,V,U,q_e:e in E]_{U*H*B3}`:

```text
U^12*H^3*B3
  = a_P*P12 + sum_i a_i*FIRST_i + F*h_F + sum_{e in E} q_e*h_e.   (1)
```

The `a_P,a_i` are the frozen V82QST3 multipliers. The producer reports total
q-degree one for both source and residual and common denominator exactly
`C*U-3*U^3=U*H`.

## Required hostile checks

1. **Exact 22-jet scope and q15.** Verify that the represented source family
   is exactly `q2..q14,q16..q24`, with no duplicate or omitted licensed jet.
   Check independently that q15 is the lower target-shear coordinate for
   fixed `p=t^15`; distinguish a legitimate quotient coordinate from a
   silently omitted source modulus. Confirm that (1) makes no unit-q claim.

2. **Literal source custody.** Trace each q variable through both the affine
   transport RHS `('g','X',0,e)` and direct `e*q_e*t^(e-1)` contribution to
   `q'`. Check that transport is not accidentally square-zero or truncated,
   that raw degree-12 CURRENT is extracted literally, and that no staged
   CURRENT/PREVIOUS/POLE row enters P12/FIRST.

3. **Omission controls.** Inspect all 44 fixtures. Verify that each one
   separately removes the intended transport or direct path, that the raw
   FIRST comparison is nonvacuous, and that no shared mutation/order effect
   can make a fixture pass spuriously.

4. **Polynomial coefficient type and augmentation division.** Audit `QPoly`
   for exact untruncated multivariate arithmetic and fail-closed inversion.
   Prove or refute that `decompose_q_residual` gives an exact decomposition of
   every polynomial with zero constant q part into the augmentation ideal,
   including arbitrary cross-q powers. Check that it never divides by a q
   expression in the coefficient ring. Independently verify the final replay
   of (1), not just inventory hashes.

5. **Degree telemetry.** Verify the reported `total_q_degree=1` and
   `residual_q_degree=1` from the actual represented polynomials. Explain why
   this means no cross-q terms occur here while the partition algorithm does
   not rely on linearity.

6. **V85 and V86 specialization.** At all q zero, independently compare P12
   and all 38 FIRST maps with the frozen V85 inventory, check the 2,893-term
   P12 and labels `0..131`, verify the frozen V82QST3 special identity, and
   verify that the q-zero `F` quotient equals frozen V85 `h_F`. In addition,
   set all q except q2 to zero and determine whether the represented V87
   source/identity really specializes to the reviewed V86 total-`(F,q2)`
   family. If the producer does not contain a sufficient exact comparison,
   classify that as a custody/proof gap and give the smallest repair rather
   than inferring it from shared code.

7. **Denominators and clearing.** Check completeness of the 312,604-value
   denominator audit: multipliers, all sources, all products, `h_F`, and all
   22 `h_e`. Verify that the LCM is exactly `U*H`, that neither `F` nor any q
   variable is inverted, and that one clearing replays all 5,626,872 scalar
   coordinates. Check the P12/FIRST omission negatives.

8. **Dual AWS custody.** Independently hash both evidence trees and reconcile
   source archive, stdout, four mathematical outputs, return codes, elapsed
   time, memory cap/RSS, and zero-swap claim. Distinguish host metadata that
   should differ from mathematical artifacts that must agree.

9. **DVR consequence.** Prove or refute the narrow consequence: on
   `D(U*H*B3)`, there is no DVR arc in this exact represented source family
   with all P12/FIRST rows zero and positive valuation for `F` and every one
   of the 22 q variables. Check that coefficients of every `h` are regular on
   that open. Explicitly reject any extension to a unit-q chart, q15,
   omitted correction/orbit/pole/center/deck/torsion/boundary variables, a
   total-Rees chart, whole fixed A3, TD6, SP-2, or JC2.

Conclude with a concise dependency table: producer assertion, independently
checked evidence, verdict, and smallest repair if applicable.
