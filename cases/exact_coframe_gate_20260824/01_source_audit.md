# Primary-source audit — EXACT-COFRAME-GATE-20260824

Source check performed after reading the frozen synthesis and before final reporting. These sources support the witness and tame-generation premises; the bridge theorem and the Broughton-row no-go are proved directly in the final report.

## Cohn witness

P. M. Cohn, “On the structure of the GL2 of a ring,” Publications Mathématiques de l'IHÉS 30 (1966), 5–53.

- DOI: https://doi.org/10.1007/BF02684355
- Open primary text: https://www.numdam.org/item/PMIHES_1966__30__5_0/
- PDF: https://www.numdam.org/item/PMIHES_1966__30__5_0.pdf

Cohn's section 8 gives the degree/order obstruction showing that a two-variable polynomial ring is not GE2. The standard determinant-one witness used in the later literature is

[[1+xy,x^2],[-y^2,1-xy]].

The present report does not rely on a quotient of SL2 by E2.

## Executable leading-term nonmembership certificate

Hyung-Ju Park, “A Computational Theory of Laurent Polynomial Rings and Multidimensional FIR Systems,” University of California, Berkeley memorandum UCB/ERL M95/39 and PhD dissertation, 1995.

- Primary PDF: https://www2.eecs.berkeley.edu/Pubs/TechRpts/1995/ERL-95-39.pdf
- Theorem 5.2.1 and the Cohn replay are on printed pages 52–53.

Park proves the following necessary condition for an elementary factorization of a matrix in SL2(k[x1,...,xm]): when the leading-term matrix has rank one, one leading row must be a monomial multiple of the other. For the Cohn matrix, the leading rows are x(y,x) and -y(y,x); neither is a polynomial or monomial multiple of the other. This is a finite, directly checkable nonmembership certificate.

The journal algorithm is:

Hyungju Park, “A Realization Algorithm for SL2(R[x1,...,xm]) over the Euclidean Domain,” SIAM Journal on Matrix Analysis and Applications 21 (1999), 178–184.

- DOI: https://doi.org/10.1137/S0895479897331096

Its abstract states that the algorithm decides precisely whether a given SL2 matrix over the stated polynomial ring factors into elementary matrices and produces the factorization when it exists.

## Current Cohn-lineage cross-check

Y. Chapovskyi, O. Kozachok, and A. Petravchuk, “Decomposition of matrices from SL2(K[x,y]),” arXiv:2412.03688, current manuscript date 2026-03-22.

- Abstract and primary manuscript: https://arxiv.org/abs/2412.03688

The paper explicitly records the Cohn matrix

[[x^2,xy-1],[xy+1,y^2]]

as non-elementary. It is related to the standard witness C by

C(x,-y) [[0,-1],[1,0]]
  = [[x^2,xy-1],[xy+1,y^2]].

The constant rotation is elementary:

[[0,-1],[1,0]] = U(-1)L(1)U(-1).

Thus the two displayed forms have the same literal nonmembership lineage using only a ring automorphism and explicit elementary multiplication.

## Jung–van der Kulk

W. van der Kulk, “On polynomial rings in two variables,” Nieuw Archief voor Wiskunde 1 (1953), 33–41.

This is the original arbitrary-field tame-generation source.

Nguyen Van Chau, “A Simple Proof of Jung's Theorem on Polynomial Automorphisms of C2,” Acta Mathematica Vietnamica 28 (2003), 209–214.

- Primary preprint: https://arxiv.org/abs/math/0408077

The abstract states the exact generation theorem used here: every polynomial automorphism of C2 is a finite product of linear automorphisms and shears (x,y) maps to (x+p(y),y). The final report derives tame-to-E2 from this statement by the chain rule and explicit constant normalizers.

## Wright priority: the weak Jacobian theorem

D. Wright, “The amalgamated free product structure of GL2(k[X1,...,Xn]) and the weak Jacobian theorem for two variables,” Journal of Pure and Applied Algebra 12 (1978), 235–251.

- Publisher record: https://www.sciencedirect.com/science/article/pii/0022404987900041
- DOI: https://doi.org/10.1016/0022-4049(87)90004-1
- Author's publication record: https://www.math.wustl.edu/~wright/math_publications.html

The publisher record confirms the title, journal, volume, issue, year, and pages. The publisher did not expose the article body to this audit. The exact theorem statement is independently printed, with attribution to Wright's Theorem 6 on page 250, in the primary research article below: if p,q are two-variable polynomials and their full Jacobian matrix belongs to GE2, then p,q generate the polynomial algebra and hence are coordinate polynomials.

V. Shpilrain and J.-T. Yu, “Polynomial Automorphisms and Gröbner Reductions,” Journal of Algebra 197 (1997), 546–558.

- DOI and publisher record: https://doi.org/10.1006/jabr.1997.7083
- Author-hosted primary PDF: https://shpilrain.ccny.cuny.edu/paperyu.pdf
- Wright's theorem is restated on printed page 6 (PDF page 5), immediately before Proposition 2.4.

Consequently, for a determinant-one full polynomial Jacobian over C[x,y], Wright supplies the converse to tame-to-elementary: membership in GE2 implies that the map is an automorphism. In determinant one, GE2 membership is equivalent to E2 membership because diagonal constants normalize E2 and every determinant-one constant diagonal matrix is elementary. Thus the exact-coframe E2/non-E2 dichotomy is prior art, not a new bridge in this gate.

### Hostile control for the claimed arbitrary-second-row strengthening

Shpilrain–Yu Proposition 2.4 goes further and prints the claim that if

    J = [[d1(p),d2(p)],[s1,s2]]] in GE2,

then not only is p a coordinate, but the arbitrary second row equals the gradient of a polynomial q and p,q generate the algebra. The latter assertion is false as printed. Take

    p=x,
    J=L(y)=[[1,0],[y,1]] in E2.

The first row is the gradient of x, but the second row (y,1) is not closed: partial_y(y)=1 while partial_x(1)=0. Hence no polynomial q has that gradient. This control does not contradict Wright, whose premise is a full Jacobian, and it does not contradict the coordinate conclusion for p=x. The final report does not use Proposition 2.4 or its arbitrary-row assertion.

## Broughton control

S. A. Broughton, “Milnor numbers and the topology of polynomial hypersurfaces,” Inventiones Mathematicae 92 (1988), 217–242.

- DOI: https://doi.org/10.1007/BF01404452
- Bibliographic primary record: https://eudml.org/doc/143566

The polynomial P=x+x^2y is the standard Broughton example. For this gate, the two properties actually used are checked directly:

- P_x=1+2xy and P_y=x^2 have no common zero, so P has no affine critical point;
- P^(-1)(0) is the union of x=0 and 1+xy=0, so P is not a coordinate polynomial.

No topological theorem from the Broughton paper is used as an algebraic premise.
