# D125 symmetry discriminator: one smaller sufficient client, not a normalization

Status: **DESK PASS for restricted-client construction; no nonemptiness or solver-win claim.** The unequal/rational μ2 fixed locus has a **22-coordinate gauge slice** using reviewed B reconstruction plus A-only Hermite graphs, versus 49 unrestricted. Standalone Hermite gives 81 versus 172. The μ3 fixed locus is impossible. No applicable theorem excluding μ2 was established. This is a smaller sufficient counterexample search only; this packet authorizes no implementation.

## Exact client and action

Work over any Q-algebra. Use the accepted complete unequal/Q source contract: A/B polygons

| Member | Vertices besides the origin | Outer face | Inner face |
|---|---|---|---|
| A | (0,15),(9,6),(2,1) | H³ | g²p+g⁹p⁶ |
| B | (0,25),(15,10),(1,0) | H⁵ | 5g/9+5g⁸p⁵/3+g¹⁵p¹⁰ |

Here H=p²(p³+g³), both constants are fixed zero, and **every** coefficient on both faces is prescribed, including zeros. Require all coefficients of [A,B]+5g²/9 to vanish and all negative-v coefficients of the literal lifts

P=A(v⁻¹,v⁴u−λ₂v²−λ₃v−v⁻¹), likewise Q.

There are 660 universal Jacobian slots and 30+75 polynomiality slots. The fixed Jacobian scalar c=−5/9 is already a unit; all vertex guards are fixed nonzero rational numbers. The accepted lift theorem makes any field solution an ordinary Keller pair of exact degrees75/125, hence a nonautomorphism by the reviewed plane degree criterion.

For τ define

Aτ=τ⁻¹⁵A(τg,τp), Bτ=τ⁻²⁵B(τg,τp),
λ₂τ=τ⁻³λ₂, λ₃τ=τ⁻²λ₃.

A/B coefficient of total degree s has character s−15/s−25. The nonzero lower faces have defects 12 or 24; c transforms by τ⁻³⁶. Thus τ¹²=1 preserves **all** faces, constants, guards and full equations. Negative row [uᵗvᵉ] has character 5t−e−D for member degree D. Indeed a term using b factors −λ₂v² and d factors −λ₃v has e=5t+3b+2d−i−j, giving exactly that character. Jacobian row of total degree d has character d−38. The source action is

Pτ(u,v)=τ⁻¹⁵P(τ⁵u,τ⁻¹v), Qτ(u,v)=τ⁻²⁵Q(τ⁵u,τ⁻¹v).

These character statements define group-scheme fixed loci over Q; adjoining roots of unity is unnecessary. Restrict by setting forbidden-character coefficients to zero and carry **all** equations through that quotient. There is no averaging or assertion that an orbit meets a fixed locus.

## Fixed loci and compression

For μ3, λ₃=0, A has total degrees 0 mod 3 and B degrees 1 mod 3. Both source variables have weight 2, while P/Q have weights 0/1; hence both physical linear jets vanish. Equivalently, a u-linear or v-linear contribution would require receiver total degree respectively 5+3b or 3b−1, both 2 mod 3. Neither member permits it. Therefore J(P,Q)(0)=0 contradicts −5/9, over the full coefficient quotient, not merely generically. μ6 and μ12 are consequently excluded. μ4 forces both λ's zero; then neither lift has a v-linear term, giving the same contradiction.

For μ2, λ₂=0 and A/B have odd total degrees. P/Q are centrally odd. This does not kill their linear jets. For example, the global odd toy P=u, Q=uv⁴−v lifts from polynomial receivers g⁴p+g⁵+g³ and p+g, and has J(0)=−1. Its Jacobian is not constant, and it does not satisfy the required faces; it only refutes an origin/parity shortcut.

| Count | Unrestricted | μ2 | μ3 (excluded) |
|---|---:|---:|---:|
| Free A/B coefficients | 71 / 196 | 33 / 94 | 20 / 60 |
| Free λ's | 2 | 1 | 1 |
| Before Hermite | 269 | 128 | 81 |
| Hermite pivots A/B | 27 / 70 | 13 / 34 | 8 / 22 |
| After Hermite | 172 | **81** | 51 |

The counts use the actual frozen slots, independently checked against polygon half-planes. At receiver total degree s<D, the existing Hermite pivot slots are (i,s−i), 0≤i<ceil(s/5). Their fixed matrices have entries (−1)^(s−i−t) binom(s−i,t), determinant ±1. With λ₂=0, the row's higher-degree inputs have degree s+2d, preserving parity. Descending graph reconstruction therefore makes every even-level pivot zero when even retained coefficients vanish; odd blocks remain closed. This proves compatibility with the **existing** Hermite coordinates, without further divisions or B-reconstruction assumptions.

