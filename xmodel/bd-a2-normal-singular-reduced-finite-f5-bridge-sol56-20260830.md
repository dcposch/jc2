# Reduced finite normal-quadratic infinity collapses to F5

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (coordinator)  
Frozen basis: `06d8f99967ffb3ce34145d30f1e27e23dd07331b`  
Lifecycle: **SEALED PROVISIONAL PRODUCER / HOSTILE REVIEW REQUIRED**

## 0. Verdict and exact scope

This packet proves a new bridge inside the fixed trace-zero quadratic
presentation.  Let

```text
X subset P2 times P1,                 [X]=2A+3B,
pi:X->P2,                             H=pi^*(L_infinity)~A,
R_X~2A+B
```

be the normal irreducible incidence surface in the charged proper cubic-block
first-leg scope.  Assume that `pi` is finite on a neighbourhood of `H` and
that the bidegree-`(2,3)` curve `H` is reduced.  The surface `X` is allowed to
have isolated Du Val singularities, including singularities in the affine
ramification locus.

Then every survivor of the dominant-`A2` rational-forest gate has infinity
curve of exact type

```text
F5=(0,1)+(1,1)+(1,1),
```

with its whole intersection with the ramification Cartier divisor, of total
length `H.R_X=8`, supported at the unique F5 triple/tangency point.

This is **not** a closure of the reduced projectively finite normal-singular
stratum.  In particular it does not say that the F5 point is singular on
`X`, and it does not move or remove ADE singularities lying on affine
ramification.  Conditional on the F5 point itself being Du Val, the packet
also gives the exact short list of possible local infinity Cartier vectors.

The charged inputs are:

```text
6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08
  rational-forest first-leg integration;
e3dc96f07825ea882edc3d2701e9f0a0357ae863c062ad695d9377a37aa2b761
  reduced bidegree-(2,3) F1--F9 classification integration;
255bd0ba04e1c0a428a18caa70e73bc35895026c5857f629ed855cee79a8f803
  smooth-surface ramification-attachment integration, used only for its
  curve-theoretic F1--F7 critical-point counts and cycle lemma;
17f41e706bcae7556cd99e019263e7fad254201fe51f9a24ed158b2be68560c6
  normal-singular quadratic/D9/crepant-ramification integration;
3846f7e2c861ebf5f399dbc9a729c3f1d35dc28c561891c8883a8a3328a7240f
  connected A/D Cartier semigroups and target-line cap technology.
```

The point of the proof below is to isolate exactly which parts of the smooth
attachment theorem do not use smoothness of the projective incidence.

## 1. Ramification and the infinity critical set survive normal singularities

The normal-singular integration gives an effective Cartier ramification
divisor

```text
R_X in |2A+B|
```

whose reduced support is connected and which contains every singular point
of `X`.  Connectedness uses ampleness of `2A+B` on the normal projective
surface; it does not require `X` to be smooth.  The reduced curve `H` is
connected already as an effective class-`(2,3)` divisor on
`P1 times P1`.

Near a point of `H`, choose target coordinates `(u,v)` with
`L_infinity={u=0}` and an affine fibre coordinate `z`.  Finiteness of `pi`
gives a hypersurface chart

```text
X: f(u,v,z)=0,             H: h(v,z)=f(0,v,z)=0.
```

On the smooth locus the determinant of `d pi` is `f_z`; normality extends
that section across the isolated singular set.  Thus its Cartier divisor is
the same `R_X` and, scheme-theoretically on `H`,

```text
H cap R_X:       h=h_z=0.                              (1.1)
```

No component of reduced `H` is a component of `R_X`.  Indeed, if an
irreducible reduced factor `q` of `h` also divides `h_z`, write `h=q*s` with
`gcd(q,s)=1`.  Reduction modulo `q` gives `q|q_z`.  In characteristic zero
this forces `q_z=0`, so `q=q(v)`.  Such a component is the whole `z`-fibre
over one point of the target infinity line, contradicting finiteness of
`pi` near `H`.

Consequently (1.1) is exactly the intrinsic critical set of the projection

```text
H -> L_infinity,
```

including singular points of `H`.  This calculation is made in the normal
hypersurface local ring and does not assume that the particular point of
`X` is smooth.

