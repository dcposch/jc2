# Hostile review: corrected uniform full-mode cascade `D14`--`D15`

Reviewer: Grok 4.6, independent hostile lane  
Date: 2026-08-28  
Charged report:

```text
xmodel/ggv-upper-endpoint-uniform-d14-d15-fullmodes-sol-ultra-20260828.md
```

Frozen packet:

```text
cases/ggv_8_28_upper_endpoint_uniform_d14_d15_fullmodes_20260828/
```

Independent checker:

```text
xmodel/ggv-upper-endpoint-uniform-d14-d15-fullmodes-corrected-r1-hostile-review-grok46-check.py
```

Machine-readable result:

```text
xmodel/ggv-upper-endpoint-uniform-d14-d15-fullmodes-corrected-r1-hostile-review-grok46-RESULT.json
```

Authoritative raw source:

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
```

## Verdict

| Charge | Verdict |
|--:|---|
| **D14 square divisibility** | **PASS** (conditional on the D8--D13 prefix) |
| **D14 `c14` kill** | **PASS** (conditional on the D8--D13 prefix and on the D14 square) |
| **D15 `c14` cancellation** | **PASS** |
| **D15 divisibility / `c8` survival** | **PASS** (conditional on the D14 conclusions) |
| **C13--C15** | **PASS** |
| **Overall** | **PASS** |

Nothing charged is REFUTED or sent back for REPAIR.  A superseded packet
falsely claimed that D15 itself killed `c14`.  That claim is **not**
repeated here, and it is independently false: the complete characteristic
`c14` mode is homogeneous at D15.  The only proposed `c14` kill that
survives is D14 polynomiality after the D14 square divisibility.

The D8--D13 prefix is a live hypothesis of this review, not a theorem
proved here.  Separate hostile reviews of that prefix already exist and
both returned PASS.  If that prefix fails, T9--T12 as stated fail with
it, because `(F^{3/2})_6` would not be `T/2` and D14 would not be the
printed square law.  Conditional on

```text
F4 = V/16 + Z^2/64 + A^2 R,
F5 = R/2 + Z V / 64 + A^2 Q,
F6 = Q/2 + R Z / 8 + V^2 / 256 + A^2 T,
c6 = 0,
c10 = 0,
```

the charged D14/D15 field-point statements hold on characteristic-zero
points of the complete fixed 303-variable / 513-generator branch-P
fixture.

No scheme divisibility, endpoint emptiness, unrestricted branch-P,
Keller-pair, or JC2 conclusion is licensed.

| # | Required check | Verdict |
|--:|---|---|
| 1 | Charged hashes; independent reconstruction of the Laurent recurrence and of raw D13--D15 | **CONFIRMED** |
| 2 | Complete nine-mode causality; `c14` first appears as `c14/A`; D14 square then D14 polynomiality | **CONFIRMED** |
| 3 | Both D15 `c14` contributions before imposing `c14=0`; exact cancellation; D15 does not independently constrain `c14` | **CONFIRMED** |
| 4 | After the D14 `c14=0` conclusion: `Delta8`, polar `g15`, `A\|U`, `c8` survival, `F7` completion | **CONFIRMED** |
| 5 | Literal G14 kernel 26 by 10, rank 10, nullity 0; `c8=1` survival point; all 513 generators; mutations; signs/powers; characteristic zero / squarefree uses | **CONFIRMED** |
| 6 | Independent C13, C14, C15 through `H0`; live necessary; no gauge normalized | **CONFIRMED** |
| 7 | Scope: char-0 field points of the complete fixed 303-variable fixture only | **CONFIRMED** |

## Promotable statements

Work over a characteristic-zero field, on a point of the complete fixed
branch-P fixture with `A = X^4-1`.  Continue from the D8--D13
field-radical prefix displayed above.  The complete characteristic
continuation is the nine-mode series of §3.

**T9 (D14 square).**  `D4 = ... = D14 = 0` forces `A | Delta7` at a field
point, where

```text
Delta7 = F7 - T/2 - Q Z / 8 - R V / 16.
```

Equivalently,

```text
polar(g14) = 3 Delta7^2 / (8 A^2) + c14 / A,
D14_raw    = -3 A A' Delta7^2     (mod A^2).
```

The order-two square cannot be cancelled by the order-one forced mode
`c14/A`.  The cross terms `T/2`, `Q Z/8`, and `R V/16` are load-bearing.
`T/2` is the honest promotion of `(F^{1/2})_6` after the D13 conclusion
`S = A T`; it is not present in the D13 polar, where `S` is still order
one in `A`.

**T10 (D14 `c14` kill).**  After T9 write `Delta7 = A U`.  Then the sole
remaining pole of `g14` is `c14/A`.  The same-row operator annihilates
that rational mode,

```text
L_14(c14 / A) = 0,
```

so D14 does not see `c14` as a differential obstruction.  The raw `G14`
window stores degrees `1..10` and cannot store `1/A`.  The literal same-row
matrix of that window against the 26 D14 generators has shape 26 by 10,
rank 10, and nullity 0: no polynomial raw kernel realizes the rational
mode.  Polynomiality of `G14` therefore forces the scalar `c14 = 0`.

**T11 (D15 `c14` cancellation).**  If `c14` is provisionally retained,
the continuation gives `g15` the further polar `-c14/(4 A^3)`.  The two
D5G pairings that can see this mode at weight 15 are

```text
same-row  (F0, G15):  L_15(-c14/(4 A^3)) = -3 c14 A',
mixed     (F1, G14):  (12-14) F1' (c14/A) + (1-8) F1 (c14/A)' = +3 c14 A'.
```

Their sum is identically zero.  D15 does **not** independently constrain
`c14`.  Treating the same-row image alone as a D15 kill is the superseded
error; it is a real calculation of one pairing and a false conclusion
about the complete mode.

**T12 (D15 square and `c8` survival).**  After T10,

```text
Delta8 = F8 - T Z / 8 - Q V / 16 - R^2 / 4,
polar(g15) = -3 U^2 / (16 A^2) + U (3 Delta8 / 4 + c8 / 2) / A,
D15_raw    = +(3/4) A A' U^2     (mod A^2).
```

Thus `A | U` at a field point.  The order-one terms, including
`c8 U / (2 A)`, land in `(A^2)` under `L_15` and become polynomial after
`U = A Y`.  D15 does not kill `c8`.  Combined:

```text
F7 = T/2 + Q Z / 8 + R V / 16 + A^2 Y,
c14 = 0.
```

A literal polynomial continuation with `c8 = 1` satisfies `D4` through
`D15` against all 513 source generators.

**T13 (C13, C14, C15).**  Raw `G13`, `G14`, and `G15` all have lower
degree one.  After the combined completion their constant terms are the
live necessary equations

```text
H0  = c8/2 + 3 F8(0)/4,

