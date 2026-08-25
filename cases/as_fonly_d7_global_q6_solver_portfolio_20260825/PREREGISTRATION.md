# Global Q6/high solver portfolio preregistration

This is an operational, non-theorem solver race over the exact frozen SMT2
formulas emitted by `as_fonly_d7_global_q6_high_20260825`.

Pinned formula SHA-256 values are:

- base 303: `65153b165ebf41d0c0eab16968ecb1533b7c09f2e32d84e5c79bb403bae3b081`;
- base 513: `2156231ae243cf9b697f4da62e3bc3be046372809013e211aceb8b2578aae7d2`;
- base 519: `37632719978aee58b0296f9e61f4d601fa5f8316eb8a7158f6e5a7b632ec14db`.

The portfolio changes solver engine, random seed, or Boolector rewrite level.
A `sat` endpoint is consumed only after the existing independent literal
integer replay passes.  An `unsat` endpoint is diagnostic until the exact SMT
bytes are deterministically bit-blasted and an independently checked proof is
frozen.  No endpoint by itself changes the mathematical scope of the source
compiler.

