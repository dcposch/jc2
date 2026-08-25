# Q9-to-Q8 witness gate V2: emit the obstruction

V1 was source-frozen and ran with a witness-required assertion.  It exited
`1` when the first emitted Q9 canonical witness had no 32-variable Q8
transition.  V1 is preserved as a fail-closed deployment negative control
and supplies no verdict by itself.

V2 consumes V1 byte-for-byte through its definition prefix.  It must emit
the 13-row accepted-image rank, full 22-row coefficient/augmented ranks, the
induced nine-row Kuranishi rank, and—when incompatible—an explicit vector
`lambda` satisfying

```text
lambda*A = 0,        lambda*b != 0 mod 3.
```

The compiler verifies both identities directly against the original exact
source-derived matrix.  A certificate supported only in the final nine rows
is a pointwise Q8 obstruction after the accepted-image rows; support in the
first thirteen rows instead identifies an earlier reconstruction error.

No conclusion about other points of the same Q9 affine fibre is licensed.