C13 = q H0 - 3 q^2 v / 128 - 3 q r^2 / 16 + 3 t^2 / 16 + 3 t y / 4 = 0,
C14 = t H0 - 3 q^2 r / 16 - 3 q t v / 64 - 3 r^2 t / 16
      - 3 t^2 z / 64 + 3 y^2 / 8 = 0,
C15 = y H0 - q^3 / 16 - 3 q r t / 8 - 3 q v y / 64 - 3 r^2 y / 16
      - 3 t^2 v / 128 - 3 t y z / 32 - 3 y^2 / 16 = 0,
```

written in `X=0` jets.  The combination `H0` is forced by the exact
additive gauge `F8(0) -> F8(0)+lambda`, `c8 -> c8-3 lambda/2`.  No
gauge, endpoint carrier, or unit is normalized.  These are scalar
compatibilities, not eliminated branch claims.

Not promoted: scheme-theoretic divisibility, emptiness of any cutoff, any
row after `D15`, unrestricted branch-P, Keller pairs, JC2, a D15 kill of
`c14`, a D15 kill of `c8`, or the statement that a non-constant
`X`-polynomial multiple of `A` can play the role of the scalar `c14`.

## 1. Custody and method

Live SHA-256 values, recomputed on disk:

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
830639eca8bf76bba512abc8528f763925a11092b661b1531d3f66b01c1c77fc
  xmodel/ggv-upper-endpoint-uniform-d14-d15-fullmodes-sol-ultra-20260828.md
53f2a7a276be4a0aa7f77cc031e270d573fc78b5db64cdb76a0cf6c502e52517
  cases/ggv_8_28_upper_endpoint_uniform_d14_d15_fullmodes_20260828/verify_uniform_d14_d15.py
7546618aa5a40ed983014159c1d39337396607562912570c97cfe2ee779394ea
  cases/ggv_8_28_upper_endpoint_uniform_d14_d15_fullmodes_20260828/RESULT.json
```

