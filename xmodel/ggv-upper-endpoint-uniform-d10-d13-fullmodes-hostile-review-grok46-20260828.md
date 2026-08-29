# Hostile review: uniform full-mode cascade `D10`--`D13`

Reviewer: Grok 4.6, independent hostile lane  
Date: 2026-08-28  
Charged reports:

```text
xmodel/ggv-upper-endpoint-uniform-d10-d11-fullmodes-independent-sol-ultra-20260828.md
xmodel/ggv-upper-endpoint-uniform-d12-d13-fullmodes-sol-ultra-20260828.md
```

Frozen packets:

```text
cases/ggv_8_28_upper_endpoint_uniform_d10_fullmodes_audit_20260828/
cases/ggv_8_28_upper_endpoint_uniform_d12_d13_fullmodes_20260828/
```

Independent checker:

```text
xmodel/ggv-upper-endpoint-uniform-d10-d13-fullmodes-hostile-review-grok46-20260828-check.py
```

Authoritative raw source:

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
```

## Verdict

| Charge | Verdict |
|--:|---|
| **D10** | **PASS** (conditional on the D8/D9 prefix) |
| **D11** | **PASS** (conditional on D8/D9 and on D10) |
| **D12** | **PASS** (conditional on D8--D11) |
| **D13** | **PASS** (conditional on D8--D12) |
| **Overall** | **PASS** |

Nothing charged is REFUTED or sent back for REPAIR.  The four field-point
theorems survive independent reconstruction of the raw `D4..D13`
generators, an independent Laurent / square-root calculation of the full
nine-mode continuation, operator-level sign checks, live source mutations
including isolated omission of `Z*V/64` and of every summand of `Delta6`,
and a search for cancelling polynomial or mixed-mode counterterms.

The D8/D9 prefix is a live hypothesis, not a theorem of this review.
It was independently reconstructed here (polar parts, operator images, and
the two producer prefix mutations) and matches the charged formulas
`c6=0` and `W=A R`.  A separate hostile review of that prefix already
exists; if that prefix fails, D10--D13 as stated fail with it, because
`(F^{3/4})_4` has an order-minus-five polar part and D10 is then not the
printed square law.  Conditional on

```text
T = A V,
F4 = V/16 + Z^2/64 + A^2 R,
c6 = 0,
```

the four charged rows hold on characteristic-zero field points of the
complete fixed 303-variable / 513-generator branch-P fixture.

No scheme divisibility, endpoint emptiness, unrestricted branch-P,
Keller-pair, or JC2 conclusion is licensed.

| # | Required check | Verdict |
|--:|---|---|
| 1 | Charged hashes; independent reconstruction of raw rows and Laurent recurrence | **CONFIRMED** |
| 2 | Complete nine-mode causality `c4,c6,c8,c10,c12,c14,c16,c18,c20`; replay of a literal gauge requiring nonzero `c16` | **CONFIRMED** |
| 3 | Honest cross terms and exact causal order D10--D13 | **CONFIRMED** |
| 4 | Each raw congruence, sign, power of `A`, squarefreeness / characteristic zero; search for missing order-one terms or allowed cancellations | **CONFIRMED** |
| 5 | Replay / replacement of live mutations, especially omission of `ZV/64` and the all-cross-term `Delta6` regression; attempt to falsify each row | **CONFIRMED** (no falsifier) |
| 6 | Scope: char-0 field points of the complete fixed 303-variable fixture only | **CONFIRMED** |

## Promotable statements

Work over a characteristic-zero field, on a point of the complete fixed
branch-P fixture with `A = X^4-1`.  Continue from the D8/D9 field-radical
prefix displayed above.  The complete characteristic continuation is the
nine-mode series of §3.

**T5 (D10).**  `D4 = ... = D10 = 0` forces `A | Delta5` at a field point,
where

```text
Delta5 = F5 - R/2 - Z V / 64.
```

Equivalently,

```text
polar(g10) = 3 Delta5^2 / (8 A^2),
D10_raw    = -9 A A' Delta5^2     (mod A^2).
```

There is no D10 mode kill: the born contributions `c4 F6`, `c8 Z/8`, and
`c10 A` are polynomial, and `c6` is already zero.  The cross term `Z V/64`
is load-bearing.  The shorthand `F5-R/2` is correct only after an explicit
shift of the `F5` coordinate, or on a specialization with `Z V = 0`.

**T6 (D11).**  After T5 write `Delta5 = A S`.  Then `D11=0` has two
causal steps that cannot be commuted.

1. First

   ```text
   polar(g11) = -3 S^2 / (16 A^2)
              + (c10/4 + (3/4) S Delta6) / A,
   Delta6     = F6 - R Z / 8 - V^2 / 256,
   D11_raw    = +(15/4) A A' S^2     (mod A^2),
   ```

   so `A | S` at a field point.  The order-one polar terms, including
   `c10/(4A)`, land in `(A^2)` under `L_11` and cannot cancel the square
   class.

2. After `S = A Q` every remaining base order-one term is polynomial.
   The only leftover pole is `c10/(4A)`, with

   ```text
   D11_raw = -3 c10 A^2 A'     (mod A^3)
   ```

   as an identity on that summand.  The constant `c10` is a scalar of the
   characteristic ODE, not an `X`-polynomial, and is forced to `0`.

Combined:

```text
F5 = R/2 + Z V / 64 + A^2 Q,
c10 = 0.
```

**T7 (D12).**  After T6,

```text
Delta6 = F6 - Q/2 - R Z / 8 - V^2 / 256.
```

The `Q/2` summand is the honest promotion of the D11 square-root coefficient
`S_5 = Q/2`; it is not present in the D11 polar (where `S` is still
order one in `A`).  Then

```text
polar(g12) = 3 Delta6^2 / (8 A^2),
D12_raw    = -6 A A' Delta6^2     (mod A^2).
```

The polar part is exactly this `A^{-2}` square: there is no leftover
`A^{-1}` class.  Squarefreeness of `A` gives `A | Delta6`.  There is no
D12 mode kill: `c4 F8`, `c8 R/2`, and `c12` are polynomial, while
`c6=c10=0` and `c14` is not born.

**T8 (D13).**  After T7 write `Delta6 = A S`.  Then

```text
polar(g13) = -3 S^2 / (16 A^2) + 3 S Delta7 / (4 A),
Delta7     = F7 - Q Z / 8 - R V / 16,
D13_raw    = +(9/4) A A' S^2     (mod A^2).
```

Hence `A | S`.  After `S = A T` the complete D13 continuation is
polynomial, so there is no second mode consequence.  Combined:

```text
F6 = Q/2 + R Z / 8 + V^2 / 256 + A^2 T.
```

The constant `c12` is a global additive `G12[X^0]` gauge and is not
killed.  The forced modes `c14,c16,c18,c20` remain mandatory continuation
coordinates.

Not promoted: scheme-theoretic divisibility, emptiness of any cutoff, any
row after `D13`, unrestricted branch-P, Keller pairs, JC2, or the statement
that a non-constant `X`-polynomial multiple of `A` can play the role of
the scalar `c10`.

## 1. Custody and method

Live SHA-256 values, recomputed on disk:

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
e24eb71b8df1a4c93fb4d156e2dd5084e53abccd332e793aaa584307e6d32a29
  xmodel/ggv-upper-endpoint-uniform-d10-d11-fullmodes-independent-sol-ultra-20260828.md
8ebe5f4f099e6cf15b0a4703dfb348aa6cc72df8fdbc60b1d095925fa3746d21
  cases/ggv_8_28_upper_endpoint_uniform_d10_fullmodes_audit_20260828/verify_uniform_d10.py
8ff338bdd47b7a53ba1515a7889823620120f92d718a03349fb9e3fd27014236
  cases/ggv_8_28_upper_endpoint_uniform_d10_fullmodes_audit_20260828/RESULT.json
e0f9037a7ca005a58b779ecce341ccbb3c349c0dfcbdf9a0e79c120624ad0047
  xmodel/ggv-upper-endpoint-uniform-d12-d13-fullmodes-sol-ultra-20260828.md
e5e2543ca50fc48623ccccf34f548f6171e79b31e6f80c8cfe6f5ca2b6798879
  cases/ggv_8_28_upper_endpoint_uniform_d12_d13_fullmodes_20260828/verify_uniform_d12_d13.py
06ca0152a7d05dd7b4549e74138b482fc572a62acae718751e7230577c5f28c8
  cases/ggv_8_28_upper_endpoint_uniform_d12_d13_fullmodes_20260828/RESULT.json
```

