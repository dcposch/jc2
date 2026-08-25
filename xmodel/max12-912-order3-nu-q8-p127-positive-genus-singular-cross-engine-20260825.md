# Independent Singular cross-engine certificate for the Q8 point count

Date: 2026-08-25  
Status: **PRODUCER-EXACT STANDALONE SOFTWARE CONTROL; hostile review optional**

## 1. Result

A complete, independent Singular 4.3.2 census over

```text
F_(127^2)=F_127[a]/(a^2-a+3)
```

recomputes for the pinned candidate plane curve `H(w,v)=0`:

```text
w fibres                           16129
affine F_(127^2)-points            16174
singular affine points                 6
smooth affine points               16168
#P1(F_(127^2))                     16130
```

Thus the earlier python-FLINT point count has now been reproduced by a
different polynomial engine.  Consuming the separately reviewed geometric
integrality of `H`, the already-CONFIRMED implication `g(Htilde)>0` remains
valid with cross-engine evidence.

This certificate is strictly about the pinned plane curve.  It proves no
source-component membership, characteristic-zero specialization, trajectory
exclusion, maximum-twelve theorem, or JC2 statement by itself.

## 2. Independent implementation

`generate_singular.py` checks the exact candidate SHA-256

```text
9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce
```

and only transcribes its sparse coefficient table into Singular syntax.
Singular performs all mathematical operations.  For each
`w in F_(127^2)` it forms

```text
h(v)=H(w,v),
h_v(v),
h_w(v),
R_w=gcd(h, v^16129-v),
S_w=gcd(R_w,h_v,h_w).
```

Binary modular powering computes `v^16129 mod h` using Singular standard
reduction; Singular's polynomial gcd supplies `R_w,S_w`.  The recorded
counts are

```text
total=deg(R_w), singular=deg(S_w), smooth=total-singular.
```

The quadratic modulus is the same irreducible modulus independently checked
by the hostile point-count review.  Since `v^16129-v` is squarefree, the gcd
counts distinct rational roots.  Both partials are required for the singular
filter.

The source hashes are

```text
generate_singular.py   9b4333f6beac564aa40e53e3e88c91fe67465a5bb3c477669532faadf5978266
run_remote.sh          fd4bbbcefa6abd97ff62e60e8c21c5fd7399fcaaed5a9f32743ea03843f5ad73
aggregate_singular.py  84d1ba633f9bfc24ece8919684533768e242ea11c15cd4b416c5499cb46386c9
run_aggregate_remote   c4bcedc17fc5f7a946debcb9385f6fc4905f496afbe4eca5b565b4fbcb05dfbe
```

No python-FLINT call occurs in this case.  The Python generator and aggregate
are exact transcription/custody programs; the finite-field polynomial
arithmetic is Singular's.

## 3. Controls and fail-closed repair

The first control source computed the four frozen fibres correctly:

```text
index 0:    8 / 7 / 1
index 39:   4 / 3 / 1
index 71:   3 / 3 / 0
index 128:  2 / 2 / 0
```

but ended with the invalid Singular spelling `exit(0)`.  Singular reported
`` `exit(0)` is undefined `` despite process status zero, and the wrapper's
error-token gate rejected the run.  It is frozen only as a harness-negative
control.

V2 changed only those exit spellings to `exit;`.  The same four controls then
passed in 1.34 seconds at 12,800 KiB RSS:

```text
tag      q8_p127_fq2_singular_controls_r6a_v2
input    8dc2c6f4d174a5d7f8db52e1831cf486532f6f9bc26fa2962b790cfb25fe2a1d
stdout   8a0406a2c9f6fcd45fe93a8e55d35abb00d12708fea701d289d4fb1812574989
stderr   fbfdfe8a0ce7b74218d9971bcd0455e748bf931b64d4f09eab8713cf4b563895
run.meta e138340609bf94a7c9ac0994bf8baf63b1158ea04ed91af2210267e789d3fdf3
```

A 16-fibre pilot independently agreed with every frozen per-fibre FLINT row:

```text
tag      q8_p127_fq2_singular_shard0000_0016_r6a_v1
stdout   42600046cf5e2de04789eeee13c17845ba9cdc2a08f883db513a7f96ea650d2c
run.meta c9cffa8e3993a54ab5f24b1da06f15e85e08e421bb2f427c9c7ba66749443e05
```

Only after both controls passed was the full census launched.

## 4. Full AWS census and aggregate

AWS r6a host `ip-172-30-0-34` ran 16 disjoint one-thread shards

```text
q8_p127_fq2_singular_full_r6a_v1_i00 ... i15
```

covering `[0,16129)` exactly.  Every generated Singular source embeds the
corresponding frozen FLINT `per_w` rows as acceptance values, but Singular
recomputes every gcd independently.  All 16 lanes ended with
`SINGULAR_FQ2_SHARD_PASS`, Singular rc zero, no error tokens, and exact
source/output hashes.  Maximum observed lane RSS was 13,864 KiB and maximum
wall time was 54.32 seconds.

The AWS-only fail-closed aggregate verifies:

- exactly 16 expected lane directories;
- exact disjoint interval coverage and 16,129 records;
- generator, runner, candidate, input, stdout, and stderr hashes;
- one terminal marker per lane, rc zero, and `/usr/bin/time` exit zero;
- absence of parser/error/mismatch tokens;
- `total=smooth+singular` on every fibre;
- the final `16174 / 16168 / 6` totals.

Its endpoint is

```text
tag         q8_p127_fq2_singular_aggregate_r6a_v1
result.json 31fa7f5502bf174ab3e339d0026a27806d86250db9d367f03607f23044887544
stderr.log  5a4f1002399faeda5a163ceda7ea4bc21d7de575bfce9a6e05fe1ec07c5b20ea
run.meta    7e0c628619bbd2216f322f2bdd2087f96409a442f02c30307886d8844716f76c
```

The aggregate completed rc zero and prints `"status": "PASS"`.

## 5. Scope and interpretation

This removes the original producer's disclosed single-engine-family
residual: python-FLINT and Singular now agree on every fibre and both
derivative filters.  The two earlier FLINT hosts remain partitioned replay,
while this is a genuinely different implementation.

The result is a supporting certificate for the already hostile-CONFIRMED
standalone plane-curve genus theorem.  It does not widen the selected-Q8
composition's hypotheses or bypass its separate whole-source/proper-model
review.
