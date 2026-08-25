# Max12 `(9,12)` selected-Q8 terminal Belyi classification

Date: 2026-08-24  
Status: **producer-exact; hostile different-model review required**

## 1. Theorem and strict application scope

Consider an actual trajectory on the selected corrected-Q8, `k=mu=0`,
`nu!=0` branch.  The frozen root-free terminal descent gives

```text
nu^10*h^3*(Z')^9=j^9*Z^8,                 (1.1)
```

with `h in C[x]`, `Z in C(x)`, and `nu,j in C^*`.  In the nontrivial
order-three Kummer branch, `3|deg(h)` and `h` is not a cube in `C(x)`.

Every rational solution of (1.1) has

```text
Z=T^3,
h=C*T^2/(T')^3                            (1.2)
```

for a nonconstant `T in C(x)` and `C in C^*`.  Writing a reduced fraction

```text
T=A/B,       gcd(A,B)=1,       W=A'*B-A*B',             (1.3)
```

equation (1.2) is

```text
h=C*A^2*B^4/W^3.                           (1.4)
```

Polynomiality of `h` forces all finite critical points of `T` to lie over
`0` or `infinity`.  The hypotheses `3|deg(h)` and `h` noncube eliminate both
unequal-degree boundary strata.  Consequently

```text
deg(A)=deg(B)=D,                            (1.5)
```

and `T` is a three-value Belyi map with the passport described in Section 4.

This is an exact necessary classification of any actual selected-Q8
trajectory.  It does **not** prove that a passport is realized by the
seven-row coefficient fibre, satisfies either Taylor family, or solves the
Jacobian problem.  No selected-Q8 trajectory is excluded merely by this
report; the cyclic `D=1,2` rows are explicit terminal positive controls.

## 2. Divisor cube and rational reconstruction

Let `a` be a finite point and put

```text
m=ord_a(h)>=0,       z=ord_a(Z).
```

If `z!=0`, characteristic zero gives `ord_a(Z')=z-1`.  Taking the valuation
of (1.1) yields

```text
3*m+9*(z-1)=8*z,
z=9-3*m.                                      (2.1)
```

Thus `3|z`.  If `z=0`, then `Z` is a unit and `ord_a(Z')>=0`; (1.1) forces
`m=ord_a(Z')=0`.  Hence every finite coefficient of `div(Z)` is divisible by
three.  The degree-zero divisor identity gives the same conclusion at
infinity.  Since `C` is algebraically closed,

```text
Z=T^3 in C(x).                                (2.2)
```

Substitute (2.2) into (1.1) and cancel `T^18`:

```text
h^3*(T')^9=constant*T^6.
```

The cube of `h*(T')^3/T^2` is constant.  The constant field of `C(x)` is
`C`, so this quotient is constant, proving (1.2).  Formula (1.4) follows
from `T'=W/B^2`.  Conversely (1.2), with a suitable nonzero scalar, gives

```text
h^3*(Z')^9/Z^8=3^9,
```

so the classification loses no rational solution of the terminal equation.

## 3. Exact finite polynomiality and coprimality conditions

Factor over `C`:

```text
A=A0*product_i (x-a_i)^alpha_i,
B=B0*product_j (x-b_j)^beta_j,
```

where `a_i!=b_j`, `alpha_i,beta_j>=1`, and let `r,s` be the numbers of
distinct roots of `A,B`.  Coprimality in (1.3) is essential.

At an `A`-root of multiplicity `alpha`, the two terms defining `W` have
orders `alpha-1` and at least `alpha`, so

```text
ord(W)=alpha-1,       ord(h)=3-alpha.          (3.1)
```

At a `B`-root of multiplicity `beta`, the corresponding orders are at least
`beta` and `beta-1`, hence

```text
ord(W)=beta-1,        ord(h)=beta+3.            (3.2)
```

At a finite point away from `A*B`, a zero of `W` would give a pole of order
a positive multiple of three in (1.4).  Therefore `h` is a polynomial if
and only if

```text
support_finite(W) subset support(A*B),
alpha_i<=3 for every i.                        (3.3)
```

There is no further finite restriction on the `beta_j`.  Under (3.3),

```text
W=constant*product_i (x-a_i)^(alpha_i-1)
          *product_j (x-b_j)^(beta_j-1).        (3.4)
```

The cube class is also explicit:

```text
[h]=[T^2] in C(x)^*/C(x)^{*3}.                  (3.5)
```

Thus the order-three branch is nontrivial exactly when `T` is not a cube.

## 4. Infinity strata and Belyi passport

