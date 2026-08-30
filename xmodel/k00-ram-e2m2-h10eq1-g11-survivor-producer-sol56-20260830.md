# Normalized K00 `e=2,m=2,h10=1` boundary through G11

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra  
Frozen campaign basis: `0d7544ebd5cb12def6bac892646010301098be3c`  
Lifecycle: **EXACT PRODUCER / G11 NONEMPTY CONTROL / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

On the normalized generic K00 support, put

```text
Lambda=tau^2,       C6=1,       ord_tau(d)=2,
k10=tau*kappa+O(tau^2),          kappa!=0,
Jdet[0]!=0.                                             (0.1)
```

The proposed one-grade closure of this boundary child does **not** occur.
Literal extraction from all 569 V20R2 tails gives

```text
V(G0,...,G11) intersect V(k10[0]) intersect D(k10[1])
                intersect {d[2]!=0} != empty.            (0.2)
```

There are at least two distinct exact survivor mechanisms:

1. the old `n=4` rank-one branch has G11 prefixes for both Gaussian signs;
2. after its rank-zero transition, the fresh `n=5` cone has rank-two and
   rank-one G11 survivors.  Only its rank-zero stratum dies at G11.

An especially small rational fixture is

```text
S=tau^2,        T=0,
N5=(2,0,0,0,-1,0),
N6=(-5/12,0,0,0,0,0),
k10=tau,        Jdet=1,                                (0.3)
```

with `d=D(S,T)+tau^5*N5+tau^6*N6`.  Every one of the seven literal rows
vanishes in G0--G11.  Thus G12, not G11, is the next unresolved coefficient
gate for this source-partition child.

This is finite-prefix nonemptiness only.  The fixture is not asserted to
extend to a formal arc, to be reachable from closure data, or to come from a
polynomial Keller map.

## 1. Custody, source, and exact arrival census

The charged inputs and this replay are

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  frozen tails.json, 569 monomials
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  exact sparse Q(i) source engine
fa5a4ef6a1b2c0640c6363b84e6b547a044920b15249f7c72b25ffbcda2c1733
  e2m2 G10 producer
efd2f4fea4f58ee4783d9b373ee68f2ff191a9923b08bf2ead8dd1c59a4d3749
  e2m2 G10 replay
4710349b6082623213a6074cb92ebc7944fb5ce751a06112f2fa560e043bb69c
  Fable 5 hostile confirmation of the G10 fan
9a94cd3bc58c04331b430f66d6fbabaa41ccee1eebcb4f18315e514fc0850c65
  general ramified calendar/meta gate
d5e458d2c430cc85be86b711e37355671090057881474458055dbf7f593609c3
  xmodel/k00-ram-e2m2-h10eq1-g11-survivor-replay-sol56-20260830.py
```

With `k10[0]=0`, the literal source through G11 is

```text
R(d)+tau^4*(tau*kappa+tau^2*kappa2+...)*A10(d).     (1.1)
```

K6, K2, and all targets remain beyond G11 by the already reconstructed
calendar.  On the centered `n=4` chart the complete coefficient census is:

- surface coefficients `S2,T2,S3,T3` can reach G11; `S4,T4` cannot;
- normal coefficients `N4,N5,N6,N7` can reach G11; `N8` cannot;
- `k10[1]=kappa` can reach G11; `k10[2]` first reaches G12.

The replay retains every coefficient in the first two lines, retains
`k10[2]` as a negative control, and verifies its literal absence.  It does
not obtain G11 by shifting the reviewed G10 display.

## 2. Literal general G11 coefficient

Write the exact graph-normal decomposition

```text
S=s*tau^2+alpha*tau^3+...,
T=t*tau^2+beta*tau^3+...,
N=tau^4*w+tau^5*v+tau^6*u+tau^7*z+... .            (2.1)
```

Let `ell2=ell(s,t)`, `ell3=ell(alpha,beta)`, let `Q=R^[2]` and
`R3=R^[3]`, and let `M4=A10^[2]`.  Define the exact surface cubic

```text
W_r(s,t)=D M4_r(ell2)[mu(s,t)]+A10_r^[3](ell2),     (2.2)
```

where `D(S,T)=ell(S,T)+mu(S,T)`.  Direct extraction of each literal source
row gives

```text
G11_r = DQ_r(w)[z] + DQ_r(v)[u]
       +D^2 R3_r(ell2)[w,v]
       +(1/2)D^2 R3_r(ell3)[w,w]
       +kappa*(D M4_r(ell2)[w]+W_r(s,t)).           (2.3)
