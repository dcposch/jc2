# Hostile review assignment: delayed-load source exclusion of the affine-Faber `A` cubic

Work in `/Users/dc/code/math/jc2`.  Review exactly

```text
xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-20260826.md
```

whose required SHA-256 is

```text
9419c08b4be09fee8ecae9b73c8c9c610770a7166e17a973251312d28b69a695
```

The charged exact cubic-form input is

```text
xmodel/max12-812-order2-affine-faber-exceptional-cubic-forms-source-ray-triage-20260826.md
```

with required SHA-256

```text
40b6d15eb23fc85038182146d8f044dee3d37c7c7e6fc4880e0ac3d223297d5f
```

The charged total-Rees audit is

```text
xmodel/max12-812-order2-affine-faber-total-rees-gate-a-audit-20260826.md
```

with required SHA-256

```text
24592572b4a6469ca5cdf446d02a8acc71ca6ee540ad3b73b92e9f925b10edb6
```

Write the unique report to

```text
xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-hostile-review-grok-20260826.md
```

Do not edit any other file and do not touch `jc2-lean`.  This is an
adversarial mathematical audit, not a trust pass.  Do not accept producer
status lines or printed residuals as evidence.  Independently rederive the
mathematics by hand; do not invoke Singular, Sage, SymPy, msolve, Lean, or
another CAS.

Audit at least:

1. Reconstruct the literal source substitution
   `k10=Lambda^12*K10`, `k6=Lambda^8*K6`,
   `k2=Lambda^4*K2`.  Verify that all effective lower loads first occur at
   `Lambda^14`, that the displayed seven-row central face and target offsets
   are correct, and that the graph is prime, `Lambda`-torsion-free, and
   invertible on `D(Lambda)`.  Flag any hidden normalization claim.
2. Check the primitive terminal tie.  Starting from a normalized cubic
   terminal `J3*t^3` and the row-seven source target five orders after the
   loaded face, verify `3*v(t)=5*v(Lambda)` and the primitive ramification
   `Lambda=sigma^3`, `t=sigma^5`.
3. Reprove the unloaded first-normal condition.  Verify that the seven
   predecessor rows vanish iff `Q0 | N^2`, the squarefree discriminant claim
   on `D(r*D)`, and the repeated-root divisor
   `Q0=z^2(z^2+p)`, `D_Q0=z(z^2+p)` when `r=0`.
4. Independently substitute the `A`-face cubic forms.  On `D(r)` check the
   eliminations through the residual `5*x^3*D/128`.  On `r=0` check
   `u=(p/2)*v`, the formulas for `v` and `g`, cancellation of every `b` term,
   and the residual `5*x^3*p^3/1024`.  Identify the first wrong identity if
   any.
5. Audit the direct rational-witness rejection: derive the
   `Lambda^10*(3/3200)z^6/(z^4-1)` predecessor and its ordinary `R2,R6`
   connection, including signs and the factor `1/2` in row six.
6. Attack omissions: tangential motion of `p,D` or the quartic center,
   moving-center cross terms, deck/ramification choices, normal variables at
   earlier orders, nilpotents, and whether any such omission invalidates the
   narrow primitive cubic claim.
7. Enforce the firewall.  The strongest possible conclusion is only the
   primitive unit-`J` cubic `A` client on this integral delayed-load ray.  It
   is not an exhaustive load-fan theorem, a later-`J` theorem, a `K`-face
   theorem, a total order-two exclusion, or JC2.

Report exactly one overall verdict: `CONFIRMED`, `REPAIR`, or `REFUTED`.
State the smallest failing identity or missing hypothesis, the strongest
exact theorem that survives, and the precise scope firewall.  End with
exactly one standalone verdict token.
