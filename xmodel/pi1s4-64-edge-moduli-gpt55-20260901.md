# EDGE-MODULI report: excluded row moduli

## Scope and input verification

Frozen inputs were checked with `shasum -a 256` before reading them; all four
matched the charge:

```text
a352be2af1aebb5e158cb541a6eacdd0feb90f2ea3aa6750fb4bf1969c6bfefe  pi1s4-64-torus-check-opus5-20260831.md
d0dc4f7971b39f516dae2337cb172f8357bb1618b1143b800c524dbf95b5f31a  pi1s4-64-zvk-u6-opus5-20260831.md
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb  row-sweep-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

I read only the frozen input copies under
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.cEifJ8/inputs`.
No canonical ledger or `jc2-lean` path was inspected, and no file outside this
report was edited. No CAS and no uncertain-duration computation was run. I did
not fetch new literature; the only literature consumed is the already-fetched
Oka05/Sh12 data quoted and hashed inside
`TC:405-454` and `TC:751-759`.

## Source map and constraints used

Path abbreviations used below:

```text
ZVK = /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.cEifJ8/inputs/pi1s4-64-zvk-u6-opus5-20260831.md
TC  = /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.cEifJ8/inputs/pi1s4-64-torus-check-opus5-20260831.md
RS  = /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.cEifJ8/inputs/row-sweep-sol56-20260831.md
CI  = /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.cEifJ8/inputs/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

The row normal form is the only source for local typing. It states every row
member as

```text
x = r(t)^2,  y = q(t),
r = t^3 + bt + c,  q = t^4 + (2b/3)t^2 + (4c/3)t,  c != 0,
j = b^3/c^2.
```

See `ZVK:154-163`. Singular parameter pairs have
`t != s`, `r(t)=+-r(s)`, and `q(t)=q(s)`, with `e=t+s`, `p=ts`
(`ZVK:94-103`). The minus branch is empty for `c != 0`; the plus branch
is exactly

```text
h(e) = e^3 + (4b/3)e - 4c/3 = 0,       p = e^2 + b.
```

This is `ZVK:165-175`. The two excluded parameters enter separately:
`disc(r)=0` gives exactly `j=-27/4`, while `disc(h)=0` gives exactly
`j=-81/16` (`ZVK:191-203`). The campaign context is that the `(6,4)`
row was the sole degree-six nodal survivor before the torus-check lane
(`RS:112-183`, `RS:460-491`), and the integration
records the same residual as the unique topological core
(`CI:70-92`).

I use the FALLACY guardrail as a negative rule only: no cap/analogy replacement,
no raw-degree shortcut, and no new exit-price assertion.

## Row normal forms at the excluded moduli

For a plus-branch solution let `e=t+s`, `p=ts=e^2+b`. The two parameters
are the roots of

```text
T^2 - eT + (e^2+b) = 0,             (1)
```

and `h(e)=0`. The pair discriminant is

```text
(t-s)^2 = e^2 - 4(e^2+b) = -3e^2 - 4b.             (2)
```

If `3e^2+4b=0`, then `h(e)=e(e^2+4b/3)-4c/3=-4c/3`, impossible because
`c != 0`. Thus every plus solution has two distinct parameters.

The common image can be read without an implicit resultant. Since
`t^2=et-(e^2+b)`, one has

```text
t^3 = -bt - e^3 - eb.
```

Using `h(e)=0`, i.e. `c=(3/4)e^3+be`, this gives

```text
r(t)=r(s)=c-e^3-eb=-e^3/4,
q(t)=q(s)=b(e^2+b)/3.
```

So the affine double point attached to `e` is

```text
P(e) = (e^6/16, b(e^2+b)/3).                       (3)
```

The branch tangent test is equally explicit. The velocity at a parameter `z`
is `(2r(z)r'(z), q'(z))`. For a plus pair,

```text
r'(t)q'(s)-r'(s)q'(t)
 = -(1/3)(t-s)(3e^2+4b)(9e^2+4b).                  (4)
