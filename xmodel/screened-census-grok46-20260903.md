# Screened census: C_FULL_TREE_ODE composed with nested-pack, to D ≤ 400

Lane SCREENED-CENSUS (Grok 4.6), 2026-09-03. Operative filter after AUDIT
delta 17(r): the whole-major-tree DP `C_FULL_TREE` plus the ODE
sharpening (3.7), composed with the exact parent-indexed nested-pack
orbit knapsack. Passport (3.8) and edgewise recentring are **side
columns only** — never folded into operative numbers.

Frozen inputs in `/tmp/jc2-lane.LGjDKK/inputs` matched 9/9 SHA-256
(mismatch would have stopped the lane):

```text
e4bbb5f8e431baed488a2a3dfd856a3f7c4ea7ea006690bcc116f0db9ee60c45  moh-program-review-sol56-20260903.md
9497e23140ca2c92f99f706e23affbaaaf4dfdab63ce7b93b5dea76933aabf6d  whole-tree-review-grok46-20260903.md
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  full_tree_partition.py
5d1b21222eecc448975c83d3628c22ada5cd26737155ecf2a7a27304ec40e553  candidate_eval.py
c2a27632d54576abbca54b9f268a7fa5d2b144497a1e364c93102450a066baf9  tree-independent.py
36b374b21b3768e841ad2cc2168d7e669d9b0d6e6b6c8d1737d203acbd079067  nested_pack.py
53d3464817f5c777d0cb106806d590f62556eb8a8dc18c12fc810eb2476cf065  nested-pack-dp-grok46-20260903.md
982c75da179e263e109d0bf6ba0e8b13e591225c80d0111d24ba32b61be67896  n6-family-review-grok46-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full.py
```

Workspace copies of `full_tree_partition.py`, `nested_pack.py`, and
`box/moh_skeleton_full.py` match those hashes. No `jc2-lean`, no
`ideation-20260903T1015Z-*` file, no other running-lane report, no
ledger edit. Desk-scale, one core, `fractions.Fraction`. No exit-price
assertion, so no `charge_basis` line.

Driver: `box/screened-census/screened_census.py`. It imports the frozen
tree DP and the frozen nested-pack DP; it does not reimplement either.
The tree cache key is `(j, path[j+1:], danger, …)` — the higher
V-tuple is in the state (CONTROL V-TUPLE, s=4 witness
`(100,40,M=(70,95,98),V=(8,4,4))`).

PATH-ARITH(1–13) means the finite space of the frozen enumerator, not
existence of a Jacobian pair. Nested N is existence of an integral
packet, not geometric realisation (`OPEN[STAR-REALISABILITY]`).

---

## 0. Headline

1. **Fail-closed composition.** Unscreened columns reproduce the charged
   nested-pack numbers: **1,189 / 587 / 470** at `D≤120`, **14,016
   groups** at `D≤200`. `n≤100`: **658 → 60 → 58** (TREE, ODE); Moh's
   six survive every screen. FT = `tree-independent.py` row-for-row on
   TREE/PASSPORT/POLY (0 disagreements). Frozen `D≤200`: TREE 3,090 V /
   1,516 groups, ODE 2,824 / 1,384, PASSPORT (side) 2,581 / 1,261.
2. **Operative nested after the screen, `48≤D≤120`.** TREE groups 113,
   nested N≥6 **57**, [6,16] **43**. ODE groups 103, nested N≥6 **51**,
   [6,16] **43**. At `D≤200`: ODE nested N≥6 **727**, [6,16] **523** of
   1,384 ODE groups (UNI 865 is a different column; not mixed).
3. **`D=105` and `D=117` empty** under TREE (and so under ODE), matching
   delta 17(r). Both named rays stay dead for every constructed member
   (Sol `L=8a+5`, `a=0..` ; `A₂=6` geometric `n=9(7t+6)`). The kill is
   still `b_min = P mod A₂ > h` at `j=2` with top-chart danger set
   (`s=3`).
