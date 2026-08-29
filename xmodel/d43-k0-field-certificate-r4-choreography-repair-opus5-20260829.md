# D43 `K0` field certificate R4 — mint/dry-run choreography repair packet and producer report

**Verdict: `SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`**

**UTC:** 2026-08-29 (host clock 2026-08-28 local)
**Producer:** Opus 5 (`claude-opus-5`), the R3 producer
**Object:** `cases/d43_k0_field_certificate_r4_20260829/`, status
`R4_SOURCE_READY_AWS_NOT_AUTHORIZED`
**Charged by:** `xmodel/d43-k0-field-certificate-r3-hostile-review-grok46-20260829.md`
(SHA-256 `49c6dd90c1ec9d87b15ecf0b6f3bbac22f6fa3d0d96d25f1d740cf8a758b3eeb`,
verdict `PASS_WITH_REPAIR`)

## What this verdict does and does not license

* **R4 authorizes nothing on AWS.** This report is written by the producer, and
  `aws_supervisor_r4.validate_authorization_record` refuses any
  `reviewer_pass.model` that normalises to contain `opus`, and requires the
  verdict field to read exactly `PASS`. Neither condition is met by this file.
  A launch needs a fresh different-model source PASS of *this* packet plus a
  coordinator GO.
* It records that the R3 review's **one blocking finding — the deployment
  choreography — is repaired and the repair is executed**, that the review's
  second, non-blocking finding (the "consumes nothing" wording) is repaired
  and frozen by a control, and that the mathematics and the reviewed privilege
  boundary are unchanged and provably so.
* **The GP file has still never been parsed by any GP.** Nothing here changes
  that. R4 edits five comment lines of it; those edits are static-audited only.
* R3, R2 and R1 are untouched. All three remain on disk exactly as reviewed;
  §2.4 re-verifies five R3 hashes against the R3 report.

---

## 1. Execution gaps, stated first

* **No PARI/GP.** There is no `gp` on this host (`command -v gp` is a shell
  alias for `git push`). `k0_field_cert_r4.gp` was edited in its header comment
  only and re-audited statically; it has never been parsed by any GP, and no
  claim below says otherwise.
* **No AWS, no root, no systemd.** No AWS API was touched. Every fixture runs
  as an ordinary user (uid 501): **no fixture in this packet creates a
  root-owned object, and none runs under systemd.** §5.4 states exactly what
  that costs and what stands in its place, including one control whose executed
  refusal is weaker than its name suggests and is disclosed as such.
* No commit, no push, no canonical edit, no CAS, no nested formalization-tree
  access, no long or high-memory process. Everything below ran in seconds.

---

## 2. Byte hashes of everything shipped

### 2.1 The R4 packet, 18 sealed members plus 4 generated files

| file | SHA-256 |
|---|---|
| `README.md` | `756c712bd157230a65ab0544abeefd59758c39d4bd669b6720d032e9d0208980` |
| `REVIEW_REQUEST.md` | `20c01d63d7d905553b48e9433a9280e0440b9d9372e5a31f267cbab3f6cec0f3` |
| `authorization_template_r4.json` | `28be1a987aaac05d813a277cc1ad6b038ba758ea40459191e8abcc97436e5304` |
| `aws_supervisor_r4.py` | `556385ae87dafdfd7bcbd9c96b8abbfc98b56c3fe0d0453663018a5aba190e28` |
| `aws_worker_r4.sh` | `5590c270d7477f9c907cc60d267e700155f2d890d12d99277987b3bb65e16e49` |
| `custody_selftest_r4.py` | `5197046b33678ad7d719c9129c9dd78563d89f6dd5a2053c465a6db9803da4fe` |
| `execution_pins_r4.json` | `6622df3d8a23874f46dcb508805e9a20441a66e53e05d005c544efc37c4ca1b9` |
| `k0_algebra_r4.py` | `a7de3c3fcefc42302e402b8dfcaeefbba6d5a582ae694447e8f95f6a8e8dd4a6` |
| `k0_field_cert_r4.gp` | `f39ee4585ae16199708ea831fa3a36a233a347b21cd1e2ec3828f3026c795dcb` |
| `k0_field_checker_r4.py` | `0d53479c14fb446820a33c4f28e931f9a6ab1f5d95c4bcef4104081758dd5761` |
| `k0_mutations_r4.py` | `9a1fe0d396eaa6d6723005bd5da7c1201ec8e89d70b7707259162a08fff99b4f` |
| `mint_claim_r4.sh` | `051a7381f325489762b913fa5fbdf67bba2247d0a17de42733a0e72dfdc3a763` |
| `preflight_r4.py` | `b43622560c1afb29f8c15a5e01711275dc0bd4f683f0606ded07a228e53db58b` |
| `preregistration_r4.json` | `b56be168046957d7d8c6b99996695fc1b47eda92ae7a1ff137bbce3d40ec06fc` |
| `retire_claim_r4.sh` | `486e060b25f0cc423c193b862b10ef426a3cf4e08853c394a1b14349f07db4a0` |
| `runner_r4.py` | `a97bd68d1e89253a403b056e09c59b8f056f4ac3aef369823f01068039e2d614` |
| `seal_r4.py` | `9d756ad382032be208bfe803e54ed8791a1081e70b17dc9b06c8ac875082e01b` |
| `systemd_unit_template_r4.service` | `8979310d2798720de979477ba5fe11270e21be596e4291d18eac1c64b21af385` |

