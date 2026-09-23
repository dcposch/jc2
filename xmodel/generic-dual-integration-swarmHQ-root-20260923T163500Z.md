# Generic-dual finiteness: independent FIRST and binding integration

Producer and integrator: swarmHQ coordinator (Codex / ROOT).
Independent reviewer: requested Fable5.1/max; hosted identities unverified.
Date: September23,2026 UTC.
Basis: 23bab6301b2507fe00d30cebb38229f0283d4da6.
Evidence tier: MANUAL, elementary commutative algebra.
Lifecycle: PROMOTED at the exact statement below, after this independent FIRST.
Literature novelty UNKNOWN; no priority claim.

## Binding result

For an inclusion A subset R of commutative domains with the same identity,
A Noetherian and [Frac(R):Frac(A)] finite,

    Hom_A(R,A) != 0  if and only if  R is a finite A-module.

No finite-generation assumption on R is imposed. Normality, smoothness,
characteristic zero, separability, a Jacobian condition, and differential
compatibility are not needed for this algebra statement. The
[producer proof](generic-dual-finiteness-swarmHQ-root-20260923T162800Z.md)
constructs an injective A-linear map R->A^n from one given nonzero functional.
Noetherianity then yields finite generation. Conversely, finite module
generators allow a common denominator for a nonzero generic functional.

For actual complex polynomial Keller inclusions this gives exactly
[NONZERO-TARGET-DUAL-1](../AUDIT.md#nonzero-target-dual-1--2026-09-23)
by its already accepted finite-etale-complex-plane endpoint. The NEW result
is a shorter, more general finiteness proof, NOT a stronger Keller criterion.
It supplies no nonzero functional, properness premise, or JC2 proof.

## Binding scope and reviewer qualifications

All seven requested checks received independent detailed CONFIRMED verdicts;
no mathematical GAP was identified. The entire mathematical FIRST is retained
verbatim below. The producer's old UNPROMOTED header is preserved historically;
this later integration and its ledger entry establish promotion.

The review's phrase "sharpening" about equivalence does not assert a new
Keller conclusion: the former promoted criterion was already an equivalence.
An equivalent endpoint remains an eligible proof route; this review establishes
neither impossibility of a positive functional construction nor a theorem that
every successful method must use every Keller hypothesis. Its "full Keller
structure" sentence is strategic language, not a necessary-method theorem.

The requested single reduced non-domain example is checked. The reviewer also
added brief purely inseparable and non-Noetherian examples beyond that requested
control scope. These are retained as auxiliary reviewer observations, not separately
promoted construction results, new campaign families, or premises of the theorem.
No further control search or descendant follows.

The primitive algebra proof has no trace or characteristic-zero input. Only
the Keller corollary retains the existing finite-etale-complex-plane endpoint.
No arbitrary finite-domain-algebra automorphy assertion is made. No independent
source audit, derived-category comparison, or literature novelty claim is included.

## Complete mathematical FIRST — verbatim

## Verdicts

1. S^-1R = L and a K-basis inside R: CONFIRMED.
2. Nonzero phi localizes to nonzero lambda: CONFIRMED.
3. T A-valued, A-linear, injective by field multiplication, no trace: CONFIRMED.
4. Noetherian submodule step gives finite generation: CONFIRMED; the Noetherian hypothesis is load-bearing (necessity example below).
5. Converse with finite common denominator: CONFIRMED.
6. A x A[1/t] defeats removal of the generic-field (domain) premise: CONFIRMED.
7. Exactly the promoted Keller criterion via the inherited finite-etale endpoint, not stronger: CONFIRMED. Trace, differential simplicity and Newton identities are removed from the finiteness step only: CONFIRMED. No positive existence premise: CONFIRMED, with the sharpening that Hom_A(R,A)!=0 is EQUIVALENT to invertibility.

Overall: the elementary statement is PROVED at its exact scope (A Noetherian domain, R domain, [L:K] finite). No GAP, no REFUTED. Fit for PROMOTED/MANUAL as an elementary proof simplification; it is not progress on the missing positive premise.

## Independent reasoning

1. S=A\{0}. S^-1R is the subring {r/s} of L, contains K=S^-1A, and is a domain. Every z in L is algebraic over K since n<infinity. For nonzero z in S^-1R the minimal polynomial over K has nonzero constant term c_0 (irreducible, z!=0, domain), so z^-1=-c_0^-1(z^{m-1}+...+c_1) lies in K[z], a subring of S^-1R. Thus S^-1R is a field containing R, hence contains Frac(R)=L; equality. For any K-basis l_i=r_i/s_i of L, the elements b_i=s_i l_i lie in R and remain a basis. Finiteness of n is essential here (A=k, R=k[x] gives S^-1R=k[x]).

2. lambda(r/s)=phi(r)/s. Well defined: r/s=r'/s' in L means rs'=r's in R, so s'phi(r)=phi(rs')=phi(r's)=s phi(r'). Additivity and K-linearity follow identically. If phi(r)!=0 in A then lambda(r/1)=phi(r)!=0 in K because A->K is injective.

