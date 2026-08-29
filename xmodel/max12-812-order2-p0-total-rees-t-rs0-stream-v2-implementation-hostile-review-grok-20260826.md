# Hostile implementation review: row-streaming `T-rs-0` V2

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_p0_total_rees_t_rs0_stream_v2_20260826/` |
| Charged baseline | Reviewed V0R1 client `cases/max12_812_order2_p0_total_rees_t_rs0_discovery_20260826/` and its Grok implementation review of 2026-08-26 |
| Producer status | **Source/software equivalence only.** This review does not consume any engine transcript, `PASS` marker, `DISCOVERY.json`, live AWS job, or ledger claim |
| Overall verdict | row-streaming equivalent of the reviewed V0R1 mathematical transcript; see the scoped token at the end |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile reread of every charged file. Printed `PASS` tokens are not algebra |
| Method | SHA-256 of every named pin; complete source reading of V2, V0R1, and the transitive compilers/tails; independent reconstruction of the 76+7 manifests; elementary comparison of every formula, gate, and sentinel; attack of row-major accumulation, poly overwrite, and the strengthened validator. No Singular, Sage, msolve, Lean, or local heavy algebra |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

V2 does not re-derive the total family, the grade-12 ceiling, or the frozen dictionary. It imports the pinned V0R1 compiler and emits the same prefix identities one Faber row at a time. The shared sentinels are value-equivalent. The extra streaming sentinels are observational. Nothing larger is proved.

---

## 0. Custody and SHA pins

No `AGENTS.md` exists in or above the repository. Every file charged in the assignment was read completely, including every path in V2 `FREEZE.sha256`, the reviewed V0R1 compiler that V2 imports, that package's preregistration and validator, `run_aws.sh` / `launch_host.sh` on both sides, `ops/aws_exact_lane.sh`, the square-load `tail_text` compiler, the owner `source_coefficients`, and the raw-cusp V2 certificate repair map. Inspection was read-only except for writing this report.

Independently recomputed SHA-256:

| Artifact | SHA-256 |
|---|---|
| V2 `FREEZE.sha256` | `b505f3c51ec8a5e10936119826445d9d2b92e47dd936f6f0996ce13e52b18397` |
| V2 `compile_t_rs0_stream.py` | `5b176dfd0747f3736bc4519077877f4d877b5b726b9701e1b9dcaf56e059a112` |
| V2 `validate_t_rs0_stream.py` | `4ff10d85aeb91f3853a4fd2c89ac2e0fe93bd07fd2c3769241cd8f40afb01949` |
| V2 `PREREGISTRATION.md` | `84361c1e686824d90219b08f46afb6474b75e8416095eb59e39664c0d9ebf3b6` |
| V2 `run_aws.sh` | `c7016857eedc0e4b449cf61b7f21ddffb56ecc6da3f0af230fa615104c775bc6` |
| V2 `launch_host.sh` | `8481a9ffc84ef34b5822bb25b15124b7542fd50561b7ffa18047db9f2ced1911` |
| V0R1 implementation review | `51c294e0ae3d07ced3dac380814d4767bec1e5cc63bd1159cd76ce698f3f69ea` |
| V0R1 `compile_t_rs0_discovery.py` | `3aa6bbbbe539607461c5f27b400aeedd335a4d18e01e40d730f5537da4f45938` |
| V0R1 `validate_t_rs0_discovery.py` | `d05afb4961c071e7ec89a8eb5f850d91aed88ad54b17b1a9965eef52bc9adf1b` |
| V0R1 `PREREGISTRATION.md` | `300faf2a37b587f5dbe21cb3d315957f20b0482516ac7819df04c5a8f51fda80` |
| V0R1 `FREEZE.sha256` | `1fda3e43d7480ff1497ab5abe918d917b7ae1ed2e43ee1c802616743561b616b` |
| owner `compile_p0_cusp_g10_g11.py` | `9d49988213806d42ea4523881595837007fa861369f31fd18d0c83b7adf494d4` |
| raw-cusp V2 `compile_raw_cusp_g12_cech_v2.py` | `8abeda327a7362e0cd5bdc8b73135bc59e1883664e3824783e34c9182743686d` |
| `compile_square_load_ladder.py` | `77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc` |
| frozen `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` |
| canonical tails JSON | `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8` |
| Codex `T-rs` implementation audit | `5e91571d84b1bae92306bad0a31924a2b4fe3bf183ee8d75ace558bc2dd52c0d` |
| Gate-T obligation table | `50db2706f5a8d435618e615bfc393d2eb7dd22828a9a3fa35ac8a2e685ab15c4` |

The four assignment hashes match. All five paths in V2 `FREEZE.sha256` rehash to the printed digest. V2's literal `OLD_SHA256` is the reviewed V0R1 compiler. V2's literal `REVIEW_SHA256` is the charged V0R1 implementation review. `old.EXPECTED` still matches the six transitive pins above. Tail census on keys `'1'`–`'7'` is `36+54+58+81+89+120+131 = 569`. Every frozen tail denominator is a power of two, maximum `2^23`; none of `32003`, `65521`, `1000033` divides any of them. Certificate integers `32768,35,4096,8192,1536` remain nonzero in all three fields (`32768 ≡ 765 (mod 32003)`).

Hash chain at runtime:

```text
V2 FREEZE.sha256
  -> compile_t_rs0_stream.py
       -> OLD_SHA256 -> V0R1 compiler
            -> EXPECTED -> tails, square ladder, owner, raw-cusp V2, audit, gate
            -> EXPECTED_CANONICAL_TAILS
       -> REVIEW_SHA256 -> V0R1 implementation review
