# Hostile review: V20R2 contracted mixed-source compiler

| Field | Value |
|---|---|
| Charged case | `cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/` |
| Charged claim | Exact typed compiler — not a jet or closure theorem — for the normalized K00 seven-row source through `Lambda^19`: contract the universal deformation vector by simultaneous parameters first, then specialize `p=(Lambda^2*k10, Lambda^6*k6, Lambda^10*k2, Lambda^14*mu2, Lambda^16*mu4, Lambda^18*mu6, Lambda^19*Jdet)`; 140 exact literal equations on a 169-column source with five boundary-zero constants and 164 free columns; exact agreement with the contracted syzygy/Kuranishi presentation |
| Overall verdict | **PASS** |
| Scope of PASS | exact source / type / compiler milestone only |
| Smallest failing identity | none |
| Repairs required of the algebra | none |
| Additive custody defects | (1) original R2 `ENDPOINT_EVIDENCE.sha256` self-listing `.tmp` entry, preserved byte-for-byte and repaired additively by `HARVEST_EVIDENCE_R2.sha256`; (2) R0/R1 compiler bytes are not separately archived on the live path, so those two freeze manifests no longer verify against current `compile_contracted_source_v20r2.py` |
| Reviewer / model | Grok 4.6 (xAI) |
| Tools | Python 3.14.6 (Clang 16.0.0 / clang-1600.0.26.6); Singular 4.4.1 (44105, 64-bit, 2025-11-11) with GMP 6.3.0, NTL 11.6.0, FLINT 3.6.0; Homebrew `sha256sum` |
| Method | Independent SHA-256 of every freeze, harvest, and claimed pin from disk bytes; independent tail-to-row reconstruction over `Q`; independent 169-column census from honest weights; independent DAG evaluator (not the producer `evaluate_dag`) on two new exact-`Q` jets and two new prime-field jets; independent truncated-series `Phi` evaluator; independent polynomial contraction `K(w) |-> D_p`; off-tree Singular 4.4.1 replay of the frozen 16 MB source and contract scripts. Producer `PASS` / `ENDPOINT` / validator strings and every integer in `RESULT.json` were treated as untrusted |
| Temporary replay | `/tmp/v20r2-hostile-replay-grok-20260827/` (outside the producer tree; no producer file, ledger, or `jc2-lean` path was written) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` (producer directory is untracked) |
| Date | 2026-08-27 |

No producer status line is evidence. No `PASS_EXACT_CONTRACTED_SOURCE_COMPILER_READY_FOR_STRATIFIED_SOLVE` marker is evidence. Canonical ledgers, `jc2-lean`, and every file other than this review were left untouched.

---

## Line-item verdicts

| # | Required attack | Verdict |
|---|---|---|
| 1 | Rehash R0/R1/R2 chronology, both failed packets, all freeze manifests, the defective original R2 manifest, and the clean 23-file harvest; confirm R0 pre-algebra and R1 pre-Singular; do not silently discard the self-listing defect | **PASS** |
| 2 | Independently derive why the R0 vector-cokernel extension test is tautological; verify `Q_p=B/(I, <p,Gamma(s)>)`, `D_p=<p,K(w)>`; decide whether contraction-before-specialization is correctly typed | **PASS** |
| 3 | Parse the 569-tail JSON, exact K00 coordinate map, load weights, target rows/signs, and boundary conditions; reconstruct all 140 coefficient equations; compare semantic equations, not only hashes, with the 309 343-node DAG and complete column map; confirm `Jdet` is not `J1` or `J2` | **PASS** |
| 4 | Recompute/replay the full 66-generator six-row syzygy module and all 87 seven-row controls; verify `h*r7=sum u_i*r_i`, `h(0)=20`, every coordinate cross relation, all contracted generators, and the exact contracted target | **PASS** |
| 5 | Independently evaluate all 140 roots on at least one new exact-`Q` fixture and one new prime-field fixture; verify the honest residual through grade 19; re-run or replace every mutation: target sign, `k6` weight, boundary restriction, modular normalization, syzygy sign, contraction order | **PASS** |
| 6 | Audit the exact source census and unit opens; five zero constants restricted before any saturation/solve; negative control that the unrestricted source differs | **PASS** |
| 7 | Enforce compiler-only scope | **PASS** (scope held) |

**Overall: PASS.**

---

## Smallest proved statement

Let `R=Q[d0,...,d5]` with `m=(d0,...,d5)`, and let the frozen 569-term one-parameter tails (raw SHA-256 `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`, canonical semantic digest `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`) be specialized at the Kummer chart

```text
C0=(1+d0)/256, C1=d1, C2=(1+d2)/16, C3=d3, C4=(3+d4)/8, C5=d5, C6=1.
```

Write `T19=F[Lambda]/(Lambda^20)`. The exact mixed source through grade 19 is the single typed jet domain with 169 labelled columns

```text
d_j = sum_{n=1}^{19} d[j,n] Lambda^n,
k10 = sum_{n=0}^{17} k10[n] Lambda^n,     k10[0] != 0,
k6  = sum_{n=0}^{13} k6[n]  Lambda^n,     k6[0]  = 0,
k2  = sum_{n=0}^{9}  k2[n]  Lambda^n,     k2[0]  = 0,
mu2 = sum_{n=0}^{5}  mu2[n] Lambda^n,     mu2[0] = 0,
mu4 = sum_{n=0}^{3}  mu4[n] Lambda^n,     mu4[0] = 0,
mu6 = sum_{n=0}^{1}  mu6[n] Lambda^n,     mu6[0] = 0,
Jdet = Jdet[0],                            Jdet[0] != 0,
```

of which the five displayed zero constants are restricted to zero *before* the coefficient equations are formed, leaving 164 free columns and two named unit opens `k10[0]`, `Jdet[0]`. The Jacobian parameter is `Jdet`; it is not either collision ideal `J1` or `J2`.

The seven rows

```text
Phi_ell = r_ell(C, Lambda^2 k10, Lambda^6 k6, Lambda^10 k2) - Lambda^{12+ell} delta_ell,
delta = (0, mu2, 0, mu4, 0, mu6, Jdet/4)
```

expand to exactly 140 coefficient equations `(Phi_ell, Lambda^n)`, `1<=ell<=7`, `0<=n<=19`. Independently reconstructed from the tails, they agree as truncated series with a deterministic 309 343-node exact-rational arithmetic DAG (SHA-256 `b9bd2e2ca1319ee3107a0f7cf4e1750386d60bb12213a3a970c4812823abdce6`) on two new exact-`Q` jets and two new prime-field jets, and the rebuilt DAG JSON is byte-identical to the frozen DAG.

Let `I=(r1,...,r6)` and `S6=Syz_R(r1,...,r6)`. Independently, in Singular 4.4.1:

- the frozen 66-generator serialization of `S6` and a fresh `syz(I)` generate the same module, and the fresh bytes equal the frozen bytes (`83832f380ce11a491c9799e50ff8b36b5fbc3a6b0d5b5dc52d90b6239c129a7a`);
- all 87 frozen seven-row generators satisfy `sum_i S87[j][i] r_i = 0`;
- `h=63*d4+20` satisfies `h(0)=20` and the polynomial identity `h*r7 = sum_{i=1}^6 u_i r_i`;
- every seven-row generator `v` satisfies the cross relation `h*K(v)-v7*K(w)=Gamma(s(v))` with `s(v)_i=h*v_i+v7*u_i`.

Over `B=R[p10,p6,p2,pmu2,pmu4,pmu6,pJ]`, the live object is the *scalar* contracted presentation, formed before any `Lambda`-substitution:

```text
Gamma_p(s) = <p, Gamma(s)>,     s in S6,
D_p        = <p, K(w)>,
Q_p        = B / (I*B + (Gamma_p(s) : s in S6)).
```

The 66 contracted generators and the 151-term target `D_p` independently replay to SHA-256 `6ba4a0233b713e65be98181285f58fe13cb7ecdb724fd29000b303204f0ef423` and `cade1704d973750e455829a3c3783d1c8444a4bb6e2b14e37e8277c83393819c`. Independently, substituting `(p10,p6,p2,pmu2,pmu4,pmu6,pJ)` for the seven coordinates of the serialized `K(w)` recovers `D_p` coefficientwise (151/151 terms), with constant `pJ`-coefficient `-5=-h(0)/4`. After the honest weighted specialization of `p`, the truncated residual `h*Phi7-sum_i u_i Phi_i` agrees with specialized `D_p` through grade 19.

This is an exact source/type/compiler theorem for this frozen client. It does **not** cover any nonlinear prefix stratum, decide existence or nonexistence of a compatible `Lambda<=19` jet, exclude an arc, decide K00 closure incidence, or imply order two, maximum twelve, or JC2.

---

## 1. Chronology, freeze manifests, failed packets, defective original

### 1.1 Three registered r6b lanes

| Lane | Tag | Freeze self-SHA | Compiler SHA (pinned) | Wrapper SHA (pinned) | Independent outcome |
|---|---|---|---|---|---|
| R0 | `...v20r2_20260827T123800Z_r6b` | `647de67b40f66eb88e7202ee76208771b4a1fae69900dd5f34e959f3ca21e549` | `13342b16367b347680d6cbb4fb726798b7c1904422b10a661f31f5b7b59974b0` | `f6332a9d4535b3731b097f4b54747ba87ed52fcf2c627fc313bc0877d35819d1` | `FileExistsError` at `Path.mkdir(exist_ok=False)` after 0.19 s / 34 880 KiB; no `output/`; no DAG; no Singular |
| R1 | `...v20r2r1_20260827T124100Z_r6b` | `4331078823c3bf88e4de46826a6a071b749ec2162d3093e872f9ae54e9b5a224` | same `13342b16…` | `7bbbf96f1de34906399dc08f85388582b41feac53472c4d23a44b4013a06e5f6` | exact-`Q` DAG and columns emitted; died at `F65521` fixture row 1, `Lambda^1`; no Singular; 3.19 s / 159 252 KiB |
| R2 | `...v20r2r2_20260827T124500Z_r6b` | `8f9e893fa3357787ef8d095cb8e1e040efe788ce54b70f150b77ad1b5bab41cb` | `2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b` | same `7bbbf96f…` as R1 | 16.07 s / 178 300 KiB; Singular source and contract replays; harvested under `aws_r6b_r2_pass/` |

Freeze self-hashes above are independently recomputed from the three `SOURCE_FREEZE_V20R2*.sha256` files and match `AWS_REGISTRATION_V20R2.md`.

### 1.2 R0 was pre-algebra

The harvested `aws_r6b_r0_failed/run/compiler.stderr` is a Python `FileExistsError` on the pre-created AWS output directory. `aws_r6b_r0_failed/output/` does not exist. `FINAL.validation` is `engine_rc=1` with no validator line. Wall time 0.19 s. R0 is permanently nonpromotable and is a wrapper defect, not an algebraic endpoint. The R0 freeze check at launch time printed `compile_contracted_source_v20r2.py: OK` against compiler `13342b16…`.

The R0 wrapper created `$aws_job/output`; the live R1/R2 wrapper (SHA `7bbbf96f…`) creates only `$aws_job/run` and passes `$aws_job/output` as the compiler argument. That is the R1 runner-only repair, frozen in `PREREGISTRATION_V20R2R1.md` (`847ae7fc8f0b86d48ba445f0a67c77c3c1c831d7c79cef94121da365cccdfb26`) before R1 ran.

### 1.3 R1 stopped before Singular

R1 output contains exactly two files:

```text
LITERAL_140_EQUATION_DAG.json   5524619  b9bd2e2ca1319ee3107a0f7cf4e1750386d60bb12213a3a970c4812823abdce6
SOURCE_COLUMNS.json               29053  2e8ceeb42dcc41752f82fe1df866c28b33e289097b065bf965db25574230919c
```

Both are **byte-identical** to the R2 artifacts of the same names. R1 therefore already compiled the exact-`Q` 140-equation DAG and then failed closed in the modular DAG evaluator, comparing unreduced integer representatives against reduced `F_65521` values, first mismatch `(row=1, Lambda^1, node=15188)`. No `*.sing` scripts, no syzygy replay, no contracted generators. R1 is permanently nonpromotable. The R2 repair, frozen in `PREREGISTRATION_V20R2R2.md` (`c50d8ca9cba09a2783815d961d22446340aa9f82e401db2a5a94375985656b2b`) before R2 ran, is exactly nodewise reduction of DAG addition and multiplication plus a mandatory unreduced-versus-reduced control.

### 1.4 Freeze verification against *current* bytes

Independently `sha256sum -c` equivalent against the live tree:

| Manifest | Self-SHA | Lines | OK | Bad | Missing |
|---|---|---|---|---|---|
| `DESIGN_FREEZE.sha256` | `a08389d0912dc22ed8ff3f7515c00d10537c819c1f93c85b859c36d700ce28c5` | 12 | 12 | 0 | 0 |
| `SOURCE_FREEZE_V20R2.sha256` (R0) | `647de67b…` | 25 | 23 | 2 | 0 |
| `SOURCE_FREEZE_V20R2R1.sha256` | `43310788…` | 27 | 26 | 1 | 0 |
| `SOURCE_FREEZE_V20R2R2.sha256` | `8f9e893f…` | 29 | **29** | 0 | 0 |
| `HARVEST_EVIDENCE_R2.sha256` | `b205bd9fae6e82b9727511d85841eba3225147453d83b879aefdbc2a61c16f56` | 23 | **23** | 0 | 0 |

The two R0-freeze mismatches are the live compiler `2ac7653c…` versus pinned `13342b16…` and the live wrapper `7bbbf96f…` versus pinned `f6332a9d…`. The one R1-freeze mismatch is the live compiler versus the same `13342b16…`. This is the in-place R1/R2 repair chronology, not silent discarding of the failed packets: both failed trees, both failure notes, and both older freeze manifests remain byte-for-byte.

**Custody limitation, not a mathematical defect of R2.** The R0/R1 mathematical compiler bytes are not stored as a second file in the harvested tree. A mechanical revert of the three documented R2 edits (nodewise `% modulus` on add/mul; `modular_representative_normalization` flag; the unreduced-versus-reduced control) did **not** recover SHA `13342b16…`. That pin is therefore a freeze-manifest claim whose preimage is not independently rehashable from the present tree. It does not infect the R2 compiler, whose live bytes match the R2 freeze.

### 1.5 Defective original R2 endpoint manifest, preserved

The original `aws_r6b_r2_pass/run/ENDPOINT_EVIDENCE.sha256` has SHA-256

```text
72277a97af9a72dabb7c491a860018357eed7133fba9b1ff6f9676a6645397e4
```

matching the charged pin. Remapping the AWS prefix `/home/ubuntu/jobs/...v20r2r2_20260827T124500Z_r6b/` onto the harvested `aws_r6b_r2_pass/` yields **21/21** hash matches and **one missing path**:

```text
a5955d9c814754b0ae336e1596445346eeb746fc36a426bf2cda69b4820ce0ae
  .../run/ENDPOINT_EVIDENCE.sha256.tmp
