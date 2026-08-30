# Degree-three Hodge divisor and the four minimal genus-one configurations

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra with sublane `/root/d3_genus_one`  
Frozen basis: `5cc7b50274df491cb09dbb91a8b528de77fc5ef4`  
Lifecycle: **EXACT PROVISIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Verdict

Assume the binding degree-three adjoint-defect theorem for a normal integral
class-`(3,3)` surface

```text
X subset P2 x P1,             q:X->P1,
```

dominated rationally by `A2`.  Let `r:Y->X` be the minimal resolution and
`f=q composed r`.  The coefficient-base genus-one fibration has an exact
Hodge-lattice inclusion

```text
f_*omega_(Y/P1)=O_P1(1)  --s-->  q_*omega_(X/P1)=O_P1(3),       (0.1)
```

and its quadratic vanishing divisor is exactly the already binding
Grauert--Riemenschneider image scheme:

```text
div(s)=T=q(Z_GR) subset P1,             length(T)=2.             (0.2)
```

After contracting vertical `(-1)`-curves to a relatively minimal rational
genus-one surface `g:S->P1`, there are only two global types: a rational
elliptic surface with a section, or an index-three Halphen surface with one
triple fibre and no section.  Combining the canonical bundle formula with
(0.2) leaves exactly four discrepancy configurations:

| type | `T` | pushed discrepancy `D` | section |
|---|---|---|---|
| no multiple fibre | `t1+t2`, `t1!=t2` | `-F_t1-F_t2` | yes |
| no multiple fibre | `2t` | `-2F_t` | yes |
| one triple fibre `F_0=3P_0` | `t0+t1`, `t1!=t0` | `-P_0-F_t1` | no |
| one triple fibre `F_0=3P_0` | `2t0` | `-4P_0` | no |

Thus the global degree-three successor is finite.  The one-point rows require
Hodge colength two at one fibre.  The torsor/minimal-Jacobian Hodge
identification in Section 5, valid also at the nonsoluble triple fibre, then
forces the simultaneous ternary-cubic divisibilities

```text
v(c4)>=8,          v(c6)>=12,          v(Disc)>=24.               (0.3)
```

Discriminant order by itself is not a level test.  The cheapest decisive
successor is a finite invariant/minimisation calculation, stratified by the
central plane-cubic orbit, with normality and generic smoothness imposed.
Section 5 keeps the required integral-Jacobian normalisation theorem explicit.

This report does not prove that any of the four rows is compatible with the
specific class-`(3,3)` polarization, does not construct a polynomial map,
and does not prove JC2.

## 1. Exact Hodge inclusion

The morphism `q` is flat.  Indeed, `X` is Cohen--Macaulay, the base is a
smooth curve, and every fibre is a nonempty one-dimensional plane cubic.
Adjunction gives

```text
omega_X=q^*O_P1(1),
omega_(X/P1)=q^*O_P1(3).                                  (1.1)
```

The fibres are connected and `q_*O_X=O_P1`, hence

```text
q_*omega_(X/P1)=O_P1(3).                                  (1.2)
```

The smooth rational surface `Y` has `chi(O_Y)=1`.  The flat connected
genus-one fibration `f` has `R^1f_*O_Y` locally free of rank one; Leray gives
degree `-1`, and relative duality gives

```text
f_*omega_(Y/P1)=(R^1f_*O_Y)^vee=O_P1(1).                  (1.3)
```

Twisting the GR inclusion `r_*omega_Y subset omega_X` by the base dualizing
bundle and pushing along `q` produces a nonzero map of line bundles (0.1).
Write it as multiplication by

```text
s in H^0(P1,O_P1(2)).                                     (1.4)
```

Put

```text
Q_rel=Q_GR tensor q^*O_P1(2).
```

The beginning of the pushed relative-dualizing exact sequence is

```text
0 -> O(1) -> O(3) -> q_*Q_rel
  -> R^1q_*(r_*omega_Y tensor q^*O_P1(2)).                (1.5)
```

The line-bundle cokernel in (1.5) has length two.  Twisting does not change
finite length or annihilators, and the binding adjoint theorem gives
`length(q_*Q_rel)=length(Q_GR)=2`; hence the injection of that cokernel into
`q_*Q_rel` is an isomorphism.  Since

```text
Q_GR=O_ZGR tensor omega_X
```

