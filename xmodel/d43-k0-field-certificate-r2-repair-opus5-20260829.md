# D43 `K0` dual-engine certificate, R2: repair packet and producer report

**UTC:** 2026-08-29
**Role:** Opus 5, primary producer of a fresh R2 source packet
**Packet built:** `cases/d43_k0_field_certificate_r2_20260829/`
**Status shipped:** `R2_SOURCE_READY_AWS_NOT_AUTHORIZED`
**R1 packet:** untouched. `seal_r1.py --root . --verify` still reports
`ok: true` with source seal `583db53e641adfee8dec8cc3f5f4fc2c413b2f2651362790bea9d08dea5cb611`,
archive `e5d140db10194f1cab0812e3eaa003ca7aafd36a6e2b1fb11c153862975790b5` —
the values the Fable 5 review recorded. Nothing in R1 was patched or
overwritten.

No AWS action, no PARI/GP execution (there is no `gp` on this host), no heavy
CAS, no `jc2-lean` access, no `git status`, no workspace-wide search, no
canonical-ledger edit, no commit, no push, no web. Every test reported below
is bounded stdlib Python and ran on this host; total preflight wall clock is
6.5 s. **No claim is made that the GP syntax or API has run: the file has
still never been seen by any GP parser.**

This is certificate engineering plus mathematical gate repair. The promoted
paper theorem (`6d3d53c2…`, grok46-confirmed `07f20be5…`) is treated as fixed
and is not broadened.

---

## 1. What R2 is answering

Two inputs.

**The observed AWS fault.** The single licensed R1 rehearsal produced
supervisor terminal `NO_VERDICT` with

```
RUNNER_EXIT: runner exited 1: ModuleNotFoundError: No module named 'k0_field_checker_r1'
```

on live `r6i.large` instance `i-0c37c2ea592ee97b5`, PARI binary
`c9673623cad2eaa7cfe402e7b7d833f1f703689a09837026b6386aaafba6deec`, one
effective core, `memory.max` 1 GiB, `memory.swap.max` 0, host `SwapTotal` 0.
`aws_supervisor_r1.py:462` invoked `python3 -I -B runner_r1.py`; isolated mode
implies `-P`, so the script's own directory is absent from `sys.path` and
`runner_r1.py:35`'s bare sibling import failed. GP was never invoked; no
mathematics ran. The fault is a source/integration defect and is not contrary
mathematical evidence.

**The Fable 5 hostile source review** (`29e9496e…`, body seal `df389c19…`),
verdict `PASS_FOR_PINNED_GP_REHEARSAL`, defect list D1–D8 required and D9–D13
cosmetic.

---

## 2. Byte hashes of everything shipped

### 2.1 The R2 packet, 15 sealed members plus 4 generated files

| file | SHA-256 |
|---|---|
| `README.md` | `8b09347d0da9265bdd2cc5e88ba6c930e909c374b794bf04841f420c402d1101` |
| `REVIEW_REQUEST.md` | `f77f8cf411dd5c6f3b5a5448730d91653f66cebc3ce93f68348fa25dea825dfa` |
| `authorization_template_r2.json` | `b0031e542514f43aac191a0b1f83a7fc4cd9258c6c1343d59339f40625e9361f` |
| `aws_supervisor_r2.py` | `55f43cdc1f11c297c491b48a99f59057a92dcd01638ccc40fea440d2de1aa0b6` |
| `aws_worker_r2.sh` | `c504e60a51ac47ee031ec63f8d59164aaeff2513c0beab81655e78fd575bd1b6` |
| `execution_pins_r2.json` | `51378ac1f357d36076c19e9117f22da678214414333abacd02262cb3f5406d2f` |
| `k0_algebra_r2.py` | `a7de3c3fcefc42302e402b8dfcaeefbba6d5a582ae694447e8f95f6a8e8dd4a6` |
| `k0_field_cert_r2.gp` | `c3f576dd5bbc1c0af970246379c97d1c541daa7ae521f722ed43f905e4713d76` |
| `k0_field_checker_r2.py` | `14650a3d473477423434763e0d2c0528914b5a4357cf4db2e6e9daf588761251` |
| `k0_mutations_r2.py` | `45ae1eeb8d70c1fa55ce9cf8ac359ec91a19581f8901c3c57f1e245c019d6650` |
| `preflight_r2.py` | `02cf8950a5d24445bd1dd328c2e45207955d98eea698392c56461997a785641a` |
| `preregistration_r2.json` | `bfc49d37267c15a6a424718ff598c1efbe7709af327540bfbf08deca89265fa5` |
| `runner_r2.py` | `c0866be32c54465ce581de51fefddb467bad9a8678c4ea67c6c661150cc0139a` |
| `seal_r2.py` | `c3fa02b1f671a891b184ba20249641f6f24c70382909fe83cb98537512256edf` |
| `systemd_unit_template_r2.service` | `9702ceaf007fa62caef3596e5394d4455e2233e0d55b94c2602c96397973e5dc` |

