# D105 driver probe notes

Status: `PROVED-HERE/UNREVIEWED` for the finite computations below.  No global
`D=105` interpolation rank was computed or inferred.

## Frozen-input gate and sealed checks

All eight charged SHA-256 values matched before inspection.  Exact replay:

```bash
sha256sum /tmp/jc2-lane.syVtTr/inputs/global-interpolation-sol56-20260902.md \
  /tmp/jc2-lane.syVtTr/inputs/globalinterp.py \
  /tmp/jc2-lane.syVtTr/inputs/census-rebase-opus5-20260902.md \
  /tmp/jc2-lane.syVtTr/inputs/survivors-D48-120.txt \
  /tmp/jc2-lane.syVtTr/inputs/ideation-20260903T1015Z-gpt55.md \
  /tmp/jc2-lane.syVtTr/inputs/time-function-endgame-review-sol56-20260902.md \
  /tmp/jc2-lane.syVtTr/inputs/bottomode.py \
  /tmp/jc2-lane.syVtTr/inputs/moh_skeleton_full.py

cd /tmp/jc2-lane.syVtTr/inputs
/usr/bin/time -f 'elapsed=%e maxrss_kb=%M exit=%x' python3 globalinterp.py controls
/usr/bin/time -f 'elapsed=%e maxrss_kb=%M exit=%x' python3 globalinterp.py selftest
```

Observed:

```text
controls: 40 checks, 0 failures; 3.84 s, 62,392 KB
selftest: 50 checks, 0 failures; 4.22 s, 62,800 KB
```

The example symbolic-rank replay also matches the sealed report:

```bash
cd /tmp/jc2-lane.syVtTr/inputs
python3 globalinterp.py example |
  python3 globalinterp.py emit - --rank symbolic --summary-only
```

It reports 36 lifted equations, 35 deduplicated equations, 27 lifted
unknowns, and exact ambient symbolic Jacobian rank 26.

## Concrete preflight wrapper

Artifacts:

```text
probe_d105_wrapper.py
probe_framework_audit.py
```

Replay:

```bash
cd /home/ubuntu/jc2/box/d105rank-drivers-20260903
/usr/bin/time -f 'elapsed=%e maxrss_kb=%M exit=%x' \
  python3 probe_d105_wrapper.py
```

The final observed time, memory, driver hashes, and deterministic JSON hash are
recorded in the sealed lane report rather than duplicated here.
Output is deterministic JSON.  It contains the eight
hash checks, sealed 40/0 and 50/0 checks, the exact group derivations, the
restricted local matrices and kernels, the count-only `2k` versus 35 table,
all 18 requested `(group,k,UNI/SPLIT)` manifest entries, the same-order control
statuses, and the tame-mutation vacuity guard.  Its global rank field is
deliberately `OPEN[D105-FULL-DECORATION]`.

Every `UNI` entry is `OPEN[D105-FULL-DECORATION]` and every `SPLIT`
entry is `OPEN[SPLIT-ORBIT-DATA]`.  The values `A_2=18,13,17` are orbit sizes
for factors of a local cover polynomial; they are not identified with
physical bottom discs or fibre branches.  Each entry prints the `3k` leaves
inside the requested stars and the `105-3k` residual leaves not in those
stars, marks the first nonvacuous global order `Q_*` unknown and the `D_2`
global emission not reached, and sets intrinsic `U(4.13)`, intrinsic
`C(4.11)`, global rank/cokernel, and saturation to `NOT_COMPUTED`.

## Exact skeleton arithmetic reached

Using Moh Def. 5.1(3), as implemented in the charged census:

| group | d-chain | delta | `(a_1,a_2,a_3)` | `(b_1,b_2,b_3)` | `R_min` | `J_2` in t | `J_2` in z |
|---|---|---|---|---|---:|---|---:|
| A | `(105,35,7,1)` | `(7/12,7/18,-1)` | `(3,75,105)` | `(2,50,70)` | 36 | `7/36` | 7 |
| B | `(105,35,7,1)` | `(11/26,2/13,-1)` | `(3,90,105)` | `(2,60,70)` | 26 | `7/26` | 7 |
| C | `(105,35,5,1)` | `(19/34,4/17,-1)` | `(3,84,105)` | `(2,56,70)` | 34 | `11/34` | 11 |

Here `a_r=n V_(r+1)/d_(r+1)` and
`b_r=m V_(r+1)/d_(r+1)`.  The first restricted exponent is
`E=J_2`; in all three groups it is nonresonant:

```text
A: mu=1/12, E/mu=7/3
B: mu=3/26, E/mu=7/3
C: mu=3/34, E/mu=11/3
```

Exact SymPy ranks of the charged restricted `(2,3,V_2=1)` operator are 5 in
all three cases, with kernel dimension 2 and cokernel dimension 0.  Kernel
bases and all matrix entries are in the wrapper JSON.  This proves only the
local two-parameter statement per decorated bottom disc.

The resulting blind count table is exactly:

```text
A: k=12,14,16,18,20,22,24 -> 2k=24,28,32,36,40,44,48 versus 35
B: k=13 -> 26 versus 35
C: k=17 -> 34 versus 35
```

Every row is `COUNTING-BOUND`.  No number in that display is a global matrix
rank, cokernel, ideal height, or emptiness certificate.

The charged census's Galois arithmetic also gives:

```text
A: A_1=2, A_2=18, Q_2=u=25, Q_2=1*18+7
B: A_1=2, A_2=13, Q_2=u=30, Q_2=2*13+4
C: A_1=2, A_2=17, Q_2=u=28, Q_2=1*17+11
```