```

`run_aws.sh` checks V2 `FREEZE.sha256` before compile. Compile then re-checks `OLD`, the review file, `old.EXPECTED`, the canonical tails digest, and the 569-term census. A swapped V0R1 compiler, review, tail file, or owner source fails closed before any `.sing` is written. V2 `FREEZE.sha256` does not itself list the V0R1 compiler; the pin lives as a literal inside the frozen V2 emitter. That is a valid one-hop chain, not a missing pin.

`launch_host.sh` ships the V2 package, the V0R1 compiler, the three hashed source compilers, `tails.json`, the audit, the gate table, the V0R1 review, and `ops/aws_exact_lane.sh`. Those are exactly the files the hash chain reads. V0R1's own validator and preregistration are not shipped; V2 does not import them.

No engine result is inferred from any live job.

---

## 1. Formula identity: no earliest mismatch

Comparison order is the emission order of the mathematical objects, not print order. No mismatch was found.

### 1.1 Imported formulae

V2 does not copy `source_block`, `series`, `shifted_series`, or `phi_text`. It `exec_module`s the pinned V0R1 compiler and calls those functions. The owner dictionary, the 569-term tail reconstruction, `Lambda -> sigma^2`, and the targets

```text
row 1: 0
row 2: sigma^{28}*mu2
row 3: 0
row 4: sigma^{32}*mu4
row 5: 0
row 6: sigma^{36}*mu6
row 7: sigma^{38}*(J/4)
```

are therefore the reviewed V0R1 strings. Targets remain zero in `R/(sigma^13)`. Load nonlinearity and weight `12+row` are still rejected inside `tail_text`.

### 1.2 Duplicated name lists and the two `p` strings

V2 reconstructs the same Python lists as V0R1:

```text
p_total  = -2*rho^2 + sum_{i=1}^{12} 2*sigma^i*ell_i
p_frozen = 2*sigma^1*ell1 + 2*sigma^2*ell2 + 2*sigma^3*ell3
```

including the harmless `sigma^1` spelling already accepted for V0R1. `source_block("T_", p_total, cs, rs, az, ac, ez, ec, k10, k6, k2)` and `source_block("F_", p_frozen, frozen_cs, ..., frozen_k10, k6, k2)` are the same calls. Frozen `k6` and `k2` still carry `k6_1` and `k2_1`. `frozen_ell` is assigned and unused in both emitters.

The duplication is a drift surface. It is currently identical to V0R1, freeze-pinned, census-checked at 76+7 and 85 unique names, and rejected by the validator if the compiler JSON list is not the hard-coded ceiling. It is not a present mismatch.

### 1.3 Ring, qring, variable order

```text
variables = [sigma, rho] + ell + cs + rs + az + ac + ez + ec + k10 + k6 + k2 + targets
ring R = characteristic, (variables), dp
qring Q = std(sigma^13)
```

Same 85 names, same order, same `dp`, `sigma` first. The leading term of `sigma^13` is `sigma^13`. Prefix arithmetic is unchanged.

### 1.4 Row identities, extraction, and controls

For each row `r = 1..7` the streaming body is the V0R1 body with reusable names:

| V0R1 | V2 |
|---|---|
| `TPhi{r}`, `FPhi{r}` | `TPhi`, `FPhi` assigned from the same `phi_text` |
| `TSpec{r}=subst(TPhi{r},rho,0)` | `TSpec=subst(TPhi,rho,0)` |
| `TSpec{r}-FPhi{r}` -> `prefixMap` | same, OR-accumulated |
| `subst(TPhi{r},rho,-rho)-TPhi{r}` -> `deck` | same |
| `Wrong{r}` with every `ell_i -> 0` | `Wrong` with the same substitutions |
| `subst(TSpec{r},ell1,0)-TSpec{r}` -> `syntheticOmission` | same, before release |
| `subst(TPhi{r},name,0)-TPhi{r}` -> `dep_name` | same, before release, all 76+7 names |
| `TQ0_r=TPhi{r}` then grade-major extract | `TQ=TPhi` then row-complete extract |

The extraction step is the same exact-division loop:

```text
G = subst(Q, sigma, 0)
Rem = Q - G
Q' = Rem / sigma
require sigma * Q' = Rem
```

through grades `0..12`, on both the total and frozen copies, with `coefficientMap` requiring `subst(G_T, rho, 0) = G_F` at every grade. V2 overwrites `TQ` with `Q'` and then checks `sigma*TQ-TRem`; that is the V0R1 identity after the V0R1 assignment `TQ{g+1}=TRem/sigma`. Multiply-back still fails closed as `extraction=0`.

