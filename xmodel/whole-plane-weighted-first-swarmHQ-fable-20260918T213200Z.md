# Independent FIRST: whole-plane polynomial weighted derivative domain

Reviewer: Fable 5.1 (requested fable/max; hosted identity not independently exposed).
Integrator: swarmHQ ROOT (gpt-6-astra), September 18, 2026.
Reviewed producer commit: f81293f4157f4d3eba2fafabfe13106f04d9c431.
Evidence tier: MANUAL, independently reconstructed explicit example.
Lifecycle: completed FIRST; promotion is recorded separately in AUDIT.md.

## Scope and custody

[Producer](whole-plane-weighted-domain-swarmHQ-root-20260918T211200Z.md),
full SHA256 8b391dd29cd5f8623317dd063388787bfa6400f38d8e497f89ce99f4245c4a03.

For phi=|x|^2+|xy|^2+|xy^2-y|^2 on the WHOLE C^2 with STANDARD Lebesgue
measure, the maximal domain of ordinary partial_x is nondense in the
entire weighted L2 space. The weight is polynomial and strictly psh,
has finite total mass, and its complex-Hessian determinant is at least
1/2. The determinant is VARIABLE. This is not a Keller weight or a
JC2 counterexample.

The independent reviewer read all three immutable charged snapshots
WHOLE, with matching pre/post pins. ROOT confirmed authoritative
termination and absence of the original processes and service cgroup
BEFORE receipt-first collection and the whole review/log reads. Terminal
receipt: DONE/exit0, CLEAN/BODY_SEALED, all three inputs UNCHANGED.
Measured author completion21:28:09 UTC; terminal receipt21:28:33 UTC.
All original review deadlines were met. No live report/log/receipt read.

Preserved originals, unchanged after removal of write bits:

- Review SHA256: 0ce3a62b51cf330c1d41cfc9d1e1da60e3bd71deb961cb3da0075ebf8bc983c0
- Receipt SHA256: 4348df7ba1ae401ba85ba18480657807f8a0d17d4b694602959111d75aa3f13e
- Log SHA256: ad3678d7711b4b62e4f94d2896d26690f29c8d0e29e5e310b525501783c81346

The original external report is a receipt-bound BODY-END body, NOT a
report bearing a canonical post-body seal. Its legacy CLEAN/BODY_SEALED
receipt classification is not a successful canonical seal verification:
the latter correctly reported a missing Body-bytes declaration. No bytes
of that original were repaired or replaced. This separately authored
integration uses the normal close/finalize/verify publication transaction.

## ROOT integration and scope clarifications

All six charged groups survive independent hostile reconstruction.
The mathematical review from Claim1 through its FALLACY screen is copied
verbatim below. Original operational custody and later dependency/verdict
sections are summarized here; they are preserved in the original, not erased.

1. With Hessian entries indexed as partial_i partialbar_j phi, the
   displayed (JG)*JG must be transposed (equivalently conjugated).
   Both have the same determinant and eigenvalues. This convention
   clarification changes none of positivity, the lower bound or nondensity.
   Read the frozen producer's Gram statement with this indexing convention.
2. The determinant bound is attained at the stated point, not uniquely
   there. It is NOT a uniform positive matrix lower bound. The reviewer
   verifies degeneration of the least eigenvalue along the escape curve.
3. ROOT checked the derivative-domain definitions in the earlier
   [Keller criterion](holomorphic-domain-density-swarmHQ-root-20260918T192600Z.md)
   and its [binding FIRST](holomorphic-density-first-swarmHQ-fable-20260918T194700Z.md),
   with their unchanged hashes3611b6fa and30c01a21. Their weight is
   exp(-|F_1|^2-|F_2|^2) with detJF constant and their derivatives are
   the lifted target derivatives. In particular the complex-Hessian
   determinant of |F|^2 is constant. This example's determinant is
   nonconstant, and its derivatives are ordinary source partials.
   Thus the present example does not instantiate that theorem's
   hypotheses and supplies no noninvertible Keller map or contradiction.
   This contextual comparison is ROOT's check, not an unperformed
   linked-report audit by Fable.
4. Standard elementary imports are Cauchy's formula, holomorphic submean,
   Laurent/Parseval/Fubini removal and the usual Gaussian/Fock calculation.
   The reviewer supplies the joint-holomorphy detail and reconstructs all
   weight-specific calculations. No specialized global estimate or
   surface-classification theorem is imported.
5. Only the original charged countercontrol and its scope are promoted.
   Additional monomial-family observations in the review are consistency
   checks, not a new research family, independent theorem queue or source
   of descendants. No claim of mathematical novelty is made.

## Verbatim mathematical review

