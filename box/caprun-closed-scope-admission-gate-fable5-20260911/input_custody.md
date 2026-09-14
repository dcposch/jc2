# Input custody — caprun-closed-scope-admission-gate-fable5-20260911

Reviewer: Fable 5.1 (claude-fable-5-1), FIRST static review of the exact holder/admission bytes. First action 2026-09-11 09:36:48 UTC (recorded with `date -u` before any read). At that instant both owned targets were ABSENT: `xmodel/caprun-closed-scope-admission-gate-fable5-20260911.md` and the directory `box/caprun-closed-scope-admission-gate-fable5-20260911/` did not exist. Original reserve 09:54 / hard 09:57 UTC, never reset. Inputs are the nine read-only files at `/tmp/jc2-lane.0oins9/inputs` plus the automatic FALLACY-v2 guardrail. No linked report, ledger, history, network or live host byte was read.

## Pre-read pins (sha256sum at 09:36:48Z) — all nine MATCH the charged list

| file | sha256 | bytes |
|---|---|---|
| holder.template.py | cbbddf401192c7548c12e3bc8c59c291ecc2b3b101a20e6f18bcf1f67318fa20 | 6753 |
| outer-admission.template.sh | 99cb19a535c8233143db8a4dc68ac0dd93f1ae9b2e68211af9522fb6145d611c | 6006 |
| README.md | 5cb4b2ab34f34f35de3bc7da36b41bbc983ccdf3d3b9ae40976487056258e82c | 15162 |
| caprun-closed-scope-admission-astra-20260911.md | e4345bab4096f2b856524619d3c5408ae4044b27f95ab45a7b8fa35d688bb59c | 5662 |
| caprun-closed-scope-admission-astra-20260911.md.artifact.json | 8db41bfae391268e5819b218b887dbc08468310b512c4f9704e7db841be04c93 | 695 |
| caprun-closed-scope-launch-order-astra-20260911.md | d91e854348bac0836eea57feb67665b9ea06941eeb574c8ce286e5698d4cb20e | 14804 |
| ROOT-REGISTRATION.template.json | db925cbf9dad59b39444ea4250b839584be68c3bc5353aee5af924d96034e8f4 | 29126 |
| CONTRACT.md | af7a2fab4aa6317f7386e438f2f03acc6daffdd04c3deee6a6554b675089ee81 | 12348 |
| outer-launch.template.sh | 2a4a7ff45c19f8bfa386da8caddd44e8cd80c44d54e04e043f7e3fb731cb478e | 4214 |

## Read scope

All nine were read fresh and WHOLE through EOF with `cat -n` / `sed -n` in parallel single-file calls (no clipping occurred; the 808-line registration was read in two consecutive ranges 1–330 and 331–808). Registration scope: MACHINE_WHOLE text read plus human-WHOLE attention to `outer_argv`, `environment`, `aggregate_cpu_start_usec`, `limits`, `source_limits`, `cgroup_path`, `execution_mode`, `allowed_phases`, `phase_policy`, `typed_slot_policy`, `closed_child_guard`, `pins`, `files`, `enabled`, `exclusive_no_concurrent_writer`; the nine `commands` vectors were read but not re-audited (accepted upstream).

## Administrative checks performed (text/hash/date/diff only)

- Nothing was executed, imported, syntax-checked, compiled, AST-parsed or smoke-tested; no Python, CAS, subprocess of any candidate, AWS, SSH, git, process control or other agent was used. The only process invocations were `sha256sum`, `diff`, `cmp`, `sed`, `grep`, `wc`, `printf`, `date`, `ls`, `pwd`, and the mandated apply_patch tool (one empty-input usage probe, which printed usage and wrote nothing).
- Old/new outer diff: `diff -u --label accepted-outer-launch.template.sh --label proposed-outer-admission.template.sh` over the two pinned inputs is BYTE-IDENTICAL to the README `diff` block (105 changed +/- lines).
- Admission report seal: body through the standalone `<!-- BODY-END -->` line = 5330 bytes, sha256 `1516391426d7ac1901e17698340afbe5e53cf7744b90c641f8d4ee4b8b1c6e99`; matches its Seal and the artifact json (`file_bytes` 5662, `full_sha256` = pinned e4345bab…, closed/finalized 09:29:16Z, before this lane's first action).
- Launch-order seal: body = 14471 bytes, sha256 `a9881c8959d19d5804935c56e8023e90fa811ae6b05996f379c9932b1d75f344`; matches its Seal.
- Byte counts by `printf | wc -c`: sentinel line `HOLDER_WAITING_FOR_ROOT_RELEASE\n` = 32 bytes; frame `RELEASE ` + 64 hex + `\n` = 73 bytes.
- Placeholder counts by grep: holder 8 lines, outer-admission 13 lines, registration 75 lines; all guards disabled.
- Holder `OUTER` (lines 23–24) and `ENV` (line 25) compared by eye to registration `outer_argv` (lines 94–102) and `environment` (lines 45–50): literal seven-element and four-key matches.

## Post-write pins

Filled in below after the report body was written and before the final `<!-- BODY-END -->` append.

Post-write `sha256sum` of all nine inputs at 2026-09-11 09:46:28 UTC, after the report body sections A–D were written and before the E–G append and the final `<!-- BODY-END -->`:

| file | post-write sha256 | equals pre-read |
|---|---|---|
| holder.template.py | cbbddf401192c7548c12e3bc8c59c291ecc2b3b101a20e6f18bcf1f67318fa20 | yes |
| outer-admission.template.sh | 99cb19a535c8233143db8a4dc68ac0dd93f1ae9b2e68211af9522fb6145d611c | yes |
| README.md | 5cb4b2ab34f34f35de3bc7da36b41bbc983ccdf3d3b9ae40976487056258e82c | yes |
| caprun-closed-scope-admission-astra-20260911.md | e4345bab4096f2b856524619d3c5408ae4044b27f95ab45a7b8fa35d688bb59c | yes |
| caprun-closed-scope-admission-astra-20260911.md.artifact.json | 8db41bfae391268e5819b218b887dbc08468310b512c4f9704e7db841be04c93 | yes |
| caprun-closed-scope-launch-order-astra-20260911.md | d91e854348bac0836eea57feb67665b9ea06941eeb574c8ce286e5698d4cb20e | yes |
| ROOT-REGISTRATION.template.json | db925cbf9dad59b39444ea4250b839584be68c3bc5353aee5af924d96034e8f4 | yes |
| CONTRACT.md | af7a2fab4aa6317f7386e438f2f03acc6daffdd04c3deee6a6554b675089ee81 | yes |
| outer-launch.template.sh | 2a4a7ff45c19f8bfa386da8caddd44e8cd80c44d54e04e043f7e3fb731cb478e | yes |

Owned outputs: only this file and `xmodel/caprun-closed-scope-admission-gate-fable5-20260911.md`. Both written solely through the mandated apply_patch tool; no Write/Edit/redirection, no other file, no local transaction, no author Seal (the adapter seals). Deviation: the report's first apply_patch write measured 1571 words by `wc -w`, 71 over the 1500-word per-write ceiling; all other writes were shorter. A whole readback of both owned files precedes the final marker append.
