# D125: the first ramified approach at a generic pure-power boundary point

2026-09-07. **DESK PASS, conditional on the queued low-row saturation review:** no full-source formal arc with finite coefficients, k=s², and generic pure-power center t≠−3 exists. The new independent ingredient is a first-tangent restriction from the Jacobian through order s³. Its composition with the sealed, still-provisional low-row lemma gives the contradiction. This does not exclude arbitrary raw truncated jets or all ramification orders, and does not imply guarded-source emptiness.

## 1. Exact hypothesis and equations used

Work over a characteristic-zero field K and K[[s]]. The generic point satisfies the accepted complete moving-face source, and every receiver coefficient is finite at s=0. The inverse guard extends only to K((s)); its inverse variable is not required to be finite. Put

    φ(g)=v⁻¹, φ(p)=v⁴u−v−v⁻¹,
    H=p²(p³+g³),
    R=R_t=H+(t+3)gp²+t p³−(t+3)p,  t≠−3.

The special pair is A₀=R³, B₀=R⁵+βR³. The constant WHOLE shear B→B−βA reduces it to pure powers. It preserves all faces: A's weight≤3 is strictly below B's inner weight5, and total degree15 is below25. The A polygon is contained in B's; origins and odd parity persist. On the lift, subtracting βφ(A) preserves every negative row, including the low ones. This is not deletion of a selected term or an assumption about the optional B₁₅ slice.

Expand A=R³+ΣsʳUᵣ and B=R⁵+ΣsʳVᵣ. All Uᵣ,Vᵣ are odd, vanish at the origin and lift ordinarily; deg Uᵣ≤13, deg Vᵣ≤23. With weight w(i,j)=5i−7j, U₁ has weight≤1, whereas U₂ has required leading term g²p of weight3. The moving B terms occur at s² and s⁴. The complete Jacobian target is −5s⁶g²/9, so its coefficients through s⁵ vanish. Only the coefficients through s³ will be needed below. No degree15/25 pair is expanded.

