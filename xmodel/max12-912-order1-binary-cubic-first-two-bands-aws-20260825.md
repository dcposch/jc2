# Producer report: fixed-D12 `(9,12)` order-one binary-cubic bands

**Status: PRODUCER-EXACT / PROVISIONAL PENDING HOSTILE REVIEW.**

## Claim

Over an algebraically closed characteristic-zero field, after the licensed
constant normalization `P9=K^3`, `Q12=K^4`, every nonzero binary cubic has one
of the geometric types `L^3`, `L^2M`, or `LMN`.  On the displayed
representatives, complete exact rational compilation of

```text
[P9,Q12] = 0,
[P9,Q11] + [P8,Q12] = 0,
[P9,Q10] + [P8,Q11] + [P7,Q12] = 0
```

gives:

| type | degree-18 linear map | degree-17 fresh map | projected quadratic obstruction | exact scheme dimension |
|---|---|---|---|---:|
| `L^3` | `19x21`, rank 11, kernel 10 | `18x19`, rank 10, kernel 9, cokernel 8 | 6 nonzero equations, span rank 6 | 7 |
| `L^2M` | `19x21`, rank 12, kernel 9 | `18x19`, rank 11, kernel 8, cokernel 7 | 6 nonzero equations, span rank 6 | 6 |
| `LMN` | `19x21`, rank 12, kernel 9 | `18x19`, rank 11, kernel 8, cokernel 7 | 7 nonzero equations, span rank 6 | 6 |

The obstruction ideals are nonunit and nonreduced; the printed standard bases
are part of the frozen evidence.  This is first-two-lower-band geometry, not a
full fixed-cap classification or exclusion.

## Source controls

The compiler uses the coefficient identity

```text
[A_i x^i y^(a-i), B_j x^j y^(b-j)]
  = (i*b-a*j) A_i B_j x^(i+j-1) y^(a+b-i-j-1)
```

and checks every bracket against an independent derivative/dictionary
implementation.  It verifies the complete row and column counts, every kernel
and left-cokernel vector, the zero-lower-face positive control, and a perturbed
`Q12` negative control.  No division by `K`, Kummer root, Q8 divided row,
Taylor row, or terminal row occurs.

## Finite-SAT interface

The frozen mod-`3^11` witness has normalized cubic coefficients
`(1,119880,40581,0)`.  Their valuation bounds under any exact continuation are
`(0,4,5,>=11)`.  In

```text
Disc(K)=a^2 b^2-4b^3-4a^3c-27c^2+18abc,
```

the five term-valuation lower bounds are respectively `18,15,23,25,22`.
The unique minimum proves `v3(Disc(K))=15`, hence nonzero discriminant, for
every exact continuation of this literal finite witness.  Conditional on such
a continuation, it enters the `LMN` row above.  Separately, the fixed-total-D12
partial-`y` leading coefficient has fourth power constant, so its Kummer class
is order one after the licensed finite scalar extension.

This does not compose a lower band for the finite witness and does not show
that the witness continues.  It is a strict SCOPE-CONFLICT with the selected
order-three Q8 leaf, not a landing there.

## AWS custody

All six lanes returned `PASS` on r6d and Box02.  For every stratum the exact
compiler JSON, emitted Singular source, Singular stdout, and result JSON are
byte-identical across hosts.  Same-source dual-host agreement is custody only.

The remote `OUTPUT.sha256` files contain one stale entry: they were written
before the final `launcher.stdout` PASS line.  They are quarantined without
mutation.  The active post-harvest manifest is
`cases/max12_912_order1_binary_cubic_bands_aws_20260825/MANIFEST.postrun.sha256`;
see `CUSTODY_SUPPLEMENT.md`.

## Firewall

Nothing here proves survival beyond `3^11`, an inverse limit, a
characteristic-zero Keller map, compatibility below degree 17, emptiness of
any root-type stratum, preservation of the B9 residue chart under `PGL2`, a
selected-Q8 landing, maximum twelve, a counterexample, or JC2.