and the given map `q|Z_GR` is a closed immersion onto `T`, annihilators in
(1.5) give the scheme-theoretic identity (0.2).  This does not identify
`Q_GR` with `R^1r_*O_Y`; those two finite modules are related by local Matlis
duality, as in the binding theorem.

## 2. Relative minimalisation

### 2.1 Anti-effectivity on the minimal resolution

Put

```text
Delta=K_Y-r^*K_X.
```

For every irreducible exceptional curve `E_i` on the minimal resolution,

```text
Delta.E_i=K_Y.E_i=2p_a(E_i)-2-E_i^2 >= 0.               (2.1)
```

There is no exceptional rational `(-1)`-curve on the minimal resolution.
The exceptional intersection matrix is negative definite with nonnegative
off-diagonal entries, and its inverse has nonpositive entries on each
connected block.  Equation (2.1) therefore gives

```text
Delta<=0.                                                (2.2)
```

Equality holds on a connected block exactly in the Du Val case.  In
particular a nonzero local GR defect has a nonzero negative discrepancy
block.

Factor the contraction of all vertical `(-1)`-curves as

```text
h:Y->S,                 g:S->P1,              f=g composed h,
```

where `g` is relatively minimal.  Set

```text
D=h_*Delta.
```

Then `S` is smooth and rational and `D<=0` is vertical.  After choosing
compatible canonical and fibre divisors, pushing
`K_Y=f^*O(1)+Delta` gives the divisor equality

```text
K_S=F+D,                                                  (2.3)
```

where `F` is a full fibre of `g`.

### 2.2 The multiplicity is one or three

The characteristic-zero canonical bundle formula is

```text
K_S ~ g^*(K_P1+L)+sum_i (m_i-1)P_i,
deg(L)=chi(O_S)=1,        F_i=m_i P_i.                    (2.4)
```

Numerically,

```text
K_S == (-1+sum_i(1-1/m_i))F.                             (2.5)
```

The rational surface `S` has `K_S^2=0` and hence Picard rank ten.  It is not
a minimal rational surface, so it has a `(-1)`-curve.  Relative minimality
makes every such curve horizontal.  For one of them, say `C`, adjunction
gives `K_S.C=-1`; therefore the coefficient in (2.5) is negative.  Two
multiple fibres would already contribute at least one, so there is at most
one.

With no multiple fibre, (2.5) gives `F.C=1`, and `C` is a section.  With one
multiple fibre of multiplicity `m>1`, (2.5) gives `F.C=m`; moreover every
horizontal degree is divisible by `m`, so there is no section.  The pushdown
to `S` of the plane hyperplane divisor has horizontal degree three.  Hence

```text
m divides 3.                                               (2.6)
```

The only cases are consequently:

```text
m=1: a rational elliptic surface with section;
m=3: an index-three Halphen surface, with F_0=3P_0 and no section. (2.7)
```

The word `elliptic` is used only in the first row, where a section has now
been proved.

## 3. Exact four-row discrepancy table

Let `Theta` be a component of a fibre of `g`.  The canonical bundle formula
and (2.3) give

```text
D.Theta=0.                                                 (3.1)
```

The kernel of a fibre's negative-semidefinite intersection matrix is
generated by its primitive fibre cycle.  Thus every nonzero local part is

```text
D_t=-b_t P_t,             b_t a positive integer,          (3.2)
```

where `P_t=F_t` for an ordinary fibre and `F_0=3P_0` at the possible triple
fibre.

The support in (3.2) is exactly the support of `T`.  One direction follows
because a Gorenstein rational surface singularity is Du Val and has zero
minimal discrepancy.  For the converse, use the factorisation formula

```text
Delta=h^*D+K_(Y/S).                                       (3.3)
```

If `D_t=0`, then the local right side of (3.3) is effective, whereas (2.2)
is anti-effective; hence both vanish.  Therefore no GR defect lies over
`t`.  This proves equality of supports without identifying local defect
length with the integer `b_t`.

If `m=1`, (2.3)--(2.4) give

```text
D ~ -2F,             so sum_t b_t=2.                     (3.4)
```

If `m=3`, then `K_S~-P_0`, hence

```text
D ~ -4P_0,
b_0+3 sum_(t!=t0)b_t=4.                                  (3.5)
```

