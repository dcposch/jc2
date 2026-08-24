# Registration — GCD3 `(6,9)` target-translation erratum

Registered after the gauge issue was identified on 2026-08-24. This is not a
blinded preregistration. It freezes the exact transformation law and the
claimed impact before different-model review.

Inputs:

- `xmodel/gcd3-69-common-cubic-first-gate-20260824.md`, frozen SHA-256
  `f63bf74fd1013c74645f9f7fe9292db69199572b390b5b19d160c5ed13b373e8`;
- `xmodel/gcd3-69-common-cubic-first-gate-review-grok-20260824.md`, SHA-256
  `5416440bc12bb50ecebfdfa520082aa9e88a26069b43deb13bdaabfcd1690503`;
- `xmodel/gcd3-69-lower-pfaffian-successor-20260824.md`, frozen SHA-256
  `7671785519bf4e55b602f117740bd8d8571c6982a8916235407a2bb0a2263043`.

Registered question: is the high-row constant `kappa` essential modulo all
legal constant target translations, and if not, does quotienting it alter the
two-sheet lower-Pfaffian exclusion?

Allowed conclusion: a correction of gauge language and an exact covariance
statement. No cube-mismatch closure, `(6,9)` exclusion, or JC2 inference.

Replay:

```text
uv run --offline --no-project --with sympy==1.14.0 python \
  cases/gcd3_69_target_translation_erratum_20260824/check.py
```

