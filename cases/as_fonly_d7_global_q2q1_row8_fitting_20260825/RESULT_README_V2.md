# Global row-8 emitter V2 result

Both source-pinned Box02 emitter runs completed with return code zero.

| formula | row8 equation | SMT2 SHA-256 | bytes | max RSS | emitter status |
|---|---|---|---:|---:|---|
| discriminator | included | `ab0c36835bf251f98ff8bb1ae1274e4d4c1949fcd949109b5696e5f2b662c331` | 12,992,696 | 168,040 KiB | `unknown` at the 1-ms smoke timeout |
| positive control | omitted | `f50697f7f4abd5ca8e7608ca405bc7990ac1359e600762bbb04ef04c3022f706` | 12,989,879 | 168,720 KiB | `unknown` at the 1-ms smoke timeout |

The parent formula SHA before appending the scalar is
`78509aee04c39200918e611049034231939902ac6b374ac97c092a6453bc13b8`.
Both runs emit the identical exact scalar expression, SHA-256
`33343694994fb329b7c632ecd5c717ecf70a9f0e3bbe679f14c0e696cf8bcec1`.
The V2 source and runner hashes are respectively
`50f79b48a9560bc93ec7f17049e2a2f4fc017bf7549b9140291e70513168a51c`
and
`12e4f6d953700f0d3ed457e634e8c7f97d4c35ca896e6a28153f5d23985d7f5a`.

AWS custody: Box02,
`/home/ubuntu/jobs/as_global_q2q1_row8_fitting_20260825T1348Z_v2/`.

The formulas are currently being raced with paired Boolector and Z3 endpoints.
`SAT` requires direct replay through the literal integer source; `UNSAT` is
diagnostic until an independently checkable proof or algebraic certificate is
available.  No Q4/Q3 existence, global exclusion, all-depth, counterexample,
or JC2 claim is made.
