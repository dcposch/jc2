# DESCENT-ANCHOR AUDIT — Grok 4.6 — 2026-09-03

Lane `descent-anchor-audit-grok46-20260903`. Charged: Opus H1/§8/§13 of
`xmodel/ideation-20260903T1200Z-opus5.md` (only 20260903T1200Z file opened).
Frozen inputs `/tmp/jc2-lane.fQcJVU/inputs` SHA-256 9/9 match. Moh 1983
`refs/moh1983_jram340_configurations_of_roots.pdf` (sha256 `6c8847a8…`),
300 dpi; journal N = PDF N−139. Pages: **151, 173–185, 196–199, 202,
207–212**. Citations `SOURCE-READ` or `SOURCE-UNVERIFIED`. No ledger
edits; `jc2-lean` not inspected; no other 1200Z file; no running-lane
report. Drivers: `box/anchor-audit-20260903/`. Desk CAS only.

## 0. Headline

1. **`OPEN[DESCENT-ANCHOR]` closes as outcome (ii).** Def 5.1(3) as
   **printed** at p.179 carries the factor `1/(n−M_s−1)` (transcribed
   below). Prop 6.3/6.4 descent of the *parent* is defined on every
   `u_s=1` census row: its hypotheses are `deg g=deg_y g`, `δ_s=−1`, and
   (when `u_s=1`) the automatic minor-disc bound of Prop 6.4 — none of
   these mention the child's `n'−M'_{s'}−1`. The vanishing denominator
   is a fact about the *child's* characteristic sequence. Moh p.174
   Definition–Remark already names the repair: if `M_h=n−1`, drop it;
   the last *effective* exponent is `M_s`. Apply Φ to the truncated
   data. Negative control: truncation is a no-op on all five p.207
   `u_s=1` rows, so the 10/10 printed rationals still MATCH. Dropping
   the printed factor (instead of dropping `M_h`) still breaks (15,10)
   (`δ_2=−3` not `−1/3`). §1–§3.
2. **Not (i), not (iii) as a kill.** Prop 6.3's hypotheses do not fail
   on the parent of an anchor-zero row. Moh does not send `δ'→−∞`: Prop
   5.1(1) says `δ_h=δ_{h−1}=−1/(n−M_{h−1}−1)`, finite; the two top discs
   coincide. Lemma 2.1 already forces every Jacobian pair to *have*
   `M_h=n−1` in the full sequence. Landing the descent map on that slot
   is the generic termination, not a degeneration of the disc and not a
   kill of the 38. §3.
3. **MEASURED.** Opus's 38/57 and 12/20 reproduce on the frozen
   drivers: `C_FULL_TREE_ODE` is 658→58 at `n≤100` (57 descendable, 38
   anchor-zero, 19 evaluable as charged) and 217→21→20 at `n=108` (19
   descendable, 12 anchor-zero, 7 evaluable as charged). After the p.174
   drop, **0/38** (resp. 0/12) remain undefined. The `u_s>1 ∪
   still-undefined` residue is **1/58** and **1/20** — `(99,66)` and the
   `n=108` analogue `u_s=2` row — not “much larger than 1/58”. p.207
   contains **zero** anchor-degenerate rows. The three Opus-named
   `(84,56)` `d_s=7` rows are census extras, not among Moh's printed
   six. §2, §4.

## 1. Task (a) — Def 5.1(3), Prop 5.3, `M_s=n−2`, the child's top exponent

### 1.1 The displayed formula at p.179 (`SOURCE-READ`)

Definition 5.1(3), p.179, displayed, for `i=r,…,s`:

```text
          (n − M_i)  Π_{j=i+1}^{s} [ V_j (n − M_j) − d_j ]
δ_i = 1 − ─────────────────────────────────────────────────────
          (n − M_s − 1) Π_{j=i+1}^{s} [ V_j (n − M_{j−1}) − d_j ]
```

The factor `1/(n−M_s−1)` is in the print, not a Keller transcription
artefact. The same factor opens the page: the p.179 identity for
`δ_s+(V_s/d_s)(δ_{s−1}−δ_s)` has denominator `(n−M_s−1)[V_s(n−M_{s−1})−d_s]`.
`box/moh_skeleton_full.py` `Skel._delta` matches the display (census-rebase
CONTROL 1). `PROVED-IN-SOURCE`.

