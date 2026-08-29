# Uniform full-mode cascade through D17

This packet exactly continues the frozen uniform branch-P characteristic
cascade through the births and first successor of the forced `c16` mode.
With

```text
B = F8-Y/2-T*Z/8-Q*V/16-R^2/4,
C = F9-Q*R/2-T*V/16-Y*Z/8,
```

the polynomial `G16` window requires

```text
3*B^2+4*c8*B+8*c16 = 8*A^2*M.
```

Thus `c16` is unique if the relation exists, but it need not vanish.  The
literal raw-source replay contains determinant-zero points with `c16=3/8`
and `c16=-3/8`.  In the additive-`F8` gauge-invariant coordinates

```text
Bhat=B+2*c8/3,       J16=c16-c8^2/6,
```

the same equation is `(3/8)*Bhat^2+J16=A^2*M`.  No gauge slice or square-root
branch is chosen.

The checker also freezes the causal firewall: if a free `c16/A^2` were
illegally retained, its D17 predecessor-mixed and same-row pieces would be
`+6*c16*A'/A` and `-6*c16*A'/A`.  They cancel.  Therefore D17 does not kill
`c16`; D16 polynomiality is what fixes it.

At D17 the full linked `c16` block is retained.  Exact cancellation using the
D16 relation leaves the successor condition

```text
K17_uniform=(3*B+2*c8)*C-2*M = 4*A^2*N.
```

This is only a structural uniform-ancestor candidate for the cutoff-three
`K` relation; the packet does not assert a specialization map.  It also
freezes the four new `G16/G17` lower-window equations, carries the live
`H0,C13,C14,C15` core, and retains all nine characteristic modes.

Replay:

```text
python3 -B verify_uniform_d16_d17.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```

Only Python standard-library exact rational arithmetic is used.  This is
necessary field-point prefix information, not endpoint emptiness or a JC2
proof.
