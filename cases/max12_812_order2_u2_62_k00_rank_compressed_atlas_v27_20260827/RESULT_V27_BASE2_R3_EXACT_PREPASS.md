# K00 V27 BASE2 R3 exact rank recursion

Date: 2026-08-27

Lifecycle: **PRODUCER-CHECKED / INTERNAL-UNREVIEWED / SPECULATIVE /
ROLLBACK-TAGGED ON BASE4 R1 AND BASE3 R2 / NOT PROMOTED**.

This is the authorized third exact producer execution in the V27 affine rank
recursion.  It independently rechecked the prior R1/R2 equalities before
testing `B+I2(A)`.  It is not campaign evidence until hostile review, and no
canonical ledger is edited by this report.

## Exact producer result

Over

```text
R = Q[d0_1,d1_1,d2_1,d3_1,d4_1,d5_1]
```

define

```text
J2base = B+I5(A)+I4(A)+I3(A),
J1base = J2base+I2(A).
```

The fresh producer replay returns

```text
J2base is proper, dim(R/J2base)=3,
J1base is proper, dim(R/J1base)=2,
237 of 351 stored nonzero I2(A) entries have nonzero normal form mod J2base,
I2(A) is not contained in J2base,
J1base != J2base.
```

Thus the affine rank-`<=1` closed subscheme survives and is a strict
scheme-theoretic cut of the provisional rank-`<=2` base scheme.  The strict
ideal relation alone is not promoted here to a distinct-radical or explicit
exact-rank-two geometric-point claim.  A separately preregistered principal
open chart `D(m)` for one exact `2 x 2` minor is the appropriate cheap
discriminator.

## Origin correction and useful target

R3 independently reduces all 49 entries of `A`, all seven generators of `B`,
and all 351 stored nonzero `I2(A)` generators to zero at the affine origin.
The target could not be the unit ideal; the runner treated a unit result as a
hard contradiction.  Add-one origin mutations for `B[1]` and the selected
`I2(A)` entry both fired.

Consequently, mere existence of a rational point remains trivial.  A useful
point target must be nonzero/projective, lie in a source-open locus, or be
compatible with the full prior ideal `P6`.  R3 proves none of these.

## Fresh inherited checks, census, and replay

The frozen comparison and fresh stored censuses are:

| ideal | literal labels | stored nonzero |
|---|---:|---:|
| `I6(A)` | 49 | 0 |
| `I5(A)` | 441 | 90 |
| `I4(A)` | 1,225 | 594 |
| `I3(A)` | 1,225 | 813 |
| `I2(A)` | 441 | 351 |

Before computing `J1base`, the run freshly proved `B+I5(A)` proper of
dimension three, reduced every stored `I4(A)` generator to zero, rebuilt the
proper dimension-three `J3base`, reduced every stored `I3(A)` generator to
zero, and rebuilt the proper dimension-three `J2base`.  R1/R2 endpoints were
scheduling and custody inputs only.

The R3 preflight markers are

```text
K00_V27_R3_PREFLIGHT=PROPER
K00_V27_R3_DIM=2
K00_V27_R3_NGEN=541
K00_V27_R3_I2PICK=1
K00_V27_R3_I2OUTSIDE=237
```

The producer serialized a ten-generator `Graw` and `541 x 10` tracked
transform.  A fresh Singular process verified

```text
matrix(J1base)*T = matrix(Graw),
```

recomputed `std(Graw)`, and reduced every stored generator of `B`, `I5(A)`,
`I4(A)`, `I3(A)`, and `I2(A)` to zero.  It rederived properness and dimension
two from that basis.  The I2-slot deletion, transform drop/add, forced-unit,
known-proper, origin add-one, and full-literal reverse-inclusion controls all
fired.  Singular stderr and outer streams are empty.

## AWS execution and custody

The immutable source ran on audited idle AWS r6a under lane

```text
max12_812_order2_u2_62_k00_v27_r3_base2_20260827T191000Z_r6a
```

with one core at nice 5, 21,600/21,000-second wall caps, and a
402,653,184-KiB virtual-memory cap.  Singular 4.3.2 returned engine rc 0 in
3.65 seconds, maximum RSS 508,948 KiB, and zero swap.  Box02 R2/R5 and all
unrelated lanes were untouched.

