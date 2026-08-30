# Complete generic-K00 `e=3,m=2` rank/transition fan through G12

Date: 2026-08-30  
Author: Sol 5.6 Ultra  
Frozen campaign basis: `0d7544ebd5cb12def6bac892646010301098be3c`  
Status: **EXACT PRODUCER / COMPLETE FIELD-VALUED POINT FAN / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

Work over an algebraic closure of a characteristic-zero field, after the
licensed Gaussian/Kummer extensions, on the normalized generic K00 ray

```text
Lambda=tau^3,        ord_tau(d)=2,       C6=1,
k10[0] != 0,         Jdet[0] != 0,
k6,k2,mu2,mu4,mu6 in tau*K[[tau]] or identically zero.       (0.1)
```

Then the seven literal source rows have no field-valued solution through
grade G12.  More exactly,

```text
V(G0,...,G12) intersect D(k10[0])
                intersect (union_i D(d_i[2])) = empty.        (0.2)
```

After the first rank-zero recentering, the leading-order open in (0.2) is
`D(s) union D(t)`.  The nonplane G4 ranks are killed before making that
replacement.  Thus every positive or infinite boundary load-order face in
the exact normalized cell is point-set empty.  Any formal solution in this
cell would truncate to a G12 point and is therefore excluded.  No converse
lifting or reachability assertion is used.

The complete transition tree is

| first normal order | rank | last compatible grade | exact decision |
|---|---:|---:|---|
| `n=2` | 2 | G5 tangent | dead at G6 |
| `n=2` | 1 | G5 tangent | dead at G6 |
| `n=2` | 0 | G5 | recenter to `n>=3` |
| `n=3` | 2 | G7 tangent | dead at G8 |
| `n=3` | 1 | G8 | dead at G9 |
| `n=3` | 0 | G7 | recenter to `n>=4` |
| `n=4` | 2 | G9 tangent | dead at G10 |
| `n=4` | 1 | G11 can survive | dead at G12 |
| `n=4` | 0 | G9 tangent | recenter at G10 to `n>=5` |
| `n=5` | 2 | G11 tangent | dead at G12 |
| `n=5` | 1 | G11 tangent | dead at G12 |
| `n=5` | 0 | G11 | dead at G12, including `ord(N)>5` |

The G4--G9 part is consistent with, but is not imported from, the neighboring
`e=2,m=2` and reviewed `e=3,m=1` packets.  Every row in this report is
re-extracted from the literal `e=3` source.  The new G10--G12 closure is
producer evidence until hostile review.

## 1. Frozen source, exact calendar, and replay

The charged bytes are

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  frozen tails.json, 569 monomials
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  compile_contracted_source_v20r2.py
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  exact sparse Q(i) engine
22e9752761f3bb4ee94b4dccf18cb72ff49bd0d92453ad4cf39eb401cc45f84a
  sealed e3m1 complete-fan producer, regression only
bcd4004e671091c7d1ffc265affbd160b1d2b2a712f62dd97b698150dfc9fcba
  e3m1 complete-fan replay, regression only
0f7c18eb06dc2451fd4db668de7682a5d59f1c734509402b2537790b0408db87
  Opus hostile review of e3m1, regression only
6c7195218dcdac680d260d2db3e7bcff197a2ba7ee09055a8e6f67884ce27a38
  promoted e3m1 coordinator integration, regression only
fa5a4ef6a1b2c0640c6363b84e6b547a044920b15249f7c72b25ffbcda2c1733
  sealed e2m2 complete-fan producer, regression only
efd2f4fea4f58ee4783d9b373ee68f2ff191a9923b08bf2ead8dd1c59a4d3749
  e2m2 complete-fan replay, regression only
7cbc45a13d84c7921e7548c7229fcd28e8c28cdd4ff6a11c4c5643b24e426a33
  xmodel/k00-ram-e3m2-g0-g12-complete-rankfan-replay-sol56-20260830.py
```

The literal `e=3` source begins

```text
R(d)+tau^6*k10(tau)*A10(d)+tau^18*k6(tau)*A6(d)
    +tau^30*k2(tau)*A2(d)-targets.                  (1.1)
