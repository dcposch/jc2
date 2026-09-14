# D125 higher moments: valid exactness functional, failed general obstruction

2026-09-07. **NO-GAIN at the proposed theorem interface.** The seed functional and moments are correct. Every complete Keller source makes all mixed moments vanish, already as identities in its guarded coefficient quotient. But all-moment vanishing does not force algebraic dependence, even with ordinaryness, receiver degrees15/25 and monic fiber degrees15/25. Moreover its proper kernel contains1 and is therefore not a Mathieu subspace. No full-client expansion, power-moment matrix or solver was run. This derivation uses only the accepted literal lift contract, not the unreviewed abstract torsor classification.

## 1. Exact functional and primitive criterion

Let T be any commutative Q-algebra, including either campaign coefficient field and any parameter quotient. Treat its coefficients as constants for relative differentials. Glue the two literal polynomial charts by

    u=g^4*w+q(g),  v=g^-1,  q=lambda2*g²+lambda3*g³.

Let C_T be the subring of T[u,v] whose substituted expressions are in T[g,w]. For R in C_T define

    H(u,v)=integral_0^u R(s,v) ds,
    L(R)=[g^1] H(q(g),g^-1).

This is finite polynomial integration/coefficient extraction, with rational scalar denominators only. For a,b>=0, writing n=a+1 and k=b-2a-1 gives

    L(u^a*v^b)=binomial(n,k)*lambda2^(n-k)*lambda3^k/n

when 0<=k<=n, and zero otherwise. The formula extends T-linearly to all polynomials; globality matters for the exactness inference, not its definition.

Put omega=du wedge dv, which transforms to g² dg wedge dw. The following exact criterion needs no surface-classification theorem:

> For R in C_T, R*omega has a global relative polynomial one-form primitive on the two charts if and only if L(R)=0.

Proof: alpha=H*dv is a primitive on U. Write H_V=H(g^4*w+q,g^-1) and H_0=H(q,g^-1). Since partial_w H_V=g^4*R_V and R_V is polynomial, integration in w gives H_V-H_0 in g^4*T[g,w]. On V,

    alpha=-g^-2*H_0*dg + a polynomial multiple of dg.

Its only possible logarithmic residue is -[g^1]H_0=-L(R); every polar term is independent of w. If this residue is zero, integrate the terms of g-degree<=-2 to a Laurent polynomial K(g) of strictly negative degrees. K is polynomial in v on U. Then alpha-dK is regular on both charts and has differential R*omega.

Conversely, if beta is a global primitive, alpha-beta is a closed polynomial one-form on U. Elementary integration in u and then v makes it dF for F in T[u,v]. Restricting the transformed identity to w=0, beta is regular at g=0 and dF(q,g^-1) has zero Laurent residue. Hence -L(R)=0. Polynomial integration and the Laurent coefficient argument remain valid over arbitrary Q-algebra quotients, including nilpotents. This asserts exactness of these global forms, not an unproved classification of the entire de Rham cohomology.

## 2. Seeds and scheme-theoretic necessity

The literal global functions

    z=u*v³-lambda2*v = g*w+lambda3,
    w=u*v^4-lambda2*v²-lambda3*v

give the exact identities

    L(1)=0,    L(z)=-lambda2²/2,
    L(w)=-lambda2*lambda3,    L(w²)=lambda3³/3.

The last identity holds even when lambda2 is not zero, slightly strengthening the proposed seed. Thus L is nonzero over every characteristic-zero field with (lambda2,lambda3)!=(0,0). No such field-point nonvanishing is silently extended to arbitrary nonreduced parameter quotients.

If P,Q are global and J(P,Q)=c, then for every i,j>=0

    d(P^(i+1)*Q^j*dQ/(i+1))=c*P^i*Q^j*omega.

The primitive is global, so c*L(P^i Q^j)=0. With c a unit, all mixed moments vanish. Apply this over the universal coefficient ring modulo ALL Jacobian rows, ALL negative-power rows and the inverse-scalar row: every moment polynomial lies in that full ideal itself, not merely its radical. Polynomial coordinate rings inject into these coordinate Laurent localizations even over nonreduced T, so no extra parameter saturation is hidden. This is a coefficient-quotient proof of consequence, not an emitted small ideal-membership certificate. Without the guard only c*L=0 follows. No moment is an additional independent equation beyond this complete system; possible usefulness against a specified weaker subsystem would need its own measurement.

## 3. Exact all-moment countermodels

Over any characteristic-zero field, the simplest countermodel is P=u, Q=u*v. Both are global, and P^i Q^j=u^(i+j)*v^j. Since ord_g(q)>=2,

    ord_g(q^(i+j+1))>=2(i+j+1)>j+1,

