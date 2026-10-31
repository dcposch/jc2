# Contractible whole nonproper-value curve exclusion

The [reviewed theorem](../../xmodel/contractible-nonproper-curve-swarmHQ-root-sol56-20261031T1245Z.md) excludes a nonempty contractible **whole** nonproper-value curve of a noninvertible plane Keller map, including reducible unions, at the explicit inherited foundations. MANUAL / PROVISIONAL; independent PASS_CONDITIONAL. Noncontractible cases and JC2 remain open; novelty is unassessed.

[CANDIDATE.md](CANDIDATE.md) preserves the original producer bytes; the [independent review](../../xmodel/contractible-nonproper-curve-review-sol56-20261031T1240Z.md) preserves its exact verdict and six-step check. [CUSTODY.json](CUSTODY.json) records hashes, the exact6322-byte proof excerpt, provenance, inherited assumptions and the review's one-window counting correction. No mathematical claim changed during publication.

Desk-only proof. From the repository root:

```sh
sha256sum -c box/contractible-nonproper-curve-swarmHQ-20261031T1245Z/SHA256SUMS
python3 ops/seal.py verify --expected-basis 8f4d810c5412aab4bb05b004ba499d5378163363 box/contractible-nonproper-curve-swarmHQ-20261031T1245Z/CANDIDATE.md
python3 ops/seal.py verify --expected-basis a8564152a8ea83c377848837381ca4e036db3aef xmodel/contractible-nonproper-curve-review-sol56-20261031T1240Z.md
python3 ops/artifact_finalize.py verify --final xmodel/contractible-nonproper-curve-swarmHQ-root-sol56-20261031T1245Z.md --expected-basis a8564152a8ea83c377848837381ca4e036db3aef --expected-manifest-sha256 1e75937786ff69128e128a5f53fb7df5fc9b023efbe33fee42dec5fd462fdd33
```

The candidate's basis is a locally banked swarmHQ producer commit, not asserted to be a public Git object. The portable copy retains its original canonical seal; the public integrated report has its own manifest. Classical source proofs were not newly audited. In particular, no individual-component exclusion or inference from normalization degree one to multibranch-image injectivity is licensed.
