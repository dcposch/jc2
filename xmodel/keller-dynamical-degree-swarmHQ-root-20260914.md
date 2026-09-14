# Normalized Keller maps have dynamical degree at least mapping degree

Producer: swarmHQ ROOT (Astra), 2026-09-14.
Basis: 3bad66352ac2eb85af19a42f48ed8edd4dbafb46.
Status: MANUAL, named external theorem import; PROVISIONAL pending
different-model FIRST. No computational certificate or novelty claim.

## Exact claim

Let F:C^2 -> C^2 be polynomial with det DF identically c, where
0 < |c| <= 1. Write d=[C(x,y):C(F_1,F_2)] and
lambda_1(F)=lim_n deg(F^n)^(1/n). Then lambda_1(F) >= d.
In particular this applies to the normalized JC2 problem c=1.

## Named import and proof

Import Dinh--Nguyen--Truong, arXiv:1303.5992v1, Theorem1.1,
together with the equilibrium-measure property stated immediately before
it: for a dominant meromorphic map on a compact Kahler manifold with
topological degree strictly larger than the other dynamical degrees,
repelling periodic points equidistribute to a probability measure charging
no proper analytic subset. Their section5 defines repulsion using regular
orbits and eigenvalues of modulus strictly greater than one.

Extend F rationally to f:P^2 --> P^2. Nonzero Jacobian implies dominance;
generic degree is d. The three dynamical degrees are 1, lambda_1(F), d.
If d=1 the assertion follows from lambda_1(F)>=1. Otherwise suppose
d>lambda_1(F). The named import applies; affine properness or a holomorphic
compactification is not required. Its measure mu has mu(H_infinity)=0.
Choose a continuous nonnegative function supported in C^2 with positive
mu integral. Equidistribution then supplies an affine repelling periodic
point for some iterate. Since F maps all of C^2 into C^2, its entire orbit
is affine and the ordinary chain rule gives det D(F^n)=c^n.
Both eigenvalues cannot have modulus greater than one when |c^n|<=1.
This contradiction proves the claim.

## Scope and controls

- For every pair of polynomial automorphisms alpha,beta with determinant1,
  the same inequality holds for alpha composed with F composed with beta
  in the normalized case: it remains Keller, and its generic degree is d.
  This is a fresh application, NOT invariance of lambda_1 under independent
  source/target changes. Only conjugacy automatically preserves lambda_1.
- For d>1 the regime lambda_1(F)^2=d is consequently impossible in this
  normalized frame. More generally the interval sqrt(d)<=lambda_1(F)<d
  cannot occur. Equality lambda_1=d and lambda_1>d remain untouched.
- Identity: d=lambda_1=1. H_m=(y,y^m-x), m>=2: det DH_m=1,
  d=1 and deg H_m^n=m^n, so lambda_1=m. This checks that no upper
  dynamical-degree bound or automatic equality follows.
- Dropping constant Jacobian: F=(x^2,y^2) has d=4, lambda_1=2 and
  repelling fixed point(1,1) with differential diag(2,2).
- For |c|>1 the periodic determinant contradiction is unavailable.
  A target scaling can normalize c, but may change lambda_1. No unchanged-
  dynamical-degree claim under that normalization is made.

The theorem is a straightforward consequence of existing complex dynamics,
not a new proof of the imported theorem or an exhaustive priority claim.
It need not distinguish Keller maps from every rational volume-preserving
map. No opposite inequality, minimizing target frame, actual candidate,
properness, inverse construction, or JC2 conclusion is supplied.
No degree-bound reproof, solver, new control family, or dependent lane.

## Evidence and read scope

- Primary: https://arxiv.org/pdf/1303.5992v1 . Submitted March24,2013;
  retrieved PDF internally dated July25,2018. Do not identify these dates.
  Publisher bibliographic record: Indiana Univ. Math. J.64(6)(2015),
  1805--1828, https://www.iumj.indiana.edu/IUMJ/FULLTEXT/2015/64/5674 .
- Retained raw PDF and mechanically extracted text are in
  box/keller-dynamical-degree-gate-20260914/ under the dnt-1303.5992v1 stem.
- ROOT read introduction/Theorem1.1, dynamical-degree definitions and
  section5 regular-periodic definitions; native Astra also read the
  section3 inverse-branch statement and concluding section5 construction.
  Neither has independently audited every imported analytic argument.
- DNT's introduction identifies an incomplete lemma proof in the older
  Guedj argument. The claim here imports DNT's theorem, not that older
  lemma. No publisher-access bypass or claim against the corrected theorem.
- Scoped APP/AUDIT/notes searches and relevant xmodel filenames found no
  exact prior campaign statement. The September13 06:06 eigenvaluation
  record is a different zero-thinness/properness stop, not displaced by
  this necessary inequality. No broad-sweep completion credit.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4600`.
- Body SHA-256:
  `affc812d62019f2cd3a5dbb9a170d38dca2a985f3666c229cb63a0259e0bd8a2`.
- Frozen basis: `3bad66352ac2eb85af19a42f48ed8edd4dbafb46`.
