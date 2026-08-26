# Hostile text-only review — corrected control-2 A

| Field | Value |
|---|---|
| Claim under review | Direct-`sat` encoding of the reviewed expanded control-2 Rees polynomials, as an independent contraction/order check of the frozen 35-generator special fibre, not a second derivation of the eight charged equations |
| Overall verdict | **CORRECTED_A_CONFIRMED**. The factored-A renderer is invalid at `E8`. The corrected compiler hash-pins reviewed B and extracts `E1,...,E8,LT` byte-for-byte. Both registered AWS executions mutually reduce to the pinned 35-generator B fibre and reprint the monomial/torus certificate |
| Smallest failing identity | none in the frozen corrected-A sources or in either AWS stream |
| Smallest missing hypothesis for a stronger theorem | an independent re-derivation of the eight charged equations (explicitly not supplied); moving-axis / `q2` / other-support / other-weight / fan / D1 / JC2 coverage (explicitly firewalled) |
| Evidence tier | SHA-256 of the freeze chain and already-emitted AWS files; `cmp`/`diff` of extracted polynomial bodies and special-fibre generators; inspection of the identity-control stdout, the bad factored `poly E8`, the corrected compiler, both compiled sources, and the two prior B reviews. No local Python, Singular, Sage, msolve, Lean, Gfan, or other substantive symbolic computation |
| Reviewer / model | Grok 4.6 (xAI). Text-only tropical / commutative-algebra / CAS-custody referee |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `4fe628a133ae62e16b1bec5e4ed6fcee420dd880` |
| Host | Darwin. Corrected compiler, identity compiler, v2 compiler, certificate compiler, and Singular were not run |

No local substantive computation was run. Hashes were checked with `shasum -a 256`. File identity was checked with `cmp` and `diff`. Git identity was read with `git rev-parse`. AWS streams were read as already-emitted text.

Frozen hashes charged in the prompt, recomputed and matched:

```text
49c745ae0e1b48b80a5d2b017e0311fe2fbb3ddc0252c0da0b5b24ac23bfb1d6  RESULT_FREEZE.sha256
d5317aacf229d85b7b550c40e85d2b7294cae99ba0dedf2e56c2064d4d9ec088  expected_B_certificate.stdout
c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b  base_B.sing
c9eb14ffd7a7ab786dbec953bfa3f276b56e84f2eabbfc923f99c92bea3db07a  aws_box03_LPDP/singular.stdout
96bed25e5816183bb279c8f7f1ef08beb8966767ac913db9c748250215481b1b  aws_r6d_DP/singular.stdout
```

Every path listed in `RESULT_FREEZE.sha256` recomputed and matched, including `PREREGISTRATION.md` `2ef68237…`, `AWS_REGISTRATION.md` `1ae2373f…`, `PRESOLVE_CUSTODY.md` `26e6fc47…`, `SOURCE_CLOSURE.sha256` `85b3369e…`, compiler `8715ae9a…`, worker `b685812f…`, `RESULT.md` `fe96e656…`, `IMPACT_MATRIX.md` `a3c2881a…`, Box03 `result.sha256` `4a28ffe2…`, and r6d `result.sha256` `d074ef70…`. Nested AWS `result.sha256` entries all matched, including empty compiler/CAS stderr `e3b0c442…`, both rc files `9a271f2a…` (`"0\n"`), Box03 LPDP input `0e92f2d1…`, and r6d DP input `a1555587…`. Identity-control stdout matched `7baf7e60…`. Certificate stdout and v2/certificate/identity `base_B.sing` are the same `c905f1b5…` bytes. A-fast and identity `base_A.sing` are the same `2b416cb8…` bytes.

Read in full before the verdict: every file at the corrected-A package root; every artifact under `aws_box03_LPDP/` and `aws_r6d_DP/`; the identity, v2, certificate, and A-fast packages; v1 `SOFTWARE_CONTROL.md`; and the already written v2 source review and B certificate review.

---

## Promotion

