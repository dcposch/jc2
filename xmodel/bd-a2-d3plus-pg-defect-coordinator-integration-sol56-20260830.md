# Coordinator integration: degree-three adjoint defect and genus-one gate

Coordinator: Sol 5.6 Ultra  
Date: 2026-08-30 UTC  
Frozen basis: `8ee80df2cc754a896469f78cb24b297932627c7e`  
Lifecycle: **BINDING PROMOTION / FIXED NORMAL PRESENTATION**

## 0. Custody and disposition

The provisional adjoint-defect theorem received a genuinely different-model
Opus 5 hostile review at maximum effort.  The lane exited zero.  Before the
report was read, the coordinator reproduced the receipt's prompt, adapter,
launcher, sandbox-profile, charge-validator, guardrail, composed-prompt,
report, and log hashes.  The raw report was then sealed and banked unchanged.

```text
4eb8fc8ba526441c609448602a122601330ed99db9264d91261ea4cfb810a113
  provisional producer, full file
01daaf7e8e786a3e759c8e1147249476a78376da6c21e68b07d5173ed0978051
  provisional producer body
f11ef6340961d41fdca88c84ded7f825c0868864d291cdf7abfe13cadbabd68c
  provisional producer artifact manifest
4c7ea0172dad0cdf44400ae076f5f2fb4d20a1c0258fee92e004b3ed66c2ace0
  frozen hostile-review prompt
80c8fd45679f56ac64966f0041fe9dce8b112fdbcfd6db66c7c25195cc42c6e8
  sealed Opus hostile review, full file
5e1173c7aab69668bc9b320467753fee0642d353766b78e3a750f3afb9b0ae21
  hostile-review body and raw receipt-bound report
09eae2733a30bf8b14c4f65c2762653a70e0049ab6ed9f95f0bbbd8b9910af88
  immutable schema-v2 run receipt
304da3bcebbc9b17037d1e6a94b04fc5284f90271b170b725459da5756163908
  immutable lane log
```

The review verdict is `CONFIRM_WITH_CORRECTIONS`.  The central cohomological
identity, the Grauert--Riemenschneider defect scheme, and the degree-three
closed-immersion theorem all survive.  This integration incorporates the
real corrections, adjudicates one overly strict review objection, and does
not edit either witness.

The receipt correctly records `charge_basis_status=ABSENT`: neither the
producer nor the review makes an exit-price or occurrence assertion.

## 1. Binding theorem

Let

```text
W=P2 x P1,       A=pr_1^*O_P2(1),       B=pr_2^*O_P1(1),
```

and let `X` be an integral normal hypersurface of class `dA+3B`, `d>=3`, over
`C`.  Assume that `X` receives a dominant rational map from `A2`.  Let
`r:Y->X` be a smooth projective resolution and let `q:X->P1` be the second
projection.  Set

```text
N_d=(d-1)(d-2).
```

Then:

1. `X` is Cohen--Macaulay and Gorenstein,

   ```text
   omega_X=O_X((d-3)A+B),
   H^1(X,O_X)=0,
   h^2(X,O_X)=h^0(X,omega_X)=N_d.
   ```

   More precisely, restriction from the ambient product gives

   ```text
   H^0(X,omega_X)
     = H^0(P2,O_P2(d-3)) tensor H^0(P1,O_P1(1)).       (1.1)
   ```

2. The dominant rational map supplies a generically finite dominant rational
   map `P2 --> Y`.  Thus `H^1(Y,O_Y)=H^2(Y,O_Y)=0`.  The stronger classical
   conclusion that `Y` is rational is valid in characteristic zero, but is
   not needed for the defect-length identity.

3. `R^1r_*O_Y` is a finite-length sheaf supported at singular points and

   ```text
   H^0(X,R^1r_*O_Y) = H^2(X,O_X),
   sum_(p in Sing X) length((R^1r_*O_Y)_p)=N_d.         (1.2)
   ```

   In particular every such `d>=3` surface is singular and has at least one
   nonrational, hence non-Du-Val, singularity.

