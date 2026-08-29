# Two-pole case III under promoted Q+E5: the merge-local index theorem (R2)

Producer: Fable 5, acting as primary repairer (not reviewer) of
`xmodel/m2-caseiii-two-pole-incoming-index-bound-sol56-20260829.md` (R1)
after the Fable 5 hostile review
(`xmodel/m2-caseiii-two-pole-incoming-index-bound-hostile-review-fable5-20260829.md`,
verdict REPAIR_REQUIRED, body `9cbb1a7c…681`). Date: 2026-08-29 UTC.
Lifecycle: `SOURCE_READY_FOR_DIFFERENT_MODEL_HOSTILE_REVIEW`. This report
authorizes **no canonical engine change and no AWS/fleet action**;
`NUCAP=500` stays. R1 and its packet are byte-untouched; the fresh packet
is `cases/m2_caseiii_two_pole_e5_local_index_r2_20260829/`.

Sources: `xmodel/sol-h5a.md` + `xmodel/grok-h5a-review.md` (promoted H5a
resolution), `ladder/BOOK-OFFAXIS.md` §§6–11a (R1.0/R2 laws, §11a promoted
17-cell book), `ladder/SHEET6-DEPTH.md` §§5c–5d (case-III/root edge laws),
`ladder/SHEET6-MULTIPOLE.md` (MP2), `cases/td7_census_e5.py` (E5 engine
pattern), `cases/book_offaxis.py` (`solve_arr`/`cell_check`/`NUCAP`), and
`xmodel/m2-budget-quotient-primary-research-opus5-20260829.md` (adjudicated
in §6). No web, no CAS, no `jc2-lean` access, no workspace-wide git.

## 0. What R1 got wrong, and what survives

R1's merge arithmetic is correct and sharp; its headline object is not.
R1 bounded "the incoming zero-edge index `h = nu_H`" via the case-III
handshake `X = mu0*(kbar - h*w0)` — the printed Prop 9.3(g),(h)/"mixed"
pin. The promoted H5a resolution (sol-h5a Props 1–2, grok-reviewed SOUND,
promoted in BOOK-OFFAXIS §11-PRE/§11a) proves that pin incoherent unless
`nu_U = nu_G` — open CONJECTURE `U_7C` — and fixes the case-III transport
as E5. Campaign-normalized (sol-h5a (18)), the 0-edge handshake is

    X = mu0*(kbar - nu_G*w_U),

where `w_U = (kbar_U - rho_U)/nu_U` is the arriving state invariant: the
incoming `nu_U` cancels into `w_U` and is **free** — the §11a book records
infinite legal arrival menus (neutral classes `nu_U == -1 (mod mu0)`).
So at the promoted tier the eliminated index is the **merge-local
`nu_G`**, there is no incoming-index bound, and none is needed. What
survives R1 unchanged is the reading-independent half: the pattern gap
lemma and the `kbar` bound (the case-II side is untouched by H5a —
grok-h5a Finding 3). This report re-founds the theorem on the promoted
pin, adds a new M-graded refinement that is *tight on 12 of the 17
promoted cells*, corrects the Opus adjudication in both directions,
plants the widening counterfixtures, and gives the source-level migration
plan. Every certificate field is regenerated, not patched.

## 1. Setting and scope hypotheses

All frames are i-normalized (DEPTH §1): `rho = D/deg p`,
`kbar = kappa*(1-pi)`, `w = (kbar - rho)/nu`. A **two-pole case-III
merge** is an interior merge `G` (not the root; root meets are case I
with the separate `0 < w < 1` window, DEPTH §5d) with:

  (H1) exactly one nonzero arriving edge, a pole-chain leaf with recorded
       state `(mu, w)`, `mu >= 1`, `w > 0` — Prop 9.3 case II;
  (H2) a pole-chain arrival at the 0-direction with multiplicity
       `mu0 >= 1` and arriving state `(w_U, M_U)`, `w_U > 0` — Prop 9.3
       case III, so `eps = mu0` and `nu_G >= 2` (a `nu_G = 1` merge is
       the `V_2\V_1` case-I meet, out of case-III scope; R2 §7 preamble);
  (H3) no inner-merge arrivals;
  (H4) the promoted pattern laws: R1.0 q-shape, R2.2 census
       `dp = mu0 + nu*(mu + Sm)`, `dq = 1 + nu*(1 + s)` with `nu = nu_G`,
       `s = k + lex`, `Sm = sum m_j` over the `k` non-chain orbits,
       `lex` q-only extras; (S) searrow `mu*dq > dp` and `mu0*dq > dp`;
       (NE) strict `m_j*dq < dp`; (R) `dp != mu_star*dq` for every
       p-multiplicity.

