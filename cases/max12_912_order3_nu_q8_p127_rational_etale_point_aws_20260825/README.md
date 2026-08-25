# Selected-Q8 `p=127,w=71,v=50` rational-point/etaleness check

This AWS-only exact control starts from the pinned pure-Singular fixed-fibre
generator, adds `v-50`, reconstructs the unique rational point, and evaluates
the determinant of the relative Jacobian of the original eight localized
generators with respect to
`(c,d2,d4,x1,x3,x5,inv,v)`.

If the point ideal has vector-space dimension one and the determinant is a
nonzero constant, it is a smooth rational point of the total curve and the
map to the `w`-line is etale there.  This does not by itself prove arithmetic
or geometric irreducibility of the generic degree-190 algebra.

Run only on AWS:

```sh
./run_remote.sh REPO OUT_ROOT q8_p127_w71_v50_etale_v1
```

