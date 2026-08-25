# TD6 V73K preregistration: single full original-source replay

V73K retains V73J's corrected monomial-order delta controls.  It removes
two redundant positive convolutions: after the exact division/lift has
constructed the previous-plus-first relation, it performs one complete
direct replay against all selected original previous and first rows and
asserts the raw target `-residual`.  It then normalizes both the stored
relation and that replayed target by the exact residual inverse and asserts
the unit `-1`.  Thus original-source ancestry is still checked by a full
replay; the omitted second lift replay and third normalized replay were
algebraic duplicates.  Denominator/factor ledgers, direct-q-prime typing,
and all controls are unchanged.

## Retained V73J source and control construction

V73J preserves V73H's positive original-row identity construction
from all selected original previous and first rows.  It replaces only the
three redundant negative full convolutions by exact leading-term delta
certificates in the integral domain
`Q(U)(algebraic constants)[beta][source variables]`: omission changes the
identity by `-m*r`, plus-one changes it by `r`, and wrong-row replacement
changes it by `m*(r_wrong-r)`.  Each factor and its leading-coefficient
product is asserted nonzero using lexicographic order on exact exponent
vectors and emitted with a deterministic digest.  This
is a proof-carrying performance change, not a source or theorem-scope
change; the full positive original-row replay, denominator ledger,
direct-q-prime control, and all fail-closed gates remain unchanged.

## Retained V73H source reconstruction

V73H retains V73D's arbitrary-degree division implementation: at each
normalized affine pivot, it eliminates all current monomials containing the
pivot in one exact quotient layer.  It refuses any pivot equation whose
leading singleton is not one or whose tail still contains the pivot, and it
retains the complete reconstructed-input replay assertion.  All source
typing, direct-q-prime path, denominator ledgers, and controls below remain.

It freezes the exact direct-q-prime left-null support discovered fail-closed
by V73F: all twelve `('X-1',d)` rows for `0 <= d <= 11`, and no pole row.
It calls the hash-pinned parent compiler itself with only its outer
`range(40)` degree iterator restricted to those twelve values.
Every inner range delegates to the built-in unchanged, and the wrapper
asserts exactly one outer interception.  In particular `q'` has degree-one
coefficient `2*beta`, so the parent term `2*f2*q'` contributes the full
`4*beta*f2[10]` at degree 11.  No pole row occurs in the support.  This is a
parent-source sparsity acceleration, not a formula transcription or staged-row
shortcut.

## Fixed target

On the exact raw line `V=0,C=-5U^2,D(U)`, rebuild transport and the first and
previous/pole stages over `E(U)[beta]` for
`q_beta=t+beta*t^2+t^25`. Do not consume the staged current/N13 object.
Instead, select the observed dependent previous row `('X-1',11)`, factor its
exact residual coordinatewise over `Q(U)`, and reconstruct its left-null
combination through the original previous/pole rows and original first rows.

The hash-pinned `b3half` parent is only a `Q(U)` arithmetic adapter. The raw
center `(-5U^2,0,U)` and raw B3 identity are asserted directly.

## Pass gate

- exact import/source preflight, AWS/Linux host/tag refusal, and raw-center
  checks;
- transport rank 3470/3602 and first rank 38/132 with the frozen pivots;
- previous/pole rank 37/94 and exactly the expected nonzero dependent rows:
  `('X-1',11),('X-1',13)` with direct q-prime, and only `('X-1',11)` when the
  direct q-prime term is omitted;
- the `('X-1',11)` residual is beta-independent and has frozen digest
  `3884ec0c...` in both modes;
- an exact inverse whose coordinate denominators have support only at U=0;
- exact reconstruction of every selected previous row through original first
  rows, followed by an original-source normalized residual `-1`;
- omission, plus-one, and wrong-row controls all break the identity;
- complete coordinate numerator/denominator and leaf-denominator ledgers;
- byte/expression agreement of independent Box02 and Box03 theorem runs.

Any changed rank, residual, factor support, source ancestry, or control is a
fail-closed result. The omit-q-prime run is a robustness/control replay, not
a distinct mathematical theorem.

## Scope firewall

A PASS excludes only the fixed normalized A3 q2-beta raw line
`V=0,C=-5U^2,D(U)`. The origin U=0 remains the separate reviewed V70 leaf.
No whole B3, whole A3, other TD6 modulus, TD6, SP-2, landing, counterexample,
or JC2 conclusion is licensed here.
