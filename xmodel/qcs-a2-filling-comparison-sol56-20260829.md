# QCS via an \(A^2\)-filling comparison: exact typing test

**Author:** Sol 5.6 Ultra  
**Date:** 2026-08-29  
**Basis:** 31777ce90994a106aade85064c0d868e32863f94  
**Lifecycle:** sealed research report; no canonical promotion

## Verdict

The quantity

\[
K=\sum_i b_i(\deg P_i-1)
\]

does have an exact vanishing-cycle interpretation, but only for the auxiliary
disjoint union of the one-variable quotient maps \(P_i:\mathbb A^1\to\mathbb
A^1\), with coefficient multiplicity \(b_i\). It is not presently typed as
the length of a positive factorization for the original polynomial \(f\), nor
as the dimension of its vanishing homology at infinity.

After morsification this is also a weighted positive half-twist length for
those auxiliary covers. It is not a positive factorization on the generic
fibre of \(f\).

An \(A^2\)-filling, positivity, and page/boundary counts alone do **not** force
the desired extra \(s-1\). The natural boundary-tree route needs two maps not
constructed in the current campaign. With \(\mathcal P\) the set of pole
places, it needs

\[
\partial_{\mathcal P}:V_{\rm aux}\twoheadrightarrow
\widetilde H_0(\mathcal P;\mathbb Q),\qquad
\Psi:\ker\partial_{\mathcal P}\twoheadrightarrow H_1(F;\mathbb Q).
\]

Their existence would immediately prove \(K\geq\delta+s-1\). Without them,
the route is untyped rather than proved or disproved. A five-cycle degree-six
control already in the repository is the cheapest decisive test.

## 1. What \(K\) counts exactly

Put \(d_i=\deg P_i\), and let \(B_i\) be a vector space of dimension \(b_i\).
For a degree-\(d_i\) polynomial, the finite ramification divisor has length

