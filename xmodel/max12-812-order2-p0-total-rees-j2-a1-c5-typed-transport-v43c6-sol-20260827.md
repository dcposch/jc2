# V43C6: fail-closed typed transport audit for the C5 certificate

Date: 2026-08-27

## Verdict

**`PASS-C5-TYPED-TRANSPORT-AUDIT-OBSTRUCTION`.  No transport certificate.**

The reviewed C5 identity

```text
a1^628 = sum_(j=1)^25 M_j(t,X) Tg_j(t,X)
```

is exact in the ordinary ring `Q[t,X19_total]`, but it does not presently
transport to either receiver checked here:

1. V20R2 contains no serialized literal C5 ring map or 25-row module map, so
   normalized K00 is skipped rather than wired by aliases.
2. For the smallest reviewed V47 terminal grade, the lexicographically first
   contact with the smallest leading charged grade is
   `A1D2_R3=(a,d,c,r_min;G,T_C2)=(1,2,3,3;14,16)`.  Its exact forward V46
   contact map sends the C5 stage-zero source generator

   ```text
   a1 = Az_0  |->  0,
   ```

   because `a=1` and the lower contact ideal kills all `Az_i` with `i<a`.
   Zero is not a unit in the nonzero localized target domain.  Thus the map
   cannot extend from `S` to `S[a1^-1]`, and the C5 target maps only to
   `0^628=0`.  The transported certificate is tautological and supplies no
   target unit.

This is the first obstruction, before any 25-row expansion.  It uses one
source generator and is strictly smaller than a missing-row witness.

## Frozen source

The source is

```text
S = Q[t,X19_total],          t |-> rho^2,
|X19_total| = 66,            source localization = none.
```

The sole general-only positive variable is `ez9`.  The complete 67-generator
alphabet, all 25 supported row names, and the exact SHA-256 of each row are in
`RESULT.json`.  The supported rows are

```text
Tg11_1,Tg11_2,Tg11_7,
Tg12_1,Tg12_2,Tg12_7,
Tg13_1,Tg13_2,Tg13_4,Tg13_5,Tg13_7,
Tg14_1,Tg14_2,Tg14_3,Tg14_4,Tg14_5,Tg14_7,
Tg15_3,Tg15_5,Tg15_7,
Tg16_5,Tg16_6,Tg17_5,Tg18_6,Tg19_7.
```

The charged C5 hostile review is SHA-256
`0ab2a7ef8a2efc4a1aa911b0857b88a6e7fb137e02c1c87b5c40640cfa4e04ce`.
It confirms the exact ordinary-ring identity and explicitly withholds a
terminal/common-source chain map.

## Search gate 1: normalized common K00 V20R2

The frozen V20R2 object has:

```text
169 labelled source columns, 164 free after five fixed-zero boundaries;
140 equations (Phi_i,Lambda^n), i=1..7, n=0..19;
target symbol Jdet;
normalized coordinates C0..C6 with C6=1;
unit opens k10_0 and Jdet_0.
```

Its authoritative `SOURCE_COLUMNS.json`, literal 140-equation DAG, and result
contain no source generator `a1`, no `Tg` row label, no `C5 -> V20R2` ring
map, no image of `a1`, and no 25-row module matrix.  V19 is retained only as
a historical type control: its three earlier quotient duals were all
`NOT_TYPED_COMPOSABLE` before V20R2 constructed the common source.

Therefore the exact V20R2 outcome here is

```text
SKIPPED_NO_LITERAL_C5_RING_OR_ROW_MODULE_MAP.
```

This is an availability/interface statement, not a theorem that no future
map can be constructed.  In particular, shared names and normalized-coordinate
formulas are not consumed as aliases.

## Search gate 2: the reviewed `A1D2_R3` endpoint

### Target rings and localizers

The exact finite V47R1 manifest ring is the polynomial ring over `Q` in the
following 24 symbols:

```text
rho, P_1,P_2,
AzD1_0..AzD1_2, AcD1_0..AcD1_2,
CzD1_0..CzD1_2, CcD1_0..CcD1_2,
BzD1_0,BcD1_0,
k10_0,k6_0,k2_0, mu2,mu4,mu6,J.
```

Its support maxima are

```text
p=2, A=2, C=2, R=0, k10=0, k6=0, k2=0.
```

The inherited endpoint localization is `D(p*k0)`.  In the V47 coefficient
ring `p=P_0=-2*rho^2` and `k0=k10_0`, hence its displayed localizer is

```text
p*k0 = (-2*rho^2)*k10_0.
```

