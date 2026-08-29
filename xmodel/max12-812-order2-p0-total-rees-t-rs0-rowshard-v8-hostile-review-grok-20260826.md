# Hostile software/source review: `T-rs-0` V8 explicit normal form

**CONFIRMED**

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v8_20260826/` |
| Charged claim | Explicit-normal-form incremental evaluation of the frozen 569-term `T-rs-0` source in the ordinary parent ring, modulo `sigma^13`; four-lane discovery of a 23-name finite prefix and a four-term exact-Q correction |
| Producer status | Four harvested AWS lanes `aws_p32003_v8r1`, `aws_p65521_v8r1`, `aws_q_v8r1`, `aws_p1000033_v8r1` plus the documented initial compiler fail-closed pair. `RESULTS.md` is provisional pending this review |
| Overall verdict | **CONFIRMED** as complete source discovery modulo `sigma^13`. V8 eliminates the Singular `qring` storage hazard. The 569 frozen terms are reconstructed, not rewritten. The four-lane mathematical payloads agree, and the exact-Q identity is an ordinary-ring polynomial identity, independently expanded |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile reread of every charged file. Printed `PASS` tokens are not algebra |
| Method | SHA-256 of every named pin and freeze entry; complete source reading of V8, V7, V6, stream V2, V0R1, square-ladder `tail_text`, and the named V0R1 review/audit/gate; independent reconstruction of all 14 `phi_text` strings and the seven V8 formula-pair hashes; independent expansion of `FrozenCert`, `FrozenOmit`, and `Delta/rho^2`; modular reduction of all six `Keep*` polynomials at 32003, 65521, and 1000033; census of every emitted `.sing` and certificate; one tiny Singular 4.4.1 canary to reproduce the reported `qring` hazard. No Sage, msolve, Lean, or local replay of the 569-term engines |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

V8 is a software-semantics repair of the predecessor `qring` clients, plus a four-lane discovery certificate. It is not a saturated Rees chart, a base-change theorem, an order-two exclusion, a maximum-twelve proof, or a JC2 verdict.

---

## Narrow reusable theorem / certificate

Work in the ordinary polynomial ring

```text
R = k[sigma, rho, 76 candidates, 7 inactive], dp
```

with `k = Q` or `F_p` for `p ∈ {32003, 65521, 1000033}`, and let `I = (sigma^13)`. Let `r : R → R` be remainder against `std(I)`. Let `Phi_row` be the frozen V0R1 `phi_text` of row `row ∈ {1..7}` (569 tail monomials plus the four target terms), built from the pinned square-ladder dictionary.

Then:

1. Every V8 row program is an ordinary parent-ring program: it contains no `qring`, and every source atom, cached power, factor product, and accumulator update is an explicit `reduce(-, PrefixNF)` with `PrefixNF = std(ideal(sigma^13))`. The image of each incremental schedule in `R/I` is `r(Phi_row)`.
2. The four harvested `DISCOVERY.json` files agree on every mathematical field after deleting characteristic and evidence-path hashes. Common `sigma`-order is 10. The discovered support through grade 12 is exactly the 23 names

```text
ell1, ell2, cs, cs1, cs2, rs, rs1, rs2,
a1, aa1, aaa1, a0, aa0, aaa0,
c1, e1, ee1, c0, e0, ee0,
k, k1, k2c.
```

Every other candidate bit is 0. All seven inactive controls `k6_1, k2, k2_1, mu2, mu4, mu6, J` are 0. Both negative controls fire.
3. The six retained cusp coefficients satisfy the frozen owner identities in the ordinary parent ring, and the total correction is the four-term identity

```text
Delta / rho^2
  = 5120 * rho^2 * cs^4 * k
  + 2640 * cs^2 * rs^2 * k
  - 4608 * cs * a0 * c1
  - 4608 * cs * a1 * c0
  = 16 * cs * (320 * rho^2 * cs^3 * k
               + 165 * cs * rs^2 * k
               - 288 * (a0*c1 + a1*c0)).
