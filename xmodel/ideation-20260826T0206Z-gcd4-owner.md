# Blind whole-portfolio ideation round — gcd4 owner

Date: 2026-08-26 02:06Z

Status: independent strategy packet; proposals only.  No item below is a
mathematical promotion or a license to consume a producer-tier endpoint.

## Scan scope and new evidence

I rescanned all 46 rows of `APPROACHES.md`, not only the current `(8,12)`
lane.  I compared the active boundary/formal/characteristic-p roots (1--4,
19,21), the geometry and global-finiteness cluster (6--7,25--33,38--39), the
algebraic and counterexample-side alternatives (5,8--18,34--37,40--45), and
formal certification (46).  The round used these developments since the last
portfolio synthesis:

- terminal order-two/four maps are exact extremal-abc objects, equivalently
  signed moment configurations and provisionally weighted DZ trees;
- the loaded order-four residual plane has four ordinary torus nodes and one
  boundary `(2,7)` cusp, and its quartic Kummer cover has genus one, subject
  to the still-open source-projection premise;
- the D1 A/B disagreement is an E8 source-identity constant error, not the
  Singular `sat` API;
- TD6 V78 shows that `q16,...,q24` are first-order P12 source syzygies but not
  absent source directions;
- Lean C1 now builds and passes its axiom audit, so proof-producing identity
  checks can safely trail discovery asynchronously.

The remaining rows supplied no comparably sharp new trigger: in particular I
do not reopen the dead implication ladders, untwisted action residues, generic
metric arguments, or dimension-three descent.  I also do not infer lower-tail
closure from a terminal tree census.

## Ranked new connections and experiments

### 1. Replace the large quotient curve by the fixed lemniscatic elliptic curve

The exact divisor now found on the rational normalization `X` has quartic
branch residues `(1,1,2)` at three places: the two simple poles of `v` and the
order-six cusp pole.  Thus `Y: y^4=v` has signature `(4,4,2)`.  After a Mobius
coordinate on `X` and removal of a fourth power, it should be isomorphic over
the algebraic closure to

```text
E: eta^4=t(t-1),
```

the Euclidean/lemniscatic elliptic curve (`j=1728`).  This connects the current
quotient gate to rows 25,28,31,39 without needing a general genus engine.

**First experiment:** on AWS, parametrize the exact residual plane, identify
the three branch places, and emit explicit fourth-power and birational
identities to `E`.  Then pull back the explicit regular differential on `E`.
Once the source-projection certificate proves nonconstancy, the contradiction
is the elementary fact that `P1` has no nonzero regular differential.  This is
smaller and more reviewable than carrying the full weighted-projective model.

**Value:** potentially closes the entire loaded order-four leaf, all `U`, with
one fixed target and a short differential certificate.

### 2. Compile lower tails as Kummer eigensheaf maps, not coefficient systems

For every terminal tree/radicand `C:u^m=h`, compute the character summands of
`pi_* O_C(D)` explicitly.  The normalized coefficient functions `a_i`, the
Faber tails, and the Taylor loads have known deck characters and pole bounds,
so each remaining condition becomes a map between finite `H^0(P1,O(d))`
spaces.  Negative degree kills a character uniformly; degree zero reduces to
a determinant.  This links rows 2--3,25,28,31,39 and turns the weighted-tree
frontend into an honest source-typed lower-tail compiler.

**First experiment:** generate the eigensheaf degree table for all confirmed
`U=3` order-two/four profiles, then for symbolic `U` on the exact `m=4,g=3`
family below.  Shard only the nonnegative-degree character blocks on AWS.

**Value:** best candidate for converting finite terminal enumeration into a
uniform-in-`U` theorem rather than an endless passport farm.

### 3. Fourier-kill the exact-order-four gcd-three star family uniformly

Weighted-tree existence plus exact order four leaves `gcd(weights)=1` or `3`.
In the `g=3` case leaf stripping forces the unique weighted star, giving

```text
A=((x-b)^r+c)^3,  B=(x-b)^(3r),  U=r+1,
h proportional to ((x-b)^r+c)(x-b)^(3r+4).
```

The cover has a visible `mu_r` action (`x-b -> zeta(x-b)`, with the compatible
action on `u`).  Decompose every coefficient and lower tail into Fourier
modes.  Since the z-degrees are fixed at 8 and 12, only finitely many mode
differences can occur; for large `r` the equations should diagonalize or force
the unloaded/Hall stratum, leaving finitely many small `r` clients.

