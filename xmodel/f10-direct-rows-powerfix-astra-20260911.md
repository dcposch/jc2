# Direct-row polynomial power: prescribed static correction

First action: 2026-09-11 04:01:25.120304512 UTC. Original reserve 04:09 UTC / hard stop 04:12 UTC, unchanged. Owner: /root/model_productivity. Basis: 0d39df3c9fd69c939a8420c54d03228b9077777d.

Scope: a new immutable arithmetic.py copy containing only the FIRST review's prescribed final-square correction. No scientific execution, import, AST, syntax, compilation, test, payload, fixture, place, worker or network action is performed.

## Completed change

The owned arithmetic.py differs from the frozen producer arithmetic.py at exactly one hunk in polynomial power(): the assignment `a,n=mul(a,a),n//2` becomes `n//=2` followed by `if n:a=mul(a,a)`. The literal diff is retained. Every other byte, including field fpow(), imports, functions, coefficients, exceptions and caps, is unchanged. The old source and report remain frozen.

Old SHA-256: d196346966f09f1e9ef2a4f6e20df74f8d218c32e06d2f341ccf25fb4b39d90b. New SHA-256: acd07f800707c379aba60bd06f239d38cd83c86867729561367abd2bcc04ce73.

The combined FIRST gate confirms A–E and identifies this specific correction for F. This report applies that prescribed correction; it does not independently promote the entire package, change the checker, patch a caller or grant registration. ROOT still verifies the exact diff and updates prospective installed hashes through its own workflow.

## Manual equivalence and stopping behavior

For initial polynomial a0 and nonnegative integer N, at each loop entry the binary-power invariant is r*a^n = a0^N. Write n=2k+epsilon, epsilon in {0,1}. The conditional accumulator multiplication replaces r by r*a^epsilon. When k is positive, the assignments n=k and a=a*a restore the invariant. When k is zero, the loop terminates and the accumulator already equals a0^N; there is no need to compute the unused square of a. For N=0 the loop is skipped and the unchanged initial constant one is returned. Negative input retains the same initial refusal.

This proof concerns the existing nonnegative-integer contract; it introduces no broader exponent type. In exact polynomial arithmetic, both versions return the same value whenever both complete. Operationally the new version omits precisely the final mul(a,a) whose result cannot be consumed. A failure solely inside that discarded multiplication is no longer demanded; all multiplications actually needed for the result, their ordering, their existing refusal checks, and all caps remain unchanged. No claim is made that either implementation now fits a given runtime or support ceiling.

A manual control is N=1: after the accumulator receives a0, the result is complete and the new loop performs no square. The old version unnecessarily computes a0 squared. N=0 retains the no-multiplication path. These are invariant checks on source text, not executed fixtures. Field fpow() is byte-identical and is deliberately outside the correction.

## Read scope and limits

Exactly two inputs were freshly hashed before their full text was read: the complete 26313-byte FIRST review and the complete 9143-byte old arithmetic.py. Neither output was clipped. Earlier campaign context is reused only as context, not an additional charged body or acceptance premise. No provenance, runtime-review files, coefficient bodies or other lane were read. PINS.json records the exact paths and hashes; custody records postpins and owned bytes.

The review's generic-support estimates, asserted cap sufficiency after the change, and cost-dominance statements are not adopted. Actual support, time, memory, required source evaluation, independent agreement and semantic-control success remain unknown. No numerical runtime forecast, cap increase, optimization, source conclusion or new canonical OPEN is supplied. The cheapest remaining check for this correction is ROOT's literal diff and installed-hash verification; actual execution remains separately authorized.

All owned source/document bytes are manually read before sealing. Source diff and metadata publication are documentary operations only; no import, AST, syntax, compile or test has occurred. Own-only target absence, no raised OPEN, unchanged postpins, unique final body marker and expected transaction verification precede custody-first handoff. All writers are IDLE at terminal, with no follow-on authority.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4382`.
- Body SHA-256:
  `b160524ceadcee28c51677fb76ca18387c11d272593108eae6b3b19b37585d20`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
