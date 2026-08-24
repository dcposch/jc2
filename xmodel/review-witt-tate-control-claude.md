# Hostile different-model review: unrestricted all-Witt Artin--Schreier control

Target: `xmodel/witt-tate-control-20260824.md` (PROVISIONAL, producer
"OpenAI Codex, Bacon provisional W descendant", basis `8bf25a5`).

**VERDICT: CONFIRMED.**

Every mathematical clause was independently rederived by hand (general odd
prime `p`, general `n`) and recomputed with this reviewer's own sparse-dict
polynomial arithmetic (no repo code, no CAS, no network): the exact integer
determinant identity, determinant one over `Z/p^n` at every level, full
reduction compatibility from every later level to every earlier level, the
fixed marked collision with distinct sources, the exact support/degree/
valuation growth, the finite-free-rank-`p`/etale presentation at every finite
level, the `p=3` crosswalk to the reviewed `W2-SURVIVOR` including both
integer determinant representatives, and the inverse-limit analysis: the
tower's coefficientwise limit is the restricted power series
`(x-x^p, y·S_∞(x))` with `S_∞ = Σ_{j≥0} p^j x^{j(p-1)} = (1-px^{p-1})^{-1}`
in `Z_p⟨x⟩`, an element of `Z_p⟨x,y⟩^2` and not of `Z_p[x,y]^2`, with exact
Jacobian one, persisting collision, and finite etale rank `p` in the
restricted-analytic category.  300/300 machine checks pass
(`p ∈ {3,5,7,11}`, `n ≤ 6`, plus brute-force fibers, Teichmuller,
truncation-convergence, and crosswalk checks); the general-`(p,n)` statements
are closed by the hand proofs in §4 below.  The interpretation boundary is
honest and correctly excludes every forbidden stronger reading.  All five
pinned artifact hashes verify; all three prior-art citations are
line-accurate; my own repository-wide dedup found no prior occurrence of the
tower or its rational/Tate limit.  Caveats C1–C6 are non-blocking; none
touches a claim clause.

**Ledger guidance.**  The upstream dependency is discharged:
`xmodel/review-witt-oddprime-claude.md` returned **CONFIRMED** at
2026-08-24T03:09Z, so the control's conditional lineage is now unconditional.
Subject to the coordinator resolving the governance point in C3, this result
**may enter the scoped audit ledger** at exactly the stated tier, as a *new,
separate* control entry — an unrestricted-support all-Witt Artin--Schreier
tower with nonpolynomial rational/restricted-analytic inverse limit — and not
as an amendment widening the `W2-SURVIVOR` entry.  Required boundary language
for the entry: support/degree grow linearly in `n`; the limit lies in
`Z_p⟨x,y⟩`, not `Z_p[x,y]`; NOT SHOWN: any bounded-support or uniformly
bounded-degree tower, any `Z_p`/characteristic-zero *polynomial* lift, any
germ, any complex/algebraic-category statement, any JC2 counterexample, and
no impossibility theorem about *other* lifts of the same special fibre.  The
existing `AUDIT.md:850` entry's "NOT SHOWN: no `W_3` …" list remains true of
the `W_2` case artifacts themselves; the new entry should cross-reference it
rather than edit it (a `W_n` lift for every `n` IS now shown, by closed form,
with grown support).  This reviewer edited no ledger.

---

## 1. Reviewer identity, environment, perimeter

- Reviewer: Claude Fable 5 (model id `claude-fable-5`), Anthropic Claude Code
  session, independent of the OpenAI Codex producer session and of the
  internal checker the producer used.
- Host: macOS (Darwin 23.6.0), zsh, Python 3.9.6, stdlib only.  No network,
  no remote machines, no CAS/solver of any kind (pure sparse-dict polynomial
  arithmetic written for this review).
- Basis: `git rev-parse HEAD = 8bf25a52f5f6c20886b77c6d9aeeb879eb18f8e4`,
  equal to the report's basis commit.  Working tree carries the known dirty
  coordination perimeter (`APPROACHES.md`, `AUDIT.md`, `COORDINATION.md`,
  `PROGRESS.md`, untracked round-1/round-2 artifacts); relevant rows are
  examined in §5/C6.
- Writes by this review: this file only.  Scratch work in `/tmp/wtc_audit/`
  (outside the repository); the checker script is transcribed by hash below.

