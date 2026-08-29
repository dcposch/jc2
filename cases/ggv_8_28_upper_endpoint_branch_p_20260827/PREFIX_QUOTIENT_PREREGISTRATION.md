# Preregistration: reviewed-prefix exact quotient

Date: 2026-08-27

The authoritative object remains the 303-variable, 513-generator literal raw
coefficient ideal with SHA-256
`ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0`.
This acceleration uses only the already-reviewed `D4,D5,D6` prefix.  It is an
ideal equality over `Q`, not a specialization, localization, saturation, or
reduced-support replacement.

Retain the following original raw coefficient generators:

```text
D4:  X-degrees 0,...,19
D5:  X-degrees 0,...,19
D6:  X-degrees 0,...,17
D7,...,D22: every serialized coefficient generator
```

Thus 466 original raw generators are retained and exactly 47 are omitted:
`D4[20..35]`, `D5[20..34]`, and `D6[18..33]`.  The selected current-slot
matrices in rows 4, 5, and 6 have ranks 20, 20, and 18 respectively.  Exact
constant-`Q` pivoting makes them a monic acyclic graph for 58 raw `G` slots;
the remaining dimensions are precisely the arbitrary `F4,F5,F6` coordinates
and the reviewed `c4,c6` modes.

The compiler must serialize a polynomial cofactor vector for every omitted
generator, expressing it in the retained original raw generators.  An
independent verifier must multiply out and replay all 47 identities over
`Q`.  A zero normal form without these cofactor bytes is not evidence of
equivalence.  No `D7` compatibility, later raw slot, polynomial mode, or one
of the 18 affine `D22=1` generators may be removed.  The endpoint-transfer
identity is not used.

The generated Singular input is an exact-`Q` decision script only.  No run is
authorized by this compilation.  The held fallback may launch only after the
current exact lanes fail and a fresh Box03 audit shows zero swap and at least
approximately 150 GiB of headroom beyond its requested cap.  Its hard limits
are one core, a single global two-hour wall cap, and 128 GiB VM.  A future
proper-ideal result is promotable
only after a complete rational 303-coordinate assignment passes the literal
raw replay.  A future unit result only licenses a fresh tracked certificate;
its cofactors must be composed or zero-padded into the 513 authoritative raw
generators and replay exactly.  Resource custody and the prohibition on
canonical edits, commits, pushes, and `jc2-lean` access remain unchanged.