**Accept `THE FACTORED CONTROL-2 A RENDERER IS INVALID AT E8. THE CORRECTED AWS COMPILER DOES NOT HAND-REPAIR THAT ROW: IT HASH-PINS REVIEWED EXPANDED B AT c905f1b5… AND EXTRACTS E1,...,E8,LT BYTE-FOR-BYTE. DIRECT sat(I,<s>) FOLLOWED BY s=0, IN BOTH (lp(1),dp(8)) AND GLOBAL dp, COMPUTES THE SAME SPECIAL-FIBRE IDEAL AS THE REVIEWED INVERSE-VARIABLE B CERTIFICATE. THAT IDEAL CONTAINS la^20 AND THE EIGHT-FACTOR TORUS PRODUCT, HAS TORUS SATURATION EXPONENT ONE, AND LOCALIZES TO (1). THEREFORE NO ARC WITH THE EXACT FIXED AXIS a=1, h=q2=k=nu=0, mu=2/3, SUPPORT AND WEIGHT (4,1,1,22,22,30,30,30), AND ALL EIGHT DISPLAYED COORDINATES NONZERO HAS A LEADING COEFFICIENT IN THAT TORUS. THE TWO A RUNS ARE SEPARATE AWS EXECUTIONS OF ONE COMPILER/SOURCE STRATEGY, NOT INDEPENDENT DERIVATIONS OF THE CHARGED EQUATIONS. THE B-ONLY THEOREM AND ITS FOCUSED CERTIFICATE REVIEW REMAIN VALID.`**

Do not promote this to: a second independent derivation of the eight charged equations; a repaired factored renderer; emptiness of coordinate-hyperplane loci; moving axis; nonzero `q2`; moving loads; another support or weight; whole-cone/fan coverage; D1; or JC2.

---

## Charge 1 — E8 correction and provenance

**CONFIRMED. Byte-extraction from pinned B is the cleanest sound correction of the charged defect.**

The frozen identity control
`max12_912_order3_d1_double_root_control2_rees_source_identity_20260826T012642Z_r6d`
compared factored A SHA `2b416cb8…` with expanded B SHA `c905f1b5…` as exact polynomials. Its Singular stdout (SHA `7baf7e60…`) is

```text
PASS_DP_E1
PASS_DP_E2
PASS_DP_E3
PASS_DP_E4
PASS_DP_E5
PASS_DP_E6
PASS_DP_E7
FAIL_DP_E8
-25134148616192/43046721
```

Compiler rc 0, Singular rc 0, empty compiler/CAS stderr. The worker then wrote `FAILED=SOLVER_FAILURE` because the wrapper fail-closes on any `FAIL_` line and on a missing identity PASS. That is the intended negative-control contract, not a crashed computation. Because the first `dp` difference is already a nonzero constant, the LPDP block was not reached.

The bad emitted polynomial is line 12 of the frozen factored A source (`poly E8=…`), pinned as `base_A.sing` in both the identity package and A-fast. It is produced by `source_a` at `compile_control2_rees_v2.py:297-306` through `compact_row_string` at `:269-275`:

```text
return f"({raw})-s^80*la^20*(1+s*tau)"
```

The V1 renderer uses the identical `compact_row_string` and the identical `poly E{ell}=compact_row_string(...)` emission line; only the `source_a` banner comment differs. IMPACT_MATRIX's "source-identical to v2 on this row" is therefore exact for the defective call.

The corrected compiler does not rewrite that formula. It hash-pins

```text
c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b  base_B.sing
```

refuses any other digest, and extracts each of `E1,...,E8,LT` by the unique-anchor regex `^poly NAME=(.*);$`. The nine extracted bodies were compared, by `grep`/`sed` equality, against all four compiled sources (`corrected_A_lpdp.sing` and `corrected_A_dp.sing` on both hosts). All nine match B byte-for-byte. There is no other transformation of `E8`.

**Is this the cleanest sound correction?** Yes, for the charged question. A hand refactor of the factored row would re-trust the renderer that already emitted a wrong constant. A patched `compact_row_string` would restore a factored encoding only by introducing a new renderer, which this package correctly refuses to claim. Extracting the already reviewed expanded polynomials and changing only contraction and term order is the conservative sound repair of the *contraction/order* check. It is not an independent derivation of the eight charged equations; `RESULT.md` and the compiled firewall string both say so.

---

## Charge 2 — 35-generator equality

**CONFIRMED. Mutual reduction is the order-invariant certificate. Textual basis identity is not required, and is not claimed, for global `dp`.**

Pinned expected B stdout SHA-256 is `d5317aac…`, identical to the certificate package's `aws_r6d/singular.stdout`. It contains exactly the consecutive indices

