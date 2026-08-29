# TD6 V89K1 dual-AWS launch record

Date: 2026-08-26

## V1

Both hosts used archive SHA256
`cdaca6c7faddb077c4d02eb089f4e6ac610d605714325778bc672d576a53359d`
and stopped with rc=1 before emitting a result because the diagnostic
misstated the unequal `U` clearing powers after the `F=0` substitution.
See `DEPLOYMENT_ERRATUM.md`.  V1 is not mathematical evidence.

## V2

Both hosts used archive SHA256
`9a23e8b31eef977fc1ca952dfbcfacdb10f27a93b9b4ef80b6b1a3fdc78e4e49`.

- Box02 tag `td6_v89k1_k_b3_mod_f_box02_20260826T171100Z`, root
  `/home/ubuntu/runs/td6_v89k1_k_b3_mod_f_v2_box02_20260826T171100Z`;
- r6d tag `td6_v89k1_k_b3_mod_f_r6d_20260826T171100Z`, root
  `/home/ubuntu/runs/td6_v89k1_k_b3_mod_f_v2_r6d_20260826T171100Z`.

Both returned rc=0 in 0.10 seconds with zero swap.  Maximum RSS was 29,136
KiB on Box02 and 29,520 KiB on r6d.  Mathematical stdout and the exact-result
file are byte-identical.
