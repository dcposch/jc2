# jc72108

Started as: settle the (72,108) case — the last open degree pair below 125 for
the plane Jacobian Conjecture (GGV–Horruitiner, arXiv:2204.14178, Prop 4.3).
Grown into: a campaign on the remaining structural avenues (sheet-6 exclusion,
DC(2), residue theory, deg ≤ 150 frontier farm).

## Progress

### (72,108) — SETTLED (empty; no counterexample with these polygons)
- [x] Pipeline validated on solved GGV families (14/14 formulation×char combos)
- [x] Subcase (2): EMPTY over ℚ + 3 primes, all strata, audited
- [x] Subcase (1): settled via verified external artifacts (Helali, Suzuki) +
      our audit; own-leaf replication retired (novelty rule)
- [x] Cross-check vs Helali & Suzuki artifacts (three-way agreement)
- [x] Paper 1 drafted + compiled (Lean-checked example); awaiting review
- [x] Certificates: cCa2/cCa6 char-0 lifts RETIRED 2026-08-13 (last-chance rule:
      no LIFT-CERT produced; mod-p verdicts at 3 primes remain the record)
- [ ] Pre-publication riders: reduce4 G4 cross-check

### Vertex-gap program
- [x] Theorem grid (2,2),(2,3),(2,4) + k≥3 impossibility (reviewed)
- [x] conj:R PROVED (Theorem A via Duistermaat-van der Kallen mechanism, adversarially
      reviewed): strip obstruction theory now UNIFORM in (k,d2), char 0
- [x] R functional = Grothendieck residue at toric boundary (3 interpretations
      verified; uniform extra formula; conj:R reduced to rigidity half)

### Sheet-6 (td = 6) exclusion — the active endgame
- [x] Campaign engine: pilot + Λ≤7 table + propagation bash (reviewed)
- [x] Sigray thesis: td≥6 proof shown incomplete as printed; errata E1–E10
- [x] ψ-budget (G2 closed), E5/N1 extraction, AF2 derived, entry-M pin proved
- [x] td ≤ 5: CLOSED (0 survivors). Single-pole td = 6: 4 r9/M2 classes
- [x] td = 7 off-axis book: 62 -> 6 (zero-chain law) -> E5-corrected census
      17 cells UNCONDITIONAL (§11a; H5a RESOLVED: Q+E5 forced). Tower
      TD = 7 PANEL CLOSED (2026-08-14): uniform tower theorem (TOWER-
      UNIFORM.md; 17/17; dual review green; 1559 gates). TD-11: entry-
      clash theorem PROMOTED at exact-core tier (TOWER-TD11.md; all 3
      entry windows close, 11-A intruder mu-robustly dead; 5-round
      review; OPEN residue named: beyond-core px2, 129 nested rows,
      multi-word families). Next: OPEN-residue attack + compiler, then
      td-13 (hard object 13-2b)
- [x] Two-pole (3,3): funneled to rigid template (a₁/a₂ = 2+√3); R6
      print-campaign closed (6/9 dead); 4 branches to coefficient level
- [ ] R1 decisive runs: minimal-branch mod-p screen RUNNING (ultramem);
      (1,2) core queued; chain cores building
- [x] Ops: msolve parenthesis hazard found + 401-file audit (all prior
      verdicts unaffected); emission rules hardened

### DC(2)
- [x] Degree-2 + degree-3 slices (reviewed; slice-scheme divergence at D=3;
      consistent with HOLDS at D ≤ 3); degree-4 sized, parked

### Frontier farm (deg ≤ 150)
- [x] §4 automation + FLINT port + sweep: 34 families, 62 systems emitted
      (7 families honestly out of reduce4 scope)
- [ ] Verdicts: 2 boxes grinding (EMPTYs banking; big char-0 cores need a
      higher-memory retry tier)

Docs: `CAMPAIGN.md` · `AUDIT.md` · `LEMMA.md` · `SURPLUS.md` · `RESIDUE.md` ·
`SHEET6-CAMPAIGN.md` (+ SHEET6-* satellites) · `DC2-PROGRAM.md` · `RECON.md` ·
`notes.md`
