# Constant graphs: an Euler identity is not a polynomial-pair certificate

ROOT manual control, September12,2026. UNREVIEWED, no promotion or JC2
claim. First publication action01:45:18; reserve01:50/HARD01:53 set now.
No scientific execution. Complete proof and exact non-conclusion below.

## Identity and integrability boundary

Over C define

    P=(1+xy)^3z+y^2(1+xy)(4+3xy),
    Q=y+3x(1+xy)^2z+3xy^2(4+3xy),
    R=2x-3x^2y-x^3z.

For a graph z=H(x,y) let p,q,r be their restrictions and
J(f,g)=f_xg_y-f_yg_x. The exact identity is

    2p J(q,r)-q J(p,r)-r J(p,q)
        = -2(2H+x H_x-y H_y).                         (1)

Manual verification avoids bulk expansion. On x!=0 put t=1/x,
s=y+t and rho=R. Solving for z gives z=5t^2-3st-rho*t^3.
Direct substitution gives

    P=s^2+st-rho*s^3,
    Q=4s+2t-3rho*s^2,
    R=rho.

Their Jacobian in(s,t,rho) is
2(2s+t-3rho*s^2)-s(4-6rho*s)=2t.
The Jacobian of(s,t,rho) in(x,y,z) is -1/t: the first two
rows have 2x2 determinant t^2 and rho_z=-x^3. The ambient
determinant is therefore -2 on x!=0, hence as a polynomial identity
everywhere. No ambient invertibility or counterexample conclusion is used.

The vector field E=-x partial_x+y partial_y+2z partial_z sends
(P,Q,R) to(2P,Q,-R), by their literal weighted homogeneity. Contracting
dP wedge dQ wedge dR=-2 dx wedge dy wedge dz with E gives

    2P dQ wedge dR-Q dP wedge dR-R dP wedge dQ
       =-2(-x dy wedge dz-y dx wedge dz+2z dx wedge dy).

Pull back by the graph, using dz=H_x dx+H_y dy. The coefficient on
the right is -2(xH_x-yH_y+2H), proving(1) with graph derivatives kept.

In particular, H=c+y^2 h(xy), h any polynomial and c!=0, has
2H+xH_x-yH_y=2c. Thus, for B=C[p,q,r] inside C[x,y],

    1=(r/(4c)) J(p,q)+(q/(4c)) J(p,r)-(p/(2c)) J(q,r).  (2)

This proves 1 belongs to the full B-Jacobian module. At H=1 and
the source origin, (p,q,r)=(1,0,0), J(q,r)=-2, and the other
two terms have zero coefficient, so(2) gives1 with the correct sign.
At c=0, (1) instead gives0, consistent with the homogeneous module
obstruction. No limit as c->0 is an argument about c!=0.

Membership is not a pair certificate. In independent target variables
(U,V,W), the exact coefficient recipe in(2) is the two-form

    beta=(W/(4c)) dU wedge dV+(V/(4c)) dU wedge dW
                           -(U/(2c)) dV wedge dW.

Its exterior derivative is

    d beta=(1/(4c)-1/(4c)-1/(2c)) dU wedge dV wedge dW
          =-1/(2c) dU wedge dV wedge dW != 0.

Hence there are NO polynomial F,G in three independent target variables
whose dF wedge dG equals this exact beta: such a form is always closed.
Although beta pulls back to dx wedge dy on the graph, this supplies
neither F nor G. Importantly, it does NOT rule out a different form
dF wedge dG with the SAME pullback: a correction lying in the kernel
of graph pullback could change the ambient derivative. No assertion
that all such corrections fail is made. No Keller pair, source point
or theorem excluding pairs on H=1 has been obtained.

This is an independent scope control, not a descendant using the new
GRAPH-WEDGE-1 theorem. That accepted theorem concerns H=y^2 K(xy,y),
whereas nonzero constant perturbations lie outside its wedge. The
explicit display alone supplies this proof. Root's original guidance
was frozen at box/constant-graph-subalgebra-control-astra-20260912/
DELTA-root-euler.md SHA
cba255f67d50fe19064e683dbaa7b43ed615ac465314a1b2fce5420b591254a9;
An Astra check of(1)/(2) was separately assigned; its body has not been
read or assumed here. Its terminal announcement arrived during authoring.
The closedness observation above was not part of that task input.

QUANTITY: explicit module membership and whether its displayed target
two-form is dF wedge dG. Answers YES and NO respectively, manually,
UNREVIEWED. CHEAPEST TEST: chart determinant, Euler contraction and one
exterior derivative; no scientific execution needed. The broader pair
existence question remains undecided, with no new canonical OPEN,
automatic integrability search, review loop or compute successor selected.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4075`.
- Body SHA-256:
  `fd3ca5de1d9fa58c56ad514a177f59536e2ec7109b7583748aa9f114df0994f1`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
