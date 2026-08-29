# Unit-root endpoint transport certificate

This packet certifies the new local bridge from a simple root `alpha` with
`V0(alpha) != 0` to the reviewed fixed `F1=A^2` characteristic endpoint
cascade.

It checks:

- the exact `t=epsilon^2*s` Newton identity and automatic leading square;
- coefficientwise `V0` normalization for the fractional-power recurrence
  and every scheduled mode through weight 22;
- the load-bearing mode-pole orders;
- the endpoint valuation and optional `c22*A^-5` kernel;
- two breaking mutations;
- the independent Bezout/root-local claim for the known D12 mixed-root
  fixture.

Replay:

```bash
python3 -B verify_unit_root_transport.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```

The scope is the characteristic-zero field-point endpoint system under the
reviewed reduced branch-P prefix, complete mode schedule, regular raw
`G0..G21`, and absent raw `G22`.  It does not prove a raw-normal-form landing,
the deep `A|V0` stratum, or JC2.
