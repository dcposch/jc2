# AS109 cubic-coupling gate

**Verdict: `CUBIC-Y NO-GO`.**

- Charged bank: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`
- Prime/seed: `p=109`, `(x-x^109,y)` over `F_109`
- Field theorem: arbitrary characteristic-zero field
- AS109 scope: arbitrary finite support and `x`-degree, with both correction
  polynomials of `y`-degree at most three
- GL2 target normalization and polynomial target shears: exact
- Exponent/support search, finite Witt inference, AWS: none
- Exact lift found: no
- JC2 inference: none

Every characteristic-zero Keller pair whose two coordinates have `y`-degree
at most three is a polynomial automorphism.  Consequently there is no exact
determinant-one AS109 lift whose two correction polynomials both have
`y`-degree at most three: the field theorem would make it injective over
`Q_109`, while the banked residue-ball lemma makes every exact lift of this
seed noninjective.

The only genuine new leading pattern beyond the quadratic gate is a
quadratic/cubic cusp block.  Its Jacobian equations put it over `K(x)` into

```text
f=z^2+U,        g=z^3+Vz+W,        z=h(x)y+r(x).
```

Polynomiality makes the initially rational shift `r` integral over `K[x]`,
hence polynomial.  The remaining Jacobian equations are then contradictory.
Thus no coupled cubic motif survives as a `CLOSED-SUPPORT + UNIT-L` compiler
core.  Any exact AS109 lift must have `y`-degree at least four in one
correction.

No novelty or prior-art claim is made for the field theorem; the deliverable
is its exact self-contained derivation and its campaign consequence.
The local corpus points to the classical leading-form/differential-equation
lineage of Magnus (1955), Appelgate--Onishi (1985), and Nowicki--Nakai
(1988) as the likely neighborhood for such a statement.  It does not contain
a verified copy of this exact degree-in-one-variable theorem, and the latter
two sources remain locally flagged as unresolved/paywalled, so this report
does not attribute the theorem to any of them.

## 1. Trust boundary

The frozen quadratic parent
`xmodel/as109-quadratic-coupling-gate-20260824.md` was still provisional when
this nonblocking child launched.  The cubic proof repeats the short
degree-at-most-two reduction it needs, so it does not promote or logically
depend on that review.  During production, the different-model quadratic
review landed `CONFIRMED` at `2026-08-24T09:51:15Z`; this improves the trust
state but is not needed by the proof below.  The earlier natural-support
parent is also not consumed.

The only banked campaign dependency is the dual-confirmed conditional Hensel
lemma in `xmodel/as109-support-gate-20260824.md`, with its carry erratum and
both reviews.  It applies only after an exact lift is assumed and is
independent of finite-digit carry bookkeeping.

## 2. Field theorem

### 2.1 Statement and the quadratic base

**Theorem.**  Let `K` be a characteristic-zero field.  If

```text
f,g in K[x,y],       deg_y(f)<=3,       deg_y(g)<=3,
J(f,g)=j in K^*,
```

then `(f,g)` is a polynomial automorphism of `A^2_K`.

We use the following self-contained quadratic base.  If both `y`-degrees are
at most two, the cubic Jacobian coefficient makes the two quadratic leading
coefficients proportional, so a constant target `GL_2` operation makes one
coordinate affine in `y`.  For

```text
f=a_1y+a_0,       g=b_2y^2+b_1y+b_0,
```

the quadratic Jacobian coefficient is

```text
2a_1'b_2-a_1b_2'.                                      (2.1)
```

If `a_1=0`, constant Jacobian forces `b_2=0`.  Otherwise (2.1) gives
`b_2=k a_1^2`, and the target shear `g->g-kf^2` removes the quadratic term.
For two affine-`y` coordinates, their leading coefficients are proportional;
a constant target combination produces `h(x)`, and
`J(h,b_1y+b_0)=h'b_1 in K^*`.  Hence `h` is linear, `b_1` is a nonzero
constant, and the pair has an explicit triangular inverse.  This proves the
quadratic base without consuming the parent verdict.

### 2.2 Cubic/cubic reduction

Write

```text
f=sum_(i=0)^3 a_i(x)y^i,       g=sum_(i=0)^3 b_i(x)y^i.
```

The highest Jacobian coefficient is

```text
[y^5]J(f,g)=3(a_3'b_3-a_3b_3').                         (2.2)
```

If both cubic leading coefficients are nonzero, (2.2) says
`a_3/b_3` is constant.  A constant target row operation kills the cubic
coefficient of one coordinate.  If one leading coefficient is already zero,
choose that coordinate first; if both vanish, use the quadratic base.  Thus
it suffices to analyze

```text
f=a_2y^2+a_1y+a_0,       g=b_3y^3+b_2y^2+b_1y+b_0.       (2.3)
```

Target operations preserve the Keller property and preserve automorphy.

### 2.3 Affine/cubic branch

Suppose `a_2=0`.  If also `a_1=0`, then `f=a_0(x)` and the coefficient of
`y^2` in `J(f,g)=a_0'g_y` forces `b_3=0`, contrary to the cubic branch.

