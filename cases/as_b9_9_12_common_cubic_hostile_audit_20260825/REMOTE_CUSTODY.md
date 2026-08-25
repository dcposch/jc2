# Remote custody

- AWS host: Box02, `ip-172-30-0-186` (`x2idn.32xlarge`).
- Remote job directory:
  `/home/ubuntu/jobs/as_b9_common_cubic_hostile_audit_20260825T1725Z`.
- Audit-only corrected emitter: `2026-08-25T17:22:27Z` to
  `2026-08-25T17:22:32Z`, rc 0.
- Independent reconstruction and literal replay: `2026-08-25T17:31:16Z`
  to `2026-08-25T17:31:21Z`, rc 0, 28,920 KiB maximum RSS.
- Source-independent witness verifier: `2026-08-25T17:32:18Z`, rc 0,
  14,592 KiB maximum RSS.

The generic solvers launched against the audit-only corrected SMT were
terminated after the independent literal witness made them unnecessary.
Their interrupted outputs are not frozen and are not cited as evidence.
