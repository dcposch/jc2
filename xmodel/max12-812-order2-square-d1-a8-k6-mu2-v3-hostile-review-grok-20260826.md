# Hostile review — D1 `a=8` complete `k6`/`mu2` transition V3

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_a8_k6_mu2_fullsupport_v3_k60count_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers, V1/V2 names, and prior reviews are not authority |
| Method | source reading, SHA-256 of every named pin and evidence file, compiled-script inspection, and hand identities only; no Singular, Sage, msolve, Lean, package compiler, CAS, or substantive exact Python |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the three required primary pins match. Every path named in `FREEZE.sha256` (10 rows) and `EVIDENCE.sha256` (32 rows) rehashes to the printed digest. Nested `compiled.sha256` rows on both lanes rehash to the retrieved V3 scripts and `result.json`. Frozen V1 and V2 pins inside `compile_v3_k60count.py` / `REGISTRATION.md` rehash, as do both ancestor freezes, both negative-control notes, the V1 freeze rows, and the V1 exact-Q / `F_65521` compiled inputs retrieved as `compiled_frozen_v1/`. The `/tmp` source archive recorded in launch metadata was not retrieved; the repository freeze and the 32 evidence files are the custody. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

V1 is immutable and fail-closed: both AWS engines returned `rc=0`, the `D(k60)` client printed every source/row/numerator sentinel, and the validator rejected the unique required marker `A8QP_SOURCE_DIVISIBLE=1` after the first diagnostic `` `k60` is not defined `` on the positive-valuation support filter. V2 performed the six intended declaration/map insertions and then failed before CAS because its postcondition demanded a global count of six for the repaired string, forgetting the one pre-existing `D(k60)` occurrence. V3 changes only that wrapper check to

```text
old_before=6, new_before=1, old_after=0, new_after=7
```

and its generated input is exactly frozen V1 with those six `k60` insertions. The new symbol has the identity image and is absent from every `V(k60)` equation; the load remains `sigma*k61+sigma^2*k62`.

On `D(p*k10)`, after the reviewed first-normal / half-weight / `M=0` hypotheses, the complete seven-row Faber/source at the fixed contact

```text
ord(A)=8,  ord(C)=9,  ord(R)>=8
```

splits exhaustively on the `k6` jet:

```text
D(k60), grade 26:  S0 = [(3/4) k60 C0 / L]_-
V(k60), grades 27/28:  U0+S0 ; U1+KRC+S1+target(mu2)
```

with

```text
U0  = [(3/4) A0 C0 / L]_-
U1  = [(3/4)((A1 C0 + A0 C1)/L - ell1 A0 C0 / L^2) + (3/8) C0^2 / L^2]_-
KRC = [(5/8) k10 R0 C0 / L]_-
S0  = [(3/4) k61 C0 / L]_-          (on V(k60); k60 C0/L on D(k60))
S1  = [(3/4)((k62 C0 + k61 C1)/L - ell1 k61 C0 / L^2)]_-.
```

No `k2`, extra `k6` (`k6 R^2/L`, `k63`, \ldots), unloaded `A^3`, `k10 R^3` / `k10 A^2`, or `mu4,mu6,J` target enters these windows. On `D(k60)` the first two analytic coefficients are exactly `(3/4)k60 c1` and `(3/4)k60 c0`; seven-row vanishing with `k60` inverted forces `C0=0`, contradicting the contact. On `V(k60)` the first `L`-numerator class is `C0(A0+k61)`. The two shifted root maps exhaust the opposite-root allocations of squarefree `L=z^2+p/2` on `D(p)`. At the shifted-`A` root the moving `U1/S1` connection cancels, every remaining simple pole contributes an extra `L` after `L^2` clearing, and the inverse-Faber image of the grade-28 `mu2` source row has

```text
h2=-mu2,  h4=(p/2)mu2,  h6=-(p^2/4)mu2,
```

