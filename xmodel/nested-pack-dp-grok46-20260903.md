# NESTED-PACK — exact parent-indexed orbit-packing DP for `s>3`, replacing the flat UNB relaxation; knapsack.py repairs R1/R2

Lane NESTED-PACK (Grok 4.6), 2026-09-03. Charged inputs verified 5/5 SHA-256 against `/tmp/jc2-lane.HtQdiv/inputs` (mismatch would have stopped the lane):

```text
55db4a9ef9021ef28d3a86dbd3e44d5e3a5aa1b72d61ba23043497f78ba94411  branch-orbits-v2-grok46-20260903.md
c61bb15528b25587578ac10101cb18267e83150fa6ea541e250f606e648d5418  branch-orbits-v2-review-gpt55-20260903.md
aaea3c345b1d53f561798f6a3e4352722f56c50a762f141dfe5e59cf35b1f276  knapsack.py
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  census-rebase-opus5-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full.py
```

No `jc2-lean`, no ideation-20260903T* file, no ledger edit. Desk-scale, one core, Fractions, cap never hit. No exit-price assertion, so no `charge_basis` line.

## 0. Headline

1. **OPEN[NESTED-PACK] is filled as a numerical filter on `48≤D≤120`.** For each (1)–(13) group the unique major `D_{s−1}` is packed level by level: at `j=s−1,…,2` children of a parent fill `p(π)` of degree `Q_j=V_{j+1}d_j/d_{j+1}`, with at most one zero-centred child per parent and free nonzero orbits of size `A_j`. Bottom discs contribute `V_2 q` with the path multiplicity. Exact DP over Fractions, `Q≤38`, cap 60 000 never hit (max 802 states).
2. **Fail-closed against the charged Z01 numbers.** Nested at `s=3` equals Z01 on all 274 groups: **173** alive at `N≥6`, **138** in `[6,16]`. Moh six rows `{9},{},{10},{9},{8},{16}`. `D=105` trio each `N={9}`. `D=88→{18}`. `D=117` 4→3. Flat UNB survivors are a superset of nested (681/575 ⊇ 587/470); 0 reverse hits.
3. **All-`s` nested: 587 at `N≥6`, 470 in `[6,16]`, of 1 189 groups.** UNB killed 614 in `[6,16]`; nested kills **105 more** (10 at `s=3`, 80 at `s=4`, 15 at `s=5`). Empty degrees unchanged: `{48}` at `N≥6`, `{48,88}` in `[6,16]`. No `D>100` empties. Split: `s=3` 173/138 of 274 (exact); `s>3` 414/332 of 915 (exact nested packing, not geometric realisation).
4. **Global Z01 is not a lower bound of nested.** Review typed all-`s` Z01 (611/493) as a lower bound at `s>3` (one `π` globally over-kills). Measured: Z01 and nested are incomparable. In `[6,16]`: 469 both, **24 Z01-only** (`s=4`: 16, `s=5`: 8 — flat budget under-kills nested `Q_j` even on NZ-only packets), **1 nested-only** (`s=5`, several parents each with their own `π`). Promote nested 470, not Z01 493.
5. **R1/R2 applied beside the charged artifact.** `knapsack.py` hash `aaea3c34…` untouched. `knapsack_v2.py` imports via `--inputs` / `$JC2_INPUTS` / repo-relative `box/` (no `/tmp/jc2-lane.GqI4QH`). Printed STRICT totals now split GLOBAL-Z01 611/493 from **s=3 subtotal 173/138 of 274**. Rerun: **336/0**.

---

## 1. The nested constraint (from the charged review)

One bottom-major disc in one tower has `|O|=∏_{j=2}^{s−1} ω_j` with `ω_j=A_j` on a nonzero (10) factor and `ω_j=1` on the zero (11) factor. Each orbit type satisfies (8)–(13) on its own. The shared constraint is packing in the parent polynomial.

At `s=3` the unique parent is `D_2` and `Q_2=V_3 d_2/d_3=u`. NZ unbounded, Z 0–1: exact, already computed. At `s>3` the flat budget `Σ |O_k| V_2^{(k)} ≤ u` is implied by nested packing (product of the inequalities `A_j V_j ≤ Q_j` along a chain) and does **not** imply it. The real constraint, one parent at a time:

- Parent `D_j` has `deg p = Q_j = V_{j+1} d_j/d_{j+1}` (Def 5.1(4)). `A_j` and (10)/(11) depend only on `V_j` and `V_{j+1},…,V_s`.
- A zero-centred child consumes `V_j`; at most one per parent.
- A nonzero orbit consumes `A_j V_j`; several residue-orbits of the same or different lower `V` may coexist. Galois conjugates of one orbit share lower data; distinct orbits pack independently.
- A child that is itself a parent at `j−1` carries `Q_{j−1}` determined by its `V_j`. Bottom discs contribute `V_2 q` each.

Bounded quantity as charged: an integer tuple of length `s−2≤3` on `D≤120`, each part in `{0,…,Q_j}`. The DP enumerates those tuples.

---

## 2. The DP

Driver `box/branch-orbits-v2-20260903/nested_pack.py` (`36b374b21b3768e841ad2cc2168d7e669d9b0d6e6b6c8d1737d203acbd079067`). Enumerator the frozen `moh_skeleton_full.py` via `knapsack_v2`'s R1 loader (`--inputs /tmp/jc2-lane.HtQdiv/inputs`). Charged `knapsack.py` is not imported and not overwritten.

For each group `(m,M,V_s)`: types are the (1)–(13) V-assignments. Recurse from `j=2` up to the unique `D_{s−1}`. At level `j`, group types by `V_j`; each kind is an NZ item of weight `A_j V_j` (unbounded; value `A_j` times a child N) and/or a Z item of weight `V_j` (0–1 across kinds). Child N at `j=2` is `{V_2 q}`; at `j>2` it is the reachable set of the child parent. Mix by Fraction-set DP on `0..Q_j`, prune above `Umax=u·max q ≤ 224/5`. Integer N in `[6,16]` and `N≥6` are read off the top parent. Capped cell ⇒ alive; **cap 0**.

Controls, all pass (NCHECK=40), abort-on-fail: Moh six rows; `Q_2=u` on 305 `s=3` assignments and `Q_{s−1}=V_s d_{s−1}/d_s` on 1 387 `s>3`; `A_j`+(10)/(11) constant on `(V_j..V_s)` at `D≤100` (1 096 rows, 0 mismatches); groups 1 189 / `s=3` 274; UNB 681/575; `s=3` nested = Z01 173/138 with 0 per-group mismatches; nested ⊆ UNB; `D=105` trio keys and `N={9}`; `D=88` nested `[6,16]` empty, `N≥6={18}`; `D=117` 4→3 on the (11)-only `m=78 M=[13,115] V_s=8` row.

Wall 0.8 s nested census, 3.4 s `knapsack_v2` full rerun.

---

## 3. Per degree, `48≤D≤120`

Columns `unb*` are the charged flat relaxation (reproduced). `nest*` are this lane. `kill` = UNB-alive / nested-dead in `[6,16]`. Degrees with no (1)–(13) skeleton (`66,78` and every unlisted `D`) omitted.

```text
    D   grp   s3  s>3  unb>=6  unb616  nest>=6  nest616  kill
   48     2    1    1       0       0        0        0     0  emptied
   54     2    2    0       2       2        2        2     0
   60    15    7    8      13      13       12       12     1
   63     2    2    0       1       1        1        1     0
   64     9    3    6       7       7        5        5     2
   72    46   11   35      26      26       19       19     7
   75     5    5    0       3       3        3        3     0
   80    40   12   28      17      17       14       14     3
   81     2    2    0       1       1        1        1     0
   84    38   20   18      21      21       20       20     1
   88     1    1    0       1       0        1        0     0  EMPTY[6,16]
   90    62   18   44      36      35       31       30     5
   96   157   19  138      92      83       72       61    22
   99     7    7    0       6       4        6        4     0
  100    57   20   37      31      31       29       28     3
  102     3    3    0       3       3        3        3     0
  104     3    3    0       3       3        3        3     0
  105    14   14    0       7       3        7        3     0
  108   125   28   97      90      70       81       61     9
  110     3    3    0       1       1        1        1     0
  112    71   21   50      29      22       28       19     3
  114     3    3    0       3       3        3        3     0
  117     7    7    0       4       4        3        3     1
  120   515   62  453     284     222      242      174    48
  TOTAL 1189  274  915     681     575      587      470   105
```

`s=3` nested = Z01: N≥6 **173**, `[6,16]` **138** (UNB `[6,16]` 148; the 10 are multi-`π` at the unique `D_2`). `s>3` nested: N≥6 **414**, `[6,16]` **332** of 915. Empty nested N≥6: `{48}`. Empty nested `[6,16]`: `{48,88}`. Cap 0.

---