## 2. Exact commands and calculations

```text
shasum -a 256 cases/round2_witt_oddprime/PREREGISTRATION.md \
  xmodel/round2-witt-oddprime-20260824.md \
  cases/round2_witt_oddprime/results.json \
  cases/round2_witt_oddprime/replay.json \
  xmodel/review-witt-oddprime-claude-prompt.md      # 5/5 match report table
git rev-parse HEAD                                   # = 8bf25a5... (matches)
python3 /tmp/wtc_audit/check.py                      # 300 PASS, 0 FAIL
# check.py SHA-256:
#   2a35db110537b63bbba7747d1a58ec183c010eb084b227d61f101d8b09fa2f5f
# dedup greps (repo-wide, excluding the target report and this review):
grep -rn -iE "tate algebra|restricted power|restricted-analytic" .
grep -rn -iE "geometric series|inverse limit|varprojlim|all-Witt" .
grep -rn -E  "1-px|px\^\{?p-1|p\^j x|x\^\{j\(p-1\)\}" .
```

The checker verifies, with independent Jacobian/derivative code and exact
integer arithmetic: for `p ∈ {3,5,7,11}`, `n = 1..6` (11 checks each): the
exact `Z[x]` determinant identity (1.2), determinant `= 1` in `Z/p^n`,
`S_m ≡ S_n (mod p^n)` for **all** `n ≤ m ≤ 7` (not just adjacent levels), the
marked collision with distinct sources, exact support/degree/valuation claims
(3.1)–(3.3), the presentation identities of (1.6)
(`x^p - x + (x-x^p) = 0` over `Z`; `Q_n·(1-px^{p-1}) ≡ y`;
`(px^{p-1}-1)·(-S_n) ≡ 1`), and the finite resummation
`(1-px^{p-1})S_n = 1 - p^n x^{n(p-1)}` over `Z`.  Additionally: brute-force
fibers of `F_n` over `(0,0)` on all of `(Z/p^n)^2` for
`(p,n) ∈ {(3,1),(3,2),(3,3),(5,1),(5,2)}` — each equals exactly the `p`
Teichmuller points `{(τ,0): τ^p = τ}`, containing `(0,0)` and `(1,0)`;
`S_n` is a unit at every point; the `p=3` crosswalk (maps equal mod 9;
producer representative determinant exactly `1+27x^2+72x^4` over `Z`);
`[−1] = −1` is the unique Artin--Schreier-fixed lift of `−1` in `Z/p^n` for
`p ∈ {3,5,7}`, `n ≤ 4`; truncation stability `S_N ≡ S_n (mod p^n)` for all
`N ≤ 9`; and the factorization `F_n = (x-x^p, y) ∘ (x, y·S_n(x))`.

## 3. Clause-by-clause findings

- **(1.1) and indexing.**  `W_n(F_p) ≅ Z/p^n` with the length-`n` convention
  (`W_1 = F_p`) is standard, matches the upstream case's `W_2(F_3) = Z/9`,
  and Witt truncation is reduction mod `p^n` under this identification
  (`V^n W(F_p) = p^n Z_p`).  `S_1 = 1`, so the `n=1` base is exactly the
  reviewed Artin--Schreier special fibre `(x-x^p, y)`; the `n=2` member is
  exactly the reviewed `W_2` lift (§2 crosswalk).  No off-by-one.  **Holds.**
- **(1.2)–(1.3) determinant.**  `∂P/∂y = 0`, so the Jacobian is
  `(1-px^{p-1})·S_n(x)`; with `z = px^{p-1}`, telescoping gives `1 - z^n =
  1 - p^n x^{n(p-1)}` as an identity in `Z[x]` (machine-confirmed for 24
  `(p,n)` pairs), hence exactly `1` in `(Z/p^n)[x,y]` where `p^n = 0`.  The
  report correctly distinguishes the integer representative from the ring
  element.  **Holds.**
- **(1.4) compatibility.**  `S_m - S_n = Σ_{j=n}^{m-1} p^j x^{j(p-1)}` has
  every coefficient divisible by `p^n`; the first coordinate has fixed
  integer coefficients.  So `F_m mod p^n = F_n` for all `m ≥ n` — one
  compatible tower, verified at all sampled level pairs.  **Holds.**