Let `W` be a simultaneous resolution of `X` and an embedded resolution of
the reduced boundary obtained by deleting `H`, the reduced ramification
support, and any missed singular/branch locus required by the charged first
leg.  The total transforms of `H` and of `Supp(R_X)` are connected.  The
first-leg theorem says that the complete boundary graph on `W` is a rational
forest.

In a forest, two connected subgraphs cannot have two separated joining
sites.  Equivalently, after contracting the internal tree in each total
transform, two physical incidences give parallel edges; blowups only
subdivide those edges or add pendant vertices.  Shared Du Val exceptional
trunks do not change this: if two distinct points are singular on `X`, the
two exceptional trees are disjoint joining sites.  A common strict carrier
would be the only escape, and the preceding factor argument excludes one
between `H` and `R_X` in the present reduced finite scope.

It follows that (1.1) can have only one physical **support site**.  This does
not assert that the reduced ramification has only one analytic branch there:
distinct ramification carrier primes can form a star at one site, exactly as
in the F5 local-different problem.  What is forced here is that the intrinsic
projection `H->L_infinity` has only one physical critical site.

## 2. The F1--F9 table leaves exactly F5

Apply the promoted reduced class-`(2,3)` rational-tree classification.

* `F8,F9` have no rational-forest refinement.
* `F3,F6` contain a target-vertical `(1,0)` component.  Its inverse image is
  positive-dimensional over a point of `L_infinity`, so these types violate
  the present finiteness hypothesis rather than being eliminated inside it.
* In `F1`, the degree-three normalization map to `L_infinity` has total
  Riemann--Hurwitz ramification four and at most two units at one point.  It
  therefore has at least two normalization-critical points.
* The exact cusp/contact patterns of `F2,F4,F7` likewise have two distinct
  physical projection-critical sites.  These counts are properties of the
  reduced curve and its normalization, not of the ambient surface.
* `F5` has exactly one such site: its unique point where the `(0,1)` branch
  and the two `(1,1)` branches meet, with the latter two tangent to order two.

The first four bullets contradict Section 1 or the hypotheses.  Hence only
`F5` survives.  Since `H.R_X=8` and there is no common component, all eight
intersection units are supported at its unique critical point `p_0`.

Locally the reduced F5 boundary can be put in the charged form

```text
h(v,z)=z(z-v)((1+v)z-v).                              (2.1)
```

It has three smooth analytic branches, pairwise intersection lengths
`1,1,2`, hence

```text
r_p0(H)=3,              delta_p0(H)=4,
delta_p0-r_p0+1=2.                                    (2.2)
```

The conclusion of this section is global but only about infinity.  Other Du
Val singularities may lie on `R_X` away from `H`; they are part of the
resolved first-leg boundary and are not seen by the F1--F9 curve table.

## 3. Conditional Cartier filter when the F5 point is Du Val

Assume now that `p_0` itself is a singular point of `X`.  On its minimal Du
Val resolution write

```text
r^*H=H'+sum_i h_i E_i,          a_i=H'.E_i,
a=C h,                           h_i>0, a_i>=0.        (3.1)
```

Choose a target line `M` through `pi(p_0)` distinct from `L_infinity` and
generic among such lines.  Finiteness excludes a common strict component.
Writing

```text
r^*M=M'+sum_i ell_i E_i,        ell_i>=1,
```

the exact total-transform intersection identity is

```text
3=A.H=M'.H'+ell^t a.                                  (3.2)
```

All terms on the right are nonnegative, so `sum_i a_i<=3`.  Each of the
three analytic branches in (2.1) has a strict transform meeting the
exceptional set with positive total intersection.  Therefore

```text
sum_i a_i=3.                                           (3.3)
```

In fact (3.2) is saturated: every branch meets a smooth point of the
exceptional divisor transversely once, `ell_i=1` on the support of `a`, and
`M'.H'=0` locally.  A branch through an exceptional node or tangent to the
exceptional divisor would already contribute more than one and violate
(3.3).

There is a second exact filter.  Put `Z=sum h_iE_i`.  Crepancy and
orthogonality of the Cartier pullback give

```text
K_Xtilde.E_i=0,
H'.Z=-Z^2,
p_a(H)-p_a(H')=-Z^2/2=h^t C h/2=h^t a/2.              (3.4)
```