```text
GH[1], …, GH[35]
```

with

```text
GH[34]=la^20
GH[35]=s
```

The compiler refuses any other shape (`len(expected)!=35` or last two not `la^20,s`). Both compiled sources build

```text
ideal EXPECTED=<all 35 parsed bodies>;
```

The `EXPECTED=` lines end `…,la^15*q0^4,la^20,s;` and contain 34 commas, hence 35 generators. None of those bodies contains an embedded comma.

Both sources then run the two membership loops, in this order:

1. `for i=1..size(GH): reduce(GH[i], GE)==0`, else `FAIL_GH_NOT_IN_B`;
2. `for i=1..size(GE): reduce(GE[i], GH)==0`, else `FAIL_B_NOT_IN_GH`.

Then `PASS_A_B_SPECIAL_FIBRE_MUTUAL_REDUCTION`. Both AWS stdouts print that marker once and print no `FAIL_`.

Emitted bases:

| execution | order | `GH[1]` | last two | special-fibre size |
|---|---|---|---|---:|
| Box03 LPDP | `(lp(1),dp(8))` | `4*r1^2+8*r2*r0+12*r1*r0+9*r0^2` | `la^20`, `s` | 35 |
| r6d DP | `dp` | `s` | `la^15*q0^4`, `la^20` | 35 |
| expected B | `(lp(3),dp(8))` after eliminating `u` | same as LPDP | `la^20`, `s` | 35 |

The LPDP generator list is *textually identical* to the pinned B certificate list. The global-`dp` list is not. After stripping `GH[n]=` prefixes and sorting, the 35 DP bodies are identical as a set to the 35 LPDP/B bodies. That is compatible with equality of ideals: a reduced Gröbner basis depends on the monomial order, while the ideal it generates does not. In `(lp(1),dp(8))` the Rees parameter `s` occupies its own lex block and appears last. In global `dp`, total degree puts the degree-1 generator `s` first and the degree-20 monomial `la^20` last. Mutual reduction, not textual identity of reduced bases, is the certificate that was actually run. Requiring the DP printout to match `la^20,s` in that order would have been an order-confused false failure.

Contraction generator counts 403 (LPDP, matching B) versus 546 (DP) are likewise order-dependent presentations of the same colon, not a disagreement of ideals.

---

## Charge 3 — contraction and saturation order

**CONFIRMED. Direct `sat` is an independent algorithm for the same colon as B's `u s-1`. Specializing first would be wrong.**

Both compiled sources, in this order and with no intervening specialization:

```text
ideal I = ⟨E1,…,E8, LT⟩          # nine Rees generators, no s=0
ideal CS = ⟨s⟩
ideal C  = sat(I, CS)            # contract from s≠0 first
ideal H  = C + ⟨s⟩               # only then specialize
ideal GH = std(H)                # only then standardize
```

B's independent device, on the same nine polynomials, is

```text
J  = ⟨E1,…,E8, LT, u s − 1⟩
C  = eliminate(std(J), u)        # Rabinowitsch colon I : s^∞
H  = C + ⟨s⟩
GH = std(H)
```

These compute the same contraction `φ_s(I) : s^∞`. LPDP is the induced order on `(s; coordinates)` after B's inverse variables are removed; DP is an independent global order. Matching LPDP contraction size 403 with B, and then matching the special-fibre ideal in both orders, is the expected signature of two algorithms for one colon.

**`sat` versus `sat_with_exp`.** Native `sat(I,J)` returns an ideal. `sat_with_exp(I,J)` returns the two-entry list `(saturated ideal, exponent)`. The fleet return-type control
`max12_912_order3_d1_sat_return_type_probe_20260826T011921Z_r6d`
proved, in both `dp` and `(lp(1),dp(8))`, that `list L=sat(I,J)` has size one and that `L[1]` is the whole ideal, mutually reducing with the direct assignment. The corrected sources assign `sat` directly to `ideal C` for the `s`-contraction (no list wrapper, no exponent required). They use `sat_with_exp` only later, on the special fibre, to read the torus exponent. A subsequent `sat(GH, ⟨TORUS⟩)` repeats the unit check without the exponent API. That is the correct split.

