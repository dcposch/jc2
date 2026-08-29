# Hostile audit: uniform `A`-adic square defects at `D7` and `D8`

Date: 2026-08-28  
Reviewer: Sol Ultra, independent exact lane  
Charged report:
`xmodel/ggv-upper-endpoint-uniform-tail-local-obstruction-grok46-20260828.md`  
Charged report SHA-256:
`f6950b257aa146df18cae4b3663d2087a067f58a4a91da72791adaa73deb6af3`

## Verdict

**REPAIR / PROMOTE THEOREMS 1--2 AFTER TWO LOCAL CORRECTIONS.**

The two load-bearing conclusions of the charged report are correct for
characteristic-zero **field points** of the pinned 303-variable fixed
branch-P fixture:

```text
D7=0  =>  A | T,

T=A V and D8=0
      =>  A | (F4 - V/16 - Z^2/64),

A=X^4-1.
```

The polar-numerator identities supporting those implications are also
correct:

```text
A^2 (F^(3/2))_7
    = -3 T^2/1024                  (mod A),

A^2 (F^(3/2))_8
    = 3(F4-V/16-Z^2/64)^2/8       (mod A),
```

after `T=A V` in the second line.  Restoring the seven `z_*` coordinates
does not alter the first identity and changes the second defect by exactly
`Z^2/64`.  The characteristic modes available through weight eight cannot
cancel either order-two pole.

Two printed details must be repaired:

1. The sign in displayed equation (1.2) is wrong.  With the report's
   conventions,

   ```text
   L7((F^(3/2))_7)
       = -27 A A' T^2/256          (mod A^2),

   D7_raw
       = +27 A A' T^2/256          (mod A^2),
   ```

   not `+27 A A'T^2/256` for `L7`.  The report's immediately following
   example `(27/64)(X^3-X^7)` actually has the corrected negative sign and
   therefore internally contradicts the displayed congruence.  The sign is
   a unit and does not affect `A|T`.

2. After `T=A V`, the exact weight-two coefficient of the `k6` mode is

   ```text
   (F^(3/4))_2 = 3/(32 A) + (3/16) A Z.
   ```

   Its `A`-adic valuation is therefore **exactly `-1` everywhere**, not
   merely when `Z(rho)` or the weight-eight defect is nonzero.  This
   strengthens, rather than weakens, the noncancellation argument.

There is no field-point, cutoff-4/3/2 emptiness, raw-ideal unit, unrestricted
branch-P, Keller-pair, or JC2 conclusion in this audit.

## 1. Custody and independent method

The live charged bytes and authoritative raw source recompute to

```text
f6950b257aa146df18cae4b3663d2087a067f58a4a91da72791adaa73deb6af3
  xmodel/ggv-upper-endpoint-uniform-tail-local-obstruction-grok46-20260828.md

ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
```

The latter identifies itself as the literal D5G recurrence system with
303 variables and 513 coefficient generators.  It has all `F4,...,F14`
and `G4,...,G21` windows, no `G22`, no `D23`, and the fixed data

```text
F0=A^4,  G0=A^6,  F1=A^2,  c2=0,
F2=(1+A^2 Z)/4,  F3=(Z+A T)/8.
```

I did not run either the Grok calculation or the cutoff-3/4 analyzers as a
proof source.  I implemented a fresh sparse Laurent ring over `Q`: a term is
an exact rational coefficient, an integer power of the formal symbol `A`,
and a commutative monomial in generic residues.  In that ring I used only

```text
S0=A^2,
Sn=(Fn-sum_(1<=i<n) Si*S_(n-i))/(2A^2),
(S^3)_n=sum_(i+j+k=n) Si*Sj*Sk,
```

and, independently for the fractional mode,

```text
n A^4 y_n
  = sum_(1<=i<=n) (((alpha+1)i-n) F_i y_(n-i)).
```

The implementation used `fractions.Fraction`, no floating point, no CAS,
and no imported campaign arithmetic.  A second checker evaluated two
explicit assignments directly in the serialized 513-generator raw JSON.

The frozen cutoff-4 packet, whose result and analysis hashes are
`f5b3b6ec...` and `3a1dc7ef...`, independently finds the specialized first
step `D8: F4^2 mod A`; I use that only as a consistency check, not as an
input here.

## 2. Fresh derivation of the `D7` defect

The oriented square root begins

```text
S0=A^2,
S1=1/2,
S2=Z/8,
S3=T/(16A).
```

Running the displayed recurrence through weight seven with generic residues
of `Z,T,F4,F5,F6,F7` gives

```text
val_A((S^3)_7) = -2,
[A^-2](S^3)_7 = -3 T^2/1024.
```

