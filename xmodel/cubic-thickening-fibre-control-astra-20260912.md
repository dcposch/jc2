# Cubic thickening: the fibre length is three, not four

First action 2026-09-12 00:36:14 UTC; original reserve00:50/HARD00:53.
Sole input TASK.md SHA256
7c07931efd8b348c04b405c7deb30d43bdf88f5402fe260946c8553ac3cfa236
matched before fresh WHOLE read. Manual co-research, not promotion.

## 1. The cover, ramification and normalization

Every proposed algebraic assertion is correct. There is an isomorphism

    S ≅ B[T]/(T³+aT+b),       T↦t.

Thus S is finite free of rank3 over B, with basis1,t,t². It is a domain,
so its generic fibre is a field of degree3. Y=SpecC[a,t] is smooth. The
Jacobian of (a,t)↦(a,−t³−at) is −(a+3t²)=−r. Therefore its ramification
divisor is exactly the reduced smooth curve C={r=0}≅A¹_t.

Direct multiplication gives the identity

    4a³+27(t³+at)²=(a+3t²)²(4a+3t²).

Hence Δ vanishes on Cplus=SpecS/(r²), and this thickening maps to the
cusp Z. On C the map is (a,b)=(-3t²,2t³). Its image ring is C[t²,t³],
the coordinate ring of Z. The extension to C[t] is finite, is birational
because t=−3b/(2a) in the common fraction field, and C[t] is normal.
It is consequently the normalization map C→Z.

Putting ε=r gives the abstract isomorphism

    O(Cplus)=C[t,ε]/(ε²),
    a=ε−3t²,       b=2t³−εt.

These are the actual B-actions. The product action through the reduced
curve would instead have a=−3t²,b=2t³. Confusing the two changes the
morphism whose fibre is being measured.

## 2. Exact fibre lengths

At z=(a,b)=(0,0), substitute a=0 and b=−t³. Then

    O(C_z)=S/(r,a,b)=C[t]/(t²),
    O(Cplus_z)=S/(r²,a,b)=C[t]/(t³),
    O(Y_z)=S/(a,b)=C[t]/(t³).

The respective C-vector-space dimensions, hence scheme lengths, are2,3,3.
For the second equality r² becomes9t⁴ and adds no relation to t³=0.
Equivalently, in dual-number coordinates the fibre imposes ε=3t² and
t³=0; ε²=0 is then redundant. It does NOT impose t²=0 and an independent
dual number. The product-action fibre would have ring
C[t,ε]/(t²,ε²), of length4, but it is a DIFFERENT Z-morphism.

This is a counterexample to multiplying these lengths from abstract
product structure alone. Smooth Y, smooth C, and a finite flat cubic
ambient map do not repair that inference.

## 3. The missing hypothesis, in two precise formulations

A sufficient multiplicative hypothesis is a factorization OVER Z

    Cplus --π--> C --> Z

with π finite locally free of rank2. Base change then makes Cplus_z finite
locally free of rank2 over C_z, so its length is2·length(C_z). The abstract
projection C×SpecC[ε]/ε²→C is indeed finite free, but the actual map to Z
does not factor through it. Flatness over C without this compatibility is
irrelevant; it is not appropriate to replace it by a vague flatness claim
over Z.

Nor can a different Z-compatible retraction fix the splitting at the
cusp. Such a retraction sends the parameter on C to τ=t+εh(t) (locally,
h is regular at t=0). Compatibility with a requires

    −3τ²=ε−3t²,       hence −6t h(t)=1,

which is impossible at0. Compatibility with b gives the same condition.
Away from0 the choice h=−1/(6t) works, so the failure is genuinely at the
normalization's exceptional fibre, not at its generic point. Any map to C
over Z must reduce to the identity, since C→Z is birational; this argument
does not overlook a different reduced lift.

More minimally, let J=(ε) in O(Cplus). As a B-module J≅O(C): multiplying
ε by a,b gives −3t²ε,2t³ε. Tensor the exact nilpotent-ideal sequence
0→J→O(Cplus)→O(C)→0 with the residue field at z. Multiplication of lengths
would hold if J⊗k(z)→O(Cplus_z) remained injective. It does not:

    J⊗k(z)≅C[t]/(t²)·ε,
    ε↦3t²,       tε↦0 in C[t]/(t³).

The kernel is the one-dimensional span of tε. The missing length is exactly
the nonzero image of the Tor connecting map; the image of J in the fibre
has length1, giving3=1+2 instead of4. Thus fibrewise injectivity is the
precise needed condition for this additive-length argument, while a
base-linear finite-flat rank2 factorization is a clean sufficient condition.

## 4. No embedded repair, and the source limitation

For ANY closed subscheme X⊂Y with ideal I, its origin fibre is
S/(I,a,b), a quotient of C[t]/(t³). Therefore length(X_z)≤3 whenever
considering this fixed origin fibre. This applies even to alternative
embedded thickenings with extra embedded structure: none can have length4.
Among effective Cartier divisors with cycle2C there is only V(r²), since
C is principal and S is factorial. An abstract Z-product double can have
length4, but cannot be embedded as a B-subscheme of this Y with the stated map.
This says nothing about a different ambient cover or altered base map.

Finally, Y_et=D(r). The coordinates (t,r) identify it with A¹×G_m; r is a
nonconstant unit. A dominant regular map A²→Y_et would inject its
coordinate ring into C[x,y], send r to a nonzero constant k, and annihilate
the nonzero element r−k. Impossible. A nonempty open A² inside Y_et would
give such a dominant open immersion and is likewise impossible.

The example is therefore NOT an actual Keller map or an intermediate
Keller-source donor. It refutes only the bare thickening/fibre-length
inference. No external paper was read, and no verdict on its theorem,
the classical geometric-degree3 exclusion, arbitrary cubic blocks or JC2
is asserted. There is no novelty claim or new canonical OPEN.

Quantity2 versus3 is resolved by the manual quotient substitutions above;
the original under15-author-minute estimate was planning, not scientific
runtime. No scientific execution or extra input was used. Own full reads,
scope/quantity/cheapest-test checks, sole-input postpin and collision check
precede the unique final marker. Independent review is still required
before any promotion; no follow-on is authorized.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5903`.
- Body SHA-256:
  `52acbcb3a5a82b0ed892b88168f99ece0cbe4cb628735e130c4e5d77deddba32`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
