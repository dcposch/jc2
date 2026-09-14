# Gate: odd D125 moving-face unit normalization (Fable 5.1, 2026-09-07)

Bounded 15-minute hostile delta gate of `xmodel/d125-parity-unit-normalization-astra-20260907.md` (6426 bytes, frozen copy) and its `check.py` (SHA `6c6e5067…`, byte-identical to the repository copy; client pin `ec2fa2d1…` re-hashed and matched). Scope is only the new normalization, assuming odd A/B total degrees and λ₂=0 directly inside the accepted complete unequal/Q source. The full lift contract and the c∈(λ₂,λ₃) lemma are consumed, not re-reviewed. No pending 22-coordinate theorem, live peer, CAS, AWS, solve or full-pair expansion was used. Producer `check.py` was not edited and was not re-run here; the coordinator's eight-control replay is taken as given.

## Verdict table

| item | verdict |
|---|---|
| 1. ℓ=λ₃ is a unit of the full quotient O₀ over every Q-algebra, nilpotents included; localize only after all negative and Jacobian rows | **CONFIRMED** |
| 2. coefficient maps, four moved faces, all other fixed faces and origins, λ̃₃=1, row factors ℓ^((5t−e−D)/2) and ℓ^((n−38)/2), wrong-parity rows zero | **CONFIRMED** |
| 3. O₀ ≅ N⊗_E D with inverse; D=E[T]/(T⁶−k⁻¹) free rank 6, finite étale, faithfully flat; properness and Q̄-point equivalence only | **CONFIRMED** |
| 4. zk−1 needed; no k≠0 from unguarded rows; physical transform descends, keeps 75/125, c=−5k³/9 nonzero on guarded field points; sufficient CE contract only | **CONFIRMED** |
| 5. cost statement: A-negative rows affine-linear in ã and k; 128 Laurent or 129 guarded coordinates; nothing measured | **CONFIRMED** as a statement |

No producer claim failed. Residual gaps are listed in §6; none is a defect of the delta.

## 1. Unit

Under g↦v⁻¹, p↦v⁴u−ℓv−v⁻¹ the monomial g^i p^j contributes u^t v^e with e=5t+2d−m, m=i+j, d the number of −ℓv factors. The coefficient [u⁰v¹] needs 2d=m+1, so d=(m+1)/2≥1 for every odd m; for even m there is no term at all, so divisibility by ℓ needs neither the parity hypothesis nor the origin. The chain rule with determinant +v² gives [P,Q]=c₀ in O₀[u,v^{±1}] once every Jacobian slot is imposed; extracting the constant term and using the t≤1 negative rows of both members gives c₀=P₁₀Q₀₁−P₀₁Q₁₀=ℓ(P₁₀s−rQ₁₀). This is an identity in the universal ring O₀, hence in every O₀-algebra, and ℓ⁻¹=M/c₀ with c₀=−5/9. Consequently O₀→O₀[ℓ⁻¹] is the identity. Dropping either row family breaks it: the accepted zero-lambda gate's toy has [P,Q]=c with a failing negative row, and the origin formula returns 0. So the producer's order "full rows first, then localize" is necessary, not stylistic. Controls C3 (chain rule, origin bookkeeping, P₀₁=Q₀₁=0 at ℓ=0) and C2 (127 [u⁰v¹] terms, all with d=(m+1)/2) agree.

## 2. Transport

Each lift row: contribution ratio new/old is ℓ^((m−D)/2−d)=ℓ^((5t−e−D)/2), independent of the slot, so L̃_(t,e)=ℓ^((5t−e−D)/2)L_(t,e) row by row, positive rows included. A pair a_ij b_kl has n=m_a+m_b−2, factor ℓ^((m_a−15)/2+(m_b−25)/2)=ℓ^((n−38)/2); n=2 gives ℓ⁻¹⁸=k³, sign preserved. Odd m forces every surviving row to even 5t−e−D and every Jacobian degree even; a row of odd 5t−e−D only receives even slots, which are zero on both sides. From the literal client, the nonzero fixed coefficients are thirteen, all on odd slots: A (0,15),(3,12),(6,9),(9,6) and B (0,25),(3,22),(6,19),(9,16),(12,13),(15,10) with exponent 0; A(2,1)→ℓ⁻⁶=k; B(8,5)→5k/3; B(1,0)→ℓ⁻¹²·5/9=5k²/9. The only even fixed slot is the origin, value 0, absent from the odd chart. Zero faces stay zero. The whole map is the total-degree dilation Ã(g,p)=τ⁻¹⁵A(τg,τp), τ²=ℓ, with (u,v)↦(τ⁵u,τ⁻¹v); odd parity is exactly the condition that every τ-exponent is even. An unchanged-face normalization cannot exist: (2,1),(8,5),(1,0) have τ-weights −12,−12,−24. Verified on a 7+9-monomial pair carrying all thirteen faces and nilpotent free coefficients: 133+350 lift rows and all 45 Jacobian rows scale exactly (C3).

