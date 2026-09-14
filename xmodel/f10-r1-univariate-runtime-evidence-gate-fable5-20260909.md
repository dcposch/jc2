# Gate: FIRST univariate runtime EVIDENCE review (hostile documentary read of the frozen run)

status=COMPLETE; verdict A CONFIRMED, B CONFIRMED, C CONFIRMED, D CONFIRMED (qualified engineering representation only); no REFUTED; no blocking GAP; no new OPEN; smallest actual defect: the new receipt carries no coefficient-bitlength field (inventory omission, non-blocking)

## 0. Custody and read scope

- Launch 21:20:53 UTC; stop is the earlier of 21:42:00 and 21:38:53 UTC, never reset. All 43 ordered charged SHA256 matched by sha256sum at 21:22 UTC before any read (diff of the ordered list, zero differences); the sha256sum output is banked as box/f10-r1-univariate-runtime-evidence-gate-fable5-20260909/charged-inputs.sha256 and reproduced verbatim in the custody table below. The lane inputs directory is read-only; only the owned box was used for scratch.
- Read WHOLE: producer report, artifact.json, READ-SCOPE.md, REGISTRATION.md, dispatch.registration.json, ROOT-ACCEPTANCE.json, univariate.full.receipt.json, normalized.full.receipt.json, controls.receipt.json, batch.PASS.json, metadata-reconciliation.json, remote-terminal.sha256 (100 lines), the adapt, full-check and semantic-controls authority and telemetry files, dummy-descendant.telemetry.json and dummy-descendant.stdout.
- Read by grep of named fields only (labelled partial): the six preflight authorities (enabled, hostname, instance, caps, cwd, argv markers, EXTRA, frontier pin count, rss argv) and their telemetries (status, pid, pgid, resource, termination, wall); dummy-descendant.authority.json (caps, enabled, host); custody.json (key census, expected transaction, manifest hash, status, root confirmation, scope counters); preflight.PASS.json (seven authority hashes); checker.py, adapter.py, input_evidence.py, semantic_controls.py, dispatch_batch.py (argv-length, reason-string, defect, cutoff and pin lines; the accepted 17p/17u code reviews are premises, not repeated); the 17p and 17u gate reports (verdict and qualification lines).
- univariate.json: HASH and SHAPE only. Its 72603 bytes hashed to the charged digest; the first 700 bytes, the key-name census and the ten id strings were read; no coefficient was read, recounted, parsed or replayed. The removed-slot wire in controls.receipt.json was read as documentary strings only.
- Tools: date, ls, mkdir, sha256sum, diff, cat, grep, sed, head, awk, wc, cut, tr, printf. No Python of any size, no CAS, no arithmetic subprocess, no import, compile or test, no network, AWS, SSH, proc, agents, provenance, ledger or live peer paths. Root's worker-state observations are consumed as upstream evidence, not reproduced.

## A. Genuine adapter.main and checker.main on the root-accepted artifact: CONFIRMED