Dependency support is the support of the unextracted `TPhi`. V0R1 computed it after all rows still existed. V2 computes it while the current `TPhi` still exists, then zeros that row. The OR over seven rows is the same bit vector. Inactive names remain `k6_1,k2,k2_1,mu2,mu4,mu6,J`.

### 1.5 Retained cusp coefficients and `Delta`

V0R1 keeps named `Tg10_2, Tg10_3, Tg12_6` and the frozen `Fg*` twins. V2 copies those six polynomials before the next grade and before row release:

```text
(grade,row)=(10,2) -> KeepT10_2, KeepF10_2
(grade,row)=(10,3) -> KeepT10_3, KeepF10_3
(grade,row)=(12,6) -> KeepT12_6, KeepF12_6
```

The certificate strings are the reviewed V2 identities with those names substituted:

```text
FrozenCert = 32768*KeepF12_6 - 35*k*rs^4 + 4096*rs*KeepF10_2 + 8192*cs*KeepF10_3
FrozenOmit = 32768*KeepF12_6 - 35*k*rs^4 + 4096*rs*KeepF10_2
Delta      = 32768*KeepT12_6 - 35*k*rs^4 + 4096*rs*KeepT10_2 + 8192*cs*KeepT10_3
```

`frozenCert`, `frozenOmit` (`==-1536*cs*c0*c1 && !=0`), `deltaSpecial`, `deltaEven`, `deltaRho2`, `deltaMultiplyBack`, and recorded `deltaNonzero` are unchanged. `Delta=0` is still allowed. V2 additionally prints `size(DeltaQ)`; that is an observational sentinel, not a formula change. The multipliers are the repaired V2 numbers `4096, 8192, 1536`, not the false V1 numbers `8192, 32768, 6144`.

### 1.6 Pass gate and scope strings

The product gate is the same twelve factors:

```text
prefixMap * deck * wrongLiteralDetected * extraction * coefficientMap
* frozenCert * frozenOmit * deltaSpecial * deltaEven * deltaRho2
* deltaMultiplyBack * syntheticOmission
```