- **(1.5) collision.**  `(0,0) ≠ (1,0)` in every `R_n`; `0-0^p = 1-1^p = 0`
  and `Q_n ∈ (y)`.  Constant sections, no moving points.  Brute force gives
  the stronger fact: the full fiber over `(0,0)` is exactly the `p`
  Teichmuller points `(τ,0)` at every sampled level (because `S_n ≡ 1 mod p`
  is a unit at every point, forcing `y = 0`, and `x^p = x` picks out the `p`
  Teichmuller roots in `Z/p^n`).  **Holds.**
- **(1.6) finite-level presentation.**  The map
  `φ: R_n[U,V,X]/(X^p-X+U) → R_n[x,y]`, `X ↦ x`, `U ↦ x-x^p`, `V ↦ yS_n(x)`
  is well defined (`x^p - x + (x-x^p) = 0` exactly over `Z`) and has inverse
  `x ↦ X`, `y ↦ V(1-pX^{p-1})`: both composites are the identity because
  `S_n·(1-px^{p-1}) = 1 - p^n x^{n(p-1)} = 1` in `R_n[x]` (machine-checked).
  The quotient is free over `R_n[U,V]` with basis `1, X, …, X^{p-1}` (monic
  degree-`p` division), so `F_n^*` is finite **free** of rank `p`; and it is
  standard-etale since `∂/∂X(X^p-X+U) = pX^{p-1}-1` is a unit with explicit
  inverse `-S_n(X)` (machine-checked).  The report's care that this is a
  module-rank statement over the non-domain `R_n`, not a generic-degree
  computation, is exactly right.  **Holds.**
- **(§2) crosswalk.**  `F_2 = (x-x^3, y+3x^2y)` equals the producer's
  `(x+8x^3, y+3x^2y)` coefficientwise mod 9 (`-1 ≡ 8`); the two *integer*
  representatives have different exact determinants — `1-9x^4` for `x-x^3`,
  `1+27x^2+72x^4` for `x+8x^3` (both recomputed exactly over `Z`) — and both
  are `1` mod 9.  The report states this represenative-dependence correctly.
  `[−1] = −1` as Teichmuller lift for odd `p` verified (unique
  Artin--Schreier-fixed lift; `= 8` in `Z/9`, matching the upstream `[2]`).
  **Holds.**
- **(§3) support/degree growth.**  `supp(Q_n) = {(j(p-1),1): 0 ≤ j < n}`
  exactly (`p^j ≠ 0` in `Z/p^n` iff `j < n`), `n` monomials, `deg Q_n =
  (n-1)(p-1)+1`, `deg F_n = max{p, (n-1)(p-1)+1}` (`= p` for `n = 1,2`, then
  linear growth), and the `j`th coefficient has exact valuation `j` — all
  machine-verified.  The unbounded-support feature is real and load-bearing.
  **Holds.**
- **(§4) inverse limit.**  All five sub-claims verified; proofs in §4 below.
  `varprojlim_n (Z/p^n)[x,y] ≅ Z_p⟨x,y⟩` (the `p`-adic completion of
  `Z[x,y]`), membership `S_∞ ∈ Z_p⟨x⟩` (valuations `j → ∞`), the resummation
  `(4.1)` with the denominator a unit of the *integral* Tate algebra and a
  unit at every point of the closed disc (`≡ 1 mod p`), exact Jacobian one
  `(4.3)`, persisting collision, finite etale rank `p` in the
  restricted-analytic category, NOT an everywhere-defined algebraic
  endomorphism of `A^2` (nonempty pole divisor at `|x| = p^{1/(p-1)} > 1`),
  and nonpolynomiality (infinitely many nonzero coefficients in the
  characteristic-zero domain `Z_p`; equivalently `Z_p[x]^× = Z_p^×` excludes
  the nonconstant denominator).  **Holds.**
- **(§5) interpretation boundary.**  The three negative statements are
  exactly what the identities prove; statement 3 is correctly scoped to *this
  tower's* formal limit, with the alternative-lift question explicitly left
  open; the do-not-refute list (fixed-support/degree-bound theorems,
  algebraization lemmas, other lifts, the char-2 Mondello stratum, JC2 over
  any characteristic-zero field) is correct — in particular the char-2
  Mondello obstruction is support-stratum-specific (`AUDIT.md:839`), and the
  Artin--Schreier support is not in that stratum, so no tension exists.  The
  refusal to call the noninjective det-1 restricted-analytic limit a JC2
  counterexample is correct: JC2 is a polynomial-category statement.
  **Holds.**
