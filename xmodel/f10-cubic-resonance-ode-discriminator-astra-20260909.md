# The standalone cubic/quintic resonance equation has solutions for every stated parameter

September9,2026. Owner /root/model_productivity. **UNREVIEWED standalone existence theorem and exact algebraic parametrization.** No source attachment, F10 exclusion, receiver point or JC2 conclusion is asserted. All arguments below are manual; ZERO mathematical subprocesses of any size.

## 1. Result and precise problem

Let K be algebraically closed of characteristic zero, q>=0 an integer, and m=3q+4. There EXIST monic C,D in K[T], of degrees3,5, and k!=0, satisfying

    (5m+1)T C'D - 3m T CD' - 3CD = k.                  (1)

In fact the construction below works over the algebraic closure of Q, supplies an exact algebraic recipe for every m in this family, and parametrizes ALL solutions, up to an explicitly justified nonzero scaling of T. It is not a finite-sample argument. It disproves an impossibility claim for the literal equation(1), not any stronger source condition from which that equation might be necessary.

Define

    h=(5m+1)/3=5q+7,     a=h/m=(5m+1)/(3m).

Then 3h-5m=1, gcd(h,m)=1, m>=4, h>=7. In particular a is none of0,1,2,3,4,5,6. This elementary nonvanishing, not an order on K, is what is used below.

## 2. Root restrictions are consequences, not assumptions

Evaluation of(1) at T=0 gives

    k=-3 C(0)D(0).

Thus both constants are nonzero. A common root of C,D would make the left side zero. A repeated root of C would make C and C' zero there and again make the left side zero; the same applies to D. Consequently every solution automatically has three and five simple, nonzero, mutually disjoint roots. At a root alpha of C and a root beta of D the exact identities are

    (5m+1)alpha C'(alpha)D(alpha)=k,
    -3m beta C(beta)D'(beta)=k.

No squarefree, distinct-root or nonzero-constant condition has been imposed in the construction to manufacture this conclusion.

## 3. Reciprocal polynomials and an exact finite contact problem

Put x=1/T and

    c(x)=x^3 C(1/x),       d(x)=x^5 D(1/x).

Monicity says c(0)=d(0)=1. They have degrees at most3,5 before using their constants. Direct differentiation, keeping all three terms in(1), gives

    (5m+1)T C'D-3m T CD'-3CD
       =T^7 {3m c d'-(5m+1)c'd}.

The top scalar cancels because 3(5m+1)-15m-3=0. Therefore(1) is equivalent to

    W(x):=3m c d'-(5m+1)c'd = k x^7.                  (2)

Write c=1+u x+v x^2+w x^3, and define the formal binomial coefficients

    f_N(u,v,w)=[x^N](1+u x+v x^2+w x^3)^a.

For clarity this is the following FINITE rational polynomial, so no analytic branch is used:

    f_N = sum over i+2j+3l=N of
          (a)_(i+j+l) u^i v^j w^l /(i! j! l!),

where (a)_r=a(a-1)...(a-r+1), and (a)_0=1. It is homogeneous of weighted degree N for weights1,2,3 on u,v,w. Define

    d(x)=sum_(N=0)^5 f_N(u,v,w)x^N.

The ENTIRE needed parameter system is exactly

    f_6(u,v,w)=0,       f_7(u,v,w)=0,       (u,v,w)!=(0,0,0).       (3)

Indeed(3) gives d-c^a=O(x^8). The formal identity (c^a)'=a c^(a-1)c' implies W=O(x^7). Since deg W<=7, W=k x^7 for a scalar k. This proves an exact polynomial identity, not just a truncated equation.

Conversely, if(2) holds, then

    (log d-a log c)' = W/(3m c d)=O(x^7).

Both logarithms have constant0. Characteristic zero permits termwise formal integration, hence log d-a log c=O(x^8), and d-c^a=O(x^8). Since deg d<=5, its coefficients MUST be f_0,...,f_5 and f_6=f_7=0. Thus(3) is a necessary and sufficient algebraic coefficient description once k!=0 is proved. There are no omitted middle differential coefficients.

## 4. Every nonzero point of(3) gives k!=0 and the required exact degrees

Suppose k=0. The rational-function derivative of d^m/c^h then vanishes, so d^m/c^h is a constant in K; evaluating at x=0 makes it1. Thus

    d^m=c^h.

