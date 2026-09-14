# F9-j1 opposite-edge transport to an ordinary 21/35 monomial-J receiver

Author: Astra, /root/nonemptiness_certificate. 2026-09-09. Basis 0d39df3c9fd69c939a8420c54d03228b9077777d.

## Outcome: PROVISIONAL source-map candidate

For the explicitly **ordinary rectangular standard F9 (3,5) source** specified below, the opposite-edge construction does extend. There are parameters r in K and lambda in K*, target constants, and ordinary polynomials A(g,p),B(g,p) with

    [A,B]_(g,p)=c*g,
    N(A)=3*conv{(0,0),(2,0),(3,1),(0,7)},
    N(B)=5*conv{(0,0),(2,0),(3,1),(0,7)}.

Thus their actual total degrees are **21 and 35**, with unique total leaders proportional to p^21,p^35. These are not 15/25 receivers and do not have constant Jacobian. No receiver exclusion, complete ideal, point, properness, or arbitrary-84/140 coverage is claimed. This is one provisional mathematical implication requiring independent review, not a verbatim quotation of GGHV Proposition 4.4 for (3,5).

The exact composite, apart from harmless output constants, is

    A(g,p)=P0(g^3*p+lambda*g^2-r, g^(-1)),
    B(g,p)=Q0(g^3*p+lambda*g^2-r, g^(-1)).                  (1)

The proof below supplies ordinaryness of (1), rather than assuming it from the formal substitution. All original nonzero corner coefficients and c remain nonzero. No output normalization c=1 is imposed.

## 1. Source, first fractional child, and normalization

Assume P0,Q0 in K[u,v], char K=0, [P0,Q0]=c!=0. They are an ordinary standard (3,5)-pair with actual degrees 84,140; starting normalized endpoints A0=(7,21), A0'=(1,0), direction (7,-2), selected F9 successor A1=(11/7,2). Explicitly require the rectangular bounds

    deg_u P0<=21, deg_v P0<=63;
    deg_u Q0<=35, deg_v Q0<=105,

and nonzero corner coefficients at (21,63),(35,105). Their unique total leaders then have the indicated monomial shapes. This is the rectangular version of the preceding source intake. If only a bare standard endpoint or monomial-total-top hypothesis is supplied without these rectangular bounds, this report does not silently supply the missing rectangle normalization. In particular this is not a theorem about every arbitrary actual 84/140 pair.

The preceding intake's licensed first cut is v->v+lambda1*u^(-2/7), with lambda1!=0, in L^(7). Its t=u^(1/7) child has Jacobian 7c*t^6. To apply ordinary-plane facts on the opposite side we **first undo this cut** in L^(7), returning to the known P0,Q0 in K[u,v]. The opposite-side construction is not an ordinary-plane argument on the fractional child. The new parameter lambda in (1) is not identified with lambda1.

We need pure leading-v coefficients, not merely a rectangular corner. Write the v-leading coefficients of P0,Q0 as f(u),h(u), of degrees 21 and 35. GGV Theorem 2.6 at weight (0,1) gives a polynomial Euler element v*a(u) for P0. Hence

    63 a'(u) f(u) - a(u) f'(u) = f(u).                    (2)

If deg a=k>=1, its highest coefficient in the left side has factor 63k-21, nonzero; comparing degrees in (2) forces k=1. A constant a gives too small a degree and is impossible. Write a=A*u+B. Then 42A=1 and (2) gives

    f(u)=alpha*(u+r)^21,   r=B/A.

The highest-v part of the constant bracket gives 105 f' h-63 f h'=0, so

    h(u)=beta*(u+r)^35.

All statements can first be proved over an algebraic closure. The shift parameter descends to K: r is the coefficient of u^20 in f divided by 21 times its leading coefficient. Set P(u,v)=P0(u-r,v), Q(u,v)=Q0(u-r,v). This is a determinant-one polynomial automorphism. It preserves the rectangle, total degrees, both corner guards and all highest-u coefficients. It strictly lowers (7,-2)-weight on every changed term, so the entire starting face, its two endpoints, selected root data and standard-pair conditions are preserved. Now the highest-v terms are exactly alpha*u^21*v^63 and beta*u^35*v^105.

Swap (x,y)=(v,u), and write the resulting ordinary pair as Ps,Qs. The bracket is -c. For each multiplier m=3 or 5 the unique maximal-x and maximal-y vertex is

    C_m=(21m,7m).

The uniqueness of the maximal-x point is what the common shift just supplied. Uniqueness of the maximal-y point also follows directly from the starting-face bound: at j=7m, -2i+7j<=7m forces i>=21m, while the rectangle gives i<=21m. The initial direction becomes d0=(-2,7); its normalized start is (21,7) and its other endpoint is (0,1). Total-degree and y-degree ratios are 3/5, as required by the opposite-edge corollary.

