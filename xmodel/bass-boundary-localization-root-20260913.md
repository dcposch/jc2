# Coordinate-uniform Bass test: the boundary localization obstruction

ROOT, September13,2026. MANUAL / PRODUCER-CHECKED / UNPROMOTED.
NO_NEW_SOURCE_CONSTRAINT. This records one failed global implication and
its exact missing boundary module; no finite-family successor is selected.

## Actual source calculation

Let A=C[p,q] subset R=C[x,y] be an actual plane Keller inclusion, N=R/A,
and let D=V(g) be its actual reduced nonproperness divisor. Over U=A2-D
the map is finite etale of degree d. Inverse-Jacobian derivatives preserve
R, so its target de Rham complex is the ordinary source de Rham complex.
The inclusion A->R induces the identity on the only cohomology group C.
Consequently the de Rham complex of N is acyclic.

This acyclicity CANNOT simply be used for its finite-monodromy connection
on U. The actual source intersection R intersect Frac(A)=A gives an
injection N->N_g and the exact D-module sequence

    0 -> N -> N_g -> Q -> 0,
    Q=R_g/(R+A_g).

Here N_g=R_g/A_g, and Q is supported on D. All rings and quotients are
literal: Q is not R/A, a source algebra, or the trace image. The algebraic
de Rham long exact sequence gives

    H_DR^i(N_g) = H_DR^i(Q) for every i.

Thus the boundary quotient retains exactly the cohomology that a putative
localization argument would discard. Since N_g is the finite-monodromy
rank-(d-1) connection of the finite etale cover on U, standard regular-
singular de Rham comparison and the finite-CW Euler formula give

    chi_DR(Q)=chi_DR(N_g)=(d-1)*(1-chi(D)).

There is no proof here that Q or its cohomology vanishes. Source acyclicity
alone supplies neither. This is the first failed implication, not a new
properness theorem or an obstruction to every coordinate-uniform argument.

## One explicit loss-of-acyclicity control

Reuse the already analyzed fixed module

    M=C[p,((p-1)(p-2))^-1]*sqrt((p-1)(p-2))
      tensor C[q,(q-1)^-1]*sqrt(q-1).

Its second factor has basis (q-1)^k sqrt(q-1), k integer; differentiation
maps it to (k+1/2)(q-1)^(k-1) sqrt(q-1), bijectively. Thus M is de Rham
acyclic. Now invert q as well. The new open set is the product
(A1-{1,2}) times (A1-{0,1}); both factors have Euler characteristic -1.
The rank-one sign local systems have no horizontal global sections, and
each punctured affine curve has no cohomology above degree1. Therefore
each factor has one-dimensional H1, and M[q^-1] has one-dimensional H2
and no other cohomology. In particular localization destroyed acyclicity.

This is a finite manual check on the existing control, not a new control
family or a Keller realization. It already fails source coordinate-uniform
Bass torsion-freeness after q'=q-1; that older warning remains binding.

## Why the tempting geometric endpoint does not attach

If d>1 and N_g were acyclic and D irreducible, the Euler formula would
give chi(D)=1. For an irreducible affine curve this forces normalization
A1 and no multi-branch identifications, hence topological contractibility.
The classical Lin-Zaidenberg theorem gives polynomial weighted coordinates
for such a curve. This is an imported KNOWN endpoint, not a new discovery:
the campaign already records its no-homeomorphic-C nonproperness endpoint
in AUDIT's September2 integration. The proposed approach has not supplied
the missing localized acyclicity or an independent proof that Q is acyclic.
For reducible D, even chi(D)=1 does not justify this irreducible argument.

Nor may a weighted Euler operator at a singular curve origin automatically
be fed into normalized Bass: that target point must be in the actual image.
A radical section of an abstract connection is not automatically a source
polynomial or a class with the same multiplicative equation in R/A.

Cheapest decisive source test would be an actual argument controlling
H_DR(Q), not another verification of H_DR(N)=0 or another weighted-curve
classification. No such argument arose. No new canonical OPEN, FIRST,
source exclusion, all-F10 or JC2 result, or automatic descendant follows.

## Read scope and custody

Current-pin WHOLE sources: kummer-weyl-selection-astra-20260912.md,
a773517be4434f0a18e8fc80b35ac7cd739190fc98ff717a9557959a38557998;
kummer-coordinate-boundary-root-20260912.md,
63a7a070b6c7aac67635729980021a2de68b24d6bf31e5ec7071ecc49db27139;
keller-source-selection-astra-20260911.md,
aeaaff1c7ccb6224bca64b931b74a32f12c80d5ace7501c051afcd8b1af16f39
(all in xmodel). The last input supplies the exact source-intersection
argument; no new FIRST of those historical reports is claimed. Targeted
history searches excluded current live reports and recovered the older
Lin-Zaidenberg endpoint; no exhaustive novelty claim.

Primary theorem statement checked in Palka, arXiv:1405.5391v2, page1,
Theorem A: https://arxiv.org/pdf/1405.5391v2 . Abstract/version and opening
theorem only, not a whole-paper proof review. Standard comparison/Euler
facts above are named imports, not newly verified foundational theorems.
Current COORD517fca6f67f3d705f9b4045e10f9039aaf11bf3280dfd27bb90bf003ee4a3ead
and unchanged administrative finalizer0f6aaf7d549952de8f318bdd974ae4627e497783d809f94cfaba16607355cb8d
apply. Only manual reasoning, primary read-only browsing, inert text/hash,
apply_patch and finalizer; no scientific execution, worker, live-peer body,
protected tree, new agent or shared evidence promotion. Own WHOLE readback,
postpins and expected finalizer verification close this bounded test.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5449`.
- Body SHA-256:
  `8e040deccd1fdac59ff9eafca22f4da0c6226ad9f1b7774ee764811f4911c06d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