These match the review prompt, `SOURCE.sha256`, and `EVIDENCE.sha256` of
both packets.  The D9 producer/result pins recorded by the D10 packet
also match live bytes

```text
f4e40d3324a9dc9058b6ec80a01458468b3a90d0d3b4794841e76450c42e8dbc
  cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/verify_uniform_d9.py
9ca90959f284052bf669911c15e675892c1749b0bfed3cb4fd6462156e61b059
  cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/RESULT.json
```

Producer `--check` rebuilds both `RESULT.json` files byte-for-byte.  That
replay is a custody check only; it is not the proof.  The D12 producer
imports the D10 checker by pinned hash.  The independent checker does not
import either producer.

A separate standard-library checker, using only `fractions.Fraction`, did
the following.

1. Rebuilt `F0..F14`, `G0..G21` from the pinned head
   `F0=A^4`, `F1=A^2`, `F2=(1+A^2 Z)/4`, `F3=(Z+A T)/8`, `G0=A^6` and the
   raw windows, then expanded
   `D_n = sum_{i+j=n} ((12-j) F_i' G_j + (i-8) F_i G_j')`
   as sparse polynomials in the 303 coefficient variables.  Rows `D0..D3`
   vanish identically.  In `D4..D13`, every `X`-degree, every monomial,
   and every sign matches the frozen generator list (315 coefficients,
   10257 terms).