```

The wrapper wrote the manifest into the directory being walked, hashed the temporary file, then renamed it. The `.tmp` path does not exist after `mv`. The self-entry hash `a5955d9c…` is **not** the hash of the final manifest (`72277a97…`). This is exactly the documented self-listing defect.

`HARVEST_EVIDENCE_R2.sha256` does **not** list `ENDPOINT_EVIDENCE.sha256`, does **not** list itself, and covers the 21 good walked files plus `launch_registration.txt` and `source_freeze_check.stdout` — 23 lines, 23/23 OK. The original defective manifest is retained. No algebra was rerun for the custody repair. This review does not discard it.

### 1.6 Charged R2 pins, independently recomputed

| Artifact | Independent SHA-256 | Match to charged pin |
|---|---|---|
| V20R1 design erratum | `0f2debfecf1ae127db20de8a806e93842a0f333fce3592a3e09231a48ad3b53b` | yes |
| R2 source freeze file | `8f9e893fa3357787ef8d095cb8e1e040efe788ce54b70f150b77ad1b5bab41cb` | yes |
| R2 compiler | `2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b` | yes |
| R2 `RESULT.json` | `a2147de95bc37e8adb629201e2b39b788b99df3d4586da54af7bd41f269a9f15` | yes |
| literal DAG | `b9bd2e2ca1319ee3107a0f7cf4e1750386d60bb12213a3a970c4812823abdce6` | yes |
| contracted generators | `6ba4a0233b713e65be98181285f58fe13cb7ecdb724fd29000b303204f0ef423` | yes |
| contracted target | `cade1704d973750e455829a3c3783d1c8444a4bb6e2b14e37e8277c83393819c` | yes |
| fixture audit | `bbcdd0e0242a23b309cd04f44f42a0ef8f1b69eb8f13ef396fc40b26e450cf55` | yes |
| defective original manifest | `72277a97af9a72dabb7c491a860018357eed7133fba9b1ff6f9676a6645397e4` | yes |

---

## 2. Why the R0 vector-cokernel test is tautological, and why the live scalar object is correctly typed

### 2.1 Independent derivation

Write, as in the withdrawn Section 4 of `PREREGISTRATION.md`,

```text
M = (R_h)^7 / ( I*(R_h)^7 + image(Gamma)_h ),
Gamma: S6 -> R^7,
Gamma(s) = (sum_i s_i a_i^{k10},
            sum_i s_i a_i^{k6},
            sum_i s_i a_i^{k2},
            -s2, -s4, -s6, 0).
