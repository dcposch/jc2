# Deep continuation: independent methods and controls

These notes describe computations, not a verdict on the full derived chart.
Frozen inputs were verified by the parent lane before these reads. The only
nonfrozen comparison code read was the named prior diagnostic engine and the
D108 survivor deep drivers; none was edited.

## Gate point controls at every local power

`deep_point_scan.py` evaluates the full degree33 K2 at the frozen gate point,
with `jet0=rho=1` or `jet0=c=1` and every other free output coordinate zero.
All four outer blocks are zero at these points. The script specializes the
coefficient blocks first. It independently substitutes the minor series in
the resulting rational polynomial by sparse `fractions.Fraction` arithmetic.
It does not obtain its point images from any elimination residual or solve.
At the historical endpoint depth, it compares every existing pole-row image
against the diagnostic engine's separate `local_rows` emitter.

The complete diagnostic point scans give:

| point | first strict pole failure | prior existing pole tags |
|---|---|---|
| delta2, `jet0=rho=1` | `G_local10_coord0 = 4096`, entering stage6 | all vanish |
| delta52, `jet0=c=1` | `G_local20_coord0 = 4096`, entering stage12 | all vanish |

The rational value 4096 is the square of the K2 local coefficient -64. The
two failures represent the same phenomenon under the denominator-two cover;
they are not units on the surrounding coefficient ideal. A failed point
never licenses replacing the locus by an empty set.

The auxiliary K3 leaders are calculated by direct polynomial substitution:
the first has local order9 and coefficients `3*zeta^2+zeta^3`; the second has
local order21 and coefficients `-pi+pi^3`. Their final F/G targets are formed
by exponentiating these computed leaders by the degree ratios99/11 and66/11.
Strict pole rows stop before the derived final target powers81/54 and189/126;
the final target rows subtract these nonzero polynomial faces. Merely setting
every old `raw_minor_support` tag to zero through its maximum would be an
incorrect extra restriction.

Every Jacobian band at either gate point vanishes identically, including the
constant coefficient. This follows exactly from `F=h2^3`, `G=h2^2` when all
outer blocks vanish. Accordingly, survival of positive-degree Jacobian bands
is expected and does not witness nonzero Jacobian. A full Keller necessary
chart must carry a nonzero constant `Jc`, its inverse `ZJ`, and the final
equations `J_constant-Jc=0`, `ZJ*Jc-1=0`. At the origin-type point with
`Jc=ZJ=1`, the former equation is -1 and the latter is0. The dilation already
used to normalize beta should not be spent again to demand a particular
numerical nonzero Jacobian constant.

## The gate points fail the added inner source-floor rows even earlier

The diagnostic output-coordinate chart permits arbitrary low-q K2 output
coordinates above its D2 floor. This is not the same as imposing the source
floors on both approximate-root remainders. To test the gate points against
those missing rows independently, the scanner performs exact monic division
of `K2-K3^3` by `K3` in `Q[t][z]`. The quotient and remainder are precisely the
normalized C2 and C3; the divisor has z-degree11 and unit leading coefficient,
so no field extension or parameter division is involved.

The weight and floors are read from `source_data.SOURCE`, which derives them
from the printed theorem. At both gate points, C2 has110 nonzero coefficients
strictly below its weight64 floor. Its minimum nonzero weight is15. The t5
band begins

```
z^0:-4224, z^1:3520, z^2:-2880, z^3:2304, z^4:-1792,
z^5:1344, z^6:-960, z^7:640, z^8:-384, z^9:192, z^10:-64.
```

C3 has94 below-floor terms on delta2 and140 on delta52, with minimum weight47
instead of the required96. Both begin `t5*(4224*z8+9152*z9+4992*z10)`.
Thus the original gate points do not pass the initial source-remainder
preblock of the full derived engine. Their later4096 failure describes only
the finite diagnostic chart in which those preblock equations were absent.
The JSON artifacts make this distinction explicit rather than silently
calling the points full-chart survivors.

## Exact deep continuation helpers

`deep_rows.py` implements two algebraic rearrangements intended for a driver
that carries every free variable and restricts only to a proved surviving
locus. Neither helper drops a coefficient by a floor.

First, polynomial substitution is a ring homomorphism. Compose the small K2
and four outer blocks with the full minor series, then form F and G from
their images. This produces the same local rows as first forming the large
global F/G and then composing, while avoiding most intermediate terms.

Second, expand the Jacobian by the product rule before multiplying the
coefficient polynomials. With normalized `H=K2`, `A=t66*A2`, `B=t99*A3`,
`C=t33*B1`, `D=t66*B2`, the exact expression is

```
(3H^2+A)*(H[H,C]+[H,D])
 -(2H+C)*(H[H,A]+[H,B])
 +H^2[A,C]+H[A,D]+H[B,C]+[B,D].
```

