# Complete generic-K00 `e=2,m=2` rank/transition fan through G10

Date: 2026-08-29  
Author: Sol 5.6 Ultra  
Frozen campaign basis: `0f7ee003be45ee40d51d4048897cdacf63821172`  
Status: **EXACT PRODUCER / COMPLETE FIELD-VALUED POINT FAN / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

Work over an algebraic closure of a characteristic-zero field, after the
licensed Gaussian/Kummer extensions, on the normalized generic K00 ray

```text
Lambda=tau^2,        ord_tau(d)=2,       C6=1,
k10[0] != 0,         Jdet[0] != 0,
k6,k2,mu2,mu4,mu6 in tau*K[[tau]] or identically zero.       (0.1)
```

Then the seven literal source rows have no field-valued solution through
grade G10.  More exactly,

```text
V(G0,...,G10) intersect D(k10[0])
                intersect (union_i D(d_i[2])) = empty.        (0.2)
```

After the first rank fan, the only surviving branch has
`union_i D(d_i[2]) = D(s) union D(t)`; the nonplane G4 branches are killed
before that replacement is made.
Thus every positive or infinite boundary load-order face of the
`e=2,m=2` generic-ray cell is point-set empty.  K6, K2, all four targets,
and their opens are absent from the proof.
Any formal solution in this exact normalized cell would truncate to such a
G10 point and is therefore excluded; no converse reachability or lifting
claim is used.

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
| `n=4` | 1 | G9 tangent | dead at G10 |
| `n=4` | 0 | G9 tangent | dead at G10, including `ord(N)>4` |

The `n=3` rank-one row is essential: it gives a genuine constructible G8
image with nonzero odd columns and dies only at G9.  Therefore neither the
`e=2,m=1` theorem nor the `e=3,m=1` fan can be imported by a
coefficient-blind induction or a substitution in `tau^2`.

This report is the smallest complete transition theorem: no AWS packet or
nonlinear elimination is needed.  Its G10 closure remains producer evidence
until a different model reconstructs it.

## 1. Frozen source, calendar, and replay

The charged bytes are

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  frozen tails.json, 569 monomials
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  compile_contracted_source_v20r2.py
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  exact sparse Q(i) engine
0eb501b414f2162d14a73725a46410b7e799adc70932cdfb8a05f4196ff0bb1a
  corrected e2m1 G7 integration, regression only
64eaafe3fe5aaa9238a338f2da045e302d9a239ac9c29312e39d5c545893d42c
  all-face/uniformity producer, regression only
0e7f98d165bf60531f675bae948315211fd08fd466f21f98aa399cd5fb12457b
  uniform rank-fan replay, regression only
0ee84a0b98d30c4436461a09118961706d1f18fcfe9686684e7b1a27b5597feb
  Fable hostile review containing the exact gradient lemma
22e9752761f3bb4ee94b4dccf18cb72ff49bd0d92453ad4cf39eb401cc45f84a
  sealed e3m1 complete-fan report, regression only
bcd4004e671091c7d1ffc265affbd160b1d2b2a712f62dd97b698150dfc9fcba
  e3m1 complete-fan replay, regression only
efd2f4fea4f58ee4783d9b373ee68f2ff191a9923b08bf2ead8dd1c59a4d3749
  xmodel/k00-ram-e2m2-g0-g10-complete-rankfan-replay-sol56-20260829.py
```

The literal e2 source begins

```text
R(d)+tau^4*k10(tau)*A10(d)+tau^12*k6(tau)*A6(d)
    +tau^20*k2(tau)*A2(d)-targets.                  (1.1)
