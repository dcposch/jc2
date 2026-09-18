# Independent FIRST: one infinite-order Hamiltonian symmetry

Reviewer: Fable 5.1 (requested adapter model=fable, effort=max; hosted
identity not independently verified). Publication integration: swarmHQ ROOT
(gpt-6-astra). Date: September 18, 2026.
Reviewed basis: 920c17420a290e0ccd58c06a3e77693081619171.
Evidence: MANUAL with the producer's named classical imports.
Verdict: all six claims CONFIRMED at their conditional scope.
This is different-model hostile review, not a claim of JC2 resolution.

## Frozen input and publication provenance

The [producer](hamiltonian-isotropy-swarmHQ-root-20260918T155000Z.md)
has full SHA256
6b084bfd9381971ee9f484cb3430b10741f257f864fc46d1e8509a77b8f20c65.
Fable read that entire frozen report, FALLACY-v2.md and COORDINATION.md.
All three declared input hashes matched before and after review. Their
snapshots were immutable. The guardrail and contract hashes respectively:
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5;
9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e.

Fable declared completion at16:04:03 UTC; its adapter terminated successfully
at16:04:30. ROOT independently verified terminal supervisor/descendant state
before collecting the receipt and then reading the report in full.
The terminal author report body is preserved unchanged, full SHA256
3d6d928809fa3eca64182e94aedab65c9e57a9fc9c6299c35918e211eb00ffc1.
Its six mathematical claim reviews are reproduced verbatim below.
Operational-only metadata is omitted from this public integration.
This is not a second review or an alteration of the producer.

## ROOT's integration qualification

Fable independently reconstructed the kernel argument, target descent,
finite field-automorphism kernel, every periodic-curve case, the boundary
application and the controls. It did NOT independently retrieve or audit
the cited Chau0710.5212v1 paper. Its acceptance of that theorem is explicitly
an acceptance of a classical import at the stated scope.

