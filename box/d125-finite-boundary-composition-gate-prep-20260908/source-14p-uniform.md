# D125: a uniform obstruction to finite ramification at a generic boundary center

2026-09-07. **DESK PASS, PROVISIONAL pending independent review.** For the accepted moving-face, odd unequal source, no genuine finite field-coefficient arc with k=s^m, m>0, has a boundary center t₀≠−3. The proof retains all intermediate coefficient orders and a moving reference. It does not assert that a guarded source point has such a degeneration, exclude the exceptional center or escape to infinity, or prove source emptiness/JC2. Arbitrary nilpotent jets are not being saturated by cancellation.

This uniform argument is re-rooted on the accepted literal source14c, field boundary classification14f, saturated low equations14g and the already imported polynomial-centralizer theorem. It does NOT use the provisional existence of the explicit six-jet or the provisional generic-m4 theorem as a theorem premise. Those terminal reports supplied the motivating mixed-order warning and pole heuristic. Root supplied the uniform question and cutoff correction; the origin filtration and monic-remainder proof below are this lane's synthesis with that feedback.

## 1. Exact hypotheses and the moving reference

Let K be a characteristic-zero field, and suppose the FULL normalized odd receiver/lift source has coefficients in K[[s]], with k=s^m. The nonzero-k guard is interpreted on the generic fiber K((s)); all full polynomial Jacobian and negative-lift rows hold in K[[s]]. All coefficients are finite at s=0. We may extend K to its algebraic closure for the proof of nonexistence. No same-field normalization of a unit multiplying s^m is asserted here; after a finite field/parameter extension such a unit can also be absorbed, if needed.

The source has fixed total leaders A₁₅=H³, B₂₅=H⁵, H=p²(p³+g³), odd A,B and zero constants. Positive-order coefficients have degrees at most13 and23. All source coefficients lift ordinarily under

    φ(g)=v⁻¹,   φ(p)=v⁴u−v−v⁻¹.

Write x=[gp²]A, y=[p³]A, e=[p]B. The accepted saturated low equations on a genuine domain arc are

    [p]A=0,       9e=5kx,       x²=3ky.

At a generic boundary center put h=t₀+3≠0. The accepted field classification gives A₀=R₀³+αR₀ and B₀=R₀⁵+βR₀³+γR₀. The first low equation gives α=0; e₀=0 gives γ=0. Remove βA, or equivalently keep this harmless polynomial target term in the calculations below. Here

    R_t=p⁵+g³p²+(t+3)gp²+t p³−(t+3)p,
    S=∂_tR_t=p(p²+gp−1).

Thus y₀=−h³ is a unit. The low equations force m=2n, ord_s(x)=n and ord_s(e)=3n. The target Jacobian begins at order3m=6n.

There is a unique t(s) with t(0)=t₀ and y(s)=−(t(s)+3)³, obtained recursively by dividing the unit3h². Put R_s=R_{t(s)} and F=A−R_s³. This is a reference choice, NOT a source automorphism or a replacement s↦s^j. The source bounds give:

* F₀=0; every coefficient is odd, ordinary, degree≤13 and of receiver-origin order≥3;
* [p]F=[p³]F=0 and [gp²]F=x, because R_s³ is divisible by p³;
* F≠0; if j=ord_s F, then 1≤j≤n;
* since j<m, the moving weight3 face is absent at this coefficient. The fixed weight3 face cancels, so w(F_j)≤1 for w(g)=5,w(p)=−7.

## 2. A uniform localized-centralizer lemma

In K[g,p,R₀⁻¹][[s]] define the formal root

    X=A^(1/3)=R_s(1+F/R_s³)^(1/3),       X₀=R₀.

No polynomiality of X is assumed. Let ν be receiver-origin order, extended to rational functions by ν(f/q)=ν(f)−ν(q). Let δ be total degree at infinity, similarly extended. Since ν(R₀)=1, every coefficient of R_s and its positive variation has ν≥1. Its positive variation has total degree3 rather than5. Binomial expansion, including the expansion of negative powers of R_s, therefore gives:

    ν(X_d)≥1,        ν((X⁵)_d)≥5;
    δ((X⁵)_d)≤23 for d>0.

