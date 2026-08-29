# D43 exact a00pp sparse rows v2: implementation report

**Status:** repaired, review-frozen, AWS-unregistered, and non-launchable.
No D43 jet was built, no exact row was emitted, no solve was attempted, and
no AWS action was taken while preparing this revision.

## Revision provenance

This is a new v2 packet.  It does not silently upgrade the v1 packet in
`cases/d43_exact_sparse_rows_20260828/`.  The v1 source seal is
`9b851ede56986fe3154cf962f336fda6185fb7a4a00d07888c93e9b78a06848d`.
V2 responds to the independent hostile review
`xmodel/d43-exact-sparse-rows-hostile-review-gpt56-20260828.md`, SHA-256
`283d47df4f55a0e83fbf1758cc8ac71fbe5ee8549dcdb1c3a6838c8ccc42b21e`,
and the three sealed audits with prefixes `456edb3a`, `69db2cd8`, and
`e1b99600`.

The v1 packet remains useful evidence for the registry, support, target,
selector, and custody designs.  Its uncollapsed coefficient engine is not an
`a00pp` producer and is superseded for launch purposes.

## Launch-critical mathematical repair

The expensive jet arithmetic now takes place in

```text
K0[W1,W2],
K0 = Q[zeta42,r3,A1,A2,h]/
     (Phi42, r3^2-3, A1^3-3-r3, A2^3-3+r3, 2h^2-3).
```

The canonical quotient basis has shape `12*2*3*3*2=432`.  It is described
as a quotient algebra, not globally asserted to be a field.

For every A-orbit source coefficient, the producer applies the literal
substitution

```text
HW1 = h*W1,   HW2 = h*W2
```

before any series or jet multiplication.  The resulting coefficient has
only the five K0 exponents and the two polynomial W exponents.  There is no
representation slot for an independent HW sign after this point.

The fixed B orbits require special handling because an individual source
factor contains `EB`, while only the completed orbit block eliminates it.
V2 verifies the literal raw B/GB source orbits, refuses any attempt to pass a
surviving EB through the a00pp adapter, and replaces the B contribution
before the A/B join by

```text
((1 + eta*t^20)^7 - 3/2)^6     for f,
((1 + eta*t^20)^7 - 3/2)^9     for g.
```

Thus no expensive multiplication takes place in the old 6048-dimensional
selector basis.  Light exact tests compare both the A-side collapsed engine
and the EB-free B blocks with post-collapse raw computations at a safe D21
prefix.

The literal 326-coordinate complement remains pinned before construction.
This includes all `uf/vf`, B-tail coordinates, and the six level-74 PIN42
tails.  The retained set is exactly the common 22-coordinate modular support.
`Xf_alpha=Xg_beta=0`; therefore the scoped P4P1 value correction vanishes.
The producer adds `+42` once at `(eta,slot)=(0,20)`.

## Exact band-20 and full-row contract

The D21 reference bank is hash-checked before unpickling, restricted by
literal source names, and collapsed through the same a00pp adapter.  A real
D43 pilot must equal this collapsed ten-row band exactly in K0[W1,W2].  The
gate also constructs three required mutations and proves that their semantic
digests differ from the correct reference:

* `HW1 -> -h*W1` with the HW2 sign unchanged;
* `HW2 -> -h*W2` with the HW1 sign unchanged;
* omission of the inhomogeneous `+42`.

Only a passing gate permits continuation.  The same process and immutable
manifest then emit all 19 bands and merge their exact disjoint cover of the
184 canonical targets.  The real run must prove exactly 155 rows are the zero
polynomial, with the 29 live rows distributed `20:10, 30:9, 40:10` and tail
degree at most two.  It also replays all 184 emitted rows at both registered
modular points.  Any mismatch terminates without a positive verdict.

## Correct E5/E6 bridge

W1 and W2 remain solve coordinates; v2 makes no degree-16 or degree-6912
residue-field claim.  No solver is included in this packet.

For the displayed E5/E6 subsystem, the exact localized projection is

```text
E = (9+5*r3)*A1*W1^4 + (9-5*r3)*A2*W2^4 = 0,
W1*W2*uW12 - 1 = 0.
```

One product-unit row makes both W coordinates units.  V2 constructs

```text
HM  = -C*a1^2*A1*W1^4 / (4*(a1-4)),
s1F = (2^8/7^16)*HM,
C   = 243*(7^12/2^6)^3*(2*r3)^4,
```

and mechanically proves in the 432-basis algebra that the first literal E5
row becomes zero, the second becomes a unit multiple of E, and the literal
E6 cube row becomes zero.  Both registered modular points pass the complete
E, one-unit, reconstructed-E5, reconstructed-E6, HM-unit, and s1F-unit replay.

This bridge is sufficient for the existential projection of the displayed
E5/E6/unit subsystem.  It says nothing about other quotient, tower, or
template equations.  Full residue-A/template membership remains a separate
claim tier.

## One immutable conditional AWS pipeline

V2 uses one manifest for the entire run:

```text
live preflight
  -> concurrent independently capped f and g builders
  -> matching side-receipt/pair-custody gate
  -> exact collapsed-D21 band-20 gate
  -> same-manifest conditional 19-band emission and 184 merge
  -> atomic terminal receipt and final artifact inventory.
```

The conditional gate is inside `selected_rows_v2.py`; shell ordering alone
cannot authorize continuation.  Every compute command consumes the same
hash-bound passing preflight receipt.  The two side receipts must match on
manifest, preflight, operational-source root, registry, support, and
coefficient-algebra digests.

The registered manifest authenticates an exact operational source-list hash.
That list binds the producer, preflight, wrapper, v1 registry dependency,
coefficient adapter, exact inputs, and hostile-review sources.  A future
`REGISTERED.json` additionally binds the manifest hash and source-list hash.
The preflight obtains the live EC2 identity document and real instance tag
through IMDSv2 and compares account, region, instance ID/type, hostname, tag,
CPU count, zero swap, memory, disk, and process state.  Duplicate jobs in the
same run directory are no longer exempt from conflict detection.

The artifact inventory is written atomically only after the terminal markers
and `FINAL_RECEIPT.json`; it excludes only itself and therefore cannot hash a
partially written copy of itself.

The review manifest deliberately has empty AWS identity and tag fields.  All
compute entry points reject it.  After a different-agent hostile PASS, create
a fresh manifest and source seal for an idle isolated host; do not edit the
review manifest in place.

## Claim tiers

1. A successful run establishes an exact support-specialized a00pp emitter
   and exact inventory for the finite 184-row raw-J truncation.
2. A later exact solve of raw J plus E and one product-unit row, followed by
   mandatory literal E5/E6 reconstruction replay, establishes only the
   displayed finite E5/E6/unit extension.
3. Full residue-A/template membership requires every other applicable
   quotient/tower/tie equation.
4. NF equivalence, all-depth compatibility, a Keller map, and a JC2
   counterexample remain separate and unproved.

## Remaining blockers

The launch-critical implementation is present, but no real D43 v2 output
exists.  Launch remains blocked on:

* a fresh hostile-review PASS of this v2 seal;
* fresh immutable registration on an idle isolated AWS host with the required
  memory, tag-enabled IMDSv2, zero swap, and copied source root; and
* creation of that operational host-specific manifest and seal.

Even after emission succeeds, exact point existence remains open because this
packet intentionally contains no solver.
