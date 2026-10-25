# LOGTENSOR1940 — actual finite/proper comparison
Status: GAP / EXACT SIGN OBSTRUCTION. Internal primary co-research, not independent review.
Launch/output basis: 9f790cee322baee72808ab3e680926a4b787e940.
Public frozen basis: 378addbd9bc3fc040d7c2bfdf0e2ee1ce040e145.
No proof or counterexample of JC2; no promotion, novelty claim or automatic successor.

## Question and admitted scope
Does the actual finite h / proper birational k correspondence force a logarithmic tensor?
Use the pinned adopted normal projective rational target Y, U=A2, boundary B, singular point q.
K_Y=-B, Cl(Y)=Z[B], Pic(Y)=Z[L], L=nB ample, L.B=1, B²=1/n.
The actual correspondence has finite h:W→Y of degree e>1 and proper birational k:W→Y.
h*B=eC, k*B=C+Z, and h*Omega=k*Omega; W and Y have rational singularities.
The k-exceptional centres are contained in {p0,q}; p0 is a smooth boundary point.
These are admitted attachment/projectivity/boundary inputs, not claims about arbitrary compactifications.
All new sheaf comparisons below are manual internal deductions and remain subject to review.

## The closing consumer and what stability would mean
Let E be the rank-two reflexive logarithmic cotangent sheaf, agreeing with Omega^1(log B) off q.
One coherent construction is the dual/reflexive hull of logarithmic derivations preserving I_B.
Its determinant is O_Y(K_Y+B)=O_Y as a reflexive rank-one sheaf.
For m≥1 let V_m=H0(Y,Sym^[m]E), using the reflexive symmetric power.
At generic B, the actual logarithmic differential has invertible leading matrix diag(e,sigma').
Consequently logarithmic tensor order scales by e, including for each symmetric power.
Pullback preserves V_m and is injective; V_m is finite-dimensional because Y is projective.
A nonzero eigenvector over C determines an invariant reduced finite algebraic web on U.
The already accepted Sep20 finite-web consumer excludes a noninvertible Keller map in this case.
We do not reprove that consumer or identify an exterior tensor with a symmetric tensor.
Under a hypothetical attached counterexample, all V_m must therefore vanish.

For m=1, a logarithmic polynomial one-form lambda has d lambda=c Omega: its coefficient
is polynomial and has nonpositive semidegree, hence is constant.
If c=0, polynomial de Rham exactness gives lambda=dH; every nonconstant H has
logarithmic differential order delta(H)>0, so lambda=0. Thus dim H0(E)≤1.
A nonzero section is precisely a logarithmic primitive up to scalar, recovering the same old gap.
A saturated rank-one subsheaf M⊂E with nonnegative L-slope has M**=O_Y(jB), j≥0.
Its inclusion extends reflexively; the effective section of O_Y(jB) gives a nonzero section of E.
Thus H0(E)=0 implies E is mu_L-stable of slope zero on this class-group package.
The missing implication is actual correspondence ⇒ failure of this stability or some V_m≠0.

## Actual relative lattices, with simultaneous frames
Set A=h^{[*]}E=(h*E/torsion)** on W and identify it rationally by dh.
Since h is finite, codimension-one points map to codimension-one points where E is locally free.
Abstractly det A=O_W; its differential image has rational determinant h*Omega=k*Omega.
Let D be a generic k-exceptional prime over smooth p0, and r its h-ramification index.
At the generic affine h-image use simultaneous DVR coordinates h*s=u^r times a unit, h*t=z.
The ambient differential lattice A has Smith orders (0,r-1).
The logarithmic normal generator for k has a genuine du/u term, because ord_D(k*B)>0.
Its coefficient in the h*ds direction has order -r; no coefficient is more negative.
The equality of pulled volume forms gives total relative determinant order zero.
The relative Smith orders are therefore (-r,r), not a one-sided lattice inclusion.
This conclusion uses simultaneous frames and the actual determinant equality, not subtraction
of two independently diagonalized Smith lists. It is not a new local-map family.

At q, E need not be locally free. The image ideal of wedge²E→det E=O_Y is an ideal I_q
supported at q. Along a divisor over q its pulled determinant has order d_D≥0.
Thus k^{[*]}E can have relative determinant order d_D against A, rather than zero.
These terms, and further cusp terms on a resolution, cannot be discarded as étale corrections.
No smooth/log-smooth/orbifold Chern identity at q is assumed here.

## Global finite/proper comparison and its decisive sign
Over U, k is an isomorphism and F is étale, so k_*A=E there.
At generic B, the logarithmic pullback is an isomorphism of lattices (e is a unit).
Reflexive extension across the two exceptional centres therefore gives a canonical inclusion
k_*A⊂E, with (k_*A)**=E. Define Q=E/k_*A.
Q has finite length supported in {p0,q}; R1 k_*A also has finite length there.
Higher direct images vanish in degrees ≥2 because fibres have dimension at most one.
The exact Euler identity is
    chi(Y,E) - chi(W,A) = length(Q) + length(R1 k_*A) ≥ 0.             (1)
Both terms are retained: Q records extension failure, R1 records fibre cohomology.
This identity applies to the reflexive sheaves specified above, not a chosen smooth replacement.

In the hypothetical counterexample H0(E)=0 and E is stable of slope zero.
Serre duality gives H2(E)=Hom(E,omega_Y)*=0: a nonzero map E→O_Y(-B)
would have rank-one kernel of positive slope, contradicting stability.
The inclusion k_*A⊂E immediately gives H0(W,A)=0, without a norm construction.
The sequence 0→k_*A→E→Q→0 and Leray then give H2(W,A)=0 and the sharper identity
    h1(W,A) - h1(Y,E) = length(Q) + length(R1 k_*A) ≥ 0.             (2)
Thus the actual correspondence accommodates the defects by growing H1.
It supplies no contradiction to stable E and no nonzero global section.
This is a failure certificate for this comparison, not a no-go theorem for all stability arguments.

For transparent Chern bookkeeping define gamma_Y=2 chi(O_Y)-chi(E),
gamma_W=2 chi(O_W)-chi(A). Rationality gives both structure-sheaf Euler characteristics 1.
Hence gamma_Y=2+h1(E)≥2 and gamma_W-gamma_Y=length(Q)+length(R1 k_*A).
Define the unknown finite-pullback defect epsilon_h=gamma_W-e gamma_Y. Exactly,
    (e-1) gamma_Y + epsilon_h = length(Q)+length(R1 k_*A).           (3)
These gamma quantities are corrected Euler quantities, not asserted orbifold c2 invariants.
Even imposing the unjustified epsilon_h=0 leaves a compatible positive right-hand side.
In a smooth locally free determinant-zero specialization gamma=c2 by Riemann–Roch;
the sign is c2(A)-c2(E)≥0, accommodating positive (e-1)c2(E), not contradicting it.
No bound on epsilon_h, the two lengths, or a common resolution has been established.

## Polarizations are genuinely different
H=h*L=enC is ample; K=k*L=n(C+Z) is nef, with K=H/e+nZ.
For any divisor class D where the intersection is defined, D.H=e D.K-en D.Z.
A k-exceptional curve has K-degree zero but positive H-degree.
Together with the two-sided relative lattice changes, this prevents automatic slope transfer.
Neither equal determinant nor finite pullback authorizes replacing H by K in a stability argument.
The exact identities (1)–(3) already keep the singular contributions without that replacement.

## One authorized fixed static discriminator, without h/k
This is the single ROOT-supplied deformation, not a new family or actual Keller counterexample.
Put w=x²-y⁵-y² and use weights delta(x)=5, delta(y)=2, delta(w)=3.
The normal form C[y,w]⊕x C[y,w] gives gr R=C[X,Y,W]/(X²-Y⁵), a domain.
Every nonconstant polynomial has positive delta at least 2; none has delta 1.
A generic boundary expansion is y=t^-2, x=t^-5+(1/2)t+xi t²+…,
with w=2xi t^-3+… and Omega leading 2(dt/t) wedge dxi.
The primitive lambda_E=(5x dy-2y dx)/7 has leading term -(6/7)t^-1 dt/t,
followed by -2xi dt/t-(2/7)dxi. Its logarithmic pole order is exactly 1.
Every other polynomial primitive differs by dH; a nonconstant dH has order delta(H)≥2.
It cannot cancel this order-one pole. There is no logarithmic polynomial primitive.
The same closed-form argument above shows H0(E)=0 whenever this filtration is realized below.

Here the realization and singularity checks can be made directly, without a deformation theorem.
Let S=C[X,Y,W,T]/(X²-Y⁵-Y²T⁶-WT⁷), with weights (5,2,3,1), and Y=Proj S.
The normal form identifies S with the Rees ring; B is T=0 and the chart T≠0 is whole A2.
The relation is primitive and linear in W, hence defines a domain. S is a hypersurface, so CM.
Its affine singular locus is X=Y=T=0, of codimension two in the three-dimensional cone.
The Jacobian criterion and S2 therefore give normality. Y is a normal projective rational surface.
Away from the W-axis the boundary has X,Y nonzero, stabilizer trivial (gcd(5,2)=1),
and nonzero X-derivative, so Y is smooth there; its only possible singular point is q on that axis.
The boundary normalization is P(1,3)=P1. At q, C[z²,z⁵] has residual mu3 action z→zeta z;
its invariants are C[z6,z9]=C[u²,u³], u=z³. Thus B is the ordinary rational cusp.
On the W-chart the index cover is x²-y⁵-y²t⁶-t⁷=0 with mu3 weights (2,2,1).
The action is free off its origin. The boundary equation t has character 1.
If mB is Cartier, its pulled local equation is t^m times a unit. A semi-invariant unit
at the fixed origin has trivial character, so 3 divides m. Conversely t³ descends.
Thus B has exact local/global Cartier index 3; elsewhere B is Cartier.
Cl(Y)=Z[B] follows from U=A2 and its constant units; Pic(Y)=Z[3B].
L=3B is ample (a positive Cartier grading sheaf). On the boundary normalization it has degree 1,
as its third Veronese is C[z³,W]; hence L.B=1 and B²=1/3.
The expansion of Omega and regularity on U give div(Omega)=-B.
The dualizing reflexive sheaf is therefore omega_Y=O_Y(-B)=I_B; no weighted adjunction is needed.
Serre duality gives H2(O_Y)=H0(I_B)*=0, since global projective regular functions are constant.
For a projective resolution pi:X→Y, X is a smooth projective rational surface, so H1(O_X)=H2(O_X)=0.
Normality gives pi_*O_X=O_Y; R1 pi_*O_X is supported at the isolated singularities and R2=0.
Leray identifies H0(R1 pi_*O_X) with H2(O_Y)=0. Thus R1 pi_*O_X=0: Y has rational singularities.
These checks give a static adopted-type ample index-three target with H0(E)=0 and stable E.
They do not supply h, k, a degree-e eigenmap, or vanishing of all higher symmetric tensors.
The static discriminator is subordinate to (1)–(3); it cannot refute the actual-map premise.

## Disposition, custody and reading limits
The hoped-for implication fails at the sign: finite/proper Euler comparison allows increasing H1
and exceptional defects. No additional actual constraint forces their opposite sign or bounds them.
The closing web consumer remains available; existence of a symmetric logarithmic tensor is unproved.
No new OPEN is raised; this is a precise failure certificate within the existing existence question.
Fresh43-input physical/hash/bytes/LF gates and eleven selection/launch archive comparisons passed.
Frozen STATE306 was personally read whole before mathematics; own earlier readings were reused
only after equality. Detailed windows, scope limits and errors are in the companion coverage receipt.
Two separately hashed ROOT addenda were read without changing the launch registry.
The early append-only partial precedes synthesis; canonical final custody is separate.
No external source, history query, CAS, child, paid lane, Git mutation or public edit was used.
The stopped 2609.18798v1 source and all old scientific/ownership stops remain in force.
OPEN(S) RAISED
None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `378addbd9bc3fc040d7c2bfdf0e2ee1ce040e145` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11781`.
- Body SHA-256:
  `8d7c310feee315100b405290a57a15286143111c914318a648e8e38ad7a06cde`.
- Frozen basis: `9f790cee322baee72808ab3e680926a4b787e940`.