<!-- REVIEW-MATH-BEGIN -->
### Claim 1 (phi real polynomial, strictly psh; det >= 1/2 with equality at (1/2,1); variable) — CONFIRMED

Reconstruction. JG rows recomputed: (1,0), (y,x), (y^2,2xy-1). Two-row minors: rows 1,2 give x;
rows 1,3 give 2xy-1; rows 2,3 give y(2xy-1)-x y^2 = xy^2-y = y(xy-1). x=0 forces 2xy-1=-1, so the
first two minors never vanish together: rank JG = 2 everywhere, the Gram matrix is positive
definite, phi is strictly psh, and G is an immersion (also injective: x, then y from xy if x!=0,
else from c=-y). phi is a real polynomial of degree 6 in (x,y,xbar,ybar).
Conjugation convention: the matrix (d_i dbar_j phi) = sum_k d_iG_k conj(d_jG_k) is the transpose
(entrywise conjugate) of (JG)^*JG. Same determinant, same real spectrum. Benign.
Cauchy-Binet: Delta = |x|^2+|2p-1|^2+|y(p-1)|^2 with p=xy. AM-GM on the first and third terms:
|x|^2+|y(p-1)|^2 >= 2|x||y||p-1| = 2|p(p-1)|. With u=2p-1: ((u+1)/2)((u-1)/2) = (u^2-1)/4, checked.
|u|<=1: triangle inequality |u^2-1| >= 1-|u|^2 gives |u|^2+(1-|u|^2)/2 = (1+|u|^2)/2 >= 1/2.
|u|>=1: expression >= |u|^2 >= 1. So Delta >= 1/2 everywhere.
Equality: needs u=0 (p=1/2), triangle equality (automatic at u=0), and AM-GM equality
|x| = |y||p-1| = |y|/2 together with |x||y| = 1/2, hence |y|=1, |x|=1/2. The equality locus is the
circle {xy=1/2, |y|=1}; it contains (1/2,1), where Delta = 1/4+0+1/4 = 1/2. Delta(0,0)=1,
Delta(1,0)=2: variable. Non-properness: c(t,1/t) = t*t^-2 - t^-1 = 0, so phi(t,1/t) = |t|^2+1.
Distinction from a uniform matrix bound is PROVABLY necessary, not a hedge: along (t,1/t),
Delta = 1+|t|^2 while trace = |JG|_F^2 = 2+|t|^2+|t|^-2+|t|^-4 -> infinity, so
lambda_min <= 2 Delta/trace -> 0. The Hessian has no uniform positive lower bound.

### Claim 2 (H with standard Lebesgue measure; x-Gaussian completion; finite mass; c in H; y, y^2 not in H) — CONFIRMED

At fixed y, r=|y|^2: phi = |x|^2(1+r) + r|xy-1|^2 = A|x|^2 - 2r Re(xy) + r, A = 1+r+r^2.
Completing the square: A mubar = r y, so mu = ybar r/A (matches); A|mu|^2 = r^3/A; remainder
r - r^3/A = r(1+r)/A = (A-1)/A = 1-1/A = E_r in [0,1). The x-integral is (pi/A)exp(-E_r).
Angular integration: integral over C of f(|y|^2) dA(y) = pi * integral_0^inf f(r) dr, so the mass is
pi^2 integral_0^inf exp(-E_r)/A dr, finite (A >= 1, A ~ r^2). This is the GLOBAL mass: the fixed-y
integral runs over the whole x-plane and then over the whole y-plane; no chart is involved. 1 in H.
c = y^2 x - y is affine in x. Mean: y^2 mu - y = y(r^2 - A)/A = -y(1+r)/A (matches). Variance:
|y^2|^2/A = r^2/A (matches). E|c|^2 = r(1+r)^2/A^2 + r^2/A. r^2 <= A, and
A^2 - r(1+r)^2 = (1+2r+3r^2+2r^3+r^4) - (r+2r^2+r^3) = 1+r+r^2+r^3+r^4 > 0, so the bracket is <= 2 and
||c||^2 <= 2 * mass. c in H globally.
||y||^2 = pi^2 integral r exp(-E_r)/A dr, integrand ~ e^-1/r; ||y^2||^2 integrand -> e^-1. Both diverge.
d_x c = y^2 not in H, so c not in E_x. The report correctly refuses to infer nondensity from this.
Measure: dA(x)dA(y) is standard Lebesgue measure on C^2 = R^4. Confirmed.
Reviewer-derived consistency (not in the report): x, xy, x^n, c^n lie in H (bounded conditional
moments times 1/A); x*C[x,xy] is inside E_x; (xy)^b for b>=1 and c^n for n>=1 are not in E_x.