- **(§6) dedup/provenance.**  All three citations line-accurate
  (`sol-pcurvature.md:136-149` special fibre control;
  `review-round1-proof-gates-claude.md:302-306` char-`p` warning;
  `round2-witt-oddprime-20260824.md:8-61` and `:149-163` `W_2`-only scope).
  Hash table 5/5 verified against disk.  My independent greps (§2) found the
  tower/limit formulas nowhere else: the only hits are coordination rows
  about this very provisional result in the dirty `PROGRESS.md:118-122` /
  `APPROACHES.md:71,124` and the unrelated namespaces `sol-wtc1*.md` ("WTC-1"
  is a pencil-center packet arrow, not Witt/Tate) and `cases/tower_check.py`/
  `cases/towers/` (a `(9,15,7,3)` certificate, different mathematics);
  `cases/witt_check.py` is the char-2 engine exactly as described.  The idea
  seed is carded in the producer's own frozen blind submission
  (`ideation-20260824T0156Z-bacon.md:112`, "an odd-prime Witt survivor with
  an all-level lift"), so the lineage is as declared.  **Holds**, with the
  provenance incompleteness recorded as C1.

## 4. Reviewer's general-`(p,n)` proofs (closing the sampled gap)

Machine checks sample `(p,n)`; the claims are for all odd `p` and all `n`.
The following complete the audit.

1. **Determinant.**  `(1-z)(1+z+⋯+z^{n-1}) = 1-z^n` in `Z[z]`; substitute
   `z = px^{p-1}`.  With `∂P/∂y = 0` the Jacobian is the product above, so
   `[P_n,Q_n] = 1 - p^n x^{n(p-1)}` in `Z[x]` and `= 1` in `R_n[x,y]`.
2. **Compatibility.**  Coefficientwise: every dropped tail term of
   `S_m - S_n` carries `p^j`, `j ≥ n`.
3. **Limit ring.**  An element of `varprojlim (Z/p^n)[x,y]` is a coefficient
   family `c_α ∈ varprojlim Z/p^n = Z_p` such that each finite level is a
   polynomial, i.e. for every `n` only finitely many `c_α ∉ p^nZ_p`.  That
   is precisely the restricted condition `c_α → 0`, so the limit is
   `Z_p⟨x,y⟩`, the `p`-adic completion of `Z[x,y]`.  The tower's limit has
   `c_{(j(p-1),1)} = p^j` and is `(x-x^p, yS_∞)`; `F_∞ mod p^n = F_n` since
   the tail vanishes mod `p^n`.
4. **Resummation and units.**  `‖px^{p-1}‖_Gauss = 1/p < 1`, and the exact
   identity `(1-px^{p-1})S_N = 1-p^Nx^{N(p-1)}` (machine-checked over `Z`)
   has right side `→ 1` in Gauss norm, so `S_∞ = (1-px^{p-1})^{-1}` in
   `Z_p⟨x⟩`; the inverse is *integral* (coefficients `p^j ∈ Z_p`), so the
   denominator is a unit of `Z_p⟨x⟩`, and at every `x ∈ Z_p` its value is
   `≡ 1 mod p`, a unit of `Z_p` — no pole on the disc, in particular at the
   marked points (values `1` and `1-p`).  Jacobian of `F_∞`:
   `(1-px^{p-1})·S_∞ = 1` exactly.  Collision: `y = 0` kills the second
   coordinate; `1-1^p = 0`.
5. **Finite etale rank `p` at the limit.**  `g = X^p - X + U` is monic with
   norm-`≤1` coefficients, so division works in `Z_p⟨U,V⟩⟨X⟩`: dividing each
   `X^m` by `g` over `Z[U]` gives integer-coefficient quotient/remainder of
   Gauss norm `≤ 1`, and for a restricted series the sums converge; the
   remainder is unique (reduce a relation `qg + r = 0`, `deg r < p`, mod
   `p^k` and compare top `X`-degrees against the monic leading term).  Hence
   `Z_p⟨U,V,X⟩/(g)` is free over `Z_p⟨U,V⟩` with basis `1,…,X^{p-1}`.  The
   map to `Z_p⟨x,y⟩` (`X ↦ x`, `U ↦ x-x^p`, `V ↦ yS_∞`) is surjective
   (substitute `f(x,y) ↦ f(X, V(1-pX^{p-1}))`, using `S_∞(1-px^{p-1}) = 1`)
   with kernel exactly `(g)`: a remainder `Σ_{i<p} r_i(U,V)x^i = 0` reduces
   mod `p` to a relation over `F_p[U,V]` where `S̄_∞ = 1`, and `F_p[x,y]` is
   free over `F_p[x-x^p, y]` on `1,…,x^{p-1}` (`deg_x(u^d x^i) = pd+i` is
   injective on `(d,i)`), so each `r̄_i = 0` (the fibre map `U ↦ x-x^p,
   V ↦ y` is injective by algebraic independence); torsion-freeness and
   `p`-adic separatedness then force `r_i = 0`.  So `F_∞^*` is finite free
   of rank `p`, and standard-etale since `g' = pX^{p-1}-1 = -(1-pX^{p-1})`
   is a unit.  All three assignments have norm `≤ 1`, so `F_∞` is a genuine
   endomorphism of the closed unit bidisc, as claimed — and the same
   rational expression is undefined on the algebraic divisor
   `1-px^{p-1} = 0`, which is nonempty over `Q̄_p` (roots have
   `|x| = p^{1/(p-1)} > 1`, off the disc), so it is *not* an endomorphism of
   affine two-space.  Exactly the report's category split.
6. **Nonpolynomiality is robust.**  `S_∞` has infinitely many nonzero
   coefficients in the domain `Z_p`, so `F_∞ ∉ Z_p[x,y]^2`.  Stronger (my
   check of the "hidden polynomial" attack): if `β ∘ F_∞ ∘ α` were
   polynomial for *polynomial* automorphisms `α, β` of `A^2_{Z_p}`, then
   `F_∞ = β^{-1} ∘ (poly) ∘ α^{-1}` would itself be polynomial —
   contradiction.  The only way to reach a polynomial is the *analytic*
   twist: `F_∞ = (x-x^p, y) ∘ (x, yS_∞(x))`, whose twist factor has
   determinant `S_∞ ≠ 1`.  So the nonpolynomiality of the limit is not a
   coordinate artifact within the determinant-one polynomial world; the
   report's claim survives the strongest reading I could mount (see O1).

## 5. Provenance and deduplication findings

1. Pinned artifacts: 5/5 SHA-256 match (`PREREGISTRATION.md`,
   `round2-witt-oddprime-20260824.md`, `results.json`, `replay.json`,
   `review-witt-oddprime-claude-prompt.md`).  Basis commit = current `HEAD`.
2. Upstream lifecycle: `xmodel/review-witt-oddprime-claude.md` — verdict
   **CONFIRMED**, executed 03:02–03:09Z, essentially simultaneous with the
   control's 03:07:57Z stamp.  The control's "remains under independent
   Claude review" was true at writing and is now stale in the favorable
   direction (C2).
3. Dedup: the compatible tower `(1.1)`, the exact determinant `(1.2)`, the
   support law `(3.1)`, the limit `(4.2)`, and the resummation `(4.1)` occur
   nowhere in the repository outside the target report and coordination rows
   that describe it.  The special fibre `(x-x^p,y)` and the `p=3` `W_2` lift
   are prior art, exactly as the report says.  Name collisions ("WTC-1",
   `tower_check.py`, `towers/`) are unrelated mathematics — verified by
   reading their headers.
4. Conceptual precedent (the substance of C1): `xmodel/sol-witt.md` §6
   (char-2 lane; also mirrored in `dist/jc72108-theory-bundle-v1/`) already
   required, for any char-0 seed, "one fixed finite coefficient support, or
   another proof that the inverse limit is polynomial rather than a formal
   power series," and warned that solutions "at every finite precision,
   growing supports" prove nothing.  The control is the first *explicit
   witness* realizing that warned-about escape (for odd `p`, with the exact
   rational form); the phenomenon-type was already registered campaign
   doctrine.  The report's novelty claim ("the closed-form compatible tower
   and its rational/Tate limit are new to the repository; the underlying
   special fibre and first lift are not") is accurate as stated, but §6
   should cite `sol-witt.md` §6 as the prior statement of the criterion.

## 6. Attack log (all negative)

1. **Indexing/off-by-one** — length-`n` Witt convention, truncation-vs-mod,
   `S_1 = 1` base, `n=2` crosswalk: all consistent; the tower interpolates
   exactly the two reviewed objects.  Negative.
2. **Representative confusion** — computed both integer determinant
   representatives (`1-9x^4` vs `1+27x^2+72x^4`); they differ over `Z`,
   agree mod 9; the report says precisely this and never leans on a
   representative-dependent quantity.  Negative.
3. **Telescoping error / hidden mod step** — determinant identity verified
   exactly over `Z[x]` at 24 `(p,n)` pairs and proved for all `(p,n)`.
   Negative.
4. **Adjacent-only compatibility** — checked all level pairs `n ≤ m ≤ 7-9`;
   any-to-any reduction holds.  Negative.
5. **Collision fragility / moving points** — constant sections, distinct at
   every level; brute-forced *entire* fibers, finding exactly the `p`
   Teichmuller preimages, a stronger fact than claimed.  Negative.
6. **Support undercount at high `n`** — exact valuation of every coefficient
   confirmed (`p^j` survives in `Z/p^n` iff `j < n`); no silent vanishing.
   Negative.
7. **Limit-object misidentification** — attacked whether the limit should be
   `Z_p[[x,y]]` or `Z_p[x,y]`: the per-precision finite-support condition
   characterizes exactly `Z_p⟨x,y⟩`; `S_∞` is restricted (valuations `→ ∞`)
   and not polynomial.  Negative.
8. **Denominator not a unit / pole at marked points** — inverse exhibited
   *inside* `Z_p⟨x⟩`; value `≡ 1 mod p` at every disc point; values `1`,
   `1-p` at the marked points.  Conversely confirmed the pole divisor is
   nonempty off the disc, validating the algebraic/analytic split rather
   than contradicting it.  Negative.
9. **Finite/etale/rank-`p` at the limit** — rebuilt the presentation via
   division by the monic distinguished `X^p-X+U` with a mod-`p`
   independence lift; unit derivative `-(1-pX^{p-1})`; norms `≤ 1` so the
   map is a genuine bidisc endomorphism.  Negative.
10. **Hidden-polynomial reading** — the limit is polynomial only up to the
    *analytic* unit twist `(x, yS_∞)`; no polynomial-automorphism
    conjugation can make it polynomial (§4.6).  The report claims only what
    survives.  Negative.
11. **Scope inflation** — searched the report for bounded-support,
    impossibility, complex-map, or JC2 readings: none present; §5's
    exclusion list is complete and correct, including the char-2 Mondello
    stratum (different support stratum, no contradiction) and the
    other-lift question (explicitly open).  Negative.
12. **Provenance/dedup fabrication** — hashes, basis commit, citation line
    ranges, and my own independent grep sweep all consistent; idea seed
    present in the producer's frozen ideation card.  Negative (C1 records
    the one uncited conceptual precedent).
