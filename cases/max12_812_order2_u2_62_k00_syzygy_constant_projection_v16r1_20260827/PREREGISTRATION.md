# Preregistration: K00 local-syzygy constant projection V16R1

Date: 2026-08-27

Status: **FROZEN BEFORE THE R1 ALGEBRA; BOTH PROJECTION BRANCHES ACCEPTED.**

## Question

In

```text
R=Q[d0,d1,d2,d3,d4,d5],  m=(d0,...,d5),
A=(r1,...,r7),
```

use the exact unloaded K00 rows at `C6=1` and the complete frozen
87-generator polynomial module `S=syz(A)` from V14R1.  Replay every
generator coefficientwise against independently pinned row bytes, serialize
all 609 origin constants, and compute over Q:

1. the rank of `ev_m(S) subset Q^7`;
2. whether coordinates 2, 4, and 6 vanish on the full span;
3. the rank of the projection to coordinates `(6,7)`; and
4. an explicit syzygy whose seventh component has nonzero origin value.

The producer must accept either branch:

- `M6_FREEDOM`: the `(6,7)` projection has rank two; serialize and freshly
  replay an additional syzygy with seventh constant zero and sixth constant
  nonzero.
- `M6_FORCED`: the `(6,7)` projection has rank one and every sixth-coordinate
  constant is zero; freshly replay the unit-base syzygy and retain all 609
  constants as the exhaustive certificate.

Any other `(6,7)` rank/pattern is reported faithfully but rejected as outside
these two decision branches.  No expected evaluation rank is hard-coded.
`p=65521` is only an independent software control.

## Localization-completeness lemma used by the interpretation

The 87 generators span the full polynomial syzygy module.  If a syzygy over
the local ring `R_m` is written with denominators, a common denominator
`s notin m` clears it to a polynomial syzygy.  Evaluating at the origin
multiplies its vector by the nonzero scalar `s(0)`.  Conversely every
polynomial syzygy is a local syzygy.  Therefore the origin-evaluation span of
the polynomial module controls *all* local representation freedom.  A
coordinate forced to zero on the polynomial span is forced to zero for every
local syzygy as well.

## Custody and scope

The exact-Q endpoint requires a fresh second Singular process built only from
serialized witness bytes, exact rational Python elimination of the 7x87
constant matrix, immutable hashes, and literal-zero replay residuals.
Missing entries, malformed rationals, diagnostics, source drift, or any
identity failure rejects.

Either outcome concerns only order-zero constants of unloaded local
relations at the normalized `C6=1` K00 point.  It is not by itself the
first-order load/deformation cokernel, an honest `Lambda<=19` source-image
test, closure-first incidence, Taylor realization, order two, maximum twelve,
or JC2.

