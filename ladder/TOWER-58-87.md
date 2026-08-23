# TOWER-58-87.md — tower certificate for (58,87,43,29)@mu0=15 (rollout PROBE 2, family representative)

Status: **PROBE 2 EXECUTED (2026-08-14) — spine complete on the E5-legal
witness, tower tier OBSTRUCTED by the identical level-1 clash; NEW
RESULT, pending hostile review. Family layer carried k-SYMBOLICALLY at
the frame tier for all six 2/(2k+1) members; spine specialization forced
(named below). ROLLOUT ERRATUM FILED: the row's min-witness rests on an
E5-refuted arrival.**
Engine: `cases/tower_check.py` (five certificates, 1435 checks incl.
21 perturbation controls, exit 0). Certificate: `cases/towers/t58_87.json`.
Baseline: `TOWER-9-15.md` (promoted), `TOWER-10-15.md` (promoted).

## 1. The wrong-object tripwire FIRED — and what it caught

Rollout-row comparison (mandatory): `kbar = 6`, `X = 4`, arrival
`(2/15; lambda 5; M15)`, `gapmax = 2/5`, window empty, census `1(1)` —
all EXACT against the constructed spine. **DEVIATION: the row's
`min deg p_{f,U} = 13650 (direct nu=7)`, `i_G = 910`, `P_min = 455`.**
The census-listed direct arrival `(7,15)` is the chain vertex
`(105,15,7)` with `kbar_U = 1` (BOOK-2.1: `(20,16) -> (130,40) ->
(105,15)` gives `kbar = (4+9)/13 = 1`), and the vertex-level E5 offset
is

```text
n = nu_U*kbar_G - nu_G*kbar_U = 7*6 - 43*1 = -1 < 1:  E5-REFUTED.
```

The rollout engine's `direct_ok` (and the §11a census itself) checks
state-level legality only — a Risk-4 superset artifact, exactly the
class the rollout's own register predicted. Consequences, all
machine-checked (`e5_refuted_arrivals` / `e5_legal_pads` blocks):

- the `(7,15)`-witness family reroutes through `nu = 14 (mod 15)` pads
  (`kbar_pad = 2(nu+1)/15`): `nu = 14` refuted (`n = -2`), `nu = 29`
  legal (`n = 2`), `nu = 44` legal (`n = 6`);
- the E5-legal MINIMUM realization is the direct `(37,15)` arrival
  `U = (555,75,37)` (`kbar_U = 5`, `n = 7`): `deg p_{f,U} = 27750`,
  `i_G = 1850`, `P = 925`;
- gap/window columns are UNAFFECTED (gaps are `d_q/deg p_f`), and the
  kill never used any arrival's realizability or `P`'s value — the
  filter only SHRINKS the realization family. Probes 1/3 and (9,15)
  pass the same filter (`n = 7, 1, 7`).
- **UT addendum (U-OB5):** every per-cell min-deg/`P_min` scan must add
  the `(h')` `n >= 1` vertex filter; the rollout §2 columns for cells
  with small-`kbar_U` direct arrivals need the same audit.

## 2. The spine (E5-legal witness) — all-green

```text
R0 — G (58,87,43)@15, terminal (4/29,29,psi=1), lambda 5 = 6-psi (exact fit)
     +-- X(925,926) nu=925 — P1          (product 925 = 5^2*37)
     +-- U(555,75,37) — V2(40,16,5) — V1(20,16,5) — P2
```

Frames `(rho,kbar,nu;w,M)`: G `(2/29,6,43;4/29,29)`,
U `(1/15,5,37;2/15,15)`, V2 `(1/8,2,5;3/8,8)`, V1 `(1/4,4,5;3/4,4)`,
X `(2,1852,925;2,1)`; kappas `43, 37, 185, 925, 39775` and poles
`79550/2775`; `K = 238650`. Everything closes (checker C1): E5
`(g')/(h')` with raw `n = 7` (`D_{f,G} = (43*1850 + 7*27750)/37 =
7400`), H5a Q-value `kappa_U = 37`, (H6) `15(6 - 43*(2/15)) = 4`,
(H8) `27750 = 1850*15`, BOOK-2.1 rows `n = 7, 6, 23`, R1.2 `tau = 4,
n = 3699`, R2.1-II `n = 925*6 - 1852 = 3698`, both Prop 4.1 pole
identities (`5/79550`, `5/2775`), derived `N_e/r_f/r_g` on all seven
edges, terminal `j = 29*(25/29) = 25 = 2*mu0 - 5`, `(k_f, l_f) =
(107300, 92500)`. T1 layer (new rows checker-derived at two points):
G: `B = A/2, C = -43A^2/6` (the family G-shape); U `(555,75,37)`:
`B = (3/2)A, C = 111A^2/10`; V2 `(40,16,5)`: `R = t^2-3At+3A^2`,
`C = -15A^3/2` (the (9,15)-F1 quadratic recurs); V1 = the (C) menu
cell; X neutral.

## 3. The kill and the k-symbolic family layer

Death gaps: `X: 463/925 > 1/2`; `V1: 2/5, V2: 1/25, U: 1/370,
G: 3/3700` — window `(gap(X), 5/2)` empty. Universal `nu_X >= 2`
three-case exhaustion + N1–N4 insertion closure at the six eligible
states (`(3/2,2)` caps, `(3/4,4)`, `(3/8,8)`, `(2/15,15)` incl. the
refuted-family's legal pads, chain-1, `(4/29,29)`); menu variants
{(C) displayed, (A) rerouted} with the gap set LOCKED to
`first_charged_gaps` (grok-t10 suggestion 2); P2-anchored `(6,4)`
insertion example replayed (`i`-chain `2/6/30/150`, `i_G 1850 -> 5550`).
**VERDICT (pending review): the cell's single filed route (1 raw/1 eq,
exact fit) is TOWER-DEAD over its full realization family.**

**k-symbolic:** the `family` block carries `m = mu0` symbolically:
cell `(4m-2, 6m-3, 3m-2, 2m-1)@m`, and the identities `kbar = 6`
(`(6m-6)/(m-1) = 6`), `X = 4` (`6m - (6m-4)`), `M_G = 2m-1`,
`w_G = 4/(2m-1)`, `j = 2m-5`, `psi = 1`, budget 5, N1
`gcd(6, 3m-2) = 1`, P3 `6m-4 = 2(3m-2)` — verified for all six members
{15,17,19,21,23,25} AND on the general odd-m lattice. **Specialization
was forced at exactly two steps** (recorded in `family.scope`): (i) the
chain-2 witness selection — the census direct/neutral menus are
member-specific data (`(7,15)/(37,15)`, `(25,17)`, `(9,19)/(47,19)`,
`(31,21)`, `(11,23)`, `(37,25)`), not functions of m; (ii) the
vertex-level E5 arrival filter (`kbar_U` is per-vertex census data).
So this certificate is the family kill at the frame+exhaustion tier;
completing all six members needs one mechanical witness row + arrival
filter table per member (U-OB5/6) — no new mechanism.

## 4. Reproduction

```bash
python3 cases/tower_check.py           # 5 certificates, exit 0
python3 cases/tower_rollout_arith.py   # the row (erratum: see SS1)
```

Perturbation controls: refuted-arrival claimed legal; even family
member injected (N1 trips). No git commit. "Untouched" = not
machine-checked.
