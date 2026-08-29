# Preregistration: exact square-tail witness discovery

Date: 2026-08-27

This is a positive-discovery specialization of the authoritative literal raw
ideal with SHA-256
`ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0`.
It is not a negative cover and cannot support an emptiness claim.

Set all 303 raw parameters of weight below 11 to zero.  In particular
`Z=T=0`, and through weight ten the fixed data are the exact square family

```text
U=H+t/2,       F=U^2,       G=U^3.
```

Retain every raw `F_n,G_n` slot of weight at least 11.  Since any product of
two retained perturbations has weight at least 22, the complete literal
system `D4=...=D21=0` restricts to an exact rational linear system.  Compute
its full nullspace without deleting any prefix coefficient equation, then
substitute that serialized linear map into all 18 literal row-22 coefficient
generators, including the unique affine target `-1`.

The compiler must pin the raw JSON, record every retained variable and full
nullspace vector, verify all 495 prefix generators symbolically, and emit the
complete 18-generator tail ideal.  Exact nonlinear solving runs only on
audited Box03 in a fresh immutable namespace, with a one-hour wall cap,
16-GiB VM cap, one core, and zero swap.  A proper result is promotable only
after extracting a rational parameter point, expanding it to all 303 raw
coordinates (zeros included), and passing `verify_endpoint.py --witness`.
A unit result excludes only this square-tail specialization and is
non-evidence for the full charged fixture.