Lemma 5.1 p.176 (`SOURCE-READ`), under `L ≤ M_s < n−1` and
`V_s(n−M_s)>d_s`:

```text
δ_s = δ(M_s) = 1 − (n−M_s)/(n−M_s−1) = −1/(n−M_s−1).
```

RADIUS-ORDER (`moh_skeleton_N.py:191–195`):
`λ_g(δ_r)= −n(1−δ_r)(n−M_s−1)/(n−M_r)`. Here `c=n−M_s−1` is the
`x`-degree of `f_{n−1}` in Lemma 2.1 (`deg_x f_{n−1}=1` ⇒ `c=1`); D1-PIN
consumes that specialisation. For `J=c x^k` the same identity runs with
`c=k+1`. Negative control, as charged: replacing `n−M_s−1` by `1` on
`(15,10)`, `M_2=11`, `V_2=3` gives `δ_2=−3` not `−1/3`. `MEASURED`.

### 1.2 Role in Prop 5.3 and Lemma 5.2

Lemma 5.2 p.177 hypothesises `L ≤ M_r < ⋯ < M_s < n−1` and writes `δ(L)`
with the same `(n−M_s−1)` in the denominator. The proof that `−1+δ*<0`
uses `n−M_s > n−M_s−1 > 0` (p.178): if `M_s=n−1` this is false and the
formula is undefined. Prop 5.3 pp.180–183 feeds Lemma 5.2 at `L=M_r` and
`L=M_{r−1}`; the factor is the radius-order conversion that makes
`λ*=(−1+δ*)d_r/(n−L)` strictly negative. Prop 5.3 therefore does **not**
apply to an un-truncated sequence ending at `n−1`. After the p.174 drop,
`M_s<n−1` is restored. Whether the proof also needs `J=const` (beyond
Lemma 2.1) is `OPEN[DESCENDED-TREE-LICENSE]`. `PROVED-IN-SOURCE`.

### 1.3 When Moh asserts `M_s=n−2`

Search (2) p.200: `M_s=n−2`, with (3) “degrees cannot be reduced
simultaneously”. Prop 5.4 p.183: if the smallest disc containing all
roots of `g T_1^ψ` has `δ_i>−1`, then either `k[x,y]=k[f,g]` or an
automorphism reduces degrees. Lemma 5.3 p.185: that disc has radius `−1`
**iff** `M_s=n−2` and the highest form of `g` has two roots, one of
multiplicity `(n/d_s)v_s` with `d_s>v_s>d_s/2`. Necessity: `−1=δ_i=
−1/(n−M_i−1)` forces `M_i=n−2`. So `M_s=n−2` is a statement about a
**minimal Keller counterexample**. The child has `J=cγ^k` with `k≥1` on
every `u_s=1` row here; Lemma 5.3 is not licensed for it, and
`M'_{s'}=n'−2` is not expected. `PROVED-IN-SOURCE`.

### 1.4 Top characteristic exponent of the child

Prop 5.1 p.173–174 (`SOURCE-READ`):

* (1) If `M_h=n−1` then `δ_h=δ_{h−1}=−1/(n−M_{h−1}−1)`, and Prop 4.6
  applies at `r=h−1`, `v=d_{h−1}`.
* (2) If `M_h<n−1` then `δ_h=−1/(n−M_h−1)`, Prop 4.6 at `r=h`.

**Definition–Remark, p.174, displayed:** *“The conclusion (1) implies
that if `M_h=n−1`, then we should drop it from our own consideration.
The ‘effective’ characteristic pairs exclude `M_h` if `M_h=n−1`. The
last effective characteristic pair is denoted by `M_s` in this
article.”*

p.151 after Lemma 2.1: `f_{n−1}≠0` and `(n,n−1)=1` imply `M_i≤n−1`, and
“all `M_i`'s terminate at `n−1` if the Jacobian condition is satisfied.”
`M_h=n−1` is the Jacobian coefficient (x-linear for `k=0`; degree `k+1`
for `J=c x^k`). Every Jacobian pair has it; Moh drops it before writing
`M_s`.

