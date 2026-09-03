# MOHSIEVE leaderboard + DESCENT engine — Grok 4.6 — 20260903

Lane: `mohsieve-descent-engine-grok46-20260903`. Software, fail-closed, desk-scale.
One typed predicate harness over `box/moh_skeleton_full.py`, and Moh's Prop 6.3
descent as a machine gated on the p.207 table. **The leaderboard is MEASURED.
No predicate is claimed to BE Moh's program.** Provenance stays typed.

## 0. Custody

Frozen charged-input SHA-256 verified first (all 9 match); no mismatch, no stop.

| sha256 | file |
|---|---|
| `b13149ecac656f7f…c0022562` | ideation-20260903T1015Z-opus5.md |
| `486b0192d6cb1f3e…e5fc6456` | ideation-20260903T1015Z-fable5.md |
| `7b56aad2c1fb0674…16438015` | ideation-20260903T1015Z-grok46.md |
| `5e1646f507e946b8…d2f320d` | ideation-20260903T1015Z-gpt55.md |
| `fb137b92d88b2f59…a58f6948` | census-rebase-opus5-20260902.md |
| `d20bf0841a1ba2b2…b6c506c2` | moh_skeleton_full.py |
| `cf0780cc0b3ef0f2…63baebe6` | d1floor.py |
| `cdf5eeb7d9e40021…12d083d2` | moh4.py |
| `d6e40234299f21ba…29f251685` | battery.py |

Firewall: `jc2-lean` not inspected; canonical ledgers not edited; no other
`ideation-20260903T1015Z-*` file than the four charged; no other running
lane's report opened. Moh PDF was **not** required: Def 5.1 / Prop 4.6 / Prop
6.1–6.4 / p.207 are taken from the charged census-rebase transcription, the
Grok/Fable/GPT-5.5 charged submissions, and `moh_skeleton_full.py`. Display
formulae that the OCR drops are cited as transcribed there.

Host `ip-172-30-0-46`, Python 3.12.3, one core. Wall **14.7 s** (`python3 -O
box/mohsieve/run_all.py`), RSS **70 MB**. No AWS.

Artifacts (this lane; `box/moh_skeleton_full.py` untouched):

```text
box/mohsieve/mohsieve.py              e7c15ad3f3368fc2d8c99f05d96813e54dbd29d8e7af1d66b448fc800a8278e4
box/mohsieve/descent.py               dfb81ffef2050c582451b1e096c8ae20b6ff0c15b61c1be0aaf5be530c10948b
box/mohsieve/gates.py                 f67bbb57b417b3e30d669915d5ae0721c80c0b9d897f74fa1feb9f89d4f47e68
box/mohsieve/test_gates.py            8aa85c919b7ccba336dc76458e63e76dfd7da917eef84bd7c6d5deefb85e3e78
box/mohsieve/run_all.py               829d6977d67abab4f40a0be650f4267f3159a896a0446eff3f6a17bfbe16e7a2
box/mohsieve/descent_terminal.txt     4fa7950fe43f36676293b5cc11f732cf01d74227e6a10302138c6ae86968dd9e
```

## 1. Predicate registry

Each entry is `(name, source, lambda)`. Source ∈ {PRINTED, DERIVED, CONJECTURE,
SOURCE-UNVERIFIED, UNDEFINED}. `UNDEFINED` is not a filter. Load-bearing
checks use `gates.require` (live under `python3 -O`); exact division of
`Q = V_{j+1} d_j / d_{j+1}` is `Q_of`, not `assert`.

