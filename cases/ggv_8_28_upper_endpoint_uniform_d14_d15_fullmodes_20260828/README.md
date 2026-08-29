# Uniform full-mode cascade through D15

This packet exactly continues the uniform branch-P A-adic cascade through the
first forced negative-mode birth.

```text
Delta7=F7-T/2-Q*Z/8-R*V/16.
```

D14 first forces `A|Delta7`; its only remaining pole is `c14/A`, so `c14=0`.
The checker explicitly guards against a tempting false successor shortcut:
at D15 the `c14` predecessor-mixed and same-row pieces cancel exactly.
Writing `Delta7=A*U`, D15 then forces `A|U`, while
`c8` survives.  Hence

```text
F7=T/2+Q*Z/8+R*V/16+A^2*Y,
c14=0.
```

Because the raw G13--G15 windows have positive lower degree, the packet also
freezes the exact live scalar compatibilities C13, C14, C15.  They use only
the gauge-invariant combination `H0=c8/2+3*F8(0)/4`; no gauge or carrier is
normalized.

Replay:

```text
python3 -B verify_uniform_d14_d15.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```

Only standard-library exact arithmetic is used.  The result is necessary
field-point prefix information, not endpoint emptiness or a JC2 proof.
