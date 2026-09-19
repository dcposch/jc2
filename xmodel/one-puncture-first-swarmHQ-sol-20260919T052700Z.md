# Independent FIRST: one-puncture target-repair exclusion

Reviewer: swarmHQ Sol, requested gpt-5.6-sol/high through the pinned
adapter; exact hosted identity is not independently attested.
Producer: swarmHQ ROOT/Astra. Evidence: MANUAL with named classical imports.
This is ROOT's structured integration of the completed hostile review,
not a verbatim transcript or a new same-model review.

## Frozen review and custody reconciliation

Reviewed publication commit: 2917d0d3605f76344be78d43955464ba7fdb5121.
The [producer](one-puncture-target-swarmHQ-root-20260919T051000Z.md)
has full SHA256
cbe728e340307c2ad926628a04ccb609d3a23e906debe7ecec9a9c4729caf362.
Sol read all six charged snapshots whole and checked unchanged pre/post
hashes. The other five pins were:

| Input | SHA256 |
| --- | --- |
| FALLACY-v2.md | e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5 |
| COORDINATION.md | 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e |
| README.md | 7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf |
| AGENTS.md | 31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f |
| APPROACHES.md | dc674ad6caaedcdc6887074bd4680d86a7332a62045102a7419fff84a34f357d |

The author declared completion September19 05:24:05 UTC; the external
process terminated successfully at05:24:29. ROOT established termination,
collected the receipt first, then read the whole raw review. Its unchanged
raw SHA256 is
72563e95704fe3b76b220510443951f10fc7e2dd39c5cba4134d70bb7b03d2e5.
All five groups are CONFIRMED with two binding exposition clarifications.
Neither clarification adds a hypothesis or changes the conclusion.

Sol flagged the difference between the publication/review commit above
and the producer's declared basis2f8bb48d64d431f96cad7c842ddfe38e61ad7452.
ROOT checked the actual Git objects: that basis is the publication
commit's parent, and the producer blob in the publication commit has
exactly the charged hash. The producer's manifest also verifies against
its declared pre-authoring basis. These are different provenance roles,
not mismatched evidence; no custody discrepancy remains. The raw review's
original wording is retained unchanged.

The terminal command/patch record shows the six complete snapshot reads,
an early incomplete draft and a saved partial finding. A full-body patch
format error was immediately repaired on the same authorized report.
Only the authorized acknowledgment/report appear in executed patches.
This is a scoped delivery audit, not an exhaustive filesystem audit.
No scientific code, network retrieval, protected-tree inspection or
delegation was used; no earlier different-model review was supplied.

## Five hostile checks and binding clarifications

1. **Distinct pencils and full affine curves: CONFIRMED.** With
   K=C(t), r_s=a_s/b_s and r_t=a_t/b_t in reduced form, the two rings

       R_s=K[x,y]/(q_s), q_s=a_s-t*b_s,
       R_t=K[u,v]/(q_t), q_t=a_t-t*b_t

   have fraction fields C(x,y), C(u,v) with separate K-embeddings.
   The reduced nonconstant-pencil equation is irreducible. Explicit
   binding clarification: work in the polynomial UFD K[x,y]; q_s is
   prime there and does not divide b_s. Thus the pencil identity

       b_s*q_t(H)=b_t(H)*q_s

   implies q_s divides q_t(H). This produces R_t -> R_s on FULL curves,
   including pencil base points. The producer already established this
   irreducibility and worked in this UFD; no extra primality assumption
   is being imposed. Dominance gives injective H* on fraction fields,
   with degree N=deg_gen(H). The identity of pencils makes it K-linear.
   Geometric integrality known on D(b_i) passes to the full curve via
   the injection R_i -> (R_i)_(b_i) and flat scalar extension.

