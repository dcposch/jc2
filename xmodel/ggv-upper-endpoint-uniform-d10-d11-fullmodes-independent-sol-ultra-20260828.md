# Independent uniform full-mode replay and extension through `D11`

Date: 2026-08-28  
Lane: independent exact desk replay  
Packet: `cases/ggv_8_28_upper_endpoint_uniform_d10_fullmodes_audit_20260828/`

## Verdict

**PASS through D11, for characteristic-zero field points.**  I independently
reconstructed the fractional-power recurrence and evaluated source-level
mutations against the authoritative 303-variable, 513-generator branch-P
JSON.  The provisional D8/D9 conclusions reproduce exactly, and the next two
rows give

```text
D10: A | (F5-R/2-Z*V/64),
D11: F5=R/2+Z*V/64+A^2*Q and c10=0,
```

where `W=A*R` follows D9 and `A=X^4-1`.

The cross term `Z*V/64` is load-bearing in the uniform fixture.  The shorthand
`F5-R/2` is correct only after explicitly shifting the `F5` coordinate or in a
specialization where `Z*V=0`.

## 1. Custody and method

The proof source is

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
```

The charged provisional D9 script and result are recorded byte-for-byte in
`RESULT.json`, but are not imported by the checker.  The checker has two
independent exact representations:

1. sparse Laurent polynomials in `A` with generic polynomial coefficients;
2. ordinary `Q[X]` arithmetic evaluating all 513 literal serialized
   generators and a separately reconstructed determinant recurrence.

All arithmetic uses the Python standard library's `fractions.Fraction`.

## 2. Complete characteristic schedule

The continuation is

```text
F^(3/2)
+ c4  t^4  F
+ c6  t^6  F^(3/4)
+ c8  t^8  F^(1/2)
+ c10 t^10 F^(1/4)
+ c12 t^12
+ c14 t^14 F^(-1/4)
+ c16 t^16 F^(-1/2)
+ c18 t^18 F^(-3/4)
+ c20 t^20 F^(-1).
```

At D10 and D11 only `c4,c6,c8,c10` have causal support.  The later four
negative modes are nevertheless retained as mandatory continuation
coordinates.  The packet replays both literal gauge points

```text
F=(A^2+t/2)^2+t^8,
```

which require `c16=+3/8` and `c16=-3/8`, respectively.  Both points satisfy
the raw determinant rows D4 through D22 before the affine target fold, and
all 513 serialized generators match direct recurrence evaluation.

## 3. Independent D8/D9 replay

After `T=A*V` and

```text
F4-V/16-Z^2/64=A*W,
```

the exact polar parts are

```text
polar(g8)=3*c6/(32*A),

polar(g9)|_(c6=0)
  =-3*W^2/(16*A^2)
   +(3*F5*W/4-3*V*W*Z/256)/A.
```

With `D_raw=-L_n(polar)` and

```text
L_n(P)=4(12-n)A^3*A'*P-8A^4*P',
```

the source-row congruences are

```text
D8=-(9/4)c6*A^2*A'       (mod A^3),
D9=+(21/4)A*A'*W^2       (mod A^2).
```

Thus D8 kills `c6`, and D9 then forces `A|W` field-radically.

## 4. D10 square defect

Write `W=A*R`.  The square root is completed through weight four:

```text
F^(1/2)
 =A^2+t/2+(Z/8)t^2+(V/16)t^3+(R/2)t^4
  +(Delta5/(2A^2))t^5+...,

Delta5=F5-R/2-Z*V/64.
```

The complete born-mode list at D10 is

```text
c4*F6,  c6*(F^(3/4))_4=0,  c8*Z/8,  c10*A.
```

Every term is polynomial, and the base polar part is exactly

```text
polar(g10)=3*Delta5^2/(8*A^2).
```

Therefore

```text
D10=-9*A*A'*Delta5^2     (mod A^2),
```

so squarefreeness of `A` gives `Delta5=A*S` on field points.  There is no
D10 mode kill.

A live source mutation sets `Delta5=1`; rows D4 through D9 vanish and the
literal D10 row is `-9*A*A'`.  Scaling by `-1` and `2` gives the exact square
law.  A second mutation takes `Z=V=1,R=0`; the exact square has `F5=1/64`.
Dropping that coefficient while continuing through G9 yields
`D10=-(9/4096)A*A'`, catching omission of `Z*V/64`.

## 5. D11: second divisibility, then `c10=0`

Put

```text
Delta5=A*S,
Delta6=F6-R*Z/8-V^2/256.
```

The complete polar part is

```text
polar(g11)
 =-3*S^2/(16*A^2)
  +(c10/4+(3/4)*S*Delta6)/A.
```

The raw row first gives

```text
D11=+(15/4)A*A'*S^2      (mod A^2),
```

and hence `S=A*Q` field-radically.  After this substitution, every base
order-one term is polynomial.  The `c4*F7` and `c8*V/16` modes are also
polynomial, `c6=0`, and `c12` has not yet been born.  The only remaining pole
is therefore `c10/(4*A)`, with

```text
D11=-3*c10*A^2*A'        (mod A^3).
```

Thus `c10=0`.  Literal mutations independently reproduce both signs and row
images, and identify every nonzero D10/D11 generator by zero-based source
index, per-generator SHA-256, and per-row SHA-256 in `RESULT.json`.

## 6. Scope

The output proves a uniform field-radical prefix cascade only.  It does not
prove scheme-theoretic divisibility, endpoint-stratum emptiness, unrestricted
branch-P exclusion, a Keller-pair theorem, or JC2.  No downstream row beyond
D11 is claimed.