| name | source | lambda | note |
|---|---|---|---|
| MOH-INCREMENT | DERIVED | `A_j ≥ 2` for `j = 1..s−1` | `j=1` is Moh p.188 exclusive-or (false at `A_1=1`). `j≥2` is by analogy with the same automorphism sentence (CONJECTURE residue). |
| NOT-ALL-11 | DERIVED | `S.any10()` | some `j ∈ {2..s−1}` takes (10). Prop 5.6 numerical shadow; `r=2` gap is OPEN[PROP-5.6-SHADOW]. |
| MAJOR-MULT | SOURCE-UNVERIFIED | `V_j ≥ 2` for `j=2..s` | Opus reading of a major-disc `p(π)` factor as non-simple. Not recovered from the charged Def 5.1 / p.200 (4)–(7) transcription. |
| M2-ABOVE-M | CONJECTURE | `M_2 > m` | Fable: not found printed on the pages read. OPEN[M2-ABOVE-M]. AM semigroup is AUTOMATIC on 658/658 (Fable §2.4) and is **not** registered. |
| PARTITION | CONJECTURE | Card I, below | Prop 4.6 partition of `Q` at levels `j=s−1..2`. |
| SECOND-POINT | **UNDEFINED** | `fn = None` | not a filter; see §1.1. |

**Card I encoding (PARTITION).** At each level `j = s−1..2`, with
`Q = V_{j+1} d_j/d_{j+1}`, `A = A_j`, `(△, □) = divmod(Q, A)`,
`lo = d_j/(n−M_j)`: there exists a partition of `Q` into positive integer
parts, one of which equals `V_j`; every part is major (`(10)∨(11)`) or
minor (`≤ lo`, Prop 6.1); `a ≠ 0` parts come in Galois orbits of size `A_j`
(at most one `a=0` part, the factor `π`). Fail-closed: the six p.202 rows
must satisfy it (they do). **MEASURED: solo kill = 0 on 658, on 1,189 groups,
and on 14,016 groups.** Given (1)–(13) already requires `(10)∨(11)` of `V_j`,
the remainder is always fillable (the `a=0` multiplicity `□` itself satisfies
(11); orbits of size `A_j` absorb the rest). The predicate is **vacuous** on
the (1)–(13) space. That is Grok Card I's typed fail-to-separate: PROGRAM is
not this partition of `deg p`.

### 1.1 SECOND-POINT — what "the L_2 tower" would have to be, and why UNDEFINED

Def 5.1 constructs **one** tower of major discs `D_s ⊃ ⋯ ⊃ D_1` (census-rebase
§1.2; p.179). Prop 4.5 / the top of `p(π)` (moh.txt p.172, p.186): `q` has
degree `n − M_s = 2`, so `p` has two roots; one multiplicity is `V_s > d_s/2`,
the complementary multiplicity is `d_s − V_s < d_s/2`. The top form of `g` is
`L_1^u L_2^v` with `u = V_s K / d_s` and `v = K − u` (`moh_skeleton_N.py`:
`u+v=K`, `u>v`).

"Joint admissibility of the L_2 tower (`v` roots, `u ↔ v`) with the same
`(n, m, d_j)`" would mean: start Def 5.1 from the complementary root of `p(π)`,
swap `u ↔ v` so `V_s^{L2} = d_s − V_s`, and keep `(n, m)` and the gcd-chain
`d_j = gcd{n, M_1, …, M_{j−1}}` (independent of `V`).

That is **not a predicate of a single `(n,m,M_*,V_*)` row**, for three printed
reasons:

1. Def 5.1(2) requires `V_s > d_s/(n−M_s) = d_s/2`. Then `V_s^{L2} = d_s−V_s`
   fails the window and is a **minor** disc (Prop 6.1), not a second major tower.
2. Def 5.1 does not assign lower `V_j` to the complementary factor. Those values
   are not a function of the L_1 skeleton; "same `(n,m,d_j)`" does not determine
   them.
3. The minor-disc theory (Props 6.1–6.4, p.209 dichotomy) is a different
   machine, already owned by DESCENT for `u_s > 1`.

**Probe** (not a registered filter): replace `V_s` by `d_s−V_s`, keep `M_*`.
**0/6** printed rows survive windows. SECOND-POINT is typed UNDEFINED, excluded
from conjunctions, and is not a vacuous-pass: it has no lambda.

## 2. Gates G1–G5 and negative control

All HARD gates green (`python3 -O`, 115 `[ok]`, 0 `[FAIL]`).

