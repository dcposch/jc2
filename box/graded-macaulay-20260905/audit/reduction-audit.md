# Independent reduction and Hilbert audit

This audit consumes the six frozen charged inputs after mechanically joining receipt
`charged_input_<i>_sha256` and `_basename` fields with `awk` and obtaining six `OK`
results from `sha256sum -c`. The retained manifest and check log are adjacent to this
file. No new Gröbner computation, fleet action, ledger edit, or source-presentation
mutation was performed.

## Meaning of charge and the unit pivots

Use $B(z)=b$, $w(z)=iK-a$, $C=(p,D)=(\ell+1,D)$. Every original coefficient
generator has first charge at least one. Nonnegative grading therefore gives the
exact, N-independent statement

\[
I_{(0,Y)}=0\quad\text{for every }Y\ge0.
\]

The charge-zero coordinates are a polynomial subalgebra of $R/I$. In particular,
there cannot be a rational-unit chart equation solving one of them: a homogeneous
equation with such a linear term would have first charge zero. Setting those
coordinates to zero or to $t^{w(z)}$ is a specialization, not a quotient
isomorphism removing redundant coordinates.

The frozen 27 and 71 triangular pivots have **positive** charge. The exact pivot
charge histograms are:

| Fibre | B=1 | B=2 | B=3 | B=4 | B=5 | B=6 | Total | Remaining coordinates, including c |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 77 | 19 | 8 | 0 | 0 | 0 | 0 | 27 | 50 |
| 136 | 18 | 17 | 14 | 11 | 6 | 5 | 71 | 65 |

This matches `instrument/emit_triangular.py`: its selection is negative first
component in the older **signed** grading, which means positive B in the
current grading. The frozen DAGs explicitly name each pivot, its constant
coefficient, source row, degree, and prior-pivot dependencies. A row

\[
q_jv_j+P_j(v_1,\ldots,v_{j-1},u)=0,\qquad q_j\in\mathbf Q^*,
\]

defines the recursive polynomial substitution $v_j\mapsto-q_j^{-1}\phi(P_j)$,
fixing every remaining coordinate u, including c. The substitution preserves
both degrees. The inverse sends each u to its quotient class. Imposing images
of all nonpivot original rows gives an exact quotient isomorphism. No parameter
denominator or nonvanishing hypothesis enters. Thus a reduced identity can be
transported and checked in the original ring.

The frozen 42 and 37 substitutions for the 111/129 fibres appear in the N=1
selected-ring fast-reduction/replay artifacts. They must not be described as
maximal full-ring elimination without checking the larger-charge rows. This audit
does not assert such maximality.

There is also no intrinsic coordinate of **residual** charge zero. The residual
character is (r(z)=pw(z)-DB(z)). Since \(\gcd(p,D)=1\) and
\(1\le w(z)\le n<D\), (r(z)=0) would imply (D\mid w(z)), impossible. The
audit script checks this explicitly for all four variable inventories. Only c has
residual character zero.

## What the c=1 section does to a finite target block

The full torus section is a valid N-independent localization reduction:

\[
(R/I)[c^{-1}]\simeq (R/(I,c-1))[s,s^{-1}].
\]

It removes c from a solver ring, but simply setting c=1 does **not** reduce the
number of monomial columns in the inherited finite \(\delta_N=NC\) component.
The linear map (R_{NC}\to\mathbf Q[z]), (c\mapsto1), is injective: for each
z-monomial its possible exponent of c is uniquely determined by the bidegree.
Its image is precisely the finite direct sum

\[
\bigoplus_{k=0}^N\mathbf Q[z]_{kC}.
\]

Indeed a monomial (z^\alpha c^j\) of degree (NC) has
\(\deg(z^\alpha)=(N-j)C\); positivity gives (0\le j\le N\). Conversely every
monomial in the displayed sum has a unique homogeneous lift by
\(c^{N-k}\). Under this map the target becomes 1. Exact original-row multiples
map into this window, and the original row-space test is unchanged.

Equivalently choose integers (A,B) with (Ap+BD=1). Retain residual character
zero and (0\le k(z^\alpha)=AB(z^\alpha)+Bw(z^\alpha)\le N\). Keeping only
residual character zero, with no inherited finite window, yields infinitely many
monomials: the inventories contain both signs of residual character. It tests a
different object. A section UNIT proves some c power, not the particular N, until
its identity is homogenized and its resulting exponent checked.

An additional honest unit elimination is the unique target equation (F-c).
Its quotient is \(\mathbf Q[z]\), with (c\mapsto F), and the original question
becomes (F^N\in J\), where J is the ideal of all other row images. This preserves
the bidegree and has no localization. It can shrink the finite column space from
\(\sum_{k=0}^N H_{\mathbf Q[z]}(kC)\) to
\(H_{\mathbf Q[z]}(NC)\), at the cost of expanding or representing (F^N).
As always a positive result must be restored to an exact identity in the declared
original ring.

