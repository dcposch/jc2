# Rigid stratum ∩ gap-free tree screen; congruence form; a screened cofinal ray

Lane: Grok 4.6. Round `20260903T1200Z`. Desk only. Canonical ledgers not
edited. `jc2-lean` not inspected. No `ideation-20260903T1200Z-*` file other
than the charged Opus submission was opened. No running-lane report was
opened. `FALLACY-v2` in force. No new exit-price assertion, so no
`charge_basis` line.

## 0. Custody and hashes

Frozen inputs, SHA-256 verified byte-exact before any read:

```text
2e4e817267cbfdba97607a41df0433b11f3d4542dbb5418226aa48982830accd  ideation-20260903T1200Z-opus5.md
693b206806a75a557bfb02683fc7b937d0529a677b4b7476cac3b4c9a151cd0e  dessin-tower-dim-grok46-20260903.md
27551a88ab6ee9f62a5606010adcd9d4a1fd4411a09d97c699e13a67c84f7096  whole-tree-review-opus5-20260903.md
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  full_tree_partition.py
5d1b21222eecc448975c83d3628c22ada5cd26737155ecf2a7a27304ec40e553  candidate_eval.py
01a5341fec7e5f26a31671c5227b3851bf6635f6ef0f3f1f9f00d0172431ffd2  candidate-results.json
4402bf528d18f8c409935433ce7a0bea5e3b2e6c23a1735f4341218035d11ad9  opus5_probe.py
36b374b21b3768e841ad2cc2168d7e669d9b0d6e6b6c8d1737d203acbd079067  nested_pack.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full.py
```

Drivers: `box/rigid-congruence-20260903/` (byte copies of the two tree
modules; SHA-256 match). Operative screens (AUDIT 17(u), whole-tree-review
§7.4): partition + universal siblings + (12)/(13), Prop. 5.6 **disabled**
(`embed_node` starts with `dangerous=False`), optionally + ODE (3.7) and
passport (3.8). Side column: gapped `C_FULL_TREE` / `C_FULL_TREE_ODE`
(ungated Prop. 5.6).

---

## Direct answer

**(A)** The gap-free screen does **not** kill the rigid stratum. All **19**
expdim-0 V-assignments of dessin-tower-dim §6.4 survive partition + siblings
+ (12)/(13) **and** ODE **and** passport. The gapped `C_FULL_TREE` (and
`_ODE`) keeps **3 / 19**; the other 16 die at the ungated Prop. 5.6 step
(killing node `j=2` or `j=3`). Those 19, and especially the 3 that also
survive the gapped column, are the campaign's most concrete zero-dimensional
CE candidates. All 19 have nested-pack orbit size `|O|=1` and a single
zero-centred packet (the selected path is the π-factor). Of the 13 with
`u_s=1`, **none** currently has a legal Appendix-II `s'=2` system: 11
descend to `s'=3`; the two that descend to `s'=2` have `V_2'>d_2'`
(`U-NEGATIVE`); the 3 gapped survivors are all **anchor-zero**, so Def 5.1(3)
on the descended pair is undefined (`OPEN[DESCENT-ANCHOR]`).

**(B)** H4 is an identity: `h_j = d_j/(n-M_j) = P_j/Q_j` on **59,175 / 59,175**
selected-path nodes at `48≤D≤200`. On `Q>P` the screen is `A_j | P_j`; off
that stratum `b ≤ h` is enough. A **screened cofinal ray with `(d,e)` and `s`
fixed** exists in closed form, extending the D=108 `C_FULL_TREE_ODE` survivor
`(108,72; M=(84,104,106); V=(8,8,3))`. On the arithmetic progression
`t=6+9k` (`k≥0`) one has `A_2=3` constant, `P_2=56+48k`, **`b_2=2` constant**,
and `h_2=(7+6k)/2 ≥ 7/2 > 2`, so `b≤h` at every node; `A_3=1` (trivial).
Six members (`t=0,6,15,24,33,42`) were re-checked by the frozen drivers:
(1)–(13) + gap-free partition + ODE + passport + gapped `C_FULL_TREE_ODE` +
UNI `N≥6`. Comparison (does **not** keep `(d,e)`): the K=16 family
`n=48t+16`, `m=32t+16`, `M=(n-12,n-2)`, `V_2=V_3=3` has `A_2=4`, `P_2=12`,
`b=0` **identically** for every tested `t=1..20,30,40,50` (includes Moh's
`(64,48)` and the D=112 TREE UNI survivor). So the residue is **not** forced
constant-and-nonzero along every linear extension; `OPEN[SCREEN-CONGRUENCE-RAY]`
is answered by a construction, not a kill.