| gate | statement | result |
|---|---|---|
| G1 HARD | six p.202 rows survive | 6/6 for EMPTY and every defined predicate (PARTITION included). SECOND-POINT has no lambda. |
| G2 | `(75,50)` after UNI `N ≥ 6` is exactly `{M_2=55, V_2 ∈ {2,3}}` | PASS on the two charged stacks: INCREMENT ∧ NOT-ALL-11 ∧ MAJOR-MULT, and M2-ABOVE-M. INCREMENT ∧ NOT-ALL-11 still keeps `(40,1)`. MAJOR-MULT still keeps `(40,2)`. |
| G3 | n≤100 vs Moh 6/4 | EMPTY = **658 rows / 63 classes**. |
| G4 | groups and emptied degrees, 48≤D≤200, K≥16 | EMPTY = **14,016 groups**. 48≤D≤120 = **1,189 groups**. |
| G5 | pinned-N knapsack downstream (`uni_hits` / `mixed_hit`, N≥6 and [6,16]) | listing D=105/108/112/117/120; see leaderboard. EMPTY D=105: 14 groups, 7 with some integer N≥6, **3 with N ∈ [6,16] (the trio)**. |
| EMPTY negative control | 658/63 and 1,189 / 14,016 | exact. |
| solo kill | a predicate whose solo count equals the base is vacuous | PARTITION kill 0/0/0. SECOND-POINT not scored. |

Opus cascade replayed to the unit on n≤100: 658 → 391 (INCREMENT) → 247
(+NOT-ALL-11) → 86 (`V_2 ≥ 2`) → **51** (`V_j ≥ 2` all `j`). Fable M2-ABOVE-M:
**94 rows / 32 classes**; + UNI N≥6 → **33 rows / 17 classes**, **28 beyond**
Moh's table (the (84,56) `M_2=64` row dies at N≥6, as in #17 A.8). NOT-ALL-11
solo kill **220 groups** at D≤120, matching census-rebase OPEN[PROP-5.6-SHADOW].

## 3. Leaderboard

Passing = defined and G1 (keeps 6/6): INCREMENT, NOT-ALL-11, MAJOR-MULT,
M2-ABOVE-M, PARTITION. Every singleton, pair, and triple of those, plus EMPTY.
Columns: rows/classes n≤100; 6/6; (75,50) residue after UNI N≥6; groups
48≤D≤200; degrees emptied **by the sieve** (pre-knapsack); UNI N≥6 / mixed
[6,16] at D=105,108,112,117,120; D=108 UNI-rows in [6,16].

**Read the N columns as floors on the kill** (a group counted alive may still
die under a stronger reading of mixed/UNI). PARTITION conjunctions duplicate
the other factor (vacuous).

```text
conjunction                              n<=100   6/6  (75,50) after N  g200   emptied-by-sieve                         105  108   112  117  120   D108r
EMPTY                                    658/63   yes  5 pairs          14016  none                                     7/3  87/76 33/29 4/4  271/264  100
INCREMENT                                391/62   yes  (40,1)+55        8824   none                                     3/3  40/39 22/21 4/4  179/149   45
NOT-ALL-11                               469/43   yes  (10,1)(40,1/2)+55 12384 none                                     7/3  81/71 32/28 3/3  255/243   89
MAJOR-MULT                               312/55   yes  (40,2)+55        7638   63,88                                    1/0  39/33  3/3  2/2   92/81    40
M2-ABOVE-M                                94/32   yes  {(55,2),(55,3)}  1545   48,54,63,88,102,104,110,114,152,153,170  0/0   5/2   5/5  1/1   27/26     2
PARTITION                                658/63   yes  = EMPTY          14016  none                                     = EMPTY
INC & NOT-ALL-11                         247/42   yes  (40,1)+55        6093   none                                     3/3  34/33 21/20 3/3  158/125   37
INC & MAJOR-MULT                         195/54   yes  {(55,2),(55,3)}  5204   63,88                                    0/0  22/20  2/2  2/2   66/58    23
INC & M2                                 59/32    yes  {(55,2),(55,3)}   997   (same as M2)                              0/0   3/1   4/4  1/1   17/16     1
NOT-ALL-11 & MAJOR-MULT                  123/17   yes  (40,2)+55        3747   48,63,81,88,104,110,152,154               1/0  30/25  2/2  1/1   66/57    29
NOT-ALL-11 & M2                           45/16   yes  {(55,2),(55,3)}  1068   +60,81,105,154,186,…                      0/0   3/1   4/4  1/1   19/17     1
MAJOR-MULT & M2                           77/30   yes  {(55,2),(55,3)}  1228   M2 + 130                                  0/0   5/2   2/2  1/1   22/19     2
INC & NOT-ALL-11 & MAJOR-MULT  (MOH-4)    51/13   yes  {(55,2),(55,3)}  1908   48,60,63,81,88,104,105,110,152,154       0/0  15/14  1/1  1/1   43/35    15
INC & NOT-ALL-11 & M2                     20/14   yes  {(55,2),(55,3)}   593   18 degrees (incl. 72,90,105)              0/0   1/0   3/3  1/1   10/9      0
INC & MAJOR-MULT & M2                     51/29   yes  {(55,2),(55,3)}   783   M2 + 130                                  0/0   3/1   2/2  1/1   16/15     1
NOT-ALL-11 & MAJOR-MULT & M2              28/11   yes  {(55,2),(55,3)}   685   17 degrees                                0/0   3/1   1/1  1/1   14/11     1
(+ PARTITION)                            = the other factor of the pair/triple
```

