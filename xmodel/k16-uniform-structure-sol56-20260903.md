# K=16 ray theorem (T): uniform normalizer and the t-dependent middle residual

**Lane:** `k16-uniform-structure-sol56-20260903`  
**Date:** 2026-09-03  
**Typed verdict:** **PARTIAL.**  The grading, weighted slice, quadratic
normalizer, Jacobian-scalar image, and its unit property are proved uniformly
for every integer `t>=1`.  The proposed fixed six-generator residual is false:
the exact `t=2` slice has four generators in two unknowns, while `t=3` has six
in three and `t=4` has eight in four.  No all-`t` unit certificate or proved
second affine recurrence is supplied, so theorem (T) on the whole ray is not
promoted.

Claim labels are literal. **PROVED-HERE** denotes a displayed proof or an exact
checked certificate. **MEASURED** denotes reproducible program output.
**MEASURED-MODULAR** never denotes a characteristic-zero proof. `OPEN[...]`
is a typed gap, not an invitation to fill it by finite sampling.

## 0. Custody, scope, and theorem direction

**MEASURED.** The readable receipt
`xmodel/k16-uniform-structure-sol56-20260903.run.v2` was parsed with `awk`.
The indexed `charged_input_<i>_basename` and `charged_input_<i>_sha256` fields
were paired mechanically under the receipt's
`/tmp/jc2-lane.fjoTgL/inputs` directory and passed to `sha256sum -c`. All
**15/15** frozen inputs returned `OK`; no digest was retyped to form the
manifest.

Only the frozen inputs were used as mathematical sources. Other than this
requested report, all new working artifacts are below
`box/k16uniform-20260903/`. No ledger was edited; `jc2-lean`, every
`ideation-*` file, and each prohibited in-progress lane report named in the
charge were not read.

Fix

```text
n=12t+4, m=8t+4, M2=12t+1, V2=3,
e=n/4=3t+1, q=m/4=2t+1, J(Q,P)=c*gamma, c!=0.
```

Here `J(f,g)=f_gamma*g_pi-f_pi*g_gamma`. If theorem (T) is stated with
`J(P,Q)` instead, then `J(P,Q)=-J(Q,P)` and replacing `c` by `-c` preserves
both `c!=0` and the saturated locus; no conclusion depends on this sign
convention.

The frozen Newton audit proves the radii
`(delta2',delta1')=(-1,t/(3t+1))` and the common coefficient bound
`ord C_i >= -i/e`; see the charged report
`k16-ray-T-newton-sol56-v3-20260903.md:194-239,280-337`.  With

```text
z=pi-gamma,
B=pi*z+b1*pi+b2,
A=pi*B+b3,
h=pi*A+b4,
```

the two-disc coefficient spaces are

```text
S_i=<1>                         1<=i<=t,
S_i=<1,A>                       t<i<=2t,
S_i=<1,A,B>                    2t<i<=3t,
S_e=<1,gamma,A,B,z>             e=3t+1.
```

The charts are

```text
P=h^e + sum_(i=1)^e alpha_i h^(e-i), alpha_i in S_i,
Q=h^q + sum_(j=2)^q beta_j h^(q-j),  beta_j in S_j.
```

The missing `beta_1` is the approximate-root/Tschirnhausen normalization.
The three safe target gauges are

```text
const(beta_q)=0, alpha_t=0, const(alpha_e)=0.
```

The middle gauge is `alpha_t`, not a fixed `alpha_2`: `e-q=t`, so its term
aligns with the leading `h^q` of `Q`. These are invertible triangular target
changes and preserve the Jacobian, monicity, degrees, and coefficient spaces
(charged uniform report, lines 84-119). The gauged chart has `9t+9` unknowns
including `c` and `14t+9` coefficient equations.

**Logical wrapper.** This polynomial order chart omits the reciprocal Laurent
tail and is a necessary **superset** of the requested tuple locus. Therefore
an exact characteristic-zero unit ideal after imposing `c!=0` proves theorem
(T) at that `t`. A nonunit ideal, a point of a subsystem, or a modular unit
basis proves no target existence/nonexistence. This is the one direction used
below.

## 1. Uniform positive grading

**PROVED-HERE.** Assign intrinsic weights

```text
wt(gamma)=wt(pi)=wt(z)=1, wt(B)=2, wt(A)=3, wt(h)=4,
wt(b_i)=i.
```

If a chart coordinate multiplying `phi` in `alpha_i` or `beta_i` is denoted
`u_(i,phi)`, set

