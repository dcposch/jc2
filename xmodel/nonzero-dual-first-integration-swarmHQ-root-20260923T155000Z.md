# Nonzero target-linear dual criterion: independent FIRST and binding integration

Coordinator/producer: swarmHQ (Codex / ROOT; hosted model identity unverified).
Independent reviewer: requested Fable5.1/max, Claude adapter; hosted identity unverified.
Date: September 23, 2026 UTC.
Basis: fdde29aeb2c304ec8459e28e5f64350ae8f35679.
Evidence tier: MANUAL with named classical imports.
Lifecycle: PROMOTED at the exact criterion below after the recorded FIRST.
Literature novelty: UNKNOWN.

## Decision and reviewed objects

For a complex polynomial Keller map F, set R=C[w1,w2] and A=C[F1,F2].
The [producer criterion](nonzero-dual-criterion-swarmHQ-root-20260923T154100Z.md)
is CONFIRMED:

    Hom_A(R,A) != 0  if and only if  F is a polynomial automorphism.

The map need only be nonzero and A-linear, not normalized, multiplicative or
differentially compatible. The proof is uniform in degree. This does NOT
construct that map for arbitrary F, and does NOT resolve JC2.

The reviewer attacked eight explicit interfaces and supplied the reasoning
below; all were CONFIRMED, with no GAP or REFUTED step. ROOT read the whole
terminal review and checked its scope against the producer. This is substantive
different-model proof review, not agreement inferred from a portfolio summary.

The immutable reviewed original has SHA256
13492b909b7fd3052e7c7ab1f343c9dce39fdbe6d47282a7f548fef0ee4466a4.
Only its section3 elementary criterion is admitted here, not its separate
derived-category calculation. The public producer report has full SHA256
9ade28ecb5ce5b2b03ec47f9fd39578bd904856f961c959cc0192592d29af075.
Its proof excerpt is byte-identical to that original section3 proof, with
SHA256 9ed601dbaff090d71245b5f2d84b067a3c1489ea4fa6c86a7ae92a08ff2409e0.
The unchanged public producer retains its historical UNPROMOTED header;
this later integration and the ledger provide its current lifecycle.

The independently authored review completed at15:45:45 UTC; its run ended
at15:46:00 with exit0/DONE. Exact process termination was established before
receipt-first collection; the complete raw report was then read and frozen
without changing its bytes. Raw report SHA256:
52b26c268b49706fb69b1100a26675deef492f4b4298119ee22f5ad291ccefcf.
Terminal receipt SHA256:
f5559208235ac3d92de97ffc13b1566584dbc075d2f5a91f468d1daa2ad24fa1.
The complete mathematical findings through excluded conclusions are preserved
verbatim below. Operational headers/paths are omitted from this public excerpt.
The excerpt's SHA256 is
dd0674d1d08fc333edbf0a6e1a2af97454570d2f6e7989ec6e46a413395076a5.

## Findings (independent derivation, then attacks)

Notation: J=det DF, a nonzero constant. A=C[F1,F2] in R=C[w1,w2], K=Frac(A), L=Frac(R), n=[L:K].

**1. Fields and generic extension.** dF1 wedge dF2 = J dw1 wedge dw2 is nonzero, so F1,F2 are
algebraically independent (a minimal relation P(F1,F2)=0 gives P_x(F)=P_y(F)=0 after wedging, so P is
constant). Hence A is a polynomial ring, K is purely transcendental of degree 2, and L/K is algebraic,
finitely generated, hence finite, and separable since char 0. Generic etaleness is not needed for this.
R tensor_A K is the localization S^{-1}R, S=A minus 0, which equals K[w1,w2] inside L; a domain that is
integral over a field is a field, and it contains w1,w2 and K, so it equals L. The extension
phi_K(r/s)=phi(r)/s is well defined by A-linearity (rs'=r's forces s'phi(r)=s phi(r')) and is nonzero
whenever phi is. CONFIRMED.

**2. Trace representation.** L/K finite separable gives a nondegenerate trace form, so every K-linear
functional L->K is Tr_{L/K}(c times -) for a unique c, and c is nonzero exactly when the functional is.
CONFIRMED (standard).

**3. Nonzero element of I, universal quantifier.** Write c=h/s with h,s in R, s nonzero (L=Frac(R));
h=cs is nonzero. For EVERY q in R the element sq lies in R, so Tr(hq)=Tr(c(sq))=phi_K(sq)=phi(sq) in A.
Thus h lies in I={h in R : Tr(hq) in A for all q in R}, derived from phi, not assumed. I is an R-ideal:
for r in R, Tr((rh)q)=Tr(h(rq)) with rq in R, and I is closed under sums. No finite set of generators
is used anywhere; every use of the defining condition quantifies over all q in R. CONFIRMED.

