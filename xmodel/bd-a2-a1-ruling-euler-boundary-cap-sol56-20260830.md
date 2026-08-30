# Producer: `A1` ruling and completion-invariant boundary Euler cap

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, with delegated primary-source audit  
Frozen basis: `28710686d682165f6146f7ce3a86120b7e3bd11e`  
Lifecycle: **SEALED PROVISIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Verdict and exact scope

Let

```text
X subset P2 times P1,       [X]=2A+3B,
H~A,                        R_X~2A+B
```

be a normal irreducible quadratic incidence in the promoted proper cubic-
block first-leg scope.  Put

```text
U=X minus Supp(H+R_X).                                  (0.1)
```

The exact conclusions of this packet are:

1. `U` is a smooth rational affine surface with `O(U)^*=C^*` and
   `bar-kappa(U)=-infinity`.
2. The Miyanishi--Sugie theorem therefore gives a surjective `A1`-fibration
   `U->C` directly on `U`, with no finite base change.  Its base is exactly
   one of `A1` or `P1`; the `P1` branch cannot be discarded.
3. If `r` is total ADE rank and `c` is the number of distinct nonexceptional
   strict components of `Supp(H+R_X)`, then

   ```text
   e(U)=12-r-c,              r+c<=11.                  (0.2)
   ```

   If the `A1`-fibration has base `P1`, then `r+c<=10`.  Equality
   `r+c=11` forces base `A1` and every scheme fibre to have irreducible
   reduced support, although an irreducible fibre may still be multiple.
4. In the reviewed reduced finite F5 scope, `H` and `R_X` have no common
   component, so `c=s+k=3+k`, where `k>=1` counts reduced ramification
   carriers.  Hence

   ```text
   r<=7,                  and r<=6 whenever k>=2.      (0.3)
   ```

The weak rank cap in (0.2) also follows independently from the existing unit
localization/class injection.  The genuinely new structural content is the
`A1`-fibration, its two possible bases, the `P1` sharpening, the equality
case, and a second ruling class after adapting the completion.

This packet does not prove that the ruling class already lives in the current
`D9` marking: resolving its boundary base points can require an unbounded
number of additional boundary blowups.  It also makes no reducedness claim
for the full projective ramification divisor.  Affine Stein-contracted
ramification carriers remain visible through `c`.

The charged internal inputs are:

```text
17f41e706bcae7556cd99e019263e7fad254201fe51f9a24ed158b2be68560c6
  normal-singular quadratic incidence reduction;
6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08
  rational-forest first-leg theorem;
f385387d3f920d4493eb145cc87934aafd3168e1c0f830330426014fd5db7d30
  reduced finite normal-singular F5 integration;
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  proper-block first-leg and missed-ramification integration.
```

## 1. Why the maximal safe open is smooth affine

The sum of the two effective Cartier divisors is

```text
H+R_X~3A+B=O_X(3,1).                                  (1.1)
```

It is the restriction of an ample divisor on `P2 times P1`.  The complement
of the support of an effective ample Cartier divisor on a projective variety
is affine, so (0.1) is affine.  The normal-singular incidence theorem proves
that every singular point of `X` lies in `Supp(R_X)`.  Hence `U` is smooth.

The declared first leg is an actual dominant morphism

```text
g_1:A2 -> U.                                           (1.2)
```

It may miss further points of `U`, but those points are not deleted in
(0.1).  A unit `u in O(U)^*` pulls back to a polynomial unit on `A2`, hence a
scalar.  Dominance of (1.2) then makes `u` the same scalar, proving

```text
O(U)^*=C^*.                                            (1.3)
```

The projective resolution of `X` is rational by the promoted conic-fibration
argument, so `U` is rational.  Logarithmic pluricanonical pullback along
(1.2) gives

```text
bar-kappa(U)=-infinity.                                (1.4)
```

This is the maximal open used below.  Replacing it by the actual first-leg
image or deleting additional missed points changes its Euler characteristic
and is not licensed.

## 2. The external `A1`-ruling theorem and base dichotomy

