Boundary coefficient spaces over the entire centre ring
=======================================================

These counts are BEFORE the transverse Jacobian recurrence and BEFORE the
characteristic identity R=G^3-F^2+aG^2+bFG+cF+dG+e0. They do not establish a
survivor of either additional system. Counts for R's minor boundary are
conditional on the separate source-license audit.

Let A be Q adjoined all retained minor centres and separation parameters, and
lambda when R is present. A parameter in the target face stays in A; no centre
or separation is specialized. Put z=y-x and w=y/x. Write a degree-D polynomial
as sum_{n=0}^D x^n f_n(w). The linear map from its physical coefficients to
the coefficients of f_n is the identity after indexing by total degree. The
map from x,z coefficients to x,y coefficients is the binomial substitution
z=y-x, with inverse y=z+x, over A.

For a major weight bound d*i-k<=h in x^i*z^k, set

    m_n=max(0,ceil((d*n-h)/(d+1))).

The major floor says that f_n is divisible by (w-1)^m_n. If d*n-h is a
nonnegative multiple of d+1, its first coefficient at w=1 is fixed by the
actual major face; let E_n=1 then, and 0 otherwise. All face coefficients,
including zero coefficients, are retained. After subtracting this prescribed
term, the unknown columns at degree n are (w-1)^k for
m_n+E_n<=k<=n.

For minor pole bound b and radius delta put s=1+delta and

    l_n=max(0,ceil((n-b)/s)).

There are l_n strict minor rows whose principal terms are the coefficients
of w^0,...,w^(l_n-1). If (n-b)/s is a nonnegative integer there is one more
row, the actual minor face coefficient; denote this indicator by L_n.

This principal-term description is valid with ALL centres, rather than only
at zero centres. A minor row has an x-power p and residue power r. Assign it
homogeneous degree n=p+s*r (which is integral on the cleared cover). A term
of a lower centre of physical order alpha<delta replacing one residue factor
contributes only from homogeneous degree n+(1+alpha). Repeated replacements
add these strictly positive increments. A constant centre has increment1;
u/x has increment2; v/x^2 has increment3. At-level constant shifts have
increment s. Thus descending induction in physical degree n makes every
centre contribution part of the already determined right-hand side. The
free mean mu in the D108 target Q=((pi-mu)^2-c) changes only that right-hand
side. These are polynomial operations over A, not a generic fibre count.

At degree n the matrix for rows j=0,...,r-1 and columns
k=M,...,M+r-1, M=m_n+E_n, is

    B[j,k-M]=(-1)^(k-j)*binom(k,j).

Its determinant is (-1)^(r*M). Indeed the Pascal finite-difference identity
reduces the determinant of binom(M+i,j), 0<=i,j<r, to 1; extracting the signs
gives the displayed sign. Therefore every pivot is a unit over A. Choosing
the first min(l_n+L_n,n+1-M) columns gives a polynomial graph map over A,
with a polynomial inverse obtained by retaining all remaining coefficients.
The graph map is reconstructed in descending n by the preceding row formula.
It carries every raw row to zero, except any explicit compatibility rows.

The remaining count at each n is

    max(0,n+1-m_n-l_n-E_n-L_n).

All nine spaces below have exactly one excess equation, at n=D. There
m_D+l_D=D, and f_D=A_top*w^l_D*(w-1)^m_D. The compatibility is that the
minor leading coefficient equals (-1)^m_D times the major leading coefficient.
It holds for the specified targets: +1 for every F/G; +lambda for99 R;
-lambda for108 R. Changing the specified minor top by1 gives residual1.
There is no centre-dependent compatibility equation in these boundary-only
linear systems.

Counts exclude all scalar centres, separation and lambda:

| Client/polynomial | Major floor | Both floors | Both floors+major face | Both complete faces |
|---|---:|---:|---:|---:|
|99 delta2 F|1522|388|363|336|
|99 delta2 G|694|181|164|146|
|99 delta5/2 F|1522|192|167|154|
|99 delta5/2 G|694|91|74|65|
|108 free-mean F|1501|301|279|255|
|108 free-mean G|685|141|126|110|
|99 delta2 R, conditional|489|129|115|100|
|99 delta5/2 R, conditional|489|65|51|44|
|108 free-mean R, conditional|530|110|97|83|