```

`Delta` is even in `rho`, vanishes at `rho=0`, is exactly divisible by `rho^2`, and is nonzero. The three prime-lane `Keep*` polynomials are the exact-Q polynomials with coefficients reduced modulo `p`.

This licenses a 23-name finite-prefix source for a later saturated `D_+(rs)` Rees/base-change client. It licenses nothing larger.

---

## Findings by severity

### High

None that change the 569-term image, the 23-name support, or the `Delta` identity.

### Medium — software only

**M1. Release-line overmatch rebuilds `TPhi` after extraction.**
File: `compile_t_rs0_rowshard_v8.py:164-167`.
Frozen stream body (`compile_t_rs0_stream.py:161`) ends each row with the combined assignment

```text
TPhi=0; FPhi=0; TSpec=0; Wrong=0; TQ=0; FQ=0; Tg=0; Fg=0; TRem=0; FRem=0;
```

V8 replaces any line that `startswith("TPhi=")` and is not exactly `TPhi=0;`. The release line therefore becomes a second full `TPhi` incremental schedule. Observed on every harvested shard, e.g. `aws_q_v8r1/compiled/t_rs0_row2_q.sing`: first schedule ends at line 440, `FPhi` at 732, `KeepT10_2=Tg` at 931, second `TPhi=0;` at 965, second `mu2` target at 1241, then `STREAM_RELEASED`. The same pattern holds on rows 1–7 of all four lanes.

Consequences:

- `FPhi=0` and the rest of the release line are discarded. In a one-process stream that would leak the previous row; V8 runs seven processes, so it does not.
- Cached powers are redeclared. Every row transcript contains Singular comments `// ** redefining T_F*pow*`. Row 2 has 14 such lines; row 6 has 22. The validator only rejects lines starting `? ` or `   ?` (`prepare_certificate.py:45`, used by V8 prepare at line 108).
- `row_incremental_update_count` overwrites `t_updates` on the second match, so the JSON still reports `2*(n_terms + n_target)` and does not detect the extra schedule (`compile_t_rs0_rowshard_v8.py:184-185`).
- `Keep*`, `diff` support, grade bits, term counts, and maps are all computed on the first `TPhi`. On the three keep-rows, `KeepT*=Tg` is strictly before the second `TPhi=0;` (row 2: 931 < 965; row 3: 1005 < 1039; row 6: 1747 < 1771). The extra schedule cannot rewrite the certificate.

This is the same class of `TPhi=` census mistake V7 was written to close, now on the successor transformer. It does not change the recorded discovery. Repair before pinning V8 as a frozen predecessor: match the formula line exactly, or exclude any line that starts `TPhi=0;`.

**M2. “Legacy formula text” does not lock the incremental schedule.**
File: `compile_t_rs0_rowshard_v8.py:61-74` and `:127`.
`formula_data` rebuilds `phi_text` and compares it to `old.phi_text`. That equality cannot fail unless `phi_text` itself changes. `row_formula_pair_sha256` is `sha256(sha256(T_phi)+sha256(F_phi))` of those unused monolithic strings, not of the emitted `BuildTerm` program. Independently recomputed, the seven pair hashes match all four compiler `result.json` files exactly. The 569-term dictionary is still fail-closed by `tail_text` (length 10, load linearity, weight `12+row`, `Fraction(str)`). A later edit of `build_schedule` would not move the formula hashes.

**M3. Validator diagnostic filter is narrower than the preregistration sentence.**
Preregistration: any “Singular diagnostic” is `FAIL/UNRESOLVED`. Implementation (`prepare_certificate.py:45`, `finalize_discovery_v8.py:82-83`) only rejects `T_RS0_FAIL=` and lines starting `? ` / `   ?`. The `// ** redefining` comments from M1 are accepted. They are comments, not `?` errors, and they are produced only by M1. A failed row still cannot emit `DISCOVERY.json` (see §5).

### Low

**L1.** V8 prepare drops V6’s explicit `len(variables)==85` certificate census (`prepare_certificate.py:218-220` vs `prepare_certificate_v8.py:197-201`). Mitigated: the ring is `("sigma","rho")+CANDIDATES+INACTIVE` from the frozen V2 lists, and the compiler JSON still carries `ring_variable_count=85`.

**L2.** V8 `build_schedule` multiplies a load at most once (`compile_t_rs0_rowshard_v8.py:117-120`). Frozen `tail_text` already rejects load exponent `>1` and V6 census requires `max_loads==1`. Unreachable on this dictionary.

