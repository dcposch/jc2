# First exact attack on `K00-V20R2-RAM-E2-M1-B11111/v1`

Date: 2026-08-29  
Author: Sol 5.6 Ultra  
Frozen campaign basis: `31777ce90994a106aade85064c0d868e32863f94`  
Status: **EXACT G3 RANK KILL / TYPED G5 RESIDUAL / REVIEW-GATED**

## Result

For the first ramified source cell

```text
Lambda=t^2,  ord_t(d)=1,
ord_t(k10)=ord_t(Jdet)=0,
ord_t(k6)=ord_t(k2)=ord_t(mu2)=ord_t(mu4)=ord_t(mu6)=1,
```

the literal grades two and three are exactly the already promoted unloaded
K00 prefix.  Therefore the complete promoted grade-three incidence theorem
applies verbatim: every compatible leading point of nonzero matrix rank is
empty, and the only surviving leading base is

```text
x=d[1]=ell(s,t)=(2s,t/8,s,t,s,2t),       (s,t)!=(0,0). (0.1)
```

This is not a periodicity inference.  It is equality of the source
polynomials: the ramified K10 load first has generic grade six, K6 first has
generic grade fourteen, K2 first has generic grade twenty-two, and every
target is later, so grades two and three contain only the same frozen
unloaded rows.

The rank-zero branch survives.  Its exact next two equations are

```text
u=d[2],
mu(s,t)=(s^2,st/8,16t^2,0,0,0),
w=u-mu(s,t),

G4_r = Q_r(w),
G5_r = DQ_r(w)[v] + (1/2)D^2 c3_r(ell)[w,w],
v=d[3],                                            (0.2)
```

for all seven rows.  The coefficient `d[4]` is free through grade five.
There is an exact prefix witness

```text
s=1, t=0, w=0, v=0, d[4]=0,                        (0.3)
```

with all required late-source unit opens chosen nonzero.  Thus this attack
kills the nonzero leading-rank strata but does not kill the whole ramified
cell.

## 1. Frozen source and replay

The source-complete grade-38 packet is

```text
98fb38535405f1cc853dd4d430e26876a84f6f97c538f862f18a0446c0c97ecf
  xmodel/k00-v20r2-valuative-comparison-v1-sol56-20260829.md.
```

It pins `273=7*39` grade-major equations, 331 labelled columns, 326 free
columns after the five boundary-zero columns, and 316 columns that can occur
through grade 38.  The ten remaining free labelled columns are retained and
certified inert at this cutoff.  Thus the small prefix below is a restriction
of a source-complete packet, not a replacement for its later equations.

The new exact stdlib replay is

```text
b4fd505d0345b21a2978f06ff63cb0c9fcacd9d7226d7accaa0b2ab489b210ea
  xmodel/k00-ram-e2m1-g5-prefix-replay-sol56-20260829.py.
```

It pins the prior exact arithmetic engine, freshly reconstructs the 569 tail
monomials through that engine, verifies the normal-degree stencil, substitutes
the source series directly, and checks (0.1)--(0.3) over exact rationals.  It
is a same-engine exact replay, not a different-implementation review.
Ordinary and optimized Python both print

```text
K00_RAM_E2M1_G5_PREFIX_REPLAY=PASS
TAIL_TERMS=569
G2_G3_SOURCE=IDENTICAL_TO_PROMOTED_UNLOADED_PREFIX
LEADING_NONZERO_MATRIX_RANKS=EMPTY_AT_G3
SURVIVING_LEADING_BASE=Pi_MINUS_ORIGIN
G4_IDENTITY=Q(u-mu)
G5_IDENTITY=DQ(w)[v]+1/2*D2c3(ell)[w,w]
K10_G6_ON_PI=ZERO;K10_FIRST_POSSIBLE_ON_RESIDUAL=G7
K6_G14_ON_PI=ZERO;K6_FIRST_POSSIBLE_ON_RESIDUAL=G15
K2_FIRST_POSSIBLE_ON_RESIDUAL=G22
CALENDAR_WITNESS_ROW2=K10_G7:5/32768,K6_G15:3/2048,K2_G22:1/32
PREFIX_WITNESS=s=1,t=0,w=0,v=0,p=0
RESIDUAL_BYTES=26852
RESIDUAL_SHA256=f471559d53c25ca40a60bb3d01241ff7186e581bcc383433b6a5163ffd07b691
MUTATIONS=CUSTODY,CUBIC,MU,K10_SCALE,K6_RESTRICTION,ODD_COLUMN_DROP
```

