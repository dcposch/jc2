# V2 erratum/preregistration: two-parameter D1 weighted infinity

Date: 2026-08-25  
Status: **NONMUTATING SOURCE SUCCESSOR; NO ALGEBRA VERDICT**

V1 remains immutable.  V2 makes one source repair and two mathematical
typing clarifications.

1. `compile_exceptional_v2.py` hashes V1 and changes exactly one `]` to `])`
   at the unique registered syntax anchor.  No mathematical source changes.
2. For a rational pole, the slope is `m/n>3` with

   ```text
   Q=s-1=tau^n, Lambda=tau^m,
   B_i=tau^(m(9-i))*A_i(1+tau^n).
   ```

   Equivariance requires jet exponents congruent to `m(9-i) mod n`.  The
   denominator is bounded on any fixed active set, but `m` is unbounded, so
   V2 makes no universal finite weight-20 jet claim.
3. At `s=1` the exceptional calculation is evaluated on the `t=1` sheet.
   The other cube-root sheets are the same weighted orbit, so vanishing of
   all descended exceptional rows is equivalent to vanishing of the eight
   original tails.  The projective ideal is saturated by the irrelevant
   ideal.  Saturation removes components supported only at the affine
   origin; it does not remove the origin as a point of the affine cone.
   `Proj` ignores that irrelevant point.

The global characteristic-zero job computes scheme/minimal-prime thickness
and two ideal containments.  It is a control for the separate Mason--Stothers
radical-support proof, not a replacement for that proof and not a normal
deformation theorem.