**L3.** `launch_host.sh` tars the entire V8 and V6 packages, so a later relaunch ships harvested `aws_*` trees. First-wave archives (`6f09c8ce…` at `T195800Z` for 32003/65521) differ from second-wave (`0ecda6a8…` at `T200100Z` for Q and 1000033) for that reason. Each job re-checks the four FREEZE manifests before compile.

**L4.** `quit;` on a failed row/certificate yields Singular `rc=0`. `run_aws.sh` therefore proceeds to the next Python gate. The Python gates reject `T_RS0_FAIL=`, missing `ENDPOINT`, and wrong map bits. Not a `DISCOVERY.json` path.

### Notes, not defects

- `k10` weight 2, `k6` weight 6, `k2` weight 10 is the frozen square-ladder convention (`LOAD_WEIGHTS = [2,6,10]`), not an inversion. `k10*Lambda^2`, `k6*Lambda^6`, `k2*Lambda^{10}`.
- `monomial[:7] → F0..F6` matches `term_text`. First row-2 term `[0,0,0,0,0,0,2,0,0,1]` is `(-3/32)*T_F6^2*T_K2*Lambda^10`, emitted as `sigma^20 * T_F6pow2 * T_K2`.
- All 569 JSON coefficients are strings. `Fraction(str(raw_coefficient))` is identical to the original formatter.
- `Delta=0` remains an allowed recorded outcome (`finalize_discovery_v8.py:105-109`). All four lanes have `delta_nonzero=true` and `delta_quotient_terms=4`.
- Initial dual-prime launch `FileExistsError` (`FAILCLOSED_INITIAL_LAUNCH.md`; `compiler.validation` `compiler_rc=1`; empty stdout digest `e3b0c442…`) is packaging only. Repair is the `v7_baseline` child path (`compile_t_rs0_rowshard_v8.py:212-215`).

---

## 0. Custody and SHA pins

Independently recomputed SHA-256. V8 `FREEZE.sha256` itself is

```text
508c7cc0aeaf26385b5954173ca366b362c697540879822327db3d75367ccc26
```

matching `RESULTS.md`. All eight FREEZE entries rehash. All thirteen `RESULTS.sha256` entries rehash. All eighteen `FAILCLOSED_EVIDENCE.sha256` entries rehash. Predecessor FREEZE files V7/V6/stream V2/V0R1 rehash with zero mismatches. Every harvested `EVIDENCE.sha256` rehashes with zero mismatches.

| Artifact | SHA-256 |
|---|---|
| V8 `compile_t_rs0_rowshard_v8.py` | `41484e92ac2c3433562b8f120c922cb8d2bff5bff736c4b5664989c692dc85fa` |
| V8 `prepare_certificate_v8.py` | `3a4b5166fc09b0c6892c983e9ddb2cb6f21779013bd760fe07ba695f58be6002` |
| V8 `finalize_discovery_v8.py` | `b939dc34f8c194a3a307ccb901b625bc9ed307fee562f06922d792c4ec420cfd` |
| V8 `run_aws.sh` | `6e58adcae4dab87a42f038d8efac6010dfb96730d8b9b92e5ba988a9e3fb1f0c` |
| V8 `PREREGISTRATION.md` | `7d0929b42914b585323dd0a51505a2748629c607a84decd417ac868560254eef` |
| V7 compiler (V8 pin) | `c678d293c2c26462c3ca5cc3776644b181176a2cf657b0beb6b65754c7dcd2d0` |
| V6 compiler | `9937fcfc61dff1d39029e6653b2be73ab3f835c2bc8bc81405876e54ef10b6bf` |
| V6 prepare | `d5f38037a2a1233ceba9e4102e3f65e3690b028d9c627f1dbff8fcee6ccd2e5f` |
| V6 finalize | `3a68a6d0d61f9a211f40de80fbdd767006c76a4c25ae8f88482d9002ceb84bfd` |
| stream V2 compiler | `5b176dfd0747f3736bc4519077877f4d877b5b726b9701e1b9dcaf56e059a112` |
| stream V2 validator | `4ff10d85aeb91f3853a4fd2c89ac2e0fe93bd07fd2c3769241cd8f40afb01949` |
| V0R1 compiler | `3aa6bbbbe539607461c5f27b400aeedd335a4d18e01e40d730f5537da4f45938` |
| V0R1 implementation review | `51c294e0ae3d07ced3dac380814d4767bec1e5cc63bd1159cd76ce698f3f69ea` |
| square-ladder compiler | `77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc` |
| `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` |
| canonical tails | `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8` |
| Codex T-rs audit | `5e91571d84b1bae92306bad0a31924a2b4fe3bf183ee8d75ace558bc2dd52c0d` |
| Gate-T obligation table | `50db2706f5a8d435618e615bfc393d2eb7dd22828a9a3fa35ac8a2e685ab15c4` |
| owner cusp compiler (hashed, not imported) | `9d49988213806d42ea4523881595837007fa861369f31fd18d0c83b7adf494d4` |
| raw-cusp V2 compiler (hashed, not imported) | `8abeda327a7362e0cd5bdc8b73135bc59e1883664e3824783e34c9182743686d` |

