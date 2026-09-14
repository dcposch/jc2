# Complete field-point classification of the unguarded D125 zero-k boundary

2026-09-07. **Primary result: DESK PASS at explicit external-theorem trust.** Over every characteristic-zero field K, all points of the unguarded k=0 normalized source are exactly

    A₀=R_t³+αR_t,
    B₀=R_t⁵+βR_t³+γR_t,       t,α,β,γ∈K,
    R_t=p²(p³+g³)+(t+3)gp²+t p³−(t+3)p.

No field extension is needed for this classification. It concerns field-valued points, not the full possibly nonreduced boundary scheme. The optional deformation interface in §5 has a separately stated provisional dependency. No guarded point or generic-fiber conclusion is claimed.

## 1. Exact source and primary input

First OMIT the k-inverse guard, then set k=0. Retain odd parity, zero receiver constants, the actual unequal closed polygons, full total faces A₁₅=H³/B₂₅=H⁵ for H=p²(p³+g³), inner faces g⁹p⁶/g¹⁵p¹⁰, all [A₀,B₀]=0 rows, and all negative coefficients for

    φ(g)=v⁻¹, φ(p)=v⁴u−v−v⁻¹.

This is not a specialization of the guarded ring, whose k=0 fiber is empty.

Imported statements are Arzhantsev–Petravchuk, [arXiv:math/0608157v2, Lemmas4–5 p.5 and Corollary1 p.6](https://arxiv.org/pdf/math/0608157v2). In characteristic zero, vanishing Jacobian gives algebraic dependence; dependent nonconstant polynomials over K lie in K[S] for a closed polynomial S. The integral closure of K[A₀] in K[g,p] is the algebra of its closed generative polynomial, unique up to affine change. Whole statements and their displayed proofs were read. Lemma4's referenced criterion and the published theorem dependencies are imported, not independently replayed. Both A₀,B₀ are nonconstant by their fixed tops.

## 2. Normalize the common generator without roots

Write A₀=F(S), B₀=G(S), with S closed. Degree composition gives deg S dividing15 and25, hence deg S=1 or5. Degree1 would make A₀'s top a scalar fifteenth power of a linear form, whereas H³ has p-multiplicity6, impossible. Thus deg S=5, deg F=3 and deg G=5.

Let J=S_top and let f₃,g₅ be the leading coefficients of F,G. Then f₃J³=H³ and g₅J⁵=H⁵. In K(g,p), put q=J/H. The identities q³=f₃⁻¹ and q⁵=g₅⁻¹ imply

    q=q⁶/q⁵=g₅/f₃²=:r∈K*.

Replacing S by (S−S(0))/r yields S(0)=0, S_top=H and monic F,G, all over K. This avoids selecting cube or fifth roots.

Let σ(g,p)=(−g,−p). Since σ(A₀)=−A₀, σ preserves K[A₀] and its integral closure K[S]. Consequently σ(S)=aS+b, with a∈K*. Evaluation at the origin gives b=0; σ²=1 gives a=±1. If a=1, A₀=F(S) would be even, contradicting its nonzero odd top. Hence σ(S)=−S. Injectivity of K[T]→K[g,p], T↦S, now forces F and G to be odd. Therefore

    A₀=S³+αS, B₀=S⁵+βS³+γS,   α,β,γ∈K.

## 3. Recover the support and polynomial lift of S

For a nonconstant polynomial V over a field and a degree-d polynomial F, the convex hull including0 satisfies

    Newt₀(F(V))=d Newt₀(V).

Indeed, for any linear weight whose maximum on Newt₀(V) is positive, the highest power V^d has strictly greater weight than every lower power and cannot cancel. When that maximum is zero, both hull support functions are zero. Equality of all support functions proves the claim; it does not require positive coordinate weights.

Applying this to A₀=S³+αS and its actual polygon gives

    deg S≤5, 5i−7j≤1, i≤2j

for every S monomial. With S_top=H, oddness and S(0)=0, the ONLY lower slots are gp²,p³,p. Thus S=H+a gp²+b p³+c p.

Now W=φ(S) lies in K(u,v). The full A-negative equations give φ(A₀)∈K[u,v], and W satisfies the monic equation W³+αW−φ(A₀)=0. Since K[u,v] is integrally closed, W is ordinary. Equivalently, a negative lowest v-power n of W would contribute uncancelable lowest power3n to W³+αW. This uses a field/domain, not an assertion over arbitrary nilpotent coefficient rings.

The complete negative part of this degree-five W is

    (a−b−3)v⁻³+(2a−3b−c−9)v⁻¹.

Hence a=b+3 and c=−b−3. Taking t=b gives exactly R_t, with no exception or parameter division.

Conversely, R_t is odd, vanishes at the origin, satisfies the three support inequalities, has total top H and unique inner leader g³p², and the two displayed negative coefficients vanish. Powers and linear combinations consequently satisfy every boundary face/support and polynomiality row, while [F(R_t),G(R_t)]=0. This verifies the entire family without expanding A₀ or B₀.

Normalized S is unique by generative-polynomial uniqueness: the remaining affine change has scale1 and translation0. R_t is closed because prime degree5 and its non-power top exclude a nontrivial composition. Thus the field parameters are unique. If the optional [p¹⁵]B₀=0 target slice is also imposed, its exact condition is β=−[p¹⁵]R_t⁵; this removes β only, with the whole shear's corresponding γ adjustment. The unsliced classification above does not assume that extra gauge.

## 4. Controls and precise limitations

Owned checks enumerate the three literal lower slots, expand only the degree-five generic generator, solve its two complete negative rows with determinant−1, test same-field top normalization, and exercise a monic pole-order toy. Real mutations insert the forbidden g²p slot, omit the actual remaining v⁻¹ row, or invert the normalization scalar incorrectly. All are rejected normally and under −O. Eight final capped runs pass, with identical witness bytes and zero Assert nodes.

The first runner attempt exposed a control bug: negative monomial exponents in a coefficient substitution were treated as exponent zero, so the omitted-row mutation was not detected. The helper now handles negative powers of unit monomials explicitly, and an exact check requires the failed candidate to leave precisely −3v⁻¹. The preliminary positive witness is retained, but only `final-witness*.json` and `final-replay.json` are charged. No earlier campaign file was edited.

Final witness SHA256 `fc345a150a1946c502cd0ad0f7dd5d5a34ecb16e5ef5bf317bb4a864eb4c0a7a`. Commands≤30wall/25CPU seconds,512MiB. This field-point classification does not assert a scheme isomorphism, reducedness, a flat family, or anything about k≠0.

## 5. Optional general order-two interface — PROVISIONAL composition

This section adds the root-requested interface. Its α=γ=0 branch depends on the earlier pure-power obstruction `99d25147…`, still PROVISIONAL and under a separate live gate, which was NOT read. The classification §§1–3 does not depend on that obstruction.

Consider a K[k]/(k³) jet through a classified center, with the prescribed moving faces. Write R=R_t, a(R)=3R²+α and b(R)=5R⁴+3βR²+γ. As before A₁ has unique weighted leader g²p. The centralizer of R is K[R], by prime degree5 and its non-power top. First order gives

    aB₁−bA₁=f(R).

Suppose α≠0 and pass to Kbar to select r≠0 with3r²+α=0. If b(r)≠0, reduction modulo R−r makes A₁ constant modulo R−r. But the leading monomial g³p² of R−r cannot divide that of A₁ minus a constant, namely g²p. Thus b(r)=0. Since b is even, a divides b, equivalently γ=βα−5α²/9, with

    q=b/a=5R²/3+β−5α/9.

Cancellation of the nonzero polynomial a in the first-order bracket gives B₁=qA₁+h(R). Second order gives

    E=a(B₂−qA₂)−(5/3)R A₁²−h'(R)A₁ ∈ K[R].

To reduce this at R=r, note that R−r is irreducible over Kbar[g,p] for every r≠0. As a cubic in g, divide by p². Its constant coefficient has p-adic valuation−2; its g coefficient is t+3 and leading coefficient1. A Laurent-series root with integer valuation n≥0 leaves the constant term as unique minimum; for n≤−1, g³ has unique minimum3n<n,−2. No root exists in Kbar((p)); a cubic is therefore irreducible there, and hence over Kbar(p). The original polynomial is primitive over Kbar[p] because its constant coefficient modulo p is −r. Gauss's lemma proves the claim, without a Newton–Puiseux import.

In the resulting domain Kbar[g,p]/(R−r), the second-order identity is a quadratic equation for A₁ with nonzero leading coefficient−5r/3 and constant coefficients in Kbar. It splits over Kbar, so A₁ is constant in that domain. The same weighted-leader contradiction follows. Thus α≠0 is excluded already at order two.

If α=0 but γ≠0, first order modulo R gives R|A₁: the scalar remainder vanishes at the origin. This is the same impossible weighted leader. If α=γ=0, the constant whole shear B→B−βA gives pure powers at k=0. It preserves the actual A⊂B polygon, every B inner slot (A's maximal weight3<5), every B total-face slot (15<25), origins, parity, and the full bracket. The30 A-negative indices lie in B's75-slot envelope, so subtracting β times those rows preserves polynomiality, including all low rows. The earlier provisional pure-power obstruction then rules out this final branch. The literal inclusion/strict-face tests and general second-order identity are independently checked here.

**Conditional composition outcome:** after accepting that remaining prior obstruction, no classified field center admits an unramified order-two k-jet. This says nothing about ramified approaches k=s^m, coefficients escaping to infinity, nilpotent boundary structure, guarded-N emptiness/properness, solver speed, or JC2. No further generation or computation is authorized. All writers are idle at custody publication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9535`.
- Body SHA-256:
  `ca0c8971d94321d56f987bdb8bf8ea613b2e3709bf05c393106e7b7fc7d33526`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