3. b_i r lies in R, so phi(b_i r) lies in A; A-linearity is inherited from phi. If r!=0 and phi(b_i r)=0 for all i, then for z=sum c_i b_i with c_i in K, K-linearity gives lambda(zr)=sum c_i lambda(b_i r)=0, so lambda vanishes on Lr. In the field L multiplication by r!=0 is a bijection, so Lr=L and lambda=0, contradiction. This is the nondegeneracy of (z,w)->lambda(zw) for ANY nonzero functional on a field: the kernel of lambda contains no nonzero ideal because L has none. No trace, separability or characteristic assumption enters. Purely inseparable check: A=F_p[t], R=F_p[t^{1/p}], trace identically zero, argument unchanged with phi=coefficient of 1.

4. R is isomorphic to T(R), a submodule of the Noetherian module A^n, hence finitely generated. Necessity of Noetherian (reviewer-side check, not a new family): A=union_m k[x,y/x^m], a non-Noetherian domain; R=A[1/x]=k[x,1/x,y]. Then K=L, n=1, and multiplication by y is a nonzero A-linear map R->A because y x^{-m} y^j=(y/x^m)y^j lies in A. Yet 1/x is not integral over A (a monic relation gives 1 in xA, but A/xA=k), so R is not finite. The failure is exactly step 4: yR is a non-finitely-generated submodule of A^1.

5. With generators r_1..r_m and d the product of the m denominators of lambda(r_j), d lambda(sum a_j r_j)=sum a_j d lambda(r_j) lies in A; only finitely many denominators are cleared. If lambda vanished on R then lambda(r/s)=lambda(r)/s would vanish on S^-1R=L, contradicting lambda!=0; d!=0 in the domain K keeps d lambda nonzero. A nonzero lambda exists since L is a nonzero finite-dimensional K-space. Legitimate.

6. A=k[t], R=A x A[1/t] with diagonal A: S^-1R=K x K, generic rank 2, R reduced, first projection nonzero and A-linear. If R were finite, its quotient R/(A x 0)=A[1/t] would be finite hence integral over A; a monic relation for 1/t times t^m gives 1 in tA, impossible. Correct. The proof breaks precisely at step 3: r=(0,1) has T(r)=0 because multiplication by r is not injective on K x K. So the domain premise is consumed exactly at the pairing step and cannot be weakened to "reduced of finite generic rank".

## Item 7: campaign implication

For a complex polynomial Keller map, A=C[F1,F2] is a polynomial ring (F1,F2 algebraically independent by the Jacobian condition), Noetherian; R=C[w1,w2] is a domain; L/K is algebraic (equal transcendence degree 2) and finitely generated, hence finite. The lemma applies: a nonzero A-linear R->A forces R finite over A. Since R is a finitely generated A-algebra, finite equals integral, which is the same intermediate the promoted proof reached through the trace ideal, Keller derivations and Newton identities. The inherited finite-etale-plane endpoint (promoted, not re-reviewed here) then gives automorphy. Same hypothesis, same endpoint, same conclusion: exactly the promoted criterion, not a stronger one.

