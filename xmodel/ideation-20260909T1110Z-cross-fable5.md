# 1110 adversarial cross — Fable 5.1 seat

tag=ideation-20260909T1110Z-cross-fable5
frozen_basis=0d39df3c9fd69c939a8420c54d03228b9077777d (provenance only)
actual_start=2026-09-09T11:38:08Z (invitation released after the 11:34:28 whole blind collection)
controlling_stop=2026-09-09T11:49:28Z (original fixed target; earlier than start+15 min = 11:53:08Z); reduced window 11 min 20 s, not reset
subprocesses=ZERO mathematical subprocesses. Only date, ls, cat, sed, sha256sum, mkdir, printf and heredoc writes. All algebra below is hand reasoning on the frozen packet.
status=see final section (COMPLETE or honest PARTIAL/LATE)

## 0. Custody and read scope

All 27 charged objects were read WHOLE from /tmp/jc2-lane.5hL2ME/inputs; sha256 of every file was recomputed and matches CROSS-PINS.json exactly (retained in box/ideation-20260909T1110Z-cross-fable5/input-pins.sha256). Four large objects overflowed the tool output cap and were re-read whole in two line-range chunks each (recorded in custody.txt). Prior same-round whole reads of the 19 frozen objects during my 11:19–11:26 blind are disclosed; byte-identical hashes were verified before reuse. No provenance path, live body/log/receipt, the in-progress whole-mate derivation, protected tree, web, CAS or solver was touched. The compact contract and module are consumed as terminal accepted 16q per the cross contract; the three blinds' smaller reconstructions are PROVISIONAL proposals.

## 1. Deduplication: one decision object, three votes, two mechanisms

By object: all three blinds target the SAME object, the r=1 complete ideal J_1 (39 vars/53 rows, gate-confirmed isomorphic to I_1 with 49/63; accepted 16q). Root Card1, Astra Card2 and Fable Card1's decision step are ONE complete source-ideal decision with three votes, not three tests. Their outcome tables agree (unit ⇒ D28 column empty for all q at the 15x/16m/16k–16p imports; exact field point or nonzero finite Q-algebra point with all rows and ηc=1 ⇒ CE endpoint via 16q; timeout/mod-p ⇒ NONDECISION). Label: KNOWN (one decision).

By mechanism: root Card2 and Astra Card1 are the SAME reduction, the fixed-unit Euler graph: the t^(k+2) row contains B_k only through κ(kB_k − 3S·B_k'), pivots κ(k−3i) on S^i, resonances exactly (k,i)=(3,1) and (0,0). DUPLICATE of each other with independent origins; the operator itself is KNOWN in the frozen LIVE excerpt (root's unsealed scratch). Fable Card1's "mate ideal of minors in ≤12 A-unknowns" is the same target with a WRONG closed-set formulation (see §2): SCOPE-CONFLICT, superseded by the Euler graph. Fable Card2 (top-row analysis h=7..4 at top R-degree) is VACUOUS at top weight: with w(S)=1, w(t)=r the weight-(7r+2) layer of EVERY bracket row is exactly the 16l ODE (I rechecked the T^7 coefficient: mD_4 − nC_2 = 0 is the row h=0 top coefficient, and T^8 vanishes identically since 3n−5m−1=0). So the top layer is already solvable for all r; Fable Card2 is KNOWN and withdrawn as stated. Root Card3 (marked source map on the rank-3 boundary) supplies no condition beyond the rows: NO_NEW_MECHANISM there, agreed with Astra's negative crosslink ([x,p]=2p−t ∉ T; rank 3 over K[S,p] is not d2=3; BD-GAL untouched).

Survivors (max three):
- S1 (KNOWN operator / NEW exact presentation, PROVISIONAL): the gauge-fixed fixed-unit Euler reconstruction of B as an exact reparametrization of J_1: 6r+7 parameters, 13r+17 residual slots, 13/30 at r=1. Must pass BEFORE any builder: (a) the gauge group is exactly {A→A+δ, B→B+βA+γ} and gauge fixing A_0(0)=B_0(0)=[S]B_3=0 is a bijection on solution sets over every field with κ a unit; (b) substituting the reconstructed B makes rows h=2..7 vanish identically; (c) the residual list is complete: rows h=0,1, both resonance scalars, B_0 monic at S^n, all seven B pole rows, wκλ−1. A ≤20-minute different-model interface audit, zero compute.
- S2 (KNOWN): one complete r=1 decision, gated by an independent two-way builder cross-check of the raw 63-row I_1 against the 30-row graph (polynomial identity checks, minutes, no Gröbner), then ONE capped exact attempt per presentation (raw/module and graph), at most two attempts total, NONDECISION retained.
- S3 (NEW, small, proof side, zero compute): redirect the uniform program from top rows to the sub-top weight layers (6r+1 and below) of the retained residuals with the Euler-reconstructed B, for general r, by bounded hand derivation. Replaces Fable Card2.