4. **New first realisation target.** Smallest `D>100` with a
   `C_FULL_TREE_ODE` + nested-N≥6 survivor is **`D=108`**: 12 ODE
   groups, 8 nested N≥6, **5 in [6,16]**, all five `s=4`, all
   `(d,e)=(2,3)`, all `u_s=1` (Prop 6.3/6.4 automatic). Named target:
   `m=72`, `M=(12,102,106)`, `V_s=5`, nested `N={15}`. First `s=3`
   campaign-window survivor above 100 is **`D=112`**, and it is a member
   of the cofinal family of §6.
5. **Cofinality: a closed-form family survives the operative screen for
   every `t≥1`.** Not Sol's ray and not the `A₂=6` ray. It is the
   `K=16` ray through Moh `(64,48)` and the `D=112` `s=3` survivor:

```text
t ≥ 1 integer
e = 3t+1,  d = 2t+1,  gcd(d,e) = 1 identically
n = 16e = 48t+16,  m = 16d = 32t+16
M = (−m, n−12, n−2),  s = 3,  V₂ = 3,  V₃ = 3
d₂ = 16, d₃ = 4, d₄ = 2
A₂ = 4,  P = 12,  P ≡ 0 (mod A₂)     # no forced zero
u_s = 1,  q = (2t+1)/4,  u = 12
|O| = 4  ((10)-only),  N = 6t+3 ≥ 9
```

   Algebra in `t` is in §6 (sympy-exact, then `Skel` + TREE + ODE +
   nested + census emission at `t=1,2,3,8,20,50`). **Q3(f) after the
   screen: the screened census cannot be a proof program by emptiness.**
   The space is cofinally nonempty.

---

## 1. Composition

Per PATH-ARITH V-assignment, in this order:

- `C_FULL_TREE` (`FT.full_tree_ok`): every major sibling extends; selected
  path embeds; Lemma 5.3 top-chart danger; Prop 5.6 kills a still-centred
  zero leaf. DERIVED. State carries the higher V-tuple (Def 5.1(3)).
- `C_FULL_TREE_ODE` (`FT.full_tree_ode_ok`): additionally `P−Qu ≠ 0` at
  every p-root (Prop A.3, RHS `cp`). Operative sharpening.
- Nested-pack (`nested_pack.nested_values`) on the surviving V-assignments
  of each group `(m,M,V_s)`, windows `N≥6` and `[6,16]`. Exact at every
  `s`; at `s=3` equals Z01.

Side columns, typed, not operative: `C_FULL_TREE_PASSPORT` (EXTERNAL,
(3.8)); `C_FULL_TREE_POLY` / `POLY+ODE` (`OPEN[FULL-TREE-RECENTER]`).
Computed through `D≤200`.

Unscreened nested is run only through `D≤120` (the charged 587/470);
unscreened **group** count is run through `D≤200` (the charged 14,016).

---

## 2. Controls (all abort-on-fail)

- Hash gate 9/9 plus three workspace copies.
- Moh six: TREE, ODE, PASSPORT, POLY, POLY+ODE, and TI `--zero-only` all
  keep every row. Nested `[6,16]` N-sets `{9}, {}, {10}, {9}, {8}, {16}`
  match the charged nested-pack control (the empty cell is
  `(84,56) M₂=64, V₂=2`, already charged).
- `n≤100`, `K_min=2`: 658 rows, 63 `(n,m)` classes; TREE 60 / ODE 58 /
  PASSPORT 55 / POLY 23 / POLY+ODE 20; `(75,50)` ODE residue
  `{(M₂,V₂)=(55,2),(55,3)}`; printed keys ⊆ every screen; FT vs TI
  row-for-row 0 disagreements on TREE, PASSPORT, POLY.
- Checkpoint `D≤120`: unscreened 1,189 / 587 / 470; TREE V/groups
  183/113; ODE V/groups 168/103 (match frozen `candidate-results.json`).
- Checkpoint `D≤200`: unscreened groups 14,016; TREE groups 1,516; ODE
  groups 1,384; PASSPORT groups 1,261.

---

## 3. Per degree, `48≤D≤200`

Columns: PATH-ARITH groups and V-assignments; TREE / ODE groups; nested
N≥6 and `[6,16]` after TREE (`tN6`) and after ODE (`oN6`,`oN16`);
PASSPORT groups (side). Unscreened nested (`unN*`) only through 120.
`EMPTY` marks ODE nested N≥6 empty among baseline-active degrees.

