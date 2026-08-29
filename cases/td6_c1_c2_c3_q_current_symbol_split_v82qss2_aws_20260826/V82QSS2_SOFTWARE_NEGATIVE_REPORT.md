# V82QSS2 empty-map constructor failure

V82QSS2 is preserved as software-negative evidence and carries no q11 or q16
CURRENT theorem.  Four independent AWS lanes completed the same exact source,
FIRST, PREVIOUS/POLE, CURRENT, direct-q-prime omission, pivot-schedule,
original-row, and production-packing computations, wrote matching exact map
tables, and then exited `rc=1` before the denominator and result assertions.

The common failure is at `replay_v82qss_symbol.py:158`:

```text
return p.denominator_for(coordinates.values()) if coordinates else p.tri.CTX(1)
TypeError: 'flint.types.fmpq_mpoly.fmpq_mpoly_ctx' object is not callable
```

`tri.CTX` is the polynomial-ring context, not a constructor.  An empty map has
unit common denominator `tri.ONE`.  q11 fails while constructing the empty
omit-map denominator; q16 fails while constructing the empty full-map
denominator.

## Matching preliminary evidence

| axis | Box03 rc / stdout SHA | r6d rc / stdout SHA | exact map-table SHA |
|---|---|---|---|
| q11 | `1` / `cac165676dd3da84a6cc95c1528e59bea46a111d7364dd53de177c7e5a076d2d` | `1` / `c16ad09eed934f0443422f93167eab391b00adc6f0f238cb4c7c208c56b6380a` | `5c263636e19e807ccf862a06d8771030fcd65fa311f3bcef76781ab7b4e808e1` |
| q16 | `1` / `b0375eff9142debb1409e5cf2cb4d100506f3b781f780ccccd5b5235f8247fdb` | `1` / `70c2a35d6e4c04b49556d4ec5798882e9052e8acdcf2cbc4b457ac79592b0fbb` | `17ec4f2ccfb619aa505504e764adfd433cd1b7c37a96bdc26ec881fe835261fd` |

Before failure, both q11 lanes print a source-replayed rank `38/132` FIRST
system and rank `38/94` PREVIOUS/POLE system with one dependent row; both q16
lanes print the same FIRST rank and a rank `38/94` PREVIOUS/POLE system with no
dependent row.  They also verify the literal direct-q-prime formulas, including
the raw q11 coefficient `11 U^6` at `('X0',10)` and raw q16 coefficient
`16 U^6` at `('X0',15)`.  These facts are preliminary because the executable
did not reach its complete denominator/output contract.

V82QSS3 is the immutable minimal repair: replace the invalid empty-map
constructor by `tri.ONE`, assert its typed unit semantics before the expensive
stage, and rerun independently on Box03 and r6d.  Nothing in V82QSS2 licenses a
q-neighborhood, family, whole-TD6, SP-2, landing, or JC2 inference.
