# Preregistration — genuine mod-3 tangent/cokernel lift gate

At the one frozen normalized common-cubic witness modulo `3^11`, consume the
exact 299-row integer residual and Jacobian.  Solve the complete next-digit
system

```text
J(w) u = -F(w)/3^11  (mod 3)
```

in all 149 coefficient/core digits.  Compute the full 205-dimensional mod-3
left cokernel, emit an explicit obstruction if inconsistent, or an affine
particular and all 55 kernel directions if consistent.  Certify that the
three exact target gauges lie in the kernel and report the 52-dimensional
non-gauge quotient.

Any SAT result must reconstruct the literal integer `P,Q,H` and replay all
276 determinant plus 23 common-cubic rows modulo `3^12`.  No point sampling,
rational-kernel substitution, or omitted equation is allowed.

Execution must fail closed off Linux or without the registered AWS job tag.
This is one-witness/one-digit scope only.
