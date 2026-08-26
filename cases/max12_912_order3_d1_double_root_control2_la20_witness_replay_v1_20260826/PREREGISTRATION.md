# Preregistration: literal witness and finite-support replay

- Fixed input: exact nine expanded generators from pinned B plus the printed
  LPDP V2 `FINAL[1..9]` and `TAIL` coefficients whose producer stdout SHA is
  pinned in the compiler.
- No saturation or Gröbner basis is recomputed. Check the exponent-96 Rees
  identity by literal polynomial equality; independently reconstruct `W`, its
  primitive integral multiple, all eight exponent vectors, and the exact
  weight multiset `80x1,81x1,82x5,88x1`.
- Positive endpoint requires literal identity zero, exact expected `W`, exact
  scaling, eight terms, no `s`/`rho`, unique weight-80 monomial `la^20`, all
  PASS markers, rc zero, and empty stderr/stdout diagnostics.
- Any discrepancy gives no verdict. This corroborates only the explicit
  fixed-source witness and its finite strict halfspaces; it is not an
  independent derivation of the equations or a full-fan theorem.