## 2. The exact q=7 import and every range hypothesis

The first corner is type II.b, so GGV Theorem 7.6(3), including its i=0 clause, applies to the polynomial Euler element E of Theorem 2.6 at (7,-2). Its end is parallel to A0, while its weight is 5 and A0 has weight 7. Therefore

    en_(7,-2)(E)=(5,15)=(5/7)*(7,21).

After the swap the correct Euler element is minus the swapped E (the swap reverses the bracket). Its start is (15,5)=(5/7)*(21,7). The reduced denominator is q=7, independently of the particular table parameter j.

Here is the complete application of GGV Corollary 7.4 (arXiv:1401.1784v3, printed pp.41–42):

| hypothesis | supplied datum |
|---|---|
| P,Q in L^(l), constant unit bracket | initially ordinary Ps,Qs, l=1, bracket -c |
| coprime m,n>1 | 3,5 |
| total-degree and y-degree ratios m/n | 84/140 and 21/35 |
| d0 in V>=0 and in Dir(P), positive value | (-2,7), sum 5, value 7m, nontrivial starting edge |
| common normalized start in Z x N | (21,7) |
| b<a | 7<21 |
| Euler start (p/q)(a,b) | (15,5)=(5/7)(21,7) |
| target direction in the whole positive interval | proved next, not inferred from q alone |

Let d=(rho,sigma) be the nearer-to-(1,0) of the clockwise-adjacent lower edge directions of Ps and Qs at their unique maximal-x vertex. Both common corners are exposed at d; rho>0>sigma. At least one of Ps(x,0),Qs(x,0) is nonconstant: otherwise both x-derivatives vanish on y=0, contradicting the constant bracket. A nonconstant axis term has positive d-value. The two maxima at d are computed at C_3,C_5 and are in ratio 3/5, hence both are positive. Equivalently 3rho+sigma>0.

This also supplies the full positivity interval demanded by Proposition 7.3. From d up to d0 the value of (21,7) remains positive: it is positive at both boundary rays, and these rays span a cone of angle less than pi. Every such direction therefore has positive value on the fixed support vertex, hence on the polynomial. Thus the lower endpoint d_tilde in Proposition 7.3 is at or below d. No minimality, swapped-standard hypothesis, or unproved positivity beyond this interval is used.

Both polygons actually have an edge at d. The putative leading bracket has weight

    8(21rho+7sigma)-(rho+sigma)=167rho+55sigma>2rho>0.

It must vanish. If one leading form were just the common-corner monomial, GGV Proposition 2.1 would force the other to be a monomial as well (the common weighted value is nonzero), contrary to the definition of d. Hence the opposite-edge corollary applies to both members at this same d.

## 3. Why the first lower slope is 2, and why no rational slope is skipped

Corollary 7.4 gives the first lower leading forms as powers 7m of roots ending at (3,1). These roots are **ordinary** at this first step: their powers are ordinary and minimum x-exponents multiply under powers. Each root has y-degree one, and the edge is nonmonomial, so it has exactly the form

    R_d=a*x^3*y+b*x^(3-k),   a*b!=0.

The exponent difference in y is one. Since both x exponents are integers, homogeneity forces the primitive direction d=(1,-k) with k an integer. This integrality is a consequence of the corollary's linear root, not a presumption about polygon slopes. Positivity says 3-k>0.

GGV's lower-side paper (arXiv:1605.09430v2), Proposition 2.1, applies to an ordinary Jacobian pair with end (a',b'), a'>b'>0, and a direction strictly between (0,-1),(1,0). All hold here with C_3 or C_5. It gives d<(1,-1), so k>1. Its proof and the slope-one Corollary 1.6 were read; no standing minimal-pair assumption from the surrounding section is substituted for its actual statement. Consequently **k=2**.

The two roots have the same nonzero root parameter. This follows either from their commuting leading forms and Proposition 2.1, or directly by differentiating their linear factors. Write it as lambda!=0. With a nonzero scalar eta_m the exact first lower face is

    ell_(1,-2)(Ps or Qs)
       = eta_m*x^(21m)*(y-lambda*x^(-2))^(7m).             (3)

The coefficient one step below its top shows lambda belongs to K: it is a coefficient ratio divided by the nonzero integer 7m. No final seventh-root choice is needed for this opposite-side map.

Apply the one shared Laurent automorphism psi(x)=x, psi(y)=y+lambda*x^(-2). Let P2,Q2 denote the pair. Formula (3) collapses to its common-corner monomial. The map has determinant +1, so the bracket remains -c. It preserves y-degree, total-degree maxima and the unique maximal-x vertex. The d0 face is unchanged, because at d0 the added x^(-2) has weight 4, strictly below weight(y)=7.