| generated | SHA-256 |
|---|---|
| `PAYLOAD.sha256` | `8bfdd426990a3891fde526336fc26585ad46d912d8fcb3a8951dc97019e5526d` |
| `SOURCE_ARCHIVE.tar` (24 members) | `569bb51cad8d64749cc7f1b911ccb849f315c4db4634beee4472ee9f9f63c685` |
| `SOURCE_ARCHIVE.sha256` | `561dea8d7a58a7c64dd5fe6613e39eb394bd9f44af012308ffb1ad9af1c374d6` |
| `SOURCE_SEAL.sha256` | `69279ae99c9a3a35c31b536f62b31970fba1b7997f5ef092ae97ecd9d8f47f34` |

### 2.2 The eight sealed external members

| file | SHA-256 | role |
|---|---|---|
| `cases/d43_common_integral_emitter.py` | `5420b5c0b4164c719e98316cade96c094c2945a6fed8bad3ac0926771855984d` | `PHI42` literal |
| `cases/d43_exact_sparse_rows_v2_20260828/selected_rows_v2.py` | `9fc9bd7a365827ddba2c1ba45cbb34870d6f2d71c9d3eecb6b242d46e00990b2` | `COEFFICIENT_ALGEBRA` block |
| `cases/d43_full_pointbank_p105337.pkl` | `bb0f13b61616c486116027e284483a4fb0f529f8df2dca7f728d56584d98fcbb` | corroboration |
| `cases/d43_full_pointbank_p105673.pkl` | `b933cdb5b72bd4073da0cb82150db768f6b4607d5cd29d3d4aec0fe22ce5bcc3` | corroboration |
| `xmodel/d43-e5-e6-elimination-bridge-gpt56-20260828.md` | `e1b99600b01f91f7b95df4f7f969481efa1e7b1ee377e83156f3f6b6a8e3c863` | **new in R2**: the literal `E`, parsed by `E_LITERAL_PIN` |
| `xmodel/d43-k0-splitting-primary-research-opus5-20260828.md` | `6d3d53c20387d324766daaf40eb502df42d9e2776c6ab6053041bc1f3dee1430` | theorem report; also the literal `q0`, parsed by `Q0_LITERAL_PIN` |
| `xmodel/d43-k0-field-theorem-hostile-review-grok46-20260829.md` | `07f20be55add0fea0ff6329ce0d4ca386024af33edad33254d46451fd575a94a` | **new in R2**: the theorem review the prose steps rest on |
| `xmodel/d43-k0-field-certificate-r1-hostile-review-fable5-20260829.md` | `29e9496e0552f94d6823c744b7b979ad02274e6cbf39ae124ec01e6465d596e2` | **new in R2**: the defect list being repaired |

### 2.3 Pinned run values

```
route                       D43-K0-FIELD-CERT-R2
python gates                42            (39 in L0-L5, 3 layer censuses)
gp gates (nexpect)          110
shared observables          29            (25 unconditional, 4 E-layer)
census   SHA-256            b828f93d6a29c15371e4d277473e63c0a25ba0280fa5ab44706d10c786f9aeb0
observable SHA-256          4b1c7ff63935adb27148a2967037b7a357354848b0bbc2f0df827db2e45148f6
battery  SHA-256            e416de0e074cc0125ac2419a724c420d0d5f9c4dcd141abbd276f477bafbc25b
gp script SHA-256           c3f576dd5bbc1c0af970246379c97d1c541daa7ae521f722ed43f905e4713d76
```

---

## 3. Tests executed, with exact counts

`preflight_r2.py --root .` → `preflight_pass: true`, rc 0, 6.5 s. It runs the
full Python checker **75 times** (1 baseline in P4, 65 inside the battery, 9
in the gate-surface probes) and spawns **8 real `python3` subprocesses**.

| stage | what it does | counts |
|---|---|---|
| P1 | packet manifest replay | 15/15 members, 0 mismatched |
| P2 | sealed archive replay | 24/24 members, 0 missing / extra / mismatched |
| P3 | GP static census, hygiene, label audit | 99 `chk`/`chkE` sites → **110 predicted = 110 declared**; 22 `obs` sites → **29 predicted**; 13 loops, 0 unresolved over gate sites; 13 forbidden constructs scanned, 0 present; 99 labels, max width **63 ≤ 80**; ASCII-only, tab-free |
| P4 | Python engine | **42/42 gates PASS**; `unconditional_k0_theorem` true, `e_conditional_ratio_theorem` true, `corroboration_ok` true, `execution_integrity` true; the three `theorem_inputs` sets are pairwise disjoint |
| P5 | mutation battery | **58 MUST_FAIL**, **4 MUST_SURVIVE**, **19 theorem-separation controls**, **5 gate unit tests**; 0 failed entries; separation census `{uncond_true_e_false: 8, both_true: 8, uncond_false: 46}` |
| P6 | pinned hashes | 8 boolean comparisons, all true (census, observable, gp script, gp gate count, observable count against both the GP prediction and the pin, runner constants, E-layer observable set) |
| P7 | emission policy | components `["K0"]`, idempotents `[0,1]`, count 1; forbidden-language scan CLEAN on `result.json`, on `mutations.json` in refusal-record mode, and on the GP text as a proxy for `gp_stdout.txt` |
| P8 | isolated-import controls | **8/8** (see §4) |
| P9 | authority controls | **33 authorization records** + template refusal + artifact-collision (3 assertions) + run-directory reuse (2 assertions) |
| P10 | gate-surface controls | **10 probes**, one per R1 defect class |

