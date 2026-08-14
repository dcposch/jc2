# TOWER-UNIFORM.md — the uniform td-7 tower theorem

Status: **PROMOTED 2026-08-14 (pending coordinator ledger pass) — all
17 cells of the E5-corrected td-7 book die at the tower tier; machine
gate `UNIFORM (17 cells): THEOREM`, 1559/1559 checks, exit 0. Review
chain: Grok SOUND-WITH-ERRATA (`xmodel/grok-uniform-review.md`) + Sol
CONFIRMED (`xmodel/sol-uniform-review.md`); ALL errata from both folded
into this revision (WIN restated over budget-admissible competing
vertices; the three vacuous/tautological uniform checks replaced with
real assertions; pad vertices included in the max-gap/prefix-delta
loops; depth compared; m=23 recomputed from cellmap; perimeter sentence
extended to charged predecessor strata; E5F rho-condition and
intermediate identity; Lemma TERM named; U_7C terminology). No cell
resisted at any review round.**
Engine: `cases/tower_check.py` — uniform mode runs after the five
certificate suites in the same gate (px2/px5 read-only; exact
`Fraction`; ~4 s). Baselines (promoted): `TOWER-9-15.md`,
`TOWER-10-15.md`, `TOWER-58-87.md`, `TOWER-25-35.md`; reviews of
record: `xmodel/grok-tower-review.md`, `xmodel/sol-tower-review.md`,
`xmodel/sol-tower-rereview.md` (+ final), `xmodel/grok-t10-review.md`,
`xmodel/grok-t58-t25-review.md`, `xmodel/grok-uniform-review.md`,
`xmodel/sol-uniform-review.md`.

## 0. THE THEOREM

> **Theorem (td-7 tower uniformity).** *Every cell of the E5-corrected
> td-7 class-B/C book dies at the tower tier. Precisely: for each of
> the 17 cells of the promoted §11a census (238 raw / 233 deduplicated
> routes), no realization of any filed completion route — over all
> recorded arrivals and their `M_U` classes, all free characteristics,
> all neutral padding, all zero-cost insertions at eligible states, all
> terminals, and rerouting of E5-refuted arrival vertices through their
> legal pads — admits a global Prop 4.2 approximate-root ladder: level
> 1 of every ladder is obstructed by the X/first-charged clash. Class B
> is empty before this tier (§11a). Hence the td-7 off-axis book is
> EMPTY at the tower tier.*

The realization quantifier includes, explicitly (Sol uniform finding 2):
**all budget-feasible charged predecessor strata, including charged
state self-returns and multiplicity partitions** — e.g. the `(21,9)`
`l=3` self-return at `(2/3,3)` (cost 4 over the filed minimum 2) and
the composite insertion + self-return + E5-pad realization are replayed
and killed in the gate (`stress (a)/(b)` checks); they change degrees,
never the clash inputs.

Perimeter (verbatim from the promoted (9,15) discipline): realizations
are the design §2.4/§4.1 families; the trust set is H5a Q-value + E5,
Prop 4.2 (ladder, delta descent, alive dichotomy), Prop 8.1(i)–(v),
Cor 6.1, St 8.3(i) + Not 4.1 (single ladder), St 3.9/3.17(i)/3.11(i),
BOOK R1.0–R2.2/P0–P3, the promoted §11a census as the route perimeter,
and the campaign tower formalization calibrated on the td=6 template.
A beyond-perimeter route (a charged step outside the filed closure or a
budget violation) would be a §11a under-enumeration to flag, never
absorbed. H5a rider (terminology per Sol uniform finding 8): the
verdict covers **the promoted Q+E5 book (17 cells) and its
U_7C-restricted sub-book (exactly `(9,15)` and `(10,15)`, killed by the
promoted certificates whose only case-III edges have equal indices)** —
no proof or hidden use of U_7C enters; U_7C is moot for td-7.

Proof structure: the panel-constant clash (§1) + four lemmas (§2) + a
per-cell witness row for each of the 16 remaining cells (§3, frozen
table = machine-checked) + the four certified instances. Every
arithmetic claim below is a named check in the uniform gate.

## 1. The panel-constant clash (imported, promoted)

