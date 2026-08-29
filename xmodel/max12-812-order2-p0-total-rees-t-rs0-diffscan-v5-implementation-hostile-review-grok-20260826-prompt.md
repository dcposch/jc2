# Hostile implementation review: derivative-scan `T-rs-0` V5

Independently audit, without editing, the frozen package

```text
cases/max12_812_order2_p0_total_rees_t_rs0_diffscan_v5_20260826/
```

against the reviewed row-streaming V2 package and its reviewed V0R1 parent.
Write exactly one report to

```text
xmodel/max12-812-order2-p0-total-rees-t-rs0-diffscan-v5-implementation-hostile-review-grok-20260826.md
```

and end with exactly `GO_DIFFSCAN_EQUIVALENT`, `REPAIR_DIFFSCAN`, or
`REJECT_DIFFSCAN`.

Pinned hashes:

```text
V5 FREEZE.sha256 = f1db35c4923cdfe97d4900455fa9743b45b76d2b9b6d4eaa7ae51ca9454e6fba
V5 preregistration = fa5af2578ec8a5e55dfb212d97751aca3b19ff49efa9d5a5a80fa25d8143c2ff
V5 compiler = d06210a240a37c08439164da9b5fbbd6c15e35a127923405437fca0f844a5dc8
V5 AWS runner = d2b90d3b1ce392917dce4d52e5006321b57dca3105945d5ce6e42e55e1a94d93
V5 host launcher = 14883225e0c2278c8e72517c82e75464e22b75b8418e0cd30e5f8dac53a0bff6
reviewed V2 compiler = 5b176dfd0747f3736bc4519077877f4d877b5b726b9701e1b9dcaf56e059a112
V2 equivalence review = 5c4ae553ae4e2bc63ff9c15168332daff366b9c33cfd57cfdf89d4fb9bf460b4
reviewed V0R1 compiler = 3aa6bbbbe539607461c5f27b400aeedd335a4d18e01e40d730f5537da4f45938
```

Charge all of the following:

1. Rehash every V5 freeze row and the imported V2/V0R1 chain.
2. Establish that V5 first asks frozen V2 to emit the entire unchanged
   85-variable, 569-tail, seven-row program and then changes exactly the 581
   registered dependency statements, with no other formula/text mutation.
3. Independently reconstruct the 76+7 names and seven occurrences per name.
4. Verify the formal-derivative equivalence in the qring: `diff(Phi,x)=0`
   iff `Phi` is independent of `x` in characteristic zero and in every
   allowed positive characteristic.  Recompute, rather than trust, the
   claimed factor/load census and a rigorous per-tested-atom exponent bound.
   Check the source coefficient degree bound eight against every `F0..F6`
   formula and account separately for target terms.
5. Attack possible failures from `sigma^13`, characteristic-p derivative
   kernels, denominators, noncanonical polynomial representation, target
   variables, and Singular 4.3.2 `diff` semantics.
6. Verify the frozen V2 validator still accepts the V5 compiler contract and
   still binds the transcript/meta/input/manifests, rejects diagnostics, and
   checks all source controls and Delta custody.
7. Verify the AWS wrapper and detached launcher ship/check every transitive
   dependency and do not weaken timeouts, memory bounds, or error handling.
8. Identify the earliest mismatch and smallest repair if any.  Do not inspect
   or rely on a live engine transcript.
9. Keep the verdict strictly at source/software-equivalence scope.  This is
   no manifest result, exact-Q validation, Rees/chart theorem, moving-p
   theorem, order-two theorem, maximum-twelve theorem, or JC2 result.
