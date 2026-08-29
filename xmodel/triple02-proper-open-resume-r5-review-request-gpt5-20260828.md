# Independent review request: TRIPLE02 proper-open resume R5

Date: 2026-08-28

Producer status: `R5_CUSTODY_REPAIRED_LAUNCH_NOT_AUTHORIZED`

Please independently hostile-review the sealed R5 packet rooted at
`cases/ggv_8_28_upper_endpoint_triple02_proper_open_resume_r1_20260828`.
AWS launch is blocked until a fresh review returns PASS and the coordinator
separately issues `GO`.

## Exact review roots

- R5 source archive:
  `custody/ggv_triple02_proper_open_resume_r5_SOURCE.tar.gz`, SHA-256
  `60f83a1d4e2eae0f974027059bc1cb1e6de8c3fc687b6cce4af4072ab18c2310`.
- Archive-external launcher: `aws_launch_preflight.sh`, SHA-256
  `4b5b4c641a40f12a7b873adeafd1afee156f046e5207b8e1cc7b1aa574a504a4`.
- Launch manifest: `LAUNCH_MANIFEST.sha256`, SHA-256
  `513051d9807c61d27fb92b18bff14c00b1b438201fbe3e4ac92882e6b319ceda`.
- Repair report: `PREFLIGHT_REPORT.md`, SHA-256
  `2cbb4f3af845dfb3a8402779c2bec425de5c7fb7e6112b6c81b0ef371f215676`.
- Report manifest: `REPORT_MANIFEST.sha256`, SHA-256
  `2b82cafa902e22221fd4edab74c5e1d8c4dacf9adc9675e9049c9b4dbe622c7f`.
- Named custody fixture result:
  `preflight/R5_CUSTODY_SELFCHECK.json`, SHA-256
  `7d5e13f1c5874081cd8c13f83d528efbe18c7fcd30691346734aede3ce711509`.
- Superseded R4 repair charge:
  `xmodel/triple02-proper-open-resume-r4-hostile-review-gpt56-20260828.md`,
  SHA-256
  `3e55f6f334c67d4ced74651dd612f174d2ea0cde205698a98e92c2c19a7ef7b9`.

## Required hostile targets

Confirm fail-closed behavior for all four R4 blockers:

1. sticky observed-swap and whole-timeout latches are mandatory terminal
   inputs and cannot be cleared by late clean state;
2. final `cgroup.procs` is read and parsed by contents, including explicit
   collected-unit handling;
3. launcher TERM/KILL/reap is bounded and bound to exact PID/start-time/UID;
4. terminal-manifest generation status, exact census/hash replay, fresh safe
   extraction, and embedded replay all precede terminal promotion.

Also attack late systemd, preflight, launcher-reap, worker-return, scope,
resource, orphan, archive-install, and decision failures.  Verify that the
public terminal rename remains the last successful action and every failure
downgrades to `CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT`.

The mathematical Singular payload must remain SHA-256
`f5050f1204f3d990be64f18c5776eb7204f2587273a64a533e6d56d37b49132a`.
The only mathematical scope is TRIPLE02 node 1 on `D(Delta)`; no complement,
whole-component, geometric-survivor, or ambient endpoint claim is authorized.

No AWS execution is requested for this source review.  Report explicit
`PASS`, `REPAIR`, or `FAIL` and seal the review with a SHA-256 sidecar.
