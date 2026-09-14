# D125 exceptional-center discriminator: independent Fable hostile gate

2026-09-07. Gate on `xmodel/d125-exceptional-center-discriminator-astra-20260907.md` (body `9c9645d7…`, producer `3c9aee52…`, terminal 06:17:36) and its `check.py`. Frozen inputs only, pinned in `box/d125-exceptional-center-gate-fable5-20260907/input_pins.sha256`; no live peers, ledgers, protected tree, network, AWS, SSH, CAS or solver. The producer checker was NOT executed (its helper `box/d125-zero-k-deformation-discriminator-20260907/check.py` is absent from the frozen set). Accepted 14c/14f/14g rows and the imported Arzhantsev–Petravchuk centralizer are treated as dependencies, not re-litigated. No dependence on the generic uniform 14p result, the finite-jet or m=4 theorems, or any live gate.

## Verdict table

| item | verdict |
|---|---|
| 1. Claim as scoped: over any char-0 field K, every arc A,B∈K[[s]][g,p] of the full odd moving-face source with k(s)≠0 of order m≥1 and centre (R³+αR, R⁵+βR³+γR), R=R_{−3}, has Δ₀=γ−βα+5α²/9=0 | **CONFIRMED** at exactly that scope; it is a finite-arc necessity, not a new equation on the guarded source, not exceptional closure, not existence, not JC2 |
| 2. Scalar pivot b=a(5z²/3+β−5α/9)+Δ₀, K[R] centralizer, odd remainder λz, Bezout A_ℓ=cR+a(R)U, cancellation to B_ℓ=b(R)U+dR+f₃R³ | **CONFIRMED**, every step replayed by hand and by own control G1–G4 |
| 3. U support {p,p³,gp²} from deg≤3, weight≤1, odd only; ordinariness via the v⁰ coefficient 27u²+α; rows (0,−1,1),(−1,−3,2); U=qS; low coefficients −αq, −γq; q=0 on both Δ₀≠0 branches | **CONFIRMED** (G5–G8) |
| 4. Induction ℓ=1..m with all orders retained, target order 3m>m, contradiction at ℓ=m via [g²p]R=0 | **CONFIRMED** (G9) |
| 5. Whole βA shear invariance of Δ₀ | **CONFIRMED** (G2, formal λ) |
| 6. Boundary counter-control k≡0, A=R³+sR, B=R⁵, X₁=1/(3R), origin valuation −3 | **CONFIRMED** as stated; it claims no guarded arc and copies no squarefree lemma (G10) |
| 7. Producer controls | **PARTLY VACUOUS**: the low-A/low-B "obstruction" controls are literal tautologies, and the tangent toy uses U=p³+gp², not S; see §4 corrections. Mathematics unaffected |
| 8. Tuned Δ₀=0 (α≠0) and pure α=γ=0 strata remain open; no generalization | **CONFIRMED** as a correctly typed stop |

No exit-price claim is made here, so no charge basis is declared.

## 1. Scope check

The source rows used are exactly: fixed total faces A₁₅=H³, B₂₅=H⁵ (hence deg A_ℓ≤13, deg B_ℓ≤23 for ℓ≥1 by odd parity), the A polygon weight(5,−7)≤3 with weight-3 slots (2,1),(9,6) only and A(2,1)=k(s), oddness, all Jacobian rows, all A-negative lift rows, and the 14g saturated low rows a01=0, 9e=5k·a12, a12²=3k·a03. Over the domain K[[s]] with k≠0, the 14g certificates k²a01=−(9/5)r₀ etc. give a01=h1=h2=0 identically; this is the only use of low saturation and it introduces no inverse of k. At the centre, [gp²]A₀=α[gp²]R=0 and [p³]A₀=−3α, so x₀=0, y₀=−3α, e=[p]B has order ≥m+1. All of this matches the report's §1 table.

## 2. Step-by-step attack

