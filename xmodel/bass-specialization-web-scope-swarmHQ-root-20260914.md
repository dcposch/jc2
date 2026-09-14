# Bass specialization and two web-geometry scope checks

Producer: swarmHQ ROOT (gpt-6-astra), with native gpt-6-astra co-research.
September14,2026; basis2fa727465f267740a2dfa8de0b494a59dfd6e031.
Evidence MANUAL/DOCUMENTARY, lifecycle PRODUCER-CHECKED, UNPROMOTED.
Same-model checking is not different-model FIRST. JC2 is unresolved.

## 1. The actual-source question

Could specialization to a target line produce an Euler-annihilated source
section, contradicting Bass, using all-coordinate normalization and source
de Rham acyclicity? This is different from the already-zero horizontal
Reynolds transfer. The first required lifting arrow fails for every nonzero
ordinary specialization class: an explicit injection records its obstruction.
This stops this attempted selection, not every use of nearby cycles or Bass.

Let A=C[p,q] subset R=C[x,y] be an actual polynomial Keller inclusion,
N=R/A, and d=[C(x,y):C(p,q)]. Use the existing actual-source facts
R intersect C(p,q)=A and the inverse-Jacobian derivations D=D_p, E=D_q.
Consequently N embeds in C(x,y)/C(p,q) and is A-torsion-free. All products
below are multiplication by A; N is NOT treated as an R-algebra.

Choose an actual image point (a,b), put h=p-a and e=hD. Bass's imported
Theorem1.4 makes N torsion-free over C[e,(q-b)E]. In particular e and
therefore D are injective on N. This uses an image center, not an assumed
surjectivity of the Keller map. It remains valid in any polynomial target
coordinate frame with the same normalization.

## 2. Exact lifting obstruction

There is an exact sequence of C[q]<E>-modules

    0 -> N/hN --omega--> N/(e+1)N -> N/DN -> 0,
    omega([n])=[Dn].                                      (1)

Here D(hk)=k+hDk=(e+1)k, so the first map is well-defined. If
Dn=(e+1)k=D(hk), injectivity of D implies n=hk. Thus omega is injective.
The final quotient is exact since (e+1)N=D(hN) is contained in DN.
All operators involved commute with q and E, proving the stated module
compatibility. No characteristic-cycle index or finite-dimensionality is
used in (1).

The induced e on N/hN is ZERO, since eN is contained in hN; it is
well-defined because e(hk)=h(e+1)k. Nevertheless [n] lifts to an
e-annihilated section n-hk of N exactly when

    Dn in (e+1)N.                                        (2)

Indeed multiplication by h is injective on N, and e(n-hk)=0 is equivalent
to Dn=(e+1)k. By (1), (2) holds only for [n]=0. Thus the specialization's
Euler relations cannot be lifted for any of its nonzero classes. This is
an actual-source calculation, not an abstract countermodel to full JC2.

For a hypothetical d>1, the specialization is genuinely nonzero for generic
a. Choose p=a not contained in the nonproperness divisor; its generic point
lies in the degree-d finite-etale locus. There

    dim_C(q) ((N/hN) tensor_C[q] C(q)) = d-1 > 0.           (3)

For the quotient identification, A intersect hR=hA follows from
R intersect C(p,q)=A. Therefore A/hA embeds in R/hR and its cokernel is
N/hN. At the chosen generic point R/hR has dimension d and A/hA dimension1.
An actual image point on that line supplies b for the Bass normalization.
Nothing asserts a constant rank at every exceptional a or every q-value.

## 3. Why source acyclicity does not annihilate (1)

The polynomial source and target de Rham complexes have the same constant
H0 and no higher cohomology. Hence their quotient, the commuting D,E
complex of N, is acyclic. Since D is injective, this says precisely that
E is bijective on C=N/DN.

Explicitly, H2=0 gives N=DN+EN, so E is surjective on C. If En=Dm,
vanishing of H1 gives n=Dr and m=Er for some r, so [n]=0 in C and E is
injective. Thus H0_E(C)=H1_E(C)=0. The two-term E-cohomology long exact
sequence of (1) identifies the E-cohomology of N/hN with that of
N/(e+1)N; it does not force either to vanish.

In particular acyclicity supplies neither D-surjectivity on N nor
(e+1)-surjectivity. Finite algebraic monodromy supplies no constructed map
annihilating omega. An identification with a nearby-cycle object, followed
by lifting its eigenvectors into N, would itself need proof. No such
identification or positivity implication is charged here.

## 4. Controls and stopping interpretation

- For an actual automorphism, N=0 and every term of (1) is zero. The
  hypothetical d>1 assertion is not applied to this case.
- Drop the D-injectivity premise and use the ambient polynomial Weyl module
  M=C[p,q], D=partial_p, h=p-a. The nonzero class [1] in M/hM maps to
  [D1]=0, so the claimed injection fails. This checks the load-bearing Bass
  premise; M is not claimed to be R/A for a nonautomorphic Keller source.