```text
wt(u_(i,phi))=4i-wt(phi),
wt(c)=4(e+q)-3=20t+5.
```

Every `alpha_i` and `beta_i` then has total weight `4i`; every term of `P`
has weight `4e`, and every term of `Q` has weight `4q`. Differentiating in
`gamma,pi` lowers total weight by two, so `J(Q,P)` has weight
`4(e+q)-2`. Matching `c*gamma` gives the displayed `wt(c)`. Monic Euclidean
division by `h` and the h-adic carry preserve this grading. All weights are
positive for `t>=1`. The charged `Q*`-constant pivot substitutions are
grading-equivariant, so the grading descends to their quotient.

Define the two surviving distinguished coordinates

```text
x=beta_(t+1),A = q(t+1)_1,
y=beta_q,B     = q(2t+1)_1.
```

Then, uniformly,

```text
wt(x)=4t+1, wt(y)=8t+2=2wt(x), wt(c)=20t+5=5wt(x).
```

Thus the weights are linear in `t`. Their fixed values are

| `t` | `wt(x)` | `wt(y)` | `wt(c)` |
|---:|---:|---:|---:|
| 1 | 5 | 10 | 25 |
| 2 | 9 | 18 | 45 |
| 3 | 13 | 26 | 65 |
| 4 | 17 | 34 | 85 |

For each of `t=1,2,3,4`, the fresh fixed-`t` monomial-difference matrix has
nullity one and recovers these primitive positive weights exactly.

## 2. The all-`t` normalizer lemma

This is a formula proof, not interpolation from `t=2,3,4`.

### 2.1 Four high recurrences and the target row

Let

```text
g1=alpha_(t+1),A, g2=alpha_q,B, g3=alpha_e,z.
```

After the constant endpoint gauge, `alpha_e` has the ordered basis
`(gamma,A,B,z)`; the charged endpoint pivot sends its `gamma` coordinate to
zero. Reducing the named bands successively by the preceding higher bands in
the exact banded identity gives nonzero rational associates of

```text
E1, band 4t+1: q*g1-e*x = 0,
E2, band 3t+1: 2q*g2-(e-q)*x*g1-2e*y = 0,
E3, band 2t:   3q*g3-(e-2q)*x*g2-(2e-q)*y*g1 = 0,
E4, band t:    (e-3q)*x*g3+(2e-2q)*y*g2 = 0,
E0, band 0:    c+y*g3 = 0.
```

For completeness, here is the bridge from the exact banded identity, rather
than an interpolation from the four computed rows. Project the h-adic identity
to its localized top associated graded. Write bars for initial forms there.
The top chain and its induced parameter are

```text
hbar=pi*Abar, Abar=pi*Bbar, Bbar=pi*zbar,
Ubar=Abar*hbar^(-(t+1)),
Ubar^2=Bbar*hbar^(-q), Ubar^3=zbar*hbar^(-e).
```

Thus the distinguished initial forms of `Q/h^q` and `P/h^e` are

```text
F(Ubar)=1+x*Ubar+y*Ubar^2,
G(Ubar)=1+g1*Ubar+g2*Ubar^2+g3*Ubar^3.
```

In this face the chain rule gives the exact initial-form identity

```text
J(h^q F,h^e G)
  = h^(e+q-1) J(h,Ubar) * (q*F*G'-e*F'*G),
in(J(h,Ubar))=pi*h^(-t),
```

where primes mean formal differentiation in `Ubar`. The coefficients of
`Ubar^0,Ubar^1,Ubar^2,Ubar^3` land respectively in bands
`4t+1,3t+1,2t,t` (with the exact remainder tags `(0,1)`, `(0,0)`, the two
endpoint tags including `(1,2)`, and `(1,1)`). Every non-corner coordinate
that could occur in those coefficient rows has already been removed by the
preceding uniform Q-constant triangular spine; h-adic carries have strictly
preceding band/tag positions. Hence the projection of the reduced exact rows
is precisely the four coefficients displayed as `E1-E4`, with no unrecorded
chart term. The first three coefficients give `E1-E3`. There is no `g4`: the
`P` table ends at deficit `e`, whose chain ends at
`zbar=Ubar^3*hbar^e`. The fourth coefficient is consequently the obstruction
`E4`, not a solve for another coordinate.

The target row is exact as well. Before its endpoint reduction, the band-zero
tag `(1,0)` row is