```

Let `X` be any one load coordinate in `{k10,k6,k2}` and let `pi_X: R^7 -> R` be projection onto that coordinate. Then:

- `pi_X` sends `I*(R_h)^7` into `I_h`;
- `pi_X(Gamma(s)) = sum_i s_i a_i^X`, which generate the V17 image ideal `E_X`.

Hence `pi_X` descends to a surjection of `R_h`-modules

```text
pi_X : M  ->  (R_h) / (I+E_X)_h  =: Q_X.
```

Every linear functional on `Q_X` therefore pulls back to a linear functional on `M` by composition with `pi_X`. Setting the other six components to zero is that pullback. Any finite sum of the three axis pullbacks is likewise an extension. Consequently an `EXTENDS` versus `DOES_NOT_EXTEND` computation for a V18 axis covector against the *uncontracted vector* quotient `M` is automatic: the map `Hom(Q_X, F) -> Hom(M, F)` is injective on the nose. That computation cannot be the mixed-source discriminator. The sentence in original Section 4 claiming the three axis covectors need not extend is correctly withdrawn.

This does **not** make the three V18 covectors composable with the honest mixed jet. Pullback along `pi_X` produces a functional on `M` whose pairing with a simultaneous mixed deformation vector `(k10,k6,k2,mu2,mu4,mu6,Jdet)` is *not* the honest residual. The missing operation is contraction by a simultaneous parameter vector, and that contraction does not descend from `M` to any single scalar quotient of `R` independent of `p`.

### 2.2 The corrected scalar object

Introduce independent parameters `p=(p10,p6,p2,pmu2,pmu4,pmu6,pJ)` over `B=(R_h)[p]`. Set

```text
Gamma_p(s) = <p, Gamma(s)>,
D_p        = <p, K(w)>
           = p10 D_{k10} + p6 D_{k6} + p2 D_{k2}
             + pmu2 u2 + pmu4 u4 + pmu6 u6 - pJ h/4,