If `a_1` is nonzero, the cubic Jacobian coefficient is

```text
[y^3]J(f,g)=3a_1'b_3-a_1b_3'.                            (2.4)
```

Equation (2.4) gives

```text
(b_3/a_1^3)'=0,       hence b_3=k a_1^3 for k in K.
```

The triangular target automorphism

```text
(f,g) -> (f,g-kf^3)                                    (2.5)
```

kills the cubic term.  The transformed pair lies in the quadratic base and
is an automorphism.  This settles every affine/cubic case.

Together with the prior reductions, the zero/top-degree cases are exhaustive:

- `a_3=b_3=0` enters the quadratic base directly;
- exactly one of `a_3,b_3` is zero already supplies the first coordinate of
  degree at most two, after a possible swap;
- two nonzero cubic tops are made proportional by (2.2) and one is killed by
  a constant target row operation;
- in (2.3), `b_3=0` is the quadratic base, while `b_3!=0` splits into
  `a_2=0` (this section) and `a_2!=0` (the genuine branch below);
- inside `a_2=0`, `a_1=0` contradicts `b_3!=0`, and `a_1!=0` is killed by
  (2.5).

### 2.4 Genuine quadratic/cubic leading form

Assume `a_2b_3` is nonzero.  The quartic coefficient is

```text
[y^4]J(f,g)=3a_2'b_3-2a_2b_3'.                          (2.6)
```

Work temporarily over an algebraic closure `Kbar`.  Equation (2.6) says
`a_2^3/b_3^2` is constant.  Unique factorization in `Kbar[x]` shows that

```text
a_2=alpha*h^2,        b_3=beta*h^3                     (2.7)
```

for a nonzero `h in Kbar[x]` and constants `alpha,beta in Kbar^*`: at each
irreducible factor, `3 ord(a_2)=2 ord(b_3)`, so the two orders are `2e` and
`3e`; taking the product of those irreducibles to the powers `e` constructs
`h` **inside `Kbar[x]`**.  Thus no unproved extraction of a polynomial root
from the fraction field is being used.  Constant diagonal target scaling
reduces (2.7) to

```text
a_2=h^2,             b_3=h^3,                          (2.8)
```

while keeping the Jacobian a nonzero constant.

Put `C=a_1` and `E=b_2`.  Under (2.8), the cubic coefficient is

```text
[y^3]J(f,g)
 =h^4 * (3C/h-2E/h^2)'.                                (2.9)
```

Hence `3C/h-2E/h^2` is constant.  Replacing `g` by `g+lambda*f` changes
that constant by `-2lambda`, so a constant target row operation makes it
zero.  We may therefore assume

```text
E=(3/2)hC.                                               (2.10)
```

Equivalently, the two rational depression shifts are

```text
r_f=C/(2h),             r_g=E/(3h^2),
6(r_f-r_g)=3C/h-2E/h^2.                                 (2.10a)
```

The cubic equation says only that their difference is constant; it does not
say they were equal initially.  Under the allowed constant target addition
`g->g+lambda*f`, one has `E->E+lambda*h^2`, hence
`r_g->r_g+lambda/3` and the right side of (2.10a) shifts by `-2lambda`.
Choosing `lambda` to kill the constant aligns the two depressions exactly.
Only after this operation do we use the common `r` in the next section.

### 2.5 Rational cusp normal form

In `Kbar(x)` define

```text
r=C/(2h),               z=hy+r,
U=a_0-r^2,
V=b_1/h-3r^2,
W=b_0-r^3-Vr.                                           (2.11)
```

Equations (2.8) and (2.10) give exact identities

```text
f=z^2+U,                g=z^3+Vz+W.                     (2.12)
```

Since `z_y=h`, computing the Jacobian first in `(x,z)` and then multiplying
by `h` gives

```text
J_(x,y)(f,g)
 =h ((3U'-2V')z^2-2W'z+U'V).                            (2.13)
```

The left side is the nonzero constant `jbar`.  Since `z` is nonconstant and
affine in `y`, its quadratic and linear coefficients in (2.13) vanish:

```text
V'=(3/2)U',          W'=0,          hU'V=jbar.           (2.14)
```

The constant field of `Kbar(x)` is `Kbar`, so

```text
V=(3/2)U+c,          W=w                           (2.15)
```

for constants `c,w in Kbar`.

### 2.6 Polynomiality forces the rational shift to be polynomial

Let `D=a_0` and `G=b_0`; both lie in `Kbar[x]`.  From (2.11)--(2.12),

```text
D=r^2+U,              G=r^3+Vr+w.
```

Substitute (2.15) and `U=D-r^2`.  Exact rearrangement gives the monic
identity

```text
r^3-(3D+2c)r+2(G-w)=0.                                  (2.16)
```

Thus `r in Kbar(x)` is integral over `Kbar[x]`.  The polynomial ring
`Kbar[x]` is integrally closed, so

```text
r in Kbar[x].                                            (2.17)
```

It follows that `U=D-r^2` and `V=(3/2)U+c` are also polynomials.  All three
factors in the last equation of (2.14),

