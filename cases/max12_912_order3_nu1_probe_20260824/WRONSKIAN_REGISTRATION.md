# Registration — `k=0` order-three spectral Wronskian ladder

Date: `2026-08-24`  
Status: `PRODUCER-EXACT ALGEBRAIC IDENTITY / REVIEW REQUIRED`

Registered claim:

```text
B=3*f*g_z-4*g*f_z
 =sum_(l=1)^8 3*(l+12)/(9-l)*r_l*F_(9-l)'.
```

On the order-three character fibre this becomes

```text
B=(15/2)*mu*F6'+18*nu*F3'+60*r8.
```

In particular, for `mu=0,nu!=0`,

```text
B=54*nu*z^2+18*nu*p+60*r8.
```

Replay from the repository root:

```sh
shasum -a 256 -c cases/max12_912_order3_nu1_probe_20260824/WRONSKIAN_MANIFEST.sha256
python3 cases/max12_912_order3_nu1_probe_20260824/wronskian_ladder.py \
  | diff -u cases/max12_912_order3_nu1_probe_20260824/wronskian_ladder.json -
```

The registration excludes component, genus, trajectory, Taylor-boundary,
maximum-twelve, counterexample, and JC2 conclusions. The separate
`generate.py` standard-basis probe is not part of this identity freeze.
