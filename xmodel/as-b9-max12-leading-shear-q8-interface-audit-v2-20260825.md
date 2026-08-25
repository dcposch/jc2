# B9 exact leading shear and the fixed-D12 order-one/max-12 interface — V2

Status: **EXACT CONDITIONAL ROUTING / ORDER-ONE LANDING / SELECTED-Q8
`SCOPE-CONFLICT`**.

This is a nonmutating successor to
`xmodel/as-b9-max12-leading-shear-q8-interface-audit-20260825.md`, SHA-256
`9f7eb4bfd61aa5ecd61a9f53939327c2ec268956e45eac2885d78b82832ce56a`.
The old note is preserved but superseded: its degree-three
`h_one/h_three` controls correctly show ambiguity in the *general*
unbounded-total `(9,12)` cell, but they do not respect the fixed total-D12
support of B9.  They may not be used for the B9 interface.

## 1. Exact hypothesis and firewall

Let `O` be the valuation ring of a finite extension of `Q_3`.  Assume that a
compatible all-depth B9 branch actually algebraizes to an exact fixed-D12
Keller pair

```text
P,Q in O[x,y],                    det J(P,Q)=1,
deg_total(P),deg_total(Q) <= 12,
(P,Q) mod 3 = (u-u^3,y+u^4),     u=x+y^3.
```

This is a conditional statement about an exact lift.  The frozen finite
congruence families do not supply one.

## 2. Equal-degree top face and integral target shear

The degree-twelve homogeneous face `Q12` is primitive: its `y^12`
coefficient reduces to one.  If `P` also has total degree twelve, the
degree-22 row of the original, denominator-free determinant equation is

```text
J(P12,Q12)=0.                                           (2.1)
```

For completeness, write two nonzero degree-12 binary forms as
`P12=y^12*a(x/y)` and `Q12=y^12*b(x/y)`.  Expanding (2.1) gives a nonzero
scalar multiple of `a'b-a b'=0`; hence `a/b` is constant.  Thus

```text
P12=c Q12                                                (2.2)
```

for a unique `c in Frac(O)`.  Taking the ratio of the `y^12` coefficients
shows more: the denominator is a unit, whereas every coefficient of `P12`
is divisible by three because the B9 first coordinate has total degree nine
after reduction.  Therefore

```text
c in 3 O.                                                (2.3)
```

The integral target shear

```text
(P,Q) |-> (P-cQ,Q)                                      (2.4)
```

removes the whole degree-twelve face of `P`, preserves the determinant, is
the identity modulo three, and preserves any actual injectivity or
noninjectivity already known.  The current evidence supplies only a
special-fibre collision, not a characteristic-zero collision.

The displayed producer-exact mod-`3^11=177147` representative is a useful
negative control, not a family verdict.  Its unit `y^12` ratio gives

```text
c = 27702 mod 177147,
```

but the `(x^3 y^9)` coefficient of `P12-cQ12` is

```text
59049 mod 177147 != 0.
```

Hence that particular representative cannot be the reduction of an exact
all-depth map satisfying (2.2).  The complete `3^183` family must be
intersected with (2.2); one failed point does not kill it.

After (2.4), `P` has total degree at most eleven and retains its unit
`y^9` coefficient, while `Q` retains partial `y`-degree twelve.  Conditional
on a nonautomorphic exact lift, the reviewed maximum-12 degree routing removes
the partial-degree-ten and partial-degree-eleven alternatives.  The surviving
broad partial-degree cell is `(9,12)`.  This statement does not yet choose a
Kummer class or the stricter total-degree-`(9,12)` normalized box.

## 3. Fixed total D12 forces Kummer order one

On the reviewed `(9,12)` partial-`y` route, after harmless nonzero constant
scalings, the leading coefficient polynomials satisfy

```text
a9(x)=h(x)^3,                    b12(x)=h(x)^4.          (3.1)
```

But `Q` still has total degree at most twelve.  Therefore its `y^12`
coefficient `b12(x)` has `x`-degree zero and is a nonzero constant.  Equation
(3.1) forces `h(x)` itself to be a nonzero constant.  After the finite scalar
extension already licensed in the Kummer preflight, that constant has a cube
root, so

