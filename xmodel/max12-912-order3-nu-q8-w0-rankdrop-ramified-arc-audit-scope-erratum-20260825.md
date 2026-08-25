# Scope erratum — pointed `b=1` shard in the Q8 ramified-arc audit

The immutable report
`xmodel/max12-912-order3-nu-q8-w0-rankdrop-ramified-arc-audit-claude-20260825.md`
(SHA-256
`01891db1277f0d8f79e694696e117c44f7ea1dfecd705373e457626e0cb75330`)
overstates the scope of its proposed Shard B1 in Section 5.

That shard substitutes

```text
d4 = 1,
d2 = 2 + u
```

and therefore tests only the slice in which `d4` is constant.  An arc whose
special point is `(d2,d4)=(2,1)` may instead have nonconstant `d4`, for
example

```text
d4 = 1 + v(t),
d2 = 2 + v(t) + u(t).
```

Consequently, a unit basis in the frozen Shard B1 would not by itself exclude
all selected arcs through `(2,1)`.

Either of the following exact computations has the needed moving-coefficient
scope:

1. the report's Shard G over the polynomial ring
   `Q[c,b,w,u,x1,x3,x5]`, with `d4=b`, `d2=b+1+u`, and with `c,b` retained
   as ring variables (not moved into the coefficient field); or
2. a pointed shard over `Q[c,v,w,u,x1,x3,x5]` with
   `d4=1+v`, `d2=2+v+u`, and landing centre
   `(v,w,u,x1,x3,x5)`.

The same distinction applies to `c`: using `Q(c)` proves a generic-`c`
statement, whereas retaining `c` as a polynomial variable is required for all
finite `c` and for `c`-drifting arcs.

This erratum does not alter the report's hand calculation of the surviving
`b=1` slope-two leading cone or its narrow interpretation of the `-108`
residual.  It narrows only the proposed frozen-Shard-B1 closure claim.
