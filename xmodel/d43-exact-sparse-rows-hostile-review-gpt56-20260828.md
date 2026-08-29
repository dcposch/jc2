# D43 exact sparse row packet: independent hostile review

**UTC:** 2026-08-28T20:03Z  
**Packet:** `cases/d43_exact_sparse_rows_20260828/`  
**Verdict:** **REPAIR — NO AWS LAUNCH.**  The selected-component Jacobian
compiler is mathematically sound in its present raw selector algebra, but that
is not the preregistered `a00pp` coefficient algebra.  Custody and continuation
defects independently block launch.  This is not a rejection of the direct
exact-sparse avenue.

## Frozen-input and light-check evidence

* `shasum -a 256 -c .../SOURCE.sha256`: **16/16 PASS** against the packet's
  current source list.
* `py_compile` on `selected_rows.py`, `test_selected_rows.py`, and
  `aws_preflight.py`: **PASS**.
* `test_selected_rows.py -v`: **14/14 PASS**, 0.229 s, about 73 MiB maximum
  RSS.
* Supporting `test_d43_exact_sparse_source_preflight.py`: **5/5 PASS**,
  0.443 s, about 86 MiB maximum RSS.
* No D43 jet, Singular, solver, or AWS computation was run in this review.

The packet-local `SOURCE.sha256` is internally consistent, but the older
sidecar
`xmodel/d43-direct-exact-sparse-source-preflight-gpt56-20260828.sha256`
is stale on its first three entries.  It records `539d6407...`, `9ba6f0b7...`,
and `389b2abf...`; the current files are respectively `480c7dcd...`,
`504341d6...`, and `5ccc9d3c...`.  The top-level ledgers still cite the old
report hash.  This is a custody failure requiring one coherent reseal, even
though the newer hashes are the ones contained in this packet's source list.

## What passes mathematically

1. The 348-name registry, 22-name support, 184 canonical targets, and band
   counts agree with the source registry and `eplus43` indexing.  The ten
   shallow graph/source translations agree with the committed D25/D43 name
   registry.  Both modular certificates have exactly this nonzero tail
   support and `Xf_alpha=Xg_beta=0`.
2. `sparse_registry` pins the literal 326-name complement before orbit
   multiplication.  This includes `uf/vf`, every B tail, and all six level-74
   PIN42 names.  The fixed B, GB42, and GB21 orbit factors remain exactly
   `{12: eta_B}` with sizes 42, 42, and 21.
3. `selected_source_rows` is the componentwise form of
   `directionb_strike.jrows`: it computes
   `(theta-12)Phi * Gamma_eta - Phi_eta * (theta-18)Gamma` by complementary
   `(eta,slot)` lookup.  The sign is correct.  Moving the right side of the
   normalized Jacobian identity to the left requires `+42`, and the code adds
   it once and only once at `(0,20)`.  At `alpha=beta=0`, the band-42
   `P4P1` sidecar is exactly zero; this says nothing about the two tangent
   directions.
4. The D21 pilot comparison is exact, not modulo a prime: the committed D21
   bank is hash-checked before unpickling, its complement is literally
   removed by source name, it is remapped into the frozen D43 registry, and
   the ten semantic row digests plus the band digest must agree.  As currently
   written this is a valid **raw-`R_ext` to raw-`R_ext`** regression.
5. The semantic encodings are insertion-order independent and retain all
   eight reduced `R_ext` exponents plus normalized numerator/denominator pairs
   in each `Q(sqrt(3))` coefficient.  Registry-ID order, rather than lexical
   source-name order, orders a monomial; because the registry hash is frozen
   and names are unique this is unambiguous, though the report should describe
   it accurately.
6. The review manifest is genuinely inert.  Abstract registration fails,
   fanout and merge fail, and the full-checkpoint path refuses before
   unpickling because final g is absent and producer/consumer compatibility is
   unproved.  `jet_g_03_G0p2.pkl` cannot masquerade as final GB21: even a
   future ready manifest must supply an explicit hash and the payload orbit
   must be `GB21`.

