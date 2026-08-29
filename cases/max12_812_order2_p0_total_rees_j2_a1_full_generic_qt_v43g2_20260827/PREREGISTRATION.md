# V43G2 additive generic-only exact `Q(t)` twin

Date: 2026-08-27

## Frozen question

This is an additive, independent execution twin of the generic stage in
V43G1.  It decides whether the literal 59-row ordered-`a1` corpus through
grade 19, after `a1=1` and the exact linear `ez9` pivot, generates the unit
ideal in

`Q(t)[X']`,  where `t=rho^2` and `|X'|=64`.

The source predicate is unchanged: 70 named slots, 59 nonzero total rows,
66 positive-weight variables, 65 variables on the `rho=0` face, sole
general-only variable `ez9`, and eight `rho`-only rows.  The unique `ez9`
occurrence must be

`Tg19_2 : (3/8)t*a1*ez9`

in its `ez9` term.  After `a1=1`, this is a nonzero scalar times `ez9` in
`Q(t)`, so consuming `Tg19_2` and eliminating `ez9` is an exact quotient-ring
isomorphism.  The decision ideal therefore has the same 58 rows and the same
64-variable alphabet as V43G1.

## The only omitted computation

V43G2 deliberately skips V43G1's redundant computation of
`std(J|_(t=0,a1=1))`.  It does not weaken or change the generic predicate.
The special-fibre conjunct is supplied externally by the pinned exact V42
radical cascade and its hostile review.  The `Q(t) -> Q(rho)`, `t |-> rho^2`
faithful field-extension bridge is supplied by the pinned V43G1 field
addendum.  Failure of any dependency hash is a hard compiler failure.

This omission is a speed optimization only.  It is not new evidence for the
special fibre, and V43G2 must never print a special-fibre PASS marker.

## Decision semantics

The primary lane computes a complete characteristic-zero `dp` standard basis
of the 58-row ideal over `Q(t)` and reduces `1` by it.

- Exact normal form zero: provisional generic-fibre unit.  Promotion still
  requires tracked multipliers, exact product replay, weighted
  rehomogenization, and (if the cleared coefficient vanishes at `t=0`) the
  explicit special-certificate converter.
- Exact nonzero normal form after completed `std`: decisive generic-fibre
  nonunit for this frozen full corpus.
- Timeout, OOM, signal, incomplete basis, missing marker, dependency drift,
  or any `FAIL_` marker: no verdict.

No modular or rational `t=c` specialization is a verdict.  The original full
V43G1 run is preserved and continues independently.

## Pinned dependencies

- V43G1 compiler:
  `03b76b7b9592abf9c13ccb3a8ea716c9b43d601f7ce26a37428733435cf6e957`.
- V43G1 preregistration:
  `8a4727c2524134583885e06bd0d7d238068231ea971ac36f51f13ac13123afe3`.
- V43G1 field bridge:
  `25f5200017d0fb95ea0ff5aead291acfcef651c400cfcf4deb272653438a09df`.
- V42 replay:
  `f4ec72933793bf08aabc600df7cdcd47b8de2c54f45c0d30341e13ac0b676459`.
- V42 report:
  `5d4c42fff1ad563586e8ae8736c3938efb1ae48467dfab96ae7fd9b861e7037f`.
- V42 hostile review:
  `a4f6b93181526cd8907c6412faeef2ed2e69012a5820e939079ba4cf891f3439`.
- repaired two-fibre theorem:
  `a7f96b0d8ac5867cefe7984f87a44ecd30ef3780df731e8b3acc3dc9db159ec6`.
- two-fibre hostile review:
  `bc539ba91600b95e5400e96635e8973ef6cb6454b9641c0c68d09a99aef0690f`.

The complete AWS source tree, this preregistration, compiler, runner, and
generated Singular script are hashed before execution.  The first lane uses
one Box02 core, a 640-GiB virtual-memory cap, and a six-hour wall cap in a
unique namespace.  Existing Box02 processes and paths are protected.
