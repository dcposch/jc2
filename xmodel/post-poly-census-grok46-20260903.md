# Post-POLY census: live targets re-based on C_FULL_TREE_POLYNOMIAL_ODE

Lane: Grok 4.6. `post-poly-census-grok46-20260903`. Desk only. Canonical
ledgers not edited. `jc2-lean` not inspected. No `ideation-*` file opened.
No running-lane report opened. `FALLACY-v2` in force. No new exit-price
assertion, so no `charge_basis` line. Everything below is **MEASURED**.
Screen survival is not existence.

Operative screen: `C_FULL_TREE_POLYNOMIAL_ODE`
(`full_tree_polynomial_ode_ok`: POLY fires only at integral `δ ≤ 0` on the
selected path; ungated Prop. 5.6). Descent radii: `Φ_eff` (AUDIT 17(dd);
charged `measure_anchor.py`): Prop. 6.3 image, drop terminal `M' = n'−1`,
set `V_{s*+1} = d_{s*+1}`, then `δ' = (k+1)·Def 5.1(3)`. Two-point means
`δ₂' = −1`. Groups: `(n, m, M, V_s)`. UNI: integer `N = k V₂ q ≥ 6`.

## 0. Custody and hashes

Frozen inputs `/tmp/jc2-lane.XV31nc/inputs`, SHA-256 verified by
`awk` from `xmodel/post-poly-census-grok46-20260903.run.v2` then
`sha256sum -c` (11/11 OK) before any read:

```text
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  full_tree_partition.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full.py
36b374b21b3768e841ad2cc2168d7e669d9b0d6e6b6c8d1737d203acbd079067  nested_pack.py
360a7baae7d148edd34ad2769f95d996af0a7e31ec4165bbc9295fa4ab7a42b3  construct_ray.py
17b03f70564ae7c621c55e4a80f607d821f2d2ede305109f78cf23223b4fce7e  ray-B-verified.json
4a5866d5e655add9ee37c6d684e2e12b017da3d8d5a52040d5b4e89a2ac372f6  measure_anchor.py
4bcb512d47cf9f935c6a2c0c7b8251ae16b3e4f73b4794abbef2d1702846c7c1  phi_delta.py
0a77eb88048fbc50dd4c09391376c6e79d03e410a0e614f8e43c59cd0e40713e  rigid-congruence-grok46-20260903.md
693b206806a75a557bfb02683fc7b937d0529a677b4b7476cac3b4c9a151cd0e  dessin-tower-dim-grok46-20260903.md
5c5d0e132196b3110c9027d220244534b5763a7d311bcc8efb7219ac596bfa77  descent-anchor-audit-grok46-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
```

Drivers: byte copies in `box/postpoly-20260903/` (not modified in
place). Rays via `construct_ray.py` (`k16_family`, `de_fixed_family`,
`try_skel`). UNI: `moh_skeleton_full.uni_hits`. `nested_pack.py` not
run (`knapsack_v2` uncharged). Script: `measure_postpoly.py`.

---

## Direct answer

1. **K=16 ray survives POLY.** All eight members `t=1..8` pass TREE, ODE,
   POLY, and POLY+ODE. No POLY site (no integral `δ ≤ 0` on the selected
   path). All are `u_s=1`, `s_eff=2`, two-point `δ₂' = −1`,
   `(n',m'; M₂'; V₂'; k) = (12t+4, 8t+4; 12t+1; 3; 1)`, `N=6t+3`.
2. **`(d,e)`-fixed AP dies under POLY.** On `t=6+9k`, `k=0..5`
   (`n=252,468,684,900,1116,1332`) TREE and ODE still hold, POLY kills
   every member at node `j=3` (`δ₃=0` integral, `A=1`, `P=9`, `Q=3`,
   selected `V₃=8`; failure `selected V path not embeddable; zero-major
   child infeasible`). The D=108 seed `t=0` **survives** POLY+ODE
   (same `δ₃=0` site). The AP is not a POLY-screened cofinal ray.
3. **Rigid stratum: 0/19 POLY.** The 16 already dead at ungated TREE die
   at `j=2` (5) or `j=3` (11). The 3 previous gapped TREE/ODE survivors
   die at POLY `j=3` (`δ₃=0`, `A=1`). No rigid POLY survivor, so no
   rigid `Φ_eff` compiler client.
