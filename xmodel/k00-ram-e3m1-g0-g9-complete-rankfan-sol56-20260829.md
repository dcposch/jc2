# Complete generic-K00 `e=3,m=1` rank/transition fan through G9

Date: 2026-08-29  
Author: Sol 5.6 Ultra  
Frozen campaign basis: `0f7ee003be45ee40d51d4048897cdacf63821172`  
Status: **EXACT PRODUCER / COMPLETE FIELD-VALUED POINT FAN / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

Work over an algebraic closure of a characteristic-zero field, after the
licensed Gaussian/Kummer extensions, on the normalized generic K00 ray

```text
Lambda=tau^3,        ord_tau(d)=1,       C6=1,
k10[0] != 0,         Jdet[0] != 0,
k6,k2,mu2,mu4,mu6 in tau*K[[tau]] or identically zero.       (0.1)
```

Then the seven literal source equations have no field-valued solution
through grade G9.  More exactly,

```text
V(G0,...,G9) intersect D(k10[0])
               intersect (D(s) union D(t)) = empty,           (0.2)
```

where `(s,t)` parameterizes the promoted leading plane.  Thus the complete
`e=3,m=1` generic-ray point fan closes at G9; there is no constructible G9
image to carry forward.  The conclusion holds uniformly over all positive
or infinite boundary load orders in (0.1), because those sectors are absent
through G9.

The complete transition tree is

| first transverse order | rank | last compatible grade | exact decision |
|---|---:|---:|---|
| `n=2` | 2 | G4 | dead at G5 |
| `n=2` | 1 | G5 | dead at G6 |
| `n=2` | 0 | G5 | recenter to `n>=3` |
| `n=3` | 2 | G6 | dead at G7 |
| `n=3` | 1 | G8 | both reduced components dead at G9 |
| `n=3` | 0 | G7 | recenter to `n>=4` |
| `n=4` | 2 | G8 | dead at G9 |
| `n=4` | 1 | G8 | dead at G9 |
| `n=4` | 0 | G8 | dead at G9, including `ord(N)>4` |

The G0--G3 leading-plane incidence is the promoted, independently reviewed
set-theoretic theorem.  The formerly provisional `e=3` G8 fixture has now
also received Fable's independent `CONFIRM_WITH_CORRECTIONS`; the corrections
were documentation/mutation issues, not mathematical failures.  Every G4--G9
transition in this report is nevertheless reconstructed afresh from the
literal source.  The new G9 closure remains producer evidence until hostile
review.

## 1. Frozen source and exact replay

The charged source bytes are

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  frozen tails.json, 569 monomials
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  compile_contracted_source_v20r2.py
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  exact sparse Q(i) engine
d453b9563d8f6cc23319d6bc0d8edce8a83f657b9e3a60cb244b00f181459860
  promoted G3 leading-plane integration
0eb501b414f2162d14a73725a46410b7e799adc70932cdfb8a05f4196ff0bb1a
  corrected G7 fan integration
0e7f98d165bf60531f675bae948315211fd08fd466f21f98aa399cd5fb12457b
  uniform rank-fan replay
0ee84a0b98d30c4436461a09118961706d1f18fcfe9686684e7b1a27b5597feb
  Fable hostile confirmation of the all-face theorem and e3 G8 fixture
3ef20945b4a009bba4dccbbf7a43461718feb8155e84f513f14c736ce45182e2
  first e3 rank-one G9 replay
bbe6ac2fa8ca7b53634e3c477d1cb2f4128e4e22e2a1cf5d4049db82402fe685
  first e3 rank-one G9 report
bcd4004e671091c7d1ffc265affbd160b1d2b2a712f62dd97b698150dfc9fcba
  xmodel/k00-ram-e3m1-g0-g9-complete-rankfan-replay-sol56-20260829.py