```text
h * U' * V = jbar in Kbar^*,                             (2.18)
```

are therefore polynomials whose product is a nonzero constant.  Each is a
nonzero constant.  In particular `V` is constant and `U'` is a nonzero
constant.  But `V'=(3/2)U'` then says `0` equals a nonzero constant.  This is
a contradiction.  The genuine quadratic/cubic branch is empty.

All leading cases are now exhausted, so the pair is an automorphism over
`Kbar`.  Automorphy descends to `K`: the inverse is unique and fixed under
every `K`-automorphism of `Kbar` (equivalently, polynomial-coordinate-ring
isomorphy descends under the faithfully flat extension `Kbar/K`).  This
proves the theorem.

## 3. AS109 consequence

Suppose an exact lift existed with

```text
F=(P,Q)=(x-x^109+109A, y+109B),
A,B in Z_109[x,y],       deg_y(A),deg_y(B)<=3,
det J(F)=1.                                                   (3.1)
```

Over `Q_109`, both coordinates of `F` have `y`-degree at most three.  The
field theorem makes `F` a polynomial automorphism and hence injective.

Its reduction is `(x-x^109,y)` with identity derivative.  For every fixed
`b in F_109`, the 109 residue balls indexed by `(a,b)`, `a in F_109`, all
map bijectively by Hensel to the same target ball indexed by `(0,b)`.  The
exact lift is therefore noninjective over `Q_109`, contradiction.  Hence

```text
NO exact AS109 determinant-one lift has both correction y-degrees <=3. (3.2)
```

No marked collision equations, support cap, `x`-degree bound, coefficient
height, or finite Witt layer is used.

## 4. Controls and exact replay

The affine/cubic tame control

```text
f=x+y,            g=y+(x+y)^3
```

has Jacobian one, and `g-f^3=y` exercises (2.5).  The pair `(f+g,g)` has
both displayed coordinates cubic in `y`; the constant target operation
`(f+g,g)->(f,g)` exercises (2.2).  The replay also retains the quadratic
control `J(x+y,y+(x+y)^2)=1` and the triangular degenerate control
`J(x,y+x^3)=1`.

The cusp-shaped rejection

```text
f=x+y^2,          g=y+y^3
```

has `J(f,g)=1+3y^2`, not a Keller Jacobian.

Run:

```text
python3 cases/as109_cubic_coupling_20260824/verify_cubic_no_go.py
```

The standalone standard-library script uses a sparse formal coefficient
ring.  It checks (2.2), (2.4), (2.6), the full cubic coefficient underlying
(2.9), the cross-multiplied depression invariant (2.10a), its exact
`-2lambda` shift under `g->g+lambda*f`, the cusp Jacobian (2.13), and the
monic identity (2.16).  Independent integer arithmetic checks all tame and
rejection controls.  The displayed derivation proves arbitrary-degree
identities; the finite formal support is a deterministic regression replay,
not a search.

Expected top-level fields are

```text
verdict = PASS-CUBIC-Y-NOGO-CONTROLS
as109_conclusion = NO-EXACT-LIFT-WITH-BOTH-Y-DEGREES-AT-MOST-3
enumeration_run = false
lift_found = false
jc2_inference = false
```

## 5. Failure and resurrection condition

Alternative (A) fired: the whole cubic-`y` family is excluded.  Therefore no
genuinely coupled cubic normal form survives for a finite
`CLOSED-SUPPORT + UNIT-L` compiler.

The narrow next resurrection condition is a coupled section whose fixed point
has `y`-degree at least four in one correction.  It must still prove finite
nonlinear closure for the entire section and retain an integral right inverse
for `L`.  This report supplies neither a quartic grammar nor an exact lift.

The result is a restricted field theorem and an AS109 family exclusion, not a
proof or disproof of JC2.  It makes no inference from finite-field or
finite-Witt data.

## 6. Provenance hashes

| Artifact | SHA-256 | Status/use |
|---|---|---|
| `cases/as109_cubic_coupling_20260824/verify_cubic_no_go.py` | `7939c0d708548cf4ba2a06a6ca7a7abe64783014fb494bb1c543d308db875b42` | present replay |
| `xmodel/as109-quadratic-coupling-gate-20260824.md` | `10ee0b91d4be7ced8d6c053ba66e6d677d7c4cc83af89fc481d215f145e38ea1` | frozen parent producer; motivation only |
| `xmodel/as109-quadratic-review-grok-20260824.md` | `4ee7793d352d130d79b5efb1f555c8a241ed5ed59335426238505da5dcae48f2` | parent review landed `CONFIRMED` during production |
| `xmodel/as109-closed-support-gate-20260824.md` | `b3fa62651673db06b89fb6ad8217ebc2a61bacd5940b7a08501a1f3a47a7d717` | earlier parent; not consumed |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | banked Hensel dependency |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` | carry scope |
| `xmodel/as109-support-review-grok-20260824.md` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` | different-model review |
| `xmodel/as109-carry-erratum-review-grok-20260824.md` | `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212` | different-model carry review |

No parent, review, canonical file, or ledger was edited.