4. **D=108: 20 ODE → 9 POLY** (6 groups, 5 UNI). One `u_s=2`; eight
   `u_s=1`. The seed `(84,104,106; 8,8,3)` lives; the rigid
   `(90,99,106; 17,16,8)` dies.
5. **`48≤D≤200` POLY+ODE: 1,420 rows / 686 groups / 459 UNI** (banked
   17(hh) reproduced). Empty among baseline-active: 27 degrees; newly
   empty vs ODE: `{72, 80, 100, 176}`. `u_s>1` is **310 rows / 177
   groups** — equal to the ODE `u_s>1` residue; POLY did not cut it.
6. **New Appendix-II target list: 17 two-point `s_eff=2` `u_s=1`
   groups** (18 rows; all UNI). Includes Moh `(64,48)`, `(75,50)` both
   `V₂`, `(84,56) V₂=5`, and K=16 at `t=1,2,3`. The 14-row `n≤100`
   excess is all `u_s=1`, `s≥4`; none of it is two-point `s_eff=2`.

---

## 1. Controls (fail-closed)

Printed before any result number. All passed.

| control | measured | expected |
|---|---|---|
| p.207 `Φ` 10/10 MATCH (charged `def51`) | 10/10 | 10/10 |
| Moh's six survive TREE, ODE, POLY, POLY+ODE | 6/6 | 6/6 |
| `n≤100` (1)–(13) rows / `(n,m)` classes | 658 / 63 | 658 / 63 |
| `n≤100` ODE / POLY+ODE rows | 58 / 20 | 58 / 20 |
| `n≤100` POLY+ODE classes / excess | 7 / 14 | 7 / 14 |
| `D=108` ODE rows | 20 | 20 |
| `48≤D≤200` `K_min=16` (1)–(13) / ODE | 23,720 / 2,824 | 23,720 / 2,824 |
| `48≤D≤200` POLY+ODE rows/groups/UNI | 1,420 / 686 / 459 | 1,420 / 686 / 459 |

`(75,50)` POLY+ODE residue remains `{M₂=55, V₂∈{2,3}}`.

---

## 2. (1) Two rays under POLY

Construction via charged `construct_ray.py`.

### 2.1 K=16: `n=48t+16`, `m=32t+16`, `M=(n−12,n−2)`, `V=(3,3)`

All `t=1..8` defined (1)–(13). POLY sites: none. Killing node: none.

```text
 t    n    m   TREE ODE POLY POLY+ODE  N   n'  m'  M'   V' k  δ₂'
 1   64   48     1   1   1      1      9  16  12  13    3 1  −1
 2  112   80     1   1   1      1     15  28  20  25    3 1  −1
 3  160  112     1   1   1      1     21  40  28  37    3 1  −1
 4  208  144     1   1   1      1     27  52  36  49    3 1  −1
 5  256  176     1   1   1      1     33  64  44  61    3 1  −1
 6  304  208     1   1   1      1     39  76  52  73    3 1  −1
 7  352  240     1   1   1      1     45  88  60  85    3 1  −1
 8  400  272     1   1   1      1     51 100  68  97    3 1  −1
```

`t=1` is Moh `(64,48)`. `u_s=1`, drop=0, `s_eff=2`, two-point identically.
`REPRESENTATIVE` of a screened family, not `FULL_ACTUAL_EXIT`.

### 2.2 `(d,e)`-fixed: seed `(108,72; M=(84,104,106); V=(8,8,3))`

Closed form of rigid-congruence §4.1, `λ=8`, `V₂`-slope 2, `V₃`-slope 0.
AP `t=6+9k`, `k=0..5`. Radii frozen `δ=(−1, 0, 1/3, 4/9)` (`δ₄..δ₁`);
POLY site `j=3`, `δ₃=0` on every member including the seed.

```text
 t  k     n  TREE ODE POLY POLY+ODE  kill j=3
 0  —   108     1   1   1      1     (seed lives; V₂=8)
 6  0   252     1   1   0      0     A=1 P=9 Q=3 V₃=8
15  1   468     1   1   0      0     same
24  2   684     1   1   0      0     same
33  3   900     1   1   0      0     same
42  4  1116     1   1   0      0     same
51  5  1332     1   1   0      0     same
```