```

Through G9 the literal source is exactly

```text
R(d)+tau^6*k10(tau)*A10(d).                         (1.1)
```

K6 first can occur at G20, K2 at G32, and the four targets at G43,
G49, G55, and G57.  These are lower bounds, not exact-order assumptions.
The `Jdet[0]` open labels the cell but its equation does not enter this
truncation.

Run

```text
python3 -B xmodel/k00-ram-e3m1-g0-g9-complete-rankfan-replay-sol56-20260829.py
python3 -B -O xmodel/k00-ram-e3m1-g0-g9-complete-rankfan-replay-sol56-20260829.py
```

Both modes print identically:

```text
K00_RAM_E3M1_G0_G9_COMPLETE_RANKFAN_REPLAY=PASS
TAIL_TERMS=569
G0_G3=IMPORTED_PROMOTED_SET_THEORETIC_LEADING_PLANE
G0_G8_PREMISE=DIFFERENT_MODEL_CONFIRMED_WITH_DOCUMENTATION_CORRECTIONS
N2=RANK2_DEAD_G5;RANK1_DEAD_G6;RANK0_TO_N3
N3=RANK2_DEAD_G7;RANK1_G8_COMPONENTS_DEAD_G9;RANK0_TO_N4
N3_G9_ROW6=EPS*i*q^3/32;S3_T3_N6_RETAINED
N4=FRESH_G8_CONE;RANK2_RANK1_RANK0_ALL_DEAD_G9
OLD_FIXTURE=G0_G8_PASS;G9_FAIL;i/32
CELL_STATUS=POINT_SET_EMPTY_THROUGH_G9_ON_C6_K10_JDET_OPENS
CERTIFICATE_BYTES=17825
CERTIFICATE_SHA256=96279f6994f3af485913d33d3f0a175c582b02da450a0b344fb82fc65f2129a0
MUTATIONS=CUSTODY,OLD_PASS_FAIL,SURFACE_-4_TO_-3,DELTA_64,W2_192,K10_OPEN
```

The deterministic 17,825-byte JSON certificate is rebuilt in memory.  The
replay uses only Python stdlib exact rational/Gaussian-rational arithmetic
and takes about twelve seconds.  No CAS or AWS computation is used.

## 2. Exact recentering and the common rank fan

The seven unloaded rows vanish identically on

```text
D(S,T)=(2S+S^2,(1+S)T/8,S+16T^2,T,S,2T).           (2.1)
```

After the promoted G3 theorem, write

```text
d(tau)=D(S(tau),T(tau))+N(tau),
S=s*tau+...,  T=t*tau+...,  (s,t)!=(0,0).           (2.2)
```

At each rank-zero transition the tangent part of the next coefficient of
`N` is absorbed by the corresponding next coefficient of `(S,T)`.  The
later coefficient block remains arbitrary, so this is a coordinate change,
not deletion of a branch.  Direct literal extraction at `n=2,3,4` gives

```text
G(2n)=Q(w),                                         (2.3)
```

with the same seven raw quadrics.  On reduced geometric support,

```text
w=ell(a,b)+(2p,0,0,q,-p,4q),
Delta=p^2+64q^2.                                   (2.4)
```

The plane `ell(a,b)` is absorbed as above.  The rank of `DQ(w)` is two on
`D(Delta)`, one on `Delta=0,(p,q)!=(0,0)`, and zero at `p=q=0`.

For `n=2,3`, the literal grade `2n+1` fan is identical after recentering.
Put `X=A(v)`, `Y=B(v)`, with

```text
A(v)=v5+16v1-4v3,        B(v)=v0-4v2+2v4.          (2.5)
```

The rank-two compatibility forms are

```text
C=t(64q^2-p^2)+2spq,
E=s(64q^2-p^2)-128tpq,                              (2.6)

