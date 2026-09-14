# Gate v2: k=s⁴ complete unguarded six-jet survivor at t₀=−4 (Fable 5.1, 2026-09-07)

Bounded 15-minute hostile gate of `xmodel/d125-m4-residue-discriminator-astra-20260907.md` (frozen SHA `d32b3965…`, matching the supplied report premise), its `check_jet.py` (`fece5e93…`, whose helper pin `25be0862…` matches the frozen `check.py`) and `reading-note.md` (`d04eab2a…`), read whole from `/tmp/jc2-lane.dNKoYE/inputs` only. The three accepted gates (classification `68e04e8c…`, low-jet saturation `65bb46ee…`, parity normalization `53f78754…`) are consumed as interfaces, not re-hardened. Root transaction `88594a61…`, root report/receipt hashes and the 22-pin/20-run producer replay (6.475 s) are custody premises, not proof. Neither producer script was executed or imported. No client stream, ledger, peer, live artifact, AWS/SSH/CAS/solver or network was touched; the source row inventory is taken from the classification gate (A vertices (0,0),(0,15),(9,6),(2,1); B vertices (0,0),(0,25),(15,10),(1,0); weight (5,−7); 30 A and 75 B negative rows; faces A(2,1)=k, A(9,6)=1, B(1,0)=5k²/9, B(8,5)=5k/3, B(15,10)=1; Jacobian target −5k³g²/9 from the low-jet gate).

## Verdict table

| item | verdict |
|---|---|
| 1. §§3–4 explicit k=s⁴ pair over Q[b]/(b⁴−3) is a COMPLETE UNGUARDED normalized odd source jet modulo s⁷: lattices, all fixed faces and zero slots, parity, origins, all 30+75 negative lift rows, all Jacobian rows | **CONFIRMED** (own controls, caps literal) |
| 2. The three saturated low equations a01=0, 9e=5kx, x²=3ky hold with x=−b²s², y=1, a01=0, e=−5b²s⁶/9, k=s⁴, by actual multiplication modulo b⁴−3 | **CONFIRMED** |
| 3. B_g first nonzero order 8 and Jacobian target order 12 are outside the verification | **GAP** (untested, correctly disclosed; both vanish modulo s⁷) |
| 4. Not a guarded point, arc, full k-saturation, properness or JC2 result; no guaranteed degeneration from any guarded point | **CONFIRMED** as scope statements; nothing beyond them is available |
| 5. §1 general residue necessity (kernel removal, R₀ | 9D²−C³ as a necessary condition) | **UNREVIEWED** (not needed by items 1–2) |
| 6. §2 exact linear-space census (15 columns, rank 6, nine-element kernel; 33 columns, dimensions 20/18) | **UNREVIEWED** (not needed by items 1–2) |

## Independent checks behind items 1–2

Literal factors (expanded, all within caps): R=R₋₄=p⁵+g³p²−gp²−4p³+p is odd, degree 5, weight leader g³p², and equals R_t at t=−4 exactly; T=R/p; S=pE; C*=Z+L=gp+gp³+p⁴; r,Z,q as displayed. C₀=r²−TZ has degree 6, even parity, weight ≤0 and low coefficients [1]=0, [gp]=−1, [p²]=0; D₀=r³−Tq has degree 9, odd parity, weight ≤1, p|D₀, i≤2j, [p]=[gp²]=[p³]=0 and lowest total degree 5. With C=b²C₀, D=(b³/3)D₀: [gp]C=−b² and ([gp]C)²=b⁴=3 by actual reduction, which is the reading-note meaning of `C_gp²=b⁴`. Explicit C₀ and D₀ coefficient lists are in the witness.

Lifts under g↦v⁻¹, p↦v⁴u−v−v⁻¹ were computed only for the degree ≤5 factors and their products. φ(R), φ(T), φ(r), φ(Z), φ(E) are ordinary; φ(R) has v-order 0 with v⁰ coefficient exactly 3u (reading-note premise confirmed); φ(T) has lowest v-power 1; the complete negative part of φ(q) is v⁻¹; φ(r)=u²v⁷−uv⁴−uv². φ(L)=φ(p)²φ(E), φ(S)=φ(p)φ(E), φ(C*), φ(Tq), φ(C₀), φ(D₀) are ordinary, and the factor products agree with the direct lifts of the literal C₀, D₀. Hence φ(U) and every A/B block other than W are ordinary as products of ordinary lifts.

W: the identity D₀²−C₀³=T·M with M=−2r³q+Tq²+3r⁴Z−3r²TZ²+T²Z³ was checked universally in four abstract variables, and 9·(1/3)²=1 gives 9D²−C³=b⁶TM. p|r, p|Z, p²|q on the literal supports, so M/p is a polynomial and W=(5b⁶/81)M/p satisfies RW=(5/81)(9D²−C³) without localization. Degree ≤13 and lowest total degree ≥5 follow from the factor degrees (every M term has degree ≤14 and ≥6), oddness from r,q odd and T,Z even. The weight bound ≤1 does NOT follow from the M route (which gives only ≤17); it follows from w(D)≤1, w(C)≤0 and the unit leading form g³p² of R, so top forms multiply and w(W)=w(9D²−C³)−1≤1. This is a reading clarification, not a defect. Ordinariness: φ(R)φ(W) is ordinary, φ(R) has v-order 0 with coefficient 3u, and 3u·c(u)≠0 for every nonzero c∈K[u] over any Q-algebra K; so φ(W) has no negative v-power. No field hypothesis on K is used anywhere; injectivity of K[g,p]→K[g,p,R⁻¹] holds because R has unit coefficient on p⁵.