Seed `Φ_eff`: drop 1, `(n',m'; M'; V'; k)=(27,18; 21; 8; 1)`,
`s_eff=2`, `δ'=(0, −2/5)`, not two-point. AP members have the same
`(δ₃, A, P, Q, V₃)` and the same `δ₂' = −2/5` after drop; they die
before descent is a screen question. The cofinal `(d,e)`-fixed
construction of 17(aa) is **not** POLY-live past `t=0`.

---

## 3. (2) 19 rigid expdim-0 assignments

Recovered uniquely as (1)–(13) skeletons (dessin-tower-dim §6.4 /
rigid-congruence §2). `P` = POLY+ODE. Side: `T` = TREE, `O` = ODE.
`j` = killing node under POLY+ODE.

```text
 n   m   M                 V         us T O P  j  POLY site
 60  40  -10,45,58         11,8,4     1 0 0 0  3  —
 80  60  68,78             7,3        1 0 0 0  2  —
 84  63  49,82             7,5        2 0 0 0  2  —
 96  72  -8,20,94          7,6,3      1 0 0 0  3  —
 96  72  -8,76,94          7,6,3      1 0 0 0  3  —
 96  72  56,92,94          7,5,3      1 1 1 0  3  δ₃=0
 96  72  80,84,94          7,6,3      1 0 0 0  3  —
100  75  85,98             7,3        2 0 0 0  2  —
108  72  60,80,106         20,9,3     1 0 0 0  3  —
108  72  60,100,106        20,9,3     1 0 0 0  3  —
108  72  90,106            17,16      2 0 0 0  2  —
108  72  90,99,106         17,16,8    1 1 1 0  3  δ₃=0
120  72  12,44,118         8,9,3      1 0 0 0  3  —
120  72  12,76,118         8,9,3      1 0 0 0  3  —
120  90  -10,25,118        7,6,3      2 0 0 0  3  —
120  90  -10,95,118        7,6,3      2 0 0 0  3  —
120  90  100,105,118       7,6,3      2 0 0 0  3  —
120  80  88,118            17,7       1 0 0 0  2  —
120  80  100,110,118       17,16,9    1 1 1 0  3  δ₃=0
```

**0 / 19 POLY.** The 3 TREE/ODE leftovers die at POLY `j=3`, `A=1`,
selected `V₃ ∈ {5,16,16}`. No rigid `Φ_eff` compiler client.

---

## 4. (3) D=108: 20 ODE → 9 POLY

All 20 ODE rows at `K_min=16`. POLY kills 11, all at `j=3` with a
`δ₃=0` site (`A=1`). Survivors (9 rows / 6 groups / 5 UNI):

```text
M                    V         us N         s_eff  drop  (n',m'; M'; V'; k)     δ₂'   two
81,106               7,7        2 21        —      —     NOT-US1                 —     —
60,100,106           1,4,3      1 []        3      0     (27,18; 15,25; 1,4; 1) −2/3   n
84,104,106  (seed)   8,8,3      1 16        2      1     (27,18; 21; 8; 1)      −2/5   n
24,78,106            1,1,5      1 6..15     3      0     (18,12; 4,13; 1,1; 3)   1/2   n
24,78,106            1,4,5      1 6..20     3      0     (18,12; 4,13; 1,4; 3)  −2/3   n
48,90,106            1,1,5      1 6         3      0     (18,12; 8,15; 1,1; 3)   3/2   n
48,90,106            1,3,5      1 6,9,12    3      0     (18,12; 8,15; 1,3; 3)   −1    Y
-18,60,106           2,15,5     1 24        3      0     (18,12; −3,10; 2,15; 3) −1/2  n
-18,60,106           11,15,5    1 []        3      0     (18,12; −3,10; 11,15; 3)−1/2  n
```

Only one D=108 POLY row is two-point, and it has `s_eff=3` (not a
direct Appendix-II `s'=2` client). The seed is `s_eff=2` but
`δ₂' = −2/5 ≠ −1`.

Dead ODE rows (all `j=3`, `δ₃=0`): the other 11, including rigid
`(90,99,106; 17,16,8)` and the `V₃=7` siblings of the seed.

---

## 5. (4) `48≤D≤200` POLY+ODE residue

Baseline-active degrees: 58. ODE-active: 35. POLY-active: 31.
POLY empty among baseline-active (27):

`48, 54, 60, 63, 72, 80, 81, 88, 100, 102, 104, 105, 110, 114, 117,
130, 152, 153, 154, 170, 174, 176, 182, 184, 186, 190, 195`.

