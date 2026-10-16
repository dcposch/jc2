# Finite-moment countercontrol: independent review and binding scope

2026-10-16. This is ROOT's faithful record and integration of the terminal
native Sol5.6 review, not a claim that the reviewer authored this file.
Producer: swarmHQ ROOT. Independent requested model: gpt-5.6-sol.
Native handle: /root/finite_moment_review_sol56_0106.
Terminal verdict: ACCEPT, measured 2026-10-16 01:06:47 UTC.

## Exact reviewed artifact

[Producer proof](finite-moment-control-swarmHQ-root-20261016T010400Z.md),
152lines,6592bytes,mode444:

    full SHA256 657ed0acd9cbaffd14ab432b45c222814025130751236c90f99283f3fce4ce0f
    body bytes6260
    body SHA256 8f896a09a356ea80a2f74a0225df4bd53daa3708898fb1a09ff8c9f04090a404
    manifest bytes702,mode444
    manifest SHA256 b8f97e05c802b6eb29b76ab2ffb28fbae7e5209011ad659c62b2a6283a0e2e05
    frozen basis4f06b4425ca61f1827c4daf4d66fcfb198732425

The producer's historical MANUAL/UNREVIEWED header and sealed bytes are unchanged.
This integration, not editing that header, records the reviewed status below.

## Independent mathematical checks reported by Sol5.6

The reviewer accepted all five requested checks by independent manual reasoning:

1. The comaximal opens D(c),D(c-1) identify the three-relation affine scheme
   with C[g,p,(1+gp)^-1] and C[a,V,(aV^2-1)^-1]. Their overlap is exactly the
   stated gluing and they cover both original charts. These explicit local
   isomorphisms exclude hidden components or nilpotent scheme structure.
2. The monic relations c(c-1)^2-ap^2=0 and b^2-ac=0, followed by the integral
   element p over C[a,p^2], prove actual module-finiteness. The cubic relation
   aV^3-V-p is primitive/irreducible; its degree3 and the degree2 squaring map
   give degree6. The proof does not substitute generic degree for finiteness.
3. The polar part of H dV is independent of p, with sole logarithmic residue
   -L(R). If zero, integrating the other polar terms gives K in C[V], so the
   adjusted primitive is global. Conversely alpha-beta=dF on the affine-plane
   chart; restricting to p=0 leaves a regular pullback of beta and a Laurent
   derivative of zero residue, forcing L(R)=0.
4. The coefficient formula is L(U^r V^s)=1/(r+1) exactly at s=2r+1, otherwise0.
   The global element p has L(p)=-1/2, so the functional is nonzero. Every
   term of U^j p^(2i) has even V-exponent, incompatible with the required odd
   exponent. This covers ALL i,j>=0, including the constant moment.
5. Both Jacobians are correct: -2p(3UV^2-1) on the affine-plane chart, and
   -2pg(2+3pg) relative to dg wedge dp on the other chart. Ramification is
   not confined to D; it includes points of the affine-plane source open.

The strongest attempted falsifications challenged the residue converse at p=0
and hidden scheme structure. The regular pullback/residue argument and explicit
localization isomorphisms respectively survived. The reviewer also challenged
the generic-versus-finite distinction and cubic irreducibility; both survived.

The terminal permitted scope was explicitly the fixed marked surface Y and
finite map (p^2,U), with all polynomial moments zero and a NON-KELLER Jacobian.
No F10-face, constant-Jacobian, only-boundary-ramification, JC2, external-novelty,
family or successor assertion was accepted.

## Custody and review limitations

The reviewer reported nonsymlink ancestry and regular-file checks for the entire
report/manifest set before body reading, exact sizes/modes/hashes as above, and
successful artifact verification at the declared basis. It read the WHOLE
152-line report including seal and the whole one-line manifest. Postpins and
artifact verification at terminal01:06:47 were unchanged/VERIFIED.

Policy/context reads reported: HQ AGENTS, POLICY, RESEARCH_POLICY, STATE and
RUNBOOK120--195; public AGENTS, README, COORDINATION, FALLACY-v2, and
APPROACHES1--120. No linked Section4 mathematical source was read; historical
comparison and external novelty were not independently audited by this review.
ROOT separately read the September7 higher-moment report in full for comparison.

Two harmless command deviations were disclosed: extra probes for the post-basis
artifact at the older basis commit found it absent and printed empty-stream
hashes, which were NOT used as validation; a RUNBOOK read at the wrong workdir
failed and was repeated at the correct HQ path. Required actual artifact
verification passed. No file writes, CAS, external sources/models, children,
protected-tree access or auth/model execution occurred in the review lane.
An early DRAFT/INCOMPLETE message preceded the terminal synthesis. Native model
routing was requested explicitly; no independent provider-identity audit is claimed.

## Binding integration

Claim ID: FINITE-MOMENT-CARRIER-CONTROL-1.
Tier: MANUAL / PROMOTED after different-model hostile review, exact scope only.

Over C, the specified two-chart smooth affine surface contains X=A2 with
complement D=A1 and a regular form omega with simple zero divisor D. Its global
ring admits a nonzero exactness functional L. The algebraically independent
pair (p^2,U) defines a finite degree-six morphism Y->A2 and satisfies
L((p^2)^i U^j)=0 for every i,j>=0. Its Jacobian on X is nonconstant and has
zeros. Therefore finiteness plus those marked-carrier moment conditions does
not exclude such maps, force dependence, or recover the Keller condition.

This is NOT a Keller counterexample, full F10 solution/exclusion, source
properness/surjectivity theorem, or statement about every possible moment
method. Complete Jacobian constraints and their prescribed faces remain
essential untested hypotheses. External novelty UNKNOWN. No descendant or
additional family is licensed; the bounded sufficiency test is closed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5765`.
- Body SHA-256:
  `821da6ed0bb6d4b0536011ba898bbddc323a489203428a8009bd3e8a6e75ea07`.
- Frozen basis: `4f06b4425ca61f1827c4daf4d66fcfb198732425`.
