# D43 `K0` field certificate R3 — hostile source review (Grok 4.6)

**Verdict: `PASS_WITH_REPAIR`**

**UTC:** 2026-08-29
**Reviewer:** Grok 4.6 (model id `grok-4.6`), independent of the R3 producer (Opus 5)
**Object:** `cases/d43_k0_field_certificate_r3_20260829/`, status `R3_SOURCE_READY_AWS_NOT_AUTHORIZED`
**Charge:** that packet's `REVIEW_REQUEST.md` (SHA-256 `ff3a8e73cb4bd31607832c9eaf7f10e662884bb397ad302e171ba05bafc289ca`)
**Producer report read:** `xmodel/d43-k0-field-certificate-r3-lease-repair-opus5-20260829.md`

## What this verdict licenses, exactly

* It licenses **nothing on AWS**. `aws_supervisor_r3.validate_authorization_record` requires `reviewer_pass.verdict` to be exactly the string `PASS`. This report's verdict is `PASS_WITH_REPAIR` and therefore **cannot enter an authorization record**. Any authorization citing this report's hash must be refused.
* It records that the **R2 mathematics, both engines' source, and the mutation battery are unchanged and confirmed**, after a mechanical R2→R3 diff (below). The Fable 5 R2 review (`824e24d794e8828de6a3f5b9c9b0b40bf93305f72a06fd91275a6e89933f3602`) may be cited for layers §5–§6 of that review. I re-checked the charged attacks on those layers against the R3 files; I found no path to a wrong Python PASS.
* It records that **R2's blocking REPAIR-1 (lease unsatisfiable for `jc2k0`) is repaired in code**: the service never creates anything in the sealed parent, the run directory is pre-created and service-owned, the claim token is root-minted 0444, and the consumption lease is taken inside the run directory after every precondition. R2's producer-found REPAIR-2 (run-directory law missing `source`) is also repaired and mutation-tested.
* It requires **one repair before any launch authorization** (REPAIR-1 below): the sealed coordinator deployment order is jointly unsatisfiable with the unit's `ExecStartPre=+ mint_claim_r3.sh`. A coordinator who follows `authorization_template_r3.json` as written will mint, dry-run, then start the unit, and the second mint dies `MINT_ALREADY_SPENT` before the supervisor runs. That is the same never-executed-integration class as R1's `-I` import and R2's lease. The repair is the choreography (template + unit), not the mathematics.
* A source `PASS` of any kind is **not** coordinator authorization and **does not** imply that GP, systemd, or the deployed root-owned half has run.

The GP engine **has still never been parsed by any GP**. Nothing here changes that.

---

## 1. Execution gap, stated first

There is no PARI/GP on this host (`gp` is a shell alias for `git push`; `shutil.which("gp")` is `None`). Following the charge I did **not** install one and did **not** launch AWS. `k0_field_cert_r3.gp` was reviewed **by adversarial source reading and static census only** (§7). Every statement below about GP is a statement about source text and about PARI 2.15 documented semantics, not about an execution.

No fixture here created a root-owned object. No fixture ran under systemd. uid of this review host is 501. The custody controls refuse to run as root; I ran them as an ordinary user.

Linux/PARI obligations **not executed**, and not to be read as executed:

| obligation | status |
|---|---|
| PARI/GP 2.15.4 parse or run of `k0_field_cert_r3.gp` | **unexecuted** |
| systemd unit (`ExecStartPre=+`, `ExecStopPost=+`, `ReadWritePaths`, empty `CapabilityBoundingSet`, `NoNewPrivileges`) | **unexecuted**; checked as a contract against supervisor constants |
| root-owned sealed parent, spent ledger, claim token | **unexecuted** on this host; same `verify_custody_preconditions` is what `--on-host-dry-run` would call on the deployed host |
| IMDSv2 identity, live tag, cgroup-v2 one-core zero-swap | **unexecuted** |
| mint as root, retire as root | **unexecuted**; non-root invocations were executed and refused (rc 77) |

Everything else charged was executed: sealer verification, full preflight under normal Python **and** `python3 -O`, standalone custody selftest, standalone mutation battery with named-gate extraction, and my own surviving-mutation probe.

A source PASS_WITH_REPAIR is not evidence the GP file runs, and is not evidence the deployed privilege boundary has run.

---

## 2. Charged inputs, verified byte-exact

All nine frozen externals match the review request's table and `execution_pins_r3.json` (recomputed with `shasum -a 256`):