The curves `H` and `H'` have the same normalization, irreducible-component
count, and normalization genera.  Applying the normalization genus formula
locally to (3.4) yields

```text
delta_p0(H)
  = h^t a/2 + sum_(q over p0) delta_q(H')
  >= h^t a/2.                                         (3.5)
```

Together with (2.2),

```text
h^t a<=8.                                              (3.6)
```

If equality holds, the minimal surface resolution already separates and
smooths all three strict boundary germs.  If `h^t a=6`, exactly one unit of
curve delta remains upstairs and is removed only by the later embedded
boundary resolution.

## 4. Exhaustive connected local list

Use the promoted connected-type theorem and its standard numbering:

```text
A_r: 1--2--...--r;
D_r: 1--2--...--(r-2), with spin vertices r-1,r at r-2.
```

Apply `sum a=3`, the exact `A/D` Cartier congruences, positivity of
`h=C^{-1}a`, and `h^t a<=8`.  The resulting list, modulo diagram
automorphisms, is:

| type | attachment vector `a` | `h^t a` |
|---|---:|---:|
| `A_r`, `2<=r<=8` | `2e_1+e_(r-1)` and its reversal | `6` |
| `A_r`, `4<=r<=8` | `e_1+e_2+e_(r-2)` and its reversal | `8` |
| `D_4` | `e_1+e_3+e_4` | `6` |
| `D_5` | `e_1+2e_4` (spin reversal equivalent) | `8` |
| `D_6` | `e_1+e_5+e_6` | `8` |

For `r=2`, the first A-row means `3e_1` and its reversal.  For `r=4`,
the second means `e_1+2e_2` and its reversal.  The two global `A_3`
embedding tags (balanced `B_4` and unbalanced `U_3`) have the same local
Cartier row but remain distinct carrier geometries.

For completeness, the A-list follows at once from

```text
sum_i i*a_i=0 mod (r+1),
(C_A^-1)_(ij)=min(i,j)*(r+1-max(i,j))/(r+1).
```

Distributing three units gives the displayed quadratic values six and
eight; every remaining integral distribution has value at least ten.  For
`D_r`, the two exact congruences

```text
a_(r-1)=a_r mod 2,
2*sum_(i<=r-2)i*a_i+(r-2)a_(r-1)+r*a_r=0 mod 4
```

and the promoted inverse formulas give precisely the three displayed rows;
the minimum for `D_r`, `r>=7`, is already ten.  Thus

```text
A1 and D7,D8,D9 are impossible at the singular F5 boundary point. (4.1)
```

This statement is local to `p_0`.  It neither excludes those types at affine
singular points nor says that any displayed row is analytically or globally
realized.

## 5. Exact successor and nonclaims

The reduced projectively finite normal-singular quadratic problem is now
typed as an **F5-decorated global fibre/effectivity problem**:

1. retain every affine ADE tree and its ramification Cartier vector;
2. if `p_0` is smooth, retain the promoted local F5 `3+5` different split;
3. if `p_0` is singular, retain only the rows in Section 4 and resolve the
   remaining `0` or `1` unit of strict-boundary delta;
4. place all trees in the actual ruled fibre forest, with the F5 vertical
   carrier and two section carriers distinguished;
5. decompose `R~2A+B` into effective strict carriers, impose connectedness,
   unit/class-group independence, and the physical forest graph.

This is substantially smaller than an untyped ADE enumeration, but it is not
yet empty.  The smooth global F5 lattice theorem cannot simply be copied:
affine ADE trees change the effective fibre configuration and carrier class
lattice even when `p_0` is smooth.

Outside this packet are nonreduced infinity, nonfinite/projective-basepoint
strata, affine coefficient common zeros, degree drops, existence of a
quadratic trace-zero basis, higher presentation degree, polynomial-map
occurrence, a counterexample, and JC2.  No finite formal row, root signature,
or Cartier vector is asserted to be a map.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12123`.
- Body SHA-256:
  `7b5ab1f2cc6c2419f9325882f080d22d0cf53e55ae4fd250dfd5aafe80f424f7`.
- Frozen basis: `06d8f99967ffb3ce34145d30f1e27e23dd07331b`.
