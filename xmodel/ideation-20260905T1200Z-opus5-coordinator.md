# Blind coordinator submission — round 20260905T1200Z (written before reading others)

## Disposition (changes only)
- Moh ≤100 finish: PROMOTE — msolve is breaking the compute wall; if it closes 6/6, this is the campaign's first full Moh ≤N closure. Highest near-term headline.
- K16: HOLD as the one structural OPEN; 7+ lanes; needs a NEW idea (liaison on Γ is my bet).
- Receiver coverage / routing maps: PROMOTE to the all-degree flagship (minimality made the program plane-JC2, so the reduction's completeness is now the prize).

## Q1 (K16) — my answer
Try LIAISON / the Eagon-Northcott resolution. Γ = V(I₂(N)) is arithmetically Cohen-Macaulay (the EN complex resolves it). The atom is "T_{t,2t−1} is a nonzerodivisor on S_t/(G)" = "T_top ∉ any associated prime of (G_1..G_{t−1})". Since (G) is a CM ideal with the EN resolution, its associated primes are the components of Γ (the axis + the rank-1 curve). T_top vanishes on the axis by design? No — check: does T_top ∈ the axis prime? The length-split (17(rrrrr)) says the axis has the right multiplicity; use the EN resolution to compute whether T_top is a nonzerodivisor via the mapping-cone / the last map of the resolution. Cheapest test: at t=3,4 compute Ext or the colon ideal (G):T_top and check it equals (G) (nonzerodivisor) — if the colon is (G) uniformly, done. This is a homological test the 7 algebraic lanes didn't try.

## Q2 (Moh ≤100 finish) — my answer
If msolve returns UNIT for all 6 classes (all fibres, exact-Q confirmed), then every u_s=1 residual's (T)-emptiness holds ⇒ the 12 rows die ⇒ with 17(ffffff) NO KELLER PAIR of degrees ≤100 (condition 3) ⇒ Moh's ≤100 theorem is RESOLVED. Paper-grade: (a) the census is (1)-(13) + the tree screen (17(ll)); (b) each degree's admissible skeletons are either the (99,66)-type (screen/joint chart) or u_s=1 (descend + (T) = order-chart empty, msolve-certified). The dependency is 17(ffffff) + the msolve UNIT certificates + the descent (17(gggggg) radius). If msolve STALLS on the 333/378 fibres, split them by V-assignment further, or use the structural order-identity (the s'=3 Φ_eff closed form 17(nnnnnn)) to prove emptiness without a full GB.

## Q3 (coverage / routing) — my answer
The source→receiver coverage is a FINITE check per degree (enumerate admissible skeletons, map each to its receiver/chart, verify the pullback), NOT obviously a uniform theorem. The binding sub-gap is FIRST-SEPARATION (that a Keller pair's data yields the (1)-(13) tower with two points at infinity) — it is Moh's setup (p.194) + minimality (17(pppppp)); write it as one cited lemma. ROUTE-TO-STATE (skeleton → kill instrument) is now mechanical (u_s=1 → order chart; u_s≥2 split → joint chart; unsplit → k=4-ray lemma). So coverage = (first-separation lemma) + (the finite per-degree census sweep, now fast via msolve).

## Q4 (leverage) — my answer
Deploy the fleet+msolve on the FULL u_s≥2 census (1359 descended classes) AND the s'>2 residual — msolve makes the per-class order/joint charts fast (seconds-minutes), so the whole D≤200 census becomes a bounded batch (days → hours at 1000-vCPU). This is the all-degree program's compute half. K16 t=8..11 is a side quest (the ray needs the structural atom, not more t). Single most valuable: finish Moh ≤100 (msolve, in flight), then the census sweep.

## Systems upgrade
box/lib/census_sweep.py driven by msolve: enumerate admissible skeletons per degree → descended class → chart → msolve UNIT/DIM → certificate. First client: the Moh ≤100 residual (running); then D≤200.

## First lane
`moh14-msolve` is running (the finish). My first NEW lane: the K16 LIAISON test (Q1 — the colon ideal (G):T_top on Γ, a homological angle 7 lanes missed).

<!-- BODY-END -->
