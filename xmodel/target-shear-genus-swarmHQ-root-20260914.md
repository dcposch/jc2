# Target shears and generic genus: a conditional scope discriminator

Producer: swarmHQ ROOT (Astra), 2026-09-14. Basis:
db5f94168f1cf1eb6eb8b25b62961f94efbc1642.
Evidence: MANUAL, conditional on the explicitly assumed map and standard
finite-normalization, purity, Bertini and curve theorems below.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED. Native Astra independently checked
the hand argument and completed; this is not different-model FIRST.
No provisional root, dependent computation or promotion is selected.

## Result and scope

Suppose an actual noninvertible complex polynomial Keller map F=(p,q)
exists, of generic mapping degree d. After ONE generic determinant-one
linear target change, for each integer N>=2 the map

    G_N=(p+q^N,q)

has the same degree d, and its GENERIC inverse-line genus tends to infinity.
More precisely, there is an integer M>0 independent of N such that

    2*g_N-2 = N*M-d-s_N,       1<=s_N<=d.

Thus g_N=N*M/2+O_d(1). Each N has its own generic parameter set; this
asserts neither irreducibility nor a genus bound for every chosen fiber.
No actual counterexample or attained Keller family is produced. The
argument is a finite-cover calculation, not a new Keller-only restriction.

In particular, an upper bound depending only on mapping degree and valid
in EVERY polynomial target frame would already exclude all counterexamples.
This does not disprove such a bound: if JC2 is true its nonlinear case is
empty. A bound after selecting a minimal or specially normalized target
frame is a different problem, untouched here. No such bound is supplied.

## Derivation

Let A=C[p,q] and K=C(x,y); let pi:Y->Spec(A) be the finite normal
normalization in K. Its degree is d>1: a birational Keller map is an
automorphism, at the accepted classical tier. Let B be the reduced AFFINE
branch locus of pi, not the whole nonproperness divisor D of F.

B is nonempty. Otherwise normal-source/regular-target purity makes pi
finite etale everywhere; the connected finite etale covers of complex A2
are trivial, contradicting d>1. [Stacks, purity, Lemma58.21.4](https://stacks.math.columbia.edu/tag/0BMB)
applies at every point: finite dominant maps have equal local dimensions,
and absence of divisorial ramification supplies its codimension-one premise.
The standard complex covering comparison uses simply connected C2.

Write B=union B_i. Choose a generic SL2 frame (U,V) on the target, and
rename its pullbacks (p,q). Every defining polynomial b_i(U,V) then has
total degree m_i and a nonzero constant coefficient of U^m_i. Rescale to
make b_i monic in U. This is possible simultaneously for the finitely
many components by avoiding their finitely many top-form zero directions.
Write delta_i=d-c_i>0, where c_i is the number of cycles of generic
local inertia on the d sheets of pi. Set M=sum_i m_i*delta_i>0.

A general line in the new target is U+V^N+cV=t. Substituting
U=t-cV-V^N into b_i gives a polynomial in V of EXACT degree N*m_i:
the monomial U^m_i supplies its nonzero leading coefficient; for any other
U^a V^b with a+b<=m_i, N*a+b<N*m_i when N>=2. On each smooth B_i the
restricted function U+V^N+cV is nonconstant. Generic t avoids its finite
critical values and the images of the finite bad strata of the branch
cover; equivalently the graph meets B_i transversely at N*m_i good points.
Generic (c,t) also avoids intersections of branch components. No assumption
that B_i is rational, smooth everywhere or equal to a component of D with
only ramified missing sheets has entered this count.

The inverse graph C_{N,c,t} is smooth because G_N is Keller. It is
irreducible for generic (c,t): apply [Poonen--Slavov2001.08672v2,
Theorem1.5](https://arxiv.org/html/2001.08672v2) to the morphism
G_N:A2->A2 subset P2. The source is geometrically irreducible, the image
has dimension2, and all nonempty fibers have dimension0; the bad-line
locus has dimension at most1 in the two-dimensional dual plane.
This is a theorem-statement import, not a new proof of Bertini.

Also C[p+q^N,q]=A. The map q on the smooth projective completion
of C_{N,c,t} has degree d. The full finite-normalization restriction and
the affine-source curve have the same function field; finitely many
omitted points do not change this smooth completion. Generic parameters
avoid singular points of Y, whose images are finite, and all other
exceptional finite strata of the cover.

At a good graph intersection with B_i, tame transverse restriction gives
ramification contribution delta_i=sum(e-1) on ALL d sheets. There are no
other finite ramification values. If s_N is the number of places over
q=infinity, their contribution is d-s_N, with 1<=s_N<=d. Therefore
[Riemann--Hurwitz in characteristic zero](https://stacks.math.columbia.edu/tag/0C1B)
gives -2d+N*M+(d-s_N), the asserted formula. In particular s_N is NOT
the total number of points missing from the original affine curve:
omitted points over finite values remain in this compact-cover calculation.
Omitted index-one sheets contribute zero to ramification, not a new price.

## Hand controls and history

For the non-Keller finite map (x^2,y), M=1 and d=2. The curve
x^2+y^N+cy=t is hyperelliptic with s_N=gcd(2,N), giving
g_N=(N-gcd(2,N))/2. This checks the finite and infinity terms separately.
For an automorphism, B is empty, d=s_N=1, and every inverse line has
genus0, agreeing with M=0. These are exact hand checks, not CAS evidence.

The generic frame is essential: in the BAD fixed frame F=(x,y^2), the
curves x+y^(2N)+cy^2=t are graphs, all genus0. Here q is constant on
the branch line; the exact N*m_i intersection argument does not apply.

The September2 xmodel/keller-pencil-genus-opus5-20260902.md, sections2
and5, already gives the Riemann--Hurwitz bookkeeping and non-Keller shear
controls. Its controls retain their accepted historical scope. The present
conditional propagation from an assumed actual map is not an exhibited
counterexample. Targeted APP/AUDIT/PROGRESS/notes/REDUCTION and report
phrase searches found no identical statement, not an exhaustive priority
census. Primary reading covered the purity lemma statement/proof, the
Bertini paper's introduction and Theorem1.5, and the curve formula; no
whole-paper audit, raw PDF pin or broad-sweep completion is claimed.

No genus ceiling, chosen-frame minimization, new missing-source hypothesis,
construction, computation, exit price, or JC2 solution follows. This ends
the bounded target-shear discriminator; no genus/control family successor.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised OPEN entries.

Command: python3 ops/open_collision.py <this leased partial> --root .
Completed with exit0 before closure; this is not a mathematical review.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6756`.
- Body SHA-256:
  `ee95976b3c7c7ef1b1d7fca062e375032ba3670c17df51eb853944e1d0241ed3`.
- Frozen basis: `db5f94168f1cf1eb6eb8b25b62961f94efbc1642`.