`deltaNonzero` is not in the product. Failure prints `T_RS0_FAIL=SOURCE_FIDELITY_OR_CONTROL` and `quit`s. Success prints `T_RS0_DISCOVERY_ENDPOINT=PASS_NAVIGATION_ONLY_MANIFEST_NOT_FROZEN`. Scope remains `DISCOVERY_ONLY_MOD_SIGMA13_NO_REES_OR_CHART_VERDICT` in the engine and `SOURCE_FIDELITY_DISCOVERY_MOD_SIGMA13_ONLY_NO_REES_CHART_OR_ORDER2_VERDICT` in both JSON contracts.

Streaming-only additions, none of which alter the shared math:

- `T_RS0_IMPLEMENTATION=ROW_STREAM_V2`
- `T_RS0_ROW_{r}_STREAM_RELEASED=1` after zeroing the working row
- `T_RS0_DELTA_QUOTIENT_TERMS`
- compiler JSON field `implementation`

Print *order* of `T_RS0_TERMS_{g}_{r}` is row-major rather than grade-major. The validator keys by name. Byte-identical stdout is not claimed and is not required for transcript equivalence.

Earliest mismatch: none.

---

## 2. Row-major accumulation and poly overwrite

### 2.1 Common order and grade support cannot latch early

The attack that would misstate common order is: latch `commonOrder` after row 1's thirteen grades, then ignore a later row that is nonzero at a strictly smaller grade.

V2 does not do that. `NZ0..NZ12` are initialized once to `0` before the row loop, set to `1` monotonically, never reset, and only after all seven rows converted to `commonOrder` by scanning grades `0..12` with `orderFound` starting at `0`. That is the same “smallest grade with some `Tg != 0`” as V0R1's grade-major OR. Default `13` (all grades zero) still fails the validator's `0..12` window.

Grade bits are therefore the OR over rows of `Tg_{g,r} != 0`. Term counts are `size(Tg_{g,r})` at the same moment. Rows do not share working polynomials across the row boundary: the release list zeros `TPhi,FPhi,TSpec,Wrong,TQ,FQ,Tg,Fg,TRem,FRem` after each row, and the next row assigns `TPhi` from `phi_text` before any extraction. Source polynomials `T_*` / `F_*` are computed once and never released; they are the common dictionary, not row state.

### 2.2 The six Keep copies are not in the release list

Ordinary Singular `poly` assignment copies (`pCopy`). The interpreter's `reference` / `shared` layer is an explicit `system("reference")` feature and is not used. After `KeepT10_2=Tg`, later `Tg=subst(...)`, `Tg=0`, or `TPhi=0` deletes or replaces `Tg` / `TPhi`, not `KeepT10_2`.

The zero list at row end is exactly the ten working names. The six `Keep*` identifiers are initialized to `0`, assigned only at the three sites above, and then read only by `FrozenCert` / `FrozenOmit` / `Delta`. If a Keep assignment were skipped, those identities would run on `0` and the product gate would fail closed.

Copy-before-release is therefore sufficient for coefficient integrity. It is not a proof that resident memory drops: `poly X=0` replaces the value and is the correct overwrite, but whether the engine returns the old terms to the allocator is a memory-repair effectiveness question, not a transcript question. `kill` is not used. This review does not treat any live RSS sample as evidence.

### 2.3 Extraction overwrite of `TQ` does not corrupt Keep or `TPhi`

Keep is copied from `Tg = subst(TQ, sigma, 0)`, not from `TQ`. Subsequent `TRem=TQ-Tg; TQ=TRem/sigma` changes the quotient for the next grade. `TPhi` is left intact until the explicit release, which is after the dependency bits. That is why V2 can stream rows at all: V0R1 needed `TPhi{r}` to survive until the final dep loop.

---

## 3. Manifests, characteristics, and hash boundaries

Independently reconstructed from the same list algebra as V0R1, then compared to the validator literals by AST:

```text
candidates (76):
  ell1..ell12
  cs, cs1..cs10
  rs, rs1..rs10
  a1, aa1, aaa1, az3..az7
  a0, aa0, aaa0, ac3..ac7
  c1, e1, ee1, ez3..ez7
  c0, e0, ee0, ec3..ec7
  k, k1, k2c, k10_3..k10_8
  k6

inactive (7): k6_1, k2, k2_1, mu2, mu4, mu6, J
```

