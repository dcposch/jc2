# Sparse syzygy r1 adapter failures

Both fresh AWS jobs passed EC2/idle/zero-swap preflight, exact source and
preregistration checks, solver self-check, and exact receiver-row
deduplication.  The independently emitted `DEDUP.json` was identical in both
jobs:

```text
eabe45db71777edc56f3b3d1717a6fd4f3f3c71c44fdf318d71a9babe3447a57
```

It certifies representative counts `q=5, G13=1, G14=5, G15=5`, with 17
generators in the exact full base.

The sparse adapter then stopped before constructing either linear system.  It
incorrectly asserted that the endpoint was homogeneous; the exact endpoint
has term degrees `{3,4,5,6,7}`.  Each solver stage exited 1 in 0.10 seconds,
and neither job emitted `CERTIFICATE.json`.  Their generic top-level
`NO_VERDICT_MODULAR_SIGNAL_ABSENT_OR_CAP` strings are superseded by the exact
classification `ADAPTER_FAILURE_INCORRECT_HOMOGENEITY_ASSERTION`.

Custody:

```text
739db1684e532df160f87aaa430d5690afce5e00b20706c6a83d308bbffd6e91  g15 archive, 102 files replayed
f1598f420d1e916b38687b93c700c632ac2ebab41fbb0ffe0a342ad74ce4e306  full archive, 102 files replayed
c66677a41f4da870de0fc3dd9a64d3a0adab87d25539b5c3feb105403a1f2f69  g15 traceback
6c33500e237b9d8163a092445d1ea7b953545c5a11eb7512d9c8718999d923c8  full traceback
ba369c39033b2393fe6cd27ec38f54bf34041924a5e262a790e3181ca1f7d332  g15 final census
044c0477bd84936fee544fe32452c469c92d61a7450051330755bac82752c0c8  full final census
```

Both final censuses contain zero members and zero swap.  These runs contain no
mathematical signal of any kind.

