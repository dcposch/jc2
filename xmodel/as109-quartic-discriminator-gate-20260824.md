# AS109 quartic-y discriminator gate

**Verdict: `QUARTIC-Y NO-GO`.**

- Charged bank: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`
- Production completed: `2026-08-24T10:16:58Z`
- Prime/seed: `p=109`, `(x-x^109,y)` over `F_109`
- Field theorem: arbitrary characteristic-zero field
- AS109 scope: arbitrary finite support and arbitrary `x`-degree, with both
  correction polynomials of `y`-degree at most four
- Exact target `GL_2`, target translations, and polynomial target shears:
  used only to test automorphy
- Generic exponent search, exponent rectangles, finite-Witt inference, AWS:
  none
- Exact lift found: no
- JC2 inference: none

Every characteristic-zero Keller pair whose two coordinates have `y`-degree
at most four is a polynomial automorphism.  The only new coprime leading
pattern beyond the cubic theorem is `(3,4)`.  Its exact coefficient equations
give a conserved product, and a degree-ten monic integrality equation forces
all initially rational depressed-form coefficients back into `Kbar[x]`.
The constant Jacobian row then contradicts the conserved product in every
branch.  Thus the `(3,4)` pattern is empty.

Consequently, no exact determinant-one AS109 lift can have both corrections
of `y`-degree at most four: field automorphy over `Q_109` would make the lift
injective, whereas the banked residue-ball Hensel lemma makes every exact lift
of this seed noninjective.  Any exact AS109 lift must have correction
`y`-degree at least five in one coordinate.

No novelty or priority claim is made.  The local corpus places the argument
in the classical leading-form/differential-equation lineage around Magnus,
Appelgate--Onishi, and Nowicki--Nakai, but it does not verify this exact
degree-in-one-variable statement in a primary source.  The theorem below is
therefore supplied self-contained and unattributed.

## 1. Trust boundary

This gate launched nonblockingly from the frozen cubic producer while its
different-model review was running.  That review subsequently landed
`CONFIRMED` during production (`2026-08-24T10:00:00Z--10:07:00Z`).  The
quartic proof nevertheless re-proves the cubic base it uses, so the quartic
theorem does not rest on promotion of its parent.  The earlier quadratic
producer/review are context only.

The sole campaign dependency for the AS109 consequence is the already
dual-confirmed conditional Hensel lemma in
`xmodel/as109-support-gate-20260824.md`, together with its carry erratum and
reviews.  That lemma assumes an exact lift and is independent of truncated
digit carries or marked-section collisions.  No existence result from the
AS109 support campaign is consumed.

## 2. Coefficient convention and cubic base

Let `K` be a characteristic-zero field and write

```text
f=sum_i a_i(x)y^i,              g=sum_j b_j(x)y^j.
```

The contribution of `(i,j)` to the coefficient of `y^(i+j-1)` in
`J(f,g)=f_xg_y-f_yg_x` is

```text
j a_i' b_j - i a_i b_j'.                              (2.1)
```

We first re-prove the needed cubic theorem.

**Cubic base.**  If `deg_y f,deg_y g<=3` and `J(f,g)=j in K^*`, then
`(f,g)` is a polynomial automorphism.

Order the actual `y`-degrees as `m<=n`.  If `m=n>0`, the top coefficient
from (2.1) is

```text
m(a_m'b_m-a_mb_m')=0.
```

Thus `a_m/b_m` is constant, and a constant target row operation lowers one
degree.  If `m=0`, then `f=a_0(x)` and `a_0'g_y=j`; hence `a_0'` and `g_y`
are nonzero constants, and the pair is triangular.  If `m=1<n`, the top
equation is

```text
n a_1'b_n-a_1b_n'=0,
```

so `b_n=k a_1^n`; the target shear `g->g-kf^n` lowers `n`.  Iteration
leaves only the genuinely coprime pattern `(m,n)=(2,3)`.

For that pattern, (2.1) gives

```text
[y^4]J=3a_2'b_3-2a_2b_3'=0.                           (2.2)
```

Over an algebraic closure `Kbar`, UFD valuations give, after constant target
scaling,

```text
a_2=h^2,                       b_3=h^3,
h in Kbar[x], h!=0.                                      (2.3)
```

The next coefficient is

```text
[y^3]J=2a_2'b_2+3a_1'b_3-2a_2b_2'-a_1b_3'
       =h^4(3a_1/h-2b_2/h^2)'.                         (2.4)
