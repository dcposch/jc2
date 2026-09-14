## 2. Weight-free centralizer

For either H, the rational centralizer of H is K(H) and its polynomial centralizer is K[H]. Here is the proof, including the field issue. Let h0 be transcendental. On the generic fiber H=h0, p is invertible. With `u=g/p`, `T=1/p`, its equation is

\[
T^5=V(u)/h_0,
\quad V(u)=u^3+1\ \text{or}\ (1+u)(1+tu)^2.
\]

Over an algebraic closure of K(h0), V has a SIMPLE zero: every zero in the Q case, and u=-1 in the golden case since t!=1. Eisenstein at that zero proves the polynomial in T irreducible over the corresponding rational function field. Its nonempty T-invertible locus is the generic fiber, so that fiber is geometrically integral. Consequently K(H) is relatively algebraically closed in K(g,p); a nontrivial separable algebraic subextension would split after algebraic closure and contradict geometric integrality.

Let `d=[H,-]/H_g`; H_g is not the zero polynomial and d(p)=1. The extension K(g,p)/K(H)(p) is finite. If d(z)=0, differentiate its monic minimal polynomial over K(H)(p). Its differentiated coefficients give a lower-degree vanishing polynomial, hence are all zero. Constants of p-differentiation in K(H)(p) are K(H), so z is algebraic over K(H), and therefore belongs to it. Finally, for coprime r,q in K[X], polynomiality of r(H)/q(H) and Bezout force q(H) to be a unit, hence q constant. This proves the polynomial assertion. A homogeneous polynomial centralizer of degree e is zero unless5 divides e, in which case it is a scalar H^(e/5). Nothing here uses reducedness of H=0 or receiver weights.

## 3. Canonical A reference and the global H² nondivisibility invariant

Define homogeneous dilations

\[
A_s=\sum_d s^{15-d}A_d,\quad B_s=\sum_d s^{25-d}B_d,
\qquad[A_s,B_s]=cs^{36}g^2.
\]

Give s,g,p combined degree1. Fix lexicographic g>p monomial division over K. The leading monomial of H is `kappa*g³p²`, where kappa=1 or rho, a fixed field unit.

Construct `R_s=H+sum_(a=1)^5 s^a R_(5-a)` successively. At stage a, take the order-a residual of A_s minus the cube of the reference built so far. It is homogeneous of ordinary receiver degree15-a. Divide it by3H², and use the quotient as R_(5-a). The quotient is homogeneous of degree5-a, and the remainder contains no monomial divisible by `g6p4`. Adding this reference coefficient changes its cube at order a by exactly3H²R_(5-a); all other changes have later s-order. Monomial division terminates, preserves total homogeneity, and uses only fixed field units. No assertion about receiver weight or a small g-degree is needed.

At order10 divide the degree5 residual of A_s-R_s³ by H. Its quotient is a scalar alpha. Subtract `alpha*s10*R_s`, and choose a0 at order15 to kill the remaining constant. Put

\[
F=A_s-R_s^3-\alpha s^{10}R_s-a_0s^{15}.           \tag{1}
\]

The first five residual coefficients stay H²-leading-monomial-normal; F10 is H-leading-monomial-normal; F15=0. All R4,...,R0, alpha and a0 are retained.

F is nonzero. Otherwise, over K(s), the nonzero bracket cs36g² factors as `(3R_s²+alpha*s10)[R_s,B_s]`. The first factor has receiver degree10, whereas the product has degree2, impossible in a polynomial domain. Hence `1<=j=ord_s F<=14`, and F_j is a nonzero homogeneous polynomial of degree15-j.

Crucially,

\[
                         H^2\nmid F_j.          \tag{2}
\]

For j<=5 its division remainder has no leading monomial divisible by the leading monomial of H²; a nonzero H² multiple cannot have that property. For j>=6, its total degree is below10. These two arguments cover every j without a missing middle range.

