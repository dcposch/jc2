# AWS registration: exact top-boundary local branches V3

Date: 2026-08-26

Status: completed diagnostic; its two-distinct-slope hypothesis failed.

- tag:
  `max12_812_order4_mu4_nonzero_toplocal_v3_20260826T013000Z_box03`;
- host: Box03 / `i-0ece0b9a3b4a7512f` / `98.80.65.144`, expected
  hostname `ip-172-30-0-249`;
- same-named directory under `/home/ubuntu/jobs/`;
- timeout `1800 s`; virtual-memory cap `16777216 KiB`;
- exact input SHA-256:
  `3747a07cbd371ead5b0f9403f37715cade35e12fea874495c36bdf0e00d5bb7f`.

The client verifies the exact identities
`Htop = constant*(9261q-484)*(27q+4)^6` and
`L2 = constant*Q2*(27q+4)^3`, then computes the discriminant of the
weighted initial quadratic at `q=-4/27`.  A nonzero discriminant means two
smooth local branches `w=c_i*(q+4/27)^3+...` with distinct `c_i`, contact
order three and local delta three.  It also independently evaluates the
left transverse coefficient at `v=81/22`.  The predecessor V2 stdout is
charged only for its exact four ordinary torus nodes and printed boundary
factors; genus is a successor hand theorem, not a CAS sentinel.

The lane ran on Box03 at `2026-08-26T01:27:55Z`, rc 0, maximum RSS
12248 KiB.  Retrieved stdout SHA-256 is
`b7aa07121bc761acd8dd0a3342bb8f5321da8e38c4068859edb23e0b8d0094ff`.
Both factor identities passed, with

```text
Htop=(-1/1982464)(9261q-484)(27q+4)^6,
L2=(81/30976)(120771q^2+189396q+30976)(27q+4)^3.
```

The weighted local coefficients at `q=-4/27` are
`A=-29/209088`, `B=7047/484`, `C=-46235367/121`; their discriminant is
zero.  Thus `EXACT_TOP_LOCAL_V3_CERTIFICATE=0` correctly rejected the
preregistered two-distinct-slope interpretation.  The independent left
transverse coefficient is `123466498884/14641 != 0`, proving the repeated
left face gives one smooth tangency.  V4/V5, not V3, resolve the repeated
top branch.