The 26,852-byte residual is a deterministic canonical JSON serialization
rebuilt in memory; it is not an untracked scratch file.  It contains every
G4/G5 polynomial, the two reduced G4 forms, source pins, opens, and the
remaining grade interval.

## 2. Leading cone and rank stratification

For `q=(q0,...,q5)` put

```text
A(q)=16q1-4q3+q5,        B(q)=q0-4q2+2q4.
```

The reduced zero locus of the seven leading quadrics `Q_r(x)` is
`A(x)=B(x)=0`, parameterized without quotienting scale by

```text
x=(2b+2u,a,b,8a+v,b-u,16a+4v).                     (2.1)
```

On this cone, `DQ(x)` has rank zero, one, or two.  Its four nonzero
two-by-two minors are nonzero rational multiples of

```text
Delta=u^2+64v^2.
```

Thus the exact field-valued fan is

```text
rank 2: Delta!=0;
rank 1: Delta=0 and (u,v)!=(0,0);
rank 0: u=v=0.
```

No rank at least three occurs on the leading base.  At grade three the rows
are exactly

```text
P3(x,u2)=DQ(x)[u2]+c3(x).                           (2.2)
```

The promoted complete incidence theorem for these same polynomials proves
set-theoretically over an algebraic closure that ranks two and one are empty
and that the compatible rank-zero locus is precisely (0.1), with `u2` free.
The exact source equality, the source hashes, and absence of every load and
target at G2/G3 are replayed before that theorem is consumed.  No result from
valuation two, four, or five is transferred.

## 3. Exact G4/G5 residual

After (0.1), direct expansion of the frozen unloaded rows gives the
generatorwise identity

```text
[t^4]Psi_r = Q_r(u-mu)=Q_r(w).                      (3.1)
```

The whole `d[3]` block disappears at this grade because `DQ(ell)=0`.  The
scheme `(Q_1(w),...,Q_7(w))` is proper and nonreduced.  Its reduced support
is the linear four-plane

```text
A(w)=0,        B(w)=0.                              (3.2)
```

The scheme equations (3.1), not merely (3.2), are retained in the residual.

At grade five, direct coefficient extraction gives

```text
[t^5]Psi_r
 = DQ_r(w)[v] + (1/2)D^2 c3_r(ell)[w,w].           (3.3)
```

There is no K10 term: in this ramified cell `t^4*k10*A10(d)` begins
generically at grade six.  Formula (3.3) is also obtained by deleting the
load term from the promoted valuation-one G5 identity, but the replay proves
it independently from the tails and does not use that deletion as evidence.
The newest coefficient `d[4]` again disappears because it is multiplied by
`DQ(ell)`.

Putting `w=v=0` makes (3.1)--(3.3) vanish.  With `s=1,t=0`, equation (0.1)
has exact transverse order one, proving the compatible prefix (0.3).  This
is formal finite data only.

## 4. Sharpened source calendar and typed successor

On the surviving plane the exact K10 quadratic satisfies

```text
M4_r(ell)=0             for all seven rows.
```

Therefore its generic grade-six arrival vanishes on the residual.  At least
one polarization `DM4_r(ell)[u]` is nonzero, so K10 is first **possible** at
grade seven.  There is a second plane cancellation:

```text
L6_r(ell)=0             for all seven rows.
```

