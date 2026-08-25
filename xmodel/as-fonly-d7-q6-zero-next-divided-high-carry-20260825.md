# AS F-only `D=7`: the cumulative zero branch is terminal at the fifth carry

**Status: PRODUCER EXACT AT THE DISPLAYED CUMULATIVE POINT; PROVISIONAL
PENDING DIFFERENT-MODEL REVIEW.**

The canonical Q9 survivor found in the first affine Kuranishi chart has
`x23=x30=1`.  It extends through Q8 with the zero 32-vector, through Q7 with
the zero 18-vector of restored `C6,D6,W5,Z5` digits, and through Q6 with the
zero 16-vector of `H7,J7` digits.  These are cumulative choices: this replay
does not independently reset any earlier representative.

For the resulting integer representatives write

```text
P=P0+3U+9C+27W+81H,
Q=Q0+3V+9D+27Z+81J.
```

If `G4=F/3+{C,D}+T+div(H,J)` denotes the already accepted fourth-digit
row, the next residual is

```text
R = G4/3 + S(U,V;H,J) + Rmix(C,D;W,Z),
Rmix = Cx Zy + Wx Dy - Cy Zx - Wy Dx.
```

The compiler exact-divides every preceding integral row, derives `R`
recursively, and independently expands the literal integer determinant.
For every homogeneous degree from 12 down to 7 it verifies

```text
R = (det J(P,Q)-1)/243  (mod 3).
```

The two byte streams agree, with SHA-256
`b4cee654df3af7f850644a468160be9626fc96659ae98c17715e3d727cf6af12`.
Their nonzero high rows are

```text
R10 = x^10,
R8  = 2 x^8,
```

while `R12,R11,R9,R7` vanish.  A fifth cap-seven correction has divergence
of total degree at most six, so it cannot alter the `x^10` row.  Therefore
this displayed cumulative point cannot extend one more 3-adic digit at
map cap seven.

The source-frozen replay ran only on Box02 (`ip-172-30-0-186`) under tag
`as_q6_zero_next_divided_high_20260825T025049Z`.  It returned zero in 10.71
seconds with 20,724 KiB maximum RSS and empty standard error.  Standard
output has SHA-256
`46fed22942a21d47b12259c7e9aacf02178d975eeaf813f56698da9541c48603`.

This is a pointwise terminal certificate.  The `x^10` coefficient has not
yet been proved invariant under the nine-dimensional Q7 kernel, the
nine-dimensional Q6 fibre, or the thirteen free directions in the earlier
Q8 affine chart.  It therefore does not kill any of those fibres, prove a
fixed-cap theorem, settle an all-depth lift, or imply anything about JC2.