It remains essential to show that the next lower direction cannot have an intermediate **rational** slope 2<kappa<3. Take the nearer of the two next lower edges. If its slope were in this interval, positivity would follow from the common end C_m and kappa<3. The same commuting-leading-form argument of Section 2, valid also in the Laurent ring, makes this edge common to both polynomials. The corollary would again supply a y-linear root ending at (3,1), now in K[x^+-1,y]. Its x exponents are still integers, so kappa must be an integer, impossible in (2,3).

For this second use q really remains 7. The unchanged d0 root is R0=y*r(x^7*y^2), r(0)!=0, with y-valuation one. The old Euler solution still solves the unchanged face identity. If a new weight-5 Euler solution differed by Z, then [Z,R0]=0. The homogeneous common-power lemma would give Z^7=constant*R0^5, forcing 7*ord_y Z=5, impossible in K[x^+-1,y]. Thus the Euler solution, and its denominator 7, are unchanged. This argument does not apply Proposition 2.11 outside its positive-rho domain.

After the cut the next lower edge is strictly below the removed one. If its slope kappa>=3, its support inequality and j<=7m give

    i-21m <= kappa*(j-7m) <= 3*(j-7m),

hence i<=3j everywhere. The same holds if the next edge is the zero-valued boundary kappa=3. No corollary is applied at that zero-valued boundary. Therefore

    v_(1,-3)(P2)<=0,    v_(1,-3)(Q2)<=0.                 (4)

The top corner attains zero, so both inequalities are equalities.

## 4. Full support inclusion and all four attained vertices

We now derive the hull, not merely draw an edge. Before psi, ordinaryness and the starting face give

    i>=0, j>=0,    -2i+7j<=7m.

Consequently i-2j>=-2m; equality is attained only at (0,m), because

    i-2j >= (3/7)i-2m.

Under psi each expanded monomial has exponent (i-2t,j-t), 0<=t<=j. This is only a support transformation formula; no power was computationally expanded. The quantity i-2j is unchanged; -2i+7j decreases by 3t; y-exponents stay nonnegative. Together with (4), the entire transformed support satisfies

    j>=0,    i<=3j,    -2i+7j<=7m,    i-2j>=-2m.          (5)

Use the Laurent involution T3(x)=g^(-1), T3(y)=g^3*p. It sends (i,j) to (I,J)=(3j-i,j). Thus (5) becomes

    I>=0, J>=0, 2I+J<=7m, I-J<=2m.                      (6)

The intersection is exactly m*conv{(0,0),(2,0),(3,1),(0,7)}. In particular T3(P2),T3(Q2) are ordinary polynomials. Attainment is separate:

- (0,7m): the original unique common corner (21m,7m), whose coefficient never changed.
- (3m,m): the original d0 endpoint (0,m), preserved because psi strictly lowers d0-weight off its face.
- (2m,0): the coefficient at (0,m) contributes lambda^m*x^(-2m) after psi. No different source monomial can contribute to that exponent, by the equality case i-2j=-2m above. It is therefore nonzero.
- (0,0): choose nonzero output constants after all changes; these do not affect the bracket or any positive supporting face.

The actual polygons are therefore

    N(A)=conv{(0,0),(6,0),(9,3),(0,21)},
    N(B)=conv{(0,0),(10,0),(15,5),(0,35)}.

By (6), I+J<=7m-I<=7m, with equality only at I=0,J=7m. Thus the actual total degrees are 21,35 and their total leaders are single powers of p. The g-degrees are 9,15, attained at (9,3),(15,5). These numbers are not alternative names for any earlier 15/25 source.

For an exact coefficient-face record, choose the original common starting root as u*r(u^2*v^7), with r monic, r(0)!=0, deg r=3; its scalar is absorbed into alpha,beta, the corner coefficients. Its F9 selected root has multiplicity two, so over the splitting field r has a double nonzero root and a distinct simple nonzero root. The receiver's (2,1)-face root is the **polynomial**

    Hbar(g,p)=g^3*p*r(p^2/g).

Its powers 3 and 5, times alpha,beta, are the two (2,1) faces. No assertion that Hbar is homogeneous for total degree is made. The (1,-1) faces are

    alpha*r(0)^3*g^6*(g*p+lambda)^3,
    beta*r(0)^5*g^10*(g*p+lambda)^5.

All displayed scalar factors and lambda are nonzero. These are necessary face identities, not a complete residual system.

## 5. Jacobian, fields, reverse scope and the printed prefactor defect

The affine u-shift has determinant +1, the swap -1, psi +1 and T3 -g. Therefore their composite (1) has determinant **+g**, and [A,B]=c*g. Directly, the substitution (u,v)=(g^3*p+lambda*g^2-r,g^(-1)) has determinant g in variable order (g,p). One may rescale outputs, but doing so changes c; no simultaneous monicity/c=1 assertion is hidden.

