# Two-bad-fiber pullback: independent FIRST and integration

Verdict: CONFIRMED; PROMOTED / MANUAL at the exact hypotheses below.
ROOT producer; independent native Astra-assigned FIRST, completed
2026-10-20 13:43:16 UTC. ROOT transcribes and integrates the returned review.
No machine proof, hosted-model-identity verification or external novelty claim.
JC2 remains unresolved. Frozen basis: 274495802774139fee1cd64ca828bc7cef898675.

## Exact accepted statement

Let F=(P,Q):A2_C -> A2_C be polynomial Keller. Identify the target
K=C(u,v) with its image in L=C(x,y). Let a,b in C[u,v] be coprime
and algebraically independent. Suppose f=a/b is target-primitive:
C(f) is relatively algebraically closed in K.

For finite lambda use the affine divisor div(a-lambda*b); for infinity
use div(b). Empty divisors count as reduced. If at most TWO of these
divisors are nonreduced, C(f) is relatively algebraically closed in L.
Affine basepoints are allowed. No generic-genus assumption is made.

The [sealed producer](two-bad-fiber-pullback-swarmHQ-root-20261020T133400Z.md)
remains unchanged, including its historically correct UNPROMOTED label.
This separate review and the evidence ledger record the later promotion.
No correction to the producer statement or proof was required.

## Independent reconstruction

1. F is dominant, etale and quasi-finite. A common prime divisor of
   a(P,Q),b(P,Q) would be contracted into the finite target base locus.
   Therefore the pullbacks are coprime. They remain algebraically independent.
   Each target prime has nonconstant polynomial pullback and thus a source
   prime above it; quasi-finiteness prevents contraction of that prime.
   Etaleness gives ramification index one. Reduced fibers stay reduced.

2. A finite intermediate curve field E/C(f) inside L is rational:
   restrict the dominant rational map from A2 to a suitable line and
   apply Riemann-Hurwitz to its smooth projective model. Thus E=C(H),
   f(P,Q)=R(H), and deg(R)=[E:C(f)]=d.

3. Write H=c/e in reduced polynomial form. A divisor-empty fiber at
   infinity makes e constant. A divisor-empty finite alpha fiber makes
   c-alpha*e a nonzero constant, so 1/(H-alpha) is polynomial.
   Either case gives a polynomial Mobius generator T of C(H).
   Express f(P,Q)=U(T)/V(T), where U,V in C[t] are coprime.
   Bezout keeps U(T),V(T) coprime in C[x,y]. Reduced-fraction uniqueness
   gives a(P,Q)=gamma*U(T), b(P,Q)=gamma*V(T), gamma in C*.
   This contradicts algebraic independence. EVERY H-fiber therefore
   has an affine prime divisor component, despite possible basepoints.

4. For any ramification point alpha of R above lambda, choose a prime
   component of H=alpha. At its generic point the composite multiplicity
   equals e_alpha(R) times its positive H-fiber multiplicity, so is >1.
   Reciprocal local parameters handle infinity. Thus lambda must be one
   of the at most two nonreduced target-fiber values. No divisor-empty
   exception remains. Componentwise reducedness, not just gcd of
   multiplicities, is the assumption used here.

5. Pad the branch-value set to two distinct values. If their fibers
   have k_0,k_1 distinct points, Riemann-Hurwitz gives
   2d-2=(d-k_0)+(d-k_1), hence k_0=k_1=1.
   Thus R=M composed with z^d composed with N for Mobius maps M,N.
   In particular M^(-1)(f(P,Q)) is a dth power in L.

6. Every target affine prime is detected with index one by step1.
   All target valuations of M^(-1)(f) are consequently divisible by d.
   Unique factorization in C[u,v], allowing negative exponents, and
   complex constant roots give M^(-1)(f)=h^d in K.
   For d>1, the nonconstant h generates a degree-d extension of C(f),
   contrary to target primitivity. Therefore every such d equals1.

These are manual algebraic arguments with the classical imports used in the
producer: etale/quasi-finite Jacobian criterion, smooth projective curve
models, line restriction/Riemann-Hurwitz, and polynomial UFD factorization.
No properness of F is assumed in the prime-detection step.

## Construction consequence and limits

Suppose a dominant rational donor D satisfies f composed D=R(H),
deg(R)>1, for a target f meeting the accepted hypotheses. A dominant
rational SOURCE substitution preserving these target functions cannot
make D polynomial Keller: the proper algebraic intermediate extension
survives the injective source-field embedding. This also covers finite
source-field enlargement when the resulting source is a rational plane.
It does not cover arbitrary birational TARGET changes.

[BIN1128](binomial-pencil-primitivity-review-swarmHQ-sol56-root-20261020T115104Z.md)
is the coprime binomial special case. The two-bad-fiber theorem adds
independence; it does not replace the polynomial/dependent-numerator
cases of [ONEBAD](one-bad-fiber-review-swarmHQ-sol56-root-20261018T211903Z.md).

Neither the producer nor the review constructs a suitable f or a
compositeness relation from a nonempty normalization boundary.
No genus-zero conclusion, arbitrary special-fiber irreducibility,
surjectivity, degree bound, B=R, counterexample or JC2 proof follows.
The normalization/boundary-to-pencil existence gap remains open.
Related historical homogeneous-pencil work was located, not exhaustively
compared. External novelty remains UNKNOWN; no novelty credit is claimed.

## Review custody

Reviewer: /root/normalization_fresh_selection_astra_2250, read-only.
Packet: prompts/two-bad-fiber-first-astra-20261020T133755Z.md in swarmHQ,
102 lines / 6330 bytes / regular0444,
SHA256 6d72d21a0bff8c0efb8e341688e785b31b6e9b6188c7d105efd918edfa72493f.
Frozen HQ STATE: 75df00d1a9f9a657b4eaf4bb2906c63b35a5987d:STATE.md,
200 lines / 15419 bytes,
SHA256 8776f99186836eb0742fa8d9e1362b79ac3d177b5f14243738ddf4b1e845d901.
Producer: 145 lines / 7058 bytes / regular0444,
SHA256 2564c37b525a92375bd934918765313dd395a799ceafc398543d7cb61e73c846.
Producer manifest: 1 line / 691 bytes / regular0444,
SHA256 536cdebd5d95b57045d766708105dab153cc8da4844cdc2c5397df7394152029.

The reviewer reported whole packet102, frozen STATE200, fresh producer145,
fresh ONEBAD114 and all three manifests. Its own complete identical-pin
BIN1128 report163 and governing-file reads were reused; public APPROACHES983
was included. Whole governing and six-object scientific metadata gates
preceded the bodies; manifests were first, and three authorized verifiers
returned VERIFIED. Required pre/post hashes, counts and modes agreed.
No reviewer deviations were reported. No writes, queries, network, new
external source, scientific code/CAS, model CLI, descendants or protected
access were used. Actual hosted model identity and costs remain unverified.
ROOT reverified the producer and read all145 lines before integration.

ACK13:40:00; substantive partial13:41:59 before13:43:20;
terminal13:43:16 before the original14:13:20 hard deadline.
These timings are event records, not renewed clocks.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6929`.
- Body SHA-256:
  `6704f1b55d88a18f89a032111d451ab3bd4b93e63c48d105be02d643886a1648`.
- Frozen basis: `274495802774139fee1cd64ca828bc7cef898675`.