- source freeze: `432b56e8b35b7b410a6c429c791ea7b4affb59d255eef2e1a35c9b03ef2e3dd8`
- immutable source archive: `598df222a1fc4db7f9b1d9ee0fe914c4c9a096bd4bdfccb72d7e4fe047b984de`
- endpoint: `bd12daa1e1e6545b8c61bef7dcb18913854146bd9c61e0b04c795fa486b4a228`
- AWS evidence manifest: `b42e23d2e12e3ef45221b387a2dd091486bfbe9b6c5bc253d240a74dc3a9f996`
- portable harvest manifest: `d440dca83973934b008fa63d324fbbf67e1e7be94e345055a821effe5ccd9b81`
- standard basis: `a840c9b69d64646e900531dddfba8ba9309336c61a83ddefb424a33d2fcdc26b`
- tracked transform: `1d045d570b0d1970bd48f694952cc956763d27cf389a4e22c7867b0e88f9f282`
- rank-2-through-6 label set:
  `f101784398a54a3f1388f97d1c26cc292ee44751fc0fc42ad800381e9127052f`

The portable manifest replays 26 harvested objects, including all 25 AWS
evidence entries plus the evidence manifest itself.

## Review target and stop

A hostile reviewer should reconstruct the full rank-2 census, independently
rederive R1/R2, replay all 351 `I2(A)` normal forms, verify the tracked basis
identity and Buchberger/standard-basis result, and reproduce the origin and
mutation controls.  Any later geometric chart should select and freeze one
specific minor with nonzero normal form and test `J2base+(z*m-1)` exactly.

No `I1(A)`, projectivization, principal-open chart, saturation, or full-`P6`
job was launched.  R3 asserts no nonzero/projective or rational exact-rank-two
point, source-open/full-`P6` point, grade-seven compatibility, lift, jet, arc,
closure incidence, counterexample, or JC2 result.  It consumes no sampled
pencil claim.

## Additive hostile-review correction: `size()` versus `ncols()`

Added 2026-08-27 after the different-model Fable 5 review.  The original
producer report bytes above had SHA-256
`5f9700c7e67eaa5255ef642ff4e784983d71da9f8c5394d6cb01245c9c0a873d`;
they are retained verbatim as historical producer output.  The frozen
endpoint JSON and tracked evidence are also left immutable.  This section
supersedes only the numerical `I2OUTSIDE=237` census and the producer-tier
refusal to draw the now-reviewed dimension corollary.

The hostile review
`xmodel/k00-v27-base4-base3-base2-hostile-review-fable5-20260827.md`
(SHA-256
`738f46030a73fea2a06a8e3139ed9aa5e2001b72a579e459357af81f6801647a`)
independently reconstructed all 351 nonzero literal `2 x 2` determinants,
verified the producer and independent characteristic-zero bases, and found

```text
291 of 351 stored nonzero I2(A) determinants outside J2base,
60 of 351 inside J2base.
```

The frozen producer loop bounded the slot scan by `size(I2MOD)=291`, although
`ncols(I2MOD)=441` retains all literal slots including zeros.  It therefore
inspected only the first 291 slots and counted 237 nonzeros.  An exact
read-only Singular 4.3.2 diagnostic on the audited producing r6a and the
reviewer's independent rational-arithmetic reduction both reproduce the
correct 291/60 census.  All future per-slot scans are required to use
`ncols()`, while `size()` remains appropriate only for an explicitly named
nonzero-entry census.

The ideal-theoretic R3 endpoint is unchanged and confirmed: `J1base` is
proper of affine dimension two, `J2base` is proper of affine dimension three,
and `J1base` strictly contains `J2base`.  After hostile review, the dimension
drop additionally proves that their radicals are distinct.  Consequently
the set difference of `V(J2base)` and `V(J1base)` is nonempty over an
algebraic closure, and the
six-variable coefficient base has a nonconstructive rank-exact-two
geometric stratum.  This supplies no explicit point, no rational point, and
no source-open, full-`P6`, grade-seven, later-grade, lift, jet, arc, closure,
counterexample, or JC2 conclusion.