2. Ran the fractional recurrence
   `n A^4 y_n = sum_{1<=i<=n} (((alpha+1)i-n) F_i y_{n-i})`
   and, independently, the oriented square-root cube `S^3` with
   `S_0=A^2`.  They agree at weights `0..13` on both the post-D9 and
   post-D11 prefixes.
3. Applied the same-row operator
   `L_n(R) = 4(12-n) A^3 A' R - 8 A^4 R'`
   to the polar parts, without importing either producer Laurent ring.
   Raw rows satisfy `D_raw = -L_n(polar)` on the polar summand.
4. Evaluated producer mutations and additional hostile mutations by a
   three-way comparison: independent D5G recurrence, serialized JSON
   generators (including the affine `D22[0] -= 1` fold), and the claimed
   closed forms.

No CAS, floating point, interpolation, AWS, or `jc2-lean` was used.  No
canonical top-level file and no frozen packet file was edited.  The
independent checker recorded 499 checks and 0 failures.

## 2. Independent reconstruction of raw `D4..D13`

The frozen JSON identifies itself as the literal D5G system on `Q` with
303 variables and 513 generators in rows `D4..D22`.  Documentary
`F1,F2,F3` and `G1,G2,G3` window slots exist in the window census but are
not among the 303 variables: those weights are the pinned cascade, not
free slots.  There is no `G22` and no `D23`.  The field is `Q`.  `A=X^4-1`,
`H=A^2`, `F1=H`, `c2=0`.

Window bounds that are load-bearing for “raw `G` is polynomial”:

- `G10` stores degrees `0..14` and contains `A`.
- `G11` stores degrees `0..13` and cannot store `1/(4A)`.
- `G12` stores degree `0`, which is the `c12` gauge slot.
- `G13` omits degree `0` (lower bound 1).  That is a fixture constraint
  on the specialized `X`-polynomial, not a characteristic mode kill.