Hence the generic G14 K6 arrivals all vanish after restriction to the
surviving leading plane.  At G15 the exact coefficient for `k6[1]=1` is

```text
L6_r(u)+A6_r^[2](ell),
```

and is nonzero on the residual.  In contrast, the K2 linear piece is already
nonzero on the leading plane at G22.  The restricted first-possible calendar
is therefore:

```text
K10:       first possible G7 on this residual;
K6:        generic G14 cancels in every row; first possible G15;
K2:        first possible G22;
mu2,mu4,mu6,Jdet targets: G29,G33,G37,G38.
```

These are sharp as polynomial restrictions.  At the exact residual point
`s=1,t=0,w=v=d[4]=0`, after setting the relevant leading source unit to one,
the row-2 load-sector coefficients are respectively

```text
K10/G7 = 5/32768,      K6/G15 = 3/2048,      K2/G22 = 1/32. (4.1)
```

The full literal sequential calendar through the cutoff is thus unloaded at
G2--G5; unloaded plus K10 from G6 (with its first restricted nonzero at G7);
K6 generically from G14 but restricted first at G15; K2 from G22; then the
four targets at G29, G33, G37, and G38.  All intervening coefficients and
all rows remain governed by the pinned source rather than by a periodicity
claim.

The minimal typed successor is

```text
K00-V20R2-RAM-E2-M1-B11111-G5-RESIDUAL/v1:

x=ell(s,t),                         (s,t)!=(0,0),
u=mu(s,t)+w,
Q_r(w)=0,                           r=1,...,7,
DQ_r(w)[v]+(1/2)D^2c3_r(ell)[w,w]=0, r=1,...,7,
d[4] free through G5,
the pinned compiler/tails define every literal source equation G6,...,G38,
k10[0]k6[1]k2[1]mu2[1]mu4[1]mu6[1]Jdet[0]!=0.
```

The cheapest next solve is a rank/Fitting split of (3.3) over the exact G4
scheme, followed by the corrected K10 G7 equation.  Radical-first is valid
only for geometric existence; the nonreduced G4 scheme must be retained for
tangent, lifting, and multiplicity claims.  If this sequential elimination
ceases to be desk-scale, its complete source and mutations must be frozen
before an exact-Q AWS launch.

## 5. Replay and mutation controls

Run

```text
python3 -B xmodel/k00-ram-e2m1-g5-prefix-replay-sol56-20260829.py
python3 -B -O xmodel/k00-ram-e2m1-g5-prefix-replay-sol56-20260829.py
```

Both executions reproduce the residual bytes and digest above.  The replay
fails closed on:

1. any drift in the tails, V20R2 compiler, valuative packet, or promoted
   G3/G4 integrations;
2. adding `d0^3` to a cubic row, which breaks the G3 plane identity;
3. changing the `16t^2` entry of `mu` to `15t^2`, which breaks G4;
4. replacing the ramified K10 scale `t^4` by the unramified scale `t^2`,
   which creates a generic G4 load; and
5. perturbing the leading plane while retaining the claimed K6/G14
   cancellation, which makes the restriction error visible; and
6. deleting the odd `t` coefficient block, which erases the nonzero G2
   leading system and the exact `m=1` open.

These are source and semantic controls.  A final `PASS` string is not used as
evidence without the exact identities and custody checks.

## 6. Scope firewall

This report closes only the nonzero leading-matrix-rank strata of the first
ramified cell through grade three and emits its exact surviving prefix
through grade five.  It does not close grades 6--38, prove a point of the
full 273-equation cell, produce a formal arc, or show source incidence `H` is
proper.  The prefix witness is not a Taylor trajectory, rational section,
polynomial map, Keller pair, counterexample, or attainment.  No other
ramification, transverse valuation, load-order cell, K00 face, order-two,
maximum-twelve, or JC2 conclusion follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10078`.
- Body SHA-256: `0b6bb668ac1c3056338dbdf167d435c90bfde86765e9018834feeedc627de5df`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