## 4. Special degrees `{105,108,112,117,120}` and `D=88`

| `D` | grp | s3/s>3 | UNB[6,16] | nested[6,16] (s3+s>3) | emptied? |
|---|---|---|---|---|---|
| 88 | 1 | 1/0 | 0 | **0** | `[6,16]` only |
| 105 | 14 | 14/0 | 3 | **3** (3+0) | no |
| 108 | 125 | 28/97 | 70 | **61** (10+51) | no |
| 112 | 71 | 21/50 | 22 | **19** (9+10) | no |
| 117 | 7 | 7/0 | 4 | **3** (3+0) | no |
| 120 | 515 | 62/453 | 222 | **174** (31+143) | no |

`s=3` nested counts on `{105,108,112,117,120}` match the review's exact Z01 subtotals 3/10/9/3/31.

**`D=88` (s=3 exact).** `m=66 M=[-33,86] V_s=9 u=18`, (10)-only `A_2=14`, `|O|=14`, `q=9/7`, one NZ packet `w=14 c=18`. Nested N=`{18}`. Empty in `[6,16]`; lives at the campaign frontier.

**`D=105` trio, all `s=3`, one NZ packet, `N={9}`:**

```text
m=70 M=[28,103] Vs=5 u=25 V2=1 q=1/2  A2=18 (10) |O|=18  N={9}
m=70 M=[28,103] Vs=6 u=30 V2=1 q=9/13 A2=13 (10) |O|=13  N={9}  (and 18 at N>=6)
m=70 M=[40,103] Vs=4 u=28 V2=1 q=9/17 A2=17 (10) |O|=17  N={9}
```

The other 11 groups: 4 live only at `N≥6` (`{24},{18},{24},{20}`), 7 hit nothing ≥6. UNI interval `[6..12]` on the first row remains refuted.

**`D=117` (s=3 exact), 4→3.** Killed: `m=78 M=[13,115] V_s=8 u=24 V2=3 q=3/7` (11)-only, one Z packet value `9/7` not integral. Survivors, all (10)-only NZ:

```text
m=78 M=[52,115] Vs=10 u=30 |O|=7  N={6,9,12}
m=78 M=[52,115] Vs=11 u=33 |O|=6  N={6,9,12,15}
m=78 M=[91,115] Vs=11 u=33 |O|=7  N={8}
```

**`D=108` s=3 nested `[6,16]` (10, exact):** `m=72` rows `M=[-24,106] Vs=11 N={12}`; `[40,106] Vs=3 {12}`; `[42,106] Vs=5 {15}`; `[48,106] Vs=9 {9}` and `Vs=11 {15}`; `[54,106] Vs=13 {6}`, `Vs=15 {16}`, `Vs=17 {12}`; `[56,106] Vs=3 {6}`; plus `m=90 M=[78,106] Vs=5 N={6,12}`. Nine UNB-alive nested-dead, all `s=4`.

**`D=112` s=3 nested `[6,16]` (9, exact):**

```text
m=48 M=[84,110] Vs=3 N={7};  m=48 M=[88,110] Vs=7 N={7}
m=64 M=[56,110] Vs=7 N={14}; m=80 M=[100,110] Vs=3 N={15}
m=84 M=[42,110] Vs=9 N={6};  m=84 M=[60,110] Vs=3 N={12}
m=84 M=[68,110] Vs=3 N={8};  m=84 M=[70,110] Vs=12 N={8,12}, Vs=13 N={12}
```

Three nested kills of UNB: one `s=3` (`m=80 M=[88,110] Vs=5`, Z01 already dead) and two `s=4` (`m=96 M=[8,36,110]` and `[8,92,110] Vs=3`). The last two are the typical UNB false Z-copies: `j=3` is (11)-only so one `D_2`; `j=2` admits both centres; UNB treats `ω_2=1` as unbounded, hitting every even N; nested allows one Z disc (`N=2`) plus one NZ orbit (`N=22`), so `{2,22,24}` — empty in `[6,16]`, alive at `N≥6`.

**`D=120` s=3 nested `[6,16]` (31, exact):** listed in `nested_pack.log`. Compact keys: `m=48` four rows `N∈{15,15,10,10}`; `m=72` one `{12,14}`; `m=80` nine rows including `{6,9,11,12,14,15}` on `M=[64,118] Vs=7`; `m=90` nine rows; `m=96` four; `m=100` four `{15,12,12,6}`. 143 `s>3` nested survivors and 48 UNB-alive nested-dead: log.

---

