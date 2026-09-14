# D125 generic ramification: mixed orders block the unrestricted tangent extension

2026-09-07. **NO-GAIN for an all-ramification exclusion.** The proposed unrestricted extension of the order-three tangent lemma to a least departure of arbitrary order j is false. An explicit finite zero-k source jet with j=2 has a non-boundary first departure because its intermediate s³ term cancels the cubic residue at s⁶. This is not a guarded ramified survivor: its required coefficient x=[gp²]A is identically zero, and it fails the Jacobian at s⁷. The strengthened implication incorporating the nonzero leading x remains open.

## 1. Exact client and the moving reference, not an automorphism

Use the accepted odd moving-face source and all ordinary-lift rows for

    φ(g)=v⁻¹, φ(p)=v⁴u−v−v⁻¹,
    H=p²(p³+g³),
    R_t=H+(t+3)gp²+t p³−(t+3)p,
    S=∂R_t/∂t=p(p²+gp−1).

The full source has A₁₅=H³, B₂₅=H⁵, inner corrections k g²p in A and (5/3)k g⁸p⁵+(5/9)k²g in B, and [A,B]=−5k³g²/9. In a genuine finite K[[s]] arc, accepted14g gives a01=0, 9e=5kx and x²=3ky, where y=[p³]A. At a classified generic center t₀≠−3, y₀=−(t₀+3)³ is a unit. Therefore ord(k)=2ord(x)=2n.

There is a unique same-field formal t(s), t(0)=t₀, satisfying y(s)=−(t(s)+3)³: recursive coefficient solving divides only by the nonzero scalar3(t₀+3)². Writing A relative to R_{t(s)}³ is a reference choice, not a source automorphism. A scalar whole B→B−β(s)A shear is genuinely allowed and preserves every fixed face, origin, parity and lift row. The monic [p¹⁵]A=1 permits matching any prescribed B₁₅ reference coefficient without a denominator.

Let F=A−R_{t(s)}³, G=B−R_{t(s)}⁵ after such a shear. A nonzero x implies ord(F)≤n. The issue is whether the least pair departure j≤n must be tangent to the boundary; one may not simply substitute sʲ for s in the previous m=2 calculation.

## 2. Exact identity showing what intermediate orders leave free

Write R=R_{t(s)}, F=sʲU(s), G=sʲV(s), retaining ALL coefficients, and set Z=3V−5R²U. Then exactly

    [A,B]=sʲR²[R,Z]+s²ʲ[U,V].

Since the target starts at order3ord(k)≥6j, Z modulo sʲ commutes with R. Coefficientwise centralizer lifting, subtracting polynomials in the actual moving R at each stage, gives Z=a(s)R+b(s)R³ modulo sʲ. This uses the accepted centralizer K[R_{t₀}] and the literal odd degree≤23 bound. The low coefficient e has order at least3n, so a(s)=0 modulo sʲ. A whole scalar B shear removes b(s), leaving Z=sʲW.

The exact next identity is

    [R, R²W−(5/3)RU²]+(sʲ/3)[U,W]
          = s⁻²ʲ[A,B].

Modulo sʲ, divide the centralizer expression by R and use its zero origin and even parity. One obtains

    U² ∈ (R,sʲ).

This does NOT imply U∈(R,sʲ). Because R is monic in p and its special fiber is squarefree, coefficientwise polynomial division shows only

    U mod R is divisible by s^ceil(j/2).

Indeed, the first nonzero residue coefficient has a nonzero square in the reduced special-fiber ring. For even j, an actual term s^(j/2)D in U modulo R is still allowed. In F it occurs at order3j/2, strictly between j and2j. Its square contributes at order3j and can cancel the cubic residue of the leading C in U₀=R₀C. This is precisely the missing intermediate-order term, not a generic smoothness assumption or a formal reparametrization.

## 3. A literal finite source jet exhibiting the cancellation

For independent variables R,S define the factored polynomials

    A*=R³+9s²RS²+9s³S³,
    B*=R⁵+15s²R³S²+15s³R²S³+45s⁴RS⁴+90s⁵S⁵.

Direct differentiation in the tiny degree-three/five pair gives the EXACT identity

    [A*,B*]_(R,S)=2835 s⁷ S⁶.

Thus the bracket is zero modulo s⁷, with no discarded intermediate coefficients. Here C=9S² and D=9S³ satisfy

    (5/9)D²−(5/81)C³=0.

