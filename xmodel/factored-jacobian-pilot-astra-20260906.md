# Factored physical-Jacobian pilot: delta2 (99,66)

2026-09-06. Producer: Astra, /root/nonemptiness_certificate.
Evidence: exact Q construction, producer-checked; different-model review pending.
Result: CONSTRUCTION_ADVANTAGE_WITH_MONIC_H_LIFT; SOLVER_WIN_UNMEASURED.

A complete genuine Keller-locus presentation for this frozen source family was
built and serialized in 137.15 seconds, with peak RSS 1.71 GiB, on one newly
owned r7i.8xlarge. It has 600 variables, 1,629 equations and 11,299,180 literal
terms. The Jacobian equations have semantic degree at most 4, while the monic
source definitions have degree at most 12. This is neither a properness result
nor a JC2 counterexample. No solve, std, Gröbner, or msolve invocation occurred.

The unfactored-in-source variant is not the recommendation: just its low
physical-degree coefficients already have 32.7 million terms. The useful
representation change is the combination of the physical Jacobian identity,
the true degree-99 support cap, and monic variables for the nonconstant
coefficients of h.

## Frozen scope and physical reconstruction

The only source is
box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json,
SHA256 778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea.
Its worker copy has identical bytes. The frozen reference direct builder is
box/t2t3-direct-20260906/build_direct.py,
SHA256 77ef23b86f655e08a11913cf838a037c82adbb89cd1bc4a7e86c6471d034be3e.
The completed physical-realization gate is
xmodel/full-ideal-counterexample-gate-fable5-20260906.md,
SHA256 5fc61ae7f4f78e7d28cde6ac3eaa7c24e7ca98966ebf94de7cbaf5ea69fb059e.

Use X=x and W=y-x. This coordinate change has determinant +1, so it preserves
the Jacobian sign. A normalized source term (r,z,e), with normalizer N,
represents e X^(N-r-z) W^z. The normalizers for h3,C2,C3,B2,A3 are respectively
11,22,33,65,98. Every r+z is at most its normalizer. The exact polynomials are

    h = h3^3 + C2*h3 + C3
    D = physical(B2)
    C = physical(A3)
    F = h^3 + (3*D+a)*h/2 + C
    G = h^2 - b*h/3 + D
    a = target_a; b = target_b.

The source has residual_rows=[]; the exporter explicitly refuses a source with
nonempty residuals rather than omitting them. Coefficient parsing permits only
nonnegative integral powers and numerical denominators, never parameter
denominators. Thus this construction is over Q, with no hidden localization.

The source support audit gives min_r(B2)=31 and min_r(A3)=63. Consequently
deg D<=65-31=34 and deg C<=98-63=35, rather than 65 and 98.
Also deg h3=11, deg C2<=14, deg C3<=14; hence deg h=33.
Its fixed top part is y^9(y-x)^24, independently of source parameters.
The leading terms of F and G are therefore h_top^3 and h_top^2:
their degrees are exactly 99 and 66 at every source point.

There are 439 syntactically occurring physical-source coordinates.
Of the 444 declared free source coordinates, exactly Z55, leader55, target_c,
target_d and target_e do not occur in h,D,C,a,b. Removing these five is an
exact unused-factor removal: the physical family does not depend on them.
The T2/T3-specific added variables Zrho,t3eq,t3_fq,lambda3,Z3 are not
introduced. This raw physical family deliberately imposes no rho, leader55,
or lambda3 separation localizer. That enlarges the search relative to such
charts, but does not compromise the physical polynomial/degree implication.
It proves no necessity or chart coverage statement.

## Identity, support, and the exact ring map

With J(U,V)=U_X V_W-U_W V_X, direct differentiation gives

    J(F,G) = ((3*D+a+b*h)/2)*J(h,D)
             + (2*h-b/3)*J(C,h) + J(C,D).

Indeed dF=(3h^2+(3D+a)/2)dh+(3h/2)dD+dC and
dG=(2h-b/3)dh+dD. The coefficient of dh wedge dD is
3h^2+(3D+a)/2-(3h/2)(2h-b/3)=(3D+a+bh)/2.
This also fixes the order J(C,h), whose sign is easy to reverse.

The physical degree bounds of the four relevant products are 99 for
D*J(h,D), 99 for h*J(C,h), 98 for b*h*J(h,D), and 67 for J(C,D).
The remaining a and b terms are smaller. Thus degrees 100 through 163 vanish
identically before any T2 equations are imposed. The historical full 13,530-slot
triangular grid is not a list of 13,530 nonzero coefficient polynomials.

Exact construction of h gives 178 physical coefficients, 9,913 source terms,
maximum source degree 12. Exactly 160 coefficients are nonconstant in the
source variables. Introduce Hfact_i_j only for these 160 positions, and append
the 160 monic equations Hfact_i_j-h_source_i_j. Keep the other 18 constant
coefficients literal. In the quotient, the replacement polynomial H is exactly
h. There is no division in this graph extension.

