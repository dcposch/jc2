# Selected-Q8 generic `F_127(w)` DRL-to-block-FGLM certificate

This AWS-only successor computes the exact localized generic quotient over
`F_127(w)`.  It keeps the pinned block target order with `v` last, but asks
Singular `stdfglm(I,"std")` to compute first in DRL and convert by FGLM.

The desired endpoint is a zero-dimensional generic algebra of dimension 190
and one monic squarefree degree-190 eliminant in `v`.  Such an endpoint gives
the common generic eliminant needed to license the fixed-fibre subset-sum
sieve.  Irreducibility and characteristic-zero lifting remain separate
lemmas.

All substantive computation must run on AWS:

```sh
./run_remote.sh REPO OUT_ROOT q8_generic_p127_stdfglm_v1
```

`generate_drl.py` / `run_drl.sh` is the cheaper first stage: it computes only
the generic DRL basis and its vector-space dimension, before any FGLM or
factorization.

