# Registration — AS-source-transformed `B8` fixed-D12 `W2 -> W3` gate

- Registered UTC: `2026-08-25T16:17:12Z`, before any CAS/linear-algebra run.
- Trigger: sealed 1550Z cross-pollination; complementary to the frozen `B9`
  finite branch.
- Execution policy: every replay/solve runs on AWS.  Local work is limited to
  source derivation, editing, hashing, transfer, and log inspection.

Over `F_3`, put

```text
u=x+y^4,
B8=(u,y+u^2),
T8(s,t)=(t,-s),
G8=T8 o (s-s^3,t) o B8=(y+u^2,u^3-u).
```

Both `B8` and `T8` have determinant one over `Z`.  The registered canonical
integer lift is

```text
P0=y+u^2,
Q0=u^3-u,
det J(P0,Q0)=1-3*u^2.
```

The full digit space in each coordinate is every monomial `x^i y^j` with
`i+j<=12`: 91 slots per coordinate, 182 variables total.  Every coefficient
row of the determinant through total degree 22 is retained (276 registered
rows before literal-zero removal).

For a digit `(R,S)`, the transported first-Cartier operator in original
coordinates is

```text
D8(R,S)
 = -y^3*R_x + R_y -(1+2*u*y^3)*S_x + 2*u*S_y       (mod 3).
```

It must agree coefficientwise, on all 182 basis vectors, with the direct
linearization

```text
J(P0,S)+J(R,Q0) mod 3.
```

The preregistered structured `W2=Z/9` point is

```text
P2=P0+3*u^2*y,
Q2=Q0,
det J(P2,Q2)=1-9*u^4.
```

The complete next-digit problem over this one `W2` point is therefore

```text
D8(R3,S3)=u^4 mod 3,
P3=P2+9*R3,
Q3=Q2+9*S3,
```

with `(R3,S3)` allowed in all 182 D12 slots.  The solver must compute exact
rank/augmented rank, choose a deterministic RREF particular if consistent,
and then verify the literal integer determinant modulo 27, source reduction,
actual total/partial degrees `(8,12)`, and omission of the full 9-digit.

Acceptance is either:

1. one explicit fixed-D12 `Z/27` survivor with an exact determinant replay;
   or
2. inconsistency of this complete 182-variable next-digit system, which
   obstructs only the registered structured `W2` point.

Neither outcome classifies the whole `W2` fibre, supplies an inverse limit,
enters selected Q8 or TD6, constructs a characteristic-zero map, or proves a
counterexample/JC2 statement.