```

The seven raw G11 polynomials have respectively

```text
36, 39, 41, 33, 39, 12, 34
```

sparse terms before lower-equation specialization.  Equation (2.3) is
checked as exact polynomial equality row by row.  In particular, the
`alpha,beta` terms are genuinely retained, and `k10[2]` is genuinely absent.

## 3. The inherited tree through G10

The different-model-confirmed G10 fan remains valid through every step that
did not use `k10[0]!=0`:

| first normal order | rank | boundary-child decision |
|---|---:|---|
| `n=2` | 2 or 1 | dead at G6 |
| `n=2` | 0 | recenter to `n>=3` |
| `n=3` | 2 | dead at G8 |
| `n=3` | 1 | genuine odd G8 component, dead raw at G9 |
| `n=3` | 0 | recenter to `n>=4` |
| `n=4` | 2 | dead at G10 by the K10-free `C,E` identities |
| `n=4` | 1 | survives G10 when the old `k10[0]` terminal is deleted |
| `n=4` | 0 | `G10=Q(N5)`; recenter to the fresh `n=5` cone |

On the `n=4` rank-one sign chart

```text
p=epsilon*8i*q, q!=0,
B(N5)=epsilon*8i*A(N5),
```

the reviewed G10 compatibility equations force

```text
s=epsilon*8i*t,       A(N5)=B(N5)=0.               (3.1)
```

The old terminal was
`-epsilon*(5i/16)*k10[0]*t^3`; it vanishes identically on the present face.
Section 5 gives a literal G11 survivor on each sign chart, so no hidden G10
obstruction is being inferred away.

## 4. Complete fresh-`n=5` reduced G11 fan

After the rank-zero recentering, put

```text
N=tau^5*w+tau^6*v+...,
w=(2p,0,0,q,-p,4q),
A=A(v),       B=B(v),
Delta=p^2+64q^2.                                    (4.1)
```

Literal extraction, with `S3,T3,N7,k10[2]` retained and verified absent,
is

```text
G10=Q(w),
G11=DQ(w)[v]+kappa*W(s,t).                          (4.2)
```

Only two row coordinates are independent:

```text
G11_1=(3/1024)(p*A-q*B)+kappa*W1,
G11_2=(3/16384)(64q*A+p*B)+kappa*W2,                (4.3)

G11_3=-(1/8)G11_1,   G11_4=0,
G11_5=-(1/128)G11_1, G11_6=0,
G11_7=-(1/1024)G11_1,                               (4.4)
```

where

```text
W1=(5/4096)t(3s^2-64t^2),
W2=(5/65536)s(s^2-192t^2).                          (4.5)
```

These are literal identities, not a recurrence from an earlier cell.

### Rank two

On `D(Delta)`, set

```text
U=-(1024/3)kappa*W1,       V=-(16384/3)kappa*W2.
```

The unique solution of (4.3) is

```text
A=(pU+qV)/Delta,
B=(-64qU+pV)/Delta.                                 (4.6)
```

The replay checks both cross-multiplied matrix identities.  Hence every
rank-two cone point extends through G11; this stratum survives.

### Rank one

On `p=epsilon*8i*q`, `q!=0`, the only compatibility equation is

```text
G11_2+(epsilon*i/2)G11_1
 =kappa*(5/65536)*(s+epsilon*8i*t)^3.               (4.7)
```

Thus reduced field-valued support requires and permits

```text
s=-epsilon*8i*t.                                    (4.8)
```

The leading-surface open then gives `t!=0`; the remaining one-dimensional
image equation determines one linear combination of `(A,B)`.  Both signs
therefore survive G11.  Notice that (4.8) is the wall opposite to the
`n=4` rank-one wall (3.1).

### Rank zero

At `p=q=0`, the image term vanishes and G11 is `kappa*W`.  Since `kappa` is
a unit, (4.5) would require `W1=W2=0`.  If `s=0` or `t=0`, the other
equation kills the remaining coordinate.  On `D(st)`, the two equations
require both

```text
s^2=(64/3)t^2,             s^2=192t^2,
```

which is impossible in characteristic zero.  Thus rank zero is empty on
`(s,t)!=(0,0)`, including the exact-graph branch `ord(N)>5`.

## 5. Two independent literal survivor controls

Use

```text
V(A,B;y1,y2,y3,y4)
 =(B+4y2-2y4,y1,y2,y3,y4,A-16y1+4y3).             (5.1)