4. With `Delta=K_Y-r^*K_X`, define the resolution-independent
   Grauert--Riemenschneider ideal and defect scheme by

   ```text
   J_GR=r_*O_Y(Delta) subset O_X,
   r_*omega_Y=J_GR tensor omega_X,
   Z_GR=V(J_GR),
   Q_GR=omega_X/(r_*omega_Y).
   ```

   Then

   ```text
   Q_GR = O_ZGR tensor omega_X
        = (R^1r_*O_Y)^D,                               (1.3)
   length(Z_GR)=N_d,
   H^0(X,omega_X) -> H^0(Z_GR,omega_X|Z_GR)
        is an isomorphism.                             (1.4)
   ```

   Here `D` is local Matlis duality.  Equation (1.3) is a duality, not a
   canonical isomorphism between `Q_GR` and `R^1r_*O_Y`.  It gives equal
   pointwise lengths and annihilators; it does not identify generators,
   socles, or filtrations on the two sides.

5. `q` is surjective and has connected fibres.  Its general fibre is a
   smooth plane curve of degree `d` and genus `N_d/2`.

For `d=3`, `N_3=2`, `omega_X=q^*O_P1(1)`, and (1.1)--(1.4) force

```text
q|Z_GR : Z_GR -> P1
```

to be a closed immersion onto a length-two subscheme.  Equivalently, exactly
one of the following occurs:

- two defect points of local geometric genus one lie in distinct `q`-fibres;
- one point has local geometric genus two and a base parameter acts
  nontrivially on `O_X/J_GR` there.

Additional Du Val singularities can be invisible to `Z_GR`.  The theorem is
about the adjoint-defect scheme, not a census of `Sing(X)`.

## 2. Corrections and adjudication

### 2.1 Surjectivity of the coefficient-base projection

The producer used injectivity of pullback from `P1` without supplying the
needed dominance proof.  For each `t in P1`, the fibre is the zero scheme of
the restricted degree-`d` section on `P2`.  If that section vanished
identically, the integral surface `X` would contain `P2 x {t}` as a
same-dimensional closed irreducible subset and hence would equal it,
contradicting `[X]=dA+3B`.  A nonzero positive-degree homogeneous polynomial
on `P2` has a nonempty zero scheme.  Thus every fibre is a nonempty plane
curve and `q` is surjective.

Plane hypersurfaces in `P2` are connected.  Stein factorization therefore
gives `q_*O_X=O_P1`; generic smoothness gives the asserted smooth general
fibre.  This repairs the proof without adding a new hypothesis.

### 2.2 Local duality is contravariant

The producer's phrase "local duality identifies this length point by point"
is safe only as a length statement.  The exact module statement is (1.3).
All downstream degree-three length and image arguments use only lengths,
annihilators, and the action on `Q_GR`, so they survive.  No general-`d`
consumer may silently transfer a module structure from one side to the other.

### 2.3 The Leray endpoint

The reviewer labels the producer's terminal

```text
H^2(X,O_X) -> H^2(Y,O_Y) -> 0
```

as an unjustified five-term endpoint.  It is not part of the bare five-term
template, but it is nevertheless exact here: `R^1r_*O_Y` has finite support,
so `H^1(X,R^1r_*O_Y)=0`, and `R^2r_*O_Y=0` by fibre dimension.  The Leray
filtration therefore makes `H^2(X,O_X)->H^2(Y,O_Y)` surjective.  In any case
`H^2(Y,O_Y)=0`, so (1.2) does not depend on this endpoint.  This is a
presentation clarification, not wrong mathematics in the producer.

### 2.4 Rationality load path

The compactification wording should be replaced by the clean function-field
argument: `C(Y)=C(X)` embeds in `C(A2)=C(P2)`, and the extension is finite.
Pullback of one-forms and pluricanonical forms along a resolution of the
resulting generically finite rational map already gives `q(Y)=p_g(Y)=0`.
Castelnuovo's rationality conclusion is valid but need not be load-bearing.
The resolution must be chosen projective, as is available here.

### 2.5 The negative control

For a Newton-nondegenerate Brieskorn hypersurface the relevant positive
lattice points satisfy the weak inequality

```text
i/a+j/b+k/c <= 1,
```

not the producer's strict rule in general.  The strict rule is falsified by
`x^3+y^3+z^3`.  For `x^3+y^4+z^5`, however, there is no positive lattice point
on the face and the two solutions remain `(1,1,1)` and `(1,1,2)`.  Thus its
geometric genus is still two, while its good-resolution graph is a
star-shaped rational tree.  The control remains valid after changing `<` to
`<=`; it continues to block any inference from reduced rational-tree topology
to rational singularities.

### 2.6 The right geometric phrasing

