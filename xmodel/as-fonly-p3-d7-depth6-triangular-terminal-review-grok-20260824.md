# Hostile different-model review — AS map-only `p=3,D=7` triangular terminal

| Field | Value |
|---|---|
| Claim under review | Frozen producer: the map-only cap-seven system is nonempty modulo `3^6=729`; the displayed triangular residue has no cap-seven lift modulo `3^7=2187`. This does **not** classify the full cap-seven locus |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking writeup remarks below; emptiness of `FONLY_(3,7)(D=7)`, a simultaneous `(A,B)` gauge cap, an all-depth tower, a characteristic-zero lift or no-lift theorem, a counterexample, and JC2 are correctly *not* claimed) |
| Evidence tier | independent expansion of `P,Q` over `Z`; exact integer Jacobian, not the modular derivative; clean-representative congruence modulo `2187`; denominator-free inversion and `H`-equivalence; affine carry identity on every used digit; rebuilt F3 RREF/nullspace **and** an independent exhaustive `3^7` search; first-variation linearization including `729^2`; mixed/Frobenius/shear/representative attacks; unmodified rerun of the four registered programs as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `1e60fcedc8626650c7c7544ad296c3624173415f` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T17:14:46Z – 2026-08-24T17:25:36Z |
| Python | host CPython 3.14.6 (hashes, sparse engine, rebuilt RREF, exhaustive digit search, registered replays); uv-pinned CPython 3.11.11 + SymPy `1.14.0` |
| Singular | 4.4.1 (registered `(integer)` replay; independent characteristic-0 computation of both quotients, then reduction modulo 3) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, freeze, and named payloads reread in full before any verdict:

- `xmodel/as-fonly-p3-d7-depth6-triangular-terminal-20260824.md` (SHA-256 `5325890a505489570a6e02409d64e026560d2635ddf989b865039eeb6ecddccb`)
- `cases/as_fonly_p3_d7_depth6_triangular_terminal_20260824/FREEZE.txt` (SHA-256 `b51a00062fa38765d3dd4199919b4e1a812fddbd8ae12cca9cc4fa2380b776bb`)
- `cases/as_fonly_p3_d7_depth6_triangular_terminal_20260824/MANIFEST.sha256` (SHA-256 `c722e0a6fef62a31d431b2b331f886bc4ab05726a75a9b5694fcc166bc99afce`)
- `cases/as_fonly_p3_d7_depth6_triangular_terminal_20260824/README.md` (SHA-256 `fff751fef07cef4eaa093b3dbcb27250a5db33c7e9ac4e889c3981a1448367a8`)
- `cases/as_fonly_p3_d7_depth6_triangular_terminal_20260824/compile_triangular_first_survivor.py` (SHA-256 `dcd2ea308ff31813cb55a88904ddbd375471a7cb92f6d7a2ffb370f1fee5acaa`)
- `cases/as_fonly_p3_d7_depth6_triangular_terminal_20260824/replay_triangular_terminal.py` (SHA-256 `17287308e709adc0579fdaf6853e947b4ec3de136433d5bcbbbc71da0aee4fdc`)
- `cases/as_fonly_p3_d7_depth6_triangular_terminal_20260824/replay_accepted_digit_trace.py` (SHA-256 `cd35cc79d927e04161c9a9adf0f973f6583677290c79884956259395601baf51`)
- `cases/as_fonly_p3_d7_depth6_triangular_terminal_20260824/audit_triangular_terminal.sing` (SHA-256 `86398ebcf209d1ba588c0e86ec280db7ee4ac7d7013f0a6bed859dfdc8b4a5c5`)

Canonical map-only orientation and the gauge-cap parents, consumed only to fix the special fibre `(x-x^3,y)` and to **refuse** promotion into `B_(p,n)(D,D)`:

- `xmodel/ideation-20260824T1633Z-as-owner.md` (SHA-256 `2e93ae2f1ee919bcb4b746993c9ea4333df3c78d1882422e948447c2e5faf68b`), map-only card only: `F_n=(P_n,Q_n)` Keller modulo `3^n` at a fixed total-degree cap, no gauge cap
- `xmodel/as109-bounded-polar-conductor-gate-20260824.md` (SHA-256 `2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b`)
- `xmodel/as109-bounded-polar-conductor-review-grok-20260824.md` (SHA-256 `bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa`), overall **CONFIRMED**, used only for `C_3=(x-x^3,y/D)` and the identity-branch special fibre
- `xmodel/as-gauge-growth-p3-depth6-cartier-d7-point-20260824.md` (SHA-256 `9bff27d0aed6294633c7e5726a7d1c0d7e0fb8a5629809790da783c62b41fea4`) and its review, used only as a *different category*: that kill is a gauge residue in `B_(3,5)`, not a map-only statement

