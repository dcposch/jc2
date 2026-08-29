# Independent audit: delayed-load source exclusion of the affine-Faber `A` cubic

Date: 2026-08-26

Target:

```text
9419c08b4be09fee8ecae9b73c8c9c610770a7166e17a973251312d28b69a695
  xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-20260826.md
```

Verdict: **REPAIR.**  The delayed-load timing, the first-normal UFD split,
the repeated-root null vector, and the displayed normalized cubic
elimination are correct.  The source exclusion skips admissible higher
square-normal correction jets.  The first proposed post-null pole is itself
cancellable by such a jet.  Consequently the normalized `A5` residual is
not yet a correction-complete total-source obstruction.

No CAS, modular inference, or local substantive computation was used.  This
is an exact characteristic-zero hand audit.  The charged producer was not
edited.

## 1. Confirmed algebra

### 1.1 Delayed-load timing

The literal source loads

```text
k10=Lambda^12*K10,
k6 =Lambda^8 *K6,
k2 =Lambda^4 *K2                              (1.1)
```

all enter the ordinary source at `Lambda^14`.  At literal `C=Q^2`, the
unloaded `F12` tail vanishes and the grade-fourteen face is exactly the
ordinary affine-Faber system with only the `mu2` target present.  The
`mu4`, `mu6`, and `J` targets occur at relative grades two, four, and five.

For a nonzero normalized cubic `R7=t^3*j3+...` to meet a unit source `J`,
one must have

```text
3*v(t)=5*v(Lambda).                              (1.2)
```

The primitive integral refinement

```text
Lambda=sigma^3,              t=sigma^5             (1.3)
```

is therefore correct.  The central loaded face is at `sigma^42` and the
unit-`J` terminal tie is at `sigma^57`.

### 1.2 First-normal UFD split

For

```text
Q0=z^4+p*z^2+r,        D=(p^2-4*r)/4 != 0,
deg(N)<=3,                                             (1.4)
```

the reviewed predecessor is

```text
the first seven tails of (3/8)*N^2/Q0 vanish
  iff Q0 divides N^2.                                 (1.5)
```

On `D(r)`, the discriminant of `Q0` is a nonzero scalar times `r*D^2`, so
`Q0` is squarefree.  Hence (1.5) forces `N=0`.

On `r=0`, `D=p^2/4` makes `p` a unit and

```text
Q0=z^2*(z^2+p),          D_Q0=z*(z^2+p).             (1.6)
```

Thus a degree-at-most-two normal vanishes, while the cubic null module is

```text
N=v*z*(z^2+p).                                     (1.7)
```

In the target's coordinates this is exactly

```text
u=(p/2)*v.                                         (1.8)
```

### 1.3 Normalized cubic forms

On `D(r)`, setting the leading normal coordinates to zero, `A1=0` gives

```text
g=(5/16)*x^2*p+(3/2)*b*D,
```

and substitution in `A3` leaves

```text
A3=(5/128)*x^3*D.
```

This algebra is correct.

On `r=0`, impose (1.8), `D=p^2/4`, and `e0=e2=0`.  Direct substitution in
the four charged forms gives

```text
v=-x^3/(5*p^2),
g=45*x^2*p/128+3*b*p^2/8,                           (1.9)
```

and then

```text
A5=5*x^3*p^3/1024.                                 (1.10)
```

All `b` terms cancel.  Thus (1.10) is a correct identity in the normalized
no-further-correction cubic initial form.  It is not yet a source
obstruction because the source reaches many correction grades before
`sigma^57`.

## 2. Smallest missing correction

The repeated-root null direction (1.7) makes the leading quadratic
receiver polynomial:

```text
N3=v*z*(z^2+p),
N3^2/Q0=v^2*(z^2+p).                               (2.1)
```

However, a source arc is not required to stop at this leading normal.  In
the `k[[t]]` subfamily alone, before allowing arbitrary intermediate
`sigma` powers, write