For `V_2=1`, all three satisfy Moh's nonzero-root branch (10) and not the
zero-root branch (11).  Thus the selected level-2 nonzero factor of the local
cover polynomial brings its full `A_2`-tuple of distinct conjugate factors.
FALLACY-v2 forbids identifying that cover-factor orbit with a physical disc
packet or fibre-branch orbit without route-to-tree data.

## Vacuity mutation

For `(f,g)=(y,x+y^3)` on the fixed reference fibre `c_2=0`, take `x=z^-3`, put
`omega=(-1+sqrt(3)I)/2`, and index the unmutated fibre roots by

```text
tau_j=-omega^(-j)z^-1,  j=0,1,2.
```

Mutate one independent coefficient equivariantly by

```text
tau_j -> -omega^(-j)z^-1 + a omega^j z.
```

The wrapper verifies `tau_j(omega z)=tau_(j+1)(z)` and reconstructs
`product_j(y-tau_j)=y^3+3ay+x-a^3t`.  Its first forbidden positive input
coefficient is `-a^3` at `z`-order 3, exactly `t`-order 1.

The explicit Rabinowitsch check is in `QQ[a,sat_witness]`:

```text
<a^3, sat_witness*a-1> has Groebner basis <1>, hence is empty.
```

The positive closed-stratum witness `a=0` reconstructs the original valid
fibre; the negative open stratum `a!=0` is empty.  The mutated packet is
rejected by the polynomial-input guard before the finite DEG/POLY emitter, so
this is a same-wrapper input-vacuity check rather than an emitter failure.

The wrapper separately prints the negative control
`g=y^2-x^2-x` with residues `1/2,-1/2` at `t^1`.  The three requested positive
controls are exact/all-order and therefore print `SURVIVES-TO-Q` at each of
`7/36,7/26,11/34`, with the analytically expected one common additive
parameter for fixed exact roots before fixing the harmless common-shift gauge
(zero after fixing that gauge).  This is not a measured emitter kernel.

## Why the sealed emitter cannot yet issue the requested global rank

Section 4.1 of the sealed framework requires, for every run, a rooted cluster
tree on all `n` labelled leaves, a checked cyclic action, every truncated root
template, sharing declarations, and a sufficient guard.  The charged D105
data supplies the numerical chain and the normalized internal star
`p_g=pi^3-pi`, but it does not supply:

1. the full placement of all 105 leaves;
2. the centres and ancestor leading coefficients of the charged bottom discs;
3. the placement of the `105-3k` leaves outside those three-root stars;
4. a cyclic permutation of all leaves and coefficient covariance;
5. tame support and ancestor-sharing equivalence classes; or
6. enough actual coefficients to close every inverse-denominator guard.

Those values occur in the first global moment matrix.  Replacing them by
independent generic entries would calculate the rank of a different system.
Consequently neither the UNI label nor a proposed coarse split can fill them
without being printed as an additional realisation assumption.

There is also a concrete implementation issue: the sealed program does not
accept an explicit tree or cyclic permutation.  It infers contacts pairwise
and trusts orbit metadata.  A probe changed its two example roots from the
equivariant pair `I*z^-1,-I*z^-1` to
`I*z^-1,-2I*z^-1`, left `verified=true`, and the program accepted it, reduced
NO-LOG to one effective equation, and reused one integration constant.  A D105
wrapper must therefore verify the permutation/covariance itself before it
passes orbit metadata to the sealed emitter.

Other implementation boundaries:

* `result["unknowns"]` counts the quadratic lift's auxiliaries, not intrinsic
  `h+u_0+|Z_Q|` from (4.13).
* `rank_report` ranks the lifted auxiliary system.  The requested first-order
  cokernel is instead the rank of the 35 descended moment rows after
  eliminating deterministic auxiliaries and restricting to intrinsic tame
  directions.
* There is no saturated-ideal routine.
* The direct count table orbit-reduces NO-LOG only; it still lists moment and
  polynomiality slots at non-invariant `z` orders.
* The shipped positive controls use quotient-ring/direct identities, not the
  same finite-order emitter path, and there was no tame-mutation guard before
  this probe.

## Affordability audit and required redesign

Even an artificially cheap `n=105,m=70,L=1,qmax=0` valuation pattern forces
at least 10,920 prefix-product equations, 105 inverse equations, and 7,245
power equations if only one coefficient per power were retained.  Under the
current `desired_power` recurrence for `tau_i=(i+1)z^-1`, it instead creates
514,395 power equations, for 525,420 equations before time and evaluation.

Thus the current all-branch straight-line lift is not the sub-30-minute,
sub-6-GB route at `(105,70)`.  The bounded redesign is:

1. Require a separate decoration JSON and validate the 105-leaf ultrametric
   tree, cyclic permutation, star normalization, sharing classes, and guard.
2. Work directly with the 35 moments `M_0,...,M_34`, projected to the trivial
   character, rather than expanding all 71 interpolant powers on every leaf.
3. Differentiate those 35 coefficients with respect to the intrinsic tame
   symbols only.  Report `rank`, row-cokernel `35-rank`, and solution tangent
   dimension separately from all lifted counts.
4. At `J_2`, add only newly active tree symbols and outer-factor corrections,
   with provenance distinct from actual coefficient order.
5. For small resulting systems, declare the coefficient ring and generator
   order, form the ideal component explicitly, and saturate successively at
   the discriminants, unit leaders, Jacobian constant, and degree leaders.
6. Run all positive controls and the cubic mutation through the same moment
   path and report the first failing order.

Until item 1 has input data, the only correct global verdict is the bounded
`OPEN[D105-FULL-DECORATION]` emitted by the wrapper.
