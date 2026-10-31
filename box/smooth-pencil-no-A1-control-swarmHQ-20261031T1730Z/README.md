# Smooth pencil with no affine-line fibre: evidence

The [standalone proof](../../xmodel/smooth-pencil-no-A1-control-swarmHQ-root-sol56-20261031T1730Z.md) gives h=[xy-1:x+y(xy-1)] over C. This morphism A2->P1 is smooth and surjective. Its three fibres at 0,1/2,-1/2 are C*; every other fibre, including infinity, is A1 minus two distinct points. Every fibre is irreducible and rational, and none has an A1 component.

Evidence: MANUAL with a fixed symbolic check; lifecycle PROVISIONAL; [independent Sol review](../../xmodel/smooth-pencil-no-A1-review-sol56-20261031T1720Z.md) PASS. Novelty is unassessed. The Jacobian xy^2-x-y is nonconstant and radial etaleness fails, so this is not a Keller counterexample or a proof of Keller surjectivity. JC2 remains unresolved.

- [Original candidate](original-candidate.md): exact sealed ROOT artifact reviewed by Sol, including its original UNREVIEWED status. Its plain-text HQ runtime paths are historical provenance, not dependencies of the public proof.
- [Reviewed mathematical core](reviewed-proof.txt): exact contiguous 3083-byte,46-LF substring of that candidate, reproduced unchanged in the standalone proof. SHA256 27fde737222dc12fc30ffac8b6f9adcac31fa2eb206fd978a036f71a7e836d7e.
- [Fixed symbolic receipt](fixed-check.json): SymPy1.12 checks the Bezout, differential, fibre and infinity identities, discriminant and resultant. The prospective Bezout coefficient had a sign typo; the check exposed it before sealing, and both the candidate and reviewer use 1+y^2. These computations do not certify the geometric argument.
- [Checksums](SHA256SUMS): six retained scientific files. Exact original reviewer bytes and the candidate seal are preserved; the public integrated report has its own artifact manifest.

The review covered every exceptional value, both inverse regular maps, smoothness, nonemptiness and irreducibility, and the exact non-Keller limitation. ROOT read all109LF of the sealed review. Its packet reading was audited independently: all required bytes covered and retained inputs unchanged. The reviewer self-reported one wrapper formatting failure before Python; no failed executed shell command was observed, and this does not alter the mathematical review. No independent editorial review of the standalone presentation or novelty investigation is claimed.
