# max12 `(9,12)` corrected-Q8 global quotient gate

This case compiles the exact approximate-cubic parity-involution quotient,
localizes its genuine Q8 chart, and Hensel-lifts the selected branch through
`w^5`.  The selected algebraic branch closure is one-dimensional by the
reviewed rank-six formal-IFT input.  The two modular standard bases are
routing evidence only and do not prove a characteristic-zero dimension
statement for the whole localized scheme.

```sh
python3 cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/replay.json -
shasum -a 256 -c cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/MANIFEST.sha256
```

The replay is intentionally substantial: it runs the exact local series and
two Singular standard bases.  No whole-scheme dimension theorem, global
plane equation, or trajectory exclusion is claimed.
