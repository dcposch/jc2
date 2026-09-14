# D125 pure exceptional gate: independent Fable review

2026-09-07. **CONFIRMED as a necessary first-contact theorem (PASS at the accepted 14f centralizer trust); NO-GAIN for uniform pure-center exclusion, as the producer states.** Every displayed identity, order count, division step and the k=0 nilpotent survivor rederive exactly. One evidence-description GAP: two of the five advertised checker mutations are predicate flips, not changed objects. The producer replay was read, not reproduced: its helper import lives in a non-charged box and was not executed. Own controls: `box/d125-exceptional-pure-gate-fable5-20260907/controls.py` (stdlib only, 8 capped normal/−O runs, 2.8 s wall, 38 MB, zero Assert nodes, witness SHA256 `0b4ed21e2755ca86398ef551fc6f6b484255a9fca23803a9b809419f990dea3a`). Input pins are in `input-pins.sha256`; the charged report hashes to the announced producer value.

## 1. Filtered transfer (W): CONFIRMED

V=g³+p³−3p is monic in g with constant term of p-valuation 1, so any root in Kbar((p)) has valuation 1/3; a cubic without roots is irreducible over Kbar(p), and Gauss gives Kbar[g,p]. Weights 15, 1, −7, −2 for V,R,S,Z rederive. For P=V^eQ with w(P)≤3, every monomial of Q has weight ≤3−15e, while p-exponent ≤2e−1 gives weight ≥−7(2e−1); the gap is exactly e+4>0 for every e≥1 (uniform, not a grid). Hence p^(2e)|Q and R^e|P. With V prime in the UFD K[g,p], R|P^N and w(P)≤3 give V|P and then R|P. Fields only, as stated. The countercontrol gpV has weight 13, p-linear coefficient g⁴, and (gpV)²=(g²V)·R by a nine-term product; R⊂(p²) so R∤gpV. No square of R was expanded.

## 2. Exact references and the mixed correction: CONFIRMED

R_t=R+(t+3)S with S=p(p²+gp−1) rederives as a degree-5 identity. Pure-p selection in (p⁵+tp³−(t+3)p)³: sum 13 only from the three permutations of (5,5,3), giving 3t; sum 3 only from (1,1,1), giving −(t+3)³. So t(s)=[p¹³]A/3 forces [p¹³]F=0 and α=([p³]A+h³)/t forces [p³]F=0; t is a unit at t₀=−3 and α₀=h₀=0, so F₀=0. Since R_s³ has origin order 3 and [p]R_s=−h, [g²p]R_s=0, [gp²]R_s=h, the low row [p]A=0 gives (L): [p]F=αh, [g²p]F=k, [gp²]F=x−αh. The toy A=R_h³+aR with h=a=s uses the FIXED R=R_{−3}, whose p-coefficient is 0, so [p]A=0 holds; t·(aR−αR_h) with α=−3a/t equals ah(R+3S) as a polynomial identity in t, hence F=(ah/t)(R+3S) and F₂=−(R+3S)/3 with p-coefficient 1, p³ zero, gp² equal −1. [R,S]≠0 (checked), so the pairing with R_h⁵ has bracket 5ahR_h⁴[R,S]≠0: an A-source control only. The lesson stands: a no-linear-term bound on F cannot be imported.

## 3. First-contact theorem: CONFIRMED

Identity (I). With Φ=z³+αz, Ψ=z⁵+βz³+γz, Ψ′=Φ′q+δ exactly (q=5z²/3+β−5α/9, δ=γ−βα+5α²/9). Expanding [Φ(R)+F, Ψ(R)+qF+G] and using [R,q(R)]=0, [F,qF]=−(10/3)RF[R,F]=−(5/3)R[R,F²], the bracket is [R,aG−δF−(5/3)RF²]+[F,G] for ANY R and scalar series. Verified exactly at three random moving instances (R of degree 2 plus an s-term, random F,G); a δ sign flip fails.

Order bookkeeping. Target order 3m>2j. At order ℓ with G_i=0 below ℓ and ℓ<j+ord δ, ℓ<2j, only 3R²[R,G_ℓ] survives (a₀=3R², R_s at order 0), so G_ℓ∈K[R]; oddness of R kills even powers of f(R), degree ≤23 leaves ηR³+θR, and the displayed reference shift removes it while changing F not at all. One clarification the text compresses: the shift changes δ at order ℓ itself (θ enters directly, ηα only above ℓ), so "first nonzero δ_d" must be read sequentially. Read that way the process is sound: at each ℓ≤2j−1 either G_ℓ is removed or ℓ=j+d with d<j, and then 3R²G_(j+d)−δ_dF_j∈K[R] because F² starts at 2j>ℓ, [F,G] at ≥j+ℓ, and every h·S correction needs a lower δ or F coefficient. Output: δ_i=0 for i<j in the final references and G=0 through 2j−1.