Put `a=deg(A)` and `b=deg(B)`.

### 4.1 Unequal degrees

If `a!=b`, the leading Wronskian coefficient does not cancel:

```text
deg(W)=a+b-1.
```

Comparing with (3.4), whose degree is `a+b-r-s`, gives

```text
r+s=1.                                          (4.1)
```

Therefore exactly one of `A,B` is constant and the other is a pure power of
one linear polynomial.

- If `a>b`, then `B` is constant,
  `T=C*(x-a0)^D`, `D<=3`, and `deg(h)=3-D`.  The condition
  `3|deg(h)` leaves only `D=3`, for which `h` is constant and hence a cube.
- If `b>a`, then `A` is constant,
  `T=C/(x-b0)^D`, and `deg(h)=D+3`.  The condition `3|deg(h)` forces
  `3|D`, so the sole multiplicity `D+3` is divisible by three and `h` is a
  cube.

Hence the unequal-degree strata are empty at the exact noncube,
`3|deg(h)` selected-Q8 scope.  They are not empty for the terminal equation
without those two Kummer hypotheses.

### 4.2 Balanced degrees

Now let `a=b=D` and set

```text
lambda=T(infinity) in C^*,
e=ord_infinity(T-lambda),       1<=e<=D.         (4.2)
```

Using the local parameter `s_infinity=1/x`, differentiation raises the
infinity order by one, so

```text
deg(W)=2D-e-1.                                  (4.3)
```

Comparison with (3.4) gives

```text
r+s=e+1,         deg(h)=3*(e+1)=3*(r+s).         (4.4)
```

The complete ramification data of `T:P1_x -> P1_T` are

```text
over 0:          (alpha_1,...,alpha_r),  each alpha_i<=3,
over infinity:   (beta_1,...,beta_s),
over lambda:     (e,1^(D-e)).                    (4.5)
```

There are no further ramification points by (3.3).  Indeed

```text
sum(alpha_i-1)+sum(beta_j-1)+(e-1)
  =(D-r)+(D-s)+(e-1)
  =2D-2,                                          (4.6)
```

which is the full Riemann--Hurwitz total.  After scaling `lambda` to `1`,
this is a three-point Belyi passport.  The passport is a necessary target
for an actual trajectory, not evidence that the coefficient fibre realizes
it.

When `e=1`, (4.4) gives `r=s=1`, so

```text
T=C*((x-a0)/(x-b0))^D,       D<=3,
h=C0*(x-a0)^(3-D)*(x-b0)^(D+3).                   (4.7)
```

The rows `D=1,2` are noncube terminal positive controls with multiplicities
`(2,4)` and `(1,5)`; `D=3` has multiplicities `(0,6)` and is a cube.  These
controls prevent promoting the terminal classification to an exclusion.

## 5. What remains charged

For each passport (4.5), an actual selected-Q8 trajectory must still:

1. lift `Z=T^3` through the exact global Q8 quotient relation;
2. reconstruct `n,q,theta,tau,Delta` and the scale `p` with fixed `nu`;
3. satisfy all six high rows and the original terminal row, not merely its
   ninth-power consequence;
4. satisfy both complete Taylor polynomiality families at `r=A_source/9`;
5. retain coprimality and every removed projective boundary.

Thus the smallest honest successor is a reduced-Nielsen/passport test against
the selected quotient's projective boundary, beginning with the positive
`(2,4)` and `(1,5)` cyclic rows as mandatory controls.  No trajectory or
degree cell is closed here.

## 6. Replay

```sh
python3 cases/max12_912_order3_terminal_belyi_classification_20260824/replay.py \
  | diff -u cases/max12_912_order3_terminal_belyi_classification_20260824/replay.json -
shasum -a 256 -c \
  cases/max12_912_order3_terminal_belyi_classification_20260824/MANIFEST.sha256
```

The portable replay checks (2.1), the reconstruction identity (1.4), all
three cyclic controls, both unequal-degree power families, and the balanced
Riemann--Hurwitz arithmetic.  It is proof support; the divisor argument above
is the theorem.

The replay was executed off-host on AWS `r6d` with return code `0` from the
immutable source

```text
source SHA256 =495844f1d51c0f230223d143f36b54679865244581fb60974c268da4c756a4bb,
stdout SHA256=4697899b8ba8e4780db56a7318911e4e463d9f0db4cea00392098a4f530c894e,
stderr SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
```

The remote evidence directory is
`/home/ubuntu/q8_terminal_belyi_20260824/`.  The frozen `replay.json` has the
exact stdout hash above.
