# Shifted child Xu, 46 complete `u_s=1` rows — Grok 4.6 — 2026-09-06

```text
VERDICT.  DATA replay, not a kill.  46/46 licensed (Prop 6.4, V' DETERMINED,
one vector).  140 flat child configs; 86 printed-closure completions.
Every-flat-I'_M-nonintegral: R025–R028, R057, R058, R063 (7).  After printed
closure only R063 still has completions, both non-integral ({33/2, 103/6};
flat 71/4).  The other six have zero printed completions.  R009/R050: I'_M=8
on every surviving closed config, I'_m^l = 8 and 13/2.  Shifted vs unshifted
differ on all 46 (ell=0 tower) and on 35/46 (I'_m) / 25/46 (closure vs flat
I'_M).  The charged R063 kill stays under gate.
```

No new exit-price assertion, so no `charge_basis=` line.

## 0. Custody

Receipt `charged_input_<i>_sha256=`/`_basename=` paired **by index** with `awk`,
then `sha256sum -c` on `/tmp/jc2-lane.u8U4Ga/inputs`: **6/6 OK**. Mathematical
reads were those frozen copies. Live `box/lib/descend_own.py` equals the charged
digest `3fbb5bb885acbd7f50f307ac083a762020b7ca1158e18d06a84a0325b2a3dcc2`.
Uncharged repo reads, declared: `box/xu-ell-shift-20260906/{ell_shift,child_close,child_row_close}.py`
and `box/exact-contact-20260906/child_xu.py` (imported by those scripts). No
ledger, no `jc2-lean`, no `ideation-*`, no fleet. Writes: this report and
`box/child-xu-shifted-20260906/` (`replay.py`, `replay.json` 81 KB). Report+JSON
≤ 1 MB. Calculus not rewritten.

## 1. What was computed

On each of the 46 complete `u_s=1` rows, `descend_own` supplies the licensed
child `(n',m',M',d',V')` and `ℓ = v_s−u_s−1` of the parent (46/46 match).
`'` is a generation label, not a derivative. Xu's `(f,g)` is the roster's
`(g,f)`; `I_M` is symmetric.

- **Shifted flat.** `ell_shift.child_configs` on `child_xu.child_tower(oc,ℓ)`:
  Thm 5.1^ℓ `I'_M` and `I'_m^ℓ = (1+ℓ)+Σ_{P_m}(δ−1−ℓ)` (charged OPEN 2, closed
  in the xu-ell-shift report).
- **Printed closure.** Same loop as `child_row_close.close_row` (depth 3, cap 4):
  major siblings continue by `child_close.search` with actual-centre updates
  `L ← lcm(L, den δ)` on a split. This driver records **every** completion
  `(I'_M,I'_m^ℓ)`, not only survivors.
- **Unshifted.** (U1) the same child with `child_tower(oc,0)`; (U2) Cor 5.3
  `I_m = 1+Σ(δ−1)` on the same shifted packets.

Positive controls against the charged xu-ell-shift report: R009 `I'_M=I'_m^ℓ=8`;
R050 `I'_M=8`, `I'_m^ℓ=13/2`; R063 flat `71/4`, closure `{33/2,103/6}`,
`I'_m^ℓ=2`. 140 flats reproduce both charged 46-row counts.

## 2. Per-row table

Columns: `ell`, `#flat`, `#closed`; unique flat `I'_M` tagged `Z`/`n` (integral?),
`≥`/`<` (`I'_M ≥ I'_m^ℓ`), then `I'_m^ℓ`. `cl:` is the printed-closure `I'_M`
set when it differs from the flat set (`∅` = no completion).

