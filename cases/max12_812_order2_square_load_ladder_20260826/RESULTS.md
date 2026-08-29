# Generic-square load-unit ladder: exact grades four and five

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER ENDPOINT; EXACT-Q PASS; NO SQUARE-BRANCH OR
ORDER-TWO VERDICT.**

## 1. Endpoints

Both independently compiled lanes passed every frozen-source,
divisibility, quotient-identity, forbidden-variable, localization, and
per-generator radical-containment sentinel:

| field | host | tag | engine | peak RSS | verdict |
|---|---|---|---:|---:|---|
| `Q` | Box03 | `max12_812_order2_square_load_ladder_q_20260826T070340Z_box03` | Singular | 14,416 KiB | PASS |
| `F_65521` | r6d | `max12_812_order2_square_load_ladder_p65521_20260826T070340Z_r6d` | Singular | 14,404 KiB | PASS |

Both completed in 0.04 seconds with zero swap.  The exact-Q stdout has SHA
`8876a2b17c9de90c10eab98f08b846a063074d181b6f232ed3e3fcc6e4385d14`;
the independent finite-field stdout has SHA
`5ea6af6c6013518b03ace5feb21cc5b80207461c53fa1c4c30bacc42923a3173`.

## 2. Fourth grade

After the preceding generic-square reduced gate `u2=u3=0`, the complete
seven loaded source rows are exactly divisible by `Lambda^4`.  Their divided
grade is independent of every finite load and target.  Over `Q` the seven
canonical rows are

```text
0,
(3/32)*v1^2,
(3/16)*v0*v1,
-(3/64)*p*v1^2+(3/32)*v0^2,
-(3/64)*p*v0*v1,
0,
-(3/512)*p^2*v0*v1.
```

On `D(p*k10)` their exact raw standard basis is

```text
v1^2,
v0*v1,
v0^2,
```

and their radical is exactly `(v0,v1)`.  This is the source-row realization,
up to the charged invertible triangular tail convention, of the analytic
receiver `[(3/8)S^2/L^2]_-`.  The quadratic scheme thickness is retained.

## 3. Fifth grade

After additionally imposing `v0=v1=0`, all seven complete source rows are
exactly divisible by `Lambda^5`.  Their divided grade contains `k10` but no
`k6`, `k2`, or target load.  On `D(p*k10)` the exact raw standard basis is

```text
cs*rs^3,
cs^3*rs,
24*p*cs^2*rs-rs^3,
8*p*cs^3-3*cs*rs^2,
rs^5,
cs^5.
```

Its radical is exactly `(cs,rs)`.  This is the complete source-row
realization of the analytic receiver `[(5/16)k10 R^3/L]_-`.

## 4. Exact consequence and scope

On the generic square open `p!=0`, the prior reduced next-tail condition
forces `M=0`.  First-contact saturation then licenses `k10!=0`.  In the
registered zero-higher-correction slice, the next two complete source grades
force, on reduced support,

```text
S=0, then R=0.
```

Thus the apparent generic square family is not free in those two registered
successive transverse directions: that slice is driven back to the
higher-contact fourth-power section.  This is an exact characteristic-zero
statement at the frozen two grades, independently reproduced at a good
prime.

It is not a correction-aware Kuranishi calculation and not an exclusion of
the generic square branch.  For example, replacing the already-zero `M` and
`S` coordinates by higher-order corrections can create cross terms at the
same fifth grade as the displayed `k10*R^3/L` term.  Those weighted
resonances, the `k6` and `k2` ties, and the target grades `13,...,19` have not
been enumerated.  The degenerate core `p=0`, square/discriminant
intersection, terminal row, and both Taylor receivers are also outside this
endpoint.  No strict-arc, order-two, `(8,12)`, maximum-twelve, or JC2 verdict
follows.
