# Persistent cusp fibre hostile review

Status: PASS_CONDITIONAL
Reviewed UTC: 2026-10-31T06:41:46.200521+00:00
Task: persistent-cusp-fibre-review-sol56-20261031T0635Z
Reviewed candidate SHA-256: `3032f55329fba0294b8b6f07f8fc55bc1d2e7f63eef356e5b3cd1fc42699ffe7`
Public basis: `a12c5f367f87f599f1fd1cdf731eca3e7acdb596`
Reviewer configuration: gpt-5.6-sol / ultra; hosted identity UNVERIFIED.

## Verdict

PASS_CONDITIONAL. I found no fatal defect in the candidate's general argument or fixed degree-four application. The conclusion is conditional on the inherited affine-projective regularity and singular-branch persistence statement in PERSISTENCE, the finite-normalization/disjoint-omitted-curves/nonnegative-slack identity in BUDGET, and the reviewed degree-four algebra in COVER. I did not re-prove or freshly source-audit those foundations.

## Independent check

1. Common resolution and the singular point. The graph closure of the target birational map is already a graph over old affine space, and also over new affine space by regularity of the inverse there. Resolving outside the union of those smooth charts gives a common smooth projective surface whose projections are simultaneously isomorphisms over the two affine planes. The old projection factors into point blowups over old infinity. Because the projective closure of D is smooth there, its strict transform has exactly the original singular point z.

A ramified valuation over D stays ramified after extension to L by multiplicativity, so its centre in the actual Keller normalization is omitted and has image D'. Hence the inherited all-Keller package gives normalization A1 for the new affine image. If z mapped to new infinity, the new affine D' would be smooth; it would therefore be a closed embedded A1. Abhyankar-Moh rectifies it to a coordinate line. Composing with that polynomial automorphism preserves the nonzero constant Jacobian. A resolution supported over old infinity then leaves the singular point untouched but maps the strict curve properly and birationally to P1. Such a curve map is finite, and a finite birational morphism to normal P1 is an isomorphism, contradicting singularity. Thus z' is affine. The two graph charts give a local isomorphism at z,z', so D' is unibranch at z'.

2. Every point of the new fibre is ramified and omitted. On isomorphic target neighborhoods, normalization commutes with restriction, so the finite normal K-models are identified. Let C0 be that normal K-algebra and C the integral closure for L. For any point y of C over z', its contraction x0 in C0 lies, by hypothesis 3, on a ramified height-one prime P over D. Going-down for the finite integral extension C0 subset C gives a prime Q contained in y with Q intersect C0=P. Integrality and dimension make Q height one. The corresponding DVR indices satisfy e(Q/D')=e(Q/P)e(P/D)>1. Thus Q is an omitted divisor through y. This uses neither smoothness nor Cartierness of P.

If any omitted component has image containing z', finiteness supplies a point over z'. That point also lies on one of the ramified omitted components just constructed. Pairwise disjointness of omitted components forces the two components to be identical. Consequently every omitted component meeting the fibre has image D', and every fibre point lies on exactly one such component.

3. Fibre/slack calculation. Let I be those components. Since D' is unibranch at z', its normalization has one point above z'. For each i in I, the finite map of curve normalizations therefore satisfies

    sum_(x in E_i over z') t_x = delta_i.

Finite flatness of the actual normalization gives

    sum_(x over z') m_x = N.

All those points occur on the disjoint components in I, so the part of the nonnegative slack over z' is

    S_z' = N - sum_(i in I) r_i delta_i.

The inherited global identity then gives

    N-1 = sum_i r_i delta_i + S_total
        >= sum_i r_i delta_i + S_z'
         = N + sum_(i notin I) r_i delta_i >= N,

a contradiction. No component, branch, or local-length term is omitted.

4. Degree-four client. COVER proves that B=C[a,b,c]/(ac-b^2) is the normal finite flat rank-four model for P=a^2+b and Q=3c+12ab+8a^3; its unique reduced non-etale divisor E0=V(b,c) has generic e=3 and residue degree 1. The target-origin fibre is supported only at a=b=c=0, which lies on E0. The image Q^2-64P^3=0 is unibranch with affine normalization A1. Its projective closure has only the affine cusp singularity; at its unique infinity point [0:1:0], the Z-derivative is nonzero. Thus all candidate hypotheses hold. The older generic mass is only 3<4, while the proved fibre/slack contradiction applies. The complement remains A1 times G_m, so this is not a donor repair or an actual Keller construction.

## Scope and audit

This review establishes only the stated prescribed-cover obstruction, conditional on the named foundations. It makes no novelty claim, no general slack-invariance claim, and no JC2 conclusion.

Packet preflight and all four canonical input seals passed. Required reading was complete: non-STATE 2095/3000 LF (MANIFEST 253; nine governors 1342; ADMISSION 54; CANDIDATE 148; PERSISTENCE 104; BUDGET 97; COVER 97) and STATE 188/200 LF. Repeats: 0 LF. Report/ACK previews: 0 LF. Truncated or failed body windows credited: 0 LF. Every continuation used the reader-returned next_start. No web/source/history query, CAS/scientific computation, secondary model, Git action, helper/scratch file, automatic retry, or protected-tree access was used.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5540`.
- Body SHA-256:
  `9a248930cf0e71fe6bbd92898c6c092d8d57cee7839b521314b07a7d2b9699b0`.
- Frozen basis: `a12c5f367f87f599f1fd1cdf731eca3e7acdb596`.
