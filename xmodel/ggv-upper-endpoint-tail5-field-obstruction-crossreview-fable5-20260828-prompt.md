# Hostile cross-review charge: cutoff-five upper-endpoint field obstruction

You are Fable 5 acting as an independent hostile mathematical reviewer in
the plane Jacobian-conjecture campaign.  Work in
`/Users/dc/code/math/jc2`.  Review a producer result; do not merely summarize
it or trust its analyzer.

## Write boundary

Write exactly one final report:

`xmodel/ggv-upper-endpoint-tail5-field-obstruction-crossreview-fable5-20260828.md`

You may use an isolated `/tmp` scratch directory.  Do not edit the producer
packet, canonical top-level ledgers, or any other repository file.  Do not
enter, list, search, read, build, status, or modify `jc2-lean`; it is a
user-owned concurrent worktree.  Do not launch AWS or any heavy local CAS.
Standard-library exact rational/polynomial scripts and the producer replay
are allowed.

## Frozen producer packet

Primary directory:

`cases/ggv_8_28_upper_endpoint_tail5_desk_20260828/`

Read at least `PREREGISTRATION.md`, `RESULT.md`, `analyze_tail5.py`, both
manifests, both standalone certificates, and the authoritative raw sources
named by `SOURCE.sha256`.  Also read these two discovery notes only as claims
to audit, not as authority:

* `xmodel/ggv-upper-endpoint-tail5-characteristic-core-unit-r0-sol-ultra-20260828.md`
* `xmodel/ggv-upper-endpoint-tail5-d18-quadratic-branch-unit-r0-sol-ultra-20260828.md`

Frozen principal hashes are:

```text
a4f627c1bc62abc02410c3c64e03433c612cb97fa3c1ed6065238f2af65b2210  RESULT.md
f62fc30a1d26192e24e035d0645af141f90affa04247995d66e927f02cb5497e  analyze_tail5.py
a3382efcd72104d48abb40981a33b87d9dacb5e7a9018a12937bef1f794f942c  TAIL5/TAIL_DEFORMATION_SYSTEM.json
6e6ce211c1152812f639c140b384f65c51ddfedca9add1d9768df6203b224076  TAIL5_DESK_ANALYSIS.json
60bd4ef90fac13412e090af9f8ba6ead0d293e53b53e0b5b7520efe08d3b85e4  CERTIFICATES/tail5_v0_unit.json
87efe8a899471d79347e7273dcd4f9b060e64877f63e974ac98bea85bf5496a2  CERTIFICATES/tail5_v_nonzero_D18_K_unit.json
0766bd5ece21a9ee2f02e5b61c1f5738af7cb5fee07877bce77b57038360b71d  SOURCE.sha256
1668e6a540ed646c11d841b224d724054b4e77723bdebfeda88850dd3da00fe5  EVIDENCE.sha256
```

## Claimed theorem

The fixed branch-P, square-baseline specialization in which every raw
deformation parameter of weight below five is zero, with `D0=...=D21=0`
and literal endpoint `D22=1` (no `D23`, no `G22` slot), has no
characteristic-zero field point.  The producer explicitly makes no claim
about the associated nonreduced scheme, the full branch-P family, another
GGV branch, a Keller pair, a counterexample, or JC2.

## Required independent audit

1. Verify the frozen hashes/manifests and run the replay.  Record elapsed
   time and exact outcome, but do not count self-consistency as independent
   proof.
2. Independently reconstruct enough of the authoritative raw determinant
   system to check the cutoff, retained-variable census, prefix rank/nullity,
   literal endpoint `-1-p32*p139+p86*p91`, raw-slot meanings, signs, and the
   absence of normalization.
3. Check the D10--D15 field-radical cascade from literal compatibility spans,
   including all four coefficients of `T^2 mod (X^4-1)`, the reconstruction
   `c=(3/16)V0(V0+4R0)`, and the three scalar core equations.  State exactly
   where squarefreeness and field-valued semantics enter.
4. Check that `p129=F8[X^0]` is absent from every D10--D22 generator and that
   setting it to zero is the global additive `F -> F+mu*t^8` gauge slice,
   not a carrier normalization.
5. Independently verify that the cumulative D16--D17 invariant-core
   intersection adds
   `K17=V0*(b*V0+R0^2)` with a valid literal-source span witness.  Try to
   falsify this by perturbing or deleting a charged source coefficient.
6. Audit the complete branch cover.  On `V0=0`, expand the division-free
   endpoint unit certificate back to its stated generators.  On `V0!=0`,
   derive—not assume—the quadratic relation and the five displayed linear
   substitutions over `K=Q[tau]/(12*tau^2+6*tau+1)`; check irreducibility and
   all forbidden divisions.
7. Rebuild the D16--D18 quadratic-field calculation independently.  Verify
   the K-linear/Q-doubled semantics, the 20/38/58 ranks, absence of a scalar
   through D17, the eight grouped cofactors (13 rational rows), and that their
   literal product-sum is exactly `1`.  Compose or audit the provenance all
   the way to literal raw rows; check that no endpoint equation, D19+ row,
   hidden normalization, numerical root choice, or unrelated relation leaks
   into the unit.
8. Run hostile mutations beyond passive replay where useful, especially one
   used D18 raw-source coefficient, the quadratic sign, and omission of
   tau-multiple rows.  Distinguish a genuinely charge-sensitive failure from
   a cosmetic mutation.
9. Search actively for sign errors, index-base errors, stale-hash reliance,
   radical/scheme overreach, bad localization, omitted branches, or a gap
   between staged compatibility rows and literal determinant equations.

## Verdict format

Lead with exactly one of:

* `PASS — independently confirmed as stated`
* `NEEDS REPAIR — core survives, but promotion is blocked`
* `FAIL — claimed field obstruction is not established`

Then give a concise theorem statement, independent checks with exact
identities/ranks/provenance, mutation results, every issue ranked by severity,
and a precise promotion recommendation.  A minor documentation defect must
not be inflated into a mathematical failure; conversely, do not pass an
identity that has only been replayed through the producer's own code.
