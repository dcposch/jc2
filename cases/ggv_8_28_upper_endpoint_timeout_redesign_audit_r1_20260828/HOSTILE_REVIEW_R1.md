# Hostile review R1: upper-endpoint timeout redesign

Date: 2026-08-28

## Verdict

`REPAIR_LAUNCH_BLOCKED`

The colon/saturation dichotomy and the decision to skip the old pure
`Delta^0,...,Delta^256` membership search on a certified proper saturation are
correct.  The four frozen packets also do show that both saturation calls and
the mutual stability comparison completed before the timeout.

The launch contract is not yet sound, for two independent material reasons.

1. A banked `OPEN_SB`, node inclusion, properness, and stability do not by
   themselves certify that the banked ideal is *the* saturation
   `I:Delta^infinity`.  The frozen source and transcript give strong provenance
   for a previous trusted `sat` computation, but the proposed replay checks are
   not a self-contained saturation certificate.  The contract must say which
   trust model it uses and bind all of its inputs, or add the missing reverse
   containment witnesses.
2. The proposed removal of `c4` is invalid for the full endpoint calculation.
   Although `c4` is absent from the node ideals, selected minors, pivot log,
   residual, and open basis, it occurs in the original 106-by-105 matrix and can
   reappear in the reconstructed right transformation and lifted kernel.  It is
   inert for the ideal-theoretic saturation stage, not established inert for
   the adjugate-kernel/endpoint stage.

No AWS action is authorized.  A repaired, hash-frozen adapter/source requires a
new hostile source review before any pilot.

## Review boundary and evidence integrity

This review used frozen evidence under `jc2/cases` only.  It did not access
`jc2-lean`, launch AWS, run Singular, or perform a heavy local computation.  It
made no canonical edit.

All five entries in `FROZEN_INPUTS.sha256` and all three entries in the original
`REPORT_MANIFEST.sha256` verified.  Each of the four terminal archives has no
duplicate member name and no absolute or `..` member path.  The relevant member
hashes reproduced directly from the sealed archives.

Every lane's archived `saturation.stdout.txt` is exactly SHA-256
`4ee63095327d80572764eb3783d0e77c7a6cf385f47cf93c1cafcea843b29418`
and contains, in order,

- a nonempty node and passing reducer fixture;
- saturation type `list`, size 1, slot 1 type `ideal`;
- node-inclusion failures zero; and
- saturation-stability failures zero;

followed by the forced-timeout `halt 1`.  Every saturation stderr is empty.  The
elapsed times and timeout flags agree with `DESIGN_AUDIT.md`.  The frozen source
places the unconditional power loop immediately after the stability marker and
before any empty/proper, closed-successor, or chart marker.  Thus the claimed
control-flow diagnosis is supported.

The original design says that per-lane residual hashes are recorded, but they
are not present in either `DESIGN_AUDIT.md` or `FROZEN_INPUTS.sha256`.  The
following directly reproduced hashes must be added to a repaired freeze along
with exact member paths:

| lane | archived residual SHA-256 | archived `reduce.sing` SHA-256 | archived `saturation.sing` SHA-256 |
|---|---|---|---|
| P | `14f53c4d7700af577ae593ff7785f06ad8fbc8c299e8da2a6511756a2afa70bb` | `55c840b21944e11b33cd0e14992506ad3af83cd44f286468ef1b7e3db714bdba` | `ab04783b930d732c06f437e3bc9cbacc43233d064f64353581973a839ebeba83` |
| C8P02 | `b66278a81de78b47c9c8c9155ba36529e15de93d636082ac08ffb004d7e6cf36` | `f4a4ac0f3518f2accf6e72d0667a9b1bbdedec1764847360d6efb3e974b30ec9` | `3198b797b28a3ff3f8513612ea90f5c31c599a4e0477d0a21f84d6eae76e09f9` |
| Q1P02 | `553f828a6310e9013f40fff0fb456c8c95f8879c889d1d8cd4b46a08905a9a48` | `77a98d195086c847c2c422f5e299b8e38aefba390a89ab171c4cba2fd0c6cfcd` | `9e125c8875f9788d3086d9e8a6f5e4a45602aa4ef0864ec7ab3f5e6152142683` |
| TRIPLE02 | `f24a4a23aa99d2864c468cce73d7a3affbb7f7baa7344af29a86060dad1a0bfb` | `28385a7044bf6b3a2d79c42738860039b687f32f13d5a43c0e67c50b247af609` | `196cb1205291c8cae0e047adf2a759cfa798fbda5a78ceefd9c18b7ec7a5f670` |

## Algebraic findings

### 1. Colon/saturation dichotomy: PASS

Let `R` be the relevant polynomial ring, `I` the node ideal, `Delta` the
selected minor, and `J=I:Delta^infinity`.  Then

`(R/I)_Delta = (R/J)_Delta`

and

`1 in J  <=>  Delta^n in I for some n >= 0`.

