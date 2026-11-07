# EULER1730 — candidate exclusion of expanding Keller maps for the actual index-three filtration
ROOT proposal for hostile review. INTERNAL / MANUAL / UNREVIEWED / UNPROMOTED. JC2 is unresolved.
Basis:47bc9b24cdc26840de5417fe74aefc9f12890cb7. No source or CAS import.
Scope is exactly the polynomial filtration below, not all Keller eigenvaluations, all Rees deformations, or a global proof of JC2.

## Claim for review
Let B=C[x,y], w=x^2-y^5. Every polynomial has a unique normal form f(y,w)+x g(y,w).
Let delta be the maximum weight of that normal form, with weights(x,y,w)=(5,2,3), and delta(0)=-infinity.
Suppose F*:B->B sends x to P and y to Q, has constant nonzero Jacobian J, and for an integer e>=1 satisfies
    delta(F*f)=e delta(f) for EVERY nonzero f in B.                (1)
CLAIM: e=1, P=alpha x, Q=beta y with alpha,beta nonzero and alpha^2=beta^5.
In particular no e>1 map satisfying these hypotheses exists.
Equation(1) is a strong full-filtration hypothesis. Three separate generator-degree equalities without injectivity on the associated graded ring do not replace it.

## 1. Actual filtration and its Euler derivation
The filtration F_m B is spanned by x^epsilon y^a w^b with epsilon=0 or1, a,b>=0 and 5epsilon+2a+3b<=m.
Its associated graded ring is A0=C[X,Y,W]/(X^2-Y^5), weights(5,2,3); it is a domain, so delta is multiplicative.
The monic relation x^2=y^5+w gives the normal basis and this associated graded presentation directly. All pieces are finite dimensional.
Put E=5x partial_x+2y partial_y. Then E(w)=10w, so each normal monomial is an E-eigenvector.
Thus delta(Ef)<=delta(f), even though the E-weight of w is10 and its delta-weight is3. These two gradings must not be confused.

## 2. Polynomial transport of E
Set D_P=(Q_y partial_x-Q_x partial_y)/J and D_Q=(-P_y partial_x+P_x partial_y)/J.
These are polynomial derivations because J is a nonzero constant; D_P(P)=D_Q(Q)=1 and D_P(Q)=D_Q(P)=0.
Define D=5P D_P+2Q D_Q. Then D(P)=5P and D(Q)=2Q, and for every f in B,
    D(F*f)=F*(Ef).                                               (2)
This constructs D on the whole actual source ring. It is not an assumed extension to a finite normalization or a completeness assertion.

## 3. Positive filtered order is impossible
Any polynomial derivation L of B has finite filtered order bounded by
    q=max(delta(Lx)-5, delta(Ly)-2, delta(Lw)-3).
Indeed apply Leibniz to each normal monomial; multiplicativity of delta gives delta(Lf)<=delta(f)+q. Zero derivatives contribute -infinity.
If q is finite and positive, at least one of x,y,w attains it. Therefore L induces a NONZERO derivation of degree q on A0.
Apply this to D. Suppose q>0 and write its leading derivation as Dbar.
By(1),(2) and delta(Ef)<=delta(f), every F*f satisfies delta(D(F*f))<=delta(F*f).
Consequently Dbar annihilates the entire image phi(A0) of the injective graded map induced by F*, with degrees multiplied by e.
Let L0=Frac(A0) and K0=Frac(phi(A0)). Both have transcendence degree2 over C; L0 is finitely generated over K0 and algebraic, hence a finite algebraic extension.
The derivation Dbar extends to L0 and vanishes on K0. Characteristic zero makes the extension separable.
For any algebraic element a with minimal polynomial m over K0, differentiation gives m'(a)Dbar(a)=0; hence Dbar(a)=0.
This contradicts nonzero Dbar. Thus q<=0 and
    delta(Df)<=delta(f) for every f in B.                         (3)
No finiteness of F*, integrality of B over F*(B), normalization regularity, tame-valuation theorem, or algebraization theorem was used here.

## 4. All polynomial derivations satisfying(3)
Let L be any such derivation. The actual small filtered pieces force
    Ly=a+b y,
    Lx=c0+c1 y+c2 w+c3 y^2+c4 x+c5 y w.
