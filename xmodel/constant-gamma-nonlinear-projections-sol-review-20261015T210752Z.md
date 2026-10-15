# Independent review: constant-gamma nonlinear projections

Claim: CONSTANT-GAMMA-NONLINEAR-PROJECTION-1.
Verdict: ACCEPT_SCOPED.
Independent reviewer: native agent `constant_gamma_hostile_sol_2106`, requested
model `gpt-5.6-sol`; hosted model identity is not independently attested.
Author finish: 2026-10-15 21:07:52 UTC.
Custody: swarmHQ ROOT transcribed the delivered message; ROOT is the producer
and custodial transcriber, not an additional independent reviewer.
The exact agent handle was personally confirmed COMPLETED at collection.
Basis: 38b0886e06f7e5aaf22a7c143630d3b8dd628c31.

Reviewed [producer report](constant-gamma-nonlinear-projections-swarmHQ-root-20261015T210000Z.md):
6150 bytes, mode444, full SHA256
`7a09a747314c2ab1fff29b397a226651f002d7bf6996062db8a76f0549887ce7`.
Body: 5818 bytes, SHA256
`9dea0e6c17ab75813a1b52bfe768681109b4f060358c4d1b68f3ffa079d31f8d`.
Manifest: 729 bytes, mode444, SHA256
`a7eacdf9e2700239018c4a4adab659815ac39e36c3e9bfbcc6f20284cb2191f9`.

The reviewer reported initial and final whole-set integrity gates PASS, a whole
read of report, manifest and FALLACY-v2, and canonical verification VERIFIED.
ROOT separately rechecked the six pinned inputs and the canonical verifier
before this transcription. No CAS, source import or numerical experiment was
used. The frozen producer's PROVISIONAL label records its creation status;
acceptance is recorded here and in the integration ledger, not by resealing it.

## Delivered mathematical review (verbatim paragraphs)

FINAL — ACCEPT_SCOPED. Finish UTC 2026-10-15T21:07:52Z. Scope accepted exactly as stated: over C, c≠0, d=deg p≥2, q'=wp'/2, and literal C0,D0,E0 polynomial on all A2, no P,Q∈C[C0,D0,E0] have nonzero constant Jacobian. This is only an exclusion of this constant-gamma construction class, not JC2/arbitrary graphs/nonconstant gamma/novelty.

Independent hard-step audit: whole-plane divisibility at x=0 gives p(c)=-2c, r(c)=q(c)+c²=0, then the x-linear coefficient of r(c(1+xy)) forces r'(c)=0 and hence p'(c)=-2. Since deg p=d and deg r=d+1, [C(w):C(p,r)] divides both degrees, hence is 1. C[w] is finite over C[p,r] via the monic rescaling of p(w)-p, and being normal with the same fraction field is the affine normalization—no embedding or assumed normality of the image is used. Homogenizing to degree d+1 gives [ZP_d:R_{d+1}:Z^(d+1)], base-point free, with unique preimage of infinity; the local p/r term has nonzero linear tau coefficient, so the image is smooth there. Birationality plus line pullback makes image degree d+1; its arithmetic genus d(d-1)/2>0 versus normalization genus 0 forces an affine singularity. A singleton finite fiber plus nonzero derivative of at least one coordinate would make the germ a smooth graph (and there is no other branch), so that singular fiber has distinct w0,w1.

Attachment/residue audit: ai=wi/c-1 are distinct and psi_i(s)=(s,ai/s) are regular C*→A2 even when ai=0; all three generators agree by p- and r-collision. For J(P,Q)=κ, beta=P dQ-κx dy is closed and has a polynomial primitive. Since psi_i*(xdy)=-ai ds/s, subtraction gives d(T∘psi0-T∘psi1)=κ(a0-a1)ds/s with the stated sign; a Laurent-polynomial derivative has zero residue but RHS coefficient is nonzero. Contradiction is valid.

Controls: the cubic example differentiates to q'=wp'/2 and the displayed quotients follow after factoring the required x and x² powers. The d=1 example yields (cx,-2y,-y²/2), with J(C0,D0)=-2c, correctly showing necessity of d≥2. No correction or gap found.

## Integration scope

This is a manual, independently reviewed construction-class exclusion, not a
formal certificate or a proof of JC2. It removes the output-degree restriction
for the specified constant-gamma class, for every eligible seed of degree at
least two. The plane arithmetic-genus formula supplies the parameter collision;
the exact-Liouville residue obstruction itself is already known.
Nonconstant gamma and arbitrary plane Keller maps are not covered. No theorem
reducing general JC2 to this class, or external novelty claim, is supplied.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4109`.
- Body SHA-256:
  `23bd833326bb188c2a6ba5ca4b0295deb2fddc22d9ce5a8920c59faba1fd1786`.
- Frozen basis: `38b0886e06f7e5aaf22a7c143630d3b8dd628c31`.
