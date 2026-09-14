# Fable5.1 FULL2240 cross report — ideation-20260911T2240Z-fable5-cross

tag: ideation-20260911T2240Z-fable5-cross
scope: POSTBLIND_EQUAL_CROSS (adversarial strategy, NOT promotion)
author: Fable 5.1 (claude-fable-5-1), fresh external CLI; launcher owns custody
started_utc: 2026-09-11T23:02:18Z (invitation received after the 23:00 blind close)
reserve_utc: 2026-09-11T23:16:00Z  hard_utc: 2026-09-11T23:19:00Z
inputs: /tmp/jc2-lane.Lp20wL/inputs, exactly the 17 charged objects, all hashed
before consumption and read WHOLE (approaches.md in four bounded line ranges
1-350, 351-700, 701-1020, 1021-1337; the source-selection/websweep/master46
aggregate was re-read from persisted tool output in two ranges 1-120, 121-190).
No prior-pin WHOLE reuse claimed. No peer cross, live file, linked report,
primary source, code, CAS, network, process or shared write was used.
Manual mathematics only; nothing below is verified or promoted.

## 1. Merged trace/Mellin proposal — arrow by arrow

Notation as in the blinds: A=C[p,q]⊂R=C[x,y], n=[Frac R:Frac A], N=R/A,
M=Tr(R), K0=ker(Tr:R→M), L_D=M/A=⊕L_i, B=C[e_p,e_q], E=Frac B,
ρ(X)=dim_E(E⊗_B X), T the target torus pq≠0, D the actual reduced
nonproperness curve, D̃_i the normalization of D_i.

1. Exact kernel sequence 0→K0→N→L_D→0 as W-modules. SUPPORTED. Kernel of
   N→M/A is K0 because Tr(r)=a∈A gives r−a/n∈K0 and K0∩A=0 (char 0);
   surjectivity and W-equivariance are TRACE-IC-1.
2. Finite ranks and additivity. SUPPORTED at the BASS-SELECTION-1 tier
   (holonomic direct image, corrected LS, de Rham comparison); E⊗_B is exact,
   and each L_i is holonomic, so ρ(K0)=ρ(N)−Σρ(L_i) is a conditional identity.
3. IC/normalization shift. SUPPORTED as a derivation, not new information.
   H2(M)=0 (TRACE-IC-1) and right exactness of H2 on 0→A→M→L_D→0 give
   H2(L_D)=0; for curves L_i=ν_+O_{D̃_i}, so H2(L_i)=H^1_dR(D̃_i)=0, hence
   g_i=0 with one place at infinity: D̃_i≅A^1. This reproduces the row-7
   one-place rationality of asymptotic components (Fable Card 2 PASSES as a
   consistency check; it is a duplicate of known structure, not a result).
4. Boundary ranks and sign. SUPPORTED without guessing: with the same DR
   convention that makes ρ(N)=χ(F^{-1}T) (the accepted +1 in dimension 2),
   DR(L_i)|_T=ν_*C[1] gives ρ(L_i)=−χ(D̃_i∩T)=n_i−1, where n_i counts
   points of D̃_i over the two axes. Nonnegativity of rank forces this sign
   whenever some n_i≥2; the opposite sign would give negative ranks.
5. Strict positivity (Astra source). SUPPORTED, and the nonvanishing part is
   unconditional: for n>1 the trace form has a nonzero trace-zero element of
   Frac R; since Frac R=(Frac A)·R (clear the constant term of a minimal
   polynomial), it clears to a nonzero element of K0. ρ(K0)≥1 then needs only
   Bass 1.4 torsion-freeness of N (named tier).
6. Quotient-line existence. UNSUPPORTED SOURCE DATUM. E⊗L_i is one E-line
   (hence δ-stable, trivially) exactly when n_i=2. Nothing in the packet says
   any actual component meets the axes in exactly two places.
7. Line lifting. FIRST UNSUPPORTED ARROW OF THE MERGED PROPOSAL. Fable's
   route made lifting vacuous through ker Tr=0. By item 5 that branch is
   exactly n=1, i.e. the automorphism case. For every nonproper map
   (K0)_E≠0, so Astra geometry's additive obstruction b∈coker(δ−a|(K0)_E)
   is never vacuous, and no source-specific vanishing of b is supplied.
8. Resonant polynomial-G normalization. UNSUPPORTED and unchanged; the
   accepted rank-1 control already shows some rational a admit no gauge.

