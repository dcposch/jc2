# V43C6 preregistration: typed transport of the C5 certificate

Date: 2026-08-27

## Question and fixed search order

Audit whether the reviewed C5 identity

```text
a1^628 = sum_(R in C5_25) M_R R
```

in the ordinary ring `S=Q[t,X19_total]`, with `t -> rho^2`, transports to
an already reviewed terminal/common-source receiver by a literal typed chain
map.  The fixed search order is:

1. normalized common K00 V20R2, but only if its frozen artifacts contain a
   serialized ring map and row-module map from the C5 source; otherwise record
   the missing interface and do not construct one from aliases; then
2. the smallest-terminal-grade reviewed V47+V47R1 endpoint,
   `A1D2_R3=(a,d,c,r_min;G,T_C2)=(1,2,3,3;14,16)`.

This audit is endpoint-specific.  It is not a coverage, `G2-PSC`, Gate T,
order-two, maximum-twelve, or JC2 result.

## Frozen source object

The source ring is

```text
S = Q[t,
  a1,aa0,aa1,aaa0,aaa1,ac3..ac8,az3..az8,
  cs1..cs7,rs1..rs7,
  e0,e1,ee0,ee1,ec3..ec9,ez3..ez9,
  ell1..ell8,
  k,k1,k2c,k10_3..k10_6,k6,k6_1].
```

There are 66 positive-weight `X19_total` symbols plus `t`.  `ez9` is the sole
general-only positive symbol.  The 25 supported rows and their exact hashes
must be read from the frozen C5 proof; no row may be selected by name alone.

## Required map data and fail-closed gates

For a positive result the evidence must serialize and check all of:

1. source and target coefficient rings;
2. the image of `t` and every one of the 66 positive source variables;
3. every source and target localization, and extension of the ring map across
   each inverted source element by the universal property of localization;
4. the image of `a1`, which must be a unit in the target ambient localized
   ring, not merely zero in a quotient or radical;
5. all 25 C5 row hashes and an exact 25-row-to-target-row module matrix;
6. exact replay of each row image and of the transported Bezout identity.

Stop at the first failed gate.  `MISSING` is a typed result, never an implicit
zero.  A prose alias, a shared spelling, or a coefficient digest is not a ring
or row-module map.

For `A1D2_R3`, independently derive the finite manifest ring from the frozen
V47R1 maxima and the contact map from the frozen V46/V46R1 schemas.  Also
serialize the generous complete polynomial extension of that map, so that a
finite-jet omission cannot hide the image of `a1`.  The lower-ideal rule is
charged before any row computation.

## Registered obstruction verdict

Return

```text
PASS-C5-TYPED-TRANSPORT-CHAIN-MAP
```

only for a complete exact map with unit image of `a1` and all row replays.
Otherwise return

```text
PASS-C5-TYPED-TRANSPORT-AUDIT-OBSTRUCTION
```

with the earliest exact obstruction, its map stage, and all later stages marked
`NOT_REACHED`.  This is a successful audit, not a successful transport.

## Mandatory negative controls

The audit must reject:

- treating the V20R2 normalized coordinate names or source columns as a C5
  map;
- replacing the V46 lower-ideal image `a1 -> 0` at positive `a` by the shifted
  leading alias `a1 -> AzD1_0`;
- declaring zero a unit or silently replacing the target by the zero ring;
- extending `S[a1^-1]` across a map with nonunit image of `a1`;
- treating an unretained finite-manifest jet as zero rather than `MISSING`;
- treating V47R1's three coefficient slots as a 25-row module map; and
- reversing the V46 transport direction.

No heavy algebra is authorized locally.  The expected audit is hash, schema,
finite-map, and exact-domain arithmetic only.