U: by degree ≤3 projected products only, U₃=r₃−R₃−2(RC*)₃+4(R²S)₃=g²p exactly, with zero p, gp², p³ coefficients; the weight-3 form is unique and equals g²p because w(r)=3 with top g²p, w(R)≤1, w(RC*)≤−1, w(R²S)≤−5; deg U≤13; U is odd.

Formal bracket: the displayed B table (5/3, 5/3, 5/3, 5/9, 10/9, 10/9, W) equals the abstract expansion of R⁵(1+ε)^{5/3}, ε=s²C/R²+s³D/R³+s⁴U/R³, through s⁶, including the CU cross term 2·(5/9)=10/9 and the only pole (5/9)D²/R−(5/81)C³/R=W. So B=X⁵+γs⁶X+O(s⁸) with X=A^{1/3} in K[g,p,R⁻¹][[s]], hence [A,B]≡0 modulo s⁷, and the Jacobian target −5k³g²/9=−5s¹²g²/9 is 0 there. Two own R=g toys with independent small C,D,U (Laurent poles in g allowed) give a zero bracket through s⁶, reject the CU factor 5/9, and show γ is bracket-free at this order; γ is fixed only by the e row.

Support: A blocks have (degree, weight) (11,≤1),(9,≤1),(13,3); B blocks (21,≤3),(19,≤3),(23,5),(17,≤1),(15,≤1),(19,≤3),(13,≤1),(5,≤1). The degree-15/25 faces stay H³/H⁵ with their 6/10 zero slots; the only weight-3 A contribution is s⁴U, so A(2,1)=s⁴=k and A(9,6)=1; the only weight-5 B contribution is (5/3)s⁴R²U, whose weight-5 form is the single monomial (5/3)g⁸p⁵, so B(8,5)=5k/3 and B(1,0), B(15,10) are untouched. Inner faces of both polygons carry no other lattice slots. Odd parity holds blockwise, so every even slot and the origin are zero.

Low rows, explicit: A modulo degree 3 is p³−b²s²gp²+s⁴g²p, so a01=0, y=a03=1, x=a12=−b²s², A(2,1)=k; g and g³ are outside the A lattice. B modulo degree 3 is γs⁶(p−gp²−4p³) with γ=−5b²/9: [g]B=0, e=[p]B=−5b²s⁶/9, b21=[g²p]B=0, b12=[gp²]B=5b²s⁶/9, b03=[p³]B=20b²s⁶/9; only the γR block reaches degree ≤3 (W has lowest degree 5). Then x²−3ky=b⁴s⁴−3s⁴=0 and 9e−5kx=−5b²s⁶+5b²s⁶=0 by actual multiplication with b⁴→3. The unsaturated source rows vanish trivially modulo s⁷ (k²=s⁸, ke=s¹⁰, xe=s⁸), which is why the three saturated equations are a genuine extra imposition, as the report says.

## Controls, scope, gaps, stop

Own `box/d125-m4-sixjet-gate-fable5-v2-20260907/gate_controls.py` (SHA `58d49068…`, stdlib, zero Assert nodes, `-B` with bytecode disabled, 512 MiB/25 CPU/30 wall caps, no frozen writes or imports): 52 named gates. Ten runs, normal and −O, positive witnesses byte-identical (`dc29df2c…`), total 1.2 s, `replay.json` `6522f2d6…`, `input_pins.txt` present. First named failures, identical in both modes: changed q (+gp⁴) → `phi(q) complete negative part = v^-1`; changed U4 coefficient (−p³) → `U4 low jet == g^2 p exactly`; changed CU factor 5/9 → `displayed B table == (1+eps)^(5/3) through s^6`; changed b⁴ reduction (b⁴→1) → `([gp]C)^2=b^4=3`, with the x²=3ky row also failing downstream. My gate order differs from the producer's, so first-failure names differ; the producer's checker was not run.

Cap discipline: no R³, R⁵, A₁₅/B₂₅, actual W, R²S, full U or actual-source bracket was expanded; U only by degree ≤3 projections; W only by abstract factorization; brackets only with R=g toys. One own-code defect (coefficient extraction carried g,p exponents into the low-equation test) was fixed before recording; no diagnostic retry of any capped computation occurred.

Scope held: the construction is a point of the unguarded source plus the three saturated equations over the nonreduced finite algebra K[s]/(s⁷), K=Q[b]/(b⁴−3). It is not an arc, not a guarded point (zk−1 cannot hold with k⁴=0), not a full k-saturation, and gives no properness, generic-fibre, degeneration or JC2 consequence. Items 5–6 are marked UNREVIEWED, not refuted; the finite construction does not depend on them. GAP-ORDER8/12: the fixed B_g=5s⁸/9 and target −5s¹²g²/9 are untested by everything here. GAP-TRANSACTION: the transaction root is not among the frozen inputs. No exit-price claim is made, so no charge basis is declared. **STOP:** review only; own checker and receipts frozen; no promotion authority beyond the six verdicts.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line, including its terminating newline; this seal is outside the body.
- Body bytes: `8837`.
- Body SHA-256: `3ec2125b485277787035f5d922287fed07a6af019e7cd4af4c0c675f370e7bb3`.
- Own artifacts: `box/d125-m4-sixjet-gate-fable5-v2-20260907/` (gate_controls.py, witness.txt, witness-O.txt, replay.json, input_pins.txt, receipts.sha256).
