# D43 `K0` field certificate R3 — privilege-boundary repair packet and producer report

**Verdict: `SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`**

**UTC:** 2026-08-29 (host clock 2026-08-28 local)
**Producer:** Opus 5 (`claude-opus-5`), the R2 producer
**Object:** `cases/d43_k0_field_certificate_r3_20260829/`, status
`R3_SOURCE_READY_AWS_NOT_AUTHORIZED`
**Charged by:** `xmodel/d43-k0-field-certificate-r2-hostile-review-fable5-20260829.md`
(SHA-256 `824e24d794e8828de6a3f5b9c9b0b40bf93305f72a06fd91275a6e89933f3602`,
verdict `PASS WITH REPAIR`)

## What this verdict does and does not license

* **R3 authorizes nothing on AWS.** This report is written by the producer, and
  `aws_supervisor_r3.validate_authorization_record` refuses any
  `reviewer_pass.model` that normalises to contain `opus`, and requires the
  verdict field to read exactly `PASS`. Neither condition is met by this file.
  A launch needs a fresh different-model source PASS of *this* packet plus a
  coordinator GO.
* It records that R2's **one blocking finding is repaired and the repair is
  executed**, that a **second defect of the same class** found while repairing
  it is also fixed, and that the mathematics is unchanged and provably so.
* **The GP file has still never been parsed by any GP.** Nothing here changes
  that. R3 edits two lines of it; those edits are static-audited only.
* R2 and R1 are untouched. Both remain on disk exactly as reviewed.

---

## 1. Execution gaps, stated first

* **No PARI/GP.** There is no `gp` on this host (`command -v gp` is a shell
  alias for `git push`). `k0_field_cert_r3.gp` was edited and re-audited
  statically; it has never been parsed by any GP, and no claim below says
  otherwise.
* **No AWS, no root, no systemd.** No AWS API was touched. The custody
  fixtures run as an ordinary user (uid 501): **no fixture in this packet
  creates a root-owned object, and none runs under systemd.** §5.3 states
  exactly what that costs and what stands in its place.
* No commit, no push, no canonical edit, no CAS, no long or high-memory
  process. Everything below ran in seconds.

---

## 2. Byte hashes of everything shipped

### 2.1 The R3 packet, 18 sealed members plus 4 generated files

| file | SHA-256 |
|---|---|
| `README.md` | `56f1fb1bd8a22a65967e8c78945c2940ee87e554564f3792ee05b0cea0df979a` |
| `REVIEW_REQUEST.md` | `ff3a8e73cb4bd31607832c9eaf7f10e662884bb397ad302e171ba05bafc289ca` |
| `authorization_template_r3.json` | `84727c5af08ba29169d1f73abc399a803edbf72325cb7f5ac178bf0795d29a5b` |
| `aws_supervisor_r3.py` | `83c80c65a108339af68e75fe5ab52d2ed2b797130456ff02685e8179f2f71b0b` |
| `aws_worker_r3.sh` | `aab607c8debc13fabe5ea4c35d13ae5d10309ee34db890f5a60c2b93ba122df8` |
| `custody_selftest_r3.py` | `28feaf3bbfb5fbd356fc87cfe0bdc33afb6c971d23a25888624718e933c02de8` |
| `execution_pins_r3.json` | `4a1e38f2f89b8f8d5137f8cce72539e541591d1621ce34ac8533d6f33647d5c4` |
| `k0_algebra_r3.py` | `a7de3c3fcefc42302e402b8dfcaeefbba6d5a582ae694447e8f95f6a8e8dd4a6` |
| `k0_field_cert_r3.gp` | `5775b63e304378f5092355f02f129f0654e1ff9c6c883dfcd866f4ebdd17c5eb` |
| `k0_field_checker_r3.py` | `9f82ae1f36a88d55b021cc1e73482a5ccb11d4c6b61d6b10bdc3c4a4020afb18` |
| `k0_mutations_r3.py` | `99671b83e2fc2d2cd179fe46acde509cf1846f95407b5b6ec1e1343166465726` |
| `mint_claim_r3.sh` | `fd709ee6bba1d2388140dd02c6f0558f448503c40ab3b6e0e1c648c43f533983` |
| `preflight_r3.py` | `d58fa4674c50c282b38d62a00fbd59bf051025da8357d2722f77666d2103e9c6` |
| `preregistration_r3.json` | `e273546a4d8ac696a1b20f14b7852f179b6ba093ccaf807f021c1713a4769896` |
| `retire_claim_r3.sh` | `832ee9d2384f37f3f00453acaeb4e8dc30f522dd6775f7d698d8da3a6173564f` |
| `runner_r3.py` | `8d21fb9394b6b24cc66fbf8f962062b807af6dd0fdc639b6fb9327df18ff4fd3` |
| `seal_r3.py` | `dfbf046fb4b980dbdda8977eb0f4f02f4e8a9190d88f63a2f50a8644292f4d6b` |
| `systemd_unit_template_r3.service` | `b9de00ee60294654d962a1512641f94169c47197b5846c2612c643e7ea23ca81` |