In particular y w belongs to F_5 and MUST be included; it has the same delta-weight as x.
From Lw=2x Lx-5y^4 Ly and x^2=y^5+w, obtain
    Lw=(2c4-5b)y^5+2c5 x y w+2c3 x y^2+2c2 x w
       -5a y^4+2c1 x y+2c0 x+2c4 w.                             (4)
The degree10 normal monomials y^5 and x y w are independent, so 2c4=5b and c5=0.
Degree9 forces c3=0. The independent degree8 monomials x w and y^4 force c2=a=0.
Degrees7 and5 force c1=c0=0. Therefore L=mu E, with mu=b/2, and Lw=10mu w.
This is an explicit calculation in B; no classification of algebraic group actions is required.

## 5. Divergence determines the scalar and closes the candidate
The polynomial derivations D_P and D_Q have divergence zero, by equality of mixed partials and constancy of J.
Thus div(D)=5D_P(P)+2D_Q(Q)=7, while div(E)=7.
By sections3-4 D=mu E, so mu=1. Equations(2) now give E(P)=5P and E(Q)=2Q.
In the ordinary positive weight grading wt(x,y)=(5,2), the weight5 space is C x and the weight2 space is C y.
Hence P=alpha x and Q=beta y. Their Jacobian makes alpha,beta nonzero, and(1) for y gives e=1.
Finally F*w=alpha^2 w+(alpha^2-beta^5)y^5; its delta-degree must be3, so alpha^2=beta^5.
For Jacobian1 this further gives alpha beta=1 and alpha^7=1. The exclusion of e>1 does not require this last specialization.

## 6. Consumer: the previously unresolved exact Rees lifts
The retained CUSPFACTOR0603/CUSPVERIFY0633 problem uses S=C[X,Y,W,T]/(X^2-Y^5-WT^7), weights(5,2,3,1).
Its bracket has T central and {X,Y}=T^7, {Y,W}=-2X, {X,W}=-5Y^4; it is homogeneous of degree zero.
Suppose a FULL homogeneous algebra lift has weights(U,V,H)=(5e,2e,3e), sends T to T^e, has the prescribed injective graded Poisson central map, and satisfies U^2-V^5=T^(7e)H.
Bracketing with V gives -2U{U,V}=T^(7e){V,H}. Since T is prime in S and U is not T-divisible, T^(7e) divides {U,V}.
Its homogeneous quotient has degree zero, hence is a scalar c. The central Poisson identity {V0,H0}=-2U0 forces c=1.
Specializing T=1 therefore gives Jac(P,Q)=1; central injectivity gives exactly(1), not merely three degree bounds.
If the candidate theorem above survives review, every such e>1 full lift is excluded, including ALL remaining k>=2 factors in that fixed explicit family.
This would close that precise lifting problem. It would not prove that an arbitrary hypothetical Keller map supplies this filtration, nor settle the global finite-normalization or primitive no-fold gaps.
Completed-local or rational formal lifts with poles are not being excluded by an argument pretending that they are polynomial.

## Review priorities, history and limits
Attack especially the finite filtered-order bound, nonzero leading derivation, annihilation of phi(A0), algebraicity/separability of its fraction-field extension, and the complete small-piece enumeration in(4).
Also check divergence transport and the full-Rees-lift consumer without assuming any missing finiteness or local-finiteness premise.
The concrete changed input is the polynomial inverse-Jacobian derivation plus the algebraic graded-subfield argument. Generic Euler/flow/graded-injectivity controls did not supply that chain.
Current frozen history: HQ4/public3 hits, all7 headers/previews routed; archived October16:306-329 and October14:4743-4766 plus DECOMP1307 task1-35 read,83/200LF.
Those scopes retain the prohibition on generic Euler/flow or abstract cusp-cylinder renewal without a changed whole-source argument. No exhaustive novelty claim follows from this bounded search.
The prior full CUSPFACTOR122LF and independent CUSPVERIFY82LF were already read and pinned in REES1705; their scope is retained, not silently broadened.
No paid lane or public promotion is authorized by this report alone. Independent hostile review is required before adoption.
Original candidate partial17:35/ROOT17:50/bank18:00 UTC2026-11-07 retained; GitHub17:45:02/18:15:02 and all other clocks unchanged.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7666`.
- Body SHA-256:
  `244e7e9db5c086b10e05f9a15ac52804d42a5ab46b2c2073feaa24c4a3ea8505`.
- Frozen basis: `47bc9b24cdc26840de5417fe74aefc9f12890cb7`.