```
row ell nF nC  I'_M Z≥ I'_m^ℓ
R001 1 2 2  4Z<5, 64/7n≥2          cl:4,17/2
R002 2 4 4  13Z≥3, 8Z≥4, 4Z<6
R003 2 2 2  13Z≥3, 9Z≥5
R004 1 1 1  9Z≥3
R005 2 1 1  24Z≥4
R006 1 1 1  18Z≥3
R007 1 2 2  10Z≥5/2, 10Z≥10
R008 4 1 1  36Z≥6
R009 1 2 1  8Z≥8, 592/29n≥2        cl:8
R010 1 3 2  12Z≥3, 138/13n≥2, 6Z≥6 cl:6,12
R011 1 2 1  6Z≥5, 318/23n≥2        cl:6
R013 5 19 14 32Z≥6,24Z≥8,16Z≥10,8Z<12,1456/29n≥6,167/4n≥7,784/19n≥6,632/19n≥8,290/7n≥6,229/7n≥7,173/7n≥9 cl:8,14,16,20,22,24,32
R014 2 4 3  12Z≥4, 6Z≥6, 453/23n≥3 cl:6,12
R017 1 1 1  15Z≥3
R018 3 2 2  20Z≥5, 20Z≥20
R019 1 6 4  18Z≥3, 9Z≥6, 315/19n≥2 cl:9,18
R020 1 12 2 18Z≥3, 9Z≥6, 95/6n≥3, 27/2n≥3, 315/19n≥2, 3533/228n≥2, 1089/76n≥2, 95/12n≥6, 27/4n≥6 cl:9,18
R021 1 3 2  15Z≥7, 15/2n<8, 573/38n≥4  cl:15/2,15
R022 2 2 1  9Z≥5, 315/19n≥3        cl:9
R025 3 4 0  127/4,107/4,91/4 (all n≥)  cl:∅
R026 3 4 0  127/4,107/4,91/4 (all n≥)  cl:∅
R027 3 2 0  127/4,111/4 (all n≥)    cl:∅
R028 3 2 0  127/4,111/4 (all n≥)    cl:∅
R030 3 2 1  32Z≥6, 704/17n≥4       cl:32
R031 1 3 3  16Z≥8/3, 16Z≥25/2
R032 1 2 2  8Z≥5, 37/2n≥2
R033 1 3 3  21Z≥3, 37/2n≥2, 21/2n≥6
R034 1 1 1  9Z≥3
R036 2 4 3  16Z≥4, 8Z≥6, 211/8n≥3  cl:8,16
R037 2 2 1  21Z≥5, 693/23n≥3       cl:21
R039 1 4 3  16Z≥3, 97/6n≥3, 27/2n≥3  cl:27/2,16
R040 1 1 1  16Z≥3
R041 1 1 1  16Z≥4
R042 1 1 1  16Z≥4
R046 1 1 1  21Z≥3
R047 2 8 2  18Z≥5, 22Z≥5, 1226/39n≥3, 86/3n≥3, 1172/39n≥3, 98/3n≥3, 270/13n≥5, 252/13n≥5 cl:18,22
R048 2 2 1  22Z≥5, 98/3n≥3         cl:22
R050 1 3 2  8Z≥13/2, 146/13n≥2     cl:8
R056 1 7 1  16Z≥8, 424/19n≥4, 139/7n≥5, 56/3n≥4, 52/3n≥6 cl:16
R057 3 1 0  209/9n≥5               cl:∅
R058 3 1 0  209/9n≥5               cl:∅
R059 1 1 1  22Z≥5
R060 1 2 2  22Z≥5, 22Z≥14
R061 1 3 3  21Z≥7/3, 21Z≥11
R063 1 1 2  71/4n≥2                cl:33/2,103/6
R064 1 4 4  22Z≥11/4, 22Z≥16, 22Z≥11
```

Totals: 140 flats (69 integral, 3 integral-but-`<` namely R001 `4<5`, R002 `4<6`,
R013 `8<12`, 66 pass both); 86 closures (77 integral, 74 pass both). Full
per-config ledger: `replay.json`.

## 3. Every child `I'_M` non-integral (DATA, not kills)

**Flat (7):** R025, R026, R027, R028, R057, R058, R063.

**Printed closure.** Only **R063** still has completions, and **every** one is
non-integral: `{33/2, 103/6}` (`I'_m^ℓ=2` never binds). R025–R028, R057, R058
have **zero** printed completions (each major sibling returns empty from
`search`). Those six are already without a surviving parent integer in the
charged im-descent replay; R063 is the only row whose parent had a surviving
integer (`19`) and whose licensed child has no integral `I'_M`. Same *shape* as
the charged child-integrality claim; **not promoted** (gate; a configuration is
not a pair).

