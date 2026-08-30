# Normalized K00 `e=2,m=2,h10=1` boundary through G12

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra  
Frozen campaign basis: `0d7544ebd5cb12def6bac892646010301098be3c`  
Lifecycle: **EXACT PRODUCER / PROVISIONAL G11 DEPENDENCY / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

On the normalized generic K00 support, put

```text
Lambda=tau^2,       C6=1,       ord_tau(d)=2,
k10=tau*kappa+tau^2*kappa2+...,  kappa!=0,
Jdet[0]!=0.                                             (0.1)
```

The literal G12 coefficient splits the two G11 survivor mechanisms rather
than closing the cell:

```text
old n=4 rank one, epsilon=+/-1:  dead at G12;
fresh n=5 rank two:              survives G12;
fresh n=5 rank one, both signs:  survives G12.          (0.2)
```

In particular,

```text
V(G0,...,G12) intersect V(k10[0]) intersect D(k10[1])
                intersect {d[2]!=0} != empty.            (0.3)
```

The two fresh-`n=5` survival claims have exact rational/Gaussian-rational
fixtures and old-pass/new-fail G12 controls.  Consequently G13, not G12, is
the next unresolved coefficient gate for this child.

This is finite-prefix field-point nonemptiness only.  No displayed fixture
is asserted to extend to a formal arc, to be reachable from closure data, or
to arise from a polynomial Keller map.

## 1. Provisional dependency and frozen custody

The transition-tree organization through G11 is imported **PROVISIONALLY**
from the sealed G11 producer while its different-model review is active.  A
reversal of that parent must quarantine or re-root this report.  The G12
identities themselves are independently reconstructed from the 569 literal
tails; no G11 formula is shifted and no coefficient recurrence is assumed.

The charged bytes are

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  frozen tails.json, 569 monomials
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  exact sparse Q(i) source engine
fa5a4ef6a1b2c0640c6363b84e6b547a044920b15249f7c72b25ffbcda2c1733
  reviewed e2m2 G10 producer
efd2f4fea4f58ee4783d9b373ee68f2ff191a9923b08bf2ead8dd1c59a4d3749
  reviewed e2m2 G10 replay
05e416fccb20b42a187f254995c021608e9060444660628d52a848d17f19b8e1
  provisional e2m2 h10=1 G11 producer
d5e458d2c430cc85be86b711e37355671090057881474458055dbf7f593609c3
  provisional e2m2 h10=1 G11 replay
cc8d84f8d5deeb8ee3852901b657e65b7499c397fbff66ba2b8361ad8cd4db15
  xmodel/k00-ram-e2m2-h10eq1-g12-branch-split-replay-sol56-20260830.py
```

Through G12 the literal source is

```text
R(d)+tau^4*(tau*kappa+tau^2*kappa2+...)*A10(d).     (1.1)
```

The same source-partition calendar keeps K6, K2, and every target beyond
G12.  The new feature relative to G11 is that both
`kappa*[tau^7]A10(d)` and `kappa2*[tau^6]A10(d)` arrive.  The replay retains
`k10[3]` as a negative control and verifies that it cannot arrive because
`[tau^5]A10(d)=0` on both survivor mechanisms.

## 2. Complete literal G12 arrival formulas

Write

```text
D(S,T)=(2S+S^2,(1+S)T/8,S+16T^2,T,S,2T),
S=s*tau^2+alpha*tau^3+gamma*tau^4+...,
T=t*tau^2+beta*tau^3+eta*tau^4+....                 (2.1)
```

Put `ell_j=ell(S_j,T_j)`, let `D4` be the degree-four coefficient
`ell(gamma,eta)+mu(s,t)` of the exact graph, and write

```text
Q=R^[2],       R3=R^[3],       R4=R^[4],
M4=A10^[2].                                           (2.2)
```

Let `W6_r=[tau^6]A10_r(D(S,T))` and
`W7_r=[tau^7]A10_r(D(S,T))`.  Thus `W6` is the cubic surface load from the
G11 packet, while `W7` is its exact directional coefficient in
`(alpha,beta)`.  These are definitions by literal extraction, not by a
guessed recurrence.

### Old `n=4` mechanism

For

```text
N=tau^4*w+tau^5*v+tau^6*u+tau^7*z+tau^8*r+...,
```

all of `S2..S4,T2..T4,N4..N8,k10[1],k10[2]` can contribute.  Direct
row-by-row extraction gives

```text
G12_r = DQ_r(w)[r] + DQ_r(v)[z] + Q_r(u)
       +D^2R3_r(ell2)[w,u]
       +(1/2)D^2R3_r(ell2)[v,v]
       +D^2R3_r(ell3)[w,v]
       +(1/2)D^2R3_r(D4)[w,w] + R3_r(w)
       +(1/2)D^2R4_r(ell2)[w,w]
       +kappa*(D M4_r(ell2)[v]+D M4_r(ell3)[w]+W7_r)
       +kappa2*(D M4_r(ell2)[w]+W6_r).               (2.3)
