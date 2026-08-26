# Erratum V2 — `(8,12)` order-four/order-two coefficient infinity

Date: 2026-08-25  
Status: **NARROW NONMUTATING REPAIR; SUPERSEDES ONLY §7 `(7.2)` AND ITS
LOAD-DIRECTION SENTENCE**

## Immutable charged pair

```text
092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e
  xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md
2f0a03a99ba6563034cdaf84ffc06f6d78ddd377144201d40aa4352ac71c6b55
  xmodel/max12-812-order24-coefficient-infinity-review-grok-20260825.md
```

The hostile review returned `REPAIR` at exactly identity `(7.2)` and the
sentence which uses it.  It independently confirmed the source typing,
terminal row, infinity residue, bounded-degree split, ordinary unloaded raw
exceptional fibre, common-quartic reduced support, strict-Rees design, chart
cover, and denominator audit in §§0--6.  The original target remains
immutable.  Read it together with this erratum as the V2 theorem.

## Replacement for §7 `(7.2)` and the adjacent sentence

At a common quartic

```text
K=z^4+pz^2+cz+r,             f=K^2,
```

the monic eighth root is

```text
w=f^(1/8)=K^(1/4),
```

not `K^(1/2)`.  Holding `f` fixed, the first variation of

```text
H_F(w)-g(z(w))
```

in the order-two load direction `k_j`, for `j in {2,6,10}`, is the strictly
negative-power Laurent part

```text
[w^j]_- = [K^(j/4)]_- .                              (E.1)
```

It vanishes if and only if `K^(j/4)` is a polynomial.  Since every such `j`
is congruent to two modulo four, this is equivalent to `K` being a square in
the polynomial ring.  For the monic depressed quartic above, the square
locus is exactly

```text
c=0,             p^2=4r,                             (E.2)
```

because a monic square with zero cubic coefficient has the form
`(z^2+p/2)^2`.  Thus all three load derivatives vanish on the proper closed
square sublocus `(E.2)` and are nonzero at a generic common quartic.  The
displayed equalities in the original `(7.2)` are false and are not consumed.

The coefficient-direction calculation `(7.1)` is unchanged: writing
`f=K^2+E`, the constant and linear terms of `f^(3/2)` in `E` are polynomial,
so the differential of every tail in every `f`-coefficient direction is
zero along the whole common-quartic locus.  Hence the order-four client has
zero first tail differential, while in the order-two client the differential
has rank at most three (only the three load directions can contribute), less
than the seven tail equations.  Neither client is linearly transverse.  This
still does not license finite determinacy or replace the exact saturation.

## Exact scope

This erratum changes no formula or conclusion in §§0--6 or §8 of the frozen
source audit.  In particular it does not change:

- the raw unloaded seven-tail exceptional fibre;
- its reduced common-quartic support and `P(2,3,4)` chart cover;
- the exact bounded degrees `(8(U+1),12(U+1))` and the `U<=2` classical
  closure only;
- the strict chart, saturation order, denominator list, or independence of
  Kummer order and Rees ramification;
- the fact that a full saturation, both Taylor families, and rational-section
  descent remain open.

It proves no saturation verdict, no Taylor realization, no closure of either
Kummer client, no maximum-twelve theorem, and no statement about JC2.
