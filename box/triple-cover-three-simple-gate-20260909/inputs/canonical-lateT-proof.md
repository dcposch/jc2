# Triple-profile late contact: a finite centralizer lemma and exclusion of j=12

September 9, 2026. **NEW PURE-PROOF RESULT / PROVISIONAL, NOT INDEPENDENTLY GATED.** The late-contact lemma is proved below, the ordinary reference construction is re-established for the distinct triple profile, and its canonical first-contact order12 is impossible. No contact order1–11, cubic unfolding, whole receiver family, original Keller source, or JC2 is excluded by this packet.

## 1. Exact input and source perimeter

Work over any characteristic-zero field K. Set L=p-g and H=p²L³. The theorem concerns ordinary polynomials

\[
A,B\in K[g,p],\quad \deg A=15,\quad\deg B=25,
\qquad A_{15}=H^3,\quad B_{25}=H^5,
\qquad[A,B]_{g,p}=cg^2,\quad c\in K^* .       \tag{S}
\]

The convention is [U,V]=U_g V_p-U_p V_g, with A the LOW component. This is an actual total-degree statement, not partial degree, a Laurent face, or a weighted-degree label. No parity, receiver-weight, polygon, inner-face or inverse-lift assumption is used.

The accepted actual-Moh receiver producer07e53340... and gateeade8ec8... supply (S) conditionally from the named ordinary125/75 parent with M=(-75,105,123), d=(125,25,5,1), V=(2,4,1), the named effective child (25,15;M2'=21,V2'=2;k=2), and its triple nonzero-slope stratum. Their simultaneous polynomial centering/shears preserve ordinaryness and the monomial Jacobian, normalize H=p²(p-g)³, and establish actual total degrees25/15. Their high/low naming has [P,Q]=c_old*g²; here A=Q,B=P, so c=-c_old remains nonzero. The child-data transport and the stated use of Moh's major-packet theorem on its transformed monomial-J child remain the accepted external dependencies. No claim is made that the triple stratum is attained or that a receiver point reversely lifts.

The accepted weight-free source report cbc0330b... covers ONLY its squarefree-Q and golden H patterns. It was read whole as a framework to audit, not invoked as a theorem about the present H. The centralizer and all required reference identities are proved afresh below. The whole four charged reports, including the terminal source-multiplicity intake909ba868..., were hash-checked before bodies and read to their endings. Full paths/hashes are in input-pins.json. No current blind, live gate, or pending theorem is a premise.

## 2. Centralizer of the triple H

Put u=pL. In the function field one has the rational inverse

\[
L=H/u^2,\qquad p=u^3/H,\qquad g=u^3/H-H/u^2.
\]

Thus K(g,p)=K(H,u); H and u are algebraically independent. Direct differentiation of the degree<=5 factors gives

\[
[H,u]=-H.
\]

Consequently the derivation [H,-] is -H times u-differentiation on K(H)(u). Its constants are precisely K(H), in characteristic zero. If a rational function r(H)/q(H), with coprime r,q in K[X], is a polynomial in g,p, Bezout for r,q makes q(H) a polynomial unit. This forces q constant. Therefore

\[
\ker([H,-]:K[g,p]\longrightarrow K[g,p])=K[H]. \tag{1}
\]

In particular a homogeneous centralizer of ordinary degree e is zero unless e=5i for an integer i>=0, when it is a scalar multiple of H^i. This proof uses neither a simple factor nor geometric reducedness of H=0. No algebraic extension or coefficient localization is required; the temporary rational coordinates are used only to prove (1).

## 3. Independent finite late-contact lemma

**Lemma.** Let H be nonconstant homogeneous of degree D>0 over K, with polynomial centralizer K[H]. Give s,g,p degree1. Let R in K[s,g,p] be combined-homogeneous of degree D with R(0,g,p)=H. Let T be a polynomial of combined degree at most N. If

\[
\operatorname{ord}_s[R,T]>N,                 \tag{2}
\]

then [R,T]=0. For T combined-homogeneous of degree N, it is in fact a finite sum of terms a_i s^(N-Di)R^i with a_i in K and 0<=Di<=N.

**Proof.** First suppose T homogeneous. If its first nonzero coefficient is T_l at order l, then l<=N. Condition (2) forces [H,T_l]=0. Since T_l has degree N-l, (1)'s analogue gives T_l=a H^i and l=N-Di. Subtract a s^l R^i from T. This preserves the bracket, polynomiality and combined degree N, while strictly increasing the s-order. Repeat. The process is finite: a nonzero polynomial of combined degree N cannot have s-order>N. Thus the eventual remainder is zero, proving the displayed finite representation and the bracket claim. If T is only bounded in combined degree, split it into its homogeneous pieces. Their brackets with R have distinct combined degrees, so (2) holds for each piece with its own (smaller) N, and the homogeneous proof applies. Zero T and infinite bracket order are included. This is finite polynomial subtraction, not convergence, formal integration, or a claim about arbitrary series.

