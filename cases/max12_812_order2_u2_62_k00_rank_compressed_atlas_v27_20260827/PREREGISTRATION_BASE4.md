# Preregistration: K00 V27 BASE4 exact rank-purity prepass

Date: 2026-08-27

Lifecycle before launch: **FROZEN DESIGN / UNRUN / NOT EVIDENCE**.

## Registered question

Work exactly in

```text
R = Q[d0_1,d1_1,d2_1,d3_1,d4_1,d5_1].
```

Consume the byte-frozen V26 matrix `A` and the literal base ideal

```text
B = (G2_row1,G2_row2,G2_row3,G2_row4,G2_row5,G2_row7,F10).
```

V26R1F proved and different-model review confirmed that

```text
J4base = B + I5(A)
```

is proper of exact affine dimension three.  The first V27 job decides

```text
J3base = B + I5(A) + I4(A).
```

All literal `5 x 5` and `4 x 4` minors are included.  The `I5(A)` summand is
retained literally even though determinantal containment makes the displayed
ideal equivalent to `B+I4(A)`.

- `J3base=(1)` means that no geometric rank-`<=3` point survives in
  `V(J4base)`, so the promoted rank-`<=4` base scheme is rank-pure of rank
  exactly four.
- `J3base` proper means that the rank-`<=3` closed subscheme survives.  It
  does not classify its exact rank; V27 must recurse to `I3(A)` before any
  lower-rank purity claim.
- A cap, warning, missing byte, source mismatch, or failed replay is
  `NO_VERDICT` or failure, never an algebraic endpoint.

## Frozen dependencies

The source freeze pins these exact bytes before algebra:

```text
d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501  ATLAS_EXACT_POLYNOMIALS.json
5de20da0d3501db668fca38db3c678ba4719745e3df7b32d0d0a8d2867e4da32  COMPILED_SOURCE.sha256
f1a6f1fc988fc77816daaab13b294b1321de7e476d2891cf7fbfa2e033868d97  V26 compiler RESULT.json
86742147085332881b3c44ba041172ac5a032d656df3992ceff5da7d0a5b46dc  V26R1F producer report
f455c7b2177eb260df2ebfa97f174381591792683c80fdeb779f1184f6e6d70e  V26R1F endpoint RESULT.json
6790ec5c06c6bbdca5e08ddf0194a88b5b68d85b6f74070477ae12ba85701865  Fable5 V26R1F hostile review
f9d2afcb01c1ad1161783d0ff51d9d47d1a6aa5831b508936072f0c9170012b9  Sol Ultra V24R6R1 cross-audit
d9e653150d14bc2791e366c2e425de5790f0f4390ab5790469bb9fe6ef4b644b  Opus5 V24R6R1 promotion cross-audit
a1b1865ab5d491b04d3876a72328893b6f25e7f867ace3b9c44f80ff551100af  V27 successor design
```

The algebra reconstructs every consumed minor from the frozen `A`; the V26
minor census is a comparison control, not a substitute.  A source-label
artifact retains every row/column subset for ranks 4, 5, and 6.  The literal
expected censuses are `1225/594` total/nonzero for `I4(A)`, `441/90` for
`I5(A)`, and `49/0` for `I6(A)`.

## Exact algorithm and replay

1. Refuse every host except Amazon EC2 Linux and require a nonempty registered
   lane tag.
2. Verify the expected source-archive hash, the expected hash of the source
   freeze itself, every freeze entry, and the pinned endpoint metadata.
3. Rebuild `A`, `B`, `I6(A)`, `I5(A)`, and `I4(A)` in a six-variable exact-Q
   Singular ring.  Recheck all minor censuses entrywise.
4. Freshly recompute `std(B+I5(A))`, require properness and dimension three,
   then decide `J3base` with `slimgb`.
5. For a unit endpoint, serialize exact coefficients `C` satisfying
   `matrix(J3base)*C=1`; replay the identity entrywise in a second Singular
   process.
6. For a proper endpoint, serialize `Graw` and a tracked transform `T` with
   `matrix(J3base)*T=matrix(Graw)`.  In a second process recompute
   `G=std(Graw)`, reduce every literal generator of `B`, `I5(A)`, and `I4(A)`
   to zero, and derive properness and dimension only from this fresh basis.
7. Treat `lift`/`liftstd` only as certificate proposers.  Empty stdout,
   nonempty Singular stderr, any `?`, `// **`, warning, failed marker,
   missing/empty certificate byte, timeout, memory cap, nonzero swap, or
   manifest mismatch fails closed.

## Mutation and negative controls

- deleting the preregistered first nonzero literal `I4(A)` entry must change
  that polynomial slot;
- deleting and adding one nonzero unit-certificate or tracked-transform entry
  must break the exact serialized identity;
- adjoining `1` must force the unit ideal, while `(d0_1)` must remain proper;
- omitting all `I4(A)` generators recovers the independently recomputed
  proper, dimension-three V26R1F control ideal;
- full literal-minor reverse reduction prevents a compacted Singular ideal
  from silently standing in for an unverified subset.

The V27 `b`-sign and restored forbidden-`k6_0` controls are explicitly not
consumed by BASE4, which contains neither `b` nor the prior/newest-variable
compiler.  They remain mandatory before LOW-KILL or any full-`P6` V27 job.
The two-class rank-five representative-replacement control likewise belongs
to MAX5CLASS and is not claimed here.

## AWS registration and resource envelope

Registered host: idle AWS `r6a` (`r6i.16xlarge`), selected after the
coordinator's live fleet audit in preference to stacking work beside Box02's
protected R2 and R5 jobs.  Those Box02 jobs must not be signaled, stopped,
reniced, rewritten, or otherwise altered.  BASE4 uses one process/core at
positive nice level with:

```text
outer wall cap       = 21600 seconds
per-Singular cap     = 21000 seconds
virtual-memory cap   = 402653184 KiB (384 GiB)
required swap count  = 0
```

The immutable extracted source tree is read-only.  The fresh job directory
records lane, hostname, EC2 identity, source/archive hashes, Singular version,
local capacity/process snapshot, the protected-Box02 placement declaration,
start/end UTC, wall telemetry, maximum RSS, swap count, validation state, and
a relative-path evidence manifest.

## Allowed producer outcomes

```text
PASS_V27_BASE4_EXACT_RANK4_PURE_PRODUCER_UNREVIEWED
PASS_V27_BASE4_EXACT_RANK_LE3_SURVIVES_PRODUCER_UNREVIEWED
RESOURCE_CAP_NO_VERDICT
DEPENDENCY_SOURCE_REPLAY_OR_ENGINE_FAILURE
```

Any exact PASS remains producer-unreviewed and speculative until an
independent different-model hostile review replays the frozen endpoint.  This
job does not edit a canonical ledger.

## Firewall

BASE4 decides only the intrinsic six-variable coefficient-base rank
filtration.  It asserts no rational point, full-`P6` point, grade-seven
compatibility, nilpotent lift, later grade, jet, arc, source reachability,
closure incidence, counterexample, or JC2 conclusion.
