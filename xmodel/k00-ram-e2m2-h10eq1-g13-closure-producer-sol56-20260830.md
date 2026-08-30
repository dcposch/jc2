# Normalized K00 `e=2,m=2,h10=1` closure at G13

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra  
Frozen campaign basis at authoring: `a619157b73c1dee1ca0599db47321ffd7588d748`  
Lifecycle: **EXACT PRODUCER / PROVISIONAL G12 PARENT / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

On the normalized generic K00 support, put

```text
Lambda=tau^2,       C6=1,       ord_tau(d)=2,
k10=tau*kappa+tau^2*kappa2+...,  kappa!=0,
Jdet[0]!=0.                                             (0.1)
```

Literal extraction from all 569 frozen V20R2 tails closes every fresh
`n=5` survivor at G13:

```text
fresh n=5 rank one, both signs:  dead at G13;
fresh n=5 rank two:              every G12 survivor dead at G13.  (0.2)
```

Together with the reviewed G11 rank-zero death and the G12 producer's old
`n=4` rank-one death, this gives the conditional cell statement

```text
V(G0,...,G13) intersect V(k10[0]) intersect D(k10[1])
                intersect D(d[2]) = empty.              (0.3)
```

The qualifier “conditional” is load-bearing: the old-`n=4` G12 parent has
not yet received its required different-model review.  The fresh-`n=5`
closure proved here is independently literal and does not depend on a
coefficient recurrence.

This is a finite-jet field-point statement.  It is not a formal-arc,
source-reachability, polynomial-map, counterexample, or JC2 statement.

## 1. Frozen custody and exact scope

The charged bytes are

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  frozen tails.json, 569 monomials
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  exact sparse Q(i) source engine
efd2f4fea4f58ee4783d9b373ee68f2ff191a9923b08bf2ead8dd1c59a4d3749
  reviewed e2m2 helper replay
8ba031e87032a007beade2eda7f97f94802eac0bfa561addf90d8f5fb3df8307
  promoted G11 coordinator integration
eda4f40b452ef1f68d53d82ff22c5ec6a4a74147b7f6785b3dc9cc1148137db8
  provisional G12 branch-split producer
cc8d84f8d5deeb8ee3852901b657e65b7499c397fbff66ba2b8361ad8cd4db15
  provisional G12 replay
a508b9853490d82f8a9c7c6242331b5c33298104249a216a9bb418c949e5403d
  xmodel/k00-ram-e2m2-h10eq1-g13-closure-replay-sol56-20260830.py
```

The replay reconstructs the rows from `tails.json`; it does not shift a G12
formula.  All local work is exact stdlib rational/Gaussian-rational sparse
arithmetic and completes in about eleven seconds.

## 2. Complete fresh-`n=5` G13 arrival

Write

```text
D(S,T)=ell(S,T)+mu(S,T),
S=s*tau^2+alpha*tau^3+gamma*tau^4+...,
T=t*tau^2+beta*tau^3+eta*tau^4+...,
N=tau^5*w+tau^6*v+tau^7*u+tau^8*z+....              (2.1)
```

Put `Q=R^[2]`, `R3=R^[3]`, `M4=A10^[2]`, and let `L_j` denote the literal
degree-`j` coefficient of `A10(D(S,T)+N)`.  Direct extraction gives, in
each of the seven rows,

```text
G13_r = DQ_r(w)[z] + DQ_r(v)[u]
       +D^2 R3_r(ell2)[w,v]
       +(1/2)D^2 R3_r(ell3)[w,w]
       +kappa*L8_r+kappa2*L7_r+kappa3*L6_r,          (2.2)

L6_r = [tau^6]A10_r(D(S,T)),
L7_r = D M4_r(ell2)[w]+[tau^7]A10_r(D(S,T)),
L8_r = D M4_r(ell2)[v]+D M4_r(ell3)[w]
       +[tau^8]A10_r(D(S,T)).                        (2.3)
