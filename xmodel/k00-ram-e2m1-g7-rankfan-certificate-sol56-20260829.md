# Exact G7 closure of `K00-V20R2-RAM-E2-M1-B11111/v1`

Date: 2026-08-29  
Author: Sol 5.6 Ultra  
Frozen campaign basis: `31777ce90994a106aade85064c0d868e32863f94`  
Status: **EXACT PRODUCER CERTIFICATE / POINT-SET EMPTY / REVIEW-GATED**

## Result

For the literal source cell

```text
Lambda=t^2,  ord_t(d)=1,
ord_t(k10)=ord_t(Jdet)=0,
ord_t(k6)=ord_t(k2)=ord_t(mu2)=ord_t(mu4)=ord_t(mu6)=1,
```

the source equations through grade seven have no point over an algebraic
closure on the exact opens.  More precisely, after the promoted G3 reduction
`d[1]=ell(s,t)`,

```text
V(G0,...,G7) intersect D(k10[0])
             intersect (D(s) union D(t)) = empty.                 (0.1)
```

Consequently the full 273-equation grade-38 cell is empty: a full point would
restrict to a point of (0.1).  No K6, K2, target, or late-column assumption is
needed for the kill.

The exhaustive path is

```text
G5 matrix rank 2  -> empty at G5;
G5 matrix rank 1  -> empty at G6;
G5 matrix rank 0  -> fresh G6 cone;
    G6 rank 2     -> empty at G7;
    G6 rank 1     -> empty at G7;
    G6 rank 0     -> empty at G7.
```

All seven labelled rows, including rows which are identically zero at an
intermediate grade, are retained in the exact serialization and replay.

## 1. Frozen source, replay, and erratum

The source-complete ramified packet is

```text
98fb38535405f1cc853dd4d430e26876a84f6f97c538f862f18a0446c0c97ecf
  xmodel/k00-v20r2-valuative-comparison-v1-sol56-20260829.md.
```

It fixes all `273=7*39` equations through G38, 331 labelled columns, the five
boundary-zero columns, the exact opens, and the literal load scale

```text
R(d)+t^4*k10*A10(d)+t^12*k6*A6(d)+t^20*k2*A2(d)-targets. (1.1)
```

The new exact stdlib replay is

```text
981b39f91afd4e449193077bc00d02937701618cee9bc3ae53547edaaa11dac6
  xmodel/k00-ram-e2m1-g7-rankfan-replay-sol56-20260829.py.
```

It reconstructs all 569 frozen tail monomials and extracts every displayed
coefficient directly from (1.1).  Ordinary and optimized Python both print

```text
K00_RAM_E2M1_G7_RANKFAN_REPLAY=PASS
TAIL_TERMS=569
UNLOADED_SINGULAR_SURFACE=EXACT
K10_G7_ERRATUM=DM4(ell)[u]+A10_CUBIC(ell)=DM4(ell)[u-mu/2]
K10_G7_ROW2_WITNESS=5/65536;OMITTED_CUBIC_MUTATION=5/32768
G5_RANK2=EMPTY;G5_RANK1=EMPTY_AT_G6;G5_RANK0=ALL_SEVEN_ROWS_ZERO
G6_CENTERED=Q(r);G6_RANK2=EMPTY_AT_G7;G6_RANK1=EMPTY_AT_G7;G6_RANK0=EMPTY_AT_G7
CELL_STATUS=EMPTY_THROUGH_G7_ON_EXACT_SOURCE_OPENS
CERTIFICATE_BYTES=22819
CERTIFICATE_SHA256=9a8e19ab5fc95b4039206029a33923dc7f080ed332e4788e465467296e72850c
MUTATIONS=CUSTODY,SURFACE_16_TO_15,OMIT_A10_CUBIC,DELTA_64_TO_63,RANK1_SIGN,ZERO_ROW_REACTIVATION
```

The 22,819-byte object is deterministic canonical JSON rebuilt in memory.
It contains the seven raw G4 quadrics, all G5 rows on the reduced G4 cone,
both specialized G6 rank-one row sets, the centered G6 rows, all literal G7
rows, K10 load rows, rank forms, opens, source pins, and the final
disposition.

### Erratum to the sealed G5 prefix

The immutable provisional prefix report and replay have full hashes

```text
a6fd11f1c6d5b32cc2e497722245cbe7381356ffdbba02c6db050ad5fe67ced0
  xmodel/k00-ram-e2m1-g5-prefix-certificate-sol56-20260829.md
b4fd505d0345b21a2978f06ff63cb0c9fcacd9d7226d7accaa0b2ab489b210ea
  xmodel/k00-ram-e2m1-g5-prefix-replay-sol56-20260829.py.
```