```

For `ord(d)=2`, its honest lower calendar is

| sector | rows | first possible grade |
|---|---|---:|
| unloaded `R` | rows 1--5,7 | G4 |
| unloaded `R` | row 6 | G6 |
| K10 globally | all rows | G8 |
| K10 restricted to the exact surface | rows 1--3,5,7 | G10 |
| K10 restricted to the exact surface | row 6 | G12 |
| K10 restricted to the exact surface | row 4 | identically zero |
| K6 | rows 1--3,5,7 | G15 |
| K6 | rows 4,6 | G17 |
| K2 | all rows | G23 |
| `mu2,mu4,mu6,Jdet` | target rows | G29,G33,G37,G38 |

“Globally G8” is a possible quadratic normal load, not a claim that it is
nonzero on every branch.  Every branch surviving to G8 has surface leading
coefficient `ell(s,t)`, and the exact tangent identity

```text
A10^[2](ell(s,t))=0                                (1.2)
```

deletes that apparent arrival.  The `n=3` normal branch can meet K10 at G9,
but its decisive row-six load is identically zero.  At G10 the replay keeps
`k10[0],...,k10[6]`; only `k10[0]` survives literal extraction.  No exact
order is imposed on any late boundary series.

Run

```text
python3 -B xmodel/k00-ram-e2m2-g0-g10-complete-rankfan-replay-sol56-20260829.py
python3 -B -O xmodel/k00-ram-e2m2-g0-g10-complete-rankfan-replay-sol56-20260829.py
```

Both modes print identically:

```text
K00_RAM_E2M2_G0_G10_COMPLETE_RANKFAN_REPLAY=PASS
TAIL_TERMS=569
CALENDAR=K10_GLOBAL_G8;SURFACE_G10;K6_G15;K2_G23;TARGETS_G29_G33_G37_G38
GRADIENT_LEMMA=R_ON_D_ZERO;ALL_42_GRADIENTS_ON_D_ZERO
G4_N2=RANK2_RANK1_DEAD_G6;RANK0_TO_G6_N3
G6_N3=RANK2_DEAD_G8;RANK1_G8_SURVIVOR_DEAD_G9;RANK0_TO_G8_N4
ODD_BRANCH_G9_ROW6=EPS*i*q^3/32;S3_T3_N6_K10_RETAINED
G8_N4=ALL_G9_TANGENT_RANKS_DEAD_G10
G10_RANK1=-EPS*5*i*k10[0]*t^3/16;RANK0=Q(v)+kW_EMPTY
ODD_FIXTURE=G0_G8_PASS;G9_FAIL;i/32
CELL_STATUS=POINT_SET_EMPTY_THROUGH_G10_ON_C6_K10_JDET_OPENS
CERTIFICATE_BYTES=6036
CERTIFICATE_SHA256=486bb644cc136c39e4c223b1dbe71aeaadc6b1ad4930d7eb9196be4059b8700f
MUTATIONS=CUSTODY,GRADIENT,ODD_-128_TO_-127,DELTA_64,W2_192,K10_OPEN
```

The 5,958-byte canonical JSON certificate is rebuilt in memory.  Runtime is
about six seconds using Python stdlib exact rational/Gaussian-rational
arithmetic.  No CAS or AWS task is used.

## 2. Exact surface, gradient lemma, and honest fresh cones

The seven unloaded rows vanish identically on

```text
D(S,T)=(2S+S^2,(1+S)T/8,S+16T^2,T,S,2T).           (2.1)
```

The replay also rechecks all 42 identities

```text
(partial R_r/partial d_j)(D(S,T))=0,
r=1,...,7, j=0,...,5.                              (2.2)
```

Thus every single-normal contribution vanishes, at every grade.  This is
the reviewed gradient lemma, now exercised directly rather than used by
custody alone.

Write, without deleting odd coefficients,

```text
d(tau)=D(S(tau),T(tau))+N(tau),
S=s*tau^2+alpha*tau^3+...,
T=t*tau^2+beta*tau^3+...,       (s,t)!=(0,0).       (2.3)
```

At each rank-zero transition the plane part of the next coefficient of `N`
is absorbed into the corresponding coefficient of `(S,T)`.  The change also
shifts later coefficients, which remain arbitrary.  It is therefore an
exact recentering, not removal of an odd column.

For each `n=2,3,4`, literal extraction gives

```text
G(2n)=Q(w),
G(2n+1)=DQ(w)[v].                                  (2.4)
```

Equation (2.4) includes the K10 sector: its apparent G8/G9 terms at `n=4`
vanish by (1.2).  On reduced geometric support,

```text
w=ell(a,b)+(2p,0,0,q,-p,4q),
Delta=p^2+64q^2.                                   (2.5)
```

The plane part is absorbed.  The rank of `DQ(w)` is two on `D(Delta)`, one
on `Delta=0,(p,q)!=(0,0)`, and zero at `p=q=0`.  On the two rank-one charts,

```text
p=epsilon*8i*q, q!=0,
B(v)=epsilon*8i*A(v),       epsilon in {+1,-1},     (2.6)
```

where

```text
A(v)=v5+16v1-4v3,       B(v)=v0-4v2+2v4.           (2.7)
```

All cone and rank statements in this report use (2.5) only on reduced
field-valued support.

## 3. The first G4 cone and G6 kill

At G5, rank two imposes `A(v)=B(v)=0`; rank one imposes (2.6); rank zero has
no G5 equation.  The rank-two G6 row six is

```text
G6_6=p(192q^2-p^2)/65536.                          (3.1)
```

On `D(Delta)`, (3.1) leaves two cases.

If `p=0`, then `q!=0`.  Row four gives `s=0`, while two exact cokernel rows
become

```text
G6_3+(1/8)G6_1       =(1/4)q^2(q+3t/8),
G6_5+(1/128)G6_1     =-(3/64)q^2(q+t/4).           (3.2)
```

They require simultaneously `t=-8q/3` and `t=-4q`, impossible.

If `p^2=192q^2`, normalize `q=1`, write `p=r`, `r^2=192`, and use row four
to put `s=-r(t+2)`.  Two labelled cokernel combinations reduce exactly to

```text
G6_5+(3/128)G6_1+(1/8)G6_3 = 1/8,
G6_7+(1/512)G6_1+(1/128)G6_3 = -1/64.              (3.3)
```

Thus rank two is empty.

On either rank-one chart, every second/third surface coefficient, all four
tangent-kernel directions, and the complete newest block are retained, but

```text
G6_6=epsilon*i*q^3/32.                              (3.4)
```

So rank one is empty on `D(q)`.  Rank zero recenters to the fresh G6 cone
with first normal order `n=3`.

## 4. The odd `n=3` branch: G8 survivor and G9 kill

For the fresh G6 cone, rank two reaches G8.  Define

```text
C=t(64q^2-p^2)+2spq,
E=s(64q^2-p^2)-128tpq.                              (4.1)
```

The exact compatibility identities are

```text
det([alpha,beta,N] rows 1,2,3)=(27/2^35)*Delta*C,
G8_4=(3/2^15)*E.                                   (4.2)
```

The determinant of `(C,E)` in `(s,t)` is `-Delta^2`; hence rank two forces
`s=t=0` and is empty.

On a rank-one chart put `X=A(N4)`, so `B(N4)=epsilon*8i*X`.  Two exact G8
cokernel equations are

```text
F3= epsilon*(3i/2048)X^2 +(3/16)tq^2
      +epsilon*(3i/128)sq^2,