**(C)** Pre-screen `u_s>1` reproduces Opus: **4,012 / 14,016** groups
(6,117 / 23,720 rows). Post-screen, `48≤D≤200`, `K_min=16`:

| screen | rows | groups | `u_s>1` rows | frac | `u_s>1` groups | frac |
|---|---:|---:|---:|---:|---:|---:|
| gap-free partition | 12,323 | 6,382 | 3,204 | 0.2600 | 1,809 | 0.2835 |
| gap-free + ODE + passport | 11,590 | 6,039 | 3,014 | 0.2601 | 1,700 | 0.2815 |
| gapped `C_FULL_TREE` | 3,090 | 1,516 | 423 | 0.1369 | 260 | 0.1715 |
| gapped `C_FULL_TREE_ODE` | 2,824 | 1,384 | 310 | 0.1098 | 177 | 0.1279 |

Anchor-zero (`M_{s−1}=n-d_s`) among screened `u_s=1`, domain of (T):

| screen | `u_s=1` rows | of which az | `u_s=1` groups | of which az | (T)-evaluable rows |
|---|---:|---:|---:|---:|---:|
| gap-free + ODE + passport | 8,576 | 1,345 | 4,339 | 685 | 7,231 |
| gapped `C_FULL_TREE` | 2,667 | **1,591** | 1,256 | 774 | 1,076 |
| gapped `C_FULL_TREE_ODE` | 2,514 | **1,494** | 1,207 | 759 | 1,020 |

At `n≤100`, `C_FULL_TREE_ODE`: **57 / 58** have `u_s=1` (the exception is
`(99,66)`, `u_s=3`); **38 / 57** are anchor-zero; **19** evaluable —
reproducing Opus H1. The gapped frontier is ~60 % anchor-zero; the gap-free
`u_s=1` residue is only ~16 % anchor-zero. Theorem (T) as currently stated
covers 19 rows at `n≤100` and 1,020 rows / 448 groups at `D≤200` under the
gapped ODE screen.

---

## 1. Controls (fail-closed)

Printed before any result number. All passed.

| control | measured | expected |
|---|---|---|
| Moh's six survive gap-partition, +ODE, +passport, `C_FULL_TREE`, `_ODE` | 6/6 | 6/6 |
| `n≤100` (1)–(13) rows / `(n,m)` classes | 658 / 63 | 658 / 63 |
| gap-free partition / +ODE / +passport at `n≤100` | 348/52, 347/52, 330/52 | 348, 347, 330 (review §7.4) |
| gapped `C_FULL_TREE` / `_ODE` at `n≤100` | 60/12, 58/12 | 60, 58 |
| `48≤D≤200` V-assignments / groups / UNI `N≥6` | 23,720 / 14,016 / 8,831 | candidate-results.json |
| pre-screen `u_s>1` groups | 4,012 / 14,016 | Opus §3 |
| gapped TREE / ODE rows at `D≤200` | 3,090 / 2,824 | 3,090 / 2,824 |
| gapped TREE rows at D=108, 112, 120 | 21, 8, 94 | candidate-results.json |
| gapped ODE rows at D=108 | 20 | Opus (217→21→20 at n=108) |
| H4: `h=P/Q` on selected nodes `D≤200` | 0 failures / 59,175 | identity |

The (75,50) TREE residue remains `{M_2=55, V_2∈{2,3}}` (not re-listed; the
n≤100 TREE count 60 includes it).

---

## 2. (A) Rigid ∩ screen

The 19 lines of dessin-tower-dim §6.4 recover uniquely from the (1)–(13)
census (`K_min=16`), each with `k_sat∈{1,2}` and the printed UNI `N`.
`expdim_A=max(k_sat-2,0)=0` on all 19.

Gap-free columns: P = partition+siblings+(12)/(13); O = +ODE; S = +ODE+passport.
Side: T = `C_FULL_TREE`; D = `C_FULL_TREE_ODE`. `j` = gapped killing node
(ungated Prop. 5.6). `fr` = selected-path free set empty? (gated 5.6 available
iff empty). Packets: all 19 have `|O|={1}` and one Z-packet `w=V_2`,
`c=V_2 q`.