`seal_r2.py --root . --verify` → `ok: true`, all four `matches_disk` true; the
archive is byte-deterministic (PAX, sorted members, uid/gid 0, empty
uname/gname, mtime 0, mode 0444).

### 3.1 The eight isolated-import controls (P8)

| control | command shape | required outcome | observed |
|---|---|---|---|
| N1 | `python3 -I -B -c "import k0_field_checker_r2"` in the packet dir | fails with `ModuleNotFoundError` | rc 1, `ModuleNotFoundError: No module named 'k0_field_checker_r2'` — **the exact R1 fault, reproduced live** |
| N2 | `python3 -I -B runner_r2.py --import-smoke` | rc 0 | `IMPORT_SMOKE_OK manifest 8bfdd426… modules 3 gates 42 mutations 62` |
| N3 | smoke against a copy with one tampered module byte | rc 70 `SEALED_MODULE_HASH` | as required |
| N4 | smoke against a copy whose manifest omits a module | rc 70 `SEALED_MODULE_UNMANIFESTED` | as required |
| N5 | smoke with `--packet-manifest-sha256 0…0` | rc 70 `PACKET_MANIFEST_BINDING` | as required |
| N6 | smoke **without** `-I` | rc 70 `SMOKE_NOT_ISOLATED` | as required |
| N7 | `--smoke-packet-dir` without `--import-smoke` | rc 70 `SMOKE_FLAG_MISUSE` | as required |
| N8 | production args **without** `-I` | rc 70 `NOT_ISOLATED` | as required |

N3–N5 are the negative controls on the loader's *authority*: the loader will
not accept a module whose bytes differ from the manifest, a module the
manifest does not list, or a manifest the authorization does not bind. N6–N8
are the negative controls that keep the repair from weakening isolation: the
smoke is only meaningful under `-I`, the test-only flag cannot reach the
production path, and production refuses a non-isolated interpreter.

### 3.2 The ten gate-surface controls (P10)

Each names an R1 defect, the R1 behaviour, and the R2 requirement.

| probe | R1 behaviour | R2 observed |
|---|---|---|
| `D2_absurd_phi42` | `RANK432_MONIC_BASIS`, `GALOIS_STABILITY`, `NONABELIAN` all PASSED on `phi42 = x^12+5` | `RANK432_INDEPENDENCE` FAIL, `SRC_PHI42_LITERAL` FAIL, `PHI42_DISCRIMINANT` FAIL, `RELATION_LEADING_TERMS` PASS *for the stated reason* |
| `D3_broken_sigma` | the relation loop computed `sigma({}) == {}` | `GALOIS_STABILITY_FREE` FAIL |
| `D4_frames_halved` | passed all 36 R1 gates | `FRAME_RELATIONS` FAIL |
| `D4_pointbank_halved` | passed all 36 R1 gates, no observable shadow | `POINTBANK_REGRESSION` FAIL |
| `D5_r3_exponent_duplication` | L1 failed, L2 kept certifying the true object | `BASE_WELLDEFINED` FAIL **and** `KUMMER_HOMS_EXHIBITED` FAIL |
| `D1_pure_L5_mutation` | `unconditional_k0_theorem: false` with zero L0–L4 failures | unconditional **true**, conditional **false**, zero L0–L4 failures |
| `D1_corroboration_only` | corroboration fed both booleans | both booleans **true**, `all_pass` false |
| `D10_trivial_representative` | the `(0,0)` need was dead code | `KUMMER_REPRESENTATIVE_CLASSES` FAIL |
| `D10_eps_datum` | the line was constant-true and its message backwards | `KUMMER_NORM_COROBORATION` FAIL |
| `D12_static_census_falsifiable` | predictor combined nested loops by `max` | deleting a gate line → 109, duplicating → 111, a parenthesised comment → 110 (unmoved) |

---

## 4. The AWS import repair, in detail

`runner_r2.py` computes `PACKET = Path(__file__).resolve().parent`, refuses
unless that directory is named `d43_k0_field_certificate_r2_20260829`, parses
`PAYLOAD.sha256` (every line must be a 64-hex digest and a path inside
`cases/<packet>/` with no further separator), and then, for each of
`k0_algebra_r2`, `k0_field_checker_r2`, `k0_mutations_r2` in dependency order:

1. rejects a symlink or non-regular file;
2. recomputes the SHA-256 and requires equality with the manifest entry;
3. builds an `importlib.util.spec_from_file_location` on the **absolute path**;
4. registers the module in `sys.modules` *before* `exec_module`, so a sibling's
   plain `import k0_algebra_r2` resolves out of `sys.modules` and never touches
   any filesystem search path;
5. asserts `sys.path` is byte-identical before and after (`SYS_PATH_MUTATED`).

The manifest's own digest is compared against `--packet-manifest-sha256`, which
the supervisor passes down from `authorization["packet_manifest_sha256"]`. So
the module load is bound to the coordinator authorization, not to a value the
packet recomputes about itself. Isolated execution is not weakened: `-I -B` is
retained in `aws_worker_r2.sh` and `aws_supervisor_r2.py`, and `runner_r2.py`
now *refuses to run* if `sys.flags.isolated` or `sys.dont_write_bytecode` is
false.

`--import-smoke` performs exactly this load and nothing else — no pointbank,
no mathematics, no artifact — and requires isolated mode itself. That is what
P8/N2 executes.

---

## 5. D1–D13: repair or explicit retained debt

### D1 — theorem booleans entangled through the census — **REPAIRED**

Three census gates replace one: `CENSUS_UNCONDITIONAL` (all L0–L4
non-`CORROBORATION` gates), `CENSUS_CONDITIONAL` (all L5 non-`CORROBORATION`
gates), `CENSUS_COMPLETE` (whole registry, integrity only). Then

```
unconditional_k0_theorem = all(L0-L4 non-CORROBORATION PASS) and CENSUS_UNCONDITIONAL
e_conditional_ratio_theorem = all(L5  non-CORROBORATION PASS) and CENSUS_CONDITIONAL
corroboration_ok            = all(CORROBORATION PASS)
execution_integrity         = all_pass and CENSUS_COMPLETE
```

`result.json` publishes `theorem_inputs` with the three gate lists; P4 asserts
they are pairwise disjoint. 19 battery entries pin the `(unconditional,
conditional)` pair they must report and the battery refuses unless at least
one entry reports `(true,false)` and at least one reports `(true,true)`;
observed 8 and 8. `GATE_UNIT_CORROBORATION_SEPARATION` skips
`POINTBANK_REGRESSION` and requires `(true, true, all_pass=false)`.

### D2 — `RANK432_MONIC_BASIS` unfalsifiable, `confluent_on_basis` asserted — **REPAIRED**

The asserted literal is deleted and the gate is retyped `EXECUTED` and renamed
`RANK432_NORMAL_FORM`; its detail string now says what it is worth. Two new
`THEOREM` gates carry the rank:

* **`RELATION_LEADING_TERMS`** works in the *free* ring `Q[z,r,A1,A2,h]`
  (`k0_algebra_r2.fp_*`, graded lex). It computes the leading monomial of each
  of the five relations, requires them to equal the declared
  `spec.leading_monomials`, requires each to be a pure power of *its own*
  generator with exponent `spec.basis_shape[k]`, requires the five to be
  **pairwise coprime**, and requires every tail monomial to be undivisible by
  any leading monomial. Pairwise coprime leading monomials satisfy Buchberger's
  first criterion, so the five are a Gröbner basis and the standard monomials
  are exactly the declared box — an executable proof of Lemma L1 for whatever
  monic presentation `Spec` declares. Graded lex is a legitimate order here
  because `deg A1^3 = 3 > deg r = 1`, `deg r^2 = 2 > 0`, `deg h^2 = 2 > 0`, and
  `Phi_42`'s tail has degree ≤ 11.
* **`RANK432_INDEPENDENCE`** is a mod-`p` witness at the registered prime
  105337. The 432 standard monomials evaluated at the 432 `F_p`-points give a
  Kronecker product of three blocks: a 12×12 Vandermonde on the primitive 42nd
  roots (each independently checked to be a root of `spec.phi42` mod `p`), an
  18×18 on the `(r, A1, A2)` points, and a 2×2 on the `h` roots. All three
  determinants are nonzero, so the 432 monomials are `F_p`-independent.

  Two independent confirmations that this is real arithmetic and not a
  restatement, computed here outside the packet:
  `det(V_z)^2 = 101851 = disc(Phi_42) mod 105337` **exactly** (the squared
  Vandermonde determinant *is* the discriminant), and
  `det(M_h)^2 = 6 = disc(h^2 - 3/2)` exactly. The middle block's
  `det^2 = 35131 ≠ 0`, and an independent cube-residue census confirms the
  middle system has exactly 18 `F_p`-points, so the frame × `mu_3`
  construction is the complete solution set and matches what GP builds from
  `polrootsmod`. The three squared determinants are row-order independent and
  are shared observables.

