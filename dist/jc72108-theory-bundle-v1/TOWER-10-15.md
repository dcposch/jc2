# TOWER-10-15.md — tower certificate for (10,15,7,5)@mu0=3 (rollout PROBE 1)

Status: **PROBE 1 EXECUTED (2026-08-14) — spine complete, rollout
arithmetic verified EXACTLY against the constructed spine (no
wrong-object alarm), tower tier OBSTRUCTED by the identical level-1
clash; NEW RESULT, pending hostile review. Consequence if promoted: the
forced-nu 2-cell sub-book {(9,15),(10,15)} is EMPTY at the tower tier
in BOTH coherent H5a readings — CONJECTURE U_7C becomes moot for td-7.**
Engine: `cases/tower_check.py` (parameterized, not forked; 937 checks
over three certificates incl. a 17-case perturbation self-test, exit 0).
Certificate: `cases/towers/t10_15.json`. Task source: `TOWER-ROLLOUT.md`
§3 Probe 1; baseline mechanism `TOWER-9-15.md` (promoted).

## 0. Trust perimeter

Everything from `TOWER-9-15.md` §0 (H5a Q-value + E5; Prop 4.2/8.1/
Cor 6.1; St 8.3(i) + Not 4.1 + Cor 6.1 single ladder; St 3.9/3.17(i)/
3.11(i); BOOK R1.2/R2.1/P1; td=6 calibration; N1–N4), plus:

| new input | role | status |
|---|---|---|
| `TOWER-ROLLOUT.md` §1 (G1–G6) | panel decomposition: level 0, gap(X), first-charged menu, window audit, universal exhaustion, terminal-independence | PLANNING ARTIFACT — its predictions are *verified* here, not consumed |
| `cases/tower_rollout_arith.py` | the per-cell arithmetic row | census parity PASS; row cross-checked against this spine EXACTLY (§2) |
| §11a row `(10,15,7,5)@3` | arrival `2/3 (2; M3)`, direct `(4,3),(7,3)` [rec. nu=7], neutral `nu=2(3)`, 47(29) routes | PROMOTED; G4 positive control **in both readings** |
| design §2.1 row 2 | certified local solution `s = t − A/2`, `C = −7A²/6` | PROMOTED (sol-td7-law) |
| design §2.3 | the 47-endpoint terminal table (1 + 28 + 5 + 13) | filed census data |
| L-A (l=1 shape contradiction) | chain-1 uncharged on the 18 slack routes regardless of budget residue | machine-checked lattice here; rollout candidate lemma — a reviewer should attack it |

Reading-independence rider: on the displayed realization `nu_U = nu_G
= 7`, so every case-III transport is identical under the Q-value and
the forced-nu readings — this cell's kill does not consume H5a.

## 1. The spine (displayed realization) and the rollout match

The §11a recorded arrival is DIRECT: the stored step-cell
`st96 l2e0k1S1x0nu7 = (21,15)`, i.e. the chain-2 has **depth 1** — its
single charged vertex U is simultaneously the first-charged menu cell
(A), the arrival vertex, and the P2-adjacent vertex. Tree:

```text
R0
|
G  (10,15,7)@mu0=3, terminal case IV (4/5,5,psi=4), budget 2 = lambda
+-- X  -- P1        (chain-1 stack rep: (7,8) nu=7, product 7)
+-- U  -- P2        (U = (21,15,7), lambda = 2)
```

| v | kappa | pi | kbar | nu | rho | w | M | (d_p,d_q) | i | deg p_f | D_f | gap |
|---|---:|---|---:|---:|---|---|---:|---|---:|---:|---:|---|
| R0 | 1 | 0 | 1 | 1 | 1/5 | — | — | root | — | 140 | 28 | — |
| G | 7 | 1/7 | 6 | 7 | 2/5 | 4/5 | 5 | (10,15) | 14 | 140 | 56 | 3/28 |
| U | 7 | 2/7 | 5 | 7 | 1/3 | 2/3 | 3 | (21,15) | 2 | 42 | 14 | **5/14** |
| X | 49 | 33/49 | 16 | 7 | 2 | 2 | 1 | (7,8) | 2 | 14 | 28 | **4/7** |
| P1 | 98 | 93/98 | 5 | 2 | 1 | 2 | 1 | pole (2,3) | — | 2 | 2 | 5/2 |
| P2 | 21 | 16/21 | 5 | 3 | 1/2 | 3/2 | 2 | pole (4,6) | — | 4 | 2 | 5/2 |

