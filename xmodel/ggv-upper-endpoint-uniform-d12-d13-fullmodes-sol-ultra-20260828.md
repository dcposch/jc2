# Uniform full-mode continuation through `D13`

Date: 2026-08-28  
Packet: `cases/ggv_8_28_upper_endpoint_uniform_d12_d13_fullmodes_20260828/`

## Verdict

**PASS through D13 on characteristic-zero field points.**  Continue the
frozen D11 prefix as

```text
F4=V/16+Z^2/64+A^2*R,
F5=R/2+Z*V/64+A^2*Q,
c6=c10=0.
```

Put

```text
Delta6=F6-Q/2-R*Z/8-V^2/256.
```

The complete born-mode calculation gives

```text
polar(g12)=3*Delta6^2/(8*A^2),
D12=-6*A*A'*Delta6^2                 (mod A^2).
```

Thus squarefreeness of `A=X^4-1` gives `Delta6=A*S`.  There is no D12
mode kill: the born contributions `c4*F8`, `c8*R/2`, and `c12` are
polynomial, while `c6=c10=0`.

At the next row, define

```text
Delta7=F7-Q*Z/8-R*V/16.
```

Then

```text
polar(g13)=-3*S^2/(16*A^2)+(3*S*Delta7)/(4*A),
D13=+(9/4)*A*A'*S^2                  (mod A^2).
```

Hence `S=A*T`.  After this substitution the complete D13 continuation is
polynomial, so there is no second mode consequence.  The combined prefix is

```text
F6=Q/2+R*Z/8+V^2/256+A^2*T.
```

The checker uses the frozen D10/D11 arithmetic library by pinned hash and
independently evaluates every live mutation against all 513 generators of
the authoritative raw JSON.  D12 and D13 square-law mutations at scalars
`-1,1,2` fix both signs.  An exact-square mutation with `Z=V=1,R=Q=X`
requires

```text
F6=1/256+(5/8)X;
```

removing it while continuing through G11 produces the predicted literal D12
residual and guards every term of `Delta6`.

The nine-mode continuation remains intact.  `c12=G12[X^0]` is an exact
global additive gauge: setting it to one leaves D4 through D22 zero before
the affine target fold.  The forced modes `c14,c16,c18,c20` are retained and
not assigned zero.

This is a field-radical prefix theorem only.  It gives no scheme-level
divisibility, endpoint exclusion, Keller-pair theorem, or JC2 conclusion.