Write `delta = mu0 - mu`, `D = mu*dq - dp >= 1` (by (S)),
`A = mu*s - Sm`, `M = gcd(dp, dq)`. From (NE)+(S), `m_j <= mu - 1`; at
`mu = 1` this forces `k = 0`. Notation warning: this `s` excludes the
arriving orbit; Opus's `s` is `r0 + k + lex = s + 1` (his §2). The packet
helper `gap_pattern_certificate` enforces every H4 law as a hard gate
(repairing R1's F7.1 acceptance of NE-illegal and `nu = 1` inputs).

## 2. Lemma A (reading-independent two-pole gap bound)

**Lemma A.** At every two-pole case-III merge with `delta >= 1`:

    D = nu*A - delta,   A >= k + mu*lex >= s >= 1,
    dq/D <= 2*delta + 3,   and
    kbar = mu*w*dq/D <= mu*w*(2*delta + 3).

Equality `dq/D = 2*delta+3` holds iff `nu = delta+1`, `s = 1`, `A = 1`
(i.e. `k=1, m_1 = mu-1, lex=0` for `mu >= 2`, or `k=0, lex=1` for
`mu = 1`); it forces `D = 1`, hence `M = 1` (since `M | D`): **every
sharpness witness is MP2-dead as an interior merge**.

*Proof.* The identity: `D = mu + mu*nu*(1+s) - mu0 - nu*(mu+Sm)
= nu*(mu*s - Sm) - delta`. `A >= k + mu*lex`: from `m_j <= mu-1`,
`Sm <= k*(mu-1)`, so `A = mu*k + mu*lex - Sm >= k + mu*lex >= s`. If
`s = 0` then `k = lex = 0`, `Sm = 0`, `A = 0`, `D = -delta < 0`,
contradicting (S); so `s >= 1`.

Gap bound. If `nu*s <= delta` then `nu <= delta` (as `s >= 1`) and
`dq = 1 + nu + nu*s <= 1 + 2*delta`, while `D >= 1`; so
`dq/D <= 2*delta+1 < 2*delta+3`. If `nu*s >= delta + 1`, put
`y = nu*A >= nu*s`; then `D = y - delta >= nu*s - delta >= 1` and
`dq = 1 + nu + nu*s <= 1 + 2*nu*s <= 1 + 2y` (using `nu <= nu*s`), so

    dq/D <= (1 + 2y)/(y - delta),

which is decreasing in `y`; at `y = delta+1` it equals `2*delta+3`.
Equality requires `nu = nu*s` (`s = 1`), `nu*s = y = nu*A` (`A = s = 1`),
and `y = delta+1` (`nu = delta+1`, `D = 1`); the two shapes listed are
the only patterns with `s = A = 1`. Conversely both attain it for every
`delta` and every admissible `mu` (packet sweep: attained at every
`delta <= 8`).

`kbar` law. The nonzero edge is case II; its R2.1 handshake
`X = mu*(kbar - w)` and the Prop 9.3(b) consistency `X/kbar = dp/dq` give
`kbar*(mu*dq - dp) = mu*w*dq`, i.e. `kbar = mu*w*dq/D`. Case II is
untouched by H5a (the transport denominator "is already `nu_G` by printed
(c)", grok-h5a Finding 3), and the pattern laws are handshake-free, so
both displayed bounds hold under either recorded case-III reading. ∎

## 3. Theorem B (M-graded refinement — the honest `M >= 2` bound)

**Theorem B.** At every two-pole case-III merge with `delta >= 1` and
`M = gcd(dp, dq)`:

    dq/D <= 2 + (2*delta + 1)/M,
    kbar  <= mu*w*(2 + (2*delta + 1)/M),

with equality iff `M | 2*delta + 1` (hence `M` odd) and the cell is the
`s = 1`, `A = 1`, `nu = delta + M` pattern; equality forces `D = M`
exactly. At `M = 1` this is Lemma A. Consequently no MP2-surviving cell
ever attains `2*delta+3`; on `M >= 2` cells `dq/D <= (2*delta+5)/2`,
and the even-`M` bound is strict (`M | 2*delta+1` is odd).

*Proof.* `M | dp` and `M | dq` give `M | D`, so `D >= M`. Branch
`nu*s <= delta`: `dq <= 1 + 2*delta` and `D >= M` give
`dq/D <= (2*delta+1)/M < 2 + (2*delta+1)/M`. Branch `nu*s >= delta+1`:
with `y = nu*A`, now `y = D + delta >= M + delta`, and
`dq <= 1 + 2y` as before, so `dq/D <= (1+2y)/(y-delta)
<= (2*delta + 2M + 1)/M` at `y = delta + M`. Equality needs `s = A = 1`,
`nu = y = delta + M`, `D = M`; then `dq = 2*(delta+M) + 1`, and
`M | dq  <=>  M | 2*delta+1`. Conversely, for any odd `M | 2*delta+1`
take the `s = A = 1` shape with `nu = delta + M`: `D = nu - delta = M`,
`dp = mu*dq - M`; `M | dq` by the divisibility, hence `M | dp`; and
`gcd(dp,dq) | D = M` while `M` divides both, so `gcd(dp,dq) = M`
exactly. ∎

Sharpness where it matters: the `mu = 1` equality family is
`(dp, dq) = (4m-2, 6m-3)` at `mu0 = m = delta+1`, `M = 2m-1 = 2*delta+1`
— exactly the promoted §11a `kbar = 6` family. **12 of the 17 promoted
cells attain Theorem B's bound exactly** (all rows with `kbar = 6`,
`mu0 = 3, 5, ..., 25`), and they are MP2-alive (`M = 2*mu0 - 1 >= 5`).
So while Lemma A's constant is realized only on MP2-dead cells (R1's
sharpness story, F6), the M-graded constant is realized on the live
promoted book — evidence it is the right refinement. Verified per cell
in the packet; the per-delta sweep also confirms graded equality occurs
at every odd divisor `M` of `2*delta+1` and never at even `M`.