```

Adding a constant multiple of `f` to `g` shifts the parenthesis by a
constant, so the two depression shifts can be aligned.  With
`z=hy+r`, the pair has an identity over `Kbar(x)` of the form

```text
f=z^2+U,                       g=z^3+Vz+W.               (2.5)
```

The chain rule gives

```text
J_(x,y)(f,g)=h((3U'-2V')z^2-2W'z+U'V).                 (2.6)
```

Thus `V=(3/2)U+c`, `W=w`, and `hU'V=jbar`, where `c,w` are constants and
`jbar!=0`.  Put `D=f(x,0)` and `G=g(x,0)`.  Since

```text
D=r^2+U,                       G=r^3+Vr+w,
```

one obtains the monic equation

```text
r^3-(3D+2c)r+2(G-w)=0.                                  (2.7)
```

Therefore `r` is integral over the integrally closed ring `Kbar[x]`, so
`r,U,V` are polynomials.  In `hU'V=jbar`, every factor is then a polynomial
and hence a unit.  In particular `V` is constant while `U'` is a nonzero
constant, contradicting `V'=(3/2)U'`.  The `(2,3)` pattern is empty.  All
other cases reduced to a triangular pair, proving the cubic base without
consuming its parent verdict.

## 3. Reduction of the quartic cases

**Theorem.**  Let `K` be a characteristic-zero field.  If

```text
f,g in K[x,y],       deg_y(f)<=4,       deg_y(g)<=4,
J(f,g)=j in K^*,
```

then `(f,g)` is a polynomial automorphism of `A^2_K`.

If both actual degrees are four, the coefficient

```text
[y^7]J=4(a_4'b_4-a_4b_4')                              (3.1)
```

makes the leading coefficients proportional.  A constant target `GL_2`
operation therefore lowers one degree.  After a possible swap, it is enough
to take `deg_y g=4` and `m=deg_y f<=3`; degrees at most three are already
covered by Section 2.

- If `m=0`, `f=a_0(x)` and `a_0'g_y=j`, which forces `deg_y g=1`, so no
  quartic branch remains.
- If `m=1`, the coefficient of `y^4` is
  `4a_1'b_4-a_1b_4'=0`.  Hence `b_4=k a_1^4`, and the target shear
  `g->g-kf^4` lowers `g` to degree at most three.
- If `m=2`, the coefficient of `y^5` is
  `4a_2'b_4-2a_2b_4'=0`.  Hence `b_4=k a_2^2`, and
  `g->g-kf^2` lowers `g` to degree at most three.

The cubic base finishes all three cases.  The only unresolved actual leading
pattern is therefore `(3,4)`.

## 4. Exact normalization of the `(3,4)` pattern

Write the top of a genuine `(3,4)` pair as

```text
f=a_3y^3+a_2y^2+...,             g=b_4y^4+b_3y^3+....
```

The two highest potentially nonconstant Jacobian coefficients are

```text
[y^6]J=4a_3'b_4-3a_3b_4',                              (4.1)

[y^5]J=3a_3'b_3+4a_2'b_4-3a_3b_3'-2a_2b_4'.           (4.2)
```

From (4.1), UFD valuations in `Kbar[x]` give

```text
a_3=alpha_0 h^3,                 b_4=beta_0 h^4,
alpha_0,beta_0 in Kbar^*,        h in Kbar[x], h!=0.    (4.3)
```

Indeed `4 ord_pi(a_3)=3 ord_pi(b_4)` at every irreducible `pi`, so the two
orders are `3e,4e`; multiplying the corresponding `pi^e` constructs `h`
inside the polynomial ring.  Constant target scaling reduces (4.3) to
`a_3=h^3,b_4=h^4` while preserving a nonzero constant Jacobian.

Put `C=a_2,E=b_3`.  Under this normalization, (4.2) becomes

```text
h^6(4C/h^2-3E/h^3)'=0.                                 (4.4)
```

The rational depression shifts are

```text
r_f=C/(3h^2),                    r_g=E/(4h^3),
12(r_f-r_g)=4C/h^2-3E/h^3.                              (4.5)
```

Equation (4.4) says only that their difference is constant.  The allowed
constant target addition `g->g+lambda f` sends `E` to `E+lambda h^3`, so
the last expression in (4.5) shifts by exactly `-3lambda`.  Choosing
`lambda` aligns the depressions before introducing a common variable.  With

```text
z=hy+r,
```

there are exact coefficients `u,v,a,b,c in Kbar(x)` such that

```text
f=z^3+uz+v,                      g=z^4+az^2+bz+c.        (4.6)
```

This is an identity in `Kbar(x)[y]`; no rational source-coordinate change is
being asserted to be a polynomial automorphism.

## 5. Corrected normal-form equations

Since `z_y=h`, the chain rule cancels the two `z_x` terms and yields

```text
J_(x,y)(f,g)=h * [
  (4u'-3a')z^4
 +(4v'-3b')z^3
 +(2au'-3c'-ua')z^2
 +(bu'+2av'-ub')z
 +(bv'-uc') ].                                         (5.1)
```

