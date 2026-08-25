# Q8 `F_127(w)` candidate-seeded quotient

This AWS-only diagnostic inserts the reconstructed monic candidate
`H(w,v)` into the exact selected-Q8 generic ideal and computes the quotient

```text
J = I + (H)  over F_127(w).
```

The candidate is pinned byte-for-byte to the successful 123-fibre
interpolation run.  Its `v`-degree is 190 and its coefficient `w`-degree is
at most 21.  Multiple variable orders, generator placements, and exact
Singular engines are independent performance/certificate lanes.

An exact zero-dimensional result with `vdim(J)=190` is useful but does **not**
alone prove `H in I`: that conclusion additionally needs an independent
certificate that the generic quotient by `I` is zero-dimensional of length
at most 190 (or a direct reduction of `H` by a standard basis of `I`).  With
that certificate, the quotient map `K[x]/I -> K[x]/J` and equality of the
two finite dimensions force `I=J`, hence `H in I`.

All Singular work is run on AWS.  A lane is invoked as

```sh
./run_remote.sh REPO OUT_ROOT TAG --engine std --order dp \
  --permutation canonical --placement first
```