Division steps. F_j=cR+R²U with U odd, degree ≤3, weight ≤1; the slot enumeration gives p,p³,gp² only. Ordinaryness: φ(R)(u,0)=3u≠0 (checked), so a negative lowest v-power of φ(U) cannot cancel. The complete negative parts of φ(p),φ(p³),φ(gp²) are −v⁻¹; −v⁻³−3v⁻¹; v⁻³+2v⁻¹, giving rows −u₃+u₁₂ and −u₁−3u₃+2u₁₂ and U=u₃S; dropping the v⁻¹ row breaks this (mutation). [p³]R=−3 and origin order 7 of R²S kill c; the leading pure-p coefficients 1,1,1 give [p¹³]R²S=1 and kill d. At 2j, (Q) holds with no suppressed term: F² enters as F_j², [F,G] at ≥3j, moving-R corrections at ≥2j+1. δ_j≠0: R|F_j, C(0)=0 from [p³], the constant of b(R)/R vanishes at the origin, R|C, F_j=R²U, killed as before. δ_j=0: R|F_j², then (W) with w(F_j)≤3 gives R|F_j. C even, nonzero, degree ≤8, ordinary by the same 3u argument. j=m is impossible because p²|R kills [g²p]F_m=k_m≠0. For j<m the weight-3 slots g²p (k_j=0) and g⁹p⁶ (fixed top) are absent, odd weights then give w(F_j)≤1 and w(C)≤0; [p³]RC=−3C(0) and [p¹³]RC=[p⁸]C (checked on random C of degree ≤8) give C(0)=[p⁸]C=0; V|C would give R|C by (W) and the same kill, so V∤C. (O): RC has no p, gp² or g²p term (checked), so ord(αh)>j and ord(x)>j. All conditions are necessary only; nothing here realizes an arc. Centralizer K[R] is consumed at the 14f trust, not rederived.

## 4. Nilpotent k=0 survivor: CONFIRMED

Formal (R,Z) chain rule: A_RB_Z−A_ZB_R for A=R³+εRZ, B=R⁵+(5/3)εR³Z+(5/9)ε²RZ² is exactly (5/9)ε³RZ² at all orders; the ε² term cancels only at coefficient 5/9 (5/27 fails). Actual [R,Z]=g³p²+6g²p³+9p³−5p⁵≠0. Z is even, weight −2, Z(0)=[p⁸]Z=0, degree 2 so V∤Z, i≤2j: exactly (C). RZ is odd, degree 7, weight −1, ordinary, with x=y=[p]A=0 and [g²p](RZ)=0, so k=ε would fail the moving A face by computation, not by fiat. RZ² is odd, degree 9, weight −3, ordinary. Both lie strictly inside the 14c polygons (A: i≤2j, 5i−7j≤3, i+j≤15; B: 5i−7j≤5, i+j≤25) and below the weight-3/5 faces. This fixture is the general 2j-solution: (Q) with δ_j=0 forces R²|b(R) and G_(2j)=(5/9)RC² after kernel removal, and with C=Z the order-3 residual is [F₁,G₂]=(5/9)RZ²[R,Z]≠0 (checked), i.e. failure at 3j for j=1. It is a k=0 point mod ε³, not a nonzero-k jet, and no extension is implied.

## 5. Checker audit

Real controls in the charged `check.py`: literal weights; the gpV term and its weight; ordinary lifts of R,Z with the 3u leading form; F₂ coefficients; multinomial selections; identity (I) at one formal moving instance R_t=g+sp (freeze-R mutation genuine); the formal two-jet bracket (coefficient mutation genuine); the cubic slot list; leading coefficients for [p¹³]R²S. Vacuous items: `need((2*1-2,2*1-1)==(0,1))` is a constant; `face_ok=Q(0)==Q(1)` is a constant and `--mutate-omit-k-face` flips that literal; `--mutate-omit-weight` replaces the computed predicate `w(bad)<=3` by True. So the sentence "Actual mutations omit the weight hypothesis … or omit the actual moving k face" overstates: those two are predicate flips, not changed objects (GAP, evidence description only). The e=1..8 loop is a finite grid of a uniform inequality. Not in the checker: the two U-lift rows and the U=dS solve, any instance of (L), and [R,S]≠0; own controls cover all three. The helper is imported from a non-charged box under a hash pin; I did not execute it and make no claim on the 12-run replay beyond having read it.

## 6. Remaining gap and stop

Remaining after 2j is the order-2j+1 equation of (I): 3R²[R,G_(2j+1)]+[R,(6h₁RS+α₁)G_(2j)]+[h₁S,3R²G_(2j)]−δ_(j+1)[R,F_j]−(10/3)[R,RF_jF_(j+1)]−(5/3)([h₁S,RF_j²]+[R,h₁SF_j²])+[F,G]_(2j+1)=0, valid since 2j+1<3m. For j≥2 the [F,G] term is absent, so it is a linear compatibility in (G_(2j+1),F_(j+1),h₁,α₁,δ_(j+1)) given C; only for j=1 does the cubic term (5/9)RC²[R,C] enter. Hence the next obstruction is at 2j+1, not automatically 3j, as the producer says. Uniform pure-center exclusion, arc existence, guarded emptiness and JC2 remain untouched. No CAS, network, AWS/SSH, live peer or protected-tree read; only degree ≤5 factors, RZ, RZ², (gpV)² and R times random C were expanded. **STOP/IDLE.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8251`.
- Body SHA-256:
  `923b70c47ef216a81799be65e70011fa20f8118c49fdc8bb912438d7493b7979`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
