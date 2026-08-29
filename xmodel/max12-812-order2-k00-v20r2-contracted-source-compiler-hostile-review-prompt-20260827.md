# Hostile review request: V20R2 contracted mixed-source compiler

Date: 2026-08-27

Write the review only to

```text
xmodel/max12-812-order2-k00-v20r2-contracted-source-compiler-hostile-review-<model>-20260827.md
```

Do not edit canonical ledgers, producer files, or `jc2-lean`.  Treat every
producer PASS marker as untrusted.  Temporary replay files must be outside
the producer tree.  State exact model and tool versions.

## Charged claim

V20R2 claims an exact, typed compiler—not a jet or closure theorem—for the
normalized K00 seven-row source through `Lambda^19`.  Its live design first
contracts the universal deformation vector by simultaneous parameters and
only then applies

```text
p=(Lambda^2*k10,Lambda^6*k6,Lambda^10*k2,
   Lambda^14*mu2,Lambda^16*mu4,Lambda^18*mu6,Lambda^19*Jdet).
```

It claims 140 exact literal equations on a 169-column source with five
boundary-zero constants and 164 free columns, plus exact agreement with the
contracted syzygy/Kuranishi presentation.

Producer directory:

```text
cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/
```

## Mandatory attacks

1. Rehash the R0/R1/R2 chronology, both failed packets, all freeze manifests,
   and the clean 23-file R2 harvest manifest.  Confirm R0 was pre-algebra and
   R1 stopped before Singular.  Audit the original R2 self-listing manifest
   defect and additive repair without silently discarding it.
2. Independently derive why the R0 vector-cokernel extension test is
   tautological: coordinate projection induces `Qcommon -> Q_X`.  Verify the
   corrected scalar object

   ```text
   Q_p=B/(I, <p,Gamma(s)> : s in Syz(r1,...,r6)),
   D_p=<p,K(w)>.
   ```

   Decide whether contraction-before-specialization is correctly typed.
3. Independently parse the 569-tail JSON, exact K00 coordinate map, load
   weights, target rows/signs, and boundary conditions.  Reconstruct all 140
   coefficient equations.  Compare semantic equations—not only hashes—with
   the 309,343-node DAG and complete column map.  Confirm `Jdet` is not `J1`
   or `J2`.
4. Recompute/replay the full 66-generator six-row syzygy module and all 87
   seven-row controls.  Verify `h*r7=sum u_i*r_i`, `h(0)=20`, every coordinate
   cross relation, all contracted generators, and the exact contracted
   target.  Do not trust generator counts alone.
5. Independently evaluate all 140 roots on at least one new exact-Q fixture
   and one new prime-field fixture.  Verify the honest residual through grade
   19.  Re-run or replace every mutation: target sign, k6 weight, boundary
   restriction order, modular normalization, syzygy sign, and contraction
   order.
6. Audit the exact source census and unit opens.  Ensure the five zero
   constants are restricted before any saturation/solve, and require a
   negative control showing the unrestricted source differs.
7. Enforce scope.  PASS is only an exact source/type/compiler milestone.  It
   does not cover nonlinear prefix strata, decide finite jet compatibility,
   exclude an arc, decide closure incidence, order two, maximum twelve, or
   JC2.

## Important frozen hashes

Read the producer report and custody erratum for the complete packet.  Key
hashes are:

```text
V20R1 design erratum       0f2debfecf1ae127db20de8a806e93842a0f333fce3592a3e09231a48ad3b53b
R2 source freeze           8f9e893fa3357787ef8d095cb8e1e040efe788ce54b70f150b77ad1b5bab41cb
R2 compiler                2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
R2 result JSON             a2147de95bc37e8adb629201e2b39b788b99df3d4586da54af7bd41f269a9f15
literal DAG                b9bd2e2ca1319ee3107a0f7cf4e1750386d60bb12213a3a970c4812823abdce6
contracted generators      6ba4a0233b713e65be98181285f58fe13cb7ecdb724fd29000b303204f0ef423
contracted target          cade1704d973750e455829a3c3783d1c8444a4bb6e2b14e37e8277c83393819c
fixture audit              bbcdd0e0242a23b309cd04f44f42a0ef8f1b69eb8f13ef396fc40b26e450cf55
defective original manifest 72277a97af9a72dabb7c491a860018357eed7133fba9b1ff6f9676a6645397e4
```

## Verdict

Return `PASS`, `FAIL`, or `INDETERMINATE` at the exact compiler-only scope.
State the smallest proved statement, all defects/additive corrections,
independent replay hashes, and the precise next finite mixed-source
discriminator.  Print the output path and SHA-256 on completion.