```text
alpha_(e,gamma)*y-g3*y-c=0.
```

The endpoint pivot sets `alpha_(e,gamma)=0`; multiplying the remaining row by
`-1` gives `E0`. Its sign also follows directly from the gamma coefficients
`+1` in `J(B,gamma)` and `-1` in `J(B,z)=pi-gamma+b1`.

### 2.2 Closed `H_t` and `c_t`

Put `r=e/q`. Solving `E1-E3` gives the first three coefficients of
`F^(e/q)`:

```text
g1=r*x,
g2=r*y+binom(r,2)*x^2,
g3=2*binom(r,2)*x*y+binom(r,3)*x^3.
```

Substitution into `E4` and `E0` gives

```text
Hhat_t(x,y)=12q^2*y^2-12q(t+1)*x^2*y
             +(t+1)(3t+2)*x^4 = 0,                 (H)

c=t(3t+1)/(6(2t+1)^3) * x*y
  *((t+1)x^2-6(2t+1)y).                            (C)
```

`box/k16uniform-20260903/uniform_binomial_identities.py` checks the algebraic
consequences of `E1-E4` exactly in `Q(t)`. The preceding associated-graded
projection is the all-`t` chart proof; independently, the frozen-builder
extractor recovers its literal sparse rows at each of `t=1,2,3,4`.

Equation (C) and `c!=0` force `x!=0`. Over an algebraic closure choose
`lambda` with `lambda^(4t+1)x=1` and apply the weighted action. It sends
`x` to one, `y` to the invariant ratio formerly denoted `y/x^2`, and `c` to
the ratio formerly denoted `c/x^5`; the normalized symbols are again renamed
`y,c` below.

Conversely inverse scaling recovers the entire orbit, so no saturated point
is lost. The normalized relations are

```text
H_t(y)=12(2t+1)^2*y^2-12(2t+1)(t+1)*y+(t+1)(3t+2),
c_t(y)=t(3t+1)y*((t+1)-6(2t+1)y)/(6(2t+1)^3).
```

The degree of `H_t` is always two, its coefficients lie in `Z[t]`, and

```text
disc_y(H_t)=48(2t+1)^2(t+1).
```

The displayed polynomial is not primitive at every integer specialization;
dividing its content divides the discriminant by the square of that content.

### 2.3 Field versus rank-two algebra

The phrase “the quadratic field for every `t`” is false. Over `Q(t)`, `H_t`
is irreducible: after discarding the square factor `16(2t+1)^2`, its
discriminant has the factor `3(t+1)`, whose valuation at `t=-1` is odd and
so is not a square in `Q(t)`. At a positive integer it splits over `Q`
precisely when `3(t+1)` is a rational square. A rational square root of an
integer is integral; writing it as `r`, one has `3|r`, say `r=3s`, and hence
equivalently

```text
t=3s^2-1 (s>=1).
```

This is an infinite set, beginning at `t=2`. The uniformly correct object is
the separable rank-two algebra

```text
A_t=Q[y]/(H_t).
```

It is a quadratic field off the split set and a product of two rational
fields on it. It is reduced for every `t>=1`, because the discriminant never
vanishes there.

Moreover `c_t` is a unit in `A_t` for every positive integer `t`. Apart from
nonzero rational factors its two y-dependent factors are `y` and
`(t+1)-6(2t+1)y`, while

```text
H_t(0)=(t+1)(3t+2),
H_t((t+1)/(6(2t+1)))=(t+1)(4t+1)/3.
```

Both are nonzero. Equivalently the resultants are

```text
Res_y(H_t,y)=(t+1)(3t+2),
Res_y(H_t,(t+1)-6(2t+1)y)
 =12(t+1)(2t+1)^2(4t+1).
```

This proves the weighted normalization and the c-unit step uniformly,
including every split fiber.

## 3. Exact fixed-`t` structures

The “Q pivots” below are the charged characteristic-zero constant-pivot spine;
the “A pivots” are affine eliminations whose coefficients have explicit
inverses in the stated rank-two algebra. Every substitution was reduced and
checked modulo `H_t`. Degrees are total degrees in the final chart unknowns,
with `y` in the coefficient algebra.

