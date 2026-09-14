# Descended arithmetic-key audit

Run from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 box/ideation-astra-20260905/cohort/cohort_compression.py
```

The script verifies the source snapshot hash mechanically against
`box/h1nonres-20260903/summary.json` before reading its cohort. This is an audit
of that banked auxiliary snapshot, not promotion of a new necessary census.
The upstream report is `xmodel/h1-nonres-census-sol56-20260903.md`, lines 52–81.

For the selected `phase == us_gt_1 and xu_ok_candidate` cohort:

| Quantity | Measured count |
|---|---:|
| Original rows | 296 |
| Arithmetic `(n',m',ell,V2')` keys | 132 |
| Arithmetic `(n',m',ell)` keys | 52 |
| Records retaining inherited `(M',V',height)` | 296 |
| Quadruple keys with different inherited decorations | 43 |
| Raw/effective child height 2 / 3 / 4 | 19 / 88 / 189 |
| Coprime degree ratios | 9 |
| Rows of ratio 3:2 | 177 |

The wider 310-row POLY/ODE cohort has 140 quadruple keys and 53 triple keys.
The JSON records every original key, exhaustive membership of each arithmetic
key, full inherited decorations, histograms, and concrete collisions.

The simplest collision has source degree `(126,84)` and `V=(5,10,5)` in
both cases. Source characteristics `M2..M4=(-14,63,124)` and `(112,119,124)`
both map to `(n',m',ell,V2')=(36,24,2,5)`, while the inherited sequences
including `M1'=-m'` are `(-24,-4,18)` and `(-24,32,34)`. Their terminal
anchors are 17 and 1. Thus even the terminal radius inferred under the
licensed monomial-Jacobian descent differs: `-3/17` versus `-3`.

The arithmetic transformation is the banked law `n'=n*u_s/d_s`,
`m'=m*u_s/d_s`, `M_i'=M_i*u_s/d_s`, `ell=V_s-u_s-1`, with `V_i'=V_i`.
These are conditional no-split descendant metadata; they do not assert that
any skeleton is realized by a polynomial pair. Equal keys need not define
equal joint charts. A common necessary overapproximation with a proved
source map could still allow one certificate to cover multiple decorated
records. The observed 296 distinct decorated records therefore imply no
lower bound of 296 required chart solves.

The prior 6209-to-1359 compression was for a different, raw census. It does
not yield 65 charts for this selected cohort. The measured quadruple
compression here is `296/132 = 2.2424...`, and the triple compression is
`296/52 = 5.6923...`.