R001 is not in the list: it has an integer `I'_M=4` with `4<5` (Cor 5.3^ℓ).

## 4. Shifted vs unshifted

All 46 have `ℓ≥1`. Three measured comparisons:

1. **ell=0 tower (U1)** vs Thm 5.1^ℓ: `I'_M` sets differ on **46/46**. 33/46
   have *zero* evaluable ell=0 patterns (A changes; `V'` drops out of the
   Prop 4.6 list) — including R009, R050, R063. 13 rows keep some ell=0
   config, never with the same `I'_M` set.
2. **`I'_m^ℓ` vs `I_m=1+Σ(δ−1)` on the same packets (U2):** differ on **35/46**.
   Equal on 11 (exactly one minor place, so `ℓ(1−N)=0`): R004 R005 R006 R008
   R017 R034 R039 R040 R046 R057 R058.
3. **Printed-closure `I'_M` vs flat `I'_M`** (the earlier replay's child
   values): differ on **25/46** — R001 R009 R010 R011 R013 R014 R019 R020 R021
   R022 R025–R028 R030 R036 R037 R039 R047 R048 R050 R056 R057 R058 R063.
   Typical mechanism: a Galois-illegal flat major-sibling is dropped, or
   splits to a different rational (R001 `64/7→17/2`; R063 `71/4→{33/2,103/6}`).

The earlier replay already used `child_xu` (Thm 5.1 with `1+ℓ−δ`) but not
`I'_m^ℓ` and not printed closure. (2) and (3) are the differences against that
run; (1) shows the radius `ℓ`-shift is not optional.

## 5. Controls

**R009** (192,128)→(48,32), `ℓ=1`, `V'=(2)`. Two flats: `8Z≥8` (no sibling) and
`592/29n≥2` (sibling, no completion). Closed: unique `I'_M=8=I'_m^ℓ`. **Confirmed.**

**R050** (196,56)→(49,14), `ℓ=1`, `V'=(4)`. Three flats: `146/13` dies at the
sibling; two survivors `8Z≥13/2`. Closed `I'_M=8`, margin `3/2`. **Confirmed.**

**R063** (168,112)→(42,28), `ℓ=1`, `V'=(3,7)`. Unique pattern
`p'_3=(π−c)^7`, `p'_2=π^5(π^3−c)^3`. Flat `71/4n≥2`. Closure: two completions
`33/2`, `103/6`, both `n≥2`. **Confirmed non-integral.** Under gate.

## 6. FALLACY-v2

*Floor/attainment.* `I'_M ≥ I'_m^ℓ` is a floor; integrality is Thm 5.1^ℓ + X §2.
*Carrier/attainment.* Rows are `NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR`.
A missing or non-integral child config is not a pair and is not an exit price.
*Prime label.* `'` is the child generation.
*Merge-free.* `V'` from `descend_own`, never a copied parent `V`.
*Replay is data.* 7+1 counts are MEASURED. The charged R063 kill stays under
gate; this lane does not promote it.
*Variable/ring map.* As §1; matching names are not a proof.

## 7. Verdict

The ℓ-shifted child calculus, run on all 46 complete `u_s=1` rows under printed
closure, reproduces the charged R009/R050/R063 numbers and lists seven
all-nonintegral-flat rows, of which only R063 still has printed completions
(all non-integral). Shifted and unshifted values differ on every row at the
tower (`ell=0`) and on 35 (resp. 25) rows for `I'_m` (resp. closed vs flat
`I'_M`). A replay is evidence. Residual unchanged.

Driver: `python3 box/child-xu-shifted-20260906/replay.py`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8605`.
- Body SHA-256:
  `94abc585cb419156ba16e8dc1d930b04ca76d856806f715ba53f1d8609830d4a`.
- Frozen basis: `bfc02c117cda4ad86c0344a67ee0caf9ffb3863e`.