**Scope honesty, stated in the README and executed in P10.**
`RELATION_LEADING_TERMS` is deliberately blind to *which* monic degree-12
`Phi_42` is used, because freeness genuinely holds for any of them. Fed
`x^12+5` it correctly passes while `RANK432_INDEPENDENCE`,
`SRC_PHI42_LITERAL` and `PHI42_DISCRIMINANT` all fail. The R1 gate passed on
all four.

### D3 — `GALOIS_STABILITY` relation loop vacuous — **REPAIRED**

`GALOIS_STABILITY_FREE` builds the five *unreduced* relations, builds sigma
from the mutable `spec.sigma_images` table, checks sigma is an involution on
each generator, substitutes it into each relation with `fp_substitute`, and
requires the image to be a member of the relation set. The induced permutation
must equal `spec.sigma_relation_permutation` and must not be the identity.
Because sigma permutes the ideal *generators*, `sigma(I) = I` and sigma
descends to a ring automorphism; `Delta` is `Gal(B/Q)`-stable and `K0/Q` is
Galois. `GATE_UNIT_SIGMA_FREE_VS_QUOTIENT` runs the R1 shape and the R2 shape
side by side on the broken table `r ↦ +r` and asserts the R1 shape accepts it
and the R2 shape does not.

### D4 — no cardinality or prime-set pins — **REPAIRED**

`_frame_cardinality` pins `len(spec.frames) == spec.frame_count_expected` and
the frame prime multiset against `spec.registered_primes`, and is called by
all four L4 gates. `POINTBANK_REGRESSION` pins
`len(spec.pointbank_expected) == spec.pointbank_count_expected` and its prime
set against the same field. `KUMMER_SILENT_PRIME_GUARD` additionally requires
the silent-prime list to be the registered set. Four MUST_FAIL entries
(`M_FRAMES_HALVED`, `M_FRAME_PRIME_SET`, `M_POINTBANK_HALVED`,
`M_POINTBANK_PRIME_SET`) plus two P10 probes reproduce the two unintended R1
survivors and require them to fail.

### D5 — gate-body literals duplicating `Spec` — **REPAIRED**

`_character_frames` reads `spec.r3_exponents` and `spec.alpha_data`;
`POINTBANK_REGRESSION` builds `E` through `_E_mod` from `spec.e_terms`. The
presentation itself moved into `Spec` and into the `K0Algebra` constructor:
`alpha_data`, `r_square`, `h_relation`. A mutation of any of them now moves
the normal form, the free relations, the frame equations, the character layer,
the split count and the rank witness together. P10's
`D5_r3_exponent_duplication` shows `BASE_WELLDEFINED` **and**
`KUMMER_HOMS_EXHIBITED` both firing, where R1 fired only the former.

Additionally, and beyond the review's request: `FIELD_DEGREE_432` no longer
multiplies the literals `48` and `9`. `BASE_DIMENSION_48` publishes the
computed `deg Phi_168` into `ctx`, `KUMMER_RANK_TWO` publishes the computed
subgroup order, and L3 multiplies those two. `M_KUMMER_RANK_DROPPED` and
`M_BASE_DIM_DROPPED` delete each source gate and require `FIELD_DEGREE_432` to
fail. The GP engine got the same treatment: `GENORDER` is set by the L2 loop
and L3 checks `poldegree(P168)*GENORDER == BASIS_RANK`, replacing R1's
`9*48 == BASIS_RANK`.

### D6 — battery coverage gaps — **REPAIRED**

All seven fields the review named have mutations (`M_BASE_S2_EXPONENTS`,
`M_BASE_GEN_Z8_POWER`, `M_I_ZETA3_EXPONENT`, `M_SILENT_PRIMES`, `M_P2_PRIME`,
`M_FRAME_SECOND`, `M_CHAR_PRIME_DUPLICATE`), and every new `Spec` field has
one too. The battery went from 35 + 2 to **58 MUST_FAIL + 4 MUST_SURVIVE**.
The two new survivors are the reordered certificate primes and the all-inverse
representative set — two of the three the R1 reviewer constructed by hand.

### D7 — GP printed `E_CONDITIONAL` with no `E`-reading gate — **REPAIRED, both ways**

The GP terminal flag is now `E_BASE_IDENTITIES` and the runner's
`TERMINAL_LINE` regex was changed to match. GP's L5 block now genuinely reads
the literal `ETERMS` data: it checks the term count, that the generators are
`A1` and `A2` in that order, that both exponents are 4, that the two
coefficients are conjugate (`ECROSS == 0`), that `C1*C2 == ENORM` in `B`, that
`CBASE` built from those coefficients satisfies `C1*CBASE == -C2`, that
`CBASE == -(2-r3)^3`, and finally the reduction