## 5. Why nested is strictly tighter than UNB, and Z01 is not a bound

UNB = both packet types unbounded, budget `Σ |O| V_2 ≤ u`. Nested ⇒ UNB (product of `A_j V_j ≤ Q_j`). The 105 reverse-empty groups are valid kills of nested packing. Split: 10 at `s=3` (several copies of the unique `π`; already in the charged Z01 delta), 80 at `s=4`, 15 at `s=5`.

Two mechanisms at `s>3`.

**(a) Unbounded Z in UNB.** Several copies of a size-1 packet repeat the unique `π` of one parent. Nested forbids it per parent. The `D=112` pair above is the type.

**(b) Flat budget vs nested `Q_j`, even NZ-only.** Witness, Z01-alive and nested-dead: `D=72 m=48 M=[32,68,70] V_s=3`, `s=4`, `u=18`, one type, `j=2` (10)-only `A_2=8 V_2=1 Q_2=15`, `j=3` both with `A_3=1 V_3=5 Q_3=6`, `q=3/8`. UNB/Z01: one NZ packet `w=8 c=3`; two copies weight 16≤18 give `N=6`. Nested: one `D_2` of `V_3=5` holds one NZ orbit (`w=8≤15`, `N=3`); two such `D_2` would consume `5+5=10>Q_3=6`. Nested N=`{3}` only. Flat `|O| V_2 ≤ u` does not reconstruct the parent-by-parent split. 24 such Z01-only groups (`s=4`: 16, `s=5`: 8).

**(c) Global one-Z over-kills nested.** One nested-only group: `D=120 m=80 M=[-60,-10,25,118] V_s=3`, `s=5`, `u=24`. Top `j=4` is (11)-only (`V_4=6=Q_4`), one `D_3`; lower levels admit both centres. Nested N=`{9}`. Global Z01 misses it (several parents, each allowed one `π`). So all-`s` Z01 493 is **neither** a subset nor a superset of nested 470.

---

## 6. Repairs R1 and R2

Charged `box/branch-orbits-v2-20260903/knapsack.py` left at `aaea3c345b1d53f561798f6a3e4352722f56c50a762f141dfe5e59cf35b1f276`. Repaired copy `knapsack_v2.py` (`856d0c5cda9919357ad6eecac7f37bada59a9810319ba262ebca73e85ac2e09c`):

- **R1.** No `sys.path` entry `/tmp/jc2-lane.GqI4QH/inputs`. Loader: `--inputs DIR`, `$JC2_INPUTS`, then `HERE/..` (repo `box/`). This rerun used the frozen inputs dir; enumerator SHA matches `d20bf084…`.
- **R2.** Prints `GLOBAL-Z01 (all s, NOT exact at s>3): z01_16 493 z01_>=6 611` and separately `STRICT s=3 subtotal: 274 groups, Z01 N>=6 = 173, Z01 [6,16] = 138` (also UNI 187/165, mix 166, UNB[6,16] 148).

Rerun of `knapsack_v2.py --inputs /tmp/jc2-lane.HtQdiv/inputs`: **ALL CONTROLS PASSED. NCHECK=336.**

---

## 7. Hostile checks; FALLACY-v2

- **Could nested equal UNB at `s>3`?** No. 95 groups at `s>3` are UNB-alive nested-dead in `[6,16]`; witness (b) is NZ-only.
- **Could Z01 still be used as a lower bound?** No. 24 Z01-alive nested-dead, 1 nested-alive Z01-dead.
- **Could the DP mix types across different parents' upper `V`?** No. Types are grouped by `V_j` given the parent signature `V_{j+1}..V_s`; CONTROL A.
- **Could `|O|` at the bottom be multiplied twice?** No. Local `ω_j` is applied when the child is placed at level `j`; the product is the path.
- **FALLACY-v2.** Flag/place/series: Moh `n=D` is never mixed with campaign `n=deg Ā_F`. Per-ray: bottom-major discs remain disjoint in `D_{s−1}`; each `g`-root is charged once at D1-PIN. Floor/attainment: the DP asserts existence of an integral nested packet, not geometric realisation (OPEN[STAR-REALISABILITY] untouched). Carrier: Lemma 6.1 is only the coordinate change on major roots. No `sat()`, no Groebner, no cap-fill, no exit claim.

---

## 8. Opens