**Five p.207 rows** (all `u_s=1`; `MEASURED`). Child top never `n'−2` or
`n'−1`; dens `2,4,2,3,3`; Prop 5.3 applies to the raw data; Φ defined as
charged.

```text
(64,48) → (16,12) M'=[13]     n'-2=14 n'-1=15
(84,56) M2=64 → (21,14) [16]  n'-2=19 n'-1=20
(84,56) M2=72 → (21,14) [18]  n'-2=19 n'-1=20
(75,50) V2=3  → (15,10) [11]  n'-2=13 n'-1=14
(75,50) V2=2  → (15,10) [11]  n'-2=13 n'-1=14
```

**Opus-named `(84,56)` `d_s=7` ODE-survivors**, after Prop 6.3 and the
p.174 drop. Raw last exponent `11=n'−1` (Jacobian). After drop, Prop 5.3
applies (`6` or `10`, both `<11`). The `[70,77,82]` row has effective
`M_s=n'−2`; Φ then gives `δ_top'=(k+1)(−1)=−5` (`k=4`), not `−1`. Lemma
5.3's “radius `−1` iff `M_s=n−2`” is constant-`J`; for monomial `J` the
geometric radius `−1` is `n−M_s−1=k+1`. `MEASURED` / `DERIVED`.

```text
M=[-56,42,77,82] V={2:1,3:12,4:6} → (12,8) raw=[-8,6,11]  Meff=[-8,6]  ≠ n'-2
M=[-56,42,77,82] V={2:3,3:12,4:6} → (12,8) raw=[-8,6,11]  Meff=[-8,6]  ≠ n'-2
M=[-56,70,77,82] V={2:11,3:10,4:6}→ (12,8) raw=[-8,10,11] Meff=[-8,10] = n'-2
```

## 2. Task (b) — p.207 has no anchor-degenerate row; why `d_s=7` is absent

p.207 table (`SOURCE-READ`) is the Prop 6.4 image of the first three
p.202 classes, licensed by the printed `u_3=d_3−v_3=1`. The five rows
have `n'−M_2'−1 = 2,4,2,3,3`. **Zero anchor-degenerate rows.** Prediction
confirmed. `(99,66)` is excluded because `u_3=3≠1`; Prop 6.4 does not
apply (p.209 treats it by a linear-power / cubic dichotomy, not Prop
6.3). `PROVED-IN-SOURCE`.

p.202 (`SOURCE-READ`) prints, for `(84,56)`:

```text
n=84, m=56, M_2=64 [72], M_3=82, M_4=83, V_3=3, V_2=2 [5]
```

So `s=3`, `M_s=82=n−2`, `M_4=83=n−1` (the Jacobian term, to be dropped
by p.174), `d_3=gcd(84,−56,64,82)=4`, `V_3=3`, `u_3=1`. Two printed data
sets, both `d_s=4`. The campaign's `MOH_TABLE` matches: `[64,82]` with
`V={3:3,2:2}` and `[72,82]` with `V={3:3,2:5}`. `PROVED-IN-SOURCE`.

`(1)–(13)` at `(84,56)`: **46 rows**, two printed, **44 extras**. The
Opus-named `s=4`, `d_s=7` chains `M=[−56,42,77,82]` (three V-assignments,
two with `u_s=1`) and `M=[−56,70,77,82]` (three V-assignments, one with
`u_s=1`) sit among the extras. They are **in the census and not on
p.202** — not a misread of `[64]/[72]` (`M_3=82`, no `M=77`). They are
`OPEN[MOH-PROGRAM]` residue at this class. `MEASURED`.

Appendix II p.208 (`SOURCE-READ`): “Similar arguments can be applied to
the **second case** to show the impossibility directly and to the third
case to reduce the number of coefficients to 22 [15 or 13].” The three
cases of p.207 are `(16,12)`, `(21,14)`, `(15,10)` — i.e. the `d_s=4`
image of `(84,56)`, not a `(12,8)` image of the `d_s=7` extras. p.211
closes `(15,10; M_2=11, V_2=3)` and then: “All other cases can be
computed directly as above.” No `(12,8)` data, no `d_s=7` row, no
`M_3'=11`. Moh did not treat the `d_s=7` rows elsewhere in Appendix II.
`PROVED-IN-SOURCE`.