whose cleared `L^2` numerator is `-mu2 L` and vanishes at either root. The surviving value is `(3/2) lambda^2 cv^2` in both orientations, nonzero on `D(p)` with nonzero leading `C`. The residual face `A0+k61 \equiv 0` is inside the contact when `k61` is a constant, and is killed by the same double pole: the numerator is `(3/8)C0^2 + L C0 \cdot(\mathrm{deg}\le 1)` and cannot vanish for `C0 \neq 0`. No finite-order normalized arc exists in either listed `k6` section. The statement is arcwise / set-theoretic, not scheme-theoretic, and it does not close `a\ge 9`, positive-order `k10`, `p=0`/`k10=0`, the square branch, order two, `(8,12)`, maximum twelve, or JC2. The exact tied-load Chebyshev/Pell survivor is not contradicted.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Three primary pins | hashes | all three match the required bytes |
| 0. Named manifests | every named file | `FREEZE` 10/10, `EVIDENCE` 32/32, both nested `compiled.sha256` 2/2 |
| 0. V1/V2 immutability | V1/V2 compilers, freezes, negative-control notes, compiled V1 inputs | all six V3-pinned hashes match; V3 `compiled_frozen_v1` byte-identical to the V1 case outputs and to V2 `compiled_frozen_v1`; V1 freeze 4/4; V2 freeze 7/7 |
| 1. V1 fail-closed; V2 six insertions then count-7; V3 wrapper only | diagnostics; byte reconstruction | **holds**; see §1 |
| 2. Ring/map arity; identity `k60`; no qplus constant load | six sites; `k6=sigma*k61+sigma^2*k62` | **holds** |
| 3. Seven-tail reconstruction | frozen Faber, three loads, four targets; `T0+T1`; not Laurent-only affine-`mu2` | **holds** |
| 4. Complete support | grade 26 = `S0`; grades 27/28 = `U0+S0 ; U1+KRC+S1+target(mu2)` | **holds** by binomial orders |
| 5. `SOURCE_SUPPORT_FILTER` | allowed variables exact; `diff` cannot hide a forbidden dependence | **holds** as an upper bound; completeness is the expansion plus row bridge |
| 6. `D(k60)` first two coefficients and `C0=0` | localization `inv*k60-1`; registered chart | **holds** |
| 7. `V(k60)` factor `C0(A0+k61)` | both shifted maps; squarefree `L` on `D(p)` | **holds**, including the `A0+k61\equiv 0` face by degree |
| 8. Inverse-Faber `mu2`; residue `(3/2)lambda^2 cv^2` | `h2,h4,h6`; `-mu2 L`; `U1/S1` cancel at `A0=-k61` | **holds** independently of Laurent-only affine-`mu2` |
| 9. Three deletion controls | each a generically nonzero module | **holds** |
| 10. Exhaustive `k6` sections; `eta` truncation | `D(k60)` vs `V(k60)` with `k61,k62` including zero; no `k63` in-window | **holds**; not an unbounded substitution |
| 11. AWS, exact Q vs `F_65521`, validator | every contact used | **holds** |
| 12. Firewall | no `a\ge 9`, no positive-order `k10`, no `p=0`/`k10=0`, no fan/order-two; Pell/Chebyshev not contradicted | **holds** |

---

## 0. Custody

Recomputed SHA-256 of the three required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `67e0c08119e67d410904e63f55b5586131bfa987e4b7d7045c02e24dd6a2e9a7` | producer report |
| `.../FREEZE.sha256` | `dcd6c3eb2d390375f1c56bc638215a4e447efe680a4c5f345c18011945514f7f` | source freeze |
| `.../EVIDENCE.sha256` | `a3a64018a350a61b02ea53aec7edbd56e159eb8def325d78d05fbd59ecb1effb` | evidence freeze |

`FREEZE.sha256` names ten files, all matching:

| Path | SHA-256 |
|---|---|
| V3 `REGISTRATION.md` | `fb7a9d434cb60dc50d9f28319c0abb623c8e8cba7d46a69e6503859f8a86ec44` |
| V3 `compile_v3_k60count.py` | `ad8b61a08fc931ad09f609b823544af46fe5ccc1aff2739f22a41ace7b36868a` |
| V3 `run_aws.sh` | `9181d69493500412054b1caf046bde0674cb21bfe356cd5249e62c2bb270bd61` |
| V3 `launch_host.sh` | `78bb5ee36a50bf5f1a7fe6d99ea4fd435f6faeaa3526fc614ab05a890be5d792` |
| V1 `compile_a8.py` | `0230ca443d49e47b5d6ebae8c0f8a88d31a793d13b1df59e3698e166226d177b` |
| V1 `FREEZE.sha256` | `c18bdd9f55a108470ef166e6c0cfa243ab61b63f45742537046fdb6e583b5dc8` |
| V1 `RESULT_NEGATIVE_CONTROL.md` | `be3d6843a27db31ee7e844fe1edea1e2f6fb7b65ba9b7c8f2289ff28e3441ed2` |
| V2 `compile_v2_k60symbol.py` | `7cc1b281f24ed8f138aab12ad7e0412c57ce441f5aa28d57eaec14dc998a28e9` |
| V2 `FREEZE.sha256` | `297a9bb5ceb76e0dda740a0b498902e497af9f7c74af96dd3b757ceb209ae9a1` |
| V2 `RESULT_NEGATIVE_CONTROL.md` | `db3c28f81f4bdbf422af87fa85e09f9d3f916292c387552b54ddad4e0e71a9f8` |

`EVIDENCE.sha256` names 32 files; all 32 rehash. Both nested `compiled.sha256` files rehash to the retrieved V3 `.sing` and `result.json`.

V1 freeze 4/4 rehashes. V2 freeze 7/7 rehashes. The V3-retrieved `compiled_frozen_v1` scripts are byte-identical to the original V1 case compiled inputs and to V2's `compiled_frozen_v1`:

