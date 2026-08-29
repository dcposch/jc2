# V3 fail-closed result

Date: 2026-08-26 19:04Z

Verdict: **COMPILER-ONLY FAILURE; NO SINGULAR RUN AND NO MATHEMATICAL
RESULT.**

Both frozen AWS lanes (`p=32003` on Box02 and `p=65521` on Box03) verified
the V3 and upstream V2 freeze manifests, generated the byte-identical-size
streaming source, found all intended 581 dependency statements, and then
stopped in the compiler.  The final assertion tested for the broad substring
`if (subst(TPhi,`, which also occurs in the unrelated rho deck-invariance
control.  Thus it raised

```text
RuntimeError: ('dependency rewrite census', 581)
```

before writing the accelerated Singular input or starting Singular.  The
successor must narrow only that final postcondition, retain the exact
per-name count of seven and total count 581, and remain navigation-only.

The common source archive SHA-256 was
`39b0e374555cc61bab6539a54f4fc439e634bc4fdce9e03ae04c95d02fabf2a8`.
The harvested immutable failure records are in `aws_p32003_v3_failclosed/`
and `aws_p65521_v3_failclosed/`; their per-file hashes are frozen in
`FAILCLOSED_EVIDENCE.sha256`.
