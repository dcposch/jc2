# Hostile review: uniform full-mode `D8` mode-kill and `D9` square defect

Reviewer: Grok 4.6, independent hostile lane  
Date: 2026-08-28  
Charged report:
`xmodel/ggv-upper-endpoint-uniform-d9-fullmodes-sol-ultra-20260828.md`  
Frozen packet:
`cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/`  
Independent checker:
`xmodel/ggv-upper-endpoint-uniform-d9-fullmodes-hostile-review-grok46-20260828-check.py`

## Verdict

**PASS.**

The two charged field-point theorems survive independent reconstruction of
the raw `D4..D9` generators, an independent Laurent/square-root calculation
of the full nine-mode continuation, operator-level sign checks, producer
replay, and a search for cancelling raw mutations.  Nothing charged is
REFUTED or sent back for REPAIR.  No scheme divisibility, endpoint
emptiness, unrestricted branch-P, Keller-pair, or JC2 conclusion is
licensed.

| # | Charge | Verdict |
|--:|---|---|
| 1 | Charged hashes; independent reconstruction of raw `D4..D9` | **CONFIRMED** |
| 2 | After reviewed `D7` and leading `D8`, polynomiality at `D8` forces scalar `c6=0`; no born mode, raw kernel, gauge, or window coefficient cancels the pole | **CONFIRMED** |
| 3 | Full `g9` polar numerator; `D9_raw = +(21/4) A A' W^2 mod A^2`; sign, powers, squarefree field-radical `A\|W` | **CONFIRMED** |
| 4 | Complete nine-mode firewall `c4,c6,c8,c10,c12,c14,c16,c18,c20` retained | **CONFIRMED** |
| 5 | Replay / replacement of every live mutation; search for a falsifying raw or Laurent point | **CONFIRMED** (no falsifier) |
| 6 | Scope: complete 303-variable branch-P fixture, char-0 field points only | **CONFIRMED** |

Custody hygiene, not a mathematical defect: the review prompt listed a
65-hex-digit string `ccff7840...ece16490e` as the charged-report SHA-256.
The live file and the packet freeze pin are the 64-digit digest
`ccf78403684ef7ee7e9f85336b4ccf86a01d679ba61b6327f4d2400ece16490e`.  The
prompt string is that freeze pin with one extra `f`.  The freeze file, not
the prompt transcription, is the custody record.

## Promotable statements