Runtime chain:

```text
V8 FREEZE.sha256
  -> compile_t_rs0_rowshard_v8.py
       -> V7_COMPILER_SHA256 -> V7 compiler
            -> V6_COMPILER_SHA256 -> V6 compiler
                 -> STREAM_SHA256 -> stream V2
                      -> OLD_SHA256 -> V0R1 compiler
                           -> EXPECTED -> tails, ladder, owner, raw-cusp V2, audit, gate
                           -> EXPECTED_CANONICAL_TAILS
                      -> REVIEW_SHA256 -> V0R1 implementation review
  -> prepare_certificate_v8.py -> V6 prepare -> V2 validator
  -> finalize_discovery_v8.py -> V6 finalize -> V2 validator
run_aws.sh also sha256sum -c V7, V6, and stream V2 FREEZE files.
```

Tail census on keys `'1'`–`'7'` is `36+54+58+81+89+120+131 = 569`. Every coefficient is a JSON string; every denominator is a power of two, maximum `2^23 = 8388608`; none of `32003`, `65521`, `1000033` divides any denominator. Certificate integers `32768,35,4096,8192,1536` remain nonzero in all three fields (`32768 ≡ 765 (mod 32003)`).

AWS engines are Singular 4.3.2 x86_64-Linux on all four `v8r1` lanes; `qring_used=0` is in every `launch_registration.txt`.

---

## 1. The `qring` hazard, and whether V8 eliminates it

A local Singular 4.4.1 canary in `R = Q[sigma, ell1]`, `qring Q = std(sigma^13)`, reproduces the charged 4.3.2 report:

```text
poly p = sigma^13*ell1;
p == 0          -> 0     (stored as sigma^13*ell1)
diff(p, ell1)==0 -> 0     (stored as sigma^13)
subst(p, ell1, 1)==0 -> 0 (stored as sigma^13)
reduce(sigma^13*ell1, std(ideal(sigma^13))) == 0  -> 1
```

In the ordinary parent ring the unreduced assignment is also nonzero, and `reduce` is zero. Equality, substitution, and differentiation on a `qring` assignment are therefore not quotient normal-form tests. V0R1/V2/V5/V7 comparison sentinels that assumed they were are software no-verdicts. That quarantine is justified.

V8 eliminates the operational assumption:

- V7 header `qring Q=PrefixIdeal;` is replaced by `ideal PrefixNF=PrefixIdeal;` plus `poly PrefixCanary=reduce(sigma^13*ell1,PrefixNF); int explicitNF=(PrefixCanary==0);` (`compile_t_rs0_rowshard_v8.py:144-150`).
- Every `poly T_*` / `poly F_*` source atom is wrapped in `reduce(-,PrefixNF)` (`SOURCE_POLY`, lines 159-163).
- Every tail factor product and accumulator add is `reduce(-,PrefixNF)` (`build_schedule`, 91-127).
- The product gate includes `explicitNF` (`:179-180`).
- Compiler and prepare refuse any surviving `qring ` or `quit(` (`:187-188`; `prepare_certificate_v8.py:94-95`; `finalize_discovery_v8.py:69-70`).
- The recombination certificate is emitted in the ordinary parent ring with `T_RS0_CERTIFICATE_PREFIX_ALGEBRA=PARENT_RING_NO_QRING` (`prepare_certificate_v8.py:199-228`). V6’s certificate `qring` is gone.