These match the review prompt, `SOURCE.sha256`, and `EVIDENCE.sha256`.
The D12 and D10 producer/result pins recorded by the charged packet also
match live bytes

```text
e5e2543ca50fc48623ccccf34f548f6171e79b31e6f80c8cfe6f5ca2b6798879
  cases/ggv_8_28_upper_endpoint_uniform_d12_d13_fullmodes_20260828/verify_uniform_d12_d13.py
06ca0152a7d05dd7b4549e74138b482fc572a62acae718751e7230577c5f28c8
  cases/ggv_8_28_upper_endpoint_uniform_d12_d13_fullmodes_20260828/RESULT.json
8ebe5f4f099e6cf15b0a4703dfb348aa6cc72df8fdbc60b1d095925fa3746d21
  cases/ggv_8_28_upper_endpoint_uniform_d10_fullmodes_audit_20260828/verify_uniform_d10.py
8ff338bdd47b7a53ba1515a7889823620120f92d718a03349fb9e3fd27014236
  cases/ggv_8_28_upper_endpoint_uniform_d10_fullmodes_audit_20260828/RESULT.json
f4e40d3324a9dc9058b6ec80a01458468b3a90d0d3b4794841e76450c42e8dbc
  cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/verify_uniform_d9.py
9ca90959f284052bf669911c15e675892c1749b0bfed3cb4fd6462156e61b059
  cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/RESULT.json
```

The independent checker does not import the D14/D15 producer.  A separate
standard-library checker, using only `fractions.Fraction`, did the
following.

1. Rebuilt `F0..F14`, `G0..G21` from the pinned head
   `F0=A^4`, `F1=A^2`, `F2=(1+A^2 Z)/4`, `F3=(Z+A T)/8`, `G0=A^6` and the
   raw windows, then expanded
   `D_n = sum_{i+j=n} ((12-j) F_i' G_j + (i-8) F_i G_j')`
   as sparse polynomials in the 303 coefficient variables.  In `D13`,
   `D14`, and `D15`, every `X`-degree, every monomial, and every sign
   matches the frozen generator list (78 coefficients, 6874 terms).
2. Ran the fractional recurrence
   `n A^4 y_n = sum_{1<=i<=n} (((alpha+1)i-n) F_i y_{n-i})`
   and, independently, the oriented square-root cube `S^3` with
   `S_0=A^2`.  They agree at weights `0..15` on the post-D13 prefix.
3. Applied the same-row operator
   `L_n(R) = 4(12-n) A^3 A' R - 8 A^4 R'`
   and the general D5G pairing
   `(12-j) F_i' G_j + (i-8) F_i G_j'`
   to polar parts, without importing the producer Laurent ring.  Raw
   square rows satisfy `D_raw = -L_n(polar)` on the omitted polar
   summand.  The `c14` D15 calculation uses the pairings themselves, not
   that sign convention, because both polars are omitted together.