| generated | SHA-256 |
|---|---|
| `PAYLOAD.sha256` | `d245952f26e2252a9eae46fea927a33806c93989b717b4528c5c5a4d253e9d02` |
| `SOURCE_ARCHIVE.tar` (28 members) | `403f790afa9904962b4ad79ebb29cf50ef21c399bbf598f5007c771ee1002a37` |
| `SOURCE_ARCHIVE.sha256` | `d86de271f3998c265f906bdf95ca575f4ba56e3f5914d1434f3394469f52f7ef` |
| `SOURCE_SEAL.sha256` | `3371887839cb98b6afeb99c78c186f12adb046a9ddebc68e3c93218f8bceeb8d` |

### 2.2 The nine sealed external members

The eight R2 externals are carried at their reviewed hashes (emitter
`5420b5c0…`, rows `9fc9bd7a…`, pointbanks `bb0f13b6…` / `b933cdb5…`, bridge
`e1b99600…`, theorem report `6d3d53c2…`, Grok 4.6 theorem review `07f20be5…`,
Fable 5 R1 source review `29e9496e…`). **New in R3**, sealed and pinned in
`execution_pins_r3.json`, hashed by `SRC_FILE_HASHES`:

| file | SHA-256 | role |
|---|---|---|
| `xmodel/d43-k0-field-certificate-r2-hostile-review-fable5-20260829.md` | `824e24d794e8828de6a3f5b9c9b0b40bf93305f72a06fd91275a6e89933f3602` | the review whose REPAIR-1 this packet answers |

### 2.3 Pinned run values — every mathematics hash identical to R2

```
route                       D43-K0-FIELD-CERT-R3     (changed)
python gates                42                       (unchanged)
gp gates (nexpect)          110                      (unchanged)
shared observables          29  (25 unconditional, 4 E)   (unchanged)
census   SHA-256   b828f93d6a29c15371e4d277473e63c0a25ba0280fa5ab44706d10c786f9aeb0   IDENTICAL to R2
observable SHA-256 4b1c7ff63935adb27148a2967037b7a357354848b0bbc2f0df827db2e45148f6   IDENTICAL to R2
battery  SHA-256   e416de0e074cc0125ac2419a724c420d0d5f9c4dcd141abbd276f477bafbc25b   IDENTICAL to R2
gp script SHA-256  5775b63e304378f5092355f02f129f0654e1ff9c6c883dfcd866f4ebdd17c5eb   REGENERATED (§4.3)
```

The three run hashes are the mechanical proof that the mathematics did not
move: the census hash is over the sorted names of the passing gates, the
observable hash is over the 29 cross-engine integers, and the battery hash is
over the `[mutation, verdict]` list. All three reproduce R2's pins exactly, in
the packet and in a standalone out-of-tree replay (§6).

---

## 3. R2 → R3 diff inventory

### 3.1 File level

Comparison is against R2 after applying the R-number token rename
(`_r2`→`_r3`, `-r2`→`-r3`, packet dirname, `CERT-R2`→`CERT-R3`); the rename is
length-preserving, so no hash below moved for formatting reasons.

