# AS-source-transformed `B8` gives an exact `(8,12)` `Z/27` survivor

Status: **PRODUCER-EXACT / DUAL-AWS REPLAY / HOSTILE REVIEW PENDING**.

## Result

Over `F_3`, put

```text
u=x+y^4,
B8=(u,y+u^2),
G8=(y+u^2,u^3-u).
```

The source map `B8` and the target reorder `T8(s,t)=(t,-s)` are polynomial
automorphisms of determinant one over `Z`; `G8=T8 o (s-s^3,t) o B8` is
etale and noninjective.  The exact integer pair

```text
P=y+u^2+3*(2*x*y^5+x^2*y)
        +9*(2*x*y^6+x^3*y^5+x^4*y),
Q=u^3-u+9*x*y^9
```

has actual total and partial `y`-degree pair `(8,12)`, reduces to `G8`, and
satisfies every coefficient equation of

```text
det J(P,Q)=1 mod 27.
```

Thus the complementary primitive maximum-twelve residue seed has a genuine
fixed-D12 finite branch through `W3=Z/27`, alongside the independently frozen
deeper `B9` branch.  This is a finite-depth survivor, not a counterexample.

## Complete transported gate

For a digit `(R,S)`, direct linearization at the integer seed and the
transported AS operator agree modulo three:

```text
D8(R,S)=J(y+u^2,S)+J(R,u^3-u)
       =-y^3*R_x+R_y-(1+2*u*y^3)*S_x+2*u*S_y.
```

The registered coordinate space is source-complete for the exact degree
pair inside total D12:

```text
R: i+j<=12, j<=8       81 slots,
S: i+j<=12, j<=12      91 slots.
```

All 276 determinant positions through total degree 22 are retained.  The
resulting 276-by-172 operator has rank 104 and nullity 68.  The V2 replay
checks the formula against the direct Jacobian on every one of the 172 basis
columns.

The deterministic complete W2 solve gives

```text
R2=2*x*y^5+x^2*y,       S2=0.
```

For `P2=P0+3R2,Q2=Q0+3S2`, exact integer division yields

```text
(det J(P2,Q2)-1)/9
 = -3*y^8+8*y^16+14*x*y^12+3*x^2*y^8-4*x^3*y^4-x^4.
```

Its negative modulo three is `u^4`.  The complete W3 equation
`D8(R3,S3)=u^4` is consistent, and deterministic RREF gives

```text
R3=2*x*y^6+x^3*y^5+x^4*y,
S3=x*y^9.
```

Literal integer expansion then verifies the claimed determinant congruence,
the exact degrees, and the collision `(0,0),(1,2)->(0,0)` in the special
fibre.  The parent W2 point without the `9`-digit is not determinant one
modulo 27.

## Custody

Case:
`cases/as_b8_max12_w3_gate_aws_20260825/`.

The preregistered V1 182-slot calculation is preserved only as a negative
control: its particular solution raised the first coordinate above
`y`-degree eight and failed the frontier assertion.  V2 was separately
preregistered before execution with the exact 81+91 coordinate envelope.

Box02 and Box03 both returned rc zero in 0.04 seconds, with maximum RSS
15,616 and 15,784 KiB.  Their stdout is byte-identical at SHA-256

```text
68bb935820310f79d39f8cd342de2c428ff2cced1ee986795600a61af2a7c604
```

and both print canonical payload SHA-256

```text
5c9219e497e7cc14017a9fefc395aaaddcf420ccb8911b0db77c9b0b6985384f.
```

## Scope firewall

This report proves only existence of one explicit determinant-one pair over
`Z/27` with fixed total-D12 support and exact degree pair `(8,12)`.  It does
not classify the full W2 fibre or its 68-dimensional kernel, continue to
`Z/81`, supply a compatible inverse system, produce a `Z_3` or
characteristic-zero polynomial map, prove nonautomorphy, enter selected Q8
or TD6, close either maximum-twelve frontier, or prove or disprove JC2.

The exact next producer gate, if allocated, is the complete W4 digit over
this frozen W3 point in the same 172-slot coordinate envelope.  A survivor
would still be finite-depth evidence only; an obstruction would kill only
this point unless globalized over the W2/W3 kernel scheme.