2. **Normalization, completion and degree: CONFIRMED.** Mapping a monic
   integral equation over R_t gives B_t -> B_s for the finite integral
   closures in their respective fields. The affine normalized map is
   regular, not assumed finite. In characteristic zero the curves have
   smooth projective completions. The induced nonconstant PROJECTIVE
   map is finite, and is flat of rank N over its smooth target curve.
   This is the precise object in the producer's degree-preserving
   base-change sentence. That rank stays N after extension to Kbar;
   geometric integrality keeps the source and target integral. Do NOT
   apply finite-flat rank to the possibly nonfinite affine map.

3. **One source puncture: CONFIRMED.** On the geometric projective
   genus-one curves, Riemann--Hurwitz makes the finite map unramified.
   Every target point has N distinct preimages. The target affine
   boundary S_t is finite and nonempty, since a positive-dimensional
   affine integral curve is not projective. Regularity gives the
   correctly directed inclusion

       f^(-1)(S_t) subset S_s,
       N*|S_t| <= |S_s|=1.

   Hence N=1. The normalizations include all affine branches over target
   pencil base points; the proof does not discard them by passing to D(b_t).
   Neither affine properness nor a constant Jacobian was assumed.

4. **Fixed Weierstrass source, arbitrary birational target: CONFIRMED.**
   For every fixed a in C, the full generic curve y^2=x^3+a*x+t is
   smooth, with nonzero discriminant -16*(4*a^3+27*t^2). Its smooth
   projective cubic adds exactly O=[0:1:0]. For arbitrary birational
   tau, the target pencil r_t=r composed tau^(-1) has the transported
   genus-one, geometrically integral function field. Multiplication
   Phi_m preserves r and has inherited degree m^2. Therefore a
   polynomial H=tau composed Phi_m would satisfy the different-pencil
   lemma and force m^2=1, impossible for |m|>=2. One-sided V_m/m scaling
   is included. The ORIGINAL source is fixed; arbitrary rational source
   changes can alter its affine punctures and are not excluded.

5. **Controls and scope: CONFIRMED.** Identity is allowed at degree one.
   The map (x,y)->(x,y^2), with r=x, shows why the same conclusion fails
   for a genus-zero one-punctured source. Multiplication
   E minus E[m] -> E minus {O} has degree m^2 and m^2 source punctures;
   this is an abstract-curve scope control, not a plane Keller example.
   The old SAME-invariant theorem permits arbitrary nonempty affine
   boundaries and gives MATCHED conjugacy exclusion. This result instead
   compares DIFFERENT pencils using one puncture on the fixed source.

Classical imports remain the producer's named curve normalization,
smoothness/completion, projective extension/finiteness, regular-curve
flatness and scalar-extension degree facts, Riemann--Hurwitz, affine-
proper finiteness, and elliptic multiplication degree/torsion facts.
Sol did not reverify old division-polynomial back-coordinate integrality,
which is not needed for this proof. No classification or formal proof
certificate is claimed.

## ROOT integration and accepted endpoint

Accept ONE-PUNCTURE-TARGET-1 at the exact MANUAL scope above, with both
binding clarifications. A dominant polynomial plane map comparing two
geometrically integral genus-one pencils has degree one if its FULL
normalized affine source generic curve has exactly one puncture.
Consequently every birational target postcomposition of the fixed
original Weierstrass multiplication donor is nonpolynomial for |m|>=2.
No constant-Jacobian condition is required for this exclusion.

The older fixed-target integral-back criterion and the matched-conjugacy
theorem remain valid at their respective scopes. Combining these with
the new fixed-source statement does not exclude arbitrary simultaneous
rational changes at both ends. No invariant or one-puncture pencil for
an arbitrary Keller map is supplied. No donor family, construction,
global properness theorem, literature novelty or JC2 conclusion follows.

AUDIT.md owns promotion; the sealed producer and raw reviewer bytes stay
unchanged. No descendant or automatic construction reset is selected.
Integrity checks do not substitute for the mathematical proof.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8151`.
- Body SHA-256:
  `3f1036a987e1e12a0fcde94dac79cf3b60d8f55c12e1635b277335e72077fdea`.
- Frozen basis: `2917d0d3605f76344be78d43955464ba7fdb5121`.
