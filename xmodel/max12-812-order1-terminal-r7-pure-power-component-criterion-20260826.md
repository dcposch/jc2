# `(8,12)` order one: terminal `r7` pure-power component criterion

Date: 2026-08-26

Status: **EXACT NECESSARY THEOREM; TERMINAL ROW ONLY.**

## 0. Frozen parents

```text
a4d7d6a1173b5a0b785aa61a4c80ad5f46e4ea83f1d73103917c425608666633
  xmodel/max12-812-terminal-power-belyi-order1-theorem-20260825.md
e322d508c2af66aebb408b2794bd017b05e96cf9ca67f0fc74be8407406f67e1
  xmodel/max12-812-terminal-power-belyi-order1-review-grok-20260825.md
14f872accdeaaa9120924bfbe187cec6092ef27a64af59c8c24a301efefc65e6
  xmodel/max12-812-order1-fixedload-coefficient-curve-probe-design-20260826.md
```

Work over an algebraically closed characteristic-zero field.  This causes no
loss for the geometric necessary condition below.

## 1. Source-line divisor

On a genuine order-one client with `U>=2`, the reviewed terminal theorem
gives

```text
q=c*(x-a)^U,
r7=lambda+gamma*(x-a)^(1-U),
gamma=j/(8*c*(1-U)) != 0.                              (1.1)
```

Hence, on the projective source line,

```text
div(r7-lambda)=(U-1)*([infinity]-[a]).                 (1.2)
```

Thus `r7-lambda` has one zero and one pole, both of order `U-1`.
Equivalently, after choosing the source coordinate `t=x-a`, the terminal map
is `lambda+gamma*t^{-(U-1)}`.  For `U>2` it has exactly the two branch values
`lambda` and `infinity`; for `U=2` it has degree one and is unramified.

The reviewed theorem also says `U=1` is empty.  The constant-core case
`U=0` has affine-linear `r7` and is separate from (1.1).

## 2. Descent to a coefficient-curve component

Let `Z` be an irreducible projective closure of a fixed-load coefficient-
curve component met by a genuine source, let `X` be its normalization, and
let

```text
phi:P1_x -> X
```

be the extended coefficient map.  Let `R in k(X)` be the coefficient
function whose pullback is the Faber tail `r7`.  The terminal identity
`8*r7'=j/q` makes `R o phi` nonconstant, so both `phi` and `R` are
nonconstant.

Then the following are necessary.

1. `X` has genus zero.
2. There are unique points `Q0,Qinf in X`, an integer `d>=1`, and the same
   scalar `lambda` as in (1.1) such that

   ```text
   div_X(R-lambda)=d*(Q0-Qinf).                        (2.1)
   ```

3. If `n=deg(phi)`, then

   ```text
   d*n=U-1,                                            (2.2)
   ```

   and `phi` is totally ramified above `Q0` and `Qinf`, at `infinity` and
   `a`, respectively.
4. After coordinates on `X` sending `Q0,Qinf` to `0,infinity`,

   ```text
   R=lambda+delta*t^d,       delta!=0.                 (2.3)
   ```

   If `d>1`, the branch-value set of `R` is exactly
   `{lambda,infinity}`; if `d=1`, `R` is an isomorphism.  Likewise `phi` is
   a power map after coordinates.

Proof.  A nonconstant morphism from `P1` to the smooth projective curve `X`
forces `g(X)=0` by Riemann--Hurwitz.  Pull back the zero and pole divisors of
`R-lambda`.  Equation (1.2) has singleton zero support and singleton pole
support, so the corresponding divisors on `X` must each have singleton
support, say orders `d0` and `dinf`.  A principal divisor has degree zero,
so `d0=dinf=d`, proving (2.1).  Each of `Q0,Qinf` has a single preimage under
`phi`; therefore that preimage has ramification index `n`.  Pullback of
(2.1) now gives `d*n=U-1` and total ramification at both points.  Since
`X=P1`, a coordinate with divisor `Q0-Qinf` turns (2.1) into (2.3).
Riemann--Hurwitz shows that the two total-ramification points consume the
entire ramification of `phi`, so it too is conjugate to a power map.

## 3. Birational special case and the important degree firewall

If the source coefficient map is known independently to be birational onto
`Z`, then `n=1` and (2.1) strengthens to

```text
div_X(R-lambda)=(U-1)*(Q0-Qinf).                       (3.1)
```

Without birationality, (3.1) on the coefficient normalization is too
strong: the exact conclusion is (2.1)--(2.2), with `d` a divisor of `U-1`.
The full order `U-1` always holds on the source line by (1.2).

This distinction is essential when consuming a modular plane projection or
a non-birational invariant quotient.

## 4. Cheapest component falsifier

For every exact irreducible component retained by the source equations:

1. normalize its projective closure and graph the actual `R=r7` function;
2. compute the complete pole divisor of `R`, including all points at
   infinity and chart complements;
3. reject the component if the pole divisor has more than one support point;
4. otherwise test whether there is a scalar `lambda` for which the fibre
   `R=lambda` is one point of multiplicity `deg(R)`;
5. equivalently, on a rational parametrization, reject if `R` has more than
   two branch values (with the degree-one exception stated above).

Only a surviving component needs a later genus or full Taylor/Rees test.  If
its source-map degree `n` is known, also require `deg(R)*n=U-1`.

## 5. Firewall

This is a consequence only of the reviewed terminal equation.  It does not
show that a sampled modular component lifts to characteristic zero, that the
plane projection is birational, that every source component was retained,
or that a source map has degree one.  It does not impose the first six Faber
tails beyond the fixed-load coefficient equations, either original Taylor
boundary, polynomiality, strict Rees closure, order-one emptiness, `(8,12)`,
maximum twelve, or JC2.
