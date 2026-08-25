# TD6 after V76: finite transverse-modulus inventory and batch gate

Status: **source-typing design note; no new theorem.**  V76 is still
review-gated and concerns only the fixed source-typed A3 q2-beta section.

## 1. What remains after the registered normalizations

The fixed combinatorial chart has rectangles `(15,60)/(25,100)`, one
x-cluster, reduced F1 pattern, and

`x=c1*s+c2*s^2+c3*s^3+t*s^4`.

The finite continuous inventory is:

| family | raw slots | quotient/source status | next disposition |
|---|---:|---|---|
| common center | `c1,c2,c3` (3) | licensed and transverse to regular source reparametrization; V76 quantifies this A3 only while all other listed data stay frozen | bank fixed-A3 result; do not recount as an untested direction inside that section |
| normalized q boundary | `q_j`, `2<=j<=24` (23) | `q_0=0`, `q_1=1`, `q_25=1`; `q_15*p` is the target lower-shear gauge; q2=beta is quantified by V76 | remaining same-stratum transverse candidates are `q_3..q_14,q_16..q_24` (21) |
| r9 dead stretch | `d_6,..,d_16` (11) | licensed, not gauge; changes the transport matrix | one dependency-filtered simultaneous dead block, ordered by first entering row |
| p boundary inside the 15-fold-root stratum | scale and translation only | `t^15` scale and `t^14` translation are normalization/reparametrization directions | no remaining same-stratum p modulus |
| full unsplit p boundary | raw `p_2,..,p_14` (13) | leaves the 15-fold-root component; the visible `p_14` direction is reparametrization, but the full quotient has not been frozen | separate root-partition/component atlas; do not mix into the same-stratum gate |
| F1/pole variables | `(S,D,L,A)` (4) | the frozen tangent constraint matrix has rank `4/4`; no stand-alone motion, but unique forced compensators may appear | eliminate as compensators in each simultaneous block |
| target gauges | 4 | two translations, reciprocal scaling, lower shear; zero Jacobian tangent | quotient away |
| source-coordinate jets | finite at each licensed truncation | the full tangent includes chart, p, and q pieces; never use a q-only vector as the whole orbit | quotient before forming transverse columns |

Thus the next **same-root-stratum** continuous block has 32 obvious
coordinates: 21 remaining q coefficients and 11 dead-stretch coefficients.
This count excludes the already quantified center/q2 coordinates and the
four forced F1/pole compensators.  The full unsplit-p component contributes
13 raw slots but requires a separate quotient/component audit; it is not
honest to add “12” to the 32 until that quotient is frozen.

Other F1 orbit patterns and other terminal/combinatorial classes are
separate discrete or positive-dimensional components, not hidden
coordinates of this one source chart.

## 2. There is no ordinary tangent space at an empty slice

Write the original source equations as

`r_i(z;m)=0`,

where `z` are transport/Jacobian unknowns and `m` are normalized source
moduli.  V76 provisionally says that for

`m=(C,V,U,beta)`

with all transverse data frozen, the source ideal contains `1` on a finite
constructible cover.  The corresponding fibre scheme is empty.  It has no
points and hence no ordinary Zariski tangent or conormal fibre.

The familiar linear map

`delta m -> [D_m r(delta m)] in coker(D_z r)`

requires a compatible base solution `z`; none exists here.  One may
differentiate a chosen source unit certificate

`sum lambda_i r_i = 1`,

but over dual numbers its deformation is automatically a unit:

`sum lambda_i r_i(eps)=1+eps*h`,

and `1+eps*h` has inverse `1-eps*h`.  Equivalently, an empty closed
subscheme remains empty under a nilpotent first-order thickening.  This is
the correct “tangent/conormal” conclusion at the V76 slice: the intrinsic
module is vacuous, while the derivative source-DAG is useful only as an
ambient compiler/support audit.