## 3. Task (c) — the three outcomes

**Verdict: (ii).** Repair Φ by Moh's own p.174 normalisation. The
repaired rule, still hitting 10/10 printed rationals:

> **Φ_eff.** Let `(n',m',M_i',V_i',k)` be the Prop 6.3 image of a
> `u_s=1` row (`n'=n/d_s`, `m'=m/d_s`, `M_i'=M_i/d_s` for `i≤s−1`,
> `V_i'=V_i`, `k=V_s−u_s−1`). If `M'_{s'}=n'−1`, drop that last
> exponent and set `V_{s*+1}=d_{s*+1}` on the truncated dictionaries
> (`s*=s'−1`). Then `δ_i'=(k+1)·`Def 5.1(3) on the effective tuple.

On p.207 the drop is a no-op (`drop=0` on all five), so Φ_eff=Φ and the
10 rationals MATCH. `MEASURED`. Cheapest negative control, as charged,
passes.

**(i) is false.** Prop 6.3 p.197 hypothesises: `g` monic in `y`,
`deg g=deg_y g=n>1`, `δ_s=−1`, and `δ^*_{s−1}≥v_s/u_s`. Prop 6.4 p.198
supplies the last of these when `u_s=1`. Every `(1)–(13)` parent has
`M_s=n−2`, hence `δ_s=−1` (Lemma 5.1). The 38 (resp. 12) rows are
`u_s=1` by construction of the descendable set. No Prop 6.3 hypothesis
fails. What fails, if one refuses the p.174 drop, is Lemma 5.2 /
Def 5.1(3) on the *child*. That is a radii-rule gap, not a descent-map
gap. `OPEN[MINOR-DICHOTOMY]` stays at 1/58, not “much larger”.
`PROVED-IN-SOURCE` / `MEASURED`.

**(iii) is false as a kill.** The naive `δ_s=−1/(n−M_s−1)→−∞` as
`M_s→n−1` applies Lemma 5.1 outside `M_s<n−1`. Prop 5.1(1) is the actual
construction: the `h`-disc and the `(h−1)`-disc **coincide**, radius
`−1/(n−M_{h−1}−1)` (times `k+1` for monomial `J`). The child “reaches
the Jacobian term” because Lemma 2.1 already put `f_{n'−1}≠0` there;
`(n',n'−1)=1` makes `d_{s'}∤n'−1` automatic. Forcing: drop `M_h`, apply
Prop 4.6 at `r=h−1` with `deg q=n'−M_{\mathrm{eff}}≥2` (automatic). No
disc collapses; no row dies. If the descent map writes `M'_{s'}=n'−1`,
that entry is the child's Jacobian termination and must be shed before
Def 5.1(3) or Prop 5.3. `PROVED-IN-SOURCE` / `DERIVED`.

## 4. Task (d) — 38/57 and 12/20, the list, the domain of (T)

Frozen copies of `full_tree_partition.py` + `moh_skeleton_full.py`,
`python3 -O`, desk, < 2 s after import. Descent map as charged:
`n'=n/d_s`, `m'=m/d_s`, `M_i'=M_i/d_s`, `V_i'=V_i`,
`k=V_s−u_s−1`. Anchor-zero: `M_{s−1}=n−d_s`. Screen:
`C_FULL_TREE_ODE` (`ode_nondegenerate=True`).

```text
n≤100  (1)–(13) 658 → ODE 58
         u_s=1 : 57          u_s>1 : 1  = (99,66) V={2:8,3:8} d_s=11
         anchor-zero : 38    evaluable as charged : 19
         after p.174 drop, still den=0 : 0
         Φ_eff defined : 57
n=108  (1)–(13) 217 → partition 21 → ODE 20     [Opus 217→21→20]
         u_s=1 : 19          u_s>1 : 1  = (108,72) M=[−72,81,106] V={2:7,3:7} d_s=9 u_s=2
         anchor-zero : 12    evaluable as charged : 7
         after p.174 drop, still den=0 : 0
         Φ_eff defined : 19
```

