# Zero local slack forces an immersed image branch

Producer: swarmHQ ROOT. Date: 2026-10-31 UTC.
Tier: INTERNAL / MANUAL / ROOT-CHECKED / INDEPENDENTLY UNREVIEWED.
Basis: bef1638f1538ed865a3275a4bba365245fcf58cf (HQ).
This is a candidate local lemma and a conditional application to the retained Keller package.
It is not a proof of JC2, a global no-fold argument, or a novelty claim.

## Exact local algebra lemma
Let A=C[[s,t]], and let B be a normal local domain finite free over A of rank m.
Let f in A generate a height-one prime, and write D=A/(f), K=Frac(D).
Let P be a height-one prime of B over (f), with C=B/P a normal domain.
Write r for the ramification index at P and d=[Frac(C):K].
If m=r*d, then D is normal.
In the curve case at hand, this says that the selected plane branch f=0 is smooth.
No smoothness of the surface Spec(B), or Cartier property of P, is assumed.

## Proof
Localize A at (f), obtaining a DVR V with uniformizer f and residue field K.
The finite free algebra B tensor_A V has rank m over V.
Because B is normal, its local rings at the primes over (f) are DVRs.
The usual length decomposition can also be read directly from its special fibre:

    m = sum_(P_j over (f)) r_j * [Frac(B/P_j):K].                    (1)

Indeed the special fibre has K-dimension m; each local Artin factor has
residue field Frac(B/P_j) and length r_j, so its dimension is the displayed product.
Every summand is positive. Equality m=r*d therefore leaves only the prime P.
Thus the generic special fibre of B over f=0 is a local Artin K-algebra T,
with residue field L=Frac(C) and composition length r.

Let tau:B->A be the trace of the A-linear multiplication endomorphism of B.
This trace is defined because B is finite free; it is not a trace assumed on C[x,y].
Reduction modulo f and then passage to K commute with the matrix trace.
For any b in B, multiplication on the powers-of-maximal-ideal filtration of T
acts on its successive residue-field vector spaces by the image b_bar in L.
Additivity of trace across this finite filtration gives

    tau(b) mod f = r * Tr_(L/K)(b_bar) in K.                        (2)

If b is in P, the image b_bar is zero, and the right side vanishes.
Since D is a domain embedded in K, tau(b) lies in (f) in A.
Consequently trace induces a D-linear map lambda:C->D with generic formula (2).

Now take c in the integral closure D_tilde of D in K.
Under K subset L, c is integral over C as well, because its monic equation has
coefficients in D subset C. Normality of C therefore puts c in C.
Since c belongs to K, its field trace from L is d*c. Formula (2) gives

    lambda(c)=r*d*c=m*c in K, with lambda(c) in D.                  (3)

The nonzero integer m is invertible over C, so c belongs to D.
Hence D_tilde=D. This proves the lemma.
The characteristic-zero/rank-invertibility step is essential to this proof.

## Application to the actual finite Keller normalization
Use the retained finite map h:X->A2 containing the WHOLE Keller source U=A2.
The application assumes the adopted omitted-curve upgrade: each E_i is smooth,
not merely finite-bijectively normalized by A1; distinct E_i are disjoint.
This assumption is carried from FIBERREVIEW0210/public397632cb, not reproved here.
The all-Keller package supplies finite flatness and

    N-1 = sum_i r_i*delta_i + S,
    S = sum_(i,x in E_i) s_x,       s_x=m_x-r_i*t_x >= 0.            (4)

Here t_x is the LOCAL DEGREE of E_i -> D_i^nu, not the number of branches.
Fix x in E_i and the one image branch selected by E_i at h(x).
Complete the smooth target local ring and take the finite local block at x.
The target ring is A=C[[s,t]]. The source block B is a finite free local normal
A-algebra of rank m_x, where rank equals the local fibre length.
These are the standard completion and finite-flat local-block facts; normality
under completion uses excellence of the finite-type complex normal surface.
The image branch has a prime equation f. The completed E_i gives a prime P of B,
and B/P is C[[u]], since E_i is smooth. Its residue extension over Frac(A/(f))
has degree t_x: normalization of the selected branch identifies that field
with C((v)), and the local parameter v has order t_x in u.
The transverse index at P is r_i; other target branches do not alter it.

If s_x=0, then m_x=r_i*t_x, so the local lemma applies and A/(f) is normal.
A normal one-dimensional complete local plane-branch ring is a DVR, hence regular.
The selected image branch is therefore smooth, equivalently immersed.
This conclusion allows other image branches at the same target point.

The retained independently reviewed converse says that an immersed selected
image branch has cyclic local model (a,b)->(a^{r_i},b), so t_x=1,m_x=r_i.
Combining the two statements, at this exact adopted package scope,

    s_x=0  if and only if  the selected image branch is immersed.   (5)

Thus every nonimmersed selected branch has strictly positive integer slack.
If B_bad is the finite set of omitted points selecting nonimmersed branches,
then S>=#B_bad. Distinct omitted points, even over the same target value, count
separately. This is a necessary inequality, not a forcing of B_bad or S=0.

## Dependencies and limits
Fresh whole canonical reads: all-Keller sheet budget97LF and smooth-branch
localization95LF, both sealed and equal to their frozen public88ce078b blobs.
Their canonical paths are xmodel/all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md
and xmodel/smooth-branch-slack-irreducible-image-swarmHQ-root-astra-sol56-20261026.md
in /home/ubuntu/jc2. The latter provides only the converse in (5), not this trace proof.
The current STATE's accepted smooth-E package is an explicit inherited premise.
No fresh source-proof audit of that premise or analytic cyclic-cover foundations is claimed.
The local lemma itself needs only its stated algebra hypotheses and the elementary trace calculation.
No polynomial inverse, properness, global trace extension, smooth X, boundary Cartierness,
single image component, or missing-value configuration is inferred.
No CAS, new external source, or paid lane was used to produce this argument.
Independent hostile review is required before this candidate is adopted or published.

## COLLISIONS
Frozen history queries at HQbef1638f and public88ce078b retained all14 STATE archives.
The bounded check recovered the accepted smooth-branch implication; it is not a
novelty certificate or an exhaustive literature search. No old stopped body was opened.
The separate secant-idempotent proposal was closed as an exact prior criterion,
and supplies no input to this proof. No new OPEN or automatic successor is created.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6688`.
- Body SHA-256:
  `19156d603b1978f893788ab8177a3890135b9a28edfdba7bdd673e71ec3110fc`.
- Frozen basis: `bef1638f1538ed865a3275a4bba365245fcf58cf`.