```text
 n   m   M                 V           de    us az N        P O S T D  j  fr
 60  40  -10,45,58         11,8,4      2,3    1  . 10       1 1 1 0 0  3  empty
 80  60  68,78             7,3         3,4    1  . 7,14     1 1 1 0 0  2  empty
 84  63  49,82             7,5         3,4    2  . 7,14     1 1 1 0 0  2  empty
 96  72  -8,20,94          7,6,3       3,4    1  . 8,16     1 1 1 0 0  3  nonempty
 96  72  -8,76,94          7,6,3       3,4    1  . 8,16     1 1 1 0 0  3  empty
 96  72  56,92,94          7,5,3       3,4    1  Y 7,14     1 1 1 1 1  -  empty
 96  72  80,84,94          7,6,3       3,4    1  . 7,14     1 1 1 0 0  3  nonempty
100  75  85,98             7,3         3,4    2  . 7        1 1 1 0 0  2  empty
108  72  60,80,106         20,9,3      2,3    1  . 16       1 1 1 0 0  3  nonempty
108  72  60,100,106        20,9,3      2,3    1  . 16       1 1 1 0 0  3  empty
108  72  90,106            17,16       2,3    2  Y 17       1 1 1 0 0  2  nonempty
108  72  90,99,106         17,16,8     2,3    1  Y 17       1 1 1 1 1  -  nonempty
120  72  12,44,118         8,9,3       3,5    1  . 10,20    1 1 1 0 0  3  nonempty
120  72  12,76,118         8,9,3       3,5    1  . 10,20    1 1 1 0 0  3  empty
120  90  -10,25,118        7,6,3       3,4    2  . 8        1 1 1 0 0  3  nonempty
120  90  -10,95,118        7,6,3       3,4    2  . 8        1 1 1 0 0  3  empty
120  90  100,105,118       7,6,3       3,4    2  . 7        1 1 1 0 0  3  nonempty
120  80  88,118            17,7        2,3    1  . 17,34    1 1 1 0 0  2  empty
120  80  100,110,118       17,16,9     2,3    1  Y 17,34    1 1 1 1 1  -  nonempty
```

**Survivors: 19 / 19 gap-free (all three operative columns); 3 / 19 gapped.**
The screen does **not** kill the rigid stratum. The gapped column kills 16/19
by ungated Prop. 5.6 along an all-zero selected path (`|O|=1`, Z-packet). Of
those 16, **9 have empty free set** (gated Prop. 5.6, the §7.4 repair, would
also kill them) and **7 have nonempty free set** (they die only under the
gapped ungated step; they are H3-type: `b>h` on the selected path, siblings
feasible).

Selected-path congruence on every rigid row (H4 holds on each node). Typical
shape: at least one node with `A ∤ P` and `b>h` (forced major zero), survived
because a sibling partition exists. The 3 gapped survivors are the ones whose
selected path is **not** forced-major-zero at every edge (`b≤h` or `A|P`).

### 2.1 Descent and Appendix-II size (`u_s=1`)

`u_s=d_s-V_s`. Descent: `n'=n/d_s`, `m'=m/d_s`, `M_i'=M_i/d_s` (`i<s`),
`V_i'=V_i`, `k=V_s-2`, `s'=s-1`. Size: D1 monomial count of
`box/appendix2/shape.py` when `s'=2` and Def 5.1(3) is defined; else typed.