The old factored A used the list wrapper `list SC=sat(I,CS); ideal C=SC[1];`. IMPACT_MATRIX is right that this wrapper is not the E8 defect. The fleet probe withdrew the first-generator-truncation diagnosis globally. Corrected A does not rely on the wrapper.

**Later torus saturation is not the contraction.** After `GH` is computed and printed, the sources test `reduce(TORUS, GH)`, then `sat_with_exp(GH, ⟨TORUS⟩)`, then `sat(GH, ⟨TORUS⟩)`. Those localize the already computed special fibre. They are not a second contraction from `s`.

**Why `s=0` before contraction is wrong.** Every submitted generator is divisible by a positive power of `s` (`E1…E8` at least `s^{52}`, `LT` by `s^4`). Two wrong orders:

- `I + ⟨s⟩` without inverting `s` yields `⟨s⟩`. The “special fibre” has no coordinate relation at all.
- `⟨s, u s − 1⟩` is already `(1)`.

Contraction first inverts `s` and intersects back; only then does `s=0` cut `in_w(I)`. The emitted 403/546 contraction generators and 35-element special fibre are direct evidence that this order was the one executed. A-fast's unit fibre `GH[1]=1` is not this wrong order: A-fast still saturates first, but its input `E8` already differs from B by a nonzero *constant*, so the ideal is not contained in `⟨s⟩`.

---

## Charge 4 — certificate semantics

**CONFIRMED. These checks support exactly the no-torus-leading-coefficient theorem on the frozen support/weight. `la^20` is a full-initial-ideal / S-polynomial consequence, not `in_w` of a submitted generator.**

Both AWS stdouts print, once each, with no `FAIL_`:

```text
PASS_A_B_SPECIAL_FIBRE_MUTUAL_REDUCTION
LA20_IN_FULL_SPECIAL_FIBRE=1
TORUS_IN_FULL_SPECIAL_FIBRE=1
TORUS_SATURATION_EXPONENT=1
TORUS_SPECIAL_FIBRE_IS_UNIT=1
RESIDUE_IDEAL_IS_UNIT=1
CONTROL2_REES_RESIDUE_SURVIVES=0
```

Interpretation, against the compiled source:

1. **`reduce(la^20, GH)==0`.** Direct polynomial membership in the full special fibre. In LPDP this monomial is the reduced basis element `GH[34]`; in DP it is `GH[35]`. Either way `la^20 ∈ H = C + ⟨s⟩`. It does not involve `s`, so `la^20 ∈ in_w(I)`.

2. **`reduce(TORUS, GH)==0` with `TORUS=la·tau·rho·q1·q0·r2·r1·r0`.** Direct membership of the eight-factor product. Independent of (1): `dp`-leading term `la^{20}` has degree 20 and does not divide the degree-8 product.

3. **`sat_with_exp(GH, ⟨TORUS⟩)` exponent 1 and unit.** Least `e` with `GH : TORUS^e` equal to the saturation is 1, and that saturation is `(1)`. Together with (2) this is `TORUS ∈ GH`.

4. **`sat(GH, ⟨TORUS⟩)=(1)`.** The same colon without the exponent API.

5. **Residue maximal ideal `⟨la-1, tau-1, rho-1, q1-1, q0+1, r2-1, r1-1, r0+2⟩` on the unit torus fibre is unit.** The displayed residue `(1,1,1,1,-1,1,1,-2)` does not lift. This is implied by torus-emptiness and is retained as a redundant point check.

On the residue torus every displayed coordinate is required nonzero, in particular `la ≠ 0`. A monomial `la^{20}` in `in_w(I)` is already a canonical obstruction to this weight. Saturating only by `la` would already yield `(1)`. The eight-factor product is a stronger, independently verified membership, not a crutch.

**`la^20` is not `in_w(E8)`.** Submitted `E8`, extracted from B, begins

```text
-1*s^81*la^20*tau-1*s^80*la^20+…
```

The `la^{20}` terms live at `s^{80}` and `s^{81}`. The lowest `s`-power in `E8` is 52, on the `(q,r)` binomials. None of `E1,…,E8,LT` has a lowest `s`-piece equal to a power of `la`. The monomial appears only after contraction has used higher-weight terms to cancel lower-weight layers. That is the Buchberger / S-polynomial content of `in_w(I)`, which is why the generator-initial prevariety can vanish at the residue while the full initial ideal does not. The v2 source review and the certificate review already recorded this distinction against the same B polynomials; corrected A inherits those polynomials and reprints the same monomial.

