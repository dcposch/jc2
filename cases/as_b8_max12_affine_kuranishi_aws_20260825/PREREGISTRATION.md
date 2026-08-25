# Preregistration — B8 complete affine `W2 -> W3` Kuranishi gate

Date: 2026-08-25

This producer consumes only the frozen B8 fixed-D12 source
`cases/as_b8_max12_w3_gate_aws_20260825/replay_v2.py`, whose required
SHA-256 is

```text
691c89fc78dbbdb053449e0c26df326a5b459ab8de28b333cbd5329f48168a13.
```

All substantive execution is AWS-only.  The two primary endpoints use the
same pinned source on different AWS hosts; the compiler itself compares two
independent constructions of the obstruction (exact determinant
interpolation and the analytic polarization identity).

## Registered source space

Retain the complete degree-compatible D12 envelope and every determinant
row:

```text
R: i+j <= 12, j <= 8       81 coefficients,
S: i+j <= 12, j <= 12      91 coefficients,
all fresh digits             172 coefficients,
Jacobian rows through D22    276 rows.
```

For the integer seed `F0=(P0,Q0)` and a first digit `T=(R,S)`, write

```text
F2 = F0 + 3*T.
```

The full `W2` equation is the affine equation

```text
D8(T)=u^2  over F3,
```

where `D8` is the direct 276-by-172 determinant linearization.  Compute a
canonical particular solution `T0`, the full kernel `K`, its rank/nullity,
and verify every kernel vector against all 276 direct rows.  Parameterize
the complete fibre by unreduced integer lifts

```text
T(t)=T0 + sum_i t_i*K_i,  t_i in F3.
```

Using unreduced lifts is mandatory: it makes coefficientwise division by
three literal and avoids a non-polynomial canonical-digit carry.

## First nonlinear gate

For a fresh digit `W`, the exact determinant expansion is

```text
det(F0+3*T+9*W)-1
 = det(F0)-1 + 3*L(T) + 9*J(T)
   + 9*L(W) + 27*cross(T,W) + 81*J(W).
```

Thus the complete `W3` compatibility condition is the cokernel-valued
quadratic

```text
kappa(t) = pi((det(F0+3*T(t))-1)/9) = 0,
```

where `pi` is the full left cokernel of `D8`.  Compile every constant,
linear, square, and cross coefficient in all 68 predecessor parameters.
Construct it twice:

1. analytically from `L(K_i)/3`, polarization, and `J(K_i)`;
2. independently by exact determinant evaluations at `0`, `e_i`, `2e_i`,
   and `e_i+e_j`, followed by interpolation over `F3`.

The two canonical ANFs must agree byte-for-byte.  Record the polynomial-span
rank, degree histogram, pure-linear consequences, tangent rank at the frozen
point, and every source/target dimension.  Replay at least one literal
compatible point through all 276 integer determinant rows modulo 27 and
audit actual total/partial degrees.

If `kappa` is zero or affine-linear, continue the complete affine family to
the next digit.  If it is genuinely quadratic, stop the digit ladder and
classify/solve this entire quadratic zero locus before following any one
selected point.  A solver result is accepted only with reconstructed digit
vectors and exact determinant replay.  UNSAT requires an independently
checkable certificate; a finite sample never licenses a full-fibre claim.

## Scope firewall

This is a finite fixed-D12 Witt/Kuranishi calculation.  A survivor at any
reported depth is neither an inverse-limit branch nor a `Z_3`/characteristic
zero map, counterexample, maximum-twelve theorem, selected-Q8/TD6 landing,
or JC2 conclusion.  Any obstruction applies only to the precisely stated
affine predecessor family and degree envelope.

