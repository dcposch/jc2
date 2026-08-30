# Hostile review: cubic discriminant/conductor invariant

You are Opus 5, an independent hostile algebraic reviewer for the plane
Jacobian-conjecture campaign. Work in `/Users/dc/code/math/jc2` on frozen git
basis `f89cbb02305ee6fef32a79ccb8ff53fc4740a2a1`.

Review this sealed exact producer:

```text
327b1f42b3ee245d1383d0108feca4c5ae20cbdaf5a00545f1c1d7fd5cee81d7
  xmodel/bd-fix3-quadratic-discriminant-conductor-invariant-sol56-20260830.md
  body 6323 / 3362a7913801a180cf0d4ee06e9bf08ee13324ea598d72e0e8f797d59ff28ac5
c8dee3199ecfaf73b6debedea625346a11babbe42082cff5bff049f8585763c2
  xmodel/bd-fix3-affine-linear-log-closure-coordinator-integration-sol56-20260830.md
e3dc96f07825ea882edc3d2701e9f0a0357ae863c062ad695d9377a37aa2b761
  xmodel/bd-a2-bidegree23-rational-forest-classification-coordinator-integration-sol56-20260830.md
```

Independently reconstruct and attack:

1. For a finite locally free generically separable rank-three algebra with
   trace splitting, verify the trace Gram determinant under every global
   `GL2(A)` trace-zero basis change. Check that `A=C[u,v]` makes the
   determinant a constant unit and state exactly whether the discriminant
   polynomial, ideal, divisor, or zero scheme is basis-invariant.
2. Starting from the displayed Miranda multiplication table in the AL3
   integration, recompute `Tr(z^2),Tr(zw),Tr(w^2)` and the full determinant.
   Compare it to the binary-cubic discriminant, including every sign/scalar.
   Verify the coefficient-degree-four and target-degree-at-most-eight claims;
   attack cancellation and identically-zero cases.
3. Audit the statement that support is the non-etale/branch divisor. Separate
   trace discriminant multiplicity, different, reduced source ramification,
   and target branch/discriminant support. Check the required separability,
   flatness, normality, and characteristic-zero hypotheses.
4. Reprove height-one-locally the order/normalization identity using an
   inclusion matrix over a DVR. Decide the exact global object represented by
   `ord(det M)`, its relation to the divisorial part of `Fitt_0(Otilde/O)`,
   and what changes if the normalization is only finite torsion-free rather
   than locally free. Check effectivity and divisor orientation.
5. Attack every proposed conductor/curve interface. Confirm that curve delta
   length needs an actual slice, flat base change/Tor control, and the correct
   order; give a minimal counterexample or warning if any report wording is
   still too strong.
6. Judge the maximum basis-safe campaign consequence and the cheapest two
   strict-henselian controls before any AWS sieve. Explicitly reject the false
   shortcuts “square leading discriminant implies Galois” and “degree-eight
   discriminant implies low-degree Miranda basis.”

Return an itemized verdict (`CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or
`REFUTED`), the maximum exact theorem safe to promote, precise corrections,
and a bounded next-test specification. No quadratic/cubic block closure,
primitivity, map claim, counterexample, or JC2 claim.

Hard output cap: at most 8,000 tokens and at most 28,000 UTF-8 bytes. Do not
restate long inputs. Do not inspect, list, search, stat, build, modify, or
control `jc2-lean`; the process sandbox also enforces this. Do not run local
heavy CAS or Singular. Do not edit any input, canonical file, script, or
dependency. Write exactly one report:

```text
xmodel/bd-fix3-quadratic-discriminant-conductor-invariant-hostile-review-opus5-20260830.md
```

End with one standalone `<!-- BODY-END -->` line and no seal block.