QUANTITY: can a nonzero class in N/hN lift to an e-annihilated section of N?
CHEAPEST TEST: identities D(hk)=(e+1)k and (1), completed manually in this
bounded co-research pass, without CAS or a numerical/coefficient search.
Answer NO under the stated source/Bass premises. This is a failed proof
mechanism, not an exclusion of the hypothetical source itself. No new
canonical OPEN, operator enlargement, countermodel family or successor.

## 5. Independent web-geometry screen

ROOT separately asked whether polynomial source-line families could turn
local inverse branches into a global inverse through web-extension rigidity.
No such implication was obtained. Two primary theorem interfaces stop the
specific imports before a classification or computation is commissioned.

[Hwang1605.05018v1](https://arxiv.org/html/1605.05018v1), Theorem1.3,
requires pairwise non-integrability and bracket generation. Definition3.8
requires, for each line distribution W_i, another W_j such that W_i+W_j
is nonintegrable. On a smooth SURFACE two distinct line subbundles span the
whole tangent bundle, which is integrable. Thus this premise is impossible
for a surface web, not a consequence of an actual plane Keller map. A
one-direction web also fails the required existence of j. Moreover the
theorem's conclusion is a generically finite correspondence, not a
single-valued inverse. The line-preserving projective hypotheses in
Theorems1.1--1.2 are not supplied either. No stabilizing-dimension or
jet/web-family successor is selected.

[Bustinduy--Giraldo--Mucino-Raymundo2015](https://matmor.unam.mx/~muciray/investigacion/A-I-26.pdf),
printed205--206, main theorem: completeness of n-1 inverse vector fields
along typical fibers is a hypothesis for invertibility. At n=2 this still
requires a complete inverse flow on the selected fibers, not merely a
nonsingular polynomial field or a commuting frame. The introduction also
points out the classical plane one-fiber consequence. This supplies no
missing completeness property. The prior2014 fiber-integration paper in
the campaign journal is distinct; neither is a newly closing source import.

## 6. Provenance, coverage and custody

ROOT personally read the current README, COORDINATION, swarmHQ policy,
whole APPROACHES and FALLACY-v2, newest LIVE STATE, and current progress
opening. Existing source results are used at their recorded conditional
tiers, not re-proved or promoted. Both of the following reports were read
WHOLE before the calculation, with current full hashes:

- xmodel/coordinate-uniform-bass-discriminator-astra-20260913.md:
  8a8998eb360b1ec389e3cbe1ab789ce4324fc81cc80695d8072cec9de8021b8c.
- xmodel/kummer-coordinate-boundary-root-20260912.md:
  63a7a070b6c7aac67635729980021a2de68b24d6bf31e5ec7071ecc49db27139.

The first report retains the accepted source-field intersection, Bass
statement/normalization and source de Rham attachment. Bass's primary
proof was not re-audited this turn. Native Astra derived (1)--(3) and the
acyclicity limit message-only; ROOT checked the displayed proof, the
generic-line quotient identification and the two controls. Native author
completion is verified before publication. No different-model FIRST is
claimed and no downstream lane consumes these statements as promoted.

Scoped documentary searches covered canonical ledgers, ladder/REDUCTION
and xmodel reports for coordinate-uniform/Euler-specialization/nearby-cycle/
characteristic-cycle and web-geometry terms. Some broad outputs clipped;
they are not an exhaustive history or novelty census. The exact previously
stopped horizontal-transfer and fixed-frame Kummer paths above were read;
the old microlocal/vanishing-at-infinity records were located, not re-audited.
The present calculation is elementary and makes no literature-novelty claim.

Primary access September14 about17:17--17:22 UTC:

- Hwang: HTML abstract/introduction through rendered184, then displayed
  Definitions3.4,3.8 and surrounding section3; exact-version PDF1--4 also
  extracted/read. Not a whole-paper audit. PDF URL
  https://arxiv.org/pdf/1605.05018v1, SHA
  53867f6a81b3dd72f4b2b632d3badf13ae980ddbf74c9ea29464c618dee06025.
- Bustinduy et al.: downloaded PDF had no extractable text; ROOT visually
  read rendered PDF1--2, printed205--206. No later proof pages read. SHA
  3c98f3697b7dad8122e51df14296630cf8b16824f3f1fc82ca3f68f32d01d72e.

Both downloaded PDFs and the two rendered pages reside only in temporary
directory /tmp/jc2-web-geometry-20260914-JMzTwH; no durable source archive is
promised. Exact URLs/pins and read scopes are retained here. Broad query
results incidentally included social posts; none was opened or used. This
was targeted primary research, NOT a completed BROAD sweep. Stopped
Mathstodon/Palomar channels and the unauthenticated campaign queue were not
visited, and no access restriction was bypassed.

No scientific computation, paid adapter, worker launch, software change or
model-balance measurement occurred. Native usage is unmeasured. The two
mechanisms end in NO_NEW_CLOSING_TEST; source selection, normality and
unrestricted polynomial construction remain open. All46 ranks unchanged;
coalesce this scoped event as a micro-round, not another full ideation echo.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10016`.
- Body SHA-256:
  `34daecbd7bf679472553a69547ebc3c8a2c1a0912d19bf36710b024ae280bc01`.
- Frozen basis: `2fa727465f267740a2dfa8de0b494a59dfd6e031`.
