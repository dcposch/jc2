# Gate: D125 zero-k boundary family and pure-power order-two obstruction (Fable 5.1, 2026-09-07)

Bounded 18-minute hostile delta gate of `xmodel/d125-zero-k-deformation-discriminator-astra-20260907.md` (frozen copy SHA `99d25147…`) with its `check.py` (`25be0862…`) and `witness.json` (`fac39101…`). Scope is only this delta on the accepted varying-face odd source (λ₂=0, λ̃₃=1, moving faces A(2,1)=k, B(8,5)=5k/3, B(1,0)=5k²/9, scalar c₀k³). No complete boundary classification, ramified-arc, flatness, generic-fibre or guarded-nonemptiness conclusion is reviewed or drawn. No CAS, AWS, solver, live peer, shared-ledger or full A15/B25 expansion was used. The frozen `check.py` was run read-only once in normal mode: its stdout hashes to the pinned witness `fac39101…`, status PASS, zero Assert nodes; the eight-run `--record` replay is taken from root as given.

## Verdict table

| item | verdict |
|---|---|
| 1. R_t ordinary lift, oddness, origin, total/inner/support bounds; full unguarded k=0 family A₀=R³+αR, B₀=R⁵+βR³+γR; whole β₁₅ shear with s_t | **CONFIRMED** |
| 2. Centralizer K[R_t] over every characteristic-zero field and every t via primary Lemmas 4–5 | **CONFIRMED** |
| 3. Order-one relation, f(R)=aR+bR³, corrected order-two E with −f′(R)A₁/3, origin, a≠0 and a=0 branches | **CONFIRMED** |
| 4. Squarefreeness for t≠−3, radical pC at t=−3, weighted-leading contradiction with g²p | **CONFIRMED** |
| 5. Logical stop: pure-power points only, k itself as parameter, boundary points have Jacobian 0 | **CONFIRMED** |

No producer claim failed. Typed residual gaps are in §6; none is charged to the delta.

## 1. Boundary family and shear

Recomputed φ(R_t) with g↦v⁻¹, p↦v⁴u−v−v⁻¹ over Q[t]: the negative part of φ(H) is exactly −3v⁻³−9v⁻¹, φ(R) has no negative v-power, its top is the monic u⁵v²⁰, and φ(R)(0,v)=−v(v²+1)(v²+t+4) (hand-checked: w=v²+1 gives w²(2−w−w²−tv²)/v³+(t+3)w/v, and w²+w−2=v²(v²+3)). Support: all seven monomials are odd, nonconstant, total degree ≤5, weight 5i−7j≤1 with the unique top g³p². The listed i≤2j is redundant, since i≥2j+1 forces 5i−7j≥3j+5.

Polygons are not in the charged inputs; I reconstructed them from the accepted parity gate's census. Odd slots with i+j≤15, 5i−7j≤3 number 44 = 33 free + 4 H³ + (2,1) + 6 zero total-face slots; with i+j≤25, 5i−7j≤5 they number 112 = 94 + 6 H⁵ + 2 moving + 10 zero. Both match the accepted 33/94 exactly, so the polygons are these two weight-and-degree triangles. supp R³ lies in the A polygon, supp R⁵, R³, R in the B polygon (multiplication adds the inequalities), the degree-15/25 parts of R³/R⁵ are exactly H³/H⁵, the weight-3/5 parts are exactly g⁹p⁶/g¹⁵p¹⁰, and the moving slots (2,1), (8,5), (1,0) vanish: a weight-5 monomial of R⁵ needs five copies of g³p², so only (15,10) occurs. Hence A₀, B₀ satisfy every k=0 face, polygon, origin, parity and lift condition, and [A₀,B₀]=0 since both lie in K[R]. The Jacobian scalar is 0, so these are non-Keller boundary points, as stated.

Shear: [p¹⁵]R³=1 and [g⁰p¹⁵]R⁵ read directly from the tiny-support R⁵ equals t⁵−20t³(t+3)+30t(t+3)² = t⁵−20t⁴−30t³+180t²+270t, matching the witness `beta15_scalar`; the three exponent selections (n₅,n₃,n₁)∈{(0,5,0),(1,3,1),(2,1,2)} are the solutions of 2n₅+n₃=5 with multinomials 1, 20, 30. So [p¹⁵]B₀=s_t+β and B₀−(s_t+β)A₀ = R⁵−s_tR³+(γ−α(s_t+β))R, i.e. β′=−s_t, γ′=γ−α(s_t+β), not merely β deleted. The shear is a chart symmetry: the A polygon lies inside the B polygon, A has weight ≤3 <5 and degree 15 <25, so B's moving faces, total face and polygon are untouched.

## 2. Centralizer

Read the primary text at p.5. Lemma 4 (char k=0; f,g∉k): algebraically dependent iff the Jacobian matrix has rank 1; proof cites [7, Ch.3, Th.III] and [18, Cor.2], accepted here at external-theorem trust as the producer states. Lemma 5 (any field): dependent iff f,g∈k[h] for a closed h; its proof (Noether normalization of k[f,g] to k[r], then Proposition 1 for the integral closure of k[r]) was read and is self-contained given Proposition 1. Both are stated over an arbitrary base field k, and algebraic dependence is field-independent (a dependence over K̄ is a linear system with K-coefficients), so they apply to every characteristic-zero K and every t∈K, not only generically.

