# F9 at j=1: an exact source interface, not yet a smaller polynomial client

Author: Astra, /root/nonemptiness_certificate. 2026-09-09. Basis: 0d39df3c9fd69c939a8420c54d03228b9077777d.

## Verdict and boundary

**KNOWN necessary family / NEW bounded intake; no exclusion found at the checked scope.** The printed F9 specialization with (m,n)=(3,5) and maximum degree 140 is distinct from the classically discarded F9 specialization (2,3), maximum degree 84. It is reasonable to retain the former as a named source-admissibility target. This is not a claim that it is attainable, mathematically open, or the next best computation. No complete original-source ideal or small ordinary receiver has been emitted or licensed here.

The exact first forward object is a **Laurent** pair. The missing arrow for a smaller ordinary-polynomial client is cancellation of every negative exponent after a further proved transformation, with all source conditions transported. A table row and a matching degree do not supply that arrow. In particular, I do not attach every arbitrary actual 84/140 pair to F9, and do not use the pending general-normalizer or arbitrary 75/125 theorem.

## 1. What the printed family says

[GGHV 1708.07936v1](https://arxiv.org/pdf/1708.07936v1), Section 5, printed page 25, gives

| datum | literal F9 value | meaning here |
|---|---|---|
| A0 | (7,21) | (1/m) en_(1,0)(P), not by definition the total-degree vertex |
| A0' | (1,0) | first edge's other normalized endpoint |
| A1 | (11/7,2) | selected root-cut successor |
| k | 1 | published terminal family parameter, not a Jacobian normalization |
| (m,n) | (j+2,2j+3) | j is the table parameter |
| j=1 | (3,5) | distinct from j=0=(2,3) |

The first direction is (7,-2): its value at A0 and A0' is 7. Section 6, printed page 27, explicitly lists F9 (3,5), maximum degree 140; it also lists F9 (2,3), maximum 84, and the different F11 (2,5), maximum 140. Swapping outputs gives the opposite degree orientation and changes the sign of the Jacobian. F11 is not F9 merely because 140 occurs twice.

Theorem 2.20 starts with **each standard (m,n)-pair**, not only a globally gcd-minimal pair. Nevertheless, its conclusion is a necessary chain for that pair; it neither realizes every admissible table row nor normalizes every arbitrary degree pair into this specific row.

There is an important ring convention: [GGV 1401.1784v3](https://arxiv.org/pdf/1401.1784v3), Definition 4.3, uses L^(l)=K[x^(1/l),x^(-1/l),y]. Even l=1 allows x inverse. Thus **ordinary polynomial status P,Q in L=K[x,y] is an explicit extra source condition**, not a consequence of the word standard alone. The definition imposes the total-degree ratio and x-degree ratio m/n, with the relevant endpoint inequalities; it does not define a rectangle.

## 2. The honest incoming polynomial source

Work in characteristic zero, extending to an algebraic closure when a selected edge root is needed. The source under consideration is explicitly:

- P,Q in K[x,y], [P,Q]_(x,y)=c in K*, an ordinary standard (3,5)-pair;
- its first published triple is A0=(7,21), A0'=(1,0), with selected successor A1=(11/7,2), direction (7,-2), and F9 terminal parameter k=1;
- for the actual-degree specialization, **deg P=84 and deg Q=140**;
- if the monomial-top formulation is used, impose the corresponding rectangle/top normalization explicitly: P_84=alpha x^21 y^63 and Q_140=beta x^35 y^105, alpha,beta nonzero. This can instead be supplied by a separately proved source normalization, but none is silently imported here.

The endpoint itself gives deg_x P=21, deg_x Q=35, and coefficients at (21,63),(35,105) nonzero. It yields only deg P>=84 and deg Q>=140 before the total-degree condition. The bare standard definition plus A0 does not justify equality or a unique total leader. Section 6's degree-140 specialization, or an explicit rectangle assumption, supplies the missing numerical restriction. This report therefore does not infer an arbitrary-84/140-to-this-frame theorem.

Under the stated monomial-top condition, the degree-28 common form is H=x^7 y^21=(xy^3)^7. Consequently P_84=alpha H^3 and Q_140=beta H^5, while the primitive form H0=xy^3 has degree 4 and the exponents are **21 and 35**, not 3 and 5. This form is not closed in the campaign's centralizer sense: H0 commutes with H but H0 is not in K[H]. The reduced top profile (1,3) is not the balanced (1,1) profile excluded immediately by GGV Theorem 2.6(4). Corollary 7.9's endpoint test gcd(7,21)>2 is satisfied. These observations license no new exclusion and do not promote the pending closed-H discussion.

This is a conditional necessary source for the specified normalized F9 class. Properness of a genuinely complete ideal of these ordinary polynomials, all Jacobian rows and nonzero guards would be sufficient for a counterexample; no such ideal or properness witness is provided. The source is not asserted necessary for every actual 84/140 counterexample.

## 3. First literal forward cut, including its sign and Jacobian

Use the published Theorem 2.20(8), at l0=1 and (rho,sigma)=(7,-2). Put z=x^(2/7)y. Since the first endpoints of P are (3,0) and (21,63), its edge is

    ell_(7,-2)(P) = x^3 pi(z),  pi(0) != 0,  deg pi = 63.

Ordinaryness forces pi to have only z-exponents divisible by 7. Likewise the Q edge is x^5 chi(z), with chi(0)!=0 and degree 105. The theorem chooses a nonzero root lambda of pi. Its displayed successor formula gives

    (11/7,2) = (1,0) + (m_lambda/3)(2/7,1),

so m_lambda=6. GGV Proposition 2.1 applied to the commuting weighted leaders of weights 21 and 35 gives a common polynomial edge root with powers 3 and 5. Hence the Q-edge multiplicity at lambda is 10. Their bracket vanishes because its possible weighted degree is 21+35-(7-2)>0 whereas the full Jacobian is constant. The field may be enlarged algebraically to contain lambda; this is an existential forward extension, not descent of a chosen root to the original field.

The literal automorphism is

    phi(x)=x,    phi(y)=y+lambda*x^(-2/7),    l1=7.

It preserves the Jacobian with respect to x,y in L^(7), since its triangular determinant is +1. Equivalently set t=x^(1/7) and Y=y-lambda*x^(-2/7). Then

    P1(t,Y)=P(t^7,Y+lambda*t^(-2)),
    Q1(t,Y)=Q(t^7,Y+lambda*t^(-2)),
    P1,Q1 in Kbar[t,t^(-1),Y],     [P1,Q1]_(t,Y)=7c*t^6.

The determinant is +7t^6, not a constant and not its reciprocal. The inverse is x=t^7, y=Y+lambda*t^(-2) on the ramified punctured chart; the map to the old x-plane is a degree-seven extension, not a polynomial automorphism of A2.

In the original fractional-x exponent convention the selected edge starts at (33/7,6) for P1 and (55/7,10) for Q1 and ends at (21,63),(35,105). In t,Y coordinates these become (33,6),(55,10) and (147,63),(245,105). Its (1,-2)-edge expressions are t^21 pi(t^2Y+lambda) and t^35 chi(t^2Y+lambda). This particular edge is polynomial in t,Y. **The entire pair need not be**: lower source terms can acquire negative t powers. Ordinary total degrees cannot be assigned to this Laurent child by relabeling its endpoint coordinates. No further chain cut or monomial receiver has been asserted.

## 4. Classical and historical scope checks

[GGHV 2204.14178v1](https://arxiv.org/pdf/2204.14178v1), Theorem 2.1, addresses maximum degree below 125. It therefore does not address an actual maximum of 140. Its Section 3 begins the F9 argument by specifying the **smallest** F9 case. It displays the family expression IM=2(j+2), then explicitly specializes j=0, obtaining IM=4, and derives Im=5. The contradiction is 4<5. At j=1 the displayed IM expression is 6; the j=0 contradiction cannot be reused. I have not extended the cited approximate-root analysis to j=1, nor asserted that all its minor-root formulas remain unchanged there.

The same paper's Proposition 4.4 is headed “Case (7,21)”, but its proof explicitly fixes (m,n)=(2,3). Its target polygons and Section 6 elimination are correspondingly the 2/3 system. That heading is **not** an all-j F9 exclusion or a licensed 3/5 polygon map. Copying the proof for j=1 would require checking the opposite-edge hypotheses and all polynomiality cancellations anew.

Two other false matches are excluded by the printed 2017 source itself. Section 6 Proposition 6.1 discards F22 (2,3), not F9. The Moh case removed by the algorithm has A0=(7,21) but A0'=(2,1), which is not in PLLC; our A0' is (1,0). Removing that different starting edge does not remove F9.

The narrow canonical search found no exact F9/84-140 retirement. The returned F9 strings in AUDIT were other chamber/coefficient labels. This is a bounded lookup, not an exhaustive ideal/literature nonexistence statement. Targeted current primary metadata reads found no additional arXiv revision beyond v1 for the 2017 and 2022 papers; narrow exact searches found no applicable new exclusion. Stronger uncaught results or external corrections remain a coverage possibility. No broad web clock is reset. Exact source pins and read scopes are in the owned box.

## 5. Cheapest next discriminator and manual safeguards

**Recommendation: retain F9-j1 as a typed, not-yet-retired-by-this-check source lead, but do not launch an ideal builder.** The highest-information next source question is whether the opposite-edge/polynomial-cancellation steps of the 2022 (2,3) map extend to the actual (3,5) F9 source. A successful proof would need a complete ordinary target polygon, its precise monomial Jacobian and nonzero guards. A failure at one named lower-edge hypothesis is a useful stop. Starting directly from the already licensed Laurent child is also possible, but any properness-to-Keller claim would still require an exact reverse ordinaryness contract; no equivalence is implicit.

Manual changed-hypothesis checks, not automated tests:

1. Replacing j=0 by j=1 changes the displayed intersection upper number from 4 to 6; the printed 4<5 contradiction disappears. This is not a surviving polynomial point.
2. Replacing A0'=(1,0) by (2,1) changes the starting-edge data and invokes a different printed exclusion. Equal A0 is not enough.
3. Replacing x^(-2/7) in phi by x^(+2/7) fails to preserve the (7,-2) homogeneous weight of y. The licensed negative exponent has weight -2. The t-Jacobian factor remains +7t^6 only for the stated variable order and actual chain rule.
4. Dropping ordinaryness or all negative-power cancellation rows can turn a Laurent receiver point into a false Keller claim. A nonzero selected lambda and all original endpoint/Jacobian guards are retained.
5. Replacing H by H0 without changing 3/5 to 21/35 is a false theorem attachment. H0 itself witnesses the failure of K[H] as the polynomial centralizer.

Scope stop: no point, proper ideal, whole-family exclusion, universal 84/140 standardization, performance result or JC2 conclusion. No mathematical subprocess of any size was run. No live peer proof/cross report was read. No shared ledger was changed. All report/source writers are idle at terminal publication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11044`.
- Body SHA-256:
  `79b85717efed0cd168f7a46bf4d071e1c7946e5f7da4f463a0feea663bdd22f8`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