Consequently, `J=R` is exactly the empty-open case.  If `J` is proper then no
power of `Delta` belongs to `I`.  If in addition `J:Delta^infinity=J`, then
`Delta` is a non-zero-divisor modulo `J`; in particular its normal form is
nonzero.  Rechecking `NF_J(Delta)!=0` is a useful fail-closed redundancy.

The scheme/open identity is stronger and more precise than a point-set slogan:
the resume is computing on `D(Delta)` in `Spec(R/I)`, represented by the
saturated closure `Spec(R/J)` together with localization at `Delta`.

### 2. Pure Delta-power loop on proper J: PASS

Once equality `J=I:Delta^infinity` and properness of `J` are certified, the old
loop testing `NF_I(Delta^e)` cannot succeed for any `e`.  A finite negative
search cannot prove the required nonexistence and is logically unnecessary.
It must be unreachable on the proper branch.

This does not prohibit per-generator reverse-containment witnesses of the form
`Delta^n*b in I` for generators `b` of a proposed saturated basis.  Those
witnesses certify the origin of `J`; they are not the futile search for
`Delta^n in I`.

### 3. Archived-basis resume: REPAIR

The exact whole-archive hash, generated-script hash, open-basis hash, empty
stderr, and ordered stdout bind the banked basis to a prior execution of

`OPEN_SB=std(sat(NODE_IDEAL,Delta)[1])`.

That is sufficient only if the preregistration explicitly accepts the frozen
Singular `sat` execution as a trusted inherited computational lemma.  Rebuilding
`std(OPEN_SB)`, checking node inclusion, checking `NF(1)`/`NF(Delta)`, and
hash-matching the old stability marker checks integrity; it does not
independently prove the saturation equality.

The logical gap has a small counterexample.  In `Q[x,y]`, take `I=(x*y)` and
`Delta=x`.  The true saturation is `(y)`, but the strict proper overideal
`B=(y,x-1)` contains `I`, is stable under saturation by `x`, has nonzero
`NF_B(1)` and `NF_B(x)`, and therefore passes all of the proposed algebraic
replay predicates.  Yet `B != I:x^infinity`.

A self-contained certificate needs both directions:

- `I subset B` and `B:Delta^infinity=B`, which imply
  `I:Delta^infinity subset B`; and
- for every generator `b` of `B`, an explicit exponent and exact membership
  replay `Delta^n*b in I`, which imply `B subset I:Delta^infinity`.

Alternatively, the contract may deliberately inherit the old `sat` result,
but then it must call this a trusted archived computation rather than a newly
replayed saturation certificate and pin the exact archive, unique member paths,
ring/ordering, generated saturation script, transcript, basis, source/library
provenance, and parser policy.  A hash match must fail closed before parsing.

### 4. `c4` scalar extension: REJECT AS WRITTEN

It is valid that, because `I`, `Delta`, and the banked `OPEN_SB` are independent
of `c4`, their ideal-theoretic saturation can be computed in the smaller ring
and extended faithfully by `[c4]`.

It is not valid to omit `c4` from the full chart computation.  In every current
timeout lane, token census gives zero `c4` occurrences in `NODE_INPUT.json`,
the node standard basis, selected witness, 95-pivot log, 110-entry residual,
and open standard basis, but **30 occurrences in the archived generated
`reduce.sing`**: one in the ring declaration and 29 in original matrix entries.
Typical entries contain `-c4+(5/128)*q0`.

The 95-pivot file is only a pivot log; it does not bank the 105-by-105 right
transformation.  Reconstructing that transformation from the original matrix
can therefore reintroduce `c4` into the lifted kernel.  This is not hypothetical.
The sealed R5 TRIPLE03 terminal archive
`b31a9b145b3bb8af6b6eda1be45c0b8d1cdea3819509c7e86873eb0284c3a2e9`
has zero `c4` tokens in its node-1 pivot log and residual, but 14 in its lifted
node-1 adjugate kernel (kernel member SHA-256
`f70d83087ceda4b755f1eba9cc0aa7825a00f1a09d8bdaecfc8f724a4bfba707`).
One such entry is row 97, which is directly consumed by
`E=x14*x72+x1*x97`.

The repaired production path must retain `c4` through reconstruction of the
right transform, kernel lift, full-row replay, and endpoint pullback.  Omitting
it may be reconsidered only after an exact proof that all consumed transformed
coordinates and every endpoint coefficient descend from the smaller ring.
Treating `c4` as an element of the coefficient *field* `Q(c4)` is not an
acceptable substitute for scalar extension by `Q[c4]`, because it inverts
nonconstant polynomials in `c4`.

### 5. Complete adjugate-kernel contract: REPAIR

The mathematical route is sound only when all of the following are exact and
fail closed.

1. Reconstruct the node elimination against the banked node reducer, not the
   open reducer.  Compare all 95 pivot row/column/value records and all 110
   residual entries to their archived hashes.  Track the full right transform
   `C`; do not describe it as banked, because it is not present in R3.
2. Base-change all 110 residual entries and all 105-by-105 entries of `C` to
   the open reducer: exactly `110+11025=11135` normal forms.  Never repivot after
   this base change.