- `F5` and `F6` both store constants, so `Z V/64` and `V^2/256` are
  writable.

Every generator of `D4..D13` was rebuilt from the D5G formula and matched
the frozen term lists.  This is independent of both producer checkers.

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

Support at weight `n` requires `n-m >= 0`.  At `n=10,11` this leaves
exactly `c4,c6,c8,c10`.  At `n=12,13` it adds `c12`.  Empty causal
support is not permission to delete `c14..c20`.  Both producer
`RESULT.json` files serialize all nine modes, with `c14,c16,c18,c20`
marked `forced_rational`.

Two literal full-fixture points requiring nonzero `c16` were replayed
against every one of the 513 serialized generators, and independently in
the Laurent ring through weight 21:

```text
F = (A^2 + t/2)^2 + t^8,
point one:  G = (A^2 + t/2)^3
            requires c8 = -3/2, c16 = +3/8,
point two:  G = (A^2 + t/2)^3 + (3/2) t^8 (A^2 + t/2)
            requires c16 = -3/8.
```

Both points have `D4..D22 = 0` before the affine target fold.  A later
slot `G14[X^1]=1` is invisible to `D4..D13`.  Setting `G12[X^0]=1` is an
exact kernel through `D22` of the unfolder formula, confirming that `c12`
is a global additive gauge and must not be killed.

## 4. Theorem T5: D10 square defect, no mode kill

After the D8/D9 prefix, both the fractional recurrence and the
square-root cube give

```text
(F^{1/2})_0 = A^2,  (F^{1/2})_1 = 1/2,  (F^{1/2})_2 = Z/8,
(F^{1/2})_3 = V/16, (F^{1/2})_4 = R/2,
```

all polynomial.  Completing the square through weight four produces the
honest defect `Delta5 = F5 - R/2 - Z V/64`.  With `c6=0` the polar part
of `g10` is exactly `3 Delta5^2/(8 A^2)`: no `A^{-1}` class, no
`A^{-3}` or lower.  The born modes at this weight are polynomial:

```text
c4 F6,   c8 (F^{1/2})_2 = c8 Z/8,   c10 (F^{1/4})_0 = c10 A.
```

Same-row calculus: `L_10(3 Delta5^2/(8 A^2))` contributes
`9 A A' Delta5^2` at order `A^1`, so

```text
D10_raw = -9 A A' Delta5^2     (mod A^2).
```

`L_10` of every polynomial lands in `(A^3)`.  Polynomial `G10` in
`{1, A, A^2}` therefore cannot kill the `A^1` class.  Adding complete
holomorphic `c4` and `c8` continuations to the `Delta5=1` mutation leaves
`D4..D9=0` and `D10 = -9 A A'` exactly.

Closed form for `Delta5=1`:

```text
D10 = 36 X^3 - 36 X^7 = -9 A A'.
```

Scalings `Delta5 = -1, 2` repeat this and multiply it by 4, fixing both
the sign and the square power.  For non-constant `Delta5=X` the exact
raw row is

```text
D10 = -9 A A' X^2 + 6 A^2 X,
```

which is still congruent to `-9 A A' X^2` modulo `A^2`.  The extra
derivative term cannot cancel the obstruction.  `A` does not divide `X`.

Field-radical last step: `gcd(A,A')=1` by the Euclidean algorithm over
`Q` (`A'=4X^3`).  Thus `A | A' Delta5^2` implies `A | Delta5^2`.  On a
field, `Q[X]/(A)` is a product of fields because `A` is squarefree, and
`Delta5^2=0` there iff `Delta5=0` there.  Direct remainder checks for
several polynomials confirm `A | W^2` if and only if `A | W` in `Q[X]`.
Over a nonreduced coefficient ring the same calculation only puts
`Delta5^2` in `(A)`.

**D8 firewall, load-bearing.**  If `c6` is not killed, `(F^{3/4})_4` has
polar part

```text
3/(2048 A^5) - 3 Z/(512 A^3) + 3 V/(128 A) + 3 Z^2/(512 A).
```

