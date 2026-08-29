# Two-pole case III under promoted Q+E5: fibre-finiteness and T1-law repair (R3)

Producer: Fable 5, acting as primary repairer of my own R2 packet
(`xmodel/m2-caseiii-two-pole-e5-local-index-repair-fable5-20260829.md`,
body `01deb67e…a1e8`) after the Opus 5 hostile review
(`xmodel/m2-caseiii-two-pole-e5-local-index-r2-hostile-review-opus5-20260829.md`,
verdict REPAIR_REQUIRED, body `c12bbca2…7b4c`). Date: 2026-08-29 UTC.
Lifecycle: `SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`. This report
authorizes **no canonical engine change and no AWS/fleet action**;
`NUCAP=500` stays. R1, R2 and their packets are byte-untouched; the
fresh packet is `cases/m2_caseiii_two_pole_e5_local_index_r3_20260829/`.

Sources: the R2 report and packet plus the R2 review in full; and the
exact canonical sources those cite — `xmodel/sol-h5a.md` +
`xmodel/grok-h5a-review.md` (promoted H5a resolution),
`ladder/BOOK-OFFAXIS.md` §§6–11a (laws; §11 zero-chain law; §11a
17-cell book, arrivals, N1 kills, family termination),
`ladder/SHEET6-DEPTH.md` §2 (DS1(c) `kbar in Z`) and §§5c–5d (`nu_G=1`
is case I), `ladder/SHEET6-MULTIPOLE.md` (MP1–MP3),
`cases/book_offaxis.py` (`cell_check:219-265`, `solve_arr:273-357`,
`NUCAP:165`, `TDMAX:39`, census `m <= td//3` at `:49-54`; imported
READ-ONLY by the test battery for the `cell_check` cross-check),
`cases/td7_census_e5.py` (`DEAD56`, `nu_legal`, `e5_cells_C`). No web,
no CAS, no `jc2-lean` access, no workspace-wide git, no commit/push.

## 0. What R2 got wrong, and what survives

The review independently confirmed the whole theorem layer — Lemma A,
Theorem B, Theorem C, both equality characterisations, the 12-of-17
attainment, the no-incoming-bound proposition, and the two-directional
Opus adjudication — with zero counterexamples in 2.1M pattern cells and
29.5M handshake samples (its F4). R3 does not re-derive that layer; it
is preserved verbatim (§2) and re-verified by the packet's unchanged
battery. Two claims were blocked and are repaired here:

1. **R2 §7.4 ("the pattern fibre over a fixed `(kbar, nu_G)` can be
   infinite") is FALSE.** Its named members beyond `s = 3` violate the
   strict (NE) law R2 itself lists in H4 — at those parameters
   `dp = 2*dq` identically, so (NE) forces every non-chain multiplicity
   `m_j = 1`, hence `Sm = k <= s`, while the family needs
   `Sm = 2s-3 > s` for `s >= 4`. R2's fixture path applied the derived
   proxy `m_j <= mu-1` instead of the true cap and sealed three
   non-cells (`(38,19)`, `(62,31)`, `(134,67)`) plus an inline `s = 45`
   member into the certificate. R3 withdraws the claim, deletes every
   illegal example from every fixture and manifest, and proves the
   opposite as **Theorem D** (§3): the fibre is *always finite*, with a
   sharp closed-form bound, a complete cap-free census, and the exact
   §7.4 fibre `{(20,10), (26,13)}`.
2. **R2 §8.3's engine-migration T1 gate (`dp | dq <=> kbar in {3,4}`)
   is the `w = 2` specialisation** of BOOK-OFFAXIS §11's zero-chain law
   (whose `w`-free printed leg is `M = d_p`), and R2's own reference
   solver raised `ValueError` on legal `w = 1` and `w = 3` input. R3
   states and proves **Lemma T1′** (§5): at the `mu = 1` pinned solve,
   `dp | dq <=> M = dp <=> w/(kbar - w) in Z>=1`, with the integer
   normalization `kbar in {w + d : d | w}`; the solver is now total on
   every legal `w` and the closed form is a theorem gate, not a crash.

Also repaired: the six §7.1 countercells are explicitly marked
`D = 1, M = 1` / MP2-dead, with the arity-graded scope theorems E and F
(§4); the `nu_U = 13` gloss (§6.1); the `(4m-2, 6m-3)` family
qualifiers (§6.2); and the migration plan's regime numbering, site
language, gate set and `w != 2` hole (§8). One review artifact did
**not** replicate and is documented rather than incorporated (§3.4).

## 1. Setting and scope (unchanged from R2, review-confirmed)

All frames i-normalized (DEPTH §1). A two-pole case-III merge is an
interior merge with (H1) exactly one nonzero arriving pole-chain edge,
state `(mu, w)`, `mu >= 1`, `w > 0`; (H2) a pole-chain 0-arrival of
multiplicity `mu0`, state `(w_U, M_U)`, with `eps = mu0` and
`nu_G >= 2` (a `nu_G = 1` merge is case I, DEPTH §5c); (H3) no
inner-merge arrivals; (H4) the promoted pattern laws — R1.0 q-shape,
R2.2 census `dp = mu0 + nu*(mu + Sm)`, `dq = 1 + nu*(1 + s)` with
`nu = nu_G`, `s = k + lex`; (S) `mu*dq > dp`, `mu0*dq > dp`; strict
(NE) `m_j*dq < dp`; (R) `dp != mu_star*dq`. Write `delta = mu0 - mu`,
`D = mu*dq - dp >= 1`, `A = mu*s - Sm`, `M = gcd(dp, dq)`. `kbar in Z`
whenever `nu_G >= 2` (DS1(c), DEPTH §2:116).

## 2. Preserved theorem layer (verbatim from R2; review F4 charges 1–5)

* **Lemma A** (reading-independent): `D = nu*A - delta`, `A >= s >= 1`,
  `dq/D <= 2*delta + 3`, `kbar = mu*w*dq/D <= mu*w*(2*delta + 3)`;
  equality iff `nu = delta+1, s = 1, A = 1`, forcing `D = M = 1` —
  every sharpness witness MP2-dead.
* **Theorem B** (M-graded): `dq/D <= 2 + (2*delta+1)/M`; equality iff
  `M | 2*delta+1` (M odd) on the `s = A = 1`, `nu = delta+M` cell (then
  `D = M`); attained on exactly the 12 promoted `kbar = 6` rows.
* **Theorem C** (Q+E5): `mu0*nu_G*w_U = delta*kbar + mu*w`; per-state
  `nu_G` menus in the REVERSE (`mu0 < mu`: strict `nu_G < w/w_U`),
  EQUAL (`mu0 = mu`: `nu_G = w/w_U` forced), and DIFFICULT (`mu0 > mu`:
  one `nu_G` per `kbar` in the finite integer menu) regimes; the
  incoming `nu_U` cancels into `w_U` and is free — no incoming bound
  exists, follows, or is required. (Regimes are now *named*; R2's §4/§8
  numbering clash, review F5.3, is thereby dead.)

The 17-cell §11a book battery, the charged td-7 slice under both pins,
the equal-join counterfixture, and the corrected two-directional Opus
adjudication all carry over unchanged and re-verify in the packet.

## 3. Theorem D: the pattern fibre is always finite (replaces §7.4)

**Theorem D.** Fix a two-pole state `(mu, w, mu0)` with `delta >= 1`
and a menu entry `(kbar, nu_G)`, `nu = nu_G >= 2`. Every fibre cell
shares `r = dq/D = kbar/(mu*w)`; put `u = mu - 1/r`, which is `> 0`
(`kbar - w = w*dp/D > 0`). Then:

1. each member is pinned by its `s`: `dq = 1 + nu*(1+s)`, `D = dq/r`,
   `dp = mu*dq - D`, `A = dq/(r*nu) + delta/nu`, `Sm = mu*s - A`;
2. strict (NE) forces `m_j < u`, i.e. `m_j <= m_max = ceil(u) - 1`; and

       s * (1 + u - ceil(u))  <=  (1+nu)/(r*nu) + delta/nu,

   whose left factor lies in `(0, 1]`, so `s` — hence the fibre — is
   **finite**;
3. the bound is **sharp**: it is attained with exact equality in the
   census below (29,444 of the 90,957 keys, largest attained member
   `s = 1202`);
4. at `mu = 1` the map `s -> dq/D = (1+nu+nu*s)/(nu*s - delta)` is
   strictly decreasing, so every `mu = 1` fibre is a **singleton**.

*Proof.* (1) is the handshake `kbar = mu*w*dq/D` plus the census
identities. (2): `m_j*dq < dp = mu*dq - D` iff `m_j < mu - D/dq =
mu - 1/r = u`. With `k <= s` and `m_j <= m_max`:
`A = mu*s - Sm >= s*(mu - m_max)`, and `mu - m_max = mu - ceil(u) + 1
= (1 + u - ceil(u)) + 1/r`. Meanwhile `dq = r*D = r*(nu*A - delta)`
inverts to `A = s/r + (1+nu)/(r*nu) + delta/nu`; subtracting `s/r`
from both sides of `s*(1 + u - ceil(u)) + s/r <= A` gives the display.
(4): the derivative sign of `(1+nu+nu*s)/(nu*s-delta)` is that of
`nu*(nu*s-delta) - nu*(1+nu+nu*s) = -nu*(delta+1+nu) < 0`. ∎

**3.1 The §7.4 fibre, exactly.** At `(mu,w,mu0) = (4,1,5)`,
`kbar = 2`, `nu_G = 3`: `r = 1/2`, `u = 2`, slack `= 1`, bound
`s <= (1+3)/(3/2)/1 + 1/3 = 3`. The complete fibre is
`{(20,10) [s=2], (26,13) [s=3]}`, each re-certified through
`gap_pattern_certificate` with an explicit witness pattern. R2's
members `(32,16) [s=4]`, `(38,19) [s=5]`, `(62,31) [s=9]`,
`(134,67) [s=21]` and the test's inline `s = 45` member are refuted
**pattern-by-pattern**: the packet enumerates every candidate
`(k, mults, lex)` with `k + lex = s`, `sum(mults) = 2s-3`, mults in
`[1,3]` (4, 6, 15, 57, 213 candidates respectively) and every one dies
at the strict-(NE) gate — `legal_patterns = 0` for all five.

**3.2 The canonical engine agrees.** The test battery imports
`book_offaxis` read-only and replays the review's F1(b) table exactly:
`cell_check(2, 4, [4], 5, gcd(dp,dq))` returns True for `s = 2, 3` and
False for `s = 4..9, 21, 45` (and `NUCAP == 500` is asserted
untouched).

**3.3 Census replay (review F1c figures — EXACT match).** Box
`mu <= 7, delta <= 8, nu <= 30, k <= 5, lex <= 8`, cells legal under
(S)+(NE)+(R): 93,735 legal cells fall into **92,772** distinct
`(mu, mu0, nu_G, dq/D)` fibres with size histogram
`{1: 92083, 2: 486, 3: 136, 4: 63, 5: 4}` and **zero** violations of
the Theorem D bound — all three published figures reproduce exactly.
All 1,815 `mu = 1` fibres are singletons (part 4).

**3.4 Complete census (supersedes the review's capped deep search) and
one non-replication.** The review's targeted deep search ("57,960
fibres … largest fibre 9 … terminates at `s = 27`", F1c) is
underspecified, and its figures did **not** replicate under any tested
reading: keys-from-the-box with `mu >= 2, r < 1` gives 75,808 keys
(max size 12 when extended); seeding from the review's F4 sweep box
gives 132,525 (max 14); extending with the box's `k <= 5` cap gives
max 5. Those figures are therefore *not incorporated*. Instead the
packet runs the stronger, exactly-specified census: every `mu >= 2` box
key (90,957; `r < 1` forces `mu >= 2` automatically since `r > 1` at
`mu = 1`), each fibre enumerated **completely** up to its proved
Theorem D bound — no cap anywhere. Results (sealed): largest complete
fibre **12** members at `(mu,mu0,nu,r) = (7,15,2,15/74)`; largest
member `s = 1202` at `(7,15,13,170/1019)`, where the bound holds with
exact equality (`1202 = ((1+13)*1019/170 + 8)/13 * 170` — the
sharpness witness of part 3); size histogram
`{1:79267, 2:5261, 3:2462, 4:1461, 5:950, 6:642, 7:481, 8:251, 9:144,
10:25, 11:8, 12:5}`.

**3.5 Consequence for the migration plan.** R2 §8.3's stated reason for
keeping `cell_check` ("the §7.4 fibre caveat forbids cell enumeration
at `mu >= 2`") is dead. The honest statement: `cell_check` is retained
as a **conservative** existence gate; Theorem D additionally makes the
finite per-entry cell book available (`fibre_solve`) but nothing
requires it. Theorem C's finiteness product is strengthened: finite
priced state closure × finite `kbar` menu × **finite pattern fibre**.

## 4. Theorems E and F: arity-graded scope of the countercells (F3)

The six §7.1 countercells all have `D = 1`, hence `M = 1`: they are
**MP2-dead as interior merges** — the same property R2 disclosed for
Lemma A's sharpness witnesses and omitted here. They remain genuine
engine-tier countercells (M_G = 1 rows reach `solve_arr`: `expand2`
yields every divisor as `MG`, no MP2 filter on that path, and MP3
exempts strict ancestors of `G*`), but the phenomenon is now exactly
graded:

**Theorem E (arity-graded bound).** At an interior merge with
`r0 >= 1` nonzero pole-chain arrivals (multiplicities `mu_1..mu_r0`,
`mu = max`, (S) on every edge), a 0-arrival `mu0 = mu + delta`,
`delta >= 1`, strict (NE), (R):

    dq/D <= (r0 + 1) + ((r0 + 1)*delta + 1)/M .

Equality forces `A' = 1`, `sigma = 1`, `nu_G = delta + M`, `D = M`,
and `M | (r0+1)*delta + 1` (necessity; machine-checked on every
equality hit). `r0 = 1` is Theorem B; at `r0 = 2, M = 1` the bound is
`3*delta + 4`, attained by all six §7.1 cells.

*Proof.* `dq = 1 + nu*(1 + t)`, `t = r0 - 1 + sigma`,
`sigma = k + lex`; `D = nu*A' - delta` with
`A' = mu*(1+t) - sum(mu_i) - Sm in Z`. Since `mu` is the max and
`m_j <= min(mu_i) - 1` (NE + (S) on the minimal edge),
`A' >= mu*sigma - Sm >= sigma`, and `A' >= 1` because
`nu*A' = D + delta >= 2`. Hence
`dq = 1 + nu*r0 + nu*sigma <= 1 + (r0+1)*y`, `y = nu*A' = D + delta`,
and `dq/D <= (1 + (r0+1)*(D+delta))/D <= (r0+1) + ((r0+1)*delta+1)/M`
using `M | D`. Equality traces back through
`r0 + sigma = (r0+1)*A'` which forces `A' = 1, sigma = 1` (else the
left side is `< (r0+1)*A'`), then `nu = y = delta + M`, `D = M`, and
`M | dq = 1 + (r0+1)*(delta+M)` iff `M | (r0+1)*delta + 1`. ∎

**Theorem F (no MP2-alive violator at `r0 <= 3`).** Every legal
`r0 in {2,3}` cell with `dq/D > 2*delta + 3` has `M = 1`. The
statement is **false at `r0 = 4`**: the cell `(44,46)` (four `mu = 1`
arrivals, `mu0 = 8`, `nu = 9`, `k = 0`, `lex = 1`) has `D = M = 2` and
`dq/D = 23 > 17 = 2*delta+3`, attaining the `r0 = 4` graded bound with
equality (`5 + 36/2 = 23`).

*Proof.* `r0 = 2`: a violator needs `3 + (3*delta+1)/M > 2*delta+3`,
i.e. `M < (3*delta+1)/(2*delta) <= 2`, so `M = 1`. `r0 = 3`: suppose
`M >= 2`. From `dq <= 1 + 4y`: `D*(2*delta-1) < 4*delta+1`, so
`D < (4*delta+1)/(2*delta-1)` while `D >= M >= 2`.
*Case `delta >= 2`*: the bound gives `D = 2 = M`; `nu | y = delta+2`
with `A' = y/nu >= 1`; `sigma <= A'` gives
`dq <= 1 + 3*nu + delta + 2`, and the violation `dq > 4*delta+6`
forces `nu > delta+1`, hence `nu = delta+2`, `A' = 1`, `sigma <= 1`,
`t in {2,3}`. `t = 2` gives `dq = 1+3*nu > 4*nu-2 => nu < 3 =>
delta = 0`, contradiction; `t = 3` gives `dq = 4*nu + 1` odd, but
`M = 2 | dq` — contradiction.
*Case `delta = 1`*: `D in {2,3,4}`, `y = D+1`, violation `dq > 5*D`.
`D = 2` (`M = 2`): `(nu, A') = (3,1)`, `t in {2,3}`,
`dq in {10, 13}`; `dq > 10` forces `dq = 13`, odd — contradiction.
`D = 3` (`M = 3`): `(nu, A') in {(2,2), (4,1)}`; `(2,2)` maxes at
`dq = 11 < 16`; `(4,1)` gives `dq in {13, 17}`, `dq > 15` forces 17,
and `3` does not divide 17 — contradiction. `D = 4`
(`M in {2,4}`): `(nu, A') = (5,1)`, `dq in {16, 21}`, `dq > 20`
forces 21, and `M | 21` with `M | 4` forces `M = 1` — contradiction. ∎

**Census confirmation (sealed).** Wide equal-multiplicity box
`mu <= 8, delta <= 12, nu <= 60, k <= 3, lex <= 7`: `r0 = 2` — 357,260
cells, 0 Theorem E violations, 96 two-pole-constant violators, all
`M = 1`, 312 equality hits, every profile exact; `r0 = 3` — 439,730
cells, 0 violations, 248 violators all `M = 1`, 272 equality hits.
Unequal-multiplicity spot box (`r0 in {2,3}`, mults `<= 5`,
`delta <= 6`, `nu <= 24`, `k <= 2`, `lex <= 4`): 75,713 cells, 0
violations, violator M-values `{1}`. This *upgrades* the review's
empirical F3 claim to a theorem and reproduces its "0 MP2-alive
violators at r0 = 2, 3" conclusion.

**Campaign scope.** MP1 gives `r(G) <= m`
(SHEET6-MULTIPOLE.md:82) and the engine census loops
`m in range(2, td//3 + 1)` at `TDMAX = 14` (book_offaxis.py:39,49-54),
so `m <= 4` and `r0 = r(G) - 1 <= 3` on every campaign row: the
no-MP2-alive-violator statement covers the entire actual range, and
its failure at `r0 = 4` is out of range. Any future `TDMAX >= 15` run
must re-examine `r0 = 4` (the `(44,46)` witness is sealed for that
purpose).

## 5. Lemma T1′: the general zero-chain identification (F2)

**Lemma T1′.** For every two-pole cell, at every `mu`:
`kbar - w = w*dp/D` (identically, from `kbar = mu*w*dq/D` and
`dp = mu*dq - D`), and `M = dp <=> dp | dq` (a gcd tautology). At
`mu = 1` — the T1 zero-chain law's home scope, the §11 pinned solve —
additionally `dq = dp + D`, hence

    dp | dq  <=>  dp | D  <=>  w/(kbar - w) = D/dp in Z>=1 ,

and if moreover `w in Z` and `kbar in Z` (DS1(c)):
`kbar in {w + d : d | w}` — via `n = w/(kbar-w) in Z>=1`,
`d = w/n | w`, and conversely. Menus: `w=1 -> {2}`, `w=2 -> {3,4}`
(the frozen td-7 encoding), `w=3 -> {4,6}`, `w=4 -> {5,6,8}`,
`w=6 -> {7,8,9,12}`. At `mu >= 2` only `mu*dq = dp + D` holds and the
divisibility leg fails — the law is never applied there.

**Solver totality.** `e5_solve_mu1` now computes the verdict as the
direct `dq % dp == 0` and enforces the closed form (and the `M = dp`
leg) as theorem gates; it is **total** on every legal
`(w, mu0, w_U)` — the battery runs it over a 300+-state legal grid
(including the exact `w = 1` and `w = 3` inputs that crashed R2) with
no exception permitted, and cross-checks the iff on a 17,610-case
sweep. Sealed regression menus (also the §8 gate G-f fixtures):

    w=1, mu0=3, w_U=1/3 : (8,16,5,8)@kbar=2 T1-DEAD; (10,15,7,5)@3 alive
    w=2, mu0=3, w_U=2/3 : (7,21,4,7)@3 DEAD; (8,16,5,8)@4 DEAD;
                          (10,15,7,5)@6 alive       [byte-match with R2]
    w=3, mu0=3, w_U=1   : (8,16,5,8)@kbar=6 T1-DEAD; (10,15,7,5)@9 alive
    w=4, mu0=5, w_U=1/5 : (29,145,24,29)@5 DEAD; (45,81,40,9)@9 alive
    w=6, mu0=2, w_U=1/2 : (15,105,13,15)@7 DEAD; (21,39,19,3)@13 alive
    w=3/2, mu0=2, w_U=1/2 : empty menu (total, no exception)

Note the DEAD56 member `(8,16,5,8)` recurring as the T1-dead candidate
across the `w = 1, 2, 3` slices at its slice-appropriate `kbar`
(`2 = w*dq/D` scales linearly in `w`) — the T1-dead *cells* are
slice-stable even though the `kbar` menu is not, which is exactly why
hard-coding `{3,4}` is wrong. R2 §8.3's citation of
`td7_census_e5.e5_cells_C` as the general model is withdrawn: that
routine hard-codes `mu*w = 2` (a td-7 instrument).

## 6. Corrected glosses (F4 charge 5, F8.1)

**6.1 The mixed pin kills `(18,27,13,9)@5`.** The no-incoming-bound
demo keeps its arithmetic (neutral arrivals `4, 9, 14, 10^20+4` all
realize the cell under E5; the mixed formula matches only at
`nu_U = 13 = nu_G`) but now states, and machine-checks, the legality
fact R2 elided: `13` is **not** an arrival-legal vertex at
`(2/5, M5)` — `13+1` is not divisible by 5 and the §11a direct list is
`{2, 7, 12}`. Imposing the mixed pin on this cell therefore *kills*
it; the forced-nu sub-book keeps exactly `(9,15,7,3)@2` and
`(10,15,7,5)@3`, as §11a records.

**6.2 The `kbar = 6` family, qualified.** The closed form
`(4m-2, 6m-3)` covers the 12 alive rows at **odd `m = 3..25` only**
(machine-checked: the graded-equality rows are exactly that list). The
even-`m` members `m = 4, 6, 8, 10` are §11a's four recorded N1 kills —
`gcd(kbar, nu_G) = gcd(6, 3m-2) = 2` — and the packet's solver finds
each with `n1_ok = False` (never alive). The family's termination at
`m = 25` is **closure-forced** (no priced state with `w <= 2/27` at
budget 5, §11a), not a consequence of any theorem here.

## 7. Counterfixtures (repaired)

1. **`r0 = 2` breaks the constant** — the six cells `(13,7)`,
   `(19,10)`, `(20,7)`, `(38,13)`, `(109,22)`, `(195,28)`; each now
   carries the disclosure `D = 1, M = 1, MP2-dead-as-interior` and the
   fact that it attains Theorem E with equality. Wholesale `NUCAP`
   replacement stays UNSOUND (the no-pin branch fires on these rows) —
   but by Theorem F the phenomenon is confined to `M_G = 1` rows at
   `r0 <= 3`.
2. **Equal-`(mu,w)` join, no 0-edge**: `kbar = w*(2nu+1)`
   affine-unbounded (members `nu = 4, 7, 100`, all `M = 3`) —
   unchanged.
3. **Inner arrivals**: unknown `w` at solve time; no elimination, no
   bound — unchanged (prose).
4. *(deleted)* — R2's §7.4 fibre family; see Theorem D. The certificate
   field `pattern_fibre_infinite_at_fixed_kbar_nu_G` no longer exists
   (the battery asserts its absence from the sealed JSON).
5. **New G-e′ fixtures** (for §8): out-of-scope rows with `M_G >= 2`
   that must stay OPEN/capped — `(15,9)` (`r0=2`, `mu=2`, `mu0=3`,
   `nu=2`, `M=3`), `(12,16)` (`r0=3`, three `mu=1` arrivals, `mu0=3`,
   `nu=3`, `M=4`), `(44,46)` (`r0=4`, `M=2`). All three are
   machine-certified against their census laws in the packet.

## 8. Source-level migration plan, revised (NOT executed here)

The canonical engine is untouched; `NUCAP=500` stays until a
different-model review of this packet passes. All R2 line references
were re-verified by the review (F5): `solve_arr` pinned-branch incoming
check `:305-309`, `mu0 == mu` branch `:320-323`, `mu0 < mu` cap
`:325-328`, `mu == 1` doc-9 cap `:329-336`, `NUCAP` loop `:337-357`
with `:165`, loop pin `:343`. **Language correction (F5.4/F8.4): no
site is "retired". The E5 path *bypasses* the legacy code on the
scoped rows only; every legacy line stays live, byte-identical, for
out-of-scope rows** (and `:305-309` is unreachable under the scope
guard anyway, since `len(non0) == 1` never reaches the R2.1(ii) pin).

Migration-safe pseudocode (named regimes; Theorem-B graded menu per
review F5.6 — licensed because `cell_check` constructs
`dp = M_G*d0, dq = M_G*q0` with `gcd(d0,q0) = 1`, so `gcd(dp,dq) =
M_G` exactly):

    def solve_arr_e5(non0, zero, inner_mus, M_G, inner0_mu=None):
        # SCOPE GUARD (review-confirmed sufficient): pole-chain 0-leaf,
        # exactly one nonzero pole edge, no inner arrivals.
        if not (zero is a pole-chain leaf and len(non0) == 1
                and inner_mus == [] and inner0_mu is None):
            return solve_arr(non0, zero, inner_mus, M_G, inner0_mu)
            # legacy path, byte-identical verdicts (gate G-d)
        (mu, w), (mu0, w_U, nu_i) = non0[0], zero
        if mu0 < mu:                                   # REVERSE regime
            for nu_G in range(2, ceil(w/w_U) - 1 + 1): # strict < w/w_U
                kbar = (mu*w - mu0*nu_G*w_U) / (mu - mu0)   # Theorem C
                X = mu*(kbar - w)
                if kbar <= w or X <= 0: continue
                if cell_check(kbar, X, [mu], mu0, M_G): return ALIVE
            return DEAD
        if mu0 == mu:                                  # EQUAL regime
            nu_G = w / w_U          # forced; kbar NOT pinned (the two
            # handshakes coincide).  The legacy branch (:320-323) does
            # NO cell_check here; mirror it exactly for verdict parity.
            return ALIVE if (nu_G integral and nu_G >= 2
                             and arrival_state_legal(mu0, M_U)) else DEAD
        delta = mu0 - mu                               # DIFFICULT regime
        for kbar in integers in (w, mu*w*(2 + (2*delta+1)/M_G)]:
            nu_G = (delta*kbar + mu*w) / (mu0*w_U)     # Theorem C
            if nu_G not integral or nu_G < 2: continue
            X = mu*(kbar - w)
            if mu == 1:
                # pinned cell: dp = mu0 + nu_G; dq = kbar*dp/X; gates:
                # dq integral, nu_G | dq-1, s >= 1; T1 by dp | dq
                # (Lemma T1' -- NEVER the {3,4} encoding); N1
                # gcd(kbar, nu_G) = 1; MP2 M >= 2.
                ...
            else:
                # conservative existence gate (s3.5); optionally the
                # finite cell book via fibre_solve (Theorem D).
                if cell_check(kbar, X, [mu], mu0, M_G): return ALIVE
        return DEAD
        # Arrival layer everywhere: state gate mu0 | M_U + menu
        # recording (neutral / direct / entry); nu_U itself is FREE and
        # never enumerated.  Tag verdicts reading=promoted-Q+E5; emit
        # the U_7C fork note for forced-nu consumers.

Gates before any engine adoption (revised): (G-a) replay the §11a book
— all 17 cells with identical `(kbar, w_U^req, arrivals)`; (G-b)
forced-reading parity — the 2-cell sub-book under `nu_U = nu_G`; (G-c)
DEAD56 negative controls; (G-d) legacy parity on out-of-scope rows —
bit-identical verdicts; (G-e′) **strengthened**: the §7.1 six *plus*
the `M_G >= 2` fixtures `(15,9)`, `(12,16)`, `(44,46)` and
inner-arrival rows must remain OPEN/capped (R2's gate tested only
`M_G = 1` rows and three non-cells); (G-f) **new**: `w != 2` in-scope
regression — the solver menus at `w = 1` and `w = 3` must match §5's
sealed cells (this is the gate that would have caught R2's §8.3). The
scoped `U_7C`-conditional mixed-pin cap remains licensed only as in R2
§8.5, unchanged.

## 9. Packet record

`cases/m2_caseiii_two_pole_e5_local_index_r3_20260829/`:

```text
5f40d91f258bea7ccff14a25d91440fa64b60e2def494f3e2a2629302cd1031d  caseiii_two_pole_e5_r3.py
d771ddc27cce3c2fa582d93b4ac5be2e1275caa7ce57de925d654a65815a7013  test_caseiii_two_pole_e5_r3.py
624a24f4d35e9937e3c3b103e77d29ef80f160cdcad5eea1fb6d1156f2704a1d  README.md
feb60ca9da85af38108f0e28e99a1702bc353250a82a385cd72faad5b7fbae65  certificate_r3.json
```

Sealed certificate SHA-256 (embedded field, rebuilt from legal cells
only; the R2 infinite-fibre field is gone):
`a26d992f1d557e8fff908319a1e5294d6364ca80815308e8a814d2f2fd88b471`.

Tests: `python3 test_caseiii_two_pole_e5_r3.py` and
`python3 -O test_caseiii_two_pole_e5_r3.py` both pass with exactly
**1,532,749 checks** (~11 s each; no CAS; canonical engine imported
read-only for the `cell_check` cross-check and the `NUCAP == 500`
assertion). The battery: R2's full inline Lemma-A/Theorem-B sweep and
17-cell book cross-check (unchanged); the solver totality grid and the
17,610-case Lemma T1′ sweep; the reduced-box fully-inline fibre census
(>100k cells) with member-for-member `fibre_solve` comparison on 500+
fibres; the module-level box census (92,772-replay) and complete
census; inline r0-graded censuses cross-checked against the module on
identical reduced boxes plus the wide-box pins; the (44,46) witness;
the charged slice; the corrected no-incoming-bound demo with the
`nu_U = 13` legality checks; certificate determinism, `-O` subprocess
sha parity, sealed-JSON byte-match; 16 invalid-input refusals; and the
mutation battery.

Hostile mutations (staged on `/tmp` copies inside both suites; an
unmutated control must pass; the packet is never modified): R2's
`MUT_A`–`MUT_F` (Lemma-A constant, graded constant, elimination sign,
countercell ratio, slice identity, firewall flip) all carry over and
still fire; plus the four **permanent** R3 mutations mandated by the
repair order — `MUT_G` re-introduces the `(38,19)`-style NE bypass
(true strict-NE cap → `mu - 1` proxy; dies `strict NE law failed` when
the re-admitted member hits the witness re-certification), `MUT_H`
re-specialises T1 to `{3,4}` (dies `Lemma T1' closed form disagrees
with dq % dp` on the `w = 1` regression), `MUT_I` misstates the
Theorem-F violator MP2 status (dies `Theorem F refuted: an MP2-alive
(M >= 2) cell exceeds the two-pole constant at r0 <= 3`), `MUT_J`
flips the countercell `M = 1` disclosure (dies on the first §7.1
cell). All ten detected in both suites.

## 10. R2-to-R3 inventory (literal)

| R2 object | R3 status |
|---|---|
| Lemma A, Theorem B, Theorem C + no-incoming-bound proposition | **preserved verbatim** (review-confirmed F4) |
| `gap_pattern_certificate`, `kbar_bound`, `e5_eliminate_nu_g` | preserved verbatim |
| `charged_slice`; `BOOK`/`FORCED_SUBBOOK`/`DEAD56_SPOT` | preserved verbatim |
| `MUT_A`–`MUT_F` | preserved (all still fire) |
| §7.4 "infinite pattern fibre" + members `(38,19)`, `(62,31)`, `(134,67)`, inline `s=45` | **withdrawn/deleted** (F1); refuted pattern-by-pattern |
| certificate field `pattern_fibre_infinite_at_fixed_kbar_nu_G` | **removed**; absence asserted; firewall key `r2_fibre_infinitude_reinstated: False` |
| §8.3 T1 gate `dp \| dq <=> kbar in {3,4}` at general `w` | **withdrawn** (F2); firewall key `t1_w2_encoding_reinstated: False` |
| `e5_solve_mu1` | **repaired**: total on legal input; verdict = `dq % dp`; closed form + `M = dp` as theorem gates |
| `e5_regimes` | repaired: named regimes; EQUAL-regime `kbar_pinned: False` record (F5.3/F5.5) |
| `counterfixtures` | repaired: fibre family deleted; `M = 1`/MP2-dead disclosure + Theorem-E-equality flag on all six `r0=2` cells; G-e′ `M_G >= 2` fixtures added |
| `no_incoming_bound_demo` | repaired: `nu_U = 13` arrival-legality facts machine-checked; mixed-pin-kills gloss (F4c5/R5) |
| `promoted_book_battery` | extended: odd-`m` family identification, even-`m` N1 kills, closure-forced termination (F8.1) |
| `certificate` | rebuilt from scratch, legal cells only |
| — | **new**: Theorem D (`fibre_bound`, `fibre_solve`, `fibre_box_census`, `fibre_complete_census`, `seven4_fibre_certificate`, `ne_cap`) |
| — | **new**: Theorem E + Theorem F (`arity_census`, `arity_unequal_census`, `theorem_ef_certificate`; `(44,46)` witness) |
| — | **new**: Lemma T1′ (`t1_closed_form`, `t1_divisor_menu`, `t1_regression`) |
| — | **new**: permanent mutations `MUT_G`, `MUT_H`, `MUT_I`, `MUT_J` |

Relative to the review itself: F1/F2/F3/F5/F8 accepted and repaired;
its arity-graded bound and fibre-bound offers independently re-derived
and, for Theorem F at `r0 = 3`, **upgraded from empirical to proved**;
its capped deep-search census figures (57,960/9/27) **did not
replicate** and are superseded by the cap-free complete census (§3.4).

## 11. Claim firewall

This remains a conditional merge-arithmetic result at the
promoted-record tier (Q+E5 per H5a; the `U_7C` fork recorded, not
adjudicated). It proves and authorizes **nothing** about: removing or
replacing `NUCAP` (stays; wholesale replacement certified UNSOUND on
`r0 >= 2`/inner rows), any canonical engine edit, equal-nonzero-join
`kbar` bounds, multipole or inner-merge trees, `r0 = 4` MP2 behaviour
beyond the single sealed witness, the legacy `cell_check` grammar
beyond its conservative-existence role, realizability of any cell
(i-sync/`n_e` untracked; the priced-closure layer is cited, not
re-proved), source landing, full configuration cover,
topological-degree bounds, Keller counterexamples, JC2, or any
AWS/fleet action. What changed vs R2's firewall: "finite cell books at
`mu >= 2`" moves from the not-proven list to the proven list (Theorem
D), and two new permanent keys pin the withdrawn claims
(`r2_fibre_infinitude_reinstated`, `t1_w2_encoding_reinstated`, both
False). Final status: `SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`.

---
Report-body SHA-256 (bytes before the separator line above): `a902c94e8f073af11df103bacb65376521e8ec2dc74678be67126c2fa024a0b6`