For the second bound, a term with ℓ≥1 copies of F has degree≤25−2ℓ; a positive coefficient of R_s⁵ replaces at least one degree5 factor by S of degree3. Inverse expansions only lower that bound. Similarly positive X coefficients have degree≤3. All these are coefficientwise bounds, not convergence assertions.

The accepted polynomial centralizer of R₀ is K[R₀]. Indeed deg R₀=5 is prime and H is not a fifth power of a linear form, so the common-generator theorem leaves no proper generator. Clearing powers of R₀ gives the localized centralizer K[R₀,R₀⁻¹]. The imported input is Arzhantsev–Petravchuk, Lemmas4–5, p5, [primary PDF](https://arxiv.org/pdf/math/0608157v2); its earlier charged closed-generator consequence is used, not a new classification import.

Induct on coefficient order d<6n in the equation [A,B]=0 modulo s^(6n). Subtract X⁵ and already obtained scalar-series multiples of A and X. The first remaining coefficient Z_d centralizes R₀: the leading bracket is 3R₀²[R₀,Z_d]. It lies in the localized ring. Moreover ν(Z_d)≥1, because B has zero constant, X⁵ has origin order≥5, A has order≥3 and X has order≥1. Also δ(Z_d)≤23, and it is odd. For a nonzero Laurent polynomial h(R₀), its lowest exponent is its origin valuation and five times its highest exponent is its degree. Hence the ONLY possible monomials of h are R₀ and R₀³. There is no negative or constant kernel. Induction proves scalar β(s),γ(s) with

    B=X⁵+β(s)A+γ(s)X  (mod s^(6n)).                 (C)

This is the point at which the no-linear-A condition is essential: without it, coefficients of the cube root can have negative origin order. The checker exhibits A=g³+sp, whose first cube-root correction is p/(3g²).

Before the first nonzero γ coefficient, (C) shows that B's linear part is just that coefficient times the linear part −hp of X₀. Neither X⁵ nor βA has a linear part. Since e and the prescribed B_g vanish below3n, it follows that ord_s γ≥3n. This uses only the leading linear part of X, not an asserted polynomial X_p series.

Now X−R_s starts at order j. Thus γ(X−R_s) starts at≥3n+j. From (C), after subtracting the POLYNOMIAL βA+γR_s, every X⁵ coefficient of order

    d < min(6n,3n+j)                                 (P)

is polynomial in g,p. In particular this holds through d=7j/2 whenever that integer is needed: j≤n gives 7j/2<3n+j and<6n. All intermediate orders are retained.

## 3. Leading divisibility and a strict transverse remainder

At order2j the first possible pole of X⁵ is (5/9)F_j²/R₀. By (P), R₀ divides F_j². For h≠0 write R₀=pT, where

    T=p⁴+g³p+hgp+t₀p²−h.

T is absolutely irreducible: after dividing by p, its monic cubic in g over K((p)) has constant p-adic valuation−1. An integer-valuation Laurent root with valuation≥0 has a unique lowest constant term; one with valuation≤−1 has a unique lowest cubic term. Thus it has no root, and the cubic is irreducible. Primitivity follows from T mod p=−h. Consequently R₀ is squarefree. Therefore

    F_j=R₀C₀,

where C₀ is nonzero, even, degree≤8, weight≤0, C₀(0)=0 and [p²]C₀=0. It is ordinary: φR₀ has v-order0 with leading3u, so a negative-v leading coefficient of φC₀ could not disappear in the product φF_j.

Crucially, T does NOT divide C₀. If C₀=TQ, degree Q≤4 and weight Q≤−8, and Q is even. Its only possible slots are p²,p⁴,gp³. Write Q=a p²+b p⁴+c gp³. The negative lift coefficients of Q at v⁻⁴,v⁻² are respectively b−c and a+4b−3c. Since φT has v-order1 and first coefficient−3u, ordinaryness of φC₀ forces b=c,a=−b. Thus

    Q=b p²(p²+gp−1),  C₀=bR₀S,  F_j=bR₀²S.

But [p³]F_j=−b h² and is zero by the moving reference, so b=0, a contradiction. This leading argument uses the actual source/lift bounds. No such bounds will be assumed for later division coefficients.

Perform monic division in p by R_s (monic degree5) coefficientwise over K[[s]][g]:

    F=s^j R_s C(s)+s^q D(s),                         (D)

where C(0)=C₀ and, if q is finite, q>j and D₀=D(0) is a nonzero remainder of p-degree<5 modulo R₀. If the remainder is identically zero take q=∞ and omit D. This division asserts only polynomial-series existence and the leading remainder. It does NOT assert preserved source weight, ordinaryness or degree for later C(s),D(s), and makes no chart change.

## 4. The first Newton balance, with nonmultiple orders included

Expand X⁵=A^(5/3) using (D). The quadratic terms are

    (5/9)s^(2j)R_s C² +(10/9)s^(j+q)CD +(5/9)s^(2q)D²/R_s.

The first two cubic terms are

    −(5/81)s^(3j)C³/R_s −(5/27)s^(2j+q)C²D/R_s².

The other cubic terms start at j+2q and3q; terms of binomial order≥4 start at4j. The first possible pole is at min(2q,3j), within (P).

If 2q<3j, polynomiality forces R₀|D₀², hence R₀|D₀, impossible for the nonzero remainder. If 3j<2q, including q=∞, it forces R₀|C₀³, hence T|C₀, excluded above. The only remaining case is

    2q=3j,    j even,    q=3j/2.

Thus the genuine mixed square/cube cancellation is permitted; it has not been suppressed. This is consistent with the previously charged R=g toy commuting through order6 and failing at7.

## 5. The next pole is uniform, not an order-by-order enumeration

Put a=j/2, L=7j/2 and

    M(s)=(5/9)D(s)²−(5/81)C(s)³.

Up to order L, the preceding expansion is exactly a polynomial series plus

    s^(3j) M(s)/R_s −(5/27)s^L C(s)²D(s)/R_s².       (E)

All omitted nonlinear terms start at4j>L. The coefficients of every displayed C,D,R_s remain unrestricted; this includes all intermediate/nonmultiple orders and moving-reference derivatives.

Polynomiality at orders3j,…,L−1 implies COEFFICIENTWISE

    M(s)=R_s W(s)+s^a N(s),

with polynomial W through order a−1 and polynomial N. This follows from monic division, or recursively subtracting each polynomial coefficient of M/R_s. It is NOT an assertion of global exact divisibility of M by R_s. It packages every earlier moving-denominator derivative into the previous polynomial W. At order L the sole remaining rational contribution is

    N₀/R₀ −(5/27)C₀²D₀/R₀².

Consequently R₀|C₀²D₀. The already imposed coefficient at3j gives R₀|9D₀²−C₀³. Reducing these two identities in the domain Kbar[g,p]/(T) forces C₀=D₀=0 there. In particular T|C₀, contradicting §3.

This proves the stated uniform finite-arc obstruction. It also identifies exactly why earlier unrestricted tangent rigidity was false: square/cube residues can balance, but the next double pole and the leading source-specific ordinaryness condition cannot both be satisfied. No unreviewed finite jet is used to infer an arc.

## 6. Evidence, dependencies and remaining boundary

Ten capped normal/−O controls pass; output bytes agree and the checker has zero Assert nodes. Actual mutations remove a moving-reference cross term, change the cubic multiplicity, omit a negative lift row, or omit the origin bound; each fails its named verifier. The small mixed toy has exact bracket2835s⁷p⁶. It is NOT an actual-source ramified survivor (the prior source realization has x=0). The controls verify bookkeeping and indispensable hypotheses, not the complete theorem or a large source expansion.

Witness SHA256: `53669df2e4c5b79023b466d53d484140fa0eaac87e643a53fad197419e431f44`. Replay with `python3 -B box/d125-uniform-ramification-discriminator-20260907/check.py` and its `-O` variant; `--record` is an exclusive-output producer, not an overwrite replay. Inputs/owned files are pinned in custody. Whole named terminal source/classification/low and prior pole reports were read; no live gate bytes were consumed. Polynomial centralizer is an explicitly imported theorem; the new uniform kernel/valuation and remainder arguments require their own different-model review.

The open logical boundary remains material: no theorem here forces a guarded point to admit a finite k→0 arc with generic center. The exceptional t₀=−3 boundary, infinity and existence of degeneration remain unhandled. No full ideal construction, solver, AWS/SSH/CAS, source-coordinate reduction or production change occurred. All commands used −B with bytecode disabled before helper import. All writers idle at publication. **STOP/IDLE.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12280`.
- Body SHA-256:
  `6b4305a9b1ad6fe7bd36bff282e8285394013825e559d77fc99ba343c8453708`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
