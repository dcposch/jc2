# Nonsingular components and a nonclosed Hamiltonian image at infinity

October 30, 2026. **PROVISIONAL / MANUAL; independent review PASS. JC2 remains unresolved.**

The construction below keeps one globally nonsingular polynomial P and one
primitive infinity valuation fixed. Globally nonsingular polynomial partners Q_n
make the Jacobian approach 1 to arbitrarily high valuation order, although P has
no polynomial Jacobian mate. The full graded source and target are smooth and
symplectic, with normal index 1 and residue degree 2. The filtered target algebra
is not Poisson closed. Thus component nonsingularity does not repair this
particular finite-jet obstruction; full filtered or global Keller constraints
remain essential. Degree grows with precision.

The proof is copied verbatim from the [frozen author candidate](../box/nonsingular-components-infinity-jets-20261030/CANDIDATE.md),
lines 7–128. The [independent review](nonsingular-hamiltonian-jet-review-sol56-20261030T2300Z.md)
checks all seven claims and finds no material gap. The candidate's original
UNREVIEWED label records its historical state; this integration records the
completed review. Novelty has not been established, and no formal verification
or general impossibility result for global approaches is claimed.

## Statement

There is a fixed nonsingular P in R=C[x,y] and polynomials Q_n, n>=0,
such that every Q_n is nonsingular, {P,Q_n} tends to 1 at a single fixed
divisorial infinity valuation, but no polynomial Q satisfies {P,Q}=1.
At that valuation each pair has primitive source and target raw log discrepancy
-1, normal index e=1 and residue-field degree f=2. Here raw log discrepancy
means 1 plus the order of the specified rational volume form at the divisor.
The full source and target associated graded rings are smooth symplectic rings,
independent of n in the explicit presentation below. The target polynomial
subalgebra is not Poisson-closed before grading, for any n.

Thus the nonzero unit class in R/D_P(R) is invisible to this valuation topology:
D_P(R) is not closed. This does not exclude full-coefficient/global methods.

## The fixed polynomial and the exact obstruction

Put w=x^2*y^5, z=w-1, and P=x-x^3*y^5=x(1-w).
Since P_y=-5*x^3*y^4 and P_x=1-3w, the gradient of P never vanishes.
Give x weight5 and y weight-2. Then P has weight5 and D_P raises weight by2.
If D_P Q=1, the weight-2 component of Q also maps to1.
Every weight-2 polynomial is y H(w), H in C[w]:
5i-2j=-2 with i,j>=0 implies i=2k,j=5k+1.
Direct differentiation gives

    D_P(y H(w)) = L(H) := (1-3w)H + 5w(1-w)H'.

If H has degree d>=0 and leading coefficient h_d!=0, L(H) has leading
coefficient -(5d+3)h_d at w^(d+1). It cannot equal1. H=0 also fails.
Therefore 1 is not in D_P(R), without a genus or topological premise.

## Polynomial approximants

Define a_0=-1/2 and, for k>=1,

    a_k = -(5k-2)/(5k+2) * a_(k-1),
    G_n(w) = sum_(k=0)^n a_k (w-1)^k,
    Q_n = y G_n(w),       c_n=(5n+3)a_n.

In the coordinate z=w-1, L=(-2-3z)-5z(1+z)d/dz.
The recurrence cancels every coefficient of z^k,1<=k<=n, and hence

    {P,Q_n} = L(G_n) = 1-c_n (w-1)^(n+1),       c_n!=0.             (1)

The Jacobian is nonconstant for every n; these are not Keller pairs.

## Nonsingularity of every Q_n

Write b_k=(-1)^(k+1)*2a_k. Then b_0=1 and
b_k/b_(k-1)=(5k-2)/(5k+2) lies strictly between0 and1.
Let h_n(s)=sum_(k=0)^n b_k s^k, so G_n(w)=-h_n(1-w)/2.
The identity

    (1-s)h_n(s)=b_0-sum_(k=1)^n(b_(k-1)-b_k)s^k-b_n s^(n+1)

and the strict triangle inequality show h_n(s)!=0 for |s|<1:
the positive coefficients on the right after b_0 sum to b_0,
while all their powers of |s| are strictly less than1.
Also G_n(0)=-h_n(1)/2<0.
Now |c_0|=3/2 and |c_(n+1)|/|c_n|=(5n+8)/(5n+7)>1.
If G_n and G_n' shared a zero, (1) would imply
|w-1|=|c_n|^(-1/(n+1))<1, contradicting the preceding bound.
Finally (Q_n)_x=2xy^6 G_n'(w), (Q_n)_y=G_n(w)+5wG_n'(w).
For x=0 or y=0 the latter equals G_n(0)!=0; otherwise a common
gradient zero would require G_n=G_n'=0. Thus Q_n is nonsingular for all n.