Among the 38: parent `s` is 4 (24 rows) or 5 (14 rows, all at `(96,64)`);
after the drop, `s_eff=2` on 24 and `s_eff=3` on 14; `s_eff=1` on **0**;
`top_eff=n'−2` on 11, `<n'−2` on 27. Among the original 19 “evaluable as
charged”, only **5** have `s'=2` (the p.207 shape: parent `s=3`); 13 have
`s'=3` and 1 has `s'=4`. At `n=108` the split inverts: the 7 evaluable-as-charged
all have `s'=3`, and the 12 anchor-zero rows become `s_eff=2` after the drop.

### 4.1 The 38 + 12, with `(n,m,M,V,d_s)`

Child data (`n'`, `M_eff`, `s_eff`, Φ_eff) in
`box/anchor-audit-20260903/anchor_zero_rows.txt`. All 38 have `drop=1`
and `den_eff≠0`. The 14 `s_eff=3` rows are the `(96,64)` parent-`s=5`
block. All 12 at `n=108` have `s_eff=2`.

**`n≤100` (38).**

```text
72,48  M=[-48,60,68,70] V={2:11,3:7,4:3}   ds=4
72,48  M=[-48,60,66,70] V={2:11,3:10,4:5}  ds=6
80,32  M=[-32,56,76,78] V={2:8,3:4,4:3}    ds=4
84,56  M=[-56,42,77,82] V={2:1,3:12,4:6}   ds=7
84,56  M=[-56,42,77,82] V={2:3,3:12,4:6}   ds=7
84,56  M=[-56,70,77,82] V={2:11,3:10,4:6}  ds=7
90,60  M=[-60,10,85,88] V={2:1,3:8,4:4}    ds=5
90,60  M=[-60,10,85,88] V={2:3,3:8,4:4}    ds=5
90,60  M=[-60,70,85,88] V={2:8,3:7,4:4}    ds=5
90,60  M=[-60,80,85,88] V={2:17,3:8,4:4}   ds=5
90,60  M=[-60,75,85,88] V={2:11,3:7,4:4}   ds=5
96,80  M=[-80,24,92,94] V={2:6,3:3,4:3}    ds=4
96,72  M=[-72,56,92,94] V={2:1,3:5,4:3}    ds=4
96,72  M=[-72,56,92,94] V={2:7,3:5,4:3}    ds=4
96,72  M=[-72,88,92,94] V={2:7,3:5,4:3}    ds=4
96,64  M=[-64,24,92,94] V={2:20,3:5,4:3}   ds=4
96,64  M=[-64,72,92,94] V={2:7,3:6,4:3}    ds=4
96,64  M=[-64,80,92,94] V={2:11,3:10,4:3}  ds=4
96,64  M=[-64,48,88,94] V={2:1,3:12,4:7}   ds=8
96,64  M=[-64,48,88,94] V={2:3,3:12,4:7}   ds=8
96,64  M=[-64,80,88,94] V={2:11,3:10,4:7}  ds=8
96,64  M=[-64,-48,24,92,94] V={2:20,3:10,4:5,5:3} ds=4
96,64  M=[-64,-16,24,92,94] V={2:1,3:8,4:4,5:3}   ds=4
96,64  M=[-64,-16,24,92,94] V={2:5,3:8,4:4,5:3}   ds=4
96,64  M=[-64,-16,24,92,94] V={2:20,3:10,4:5,5:3} ds=4
96,64  M=[-64,-16,72,92,94] V={2:1,3:8,4:4,5:3}   ds=4
96,64  M=[-64,-16,72,92,94] V={2:2,3:8,4:4,5:3}   ds=4
96,64  M=[-64,16,24,92,94]  V={2:20,3:10,4:5,5:3} ds=4
96,64  M=[-64,48,72,92,94]  V={2:24,3:12,4:6,5:3} ds=4
96,64  M=[-64,48,88,92,94]  V={2:1,3:12,4:6,5:3}  ds=4
96,64  M=[-64,48,88,92,94]  V={2:3,3:12,4:6,5:3}  ds=4
96,64  M=[-64,48,88,92,94]  V={2:17,3:12,4:6,5:3} ds=4
96,64  M=[-64,80,88,92,94]  V={2:5,3:10,4:5,5:3}  ds=4
96,64  M=[-64,80,88,92,94]  V={2:11,3:10,4:5,5:3} ds=4
96,64  M=[-64,80,88,92,94]  V={2:11,3:7,4:6,5:3}  ds=4
100,40 M=[-40,70,95,98] V={2:8,3:4,4:4}    ds=5
100,80 M=[-80,50,95,98] V={2:1,3:8,4:4}    ds=5
100,80 M=[-80,50,95,98] V={2:3,3:8,4:4}    ds=5
```

