# Fixed-degree 75/125 standardization: primary-source interface audit

Author: /root/nonemptiness_certificate. Date: 2026-09-09. Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.

## Verdict and exact scope

**CONFIRMED at imported-primary-theorem/table trust:** an ordinary complex polynomial pair of actual total degrees 75 and 125 with nonzero constant Jacobian has an ordinary standard GGV (3,5) representative with normalized endpoint A0=(5,20). Global minimality is not required. The transformations needed here are polynomial source automorphisms and constant output scaling; no nonlinear output degree reduction is used. Over an arbitrary characteristic-zero field the argument gives the corresponding geometric statement after field extension, sufficient for nonexistence implications; a normalizer rational over the original field is not asserted.

The key extra argument is an exact degree comparison through the inverse rectangle normalizer. The published chain statements are applied to the resulting ordinary standard pair, not to an assumed globally minimal pair. No successor hypothesis is added. The finite table is consumed as the authors' published exhaustive result, not as a computation independently rerun here.

A separate consequence in §6 confirms that an ordinary constant-J pair of coprime reduced degrees mD,nD, m,n>1, whose common homogeneous root H has polynomial centralizer exactly K[H], is already excluded by this classical normalization plus GGV Corollary 7.9. This is an explicit hypothesis class, not arbitrary JC2. Neither conclusion consumes any campaign receiver exclusion, late-contact proof, current blind submission, or pending review. This report itself awaits root adjudication; it does not promote a degree-125 exclusion.

## 1. Primary inputs and quantifier audit

Exact PDF and extracted-text hashes, byte counts and URLs are in the owned `input-pins.json`, `source-pins.json` and `source-record.md`. The mathematical imports are:

