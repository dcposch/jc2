# N5-S1: singular-branch survivor at \(N=5\)

## 1. Scope, sources, and status conventions

The three frozen inputs were verified before the first filesystem write.  Their
SHA-256 values are, in charge order,

```text
48d417d6980e52d61550a733f0dcded7d26a0c4e127677ac73bd544a8a00713b
bd6443b34e95213b0b2950e45c896417c492487c38a0a721eae4977d1e73f5d6
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc
```

I write `B0:n`, `REV:n`, and `INT:n` for line `n` of, respectively,
`b0-reducible-n5-opus5-20260831.md`,
`b0-reducible-n5-hostile-review-sol56-20260831.md`, and
`block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md` in the
frozen `inputs/` directory.  The review is controlling where it corrects B0:
it confirms the P1 numerical cage but rejects the claimed extra affine
singularity, corrects the S1b local orbits, and holds the generic-line degree
floor pending citation custody (`REV:82-107,145-154`).  The later integration
promotes an explicit-family \(S_4\) row-kill and its INF-TRIVIAL ingredient, but
expressly routes S1 for its own singular-branch treatment (`INT:30-60,73-82`).
It supplies no \(S_5\) cusp theorem.

All conclusions below are necessary conditions, never attainment claims.  A
normalization parameter, its normalization place, and its physical image point
remain distinct.  I use \(\delta_p\) only for the plane-curve delta invariant;
the degree of the branched component is denoted \(d\), avoiding B0's overloaded
`delta`.  No new exit price is asserted.

## 2. Exact S1 configuration extracted from the reviewed cage

S1 is P1, the cost partition \((2,1)+(1,0)\) in the exact budget
\(\sum_l(\mu_l+\operatorname{corr}_l)=4\) (`B0:53-57,191-200`; review
confirmation `REV:28-54`).  There are two dicriticals and every component has
an owner, so reducibility forces distinct owners and \(m=2\):

| datum | branched component \(D_A\) | trivial-owner component \(D_B\) |
|---|---:|---:|
| \((\mu,\operatorname{corr},s)\) | \((2,1,1)\) | \((1,0,1)\) |
| \(W=\sum s\mu\) | \(2\) | \(1\) |
| generic affine fibre \(a=5-W\) | \(3\) | \(4\) |
| generic meridian in \(S_5\) | \((2,1,1,1)\) | identity |

This ownership and these values are review-confirmed (`B0:227-245,474-486`;
`REV:82-91`).  The cover-ramification floor
\[
 \operatorname{corr}_l=\mu_l(s_l-1)
   +\sum_t(M_t-e_t\mu_l),\qquad M_t-e_t\mu_l\ge0,
\]
forces both cover degrees to be one (`B0:121-137,204-225`; `REV:48-54`).
Thus both normalizations are \(\mathbb A^1\), both components have one place at
infinity, and both normalization-factor maps \(h_A,h_B\) are isomorphisms.
Chau's cited theorem additionally pins all components to one common physical
point at infinity and a common coprime leading-exponent pair; this is not an
affine-disjointness assertion (`B0:537-548`; `REV:89,151`).

On \(D_A\), \(K_A=1\).  Since the summands are nonnegative integers, there is
exactly one parameter \(t_0\) with \(e_{t_0}=1\), \(k_{t_0}=1\), and
\(M_{t_0}=3\).  Put \(p_0=\eta_A(h_A(t_0))\).  The reviewed pointwise
Żołądek law makes the parametrization critical precisely there; because
\(h_A\) is an isomorphism, \(d\eta_A=0\) at that normalization place.  Hence
the corresponding locally irreducible branch of \(D_A\) is genuinely singular
(cusp-type), although neither its Puiseux pair nor an analytic normal form is
pinned (`B0:64-72,257-280,478-504`; `REV:60,89`).

On \(D_B\), \(\mu=1\) and \(s=1\) make \(\eta_B\) immersive at every
normalization parameter.  This conclusion is **only** about \(D_B\): it cannot
be transported across the two-component ownership map to \(D_A\).  It says
that every branch of \(D_B\) is smooth, not that \(D_B\) is injectively
parametrized or disjoint from \(D_A\).