| parent | `(n',m'; M'; V'; k)` | `s'` | az' | size |
|---|---|---:|---|---|
| (60,40) | (12,8; −2,9; 11,8; k=2) | 3 | n | not s'=2; child windows fail (`V_3'=8>d_3'=2`) |
| (80,60) | (20,15; 17; 7; k=1) | 2 | n | `U-NEGATIVE` (`V_2'=7>d_2'=5`); crude `K'(K'+1)/2=15` |
| (96,−8,20,94) | (24,18; −2,5; 7,6; k=1) | 3 | n | not s'=2 |
| (96,−8,76,94) | (24,18; −2,19; 7,6; k=1) | 3 | n | not s'=2 |
| (96,56,92,94) **T** | (24,18; 14,23; 7,5; k=1) | 3 | **Y** | ANCHOR-ZERO; Def 5.1(3) den `n'-M_{s'}'-1=0` |
| (96,80,84,94) | (24,18; 20,21; 7,6; k=1) | 3 | n | not s'=2 |
| (108,60,80,106) | (27,18; 15,20; 20,9; k=1) | 3 | n | not s'=2 |
| (108,60,100,106) | (27,18; 15,25; 20,9; k=1) | 3 | n | not s'=2 |
| (108,90,99,106) **T** | (12,8; 10,11; 17,16; k=6) | 3 | **Y** | ANCHOR-ZERO |
| (120,12,44,118) | (30,18; 3,11; 8,9; k=1) | 3 | n | not s'=2 |
| (120,12,76,118) | (30,18; 3,19; 8,9; k=1) | 3 | n | not s'=2 |
| (120,88,118) | (15,10; 11; 17; k=5) | 2 | n | `U-NEGATIVE` (`V_2'=17>d_2'=5`); crude 15 |
| (120,100,110,118) **T** | (12,8; 10,11; 17,16; k=7) | 3 | **Y** | ANCHOR-ZERO |

The 3 gapped-TREE rigid survivors (marked **T**) are all anchor-zero. The
zero-dimensional coefficient system the Card 2 hoped to solve is **not** an
Appendix-II `s'=2` pair under the promoted δ' rule. Residual: the pre-descent
sibling system on the 19 (gap-free) or on the 3 (gapped), or a repair of
`OPEN[DESCENT-ANCHOR]`. Typed OPEN, not filled by the crude triangular count.

The six `u_s=2` rigid rows do not descend (`OPEN[MINOR-DICHOTOMY]` residue).

---

## 3. (B) Congruence scan, D = 108, 112, 120

Counts (V-assignments / groups / UNI `N≥6` groups). Baseline is (1)–(13).

| D | baseline | gap-free P | gap-free +ODE+pass | gapped TREE | gapped ODE |
|---:|---|---|---|---|---|
| 108 | 206 / 125 / 87 | 93 / 49 / 26 | 88 / 46 / 25 | 21 / 13 / 8 | 20 / 12 / 8 |
| 112 | 76 / 71 / 33 | 31 / 29 / 8 | 31 / 29 / 8 | 8 / 7 / 2 | 8 / 7 / 2 |
| 120 | 782 / 515 / 271 | 366 / 223 / 95 | 329 / 206 / 80 | 94 / 53 / 28 | 82 / 46 / 22 |

H4 holds on every selected node below. Tuple `(A, P, Q, P mod A, h=P/Q)`.
Forced-zero siblings at a node share `(A,P,Q,h)` (level-data depends on
`V_{j+1},…,V_s` only); they differ by the child `V_j=b`.

### 3.1 D = 108, gapped ODE, UNI `N≥6` (12 rows; 8 groups)

```text
M                    V         us az  N           j=3 (A,P,Q,b,h)     j=2 (A,P,Q,b,h)
81,106               7,7        2  .  21          (s=3)               4,28,21,0,4/3     A|P
84,104,106           8,8,3      1  Y  16          1,9,3,0,3           3,24,16,0,3/2     A|P both
12,102,106           1,8,5      1  Y  10,15,20    1,10,5,0,2          21,24,64,3,3/8    b=3>h
12,102,106           3,8,5      1  Y  18          1,10,5,0,2          21,24,64,3,3/8    b=3>h
24,78,106            1,1,5      1  .  6..15       6,10,25,4,2/5       2,3,7,1,3/7       both f0
24,78,106            1,4,5      1  .  6,8,..20    6,10,25,4,2/5       3,12,28,0,3/7
48,90,106            1,1,5      1  .  6           7,10,15,3,2/3       2,3,5,1,3/5
48,90,106            1,3,5      1  .  6,9,12      7,10,15,3,2/3       1,9,15,0,3/5
-18,60,106           2,15,5     1  .  24          39,15,40,15,3/8     2,30,105,0,2/7
54,99,106            1,12,8     1  Y  6,9,12      1,16,8,0,2          7,24,36,3,2/3     b=3=h
54,99,106            3,12,8     1  Y  18          1,16,8,0,2          7,24,36,3,2/3
90,99,106  (rigid T) 17,16,8    1  Y  17          1,16,8,0,2          15,32,16,2,2      b=2=h
```

