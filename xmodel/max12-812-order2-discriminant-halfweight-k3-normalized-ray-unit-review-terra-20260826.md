# Hostile review: `(8,12)` order-two discriminant normalized ray

Date: 2026-08-26

Verdict: **CONFIRMED — as the explicitly scoped normalized-ray source
theorem, not as an unconditional full-discriminant or order-two result.**

Target:

```text
94fbced433f2677333417456f20b519d39ac8cc8650e745724a1104d87b34601
  xmodel/max12-812-order2-discriminant-halfweight-k3-normalized-ray-unit-theorem-20260826.md
```

## Findings

1. The exact K2 scheme, localization, and routing are correct.  The identity
   `I_K2=(kappa,e,U^2,V+6*y*U)` is only asserted in `R_bm`; `m=0` is
   excluded and `b=0` is routed to the square analysis.  The target preserves
   this scope.

2. No missing local formal or Puiseux ray was found.  For the local
   triangular complete intersection, the only fractional primitive normal
   slope is `ord(U)=ord(rho)/2`; `e,kappa,F` cannot occur below `ord(rho)`
   without producing an earlier independent initial form.  Higher valuations
   are coordinate faces or delayed terms of the `(1,2,2,2)` chart.  First
   tangent motion is included and its weight-two derivatives are checked.

3. The source includes `q,s`, all normal and correction variables, raw
   `U,F`, and first tangent cross terms.  The inverse truncations are checked
   modulo `(sigma^3,m0*mi-1)`.

4. All seven complete-source rows are compared independently, before unit
   saturation, with the unitriangular Laurent-to-Faber transform and the
   factor `16`.  Thus the source unit is not inferred merely from the
   analytic unit.

5. The last-three certificate is sound without replacing `W=U1^2` by an
   independent reduced variable: `b*L6+L7` forces `chi=0`, `L6` then forces
   `W=0`, and `L5` contradicts `b*t!=0`.

6. Custody is consistent.  The target, design, FREEZE, RESULT, and RESULTS
   hashes match their charged values; both manifests verify; and both lanes
   record the unique PASS validator.  Exact Q, not the prime lane, is the
   characteristic-zero producer endpoint.

7. The firewall is precise.  The explicit source branch result is
   unconditional.  The statement excluding every nonsquare discriminant K2
   point on `D(b*m)` remains conditional on the exact-Q proof of K2
   source/analytic equality.  The square route, Taylor conditions, and full
   order-two conclusion remain open.

No smaller failing identity or hypothesis was found.