Local irreducibility of the distinguished branch also does not identify that
branch with the entire physical germ at \(p_0\).  The reviewed cage therefore
has two exhaustive local types for the \(D_A\)-germ (the S1a case still splits
according to \(D_B\)-incidence):

- **S1a:** \(r_{A,p_0}=1\).  The whole \(D_A\)-germ is the cusp branch, while
  \(D_B\) may still pass through the same physical point.  LOC gives
  \(a_{p_0}=2-r_{B,p_0}\), and affine fixed letters plus the \(\mu=1\)
  clusters total exactly two.
- **S1b:** \(r_{A,p_0}=2\).  A second, smooth \(D_A\)-branch meets the cusp
  branch.  LOC forces \(D_B\) away and \(a_{p_0}=0\); the nonfixed local
  orbits are exactly \(3+2\), not an optional orbit of size five
  (`REV:93-97`, correcting `B0:488-494,594-599`).

Away from \(t_0\), \(\eta_A\) is immersive.  Since LOC gives
\(r_{A,p}\le2\), every other singularity of \(D_A\) is a meeting of two smooth
branches (tangency allowed).  At such a point \(D_B\) incidence remains
possible: without \(D_B\), \(a_p=1\); with it, necessarily
\(r_{B,p}=1,a_p=0\).  The total local fixed count is one in either case
(`B0:360-377`; `REV:95`).

Writing \(d=\deg D_A\), B0's transversal-genus calculation gives
\(d=3+2g_L+\Sigma_\infty\ge4\), but the review holds this floor
custody-conditional because both supplied proofs use the same uncited
generic-line \(\pi_1\)-surjection (`B0:379-428`; `REV:105,154,174`).  The safe
unconditional degree data here are \(\deg D_B\ge1\) and no upper bound on
either degree.

## 3. Per-component geometry and numerical identities

The only stated generic-fibre identity that is componentwise is
\(a_i+W_i=N\).  It gives
\[
 (a_A,W_A)=(3,2),\qquad (a_B,W_B)=(4,1).
\]
The correction/cover floor gives \(K_A=1,K_B=0\).  The aggregate identity is
therefore
\[
 W_A+W_B+K_{\rm tot}=2+1+1=4=N-1. \tag{3.1}
\]
As B0 itself observes, this is just the Orevkov budget after the cover-floor
decomposition, not a new constraint (`B0:155-172,204-225`).

A particularly tempting but invalid kill is to apply the irreducible formula
\(K=a-1\) separately to \(D_A\), obtaining \(1\ne3-1\).  The Euler
stratification is global and does not split this way.  Combining (3.1) with
\(a_A=5-W_A\) instead gives the correct relation
\[
 K_{\rm tot}=a_A-1-W_B=3-1-1=1. \tag{3.2}
\]
The other component's weight is exactly the apparently missing unit.  Moving
immersivity from \(D_B\) to \(D_A\), or moving the irreducible Euler identity
in the same way, would repeat the component-carrier error highlighted in the
charge.

Here is the full compact-support check.  Let \(\Sigma\) contain every singular
or component-incidence point needed for the stratification and the unique
correction image.  Put
\[
 \sigma=|\Sigma|,\quad
 R_i=\sum_{p\in\Sigma}r_{i,p},\quad
 A_\Sigma=\sum_{p\in\Sigma}a_p.
\]
Because each normalization is \(\mathbb A^1\), removing \(\Sigma\) removes
exactly \(R_i\) normalization points, so
\(\chi_c(D_i\setminus\Sigma)=1-R_i\).  The reviewed stratification identity
specializes to
\[
 2(1-R_A)+(1-R_B)=4-5\sigma+A_\Sigma. \tag{3.3}
\]
On the other hand, summing LOC
\(a_p+2r_{A,p}+r_{B,p}+K_p=5\), and using
\(\sum K_p=1\), gives
\[
 A_\Sigma+2R_A+R_B+1=5\sigma. \tag{3.4}
\]
Substitution turns both sides of (3.3) into
\(3-2R_A-R_B\).  Thus the aggregate Euler identity is identically satisfied,
including at the cusp; it cannot be spent as an independent inequality.