H3 is visible here: several UNI ODE survivors have `b>h` at a node
(`12,102,106` at j=2; `24,78,106` at j=3) and still survive, because the
forced-zero sibling admits a feasible lower tree. The two `A|P` rows
`(81,106)` and `(84,104,106)` are the congruence-clean seeds.

Forced-zero sibling `b`-lists (same `(A,P,Q)` as the node): e.g. `(81,106)`
at j=2 has forced major `b∈{4,8,12,16,20,24,28}` (all `>4/3`); the selected
path takes the **nonzero** `V_2=7` (not in that list), so Prop. 5.6 never
engages — TREE survives. The rigid `(90,99,106)` has forced major
`b∈{17,32}` at j=2 and selected `V_2=17` **is** the zero-factor of
multiplicity 17 (`17>2` would be major, but `b_min=2≤h=2` so zero need not
be taken; selected 17 is a major nonzero).

### 3.2 D = 112, gapped TREE, UNI (3 rows / 2 groups)

```text
(112,80) M=(100,110) V=(3,3)   N=15   j=2: (4,12,9,0,4/3)   A|P   [K=16, t=2]
(112,84) M=(42,105,110) V=(1,11,6)  N=6..24  j=3: (1,12,6,0,2); j=2: (6,22,55,4,2/5)  b=4>h
(112,84) M=(42,105,110) V=(4,11,6)  N=16,32  same (A,P,Q,b,h)
```

### 3.3 D = 120, gapped TREE, UNI: 35 rows / 28 groups

Pattern as at 108: many rows have `A_3=1` (δ_3=0) and a j=2 node that is
either `A|P` or `b>h` with a feasible sibling. Sample, including the
`(d,e)=(2,3)` class of the constructed ray's degree-120 neighbour:

```text
(120,80) M=(90,115,118) V=(7,7,4)  N=21  j=3 (1,8,0,4); j=2 (4,28,21,0,4/3)  A|P
(120,80) M=(100,118) V=(5,16)      N=6,9,..18  j=2 (5,32,16,2,2)
```

Full dumps: `box/rigid-congruence-20260903/results.json`.

---

## 4. (B) Construction: a screened cofinal ray with `(d,e)` and `s` fixed

### 4.1 The family (PROVED-HERE as skeletons; driver-checked)

Seed: the D=108 congruence-clean ODE UNI survivor

\[
n=108,\; m=72,\; M=(84,104,106),\; V=(8,8,3),\;
(d,e)=(2,3),\; s=4,\; K=36.
\]

Windows `n-M_2=24`, `n-M_3=4` are held constant. Linear extension, `V_2`
slope 2, `V_3` slope 0 (charged: vary `V_2,V_3` linearly; slope 0 is
linear):

\[
K(t)=36+8t,\quad
n(t)=3K=108+24t,\quad
m(t)=2K=72+16t,
\]
\[
M(t)=(n-24,\,n-4,\,n-2),\quad
V(t)=(8+2t,\,8,\,3).
\]

`(d,e)=(2,3)` and `s=4` for every integer `t≥0` at which the gcd chain
exists. The (1)–(13) locus inside `t=0..80` is

\[
t=0 \qquad\text{and}\qquad t=6+9k\ (k\ge 0).
\]

On the arithmetic progression `t=6+9k`:

\[
\begin{aligned}
n&=252+216k, & m&=168+144k, & K&=84+72k,\\
V_2&=20+18k, & V_3&=8, & V_4&=3,\\
d&=(n,\,K,\,12,\,4,\,2) & &\text{(}d_3,d_4,d_5\text{ frozen).}
\end{aligned}
\]

Radii are **frozen** (Def 5.1(3) along this ray):

\[
\delta=(-1,\;0,\;1/3,\;4/9)
\quad(\delta_4,\delta_3,\delta_2,\delta_1),\qquad
A_1=3,\ \text{(12) holds identically}.
\]

Galois data at the two internal nodes:

| node | `A(t)` | `P(t)` | `Q(t)` | `b=P\bmod A` | `h=P/Q` |
|---|---|---|---|---|---|
| `j=3` | `1` | `9` | `3` | `0` | `3` |
| `j=2` | `3` | `56+48k` | `16` | **`2`** | `(7+6k)/2` |