Every monomial involving `Z` or `F4,...,F7` cancels from this leading
coefficient.  One transparent way to locate the coefficient is to regard
`A T t^3/8` as the nonsquare defect in `F`.  The quadratic Taylor term of
`F^(3/2)` is `(3/8)F^(-1/2)(A T/8)^2 t^6`; the weight-one coefficient of
`F^(-1/2)` is `-1/(2A^4)`, giving

```text
(3/8)*(A^2 T^2/64)*(-1/(2A^4))
  = -3 T^2/(1024 A^2)
```

at weight seven.  All possible linear-defect contributions have valuation
at least `-1`, and cubic-defect terms start after weight seven.  The direct
recurrence verifies that this accounting is exact.

The characteristic identity

```text
E(F,t^m F^((12-m)/8))=0
```

shows that, after the already reviewed rows through `D6`, the complete
weight-seven coefficient is

```text
g7=(F^(3/2))_7 + k4 F3 + k6 (F^(3/4))_1.
```

Here

```text
(F^(3/4))_1=3A/4,
```

so both mode terms are polynomial.  There is no odd rational kernel at
weight seven: `ker L7` would require `A^(5/2)`, which is not in `K(X)`.
Thus no characteristic mode cancels the order-two pole.  The standard
weighted-degree count puts every coefficient which is polynomial inside the
literal raw `G7` window `0..17`; the raw upper cutoff creates no converse
gap.

For the exact sign, with

```text
L7(R)=20A^3 A'R-8A^4R',
```

one has

```text
L7(N/A^2)=36 A A' N-8A^2 N',
```

and hence, modulo `A^2`,

```text
L7((F^(3/2))_7)
  = 36 A A'*(-3T^2/1024)
  = -27 A A'T^2/256.
```

The literal raw `G7` block is divisible by `A^3`, while the literal same-row
`F7` block is divisible by `A^5`.  Since the characteristic continuation
has zero row, the raw row satisfies

```text
D7_raw = -L7(g7) = +27 A A'T^2/256   (mod A^2).
```

At each root `rho` of `A`, `A'(rho)` is a unit.  Thus `D7=0` puts `T^2` in
the zero class of `K[X]/(A)`.  This quotient is reduced in characteristic
zero, so a field point has `T=0 mod A`, equivalently `A|T`.  No analogous
scheme-theoretic conclusion `A|T` is licensed.

## 3. Literal raw earliest-row counterexample

The proposed counterexample to any earlier forcing survives a direct replay
against the authoritative JSON.  Set

```text
Z=0, T=1, F_n=0 for n>=4,
G4=3A/32, G5=0, G6=3/512,
G_n=0 for n>=7.
```

In literal raw coordinates the only nonzero surviving variables are

```text
tt_0=1,
g_0_8=-3/32, g_4_20=3/32,
g_0_6=3/512.
```

All serialized generators in rows `D4,D5,D6` evaluate to zero.  Row `D7`
evaluates to

```text
[X^3]D7=-27/64,  [X^7]D7=+27/64,

D7=(27/64)(X^7-X^3)=(27/256)A A'.
```

This simultaneously confirms that `D6` does not force `A|T`, that `D7` is
the first forcing row, and that the corrected sign above is the raw sign.
The Laurent valuations of `(F^(3/2))_n`, `n=0,...,7`, are exactly

```text
6, 4, 2, 0, 1, infinity, 0, -2,
```

matching the charged report.

## 4. Fresh derivation of the `D8` defect

After the field-radical conclusion `T=A V`, the first square-root
coefficients are polynomial:

```text
S1=1/2,  S2=Z/8,  S3=V/16.
```

Put

```text
Delta4=F4-V/16-Z^2/64.
```

Then

```text
S4=Delta4/(2A^2).
```

Fresh recurrence through weight eight with generic residues of
`V,Z,F4,...,F8` gives

```text
val_A((S^3)_7)>=0,
val_A((S^3)_8)=-2,
[A^-2](S^3)_8=(3/8)Delta4^2.
```

Expanded, the six independently obtained monomial coefficients are

```text
F4^2             3/8
F4*V            -3/64
F4*Z^2          -3/256
V^2              3/2048
V*Z^2            3/4096
Z^4              3/32768.
```

They are precisely the expansion of `(3/8)(F4-V/16-Z^2/64)^2`.  No
`F5,F6,F7,F8` residue occurs.  Equivalently, once the square has been
completed through weight three, the quadratic Taylor term in the new
weight-four defect is

```text
(3/8) F^(-1/2)_0 Delta4^2 t^8
  = 3 Delta4^2/(8A^2) t^8.
```

