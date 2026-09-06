# DATA: printed-closure screen on 1,420 operative rows — Grok 4.6 — 2026-09-06

```text
TYPE. DATA (a replay, not a theorem).
N = 0 is DEAD-mod-[printed fixed-list + D1 residues], NOT promoted.
  1,420 rows; 1,330 with N = 0 complete configs; 1,332 with 0 survivors.
  Control: the roster's 66 reproduce the frozen table (109 complete, all
  integral; 102 with I_M ≥ I_m; N = 0 only R063; 0-survivors R001 and R063).
  Cross-tab vs own-data 1,354 empty / 66 singleton:
    1 of 66 singletons has N = 0 (R063);
    25 of 1,354 already-empty rows have N > 0 (all PROP6.3_FINITE_POLE_US1).
  The two necessary-tree notions differ: own-data is a child first-support /
  descent tree; printed N is a source-tower Galois product. A missing
  configuration is not a pair.
```

No new exit-price assertion, so no `charge_basis=` line.

## 0. Custody

Receipt `charged_input_<i>_sha256=`/`_basename=` joined by index with `awk`,
then `sha256sum -c` on `/tmp/jc2-lane.rMDzWM/inputs`: **5/5 OK**. Mathematical
reads were those frozen copies plus
`box/integrality-table-20260906/integrality_table.py` and the gate scripts
`box/exact-contact-gate-20260906/{census_replay.py,closure_fixed.py}` (path
redirect only; identities not rewritten). Row source parametrized to
`box/child-own-v-20260905/enumerated-source-rows.json` (1,420) with own-data
labels from `own-rows.jsonl`. No ledger, no `jc2-lean`, no `ideation-*`, no
fleet. Driver: `box/printed-closure-screen-20260906/printed_closure_screen.py`.
JSON 501 KB. Report+JSON ≤ 2 MB. 0.20 s.

## 1. What was counted

Same packet arithmetic as the frozen integrality table: Moh Def. 5.1(4) p.179
and Prop. 5.3 p.180 send every above-threshold factor along the **same** global
`M`-list with the **actual** centre stabilizer `L` (zero keeps `L`; nonzero
`L ← lcm(L, den δ)`). At `r = 1`, Prop. 4.6 forces squarefree coprime leading
polynomials; `D_1` residues `ρ_f, ρ_g ≡ 0 or 1 (mod A)`, not both 1. `I_M` is
the complete final-major sum; `I_m` is the unsplit minor floor. `CountingClosure`
is imported, not copied. `E####` is the 0-based index in
`enumerated-source-rows.json`; a roster hit keeps `R001`–`R066`.

## 2. Control: the 66

Every roster overlay matches `integrality-table.json` on `N`, integral count,
`I_M ≥ I_m`, survivors, and pair lists. Totals **109 / 109 / 102**. Unique
`(8,8)` on R009 and R050. R001 is `N = 1`, pair `(4,5)`, Cor. 5.3 FAIL. R063
is `N = 0` (empty complete tree: unique actual-`L` `p_3=π^{21}`,
`p_2=π^{12}(π^{10}-c)^3`, zero sibling `D_1` with `A=59` fails residues).

## 3. The 1,420

| | rows | complete `N` | integral | `I_M ≥ I_m` | survivors |
|---|---:|---:|---:|---:|---:|
| all 1,420 | 1,420 | 153 | 153 | 142 | 142 |
| roster 66 | 66 | 109 | 109 | 102 | 102 |
| non-roster | 1,354 | 44 | 44 | 40 | 40 |
| rows with `N > 0` | 90 | | | | |
| rows with `N = 0` | **1,330** | | | | |
| rows with 0 survivors | **1,332** | | | | |

Every complete configuration is integral. `N`-histogram:
`0:1330, 1:70, 2:8, 3:4, 4:1, 6:1, 7:4, 8:1, 9:1`. `s`-dist `3:43, 4:414,
5:797, 6:166`.

## 4. Every `N = 0` row, and every 0-survivor row

**`N = 0` (1,330 rows).** Empty complete tree, typed
**DEAD-mod-[printed fixed-list + D₁ residues]**. Not promoted.

- Among the 66: **R063 only**.
- Among the 1,354 already-empty: **1,329** rows = every empty-own `E####`
  except the 25 in §5. Explicit 1,330-id list: JSON `N0_row_ids`.

**0 survivors (1,332 rows).** The 1,330 empty trees, plus two complete-but-below
rows (Thm 5.1 integer PASS, Cor. 5.3 FAIL):

| id | own | `(n,m)` | `N` | pair | note |
|---|---|---|---:|---|---|
| R001 | singleton | `(84,56)` | 1 | `(4,5)` | Xu §6.2(i); frozen table |
| E0939 | empty / finite-pole | `(192,128)` `M=(-128,152,188,190)` `V=(3,5,3)` | 1 | `(9,10)` | same type as R001 |

JSON `zero_survivor_ids` is the 1,332. `zero_survivor_rows_with_N_gt_0` is
exactly `{R001, E0939}`.

## 5. Cross-tab against own-data (1,354 empty / 66 singleton)

| own-data | rows | `N = 0` | `N > 0` | 0 survivors |
|---|---:|---:|---:|---:|
| singleton | 66 | **1** (R063) | 65 | 2 (R001, R063) |
| empty | 1,354 | 1,329 | **25** | 1,330 (1,329 + E0939) |
| total | 1,420 | 1,330 | 90 | 1,332 |