The order-minus-five term dominates `Delta5^2/A^2`.  A mixed raw mutation
with leftover `c6=1` through `G7` still has `D8 = -(9/4) A^2 A'` as first
obstruction; with `F3=F4=0` the extra `G6,G7` slots are invisible to D10
and cannot cancel the square class.  D10 as stated is therefore invalid
unless D8 has already forced scalar `c6=0`.  That is the precise sense in
which T5 is conditional on D8/D9.

The coefficient `9` vanishes in characteristic 3, and the denominators
`64, 32` vanish in characteristic 2.  Characteristic zero is
load-bearing and is in the stated scope.

## 5. Theorem T6: D11 second divisibility, then `c10=0`

After `Delta5 = A S`, the square-root coefficient `S_5 = S/(2A)` is still
polar.  The weight-eleven continuation, with `c6=0`, has polar part
exactly

```text
-3 S^2 / (16 A^2)
+ c10 / (4 A)
+ (3/4) S (F6 - R Z/8 - V^2/256) / A.
```

There is no `A^{-3}` class.  The order-two coefficient is only `-3 S^2/16`
and cannot be cancelled by the order-one terms.  `L_11` of every order-one
polar monomial lands in `(A^2)`, so

```text
D11_raw = +(15/4) A A' S^2     (mod A^2).
```

The coefficient `15/4` vanishes in characteristics 3 and 5; characteristic
zero is again load-bearing.  Squarefreeness gives `A | S`.

After `S = A Q` the `S Delta6 / A` term becomes polynomial.  The only
remaining pole is `c10/(4A)`, and

```text
L_11(c10/(4A)) = 3 c10 A^2 A',
D11_raw        = -3 c10 A^2 A'
```

exactly on that summand (not merely modulo `A^3`: the polar is a pure
`A^{-1}` multiple of the scalar `c10`).  `gcd(A,A')=1` forces the scalar
`c10=0`.  The `G11` window cannot store `1/(4A)`.  Adding holomorphic
`G11=1` to the `c10=1` mutation leaves the `A^2` class untouched.

Causal order is essential.  A mixed raw mutation with `S=1` (so
`Delta5=A`) together with `c10=1` has `D4..D10=0`, but `D11` is neither
the pure square law nor the pure `c10` residual.  Killing `c10` before
`A|S` is invalid.

The statement `c10=0` is scalar.  A fake non-constant mode `c10=A`,
implemented as polynomial `G10=A^2` and holomorphic `G11=1/4`, is **not**
a kernel: `D10` and `D11` are both nonzero.  If `c10` were allowed to be
an `X`-polynomial, the remaining pole `c10/(4A)` would become holomorphic
upon `A|c10`, and T6 would be a weaker divisibility.  The characteristic
ODE treats `c10` as a constant; T6 is that scalar statement.

Combined with T5:

```text
F5 = R/2 + Z V / 64 + A^2 Q,   c10 = 0.
```

At this stage the D11 defect `Delta6 = F6 - R Z/8 - V^2/256` correctly
omits `Q/2`, because `Q` has only just appeared as `S = A Q` and has not
yet been absorbed into the regular part of `F^{1/2}`.

## 6. Theorem T7: D12 square defect, no mode kill

After T6 the square-root coefficients are polynomial through weight five,
with `(F^{1/2})_5 = Q/2`.  Completing the square at weight six produces
the honest D12 defect

```text
Delta6 = F6 - Q/2 - R Z / 8 - V^2 / 256.
```

This is not the D11 `Delta6`.  The extra `Q/2` is the regularized `S_5`.
Omitting it is the same class of error as omitting `Z V/64` at D10.

With `c6=c10=0` the polar part of `g12` is exactly `3 Delta6^2/(8 A^2)`.
This was the most important negative search at this row: an undetected
`A^{-1}` class would have been invisible in `D12 mod A^2` (because
`L_12` of an `A^{-1}` term lands in `(A^2)` when `12-n=0`) and would have
propagated into D13.  There is none.  There is also no `A^{-3}` or lower.
The born modes are polynomial:

```text
c4 F8,   c8 (F^{1/2})_4 = c8 R/2,   c12 (F^0)_0 = c12.
```

Same-row calculus gives

```text
D12_raw = -6 A A' Delta6^2     (mod A^2).
```

The coefficient is `-6`, not a copy of D10’s `-9`: the `(12-n)` term in
`L_n` vanishes at `n=12`, leaving only the derivative contribution
`6 A A' Delta6^2` before the overall minus.  Closed form for `Delta6=1`:

```text
D12 = 24 X^3 - 24 X^7 = -6 A A'.
```

Scalings `-1, 2` fix the square power.  For `Delta6=X` the exact raw row
is `-6 A A' X^2 + 6 A^2 X`, still congruent modulo `A^2`.  Polynomial
`G12` in `{1,A,A^2}` and the holomorphic modes `c8,c12` cannot cancel
the class.

Every summand of `Delta6` is load-bearing.  On the exact square with
`Z=V=1`, `R=Q=X`,

```text
S = A^2 + t/2 + t^2/8 + t^3/16 + (X/2) t^4 + (X/2) t^5,
F6 = 1/256 + (5/8) X = Q/2 + R Z/8 + V^2/256,
```

and `D4..D22=0` before the affine fold.  Setting `F6=0` and continuing
`F^{3/2}` through `G11` produces the predicted literal D12 residual.
Isolating each summand separately (drop only `Q/2`, only `R Z/8`, or
only `V^2/256`) likewise produces a nonzero D12 of the predicted square
shape.  The producer’s all-at-once `F6=0` mutation is therefore not
masking a cancelled cross term.

## 7. Theorem T8: D13 second divisibility, no mode kill

After `Delta6 = A S` the polar part of `g13` is exactly

```text
-3 S^2 / (16 A^2) + 3 S (F7 - Q Z/8 - R V/16) / A.
```

No characteristic mode appears in this polar part: `c12 (F^0)_1 = 0`,
`c8 (F^{1/2})_5 = c8 Q/2` is polynomial, `c4 F9` is polynomial, and
`c14` is not born.  `L_13` of the order-one terms lands in `(A^2)`, so

```text
D13_raw = +(9/4) A A' S^2     (mod A^2).
```

Closed form for `S=1`:

```text
D13 = -9 X^3 + 9 X^7 = (9/4) A A'.
```

Scalings `-1, 2` fix the square power.  After `S = A T` the remaining
polar part is empty, so there is no analogue of the D11 `c10` kill.
Combined:

```text
F6 = Q/2 + R Z / 8 + V^2 / 256 + A^2 T.
```

The `G13` window’s missing degree-0 slot is a fixture constraint on the
specialized `X`-polynomial, not a further characteristic consequence, and
is not charged.

## 8. Mutations and falsification search

Producer mutations, independently rebuilt from window slots and checked
three ways through `D22` (serialized generators include the affine fold
`D22[0] -= 1`):

| mutation | prior rows | residual |
|---|---|---|
| `Delta5=1` through `G6` | `D4..D9=0` | `-9 A A'` |
| `Delta5=-1,2` | same | square scaling |
| `S=1` (`Delta5=A`) through `G10` holomorphic | `D4..D10=0` | `+(15/4) A A'` |
| `c10=1` as `G10=A` | `D4..D10=0` | `-3 A^2 A'` |
| `Delta6=1` through `G7` | `D4..D11=0` | `-6 A A'` |
| `S=1` (`Delta6=A`) through `G12` holomorphic | `D4..D12=0` | `+(9/4) A A'` |
| `Z=V=1,R=0` exact square, drop `F5=1/64` | `D4..D9=0` | `-(9/4096) A A'` |
| `Z=V=1,R=Q=X` exact square, drop `F6` | `D4..D11=0` | predicted `Delta6^2` law with `X`-derivative |
| `G12=1` | `D4..D22` formula `=0` | additive gauge |
| `c16` points one and two | `D4..D22` formula `=0` | both signs of `c16` |