```
(alpha2/alpha1) * s^4  ==  CBASE .
```

That identity is the entire `E`-conditional content that a base-level engine
can carry: with `q0 = u*s` one has `q0^4 = u^4 s^4`, and `q0^4 = c = CBASE*u`
is equivalent to `u^3 * s^4 = CBASE`, i.e. to the displayed identity plus
`u^3 = alpha2/alpha1`, which is exactly the two cubic defining relations.
Hand-checked here: `(2-r3)*(4r3-7) = 15r3-26 = -(9-5r3)^2/6`. A separate
`E_BASE_REDUCTION` gate runs the same chain in the Python 432-monomial
algebra, and the four `e_*` observables are shared.

**And the terminal is retyped.** `E_CONDITIONAL_RATIO_THEOREM` now carries
`"engines": ["stdlib Python"]`, `"single_engine": true`, a
`single_engine_reason` naming the missing cube-root layer, and
`"corroborated_by": ["PARI/GP E_BASE_IDENTITIES flag", "4 shared E-layer
observables"]`. The unconditional theorem keeps its two-engine claim, and its
`engine_agreement` string counts only the 25 unconditional observables.
The GP engine also splits its accumulators (`ok` for L0–L4, `okE` for L5), so
an L5 failure cannot flip the unconditional banner.

### D8 — authorization checks incomplete — **REPAIRED**

`validate_authorization_record` is a pure, I/O-free function. It requires
`reviewer_pass.verdict` to be a `str` **identically equal** to `"PASS"`, and
refuses any model whose normalisation (`lowercase`, all non-alphanumerics
stripped) contains `opus`. Preflight P9 exercises it on 33 crafted records
including `pass`, `PASS `, `Pass`, `PASSED`, `<MUST_BE_PASS>`, `true`, absent;
`Opus 5`, `OPUS5`, `opus-5`, `Opus5`, `  Opus  5  `, `claude-opus-5`,
`Opus 5 (max reasoning)`, empty, absent; `Fable 5` and `GPT-5.6` accepted;
plus route, schema, status, `coordinator_go`, instance type, host label, gp
version, hash shapes and path shapes. It also asserts that the shipped
`authorization_template_r2.json` is **refused** (`AUTHORIZATION_STATUS`).

### D9 — `alarm(600)` versus the 120 s cap — **CLOSED BY DELETION**

The optional `nffactor` block is removed outright. It was never on the theorem
path. Two consequences: the runner no longer skips `OPTIONAL` lines, so **any**
unrecognised GP output line is now a fault; and `nfinit`, `nffactor`,
`rnfequation`, `alarm`, `znlog`, `znprimroot` are all absent, which P3's
hygiene scan enforces.

### D10 — constant-true sub-checks — **REPAIRED (with named retained pins)**

* `BASE_CONDUCTOR_TOWER` computes `disc(x^2 - r_square)` by resultant and
  computes `deg Phi_21 = 12`, `deg Phi_84 = 24`, `deg Phi_168 = 48`, comparing
  against `spec.basis_shape` products and the `ctx` base dimension. The
  divisibility relations now read `spec.conductor_tower`.
* `KUMMER_NORM_COROBORATION` reads `spec.alpha_data` and `spec.eps_data`,
  computes both norms and the rational product, verifies the `r`-part
  vanishes, verifies `N(eps) = 1`, verifies **both** embeddings are positive
  via trace > 0 and norm > 0 (the R1 message asserted the opposite and was
  constant-true), enumerates the nine residue pairs showing `x^2-3y^2 ≡ -1`
  is impossible mod 3, and shows the only `b = 1` unit constant is 2.
* The vacuous within-fibre character equality is replaced: Python now checks
  `Phi_168(omega) ≡ 0 (mod p)` for each of the 48 homs (non-trivial, since it
  gets them from an order test) and pins the two fibre sizes to 24; GP checks
  the mirror-image non-trivial direction, that each `polrootsmod` root has
  **exact order 168**, and pins the equal halves.
* The dead `(i,j) != (0,0)` need moved ahead of the witness search.
* `NONABELIAN` computes `alpha1*alpha2` in the algebra, requires it rational,
  and computes `disc(t^3 - m)` by resultant instead of asserting `6` and
  `-972`; Eisenstein primes come from `factor_small(m)`.

**Retained by design** (all `Spec`-routed and mutation-covered, so none can
pass by recomputing a literal from *itself*, but each is a declared target
rather than a derivation): `IDEMPOTENTS_ONLY_0_1`'s `("K0",)` and `(0,1)`;
`RAMIFIED_EXACTLY_2_3_7`'s `(2,3,7)` and witness `5`; `FIELD_DEGREE_432`'s
`basis_rank == 432`; the GP mirrors of the same three. These are emission and
scope policy pins whose mathematical content lives in
`FIELD_DEGREE_432`/`KUMMER_RANK_TWO` (fieldness and degree) and in
`ETALE_OVER_Z_1_42` plus the subfield discriminants (ramification). Mutations
`M_COMPONENT_PRODUCT`, `M_IDEMPOTENT_LIST`, `M_RAMIFIED_SET`,
`M_UNRAMIFIED_WITNESS`, `M_DEGREE` cover them.