### Claim 3 (chart t=1/y, s=xy^2-y; Jacobian exactly 1; local L2 extension for EVERY h) — CONFIRMED

Inverse: y=1/t; s = xy^2-y gives x = (s+y)/y^2 = s t^2 + t. Jacobian matrix of (t,s)->(x,y):
[[1+2st, t^2], [-t^-2, 0]], determinant 0 - t^2(-t^-2) = 1 exactly. Real Jacobian |1|^2 = 1, so
dA(x)dA(y) = dA(t)dA(s) with no |t| power. Bijection {t!=0}xC <-> {y!=0}xC with this inverse.
Weight: x=t+st^2, xy=1+st, c=s, so Phi = |t+st^2|^2+|1+st|^2+|s|^2, a real polynomial smooth at t=0;
on a closed bidisc exp(-Phi) lies in [exp(-M),1] with M = max Phi there.
Local L2 for arbitrary h in H: integral over the punctured bidisc of |q|^2 dA(t)dA(s)
<= exp(M) integral |q|^2 exp(-Phi) = exp(M) integral over the image of |h|^2 exp(-phi) dA(x)dA(y)
<= exp(M) ||h||_H^2 (injective change of variables, Jacobian 1). No polynomial assumption.
Extension: a_k(s) = (2 pi i)^-1 contour integral over |t|=rho of q t^(-k-1) dt is holomorphic in s.
Parseval at fixed s: integral_{|t|<eps} |q|^2 dA(t) = 2 pi sum_k |a_k(s)|^2 integral_0^eps rho^(2k+1) drho,
infinite whenever a_k(s) != 0 for some k <= -1. Fubini: the inner integral is finite for a.e. s; a
nonzero holomorphic a_k is nonzero on an open dense set; contradiction, so a_k = 0 for all k <= -1.
Joint holomorphy of the extension (implicit in the report): Cauchy estimates
|a_k(s)| <= max_{|t|=rho,|s|<=R} |q| * rho^-k give uniform convergence of sum_{k>=0} a_k(s) t^k on
|t|<=rho/2, |s|<=R. Since eps and R are arbitrary, q extends to an ENTIRE function of (t,s) for
every h in H; y -> 1/t and y^2 -> 1/t^2 are correctly excluded (y, y^2 not in H). t=0 is not a
point of the source: auxiliary chart only, as stated. Confirmed.

### Claim 4 (maximal E_x; q_s = t^2 h_x pulled back; q(0,s) constant; disc containing 0 and 1) — CONFIRMED

Chain rule: d_s q = h_x * d_s x + h_y * d_s y = t^2 h_x(t+st^2, 1/t) + 0, because d_s y = 0 exactly.
For h in E_x, Claim 3 applies both to h and to h_x in H, so q and p := pullback of h_x extend across
t=0. d_s qtilde and t^2 ptilde are holomorphic on the full bidisc and agree on t!=0, hence
everywhere; at t=0, d_s qtilde(0,s) = 0. R is arbitrary, so any disc |s|<R with R>1 contains 0 and
1; in fact qtilde(0,.) is an entire function of s with zero derivative, constant on all of C.
The argument uses only h in H and h_x in H, which is the definition of the maximal domain E_x.

### Claim 5 (ell bounded on H; ell(E_x)=0; ell(c)=1; nondensity of the entire maximal domain) — CONFIRMED

qtilde(0,s_j) = (2 pi i)^-1 contour integral over |t|=rho of qtilde(t,s_j) dt/t, 0<rho<eps (Cauchy
formula in t at fixed s_j). On |t|=rho, qtilde = q = h composed with the chart, and the curve
theta -> (rho e^{i theta} + s_j rho^2 e^{2i theta}, rho^-1 e^{-i theta}) is a compact subset K_j of
the SOURCE C^2 (|y| = 1/rho). Submean on a polydisc of radius delta:
|h(z)|^2 <= (pi^2 delta^4)^-1 integral_{P(z,delta)} |h|^2 dA <= (pi^2 delta^4)^-1 exp(max phi on
the delta-neighbourhood) ||h||_H^2 for z in K_j. So |ell(h)| <= C ||h||_H with C depending only on
rho, delta, s_j in {0,1}. Linearity: pullback, Laurent extension and Cauchy integral are linear.
Bounded implies ker ell closed. ell(E_x)=0 by Claim 4. ell(c)=1: q_c = s by the definition of s,
so qtilde_c(0,s)=s. Hence closure(E_x) is inside ker ell, which excludes c: E_x is not dense in H.
E inside E_x gives E not dense. No boundary evaluation is used; the circles sit at |y|=1/rho in the
source. The report correctly separates this from the mere fact c not in E_x, which by itself
cannot give nondensity. Closedness of H in weighted L2 is standard and not needed for nondensity.
Reviewer cross-check: ell(x^a (xy)^b)=0 for a>=1 (these lie in E_x; pullback (t+st^2)^a(1+st)^b
vanishes at t=0); ell(xy)=0 although xy is not in E_x (allowed: ker ell may exceed closure(E_x));
ell(c^n)=1 for all n>=1 (c^n in H, not in E_x). No contradiction found.

