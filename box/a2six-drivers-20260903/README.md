# A2=6 fixed-N=6 moment artifacts

Status: `PROVED-HERE` for arithmetic identities and the displayed rational
matrix ranks; `WITNESS-ONLY / UNREVIEWED` for the non-proper contact-tree
completion.  Nothing here asserts geometric realization by a Keller pair.
In JSON key names, the legacy suffix `_t` means valuation in
`xi=x^{-1}`; `t` as a Python argument remains the integer ray index.
Legacy `unknowns_*` fields count independent value columns, not geometric
unknowns, and `*Schur_rank` fields are value-rank increments, not the actual
tame-parameter Schur map.

## What can and cannot be emitted

The frozen `GLOBAL-INTERPOLATION/1.0` driver correctly refuses the bare
`t=0` tuple (`bare-t0-stock-refusal.json`): it needs all `n` Puiseux roots.
The arithmetic numerically admits 12 proper bottom discs and fixes aggregate
non-proper counts; the witness manifest declares that packet but does not prove
attainment.  The charge does not fix the non-proper rooted tree, Galois action, tame
supports, coefficient sharing, or inverse/integration guard.  Therefore no
family-intrinsic associated-graded matrix or tropical basis exists from the
given data alone.

`a2six_moment_driver.py` emits the scalable direct consecutive-moment parity
map `A[r,i]=tau_i^r/D_i` for one declared valuation-tree completion.  Its raw
leaf model gives three confluent columns per rigid star.  Its macro model gives
one column per normalized cubic slot.  These are two conditional projections,
not a claim that either is the missing deformation-to-primitive map.

The full frozen quadratic lift is not attempted.  Even at the bottom/D2
window (`qmax_z=5`), branch-power variables alone have lower bounds
`417645, 4305807, 15744465, 38816019` for `t=0,1,2,3`; this omits every other
auxiliary family and SymPy expression overhead.

## Exact root counts and constants

For `P=7t+6`, `K=3P`, `e=3`, `u=18t+15`, and `k=12`:

| t | D | D2 roots `3u` | proper | D2 residual | top minor | all non-proper `3(K-12)` |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 54  | 45  | 36 | 9   | 9  | 18  |
| 1 | 117 | 99  | 36 | 63  | 18 | 81  |
| 2 | 180 | 153 | 36 | 117 | 27 | 144 |
| 3 | 243 | 207 | 36 | 171 | 36 | 207 |

The two size-six orbits are orbits of **discs**, not of all root series.
Because `A1=2` acts by `pi -> -pi` on
`p_g=pi(pi-1)(pi+1)`, each disc orbit displays one length-six branch orbit
(`pi=0`) and one length-twelve branch orbit (`pi=+/-1`).  Thus the visible
proper packet has four raw integration constants.  Getting the requested two
requires the explicit extra equality identifying the zero/nonzero constants
inside each disc orbit.  Non-proper constants remain undetermined until their
Galois partition is supplied.

This also fixes the `(4.13)/(4.16)` convention in the new driver: leading/star
coordinates are already in `Z_page`, so `U_page=h_constants+|Z_page|`; `u0`
is not added again.  Page matrix columns exclude constants and list them
separately.

## Rank tables

The homogeneous page has `K-1=17,38,59,80` equations.  For `k=12`:

| t | raw proper unknowns/rank/coker | D2 raw value increment | macro proper unknowns/rank/coker | D2 macro value increment | top value increment |
|---:|:---|---:|:---|---:|---:|
| 0 | 36 / 17 / 0  | 0  | 12 / 12 / 5  | 3  | 2  |
| 1 | 36 / 36 / 2  | 2  | 12 / 12 / 26 | 21 | 5  |
| 2 | 36 / 36 / 23 | 23 | 12 / 12 / 47 | 39 | 8  |
| 3 | 36 / 36 / 44 | 44 | 12 / 12 / 68 | 57 | 11 |