## 4. Theorem C (the E5 elimination and the merge-local `nu_G`)

**Theorem C.** Under the promoted Q+E5 pin, at a two-pole case-III merge
the two handshakes `X = mu*(kbar - w)` (case II) and
`X = mu0*(kbar - nu_G*w_U)` (E5 case III) eliminate `X` to the exact
identity

    mu0*nu_G*w_U = delta*kbar + mu*w.

Consequently, per arriving state `(w_U, M_U)`:

1. (`mu0 > mu`, difficult regime) `kbar in Z` (`nu_G >= 2`), and
   Lemma A / Theorem B give the finite menu
   `kbar in Z ∩ (w, mu*w*(2*delta+3)]` with exactly one candidate
   `nu_G = (delta*kbar + mu*w)/(mu0*w_U)` per `kbar`; hence

       nu_G <= mu*w*(delta*(2*delta+3) + 1)/(mu0*w_U),

   and on a cell of gcd `M` the graded form
   `nu_G <= mu*w*(delta*(2 + (2*delta+1)/M) + 1)/(mu0*w_U)`, which is an
   *equality* on the 12 promoted `kbar = 6` rows.
2. (`mu0 = mu`) the elimination degenerates to `nu_G*w_U = w` exactly:
   at most one `nu_G`, no pattern input needed; `nu_G = 1` means the
   configuration is case-I territory, not a case-III merge.
3. (`mu0 < mu`) `X > 0` gives `kbar > w`, hence
   `mu0*nu_G*w_U = mu*w - (mu-mu0)*kbar < mu0*w`, i.e. the strict bound
   `nu_G < w/w_U` — sharper than the R1-form `mu*w/(mu0*w_U)`, which
   only used `kbar > 0`.