| Lane | SHA-256 |
|---|---|
| exact Q | `4507695e088dbbae4c57a822add0db649df75313506d73d3d82049af205b8780` |
| `F_65521` | `f9de56c5d8f924e5d1bd9604734a5a2c4fe65abe9abcbc91cce3ffbf31eef695` |

Ancestry pins consumed by V1 also rehash: base `compile_r1_d1_ac.py` `e024a13d…`, its freeze `34b0f325…`, the V12 source-support erratum `997dda08…`, first-normal promotion `40790378…`, closure criterion `3c0a33ce…`, CGE3 compiler `352ad4f2…`, load-ladder `77f25216…`, `tails.json` `d72f774c…`, canonical all-tails `6eed03d4…`. All seven Faber rows contain `k10`, `k6`, and `k2` monomials (counts `(12,4,1)`, `(18,7,2)`, `(19,7,2)`, `(27,10,4)`, `(30,11,4)`, `(40,16,7)`, `(44,17,7)`); every monomial has weight `12+row` and load-linear.

Exact Q and `F_65521` are genuinely separate frozen runs.

| Charge | Exact `Q` (Box03) | `F_65521` (r6d) |
|---|---|---|
| Host | `ip-172-30-0-249` | `ip-172-30-0-45` |
| Tag | `…_v3_k60count_q_20260826T124500Z_box03` | `…_v3_k60count_p65521_20260826T124500Z_r6d` |
| Characteristic | `0` in all three rings | `65521` in all three rings |
| V3 compiled script SHA | `58a4145216694293c7af91b6368330777a6f9f2a414380b5ff47d87c1eb5e941` | `3b0bdf6fc0f70777a265a9d32a577059266bbbb1386b02fc05da2b39a7ec1a22` |
| V1 compiled script SHA | `4507695e…` | `f9de56c5…` |
| Counts | `old_before=6, new_before=1, old_after=0, new_after=7` | same |
| Engine `rc` | `0` | `0` |
| Validator | `PASS_D1_A8_K6_MU2_V3_K60COUNT` | `PASS_D1_A8_K6_MU2_V3_K60COUNT` |
| Stdout SHA | `4a1f5e8c4aac59e6ec2fa22f167ebc0c95b85395d772e17ee0f4c54658084186` | same sentinel payload |
| Stderr SHA | `f20a42779abebb0f0f0a3379316b2dec4ef283575fb86569616e8fdca6f86d1f` | `141a07b6d9874073b12dade3b21092b9e79ba3e09301c4d562f9ae148731ba6a` |
| Peak RSS / swaps | 14,936 KiB / 0 | 12,876 KiB / 0 |
| User / elapsed | 0.04 s / 0.05 s | 0.03 s / 0.03 s |

The two V3 compiled scripts differ by exactly the three ring-characteristic tokens (`Rq0`, `Rqp`, `Eqp`). Substitutions, maps, recurrences, and sentinels are otherwise identical. The two validation files are byte-identical (`engine_rc=0` plus the same validator line), hash `ba874320…`; that common payload is not evidence that the runs were copied. Identical stdout is expected: on success the script prints only `0/1` markers. Both `freeze_check.stdout` records report every `FREEZE` row OK. Both metas record `argv` as `timeout 1800 Singular -q` on the lane-local V3 script, return code 0, and stdout hashes matching `EVIDENCE.sha256`. Caps were 24 GiB virtual (`25165824` KiB), 600 s compile, 1800 s engine. Compiler stderr is the empty-file digest `e3b0c442…` on both lanes. The validator rejects `=FAIL`, `// **`, a leading `?`, and `error occurred`. Neither stdout nor stderr contains those patterns.

A passing manifest is not a mathematical verdict. The algebra below is independent of those sentinels.

---

## 1. V1/V2/V3 custody

V1 is pinned by digest and was re-emitted unchanged as `compiled_frozen_v1/` on both V2 and V3 lanes. It is AWS-only, refuse-if-exists, and pin-checks the r1/d1 base, the V12 erratum, first-normal, and the imported CGE3/load-ladder/tails pins before writing. Both V1 engines returned `rc=0`. Source extraction at `D(k60)` passed (`SOURCE_DIVISIBLE`, `SOURCE_QUOTIENT_IDENTITIES`, `SOURCE_SUPPORT_FILTER`, `ROW_IDENTITIES_26`, numerator coefficients, `DK60_FORCES_C_ZERO` all printed `1`, endpoint `PASS_A8_Q6_ZERO_SIMPLE_POLE`). The fail-closed validator rejected the unique required marker `A8QP_SOURCE_DIVISIBLE=1`. Exact-Q / `F_65521` stdout hashes are `1c84808a…` / `87021880…`, matching the V1 negative-control note. The first diagnostic in both fields is

```text
? `k60` is not defined
```

immediately followed by a cascade at `poly A8QP_Rem28_1=…`. The positive-valuation ring, target ring, and four maps omit `k60`, while `extract_source` differentiates the support filter with respect to that symbol. Engine `rc=0` is therefore not a mathematical `V(k60)` endpoint.