All checker C1 families close: E5 `(g')/(h')` with raw `n = 7`
(`kbar_G = (7·5+7)/7 = 6`, `D_{f,G} = 14 + 42 = 56`), H5a Q-value
`kappa_U = 7`, (H6) `X_G = 3(6 − 14/3) = 4`, (H8) **twice on U**
(`deg p_{f,U} = i_G·mu0 = 14·3 = 42` and `deg p_{f,P2} = i_U·2 = 4` —
the depth-1 novelty), R1.2 on X→P1 (`tau = 4`, `n = 27`), R2.1-II on
G→X (`n = 7·6 − 16 = 26`), BOOK(2.1) on U→P2 (`n = 10`,
`(1/2+10)/15 = 21/30`), both Prop 4.1 pole identities (`5/98`, `5/21`),
Cor 6.1 q-law at all non-poles, `K = 294` with derived
`N_e/r_f/r_g` on every edge, and the case-IV terminal package
(`j = 5·(1/5) = 1`, `R_term = 5`, `psi = 4`, `k_f = 140`, `l_f = 28`).
T1 layer: G's certified row (`B = A/2`, `C = −7A²/6`), U's menu-cell
row (forced `B = (3/2)A`, `C = 21A²/10`, re-derived by exact
eta-calculus at two points), X's neutral row (`8C + 7A = 0`).