The D² term is absent in the naive substitution s→s² into the previous cubic-residue argument. If all odd intermediate powers s³ and s⁵ are deleted from the actual pair, the bracket already fails at s⁶; the checker rejects this mutation.

Now substitute the ACTUAL degree-five R_t and degree-three S=∂_tR_t above. Both lift ordinarily. Their total degrees, weights w=5i−7j, and lower-side maxima i−2j are respectively

    R: (5,1,−1),     S: (3,−7,−2).

Every correction in A* has total degree<15 and weight<3; every B* correction has degree<25 and weight<5. A* satisfies i≤2j, and both pairs have nonnegative exponents, odd parity and zero origins. Consequently they preserve ALL zero-k total/inner-face coefficients, including prescribed zeros. Multiplication of the ordinary generator lifts proves EVERY polynomiality row, without expansion of R³ or R⁵. Therefore this is a genuine point of the complete UNGUARDED k=0 source over K[s]/(s⁷), not merely a selected-row fixture.

It is not an exact commuting arc: on the actual generators the bracket is

    2835 s⁷ S⁶[R_t,S],

which is nonzero. A tiny derivative evaluation at g=p=1,t=0 gives S=1 and [R_t,S]=14. This is an identity-control evaluation, not point sampling for the source or a purported Keller point.

## 4. Recentring does not remove the counterexample to tangent rigidity

Put h=t+3≠0. For the actual A* its low coefficient is exactly

    y(s)=−h³−9h s²−9s³.

The moving reference starts

    t(s)=t+(3/h)s²+(3/h²)s³+O(s⁴).

After subtracting R_{t(s)}³, the first remaining coefficient is

    F₂=9RS²−(9/h)R²S.

It is nonzero, has [p]F₂=[p³]F₂=0, and is NOT of the boundary-tangent form cR+dR²S. The constant term forces c=0; division by the nonzero RS would then make S a scalar multiple of R, impossible since their degrees are3 and5. Equivalently hS−R=3p³−H is explicitly nonzero. A B₁₅ whole shear cannot alter this A coefficient. Hence even with the y-reference fixed, unrestricted nilpotent boundary rigidity fails.

However, BOTH R and S are divisible by p, so A* is divisible by p³. Thus

    x=[gp²]A*=0 IDENTICALLY.

This toy does not satisfy the genuine k=s⁴ leading requirement x₂²=−3h³≠0. It also lacks the s⁴ moving face. It is neither an m=4 survivor nor a counterexample to a strengthened lemma using that nonzero x. For higher ord(k), truncation can hide the future face and saturation conditions, but no continuation is supplied. The case k=0 has no inverse guard, and no guarded-source point is claimed.

## 5. Exact remaining bridge and stop

The useful obstruction is now specific: a proof for arbitrary ramification must control the mixed square/cube residue together with the nonzero leading x and ALL remaining rows. It cannot rely only on centralizer lifting, parity, closed supports, ordinaryness and the first three multiples of a least departure order. The relation U²∈(R,sʲ) does not supply the stronger divisibility needed to erase intermediate motion. No general shape of C,D, divisor-class restriction, or all-m theorem is established here. The exceptional center t=−3, coefficients at infinity, and existence of a finite degeneration from any guarded point also remain open.

Eight capped normal/−O controls pass with zero Assert nodes and exact rational-string witnesses. The actual verifier rejects deleting mixed orders, promoting the finite toy to a full commuting arc, and declaring it a k=s⁴ saturated survivor. All runs use −B and set `sys.dont_write_bytecode=True` BEFORE helper import. No prior caches or frozen files were changed. Only the independent R,S toy and actual degree≤5 generators were expanded; no actual degree15/25 powers, full rows, CAS, AWS, SSH or solver were used.

Witness SHA256 `24a90700ac30b9af4823891a246287abd9c7826485a7795c3d1dcacda3168de1`. The bounded named-history check found the already charged mixed-order warning and unrelated ramified clients; no exhaustive novelty claim follows. The incoming m=2 gate remained LIVE and was not read. This packet's explicit countercontrol and NO-GAIN conclusion do not require that unreviewed theorem to be true. All source/input pins, arithmetic caps and terminal custody are in the owned box. **STOP/IDLE; no implementation or solver consequence.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8254`.
- Body SHA-256:
  `c98f4986969b85a14bbfdfb6d68a05ccc48147ae8f19c7b6ffc5c941828c4433`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