The two lists are disjoint, and with `{sigma, rho}` they exhaust the 85 ring variables. Validator `CANDIDATES` / `INACTIVE` are order-identical to the compiler lists. `k` / `k1` / `k2c` / `k10_3` and `k2` / `k2c` remain distinct atoms; `subst` is not a string-prefix operation.

Characteristic sets:

| Surface | Allowed |
|---|---|
| V0R1 compiler / validator / `launch_host.sh` | `{0, 32003, 65521}` |
| V2 compiler / validator / `launch_host.sh` / `run_aws.sh` | `{0, 32003, 65521, 1000033}` |

`32003`, `65521`, and `1000033` are prime. The extra prime is a later confirmation characteristic, not a change to the total family. It does not appear in V0R1, so a V0R1 validator cannot parse a `p1000033` job; the V2 validator can. Formulae do not depend on which of these four values is written into `ring R=...`.

AWS tag prefix is now mandatory: `max12_812_order2_p0_total_rees_t_rs0_stream_v2_`. A reused V0R1 lane tag fails `require_aws`. `run_aws.sh` still exports `JC2_REGISTERED_AWS_LANE` before compile, still applies `ulimit -v`, still maps characteristic `0` to filename `q`, still treats engine `124` as `TIMEOUT_NO_VERDICT` without invoking the validator, and still treats nonzero engine rc as `FAIL_ENGINE`. Compile output is `t_rs0_stream_{label}.sing`, not the V0R1 `t_rs0_discovery_` name.

`T_RS0_SOURCE_HASHES=PASS` remains a hardcoded engine print after Python already hashed. Same V0R1 residual; the actual hash checks are in Python.

---

## 4. Attack of the strengthened validator

The V0R1 review named three parser repairs. All three are present. Additional gates are noted.

| Attack | What V2 actually does | Outcome |
|---|---|---|
| Forged stdout, compiler JSON left intact | Requires `meta.rc=0` and `meta.stdout_sha256 == sha256(stdout)` from `aws_exact_lane.sh` | **Holds against an unmatched handmade stdout.** A pair of forged stdout *and* matching meta is still a parser, not algebraic replay; that remaining hole is custody of the job directory after the lane returns |
| Altered compiler JSON | Status must be `PASS-T-RS0-DISCOVERY-COMPILER`; `implementation` must be `ROW_STREAM_V2`; characteristic must match; `input_sha256` must be the `.sing` that is passed in; candidate/inactive lists must equal the hard-coded tuples; census must be 76 and 85 | **Holds.** Dropping `implementation`, swapping a `.sing`, or editing the JSON list fails |
| Omitted candidate (`ell12` dropped from JSON) | `tuple(compiler["candidate_manifest"]) != CANDIDATES` | **Holds.** A missing `T_RS0_DEP_ell12` in stdout also fails the Boolean dep check |
| `GRADE_g_NONZERO=1` with all seven term counts 0, or the opposite | `bit != int(grade_sum > 0)` | **Holds.** This is the V0R1 hole, closed. Engine-side `Tg!=0` iff `size(Tg)>0` on a reduced polynomial, so a genuine V2 transcript is not rejected |
| Stale metadata | `stdout_sha256` must match the file being parsed; duplicate meta keys fail in `parse_meta` | **Holds against a meta/stdout mix-and-match.** Replaying an entire old `(stdout, meta, .sing, result.json)` tuple would still parse; that is transcript replay, not a new algebra |
| Duplicate sentinels | `unique()` requires exactly one expected value; grade/dep/delta bits reject any list other than `["0"]` or `["1"]`; term counts and `DELTA_QUOTIENT_TERMS` require length 1 | **Holds** |
| Zero `Delta` | `DELTA_NONZERO` is recorded, not a pass gate; cross-check is `delta_nonzero == (quotient_terms > 0)` | **Holds as designed.** `Delta=0` with `size(DeltaQ)=0` is allowed. `DELTA_NONZERO=1` with `QUOTIENT_TERMS=0` fails |
| Nonzero `Delta` with failed `rho^2` division | Product gate prints `T_RS0_FAIL=` and `quit`s before `DISCOVERY_ENDPOINT` | **Holds.** Validator also rejects `T_RS0_FAIL=` anywhere |
| Timeout | `run_aws.sh` writes `TIMEOUT_NO_VERDICT` and exits 124; validator is not invoked | **Holds** |
| Engine diagnostic | Any line starting `? `, or `T_RS0_FAIL=` anywhere, fails before sentinel equality | **Holds** |
| Missing row-release sentinel | `T_RS0_ROW_{r}_STREAM_RELEASED` must be exactly `["1"]` for `r=1..7` | **Holds.** A truncated stream that never released row 7 cannot pass |
| Empty discovered set / inactive `dep=1` | same as V0R1, now over the hard-coded inactive tuple | **Holds** |
| `commonOrder=13` | not in `0..12` | **Holds** |
| Garbage `int(...)` | `ValueError`, nonzero exit, `FAIL_STREAM_PARSER` | **Holds** |