13. **Governance** — see C3; the report's own discipline (explicit
    PROVISIONAL label, standalone algebra, no promotion, no ledger edit, no
    search/enumeration/solver) conforms to the one-provisional-descendant
    allowance in `ideation-20260824T0156Z-synthesis.md:200-206`.  Negative
    as to the report's conduct; one open adjudication for the coordinator.

## 7. Caveats and observations (non-blocking)

- **C1 (smallest worthwhile correction).**  §6 omits the closest in-repo
  conceptual precedent: `xmodel/sol-witt.md` §6 already stated the
  fixed-support-or-nonpolynomial-limit criterion this control witnesses.
  Add the citation.  No claim clause is affected (the tower and formulas are
  genuinely new); this is provenance completeness only.
- **C2.**  The status block is now stale in the favorable direction: the
  upstream review returned CONFIRMED at 03:09Z.  The conditional-lineage
  sentence is discharged; only this review remained as the promotion gate.
- **C3 (coordinator adjudication requested).**  The round-2 synthesis
  simultaneously (a) hard-stops the W root at "no `W3`/support expansion"
  in the same generation (`:198`, `:156-158`) and (b) permits exactly one
  explicitly-PROVISIONAL descendant of a producer-checked result
  (`:200-206`), which this report claims to be.  The upstream review's
  guidance "any `W_3` attempt is a new preregistered cap" targets
  *enumerative* caps (preregistration protects searches; a closed-form
  identity note has no search space to cherry-pick).  This reviewer finds
  the report's reading defensible and its conduct clean, but the tension
  should be resolved explicitly in the next `LIVE STATE` when banking; the
  entry should be typed as a closed-form negative control descended from
  the survivor, not as a continuation of the W enumeration lane.
