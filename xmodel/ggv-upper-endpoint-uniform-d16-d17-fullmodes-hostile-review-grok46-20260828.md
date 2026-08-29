# Hostile review: uniform full-mode `D16`/`D17` cascade

Reviewer: Grok 4.6, independent hostile lane  
Date: 2026-08-28  
Charged report:
`xmodel/ggv-upper-endpoint-uniform-d16-d17-fullmodes-sol-ultra-20260828.md`  
Frozen packet:
`cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828/`  
Independent checker:
`xmodel/ggv-upper-endpoint-uniform-d16-d17-fullmodes-hostile-review-grok46-check.py`  
Independent result:
`xmodel/ggv-upper-endpoint-uniform-d16-d17-fullmodes-hostile-review-grok46-RESULT.json`

## Verdict

| Charge | Verdict |
|--:|---|
| `D16`: `polar(g16)=(3 B^2/8 + c8 B/2 + c16)/A^2` forces `3 B^2+4 c8 B+8 c16=8 A^2 M`; `c16` unique if a polynomial continuation exists, and not killed | **PASS** |
| Gauge invariance / nine-mode schedule: `Bhat=B+2 c8/3`, `J16=c16-c8^2/6`, live `c8`, born `c16`, retained `c18,c20`, `c12` shift | **PASS** |
| `D17` causal `c16` cancellation: predecessor `+6 c16 A'/A` cancels same-row `-6 c16 A'/A`; D17 does not kill `c16` | **PASS** |
| `D17` `A^2` relation: after (D16), `(3 B+2 c8) C-2 M=4 A^2 N`; both `A`-adic lifts live | **PASS** |
| Literal 513-generator controls, `G16`/`G17` ranks, signs, powers | **PASS** |
| Lower-window `C16,0`,`C16,1`,`C17,0`,`C17,1` and preservation of `C13`--`C15`/`H0` | **PASS** |
| Overall | **PASS** |

All six prompt-charged SHA-256 values match the live bytes.  The independent
Laurent ring, square-root cube, termwise `D16`/`D17` reconstruction, and
three-way 513-generator replay confirm the charged identities.  Nothing is
REFUTED.  `K17_uniform` is only a structural ancestor candidate.  No scheme
divisibility, endpoint emptiness, unrestricted branch-P, Keller-pair, or JC2
conclusion is licensed.

D16/D17 are conditional on the independently reviewed D15 completion
`F7=T/2+Q Z/8+R V/16+A^2 Y` and `c6=c10=c14=0`.  This lane's D14/D15 review
is PASS of the live repaired packet.  Prefix identities used here were
re-derived in an independent Laurent ring; they are not imported from the
D16/D17 producer.

## Promotable statements

