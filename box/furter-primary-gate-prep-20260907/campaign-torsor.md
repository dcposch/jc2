# D125 torsor geometry: exact Wright interface, no imported obstruction

2026-09-07. **NO-HIT / classical marked-surface reformulation**, with one useful quasi-finite interface. The actual surface is an O(-4)-torsor and, for nonzero class over C, a Danilov–Gizatullin surface of index4. Its canonical divisor and the receiver Jacobian agree, rather than contradicting one another. The applicable general nonexistence statement is Wright's conjecture; his proved coefficient case is excluded by our literal transition. No full-source point, properness result, support-preserving normalization, or JC2 conclusion is obtained.

## Exact geometry and marked Jacobian

Work over a characteristic-zero field K, and use C for the imported complex-surface classification. Glue U=Spec K[u,v] and V=Spec K[g,w] by

    v=g^-1,       u=g^4*w+lambda2*g²+lambda3*g³,       w=p+g.

The linear transition is O(-4), not O(4): for tautological frames e_V=g*e_U, the fourth tensor power has e_V=g^4*e_U and fiber coefficients u=g^4*w. In this trivialization the Cech class lies in

    K[g,g^-1] / (K[g^-1]+g^4*K[g]),

with basis g,g²,g³ and coordinates (0,lambda2,lambda3). Indeed changes u->u+a(v), w->w+b(g) alter the translation by a(g^-1)-g^4*b(g). Thus the class is nonzero exactly when the two lambdas are not both zero. All these statements are exact over K; the complex classification does not give a same-field, marked-chart isomorphism.

A nontrivial O(-d)-torsor is the complement of an ample section of self-intersection d in a Hirzebruch surface. For d=4 this is the affine DG surface of **index4**; Dubouloz's model name S(d-2)=S(2) does not change the index. The abstract complex isomorphism type forgets the chosen fiber F, the étale chart, and every receiver support/pin. It therefore supplies no coefficient normalization of this client. [Dubouloz, Section3.1, Proposition3.1, p.6](https://arxiv.org/pdf/1108.6209v1).

Here F=V(g)=S\U. Both charts are factorial and the overlap has units K* g^Z, so the units/Picard gluing sequence gives Pic(S)=Z, with generator [F]=pi*O(1). Direct differentiation gives

    du wedge dv = g² dg wedge dw.

Consequently K_S=pi*O(2)=O_S(2F). The global two-form omega defined by du wedge dv on U and g² dg wedge dw on V has divisor **2F**, not the reduced divisor F. Equivalently the relative cotangent of an O(-4)-torsor is pi*O(4), and tensoring with pi*Omega(P1)=pi*O(-2) gives the same sign and exponent.

At any point satisfying the complete receiver Jacobian and ALL lift-polynomiality rows, the regular functions P,Q on U and A(g,w-g),B(g,w-g) on V glue to f:S->A². The p->w-g shear has determinant1. Therefore f*(dA wedge dB)=c*omega, its ramification divisor is exactly2F, and f is étale on U. It is not étale on S. Nontrivial Picard or canonical class alone is consistent with these equations.

## Exact published obstruction boundary

In Wright's marked coordinates choose (x,y)=(v,u), (x',y')=(g,w). His transition becomes

    x'=x^-1,   y'=x^m*y+alpha1*x^(m-1)+...+alpha_(m-1)*x,
    m=4,       (alpha1,alpha2,alpha3)=(0,-lambda2,-lambda3).

