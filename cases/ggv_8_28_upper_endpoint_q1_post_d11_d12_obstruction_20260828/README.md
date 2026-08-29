# D12 obstruction for the frozen q1 D11 survivor

This exact standard-library packet proves that the rational proper-divisor
prefix frozen in the predecessor case has no extension to `D12` in the
authoritative raw windows.

Replay:

```bash
cd cases/ggv_8_28_upper_endpoint_q1_post_d11_d12_obstruction_20260828
python3 -B verify_q1_d12_obstruction.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```

The characteristic quotient/remainder and an independent direct raw-row
rank/dual certificate are both included.  This kills only the one frozen
prefix; it is not a universal q1, endpoint, or JC2 theorem.