The rational inverse on v!=0 is

    g=v^(-1),   p=v^3*(u+r)-lambda*v,

whose determinant in (u,v) is +v. It transforms c*g to the constant c. Nevertheless, arbitrary ordinary receiver polynomials can acquire negative v-exponents under this inverse. Exclusion of the complete necessary receiver family would be usable after this map is reviewed; properness of a receiver ideal alone would not provide an ordinary source. No inverse polynomiality equations are emitted in this task.

The scalar parameters r and lambda descend to the original characteristic-zero coefficient field by the coefficient ratios noted above. Imports can be proved over its algebraic closure, but the final coordinate formulas use those same-field parameters. Optional factorizations of r may use an algebraic extension; they are not needed for the support/Jacobian map. No scheme isomorphism or nilpotent-base assertion is claimed.

**Literal primary defect, not concealed transcription.** In frozen 2204.14178v1, printed p12, Proposition 4.4 displays x^28*(y-lambda*x^-2)^14 and x^42*(y-lambda*x^-2)^21. I inspected the PDF image, not only text extraction. Those prefactors do not match its stated corners (42,14),(63,21). Formula (3), independently derived from Corollary 7.4, gives x^42 and x^63 in the m=2,3 specialization. For our m=3,5 they are x^63 and x^105. The target polygons in the proposition are consistent with (3). This report does not import the inconsistent displayed prefactors, does not silently edit the paper, and does not infer a refutation of its polygon proposition.

## 6. Imports, history and manual falsification perimeter

Actual primary mathematical imports, with their hypotheses read:

1. GGV arXiv:1401.1784v3: Theorem 2.6 (ordinary polynomial Euler element and endpoint properties), Proposition 2.1 (commuting homogeneous common powers), Theorem 7.6(3) including the first type-II corner, Proposition 7.3 and Corollary 7.4 including the full positivity-range definition. Theorem 2.6 and Proposition 2.1 proofs were read; Corollary 7.2's proof and the displayed mirrored Proposition 7.3/Corollary 7.4 proofs were read. Their imported theorem interiors are used at primary-statement trust, not newly formalized here. No minimality is required by these imported statements.
2. GGV arXiv:1605.09430v2: Proposition 2.1, Corollary 1.6 and their complete proofs, with the preceding exactness theorem/proof inspected. The explicit polynomial-pair scope, not the section's separate minimal-pair setup, is used. Proposition 2.2 is not imported.
3. GGHV arXiv:1708.07936v1: Theorem 2.20 and the F9 row, already read and pinned in the source intake, fix the incoming type-II triple and first fractional child. They do not establish this new polynomial receiver theorem.
4. GGHV arXiv:2204.14178v1: whole Proposition 4.4 read as historical method and scope; its literal (2,3) theorem is not promoted to (3,5) by label substitution. The source-size proof above is the new composition.

History was checked before claiming a new map: the terminal D125 published-chain producer and gate were read wholly at their pinned hashes. Their joint-lower-edge positivity and integer linear-root mechanism provide a known pattern, not an F9 attachment. The D108 published-case report was searched at its explicitly named opposite-edge/hypothesis passages; its b=2 split-root machinery is not needed. None of their old arithmetic checkers was imported or executed. Accepted 15q and newly banked 15x/15y are not proof premises here.

Manual changed-object controls:

- Omitting the common constant shift leaves a non-pure maximal-x coefficient after the swap. The proof explicitly derives and applies that shift before asserting a unique maximal-x vertex.
- Treating kappa as automatically integral would be invalid. Integrality is instead forced at every positive candidate edge by the q=7 root's y-degree one in the integer Laurent lattice.
- Replacing the prefactor x^(21m) in (3) by x^(14m) changes its top endpoint to (14m,7m), exactly exposing the printed discrepancy; the desired corner is lost.
- Replacing T3 by T2 sends the actual corner (21m,7m) to (-7m,7m); ordinaryness fails. Thus the exponent 3 is not a cosmetic choice.
- The monomial-J pair (g,g*p) has Jacobian g but its inverse first coordinate is v^-1, not an ordinary polynomial. This small manual example is outside our full polygon guards; it demonstrates why bare monomial-J rows do not supply a reverse source theorem.

No mathematical subprocess of any size, coefficient expansion, CAS, source builder, solver or worker was used. The only new image is documentary conversion of the frozen primary PDF page. No live peer body/log/receipt, protected project or shared ledger was accessed. All owned writers are idle at terminal publication. STOP after this one provisional source-map candidate; no degree-140 exclusion, novelty, all-source coverage, or counterexample claim.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18543`.
- Body SHA-256:
  `37063b4eff4f6946bb52948b305a466a88b32131ee31f8bfc3f264e0977e6cac`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
