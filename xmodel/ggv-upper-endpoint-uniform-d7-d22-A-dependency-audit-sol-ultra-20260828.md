# Dependency audit: how much of the D7--D22 cascade depends on `A=X^4-1`?

## Verdict

The characteristic/A-adic obstruction itself is not special to
`X^4-1`.  Conditional on the same normal form

```text
F0=A^4,  F1=A^2,
```

the same characteristic modes, the same F/G weight and X-degree windows,
and a nonconstant squarefree quartic `A`, the D7--D22 field-point argument
goes through over any characteristic-zero field.  In particular, the final
step needs only `A` nonconstant:

```text
D22 in (A),  D22=1  =>  contradiction.
```

What has **not** been proved is the bridge from the authoritative fixed raw
branch-P source, whose leading factor is literally `X^4-1`, to a universal
family with arbitrary quartic `A`.  That is a separate raw-normal-form and
degree-window theorem.

## Uses that require only formal `A`

The fractional-power recurrence and same-row operator

```text
n*A^4*y_n = sum_i (((alpha+1)*i-n)*F_i*y_(n-i)),
L_n(R)=4*(12-n)*A^3*A'*R-8*A^4*R'
```

are identities for an arbitrary polynomial `A`.  All cross-term completions
from F4 through F14, the nine indicial exponents, the linked predecessor-mode
cancellations, and the D18--D22 numerators use only this formal calculus.

The direct divisibilities at D16--D21 also need no special roots or sparse
coefficients of `A`: polynomiality of a Laurent expression forces its
displayed numerator to lie in the stated power of `(A)`.  Killing a scalar
negative mode uses only that a nonzero constant cannot be divisible by a
nonconstant `A`.

At D22, `g22` has minimum A-exponent `-2`; therefore `-L22(g22)` has minimum
A-exponent `1`.  This calculation is independent of `deg A`.  The
contradiction with `D22=1` uses only that `(A)` is a proper ideal.

## Uses of squarefreeness

The alternating early field-radical steps have the form

```text
A*A'*Delta^2 = 0 mod A^2.
```

They first use `gcd(A,A')=1` and then reducedness of `K[X]/(A)` to upgrade
`A | Delta^2` to `A | Delta`.  This occurs at D7/D8 and in the successive
square-defect lifts through D15.  Thus squarefreeness, not the particular
four roots `1,-1,i,-i`, is the essential hypothesis there.  Characteristic
zero supplies the rational recurrence and ensures separability is equivalent
to nonzero discriminant.

The late raw G18--G21 same-row maps remain injective for any nonconstant `A`:
the formal kernel of `L_n` is proportional to
`A^((12-n)/2)`, which is nonpolynomial for `n=18,19,20,21`.  The literal rank
certificates in the frozen packet are nevertheless source-specific checks at
`A=X^4-1`, not yet universal certificates.

## Uses special to `X^4-1`

The following artifacts do not automatically transport:

- every literal 303-variable/513-generator replay, raw slot name, row hash,
  and mutation;
- the explicit evaluations `A(0)=-1`, `A'(0)=0`, and the sparsity
  `A^k=(-1+X^4)^k`, used to print the low-degree C13--C17 compatibility
  formulas;
- the concrete Hermite sign lifts over `Q(i)` and the labels of the roots
  `1,-1,i,-i` in the D16/D17 sign classifier;
- any argument that an omitted low X-degree coefficient stays omitted after
  changing X-coordinates.  Translation is especially dangerous because the
  raw Newton windows are not translation-invariant.

Those special low-window equations and sign labels are not used by the
D18--D22 endpoint ideal containment.  At a hypothetical raw point they are
additional necessary equations, so retaining them cannot create an escape
from the endpoint contradiction.

## Exact missing bridge

A promotable universal theorem needs a parameterized raw compiler over

```text
K[a0,a1,a2,a3, Disc(A)^-1],
A=X^4+a3*X^3+a2*X^2+a1*X+a0
```

(or the corresponding homogeneous binary-quartic chart), together with a
proof of all of the following:

1. the allowed branch-P coordinate changes and localizations put the leading
   data in `F0=A^4, F1=A^2` without changing the endpoint equation except by
   a recorded nonzero unit;
2. the exact D4--D6 integration gives the same `F2,F3` normal form and the
   complete nine-mode schedule before the D7 argument starts;
3. every F4--F14 and G4--G21 coefficient produced/required by the
   characteristic recurrence lies in exactly the claimed X-degree window,
   with omitted lower coefficients retained as equations rather than erased;
4. the raw same-row maps have precisely the needed kernels/ranks over the
   discriminant localization, and there is no raw `G22` receiver;
5. the complete endpoint row is still the polynomial target `D22=u` for an
   explicitly tracked unit `u` (then `(A)` cannot contain `u`).

Until that compiler/bridge is source-replayed, the frozen endpoint packet is
a theorem for the fixed `A=X^4-1` branch-P fixture.  The universal arbitrary-
squarefree-quartic statement is a strongly supported formal generalization,
not yet a raw theorem.
