# Uniform full-mode `D8` mode kill and `D9` square defect

Date: 2026-08-28  
Producer: Sol Ultra, exact independent desk lane  
Certificate packet:
`cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/`

## Verdict

**TWO EXACT FIELD-POINT THEOREMS.**  On a characteristic-zero field point
of the complete fixed branch-P 303-variable fixture, continue from the two
reviewed conclusions

```text
T=A V,
F4-V/16-Z^2/64=A W,
A=X^4-1.
```

Then the *same* full `D8` equation has a second consequence which was absent
from the earlier leading-pole statement:

```text
D4=...=D8=0  =>  c6=0.                         (T3)
```

With that mode killed, the next row gives

```text
D4=...=D9=0  =>  A | W.                        (T4)
```

The exact raw congruences fixing the signs are

```text
D8_raw = -(9/4)c6 A^2 A'                       (mod A^3),
D9_raw = +(21/4)A A' W^2                       (mod A^2).
```

The qualification “with that mode killed” is load-bearing.  Before `T3`,
the `c6` contribution to the weight-nine characteristic coefficient has an
order-three pole and dominates the proposed `W^2/A^2` obstruction.  Thus a
direct `D9` proof which silently omits `c6` is invalid even though the repaired
two-row argument succeeds.

These are field-point statements only.  There is no endpoint exclusion,
raw-ideal unit, cutoff-two classification, unrestricted branch-P result,
Keller-pair result, or JC2 conclusion here.

## 1. Custody and method

The authoritative literal source is

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
```

It has 303 raw variables and 513 generators in rows `D4,...,D22`.  The
checker uses two independent representations:

1. a sparse Laurent ring over `Q`, keyed by an integer power of `A` and a
   commutative monomial in generic polynomial symbols; and
2. ordinary exact univariate `Q[X]` arithmetic, used to evaluate literal
   serialized raw generators and independently reconstructed determinant
   rows on source-level mutations.

Every coefficient is a `fractions.Fraction`.  There is no CAS, floating
point, interpolation, evaluation at roots, cutoff specialization, or AWS
computation.

The exact contextual bytes consulted were the characteristic firewall and
the two hostile audits with hashes recorded in `RESULT.json`.  The raw JSON,
not those explanatory reports, is the proof source.

## 2. Complete causal mode schedule

The safe characteristic continuation is retained as

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

At weights eight and nine, causality leaves exactly the already-born modes
`c4,c6,c8`.  The later modes have coefficient index `n-m<0`, hence zero
support at these two rows.  In particular, `c14,c16,c18,c20` have not been
deleted: they remain serialized as mandatory forced rational modes at every
row at or after their birth.  “No support yet” is not the forbidden
five-mode truncation.

For every fractional power `y=F^alpha`, the checker uses the pinned safe
recurrence

```text
n A^4 y_n
  = sum_(1<=i<=n) (((alpha+1)i-n) F_i y_(n-i)).       (2.1)
```

## 3. Post-`D7` and post-leading-`D8` substitution

After the reviewed field-radical steps, the beginning of `F` is exactly

```text
F0=A^4,
F1=A^2,
F2=1/4+A^2 Z/4,
F3=Z/8+A^2 V/8,
F4=V/16+Z^2/64+A W.
```

Applying (2.1) independently gives the following three coefficients of the
base solution.  The first two are polynomial:

```text
(F^(3/2))_7
 = 3F5 Z/16 + 3F6/4 + 3V^2/1024
   + 3A V W/32 + 3A^2 F7/2,

(F^(3/2))_8
 = 3F5 V/32 + 3F6 Z/16 + 3F7/4
   - 3V^2 Z/4096 + 3W^2/8 + 3A^2 F8/2.
```

The next coefficient has polar part

```text
polar((F^(3/2))_9)
 = -3W^2/(16A^2)
   + (3F5 W/4-3V W Z/256)/A.                       (3.1)