```

The rational fresh-`n=5` fixture (0.3) has `p=1,q=0`, `A(N6)=0`, and
`B(N6)=-5/12`, exactly the specialization of (4.6).  All seven rows pass
G0--G11.  Replacing `-5/12` by `-5/13` makes G11 nonzero.

For each `epsilon in {+1,-1}`, a separate old-`n=4` rank-one fixture is

```text
S=epsilon*8i*tau^2,       T=tau^2,
N4=(epsilon*16i,0,0,1,-epsilon*8i,4),
N5=V(0,0;5/72,0,0,0),
N6=V(0,-128;0,0,0,0),
N7=V(0,320/9;0,0,0,0),
k10=tau,                  Jdet=1.                  (5.2)
```

Again all seven literal rows pass G0--G11 for both signs.  Replacing the
`5/72` entry by zero while retaining the other displayed data makes G11
nonzero.  These controls exercise two different branches of the transition
tree and make the nonemptiness conclusion insensitive to a single chart.

## 6. Exact conclusion and next gate

The `h10=1` child is not eliminated at its first surface-load grade.  The
sharp result is

```text
POINT_SET_NONEMPTY_THROUGH_G11;
FORMAL_ARC_STATUS_OPEN;
NEXT_LITERAL_GATE=G12.                              (6.1)
```

A G12 attack must retain at least the next normal blocks on both survivor
mechanisms, the next surface coefficients, `k10[2]`, and every unloaded
quartic/cubic term that first reaches that grade.  The two fixtures in
section 5 are useful controls but their zero continuations are not evidence
for or against extendability: fresh G12 coefficients may change every raw
G12 remainder.

No conclusion is made about `h10>=2`, `h10=infinity`, another `(e,m)`, a
different K00 support, nonreduced scheme-valued points, lifting, source
reachability, algebraization, a polynomial map, a counterexample, or JC2.

## 7. Deterministic replay

Run

```text
python3 -B xmodel/k00-ram-e2m2-h10eq1-g11-survivor-replay-sol56-20260830.py
python3 -B -O xmodel/k00-ram-e2m2-h10eq1-g11-survivor-replay-sol56-20260830.py
```

Both modes print identically:

```text
K00_RAM_E2M2_H10EQ1_G11_SURVIVOR_REPLAY=PASS
TAIL_TERMS=569
GENERAL_G11=LITERAL_N4_FORMULA;ALL_CAPABLE_SLOTS_RETAINED;K10_2_ABSENT
N4_RANK1=G11_SURVIVOR_BOTH_SIGNS
N5_G11=RANK2_SURVIVES;RANK1_SURVIVES_ON_OPPOSITE_WALL;RANK0_DEAD
FIXTURE_N5=S2=1;T2=0;P5=1;Q5=0;A6=0;B6=-5/12
FIXTURE_N4=S2=EPS*8i;T2=1;Y1_5=5/72;B6=-128;B7=320/9
CELL_STATUS=POINT_SET_NONEMPTY_THROUGH_G11;FORMAL_ARC_OPEN
CERTIFICATE_BYTES=2656
CERTIFICATE_SHA256=d83eeb1db7e7d092eaa5cb23016e73ebcf72835024300d679316121a9518d817
MUTATIONS=CUSTODY,WALL_SIGN,N5_B,N4_Y1
```

The replay uses Python stdlib exact rational/Gaussian-rational arithmetic,
writes no files, and completes in about two seconds.  It imports the charged
exact sparse engine and the reviewed e2m2 helper layer; different-model
review remains mandatory before promotion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9996`.
- Body SHA-256: `a0104064a049911d4bc732245b53d653a093acffa9019116dca58092abdd9865`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