The Jacobian in this ordered étale chart is -c. Wright's Conjecture3.2 asks precisely for nonexistence of a morphism from such an affine A1-bundle to A² that is étale after deleting one fiber. His Theorem3.3, p.600, proves the case alpha1!=0; ours has alpha1=0 identically. Interchanging base charts can change this coefficient but moves the marked étale chart to V, on which the actual determinant vanishes at g=0. Thus that maneuver does not satisfy the theorem's hypotheses. [Wright, original paper, pp.599–601](https://doi.org/10.1215/ijm/1256068982); [author-uploaded primary text](https://www.researchgate.net/publication/258233253_Affine_surfaces_fibered_by_affine_lines_over_the_projective_line). The pinned secondary restatement is itself a research primary: [Rodriguez v2, Theorems3.7 and3.9, pp.5–6](https://arxiv.org/pdf/2403.02219v2).

The failure is visible without classification. Our form has the global regular primitive

    theta=v*du=g³*dw+(4g²*w+2lambda2+3lambda3*g)*dg,
    dtheta=-omega.

Adding the missing Cech term lambda1*g would introduce lambda1*dg/g in theta. That residue is absent here, so the corresponding differential obstruction supplies no contradiction. This is an explanation of the coefficient condition, not a stronger theorem.

For completeness, the literal Wright ring generators are

    u, v*u, v²*u, v³*u-lambda2*v, v⁴*u-lambda2*v²-lambda3*v.

On V they are respectively u, g³*w+lambda2*g+lambda3*g², g²*w+lambda2+lambda3*g, g*w+lambda3, w. Their regularity is checked directly. Their generation of Gamma(S) is the imported Theorem3.1, not a newly emitted ideal or a claim that arbitrary elements satisfy our fixed faces.

The latest checked Rodriguez version is v2, 11 April2024: the author explicitly corrected a false earlier Lemma2.3 by conditioning subsequent results. Its stronger normalization conclusions require a primary-submodule hypothesis not established here. We neither identify S with the finite integral normalization nor import the proposed index3 conclusion; its multiplicity use would also require a separate audit against our exact divisor2F. [Version record](https://arxiv.org/abs/2403.02219). No retracted/unconditional v1 conclusion is used.

## Useful finite-fiber arrow and exact remaining gap

For the charged full faces, A(0,w) and B(0,w) have monic degrees15 and25. Hence f|F is nonconstant and has finite geometric fibers: w is integral over K[A(0,w)], by its monic polynomial. The étale restriction on U also has finite geometric fibers. Since S=U union F, f is quasi-finite, separated and dominant; its function-field extension is finite.

Let N be the normalization of A²_target in K(S). This normalization is finite because the target polynomial ring is excellent. Normality of S makes every integral element regular on S, giving S->N; Zariski's Main Theorem identifies this birational quasi-finite map as an open immersion. Thus

    S --open--> N --finite--> A².

The first arrow is **not proved surjective**. Missing boundary curves are not ruled out by affineness or Pic(S)=Z. In particular quasi-finite does not mean finite or proper. [Stacks Project, Lemma37.43.2](https://stacks.math.columbia.edu/tag/02LR), [Lemma37.43.3](https://stacks.math.columbia.edu/tag/05K0). This exact missing-boundary interface is useful, but no theorem reviewed here removes the boundary or excludes this marked morphism under the supplied hypotheses.

| Proposed arrow | Scoped verdict |
| --- | --- |
| Nonzero literal class -> affine DG index4 over C | Imported theorem applies; no marked support transport |
| Complete source rows -> morphism with ramification2F | Exact chart identity |
| Monic fiber faces -> quasi-finite -> open/finite factorization | Proved above |
| Abstract surface isomorphism -> favorable Wright coefficient in the same étale chart | Not supplied |
| Wright Theorem3.3 -> exclusion of this source | Fails alpha1!=0 hypothesis |
| Open S subset N -> S=N / a usable global finiteness obstruction | Missing; no properness assumed |

## Evidence, history and stop

`box/d125-torsor-geometry-discriminator-20260907/inputs.json` pins the terminal source contracts, the related campaign log-Kodaira report, and retrieved primary snapshots. `primary-interface.md` records exact reading scopes and the limited named-ledger history search. The earlier campaign obstruction concerns a dominant map A²->a surface minus a section, opposite to our map and with a different deleted divisor. No repo-wide novelty claim: this is an explicit specialization of Wright's classical setup.

Wright's publisher downloads were blocked HTML and are retained under that name; the relevant original statements/differential argument were read through the author-uploaded primary mirror, with subscripts cross-checked against pinned v2. No complete original Wright PDF or whole-proof replay is claimed. Selected Dubouloz sections and proofs, and both Stacks statements/proofs, were read completely; remaining papers were not audited wholesale.

Owned standard-library controls verify the actual transition Jacobian, Cech coboundaries, five global generators, and the primitive/residue identities. Normal and -O pass; actual transition-power and differential-sign mutations fail in both modes. Six-run receipt is byte-pinned, with per-process30wall/25CPU/512MiB caps. No full receiver expansion, CAS, AWS, solver, extra lane, live peer read, protected/shared edit, baseline change, or theorem-driven computation follows. **STOP: retain this exact interface; no geometry-based faster proof path was licensed by the bounded search. All writers are idle at custody publication.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8785`.
- Body SHA-256:
  `2f6b5053d8c1f6c16e776ea45c43778b8a7f7d8ab955a94b01ddf5f54ab5fa2d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