| generated | SHA-256 |
|---|---|
| `PAYLOAD.sha256` | `1650518ac9768c9ac0463bf27187e2af1a6344f601d736eaf74a2c286bd29ace` |
| `SOURCE_ARCHIVE.tar` (29 members) | `06c9d8d5af2edcba4cd548e7d13c17b89c30cbcc3ec94093bd5e1b442f77e134` |
| `SOURCE_ARCHIVE.sha256` | `3498278deb72c84e4b973a3d277053b4a1bb15a0c01e3997adcffb659b36df4a` |
| `SOURCE_SEAL.sha256` | `fafc30d9b8ca32abcf090218c320c26ab8d75811a7f9c6c679d678bedb46b0ae` |

### 2.2 The ten sealed external members

The nine R3 externals are carried at their reviewed hashes (emitter
`5420b5c0…`, rows `9fc9bd7a…`, pointbanks `bb0f13b6…` / `b933cdb5…`, bridge
`e1b99600…`, theorem report `6d3d53c2…`, Grok 4.6 theorem review `07f20be5…`,
Fable 5 R1 source review `29e9496e…`, Fable 5 R2 source review `824e24d7…`).
**New in R4**, sealed and pinned in `execution_pins_r4.json`, hashed by
`SRC_FILE_HASHES`:

| file | SHA-256 | role |
|---|---|---|
| `xmodel/d43-k0-field-certificate-r3-hostile-review-grok46-20260829.md` | `49c6dd90c1ec9d87b15ecf0b6f3bbac22f6fa3d0d96d25f1d740cf8a758b3eeb` | the review whose REPAIR-1 this packet answers |

### 2.3 Pinned run values — every mathematics hash identical to R2 and R3

```
route                       D43-K0-FIELD-CERT-R4     (changed)
python gates                42                       (unchanged)
gp gates (nexpect)          110                      (unchanged)
shared observables          29  (25 unconditional, 4 E)   (unchanged)
census   SHA-256   b828f93d6a29c15371e4d277473e63c0a25ba0280fa5ab44706d10c786f9aeb0   IDENTICAL to R2/R3
observable SHA-256 4b1c7ff63935adb27148a2967037b7a357354848b0bbc2f0df827db2e45148f6   IDENTICAL to R2/R3
battery  SHA-256   e416de0e074cc0125ac2419a724c420d0d5f9c4dcd141abbd276f477bafbc25b   IDENTICAL to R2/R3
gp script SHA-256  f39ee4585ae16199708ea831fa3a36a233a347b21cd1e2ec3828f3026c795dcb   REGENERATED (header comments only)
```

All three run hashes reproduce inside the packet and in a standalone
out-of-tree replay run from `/tmp` (§5.2).

### 2.4 R3 is untouched, re-verified against the R3 report

```
56f1fb1bd8a22a65967e8c78945c2940ee87e554564f3792ee05b0cea0df979a  r3/README.md
83c80c65a108339af68e75fe5ab52d2ed2b797130456ff02685e8179f2f71b0b  r3/aws_supervisor_r3.py
403f790afa9904962b4ad79ebb29cf50ef21c399bbf598f5007c771ee1002a37  r3/SOURCE_ARCHIVE.tar
b9de00ee60294654d962a1512641f94169c47197b5846c2612c643e7ea23ca81  r3/systemd_unit_template_r3.service
84727c5af08ba29169d1f73abc399a803edbf72325cb7f5ac178bf0795d29a5b  r3/authorization_template_r3.json
```

All five equal the values in the R3 producer report §2.1. No R3 file was
opened for writing at any point.

---

## 3. R3 → R4 diff inventory

### 3.1 File level

Comparison is against R3 after applying the R-number token rename
(`_r3`→`_r4`, `-r3`→`-r4`, `CERT-R3`→`CERT-R4`, `R3_SOURCE_READY`→`R4_…`,
`"r3_scope"`→`"r4_scope"`, packet dirname). The rename is length-preserving.
The GP file's `R3E`, the `r3` generator and the `[R3-A]`/`[R3-B]` change tags
are mathematics and history and were **not** renamed.

