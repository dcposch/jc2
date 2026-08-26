# Erratum to the 04:51Z synthesis: order-one `r7` degree downstairs

Date: 2026-08-26 05:00Z

Corrects:

```text
e16c128c2caf07afbebdbaa02095c7f7e309015392344a26bd77fc694ab07e60
  xmodel/ideation-20260826T0451Z-synthesis.md
```

Status: **STRATEGY CORRECTION; NO ORDER-ONE COMPONENT HAS YET BEEN
PROMOTED.**

The synthesis correctly quoted the reviewed terminal source formula

```text
r7=lambda+gamma*(x-a)^(1-U)
```

on the source `P1_x`, and therefore correctly has

```text
div_P1(r7-lambda)=(U-1)(infinity-a).                 (1)
```

It then overstated the multiplicities after passing to the normalization
`X` of a coefficient-curve component.  If the source map

```text
pi:P1_x -> X
```

has degree `n` and `R in k(X)` pulls back to `r7`, the correct necessary
form is

```text
div_X(R-lambda)=d*(Q0-Qinfinity),     d*n=U-1.       (2)
```

The equality `d=U-1` is licensed only when `pi` is birational (`n=1`).
Equation (2), not the stronger claim, follows by pulling the downstairs
divisor back through the finite dominant source map; the unique source zero
and pole force total ramification over the corresponding two places.

The unconditional component falsifiers stated in the strategy survive in
the corrected form:

- `X` must have genus zero;
- for some `lambda`, `R-lambda` has exactly one zero place and one pole
  place, with equal multiplicity `d`;
- equivalently after choosing a rational coordinate on `X`,
  `R=lambda+delta*t^d`; hence `R` has at most two branch values (with the
  degree-one exception unramified);
- the source degree must satisfy the divisibility constraint `d*n=U-1`.

Thus two pole places, two zero places for every `lambda`, positive
normalization genus, more than two branch values, or failure of the degree
divisibility kills the component.  A component that passes these tests must
still be lifted through the six tail equations, terminal core, original
Taylor boundaries, and source map.  No order-one, `(8,12)`, maximum-twelve,
or JC2 conclusion follows.

The exact producer formulation that caught this issue is

```text
bbd744fa0c3875f11d5f0038dbbdea461e2656c6a9eb98d2b9050c1eae31712a
  xmodel/max12-812-order1-terminal-r7-pure-power-component-criterion-20260826.md
```

and remains producer-tier pending its own hostile review.