```text
    D   grp     V  treeG  odeG   tN6   oN6  oN16  passG  unN6 unN16
   48     2     2      0     0     0     0     0      0     0     0  EMPTY
   54     2     2      0     0     0     0     0      0     2     2  EMPTY
   60    15    18      0     0     0     0     0      0    12    12  EMPTY
   63     2     2      0     0     0     0     0      0     1     1  EMPTY
   64     9    10      1     1     1     1     1      1     5     5
   72    46    55      2     2     0     0     0      2    19    19  EMPTY (TREE alive, nested dead)
   75     5     9      1     1     1     1     1      1     3     3
   80    40    45      1     1     0     0     0      1    14    14  EMPTY (TREE alive, nested dead)
   81     2     2      0     0     0     0     0      0     1     1  EMPTY
   84    38    51      5     4     3     2     2      4    20    20
   88     1     1      0     0     0     0     0      0     1     0  EMPTY
   90    62    91      6     6     2     2     2      6    31    30
   96   157   229     21    20    10    10    10     20    72    61
   99     7     8      1     1     1     1     1      1     6     4
  100    57    67      2     2     1     1     1      1    29    28
  102     3     3      0     0     0     0     0      0     3     3  EMPTY
  104     3     4      0     0     0     0     0      0     3     3  EMPTY
  105    14    15      0     0     0     0     0      0     7     3  EMPTY
  108   125   206     13    12     8     8     5     11    81    61
  110     3     3      0     0     0     0     0      0     1     1  EMPTY
  112    71    76      7     7     2     2     2      7    28    19
  114     3     4      0     0     0     0     0      0     3     3  EMPTY
  117     7     7      0     0     0     0     0      0     3     3  EMPTY
  120   515   782     53    46    28    23    18     41   242   174
  ---- 1189  1692    113   103    57    51    43     96   587   470
```

`121–200` (side passport still on): TREE 1,403 groups / ODE 1,281 /
ODE nested N≥6 676 / [6,16] 480 / PASSPORT 1,165. Combined `48–200`:

| slice | PATH-ARITH g / V | TREE g | ODE g | ODE nest N≥6 | ODE nest [6,16] | PASSPORT g (side) |
|---|---:|---:|---:|---:|---:|---:|
| 48–120 | 1,189 / 1,692 | 113 | 103 | **51** | **43** | 96 |
| 121–200 | 12,827 / 22,028 | 1,403 | 1,281 | 676 | 480 | 1,165 |
| 48–200 | **14,016** / 23,720 | **1,516** | **1,384** | **727** | **523** | **1,261** |

Highly composite degrees dominate the raw count (`D=144`: 1,216 groups;
`D=180`: 2,559; `D=192`: 3,589; `D=200`: 1,591) and the screened count
(`D=180` ODE nested N≥6 = 150; `D=192` = 246).

**Degrees EMPTIED by TREE** among baseline-active `D≤200` (no TREE
group): `48, 54, 60, 63, 81, 88, 102, 104, 105, 110, 114, 117, 130, 152,
153, 154, 170, 182, 186, 190, 195`. Matches charged `C_FULL_TREE`
`candidate_zero_degrees`.

**Additionally emptied by ODE** (TREE alive, ODE dead): `174, 184`.

**Additionally emptied by nested N≥6 after ODE** (ODE groups exist, no
integral nested packet ≥6): `72, 80`. These two have TREE/ODE
V-assignments (the `n≤100` excess at those degrees) whose orbit packets
miss every integer `N≥6`.

Operative empty set at `D≤200` (ODE + nested N≥6): the TREE-empty list
plus `{174, 184, 72, 80}`.

`D=105` and `D=117` are in the TREE-empty list (0/0/0), as charged.
Unscreened nested still sees the trio at `D=105` (`unN16=3`) and three
groups at `D=117` — those are baseline-only.

---

## 4. Survivor lists at `D=108, 112, 120`

Under **`C_FULL_TREE_ODE` + nested `[6,16]`**. Packets are
`(tag, w, c, |O|)` of the surviving V-assignments; `N` is the group's
nested integer set.

### `D=108` — 5 groups in `[6,16]` (plus 3 N≥6-only)

All five campaign-window groups are `s=4`, `m=72`, `(d,e)=(2,3)`,
`K=36`, `u_s=1`.

