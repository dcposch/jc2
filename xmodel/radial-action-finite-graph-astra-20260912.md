# Radial action and a finite canonical graph

MANUAL co-research, not FIRST/promotion. First2026-09-12 12:50:09 UTC; reserve13:02/HARD13:05 unchanged. Both inputs matched and freshly WHOLE, COORDINATION before TASK. Own outputs absent; no other mathematical input or execution.

## Exact quantities

For a polynomial complex Keller pair, decide radial-potential field generation and existence of a finite birational canonical graph after an explicit polynomial symplectic source shear. Separate these from finiteness of the Keller map and normality of the graph.

## Result

Both candidates hold. Every radial canonical potential generates the source function field with f,g. After the linear change and polynomial shear, one such H gives a finite birational surjective canonical graph with normalization A2. Graph normality and Keller invertibility do NOT follow. All conclusions are MANUAL/UNREVIEWED.

## A. Radial field generation

Let R=C[x,y], L=Frac(R), F=C(f,g), and alpha=(x dy-y dx)/2. Since d alpha=dx wedge dy=df wedge dg, a polynomial T with dT=alpha-f dg exists; its additive constant is irrelevant. Jacobian one implies f,g algebraically independent and L/F finite separable. Put K=F(T). The derivations partial_f and partial_g extend uniquely through these finite characteristic-zero fields. For an algebraic element a with separable minimal polynomial m, the forced extension formula is D(a)=-(D m)(a)/m'(a), which lies in the same field; restrictions are compatible by uniqueness.

The inverse Jacobian gives

    partial_f=g_y partial_x-g_x partial_y,
    partial_g=-f_y partial_x+f_x partial_y.

For E=(x partial_x+y partial_y)/2, contraction with dT gives

    T_f=-E(g),       T_g=E(f)-f.

Moreover alpha(E)=0, so E(T)=-f E(g)=f T_f. Hence

    E(f)=f+T_g,       E(g)=-T_f,       E(T)=f T_f

all belong to K. Product and quotient rules prove E(K) is contained in K. The last identity is essential; preservation of f,g alone does not establish preservation of F(T). No multiplicative-group action on K was assumed.

For a polynomial A in K of total degree at most n, write A=sum A_i with A_i homogeneous of degree i. Finite interpolation in E yields

    A_i=[product_(0<=j<=n,j!=i) (E-j/2)/((i-j)/2)] A in K.

Only nonzero rational constants are divided by. Thus the linear homogeneous pieces f_1,g_1 belong to K. Their coefficient matrix is the Jacobian matrix of f,g at the origin, of determinant one. They therefore span x,y over C, proving K=L. Constants in f,g contribute degree zero and cause no obstruction. This is total-degree projection for the radial potential, not a correction of the distinct x dy potential theorem.

For a full-plane sanity check, f=x+a,g=y+b has T=-xy/2-a y up to a constant: its derivative is exactly alpha-f dg, and f_1=x,g_1=y. For a genuine out-of-scope control, on x!=0 let f=x^2,g=y/(2x). Then J=1 and f dg=alpha, so T=0 is radial canonical, yet F(T)=F is a proper degree-two subfield of L. Indeed L=F(x), x^2=f, y=2gx, and (x,y)->(-x,-y) fixes F. This rational punctured-plane example removes global polynomiality and is NOT a full-plane Keller counterexample.

## B. Algebraic finiteness with all lower terms retained

Let m=deg(f)>=1. Choose a nonzero vector v with f_m(v)!=0, and a vector w with det(w,v)=1. The linear source substitution (old x,old y)=w*x+v*y is determinant one and gives f_m(0,1)!=0 in the new coordinates. Such a v exists because f_m is a nonzero homogeneous polynomial. The area form alpha is invariant under this linear substitution; in any event recompute T by dT=alpha-f dg in the chosen coordinates.

Choose an integer N>max(deg(T),2), interpreting the degree condition harmlessly if T is zero, and put H=T+x^N. Its top form is x^N. The forms f_m and x^N have no common point on P1: x=0 is the only zero of x^N there, and f_m(0,1)!=0.

Here is an explicit filtered proof, not an assertion of properness. Write f_m=c*y^m+x*(homogeneous polynomial), with c!=0. The homogeneous quotient

    R/(f_m,x^N)

is spanned over C by x^i y^j with 0<=i<N, 0<=j<m: reduce modulo x^N and divide by the monic-in-y polynomial c^-1 f_m. These operations preserve total degree, so every homogeneous polynomial of degree greater than D=N+m-2 belongs to (f_m,x^N).

Let A=C[f,H]. Induct on total degree to show that all monomials of degree at most D generate R as an A-module. For P of degree d>D, its top homogeneous part has a homogeneous expression

    P_d=f_m a_(d-m)+x^N b_(d-N),