The committed basis is exactly `1e60fcedc8626650c7c7544ad296c3624173415f`. Named producer artifacts remain uncommitted on top of that basis. No producer, case, canonical, ladder, notes, prompt, log, run, or erratum file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp/as_fonly_p3_d7_review/` and did not import `compile_triangular_first_survivor.py`, `replay_triangular_terminal.py`, `replay_accepted_digit_trace.py`, or `audit_triangular_terminal.sing`.

Tried hard, and failed, to equate the compact product `(1+6x^2+18x^4+27x^6)Q_y` with the literal integer Jacobian of the displayed `P`; to claim that the original residual is already `-x^{12}` (it is `x^6-x^{12}`); to cancel `x^{12}` by a mixed cap-seven digit, a Frobenius monomial, a target shear, or a different `729`-lift of the same residue; to treat the compiler’s stop at the first survivor as exhaustion of the terminal locus; to sneak an `(A,B)` cap into the system; to realise a cap-seven lift modulo `2187`; and to promote the pointwise kill to emptiness of `FONLY_(3,7)(D=7)`, a compatible tower, a polynomial/Tate lift, a no-lift theorem, a counterexample, or JC2. The only tested cancellation of `x^{12}` uses `U=x^{13}`, which is excluded by every total-degree cap at most twelve.

---

## Promotion

**Accept `THE MAP-ONLY CAP-SEVEN SYSTEM IS NONEMPTY MODULO 3^6, AND THE DISPLAYED TRIANGULAR RESIDUE HAS NO CAP-SEVEN LIFT MODULO 3^7`.**

On the map-only category `FONLY_(3,n)(D=7)` — polynomials `P,Q` over `Z/3^n Z` of total degree at most seven, special fibre `(x-x^3,y)` over `F_3`, `det J(P,Q)=1`, and **no** cap on a canonical gauge `(A,B)`:

- The integer maps
  `P=x+2x^3+441x^5+108x^7`, `Q=y-6x^2 y+18x^4 y-27x^6 y`
  have total degree seven, reduce to `(x-x^3,y)` modulo 3, and satisfy `det J(P,Q)=1 (mod 729)`. The complete integer determinant is recorded below; it is not the compact modular product.
- Replacing the `x^7` coefficient by the congruent value `1566=108+2·729` does not change the class in `(Z/729Z)[x,y]`. For that lift one has the genuine congruence `det J(P_tilde,Q)=1-729 x^{12} (mod 2187)`, which is **not** an identity over `Z`. The change of representative alters the first residual by the divergence of `U=2x^7`.
- The displayed point is triangular: `P=P(x)`, `Q=y T(x)`. The source polynomial `a` with `P_x=1+3a` satisfies the only derivative-provenance conditions `[x^2]a=-1` and `[x^5]a=0 (mod 3)`, inverts denominator-free through modulus 729, and meets `deg T<=6` by high vanishing of `H(a)` modulo 81. Integration to `P` uses only units `5^{-1}` and `7^{-1}` modulo 729 together with the licensed multiplier-three stratum at `x^3`.
- Every cap-seven next digit of this residue is of the form `P_tilde+729 U`, `Q+729 V` with `deg U,V<=7`. The first residual is `-x^{12}+U_x+V_y (mod 3)`. No divergence of total degree at most seven has an `x^{12}` term, so the fibre in `FONLY_(3,7)(D=7)` is empty.

**Do not promote this to:** emptiness of `FONLY_(3,7)(D=7)` or of the full depth-six D7 locus; a simultaneous `(A,B)` gauge-cap theorem; uniqueness of the displayed triangular survivor; an all-depth compatible tower; a polynomial, Tate-algebra, or inverse-limit lift of `(x-x^3,y)`; a characteristic-zero no-lift theorem; a counterexample to JC; or any JC2 inference. It does not falsify the characteristic-zero expectation that `D=7` is a negative control. It falsifies only the stronger finite claim that depth six would already certify emptiness.

**Smallest honest successor.** An exhaustive accepted-digit compilation of **every** depth-six cap-seven residue — all 27 triangular base components through the terminal digit, and the non-triangular map-only components — is the smallest exact search that could decide `FONLY_(3,7)(D=7)`. If some residue has vanishing cap-boundary class, the same test at later depths is the next discriminator. Neither search is a theorem of this pointwise obstruction. Do not spend further work trying to lift *this* residue at cap seven.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a polynomial lift of `(x-x^3,y)`, identifies the polar divisor with `A_infinity`, runs `p=109`, empties any depth-seven bounded system, or produces a compatible tower. Producer strings `PASS-FONLY-P3-D7-N6-SURVIVOR-N7-TERMINAL`, `PASS-TRIANGULAR-SURVIVOR`, `PASS-ACCEPTED-DIGIT-TRACE`, and `PASS-SINGULAR-FONLY-P3-D7-N6-TRIANGULAR` were not used as evidence; the integer Jacobian, the two residuals, the inverse and `H` identities, the affine carry, the RREF counts, and the first-variation formula were re-derived. The polar parent is used only for the special fibre of `C_3` and to keep the map-only system distinct from the reviewed equal-cap gauge systems `B_(p,n)(D,D)`. The depth-six Cartier kill of a frozen *gauge* residue is a different category and does not enter the map-only verdict. Independent reconstruction, not the producer scripts, is the evidence for every numbered claim.

---

## Scope (not enlarged)

One prime `p=3`; one total-degree cap seven; the single triangular residue class modulo `729` displayed above; the two congruences `det J=1` modulo `729` and the empty cap-seven fibre modulo `2187`. The kill is pointwise in that residue class. No rectangular support, no enumerator, no AWS, no gauge cap, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | The displayed `P,Q` have total degree seven, special fibre `(x-x^3,y)` over `F_3`, and `det J=1 (mod 729)`. The literal integer determinant is `1+2187 x^4-12393 x^6+34992 x^8-45927 x^{10}-20412 x^{12}`. Its quotient by 729 reduces to `x^6-x^{12}` modulo 3; the `x^6` term is present | **CONFIRMED** | a reduced monomial of total degree `>7`; special fibre not `(x-x^3,y)`; a coefficient of `det J-1` not divisible by 729; quotient modulo 3 missing `x^6` or missing `x^{12}` |
| 2 | `1566≡108 (mod 729)` is a legitimate integer representative of the same depth-six class; `det J(P_tilde,Q)=1-729 x^{12} (mod 2187)` and not over `Z`; the representative change alters the residual by a divergence | **CONFIRMED** | `1566≢108 (mod 729)`; a remainder of `J_tilde-(1-729 x^{12})` not divisible by 2187; a false claim that the original integer `P` already has residual `-x^{12}` |
| 3 | For `P_x=1+3a`, `Q=yT+S`, the shear `S` is determinant-invisible; the only derivative-provenance restrictions are `[x^2]a=-1` and `[x^5]a=0 (mod 3)`; `T=sum_{k=0}^5 (-3a)^k (mod 729)`; `deg T<=6` iff high `H(a)` vanishes modulo 81 | **CONFIRMED** | a nonzero contribution of `S` to `det J`; an extra provenance restriction on a unit-multiplier exponent; a high term of `T` not accounted for by `9H`; failure of the geometric series at modulus 729 |
| 4 | There are 27 base forms; the carry `H(a+3^r δ)/3^r ≡ H(a)/3^r + 2 a_0 δ (mod 3)` holds for `r=1,2,3`; counts `27 → 3645 → 531441` with 1458 second-stage inconsistencies; first terminal survivor after 486 inconsistencies is `a=2x^2+6x^4+9x^6 (mod 81)`; stopping there is existence, not exhaustion | **CONFIRMED** | a 28th legal base; failure of the affine identity at a used `r`; a different count; first survivor not the displayed `a`; a uniqueness claim for the terminal locus |
| 5 | This `a` inverts to `T=1-6x^2+18x^4-27x^6 (mod 729)`; integration to the displayed `P` uses only `5^{-1}`, `7^{-1}`, and the licensed `x^3` stratum; the system is map-only | **CONFIRMED** | `(1+3a)T ≢ 1 (mod 729)`; a division by 3 at a non-stratum exponent; a hidden cap on `(A,B)` |
| 6 | Every cap-seven lift of this residue has first residual `-x^{12}+U_x+V_y (mod 3)` for the clean representative. Derivatives of degree `<=7` have degree `<=6` and cannot cancel `x^{12}`. Mixed terms, Frobenius, shears, and other depth-six representatives do not evade it | **CONFIRMED** | a leftover cross term not divisible by 3; `729^2 ≢ 0 (mod 2187)`; a cap-seven pair with residual `0`; a representative change moving the `x^{12}` class |
| 7 | The supported statement is exactly one D7 map-only point modulo `3^6` whose residue has no D7 lift modulo `3^7`. Full-locus emptiness, gauge-cap, all-depth, characteristic-zero, counterexample, and JC2 inferences are out of scope. The smallest next exact obligation is exhaustive compilation of every remaining D7 residue at the depth-six to depth-seven step | **CONFIRMED** | `FONLY_(3,7)(D=7)=∅` asserted; a simultaneous gauge-cap theorem; the successor sold as proved empty |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Replay and hashes

Frozen hashes, recomputed on the charged tree, match the launch prompt, the manifest, and the freeze record:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as-fonly-p3-d7-depth6-triangular-terminal-20260824.md` | `5325890a505489570a6e02409d64e026560d2635ddf989b865039eeb6ecddccb` | prompt, freeze `report_sha256` |
| `cases/.../FREEZE.txt` | `b51a00062fa38765d3dd4199919b4e1a812fddbd8ae12cca9cc4fa2380b776bb` | prompt |
| `cases/.../MANIFEST.sha256` | `c722e0a6fef62a31d431b2b331f886bc4ab05726a75a9b5694fcc166bc99afce` | prompt, freeze `manifest_sha256` |
| `cases/.../README.md` | `fff751fef07cef4eaa093b3dbcb27250a5db33c7e9ac4e889c3981a1448367a8` | prompt, `MANIFEST` |
| `cases/.../compile_triangular_first_survivor.py` | `dcd2ea308ff31813cb55a88904ddbd375471a7cb92f6d7a2ffb370f1fee5acaa` | prompt, freeze, `MANIFEST` |
| `cases/.../replay_triangular_terminal.py` | `17287308e709adc0579fdaf6853e947b4ec3de136433d5bcbbbc71da0aee4fdc` | prompt, freeze, `MANIFEST` |
| `cases/.../replay_accepted_digit_trace.py` | `cd35cc79d927e04161c9a9adf0f973f6583677290c79884956259395601baf51` | prompt, `MANIFEST` (absent from freeze) |
| `cases/.../audit_triangular_terminal.sing` | `86398ebcf209d1ba588c0e86ec280db7ee4ac7d7013f0a6bed859dfdc8b4a5c5` | prompt, freeze, `MANIFEST` |
| polar-conductor gate | `2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b` | parent |
| polar-conductor review | `bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa` | parent |
| gauge Cartier producer | `9bff27d0aed6294633c7e5726a7d1c0d7e0fb8a5629809790da783c62b41fea4` | different category |