Their K10/G7 sharpness check retained only the polarization
`DM4(ell)[u]`.  The literal coefficient also contains the cubic normal-degree
piece:

```text
[t^3]A10(d(t))
 = DM4(ell)[u]+A10^[3](ell)
 = DM4(ell)[u-mu/2].                                (1.2)
```

At `s=1,t=0,u=mu`, row 2 is

```text
old polarization =  5/32768,
cubic correction = -5/65536,
literal G7 load  =  5/65536.                        (1.3)
```

Thus the old numerical witness and displayed G7 formula were wrong.  The
following conclusions survive exact recheck:

1. the G3 nonzero-rank kill, because no load occurs at G2/G3;
2. the exact G4/G5 identities and finite G5 witness, because K10 first occurs
   only later; and
3. first nonzero K10 arrival at G7, now witnessed by (1.3).

This report supersedes only the erroneous G7 coefficient statement; it does
not alter either sealed parent artifact.

## 2. Exact unloaded surface and centering

The seven unloaded rows vanish identically on the exact surface

```text
D(S,T)=(2S+S^2,(1+S)T/8,S+16T^2,T,S,2T):
R_r(D(S,T))=0,                         r=1,...,7.    (2.1)
```

This identity is reconstructed from the tails, not inferred from another
valuation.  It explains the successive centers below.  It is not a point of
the full source: the load polynomials do not vanish identically on (2.1).

Retain the G4 scheme equations `Q_r(w)=0`.  For geometric existence only,
their reviewed reduced support is parameterized by

```text
w=(2b+2p,a,b,8a+q,b-p,16a+4q),
Delta=p^2+64q^2.                                    (2.2)
```

The rank of `DQ(w)` is two on `D(Delta)`, one on
`Delta=0,(p,q)!=(0,0)`, and zero at `p=q=0`.

## 3. First exhaustive fan: G5

Put

```text
A(v)=16v1-4v3+v5,       B(v)=v0-4v2+2v4,
X=A(v),                 Y=B(v).
```

Direct extraction gives

```text
G5_r=alpha_r X+beta_r Y+N_r(s,t,a,b,p,q),           (3.1)
```

where

```text
alpha=(3p/1024, 3q/256, -3p/8192, 0,
       -3p/131072, 0, -3p/1048576),
beta =(-3q/1024, 3p/16384, 3q/8192, 0,
        3q/131072, 0, 3q/1048576).
```

No coefficient direction outside `X,Y` occurs.  Define

```text
C=t(64q^2-p^2)+2spq,
E=s(64q^2-p^2)-128tpq.                              (3.2)
```

The exact compatibility identities are

```text
det([alpha,beta,N] rows 1,2,3) = (27/2^35) Delta C,
G5_4                              = (3/2^15) E,
(3/128)G5_1+(1/8)G5_3+G5_5       = 0,
G5_6                              = 0,
(1/512)G5_1+(1/128)G5_3+G5_7     = 0.              (3.3)
```

The zero in labelled row 6 is kept; it reactivates at G6 on the rank-one
branches.

### Rank two

On `D(Delta)`, (3.3) gives `C=E=0`.  The determinant of their coefficient
matrix in `(s,t)` is

```text
-Delta^2.                                           (3.4)
```

Thus `s=t=0`, contrary to the exact transverse-order-one open.

### Rank one

Over an algebraic closure the two charts are

```text
p=epsilon*8i*q,  q!=0,       epsilon in {+1,-1}.
```

Row 4 gives `s=epsilon*8i*t`; all seven G5 rows then vanish exactly after

```text
Y-epsilon*8i*X=-128tq.                              (3.5)
```

This is a genuine G5 survivor, so it is not silently discarded.  At G6 the
following exact labelled combinations are independent of every new
coefficient and every free variable:

```text
(3/128)G6_1+(1/8)G6_3+G6_5 = -q^3/16,
G6_6                              = epsilon*i*q^3/32,
(1/512)G6_1+(1/128)G6_3+G6_7 = q^3/128.            (3.6)
```

Hence `q=0`, contradicting the rank-one chart.

### Rank zero

For `p=q=0`, every one of the seven G5 rows is the zero polynomial.  No row
or variable is removed.  Renaming the two free plane coordinates, write
`w=ell(a,b)`; this branch proceeds to the second fan.

## 4. Second exhaustive fan: centered G6 and literal G7

On the G5 rank-zero branch write `w=ell(a,b)` and

```text
nu3=(2sa,(sb+at)/8,32tb,0,0,0),
d[3]=nu3+r.
```