For every cell: both poles are the unique td-7 entry (type (2,3),
`(1,1,2) ⊕ (1,2,3)`, `deg p_{f,P1} = 2`, `deg p_{f,P2} = 4`), so level
0 of every ladder is `(k_0,l_0) = (2,3)`, `alpha_1 = 3/2`, with the
pole death gap `5/2` (identical collapses at both poles). Chain 1 is
frozen at `(mu,w,M) = (1,2,1)`; its (H8)-forced synchronization stack
has pole-adjacent gap `gap(X) = (nu_X+1)/(2 nu_X) in (1/2, 3/4]` for
every `nu_X >= 2`. The chain-2 side always carries a first-charged
vertex from the universal menu {(A),(C)} with `i = 2` and simple
reduced factors (the `k | 2` cap, joint cap N3 under insertions). The
level-1 window `(gap(X), 5/2)` contains no realization vertex gap
(Lemma WIN), so the first post-pole death is X, and the universal
`nu_X >= 2` three-case refutation (A: `k_1 = 2 nu_X > 2`; B: the
first-charged gap `< 1/2` cannot precede X; C: non-killing prefixes
with `k_j | 2`, then X-death `l_m` never integral, any prefix length)
plus N1–N4 (insertion closure) kill every ladder. All of this is the
promoted `(9,15)`/probe machinery, cell-independent; the lemmas below
discharge its panel-level premises.

## 2. The lemmas

**Lemma L-A (U-OB1; chain-1 freeze, budget-independent).** *On every
route of every cell, chain 1 is uncharged.* Proof: chain-1's state has
`M = 1` (entry, MP4/P3). St 8.4 forces every arriving multiplicity
`l | M = 1`, so every chain-1 cell is the clean `l = 1` shape
`(nu, n nu + 1)` — whose own `M = gcd(nu, n nu + 1) = gcd(nu, 1) = 1`
(the freeze propagates). R1.3 excludes dirty vertices at `mu = 1`;
vertex-locally the same fact: a charged direction needs
`m d_q < d_p = nu` (P0/L7), impossible since `d_q = n nu + 1 > nu` and
`m >= 1`. So budget residue on slack routes cannot be spent on chain 1.
(Checks: `L-A step 1/2`; the gcd identity and the shape contradiction
on lattices.)

**Lemma AM (U-OB2; absorbing M = 1 and the first-charged menu).** *The
first charged chain-2 step of every class-C realization is (A) =
`(21,15) nu7 -> (2/3,3)` or (C) = `(20,16) nu5 -> (3/4,4)`, both
`lambda = 2`, `i = 4/l = 2`.* Proof: from ENTRY `(3/2,2)`, St 8.4
forces `l | M = 2`. `l = 1` steps are neutral (uncharged, Lemma L-A's
shape argument). The `l = 2` charged menu is exactly {(A),(C)}
(engine-audited = the filed P0 menu). Every other charged first step
(the eps-step and the pure-b family) lands `M = 1`, and `M = 1` is
ABSORBING (St 8.4 gives `l = 1` forever, children `(nu, n nu+1)` keep
`M = 1`); a class-C arrival needs `mu0 | M_U` with `mu0 >= 2` —
unreachable from `M = 1`. (Checks: `AM identity/menu/absorption`.)

**Lemma WIN (U-OB3; window emptiness — restated per both uniform
reviews).** *Every budget-admissible competing vertex other than the
poles and the pole-adjacent chain-1 vertex X has death gap
`<= 2/5 < 1/2 <= gap(X)`; the level-1 window `(gap(X), 5/2)` is
empty.* Proof ingredients, each a named gate check: (i′) **entry**: at
`D = 4`, St 8.4 forces `l | 2`; the charged entry ratios are (C) `8/5`,
(A) `10/7`, eps-`(7,5)` `10/7` — max entry child gap `= 2/5`, attained
only by (C); (i″) **raw-menu bound with the budget qualifier**: the raw
69-state non-resonant ratio supremum is `5/2`, attained only by the
st96 `(14,7) l=5` outlier at `(3/5,5)`, whose `dl = 2` step is
budget-blocked (`dist = 5`); framed budget-admissible non-resonant
steps have ratio `<= 2` (sup at `(10,5) l=4`) — the earlier "sup = 2
over the full closure" sentence was FALSE as a raw menu fact and is
hereby corrected (Grok finding 1 / Sol finding 1); (ii) **growth**:
`deg_child = deg_par d_p/l >= nu deg_par >= 2 deg_par` anchored at 4,
so non-entry parents have `deg >= 8` and deeper children have gap
`<= (5/2)/8 = 5/16 < 1/2`; (iii) **resonant audit (robust form, no
min-deg defaults)**: the resonant-step states are exactly
`{(3,1), (3/5,1), (3/5,5)}`, all non-entry, so their `n = 2` children
are covered by (ii) alone; (iv) parametric families by the identities
`l(nu+1)/(l nu + eps) <= (nu+1)/nu <= 3/2` and N4
(`(nu+1)/(D_prev nu) <= 3/8` at `D_prev >= 4`); (v) terminal side by
**Lemma TERM** below. The framed enumeration maximum `2/5` (witness
(C)) is corroboration from a finite SYMBOLIC SAMPLE (242 path-states;
one characteristic per parametric family, depth/degree cutoffs), not an
exhaustive realization enumeration — the quantifier closure is by
(i′)–(v) (Sol finding 3).