### Claim 6 (Fock comparison; scope limits) — CONFIRMED as a scope statement

||x^a y^b||^2 = (pi a!)(pi b!) = pi^2 a! b! from integral_C |z|^{2a} exp(-|z|^2) dA = pi a!.
Monomials are orthogonal (angular integration), Taylor series converge in norm, polynomials are
dense, closed under d_x, d_y, and contained in the Fock space, so E is dense there. The failure is
weight-specific, not a formal artifact of the definition of E.
Scope limits verified from the supplied text: source is literally C^2 with standard Lebesgue
measure; weight is a real polynomial; G has THREE components into C^3, not a two-output Keller map;
det of the complex Hessian is variable (1, 2, 1/2 at three points) and nowhere claimed constant;
derivatives are ordinary d_x, d_y; the report claims no JC2 counterexample, no positive density
estimate, no completeness theorem. Classical geometry: a=x, b=xy, c=xy^2-y satisfy
ac = x(xy^2-y) = (xy)^2 - xy = b(b-1); the image misses exactly the line {a=0,b=1} (a=0 forces
b=xy=0), so "missing-line chart" is accurate. This affine geometry is not load-bearing and no
novelty is claimed for it. The comparison of a classical chart with a new domain calculation is
correctly not presented as novelty.

## Binding corrections

No mathematical REFUTED or GAP. No binding correction to any of the six exact claims.
The following remarks should travel with any promotion as scope notes, not as refutations:

- R1. Equality Delta = 1/2 holds on the whole circle {xy = 1/2, |y| = 1}, not only at (1/2,1).
  The report's single witness point is true; a reader must not infer uniqueness from it.
- R2. Hessian convention: (d_i dbar_j phi) is the transpose (entrywise conjugate) of (JG)^*JG as
  printed. Determinant and spectrum agree, so nothing in the argument depends on it.
- R3. The absence of a uniform matrix lower bound is a theorem for this weight, not merely an
  un-asserted possibility: along (t,1/t) as t -> 0, Delta -> 1 while the trace grows like |t|^-4,
  so the least eigenvalue tends to 0. The report's disclaimer (lines 60-61) is exactly right.
- R4. The chart extension is entire in (t,s) for every h in H, and qtilde(0,.) is constant on all of
  C for every h in E_x. The report's "any connected s-disc" is a weaker true statement; the disc
  containing 0 and 1 exists for every radius R > 1.
- R5. Joint holomorphy of the Laurent extension (uniform convergence through Cauchy estimates on
  the coefficients) is used at line 122 without being spelled out. Standard; recorded for
  completeness, not as a gap.
- R6. Line 94-95 says the norms of y and y^2 "contain" the displayed integrals; they EQUAL them.
  Wording only; the divergence conclusion is unaffected.

FALLACY-v2 screen: no exit claim, no charge_basis line required, no OPEN entry raised, no floor
treated as attainment (the determinant floor 1/2 is attained and the attainment set is exhibited),
no ring/variable map issue (the chart map and its inverse are declared with coefficient field C and
the Jacobian is computed, not inferred from names).

<!-- REVIEW-MATH-END -->

## Integration decision

CONFIRMED at the exact producer scope, with the harmless Hessian convention
made explicit above and reviewer notes R1--R6 retained. Evidence remains
MANUAL; the reviewer's later use of the word PROVED does not silently
change campaign evidence tiers. A continuous functional, not merely a
strict domain inclusion, proves the claimed nondensity.

The example rules out a generic shortcut using only whole-plane topology,
polynomial strict plurisubharmonicity, finite mass and a determinant floor.
It provides no positive density estimate for Keller weights, no completeness
or spectral theorem, and no JC2 counterexample or proof. It does not
alter the actual-source real Sobolev or holomorphic density results.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Administrative command: `python3 ops/open_collision.py <this partial report>
--root .`, terminal exit 0. No new exit-price assertion, computation or
automatic successor. The bounded
quantity and cheapest test were this exact weight's derivative-domain
density and a manual hostile reconstruction; both are complete.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15924`.
- Body SHA-256:
  `ab688a6ffc45f15063dc2a0bc296cab32de3b126a8f7fc70f52c3ab41f436a37`.
- Frozen basis: `f81293f4157f4d3eba2fafabfe13106f04d9c431`.