**Proposition (no incoming bound follows or is required).** Under Q+E5:
(i) the case-III law contains no `nu_U` — the incoming index enters only
through the state invariant `w_U`, so the map (arrival vertex) → (cell
data) factors through `(w_U, M_U)`; (ii) at fixed state the legal
arrival menu contains the entire neutral congruence class
`nu_U == -1 (mod mu0)` (P2 arrival law; recorded per cell in the
promoted §11a book), so infinitely many `nu_U` realize the identical
cell and **no finite incoming bound is derivable** — one would refute
the promoted book's own recorded menus; (iii) none is required: two-pole
finiteness at fixed budget is (finite priced `(w_U, M_U)` closure) ×
(finite `kbar` menu, Lemma A) × (one `nu_G` per `kbar`, the
elimination). Moreover the mixed pin's "required incoming index"
`h_mixed = (delta*kbar + mu*w)/(mu0*w_U)` **equals `nu_G` identically**
on every E5-realizable cell (verified 17/17), so imposing the mixed pin
there is precisely imposing `nu_U = nu_G`, i.e. CONJECTURE `U_7C`. ∎
(Packet demo: on `(18,27,13,9)@5`, sampled neutral arrivals
`nu_U in {4, 9, 14, 10^20+4}` are all legal and cell-invariant under E5,
while the mixed formula varies and matches the cell only at
`nu_U = nu_G = 13`.)

## 5. The 17 promoted cells, the old discriminator slice, sharpness

**Promoted book (§11a), frozen chain-1 `(mu,w) = (1,2)`.** All 17 cells
verify, in the packet and by the independent test copy: the pattern
`dp = mu0 + nu_G`, `dq = 1 + 2*nu_G` (`k = 0` forced at `mu = 1`,
`lex = 1`); the reading-free `kbar = 2*dq/D` with `kbar in {5,6,7}
<= 2*(2*delta+3)`; the E5 identity `mu0*nu_G*w_U = delta*kbar + 2`; the
regime-1..3 `nu_G` bounds; Theorem B with equality exactly on the 12
`kbar = 6` rows; and recovery of every row by the packet's merge-local
solver `e5_solve_mu1` (which also re-finds the `DEAD56` members
`(7,21,4,7)` and `(8,16,5,8)` as its `kbar in {3,4}` T1-dead candidates
at the `(2/3, M3)` state — the solve and the census agree).

**Old td-7 discriminator slice** `(mu,w) = (1,2)`, `(mu0,w_U) = (2,3/2)`
— recomputed under BOTH pins, kill reading-stable:

* E5: `3*nu_G = kbar + 2 <= 12` gives `nu_G in {2,3,4}`: `nu_G = 2` →
  `kbar = 4`, cell `(4,8)`, T1-dead (`kbar in {3,4}`); `nu_G = 3` →
  `kbar = 7`, cell `(5,7)`, `M = 1`, MP2-dead; `nu_G = 4` → `kbar = 10`,
  `dq = 15/2` non-integral, dead.
* Mixed (conditional on `U_7C`): `h <= floor(12/3) = 4`, odd ray leaves
  `h = 3`, same `(5,7)` cell, MP2-dead — R1's computation, reproduced.

Provenance flags (carried in the sealed certificate): this slice replays
**RETRACTED** BOOK-OFFAXIS §8 Step 3 and is legitimate only as the
`w_U = 3/2` entry-state slice of class C; the genuinely promoted `@2`
cell `(9,15,7,3)` lives on the `w_U = 1/2` slice and is untouched and
unkilled; "h odd, h >= 3" is `nu_U` language, meaningful only under the
mixed pin.

**Sharpness.** Equality in `dq/D <= 2*delta+3` has `D = M = 1` and is
MP2-dead (Lemma A); the constant is attained for every `delta` but never
by an MP2-surviving cell. The honest `M >= 2` refinement is Theorem B:
`dq/D <= 2 + (2*delta+1)/M`, strict at even `M`, attained exactly at odd
`M | 2*delta+1` on the `nu_G = delta+M` cell — and realized inside the
promoted book itself (12/17 rows, including `(10,15,7,5)@3` with
`nu = 2+5` and `(98,147,73,49)@25` with `nu = 24+49`, where the graded
`nu_G` bound is also exact: `73 = (24*6+2)/(25*(2/25))`).

## 6. Opus adjudication, corrected in both directions

R1 wrote: Opus Thm 2.4/4 "correctly bounds … `nu_G`" and errs only in
later calling it `nu_H`. Both halves are wrong, in opposite directions:

* **R1 was too generous.** Opus clause 4, `nu <= mu0*num(w_0)`
  "unconditionally", binds *neither* index. As a `nu_G` bound, **16 of
  the 17 promoted cells violate it** (all but `(25,35,17,5)@8`; e.g.
  `(9,15,7,3)@2`: `7 > 2`; `(98,147,73,49)@25`: `73 > 50`). As an
  incoming-`nu_U` bound it fails on the forced-subbook cell
  `(9,15,7,3)@2`, which is legal under *both* readings with recorded
  arrival `nu_U = 7 > 2 = 2*num(1/2)`. The root cause is Theorem 4(4a):
  sound for case-I/II edges (it holds with equality on the nonzero edge
  of `(9,15,7,3)`), but clause 4 feeds the **0-edge** into (4a)'s
  case-II transport `kbar = mu_e*w_e*dq/E_e`, which matches neither
  recorded case-III reading; under E5, `E_0 = nu_G*|T|` makes `nu_G`
  cancel and the route collapses.
* **R1 was too harsh.** Opus did not confuse two symbols. Its §10c
  states the H5a fork verbatim ("under the promoted E5/Q-value reading
  (I4) uses `nu_G`, so `nu_U` is genuinely free … I do not adjudicate
  H5a") and its clause-4 phrasing is internally consistent with the
  mixed reading it declined to reject. The unlicensed step is the
  (4a)-on-the-0-edge transport, not the naming. R1's "notation
  correction" — silently resolving the fork on the non-promoted side —
  was itself the inverted move.
* **Sound replacement** (this packet): the reading-free
  `kbar <= mu*w*(2*delta+3)` (Lemma A), the E5 elimination
  `mu0*nu_G*w_U = delta*kbar + mu*w`, and the per-state bound
  `nu_G <= mu*w*(delta*(2*delta+3)+1)/(mu0*w_U)`, with the Theorem-B
  graded form tight on the `kbar = 6` family. Verified on all 17
  promoted cells. Opus's congruence-quotient claim for 0-edges ("the
  congruence quotient is complete at 0-edges" under E5, §10c) is
  *confirmed* by Theorem C's proposition; its clause-4 "finite set of
  exact values" quotient for case-III arrivals is the `U_7C`-conditional
  statement only.

## 7. Why the theorem cannot be widened (counterfixtures)

All planted and machine-certified in the packet (`counterfixtures()`),
each satisfying every recorded law of its shape:

1. **Second nonzero arrival (`r0 = 2`) breaks the constant.** Two
   equal-`mu` nonzero arrivals + 0-edge, `nu = delta+1`, `k = 1`,
   `m = mu-1`, `lex = 0` gives `D = 1` and `dq/D = 3*delta + 4
   > 2*delta+3`, with (S) on all three edges, strict (NE), and (R):
   cells `(13,7)` (`mu=2, mu0=3`), `(19,10)`, `(20,7)`, `(38,13)`,
   `(109,22)` (`mu=5, mu0=11`), `(195,28)` (`mu=7, mu0=15`). These rows
   are reachable by `solve_arr`'s own no-pin branch (it fires for any
   `len(non0)`), so **wholesale `NUCAP` replacement by the two-pole
   bound is unsound even under the mixed pin** — R1's "closes the
   mathematical reason for the old `NUCAP=500` fallback in the
   `mu0>mu>=2` branch" stays overdrawn exactly as reviewed (F3).
2. **No 0-edge: no bound at all.** The equal-`(mu,w)` join family
   (Opus §6a) has `E = mu` constant and `kbar = w*(2*nu+1)`
   affine-unbounded; packet members `(mu,w) = (3,3)`,
   `nu in {4,7,100}`, all `M = 3`, T1-alive. The 0-arrival is what pins
   `kbar` against `delta`; remove it and no constant exists.
3. **Inner arrivals.** An inner-merge edge (0-slot or partner) has
   unknown `w` at solve time: the case-II elimination is unavailable and
   no `nu_G` bound is derivable from recorded data. Rows with
   `inner_mus != []` or `inner0_mu` must keep the cap and OPEN fallback.
