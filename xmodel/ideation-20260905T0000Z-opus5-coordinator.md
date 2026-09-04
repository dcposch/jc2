# Blind coordinator submission — round 20260905T0000Z (written before reading any other submission)

## Disposition (changes only)
- (99,66) DEGREE-WIDE: PROMOTE from "N1 is a citation gap" to "N1 is a finite, mechanizable kill list" — 5 skeletons left, the batch-3 lane is on them. This is the single closest headline result (resolves a published open case).
- (H2) descent half: DOWNGRADE the "all-K uniform lemma" ambition — the census members are closed, the census is finite, so the uniform-in-K statement is nice-to-have, not on the critical path.
- K16: HOLD as the one true structural OPEN; four lanes sharpened it to an atom; it needs an idea, not another compute lane.

## Q1 (K16 atom) — my answer
Attack the WEAKER (8.1) = τ_t ∈ radical(I_{t,+}), not (V0). The length-split (17(rrrrr)) shows the b₃-axis is the only positive-dimensional component of the cone, and τ_t vanishes on it (banked). So (8.1) reduces to: τ_t ∈ radical on the ZERO-dimensional part (the EN curve Γ's lift) — which is exactly clause (ii) but for τ_t rather than the full nonzerodivisor. Cheapest new idea: τ_t = T_{t,0} is the CONSTANT row; on Γ (where all G_r vanish and rank N = 1), express τ_t via the same (1:β) substitution as W_r and test whether τ_t ∈ (W_1..W_{t−1}) + I₂(N) directly — a radical membership, provable by a valuation on Γ (Γ is CM of dim 1, so a discrete valuation at each point). This sidesteps the nonzerodivisor question. Bounded test: at t=3,4 compute τ_t mod (I₂(N)+(W_r)) and check it's nilpotent.

## Q2 (N1 / degree-wide) — my answer
Kill the 5 (batch-3 running) — do NOT wait for a uniform-in-V argument; the triage shows all 5 are 2271–3441-coeff charts, tractable with the pin+parametrization method that closed S5/K8/K9. On (1)–(13)-completeness: it IS citable — it is Moh's classification (every Keller pair of given degrees has characteristic data satisfying (1)–(13)); the "hole" was never completeness, only that Moh picked one V. So killing all 8 admissible V-assignments closes the degree-wide theorem with Moh's own classification as the only external input. Reconcile the N1 wording in the ledger accordingly.

## Q3 ((H1) census) — my answer
Batched guided_gb sweep with the pin+parametrization preprocessor, NOT a uniform theorem (the augmented Schur row is chart-specific, 17(lllll)/(ttttt) — there is no uniform theorem to find). Price: the method closed S5/K8/K9/S6 in seconds-to-minutes each at ~36 vars; the 296-row census at ~similar cost is ~a few lane-days of batched runs. Build a census-sweep driver on box/lib/ (pin + lower-band parametrization + guided_gb + the verifier) and run it in batches by ascending coefficient count.

## Q4 (the finish) — my answer
YES, the degree-wide method generalises: for each two-point degree (n,m), enumerate the (1)–(13)-admissible skeletons and kill each. (99,66) is the first full instance. Combined with the K16 (H2) prototype and the descent/(T) machinery, the two-point stratum reduces to: (a) the census sweep (mechanizable, compute), (b) the K16-type cofinal rays (the one genuine structural OPEN, per (H2)), (c) the routing maps (first-separation, route-to-state, ordinary-support — still unproved, the real interface gap). The single most valuable next object: FINISH the (99,66) degree-wide theorem (5 skeletons) — it is the first fully-closed degree, a published open case, and the template for the whole census.

## Systems upgrade
Build box/lib/census_sweep.py: a driver that takes a two-point skeleton, applies the pin + exact lower-band parametrization, calls guided_gb, and emits a typed per-skeleton certificate — so the census (and each degree's N1 list) is one batched command, not a hand-built lane per row.

## First lane
`g9966-n1-batch3` is already running (the 5 skeletons). My first NEW lane: the K16 (8.1)-via-radical-on-Γ attack (Q1) — the one structural OPEN, with a concrete new angle (τ_t membership by valuation on the CM curve).

<!-- BODY-END -->