## One fixed primitive infinity valuation

Set u=xy^3 and t=(w-1)/u^2. These are rational coordinates on C(x,y), since

    w=1+u^2 t,    x=w^3/u^5,    y=u^2/w.

Take v=ord_u with t transcendental in the residue field. This is a primitive
divisorial valuation, with v(x)=-5,v(y)=2,v(z)=2. Direct substitution gives

    dx wedge dy = -w/u^2 du wedge dt,
    P=-t w^3/u^3,       Q_n=u^2 G_n(w)/w.

Consequently v(P)=-3,v(Q_n)=2 and v({P,Q_n}-1)=2(n+1).
The source volume has order-2 and raw log discrepancy-1.
Use full target-field coordinates a=1/(P Q_n), b=P^2 Q_n^3.
Their inverse relations are P=1/(a^3 b), Q_n=a^2 b; thus no target subfield
is substituted for C(P,Q_n). We have v(a)=1,v(b)=0, residue(b)=-t^2/8.
The restricted target valuation is a-adic, with residue field C(-t^2/8),
because that residue is transcendental. Therefore e=1 and f=2.
For abstract target coordinates U,V, the same change of variables gives

    dU wedge dV = -1/(a^2 b) da wedge db.

The target raw log discrepancy is also-1. The valuation is fixed for all n.

## Full graded rings and the missing filtered compatibility

Let r=in_v(u), of degree1, and s=in_v(x^2 y^4 z), of degree0.
The latter polynomial equals w^2 t in the chart. Also xy^2=w/u gives r^-1.
Every polynomial in x,y has a Laurent u expansion with polynomial coefficients
in t, since w=1+u^2t has constant term1. It follows in both directions that

    gr_v R = C[r,r^-1,s],       {r,s}=-r^2.

The bracket raises the sum of degrees by1; this follows from the displayed
volume form. Its bivector is invertible on this Laurent polynomial ring.
The initial forms p=in_v(P)=-s r^-3 and q=in_v(Q_n)=-r^2/2 are algebraically
independent. Hence leading terms of distinct weight-homogeneous expressions
cannot cancel, and for A_n=C[P,Q_n] with its induced filtration,

    gr_v A_n = C[p,q],         {p,q}=1.

This bracket is the restriction of the ambient graded bracket.
It is not a Poisson bracket induced from a Poisson-closed filtered A_n.
Indeed, fix any q_0!=0. On x=0 choose y=q_0/G_n(0). Then (P,Q_n)=(0,q_0)
and the Jacobian equals G_n(0)<0. On w=1 choose y=-2q_0 and any complex
root x of x^2 y^5=1. Again (P,Q_n)=(0,q_0), but the Jacobian is1.
Thus {P,Q_n} is not in A_n, for every n.

## Scope and verification

Equation(1) puts1 in the closure of the linear subspace D_P(R) for the
valuation topology with neighborhoods {r:v(r)>=m}, while the weight proof
shows1 is not in that subspace. This topology is not asserted to be an ideal-adic
topology on R. No fixed-degree bound, full filtered compatibility, polynomial
no-fold theorem, or statement about an actual Keller counterexample follows.


## Reproducible checks and provenance

The [portable check](../box/nonsingular-components-infinity-jets-20261030/check.py) verifies exactly n=0,1,2 and
ten displayed identities. Its [recorded output](../box/nonsingular-components-infinity-jets-20261030/check-result.json)
is PASS. These finite checks supplement the all-n written proof; they do not prove
the universal claims. Only the output destination changed from the author's
check, and all scientific output fields agree exactly.

The [evidence guide](../box/nonsingular-components-infinity-jets-20261030/README.md) contains commands and scope;
[input pins](../box/nonsingular-components-infinity-jets-20261030/SCIENTIFIC-INPUTS.json) preserve exact source hashes.
No new OPEN entry is raised. The collision gate's EMPTY result only reports that
fact; it is not a literature novelty check.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7571`.
- Body SHA-256:
  `ee050a766deaad261397549aa44b4161db0488624630ece36703f4a38a0b80a2`.
- Frozen basis: `f5926b84f588e6dbac090a51d4bc84dd2b6d436f`.