Every member hash inside `MANIFEST.sha256` was recomputed from the case directory and matched. The freeze record is not a second copy of the manifest; it names the manifest digest and four of the five payload digests. The accepted-digit replay is in the manifest and the launch prompt but is omitted from the freeze file. That is a freeze bookkeeping omission, not a mathematical gap.

Registered commands, rerun unmodified from the case directory (`Singular -q` was fed an extra `exit;` without editing the payload):

```text
python3 compile_triangular_first_survivor.py
python3 replay_triangular_terminal.py
python3 replay_accepted_digit_trace.py
Singular -q audit_triangular_terminal.sing
shasum -a 256 -c MANIFEST.sha256
```

All four engines exited 0 and the manifest check passed. Live compiler output:

```text
stage 1 {..., digit_1_output: 3645, digit_1_inconsistent: 0, digit_1_rank_hist: {2: 9, 3: 18}}
stage 2 {..., digit_2_output: 531441, digit_2_inconsistent: 1458, digit_2_rank_hist: {2: 2187, 3: 1458}}
stage 3 {..., digit_3_output: 1, digit_3_inconsistent: 486, digit_3_rank_hist: {2: 487}}
enumeration_sha256 1d7ab40f50bfa01e7189e4022742984c12b8fba151bae83f8e332dbc0cdbf35e
first_a_mod81 [0, 0, 2, 0, 6, 0, 9]
```