The validator is still a fail-closed *parser*. It does not replay the `.sing` file. It does not check `meta.lane` against the AWS tag, does not check a characteristic field inside meta (the lane meta has none), and does not re-hash `OLD_SHA256` from the compiler JSON. Those are residual custody gaps one layer above the named repairs. They do not restore the V0R1 holes that V2 was asked to close.

---

## 5. Defect classification

**Math/source defect.** None. The total/frozen dictionary, seven rows, targets, quotient grades, dependency bits, both negative controls, six retained cusp coefficients, `Delta` identities, and the twelve-factor pass gate match the reviewed V0R1 client. Row-major evaluation commutes because rows are independent polynomials in a shared source dictionary.

**Software/custody defect.** None that break equivalence or reopen a named validator hole. Residuals, not repairs owed before using V2 as a streaming stand-in:

1. Name lists are duplicated in V2 rather than read from the imported module. Currently identical and hard-coded in the validator.
2. `FPhi` remains a parallel `source_block` rewrite, not a call into `owner.source_coefficients()`. Inherited from V0R1 and still closed for the three pinned cusp rows by `FrozenCert` / `FrozenOmit`.
3. The parser cannot stop an attacker who rewrites both stdout and the lane meta after `aws_exact_lane.sh` returns.
4. `poly X=0` is the release mechanism; transcript integrity does not prove a memory drop.
5. Characteristic `1000033` is an added later-confirmation prime, not part of the reviewed V0R1 argparse set.

**Scope wording defect.** The V2 preregistration says the three cusp coefficients are “copied before each row is released.” The code copies only at `(10,2)`, `(10,3)`, and `(12,6)`, which is the correct and smaller statement. Engine and JSON scope strings remain discovery-only and do not claim a Rees, chart, or order-two verdict. Compiler JSON status is still `PASS-T-RS0-DISCOVERY-COMPILER`; the stream validator requires that string plus `implementation=ROW_STREAM_V2`. That naming is slightly stale and not a math claim.

A later human comparing a V2 stdout to a V0R1 stdout must compare shared keys, not lines. Term-count print order and the three streaming-only sentinels will differ even when the mathematics agree.

---

## Firewall

This review licenses treating the frozen V2 emitter as a row-streaming evaluation of the reviewed V0R1 discovery transcript, under the same `sigma^13` prefix ring, the same 76+7 ceiling, and the same polynomial identities. It does not prove:

- that any V2 or V0R1 job has already passed, or that any future `PASS` marker is algebra;
- that resident memory is lower than V0R1 on any host;
- Gate T for `T-rs`, or any other standard chart;
- that `rho=0` is flat, or that saturation commutes with the specialization;
- emptiness of `V(J1+J2)`, the seven residual `A` shards, or the `D(rho)` overlap;
- `k10=0`, another load ray, another square-normal cone;
- order two, `(8,12)`, maximum twelve, moving-`p`, or JC2.

The compiled scope string is `SOURCE_FIDELITY_DISCOVERY_MOD_SIGMA13_ONLY_NO_REES_CHART_OR_ORDER2_VERDICT`. This review enforces it.

GO_STREAM_EQUIVALENT

This is no Rees, moving-`p`, order-two, maximum-twelve, or JC2 theorem.
