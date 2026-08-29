# Hostile review request: V21R1 exact filtered-dual local nonmembership

Date: 2026-08-27

Write the review only to

```text
xmodel/max12-812-order2-k00-v21-filtered-dual-local-nonmembership-hostile-review-<model>-20260827.md
```

Do not edit canonical ledgers, producer files, or `jc2-lean`.  Treat every
producer PASS marker as untrusted.  You may write temporary replay files
outside the producer tree.  State the exact model and tool versions used.

## Charged claim

For the exact normalized K00 data over `Q`, put

```text
J_X=(r1,...,r6)+E_X,
D_X=h*a7^X-sum_i u_i*a_i^X,
```

for `X=K10,K6,K2`.  V21R1 claims exact functionals on
`R/m^(D+1)` at cutoffs 4, 3, and 2 which annihilate the complete truncated
images of `J_X` and pair nontrivially with `D_X`.  It concludes

```text
D_X notin (J_X)_m
```

in all three directions, hence the three V17 branches are `LOCAL_NONZERO`.

## Frozen packet

Producer directory:

```text
cases/max12_812_order2_u2_62_k00_filtered_dual_local_nonmembership_v21_20260827/
```

Important hashes:

```text
PREREGISTRATION.md                 27fb885a1602257c2885e89c194c2d5f5bb2e7a3709f88f366e0c2807a5ad5dc
PREREGISTRATION_R1.md              137fdc18c349a549949e90c3d515b5e08e01d9f69a6be5f8efbbf97b78175d7d
FAILURE_R0.md                      06544be839c794e452de101a75a0926d1a99acc4ba86b27470eaa9d2de15fd20
R1 verifier source                 fd97d0b80b48bd46afd45a21a29a50f18592a68aac9047ad94d9abfb438ad875
R1 source-freeze manifest          4c35362b7223566317ca346bd261fb13023fbb3d8a48aef2908dd00d1a168026
31-input flat manifest             38c6dd45b888ec04a5c0b9bdd4b93625a1df491b4e4f63851f5546cb1d7d465f
RESULT.md                          b514ef728afd47518246727efc5a7b41efb768707c4fe08f5625a96a8d32efb9
exact RESULT.json                  7341d67bb6abfba9ce1b99d6670360721214aaf6bbb51165dbf84964c65e7ad3
49-file evidence manifest          00159ec022932932373fc294980541ca791a173e5bbdbe58072d84d6b3b74b49
fresh/serialized syzygy module     83832f380ce11a491c9799e50ff8b36b5fbc3a6b0d5b5dc52d90b6239c129a7a
```

Exact evidence is under `aws_q_box01_r1_pass/`.  The rejected R0 packet is
under `aws_q_box01_r0_failed/` and must remain nonpromotable.

## Mandatory attacks

1. Rehash every R1 freeze/evidence entry and verify the R0/R1 chronology.
   Confirm that R1 changes only the zero-column module comparison and
   unsupported Singular quit syntax.
2. Independently reconstruct the six unloaded rows, the three seven-row load
   coefficient lists, `h,u_i`, all 66 syzygy images, and all three targets.
   Replay the syzygy identities and establish that the serialized module is
   the full `Syz(r1,...,r6)`, not a sampled submodule.  Do not rely only on
   the producer's generator count.
3. For each cutoff, independently enumerate all monomials of degree at most
   `D`, every generator multiplier through `D-ord(g)`, and rebuild the
   augmented matrix.  Compare its semantic entries and row/column maps with
   the frozen bytes.  Check that no high-order generator which could
   contribute was omitted.
4. Independently parse each rational dual.  Verify coefficientwise
   `y^T M=0` and exact nonzero pairings

   ```text
   K10: 25/45056,  K6: 45/11264,  K2: -25/352.
   ```

   Mutate one target or one live matrix entry and require the replay to fail.
5. Audit the local-unit lemma carefully.  Check both implications used:
   local membership gives `s(0)!=0` with `sD in J`, and such `s` is a unit
   modulo `m^(D+1)`.  Decide whether the exact finite dual really implies
   local nonmembership without a colon computation.
6. Audit the dependency-order repair.  Decide whether this exact proof can
   supersede only V18R2's administrative wait for monolithic V17-Q while
   preserving the V17/V18 mathematical definitions.  Treat the live colon
   calculation only as a cross-check; flag any hidden circular dependence on
   its unknown exact endpoint.
7. Enforce the scope firewall.  Even PASS proves only three separate
   normalized first-load local classes.  It does not couple loads, restore
   Lambda weights, include targets/Jdet, exclude an arc, decide K00 closure,
   order two, maximum twelve, or JC2.

## Required verdict

Give `PASS`, `FAIL`, or `INDETERMINATE` at the exact charged scope.  State the
smallest proved statement, every defect or additive correction, the replay
hashes you independently obtained, and whether V18R2's exact filtered
results may now be consumed without waiting for monolithic V17-Q.  On
completion, print the output path and SHA-256 in your final response.