4. **Pattern-fibre caveat (new).** Even inside two-pole scope, for a
   `mu >= 2` partner with `kbar < mu*w` the cell fibre over a fixed
   `(kbar, nu_G)` can be **infinite**: at `(mu,w,mu0) = (4,1,5)`,
   `nu_G = 3`, `kbar = 2`, the family `A = 3+2s`, `Sm = 2s-3` gives
   cells `(20,10), (26,13), (38,19), (62,31), …` for every `s >= 2`
   (integrality is automatic), with `M = |T|` growing without bound.
   All bounds of §§2–4 hold on every member (`dq/D = 1/2`); what fails
   is any hope of a finite *cell book* per state at `mu >= 2`. The
   finite objects are the `kbar` menu and `nu_G`; the pattern layer
   must remain an existence check (`cell_check` style), exactly as at
   `mu = 1` it happens to collapse to at most one cell
   (`dp = mu0 + nu_G` pinned). This caveat binds the migration plan.

## 8. Source-level migration plan (NOT executed here)

Goal: replace the legacy capped `nu_H` enumeration with a Q+E5
merge-local solve in the `cases/td7_census_e5.py` style. The canonical
engine `cases/book_offaxis.py` is not modified in this task; `NUCAP`
stays until a different-model review of this packet passes.

Mixed-pin sites to retire (all instantiate `X = mu0*(kbar - nu_H*w0)`):
`solve_arr` pinned-branch incoming check (`book_offaxis.py:305-309`,
`nuH = (kbar - X/mu0)/w0`), the `mu0 == mu` branch (`:320-323`,
`nuH = w/w0`), the `mu0 < mu` cap (`:325-328`), the `mu == 1` doc-9 cap
(`:329-336`), the `mu0 > mu >= 2` `NUCAP` loop (`:337-357` with `:165`),
and the loop pin `kbar = (mu0*nuH*w0 - mu*w)/(mu0-mu)` (`:343`).

Steps:

1. Add `solve_arr_e5(non0, zero, inner_mus, M_G, inner0_mu)` alongside
   (no in-place edit). Scope guard first: the E5 solve applies iff
   `zero` is a pole leaf, `len(non0) == 1`, `inner_mus == []`,
   `inner0_mu is None`. Out-of-scope rows fall through to the legacy
   branch unchanged (cap + OPEN) — countercells §7.1/7.3 make this
   mandatory.
2. In scope, with `(mu, w) = non0[0]`, `(mu0, w_U, nu_i) = zero`:
   regime 2 solves `nu_G = w/w_U` (forced; integer `>= 2` else DEAD);
   regime 1 loops `nu_G < w/w_U` (strict, finite); regime 3 loops the
   finite menu `kbar in Z ∩ (w, mu*w*(2*delta+3)]`, computing
   `nu_G = (delta*kbar + mu*w)/(mu0*w_U)` — integer `>= 2` else skip.
   **No `nu_H` loop exists; `NUCAP` is removed by rebuild, not replaced
   by a bound.**
3. Per `(kbar, nu_G)`: keep the existing `cell_check(kbar, X, …)`
   existence solve for the pattern layer (the §7.4 fibre caveat forbids
   cell enumeration at `mu >= 2`); at `mu == 1` optionally pin
   `dp = mu0 + nu_G`, `dq = kbar*dp/X` and apply T1
   (`dp | dq <=> kbar in {3,4}`), N1 (`gcd(kbar, nu_G) = 1`), MP2, and
   `dq == 1 (mod nu_G)` directly, as `td7_census_e5.e5_cells_C` does
   via its `(I5a)-(I5d)` inversion.
4. Arrival legality: replace the `nu_ok(nuH, …)` incoming test with the
   state-level gate `mu0 | M_U` plus menu recording (neutral class
   always nonempty; direct step-cells and entry as in
   `td7_census_e5.nu_legal`) — the arrival vertex itself is free and
   must not be enumerated. The `nu_i` argument survives only for the
   legacy branch.
5. Tag every verdict with the reading: `reading=promoted-Q+E5`;
   emit the `U_7C` fork note wherever a forced-nu consumer would read
   the output. If the campaign ever elects to work inside `U_7C`, the
   scoped mixed-pin cap `ncap = floor(mu*w*(delta*(2*delta+3)+1)/
   (mu0*w0))` with DEAD-on-exhaust is licensed **only** on the H1–H3
   scope rows and only with an explicit `U_7C`-conditional tag (review
   §"safe engine consequence", restated).
6. Gates before any engine adoption: (G-a) replay the §11a book — all 17
   promoted cells recovered with identical `(kbar, w_U^req, arrivals)`;
   (G-b) forced-reading parity — the 2-cell sub-book under the
   `nu_U = nu_G` gate; (G-c) DEAD56 negative controls; (G-d) legacy
   parity on out-of-scope rows (bit-identical verdicts); (G-e) the
   packet's counterfixture cells must remain OPEN/capped. The packet's
   `e5_solve_mu1` already passes (G-a)-style recovery for all 17 rows
   plus the two DEAD56 spot candidates.

