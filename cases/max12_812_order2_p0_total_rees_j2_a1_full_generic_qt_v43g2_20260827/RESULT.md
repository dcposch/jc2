# V43G2 generic-only exact decision result

Date: 2026-08-27

Status: **PASS; exact generic-fibre unit, provisional pending multipliers and
total replay.**

The frozen Box02 lane regenerated the literal full total corpus and passed
all preregistered censuses:

- 70 named source slots and 59 nonzero total rows;
- 66 positive-weight total variables and 65 rho-zero variables;
- sole general-only variable `ez9`;
- exactly eight rho-only rows:
  `Tg11_2,Tg11_3,Tg11_5,Tg11_7,Tg12_5,Tg12_7,Tg13_7,Tg14_6`;
- sole `ez9` occurrence and exact pivot
  `Tg19_2 : (3/8)t*a1*ez9`;
- 58 rows in 64 variables after `a1=1` and exact linear elimination of
  `ez9`.

Singular computed the complete characteristic-zero `dp` standard basis over
`Q(t)` in 0.10 seconds (19,616 KiB peak RSS).  The basis file is literally
`1`, the normal-form file is literally `0`, and stdout records
`V43G2_GENERIC_BASIS_SIZE=1`, `V43G2_GENERIC_OUTCOME=unit`, and the terminal
PASS marker.  Compiler reconstruction took 244.43 seconds and 145,044 KiB
peak RSS.  Neither lane swapped.

## Exact custody

- frozen AWS source-manifest SHA-256:
  `b9b557d0ea1b3fc8c3335fa0589c5b0cc96096b9ebb07e39475f1d2152aa634c`;
- compiler-result SHA-256:
  `fac99098b36f5875b53c8d66439f34ca59b47e7f25a58f97dba1cb8cddd3806c`;
- generated Singular SHA-256:
  `7e3149d9ff89274e31c1068a51903dd9e2e716168141bd6286fa6b47d56328b3`;
- remote evidence-manifest SHA-256:
  `2cd5a6390d659caf3ffa52015bd1982534c72f15e5332c8cef46367a64077f61`;
- local harvest-manifest SHA-256:
  `65486fbb7ac8e6a0427149c4d2e1d2d73b3d4f8e46ee3049fbd004ac5e8dae9b`;
- basis-file SHA-256:
  `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b`;
- normal-form-file SHA-256:
  `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`.

The source manifest contains six harmless macOS AppleDouble metadata files,
all explicitly hashed.  They are never read by the compiler and cannot alter
the algebraic input.  The source tree was made read-only before launch and
was not mutated afterward.

## Scope and next gate

This proves the generic `Q(t)` conjunct for the frozen full grade-at-most-19
ordered-`a1` corpus, equivalently the generic `Q(rho)` conjunct by the pinned
faithful field bridge.  It is not yet an unrestricted total certificate.
Promotion waits for a separately frozen `liftstd` multiplier reconstruction,
literal 59-row/pivot replay, sigma-residue projection, weighted
rehomogenization, denominator/content clearing, and the reviewed special
converter if the cleared coefficient has positive `t`-valuation.

V43G1 remains live and untouched until that total replay passes.
