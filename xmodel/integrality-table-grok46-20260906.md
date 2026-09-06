# Corrected integrality table — printed fixed-list closure — Grok 4.6 — 2026-09-06

The complete final-major sum is the Xu quantity `I_M`; a truncated sibling sum is not. Under Moh Def. 5.1(4) p.179 and Prop. 5.3 p.180 (fixed `M`-list, actual centre `L`), there are **109** galois-valid complete configurations on the 66 rows: **all 109** have `I_M ∈ Z` (Xu §2 + Thm 5.1), and **102** also satisfy `I_M ≥ I_m` (Cor. 5.3). **R009 and R050** each have a unique complete survivor with **`I_M = I_m = 8`**. **R001** is excluded by Xu §6.2(i) (`4 < 5`) without Lemma A or B. Of the **19** premature members of the producer’s 924, **10** survive after printed completion and **9** have no galois-valid completion. Two rows have **zero** surviving complete configurations: R001 (known Xu) and **R063** (empty complete tree). R063 is typed below from the printed lines and is **not promoted**. The six claimed row kills remain alive. A configuration is not a pair.

No new exit-price assertion, so no `charge_basis=` line.

## 0. Custody

Receipt `charged_input_<i>_sha256=`/`_basename=` fields were joined by index with `awk` and checked with `sha256sum -c` against `/tmp/jc2-lane.IaL1Mu/inputs`: **4/4 OK**. Mathematical reads were those frozen copies plus the gate scripts/extracts in `box/exact-contact-gate-20260906/`. No ledger edit, no `jc2-lean`, no `ideation-*` input, no fleet. Driver: `box/integrality-table-20260906/integrality_table.py` (reuses `census_replay.py` and `closure_fixed.py`; does not rewrite the identities). JSON 51 KB.

## 1. What is counted

Xu §2 defines `I(f_ξ,g) = deg_x Res_y(f_ξ,g) ∈ Z` (extract `xu.txt:42–44`). Thm 5.1 p.7 equates that integer with `I_M` for a Jacobian pair (`xu.txt:351–352`). Cor. 5.3 is `I_M ≥ I_m` (`xu.txt:396–397`). Orientation: `deg_y f = m` smaller, `deg_y g = n` larger. `I_m` here is the **unsplit** minor floor; a genuine earlier minor split strictly raises it. Moh Def. 5.1(4) and Prop. 5.3 send every above-threshold factor along the **same** global `M`-list, `r → r−1`. At `r=1`, Prop. 4.6 is a nonzero constant (`moh.txt:1646–1648`), so `D_1` is final, squarefree and coprime. Actual centre: zero factor keeps `L`; a nonzero factor sets `L ← lcm(L, den δ)`. Final residues: `ρ_f, ρ_g ≡ 0 or 1 (mod A)`, not both `1`.

The producer’s 1,080 objects use coarse `L_i = lcm(den δ_{i+1},…,den δ_s)`. That lattice is larger than the printed stabilizer (R063: 509 coarse level-2 patterns versus one actual-`L` pattern). The corrected table enumerates complete trees in the printed model. Pair-sets on the nine gate targets match `closure-fixed-results.json` exactly.

## 2. Per-row table

Columns: complete trees `N`; how many have `I_M ∈ Z`; how many have `I_M ≥ I_m`; how many survive both; surviving `(I_M,I_m)` pairs. Extra complete-but-below pairs: R001 `(4,5)`; R002 `(4,6)` (Xu §6.1(ii)); R013 `(8,12)`; R023/R024 one each; R025/R026 `(8,10)`.