## R1 — decisive coefficient-scope mismatch

The preregistered fast route is the fixed `a00pp` algebra

```text
K0[W1,W2],  K0 = Q(zeta42,r3,A1,A2,h),  [K0:Q] <= 432,
HW1 = h*W1,  HW2 = h*W2,  2*h^2 = 3.
```

The producer does not make this specialization.  It retains the original
`r1_experiment.R_ext` basis with **independent** `HW1` and `HW2` quadratic
generators and the seven-fold `EB` generator.  Before any component choice,
that finite coefficient basis has rank

```text
12 * 2 * 3 * 3 * 2 * 2 * 7 = 6048
```

over `Q[W1,W2]`, not 432.  The existing exact adapter
`cases/d43_common_integral_emitter.py:234-274` performs the missing literal
`a00pp` substitution and refuses an uncancelled B radical.  The packet neither
uses nor hash-pins that adapter.  Its D21 regression compares the uncollapsed
D21 bank to the same uncollapsed algebra; band 20 already contains separate
`HW1` and `HW2` coefficient terms, so the regression cannot detect this
omission.

Thus a successful current pilot would certify a broader selector-algebra row
emitter, not the advertised `a00pp`/rank-432 emitter.  Such output is not
false mathematics, but the 29-live-row, tail-rank-22, and seven-residual-
condition forecasts do not follow from it, and it defeats the intended speed
reduction.

**Clean repair:** make the manifest state the coefficient algebra explicitly
and substitute `HW_i=h*W_i` source-first, preferably before jet multiplication.
Emit canonical `K0[W1,W2]` coefficients and compare band 20 exactly with the
likewise collapsed D21 bank.  A row-level application of the committed
adapter is a semantic fallback but forfeits much of the computational gain.
Add a mutation in which the two HW signs are made independent and require its
digest to differ.

## R2 — relation E is sufficient for the displayed existential bridge

The packet's sentence “relation E alone is insufficient” is literally false
over `C` if `HM` and `s1F` are existential variables constrained only by the
displayed E5/E6/unit equations.  Put `r^2=3`, `a1=3+r`, `a2=3-r`, and
`U=A1*W1^4`, `V=A2*W2^4`.  Eliminating the common linear `HM` from E5 gives

```text
a1^2*(a2-4)*U - a2^2*(a1-4)*V = (-2*r) * E,
E = (9+5*r)*U + (9-5*r)*V.
```

The scalar is a unit.  On `W1*W2 != 0`, E reconstructs a unique nonzero HM,
and

```text
s1F = (2^8/7^16)*HM
```

satisfies E6 and is nonzero; the other choices differ by cube roots of unity.
Therefore `E + W-units` is exactly the existential projection of this
displayed subsystem.

The independent bridge
`xmodel/d43-e5-e6-elimination-bridge-gpt56-20260828.md`, SHA-256
`e1b99600b01f91f7b95df4f7f969481efa1e7b1ee377e83156f3f6b6a8e3c863`,
is **PASS**: its formulas, scalar, units, and E6 reconstruction are correct.

This does **not** collapse the claim tiers.  Relation E does not verify any
other quotient, tower, upstream-template, or pre-existing scale-coordinate
equation.  The correct distinction is:

* raw finite J source: the 184 coefficient equations only;
* displayed E5/E6/unit extension: exactly E plus W units over `C`, with
  mandatory literal reconstruction replay;
* full residue-A/template locus: the preceding objects plus every other
  applicable quotient/tower/tie equation;
* NF equivalence, all-depth compatibility, a Keller map, and JC2: still
  separate and unproved.

## R3 — operational custody defects

The frozen review manifest correctly refuses execution, but merely filling
its fields would not create an acceptable operational packet:

1. `selected_rows.py` checks only that registration fields are nonempty; a
   directly invoked CLI does not verify Linux/EC2/live preflight custody.
   The AWS wrapper must be the only authorized entry, or every compute command
   must consume a hash-bound passing preflight receipt.