| file | R3 → R4 lines | +/− after rename | what changed |
|---|---|---|---|
| `k0_algebra_r4.py` | 669 → 669 | +0 −0 | **byte-identical** to R2's and R3's, SHA-256 `a7de3c3f…` |
| `aws_worker_r4.sh` | 31 → 31 | +0 −0 | identical after rename |
| `aws_supervisor_r4.py` | 979 → 979 | +1 −1 | the docstring title line. **Nothing else.** The whole custody boundary, `run_job`, and `validate_authorization_record` are untouched. |
| `runner_r4.py` | 810 → 810 | +1 −1 | the docstring title line |
| `k0_field_checker_r4.py` | 1675 → 1675 | +1 −1 | the docstring title line |
| `k0_mutations_r4.py` | 541 → 541 | +1 −1 | the docstring title line |
| `retire_claim_r4.sh` | 45 → 45 | +1 −1 | the header title line |
| `k0_field_cert_r4.gp` | 526 → 530 | +5 −1 | the header title plus a four-line note saying R4 changes nothing in either engine. All comments. |
| `seal_r4.py` | 151 → 153 | +6 −4 | the tenth external member and its docstring line |
| `execution_pins_r4.json` | 51 → 54 | +4 −1 | new GP hash, R3-review pin |
| `mint_claim_r4.sh` | 137 → 170 | +49 −16 | §4.2, the three-argument interface |
| `systemd_unit_template_r4.service` | 140 → 185 | +75 −30 | §4.1, the two `ExecStartPre` commands |
| `authorization_template_r4.json` | 88 → 120 | +61 −29 | §4.1, the one-path deployment order |
| `custody_selftest_r4.py` | 696 → 1490 | +836 −42 | §4.1/§4.3/§4.4, the four new control blocks, `--pre-mint-advisory`, the hardened CLI |
| `preflight_r4.py` | 1098 → 1233 | +144 −9 | `CM14`–`CM24` and four new mutation kinds |
| `preregistration_r4.json` | 239 → 269 | +50 −20 | R4 scope, supersession, the choreography block |
| `README.md` | 372 → 482 | +163 −53 | the choreography, the R3 disposition table |
| `REVIEW_REQUEST.md` | 310 → 427 | +160 −43 | the new charge (§G0), corrected replay hashes |

### 3.2 Function level

`custody_selftest_r4.py`

| function | change |
|---|---|
| `on_host_dry_run` | takes an optional `policy` (production caller passes none, so the deployed dry run always builds `production_policy()`); returns `lease_taken: False` and an explicit `cost` string instead of the old "consumes nothing" docstring |
| `pre_mint_advisory` | **new**; read-only, refuses `PREMINT_ALREADY_MINTED` once the run directory or the spent marker exists |
| `main` | **rewritten**; `--pre-mint-advisory`, mutual exclusion of the two modes, `rc 70` on *any* refusal including a non-`CustodyFault` exception, `CUSTODY_…_FAULT` on stderr |
| `unit_directives`, `_exec_entries` | **new**; the shipped unit parsed into ordered `(key, prefixes, command)` triples with backslash continuations joined |
| `choreography_controls` | **new**; 25 recorded controls (§4.1) |
| `dry_run_controls` | **new**; 13 recorded controls, executed against real trees (§4.3) |
| `pre_mint_advisory_controls` | **new**; 4 recorded controls |
| `call_graph_controls`, `_module_functions`, `_calls_in`, `_is_read_open`, `_verify_precedes_lease` | **new**; 11 recorded controls (§4.4) |
| `wording_controls` | **new**; 6 recorded controls over 8 forbidden and 7 required phrases |
| `fixture_authorization`, `_dry_run_fixture`, `_tree_snapshot` | **new** fixtures; the authorization is frozen on disk first and its digest read back from the bytes, so the claim token is minted for the *real* digest |
| `mint_script_controls` | 12 → 19 controls: the new arity, R3's four-argument call now `rc 64`, the derivation and recomposition, the "no external mint" statement |
| `unit_contract_controls` | uses the shared parser; `+ type_oneshot` |
| `run_controls` | four new blocks wired into the report and into `ok` |
| `production_policy_controls`, `posix_semantics_controls`, `boundary_controls`, `runner_pre_run_controls`, `build_tree`, `fixture_policy`, `_expect_fault`, `_leases_anywhere` | **unchanged** |

`preflight_r4.py`: `CUSTODY_MUTATIONS` 13 → 24 entries; `MUTATION_SOURCE`,
`WORDING_FILES`, `_stage` new; `custody_controls` gains the `unit`,
`template`, `selftest` and `callgraph` kinds. Nothing else moved.

`mint_claim_r4.sh`: `$# != 4` → `$# != 3`; `RUN_ARG` shape checks (`//`,
`/../`, `/./`, absolute); `PARENT=$(dirname …)`, `RUN_NAME=$(basename …)`;
recomposition test. Every existing gate — parent owner/mode/`realpath`,
authorization owner/mode, spent-first with `set -C`, token before the `chown`,
no JSON parser — is unchanged and re-pinned.