```

The complete term list, including every holomorphic summand, is serialized
in `RESULT.json` and recomputed by the checker.

## 4. Theorem T3: `D8` kills `c6`

At weight eight the complete continuation is

```text
g8=(F^(3/2))_8+c4 F4+c6(F^(3/4))_2+c8(F^(1/2))_0.
```

The two required mode coefficients are exactly

```text
(F^(3/4))_2 = 3/(32A)+3A Z/16,
(F^(1/2))_0 = A^2.
```

Thus the base coefficient, the `c4` term, and the `c8` term are polynomial,
and

```text
polar(g8)=3c6/(32A).                               (4.1)
```

No other mode can cancel (4.1): `c4,c6,c8` are the complete born-mode list,
and the only polar term among them is the displayed `c6` term.  Since a raw
solution has polynomial `G8`, (4.1) forces the scalar characteristic
constant `c6` to vanish.

For an independent raw-row sign check, write

```text
L_n(R)=4(12-n)A^3A'R-8A^4R'.
```

The polynomial same-row contribution lies in `A^3`, while

```text
-L_8(3c6/(32A))=-(9/4)c6 A^2A'  (mod A^3),
```

which is the first stated raw congruence.

### Literal live mutation for T3

Set all 303 raw variables to zero except the polynomial coefficients

```text
G6=A^3,       G7=3A/4.
```

In literal slots these are

```text
g_0_6=-1, g_4_18=3, g_8_30=-3, g_12_42=1,
g_0_5=-3/4, g_4_17=3/4.
```

The serialized JSON and an independent recurrence replay agree in every row
`D4,...,D21`.  Rows `D4,...,D7` vanish and

```text
D8=-9X^3+18X^7-9X^11=-(9/4)A^2A'.
```

Live rescalings `c6=-1,2` reverse and double this residual exactly.  They are
serialized, not inferred from interpolation.

## 5. Theorem T4: the `D9` square defect

Before using `T3`, the full born-mode coefficient is

```text
g9=(F^(3/2))_9+c4 F5+c6(F^(3/4))_3+c8(F^(1/2))_1,
```

where

```text
(F^(3/4))_3=-1/(128A^3)+3Z/(64A)+3A V/32,
(F^(1/2))_1=1/2.
```

This exhibits the order-three `-c6/(128A^3)` firewall explicitly.  After
`T3` gives `c6=0`, `c4F5` and `c8/2` are polynomial and (3.1) is the complete
negative part of `g9`.  Its order-two coefficient cannot be canceled by the
order-one term.  Polynomial raw `G9` therefore gives

```text
A | W^2.                                             (5.1)
```

Equivalently, applying the same-row operator to
`N/A^2`, `N=-3W^2/16`, gives

```text
L_9(N/A^2)=28AA'N-8A^2N',
D9_raw=-L_9(g9)=+(21/4)AA'W^2  (mod A^2).            (5.2)
```

Since `gcd(A,A')=1`, (5.2) again gives (5.1).  The polynomial
`A=X^4-1` is squarefree in characteristic zero, so at a field point
`A|W^2` implies `A|W`.  This last radical step is not valid as a
scheme-theoretic assertion over arbitrary nonreduced coefficient rings.

### Literal live mutations for T4

For `W=1`, set all raw variables to zero except

```text
F4=A,
G4=3A^3/2,
G5=3A/4,
G8=3/8.
```

The nonzero literal slots are

```text
f_0_4=-1, f_4_16=1,
g_0_8=-3/2, g_4_20=9/2, g_8_32=-9/2, g_12_44=3/2,
g_0_7=-3/4, g_4_19=3/4,
g_0_4=3/8.
```

Again the pinned JSON and independent recurrence agree in every row through
`D21`.  Rows `D4,...,D8` vanish and

```text
D9=-21X^3+21X^7=(21/4)AA'.
```

The checker also runs the live mutations `W=-1` and `W=2`, rebuilding every
raw slot each time.  They give respectively the same residual and four times
the residual:

```text
D9(-W)=D9(W),
D9(2W)=4D9(W).
```

This independently fixes both the sign and the square power in (5.2).

## 6. Replay and scope

From the repository root:

```text
python3 -B cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/verify_uniform_d9.py --check
```

The replay hash-checks the authoritative raw JSON, recomputes every Laurent
identity, checks both operator congruences, evaluates the literal mutations,
and compares the raw JSON to the independent determinant recurrence in all
rows `D4,...,D21` for every mutation.

Promotion scope after independent review:

- the separately stated `D8 => c6=0` mode-kill theorem;
- the repaired `D9 => A|W` field-point divisibility theorem;
- the two raw signs and all mutation scaling laws;
- the warning that `D9` cannot be consumed before the full `D8` mode kill.

Not promoted by this packet: scheme divisibility, endpoint emptiness, any
later defect, or any result beyond the fixed branch-P fixture.