```

For `ord(d)=2`, the honest lower calendar is

| sector | rows | nominal/actual first grade |
|---|---|---:|
| unloaded `R` | rows 1--5,7 | G4 |
| unloaded `R` | row 6 | G6 |
| K10 globally | all rows | nominal G10 |
| K10 on the exact surviving surface | rows 1--3,5,7 | actual G12 |
| K10 on the exact surviving surface | row 6 | G14 |
| K10 on the exact surviving surface | row 4 | identically zero |
| K6 | rows 1--3,5,7 | G21 |
| K6 | rows 4,6 | G23 |
| K2 | all rows | G33 |
| `mu2,mu4,mu6,Jdet` | target rows | G43,G49,G55,G57 |

The nominal K10 G10 is not an actual collision.  On every branch surviving
G9, the leading coefficient is the exact tangent plane `ell(s,t)`, and

```text
A10^[2](ell(s,t))=0.                               (1.2)
```

The replay retains arbitrary `S3,T3` and verifies the complete raw K10
coefficients at degrees four and five are zero, so G10 and G11 receive no
K10 term.  At raw degree six the exact surface rows begin with

```text
W1=(5/4096)t(3s^2-64t^2),
W2=(5/65536)s(s^2-192t^2),                         (1.3)
```

and the remaining rows are their literal companions.  These produce the
first actual K10 collision at G12.  On the `n=4` rank-one support, the
possible normal part of that collision vanishes in row six; the decisive
row-six obstruction there is unloaded.

Run

```text
python3 -B xmodel/k00-ram-e3m2-g0-g12-complete-rankfan-replay-sol56-20260830.py
python3 -B -O xmodel/k00-ram-e3m2-g0-g12-complete-rankfan-replay-sol56-20260830.py
```

Both modes print identically:

```text
K00_RAM_E3M2_G0_G12_COMPLETE_RANKFAN_REPLAY=PASS
TAIL_TERMS=569
CALENDAR=K10_NOMINAL_G10_BUT_EXACT_G10_G11_ZERO;FIRST_ACTUAL_G12;K6_G21_G23;K2_G33;TARGETS_G43_G49_G55_G57
G4_N2=RANK2_RANK1_DEAD_G6;RANK0_TO_N3
G6_N3=RANK2_DEAD_G8;RANK1_DEAD_G9;RANK0_TO_N4
G8_N4=RANK2_DEAD_G10;RANK1_G10_SURVIVOR_DEAD_RAW_G12;RANK0_TO_N5
N4_G12_ROW6=EPS*i*q^3/32;ALL_S3_T3_S4_T4_N5_N6_N7_N8_K10_RETAINED
G10_N5=RANK2_RANK1_RANK0_ALL_DEAD_G12
N5_G12_RANK1=-EPS*5*i*k10[0]*t^3/16;RANK0=Q(N6)+k10[0]*W_EMPTY
FIXTURES=N4_G0_G11_PASS_G12_FAIL;N5_K10_OFF_PASS_ON_FAIL
CELL_STATUS=POINT_SET_EMPTY_THROUGH_G12_ON_C6_K10_JDET_OPENS
CERTIFICATE_BYTES=5968
CERTIFICATE_SHA256=6ae3c1d9c7a51add533f08fcc4a23ea791a7cac9724add25d785380046007c70
MUTATIONS=CUSTODY,CALENDAR,N4_-128_TO_-127,N4_ROW6,N5_K10_OPEN,DELTA_64,W2_192
```

The deterministic 5,968-byte JSON certificate is rebuilt in memory.  The
replay uses only Python stdlib exact rational/Gaussian-rational arithmetic,
takes about eleven seconds in either mode, and writes no files.  No CAS or
AWS computation is used.

## 2. Exact surface, recentering, and common cone fan

The seven unloaded rows and all 42 first derivatives vanish identically on

```text
D(S,T)=(2S+S^2,(1+S)T/8,S+16T^2,T,S,2T).           (2.1)
```

Thus a single normal coefficient never contributes by itself.  Write

```text
d(tau)=D(S(tau),T(tau))+N(tau),
S=s*tau^2+alpha*tau^3+gamma*tau^4+...,
T=t*tau^2+beta*tau^3+eta*tau^4+...,
(s,t)!=(0,0).                                      (2.2)
```

At every rank-zero transition, the tangent-plane part of the next normal
coefficient is absorbed into the corresponding next coefficient of `(S,T)`.
All later coefficients remain arbitrary.  This is a coordinate change, not
deletion of an odd column.

For every fresh order `n=2,3,4,5`, direct literal extraction gives

```text
G(2n)=Q(w),             G(2n+1)=DQ(w)[v].          (2.3)
```

The exact K10 G10/G11 cancellation is included in (2.3).  On reduced
geometric support,

```text
w=ell(a,b)+(2p,0,0,q,-p,4q),
Delta=p^2+64q^2.                                   (2.4)
```

The plane is absorbed.  `DQ(w)` has rank two on `D(Delta)`, rank one on
`Delta=0,(p,q)!=(0,0)`, and rank zero at `p=q=0`.  The rank-one charts are

```text
p=epsilon*8i*q, q!=0,
B(v)=epsilon*8i*A(v),       epsilon in {+1,-1},     (2.5)
```

where

```text
A(v)=v5+16v1-4v3,       B(v)=v0-4v2+2v4.           (2.6)
```

At the surface-normal compatibility grade, put

```text
C=t(64q^2-p^2)+2spq,
E=s(64q^2-p^2)-128tpq.                              (2.7)
```

At G8, G10, and G12, as applicable, the replay rechecks

```text
det([alpha,beta,N] rows 1,2,3)=(27/2^35)*Delta*C,
compatibility row 4                 =(3/2^15)*E.    (2.8)
```

Here `alpha,beta` are the two `DQ(w)` column forms associated to `A,B`;
they are not the odd surface coefficients carrying the same mnemonic names
in (2.2).

The determinant of `(C,E)` in `(s,t)` is `-Delta^2`.  Rank two therefore
forces `s=t=0` and is impossible on the normalized leading-order open.

On a rank-one chart, writing `X=A(v)`, two compatibility equations are

```text
F3= epsilon*(3i/2048)X^2 +(3/16)tq^2
      +epsilon*(3i/128)sq^2,

