# D125 marked component: exact submersion discriminator

2026-09-08. **NO-GAIN for exclusion of the full source.** The exact embedded punctured curve occurs in a polynomial submersion. Its prescribed normal cofactor does yield a short obstruction when that cofactor has u-degree at most1, but the licensed source has u-degree14. This missing degree restriction cannot be supplied by the embedding alone. The result uses accepted14c and the terminal marked-fiber calculation, independently of all finite-boundary proofs.

## Exact marked data and a stronger negative control

Over a characteristic-zero field K, set q=1+v² and N=uv⁵−q. The marked data are

    P=N M,  M|C=k v⁻³,  Q|C=d/v,
    C=(N=0),  k!=0,  d=5k²/9,  J(P,Q)=−kd.

C is closed and smooth, with coordinate ring K[v,v⁻¹] and u=v⁻³+v⁻⁵. Nevertheless the polynomial

    P_plus=vN=uv⁶−v³−v

is a submersion: its u derivative is v⁶, and at v=0 its v derivative is −1. Thus **this precise C and its pole orders**, not just an abstract G_m, occur as a reduced fiber component of a nonsingular polynomial. Its other component is the disjoint line v=0. Its cofactor is v, not kv⁻³; it is not a full marked-source or Keller-pair counterexample. The required general control x(xy−1) has derivatives x² and2xy−1 and is likewise nonsingular. Neither control authorizes discarding the specific cofactor condition.

There is no first-order contradiction on C. Since N_u=v⁵ and N_v|C=3v+5/v,

    P_u|C=kv²,  P_v|C=k(3v⁻²+5v⁻⁴),
    J(P,Q)|C=P_u|C * (d/dv)(Q|C)=−kd.

The normal and tangential restrictions reproduce the required constant and sign exactly.

## A genuine but insufficient low-degree obstruction

Suppose deg_u M<=1, and write M=a(v)u+b(v). Restriction to C gives

    a q+b v⁵=k v².

As q is a unit modulo v⁵, all polynomial solutions are

    a=k(v²−v⁴)+v⁵h(v),  b=kv−q h(v).

As a quadratic in u, P has coefficients A=v⁵a, B=v⁵b−qa, D=−qb. Its discriminant is

    B²−4AD=(v⁵b+qa)²=k²v⁴.

For v a unit with a(v)!=0, its u-critical value is therefore

    P(−B/(2A),v)=−k²/(4 H(v)),
    H(v)=va(v)=k(v³−v⁵)+v⁶h(v).

H has a root of multiplicity exactly3 at0 and a nonzero v⁵ coefficient, so it is not a monomial. Over Kbar it has r>=2 distinct roots. If deg H=D0, the roots of H account for D0−r of the D0−1 zeros of H', counting multiplicities. Consequently some v0 satisfies H'(v0)=0 and H(v0)!=0. At the corresponding u-critical point both derivatives of P vanish: differentiating its critical-value function has no u-derivative contribution. Hence **no such P can have a constant nonzero Jacobian mate**. This argument is over the algebraic closure and proves geometric failure even if no critical point is K-rational.

For h=0,k=1 an exact control is v²=3/5, uv=35/36; both derivatives vanish. The proof is universal in h; two exact h fixtures and this field-valued critical point are controls, not a numerical or finite-sampling proof.

The actual source lies outside the proved range. Receiver total degree15 bounds physical u-degree by15, and its monic pi¹⁵ term gives [u¹⁵]P=v⁶⁰. Thus deg_u M=14. More explicitly, put

    M0=v+uv²−uv⁴,  w=uv⁴−v.

Because M0|C=v⁻³, w|C=v⁻¹ and the restriction kernel is the prime ideal(N), **all** polynomial extensions of the marked restrictions are exactly

    M=k M0+N H(u,v),  Q=d w+N T(u,v).

The low-degree theorem covers H=h(v), whereas the source allows deg_u H=13. No condition here removes those higher-u terms or solves the full Jacobian equations for H,T. This is the first explicit missing arrow.

## Rational straightening does not repair the gap

The root-suggested chart x=N/v³, y=v⁻¹ has Jacobian −1 and inverse

    u=xy²+y³+y⁵,  v=y⁻¹.

It identifies the marked curve with x=0,y!=0. The transformed restrictions are P(0,y)=0, P_x(0,y)=k and Q(0,y)=dy. These are Laurent-polynomial identities in K[x,y,y⁻¹], not polynomial identities extending across y=0. An arbitrary original polynomial can have a pole there (v itself becomes y⁻¹). No source affine line or global polynomial symplectic change has been constructed. The previously checked affine-line injectivity theorem remains inapplicable.

## Reading, evidence and stop

The accepted14c, terminal marked-fiber and terminal torsor reports were read wholly. Named history checks in APPROACHES, ladder/REDUCTION and these reports found no already charged version of the low-u discriminant argument; this is not an exhaustive novelty claim. The earlier marked-fiber report already records the exact primary affine-line/generic-fiber mismatches. Targeted discovery of C* embedding/submersion literature returned rational-whole-fibration or embedding-classification interfaces; no new primary theorem or unexamined proof was imported. This report's new statements are the elementary identities and derivative argument above, not a literature-wide nonexistence assertion.

Eight capped standard-library runs pass, normal and−O, with zero Assert nodes and actual changed-cofactor, changed-Q-sign and changed-critical-point failures. The final witness is byte-identical across modes. A preterminal parity mistake in the critical-point test was corrected before these final runs; no claimed mathematical identity was changed. Inputs, code, final replay and report/transaction are pinned by owned custody. No actual degree15/25 pair expansion, CAS, AWS, solver, live peer, shared edit or pending theorem was used. **STOP: exact higher-u cofactor control remains absent; no marked-family exclusion, point, ideal decision, degeneration assertion or faster solver claim. All writers idle at final custody publication.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5760`.
- Body SHA-256:
  `f1559ba5e98efeee6aecf8811d9fc962a0e7d99c13c2f283a706b4a403f0ca7e`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
