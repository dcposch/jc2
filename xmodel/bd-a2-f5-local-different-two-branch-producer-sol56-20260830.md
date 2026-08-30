# Quadratic F5 gate: the local different has two branches

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra sublane `/root/f5_local_different`  
Frozen basis: `1c665e1f04ca47fc605484777bcfbb4d4e21c619`  
Lifecycle: **EXACT LOCAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

At the unique triple/contact point of the promoted infinity type

```text
F5=(0,1)+(1,1)+(1,1),
```

the source different of any smooth projectively finite cubic incidence has
exactly two smooth analytic branches, with distinct tangent lines.  Their
intersection multiplicities with the reduced infinity divisor are exactly
`3` and `5`.  In particular the known total

```text
H.R_pi=8
```

cannot be carried by one reduced ramification branch.

Consequently, if the global reduced ramification closure is irreducible,
its normalization has two distinct branches over the connected resolved
infinity tree.  The promoted attachment-cycle lemma then produces a cycle.
Thus the `F5` alternative in the promoted attachment dichotomy also fails
under irreducible reduced ramification.  Within that theorem's declared
scope, every survivor must have reducible reduced ramification support.

This conclusion comes from a complete local-ring calculation.  It is not a
finite-jet survival claim and does not assert an arc, an occurrence, or a
map.

## 1. Frozen inputs and object firewall

The binding inputs on the frozen basis are

```text
e3dc96f07825ea882edc3d2701e9f0a0357ae863c062ad695d9377a37aa2b761
  reduced bidegree-(2,3) rational-forest classification integration

255bd0ba04e1c0a428a18caa70e73bc35895026c5857f629ed855cee79a8f803
  quadratic ramification-attachment integration

410de2f569e2ad5599152fdd9414198f012dbdced7d17c5a51dde0096fe4601e
  intrinsic discriminant and normalization-index integration.
```

Retain the notation of the attachment integration.  Thus `X` is a smooth
quadratic Miranda incidence surface, `pi:X->P2` is finite near the reduced
infinity divisor `H`, and `R_pi` is the Cartier ramification/different
divisor.  The closure of the reduced affine ramification support is
`Rbar`.  These objects remain separate from

```text
the target trace-discriminant divisor,
the reduced target branch locus,
the normalization-index/Fitting divisor, and
the conductor.
```

The proof below computes the source Cartier different and its reduced local
support.  The target discriminant appears only as an independent numerical
check.  No conductor or normalization-index identification is used.

## 2. Exact F5 one-chart normal form

Let `p` be the unique F5 triple point.  Choose a target coordinate `v` on
the infinity line and a fibre coordinate `z`, both vanishing at `p`.  The
`(0,1)` component can be sent to `z=0`.  Each `(1,1)` component is the graph
of a Mobius transformation through `(0,0)`.  Their contact order two says
that the two transformations have the same nonzero first derivative, while
their intersection number two says that they are distinct and have no
further coincidence.  Independent projective changes in `v,z`, followed by
a common scaling, give the exact equations

```text
H_0: z=0,
Q_1: z-v=0,
Q_2: (1+v)z-v=0.
```

Indeed the two graph functions are `v` and `v/(1+v)`.  Hence, up to a local
unit, the entire reduced infinity curve is

```text
h(v,z)=z(z-v)((1+v)z-v).                            (2.1)
```

Let `u=0` be the infinity line in the target surface.  Since the full
incidence equation restricts to (2.1), its completed one-chart equation is

```text
f(u,v,z)=h(v,z)+u*g(u,v,z)=0.                       (2.2)
```

The triple point is singular on `H`, so `h_v(0)=h_z(0)=0`.  Smoothness of
`X` therefore forces

```text
g(0,0,0)=f_u(0,0,0) != 0.                           (2.3)
```

Thus `g` is a unit.  This is the cheapest exact local model: no unspecified
quadratic-incidence coefficient is needed beyond the single open condition
(2.3).  A base-dependent change of fibre coordinate only multiplies the
relative derivative by a unit on `X`, and multiplying (2.2) by a unit does
the same.  Hence the different calculation is coordinate-safe.

## 3. The different is a forced ordinary two-branch germ

By (2.3), the completed local ring of `X` is `C[[v,z]]`; solve (2.2) for

```text
u=U(v,z).
```

The lowest homogeneous part of `h` is

```text
in_3(h)=z(z-v)^2,
```

so (2.2) and the unit `g` give

```text
U in (v,z)^3.                                       (3.1)
```

For the finite hypersurface map to the `(u,v)`-plane, the source different
is cut on `X` by `f_z`.  In the coordinates `(v,z)` its equation is

```text
r(v,z)=f_z(U(v,z),v,z)
      =h_z(v,z)+U(v,z)g_z(U(v,z),v,z).               (3.2)
```

