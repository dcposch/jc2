# D5G review-independent raw-global determinant

This case compiles the literal generic raw determinant coefficients
`D0..D22`, then gives exact certificates

```text
D22=H*Q22+R22,
D22=M(Y22)+rM22.
```

Generated artifacts are compact canonical JSON.  Replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B compile_d5g.py --check \
  ../ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json \
  DIRECT_DETERMINANT.json D22_CERTIFICATE.json RESULT.json
```

The D4R1 local naturality path remains dependency-locked.  This case makes
no Keller, target, or face-exclusion claim.
