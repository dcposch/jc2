# Selected-Q8 coordinate reconstruction over `F_127(w)`

This is an AWS-only successor to the exact pure-Singular fixed-fibre sieve.
For a fixed nonzero `w` it recomputes the original localized eight-generator
ideal, then asks Singular's `stdfglm` for a reduced lexicographic basis with
`v` last.  On a primitive degree-190 fibre the expected shape basis is

```
c-C(v), d2-D2(v), d4-D4(v), x1-X1(v), x3-X3(v),
x5-X5(v), inv-U(v), H(v).
```

The first lane is a bounded control at `w=25`.  Only after its basis reduces
all eight original rows to zero and has the expected shape should further
fibres be dispatched.  The intended successor interpolates the seven shape
coefficients rationally in `w` and verifies the reconstructed formulas by
direct substitution modulo the candidate `H(w,v)`.  Such a substitution
identity would be a generic certificate; fixed-fibre shape bases alone are
only exact specialization data.

All substantive computation must run on AWS.  No msolve output is consumed.

