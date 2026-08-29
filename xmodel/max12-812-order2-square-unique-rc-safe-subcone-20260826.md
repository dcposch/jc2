# `(8,12)` order-two square fan: a uniform safe subcone of unique `RC`

Date: 2026-08-26

Status: **HAND LOCAL TRUNCATED-DIVISIBILITY REDUCTION, CONDITIONAL ON
COMPLETE SOURCE/FABER SUPPORT AND COEFFICIENT REPLAY.  NO BRANCH VERDICT.**

## Parametrization

Work on the unit-load generic-square chart `D(p*k0)`.  In the unique-`RC`
cell put

```text
x=a-r-1>=1,       y=c-r-1>=1.
```

The remaining strict lower-face inequalities are

```text
y<=r-3,           y<=2*x+3.                         (1)
```

Conditional on exact replay, this note eliminates the subcone

```text
2*y <= r+x+3.                                      (2)
```

The complementary region `2*y>=r+x+4` remains live.

## Root allocation and target

The first `RC` equation gives `L|R0*C0`.  Over the etale root algebra orient

```text
L0=u0*v0,  R0=beta*u0,  C0=gamma*v0,
beta*gamma!=0.                                     (3)
```

At the local ring `u0=0`, the first `C2` term occurs at gap `y` and is

```text
(3/8)*C0^2/L0^2=(3/8)*gamma^2/u0^2,                (4)
```

a nonzero double pole.

The primary successor gaps relative to `RC` are

```text
AC:      x,
C2:      y,
R3:      r-y-2,
A2:      4+2*x-y,
RA2:     r+2+2*x-y,
kR2A:    r+2+x-y,
A3:      r+6+3*x-y,
kAC:     4+x,
RAC:     r+2+x,
RC2:     r+y+2.                                    (5)
```

## Pole audit under (2)

All terms with denominator at most `L` join one local simple-pole block.
Vanishing of its negative coefficients through gap `y-1` gives truncated
divisibility by the moving root `u(sigma)`; its gap-`y` coefficient has at
most a simple pole.  This argument is for the sum of the terms and includes
moving-root connections and cancellations.

The only higher-denominator terms which could reach (4) are `RA2` and
`kR2A`:

- `RA2=R*A^2/L^2` starts with one `u0` factor from `R0`, hence has at most a
  simple pole at first appearance.  By (2),

  ```text
  (gap_RA2)-y = r+2+2*x-2*y >= x-1 >= 0,
  ```

  so no correction of `RA2` occurs before the target.
- `kR2A=k0*R^2*A/L^2` starts regular at `u0=0`; its first correction has at
  most a simple pole and only its second correction can have a double pole.
  Again by (2),

  ```text
  (gap_kR2A)-(y-1) = r+x+3-2*y >= 0,
  ```

  so at most the first correction can reach the target.

Equation (1) also puts `A3`, `RAC`, and `RC2` strictly after gap `y`:

```text
(gap_A3)-y >= 6+x,
gap_RAC>y,
gap_RC2>y.
```

Thus every competitor at gap `y` has pole order at most one at `u0=0`,
while (4) has nonzero order two.  Polynomiality is impossible throughout
the subcone (2).  The deck-conjugate orientation is identical.

## Exact client acceptance test

A symbolic dual-field client should fail closed unless it verifies:

1. all seven complete source rows and the moving lower-unitriangular bridge
   through the first `RC` grade plus `y`;
2. the parametrization (1), gap table (5), and inequality deductions without
   finite-box sampling;
3. the local simple-block truncated-division identity for every denominator-
   `L` term and moving correction;
4. the exact correction-level pole bounds for `RA2` and `kR2A`, including a
   fail-closed control in the complementary region where a double pole can
   return;
5. the nonzero coefficient `3/8` in (4), both root orientations, exact `Q`,
   and one good-prime software control.

## Firewall

Conditional on exact replay, this note eliminates only the unique-`RC`
subcone (2).  It does not eliminate the complementary unique-`RC` region,
unique `AC`, a tied first face, positive-order or ramified loads, `p=0`,
`k0=0`, the exact-square zero section, terminal/Taylor conditions, fan
exhaustiveness, order two, maximum twelve, or JC2.
