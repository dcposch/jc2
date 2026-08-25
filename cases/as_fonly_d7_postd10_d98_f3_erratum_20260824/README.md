# Erratum: omitted divided Frobenius cross-carry

This package retracts the compatibility columns and literal-F3 censuses in
`as_fonly_d7_postd10_d98_f3_20260824`.  The frozen predecessor bytes remain
unchanged as quarantined provenance.

Replay:

```sh
python3 replay_omitted_frobenius_carry.py
shasum -a 256 -c MANIFEST.sha256
```

The replay derives two exact integer witnesses for the omitted
`[K_Frob/3] mod 3` term: degree eight on the vertical branch and degree nine
on the `g != 0` endpoint.