2. `aws_preflight.conflicts` suppresses *every* process whose command contains
   the run directory, not just its own ancestors.  A concurrent duplicate job
   in the same directory can therefore evade the idle-host gate.  Remove that
   broad exemption.
3. The manifest's source inventory omits the wrapper, preflight, source-list
   file, and an archive/packet root.  `SOURCE.sha256` includes some of them but
   is not itself authenticated by the registered manifest.  Register one
   immutable archive/root digest (or bind all operational files explicitly).
4. The alleged run tag is only an environment variable and directory basename;
   no live EC2 instance tag is checked.  Bind the real instance tag/identity in
   the launch record.
5. `ARTIFACTS.sha256` is created inside the directory being enumerated, so the
   hash list can include its own file while it is being written.  It is also
   made before final verdict/terminal markers.  Exclude the manifest itself,
   write it atomically after all result files, and bind the terminal receipt.

## R4 — the advertised post-pilot continuation cannot reuse the pilot

`load_sparse_checkpoint_pair` requires the sparse receipt's
`manifest_sha256` to equal the **current** manifest.  The preregistration then
requires a different post-pilot manifest to authorize fanout.  Consequently
the new manifest cannot reuse the reviewed pilot checkpoints unless they are
rebuilt; there is no parent-receipt adoption rule.

The clean, faster design is one immutable conditional pipeline:

```text
build sparse f/g -> exact collapsed-D21 band20 gate
                   -> on PASS, emit all 184 rows from the same inputs
                   -> freeze full receipt for background hostile review.
```

The condition must be enforced inside the producer by a same-manifest pilot
receipt with matching input custody, not only by shell ordering.  Emission is
not a solve, so there is no reason to discard the loaded jets or wait for a
second review round.  If separate manifests are retained instead, v2 needs an
explicit parent manifest/pilot/checkpoint adoption object binding every
content and semantic hash.

The source f and g jets are independent.  Building them serially on one pinned
CPU wastes almost all of a 128-vCPU host.  Build them concurrently as two
separately capped, separately receipted workers (or on two isolated hosts),
then assemble the pair receipt only after their manifest, registry, support,
source, and coefficient-algebra digests match.  Load the pair once for the
all-row emission.

## Independent route evidence and exact launch gate

The sealed Opus 5 audit
`xmodel/d43-exact-sparse-source-opus5-hostile-audit-20260828.md`, SHA-256
`456edb3ad982da10c13ebe6f41e9ebdf7e7124e1ae4ef76363f253626ad5fea0`,
reports source-first modular diagnostics of 29/184 live rows in bands
20/30/40, degree at most two, and tail-Jacobian rank 22/22 at both registered
points.  This makes the **repaired a00pp lane** high priority, but those
diagnostics are not evidence that the current uncollapsed packet has the same
shape.  A nonzero modular 22-minor supports a generic chart; exact elimination
must still retain alternatives where the chosen minor vanishes.

No AWS launch is licensed until all of the following are in one new seal and
receive a different-agent PASS:

1. literal source-first `HW1=hW1`, `HW2=hW2` specialization and canonical
   `K0[W1,W2]` output;
2. exact collapsed-D21 band-20 equality plus HW-sign and `+42` mutations;
3. corrected E/E5/E6 claim language using the reviewed bridge;
4. coherent current hashes/sidecars/ledgers and authenticated operational
   source root;
5. live EC2 identity/tag, zero swap, conflict, process, resource, atomic
   terminal, and artifact-manifest custody;
6. a same-manifest conditional all-184 continuation (or a formally bound
   parent-receipt adoption rule).

After that PASS, launch the collapsed D21 pilot and conditional all-184
emission immediately on isolated AWS.  The maximum first-run promotion is an
exact support-specialized `a00pp` raw-source emitter and its exact row
inventory—not point existence, full-template existence, NF equivalence,
all-depth compatibility, a Keller map, or a JC2 counterexample.