F4=-(3/4096)X^2-epsilon*(3i/32)tq^2+(3/256)sq^2.   (2.9)
```

They force, over a field on `D(q)`,

```text
s=epsilon*8i*t,        X=0.                        (2.10)
```

These identities are re-extracted separately at each transition; no
coefficient-blind induction is asserted.

## 3. G4 and G6 cones: closure through the `n=3` transition

At the first G4 cone, rank two reaches G6.  Its row-six equation is

```text
G6_6=p(192q^2-p^2)/65536.                          (3.1)
```

If `p=0`, row four forces `s=0`, while two exact cokernel equations demand
simultaneously `t=-8q/3` and `t=-4q`.  If `p^2=192q^2`, two exact reduced
cokernel combinations are the nonzero constants `1/8` and `-1/64`.
Thus rank two is empty.  On either rank-one chart,

```text
G6_6=epsilon*i*q^3/32,                              (3.2)
```

so rank one is empty.  Rank zero recenters to the fresh G6 cone.

For `n=3`, rank two dies at G8 by (2.8).  Rank one has a genuine G8
constructible support described by (2.10) and

```text
B(N5)-epsilon*8i*A(N5)=-128tq.                     (3.3)
```

Every odd surface slot, four tangent-kernel coordinates, and the complete
next normal block are retained.  The literal G9 row six is nevertheless

```text
G9_6=epsilon*i*q^3/32.                              (3.4)
```

Rank zero recenters to the fresh G8 cone.  This reproduces the neighboring
fan only after direct `e=3,m=2` extraction.

## 4. The new `n=4` G10 survivor and unloaded G12 kill

For the fresh G8 cone, rank two dies at G10 by (2.8).  On either rank-one
chart, G9 imposes the tangent relation in (2.5), while G10 imposes (2.10).
After those equations, every G10 row is its displayed scalar multiple of
`qH`, where

```text
H=B(N6)-epsilon*8i*A(N6)+128tq.                    (4.1)
```

Thus G10 has a genuine rank-one survivor with `H=0`.  Retain arbitrary
`S3,T3,S4,T4`, all four kernel coordinates in each normal block, all six
coordinates of `N7,N8`, and every K10 coefficient capable of arrival.
G11 may impose further equations, but row six vanishes there and at G12 is
identically

```text
G12_6=epsilon*i*q^3/32.                             (4.2)
```

This expression is independent of every retained lift and of K10.  The raw
K10 row-six coefficients through degree six are identically zero.  Hence
every possible G11 survivor dies at G12.

The stop is sharp.  For `epsilon=+1`, the literal fixture

```text
S=8i*tau^2,             T=tau^2,
N4=(16i,0,0,1,-8i,4),   N5=0,
N6=(-128,0,0,0,0,0),    N7=N8=0,
k10=1                                                   (4.3)
```

passes every row in G0--G11 and has `G12_6=i/32`.  Replacing `-128` by
`-127` makes G10 nonzero.  This old-pass/new-fail pair independently tests
the G10 affine lift and proves that G12, rather than G10 or G11, is the
honest terminal for this fixture.

At rank zero, the replay verifies row by row that G10 is exactly

```text
Q(N5)=0.                                           (4.4)
```

The tangent-plane part of `N5` is absorbed, so (4.4) is precisely the fresh
`n=5` cone.  This is an independently replayed recentering, not an inference
from the `n=4` rank-one branch.

## 5. Fresh `n=5` cone and delayed loaded G12 closure

Let `w=N5`, `v=N6`, and `u=N7` after recentering.  Literal extraction gives

```text
G10=Q(w),              G11=DQ(w)[v],