```
row  N int ge sv  survivors
R001 1 1 0 0  (4,5) Cor.5.3 fail
R002 2 2 1 1  (8,4)
R003 1 1 1 1  (9,5)
R004 1 1 1 1  (9,3)
R005 1 1 1 1  (24,4)
R006 1 1 1 1  (18,3)
R007 1 1 1 1  (10,4)
R008 1 1 1 1  (36,6)
R009 1 1 1 1  (8,8)
R010 1 1 1 1  (12,3)
R011 1 1 1 1  (6,5)
R012 1 1 1 1  (21,7/2)
R013 3 3 2 2  (16,10)(24,8)
R014 2 2 2 2  (6,6)(12,4)
R015 1 1 1 1  (16,8/3)
R016 1 1 1 1  (9,17/2)
R017 1 1 1 1  (15,3)
R018 1 1 1 1  (20,5)
R019 1 1 1 1  (18,3)
R020 1 1 1 1  (18,3)
R021 1 1 1 1  (15,7)
R022 1 1 1 1  (9,5)
R023 7 7 6 6  (12,15/2)(13,17/2)(16,11/2)(17,13/2)(21,9/2)(22,11/2)
R024 7 7 6 6  (13,17/2)(17,13/2)(18,15/2)(21,9/2)(22,11/2)(27,9/2)
R025 9 9 8 8  (12,8)(13,9)(16,6)(17,7)(21,5)(22,6)
R026 8 8 7 7  (12,8)(13,9)(16,6)(17,7)(21,5)
R027 6 6 6 6  (13,9)(17,7)(18,8)(21,5)(22,6)
R028 4 4 4 4  (13,9)(17,7)(18,8)(22,6)
R029 1 1 1 1  (10,5/3)
R030 1 1 1 1  (32,6)
R031 1 1 1 1  (16,5)
R032 1 1 1 1  (8,5)
R033 1 1 1 1  (21,3)
R034 1 1 1 1  (9,3)
R035 2 2 2 2  (9,15/2)(18,9/2)
R036 2 2 2 2  (8,6)(16,4)
R037 1 1 1 1  (21,5)
R038 1 1 1 1  (16,23/4)
R039 1 1 1 1  (16,3)
R040 1 1 1 1  (16,3)
R041 1 1 1 1  (16,4)
R042 1 1 1 1  (16,4)
R043 1 1 1 1  (21,23/3)
R044 1 1 1 1  (8,7/2)
R045 1 1 1 1  (15,5/2)
R046 1 1 1 1  (21,3)
R047 2 2 2 2  (18,5)(22,5)
R048 1 1 1 1  (22,5)
R049 3 3 3 3  (10,10)(20,5)(20,25/2)
R050 1 1 1 1  (8,8)
R051 1 1 1 1  (25,11/2)
R052 1 1 1 1  (21,11/3)
R053 1 1 1 1  (28,7/3)
R054 1 1 1 1  (16,7/2)
R055 1 1 1 1  (16,44/5)
R056 1 1 1 1  (16,8)
R057 1 1 1 1  (18,6)
R058 1 1 1 1  (18,6)
R059 1 1 1 1  (22,5)
R060 1 1 1 1  (22,5)
R061 1 1 1 1  (21,7/2)
R062 1 1 1 1  (33,11/4)
R063 0 0 0 0  EMPTY
R064 1 1 1 1  (22,6)
R065 1 1 1 1  (22,6)
R066 1 1 1 1  (16,17/2)
```

R009/R050: `N = sv = 1` and the only pair is `(8,8)`. R014 and R049 also have a margin-zero pair, each among several survivors, so those contacts are not pinned.

## 3. The 19 premature terminations

All 19 lie in the 924, on R022(1), R025(3), R026(4), R027(2), R028(2), R047(4), R048(1), R057(1), R058(1). Flat `I_M` assumed immediate `D_1` for a major sibling born at level ≥ 3. Printed continuation is one more nonfinal `D_2` then final `D_1`.