| `t` | full rows / unknowns | Q pivots; quotient rows / unknowns | primitive `H_t`; disc | post-H/c rows / auxiliaries | A pivots | terminal system |
|---:|---:|---:|---|---:|---:|---|
| 1 | 23 / 18 | 7; 15 / 11 | `54y^2-36y+5`; 216 | 11 / 8 | 4 then unit | `[1]` |
| 2 | 37 / 27 | 10; 26 / 17 | `25y^2-15y+2`; 25 | 20 / 14 | 12 | 4 rows / 2 vars |
| 3 | 51 / 36 | 13; 37 / 23 | `147y^2-84y+11`; 588 | 29 / 20 | 17 | 6 rows / 3 vars |
| 4 | 65 / 45 | 16; 48 / 29 | `486y^2-270y+35`; 4860 | 38 / 26 | 22 | 8 rows / 4 vars |

### 3.1 `t=1`: `(16,12;13;3)`

Here `x=q2_1`, `y=q3_1`, and

```text
H_1=54y^2-36y+5,
c=-4y(9y-1)/81.
```

After four checked affine pivots the normalized system contains the
coefficient-field constant

```text
20y-10/3, inverse 27/10-27y/5 modulo H_1.
```

Thus its ideal is `[1]` before any multivariate basis computation. The
normalized and full gauged exact Singular replays both return `[1]` with all
controls passing. This is consistent with Moh's `(16,12)` conclusion but does
not attribute this unprinted elimination to Moh. It also explains why `t=1`
does not have the later terminal pattern: the boundary regimes of the
coefficient table collide and an early unit appears.

### 3.2 `t=2`: `(28,20;25;3)`

Here `x=q3_1`, `y=q5_1`, and

```text
H_2=(5y-1)(5y-2),
c=-7y(10y-1)/125.
```

The two fibers are

```text
y=1/5, c=-7/625;     y=2/5, c=-42/625.
```

Neither is discarded. Twelve common-algebra unit pivots and four zero-row
reductions leave four generators in `(b3,b4)`, one at each band
`h=0,1,2,3`, of degrees `9,8,7,6`. Independent rational-fiber presentations
are printed in `box/k16uniform-20260903/t2_t1_audit.md`; exact Singular `std`
returns `[1]` on each. The full 37-row gauged saturation independently
returns `[1]`.

This alone refutes the proposed literal residual: the safe gauge is
`alpha_t=alpha_2=0`, so `a2_0` is not even a `t=2` chart variable.

### 3.3 `t=3`: `(40,28;37;3)`

Here `x=q4_1`, `y=q7_1`, and

```text
H_3=147y^2-84y+11,
c=10y(2-21y)/343.
```

The fresh replay starts from the frozen charged drivers, repeats the thirteen
Q pivots, removes six exact Q-associate duplicates and the `H_3` row, and
uses seventeen checked A-pivots. It leaves exactly six generators in
`(b3,b4,a2_0)`, one at each band `h=0,...,5`, with degrees
`13,12,11,10,9,8`. Their complete coefficients are in
`box/k16uniform-20260903/t3_residual_generators.tsv` (SHA-256
`c09d9f0b8b7e763734c42d5c7cf69ca9adfd41d25ae53a3dbbbe1896badacae1`).

The exact replay input has SHA-256
`fc2c504604c51e33e7c63e32bde4a952d0c6741b99fcf5e9c334c63eefb4796b`,
identical to the charged decisive input. Singular 4.3.2 `std` returns

```text
MAIN_START ... residual_equations=6 residual_unknowns=3
MAIN_DONE basis_size=
1
MAIN_QUADRATIC_FIELD_EMPTY
G[1]=1
```

in 0.06 s with 12,988 KiB maximum RSS and empty stderr.

### 3.4 `t=4`: `(52,36;49;3)`

Here `x=q5_1`, `y=q9_1`, and

```text
H_4=486y^2-270y+35,
c=y(130-1404y)/2187.
```

Sixteen exact Q-pivots reduce the 65-row/45-unknown chart to 48 rows in 29
unknowns. After the slice, exact duplicate removal, and passage to
`Q[y]/(H_4)`, there are 38 rows in 26 auxiliaries. Twenty-two further
unit-only affine pivots leave eight generators in four variables
`(b3,b4,a2_0,q3_0)`, one at each band `h=0,...,7`, all with remainder tag
`(gamma_power,pi_power)=(0,1)`, and degrees `17,16,...,10`. The appearance of
`q3_0` rather than `a3_0` is a valid pivot-coordinate choice, not an invariant
naming claim.

This residual closes exactly in characteristic zero. Since

```text
486*((15+sqrt15)/54)^2-270*((15+sqrt15)/54)+35
  =(sqrt15^2-15)/6,
```

