# V43G1 full generic-fibre decision preregistration

Date: 2026-08-27

## Frozen question

Let the literal V43 regeneration produce the 59 nonzero ordered-`a1`
total rows through grade 19 in

`S = Q[rho, X]`,

where `X` is the exact 66-variable positive-weight alphabet (including `a1`
and the general-only variable `ez9`).  Every rho exponent in these rows is
even, so put `t = rho^2`.  This lane decides whether the full dehomogenized
generic fibre

`J_K = (all 59 rows)|_(a1=1) * K[X \ {a1}]`,

is the unit ideal in `K[X \ {a1}]`, where `K = Q(t)`.

The literal census is part of the predicate: 70 named source slots, 59
nonzero total rows, 66 positive variables, 65 rho-zero variables, sole
general-only variable `ez9`, and exactly eight total rows whose specialization
at `t=0` is zero.  All eight such rows remain in the mathematical input and
their names and hashes must be emitted by the compiler.

## Exact linear elimination of `ez9`

The compiler must find exactly one occurrence of `ez9` in the complete
59-row corpus.  After `a1=1`, that occurrence must be a nonzero element of
`K` times the monomial `ez9`, with no other positive variable in that term,
and no other row may contain `ez9`.  If these checks pass, its row is of the
form

`c(t) ez9 + h(X')`, with `c(t) != 0` in `K`.

It is used as a monic linear equation to eliminate `ez9`.  Thus unitness of
the original 59-row ideal is exactly unitness of the remaining 58 rows in
the 64-variable ring `K[X']`.  The pivot row is consumed by this exact ring
isomorphism; it is not omitted from the source question.  Any census or
linearity failure is a hard failure.

## Decision and evidence semantics

The exact decision is a complete characteristic-zero degrevlex standard
basis in `Q(t)[X']` followed by exact reduction of `1`.

- Exact normal form zero: provisional generic-fibre unit.  It is not promoted
  to a total certificate until a tracked multiplier run, exact product replay,
  rehomogenization, and the reviewed special-certificate denominator converter
  all pass.
- Exact normal form nonzero after a completed standard basis: decisive
  generic-fibre nonunit for this frozen full corpus.  In conjunction with the
  reviewed two-fibre theorem and exact special-fibre unit, this rules out the
  ordered-`a1` localized certificate sought by this lane.
- Timeout, memory exhaustion, compiler failure, incomplete basis, or missing
  output: no verdict.

The compiler also runs an exact positive control: all 59 rows specialized at
`t=0` and `a1=1` must generate `1` over `Q`.  The eight rho-only rows become
zero in this control, as they should.  Failure is fail-closed.

Rational or finite-field specializations `t=c` are telemetry only and can
never decide this frozen question.  They are deliberately not needed for the
first exact launch.

## Custody

Pinned inputs:

- V43 literal total compiler SHA-256
  `0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00`.
- V43 census addendum SHA-256
  `266dfb8962cbeb1af73d4f03947670148b71a00eebd5e2a91fce9c78b99bf658`.
- Fable5 V43 compiler delta review SHA-256
  `ae8ecf1887a62afd873fc795d0eeec50ff0aac6e4954813931d09a34c8bfc31a`.
- Grok two-fibre hostile review SHA-256
  `bc539ba91600b95e5400e96635e8973ef6cb6454b9641c0c68d09a99aef0690f`.

The AWS source tree and every launcher/compiler byte are frozen in a manifest
before launch.  The exact run is one core, at most 640 GiB virtual memory, and
at most six hours on Box01.  Existing Box01 jobs are protected and untouched.