F4=-(3/4096)X^2-epsilon*(3i/32)tq^2+(3/256)sq^2.   (4.3)
```

They satisfy

```text
F3+epsilon*2i*F4
  =epsilon*(3i/64)q^2(s-epsilon*8i*t),
F4 |_(s=epsilon*8i*t)=-(3/4096)X^2.                (4.4)
```

Over a field on `D(q)`, G8 compatibility is therefore

```text
s=epsilon*8i*t,       X=0,       t!=0,             (4.5)
B(N5)-epsilon*8i*A(N5)=-128tq.                     (4.6)
```

This is a genuine constructible G8 component for each sign.  The odd
surface coefficients `alpha,beta`, all four coordinates of the common
kernel `A(N4)=B(N4)=0`, and the five-dimensional affine N5 lift fiber are
free.

At G9 the replay retains those blocks, all six N6 coefficients, and every
K10 coefficient capable of arrival.  The literal row-six equation is

```text
G9_6=epsilon*i*q^3/32,                              (4.7)
```

and every K10 row-six coefficient through the required degree is zero.
Thus both odd G8 components die at G9.

An exact old-pass/fail fixture makes the odd-column requirement concrete.
Over `Q(i)`, let

```text
S=8i*tau^2+3*tau^3,       T=tau^2+5*tau^3,
N3=(16i,0,0,1,-8i,4),
N4=V(0,0;1,2,3,4),
N5=V(0,-128;0,0,0,0),     k10=Jdet=1,              (4.8)
```

where

```text
V(A,B;y1,y2,y3,y4)
 =(B+4y2-2y4,y1,y2,y3,y4,A-16y1+4y3).             (4.9)