R_s need NOT be cubic in g: `H+s*g4` is a legitimate degree5 homogeneous-reference shape with g-degree4. This is a direct small countercontrol to importing the old cubic claim, not a source pair. No finite R-normal blocks with g-degree<=2 are asserted or used.

The normalization is load-bearing for (2): in an unnormalized candidate coefficient `F_5=H²`, every factor that is double in H would have multiplicity4, not2 or3. At stage5 its scalar quotient by3H² is1/3, so this exact term is absorbed into R0 rather than surviving as the first remainder. This is a symbolic single-coefficient control, not an expanded pair or a source point.

## 4. Exact B reference, all kernels, and first-contact divisibility

Write `alpha_s=alpha*s10`, and `b_i,s=b_i*s^(25-5i)`, i=0,...,4. In the following formulas suffixes s on scalar references are suppressed:

\[
f_B(R)=R^5+b_4R^4+b_3R^3+b_2R^2+b_1R+b_0,
\quad q(R)=\tfrac53R^2+\tfrac43b_4R+b_3-\tfrac59\alpha,
\]
\[
\tau=2b_2-\tfrac43b_4\alpha,\qquad
\delta=b_1-b_3\alpha+\tfrac59\alpha^2,
\quad G=B_s-f_B(R_s)-q(R_s)F.
\]

Thus `ord alpha>=10`, `ord tau>=15`, `ord delta>=20`; all terms have their indicated combined homogeneity, and G0=0 by the common top. Since `f_B'=(3R²+alpha)q+tau R+delta`, exterior differentiation in independent R,F,G gives the EXACT identity

\[
[A_s,B_s]=[R_s,\mathcal T]+[F,G],
\quad \mathcal T=(3R_s^2+\alpha)G-(\tau R_s+\delta)F
 -(\tfrac53R_s+\tfrac23b_4)F^2.                 \tag{3}
\]

The dR wedge dF, dR wedge dG and dF wedge dG coefficients are respectively `-(tau R+delta)-q'F`, `3R²+alpha`, and1. In particular no b4, alpha or constant-kernel term was dropped.

If the first G_l occurs below2j, its equation in (3) is `[H,3H²G_l]=0`. All F² terms begin at2j; `15+j>2j` for j<=14; and `[F,G]` begins after l. Hence G_l centralizes H. Its degree25-l permits only l=5,10,15,20,25, with respective leaders H4,H3,H2,H,1. Remove these successively by changing the corresponding scalar b_i. For scalar increment e, the exact changes to G are

\[
-es^5(R_s^4+\tfrac43R_sF),\quad
-es^{10}(R_s^3+F),\quad-es^{15}R_s^2,\quad
-es^{20}R_s,\quad-es^{25}.
\]

Each alters only its designated and later orders, and preserves the tau/delta bounds. This finite induction proves `ord G>=2j`, with infinity allowed. It is a change of reference decomposition, not a target shear that silently omits alpha or a0 corrections.

At order2j<36,

\[
[H,3H^2G_{2j}-\tfrac53H F_j^2]=0.              \tag{4}
\]

The inner polynomial has degree35-2j. For integer1<=j<=14, its only possible nonzero homogeneous centralizer values are a scalar H5 at j5 or scalar H3 at j10. Otherwise it is zero. All are divisible by H², so (4) yields

\[
H\mid F_j^2,\qquad D:=\operatorname{rad}(H)\mid F_j. \tag{5}
\]

The second implication uses that every multiplicity in H is either1 or2. Therefore j<=11 for `D_Q=p(g³+p³)` of degree4 and j<=12 for `D_G=pLM` of degree3. If `H|F_j`, j>10 is ruled out by degree and j10 by the chosen H-normal remainder. Thus

\[
H\mid F_j\ \Longrightarrow\ 1\le j\le9,\quad
F_j=HC,\quad \deg C=10-j,
\quad H\nmid C.                                \tag{6}
\]

The last assertion is (2). There is deliberately no additional g-degree or weight bound on C.