---

## 4. The repairs

### 4.1 REPAIR-1 — the choreography (the R3 review's blocking finding)

The defect, exactly as charged. `authorization_template_r3.json` carried, as a
sealed member and under the heading "DEPLOYMENT ORDER, which is not optional":
(c) root runs `mint_claim_r3.sh`, (d) ops runs the dry run as `jc2k0`, (e)
"only then start the unit". `systemd_unit_template_r3.service`'s only
`ExecStartPre=+` **is** that mint, and the mint spends
`<sealed parent>/spent/<digest>.spent` with `O_EXCL` before anything else
exists. A coordinator following the sealed order on a *correctly configured*
host therefore burned the licensed rehearsal at `ExecStartPre` with
`MINT_ALREADY_SPENT` rc 75, before the supervisor and before either engine.

**The R4 design: one atomic systemd choreography, and no other path.**

```
systemctl start jc2-d43-k0-field-cert-r4.service      <- the only launch action

  1. ExecStartPre=+   root      mint_claim_r4.sh          one-shot, spends first
  2. ExecStartPre=    jc2k0     custody_selftest_r4.py    --on-host-dry-run, no lease
  3. ExecStart=       jc2k0     aws_supervisor_r4.py      verify, then lease
  4. ExecStopPost=+   root      retire_claim_r4.sh        seals the evidence
```

The template, the unit, the preregistration, the README, the review request
and the static pins all describe exactly this. There is no external mint and
no external dry run anywhere in the packet.

**Why step 2 runs as the service identity, under the intended sandbox.**
systemd's executable prefixes are `@`, `-`, `:`, `!`, `!!` and `+`. `+` is the
only one that suppresses the user switch *and* the sandbox; `!`/`!!` suppress
only part of the user switch; `-` makes a failure non-fatal; `@` rewrites
argv[0]; `:` suppresses variable substitution. Step 2 carries **none** of
them, so systemd runs it with the unit's `User=jc2k0`, `Group=jc2k0`, empty
`CapabilityBoundingSet=`, `NoNewPrivileges=yes`, `ProtectSystem=strict`,
`SystemCallFilter=`, and a mount namespace built from the same
`ReadWritePaths=<ABSOLUTE_RUN_DIRECTORY>` / `ReadOnlyPaths=` as step 3 — the
identical identity and the identical view of the filesystem `ExecStart=` gets.
`ExecStartPre` commands complete before the next command's namespace is set
up, so `ReadWritePaths=<run dir>` resolves against a directory step 1 has
already created. A non-zero exit from step 1 or step 2 aborts the start, and
`ExecStopPost=` still runs. **This paragraph is documented systemd semantics,
not an execution; §5.4 says so.**

The unit itself is checked, not trusted: `choreography_controls` parses it
into ordered directives and records 25 controls —

* shape: `exec_start_pre_count == 2`, one `ExecStart`, one `ExecStopPost`, no
  `ExecStartPost`, mint at index 0, dry run at index 1, `dry_run_after_mint`;
* one-shot: `unit_mints_exactly_once`, `unit_dry_runs_exactly_once`;
* identity: `mint_is_root_prefixed`, `dry_run_carries_no_prefix`,
  `dry_run_runs_as_service_identity`, `dry_run_is_the_packet_selftest`,
  `dry_run_uses_isolated_interpreter` (`-I -B`), `start_carries_no_prefix`,
  `retire_is_root_prefixed`;
* fail-closed: `no_failure_tolerant_exec_prefixes` (every prefix set ⊆ `{+}`),
  `only_mint_and_retire_are_privileged`;
* composition: `run_directory_sentinel_users == [ExecStartPre, ExecStopPost,
  ReadWritePaths]`, `authorization_sentinel_users == [ExecStart,
  ExecStartPre]`, `no_split_run_directory_sentinels`, `mint_argument_count ==
  3`, `mint_arguments`, `dry_run_binds_run_path`, `dry_run_binds_authorization`.

### 4.2 REPAIR-1c — one sentinel per path (producer-found while repairing 4.1)

R3's mint took `<sealed parent> <run name>` while the unit's
`ReadWritePaths=`, the dry run and the retirement all named the run
*directory*, and **nothing checked that the two spellings composed**. A
coordinator who filled `<ABSOLUTE_SEALED_PARENT_DIRECTORY>` and
`<RUN_DIRECTORY_NAME>` inconsistently with `<ABSOLUTE_RUN_DIRECTORY>` would
have minted in one place and verified in another; the launch would have died
`CLAIM_ABSENT` *after* the mint had spent the digest.