det([alpha,beta,N] rows 1,2,3)=(27/2^35)*Delta*C,
G(2n+1)_4=(3/2^15)*E.                              (2.7)
```

The determinant of the two equations `(C,E)` in `(s,t)` is `-Delta^2`.
Thus rank two forces `s=t=0` and is impossible.  Rank one has exactly the
two Gaussian charts

```text
p=epsilon*8i*q,  q!=0,
s=epsilon*8i*t,  t!=0,
Y-epsilon*8i*X=-128tq,     epsilon in {+1,-1}.      (2.8)
```

Every labelled odd-grade row vanishes after (2.8).  At rank zero every
labelled odd-grade row is zero and recentering advances `n` by at least one.
These three cases exhaust the reduced support of every fresh cone used here.

## 3. First transverse order `n=2`

The rank-two branch dies at G5 by (2.6)--(2.7).  Both rank-one charts survive
G5, with arbitrary second surface coefficients, four kernel directions in
the G5 lift, and arbitrary next normal coefficient retained.  At G6 the
following coefficient-blind labelled combinations are re-extracted:

```text
(3/128)G6_1+(1/8)G6_3+G6_5 = -q^3/16,
G6_6                              = epsilon*i*q^3/32,
(1/512)G6_1+(1/128)G6_3+G6_7 = q^3/128.            (3.1)
```

Thus rank one is impossible on `D(q)`.  Rank zero has no remaining G5
equation and recenters to the fresh G6 cone with `n=3`.

## 4. First transverse order `n=3`: all G8 components

Rank two dies at G7.  On either rank-one chart (2.8), retain

```text
S=epsilon*8i*t*tau+alpha*tau^2+gamma*tau^3+...,
T=t*tau+beta*tau^2+eta*tau^3+...,                  (4.1)
```

and let `X=A(N4)`.  Two exact G8 cokernel forms are

```text
F512=X^2-epsilon*48i*tq*X-512*t^2q^2
       +16alpha*q^2-epsilon*128i*beta*q^2,

F640=X^2-epsilon*48i*tq*X-640*t^2q^2
       -16alpha*q^2+epsilon*128i*beta*q^2,          (4.2)

G8_3+(1/8)G8_1 = epsilon*(3i/2048)*F512,
G8_4            = -(3/4096)*F640.                  (4.3)
```

Their exact factorization is

```text
F512-F640=32q^2(4t^2+alpha-epsilon*8i*beta),
F512+F640=2(X-epsilon*24i*tq)^2.                    (4.4)
```

Consequently the localized scheme pair generated by these two forms is

```text
(4t^2+alpha-epsilon*8i*beta,
 (X-epsilon*24i*tq)^2) on D(q).                    (4.5)
```

On its field-valued/reduced support,

```text
X=epsilon*24i*tq,
alpha-epsilon*8i*beta=-4t^2.                       (4.6)
```

Write `z=N5` and retain all four kernel coordinates `y1,...,y4` of `N4`.
Every remaining G8 row is its displayed nonzero scalar multiple of `qH`,
where

```text
Az=z5+16z1-4z3,
Bz=z0-4z2+2z4,

H=Bz-epsilon*8i*Az+128q*beta+epsilon*1088i*t^2q
  -512t*y1-epsilon*8i*t*y2+64t*y3+epsilon*8i*t*y4. (4.7)
```

Since `H` is monic in `z0`, each sign has exactly one reduced constructible
G8 component in this normal form, with a five-dimensional `z` fiber over
the free `beta` and `y` parameters.  The later surface parameters
`gamma,eta`, the complete `N6` block, and `k10[0..3]` are also retained;
they do not enter G8.

Direct extraction of the next literal coefficient gives

```text
G9_6=epsilon*i*q^3/32.                              (4.8)
```

It is independent of `beta,gamma,eta`, all four `y` directions, the full
five-dimensional G8 lift fiber, all six `N6` coordinates, and
`k10[0..3]`.  The K10 row-six coefficients capable of reaching G9 are
identically zero.  Hence both reduced G8 components are empty at G9 on
`D(q)`.

The banked fixture is the specialization

```text
epsilon=+1, t=q=k10[0]=1, beta=gamma=eta=y=0,
z=(-1088i,0,0,0,0,0).                              (4.9)
```

Literal evaluation again gives all 63 coefficients G0--G8 equal to zero,
then `G9_6=i/32`.  Thus the old pass remains a pass and its first failure is
located exactly.

At rank zero, the G7 equations vanish and exact recentering produces the
fresh G8 cone with `n=4`.

## 5. Fresh `n=4` G8 cone and final G9 fan

All three reduced ranks of `Q(w)=0` are G8-compatible.  The literal G9 rows,
with arbitrary second and third surface coefficients, full `N5`, an
arbitrary `N6` block, and `k10[0..3]` retained, are

```text
G9_r = DQ_r(w)[N5]
       +(1/2)D^2 R_r^[3](ell)[w,w]
       +k10[0]*W_r(s,t).                            (5.1)