Newly empty versus ODE: **`{72, 80, 100, 176}`**. `D=105, 117` stay
empty (already TREE-empty). `D=108` 9/6/5; `D=112` 1/1/1 (K=16 `t=2`);
`D=120` 44/23/14.

Row partition by `u_s` × `s_eff` after `Φ_eff` × (`δ₂' = −1` vs not).
`u_s>1` is not descended (`NOT-US1`). Group cell-counts may overlap
when `s_eff>2` (`δ₂'` is V-path-dependent); row counts partition 1,420.
Unique groups: 686 = 509 `u_s=1` + 177 `u_s>1`.

| `u_s` | `s_eff` | two-point | rows | groups (cell) | UNI groups (cell) |
|---|---:|---|---:|---:|---:|
| =1 | 2 | `δ₂'=−1` | 18 | 17 | 17 |
| =1 | 2 | not | 30 | 28 | 27 |
| =1 | 3 | `δ₂'=−1` | 18 | 15 | 14 |
| =1 | 3 | not | 312 | 189 | 115 |
| =1 | 4 | `δ₂'=−1` | 17 | 10 | 10 |
| =1 | 4 | not | 579 | 235 | 172 |
| =1 | 5 | not | 136 | 35 | 21 |
| >1 | NA | NA | 310 | 177 | 103 |

`u_s>1` rows/groups = 310 / 177, matching the ODE `u_s>1` residue
exactly (POLY killed 1,404 of 2,514 ODE `u_s=1` rows and 0 of 310
`u_s>1` rows).

### 5.1 Target list: two-point `s_eff=2` `u_s=1` groups (17)

Appendix II compiler's direct clients under the operative screen.
All UNI. `V'` is `V₂'` after drop; `(75,50)` has two V-paths.

```text
 n    m  M                    Vs s drop  n'  m'  M'   V₂' k  N
  64  48  52,62                3 3    0  16  12  13    3  1  9          K=16 t=1
  75  50  55,73                4 3    0  15  10  11  2|3  2  8,9        Moh both V₂
  84  56  72,82                3 3    0  21  14  18    5  1  10         Moh V₂=5
 112  80  100,110              3 3    0  28  20  25    3  1  15         K=16 t=2
 125  75  105,123              4 3    0  25  15  21    2  2  6,12
 132  88  120,130              3 3    0  33  22  30    8  1  8,12,16
 147  98  105,145              6 3    0  21  14  15    6  4  36
 160 112  148,158              3 3    0  40  28  37    3  1  21         K=16 t=3
 168 112  126,161,166          6 4    1  24  16  18    7  4  21
 175 100  155,173              4 3    0  35  20  31    2  2  8,16
 175 125  155,173              4 3    0  35  25  31    3  2  21
 180 120  168,176,178          3 4    1  45  30  42   11  1  11,22
 180 144  150,178              5 3    0  30  24  25    4  3  16,32
 189 126  147,182,187          6 4    1  27  18  21    8  4  16,32
 192 128  136,190              7 3    0  24  16  17    2  5  6..28
 196  56  184,194              3 3    0  49  14  46    4  1  6,8,10
 200 120  188,198              3 3    0  50  30  47    7  1  21
```

Moh `(84,56) V₂=2` is POLY-live, `s_eff=2`, **not** two-point
(`δ₂' = −1/2`); it is not on this list. Three groups have `drop=1`
(p.174). K=16 `t≥4` (`n≥208`) lies outside `D≤200`.

---

## 6. (5) `n≤100` 14-row excess and `Φ_eff`

20 POLY+ODE rows / 7 classes: Moh's six (`s=3`) plus 14 excess, all
`u_s=1`, all `s≥4`, classes `(90,60)×4`, `(96,64)×4`, `(96,72)×6`.
`s=3` at `n≤100` is exactly Moh's six. None of the 14 is two-point
`s_eff=2`. `s_eff`: 13 at 3 (drop 0), 1 at 4 (the `s=5` row). Two
rows are two-point at `s_eff=3` (not compiler-direct).