V2 runs frozen V1, then replaces the unique token

```text
b0,b1,k0,k61,k62,k2load
```

by

```text
b0,b1,k0,k60,k61,k62,k2load
```

and refuses unless the old string occurs exactly six times and the new string occurs exactly six times after replacement. Frozen V1 already contains one legitimate occurrence of the new string in the `D(k60)` ring, so the correct global count after repair is seven. Both AWS compilers raised `RuntimeError: V2 formal-k60 replacement failed` with `compiler_rc=1` (stderr hashes `e1c2a465…` / `7a0a2c25…`, validation `f5d6f1d5…`). No Singular process was launched. This is only a wrapper assertion error.

V3 versus V2 differs by: pinning V2; replacing the postcondition by the four-tuple `(6,1,0,7)`; recording those counts; and renaming status/output. The replacement token is unchanged. Byte reconstruction `V1.replace(old, new)` equals the corresponding V3 script on both lanes. Lengths grow by 24 characters (`6` insertions of `k60,`). The old token is absent from V3; the new token occurs seven times. Nothing else in the generated Singular bytes changes.

---

## 2. Ring and map arity; identity `k60`; no qplus constant load

The six repaired sites in the V3 exact-Q script are:

```text
152  ring Rqp=0,(…,b0,b1,k0,k60,k61,k62,k2load,…,rtx,aua,cvg),dp;
437  ring Eqp=0,(…,b0,b1,k0,k60,k61,k62,k2load,…,rtx,aua,cvg),dp;
438  map A8QP_posmap=Rqp,…,b0,b1,k0,k60,k61,k62,k2load,…;
439  map A8QP_negmap=Rqp,…,b0,b1,k0,k60,k61,k62,k2load,…;
440  map A8QP_posrootmap=Rqp,…,b0,b1,k0,k60,k61,k62,k2load,…;
441  map A8QP_negrootmap=Rqp,…,b0,b1,k0,k60,k61,k62,k2load,…;
```

plus the pre-existing `Rq0` occurrence (the seventh new-string count). Each qplus ring has 28 variables; each map has 28 images, with `k60` in the same slot as the ring variable, hence the identity image. V1 qplus rings/maps have 27 slots and no `k60`.

On `V(k60)`, compiled loads and the analytic comparator use exactly `(sigma*k61+sigma^2*k62)`. After line 152 the only `k60` tokens are the two ring declarations, the fourteen support-filter `diff(g,k60)` tests, and the four identity map images. No qplus `Phi` and not `A8QP_Hshift` contains `k60`. There is no accidental constant `k60` load. On `D(k60)` the load is the full jet `(k60+sigma*k61+sigma^2*k62)`, as required for that section.

---

## 3. Seven frozen Faber/source tails, not Laurent rows

`extract_source` emits, for each of the seven rows, `tail_text` of the frozen Faber row with

```text
loads = {k10: k0,  k6: (k60+sigma*k61+sigma^2*k62) on D(k60)
                   (sigma*k61+sigma^2*k62)          on V(k60),
         k2: k2load},
targets = {1: 0, 2: mu2, 3: 0, 4: mu4, 5: 0, 6: mu6, 7: J/4},
```

subtracting `sigma^{2(12+row)}` times the target when the target is nonzero. Compiled `A8Q0_Phi1..Phi7` and `A8QP_Phi1..Phi7` are those expansions. Every tail row contains `k10`, `k6`, and `k2` monomials (§0). Weight bookkeeping in the ladder is `Lambda^{2,6,10}` for `(k10,k6,k2)`, i.e. `sigma^{4,12,20}`, matching `sigma^4 k10 f^{5/4}`, `sigma^{12} k6 f^{3/4}`, `sigma^{20} k2 f^{1/4}`. Compiled `Phi` ends are `-sigma^{28}*(mu2)`, `-sigma^{32}*(mu4)`, `-sigma^{36}*(mu6)`, `-sigma^{38}*(J/4)` on the even target rows, identically on both sections.

`source_coefficients` realises `f=K^2+sigma^5 D` with `K=L^2+sigma^2 R`, `D=LA+C`, `L=z^2+pp/2`, `pp=p+2 sigma ell1`, after the documented factors 2 and 4. Outer `sigma` then contact `sigma`:

```text
kc = sigma^2 * rz,   rz = sigma^8 * eta * b1
kr = (pp)^2/4 + sigma^2 * rc,   rc = sigma^8 * eta * b0
n3 = sigma^3 * az,   az = sigma^8 (a1+sigma aa1)
n1 = sigma^3 ((pp*az)/2 + cz),   cz = sigma^9 (c1+sigma cc1)
```

and cyclic in the constant terms. Compiled `Phi` display these compositions explicitly (`sigma^2*((sigma^8*eta*b1))`, `sigma^9*(c1+sigma*cc1)`). No doubled or dropped outer `sigma` after the contact substitution. Quotient extraction is `Phi / sigma^{26}` on `D(k60)` and `Phi / sigma^{27}` on `V(k60)`, with a `reduce` divisibility check and the polynomial identity `sigma^g Q = Phi`, then one further exact `/sigma` step to the next grade on `V(k60)`.

