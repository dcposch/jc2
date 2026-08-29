# K00 unloaded local-surface test v1

Date: 2026-08-29 UTC
Status: PREREGISTERED EXACT-Q AWS SCREEN / NO THEOREM YET

## Question

Let `I=(r1,...,r7)` be the seven frozen unloaded normalized K00 rows in
`Q[d0,...,d5]`, and let

```text
f0 = d0-2*d4-d4^2,
f1 = 8*d1-(1+d4)*d3,
f2 = d2-d4-16*d3^2,
f5 = d5-2*d3,
J  = (f0,f1,f2,f5).
```

The graph `V(J)` is the exact two-parameter unloaded surface

```text
D(S,T)=(2S+S^2,(1+S)T/8,S+16T^2,T,S,2T).
```

Test whether the local radical of `I` at the origin is `J`. This would be a
candidate algebraic input to a formal recentering theorem; it is not itself
such a theorem.

## Frozen source

The only row source is

```text
cases/max12_812_order2_u2_62_k00_colon_local_v14r1_20260827/
  aws_q_box01_pass/compiled/serialized_replay_prelude_Q.sing
```

with SHA-256 to be checked by the route runner. No row may be retyped.

## Independent exact lanes

1. `LOCAL-POWER`: map `I` to the local degree ordering at the origin, compute
   an exact standard basis, and search independently for powers of each
   `f0,f1,f2,f5` with zero local normal form. Record the standard basis and
   every first-zero exponent. A zero local normal form is screening evidence
   until a denominator-cleared identity is serialized and replayed.
2. `GLOBAL-MINASS`: compute the exact characteristic-zero minimal associated
   primes of `I`, serialize every component, and identify which components
   contain the origin. Promotion requires direct two-way containment checks
   and confirmation that the unique origin component is exactly `J`.
3. `GLOBAL-POWER`: independently compute a tracked exact standard basis of
   `I`, search through exponent 64 for each `f0,f1,f2,f5`, and serialize a
   direct multiplier vector for every first power found. Every certificate
   must replay the polynomial identity `matrix(I)*L=f_i^n`; a changed
   multiplier must fail. This is the portable certificate route from
   `J subset sqrt(I)`, while the already checked `I subset J` gives the
   reverse radical containment without relying on primary-decomposition
   internals.

Both lanes must first verify `I subset J`, `J` has dimension two, and the
surface substitution kills all seven rows. Mutations change the coefficient
`16` in `f2` to `15` and must break containment.

## Endpoint discipline

Allowed endpoints are `SCREEN_SUPPORTS_LOCAL_RADICAL_J`,
`SCREEN_REFUTES_LOCAL_RADICAL_J`, `EXACT_GLOBAL_RADICAL_J`, or
`RESOURCE_CAP_NO_VERDICT`. The exact endpoint requires four replayed global
power identities in addition to `I subset J`. Even an exact global radical
equality is only unloaded coefficient geometry. It does not
prove that mixed source arcs lie on the surface, that ramification reduces to
an integer section, that a finite jet lifts, that any arc is a polynomial
map, or that JC2 holds.