```text
m=72 M=[12,102,106] Vs=5 u=30 q=5/7  |O|={1,21} N={15}
  V=(1,8,5) NZ w=21 c=15 |O|=21  (10) at j=2, both at j=3; (13)
  V=(3,8,5) Z  w=3  c=18/7 |O|=1  (11) at j=2
m=72 M=[24,78,106]  Vs=5 u=30 q=1/2  |O|={3,6,12} N={6..15} (and 17)
  V=(1,1,5), (1,4,5)
m=72 M=[48,90,106]  Vs=5 u=30 q=3/14 |O|={1,7,14} N={6}
  V=(1,1,5), (1,3,5)
m=72 M=[54,99,106]  Vs=8 u=32 q=3/7  |O|={1,7}    N={6,9} (and 18)
  V=(1,12,8), (3,12,8)
m=72 M=[84,104,106] Vs=3 u=27 q=8/13 |O|={1,3}    N={16}
  V=(8,7,3), (21,7,3), (8,8,3)
```

N≥6 only (not in `[6,16]`): `m=72 M=[-18,60,106] Vs=5 N={23,24}` (`s=4`);
`m=72 M=[81,106] Vs=7 N={21}` (**`s=3`**, `u_s=2`); `m=72 M=[90,99,106]
Vs=8 N={17}` (`s=4`). The `s=3` row is the first `s=3` ODE+N≥6 survivor
above 100, but it lives at `N=21`, outside the campaign window.

At `j=2` the five `[6,16]` groups have `b_min > h` (a major zero
*would* be forced). They survive because `s=4`: a nonzero label at
`j=3` clears the Lemma 5.3 danger flag before `j=2`, so the forced
zero is not a Prop 5.6 leaf. That is the `s=3`/`s>3` split of the kill
mechanism, not a contradiction.

### `D=112` — 2 groups

```text
s=3 m=80 M=[100,110] Vs=3 u=12 q=5/4 |O|={4} N={15}
  V=(3,3)  NZ w=12 c=15 |O|=4  (10)-only  P=12 A₂=4 P≡0  u_s=1
  K=16 e=7 d=5   ← member t=2 of the §6 family
s=4 m=84 M=[42,105,110] Vs=6 u=24 q=1 |O|={1,6} N={6,12} (and 18)
  V=(1,11,6), (4,11,6)
```

### `D=120` — 18 groups (6 `s=4` + 12 `s=5`)

```text
s=4 m=48 M=[60,104,118]   Vs=3 u=18 q=15/22 N={10,15}
s=4 m=80 M=[-8,68,118]    Vs=3 u=30 q=66/95 N={15}
s=4 m=80 M=[60,108,118]   Vs=3 u=30 q=3/8   N={9}
s=4 m=80 M=[60,110,118]   Vs=9 u=36 q=3/7   N={6,9}
s=4 m=90 M=[70,115,118]   Vs=4 u=24 q=1/2   N={7,11}
s=4 m=96 M=[60,114,118]   Vs=5 u=20 q=15/13 N={15}
s=5 m=80 M=[-60,-10,25,118] Vs=3 u=24 q=3/8 |O|={1,11} N={9}  u_s=2
    (Prop 6.3 hyp: δ*_{s−1}=56/37 ≥ v_s/u_s=3/2)
s=5 m=80 M=[-60,50,75,118]  Vs=4 N={16}
s=5 m=80 M=[-60,70,75,118]  Vs=4 N={16}
s=5 m=80 M=[-60,70,85,118]  Vs=4 N={16}
s=5 m=80 M=[-60,70,105,118] Vs=4 N={16}
s=5 m=80 M=[-20,30,115,118] Vs=4 N={6,9,12,15}
s=5 m=80 M=[-20,50,105,118] Vs=4 N={16}
s=5 m=80 M=[-20,70,75,118]  Vs=4 N={16}
s=5 m=80 M=[-20,90,115,118] Vs=4 N={6,12,14}
s=5 m=80 M=[20,50,115,118]  Vs=4 N={15}
s=5 m=80 M=[60,110,115,118] Vs=4 N={16}
s=5 m=80 M=[100,110,115,118] Vs=4 N={10}
```