The source audit used the following primary theorem and two modern
crosschecks:

1. M. Miyanishi and T. Sugie, *Affine surfaces containing cylinderlike open
   sets*, J. Math. Kyoto Univ. **20** (1980), 11--42,
   `doi:10.1215/kjm/1250522319`.
2. A. Dubouloz and T. Kishimoto, *Log-uniruled affine varieties without
   cylinder-like open subsets*, Bull. Soc. Math. France **143** (2015),
   383--401, Section 1.2.2, `doi:10.24033/bsmf.2692`.
3. R. V. Gurjar and M. Miyanishi, *Automorphisms of affine surfaces with
   A1-fibrations*, Michigan Math. J. **53** (2005), especially Lemmas
   2.2--2.3, `doi:10.1307/mmj/1114021083`.

At the exact hypotheses used here, the Miyanishi--Sugie theorem says that a
smooth affine complex surface has negative logarithmic Kodaira dimension if
and only if it is `A1`-ruled.  The cylinder projection extends on the surface
itself to a surjective morphism

```text
rho:U -> C                                               (2.1)
```

onto a smooth curve whose general fibre is `A1`.  The finite base changes
seen in deformation results concern families of surfaces and are not needed
for (2.1).

Because `U` is rational, `C` is rational.  Write `C=P1 minus S`.  When
`S` is nonempty, pullback injects `O(C)^*` into (1.3), while

```text
O(C)^*/C^* ~= Z^(#S-1).
```

Thus `#S<=1`, and the exact dichotomy is

```text
C=A1 or C=P1.                                          (2.2)
```

Neither dominance by `A2` nor constant units removes the complete-base
branch; Section 6 gives an explicit control.

## 3. The adapted second-ruling class

Resolve the boundary base points of the rational extension of (2.1) by point
blowups supported entirely in the boundary.  On a resulting smooth strict
SNC completion `(V,D)`, the fibration extends to a `P1`-fibration.  If `L` is
the class of a general completed fibre, then

```text
L^2=0,        K_V.L=-2,        D.L=1.                  (3.1)
```

More precisely, `L` is primitive, nef, effective, and basepoint-free.  There
is exactly one horizontal boundary component `S_0`, with

```text
L.S_0=1,              L.D_i=0 for D_i!=S_0.            (3.2)
```

If the base in (2.2) is `A1`, the boundary additionally contains a complete
fibre over the missing point of `P1`; its connected intersection matrix has a
primitive positive kernel vector equal to the fibre multiplicity vector.  A
`P1` base forces no complete boundary fibre.

Equations (3.1)--(3.2) are valid on an adapted completion, not automatically
on the current minimal `D9` resolution.  For example, the polynomial ruling
`x+y^n` on `A2` has general closure `nH` in `P2`, with square `n^2`, canonical
intersection `-3n`, and boundary intersection `n`; only boundary base-point
resolution recovers (3.1).  Boundary weak factorization controls the changes
qualitatively, but gives no uniform bound on their number here.

On any fixed adapted completion, (3.1)--(3.2) give a finite lattice test after
choosing the horizontal component: two solutions differ in the lattice
orthogonal to the boundary, which is negative definite when the boundary
supports an ample divisor.  One must still test primitivity, nefness,
effectivity, and semiampleness.  This is a valid successor after an adaptation
bound, not a present elimination on the raw 115 fibre signatures.

## 4. Completion-invariant Euler identity

Let

```text
r = total rank of all Du Val exceptional trees;
c = number of distinct nonexceptional strict components of Supp(H+R_X);
b = number of additional point blowups used to make the boundary strict SNC.
```

On the minimal Du Val resolution, `e=13`.  Every exceptional curve belongs to
the resolved ramification support.  The supports of `H` and `R_X` are
connected and meet, so their full reduced transform is connected.  The
rational-forest theorem makes every component rational and its connected SNC
dual graph a tree.  After the `b` extra boundary blowups,

```text
e(V)=13+b,
N=#components(D)=r+c+b,
e(D)=2N-(N-1)=N+1.
```

