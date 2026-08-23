VERDICT: STILL-BROKEN

The exact-core arithmetic is sound, but the round-4 document does not consistently restrict its live proof to that tier.

## Findings, ranked

1. **HIGH — the withdrawn beyond-core inference remains in the theorem proof.** The statement correctly makes states beyond the audited region OPEN (`TOWER-TD11.md:352-370`), but its live proof assembly still claims no competing object “anywhere on the budget-9 px2-menu slice — exact core + grammar bound” (`:388-391`). Section 4 likewise says an `M`-preserving route stays below `1/2` “forever” (`:117-120`), and ledger row 8 still credits the false bound `47` (`:461`) immediately before row 9 withdraws it. These are the rejected beyond-core quantifier, not harmless exact-core claims. The stale `LAW-SAFE` comments at `cases/tower_td11.py:659-663,706-707` mirror the same contradiction, although the executable verdict now calls that region OPEN.

2. **LOW — restoration path (a) is itself mis-scoped.** Section 13.0 asks for its numerator/degree inequality on “every state reachable” (`TOWER-TD11.md:514-521`), but it already fails at seed `(3,2)`, where `deg=4` and even `N*=3` gives `1+N*/2=5/2 > 2=deg/2` (the admitted `5/8` row). It is a sufficient restoration condition only for states first reached beyond degree 94, after the exact core and its allowed seed exception are removed. Path (b), the cap-free shared-budget-9 closure, is correctly stated.

3. **CONFIRMED — the exact cores themselves replay.** `python3 cases/tower_td11.py` exits 0 with `58/58`. B9d returns `12/10/8` distinct audited states and zero non-exempt violations. As a sample, `(3,2)` at degree 4 has the admitted clean ratio `5/2` (gap `5/8`); its largest non-exempt seed gap is `7/16`, and the full 12-state core has no other gap at least `1/2`. The theorem aggregate now conjuncts B9.

4. **CONFIRMED — the OPEN inventory is otherwise complete.** Sections 10 and 12 explicitly release the beyond-core/cap-external horizon, all 129 nested 11-C rows, every multi-word-deep configuration, `nu=1` and other resonance-bearing chains, the unknown Q+E5/E5F refile, and unmapped or unaudited decorations/current-state classes. No additional mathematical family from the former quantifier is missing; the remaining defect is that the live §9 proof still reclaims the beyond-core slice it formally released.