**Rollout-row match (wrong-object tripwire — passed).** Every number of
the `tower_rollout_arith.py` row equals the constructed spine value:
`kbar = 6`, `X = 4`, arrival `(2/3; lambda 2; M3)`, first-step menu
`{(21,15) nu7, (20,16) nu5}`, `min deg p_{f,U} = 42` (witness = this
spine's U), `i_G = 14`, `P_min = 7`, `gapmax = 2/5`, window empty,
census `47(29)` parity. No deviation; no alarm.

## 2. The kill (identical level-1 clash)

Death gaps: `gap(X) = 4/7 > 1/2`; `gap(U) = 5/14`, `gap(G) = 3/28`,
both `< 2/5 < 1/2`; poles at `5/2`. The window `(gap(X), 5/2)` contains
no vertex gap. The universal `nu_X >= 2` three-case exhaustion applies
verbatim (the checker's UNIVERSAL blocks are shared, not re-derived):

- **Case A**: `(k_1,l_1) = (2 nu_X, 2 nu_X + 1)`, `k_1 > 2`, refused by
  the `k | 2` cap — at U the cap carrier is the simple factor
  `(t − B_u)` of `p_{f,U} = S[(t−A)²(t−B)]²` (exponent `2 = i_U`, or
  `2 P_pre` under pre-U insertions, joint cap N3 with the P2-adjacent
  exponent 4).
- **Case B**: the first-charged vertex cannot die first, for **both**
  menu gaps: `(nu+1)/(2nu) = 5/14` and `= 2/5` have no `nu >= 2`, and
  the fc-pairs `(7,6)` / `(10,9)` have nonintegral X-exponents
  `12/7` / `9/5`.
- **Case C**: prefix menu `{(1,2),(2,3),(2,5)}` (delta-integral at
  G, U, X: e.g. (A)-column `16, 9, 23` — the rollout's G3 row), then
  the r-parity closed forms kill X-death at any prefix length.

Variants and families (C3-V menu-style + C3-N): single `M_U` class 3
(realized by U, `M = gcd(21,15) = 3`); the (C) = `(20,16)` first-charged
alternative verified (gap `2/5`, `n = 7`, Sol-row deltas `11, 6, 16`)
with the arrival-superset rider for its deeper arrival vertices
(rollout Risk 4: covered parametrically by the `gapmax = 2/5` audit +
universal exhaustion, never relied on for realizability); the neutral
arrival family `nu = 2 (mod 3)` and all zero-cost insertions closed by
N1–N4 at the eligible states `(3/2,2)` [pre-U, odd nu, feeds N3],
`(2/3,3)` [post-U padding, `Dprev >= 42`], `(2,1)` [= the X-family],
`(4/5,5)` [terminal side, `Dprev >= 140`]; the P2-anchored `(6,4)`
insertion example replayed on this cell (`i_U: 2 -> 6`, `gap(U): 5/14
-> 5/42`, `i_G: 14 -> 42`, product `7 -> 21`, continuation row
`(3/2+9)/15 = 21/30` with `kbar_U = 5` preserved). The U→P2 dead-member
handoff `mult(eta(t−A)³(t−B)², c) = 3 = deg p_{h1,P2}` is computed
exactly at two points.

**Terminals: all 47 filed endpoints.** The certificate carries the full
§2.3 endpoint table (1 direct eq `(4/5,5,4)` + 28 eq trunk `psi = 1` +
5 slack trunk-1 + 13 slack trunk-2 = 47 raw / 29 eq — the census
counts); each row's `j in N*`, psi formula, and budget class are
checked. Terminal-independence is the promoted G6/L-E schema: the clash
lives on the pole-to-merge subtree; trunk gaps sit below the window by
searrow growth. The 18 slack routes leave budget residue; chain-1
stays uncharged by **L-A** (an `l = 1` cell `(nu, n·nu+1)` admits no
charged direction: `m·d_q < d_p = nu` is impossible for `m >= 1` —
machine-checked lattice; this is the rollout's candidate lemma and the
right review target for this cell).

**VERDICT (pending review): `(10,15,7,5)@3` is TOWER-DEAD** — every
realization of every filed §11a completion route (47 raw / 29 eq, the
single M3 arrival class, direct + neutral families, free
characteristics, padding, insertions, all terminals).

## 3. Consequence: the forced-nu sub-book closes; U_7C is moot for td-7

§11a records two books: the promoted Q-value book (17 cells) and the
forced-nu book, which is **exactly** `{(9,15,7,3)@2, (10,15,7,5)@3}`
(BOOK-OFFAXIS §11a: "the book is then EXACTLY 2 cells"). The (9,15)
cell kill is promoted; this probe kills (10,15). On the displayed
realization `nu_U = nu_G`, so the kill is valid under either coherent
H5a reading. Hence, once this certificate survives review: **both
members of the forced-nu book are tower-dead, the sub-book is EMPTY at
the tower tier reading-independently, and CONJECTURE U_7C no longer
gates any td-7 conclusion at this tier** — the H5a conditionality
collapses from "two books differ" to "both books die." (The other 15
Q-value cells remain ARITH-DEAD-PREDICTED only.)

## 4. What the uniform theorem still needs (post-probe report)

Probe 1 exercised: depth-1 chains (U = first-charged = arrival =
P2-adjacent — the (H8)-on-one-vertex configuration is now stated and
machine-checked), direct stored-step-cell arrivals (arrival-law clause
split), menu-style C3-V variants, the widest terminal family (47
endpoints, all four psi values), and L-A under real slack. Remaining
for UT (rollout §1.5): **U-OB1** hostile review of L-A itself;
**U-OB2** the absorbing-M lemma pinning the first-charged menu to
{(A),(C)} (cited from P0 here, not proved); **U-OB3** the parametric
closure-wide window lemma (this probe consumed the engine audit +
per-cert bounds); **U-OB5/6** per-cell mechanical tables for the
remaining 15 (this checker is now table-driven — a new cell needs only
its JSON); **U-OB7** per-terminal instantiation is demonstrated at
width 47. Probe 2 (family representative, parametric in mu0) is the
natural next round.

## 5. Reproduction

```bash
cd /Users/dc/code/math/jc72108
python3 cases/tower_check.py           # < 2 s, exit 0, 937 checks,
                                       # 3 certificates + 17 perturbations
python3 cases/tower_rollout_arith.py   # the arithmetic row this spine verifies
```

New perturbation controls for this cell: U-cell `B = (2/3)A` (wrong
forced ratio), slack-endpoint psi tamper, dropped (C)-menu variant with
its case-B gap. Files: `cases/towers/t10_15.json` (certificate),
`cases/tower_check.py` (parameterized checker, three certificates),
this document. No git commit was made. "Untouched" for the other 15
cells still means only "not machine-checked."