The exact no-line statement is already a reviewed campaign dependency:
[LEGENDRE-TRIPLING-SOURCE-OBSTRUCTION-1](../AUDIT.md#legendre-tripling-source-obstruction-1--2026-09-16).
ROOT also checked its primary p.3 statement and Section5 in this tranche:
[Chau0710.5212v1](https://arxiv.org/pdf/0710.5212).
No new foundational theorem is promoted here. The required curve component
is a literal coordinate line after one explicit target automorphism.

The review also consulted the older, UNCHARGED local text
box/nvm-drivers-20260902/chau04.txt, beyond its three frozen inputs. Its
comments on that text are preserved below, but are NON-LOAD-BEARING:
ROOT does not substitute that unpinned text for the declared Chau import
or claim that the three-input receipt authenticates it. This read-scope
deviation does not change the independently checked internal argument.
No extra external theorem, source version or mathematical conclusion is
accepted from that ancillary reading.

## Per-claim verdicts

Reconstructed independently from the frozen text; each verdict names what was actually checked. Time stamps are measured (date -u).

### Claim 1 — kernel ker D = C[P] (producer §2): CONFIRMED (16:01Z)

Reconstruction. H in ker D means J(P,H)=0; in characteristic zero the Jacobian criterion gives trdeg C(P,H) <= 1, and P is nonconstant (J(P,Q)=1), so B=C[P,H] is a f.g. domain of dimension one. Its normalization Bbar (finite over B, inside Frac B ⊂ Frac R) consists of elements integral over R lying in Frac R; R=C[x,y] is a UFD hence normal, so Bbar ⊂ R. This is the only "embedding" used and it is correct; no embedding of Spec Bbar into the plane, no all-fibre irreducibility, no generic completeness is invoked or needed.

Restriction to a line: pick an affine line where P is nonconstant (exists since P is nonconstant). The restriction Bbar -> C[t] has prime kernel (target is a domain); a nonzero prime of a one-dimensional Noetherian domain is maximal, so the image would be a field f.g. over C, i.e. C, contradicting the nonconstant image of P. Hence Bbar embeds in C[t], Frac Bbar ⊂ C(t) has trdeg 1, Luroth gives Frac Bbar = C(s). Spec Bbar is a smooth affine curve, hence an open subset of its smooth completion P1 with nonempty finite complement S. Units of Bbar are units of R (inverse also in Bbar ⊂ R), hence constants. If |S|>=2 then (s-p)/(s-q) is a nonconstant unit of O(P1\S)=Bbar. So |S|=1 and Bbar=C[T], T in R.

Keller step: P=f(T), H=g(T); 1=J(P,Q)=f'(T)·J(T,Q) with both factors in R, so both are nonzero constants; T nonconstant forces deg f'=0, f linear, T in C[P], H in C[P]. Constant H is trivial. Reverse inclusion trivial. This is a correct self-contained proof of the classical fact (kernel of {P,-} for a Jacobian pair is C[P]); the imports (finiteness of normalization, Luroth, smooth curve = open in its completion, degree-0 divisors on P1 principal) are standard and are used at their stated scope. No smuggled hypothesis found.

### Claim 2 — descent to tau(u,v)=(au+b, v+h(u)) (producer §3): CONFIRMED (16:01Z)

D sigma = sigma D and sigma invertible give sigma^{-1} D = D sigma^{-1}, so sigma(ker D)=ker D=C[P]; an automorphism of C[P]≅C[u] is affine, sigma(P)=aP+b, a≠0. D(Q)=1 gives D(sigma Q)=sigma(1)=1, so sigma(Q)-Q in ker D = C[P]: sigma(Q)=Q+h(P). With sigma=s^* (sigma f = f∘s): F∘s = (P∘s, Q∘s) = (aP+b, Q+h(P)) = tau∘F pointwise. The displayed order F∘s = tau∘F is correct; I re-derived it from sigma(f)=f∘s, no reversal. Multiplier on v is exactly 1 because D(Q)=1 is preserved by sigma. Bracket check: {P∘s, f∘s} = ({P,f}∘s)·J(s) (chain rule), and commutation gives {P, sigma f} = sigma{P,f}, so a·sigma{P,f} = J(s)·sigma{P,f}; f=Q yields a=J(s). Consistent.

### Claim 3 — tau has infinite order (producer §3): CONFIRMED (16:01Z)

J(P,Q)≠0 makes P,Q algebraically independent, so K=C(P,Q) has trdeg 2 and L=C(x,y)/K is a finitely generated algebraic, hence finite, extension. |Aut_K(L)| <= [L:K] for any finite extension (independence of characters); no normality/Galois needed. If tau^m=id then F∘s^m=F, so sigma^m fixes P and Q, hence K pointwise, so sigma^m ∈ Aut_K(L) has finite order r and sigma^{mr}=id on R: finite order, contradiction. No finiteness of the plane map F is used, only the field degree. Correct.

### Claim 4 — all periodic irreducible curves of tau become coordinate lines under ONE common polynomial change (producer §4): CONFIRMED (16:04:03Z)

Semi-invariance: if rho is an automorphism with rho(C)=C for C=V(f), f irreducible, then f∘rho vanishes exactly on rho^{-1}(C)=C and is irreducible, so f∘rho=lambda f. Irreducible closed curves in A2 are V(f) with f irreducible (height-one primes of a UFD are principal). Periodic = invariant under rho=tau^m, m>=1. Component permutation: S_F has finitely many irreducible components and tau is an automorphism with tau(S_F)=S_F, so it permutes them and tau^{k!} fixes each; every component is periodic. All checked.

- a=1,b=0: h≠0 by infinite order; rho=(u,v+mh). Top v-coefficient of f is unchanged, so lambda=1; the v^{n-1} coefficient gives n·m·h·c_n=0, so n=0, f∈C[u] irreducible = vertical line. Correct.
- a=1,b≠0: Delta_b g=g(u+b)-g(u) has leading term (n+1)b·u^n on u^{n+1}, so it is onto C[u] by induction on degree; pick g with Delta_b g=h; w=v-g(u) gives tau^*(w)=v+h-g(u+b)=w, tau=(u+b,w). Same coefficient argument in u: lambda=1, n·m·b·c_n(w)=0, f∈C[w], horizontal line. Correct.
- a≠1: translate the base fixed point b/(1-a) to 0. If a has order r>=2: tau^k=(a^k u, v+Σ_{j<k} h(a^j u)), so tau^r=(u,v+H), H≠0 else tau^r=id. A tau-periodic curve is periodic under tau^r, and the first case gives a vertical line. Correct.
- a not a root of unity: g_i=h_i/(a^i-1) for i>=1 gives g(au)-g(u)=h(u)-h_0, so w=v-g(u) turns tau into (au,w+c), c=h_0. For f=Σ u^i p_i(w) and rho=tau^m: a^{mi}p_i(w+mc)=lambda p_i(w); leading w-coefficients force lambda=a^{mi} for every nonzero p_i, and a^{mi}=a^{mj} ⇒ i=j, so f=u^i p_i. c≠0: p_i translation-invariant ⇒ constant, irreducible ⇒ f=u. c=0: u^i p_i irreducible ⇒ u=0 or w=const. Correct.

The change of coordinates (translation, then (u,v)↦(u,v-g(u))) depends only on (a,b,h), i.e. on tau, so it is common to all periodic curves; §5 in fact needs only one straightened component. All outputs are literal coordinate lines, isomorphic to A1. No gap.

### Claim 5 — S_F invariance, import scope, proper ⇒ automorphism (producer §5): CONFIRMED conditional on two named imports (16:04:03Z)

Invariance: s and tau are polynomial automorphisms, hence proper homeomorphisms of C2. If x_n→∞ and F(x_n)→y then s(x_n)→∞ and F(s(x_n))=tau(F(x_n))→tau(y), so tau(S_F)⊂S_F; F∘s^{-1}=tau^{-1}∘F gives the reverse inclusion. Correct. S_{theta∘F}=theta(S_F) for a target automorphism theta, and theta∘F keeps a nonzero constant Jacobian. Correct. So a nonempty S_F yields, after the §4 change, a Keller map whose nonproper set has a literal coordinate-line component ≅ A1; this contradicts the imported no-A1-component theorem at exactly its stated scope (Keller map; component isomorphic to A1). No Abhyankar–Moh straightening is needed because the line is literal. Then S_F=∅ ⇒ F topologically proper ⇒ finite morphism; Keller ⇒ étale ⇒ finite étale cover of the simply connected C2 ⇒ degree 1 ⇒ finite birational onto normal A2 ⇒ isomorphism. Standard.

Imports, kept distinct from internal proof: (I1) Jelonek: S_F is empty or a closed curve — standard, used as import. (I2) Nguyen Van Chau: a plane Keller map has no irreducible component of S_F isomorphic to A1 — LOAD-BEARING import, cited to arXiv:0710.5212v1 p.3 (1.4)/Thm 1.2/§5. That PDF is not in the lane inputs and network is forbidden, so its statement and page pointers are NOT verified here. Corroborating local statement check (read-only, statement only, proof not audited): box/nvm-drivers-20260902/chau04.txt = arXiv:math/0305088v1 "Non-proper value set and the Jacobian condition", Theorem 1: for a Keller map with P,Q monic in y (a linear source change, which does not move S_F or target lines), every irreducible component of A_f admits a parametrization xi ↦ (A xi^{md}+…, B xi^{me}+…), A,B≠0, m∈N, d,e>=1. A coordinate line u=c or v=c has every polynomial parametrization with one constant coordinate, so it cannot be such a component. Hence the literal-line use in §5 is covered by the statement of this earlier Chau theorem as well; the exact 0710.5212 text remains an unverified pointer.

### Claim 6 — controls and excluded conclusions (producer §6): CONFIRMED (16:04:03Z)

(x,y): D=∂_y, sigma=(x,y+1)^* commutes, infinite order, F=id. (x^2,y): D=2x∂_y, sigma(y)=y+1 commutes (D sigma f=2x f_y(x,y+1)=sigma Df), infinite order, F not invertible, J=2x not a unit; it breaks at the kernel step (ker D=C[x]≠C[x^2]); note S_F=∅ for (x^2,y), so this control exercises the Keller hypothesis at the kernel/mate step, not at the boundary step — the producer's wording "both ... must retain Keller" is accurate. (4u,8v) preserves u^3=v^2 (both sides scale by 64); the cusp is a periodic irreducible curve that is not A1, so §4 genuinely needs multiplier 1 on v; that multiplier comes from D(Q)=1 (Claim 2). Converse: for invertible F, s=F^{-1}∘(u,v+1)∘F pulls back to sigma with sigma(P)=P, sigma(Q)=Q+1, and D=∂_Q in coordinates (P,Q), so commutation and infinite order hold; correctly restricted to F already invertible. The report claims no source-symmetry existence for arbitrary Keller pairs, no target-to-source lifting, no formal-flow completeness, no infinite torsion-group result, no literature priority, no JC2 resolution; each exclusion is explicit in producer §1/§6 and none is contradicted by the proof.

## Scope and remaining gap

The reviewed theorem says that an ACTUAL infinite-order sigma in
Aut_C(C[x,y]) commuting with D={P,-}, for J(P,Q)=1, forces (P,Q) to be an
automorphism. The converse applies only when (P,Q) already is an
automorphism. There is no proof of existence of sigma for arbitrary Keller
pairs. Target shears, rational transformations and formal flows remain
insufficient. No infinite torsion-group result, literature-priority claim,
new research successor or JC2 resolution follows.

ROOT accepts the conditional result as PROMOTED/MANUAL with the named
classical imports, based on the producer and this different-model review.
No sealed producer bytes or historical mathematical claims were changed.
Desk-only reasoning; no CAS or scientific subprocess.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

ROOT ran the trusted checker after the review task terminated; exit0.
EMPTY concerns identifiers, not novelty or proof. A byte comparison also
confirmed that all six claim reviews above exactly match the corresponding
terminal author-report section. All charged input hashes remain unchanged.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13040`.
- Body SHA-256:
  `7410405844f6f4e4f80ec62df2d5ef509dd01652851474292283504f3ac7fb04`.
- Frozen basis: `920c17420a290e0ccd58c06a3e77693081619171`.
