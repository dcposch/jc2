# Registration: relative cone extraction from the full affine-Faber `K` support

Date: 2026-08-26

Status: preregistered exact support analysis; navigation only.

## Input

The exact-Q 371-term stdout from the frozen full-`K` support producer,
SHA-256

```text
1fd637a6918608b488c8e30e134f9a911354f7394ea83741634e04cdc5a7606b.
```

## Questions

1. Group equal valuation monomials while retaining their exact coefficient
   polynomial in the unit variables `M,E`.
2. On the fixed delayed schedule

   ```text
   a:5, lambda:15, X:Y:q, R*:S*:2q,
   K10:K6:K2:mu2:42, mu4:48, mu6:54, J:57,
   ```

   determine the exact raw-`K` threshold relative to the intrinsic weight
   45, its equality terms, and the margin at `q=6`.
3. Record the Pareto-minimal load and target forms and exhibit whether a
   lower load slope can beat or tie the intrinsic term.

This client does not reduce by predecessor initial ideals.  In particular,
it must label the row-system wall `30+2q=42` (`q=6`) separately from the raw
`K` threshold, and it must not promote either wall to a coverage theorem.

Exact rational parsing runs only on AWS.  The F65521 stdout is an
independent support-sequence control; characteristic-zero coefficients come
only from the exact-Q stdout.
