# Result: generic affine-Faber parity/J data

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER PASS.  CHARACTERISTIC-ZERO COMPLETE-LOCAL HAND
THEOREM; HOSTILE REVIEW AND LITERAL TOTAL-REES CONSUMPTION GATE PENDING.**

## Runs

The V2 exact-Q producer and characteristic-65521 software control both
completed with

```text
compiler_rc=0
engine_rc=0
validator=PASS_GENERIC_J_EXCLUSION_DATA
```

under tags

```text
max12_812_order2_faber_generic_j_20260826T131212Z_q_v2
max12_812_order2_faber_generic_j_20260826T131212Z_p65521_v2.
```

Each Singular run took less than 0.01 seconds, used at most 11,876 KiB RSS,
and reported zero swaps.  Every non-determinant endpoint line is literally
identical between the two fields.  The determinant factorization differs
only by reduction of coefficients modulo 65521.

## Exact endpoint

The compiler starts from the frozen complete ordinary Faber tails and the
exact coefficient presentation

```text
F=Q^2+N,
Q=z^4+p*z^2+c*z+r,
N=n3*z^3+n2*z^2+n1*z+n0,
u=n1-(p/2)*n3.
```

It verifies the polynomial inverse from the seven centered octic
coefficients, so `(c,u,n3)` are all odd coefficient directions.  It then
verifies exact parity of all seven rows and the corrected affine graph

```text
beta=(5*D-s)/4,
gamma=D*(5*D-4*s)/16,
mu2=D^2*s/32.
```

For rows `(R1,R3,R5)` and columns `(c,u,n3)`, both lanes reproduce the
registered matrix

```text
          c                 u                    n3
R1        a                 C/4                  0
R3       -p*a/4            -p*C/16               K/4
R5        a*A0              (C*A0+K)/4           -p*K/16,
```

where

```text
a=D*(5*D+2*s)/32,
C=(5*D-3*s)/4,
K=5*D*(5*D-2*s)/16,
A0=-p^2/32-D/4.
```

The exact determinant check is

```text
det=-a*K^2/16
   =-25*D^3*(5*D+2*s)*(5*D-2*s)^2/2^17.
```

Thus it is a unit on

```text
D(D*(5*D+2*s)*(5*D-2*s)).
```

The same source replay confirms that the `A` face has rank two with its
sole kernel `R7`-null, while the `K` face has rank one and its entire
two-dimensional kernel is `R7`-null.  It also confirms the raw cubic and
quintic transverse identities before any radical or saturation.

Together with parity and the formal implicit-function theorem, the exact-Q
data support the characteristic-zero statement that, in the completed
normalized ordinary-Faber coefficient space on the generic open,

```text
(R1,R3,R5)=(c,u,n3),
R7=0,
((R1,R3,R5,J-4*R7):J^infinity)=(1).
```

The hand proof is frozen separately at

```text
fe1193abe8c45c590f7653d96998a7b053e8de0e09a751cd8fb686d2cbf72fc1
  xmodel/max12-812-order2-exact-square-affine-faber-generic-j-exclusion-theorem-20260826.md
```

## Scope firewall

This result concerns the normalized ordinary-Faber coefficient space.  It
does not yet discharge the literal total-Rees consumption gate: the
two-sided `k10` normalization, every Rees power, any moving-center gauge,
torsion, and all target/load directions must be shown to pull back to this
face without an omitted odd direction.  It does not classify either
exceptional divisor, `Delta=0`, or `k10=0`; run terminal `[6,2]` or either
Taylor family; close order two, `(8,12)`, maximum twelve; or prove or
disprove JC2.

The V1 parser failure is immutable deployment-negative custody in
`NEGATIVE_V1.md` and is not evidence for any mathematical claim.

