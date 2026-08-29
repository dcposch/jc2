# V82QST3 dual-host launch record

Date: 2026-08-26

Corrected wrapper SHA-256:
`6977d0acb3d178447effe225f80f7f415a23042090092a648a8bbfbfc462a497`.

Frozen V82QST2 parent SHA-256:
`5a1054269237d9a2da5c7f5e51ae001ad59f61607ac36f2e7a9b059c972c74d5`.

Frozen source archive SHA-256:
`731eed3fdbaaf17b9f14468ca885f16bf4008f1b43bb8b276a99a530966a6d5c`.

## Box02

- endpoint: `34.203.207.55`;
- run root:
  `/home/ubuntu/runs/td6_v82qst3_f_p12_v3_box02_20260826T1131Z`;
- q2 supervisor PID: `276214`;
- q10 supervisor PID: `276215`;
- launch window: `2026-08-26T11:31Z`.

## r6a

- endpoint: `3.91.104.135`;
- run root:
  `/home/ubuntu/runs/td6_v82qst3_f_p12_v3_r6a_20260826T1133Z`;
- q2 supervisor PID: `49986`;
- q10 supervisor PID: `49987`;
- launch window: `2026-08-26T11:33Z`.

Each lane uses `TD6_PIVOT_POLICY=ascending`,
`TD6_PIVOT_SCOPE=all-staged`, a 4 GiB virtual-memory cap, and a 1,800-second
timeout.  Results require `rc=0`, exact source/hash closure, and the distinct
banner `TD6-V82QST3-F-RAW-GENUINE-P12-SOURCE PASS`.  The earlier dispatch and
reporter failures are excluded by `V82QST3_DEPLOYMENT_ERRATUM.md`.

All four endpoints returned `rc=0` with that PASS banner.  Their selected
base-result streams agree at SHA-256
`1e21693abf0f0354aa438c056b391ec2cf6aa0ecab6935b5186597c13b73dd91`,
and all four emitted certificate files are byte-identical at SHA-256
`8e892ffa914e0f93969abb9722f926486843f59cf77f5861c5ce3d3438281482`.