Hostile replacements that failed to cancel any obstruction: polynomial
`G10` against `Delta5`; polynomial `G12` against `Delta6`; complete
`c4` and `c8` together with `Delta5`; complete `c4` and `c8` together
with `c10`; `c8` and `c12` together with `Delta6`; `Delta5=X` and
`Delta6=X` (congruence holds, `A` divides neither); leftover `c6`
through `G7` (D8 still the mode obstruction; D10 still the square law
when `F3=F4=0`); mixed `S` and `c10` (D11 neither pure residual);
isolated omission of `R/2`, of `Q/2`, of `R Z/8`, and of `V^2/256`;
fake `c10=A` (not a kernel); holomorphic `G11=1` against scalar `c10`;
illegal `G14[X^1]=1` (invisible at these rows).

No literal raw field point or local Laurent mutation was found that
falsifies T5--T8 inside the stated hypotheses.

## 9. Scope

These are statements about characteristic-zero field points of one fixed
303-variable branch-P fixture, at rows `D10` through `D13`, after the
D8/D9 prefix.  They are not:

- scheme-theoretic divisibility over nonreduced coefficient rings;
- emptiness of the endpoint, of cutoff 4/3/2, or of any later row;
- an unrestricted branch-P theorem, a Keller-pair theorem, or JC2;
- a licence to drop `c14..c20`, or to kill the additive gauge `c12`;
- a claim that `D11` may kill `c10` before `A|S`, or that `D10` may be
  consumed before the D8 mode kill;
- a claim that a non-constant `X`-polynomial may play the role of
  scalar `c10`.

The coefficients `9`, `15/4`, `6`, `9/4`, and `3` make characteristic
zero essential.  The D8/D9 prefix remains a live external hypothesis: if
it fails, T5--T8 as stated fail with it.

## Hashes

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
e24eb71b8df1a4c93fb4d156e2dd5084e53abccd332e793aaa584307e6d32a29  xmodel/ggv-upper-endpoint-uniform-d10-d11-fullmodes-independent-sol-ultra-20260828.md
8ebe5f4f099e6cf15b0a4703dfb348aa6cc72df8fdbc60b1d095925fa3746d21  cases/ggv_8_28_upper_endpoint_uniform_d10_fullmodes_audit_20260828/verify_uniform_d10.py
8ff338bdd47b7a53ba1515a7889823620120f92d718a03349fb9e3fd27014236  cases/ggv_8_28_upper_endpoint_uniform_d10_fullmodes_audit_20260828/RESULT.json
e0f9037a7ca005a58b779ecce341ccbb3c349c0dfcbdf9a0e79c120624ad0047  xmodel/ggv-upper-endpoint-uniform-d12-d13-fullmodes-sol-ultra-20260828.md
e5e2543ca50fc48623ccccf34f548f6171e79b31e6f80c8cfe6f5ca2b6798879  cases/ggv_8_28_upper_endpoint_uniform_d12_d13_fullmodes_20260828/verify_uniform_d12_d13.py
06ca0152a7d05dd7b4549e74138b482fc572a62acae718751e7230577c5f28c8  cases/ggv_8_28_upper_endpoint_uniform_d12_d13_fullmodes_20260828/RESULT.json
9b9840216227d6452e14f3d5782689fe291eb339e8ba8819ee96045f13dd6830  xmodel/ggv-upper-endpoint-uniform-d10-d13-fullmodes-hostile-review-grok46-20260828-check.py
```

The SHA-256 of this review file is the digest of the on-disk bytes of

```text
xmodel/ggv-upper-endpoint-uniform-d10-d13-fullmodes-hostile-review-grok46-20260828.md
```

computed after the final write, recorded immediately below.

<!-- self-hash -->
c70a31639a4d9000352a8e34a0e8830dcbed26f0ccc1b954fee3c57cc0d901f9  report body above this delimiter
