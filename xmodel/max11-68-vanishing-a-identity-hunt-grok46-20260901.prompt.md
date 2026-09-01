# Research lane: hunt the missing exact identity for the 68 vanishing-A chamber

Bounded primary research lane (paper mathematics; read-only). The `q=0`
vanishing-A chamber of the max11 `(6,8)` scale-zero endpoint system is
genuinely open at the current constraint level (elimination count in
`xmodel/max11-68-vanishing-a-elimination-count-grok46-20260831.md`:
expected dimension ~19m; no landed family flips it). The sibling Fce-zero
terminal branch fell only when the H-descent/U-profile identities were
*derived* — new exact structure, invisible to constraint counting. Your
task: hunt the analogous new identity for this chamber.

## Frozen input

Read at current `origin/master` of `dcposch/jc2-lean`, `max11-partial-y/`:
the committed vanishing-A jet (`Grok68QZeroVanishingAJetScratch.lean`),
both count/induction reports in `xmodel/`, the committed terminal-branch
suite (H-descent `..._H_quotient68`, U-profile, V-descent, square fiber —
study HOW those were originally derived from the row system: what
generating manipulation produced `4H − C(C0) = BT`), and the producing
companion/discriminant/I4 modules of the q=0 branch.

Chamber state (wall `9N=7S`, `N=7m`, `Fce_0 ≠ 0`, matching through k=3):
`A = A_p X^p + s` (`deg s ≤ 14m−4`), `c = λX^N B + r_c` (`deg r_c ≤ 10m−4`),
`e = −λX^N d + r_e` (`deg r_e ≤ 15m−4`), I4 identity
`B r_e + r_c d = (1/9)B³ − (3/2)γd − (3/4)εB + C(Fce_0)`, cusp top
`A_p B_D² + 3c_{Cc}² = 0`, resultant `4B_D²c_{Cc} + 9d_V² = 0`, Δ-jets
`k ≤ 4m`, `J = Bc² − (1/9)AB³ − 3de` with `deg J ≤ 14m`.

## Hunt directions (attack in order, deviate freely)

1. **H-analogue.** The terminal branch's H = 4B²c + 9d² satisfied an exact
   descent 4H − C(C0) = BT. Look for the q=0 analogue: combinations like
   `B·r_e + r_c·d` (already = the I4 right side), `9d² + 4B²·(c-part)`,
   or `J`-like mixtures whose derivative or whose product with B',d
   telescopes against the row system into `B·(quotient) + constant`.
   The key move in the terminal derivation was pairing the row identity
   with the DERIVATIVE of a squared/quadratic form — try d/dX of the I4
   identity paired with the Δ-jet generating function.
2. **Fce_0-charged descent.** This chamber's distinguishing scalar is
   `Fce_0 ≠ 0` (the terminal had `terminal ≠ 0`). Hunt an identity where
   `C(Fce_0)` plays the role `C(C0)` played: something = `B·T' + C(c·Fce_0)`
   would immediately enable the two-case degree kill. Candidate: apply the
   Euclidean division of `(1/9)B³ − (3/2)γd − (3/4)εB + C(Fce_0)` by `B`
   inside the I4 identity and chase the remainder `−(3/2)γd + ...` against
   `d² ≡`-type relations if any exist on this branch (does the q=0 branch
   have a square-fiber analogue? derive one if the rows permit).
3. **Wronskian/second symmetric object.** `J` has a degree DROP
   (≤14m vs naive 23m). Degree-drop objects encode identities: compute
   what the drop forces coefficientwise beyond the recorded top, and
   whether `Wr(c, B)` or `Wr(e, d)` inherits a descent from the matching.
4. **Negative result.** If every route fails, characterize the obstruction:
   exhibit the smallest consistent model (concrete m=1 numerical solution
   of the full landed system, via exact arithmetic) — an actual model
   would prove the chamber cannot close without new ROWS (not identities),
   redirecting the campaign to deeper jets.

## Report

`xmodel/max11-68-vanishing-a-identity-hunt-grok46-20260901.md`, verdict
`DERIVED`/`PARTIAL`/`BLOCKED`, all computations shown, UNVERIFIED labels
where sources could not be read. A concrete m=1 model, if found, must be
exact (integer/rational arithmetic) and fully displayed. No overclaims.