Only 336 of the 660 Jacobian slots can survive parity. Of 105 negative slots, 16 A and 39 B can survive; eight fixed-top rows already vanish by the multiplicities of H³/H⁵ at p/g=−1, leaving the 47 Hermite pivots. Retaining the original full row lists is safe; these are typed zero counts, not omitted compatibility equations. All remaining low Jacobian rows stay. These counts are not ideal dimensions, term counts or runtime measurements. λ₃ is forced to be a unit at any full μ2 solution (λ₃=0 kills both v-linear terms), but **λ₃=1 is not a licensed normalization**.

### Cheaper compatible B+A composition

The terminal B and B+A-Hermite gates were read wholly; only the repaired exact witness is used. At B degree d, the fixed-unit diagonal [H³,B_d] and every selected forcing row have character d−25. Their unique triangular graph solution is therefore equivariant over arbitrary base quotients. In particular, even B blocks have zero forcing after higher even blocks vanish; their kernel coordinates also vanish. Fixed inner blocks occur only at odd degrees 1 and 13. The actual odd free B columns total94, with exact fixed-matrix rank92 and kernels H,H³ at degrees5,15. These were independently recounted and ranked without expanding forcing.

After A's13 parity-compatible Hermite pivots, the graph ring has 20 A coordinates, β₁=[p⁵]B, β₃=[p¹⁵]B and λ₃: **23 coordinates**. The omitted β₂=[p¹⁰]B and β₄=[p²⁰]B have odd characters and vanish. Put s=β₃, a₅=[p⁵]A; a₁₀=0. The whole target shear B'=B−sA sends β₁ to β₁−s a₅ and β₃ to zero, with inverse restoring sA. Both s and a₅ are μ2-invariant. A is strictly below B's inner/outer faces and has zero constant, so all prescribed coefficients survive. Thus the reviewed affine-line decomposition is equivariant with trivial action on s: the **fixed-locus** complete quotient is T₂[s], where T₂ is a quotient on **20 A + one B kernel + λ₃ = 22 coordinates**.

Every unselected high Jacobian row and all degrees0–13 (including the target) remain. All75 B-negative rows remain; their shear invariance is used only modulo the imposed A-negative equations. No70 B-Hermite savings are subtracted. This is a polynomial graph/gauge theorem, not a materialized 22-variable ideal or a fill bound. The two matrix/kernel-character and whole-gauge-inverse mutations also fail normally and under −O.

## Does an equivariant theorem already exclude μ2?

Not on the checked interface. [Moskowicz, arXiv:1410.7705v1](https://arxiv.org/pdf/1410.7705v1), Lemma 2.1 p.1, claims every order-two polynomial automorphism is conjugate to exchange. Central inversion has Jacobian +1; exchange has −1. Polynomial conjugacy preserves this determinant, so that universal lemma is false. Theorem 2.3's proof explicitly depends on it; its apparent “any involution” extension cannot exclude this client. This refutes that proof dependency, not a Keller theorem's conclusion. Exchange equivariance is a different condition.

[Shaska, arXiv:2607.20210v2](https://arxiv.org/pdf/2607.20210v2), Theorem 3.4 pp.8–10, assumes a nontrivial G_m action with equivariance for every parameter. Finite odd parity does not supply it. No such extension is proved here. The bounded primary search is not an exhaustive absence theorem.

History checksum found related high-z μ2 necessary systems, not this complete source restriction; no priority claim follows. Source/version/read-scope receipts and exact hashes are in `box/d125-symmetry-discriminator-20260907/sources-and-history.md` and custody.json. Twelve capped runs passed: each normal/-O witness agrees byte-exactly, and all four actual mutations fail in both modes; zero Assert nodes. Standalone witness SHA256: `9c3708294dc3c0df25cb256598436db5736a9737a2504dada04d0777171c2e4a`.

**Decision:** μ2 gives a materially smaller coordinate presentation of an honest *restricted sufficient* CE client, but no measured speed advantage or evidence of a point. A solution would satisfy the accepted full lift contract; exclusion would retire only this symmetry-fixed locus. No global D125 coverage, fixed-locus normalization, baseline change, builder, solver, or follow-on work is performed. All owned writers are finished on custody publication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8661`.
- Body SHA-256:
  `caedb9048e3f0e245b3eec41d11609519c27eef617f03adf8bffcd3ff913421b`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