Given [R,E]=0 with E nonconstant, R=F(S) with deg F·deg S=5. Since 5 is prime, either F is affine (then K[S]=K[R]) or S is affine and H=c·L⁵; but p divides H with multiplicity exactly 2 (H/p²=p³+g³ has nonzero p-constant g³), impossible for a fifth power of a linear form. Constants lie in K[R] trivially. The centralizer is K[R]. CONFIRMED.

## 3. Jet identities

Derived by hand: the k¹ coefficient is 3R²[R,B₁]−5R⁴[R,A₁]=R²[R,3B₁−5R²A₁], using [R,R²A₁]=R²[R,A₁]. Domain plus centralizer gives 3B₁−5R²A₁=f(R); degrees ≤23<25 and oddness (1,R²,R⁴ independent) give f=aR+bR³. Consistency check: the weight-5 part is 3·(5/3)g⁸p⁵−5g⁸p⁵=0, which is where the face 5/3 comes from. The k² coefficient is 3R²[R,B₂]−5R⁴[R,A₂]+[A₁,B₁] with [A₁,B₁]=−(10/3)RA₁[R,A₁]−(1/3)f′(R)[R,A₁], and this equals [R,E] for E=3R²B₂−5R⁴A₂−(5/3)RA₁²−(1/3)f′(R)A₁. The producer's factor −1/3 is correct; −1 is wrong. E(0,0)=0 since R(0,0)=A₁(0,0)=0 (odd parity forces zero origins for all k), so h(0)=0. a≠0: E≡−(a/3)A₁ mod R and h(R)≡0, so R|A₁. a=0: E/R=3RB₂−5R³A₂−(5/3)A₁²−bRA₁=h(R)/R, its origin value kills the linear coefficient of h, and reduction mod R gives R|A₁². No other f-term survives parity. CONFIRMED. Own control C4 verifies both identities on the actual R_t at t=2 and on random small polynomials, with generic B₁ for order one; the producer's toy uses R=g, A₁=p only, a single instance.

## 4. Squarefreeness and the impossible face

R=pT with T mod p=−(t+3), T_g=p(3g²+t+3), T monic of degree 4 in p; a factor of 3g²+t+3 lies in K[g] and cannot divide a p-monic T, so gcd(T,T_g)=1. Independent certificate: as a cubic in g over K[p], T has content 1 for t≠−3 and discriminant −4p⁴(t+3)³−27p²(p⁴+tp²−(t+3))² whose p¹⁰ coefficient is −27 for every t, so T is squarefree and R=pT is squarefree. At t=−3, R=p²C, C=p³+g³−3p, p∤C, g∤C, C_g=3g², so rad R=pC with weighted leader g³p (weight 8); for t≠−3 the leader of R is g³p² (weight 1), t-independent. For any weight vector, including (5,−7), leading forms multiply in a domain; checked on 20 random products. A₁'s leading form is exactly g²p because the only odd weight-3 slots of the A polygon are (2,1) and (9,6), (9,6) is in the fixed total face H³ so A₁(9,6)=0, and A(2,1)=k puts coefficient 1 in A₁; no monomial of weight >3 exists in the polygon. Neither g³p² nor g³p divides g²p. Escape search: field (Lemmas hold over any char-0 K), origin (parity-forced), total face (fixed for all k, so deg A₁≤13), exceptional t (only t=−3 changes the radical, handled), branches (a≠0/a=0 exhaustive), B faces (unused by the proof, consistent). None found. CONFIRMED.

## 5. Stop

The proved statement is: no (A,B) over K[k]/(k³) with A≡R³, B≡R⁵ mod k satisfies the chart, for every t and K. Nothing about α≠0 or γ≠0 centers follows, since the order-one factor R² is then lost. The β-only centers (α=γ=0) are equivalent to the pure-power ones by the §1 shear, which the producer does not claim; this covers the b₍₀,₁₅₎-normalized point (R³,R⁵−s_tR³) if that normalization is imposed. No k=s^m, full-boundary, guarded-client or JC2 claim is made. CONFIRMED.

## 6. Controls and gaps

Own `gate_controls.py` (SHA `953455a9…`, stdlib, pinned frozen paths, zero Assert nodes): C1 lift/support/leader, C2 polygon census 44/112 and 33/94, containments, faces, s_t vs witness, C3 factor and discriminant certificates, t=−3, leading-form multiplicativity, C4 jet identities and the dependent jet with zero moving faces. Ten runs: normal and −O witnesses byte-identical (`62d91f5a…`), 3.4 s total, caps 30 wall/25 CPU s, 512 MiB. Mutations: gp² coefficient t+3→t+4 (negative v-power appears), factor −1 (order-two identity breaks), A-polygon weight 3→5 (max-weight slots change), shear multinomial 20→10 (s_t mismatch); each exits 1 in both modes with its intended message. Artifacts in `box/d125-zero-k-deformation-gate-fable5-20260907/`.

Typed gaps, not charged: **GAP-POLYGON** the polygon definition is inferred from the accepted census, not read from a charged source. **GAP-NORMALIZATION** whether b₍₀,₁₅₎=0 is imposed is not in the inputs; the §2 theorem does not need it. **GAP-HISTORY** the producer's scoped history scan is not replayed. No exit-price claim is made, so no charge basis is declared. **STOP:** review only.

<!-- BODY-END -->