- **C4.**  The identities are prime-agnostic; only the sentence
  interpreting `-1` as a Teichmuller lift needs `p` odd (at `p=2`,
  `[1] = 1 ≠ -1` in `Z/4`).  The odd-`p` restriction is inherited lineage
  framing, not mathematical necessity; nothing in the report asserts a
  `p=2` failure, and the char-2 Mondello theorem lives on a different
  support stratum either way.
- **O1 (observation, strengthens the control).**  `F_n = (x-x^p, y) ∘
  (x, yS_n(x))` at every level: the tower is the unit-twist of the constant
  Artin--Schreier tower, and the determinant-one normalization is exactly
  what forces the geometric series into the second coordinate.  This makes
  the mechanism transparent and shows the analytic escape is the *generic*
  outcome of det-normalizing a non-etale-trivial constant family.
- **C6.**  The dirty working tree carries coordination rows describing this
  provisional result (`PROGRESS.md:118-122`, `APPROACHES.md:71,124,191`);
  their language is correctly bounded ("provisional", "nonpolynomial
  rational/restricted-analytic limit").  Uncommitted edits cannot be
  attributed to sessions from the tree alone; nothing here contradicts the
  producer's "no shared-ledger edit" method claim, which concerns its own
  session.

## 8. Precise campaign consequence

Confirmed, at the stated tier, the control establishes exactly:

1. The odd-prime Artin--Schreier survivor seed admits an explicit compatible
   determinant-one Keller-collision lift at **every** finite Witt level once
   support may grow — so no later finite unrestricted-support Witt
   obstruction can kill this seed, and `W_2` survival was the last
   obstruction-type event available to the unrestricted lane.
2. All-Witt compatibility (with exact determinant one and a persisting
   marked collision at every level) does **not** algebraize: the tower's own
   inverse limit lies in `Z_p⟨x,y⟩ \ Z_p[x,y]`.  Any future route from Witt
   towers to a characteristic-zero polynomial counterexample must therefore
   carry a uniform support/degree (or equivalent finiteness) hypothesis —
   this control is the standing witness that the hypothesis is not
   removable.  Avenue 19's redesign direction ("uniform polynomial
   complexity or a different lift") is now provably the only direction.
3. The campaign gains a clean category-boundary control: a noninjective,
   determinant-one, finite etale rank-`p` restricted-analytic endomorphism
   of the `p`-adic bidisc — Jacobian-conjecture-style inference fails in the
   restricted-analytic category, so any future "analytic continuation" or
   completion argument must show its output is polynomial before invoking
   JC-category facts.

What it does not change: no bounded-support/degree tower exists or is
excluded; no `Z_p`, `Q_p`, `Q`, or `C` polynomial statement of any kind; the
char-2 Mondello promotion, all fixed-support theorems, and the JC2 problem
itself are untouched.

## 9. Scope restated

Confirmed exactly and only: for every odd prime `p` and every `n ≥ 1`, the
displayed `F_n` over `W_n(F_p) = Z/p^n` form one reduction-compatible tower
with exact integer determinant `1 - p^n x^{n(p-1)}` (hence determinant one at
every level), fixed distinct marked sources `(0,0), (1,0)` colliding at
`(0,0)` at every level, exactly `n` second-coordinate monomials of exact
valuations `0,…,n-1` and degree `(n-1)(p-1)+1`, finite free rank-`p` etale
finite-level presentations, and coefficientwise inverse limit
`(x-x^p, y/(1-px^{p-1}))` — a restricted-analytic, rational, nonpolynomial,
noninjective, determinant-one, finite etale rank-`p` endomorphism of the
closed `p`-adic unit bidisc over `Z_p`.  Nothing beyond this tier is
asserted or licensed.
