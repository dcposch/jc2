The optional accelerated computation at jet0=0 uses the second source
translation, with an explicit inverse. It is not promoted merely because a
coordinate slice gives a unit.

For any normalized polynomial K=t^D Q(t^-1,(z+1)/t), the simultaneous
translation Q_q(x,y)=Q(x+q,y+q) gives

    T_q K = (1+qt)^D K(t/(1+qt),z/(1+qt))
          = sum c_(r,p) t^r z^p (1+qt)^(D-r-p).

Every exponent D-r-p is a nonnegative integer in the actual full coefficient
box. The transformation is polynomial over Q[q], unit triangular by r, and
T_a T_b=T_(a+b); hence T_(-q) is its polynomial inverse. The coefficient
identity is mechanically checked for every normalization degree up to99 by
translation_controls.py. The source degree boxes and all y-degree remainder
bounds are preserved. Monic approximate roots commute with this translation
by uniqueness, and the displayed remainder identities are transported with
all their coefficients. There is no reset of an auxiliary variable.

The minor-root series of Q_q is the old series evaluated at x+q, minus q.
Its coordinates transform as

    jet0 -> jet0-q, u -> u,
    minor_a2 -> minor_a2-q*u  (delta2),
    v -> v-q*u               (delta52),
    rho -> rho, c -> c.

The generic coefficient at the selected splitting radius is unchanged;
all other terms induced by expanding (1+qt)^(-delta) are strictly above
that radius. The major direction and ordinary centre remain fixed because
the translation is diagonal. D2/D1 centres change only above their radii:
for example the D1 correction to its t^(1/3) y-centre begins at t^(4/3),
strictly above4/9. The full generic disc, every valuation and every leading
face therefore transport to the same labelled disc with the coordinates
shown above. Polynomial substitution of the generic variable by itself
plus terms of higher local order preserves all complete strict-below
coefficient ideals and leading-face differences.

Each source coefficient equation in the full chart is transported into the
corresponding complete coefficient ideal. This includes the canonical C2/C3
and all outer minor bounds, and the full D2/D1 systems. The Jacobian
satisfies J(Q_q,R_q)(x,y)=J(Q,R)(x+q,y+q), since the source translation has
determinant1. Once the positive-degree Jacobian coefficients vanish, its
scalar is unchanged, so a nonzero scalar remains nonzero.

Consequently the free-centre full chart X is isomorphic to
X_(jet0=0) x A1 by p -> (T_jet0(p),jet0), with inverse
(p0,j) -> T_(-j)(p0). This is an orbit decomposition of the entire chart,
including u=0, not division by u or a choice of one irreducible component.
Dimensions differ by1; a unit on the jet0=0 chart implies the free-centre
chart is empty. Conversely every point of the slice lifts to every desired
jet0, including the controls' value1.

The ledger assigns this operation only to the residual diagonal source
translation. The first translation already fixed the major ordinary centre.
No torus is spent; rho and c remain free and localized. minor_a2 or v is
transported, not fixed. Finally every nonconstant h3 term has positive
z-degree, while T_q leaves t^11 Hc_11_0 unchanged: h3(x,x)=Hc_11_0 is
translation invariant. The optional gauge engine explicitly retains it.
