# Source/hash review — `j!=0`-localized V2 compiler

Date: 2026-08-25  
Verdict: **SOURCE-CONFIRMED FOR AWS EMISSION; NO SATURATION VERDICT**

## Frozen inputs

```text
840a12e29386d37801f986e39273c3fb34f5542019cc1da7043ee1730dcb31f2
  cases/max12_812_order2_u2_62_strict_rees_20260825/compile_rees.py
3958fd2d3eea3ed7d164659b675a8b35d298004da9f8a3df76dc6d7400add060
  cases/max12_812_order2_u2_62_strict_rees_20260825/compile_rees_v2.py
5aa954cbe6396ef5de353519eaf10aed567aec55964bb197c9eb1576b131c10b
  xmodel/max12-812-order2-u2-62-strict-rees-client-erratum-v2-20260825.md
6de652872b1fb694bec5de24498fa32af016d1a235b660ffe5b648cd557dd2c8
  xmodel/max12-812-order2-u2-62-strict-rees-v1-j-saturation-failure-20260825.md
```

## Review

The wrapper imports only the pinned V1 compiler and fails if either its hash
or the erratum hash changes.  It delegates all Faber and seven-tail
reconstruction to that frozen source.  Its patched emitter requires the V1
saturation block to occur exactly once and replaces exactly

```text
SR=sat(KT,rho); K=SR[1];
```

by

```text
SR=sat(KT,rho); KR=SR[1];
SJ=sat(KR,j);  K=SJ[1];
```

leaving every `Psi` line, target exponent, boundary, irrelevant ideal, and
endpoint test unchanged.  Post-emission checks require all three principal
localizations in order, require the `j`-saturation marker, preserve the
known all-tail hash
`6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`,
and fail if the separate lower-load DS optimization appears.  The output is
renamed `strict_rees_v2.sing` and its hash is recorded in `result.json`.

The AWS-only guard remains load-bearing because `module.main()` invokes the
frozen compiler's Linux/Amazon-EC2/registered-tag check.  The runner adds the
same 128-GiB cap and hardened shared lane used by V1.

This review licenses AWS emission and syntax/execution testing of V2.  It is
not independent reconstruction of the tails, does not anticipate a unit or
nonunit endpoint, and says nothing about Taylor realization, order-two
closure, or JC2.