4. Evaluated producer mutations and additional hostile mutations by a
   three-way comparison: independent D5G recurrence, serialized JSON
   generators (including the affine `D22[0] -= 1` fold), and the claimed
   closed forms.

No CAS, floating point, interpolation, AWS, or `jc2-lean` was used.  No
canonical top-level file and no frozen packet file was edited.  The
independent checker recorded 334 checks and 0 failures.

## 2. Independent reconstruction of raw `D13`--`D15`

The frozen JSON identifies itself as the literal D5G system on `Q` with
303 variables and 513 generators in rows `D4..D22`.  Documentary
`F1,F2,F3` and `G1,G2,G3` window slots exist in the window census but are
not among the 303 variables.  There is no `G22` and no `F15`.  The field
is `Q`.  `A=X^4-1`, `H=A^2`, `F1=H`, `c2=0`.

Window bounds that are load-bearing for “raw `G` is polynomial”:

- `G13` stores degrees `1..11` and omits the constant.
- `G14` stores degrees `1..10` and cannot store `1/A` or a constant.
- `G15` stores degrees `1..9` and cannot store `-1/(4 A^3)` or a constant.
- `F7` and `F8` both store constants, so `T/2` and the `H0` jet of `F8`
  are writable.
- `F9` and later omit degree 0, so those constants are fixture-zero and
  do not enter C13--C15.

Every generator of `D13..D15` was rebuilt from the D5G formula and
matched the frozen term lists, including row digests

```text
D13  aa794ef212b7f985a0e75db864b483f352504b9519f77de9247295bcbf9880ab
D14  35548a74a3af2126abfeda0519d1600bcf8cf5e24fc0f7dd4050bc2fe9f84caf
D15  4e7f3882153593594004cf817ce6f76e776cc10af09bc57e01a9202013d39b68
```

This is independent of the producer checker.

## 3. Nine-mode firewall

The safe continuation, retained and not truncated, is

```text
F^{3/2}
+ c4  t^4  F
+ c6  t^6  F^{3/4}
+ c8  t^8  F^{1/2}
+ c10 t^{10} F^{1/4}
+ c12 t^{12}
+ c14 t^{14} F^{-1/4}
+ c16 t^{16} F^{-1/2}
+ c18 t^{18} F^{-3/4}
+ c20 t^{20} F^{-1}.
```

Birth values `y_0 = A^{4 alpha}` were recomputed for all nine modes:

```text
c4: A^4,  c6: A^3,  c8: A^2,  c10: A,  c12: 1,
c14: A^{-1},  c16: A^{-2},  c18: A^{-3},  c20: A^{-4}.
```

Support at weight `n` requires `n-m >= 0`.  At `n=14` this first includes
`c14`, with birth pole `c14/A`.  At `n=15` the same mode continues as
`-c14/(4 A^3)`.  Empty causal support is not permission to delete
`c16,c18,c20`.  The producer `RESULT.json` serializes all nine modes,
with `c14,c16,c18,c20` marked `forced_rational` and
`retained_mandatory`.  Only the coefficient `c14` is derived to vanish;
the later forced modes remain unconstrained.

At D14 the polynomial born contributions are `c4 F10`, `c8 T/2`, and
`c12 (F^0)_2 = 0`.  At D15 they are `c4 F11`, `c8 (U/(2A) + holomorphic)`,
and `c12 (F^0)_3 = 0`.  The `c6` and `c10` coefficients are already zero
by the prefix.

## 4. Theorem T9: D14 square defect

After the D13 prefix, both the fractional recurrence and the square-root
cube give `(F^{1/2})_6 = T/2`, polynomial.  Completing the square through
weight seven produces the honest defect `Delta7` displayed in T9.  With
`c6=c10=0` the polar part of `g14` is exactly
`3 Delta7^2/(8 A^2) + c14/A`: no `A^{-3}` or lower.  The order-two piece
is supported on `Delta7^2` alone; the order-one piece is supported on
`c14` alone.  Those valuations cannot cancel.