3. Replay the selected rank minor at the same banked row/column indices, require
   equality with the base-changed witness and require its normal form `Delta`
   nonzero.  Bind the inherited rank upper-bound certificate.  A nonzero rank
   `r` minor plus the upper bound is what makes the localized kernel rank exactly
   `10-r`.
4. Build all `10-r` denominator-cleared Cramer/adjugate vectors.  Check all 11
   residual rows for every vector, lift every vector through the full `C`, and
   check all 106 original rows for every vector.  Record every kernel entry.
   Because the free-coordinate block is `Delta` times the identity and `Delta`
   is inverted on the chart, these vectors then form a basis, not merely a
   collection of kernel elements.
5. Pull back every symmetric coefficient of the quadratic: every diagonal and
   every cross term.  Exact zero of all coefficients proves chart-local death;
   a nonzero coefficient remains ring-level and pending nilpotence/radical.

The exact expected counts, which must be literal gates rather than vague
"complete" markers, are:

| lanes | `r` | kernel vectors | bordered/residual identities | lifted kernel entries | full-row replays | endpoint coefficients |
|---|---:|---:|---:|---:|---:|---:|
| P, C8P02 | 9 | 1 | 11 | 105 | 106 | 1 |
| Q1P02, TRIPLE02 | 6 | 4 | 44 | 420 | 424 | 10 |

The terminal parser must require these counts, zero failures, the exact
selected-minor replay, rank provenance, `Delta` nonzero, and the exact endpoint
coefficient census.  A zero failure count without the expected positive count
is not a certificate.

### 6. Fixtures and controls: REPAIR

The proposed fixtures have the correct mathematics:

- `I=(x*y)`, `Delta=x` has saturation `(y)` and must take the proper branch
  without entering the pure-power search;
- `I=(x^3)`, `Delta=x` has unit saturation, with
  `NF(1),NF(x),NF(x^2)` nonzero and `NF(x^3)=0`.

The adapter must record dynamic operation counts, not merely print an
`EMPTY_POWER_SEARCH_ENTERED` assertion.  The proper fixture must have zero
pure-power reductions.  The empty fixture must replay exponent 3 and the three
preceding nonmemberships.  A fixed bound of 256 is not a theorem for arbitrary
production empty branches; exhaustion may only return no verdict unless an
independent bound is proved.

Add the strict-proper-overideal mutation `B=(y,x-1)` described above.  Also add
mutations/tamper tests for the ring ordering, `Delta`, exact member selection,
one residual entry, repivoting under `OPEN_SB`, deletion of one transform entry,
deletion of a `c4` matrix term, each exact count, one endpoint cross coefficient,
and both semantic plants.  Each must be rejected before any mathematical
terminal marker.

The bordered plant `NF(0+Delta)=NF(Delta)!=0` is appropriate.  The endpoint
affine plant is also safe, but `e+1` can legitimately vanish when `e=-1`; that
case must be a control no-verdict, never a mathematical classification.  A
predeclared two-shift control (`e+1`, `e+2`, at least one nonzero in
characteristic zero) avoids this innocent failure.

### 7. Exact scope: PASS, with required literal wording

The two proposed terminal claims are appropriately narrow:

- `EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY`; or
- `RING_LEVEL_ENDPOINT_NONZERO_ON_NODE1_PROPER_OPEN_PENDING_NILPOTENCE_RADICAL`.

They apply only to the named lane's node-1 open
`D(Delta) intersect Spec(R/I)`.  They do not cover `V(I,Delta)`, later recursive
nodes, another lane, an entire component, or the ambient endpoint problem.  A
timeout, hash/member/parser/source/reducer/plant/count disagreement is no
verdict.  Computing the closed successor only after archiving the open result is
the correct sequencing, and no later closed computation may erase or promote
the chart-local classification.

## Mandatory repairs before launch

1. Remove the global `c4`-omission license; keep `c4` through transform, kernel,
   full-row, plant, and endpoint calculations.
2. Choose and state one saturation trust model.  Prefer a self-contained
   two-containment certificate with per-basis-generator reverse witnesses; if
   inheriting the old `sat` run, explicitly label and fully pin that trust.
3. Add the missing residual/generated-script hashes above, exact unique member
   paths, ring order, input/source/library provenance, and the new adapter and
   source-archive hashes to the freeze.
4. Reconstruct and track the right transform under the node reducer, compare the
   pivot log and residual exactly, base-change exactly 11135 entries, and forbid
   post-base-change repivoting.
5. Gate the exact rank-dependent kernel, row, and endpoint counts in the table,
   together with rank provenance and exact selected-minor replay.
6. Strengthen proper/empty fixtures with dynamic counts, the strict proper
   overideal adversary, hash/member/ring/repivot/`c4`/count/cross-term mutations,
   and fail-closed plant handling.
7. Preserve the exact node-1-open-only classifications and no-promotion marker.
8. Freeze the repaired adapter/source and obtain a new hostile source review.

Until all eight items are satisfied, the preregistered status remains
`DESIGN_FROZEN_LAUNCH_NOT_AUTHORIZED` and the correct overall verdict is
`REPAIR_LAUNCH_BLOCKED`.
