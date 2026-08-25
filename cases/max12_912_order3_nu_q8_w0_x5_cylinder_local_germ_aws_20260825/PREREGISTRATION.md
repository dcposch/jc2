# Preregistration: finite `x5=0` cylinder local-germ gate

Date: 2026-08-25  
Status: **FROZEN BEFORE CAS**

Let `X=V(I)` be the six-row approximate-cubic source over
`Q[w,c,d2,d4,x1,x3,x5]`, localized at `x3!=0`. Define the explicit cylinder

```text
B: x5=0, x1=x3, d2=d4=0, c*x3=1.
```

This producer must verify from the exact source that:

1. every one of the six rows vanishes modulo the full cylinder ideal with
   `w` free (not merely after `w=0`);
2. every `w` derivative vanishes on `B`;
3. the full six-by-seven source Jacobian has rank exactly five at every point
   of `B`: all seven six-by-six minors vanish, while the five-by-five minor
   obtained by dropping row `e5` and coefficient column `c` is
   `1024*x3^6/1594323`, hence a unit on `x3!=0`;
4. the two tangent directions are the `w` direction and the cylinder
   `x3` direction `(-x3^-2,0,0,1,1,0)` in
   `(c,d2,d4,x1,x3,x5)`;
5. exact normal forms of `e6=r6` and `e8=r8` on the whole cylinder are
   retained.

The local-algebra consequence is separate from the CAS: since `B` is a
smooth twofold contained in `X`, the rank-five certificate makes every local
ring `O_(X,q)`, `q in B`, a regular local domain of dimension two. The
surjection to the dimension-two local ring `O_(B,q)` then has zero kernel;
otherwise a nonzero ideal in a Noetherian local domain lowers dimension.
Thus `X` and `B` have identical local germs along finite `x3!=0`.

This excludes incidence of the closure of `X intersect D(x5)` with a finite
point of `B`; it does not classify the overlap `x3=0`, the limit `x3=infinity`,
projective coefficient escape, or any separate trajectory leaf globally
contained in `x5=0`. Terminal/Taylor use of the output normal forms is a
successor, not part of the source-germ claim.

Acceptance requires two independent AWS engine/order lanes, zero literal-row
remainders, all stated tangent/Jacobian identities, exactly one PASS marker,
and no Singular diagnostics.