so every mixed moment vanishes. The monomial exponent map (i,j)->(i+j,j) is injective, proving algebraic independence. The Jacobian is u, not a nonzero constant.

There is also a stronger **factored, unexpanded** control:

    P=w^15,             Q=w^25+u*w^6.

To prove its entire infinite moment family vanishes, first observe that

    L(u^r*w^n)=0 whenever n>3r+2.

Indeed a term using a factors u*v^4, b factors -lambda2*v² and d factors -lambda3*v has a+b+d=n. A nonzero moment would require

    4a+2b+d+1 <= 3(r+a+1),
    hence n+b<=3r+2,

because deg_g q<=3. This contradicts the asserted bound. In P^i Q^j, each binomial term has u-exponent r<=j and w-exponent n=15i+25j-19r. For i+j>0,

    n-3r>=15i+3j>=3.

The constant case is L(1)=0. This proves all mixed moments without expanding any high power or inferring infinity from a finite check.

These P,Q are ordinary in both charts. Their receiver representatives are w^15 and w^25+(g^4*w+q)*w^6, with w=p+g; total degrees are15/25 and the p^15/p^25 coefficients are1. Their restrictions at g=0 are w^15,w^25. Physical degrees are exactly75/125, with the contract's monic total leaders. But

    J(P,Q)=-15*w^20*(4u*v³-2lambda2*v-lambda3)

is nonzero and nonconstant, proving algebraic independence but not Keller. Crucially, this is **not** a point of a charged full-face client: its outer A=(p+g)^15 has g^15 coefficient1, while either prescribed H³ is divisible by p^6 and has that coefficient0. Thus the control refutes a general or degree/monicity-only moment theorem, not inconsistency of the actual fixed-face moment subsystem.

## 4. Published theorem interface and history

For a nonzero lambda class over a field, M=ker(L|C_T) is proper but contains1. If M were Mathieu, taking a=1 in its defining condition would force b*1^m=b into M for every b, contradicting L(z)!=0 or L(w²)!=0. Hence the **literal Mathieu claim is false**, not merely awaiting an image-conjecture theorem. The map R->g^-1*H(q,g^-1) expresses L as a Laurent constant term but is linear, not multiplicative: it does not transport powers to powers. [Zhao, Definition1.1 p.2 and Theorem1.3 p.3](https://arxiv.org/pdf/0902.0212v3). His Image Conjecture1.4 remains a conjectural statement there; no such claim is imported as a theorem.

Pakovich–Muzychuk's theorem classifies vanishing of entire integrals of powers of one polynomial on a fixed segment with distinct endpoints, using sums of composition solutions. Here only one Laurent coefficient of a moving-endpoint primitive vanishes. There is no proved transport preserving multiplication and those hypotheses, and the explicit countermodels prohibit the desired broad conclusion. [Theorem1.1, pp.1–3](https://arxiv.org/pdf/0710.4085v2).

The named AUDIT de Rham, trace-moment and parent-residue entries already distinguish class equations from polynomial realization and residues from independent full-Jacobian constraints. `avenues/MATHIEU.md` already records the elementary containing1 argument; its successful, priority-corrected Liouville/Zoladek polynomial ODE theorem has no demonstrated bridge from today's functional. No novelty for that general reasoning is claimed. Exact searched filenames, reading limits, observed ledger hashes and primary URLs are in the owned `reading-scope.md`; terminal/source PDF pins are in `v2-inputs.json`.

**First remaining arrow:** prove a genuinely more restrictive statement using the actual fixed faces and all moments, or exhibit a cheaply useful moment consequence of a named partial ideal. Neither is supplied. Ordinaryness plus all moments, even at the right degrees and monicity, is insufficient; adding the full Keller equation recovers consequences already present. This is not a new equivalent formulation proven to resolve JC2.

## 5. Controls and stop

Owned standard-library `check.py` compares direct finite integration with the binomial formula, checks seed/globality/Jacobian signs, verifies the residue and explicit primitive corrections, and tests the strong countermodel's scalar degree inequalities without expanding its powers. `v2-replay.json` records normal/-O passes and actual coefficient-index/denominator mutations failing in both modes, each under30wall/25CPU/512MiB. Earlier preliminary replay files are retained but superseded by v2 after strengthening the controls. No numerical sampling, finite-to-infinite inference, full client expansion, AWS/CAS/solver, new agent, live peer access, protected/shared edit or baseline change. Transactional publication and terminal custody follow; all writers are idle. **STOP: valid necessary identities, no licensed faster obstruction.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9145`.
- Body SHA-256:
  `a9acae719f83ec6143ed96c536e3da5619390a63eaa7956ef0447e47d1ec0285`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
