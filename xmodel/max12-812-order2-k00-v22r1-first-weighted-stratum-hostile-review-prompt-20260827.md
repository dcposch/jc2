# Hostile review charge: V22R1 first weighted K00 stratum

You are an adversarial mathematical and computational reviewer.  Treat every
producer PASS marker, prose claim, and serialized Gröbner basis as untrusted.
Work independently from the frozen bytes.  Do not edit producer artifacts,
canonical ledgers, or `jc2-lean`.

Review producer directory:

`cases/max12_812_order2_u2_62_k00_weighted_first_stratum_v22_20260827/`

Write your report only to:

`xmodel/max12-812-order2-k00-v22r1-first-weighted-stratum-hostile-review-20260827.md`

When complete, print the output path, SHA-256, and one of `PASS`, `FAIL`, or
`INCONCLUSIVE` with its exact charged scope.

## Frozen gates

- `PREREGISTRATION.md`:
  `1b4ae1199e7e2e88fa56c9a8c4d5a48e853af5fa67b75766b0a30c1aa0353180`
- `PREREGISTRATION_R1.md`:
  `1bbabb2aeb9385756e2ac1edf0ec075a613920fb939122826307e9bd3f7caf78`
- `FAILURE_R0.md`:
  `677f6451fc126ef1b44998619436d11e9a2ca1c567ba3fd4dba0be2c01d4d0ad`
- R1 source-freeze manifest:
  `19c5a44190f685438240fc418fe0a99e419abf71c8d055133e3f14fb05a7751b`
- R1 compiler:
  `23ad457b06c42073ddf64b2162b8458d412315d104fb61995d1eacf6b1855a81`
- producer report:
  `494075c5675a2571808aec8606ed5744c2362bf3abc470304226b6fee699e293`
- exact `RESULT.json`:
  `920c31841cd96ea4cbac0172f14923b209c3e2a3d00ad8a264299ff592bdd9c4`
- evidence manifest:
  `99d6b1e6274a30cbffdae87a72e8a42011fe2059a499684c6ac1f28774512ad9`
- serialized quartic `F10`:
  `c8e214ae21b058dddb063dcd7a9075a34b02a14f01f54386822cf85f0dc2c8e8`

First rehash the freeze and all 14 evidence entries, checking that the
manifest excludes itself.  Audit the complete R0/R1 diff: R0 must remain a
pre-algebra failure, and R1 may change only the exact quadratic-profile
predicate, its two mutations, and its preregistration gate.

## Required independent attacks

1. Parse the frozen unloaded rows independently.  Confirm exactly that the
   degree-two initials `Q1,...,Q5` are nonzero and `Q6=0`; fire both a
   nonzero-Q6 mutation and a zero-Q1-through-Q5 mutation.
2. Reconstruct the 66-generator K10 filtered image and target from the
   charged V21/V18 bytes.  Replay every entry of the complete D3 lift with
   the correct sign.  Confirm that the residual vanishes through degree
   three and independently emit its degree-four homogeneous part `F10`.
   The re-emitted polynomial must be byte-identical or proved coefficientwise
   equal to the charged quartic.
3. Replay the exact D4 dual coefficientwise.  It must annihilate every
   truncated generator and pair with `F10` as exactly `25/45056`.  Check a
   sign mutation and at least one lift-coefficient or dual mutation.
4. Independently compute `T=(Q1,...,Q6)` and
   `L=(Q1,...,Q6,F10)` over `Q`, preferably with a different order or
   architecture.  Confirm `F10` is nonzero modulo `T`, `L` is proper, and
   `dim Q[x0,...,x5]/L=3`.  Explain why homogeneity and affine dimension
   three imply a nonempty projective closed prefix stratum.
5. Type-check the honest weighting.  On
   `d=Lambda*x+O(Lambda^2)`, `k10=kappa+O(Lambda)`, `kappa!=0`, verify that
   the first canonical contracted K10 equation is at weighted grade six and
   is `kappa*F10(x)=0`.  Explicitly rule out cancellation at that grade by
   the K6, K2, mu2, mu4, mu6, and Jdet weighted directions or by a change of
   the complete six-row syzygy representative.  If the frozen artifacts do
   not suffice for this typed conclusion, say exactly what is missing and
   downgrade the verdict.
6. Reject either inflation: `F10 nonzero mod T` alone does not exclude all
   valuation-one prefixes, while `dim L=3` does not produce a full
   Lambda<=19 jet or arc.  State the smallest exact theorem and both-outcome
   scope.

The only charged conclusion eligible for PASS is: at grade six on the
valuation-one, `k10(0)!=0` prefix, the open set `D(F10)` is excluded and the
closed homogeneous stratum `V(Q1,...,Q6,F10)` remains, with affine dimension
three.  No grades 7--19, full-jet, arc, closure-incidence, order-two/max-12,
or JC2 conclusion is authorized.