Same-row calculus: `L_14(3 Delta7^2/(8 A^2))` contributes
`3 A A' Delta7^2` at order `A^1`, so the omitted-polar identity

```text
D14_raw = -L_14(polar_square) = -3 A A' Delta7^2     (mod A^2)
```

holds.  `L_14` of every polynomial lands in `(A^3)`, so polynomial `G14`
cannot kill the `A^1` class.  Adding a window element `G14[X^1]=1` to the
`Delta7=1` mutation leaves the square class outside `(A^2)`.

Closed form for `Delta7=1`:

```text
D14 = 12 X^3 - 12 X^7 = -3 A A'.
```

Scalings `Delta7 = -1, 2` repeat this and multiply it by 4, fixing both
the sign and the square power.  All 513 generators match the independent
recurrence, including D14 generators 318 and 322
(`c73aa941...`, `1edbb3e0...`).  Omitting `F7` from an exact square
continuation through `G13` produces a nonzero D14 while `D4..D13` remain
zero.

Field-radical last step: `gcd(A,A')=1` by the Euclidean algorithm over
`Q` (`A'=4 X^3`).  Thus `A | A' Delta7^2` implies `A | Delta7^2`.  On a
field, `Q[X]/(A)` is a product of fields because `A` is squarefree, and
`Delta7^2=0` there iff `Delta7=0` there.  Direct remainder checks for
several polynomials confirm `A | W^2` if and only if `A | W` in `Q[X]`.
The coefficients `3`, `8`, and `4` make characteristic zero essential.
Over a nonreduced coefficient ring the same calculation only puts
`Delta7` in the radical of `(A)`, which is not claimed.

Isolated omission of `T/2`, of `Q Z/8`, or of `R V/16` changes the polar
part of `g14`.  Those summands are not optional shorthand.

## 5. Theorem T10: D14 polynomiality kills `c14`

After `Delta7 = A U`, substitution into `g14` leaves polar part `c14/A`
and holomorphic part including `3 U^2/8`.  The holomorphic part is
writable in the `G14` window.  The pole is not.

Two independent facts:

1. `L_14(c14/A) = 0` as a Laurent identity.  Equivalently the D5G pairing
   `(F0, G14)` vanishes on this mode.  No other D14 pairing can see
   `c14`, which is not born at weight 13.  D14 therefore supplies no
   differential equation for the scalar `c14`.
2. The 10 polynomial slots of `G14` inject into the 26 D14 generators:
   rank 10, nullity 0, over `Q`.  A constant cannot be stored
   (`G14` lower degree 1), and `A` does not divide a nonzero constant, so
   `c14/A` is not secretly a polynomial in the window.

The kill is therefore fixture polynomiality of `G14`, not a D14 raw
congruence.  Causal order is essential: before `A | Delta7` the order-two
square dominates, and one cannot commute the `c14` conclusion in front of
the square.

The scalar `c14` is a characteristic constant, not an `X`-polynomial.  A
non-constant polynomial multiple of `A` in the role of `c14` would be a
holomorphic `G14` element, already covered by the nullity-zero matrix.

## 6. Theorem T11: D15 does not independently constrain `c14`

This is the audit point that a superseded packet got wrong.

Retain `c14` after `Delta7 = A U`.  Then

```text
polar(g14) = c14 / A,
polar(g15) = -c14 / (4 A^3) - 3 U^2 / (16 A^2)
             + U (3 Delta8 / 4 + c8 / 2) / A.
```

The only D15 pairings that contain the born `c14` mode are `(F0, G15)`
and `(F1, G14)`, because `c14` lives in `G14` and `G15` only.

Independent evaluation of those pairings, using `F0=A^4` and `F1=A^2`:

