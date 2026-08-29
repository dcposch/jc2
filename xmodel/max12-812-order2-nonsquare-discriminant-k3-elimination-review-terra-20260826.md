# Hostile review: nonsquare discriminant K3 elimination composition

Date: 2026-08-26

Verdict: **CONFIRMED after custody repair.**

Reviewed immutable pair:

```text
96f59880e588a5689d6eed331f7fe2fa1bed7640da7899775dc7bde43004ea71
  xmodel/max12-812-order2-nonsquare-discriminant-k3-elimination-promotion-20260826.md
6eb104a3288bf663aced9b8aa6f0bdac3a91c9cb6bd26d44e4b4989a5efe7c36
  cases/max12_812_order2_disc_halfweight_kuranishi_v3_row_identity_20260826/RESULTS.sha256
```

The prior custody defect was repaired by hashing `REGISTRATION_RETRY1.md`
in the RESULTS manifest.

## Findings

1. From `w^4=A^2(A^2+b*A+e)`, `q=A/w`, and `v=w^-1`, one gets exactly
   `q^4+b*v*q^3+e*v^2*q^2=1`.  Also `A^-j=v^j*q^-j`; the exact client checks
   the correct orientation
   `16*source_l=sum_(j<=l)T_(l,j)*analytic_j`.

2. The recurrence constructs `T` over `Q[b,e]` with diagonal one.  Its
   inverse is again polynomial lower unitriangular.  Since sixteen is a
   rational unit, the seven coefficientwise identities prove inclusion both
   ways and exact equality of the two seven-row ideals before localization,
   reduction, or saturation.

3. The initial relative-path launches failed before freeze validation or
   compilation and are retained only as no-verdict controls.  The retries
   changed only the output path.  Both successful lanes verify the frozen
   source, record compiler and engine return code zero, contain one copy of
   every required sentinel, and have PASS validators.

4. Polynomial ideal equality persists under localization by `m` and `b`.
   In `R_bm`, the analytic V2 theorem gives the raw nonreduced scheme
   `(kappa,e,U^2,F)`, with `U=h+b*y` and
   `F=m^3+6*h*y+6*y*U`.  Its two complementary rows are triangular, so
   solving them after `m` inversion discards no source component.

5. The reduced support parametrization
   `m=6*b*t^2`, `y=6*b*t^3`, `h=-6*b^2*t^3`, `b*t!=0` exhausts the stated
   `D(b*m)` chart.  Both free complementary-kernel parameters `q,s` remain
   in the source calculation.

6. Because source and analytic K2 ideals agree as raw ideals, the
   nonreduced conormal `U^2` and its valuation fan transport componentwise.
   The only new primitive fractional ray is `(1,2,2,2)` after
   `rho=sigma^2`; strict inequalities are its faces.  The reviewed client
   retains the raw square direction and tangent motion.

7. The normalized complete-source successor ideal is unit on `D(b*t)`.
   Later lower loads, scalar or terminal rows, and Taylor equations cannot
   restore a branch that already fails this necessary tail condition.

8. Scope is correct: the result excludes only the source-typed nonsquare
   discriminant first-normal component on `D(b*m)`.  It does not cover the
   square component or `b=0` intersection, all Taylor receivers, all order
   two, `(8,12)`, maximum twelve, or JC2.

No remaining smaller failing identity or hypothesis was found.