Also retained, with the review's own reasoning: the `L1 CRT` line (redundant
belt-and-braces, both sides read the same mutable exponents, fired by
`M_BASE_SURJ_EXPONENT` and `M_BASE_GEN_Z8_POWER`), and `SPLIT_COUNT_432`'s
`CONSISTENCY` typing with the `L × L × L` caveat verbatim in both engines.

### D11 — `emit_immutable` window and `RUN_DIR_REUSE`'s three-name list — **REPAIRED**

`emit_immutable` now creates the **final** name with
`O_WRONLY|O_CREAT|O_EXCL`, writes, `fsync`s, `fchmod`s to `0444` on the open
descriptor, and `fsync`s the directory. There is no `.tmp` sidecar, no
exists-then-replace window, and no temporary name that could collide with a
member; the collision semantics *are* the atomic create. `atomic_bytes` in the
supervisor got the same treatment. `check_run_dir_clean` pins the whole
pre-run directory listing to exactly `{job_marker.json,
execution_pins_live.json}` instead of asking about three names. The
archive-replay `or` fallback is gone: an explicit per-member expectation table
is built, including `manifest.json`. P9 executes the collision, the mode, the
size cap and the reuse refusal.

### D12 — static-census predictor fragilities — **REPAIRED**

Nested loops multiply instead of taking `max`; comments and string literals
are stripped before the parenthesis scan; loop bounds are resolved from the
file's own vector declarations (`#CERTPRIMES` → 2, `#SILENT` → 2) rather than
a hardcoded table; a loop whose trip count cannot be resolved and which
encloses a gate site makes the prediction refuse rather than guess. P10 mutates
the GP text three ways and requires 109 / 111 / 110. A new label audit bounds
all 99 printed labels against the runner's 80-character parse window (observed
max 63) and requires the file to be ASCII and tab-free — a hand check in the
R1 review, executed here, because an over-wide label would burn a rehearsal
exactly as the import defect did.

### D13 — dead code — **REPAIRED**

`SAFE_ID_RE` and the unused `signal` and `socket` imports are gone from the
supervisor. The runner's `GP_DATA_DIR` passthrough is gone (the supervisor
forbids the variable, so passing it was dead). The `OPTIONAL` line-skip is
gone with the block it served.

---

## 6. Route, schema and custody changes

* Route `D43-K0-FIELD-CERT-R2`; schemas `…-checker-r2`, `…-runner-r2`,
  `…-mutations-r2`, `…-preflight-r2`, `…-prereg-r2`, `…-launch-auth-r2`,
  `…-job-marker-r2`, `…-aws-terminal-r2`, `…-execution-pins-r2`. Every file
  name carries `_r2`.
* **AWS-only live identity preserved.** IMDSv2 token, identity document, three
  live tags; no local-execution mode; `NO_LIVE_EC2_IDENTITY` on any failure.
* **Exact binding preserved.** Root-owned symlink-free authorization, source
  archive and `gp` binary; archive hash; `PAYLOAD.sha256` hash and every packet
  member hash; live instance id / type / image / region against the record.
* **Instance type collapsed** from R1's six-member allowlist to the single
  `r6i.large` the rehearsal actually ran on, as the review asked. Extending it
  is a source change and a new R-number.
* **gp binary.** Still coordinator-supplied and runner-verified against the
  on-disk file. `execution_pins_r2.json` records the R1-observed hash
  `c9673623…` as `r1_observed_gp_binary_sha256`, explicitly informational; the
  supervisor reports `gp_binary_matches_r1_observation` in the terminal core
  and does **not** gate on it. Gating a hash observed on a now-terminated
  ephemeral host would block a legitimate rehearsal for an operational reason;
  reporting the drift is the honest middle.
* One core, 1 GiB, zero swap, `TasksMax=24`, `RuntimeMaxSec=300`,
  runner 240 s, gp 120 s: all unchanged.
* **One atomic run lease, plus a new authorization lease.**
  `claim_authorization_lease` takes `O_CREAT|O_EXCL` on
  `<run_parent>/.jc2-k0-r2-authorization-<digest>.lease` after checking the
  parent is root-owned and not group/world-writable, and `claim_run_path` then
  does the atomic `mkdir`. **Both are outside the try block**, so a refused
  second launch writes no terminal at all. This is what makes a crashed or
  `NO_VERDICT` R2 authorization non-reusable *even with a fresh run path* —
  the failure mode R1 could not exclude. A retry requires a new coordinator
  record, a new digest and a new live tag.
