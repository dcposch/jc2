# DATA: actual-centre stabilizer on the 24,063-row census — Grok 4.6 — 2026-09-06

```text
TYPE. DATA (a convention replay, not a theorem and not a kill).
  Sound-convention operative count: 90 vs 1,420.
  Delta: 1,330 lost, 0 gained. Sets equal printed-closure N=0 / N>0.
  Roster 66: only R063 drops. Residual 64 UNAFFECTED (64/64 remain).
  εN ∈ Z on descend_own zero routes: 44 of 1,420 fail with coarse N;
  0 of 90 fail with actual N.
```

No new exit-price assertion, so no `charge_basis=` line.

## 0. Custody

Receipt `charged_input_<i>_sha256=`/`_basename=` joined by index with `awk`,
then `sha256sum -c` on `/tmp/jc2-lane.adumu9/inputs`: **7/7 OK**. Reads were
those frozen copies plus uncharged repo files `opus5_probe.py` (byte-identical
to the census-coverage snapshot), `closure_fixed.py`, `own_v_routes.py`
(import of charged `descend_own.py`), and `enumerated-source-rows.json` (E####
labels only). No ledger, `jc2-lean`, `ideation-*`, or fleet. Driver:
`box/actual-stabilizer-census-20260906/actual_stab_census.py`. JSON 314 KB.
Report+JSON ≤ 1 MB. 24.3 s. Rows stay
`NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR`.

## 1. How A and the level patterns are computed

**Census / Moh (8) is coarse.** Charged `moh_skeleton_full.py` `Skel.A` /
`Skel.L` (lines 98–107) set `L_j = lcm(den δ_{j+1},…,den δ_s)` and
`A_j = den(L_j δ_j)`, independently of whether the selected factor is the
zero root. `census(..., full=True)` (lines 185–213) threads that same `Lcm`
into (10)/(11) at every level and into (12)/(13) at the bottom
(`A = (Lcm*di).denominator`, line 194; `Lc = lcm(Lcm, den δ_i)`, line 210).
`cond1011` (lines 117–122) is `(10) V≤TRI or (11) V≡SQ (mod A)` on that A.
Level patterns are not enumerated here: only the selected `V` is tested.

**Operative screen `C_FULL_TREE_POLYNOMIAL_ODE` is the same coarse L, now
on every major factor.** `opus5_probe.Tree.node` (lines 70–81) recomputes
`L = lcm(den δ_{j+1..s})` from the current `high` chain and
`A = (L*δ_j).denominator`; `bottom` (83–92) does the same for `A_1`.
`_ok` (137–179) walks `b = z` in `range(P%A, P+1, A)` and orbit
multisets summing to `(P-b)/A`, with per-factor ODE `P≠Qv` and Prop 5.6
danger. `embeds` (209–215) starts at `j=s-1` with `high=(V_s,)`.
`scope_enum.operative` (27–35) is `Tree(gate=False, ode=True)` plus
`recenter=True`. Coarse control: `StabTree(actual=False)` = live
`opus5_probe` on 342 n≤90 rows (0 mismatch) and **1,420** at n≤200.

**Actual centre L** (charged `descend_own.py:151–152`; `own_v_routes.py:71`;
`closure_fixed.py:75,89`): start `L=1`; a zero factor keeps `L`; a nonzero
centre does `L ← lcm(L, den δ)`. Until first nonzero, `A = den(δ)`, not an
accumulated denominator.

## 2. Replay on the 24,063

Same population as the coverage gate: `census(n, Kmin=2, full=True)` for
`16≤n≤200`. Flags of the operative screen held fixed; only L-update rule
changed.

| | rows | s=3 | s=4 | s=5 | s=6 | n≤100 |
|---|---:|---:|---:|---:|---:|---:|
| census (1)–(13) | 24,063 | | | | | |
| coarse operative | **1,420** | 43 | 414 | 797 | 166 | 20 |
| actual operative | **90** | 43 | 45 | 2 | 0 | 6 |
| lost / gained | **1,330 / 0** | 0 | 369 | 795 | 166 | 14 |