MOH-4 emptied degrees **[48, 60, 63, 81, 88, 104, 105, 110, 152, 154]** match
Opus to the unit; MOH-4 groups **1,908** match. M2-ABOVE-M groups at D≤120:
1,189 − 1,010 = **179**, matching Fable; after UNI N≥6 at the listing degrees,
D=105 is 0/0, D=108 is 5/2, D=117 is 1/1, D=120 is 27/26, matching Fable's
D≤120 table on those cells.

**D=105 is emptied by the sieve** only under stacks that include MAJOR-MULT
together with enough of INCREMENT/NOT-ALL-11 to kill the non-trio residue, or
**by knapsack** under M2-ABOVE-M (5 groups remain after `M_2>m`, all with no
integer N≥6). G4 and G5 are distinct.

Tightest G1-passing stack on n≤100 is INC ∧ NOT-ALL-11 ∧ M2: **20 rows / 14
classes**, still 14 excess classes versus Moh's 4. OPEN[MOH-PROGRAM] is not
closed.

## 4. M2-ABOVE-M vs MAJOR-MULT (2×2)

On the 658-row n≤100 census:

```text
                 MAJOR-MULT=1    MAJOR-MULT=0
M2-ABOVE-M=1          77              17
M2-ABOVE-M=0         235             329
```

