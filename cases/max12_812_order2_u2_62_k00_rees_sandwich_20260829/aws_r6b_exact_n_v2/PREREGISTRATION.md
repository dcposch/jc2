# K00-REES-SANDWICH V2 exact rerun preregistration

- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
- Registered lane: `K00-REES-SANDWICH-EXACT-N-V2-R6B-20260829`.
- Registered host: campaign r6b, instance `i-0f089e64c378f5da3`.
- Original immutable inputs only: frozen unloaded prelude SHA-256
  `5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a`
  and the 28 reviewed fifth-power multiplier polynomials.  No V1 output,
  witness, apparent exponent, or normal form is an input.
- V1 is sealed and quarantined as `NO VERDICT` in `../V1_QUARANTINE.md`.

## Exact search

Recompute from degree 16 downward, without a seeded endpoint.  Replay
`I subset J^2`, `I not subset J^3`, all four identities `fa^5 in I`, all four
nonmembers `fa^4 notin I`, and source/certificate mutations.  At each degree
reduce every monomial with all four exponents at most four against a fresh
exact-Q standard basis of `I`.  Fifth-power divisibility handles every omitted
monomial.  The first degree `n` with a nonzero exact normal form proves that
the least `N` with `J^N subset I` is `n+1`; monotonicity rules out every lower
exponent.

In a separate exact process, carry the seven literal rows and `f0^5` together
across the ring change, then test the plane
`S=T=0, e0=4e2, e5=-2e1`.  Divisibility of all seven row images by `l^3`
checks vanishing of their quadratic initials; the separately carried eighth
entry must equal `1024*l^5*u^5` and remain nonzero.

## Planted fail-closed regression

Before either evidence process, run `undefined_symbol_regression.sing`.  It
deliberately references `definitely_undefined_k00_symbol` and then prints a
fake PASS line.  Singular is expected to return status zero while emitting a
diagnostic.  The same generic output validator used for both evidence runs
must reject the planted output specifically with diagnostic status 41.  If
it accepts the fake PASS, rejects for a different reason, or the planted
diagnostic is absent, the route fails before mathematical work.

## Caps and endpoints

- Negative control: 30 wall / 30 CPU seconds / 256 MiB aggregate RSS.
- Exact search: 1,800 wall / 1,800 CPU seconds / 32 GiB aggregate RSS.
- Initial strictness: 120 wall / 120 CPU seconds / 1 GiB aggregate RSS.
- Every process uses `CAPRUN/v1`, closed stdin, 0.10-second RSS sampling, and
  five-second TERM grace.
- The runner is bound to Linux, Amazon EC2, the exact instance ID, lane tag,
  and payload manifest.  It rejects reused outputs, non-normal lifecycle,
  any `K00_REES_FAIL=`, or any generic Singular diagnostic including lines
  beginning with `?`, `error occurred in or before`, `not defined`, or
  `expected ... expression`.
- Required endpoints are exactly
  `PASS_K00_REES_SANDWICH_EXACT_MINIMAL_N` and
  `PASS_K00_REES_INITIAL_IDEAL_STRICTNESS`.
- Any other outcome is `NO VERDICT`.

This does not recompute or consume the producer-unreviewed quartic
elimination owned by the live Fable hostile review.  It makes no loaded,
cell, arc, closure, map, or JC2 claim.
