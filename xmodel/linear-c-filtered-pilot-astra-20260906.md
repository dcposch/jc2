# Exact filtered C-linear reduction: 189 universal constant pivots

2026-09-06. Producer: Astra, /root/nonemptiness_certificate.
Evidence: exact Q linear algebra and identities; PRODUCER-CHECKED.
Different-model review remains required. No solve or properness claim.

The actual 192-dimensional C source space admits 189 constant pivots, with
selected minor identically 1 for EVERY polynomial G whose leading form is
H^6, H=(X+W)^3 W^8. The three remaining coordinates have degrees 22,11,0.
The constant coordinate is completely Jacobian-invisible, leaving TWO
nonconstant C coordinates after this reduction. This is stronger than the
requested 188-pivot bound; it is not a maximality claim for every possible
use of the fixed lower coefficients of the actual source G.

An exact basis/minor certificate and a triangular reconstruction DAG are
retained. Full residual substitution was deliberately not expanded, and no
solver was launched. A constant minor eliminates a major variable block
globally; it does not by itself make the remaining equations easy or proper.

## Inputs and exact ambient rings

Frozen source:
box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json,
SHA256 778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea.
The source has no residual rows. Root's preflight.py in the owned box,
SHA256 ac6828e97060c0ec76e1403b53f0bc89bccd97db6eeaedea1243f63d4e07a39a,
was read; it was not modified.

In X=x,W=y-x, a source row (r,z,e) with normalizer N represents
e X^(N-r-z) W^z. Use N=11,22,33,65,98 for h3,C2,C3,B2,A3 respectively.
Write h=h3^3+C2*h3+C3, D=physical(B2), C=physical(A3), a=target_a,
b=target_b. Then

    F = h^3+(3D+a)h/2+C
    G = h^2-bh/3+D
    J(F,G) = K+J(C,G)
    K = ((3D+a+bh)/2) J(h,D).

Here J is the determinant in the determinant-one coordinates X,W.
The exact source has deg h=33, deg D<=34, deg C<=35, h_top=H^3,
G_top=H^6; F,G always have exact degrees 99,66. Thus deg J(F,G)<=99.
This construction concerns the full raw physical Jacobian locus, not T2/T3.

The source C map is a homogeneous linear injection from Q^192 into
Q[X,W]_{<=35}, supported at 201 physical positions. Each original C parameter
has an identity slot. Its parameters are disjoint from h3,C2,C3,B2.
Both implementations verified these facts directly from the frozen map.

Let A be Q in the 247 other syntactically occurring physical-source
coordinates. The original ring is A[c_1,...,c_192,Zj].
No parameter is inverted in the C reduction. All basis changes divide only
by explicit nonzero rational numbers. The coefficient field is Q, not a
claimed integral or arbitrary-characteristic model.

## Why a universal constant minor exists

For a nonzero homogeneous P of degree l, J(P,H^6)=0 is equivalent to
J(P,H)=0. Euler's identities then imply

    11 H dP = l P dH,
    d(P^11/H^l) = 0.

In characteristic zero the rational function is constant. Since
H=(X+W)^3 W^8, valuations of P^11=c H^l imply
11 ord_(X+W)(P)=3l and 11 ord_W(P)=8l. Hence 11 divides l,
and P is a scalar multiple of H^(l/11). Conversely these powers are
in the kernel. For l=0 the kernel is the constants. Thus the homogeneous
leading map has a one-dimensional kernel exactly at degrees 0,11,22,33
within degree<=35, and no kernel at the other degrees.

It is essential to adapt the SOURCE SUBSPACE to the degree filtration.
Original source columns can mix homogeneous levels, and their displayed
highest parts need not be independent. The producer first performs rational
column echelonization of the 201-by-192 source coefficient matrix in
descending total degree, recording every source-column combination.
The resulting degree-l leading parts form a basis of the actual associated
graded source subspace.

Within each degree, rational column operations reduce J(P_l,H^6), selecting
one physical output coefficient for each nonkernel column and normalizing it
to 1. Output degree is l+64. Order degree groups descending, and within each
group retain the column-elimination pivot order.

For an input column of smaller degree, every selected higher-degree output
coefficient is zero for ALL lower G. In an equal-degree group only G_top
contributes, and the recorded column operations make the above-diagonal
entries zero and the diagonal entries 1. Contributions from arbitrary lower G
occur only below the degree blocks. Therefore the selected square matrix is
unit lower triangular over Q[g_uv : u+v<66], not merely at one G sample.
Its determinant is identically 1. Specializing g_uv to the actual nonlinear
source coefficients preserves this identity over A.

Summing the homogeneous rank deficiencies proves at least 192-4=188
constant pivots. The actual source has no W^33 monomial, so H^3 cannot occur
in its degree-33 graded piece. Its exact deficiency is three, not four,
and the construction yields 189 pivots.