Euler additivity therefore cancels every later boundary blowup and gives

```text
e(U)=e(V)-e(D)=12-r-c.                                 (4.1)
```

This formula uses distinct support components.  If `H` and `R_X` shared a
strict carrier, it would be counted once in `c`, not twice.  In the reviewed
reduced finite F5 scope the local `h_z` argument excludes such a component,
so, with `s=#Irr(H)` and `k=#Irr(Supp R_X)`,

```text
c=s+k.                                                 (4.2)
```

No reducedness of the Cartier divisor `R_X` is needed: `k` counts its reduced
support, including any affine carrier contracted by the Stein map.

## 5. Euler of the `A1` fibration and exact caps

The Gurjar--Miyanishi fibre theorem says that the reduced support of every
fibre of (2.1) is a disjoint union of affine lines.  Let `r_t` be its number
of irreducible components at a degenerate value.  Scheme multiplicities do
not change the topological Euler number.  Stratifying the base gives

```text
e(U)=e(C)+sum_t(r_t-1).                                (5.1)
```

All correction terms are nonnegative.  From (2.2), (4.1), and (5.1),

```text
r+c<=11;                                               (5.2)
C=P1  =>  r+c<=10.                                    (5.3)
```

If equality holds in (5.2), then `e(U)=1`; hence `C=A1` and every `r_t=1`.
This excludes reducible reduced fibres of the `A1` ruling, but not a multiple
irreducible fibre.

There is an independent elementary proof of (5.2).  Localization on `(V,D)`
and (1.3) inject the free group on the `N=r+c+b` boundary components into
`Pic(V)`, whose rank is `11+b`.  Thus (5.2) is a consistency theorem rather
than independent double evidence.  Equations (5.3), (5.1), and the equality
classification are the extra output of the `A1` theorem.

For F5, `s=3`; ramification is nonempty, so `k>=1`.  Equations (4.2) and
(5.2) give

```text
r+k<=8,        r<=7,        k>=2 => r<=6.             (5.4)
```

These bounds apply before any local Cartier-vector or carrier-effectivity
enumeration.  They do not say which remaining rank pattern occurs.

## 6. Sharp controls and firewall

The weak bound is numerically sharp: `A2->A1` has Euler number one.  Start
from the `P1 times P1` completion whose boundary is the two coordinate
rulings, and make nine boundary blowups.  This produces `e(V)=13` and eleven
boundary components without changing the open surface.

The complete-base branch is also real.  On the Hirzebruch surface `F_n`, let

```text
S~C_0+mF,             m>n,
```

be a smooth ample section and put `U_0=F_n minus S`.  Then `U_0` is smooth,
rational, and affine; localization gives `O(U_0)^*=C^*`.  Projection to
`P1` has every fibre `A1`, so `e(U_0)=2`.  Over `A1 subset P1` the complement
of the section is an `A1`-bundle, hence is trivial and gives an open
`A2 subset U_0`.  Its inclusion is a dominant etale morphism.  Thus even a
dominant etale `A2` first leg, rationality, and constant units do not force
base `A1`.  This control has generic degree one, so it does not settle a
possible extra proper-block obstruction from `d_1>=2`.

Finally, the numerical shadows `L^2=0`, `K.L=-2`, and `D.L=1` without
primitive/nef/effective/semiample conditions do not produce a fibration.
The packet proves no bounded completion-adaptation theorem, no global
ramification reducedness, no effectivity of a decorated D9 signature, no
finite algebra or etale first leg, no polynomial map, no counterexample, and
no JC2 conclusion.

The cheapest exact successor is to apply (5.4) to the F5-decorated global
fibre rows, split the equality cell into `A1`-base/Ga-action analysis, and in
parallel seek either a bounded adaptation lemma or a block-specific
`d_1>=2` obstruction to the sharp `P1`-base control.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11870`.
- Body SHA-256:
  `3cb1243350658fc146671cf7723b96c65c6836f8852582e72cd0781546df596d`.
- Frozen basis: `28710686d682165f6146f7ce3a86120b7e3bd11e`.