Two manual changed-object controls locate the hypotheses. If the centralizer hypothesis is dropped, R=g³+s²p and T=g have combined degrees3 and1, while [R,T]=-s² has order2>1 and is nonzero: H=g³ has the larger centralizer K[g]. If the true degree bound is dropped, R=g and T=s²p have bracket s², but T has combined degree3, not the falsely assigned N=1. Neither object satisfies the omitted hypothesis. These are hand-checked degree<=3 controls; no executable test or mathematical subprocess was run. The strict threshold in (2) is sufficient; optimality is not claimed.

## 4. Ordinary reference construction for (S)

Use the genuine homogeneous dilations

\[
A_s=\sum_{d=0}^{15}s^{15-d}A_d,\quad
B_s=\sum_{d=0}^{25}s^{25-d}B_d,
\qquad[A_s,B_s]=cs^{36}g^2.                 \tag{3}
\]

They have combined degrees15/25. Construct

\[
R=H+\sum_{a=1}^{5}s^a R_{5-a}
\]

by successive ordinary monomial division of the order-a residual of A_s-R³ by 3H², for a=1,...,5, with fixed lex order g>p. The quotient has degree5-a; add it as R_(5-a). The new cube changes that order by exactly 3H²R_(5-a), and changes other terms only later. Division uses fixed field units and terminates. The first five residuals are leading-monomial-normal for H². For this H the leading monomials are -g³p² and g⁶p⁴, respectively. No small g-degree property of R is asserted.

At order10 divide the degree5 residual A_s-R³ by H and call its scalar quotient alpha. Put alpha_s=alpha*s10 and subtract alpha_s R. Choose a0 to remove the remaining constant at order15. Then

\[
F=A_s-R^3-\alpha_sR-a_0s^{15}               \tag{4}
\]

is combined-homogeneous of degree15, its coefficients1–5 retain H²-normality, its coefficient10 is H-normal, and F15=0. It is nonzero: otherwise the nonzero bracket in (3), over K(s), factors as (3R²+alpha_s)[R,B_s]. Its first factor has ordinary receiver degree10, impossible for a nonzero polynomial product of degree2. Therefore

\[
1\le j=\operatorname{ord}_sF\le14,
\qquad \deg F_j=15-j,
\qquad H^2\nmid F_j.                       \tag{5}
\]

The last assertion follows from normality when j<=5 and degree<10 when j>=6. This reference changes no actual source pair; a0 is an additive target constant and all other operations are identities decomposing that fixed pair. A single coefficient H² at order5, if present before normalization, would be absorbed by R0=1/3; it cannot be counted as a normal first remainder. This is a formal coefficient control, not an expanded source.

## 5. All B kernels and the exact wedge identity

Choose scalars b_i in K for i=0,...,4, write b_i,s=b_i*s^(25-5i), and suppress the s subscripts below (including on alpha). Define

\[
f_B(R)=R^5+b_4R^4+b_3R^3+b_2R^2+b_1R+b_0,
\]
\[
q(R)=\tfrac53R^2+\tfrac43b_4R+b_3-\tfrac59\alpha,
\quad \tau=2b_2-\tfrac43b_4\alpha,
\quad \delta=b_1-b_3\alpha+\tfrac59\alpha^2,
\quad G=B_s-f_B(R)-q(R)F.                  \tag{6}
\]

Here ord alpha>=10, ord tau>=15, ord delta>=20. Differentiating in g,p only gives f_B'=(3R²+alpha)q+tau R+delta. Expanding just the formal wedge dA wedge dB, not a polynomial pair, yields

\[
[A_s,B_s]=[R,T]+[F,G],
\quad
T=(3R^2+\alpha)G-(\tau R+\delta)F
 -(\tfrac53R+\tfrac23b_4)F^2.              \tag{7}
\]

Indeed the dR wedge dF coefficient is -(tau R+delta)-q'F; the dR wedge dG and dF wedge dG coefficients are 3R²+alpha and1. Each term of T has combined degree35. This retains b4,b2,alpha, both lower kernels and the constant reference; it is not the odd-only B reference.

The b_i can be selected with

\[
\operatorname{ord}_sG\ge2j.                \tag{8}
\]

To prove this, if a first G_l occurs below2j, the order-l equation in (7) is [H,3H²G_l]=0: F² starts at2j, (tau R+delta)F later than2j because 15+j>2j, and [F,G] starts after l. The target begins at36>2j. Thus G_l centralizes H. Its degree25-l permits only l=5,10,15,20,25, with scalar multiples of H4,H3,H2,H,1. Changing the corresponding b_i by e removes that leading coefficient. The exact changes to G are, respectively,