```text
OPEN[NESTED-PACK]  FILLED as exact numerical packing on 48<=D<=120
   (tuple of length s-2<=3; DP enumerates it).  Residue: geometric
   realisability of a surviving packet, already OPEN[STAR-REALISABILITY]
   / OPEN[BRANCH-ORBITS].  Cheapest remaining test is not another knapsack.

OPEN[BRANCH-ORBITS]  geometric existence, quantity in {1..u}.  Numerical
   orbit-size and nested packing are now exact; still no pair (f,g)
   realising several orbits, nor a theorem that a degree-minimal
   counterexample has one.  Cheapest test: local Prop 4.6 construction
   at a surviving nested packet.

OPEN[PROP-5.6-SHADOW]  census-rebase; 220 groups at D<=120.  Do not
   proxy by "all (11)".  Track whether sigma_1 has all previous
   coefficients zero; controls against Moh's six rows.

OPEN[MOH-PROGRAM]  652 excess rows at n<=100.  Reimplement the missing
   restrictions of Moh's program; require exact p.202 before using above 100.

OPEN[V-FLOOR]  integer V_j windows / pinned q.  Search surviving nested
   packets for a measured floor on V_2 or q; equality needs a theorem.

OPEN[STAR-REALISABILITY]  multiplicity partition of p(pi) of degree e V_2
   at each surviving skeleton.  Cheapest test: Prop 4.6 at level 1;
   kill repeated roots where D1-STAR predicts simple roots.
```

---

## 9. Typed block

```text
LANE          NESTED-PACK (Grok 4.6), 2026-09-03
SOURCE        Moh 1983 JRAM 340 Def 5.1 / (8)-(13); charged BRANCH-ORBITS v2
              report+review; enumerator d20bf0841a1ba2b2.
PROVED-HERE   nested packing DP exact on 48<=D<=120: at each parent D_j,
              NZ unbounded of weight A_j V_j, at most one Z of weight V_j,
              child Q_{j-1} from V_j; s=3 recovers Z01 173/138 of 274;
              nested => UNB (105 extra [6,16] kills, 0 reverse);
              D=88 nested N={18}; D=105 trio N={9}; D=117 4->3;
              Moh six-row N-sets; Q_2=u (305) and Qtop formula (1387);
              global Z01 is not a nested lower bound (24 Z01-only, 1 nested-only).
CONFIRMED     unique D_{s-1}; |O|=prod omega_j; (8)-(13) per orbit;
              A_1 not a disc-orbit multiplier; census 1189/274 s=3;
              UNB 681/575; empty {48} at N>=6 and {48,88} in [6,16];
              no D>100 empty; knapsack_v2 controls 336/0 after R1/R2.
REFUTED       reading UNB 575 as exact nested packing (now 470);
              reading all-s Z01 493 as a lower bound of nested;
              UNI across orbits (unchanged); D=105 UNI [6..12].
NOT CLAIMED   geometric realisation of any packet; emptiness of any D>100
              as a Keller pair; a D-ceiling; PLACE-LEDGER identification;
              Prop 5.6 as a numerical kill; filling BRANCH-ORBITS.
MEASURED      nested N>=6 587 / [6,16] 470 of 1189 (s=3: 173/138 of 274;
              s>3: 414/332 of 915).  UNB-alive/nested-dead [6,16]: 105
              (s=3:10, s=4:80, s=5:15).  Z01 vs nested [6,16]: 469 both,
              24 Z01-only, 1 nested-only.  cap 0.  wall 0.8 s nested,
              3.4 s knapsack_v2.  max Q=38, max Umax=224/5, max states 802.
              D=108: 70->61; D=112: 22->19; D=120: 222->174.
OPEN          NESTED-PACK filled numerically on D<=120; residue is
              STAR-REALISABILITY / BRANCH-ORBITS.  PROP-5.6-SHADOW;
              MOH-PROGRAM; V-FLOOR.
ARTIFACTS     box/branch-orbits-v2-20260903/nested_pack.py     36b374b21b3768e8
              box/branch-orbits-v2-20260903/nested_pack.log    74908c3af46fe761
              box/branch-orbits-v2-20260903/knapsack_v2.py     856d0c5cda991935
              box/branch-orbits-v2-20260903/knapsack_v2.log    55bf8fb7d0de93bc
              charged knapsack.py UNTOUCHED                    aaea3c345b1d53f5
              Enumerator box/moh_skeleton_full.py not modified.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17546`.
- Body SHA-256:
  `999f42474b6b210394d6d49de94f617a91339044e25ec9ca34e143863b878b6e`.
- Frozen basis: `4b3496561332da883e39ce4602bde9dba791032e`.