The last row is the nested-only `s=5` group of the charged nested-pack
report (global Z01 missed it); it survives ODE. Full V-assignments and
packets: `box/screened-census/listings_108_112_120.json`.

---

## 5. First realisation target (`D=108`)

Smallest `D>100` with an operative survivor: **108**. Named target
(lexicographic first of the five `[6,16]` groups):

```text
n=108, m=72, s=4, M=(12, 102, 106), V_s=5
K=36, e=3, d=2,  d = (108, 36, 12, 6, 2)
u = 30,  u_s = d_s − V_s = 6 − 5 = 1
δ = (δ₁, δ₂, δ₃, δ₄) = (17/42 or 2/7, 5/21, 0, −1)   # δ₁ depends on V₂
```

Two V-assignments in the group:

| V | q | (10)/(11) | (12)/(13) | \|O\| | packet |
|---|---|---|---|---:|---|
| `(1,8,5)` | 5/7 | j=2 (10); j=3 both | (13) | 21 | NZ `w=21, c=15` |
| `(3,8,5)` | 6/7 | j=2 (11); j=3 both | both | 1 | Z `w=3, c=18/7` |

Nested mix: one NZ orbit of the first type hits `N=15` exactly
(`w=21≤u=30`). The Z packet `18/7` is not integral. Group `N={15}`.

**Prop 6.3 descent datum.** `u_s=1`, so Prop 6.4 applies: the minor-disc
radius inequality is automatic and Prop 6.3 produces a monomial-Jacobian
pair of π-degrees `u_s n/d_s = 108/6 = 18` and `u_s m/d_s = 12`, Jacobian
`∼ γ^{v_s−u_s−1} = γ^{3}`. This is a bounded descended problem (unlike
the §6 family, whose descended degrees grow). Cheapest next test on this
row: `OPEN[SIBLING-COEFFICIENTS]` at the `j=3` node (the sibling
`p,q` of degrees `P=10, Q=…` with the A.3 ODE), already launched as a
sibling lane.

---

## 6. Cofinality

### 6.1 The two named rays stay dead

Sol `L=8a+5`: `b_min=10a+7 > h=(8a+5)/(16a+11)` identically; TREE-dead
at every constructed `a` (including far past `D=400`). `A₂=6` geometric
`n=9(7t+6)`: `b_min=3 > h=3/5` identically; TREE-dead at every
constructed `t`. Delta 17(n)'s cofinal-nonemptiness is PATH-ARITH +
integrality, **false** after `C_FULL_TREE` for those two rays.

### 6.2 The `K=16` family (PROVED-HERE, all `t≥1`)

Search: among `s=3` ODE survivors, `P≡0 (mod A₂)` (so `b_min=0`, no
forced zero) with `h` possibly `<1`. Moh `(64,48)` and the `D=112` `s=3`
row share `K=16`, `M₂=n−12`, `V₃=3`, `A₂=4`, `P=12`. That is a ray.

**Closed form.** For integer `t≥1` set `e=3t+1`, `d=2t+1`. Euclid:
`gcd(2t+1, 3t+1)=gcd(2t+1, t)=gcd(1,t)=1`. Then

```text
n = 16e = 48t+16,   m = 16d = 32t+16,   M₂ = n−12 = 48t+4,   M₃ = n−2
V₂ = V₃ = 3
```

**`d_j`.** `d₂=gcd(n,m)=16` because `gcd(e,d)=1`.
`d₃=gcd(16,48t+4)=gcd(16,4)=4` (`12t+1` is odd).
`d₄=gcd(4,48t+14)=gcd(4,2)=2`.

**Windows.** `i=3`: `2 < 3 ≤ 4`. `i=2`: `4/3 < 3 ≤ 12`. Both, all `t`.

**Radii.** `δ₃=−1`. `w=n−M₂=12` is **constant**, so
`δ₂ = 1 − 12(6−4)/(36−4) = 1/4` independently of `t`. `A₂=4`.
`P=V₃ d₂/d₃=12`, `P≡0 (mod 4)`: **no forced zero**. `Q=V₃ w/d₃=9`.
(9): `12=3·4+0`, `△=3`, `□=0`. (10): `V₂=3≤3`. (11): `3≢0 (mod 4)`.
**(10)-only**, `|O|=A₂=4`. `u=12`.

