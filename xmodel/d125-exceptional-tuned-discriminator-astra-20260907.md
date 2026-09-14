# D125 tuned exceptional center: a polynomial uniform obstruction

2026-09-07. **DESK PASS, PROVISIONAL pending independent review.** No genuine finite field-coefficient arc of the accepted moving-face source can have t₀=−3, α₀≠0 and Δ₀=γ₀−β₀α₀+5α₀²/9=0. The proof uses a polynomial identity and a finite reference-normalization induction, not a formal inverse or an assumption that intermediate orders vanish. The α₀=γ₀=0 pure center remains outside the theorem. No degeneration-existence, guarded-emptiness or JC2 conclusion follows.

This tuned-only statement starts from accepted14c source,14f classification/centralizer/critical-fiber input and14g low equations. It does not depend on the live exceptional-center gate or on its provisional Δ₀≠0 theorem. The latter terminal producer was read for the already derived cubic quotient lemma, which is reproved here. The now-accepted generic uniform theorem is not a premise either. Root supplied the critical-fiber seed; this lane replaced the inverse-series proposal by the polynomial identity and checked the full scalar-reference bookkeeping.

## 1. Literal arc and a reference fixed by the p³ coefficient

Let K have characteristic zero. Suppose every receiver coefficient is finite in K[[s]], all full source Jacobian and ordinary-lift rows hold, and k(s) is nonzero of finite positive order m. Its inverse is required only over K((s)), not at s=0. The theorem permits an arbitrary leading unit of k(s). Set

    R=R_{−3}=p²(p³+g³−3p),       S=p(p²+gp−1).

At the classified tuned center,

    A₀=R³+α₀R,
    B₀=R⁵+β₀R³+γ₀R,
    α₀≠0,   γ₀=β₀α₀−5α₀²/9.

The exact low equation gives [p]A=0. R has origin order3 and p³ coefficient−3. Define, over the SAME field,

    α(s)=−[p³]A/3,
    F=A−(R³+α(s)R).

Then F₀=0, every F coefficient is odd and ordinary, its degree is≤13 and weight w(g)=5,w(p)=−7 is≤3, and

    [p]F=[p³]F=0,        [g²p]F=k(s).

The degree bound uses the fully fixed total face A₁₅=H³ and oddness. Thus F is nonzero, and j=ord_s F satisfies 1≤j≤m. This is a literal reference choice, not a source automorphism or a reparametrization s↦s^j. No “first tangent” is assumed removable.

Let β(s),γ(s) initially have their stated constant terms, with later coefficients to be selected as references. Define scalar-polynomial expressions

    a_s=3R²+α(s),
    q_s=5R²/3+β(s)−5α(s)/9,
    δ_s=γ(s)−β(s)α(s)+5α(s)²/9,
    G=B−(R⁵+β(s)R³+γ(s)R)−q_sF.

G₀=0. Each positive coefficient of G is an odd polynomial of degree≤23: q_sF has degree≤10+13 and the total B₂₅ face is fixed. The reference choices never change A or B.

## 2. Exact polynomial identity, with the cross term retained

For arbitrary F,G and arbitrary scalar series α,β,γ,

    [A,B] = [R, a_sG−δ_sF−(5/3)R F²] + [F,G].      (I)

Indeed, if f(z)=z³+αz and b(z)=5z⁴+3βz²+γ, then

    b(R)=a_s q_s+δ_s,       q_s'=10R/3.

Expanding [f(R)+F, R⁵+βR³+γR+q_sF+G] gives a_s[R,G]−δ_s[R,F]−q_s'F[R,F]+[F,G], which is (I). The −5/3 factor and the nonzero cross bracket are checked directly on small formal R=g polynomials with moving scalar series.

The full target bracket has order3m. All coefficient equations used below lie at orders≤2j<3m. The term [F,G] is never discarded as an identity; it drops from a specific coefficient only after its valuation is proved larger.

## 3. Source-specific zero lemma

Put a₀=3R²+α₀. Suppose a coefficient polynomial Z has the same oddness, degree≤13, weight≤3, ordinaryness and zero p,p³ coefficients as F_j. If

    Z=cR+a₀U,                                      (Z)

then Z=0. Here coefficients may be extended to Kbar for this lemma.

Degree and weight of the product force U odd, degree≤3 and weight≤1. These bounds alone leave only U=u₁p+u₃p³+u₁₂gp². No lower polygon inequality is inferred through division. Under the exact lift

    φ(g)=v⁻¹,    φ(p)=v⁴u−v−v⁻¹,

φ(R)(u,0)=3u, so the leading v⁰ coefficient of φ(a₀) is 27u²+α₀≠0. Ordinaryness of Z−cR therefore forces φ(U) ordinary. Its COMPLETE negative rows are

    −u₃+u₁₂=0,       −u₁−3u₃+2u₁₂=0.

Thus U=dS. Its p coefficient in a₀U is−α₀d; [p]Z=0 and α₀≠0 give d=0. Then [p³]Z=−3c=0 gives c=0. The two low-reference constraints are independent and both are checked. No squarefreeness of R is involved.

One useful consequence is: if δ is a nonzero scalar and

    a₀V−δZ=h(R),

then Z=0. Reduce the odd scalar polynomial h(z) modulo the even quadratic3z²+α₀: the remainder is λz, yielding (Z) by polynomial division. This is a fixed-field-unit calculation, not division by an unknown source parameter.

## 4. Reference-kernel removal, retaining every intermediate order