This is not a Laurent-only affine-`mu2` client. The affine-`mu2` receiver integerizes Laurent coefficients of `H=sqrt(Q)(Q^2+beta Q+gamma)` with a factor `1024` in `E2`. Here the `mu2` target lives on Faber row 2 of the frozen source, and the analytic comparator is the inverse-Faber image of that row (§8). The moving bridge is `T0+T1` (§5), not a Laurent coefficient dump.

---

## 4. Complete source sigma support at `a=8`

Write `f=L^4(1+\varepsilon)` with `varepsilon=2 sigma^2 R/L^2 + sigma^4 R^2/L^4 + sigma^5 D/L^4` and `D=LA+C`. Binomial expansions, recomputed independently of the producer page:

```text
sigma^{12} k6 f^{3/4}:   (3/4) sigma^{17} k6 C / L     at order 18+a
                         (3/8) sigma^{16} k6 R^2 / L   at order 16+2a
f^{3/2}:                 (3/4) sigma^{10} AC / L       at order 11+2a
                         (3/8) sigma^{10} C^2 / L^2    at order 12+2a
sigma^4 k10 f^{5/4}:     (5/8) sigma^{11} k10 R C / L  at order 12+2a
sigma^{20} k2 f^{1/4}:   (1/2) sigma^{22} k2 R / L     at order 22+a
```

Orders at unit leading `k6`, `k10`, `ord(A)=8`, `ord(C)=9`, `ord(R)\ge 8`:

| term | absolute order | `a=8` | in `D(k60)` window 26? | in `V(k60)` window 27/28? |
|---|---:|---:|---|---|
| `k60 C/L` (`S0` on `D(k60)`) | `18+a` | 26 | yes | no (`k60=0`) |
| `k61 C/L` (`S0` on `V(k60)`) | `19+a` | 27 | no | yes |
| `k62 C/L` and moving-`L` of `k61 C/L` (`S1`) | `20+a` | 28 | no | yes |
| `AC/L` (`U0`) | `11+2a` | 27 | no | yes |
| `C^2/L^2`, moving-`L` of `AC` (`U1`) | `12+2a` | 28 | no | yes |
| `k10 RC/L` (`KRC`) | `12+2a` | 28 | no | yes |
| `mu2` target | 28 | 28 | no | yes |
| `k6 R^2/L` | `16+2a` | 32 | no | no |
| `k10 A^2/L` | `14+2a` | 30 | no | no |
| `k10 R^3/L` | `10+3a` | 34 | no | no |
| `k2 R/L` | `22+a` | 30 | no | no |
| `k63 C/L` | `21+a` | 29 | no | no |
| unloaded `A^3` | `15+3a` | 39 | no | no |
| `mu4,mu6,J` | `32,36,38` | those | no | no |

On `D(k60)`, grade 26 is exactly the simple-pole module `S0`. On `V(k60)`, grades 27/28 are exactly `U0+S0` and `U1+KRC+S1+target(mu2)`. No `k2`, additional `k6`, unloaded, or other target module is in-window. The analytic `Hshift` contains the higher universal summands; they have valuation outside the extracted grades.

---

## 5. `SOURCE_SUPPORT_FILTER`, quotient identities, analytic rows

Forbidden charges are `k60,k61,k62,k2load,mu2,mu4,mu6,J`. Allowed, grade by grade:

```text
D(k60) grade 26:  k60
V(k60) grade 27:  k61
V(k60) grade 28:  k61, k62, mu2
```

Compiled `diff` lines match this: `A8Q0_g26_*` forbids `k61` and every later charge but not `k60`; `A8QP_g27_*` forbids `k60` and `k62` but not `k61`; `A8QP_g28_*` forbids `k60` and `k2load,mu4,mu6,J` but not `k61,k62,mu2`. Any nonzero derivative in a forbidden variable sets `support=0` and quits. A `diff` check cannot hide a forbidden dependence.

The filter is an upper bound. It does not require an allowed variable to appear, and it does not mention `k0` or `eta`. Completeness of `S0,S1,KRC` is the §4 expansion plus the row bridge (and, for `k6` and `mu2`, the source-side negative controls). A missing `k10` term in both source and analytic would not trip the filter; the independent grade table is the check that no such term belongs in the `D(k60)` window, and a source/analytic mismatch at grade 28 would trip `ROW_IDENTITIES_28`.

Exact source identities compiled: `reduce(Phi, sigma^g)=0` and `sigma^g Q_g = Phi`; then `reduce(Q_g - g, sigma)=0` and `sigma Q_{g+1} = Q_g - g`. Analytic divisibility is the same pair on `Hshift`. Both recurrences of §6–§7 are the analytic row identities for a simple pole (`h_{k+2}+(p/2)h_k=0`) and a double pole (`h_5+p h_3+(p^2/4)h_1=0` and cyclic).