Those Booleans and the pasted Singular identity `J-expected=0` were discarded as evidence for Claims 1–7. (The registered Singular script pastes the six-term integer determinant and checks it; that is why it is regression-only. The independent characteristic-0 computation below *divides* `det J-1` by 729 over `Q`.)

Independent engines, written for this review and not imported from any registered program (scratch SHA-256, outside the repository):

- integer sparse engine + rebuilt F3 RREF + exhaustive `3^7` search, host CPython 3.14.6: `3267137ce6586d70f3461d4732f20aedb4d1771283bdd8a6d3bca913f86a26e6`
- SymPy `1.14.0` over `ZZ[x]`: `c2c1d0a8cf39b1a84feeedc871d0cf0c9eeac00ab7c0e27ff36a516953555357`
- second Singular script, characteristic 0 then reduction modulo 3: `46f76d65ac1159d270bd32f26515e31056b5ec7276a1b78a7d74f0e6deac1972`

The three non-pasting engines produced the same integral Jacobian, the same original residual `x^6-x^{12}`, and the same clean congruence modulo 2187.

---

## Independent recomputation

### 1. Literal point, complete integer determinant, residual `x^6-x^{12}` — CONFIRMED

Write `P=x+2x^3+441x^5+108x^7` and `Q=y T(x)` with `T=1-6x^2+18x^4-27x^6`. Both supports are total-degree seven. Coefficientwise reduction modulo 3 uses `2≡-1`, `441≡0`, `108≡0`, and `6,18,27≡0`, so