## Actual source certificate and replay

filtered_basis_certificate.json explicitly contains all 192 original source
columns, identity slots, the 192 transformed physical polynomials, their exact
rational source combinations, the degree profile, selected Jacobian rows,
and every selected matrix entry as a rational linear form in arbitrary lower
g_uv. The source transform has a nonzero exact rational determinant; its full
value is in verify_filtered_summary.json. The selected Jacobian minor is 1.

The only deficient degree blocks are:

| Physical C degree | Graded source dimension | Leading-map rank |
|---|---:|---:|
| 22 | 7 | 6 |
| 11 | 4 | 3 |
| 0 | 1 | 0 |

All other blocks have full column rank, including dimension/rank 9 at degree33.
The surviving basis polynomials, with this certificate's normalization, are

    B22 = H^2 - 3X^5 W^13 + 3X^4 W^10 - X^3 W^7
    B11 = H
    B0  = 1.

The lower terms in B22 exhibit why the original source mixing cannot be
discarded. The full changed basis contains 681 physical terms and 660 source
change-of-basis terms.

The selected 189-by-192 matrix has 15,391 nonzero entries and 42,131 literal
terms in independent g coordinates. Every forbidden upper entry and every
diagonal value was checked IDENTICALLY, including all lower-G coefficients.
All 189 selected physical rows also occur in the immutable complete
factored-J coefficient-label stream.

A separate implementation parsed the source with SymPy, checked the source
transformation determinant with FLINT, and rederived all 42,131 terms using
separate differentiation code. It agreed exactly. This is an independent
implementation by the same producer, not different-model promotion.

Controls include full homogeneous ranks for degrees0..35, the explicit
H-power kernels, X^11 as a nonkernel negative control, an arbitrary exact
lower-G sample, a deliberately changed pivot coefficient, and a mixed-degree
source example. In the latter, X^2+W and X^2-W hide the degree-one vector 2W;
using only their two displayed leading parts would lose a rank contribution.
These tests passed. No modular rank inference is used for the theorem.

## Exact quotient reconstruction, with ALL remaining rows retained

Write the changed C coordinates as u_0,...,u_188,v22,v11,v0. Let M be the
selected 189-by-189 unit lower-triangular block, N the two nonconstant-free
columns, and K_R the selected coefficients of K. The chosen Jacobian equations
are

    M u + N (v22,v11)^t + K_R = 0.

They have the unique polynomial reconstruction, recursively,

    u_i = -K_Ri - sum_(j<i) M_ij u_j - N_i,22 v22 - N_i,11 v11.

Every coefficient belongs to A; no saturation, radical operation, generic
open chart, or parameter denominator occurs here. The selected equations
therefore give a graph over A[v22,v11,v0,Zj]. Substitute this graph into EVERY
other positive-degree coefficient of K+J(C,G), and retain

    Zj * (constant coefficient of K+J(C,G)) - 1.

If I_rem is that complete reconstructed residual ideal in
A[v22,v11,Zj], the original full-J quotient is exactly

    A[c_1,...,c_192,Zj]/I_full  ~=  (A[v22,v11,Zj]/I_rem)[v0].

The final polynomial factor exists because J(1,G)=0 identically. Removing it
preserves properness but is not an isomorphism of the two rings without that
factor. The two nonconstant free columns need not lie in the kernel of the
FULL actual G; their remaining equations must not be dropped.

reconstruction_graph.json records all 189 recursive equations, the literal
source basis map, g and K coefficient definitions, and residual labels.
Its conservative residual list includes all 4,860 positive physical slots
of degree<=99 other than the selected189, even identically zero slots.
Using the earlier complete coefficient support gives 1,279 previously nonzero
positive rows; all are listed separately. The inverse-J equation remains.
A selected-only old-pass/remaining-row-fail control is included to prevent
mistaking the graph equations for the full ideal.

The resulting theoretical source presentation has 247+2+1=250 variables.
Retaining the prior160 h-definition variables instead gives410 variables,
with nominal1,440 remaining rows before substitution-created zero cleanup.
These are coordinate/row counts, NOT a completed expanded reduced system.

## Measured cost and the deliberate stopping point

| Artifact step | Payload wall | Process high-water |
|---|---:|---:|
| Source basis + universal minor | 0.335 s | 34.1 MiB |
| Separate replay + exact face controls | 1.538 s | 108.8 MiB |
| Reconstruction DAG serialization | 0.075 s | 36.2 MiB |

The triangular graph has42,320 literal terms in abstract g,K,C coordinates
and uses only188 lower-G coefficients, of physical degrees34..65.
This is NOT a42,320-term graph in the original nonlinear source coordinates.
No substitution of the g,K coefficients into those source variables, and no
189-fold dense reconstruction, was performed.