Work over a characteristic-zero field, on a point of the complete fixed
branch-P 303-variable / 513-generator fixture whose authoritative source is

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
```

with `A=X^4-1`.  Continue from the D15 field-radical prefix

```text
F4 = V/16 + Z^2/64 + A^2 R,
F5 = R/2 + Z V/64 + A^2 Q,
F6 = Q/2 + R Z/8 + V^2/256 + A^2 T,
F7 = T/2 + Q Z/8 + R V/16 + A^2 Y,
c6 = c10 = c14 = 0.
```

The complete characteristic continuation is the nine-mode series of §3.
At weights 16 and 17 the live modes are `c4,c8,c12,c16`; `c18,c20` are
retained in the formalism and have empty support.

Write

```text
B = F8 - Y/2 - T Z/8 - Q V/16 - R^2/4,
C = F9 - Q R/2 - T V/16 - Y Z/8.
```

**T8 (D16).**  After the prefix, the weight-16 continuation satisfies

```text
polar(g16) = (3 B^2/8 + c8 B/2 + c16) / A^2
```

exactly, as a Laurent identity.  There is no `A^{-3}` or lower.  The same-row
operator `L_16` annihilates the indicial kernel `c16/A^2`, so raw `D16` does
not see the constant `c16`.  Raw `G16` is the window of degrees `2..8` and
cannot store `A^{-2}`, a constant, or a linear term.  Polynomiality therefore
requires the numerator to lie in `(A^2)`:

```text
3 B^2 + 4 c8 B + 8 c16 = 8 A^2 M.
```

A nonzero scalar cannot lie in `(A^2)`, so if a polynomial continuation
exists then `c16` is unique.  It is not forced to vanish.  Literal
determinant-zero fixtures realise both `c16=3/8` and `c16=-3/8`.  Live `c8`
remains in the cross term and is not normalised.

**T9 (gauge and modes).**  The additive `F8` gauge of the complete
nine-mode family acts by

```text
B  -> B + lambda,
c8 -> c8 - 3 lambda/2,
c12 -> c12 - c4 lambda,
c16 -> c16 - c8 lambda/2 + 3 lambda^2/8.
```

The `c12` shift is required by `c4 t^4 F` when `F -> F + lambda t^8`.  It has
no D16/D17 polar tail because `F^0` has no positive-weight coefficients;
literal `c4=1` families with and without the `G12` adjustment are raw kernels
through `D22`.  The combinations

```text
Bhat = B + 2 c8/3,     J16 = c16 - c8^2/6
```

are invariant, and (D16) is

```text
(3/8) Bhat^2 + J16 = A^2 M.
```

`H0=c8/2+3 F8(0)/4` remains live and invariant.  No gauge slice or
square-root branch is selected.  All nine modes are retained in the schedule.

**T10 (D17 causal firewall).**  Before using (D16),

```text
polar(g17) = -(3 B^2/8 + c8 B/2 + c16)/(2 A^4)
           + (3 B/4 + c8/2) C / A^2.
```

The `A^{-4}` block retains the linked `c16` successor.  If a free `c16/A^2`
is illegally kept, the predecessor mixed pair `(F1,G16)` contributes
`+6 c16 A'/A` and `L_17(-c16/(2 A^4))` contributes `-6 c16 A'/A`.  They
cancel, as do the corresponding polynomial storage defects.  D17 does not
independently kill `c16`.  The raw `G16` window is what fixes it, through T8.

**T11 (D17 after T8).**  Substituting (D16) converts the full `A^{-4}`
block, including `c16`, to `-M/(2 A^2)`.  The remaining pole is

```text
polar(g17) = ((3 B/4 + c8/2) C - M/2) / A^2.
```

Polynomiality is exactly

```text
(3 B + 2 c8) C - 2 M = 4 A^2 N,
```

i.e. `K17_uniform := (3 B+2 c8) C-2 M` lies in `(A^2)`.  Same-row calculus
gives the first lift `A | obstruction` at a field point, then the second
lift `A | ell` after `obstruction = A ell`, visible as the `A^2` class
`12 A^2 A' ell`.  A literal mutation with `K=A L` and `L` not in `(A)` has
`D4..D16=0` and a nonzero `D17` residual in `(A^2)` but not in `(A^3)`.
Stopping after one factor of `A` is therefore not the theorem.

**T12 (lower window).**  Raw `G16` and `G17` omit degrees `0` and `1`.  After
T8--T11 the continuations are holomorphic, and their `X^0`/`X^1` jets are
live scalar equations.  The constants are

```text
C16,0:  M0 = 3 Q0^2 T0/16 + 3 Q0 R0 Y0/8 + 3 R0 T0^2/16
             + 3 T0 V0 Y0/64 + 3 Y0^2 Z0/64,
C17,0:  N0 = 3 Q0^2 Y0/16 + 3 Q0 T0^2/16 + 3 R0 T0 Y0/8
             + 3 V0 Y0^2/128.
```

