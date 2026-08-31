# Research lane: all-orders jet matching in the 68 q=0 vanishing-A chamber

You are a bounded primary research lane (paper mathematics; read-only on the
repository; no edits outside your lane workspace). Derive, or refute, the
all-orders extension of the jet-matching pattern in the `q=0` vanishing-A
chamber of the max11 `(6,8)` scale-zero endpoint system, and if it extends,
derive the closing contradiction.

## Frozen input

Read these kernel-checked modules in `jc2-lean/max11-partial-y/` (all green):

- `Grok68QZeroVanishingAJetScratch.lean` (SHA
  `b567d6987263468f206347bbd74f16d3605ac3febec40f53aed92e97ec410e17`):
  on the wall `9N=7S` with `Fce.coeff 0 ≠ 0` and the vanishing rows
  `A_(2N-1)=A_(2N-2)=A_(2N-3)=0`, the landed identities are
  `c_Cc B_(D-k) - B_D c_(Cc-k) = 0` and
  `B_D e_(E-k) + c_Cc d_(V-k) = 0` for `k=1,2,3`, with the degree drops
  `deg(c_Cc X^n B - B_D c) ≤ Cc-4` (for the appropriate power shift `n`)
  and `deg(B_D e + c_Cc X^m d) ≤ E-4`. Residual Prop:
  `FiveToSixCuspZetaFirstB3EqualitySupportQZeroVanishingAJetResidual68`.
- `Sol68...QZeroCompanionThirdReductionScratch.lean` (`third_companion_split68`)
  — the producing split; study how each discriminant/companion jet row is
  generated from one vanishing `A` row.
- The closed-sibling patterns for endgames:
  `Grok68TerminalBranchClosureScratch.lean` (exact identity + two-case degree
  comparison) and the strict-B3/sparse-endpoint closures.

## Questions, in order

1. **Uniformity.** Is the argument that produces row `k` of the matching
   (`c_Cc B_(D-k) = B_D c_(Cc-k)`) from the vanishing row `A_(2N-k)` uniform
   in `k`? Exhibit the exact recurrence: which discriminant/companion jet at
   order `k` is used, what other rows enter, and whether any denominator or
   side condition can fail at some `k` (e.g. at `k = D`, when `B` runs out of
   coefficients, or where the `I4` compensation degenerates).
2. **All-orders consequence.** If uniform through `k = D` (or through
   whatever bound the recurrence honestly supports), conclude the exact
   proportionality statement: `c_Cc · X^{Cc-D} · B = B_D · c` plus remainder
   of controlled degree, equivalently `B ∣ c` up to the shift — state it
   exactly. Similarly for the `e`/`d` incidence.
3. **Endgame.** Feed the proportionality into the frozen packet's exact
   identities (the cusp equation, the `Fce.coeff 0 ≠ 0` condition, the
   terminal quotient `2c + C(3γ) = Bv` if it applies in this chamber, and
   the degree data) and derive `False`, in the style of the terminal-branch
   closure (exact identity, then degree comparison). If instead the
   proportionality is *consistent*, exhibit the surviving normal form as a
   sharply smaller residual (ideally a finite-dimensional family).
4. **If not uniform:** identify the exact first `k` where the recurrence
   breaks and what new input would be needed.

## Report

Write `xmodel/max11-68-vanishing-a-uniform-induction-grok46-20260831.md`
with verdict `DERIVED` (contradiction, referee-checkable), `PARTIAL`
(uniform recurrence + all-orders statement but no contradiction, or
contradiction modulo a stated gap), or `BLOCKED`. Show all computations;
label anything not verified from the Lean sources UNVERIFIED. No overclaims.
