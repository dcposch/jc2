# AWS registration: V24R3 independent-prime preflight

- host: Box02, `ip-172-30-0-186` (`x2idn.32xlarge`)
- public endpoint at launch: `34.203.207.55`
- tag: `max12_812_order2_u2_62_k00_v24r3_multiprime_20260827T141134Z_box02`
- immutable source: `/home/ubuntu/jobs/max12_812_order2_u2_62_k00_v24r3_multiprime_20260827T141134Z_box02_source`
- job: `/home/ubuntu/jobs/max12_812_order2_u2_62_k00_v24r3_multiprime_20260827T141134Z_box02`
- outer PID: `367659`
- start: `2026-08-27T14:13:09Z`
- fields: `F_32003`, `F_65519`, `F_65537`
- resources: three independent one-core Singular processes, each inheriting
  a 64-GiB virtual-memory cap; 600-second inner and 900-second outer wall caps
- source-freeze SHA256:
  `6d362fc7b964753b00db978461694cc55b7fa9157ded79060ef86fec62f24a13`
- scope: theorem-ineligible modular properness preflight only; no exact-Q,
  compatibility, stratum, jet, arc, closure, order-two, maximum-twelve, or
  JC2 conclusion

At launch all six frozen inputs replayed, the three Singular processes were
separate and single-core, and the host retained approximately 1.9 TiB
available memory with zero swap.  The protected V24R2 exact-Q namespace and
all unrelated jobs are untouched.
