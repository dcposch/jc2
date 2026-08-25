# TD6 q2-beta `U=0` canonical-digest custody repair (V69)

Status: **producer-exact reporter/custody repair; no mathematical scope
change; hostile review of the underlying `U=0` theorem remains pending.**

The V33 raw `U=0` producer hashed `repr(BetaPoly)` values whose coefficients
were `E3` objects.  `E3` had no `__repr__`, so these strings contained
process-specific object addresses.  Fresh Box02 and Box03 replays therefore
agreed on every exact mathematical marker but disagreed on six printed
digests.  The old frozen bytes remain immutable and are not used as
cross-host deterministic hashes.

V69 copies the V33 producer and changes only its digest serializer.  Every
`E3` value is encoded by its 18 exact `Rat3` coordinates; every numerator and
denominator is encoded by sorted monomial/coefficient tuples.  It rejects any
serialization containing a Python object address.

Independent AWS runs on Box02 and Box03 both returned rc 0 and byte-identical
stdout SHA256

```text
9726fb09a9279c7c19c507eeafc5b541bfd2d89e9d34a7e972b73badde042734.
```

They reproduce, without changing algebra, transport rank `3470/3602`, first
rank `36/132`, the dependent original row `('X-2',14)`, degree-zero
compatibility gcd, denominator one, and original-row replay.  Thus the already
frozen narrow result remains: the raw `U=0` divisor is empty for every `beta`
inside the fixed source-typed A3 q2 family.

The direct-q-prime omission run also returns the same unit residual, while its
source support drops from 14 rows to 1.  This is an exact source-path control:
the `U=0` contradiction occurs early enough that direct q-prime is not
load-bearing.  It does not broaden the source family.

Two initial main launch tags accidentally passed one empty positional
argument, failed before mathematics with rc 1, and are preserved under
`evidence/operator-failure-*`.  Their corrected successors are the only main
evidence used above.

Source archive SHA256:
`9e89808cca9d24ec5182466b40e53d612317a4f03c70053a9c490e957ab51f38`.
V69 source-manifest SHA256:
`fe39baefa6bcec511646397b5060ee8a4d555d17c2310b40b0035ff5931900ac`.

Run `python3 verify.py` for a lightweight archive, custody, marker, negative
control, and scope replay.  This package makes no claim about `U!=0`, other
TD6 moduli, whole TD6, SP-2, landing, or JC2.