```

The seven raw G12 rows have respectively

```text
75, 88, 92, 81, 93, 51, 86
```

sparse terms before branch specialization.  Equation (2.3) is checked as
exact polynomial equality in every row.  It explicitly includes the first
capable unloaded quartic contribution and every cubic contribution.
`k10[3]` is retained and verified absent.

### Fresh `n=5` mechanism

For

```text
N=tau^5*w+tau^6*v+tau^7*u+tau^8*r+...,
```

the complete coefficient is

```text
G12_r = DQ_r(w)[u] + Q_r(v)
       +(1/2)D^2R3_r(ell2)[w,w]
       +kappa*(D M4_r(ell2)[w]+W7_r)
       +kappa2*W6_r.                                 (2.4)
```

The seven raw term counts are

```text
22, 25, 23, 15, 22, 0, 20.
```

The replay retains `S4,T4,N8,k10[3]` and verifies their literal absence.
No unloaded quartic can reach G12 here: its cheapest term with two surface
and two normal factors has grade `2+2+5+5=14`.  Thus (2.4) contains every
quadratic, cubic, quartic, and loaded contribution capable of arrival.

## 3. Old `n=4` rank-one branches die at G12

On either Gaussian sign chart, the inherited equations through G10 put

```text
p=epsilon*8i*q,     q!=0,
s=epsilon*8i*t,
A(N5)=B(N5)=0,
B(N6)-epsilon*8i*A(N6)+128*t*q=0.                  (3.1)
```

Retain arbitrary `S3,T3,S4,T4`, all four kernel coordinates in each normal
block, complete `N7,N8`, and both `kappa,kappa2`.  Literal extraction gives

```text
G11_6=0,
G12_6=epsilon*i*q^3/32.                             (3.2)
```

Moreover the K10 row-six coefficients at raw degrees six and seven vanish
identically, so neither `kappa2` nor the new `kappa` load can alter (3.2).
Because `q!=0`, every G11 survivor on either old rank-one chart dies.

The stop is sharp on both signs.  The G11 fixtures

```text
S=epsilon*8i*tau^2,       T=tau^2,
N4=(epsilon*16i,0,0,1,-epsilon*8i,4),
N5=V(0,0;5/72,0,0,0),
N6=V(0,-128;0,0,0,0),
N7=V(0,320/9;0,0,0,0),
k10=tau
```

pass G0--G11 and fail exactly as `G12_6=epsilon*i/32`.

## 4. Fresh `n=5` rank two survives: rational fixture

Use the exact graph-normal data

```text
S=tau^2,       T=0,
N5=( 2,0,0,0,-1,0),
N6=(-4,0,0,0, 0,0),
N7=(-2,0,0,0, 0,0),
k10=(48/5)*tau,       Jdet=1.                       (4.1)
```

Here `p=1,q=0`, so `Delta=p^2+64q^2=1` and the fresh cone has rank two.
All seven literal rows vanish in G0--G12.  The value `B(N6)=-4` is exactly
the G11 affine solution for `kappa=48/5`; `B(N7)=-2` removes the remaining
G12 image coordinate.

Changing only `B(N7)` from `-2` to `-1` leaves G0--G11 unchanged and makes
`G12_2=3/16384`.  This is an old-pass/new-fail control for the new grade.

## 5. Fresh `n=5` rank one survives on both signs

For each `epsilon in {+1,-1}`, use

```text
S=8*tau^2,                 T=epsilon*i*tau^2,
N5=(epsilon*16i,0,0,1,-epsilon*8i,4),
N6=(-epsilon*128i,0,0,0,0,16),
N7=( epsilon*128i,0,0,0,0,0),
k10=-(12/5)*tau,           Jdet=1.                  (5.1)
```

The leading normal satisfies `p=epsilon*8i*q`, `q=1`.  The surface lies on
the G11 opposite wall

```text
s=-epsilon*8i*t,
```

because `t=epsilon*i` and `s=8`.  In the notation of the G11 tangent block,

```text
A(N6)=16,       B(N6)=-epsilon*128i,
B(N6)-epsilon*8i*A(N6)=-(320/3)*kappa*t^3.         (5.2)
```

Direct literal evaluation makes every row zero in G0--G12, for both signs.
Changing only the first coordinate of `N7` from `epsilon*128i` to
`epsilon*127i` preserves G0--G11 and leaves
`G12_1=epsilon*3i/1024`.  Thus the survival is not a cancellation artifact
of a row omitted from the replay.

## 6. Sharp conclusion and next gate

Relative to the provisional G11 transition organization, the complete
branch decision at the next grade is

```text
N4_RANK1_BOTH_SIGNS_DEAD_G12;
N5_RANK2_SURVIVES_G12;
N5_RANK1_BOTH_SIGNS_SURVIVE_G12.                   (6.1)
```

The sharp cell statement is

```text
POINT_SET_NONEMPTY_THROUGH_G12;
FORMAL_ARC_STATUS_OPEN;
NEXT_LITERAL_GATE=G13.                             (6.2)
```

This report does not classify the entire G12 scheme structure, the G13 fan,
`h10>=2`, `h10=infinity`, another `(e,m)`, another K00 support, lifting,
source reachability, algebraization, a polynomial map, a counterexample, or
JC2.  The explicit fixtures prove only finite-prefix field-point survival.

## 7. Deterministic replay

Run

```text
python3 -B xmodel/k00-ram-e2m2-h10eq1-g12-branch-split-replay-sol56-20260830.py
python3 -B -O xmodel/k00-ram-e2m2-h10eq1-g12-branch-split-replay-sol56-20260830.py
```

Both modes print identically:

```text
K00_RAM_E2M2_H10EQ1_G12_BRANCH_SPLIT_REPLAY=PASS
TAIL_TERMS=569
DEPENDENCY=G11_PROVISIONAL;G12_LITERAL_FROM_569_TAILS
N4_G12=RANK1_BOTH_SIGNS_DEAD;ROW6=EPS*i*q^3/32
N5_G12=RANK2_SURVIVES;RANK1_BOTH_SIGNS_SURVIVE
ARRIVAL=N4_CUBIC_QUARTIC_K10_2_RETAINED;N5_CUBIC_K10_2_RETAINED
FIXTURE_N5_RANK2=S2=1;P5=1;B6=-4;B7=-2;K10_1=48/5
FIXTURE_N5_RANK1=S2=8;T2=EPS*i;P5=EPS*8i;Q5=1;A6=16;B6=-EPS*128i;B7=EPS*128i;K10_1=-12/5
CELL_STATUS=POINT_SET_NONEMPTY_THROUGH_G12;FORMAL_ARC_OPEN;NEXT_GATE_G13
CERTIFICATE_BYTES=2725
CERTIFICATE_SHA256=56ebd72c0b66326eeee7fc1148838d11212ad1ef049907291675959b5484538e
MUTATIONS=CUSTODY,N4_ROW6,N5_RANK2_B7,N5_RANK1_B7,CAPABLE_SLOT_ABSENCE
```

The replay uses Python stdlib exact rational/Gaussian-rational arithmetic,
writes no files, and completes in about ten seconds.  The G12 producer still
requires hostile review by a different model before promotion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9501`.
- Body SHA-256: `b1e79f4643ac1f0151441086056a91694e67cc12a678d7de3565fde073224343`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