The term `2av'` in the `z` coefficient is essential.  It rules out the
incorrect linear relation `b~u`; the exact replay checks the full row in
(5.1).

Vanishing of the first three rows integrates to

```text
a=4u/3+alpha,
b=4v/3+beta,
c=2u^2/9+2alpha*u/3+gamma,                             (5.2)
```

with `alpha,beta,gamma in Kbar`.  A constant translation of the target
coordinate `f` replaces `v` by `v+t` and `beta` by `beta-4t/3`; taking
`t=3beta/4` makes `beta=0` without changing the Jacobian or automorphy.

The `z` row of (5.1) is then exactly

```text
((4u/3+2alpha)v)'=0,
(4u/3+2alpha)v=delta,             delta in Kbar.         (5.3)
```

The constant row is

```text
jbar/h = (4/3)vv'-(2/9)u(2u+3alpha)u'.                 (5.4)
```

Equations (5.3)--(5.4), not the discarded `b~u` branch, control the genuine
quartic case.

## 6. Degree-ten integrality discriminator

Although `r,u,v` initially lie only in `Kbar(x)`, the original constant
terms

```text
D=f(x,0),                         G=g(x,0)
```

lie in `R=Kbar[x]`.  Define, first at the actual rational `r`,

```text
S=D-r^3,
E=G+r^4/3-alpha*r^2-gamma-(4/3)D*r.                    (6.1)
```

Substitution from (4.6) and (5.2) gives the exact identities

```text
S=ur+v,
E=2u^2/9+2alpha*u/3,
u^2+3alpha*u-(9/2)E=0.                                (6.2)
```

Using `v=S-ur`, the conserved product (5.3), and the quadratic in (6.2)
gives, without division,

```text
L u=M,                                                  (6.3)

L=2alpha*r+(4/3)S,
M=6rE-2alpha*S+delta.                                  (6.4)
```

Multiplying the monic quadratic in (6.2) by `L^2` and substituting (6.3)
produces

```text
M^2+3alpha*M*L-(9/2)E*L^2=0.                          (6.5)
```

No `L!=0` hypothesis is used.  To see the integrality content, replace `r`
in (6.1), (6.4), and (6.5) by an indeterminate `T`, while retaining
`D,G in R` as coefficients:

```text
S(T)=D-T^3,
E(T)=G+T^4/3-alpha*T^2-gamma-(4/3)D*T,
L(T)=2alpha*T+(4/3)S(T),
M(T)=6T*E(T)-2alpha*S(T)+delta.
```

Then the left side of (6.5) has degree ten and leading coefficient

```text
2^2-(9/2)(1/3)(4/3)^2 = 4/3.                           (6.6)
```

After multiplication by `3/4`, (6.5) is monic in `R[T]` and vanishes at
`T=r`.  Hence `r` is integral over `R`.  Because `R=Kbar[x]` is integrally
closed in `Kbar(x)`,

```text
r in R.                                                 (6.7)
```

Now `S,E in R`, and the monic quadratic in (6.2) makes `u in Kbar(x)`
integral over `R`; therefore `u in R`.  Finally `v=S-ur in R`.  This step
precludes cancellation of poles by `h` in (5.4).

## 7. The conserved-product contradiction

Put `q=4u/3+2alpha`.  All of `h,q,u,v` and their derivatives now lie in the
domain `R`, and (5.3) says `qv=delta`.

- If `delta!=0`, then `q` and `v` are units of `R`, hence constants.  Thus
  `u` and `v` are constant, so the right side of (5.4) is zero, contrary to
  `jbar!=0`.
- If `delta=0`, the domain property gives `q=0` or `v=0`.  If `q=0`, then
  `u` is constant and (5.4) reduces to `jbar/h=(4/3)vv'`.  The nonzero
  constant product `hvv'` forces `v` to be a unit, hence constant, contrary
  to `v'!=0`.  If `v=0`, then (5.4) says that a nonzero scalar multiple of
  `h*u*(2u+3alpha)*u'` is the nonzero constant `jbar`.  Every factor is a
  unit; in particular `u` is constant, contrary to `u'!=0`.

Every branch is contradictory.  Thus no Keller pair has actual leading
pattern `(3,4)`.  Section 3 reduces all remaining quartic cases to the cubic
base, so the field theorem is proved over `Kbar`.

The resulting automorphy descends to `K`.  The polynomial inverse over
`Kbar` is unique; applying any `K`-automorphism of `Kbar` gives the same
inverse, so its coefficients lie in `K` (equivalently, coordinate-ring
isomorphy descends under the faithfully flat extension `Kbar/K`).

## 8. AS109 consequence

Suppose there were an exact polynomial lift