Finally `T` has length two, and every point of its support has positive
local length.  Combining support equality with (3.4)--(3.5) gives exactly
the four rows in Section 0.  In particular the triple-fibre point itself
must carry a defect unit.  The two-support rows have local lengths `1+1`;
the one-support rows have the nonreduced base scheme `Spec C[[t]]/(t^2)`.

Additional Du Val singularities remain invisible and are not excluded.

## 4. Vertical blowups and Picard lower bounds

Write `h` locally as a sequence of blowups.  Starting from `D_0=D`, after a
blowup `pi_j` with exceptional curve `E_j`, formula (3.3) gives

```text
D_j=pi_j^*D_(j-1)+E_j,
coeff_(E_j)(D_j)=1+mult_(p_j)(D_(j-1)).                  (4.1)
```

The final divisor is `Delta<=0`, so every centre has multiplicity at most
`-1`.  A centre of multiplicity `-1` creates a coefficient-zero curve.  Such
a curve can be the non-`r`-exceptional carrier mapping onto the plane-cubic
fibre.  This is why a negative full-fibre term does not imply that `r`
contracts the entire fibre.

For each `t`, the proper map `r:Y_t->X_t` is onto the one-dimensional plane
cubic fibre.  Consequently at least one component of `Y_t` is not
`r`-exceptional and has coefficient zero in `Delta`.  If `D_t=-bP_t`, every
component already present on `S_t` starts with a negative coefficient, so a
zero-coefficient carrier must be created by the blowup chain.  Formula
(4.1), together with the requirement that each centre have multiplicity at
most `-1`, shows inductively that starting from `-bP` requires at least `b`
blowups before such a carrier can appear.  Blowups over distinct fibres are
disjoint and their counts add.  Since a relatively minimal rational
genus-one surface has Picard rank ten, the minimal resolution satisfies

```text
rho(Y)>=12   in the first three rows;
rho(Y)>=14   in the m=3, T=2t0 row.                       (4.2)
```

These are bounds for the minimal resolution.  Arbitrary further blowups
must not be used to manufacture them.

There is no contradiction at the canonical-bundle level alone.  Abstract
rational elliptic and Halphen surfaces can be modified along fibres and
contracted to produce simple-elliptic defect points.  The remaining content
is compatibility with the given plane class-`(3,3)` model.

## 5. Invariant scaling and the finite successor

There is one real no-section issue to settle before applying invariant
weights.  Over the strict henselian DVR at a base point, Liu--Lorenzini--
Raynaud Theorem 3.1 supplies a canonical map

```text
H^1(S_DVR,O_S) -> Lie(Neron(Jac(f_eta)))                 (5.0)
```

which is generically an isomorphism and whose kernel and cokernel have equal
length.  Both modules here are free of rank one: the Neron model is smooth,
and the proper flat connected genus-one family is cohomologically flat in
degree zero and one.  Thus (5.0) is injective, its kernel has length zero,
and the theorem forces its cokernel to have length zero as well.  Dualizing
canonically identifies the resolved-torsor Hodge lattice with the
minimal-Jacobian invariant-differential lattice, including at the nonsoluble
index-three Halphen point.

Now (0.1) identifies that minimal lattice with a sublattice of the plane
model's generic Hodge line.  If a minimal generator `alpha` maps to
`s beta`, where `beta` is a plane generator, equality of the invariant
tensors and their weights gives, over every DVR,

```text
c4_plane=s^4 c4_min,
c6_plane=s^6 c6_min,
Disc_plane=s^12 Disc_min.                                (5.1)
```

Globally `Disc_plane` is a section of `O(36)`, `Disc_min` is a section of
`O(12)`, and `s^12` contributes degree 24.  Thus

```text
36=24+12.                                                 (5.2)
```

This is a Hodge-lattice identity and does not assume that the genus-one
fibration has a section.  Fisher's invariant-weight theorem fixes its
orientation, while Cremona--Fisher--Stoll Lemma 3.2 independently identifies
the discriminant exponent with twelve times the ternary-cubic level even for
an insoluble model.

At a point where `T` has local length `k`, (5.1) forces

```text
v(c4_plane)>=4k,   v(c6_plane)>=6k,
v(Disc_plane)>=12k.                                      (5.3)
```

For the two one-point rows, `k=2`, giving (0.3).  For each point of a
two-support row, `k=1`, giving the `4/6/12` version.