So `b_2=2` is constant and **nonzero**, but `h_2=(7+6k)/2 ≥ 7/2 > 2`, hence
`b≤h` (no forced major zero). This is **not** the `Q>P` stratum (`Q_2=16 < P_2`
for all `k≥0`), so H4's `A|P` criterion is not the operative one; the weaker
`b≤h` is. `A_3=1` makes `j=3` vacuous. UNI packet: `q=2/3` constant,
`N=40+36k ≥ 6`. `u_s=1` identically. **Anchor-zero identically**
(`M_3=n-4=n-d_4`).

Driver check, six members `t=0,6,15,24,33,42` (n=108,252,468,684,900,1116):
each satisfies (1)–(13), gap-free partition, ODE, passport, gapped
`C_FULL_TREE` and `_ODE`, and UNI `N∈{16,40,76,112,148,184}`. At `t=0` one
has the stronger `A_2|P_2` (`b=0`); the AP tail has `b=2≤h`. Nested N≥6
holds (UNI already).

This is a screened cofinal ray in closed form, with `(d,e)` and `s` held.
It lives on the anchor-zero locus, so it is **outside** the present domain
of theorem (T).

### 4.2 Comparison: K=16 family (does not keep `(d,e)`)

Independently reconstructed from the charged Def 5.1 / (1)–(13) arithmetic
(AUDIT 17(v) recorded it; this lane did not open that report):

\[
e=3t+1,\ d=2t+1,\ \gcd(d,e)=1,\quad
n=16e=48t+16,\ m=16d=32t+16,
\]
\[
M=(n-12,\,n-2),\quad V_2=V_3=3.
\]

`(d,e)` **moves**. For every tested `t=1,2,…,20,30,40,50` (23 members, n up
to 2,416): (1)–(13), all gap-free columns, gapped TREE and ODE, `A_2=4`,
`P_2=12`, **`b=0` identically**, `h=4/3`, `N=6t+3`. `t=1` is Moh's printed
`(64,48)`; `t=2` is the D=112 TREE UNI survivor of §3.2. `u_s=1`,
**anchor non-degenerate** (`M_2=n-12 ≠ n-4=n-d_3`). This is the cleaner
A|P ray; it is not the charged `(d,e)`-fixed construction.

### 4.3 What fails, and the leftover conjecture

The other D=108 `A|P` seed `(108,72; M=(81,106); V=(7,7); s=3)` with
window `n-M_2=27` does **not** extend: already at `t=1` along
`K(t)=36+36t` (the modulus that freezes `A_2=4`, `P_2=28(t+1)`, `b=0`)
windows and (10)/(11) hold but **(12)/(13) fails** (`A_1` jumps 3→34).
The obstruction is the **bottom** congruence, not `A_2 ∤ P_2`.

So: a constant nonzero residue at an internal node is **not** forced along
every `(d,e)`-fixed linear extension (counterexample: §4.1, `b=2≤h`, and
K=16, `b=0`). A kill of the shape "internal `A|P` fails with constant
`b>h`" is false as an all-degree statement (H3 + §4.1). A remaining
**conjecture, exact hypothesis**, not claimed:

> **(not claimed).** Along a `(d,e)`-fixed window-constant extension of an
> `s=3` skeleton for which `A_1(t)` is unbounded, (12)/(13) fails for all
> sufficiently large `t`.

Cheapest test already done on the `(81,106)` seed (fails at `t=1`). Not
promoted: one seed, and §4.1 shows `s=4` with frozen `A_1=3` is cofinal.

`OPEN[SCREEN-CONGRUENCE-RAY]` is **answered by a construction** (two, one
of them `(d,e)`-fixed).

---

## 5. (C) Post-screen `u_s>1` and the domain of (T)

`u_s=d_s-V_s` is a group-level quantity. Pre-screen at `48≤D≤200`,
`K_min=16`: **4,012 / 14,016 groups** (28.62 %) and 6,117 / 23,720 rows
(25.79 %), matching Opus §3.