`mint_claim_r4.sh` now takes the absolute run directory as one argument and
derives `PARENT=$(dirname …)`, `RUN_NAME=$(basename …)`, then asserts
`"$PARENT/$RUN_NAME" == "$RUN_ARG"`. The unit uses `<ABSOLUTE_RUN_DIRECTORY>`
in all four places and the agreement is now a control. New refusals:
`MINT_RUN_SHAPE` for a non-absolute path, an empty component (`//`), a
non-normalised path (`/../`, `/./`), or a failed recomposition;
`MINT_PARENT_SHAPE` for a run directory directly under `/`. R3's
four-argument call is now `rc 64` and is an executed control. Mutation `CM24`
restores the two-sentinel call and two controls fail.

### 4.3 The dry run cannot consume the one-shot claim — executed

`dry_run_controls` runs the real entry point against real trees, 13 recorded
controls:

* `dry_run_verifies_a_good_tree` — returns the right run directory, sees the
  claim, derives the digest from the file bytes, reports `lease_taken: false`;
* `dry_run_creates_nothing` — the **whole tree** (including
  `sealed/spent/<digest>.spent` and the frozen authorization) is compared
  before and after on `(S_IFMT, mode, size, mtime_ns, inode, nlink)` for every
  path; 6 paths, identical, and zero leases anywhere;
* `dry_run_does_not_spend_the_mint` — the spent ledger holds exactly the one
  marker it held before;
* **`dry_run_then_launch_still_succeeds`** — two dry runs, then
  `establish_custody`, which succeeds and produces exactly one lease. This is
  the load-bearing control: a dry run that consumed the claim could not leave
  it true;
* `dry_run_requires_service_identity` — a wrong-identity policy against a tree
  that is *also* broken (no claim token) yields `SERVICE_USER`, not
  `CLAIM_ABSENT`, so identity is checked first;
* `dry_run_reports_claim_absent` / `…_group_writable_parent` /
  `…_wrong_run_dir_mode` — each fault propagates, each with zero leases in the
  tree afterwards;
* `dry_run_refuses_run_path_mismatch` (`RUN_DIR_SHAPE`) and
  `dry_run_refuses_an_unauthorized_record` (`AUTHORIZATION_STATUS`);
* `dry_run_cli_fails_closed` (rc 70, `ok: false`, `consumed: false`),
  `dry_run_cli_requires_its_arguments` (rc 2),
  `dry_run_and_advisory_are_never_combined` (rc 2).

### 4.4 The same claim, statically

`call_graph_controls` walks the supervisor AST from
`verify_custody_preconditions`, following local calls **and** attribute calls
whose name matches a function or method defined in the module. It reports the
reachable set —

```
_lstat, authorization_lease_name, claim_token_name, describe, fault,
require_root_owned_immutable, require_run_dir_pristine,
require_service_owned_run_dir, sha256_path, verify_claim_token,
verify_custody_preconditions
```

— and requires: no name and no attribute in that closure is one of 27 write
primitives (`mkdir`, `chmod`, `chown`, `unlink`, `rename`, `write_text`,
`touch`, `rmtree`, `atomic_bytes`, `fsync_directory`, `extractall`, …) or
`claim_authorization_lease` / `establish_custody`; every `open` on the path is
read-mode; the four gate functions *are* covered; `on_host_dry_run`'s `sup.*`
calls are a subset of `{production_policy, require_service_identity,
validate_authorization_record, verify_custody_preconditions, fault}` and
include the last two; and `establish_custody` calls verify **before** the
lease, checked by source position. Mutation `CM22` adds one `.touch()` inside
`verify_custody_preconditions` and the control fails.

### 4.5 REPAIR-1d — what a refusal actually costs

The review's second finding: "consumes nothing" and "a failed precondition
never consumes this record" are true of the **lease** and false of the
**mint**. Every sealed file now says instead that *the mint has already spent
the digest*, so a refusal from `systemctl start` onwards retires the
coordinator record. `wording_controls` freezes this: 8 forbidden phrases and 7
required phrases across 7 files, compared case-insensitively. The forbidden
strings are assembled from fragments so that the control file does not itself
contain the text it forbids. Mutations `CM15` and `CM23` restore the R3
sentences and the controls fail.

The reviewer's optional suggestion — "a **pre-mint** parent-only check … if the
producer wants a refusal that really costs no coordinator record" — is taken as
`custody_selftest_r4.py --pre-mint-advisory`. It validates the record and the
sealed parent, is read-only, and **refuses `PREMINT_ALREADY_MINTED` the moment
the run directory or the spent marker exists**, which is what stops it becoming
a second launch path: it cannot be run in place of step 2, and it cannot mint
or lease. Four executed controls, including that it creates nothing.

### 4.6 Recorded and deliberately not changed

