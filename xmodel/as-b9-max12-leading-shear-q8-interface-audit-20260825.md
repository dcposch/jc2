# B9 exact leading shear and the `(9,12)`/selected-Q8 interface

Status: **EXACT ALGEBRAIC ROUTING / `SCOPE-CONFLICT` AT THE KUMMER-LEAF
INTERFACE**.

## 1. Integral total-degree shear

Let `O` be the valuation ring of a finite extension of `Q_3`, and suppose a
coefficientwise compatible all-depth B9 branch actually algebraizes to an
exact fixed-D12 Keller pair

```text
P,Q in O[x,y],                    det J(P,Q)=1,
(P,Q) mod 3 = (u-u^3,y+u^4),     u=x+y^3.
```

This is a conditional statement about an exact lift.  A finite congruence
solution alone does not satisfy its hypothesis.

The degree-twelve homogeneous face `Q12` is primitive: its `y^12`
coefficient reduces to one.  If `P` also has total degree twelve, the top
degree-22 row of the original, denominator-free determinant equation is

```text
J(P12,Q12)=0.                                           (1)
```

For homogeneous binary forms of the same positive degree in characteristic
zero, (1) makes `P12/Q12` constant.  Thus there is a unique `c in Frac(O)`
with

```text
P12=c Q12.                                              (2)
```

Choose the unit `y^12` coefficient of `Q12`.  Every coefficient of `P12`
is divisible by three because the B9 first coordinate has total degree nine
after reduction.  Equation (2) therefore gives

```text
c in 3 O.                                               (3)
```

The integral target shear

```text
(P,Q) |-> (P-cQ,Q)                                     (4)
```

removes the full degree-twelve face of `P`, preserves the determinant, and
is the identity modulo three.  Being an invertible target operation, it also
preserves any actual injectivity or noninjectivity property already known.
The current B9 evidence supplies only a special-fibre collision, not an
actual characteristic-zero collision.

After (4), the first coordinate has total degree at most eleven and retains
its unit `y^9` coefficient modulo three.  Hence its actual partial `y`-degree
is at least nine.  Conditional on a nonautomorphic exact lift, the reviewed
maximum-twelve degree routing removes partial degrees ten and eleven; the
only primitive open degree cell compatible with the unit `y^9` coefficient
is `(9,12)`.  This is a genuine broad-cell landing, but it does not select a
Kummer leaf.

## 2. Exact order-one/order-three ambiguity

The reviewed `(9,12)` high-row routing writes the leading `y` coefficients,
after harmless constant scalings, as

```text
a9=h^3,                  b12=h^4,
```

and splits according to the class of `h` in
`K^*/K^{*3}`, `K=Frac(O)(x)`.  The B9 reduction gives only

```text
h mod 3 = -1,            a9 mod 3=-1,          b12 mod 3=1.    (5)
```

At the wild prime three, (5) does not determine whether `h` is a cube.  The
following two residual-degree-three controls have identical reduction:

```text
h_one   = -(1+3x)^3       = (-(1+3x))^3,        order one;
h_three = -(1+3x^3),                                order three.
```

The second polynomial has three simple zeros over an algebraic closure, so
its divisor is not divisible by three and it is not a cube in `K`.  Both have
`deg_x h=3` and reduce to `-1`, so even the reviewed residual condition
`3 | deg_x h` does not separate them.  Their pairs `(h^3,h^4)` both reduce
to the B9 leading pair `(-1,1)`.

Therefore the integral shear proves neither an order-one landing nor an
order-three landing.  The Kummer class is new 3-adic information in the
first nonconstant coefficients of `h`, not a property of the B9 residue
seed.

## 3. Why the selected-Q8 chart is not a source-honest landing

The selected-Q8 source is the strict characteristic-zero approximate-cubic
chart

```text
K=z^3+z+q,                 p=1,
k=mu=0,                    nu!=0,
```

together with six divided rows

```text
r1/t, r3/t, r5/t, r7/t, r2, r4
```

and the stated localization factors.  Its compiler explicitly sets
`p=a7/3=1`; the reviewed selected-contact theorem refuses the order-one core
and all other `(9,12)` leaves.

The B9 special leading core is the monomial cubic `y^3`.  In approximate-
cubic coordinates it lies at

```text
p=0, q=0,                 disc(K)=0,             (6)
```

not in the `p=1` open.  Under `z=lambda Z`, normalizing a nonzero `p` to one
requires `lambda^2=p` and divides the remaining coefficients by powers of
`lambda`.  When `p` has positive 3-adic valuation, this is a ramified,
non-integral coordinate change; when `p=0`, it is impossible.  Thus an
algebraic-closure normalization to `p=1` is not an integral horizontal map
from the B9 coefficient scheme.

This failure cannot be repaired by substituting into the divided Q8 rows.
The source-honest denominator-cleared rows are

```text
r1,r3,r5,r7,r2,r4.
```

Restoring them multiplies each odd divided row by the parity parameter `t`.
On the degenerate boundary used to form the quotient, those products acquire
vertical components; they do not imply the divided equations at `t=0`.
Likewise, clearing the powers of `3`, the Kummer root, and the source scaling
which are units in characteristic zero but not at the prime three creates a
special fibre larger than the selected `p=1` source.  No existing source
identity or horizontal saturation identifies that larger boundary with the
selected-Q8 six-row scheme.

There are further independent missing equalities: B9 reduction does not
force the characteristic-zero Faber constant `k` to be exactly zero, does
not force `mu=0` or `nu!=0`, and does not reconstruct either Taylor boundary
or the terminal row.  Congruence of those quantities modulo three would not
replace exact equality.

## 4. Verdict and smallest bridge

The exact verdict is

```text
integral degree-12 target shear:               PASS;
conditional landing in the broad (9,12) cell: PASS;
order-one Kummer landing:                      NOT DERIVED;
order-three Kummer landing:                    NOT DERIVED;
selected p=1 corrected-Q8 landing:             SCOPE-CONFLICT.
```

The smallest honest successor is not a generic divided substitution.  Build
one denominator-cleared `Z_3` source from the original coefficient rows,
retain the Kummer-class discriminator and the `p=0`/positive-valuation
normal cone, saturate horizontally before reducing modulo three, and then
split:

1. `h in K^{*3}` (order-one polynomial core);
2. `h notin K^{*3}`, `p=0` or `v_3(p)>0` (ramified order-three boundary);
3. the genuinely integral `p`-unit open, where normalization to `p=1` can be
   compared with the selected-Q8 source.

Only the third stratum could feed the existing Q8 ledger, and it requires
exact reconstruction of `k,mu,nu`, the Taylor families, and the original
localizers.  Shared degree numerology and the monomial special fibre are not
a landing theorem.

## 5. Firewall

This note assumes an exact all-depth algebraized D12 lift only to prove the
integral leading shear.  The frozen B9 calculations are finite-depth and do
not supply such a lift.  No actual `Z_3` map, collision, nonautomorphism,
order-one/order-three exclusion, selected-Q8 trajectory, maximum-twelve
theorem, counterexample, or JC2 conclusion is asserted.

