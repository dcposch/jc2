# Candidate `H(w,v)` plane-curve integrality over `F_127`

This small AWS replay proves only that the explicit monic degree-190
candidate `H(w,v)` defines a geometrically integral plane curve over
`F_127`.

It independently factors the exact specializations at `w=25` and `w=47`,
checks their squarefreeness, and verifies the smooth rational point
`(w,v)=(71,50)`.  The factor-degree subset-sum argument is:

```text
proper subset sums at 25: {2,188}
proper subset sums at 47: {1,3,4,186,187,189}
intersection: empty.
```

Because `H` is monic in `v`, any factor over `F_127(w)` extends monically
over `F_127[w]` and keeps its `v`-degree under both specializations.  The
empty intersection therefore proves arithmetic irreducibility.  The smooth
`F_127`-rational point removes a nontrivial constant-field extension, hence
gives geometric irreducibility.

This does **not** prove `H` belongs to the selected-Q8 quotient ideal or that
the plane curve is a quotient component.