```

The seven literal G13 rows have respectively

```text
51, 55, 57, 33, 56, 15, 51
```

sparse terms before lower-equation specialization.  Equations (2.2)--(2.3)
are checked as exact polynomial equalities row by row.  The replay retains
`S2..S4,T2..T4,N5..N9,k10[1..4]`; it verifies that `N9` and `k10[4]`
cannot arrive.  In particular, row six has its first nonzero fresh-`n=5`
coefficient at G13, with 15 raw terms.  This new cokernel row is why merely
continuing the two old image coordinates would miss the closure.

No unloaded quartic can reach G13 on the fresh chart: two surface and two
normal factors cost at least `2+2+5+5=14`.

## 3. The first G13 terminal: a surface quartic wall

Use the cone and tangent coordinates

```text
w=(2p,0,0,q,-p,4q),
v=V(A,B;y1,y2,y3,y4),
Delta=p^2+64q^2.                                    (3.1)
```

Let `G11_1,G11_2` be the literal first two lower coefficients after the
fresh recentering.  Direct row-six extraction gives the exact identity

```text
G13_6 = (t/8)G11_1-(s/32)G11_2
       +(35*kappa/2^23) P4(s,t),                    (3.2)

P4(s,t)=s^4-384s^2*t^2+4096t^4.                    (3.3)
```

There is no `N8` term in (3.2), because the quadratic sixth row is zero.
Every G13 survivor must therefore lie on the new ratio wall `P4=0`.

### Rank one

On `p=epsilon*8i*q`, `q!=0`, the reviewed G11 compatibility condition is

```text
s=-epsilon*8i*t,       t!=0.                        (3.4)
```

But literal substitution in (3.3) gives

```text
P4(-epsilon*8i*t,t)=32768*t^4.                      (3.5)
```

Since both `t` and `kappa` are units, (3.2) cannot vanish.  Thus every
rank-one G12 survivor dies at G13, on both Gaussian signs.  This conclusion
does not depend on how its free G12 coefficients were chosen.

## 4. The second G13 terminal kills rank two

Suppose `Delta!=0`.  The two G11 image equations uniquely give

```text
U=-(1024/3)kappa*W1,       V=-(16384/3)kappa*W2,
A=(pU+qV)/Delta,
B=(-64qU+pV)/Delta,                              (4.1)
```

where

```text
W1=(5/4096)t(3s^2-64t^2),
W2=(5/65536)s(s^2-192t^2).                         (4.2)
```

At G12, let `H1,H2` be the first two residuals before inserting `u`, and
put

```text
U2=-(1024/3)H1,       V2=-(16384/3)H2,
C=(pU2+qV2)/Delta,
D=(-64qU2+pV2)/Delta.                               (4.3)
```

Every rank-two G12 survivor necessarily has (4.1) and (4.3), regardless of
its additional lower-row constraints.  Retain arbitrary
`alpha,beta,gamma,eta,kappa2,kappa3`, all four kernel coordinates of `v`
and `u`, and an arbitrary new `N8`.  The quadratic `N8` image obeys

```text
I3=-I1/8,       I5=-I1/128.                         (4.4)
```

Consequently the combination

```text
T13=G13_5+(1/8)G13_3+(3/128)G13_1                 (4.5)
```

annihilates every possible `N8`.  Substitute (4.1), (4.3), clear the sole
power of `Delta^{-1}`, and reduce only by `P4=0`.  Literal exact reduction
gives

```text
T13 = (35*kappa/2^17) s*t*(s^2-64t^2).             (4.6)
```

Every free slot listed above cancels identically.  This is an identity from
the frozen tails, not a recurrence or a numerical interpolation.

Equations (3.3) and (4.6) have no projective common point in characteristic
zero:

```text
s=0       and P4=0  imply t=0;
t=0       and P4=0  imply s=0;
s^2=64t^2          gives P4=-16384t^4.              (4.7)
```

The first two alternatives violate `d[2]!=0`, and the last again forces
`t=0`.  Since `Delta` and `kappa` are units on this branch, every rank-two
G12 survivor dies at G13.

## 5. Exact old-pass/new-fail controls

### Both rank-one signs

For each `epsilon in {+1,-1}`, use the G12 fixture

```text
S=8*tau^2,                 T=epsilon*i*tau^2,
N5=(epsilon*16i,0,0,1,-epsilon*8i,4),
N6=(-epsilon*128i,0,0,0,0,16),
N7=( epsilon*128i,0,0,0,0,0),
k10=-(12/5)*tau.                                      (5.1)
```

Every literal row vanishes in G0--G12, while

```text
G13_6=-21/64                                           (5.2)
```

for both signs.

### Rank two, with the new image already removed

Use

```text
S=tau^2,       T=0,
N5=( 2,0,0,0,-1,0),
N6=(-4,0,0,0,0,0),
N7=(-2,0,0,0,0,0),
N8=(32,0,0,0,0,0),
k10=(48/5)*tau.                                      (5.3)
```

Here `N8=V(0,32;0,0,0,0)` kills both available G13 image coordinates.
Every row vanishes in G0--G12 and every G13 row except the sixth vanishes;
the isolated failure is

```text
G13_6=21/524288.                                     (5.4)
```

These controls distinguish the new grade from every inherited equation and
exercise both surviving ranks.

## 6. Exact branch inventory and qualifiers

The normalized `h10=1` transition inventory is now

```text
n=2 rank 2/1 dead G6; rank 0 recenters;
n=3 rank 2 dead G8; rank 1 dead G9; rank 0 recenters;
n=4 rank 2 dead G10; rank 1 both signs dead G12; rank 0 recenters;
n=5 rank 0 dead G11;
n=5 rank 1 both signs dead G13;
n=5 rank 2 every G12 survivor dead G13.             (6.1)
```

The entries through G11 are reviewed.  The old-`n=4` G12 entry is imported
from the sealed but still provisional parent.  Therefore the fresh-`n=5`
G13 closure is exact, while the whole-cell conclusion (0.3) remains gated
by review of both the G12 parent and this producer.

No statement is made about `h10>=2`, `h10=infinity`, another `(e,m)`, a
different K00 support, nonreduced scheme-valued points, lifting, an infinite
compatible jet, a formal arc, source reachability, algebraization, a
polynomial Keller map, a counterexample, or JC2.

## 7. Deterministic replay

Run

```text
python3 -B xmodel/k00-ram-e2m2-h10eq1-g13-closure-replay-sol56-20260830.py
python3 -B -O xmodel/k00-ram-e2m2-h10eq1-g13-closure-replay-sol56-20260830.py
```

Both modes print identically:

```text
K00_RAM_E2M2_H10EQ1_G13_CLOSURE_REPLAY=PASS
TAIL_TERMS=569
GENERAL_G13=LITERAL_FRESH_N5;ROWS=51,55,57,33,56,15,51
ROW6_WALL=P4=s^4-384*s^2*t^2+4096*t^4
N5_RANK1=BOTH_SIGNS_DEAD_G13;P4=32768*t^4
N5_RANK2=ALL_G12_SURVIVORS_DEAD_G13;SECOND_TERMINAL=s*t*(s^2-64*t^2)
CONTROL_RANK1=G0_G12_PASS;G13_ROW6=-21/64;BOTH_SIGNS
CONTROL_RANK2=G0_G12_PASS;N8_B=32;ONLY_G13_ROW6=21/524288
CELL_STATUS=FRESH_N5_EMPTY_G13;FULL_H10EQ1_CLOSURE_CONDITIONAL_ON_G12_PARENT
CERTIFICATE_BYTES=2899
CERTIFICATE_SHA256=3bb22822763ecdf6cb19e083786fffbd0f1ad4f4a3f83b937f7ef69d8ca4202e
MUTATIONS=CUSTODY,G13_FORMULA,ROW6,RANK1_SIGNS,RANK2_INVERSE,RANK2_CONTROL,N8_IMAGE
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9494`.
- Body SHA-256:
  `82c277ca01460a6a1cfe05e79ec5b3ed2cce95b520ad0d287f3b8c62ab088cfd`.
- Frozen basis: `a619157b73c1dee1ca0599db47321ffd7588d748`.