If A is the polynomial ring in the 439 source variables, the map

    A[Hfact,Zj]/(Hfact_i_j-h_source_i_j) -> A[Zj]

sending every Hfact to its displayed source coefficient is an isomorphism.
Under it the exported positive Jacobian coefficients become the literal
physical coefficients of J(F,G). Including the one inverse row Zj*J0-1
therefore gives the same quotient as the full physical Jacobian ideal on this
source affine space. This is an exact graph-extension statement, not an
asserted equivalence to the T2/T3 ideal.

The complete support loop visits all 1,469 potentially nonzero physical
positions, including (0,0); all 1,469 are nonzero polynomials in the lifted
ring. A fixed modular source evaluation also makes all 1,469 nonzero and
agrees coefficient-by-coefficient with independently expanded physical F,G.
Together with the universal support computation this checks that no original
source coefficient is being counted merely because lifting removed a
source-specific cancellation. The generic polynomial identity above, not
that single modular evaluation, supplies the characteristic-zero equality.

The charged ideal has 1,468 positive-degree rows, 160 monic definitions, and
one inverse row: 1,629 total. There are 439+160+1=600 variables. Q and the exact
600-name order are explicit in both the JSONL header and complete_export.json;
the Singular order is global dp. The full J coefficients contain 11,289,124
terms including the 12-term J0. Replacing J0 by the 13-term inverse row and
adding 10,055 graph terms gives 11,299,180 terms. Maximum Jacobian degree is 4,
inverse degree 5, and ideal degree 12. These are not quadratic equations in
the original semantic variables.

Conditional on this ideal being proper over Q, a geometric point gives actual
polynomials with nonzero constant Jacobian and degrees 99,66. These degrees
cannot be a polynomial automorphism degree pair, since neither divides the
other. This conditional implication is the appropriate independent gate.
A unit result here would exclude only this source family, not resolve JC2.
Neither properness nor a point has been obtained.

## Measurements and the honest comparison

All substantive arithmetic ran on the allocated AWS worker. Times below are
payload build times; RSS is process high-water unless explicitly marked sampled.

| Representation / scope | Rows | Literal terms | Max semantic degree | Wall | Peak RSS |
|---|---:|---:|---:|---:|---:|
| Frozen exact T2 subset, incomplete | 466 | 6,448,959 | 34 | 1,192.235 s | 85.39 GiB |
| Unlifted exact J, physical degrees 0..20 only | 100 | 32,728,432 | 26 | 334.210 s | 2.22 GiB |
| Lifted full J, measurement only | 1,469 J + 160 definitions | 11,299,179 before inverse replacement | 12 | 105.226 s | 259.4 MiB |
| Complete lifted J ideal, literal export | 1,629 | 11,299,180 | 12 | 137.145 s | 1.71 GiB |

The frozen baseline is certificate-build.json in
box/t2t3-compressor-gate-20260906: 462 upper T2 rows, just one face row, and
three inverse rows. It is not full T2 or T2/T3, and its nonunit outcome is
inconclusive. Its largest row alone has 4,607,718 terms. The new complete
Jacobian presentation's largest J row has 30,218 terms at physical (8,52).
This is a scoped construction comparison, not a same-ideal solver benchmark.
There was no closed full-T2/T3 artifact available for a total-term baseline;
no extrapolated full count is charged here.

The unlifted full modular build hit its registered 600-second cap and was
cleanly terminated; it is INCOMPLETE, not a solver or emptiness verdict.
At the 100-row checkpoint it had already reached 32,728,432 terms.
Maximum sampled process-group RSS was 6,591,143,936 bytes.
No exact full unlifted construction was attempted after this preflight.

For the proposed T2-plus-low-J alternative, jets through physical degree 22
suffice for degree<=20 Jacobian rows because differentiation reduces total
degree by two and every physical input degree is nonnegative. The nominal
230 positive slots reduce to 99 nonzero positive coefficients in this source.
The scalar full/low streams agree on all 100 rows including J0. But the exact
low coefficients still have 32.7 million source terms, before retaining T2.
This variant offers no demonstrated term-count advantage.

The historical corrected engine
box/g9966-repair-gate-20260905/corrected_face_engine.py:479-503
builds expanded KF/KG before computing the Jacobian. The completed corrected
engine report records that earlier grid and zero-Jacobian survivor issue.
This pilot does not claim invention of the chain-rule identity; the implemented
difference is constructing h-coefficient graph variables and the factored
physical bracket before expanding semantic products.

## J0, exact controls, and serialization

J0 was extracted separately and checked against F_X(0)G_W(0)-F_W(0)G_X(0).
The h constant and linear jets were reconstructed independently from
h3,C2,C3 by the product rule and compared exactly with expanded h.
Substituting the origin Hfact variables into lifted J0 then agrees exactly with
the independent source expression: 45 terms, source degree 8.
See complete_export.J0.json; its own complete-file SHA is in custody.json.
The lifted J0 text SHA is
275d955b760e52bcea6a28923bdc6bc5134bd1b855da9016e225fd004fb53743;
the source J0 text SHA is
63b5edb9fadbf9dd1b530b51613e4732ab2f2c94e62b29f287d4d425cc079d30.