For the charge's unibranch reading at \(p_0\), let
\(b=r_{B,p_0}\).  Then LOC is
\[
 a_{p_0}+2+b+1=5,qquad a_{p_0}=2-b,qquad 0\le b\le2. \tag{3.5}
\]
If “locally irreducible image singularity” is scoped to the whole \(D_A\)-germ,
this selects S1a but still does not bar \(D_B\) incidence; if it is scoped only
to the distinguished image branch, the reviewed S1b fallback remains.  If it
is instead asserted for the whole union germ, then \(b=0\).  Every one of these
readings satisfies (3.3)-(3.5).  For S1b, LOC gives
\(r_A=2,r_B=0,a_{p_0}=0\), and the same global cancellation holds.

## 4. Cusp contribution and numerical verdict

Let \(\overline D_A\) be the projective closure.  Its normalization is
\(\mathbb P^1\), so the exact genus formula is
\[
 \delta_\infty+\delta_{\rm aff}
   =p_a(\overline D_A)=\frac{(d-1)(d-2)}2. \tag{4.1}
\]
For S1a,
\[
 \delta_{\rm aff}=\delta_{p_0}
   +\sum_{q\ne p_0} I_q(C_{q,1},C_{q,2}),qquad \delta_{p_0}\ge1. \tag{4.2}
\]
For S1b, \(\delta_{p_0}\) must mean the whole two-branch germ, and the
review supplies the sharper estimate
\[
 \delta_{p_0}=\delta(C_{\rm cusp})
   +I_{p_0}(C_{\rm cusp},C_{\rm sm})\ge1+2=3. \tag{4.3}
\]
These are exactly the corrected budgets at `REV:99-105` (cf.
`B0:521-535`).

Equations (4.1)-(4.3) do not enter (3.3).  Normalization Euler bookkeeping
uses \(r_p-1\), whereas algebraic genus bookkeeping uses \(\delta_p\).  For an
ordinary node the two happen to agree:
\((r,\delta,\mu_{\rm Milnor})=(2,1,1)\).  For a minimal cusp they do not:
\((r,\delta,\mu_{\rm Milnor})=(1,1,2)\).  More generally
\(\mu_{\rm Milnor}=2\delta-r+1\); S1a has \(r-1=0\) but
\(\delta\ge1\), while S1b has \(r-1=1\) but \(\delta\ge3\).  Thus the
\(N=4\) one-node exclusion pattern cannot be transferred by replacing a node
with a cusp.  The charged covering stratification contains neither a Milnor
number nor a vanishing-cycle term.

There is also no genus-cap contradiction.  Even granting the
custody-conditional floor \(d\ge4\), the nonnegative allocations
\[
 \begin{array}{c|ccc}
 &d&\delta_{p_0}&\delta_\infty+\sum_{q\ne p_0}\delta_q\\ \hline
 \text{S1a}&4&1&2\\
 \text{S1b}&4&3&0
 \end{array}
\]
satisfy (4.1).  They are arithmetic controls only, not curve or Keller-map
witnesses.  At larger \(d\) the right side only grows, and no charged theorem
gives an upper bound for \(d\) or a lower bound for \(\delta_\infty\) that
reverses this conclusion.  Here \(\delta_\infty\) is the curve singularity
invariant; it must not be identified with Gate TG's unrelated
\(\Sigma_\infty\).

**Numerical verdict: S1 survives.**  Closing it numerically would require a new
cusp-inclusive polar/vanishing-cycle identity coupling
\(\delta_{p_0}\) (or \(\mu_{\rm Milnor}\)) to \(K=1\), or an independently
proved degree/infinity cap.  Neither is present in the frozen promoted toolkit;
the review expressly rejects the inference that another affine singularity is
forced (`REV:105-107,154`).

