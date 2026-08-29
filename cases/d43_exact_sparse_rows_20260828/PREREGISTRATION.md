# D43 exact sparse source-row pilot preregistration

Status: **review-frozen, deliberately unregistered, and not launchable**.

The initially considered box01 lane was withdrawn before sealing because the
monolithic `build_tails43.py` process is still active there.  The manifest has
empty hostname, instance, product, tag, and CPU registration fields.  The
preflight requires all of them to be nonempty and mutually equal to the live
host/environment/registration record, so this review packet necessarily
refuses execution.

After hostile review, choose an idle isolated host (box02 is the natural
high-memory candidate if the source packet can be copied immutably), create a
fresh operational manifest with a new tag and exact host identity, write the
matching `records/REGISTERED.json`, and reseal every operational source.  Do
not edit this review manifest in place.

The operational preflight will check the immutable manifest digest in its
registration, Linux, Amazon EC2 vendor/product/instance/hostname, exact CPU
count, at least 512 GiB available RAM, at least 100 GiB free disk, zero swap,
all source hashes, and the absence of another heavy algebra process.

## Mathematical object

The producer rebuilds the exact pure-y D43 jets from source formulas after
pinning all 326 source-coordinate complements to literal zero.  The 22
retained source coordinates are exactly the support common to both
floor-passing modular points.  In particular all `uf`/`vf`, B-side tails, and
the six PIN42 level-74 variables are zero.  The B orbits themselves are not
deleted: their fixed `eta_B` constant factors remain in the exact f/g source
products.  The x-side coordinates are frozen at `alpha=beta=0`, so the row-42
`P4P1` sidecar is zero.  The inhomogeneous `+42` term is appended at `(eta,
slot)=(0,20)`.

`W1,W2` remain free exact polynomial coordinates in `R_ext`.  Their deferred
E5 quartic relations are **not** inferred from residues and are **not**
imposed by this pilot.  Any later solver must add and mechanically verify the
exact E5 relations.

## Pilot and fanout gate

The pilot builds hash-receipted sparse f/g checkpoints, emits only the ten
band-20 canonical targets by complement-indexed products, and requires exact
semantic equality with the independently committed D21 source bank.  Dict
insertion order is excluded from all semantic hashes.

The pilot manifest has `fanout_after_pilot=false`.  Every non-band-20 shard
and the 184-row merge therefore fail closed.  After hostile review of a
successful pilot, a new immutable manifest may authorize the 19 disjoint band
shards.  The merge requires exactly 19 shard receipts, identical source and
registry custody, no duplicate target, and exact coverage of the frozen
184-target registry.

## Full-checkpoint lane

The alternative sharder records the available final f checkpoint by content
hash, but its final g entry is null because box01 has not produced the GB42
and GB21 cumulative checkpoints.  Its status is
`BLOCKED_MISSING_FINAL_G_GB42_AND_GB21_CHECKPOINTS`; attempting to use it is a
hard error.  The observed `jet_g_03_G0p2.pkl` is explicitly recorded only as
an incomplete checkpoint and is never accepted as the final g input.

## Claim boundary

A successful pilot certifies an exact source-row emitter and one exact
band-regression only.  It is not an exact D43 point, a normal-form/source
equivalence, an all-depth construction, or a JC2 counterexample.