**First experiment:** derive the symbolic character table by hand, then run
AWS exact blocks for `r=2,...,12` to detect the stable recurrence and threshold.

**Value:** removes an infinite terminal family that a raw tree enumerator
would keep rediscovering.

### 4. Exhaust `U=4` over the base field by trace/norm sharding

For signed weights `n_i`, normalized centers `0,1,x,y`, the moment equations
give, outside the decomposable pair case,

```text
n3(n1+n2)x^2 - 2 n2 n3 x + n2(n1+n3)=0,
disc = 4 n1 n2 n3 n4,
y=(n2+n3 x)/(n1+n2+n3).
```

Thus every four-node affine terminal configuration is at most quadratic over
its profile field.  Instead of reconstructing each algebraic Belyi map, emit
the lower tails in the quadratic algebra and descend them by trace and norm.
Handle `n1+n2=0` separately via its linear `x+y=1` solution, and saturate all
collisions and exact-gcd failures.

**First experiment:** enumerate admissible integer profiles only, compile two
base-field systems per profile, and compare their count with the weighted-tree
Hurwitz count before any saturation endpoint is consumed.

**Value:** an exhaustive, field-safe `U=4` wave with no numerical recognition.

### 5. Couple terminal trees to the three-generator collision ideal

The old passport test (row 25) was too generous because it saw one cover.  The
new exact identity for row 32 gives the off-diagonal collision scheme as
`I+(det A)` with only three generators.  For a weighted tree, label pairs of
ends and compute the valuation of those three generators along the unique
tree path between them.  Tropical initial ideals at paired ends then test both
Keller coordinates and their Jacobian contacts simultaneously.

**First experiment:** for every `U<=4` weighted tree, enumerate unordered end
pairs, form the path-valuation initial ideal, and look for a leaf-removal
recurrence.  Use AWS only for exact saturations after the combinatorial screen.

**Value:** upgrades dessins from a single-coordinate necessary condition to a
coupled injectivity obstruction and may feed a global pruning theorem.

### 6. Use a filtered Rees module for the TD6 high-q syzygies

V78 says `q16,...,q24` vanish in the first P12 differential but remain real
source directions.  Treat the first-order kernel as a filtered module and
compute the initial Fitting ideal of the second fundamental form on that
kernel, with dead-stretch coefficients included.  This is the module analogue
of the corrected D1 Rees-cone calculation: it asks at which valuation order a
nominally invisible direction first becomes visible, rather than deleting it
or expanding the whole nonlinear atlas.

**First experiment:** automatic second differentiation only on the eleven
dead-stretch plus nine high-q slots, reduce modulo the frozen V78 image, and
shard the resulting weight blocks.  A nonzero initial Fitting minor is a
finite obstruction; a zero block gives an exact higher-order syzygy to carry
forward.

**Value:** proof-discriminating bridge between avenues 2,4,38, avoiding serial
one-coordinate growth.

### 7. Make source identities proof-carrying with derivative-plus-basepoint checks

The D1 E8 incident exposes a general compiler flaw: equality of derivatives
certifies a polynomial identity only up to a constant.  Every hand-factored /
expanded A/B equivalence should emit both a derivative/Jacobian comparison
and evaluation at a canonical integral basepoint.  The same generator should
emit a small Lean `ring` theorem for the source identity, while CAS endpoints
remain separate and asynchronous.

**First experiment:** repair D1 E8 from the reviewed B source, auto-generate
the two checks and Lean identity, then apply the template to the TD6 and Faber
compilers.  Add a constant-defect negative control.

**Value:** does not prove JC2 directly, but prevents silent source corruption
at precisely the interfaces now carrying the highest-value Rees and quotient
claims (rows 4,36,46).

## Allocation recommendation

Run 1 and the current source-projection certificate immediately; they can
close a whole `(8,12)` leaf.  Start 2 and 3 as the uniform unbounded-`U`
research lane.  Use 4 as the next bounded exhaustive wave, 5 as the genuinely
coupled passport experiment, and 6 behind the active TD6 producer.  Deploy 7
as shared compiler infrastructure without blocking any producer or review.
