# AS109 exact-lift partial-`y` floor twelve — theorem-interface composition

Date: 2026-08-26

Producer: Opus 5 blind ideation lane, extracted into
`xmodel/ideation-20260826T2230Z-opus5-blind-extract.md`.

## Claim

Let

```text
P = x - x^109 + 109*A,
Q = y + 109*B
```

belong to `Z_109[x,y]`, and suppose `det J(P,Q)=1`.  Then

```text
max(deg_y(A),deg_y(B)) >= 12.
```

## Proof

If both correction degrees were at most eleven, then over `Q_109`

```text
deg_y(P) <= 11,
deg_y(Q) <= max(1,deg_y(B)) <= 11.
```

The promoted maximum-eleven theorem therefore makes `(P,Q)` a polynomial
automorphism over `Q_109`.  But the reviewed AS109 Hensel bridge says that
each of the 109 source balls `(a,b)+109*Z_109^2` maps bijectively to the same
target ball `(0,b)+109*Z_109^2`; hence the map is noninjective over `Q_109`.
Contradiction.

## Scope

This is conditional on an exact integral polynomial lift in the displayed
AS109 coordinates.  Partial `y`-degree is not invariant under arbitrary
source changes.  The conclusion supplies no lift, support bound, marked
collision, routing into an exact degree-twelve cell, arbitrary-support no-go,
counterexample, or JC2 result.

