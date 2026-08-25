# Preregistration — solve the first B8 affine quadratic obstruction

Registered after the dual-host compiler returned the identical ANF SHA-256

```text
9121d7cb4ee5aa5f38f31312077c084dc98fbc1b4175c73cef4a95dadaad45a4.
```

The complete `W2` fibre has dimension 68.  Its `W3` compatibility system has
polynomial-span rank 81, quadratic-coefficient rank 42, tangent rank 41 at
the frozen point, and 39 exact pure-linear consequences.  This is therefore
the first genuinely nonlinear gate and must be solved before advancing any
selected digit branch.

The AWS-only successor must:

1. reconstruct the 39 pure-linear consequences from the pinned ANF, solve
   them exactly, and substitute their full kernel into all 81 equations;
2. emit the resulting canonical quadratic ideal, the exact map back to all
   68 predecessor parameters, and independent direct-substitution controls;
3. report the reduced variable/equation/tangent ranks and a certified linear
   subspace lower bound;
4. enumerate only the registered weight-at-most-two points as routing, never
   as a completeness claim, and replay every emitted literal witness through
   all 276 integer determinant rows with actual total/partial degrees;
5. emit two fail-closed Singular inputs for the whole reduced ideal: geometric
   `std/slimgb` dimension and the exact `F3`-point ideal obtained by adjoining
   every `s_i^3-s_i`;
6. accept a complete `F3` classification only from a terminal exact standard
   basis (and an independent complementary-order/engine replay).  The
   zero-dimensional quotient length after field equations equals the number
   of compatible `F3` predecessor digits because that field ideal is reduced.

For every compatible predecessor digit, the fresh `W3` digit is an affine
68-space.  Hence the truncation image is exactly this quadratic zero locus,
and the total finite `W3` family is its product with the fresh kernel.  No
finite sample, tangent rank, or one component can replace the whole ideal.

The scope remains fixed D12 and finite depth.  No inverse limit,
characteristic-zero map, counterexample, maximum-twelve theorem, or JC2
conclusion is licensed.