Verdict: arrows 1–5 survive at their tiers; arrow 6 is missing source data;
arrow 7 is the first unsupported implication and is unsupported precisely
because arrow 5 holds. The "simple boundary summand ⇒ first-order source
vector" shortcut is closed, as Astra geometry predicted.

## 2. ker Tr=0 versus K0≠0; what the budget really says

Both assertions survive and do not conflict. Fable's dichotomy "N≅L_D or a
nonpolynomial element with polynomial trace exists" has a vacuous first horn
for n>1; the second horn is automatic (trace-zero elements). So the rank
identity is never a rank-0 statement; it is the strict budget
ρ(N)≥1+Σ_i(n_i−1), and ρ(K0)=0 would already force n=1. Fable's Card 1
"n_i=2 line" shortcut is WITHDRAWN.

Does the budget exceed standard fibre Euler identities? Compute ρ(N) by
constructible functions: F is étale, fibres over T∖D have n points, fibres
over t∈D have n−e(t) points with e(t)≥1 (escape multiplicity), and e(t)≥e_b
at special points of each branch b by openness. With χ(T)=0,

    ρ(N) = χ(F^{-1}T) = −∫_{D∩T} e dχ,

which is the accepted 1−χ(p=0)−χ(q=0)+#F^{-1}(0) (fibre additivity). With
χ(D∩T)=Σ_iχ(D̃_i∩T)−Σ_z(r_z−1) over singular points z∈D∩T with r_z
branches, and ρ(L_i)=n_i−1, the budget becomes

    ρ(K0) = Σ_i (e_i−1)(n_i−1) + Σ_{special t∈D∩T} ( Σ_{b∋t} e_b − e(t) ) ≥ 1,

e_i the generic escape multiplicity along D_i. Smooth jump points contribute
e_i−e(t)≤0; nodes contribute e_b+e_b'−e(z), sign undetermined. So the
budget is NOT a bookkeeping identity: the Euler ledger fixes only ∫e dχ,
while the inequality constrains the escape multiplicities against the
axis-place counts. Example: one component, smooth in T, e_1=1, no special
points gives ρ(K0)=0, contradicting Bass torsion-freeness; that configuration
is excluded at the Bass/LS tier. Whether e_i≥2 is already known for Keller
maps I cannot verify from the packet; even then the n_i=1, node-free
configuration still gives 0, so the inequality retains content. It does not
exclude any general configuration by itself: the e-data are free. No sign
was guessed; the only convention used is the accepted ρ(N) sign plus rank
nonnegativity. Consistency control: the packet's one-branch Kummer/open
immersion model has ρ(K0)=0 with K0≠0, allowed there because K0 is B-torsion
(e_p acts by half-integers), which is exactly why Bass 1.4 is load-bearing.

## 3. ONE cheapest source-specific discriminator

Quantity: the escape–place inequality above for the ACTUAL D of a
hypothetical Keller map. Dependencies: TRACE-IC-1, BASS-SELECTION-1 tiers,
Bass 1.4, plus the elementary fibre-additivity computation. Cheapest test:
20 minutes UNMEASURED manual re-derivation of the displayed formula by a
different model, checking (i) the Kummer control returns 0, (ii) n=1 returns
0, (iii) the sign by nonnegativity, (iv) whether any accepted theorem bounds
e_i≥2 (then restate the excluded configuration). Outcome A: formula holds ⇒
bank a conditional necessary condition tying avenue-7 place data (n_i) to
escape multiplicities (e_i, e(t)), the first quantity where the trace and
Mellin attachments interact beyond bookkeeping; no exclusion until a source
theorem pins e-data. Outcome B: formula fails ⇒ the LS attachment to L_D is
misapplied and the merged proposal stops. Stop rule: no module farm, no
operator family, no assumed quotient line, no mixed localization, no lane;
one different-model FIRST note only.

## 4. Degree-doubling deduction; rankings; F10

Astra source's deduction is SOUND and elementary: E*ω=2ω gives
{H∘E,G∘E}=2({H,G}∘E), so (H∘E^k,2^{-k}G∘E^k) is a regular scalar pair with
the same Laurent support (DS-INV-1) and generic degree 2^k·d, degrees
multiplying in the function-field tower. Attack: it only goes up; nothing
descends a pair along E, and ordinary degrees grow with k. Consequence for
allocation: none for construction ranking; it forbids any "support ⇒
degree ceiling" preprocessing, which would already be a full exclusion
theorem at that support. Construction ranking stays: regular scalar pair
on the merged S/T interface, then complete guarded characteristic-zero F10
source properness, then AS109. No candidate exists for any of them.

