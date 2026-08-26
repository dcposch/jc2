# Loaded order-four lemniscatic target V1: fail-closed record

Date: 2026-08-26

Status: **NO VERDICT.  V1 is an immutable failed control.**

The registered Box03 lane
`max12_812_order4_lemniscatic_param_v1_20260826T021600Z_box03` ended with
shell return code zero, but Singular's `paraPlaneCurve` failed inside
`paraplanecurves.lib::deltaLocMod` with `exponent must be non-negative`.
Consequently `RP1` and `PARA` were undefined and
`PARAMETRIZATION_TEST=0`.  Singular continued after those errors, so the
later token `PARAMETERIZATION_AND_BRANCH_FACTORIZATION=PASS` is fallthrough
and has no evidentiary value.

The retrieved immutable outputs are in `aws_v1_failed/`.  Their principal
hashes are:

```text
stdout  06c4b9a3ed8a66ed0e3d25b5d49667b13aaefbfa6d056e3f70d68f40622128aa
stderr  a91df5c1c6cebb240f6cc01a3d5c37149dc028ed1c4ed237d11ed37ef7c9df5a
meta    76801aac6040cff7109c641417383dab3af482bdb5cb2371707463b5bc59ae44
```

The maximum resident set was `554672 KiB`, elapsed time `3:21.75`, and
there was no swap.  Nothing from V1 is promoted or consumed.  V2 avoids the
failing library route and checks a separately derived rational map by direct
cleared-denominator polynomial identities.
