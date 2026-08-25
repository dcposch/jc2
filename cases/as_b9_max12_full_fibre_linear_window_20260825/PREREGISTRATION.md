# Preregistration — B9 full affine linear window through `3^10`

Date: 2026-08-25

Anchor at the literal B9 modulo-243 map `(P5,Q5)` and write

```text
F = (P5,Q5) + 243*T.
```

The exact determinant identity is

```text
det J(F)-1 = D5 + 243*A*T + 243^2*det J(T).
```

Since `243^2=3^10`, the complete solution families modulo `3^(5+k)` for
`1<=k<=5` are exactly the linear congruence families

```text
D5/243 + A*T = 0 mod 3^k.
```

Compute them by exact successive Bocksteins, never point enumeration.  Retain
all 182 coefficient variables and all 276 determinant rows.  At each stage
emit rank, total affine kernel dimension, projection dimension to the prior
family, a literal integer witness, and the selected-particular lift control.

The quadratic term is zero modulo `3^10`; it first enters the divided carry
when attempting to lift a modulo-`3^10` family to modulo `3^11`.  No linear
claim is allowed at that transition.

Success proves finite-depth fixed-D12 families only, not an inverse limit,
characteristic-zero map, counterexample, maximum-twelve theorem, or JC2.