```text
P ≡ x-x^3,     Q ≡ y     (mod 3).
```

The map is triangular, so `P_y=0` and `det J(P,Q)=P_x Q_y`. The *literal* integer derivatives are

```text
P_x = 1 + 6x^2 + 2205 x^4 + 756 x^6,
Q_y = 1 - 6x^2 + 18x^4 - 27x^6.
```

The compact polynomial `short=1+6x^2+18x^4+27x^6` is the coefficientwise reduction of `P_x` modulo 729, not `P_x` itself: `2205=18+2187` and `756=27+729`. Over `Z` one still has the exact product identity

```text
short · Q_y = 1 - 729 x^{12}.
```

(Let `t=3x^2`. Then `short=(1+t)(1+t+t^2)` and `Q_y=(1-t)(1-t+t^2)`, so the product is `(1-t^2)(1+t^2+t^4)=1-t^6=1-729 x^{12}`.) Substituting the literal derivative

```text
P_x = short + 2187 x^4 + 729 x^6
```

gives the complete integer Jacobian

```text
det J(P,Q)
  = 1 - 729 x^{12} + 729(3x^4 + x^6) Q_y
  = 1 + 2187 x^4 - 12393 x^6 + 34992 x^8 - 45927 x^{10} - 20412 x^{12}.
```

Every coefficient of `det J-1` is divisible by 729, and

```text
(det J-1)/729 = 3x^4 - 17 x^6 + 48 x^8 - 63 x^{10} - 28 x^{12}.
```

Reducing modulo 3 uses `-17≡1`, `-28≡2≡-1`, and `3,48,63≡0`, hence

```text
(det J-1)/729 ≡ x^6 - x^{12}     (mod 3).
```

The `x^6` term is present. It is a cap-seven divergence class (`U=x^7` has `U_x=7x^6≡x^6 (mod 3)`) and must not be dropped from the original representative. It is *not* a cap-boundary class. Three engines (sparse `Z`, SymPy `ZZ[x]`, Singular over `Q` then `F_3`) return this same six-term polynomial and this same residual. The compact product `1-729 x^{12}` is therefore **not** the literal determinant of the displayed integer `P`. The producer flags that distinction; the claim `det J=1 (mod 729)` survives.

### 2. Clean representative and representative-invariance — CONFIRMED

The coefficient `1566=108+2·729` is congruent to `108` modulo 729, so `P_tilde=x+2x^3+441x^5+1566 x^7` is another integer lift of the *same* class in `(Z/729Z)[x,y]`. Now `1566·7=10962=27+5·2187`, and `2205=18+2187`, so

```text
P_tilde_x = short + 2187(x^4 + 5 x^6) ≡ short     (mod 2187).
```

Therefore

```text
det J(P_tilde,Q) = 1-729 x^{12} + 2187(x^4+5x^6)Q_y
                 ≡ 1-729 x^{12}                 (mod 2187).
```

The error over `Z` is not zero. Its quotient by 2187 is the explicit polynomial

```text
(x^4+5x^6)Q_y = x^4 - x^6 - 12 x^8 + 63 x^{10} - 135 x^{12},
```