* **Fail-closed terminal behaviour preserved and extended.** The runner's
  fault path writes no terminal (stderr + exit 70). The supervisor publishes
  exactly one terminal through `publish_terminal`; the fault path sets
  `verdict: NO_VERDICT` and all four status fields to `NO_VERDICT` with
  `credited_* = false`. The success path replays the manifest and the archive
  before installing anything.

---

## 7. What the terminal will and will not say

Four separated blocks, and a stated crediting rule:

```
K0_UNCONDITIONAL_THEOREM     PASS/FAIL   two engines, L0-L4 layer census
E_CONDITIONAL_RATIO_THEOREM  PASS/FAIL   one engine (Python), L5 layer census
EXECUTION_INTEGRITY          PASS/FAIL   census, battery, engine agreement,
                                         manifest/archive replay, environment
CORROBORATION                PASS/FAIL   pointbanks + GP base identities
credited_k0_unconditional  = K0 theorem AND execution integrity
credited_e_conditional     = E  theorem AND execution integrity
```

with `"crediting_rule": "a theorem status is credited only jointly with
EXECUTION_INTEGRITY = PASS; corroboration is reported and never credited"`.

Nothing anywhere claims a D43 row, point, template, D25, raw-J, branch
survival, Keller or JC2 result; nothing derives fieldness from the 432-frame
count; nothing claims the GP engine has ever run. The preregistration's
`forbidden_claims` list carries the last of these explicitly.

---

## 8. Retained debt, stated plainly

1. **The GP file has never been parsed.** No amount of static review retires
   this. Every failure mode lands fail-closed in the runner (`GP_EXIT`,
   `GP_UNPARSED_LINE`, `GP_GATE_COUNT`, `GP_CENSUS`, `GP_OBSERVABLE_COUNT`,
   `GP_TERMINAL`, `ENGINE_DISAGREEMENT`) — a refusal, never a wrong verdict.
   R2 *increases* the unexecuted surface in two places (`matrix`/`matdet` for
   the rank witness, multivariate `subst` for the free-ring sigma) and
   *decreases* it in several (`Map`/`mapput`/`mapget`/`Mat(t_MAP)`, `nfinit`,
   `nffactor`, `alarm`, `znlog`, `znprimroot`, `select`, closures, the whole
   optional block). Net: fewer distinct constructs than R1, but two new ones.
   The reviewer should read them adversarially.
2. **Prose steps the certificate does not re-prove.** `Z[zeta_n]` maximality,
   the Kummer correspondence `[L:B] = |Delta|`, the equal-dimension surjection,
   the local-unit descent behind the character argument, and the abelian
   descent lemma all live in the theorem report and are grok46-CONFIRMED. The
   certificate's executable shadow of the valuation step is still only the
   `(3 ± r) mod p ≠ 0` residue check.
3. **The E theorem is single-engine and conditional.** Both facts are now in
   the terminal, the preregistration and the README.
4. **Registered-target pins** (`432`, `{2,3,7}`, witness `5`, `["K0"]`,
   `[0,1]`) are `Spec`-routed policy pins, not derivations. Listed in §5 D10.
5. **`is_cube`** in `KUMMER_NORM_COROBORATION` brackets a float cube root by
   ±2, which is exact for the norms it sees (6 and 36) but is not a general
   integer cube test.
6. **The label-width estimator is an upper bound**: a comma inside a label
   string is conservatively counted as one more interpolated argument.
7. **`preflight_r2.py` P8 uses `sys.executable`** on the producer host. It
   demonstrates the loader and the R1 failure shape; it is not a test of the
   AWS host's interpreter.
8. The `r6b` → `r6i.large` and `gp` binary pins reflect one terminated
   ephemeral host. If the next host differs, the packet refuses on the type
   (new R-number) and reports on the binary.

---

## 9. Status and the only licensed next action

The packet is `SOURCE_READY_AWS_NOT_AUTHORIZED`. It is **not** authorized, not
launched, and not reviewed.

**The only licensed next action is a different-model hostile source review of
`cases/d43_k0_field_certificate_r2_20260829/`**, charged by that packet's
`REVIEW_REQUEST.md`. Not a launch, not a coordinator GO, not a ledger edit, and
not a GP rehearsal. A PASS from that review is one of three separate
preconditions for execution; the others are the coordinator GO recorded as
`coordinator_go = true` and the coordinator-supplied `gp` binary path and
SHA-256. Since the reviewer's report hash and model go into the authorization,
and the supervisor now requires the verdict to read exactly `PASS` and refuses
any model normalising to contain `opus`, the review must be produced by a
different model than the producer of this report.

Files written by this task: the packet directory
`cases/d43_k0_field_certificate_r2_20260829/` (19 files) and this report.
Nothing else on this host was created, modified or deleted.
<!-- self-hash -->
46a4f6ceb226d51e8e8bb8c693044f5a82c026bbfa17752c7b644565ab2515ab  report body above this delimiter