| item | why not |
|---|---|
| §5, "I do **not** want the dry-run duplicated as a precondition inside `run_job`" | honoured. `run_job` is byte-identical after the rename; no dry-run code was added to it. |
| §11.3, ancestors are `lstat`-ed, not resolved, on the unprivileged side | carried. `mint_claim_r4.sh` still `realpath`-checks the parent as root; demanding resolution on the unprivileged side would make off-host fixtures impossible (`/tmp` and `/var` are symlinks on macOS). Recorded, not solved, and not weakened. |
| §11.6, `0pus 5` through `normalize_model` | `validate_authorization_record` stays frozen: the charge forbids changing authorization semantics, and both prior reviews called this a note. |
| §6, `IDEMPOTENTS_ONLY_0_1` retyping | would move a gate between the `theorem_inputs` censuses — the D1 separation surface — and change a census hash this packet must preserve. |
| §7, the GP leading-term block validates declared `LEAD` data | changing it changes the GP engine, which this charge excludes. The README says so. |
| §6, the coordinated multi-field scope shrink passes the checker | already documented in R2/R3 and refused at run level by the observable pin and cross-engine agreement. |
| R3 review's charge-doc note (the review request quoted the **R2** GP hash) | fixed: R4's review request quotes `f39ee458…` and P6 checks the pin against the file. |

---

## 5. Tests executed, with exact commands and counts

### 5.1 Commands

```
cd /Users/dc/code/math/jc2
python3 cases/d43_k0_field_certificate_r4_20260829/seal_r4.py --root . --verify
python3 cases/d43_k0_field_certificate_r4_20260829/preflight_r4.py --root .
python3 -O cases/d43_k0_field_certificate_r4_20260829/preflight_r4.py --root .
python3 cases/d43_k0_field_certificate_r4_20260829/custody_selftest_r4.py
```

### 5.2 Results

* `seal_r4.py --verify` → `ok: true`, **29 archive members** (19 packet + 10
  external), all four `matches_disk` true, archive `06c9d8d5…`, payload
  `1650518a…`.
* `preflight_r4.py --root .` → `preflight_pass: true`, rc 0, **9.2 s**.
* `python3 -O preflight_r4.py --root .` → `preflight_pass: true`, rc 0, 9.4 s.
  Flattened leaf-by-leaf against the normal report: **24 leaves differ, 22 of
  them per-run temporary paths and the other 2 the fixture authorization
  digest and lease name, which embed a temporary path.** Two consecutive
  *normal* `custody_selftest_r4.py` runs were diffed the same way and differ in
  the same 24 leaves and the same 2 non-path leaves. **There is no `assert`
  statement in any of the eight Python files** (`grep -c '^\s*assert ' = 0`
  for each), so `-O` cannot silence anything.
* `custody_selftest_r4.py` standalone → `ok: true`, rc 0, uid 501, all ten
  blocks true.
* Standalone battery, run from `/tmp` with its own path loader:
  `battery_pass: true`, `battery_sha256 e416de0e…` = the R2/R3 pin, 58
  MUST_FAIL + 4 MUST_SURVIVE, `failed_entries` empty, separation census
  `{uncond_true_e_false: 8, both_true: 8, uncond_false: 46}`.

| stage | counts |
|---|---|
| P1 packet manifest | **18/18** members, 0 mismatched |
| P2 archive replay | **29/29**, 0 missing / extra / mismatched |
| P3 GP static census | 99 sites → **110 predicted = 110 declared**; 13 loops, 0 unresolved; **29** predicted observables; 0 forbidden constructs; 99 labels, max width **63 ≤ 80**; ASCII, tab-free |
| P4 Python engine | **42/42** gates PASS; all four booleans true; the three `theorem_inputs` sets pairwise disjoint |
| P5 mutation battery | **58 MUST_FAIL + 4 MUST_SURVIVE + 19 separation controls + 5 unit tests**, 0 failed; census `{8, 8, 46}` |
| P6 pinned hashes | 8/8 booleans true (census, observable, **new GP script hash**, gate count, observable count vs GP and vs pin, runner constants, E-layer observable set) |
| P7 emission policy | components `["K0"]`, idempotents `[0,1]`, count 1; forbidden-language scan CLEAN on all three blobs |
| P8 isolated-import controls | **8/8** (`N1`–`N8`) |
| P9 authority controls | **33** authorization records + template refusal + 3 artifact-collision assertions + the run-directory control |
| P10 gate-surface controls | **10/10** probes |
| **P11 custody boundary** | **11 blocks, 129 recorded controls + 24 hostile source mutations**, 0 failures (§5.3) |

### 5.3 P11 in detail

