# Ratio-reduced selected-Q8 vertical bound

At generic fixed `w`, substitute the exact ratio identity

```text
x3=(v+2)*x5
```

into the six divided source rows.  This leaves six equations in
`(c,d2,d4,x1,x5,v)`.  The AWS replay combines every coefficient exactly as a
polynomial in the generic parameter `w`, then computes raw and origin-
augmented six-dimensional mixed volumes.

The selected localization has `x5*v!=0`; nevertheless the origin-augmented
value is retained as a safe affine overcount.  A bound below `380` would force
at most one `H` pushforward multiplicity because `deg_v(H)=190`.