Q_p        = B / ( I*B + (Gamma_p(s) : s in S6) ).
```

Changing the chosen unloaded relation by a six-row syzygy changes `D_p` by one of the displayed generators, so `[D_p] in Q_p` is representation-independent. `Gamma` has seventh coordinate identically zero, so `pJ` does not appear in any contracted generator; it appears only in the target, as `-pJ h/4`. Independently, the serialized `K(w)` ends in `-5*gen(7)` and the serialized `D_p` contains `-5*pJ` and `-(63/4)*d4*pJ`, matching `-h/4` for `h=63*d4+20`.

A generator of `Gamma` with both first and second coordinates nonzero exists (Singular control `K00_V20R2_COUPLED_GENERATOR=1`, independently replayed). Therefore `Q_p` is not a product of axis quotients, and swapping `(p6,p2)` changes both the contracted generators and `D_p`. That is the contraction-order mutation, independently detected.

### 2.3 Contraction-before-specialization is correctly typed in the live compiler

The honest mixed specialization is the ring map `B -> T19[source]` sending

```text
p |-> (Lambda^2 k10, Lambda^6 k6, Lambda^10 k2,
       Lambda^14 mu2, Lambda^16 mu4, Lambda^18 mu6, Lambda^19 Jdet).
```

The live design forms `Gamma_p` and `D_p` in `B` *first*. Independently:

- `contract_replay_v20r2.sing` enlarges the prelude ring to `R=0,(d0,...,d5,p10,p6,p2,pmu2,pmu4,pmu6,pJ),dp;` and writes 66 polynomials `gp=<p,Gamma[j]>` and `Dp=<p,K(w)>` with **no** `Lambda` in the ring;
- the 140-equation DAG is the *literal specialized* presentation, with the honest weights implemented as series shifts `2,6,10,14,16,18,19`;
- the truncated residual identity `h*Phi7-sum u_i Phi_i = specialized D_p` through grade 19 is the comparison between those two presentations.

This is the correct variance. Specializing first and then testing axis extension in `M` is the withdrawn tautology. The compiler does not do that.

V18 duals remain navigation controls on the three coordinate specializations of `Q_p`. Their pullbacks to `M` carry no mixed-source verdict.

---

## 3. Tails, coordinate map, 140 equations, DAG, `Jdet`

### 3.1 Tails and unloaded rows

Independently parsed `tails.json`: seven keys `"1"`…`"7"`, **569** terms, every monomial length 10, affine in the three loads (`sum of load exponents <= 1`, each 0 or 1), and weighted-homogeneous of weight `12+ell` against `(8,7,6,5,4,3,2, 2,6,10)`. Canonical JSON digest matches `6eed03d4…`. The file contains neither `J1` nor `J2` nor `Jdet` (targets are not tail variables).

Unloaded specialization through the Kummer chart independently equals the frozen V14R1 prelude rows, coefficientwise. Independently `h=63*d4+20`, `h(0)=20`, and `h*r7-sum_{i=1}^6 u_i r_i` is the zero polynomial in `R`. Load rows and targets `D_X=h a_7^X - sum u_i a_i^X` independently equal the V21 serializations for `X in {K10,K6,K2}`.

### 3.2 Census, derived rather than believed

Honest weights and truncation `Lambda^20` independently force the index ranges

```text
d_j : 1..19          (6*19 = 114)
k10 : 0..17          (18)     first grade 2
k6  : 0..13          (14)     first grade 6,  k6[0] FIXED_ZERO
k2  : 0..9           (10)     first grade 10, k2[0] FIXED_ZERO
mu2 : 0..5           (6)      first grade 14, mu2[0] FIXED_ZERO
mu4 : 0..3           (4)      first grade 16, mu4[0] FIXED_ZERO
mu6 : 0..1           (2)      first grade 18, mu6[0] FIXED_ZERO
Jdet: 0..0           (1)      first grade 19, FREE unit open
```

Total 169, five zeros `{k6_0,k2_0,mu2_0,mu4_0,mu6_0}`, 164 free, unit opens `{k10_0,Jdet_0}`. The producer `SOURCE_COLUMNS.json` (SHA `2e8ceeb42dcc41752f82fe1df866c28b33e289097b065bf965db25574230919c`) matches this table semantically, field-by-field, including `kind`, `first_Lambda_grade`, and `boundary_status`. `Jdet` is the unique column of kind `jacobian`; there is no `J1` or `J2` column.

The producer hard-codes the same ranges and then asserts the counts 169/164. That is a style defect relative to “derive rather than hard-code”, not a census error: the independently derived table is identical.

### 3.3 DAG structure and semantic comparison

Frozen DAG JSON:

```text
format     K00_V20R2_EXACT_RATIONAL_ARITHMETIC_DAG_V1
truncation Q[Lambda]/(Lambda^20)
nodes      309343     opcodes  c:636  v:164  m:161705  a:146838
roots      140        (ell,n) in {1..7} x {0..19}, complete
target     Jdet       forbidden aliases J1, J2
coord map  C0=(1+d0)/256, C2=(1+d2)/16, C4=(3+d4)/8, C6=1
boundary   SUBSTITUTE_FIVE_ZERO_CONSTANTS_BEFORE_ANY_SOLVE_OR_SATURATION
```

The 164 `v`-nodes are exactly the 164 free column names; the five boundary zeros are interned as the constant `0` (node 0 is `["c",0,1]`). Every grade-0 root is that zero node, as required by `d_j` starting at `Lambda^1` and the K00 origin of the unloaded rows.

Semantic comparison, not hash worship:

1. Rebuilding the DAG from the tails with the producer intern order, including the residual intern, produces a JSON file whose SHA-256 is **byte-identical** to the frozen DAG `b9bd2e2c…`. Residual LHS/RHS node-id lists match the frozen lists.
2. A *second* truncated-series implementation of `Phi_ell` (independent of the producer `Dag` class and of `direct_tail_rows`) agrees with evaluation of the *frozen* DAG nodes on four independent jets (Section 5). That is agreement of two algorithms on the 140 coefficient polynomials, sampled at new points, not a replay of producer fixture hashes.
3. Residual LHS and RHS are **not** intern-equal as node ids (`lhs[1]=249899`, `rhs[1]=0`, …). Hash-consing does not fold algebraic zeros. They **evaluate** equal on every jet in Section 5. This is an unsimplified-but-correct identity, not a discrepancy in the 140 `Phi` roots.

`J1`/`J2` occur in the DAG JSON only as `forbidden_aliases`. The target symbol is `Jdet`. The row-7 target scale in both the DAG builder and the independent series evaluator is `-1/4`, i.e. `-Lambda^{19} Jdet/4`, matching `delta_7=Jdet/4` with overall minus sign.

---

## 4. Syzygies, cross relations, contracted presentation

Off-tree copies of the frozen 16 013 986-byte source script and 16 016 936-byte contract script were run in Singular 4.4.1 with cwd `/tmp/v20r2-hostile-replay-grok-20260827/sing/`. Producer stdout was not reused.

### 4.1 Source replay (7.43 s local)

```text
K00_V20R2_SERIALIZED_MODULE_REPLAY=1
K00_V20R2_FRESH_SYZ6_GENERATORS=66
K00_V20R2_SYZ6_MODULE_EQUAL=1
K00_V20R2_BASE_RELATION=1
K00_V20R2_H0=20
K00_V20R2_CROSS_RELATIONS=1
K00_V20R2_SIGN_MUTATION_DETECTED=1
K00_V20R2_SOURCE_REPLAY=PASS
```

Independent output hashes, all equal to the frozen R2 files:

| Artifact | Independent SHA-256 |
|---|---|
| `source_replay.stdout` | `35de48fc3ac4943843fbbb027e747f7e4c775b7b936a6d523efdcb611921bec5` |
| `FRESH_SYZ6_MODULE.txt` | `83832f380ce11a491c9799e50ff8b36b5fbc3a6b0d5b5dc52d90b6239c129a7a` |
| `GAMMA_MODULE.txt` | `65b75de1ad6ab1044d25365022c7f97707687431c135575fd439ac64c7bece02` |
| `K_VECTOR.txt` | `940d9e42e1fce079f4bfcb5e1a319884c4b606f32f50ba435d5dc294ed7ff24a` |

The fresh `syz(I)` bytes equal the V21 frozen `syz6.txt` bytes, not merely the same module. Top-level generator counts independently parsed from the text (comma-split at paren-depth 0): `S6=66`, `S87=87`, `Gamma=66`. Counts were not trusted alone: every frozen six-row generator was reduced against `std(syz(I))` and every fresh generator against `std(T)`, and every seven-row generator was multiplied against `(r1,...,r7)` to a literal zero polynomial.

The sign mutation in the script replaces `s(v)_i = h*v_i + v7*u_i` by `h*v_i - v7*u_i` in the `k10` component of (4.2) and requires a nonzero discrepancy. Independently detected.

The even-target components of (4.2) are identities in the definition of `s(v)` (`K(v)_4=-v2`, `Gamma(s)_4=-s2`, etc.); the load components are the load-bearing checks. All 87 passed.

### 4.2 Contract replay

```text
K00_V20R2_CONTRACTED_GENERATORS=66
K00_V20R2_COUPLED_GENERATOR=1
K00_V20R2_CONTRACTION_ORDER_MUTATION_DETECTED=1
K00_V20R2_CONTRACT_REPLAY=PASS
```

| Artifact | Independent SHA-256 |
|---|---|
| `contract_replay.stdout` | `50095796c650191ec5d093dd7a7b95a5105b5d6156b38a8ea289f57733de659d` |
| `CONTRACTED_GENERATORS.txt` | `6ba4a0233b713e65be98181285f58fe13cb7ecdb724fd29000b303204f0ef423` |
| `CONTRACTED_TARGET.txt` | `cade1704d973750e455829a3c3783d1c8444a4bb6e2b14e37e8277c83393819c` |

Python-side contraction: replace `gen(1)..gen(7)` in `K_VECTOR.txt` by `(p10,p6,p2,pmu2,pmu4,pmu6,pJ)` and parse both sides in `Q[d0,...,d5,p]`. Result: **151/151 terms equal**. No `J1`/`J2` token in either file.

The contraction-order mutation swaps `p6` with `p2` in the pairing. Independently detected, and it can fire only because a coupled generator exists.

---

## 5. New fixtures, residual, mutations

Producer fixtures 1, 2, 3 were **not** reused as mathematical evidence. Their assignment SHA-256 values were recomputed from the published recipe and match `FIXTURE_AUDIT.json` (`d8c3e167…`, `6e41f6f4…`, `de22b864…`); that is a custody cross-check only.

New jets, assignment seed `GROK-V20R2|{seed}|{column}`, values independent of the producer `V20R2|{fixture}|{name}` recipe; `k10_0=11`, `Jdet_0=13` (or those reduced at `p`), boundary columns held at 7 for the unrestricted control and zeroed in the restricted source:

| Label | Field | 140 DAG roots = independent `Phi` | DAG residual LHS = RHS | numeric `h*Phi7-sum u_i Phi_i` = specialized `D_p` through grade 19 |
|---|---|---|---|---|
| `Q17` | `Q` | yes | yes | yes |
| `Q99` | `Q` | yes | yes | yes |
| `P23` | `F_65537` | yes | yes | yes |
| `P65521-F7` | `F_65521` | yes | yes | yes |

`F_65537` is a different prime from the producer control `65521`. Denominators 256, 16, 8, 4 remain invertible.

Mutations, all detected on every new jet (Python) or on the Singular replay (the last two):

| Mutation | Mechanism | Detected |
|---|---|---|
| target sign | `delta |-> -delta` (`target_sign=+1`) | yes, on all four jets |
| `k6` weight | shift 6 replaced by 5 | yes, on all four jets |
| restriction-before-saturation | five boundary constants left free | yes, on all four jets; unrestricted rows differ from restricted |
| modular representative normalization | unreduced integer DAG versus nodewise `% p` | yes, on both prime jets; raw representatives differ and `raw % p` equals nodewise |
| syzygy sign | `s(v)_i = h v_i - v7 u_i` in (4.2) | yes, Singular `SIGN_MUTATION_DETECTED=1` |
| contraction order | swap `p6` with `p2` in `<p,Gamma>` and in `D_p` | yes, Singular `CONTRACTION_ORDER_MUTATION_DETECTED=1` |

`FIXTURE_AUDIT.json` records only the first four. That is an additive reporting gap, not a missing control: syzygy sign and contraction order live in the Singular stdout, which independently replayed. They are not silently absent.

---

## 6. Source census, unit opens, restriction order

Five zero constants independently identified: `k6_0, k2_0, mu2_0, mu4_0, mu6_0`. The DAG intern contains 164 variable nodes and does **not** contain those five names: they are substituted by the constant 0 at DAG construction, before any later solve or saturation (of which this producer performs none). Unit opens `k10_0` and `Jdet_0` remain free variables and are forced nonzero on every fixture.

Negative control: evaluating the same tails with those five columns left at their assignment values (nonzero by construction) produces a different 140-tuple on every new jet. The unrestricted source is therefore not the restricted source.

There is no saturation and no solve in V20R2. “Restricted before any saturation/solve” is vacuously true of the compiler and non-vacuously true of the DAG it emits. A later stratified solver that reintroduced the five zeros as free columns would be a different, untyped source.

---

## 7. Scope firewall

PASS is an exact source/type/compiler milestone for this frozen K00 client. Explicitly **not** proved, and not claimed by the live preregistration endpoint:

- any constructible prefix stratum of the 140-equation system, Fitting split, or rank jump;
- existence or nonexistence of a compatible `Lambda<=19` jet;
- an obstruction dual;
- exclusion of a formal or algebraic arc;
- K00 closure incidence;
- order two, maximum twelve, or JC2;
- V21R1 local nonmembership (recorded as a provisional dependency and not used for source typing; the six-row module was independently regenerated from `syz(r1,...,r6)`).

The original V20 charged question — mixed reachability through `Lambda^19` — remains open. V20R2 supplies the typed source on which that question can now be asked.

---

## Additive defects and corrections (none algebraic)

1. **Original R2 endpoint manifest self-listing defect.** Preserved at SHA `72277a97…`. Clean additive harvest `HARVEST_EVIDENCE_R2.sha256` (self `b205bd9f…`) covers 23/23 files and does not include the defective manifest or itself. Not silently discarded.
2. **R0/R1 compiler preimage not archived as a second file.** Live path holds only the R2 compiler. Older freeze manifests correctly fail against current bytes. Failed packets and freeze files remain. Does not infect the R2 pin `2ac7653c…`.
3. **DAG residual LHS/RHS not intern-identical.** They evaluate identically on every jet tested and rebuild to the frozen node-id lists. Unsimplified zeros, not a wrong residual.
4. **`FIXTURE_AUDIT.json` omits syzygy-sign and contraction-order.** Both controls exist in the Singular scripts, fired, and independently replayed.
5. **Census ranges are hardcoded then counted.** Independently derived ranges match; no numerical error.

R0 and R1 remain immutable and nonpromotable.

---

## Independent replay hashes (this review)

| Item | SHA-256 / result |
|---|---|
| rebuilt DAG JSON | `b9bd2e2ca1319ee3107a0f7cf4e1750386d60bb12213a3a970c4812823abdce6` (equals frozen) |
| local Singular source stdout | `35de48fc3ac4943843fbbb027e747f7e4c775b7b936a6d523efdcb611921bec5` (equals frozen) |
| local Singular contract stdout | `50095796c650191ec5d093dd7a7b95a5105b5d6156b38a8ea289f57733de659d` (equals frozen) |
| local `FRESH_SYZ6_MODULE.txt` | `83832f380ce11a491c9799e50ff8b36b5fbc3a6b0d5b5dc52d90b6239c129a7a` |
| local `GAMMA_MODULE.txt` | `65b75de1ad6ab1044d25365022c7f97707687431c135575fd439ac64c7bece02` |
| local `K_VECTOR.txt` | `940d9e42e1fce079f4bfcb5e1a319884c4b606f32f50ba435d5dc294ed7ff24a` |
| local `CONTRACTED_GENERATORS.txt` | `6ba4a0233b713e65be98181285f58fe13cb7ecdb724fd29000b303204f0ef423` |
| local `CONTRACTED_TARGET.txt` | `cade1704d973750e455829a3c3783d1c8444a4bb6e2b14e37e8277c83393819c` |
| `K(w)` contracted in Python | 151/151 terms equal `D_p`; `pJ`-coefficient `-5` |
| new `Q` fixtures `Q17`, `Q99` | 140/140 roots; residual identity through grade 19 |
| new `F_65537` fixture `P23` | 140/140 roots; residual identity; modular-normalization mutation fires |
| new `F_65521` fixture `P65521-F7` | 140/140 roots; residual identity |
| R1 DAG vs R2 DAG | byte-identical (`b9bd2e2c…`) |
| HARVEST 23/23 | self `b205bd9fae6e82b9727511d85841eba3225147453d83b879aefdbc2a61c16f56` |

Temporary replay files remain under `/tmp/v20r2-hostile-replay-grok-20260827/` and were not copied into the producer tree.

---

## Precise next finite mixed-source discriminator

V20R2 types the source. The next finite calculation that can actually decide mixed reachability is a complete constructible-stratum / Fitting cover of the 140 literal coefficient equations — equivalently, of the first six specialized rows plus the honestly specialized residual `D_p` — through `Lambda^19`, with a replayed lift or a rational dual in the literal seven-row presentation at every rank jump, the five boundary zeros held at zero, and the two unit opens retained.

Anything short of a complete prefix-stratum cover (a single modular dual, a V18 axis class, a raw nonzero residual, a random point, a valuation heuristic) is navigation, not a mixed-source theorem.

---

## Verdict

**PASS**, at exact compiler-only scope.

The live V20R2 packet is an exact, typed, contracted mixed-source compiler for the frozen normalized K00 seven-row client through `Lambda^19`. The R0 vector-cokernel test is tautological and is not the live object. R0 and R1 are nonpromotable wrapper/evaluator failures, preserved. The original endpoint-manifest self-listing defect is preserved and additively repaired. No jet, stratum, arc, closure, order-two, maximum-twelve, or JC2 conclusion follows.