## 2. Attack on the mate reduction; correction of the Fable blind

The cross contract's objection is correct and I retract my formulation. For fixed A the bracket rows are a linear system M(A)·B = cδ; its solvability locus is rank M = rank [M|cδ], which is constructible, not the zero set of an ideal of minors: the hand control a·x=1 has locus a≠0. A rank-stratified route must carry pivot-open conditions and every exceptional rank as separate localized charts, plus B_0 monic and κ_Aκ_B=c≠0 as extra equations. That is strictly worse than the Euler graph, where every pivot is a nonzero rational constant times κ, already a unit by wκλ−1, so NO rank stratification exists: solvability is the closed condition "two resonant right-hand sides vanish", and B is unique modulo the kernel.

Hand verification of the graph (no subprocess): row t^h is Σ_{i+l=h+1}(lA_i'B_l − iA_iB_l'); with A_3=κS the only B_k term in row h=k+2 is kκB_k − 3κS·B_k', all other B-indices are >k because i≤2; degree of the right side ≤ n−rk. Row h=7: 5κλS² − 6κλS² = −κλS² against −cS² gives κλ=c. Row h=6 with A_2=Sd−κu (module form) and B_4=S²e−2uλS reduces to κ(2e+3Se') = λ(d+5Sd'), the uncancelled 2κλuS being exactly c·Δ_6 (Δ = 1+ut−ℓt²+(ℓu−1)t³+(2u−ℓS)t⁴−(u²+2S)t⁵+2uSt⁶−S²t⁷); so e_i = (λ/κ)(1+5i)/(2+3i)·d_i. Astra's (1) is exact, and my blind's −4D_0A_2(0)+C_0B_4'(0)=2cu is its S^0 specialization. Unused rows: h=0: A_0'B_1 − A_1B_0' = c (7r+3 slots); h=1: 2A_0'B_2 + A_1'B_1 − A_1B_1' − 2A_2B_0' = cu (6r+3 slots). Resonance control: (3−3S d/dS)S=0, so S is not in the image and the compatibility scalar is a genuine equation. B_0 monicity is a residual because row k=0 fixes B_0' only. The seven B pole rows (gate Target C list) are NOT implied by the recursion in general (B_{4,0}=0 is, since the h=6 right side has no S^0 term; the others are retained). Inverse-pole rows for A are identically satisfied by A's module form. Verdict: the graph is an exact elimination order of J_1, but its 13/30 count is a slot bound; reconstructed B coefficients have parameter degree growing to about 6–8 and the residuals to about 8–9, so no speed claim follows.

## 3. Root's gauge objection: audited and accepted

B→B+βA+γ preserves [A,B], t-degree ≤5 and every deg B_k ≤ n−rk (deg A_k ≤ m−rk < n−rk), inverse-ordinaryness (A is inverse-ordinary, γ constant), B_5=λS² (A has no t⁵), and B_0 monic since deg A_0=m<n. Likewise A→A+δ. Hence a ≥2-dimensional homogeneous kernel of B↦[A,B] is FORCED for every A (it contains A and 1), and my blind's outcome "kernel for generic A ⇒ builder error, stop and audit" was wrong: it would fire on every correct builder. Uniqueness modulo gauge is proved by root's triangular argument, which I rechecked: a difference D with [A,D]=0 and D_5=0 has D_4=0 (4≠3i), D_3=βS, then D−(β/κ)A has D_3=0, rows k=2,1 kill D_2,D_1, row k=0 leaves D_0=γ. So existence of a mate is a well-posed closed condition and the mate is unique modulo exactly βA+γ; any dimension or point claim on the ungauged 39/49-variable ideals must subtract this 3-dimensional orbit (unit certificates are unaffected). Note the ideal is genuinely inhomogeneous: no torus weight makes Δ homogeneous (tΠ² and ut cannot share a weight), so cone-style dim-0 tests do not apply.

## 4. Uniform obstruction versus a first bounded r=1 decision

Neither outranks the other in value; the r=1 decision comes FIRST in order because it is finite, two-sided and calibrates the uniform program (a unit certificate's cofactor support says which weight layers matter; a point ends the search for a uniform obstruction). Cheapest decisive first test: the two-way builder cross-check of S2 (substitute the reconstructed B into the raw 63 rows; rows h=2..7 must vanish identically, rows h=0,1 and the pole rows must reproduce the 30 residuals). Outcomes: match ⇒ same ideal, proceed; mismatch ⇒ builder error, STOP, no solve. Then one capped exact decision per presentation. Outcomes: verified exact Q-unit certificate ⇒ the 112/196 D28 exception is closed at its imports and, with 16m, the whole numerical D28 column for every q; verified properness or an all-row field point ⇒ CE candidate, re-verified against the RAW contract (never the reduced graph alone) before any claim; timeout, memory, mod-p only, or partial rows ⇒ NONDECISION, no rank change. Defensible cap: chosen from the measured construction (term count, maximum parameter degree, memory), bounded above by one lane-hour and one ordinary fleet worker's RAM; historical baselines are the 300 s hybrid-81 timeout (15c) and the 20-hour K7 timeout (14h), which show that variable count alone predicts nothing. Stop: no second prime, no RAM/time escalation, no r≥2, no farm; two non-informative attempts (one per presentation) force redesign per COORDINATION. In parallel and at zero compute, S3: the top weight layer of every row is the 16l ODE, so a uniform argument must live in the weight-(6r+1) and lower layers; derive the 6r+1 layer by hand for general r and stop if no r-uniform relation beyond the ODE appears.

## 5. Global holes; NO_NEW_MECHANISM

A uniform F10 result, if obtained, closes only the ordinary rectangular F10 stratum at the 16k imports. 16m's D28 column is the single numerical column 28(q+2)/28(2q+3); the printed F10(j), j≥1 (5j+7, 3j+4) columns and every other degree are untouched, as are the 126/128/132/135 table configurations, Laurent-standard pairs, and all-degree landing (G2-PSC is transport/fidelity, G2-BD is post-residue-A delay; neither implies the other). K16 stays proved only through t≤8 with the b·B·η product and separate b=0 obligations. The rank-3 algebra T over K[S,p] is a boundary ring; BD-GAL closes d2=2 only, and T assigns no field degree to the source map. Mechanism verdict: NO_NEW_MECHANISM. The two genuinely new statements in this cross are corrections (gauge kernel βA+γ forced; minors ideal replaced by unit-pivot closed conditions) and one small structural fact (top weight layer = 16l ODE, so top-row analysis is vacuous). Strongest hidden assumption shared by all three blinds: that the reduced system is the object to decide; the honest object remains the raw contract, and every point must be re-verified there.

## 6. Separate systems verdict: NO_CHANGE (retracting my blind's UPGRADE)

My blind attributed the missed 11:13 release to post-seal preflight. The record refutes that: root's blind closed 11:17:40, Fable's receipt started 11:19:09 and Astra's local start was 11:19:32, so preflight took under two minutes; the miss occurred BEFORE the seal, in root's own blind authoring (lease 11:07:44–11:17:40) against a planned 11:13 release. The 0730 misses were coordinator context/status interruption per the synthesis. A release script would have saved nothing measurable. Verdict: NO_CHANGE; no wrapper, ledger or probe. Smallest regression test if anyone still wants one: record (root artifact closed_utc, first receipt start) per round from the existing artifact and receipt files, and only if the median gap exceeds three minutes over the next three rounds does a release tool earn a test. Release utility of the compact endpoint itself is unchanged by this cross: no builder, solver or allocation is licensed.

## 7. Continue / redesign / stop

- CONTINUE: uniform source-attached F10 work, REDIRECTED to sub-top weight layers (S3); the global landing/coverage obligations at unchanged low priority.
- REDESIGN: the CE test around the gauge-fixed Euler graph (S1) only after the ≤20-minute interface audit and the builder cross-check (S2); one capped decision per presentation, NONDECISION retained.
- STOP: my minors-ideal formulation, my top-row Card2 as stated, my systems UPGRADE; root Card3 unless a source-implied condition beyond the rows is exhibited; norm/ODE-only routes; retired F2/F9/D125/D108 solves; any r≥2 farm; any AWS allocation now.

Dependencies: accepted 15x, 16g–16p, 16q (terminal); provisional: Euler-graph equivalence and 13/30 count (root/Astra blinds), corrected here by hand but NOT gated. Arrow: gauge-fixed 13-parameter graph over Q[params]_(wκλ=1) presenting V(J_1) modulo the 3-dimensional gauge (PROVISIONAL), J_1 ⊂ Q[39] ≅ I_1 ⊂ Q[49] as Q-algebras (16q Target G) → field point → (Â,B̂) ∈ K[R,t] → cond 4 → K[p,z] → K[g,p] → P,Q ∈ K[U,V], degrees 28m/28n, [P,Q]=c (16q Target B) → Jung–van der Kulk → non-automorphism → embed in C. No theorem is promoted by this report; no authored Seal or charge_basis.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check over this body; no corpus scan performed or permitted.

Status: COMPLETE within the reduced window if the marker below is on disk before 11:49:28Z; otherwise LATE by the recorded seal time. All writers IDLE after the marker.

<!-- BODY-END -->