**`δ₁` (sympy).** `δ₁=(7t+2)/(4(3t+1))`. `L₁=4`,
`L₁δ₁=(7t+2)/(3t+1)`. Euclid: `gcd(7t+2,3t+1)=1`, so **`A₁=3t+1=e`**.

**(12).** `A₁ | e·V₂ = 3(3t+1)` and `A₁ | d·V₂−1 = 6t+2=2(3t+1)`: both
hold identically. **(13)** fails (`3t+1` leaves remainder 1 on `6t+3`).
So (12)∨(13) for all `t`. `q=(1−δ₁)de/(d+e)=(2t+1)/4`.
`N=|O|V₂ q=12q=6t+3`.

**TREE / ODE.** At `j=2`: `b=0`, `total=3`, `max_orbits=⌊9/4⌋=2`,
`h=4/3`. Selected `V₂=3` is a major nonzero orbit; complement empty;
ODE `P−Q·3=12−27≠0` (and `12/9` is not an integer, so no minor
`u=P/Q` sibling). Danger clears on the nonzero label. Bottom (12)
holds. The same partition is the generic tree (`b=0`, one major coin 3).

**Nested.** `s=3` exact: one NZ packet `w=12=u`, `c=6t+3`. One copy
fits. `N={6t+3}≥9`. Cap never relevant.

**Census.** `K=16≤n/3` for `t≥1`; divisor chain `[4]` gives `s=3`,
`gcd(16,M₂)=4`. Emitted at `t=1,2,3,8,20,50` (`n` up to 2,416).
TREE+ODE+nested checked at those `t`. Members `t=1..8` with `n≤400`:
`64, 112, 160, 208, 256, 304, 352, 400`. Campaign window `[6,16]` holds
only for `t=1,2` (`N=9,15`); the family is cofinal at **`N≥6`**, not at
pinned `N=6` and not inside `[6,16]`.

`t=1` is Moh `(64,48)`. `u_s=1` for every `t`, so Prop 6.3/6.4
**descends the whole ray** to monomial-Jacobian pairs of degrees
`n/d_s=4e=12t+4` and `m/d_s=4d=8t+4`, unbounded in `t`. Descent does
not kill the family; it converts it into the unbounded-degree `s'=2`
objects of m2-descent theorem (T). That is a different proof program,
not emptiness of the screened census.

### 6.3 Growth, and Q3(f)

Through `D=200` the operative count is 727 groups at N≥6 and growing
(`D=180`: 150; `D=192`: 246). The `D≤400` loop completed every baseline-active degree through
**`D=238`** (73 degrees, 127 s) and stopped: `D=240` TREE+ODE is 26 s
on a prior bench (27,501 V) but nested mix-DP on those TREE groups did
not finish in the remaining desk budget. Snapshot `D≤238`: **1,224**
ODE+nested-N≥6 of 2,262 ODE groups. The §6.2 family independently puts
a survivor at `256, 304, 352, 400`. **The screened space is cofinally
nonempty.** Q3(f) after the screen is **no**. A uniform theorem still
needs a datum outside PATH-ARITH+TREE+ODE+nested — sibling
coefficients, or descended monomial-Jacobian analysis along `u_s=1`.

Naive scalings of `(75,50)` and `(99,66)` fail for `t≥2`. No second
closed form was isolated in the `s=3` `P≡0` slice; the `K=16` ray is
the one proved.

---

## 7. Residue at `n≤100`: 58 − 6 = 52

All 52 excess `C_FULL_TREE_ODE` rows have **`u_s=1`** and therefore
descend by Prop 6.3/6.4. None is `s=3`: the only `s=3` ODE rows at
`n≤100` are Moh's six (five of those also have `u_s=1`; `(99,66)` has
`u_s=3`). Split: 37 at `s=4`, 15 at `s=5`. Classes (row counts):
`(72,48)×2`, `(80,32)×1`, `(84,56)×3`, `(90,60)×9`, `(96,64)×24`,
`(96,72)×9`, `(96,80)×1`, `(100,40)×1`, `(100,80)×2`.

`(10)/(11)` at each printed level (all `u_s=1`, Prop 6.3 automatic).
Full rows: `box/screened-census/residue_n100.json`.

