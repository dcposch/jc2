Current-band ranks after both complete boundaries
================================================

All counts below are counts of generators after rational graph pivots, not
dimensions. Nonpivot compatibility equations in previously introduced
coordinates remain equations. The matrices do not decide those equations.

Put F=sum x^(n-r)F_r(w), G=sum x^(m-r)G_r(w), w=y/x. For homogeneous inputs
J(x^N f(w),x^M g(w))=x^(N+M-2)(N*f*g'-M*f'*g). Hence the current-block
linear map at depth r is exactly

    n*F_0*g'-(m-r)*F_0'*g+(n-r)*f*G_0'-m*f'*G_0.

The known lower terms move to a right-hand side B_r(w). The boundary-map
proof makes the current variation spaces

    f in w^L_F*(w-1)^M_F Q[w]_(degree<d_F),
    g in w^L_G*(w-1)^M_G Q[w]_(degree<d_G).

The L,M include the equality-face rows, and d_F,d_G are the counts from
boundary_counts.json. This basis is related to the earlier retained-column
Hermite basis by a unit triangular polynomial matrix. No parameter is
specialized to obtain the current linear map.

Here F_0=P^3,G_0=P^2 with P=w^9(w-1)^24 for99 and P=w^8(w-1)^28 for108.
Writing f=(3/2)P*g+h, the linear map becomes

    P*(2*(n-r)*P'*h-m*P*h').

Thus every allowed g has the paired kernel vector ((3/2)P*g,g). The driver
checks the two boundary divisibilities for every such current space. The
remaining homogeneous equation has only h=constant*P^(3-r/(n/3)). A
polynomial solution exists precisely at r divisible by11 for99 or9 for108.
The possible radial solutions are respectively

    w^(27-3r/11)*(w-1)^(72-8r/11),
    w^(24-2r/9)*(w-1)^(84-7r/9).

They satisfy both current boundary conditions at every indicated depth.
There are9,9,12 radial directions over the three clients.

| Client | Boundary generators | Q pivots from J | Remaining generators |
|---|---:|---:|---:|
|99 delta2|482|327|155|
|99 delta5/2|219|145|74|
|108 free mean|365|243|122|

The per-band exact Q RREF replay agrees with the kernel proof. Removing the
same explicit nonzero polynomial factor from every matrix column reduces
the maximum row/column sizes to7/10,4/4,5/7. This is an injection of Q[w]
modules, not an inversion of a source parameter. For an actual right-hand
side it adds the necessary divisibility/remainder conditions; those may not
be dropped. All bands after r=n are pure compatibility equations, through
the constant-Jacobian depth163/178.

Add the complete characteristic family

    R=G^3-F^2+aG^2+bFG+cF+dG+e0.

Its current F/G linear part at ambient characteristic depth r is
P^3*(3P*g-2f). All depths r<=n lie strictly before the permitted actual R
degree, so these rows have zero target. Introduce b,a,c exactly when their
first terms appear, at r=k,2k,3k respectively, k=n/3. After dividing out
the displayed common P^3 their columns are P^2,P,1. Each can absorb its
corresponding radial direction; every other radial direction is killed by
an additional rational pivot. The exact joint matrices give:

| Client | Boundary F/G + b,a,c | Joint Q pivots | Remaining generators |
|---|---:|---:|---:|
|99 delta2|485|336|149|
|99 delta5/2|222|154|68|
|108 free mean|368|255|113|

The largest stacked matrices have14/10,8/4,10/7 rows/columns. Every current
F coefficient is a pivot; all G coefficients and b,a,c remain generators.
At r=4k the new scalar d has the monic column P^2 in the still-forbidden
degree2k, so introducing d and solving its leader contributes net zero
generators, with all other equations retained. The free constant e0 adds
one if retained; it enters no upper, face, or Jacobian row. Centres and
separation are additional scalar generators:3 for99 and4 for108 on the
licensed jet0=0 slice.

The three target transformations F->F+beta*G+gamma and G->G+alpha have to be
handled through the declared completion-of-square/depressed-cubic map. If
factored by that isomorphism they remove exactly three scalar factors from
the last column, leaving146/65/110, before centres and the R constant. In
particular an additional subtraction of one for G's constant would count
the same G translation twice. A further dimension reduction needs another
proved equation or a different explicitly declared coordinate factor.

Executable receipts are boundary_jacobian_ranks.py/.json and
boundary_joint_ranks.py/.json. They bind all matrices, pivots and kernel
counts, and explicitly label compatibility equations unevaluated. They
make no properness, nilpotence, or Keller realization claim.