Consequently a q3 run at `beta=0,gamma=eps` is only a discriminator.  It
can certify the source slot `('g','X',0,3)`, direct `q'` contribution
`3*gamma*t^2`, varying-echelon/lambda-prime terms, degree/support, and
denominator factors.  Its dual-number emptiness cannot prove an untruncated
gamma line or a neighborhood, and a nonzero derivative cannot locate or
exclude finite gamma values.

## 3. Avoiding a coefficient-by-coefficient chain

One all-32-variable elimination is mathematically legitimate but is a poor
first implementation target: the q block preserves the homogeneous
transport matrix, while dead stretch changes it.  The smallest
dependency-complete plan is a two-tier finite atlas.

### Tier Q: all normalized q coefficients simultaneously

Use

`q=t+sum(b_j*t^j, 2<=j<=24)+t^25`

with the lower-shear `b_15` quotient removed.  The transport homogeneous
matrix is constant; only its affine boundary RHS varies linearly.  The
Jacobian rows see the same coefficient vector through

`q'=1+sum(j*b_j*t^(j-1))+25*t^24`.

Build a single original-row module over

`E[C,V,U,b_2..b_14,b_16..b_24]`,

reuse the frozen transport echelon, and seek an operator-level P12/N13
syzygy whose unit remainder is independent of the entire q vector.  Use a
fraction-free numerator DAG and augmented Fitting ideals.  Every pivot or
denominator divisor becomes an explicit constructible stratum; rank is
stratified before consistency is asserted.  Sparse evaluation/interpolation
may discover the identity, but promotion requires a certified degree bound
and exact symbolic replay of the reconstructed polynomial identity.

The first decisive falsifier is untruncated `(beta,gamma)` q2+q3 on the
generic center chart, not another dual run: does the reviewed combination

`P12-(25/k)*T*N13`

retain the constant unit `-k/50` after the complete q3 source lift?  A yes
licenses the universal-q operator attack; a new numerator factor becomes a
named atlas divisor.

### Tier D: all eleven dead-stretch coefficients

Dead stretch changes the transport matrix, so it should not be hidden in
Tier Q's constant-matrix cache.  First compute all eleven exact source-typed
columns together and filter them by the earliest equation in which they
enter.  Form the smallest dependency-closed prefix block, including forced
`(S,D,L,A)` compensators from the invertible 4-by-4 tangent system.  Run
fraction-free source-DAG/Fitting elimination on each rank stratum.  Promote
only after the finite divisor atlas closes; do not infer the later dead
slots from a first-entry pattern.

If Tier Q yields a universal unit syzygy whose coefficients remain valid
when the transport matrix varies, then Q and D can merge into one
32-variable source identity.  Until that exact operator identity exists,
the two-tier atlas is the minimal source-honest batch design.

### Separate P atlas

The general unsplit `p_2,..,p_14` family changes the 15-fold-root partition
and may change source normalization.  It needs its own component atlas and
full source-orbit quotient.  It must not be advertised as a transverse
neighborhood of the fixed monomial-p result.

## 4. Immediate schedule and stop rules

1. Run V77 q3 dual only as a compiler/support sentinel; stop interpreting
   it after source slot, direct q-prime, lambda-prime, and denominator
   controls pass.
2. Launch the untruncated `(beta,gamma)` generic-open source-DAG identity.
   If the unit is gamma-independent, move directly to the universal q
   vector.  If not, factor the exact compatibility numerator and recurse on
   every divisor.
3. In parallel, emit the 11-column dead-stretch first-entry/dependency
   table without eliminating each coefficient separately.
4. Do not open q4, q5, ... as independent lanes unless the simultaneous q
   representation fails a preregistered memory/degree cap and the failure
   identifies a mathematically necessary block boundary.
5. Keep all p-partition changes and other F1/terminal components outside the
   fixed-A3 promotion statement.

This design turns the remaining work into a finite constructible atlas,
not an unbounded sequence of one-parameter experiments.