**`n=108` (12).** All `(108,72)`, parent `s=4`.

```text
M=[-72,84,104,106] V={2:8,3:7,4:3}   ds=4
M=[-72,84,104,106] V={2:21,3:7,4:3}  ds=4
M=[-72,84,104,106] V={2:8,3:8,4:3}   ds=4
M=[-72,12,102,106] V={2:1,3:8,4:5}   ds=6
M=[-72,12,102,106] V={2:3,3:8,4:5}   ds=6
M=[-72,84,102,106] V={2:8,3:7,4:5}   ds=6
M=[-72,96,102,106] V={2:17,3:8,4:5}  ds=6
M=[-72,90,102,106] V={2:11,3:7,4:5}  ds=6
M=[-72,54,99,106]  V={2:1,3:12,4:8}  ds=9
M=[-72,54,99,106]  V={2:3,3:12,4:8}  ds=9
M=[-72,90,99,106]  V={2:11,3:10,4:8} ds=9
M=[-72,90,99,106]  V={2:17,3:16,4:8} ds=9
```

Opus's “three of Moh's printed six” is a mislabel: the three ODE-surviving
`d_s=7` `(84,56)` rows above are **census extras** at a printed `(n,m)`,
not members of the p.202 six. Zero of the six printed rows are
anchor-zero (the five `u_s=1` printed rows are the p.207 parents, all
`den≠0`; `(99,66)` has `u_s=3`). `MEASURED`.

### 4.2 Domain of theorem (T), restated

Two numbers, because “Φ defined” and “`s'=2` monomial-Jacobian pair”
are not the same predicate (Opus used the first as a proxy for (T)).

| predicate | `n≤100` (of 57 / of 58) | `n=108` (of 19 / of 20) |
|---|---|---|
| Φ as charged (no drop) | **19 / 57** | **7 / 19** (7/20 of ODE) |
| Φ_eff (p.174 drop) | **57 / 57** | **19 / 19** |
| `s_eff=2` after Φ_eff | **29 / 57** (5 of the old 19 + 24 of the 38) | **12 / 19** (the *former* az rows) |
| `u_s>1 ∪ still-undefined` | **1 / 58** | **1 / 20** |

(T) as “evaluate Φ on a descended pair” now covers **all 57 / all 19**
descendable screened rows. (T) as “bounded tower height `s'=2`” covers
29/57 and 12/19 after the repair — and at `n=108` those 12 are exactly
the rows Opus thought were undefined. The 14 `n≤100` rows with
`s_eff=3` (all `(96,64)`, parent `s=5`) still want a second descent;
that is a height question, not an anchor question. `OPEN[MINOR-DICHOTOMY]`
is **not** enlarged. `MEASURED` / `DERIVED`.

Coverage, retroactive, for the promoted `δ'` rule:
`coverage={"defined_on":19,"of_live_rows":57,"undefined_reason":"M_{s-1}=n-d_s","printed_controls_covered":"10/10","after_p174_drop":{"defined_on":57,"of_live_rows":57}}`

## 5. Bounded quantities, OPENs, cheapest tests

* `OPEN[DESCENT-ANCHOR]` **CLOSED** as (ii). Φ charged: 19/57 and 7/19.
  Φ_eff: 57/57 and 19/19. 10/10 preserved. 0 az on p.207. Not a kill.
* `OPEN[MINOR-DICHOTOMY]` untouched, still 1/58 and 1/20. The count *is*
  the cheapest test.
* `OPEN[DESCENDED-TREE-LICENSE]` untouched. Prop 5.3's printed `M_s<n−1`
  holds after the drop; whether the proof uses `J=const` besides Lemma
  2.1 is the existing 45-minute re-read of pp.190–195, p.200. Load-bearing
  only for a *kill* from the composite screen.