```

No later coefficient in the retained blocks occurs.  The same exact
rank-two determinant and row-four identities (2.6)--(2.7) hold with the K10
term included.  Therefore rank two again forces `s=t=0`.

At rank one, (2.8) holds and the coefficient-independent cokernel is

```text
G9_2+(epsilon*i/2)G9_1
   =-epsilon*(5i/16)*k10[0]*t^3.                   (5.2)
```

It cannot vanish on the chart.  The `k10[0]` open is load-bearing here.

At rank zero, the unloaded and newest-coefficient blocks vanish, leaving
`G9=k10[0]*W`.  Two rows are

```text
W1=(5/4096)t(3s^2-64t^2),
W2=(5/65536)s(s^2-192t^2).                          (5.3)
```

Their only common zero is `(s,t)=(0,0)`: if either coordinate is zero the
other row kills the remaining coordinate, while on `D(st)` the two equations
would require simultaneously `s^2=64t^2/3` and `s^2=192t^2`.  This also
kills the subbranch with `ord(N)>4`.  The table in section 0 is exhaustive,
proving (0.2).

## 6. Coefficient, scheme, and lifecycle discipline

For the `n=3` G9 coefficient, the only surface coefficients that can enter
are `S1,T1,S2,T2,S3,T3`; the only normal coefficients that can enter are
`N3,...,N6`.  All are retained symbolically.  `S4,T4` and `N7` first can
reach G10, so their absence is an exact truncation statement rather than a
coefficient-blind recurrence assumption.  The fresh `n=4` calculation also
retains second/third surface coefficients, `N6`, and `k10[0..3]` and verifies
their literal absence from G9.

The promoted G3 theorem and every cone parameterization are used only for
geometric points over an algebraic closure.  Equation (4.5) records the
visible nonreduced double-root thickness, but this report does not identify
the full G8 ideal scheme-theoretically, transport multiplicities through the
normal form, or prove a formal lifting statement.  Point-set emptiness is
legitimate because every possible field-valued point lies on one of the
enumerated reduced-support charts.

The replay fails closed on source drift and on these semantic controls:

1. the old fixture passes G0--G8 and fails at G9;
2. changing its propagated second surface coefficient from `-4` to `-3`
   makes G8 nonzero;
3. changing `64` in the transverse discriminant to `63` breaks the rank
   determinant identity;
4. changing `192` to `191` in `W2` is detected; and
5. setting `k10[0]=0` deletes the final rank-one terminal, verifying that
   the declared open is load-bearing.

This packet is an exact producer and must receive different-model hostile
reconstruction before promotion.  Stop or narrow it if review changes the
literal source hashes, the `Lambda=tau^3` or K10 shift convention, the
leading-plane incidence, the exact surface recentering, any rank chart, or
either G9 terminal.

No statement is made about scheme equality, formal arcs, source
reachability, attainment, algebraization, polynomial maps, another
ramification pair, or JC2.  A finite-jet exclusion is not an arc theorem or
a global source classification beyond the exact cell and opens in (0.1).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13038`.
- Body SHA-256:
  `2e3086f577cc4e0b228cfe55df92413ca749e0b3230ddb71208735b49809bc8e`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