| block | controls | what it executes |
|---|---|---|
| `production_policy` | 8 | static: `CustodyPolicy(` occurs once, literal `custodian_uid=0`, passwd/group resolution, no env or argv, `run_job` uses it, the supervisor refuses root |
| `posix_semantics` | 6 | the four POSIX facts the boundary rests on, for real |
| `boundary` | 20 | the R3 custody sequence, unchanged: one-time claim, both parent branches, the run-directory gates, the five claim bindings, token immutability, crash/restart, `LEASE_UNWRITABLE` on a real 0500 directory, `no_burn_before_verification` (6 refusal cases, 0 leases after each) |
| `runner_pre_run_law` | 6 | the R3 REPAIR-2 law, both directions |
| `mint_script` | 19 | **R4**: 3-argument arity, R3's 4-argument call → rc 64, derivation and recomposition, path-shape rejections, "no external mint"; plus R3's non-root rc 77, usage rc 64, `bash -n`, spent-before-run-dir, `set -C`-before-spent, token-before-`chown`, parent owner/realpath, no JSON parser |
| `unit_contract` | 11 | identity/sandbox contract vs the supervisor's constants, `Type=oneshot` |
| `choreography` | 25 | **R4**, §4.1 |
| `dry_run` | 13 | **R4**, §4.3 |
| `pre_mint_advisory` | 4 | **R4**, §4.5 |
| `call_graph` | 11 | **R4**, §4.4 |
| `wording` | 6 | **R4**, §4.5 |

**24 hostile source mutations**, five kinds, each patching one unique anchor
(`anchor_hits == 1` is itself checked) and requiring the named controls to
stop holding. All 24 behave; `failed_mutations: []`.

| mutation | kind | control that must break | effect if shipped |
|---|---|---|---|
| CM1–CM10 | static / boundary | as in R3 | the R3 boundary defects |
| CM11–CM13 | runner | as in R3 | the R3 run-directory defects |
| **CM14** unit gains a second mint | unit | `unit_mints_exactly_once`, `mint_is_the_first_exec_start_pre`, `dry_run_is_the_second_exec_start_pre` | the unit mints twice; the second dies `MINT_ALREADY_SPENT` |
| **CM15** template restores R3's "only then start the unit" | template | `no_forbidden_phrase`, `no_missing_required_phrase` | **the R3 defect**: the coordinator record orders an external mint |
| **CM16** dry run gains `+` | unit | `dry_run_carries_no_prefix`, `dry_run_runs_as_service_identity`, `only_mint_and_retire_are_privileged` | the dry run runs as root and proves nothing about `jc2k0` |
| **CM17** dry run placed before the mint | unit | `mint_is_the_first_exec_start_pre`, `dry_run_is_the_second_exec_start_pre`, `dry_run_after_mint` | the dry run always dies `RUN_DIR_ABSENT` |
| **CM18** dry run gains `-` | unit | `no_failure_tolerant_exec_prefixes`, `dry_run_carries_no_prefix` | a refused dry run is non-fatal and `ExecStart` runs anyway |
| **CM19** dry run calls `establish_custody` | selftest | `dry_run_creates_nothing`, `dry_run_then_launch_still_succeeds` | the dry run burns the authorization it was checking |
| **CM20** dry run drops `require_service_identity` | selftest | `dry_run_requires_service_identity`, `dry_run_checks_identity` | the dry run no longer proves it ran as the service user |
| **CM21** dry-run CLI exits 0 on refusal | selftest | `dry_run_cli_fails_closed` | systemd proceeds to `ExecStart` after a refused dry run |
| **CM22** `verify_custody_preconditions` touches a file | callgraph | `reaches_no_write_primitive` | the dry run is no longer read-only |
| **CM23** template restores "never consumes this record" | template | `no_forbidden_phrase` | the record claims again that a refusal after the mint is free |
| **CM24** unit restores the two-sentinel mint call | unit | `mint_arguments`, `no_split_run_directory_sentinels` | parent and name need not compose to the verified directory |

For the `selftest` kind the **sealed** controls drive the **mutated** entry
point (`CS.dry_run_controls(SUP, root, cs=cs_mut, cli_dir=<staged>)`), so a
mutation cannot weaken the control that catches it.

### 5.4 What is **not** executed, and one control that is weaker than its name

* **No root-owned object, no systemd, no GP.** Unchanged from R3, and R4 adds
  no root fixture. The `ExecStartPre=+` / no-prefix semantics in §4.1 are
  documented systemd behaviour, not an execution on this host. What carries
  the deployed claims instead: the 8 production-policy static pins, `CM1`, the
  25 parsed unit controls, and the unit's own step 2 on the deployed host.
