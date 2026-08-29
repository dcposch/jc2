# TD6 V89H3 dual-AWS launch record

Date: 2026-08-26

V1 through V3 stopped at fail-closed environment-sentinel checks before
source import or algebra.  Their immutable traces and the exact corrections
are recorded in `DEPLOYMENT_ERRATUM.md`; none is mathematical evidence.

V4 used source archive SHA256
`a1c6eb18828897ac16b5af2c433553e54bfbe5318d4cae559d0b35aa9a465494`.

- Box02 tag `td6_v89h3_q14_pivot_box02_20260826T171100Z`, root
  `/home/ubuntu/runs/td6_v89h3_q14_pivot_v4_box02_20260826T171100Z`;
- r6d tag `td6_v89h3_q14_pivot_r6d_20260826T171100Z`, root
  `/home/ubuntu/runs/td6_v89h3_q14_pivot_v4_r6d_20260826T171100Z`.

Both returned rc=0 with zero swap.  Wall times were 1:59.88 and 2:00.85;
maximum RSS was 297,596 KiB and 296,920 KiB respectively.  Mathematical
stdout and all three emitted exact artifacts are byte-identical.