| file | R2 → R3 lines | +/− after rename | what changed |
|---|---|---|---|
| `k0_algebra_r3.py` | 669 → 669 | +0 −0 | **byte-identical to `k0_algebra_r2.py`**, same SHA-256 `a7de3c3f…` |
| `k0_field_checker_r3.py` | 1675 → 1675 | +1 −1 | one docstring title line. Raw diff vs R2: the title, `import k0_algebra_r3 as KA`, `SCHEMA = "…-checker-r3"`. Nothing else. |
| `k0_mutations_r3.py` | 541 → 541 | +1 −1 | one docstring title line. Raw diff vs R2: the title, one docstring cross-reference, two imports, `SCHEMA = "…-mutations-r3"`. Nothing else. |
| `aws_worker_r3.sh` | 31 → 31 | +0 −0 | identical after rename |
| `k0_field_cert_r3.gp` | 499 → 526 | +33 −6 | §4.3: three data variables, three use sites, one defensive-branch comment, header block |
| `aws_supervisor_r3.py` | 637 → 979 | +416 −74 | §4.1, the boundary |
| `runner_r3.py` | 776 → 810 | +43 −9 | §4.2, the run-directory law |
| `preflight_r3.py` | 926 → 1098 | +180 −8 | P11 + P9 signature update |
| `systemd_unit_template_r3.service` | 86 → 140 | +59 −5 | mint/retire/`ReadWritePaths` + the boundary comment |
| `seal_r3.py` | 149 → 151 | +7 −5 | ninth external member |
| `execution_pins_r3.json` | 48 → 51 | +4 −1 | GP hash, R2-review pin |
| `authorization_template_r3.json` | 65 → 88 | +29 −6 | deployment order, `run_path` semantics |
| `preregistration_r3.json` | 167 → 239 | +87 −15 | R3 scope, supersession, boundary |
| `README.md` | 245 → 372 | +161 −34 | boundary, disposition table, replay |
| `REVIEW_REQUEST.md` | 214 → 310 | +126 −30 | new charge (§G, §G2) |

New files: `custody_selftest_r3.py` (696 lines), `mint_claim_r3.sh` (137),
`retire_claim_r3.sh` (45). Removed: none.

### 3.2 Function level

`aws_supervisor_r3.py`