**4. Target derivations, trace commutation, product rule.** Define delta_1=(F2_y d_1 - F2_x d_2)/J and
delta_2=(-F1_y d_1 + F1_x d_2)/J with d_i=d/dw_i; direct substitution gives delta_j(F_k)=delta_jk. They
are polynomial-coefficient derivations of R (1/J is a constant), so they preserve R. On A they act as
the coordinate partials: delta_j(P(F1,F2))=P_{x_j}(F1,F2) in A. The change-of-frame matrix has
determinant 1/J, a unit, so they are an R-basis of Der_C(R) (not needed below). Extend delta_j to L by
the quotient rule; it maps K into K. Trace commutation: let N be the Galois closure of L/K. Since N/K
and N/L are separable, delta_j|_K and delta_j|_L each extend uniquely to N, and the two extensions
agree on K, hence coincide; call it D. For sigma in Gal(N/K), sigma D sigma^{-1} is a derivation of
N extending delta_j|_K, so it equals D. Tr_{L/K}(q) is the sum of the n K-embeddings tau of L into N,
each a restriction of some sigma, so D(Tr q)=sum tau(Dq)=Tr(delta_j q), and D(Tr q)=delta_j(Tr q)
because Tr q lies in K. For h in I and any q in R: Tr((delta_j h)q)=delta_j(Tr(hq))-Tr(h(delta_j q)).
The first term lies in delta_j(A) subset A; the second lies in A because delta_j q is in R and h is in
I. So delta_j h is in I for every h in I. CONFIRMED.

**5. Source frame and minimal degree.** Let E=d_i - sum_j (d_i F_j) delta_j. E kills F1 and F2, so
the vector (E w1, E w2) is in the kernel of DF, which is invertible over R (unit determinant); hence
E=0 and d_i = sum_j (d_i F_j) delta_j on R. For h in I, each delta_j h is in I and I is an R-ideal, so
d_i h is in I. Now take nonzero h in I of minimal total degree. If the degree were positive, some d_i h
would be nonzero (char 0: both partials zero forces a constant) of smaller degree, contradicting
minimality. So I contains a nonzero constant, a unit, and I=R; in particular Tr(q) in A for all q in R.
CONFIRMED. (This is the differential simplicity of C[w1,w2] in char 0; it genuinely requires I nonzero,
which is exactly what step 3 supplies from phi.)

**6. Integrality and finiteness.** For r in R every power r^k lies in R, so p_k=Tr(r^k) lies in A. Let
T^n+a_1 T^{n-1}+...+a_n be the characteristic polynomial of multiplication by r on L over K; its roots
in N are the conjugates of r with multiplicity [L:K(r)], and p_k is their k-th power sum. Newton's
identities p_k+a_1 p_{k-1}+...+a_{k-1}p_1+k a_k=0 (valid in any commutative ring) give, by induction on
k and division by k in C subset A, all a_k in A. Cayley-Hamilton (the minimal polynomial divides the
characteristic polynomial) gives a monic equation for r over A, so r is integral over A. Applying this
to w1 and w2, R=A[w1,w2] is a finitely generated A-module. CONFIRMED.

**7. Endpoint and converse.** The presentation R = A[W1,W2]/(F1(W)-x1, F2(W)-x2) with Jacobian
determinant J(W) a unit shows A->R is standard etale; with finiteness it is finite etale of degree n.
Named classical import (consumed, not newly source-audited by producer or reviewer): finite etale
covers of complex A^2 are trivial. Self-contained justification at standard covering-theory scope:
finiteness gives properness of F (each w_i satisfies a monic equation whose coefficients are
polynomials in the target coordinates, so preimages of compact sets are bounded and closed); J
nonzero everywhere makes F a local biholomorphism; a proper local homeomorphism of connected
manifolds is a finite-sheeted covering; C^2 is simply connected and the total space C^2 is connected,
so the covering has one sheet and F is a bijective local biholomorphism, hence injective. For a finite
etale map the fiber cardinality equals n, so n=1 and L=K. Then R sits inside K, is integral over the
normal ring A (a polynomial ring), hence R=A: w_i=G_i(F1,F2) with G polynomial, and G composed F=id,
so F is a polynomial automorphism. Converse: an automorphism has R=A, and the identity R->A is a
nonzero A-linear map (indeed a unital retraction). Both directions CONFIRMED.

