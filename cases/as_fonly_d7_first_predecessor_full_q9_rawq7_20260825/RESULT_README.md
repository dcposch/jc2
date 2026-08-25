# Complete first-predecessor Q9-fibre proof custody

The frozen producer makes all 19 Q9-kernel trits, all 32 raw Q8 digits, and
all 18 raw Q7 digits symbolic over the first corrected-Q10 predecessor
`c5_5=2` (all other predecessor coordinates zero).  It imposes all
23/22/19 source rows and all 46 terminal-high rows.  The checked formula is
UNSAT.

```text
host/job  Box02 /home/ubuntu/jobs/as_first_predecessor_full_q9_rawq7_20260825T0712Z
SMT2      0061e1ccd62c849d54db9258247413d8fe80bf8cdf696ef987ea904fae89fd5d
CNF       a25c7ed0f48766548fc518f9de2b4c7d4e51e413c085dc30f68d6668f1928369
DRAT      b8dbb0649833f5c545190e6b56e0efb4c9721385f08a553fdfd92d25ff956eda
checker   s VERIFIED
```

The repository custody archive is
`results_box02_full_custody/full_custody.tar.zst`, SHA-256
`601076db6aa5f27e74315657baf7c5a87c2ad64982011612064ee26c1c3f5649`.
Routine verification should hash it rather than extract it.  Full replay is
AWS-only.

Strict scope: one corrected-Q10 predecessor and its complete 19-dimensional
Q9 fibre.  The other 11,880 compatible predecessors and all nonvertical
boundary families remain open.

