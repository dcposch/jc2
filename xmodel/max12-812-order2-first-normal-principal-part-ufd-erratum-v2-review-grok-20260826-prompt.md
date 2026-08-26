# Delta hostile review: principal-part/UFD saturation-slice erratum V2

You are an independent hostile mathematical reviewer.  Work in
`/Users/dc/code/math/jc2`.  Read the corrected target in full:

```text
xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md
SHA-256 4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d
```

Also read the frozen V1 and its hostile review at the two hashes pinned in
target §0.  Treat the V1 review's confirmed identities as charged context,
but independently audit the repaired saturation/slice logic.  Do not run
CAS, Python algebra, Lean, or heavy computation.  Do not inspect or print a
full dirty-worktree status.  The only permitted write is:

```text
xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-review-grok-20260826.md
```

Attack these exact points:

1. Check the definitions and order of `I*` and `I0*`, including saturation
   by multi-generator irrelevant ideals.
2. Prove or refute the sliced-then-saturated reduced-support equality
   `V(I0*)_red=S union D`.  Charge the zero-normal section and density in
   both opens.
3. Prove or refute equality on
   `O=V(k10) intersect D(A) intersect D(n0,n1,n2,n3)`.
4. Prove or refute that both full affine closures `S,D` lie in
   `V(I*) intersect V(k10)` even at their boundary points.
5. Prove or refute the exceptional-set containment: every additional point
   after saturation-before-slice has `k10=N=0` and nonsquare `K`.  Explicitly
   test hypothetical specializations of `k10!=0` branches.
6. Check whether the Padé support lemma `k10!=0 => K square` really suffices
   to make the exceptional set empty, or whether a vertical/embedded/
   nonreduced component creates a remaining reduced-support gap.
7. Confirm that V1 is not silently promoted: (1.1), (1.2), the two
   parameterizations, and arbitrary-load square solution survive, but no
   full radical/reducedness/scheme or strict-arc claim appears.

Give one verdict `CONFIRMED`, `REPAIR`, or `REFUTED`.  If not confirmed,
identify the smallest failing sentence and give the clean exact correction.
Pin the target, V1, and V1-review hashes.