matching the registered Singular printout of `clean_lift_error_over_2187`. Any claim that `det J(P_tilde,Q)=1-729 x^{12}` *over the integers* is false. The congruence modulo 2187 is true.

The change of representative is `P_tilde-P=729·(2x^7)`. The first residual therefore shifts by `U_x=14 x^6≡2x^6 (mod 3)`:

```text
x^6 - x^{12} + 2x^6 ≡ -x^{12}     (mod 3),
```

which is the clean residual. This is exactly a divergence, so the cap-boundary class of `x^{12}` is independent of the choice of integer lift of the depth-six coordinates by multiples of 729. Using `P_tilde` for the obstruction is legitimate; claiming the original integer `P` already has residual `-x^{12}` is not.

### 3. Triangular equivalence, provenance, inversion, `H` — CONFIRMED

Write `P_x=1+3a(x)` and `Q=y T(x)+S(x)` with `deg P<=7` and `deg T<=6`. Then `P_y=0` and

```text
det J = P_x T,
```

independent of the target shear `S`. Setting `S=0` is a representative choice, not a determinant constraint; `deg Q=max(deg S, 1+deg T)` still forces `deg T<=6` separately.

Source provenance: `P=x-x^3+3U` gives `a=U'-x^2`. The coefficient of `x^m` in `U'` is `(m+1)U_{m+1}`. For `deg a<=6` the exponents with `3∣(m+1)` are only `m=2` and `m=5`, and they give exactly

```text
[x^2]a ≡ -1,     [x^5]a ≡ 0     (mod 3).
```

The multipliers at `m=0,1,3,4,6` are `1,2,4,5,7`, all units modulo 729 (inverses `1,365,547,146,625`). There are no further derivative-provenance restrictions at modulus 243 or 729: the two displayed conditions remain the only ones, and they are conditions modulo 3, not modulo 243. (The producer’s phrase “restrictions on `a` modulo 243” is clumsy and is read as “the only restrictions that exist at that depth”, which is correct.)

Denominator-free inversion modulo `729=3^6` is the truncated geometric series, exact because `(-3)^6=729`:

```text
T = (1+3a)^{-1} = 1-3a+9a^2-27a^3+81a^4-243a^5     (mod 729).
```

Grouping `T=1-3a+9H(a)` with `H(a)=a^2-3a^3+9a^4-27a^5` is an identity of polynomials. Since `deg a<=6`, the polynomial `1-3a` has degree at most six, so `deg T>6` in `(Z/729Z)[x]` if and only if a degree-`>6` coefficient of `9H` is nonzero modulo 729, if and only if the corresponding coefficient of `H` is nonzero modulo 81. There is no `a^6` term: it would carry a factor 729. Working with `H` modulo 81 is the exact cap condition, and `H (mod 81)` depends only on `a (mod 81)`.

Modulo 3, `H(a)≡a^2`. High vanishing plus the fact that `F_3[x]` is a domain forces `deg a_0<=3`. Together with `[x^2]a_0=-1` this is exactly the 27-dimensional affine space

```text
a_0 = c_0 + c_1 x - x^2 + c_3 x^3,     (c_0,c_1,c_3)∈F_3^3.
```

The condition `[x^5]a=0` is then automatic. Direct evaluation of `H(a_0)` confirms that all 27 bases already satisfy the high condition modulo 3.

### 4. Accepted-digit recursion, counts, existence versus exhaustion — CONFIRMED

For `λ=3^r` with `r>=1` the binomial expansion of `H(a+λ δ)` has linear term

```text
L = (2a - 9a^2 + 36 a^3 - 135 a^4)δ ≡ 2 a_0 δ     (mod 3)
```

and every quadratic-or-higher term carries a factor `λ`. Hence in every degree, including every high degree actually used,

```text
H(a+3^r δ)/3^r ≡ H(a)/3^r + 2 a_0 δ     (mod 3),     r=1,2,3.
```

This was checked on all 27 bases, all seven coordinate deltas, and a mixed delta, including after a generic lift of `a` by a multiple of 3. Because `deg a_0<=3` and `deg δ<=6`, the linear map `δ ↦ 2 a_0 δ` can move only degrees 7, 8, and 9. Degrees `>=10` of the right-hand side are extra consistency conditions, not digit variables.