```

The first two factors cannot vanish by (2) and `c != 0`; also `r(t)=-e^3/4`
is nonzero because `h(0)=-4c/3`. Therefore the two branch tangents coincide
exactly when

```text
9e^2 + 4b = 0,          equivalently h'(e)=0.       (5)
```

Finally, each branch is smooth. If the parametrised velocity vanished at a
singular preimage, then either `r=0` (impossible for plus pairs) or
`r'=q'=0`; but `r'=0` implies `q'=4c/3 != 0`
(`ZVK:253-255`).

## Local singularity typing

### `j = -27/4`

Write

```text
r(t) = (t-tau)^2(t+2tau),   b=-3tau^2,   c=2tau^3,   tau != 0.
```

This is exactly the `(2,1)` cross-locus case recorded in ROW-NF
(`ZVK:191-199`). It is not a tacnode of the row curve. The affine
singularities still come only from the plus roots of `h`, and here `disc(h) != 0`
because the `h` discriminant vanishes only at `j=-81/16`
(`ZVK:200-203`). Hence all three roots of `h` are simple, and by (5)
all three affine double points have distinct branch tangents:

```text
Sing_aff(D_{-27/4}) = 3A_1.
```

The cross-locus collision itself is the smooth point `t=tau` over `x=0`.
Indeed `r(t)=z^2(3tau+z)` with `z=t-tau`, while
`q'(tau)=8tau^3/3 != 0`; locally

```text
x = z^4(3tau+z)^2,     y-y(tau)=q'(tau)z+O(z^2).
```

Thus the branch is smooth, with projection ramification order four over `x=0`.
It is a Zariski-van Kampen projection degeneration, not an affine curve
singularity.

### `j = -81/16`

Here `r` has three simple roots, but `h` has one double root and one simple
root. For the double root `e0`,

```text
9e0^2+4b=0,      c=(2b/3)e0,
```

and the remaining simple root is `-2e0`; `e0 != 0` because `c != 0`. Their
image points are distinct by (3), since the `x`-coordinates are
`e0^6/16` and `(-2e0)^6/16`.

The simple `h` root gives one ordinary node. The double `h` root gives two
smooth branches with a common tangent. The total affine delta is still exactly
`3` for every `c != 0` row member (`ZVK:154-163`). After the remaining
node contributes `1`, the tangential double point contributes `2`. For two
smooth branches this delta equals their intersection multiplicity, so the
contact is exactly two. Therefore the singularity is the ordinary tacnode:

```text
Sing_aff(D_{-81/16}) = A_3 + A_1.
```

There is no affine cusp, no `A_5`, and no multiplicity-`>=3` point in either
excluded member.

## Torus obstruction chain

### Projective singularity package

For both edge members the parametrisation is still birational of degree six
(`TC:89-99`). The calculation at infinity is unchanged:
there is one place at `Q_infty=[1:0:0]`, with multiplicity `2` and
`I(C,L_infty;Q_infty)=6` (`TC:103-124`). Since the affine
delta is `3` in both cases, the genus ledger gives `delta_infty=10-3=7`
(`TC:126-139`). A unibranch multiplicity-two germ with
`delta=7` is `A_14`. Thus the projective configurations are:

```text
j=-27/4:    3A_1 + A_14,
j=-81/16:   A_3 + A_1 + A_14.
```

### No torus type

The Oka inner-singularity calculus quoted in the torus-check says that an inner
simple singularity of a torus sextic is of type `A_{3i-1}` (if the cubic is
smooth there), or `E_6` in the singular-cubic case; also
`sum rho(P,5)=6` over inner simple singularities for a sextic of torus type
(`TC:253-261`). The torus-check applies this to the open row:
`A_1` is outer, `A_14=A_{3*5-1}` contributes `5`, and the missing contribution
would have to be an affine `A_2` cusp (`TC:263-280`).