G12_r=DQ_r(w)[u]+Q_r(v)
       +(1/2)D^2 R_r^[3](ell)[w,w]+k10[0]*W_r(s,t). (5.1)
```

`S3,T3,k10[1],k10[2]` are retained and verified absent from G12.  There is
no K10 normal term in (5.1): `ell` has order two and `w` order five, so that
term first has raw degree seven and reaches G13.  Equation (5.1) is the first
actual delayed-load gate.

For rank two, the G11 tangent condition gives `A(v)=B(v)=0`, and (2.8)
again forces `s=t=0`.  Rank two is empty.

For rank one, (2.9) forces (2.10).  A remaining exact cokernel combination
is

```text
G12_2+(epsilon*i/2)G12_1
    =-epsilon*(5i/16)*k10[0]*t^3.                  (5.2)
```

Here `q!=0`, and `(s,t)!=(0,0)` together with (2.10) gives `t!=0`.
The K10-unit open therefore makes (5.2) nonzero.

For rank zero, G11 vanishes and (5.1) is

```text
Q(N6)+k10[0]*W(s,t)=0.                              (5.3)
```

Write `A=A(N6)` and `B=B(N6)`.  Row four and an exact split combination are

```text
G12_4=(3/524288)(B^2-64A^2),

B=delta*8A  =>  G12_3+(1/8)G12_1
                    =delta*(3/2048)A^2,            (5.4)
```

with `delta=+1` or `-1`.  Thus `A=B=0`, every quadratic row vanishes, and
(5.3) reduces to `k10[0]W=0`.  The two rows in (1.3) have no common zero on
`D(s) union D(t)`: the coordinate-axis cases are immediate, while on
`D(st)` they require both `s^2=64t^2/3` and `s^2=192t^2`.  Rank zero is
empty, including `ord(N)>5`.

The K10 dependence is independently mutation-tested.  The fixture

```text
S=8i*tau^2,             T=tau^2,
N5=(16i,0,0,1,-8i,4),   N6=0,
N7=(-128,0,0,0,0,0)                                 (5.5)
```

passes all rows through G12 when `k10[0]=0`.  It passes G0--G11 but fails
G12 when `k10[0]=1`.  Thus deleting the unit open really changes the final
fan; the loaded terminal is not decorative.

## 6. Completeness and maximum safe scope

The replay retains every coefficient capable of reaching a decision grade:

1. `S2,T2,S3,T3` throughout; `S4,T4` on the `n=4` G12 branch;
2. complete normal blocks through `N8` on that branch and through `N7` on
   the `n=5` branch;
3. `k10[0],k10[1],k10[2]`, with the latter two verified absent; and
4. every odd/tangent/kernel coordinate before imposing a rank-chart
   equation.

Later surface or normal coefficients first reach G13 or beyond by the exact
deviation-grade census.  K6, K2, and the four targets lie strictly beyond
G12 by the literal calendar; they are not set to zero inside the relevant
window.

The replay fails closed on custody drift, a false G10/G11 K10 arrival, the
G10 affine-lift mutation `-128 -> -127`, deletion of the raw G12 row-six
terminal, deletion of the K10-unit open, changing `64` in the cone
discriminant, or changing `192` in W2.

The theorem is exactly the field-valued finite-jet emptiness (0.2) for the
normalized generic K00 `e=3,m=2` cell.  Reduced cone parameterizations and
Gaussian splittings are used only set-theoretically.  No ideal equality,
multiplicity statement, nilpotent lifting, scheme-valued normal form,
all-ramification induction, source completeness theorem, or statement about
another K00 support follows.

Apart from the one-way truncation consequence for a hypothetical formal
solution in this exact cell, no assertion is made about arc existence,
converse lifting, source reachability, attainment, algebraization, a
polynomial map, another ramification pair, or JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14872`.
- Body SHA-256:
  `06ccbd8b31293874a18a21011cf469e55f25abb349133ad359a1645aab1a1eb7`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
