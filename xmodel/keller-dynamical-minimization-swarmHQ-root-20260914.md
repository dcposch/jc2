# Dynamical minimization: attained for Keller maps, not generally small

Producer swarmHQ ROOT (Astra), September14,2026.
Basis1c020ec21b75181883d3c75886716291d0c5607d.
MANUAL with named published imports; PROVISIONAL pending different-model
FIRST. No computation, novelty claim, actual counterexample to JC2 or
coordinate-search algorithm.

## 1. Normalized Keller dynamical degrees are integers

Let F:C^2->C^2 be polynomial, detDF=1, and let d be its generic mapping
degree. Write lambda=lambda1(F)=lim_n deg(F^n)^(1/n). Then

    lambda belongs to Z,     lambda >= d.

The lower bound is the already-promoted KELLER-DYNAMICAL-DEGREE-1,
with its named Dinh--Nguyen--Truong imports; its proof is not re-audited.
If lambda=1, integrality is immediate. Otherwise d<=lambda<lambda^2.
Import Favre--Jonsson (FJ), *Dynamical compactifications of C2*,
Proposition2.3: there is an eigenvaluation nu in V1 with F_bullet(nu)=nu
and d(F,nu)=lambda. Section1.3 gives finite thinness -2<=A(nu)<=0.
The normalized Jacobian identity, equation(5.2), gives

    A(nu) + nu(1) = lambda*A(nu).

Thus A(nu)=0. Section1.3 says irrational valuations have irrational
thinness, so nu is not irrational. Under precisely d<lambda^2,
Proposition2.5 then forces lambda to be an integer. This is not an
exclusion of zero-thinness divisorial or infinitely singular valuations.

Let Aut_1 be the determinant-one polynomial automorphisms. Every
alpha F beta with alpha,beta in Aut_1 remains normalized Keller with
generic degree d. Reapply the result, NOT invariance under independent
coordinate changes. The set

    { lambda1(alpha F beta) : alpha,beta in Aut_1 }

is nonempty and contained in Z_{>=d}; its infimum is attained by
well-ordering. Also beta (alpha F beta) beta^-1=beta alpha F, so allowing
both sides gives the same set as allowing a single left composition.
This last equality uses conjugacy invariance, unlike an independent
change. No bound on the degree of a minimizing automorphism follows.

## 2. General polynomial maps need not minimize to mapping degree

This is ONE non-Keller control, not a proposed search family. Set
M(x,y)=(x^2*y,x*y). It is birational, with rational inverse
(u/v,v^2/u), but JM=x^2*y is not constant. For ALL polynomial
automorphisms alpha,beta (even without determinant restrictions),

    lambda1(alpha M beta) >= sqrt(2) > generic degree(M)=1.

Put f=alpha M beta. It contracts the distinct intersecting curves
beta^-1({x=0}) and beta^-1({y=0}) to alpha(0). If lambda1(f)=1,
its mapping degree is also1. FJ Propositions5.1--5.2 classify the two
possibilities: bounded degree growth gives an automorphism; unbounded
growth gives a polynomial conjugate of

    (u,v) -> (a*u+b, A(u)*v+B(u)),    a!=0.

An automorphism contracts no curve. Every irreducible curve contracted
by the displayed skew product must be a vertical line, since its first
coordinate is constant on that curve. Distinct vertical lines are
disjoint. Polynomial conjugacy preserves incidence, a contradiction.
This handles translations and arbitrary degrees, not just linear frames.

Pointwise lambda1(f)>1 alone would NOT give a strict infimum bound.
For the uniform gap, mapping degree1<lambda1(f)^2 permits FJ
Proposition2.5 and its proof: lambda1 is integral or is the spectral
radius of a nonnegative integral2x2 matrix. A reducible such matrix has
integral radius. For an irreducible matrix both off-diagonals are >=1.
If both diagonals vanish, radius=sqrt(b*c), hence >=sqrt2 when >1.
If either diagonal is nonzero, monotonicity of the Perron radius gives
at least (1+sqrt5)/2, by comparison with [[1,1],[1,0]] after a possible
simultaneous row/column permutation. Thus the conservative gap follows. No exact
infimum or minimizing frame for M is claimed.

## Evidence, controls and limits

- Primary FJ: Annals173(2011),211--249, DOI10.4007/annals.2011.173.1.6,
  https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n1-p06-p.pdf .
  Read selected section1.3 definitions, Propositions2.3/2.5 with the
  latter proof, the Jacobian formula in Proposition2.8 proof and(5.2),
  TheoremC/coordinate convention, Propositions5.1--5.2 and their printed
  proofs. Earlier Eigenvaluations and classification foundations remain
  named imports; no whole-paper proof audit.
- ROOT formulated the two tests. Separate native Astra tasks independently
  checked integrality/attainment and the M control; both completed before
  intake. Same-model checks are not different-model FIRST.
- Identity has lambda=d=1. H_m=(y,y^m-x), m>=2, has det1, d=1,
  lambda=m, but composing on the left by its polynomial inverse reaches1.
  Thus arbitrary frame values need not equal their attained minimum.
- Scoped APP/AUDIT/notes checks found the earlier A(nu)=0 observation
  and the promoted lower bound, not these exact minimization statements.
  No exhaustive priority claim. The old zero-thinness gap is unchanged.
- Integrality/attainment here is asserted only for det1, not for every
  constant multiplier by an unlicensed invariance argument. The M control
  has contracted curves, forbidden for Keller maps: it rejects a general
  degree-only minimization premise, not Keller-specific minimization.
- Neither result supplies a lowering step, minimum<=d, minimum<d for
  d>1, properness, inverse, complete scalar pair or a JC2 proof. A minimum
  exists; the missing decisive step is a genuinely Keller-specific bound
  or reduction. No automatic control/degree/valuation-family successor.

## COLLISIONS

Lexical check EMPTY: no explicitly raised OPEN entries. This is not a
novelty proof or a mathematical gate. Scoped history checks are above.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5652`.
- Body SHA-256:
  `edcb3bd34836a461772cbf4d3b3a7380e7e2fac273cef138c6dc233a2762c657`.
- Frozen basis: `1c020ec21b75181883d3c75886716291d0c5607d`.