---

## 6. `D(k60)`: first two coefficients and `C0=0`

Convention: ordinary coordinates satisfy `h_{\mathrm{row}}=[t^{\mathrm{row}+1}]H` with `H=t F` and `z=1/t`. Then `L=z^2+p/2=t^{-2}(1+\mathrm{sp}\,t^2)` and `1/L=t^2\mathrm{Inv}_1`. Direct polynomial coefficients give `C_{\mathrm{poly}}=c_1 z+c_0`, so `C_t=c_1+c_0 t` and `C_{\mathrm{poly}}/L=t C_t\mathrm{Inv}_1`. The binomial of `sigma^{12} k6 f^{3/4}` contributes `(3/4)sigma^{17} k6 C/L` as the first `C/L` polar piece, so

```text
F_S = (3/4) k6 t C Inv1,     H_S = t F_S = (3/4) k6 t^2 C Inv1.
```

Compiled `A8Q0_Hshift` is that formula with `C=sigma^9 C_t` and the full `k6` jet, hence leading term `(3/4)sigma^{26} t^2 k60 C_t\mathrm{Inv}_1`. At `sigma^{26}` with leading `Inv1=1`,

```text
H = (3/4) k60 t^2 (c1 + c0 t) (1 - (p/2) t^2 + \cdots),
h26_1 = [t^2]H = (3/4) k60 c1,
h26_2 = [t^3]H = (3/4) k60 c0.
```

The remaining five rows are then the simple-pole recurrence `h_{k+2}+(p/2)h_k=0`, i.e. `N/L` with `N=h_1 z+h_2`. Compiled checks are exactly `h26_1-(3/4)k60 c1==0` and `h26_2-(3/4)k60 c0==0`, plus that recurrence. Seven-row vanishing therefore forces `k60 c1=k60 c0=0`. The localization `inv*k60-1` puts `c0` and `c1` in the ideal `(h26_1,h26_2,inv*k60-1)`, which is the compiled `DK60_FORCES_C_ZERO` test. On the registered chart `ord(C)=9`, the leading pair `(c0,c1)` is nonzero: contradiction.

Hypotheses actually used: `k60` invertible; leading `C` of exact order 9; characteristic not `2` or `3` (coefficient `3/4`). `D(p)` is not required for this coefficient identity. `Inv_1` truncated through `t^8` is exact for seven rows. Higher jets `k61,k62` sit at grades 27 and 28 and cannot cancel grade 26.

---

## 7. `V(k60)`: leading factor `C0(A0+k61)` and the two shifted maps

First-grade receiver is `U0+S0`. With `k6=sigma k61+\cdots` and `A=sigma^8 A_t`, `C=sigma^9 C_t`,

```text
H_{U0} = (3/4) sigma^{27} t A_t C_t Inv1,
H_{S0} = (3/4) sigma^{27} t^2 k61 C_t Inv1.
```

The polar numerator of `AC/L` is `AC-a1 c1 L`, so as an `L`-class

```text
Nfirst \equiv (3/4) C0 (A0+k61)  (mod L).
```

`L` divides `Nfirst` iff `L` divides `C0(A0+k61)`. On `D(p)`, `L=z^2+p/2` is squarefree of degree 2. Degree `\le 1` factors force one of: opposite roots of `L`; `C0\equiv 0` (out of contact); or `A0+k61\equiv 0`. Same-root allocation gives `(z-\lambda)^2`, not a multiple of squarefree `L`. Constant `A0+k61` times linear `C0` is degree 1. So the only in-contact solutions with non-constant shifted `A` are the two opposite-root charts

```text
A0+k61 = aua (z \mp lambda),   C0 = cvg (z \pm lambda),
```

which are exactly `A8QP_posmap` / `A8QP_negmap` (`p\mapsto -2\,\mathrm{rtx}^2`, `a0\mapsto \mp aua\,rtx-k61`, `c0\mapsto \pm cvg\,rtx`). Then `C0(A0+k61)=aua\,cvg\,L` and `Nfirst` vanishes identically (the holomorphic subtraction `a1 c1 L` matches `aua cvg L` after the same substitution). Those two maps exhaust the opposite-root allocations for squarefree `L` on `D(p)`.

The residual first-numerator component `a1=0`, `a0=-k61` (constant `A` of order 8, inside the contact when `k61` is a nonzero constant) is not a third root chart: `Nfirst` already vanishes without allocating `C0`. On that face the moving-`L` terms cancel as polynomials, the `C1` simple-pole pair `A0 C1 + k61 C1` cancels, and `mu2` contributes a multiple of `L`, leaving

```text
N = (3/8) C0^2 + L C0 \cdot((3/4)(A1+k62)+(5/8) k0 R0 - mu2).
```