For any irreducible factor of c, coprimality gcd(h,m)=1 forces its multiplicity in c to be divisible by m. But deg c<=3<m. Therefore c=1, and d=1 follows from its value at0. Thus u=v=w=0, contrary to(3). This elementary factor argument accounts for all possible repeated factors; none is assumed absent.

We have proved k!=0 at EVERY nonzero common point of f_6,f_7. Since W has degree7 and deg W<=deg c+deg d-1, while deg c<=3 and deg d<=5, necessarily

    deg c=3,       deg d=5.

In particular w!=0 and d_5:=f_5(u,v,w)!=0. Comparing the degree7 term in W gives

    k=(15m-3(5m+1))w d_5=-3w d_5!=0.                 (4)

The reciprocals C=T^3+uT^2+vT+w and D=T^5 d(1/T) are therefore monic of exact degrees3,5, with nonzero constants, and satisfy(1). The root restrictions in Section2 follow automatically. The contact d-c^a is exactly of order8, not higher: its coefficient at x^8 is k/(24m), from(2) and the logarithmic derivative. This also supplies an independent sign check on the contact convention.

## 5. Uniform existence, using a small homogeneous resultant

It remains to prove that(3) has a nonzero solution for EVERY stated m. No actual resultant, coefficient solve, numerical experiment or source power was run.

Set

    F(X,Y,Z)=f_6(X,Y^2,Z^3),
    G(X,Y,Z)=f_7(X,Y^2,Z^3).

These are ordinary homogeneous forms of degrees6,7 in three variables. Their coefficients of X^6,X^7 are respectively (a)_6/6! and (a)_7/7!, both NONZERO scalars. In particular, considered as polynomials in X, their leading coefficients are nonzero constants and never disappear under a specialization of Y,Z.

Let R(Y,Z)=Res_X(F,G), the Sylvester resultant. The elementary facts needed here follow from its determinant, or its root-product formula: it is a polynomial in Y,Z; after any specialization its value is zero exactly when these two fixed-degree X-polynomials have a common root; and homogeneity gives

    R(tY,tZ)=t^42 R(Y,Z).

For example, each root of F in X scales by t, and G evaluated at that root scales by t^7, giving total exponent6*7=42. These facts are elementary polynomial linear algebra; no external library computation or theorem-specific software is invoked.

If R is identically zero, take any nonzero pair(Y,Z). The two specialized polynomials have a common finite root X, since their leading coefficients remain nonzero. If R is not zero, it is a binary homogeneous form of positive degree42. Over an algebraically closed field such a form has a projective zero(Y:Z): either its dehomogenization has a root, or it is a pure power in the other variable and vanishes at the remaining projective point. At this nonzero pair the same resultant property gives a common finite X.

In BOTH cases (X,Y,Z)!=(0,0,0) and

    u=X,       v=Y^2,       w=Z^3

is a nonzero solution of(3). Sections3–4 therefore construct the required solution of(1). This proves existence uniformly, not generically and not just away from an undisclosed finite exceptional list. The nonzero leading resultant coefficients were checked for every m=3q+4.

Because all displayed coefficients are rational for each integer m, this same construction can be performed in Qbar: roots of the binary resultant and of the specialized X-polynomials are algebraic numbers. Every algebraically closed characteristic-zero K contains a copy of Qbar, so the resulting pair exists in the requested field. No real-coefficient, real-root or same-number-field conclusion is claimed.

## 6. Explicit normalized algebraic recipe and completeness

Every nonzero solution of(3) has u!=0. To see this without a genericity assumption, set u=0. The only partitions contributing to f_6,f_7 give

    f_6(0,v,w)=(a)_2 w^2/2+(a)_3 v^3/6,
    f_7(0,v,w)=(a)_3 v^2 w/2.

Here (a)_2 and (a)_3 are nonzero. The second equation forces v=0 or w=0, and the first then forces both zero. This is the excluded origin.

Scaling T is licensed exactly as follows: for t!=0 put

    C_t(T)=t^-3 C(tT),       D_t(T)=t^-5 D(tT).

They are monic and satisfy(1) with k_t=t^-8 k. Their reciprocal coefficients are (u/t,v/t^2,w/t^3). Thus choosing t=u normalizes u=1. No translation of T, independent output scaling, or normalization of k at the same time is silently performed.

If the problem prescribes a particular nonzero target k_star, rather than allowing any k!=0, the same scaling realizes it: choose t with t^8=k/k_star in K. This latter choice need not preserve u=1. Thus every prescribed nonzero target is also attained, without asserting two simultaneous normalizations.

