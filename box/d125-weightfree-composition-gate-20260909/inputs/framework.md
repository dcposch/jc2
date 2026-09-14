# Degree15/25 weight-free reference framework and conditional factor cover

September 9, 2026. **NEW SOURCE FRAMEWORK PROVED HERE / UNREVIEWED. CONDITIONAL CASE COVER, NOT A RECEIVER EXCLUSION.** The ordinary-degree reference construction and factor-cover arithmetic survive removal of ALL weights and polygon bounds. The local exclusions and double-chart resonance comparison are separate obligations, explicitly not premises proved in this packet.

## 1. New hypotheses and exact dependency boundary

Let K be a characteristic-zero field. In the golden case require either root rho of `rho²-3rho+1=0` in K and put `t=1-rho`. Set either

\[
H_Q=p^2(g^3+p^3),\qquad
H_G=p^2LM^2,\quad L=p+g,\ M=p+tg.
\]

Assume ONLY

\[
A,B\in K[g,p],\quad \deg A=15,\ \deg B=25,
\quad A_{15}=H^3,\ B_{25}=H^5,
\quad[A,B]_{g,p}=cg^2,\ c\in K^* .              \tag{S}
\]

There is no receiver-weight condition, prescribed inner face, polygon restriction, parity, origin normalization or lift equation. In particular no bound `deg_g C<=2`, cubic-in-g R reference, or old normal-remainder branch injection is imported.

The three pinned inputs were verified before bodies: whole accepted golden source SHA `14c4cdeddf9b1166046759022378775fc7ebc147c7d939579cf93f6b78aa51c6`; whole frozen AUDIT15m SHA `b02ae267bb8cfef6956d6e0cec0b6188196b222d3d9d78e3d1582f4a5cc1a440`; whole minimal-receiver report SHA `7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413`. Exact paths are in input-pins.json. Their weighted exclusions are NOT invoked to prove a weight-free conclusion. Their algebraic identities are rederived below; the receiver input only describes which existing normalized objects would meet (S). No pending simple-L, coalesced/separated M or other producer is a premise.

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

## 5. Weight-free local-chart interface, not a local exclusion

Pass to an algebraic closure of K when factoring H. Its simple factors and double factors are:

| H | simple factors | double factors | deg D |
|---|---|---|---:|
| Q | the three distinct linear factors of g³+p³ | p |4|
| golden | L | p and M |3|

Every factor is transverse to a suitable generic affine line coordinate y: use x=g,y=p for V/L/M roots and x=p,y=g at p=0. At a simple root, the formal inverse `R_s(x,y)=z` exists over Kbar(y)[[s,z]] because the transverse derivative of H is nonzero. If F_j=HC and the C value there is nonzero, its first source coefficient in z has exact local order1.

At any double factor, the critical-point equation has a formal solution x_c(s,y). Put xi=R_s(x_c,y). **Without assuming R_s cubic**, Taylor factorization gives

\[
R_s(x_c+w,y)=\xi+w^2 U_s(w,y),\qquad
U_0(0,y)=H_{xx}(x_0,y)/2\ne0.
\]

Taking the formal square root of this unit gives `zeta=w sqrt(U_s)` and an inverse with nonnegative s-orders. A finite algebraic coefficient extension suffices; in these homogeneous degree5 charts the initial unit is a nonzero constant times y³. The resulting Morse identity `R_s=xi+zeta²` has combined degree5, with zeta of degree5/2. General higher w terms do not invalidate the formal inverse or its order bounds.

If the transverse multiplicity of F_j at that factor is d, then in the FULL transformed F Taylor series the coefficient of zeta^d has order exactly j, all lower-index coefficients have order greater than j, and every coefficient has order at least j. This follows by taking the s^j coefficient after the formal substitution; its leading transverse coefficient is multiplied by a nonzero d-th power of the inverse linear coefficient. It does not discard later moving constants or infer any coalesced/separated condition.

The transformed nonzero bracket starts at order36 in each generic Morse chart. At p=0 use `[A,B]_(p,g)=-c*g²`, so its generic target is nonzero, not zero. At M and every simple V/L root, g is a nonzero scalar multiple of the tangent variable. The formal coordinate derivative is a unit at s=zeta=0. This supplies exact chart conventions to a future local proof.