| function | change |
|---|---|
| `CustodyPolicy` (class) | **new**; the single production/fixture seam |
| `production_policy` | **new**; the only `CustodyPolicy(` construction, literal `custodian_uid=0`, service identity from `pwd`/`grp` |
| `require_service_identity` | **new**; real *and* effective uid/gid must be the service identity, and must not be 0 (R2 compared `os.getuid()` only) |
| `_lstat` | **new**; `OSError` → `CustodyFault("PATH_STAT")` |
| `require_root_owned_immutable` | signature `(policy, path, label)`; owner read from the policy; ancestors may be custodian- **or** root-owned (identical sets in production, where the custodian *is* root); all stats through `_lstat` |
| `require_service_owned_run_dir` | **new**; the run directory must already exist, service-owned, mode exactly 0700, not a symlink. Creates nothing. |
| `verify_claim_token` | **new**; root-owned 0444 regular file, single link, canonical binding of schema/route/digest/run path/service user, plus record↔directory agreement |
| `require_run_dir_pristine` | **new**; only the claim token and this authorization's lease may be present before launch |
| `claim_authorization_lease` | rewritten: lease lives **inside the run directory**; `FileExistsError` → `AUTHORIZATION_REUSE`; every other `OSError` → `LEASE_UNWRITABLE` (R2's uncaught `PermissionError`) |
| `claim_run_path` | **deleted**; the service no longer creates any directory |
| `verify_custody_preconditions` | **new**; filesystem-pure, the on-host dry run's entry point |
| `establish_custody` | **new**; verify, then burn, in that order |
| `stage_packet` | **new**; extracted from `run_job` so P11 can execute the real staging |
| `materialize_source`, `load_authorization` | take the policy |
| `run_job` | uses the above; the custody sequence is outside the try block; terminal `core` records the custody block and the service identity |
| `main` | catch-all `except Exception` → `CUSTODY_FAULT UNCLASSIFIED`, rc 70 |
| `validate_authorization_record`, `normalize_model`, `live_identity`, `verify_cgroup_contract`, `reject_inherited_environment`, `atomic_bytes`, `publish_terminal` | **unchanged** |

`runner_r3.py`: `PRE_RUN_FILES` (+`source`), new `REQUIRED_PRE_RUN_FILES`,
custody name constants and `SHA_RE`; `check_run_dir_clean(run_dir, auth_sha)`
rewritten in both directions; its call site passes the marker's
`authorization_sha256`. Everything else, including both engines' invocation,
the observable agreement, the artifact caps and the terminal, is unchanged.

`preflight_r3.py`: `custody_controls` (P11), `CUSTODY_MUTATIONS` (13 entries),
`_load_mutated`; `authority_controls`' run-directory case updated to the new
signature; `custody_selftest_r3` added to `SEALED_MODULES`.

---

## 4. The repairs

### 4.1 REPAIR-1 — the privilege boundary (the R2 review's blocking finding)

The defect, exactly as charged: `claim_authorization_lease` called
`require_root_owned_immutable(run_path.parent)` — uid 0, no group or world
write bit, no writable ancestor — and then `os.open(parent/…lease,
O_CREAT|O_EXCL)`. Creating a directory entry needs write permission on the
directory; for a root-owned directory with no group/world write bit only root
has it; the unit runs `User=jc2k0` with `CapabilityBoundingSet=` empty, so
`CAP_DAC_OVERRIDE` is unavailable; and a POSIX ACL cannot help because the ACL
mask surfaces in the group-class bits the same check rejects. Jointly
unsatisfiable. `ReadWritePaths=` lifts only the `ProtectSystem=strict`
read-only remount and grants no DAC permission.

**The R3 design.** One boundary, drawn so that each side does only what its
privilege allows:

```
<sealed parent>                             root:root   0755   never service-writable
  ├── spent/                                root:root   0700   root-only mint ledger
  │     └── <auth-sha>.spent                root:root   0444   the one-shot gate
  └── run-<UTC>/                            jc2k0:jc2k0 0700   the only writable path
        ├── .jc2-k0-r3-claim-<auth-sha>.json          root:root 0444
        └── .jc2-k0-r3-authorization-<auth-sha>.lease jc2k0     0444
```

1. **The parent-owner gate is not weakened.** `require_root_owned_immutable`
   still demands uid 0 and no group/world write bit on the sealed parent and
   its ancestors. It became satisfiable because the service stopped writing
   there, not because the rule changed. (The reviewer's option (a) — allow a
   service-owned parent — was available and is *not* taken.)
2. **The run directory is pre-created by root** (`ExecStartPre=+
   mint_claim_r3.sh`) and chowned to `jc2k0` at mode 0700. The supervisor
   verifies it and creates no directory anywhere; `claim_run_path` is gone.
3. **The claim token is the root-owned, no-replace primitive.** Root writes it
   *inside* the service-owned directory as a 0444 root-owned file. An
   unprivileged process cannot create it (it cannot `chown` to root) and
   cannot modify it (no write bit for any class but root's own, and the empty
   capability set excludes `CAP_DAC_OVERRIDE`/`CAP_CHOWN`/`CAP_FOWNER`). It
   can unlink it, which denies only itself: the launch refuses `CLAIM_ABSENT`
   and consumes nothing. The token binds schema, route, authorization digest,
   run path and service user, and the supervisor additionally requires the
   authorization record's own `run_path` to be that directory.
4. **The creation/consumption protocol is enforced outside the unprivileged
   process.** `mint_claim_r3.sh` runs as root and is one-shot by construction:
   it creates `spent/<digest>.spent` with `O_EXCL` (bash `set -C`) **before**
   the run directory exists, so a unit restart dies at `MINT_ALREADY_SPENT`
   and never reaches the supervisor, even if the first mint crashed halfway.
   It deliberately does not parse the authorization record; the
   record↔claim binding lives in `verify_claim_token`, which is reviewed
   Python. `ExecStopPost=+ retire_claim_r3.sh` seals the finished run
   directory back to root-owned and read-only.
5. **Verify, then burn.** `establish_custody` runs
   `verify_custody_preconditions` — parent gate, run-directory gate, claim
   token, pristine listing — and only then takes the lease. A failed
   precondition therefore leaves the authorization unconsumed, which P11
   proves by walking the whole fixture tree for lease files after each
   refusal. Both halves sit outside the try block, so a refused launch writes
   no terminal at all.
6. **No traceback path remains.** Every custody filesystem call converts
   `OSError` to a `CustodyFault` (`PATH_STAT`, `LEASE_UNWRITABLE`,
   `RUN_DIR_SHAPE`), and `main` converts anything else to `CUSTODY_FAULT
   UNCLASSIFIED` with rc 70. R2's second failure branch — a raw
   `PermissionError` traceback and exit 1 — is closed and is exercised
   against a real mode-0500 directory.

Why not the simpler option (a)? Allowing a service-owned lease parent would
have made the lease *removable by its own creator*: the service owns the
directory, so it could unlink its own lease and re-present the authorization.
The R3 shape keeps the grant direction in an object the service provably
cannot forge, and puts the one-shot ledger where the service cannot reach it
at all. The cost is one root-side script and a stricter deployment order, both
documented in the authorization template.

New fault codes: `PATH_STAT`, `RUN_DIR_ABSENT`, `RUN_DIR_SHAPE`,
`RUN_DIR_OWNER`, `RUN_DIR_MODE`, `RUN_DIR_DIRTY`, `CLAIM_ABSENT`,
`CLAIM_SHAPE`, `CLAIM_OWNER`, `CLAIM_MODE`, `CLAIM_BINDING`,
`LEASE_UNWRITABLE`. Retired: `DUPLICATE_LAUNCH`, `RUN_PATH`.

### 4.2 REPAIR-2 — producer-found, same class, not in the R2 review

While rebuilding the run-directory law I found a second guaranteed-failure
integration defect in R2, downstream of REPAIR-1 and of exactly the same kind:

`runner_r2.check_run_dir_clean` required `set(os.listdir(run_dir)) <=
{"job_marker.json", "execution_pins_live.json"}`. But `run_job` extracts the
reviewed archive to `<run dir>/source` **before** it writes either JSON file
and spawns the runner. So on every real launch the listing would have been
`{source, job_marker.json, execution_pins_live.json}` and the runner would
have died on `RUN_DIR_REUSE` — after the mathematics-free custody steps, still
before either engine. R1 never reached this line (it died in the import), P9
exercised the function only on a hand-built directory that omitted `source`,
and the R2 review could not execute the AWS path.

R3's law is exact in both directions: the listing must be exactly
`{source, job_marker.json, execution_pins_live.json}` plus the claim token and
lease **named from the marker's `authorization_sha256`**, `source` must be a
directory, and a non-SHA marker digest is `MARKER_AUTHORIZATION`. Mutation
`CM11` restores the R2 set and the "correctly staged launch is accepted"
control fails, reproducing the defect on demand.

Note for the reviewer: the source-tree presence is checked twice on purpose
(set membership and `is_dir`), so no single-line mutation can hide an unstaged
source; `CM13` removes both and the control fails.

### 4.3 The GP constant-true line (R2 review §7.i) — the one mechanical GP fix

R2's `L1 CRT 21*5 + 4*16 == 1 mod 168` could not print 0 without editing the
file. R3 adds three data variables next to the existing presentation data —
`Z42E = 4`, `Z8E = 21`, `GENE = [5,16]` — and routes the ζ₈ line, the
`GENERATION` line and the `CRT` line through them, with the modulus read from
`CONDTOWER[3]`. A drifted exponent now moves all three. Unchanged: the gate
count (110 declared = 110 predicted), the 99 static sites, the 13 loops, the
29 observables, `crt_residue = 1`, the label census (99 labels, max width 63 ≤
80), ASCII-only, tab-free, and the hygiene scan (0/13 forbidden constructs).
The GP file's own hash necessarily moved and is re-pinned in
`execution_pins_r3.json`; that is the only regenerated mathematics-layer hash,
and P6 checks the pin against the file.

The R2 review's §7.ii item is handled as documentation: the unreachable
within-fibre branch in `charframes` now carries an `[R3-B]` comment saying it
is defensive, not a gate, and is not counted in the census.

**This edit has never been parsed by any GP.** If it does not parse, that is a
repair, not a finding — but it would burn a rehearsal, which is precisely why
the static census, the hygiene scan and the label audit all re-ran.

### 4.4 Recorded and deliberately not changed

| item | why not |
|---|---|
| §7.iii, the GP leading-term block validates declared `LEAD` data rather than recomputing the relations' leading monomials | the reviewer asked for "one honest line in a future README"; that line is now in the README. Changing the GP block would change the GP engine, which this charge excludes. |
| §5E, retype `IDEMPOTENTS_ONLY_0_1` away from `THEOREM` (explicitly cosmetic) | retyping moves a gate between the `theorem_inputs` censuses — the D1 separation surface the review confirmed — and would change the census composition this packet is required to preserve. Live item for a mathematics revision. |
| §8, `normalize_model` maps `0pus 5` to `0pus5` (the reviewer typed it a note, not a repair) | `validate_authorization_record` is frozen in R3: the charge forbids changing authorization semantics. The guard targets accidental same-model review, not a coordinator who could write anything. |
| §6, the coordinated multi-field scope shrink passes the checker | already documented in R2 and refused at run level by the observable pin and cross-engine agreement. Unchanged. |
| model-name and other cosmetic items | recorded here; not overfitted. |

---

## 5. Tests executed, with exact commands and counts

### 5.1 Commands

```
cd /Users/dc/code/math/jc2
python3 cases/d43_k0_field_certificate_r3_20260829/seal_r3.py --root . --verify
python3 cases/d43_k0_field_certificate_r3_20260829/preflight_r3.py --root .
python3 -O cases/d43_k0_field_certificate_r3_20260829/preflight_r3.py --root .
python3 cases/d43_k0_field_certificate_r3_20260829/custody_selftest_r3.py
python3 cases/d43_k0_field_certificate_r3_20260829/k0_mutations_r3.py --root . \
  --pins cases/d43_k0_field_certificate_r3_20260829/execution_pins_r3.json \
  --pointbank "105337:cases/d43_full_pointbank_p105337.pkl:bb0f13b6…" \
  --pointbank "105673:cases/d43_full_pointbank_p105673.pkl:b933cdb5…"
```

### 5.2 Results

* `seal_r3.py --verify` → `ok: true`, **28 archive members** (19 packet + 9
  external), all four `matches_disk` true, archive `403f790a…`, payload
  `d245952f…`.
* `preflight_r3.py --root .` → `preflight_pass: true`, rc 0, **6.4 s**.
* `python3 -O preflight_r3.py --root .` → `preflight_pass: true`, rc 0, 6.4 s.
  The two reports differ only inside `P11_custody_boundary`, and only in the
  per-run temporary-directory paths embedded in fault detail strings; two
  consecutive *normal* runs differ in exactly the same places. **There is no
  `assert` statement in any of the nine Python files** (`grep -c "assert "` =
  0 for each), so `-O` cannot silence anything.
* Standalone battery, run from `/tmp` with its own path loader:
  `battery_pass: true`, `battery_sha256 e416de0e…` = the R2 pin, 4.8 s.

| stage | counts |
|---|---|
| P1 packet manifest | **18/18** members, 0 mismatched |
| P2 archive replay | **28/28**, 0 missing / extra / mismatched |
| P3 GP static census | 99 sites → **110 predicted = 110 declared**; 13 loops, 0 unresolved; **29** predicted observables; 0/13 forbidden constructs; 99 labels, max width **63 ≤ 80**; ASCII, tab-free |
| P4 Python engine | **42/42** gates PASS; all four booleans true; the three `theorem_inputs` sets pairwise disjoint |
| P5 mutation battery | **58 MUST_FAIL + 4 MUST_SURVIVE + 19 separation controls + 5 unit tests**, 0 failed; census `{uncond_true_e_false: 8, both_true: 8, uncond_false: 46}` |
| P6 pinned hashes | 8/8 booleans true (census, observable, **new GP script hash**, gate count, observable count vs GP and vs pin, runner constants, E-layer observable set) |
| P7 emission policy | components `["K0"]`, idempotents `[0,1]`, count 1; forbidden-language scan CLEAN on all three blobs |
| P8 isolated-import controls | **8/8** |
| P9 authority controls | **33** authorization records + template refusal (`AUTHORIZATION_STATUS`) + 3 artifact-collision assertions + run-directory reuse on the new signature |
| P10 gate-surface controls | **10/10** |
| **P11 custody boundary** | **60 recorded controls + 13 hostile source mutations**, 0 failures (§5.3) |

### 5.3 P11 in detail — what is executed, and what is not

**Executed for real**, by a non-root user against real directories, real
`lstat` results, real uid/gid values, real mode bits:

* **4 POSIX facts** the whole boundary rests on:
  `dir_without_write_bit_refuses_create` (this is the R2 defect's kernel-level
  cause), `mode_0444_refuses_write_by_owner`,
  `unprivileged_chown_to_root_refused`, `o_excl_refuses_second_create`.
* **20 boundary controls** driving the real supervisor functions:
  `one_time_claim` (lease created, mode 0444, binds digest and run path;
  second claim → `AUTHORIZATION_REUSE`; exactly one lease in the whole tree),
  `parent_wrong_owner` → `PATH_OWNER`, `parent_group_writable` → `PATH_MODE`,
  `run_dir_absent`/`run_dir_wrong_mode`/`run_dir_wrong_owner`,
  `claim_absent`/`claim_wrong_mode`/`claim_service_written_refused`
  (`CLAIM_OWNER`), five `claim_wrong_*` binding cases (route, digest, run
  path, schema, service user), `claim_token_immutable_to_service` (write
  refused, `chown` to root refused, delete → `CLAIM_ABSENT` with **zero**
  leases in the tree), `crashed_run_refused` → `RUN_DIR_DIRTY`,
  `restart_after_clean_claim_refused` → `AUTHORIZATION_REUSE`,
  `lease_unwritable` → `LEASE_UNWRITABLE` against a real 0500 directory,
  `no_burn_before_verification` (**6 refusal cases**, each asserting the fault
  *and* that no lease exists anywhere in the tree afterwards), and
  `custody_then_runner_handshake`.
* **6 runner controls** on the REPAIR-2 law: `clean_launch_accepted` (the
  5-entry listing), `stale_artifact_refused`, `unstaged_source_refused`,
  `missing_lease_refused`, `foreign_authorization_refused`,
  `non_sha_marker_refused`.
* **7 production-policy pins** (static): `CustodyPolicy(` occurs **exactly
  once** in the supervisor, `production_policy` pins the literal
  `custodian_uid=0`, resolves the service identity from `pwd`/`grp`, reads no
  environment or argv; `run_job` uses it and calls `establish_custody`; the
  supervisor refuses to run as root.
* **13 mint/retire facts**, three of them live executions: `mint_claim_r3.sh`
  with no arguments → rc **64**; as a non-root user → rc **77**
  `MINT_REFUSED MINT_NOT_ROOT`; `retire_claim_r3.sh` non-root → rc **77**;
  `bash -n` clean on both; plus source-order assertions (spent marker before
  the run directory, `set -C` before the spent marker, token written before
  the chown to the service user) and the parent owner/realpath checks.
* **10 unit-contract facts**: `User=`/`Group=` equal the supervisor's
  constants, `ExecStartPre=+` mints as root, `ExecStopPost=+` retires as root,
  `ExecStart=` is unprivileged, `ReadWritePaths` is the run **directory** and
  no `ReadWritePaths` mentions a parent, empty capabilities,
  `NoNewPrivileges=yes`, `Restart=no`.

**13 hostile source mutations**, each patching one unique anchor in the sealed
supervisor or runner, loading the patched module, and requiring the named
control to stop holding. All 13 behave:

| mutation | control that must break | effect if shipped |
|---|---|---|
| CM1 `custodian_uid=0` → running uid | `production_policy_pins_uid_zero` | the deployed custodian would not be root |
| CM2 parent mode gate removed | `parent_group_writable` | group-writable sealed parent accepted |
| CM3 claim owner gate removed | `claim_service_written_refused` | a service-written claim authorizes |
| CM4 lease loses `O_EXCL` | `one_time_claim`, `restart_after_clean_claim_refused` | the authorization can be presented twice |
| CM5 burn moved before verification | `no_burn_before_verification` | a failed precondition consumes the authorization |
| CM6 lease `OSError` catch removed | `lease_unwritable` | R2's traceback returns |
| CM7 run-dir mode gate removed | `run_dir_wrong_mode` | a group-readable run directory accepted |
| CM8 run-dir owner gate removed | `run_dir_wrong_owner` | a foreign-owned run directory accepted |
| CM9 claim `run_path` binding dropped | `claim_wrong_run_path` | a claim minted elsewhere accepted |
| CM10 pristine gate removed | `crashed_run_refused` | a crashed run relaunches in place |
| CM11 R2's `PRE_RUN_FILES` restored | `clean_launch_accepted` | **the R2 defect**: every real launch refused |
| CM12 completeness check removed | `missing_lease_refused` | a launch that never took its lease accepted |
| CM13 both completeness checks removed | `unstaged_source_refused`, `missing_lease_refused` | a run that staged nothing accepted |

**Not executed, and no claim is made otherwise.** No fixture creates a
root-owned object: the producer host has no root, and the controls refuse to
run as root because root would bypass every denial they assert. The fixtures
therefore drive the same functions through a `CustodyPolicy` whose custodian
uid is the running uid. What carries the "the deployed custodian is root" claim
instead is (i) the 7 static pins above, (ii) mutation CM1, and (iii)
`custody_selftest_r3.py --on-host-dry-run`, run **as the service user on the
deployed host** before the unit starts, which calls the same
`verify_custody_preconditions` against the real root-owned tree and stops
before the lease, so it consumes nothing. Likewise systemd itself is not run:
the unit is checked as a contract against the supervisor's constants. A
reviewer who thinks the dry run should be a precondition inside the supervisor
rather than an operational step should say so — the review request asks that
question directly.

---

## 6. What did not change

* Both engines' mathematics, gate for gate: census `b828f93d…`, observables
  `4b1c7ff6…`, battery `e416de0e…`, all identical to R2, reproduced both
  inside the packet and from an out-of-tree standalone battery run.
* The unconditional/conditional separation: 42 gates, the three layer
  censuses, the pairwise-disjoint `theorem_inputs`, the 19 separation controls
  and the `{8, 8, 46}` census. No gate was retyped, added or removed.
* `validate_authorization_record` and every authorization semantic: same 33
  P9 cases, same exact-`PASS` verdict rule, same producer-model refusal, same
  single instance type.
* The terminal's four separated blocks, the single-engine typing of the E
  theorem, the emission policy, and the claim firewall.
* `emit_immutable`, the artifact caps, the manifest and archive replay, the
  sealed-module loader and the `-I -B` discipline.

---

## 7. Residual risk

1. **The GP file has never been parsed by any GP**, and R3 edited two of its
   lines. Every plausible failure lands in a runner refusal rather than a
   wrong verdict (the runner requires 110 parsed gate lines, the census line,
   29 observables and the terminal line), but the two-engine claim becomes
   true only when GP actually runs and agrees.
2. **The root-owned half of the boundary is unexecuted here** (§5.3). Its
   substitutes are the static pins, CM1, and the on-host dry run.
3. **systemd is not run.** `ExecStartPre=+` semantics (root, sandbox not
   applied, completes before the ExecStart namespace is built, so
   `ReadWritePaths=<run dir>` resolves) are taken from documented behaviour,
   not from an execution on this host.
4. The mint is deliberately unforgiving: it spends the digest *before* it
   creates the run directory, so a mint against an existing name retires the
   authorization and costs a coordinator record. That is the fail-closed
   direction and is stated in the script and the template.
5. Ancestor paths are `lstat`-ed, not resolved, in the unprivileged check, so
   a root-owned symlink ancestor pointing somewhere writable would pass. The
   deployed host's `/var/lib/jc2-k0` has no symlink ancestors, and
   `mint_claim_r3.sh` asserts `realpath "$parent" == "$parent"` as root at
   mint time. Adding a symlink-ancestor gate to the unprivileged side would
   make off-host fixtures impossible on this platform (`/tmp` and `/var` are
   symlinks on macOS); that trade is recorded rather than taken.
6. Everything the R2 review listed as residual for the mathematics (§10.3–7 of
   that report: the prose base, the E theorem's conditionality, frames as
   witnesses, the single-field battery, the compound-shrink boundary) stands
   unchanged, because the mathematics stands unchanged.
7. Nothing here is a D43 row, point, template, D25, raw-J, Keller or JC2
   result; nothing derives fieldness from the 432-frame count; and this report
   cannot enter an authorization record.

---

## 8. Status and the only licensed next action

`R3_SOURCE_READY_AWS_NOT_AUTHORIZED`.

The next action is a **hostile source review by a model other than Opus 5**,
charged by `cases/d43_k0_field_certificate_r3_20260829/REVIEW_REQUEST.md`
(SHA-256 `ff3a8e73cb4bd31607832c9eaf7f10e662884bb397ad302e171ba05bafc289ca`),
concentrated on the custody surface: `aws_supervisor_r3.py`'s boundary,
`runner_r3.py`'s run-directory law, the two root-side scripts,
`custody_selftest_r3.py`, P11, the unit template, and the two-line GP change.
The mathematical layers may cite the R2 review as already-confirmed **only
after** verifying the §3.1 diff is what it says it is.

A literal `PASS` from that review plus a coordinator GO, followed by the
deployment order in `authorization_template_r3.json` (sealed parent, frozen
authorization, root mint, service-user dry run, then start), is the only route
to a rehearsal.

## 9. Reproduction

```
cd /Users/dc/code/math/jc2
python3 cases/d43_k0_field_certificate_r3_20260829/seal_r3.py --root . --verify
python3 cases/d43_k0_field_certificate_r3_20260829/preflight_r3.py --root .
python3 -O cases/d43_k0_field_certificate_r3_20260829/preflight_r3.py --root .
python3 cases/d43_k0_field_certificate_r3_20260829/custody_selftest_r3.py
```

Body hash below: verify with
`sed -n '1,/^<!-- BODY-END -->$/p' <this file> | shasum -a 256`.

<!-- BODY-END -->
80ed2c4ea8a741764e812661b78f73a73a265517c7c65331c578ecfedcc7e011  body: everything from the first byte of this file through the BODY-END line inclusive
