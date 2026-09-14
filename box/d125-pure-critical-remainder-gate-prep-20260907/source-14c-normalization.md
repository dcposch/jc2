# Odd D125 source: exact unit normalization with moving faces

2026-09-07. **DESK PASS: rank-six finite étale descent, not an unchanged-face normalization.** This proof assumes odd A/B and λ₂=0 directly. It does not use the pending 22-coordinate graph theorem. No source, ideal or solver implementation is changed.

## 1. Rings and the unit, before normalization

Take the accepted complete unequal/Q source: the original polygons and every prescribed zero/nonzero face coefficient, H=p²(p³+g³), A₁₅=H³, B₂₅=H⁵,

A_inner=g²p+g⁹p⁶,
B_inner=5g/9+5g⁸p⁵/3+g¹⁵p¹⁰,
[A,B]=c₀g², c₀=−5/9.

Impose odd total receiver degrees and λ₂=0; put ℓ=λ₃. Retain ALL Jacobian coefficient equations and all30+75 negative-v rows for

P=A(v⁻¹,v⁴u−ℓv−v⁻¹), and likewise Q.

Let O₀ be this complete coefficient quotient over Q. The accepted unit-ideal lemma gives c₀=ℓM in O₀. Explicitly, each v-linear coefficient is divisible by ℓ: its monomial contributions require 2d=i+j+1, hence d≥1. Write P_v(0)=ℓr, Q_v(0)=ℓs. Ordinariness and the full bracket give c₀=ℓ(P_u(0)s−rQ_u(0)). Thus ℓ⁻¹=M/c₀ already exists. This is an identity over arbitrary Q-algebras, including nilpotents, not a radical or field-point argument. Consequently O₀≅O₀[ℓ⁻¹]; localization loses no component.

## 2. Exact transported chart

For a coefficient of odd total degree m define

ã_ij=ℓ^((m−15)/2)a_ij,
b̃_ij=ℓ^((m−25)/2)b_ij,
k=ℓ⁻⁶.

All exponents are integers. Define N over E=Q[k,k⁻¹] using the SAME odd slots, zeros, origins and total faces, but lift parameter λ̃₃=1 and

| Prescribed coefficient | New value |
|---|---:|
| A_(2,1) | k |
| B_(8,5) | 5k/3 |
| B_(1,0) | 5k²/9 |
| Jacobian scalar | c₀k³ |

All other fixed coefficients are transported too; outer coefficients are unchanged and zero coefficients remain zero. Require all coefficients of [Ã,B̃]−c₀k³g² and every negative row of the λ̃₃=1 lifts. A polynomial-ring presentation MUST include zk−1. No assertion that the unguarded full equations force k≠0 is made; no k=0 branch is licensed.

For member degree D and negative row (t,e), each contributing term satisfies e=5t+2d−m. Therefore

L̃_(t,e)=ℓ^((5t−e−D)/2)L_(t,e).

The exponent is integral for every surviving row. Wrong-parity rows are identically zero on both sides. For a Jacobian row of total degree n, its transport factor is ℓ^((n−38)/2); only even n survive. At n=2 this is ℓ⁻¹⁸=k³, including the target scalar with its sign. All factors are units. These identities transport EVERY row, not a jet or selected subsystem; face and guard relations transport as displayed.

## 3. The exact reverse arrow and descent

Let D=Q[ℓ,ℓ⁻¹], viewed as an E-algebra by k↦ℓ⁻⁶. The coefficient maps above and their inverses

a_ij=ℓ^((15−m)/2)ã_ij,
b_ij=ℓ^((25−m)/2)b̃_ij

give an explicit ring isomorphism

**O₀ ≅ N ⊗_E D.**

The reverse faces satisfy kℓ⁶=1, k²ℓ¹²=1 and k³ℓ¹⁸=1. The unit row factors prove equality of the complete transported ideals, so the isomorphism is valid over any further, possibly nonreduced coefficient quotient.

As E-algebras, D≅E[T]/(T⁶−k⁻¹), with T automatically invertible. It is free of rank6 with basis1,T,…,T⁵; derivative6T⁵ is a unit, hence the cover is finite étale and faithfully flat. The same holds after base change to N, including when N has nilpotents. Therefore O₀ is nonzero iff N is nonzero, and their defining ideals have equivalent properness. Every old point gives a new point over the same field; a new point lifts after adjoining a sixth root ℓ of k⁻¹. Such a root need not exist in the original field. Qbar-point nonemptiness is equivalent. This is not generally an isomorphism O₀≅N or a same-field inverse on points.

For the physical source transformation, over the faithfully flat extension τ²=ℓ the formula is

P̃(u,v)=τ⁻¹⁵P(τ⁵u,τ⁻¹v),
Q̃(u,v)=τ⁻²⁵Q(τ⁵u,τ⁻¹v).

Odd parity makes every coefficient exponent of τ even, so these polynomials descend without choosing a square root: [uᵗvᵉ]P is multiplied by ℓ^((5t−e−15)/2), and similarly for Q. The determinant is c₀ℓ⁻¹⁸=c₀k³. Monic coefficients u¹⁵v⁶⁰ and u²⁵v¹⁰⁰ have scaling factor1. Thus ordinaryness and exact degrees75/125 persist. The accepted sufficient counterexample contract applies to every guarded field point of N; none is exhibited.

## 4. Cost boundary and controls

The parameter is traded, not removed: the actual odd slots give33 A+94 B+one unit parameter=128 Laurent coordinates. Representing k⁻¹ by z gives129 polynomial generators and zk−1. No pending compression theorem is used in that count.

At λ̃₃=1 the A-polynomiality rows have constant rational coefficient matrices and affine-linear forcing in k; A's only varying prescribed lower face is k. Thus its existing Hermite linear elimination would remain affine-linear in retained A coefficients and k, rather than contain powers of ℓ. B-negative rows may contain k², and Jacobian rows k³. No residual substitution, term count, runtime benefit or production authority follows from these degree observations.

Eight capped standard-library controls passed normally/−O with byte-identical witnesses, zero Assert nodes, and genuine changed-face, changed-c-power and omitted-invertibility failures. The guard negative control is a k=0 **parameter-contract** fixture, not a claimed full-system point. Checks use Q[ε]/(ε²), all13747 support/exponent contributions and12 separate toy Laurent monomials; no full pair is expanded. Witness SHA256 `a04393cf75fbc22d2ff4fb4480fa27600921fba57de42cd5b2556f80cff7e39c`. Whole terminal lift and unit-lemma proofs/gates were consumed; pins and custody are in `box/d125-parity-unit-normalization-20260907/`. All writers idle at handoff. **STOP:** exact varying-face transport only; no unchanged-face overwrite, source-coverage claim, solve, proper ideal or JC2 resolution.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6094`.
- Body SHA-256:
  `a015d135dc3da999442a7ba1c46ec308688db0a82ad4901105b7b4946917dd9f`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