Independent census of all 28 row programs and all four `certificate.sing` files: zero `qring `, zero `quit(`, one explicit-NF canary, `T_RS0_QRING_DISABLED=1` and `T_RS0_EXPLICIT_NORMAL_FORM=1` unique in every row transcript. The V8 canary tests that `reduce` works in the parent ring; the hazard elimination is the absence of `qring` plus explicit reduction before every comparison that is a quotient test.

---

## 2. Transitive import / 569-term reconstruction

V8 does not copy `source_block`, `series`, `shifted_series`, or `phi_text`. It `exec_module`s the pinned V7 compiler, which imports V6, stream V2, and V0R1. `formula_data` calls `base.tail_text` (square-ladder) and `old.phi_text` (V0R1) on the same 569 entries.

Independently, for every row and both prefixes, V8’s rebuilt `expected` string equals `old.phi_text`. Independently, the seven V8 pair hashes equal the four compiler JSON maps:

```text
1 54ea6593efa98ea2fb9d4968a882807cf3af9aca0852688b968e40bbf94d9e23
2 c7177a5ca398708e67150fd9e87b794512351968721e9207ba8081af178fc6c5
3 879f67854faddcf4a6b236e14d1eb4352f648c95198a566cd53648270ee523c2
4 585947e1eae45d23285879bf1e321a5dbedd06bb7f51c31fb4359676e3f6be39
5 efad1a1517b6f9c0b868ccc5fc97b472bfaf595d1ad4e50f5616b3e932d0928d
6 77b58a7f47f996b4af7ee64f89b974a4e1bc25c7c9117fb136657b50098458dc
7 4c71821e5bd5cdf69d1742674f04380645fdd083d90a3e57414294d383eec5d9
```

`row_incremental_update_count` is `72,110,116,164,178,242,264 = 2*(n_terms + n_target)` with targets on rows 2,4,6,7. That is T+F once (the JSON does not count M1’s extra T).

Required inspections:

| Check | Result |
|---|---|
| `Fraction(str(raw_coefficient))` | Identical to `tail_text` line 133. All 569 JSON values are strings |
| Coefficient-index orientation | `monomial[:7] → F0..F6`, `monomial[7:] → K10,K6,K2`. Same as `term_text` |
| Cached powers | `Fpow e = r(Fpow{e-1} * F)` for `e≥2`. Ring homomorphism |
| `k10/k6/k2` mapping | `load_names=("K10","K6","K2")`, `load_weights=(2,6,10)` = frozen `LOAD_WEIGHTS` |
| `Lambda → sigma^2` | V8 emits `sigma^{2*lambda_power}`; V0R1 emits `(sigma^2)^{lambda_power}`. Same polynomial |
| Target-row terms | `sigma^{2*(12+row)}*(mu2|mu4|mu6|J/4)` on rows 2,4,6,7. All exponents `≥28>12`, hence `r=0` |
| Legacy formula-text comparison | Holds, and is tautological as a schedule lock (M2) |

The emitted evaluation is not the V7 one-line `qring` assignment. It is the same 569-term dictionary, evaluated by reduced recurrence in the parent ring.

---

## 3. Incremental reduction is the image in `R/(sigma^13)`

`I = (sigma^13)` is a monomial ideal; `sigma` is first in `dp`; the leading term of `sigma^13` is `sigma^13`. Remainder `r` is the unique representative of `sigma`-degree `<13`, and `r` is a ring homomorphism onto that span with product `r(ab)`. Therefore

```text
r(r(a)*r(b)) = r(ab),     r(r(a)+r(b)) = r(a+b).
```

Normalizing source atoms and cached powers cannot change the quotient image. A factor whose complete image is already in `I` (every `k2`-loaded monomial `Lambda^{10} → sigma^{20}`, every target `sigma^{≥28}`, `k6_1` after `k6`’s `sigma^{12}`) is correctly lost: its quotient image is zero. That is the inactive-custody requirement, not a missing dependency.

There is no division during formula construction. Extraction divides the already-reduced `TPhi` by `sigma` through grades `0..12`, with multiply-back `sigma*TQ == TRem` fail-closed in the parent ring. In the parent ring `Ann(sigma)=0`, so this is exact coefficient extraction of `r(Phi)`, not a `qring` annihilator quotient.