```text
Q(t)=Q0+t*x*z+O(t^2),
E(t)=t^3*N3+t^4*N4+O(t^5),
N4=m3*z^3+m2*z^2+m1*z+m0.                          (2.2)
```

The coefficient of `t^7` in the first unloaded negative receiver is

```text
(3/8)*[
  2*N3*N4/Q0 - N3^2*(x*z)/Q0^2
]_-.                                               (2.3)
```

Using (1.6)--(1.7),

```text
N3*N4/Q0 = v*N4/z,
N3^2*(x*z)/Q0^2 = v^2*x/z.                         (2.4)
```

Only the constant coefficient `m0` of `N4` contributes a negative term.
Therefore the raw and ordinary first row at `t^7` is

```text
R1[t^7]=(3/4)*v*m0-(3/8)*v^2*x.                    (2.5)
```

The parity-allowed choice

```text
m0=v*x/2                                           (2.6)
```

cancels (2.5) exactly.  In the normalized notation it is simply a higher
even jet

```text
n0=t^2*e0(t),             e0(t)=t^2*m0+... .       (2.7)
```

The leading equation `e0=0` in the target removes only the coefficient of
`t^2`; it does not remove (2.7).  Indeed the independent normalized IFT
producer itself exhibits a nonzero `t^4` coefficient of `n0`, although its
value is governed by the normalized, not delayed-source, equations.

Consequently the provisional fixed-truncation value

```text
R1[t^7]=-(3/8)*v^2*x
```

is a useful omission control, not an exclusion.  Any compiler which omits
`m0` will print a false early unit on the repeated-root face.

## 3. Why the normalized `A5` cannot yet be imposed

Under (1.3), the correction hierarchy is

```text
leading odd normal t^3:       sigma^15,
next k[[t]] normal t^4:       sigma^20,
central delayed loads:        sigma^42,
unit-J cubic tie:             sigma^57.             (3.1)
```

An arbitrary literal source arc over `k[[sigma]]` has still more possible
normal, square-tangent, and load jets at the powers not divisible by five.
The source equations must be solved sequentially at every grade below
fifty-seven.  Products of intermediate normal jets can tie later unloaded
grades, and normal jets near grade forty-two can tie the loaded correction
rows.  The UFD condition on the **first** normal coefficient does not set
all of these later coefficients to zero.

The charged forms `A1,A3,A5,J3` are the `t^3` initial forms of the
normalized ordinary-Faber system in which the three loads are already at
leading scale.  On the delayed source ray, those forms occur only after the
unloaded predecessor tower and after the grade-forty-two central loaded
face.  Equation (1.10) may be used only after a correction-complete solve
proves that every earlier contribution to the same ordinary row is zero or
has been uniquely eliminated.

Thus the target's implication

```text
quadratic UFD null + normalized A5 unit
  => no literal primitive source cubic
```

is not established.

## 4. Tangent, centre, and deck audit

- A moving exact-square quartic `Q(sigma)` is a legitimate tangent and is
  harmless to the first statement (1.5), because the first normal is
  defined after absorbing that tangent.  Its later jets can nevertheless
  tie the sequential source equations and must be retained.
- The leading odd tangent `c=t*x` is load-bearing in (2.3).  Higher `c`
  jets, and tangential `p,D` jets, cannot be discarded merely because the
  displayed normalized cubic forms are polynomial in the closed-point
  parameters.
- The literal one-parameter `Phi_l` ring is centered: it has `C0,...,C6`
  and no `C7`.  Hence an uncentered moving-centre variable is not an extra
  direction **inside that frozen ring**.  Any import from a global or
  differently centered chart must still print the two-sided centering
  gauge; it cannot assume the absence globally.
- The source parity sends odd coefficient directions to their negatives.
  The correction (2.7) is even and is therefore allowed.  A parity argument
  does not remove it.
- The ramification in (1.3), the square-chart deck if
  `Lambda=sigma0^2` is also used, and the order-two `z -> -z` deck are
  separate actions until an overlap map identifies them.

