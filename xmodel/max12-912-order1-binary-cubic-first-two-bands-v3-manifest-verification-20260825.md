# Independent V3 manifest verification

Scope: custody only; no mathematical replay and no CAS.

On the local orchestration host, after `FREEZE.v3.sha256` was written and
before the final V3 hostile review was launched, the command

```text
LC_ALL=C LANG=C shasum -a 256 -c \
  cases/max12_912_order1_binary_cubic_bands_aws_20260825/MANIFEST.postrun.v3.sha256
```

returned exit code zero, printed exactly 102 `OK` records, and printed no
warning or malformed line.  The checked manifest SHA-256 is
`38466426e3a0b113a4cbd71b447d9a44b01482bcd3e3acea4879cad96589a8e3`;
the custody-root file `FREEZE.v3.sha256` has SHA-256
`b4374cb2395cadb1c4755432dd7087dd19f44e4ac1e21265054a38aa429354d5`.

The immutable V1/V2 manifests and roots are diagnostics only.  This verifier
does not broaden the producer's first-two-band or finite-SAT scope.