By own-data partition: `EMPTY_NECESSARY_DATA_US1` 890/890 `N=0`;
`EMPTY_NECESSARY_DATA_US_GE2` 284/284; `U_NEG_US1` 84/84;
`U_NEG_US2_RADIUS_CONDITIONAL` 6/6; `OWN_V_CANDIDATES_US1` 1/46 `N=0` (R063);
`OWN_V_CANDIDATES_US_GE2` 0/20 `N=0`; `PROP6.3_FINITE_POLE_US1` **65 `N=0` /
25 `N>0`** of 90.

The 25 already-empty rows with `N > 0` are **all** `u_s=1` finite-pole tails
(`n ∈ [108,200]`; none `≤ 100`). `E####` `(n,m)` `M` `V` then `N` / integral /
`I_M ≥ I_m` / survivors `(I_M,I_m)`:

```
E0022 (108,72)  (-72,84,104,106) (8,8,3)           1 1 1 1  (16,5)
E0053 (120,80)  (-80,90,115,118) (7,7,4)           1 1 1 1  (21,5)
E0097 (135,90)  (-90,105,130,133) (8,8,4)          2 2 2 2  (16,5)(16,17/2)
E0120 (144,96)  (-96,108,138,142) (7,7,5)          1 1 1 1  (21,8)
E0127 (144,96)  (-96,112,140,142) (8,11,3)         1 1 1 1  (16,9)
E0301 (160,120) (-120,130,155,158) (3,7,4)         2 2 2 2  (9,9)(18,6)
E0344 (162,108) (-108,126,156,160) (8,8,5)         1 1 1 1  (16,17/2)
E0354 (168,48)  (-48,152,164,166) (4,5,3)          1 1 1 1  (8,5)
E0355 (168,72)  (-72,152,164,166) (5,5,3)          1 1 1 1  (15,4)
E0383 (168,112) (-112,126,161,166) (7,7,6)         1 1 1 1  (21,11)
E0415 (180,108) (-108,156,176,178) (7,8,3)         1 1 1 1  (21,6)
E0452 (180,120) (-120,168,176,178) (11,9,3)        1 1 1 1  (22,6)
E0467 (180,120) (-120,132,174,178) (2,9,5)         7 7 6 6  (12,9)(13,10)(16,7)(17,8)(21,6)(22,7)  below (8,11)
E0468 (180,120) (-120,132,174,178) (3,9,5)         7 7 6 6  (13,10)(17,8)(18,9)(21,6)(22,7)(27,6)  below (9,12)
E0475 (180,120) (-120,135,175,178) (7,11,4)        1 1 1 1  (21,10)
E0483 (180,120) (-120,140,176,178) (8,14,3)        1 1 1 1  (16,13)
E0489 (180,120) (-120,140,175,178) (8,11,4)        3 3 3 3  (16,25/3)(16,12)(16,40/3)
E0608 (180,120) (-120,140,170,175,178) (8,8,7,4)   1 1 1 1  (16,10)
E0724 (189,126) (-126,147,182,187) (8,8,6)         3 3 3 3  (16,17/2)(32,13/2)(32,10)
E0771 (192,144) (-144,156,186,190) (3,7,5)         2 2 1 1  (18,9)  below (9,12)
E0773 (192,144) (-144,160,188,190) (11,11,3)       1 1 1 1  (33,6)
E0939 (192,128) (-128,152,188,190) (3,5,3)         1 1 0 0  —  below (9,10)
E0946 (192,128) (-128,144,184,190) (7,7,7)         1 1 1 1  (42,7)
E1263 (200,80)  (-80,184,196,198) (8,5,3)          1 1 1 1  (16,5)
E1279 (200,160) (-160,170,195,198) (5,7,4)         1 1 1 1  (25,7)
```

## 6. How the two necessary-tree notions differ

**Own-data** (the 1,354/66 partition) asks whether a *child* first-support
route exists: Def. 5.1 root-count / Prop. 4.6 degree arithmetic, the source
tree, U-NEG, and Prop. 6.3(2) finite-pole monicity. Empty means no licensed
own `V'`.

**Printed `N`** asks whether the *source* tower admits a Galois-valid complete
sibling product along the fixed `M`-list with actual `L` and `D_1` residues.

They disagree on 26 rows, in both directions:

1. **R063** is a singleton own-child (`V'=(3,7)`) and a printed `N = 0` source
   tree. Own-data does not see the sibling `D_1` residue failure.
2. **25 finite-pole rows** are own-data empty (child leading form not monic in
   `π` at `δ_{s-1}=0`) and printed `N > 0`. The pole is a descent obstruction,
   not a source-tower Galois obstruction. The other 1,329 empties (first-support,
   U-NEG, whole-tree) are `N = 0` under both.

`N = 0` is a kill **only if** the printed closure is a proved necessity of a
realized pair. That licence is left to the gate.

## 7. FALLACY-v2

*Carrier/attainment.* A missing configuration is not a pair. Rows stay
`NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR`. *Floor/attainment.* `I_m`
unsplit is a floor; `I_M` is the complete major sum, not a truncated sibling.
*Pole/interior.* Prop. 4.6 `r=1` is used only at `D_1` after the `κ`-sign
vertex class. *Variable/ring map.* Source `(n,m,M,V)` from the enumerator;
matching names are not a proof. No exit price is declared.

Positive controls: frozen 66, including R009/R050 `(8,8)` and R063 empty.
Replay: `python3 box/printed-closure-screen-20260906/printed_closure_screen.py`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8246`.
- Body SHA-256:
  `3f916fca253f2b58049d92cfffc5d28a96a4316fc3e062daf13e6b5bfc60cd4a`.
- Frozen basis: `15cfb72bc5c3e252d8723968517ddbc60cc7b70a`.