## Exact Hilbert data that the frozen truncations support

`audit_hilbert.py` verifies all source/basis/custody hashes in the frozen second
nonmembership audit, reconstructs the saved rational basis leading monomials with
the declared positive weighted reverse lexicographic order, and directly counts
standard monomials of the exact target bidegree. An independent generating-function
dynamic program reproduces the receiver ambient counts. The script also checks
that each total graded map is surjective onto its receiver: retained coordinates
are fixed, and a curve parameter t is the image of an original weight-one
charge-zero coordinate.

No fresh Gröbner algorithm is invoked. Completeness through the cutoff is consumed
from the frozen, exact S-pair verifications. The newly counted dimensions are:

| Fibre | Saved receiver variables | Ambient receiver monomials at C | H of saved finite receiver at C |
|---|---:|---:|---:|
| 77 | 40 | 448 | 1 |
| 111 | 65 | 190 | 2 |
| 129 | 62 | 605 | 21 |
| 136 | 79 | 206 | 2 |

All standard monomials counted in the last column are explicitly listed in
`hilbert-audit.json`. These values imply the exact
lower bounds

\[
H_{R/I}(C)\ge1,2,21,2
\]

in fibre order 77,111,129,136. They are not equalities asserted for the original
quotients. All four saved finite witness algebras have (H(2C)=H(3C)=0) because
those degrees exceed their saved overflow cutoffs. These zeros carry no original
positive-membership information. The frozen full N=2 attempt did not complete;
it supplies no (H_{R/I}(2C)). The original full target Hilbert values at 2C and
3C therefore remain OPEN unless a new full computation settles them.

There is independent exact full-ring Hilbert information in first charge zero:

\[
H_{R/I}(0,Y)=[v^Y]\prod_{B(z)=0}(1-v^{w(z)})^{-1}.
\]

The script computes all these coefficients through 3D. At the corresponding
second target weights they are:

| Fibre | H(0,D) | H(0,2D) | H(0,3D) |
|---|---:|---:|---:|
| 77 | 6,734,854 | 27,685,630,381 | 15,176,246,758,887 |
| 111 | 411,455 | 422,432,178 | 76,314,908,354 |
| 129 | 11,406,589 | 62,103,598,456 | 42,907,618,352,778 |
| 136 | 411,455 | 422,432,178 | 76,314,908,354 |

These are exact values of the full quotient in the **displayed** bidegrees, not
at (NC). They exhibit the permanent charge-zero polynomial directions and
explain why an Artinian top-degree shortcut cannot apply.

## Modular membership and a valid negative certificate

Let M be the declared rational Macaulay matrix, and e the target row. Clear all
entry denominators before reduction. A prime avoiding these denominators still
need not preserve rank. For example $M=[p]$, $e=[1]$ has membership over Q
and nonmembership modulo p. The variant $M=[p,1]$, $e=[1,0]$ is a true
nonmembership example over both fields and illustrates why the row and augmented
ranks must be treated together. A sharper primitive-row bad-prime example is

\[
M=\begin{pmatrix}1&1\\1&1+p\end{pmatrix},\qquad e=(1,0).
\]

Both matrix rows are primitive over Z. M is invertible over Q, so e belongs to
its row space, while modulo p the row space is spanned by (1,1) and misses e.
Thus primitive generator normalization and exclusion of original entry
denominators do not establish a good prime.

An exact good-prime negative argument is:

1. Certify \(\operatorname{rank}_{\mathbf Q}M=r\). A nonzero modular r-minor
   supplies a lower bound; an exact rational factorization $M=UV$ with r
   columns in U, or exact rational row reductions of every original row to an
   r-row basis, supplies the upper bound.
2. Compute \(\operatorname{rank}_{\mathbf F_p}M=r\) and
   \(\operatorname{rank}_{\mathbf F_p}[M;e]=r+1\).
3. The augmented modular minor is nonzero over Q, so the augmented rational
   rank is at least r+1. This proves exact nonmembership.

An alternative direct negative certificate is an exact rational column vector v
with $Mv=0$ and $ev\ne0$. A modular v can guide reconstruction, but both
equalities must be checked over Q against every original matrix row. Agreement
of several primes is evidence, not an exact rank upper bound.

A modular YES is a support signal. Recover rational row coefficients on the
identified support, then verify the resulting polynomial identity in the original
full ring. If computation took place after triangular elimination, its inverse
transport must be included; if it used c=1, the identity must be homogenized with
nonnegative c exponents. No truncated or specialized zero remainder alone proves
a full-chart kill. This is exactly the required FALLACY-v2 promotion boundary.
