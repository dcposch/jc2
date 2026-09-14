# Actual-source weights: the boundary extension still has no vanishing input

Producer: swarmHQ Astra, native lane `/root/trace_weight_source`.
Evidence: MANUAL, with explicitly named standard Hodge-module inputs.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED; not different-model FIRST.
Verdict: KNOWN / NO_NEW_SOURCE_CONSTRAINT. JC2 remains unresolved.

First action: 2026-09-14 15:46:09 UTC. Research cap: 16:01:09 UTC;
sealing cap: 16:06:09 UTC. The history collision was found at 15:49:55
and mathematical search stopped then. No successor is proposed.
Frozen basis: `a6fe1fa95ab05e61af3e7bf9cf53744ae054f8fa`.

## 1. The exact class, before a proposed implication

Let F:X=A2_C -> Y=A2_C be an arbitrary polynomial Keller map. Work in
the algebraic mixed-Hodge-module category with rational coefficients.
Put P=F_* Q_X^H[2]. The affine etale direct-image calculation gives a
single perverse object: on the D-module side the relative transfer is
the etale one and affine direct image has no higher coherent direct
images. Its underlying D_Y-module is R=C[x,y], with the lifted target
derivations. In particular, this does not identify an ordinary stalk
with the cohomology of an ordinary fiber by proper base change.

Standard weight functoriality gives P weights >=2, NOT purity. Define

    I=W_2 P,       C=P/I,
    e=[0 -> I -> P -> C -> 0] in Ext^1_MHM(Y)(C,I).

Here I is pure of weight 2 and C has weights >=3. This is an actual
extension on the actual target, not a class on a selected compactification.
On the finite etale locus U=Y\D, I and P restrict to the permutation
variation L[2]. There are no boundary-supported subobjects of P:
etale pullback is perverse-exact, adjunction reduces such a subobject to
a morphism into the simple Q_X^H[2] from an object with smaller support.
Thus I is the intermediate extension of L[2]. Its pure decomposition is

    I = Q_Y^H[2] direct_sum IC_Y(L_0),

where L_0 is the generic trace-zero variation. This uses semisimplicity
only for the PURE object I, not for P. Equivalently the image of
F_! Q_X^H[2] -> P is I: weight bounds make that image pure of weight 2,
and it has full generic restriction with no boundary summand. The
inequality for F_! is weights <=2. Neither F_!=F_* nor a trace section
P -> Q_Y^H[2] is assumed.

The chosen cohomological discriminator is the connecting morphism

    delta_e: H^{-1}(Y,C) -> H^0(Y,I).

Source acyclicity gives H^{-1}(Y,P)=H^1(X,Q)=0 and
H^0(Y,P)=H^2(X,Q)=0. Therefore delta_e is an ISOMORPHISM, not a map
forced to be zero. Since H^0(Y,Q_Y^H[2])=H^2(Y,Q)=0, its target is
H^0(Y,IC_Y(L_0)). A closing argument would need a new restriction on
this specific extension, not merely source acyclicity.

The weights do not supply that restriction. A weight-3 boundary object
may contribute weight 2 in H^{-1}; the weight-2 core may contribute
weight 2 in H^0. Saito's Ext vanishing for pure weights m,n is under
m<n+j. At m=3,n=2,j=1 it says NOTHING: equality is the allowed
extension boundary. It is invalid to reverse that strict inequality or
to discard the cohomological degree shift.

No assertion is made that nonproperness by itself forces the displayed
H^{-1}(Y,C) to be nonzero in every Keller case. More importantly, even
if that implication were supplied, the source presently forces an
isomorphism, not a contradiction.

## 2. Relation to the existing trace-kernel obstruction

Write A=C[F_1,F_2], M=Tr(R), E=ker(R -> M). Accepted TRACE-IC-1 and
TRACE-SPLIT-1 already isolate the connecting map

    H^1_DR(M) -> H^2_DR(E).

Under their named IC/de-Rham comparison this is an isomorphism and the
groups have one generator per irreducible nonproperness component.
The residue representatives d d_i/d_i are boundary Tate classes, so a
compatible Hodge enhancement assigns weight 2 to the relevant classes.
This is compatible with, not contrary to, the lower bound on ordinary
cohomology of the trace-free subobject of P. No new mixed-Hodge
enhancement or stronger theorem is promoted by this report.

The actual target constant object maps INTO P by the unit. The generic
field trace instead extends naturally into the localization on Y\D;
its image need not be the constant object on Y. Confusing these two
extensions manufactures precisely the forbidden trace splitting.
Likewise, applying duality exchanges the ordinary and compact-supported
extensions and supplies no equality between them.

History already decided this lens: notes.md, September13 14:42, says
boundary Tate classes and kernel weights agree; September13 17:47
records the actual-source boundary Gysin isomorphism and explicitly
requires a new Keller-specific restriction on the extension; September14
05:48 rejects repetition of that screen. The new notation e and delta_e
does not change that decisive test. No all-degree proof dependency was
removed, and no new counterexample construction was obtained.

