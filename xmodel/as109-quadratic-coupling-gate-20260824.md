# AS109 quadratic-coupling gate

**Verdict: `QUADRATIC-Y NO-GO`.**

- Charged bank: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`
- Prime/seed: `p=109`, `(x-x^109,y)` over `F_109`
- Exact coefficient ring: `Z_109`; field step over `Q_109`
- Scope: arbitrary finite `x`-degree and support, but both correction
  polynomials have `y`-degree at most two
- Exponent rectangle, slot-cap search, finite Witt inference, AWS: none
- Exact lift found: no
- Characteristic-zero counterexample or JC2 inference: none

There is no exact determinant-one lift of the AS109 seed whose two correction
polynomials both have `y`-degree at most two.  The reason is stronger and
independent of a support ansatz: over any characteristic-zero field, every
Keller pair whose two coordinates have `y`-degree at most two is a polynomial
automorphism.  Such an automorphism cannot coexist with the already-confirmed
AS109 residue-ball noninjectivity.

This kills every rank-two, rank-three, or larger coupled coefficient motif
confined to quadratic `y`-degree, with no cap on its `x`-exponents.  A future
`CLOSED-SUPPORT + UNIT-L` certificate for this seed must allow `y`-degree at
least three.

## 1. Trust boundary and parent status

The immediate parent artifact
`xmodel/as109-closed-support-gate-20260824.md` is **PROVISIONAL** pending its
hostile review.  It motivated testing essential quadratic coupling, but no
theorem from that artifact is assumed here.  In particular, the present
field theorem reproves and strictly subsumes its affine-`y` restriction while
neither reviewing nor consuming its independent-literal-slot theorem.

The sole campaign dependency is the dual-confirmed conditional Hensel lemma
from `xmodel/as109-support-gate-20260824.md`, with its carry erratum and both
different-model reviews: an already exact `Z_109` polynomial lift of the
AS109 seed with determinant one is noninjective over `Q_109`.  That lemma is
independent of truncated digit carries and does not assert existence.

## 2. Characteristic-zero field theorem

### 2.1 Statement

**Theorem.**  Let `K` be a characteristic-zero field.  If

```text
f,g in K[x,y],        deg_y(f)<=2,        deg_y(g)<=2,
J(f,g)=j in K^*,
```

then `(f,g)` is a polynomial automorphism of `A^2_K`.

The proof uses a constant target `GL_2(K)` operation, followed when needed by
the triangular target automorphism `(u,v)->(u,v-ku^2)`.  These operations
preserve the Keller property and preserve whether the original pair is an
automorphism.

### 2.2 Make one coordinate affine

Write

```text
f=a_2(x)y^2+a_1(x)y+a_0(x),
g=b_2(x)y^2+b_1(x)y+b_0(x).
```

The cubic coefficient of the Jacobian is

```text
[y^3]J(f,g)=2(a_2'b_2-a_2b_2').                           (2.1)
```

If both `a_2` and `b_2` are nonzero, (2.1) and characteristic zero imply

```text
(a_2/b_2)'=0,       hence a_2=lambda*b_2 for lambda in K.
```

The constant target row operation `f->f-lambda*g` removes the quadratic
term from `f`.  If exactly one of `a_2,b_2` vanishes, the corresponding
coordinate is already affine in `y` (swap the coordinates if necessary); if
both vanish, there is nothing to do.  Thus, after a target `GL_2(K)` change,
one may assume

```text
f=a_1(x)y+a_0(x),
g=b_2(x)y^2+b_1(x)y+b_0(x).                               (2.2)
```

No case is lost: proportional coordinates would have zero Jacobian, so the
new affine coordinate cannot vanish identically in a Keller pair.

### 2.3 Remove the remaining quadratic term

For (2.2),

```text
[y^2]J(f,g)=2a_1'b_2-a_1b_2'.                            (2.3)
```

If `a_1=0`, then `f=a_0(x)` and

```text
J(f,g)=a_0'(2b_2y+b_1).
```

Since this is a nonzero constant and the characteristic is zero, `b_2=0`.
Both coordinates are affine in `y`.

If `a_1` is nonzero, (2.3) gives

```text
(b_2/a_1^2)'=0,       hence b_2=k*a_1^2 for k in K.       (2.4)
```

The triangular target shear

```text
(f,g) -> (f, g-k f^2)                                    (2.5)
```

has determinant one and polynomial inverse.  Equation (2.4) says exactly
that (2.5) kills the `y^2` coefficient of `g`.  Again both coordinates are
affine in `y`.

The first step needs only a constant `GL_2` target change.  The second is a
polynomial target shear; it is used over `K` solely to decide automorphy.  It
need not preserve the original integral AS109 representative or its special
fibre, and no claim here treats it as an allowed support gauge.

### 2.4 Affine-`y` Keller pairs are triangular

It remains to consider

```text
f=a_1(x)y+a_0(x),        g=b_1(x)y+b_0(x).                (2.6)
```

The two Jacobian coefficients are

```text
[y]J(f,g)=a_1'b_1-a_1b_1',
[1]J(f,g)=a_0'b_1-a_1b_0'.                               (2.7)
```

If both `a_1,b_1` are nonzero, the first equation says
`a_1=lambda*b_1` for a constant `lambda in K`.  Put

```text
h=f-lambda*g=a_0-lambda*b_0 in K[x].
```

Then

```text
J(h,g)=h'b_1=j.
```

A product of two polynomials in `K[x]` is a nonzero constant only when both
are nonzero constants.  Hence `h=alpha*x+beta` and `b_1=gamma`, with
`alpha,gamma in K^*`.  The inverse is explicitly

```text
x=(h-beta)/alpha,        y=(g-b_0(x))/gamma.              (2.8)
```

If one of `a_1,b_1` is zero, (2.7) directly gives the same triangular form
(possibly after swapping `f,g`); both cannot vanish because `j` is nonzero.
Thus (2.6), and hence the original quadratic pair, is a polynomial
automorphism.  This proves the theorem.

## 3. Application to the AS109 lift

Suppose for contradiction that

```text
F=(P,Q)=(x-x^109+109A, y+109B),
A,B in Z_109[x,y],       deg_y(A),deg_y(B)<=2,
det J(F)=1.                                                   (3.1)
```

After base change to `K=Q_109`, the two coordinates of `F` have `y`-degree
at most two.  The field theorem makes `F` a polynomial automorphism over
`Q_109`, hence injective on `Q_109^2`.

On the other hand, its reduction is

```text
F_bar=(x-x^109,y),       J(F_bar)=I.
```

For each fixed `b in F_109`, all 109 residue points `(a,b)` map to `(0,b)`.
The banked multivariate Hensel lemma says that every one of the 109 source
balls `(a,b)+109Z_109^2` maps bijectively onto the same target ball
`(0,b)+109Z_109^2`.  Therefore `F` is noninjective over `Q_109`, a
contradiction.

Consequently

```text
NO exact AS109 determinant-one lift has deg_y(A),deg_y(B)<=2. (3.2)
```

No marked-section condition is required.  There is no restriction on
`x`-degree, number of monomials, coefficient height, or coupled linear
relations among the coefficients.

## 4. Exact controls and replay

The positive quadratic Keller control

```text
f=x+y,                  g=y+(x+y)^2
```

has `J(f,g)=1`.  The forced shear gives `g-f^2=y`.  The pair `(f+g,g)` has
both displayed coordinates quadratic in `y`; the constant target operation
`(f+g,g)->(f,g)` exercises the first reduction.

The nonproportional-top negative control

```text
f=x+y,                  g=y+xy^2
```

has

```text
J(f,g)=1+2xy-y^2,
```

so the predicted nonzero quadratic Jacobian coefficient is visible.

Run the standalone standard-library replay:

```text
python3 cases/as109_quadratic_coupling_20260824/verify_quadratic_no_go.py
```

Its sparse formal coefficient ring checks (2.1), (2.3), and (2.7) on a
generic finite symbolic support.  Independent integer arithmetic checks the
quadratic Keller pair, both target reductions, the negative control, and the
degenerate triangular control `J(x,y+x^2)=1`.  The displayed coefficient
derivations prove the theorem for arbitrary degrees; the replay is a finite
regression control, not an exponent search.

Expected top-level fields are

```text
verdict = PASS-QUADRATIC-Y-NOGO-CONTROLS
as109_conclusion = NO-EXACT-LIFT-WITH-BOTH-Y-DEGREES-AT-MOST-2
enumeration_run = false
lift_found = false
jc2_inference = false
```

## 5. Failure and resurrection condition

The attempted smallest essential coupled escape, quadratic `y`-dependence,
is stopped globally rather than by a rank-two or rank-three motif census.
No positive closed module was found.

A future fixed-support contraction certificate for this AS109 seed must
allow a fixed point with `y`-degree at least three.  It must still provide a
finite genuinely coupled section, exact nonlinear closure on the whole
section, and an integral right inverse for `L`.  The present theorem says
nothing about cubic or higher `y`-degree and does not supply a finite grammar
there.

No result here proves or disproves JC2.  It excludes one exact-lift family;
it does not infer nonexistence of arbitrary AS109 lifts.

## 6. Provenance hashes

| Artifact | SHA-256 | Status/use |
|---|---|---|
| `cases/as109_quadratic_coupling_20260824/verify_quadratic_no_go.py` | `846aaef1be5be8efd402ce8c596cf6985b6f9fb19a5553d5bcd2757de746ed69` | present replay |
| `xmodel/as109-closed-support-gate-20260824.md` | `b3fa62651673db06b89fb6ad8217ebc2a61bacd5940b7a08501a1f3a47a7d717` | **PROVISIONAL parent; motivation only** |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | banked Hensel dependency |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` | carry scope |
| `xmodel/as109-support-review-grok-20260824.md` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` | different-model review |
| `xmodel/as109-carry-erratum-review-grok-20260824.md` | `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212` | different-model carry review |

The parent, banked producer, erratum, reviews, and canonical ledgers were not
edited.