```

All seven literal rows vanish in G0--G8 and `G9_6=i/32`.  Replacing `-128`
in N5 by `-127` makes G8 nonzero.  This control would be impossible in a
compiler which silently deleted odd columns.

At rank zero the G8 equation is the fresh cone `Q(N4)=0`, leading to the
final `n=4` fan.

## 5. Fresh G8 cone, G9 tangent fan, and loaded G10 closure

All three ranks of the fresh G8 cone have an honest G9 tangent image by
(2.4).  Retain arbitrary `alpha,beta`, the full N5 tangent block, the full
N6 block, and `k10[0],...,k10[6]`.  The G10 rows are exactly

```text
G10_r = DQ_r(w)[N6]+Q_r(N5)
        +(1/2)D^2R_r^[3](ell)[w,w]
        +k10[0]*L_r(s,t,w),                         (5.1)

L_r=DM4_r(ell)[w]+W_r(s,t).                        (5.2)
```

The odd surface coefficients and `k10[1],...,k10[6]` are verified absent,
not set to zero.  This is the first honest load collision on the final fan.

### Rank two

The tangent condition gives `A(N5)=B(N5)=0`, hence `Q(N5)=0`.  Despite the
normal K10 term in (5.2), the exact determinant and row-four identities are
again (4.2).  They force `s=t=0`, so rank two is empty.

### Rank one

Put `A(N5)=X`, `B(N5)=epsilon*8i*X`.  The first two compatibility equations
are exactly (4.3), now at G10, and force (4.5).  A remaining cokernel row is

```text
G10_2+(epsilon*i/2)G10_1
   =-epsilon*(5i/16)*k10[0]*t^3.                   (5.3)
```

It is nonzero on the chart.  The K10-unit open is load-bearing precisely
here.

### Rank zero

At `p=q=0`, G9 vanishes and G10 becomes

```text
Q(N5)+k10[0]*W(s,t)=0.                              (5.4)
```

Write `A=A(N5)`, `B=B(N5)`.  Row four gives

```text
B^2-64A^2=0.                                       (5.5)
```

Over the algebraic closure, put `B=delta*8A`, `delta=+1` or `-1`.  The
exact combination of literal rows is

```text
G10_3+(1/8)G10_1=delta*(3/2048)A^2.                (5.6)
```

The K10 surface load cancels from (5.6), so `A=B=0`.  Every quadratic row
then vanishes and (5.4) reduces to `k10[0]*W=0`.  Two load rows are

```text
W1=(5/4096)t(3s^2-64t^2),
W2=(5/65536)s(s^2-192t^2).                          (5.7)
```

Their only common zero is `(s,t)=(0,0)`: coordinate-axis cases are
immediate, while on `D(st)` they demand both `s^2=64t^2/3` and
`s^2=192t^2`.  Rank zero is empty, including the branch with `ord(N)>4`.
This completes (0.2).

## 6. Scope, controls, and lifecycle

All surface coefficients capable of reaching the relevant grades are
retained.  On the odd G9 branch these are `S2,T2,S3,T3`; on the G10 branch
`S3,T3` are retained and verified absent.  Every normal coefficient through
N6 is retained wherever it can occur.  Later coefficients first reach G11
or beyond by the exact deviation-grade census and are not silently set to
zero.

The replay fails closed on:

1. drift in any frozen source, reviewed lemma, or regression packet;
2. changing `16T^2` in the exact surface to `15T^2`;
3. changing the odd affine lift `-128` to `-127`;
4. changing `64` in the transverse discriminant to `63`;
5. changing `192` in W2 to `191`; and
6. deleting the `k10[0]` open, which removes the final rank-one terminal.

The theorem is point-set over an algebraic closure.  The raw cone equations
are retained, but their parameterization and the splittings
`p=+/-8iq`, `B=+/-8A` are used only on reduced geometric support.  No ideal
equality, multiplicity, nilpotent lifting, or scheme-valued normal-form
theorem follows.

This packet is `EXACT PRODUCER / REVIEW REQUIRED`.  Stop or narrow it if a
different-model reconstruction changes the frozen source, `Lambda=tau^2`,
the exact gradient lemma, an odd-column coefficient, the K10 shift, a rank
chart, or any displayed terminal.

Beyond the truncation consequence stated in section 0, no assertion is made
about arc existence or lifting, source reachability, attainment,
algebraization, a polynomial map, another ramification pair, another K00
support, or JC2.  Finite-jet point-set emptiness is used only within the
exact cell and opens (0.1).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14580`.
- Body SHA-256:
  `510f81b84a4d965962f8c07ee261beaa8912e5a05baf206b80ffe88a7e67f637`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
