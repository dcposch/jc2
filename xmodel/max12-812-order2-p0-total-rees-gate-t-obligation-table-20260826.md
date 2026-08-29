# `(8,12)` order two: proof-carrying total-Rees Gate T obligation table

Date: 2026-08-26

Status: **COORDINATOR DESIGN AND EXACT CHART-PRESENTATION LEMMA.  NO TOTAL
REES, MOVING-`p`, ORDER-TWO, MAXIMUM-TWELVE, OR JC2 VERDICT.**

## 1. Purpose and charged inputs

This note instantiates the landing priority from the 17:40Z ideation round
on the smallest nearly assembled source cover: the post-`M=0`, unit-`k10`
collision family over

```text
p=-2*rho^2,
J1=(rs,cs,c0,c1),
J2=(a0,a1) on V(J1).
```

The abstract DVR coverage theorem and current source design are

```text
6995a991b1e7803a26bbf5374b10d54a0cda7d17158ad9f1595db76218aadb92
  xmodel/cross-iterated-blowup-cech-valuative-propagation-20260826.md

22d32f1840f47da09660fd8f6b37966562b6532e8bad12544953a7cbb6185c85
  xmodel/cross-empty-special-fibre-valuative-propagation-20260826.md

99e45e341925ceb9a01843b4dd36ab99218f97055449c203e792e91e38244434
  xmodel/max12-812-order2-p0-cech-lowcontact-pell-total-rees-successor-design-20260826.md
```

The third file remains the detailed source specification.  This note
deduplicates its obligations, updates stale endpoint statuses, and records a
chartwise construction that avoids computing one monolithic Rees kernel.

## 2. Exact affine-chart presentation

Let `A` be a noetherian ring and `I=(f0,...,fn)`.  On the standard blowup
chart `D_+(fi*T)`, the coordinate ring is

```text
C_i=(Rees_A(I)[1/(fi*T)])_0
   =A[f0/fi,...,fn/fi] inside A[1/fi].              (2.1)
```

Introduce ratio variables `yj`, `j!=i`.  If

```text
P_i=(fi*yj-fj : j!=i) in A[yj],                    (2.2)
```

then an exact presentation, including all zero-divisor torsion, is

```text
C_i = A[yj]/(P_i:fi^infinity).                      (2.3)
```

Equivalently, the kernel in (2.3) is obtained without guessing a saturation
exponent by eliminating `u` from

```text
P_i+(1-u*fi).                                      (2.4)
```

Indeed, localizing (2.2) at `fi` identifies every `yj` with `fj/fi`; the
kernel before localization is exactly the `fi`-torsion.  Formula (2.3) is
therefore the actual Rees chart, not the possibly larger symmetric-algebra
chart.  It remains valid if `fi` is a zero divisor; if localization kills
the ring, the saturation is the unit ideal.

For Gate T, apply (2.3) separately to the four `J1` charts.  On the closed
receiver `A/J1`, apply it to the two `J2` charts.  Thus six independent
elimination jobs replace a global Rees presentation.  Standard blowup charts
cover by construction; ordered endpoint proofs use their exact overlaps.

### Special-fibre comparison

For each chart compute two ideals in the same named ratio coordinates:

```text
K_i^tot +(rho),
K_i^0,                                             (2.5)
```

where `K_i^tot` is (2.3) over the unspecialized total source and `K_i^0` is
formed after the literal `rho=0` source specialization.  Gate T requires
scheme-theoretic equality in (2.5), or an explicit kernel/cokernel and a new
receiver.  Equality of radicals is insufficient.  This is the precise test
for the base-change/torsion issue which the specialized units do not settle.

## 3. Finite-prefix acceleration

Let `A_g` be the total source quotient by every raw coefficient equation
through grade `g`, and let `A_full` add the later equations.  The map

```text
A_g[I/fi] -> A_full[I* A_full/fi]                   (3.1)
```

is surjective.  Hence a localized identity making `rho` a unit in a chart of
`A_g` remains a unit after every later source equation is imposed.  A chart
may therefore be certified from its first decisive grade, provided that:

1. the source emitter is the common bivariate `(sigma,rho)` emitter;
2. every term capable of contributing through that grade is retained;
3. the Rees ideal and ratio names are the restrictions of the common total
   chart; and
4. the emitted certificate has the exact form

   ```text
   s=sum H_i*Phi_i+rho*H,
   ```

   with only registered chart units in `s` and all denominators.

This removes the need to build every six-chart job through grade 38.  The
required prefixes are grade 10 for the two trivial `C` opens, grade 12 for
the cusp, grade 14 for the odd sheet, and at most grade 15 for each currently
named low/high-contact `A` shard.  Only the terminal exact-square/all-load
receiver presently needs the later target window through grade 38.

