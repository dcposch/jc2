# AWS launch metadata

Date: 2026-08-26

Both lanes used the frozen V2 source package, a 16 GiB virtual-memory cap,
a 600-second compiler timeout, an 1800-second engine timeout, and the shared
exact-lane wrapper.  No local CAS was run.

| lane | host | characteristic | registered tag | start UTC | engine | elapsed | peak RSS | swap | validator |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| theorem | Box03 / `ip-172-30-0-249` | `0` | `max12_812_order2_p0_cusp_raw_g12_cech_v2_20260826T114504Z_Box03_q` | `2026-08-26T11:45:14Z` | `rc=0` | `0.29 s` | `39844 KiB` | `0` | `PASS_P0_CUSP_RAW_G12_CECH_CERTIFICATE_V2` |
| control | r6d / `ip-172-30-0-45` | `65521` | `max12_812_order2_p0_cusp_raw_g12_cech_v2_20260826T114504Z_r6d_p65521` | `2026-08-26T11:45:14Z` | `rc=0` | `0.12 s` | `29144 KiB` | `0` | `PASS_P0_CUSP_RAW_G12_CECH_CERTIFICATE_V2` |

The exact-Q compiled input SHA is
`726b0feaa3bae6fa0e23b0ffdb0f2e9ca8d1e1eda0396af376034a6707eb1176`;
the `F_65521` input SHA is
`73bd8cc77e94e4a33adefb11829e3e88541b0add4853773ef80e08e02553fd9e`.
The two inputs differ only through the declared characteristic and registered
lane metadata.
