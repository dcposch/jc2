# Gate: uniform finite-ramification obstruction at a generic boundary center (Fable 5.1, 2026-09-07)

Bounded 18-minute hostile gate of `xmodel/d125-uniform-ramification-discriminator-astra-20260907.md` (frozen SHA `94fa5194…`, whole text read) with its `check.py` (`1d65345a…`, read, NOT executed: its helper is absent by design), read from `/tmp/jc2-lane.RKguav/inputs` only, beside the parity normalization (`19f0394c…`), the zero-k classification (`129947ee…`) and its gate (`68e04e8c…`), the low-jet saturation report (`57d85da3…`) and its gate (`65bb46ee…`), the mixed-order countercontrol gate (`ad1a4ddb…`) and `FALLACY-v2.md`. Root's checker read, custody pins and transaction `c3966052…` are taken as given and are not proof authority. Accepted at their scopes: source14c, classification14f, low14g, the imported common-generator/centralizer theorem. Neither the six-jet existence nor the generic-m4 theorem is used as a premise here or by the producer. No CAS, AWS, SSH, solver, network, peer, ledger or live report; no R³, R⁵, R²S, A₁₅, B₂₅, full-jet or C³/C²D expansion on the actual source. All frozen bytes preserved; pins in the owned box.

## Verdict table

| item | verdict |
|---|---|
| 1. Hypotheses, low equations at the center (α=γ=0, y₀=−h³, m=2n, ord x=n, ord e=3n, target at 6n), moving reference t(s), F bounds: F₀=0, odd, ordinary, degree ≤13, origin ≥3, [p]F=[p³]F=0, [gp²]F=x, 1≤j≤n, w(F_j)≤1 | **CONFIRMED** |
| 2. Localized ring, valuations ν and δ, ν(X_d)≥1, ν((X⁵)_d)≥5, δ((X⁵)_d)≤23, δ(X_d)≤3, localized centralizer K[R₀,R₀⁻¹], kernel exactly {R₀,R₀³}, (C) through <6n, ord γ≥3n, (P) through <min(6n,3n+j) | **CONFIRMED** |
| 3. First pole (5/9)F_j²/R₀, T absolutely irreducible, R₀=pT squarefree, F_j=R₀C₀ with the stated properties, T∤C₀ via the three Q slots, rows (0,1,−1)/(1,4,−3), Q=bp²(p²+gp−1), [p³]F_j=−bh² | **CONFIRMED** |
| 4. Monic coefficientwise division (D), q>j, first pole at min(2q,3j), balance 2q=3j, (E) through L=7j/2 with every intermediate order, M=R_sW+s^aN, R₀∣C₀²D₀ and R₀∣9D₀²−C₀³, domain reduction, contradiction | **CONFIRMED** |
| 5. Scope, stop clauses, controls | **CONFIRMED**; two uncharged notes (§5) |

## 1. Hypotheses, moving reference, F bounds (item 1)

The special point of a K[[s]]-arc with k=s^m satisfies every unguarded k=0 row, so classification14f applies over K: A₀=R₀³+αR₀, B₀=R₀⁵+βR₀³+γR₀. The low-jet gate's literal values a01=−αh, e=−γh, a03=−h³+αt₀ with h=t₀+3≠0 give α=γ=0 and y₀=−h³, a unit. From x²=3ky and 9e=5kx in the domain K[[s]]: 2·ord x=m, so m=2n, ord x=n, ord e=3n; the target −(5/9)k³g² starts at 6n. The recursion (h+τ)³=−y(s) divides by 3h²≠0, so t(s) exists uniquely in K[[s]]; R_s=R₀+τS with S=∂ₜR_t=p(p²+gp−1) exactly (R_t is affine in t). It is a reference, not an automorphism or reparametrization.

F=A−R_s³: F₀=0 since α=0. Origin order: A has zero constant, no g slot (the A lattice 5i−7j≤3 excludes (1,0), weight 5), [p]A=0 on the arc, and odd parity kills degree 2, so ν(A_d)≥3 for d>0; p³∣R_s³ coefficientwise (p∣R₀, p∣S), so ν(F_d)≥3, [p]F=0, [gp²]F=[gp²]A=x. [p³]R_s³=(−(t(s)+3))³=y(s), so [p³]F=0. Degrees: A_d≤13 (fixed top face, odd), R₀^aS^b with b≥1≤13. Ordinary: A rows hold in K[[s]]; φR_t is ordinary for symbolic t and own C1 finds φS of v-order 1. F≠0 because [gp²]F_n=x_n≠0, so 1≤j≤n. Weight: odd A slots of weight 2 do not exist (5i−7j=2 forces i+j even), the weight-3 slots (2,1),(9,6) carry s^m and 1, absent at 0<j<m; positive R_s³ coefficients have weight ≤2−7=−5. So w(F_j)≤1. CONFIRMED.