## 3. Descent

φ: N⊗_E D→O₀, ã↦ℓ^((m−15)/2)a, b̃↦ℓ^((m−25)/2)b, ℓ↦ℓ is well defined only because ℓ⁻¹∈O₀ (§1); ψ with the inverse exponents is defined on Q[ℓ,a,b] and kills I₀ because each generator maps to a unit multiple of a transported generator, and conversely. Face constants agree (kℓ⁶=1 etc.). So O₀≅N⊗_E D as rings, including nilpotent structure. D=Q[ℓ^{±1}] is free over E=Q[k^{±1}] on 1,…,ℓ⁵ (ℓⁿ=k^{−q}ℓ^r, n=6q+r; C4 checks −13≤n≤13), equal to E[T]/(T⁶−k⁻¹); 6T⁵·(kT/6)=1, so the cover is finite étale and faithfully flat, also after base change to N. Hence N=0 iff O₀=0. A Q̄-point of O₀ restricts to one of N; a Q̄-point of N extends because Q̄⊗_E D=Q̄[T]/(T⁶−k₀⁻¹) has points (k₀≠0 as k is a unit of E). Correctly not claimed: O₀≅N, same-field lifting, or isomorphism of distinct k-fibres. The parameter is traded, not removed.

## 4. Presentation and counterexample contract

k is a face coefficient and the client guards GUARD/A/2/1 and GUARD/B/1/0 demand its inverse, so a polynomial presentation needs zk−1; the producer claims nothing about k≠0 from unguarded rows, and none is available: at k=0 the transported target is c̃=0, so that fibre could never feed the contract anyway. On a guarded field point of N, P̃=Ã(v⁻¹,v⁴u−v−v⁻¹) and Q̃ are polynomials by N's negative rows and [P̃,Q̃]=c₀k³ by the chain rule directly, no τ needed. Degree: t+e=6t+2d−m≤5j−i≤5D with equality only at (0,D), t=D, so degrees are exactly 75 and 125 with coefficient 1 (C3), neither dividing the other. The accepted sufficient contract applies; no point exists or is claimed.

## 5. Cost

At λ̃₃=1 the A-negative rows are Q-linear in ã with constant matrices; k enters only through (2,1) in rows (0,−3) and (0,−1). B rows carry k and k² through (8,5) and (1,0), Jacobian rows k³. Literal odd free slots: 33 A, 94 B, so 128 Laurent coordinates or 129 with z (C1). No fill, speed or authority follows, as the producer says.

## 6. Controls, gaps, custody

Producer `check.py` verifies exponent arithmetic on 13747 (slot,t,d) triples, which are rearrangements of e=5t+2d−m and cannot fail; six toy monomials per member, the four faces and the guard are its only substantive tests. It never exercises a bilinear Jacobian transport, the chain rule or the unit identity; those rest on the text, which I re-derived above. Own `gate_controls.py` (SHA `d123d57b…`, standard library, explicit frozen client path, ring Q[ε]/(ε²), ℓ=3+2ε): C1 census 33/94/156 and the thirteen fixed exponents; C2 all 156 odd single-monomial lifts, 13747 covariance rows, 127 [u⁰v¹] terms with d=(m+1)/2; C3 the 7+9 pair (rows, Jacobian, c₀ℓ⁻¹⁸=c₀k³, chain rule, origin bookkeeping, ℓ=0 vanishing, degrees); C4 rank-6 basis and unit derivative; C5 guard. Negative controls alter the (2,1) face to 1, the c-power to k², omit the guard, and put a nonzero coefficient on even slot (4,4); each exits 1 in normal and −O with its intended message, and the positive witnesses are byte-identical (`0dc1e2b8…`, `replay.json`). Positive run 9.9 s, 22 MB; mutations fail before the heavy loop. Caps 30 wall/25 CPU s, 512 MiB, zero Assert nodes.

Typed gaps, none charged to the producer: **GAP-HYP** odd parity and λ₂=0 are hypotheses, so nothing here transfers to the full source's Q̄-points until the separate parity theorem is gated. **GAP-FIBRE** no k-fibre of N is shown nonempty or empty; distinct k-fibres are not shown isomorphic. **GAP-PROPER** properness of N is untouched. No exit-price claim is made, so no charge basis is declared. Own artifacts only in `box/d125-parity-unit-normalization-gate-fable5-20260907/`. **STOP:** review only; no construction authority.

<!-- BODY-END -->