```text
F=(P,Q)=(x-x^109+109A, y+109B),
A,B in Z_109[x,y],       deg_y A,deg_y B<=4,
det J(F)=1.                                                (8.1)
```

Over `Q_109`, both coordinates have `y`-degree at most four, so the field
theorem makes `F` a polynomial automorphism and therefore injective.

Modulo `109`, however, `F` is `(x-x^109,y)`, its derivative is the identity,
and every residue point `(a,b)` maps to `(0,b)`.  Multivariate Hensel says
that each of the 109 source balls indexed by `(a,b)` maps bijectively to the
same target ball indexed by `(0,b)`.  Hence the exact lift is noninjective
over `Q_109`, contradiction.  Therefore

```text
NO exact AS109 determinant-one lift has both correction y-degrees <=4. (8.2)
```

This uses neither a finite-Witt approximation nor a marked lattice-point
collision.  Target normalizations in the field proof need not preserve the
integral seed chart: they are used only to establish automorphy of the
original pair over `Q_109`.

## 9. Exact replay and controls

Run:

```text
python3 cases/as109_quartic_discriminator_20260824/verify_quartic_no_go.py
```

The standard-library sparse formal engine checks:

- (3.1), the affine/quartic and quadratic/quartic leading rows, and both
  rows (4.1)--(4.2);
- the cross-multiplied depression invariant (4.4) and its exact
  `-3lambda` target shift;
- every coefficient in the corrected normal-form Jacobian (5.1), including
  `2av'`;
- the conserved product, the quadratic relation, `Lu=M`, the exact
  eliminant remainder modulo the conserved-product relation, and degree ten
  with leading coefficient `4/3` (`24` after the replay's denominator
  clearing);
- the cleared constant row in (5.4).

Exact positive controls are

```text
J(x+y,   y+(x+y)^4)=1,                 # affine/quartic shear
J(x+y^2, y+(x+y^2)^2)=1,               # quadratic/quartic shear
```

and replacing the first coordinate of the first pair by `f+g` gives a pair
with both displayed `y`-degrees four, reversed by constant target `GL_2`.
The exact negative control

```text
J(x+y^3,y+y^4)=1+4y^3
```

rejects a superficially `(3,4)`-shaped non-Keller pair.

Expected top-level output fields are

```text
verdict = PASS-QUARTIC-Y-NOGO-CONTROLS
as109_conclusion = NO-EXACT-LIFT-WITH-BOTH-Y-DEGREES-AT-MOST-4
enumeration_run = false
lift_found = false
jc2_inference = false
```

The finite formal supports in the replay are regression witnesses for
universal identities, not a support or coefficient search.

## 10. Failure and resurrection condition

Alternative (A) fires: all coordinate pairs with both `y`-degrees at most
four are automorphisms, so no quartic coupled normal form survives as an
AS109 `CLOSED-SUPPORT + UNIT-L` compiler core.

The smallest remaining exact escape must allow `y`-degree at least five in
one correction.  A resurrection still requires an explicitly finite coupled
section with nonlinear closure, a residual module containing `x^108`, and
an integral right inverse for the linearized determinant operator.  This
report supplies no quintic motif, no closed section, and no exact lift.

The result is a restricted field theorem and a family-wise AS109 exclusion.
It does not prove or disprove JC2 and makes no inference from finite-field
or finite-Witt data.

## 11. Provenance hashes

| Artifact | SHA-256 | Status/use |
|---|---|---|
| `cases/as109_quartic_discriminator_20260824/verify_quartic_no_go.py` | `84fc5c3197490a405955220f95ca6f1777b0b47cc124b3763dbe158375e2e35e` | present exact replay |
| `xmodel/as109-cubic-coupling-gate-20260824.md` | `198f0b2ff39f91a7815b9be15f7fc3c3afdd00c00b1c4c0ada6b9f6438d62820` | frozen parent; base re-proved here |
| `xmodel/as109-cubic-review-grok-20260824.md` | `2fdb8ae2beffb766b38d8e7de4bdff353bc354c4dba84d026225f88376f95cef` | parent review landed `CONFIRMED` during production |
| `xmodel/as109-quadratic-coupling-gate-20260824.md` | `10ee0b91d4be7ced8d6c053ba66e6d677d7c4cc83af89fc481d215f145e38ea1` | earlier context only |
| `xmodel/as109-quadratic-review-grok-20260824.md` | `4ee7793d352d130d79b5efb1f555c8a241ed5ed59335426238505da5dcae48f2` | earlier review; context only |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | banked Hensel dependency |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` | carry scope |
| `xmodel/as109-support-review-grok-20260824.md` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` | different-model Hensel review |
| `xmodel/as109-carry-erratum-review-grok-20260824.md` | `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212` | different-model carry review |

No parent, review, canonical file, ledger, or AWS resource was edited.