## 5. \(S_5\)-monodromy and representation constraints

Let \(\rho\) be the five-sheet monodromy.  It is transitive; \(D_B\)-meridians
map to the identity, so \(\rho\) factors through
\(\pi_1(\mathbb C^2-D_A)\).  Every \(D_A\)-meridian is a transposition.  A
transitive subgroup generated by transpositions is the full symmetric group
(the transposition-support graph is connected), hence
\[
 \rho:\pi_1(\mathbb C^2-D_A)\twoheadrightarrow S_5. \tag{5.1}
\]
This reviewed conclusion is the only PI1-S4-shaped part of S1
(`B0:550-569`; `REV:89-91`).

The corrected local constraints are sharper:

- At every other two-smooth-branch point of \(D_A\), the two branch
  meridians are disjoint transpositions.  The local fixed count is one whether
  that letter is affine or comes from a \(D_B\) trivial cluster (`REV:93-95`).
- In S1a, the correction cluster is one orbit of size three and two letters
  are fixed.  Its transitive, transposition-generated image is the natural
  \(S_3\) on that orbit (`REV:96`).  A desk peripheral lemma adds that, after
  the trivial \(D_B\)-meridians are killed, the distinguished cusp-branch
  longitude maps to one.  Indeed it commutes with a cusp meridian, has zero
  cusp-meridian exponent and hence even image, while
  \(C_{S_3}((12))\cap A_3=\{1\}\).  This is a local peripheral statement, not
  a statement about the loop at infinity; any linking contributions from an
  incident \(D_B\) die under \(\rho\).
- In S1b, the invariant orbits are exactly \(O_3\sqcup O_2\), and the review
  pins projections \(S_3\) and \(C_2\) (`REV:97`).  The following desk upgrade
  explicitly supplies the inertia step requested there.  The reviewed
  branch/cluster dictionary makes singular-branch Wirtinger meridians
  \((\text{transposition},1)\) on the actual orbits; they generate
  \(S_3\times1\).  A smooth-branch meridian is
  \((1,\text{nontrivial})\).  Hence the full local image is
  \(S_3\times C_2\).  No five-letter local orbit is possible.

The number \(M_{t_0}=3\) is a cover-cluster size, not a Puiseux pair or braid
exponent.  In particular it does not pin the cusp to \(A_2\).  If the germ is
the ordinary cusp, its meridians satisfy \(aba=bab\), and
\(a=(12),b=(23)\) give the required \(S_3\); the central word
\((ab)^3\) maps to one.  But already \(ab=(123)\) and
\((ab)^2=(132)\) are nonidentity even words.  B0's more general Fox/determinant
test and its \(T(2,n)\) list remain citation-custody-conditional under the
review (`B0:582-593`; `REV:96,174`), and no exact analytic type is available
to apply them.

This is precisely where the promoted INF-TRIVIAL argument stops transferring.
INT proves it only for the explicit ROW-NF \(S_4\) sextics and transported
octics, using family/stratum-specific infinity-word data recorded as
\(2+2+2\) and \(g_5^2g_1^4\) (`INT:30-60,90-98`).  It is not the assertion
that every even-length word in transpositions is trivial.  **If** an S1
infinity word has even exponent sum, its image is constrained only by
\[
 \rho(\gamma_\infty)\in A_5,
\]
allowing identity, a 3-cycle, a double transposition, or a 5-cycle.  A product
of two transpositions can already be a nontrivial 3-cycle.  No frozen input
provides an S1 meridional word for \(\gamma_\infty\), much less a rewrite as a
product of individual even powers.