If the second summand is nonzero its degree is at least 2, while if it is zero then `N=(3/8)C0^2`. On `D(p)`, `C0^2` is never a multiple of squarefree `L` for `C0\neq 0` (`(alpha z+beta)^2 = k(z^2+p/2)` forces `p=0` or `C0=0`). This face is therefore empty. It is not a missing hypothesis that breaks the elimination claim; it is the remaining component of the derived factor `C0(A0+k61)`.

---

## 8. Inverse-Faber `mu2` transform, cancellation, residue

The source target on Faber row 2 is `-sigma^{28} mu2`; other target rows sit at grades `32,36,38`. At grade 28 the target increment is therefore `g_2=-mu2` and `g_i=0` for `i\neq 2`. The even connection `T_0` is lower-triangular with ones on the diagonal: `delta=i-j=2n`,

```text
T0 = c p^n,   c = (j/2)(j/2+1)\cdots(j/2+n-1) / (n! 2^n).
```

Solving `g=T_0 h` independently of the programmed `Hshift`:

```text
h1=0,
h2=g2=-mu2,
h3=0  (odd),
h4 = T(4,2) mu2 = (p/2) mu2,     T(4,2)=(1/2)p,
h5=0,
h6 = -T(6,2)h2 - T(6,4)h4 = -(p^2/4)mu2,
     T(6,2)=(1/4)p^2,  T(6,4)=p,
h7=0.
```

This is exactly the compiled comparator `sigma^{28}(-mu2 t^3+(p/2)mu2 t^5-(p^2/4)mu2 t^7)` and the claimed `(h2,h4,h6)`. It is the inverse Faber of a pure row-2 source target, not the Laurent affine-`mu2` integerization `E2-1024 mu2`.

The `L^2`-numerator of a double pole is

```text
Nnext = h1 z^3 + h2 z^2 + (h3+p h1) z + (h4+p h2).
```

The `mu2` contribution is `-mu2 z^2 + ((p/2)mu2 + p(-mu2)) = -mu2(z^2+p/2) = -mu2 L`, a multiple of `L`, vanishing at either root. The next-grade recurrence identities `h_5+p h_3+(p^2/4)h_1=0` and cyclic hold for this triple, so the seven-row `mu2` piece really is of type `N/L^2` with that numerator.

At the shifted-`A` root `A0(\lambda)=-k61`, `L(\lambda)=0`, `C0(\lambda)=\pm 2 cvg \lambda`. Simple poles (`(A1 C0+A0 C1)/L`, `(k62 C0+k61 C1)/L`, `KRC`) contribute an extra `L` after `L^2` clearing and vanish. The `C1` pair `A0 C1 + k61 C1` cancels as polynomials on this face. The two moving-`L` numerator values are

```text
U1:  -(3/4) ell1 A0(\lambda) C0(\lambda) = +(3/4) ell1 k61 C0(\lambda)
S1:  -(3/4) ell1 k61 C0(\lambda).
```

They cancel by `A0=-k61`. The `mu2` numerator `-mu2 L` vanishes. The only surviving value is

```text
(3/8) C0(\lambda)^2 = (3/8)(2 cvg \lambda)^2 = (3/2) \lambda^2 cvg^2.
```

Compiled residue identity is that polynomial on both `posrootmap` (`z\mapsto rtx`) and `negrootmap` (`z\mapsto -rtx`). It is nonzero on `D(p)` with nonzero leading `C`. Sign of `H_{C^2}=(3/8)sigma^{10} t^3 C^2\mathrm{Inv}_2` is positive, matching the positive residue. Both orientations produce the same square.

The moving `T0+T1` bridge used to identify source `g` with this `H` is audited in §5: `row_checks` at grade 27 uses only `T0`; at grade 28 it uses `T0` on current `h` and `T1` on previous `h`. Compiled `Check28_*` match the independent formulae `T1=2 n c ell1 p^{n-1}`. There is no `ell2` in the ring and `T2` is never applied.

---

## 9. Three deletion controls

1. **Delete `T1`.** At grade 28, `g` is compared to the `T0`-only prediction. `t1needed=1` means that prediction fails. `T1` is generically nonzero for every even `i-j\ge 2`, and the first-grade `h` (`U0+S0`) is generically nonzero before allocation (`(1/2)ell1 h27_1` in `Check28_3`). This is a source-row test of a nonzero module, not a presentation artifact. Full `T0+T1` identities are the separate `ROW_IDENTITIES_28` check, so failure of `T0` alone is exactly the moving connection.

2. **Delete `k6 C`.** Source `g` is tested for `diff(-,k61)` on grade 27 or `diff(-,k62)` on grade 28. Combined with the support filter this reduces to: grade 27 depends on `k61`, or grade 28 depends on `k62`. The dependence is in the frozen Faber rows (the `k6` monomials of §0), not in `Hshift`. On `V(k60)` the first-numerator factor `A0+k61` is load-bearing for the allocation.

3. **Delete `mu2`.** Source `g28` is tested for `diff(-,mu2)`. The unique in-window target is the Faber row-2 subtraction `-sigma^{28} mu2`. Deleting it would drop a generically nonzero source monomial and, if left in `H`, would break the row identities. The control is on the source, not a presentation name.

