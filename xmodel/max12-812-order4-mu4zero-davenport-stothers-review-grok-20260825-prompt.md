# Hostile review request — Shioda/Hall divisor-19 elimination

Act as an independent hostile mathematical reviewer.  Read the immutable
target and every charged local source in full.  Independently verify the
primary-source statement and rederive or break every bridge.  Do not use a
producer or prior reviewer verdict string as evidence.

Immutable target:

```text
a5d40fd81838118735c4c2ad379bbac0a1e7d70a66a4a419eff078e8099d7b03
  xmodel/max12-812-order4-mu4zero-davenport-stothers-elimination-20260825.md
```

Charged local sources are exactly those named and hashed in target §1 and
§6.  Primary source:

```text
T. Shioda, Elliptic Surfaces and Davenport-Stothers Triples (2005)
DOI 10.14992/00008689
https://rikkyo.repo.nii.ac.jp/record/8708/files/AA00610867_54-01_04.pdf
expected PDF SHA-256:
467701925109586976ca8f89ec614ee95c5ad740084b969a93ba3795b0cdb740
```

Audit at least the following.

1. Verify from Shioda §5 the definition of essential equivalence, the exact
   Hall `m=4` polynomials and sign, `St(4)=1`, and Theorem 5.1.  Decide
   whether applying the unique orbit over the algebraic closure of the
   Kummer function field is licensed; attack the stated ACF0/Lefschetz
   transfer.
2. Starting only from the charged tail convention, recompute
   `W=g^2-f^3=-2r_7 z^5+O(z^4)` when `g=F12(f)` and `r1=...=r6=0`.  Check
   signs, the `w`-to-`z` conversion, nonvanishing, and the exact use of
   Davenport's lower bound to obtain an order-four DS triple.  Keep the
   `mu4!=0` degree-eight case separate.
3. Starting from the full affine/scaling equivalence, solve the monic and
   depressed constraints.  Recompute `c=alpha^-4`, `beta=-3/4`, the
   translated Hall coefficients `21/4` and `11/4`, and the leading
   coefficient `27 alpha^-19` of `g^2-f^3`.  Check that the two coefficients
   really descend `alpha` from `Mbar` to `M` and that
   `r7=-(27/2)alpha^-19` has divisor orders divisible by nineteen.
4. Hostilely rederive the divisor argument on the smooth normalization of
   `u^4=h`: the number of places and local orders at a root of multiplicity
   `m`; why inertia forces `r7(P)=0` for `m<4`; why the resulting orders are
   `3,1,1`; the nonzero residue at `m=4`; the pole order and total pole
   degree for `m>4`; and why an unramified finite zero would have order one.
   At infinity check all four places, transitivity, existence of a zero,
   order `U-1`, and degree balance.  Look specifically for a loophole from
   nonzero integration constants on different sheets or from residue
   cancellation.
5. Verify the concrete order-two `U=2,[6,2]` corollary only on the stated
   all-`k`, all-`mu` zero sub-stratum.  Check `T^2=(x-1)/x`,
   `r7=(j/4)T`, `div(T)=[0]-[infinity]`, and why nonzero loads lie outside
   the DS argument.
6. Enforce the firewall: even confirmation eliminates only the whole
   order-four `mu4=0` terminal stratum and the named closed order-two
   zero-load sub-stratum.  It does not eliminate `mu4!=0`, the remaining
   order-two client, the order-one leaf, `(8,12)`, maximum twelve, or JC2.

Write exactly one report and edit no other file:

```text
xmodel/max12-812-order4-mu4zero-davenport-stothers-review-grok-20260825.md
```

Include the exact target SHA, every consumed source hash, model identity,
an explicit verdict `CONFIRMED`, `REPAIR`, or `REFUTED`, the smallest failing
identity or missing hypothesis, a complete independent proof/attack, and a
strict scope firewall.  This is source reading and hand derivation only:
run no CAS, solver, substantive Python, Lean, or other heavy local
computation.