the maps `y -> (15+sqrt15)/54` and `sqrt15 -> 54y-15` identify
`Q[y]/(H_4)` with `Q(sqrt15)`. Thus this is an isomorphism of the abstract
coefficient fields, not a choice that loses the conjugate root. The complete
eight-generator input
`box/k16uniform-20260903/t4_exact_Qsqrt15_nfmodstd.sing` has SHA-256
`6b2f8f0eafe2792b99ede7d902504a34a9a8ce7096df7d948b441e97936421cf`.
Singular's exact number-field `nfmodStd` returns

```text
MAIN_START t=4 field=Qsqrt15 rows=8 vars=4 method=nfmodStd
MAIN_DONE basis_size=
1
MAIN_EXACT_UNIT
G[1]=1
```

in 0.82 s with 15,532 KiB maximum RSS and empty stderr. Its actual-pair,
`c`-unit, ring/type, and EMPTY/NONEMPTY controls pass separately in the
rational ambient ring, the coefficient ring, and the final residual ring.
Because every preceding pivot is a checked coefficient-field unit and the
weighted slice is equivalent on `c!=0`, this proves the exact t=4 chart empty.

The previously charged full-chart bases `[1]` over three good primes remain
**MEASURED-MODULAR** cross-checks only; they are not used to promote the
characteristic-zero conclusion.

## 4. The residual pattern and the exact blocker

### 4.1 What the finite systems actually say

The proposed statement

```text
six generators in (b3,b4,a2_0), bands 0,...,5, for every t
```

is false, not merely unproved. Both `t=1` and `t=2` are counterexamples to
that presentation; at `t=2`, `a2_0` is eliminated by the required gauge.

The exact `t=2,3,4` reductions instead exhibit the tentative linear pattern

```text
post-H/c input:       9t+2 rows in 6t+2 auxiliaries,
affine pivots:        5t+2,
zero/duplicate rows:  2t,
terminal:             2t rows in t variables,
bands:                0,...,2t-1,
degrees:              4t+1,...,2t+2.
```

This is exact for the three displayed integers, but is **not** promoted as an
all-`t` theorem. Residual coordinate names depend on the chosen valid pivot
sequence, and no closed second-spine recurrence has been proved.

### 4.2 Smallest proved uniform statement

The following much smaller statement is proved uniformly:

1. The banded chart, coefficient spaces, and three gauges are valid for all
   `t>=1` and contain no parameter denominators.
2. There are `3t+4` Q-constant quotient pivots, descending from band
   `4t+1` through band `2t`. The gauged chart has `9t+9` variables, so this
   leaves `6t+5` before the weighted slice.
3. The positive grading, equations (H) and (C), the `x=1` equivalence, and
   the c-unit statement in the separable algebra `A_t` hold for every
   positive integer `t`.
4. No fixed collection of low bands, or of low plus a fixed number of
   extreme-high bands, can supply a uniform unit certificate: the charged
   exact point
   `Q=h^q+B, P=h^e+2pi-gamma, c=-1` satisfies all low levels through
   `2t-1` and fails only at the moving bands `2t` and `3t+1`.

The missing object is the **second affine spine in the t-scaling middle**.
After passage to `A_t`, every proposed pivot coefficient is an element
`u_(t,j)(y)`. A uniform quotient-ring elimination must give a closed formula
or recurrence for these elements and prove, for every required band index and
every positive integer `t`,

```text
u_(t,j) is a unit in A_t
    iff Res_y(H_t,u_(t,j)) != 0.
```

For the displayed nonmonic `H_t`, the determinant norm and resultant differ
by a nonzero rational power of its leading coefficient (and possibly the
orientation sign), so only this nonvanishing equivalence is asserted. The
elimination must also prove the observed duplicate/zero recurrence and
identify the t-dependent
terminal ideal. The coefficient-space boundaries move at low band `t` and at
high offset `t`; this is precisely where the charts for `t` and `t+1` first
differ. Thus the normalizer is no longer the blocker. The t-dependent middle
system is.

## 5. Why a generic-`t` `[1]` is not presently available

There is no fixed six-by-three residual `R_t` to enter in
`Q(t)[y]/(H_t)`: the verified `t=2,3,4` terminal rings already refute that
fixed presentation and have observed growing sizes. One could encode the
systems by an indexed recurrence, but that recurrence is the open
second-spine problem just named. Consequently no generic Gröbner basis was
computed and no finite exceptional denominator set is asserted.