## 2. Localized kernel and (P) (item 2)

ν (order at the origin) and δ (total degree) are valuations on the domain K[g,p], hence extend to K[g,p,R₀⁻¹] by the quotient rule; ν(R₀)=ν(S)=1, δ(R₀)=5, δ(S)=3. R_s^{−a}=R₀^{−a}(1+τS/R₀)^{−a} has s^i-coefficients R₀^{−a−i'}S^{i'} with ν=−a and δ=−5a−2i'≤−5a. For the term F^ℓR_s^{5−3ℓ}: ν≥3ℓ+5−3ℓ=5 and δ≤13ℓ+25−15ℓ=25−2ℓ≤23 (ℓ≥1); ℓ=0 at d>0 gives δ=25−2i≤23. Same computation gives ν(X_d)≥1 and δ(X_d)≤5−2ℓ≤3. X is odd because σ(F/R_s³)=F/R_s³. All coefficientwise, as stated.

Centralizer: [R₀,f/R₀^a]=R₀^{−a}[R₀,f], so the localized centralizer is K[R₀,R₀⁻¹] given the accepted K[R₀]. Induction: with B'=B−X⁵−β_{<d}A−γ_{<d}X, the identities [A,X⁵]=[A,X]=0 (A=X³ formally) and scalar β,γ give [A,B']=[A,B]≡0 mod s^{6n}; B'≡0 mod s^d by the hypothesis, so 3R₀²[R₀,Z_d]=0. Bounds: ν(Z_d)≥1 (B zero constant, X⁵≥5, A≥3, X≥1), δ(Z_d)≤23 for d>0 (B_d≤23, X⁵≤23, A≤13, X≤3), odd. For h(R₀) Laurent, distinct exponents have distinct ν and δ, so ν=lowest exponent, δ=5·highest; r≥1, 5r≤23, r odd gives {1,3} (own C6; the mutation admitting r≤0 fails). So (C) holds through <6n. ord γ: at d₀=ord γ<6n the linear part of B_{d₀} is γ_{d₀}·(−hp) (X⁵ and A have none; earlier γ_i=0); [p]B=e has order 3n, so d₀≥3n. γ(X−R_s) then starts at ≥3n+j, and B−βA−γR_s is polynomial, giving (P). Cutoffs 7j/2<3n+j⟺j<6n/5 and 7j/2<6n hold for j≤n (own C5, n≤40 and the symbolic inequality). CONFIRMED.

## 3. Leading divisibility, T, the Q slots (item 3)

C(5/3,2)=5/9, C(5/3,3)=−5/81, 3·C(5/3,3)=−5/27 (own C5). The only rational term at order 2j is (5/9)F_j²/R₀; 2j≤2n is inside (P). T=p⁴+g³p+hgp+t₀p²−h: T/p=g³+hg+(p³+t₀p−h/p) has constant valuation −1 and g-coefficient h; a Laurent root of integer valuation ν gives {3ν,ν,−1} with a unique minimum for every ν, so no root in K̄((p)), a cubic is irreducible, T is primitive (constant −h mod p), Gauss. p∤T, so R₀ squarefree and F_j=R₀C₀. C₀: even (odd/odd), degree ≤8, weight ≤0, ν≥2 so C₀(0)=0, and [p³]F_j=[p²](TC₀)=−h[p²]C₀ forces [p²]C₀=0. Ordinary: own C1 verifies φR₀ has v-order 0 with leading 3u at three (h,t₀); a negative lowest term of φC₀ would survive in φF_j. If C₀=TQ: δ(Q)≤4, w(Q)≤0−8, even, slots exactly p²,p⁴,gp³ (own C2). φT has v-order 1 with leading −3u (own C1), and the Q lifts have negative rows only at v⁻⁴,v⁻² with matrix (0,1,−1)/(1,4,−3) (own C3, kernel exactly b(−1,1,1); omitting a row leaves a plane and fails). So Q=bp²(p²+gp−1), C₀=(pT)(p(p²+gp−1))=bR₀S by associativity, and [p³](R₀²S)=−h² on the pure-p parts (own C4, univariate mod p⁴); also [p²](TQ)=−ha gives the same b=0. So T∤C₀. CONFIRMED.

