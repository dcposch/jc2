# VOLUMEREVIEW0520 — independent numerical-volume audit

Status: PASS / INTERNAL / MANUAL / INDEPENDENT REVIEW.
Launch basis: c733c94940852bfd622b90ab0cbc36f490c2412c.
Public basis: c3a384e1ce42e65fcbbe26ee711e84be6f05cb23.

## Verdict and exact scope

For the defined numerical-resolution quantity, at the adopted DIVISORIAL scope with q
the only singular point of Y,

    e V_Y(q) <= V_W(p) <= V_Y(q)+E_mat,    V_Y(q)>0.              (A)

The definition, model independence, finite lower comparison, and actual k-matrix upper
majorant are sound. E_mat is an explicit charge on one simultaneous resolution; it is
not identified with an external volume invariant and has no independently asserted sign.
The estimate needed to contradict the sheet budget remains unproved. Equation (3) in the
producer is one stronger sufficient proposal, not a necessary closing condition.

## Numerical nef envelope

On an SNC resolution rho:X->T, numerical pullback of a Weil divisor is well-defined by
the invertible negative-definite exceptional matrix; no Cartierness of R is used. For the
exceptional log vector L, the set of exceptional nef vectors P<=L is nonempty, bounded,
and closed under componentwise maximum. The sign pattern M_off>=0, M^-1<=0 proves these
claims and gives a unique componentwise maximal P. Complementarity gives

    N=L-P>=0,    P.N=0,    V(T,o;D)=-P^2>=0.

If Q<=P are exceptional nef vectors, then
(P^2-Q^2)=(MP+MQ).(P-Q)>=0; hence -P^2<=-Q^2. This is the order/energy
direction used in both comparisons.

Under a point blowup of an SNC boundary centre meeting a components, a<=2,

    L_new=sigma*L+(2-a)F.

The pullback P_new=sigma*P and N_new=sigma*N+(2-a)F retain nefness, effectivity and
orthogonality. Maximality then gives invariance; common refinements give model independence.
No external volume theorem is invoked.

## Positivity on the exact target

Because K_Y+B=0, L_Y=K_X+B'+E on the resolution over q. The exact hypotheses matter:
B' is P1, q is the only ambient singularity, and the unibranch embedded resolution makes
B' meet the reduced exceptional divisor once. Adjunction yields L_Y.B'=-1. Since L_Y is
exceptional, it has a negative coefficient; zero is not an admissible vector below L_Y,
so the maximal nef part P_Y is nonzero. Negative definiteness gives V_Y=-P_Y^2>0.
This argument is not transferred to a weakened target with another singularity on B.

## Finite lower comparison

The restricted finite inverse image of q has the single point p because h^-1(B)=C and
h_C is an isomorphism. On compatible resolutions g:Z->X of degree e, logarithmic
ramification cancels along target exceptional divisors and along strict C. Restoring the
strict ramification divisor before subtracting the numerical pullback gives

    L_W=g*L_Y+T-E_R,    E_R>=0,    g_*T=0,
    g_*L_W=eL_Y-g_*E_R<=eL_Y.                                    (B)

Effectivity of E_R follows from -M_rho^-1 applied to the nonnegative intersections of
the effective strict transform R_strict with distinct exceptional curves. This does not
assume R Cartier.

For source maximal P_W, put Q=g_*P_W/e. Projection against pullbacks of target exceptional
curves shows Q is target-nef; (B) gives Q<=L_Y, hence Q<=P_Y. Write
P_W=g*Q+K with g_*K=0. Projection gives K.g*Q=0 and (g*Q)^2=eQ^2, while the source
exceptional lattice gives K^2<=0. Therefore

    V_W=e(-Q^2)-K^2 >= e(-Q^2) >= eV_Y.

Every support statement here is localized over p/q; no infinitely-singular transfer occurs.

## Actual k-block majorant

On a common model over q split the k-exceptional lattice into all source-resolution
blocks A over every point of k^-1(q), and strict omitted curves T centred at q. With
G=-M_AA^-1 M_AT>=0, the exact source vector is

    L_source,A=L_A-GR_T.

For target decomposition L=P+N, each T coefficient of N is r_i-P_i>0. Orthogonality
and nefness force P.E_i=0. Set eta=P_A-GP_T and J=(GP_T,P_T). Then J is the numerical
pullback of P_T, eta.J=0, eta is source-nef, and

    -eta^2=V_Y+J^2<=V_Y,
    L_source,A-eta=N_A-G(R_T-P_T).                                (C)

No sign is silently assigned to the final vector in (C).

Let d=[G(R_T-P_T)-N_A]_+, v=[-M_AA d]_+, and u=-M_AA^-1v. The matrix signs give
u>=d>=0 and M_AA u=-v<=0. Thus eta-u is source-nef and eta-u<=L_source,A. Energy
monotonicity on every A-block yields

    V_W(p) <= V_source,total <= -(eta-u)^2
             =V_Y+J^2+2 eta.u-u^2 = V_Y+E_mat.                   (D)

The first inequality is only nonnegativity of the other local volumes. It is not equality;
the construction correctly includes every block over k^-1(q), not only the cusp block.

## Missing comparison and actual intersection data

Combining (A) makes E_mat>=(e-1)V_Y necessary. A sufficient contradiction would follow
from the weaker comparison clarified in the result receipt,

    E_mat <= (sum_i r_i delta_i-1)V_Y,

because the accepted sheet budget has sum_i r_i delta_i<=e-1<e. The producer's equation
(3), with sum_i(r_i-1)delta_i, is stronger and also sufficient, but remains unproved.
Failure to prove it is not a no-go theorem for the weaker comparison.

The ample-C/class-group identities

    sum_i z_i delta_i d_i=e-1,    S z_T=-(C.E_i)_T<0

are valid on the actual compact model. They involve z_i,d_i, whereas E_mat depends on
G,P_T,N_A and the exceptional quadratic form. No supplied implication controls the latter
by the sheet weights. The old LOGVOLUME control remains k-only and does not refute (A).

## Custody and limits

ACK: 2026-10-26T05:18:39.957945Z. Whole launch STATE353 completed
2026-10-26T05:18:55.442079Z and matched launch STATE. All30 fixed inputs passed before
mathematics. VOLUMESHEET91 was canonically verified and read whole; result96--103 was read
as the mandatory scope clarification. Accepted sheet/logarithmic dependencies were used
only at their pinned scopes, not re-audited.

No history/source/web query, CAS, paid/CLI/cloud action, child, protected-tree access,
shared/public/Git edit, replacement model, missing-bound design, promotion or successor
occurred. Exact personal windows, own reuse evidence, postpins, read charge and collision
custody are in companion receipts.

OPEN(S) RAISED
None. The weighted comparison is the already explicit retained gap.

## COLLISIONS
Terminal frozen-public collision custody is recorded separately after sealing.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6361`.
- Body SHA-256:
  `f93a68dc65f2b2b87e4b38c08f634c9a89434886ea2d2864e0991265ab26a95c`.
- Frozen basis: `c733c94940852bfd622b90ab0cbc36f490c2412c`.