**Scalar identity.** a(5z²/3+β−5α/9)=5z⁴+3βz²+αβ−5α²/9, so b minus it is γ−αβ+5α²/9=Δ₀ (G1, α,β,γ all formal). Under B→B−λA, β→β−λ, γ→γ−λα, and Δ₀ is unchanged (G2). No β term is deleted without its γ correction.

**Centralizer.** [R,F]=0 gives F∈K[S] for a closed S with R=F₀(S). deg S divides 5; deg S=1 would make H=p²(p³+g³) a fifth power of a linear form, false (p-multiplicity 2). So deg S=5, R affine in S, K[S]=K[R]. Squarefreeness of R is never used; the p² factor is irrelevant here. Same external trust as 14f.

**First-order relation.** For ℓ≤m the s^ℓ coefficient of −5k³g²/9 is zero (order 3m>m). With A_i,B_i∈K[R] for 0<i<ℓ, cross brackets vanish, and [A₀,B_ℓ]+[A_ℓ,B₀]=a(R)[R,B_ℓ]−b(R)[R,A_ℓ] since [F(R),G]=F′(R)[R,G]. Hence [R,a(R)B_ℓ−b(R)A_ℓ]=0 and a(R)B_ℓ−b(R)A_ℓ=f(R). Parity: a,b even, A_ℓ,B_ℓ odd, R odd, R transcendental over K, so f is odd; its remainder modulo the monic-up-to-3 even quadratic a is odd of degree ≤1, i.e. λz, λ=0 allowed (G4). Reduction in K[g,p] modulo the ideal (a(R)) with b(R)≡Δ₀ and f(R)≡λR gives −Δ₀A_ℓ≡λR, so A_ℓ=cR+a(R)U with c=−λ/Δ₀; only the scalar units Δ₀,3,9 of K are inverted, no base change. Substituting, a(R)([R,B_ℓ]−b(R)[R,U])=0 and a(R)≠0 in the domain K[g,p] gives [R,B_ℓ−b(R)U]=0, so B_ℓ−b(R)U=h(R) odd of degree ≤23, h=dz+f₃z³. CONFIRMED.

**U enumeration.** deg a(R)=10, top weight w(a(R))=2 (w(R)=1 from g³p²), weights add in a domain. deg(A_ℓ−cR)≤13 and w(A_ℓ−cR)≤3 force deg U≤3, w(U)≤1, U odd. The only monomials are p, p³, gp² (G5); g²p has weight 3 and is excluded. No lower-edge (i≤2j) inequality is transported through the division, so the α=0 lower-edge change of a is irrelevant. CONFIRMED.

**Ordinariness.** φ(A_ℓ) and φ(cR) are polynomial (lift rows are linear in the s-coefficients; φ(R) is ordinary with v⁰ coefficient 3u, G7 by the degree-5 lift of R). φ(a(R))=3φ(R)²+α has v⁰ coefficient 27u²+α, a nonzero element of K[u] for every α including α=0; a negative lowest v-power n of φ(U) would give the uncancelled term (27u²+α)c_n(u)v^n in φ(a(R)U). K[u] domain cancellation is exactly what is used; no constant unit is assumed. The complete negative parts are φ(p)∋−v⁻¹, φ(p³)∋−v⁻³−3v⁻¹, φ(gp²)∋v⁻³+2v⁻¹ (G6), so u₁₂=u₃, u₁=−u₃, U=qS with S=p³+gp²−p. CONFIRMED.

**Low coefficients.** R²S, R⁴S and R³ have origin order ≥7, so [p]A_ℓ=α q[p]S=−αq and [p]B_ℓ=−γq (G8, by order bookkeeping, no R²S expansion). α≠0: a01≡0 forces q=0. α=0: Δ₀=γ≠0 and e_ℓ=0 for ℓ≤m force q=0. Then A_ℓ=cR, B_ℓ=dR+f₃R³, closing the induction. At ℓ=m, [g²p]A_m=k_m≠0 but [g²p]R=0 (G3/G9). No reparametrization, no discarded intermediate order. CONFIRMED.