The polynomial centralizer of R is K[R]. This is the already accepted characteristic-zero common-generator theorem plus prime degree5 and the non-power total top H; R need not be squarefree. The imported primary is Arzhantsev–Petravchuk, [Lemmas4–5 p5](https://arxiv.org/pdf/math/0608157v2), at the previously charged external-theorem trust.

When a coefficient equation says [R,a₀G_ℓ]=0, it follows that G_ℓ∈K[R]. Its oddness and degree≤23 leave G_ℓ=ηR³+θR. Remove that coefficient by changing ONLY the references

    β(s)→β(s)+ηs^ℓ,       γ(s)→γ(s)+θs^ℓ.

The exact changes, not approximations, are

    G→G−ηs^ℓR³−θs^ℓR−ηs^ℓF,
    δ_s→δ_s+θs^ℓ−ηs^ℓα(s).                         (K)

The last G term starts at ℓ+j. In particular, a kernel removed at order j DOES change G at2j and δ_j; these terms remain in the argument below.

First remove G₁,…,G_(j−1). At each step the F terms start later, lower G coefficients have been removed, and (I) gives precisely the centralizer equation. This fixes the reference coefficients β,γ below j and hence δ below j. The assumption δ₀=0 is retained.

Suppose δ has a first nonzero coefficient δ_d at some d<j. Remove G_j,…,G_(j+d−1) in the same way; the δF term has not started yet. These reference changes have order≥j and cannot alter δ_d. At order j+d, (I) becomes

    [R, a₀G_(j+d)−δ_dF_j]=0.

The quadratic term starts at2j>j+d; [F,G] also starts later because the lower G coefficients are zero. The consequence of §3 forces F_j=0, contradiction. Therefore a genuine arc must have δ_s of order≥j after this reference normalization.

Now remove G_j,…,G_(2j−1). At each step δF and F² start at2j and the lower G coefficients vanish; the centralizer equation applies. Changes (K) preserve the vanishing of δ below j. They may change δ_j and G_(2j), and BOTH are retained. Thus the construction yields

    ord_s δ_s≥j,        ord_s G≥2j.

This finite procedure includes every intermediate/nonmultiple order. It does not assume that common-generator motion was absent, that δ_j is zero, or that the reference changes preserve some new source chart: the actual A,B were never changed.

## 5. The order2j critical-fiber contradiction

Take coefficient2j in (I). Since [F,G] starts at≥3j, and all lower G coefficients are zero, the exact equation is

    a₀G_(2j)−δ_jF_j−(5/3)R F_j²=h(R).              (Q)

This follows from the polynomial centralizer. No derivative of a moving critical root is omitted: α(s)'s positive coefficients multiply already-zero earlier G coefficients. The moving scalar kernel δ_j remains as the linear-F term.

Over Kbar choose r≠0 with3r²+α₀=0. Each R−r is absolutely irreducible, including at this exceptional center. Indeed, dividing by p² gives the cubic in g

    g³+p³−3p−r p⁻².

A root in Kbar((p)) would have valuation−2/3, impossible in that Laurent-series field. A cubic without a root is irreducible. The original polynomial is primitive over Kbar[p], because its constant coefficient modulo p is−r. Gauss's lemma proves the claim. This is also the accepted14f critical-fiber argument, specialized explicitly; no theorem on the repeated zero fiber is inferred.

Reducing (Q) in the integral domain Kbar[g,p]/(R−r) gives a scalar quadratic equation for F_j, with nonzero leading coefficient−5r/3. It splits over Kbar, so F_j is a scalar there. The same holds on R+r. Oddness under (g,p)→(−g,−p) makes the two constants opposite. Hence there is a scalar c with

    F_j−cR divisible by both R−r and R+r.

The two factors are coprime, so F_j=cR+a₀U. Section3 then gives F_j=0, contradicting its definition. This proves the tuned exceptional-center finite-arc obstruction for every finite m, without enumerating ramification orders.

## 6. Scope, evidence and stop

The hypothesis α₀≠0 is essential to this argument: it supplies nonzero critical roots and the low-A scalar pivot. The α₀=γ₀=0 pure center, its possible repeated-factor behavior and its negative-origin cube-root countercontrol are NOT resolved here. Untuned centers are assessed by the separate producer/gate; its promotion is not assumed for this theorem. There remains no result forcing a guarded point to admit any finite k→0 degeneration. No guarded-source or JC2 conclusion is drawn.

Ten capped normal/−O controls pass with identical rational-string witness bytes and zero Assert nodes. Genuine mutations change the quadratic factor, omit a nonzero [F,G], omit the actual −ηs^ℓF reference correction, or omit the p³ reference condition. The checker expands only actual degree≤5 factors and cubic lifts, plus formal R=g identities. No actual R³,R⁵,R²S, degree15/25 pair, full source or large matrix is expanded.

Witness SHA256 `dbbcf4b8beb0578d49bc5de6aa426275cdfacbfd613abe5b9e09ffa0f0d56373`. Replay ordinary/−O `python3 -B box/d125-exceptional-tuned-discriminator-20260907/check.py`; `--record` writes exclusively and is not an overwrite replay. Exact dependencies and owned bytes are pinned in custody. The bounded history check found the already accepted unramified quadratic interface; the claimed delta is the polynomial uniform reference argument, not new notation for that old result. The new theorem requires its own different-model review. No live gate read, AWS/SSH/CAS, solver, full builder, shared edit, new agent or further generation occurred. All writers idle at handoff. **STOP/IDLE.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10451`.
- Body SHA-256:
  `cc0561a9a74bfc35675c0c3139c51eea3b145491008cf8ba853fc412f27e29ef`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
