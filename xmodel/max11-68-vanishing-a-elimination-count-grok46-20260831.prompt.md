# Research lane: elimination count for the 68 vanishing-A chamber

Bounded primary research lane (paper mathematics; read-only). Execute the
calculation that `xmodel/max11-68-vanishing-a-uniform-induction-grok46-20260831.md`
§3.4 declined: count the unused constraints against the unmatched
coefficients in the `q=0` vanishing-A chamber of the max11 `(6,8)`
scale-zero endpoint system, and determine whether the chamber is empty,
finite-dimensional, or genuinely open.

## Frozen input

Read the committed modules at current `origin/master` of `dcposch/jc2-lean`,
`max11-partial-y/` (the vanishing-A jet and the induction report's §0-§2 are
now committed as `Grok68QZeroVanishingAJetScratch.lean` plus the report
itself in `xmodel/`). On the wall `9N=7S`, `N=7m`: after matching through
`k=3`,

- `Fce = C(Fce_0)`, `Fce_0 ≠ 0`;
- `A = A_p X^p + s`, `deg s ≤ 14m-4`;
- `c = λ X^N B + r_c`, `deg r_c ≤ 10m-4`;
- `e = -λ X^N d + r_e`, `deg r_e ≤ 15m-4`;
- unused Δ-jets `Δ_{U-k} = 0` for `k = 4..4m`; the `k=4` instance is
  `A_{p-4} B_D + 6λ (r_c)_{Cc-4} = 0`;
- the I4 identity `(∗)`: `B r_e + r_c d = (1/9)B³ - (3/2)γ d - (3/4)ε B + C(Fce_0)`;
- cusp top `A_p B_D² + 3 c_{Cc}² = 0`, top resultant `4 B_D² c_{Cc} + 9 d_V² = 0`;
- `J := B c² - (1/9)A B³ - 3 d e` with `deg J ≤ p = 14m`.

## Task

1. Enumerate ALL constraint families on the free coefficient spaces
   (`s`: 14m-3 coefficients, `r_c`: 10m-3, `r_e`: 15m-3, `d`: 8m+1, `B`:
   3m+1, plus scalars): the Δ-jets `k=4..4m`, the coefficientwise content
   of `(∗)` (degree-by-degree: which coefficients of both sides match
   automatically, which are constraints), the `deg J ≤ 14m` conditions
   (coefficients 14m+1..23m of J vanish — how many are independent after
   the known top cancellation), and any other landed families.
2. Count: constraints minus unknowns as a function of m. If the count is
   favorable, identify the structure needed to convert the count into
   emptiness (the relations are polynomial, not linear — look for a
   triangular/elimination order in which each constraint pins one new
   coefficient, the way the jet matching pinned `B/c` matching rows).
3. If a triangular elimination exists, derive the endgame: the final
   pinned relation should collide with `Fce_0 ≠ 0` or an exact top
   coefficient. If the count is unfavorable, say which new constraint
   family (a deeper jet, a second I4-like identity) would flip it.

## Report

`xmodel/max11-68-vanishing-a-elimination-count-grok46-20260831.md`, verdict
`DERIVED`/`PARTIAL`/`BLOCKED`, all computations shown, UNVERIFIED labels
where sources could not be read. No overclaims.