There is one unconditional homological pin.  Define \(\gamma_\infty\) to be
the infinity loop in the same generic target line used in Gate TG.  After the
trivial \(D_B\)-meridians are killed, elementary linking gives
\([\gamma_\infty]=\pm d[\mu_A]\) in abelianization, whence
\[
 \operatorname{sgn}\rho(\gamma_\infty)=(-1)^d. \tag{5.2}
\]
Thus odd \(d\) prevents INF-TRIVIAL/projective descent but is not a
contradiction; even \(d\) puts the image in \(A_5\) but does not make it one.
Conditionally on the reviewed-held Gate TG, the cycles of this restricted-cover
infinity permutation correspond to the normalization points above the generic
\(q_\infty\), so the desk identification is
\(c=\Sigma_\infty\).  Hence \(d=3+2g_L+c\).  Even infinity image gives
\(c=1,3,5\), hence respectively
\(d=4+2g_L,6+2g_L,8+2g_L\); actual triviality would select the last row.  This
is a conditional refinement only, not a promoted degree gate.

Finally, the local conjugacy data contain no abstract \(S_5\) contradiction.
For example
\[
 a=(12),\ b=(23),\qquad c=(14),\ d=(25)
\]
satisfy the ordinary-cusp braid relation for \(a,b\), give a disjoint commuting
pair \(c,d\), and have a connected support graph, hence generate \(S_5\).
This is only a permutation-level consistency control, not a curve-group or
Keller-map witness.  It also cannot be reversed to force another affine
double point, an inference the review explicitly rejects (`REV:107,154`).

Even a future proof of \(\rho(\gamma_\infty)=1\) would not finish the old
\(S_4\) chain: INT also uses an \(S_3\) resolvent and a projective-cover/torus
obstruction (`INT:40-50`).  The group \(S_5\) has no \(S_3\) quotient, and no
\(S_5\) cusp-scope replacement is supplied.

## 6. Final verdict and typed first missing tool

**VERDICT: S1 is OPEN, not KILLED.**  The per-component generic-fibre
identities hold, the aggregate Euler calculation reduces identically to
\(2+1+1=4\), and the cusp's \(\delta\)-cost lives in a separate genus budget
with no charged degree or infinity cap.  The exact local permutation data are
also group-theoretically consistent with \(S_5\).  Neither N-A/N-A-RES nor the
explicit-family PI1-S4 row theorem has the singular-branch scope needed here
(`B0:496-504,622-632`; `REV:136,151-160`; `INT:77-82`).

The residual can be pinned safely as follows.

> **`OPEN[PI1-S5-CUSP-CORRECTION]`.**  Can an irreducible polynomial curve
> \(D_A\), with normalization \(\mathbb A^1\) and one place at infinity, admit
> a surjection \(\pi_1(\mathbb C^2-D_A)\twoheadrightarrow S_5\) taking every
> meridian to a transposition, subject to: exactly one critical normalization
> branch with \(K=1,M=3\) and unknown Puiseux type; local image \(S_3\) on a
> three-letter orbit in S1a, or \(S_3\times C_2\) on the reviewed \(3+2\)
> orbits in S1b; disjoint transpositions at every other two-smooth-branch
> singularity; the exact delta-genus budget; and
> \(\operatorname{sgn}\rho(\gamma_\infty)=(-1)^d\)?  A **NO** kills S1.  A
> **YES** passes only this necessary representation gate and is not an
> attainment claim for a Keller map.

For the requested INF-TRIVIAL-style route, the first missing lemma is more
specific:

> **`OPEN[N5-S1-INF-WORD]`.**  Determine an S1 cusp-compatible
> Zariski--van Kampen/peripheral word for the generic-line infinity loop and
> decide its image in every representation above.  In particular, is it
> forced to be the identity, rather than merely an even permutation when
> \(d\) is even?

The local S1a longitude calculation does not answer this global question.  If
INF-WORD did force identity, one further tool would still be needed: an
\(S_5\) projective-cover obstruction at singular-branch scope.  The promoted
\(S_4\) proof uses an \(S_3\) resolvent and Shirane's specialized obstruction;
\(S_5\) has no \(S_3\) quotient and the frozen toolkit contains no replacement.
This is the first honest stop; no cap, analogy, or floor has been promoted into
an equality.

<!-- BODY-END -->