77+17+235+329 = 658. **Neither implication holds.** 17 rows have `M_2>m` and
some `V_j=1` (Fable's residual list already shows several `V_2=1` with `M_2>m`).
235 rows have every `V_j≥2` and `M_2≤m` (the D=105 trio is in this cell's
campaign analogue: `V_2=1` actually, so the trio is in (0,0) together with
other `M_2≤m` simple-bottom rows). The two charged sieves cut different
directions; their intersection is 77 rows at n≤100 / 1,228 groups at D≤200,
not a containment.

## 5. DESCENT engine (Prop 6.3/6.4)

Input: a (1)–(13) group with `u_s = d_s − V_s = 1`. Emit
`n' = n/d_s`, `m' = m/d_s`, `M_i' = M_i/d_s` for `i ≤ s−1` (drop `M_s`),
`d_i' = d_i/d_s`, Jacobian exponent `k = v_s − 2`. Re-run the gcd chain and
Def 5.1(2) windows on the inherited `V_2..V_{s−1}` with `V_{s'+1} := 1`, and
flag `M_2' > m'`. Recurse while `u_{s'}=1`. The engine **transforms**; a
WINDOW/GCD/INTEGRAL flag is not a degree-kill (G8).

### 5.1 G6 HARD — p.207 table to the unit

| p.202 row | u_s | n', m', M_2', k | tag | status |
|---|---|---|---|---|
| (64,48) | 1 | 16, 12, 13, 1 | X | TERMINAL (windows, gcd, M_2'>m') |
| (84,56) M_2=64, V_2=2 | 1 | 21, 14, 16, 1 | X | TERMINAL |
| (84,56) M_2=72, V_2=5 | 1 | 21, 14, 18, 1 | X | TERMINAL |
| (75,50) V_2=3 | 1 | 15, 10, 11, 2 | X^2 | TERMINAL |
| (75,50) V_2=2 | 1 | 15, 10, 11, 2 | X^2 | TERMINAL |
| (99,66) | 3 | — | — | no Prop 6.3 (p.207 excludes it) |

GPT-5.5 Appendix-II signatures, all present: `(16,12,13; X)`, `(21,14,16[18]; X)`,
`(15,10,11; X^2)`. Fourth-case **X^4** branch for (99,66): the p.209
linear-power alternative `n' = u_s n/d_s` etc. gives `(27, 18, 21; V_2=8,
k = v_s − u_s − 1 = 4)` = X^4. That branch is a **cross-check**, not a
Prop 6.3 step, and is not used as a filter.

### 5.2 G7, G8

G7: every printed `u_s=1` row has `M_i` (`i < s`) divisible by `d_s` (4 or 5).
G8: occupancy of (1)–(13) groups at D=64,75,84,99 is {9, 5, 38, 7}. The engine
does not drop them. Even if WINDOW/GCD/INTEGRAL were treated as kills, those
four degrees still have a surviving group (Moh's own TERMINAL rows at 64, 75,
84; (99,66) is `u_s>1` and is not touched by Prop 6.3).

### 5.3 Terminal table, 48 ≤ D ≤ 200

Full listing: `box/mohsieve/descent_terminal.txt` (10,004 `u_s=1` groups).

```text
groups 14,016
u_s = 1     10,004
u_s > 1      4,012   fraction 1003/3504 ≈ 28.6 %   (need p.209 minor-disc dichotomy)
first-descent status, u_s=1 only:
  WINDOW-FAIL         8,226   inherited V_2 often exceeds d_2' = K/d_s
  M2-LE-M             1,492   windows+gcd hold, M_2' ≤ m'
  TERMINAL              254   s'<3 or d_s'<4, windows+gcd+M_2'>m'  (p.207 shape)
  DESCENDED-IN-SPACE     32   s'≥3 and d_s'≥4 (rare; still outside K≥16 search)
```

WINDOW-FAIL is the generic fate of a `u_s=1` campaign group: the original
window allows `V_2 ≤ V_s · (K/d_s) = (d_s−1) d_2'`, while the shortened
tower has `V_{s'+1}=1` so `V_2 ≤ d_2'`. This is a **flag**, not a sieve, and
it does not fire on Moh's six (G6). Recursion past the first step is
per-row (`V_{s−1}` is not a group invariant) and is run on the printed rows
and the trio; none of Moh's TERMINAL rows have a second integral step
(`M_2'=13` is not divisible by `d_2'=4`).

## 6. D = 105 trio through both tools

Three (1)–(13) groups, all `m=70`, `K=35`, `(d,e)=(2,3)`, `V_2=1`:

| | M | V_s | d_s | u_s | q | UNI N | INCREMENT | NOT-ALL-11 | MAJOR-MULT | M2-ABOVE-M | PARTITION | descent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| G1 | [28,103] | 5 | 7 | **2** | 1/2 | 6..12 | T | T | F | F | T | **US-GT-1** (p.209 dichotomy; not Prop 6.3) |
| G2 | [28,103] | 6 | 7 | 1 | 9/13 | 9 (and 18) | T | T | F | F | T | **(15,10; γ^4, M_2'=4)**, status M2-LE-M |
| G3 | [40,103] | 4 | 5 | 1 | 9/17 | 9 | T | T | F | F | T | **(21,14; γ^2, M_2'=8)**, status M2-LE-M |

G2 and G3 match Fable §3 to the unit. Both descended pairs fail `M_2' > m'`
(4 ≰ 10, 8 ≰ 14): the trio is exactly the kind of `u_s=1` group the M2 flag
was built to see, **after** Prop 6.3 as well as before. G1 cannot descend by
Prop 6.3 (`u_s=2`); it is the (99,66)-shaped case.

Sieve: the trio dies on MAJOR-MULT (`V_2=1`) and on M2-ABOVE-M (`M_2 ∈ {28,40} < 70`).
It survives INCREMENT, NOT-ALL-11, and the vacuous PARTITION. Under MOH-4 the
degree has **0 groups**. Under M2-ABOVE-M it has 5 groups and **0** with integer
N≥6. EMPTY has 14 groups at D=105; the packet's "trio" is the 3 with N ∈ [6,16].

## 7. Unit tests, python3 -O, hashes, replay

```text
python3    box/mohsieve/run_all.py
python3 -O box/mohsieve/run_all.py
```

`run_all.py` enumerates once (n≤100 in 0.27 s; 48≤D≤200, 23,720 V-assignments
in ~8 s), then sieve, descent, and `test_gates.py` on the same cache.

AST scan of the harness (`mohsieve.py`, `descent.py`, `test_gates.py`,
`gates.py`, `run_all.py`, `__init__.py`): **0 `ast.Assert` nodes**. Every
load-bearing check is `require()`. `python3 -O` replay: `optimize=1`,
**115 `[ok]`, 0 `[FAIL]`, ALL GREEN**, wall 14.7 s, RSS 70 MB.

`box/moh_skeleton_full.py` (untouched) contains `assert` on exact division
inside `div9`. That library is **ordinary-only** for those two asserts
(COORDINATION.md). The harness does not consume them: `Q_of` re-checks
`d_{j+1} | V_{j+1} d_j` with `require`/`RuntimeError` and compares to
`div9`'s Q. Under `-O` the library asserts are stripped and the harness
checks remain. No optimized-mode evidence claim is made about
`moh_skeleton_full.py` itself.

Unit tests cover G1 (six rows, L2-swap 0/6, SECOND-POINT `fn is None`), G2
(both charged stacks), G3 (658/63, 1189, 14016), G4 (MOH-4 empties 105;
M2 does not, pre-knapsack), G5 (EMPTY D=105 is 14 groups / 3 in [6,16];
MAJOR-MULT kills the trio's [6,16]; M2 kills N≥6; MOH-4 has 0 groups),
G6–G7 (p.207 + GPT-5.5 signatures + X^4), G8 (printed rows not
status-killed; four Moh degrees occupied), Opus cascade 658/391/247/86/51,
Fable 94.

## 8. FALLACY-v2 / typed block

No exit-price assertion; no `charge_basis` line. No flag/place/series
identification: `A_j` (denominator increment of `δ_j`), `V_j` (multiplicity),
`Q = deg p(π)`, `u_s = d_s − V_s` (top complementary multiplicity), and
campaign `N` (pinned geometric degree) are kept apart. `REPRESENTATIVE` is
not used. Floor ≠ attainment: every kill count is a floor (necessary
conditions or MEASURED candidates). `N ≥ 6` and `[6,16]` are consumed from
the frontier line via `uni_hits`/`mixed_hit`, never re-derived. Prop 6.3
descent is a change of coordinates, not an MP0 merge and not Statement 8.5.
No `sat()`, no ring map, no prime-as-derivative. SECOND-POINT is typed
UNDEFINED rather than filled by cap or analogy.

```text
SUBMISSION   mohsieve-descent-engine-grok46-20260903
MEASURED     EMPTY 658/63 and 1189/14016 exact; PARTITION vacuous (solo 0);
             SECOND-POINT UNDEFINED (L2-swap 0/6); Opus 391/247/86/51 and
             MOH-4 groups 1908 / emptied 10 degrees including 105;
             Fable M2 94/32, +UNI 33/17 with 28 excess, D<=120 groups 179;
             2x2 (77,17; 235,329) — no implication;
             G6 p.207 to the unit; G8 does not empty 64,75,84,99;
             u_s>1 fraction 4012/14016; trio G2=(15,10;γ^4,M2'=4),
             G3=(21,14;γ^2,M2'=8), G1 u_s=2
NOT CLAIMED  that any predicate IS Moh's program; that PARTITION being
             vacuous decides PROGRAM; that WINDOW-FAIL of a descended
             campaign group is a theorem-kill; that the X^4 branch is
             Prop 6.3; any realisation; any D <= C(N)
```

<!-- BODY-END -->