The exact linear equations `C16,1` and `C17,1`, including every allowed raw
`F9..F14` jet, match the charged `RESULT.json`.  `C13`,`C14`,`C15` and
`H0` are carried unchanged from the D15 packet and remain gauge-invariant.
`F9` through `F14` omit the degrees their windows omit; those constant jets
are window-forced zeros, not discarded live unknowns.

Not promoted: scheme-theoretic divisibility, emptiness of any cutoff, any
row after `D17`, transport of `K17_uniform` to the cutoff-three `K`
relation, unrestricted branch-P, Keller pairs, JC2, dropping `c18,c20`, a
D17 kill of `c16`, a D16 kill of `c8` or `B`, or a claim that `C13`--`C17`
exhaust the lower-window ideal.

## 1. Custody and method

Prompt-charged SHA-256 values, all matching the live bytes:

```text
4f7b363addd020e95096ffa289ff96408b21fc4b1c09cfd6235571956117408a
  xmodel/ggv-upper-endpoint-uniform-d16-d17-fullmodes-sol-ultra-20260828.md
5904d7b19dc5d46d31a781150c4b6de9e62e32812b554006e92f78f9d76fd5d9
  cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828/verify_uniform_d16_d17.py
2a6f363df8fb4aef94f01d7a938e3bfcff15f6db49af3164e36367c9a6d1929a
  cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828/RESULT.json
53f2a7a276be4a0aa7f77cc031e270d573fc78b5db64cdb76a0cf6c502e52517
  cases/ggv_8_28_upper_endpoint_uniform_d14_d15_fullmodes_20260828/verify_uniform_d14_d15.py
7546618aa5a40ed983014159c1d39337396607562912570c97cfe2ee779394ea
  cases/ggv_8_28_upper_endpoint_uniform_d14_d15_fullmodes_20260828/RESULT.json
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
```

Live `SOURCE.sha256` / `EVIDENCE.sha256` pins match the live files.  The
producer was not used as a derivation.  A separate standard-library checker,
using only `fractions.Fraction`, did the following.

1. Rebuilt `D16` and `D17` from the pinned head `F0=A^4`, `F1=A^2`,
   `F2=(1+A^2 Z)/4`, `F3=(Z+A T)/8`, `G0=A^6` and the raw windows, then
   expanded `D_n=sum_{i+j=n}((12-j) F_i' G_j+(i-8) F_i G_j')` as sparse
   polynomials in the 303 coefficient variables.  Every `X`-degree, every
   monomial, and every sign matches the frozen generator list (47
   coefficients, 3618 terms).
2. Ran the fractional recurrence
   `n A^4 y_n = sum_{1<=i<=n} (((alpha+1)i-n) F_i y_{n-i})`
   and, independently, the oriented square-root cube `S^3` with
   `S_0=A^2`.  They agree at weights `0..17`.
3. Applied the same-row operator
   `L_n(R)=4(12-n) A^3 A' R - 8 A^4 R'`
   to polar parts, and the mixed `(F_1,G_16)` term of `D_17`, without
   importing the producer Laurent ring.
4. Evaluated producer mutations and additional hostile mutations by a
   three-way comparison: independent D5G recurrence, serialized JSON
   generators, and the claimed closed forms.  Every mutation was checked
   against all 513 generators.
5. Extracted `X^0` and `X^1` jets of holomorphic `g16,g17` after the
   combined completion, and re-extracted `C13`--`C15` from `g13,g14,g15`.

No CAS, floating point, interpolation, AWS, or `jc2-lean` was used.  No
canonical top-level file and no frozen packet file was edited by this
review.

The independent checker reports 361/361 PASS.

## 2. Independent reconstruction of raw `D16`--`D17`

The frozen JSON is the literal D5G system on `Q` with 303 variables and
513 generators in rows `D4..D22`.  Documentary `F1,F2,F3` window slots
exist in the census but are not among the 303 variables.  There is no
`G22` and no `F15`.

Load-bearing window bounds:

| window | degrees | consequence |
|---|---|---|
| `F8` | `0..8` | `F8(0)` is a real slot; enters `B` and `H0` |
| `F9` | `1..7` | `F9(0)=0` is forced; `C` has no constant from `F9` itself |
| `F10`,`F11` | omit degree 0 | `f101`,`f111` are live linear jets |
| `F12`--`F14` | omit degrees `0,1` | no live `f121` in `C16,1` |
| `G16` | `2..8` | cannot store `c16/A^2`, a constant, or a linear term |
| `G17` | `2..7` | cannot store `-c16/(2 A^4)` or `K/(4 A^2)` |

Row hashes of the authoritative source, independently confirmed by
termwise reconstruction:

```text
D16  9797edd07406098cd9127cef3b40bffa3260f673d1f2735df0b6b88914a46001
D17  ef66ca0d870a4c2f9bc8db38b7d0220921be0ab4127981fac24d947dd73dc0dc
```

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

Birth values `y_0=A^{(12-m)/2}` were recomputed for all nine modes.
Support at weight `n` requires `n-m>=0`.  At `n=16` this leaves
`c4,c8,c12,c16` (with `c6=c10=c14` already killed).  In particular `c16`
is the first weight-16 forced negative mode, born as `c16/A^2`, and is
not omitted.  Empty causal support of `c18,c20` is not permission to
delete them.  Live `RESULT.json` serializes all nine, with `c16` marked
`retained_and_uniquely_forced_by_D16_polynomiality` and `c18,c20` marked
`retained_unborn`.

Direct from the recurrence with `alpha=-1/2`:

```text
(F^{-1/2})_0 = A^{-2},
(F^{-1/2})_1 = -1/(2 A^4).
```

These depend only on pinned `F0,F1`.  The `c16` polar pieces at D16/D17
are therefore cascade-independent.

At D16, `c4 F12` and `c12 (F^0)_4` are polynomial (`(F^0)_4=0`).  At D17
the same holds for `c4 F13` and `c12 (F^0)_5`.  Live `c8 (F^{1/2})_8`
contributes the order-minus-two cross term `c8 B/(2 A^2)`.

## 4. Theorem T8: `D16` forces `c16` uniquely and does not kill it

After the D15 prefix both the fractional recurrence and the square-root
cube give

```text
polar(g16) = (3 B^2/8 + c8 B/2 + c16) / A^2
```

exactly.  The order-two coefficient involves both the square `3 B^2/8` and
the live cross term `c8 B/2`.  The only new born summand is `c16`.

Same-row calculus:

```text
L_16(N/A^2) = -8 A^2 N',
D16_same_row = 8 A^2 N'.
```

`L_16(c16/A^2)=0` identically, because `c16` is a constant.  Characteristic
zero is load-bearing for the coefficient `8`.  The displayed congruence is
therefore blind to `c16`; uniqueness comes from the polynomial window, not
from a raw `D16` class in `c16`.

After writing `N=A^2 M`, `g16` is holomorphic.  If two values of `c16`
realised polynomial continuations for the same `B,c8`, their difference
would be a scalar in `(A^2)`.  `A^2` contains no nonzero scalar, so `c16`
is unique when it exists.  Exact points

```text
F8=1,                         c8=-3/2, c16= 3/8,
F8=1, G8=(3/2) A^2, G9=3/4,  c8=0,    c16=-3/8
```

have `D4` through `D22` identically zero before the affine fold (folded
`D22` generator 495 equals `-1`).  Both signs are live.  Omitting `c16`
from the formalism would make uniqueness vacuously empty; the mode must be
present in order to be forced.

The same-row matrix of the seven `G16` slots against the 24 raw `D16`
generators has rank 7 and nullity 0.  A hostile polynomial `G16=X^2`
against the `B=X` square does not kill the obstruction.  Source-level
square mutations at scalars `-1,1,2` scale quadratically as `6 A^2 X`;
mixed `c8` mutations scale as `A^2 (6 X+4 c8)`.