* `OPEN[MOH-PROGRAM]` untouched. The `d_s=7` `(84,56)` extras (44 of 46
  `(1)–(13)` rows at that class) are instances of the 652, not a new bound.
* `OPEN[T-HEIGHT]` (new, not this lane). 14 of 57 have `s_eff=3` after one
  descent+drop, all `(96,64)`. Cheapest test: if `u_{s*}=1` on the
  effective child, descend once more (desk, minutes). If that yields
  `s**=2`, (T) as `s'=2` covers 43/57.

## 6. Typed block

```text
LANE     descent-anchor-audit-grok46-20260903 (Grok 4.6)
SOURCE   Moh 1983 300 dpi: pp.151, 173-185, 196-199, 202, 207-212
GATE     hashes 9/9; p.179 display; 10/10 Φ; drop-factor (15,10)=−3≠−1/3
PROVED-IN-SOURCE  Def 5.1(3) has 1/(n−M_s−1).  Lem 5.1: δ_s=−1/(n−M_s−1)
             for M_s<n−1.  Prop 5.1(1)+p.174: if M_h=n−1, DROP it;
             δ_h=δ_{h−1}=−1/(n−M_{h−1}−1).  Prop 6.3 hyps ignore n'−M'−1.
             Search (2)/Lem 5.3/Prop 5.4: M_s=n−2 for a minimal Keller CE.
             p.207 has 0 az rows.  App II “second case” = (21,14) from d_s=4.
DERIVED  Φ_eff=(k+1)·Def 5.1(3) after the p.174 drop.
MEASURED 658→58 ODE n≤100; 57 u_s=1; 38 az; 19 as-charged.  217→21→20
             at n=108; 19 u_s=1; 12 az; 7 as-charged.  After drop: 0 undefined.
             Residue u_s>1 ∪ undef = 1/58, 1/20.  (84,56): 46 (1)–(13), 2 printed.
NOT CLAIMED  kill of the 38; AUDIT 17(p); DESCENDED-TREE-LICENSE; MOH-PROGRAM
TYPED    OPEN[DESCENT-ANCHOR] CLOSED as (ii).  (T) via Φ_eff: 57/57 and 19/19.
             (T) as s_eff=2: 29/57 and 12/19.  MINOR-DICHOTOMY not enlarged.
OPEN CLOSED  OPEN[DESCENT-ANCHOR]
```

## 7. Drivers

```text
box/anchor-audit-20260903/measure_anchor.py      Φ, drop-factor, p.207, (84,56), 38/57, 12/20, Φ_eff
box/anchor-audit-20260903/measure_anchor.json    counts + rows
box/anchor-audit-20260903/anchor_zero_rows.txt   the 38+12 with child data
box/anchor-audit-20260903/phi_delta.py           frozen 10/10 (rerun)
box/anchor-audit-20260903/full_tree_partition.py + repro/moh_skeleton_full.py  frozen
  Page images not kept.  pdftoppm -r 300; journal N = PDF N−139.
```

## 8. FALLACY-v2

No exit price, so no `charge_basis` line. No cv-flag / place / series;
no per-ray charge; no pole identity; `sat()` does not arise.
**Floor/attainment:** 38/57 and 12/20 are exact finite enumerations; Φ_eff
equals the 10 printed rationals (negative control: dropping the printed
factor fails). **Prime label/derivative:** `δ_i'`, `n'`, `M_i'`, `k` are
labels; `f_i'(x)` in Lemma 2.1 is a derivative (p.151). Untruncated
`M_s=n−1` was not used to “correct” p.207; the `d_s=7` `(84,56)` chains
were not used to overwrite printed `[64]/[72]`. Outcome (i) was not
filled by analogy (Prop 6.3 hyps read and checked). Outcome (iii) as
`δ'=−∞` was not filled by a limit outside Lemma 5.1; the source
replacement is Prop 5.1(1).

## COLLISIONS

status: EMPTY

- `OPEN[DESCENT-ANCHOR]` (this report: closed as (ii)): NONE
- `OPEN[MINOR-DICHOTOMY]` (re-priced, not re-typed): NONE

<!-- BODY-END -->