In the `m=3` rows, the scheme-theoretic plane fibre must be a triple line:
all component multiplicities on the resolved fibre are divisible by three,
whereas its plane degree is three.  In local coordinates the finite jet has
the form

```text
F=x^3+tG1+t^2G2+t^3G3.                                  (5.4)
```

Two controls delimit the computation:

1. `x^3+t(y^3+z^3)` is normal, has three `A2` points, and has discriminant
   order eight.  It is not a triple fibre after resolution.
2. `x^3+t y^3+t^2 z^3` is normal with one weighted-homogeneous
   simple-elliptic singularity and discriminant order twelve.  It realizes
   the local level-one numerical pattern, so normality does not eliminate
   the Halphen row.

Discriminant cancellation also creates false positives.  In the Hesse
family

```text
x^3+A(t)y^3+B(t)z^3+C(t)xyz,
A=t+3t^3,       B=t^2,       C=-3t-3t^3,                (5.5)
```

the factor `C^3+27AB` begins in order seven, so the discriminant has order
24, while `c4` has order four and `c6` order six.  This is compatible with
one scaling step and a minimal discriminant of order twelve, but not with
Hodge level two.

The fail-closed successor is therefore:

1. stratify `F_0` by the finite projective orbit types of singular plane
   cubics;
2. compute the universal `c4,c6,Disc` of (5.4);
3. impose generic smoothness and saturate by the nonnormal locus;
4. test the simultaneous `8/12/24` divisibility locus;
5. on every survivor, run actual ternary-cubic minimisation rather than
   inferring level from valuations;
6. repeat at `4/6/12` to classify the possible simple defect fibres.

If the saturated `8/12/24` locus is empty, both one-point rows die.  A
nonempty locus is only a candidate list, not an existence proof.  The
calculation is finite because the coefficient-base degree is exactly three;
it should begin with small symbolic orbitwise jobs and move to AWS only when
elimination becomes heavy.

## 6. Source scope and firewalls

The invariant weights and relation between genus-one models and their
Jacobians are treated in Tom Fisher, *The invariants of a genus one curve*,
Proc. LMS 97 (2008), arXiv `math/0610318`.  The local relation
`v(Disc_model)=v(Disc_Jac_min)+12 level` is a minimisation theorem in
Cremona--Fisher--Stoll, *Minimisation and reduction of 2-, 3- and 4-coverings
of elliptic curves*.  Liu--Lorenzini--Raynaud, *Neron models, Lie algebras,
and reduction of curves of genus one*, Invent. Math. 157 (2004), Theorem 3.1,
supplies the no-section Hodge bridge used above; its 2018 corrigendum concerns
a later Brauer-group formula, not that theorem.  Sadek, *Minimal Genus One
Curves*, arXiv `1002.0451`, develops a related integral-model/Hodge
formulation under a rational-point hypothesis and is used only as
corroboration in the soluble case.  Thus no local-solubility hypothesis is
silently added at the Halphen point.

Firewalls:

- `T` is the scheme-theoretic image of `Z_GR`; its points are not branches,
  places, sheets, or ramification primes.
- A length-two point means a nontrivial base-parameter action, not two
  unresolved geometric points.
- The `m=3` surface has no section and is not called elliptic here.
- High discriminant order does not imply positive Hodge level.
- Necessary invariant divisibility does not prove an integral model is
  nonminimal, normal, effective globally, or induced by a polynomial map.
- The four rows classify the relatively minimal genus-one/discrepancy data;
  they do not classify all singularities of `X`.

## 7. Disposition

1. Submit Sections 1--4 to a hostile surface-theory review, with special
   attention to support transfer (3.3), multiple fibres, and the Picard
   lower bounds.
2. Independently reproduce the invariant normalisations and the two local
   controls in Section 5.
3. Build the finite central-orbit `8/12/24` threat map.  Treat every survivor
   as provisional until exact minimisation and a different-model review.
4. Promote the four-row theorem only after those reviews; do not make
   downstream work wait for them.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16387`.
- Body SHA-256:
  `3f3d7e0c71ecb8382f9d7671fb2470cb999262770f27680e9025141f50101c3c`.
- Frozen basis: `5cc7b50274df491cb09dbb91a8b528de77fc5ef4`.