| file | SHA-256 |
|---|---|
| `cases/d43_common_integral_emitter.py` | `5420b5c0b4164c719e98316cade96c094c2945a6fed8bad3ac0926771855984d` |
| `cases/d43_exact_sparse_rows_v2_20260828/selected_rows_v2.py` | `9fc9bd7a365827ddba2c1ba45cbb34870d6f2d71c9d3eecb6b242d46e00990b2` |
| `cases/d43_full_pointbank_p105337.pkl` | `bb0f13b61616c486116027e284483a4fb0f529f8df2dca7f728d56584d98fcbb` |
| `cases/d43_full_pointbank_p105673.pkl` | `b933cdb5b72bd4073da0cb82150db768f6b4607d5cd29d3d4aec0fe22ce5bcc3` |
| `xmodel/d43-e5-e6-elimination-bridge-gpt56-20260828.md` | `e1b99600b01f91f7b95df4f7f969481efa1e7b1ee377e83156f3f6b6a8e3c863` |
| `xmodel/d43-k0-splitting-primary-research-opus5-20260828.md` | `6d3d53c20387d324766daaf40eb502df42d9e2776c6ab6053041bc1f3dee1430` |
| `xmodel/d43-k0-field-theorem-hostile-review-grok46-20260829.md` | `07f20be55add0fea0ff6329ce0d4ca386024af33edad33254d46451fd575a94a` |
| `xmodel/d43-k0-field-certificate-r1-hostile-review-fable5-20260829.md` | `29e9496e0552f94d6823c744b7b979ad02274e6cbf39ae124ec01e6465d596e2` |
| `xmodel/d43-k0-field-certificate-r2-hostile-review-fable5-20260829.md` | `824e24d794e8828de6a3f5b9c9b0b40bf93305f72a06fd91275a6e89933f3602` |

Sealer `--verify`: `ok: true`, 28 archive members, all four `matches_disk` true.

```
PAYLOAD.sha256            d245952f26e2252a9eae46fea927a33806c93989b717b4528c5c5a4d253e9d02
SOURCE_ARCHIVE.tar        403f790afa9904962b4ad79ebb29cf50ef21c399bbf598f5007c771ee1002a37
SOURCE_ARCHIVE.sha256     d86de271f3998c265f906bdf95ca575f4ba56e3f5914d1434f3394469f52f7ef
SOURCE_SEAL.sha256        3371887839cb98b6afeb99c78c186f12adb046a9ddebc68e3c93218f8bceeb8d
```

Packet members (recomputed; agree with `SOURCE_SEAL.sha256` and the producer report §2.1):

```
README.md                      56f1fb1bd8a22a65967e8c78945c2940ee87e554564f3792ee05b0cea0df979a
REVIEW_REQUEST.md              ff3a8e73cb4bd31607832c9eaf7f10e662884bb397ad302e171ba05bafc289ca
authorization_template_r3.json 84727c5af08ba29169d1f73abc399a803edbf72325cb7f5ac178bf0795d29a5b
aws_supervisor_r3.py           83c80c65a108339af68e75fe5ab52d2ed2b797130456ff02685e8179f2f71b0b
aws_worker_r3.sh               aab607c8debc13fabe5ea4c35d13ae5d10309ee34db890f5a60c2b93ba122df8
custody_selftest_r3.py         28feaf3bbfb5fbd356fc87cfe0bdc33afb6c971d23a25888624718e933c02de8
execution_pins_r3.json         4a1e38f2f89b8f8d5137f8cce72539e541591d1621ce34ac8533d6f33647d5c4
k0_algebra_r3.py               a7de3c3fcefc42302e402b8dfcaeefbba6d5a582ae694447e8f95f6a8e8dd4a6
k0_field_cert_r3.gp            5775b63e304378f5092355f02f129f0654e1ff9c6c883dfcd866f4ebdd17c5eb
k0_field_checker_r3.py         9f82ae1f36a88d55b021cc1e73482a5ccb11d4c6b61d6b10bdc3c4a4020afb18
k0_mutations_r3.py             99671b83e2fc2d2cd179fe46acde509cf1846f95407b5b6ec1e1343166465726
mint_claim_r3.sh               fd709ee6bba1d2388140dd02c6f0558f448503c40ab3b6e0e1c648c43f533983
preflight_r3.py                d58fa4674c50c282b38d62a00fbd59bf051025da8357d2722f77666d2103e9c6
preregistration_r3.json        e273546a4d8ac696a1b20f14b7852f179b6ba093ccaf807f021c1713a4769896
retire_claim_r3.sh             832ee9d2384f37f3f00453acaeb4e8dc30f522dd6775f7d698d8da3a6173564f
runner_r3.py                   8d21fb9394b6b24cc66fbf8f962062b807af6dd0fdc639b6fb9327df18ff4fd3
seal_r3.py                     dfbf046fb4b980dbdda8977eb0f4f02f4e8a9190d88f63a2f50a8644292f4d6b
systemd_unit_template_r3.service b9de00ee60294654d962a1512641f94169c47197b5846c2612c643e7ea23ca81
```

Charge-document note, not a packet defect: `REVIEW_REQUEST.md` §"How to replay" still expects GP script SHA-256 `c3f576dd5bbc1c0af970246379c97d1c541daa7ae521f722ed43f905e4713d76` (the **R2** file). The R3 file and `execution_pins_r3.json` pin `5775b63e…`. P6 checks the pin against the R3 file and passes.

---

## 3. R2 → R3 diff, verified first