```text
(12-15) F0' (-c14/(4 A^3)) + (0-8) F0 (-c14/(4 A^3))' = -3 c14 A',
(12-14) F1' (c14/A)       + (1-8) F1 (c14/A)'       = +3 c14 A'.
```

The first pairing agrees with `L_15`.  The second is not a same-row term
and cannot be recovered from `L_15` alone.  Their sum is the zero
Laurent series.  The `A^0` class of `D15` therefore does not see `c14`.

If both polars are omitted from the polynomial fixture, the omitted-polar
identity gives

```text
D_raw_c14 = - (same-row) - (mixed) = 0
```

as well.  Same-row alone would have produced the superseded image
`+3 c14 A'` after the `D_raw = -L_n` convention, or `-3 c14 A'` if one
quotes `L_15` without mixed.  Either leftover is an artefact of dropping
the predecessor.  The complete characteristic mode is homogeneous at
D15.

The charged note, producer, and `RESULT.json` all state this
cancellation and retract the standalone D15 image.  Encoded same-row and
mixed pieces match the independent pairings, and `D15_c14_total` is
empty.

## 7. Theorem T12: D15 square, `A|U`, `c8` survives

After T10, the `c14` terms are gone and

```text
polar(g15) = -3 U^2 / (16 A^2) + U (3 Delta8 / 4 + c8 / 2) / A.
```

The order-two piece is supported on `U^2` alone.  `L_15` of every
order-one term lands in `(A^2)`, including the live `c8 U / (2 A)`.
Same-row calculus on the square gives

```text
D15_raw = -L_15(-3 U^2 / (16 A^2)) = +(3/4) A A' U^2     (mod A^2).
```

The coefficient `3/4` is nonzero in characteristic zero.  Squarefreeness
of `A` upgrades `A | U^2` to `A | U` on a field, as in T9.

Literal mutation with `U = X` (so `A` does not divide `U`):

```text
F7 = A X,   G7 = (3/2) A^3 X,   G8 = (3/4) A X,
G14 = (3/8) X^2,
D15 = (3/4) A A' X^2 - 3 A^2 X = -3 X + 3 X^5,
```

with `D4..D14=0`.  The extra `-3 A^2 X` is a derivative term, congruent
to zero modulo `A^2`.  Scalings `U = -X, 2X` multiply the residual by 4.
All 513 generators match, including D15 generators 342 and 346
(`6b7ebc3c...`, `7f4b92bd...`).  Isolated omission of `R^2/4` from
`Delta8` changes the polar part of `g15`.

After `U = A Y` the remaining polar of `g15` is empty, and
`c8 U / (2 A)` becomes the polynomial `c8 Y / 2`.  The charged survival
point

```text
F = (A^2 + t/2)^2 + A^2 X t^7,
G = F^{3/2} + t^8 F^{1/2}   through G15,
```

has `c8=1`, `Y=X`, `Delta8=0`, and `D4..D15=0` against all 513
generators.  D15 does not kill `c8`.  No unit is normalized.

## 8. Theorem T13: live lower-window equations

After the combined completion, `g13`, `g14`, and `g15` are holomorphic.
Their `X^0` jets, using `A(0)=-1` and dropping the fixture-zero constants
of `F9` and later, match the charged encodings of `G13_X0`, `G14_X0`,
and `G15_X0`.  Factoring the combination `H0 = c8/2 + 3 F8(0)/4`
recovers C13, C14, C15 exactly.

Each equation is nonzero as a polynomial (C13 has `3 t^2/16`, C14 has
`3 y^2/8`, C15 has `-q^3/16`).  Each has terms beyond the `H0` factor.
The additive gauge

```text
F8(0) -> F8(0) + lambda,    c8 -> c8 - 3 lambda / 2
```

