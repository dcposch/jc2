# Filtered Euler rigidity: frozen evidence

Claim: FILTERED-EULER-LIFT-RIGIDITY-1, MANUAL / PROVISIONAL, independently confirmed in its exact scope.

The [public proof](../../xmodel/filtered-euler-lift-rigidity-swarmHQ-root-sol56-20261107T1755Z.md) shows that a Keller map exactly scaling the normal-form filtration of x^2-y^5 with weights (5,2,3) is diagonal. Its full polynomial Rees-lift corollary excludes every e>1. It does not establish this filtration hypothesis for arbitrary Keller maps or resolve JC2.

- `producer.md`: exact immutable ROOT proposal, SHA256 225c46785d30f3b066474b0b3277b63a01900e42696a2906e9dcb270ae36cc88.
- `review.md`: exact immutable independent Sol report, SHA256 d3ad89f0a7a4b0b9e209c321c51431019bd06abbd3a808581c0b3667f1fe614b.
- `review-status.json`: public disposition, reading checks and qualifications.

The producer's original basis is the operational workspace commit 47bc9b24cdc26840de5417fe74aefc9f12890cb7; the review and public synthesis use public basis a636e88e7cfc086340c87f66ff149e48f0120d63. Workspace filenames in the immutable originals are provenance labels, not required public replay inputs. These two original reports are preserved byte for byte; their original seals retain their original basis. No operational packet, private model reasoning, credentials, or machine inventory is published here.

Replay is desk-only: read the complete proof and review. From the repository root, verify retained bytes with:

```sh
sha256sum -c box/filtered-euler-lift-rigidity-swarmHQ-20261107T1755Z/SHA256SUMS
python3 ops/seal.py verify box/filtered-euler-lift-rigidity-swarmHQ-20261107T1755Z/producer.md
python3 ops/seal.py verify box/filtered-euler-lift-rigidity-swarmHQ-20261107T1755Z/review.md
```

No CAS, search, formal proof or external source validation is needed or claimed for this evidence package. Literature novelty remains unassessed.