`diff(TPhi, x)` for `x ≠ sigma` does not raise `sigma`-degree. Characteristic bound 72 is below all three primes, so there is no `p`-power kernel on any tested atom. Support of `r(Phi)` is the support of the unique normal form.

M1’s second `TPhi` is the same schedule run again after those tests. It does not feed `Keep`, `dep_*`, or maps.

---

## 4. Transformation logic and censuses

| Census | Status |
|---|---|
| Exact `qring Q=PrefixIdeal;` replacement | Holds; any other spelling fails the later `qring ` ban |
| `T_RS0_IMPLEMENTATION` rewrite | Holds; V6 token replaced by `ROW_SHARD_INCREMENTAL_NF_V8` plus prefix-algebra / qring-disabled prints |
| `SOURCE_POLY` wrap of `T_*`/`F_*` | Holds on the V7 source block |
| `TPhi=` / `FPhi=` replacement | Formula lines replaced; combined release line also replaced (M1) |
| Staging → output path replacement | Holds; harvested `write(...)` targets the job `compiled/` directory |
| 83 `if (diff(TPhi,` per row | Holds on all 28 programs. M1 does not add diffs, so this census does not see the extra schedule |
| Explicit-NF canary | One per row; `explicitNF` in the product gate |
| Numeric `quit(` removal | `quit(91)` rewritten to `quit;`; surviving `quit(` fails compile |
| Retained coefficients | Rows 2,3,6 write the six `Keep*` files; prepare checks the written sentinels and `SAFE_POLY` text |
| Formula/update hashes | Identical across four lanes; pair hashes independently reconstructed |

`PrefixNF` count on row 1 is 516, well above the `<10` floor.

---

## 5. Both validators fail-closed; no failed-row `DISCOVERY.json` path

`run_aws.sh` is a linear gate: compile `rc=0` → seven row engines all `rc=0` (timeout 124 aborts before prepare) → prepare → certificate engine `rc=0` → finalize. `DISCOVERY.json` is written only at the end of `finalize_discovery_v8.py`, after every check.

Prepare (`prepare_certificate_v8.py` + frozen V6 helpers):

- compiler JSON: status, implementation, characteristic, `prefix_algebra`, `qring_used=False`, incremental flag, 76/85/72, candidate and inactive lists vs frozen V2 tuples, v8 tag prefix, seven row hashes;
- each row: input hash, AWS meta `rc=0` and transcript binding, `transcript_values` rejects `T_RS0_FAIL=` and `? ` diagnostics, `unique()` on scope/implementation/prefix-algebra/qring-disabled/explicit-NF/incremental/shard-row/maps/endpoint;
- grade bit vs term-count `bit == (count>0)`, OR-accumulated;
- 83 dependency bits OR-accumulated; any inactive `1` fails;
- negative controls must be detected globally (`wrong_literal |=` and `synthetic_omission |=`, then both required `==1`);
- keep sentinels only on rows 2,3,6;
- empty discovered set or all-zero grades fail.

Finalize:

- pre status, implementation, characteristic, compiler and certificate input hashes;
- no `qring `/`quit(` in the certificate;
- certificate meta `rc=0` and transcript binding;
- `T_RS0_FAIL=` / `? ` rejected;
- `unique()` on scope, prefix-algebra, frozen cert, omit control, four Delta flags, endpoint;
- `delta_nonzero == (quotient_terms > 0)`.

A fidelity failure prints `T_RS0_FAIL=...` and `quit;` before `ENDPOINT`. Prepare then fails on `T_RS0_FAIL=` and on `unique(ENDPOINT)`. A missing row artifact, hash mismatch, duplicate sentinel, inactive hit, or certificate recombination failure never reaches the `DISCOVERY.json` write. I found no path from a failed row or failed control to that file.

Residual, not a present hole: M1’s `// ** redefining` comments are not treated as diagnostics; `quit;` maps to engine `rc=0` and is caught one gate later; finalize trusts `AGGREGATE_PRE.json` rather than re-parsing row transcripts (those transcripts are hash-bound inside `row_records` and `EVIDENCE.sha256`).

---

## 6. Four-lane payloads and the exact-Q identity