Causal order is load-bearing.  Omitting the square and cross terms leaves
an `A^{-2}` class that dominates any later attempt to set `c16=0`.

## 5. Theorem T9: additive gauge, `Bhat`, `J16`, and `c12`

The binomial expansion of the complete family under `F -> F+lambda t^8`
gives exactly the charged action on `B,c8,c16`, and the accompanying
`c12 -> c12-c4 lambda` from `c4 t^4 F`.  Direct polynomial algebra shows
`Bhat` and `J16` are fixed, and

```text
(3/8) Bhat^2 + J16 = 3 B^2/8 + c8 B/2 + c16.
```

The literal family `F8=lambda`, `G8=A^2`, `G9=1/2` at `lambda=-1,1,2` is a
raw kernel through `D22` and keeps `Bhat=2/3`, `J16=-1/6`.  Adding `c4=1`
via `G4=A^4`, `G5=A^2`, `G6=1/4` remains a kernel whether or not `G12`
absorbs `lambda`; that is the no-tail claim.  `H0` is related by
`Bhat(0)=4 H0/3 - (Y/2+T Z/8+Q V/16+R^2/4)(0)` and is not used as a
normalisation.

The rootwise display `Bhat(alpha)^2=-8 J16/3` at `A(alpha)=0` is an
equivalent writing of the centered congruence.  No square root is chosen.
Branches coalesce when `J16=0`.

## 6. Theorem T10: D17 does not kill `c16`

With `F8=base8+B` and `c14=0`, both recurrences give the pre-relation
polar of §T10, including `-c16/(2 A^4)`.  The predecessor pair
`(i,j)=(1,16)` is cascade-independent because `F1=A^2` is pinned:

```text
(12-16) F1' (c16/A^2) + (1-8) F1 (c16/A^2)' = +6 c16 A'/A,
L_17(-c16/(2 A^4))                                 = -6 c16 A'/A.
```

No other `(i,j)` at weight 17 carries a free `c16` (`c16` is born at 16).
The two pieces cancel.  Polynomial storage defects cancel with the opposite
overall sign.  The charged packet records this cancellation and does not
claim a successor-row kill.  That is the correct theorem.

## 7. Theorem T11: `K17_uniform` in `(A^2)`

After T8 the `A^{-4}` block becomes `-M/(2 A^2)`, leaving the order-minus-two
obstruction `(3 B/4 + c8/2) C - M/2`.  Then

```text
L_17(N/A^2) = -4 A A' N - 8 A^2 N'  (mod higher),
D17_raw     = 4 A A' N               (mod A^2).
```

Field squarefreeness and `gcd(A,A')=1` give the first lift `A | N`.  After
`N=A ell`, the remaining class is `12 A^2 A' ell`, so the second lift
`A | ell` is independent of the first.  The exact polynomial-window
condition is `N in (A^2)`, i.e.

```text
(3 B + 2 c8) C - 2 M = 4 A^2 N.
```

A first-failure mutation with `B=1`, `c8=0`, `c16=-3/8`, `C=s X`, `M=0`
has prior rows zero and residual `s (3 A A' X + 6 A^2)`, linear in `s`.
The second-lift mutation of the charged packet has `K=A L` with
`L rem A = -15/32 + 3 X^2/2`, prior rows zero, and residual in `(A^2)`
but not in `(A^3)`.  Omitting the inserted polynomial `G17` still leaves a
nonzero `D17`.  The full `(A^2)` condition is live.

`K17_uniform` is the structural uniform ancestor candidate of the
cutoff-three `K` relation.  No specialisation map is asserted, and none is
promoted.

## 8. Theorem T12: `C16`,`C17` and carried `C13`--`C15`

After T8--T11 the continuations `g16,g17` are holomorphic.  Because
`A=X^4-1` has no degrees `1,2,3`, the `X^0` and `X^1` jets of an A-adic
series coincide with evaluating A-adic coefficients at `A(0)=-1` together
with the first jets of the live symbols.  The resulting jets match the
charged lists exactly.  Window-forced zeros of `F9(0)` and of
`F12,F13,F14` at degrees `0,1` do not hide extra live monomials.