Also `B_s-R_s^5 in sK[s,g,p]` holds from the common top alone. Therefore every coefficient of its full Morse Taylor expansion has s-order at least1. This potentially useful uniform bound is proved here; no local Newton balance or exclusion is inferred from it alone.

## 6. Exact factor cover CONDITIONAL on separate local lemmas

The following is a logical reduction, NOT proof of the listed consumers.

1. **H-divisible, simple value:** if a simple factor fails to divide C, the unramified chart has nonzero local C value with j<=9. A local simple-root exclusion would eliminate this case. Conditional on that exclusion, every simple factor divides C.
2. **H-divisible, double value:** if any double factor T fails to divide C, `ord_T F_j=2`, with j<=9. A local d2 theorem covering both coalesced and separated regimes would eliminate this case.
3. **H-divisible, remaining case:** if all simple and all double factors divide C, then D|C. Thus j<=6 in Q and j<=7 in golden by total degree alone. If every double factor also had T²|C, then H|C, contradicting (6). Hence some double factor has `ord_T C=1`, giving `ord_T F_j=3`, j<=7. A local d3 theorem covering both regimes would finish this branch. The proposed strict margins `15r<=5j<=35<36` and `7eta+kappa/2<5j` are compatible with this arithmetic but their analytic hypotheses/inequalities must be proved by that theorem; they are not established here.
4. **Non-H-divisible:** (5) ensures every simple factor already divides F_j. Consequently H∤F_j can occur only at a double factor with exact `ord_T F_j=1`. The degree bound is j<=11 in Q, j<=12 in golden. A local d1 theorem excluding j<=11 would leave only golden j12. This claim is not imported from weighted15m.
5. **Golden last endpoint:** at j12 the total degree of F12 is3 and D has degree3, hence `F12=lambda*pLM`, lambda in K*, without normal-remainder or weight assumptions. Its multiplicity is exactly1 at BOTH double factors p and M. Therefore any d1 classification must apply at both charts, not merely at one chosen factor. A separate two-chart resonance contradiction would close this final conditional leaf.

For use by that separate consumer, the exact degree<=5 source projections at the last endpoint are

| transverse/tangent coordinates | quadratic H coefficient | transverse F12 derivative | bracket convention |
|---|---|---|---|
| x=p,y=g at p=0 | rho*y³ | lambda*t*y² | -c*y² |
| x=g,y=p at M=0 | t(t-1)*y³ | lambda*(t-1)*y² | c*y²/t² at the root |

These give, after a Morse square root a, the linear coefficients `lambda*t/a` with a²=rho and `lambda*(t-1)/a` with a²=t(t-1), times y^(1/2). Both are nonzero for both rho embeddings. The proposed competing values of c require the separate resonant initial analysis; this packet neither assumes its equality-order hypotheses nor consumes a weighted-face coefficient equation.

## 7. Conclusion, limits and custody

The canonical framework, (2), (5), (6), chart availability and factor cover are proved using only ordinary degrees, top forms, full bracket identity and characteristic zero. No weight-dependent remainder injection survives by assertion. The framework has no identified gap at this scope; the first missing arrows for a COMPLETE weight-free exclusion are precisely the local simple/d1/d2/d3 consumers with all moving orders retained, and the golden two-chart equality consumer.

If those independent obligations were proved, this case cover would apply to every polynomial receiver with the two monic top patterns, irrespective of its polygon. The accepted minimal receiver statement supplies such tops for all six normalized receiver families. This is a CONDITIONAL applicability observation, not a new all-six exclusion, all-degree theorem, properness result, computed unit certificate or announcement about JC2. Necessity from an original source retains its existing external hypotheses. Nilpotent coefficient schemes are not covered by this field/UFD argument.

No mathematical subprocess, full high power, A15/B25 source or 6/10 pair expansion was performed. The small `H+s*g4` shape and the table are prose factor/degree controls, not an executable mutation suite or source point. Only bounded metadata/publication Python -I -B operations ran; no CAS/AWS/SSH/web, live peer body, new agent, shared/protected edit or external action. Three input pins are checked again at publication. Whole substantive proof is complete; terminal transaction/custody record all owned files. STOP/IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15307`.
- Body SHA-256:
  `47e59373e6d43fc6e4149ef99927a30587f44a93aa7a330def436b4f214b0d89`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