The charge says the mathematical layers may be cited as already-reviewed only if this diff is what it claims. It is, with one understatement in the charge table.

After the length-preserving R-number token rename (`_r2`→`_r3`, `-r2`→`-r3`, `CERT-R2`→`CERT-R3`, packet dirname):

| file | result |
|---|---|
| `k0_algebra_r3.py` | **byte-identical** to `k0_algebra_r2.py`, SHA-256 `a7de3c3fcefc42302e402b8dfcaeefbba6d5a582ae694447e8f95f6a8e8dd4a6` |
| `k0_field_checker_r3.py` | remaining diff is the docstring title `R2`→`R3`. The import and `SCHEMA` changes are exactly the token rename. No gate body, census, or typing change. |
| `k0_mutations_r3.py` | remaining diff is the docstring title `R2`→`R3`. Imports, schema, and the 58+4+19+5 battery are the token rename. Battery SHA-256 unchanged. |
| `aws_worker_r3.sh` | identical after rename |
| `k0_field_cert_r3.gp` | header/comment block; three data variables `Z42E=4`, `Z8E=21`, `GENE=[5,16]`; three use sites (zeta8, GENERATION, CRT+`crt_residue` now through those and `CONDTOWER[3]`); `[R3-B]` comment on the unreachable within-fibre branch. Gate count, label set, observables, printed values claimed unchanged; static census still 110/110. |

The charge table said the checker diff was "one import line and one schema string". After rename the leftover is the title line. The producer report §3.1 is the accurate inventory. Not a defect.

`validate_authorization_record` and `normalize_model` are byte-identical to R2 after the R-number token rename. Frozen, as claimed.

Census `b828f93d6a29c15371e4d277473e63c0a25ba0280fa5ab44706d10c786f9aeb0`, observables `4b1c7ff63935adb27148a2967037b7a357354848b0bbc2f0df827db2e45148f6`, battery `e416de0e074cc0125ac2419a724c420d0d5f9c4dcd141abbd276f477bafbc25b` all reproduced here and equal the R2 pins.

---

## 4. Replication record (commands and counts)

* `python3 cases/d43_k0_field_certificate_r3_20260829/seal_r3.py --root . --verify` → `ok: true`, 28 members, all four `matches_disk` true, archive `403f790a…`, payload `d245952f…`, source-seal file `33718878…`.
* `python3 …/preflight_r3.py --root .` → `preflight_pass: true`, rc 0. P1 18/18; P3 predicted **110 = declared 110**, 99 static sites, 13 loops, 29 predicted observables, hygiene 0 forbidden constructs, 99 labels max width **63 ≤ 80**, ASCII, tab-free; P4 **42/42** gates, both theorem booleans true, `theorem_inputs` pairwise disjoint; P5 **58 MUST_FAIL + 4 MUST_SURVIVE + 19 separation controls + 5 unit tests, 0 failed**, separation `{uncond_true_e_false: 8, both_true: 8, uncond_false: 46}`; P6 all pins true including the **new** GP script hash `5775b63e…`; P7 CLEAN; P8 8/8; P9 33 records + template refusal + artifact/run-dir controls; P10 10/10; P11 baseline ok, **13/13** custody mutations PASS, `failed_mutations: []`.
* `python3 -O …/preflight_r3.py --root .` → `preflight_pass: true`. Grep of the packet's `*.py`: **no `assert ` statements**, so `-O` cannot silence anything.
* `python3 …/custody_selftest_r3.py` → `ok: true` (uid 501). POSIX facts, boundary controls, mint/retire non-root refusals (rc 77 / 64), unit-contract pins, production-policy static census (`CustodyPolicy(` occurs once; `custodian_uid=0` literal).
* Standalone battery (path loader, packet dir on `sys.path` only for this check): `battery_pass: true`, SHA-256 `e416de0e…`. Over all 58 MUST_FAIL entries: **empty "did not fire" list** — every named gate fired. Sampled `gate_errors` carry the intended reasons (`M_SIGMA_NO_SWAP` → relation 2 outside the set; `M_E_EXPONENT` → homogeneity / exponent / literal-pin messages; `M_BASE_SURJ_EXPONENT` → `zeta8^5 * zeta42^15 != zeta_168`). Four MUST_SURVIVE entries all `(True, True)` with `all_pass: true`.
* New surviving mutation, as charged: `zeta8_exponent=189` (= 21+168) passes 42/42. Benign; same element mod 168. The harness does not reject it. Same class as the R2 review's `X_Z8_PLUS168`.

Pinned run values reproduced: census `b828f93d…`, observables `4b1c7ff6…`, GP script `5775b63e…`.

---

## 5. REPAIR-1 (required): the sealed deployment order burns the one-shot mint

R2's blocking finding is repaired **in the supervisor**. The new defect is the coordinator-facing choreography that was added to make that repair operable.

`authorization_template_r3.json` (a sealed packet member, the file a coordinator will actually follow) says, labelled **"DEPLOYMENT ORDER, which is not optional"**:

1. root creates the sealed parent;
2. freeze the authorization and set the live tag;
3. **root runs `mint_claim_r3.sh`** — "normally as the unit's `ExecStartPre=+`, which is the supported path";
4. ops runs `custody_selftest_r3.py --on-host-dry-run` as `jc2k0` against `--run-path` / `--authorization`, claimed to consume nothing;
5. **"only then start the unit."**

Those last three steps are jointly unsatisfiable.

* `--on-host-dry-run` calls `verify_custody_preconditions`, which **requires the run directory and the claim token to already exist**. It cannot run before mint.
* Mint is one-shot: `spent/<digest>.spent` is created with noclobber/`O_EXCL` **before** the run directory exists. A second mint dies `MINT_ALREADY_SPENT` (rc 75) and never reaches the supervisor.
* The unit template's only `ExecStartPre=+` **is** that mint. Starting the unit after a manual mint therefore dies at `ExecStartPre` on the spent marker.
* systemd does not insert an ops dry-run between `ExecStartPre` and `ExecStart`. The shipped unit has no second `ExecStartPre` for the dry-run.

So a coordinator who follows the numbered order mints, dry-runs successfully, starts the unit, and burns the only licensed rehearsal **on a correctly configured host**, before either engine. A coordinator who instead takes the parenthetical "supported path" (just start the unit; mint as `ExecStartPre`; skip the dry-run) can launch — which is why this is a repair rather than a statement that the supervisor is still jointly unsatisfiable in the R2 sense.

The dry-run's advertised purpose is also not met as written. The docstring and preregistration say a refusal "costs nothing" / "the authorization is still unconsumed". That is true of the **lease**. It is false of launch retryability once mint has written `spent/<digest>.spent`. The template's sentence "a failed precondition never consumes this record" is likewise true only of the lease, and is false of the supported `ExecStartPre` path: mint spends first, then the supervisor verifies. A `PATH_OWNER` / `CLAIM_BINDING` refusal after mint cannot be retried under the same digest.

This is the same class as R1 `-I` and R2's lease: new custody path, never executed end-to-end on a Linux host, guaranteed to fail closed before mathematics **if the sealed coordinator instructions are followed**. `preflight_r3.py` P11 does not execute mint-then-dry-run-then-unit-start; it cannot, because this host has no root and no systemd.