with absent negative-degree coefficients interpreted as zero. Subtract f*a+H*b. The remainder has degree less than d, and a,b themselves have degree less than d because m,N are positive. Induction expresses each in the fixed finite generating set over A. This retains every lower term of f and H and terminates strictly by degree. Therefore R is finite over A. Integrality preserves dimension, so dim(A)=2 and f,H are algebraically independent. Thus (f,H):A2->A2 is a finite surjective morphism.

Now let B=C[f,g,H]. The same finite A-module generators also generate R as a B-module, since A is contained in B and B in R. Hence j_H:Spec(R)->Spec(B) is finite and surjective by lying over. This says nothing yet about finiteness over C[f,g].

## C. The canonical shear and normalization attachment

Set

    X=x,       Y=y+(2N/(N-2))*x^(N-1).

This is a polynomial automorphism of Jacobian one with polynomial inverse. Direct differentiation, including the subtraction of Y dX, gives

    (X dY-Y dX)/2
      =alpha+[(2N/(N-2))*(N-2)/2]*x^(N-1) dx
      =alpha+d(x^N).

Consequently dH=(X dY-Y dX)/2-f dg. Expressed in X,Y, the same f,g remain polynomial with Jacobian one. Part A applies to this radial potential H, so Frac(B)=C(X,Y)=L. The leading-form finiteness proof was performed before the shear; it need not remain a leading-form statement afterward, since the coordinate ring has not changed.

Thus j_H is finite birational surjective. R is exactly the integral closure of B in L: R is integral over B and integrally closed, while every element of L integral over B is also integral over R, hence belongs to R. This is an algebraic finite canonical-graph attachment with normalization A2, not an assertion that Spec(B) itself is normal. Choices of additive constants in T or H change neither the rings nor the argument.

## D. Exact global gap and a stronger control

The Keller differential identity makes Omega_(R/C[f,g])=0, hence also Omega_(R/B)=0. Thus even unramifiedness of j_H does not discharge the missing normality argument. An elementary abstract control retaining finite, birational, unramified normalization and a simply connected smooth source is

    R0=C[t,s],       B0=C[u,v,s],
    u=t^2-1,        v=t(t^2-1).

Here v^2=u^2(u+1), t satisfies t^2=u+1, and t=v/u in the fraction field. Thus R0 is the finite normalization of B0. Points (1,s) and (-1,s) have the same image, so it is not an isomorphism and B0 is nonnormal. Moreover du=2t dt, dv=(3t^2-1)dt and

    3t du-2dv=2dt.

Together with ds this proves Omega_(R0/B0)=0. This is a nodal curve times A1, NOT an example of a polynomial Keller pair generating the particular B above. It refutes the general finite-birational/unramified/smooth-source inference only; it does not decide normality for a canonical Keller graph.

There is a useful precise conditional implication in the actual source situation. If B is normal, the normalization statement gives B=R. Put A0=C[f,g]. Then R=A0[H], so the surjection C[U,V,W]->R has height-one prime kernel (P), with P irreducible and of positive W-degree. It has no nonzero relation in U,V because f,g are algebraically independent. The relative differential presentation is

    Omega_(R/A0)=R dW/(P_W dW)=0.

Hence the image of P_W is a unit of R=C[x,y], necessarily a nonzero complex constant c. Thus P_W-c belongs to (P). Its W-degree is smaller than that of P, so P_W-c=0 as a polynomial; polynomial multiples of a nonzero P cannot have smaller W-degree. Characteristic zero now gives P=cW+Q(U,V). Therefore H belongs to A0 and R=A0: f,g form a polynomial automorphism. Conversely an automorphism gives A0=R=B, which is normal. For these constructed graphs, normality is therefore equivalent to invertibility, not a consequence already obtained from finiteness.

This conditional argument uses the actual global unit group R^*=C^* and the Keller differential condition; neither is available in arbitrary finite-graph reasoning in the required combination. No normality proof, conductor elimination, individual-divisor saturation, BGV import, or JC2 conclusion is supplied. Generic finite primitive graphs are not claimed new; the verified additional feature is retaining an explicitly canonical radial potential through a source shear.

## Quantity, controls and stopping point

The requested quantities are settled manually; normality of the exact B remains the equivalent invertibility gate. Cheapest independent check: audit E(T), the degree induction, shear coefficient and relative differential presentation. Five minutes is UNMEASURED planning, not observed cost or authority. The three controls above were checked manually. No normality search, canonical OPEN, charge_basis or descendant is declared.

## Read scope and closeout

Exactly COORDINATION and TASK are charged inputs. COORDINATION806lines freshly read in1–220,221–440,441–660,661–806; TASK fresh WHOLE. All links inert. No old theorem, peer/live body, corpus, network, worker, protected tree, scientific interpreter/CAS/helper/import/AST/syntax/test or agent used. Only inert text/hash/UTC/presence and apply_patch plus existing administrative artifact_finalize. Own WHOLE, postpins, quantity/control and absence checks precede marker LAST. No canonical OPEN or charge_basis.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9755`.
- Body SHA-256:
  `fb7ecaa28b33e30fd424d8b80c158e954f31d7b30982b3d6a1e2188c4ca7794d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
