# B9 `(9,12)` common-cubic Kuranishi structural compression

**Status:** producer-exact; parent reduction different-model CONFIRMED; this
110-row successor awaits focused hostile review.

## Scope and parent

The reviewed parent report
`xmodel/as-b9-9-12-common-cubic-global-fresh-elimination-producer-20260825.md`
and Grok review SHA
`6fc2210f9aa3d364c37d7e371a6653365dc58115dccc114bd3d93e8213b0be7a`
give, above one fixed B9 mod-243 parent, an exact next-layer criterion

```text
K : F3^95 -> F3^176,
```

where the 95 predecessor parameters are `17+78`, all 276 determinant rows and
23 common-cubic rows are retained, and the final fresh55 block has constant
rank 29, kernel 26, and left quotient 176.  This note changes only the output
presentation of that already reviewed map.

## Exact 176 to 111 relation certificate

`analyze_structural_span.py` reconstructs the pinned 34,555-node modular DAG
from emitter SHA
`1d6dbd671e6652592d9de76a74c86034f8f2e9177703c3410c8a05e533963edf`.
Among the 299 pre-quotient next-carry expressions it finds 234 distinct
recursive SHA-256 digests.  It writes every one of the 176 coordinates as an
F3-linear form in those formal atoms, selects original coordinate rows by
exact RREF, and emits an exact relation vector for every omitted coordinate.
The formal row rank is 111.

Box02 and Box03 independently replayed the same source closure.  Both produced
byte-identical certificate gzip SHA
`45b40fd0540e060869a25683c0f5d852a0a24c39e4d04ff17d60af568453d578`
and uncompressed certificate SHA
`d363cc0c5adbf432d8f3d5287ca7fc068801535fc2b5f891511ecd5fd61c0785`.
The reconstructed parent SMT is byte-identical SHA
`108cfdaae0c897ab66518e18d5e38d0969a1f8f936eeb488fd9144e4fbfe0f4c`.
Each replay used about 68 MiB RSS and 12.5 seconds.

The Box02 first launch has a custody-only defect: shell `&` precedence wrote
its wrapper PID in the remote home directory rather than the job directory.
The typed runner itself exited zero, and the clean Box03 mirror has correct
PID/RC custody.  No theorem depends on the missing Box02 PID file.

## Exact constant refinement: 111 to 110

Formal-atom rank intentionally treats distinct DAG digests as independent.
`analyze_structural_span_constants.py` evaluates every input-independent DAG
atom using the exact 2-bit/F3 and 20-bit/mod-531441 semantics.  Exactly one of
the 234 parent groups is constant: group 215 is zero.  It supplies coordinate
row 96 (`n33349`), so it is deleted, not turned into an obstruction.

The resulting exact rank is 110.  Its relation-certificate uncompressed SHA is
`94574911f3a4b39117ddefdd5eab138d134a4a3ccae65a813e478d913c7b2228`;
the Box02 result SHA is
`0b079e314561e1a03139b3c40cd68b6fd459fc0f47ac62df3616792b144d4b27`.
Consequently, on the complete displayed 95-parameter chart,

```text
K(x)=0  iff  K_i(x)=0 for the 110 certified original coordinate rows i.
```

This is the producer theorem.  It is not a sampled rank statement.

## Exact syntactic dependency control

The basis-DAG dependency replay uses the full formula SHA `108cfdaa...` and
all 34,555 definitions.  Ten chart inputs are absent exactly:

```text
a_0, a_1, s_0, s_1, s_2, s_3, s_4, s_6, s_14, s_29.
```

The other 85 inputs form one syntactic incidence component; thus this analysis
does not split the problem into independent blocks.  Support sizes among the
111 pre-refinement basis rows are
`{0:1,48:1,49:1,77:5,80:10,83:17,84:9,85:67}`.  Used supports may
overapproximate semantic dependence after cancellation; absence is exact.
Result SHA is
`865f6e964af4b3b53eed5a8564bb11938d39be0d116a8046b027ffa86f6d839d`.

## Diagnostics and solver custody

The 447-point control design has no zero of `K`, origin support 7, sampled
difference rank 9, and 53 failed univariate-affinity directions.  It does not
globalize: the exact source-DAG rank is 110, not 9.  Z3 4.16 bit-blasting the
full formula failed with `table overflow` after 7m35s and roughly 59.5 GiB;
that is an engine negative only.  The logically equivalent 111-row SMT (one
extra row is identically zero) has SHA
`ed5e5629103c50e526ae268f0052140d49c66dff4dc21f71c3dd0e5a77a10db8`.
Any solver endpoints remain outside this theorem: SAT requires literal integer
reconstruction and all-row replay; UNSAT requires a checked proof or exact
finite-field certificate.

## Firewalls

- One fixed B9 mod-243 parent only; not all normalized or all D12 maps.
- Finite mod-`3^12` transition only; no next-depth or inverse-limit claim.
- No emptiness or survivor claim for the 110-coordinate zero locus.
- No maximum-12 or JC2 inference.  Independently, the exact total-degree pair
  here is `(9,12)` with gcd 3, so the campaign's cited degree-gcd lower bound
  already bars this fixed support from furnishing a characteristic-zero JC2
  counterexample; this computation is methodology/custody evidence.  The
  campaign routing note is
  `xmodel/sol-fixed-total-d12-classical-closure-20260825.md`, SHA
  `71a8c83b923a077b733412fadaae2f03c1c4e50e91fab1249189c6a33eaabf9a`.