```text
n   m   M                    V                s  (10)/(11)
72  48  [60,66,70]           (11,10,5)        4  11; 10/11
72  48  [60,68,70]           (11,7,3)         4  11; 10/11
80  32  [56,76,78]           (8,4,3)          4  11; 10/11
84  56  [42,77,82]           (1,12,6)/(3,12,6) 4  10; 10/11  and  10/11; 10/11
84  56  [70,77,82]           (11,10,6)        4  11; 10/11
90  60  [10,45,88]           (1,8,4)/(3,8,4)  4  10; 11  and  10/11; 11
90  60  [10,85,88]           (1,8,4)/(3,8,4)  4  10; 10/11  and  11; 10/11
90  60  [45,80,88]           (2,5,4)/(3,5,4)  4  10/11; 11  and  10; 11
90  60  [70,85,88]           (8,7,4)          4  11; 10/11
90  60  [75,85,88]           (11,7,4)         4  11; 10/11
90  60  [80,85,88]           (17,8,4)         4  11; 10/11
96  64  [-48,-8,20,94]       (1,1,6,3)        5  10/11; 10/11; 11
96  64  [-48,24,92,94]       (20,10,5,3)      5  11; 11; 10/11
96  64  [-16,24,92,94]       (1|5|20, 8|10, 4|5, 3)  5  mix 10/11
96  64  [-16,72,92,94]       (1,8,4,3)/(2,8,4,3) 5  10/11;11;10/11  and  10;11;10/11
96  64  [16,24,92,94]        (20,10,5,3)      5  11; 11; 10/11
96  64  [24,92,94]           (20,5,3)         4  11; 10/11
96  64  [48,68,94]           (1,2,3)/(2,1,3)/(3,2,3)  4
96  64  [48,72,92,94]        (24,12,6,3)      5  11; 11; 10/11
96  64  [48,88,92,94]        (1|3|17,12,6,3)  5  mix
96  64  [48,88,94]           (1,12,7)/(3,12,7) 4  10; 10/11  and  10/11; 10/11
96  64  [72,92,94]           (7,6,3)          4  11; 10/11
96  64  [80,88,92,94]        (5,10,5,3)/(11,7,6,3)/(11,10,5,3)  5
96  64  [80,88,94]           (11,10,7)        4  11; 10/11
96  64  [80,92,94]           (11,10,3)        4  11; 10/11
96  72  [-60,56,94]          (1,9,3)          4  10; 11
96  72  [36,78,94]           (1,1,5)/(1,3,5)/(4,3,5)  4
96  72  [36,80,94]           (1,9,3)/(4,9,3)  4
96  72  [56,92,94]           (1,5,3)/(7,5,3)  4  10; 10/11  and  11; 10/11
96  72  [88,92,94]           (7,5,3)          4  11; 10/11
96  80  [24,92,94]           (6,3,3)          4  11; 10/11
100 40  [70,95,98]           (8,4,4)          4  11; 10/11
100 80  [50,95,98]           (1,8,4)/(3,8,4)  4  10; 10/11  and  11; 10/11
```

Moh six, for the record: `(64,48)` `u_s=1` (10); `(84,56) M₂=64`
`u_s=1` (10); `(84,56) M₂=72` `u_s=1` (10) and (11); `(75,50)` both
`u_s=1` (10); `(99,66)` **`u_s=3`** (10), Prop 6.3 not automatic.

**52/52 excess rows have `u_s=1`.** The `n≤100` ODE residue is a
descent residue: every excess row is a Prop 6.3/6.4 input. That does
not close `OPEN[MOH-PROGRAM-ARTIFACT]` (the CDC listing is still
missing); it retypes the 52 as descended monomial-Jacobian candidates
of bounded degree.

---

## 8. Side columns (not operative)