These checks support exactly: no exact arc with this frozen axis, these loads, this support, this weight, and all eight displayed coordinates nonzero. They do not empty the axes of this torus, other weights, moving axis, `q2`, other loads, the fan, D1, or JC2.

---

## Charge 5 — AWS custody

**CONFIRMED for both registered executions. They are two orders of one compiler/source strategy, not two derivations of the equations.**

Registered tags, matching `worker.metadata` and stdout `AWS_TAG=`:

```text
max12_912_order3_d1_double_root_control2_rees_corrected_A_20260826T013127Z_box03_LPDP
max12_912_order3_d1_double_root_control2_rees_corrected_A_20260826T013127Z_r6d_DP
```

`AWS_REGISTRATION.md` records both workers blocked in `WAITING_COMPILE` with no GO sentinel after the complete frozen source closures verified. Package `SOURCE_CLOSURE.sha256` is five files (`PREREGISTRATION.md`, `base_B.sing`, `expected_B_certificate.stdout`, `compile_corrected_A.py`, `remote_worker.sh`) and is byte-identical in both AWS trees. Both `source.check` files report all five OK. Compiler is AWS-only (`REFUSE_NON_LINUX`, `REFUSE_NON_AWS_EC2`, tag prefix `…_rees_corrected_A_`). Caps match registration and metadata:

| host | encoding | compiler | solver | PID |
|---|---|---|---|---|
| Box03, `ip-172-30-0-249` | LPDP, 192 GiB / 21600 s | 4 GiB / 600 s | `memory_kib=201326592` | 133163 |
| r6d, `ip-172-30-0-45` | DP, 320 GiB / 43200 s | 4 GiB / 600 s | `memory_kib=335544320` | 200483 |

Both compilers: rc 0, stderr 0 bytes, unique `PASS_CONTROL2_REES_CORRECTED_A_COMPILER` once, expected 35 GH generators, pinned input hashes reprinted. Both solvers: rc 0, stderr 0 bytes, `/usr/bin/time -v` isolated in `singular.time` (Box03 wall `1:19.21` / RSS 102852 KiB; r6d wall `5:51.12` / RSS 494288 KiB; both `Exit status: 0`). Unique encoding PASS once each (`…_LPDP`, `…_DP`). Worker requires those markers, mutual-reduction PASS, `LA20_IN_FULL_SPECIAL_FIBRE=1`, torus-unit, empty CAS stderr, rc 0, and absence of `FAIL_`. Both wrote `PASS_REMOTE_WORKER`. No `COMPILE_FAILED`, `SOLVE_FAILED`, or `REFUSED` file exists.

`solve_source.check` verifies only the encoding actually solved (LPDP on Box03, DP on r6d). Each host also emitted the other order, tagged with *that* host's job tag. After replacing the embedded AWS tag, the two LPDP sources are identical and the two DP sources are identical. Frozen solve inputs match `PRESOLVE_CUSTODY.md` and `RESULT.md`.

Singular on both hosts is 4.3.2 (4330). Timing is not mixed into CAS stderr, unlike quarantined v1.

The two A runs share `compile_corrected_A.py`, the same pinned B polynomials, and the same expected 35-generator ideal. They differ by ring order and by AWS host/caps. That is dual-order corroboration of one contraction strategy, not a second derivation of `E1,…,E8,LT`.

Non-blocking custody note, not a repair: `PRESOLVE_CUSTODY.md` quotes normalized SHA-256 values `21edd6da…` / `83ddc95f…` for tag-replaced sources. Those `.normalized` files are not stored. Several standard tag-replacement conventions, including replacement by `TAG` and deletion of the `AWS_TAG=` line, produce *cross-host identical* files for each order but do not reproduce those two numeric hashes. The identity claim itself is independently verified by `diff`; the published normalized digests are unreproduced prose.

---

## Charge 6 — impact enumeration

**CONFIRMED against repository text. No top-level promoted theorem consumed a bad A endpoint. The v2 source review's A-equivalence discussion is superseded for A only; its B-only computation remains valid. Tied-toric and other list-wrapped `sat` clients are not quarantined.**

Historical control-2 A-only artifacts that consumed the bad renderer:

