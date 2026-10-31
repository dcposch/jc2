# A whole affine-plane chart does not by itself make its omitted line Cartier

Status: CANDIDATE / INTERNAL / MANUAL / UNREVIEWED. ROOT proposes one fixed falsifier of a coarse implication; no novelty or JC2 claim. No symbolic-computation or external-source proof is imported.

Let B=C[x,y,z]/(xy-z^2(z-1)), X=Spec B, and E=V(x,z). Define

    j:A2_(u,v) -> X,
    x=u, z=1+uv, y=v(1+uv)^2.

The defining relation follows from uv=z-1. The image is exactly U=X-E: on D(x) the inverse is u=x,v=(z-1)/x, and on D(z) it is u=x,v=y/z^2. These formulas agree because xy=z^2(z-1). D(x) union D(z)=X-E. The map j lands in that union since u=0 gives z=1. The two formulas directly compose to the identity in both directions. Thus U is the WHOLE affine plane, not a punctured chart. E=Spec C[y] is one scheme-smooth affine line.

The polynomial xy-z^2(z-1) is irreducible: it is primitive and linear in y over the UFD C[x,z], with relatively prime coefficients x and -z^2(z-1), and is irreducible over C(x,z). Hence B is a domain of dimension2. The hypersurface is Cohen-Macaulay, hence S2. Its singular locus from the three partial derivatives y,x,-(3z^2-2z) and the equation is exactly p=(0,0,0). It is regular in codimension1, so Serre's criterion makes B normal. The local embedding dimension at p is3, while its dimension is2, so p is singular. These standard hypersurface and normality criteria are named foundations, not freshly source-audited results.

At p the prime ideal of E is I=(x,z). Its images x,z are linearly independent in I/mI, since the defining relation has no linear term and mI is contained in m^2. Thus I requires two generators at p and E is not Cartier there. Near p, z-1 is a unit. At the generic point of E, y is a unit and x=z^2(z-1)/y, so ord_E(x)=2. The other component of V(x), namely L=V(x,z-1), is absent near p. Consequently div(x)=2E near p: the local Cartier index of E at p is exactly2.

Globally div_X(x)=2E+L. The localization argument using U=A2 gives Cl(X)=Z[E]: any Weil divisor restricts to a principal divisor on U, and a relation supported on E would be the divisor of a rational function with no zero or pole on A2, hence of a constant. In particular [L]=-2[E]. Thus even a free global class group with primitive omitted-divisor generator is compatible with a nontrivial local index in this explicit affine example.

A fixed finite map to a smooth plane is

    h:X -> A2_(s,t), s=x+y, t=z.

Its ring presentation is

    B = C[s,t,T]/(T^2-sT+t^2(t-1)),
    x=T, y=s-T, z=t.

It is free of rank2 over C[s,t], with basis1,T. The monic presentation also proves target-ring injection, so h is finite flat and dominant of degree2.

Crucial scope failure: on the WHOLE chart U, h becomes

    (u,v) |-> (u+v(1+uv)^2, 1+uv),
    det D(hj)=u-v(1+uv)^2=x-y.

This is not a nonzero constant. It vanishes, for example, at (u,v)=(0,0), which maps to the smooth point (x,y,z)=(0,0,1) of U. Relative differentials for the monic quadratic give the non-etale support x-y=0. That support meets U; it is not confined to E, and h is generically etale along E. Therefore this example does NOT satisfy the actual Keller normalization hypothesis. It does not refute a Keller-specific global Cartierness theorem and is not a JC2 counterexample.

If independently confirmed, the example refutes only: normal affine X with a whole A2 open chart, one smooth omitted A1, free boundary-generated class group, and a finite flat map to A2 implies local Cartierness or smoothness. The essential remaining task is a use of the actual etaleness on U and its resulting ramification restrictions. No family, repaired map, parameter variation or automatic paid review is authorized by this candidate.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3723`.
- Body SHA-256:
  `8a61108616c379ee40153cdac3d23e2c1a300d999fd5db9b95e510f06531eec7`.
- Frozen basis: `d873bee2f519f5f2dec33f259c0dbc59c45ae011`.
