# Preregistration: row-shard compiler census repair V7

Date: 2026-08-26

Status: **COMPILER-ONLY SUCCESSOR; SAME NAVIGATION-ONLY V6 ROW-SHARD
IMPLEMENTATION. NO MATHEMATICAL VERDICT.**

Frozen V6 stopped in Python before Singular because its last assertion
counted both the unique row formula assignment `TPhi=...` and the deliberate
release assignment `TPhi=0;`.  V7 imports every frozen V6 helper and changes
only that assertion to exclude the literal release line, matching the
already-correct V6 row splitter.  It retains the V6 transcript token,
validators, seven-way AWS runner semantics, derivative bound, certificate
recombination, and all scope fences.

V7 must pass a compiler-only source-generation test before AWS engine launch,
then agree at two primes with sequential V5 and reviewed V2.  The V6 failed
compiler runs remain no-verdict evidence.