\[
-es^5(R^4+\tfrac43RF),\quad
-es^{10}(R^3+F),\quad-es^{15}R^2,\quad
-es^{20}R,\quad-es^{25}.
\]

These changes preserve all earlier orders and the stated tau/delta bounds. The finite leading-order induction proves (8), allowing G=0. This is adjustment of reference scalars, not an unlicensed target shear.

At order2j, (7) consequently gives

\[
[H,3H^2G_{2j}-\tfrac53HF_j^2]=0.           \tag{9}
\]

The inner homogeneous degree is35-2j. Within1<=j<=14, its only possible nonzero centralizer values are a scalar H5 at j5 or H3 at j10. They are both divisible by H²; hence (9) implies H|F_j². For the PRESENT multiplicities (2,3), unique factorization gives the stronger conclusion

\[
pL^2\mid F_j,\qquad j\le12.               \tag{10}
\]

It is the ceiling of half of each multiplicity, not a borrowed simple/double-factor cover. At j12, degree3 forces

\[
F_{12}=\lambda pL^2,\qquad\lambda\in K^*.  \tag{11}
\]

No other source stratum, normalization or field root is required for this implication.

## 6. The late endpoint is impossible

Assume j=12. In (9) the inner degree is11, which is not divisible by5, so its centralizer value is zero. With (11), this gives exactly

\[
G_{24}=\tfrac59\frac{F_{12}^2}{H}
       =\tfrac59\lambda^2 L.               \tag{12}
\]

By (8), [F,G] has s-order at least36. Equation (3) and the exact identity (7) therefore show

\[
\operatorname{ord}_s[R,T]\ge36>35.
\]

T is a finite polynomial of combined degree35, and R satisfies the independent lemma with D=5 and the centralizer proved in §2. The lemma gives

\[
[R,T]=0\quad\hbox{exactly},\qquad
[A_s,B_s]=[F,G].                            \tag{13}
\]

There are no hidden later scalar kernels in this step: the lemma subtracts every permitted homogeneous kernel finitely. Neither T=0 nor the vanishing of its reference coefficients is asserted or needed.

For clarity, all still-allowed tail coefficients remain visible. Combined degrees and the chosen constants give

\[
F=s^{12}f_3+s^{13}f_2+s^{14}f_1,
\qquad G=s^{24}g_1+s^{25}g_0,
\]

where f3=lambda*pL², g1=(5/9)lambda²L, and g0 is a scalar (which may also be absorbed in b0). The coefficient of s36 in (13), unaffected by f2,f1,g0, is therefore

\[
cg^2=[\lambda pL^2,\tfrac59\lambda^2L]
     =\tfrac59\lambda^3L^2.                \tag{14}
\]

The sign is positive: L_g=-1,L_p=1, and [pL²,L]=L². Reversing the component order reverses both bracket conventions, not the mismatch of linear factors. Equation (14) is impossible: evaluate at g=p=1 to obtain c=0, contrary to (S). Equivalently, its p² coefficient would force lambda³=0 in the field. The s37/s38 equations would impose [f2,g1]=[f1,g1]=0, but they were not silently assumed or used to obtain the contradiction.

Thus the exact claim that the Jacobian becomes (5/9)lambda³L² is licensed at its degree-two/s36 coefficient first; the lower-degree terms have been explicitly retained. There is no unsupported assertion that F consists solely of its order12 coefficient. An example with the sign reversed would change (14)'s scalar, never turn L² into g². These are manual changed-object/sign checks of the actual coefficient equation, not a reported executable mutation suite.

## 7. Outcome and strict stopping scope

The general finite late-contact lemma, the triple-profile ordinary reference/wedge construction, (10), and the j12 exclusion are proved here as new statements pending independent review. Relative to the accepted actual-Moh source map, they exclude ONLY this canonical late-contact endpoint of the named conditional triple receiver. The surviving possible canonical orders are1–11; none has been analyzed here. No whole triple stratum, full Moh125 branch, all15/25 family, all-degree theorem, reverse Keller lift, scheme ideal, radical/unit certificate or JC2 conclusion follows from this packet.

All algebra was factored prose or a formal exterior/coefficient identity. No mathematical subprocess, Python/SymPy/CAS control, high H/R power or full A/B pair was materialized; no full source/row stream, AWS/SSH/web, new agent, current round body, live gate, shared ledger or protected project was accessed. Only bounded -I -B metadata scripts performed hashing and begin/close/finalize/verify. Input pins are checked before and after publication; custody records owned paths and writers. The four source reports were read whole at the exact pins; their upstream published source proofs are imported only at the accepted gate's explicitly named scope, not newly replayed. All writers are IDLE after sealing. Stop by01:38 UTC; no dependent task is launched.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13352`.
- Body SHA-256:
  `85e1528727b56c00881f8cbcb5a8d7eb101a48ecd9c62be4afb05ccd2cf2c3dc`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
