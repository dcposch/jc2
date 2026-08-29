# TD6 V84R2 disjoint q-block producer report

Date: 2026-08-26 06:55Z

Verdict: **PRODUCER PASS, NARROW PREVIOUS/POLE SCOPE**.

The registered r6d exact replay of block `(0,1)` completed with `rc=0`.
After rank-3470 transport, rank-38 FIRST, and rank-38/94 previous/pole
reduction, all 16 pairs

```text
q_i q_j,  i in {2,3,4,5}, j in {6,7,8,9}
```

have zero pairing with the unique previous/pole leftover.  The exact table
is header-only with SHA-256
`b93bed47384146af9d18c44cc51897aa95455094fa55cec51470d2ea3cc737ab`;
the denominator is the unit `(1, [])`, SHA-256
`8041f53d2bb2b7e92f9e047d2ca6bad668bac36b5f2a1e0a146cec71be70af43`.
The stdout SHA-256 is
`5032c74efa921ab7d7d980a4699fa37c4b803f4df6aa2acaa76872d4ae6955e5`
and the source archive SHA-256 is
`71934436bf932284f136d7742b398208504ef59bc07f29969bad91e6bf32abc3`.

This supplements, but does not broaden, reviewed V84R2.  It is fixed A3,
common generic open, and previous/pole only.  The full current system is
inconsistent, so no tangent, nonlinear family, whole TD6, SP-2, landing, or
JC2 inference follows.  Hostile review is not yet attached to this disjoint
block; producer work continues nonblockingly toward the exact current
obstruction on the 24-dimensional Stage-A kernel.