Removed from the finiteness step: the trace pairing and its separability requirement, characteristic-zero differential simplicity, and Newton identities. Retained: the finite-etale endpoint, where characteristic zero and the topology of C^2 still enter.

Existence premise: none. Sharper: the lemma is an equivalence, and finite <=> invertible for Keller inclusions (invertible gives R=A; finite gives finite etale, hence automorphism). Therefore Hom_A(R,A)!=0 <=> F invertible, and for a hypothetical noninvertible Keller map Hom_A(R,A)=0 exactly. The producer's "missing implication" (construct a nonzero functional without assuming finiteness) is thus a restatement of JC2 for that map, not an independent premise; any general mechanism producing such functionals must use the full Keller structure. This matches the runbook's sufficient-versus-equivalent caution.

## Scope, imports, exclusions

Imported textbook facts: (i) a domain algebraic over a field is a field; (ii) submodules of finitely generated modules over a Noetherian ring are finitely generated. Campaign imports for item 7 only: algebraic independence of Keller components; the promoted finite-etale-plane endpoint. Excluded: any wider algebra statement without the Noetherian or domain hypotheses (both shown necessary); any existence, splitting, uniform-denominator or JC2 conclusion; literature novelty (not searched). No exit-price assertion; no charge_basis line.


## Custody and read limitations

The frozen completed producer supplied to the reviewer has full SHA256
262bfbe318acc2d8880378397d986e620e6e1424401498fb3ffd7376edbedb4a.
The public producer's statement, proof and scope check are an unchanged
2617-character excerpt of that input. Public producer full SHA256
e3480c332fc516fbdb01fd22463c66abe150c1b9b7835bab82632938f9e12af3,
6259bytes, with independently verified transactional manifest
d2018e9ddc35cdefdc71b88dd73715a745d7b7b23337de4d2ab4d5599bea74ea.

The terminal raw FIRST has full SHA256
ed99972f99060ea8fc23d55dbc448f68084ba5519045c47dd4f6c83d2fe25751,
8786bytes; its complete mathematical portion is reproduced above.
The corresponding terminal receipt SHA256 is
daf550686dc3a475ca7c285a6d664e6994f01f8ff1dfc2c5f61d9be26d93b4cd.
The raw report has a clean final body marker and legacy receipt BODY_SEALED,
but canonical seal verification is INVALID (missing Body bytes declaration).
No raw bytes were rewritten or a seal retrofitted. After exact writer
termination and receipt-first collection, the raw report/log/receipt were
made read-only with unchanged hashes. This canonical integration is a separate
transactionally finalized artifact; custody alone does not certify mathematics.

The reviewer reports whole reads and matching full pre/post hashes for the
producer and all ten charged/documentary inputs. Parent postpins match.
The reviewer omitted the prompt selfhash; the parent independently pinned
the immutable prompt. Separate startup acknowledgment was captured in56.295s.
The initial draft and partial findings were reported saved before completion.
Known launcher warnings did not negate the separately observed protected
read-only masks; no tool repair or authentication reconfiguration was done.

No scientific computation, source retrieval, cloud allocation or mathematical
descendant was commissioned. Provider billing and hosted identity are not
independently attested. Operational details remain in the private workspace.

## OPENS RAISED

None. The unsupplied positive functional is not repackaged as a bounded test.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `23bab6301b2507fe00d30cebb38229f0283d4da6` (Git blobs only).

Whole-author readback completed September23,2026 16:36:31 UTC; full
mathematical FIRST excerpt compared unchanged. Terminal custody and input
postpins were checked before integration. Author complete.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11718`.
- Body SHA-256:
  `400fc8eb8f59151590e4912ac5bb667085b691dd7315d96b8a7cb75268788be1`.
- Frozen basis: `23bab6301b2507fe00d30cebb38229f0283d4da6`.
