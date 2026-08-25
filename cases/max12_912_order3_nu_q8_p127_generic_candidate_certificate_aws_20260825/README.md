# Selected-Q8 generic degree-190 candidate certificate over `F_127(w)`

This AWS-only successor consumes the root-owned interpolation candidate
`H(w,v)` (SHA pinned below), computes the exact original localized quotient
over `F_127(w)` in pure DRL, and tests whether `H` reduces to zero modulo its
Groebner basis.

Required endpoint:

```text
generic_dim=0, generic_vdim=190,
candidate_v_degree=190, candidate_monic=1,
candidate_remainder=0.
```

Together with the exact fixed specializations at w=25 and w=47, this endpoint
would prove `H` irreducible by the disjoint subset-sum certificate.  Since an
irreducible degree-190 subalgebra then embeds in a quotient of total dimension
190, the generic quotient is that field.  Constant-field removal and
characteristic-zero lifting remain separate.

The candidate is copied byte-for-byte from root's AWS interpolation V6:

```text
interpolation_candidate.json
  9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce
```

Run only on AWS, with independent engines/hosts where possible:

```sh
./run_remote.sh REPO OUT_ROOT TAG std
./run_remote.sh REPO OUT_ROOT TAG slimgb
```

