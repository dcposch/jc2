# Max11 (6,8) balanced endgame after `2h=3g`

Independent derivation, 2026-08-28.  Algebra checked in
`cases/grok_balanced_endgame_cas_20260828.py` (SymPy).  Lean names are
from `max11-partial-y/LowScale68SecondaryResidualExtraction.lean` and
`LowScale68SecondaryResidualDescent.lean`.  No tracked file was modified.

## Standing data

Chamber: `0 < g < h < 2g`, `2h = 3g` (so `g` is even, `g ≥ 2`), `3g < n`,
characteristic zero.

Residual coordinates after `C = A²/3 + c` and `D = AB/3 + d`:

| poly | degree bound | top | nonvanishing |
|---|---|---|---|
| `A` | `2n` | `a` | `a ≠ 0` |
| `B` | `3n-g` | `b` | `b ≠ 0` |
| `c` | `4n-g` | `c` | `c ≠ 0` |
| `d` | `5n-h` | `d` | `d ≠ 0` |
| `e` | `6n-h` | `e` | `e ≠ 0` |

The selector already supplies all five nonvanishing statements together with
the middle-face discriminant.  Write `M₁₁ = 11n-3g`, `M₁₂ = 12n-3g`,
`M₁₃ = 13n-3g`, `M₁₄ = 14n-3g`.  All four are positive in `3g < n`.

Invariants (load-free residual forms):

```
Q  = B e + c d - B³/9          # I4 = (8/3) Q
I3 = (-8/9) A B d - (8/9) B² c + (8/3) c e + (4/3) d²
Disc = A B² + 3 c²
R  = -2 d Disc + 3 B d² - (4/3) B³ c
```

Lean already has `Q.natDegree < 9n-3g` and `I3.natDegree < 10n-3g` on this
chamber (quartic/cubic invariants plus the cubic-face load cutoffs), and
`R.natDegree < 13n-4g`.

## Given scalar relations

Middle incidence, *before* `B³` normalisation:

```
(I)   b e + c d = 0
(D)   a b² + 3 c² = 0
```

`(I)` is the `9n-g-h` face of `Be+cd`.  The `B³` term sits at `9n-3g`,
strictly lower by `g/2`.  After the quartic invariant one uses `Q` itself,
not `(I)`, as the polynomial object: `Q.natDegree < 9n-3g`.  For leading
`e` this is the same as `(I)`; the next term of `e` is `b²/9` at degree
`6n-2g`.

Row two on the coinciding cubic face `11n-3g-1`, already extracted in
`GrokRowTwoBalancedScratch.lean`:

```
(R2)  4 b c² - 9 d e = 0
```

Prefactor `(-8/27) M₁₁ ≠ 0`.  The `B² d` derivative is strictly below
because `g < h`.  Constant-Jacobian row-two loads are already below
`11n-3g-1`.

Cubic-defect balanced three-term face at `13n-4g`, already in
`secondaryResidualCubicDefect_balancedChamber68`:

```
(R)  -2 d δ + 3 b d² - (4/3) b³ c = 0,
     δ := Disc.coeff(8n-4g+h) = Disc.coeff(8n-5g/2),
     Disc.natDegree ≤ 8n-5g/2.
```

This is *not* a relation among the five tops alone.

## Scalar chart of `(I)+(D)+(R2)`

Solve in the `b ≠ 0` chart (the vanishing branch `c = 0` is excluded by
the selector):

```
e = - c d / b
c = - 9 d² / (4 b²)
e =   9 d³ / (4 b³)
a = - 243 d⁴ / (16 b⁶)
```

Equivalent pair of quadratics in `(b,c,d)`:

```
(R2')  4 b² c + 9 d² = 0     # (R2) after (I), using c ≠ 0
```

`(D)+(I)` imply the middle cubic-invariant face `-a b d + 3 c e = 0`
identically, as in `secondaryResidualBetweenFace68_classify`.

Cubic defect on this chart collapses to `δ = 3 b d`.  It forces the next
discriminant coefficient and does **not** contradict the tops.  Discard it
for the fastest route.

## High faces of rows one and zero vanish

Newton products, on `2h=3g`:

| row | high face | next (cubic) face | gap |
|---|---|---|---|
| one | `12n-g-h-1 = 12n-5g/2-1` | `12n-3g-1` | `g/2` |
| zero | `13n-g-h-1 = 13n-5g/2-1` | `13n-3g-1` | `g/2` |

Inner row one at the high face:

```
2 a (10n-g-h) (a b d - 3 c e) = 0
```

by the middle cubic invariant.  Inner row zero at the high face:

```
- 2n a² (b e + c d) = 0
```

by `(I)`.  Residual scalings `(-4/27)` and `(+4/27)` do not revive them.

Subleading of these high blocks *would* spill onto the cubic faces at gap
`g/2`.  That spill is removed by rewriting through `I3` and `Q` rather than
by a further Newton split.

## Identities (CAS-checked, polynomial)

Row-two `Q`-rewrite, already in Lean:

```
row2_body = -6 A Q' + 3 A' Q
          - 2 A B² B' - (2/3) A' B³
          + 6 (B² d)' + 6 (B c²)' - 18 (d e)'
```

Row-one high-block `I3`-rewrite (new):

```
2 A (A B d)' - 6 A (c e)'
  = 2 A ( -(9/8) I3' - (B² c)' + (3/2) (d²)' )
```

because `c e = (3/8) I3 + (1/3) A B d + (1/3) B² c - (1/2) d²`.  With
`I3.natDegree < 10n-3g`, the term `A I3'` has degree `< 12n-3g-1`.

Row-one / row-zero `Q`-substitution (clear denominators `B³`, `B` rather
than dividing in Lean): every remaining `e` is
`(Q - c d + B³/9)`.  Each `Q`-summand then has degree `≤ 12n-3g-2` or
`≤ 13n-3g-2` respectively.

After both rewrites the cubic-face coefficients depend only on the five
tops and on the two-term leading of `e = b²/9 - c d/b`.

## Cubic-face scalars

On `(D)` and two-term `e` (i.e. `(I)` plus `Q` below `B³`), inner bodies
at the coinciding cubic faces are

```
row2_body [11n-3g-1] =  2 M₁₁ (c/b) (4 b² c + 9 d²)
row0_body [13n-3g-1] = -2n (c³/b³) (4 b² c + 9 d²)
row1_body [12n-3g-1] =  M₁₄ (c²/b²) (4 b² c - 9 d²)
```

Residual scalings:

```
row2 = (-4/27) row2_body = (-8/27) M₁₁ (4 b c² - 9 d e)   # matches Lean
row0 = (+4/27) row0_body = 0  on (R2')
row1 = (-4/27) row1_body = (-4/27) M₁₄ (c²/b²) (4 b² c - 9 d²)
```

The row-two and row-zero faces are the *same* quadratic `4 b² c + 9 d²`.
Row one is the opposite sign `4 b² c - 9 d²`.

## Contradiction

`(R2')` and vanishing of residual row one give

```
4 b² c + 9 d² = 0
4 b² c - 9 d² = 0
```

hence `8 b² c = 0` and `18 d² = 0`, contradicting `b,c,d ≠ 0`.

On the explicit chart the residual row-one coefficient is

```
(27/2) (14 n - 3 g) d⁶ / b⁶
```

nonzero in characteristic zero.  Samples: `(n,g)=(11,2) ↦ 1998 d⁶/b⁶`,
`(17,4) ↦ 3051 d⁶/b⁶`.

No further Newton split is required.  Row zero is redundant.  Cubic defect
is redundant.

## Nonvanishing / integrality checklist

- `char 0` (prefactors `2,3,4,8,9,27` and `M₁₄`)
- `a,b,c,d,e ≠ 0` (selector)
- `3g < n` ⇒ `M₁₄ = 14n-3g ≥ 13n > 0`, `n-2g ≥ g+1 > 0`, `n-3g ≥ 1`
- `2h=3g` in `ℕ` ⇒ `g` even
- polynomial identities should be stated multiplied by `B³` (resp. `B`)
  so that the `Q`-rewrite never divides

## Missing Lean lemmas / cutoffs

Already present and sufficient for the invariant side:

- `secondaryResidualIncidenceDefectPolynomial68_degree_lt_cubicFace`
  (`Q < 9n-3g`)