With arbitrary `r` and arbitrary `d[4]`, direct source expansion gives

```text
G6_r=Q_r(r),                       r=1,...,7.        (4.1)
```

Thus its reduced cone has the same literal rank parameterization, now write

```text
r=ell(c,d)+rT,
rT=(2p,0,0,q,-p,4q),
Delta=p^2+64q^2.                                    (4.2)
```

The plane part `ell(c,d)` is absorbed into the coefficients of `S(t),T(t)`
on (2.1).  Center the next source coefficient by

```text
nu4=(a^2+2sc,(sd+ab+ct)/8,16b^2+32td,0,0,0),
d[4]=nu4+z.                                         (4.3)
```

Direct extraction from the literal source, including both normal-degree
pieces in (1.2), gives

```text
G7_r = DQ_r(rT)[z]
       +(1/2)D^2c3_r(ell)[rT,rT]
       +k*W_r(s,t),                 k=k10[0].        (4.4)
```

Here `k10[1]` is exactly absent, and the load is independent of `a,b,c,d`.
Two load rows sufficient for the rank-zero case are

```text
W_1=(5/4096)t(3s^2-64t^2),
W_2=(5/65536)s(s^2-192t^2).                         (4.5)
```

The same `alpha,beta,Delta,C,E` formulas from (3.1)--(3.2), now for `rT`
and `A(z),B(z)`, are rederived from (4.4).  Crucially, the corrected K10 load
cancels from the rank-two determinant and row 4:

```text
det([alpha,beta,N+kW] rows 1,2,3)=(27/2^35)Delta C,
G7_4=(3/2^15)E.                                    (4.6)
```

No periodicity statement is used; these are literal G7 coefficient
identities.

### G6 rank two

Equations (4.6) and the determinant (3.4) force `s=t=0`, contradicting the
source open.

### G6 rank one

Put `p=epsilon*8i*q`, `q!=0`.  Row 4 forces
`s=epsilon*8i*t`, so the source open gives `t!=0`.  The exact remaining
compatibility is

```text
G7_2+(epsilon*i/2)G7_1
   =-epsilon*(5i/16)*k*t^3.                         (4.7)
```

This cannot vanish because both `k` and `t` are units on the chart.

### G6 rank zero

At `p=q=0`, the unloaded part and the complete new-coefficient block in
(4.4) are zero, leaving `G7=kW`.  The two cubics (4.5) have only the common
zero `(s,t)=(0,0)`: if either coordinate is zero the other cubic kills the
remaining coordinate; if both are nonzero they require simultaneously
`s^2=64t^2/3` and `s^2=192t^2`.  This again contradicts the source open.

These three cases exhaust the reduced G6 cone, completing (0.1).

## 5. Scheme discipline and controls

The G4 ideal is nonreduced.  This proof does not replace it scheme-theoretically
by its radical.  It uses the radical only for point-set existence, licensed by
`V(I)=V(sqrt(I))`, and retains the original seven G4 generators and all later
labelled rows in the source/certificate.  No multiplicity, embedded-prime,
tangent, or lifting statement is inferred.

Run

```text
python3 -B xmodel/k00-ram-e2m1-g7-rankfan-replay-sol56-20260829.py
python3 -B -O xmodel/k00-ram-e2m1-g7-rankfan-replay-sol56-20260829.py
```

The replay fails closed on:

1. drift in the tails, compiler, source packet, promoted G3 theorem, or
   immutable prefix artifacts;
2. changing the `16T^2` coefficient in the exact surface to `15T^2`;
3. omitting `A10^[3](ell)` from G7, which recreates the old `5/32768` error;
4. changing the `64` in `Delta` to `63`;
5. reversing either rank-one affine sign; and
6. treating the labelled zero G5 row 6 as globally absent, since it becomes
   the nonzero unit `epsilon*i*q^3/32` at G6.

These are exact source and semantic controls; the final `PASS` line alone is
not evidence.

## 6. Scope firewall

This certificate closes exactly the normalized `e=2,m=1,B11111` ramified
cell above.  It does not prove that integer or ramified valuation cells
exhaust closure incidence, close another load-order cell, treat another
normalization or K00 support, or establish properness of the full source
incidence.  It produces no arc, polynomial map, Keller pair, counterexample,
attainment, K00-wide conclusion, or JC2 conclusion.  The exact surface (2.1)
belongs only to the unloaded rows and is not itself a full-source solution.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11123`.
- Body SHA-256: `c9a96bd9282dc874a366f709e5f76d3e2ebd84b0650e3ac0c52d6d81b0c98a2d`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