Work over a characteristic-zero field, on a point of the complete fixed
branch-P 303-variable / 513-generator fixture whose authoritative source is

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
```

with `A = X^4-1`.  Continue from the already reviewed field-radical
conclusions

```text
T = A V,
F4 - V/16 - Z^2/64 = A W.
```

The complete characteristic continuation is the nine-mode series of §4.
At weights 8 and 9 the only born modes are `c4,c6,c8`.

**T3.**  `D4 = ... = D8 = 0` forces the scalar characteristic constant
`c6 = 0`.  Equivalently,

```text
polar(g8) = 3 c6 / (32 A),
D8_raw = -(9/4) c6 A^2 A'     (mod A^3).
```

No born mode, polynomial `G8` window, additive gauge, or allowed later
slot cancels this `A^2` class.  The constant `c6` is a scalar of the
characteristic ODE, not an `X`-polynomial.

**T4.**  After T3, `D4 = ... = D9 = 0` forces `A | W` at a field point.
Equivalently, writing `N = -3 W^2 / 16`,

```text
polar(g9) = N / A^2 + (3 F5 W/4 - 3 V W Z / 256) / A,
D9_raw    = +(21/4) A A' W^2     (mod A^2).
```

Since `gcd(A,A') = 1` in characteristic zero, this yields `A | W^2`, and
squarefreeness of `A` upgrades that to `A | W` on a field.  The upgrade is
not a scheme-theoretic claim over nonreduced coefficient rings.

**Ordering.**  T4 is invalid if T3 is omitted.  Before `c6 = 0`, `g9` has
an order-three term `-c6/(128 A^3)` which dominates `W^2/A^2` and changes
the leading raw class of `D9`.

Not promoted: scheme divisibility, emptiness of any cutoff, any row after
`D9`, unrestricted branch-P, Keller pairs, JC2, or the statement that a
non-constant `X`-polynomial multiple of `A` can play the role of `c6`.

## 1. Custody and method

Live SHA-256 values, recomputed on disk:

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
ccf78403684ef7ee7e9f85336b4ccf86a01d679ba61b6327f4d2400ece16490e
  xmodel/ggv-upper-endpoint-uniform-d9-fullmodes-sol-ultra-20260828.md
f4e40d3324a9dc9058b6ec80a01458468b3a90d0d3b4794841e76450c42e8dbc
  cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/verify_uniform_d9.py
9ca90959f284052bf669911c15e675892c1749b0bfed3cb4fd6462156e61b059
  cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/RESULT.json
a2533344de5f91d195d215e6f407d58266ee80b80e409da63c7513e8785dc44d
  cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/README.md
```

These match `FREEZE.sha256` and the raw-source pin in the charge.  The
producer checker `--check` rebuilds `RESULT.json` byte-for-byte and prints
`PASS_EXACT_FIELD_POINT_DIVISIBILITY`.  That replay is a custody check
only; it is not the proof.

I did not use the producer checker as a derivation source.  A separate
standard-library checker, using only `fractions.Fraction`, did the
following.

1. Rebuilt `F0..F14`, `G0..G21` from the pinned head
   `F0=A^4`, `F1=A^2`, `F2=(1+A^2 Z)/4`, `F3=(Z+A T)/8`, `G0=A^6` and the
   raw windows, then expanded
   `D_n = sum_{i+j=n} ((12-j) F_i' G_j + (i-8) F_i G_j')`
   as sparse polynomials in the 303 coefficient variables.  Rows `D0..D3`
   vanish identically.  In `D4..D9`, every `X`-degree, every monomial, and
   every sign matches the frozen generator list (201 coefficients, 10960
   terms).
2. Ran the fractional recurrence
   `n A^4 y_n = sum_{1<=i<=n} (((alpha+1)i-n) F_i y_{n-i})`
   and, independently, the oriented square-root cube `S^3` with
   `S_0=A^2`.  They agree at weights `0..9`.
3. Applied the same-row operator
   `L_n(R) = 4(12-n) A^3 A' R - 8 A^4 R'`
   to the polar parts, without importing the producer Laurent ring.
4. Evaluated producer mutations and additional hostile mutations by a
   three-way comparison: independent `D5G` recurrence, serialized JSON
   generators, and the claimed closed forms.

No CAS, floating point, interpolation, AWS, or `jc2-lean` was used.  No
canonical top-level file and no frozen packet file was edited.

The producer’s historical pins of `CHARACTERISTIC_CROSSCHECK.md` and the
two prior hostile audits still match the live bytes.  Those notes are
context, not proof.

## 2. Independent reconstruction of raw `D4..D9`

The frozen JSON identifies itself as the literal D5G system on `Q` with
303 variables and 513 generators in rows `D4..D22`.  Documentary `F1,F2,F3`
window slots exist in the window census but are not among the 303
variables: those weights are the pinned cascade, not free slots.  There is
no `G22` and no `D23`.

The `G6` window is degrees `0..18` and contains `A^3`.  The `G7` window
is `0..17` and contains `3A/4`.  The `G8` window is `0..16` and cannot
store `3/(32A)`.  The `G9` window is `0..15` and cannot store
`-3 W^2/(16 A^2)`.  These bounds are load-bearing for “raw `G` is
polynomial”.

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

Birth values `y_0 = A^{(12-m)/2}` were recomputed for all nine modes.
Support at weight `n` requires `n-m >= 0`.  At `n=8` and `n=9` this leaves
exactly `c4,c6,c8`.  In particular `c10` first contributes at weight 10,
and a raw `G10` slot is invisible to `D4..D9` (literal mutation: `G10=1`
leaves those rows zero).  Empty causal support is not permission to delete
`c10..c20` from the formalism.  The producer `RESULT.json` serializes all
nine modes, with `c14,c16,c18,c20` marked `forced_rational`.

## 4. Theorem T3: `D8` kills scalar `c6`

After `T=A V` and `F4-V/16-Z^2/64=A W`, both the fractional recurrence and
the square-root cube give polynomial `(F^{3/2})_7` and `(F^{3/2})_8`, with
the printed term lists.  The weight-eight continuation is

```text
g8 = (F^{3/2})_8 + c4 F4 + c6 (F^{3/4})_2 + c8 (F^{1/2})_0,
(F^{3/4})_2 = 3/(32 A) + 3 A Z / 16,
(F^{1/2})_0 = A^2.
```

The base coefficient, `c4 F4`, and `c8 A^2` are polynomial.  The polar
part of `(F^{3/4})_2` is `3/(32A)`, independent of `Z,V,W` and of every
later `F`-window.  Hence

```text
polar(g8) = 3 c6 / (32 A).
```

Same-row calculus: `L_8(3 c6/(32 A)) = (9/4) c6 A^2 A'` exactly, so

```text
D8_raw = -L_8(polar(g8)) = -(9/4) c6 A^2 A'
```

as an identity on the polar summand.  For any polynomial `P`,
`L_8(P) in (A^3)`, so the displayed congruence holds modulo `A^3`.  Because
`gcd(A,A')=1` in characteristic zero (`A'=4X^3`, Euclidean algorithm
returns `1`) and `c6` is a scalar, `D8=0` forces `c6=0`.

Cancellation search, all negative:

- `c4` and `c8` are polynomial at this weight; adding both to the `c6=1`
  mutation leaves `D8 = -(9/4) A^2 A'` exactly, with `D4..D7` still zero.
- Polynomial `G8` in `{1, A, A^2, X^3}` changes `D8` only by an `A^3`
  class; the `A^2` obstruction is untouched.
- `Z=1` with matching square-root `G` through weight 7 and holomorphic
  `3 A Z/16` stored in `G8` still gives `D8 = -(9/4) A^2 A'`.
- Pure `c4` and pure `c8` (the latter with polynomial `G9=c8/2` included)
  are kernels through `D9` on the exact square, so they cannot manufacture
  a counterterm to the `c6` pole.
- A fake non-constant mode `k6=A`, with polynomial
  `G6=A^4`, `G7=3 A^2/4`, `G8=3/32`, is **not** a kernel: `D6,D7,D8` are
  nonzero.  Its `D8` does lie in `(A^3)`, so the producer modulus would be
  too coarse if `c6` were allowed to be an `X`-polynomial.  The
  characteristic ODE treats `c6` as a scalar; MODE_AUDIT’s weight-6 kernel
  is one-dimensional, supported exactly on the degrees of `A^3`.  T3 is
  the scalar statement, and the fake mode is correctly excluded.

The producer mutation `G6=A^3`, `G7=3A/4`, remaining raw slots zero, has
`D4..D7=0` and

```text
D8 = -9 X^3 + 18 X^7 - 9 X^{11} = -(9/4) A^2 A'.
```

Live rescalings `c6=-1,2` reverse and double this residual.  JSON
generators and the independent recurrence agree through `D21`.

Coefficients: `9/4` and the `3` in `3 c6/(32A)` vanish in characteristic
3, and `32` is zero in characteristic 2.  Characteristic zero is
load-bearing and is in the stated scope.

## 5. Theorem T4: `D9` square defect after T3

Before T3 the weight-nine continuation is

```text
g9 = (F^{3/2})_9 + c4 F5 + c6 (F^{3/4})_3 + c8 (F^{1/2})_1,
(F^{3/4})_3 = -1/(128 A^3) + 3 Z/(64 A) + 3 A V / 32,
(F^{1/2})_1 = 1/2.
```

The full polar part, recomputed, is

```text
-c6/(128 A^3)
- 3 W^2 / (16 A^2)
+ 3 c6 Z / (64 A)
+ (3 F5 W / 4 - 3 V W Z / 256) / A.
```

The order-three `c6` term is the firewall: a direct `D9` argument that
silently sets `c6=0` is invalid.  A mixed raw mutation with `c6=W=1`
confirms this: `D8` is still the `c6` obstruction, while `D9` is
`-51/2 X^3 + 21 X^7`, not the square-defect polynomial.

After T3, `c4 F5` and `c8/2` are polynomial, and the remaining polar part
is exactly the printed `(3.1)`.  The order-two coefficient `-3 W^2/16`
cannot be cancelled by the order-one terms.  Applying `L_9` to `N/A^2`
gives `28 A A' N - 8 A^2 N'`, hence

```text
D9_raw = +(21/4) A A' W^2     (mod A^2).
```

`L_9` of every order-one polar monomial lands in `(A^2)`.  `L_9` of every
polynomial lands in `(A^3)`.  Polynomial `G9` in `{1,A,A^2}` therefore
cannot kill the `A^1` class.  Adding `c4` and `c8` to the `W=1` mutation
leaves `D4..D8=0` and `D9=(21/4) A A'` exactly.

For constant `W` the extra derivative term `-3 A^2 W W'` vanishes, so the
producer’s `W=1` closed form is an equality, not merely a congruence:

```text
D9 = -21 X^3 + 21 X^7 = (21/4) A A'.
```

`W=-1` repeats this; `W=2` multiplies it by 4, fixing both the sign and
the square power.  For non-constant `W=X` the exact raw row is

```text
D9 = (21/4) A A' X^2 - 3 A^2 X,
```

which is `{'1': -3, '5': -15, '9': 18}` and still congruent to
`(21/4) A A' X^2` modulo `A^2`.  The extra term cannot cancel the
obstruction.  This is a clarification of the modulus, not a defect: the
charged statement is the congruence.

Field-radical last step: `gcd(A,A')=1`, so `A | A' W^2` implies `A | W^2`.
On a field, `Q[X]/(A)` is a product of fields because `A` is squarefree,
and `W^2=0` there iff `W=0` there.  Direct remainder checks for several
`W` confirm `A | W^2` if and only if `A | W` in `Q[X]`.  Over a nonreduced
coefficient ring the same calculation only puts `W^2` in `(A)`.

## 6. Mutations and falsification search

Producer mutations, independently rebuilt from window slots and checked
three ways through `D21`:

| mutation | `D4..D7` | `D8` | `D9` |
|---|---|---|---|
| `c6=1` through `G7` | 0 | `-(9/4) A^2 A'` | (not used) |
| `c6=-1,2` | 0 | linear in `c6` | (not used) |
| `W=1` through `G8` | 0 | 0 | `+(21/4) A A'` |
| `W=-1` | 0 | 0 | same |
| `W=2` | 0 | 0 | four times |

Hostile replacements that failed to cancel either obstruction: polynomial
`G8` against `c6`; polynomial `G9` against `W`; `c4` and `c8` together
with `c6`; `c4` and `c8` together with `W`; `Z=1` against `c6`; mixed
`c6` and `W` (D8 still the mode obstruction; D9 not the square law);
`W=X` (congruence holds, `A` does not divide `X` or `X^2`); illegal
`G10=1` (invisible at these rows); fake `k6=A` (not a kernel).

No literal raw field point or local Laurent mutation was found that
falsifies T3 or T4 inside the stated hypotheses.

## 7. Scope

These are statements about characteristic-zero field points of one fixed
303-variable branch-P fixture, at rows `D8` and `D9`, after the reviewed
`D7` and leading-`D8` substitutions.  They are not:

- scheme-theoretic divisibility over nonreduced coefficient rings;
- emptiness of the endpoint, of cutoff 4/3/2, or of any later row;
- an unrestricted branch-P theorem, a Keller-pair theorem, or JC2;
- a licence to drop `c10..c20` from later weights;
- a claim that `D9` may be consumed before the full `D8` mode kill.

The coefficients `9/4` and `21/4` make characteristic zero essential.

## Hashes

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
ccf78403684ef7ee7e9f85336b4ccf86a01d679ba61b6327f4d2400ece16490e  xmodel/ggv-upper-endpoint-uniform-d9-fullmodes-sol-ultra-20260828.md
f4e40d3324a9dc9058b6ec80a01458468b3a90d0d3b4794841e76450c42e8dbc  cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/verify_uniform_d9.py
9ca90959f284052bf669911c15e675892c1749b0bfed3cb4fd6462156e61b059  cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/RESULT.json
1b6e101eb8c19ed5ba8ff6c3ede6e949da471f8b4b2689d0ce5f90fca09ba8b8  xmodel/ggv-upper-endpoint-uniform-d9-fullmodes-hostile-review-grok46-20260828-check.py
```

The SHA-256 of this review file is the digest of the on-disk bytes of

```text
xmodel/ggv-upper-endpoint-uniform-d9-fullmodes-hostile-review-grok46-20260828.md
```

computed after the final write, recorded immediately below.

<!-- self-hash -->
8b999c0862a56d8175d8f0eee43352d3d561341aea69fd968d2b3e68a9106309  report body above this delimiter