These omissions do not change identities (1.9)--(1.10); they prevent those
identities from being a complete source ideal at the claimed grade.

## 5. Strongest theorem that survives

The charged target supports the following narrower statements.

1. The delayed-load graph (1.1) gives the literal ordinary affine-Faber
   **central exact-square face** at `Lambda^14`; it is a selected integral
   load ray, not a fan-exhaustion theorem.
2. Before that face, every first square-normal coefficient must satisfy the
   exact UFD condition (1.5).  On `D(r*D)` it vanishes.  On `r=0,D!=0` its
   only possible cubic direction is (1.7).
3. In the normalized cubic initial form with all unprinted higher normal
   and tangent corrections set to zero, the algebraic eliminations
   (1.9)--(1.10) hold.  This is a compiler control, not a literal-source
   exclusion.
4. The particular frozen rational witness

   ```text
   D=1,p=0,x=1,v=-1/20,
   b=g=e0=e2=u=0
   ```

   has squarefree `Q0=z^4-1`.  Its first unloaded quadratic term on the
   minimal unit-`J` ray occurs at `Lambda^10` and gives

   ```text
   R2=3/3200,             R6=3/6400.                (5.1)
   ```

   Since this is the first nonzero normal grade and no load or target is
   present, no later correction can cancel it.  The direct rejection of
   this **specific natural lift** therefore survives exactly.

Statement 4 does not reject other positive-valuation `J` rays or a forced
total-source branch with different coefficient-normal weights.

## 6. Smallest repair

There are two honest repairs.

### 6.1 Wording-only repair

Downgrade the target to

```text
NORMALIZED NO-FURTHER-CORRECTION CUBIC INITIAL-FORM EXCLUSION.
```

State explicitly that every unprinted higher coefficient-normal,
quartic-tangent, load, and target jet is zero.  Retain (1.10) only as an
initial-form/negative-control identity.  This has no total-source
exclusion consequence.

### 6.2 Source theorem repair

Build the complete delayed-load predecessor through `sigma^57` from the
frozen `Phi_l` rows.  At every grade:

1. retain all four square-normal corrections and all moving `Q`, load, and
   target jets that can tie;
2. preserve the raw predecessor ideal;
3. use ordinary Faber rows, including the moving connection;
4. solve only printed unit pivots;
5. emit the residual odd rows and `J` row; and
6. stop at a raw localized unit or a frozen survivor.

The coefficient (2.5), together with the cancellation (2.6), is the first
mandatory positive/negative omission pair.  Only after this recursion may
the normalized residual (1.10) be tested against the Schur-reduced source
row.

## 7. Frozen dependencies and scope

```text
9419c08b4be09fee8ecae9b73c8c9c610770a7166e17a973251312d28b69a695
  xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-20260826.md

5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md
1da9974dde45fd73c757eb315d50bc9e8abaa028ebb8d5894ca2ea4b2bd6d2de
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-review-grok-20260826.md

4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d
  xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md
08a5ca51461afb1753b21ee7fcf4bf8ed3719cb6edafb7d2020043ad63ab9efa
  xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-review-grok-20260826.md

40b6d15eb23fc85038182146d8f044dee3d37c7c7e6fc4880e0ac3d223297d5f
  xmodel/max12-812-order2-affine-faber-exceptional-cubic-forms-source-ray-triage-20260826.md

62e0f17d0679f21a00b1e96d36d68399ee93e22f698f8ed96ef01405c1053046
  cases/max12_812_order2_affine_faber_a_ift_lift_20260826/RESULT.md
```

This audit confirms exact displayed algebra and identifies a correction-
completeness gap.  It does not classify the full repeated-root formal
recursion, disprove the normalized `A` arc, exhaust delayed-load rays,
classify the `K` face, impose terminal/Taylor conditions, or close order
two, `(8,12)`, maximum twelve, or JC2.