All three controls fail-closed (`product != 1` quits). They delete mathematical modules present in the complete source at this contact, not artifacts of the six-symbol wrapper.

---

## 10. Exhaustive `k6` sections and `eta` truncation

Finite-order or identically zero `k6` means either some jet coefficient is a unit or every coefficient vanishes. Writing `k6=k60+sigma k61+sigma^2 k62+\cdots`:

- `k60\neq 0` is `D(k60)`. Grade 26 already kills, independently of `k61,k62` and of omitted higher jets.
- `k60=0` is `V(k60)`, with `k61,k62` free in the ring and allowed to specialize to zero. Identically zero `k6` is the specialization `k61=k62=0` inside this section: the first numerator reduces to `C0 A0` and the residue is still `(3/2)lambda^2 cv^2`.

Omitted `k63` first produces `k63 C/L` at order `21+a=29`, after grade 28. No unbounded `k6` substitution is used; `a` is fixed at 8 and the jet is truncated by the window.

`R=sigma^8 eta (b1 z+b0)` with `eta` a ring variable. Arbitrary `eta` is the exact grade-8 section, including the closed face `eta=0`. No substitution `eta=sigma^s` occurs. The next `R` jet would first produce a `k10 R_1 C` term at grade `13+2a=29`, after `g+1=28`. Thus `eta=0` is complete through the next grade for every `ord(R)>8`. This is a finite truncation, not a disguised unbounded substitution. `Inv_1,Inv_2,Inv_3` are the binomial series of `(1+\mathrm{sp}\,t^2)^{-1,-2,-3}` through `t^8`; ordinary coordinates run through `[t^8]`, so the truncation is exact for seven rows.

---

## 11. Inversions, exact-Q versus finite field, AWS, diagnostics

Inversions / nonzero contacts actually used:

- `D(p)`: two distinct roots of squarefree `L`, `lambda^2=-p/2`, compiled as `p\mapsto -2\,\mathrm{rtx}^2`.
- `D(k10)`: ambient first-normal reduction to the square; not a factor of the residue `(3/2)lambda^2 cv^2`.
- `D(k60)` on section 1 only: `inv*k60-1`.
- Nonzero leading `C` for exact order 9; nonzero leading `A` (via `aua`) on the opposite-root charts of section 2.
- Characteristic not `2` or `3` (coefficients `3/4,3/8,5/8,3/2` and the `L^2` leading `1/4`). Exact Q is characteristic 0. `65521` is a software control: `2,3,5` remain units; it is not a characteristic-zero proof.

No inversion of `k61`, `eta`, `ell1`, or `L` in the ring: poles are encoded by generating functions and recurrences.

The geometry is arcwise / set-theoretic: two oriented root charts, not a scheme-theoretic initial ideal, not a radical membership, and not a fan cover. Engine `rc=0`, validator PASS, no rejected diagnostic, `/usr/bin/time -v` in stderr, zero swaps, virtual-memory cap 24 GiB, compile/engine caps 600/1800 s, AWS-only compilers, distinct hosts, distinct compiled-script hashes. Tags, PIDs (`219197` / `278616`), and job directories match `AWS_LAUNCH_METADATA.md` and `launch_registration.txt`. Both lanes recorded `characteristic` `0` / `65521` as required.

---

## 12. Firewall and Pell/Chebyshev

The compiled V3 scope string is `SIX_FORMAL_K60_RING_MAP_INSERTIONS_WITH_EXACT_COUNTS_ONLY`. The V1 payload it wraps is `TWO_EXHAUSTIVE_K6_SECTIONS_FIXED_A8_COMPLETE_SOURCE_NO_ORDER2_VERDICT`. `RESULT.md` claims only the fixed `a=8` D1 contact on `D(p*k10)` after the cited first-normal / half-weight / `M=0` gates. It claims no `a\ge 9`, no positive-order `k10`, no `p=0`/`k10=0`, no other face, no zero/infinity receiver, no scheme structure, and no full square / order-two / `(8,12)` / maximum-twelve / JC2 theorem.

At `a=9`, `AC/L` has order `11+18=29` while `k61 C/L` has order `19+9=28` if the valuation of `k6` is again positive; that successor is correctly left open.

The all-load Chebyshev/Pell survivor is the reduced support of `sqrt(Q)(k10 Q^2+k6 Q+k2)` in which `k6` and `k2` are comparable to `k10` and may cancel off the unit-`k10` square (hostile-review confirmed theorem SHA `523a32dd…`, with exact example `Q=z^4-1`, `16Q^2+20Q+5=U_4(z^2)`, `A=T_5(z^2)`). Emptiness of the two listed D1 sections on `D(p*k10)` does not contradict that locus. Later complete-support clients must keep it as a positive control, as `RESULT.md` states.

---

CONFIRMED
ORDER2_SQUARE_D1_A8_K6_MU2_V3_CONFIRMED
