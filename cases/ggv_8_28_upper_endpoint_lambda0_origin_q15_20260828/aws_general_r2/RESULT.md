# General arbitrary-Q result

The exact compiler and triangular reducer passed.  The reduced system has 41
active variables, five q-compatibility equations, one G13 receiver equation,
89 G14 receiver equations, 73 G15 receiver equations, and the `c2 != 0` open
condition.  Exact and all three modular ranks agreed during reduction.

Every bounded Gröbner/membership discriminator then reached its five-minute
cap without a marker:

| family | p=65521 max RSS | p=65519 max RSS | p=65497 max RSS | result |
|---|---:|---:|---:|---|
| G15-only membership | 15,820,668 KiB | 15,797,616 KiB | 15,804,308 KiB | all rc124 |
| full-base membership | 19,750,916 KiB | 19,750,544 KiB | 19,750,492 KiB | all rc124 |
| full endpoint ideal | 15,014,464 KiB | 15,014,424 KiB | 15,014,392 KiB | all rc124 |

All nine runs recorded zero swaps.  No modular unit, membership, survivor, or
certificate marker appeared, so the frozen verdict is exactly
`NO_VERDICT_MODULAR_SURVIVOR_OR_CAP`.  No exact-Q Gröbner calculation was
started.  Repeating this same prime and term ordering serially is forbidden.

Principal hashes:

```text
d0a722a33e26cd90f8665df234f15036ec133e95636a8f537a253b2aea14595a  JOB_ARCHIVE.tar.gz
b3f1196f9d69fd060c8acfd21d867c6da1b5447af984bbce6013c5c9a4ec0ba6  REDUCTION.json
16a1d0ec3206a0c0a870c7a1395e4bb36e6788c847d30e6be3b445e453a05bd0  ORIGIN_Q15_SYSTEM.json
830ca8fc9276ff8b18b34e59aeb5576a47021fe5013e18201b7c21aa910b79ef  output/TERMINAL
7726acf58f47865aaf561634c10e8cdef89612581fe71f092229502e7c66f5c6  output/VERDICT
88b956244e18a30f4cac3f14d799466ec4333b144ef830ddf9d4627e9eb317c8  records/FINAL_CENSUS.json
18c584672b62674e25534483333b566f3ae9e3876f52ba04a3d7e12f455a1383  EVIDENCE.sha256
```

The worker and monitor both exited zero.  The final census at
2026-08-28T11:03:49Z reports zero members, zero group RSS, and zero swap.

This is a bounded computational no-verdict.  It proves neither endpoint
emptiness nor existence on the fixed proper subbranch and says nothing about
the full lambda-zero face, branch P, JC2, HENS-CT, or `jc2-lean`.