## 4. Newton balance and the double pole (item 4)

Division by the p-monic R_s over K[[s]][g] is coefficientwise (reduce mod s, uniqueness), so F≡0 mod s^j forces C',D'≡0 mod s^j, and F_j=R₀C₀ with a degree-<5 remainder forces the order-j remainder to vanish: q>j, C(0)=C₀, D₀≠0 of p-degree <5 if q finite. Expanding X⁵ with (D): the quadratic and cubic terms are as displayed; the other cubic terms sit at j+2q, 3q and the quartic tail at 4j. 2j+q>min(2q,3j) for every q>j (own C5). Cases: 2q<3j gives R₀∣D₀², R₀∣D₀, impossible by p-degree; 3j<2q (q=∞ included) gives R₀∣C₀³, T∣C₀, excluded. So 2q=3j, j even, a=j/2≥1, L=7j/2 integer, and 3j<L<4j.

(E): up to order L the rational part is s^{3j}M/R_s−(5/27)s^LC²D/R_s² with M=(5/9)D²−(5/81)C³; own C7 (formal R=g, independent S,c,d, j=2,q=3) finds the negative-R part of X⁵ through s⁷ byte-equal to (E) with moving denominators, the simple pole M₀/R₀ at order 6 and the R⁻² part at order 7 equal to −(5/27)c²d−M₀S; freezing the denominator at R fails. Divisibility: with Y=M/R_s and W=Σ_{i<a}Y_is^i polynomial, M−R_sW=s^aN with N polynomial because both sides are; N₀=M₁−(M₀/R₀)S is the packaged moving-denominator correction, polynomial exactly because order 3j gave R₀∣M₀. At order L the rational part is N₀/R₀−(5/27)C₀²D₀/R₀²; multiplying by R₀² gives R₀∣C₀²D₀, and order 3j gives R₀∣9D₀²−C₀³. In the domain K̄[g,p]/(T): C̄₀≠0 by §3, so D̄₀=0, then C̄₀³=0, contradiction; divisibility over K̄ descends to K. Every case is contradictory, so no arc exists. CONFIRMED.

## 5. Scope, controls, gaps (item 5)

Scope matches the exact claim: char-0 K, full normalized odd unequal source in K[[s]], k=s^m, finite coefficients, h≠0; nothing about emptiness, properness, degeneration existence, h=0, infinity, nilpotent jets or JC2; K→K̄ is licensed because an arc over K is one over K̄. Notes, uncharged: (N1) the §1 aside that a unit multiplying s^m "can be absorbed after a finite extension" is unused and needs both an m-th root of the unit's constant and a parameter change; the claim as stated is k=s^m only. (N2) the producer's toy asserts nothing beyond bookkeeping, as it says.

Own `gate_controls.py` (SHA `57b2f1a5…`, stdlib, `-B` and `sys.dont_write_bytecode` first, RLIMIT 25 CPU s/512 MiB, zero `assert` statements): normal and −O witnesses byte-identical (`69288784…`); mutations `--mutate-moving-denominator`, `--mutate-double-factor`, `--mutate-omit-low-lift`, `--mutate-origin-bound` each exit 1 at the named gate in both modes. Only degree-≤5 factors, the three Q-slot lifts, univariate pure-p truncations and the R=g formal toy were computed. Frozen input SHA-256: `1d65345a…` check.py, `57d85da3…`, `65bb46ee…`, `ad1a4ddb…`, `19f0394c…`, `94fa5194…`, `129947ee…`, `68e04e8c…` (full digests in `input_pins.txt`). Typed gaps, none charged: **GAP-TRANSACTION** (root `c3966052…` not among frozen inputs); **GAP-CHECKER-REPLAY** (producer checker unexecutable here by design; its expected values were re-derived independently). No exit-price claim, so no charge basis line. **STOP/IDLE** after the seal.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10003`.
- Body SHA-256:
  `ff1641755ba9386109082bde06ffe90c70467c5dd1a623e7bddc1c0cfd635072`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