\[
\mu_{\rm fin}(P_i)
=\sum_{z\in\mathbb A^1}\operatorname{ord}_z(P_i')
=d_i-1
=\sum_a(d_i-q_i(a)),
\]

where \(q_i(a)\) is the number of distinct points in \(P_i^{-1}(a)\). Hence,
for the auxiliary map \(P_{\rm aux}=\coprod_iP_i\), define

\[
V_{\rm aux}
=\bigoplus_i\ \bigoplus_{z\in\operatorname{Crit}(P_i)}
B_i\otimes\phi_z(P_i).
\]

Counting Milnor multiplicity at each critical point gives the exact identity

\[
\dim V_{\rm aux}=\sum_i b_i(d_i-1)=K.
\]

Equivalently, after a small morsification of each \(P_i\), its finite branch
monodromy is a product of \(d_i-1\) positive half-twists in the braid group on
\(d_i\) sheets. Taking \(b_i\) formal coefficient copies makes \(K\) the
weighted positive length of the disjoint auxiliary braid factorizations.
These are vanishing zero-cycles of finite covers of the \(a\)-line, not
vanishing one-cycles in the surface page \(F\).

This is compatible with the fixed-value collision count
\(C(a)=\sum_i b_i(d_i-q_i(a))\), whose sum is \(K\). It does not identify a
cycle in the generic fibre of \(f\): the \(P_i\) live on quotient lines and the
\(B_i\) are coefficient multiplicities.

## 2. The precise missing boundary complex

For the connected generic affine fibre \(F\), Suzuki gives

\[
\delta=1-\chi_{\rm gen}=b_1(F).
\]

The clean boundary-tree proof would make \(V_{\rm aux}\) the edge space of a
graph whose vertices are the \(s\) physical pole places. Precisely, one needs
a pole-incidence boundary and a cycle-realization map

\[
\partial_{\mathcal P}:V_{\rm aux}\twoheadrightarrow
\widetilde H_0(\mathcal P;\mathbb Q),
\qquad
\Psi:\ker\partial_{\mathcal P}\twoheadrightarrow H_1(F;\mathbb Q).
\tag{2.1}
\]

The first surjectivity says the putative boundary graph is connected. Its
kernel is the graph cycle space; the second says those graph cycles carry all
of the page homology. Rank-nullity then gives exactly

\[
K=\dim V_{\rm aux}
=(s-1)+\dim\ker\partial_{\mathcal P}
\ge (s-1)+b_1(F)=s-1+\delta.
\]

This formulation also identifies the missing geometry: every weighted
quotient critical event needs two endpoints among actual pole places, and
cycles in that incidence graph need a suspension/attachment into the generic
fibre. If a fibre is allowed to have \(c\) connected components, the vertex
part decomposes into within-component pole differences of dimension \(s-c\)
and between-component differences of dimension \(c-1\), totaling \(s-1\).

Neither map in (2.1) currently exists in the repository. The Section 7
collision formula is an equality of Euler/constructible-function counts. Its
cyclic quotients \(U_i\) are abstract coefficient quotients, and the
resolution-free repair intentionally avoids putting all \(U_i\) on a common
resolved boundary. Thus it supplies neither pole endpoints nor a suspension
from quotient zero-cycles to page one-cycles. Earlier common-resolution
direction claims were not promoted; their fixed-weight version failed.
Likewise, the monodromy reports distinguish branch-value braids from
source-sheet monodromy, and ordinary passports can omit unramified
(\(e=1\)) boundary sheets. The Hamiltonian--Kummer audit also stops at exactly
this type gate: its character spaces have no map to quotient lines or pole
places. These facts block construction of \(\partial_{\mathcal P}\) and
\(\Psi\), while preserving pole **places**, flags, and series as distinct
objects.

## 3. Filling alone cannot supply the missing \(s-1\)

There is a simple positive allowable Lefschetz-fibration control. Begin with
the disk PALF on \(D^4\). Perform five positive stabilizations. Each adds a
canceling 1/2-handle pair, so the total space remains \(D^4\). Choose four
boundary-increasing stabilizations and one genus-increasing stabilization;
the resulting page is \(\Sigma_{1,4}\), with

\[
b_1(\Sigma_{1,4})=2(1)+4-1=5.
\]

The five stabilization curves can be ordered so that each crosses its new
1-handle once. Their homology classes are therefore triangular with unit
diagonal in the corresponding handle basis, hence form a basis of
\(H_1(\Sigma_{1,4})\). The thimble-to-page map from the five positive
vanishing cycles consequently has zero kernel.

Mark any two of the four boundary components as poles. Then
\(\widetilde H_0(\text{marked poles})\) has dimension one, but it cannot inject
into that zero kernel. Thus a \(D^4\cong A^2\)-type filling, positivity, five
vanishing cycles, and \(s=2\) do not by themselves force an extra pole
relation. This is a topological control, not a polynomial/Keller example; it
shows exactly that quotient-collision locality or a common-boundary attachment
theorem is essential.

## 4. Cheapest discriminator: a labelled PALF lift of the degree-six control

Use the matched abstract cover already recorded in the QCS report:

\[
(G,s,n,K,\delta,E)=(1,2,2,5,5,0),
\]

with one quotient datum \((d_1,b_1)=(2,5)\) and branch permutations

\[
\sigma_+=(1\ 2\ 3\ 4\ 5),\qquad
\sigma_-=(0\ 1\ 2\ 4\ 3),\qquad
\sigma_\infty=(0\ 3\ 1\ 5\ 2).
\]

They have product \(1\) and generate the recorded transitive \(A_6\) action.
The page has type \(\Sigma_{1,4}\), with two boundary components labelled as
poles and two as finite ends. The quotient datum gives five weighted positive
auxiliary generators. Since \(K=\delta=5\) and \(s=2\), no complex of the
form (2.1) can exist for this control: a surjective pole boundary leaves a
four-dimensional kernel, too small to cover \(H_1(\Sigma_{1,4})\).

The cheapest discriminator is therefore a **labelled PALF-realization test**,
not another numerical Euler check. Try to realize on \(\Sigma_{1,4}\):

1. the degree-six \((5,1),(5,1),(5,1)\) source-sheet passport and the
   coalescence of \(\sigma_+,\sigma_-\);
2. the quotient braid \(P=z^2\) with coefficient rank five;
3. the two pole and two finite-end boundary labels; and
4. a five-vanishing-cycle positive factorization whose total handlebody is
   \(D^4\).

This is a finite mapping-class/relative-homology and Kirby calculation on a
fixed page. Compute the \(5\times5\) homology matrix and the labelled boundary
incidence; no heavy CAS is needed.

* If a determinant-unit factorization exists with all labels and passport
  constraints, then even matched braid data plus a topological \(A^2\) filling
  do not force QCS. A successful proof must use genuinely algebraic
  polynomial-boundary data beyond filling topology.
* If every labelled realization is non-
  \(D^4\), or forces a pole-incidence rank that drops the page-homology rank,
  the resulting obstruction is the candidate missing global theorem to lift
  from the control to polynomial compactifications.

The unlabelled stabilization construction in Section 3 already realizes the
counts with determinant one. Thus the only remaining content in this
discriminator is the compatibility of the quotient collision, source-sheet
passport, and physical boundary labels. That is strictly cheaper and better
typed than attempting a general log-surface theorem first.

## Nonclaims

This report does not refute QCS, does not produce a Keller counterexample, and
does not assert that every quotient collision lifts to a Lefschetz vanishing
cycle. It identifies \(K\) exactly at the auxiliary one-variable tier,
exhibits why filling data alone are insufficient, and names the pole-incidence
and suspension maps required to turn the boundary-tree route into a proof.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9012`.
- Body SHA-256:
  `9c41323249ac54ddf0f13bd34631ce52225ce16adf1119333f0d0d50a322ec60`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