The second term has order at least three.  Directly from (2.1),

```text
in_2(r)=d/dz [z(z-v)^2]
       =3z^2-4vz+v^2
       =(z-v)(3z-v).                                (3.3)
```

The two tangent factors are distinct in characteristic zero.  Formal
Hensel factorization (equivalently the ordinary-node criterion) therefore
shows that `r` has exactly two reduced smooth branches at `p`, transverse
to each other, with tangent lines

```text
D_tan:   z=v,
D_tr:    3z=v.                                      (3.4)
```

In particular the Cartier different is already reduced at this point.  Its
reduced support cannot be one analytic branch with multiplicity eight (or
with any other multiplicity).

## 4. Exact distribution of the eight intersection units

On `X`, the ideal of `H` is generated equivalently by `U` or by `h`, since
`U*g(U,v,z)=-h`.  Modulo this ideal, (3.2) reduces to `h_z`.  Therefore

```text
I_p(H,R_pi)
 =length C[[v,z]]/(h,r)
 =length C[[v,z]]/(h,h_z).                          (4.1)
```

Regard (2.1) as a cubic in `z`.  Its leading coefficient and roots are

```text
1+v;        0, v, v/(1+v).
```

The root-difference formula gives the exact fibre discriminant

```text
disc_z(h)
 =(1+v)^4
   *v^2 *[v/(1+v)]^2 *[v-v/(1+v)]^2
 =v^8.                                               (4.2)
```

Because the leading coefficient is a unit, the resultant-length identity
applied over `C[[v]]` turns (4.2) into

```text
I_p(H,R_pi)=8.                                      (4.3)
```

The two branches in (3.4) divide this length rigidly.  `D_tr`, tangent to
`z=v/3`, is transverse to all three branches of `H`, so

```text
I_p(H,D_tr)=1+1+1=3.                                (4.4)
```

`D_tan` is transverse to `H_0` and tangent to both `Q_1,Q_2`; hence its
three contributions are at least `1,2,2`.  Additivity together with
(4.3)--(4.4) forces equality in both tangential contacts:

```text
I_p(H,D_tan)=1+2+2=5.                               (4.5)
```

Thus the eight units are forced to split as

```text
8=3+5,                                               (4.6)
```

independently of every higher coefficient in `g`.

Equation (4.2) is also the restriction to `u=0` of the target trace
discriminant in this chart, up to a nonzero unit.  This agreement is a norm
check only: it does not identify either source branch in (3.4) with a branch
of the target discriminant, and it says nothing about the index or
conductor.

## 5. Binding consequence if reviewed

The promoted no-boundary-component lemma says neither branch in (3.4) is
contained in `H`; both are closures of affine ramification branches.  There
are exactly two possibilities globally:

1. the two local branches lie on one irreducible `Rbar`; then its
   normalization has two points over `p`, and the promoted attachment-cycle
   lemma creates a cycle with the connected resolved F5 infinity tree;
2. the two local branches lie on distinct global components; then the
   reduced affine ramification support is reducible.

Therefore

```text
F5 + rational-forest full boundary
   => reduced ramification support is reducible.     (5.1)
```

Combining (5.1) with the promoted exclusions of irreducible ramification in
`F1,F2,F4,F7` and the projective-finiteness exclusion of `F3,F6` sharpens
the earlier dichotomy to

```text
smooth projectively finite quadratic survivor
+ reduced squarefree infinity
+ promoted A2 first-leg hypotheses
   => R_red is reducible.                            (5.2)
```

The cheapest next gate is now global rather than local: enumerate effective
splittings of the Cartier class `R_pi=2A+B` for which the two F5 germs of
weights `3` and `5` lie on distinct components, and impose adjunction plus
the promoted component-class injection into `Cl(Y)`.  A finite lattice
enumeration should precede any coefficient elimination.  If a universal
coefficient realization test is later needed, it is heavy/uncertain and
must be packaged for AWS rather than run locally.

## 6. Nonclaims

This packet does not eliminate reducible ramification, prove that an F5
incidence occurs, identify a target-discriminant branch, compute a conductor
or normalization index, or commute normalization with a slice.  It does not
construct a compatible formal arc, a polynomial map, or a counterexample.
It proves no general quadratic/cubic block closure, primitivity theorem, or
JC2 statement.  The campaign consequence (5.2) remains provisional until a
different model independently reviews the local normal form, the Hensel
step, the `3+5` intersection split, and the attachment inference.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9253`.
- Body SHA-256:
  `61931ec73f0b6bd13cfef1d75e9c6c4bdd6d36a2364631b898131f66b19aa897`.
- Frozen basis: `1c665e1f04ca47fc605484777bcfbb4d4e21c619`.