leaves `H0` and all three jets invariant at `lambda = -1, 1, 2`.  The
same scalars, imposed as raw `F8` constants with default `G`, are an
exact kernel of `D4` through `D22` before the affine target fold.  That
is a raw gauge, not a normalisation: `H0` is retained as a coordinate,
and the `c8=1` survival point has `H0 = 1/2`.

C13, C14, and C15 remain live necessary equations.  They are not claimed
exhausted, and they are not used to kill `c8` or to set `F8(0)=0`.

## 9. Mutations, signs, and attempted falsifiers

Replay / replacement, all against the independent D5G recurrence and the
513 serialized generators:

- `Delta7 = -1, 1, 2` (square power 2, residual `-3 A A'` times the
  square);
- `U = -X, X, 2X` (square power 2, residual congruent to `(3/4) A A' U^2`
  modulo `A^2`);
- polynomial `G14[X^1]` against the D14 square (does not kill the `A^1`
  class);
- pure polynomial `G14[X^1]` with empty `F7` (nonzero D14, so not a
  kernel);
- `c8=1` survival through D15;
- `F8` constant gauge at three scalars;
- exact square continuation with `Y=X` (C13--C15 hold by vanishing
  jets);
- omission of `F7` from that exact square (D14 becomes the first residual).

No literal raw field point or local Laurent mutation was found that
falsifies T9--T13 inside the stated hypotheses.  In particular, no
mutation was found in which D15 independently constrains `c14`.

## 10. Scope

These are statements about characteristic-zero field points of one fixed
303-variable branch-P fixture, at rows `D14` and `D15`, after the
D8--D13 prefix.  They are not:

- scheme-theoretic divisibility over nonreduced coefficient rings;
- emptiness of the endpoint, of cutoff 4/3/2, or of any later row;
- an unrestricted branch-P theorem, a Keller-pair theorem, or JC2;
- a licence to drop `c16,c18,c20`, or to kill `c8` or the additive
  `F8`/`c8` gauge;
- a claim that `D15` may kill `c14`, or that `D14` may kill `c14` before
  `A | Delta7`;
- a claim that a non-constant `X`-polynomial may play the role of
  scalar `c14`.

The coefficients `3`, `3/4`, `8`, `16`, and `4` make characteristic zero
essential.  The D8--D13 prefix remains a live external hypothesis: if it
fails, T9--T12 as stated fail with it.

## Hashes

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
830639eca8bf76bba512abc8528f763925a11092b661b1531d3f66b01c1c77fc  xmodel/ggv-upper-endpoint-uniform-d14-d15-fullmodes-sol-ultra-20260828.md
53f2a7a276be4a0aa7f77cc031e270d573fc78b5db64cdb76a0cf6c502e52517  cases/ggv_8_28_upper_endpoint_uniform_d14_d15_fullmodes_20260828/verify_uniform_d14_d15.py
7546618aa5a40ed983014159c1d39337396607562912570c97cfe2ee779394ea  cases/ggv_8_28_upper_endpoint_uniform_d14_d15_fullmodes_20260828/RESULT.json
44af761192103401d91a5080a6e458e46a9cbddc0c37b23a05d55c91c9401a2d  xmodel/ggv-upper-endpoint-uniform-d14-d15-fullmodes-corrected-r1-hostile-review-grok46-check.py
813131e69431d36dcb64d66a9a901521fb5b0107ef36b4e5042f18c4a4c7950e  xmodel/ggv-upper-endpoint-uniform-d14-d15-fullmodes-corrected-r1-hostile-review-grok46-RESULT.json
```

The SHA-256 of this review file is the digest of the on-disk bytes of

```text
xmodel/ggv-upper-endpoint-uniform-d14-d15-fullmodes-corrected-r1-hostile-review-grok46-20260828.md
```

computed after the final write, recorded immediately below.

<!-- self-hash -->
aca262d8a67bba6a0f865c9430ec4c65290ac1e6dafd6383c883f8a9b7c89f72  report body above this delimiter