An exact recipe, and classification up to this scaling, is therefore:

1. Set a=(5m+1)/(3m). Choose ANY common solution(v,w) in K^2 of f_6(1,v,w)=f_7(1,v,w)=0. The preceding proof guarantees at least one.
2. Put C=T^3+T^2+vT+w and
       D=sum_(N=0)^5 f_N(1,v,w) T^(5-N).
3. Put k=-3w f_5(1,v,w). This is nonzero automatically; no additional point selection is needed.

For a completely explicit two-equation algebraic description, write a_r=(a)_r. The two polynomials in step1 are

    f_6(1,v,w)=a_6/720+a_5 v/24+a_4 v^2/4+a_3 v^3/6
                   +a_4 w/6+a_3 v w+a_2 w^2/2,

    f_7(1,v,w)=a_7/5040+a_6 v/120+a_5 v^2/12+a_4 v^3/6
                   +a_5 w/24+a_4 v w/2+a_3 v^2 w/2+a_3 w^2/2.

These are obtained directly from the finite partition formula, not by an executed expansion. They are an exact algebraic construction, not a decimal or sampled approximation. Section3 proves the converse, so EVERY pair solving(1), after the stated T-scaling, occurs in this description. No solution is lost by setting u=1.

One may also verify that this normalized algebraic set is finite, without solving it. A common homogeneous factor of F,G would vanish somewhere on X=0: its restriction there is either identically zero or a binary positive-degree homogeneous form. But the u=0 calculation shows there is no common projective zero on X=0. Hence F,G have no common factor, and their X-resultant is not identically zero. It has finitely many projective(Y:Z) zeros; each gives finitely many X roots. This makes their projective intersection finite, and the normalization X=1 together with v=Y^2,w=Z^3 makes the stated parameter set finite as well. No multiplicity count or claim of seven distinct solutions is made.

## 7. Meaningful manual changed-object controls

All controls are manual and do not represent full-source points.

- Keeping only d=[c^a] through degree5 is insufficient. For c=1+x, the coefficient f_6=binom(a,6) is nonzero. The leading discrepancy gives W=-18m f_6 x^5+O(x^6), not kx^7. The two imposed contact coefficients are essential.
- Attempting u=0 does not provide a hidden missing family: the two explicit equations above force v=w=0, which gives k=0 and is rejected. The T-scaling normalization was proved rather than presumed.
- The multiplicity argument excluding k=0 uses the parameter range. For m=1, outside the task, a=2 and c=1+x,d=(1+x)^2 give W=0 with nonconstant c. Thus the reduced-denominator/degree check is load-bearing, not a universal claim about arbitrary rational a.
- For a constructed pair, changing only the claimed k away from -3w d_5 immediately fails(1) at T=0. The target scalar is not a free label that can disguise a wrong identity.
- Repeated or common nonzero roots in a proposed C,D force k=0 by direct evaluation and are rejected by Section2. Our resultant construction requires no unchecked distinctness assumption to avoid this failure.

## 8. Read perimeter, scope and terminal status

This is independent of all source producers, current gates and peers. The only mathematical input is the exact standalone equation and parameter/field conditions supplied in the task. The prompt's possible F10 attachment is explicitly UNREVIEWED and was not used. No source report, uniform local exclusion, protected project, live report/log/receipt, broad literature sweep or new primary claim was read or imported. No mathematical subprocess, CAS, toy code, coefficient emission, actual source power, solver, AWS/SSH, agent or shared/public write occurred.

The result is a new UNREVIEWED campaign discriminator: the literal small-polynomial equation has solutions for EVERY required m, with exact algebraic construction and a complete normalized coefficient parametrization. It does NOT certify any of those solutions as realizable F10 source initials or as a receiver/Keller point. Any proposed contradiction must use additional source restrictions, not this ODE alone. No literature novelty, exhaustive source attachment or follow-on task is claimed.

The owned INPUT.md freezes the exact standalone problem and no-source premise; READ-SCOPE.md records the zero-source/zero-subprocess perimeter. Current hashes, own whole/open check and the normal artifact transaction are recorded in terminal custody. All writers become IDLE after publication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12649`.
- Body SHA-256:
  `5e113c2e5a7671ac8e31a11ed6298486245df34537d374a69be91c6c1fce3e15`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
