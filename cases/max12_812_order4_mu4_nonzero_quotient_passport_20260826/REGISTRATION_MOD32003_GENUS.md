# AWS registration: mod-32003 complete quotient genera

Date: 2026-08-26

Status: preregistered; characteristic-32003 support only.

- tag:
  `max12_812_order4_mu4_nonzero_quotient_genus_mod32003_v1_20260826T005500Z_box02`;
- Box02 / `i-010201a5da47795c4` / `34.203.207.55`, expected hostname
  `ip-172-30-0-186`;
- same-named remote directory under `/home/ubuntu/jobs/`;
- parent corrected-V2 mod-32003 stdout SHA-256:
  `e9d81781230f85f69c716909724b9005e953492b2c9cd694b38adb93180edd68`;
- input: `mod32003_quotient_genus_v1.sing` (hash recorded before launch);
- runner SHA-256:
  `01dc64151226ef8dbcc7c1683e485a5dd16b8c4daae7d33ecdae7f061ce65b48`;
- timeout `3600 s`, cap `67108864 KiB`.

The job computes complete geometric genera, not affine arithmetic genera, for
the residual plane `P(q,v)`, deck plane `P(q,y^4)`, and normalized-slice
plane `P(s^2/t^3,t^8)` over `F_32003`.  It also prints the residual torus
singularity ideal.  The result is not a characteristic-zero genus verdict
until the exact-Q plane polynomial is proved integral/irreducible and its
good reduction is matched exactly.  Missing genus sentinels or any library
error is **NO VERDICT**.