- `secondaryLoadInvariantThreePolynomial68_degree_lt_cubicFace`
  (residual `I3 < 10n-3g`)
- `cubicLoadRowTwoPolynomial68_degree_lt_cubicFace`
  (row-two loads `< 11n-3g-1` for general middle `h`)
- row-two coefficient `grokRowTwo_coeff_balancedChamber68`

**Missing, and blocking a Lean close of this route:**

1. **Row-one load cutoff at the cubic face, general middle `h`.**
   `cubicLoadRowOnePolynomial68_degree_lt_residualDouble` only treats
   `e.natDegree ≤ 6n-2g`.  On the balanced wall one has the weaker bound
   `e ≤ 6n-h = 6n-3g/2`.  Dominant load is still `ℓ A³` against `D'` /
   `E'` / `V'`, degree `11n-g-1`.  Gap to the target:
   `(12n-3g-1) - (11n-g-1) = n-2g > 0`.  Needed:

   ```
   cubicLoadRowOnePolynomial68_degree_lt_cubicFace
     ... (he : e.natDegree ≤ 6n-h)
     : load.natDegree < 12n-3g-1
   ```

   Same shape as the existing row-two cubic-face load lemma.  The
   `e`-dependent load terms (`Uℓ ~ e`, `Vℓ ~ e`) sit at `11n-g-h-1` or
   lower and are even safer.

2. **Row-one `I3`-rewrite identity** (field identity, no analysis).  Same
   style as `grokBalancedRowTwo_eq_inner68`.

3. **Row-one `Q`-rewrite of the remaining `e` terms**, or a single combined
   rewrite `row1_body = (I3,Q-terms below 12n-3g-1) + cubic core`.  State
   it as a polynomial identity after multiplying by `B³`.

4. **Coefficient lemma** `grokRowOne_coeff_balancedChamber68` extracting

   ```
   (secondaryResidualRowOnePolynomial68 A B c d e).coeff (12n-3g-1)
     = (-4/27) M₁₄ (c²/b²) (4 b² c - 9 d²)
   ```

   under `(D)`, `Q.natDegree < 9n-3g`, `I3.natDegree < 10n-3g`, and the
   degree bounds above.  Vanishing then contradicts `(R2')`.

Optional, not on the critical path:

- row-zero cubic-face load cutoff `load < 13n-3g-1` (naive dominant
  `Uℓ E'` has degree `12n-1`, and `(13n-3g-1)-(12n-1)=n-3g>0`).  Only
  the double-face version exists today.
- cubic defect is not needed; its next-Disc condition `δ = 3bd` is the
  first step of a *slower* residual-discriminant split at gap `g/2`.

No missing *invariant* cutoff on `I3` or `I4` themselves: both cubic-face
load theorems already take `e ≤ 6n-h` and `g < h` in `3g < n`.

## Lean proof route (shortest)

1. Selector: `g < h < 2g`, `a,b,c,d,e ≠ 0`, `(D)` and `(I)`.
2. Restrict to the balanced wall `2h=3g`.
3. Quartic invariant ⇒ `Q < 9n-3g`.  Cubic invariant ⇒ residual `I3 < 10n-3g`.
4. Row two + existing load cutoff ⇒ `(R2)`, hence `(R2')`.
5. Prove the row-one `I3`/`Q` rewrite (kernel `ring` over `RatFunc`).
6. Prove the missing row-one cubic-face load cutoff by `compute_degree; omega`.
7. Extract `row1.coeff(12n-3g-1) = (-4/27) M₁₄ (c²/b²) (4 b² c - 9 d²)`.
8. Prefactor ≠ 0, so `4 b² c - 9 d² = 0`.  With `(R2')` contradict
   `c ≠ 0` (or `d ≠ 0`).

Do not open a Disc-gap split and do not extract row zero.

## What this is not

The homogeneous pullback with exact `Q = I3 = 0` (the discovery script
`max11_68_middle_surface_reduction_20260828.py`) produces a genuine
first-order system in `(B,r,u)` with nonzero `(B',r',u')` determinant.
That is the ODE on the load-free *surface*, not the Newton face of the
polynomial system.  After `(R2)` the cubic face of residual row one is
already nonzero, so that surface is never attained.
