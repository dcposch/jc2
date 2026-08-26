# AWS launch metadata

Registered before either compiler GO sentinel at `2026-08-26T03:27:42Z`.
Local placement audit found no campaign-owned local Singular, Sage, msolve,
Lean, exact compiler, or other heavy worker; no local PID was stopped.

- Box03 `98.80.65.144`: remote job root
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_control2_q2_syzygy_lift_v2_20260826T032200Z_box03_A`,
  run directory beneath `cases/` of the package name, worker PID `150218`,
  encoding A/global `dp`, compiler cap 4 GiB / 900 s, solver cap 8 GiB /
  1800 s, nice 10, state `WAITING_COMPILE`.
- r6d `100.26.198.153`: remote job root
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_control2_q2_syzygy_lift_v2_20260826T032200Z_r6d_B`,
  run directory beneath `cases/` of the package name, worker PID `217964`,
  encoding B/`(lp(2),dp(8))`, compiler cap 4 GiB / 900 s, solver cap 8 GiB /
  1800 s, nice 10, state `WAITING_COMPILE`.

Frozen source-closure manifest SHA-256:

```text
f6938514c9d050e45f46a3a37b331d1ef8904d32939acdfc902e21757e81b2d5
```

The launcher's displayed shell `$!` was accidentally expanded by the local
shell and printed `0`; the worker-owned `worker.metadata` files and remote
process tree independently record the actual PIDs above.  No GO sentinel was
present during that check.

Both AWS compilers then returned rc 0 with empty stderr.  Before solve GO,
the chosen compiled inputs were independently pinned as follows:

- Box03 A/global-dp input SHA-256
  `cafa685fc2219b81180eee892487dd56d5597eaca6dd40dc499bfe46b7b2831e`.
- r6d B/LPDP input SHA-256
  `12bc04b6f876974a95d539fc75063800c2de13bd4cf99791f9f1d11455354c2a`.

The tag-dependent compiler stdout and Singular source hashes differ, as
preregistered, but both compilers emitted the identical canonical corrected
polynomial SHA `ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b`
and corrected coefficient SHA
`ac7d43b5e71444f5cd487328f7aff6b2312d198649a2c0b001d4a13ef006956c`.
The first bad component SHA is
`4493daefdd98d9158f556735b8adf50978ec5b8e61295c58fd79e65d1e907b28`.
Both report the canonical correction `(g1,g2,g3,...,g8)=(1/12,-1/9,0,...,0)`
and sample minimum 80, uniquely `la^20`.
