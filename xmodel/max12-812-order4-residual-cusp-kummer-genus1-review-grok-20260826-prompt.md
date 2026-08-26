# Hostile review: order-four residual cusp and deck-genus gate

You are the independent different-model hostile reviewer.  Work read-only
except for the single deliverable

```text
xmodel/max12-812-order4-residual-cusp-kummer-genus1-review-grok-20260826.md
```

Review target:

```text
cd6c37c145e325a48dbf382453bde4c727b98a576897d10a1f9b3752ebdd1756
  xmodel/max12-812-order4-residual-cusp-kummer-genus1-gate-20260826.md
```

Read every charged exact artifact named in target Section 5, together with
the corresponding frozen inputs and metadata under
`cases/max12_812_order4_mu4_nonzero_quotient_passport_20260826/`.  Rehash
them.  Do not import the target's conclusions.

Adversarially check, at minimum:

1. the Newton hull, area, boundary length, and seven interior points;
2. irreducibility and what exact ideal membership does and does not prove;
3. whether length four plus Hessian-unit really proves four ordinary torus
   nodes over the algebraic closure;
4. every toric boundary point, including fixed points/corners, the repeated
   left tangency, the simple top root, and the primitive edges;
5. the HN interpretation at `q=-4/27`: one `(2,7)` branch, delta three,
   repeated slope `1/52488`, and especially `ord(v)=-6` rather than two
   branches of order `-3`;
6. the genus subtraction `7-4-3=0` and completeness of
   `div(v)=8P_0-P_ul-P_A-6P_B`;
7. exact-order-four irreducibility of `y^4=v`, every local inertia/point
   count, and the RH conclusion `g(Y)=1`;
8. the source firewall: identify the weakest exact projection/nonconstancy
   statement sufficient for exclusion, and reject any use of `rho`
   nonconstancy that does not actually force `(q,y)` nonconstancy;
9. whether `a_6=0`, saturation, components, or completion can evade the
   stated conditional result.

Keep conditional and unconditional statements separate.  The prior
nondegenerate toric theorem is only a control whose hypothesis fails here;
do not promote its genera 7/37/165.  Report any wrong constant or missing
place explicitly.  End the review with exactly one line:

```text
VERDICT: CONFIRMED
```

or

```text
VERDICT: REPAIR
```

or

```text
VERDICT: REFUTED
```