Through `D≤200`, PASSPORT groups = 1,261 (charged 1,261). POLY /
POLY+ODE were evaluated on TREE survivors through `D=200` (fail-closed
on Moh's six) and are not added into any headline count. The §6 family
happens to pass both at sampled `t`; that is a measurement, not a
promotion of (3.8) or of edgewise recentring.

---

## 9. OPENs, bounded, cheapest test

```text
OPEN[STAR-REALISABILITY]  untouched.  Geometric existence of any
   nested packet, including the §6 family and the D=108 target.
   Cheapest: Prop 4.6 at D1 on the N=15 packet of the named D=108 group.

OPEN[SIBLING-COEFFICIENTS]  charged residual.  Bounded: the D=108
   named target (s=4, two V-assignments) and one n≤100 excess
   (e.g. (90,60)).  Cheapest: A.3 ODE for sibling p,q at j=3.

OPEN[MOH-PROGRAM-ARTIFACT]  not closed.  49 excess after PASSPORT
   (52 after ODE).  No desk test.

OPEN[FULL-TREE-RECENTER]  unchanged; side column.

OPEN[PASSPORT-SHARPNESS]  unchanged; side column.

OPEN[MINOR-DICHOTOMY] / theorem (T)  the §6 family has u_s=1 for
   every t, so Prop 6.3 produces an unbounded-degree s'=2
   monomial-Jacobian family (deg 12t+4).  That is the leftover
   proof program.  Cheapest: one large-t descended pair
   (t=3, n=160 → degrees 40, 28).
```

Q3(f) after the screen is answered: **no proof program by emptiness**.

---

## 10. Typed block

```text
LANE          SCREENED-CENSUS (Grok 4.6), 2026-09-03
CHARGED       delta 17(r); C_FULL_TREE / ODE; nested-pack 587/470;
              enumerator d20bf0841a1ba2b2.
PROVED-HERE   K=16 family for all t≥1 (gcd, windows, δ₂=1/4, A₂=4,
              P=12≡0, A₁=e, (12) identically, q=(2t+1)/4, N=6t+3,
              TREE/ODE partition, nested one NZ packet, census
              emission).  52/52 ODE excess rows at n≤100 have u_s=1.
CONFIRMED     unscreened 1189/587/470 and 14016; n≤100 658→60/58/55/
              23/20; Moh six on every screen; FT=TI row-for-row;
              D=105 and D=117 TREE-empty; both named rays TREE-dead
              with b_min>h identically; D≤200 TREE 1516 / ODE 1384 /
              PASSPORT 1261 groups.
MEASURED      operative nested after ODE: D≤120  51 N≥6 / 43 [6,16]
              of 103 ODE groups; D≤200  727 / 523 of 1384;
              D≤238  1224 / 872 of 2262 (loop stopped: D=240 nested
              mix-DP exceeded remaining desk budget).
              D=108: 5 groups in [6,16], all s=4 u_s=1; D=112: 2;
              D=120: 18.  TREE-empty degrees at D≤200 as charged
              plus ODE-kills {174,184} and nested-kills {72,80}.
REFUTED       cofinal emptiness of C_FULL_TREE_ODE + nested N≥6
              (the K=16 family); Q3(f) as a screened-census proof
              program.  Sol L=8a+5 and A₂=6 rays as screened-cofinal
              (already delta 17(r); reconfirmed).
NOT CLAIMED   geometric realisation of any packet; Jacobian pairs at
              D=108 or along the family; passport/recenter as
              operative; OPEN[MOH-PROGRAM] closed; UNI 865 as nested.
SIDE          PASSPORT 1261 groups at D≤200 (EXTERNAL).  POLY /
              POLY+ODE fail-closed, OPEN, not in headlines.
ARTIFACTS     box/screened-census/screened_census.py
              box/screened-census/listings_108_112_120.json
              box/screened-census/residue_n100.json
              box/screened-census/census_through_238.json
              box/screened-census/screened_census.log
              enumerator / tree / nested-pack hashes as in the gate.
```

No `charge_basis` line: this report asserts no new exit price.

---

## 11. FALLACY-v2

Flag/place/series: Moh `n=D` is never mixed with campaign `n=deg Ā_F`.
Per-ray: the `K=16` family is one V-assignment, one NZ packet, charged
once. Carrier: nested N is a packet, not `FULL_ACTUAL_EXIT`.
Floor/attainment: knapsack existence ≠ geometric realisation; `P≡0
(mod A₂)` is the TREE survival mechanism, not attainment of a pair.
Pole/interior: unused. `sat()`: unused. The `s=3` kill `b_min>h` is
not applied to `s>4` rows whose danger has already cleared (D=108
lists). Merge-free/M-descent: unused. No cap-fill.

<!-- BODY-END -->
