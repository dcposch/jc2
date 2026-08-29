# Hostile review of Opus5 `L43` support theorem

Date: 2026-08-27  
Reviewer: Sol (different model from the Opus5 producer)  
Verdict: **CONFIRMED WITH STRICT SCOPE CORRECTIONS**

## Reviewed claim

Opus5 reported that the 51 nonzero frozen ordered-`a1`, `rho=0` raw rows
through grade 19, in 65 occurring variables, have a maximum coordinate-linear
zero section of dimension 43.  The displayed section sets 22 variables to
zero and leaves `k` free.

Producer report:

```text
0fbb452456a34b24b28b35a9fd0f99fc6ac86f81edab7a704369aeba0b7881da
  xmodel/ideation-20260827T0635Z-opus5.md
```

## Independent exact replay

The replay parses the hash-pinned V37 row corpus, independently rebuilds the
set of distinct monomial supports and its inclusion-minimal antichain, and
checks a short combinatorial optimality certificate.  It does not trust the
producer's branch-and-bound implementation.

```text
3f8ab1d4888c4f4c22894e32a2df46e4a52291e4b8e198c1f29f15eea0b30aeb
  cases/max12_812_order2_p0_total_rees_j2_a1_support_hypergraph_l43_review_v40_20260827/replay_l43_review.py
ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b
  cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_20260827/solve_graded_ladder_v37.py
```

Replay:

```sh
python3 cases/max12_812_order2_p0_total_rees_j2_a1_support_hypergraph_l43_review_v40_20260827/replay_l43_review.py
```

The exact census is reproduced:

```text
70 named rows; 51 nonzero rows; 65 variables
4,997 distinct monomial supports
88 inclusion-minimal supports: 11 singletons, 54 pairs, 23 triples
```

The eleven singleton supports force every hitting set to contain

```text
a1, aa0, aa1, e0, e1, ec3, ec4, ee0, ee1, ez3, ez4.
```

After those forced vertices, the replay verifies the following eleven
remaining minimal supports are pairwise disjoint and disjoint from the forced
set:

```text
{aaa0,ez7}       {az3,ec6}       {ac3,ez6}
{k6_1,rs1}       {k2c,rs2}       {aaa1,ec7}
{cs1,k10_3}      {k,rs3}         {az4,ec5}
{ac4,ez5}        {cs2,ell1,k1}
```

Consequently every hitting set has size at least `11+11=22`.  Opus5's
displayed 22-variable zero set hits every one of the 88 minimal supports (and
hence all 4,997 supports), so the minimum hitting-set size is exactly 22 and
the maximum coordinate-zero-section dimension is exactly `65-22=43`.
The replay additionally emits a separate minimal-support witness for each of
the 22 zeroed variables, proving that this displayed section is
inclusion-maximal as well as maximum-dimensional.  Direct monomial
substitution leaves no surviving term in any of the 51 rows.  `k` is free;
`a1` is forced to zero.

## Scope corrections

The supported statement is:

> The homogeneous raw ordered-`a1`, `rho=0` row system through grade 19 has a
> maximum 43-dimensional coordinate-linear zero section meeting `D(k)`.

It is **not** any of the following:

- an all-depth theorem (only literal K00 currently has the all-depth raw
  replay);
- a general-`rho` theorem beyond separately available grades;
- proof that this linear subspace is an irreducible component of the raw
  scheme;
- an honest saturated-Rees, receiver, chart, routing, Gate-T, or JC2 result;
- a `T-a1` obstruction, since this section has `a1=0`;
- a license to evaluate honest receiver equations at a "generic L43 point"
  without first constructing a typed map from those 43 raw coordinates to the
  receiver presentation.

Thus Opus5's exact support theorem and preflight mechanism survive review;
the phrases "43-dimensional component" and "generic-L43 honest-equation
test" require the corrections above.  The proposed row-32/secant interface
remains speculative until its input/output types are explicitly matched.

## Disclosure

The reviewer read the producer report, the V37 loader, and the frozen rows
through that loader; ran only desk-scale exact Python set/combinatorial
arithmetic; used no CAS, AWS, network, or `jc2-lean`; and wrote only the replay
script and this report.
