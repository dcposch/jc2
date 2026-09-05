# Blind coordinator submission — round 20260905T0200Z (written before reading any other submission)

## Disposition (changes only)
- Moh ≤100 (full): PROMOTE to the primary FINISHABLE goal — (99,66) is closed (17(ffffff)); only 14 u_s=1 rows remain, radius-automatic, a lane is on them. This is the closest big headline.
- K16 atom: HOLD as the one structural OPEN; five lanes; Astra now on the named (F3)-Abel target.
- (H1) all-degree: the (K,ℓ)-lattice sweep is the scalable route; build the sweep tool once.

## Q1 (K16 (F3)-Abel rigidity) — my answer
The rigidity B·W'(0)=0 is a statement that the (F3) Abel equation has NO nonconstant polynomial solution off the a₀=0 locus. The cheapest new mechanism I see: a WRONSKIAN/differential-resultant argument. (F3) links C, W, B, b through A=3x³C²/(4y²), D=3bxC/(2y); the condition B·W'(0)≠0 with (F1)-(F3) satisfied is a differential-algebraic system — form the differential resultant of (F3) and its derivative in the ordered-root cover and show it forces W'(0)=0 or B=0. This is coefficient-sensitive (uses A,D linkage), immune to the degree-blind obstruction, and provable uniformly if the resultant's leading coefficient is a unit of A_t. Cheapest test: t=3,4 differential resultant, check it vanishes only at a₀=0.

## Q2 (full Moh ≤100) — my answer
The 14 rows ARE the only residual (17(ll)/(ffffff): the operative screen leaves exactly these at n≤100, all u_s=1). Uniform argument: they are 3 degrees ((90,60),(96,64),(96,72)) × V-assignments; by the (K,ℓ) lattice they descend to a FEW descended classes — likely ≤4 distinct, several sharing. So the descended-class sweep kills them in ≤4 charts, not 14. Price: if each descended chart is ~36-var (like the (99,66) case-A rows), the whole ≤100 residual is a few lane-hours. The moh100-14rows lane is testing exactly this; if it stalls on chart size, apply the pin+parametrization. This is the FINISH of Moh's ≤100 theorem — the single highest-value deliverable.

## Q3 ((H1)/all-degree) — my answer
Two components: (a) a CENSUS SWEEP (mechanizable) via box/lib/census_sweep.py = enumerate admissible skeletons per degree → descended class → pin+parametrization → guided_gb; the (K,ℓ) compression makes it ~1359 classes for 16≤n≤200, tractable in batches; (b) the cofinal K16-type rays (structural, the one true OPEN). The binding routing-map gap is FIRST-SEPARATION (that a Keller pair's data satisfies (1)-(13) with two points at infinity, M_s=n−2) — it is Moh's own setup, citable, but the campaign has never written the citation as a lemma; do that. ROUTE-TO-STATE (which skeleton→which kill instrument) is now mechanical (the (K,ℓ) type determines it).

## Q4 (framing) — my answer
The (H1)∧(H2) framing is sound for the two-point M_s=n−2 stratum, and I do NOT see a missing case WITHIN it: every admissible skeleton is split (joint chart) or unsplit (descend + (T)), and the descent is radius-discharged (17(gggggg)). The genuine incompleteness is at the BOUNDARY: (i) one-place / M_s<n−2 (Abhyankar–Moh territory, a separate program — the campaign should state this scope explicitly and not claim it); (ii) the cofinal K16-type rays are the only INFINITE piece and the one unproved structural statement. Single most valuable next object: FINISH Moh ≤100 (the 14 rows) — it is a complete, famous, citable theorem within reach this session.

## Systems upgrade
box/lib/census_sweep.py (the enumerate→descend→pin→guided_gb→certificate driver) — turns each degree's census into one batched command; first client the 14 ≤100 rows, then the 1359-class general sweep.

## First lane
The 14-row Moh ≤100 lane is running (Opus). My first NEW lane: build census_sweep.py and run it on the 14 rows' descended classes (Q2) — the finish of ≤100. (K16 stays with Astra on the (F3)-Abel target.)

<!-- BODY-END -->