V46R1's root-coordinate interface is separately on `D(rho)`.  These are
nonzero elements of a polynomial domain; their localizations remain nonzero
domains.

For a truncation-independent control, the audit also constructs a complete
63-generator polynomial extension retaining the image of every C5 variable.
The endpoint equations remain in the finite subring.  This generous extension
does not repair the target image: `a1` still maps to zero.

### Literal forward map

The map direction is exactly the frozen V46 direction

```text
total coefficient ring -> shifted D1 coefficient ring.
```

At `(a,c,r)=(1,3,3)`, write `n>=0`.  The complete extension map is

```text
t                         -> rho^2
ell_i                     -> P_i/2
az_(1+n), ac_(1+n)        -> AzD1_n, AcD1_n
ez_(3+n), ec_(3+n)        -> 2*CzD1_n, 2*CcD1_n
cs_(3+n), rs_(3+n)        -> BzD1_n, 4*BcD1_n
k,k1,k2c,k10_i            -> k10_0,k10_1,k10_2,k10_i
k6,k6_1                   -> k6_0,k6_1.
```

Every coefficient below its displayed contact order maps to zero.  In
particular,

```text
a1=Az_0 -> 0,
e1=Ez_1 -> 0, ee1=Ez_2 -> 0,
e0=Ec_1 -> 0, ee0=Ec_2 -> 0,
cs1,cs2,rs1,rs2 -> 0.
```

The factor `P_i/2` is forced by V46's normative
`P=p0+2*sum ell_i sigma^i`.  The `k2c` image is the total `k10` jet
`k10_2`, never the distinct D1 leading `k2load` name.

All 67 images are serialized in `RESULT.json`.  Restricting to the finite
V47R1 manifest leaves 28 defined images and 39 explicitly `MISSING` images.
No missing high jet is silently set to zero.

### Why the certificate cannot close this endpoint

Let `T` be either the finite target ring or the complete polynomial extension,
localized by the registered nonzero endpoint factors.  Both are nonzero
domains.  The exact map has

```text
phi(a1)=0,                 phi(a1^628)=0.
```

Hence `phi(a1)` is not in `T^x`.  By the universal property of localization,
there is no extension `S[a1^-1] -> T`.  Applying `phi` to the C5 identity can
at best produce

```text
0 = sum_j phi(M_j) phi(Tg_j),
```

which is not a Bezout/unit certificate in the endpoint receiver.

The V47R1 endpoint exposes exactly three charged literal slots,
`Phi1[14]`, `Phi2[14]`, and `Phi4[16]`.  They are not a serialized
25-row module map.  Because the unit-image gate already fails, the row-module
stage is correctly recorded as `NOT_REACHED_AFTER_NONUNIT_A1_IMAGE` rather
than assigning unmapped rows the value zero.

## Controls

The replay rejects all registered shortcuts:

- V20 normalized-coordinate aliases are not a C5 map;
- the forbidden stage-zero substitution `a1 -> AzD1_0` conflicts with the
  exact V46 lower ideal;
- zero is not a unit and the target is not silently replaced by the zero ring;
- a map with `a1 -> 0` cannot extend over `D(a1)`;
- `az4` and every other unretained finite-manifest jet remain `MISSING`, not
  zero;
- three V47 coefficient slots are not treated as a 25-row module map; and
- the V46 transport is never reversed.

The replay uses hashes, JSON schemas, finite maps, and exact domain arithmetic
only.  Runtime is below one second, with no CAS, heavy local algebra, or AWS
job.

## Scope firewall

This report does not refute C5, V20R2, V46/V47, or their reviewed theorems.
It isolates why this particular certificate cannot be consumed by the named
receiver interfaces.  It does not claim that no different source invariant,
different chart certificate, or newly constructed K00 chain map can work.
It supplies no C5 row image, contact cover, endpoint replacement, `G2-PSC`,
Gate T, order-two, maximum-twelve, JC2, or counterexample conclusion.

## Evidence

```text
967864722b7302f3f65de29503786e5827a073930f9faf6780bfa858df9fb911
  cases/max12_812_order2_p0_total_rees_j2_a1_c5_typed_transport_v43c6_20260827/PREREGISTRATION.md

dc0c61a16420c5c763f89f13f1954f158d7f85f02460c76257048ff981462523
  cases/max12_812_order2_p0_total_rees_j2_a1_c5_typed_transport_v43c6_20260827/audit_c5_typed_transport_v43c6.py

30b4ec0b30013a9061a0d6c8587096ffde9af26ced4025562eb4f4b4f71911ff
  cases/max12_812_order2_p0_total_rees_j2_a1_c5_typed_transport_v43c6_20260827/RESULT.json
```