A conservative uncollected recurrence bounds a reconstructed coordinate by
329321309261706864157000551752128693403980556754525116134127842 terms
(about3.29e62), with abstract g,K,v degree at most35. This loose syntactic bound
is neither a measured expanded count nor a prediction after cancellations.
It is a warning that the small constant minor alone does not license claiming
manageable expansion. Preserve the DAG or measure structured substitution
separately; no solver improvement has yet been demonstrated.

## Optional highest face: geometric equivalence, not scheme equivalence

Let d=D_34 and c=C_35. The degree99 Jacobian face is

    (3/2)d J(H^3,d) + 2H^3 J(c,H^3)
      = J(H^3, (3/4)d^2 - 2H^3 c).

The homogeneous degree68 map S -> J(H^3,S) is injective by the same kernel
lemma, since11 does not divide68. Its exact coefficient-matrix rank is69,
verified independently. Therefore the highest-face coefficient ideal equals
the ideal of coefficients of (3/4)d^2-2H^3 c, by a constant Q left inverse.

Actual source top supports give d=X^2 W^25 P7(X,W), with P7 homogeneous of
degree7, and c supported on W exponents26..32. Over any characteristic-zero
FIELD, the face equation implies (X+W)^9 divides d^2, hence (X+W)^5 divides
P7. There is a unique homogeneous quadratic L such that

    d = X^2 (X+W)^5 W^25 L,
    c = (3/8) X^4 (X+W) W^26 L^2.

Conversely these expressions obey the exact face equation and the source
supports. The source maps onto its eight-dimensional d top space and
seven-dimensional c top space with disjoint parameter sets; the ranks8 and7
were checked exactly. Thus this is a field-point parametrization of the
highest-face locus, and an isomorphism of its reduced top-coefficient locus
with affine3-space. It may be pulled back through the actual linear source map.

Source mixing must still be respected. In particular the W^25 coefficient
of d is

    B2c_47_13 + 4B2c_51_10 + 10B2c_55_7
      + 20B2c_59_4 + 35B2c_63_1.

Solving for B2c_47_13 also changes lower D coefficients. Updating only d while
keeping those lower coefficients independently fixed would not preserve the
source family.

The parametrization is NOT an isomorphism of the original face scheme.
Over Q[epsilon]/(epsilon^2), take d=epsilon X^9 W^25 and c=0. The face equation
holds because d^2=0, but d is not divisible by (X+W)^5 and so has no displayed
L representation. This exact nilpotent negative control passed. On coefficient
ideals, the parametrized prime graph is the RADICAL of the original top-face
ideal, not the original ideal itself. No full-J radical calculation or
counterexample follows from this face analysis.

## Terminal artifacts and custody

All three owned capped jobs are NORMAL_EXIT, rc0, with no stderr and no
remaining writers. Their supervisor wall total was under4 seconds; each had
a600-second/32-GiB exact-PGID cap and none overlapped. The allowed1800-second
aggregate arithmetic budget was not approached.

Only /home/ubuntu/linear-c-discriminator-20260906 on the existing root-owned
worker i-0da0cebfc97c9fd54,172.30.0.56 was written. The older factored-J
artifacts remain unchanged; only their frozen label TSV was read. No Fable
scratch, live gate, blind ideation report, active adapter, or shared ledger
was read or modified. No worker was launched, terminated, or retagged.

The worker remains under ROOT CUSTODY. All listed new worker artifacts are
read-only, and the producer promises no further edits. Complete job metadata,
file sizes and hashes are in box/linear-c-discriminator-20260906/custody.json,
SHA25684cd61258f35dc4fba6f992b9527094cbb940622be84800a67ae3e3f4ad0e989.

Key exact artifacts:

- filtered_basis_certificate.json,1,429,336 bytes:
  c2b5965278e0fa30f0490b7f5a019434abe5291e50b748d3a3c0795c8175f906.
  Copied locally beside the scripts and compact terminal evidence.
- reconstruction_graph.json,1,613,277 bytes, worker copy:
  8fef3537678e8eeb549701fd994d76ba6c96a59b567ac1dc76a54701271384d6.
- Source scripts: filtered_basis.py, verify_filtered.py,
  reconstruction_dag.py; full hashes and replay requirements are in custody
  and REGISTRATION.md. They require the registered worker and exact scratch;
  a fresh-scratch replay needs an explicitly reviewed guard-path adjustment
  in a copied script, never a charged-file overwrite.

Recommendation: independently review the189-pivot certificate and global
quotient map, then measure structured residual substitution with a separate
cap. Highest-face radical parametrization is a second, distinct possible
compression; preserve its field-point/scheme distinction.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14380`.
- Body SHA-256:
  `5a56fbd1eb5d258a11fe1a1d14198c8c1f1b115ee4f44fb7080ee4a68c82389f`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