Post-screen (same census, the four operative/side screens): see Direct
answer. The gap-free fraction is essentially the pre-screen fraction
(~26 % rows / ~28 % groups). The gapped TREE step cuts `u_s>1`
preferentially (13.7 % rows / 17.2 % groups; ODE 11.0 % / 12.8 %).
`OPEN[MINOR-DICHOTOMY]` is **not** a 4,012-group bottleneck after the
gapped screen: 177 ODE groups at `D≤200`. After gap-free+passport it
remains 1,700 groups — still the large residue if the campaign retires
ungated Prop. 5.6.

Anchor-zero among screened `u_s=1` (Direct answer table). Reproducing
Opus H1 at `n≤100` ODE: 58 rows, 57 descendable, 38 anchor-zero, 19
evaluable. At `D≤200` the gapped ODE (T)-domain is **1,020 rows / 448
groups**; the gap-free+passport (T)-domain is **7,231 rows / 3,654
groups**, of which most will still need the gapped-or-gated 5.6 question
settled before anyone treats them as Moh-program survivors.

The constructed `(d,e)`-fixed ray of §4.1 is entirely anchor-zero, hence
**outside** (T). The K=16 ray is inside (T)'s `u_s=1` + non-az box.

---

## 6. OPEN ledger (bounded quantity + cheapest test)

| OPEN | this lane | bounded quantity | cheapest leftover |
|---|---|---|---|
| Card 2 rigid ∩ screen | **answered**: 19/19 gap-free, 3/19 gapped TREE | 19 assignments; 3 gapped survivors, all az | sibling system on the 3, or DESCENT-ANCHOR repair |
| `OPEN[SCREEN-CONGRUENCE-RAY]` | **answered by construction** | 6+6 checked members; K=16: 23 members | realise one member at coefficient level |
| `OPEN[MINOR-DICHOTOMY]` | post-screen number | 3,014/11,590 gap-free+pass rows; 310/2,824 gapped ODE | none; the number was the test |
| `OPEN[DESCENT-ANCHOR]` | coverage at `D≤200` | 1,494/2,514 gapped-ODE `u_s=1` rows are az (38/57 at n≤100) | Card 1 of the charged Opus (source, not this lane) |
| (T) domain | measured | 19 evaluable at n≤100 ODE; 1,020 rows / 448 groups at D≤200 ODE | — |

No OPEN was filled by cap. The `(d,e)`-fixed ray is a skeleton family, not a
map: `REPRESENTATIVE` of a screened cofinal set, not `FULL_ACTUAL_EXIT`.

---

## 7. Desk

Python 3 stdlib. One core. Peak RSS well under 4 GB (TreePartition caches on
23,720 rows). Wall: rigid_congruence.py 82 s (of which (C) 62 s);
construct_ray.py 0.7 s; member verification 2 s. Total ~85 s.

Moh pages used only as already charged (Def 5.1(3), (8)–(13), Prop. 5.6 as
the gapped side column). No `jc2-lean`. No ledger edit. No other
`ideation-20260903T1200Z-*`. No running-lane report.

---

## Disposition

| item | status |
|---|---|
| Rigid ∩ gap-free screen | **19/19 survive** (ODE+passport too); not a kill of the rigid stratum |
| Rigid ∩ gapped `C_FULL_TREE(_ODE)` | **3/19**; all three anchor-zero; killing node j=2 or 3 on the other 16 |
| Appendix-II size on rigid `u_s=1` | none currently solvable as s'=2 D1; 2× U-NEGATIVE, 3× az, rest s'=3 |
| H4 `h=P/Q` | identity, 0/59,175 failures |
| `(d,e)`-fixed screened cofinal ray | **constructed**, AP `t=6+9k`, `b_2=2≤h`, 6 members driver-checked |
| K=16 comparison ray | `A_2\|P_2` identically; not `(d,e)`-fixed; 23 members checked |
| Constant-nonzero internal residue as all-degree kill | **false** as stated (this construction + H3) |
| Post-screen `u_s>1` | 26 % gap-free; 11–14 % gapped (vs 29 % pre-screen groups) |
| (T) domain, gapped ODE, `D≤200` | 1,020 rows / 448 groups (n≤100: 19) |
| `OPEN[SCREEN-CONGRUENCE-RAY]` | answered as a family, not a theorem of emptiness |

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `22164`.
- Body SHA-256:
  `1c3e0347fcf54d5d1cfcf5cfa1674bab8756cebe6eaa681f7231eee832fc4bc0`.
- Frozen basis: `13ab15af56fe786d30f013fc3611d754f6b94f09`.