The authoritative arithmetic is boundary_counts.py/.json; the F/G row entries
in this note must agree with that output. In particular these are counts of
boundary coefficients, not counts after the nonlinear transverse recurrence.
The combined complete-face counts for F,G are482,219,365. Including the
conditional R coordinates gives582,263,448.

For99 the major h values are9,6,5 and degrees99,66,55; d=3. For108 they
are12,8,7 and degrees108,72,63; d=4. The minor b values for99 delta2 are
18,12,10, for99 delta5/2 are9/2,3,5/2, and for108 are12,8,7. Their target
degrees are respectively27/18/15 and24/16/14. The99 actual F/G targets and
the centre transport are in the charged g9966 report; the108 free-mean and
R source hypotheses are audited separately by this lane.

Actual coefficient maps and their replay
---------------------------------------

`boundary_maps.py` constructs the maps as exact arithmetic circuits in Q over
the unspecialized scalar ring A. It stores Merkle roots rather than expression
trees; deterministic re-execution reconstructs every operation. The extra
`boundary_maps.json` receipt records each forward map, inverse projection,
integer inverse-matrix certificate and independent rational raw-row replay.

On the licensed jet0=0 slice write the minor arc as

    y=u/x+v/x^2+pi/x^delta.

For delta2, v is the free minor_a2, and pi is zeta; its face is
zeta^2(zeta+3*rho). For delta5/2 the face is pi(pi^2-c). For108 the free mean
stays in the face ((pi-mu)^2-c); no equation fixes mu. If
H=sum p[N,j]*x^(N-j)*y^j, the exact row with assigned degree n and residue
degree r is

    sum_{a,b>=0, N=n+2a+3b<=D, j=r+a+b<=N}
      binom(j,r)*binom(a+b,a)*u^a*v^b*p[N,j].

The a=b=0 term is p[n,r]. Every other term uses N>n. Subtract the prescribed
minor target and all higher-degree terms. Within the current block subtract
the fixed major equality term and the retained high-k free columns. Apply
the explicit integer inverse matrix to the remaining right-hand side. This
is the actual graph construction in the driver; it is not a count-only
existence assertion.

For M>0 and r pivot rows, the inverse of B above is

    B_inverse[k,l]=(-1)^M * sum_{j=max(k,l)}^(r-1)
                       binom(j,k)*binom(M+j-l-1,j-l).

For M=0 it is binom(l,k) when l>=k and zero otherwise. These formulas come
from division by (w-1)^M in A[[w]], truncation below w^r, and the substitution
w=(w-1)+1. The driver checks B*B_inverse=I over Z for every distinct block.
The variable w is never inverted. Restoring the ambient x,y coefficients is
the exact binomial change p[n,j]=sum_{k>=j}(-1)^(k-j)binom(k,j)c[n,k].

More formally let S=A[c[n,k]:0<=k<=n<=D] and let I_boundary contain every
major floor/actual-face row and every minor pole/actual-face row. Let T be
A adjoined the surviving high-k coefficients. Define phi:S->T by the circuit,
and psi:T->S/I_boundary by sending each free coefficient to its original
class. The unit block identity and descending-degree induction prove
phi(I_boundary)=0; the only extra top block is the already checked leading
compatibility. They also prove psi*phi is identity on S/I_boundary, while
phi*psi is identity on T by construction. Thus S/I_boundary is isomorphic
to T over A. This is a two-way coefficient map for precisely the declared
boundary ideal. It does not transport unlisted D1/tower/characteristic rows
unless they are explicitly substituted through phi.

The all-client run constructs674617 circuit nodes in approximately22 seconds
and checks6680 minor rows at each of two rational controls, plus20660 major
rows at each control. These evaluations are exact Q checks and only controls;
the symbolic proof above establishes universality. The rational points use
nonzero separation and lambda, with different u,v values;108 also uses
different nonzero means. A changed minor leading coefficient by1 has residual1.
No whole-chart survival or nilpotence conclusion follows from these controls.

Source-audit follow-up: the separate transport audit supplies the minor R
licence using Prop6.1(2), Def3.1(4), and the full leading target. The retained
`_conditional` client names record this driver's original scope; the reported
arithmetic is unchanged. For108 its notation Q is negative-monic, whereas
this note uses the positive-monic quadratic. The shared explicit R target is

    -lambda*((pi-mu)^2-c)^7.

Replacing that minus sign by plus gives top compatibility residual2*lambda
and would manufacture a false localized unit.