| artifact | renderer / input | endpoint | disposition |
|---|---|---|---|
| V1 A | `compile_control2_rees.py` `source_a` / `compact_row_string`, same E8 row as v2 | Box02 tag `…rees_20260826T004241Z_box02_A`; A SHA `912a6e27…` (r6d compile `99a0ed11…`; normalized `faee98eb…`) | Affected. Solve stopped. V1 wrapper separately fails its timing/stderr contract. `SOFTWARE_CONTROL.md` forbids use |
| V2 A | `compile_control2_rees_v2.py:297-306` through `:269-275`; emitted `poly E8` at line 12 | Box02 tag `…rees_v2_20260826T005028Z_box02_A`; A SHA `d72c1e53…` (r6d emission `2b416cb8…`; normalized `8775a483…`) | Affected. Registered Box02 Singular process was stopped. No A mathematical verdict |
| A-fast | `compile_Afast.py` pinned `base_A.sing` SHA `2b416cb8…` | Box03 tag `…rees_Afast_20260826T011021Z_box03`; contraction 398, `GH[1]=1` | Affected / immutable negative control. Unit fibre is the spurious E8 constant, not a no-lift theorem |
| Identity control | deliberate comparison of `2b416cb8…` against `c905f1b5…` | r6d tag `…source_identity_20260826T012642Z_r6d`; stdout SHA `7baf7e60…` | Unaffected diagnostic. Its intended endpoint is the exact `E8` failure and displayed difference |

SHA prefixes in `IMPACT_MATRIX.md` match `COMPILE_CUSTODY.md` of v1 and v2, A-fast `SOURCE_CLOSURE`, and the identity `RESULT.md` / stdout. A-fast printed `A_CONTRACTION_GENERATORS=398` and `GH[1]=1` as charged.

**Top-level / xmodel statements.** `notes.md` 01:25Z, `APPROACHES.md`, `PROGRESS.md`, and `AUDIT.md` recorded the A-fast unit fibre versus inverse-B nonunit as an unresolved discrepancy and as a `sat`-API false alarm, not as a promoted no-lift theorem. The v2 source review explicitly refused to read encoding A as a result. The certificate `RESULT.md` left promotion pending an A endpoint and did not consume A-fast. Campaign log `notes.md` 01:42Z describes this corrected package; it is not a prior promotion of the bad renderer. No top-level theorem relied on a bad A endpoint.

**V2 source review A-equivalence, superseded in part.** That review confirmed, from compiler *source*, that both encodings were intended to be the same nine specialized generators (same tails, same targets, same Rees map, “same generator” for `LT`). It did not compare emitted A polynomials with emitted B. The identity control now shows that intention fails at rendered `E8`. The A-equivalence discussion is therefore superseded for A. The review's computational layers that used only B — hand evaluation of B generator-initials, B contraction, B unit torus fibre, B custody — remain valid, as does its explicit firewall that encoding A was not a result.

**Do not contaminate tied-toric.** The tied `alpha=2 beta` toric-blowup compiler and older weighted-infinity compilers use independent equation builders. Their list-wrapped `sat` calls are semantically complete on fleet Singular 4.3.2. The earlier stop of a tied A process on the list-wrapper suspicion was unnecessary for this E8 defect. IMPACT_MATRIX states this correctly.

---

## Charge 7 — B theorem and firewall

**CONFIRMED. The B-only theorem and the focused B certificate review remain valid. The strongest permitted promotion is exactly the frozen support/weight torus statement.**

B encoding, certificate, and r6d outputs never consume factored A. Certificate stdout SHA `d5317aac…` is the expected stream pinned here. V2 B printed contraction 403, special fibre 35, torus fibre unit, `GHT[1]=1`, residue unit. The certificate printed `GH[34]=la^20`, `GH[35]=s`, saturation exponent 1, and the same unit torus fibre. Corrected A mutually reduces to that ideal by a different contraction algorithm and, in DP, a different term order.

Strongest statement now licensed, and no more:

For the finite Rees ideal in the pinned expanded equations, with

```text
a=1, h=q2=k=nu=0, mu=2/3,
w(la,tau,rho,q1,q0,r2,r1,r0)=(4,1,1,22,22,30,30,30),
```

the full weighted initial ideal contains `la^{20}`, hence has empty intersection with the eight-coordinate torus. No arc with this exact fixed axis, fixed loads, support mask, and weight vector has a leading coefficient in that torus. In particular the displayed residue does not lift.