**Repair shape (producer's choice, but it must be one path):**

* **A.** Keep mint as `ExecStartPre=+`. Delete steps (d)+(e) as a pre-start pair. Add a second `ExecStartPre=` (no `+`, so it runs as `User=jc2k0`) that is the dry-run, after mint and before `ExecStart`. Update every "consumes nothing" sentence to: mint already spent the digest; the dry-run does not take the lease.
* **B.** Remove mint from the unit. Mint is a manual root step. Dry-run as `jc2k0`. Unit `ExecStart` only runs the supervisor, and must refuse if the spent marker / claim token is absent rather than trying to remint.
* Optional, either way: a **pre-mint** parent-only check (sealed parent, authorization file, service identity — no claim token) if the producer wants a refusal that really costs no coordinator record.

I do **not** want the dry-run duplicated as a precondition inside `run_job`. `verify_custody_preconditions` is already that function, and putting it after mint cannot save the spent marker.

Until this lands, do not authorize. The mathematical layers and the supervisor's lease/claim code do not need to move.

---

## 6. The unconditional mathematics, gate by gate (R2 confirmed; R3 re-checked)

Registry unchanged: 42 gates. Grep of gate bodies: **no L0–L4 gate reads `spec.e_terms`, `spec.q0_terms`, or the pointbanks**. Those names occur in L5 helpers `_E` / `_E_mod` sitting *between* `P2_HENSEL_REPLAY` and `E_LITERAL_PIN`, not in the L4 gate. P4 `theorem_inputs_disjoint: true`.

**A. `RELATION_LEADING_TERMS`.** Confirmed. `grlex_key = (total degree, lex tuple)` is a monomial order. The gate computes leading monomials in the free ring, requires each to be a pure power of its own generator with exponent `basis_shape[k]` (so `deg z^12 = 12` beats a degree-≤11 tail, `deg A1^3 = 3 > deg r = 1`), requires pairwise coprimality, and requires every tail monomial already reduced. Pairwise coprime LMs satisfy Buchberger's first criterion; the standard monomials are the 12·2·3·3·2 box. Deliberate blindness to *which* monic degree-12 `Phi_42` is used is honestly documented. Coverage: `SRC_PHI42_LITERAL` (emitter literal **and** recomputation from `x^42-1`), `PHI42_DISCRIMINANT`, and the independence witness. P10's `x^12+5` probe executed here: leading-term PASS, the other three FAIL.

**B. `RANK432_INDEPENDENCE`.** Completeness is sound. In a field, `r^2=3` has at most 2 roots and each `x^3=c` (c≠0) has 0 or 3; the gate exhibits 18 distinct verified points, hence the complete set. Python builds them as (registered frame)×`μ3` plus the involution `(r,A1,A2)↦(-r,A2,A1)` (because `α1(-r)=α2(r)`). GP builds the same set from `sqrt(Mod(RSQ,p))` and `polrootsmod` of the two cubics. Column index `j-1 = 9b+3c+d` is used identically by Python's triple loop and GP's `matrix` expression. Squared determinants are row-order independent, so the two engines cannot disagree on the three shared observables even if they order rows differently. If a cubic failed to split, GP `error()`s and Python's count check fails; that is fail-closed, not a design fault. I did not re-scan `F_105337` (R2 already did that against this same algebra file); the argument does not need a rescan.

**C–G.** L1–L5 and the Galois/idempotent/E-reduction questions in the charge: I agree with the R2 review, having re-read the R3 gate bodies (byte-identical after the title/import rename). Short answers:

* `GALOIS_STABILITY_FREE`: `fp_substitute` expands by `fp_mul`/`fp_add` only; there is no call to `K0Algebra.norm`. The involution test (`sigma² = id` on generators) is not vacuous (`M_SIGMA_NO_SWAP` fires). Permuting the ideal generators plus involution gives `σ(I)=I`, so `σ` descends to an automorphism of the quotient. Extending that to "`K0/Q` is Galois" remains the charged report's prose. `sigma_relation_permutation` is computed then compared to `Spec`; it is a mutation surface, not circular.
* `L1 CRT` in Python reads mutable `Spec` exponents (`M_BASE_SURJ_EXPONENT` fires it). In GP it now reads `Z8E`, `GENE`, `CONDTOWER[3]`; `(21*5+4*16)%168 = 1`. Falsifiable by drifting those three data variables without editing the `chk` line. Still redundancy beside GENERATION, now honest redundancy.
* `IDEMPOTENTS_ONLY_0_1` is still a Spec-routed emission-policy pin. Routing through `Spec` is enough for that job (`M_COMPONENT_PRODUCT` / `M_IDEMPOTENT_LIST` fire it). Retyping it away from `THEOREM` would move a census hash this packet is required to preserve. Recorded; not a repair.
* GP `x^2-3y^2=-1` mod 3: nine residue pairs, counts how many give residue 2, requires 0. Uses `RSQ`. Real, not padding.
* `E_BASE_REDUCTION`: every coefficient comes from `spec.e_terms` / `alpha_data` / `eps_data`; `CBASE` is computed via an exhibited inverse; `(α2/α1)*s^4 == CBASE`, `u^3 == α2/α1`, and `q0^4 == c` are checked, not read back from themselves. `M_E_EXPONENT` errors include the homogeneity message.

**H. Theorem separation (D1).** Three censuses partition the registry. `unconditional_k0_theorem` is `all(L0–L4 non-corroboration PASS) and CENSUS_UNCONDITIONAL`; `e_conditional_ratio_theorem` is the L5 analogue; `CENSUS_COMPLETE` feeds only `execution_integrity`. A skipped or failed L0–L4 gate cannot leave the unconditional boolean true: the `all(...)` conjunct fails, and the name is missing from `ctx["executed"]` so the layer census fails too. 19 separation controls; battery refuses unless both `(true,false)` and `(true,true)` occur (8 and 8 observed). An L5 or CORROBORATION failure cannot reach `unconditional_k0_theorem`.

**Battery.** 58 MUST_FAIL, each fired its named gate. 4 MUST_SURVIVE survive for the right reasons (non-cube covering set; det-1 basis change; prime-set order; inverse-closed representatives). I found no load-bearing gate-body literal that can produce a wrong PASS and is out of `Spec`'s reach; the R1 pair (`14/154`, pointbank `E` form) stay Spec-routed. Remaining in-body literals are verification targets, structural constants, or the cosmetic `12` in `SPLIT_COUNT_432` already noted by R2.

The compound coordinated-scope-shrink fixture the R2 review constructed is still a checker-level hole and is still refused at run level by the observable pin and cross-engine agreement. Unchanged; still not a live hole.

---

## 7. The GP file (source review only — never parsed by any GP)

Hand-plus-static census: P3 predicts **110 = `nexpect` 110**, 29 observables, 99 labels, max width 63, ASCII, tab-free, 0/13 forbidden constructs. The runner will not trust a GP banner: it requires 110 parsed gate lines all printing 1, the `CENSUS 110/110` line, 29 observables, and the terminal line. A syntax error or `error()` mid-script is a **repair**, not a FAIL of the Python unconditional layer, but it would make the terminal's two-engine claim for that run false — and this source review must not say the two-engine claim has been executed.

R3-only surface:

* `Z42E`, `Z8E`, `GENE` and their three use sites are the only load-bearing GP edit. PARI vectors are 1-indexed: `GENE[1]=5`, `GENE[2]=16`. `CONDTOWER=[21,84,168]`, so `[3]=168`. The CRT line is now data-driven. If this does not parse, that is a repair.
* `[R3-B]` is a comment on an uncounted defensive branch. It is not a gate.
* `chk`/`chkE` both increment the one `ncheck`; `ok` and `okE` never mix. `printf("%-58s %d\n", lab, b)` with max label 63 still fits the runner's 80-character `GATE_LINE` window.
* `matrix`/`matdet` over `t_INTMOD`, `polrootsmod` on `2t^2-3` and the cubics, and the `sg(f)` `'tw` subst chain are unchanged from the R2 source audit. I re-read them; I did not execute them.
* GP leading-term block still validates declared `LEAD` data, not recomputed LMs of the relations. The README now says so. Asymmetry stands; two-engine rank content is the independence witness and the 25 unconditional shared observables.

---

## 8. Custody attack table (charge G)

Walk of `run_job`: `production_policy` → `live_identity` → `load_authorization` → host binding → `require_service_identity` → environment → cgroup → `establish_custody` (verify then burn) → try (`stage_packet`, marker, pins, runner, `publish_terminal`). Every step before the try writes no terminal. `main` converts any leftover exception to `CUSTODY_FAULT UNCLASSIFIED`, rc 70.

Can a `jc2k0` process with an empty capability set actually do this on a Linux host where the sealed parent is root-owned 0755? **Yes, once the run directory already exists and holds the root-minted claim**, which is the R2 repair. The parent gate is unchanged (uid 0, no group/world write, ancestors `{0}` in production because `custodian_uid` is 0). The service creates nothing in the parent. The lease is `O_CREAT|O_EXCL` inside the service-owned 0700 directory, which is the only `ReadWritePaths` entry.

| attack | result |
|---|---|
| `chown` claim token to self / to root | unprivileged `chown` to root is `EPERM` (executed here). Empty `CapabilityBoundingSet` excludes `CAP_CHOWN`. `CLAIM_OWNER` if the token is not custodian-owned. |
| `chmod` claim token | 0444 root-owned; no write bit for the service; `CAP_FOWNER` unavailable. Mode mismatch is `CLAIM_MODE`. |
| `chmod` run directory to 0777 / 0750 | service owns it, so this works — and then `RUN_DIR_MODE` refuses (exact 0700). Fail-closed. |
| rename / unlink the token | service owns the directory, no sticky bit, so unlink works. Next launch: `CLAIM_ABSENT`, **no lease**. Self-denial. Mint already spent, so this also costs the coordinator record. |
| replace the run directory | parent is root-owned 0755; service cannot `rename` or `rmdir` it. |
| symlink at the token path | `is_symlink` checked before `exists`; `CLAIM_SHAPE`. |
| symlink at the run path | `RUN_DIR_SHAPE`. |
| hard link the token (`nlink≠1`) | refused `CLAIM_SHAPE`. `fs.protected_hardlinks=1` (typical Linux) additionally blocks linking a file you do not own. |
| forge a new token as `jc2k0` | new file is service-owned → `CLAIM_OWNER`. Cannot `chown` to 0. |
| POSIX ACL on the token | service does not own the file; `setfacl` fails. |
| POSIX ACL on the run directory | service owns it; adding an ACL typically raises the group-class / mask bits, so mode is no longer 0700 → `RUN_DIR_MODE`. ACL mask on the **parent** would surface in group-class bits the parent gate rejects. |
| `CAP_DAC_OVERRIDE` / `CAP_CHOWN` / `CAP_FOWNER` | unit: `CapabilityBoundingSet=` empty, `AmbientCapabilities=` empty, `NoNewPrivileges=yes`. |
| second presentation, same `run_path` | same directory (path is inside the hashed record, hence inside the live tag) → lease `O_EXCL` → `AUTHORIZATION_REUSE`. No terminal (outside the try). |
| second presentation, different `run_path` | claim token name/digest/run_path binding fails, or mint already spent. |
| burn before verification | `establish_custody` verifies first. P11 `no_burn_before_verification` (6 refusal cases, 0 leases after). CM5 swaps the order and the control fails. |
| `PermissionError` traceback (R2) | every custody `OSError` → `CustodyFault`; lease create catch includes `OSError` → `LEASE_UNWRITABLE`; `main` catch-all. CM6 restores the traceback path and the control fails. Executed against a real mode-0500 directory. |
| crash mid-`emit_immutable` | `O_CREAT\|O_EXCL` on the final name; short write is caught by manifest/archive replay before any terminal. Unchanged from R2. |
| `retire_claim_r3.sh` pointed at the wrong tree | requires absolute path, not a symlink, `realpath` identity, basename `run-YYYYMMDDTHHMMSSZ`. Does not delete, does not touch `spent/`. `chown -R 0:0` + `chmod -R a-w` + dirs 0555 seals evidence; running twice is idempotent-enough. Unit binds the argument. A coordinator who puts a matching basename that is not the run dir is a root error, not a `jc2k0` attack. |
| mint argument injection | `RUN_NAME` and `SERVICE_USER` regex-constrained; `PARENT`/`AUTH_JSON` must be absolute; all expansions quoted; no `eval`; authorization JSON is **not** parsed (binding is in `verify_claim_token`). `set -C` before the spent redirect; token write still under noclobber; `chown` of the directory happens **after** the token is 0444 root-owned. |
| partial mint / unit restart | spent marker first: restart is `MINT_ALREADY_SPENT`. Fail-closed; costs a coordinator record, as the script comments say. |
| `CustodyPolicy` seam reached in production | `CustodyPolicy(` occurs **once**, in `production_policy`, literal `custodian_uid=0`, service identity from `pwd`/`grp`, no env/argv. `run_job` calls `production_policy()`. CM1 replaces `0` with `os.geteuid()` and the pin fails. Fixtures use a different constructor with the running uid; that is not a production path. In production `allowed_owners = {0, policy.custodian_uid} = {0}`. |
| fixture policy "proves" the deployed host | it does not, and is not claimed to. It proves the mode/`O_EXCL`/`EACCES`/`EPERM` laws and the Python control flow. The deployed custodian-uid-0 claim is the static pin + CM1 + launch-time `production_policy()`. |
| P11 mutation whose effect is wrong / control with no mutation | all 13 anchors unique (`hits==1`); all 13 declared controls go false. Mint/retire are shell, tested by `bash -n`, non-root rc, and source-order assertions, not by the 13 Python patches. That split is honest. |
| `0pus 5` through `normalize_model` | maps to `0pus5`, which does not contain `opus`. I agree with R2: a note, not a repair. The guard is against accidental same-model review. Frozen in R3, correctly. |
| instance type `r6i.large` only | right call. Pins the type, not the terminated instance id. Will not block a legitimate rehearsal of the same type. |
| `_forbidden_language_scan` `\bK_?[1-9]\d*\b` | CLEAN on the new artifacts (`mint`/`retire`/`custody_selftest`/unit/supervisor/runner/README/preregistration/GP/checker/mutations). `K0` / `KUMMER_*` are safe. |

**Runner law (REPAIR-2), both directions.** Pre-run listing must be exactly `{source, job_marker.json, execution_pins_live.json}` plus the claim token and lease **named from the marker's `authorization_sha256`**. Extra names → `RUN_DIR_REUSE`. Missing names → `RUN_DIR_INCOMPLETE`. `source` must be a directory (second check, so CM12 still catches an unstaged tree). Non-SHA marker digest → `MARKER_AUTHORIZATION`. CM11 restores the R2 two-name set and `clean_launch_accepted` fails. Supervisor stages `source` *before* spawning the runner, after the lease; the five-entry listing is what a real launch has. This would have refused every R2 launch. Repaired.

**Mint/Python split** (mint does not parse the authorization; `verify_claim_token` binds schema/route/digest/run_path/service_user, and additionally requires `record["run_path"]` to be that directory) is sound. A mint against the wrong run name produces `CLAIM_BINDING` / `CLAIM_ABSENT` and, because spent-first, cannot be retried.

---

## 9. Charge G2 — substitutes vs a rehearsal license

Executed POSIX facts (this host, uid 501): a directory without a write bit refuses create even to its owner; a 0444 file refuses a write even to its owner; unprivileged `chown` to root is refused; `O_EXCL` refuses a second create.

Systemd identity is a **contract** (`User=`/`Group=` vs `DEDICATED_SERVICE_USER`/`DEDICATED_SERVICE_GROUP`; empty capabilities; `NoNewPrivileges=yes`; `ReadWritePaths` is the run directory, not the parent). Not a systemd execution.

The root-owned half is supposed to be `custody_selftest_r3.py --on-host-dry-run` as `jc2k0` on the deployed host. That function is the right function. The **placement** is the REPAIR-1 defect: it cannot sit where the template puts it.

That is **not** enough to license a rehearsal until the choreography is one path. The supervisor's own `verify_custody_preconditions` will still fail-closed on a bad parent at launch time; the cost of a misconfigured parent is then a spent mint, which is the wrong cost model for a preflight but is not a wrong theorem. The blocking issue is the correctly configured host that follows the sealed order and never starts.

I do not want the dry-run moved *into* the supervisor. I want the unit and the template to describe the same sequence.

---

## 10. Claim discipline

Checked.

* No unconditional gate reads `spec.e_terms`, `spec.q0_terms`, or the pointbanks.
* `unconditional_k0_theorem` is L0–L4 non-corroboration plus `CENSUS_UNCONDITIONAL` only. `e_conditional_ratio_theorem` is L5 non-corroboration plus `CENSUS_CONDITIONAL` only. Corroboration is a separate boolean and is never credited.
* E theorem is typed **single-engine** in the runner terminal (`single_engine: true`, named reason, GP listed under `corroborated_by` as `E_BASE_IDENTITIES`), in the preregistration, and in the README. GP terminal regex is `K0_UNCONDITIONAL … E_BASE_IDENTITIES`, not `E_CONDITIONAL`.
* `not_claimed` carries the firewall (D43 row/point, template/D25, raw-J, Keller, JC2). Unconditional statement does not derive fieldness from the 432-frame count (`SPLIT_COUNT_432` remains `CONSISTENCY`, caveat verbatim). Nothing claims the GP engine has run. Crediting is joint with `EXECUTION_INTEGRITY`.
* Promotion-safe maximum of this packet, after a future literal-`PASS` review of the repaired choreography and a coordinator GO: an executable certificate of the coefficient-field theorem (two engines, once GP actually runs and agrees) plus one E-ratio theorem **conditional** on the hashed displayed `E` (one engine). Not a row, not a point, not a template, not D25, not raw-J, not Keller, not JC2.

The runner's unconditional block lists both engines as the intended successful-run typing. That typing becomes true only when GP runs. This review does not say it has.

---

## 11. Residual risk (execution debt, not blocking source defects)

1. **GP has never been parsed by any GP**, and R3 edited its data-driven CRT line. Containment: runner refusal, not a wrong Python PASS. Two-engine claim is execution debt.
2. **Root-owned objects and systemd are unexecuted here.** The Python boundary is executable as `jc2k0` once mint has happened. Linux behaviour of `ExecStartPre=+` (root, sandbox dropped, completes before the ExecStart namespace so `ReadWritePaths=<run dir>` resolves) is taken from documented systemd semantics, not from a run.
3. Ancestor paths are `lstat`-ed, not resolved, on the unprivileged side. A root-owned symlink ancestor with write bits on the target would be a residual. Mint checks `realpath "$PARENT" == "$PARENT"` as root on the parent itself, not on every ancestor. Recorded by the producer; I agree it is not a repair on this packet (macOS `/tmp`/`/var` are symlinks, which is why the unprivileged gate cannot demand it). Production `/var/lib/jc2-k0` is a real directory on typical Ubuntu.
4. Mint spends before supervisor verification. That is fail-closed and must be *said* (REPAIR-1 wording), not weakened.
5. Mathematics residuals of the R2 review (§10.3–7 there: prose base, E conditionality, frames as witnesses, single-field battery, compound-shrink at checker level) stand, because the mathematics stands.
6. `0pus 5` / `IDEMPOTENTS_ONLY_0_1` typing / GP declared-LEAD asymmetry: recorded, deliberately unchanged, not repairs.

---

## 12. Answers to the charge's direct questions

| question | answer |
|---|---|
| Unconditional layer prove what the terminal says, using only what it executes? | **Yes**, for the Python engine, with the charged report's named prose base (cyclotomic irreducibility, Kummer correspondence, etc.). GP is source-only. |
| Conditional layer quarantined now that censuses are layer-restricted? | **Yes.** |
| Path to a wrong PASS (gate that cannot fail, mutation that should fail and does not, asserted conclusion)? | **Not in the mathematics or Python harness.** The live wrong-*launch* path is REPAIR-1 (burned rehearsal, no theorem). |
| `RELATION_LEADING_TERMS` blind to which `Phi_42`, README honest, other pins cover it? | **Yes.** |
| `RANK432` completeness, Kronecker indexing, squared dets, two construction routes? | Completeness and Kronecker indexing **yes**. Different *sets* would be a disagreement the runner refuses, not a silent wrong PASS; both routes aim at the complete split set. |
| Declared mutation pair wrong / class the controls miss? | **None found** in the 19 pins. Coordinated multi-field shrink is refused at run level. |
| `fp_substitute` expands? Involution vacuous? Descent? Permutation pin circular? | Expands; involution real; descent as a ring automorphism of the quotient is the right executable shadow; pin is not circular. |
| Dry-run as supervisor precondition? | **No.** Fix the unit/template order (REPAIR-1). |

README disposition table: treated as allegation; REPAIR-1/1b/2, GP CRT, `[R3-B]`, recorded-not-changed items, and the GP-never-parsed restatement all match the files.

---

## 13. Reproduction

```
cd /Users/dc/code/math/jc2
python3 cases/d43_k0_field_certificate_r3_20260829/seal_r3.py --root . --verify
python3 cases/d43_k0_field_certificate_r3_20260829/preflight_r3.py --root .
python3 -O cases/d43_k0_field_certificate_r3_20260829/preflight_r3.py --root .
python3 cases/d43_k0_field_certificate_r3_20260829/custody_selftest_r3.py
```

plus the standalone battery and `zeta8_exponent=189` probe of §4. No AWS, no PARI, no CAS.

Body hash below: verify with
`sed -n '1,/^<!-- BODY-END -->$/p' <this file> | shasum -a 256`.
Full-file hash is of this file through the body-hash line inclusive (the
`full:` line is excluded). Verify by hashing the body plus the following
`body:` line.

<!-- BODY-END -->
4071ad8ee28a8b8d10147567f9c6521fc4f4be83a04fb3edab24662843325421  body: everything from the first byte of this file through the BODY-END line inclusive
ce023897d8e2dd53c03efdd82f3a028122476447267324aa48f0796eb49fc090  full: this file through the body-hash line inclusive (this full-hash line excluded)