## 4. Special-fibre obligation matrix

The table separates a reviewed endpoint from the still-missing assertion
that it is the base change of the same total Rees chart.

| ordered special-fibre stratum | first endpoint | endpoint status | Gate-T map |
|---|---|---|---|
| `D_+(rs)` | raw grade-12 cusp identity and unit on `D(k10*rs)` | **CONFIRMED**, review SHA `aaf20f09...` | **MISSING** |
| `V(rs) intersect D_+(cs)` | raw grade-14 odd-sheet unit on `D(k10*cs)` | **PROMOTED**, SHA `f48401b5...` | **MISSING** |
| `V(rs,cs) intersect D_+(c0)` | grade-10 `(3/32)c0^2` | elementary raw unit | **MISSING** |
| `V(rs,cs,c0) intersect D_+(c1)` | grade-10 `(3/32)c1^2` | elementary raw unit | **MISSING** |
| `V(J1) intersect D_+(a0)` | contact-one raise; high-contact grade-15 cube | promoted only at the named contact-one/high-contact scopes, SHAs `f630f3c1...`, `4aeee798...` | **MISSING; finite secondary fan open** |
| `V(J1,a0) intersect D_+(a1)` | tangent contact-one raise; high-contact triangular/cube unit | promoted only at the same named scopes | **MISSING; finite secondary fan open** |

The residual `A` debt is exactly the seven source shards

```text
(c,r)=(2,>=3),(2,2),(3,>=3),(3,2),
r=1 with c=2, c=3, or c>=4.                         (4.1)
```

Every tangent shard must retain the dichotomy `ROUTE_CONSTANT_A` versus
`STAY_TANGENT`; a chart obtained by setting all later constant `A`
coefficients to zero is not a cover.

If both `J1` and `J2` vanish, the arc routes to the named exact-square/all-
load receiver.  Its reduced seven-tail support is reviewed as square plus
Chebyshev/Pell (review SHA `eff19a41...`), but the affine-target row, later
corrections, terminal `[6,2]`, and both Taylor pullbacks remain open.  It is
not removed by projectivization.

## 5. First executable chart: `T-rs`

The smallest total-source discriminator is the `D_+(rs)` chart.

1. Extend the frozen complete cusp emitter to the bivariate substitution
   `p=-2*rho^2`, with `rho` independent of `sigma`, and collect every source
   coefficient through grade 12.
2. Construct the actual chart by (2.3), not by the three bilinear equations
   alone.  Emit both the saturation presentation and the auxiliary-variable
   elimination proof (2.4).
3. Compute (2.5) exactly.  On equality, print the two-sided name map to the
   frozen raw cusp algebra.  On failure, freeze the first torsion/base-change
   discrepancy as the landing obstruction.
4. Lift the confirmed special-fibre identity

   ```text
   32768*g12_6-35*k10*rs^4
     =-4096*rs*g10_2-8192*cs*g10_3
   ```

   to a total identity with an explicit `rho*H` remainder.  Since
   `p=-2*rho^2`, every newly introduced coefficient must in fact be divisible
   by `rho^2`; this stronger divisibility is a sentinel, not an assumption.
5. Require the negative control omitting `g10_3` to leave the known nonzero
   nilpotent residue.  Compare the actual chart with the naive symmetric
   presentation: if they differ, print the torsion witness; if they agree,
   certify equality rather than requiring an artificial failure.
6. Run exact Q on one AWS host and an independently compiled good-prime
   control on another.  No Singular or exact-Python algebra runs locally.

A PASS proves Gate T only for `T-rs`.  It provisionally permits successor
work on the next chart while hostile review runs, but five other maps, the
seven `A` shards, the terminal receiver, and the `D(rho)` generic-square
overlap remain mandatory.

## 6. Overlap and propagation rule

On a later standard chart, a nonzero earlier homogeneous ratio lies in an
already tested overlap.  The ordered closed complement sets that ratio to
zero and reaches the next specialized endpoint.  Each such step must print
the exact restriction map; set-theoretic partition language is not enough.
After all six standard charts and the terminal receiver are empty in the
same total family, the blowup universal property covers every DVR arc, and
the explicit chart identities make `rho` a unit.  No arc with
`ord(rho)>0` remains.  After a finite ramified extension this covers rational
valuations, and `p=-2rho^2` converts the conclusion to the named moving-`p`
chart.

## 7. Firewall

The chart-presentation and finite-prefix statements are elementary algebra;
the matrix is an obligation ledger.  No current artifact verifies even the
first total base-change map.  Nothing here covers `k10=0`, another load ray,
another square-normal cone, the full order-two source, maximum twelve, the
global Sigray landing obligations, a cofinal complexity bound, or JC2.