Closed-form rank of the `3×3` on `(δ_4,δ_5,δ_6)`: rank 3 if `c_3≠0` (18 bases), rank 2 if `c_3=0` (9 bases). An independent exhaustive search of all `3^7` digits, not using the producer RREF, gives

```text
27 bases, 0 inconsistencies  →  3645   =  9·3^5 + 18·3^4,
3645 inputs, 1458 inconsistencies  →  531441 = 2187·3^5.
```

The 1458 second-stage inconsistencies are precisely the 1458 rank-3 parents. Their stage-one digits already produced `H`-mass in degrees `>=10` (from the quadratic `δ^2` of the previous carry), which the next linear map cannot cancel. Every one of the 2187 rank-2 parents is consistent, each with a 5-dimensional kernel, and `2187·243=531441`. A rebuilt F3 RREF with free variables enumerated in the same lexicographic order reproduces the producer trace, including

```text
enumeration_sha256
  = 1d7ab40f50bfa01e7189e4022742984c12b8fba151bae83f8e332dbc0cdbf35e,
first survivor after 486 inconsistencies:
  a = 2x^2 + 6x^4 + 9x^6     (mod 81).
```

That first survivor lies on the first base `(c_0,c_1,c_3)=(0,0,0)`, with stage-one digit `2 x^4`, stage-two digit `x^6`, and stage-three particular equal to zero. The parent already satisfies `H(a)` high `≡0 (mod 81)`, so the terminal particular is the zero digit. The kernel at this parent has dimension 5, hence **243** affine solutions in this component alone. The compiler retains only the RREF particular and stops. The counts `27 → 3645 → 531441` certify the *route* to a point; they do not enumerate the terminal locus. The producer’s language (“existence search, not an exhaustion of all survivors”) is exactly the licensed claim. A uniqueness or complete-locus reading of `digit_3_output: 1` would be false, and is not made.

### 5. Integration and source honesty; no hidden gauge cap — CONFIRMED

Substituting `a=2x^2+6x^4+9x^6` into the finite inverse yields

```text
T ≡ 1 - 6x^2 + 18x^4 - 27x^6     (mod 729),
```

i.e. coefficients `[1,0,723,0,18,0,702]` with `723≡-6` and `702≡-27`. The integer identity `(1+3a)T=1-729 x^{12}` holds, so the product is `1` in `(Z/729Z)[x]`. Integrating `P_x=1+6x^2+18x^4+27x^6` coefficientwise modulo 729:

```text
1·P_1 = 1,
3·P_3 = 6  ⇒  P_3 = 2          (licensed multiplier-three stratum; 3·2=6, not a division by three in Z/729),
5·P_5 ≡ 18  ⇒  P_5 = 441,      5^{-1}≡146,   18·146=2628≡441 (mod 729),
7·P_7 ≡ 27  ⇒  P_7 = 108,      7^{-1}≡625,   27·625=16875≡108 (mod 729),
```

and the odd-looking even exponents are zero. These are the displayed coefficients of `P`. The kernel of integration at the multiplier-three stratum is `243 Z`: `P_3 ∈ {2,245,488}` all satisfy `3 P_3 ≡6 (mod 729)`. The displayed choice `P_3=2` is one licensed lift, corresponding to setting the unused `81`-digit of `a` to zero. Other integrations give other depth-six maps with the same `P_x`; they are different residues modulo 729, each still carrying the `x^{12}` class after a divergence (Claim 6). None of this imposes a cap on a gauge `(A,B)`. The equations used are `det J(P,Q)=1`, the special fibre, and `deg(P,Q)<=7`. That is the map-only system `FONLY_(3,6)(D=7)`.

### 6. Terminality at depth seven — CONFIRMED

Every cap-seven lift of the displayed depth-six class is

```text
P_new = P_tilde + 729 U,     Q_new = Q + 729 V,     deg U,V <= 7.
```

The complete expansion is `J(P+λU,Q+λV)=J+λ({P,V}+{U,Q})+λ^2 J(U,V)` with `λ=729`. The quadratic term vanishes modulo 2187 because `729^2=243·2187`. Reducing the linear term modulo 3 uses only the special fibre `P_x≡1`, `P_y≡0`, `Q_x≡0`, `Q_y≡1`, and yields

```text
(det J(P_new,Q_new)-1)/729 ≡ -x^{12} + U_x + V_y     (mod 3)
```

for the clean representative. (For the original integer `P` the same identity holds with `x^6-x^{12}` on the right-hand side; the extra `x^6` is then cancelled by `U=x^7` and the `x^{12}` remains.)

