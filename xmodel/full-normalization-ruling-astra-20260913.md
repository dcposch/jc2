# Full normalization: open plane chart versus coordinate ruling

Verdict: **NO_NEW_ACTUAL_SOURCE_CONSTRAINT / GAP.** The open-plane-chart implication is false even for a smooth affine surface with an affine-base A1-fibration. The explicit marked-chart countercontrol below does not satisfy the Keller condition. Manual co-research only; not a proper-block exclusion or promotion.

First action 2026-09-13 05:39:26.876716499 UTC. Original reserve05:58 / HARD06:01 UTC. The exact ruling implication, not ROOT's conditional coordinate-integrality endpoint, is the assigned question.

## History and exact question

The current full avenue snapshot separates actual full normalization from proper blocks, and qualitative ruling from a compatible coordinate. The old cubic one-place integration excludes the complete-base branch by a DEGREE-THREE sheet census; it is not an all-degree affine-base theorem. Its accepted scope is imported, not reverified. The pseudo-plane ML/equivariance check separately warns against automatic functoriality and remains at its recorded DOCUMENTARY/MANUAL, UNPROMOTED tier.

The cited primary paper distinguishes cylinder existence from an additive-group action having the same fibers; its example uses a projective-base ruling. Its class-group proposition has an extra torsion hypothesis. Neither statement supplies the marked-coordinate property needed here. [Dubouloz–Kishimoto, §1.1, printed385–387](https://www.numdam.org/item/10.24033/bsmf.2692.pdf).

For an actual hypothetical Keller map, the full-field normalization has a distinguished open embedding j:A2->Y. The required extra assertion is existence of h in O(Y) such that j^*h is a polynomial coordinate of THIS plane. The countercontrol addresses precisely whether the open chart and an affine ruling imply that assertion; it does not replace the actual Keller hypothesis by abstract rational domination.

## One exact smooth countercontrol

Let

    Y = Spec C[a,b,z]/(ab-z(z-1)(z-2)),
    j(u,v) = (a=u(uv-1), b=v(uv-2), z=uv).

Y is smooth: a singular point would have a=b=0 and a repeated root of z(z-1)(z-2), which has none. Put D1={b=0,z=1}, D2={a=0,z=2}. These are disjoint affine lines. The image of j is exactly U=Y minus(D1 union D2), and j:A2->U is an isomorphism, not merely dominant or etale.

Here are regular inverse formulas on an open cover of U:

    z!=1,2:           u=a/(z-1),           v=b/(z-2);
    b!=0, z!=2:       u=z(z-2)/b,          v=b/(z-2);
    a!=0, z!=1:       u=a/(z-1),           v=z(z-1)/a.

The surface equation checks every formula and their overlaps. They cover U; at z=1 its points have b!=0, and at z=2 they have a!=0. Conversely j avoids D1 and D2. Thus all scheme-theoretic chart claims are explicit.

Y DOES admit an affine-base A1-fibration, namely a:Y->A1. For a=c!=0 its fiber has free coordinate z and b=z(z-1)(z-2)/c. But D1 is horizontal for this ruling. Its restriction to U deletes z=1 from each such fiber, giving G_m, not A1. In source coordinates a=u^2v-u; its c!=0 fiber has u!=0 and v=(u+c)/u^2.

The following proves more than failure of that particular ruling: **NO nonconstant element of O(Y) pulls back to a polynomial coordinate of C[u,v].**

## All-functions obstruction, with no degree bound

Using ab=z(z-1)(z-2), every element of O(Y) has a unique finite normal form as a linear combination of

    z^j (j>=0),     a^i z^j,     b^i z^j (i>=1,j>=0).

Spanning follows by eliminating a factor ab. Independence also follows directly under j: the respective highest source monomials are

    u^j v^j,     u^(2i+j) v^(i+j),     u^(i+j) v^(2i+j).

These exponent pairs are pairwise distinct. Among terms of maximal total degree there can therefore be no cancellation; terms of smaller total degree cannot contribute at that degree. This also verifies independence without trusting a proposed normal form.

Every nonconstant basis monomial has highest term divisible by uv. Consequently every nonconstant H in j^*O(Y) has highest homogeneous part divisible by uv. For every scalar c, the projective equation of H-c then contains BOTH infinity points [1:0:0] and [0:1:0].

If H were a polynomial coordinate, H=c would be an irreducible embedded affine line. The polynomial parametrization supplied by the inverse plane automorphism extends to a morphism P1->P2. Its projective image is that curve's closure; all finite parameter values remain affine, so its infinity set is the image of the single parameter infinity, hence a SINGLE point. This contradicts the two displayed infinity points. No coordinate-degree classification, finite support envelope or computational enumeration was used.

## Source boundary and stop

The example even has a literal full-normalization presentation: the map (a,b):Y->A2 is finite, since z satisfies the monic equation z^3-3z^2+2z-ab=0. Y is normal and shares its function field with U, so it is the normalization of that target in the full field C(u,v). This follows directly: any element of that field integral over C[a,b] is also integral over O(Y), hence belongs to O(Y) by normality.

However, the induced source map has Jacobian

    J(u(uv-1), v(uv-2)) = (2uv-1)(2uv-2)-(uv)^2
                         = 3(uv)^2-6uv+2,

which vanishes on the two hyperbolas uv=1 plus or minus 1/sqrt(3). It is NOT Keller. Thus finiteness is present; the omitted condition is the etale constant-Jacobian source. This is a diagnostic of the missing hypothesis, not a low-degree frontier, hypothetical Keller counterexample, or reopening of any proper-block case.

Thus the first proposed shortcut fails: even smoothness, an actual open A2 chart, finite full normalization, and existence of an affine-base A1-fibration do not by themselves give a coordinate-pulling ruling. The still-missing arrow must use the everywhere nonzero constant Jacobian in an additional way; none is proved here. No conclusion about all actual Keller normalizations follows from this control. Separately, even the sufficiency of one arbitrary integral coordinate is left to ROOT's endpoint analysis, with its monicity/general-position qualifications; it is not assumed proved in this report.

The bounded quantity was existence of a coordinate in j^*O(Y) for the cheapest chart test. The exact normal-form/infinity argument decides it negatively for this ONE surface. It improves scope discrimination, not the global proof. STOP this open-chart-only inference; no surface family, Ga-action classification, degree successor or automatic new task is proposed.

## Provenance and custody scope

TASK and all307 lines of the changed APPROACHES snapshot were fresh WHOLE reads after hashes. COORDINATION is exact-byte personal WHOLE reuse from this agent's completed preceding task at05:09–05:14, with its current snapshot hash freshly matched; no summary-only substitution. The two newly selected history reports (cubic one-place integration and pseudo-plane ML/equivariance scope) were pinned then fresh WHOLE read. Filename-only searches of xmodel and the named canonical ledgers preceded derivation; a subsequent exact-formula search supplied no relied-on body. These are bounded checks, not exhaustive novelty evidence. No linked historic source, described computation, live peer, protected tree or mirror was read.

The sole substantive external text was Dubouloz–Kishimoto's published PDF, browser text of the opening through §1.1 (including Proposition2), with nearby supplied context. The whole22-page paper and its cited proofs were NOT audited; no downloaded raw bytes or SHA are claimed. Four targeted discovery queries were primary-host restricted; noisy/clipped search results supply no theorem premises. The primary text was accessed during the observed05:39:26–05:44:57 interval. Its generalities are not used to prove the explicit control. ROOT's concurrent notes cautioned about the unproved arbitrary-coordinate endpoint and independently suggested the natural finite projection; the displayed inverse, normal forms and Jacobian are checked directly here, not claimed as blind agreement.

No canonical OPEN, source computation, code, interpreter/CAS test, AWS activity, external publication or descendant. All authored bytes used apply_patch; Python was used only for the unchanged administrative finalizer. PINS and terminal custody bind exact read modes, source/output hashes, expected transaction and original clocks. No further action is authorized by this report.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8465`.
- Body SHA-256:
  `e950fc314e136dffe1162dd6034001819b0896f3e9e86071c2ae2611696d0baf`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