The imported centralizer fact is K[R]: Arzhantsev–Petravchuk, [math/0608157v2, Lemmas4–5, p.5](https://arxiv.org/pdf/math/0608157v2), at the same external-theorem trust as the promoted boundary packet. Prime degree5 and H's p-multiplicity2 exclude a fifth-power linear inner generator. The previously read primary statements and the whole terminal source/boundary proofs are retained as inputs; no new literature theorem or live gate was consumed.

## 2. Orders one and two: retain the genuine first motion

Order one gives

    3V₁−5R²U₁=f(R)=aR+bR³.

Order two gives [R,E₂]=0, where

    E₂=3R²V₂−5R⁴U₂−(5/3)R U₁²−(1/3)f'(R)U₁.

Thus E₂=h₂(R), h₂(0)=0. If a≠0, reduction modulo R gives R|U₁. If a=0, divide by R, evaluate at the origin to kill the scalar remainder, and reduce modulo R: R|U₁². Here R=pT is squarefree, with

    T=p⁴+g³p+(t+3)gp+t p²−(t+3).

Indeed T is irreducible even over Kbar: after dividing by p it is monic cubic in g, whose constant coefficient has p-adic valuation−1. An alleged Laurent-series root of integer valuation n≥0 leaves that constant as the unique minimum; n≤−1 leaves g³ as the unique minimum3n<n,−1. Thus there is no root, hence the cubic is irreducible over Kbar((p)); primitivity and Gauss's lemma give polynomial irreducibility. T mod p=−(t+3) is nonzero, so p and T are coprime.

Consequently U₁=RC, with C even, deg C≤8 and w(C)≤0. The actual degree-five lift has φ(R)(u,0)=3u. Therefore ord_v φ(R)=0, and ordinaryness of φ(U₁) implies ordinaryness of φ(C). Nothing here sets C to zero or assumes the first motion commutes with R.

When a≠0, divide E₂ by R and reduce modulo R again. This makes C scalar modulo R, hence modulo T. It remains to prove the corresponding statement when a=0.

## 3. Order three: the first motion is a boundary tangent

In the a=0 branch, the permitted WHOLE shear B→B−s(b/3)A removes b. Now

    V₁=(5/3)R³C,
    V₂=(5/3)R²U₂+(5/9)RC²+(ℓ/3)R+(m/3)R³.

The latter follows from E₂'s centralizer identity, parity and the degree bounds; no kernel term has been omitted. Direct differentiation gives the order-three Jacobian as [R,E₃], with

    E₃=3R²V₃−5R⁴U₃−(10/3)R²CU₂
          +(5/27)RC³−(ℓ/3)RC−mR³C.

Thus E₃=h₃(R). It is divisible by R, and division followed by reduction modulo R yields

    (5/27)C³−(ℓ/3)C = scalar  (mod R).

In particular this holds modulo the irreducible T. Over Kbar the scalar cubic splits, so the domain Kbar[g,p]/(T) forces C to be a scalar c modulo T.

Write C−c=TD. The exact bounds and parity imply D even, deg D≤4 and w(D)≤−8. Its ONLY possible monomials are p²,p⁴,gp³. Set D=p²(A+Bp²+C₀gp). The lift of T has first term −3uv, hence valuation1. The complete negative part of φ(D) is

    (B−C₀)v⁻⁴+(A+4B−3C₀)v⁻².

Since φ(TD) is ordinary, its valuation is nonnegative. Both displayed powers must vanish: B=C₀ and A=−B. Therefore, in both branches,

    C=c+dR R_t',      R_t'=p(p²+gp−1),
    U₁=cR+dR²R_t'.

Also D is divisible by p², so C(g,0)=c; consequently c∈K. The proportionality scalar d is likewise in K by its literal coefficient. This is a restriction proved from the full face/lift conditions and three Jacobian orders, not a normalization or an automorphism removing U₁.

## 4. Contradiction for a genuine k=s² arc

The separate low-row producer `57d85da3…` is still PROVISIONAL at this packet's cutoff; its active gate was not read. Its explicit polynomial certificates imply, in any domain carrying a full generic guarded point,

    a01=0,  9e=5kx,  x²=3ky,
    x=[gp²]A, y=[p³]A, e=[p]B.

This use needs only the certificates and cancellation of nonzero k, not a reducedness assertion about the boundary. At the present center x₀=0 and y₀=−(t+3)³≠0. Thus k=s² forces

    x₁²=−3(t+3)³≠0.

But U₁=cR+dR²R_t' has [p]U₁=−c(t+3) and [gp²]U₁=c(t+3): the degree-three contribution of R²R_t' is pure p³. The first equality and a01=0 force c=0; the second then gives x₁=0, a contradiction.

Only Jacobian orders1,2,3, the exact first-coefficient face/lift conditions, a01 through order1 and x²=3ky through order2 are needed after saturation. Order4 is unnecessary. In particular no potentially invalid removal of the boundary tangent is used.

This also excludes the corresponding three-jets of the k-saturated closure, with those low equations explicitly imposed. It does NOT prove that raw unsaturated full-source jets over K[s]/(s⁴) or K[s]/(s⁵) do not exist: nilpotent k=s² cannot be canceled there. A tiny actual countercontrol A=sp, B=5s⁴g/9 over K[s]/(s⁵) has zero Jacobian although A_p=s≠0; it demonstrates the cancellation error only, not a full-client jet. The known low-row ramified survivor likewise remains a low-row object, not a full-source survivor.

## 5. Verification, scope and stop

Ten capped stdlib runs pass normally/−O, with identical exact rational-string witnesses and zero Assert nodes. The same checker rejects a changed E₃ cubic factor, omission of the actual v⁻² kernel row, an independent gp² tangent term, and cancellation of nilpotent k in the explicit truncated control. Actual expansions stop at R degree5 and D degree4; the bracket identity uses only a tiny R=g toy. Witness SHA256 `37387ae526322c18c614502d78794a9b6be983b4afecf90ee3a58ffbb41618ec`.

The bounded history check covered the named terminal boundary/low-row reports and `APPROACHES.md`/`ladder/REDUCTION.md`. Existing unramified and unrelated ramified-client statements were found; no priority or exhaustive novelty claim is made. A first lookup of nonexistent root `REDUCTION.md` was corrected to the actual ladder path. Root supplied, during this task, the same T irreducibility and degree-four kernel bridge; the independent cubic identity and controls above were derived here.

The result is only generic t≠−3, pure-power center up to the whole β shear, and k=s². No statement is made about t=−3, higher ramification, coefficients escaping to infinity, an arbitrary point's having a finite boundary arc, or generic-fiber emptiness. Extending the tangent argument to a least departure of order j with a moving R_{t(s)} would require controlling all mixed and nonmultiple orders; that bridge is not proved. No source/build/solver change, performance claim, guarded point or JC2 consequence follows. All owned writers finish at custody publication. **STOP/IDLE.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8482`.
- Body SHA-256:
  `0a6a9c397d4d94d5066b121554fc189fb0bfe4d43e87a6744f50d114c580fc53`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