```text
[h]=1 in k(x)^*/k(x)^{*3}.                              (3.2)
```

Thus every exact fixed-D12 B9 candidate lies on the **order-one
polynomial-core leaf**.  The nontrivial order-three leaf, including the
selected corrected-Q8 source, cannot contain it.  In the history notation
`H=deg_x(h)=0`; the residual divisibility `3|H` still holds, but it does not
make the Kummer class nontrivial.  On this leaf the depression mismatch
`delta` remains weight-unforced.

Exactly the same cap argument applies to fixed-D12 B8:

```text
a8=h^2,                         b12=h^3,
deg_total(Q)<=12  =>  h constant  =>  Kummer order one.
```

Therefore the B8 seed cannot occupy its order-two or order-four Kummer
leaves either.

This partial-`y` conclusion must not be conflated with the separate
top-homogeneous common-power condition.  On the strict total-degree
`(9,12)` stratum one still has

```text
P9=a K^3,                         Q12=b K^4
```

for a homogeneous binary cubic `K`; the analogous B8 condition uses a
homogeneous quartic.  The common cubic/quartic can vary even though the
partial-`y` coefficient `h(x)` is constant.  Fixed-cap Kummer order one does
not solve that total-homogeneous incidence or any lower determinant row.

## 4. Selected corrected-Q8 is an exact scope conflict

The selected corrected-Q8 source is an **order-three** characteristic-zero
chart.  It fixes the approximate cubic

```text
K=z^3+z+q,                      p=1,
k=mu=0,                        nu!=0,
```

and imposes the six quotient rows

```text
r1/t, r3/t, r5/t, r7/t, r2, r4
```

with their stated localizers.  Its reviewed contact theorem explicitly
refuses the order-one core.

The fixed-D12 order-one result (3.2) already prevents a source-honest B9
landing there.  The integral degeneration gives the same conclusion from a
second direction: the B9 monomial leading cubic lies at `p=q=0`, where
normalizing a nonzero `p` to one requires extracting and dividing by a
square root of `p`; at positive 3-adic valuation this is nonintegral, and at
`p=0` it is impossible.

One also cannot repair the interface by substituting B9 into the divided Q8
rows.  The denominator-cleared source rows are

```text
r1,r3,r5,r7,r2,r4.
```

Multiplication by `t` makes the odd quotient rows acquire vertical boundary
components at `t=0`; the products do not imply the divided equations there.
Clearing powers of three, Kummer roots, or source scalings which were units
only in the characteristic-zero normalized chart likewise enlarges the
special fibre.  B9 also does not force the exact Q8 loads
`k=mu=0,nu!=0`, either Taylor family, or the terminal row.

The selected-Q8 verdict is therefore not merely “order unknown”:

```text
integral degree-12 target shear:                     PASS;
conditional broad partial-y (9,12) landing:          PASS;
fixed-D12 Kummer landing:                            ORDER ONE;
selected order-three corrected-Q8 landing:           SCOPE-CONFLICT.
```

## 5. Source-honest successor

The smallest exact successor has two family-level stages.

1. On the complete broad B9 family, add `c` and impose every coefficient of
   `P12-cQ12=0`, solving `c` from the unit `y^12` coefficient.  Only a
   complete incidence result may replace the failed displayed witness.
2. Apply the target shear familywise.  On the strict total-degree-`(9,12)`
   stratum, impose the homogeneous common-cubic equations and compile the
   **order-one polynomial-core** lower system from the original,
   denominator-free determinant rows.  Split the cubic by its three binary
   root-multiplicity types before any large elimination.

For B8, use the same fixed-cap order-one logic with the common homogeneous
quartic, retaining its cross-ratio and multiplicity strata.  No generic
order-three Q8 substitution is a licensed shortcut.

## 6. Refusal scope

This note proves a conditional exact routing theorem only.  It does not show
that the complete B9 leading-face incidence is empty or nonempty, construct
an all-depth `Z_3` point, exclude the order-one core, solve the common cubic,
settle B8, land any Taylor/terminal system, prove maximum twelve, construct a
counterexample, or resolve JC2.