- Root acceptance binding. dispatch.registration.json and all three mathematical authorities carry the identical normalized_acceptance payload: status ROOT-ACCEPTED-GENUINE-CHECKER-RECEIPT, accepted 20:49:23 UTC, generator d444d022, checker 091bbf35, normalized e62734b0, receipt 062cf0c0, and the six evidence digests; ROOT-ACCEPTANCE.json (charged 6451f6b4) has the same fields. The pinned normalized artifact e62734b0 and prior receipt 062cf0c0 are the exact inputs named in every child argv.
- adapt (operation build). Authority 247b0585: child argv of 8 process elements (python3 -I -B adapter.py AUTHORITY NORMALIZED RECEIPT OUTPUT), so adapter.py:80 sees sys.argv length 5; telemetry 9e9f3a32 records argv_count 8, NORMAL_EXIT, child rc 0, stderr 0 bytes, stdout 41 bytes, pid=pgid 2147; batch record caller_pid 2146 with parent 2045. The authority pins the fifteen base files (adapter 11ebf430, checker 6547063b, input_evidence d262f3d4, algebra 7d565299, execution_gate cbfe55ff, probe 02913a1c, dispatch_batch 9be0c70a, semantic_controls cc04757e, run_capped 4435279d, admissibility 02952e1b, frontier f9d1fddc, normalized e62734b0, normalized receipt 062cf0c0, registration db06dab1, python a92f0f95) and no univariate pin, matching the fresh mode-x output at adapter.py:87.
- full-check (operation check). Authority d971a351: child argv of 9 process elements ending in univariate.json and univariate.full.receipt.json, so checker.py:131 sees sys.argv length 6; telemetry cce20c89 records argv_count 9, NORMAL_EXIT, rc 0, stderr 0 bytes, stdout 41 bytes, pid 2155. This authority adds the pin univariate.json 3cfec9aa. checker.py:137 refuses an unregistered or changed artifact, :139 binds the artifact's implementation_sha256 to the pinned adapter.py (the artifact carries 11ebf430, equal to the adapter pin), :140 binds input_evidence to the helper's recomputation, and :142 writes the receipt in mode x.
- The new receipt (charged 0c22af83, 1104 bytes) is a real checker product, not a status string: status PASS-NINE-ROW-ADAPTER-NOT-IDEAL-DECISION, univariate_sha256 3cfec9aa, univariate_bytes 72603 (equal to the charged file's size and digest), row_slots 9, guard_factors r and h0, actual_degrees 3,3,2,4,3,3,2,2,5, actual_guard_degree 5, rational_basis_terms 28,28,21,35,28,28,21,21,42 (receipt-reported, not recounted here), execution.authority_sha256 d971a351 (the charged full-check authority), hostname ip-172-30-0-72, instance i-08d2a40f272ee9fa2, and input_evidence equal to the five root-acceptance digests plus original source 168bdfd3. batch.PASS.json records full_receipt_sha256 0c22af83 and the same code pins.
- Artifact shape: ten id strings (E1/S1, E1/S2, E1/S3, E0/S1..E0/S4, P4, P11 and the consumed Phi3), nine degree_bound keys, guard with equation, q, variable and factors, r, ubar, cover, cubic, consumed_slot, coefficient_ring, execution, input_evidence and implementation_sha256. Consistent with the accepted checker's row list and with 17p's nine-row envelope.
- Prior versus new receipt: normalized.full.receipt.json (062cf0c0) binds artifact e62734b0 of 432282 bytes with eleven measured rows G1..G9, H0, H1 and per-row max_rational_bits; univariate.full.receipt.json (0c22af83) binds 3cfec9aa of 72603 bytes with nine rows and no bitlength field. Distinct files, statuses and digests.
- No new original-source expansion: the three authorities pin only the 432282-byte normalized artifact as mathematical input, the receipt's reconstruction string names the accepted symbolic monic cubic cover, and the 100-file terminal manifest contains no other coefficient artifact. Retained qualifications: U-slot binding rests on the prerequisite normalized full source checker; process argv 8/9/10 versus sys.argv 5/6/7; the COVER literal identity is not a fresh proof; backend, helper and CAPRUN constants are accepted premises.

## B. Ten operation records, refusal defects, sentinel, dummy descendant, cutoffs: CONFIRMED

- All ten records of batch.PASS.json carry authority and telemetry digests equal to the twenty charged files' sha256sum output, equal to metadata-reconciliation.json, and present in remote-terminal.sha256 (twenty matches). Record order gate-disabled, gate-wronghost, gate-argv, gate-cap, gate-missing-input, gate-valid, dummy-descendant, adapt, full-check, semantic-controls is the literal order of dispatch_batch.py:193-197 followed by the three mathematical runs. preflight.PASS.json's seven authority digests equal batch records one to seven.
- Five intended refusal defects preserved, none demanded valid: disabled has enabled false; wronghost has hostname NOT-THE-REGISTERED-HOST; argv has the literal EXTRA element appended to parent_argv (dispatch_batch.py:81); cap has caps.rss_bytes "1" while the parent argv still carries 2147483648 (the intended registration/CAPRUN mismatch); missing-input lacks the frontier.json pin in file_sha256 (two frontier occurrences against three in gate-valid). All five returned 1 under NORMAL_EXIT; no gate-*.sentinel exists in the manifest except gate-valid.sentinel, as dispatch_batch.py:109-110 requires.
- Valid sentinel: gate-valid rc 0, NORMAL_EXIT, gate-valid.sentinel in the manifest; dispatch_batch.py:196 requires its POSTAUTHORIZE content.
- Dummy descendant: rc 125, status RESOURCE_CAP, resource rss, max_observed_group_rss 77946880 above the 33554432 cap; identity_checks MATCH (pid 2134, pgid 2134, start_ticks 9726), SENT signal 15, MATCH, SENT signal 9; term_sent, kill_sent, cleanup_complete and leader_reaped true; group_live_before_reap empty, zombies before reap only the leader 2134; dummy-descendant.sentinel present. Its stdout shows leader 2134, child 2136, and the child stat line with parent 1 and pgid 2134 in namespace pid:[4026531836], the namespace of every record. The leader 0 / runner 125 pairing is the intended instrument outcome.
- Cutoffs: the seven preflight records store hard_cutoff_epoch 1788988320.0 (the absolute 21:12:00 UTC deadline) with first_math null; the three mathematical records store first_math_epoch 1788987616.5901842 and hard_cutoff_epoch 1788988216.5901842, the stored first-math-plus-600 value, which is earlier than the absolute. Every returned_epoch (1788987615.27 through 1788987618.16) is below its record's cutoff, admission_margin_seconds is 15 everywhere, remaining_group_live is empty everywhere, and the batch ended 21:00:18.169100 UTC.
- Normal-exit termination fields (cleanup_complete null, term_sent, kill_sent, leader_reaped false) are the CAPRUN convention for children that exited on their own. The initial live tree caller 2045 / CAPRUN 2054 / probe 2097 is the gate-wronghost record (caller_pid 2054, telemetry pid 2097); it is a documentary summary, as declared.
- Not invented: no CPU, billing, strict no-overshoot or final outer transient-unit measurement is claimed; the metadata key-order correction was a local comparison fix, not a rerun.

## C. Seven in-process changed-object negatives: CONFIRMED

- controls.receipt.json (charged c8f955d2) lists seven cases, each with entrypoint "checker.verify IN-PROCESS, not checker.main", exception ValueError and status EXPECTED-REJECTION; semantic_controls.py:55 requires the exception type and the exact message, and :58 re-hashes the fixture after reread.
- Each reason string is the exact checker.py message on the expected path: :60 all Phi3 coefficients; :62 actual c inverse identity; :67 affine r constant; :117 literal univariate row E1/S1; :119 guard equation and both factors retained; :120 entire guard q=r*h0; :64 every univariate coefficient slot including zeros.
- All seven fixture digests (6fcaec0a, 0a793173, 3940f45c, 0184dfad, 381fcfc0, 87d9691b, 01a7c4ca) are in the terminal manifest under fixture-*.json names. The receipt binds harness cc04757e, genuine_production_receipt 0c22af83, univariate 3cfec9aa, the four code pins and execution authority add1facd (the charged semantic-controls authority, which itself pins univariate.json and univariate.full.receipt.json).
- Omitted dense slot: mutation_evidence records removed_slot_index 3 of row E1/S1 with the removed wire preserved as strings and the scope "no assumption that it is zero"; semantic_controls.py:92 pops the last slot. The fixture is 71652 bytes, the six "add constant 1" fixtures are 72604 to 72634 bytes. Sizes only; no coefficient arithmetic.
- No fresh bracket, pole, positive-precision, COVER or authority negative is inferred; positive_scope names the separate registered checker.main. Root has not replayed coefficients and neither has this gate.

## D. Qualified engineering representation acceptance: CONFIRMED (qualified)

The genuinely checked univariate artifact 3cfec9aa (72603 bytes) with receipt 0c22af83 can be admitted as the actual input representation to the already proved generic exact decision contract, under separately registered and root-authorized execution. This is an engineering representation acceptance only: not unitness, properness, a source point or exclusion, or JC2. This review authorizes no solve, matrix, worker or measurement. Coefficient bitlength and any future solve time remain unmeasured. Retained premises: 17p, 17t (selected-authority and Pi-before-bracket qualifications), 17u, root's normalized acceptance of 20:49:23 UTC, accepted backend, helper and CAPRUN correctness, and no coefficient replay by root or here.

## Smallest actual defect and impact

The new receipt emits no per-row or maximum coefficient bitlength, while the prior normalized receipt carried max_rational_bits per row. Impact: a future solve registration cannot take its size budget from this receipt and needs a separately registered measurement; no verdict in A to D depends on it, and the producer already labels it UNMEASURED.

## GAPs and limitations (documentary, non-blocking)

- No independent process observation: unit start, live cgroup tree, worker STOPPED and the 100-hash capture are the producer's and root's upstream evidence.
- The six preflight authorities and telemetries, custody.json, preflight.PASS.json and the five code files were read by grep of named fields, not WHOLE.
- Coefficient content of the artifact, the fixtures and the receipts' term counts are hash-bound only, never recounted.

## Custody table (sha256sum output, charged order)

| file | sha256 |
|---|---|
| f10-r1-univariate-runtime-execution-astra-20260909.md | d1844ddaad655187f2120f56b40923e69cb883e91cd0ca24c75c2504e14be316 |
| f10-r1-univariate-runtime-execution-astra-20260909.md.artifact.json | 9fa50db01db0ede032ab492f41ea2038604c847927fc1d0a1d6784f5a44fa414 |
| REGISTRATION.md | d32b3a05a1aeec77ebbef63bb11b161d2c1fdf6dba2a6139f312fe25fe5312fe |
| dispatch.registration.json | db06dab1f26d3d602bbc67bd7238f5c2902e6589452e41931ed7e0b6769ac774 |
| custody.json | a716d84773b341ad7e254707f384640d585ba2f4bfd56cdd34d20e3f973a7624 |
| remote-terminal.sha256 | a4e55d474a67bb535e4d8e9abf3c60c9785aa5c1ddbf37e3e9967be20e402414 |
| metadata-reconciliation.json | 3dae04164d9e0459d5efb1d206fcfed5827cae062075b8c371b5478f9b9fabeb |
| READ-SCOPE.md | 78eaeff6b5c9fda5f8e97a5c7caaa3159df0739e41329d2000ee38dccb08c04e |
| adapter.py | 11ebf4307e7cff9b7909020dcdf69cda32f689236453763ce9433fff66fd7b67 |
| checker.py | 6547063b8cf2970ce0aa1e47e5a49db31c2fd4b1e97d87690c954487500a61f0 |
| input_evidence.py | d262f3d498323b4606c51828a647b7334e8885095b099acbff41d17dd6db88b9 |
| dispatch_batch.py | 9be0c70a3ab8342a79509e039860d31b6d46401ee3aeb211e24f913b3ef69558 |
| semantic_controls.py | cc04757ed669dab0a506579079478bf71f41ba8debde0de83944ecdd7b416a90 |
| batch.PASS.json | f7460450844e97aae3a87f657e3f169ba8d50d61306451d4a57ef74549caa353 |
| preflight.PASS.json | 43fe0c187ae704697c6a33b7d3da6257a45854845d030a7f75b22f35152685af |
| univariate.full.receipt.json | 0c22af83d8846a6dbf77b424a482a0963559c9c51151539605f1c9a4f5ad0714 |
| controls.receipt.json | c8f955d2255dc222af0e2e94813b202ef95d3a5adee70b3a3cfa1aee9a6256fa |
| univariate.json | 3cfec9aaec77c3f1c15f0192aee0fa3fc2b958ca4a41261cb079ec87a71d769a |
| normalized.full.receipt.json | 062cf0c0296f67154736de1cbf7c43378f649da49bbd89f141950f58272f3aab |
| ROOT-ACCEPTANCE.json | 6451f6b42eb8867c0b46ec7aa6f55f2cd660305c5bfe1cad570a75b27fe3066f |
| f10-r1-univariate-adapter-gate-fable5-20260909.md | e169b3e42828885e38f74ef7ed53e2d022151bb9588ea44d71e45eeb3a9c44c2 |
| f10-r1-univariate-runtime-gate-fable5-20260909.md | 89f905c8fa9ce31aaae23d0c2da8d852756d099097f126d1ff27b2524e4893f5 |
| gate-disabled.authority.json | 675122d77a43f448bfa2ef772da7248c980c8127cd13c9eade73cd7568609ff0 |
| gate-disabled.telemetry.json | 2273b94fc8b7db742aa4f08c68cbec71e0b2bff3fe4399ef1142ecdc47cdbfdc |
| gate-wronghost.authority.json | b3019ae85ba3f2635e8c11559c9480a029224e05a697efdad6257c168aafe2c4 |
| gate-wronghost.telemetry.json | 15c039b85e5a44692bd330825eb29e1f4159f6cb3b40bdf13095a5ef40a3d968 |
| gate-argv.authority.json | 4db3f7f826ec45735a100e7ee3f7c1f364ad9b58422a55e067bdb1052f732687 |
| gate-argv.telemetry.json | ccbf8a4ffe9ad3aabf5cf1f60a055db22c5aea06118c0151504da6148b4c97b4 |
| gate-cap.authority.json | 4b696fd9f00d2f795df91d28e908f04709b0c5373a7b51e130584606cbfd1e81 |
| gate-cap.telemetry.json | 66fedf2dba5c88733d0e90b96a96e75b9bd6c79a0097112d6ae0341833b66efe |
| gate-missing-input.authority.json | 1276c9d470069fbe3f0f2e79c225ceedb85fdfe4147fe431673c22718ace8f44 |
| gate-missing-input.telemetry.json | eea658b1292b6839a11c7a9ce422fb417fb55e2e3fada490c48123fb8ad6933d |
| gate-valid.authority.json | 5a21ebb1ae9d72db5f2a76e7264111df27d4232f07763ac3eedaebc2db856b30 |
| gate-valid.telemetry.json | 23eed7dbbc366c9c67c8c054587eb810b65aad28ed89190c338c2000e1ffdf89 |
| dummy-descendant.authority.json | 81e18d35465347b7cc1d8f78251ac36fa5a8eb47e2709d7c6b1ed5b75d5e5916 |
| dummy-descendant.telemetry.json | f8af1f00f9a87ab752c02a745b14f607ef57527d2102968a40fa2fefb674e77e |
| adapt.authority.json | 247b0585bd13beec9c0eca11263e96546cd948a6388a543dfa565b8bc5e34cf4 |
| adapt.telemetry.json | 9e9f3a327f242d4e14396cdd3949c5d33ef81c7d5104a6dcbc1e2d92c1d984fe |
| full-check.authority.json | d971a3510f468be232d3d491257d7ff59e13b060d8c340504b0bd70517636e0c |
| full-check.telemetry.json | cce20c89044cb3b4b17ac5d0c7c4a5f262b8d3946dc09868266acde09df8f813 |
| semantic-controls.authority.json | add1facdae907081b8f51d2a22b6049ef18a5c47afdee8d57d6f8d8c619547cf |
| semantic-controls.telemetry.json | 55e42a58a27f52014a3421db21536743ade6df141007dd2c349745b880e5480b |
| dummy-descendant.stdout | 3bf4831ece5adb77a3aca95823fb95df933b630d896b8eb7bb92ce6a0b7cf722 |

## OPEN(S) RAISED

None. The bitlength omission is a bounded inventory gap for a future solve registration (cheapest test: one registered statistics child reading the frozen artifact and emitting max_rational_bits per row, seconds of wall on the accepted worker); it needs no canonical identifier and blocks nothing in this gate. No exit-price assertion is made, so no charge_basis line is authored.

## COLLISIONS

Own-only: this report and box/f10-r1-univariate-runtime-evidence-gate-fable5-20260909/ are the only paths written. The xmodel .log and .run.v2 files with this lane's name are the launcher's harness files, and box/f10-r1-univariate-runtime-evidence-gate-20260909/ (no fable5 suffix) is root's; neither was written or read. No live peer report was followed.

## Own whole-read and completion

Own whole-read at 21:28 UTC by cat -n of lines 1-112: title, status line, sections 0, A, B, C, D, smallest defect, GAPs, custody table (43 rows), OPEN(S) RAISED, COLLISIONS, this section. The 43 distinct 64-hex tokens in this report are exactly the 43 charged digests (comm against the banked sha256sum output: nothing in the report outside custody, counts equal). Every 8-hex prefix in the prose that is not a prefix of a charged digest was grepped verbatim in the charged inputs (the seven fixture digests, the code, source, interpreter and root-acceptance pins each occur in four or more charged files); the remaining tokens 20260909, 33554432 and 77946880 are the date, the registered dummy cap and the dummy's sampled peak. No placeholder, no exit-price line, no Seal, no charge_basis and no marker before this line. Verdict unchanged after the whole-read: A, B, C, D CONFIRMED; no REFUTED; no blocking GAP; no OPEN raised; own-only collision check clean. Completed before the 21:38:53 UTC stop; no execution authority, worker, solve, cap, fixture, registration or measurement was created, and no mathematical process of any size ran locally.

<!-- BODY-END -->