The separate monic row makes `K=18,39,60,81` affine DEG equations.  Raw
proper ranks/cokernels are `18/0,36/3,36/24,36/45`.  Macro proper
ranks/cokernels are `12/6,12/27,12/48,12/69`.  In the witness completion the
D2-residual value columns fill the entire raw value defect.  In the macro
projection D2 adds `18t+3`, while the top minor adds `3t+3`; value rank is `K`.

All ranks are exact over Q by a Hermite/Vandermonde determinant.  They were
also recomputed independently modulo `1009,1013,1019`; every residue agrees.

For the `k=6` negative-control packet, homogeneous raw proper
ranks/cokernels are `17/0,18/20,18/41,18/62`; macro ranks/cokernels are
`6/11,6/32,6/53,6/74`.  Witness non-proper value columns again fill all rows.

## Stable affine bottom functional

Let `h=K`, `p=3k`, and
`G_bot(Y)=product_(i in bottom)(Y-tau_i)`.  Whenever `h>p`, put

```text
Lambda_{t,k}(Y)=Y^(h-1-p) G_bot(Y).
```

If `lambda` is its coefficient vector, then exactly
`lambda^T A_bot=0` and `lambda^T b_monic=1`.  The exponent is `21t-19` for
`k=12` and `21t-1` for `k=6` (the formula exists from `t=1`; it is negative
at `t=0`).  On a non-proper column `eta`, the value is
`Lambda(eta)/D_eta`, generically nonzero.  Hence this is a stable bottom-block
functional, not a cofinal obstruction after the non-proper interface is
included.

## Conditional tropical minima

Completion A places all residual D2 roots in one cluster at
`rho=1/6+1/(6(Rres-1))` (`ord D=-3/2`) and the top block at contact 2.
Completion B changes only the formal residual contact to
`1/6+3/(6(Rres-1))` (`ord D=-7/6`).  Both obey the strict non-proper frontier.

For `k=12`, completion-A minimum weights and basis compositions
`(proper,D2-residual,top)` are:

| t | weight | composition |
|---:|---:|:---|
| 0 | 467/12 | (17,0,0) |
| 1 | 20263/124 | (24,14,0) |
| 2 | 84337/232 | (24,35,0) |
| 3 | 10832/17 | (24,56,0) |

Completion-B weights are `621/16,19745/124,82027/232,10566/17`; at `t=0`
the basis composition changes to `(15,2,0)`.  Thus even the minimum weight,
and sometimes the minimizing composition, changes under a formal non-proper
contact omitted by the charge.  These scalar contact trees are not asserted
Galois-complete or geometrically attainable.

## Controls and reproduction

```text
python3 box/a2six-drivers-20260903/verify_ray.py
python3 box/a2six-drivers-20260903/a2six_moment_driver.py selftest
python3 box/a2six-drivers-20260903/a2six_moment_driver.py controls
python3 box/a2six-drivers-20260903/a2six_moment_driver.py all --k 12
python3 box/a2six-drivers-20260903/a2six_moment_driver.py all --k 6
python3 box/a2six-drivers-20260903/a2six_moment_driver.py validate \
  box/a2six-drivers-20260903/t0-k12-manifest.json
python3 box/a2six-drivers-20260903/a2six_moment_driver.py validate \
  box/a2six-drivers-20260903/partial-orbit-refused.json
```

Selftest: 49 checks, PASS.  The frozen driver: 40 exact controls, 0 failures.
`verify_ray.py` hash-checks the frozen census and reproduces all four rows in
`ray-verification.json`.
`(y,x+y^3)` and `(y,x+y^5)` pass the same moment page; the rigid bottom star
passes its bracket and trace checks.  `y^2-x^2-x` fails NO-RESIDUE at t-order
1 with branch coefficients `+/-1/2`.  The partial five-of-six orbit exits 2
with `REFUSED[PARTIAL-ORBIT]`.