## 3. Existing negative control; no control-family successor

The already banked kernel report uses j:Gm x A1 -> A2 and the nonsplit
sequence 0 -> A -> A[1/p] -> A[1/p]/A -> 0. It is a genuine nonproper
etale direct image, whose generic trace pairing is perfect but whose
global ordinary extension is not semisimple or self-dual. Its smooth
boundary quotient has weight 3, while the constant subobject has
weight 2. Pure graded pieces therefore do not split this extension.
This is an existing control, not a new result or reproof. Its source
H^1 is nonzero, so it is NOT an A2-source counterexample to a proposed
Keller theorem. The source-A2 connecting isomorphism in section 1
already states the remaining distinction exactly.

The existing S/T chart in APPROACHES section 8 also warns that a
whole-plane etale source with smooth affine target is not enough if
the target is changed from A2 to the pseudo-plane S. That construction
is cited only as a scope warning; no new Hodge calculation or expanded
control family is claimed here.

## 4. Evidence and primary-source scope

Read before research: AGENTS.md, README.md, all COORDINATION.md, all
team/swarmHQ/README.md, all APPROACHES.md, and FALLACY-v2.md. Frozen
APP SHA256 `f27f0d1a8e8b09d93ba5473dd8609d8e15af125bfd73698a99b6b1f766ef832d`;
AUDIT SHA256 `bda4b17b6afb67a8408c2a461dc2fd44cc96d281dea1522c54392a993d92149a`.
Selected canonical history: AUDIT TRACE-IC-1/CUTOFF-1/SPLIT-1,
master inventory row 39, and the dated notes passages in section 2.
Searches were targeted, not an exhaustive repository census; large
initial discovery output was clipped, then selected instructions and
relevant mathematical passages were read in bounded complete chunks.

Terminal publication of both charged historical reports was already
recorded in the canonical intake. Expected-manifest verification was
run BEFORE reading either report, followed by WHOLE report reads:

- `xmodel/keller-trace-image-root-20260911.md`, full SHA256
  `76fa7291c32150f8728b704116fdc92171ad40bf4c468bddfb1f01e0bf55c025`;
  expected manifest
  `1b830d99313873580424ba0c0988c4271c35c5652574b01dd34460c42dc0981a`.
- `xmodel/keller-trace-kernel-astra-20260911.md`, full SHA256
  `7d943729d2ff5b101e38e015df006ab596651e3fea3d4915bdf01d9b45b6b2bd`;
  expected manifest
  `a7341650391685959a9faac21da1215e03bb8f562cefb860e62d48eb7046ea5d`.

Primary source: Morihiko Saito, *Mixed Hodge Modules*, Publ. RIMS 26
(1990), 221--333, [public author-paper copy](https://www.math.purdue.edu/~arapura/preprints/saito_mhm.pdf).
Selected text read: introduction/Theorem 0.1; Propositions 2.25--2.26
and their displayed proofs; (4.3.2)--(4.3.5), (4.4.1), and
(4.5.1)--(4.5.14). Imported facts are six-functor compatibility,
duality, weight inequalities, pure semisimplicity, and the displayed
Ext-vanishing range, not a properness or JC2 theorem. This was not a
whole-paper audit or a new verification of all its dependencies.

Browser PDF extraction refused the oversized file. Ordinary authenticated-
TLS public retrieval then succeeded without bypassing an access control;
pdftotext supplied the selected primary pages. The downloaded PDF is
`/tmp/jc2-trace-weight-source-20260914-QXgdUj/saito-mhm.pdf`, SHA256
`213a2c49fd83874c16c75a8ed8736c04a34969376401f89fc6b895301d302b8d`.
It is a temporary source copy, not a new permanent campaign artifact.
Other search results were discovery only; no theorem was imported from
their snippets. No stopped-channel access or broad-sweep credit.

## COLLISIONS

MANUAL collision check; no new machine OPEN identifier is raised.

- KNOWN: row 39 already required an explicit class before cohomological
  work. Section 1 supplies that class but no new vanishing premise.
- DUPLICATE: September13 14:42/17:47 and September14 05:48 already stop
  weight-only trace/boundary splitting. The same missing implication
  remains; notation and primary-source confirmation do not reopen it.
- SCOPE-CONFLICT: proper direct-image purity is unavailable for F;
  generic trace splitting is not global; nonzero kernel cohomology is
  not forbidden; neither the open-immersion nor pseudo-plane target
  control is a polynomial Keller counterexample on A2.

Decision: STOP this discriminator. No new scientific computation, CAS,
paid lane, AWS mutation, shared-ledger edit, nested-repository inspection,
review debt, or dependent lane. The general JC2 goal and genuinely new
source-specific Hodge methods remain open; this report is not a proof
that all such methods must fail.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9410`.
- Body SHA-256:
  `52f05cc071470c131a5c98d8c3327df2d648c3ab6b95201f79801d9e5416dfbc`.
- Frozen basis: `a6fe1fa95ab05e61af3e7bf9cf53744ae054f8fa`.