It is not a moving-axis, moving-load, nonzero-`q2`, other-support, other-weight, whole-cone/fan, D1, or JC2 theorem. The two corrected-A AWS executions corroborate that statement as contraction/order checks of B's equations. They do not re-derive those equations.

---

## Directed defect search

| hunted defect | finding |
|---|---|
| Hand-repaired E8 smuggled into the compiler | Absent. Compiler hash-pins B and copies nine unique `poly NAME=…;` bodies |
| Extracted polynomials silently rewritten | All nine bodies match `base_B.sing` on both hosts and both orders |
| Expected B stream not the certificate stdout | SHA `d5317aac…` identical; 35 consecutive `GH[i]`; last two `la^20,s` |
| One-sided membership sold as equality | Both reduction loops are present and both PASS |
| Textual DP basis required | Not required; sorted bodies match; mutual reduction is the certificate |
| `s=0` before contraction | Not what the source does. Output sizes 403/546 then 35 refute `⟨s⟩` or `(1)` |
| `sat` truncated to the first generator | Direct `ideal C=sat(I,CS)`. Fleet probe: native `sat` is ideal-valued. 403/546 generators |
| `sat_with_exp` used as the `s`-contraction | Used only later, on `GH`, for the torus exponent |
| List-wrapper blamed for E8 | Identity control fails at the polynomial `A_E8-B_E8`, before any `sat` |
| `la^20` is `in_w(E8)` | False. `E8`'s `la^{20}` terms are `s^{80}` and `s^{81}` |
| Hidden localization producing `la^{20}` | Printed in `GH` before torus saturation |
| Two A hosts as independent equation derivations | Same compiler, same pinned B, same EXPECTED; only order/caps differ |
| Bad A promoted at top level | No. V1 quarantined; v2 A stopped; A-fast is a negative control; identity is the diagnostic |
| V2 B theorem contaminated | B never consumed factored A. Certificate review remains valid |
| Tied-toric quarantined for `list L=sat` | Not shown affected. Fleet probe withdrew that diagnosis |
| V1 telemetry contamination | Corrected worker isolates `singular.time`. V1 remains a software control |
| Resource kill disguised as a unit | rc 0, empty stderr, explicit PASS markers, timing/RSS recorded |

Non-blocking notes, not repairs: (i) PRESOLVE's numeric normalized hashes are unreproduced from stored files, while cross-host identity of each order after tag replacement is independently verified; (ii) the identity wrapper writes `FAILED` on the intended `FAIL_DP_E8`; (iii) each host emits the unused other-order source tagged with its own job tag; (iv) this is still not an independent derivation of the eight equations.

---

## Sharpest non-claim

Dual-contraction, dual-order emptiness of the torus special fibre of this frozen-axis, fixed-load, weight-`(4,1,1,22,22,30,30,30)` degeneration of the exact eight-row D1 coefficient ideal, using the reviewed expanded B polynomials. Not a second derivation of those polynomials. Not a repaired factored renderer. Not emptiness of the axes. Not a statement about any other ray, residue, load, moving axis, or `q2` chart. Not a classification of the double-root fan. Not D1. Not JC2.

---

## Evidence layers (do not collapse)

1. Identity-control stdout: `E1,…,E7,LT` pass, `A_E8-B_E8` the displayed nonzero constant; bad `poly E8` at factored-A line 12; renderer `compact_row_string` / `source_a`.
2. Byte extraction of nine B polynomials into both compiled A sources; compiler hash pins; no E8 rewrite.
3. Construction order `sat` then `s=0` then `std`; comparison with B's `u s-1`; fleet `sat` versus `sat_with_exp` control.
4. 35 consecutive expected generators; both reduction loops; LPDP textual identity with B; DP sorted-body identity and `s`-first / `la^{20}`-last printout.
5. Direct `la^{20}` and torus membership, exponent-one saturation, unit localization, residue unit; `la^{20}` not a submitted initial form.
6. SHA-256 of the corrected-A freeze chain and both AWS result trees; v1 `SOFTWARE_CONTROL.md`; IMPACT_MATRIX against v1/v2/A-fast/identity custody files; prior B source and certificate reviews.

CORRECTED_A_CONFIRMED