* **`dry_run_cli_fails_closed` is honest but partial.** It executes the shipped
  CLI as a subprocess and observes rc **70** with `ok: false` and
  `consumed: false` — but on this host the refusal is `SERVICE_USER` ("the
  dedicated service user jc2k0 has no passwd entry"), raised by
  `production_policy()` before any filesystem check. It therefore pins the
  exit-code contract that systemd reads, and `CM21` shows that pin is
  load-bearing, but it does **not** execute a full custody verification through
  the CLI. The full verification is executed through `on_host_dry_run` directly,
  with a fixture policy, by the other twelve `dry_run` controls.
* The fixture policy still cannot make a root-owned object, so
  `custodian_uid` is the running uid in every fixture. That seam is unchanged
  from R3 and pinned the same way.

---

## 6. What did not change

* Both engines' mathematics, gate for gate: census `b828f93d…`, observables
  `4b1c7ff6…`, battery `e416de0e…`, all identical to R2 and R3, reproduced
  inside the packet and from an out-of-tree standalone battery run.
* The privilege boundary the R3 review confirmed: `aws_supervisor_r4.py`
  differs from `aws_supervisor_r3.py` by one docstring line after the rename.
  `require_root_owned_immutable`, `require_service_owned_run_dir`,
  `verify_claim_token`, `require_run_dir_pristine`,
  `claim_authorization_lease`, `establish_custody`, `run_job` and
  `validate_authorization_record` are untouched.
* The runner's REPAIR-2 run-directory law: `runner_r4.py` differs by one
  docstring line.
* The unconditional/conditional separation: 42 gates, three layer censuses,
  pairwise-disjoint `theorem_inputs`, 19 separation controls, `{8, 8, 46}`.
* `retire_claim_r4.sh`, the terminal's four separated blocks, the single-engine
  typing of the E theorem, the emission policy, the claim firewall,
  `emit_immutable`, the artifact caps, the sealed-module loader and `-I -B`.

---

## 7. Residual risk

1. **The GP file has never been parsed by any GP.** R4 changes five comment
   lines of it and nothing else. The two-engine claim remains execution debt.
2. **The root-owned half and systemd are unexecuted here** (§5.4). Their
   substitutes are the static pins, `CM1`, the 25 parsed unit controls, and
   step 2 on the deployed host.
3. **`dry_run_cli_fails_closed` refuses for the wrong reason on this host**
   (§5.4). Disclosed rather than dressed up.
4. **The mint still spends before any verification.** That is the fail-closed
   direction and R4 does not change it; what R4 changes is that the packet now
   *says* so everywhere, and that the only free check is `--pre-mint-advisory`
   before the unit starts.
5. **Ancestor paths are `lstat`-ed, not resolved,** on the unprivileged side. A
   root-owned symlink ancestor pointing somewhere writable would pass.
   Unchanged from R3, recorded, not solved, not weakened.
6. **`ExecStopPost=+ retire_claim_r4.sh` exits rc 72 when step 1 refused** and
   no run directory exists. Logged; no custody state changes; the script was
   deliberately left byte-identical rather than made tolerant.
7. **The choreography controls read the shipped template.** They cannot stop a
   coordinator who edits the installed unit after review; the unit is required
   to be root-owned 0444 with drop-ins forbidden, which is an operational
   control, not a checked one.
8. Everything the R2 and R3 reviews listed as residual for the mathematics
   stands unchanged, because the mathematics stands unchanged.
9. Nothing here is a D43 row, point, template, D25, raw-J, Keller or JC2
   result; nothing derives fieldness from the 432-frame count; and this report
   cannot enter an authorization record.

---

## 8. Status and the only licensed next action

`R4_SOURCE_READY_AWS_NOT_AUTHORIZED`.

The next action is a **hostile source review by a model other than Opus 5**,
charged by `cases/d43_k0_field_certificate_r4_20260829/REVIEW_REQUEST.md`
(SHA-256 `20c01d63d7d905553b48e9433a9280e0440b9d9372e5a31f267cbab3f6cec0f3`),
concentrated on §G0: the unit, the coordinator template, the three-argument
mint, `custody_selftest_r4.py`'s new blocks, and `CM14`–`CM24`. The
mathematical layers and the privilege boundary may cite the Grok 4.6 R3 review
as already-confirmed **only after** verifying the §3.1 diff is what it says it
is.

A literal `PASS` from that review plus a coordinator GO, followed by the
deployment order in `authorization_template_r4.json` — sealed parent, frozen
and tagged authorization, unit installed, optional `--pre-mint-advisory`, then
one `systemctl start` — is the only route to a rehearsal.

## 9. Reproduction

```
cd /Users/dc/code/math/jc2
python3 cases/d43_k0_field_certificate_r4_20260829/seal_r4.py --root . --verify
python3 cases/d43_k0_field_certificate_r4_20260829/preflight_r4.py --root .
python3 -O cases/d43_k0_field_certificate_r4_20260829/preflight_r4.py --root .
python3 cases/d43_k0_field_certificate_r4_20260829/custody_selftest_r4.py
```

Body hash below: verify with
`sed -n '1,/^<!-- BODY-END -->$/p' <this file> | shasum -a 256`.
Full-file hash is of this file through the body-hash line inclusive (the
`full:` line is excluded).

<!-- BODY-END -->
b8ab9a563867a0ba3f329c6428971799acad150478cf49d4b5ff513638e59c62  body: everything from the first byte of this file through the BODY-END line inclusive
9c906bf7c4a8ea507257a7873c79f4e501ab3d984a5595d34706ff1741118d11  full: this file through the body-hash line inclusive (this full-hash line excluded)
