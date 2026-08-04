# jc72108

Settle the (72,108) case — the last open degree pair below 125 for the plane
Jacobian Conjecture (GGV–Horruitiner, arXiv:2204.14178, Prop 4.3).

## Progress

- [x] Pipeline validated on solved GGV families (14/14 formulation×char combos)
- [x] Subcase (2): EMPTY over ℚ + 3 primes, all strata, audited
  - [x] generic chart — explicit symbolic contradiction (vertex–gap)
  - [x] a2 = 0 branch
  - [x] a6 = 0 branch (char-0: 17.7 h / 761 GB)
- [ ] Subcase (1): 8 branch leaves computing (rev order, 2 boxes)
- [x] Vertex-gap theorem, (2,2) regime (LEMMA + SURPLUS, adversarially reviewed)
- [x] Cross-check vs Helali & Suzuki artifacts (three-way agreement)
- [ ] Certificates (chartG: 1-term cofactor done; cCa2/cCa6 lifts pending)
- [ ] §4 reduction automation → family farm (designed; pending quota + FLINT port)
- [ ] Write-up + open-source release (awaiting go-ahead)

Docs: `CAMPAIGN.md` · `AUDIT.md` · `LEMMA.md` · `SURPLUS.md` · `notes.md` · `plan-72-108.md`