A polynomial of total degree at most seven has derivatives of total degree at most six. The monomial `x^{12}` does not lie in that support. Equivalently, the unique monomial primitives of `x^{12}` under `∂_x` and `∂_y` are `x^{13}` and `x^{12} y`, both of degree 13. Direct exhaustion of the 36 monomials of total degree `<=7`, as `U` or as `V`, never produces an `x^{12}` coefficient in the divergence. Further attacks, all of which leave the class `-x^{12}` untouched:

- mixed terms `U=x^i y^j` with `i+j<=7` (including `x^4 y^3`, `x^2 y^5`, `y^7`);
- Frobenius-zero derivatives `x^3`, `x^6`, `y^3`, `x^3 y^3`, `x^3 y^4` (these shrink the image of divergence, they do not enlarge it);
- target shears `V=S(x)` of degree `<=7` (`V_y=0`);
- the original representative in place of `P_tilde` (residual `x^6-x^{12}`; `x^6` dies, `x^{12}` does not);
- an explicit mixed pair `U=x^5 y^2+2 x^3 y+x^7`, `V=y^7+x^4 y^2+2 x^6 y`, for which the computed residual equals `-x^{12}+U_x+V_y` in `F_3`.

The one successful cancellation in tests is `U=x^{13}`, which has `U_x=13 x^{12}≡x^{12} (mod 3)` and is excluded by the cap. Cap seven is load-bearing; the same obstruction in fact kills every lift of total degree at most twelve of this residue. That stronger statement is not needed, and is not promoted.

### 7. Scope and the smallest next exact obligation — CONFIRMED

The identities above prove

```text
FONLY_(3,6)(D=7)  is nonempty
```

and that the displayed residue class in the fibre of reduction `FONLY_(3,7)(D=7) → FONLY_(3,6)(D=7)` is empty. They do not prove

```text
FONLY_(3,7)(D=7)  is empty.
```

Another depth-six residue — another triangular component among the 27 bases, another kernel vector at a surviving affine stratum, or a non-triangular map with `P_y≠0` — may have vanishing cap-boundary class. The compiler’s 243-dimensional kernel at the displayed parent already exhibits further *unlisted* triangular survivors modulo 81, each of which still has to be tested at the next obstruction and none of which has been shown to die or to live. The result is not a simultaneous `(A,B)` gauge-cap statement (the polar/wild parents remain in their reviewed `B_(p,n)` category), not an all-depth tower, not a characteristic-zero lift or no-lift theorem, not a counterexample, and not evidence for or against JC2.

The smallest next exact obligation for a full D7 decision is an exhaustive accepted-digit compilation of every remaining depth-six cap-seven residue through the depth-seven obstruction: all 27 triangular bases and all surviving affine carry strata, together with the non-triangular map-only components. If that compilation returns empty, `FONLY_(3,7)(D=7)=∅` becomes a theorem. If some residue has zero cap-boundary class, the same test at depth eight or later is the next discriminator. Neither outcome is licensed by the displayed point.

---

## Non-blocking remarks

1. Equation number `(2)` is used twice in the producer report, once for the clean congruence and once for the provenance restrictions. The identities are distinct and both correct.
2. The xmodel prose never prints the six-term integer determinant or the original residual `x^6-x^{12}`. Both live in the payloads, and the prose explicitly warns against mistaking the compact product for the literal Jacobian. The clean representative is then used for the obstruction, which is the legitimate move (Claim 2). This is a writeup compression, not a silent erasure of the cap-boundary class.
3. The freeze file omits the accepted-digit replay hash. The file is in the manifest and matches the launch prompt.
4. “Lexicographically canonical particular” and “first canonical surviving path” refer to RREF particular solutions with free variables set to zero, in the compiler’s enumeration order. They are not uniqueness statements; the producer separately refuses exhaustion.
5. Integration at exponent three determines `P_3` only modulo 243. The displayed coefficient 2 is one licensed choice. Other choices are different depth-six residues, still terminal at cap seven by the same `x^{12}` class.

None of these remarks changes a numbered verdict.

---

## End quarantine

This review confirms a pointwise map-only statement at one prime, one cap, and one triangular residue. It does not empty `FONLY_(3,7)(D=7)`, does not cap a gauge, does not produce a tower or a polynomial, and does not speak to JC2. Independent reconstruction is the evidence; registered `PASS-*` strings are not.