All 43 height-three rows survive (at `j=2`, both conventions have `L=1`).
Every s=6 row drops. n≤100: the 14 excess s≥4 rows drop; the six Moh p.202
rows remain (`R001 R002 R003 R004 R007 R015`).

**Roster 66.** Only **R063** `(168,112)` `M=(140,160,166)` `V=(3,21,3)`
(`E0393`) changes: coarse-operative, not actual-operative. Control:
`P_3=V_3=21`, `δ=(3/4, 3/10, 1/5, −1)`, coarse `L_2=5`, `A_2=2`,
`εN=3/5∉Z`; actual `A_2=10`, `εN=3`. The other 65 stay.

**Residual 64** (66 minus R001 Xu and R063): **64/64 still actual-operative.
Unaffected. Confirmed** — own-data already used actual L.

**Set equality (DATA, two screens).** The 90 are exactly printed-closure
`N>0`: 65 roster + the 25 finite-pole rows `E0022, E0053, E0097, E0120,
E0127, E0301, E0344, E0354, E0355, E0383, E0415, E0452, E0467, E0468,
E0475, E0483, E0489, E0608, E0724, E0771, E0773, E0939, E0946, E1263,
E1279`. The 1,330 lost ids equal printed `N=0`. Not a theorem that embed
and printed-complete N are the same test; they coincided here. Full lists:
JSON `actual_rows`, `lost_ids`.

## 3. Additional screen: `εN ∈ Z` on zero routes

A descend_own zero-route is a prefix of selected levels with
`(P−V_i) % den(δ_i) == 0`, first nonzero at `j` with `ε=δ_j`.
`N_coarse = A_j^{Moh (8)}`; `N_actual = den(δ_j)` (`L=1`).

| population | fail |
|---|---|
| 1,420, descend_own prefix, `ε N_coarse ∉ Z` | **44** |
| 1,420, looser coarse-(11) prefix, same N | 1,137 |
| 90, `ε N_actual ∉ Z` | **0** |
| 90, still `ε N_coarse ∉ Z` | 2 (`R066=E0350`, `E0608`) |

The 44 (JSON `epsN_fail_44`) is the R063-type condition. It is strictly
weaker than switching the tree to actual L (1,330). R066 is residual-64
and remains actual-operative: the selected path *embeds* under actual L
(nonzero reading at the higher level) even though a zero-route reading of
the same V has `εN_coarse=1/3`. Not applied as a kill.

## 4. FALLACY-v2

*Carrier/attainment.* A missing actual-L embed is not a pair. *Floor/attainment.*
No I_M / I_m claim. *Target/arrival.* Coarse `A_i` kept distinct from actual
orbit size `N`. *Flag/place/series.* Zero-factor, old-lattice L, and physical
packet stay apart. A convention change is not a kill until gated; counts are
typed DATA. Residual 64 is a status check, not a promotion.

## 5. Verdict

```text
DATA. Sound-convention operative count = 90 (vs 1,420).
  Lost 1,330, gained 0; list = JSON lost_ids / actual_rows.
  Roster 66: only R063 changes. Residual 64: UNAFFECTED (confirm).
  εN ∈ Z (descend_own zero routes): 44 of 1,420 fail with coarse N;
  0 of 90 fail with actual N.
DO NOT PROMOTE: the 1,330 as dead; εN as a kill; any exit price.
  Printed N=0 already typed DEAD-mod-[printed fixed-list + D1 residues],
  not promoted; this tree-screen coincidence is corroboration, not a gate.
```

Replay: `python3 box/actual-stabilizer-census-20260906/actual_stab_census.py`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6159`.
- Body SHA-256:
  `3167a61ae19ae4e39208eedf762934846460e7375c8270e44a08032c858ef818`.
- Frozen basis: `81ac7b6553dd0d57e613bddbb1315fee509667c2`.