```text
(n,m) M                    V            N      s_eff  (n',m'; M'; V'; k)           δ₂'   two
90,60 10,45,88             1,8,4        10,15     3  (18,12; 2,9; 1,8; 2)        −1/3   n
90,60 10,45,88             3,8,4        18        3  (18,12; 2,9; 3,8; 2)        −1/3   n
90,60 45,80,88             2,5,4        8         3  (18,12; 9,16; 2,5; 2)       −3/2   n
90,60 45,80,88             3,5,4        []        3  (18,12; 9,16; 3,5; 2)       −3/2   n
96,72 -60,56,94            1,9,3        []        3  (24,18; −15,14; 1,9; 1)     −1/6   n
96,72 36,80,94             1,9,3        9         3  (24,18; 9,20; 1,9; 1)       −1/2   n
96,72 36,80,94             4,9,3        []        3  (24,18; 9,20; 4,9; 1)       −1/2   n
96,72 36,78,94             1,1,5        6         3  (16,12; 6,13; 1,1; 3)        3/2   n
96,72 36,78,94             1,3,5        6,12      3  (16,12; 6,13; 1,3; 3)        −1    Y
96,72 36,78,94             4,3,5        []        3  (16,12; 6,13; 4,3; 3)        −1    Y
96,64 48,68,94             2,1,3        8         3  (24,16; 12,17; 2,1; 1)       1/2   n
96,64 48,68,94             1,2,3        6         3  (24,16; 12,17; 1,2; 1)        0    n
96,64 48,68,94             3,2,3        9         3  (24,16; 12,17; 3,2; 1)        0    n
96,64 -48,-8,20,94         1,1,6,3      6..18     4  (24,16; −12,-2,5; 1,1,6; 1)  0    n
```

---

## 7. (6) Moh's six; runtime

All six survive TREE, ODE, POLY, POLY+ODE. `Φ_eff`:

| row | `u_s` | `(n',m'; M'; V'; k)` | `s_eff` | `δ₂'` | two-point |
|---|---:|---|---:|---|---|
| `(64,48)` | 1 | `(16,12; 13; 3; 1)` | 2 | `−1` | Y |
| `(84,56) V₂=2` | 1 | `(21,14; 16; 2; 1)` | 2 | `−1/2` | n |
| `(84,56) V₂=5` | 1 | `(21,14; 18; 5; 1)` | 2 | `−1` | Y |
| `(75,50) V₂=3` | 1 | `(15,10; 11; 3; 2)` | 2 | `−1` | Y |
| `(75,50) V₂=2` | 1 | `(15,10; 11; 2; 2)` | 2 | `−1` | Y |
| `(99,66)` | 3 | `NOT-US1` | — | — | — |

Wall 39.77 s, one core, Python 3 stdlib + charged drivers (degree-scan
36.57 s). Peak RSS well under 4 GB.

---

## 8. FALLACY-v2

No new exit-price. POLY+ODE survival is a finite DP on (1)–(13)
skeletons, not a Jacobian pair (`REPRESENTATIVE` ≠ `FULL_ACTUAL_EXIT`).
`Φ_eff` is a radii rule, not attainment. UNI is an integral packet, not
realisation. `u_s>1` stays typed `NOT-US1`. The AP kill is a per-member
`j=3` certificate (the seed is the negative control).

---

## Disposition

| item | MEASURED |
|---|---|
| Operative screen | `C_FULL_TREE_POLYNOMIAL_ODE`; n≤100 20/7 (14 excess); D≤200 1420/686/459 |
| K=16 `t=1..8` | **survives** every column; two-point `s_eff=2` |
| `(d,e)`-fixed AP `t=6+9k` | **dies** at POLY `j=3` (`δ₃=0`); seed `t=0` lives |
| Rigid 19 | **0/19 POLY**; 3 ODE leftovers die at POLY `j=3` |
| D=108 | 20 ODE → 9 POLY (6 groups, 5 UNI); 1 `u_s=2` |
| Empty vs ODE | `{72, 80, 100, 176}` |
| Compiler targets | **17** two-point `s_eff=2` `u_s=1` groups, all UNI |
| `n≤100` excess `Φ_eff` | all `u_s=1`; `s_eff∈{3,4}`; 0 two-point `s_eff=2` |
| Moh's six | 6/6 every column |

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15913`.
- Body SHA-256:
  `e68e2b4c06a2ed4f1c43c947c4415b1fc80218688238ce27a07ebbc04601971f`.
- Frozen basis: `058a7195e04df428158ea9e70eee086bf6bb4ac9`.