Every abstract length-two complex scheme embeds in `P1`.  The content is not
the abstract isomorphism type `Z_GR ~= T`; it is that the *given projection*
`q|Z_GR` is a closed immersion.  This is the form promoted in Section 1.

## 3. A new genus-one handle at degree three

Let `d=3` and put `f=q composed r:Y->P1`.  The general fibre is a smooth plane
cubic, and

```text
f_*O_Y=O_P1,
```

so `f` is a genus-one fibration with connected fibres.  No section has yet
been proved; it is therefore premature to call it an elliptic fibration.

Since `K_X=B`,

```text
K_X^2=0,
K_Y=r^*K_X+Delta,
K_Y^2=Delta^2.
```

The defect has length two, so `Delta` is nonzero.  The exceptional
intersection form is negative definite, hence `Delta^2<0`.  Because `Y` is a
smooth rational surface,

```text
K_Y^2=10-rho(Y),       so       rho(Y)>=11.            (3.1)
```

This is a useful strengthening, but the review's phrase "rational elliptic
surface" is too strong without a section.  The binding conclusion is:

> the resolution is a rational genus-one surface of Picard rank at least
> eleven, before relative minimalization.

This opens a sharper successor than a raw local coefficient search.  Contract
vertical `(-1)`-curves to a relatively minimal genus-one fibration, apply the
canonical bundle formula, and transport the exceptional discrepancy cycle
and the length-two GR quotient through those contractions.  At degree three

```text
K_Y=f^*O_P1(1)+Delta,                                 (3.2)
```

while the canonical bundle formula expresses `K_Y` using the Hodge bundle
and possible multiple fibres.  Equating the two descriptions can constrain
which singular fibres can carry the two adjoint-defect units.  This route
keeps the infinitesimal one-point case visible and may reduce the successor
to a finite fibre-configuration problem.

## 4. Successor and firewalls

The next gate remains `D3-ADJOINT-HORIZONTALITY`, now with two coordinated
tracks:

1. **Global genus-one track.**  Relatively minimalize `f`, write the canonical
   bundle formula with all multiple-fibre terms, and determine how (3.2) and
   the exceptional discrepancy cycle constrain the `q`-values and local
   lengths of `Z_GR`.
2. **Local adjoint track.**  For licensed normal Weierstrass cubic germs,
   compute `J_GR` and the coefficient-base parameter action on
   `Q_GR=omega_X/r_*omega_Y`.  Test both the two-point/distinct-fibre case and
   the one-point/nonzero-nilpotent case.
3. **Bridge track.**  Only after the first two tracks produce exact local and
   global objects, impose the cubic different/discriminant and resolved
   first-leg boundary data.

The following firewalls are binding:

- `q:X->P1` is the coefficient-base genus-one projection.  The cubic
  different and discriminant belong to `pi:X->P2`.  They are not the same
  map, and `pi` need not be finite.
- A contradiction must eliminate both length-two alternatives.  Showing only
  that a single local defect is vertical does not exclude two defects in
  distinct fibres, and excluding two fibres does not kill the infinitesimal
  one-point alternative.
- `Z_GR` points are not branches, places, sheets, ramification primes,
  exceptional components, or discriminant points.
- The theorem assumes one fixed integral normal class-`(d,3)` incidence with
  a dominant first leg.  It supplies no block, finite presentation, basis
  invariance, occurrence theorem, polynomial map, counterexample, or JC2
  conclusion.
- Nonnormal, reducible, nonreduced, fibre-degree-drop, projective-basepoint,
  and vertical-component strata remain outside this gate.
- No quadratic conic-bundle, Du Val, crepancy, `D9`, or `R_pi=2A+B` result is
  imported into degree at least three.

## 5. Campaign disposition

`D3+-ADJOINT-DEFECT` is promoted as a binding conditional theorem in its fixed
normal-presentation scope.  It does not eliminate degree three.  Its new
value is a rigid exact interpolation scheme of length two together with a
rational genus-one resolution of Picard rank at least eleven.  The campaign
should now run the global canonical-bundle calculation and the local
base-parameter calculation in parallel, with background adversarial review
rather than serializing discovery behind it.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11856`.
- Body SHA-256:
  `97bb4dd799de5c8ed00cd49c677675f110663f650fc058f29ea15a0fdf423332`.
- Frozen basis: `8ee80df2cc754a896469f78cb24b297932627c7e`.