## 9. Packet record

`cases/m2_caseiii_two_pole_e5_local_index_r2_20260829/`:

```text
e2643ec770c57772b9d25c58bcff28407552c986b77624b00aadff3a1f17fbfb  caseiii_two_pole_e5_r2.py
741fb06b2365d9da69d21890c06c92539d3c312d0cffb4be2581c598b283e348  test_caseiii_two_pole_e5_r2.py
4095486921b505a3a373ff1f8767c7be0908978e914421cb9ee8101c1eb43a6b  README.md
02586a42d3eae43b9f0bbeb30ebf12c9fb995fe573189afeee8341a8a67dba46  certificate_r2.json
```

Sealed certificate SHA-256 (embedded field, regenerated — including the
inverted R1 `notation_correction`, per review F7.3):
`bf8e25ebb0af755ad9242ff22d34976a193ff59700fc79ed999628e3fee09c6a`.

Tests: `python3 test_caseiii_two_pole_e5_r2.py` and
`python3 -O test_caseiii_two_pole_e5_r2.py` both pass with exactly
**1,264,851 checks** (< 1 s each; no CAS). The battery: an independent
integer sweep of Lemma A + Theorem B over `mu <= 6, delta <= 8,
nu <= 26, k <= 3, lex <= 4` (299,447 `D > 0` cells, 49,791 NE-legal;
NE-illegal tuples separately verified to have `dq/D <= 1`), exact
equality censuses (plain equality: `D = M = 1` at every hit, attained at
every delta; graded equality: `D = M`, `nu = delta+M`, only odd
`M | 2*delta+1`, attained at every delta, `M = 3` whenever
`3 | 2*delta+1`), an independently typed copy of the 17-cell book with
the full §5 battery, regime menus and solver recovery (including the
`mu0 = 3` menu being exactly {two DEAD56 T1-dead candidates + the book
cell}), the charged slice under both pins, all counterfixture families
plus inline members beyond the module's lists, the no-incoming-bound
demo (`nu_U = 10^20 + 4` legal and cell-invariant), certificate
determinism, `-O` subprocess sha parity, byte-match of the committed
`certificate_r2.json` against fresh regeneration, and 10 invalid-input
refusals (including NE-illegal and `nu = 1` patterns, now hard-rejected).

Hostile mutations (all NEW vs R1's four; staged on `/tmp` copies inside
the ordinary test run, packet untouched; an unmutated control must
pass): MUT_A Lemma-A constant `2*delta+3 -> 2*delta+2`; MUT_B graded
constant `+1 -> -1`; MUT_C elimination sign `+mu*w -> -mu*w`; MUT_D
countercell ratio `3*delta+4 -> 3*delta+3`; MUT_E charged-slice identity
`3*nu_G-2 -> 3*nu_G+2`; MUT_F firewall flip
`nucap_removal_authorized -> True`. All six detected (nonzero exit in
`certificate()`); manual spot-run of MUT_C dies with "solver failed to
recover book cell alive".

## 10. Claim firewall

This is a conditional merge-arithmetic result at the promoted-record
tier (Q+E5 per H5a; the `U_7C` fork is recorded, not adjudicated — the
mixed pin remains coherent inside `U_7C`, and the 2-cell sub-book is
untouched). It proves and authorizes **nothing** about: removing or
replacing `NUCAP` (stays; wholesale replacement certified UNSOUND on
`r0 >= 2`/inner rows), any canonical engine edit, equal-nonzero-join
`kbar` bounds (affine-unbounded, §7.2), multipole or inner-merge trees,
the legacy `cell_check` grammar beyond its existence role, finite cell
books at `mu >= 2` (§7.4), realizability of any cell (`i`-sync/`n_e`
untracked), source landing, full configuration cover, topological-degree
bounds, Keller counterexamples, JC2, or any AWS/fleet action. Final
status: source-ready for different-model hostile review.

---
Report-body SHA-256 (bytes before the separator line above): `01deb67e278153f607ee9483761cfe0657dabf475458b5071d9f397ddf7ca1e8`
