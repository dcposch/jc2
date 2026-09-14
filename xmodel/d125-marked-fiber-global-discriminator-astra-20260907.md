# D125 marked punctured fiber: primary interface returns NO-GAIN

2026-09-07. **NO applicable global exclusion found in this bounded primary lookup.** The exact marked component exists conditionally on a guarded source point and maps with degree1 onto a punctured target line. The checked theorems require an affine-line component, a generic whole punctured fiber, or additional arithmetic. None of those missing hypotheses follows here. This is not a no-go for every possible global theorem and uses no pending pure-center proof.

## Exact physical component and its map

Work over a characteristic-zero field, extending to C for the complex primary statements. At a hypothetical guarded point of accepted14c let k be nonzero, d=5k²/9, and use its full ordinary lifts

    g=v⁻¹,   p=(v⁵u−v²−1)/v,   P=phi(A), Q=phi(B).

The licensed supports and low rows give A(g,0)=0, A_p(g,0)=kg² and B(g,0)=dg. Indeed the only possible p-linear A terms are a01 p and kg²p; the constant Jacobian row forces a01=0 since d is a unit. The derivative of this chart has determinant v², giving J(P,Q)=−5k³/9.

Set N=v⁵u−v²−1. Its zero curve C has coordinate ring

    K[u,v]/(N) = K[v,v⁻¹],
    u=v⁻³+v⁻⁵,        v⁻¹=uv⁴−v.

Thus C is a closed irreducible smooth G_m, not A1. P vanishes on it, so N divides P. Moreover P_u|C=kv² is nonzero; C is a reduced fiber component. Writing P=N M gives M|C=kv⁻³, a unit, so other components cannot intersect C. This does not identify the rest of the fiber.

On this component,

    Q=d/v,   dQ/dv=−d/v²,
    v=d/Q,   u=Q³/d³+Q⁵/d⁵.

The function-field degree is1 and the restriction is an isomorphism onto the punctured line. It is NOT finite/proper onto A1: the inverse coordinate v has a pole at Q=0. As v tends to infinity, u tends to0, while (P,Q) tends to(0,0). Consequently (0,0) is a nonproper value of the hypothetical map. This does not make the entire target line a nonproperness component or show that (0,0) has no other preimage.

## Exact primary hypotheses and first missing arrows

[Gwozdziewicz, Theorem1.1, arXiv:alg-geom/9305008v1](https://arxiv.org/pdf/alg-geom/9305008v1) concerns a constant-Jacobian plane polynomial map injective on an affine line in its SOURCE. Its proof uses line-embedding rectification and Newton polygons. Our C cannot be rectified into A1: K[v,v⁻¹] has nonconstant units, whereas K[t] does not. Its image also omits a point. The first invalid arrow would be replacing this punctured-line open immersion by the theorem's embedded affine line. Degree1 alone does not perform that replacement.

[Chau, arXiv:1502.00328v3, Lemmas2.3 and3.2(b)](https://arxiv.org/pdf/1502.00328v3) respectively require an affine-line-type component or exclude a GENERIC whole fiber of punctured-line type. Neither matches one known special G_m component. The latter proof varies generic fiber values; that variation and whole-fiber hypothesis are absent. His concluding remark(iii), p.5, leaves exclusion of arbitrary punctured-line components as an additional requirement, not a proved consequence. This is the paper's scoped statement, not a claim that no later result can exist.

The same paper's Theorem1.1/Corollary2.2 require an infinite quasi-integral set, not merely infinitely many rational points. That bridge is particularly unavailable on C: for any fixed positive integer D, writing u=a/D and v=b/D gives

    a b⁵=D⁴b²+D⁶,   b nonzero,

so b divides D⁶. There are only finitely many such b and corresponding a. Hence this marked component has no infinite bounded-denominator rational subset, independently of the hypothetical source coefficients. Other fiber components remain unknown; general algebraic source points need not have rational coefficients either.

## Scope, primary custody and stop

The two complete primary papers and their relevant proofs were read; cited underlying embedding/arithmetic theorems remain imports. Exact versions, URLs, retrieval timestamps and scope are in `box/d125-marked-fiber-global-discriminator-20260907/primary-interface.md`; PDF/text/version-record and campaign-snapshot hashes are in `custody.json`. PDF retrieval was23:32:47–48UTC. The marked-curve statements are direct hand algebra, not a full-source computation.

The prior torsor report's missing-boundary/properness gap is not repaired by this component. No actual A15/B25/high R power, CAS, AWS, solver, pending proof, live peer or protected tree was used. Discovery remained a single bounded Keller-fiber applicability pass, not an exhaustive literature census. No source point, ideal decision or global degeneration theorem follows. All task writers and children terminal; transaction verified; STOP/IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4754`.
- Body SHA-256:
  `860e5c684679f67f287d108b9e249e09e1d33ce88d5c477a2ab4081e958e583a`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
