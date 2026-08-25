# Evidence and custody notes

- Box02 job: `/home/ubuntu/jobs/as_b9_9_12_quadratic_3p11_20260825T1800Z_box02`.
- Box03 job: `/home/ubuntu/jobs/as_b9_9_12_quadratic_3p11_20260825T1800Z_box03`.
- Both jobs returned `rc=0` from the same source closure and produced the
  same `result.json` bytes.
- Source-closure manifest SHA-256 on both hosts:
  `b0d8da1b2d313d0c1f9afe8372fbb0a09d5d96e92c64b0e1fc70e8df54d20425`.
- Parent normalized linear-window result SHA-256:
  `8c4060e8e48978492e115955af167e11149d6ba18be83ee3c82121834d617667`.
- Producer source SHA-256:
  `7a51c772b0df8c900eddd84e4388fe5f3d47e2bb755ef837d17d7cc28debde58`.
- Dual-host equality is a deployment/custody check only.  Independent
  source/compiler review remains required for promotion.