| Primary result | Applicable statement and boundary |
| --- | --- |
| [Makar-Limanov, Serdica 51 (2025), 299–314](https://serdica.math.bas.bg/index.php/serdica/article/download/300/153/862), the unnumbered normalization discussion, printed pp.302–305 | Polynomial **source** automorphisms take a given counterexample's first coordinate to a polynomial containing its joint x/y degree corner, with unequal positive corner coordinates. A source swap fixes their orientation. This is not stated only for a globally minimal counterexample. The separate later output reduction is unnecessary here. |
| [GGV, arXiv:1401.1784v3](https://arxiv.org/pdf/1401.1784v3), Definition 4.3 and Proposition 5.20 | An ordinary (m,n)-pair is characterized by constant nonzero bracket, the total/x-degree ratios, and the endpoint inequality. Each such pair can be standardized by an ordinary polynomial automorphism preserving both total degrees and en10(P). The successor condition belongs to an additional preservation assertion, not the initial hypothesis. |
| [GGHV, arXiv:1708.07936v1](https://arxiv.org/pdf/1708.07936v1), Theorem 2.20, §2.4, §5 | Each standard pair gives a complete admissible chain. Section 5 lists all chains with normalized initial-corner total at most 35 and their (m,n) families, including the swapped orientation. No global-minimality assumption occurs in these incoming statements. Later chain children may be Laurent; that does not change the ordinary incoming representative. |
| [Chau, arXiv:math/0408077v1](https://arxiv.org/pdf/math/0408077v1), Division Lemma | An ordinary complex plane automorphism's two total degrees divide one another. Thus actual degrees 75/125, or mD/nD with coprime m,n>1, are nonautomorphic. |

GGV's §4 introduces minimal pairs, but Definition 4.3 does not impose minimality. Proposition 5.20 precedes the separate minimal-pair application in Corollary 5.21. Likewise the first assertion of Corollary 7.9 is for each ordinary standard pair; only its subsequent assertion about the globally minimal gcd B uses Corollary 5.21. These distinctions are essential.

Read scope: the whole ML and Chau papers; the whole identified GGV Definition/Proposition/Corollary proofs and relevant surrounding text; the whole GGHV Theorem 2.20 proof, admissibility subsection and Section 5, plus its valid-edge and family definitions/propositions. This is not an independent recursive proof audit of every historical citation or an implementation audit of Algorithms 8–9. Precise read intervals are recorded separately. No Strinz claimed theorem or its status is used as authority. GGV Proposition 4.7 and its endnote/normalization repair are not invoked.

## 2. Rectangle-pair and inverse-degree lemma

Work over C. Write the original hypothetical pair as P0,Q0. Normalize its Jacobian by a constant output scalar. By the Division Lemma it is a counterexample. ML supplies a polynomial source automorphism ψ for which P=ψ(P0) has support in [0,r]×[0,s] and a nonzero coefficient at (r,s), with r≠s. Neither r nor s can be zero: a univariate polynomial coordinate in a constant-J pair must be linear, and the resulting pair is an automorphism. A source swap allows 0<r<s. Let Q=ψ(Q0).

For every strictly positive rational weight w=(ρ,σ), the leading form of P is αx^r y^s. GGV Proposition 4.1 gives a strictly positive excess degree for the leading Jacobian of a counterexample, so [P_w,Q_w]=0. In the bracket with x^r y^s, distinct Q monomials give distinct output exponents, and the coefficient multiplier for x^i y^j is rj−si. Hence every monomial of Q_w lies on the ray through (r,s). Positive weighted homogeneity makes Q_w a single monomial.

For w=(1,1), call its exponent (t,u). For any other positive w, its ray exponent cannot be farther from zero than (t,u), by maximality of the ordinary total degree. It cannot be nearer either, since the actual monomial at (t,u) is available and would have larger w-degree. Thus (t,u) is the same unique maximum for every positive w. Taking rational weights tending toward the two coordinate directions proves that Q's support lies in [0,t]×[0,u], and (t,u) is a nonzero joint corner. Moreover (t,u) is proportional to (r,s).

Let U=ψ^{-1}(x), V=ψ^{-1}(y), M=deg U and N=deg V. Since U,V are nonconstant polynomial coordinates, M,N≥1. The rectangle corner is uniquely maximal for the strictly positive weight (M,N). Consequently there can be no leading cancellation in substitution:

    deg P0 = Mr+Ns,       deg Q0 = Mt+Nu.                 (1)

More precisely, if U_M,V_N denote their nonzero highest homogeneous forms, then

    (P0)_top = α U_M^r V_N^s.                            (2)

Every other supported monomial has strictly smaller substituted degree; the corner product is nonzero in the polynomial domain. This does not assume that the two leading coordinate forms are algebraically independent. It also does not assume that ψ preserves degrees a priori.

## 3. Actual 75/125 degrees supply the missing finite bound

Equation (1), proportionality, and deg P0:deg Q0=3:5 force

    (r,s)=3(a,b),    (t,u)=5(a,b),    0<a<b,
    a,b∈N,          25=Ma+Nb ≥ a+b.                     (3)

Thus P,Q have total degrees 3(a+b),5(a+b), x-degrees 3a,5a, endpoint en10(P)=3(a,b), and endpoint difference 3(a−b)<0. They meet **all** ordinary (3,5)-pair hypotheses in Definition 4.3. Proposition 5.20 now gives an ordinary standard pair with the same two total degrees and the same endpoint. In its proof the normalizer is the identity or y↦y+λ, and its total leaders are also retained.

Theorem 2.20 attaches a complete chain with A0=(a,b). The admissibility conditions in §2.4 apply to that source chain. By (3), Section 5's exhaustive bound 35 applies, with the sharper cutoff a+b≤25.

Here is the complete small manual filter of the published family table at that cutoff; j is its nonnegative family parameter, not a source contact order:

| Families | A0 | Listed (m,n) |
| --- | --- | --- |
| F1 | (4,12) | (2j+3,3j+4) |
| F2 | (5,20) | (j+2,2j+3) |
| F3 | (5,20) | (4j+3,3j+2) |
| F4 | (5,20) | (2j+3,12j+16), with its additional parameter restriction |
| F5 | (5,20) | (7j+9,4j+5) |
| F6 | (5,20) | (3j+4,8j+10) |
| F7, F18 | (6,15), (6,18) | (j+2,4j+7) |
| F8, F19 | (6,15), (6,18) | (2j+3,5j+7) |

Every omitted table row has a+b≥28. Checking both the displayed and swapped orientations, only F2 at j=1 gives {m,n}={3,5}. F1 gives (3,4) or (5,7) at its first two values; F3 gives (3,2) then (7,5); every remaining row already has an entry too large when the other could be 3 or 5. No extra exclusion of F18/F19 is needed for this filter.

Therefore the incoming standard source has

    A0=(5,20),  A0'=(1,0),  A1=(7/5,2),  k=1,
    (m,n)=(3,5).                                       (4)

There is also a useful consistency strengthening: (3) becomes 25=5M+20N, so M=N=1. The selected rectangle normalizer was necessarily affine. Accordingly the standardized pair still has actual total degrees 75 and 125, not merely a ratio or an upper bound. This conclusion was deduced from the table and unique-corner comparison; it was not assumed in invoking ML.

## 4. What the interface does and does not supply

The chain just established is

    actual ordinary 75/125 Keller pair
      → ordinary proportional rectangle pair, normalized gcd ≤25
      → ordinary standard (3,5)-pair with the same corner
      → published admissible F2 chain (4).

Every arrow is necessary/existential. None uses globally minimal gcd B, the strengthened successor clause of Proposition 5.20, a chosen public normalized coefficient chart, or the campaign's reverse-lift/receiver exclusions. This report does not implement a coefficientwise map from an arbitrary input pair to a public chart, does not show that every public truncated point lifts, and does not produce an exact ideal certificate. Those are distinct claims.

The finite enumeration remains a precise external trust boundary. If one declines the Section 5 exhaustiveness import, the proved intermediate result is a standard (3,5)-pair with A0=(a,b), 25=Ma+Nb and a+b≤25; F2 selection then remains the named missing arrow. There is no additional missing hypothesis at the printed statement interface.

## 5. Characteristic-zero fields

For an arbitrary characteristic-zero field K, place the finitely many original coefficients in a finitely generated subfield k0/Q and embed k0 in C. Nonzero coefficients, the degrees and the constant-J identity survive the embedding. The preceding argument applies to the embedded pair. This already suffices for any implication whose endpoint is nonexistence of complex F2 standard pairs.

One can also express the geometric existence conclusion over an algebraic extension: the finitely many coefficients of the selected source automorphism and its inverse satisfy finite polynomial identities over k0, with finitely many nonvanishing conditions for their actual degrees and the standard source conditions. Their complex solution gives a solution over an algebraic closure of k0. Composing that extension with an algebraic closure of K gives an ordinary geometric representative of the original pair. No assertion that the selected automorphism descends to K itself is made. No analytic specialization of an infinite family of coefficients is needed.

## 6. Separate closed-common-root consequence

Assume now P0,Q0 are ordinary with nonzero constant Jacobian, degrees mD,nD, coprime m,n>1, and homogeneous leading forms H^m,H^n (nonzero scalar factors are harmless). Suppose

    ker([H,−]:K[x,y]→K[x,y]) = K[H].                    (5)

Again this is a counterexample by the Division Lemma. Repeating §2 gives rectangle corners m(a,b),n(a,b), with 0<a<b and D=Ma+Nb. Proposition 5.20 produces an ordinary standard (m,n)-pair with the same normalized endpoint (a,b). GGV Corollary 7.9, printed p.45, applies to this **individual** standard pair and gives d=gcd(a,b)>2. Its separate globally-minimal-B conclusion is not used.

The leading-corner identity (2), compared with H^m, gives over an algebraically closed field

    H = λ U_M^a V_N^b
      = λ (U_M^(a/d) V_N^(b/d))^d.                    (6)

The passage from equal m-th powers to proportional polynomials is valid in the polynomial domain over an algebraically closed field. Also d divides D=Ma+Nb. The displayed root W=U_M^(a/d)V_N^(b/d) is a nonconstant homogeneous polynomial of degree D/d, and [H,W]=0. It cannot belong to Kbar[H] by its smaller positive degree. This contradicts the scalar extension of (5).

For completeness, that scalar extension needs no hidden algebraic-closedness assumption. Write any polynomial over an extension field using a finite linearly independent set of extension-field scalars over K. The bracket equation separates coefficientwise, so each K-polynomial component centralizes H. Equation (5) therefore implies the extension-field centralizer is the polynomial algebra in H. To reduce first to the finitely generated coefficient field, the intersection K[H]∩k0[x,y]=k0[H] follows by successively comparing the highest-degree coefficient of a polynomial in H. These two elementary facts justify the complex reduction used above even when (5) was initially supplied over K.

Thus the **whole explicit closed-H, reduced m/n>1, ordinary constant-J class is empty at the cited classical-theorem trust tier**, independently of a late-contact bound. This does not assert every hypothetical Keller pair belongs to that class: a proper-power common root has a larger polynomial centralizer. In particular H=(xy^4)^5 in the F2 rectangle is not closed. Nor does the consequence apply to polynomial receivers with bracket c g², to Laurent pairs, or to a changed top root merely inferred from matching degree labels. No normalizer-affineness argument or leading-Jacobian argument for U,V is needed for (6). This is source admissibility, not a novelty claim.

## 7. Manual hostile controls and remaining trust

These controls were checked symbolically in prose; **no mathematical subprocess, numerical sampling or code replay was run**.

* Dropping the joint-corner hypothesis breaks (1): f=x−y² and the polynomial automorphism U=x+y²,V=y give f(U,V)=x, despite maximum (2,1)-weight 2 in f. The two leading terms cancel. Its support has no joint corner (1,2), exactly the premise used to prevent this cancellation.
* Allowing nonlinear target degree reduction breaks the preserved-ratio inference: the automorphism pair (x,y+x²) changes degrees 1/2 to 1/1 under Q↦Q−P². Our argument does not use this operation from ML's later discussion.
* Dropping closedness invalidates §6's contradiction: H=(xy)^d, d>1, has the lower-degree commuting polynomial xy. Formula (6) is then consistent, not impossible. The F2 top above exhibits this same distinction within the normalized interface.
* Replacing an ordinary polynomial inverse by a Laurent substitution removes M,N≥1 and the rectangle degree comparison; the proof must not be transferred to a monomial-J receiver through its rational inverse chart.

The primary normalization/reduction proofs and published finite enumeration remain imported mathematics. Their exact applicability is confirmed here; a new independent recursive proof of the entire literature is not claimed. There is no computed unit certificate, no full-source row construction, no public-chart properness result and no general JC2 conclusion. No new campaign OPEN identifier is introduced. Owned collision extraction is empty and does not scan any current blind/protected corpus.

All mathematical work was prose. Only primary-byte retrieval/text conversion, bounded metadata hashing and the existing publication transaction were executed. All owned writers are idle at terminal custody.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15932`.
- Body SHA-256:
  `ad0511e505332af3940223f2fa8d2c642ab28d68639cf7d9d2073bcd257a27c6`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