The complete mode census at weight eight is

```text
k4 F4,
k6 (F^(3/4))_2,
k8 (F^(1/2))_0.
```

Fresh application of the fractional-power recurrence gives the exact
middle coefficient

```text
(F^(3/4))_2=3/(32A)+(3/16)AZ.
```

Thus the three modes have pole orders `0,1,0`, respectively.  No choice of
`k4,k6,k8` can cancel the order-two `Delta4^2` pole.  A polynomial raw `G8`
therefore forces `Delta4^2=0 mod A`; reducedness of `K[X]/(A)` yields
`A|Delta4` on field points.

This also explains the cutoff dictionary without importing any later
cutoff result:

```text
cutoff 4: Z=T=0  =>  A|F4;
cutoff 3: Z=0    =>  A|(F4-V/16);
cutoff 2:          A|(F4-V/16-Z^2/64).
```

## 5. Literal raw `D8` mutations and mode attack

For a source-level test set

```text
Z=T=0, F4=1, F_n=0 for n>=5,
G4=(3/2)A^2, G5=3/4, G6=G7=G8=0.
```

Equivalently, the nonzero raw slots are

```text
f_0_4=1,
g_0_8=3/2, g_4_20=-3, g_8_32=3/2,
g_0_7=3/4.
```

Every literal raw generator through `D7` vanishes, while

```text
[X^3]D8=48,  [X^7]D8=-48,
D8=-12 A A'.
```

This agrees with `(F^(3/2))_8=3/(8A^2)` and
`D8_raw=-L8((F^(3/2))_8)`.

To attack the claimed noncancellation, add `k6=1` through its available
polynomial coefficients

```text
delta G6=A^3,
delta G7=3A/4.
```

All raw rows through `D7` still vanish.  The literal `D8` residual becomes

```text
39 X^3-30 X^7-9 X^11
  = -12 A A' - 9 X^3 A^2.
```

The `A^1` obstruction is unchanged; the `k6` mutation changes only an
`A^2` term, exactly as the order-one pole calculation predicts.  This is a
source-level negative control against hidden cancellation by the only
nonpolynomial mode.

Further exact mutations behaved as required:

| mutation | exact outcome |
|---|---|
| replace `-3/1024` by `-3/512` | fails already at `T=1` |
| restore arbitrary `Z mod A` in the `D7` recurrence | the `A^-2` coefficient remains `-3T^2/1024` |
| omit `Z^2/64` from `Delta4` | leaves nonzero `F4*Z^2`, `V*Z^2`, and `Z^4` residuals |
| attempt cancellation with `k6` | affects only order `A^-1` in `g8`, hence only order `A^2` in the raw row |
| infer `A|T` or `A|Delta4` over dual numbers | invalid; only their squares vanish in the residue-ring ideal |

## 6. Separate qualification to Theorem 3

The formula

```text
g22=(X^5/5-X+c)/(8A^5),  L22(g22)=-1
```

is correct, as is the conclusion that a polynomial `g22` cannot produce
the endpoint target.  The phrase “polar order exactly five along `A=0`”
should not be read as order five at **each** of the four geometric roots.
For example, with `c=4/5`,

```text
X^5/5-X+4/5
  = (X-1)^2 (X^3+2X^2+3X+4)/5,
```

so the solution has pole order three at `X=1` and order five at the other
roots.  Its global full-`A` denominator exponent is still five because the
numerator is not divisible by all of `A`.  This qualification does not
affect Theorems 1--2 or the polynomial-`g22` contradiction.

## 7. Promotion scope and next exact step

Promotable after correcting the two displayed details:

- the universal polar identities at `D7` and `D8`;
- their characteristic-mode noncancellation;
- the two field-radical divisibilities on the complete fixed cutoff-2
  fixture;
- the exact specialization to cutoffs 3 and 4;
- the fact that `D7`, not any earlier row, first kills `T mod A`.

Not promoted:

- a scheme-theoretic divisibility rather than a field-radical one;
- an emptiness result for cutoff 2 or 3;
- any use of the later cutoff-4 or cutoff-5 exclusion as an input;
- a statement at every local root that the endpoint pole order is five;
- any unrestricted branch-P, other-face, Keller, or JC2 conclusion.

The best successor remains a single uniform recurrence compiler for the
next defects, but it should serialize both objects at every row:

1. the leading Laurent numerator identity, and
2. its literal raw-row image modulo `A^3`, including all characteristic
   modes already born.

That paired certificate would prevent the sign slip found here and would
turn the proposed `D9` and later square steps into immediately reviewable
raw implications rather than characteristic-only heuristics.
