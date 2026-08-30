# K00-REES-SANDWICH desk discriminator preregistration

- Basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
- Frozen source: unloaded prelude SHA-256
  `5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a`.
- Ring: `Q[d0,...,d5] = Q[S,T,e0,e1,e2,e5]`, with
  `S=d4`, `T=d3`, and `e=(f0,f1,f2,f5)`.
- Ideals: `I=(r1,...,r7)` and `J=(e0,e1,e2,e5)`.
- Question: whether the degree-16 monomial
  `e0^4*e1^4*e2^4*e5^4` survives after specializing `S=T=0`.
- Exact implication: a nonzero normal form proves `J^16` is not contained
  in `I`; together with the four reviewed identities `e_a^5 in I`, the
  pigeonhole containment `J^17 subset I` would then make 17 the smallest
  global exponent.  A zero normal form is no verdict on minimality and
  triggers a redesigned witness search.
- Runner: local reviewed `CAPRUN/v1`, Singular batch input with explicit
  `quit;`, wall cap 30 seconds, CPU cap 30 seconds, aggregate RSS cap 1 GiB.
- No modular computation or msolve output is accepted as evidence.
- Stop condition: typed normal completion, cap, or failure; no uncapped retry.

This is a desk-scale four-variable specialized membership test.  Any full
six-variable filtered standard-basis computation of `in_J(I)` is excluded
from this local run and must be frozen for AWS if still needed after the live
Fable review.