**8. Scope.** The argument produces no phi: it is an equivalence whose both sides are false for a
hypothetical noninvertible Keller map (giving the necessary condition Hom_A(R,A)=0 there). It supplies
no positive existence, splitting, or vanishing premise and is not a JC2 proof. Characteristic zero is
used essentially at step 5 (differential simplicity fails: (w1^p) is stable under both partials in
char p), step 6 (division by k up to n) and step 7 (etale fundamental group). Brief essential check,
not a new family: over an algebraically closed field of characteristic p, F=(x+x^p, y) has J=1, R is
free over A=k[x+x^p,y] with basis 1,x,...,x^{p-1} (the Artin-Schreier polynomial T^p+T-u is
irreducible over k(u,y)), so Hom_A(R,A) is nonzero, yet F(x+c,y)=F(x,y) for the p-1 nonzero c with
c^p+c=0. So the criterion is FALSE in positive characteristic, and its restriction to complex
polynomial sources is correct and necessary. For non-polynomial source rings the endpoint and the
degree function are not available as written; no claim beyond R=C[w1,w2] is made or endorsed.
**Sections 1-2 are NOT needed.** The chain phi -> I -> I=R -> integrality -> finite etale -> automorphism
-> R=A -> identity retraction proves Hom_A(R,A) nonzero iff A in R splits iff F is an automorphism using
only section 3. The further equivalence with kappa=0 depends on sections 1-2 and is outside this
review; nothing in the criterion above consumes it.

**Attacks tried and failed.** (a) Making phi vanish on a generating set but not on R: irrelevant, the
universal condition is evaluated on all of R through sq. (b) A trace not preserved by delta_j:
excluded by the unique-extension argument on the Galois closure, no integral trace pairing assumed.
(c) I nonzero without phi: not claimed; steps 2-3 derive it. (d) Minimal-degree step in a ring without a
degree or in char p: correctly excluded by the stated scope. (e) Endpoint without finiteness: the
import needs the finite (proper) hypothesis, which step 6 supplies; an etale nonfinite map is exactly
the open problem and is not used. (f) Newton over a ring without 1/k: not the case here.

**Excluded conclusions preserved.** No existence of a nonzero A-linear map for any Keller map is
established; no derived splitting, no trace-kernel vanishing, no source-selection theorem, no
global no-go for trace or derived methods, no novelty verdict. The producer's open-immersion control
(Hom_A(A[1/p],A)=0) is consistent with the theorem but is not a Keller source and was not re-derived.

## Binding scope and evidence limitations

The promoted endpoint is the displayed nonzero-functional criterion ONLY.
No existence, vanishing, derived-extension splitting, new source-selection
theorem, or trace-method impossibility is established. The older trace-kernel
map has different arrows and is not a premise. Finite-cover triviality is a
named classical complex-plane import; neither producer nor reviewer performed
a fresh primary-source proof audit. The review's covering-theory explanation
retains its standard topological and normality facts. Sections1--2 of the
original calculation are not needed and remain outside this review.

The brief characteristic-p check locates excluded hypotheses; it is not a new
construction campaign. The proof does not concern arbitrary rational sources
or assert that a generic field trace is polynomial-valued. A nonzero functional
must supply a SINGLE nonzero trace multiplier valid on ALL of R.

Review delivery limitations are kept separate from mathematical scope. The
startup acknowledgment was late, and the reviewer mislocated the immutable
prompt, so did not provide its self-hash. The parent had pinned that prompt
before launch and rechecked it afterwards. The review abbreviates nine document
hashes in its manifest despite the request for full hashes; the producer's full
hash is stated, and parent full pre/post pins and the five charged snapshots
match. Hosted model identity is not independently attested beyond the
recorded request/runtime evidence.

The raw legacy report has a clean terminal body receipt but lacks the canonical
Body-bytes declaration, so standalone canonical seal verification fails. Its
bytes are retained unchanged; this newly finalized integration does NOT
retroactively certify the raw seal. The published mathematical excerpt and
its producer comparison are independently inspectable here. The excerpt
contains the proof attacks, not merely a verdict.

## Replay and remaining gap

Desk-only proof review; no CAS, numerical calculation, network retrieval or
independent primary-source search. Compare the exact proof excerpt and review
excerpt hashes with their frozen originals. Sealing checks custody, not truth.

The missing global implication is unchanged: produce a nonzero A-linear
functional R->A from the actual Keller source. This report does not prescribe
a repeated finite-moment, formal-Taylor or automatic-splitting experiment.
Any next attempt needs a genuinely changed argument at its recorded scope.

## OPENS RAISED

None. No new bounded experiment is claimed.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `fdde29aeb2c304ec8459e28e5f64350ae8f35679` (Git blobs only).

Whole-author readback completed at15:50:52 UTC; final documentary wording,
excerpt identity and unchanged producer/reviewer postpins checked at15:53:09 UTC
on September23,2026. No mathematical excerpt was altered. Author complete.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13685`.
- Body SHA-256:
  `8902d79b871196194d7932c1edbe58f4a73770d889e248e81fb1143d8c4b4000`.
- Frozen basis: `fdde29aeb2c304ec8459e28e5f64350ae8f35679`.
