# Normal degree-at-least-three incidence: exact defect and adjoint-image gate

Coordinator: Sol 5.6 Ultra  
Date: 2026-08-30 UTC  
Frozen basis: `54df5b64b5ea8355cd8c13aa790dcf0f703c5bb7`  
Lifecycle: **PROVISIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Scope and verdict

Let

```text
W=P2 times P1,       X subset W,       [X]=dA+3B,       d>=3,
```

where `X` is an integral normal Cartier hypersurface over `C`.  Assume that
`X` receives a dominant rational map from `A2`; in the intended application
this is the promoted first leg of an already-existing proper cubic block, not
an assertion that a block or a counterexample exists.  Let `r:Y->X` be a
resolution.

The cohomological observation from the blind ideation round is correct, but
its most useful form is stronger than a numerical defect identity.

> **Provisional theorem (`D3PLUS-ADJOINT-DEFECT`).**  Put
>
> ```text
> N_d=(d-1)(d-2).
> ```
>
> Then `Y` is rational,
>
> ```text
> H^1(X,O_X)=0,       h^2(X,O_X)=N_d,
> sum_(p in Sing X) length (R^1 r_*O_Y)_p=N_d.        (0.1)
> ```
>
> The Grauert--Riemenschneider trace inclusion defines an ideal
>
> ```text
> r_*omega_Y = J_GR tensor omega_X  subset omega_X,
> Z_GR=V(J_GR).
> ```
>
> It satisfies
>
> ```text
> length(Z_GR)=N_d,
> H^0(X,omega_X) -> H^0(Z_GR,omega_X|Z_GR)
>                         is an isomorphism.           (0.2)
> ```
>
> In the first nonquadratic case `d=3`, projection `q:X->P1` restricts to
> an isomorphism
>
> ```text
> Z_GR  ~=  T subset P1,       length(T)=2.            (0.3)
> ```

Thus a normal singular class-`(3,3)` survivor is not merely required to have
total local geometric genus two.  Its canonical/adjoint defect must move
scheme-theoretically in the coefficient-base direction.  This is a sharp
new discriminator.  It is not yet an exclusion: reduced rational-forest
topology does not by itself see the nonreduced exceptional cycles measured by
`J_GR`.

No web search and no CAS were used.  The charged stable interfaces are:

```text
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  block-descent-structure coordinator integration
6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08
  rational-forest coordinator integration
17f41e706bcae7556cd99e019263e7fad254201fe51f9a24ed158b2be68560c6
  normal quadratic-incidence coordinator integration
34b7c50638509e50c308766db4d21051824740c64afb1188bff88b248d27f1a3
  reviewed smooth one-attachment/discriminant theorem
```

The quadratic report is used only as a checked model for the Leray bridge;
none of its conic, Du Val, `D9`, or fixed-`d=2` conclusions is imported.

## 1. Ambient cohomology

The hypersurface sequence is

```text
0 -> O_W(-d,-3) -> O_W -> O_X -> 0.                  (1.1)
```

For `d>=3`, Kunneth and Serre duality give

```text
H^i(P2,O(-d))=0 for i=0,1,
h^2(P2,O(-d))=h^0(P2,O(d-3))=(d-1)(d-2)/2,

H^0(P1,O(-3))=0,
h^1(P1,O(-3))=2.
```

Consequently the only nonzero cohomology of `O_W(-d,-3)` is in degree
three, and

```text
h^3(W,O_W(-d,-3))=(d-1)(d-2)=N_d.                   (1.2)
```

Since `H^i(W,O_W)=0` for `i>0`, the long exact sequence of (1.1) gives

```text
H^1(X,O_X)=0,       h^2(X,O_X)=N_d.                  (1.3)
```

Equivalently, adjunction gives

```text
omega_X=O_X((d-3)A+B),                               (1.4)
```

and Serre duality gives `h^0(omega_X)=N_d`.

## 2. Rational resolution and the local defect identity

The dominant rational map `A2 --> X` composes on dense opens with the
birational inverse of `r` to give a dominant rational map `P2 --> Y` after
compactification.  Thus the smooth projective surface `Y` is unirational and,
in characteristic zero, rational.  In particular

```text
H^1(Y,O_Y)=H^2(Y,O_Y)=0.                              (2.1)
```

Normality gives `r_*O_Y=O_X`.  A normal surface has finite singular locus,
so `R^1r_*O_Y` has zero-dimensional support and no higher cohomology.  The
Leray five-term sequence is

```text
0 -> H^1(X,O_X) -> H^1(Y,O_Y)
  -> H^0(X,R^1r_*O_Y) -> H^2(X,O_X)
  -> H^2(Y,O_Y) -> 0.
```

Using (1.3) and (2.1) yields

```text
H^0(X,R^1r_*O_Y) ~= H^2(X,O_X),                      (2.2)
```

which proves (0.1).  The summand at `p` is the usual local geometric-genus
module of the normal surface singularity.  Therefore every `d>=3` normal
survivor is singular and has at least one nonrational singularity.  Since `X`
is Gorenstein, a rational singularity would be Du Val, but (0.1) shows that
not all singularities can be rational or Du Val.

For `d=3`, the only length partitions are

```text
2,       or       1+1.                               (2.3)
```

This is a partition of local cohomological lengths, not a partition of
physical branches, exceptional curves, or points of a discriminant.

## 3. The adjoint defect scheme

For a resolution of a normal Gorenstein surface, the trace map gives the
canonical rank-one inclusion

```text
r_*omega_Y subset omega_X.
```

Because `omega_X` is invertible, there is a unique coherent ideal `J_GR`
with

```text
r_*omega_Y=J_GR tensor omega_X.                       (3.1)
```

