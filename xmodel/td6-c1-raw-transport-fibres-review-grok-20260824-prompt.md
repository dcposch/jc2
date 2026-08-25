# Hostile different-model review — TD6 c1 raw transport-exceptional fibres

Work in `/Users/dc/code/math/jc2`.  This review is charged against the frozen
raw-fibre package, not against a generic parameterization.  Read in full:

- `xmodel/td6-c1-raw-transport-fibres-gate-20260824.md`;
- every file named by
  `cases/td6_c1_raw_transport_fibres_20260824/MANIFEST.sha256`;
- the reviewed TD6 whole-qB pencil, adjoint, and centering-tangent packages;
- the generic c1 transport package only to identify why `C=0,3` were its
  transport-exceptional fibres, never as evidence for their raw ranks.

Charged hashes are:

```text
producer report  24ecd47e3c9e2045d72f0b2c70cfa3257c5bf21e4142dcb0ae2c704f58b865e1
MANIFEST         7cfe741bc6344a5eba2da60bac679b685f98f3b6c4d63d73fbdd6533dc6eda8c
FREEZE           7cfe741bc6344a5eba2da60bac679b685f98f3b6c4d63d73fbdd6533dc6eda8c
canonical stdout b48210ae9010015185982174192a46dd7190f28909957036711bb4341894e1b7
```

Verify hashes and the registered replay, but use it only as regression.
Independently reconstruct and attack every load-bearing claim:

1. Rebuild the registered normalized TD6 section and the original 3,602-
   column transport systems after specializing `C=0` and `C=3`, before any
   generic elimination.  Reproduce or refute transport rank `3470/3602`, no
   dependent-row incompatibility, 132 parameters, and the two adaptive-minor
   digests.  Check that no singular generic pivot list is evaluated.
2. On each independently rebuilt chart, regenerate the first centered band
   from source and verify rank `38/132`, consistency, and the exact adaptive
   echelon.  Attack row-order and pivot-choice dependence.
3. Reconstruct the current `t^12` polynomial before first-band reduction.
   Verify it is genuinely quadratic with `2824` terms at `C=0` and `2885`
   at `C=3`, including the documented raw-polynomial digests.
4. Independently reduce the genuine polynomial modulo the first-band ideal.
   Verify the remainder is exactly `-k/50` at both fibres.  Then replay the
   lifted identities against the *original* 38 first rows, checking all
   coefficients, 28 nonzero source rows, multiplier term counts `1423` and
   `1515`, and full relation digests.  A reduced-row-only certificate is not
   enough.
5. In the exact degree-18 field, independently verify the defining
   polynomial, the displayed inverse of `k`, and hence that `-k/50` is a
   nonzero unit over every field extension in scope.
6. Check that `C=0,3` are precisely the two exceptional fibres of the named
   generic *transport* echelon, while distinguishing later generic
   first-stage exceptional roots.  Enforce the refusal boundary: this closes
   only these two raw fibres in one fixed normalized section, not the full c1
   line, other center/boundary/F1/pole moduli, SP-2, a terminal class, or JC2.

Use exact arithmetic and genuinely independent reconstruction; producer PASS
strings and the canonical stdout are regressions only.  Keep scratch outside
tracked paths.  Do not edit producer, case, canonical, prompt/log/run,
coordination, ladder, or predecessor files.  Do not launch AWS.  Write exactly:

`xmodel/td6-c1-raw-transport-fibres-review-grok-20260824.md`

Give one overall and per-item verdict from `CONFIRMED`, `GAP`, or `REFUTED`,
checked hashes, the smallest failing identity or missing hypothesis, precise
promotion language, and precise quarantine language.

