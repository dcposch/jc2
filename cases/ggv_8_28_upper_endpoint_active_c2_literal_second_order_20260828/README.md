# Relaxed second-order exact-Q screen

Status: **`SECOND_ORDER_RELAXED_INCONSISTENT_AT_THIS_POINT`**

The frozen V2 producer was run unchanged on audited idle AWS Box03 with
`--exact-output`.  It included the nonlinear reduced-prefix Hessian, formed
all 153 symmetric quadratic columns from the exact 17-dimensional tangent
kernel, relaxed their Veronese relations, and certified that even this
enlarged 510-by-461 system is inconsistent over `Q`.

The complete immutable job packet is in `aws_exact_q_r1/`.  From this
directory, replay the custody hashes with:

```bash
sha256sum -c SOURCE.sha256
sha256sum -c EVIDENCE.sha256
```

`LOCAL_POSTCHECK.json` records a read-only standard-library replay of all 26
remote evidence entries, all 70 frozen source entries, the exact dual
pattern, modular checks, terminal marker, zero-swap record, and empty final
census.  See `REPORT.md` for the mathematical implication and strict scope.