The quotient

```text
Q_GR=omega_X/(r_*omega_Y)
     =O_ZGR tensor omega_X                            (3.2)
```

has finite support.  Grauert--Riemenschneider vanishing gives
`R^i r_*omega_Y=0` for `i>0`, so

```text
H^i(X,r_*omega_Y)=H^i(Y,omega_Y).
```

Rationality of `Y` and Serre duality kill the latter for `i=0,1`.  Taking
cohomology in

```text
0 -> r_*omega_Y -> omega_X -> Q_GR -> 0
```

therefore yields the isomorphism in (0.2).  Since `Q_GR` is zero-dimensional,

```text
length(Z_GR)=h^0(Q_GR)=h^0(omega_X)=N_d.              (3.3)
```

Local duality identifies this length point by point with the length in
(2.2).  The advantage of (3.1)--(3.3) is geometric: the defect is now an
actual finite adjoint scheme on the incidence surface, and the full canonical
linear system restricts to it with no kernel and no cokernel.

This scheme is not the reduced singular set.  Its support lies in
`Sing(X)`, but its nilpotent structure records precisely the information that
a reduced dual graph or reduced boundary divisor forgets.

## 4. Degree three forces horizontal adjoint defect

Set `d=3`.  Adjunction becomes

```text
omega_X=O_X(B)=q^*O_P1(1),       h^0(omega_X)=2.       (4.1)
```

The two sections are exactly the pullbacks of `H^0(P1,O(1))`: pullback is
injective, and both spaces have dimension two by (1.3)--(1.4).  Combining
(0.2) and (4.1) gives

```text
H^0(P1,O(1)) -> H^0(Z_GR,q^*O(1)|Z_GR)
```

as an isomorphism.

Let `T` be the scheme-theoretic image of the finite map
`q|Z_GR:Z_GR->P1`.  If `length(T)<=1`, a nonzero linear form on `P1` vanishes
on `T`, hence its pullback vanishes on `Z_GR`, contradicting injectivity of
the displayed evaluation map.  Thus `length(T)>=2`.  On the other hand a
scheme-theoretic image has length at most that of its source, and (3.3) gives
`length(Z_GR)=2`.  Hence

```text
length(T)=length(Z_GR)=2.
```

The defining injection `O_T -> (q|Z_GR)_*O_ZGR` is consequently an
isomorphism, proving (0.3).

There are exactly two scheme types:

1. two reduced defect points with distinct `q`-values; or
2. one length-two defect scheme at one physical point, with a base parameter
   acting nontrivially (the image is the double point of `P1`).

In particular, two length-one defects over the same base value are
impossible, and a length-two defect killed by the base maximal ideal is
impossible.  These statements concern `Z_GR`; they do not identify its
points with ramification places, sheets, branches, or normalization points.

## 5. What this does and does not close

The smooth `d>=3` obstruction is recovered as the special case in which
`R^1r_*O_Y=0`: equation (0.1) is then impossible.  More generally, (0.1)
forces singularities to absorb the entire ambient canonical system.

It is unsafe to append "therefore the rational forest is impossible."
Rational-forest controls the reduced SNC support.  Rational trees can support
nonreduced exceptional cycles with positive local geometric genus.  A useful
topology-only negative control is the weighted-homogeneous Brieskorn
singularity

```text
x^3+y^4+z^5=0.
```

Its standard monomial count has exactly the two positive triples below the
Newton face,

```text
1/3+1/4+1/5<1,       1/3+1/4+2/5<1,
```

so its local geometric genus is two, while its good-resolution plumbing is a
star-shaped tree of rational curves.  This is not asserted to occur in a
class-`(3,3)` cubic block; it only falsifies any argument that uses reduced
forest topology alone to infer rational singularities.

Nor does the theorem prove that every proper cubic block admits a finite
degree-`d` presentation, that coefficient degree is basis-invariant, or that
any normal projective closure exists.  It applies after one fixed normal
class-`(d,3)` incidence and the promoted dominant first leg have both been
supplied.  Nonnormal closures, fibre-degree drop, and projective coefficient
basepoints remain separate strata.

## 6. Cheapest decisive successor

The next exact gate is `D3-ADJOINT-HORIZONTALITY`:

1. construct `J_GR` from one normal class-`(3,3)` local Weierstrass cubic and
   express the action of a coefficient-base parameter on
   `omega_X/r_*omega_Y`;
2. test the two cases forced by Section 4: two local-`p_g=1` singularities in
   distinct `q`-fibres, or one local-`p_g=2` singularity on which the base
   parameter has a nonzero nilpotent action;
3. impose the finite-flat cubic different/discriminant and the full resolved
   first-leg boundary, retaining exceptional multiplicities rather than only
   the reduced graph;
4. prove that every licensed defect is vertical, which would contradict
   (0.3), or produce an explicit horizontal local/global control and stop the
   proposed exclusion at its exact missing invariant.

For general `d`, (0.2) says that the length-`N_d` adjoint scheme is an exact
interpolation scheme for `|(d-3)A+B|`.  A determinant/Fitting formulation of
that evaluation map is the natural bridge to `DISC8-INDEX`; another raw
coefficient-degree search is not.

This successor is desk-scale at the local-definition stage.  Any uncertain
elimination or singularity classification must be frozen and run on AWS.
Different-model review is mandatory before promotion or canonical-ledger
integration.

No proof or counterexample to JC2 is claimed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10372`.
- Body SHA-256:
  `01daaf7e8e786a3e759c8e1147249476a78376da6c21e68b07d5173ed0978051`.
- Frozen basis: `54df5b64b5ea8355cd8c13aa790dcf0f703c5bb7`.
