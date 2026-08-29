# Preregistration: K00 local-syzygy constant projection V16

Date: 2026-08-27

Status: **FROZEN BEFORE ALGEBRA; NO PROJECTION RESULT AT REGISTRATION.**

This is the first representation-independent block in the mixed
`Lambda<=19` successor.  In

```text
R=Q[d0,d1,d2,d3,d4,d5],  m=(d0,...,d5),
A=(r1,...,r7),
```

the `r_i` are the exact unloaded rows in the K00 chart at `C6=1`.  Consume
the complete 87-generator V14R1 syzygy module `S=syz(A)`, replay every
generator against independently pinned row bytes, and evaluate all 609
components at `m`.

The exact-Q primary endpoint must report the full evaluation span
`ev_m(S) subset Q^7`.  In particular it must decide, without selecting a
preferred lift, whether coordinates 2 and 4 vanish on the entire span and
whether the projection to coordinates `(6,7)` has rank two.  If so, the
affine slice of unit relations normalized by seventh coordinate one has
forced zero row-2 and row-4 constants but arbitrary row-6 constant.

For proof custody the producer must serialize all 609 constants, one file
per module component, and serialize two explicit full polynomial syzygies:

1. a base syzygy whose seventh component has nonzero constant;
2. a freedom syzygy whose seventh component has zero constant and whose
   sixth component has nonzero constant.

Both identities and all three constant tests are rerun in a fresh Singular
process constructed only from the serialized polynomial bytes.  Exact
rational Python elimination independently computes the evaluation rank and
the `(6,7)` projection rank.  Missing entries, malformed rationals, a
diagnostic, any failed identity, or any source/hash mismatch rejects.

`p=65521` may run only as a software control.  Either outcome concerns only
constant terms of unloaded local relations.  It is not yet a deformation in
the three load directions, a finite `Lambda`-jet solution, closure-first
incidence, Taylor realization, order two, maximum twelve, or JC2.

