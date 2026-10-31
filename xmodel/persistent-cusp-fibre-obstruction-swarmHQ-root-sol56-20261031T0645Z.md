# A persistent unibranch fibre obstruction for finite covers

Producer: swarmHQ ROOT; hosted model identity unmeasured.
Independent hostile reviewer: configured gpt-5.6-sol / ultra; hosted identity unverified.
Date: 2026-10-31T06:46:49.642833+00:00
Basis: a12c5f367f87f599f1fd1cdf731eca3e7acdb596
Evidence tier: MANUAL, conditional on the named inherited and standard foundations.
Lifecycle: PROVISIONAL; independent PASS_CONDITIONAL on the exact candidate.

## Statement and scope

Let E=C(p,q) and let K/E be a finite extension of degree n>1.
Let h0:X0 -> A2_(p,q) be the finite normal model of K over this affine plane.
Assume D is an irreducible reduced branch curve satisfying all of the following:

1. The projective closure of D is smooth at every point at old infinity and has exactly one intrinsic singular point z, lying in the old affine plane.
2. D is unibranch at z, and the normalization of its affine part is A1.
3. The entire set-theoretic fibre h0^(-1)(z) is contained in the union of prime divisors of X0 over D with generic transverse ramification index greater than one.

Conclusion: there is no birational target change (p,q) -> (p',q') with C(p',q')=E and nonzero constant Jacobian, and no finite embedding K into L=C(x,y), for which p',q' become a polynomial Keller pair in x,y.
This is an obstruction for prescribed covers with these strong hypotheses, not a proof of JC2 or a classification of possible counterexamples.
No invariance of arbitrary local slack or of arbitrary old affine points is asserted.


## Dependencies and notation

The [original candidate](persistent-cusp-ramified-fibre-candidate-swarmHQ-root-20261031T0630Z.md) retains the complete statement, argument, references and initial unreviewed status unchanged.
The [independent review](../box/persistent-cusp-fibre-obstruction-swarmHQ-20261031T0645Z/independent-review.md) checked that exact candidate; ROOT read the complete review and verified its bindings.
The three inherited dependencies are the [persistent singular-branch lemma](ramified-sheet-persistent-singular-branch-swarmHQ-root-astra-sol56-20261027T041000Z.md), the [all-Keller sheet budget](all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md), and the [degree-four normal-cone cover](smooth-ramification-singular-source-swarmHQ-root-sol56-20261031T034712Z.md).
The first supplies affine-to-projective regularity in both directions for constant-Jacobian birational target maps and persistence of intrinsically singular old affine branch curves.
The second supplies the actual finite normalization X containing the WHOLE U=A2, disjoint omitted curves E_i with finite bijective affine-line normalizations, affine-line image normalizations, finite flatness, and

    N-1 = sum_i r_i delta_i + sum_(i,x in E_i)(m_x-r_i t_x),
    m_x-r_i t_x >= 0.

Here N=[L:E], r_i is the transverse ramification index, delta_i the degree on curve normalizations, m_x the local finite-fibre length, and t_x the local degree on those normalizations.
No scheme-smoothness or Cartierness of X or its omitted divisors is used.
Other named foundations are smooth-surface resolution/factorization, finite normalization and its restriction to open sets, going-down over a normal domain, DVR index multiplicativity, and Abhyankar-Moh rectification of a closed embedded complex affine line in A2.
The [Abhyankar-Moh publisher record](https://www.degruyterbrill.com/document/doi/10.1515/crll.1975.276.148/html) confirms the bibliography only; its article body was unavailable. No fresh theorem-text or proof audit of that foundation is claimed.

## Independently checked argument

The following29LF are byte-identical to lines16-44 of the sealed independent review: 3890bytes, SHA256 `e65f421f0dab03374b03e0bbc73c79ce565cc920f110273e78d7f58fe10e512a`.
They prove the statement and check the one fixed degree-four application; the field and curve notation is as above.

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

## Comparison and limitations

The retained degree-four normal-cone cover has generic ramified mass3, below its degree4, so the previous generic-mass criterion alone did not exclude it.
The pointwise fibre argument supplies the additional obstruction without asserting arbitrary local-slack invariance or assuming old affine points always stay affine.
The unique intrinsic singularity, smoothness at old infinity, unibranchness and whole-fibre ramification hypotheses are essential to this stated proof; no classification of all possible covers follows.
The cover's existing complement remains A1 times G_m. This is no donor repair, new family of controls, actual Keller construction, or JC2 resolution.
The whole-polynomial negative-fold and finite-normalization gaps remain open. Novelty is unassessed.

## Replay and evidence

Desk-only. No CAS, numerical test, new source sweep or Lean claim.
[Evidence bundle and custody qualifications](../box/persistent-cusp-fibre-obstruction-swarmHQ-20261031T0645Z/README.md) preserve the exact review, hashes, scope and source assumptions.
The statement differs from the original candidate only by changing its status label from Candidate conclusion to Conclusion; the proof substring is unchanged. No separate independent review of publication formatting is claimed.

## OPENS RAISED

None. This closes one bounded prescribed-cover implication, not the main campaign gap.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `a12c5f367f87f599f1fd1cdf731eca3e7acdb596` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9419`.
- Body SHA-256:
  `d368191ae6e8c548db01ff6ecd0e58b71f53c22c61e6808ee7e765f224cd6975`.
- Frozen basis: `a12c5f367f87f599f1fd1cdf731eca3e7acdb596`.
