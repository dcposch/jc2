# Exact-Q endpoint tangent certificate

Status: **`TANGENT-OBSTRUCTED-AT-THIS-POINT`**

The frozen producer `probe_tangent.py` was run unchanged on the authorized
AWS host with `--exact-output TANGENT_CERTIFICATE.json`.  It returned an
exact left-dual contradiction witness over `Q`; the complete immutable job
packet is in `aws_exact_q_r1/`.

Key replay commands from this directory are:

```bash
sha256sum -c SOURCE.sha256
sha256sum -c EVIDENCE.sha256
```

`LOCAL_POSTCHECK.json` records a standard-library, read-only replay of all
24 remote evidence-manifest entries, all 18 frozen-source entries, the exact
dual pattern, modular cross-checks, terminal marker, zero-swap record, and
zero-member final census.

See `REPORT.md` for the mathematical certificate and its scope firewall.