| row | idx | flat `I_M` | flat `I_m` | status | `N` | sv | surviving pairs |
|---|---:|---|---:|---|---:|---:|---|
| R022 | 1 | 801/49 | 4 | NO_GALOIS | 0 | 0 | — |
| R025 | 0 | 244/11 | 8 | SURVIVES | 3 | 2 | (12,8)(13,9) |
| R025 | 1 | 288/11 | 6 | SURVIVES | 3 | 3 | (12,8)(16,6)(17,7) |
| R025 | 2 | 343/11 | 5 | SURVIVES | 3 | 3 | (17,7)(21,5)(22,6) |
| R026 | 0 | 91/4 | 7 | SURVIVES | 4 | 3 | (12,8)(13,9)(17,7) |
| R026 | 1 | 107/4 | 5 | SURVIVES | 4 | 4 | (12,8)(16,6)(17,7)(21,5) |
| R026 | 2 | 53/2 | 6 | NO_GALOIS | 0 | 0 | — |
| R026 | 3 | 877/28 | 5 | NO_GALOIS | 0 | 0 | — |
| R027 | 0 | 299/11 | 7 | SURVIVES | 3 | 3 | (13,9)(17,7)(18,8) |
| R027 | 1 | 343/11 | 5 | SURVIVES | 3 | 3 | (17,7)(21,5)(22,6) |
| R028 | 0 | 111/4 | 6 | SURVIVES | 4 | 4 | (13,9)(17,7)(18,8)**(22,6)** |
| R028 | 1 | 63/2 | 5 | NO_GALOIS | 0 | 0 | — |
| R047 | 1 | 654/23 | 4 | NO_GALOIS | 0 | 0 | — |
| R047 | 3 | 9330/299 | 4 | NO_GALOIS | 0 | 0 | — |
| R047 | 5 | 8916/299 | 4 | NO_GALOIS | 0 | 0 | — |
| R047 | 7 | 746/23 | 4 | NO_GALOIS | 0 | 0 | — |
| R048 | 1 | 746/23 | 4 | NO_GALOIS | 0 | 0 | — |
| R057 | 0 | 1899/83 | 6 | SURVIVES | 1 | 1 | (18,6) |
| R058 | 0 | 209/9 | 5 | SURVIVES | 1 | 1 | (18,6) |

R028’s coarse `111/4` becomes integer `22` on the same selected path, matching the gate certificate. The six claimed dead rows all retain survivors. R022/R047/R048 keep other complete survivors; their premature configs die at `D_1` residues.

## 4. Zero-survivor rows (typed, not promoted)

**R001.** Two coarse patterns. `(z=0; 2,1)` is complete: `I_M=4`, `I_m=5`, Thm 5.1 integer PASS, Cor. 5.3 FAIL — Xu §6.2(i) verbatim. `(z=7; 2)` is forced final at `δ=7/17`, `A=17`, `ρ_f=14`, galois FAIL (`152/17`). No remaining major index. Exclusion does not use Lemma A or B.

**R063** (`n,m)=(168,112)`, `M=(-112,140,160,166)`, `V=(3,21,3)`. Printed closure, not the coarse 509:

1. Def. 5.1(4) p.179 / the note after it (`moh.txt:2137–2148`): every tower uses the **fixed** characteristic list; any above-average subdisc of `D_s` may be `D_{s-1}`.
2. Prop. 5.3 p.180 (`moh.txt:2157–2179`) and p.200(4) (`moh.txt:3231–3247`): a factor with `V_r > d_r/(n-M_r)` continues to `D_{r-1}` with the **same** `M_{r-1}`, `d_{r-1}`. No free inserted `W`.
3. Unique `D_3` pattern containing `V_3=21`: `p_3=π^{21}` (zero factor). Actual `L` stays 1.
4. Unique `D_2` pattern containing `V_2=3` at actual `A=den(Lδ)=10`: `p_2=π^{12}(π^{10}-c)^3`.
5. The zero sibling is major (`ρ_f=24`, `κ=14`). Prop. 5.3 sends it to final `D_1`. Prop. 4.6 r=1 (`moh.txt:1646–1648`) forces squarefree coprime leading polynomials. That disc has `δ=24/59`, `A=59`, `ρ_f=24 ̸≡ 0,1 (mod 59)`: galois FAIL. The selected arm (`ρ_f=6`, `δ=3/4`, `A=2`) is legal, but the product is empty.

So `N=0`. The producer’s one flat survivor `I_M=19` used coarse `L=5`, `A=2` at `D_2` and never tested the sibling’s actual `D_1`. Typed **DEAD-mod-[printed fixed-list + D_1 residues]**. **Not promoted:** a missing complete configuration is not a polynomial pair (FALLACY-v2 carrier/attainment). Residual 65 is unchanged.

## 5. FALLACY-v2

A truncated major sum is not `deg_x Res_y`. A configuration is not a pair. `I_m` unsplit is a floor. `ρ` counts roots, `A` is a Galois increment, `M` is global eta-characteristic data. Thm 5.1 is applied as a necessary integer test on complete trees, never as existence. No exit price is declared.

Replay: `python3 box/integrality-table-20260906/integrality_table.py`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8643`.
- Body SHA-256:
  `027d844c0ba466332962851d26216e340c41893a3690f00fdab334a98beb28a3`.
- Frozen basis: `44e7aefaf955b5d9406481b6bc058f07bbe61913`.