controls.py performs exact rational physical-polynomial checks: an affine
J=1 positive control; h=X,D=0,C=W giving J=-2X as a sign-negative control;
and h=X,D=W,C=0,a=2,b=6 giving J=3W/2+3X+1.
It also evaluates the frozen source at rho=1 and all other parameters zero.
There D=C=0, F=h^3, G=h^2, with exact degrees 99,66 and identically zero J.
Thus all positive J equations pass, while Zj*J0-1 is exactly -1. This meaningful
old-pass/new-fail control prevents omitting the constant-J inverse condition.

The exporter’s first rational-format regex was over-escaped and ineffective.
That completed producer file is preserved, not silently edited. The separate
check_serialization.py rejects an unsafe x^9/32768 control, wraps rational
coefficients, reparses every literal row exactly in FLINT, verifies its term
count and degree, verifies monic source-only definitions and the inverse J0
row, and checks the complete generator-stream footer. It emits
complete_checked.sing; this, not complete_export.sing, is the charged launch
input. Exact wrapping/reparse passed in 153.159 seconds, 118.1 MiB high-water.

Singular 4.3.2 parsed that entire Q/global-dp input with rc=0, no diagnostics,
and all four markers ALL_ROWS_PARSED, GENERATORS=1629, VARIABLES=600, END_PARSE.
Its only footer operations were printing these markers and quitting.
Parse-only wall was 97.385 seconds; sampled process-group RSS peaked at
15,588,319,232 bytes (14.52 GiB). Parsing is not solving.

The *.rows.tsv exact/modular row hashes are hashes of measurement strings
(term count and degree), not literal polynomial certificates. Scalar row
hashes do hash scalar values. The complete JSONL is the authoritative literal
polynomial stream, with separate whole-file and generator-substream hashes.

## Immutable delivery and custody

All arithmetic, export, checker, control and parse-only writers are DONE.
No producer task remains running. The one worker i-0da0cebfc97c9fd54,
172.30.0.56, r7i.8xlarge is retained under ROOT CUSTODY by explicit root approval,
superseding the initial terminate-before-seal rule. Its AWS Owner tag is now
coordinator-factored-jacobian-20260906. No pre-existing/protected worker was used.

Worker root: /home/ubuntu/factored-jacobian-pilot-20260906.
All listed worker files are read-only; the producer promises no further edits.
Root may now grant the independent gate a fresh reviewer scratch subtree,
reading the originals without using them as outputs. No solve is authorized
by this pilot. The full paths, bytes, 54 artifact hashes, terminal job states,
caps, and ownership transfer are in
box/factored-jacobian-pilot-20260906/custody.json, also copied to the worker.

Primary worker artifacts:

- complete_export.generators.jsonl: 432,003,707 bytes;
  SHA256 39ea3365c8c83916c5f813be0b7719374dcad131cdd4b10ed24d25516bfae75f.
- complete_checked.sing: 436,422,501 bytes;
  SHA256 50792efed4a5ed47cf2da5bf1f0d3b65e4f68efcba8e528b7dc29a541b72e091.
- custody.json:
  SHA256 f9000c9fb461b052b076d2cc60649b4bd312e36d2d59ebb91c364e12ac7c26d0.

Compact source code and terminal evidence are in the local owned box directory;
large polynomial streams were not copied to math-hq. Local payload remains
well below the 2 MB limit. The unchanged run_capped.py exact-PGID supervisor
enforced all caps. Its child-memory/timeout dummy and real modular timeout
both confirmed clean termination, not just a supervisor exit.

Replay in a fresh subtree on the retained worker, under the registered cap
wrapper and environment shown in REGISTRATION.md:

    python3 export_complete.py --mode exact --lift-h --out complete_export
    python3 check_serialization.py
    /usr/bin/Singular -q complete_checked.sing
    python3 controls.py

The latter two Python checkers expect their named source/evidence files in the
current scratch directory; copy inputs, never overwrite charged originals.
The scalar controls additionally use pilot.py with --mode scalar and --out
scalar_full, then --mode scalar --cap 20 --out scalar_low.

Stock msolve 0.10.1's known signed-32-bit exponent-offset guard fails:
11,299,180*600=6,779,508,000 > 2,147,483,647. Do not feed this into an unreviewed
stock msolve path or infer safety from the much cheaper construction.

Recommendation: independently gate this complete physical-J locus first, then
measure a separately authorized structured elimination or solver pilot.
No extension of the expensive unlifted expansion is justified by these data.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14490`.
- Body SHA-256:
  `ec33381a41a912c3fe76a457d56e3866d6a38988bbe908d6cae11a47a6e944d9`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