The same count applies to the two edge members. `A_1` is not `A_{3i-1}` or
`E_6`; `A_3` is also not `A_{3i-1}` or `E_6`. Hence all affine singularities in
both edge members are outer. The only possible inner singularity is still
`A_14`, contributing either `0` or `5`, never the required `6`. Therefore neither
edge sextic is of `(2,3)`-torus type.

### Infinity meridian

For `j=-81/16`, `disc(r) != 0`, so the original `INF-TRIVIAL` proof applies
unchanged: over `x=0` the six points split into three disjoint two-strand
clusters, giving `g1=g2`, `g3=g4`, `g5=g6`; the geometric-basis product is
`gamma_infty=g6g5g4g3g2g1`, hence `gamma_infty=g5^2g3^2g1^2` and every
involution-valued representation kills it (`TC:494-555`).

For `j=-27/4`, replace the three `2`-clusters by a `4+2` cluster. At the double
root `tau` of `r`, the local model above gives `x=a z^4+O(z^5)`,
`y-y(tau)=b z+O(z^2)` with `ab != 0`; a loop around `x=0` cyclically permutes
the four nearby points, and the local ZvK relation identifies their four
meridians. At the simple root `-2tau`, the usual fold model gives one two-strand
identification. In an adapted basis,

```text
g1=g2=g3=g4,       g5=g6,
gamma_infty = g6g5g4g3g2g1 = g5^2 g1^4.
```

Thus any homomorphism sending all meridians to involutions has
`chi(gamma_infty)=1` here as well.

### Sh12/Shimada triple-cover contradiction

Assume an edge member admitted a surjection

```text
phi : pi_1(C^2 - D_j) ->> S_4
```

sending every meridian to a transposition. Composing with
`S_4 -> S_4/V = S_3` gives a surjective transposition-valued `psi`
(`TC:466-470`). By the infinity-meridian paragraph,
`psi(gamma_infty)=1`, so `psi` descends to `pi_1(P^2-Fbar_j)`. The associated
normal triple cover has branch divisor exactly `Fbar_j` of degree six
(`TC:434-450`). Sh12 Corollary 0.6 then forces `Fbar_j` to be
defined by `G_2^3+G_3^2`, i.e. to be of torus type
(`TC:405-454`). This contradicts the no-torus result above.
Sh12 is explicitly used because it has no genericity or simple-singularity
escape (`TC:424-430`).

## Conclusions

The two excluded row moduli are typed as follows:

```text
j = -27/4:   affine 3A_1.
             The `(2,1)` cross-locus is a smooth projection ramification point,
             not a tacnode of D.

j = -81/16:  affine A_3 + A_1.
             The `A_3` is an ordinary tacnode: two smooth branches with
             contact exactly two.
```

Neither member has an affine `A_2`, affine `A_5`, or affine multiplicity-`>=3`
singularity. The only inner-capable singularity left by Oka's calculus is the
existing infinity `A_14`, whose contribution is `5` and cannot meet the required
torus total `6` without an affine cusp. Therefore `NO-TORUS` extends to both
edge members.

The infinity bridge also extends. For `j=-81/16` it is the original
`INF-TRIVIAL` relation. For `j=-27/4` the `x=0` relation changes from `2+2+2`
to `4+2`, but still expresses `gamma_infty` as a product of even powers of
meridians, hence it is killed by every transposition-valued representation.
Sh12 Corollary 0.6 then gives the same contradiction as ROW-KILL.

Verdict:

```text
D_{-27/4}:   KILLED.
D_{-81/16}:  KILLED.
```

So residual `R2` is closed at the same ROW-NF/provisional row-geometry scope:
ROW-KILL extends from `j notin {-27/4,-81/16}` to the whole ROW-NF row
`c != 0`. There is no typed edge residual left open for these two moduli.

<!-- BODY-END -->