If a future recurrence or genuinely fixed reformulation does yield

```text
1=sum_i A_i(t,y,u) R_i(t,y,u)+B(t,y,u)H_t(y)
```

in `Q(t)[y,u_1,...,u_r]`, FALLACY-v2 requires clearing a common nonzero denominator
`D(t)`. The certificate specializes only when `D(t0)` and the leading
coefficient of `H_t0` are nonzero. Every inverted `A_t` coefficient must
contribute its norm/resultant to `D`, and every integer root of `D` must be
handled exactly.

The infinite split set `t=3s^2-1` is not a finite denominator-exception set.
Splitting itself does not invalidate an algebra identity: one specializes in
the product algebra and checks the recorded resultants. What is invalid is to
call every specialized quotient a field or silently invert a zero divisor.
This is the required FALLACY-v2 distinction between a generic identity and
its specializations.

## 6. Controls and theorem status

Every accepted full-chart exact run extracts the ideal component returned by
`sat()`, asserts its type and declared ring, and passes both controls

```text
EMPTY:    <c>:<c>^infinity = <1>,
NONEMPTY: <c-1>:<c>^infinity != <1>,
```

or their equivalent Rabinowitsch presentations. Every normalized ring first
proves the displayed image of `c` is a unit and repeats positive and negative
wrapper controls in that declared coefficient ring. No completed output has a
CAS error marker; files used to capture `/usr/bin/time` contain resource data,
not a silent algebra failure.

The semantic negative classifier is

```text
(F,G)=(pi,pi-gamma^2/2), J(F,G)=gamma.
```

It passes both reciprocal quadratic-anchor shapes, but its pi-degrees are
`(1,1)` and it has none of the K=16 degree/tuple data. Hence it fails the
tuple and is never inserted as a target-chart point.

Monic h-division keeps zero remainders and never divides by a
parameter-dependent leader. Prime marks remain labels unless the source
defines differentiation. No cv flag, place, or series is identified; no
carrier or attainment assertion is made. No exit set or exit price is
asserted, so no `charge_basis=...` line is due.

The fixed rows now have the following status:

- `t=1`: **PROVED-HERE**, exact normalized unit and full-chart `[1]`.
- `t=2`: **PROVED-HERE**, both exact split fibers and full-chart `[1]`.
- `t=3`: **PROVED-HERE**, exact six-generator quadratic-field `[1]` replay.
- `t=4`: **PROVED-HERE**, exact eight-generator `Q(sqrt15)` basis `[1]`.
- all `t>=1`: **PARTIAL / OPEN[T-UNIFORM-MIDDLE]**.

The bounded next step is to prove the second affine recurrence by induction on
the band index, recording every pivot norm, then prove or refute the observed
`2t`-row/`t`-variable terminal family and seek a terminal recurrence ending in
a nonzero coefficient-algebra constant. Finite additional samples cannot
replace that induction.

## 7. Principal reproduction

From `/home/ubuntu/jc2`:

```text
cd box/k16uniform-20260903 && sha256sum -c t2_t1_charged.sha256 && cd ../..
python3 box/k16uniform-20260903/t2_t1_normalized_audit.py
python3 box/k16uniform-20260903/t3_normalization_replay.py
Singular -q box/k16uniform-20260903/t3_normalized_K_std.sing
Singular -q box/k16uniform-20260903/t3_RK_wrapper_controls.sing
python3 box/k16uniform-20260903/t4_normalization_probe.py
Singular -q box/k16uniform-20260903/t4_exact_Qsqrt15_nfmodstd.sing
python3 box/k16uniform-20260903/uniform_binomial_identities.py
python3 box/k16uniform-20260903/uniform_extract_normalizers.py 1 2 3 4
```

Detailed generator sets, pivot inverses, row maps, commands, controls, outputs,
resource records, and SHA-256 manifests are under
`box/k16uniform-20260903/`; `SHA256SUMS.final` indexes the complete top-level
artifact bundle. The supporting audits are
`t2_t1_audit.md`, `t3_normalization_audit.json`,
`t4_normalization_audit.json`, `t4_affine_audit.json`,
`t4_modular_audit.md`, and `uniform_pattern_audit.md`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `22457`.
- Body SHA-256:
  `ba665247c6f756058479d155fab641e45e813f5280c823d09874ca857fc95ae4`.
- Frozen basis: `b4c4f418badef480d568ae60eff680c09cca7aee`.