Proof ranking reconciled: (1) source-derived contradiction from the
trace/derivation structure, now with a concrete quantity (section 3);
(2) uniform source geometry/landing/cofinality; (3) bounded fixed-r F10 only
with an authenticated instrument. F10 disagreement: Fable's blind Card 3
(single-shot r3 attempt) is WITHDRAWN as a launch recommendation. All four
F10 cards are the same deferred experiment; the release flow is unqualified;
the contract closes the engineering cycle. Keep it as the nearest finite
test on paper; no worker, retry or cap change, no utilization launch.

## 5. What survives; FIRST review; objects NOW

Survives: exact sequence, K0≠0 for n>1 (unconditional), D̃_i≅A^1 as a
consistency duplicate, ρ(L_i)=n_i−1, the escape–place inequality (conditional),
Astra geometry's never-vacuous lifting obstruction, the degree-doubling
warning. Dead: Fable's ker Tr=0 branch and its n_i=2 shortcut; any rank-0 or
trace-section reading. Different-model FIRST review is warranted only for
the section-3 formula (ROOT or Astra, not Fable, since Fable co-authored the
rank identity). No lane has a genuine runnable object NOW: the discriminator
is a manual note, F10 is deferred, surfaces have no H. No new canonical OPEN
is requested; if ROOT wants one, the quantity and cheapest test are in
section 3. Systems: NO_CHANGE; ROOT's documentary cleanup proceeds alone.

## 6. Custody and checks

All 17 charged inputs hashed fresh and pin-verified at 23:03:22Z (one heredoc typo in my own
expected line for cross-contract.md was caught by direct digest comparison;
the printed digest f865500a…a684 equals the invitation pin). Post-write
re-hash at 23:11:19Z matched all 17; digests generated below. Quantity/cheapest-test check: one
quantity (section 3) with both outcomes and stop rule. Collision check: no
new OPEN identifier; own destination is this file only; no box write.
Word budget: body excluding this section and the header is under 1500 words.

```
08c770deaf7200008e2012269bc70d93267b81f22bc91f85dadf18db40988ba6  CROSS-PINS.json
c7bf5ece33ff3e1a8ea2186ada05d063765a2eefbaebdc2e94af9b4af295cf8a  PINS.json
693d30d398231c599c87dfd3c8c9ea802a59b55b68f9e7565ef888555b910300  approaches.md
c235fca15b48d29860291e26b7c8056915110deb1a9dc15b7ff1a20926d8d4ac  master46-history.md
615ad4f1227a84604877d5e4ad8daef52589ed31e70dcf745af30e6573f3faa7  reduction-interfaces.md
2eea9603f980f37c61f62db16fab72ecb19a8e6520ff4fb3fd6914c0169ecb23  audit-new.md
7f60d1d6f05fbd68e06908e05a69ed3b1dda2b03258a9425462b4a47fbac9ebc  previous-synthesis.md
807118f76508ff61ede6686f0f00108c9a88756eb48a762b49592c899809ab5b  latest-websweep.md
aeaaff1c7ccb6224bca64b931b74a32f12c80d5ace7501c051afcd8b1af16f39  source-selection.md
095c76cc5e8cdf560637025db0993ef8288717edc53d161f20fec55ffb35df88  live-state.md
738eabadef18e32398201faa56de6c9b738fbbe4b7d457e9ce4853b7590207db  common-contract.md
3adb0c5425d0763c86f191107208598a984b0db46b099e5ef385ed54099e104e  ideation-20260911T2240Z-root.md
6cc3eeb61f37222b0ae19115dbe6b357b8f2e3af9892d31b58ace77544b31758  ideation-20260911T2240Z-astra-geometry.md
6450d7e9605a2e8bc21fb5b1dab42425503987e7fd4936e773a17a7a575d92a4  ideation-20260911T2240Z-astra-source.md
cf7b305bd43193b813537bdb6d3012c0fd2e9a47c0d753dd13d21de06749ecd8  ideation-20260911T2240Z-fable5.md
b3e8798345674206c085dda901b89a8e9cdaf96d5821ca96f00915894365020f  ROOT-POSTBLIND-HISTORY.md
f865500ab4fa1a05f22981824786fabe48c35edf40bf657f54e0ea2890e3a684  cross-contract.md
```

postpin_utc: 2026-09-11T23:11:37Z; own WHOLE read performed before the marker; ALL WRITERS IDLE after the marker.

<!-- BODY-END -->