After deleting characteristic and evidence-path fields, every mathematical field of the four `DISCOVERY.json` files is identical: `common_sigma_order=10`, the 23-name manifest, all other candidate bits 0, all seven inactive bits 0, `grade_nonzero` only at 10/11/12, identical `term_counts`, `delta_nonzero=true`, `delta_quotient_terms=4`, both negative controls 1, status `PASS-T-RS0-ROW-SHARD-INCREMENTAL-NF-V8-NAVIGATION-ONLY`, scope `SOURCE_FIDELITY_DISCOVERY_MOD_SIGMA13_ONLY_NO_REES_CHART_OR_ORDER2_VERDICT`.

Compiler JSON: `qring_used=false`, formula hashes and update counts identical, tails/canonical/V7/V6/reviewed/review/prereg hashes identical.

All five validation files per lane record `rc=0`; finalize appends `PASS_T_RS0_ROW_SHARD_INCREMENTAL_NF_V8_NAVIGATION_ONLY`.

Exact-Q `Keep*` polynomials, independently parsed and combined:

```text
FrozenCert = 32768*KeepF12_6 - 35*k*rs^4 + 4096*rs*KeepF10_2 + 8192*cs*KeepF10_3
           = 0

FrozenOmit = 32768*KeepF12_6 - 35*k*rs^4 + 4096*rs*KeepF10_2
           = -1536 * cs * c0 * c1   (and nonzero)

Delta = 32768*KeepT12_6 - 35*k*rs^4 + 4096*rs*KeepT10_2 + 8192*cs*KeepT10_3
      = 5120 * rho^4 * cs^4 * k
      + 2640 * rho^2 * cs^2 * rs^2 * k
      - 4608 * rho^2 * cs * a0 * c1
      - 4608 * rho^2 * cs * a1 * c0
```

`Delta` has only even `rho` powers and vanishes at `rho=0`. `Delta/rho^2` has four terms and equals both claimed forms, including `16*cs*(...)`. This is ordinary rational polynomial arithmetic on the six harvested files, not a Boolean from `DISCOVERY.json`.

Each of the six `Keep*` polynomials, coefficients reduced modulo 32003, 65521, and 1000033, equals the corresponding prime-lane file as a monomial dictionary (5, 3, 5, 1, 9, 4 terms respectively). Certificate `poly Keep*=...` literals equal the `.poly` files on all four lanes.

Certificate transcripts on all four lanes are the eleven expected sentinels, including `DELTA_QUOTIENT_TERMS=4`, with no `FAIL` and no `?`.

---

## 7. Scope fence

This is complete source discovery modulo `sigma^13`.

It is not:

- an actual saturated Rees chart, or a moving-`p` chart;
- a base-change theorem, or a proof that `rho=0` is flat;
- an order-two exclusion, `(8,12)` bound, or maximum-twelve proof;
- a JC2 verdict;
- a claim that the total lift is the frozen identity (it is not: the first correction is a four-term even nonzero `rho^2` multiple);
- a claim that V0R1/V2/V5/V7 engine transcripts are algebraically usable (they are quarantined as `qring` software no-verdicts).

Engine and JSON scope strings remain `DISCOVERY_ONLY_MOD_SIGMA13` / `SOURCE_FIDELITY_DISCOVERY_MOD_SIGMA13_ONLY_NO_REES_CHART_OR_ORDER2_VERDICT` / `PASS_NAVIGATION_ONLY`. This review enforces them.

---

## Next smallest honest obligation

Two successor jobs, in this order:

1. **Software-only, before V8 is imported as a frozen predecessor.** Tighten the `TPhi=` matcher so the stream-release line is not a second formula (`compile_t_rs0_rowshard_v8.py:164`), require uniqueness of that match, and reject `// ** redefining` in row transcripts. No mathematical change.
2. **Mathematical, using this certificate.** An actual saturated `D_+(rs)` Rees / base-change client on the 23-name finite prefix, with ordinary-ring (not `qring`) truncation, taking the four-term `Delta/rho^2` as navigation for the first correction rather than as an obstruction.

Do not promote this package to a Rees, chart, order-two, maximum-twelve, or JC2 verdict. The 23-name support and the four-term exact-Q identity may be frozen as discovery modulo `sigma^13`.
