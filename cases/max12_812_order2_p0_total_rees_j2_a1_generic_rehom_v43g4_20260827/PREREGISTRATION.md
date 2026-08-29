# V43G4 exact generic Bezout rehomogenization

Date: 2026-08-27

V43G4 consumes only the separately frozen V43G3 multiplier evidence.  It
must reparse all 58 saved `Q(t)` multipliers, independently replay their
product with the exact regenerated dehomogenized rows as `1`, and retain the
original `Tg19_2` pivot with coefficient zero.

It then performs these deterministic exact operations:

1. clear the least common rational denominator and the least common negative
   `t` exponent;
2. divide the target and every multiplier by their common integer content;
3. replay the resulting polynomial identity
   `v(t)=sum D_i(t,X) Tg_i(1,t,X)` in `Q[t,X]`;
4. project each `D_i` to the sigma residue satisfying
   `wt(monomial)+grade(Tg_i)=0 mod 5` and replay again;
5. homogenize every retained term with powers of `a1`, using one common
   maximum sigma level, and replay
   `v(t)*a1^E=sum H_i(t,a1,X) Tg_i(t,a1,X)` in the literal total rows;
6. run a corrupted-row negative control.

No interpolation, modular arithmetic, rational `t=c` specialization, or
floating point is allowed.  The Laurent parser is fail-closed and accepts
only the exact monomial-denominator grammar emitted in the frozen multiplier
files.  A terminal PASS requires equality of full sparse polynomial maps at
all three replay stages.

The expected telemetry from the frozen files is a common denominator
`5*t^6`, product levels 15 and 20, and total target `5*t^6*a1^4`; these are
not hard-coded verdicts and must be derived and checked.  Since the expected
coefficient has positive `t`-valuation, even a PASS is still provisional
until the independently replayed special `a1^M` certificate is composed by
the reviewed converter.

Pinned V43G3 result SHA-256:
`6db87ebacaa175c68dca5739dbad35390d36ff62ff914859c82a1d60e79270c4`.

Pinned V43G3 freeze SHA-256:
`8f60b30576e1712479e09cc01c3244c6ff5c7053c0d3cd08e9d4fbad8745ca45`.

The first exact run uses one r6b core, a 64-GiB virtual-memory cap, and a
one-hour wall cap.  Existing r6b work remains protected.