**Lemma TERM (formerly the undefined `L-E` label; Sol finding 4).**
*Terminal choice cannot steal the window: every merge gap
`d_q/(i_G d_p) < 1/2` (largest on the panel: `3/28`, `7/250`,
`3/196`), and every trunk/terminal-side child has gap
`<= (5/2)/deg p_{f,G} < 1/2` since `deg p_{f,G} >= 42` panel-wide and
kappa-rescaling cancels in `kbar/D_f`.* (Gate check `TERM`, all 16
cells.)

**Lemma E5F (U-OB5; the uniform vertex-level E5 offset law).** *A
recorded arrival vertex `(nu_U, kbar_U)` of a cell `(kbar_G, nu_G)` is
E5-realizable iff `n = nu_U kbar_G - nu_G kbar_U >= 1` (printed (h')
positivity; the congruence is automatic). General intermediate identity
(Sol finding 6): `n = nu_U X/mu0 - nu_G rho_U`. Closed forms: on a
charged arrival with `rho_U = 1/mu0` (which requires `mu0 | M_U`, NOT
`M_U = mu0` — `(9,15)`'s `M_U = 4` arrival has `rho_U = 1/2`; Sol
finding 5): `n = (X nu_U - nu_G)/mu0`; on a clean pad
(`rho_U = w_U`, `kbar_U = (nu_U+1) w_U`): `n = ((nu_U+1) X -
mu0 kbar_G)/mu0`, so the MINIMAL pad `nu_U = mu0 - 1` has
`n = X - kbar_G = -2` identically (the kbar=5 pad class), and the
family's `kbar_U = 1` directs `nu_U = (m-1)/2` have `n = -1`
identically (`(7,15), (9,19), (11,23)`). The charged form is now a
real gate lattice (not a placeholder), m=23's pad-only status is
recomputed from the cellmap (sole direct `(11,23)`, `n = -1`), and the
negative controls are live-witness mutations (Grok finding 2).* Consequences, all checked:
the §11a arrival-vertex lists are a state-level superset (the census
prices states — its cell list and 238/233 route counts are untouched);
7 of 16 rollout §2 min-witness rows were contaminated and are corrected
in §3 (`(15,25,12,5)`, `(21,35,17,7)`, `(27,45,22,9)`, `(34,51,25,17)`,
`(42,63,31,21)`, `(58,87,43,29)`, `(90,135,67,45)`); `m = 23` has NO
legal direct arrival (pad `nu = 45`, `n = 2`, is its witness). Refuted
vertices' realization families reroute through legal pads and are
killed with everything else — no kill ever relied on an arrival's
realizability. **Census-audit-class note:** any future consumer of
§11a arrival-vertex columns must apply the `n >= 1` filter; this is a
vertex-realizability refinement, not a census edit.

## 3. The per-cell witness table (frozen; machine-recomputed each run)

For each cell: the minimal E5-legal realization (frame-tracked exact
enumeration of the filed closure, budget 5, with `rho/kbar` replayed
per vertex via BOOK-2.1/R1.2), its clash instantiation (window, caps,
prefix-delta integrality at every witness vertex, universal A/B/C), and
census parity. `P = i_G/2` is the chain-1 stack product ((H8)); `first`
is the first-charged menu cell.

| cell @ mu0 | kbar | X | witness arrival | n | deg p_{f,U} | i_G | P | maxgap | first | refuted min (was) |
|---|---:|---:|---|---:|---:|---:|---:|---|---|---|
| (10,15,7,5)@3 | 6 | 4 | direct nu=7 | 7 | 42 | 14 | 7 | 5/14 | (A) | — |
| (15,25,12,5)@3 | 5 | 3 | pad nu=5 | 1 | 12750 | 4250 | 2125 | 2/5 | (C) | 5100 (pad nu=2, n=−2) |
| (18,27,13,9)@5 | 6 | 4 | direct nu=7 | 3 | 490 | 98 | 49 | 5/14 | (A) | — |
| (21,35,17,7)@4 | 5 | 3 | pad nu=7 | 1 | 214200 | 53550 | 26775 | 2/5 | (C) | 91800 (pad nu=3, n=−2) |
| (25,35,17,5)@8 | 7 | 5 | direct nu=5 | 1 | 400 | 50 | 25 | 2/5 | (C) | — |
| (26,39,19,13)@7 | 6 | 4 | direct nu=17 | 7 | 1190 | 170 | 85 | 2/5 | (C) | — |
| (27,45,22,9)@5 | 5 | 3 | pad nu=9 | 1 | 1598850 | 319770 | 159885 | 2/5 | (C) | 710600 (pad nu=4, n=−2) |
| (34,51,25,17)@9 | 6 | 4 | direct nu=13 | 3 | 11466 | 1274 | 637 | 5/14 | (A) | 7650 (direct, n=−1) |
| (42,63,31,21)@11 | 6 | 4 | direct nu=16 | 3 | 35530 | 3230 | 1615 | 2/5 | (C) | 2750 (direct, n=−1) |
| (50,75,37,25)@13 | 6 | 4 | direct nu=19 | 3 | 41990 | 3230 | 1615 | 2/5 | (C) | — |
| (58,87,43,29)@15 | 6 | 4 | direct nu=37 | 7 | 27750 | 1850 | 925 | 2/5 | (C) | 13650 (direct, n=−1) |
| (66,99,49,33)@17 | 6 | 4 | direct nu=25 | 3 | 541450 | 31850 | 15925 | 5/14 | (A) | — |
| (74,111,55,37)@19 | 6 | 4 | direct nu=47 | 7 | 116090 | 6110 | 3055 | 2/5 | (C) | — |
| (82,123,61,41)@21 | 6 | 4 | direct nu=31 | 3 | 553350 | 26350 | 13175 | 2/5 | (C) | — |
| (90,135,67,45)@23 | 6 | 4 | **pad nu=45 (no legal direct)** | 2 | 36773550 | 1598850 | 799425 | 2/5 | (C) | 817190 (direct, n=−1) |
| (98,147,73,49)@25 | 6 | 4 | direct nu=37 | 3 | 2987750 | 119510 | 59755 | 2/5 | (C) | — |

Every row: `kbar` pin closes both ways (2dq/(dq−dp) = E5 (I4)); N1/P3;
census parity (routes raw/eq match §11a exactly, 16/16); `n >= 1` with
the applicable E5F closed form; `i_G` and `P` integral, `P >= 2` (stack
exists; a non-integral `P` would be spine-death, bookkept separately —
none occurs); `maxgap <= 2/5` (window empty); first-charged in
{(A),(C)} (cap `k | 2`); prefix-menu deltas `D_f g - kbar` positive-
integral at every witness vertex for `g in {3/2, 1, 2}` (Case C
legality). The universal A/B/C + N1–N4 blocks (run five times in the
certificate suites) consume only these premises — so each row is a
complete clash instantiation. The `(9,15)` cell (both completions) and
the three probe cells are the certified instances; rows 1/5/11 above
reproduce their certificate ledgers exactly.

## 4. What the theorem does NOT claim

Formal-tier scope, inherited verbatim from `TOWER-9-15.md`: this is an
obstruction over the filed route perimeter — not a statement about
convergence, P-realizability, global polynomiality, or the existence
question away from the represented charts. Milestone-2 (jet-window
emission) is moot panel-wide unless review overturns a dependency. The
witness rows instantiate parametric families minimally; their quantifier
closure is by the lemmas (WIN/E5F identities + N1–N4), not by
enumeration. Promotion requires hostile review of: the four lemma
proofs (L-A, AM, WIN, E5F), the frozen table, and the theorem's
perimeter sentence.

## 5. Reproduction

```bash
cd /Users/dc/code/math/jc72108
python3 cases/tower_check.py    # ~4 s, exit 0: 5 certificate suites,
                                # 21 perturbations, then UNIFORM mode
                                # (lemmas + 16 witness rows), 1559 checks;
                                # final line: UNIFORM (17 cells): THEOREM
python3 cases/tower_rollout_arith.py   # the prediction table (7 rows
                                       # corrected by SS3; gap/window
                                       # columns were always exact)
```

Uniform-mode structure: Lemma L-A, Lemma AM (menu audit), 69-state
closure + frame-tracked path enumeration (242 path-states — a symbolic
corroboration sample, not exhaustive; quantifier closure is by the
lemmas), Lemma WIN restated (entry `l | 2` ratio `<= 8/5`; raw-menu
`5/2` outlier budget-blocked; framed sup 2; growth; robust 3-state
resonant audit; parametric identities), Lemma TERM (terminal-side
audit, 16 cells), Lemma E5F (real charged lattice, pad/minimal-pad
identities, family `n = -1`, m=23 cellmap recompute), the charged-
stratum stress realizations (self-return `(21,9)`; the composite
insertion + self-return + pad), 16 witness rows against the frozen
table with pad vertices included in max-gap/prefix-delta and chain
depth compared, Sol's three pad-delta triples replayed, the 7-row
erratum count, and live-mutation negative controls. Gate totals:
1559/1559 PASS, exit 0, 21/21 certificate-suite perturbations. No
msolve, no network, no floats; `ops/FLEET.md` respected. No git commit
was made.
