# q1 post-D9 proper-divisor survivor through D11

This is an exact, provisional, standard-library replay of the first two
rows after the q1 D9 repair.  It proves that D10/D11 do **not** repair the
next proper-divisor square defect: a rational point with `W=B` survives all
determinant rows `D0,...,D11` in the authoritative raw coefficient windows.

Replay:

```bash
cd cases/ggv_8_28_upper_endpoint_q1_post_d9_d11_survivor_20260828
python3 -B verify_q1_post_d9_d11.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```

The generic frozen raw input is used only for its literal coefficient-slot
windows.  Its unrelated leading-row fixture is not imported.  This packet
does not claim a D12+ lift, endpoint solution, GGV landing, counterexample,
or result on JC2.
