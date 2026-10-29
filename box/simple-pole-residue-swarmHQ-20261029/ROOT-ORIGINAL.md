# SIMPLEPOLE2115 — linear residues on simple-pole divisors

Status: INTERNAL / ROOT-MANUAL / UNREVIEWED. This is a proposed strengthening of the FILTER1940 observation, not an accepted campaign theorem, a novelty claim, or a solution of the negative-boundary fold problem. The history checks were lexical and partial; their absence of an exact match is not evidence of novelty.

Work over C. On the rational function field C(x,y), put Omega=dx wedge dy and label a prime divisor D by A(D)=ord_D(Omega)+1. A divisor over the standard affine plane with A(D)=0 is a simple-pole divisor. Its residue is a rational one-form on its residue curve.

**Claim.** The residue curve of every such divisor is P1 and has a rational coordinate s for which Res_D(Omega)=c ds, with c nonzero. In particular its rational primitive has degree exactly one, not merely some positive degree.

Use a smooth model obtained from P2 by finitely many point blowups, on which D occurs. The standard facts that a divisorial valuation occurs on such a model and that its generic point is unaffected by further blowups are inherited surface foundations. They are not a new source admission. A divisor with A=0 cannot have an affine centre: Omega has no zero or pole on A2, and divisors above affine centres have strictly positive labels. Thus its construction can be restricted to centres in the boundary over the line at infinity. This boundary remains a simple-normal-crossing tree of rational curves.

The initial line at infinity has A=-2. At a smooth point of one boundary component with label a, blowing up creates a component with label a+1. At a node with component labels a,b it creates a component with label a+b. These formulas follow by substituting into the local expression u^(a-1) v^(b-1) times a unit times du wedge dv; at a smooth point the second factor is absent.

Two elementary invariants follow by induction: no boundary edge joins a strictly negative label to a strictly positive label, and no edge joins two zero labels. A smooth-point blowup preserves both statements. At a node, the permitted pairs are two labels of the same strict sign, or zero and a nonzero label; inserting their sum preserves both statements. The initial single vertex satisfies both.

Consequently a new zero-label divisor can never be born at a node. It is born by blowing up a smooth point of a component with label -1. At that point choose regular parameters u,z, with the component u=0 and the point z=z0. Write Omega=u^(-2) b(u,z) du wedge dz, where b is a unit. In the blowup chart u=t, z=z0+t s,

    Omega=t^(-1) b(t,z0+t s) dt wedge ds,
    Res_D(Omega)=b(0,z0) ds.

Here s is a rational coordinate on the new exceptional P1 and b(0,z0) is nonzero. The residue therefore has exactly one double pole, at s=infinity, and no zeros. Further blowups do not change this rational one-form on the strict transform. This proves the claim at the stated surface-foundation scope.

**Transport consequence.** Let H be a dominant rational map between two standard plane function fields, with H^*Omega_t=c Omega_s for nonzero constant c. Suppose a source divisorial valuation restricts to e times a target divisorial valuation, both of label zero. Let h be the resulting nonconstant map of residue curves, with degree f. Taking residues at the generic points gives

    e h^*Res(Omega_t)=c Res(Omega_s).

Indeed a target uniformizer pulls back to u^e times a unit, and the coefficient of du/u is multiplied by e. Choose degree-one residue primitives R_s,R_t from the claim. Characteristic zero then gives c R_s=e(R_t composed with h)+constant. Comparing degrees gives f=1. Equivalently h is affine in the residue coordinates and carries the distinguished double-pole point to the distinguished double-pole point. This statement needs neither periodicity nor a finite invariant set of divisors. It applies to constant-Jacobian rational maps as well as polynomial Keller maps.

**Scope and hostile checks.** The proof uses the divisor of the standard nowhere-vanishing affine volume form, not an arbitrary exact rational two-form. Arbitrary exact forms can have other zero/pole components and do not satisfy the sign induction. The no-opposite-sign and no-zero-zero edge statements are both needed; the first alone would not exclude creation of a zero divisor at a zero-zero node. A zero divisor can acquire additional boundary intersections later, but its rational residue and degree-one primitive remain unchanged. Normal ramification e is not forced to one by residue transport. Nor does f=1 alone establish the full weak local-homeomorphism statement needed elsewhere in the campaign.

The current obstruction has A=-1, not zero; the specified inverse ends are infinitely singular, not divisorial. The claim supplies no bound on normal ramification, no properness or no-escape theorem, and no exclusion of that negative fold. It replaces the unspecified primitive degree m_D in FILTER1940 by m_D=1 at this precise divisorial simple-pole scope. Its mathematical proof and generic residue-transport step still require independent hostile review before any campaign promotion. No new paid, source, or control-family successor is automatically authorized.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5238`.
- Body SHA-256:
  `41bab1de637f788cabe0bb7f6f46918a4b80e1abac93eff4b77690c99220a633`.
- Frozen basis: `26efb4f4ca452199c6d4bdab4210602071d6abcf`.