## 3. Boundary counter-control

k≡0, A=R³+sR, B=R⁵ is the classified family with α=s, β=γ=0 fibrewise; faces, ordinariness, zero bracket and the low rows hold ([p]A=[gp²]A=[p]B=0 by origin order, G10). (g+sX₁)³=g³+sg gives X₁=1/(3g), valuation −1 in R, −3 at the origin. The report uses it only to show that "no linear A" does not force positive origin valuation of cube-root corrections at this centre, states that k≡0 neither bypasses the theorem nor yields a ramified guarded survivor, and does not transfer squarefreeness. CONFIRMED as written. The tuned toy A₁=p³, B₁=(5g²/3−10/9)p³ at (2,0,−20/9) commutes to first order because (aq−b)[g,F]=0 with q a function of R=g; it is a bracket-interface toy only and the report says so; it says nothing about source ordinariness.

## 4. Producer checker audit and named corrections

Read, not run. Substantive computations: scalar remainder (γ=7 fixed, α,β formal), R coefficients and origin order, U slot census, the two negative lift rows and kernel, the formal R=g tangent identity, the tuned toy. Corrections:

- **C1 (low-A/low-B controls are tautologies).** `lowA(value)` returns `value==0`; the test `lowA(Q(0)) and not lowA(Q(-2))` never computes [p](a(R)S); −2 and −5 are literals. The §6 sentence "omit the actual low-A or low-B constraint" over-describes them. The mathematical claim (3) is nevertheless correct (G8 here derives it from [p]S=−1 and origin orders; the mutation with S lacking its −p term is rejected).
- **C2 (tangent toy does not test U=S).** It uses U=p³+gp², which is not ordinary; as a formal R=g bracket identity that is legitimate, but it exercises no lift content.
- **C3 (trivial gates).** `need(-3<1,…)` and the X₁ line `3g²·(1/3g)=g` are arithmetic tautologies; they should not be counted among the "twelve" as evidence.
- **C4 (labels).** §1 "R is NOT squarefree, and no squarefree inference is used" is accurate; §2 should say the K[R] conclusion uses deg S | 5 and the non-fifth-power top, as 14f does.
- **C5 (14f label).** The upstream classification's field part is promoted per the low-jet gate; the report cites it as "accepted", consistent.

Typed gaps, none charged to the theorem: **GAP-HELPER** (producer helper absent, checker not replayed here; its witness hash `ccf4b975…` unverified); **GAP-TRANSACTION** (root `c4a5499a…` not in the frozen set); **GAP-LEMMA4** external trust as in 14f.

## 5. Own controls

`box/d125-exceptional-center-gate-fable5-20260907/gate_controls.py`, stdlib only, `-B`, zero Assert nodes, ten gates G1–G10, run normal and `-O` under 30 s wall / 25 s CPU / 512 MiB. Witness `out.json` = `out-O.json`, SHA256 `7883cffee63edc3276933f72797fc8714fa53efafa9a80d55332ff0e88b774be`. Six mutations fail at the named gate in both modes: delta sign (G1), shear without the γ correction (G2), even f (G4), omitted v⁻³ lift row (G6), R without −3p³ (G7, φ non-ordinary), S without its −p term (G8). Actual expansions: R, S (degree ≤5), cubic U lifts, one degree-5 lift of R; no R²S, R³, R⁵, A₁₅/B₂₅ or full source. Pins: `own_artifacts.sha256`, `run_log.txt`.

**Overall:** CONFIRMED at the finite-arc, field, t₀=−3 scope, with the five checker corrections above; the tuned α≠0,Δ₀=0 and pure α=γ=0 strata stay open exactly as the report types them. No promotion beyond these verdicts. **STOP/IDLE.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9534`.
- Body SHA-256:
  `433da2bf97ab8f7fc87567aab387b09a36130029f18fd17395c9567d1ac5d3b3`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
