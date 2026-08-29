# Addendum: fan-report custody used by the V12 source-support erratum

Date: 2026-08-26

This is a nonmutating custody addendum to
`xmodel/max12-812-order2-square-r1-d1-v12-source-support-erratum-20260826.md`
(SHA-256
`997dda081223d99283bff92851e7da8bc260b7b3e52ff89b97fb0a50c817a114`).

The historical amended fan report with SHA-256
`0d373399b47a4b53686a381f587e6912b9004915544f6116cf08ad168865a075`
is preserved byte-for-byte at

```text
cases/max12_812_order2_square_positive_load_fan_z3_20260826/RESULT_V1_PRE_COUNT_CORRECTION.md.
```

The current corrected report is

```text
e43bc4b2a454e84964d4a2e99479d521841304e1b55c0d47a652ad920a649c0f
  cases/max12_812_order2_square_positive_load_fan_z3_20260826/RESULT.md
```

and its count erratum is

```text
bad003fdb74ffd81e52d6325df3d78bb1d53ebf18d4b9c2ac04de8c040b2570f
  cases/max12_812_order2_square_positive_load_fan_z3_20260826/RESULT_COUNT_ERRATUM.md.
```

The current report correctly says **seven** enumerated forms and
`1016=(2^7-1)*8` active-set/boundary candidates.  This bookkeeping repair
does not change the source-support erratum's mathematical point: the
seven-form enumeration omits lower-load and target support and is navigation
only.
