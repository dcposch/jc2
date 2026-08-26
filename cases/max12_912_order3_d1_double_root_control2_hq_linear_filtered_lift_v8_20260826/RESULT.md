# Result: 24-column hQ lift closes the eta half-line in the fixed chart

Date: 2026-08-26 UTC

Status: **PRODUCER-TIER EXACT DUAL-AWS RESULT; HOSTILE REVIEW REQUIRED.**

## Exact endpoint

Both registered encodings returned `SOLVABLE`.  The complete projected
system has 18 monomial equations, 24 preregistered columns, rank 9, and
zero-based pivots `0,...,8`.  With the canonical column order

```text
(row 1,q2), (row 1,q1), (row 1,q0), ...,
(row 8,q2), (row 8,q1), (row 8,q0),
```

the free-zero solution has exactly two nonzero coordinates:

```text
(row 1,q1) = -1/36,
(row 2,q0) = -1/72.
```

Thus, starting with the frozen V7 multipliers, the additional correction is

```text
F1^(8) = F1^(7) - (1/36) h q1,
F2^(8) = F2^(7) - (1/72) h q0,
Fi^(8) = Fi^(7),  i=3,...,8.
```

The exact product `sum_i F_i^(8) E_i(h)` is a 48-term polynomial of
canonical SHA

```text
e549fd6879763d9f6804b9fcc17327e114bd54e29180246cc0b2e7c632fff38b
```

and is an identity in the full frozen Q/R/h ring, not a congruence.  Its
h-zero slice is the reviewed q2 witness, and the complete projected union

```text
h-linear Q-R  +  h-linear (R^2 or Q^3)  +  h-linear Q^2 R
```

vanishes.  The input h-linear Q-squared-R component has exactly eight terms
and SHA

```text
6c42c451732eba42d43402f2175510dc87b901fe986d82f500c4bdb9c1b0048b.
```

## Fixed-chart weight theorem emitted by the producer

Keep the pinned ordinary-tail eight-row module at

```text
a=1, p=-3, c=2+h, k=nu=0, mu=2/3,
```

with full Q and R support and fixed loads.  Normalize `wt(la)=L` and put

```text
alpha = 15/2,
beta  = 5+u,
delta = 5+v,
eta   = wt(h)/L.
```

For every `u>0`, `v>0`, and `T>0`, the 48-term identity has unique
least-weight term `la^20` whenever `eta>=0`.  This bound is uniform and
sharp as a bound over the whole open `(u,v)` quadrant: for negative eta,
one of the displayed h-positive zero-corner-margin terms wins after taking
its positive `u/v` margin sufficiently small.

The exact record scan has h-degree histogram `37+10+1` in degrees
`0,1,2`.  Its eta infimum is zero.  At eta zero, all 30 non-target terms on
the closed-corner face have a positive `u` or `v` coefficient; hence every
one is strictly above target on the open quadrant.  The split target
`la^20*tau` is strictly above by `T>0`.  No negative-corner-margin term
remains.  In particular this one finite polynomial witness covers every
positive h valuation in this fixed chart; no h-adic convergence claim is
needed for that statement.

## Dual custody

| Host | Tag | Worker PID | Order | JSON SHA | Elapsed / max RSS / swaps |
|---|---|---:|---|---|---|
| Box03 `98.80.65.144` | `max12_912_order3_d1_double_root_control2_hq_linear_filtered_lift_v8_20260826T043000Z_box03_forward` | 158757 | forward | `574c19699bcd95c282c45c7d70706c9ff9e0ecc830c535a1cbcf7271f020761f` | 5.92 s / 22,384 KiB / 0 |
| r6d `100.26.198.153` | `max12_912_order3_d1_double_root_control2_hq_linear_filtered_lift_v8_20260826T043000Z_r6d_reverse` | 226117 | reverse | `f4fb41f61ed185aba053d0f19fd5b132f04ca0e79516f022ec8159900e7fc666` | 5.91 s / 22,468 KiB / 0 |

Both runs have rc 0, empty compiler stderr, exactly one PASS endpoint, and
successful frozen source checks.  After deleting only the preregistered
`tag` and `order` fields, the sorted certificates are identical with SHA

```text
7bae4055e967eaa29831415a1432b04016747759ea56c62b55e4002f1f7e6c0b.
```

## Firewall

This result is exact only for the pinned axis/cusp, fixed loads, charged
ordinary-tail rows, full Q/R support, and the stated `(alpha,beta,delta)`
cell.  It is not a moving-axis or moving-load theorem, not a proof that all
normal directions have been activated, not a whole-double-root-fan result,
and not D1 or JC2.  The 24-column RREF is complete only for its stated
filtered projection; the stronger weight conclusion comes from scanning
every term of the resulting full polynomial identity, not from claiming
that the 24 columns exhaust the row module.