The bracket between normalization degrees d,e is emitted directly on two
monomials: `a*t^r*z^q`, `b*t^s*z^k` contribute
`((d-r)*k-(e-s)*q)*a*b*t^(r+s)*z^(q+k-1)`. The code obtains all degrees and
power ratios from the executable source derivation. In particular the
identically cancelling `[H^3,H^2]` product never needs to be expanded.

`deep_rows_control.py` compares this bracket formula with the frozen engine
on independent symbolic nonzero H,A,B,C,D blocks for every band t0..t5,
including all w coefficients. It also compares the composed-block local
formula to the frozen global-then-local emitter on both branches. Every
comparison passes over Q; `deep_rows_control.json` retains the evidence.

The helper `pure_power_radical_rows` has a deliberately narrow certificate:
if one existing row factors exactly as `a*f^n` with `a in Q*`, `n>1`, it may
adjoin `f`. It records and checks the polynomial identity. It will never
select one factor of a product of distinct factors such as `x*y`. This is
the safe local version of the D108 deep lane's radical reduction. General
set-equivalence of a proposed locus still needs its own proof.

Finally, `point_controls` separately records the original gate point and the
rational candidate obtained by resolving only an exact Q* pivot map. Each
candidate is substituted into the raw rows. A point of residual generators
alone is insufficient unless its pivot coordinates have been lifted and all
raw rows are checked.

## Full source driver, acceleration, and stronger Jacobian obligations

The independent source-coordinate stage0..2 runs complete over Q with
dimensions1025,978,936 on delta2 and1023,976,934 on delta52. Their cumulative
outer/joint QQ* pivot counts are41,88,130. Each residual ideal is zero, and
each stage's reconstructed rational point is substituted into every emitted
raw row. These points use the new explicit C2/C3 coordinates, not the old K2
output coordinates. They are distinct controls. With E82=0 and all other free
coordinates zero except jet0 and the localizer1, their first F/G failures are
G local34 (delta2) and74 (delta52). The newly required C2 minor floor sees
them earlier, at local8/16 with coefficient20/3. These source-coordinate
point scans are `deep_source_point_delta2.json` and`deep_source_point_delta52.json`.

`deep_driver.py` carries the initial outer D2 coordinate ring and adds the
outer D1 rows by scheduled offset. It propagates only QQ* pivots and verified
pure-power radical equations before each product. It emits the full local
and Jacobian schedules, and after the finite prefix also emits the source
minor bounds for C2/C3, h2's derived target, and every outer remainder.
Every reduction phase has a self-contained certificate: preceding map and
residual, raw new rows, the selected equation/leader/RHS of every pivot,
every radical source identity, and the following map/residual. This avoids
attempting to recover a preceding locus by deleting keys from a final map.

`deep_accelerated.py` uses exactly the same stages0..8, then processes all
canonical inner and outer minor rows in local-power order before further
global Jacobian products. The inner strict floors are18/27 or42/63. At the
inner equality, the actual coefficient equation is C2_face*P+C3_face=0,
since h3 has the derived faceP and h2 must have faceP^3. For the outer blocks,
strict minor bounds imply that the only F/G pole equations remaining are
A2_face*P^3+A3_face=0 and B1_face*P^3+B2_face=0. All their coefficients are
emitted. Thus the complete pole constraints can be certified by small-block
multiplication instead of forming the full global F/G. The final implication
check is literal polynomial equality, or an exact-Q Singular normal form in
the maintained localized residual ideal if nonzero residuals remain.

The independent complete inner probe and the accelerated smoke check agree:
delta2 has33 additional QQ* pivots, leaving31 inner coordinates; delta52 has
51, leaving11. Both have zero residual. This is graph elimination of actual
source rows, never a specialization to an arbitrarily chosen point.

`deep_gauge_accelerated.py` is a separately labelled gauge-slice instrument.
It derives the generic source state first, then applies only jet0->0 and
specializes the minor series before expansion. All other minor centres and
Hc_11_0 are retained. Its computation is typed as a slice until the parent
lane's explicit T_q/T_(-q) coefficient transport certifies coverage. The
delta52 stage0 slice control has dimension1022, exactly one less than1023 on
the redundant jet0-free chart. No numerical Jacobian normalization is added.

After the complete minor block, the strong gauge run imposes the parent's
derived D1 Jacobian face `(3*P*Q'-2*P'*Q)/9=Jc` coefficient by coefficient,
with Jc nonzero via its inverse ZJ. If needed, it additionally imposes the
constant coefficient of the global Jacobian, computed from actual polynomial
values and first derivatives at x=y=0. For a normalized degreeD coefficient
polynomial K, these three jets are K[D,0], K[D-1,0]-K[D-1,1], K[D-1,1].
`deep_gauge_corner_control.json` verifies the resulting Jacobian formula
against independent direct differentiation of symbolic actual x,y
polynomials. The zero-outer control returns0 exactly.

The D1 nonzero Jacobian face is a required source obligation, not an optional
conditional probe. A point satisfying only positive-degree global Jacobian
rows therefore cannot be promoted to a survivor of the full source chart.
The stronger source runs either produce a certified unit, a point of every
required row, or a recorded computation limit.
