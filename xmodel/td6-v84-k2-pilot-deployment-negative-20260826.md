# TD6 V84 bounded K2 pilot: deployment-negative report

Verdict: **HARNESS FAILURE; NO MATHEMATICAL VERDICT**.

The dual-AWS bounded pilot reached the exact frozen transport checkpoint
(`3470/3602`, free dimension `132`) on both hosts, then failed before constructing
the source RHS or any quadratic previous/pole table. The inherited
`v81.propagate_q` route passes a symbolic `E[C,V,U]` value through the old scalar
source constructor, ending in `fractions.Fraction` with `TypeError: argument
should be a string or a Rational instance`.

Both hosts used source archive SHA-256
`91b09bca835473dc081d07c53e0f6df977069812a7c1927c80757d011ba20fe3`.
The raw output SHAs are:

- r6d stdout `741cf1da8ffc17c7182854f8281f0698258778e4e28130e0eeb7dc850ad0a864`,
  stderr `a0f8564364481601a7a2a2fb1e037d3d5875de7766c0670bba6a4edb9dd0fb1a`;
- Box03 stdout `bd73270ee6e7ce537ecc964a88c73f519352319915cde4e58475819a21fb03ef`,
  stderr `38f32c3ab848065ecf701bffdfe0a37c3f9c3d15086c99bf57dab3154c6750dc`.

This package licenses no K2 claim. The smallest repair is a typed source-RHS
propagator over the symbolic center ring, with the archived block and controls
rerun independently on both AWS hosts.

Evidence package:
`cases/td6_c1_c2_c3_qdead_previous_pole_k2_pilot_v84_aws_20260826/`.