`C13`--`C15` were re-derived from `g13,g14,g15` after the D15 completion
and match the D14/D15 packet byte-for-byte as strings.  The gauge
`F8(0)->F8(0)+lambda`, `c8->c8-3 lambda/2` leaves `H0` and each of
C13--C15 invariant.  The D16 packet carries them honestly and does not
solve, drop, or normalise them.

## 9. Scope

These are statements about characteristic-zero field points of one fixed
303-variable branch-P fixture, at rows `D16` and `D17`, after the D15
prefix.  They are not:

- scheme-theoretic divisibility over nonreduced coefficient rings;
- emptiness of the endpoint, of any cutoff, or of any later row;
- an unrestricted branch-P theorem, a Keller-pair theorem, or JC2;
- a licence to drop `c18,c20`, or to kill `c16`;
- a D16 normalisation of `c8`, `B`, `H0`, carriers, or units;
- a transport of `K17_uniform` to cutoff-three `K` without a separate
  literal map;
- a claim that `C13`--`C17` are the full lower-window ideal.

The coefficients `8`, `3/8`, `3/4`, and `A'=4 X^3` make characteristic
zero essential.  Squarefreeness of `A` is essential for the radical step
in the first D17 lift; the D16 relation itself is polynomial-window
divisibility `A^2 | N`.

## Hashes

Charged packet and predecessors (all verified):

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
53f2a7a276be4a0aa7f77cc031e270d573fc78b5db64cdb76a0cf6c502e52517  cases/ggv_8_28_upper_endpoint_uniform_d14_d15_fullmodes_20260828/verify_uniform_d14_d15.py
7546618aa5a40ed983014159c1d39337396607562912570c97cfe2ee779394ea  cases/ggv_8_28_upper_endpoint_uniform_d14_d15_fullmodes_20260828/RESULT.json
4f7b363addd020e95096ffa289ff96408b21fc4b1c09cfd6235571956117408a  xmodel/ggv-upper-endpoint-uniform-d16-d17-fullmodes-sol-ultra-20260828.md
5904d7b19dc5d46d31a781150c4b6de9e62e32812b554006e92f78f9d76fd5d9  cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828/verify_uniform_d16_d17.py
2a6f363df8fb4aef94f01d7a938e3bfcff15f6db49af3164e36367c9a6d1929a  cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828/RESULT.json
204e93d1d918dff670fef3abb8a3010e7eb3d4b4568e19ec605cc4f743aabc10  cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828/README.md
1d810d703a5c65165a8a3daaa262e42b891f170ba83bb33aec76ea647df5bc97  cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828/SOURCE.sha256
6ba69c331378ffee8eef5bff2d8a7a4a9f5b58ac239690e4ab0a56dfc83276d6  cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828/EVIDENCE.sha256
```

New artifacts of this review:

```text
0b3bccc3fb0bcf3d44c5b5a81d392a4ba224db505b489a2779e8e99e76eaffb0  xmodel/ggv-upper-endpoint-uniform-d16-d17-fullmodes-hostile-review-grok46-check.py
88858431199fa5daeb9b46dd0a9d19ee5a17bbe952a94ce8f91bef7e485d0acd  xmodel/ggv-upper-endpoint-uniform-d16-d17-fullmodes-hostile-review-grok46-RESULT.json
```

The SHA-256 of this review file is the digest of the on-disk bytes of

```text
xmodel/ggv-upper-endpoint-uniform-d16-d17-fullmodes-hostile-review-grok46-20260828.md
```

computed after the final write, recorded immediately below.

<!-- self-hash -->
d7d0124439a267c6ef3a7d23437f1f1b640f25a9046dde34d55d1876a983856d  report body above this delimiter
