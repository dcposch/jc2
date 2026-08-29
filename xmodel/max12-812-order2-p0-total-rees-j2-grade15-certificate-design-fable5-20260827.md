# Independent J2 grade-15 certificate design (Fable 5)

Date: 2026-08-27

Lane: speculative, reversible child of V22R1.  Sole write of this lane.
Author: Fable 5, equal blind co-researcher.

Status: **T-a0 CLOSED BY TWO EXACT DESK CERTIFICATES (DIFFERENT-MODEL REVIEW
REQUIRED); T-a1 TYPED CERTIFICATES REFUTED IN ALL DESK-REACHABLE SHAPES, ONE
EXACT OBSTRUCTION PROVEN BY HAND; DECISIVE T-a1 QUESTION SPECIFIED FOR AWS.**

## 0. Inputs, custody, erratum compliance

All hashes below observed by me with `shasum -a 256` on 2026-08-27.

- `FREEZE_R1.sha256` of
  `cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827/`
  verifies OK from the repo root (5/5 files, including the pinned V1
  implementation `census_j2_typed_v23.py` at
  `14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501`).
- `output_r1/RESULT.json` observed at
  `ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641`.
  I reran the frozen `census_j2_typed_v23r1.py` to a scratch directory:
  the entire output tree, including `RESULT.json`, is **byte-identical**
  (0.4 s).  V1 erratum respected: the quarantined `output/` was not
  consumed by any check below; only `output_r1/` is used.
- Upstream manifests re-verified: V9 `COEFFICIENTS.json`
  `86c535a3…63c0e`, V20 `RESULT.json` `b23ffacd…e68d`, V22R1 (`aws_q_r1`)
  `RESULT.json` `829239c9…cf00b8`; all 42 per-coefficient file hashes
  re-checked against these manifests by my own script.
- Provenance state observed: V9 and V20 promoted; V22R1 hostile review
  (Grok) has landed with verdict **CONFIRMED WITH REPAIRS**, and its repair
  list states no coefficient, term count, section residual, or historical
  identity changes.  The grade-15 bytes I use are therefore review-confirmed.

## 1. Independent verification of the V23R1 census

I re-implemented the entire specialization pipeline from scratch (own
scanner-based parser, no Python `ast`; own sigma-weight table re-derived
from the V20 emitter formulas; own substitution code) and ran it on the 42
raw hash-gated coefficient files:

- all 42 rows sigma-homogeneous at their grades and rho-even;
- V22R1 grade-15 term counts reproduced: 133, 224, 355, 140, 585, 200, 759;
- all 84 specialized chart rows (`J1=(rs,cs,c0,c1)` killed; `a1=a0*qa1`
  for `T-a0`; `a0` killed for ordered `T-a1`) **match the frozen
  `output_r1` bytes** as polynomials, 84/84;
- the pure exceptional census is reproduced exactly, including the full
  a0-chart cubic vector of the assignment prompt (all five rows verified
  from literal bytes, not trusted):

```text
Tg15_3|a0: -(1/16) a0^3 qa1^3
Tg15_4|a0: -(3/16) a0^3 qa1^2
Tg15_5|a0: -(3/16) a0^3 qa1 - (3/32) a0^3 qa1^3 rho^2
Tg15_6|a0: -(1/16) a0^3 - (3/16) a0^3 qa1^2 rho^2
Tg15_7|a0: -(3/32) a0^3 qa1 rho^2 - (3/128) a0^3 qa1^3 rho^4
Tg15_3|a1: -(1/16) a1^3;  Tg15_5|a1: -(3/32) a1^3 rho^2;  Tg15_7|a1: -(3/128) a1^3 rho^4
```

- specializing my parsed rows at `qa1=0, a0=1` reproduces the A00 values I
  independently confirmed in my V21 hostile review; the A10 tie-in is the
  a1-ordered pure triple above.

The grade-10 negative control (all 14 chart rows zero) holds in my
pipeline as well.

## 2. T-a0: two exact certificates; the chart is empty

Both identities below are polynomial identities in
`Q[a0,qa1,rho,jets]` among the frozen specialized rows
(`output_r1/a0_chart/*.poly`), verified by direct exact-`Fraction`
expansion with residual identically zero, through two independent parses
(my raw-input re-specialization and the frozen census bytes).

### 2a. Human-checkable typed certificate (six rows)

```text
a0^3 * (1 + 3 qa1^2 rho^2) =
    -16 * Tg15_6
    - 2 rs1        * Tg12_2
    - 2 rs2        * Tg11_2
    - 4 cs1        * Tg12_3
    - 6 rho^2 cs1  * Tg12_1
    + (6 cs1 ell1 - 8 rho^2 cs2) * Tg11_1        (A0-CERT-U)
```

Sigma-weight 15 in every summand.  Derivation is fully hand-reconstructible
from the literal bytes: the grade-11 rows on this chart are
`Tg11_1=(3/8)a0(e0 qa1+e1)` and `Tg11_2=(3/8)a0(e0+e1 qa1 rho^2)` (rows
3/5/7 are rho-multiples of row 1), the grade-12 rows supply the
`ee`/`aa`/`e^2` blocks, and the 19-term `Tg15_6` decomposes exactly into
`-(1/16)a0^3(1+3qa1^2 rho^2)` plus six group multiples of those rows
(the `rs1` block of `Tg15_6` is exactly `-(rs1/8)*Tg12_2`, the `rho^2 cs1`
block exactly `-(rho^2 cs1/2)*Tg12_1`, etc.).

Typing per the promoted staged calculus: exceptional power `a0^3`
(absorbed by kernel-as-saturation), genuine localizer `s = 1` (no residual
stratum), unit `1 + rho*W` with `W = 3 qa1^2 rho`, ordered generators only
`J1` itself (stage-two base), no inversion of `rho`, jets, or exceptional
coordinates.  Rows used: V9 grade-11/12 (promoted) and V22R1 `Tg15_6`
(confirmed with repairs).

### 2b. Pure-power certificate: `a0^3` itself is in the row ideal

Stronger and localizer-free *and* unit-free:

```text
a0^3 = sum over 13 rows of (cofactor) * (row), with exactly these cofactors:

Tg11_1: 6*cs1*ell1 + (9/4)*cs1*ell1*qa1^2*rho^2 - 3*cs2*qa1^2*rho^4
        - 8*cs2*rho^2 + (27/2)*ell1*ell3*qa1*rho^2 + (27/4)*ell2^2*qa1*rho^2
        - 9*ell4*qa1*rho^4 + (27/8)*qa1*rho^2*rs2
Tg11_2: 9*cs2*qa1*rho^2 - (3/4)*qa1^2*rho^2*rs2 - 2*rs2
Tg12_1: -(9/4)*cs1*qa1^2*rho^4 - 6*cs1*rho^2 + (27/2)*ell1*ell2*qa1*rho^2
        - (27/2)*ell3*qa1*rho^4 + (27/8)*qa1*rho^2*rs1
Tg12_2: 9*cs1*qa1*rho^2 - (3/4)*qa1^2*rho^2*rs1 - 2*rs1
Tg12_3: -4*cs1 - (3/2)*cs1*qa1^2*rho^2 + 9*ell3*qa1*rho^2
Tg13_1: (27/4)*ell1^2*qa1*rho^2 - (27/2)*ell2*qa1*rho^4
Tg13_3: 9*ell2*qa1*rho^2
Tg14_1: -(27/2)*ell1*qa1*rho^4
Tg14_3: 9*ell1*qa1*rho^2
Tg15_1: (27/4)*qa1*rho^6
Tg15_3: -9*qa1*rho^4
Tg15_5: 18*qa1*rho^2
Tg15_6: -16 - 6*qa1^2*rho^2                       (A0-CERT-P, 32 entries)
```

Residual verified identically zero over `Q`.  Row provenance: V9
(11_1,11_2,12_1,12_2,12_3), V20 (13_1,13_3,14_1,14_3), V22R1
(15_1,15_3,15_5,15_6).  Chart-row byte pins (`output_sha256` in
`RESULT.json ce4d0adb…`): Tg11_1 `ddfff315…`, Tg11_2 `70cf6c47…`,
Tg12_1 `8c827abf…`, Tg12_2 `b28d2dea…`, Tg12_3 `9106a962…`, Tg13_1
`125cfe9d…`, Tg13_3 `0672ce27…`, Tg14_1 `1a7e3346…`, Tg14_3 `86187535…`,
Tg15_1 `c1919647…`, Tg15_3 `dd5138e0…`, Tg15_5 `a272b7c8…`, Tg15_6
`c3bb2b11…`.

### 2c. Consequences, minimality, and lifting

- Because `A0-CERT-P` has no unit and no localizer,
  `(I_a0 : a0^infinity) = (1)` for the truncated row ideal `I_a0`
  (all 28 nonzero specialized rows, grades 11-15).  Two independent local
  Singular runs concur (`sat(I,a0)` returns the unit ideal), but the
  load-bearing verification is my exact `Fraction` replay of the printed
  identity, not Singular.
- Hence the presented `T-a0` chart ring
  `(A/J1)[qa1] / ((a0*qa1 - a1) : a0^infinity)` of the **truncated**
  exported source model is the zero ring: the whole chart is empty, not
  merely its `rho=0` fibre.  Adding further true source relations
  (grade >= 16) only enlarges the ideal, so emptiness persists for the
  full registered actual-total source, conditional only on the recorded
  provenance chain (V9/V20 promoted, V22R1 confirmed) and the promoted
  chart-presentation theorem.
- Lifting to the promoted certificate form (2): each specialized row
  differs from its literal total-source row by a `J1`-combination plus a
  multiple of the chart bilinear `a0*qa1 - a1`; collecting those
  cofactors turns either identity into
  `a0^3 * s * (1 + rho*W) = sum H*(a0*qa1 - a1) + sum G*q_m + sum L*z_e`
  with `z_e` running over `rs,cs,c0,c1` — honest stage-one exceptional
  coordinates of the staged `J1/J2` tree.  Conversely any form-(2)
  certificate specializes back under `(J1, a1 - a0*qa1) -> 0`, so working
  with the specialized rows is lossless.
- Minimality/necessity (all proven from the verified census, not assumed):
  `N = 3` is the least possible pure exceptional power at any localizer of
  sigma-weight < 1 (weights: `a0^N` has weight `5N`; nonzero rows start at
  grade 11); every certificate must use grade-15 rows (grades 11-14 have
  no pure exceptional terms on either chart); and the anchor is forced:
  the only source of the `qa1^0 rho^0` monomial `a0^3` is `Tg15_6`, whose
  cofactor constant term must be exactly `-16`.

## 3. Ordered T-a1: exact refutations and one hand-proven obstruction

Let `I_a1` be the ideal of the 31 nonzero `a1_ordered` rows (grades
11-15) in `Q[a1,rho,jets]`.  Since all rows are sigma-homogeneous, a typed
certificate `a1^N k^M (1 + rho*W) ∈ I_a1` forces its weight-`(5N+4M)`
graded part `a1^N k^M (1 + rho*W0)`, `W0 ∈ Q[rho]`, to be an identity on
its own; and the retraction `a0 -> 0, qa0 -> 0` shows form-(2) terms
(bilinear, `z_e = a0`) cannot rescue it.  My exact sparse linear solves
over the complete homogeneous cofactor spaces give:

| target | weight | field | result |
|---|---|---|---|
| `a1^3 (1+rho W)` | 15 | exact `Q` | **INFEASIBLE** (rho-cap 10 and 20; 644 and 1176 columns) |
| `a1^3 k (1+rho W)` | 19 | exact `Q` | **INFEASIBLE** (8 501 columns; rho-cap 12 and 16) |
| `a1^4 (1+rho W)` | 20 | exact `Q` | **INFEASIBLE** (14 738 columns) |
| `a1^3 k^2 (1+rho W)` | 23 | mod `2^31-1` | INFEASIBLE (68 750 columns) |
| `a1^4 k (1+rho W)` | 24 | mod `2^31-1` | INFEASIBLE (111 226 columns) |

(The same solver, run on the a0 chart, finds `A0-CERT-P` feasible — a
positive control that the infeasibilities are not a solver artifact.)

**Hand-checkable obstruction for the primary shape** `(N,M)=(3,0)`:

1. Anchor forcing.  The only rho-free row monomial dividing `a1^3` in any
   of the 31 rows is `-(1/16)a1^3` in `Tg15_3` (weights 5 and 10 admit no
   rows; the pure census has no other candidates).  So in the `rho^0` layer
   the `Tg15_3` cofactor has constant term exactly `-16`.
2. Uncancellable monomial.  `Tg15_3` also contains `-(5/512) a1 k rs1^2`
   (literal byte, pin `3c11307c…`).  A machine scan over all 31 rows shows
   the **only** rho-free row monomial dividing `a1*k*rs1^2` is that very
   term (no grade-12 row contains `k`; grade-10 rows vanish; weight
   arithmetic excludes everything else).  Hence the identity's right side
   contains `(5/32) a1 k rs1^2` at `rho^0`, which the left side
   `a1^3(1+rho W)` cannot contain.  Contradiction.

Geometric counterpart: on the closed family `rho=0`, all vars 0 except
`(a1, rs1, k)`, exactly two rows survive, `Tg13_2 -> -(3/32)a1^2 rs1 +
(5/1024)k rs1^3` and `Tg15_3 -> -(5/512)a1 k rs1^2 - (1/16)a1^3`, and
they force `k rs1^2 = (96/5)a1^2` and `k rs1^2 = -(32/5)a1^2`
simultaneously — no witness point with `a1 != 0` exists on this family.
The exported grade-13 row actively closes the `k rs1^2` escape; I found
no obstruction witness point, and the bounded certificate shapes all fail.
The truncated `T-a1` question is genuinely open and is exactly the AWS
job below.

What is *not* refuted: unbounded `(N,M)` beyond the table, and
certificates using grade >= 16 rows once exported.

## 4. Hash-ready AWS experiment specification (proposed V24)

Proposed case: `max12_812_order2_p0_total_rees_j2_a1_sat_v24_2026xxxx`.
This lane launches nothing; the spec is ready to freeze.

- **Decision identity** (proved in section 3 preamble + the equivalence
  below, both directions elementary):
  a typed certificate `a1^N k^M (1+rho*W) ∈ I_a1` exists for some
  `N, M, W`  **iff**  `1 ∈ ((I_a1 : a1^infinity) : k^infinity) + (rho)`.
  (Forward: reduce mod `rho`.  Back: `1 - rho*w ∈ Isat` un-saturates to
  the typed identity with `W = -w`.)
- **Ring**: characteristic-0 lane and `F_65521` control lane, `dp` order,
  the 32 variables
  `a1, rho, aa0, aa1, aaa0, aaa1, ac3, ac4, az3, az4, cs1, cs2, cs3, e0,
  e1, ec3, ec4, ec5, ee0, ee1, ell1, ell2, ell3, ell4, ez3, ez4, k, k1,
  k2c, rs1, rs2, rs3`.
- **Generators**: the 31 nonzero `output_r1/a1_ordered/*.poly` files,
  pinned individually by the `output_sha256` table inside
  `RESULT.json ce4d0adb…` (rehash before parse; restricted parser).
- **Computations and stop rules**:
  1. `Q3` (cheapest, obstruction direction): in the same ring without
     `rho`, `I0 = I_a1|rho=0` (23 nonzero generators),
     `T0 = sat(I0, a1*k)`.  If `T0 != (1)`: **typed certificates from
     grades <= 15 are impossible**; export `std(T0)` and, if feasible, a
     rational witness point with `a1*k != 0`.  (Desk attempts at 60-90 s
     time out in both characteristics; this is genuinely AWS-scale.)
  2. `Q1/Q2`: `S = sat(sat(I_a1, a1), k)`; report `size(S)==1` and
     `reduce(1, std(S + ideal(rho)))==0`.
  3. If `Q2` passes: extract `w` with `1 - rho*w ∈ S` by `lift`, then
     `division` of `a1^N k^M (1 - rho*w)` against `I_a1` for the minimal
     saturation exponents; export every cofactor and rehash.
- **Controls**: positive — the identical pipeline on the 28 a0-chart rows
  must return `sat(I_a0, a0) = (1)` and `reduce(a0^3, std(I_a0)) == 0`,
  reproducing `A0-CERT-P`; negative — grade-10 inputs specialize to zero;
  diagnostic (not a gate) — dropping `Tg15_3` should break `Q2`.
- **Resources**: two independent hosts, 64 GiB / 24 h per lane; on breach,
  write the campaign-standard TIMEOUT artifact and stop; no retry without
  a new freeze.

## 5. Ranked immediate successor queue

1. **Different-model hostile review of section 2** (cheap, pure algebra:
   re-expand `A0-CERT-U` and `A0-CERT-P` from the frozen bytes).  On
   confirmation, promote: *the ordered stage-two `T-a0` chart over
   `V(J1)` is empty for the registered actual-total source* — closing one
   of the two `J2` nodes of the staged tree with no residual localizer
   stratum.
2. **Freeze and launch AWS V24** per section 4 (decisive for `T-a1`
   within exported grades; `Q3` alone already decides the obstruction
   direction).
3. If V24 `Q3` reports `T0 != (1)`: **grade-16/17 export (V25)** — the
   `T-a1` chart then provably needs deeper source rows, and the divisor
   analysis in section 3 (the `k`-block first appears at grade 13; the
   `a1*k*rs1^2` gap) indicates which monomial blocks the next grades must
   supply.
4. Terminal receiver `V(J1+J2)`: untouched by this lane; schedule after
   the `T-a1` outcome, since a `T-a1` emptiness proof would reroute all
   remaining mass there.

## 6. Scope firewall

Everything here concerns the literal exported grade-10..15 coefficients
of the frozen 569-tail actual-total source, specialized to the two
stage-two presentations over `A/J1`.  The `T-a0` emptiness statement is a
theorem about the truncated model, extending to the full registered
source only by ideal-monotonicity and only through the recorded
provenance chain; it awaits different-model review and is not promoted by
this lane.  The `T-a1` refutations are relative to the listed certificate
shapes, weights, and rho-caps, plus one exact hand theorem at
`(N,M)=(3,0)`; they do not prove the chart nonempty, and they say nothing
about grade >= 16 rows, unwritten Rees equations beyond the presented
bilinear-plus-saturation form, other localizers the campaign might
register, the terminal receiver, the deck/square bridge, Gate T, order
two, maximum twelve, or JC2.  Point killing (A00/A10) is V21's result,
distinct from the chart-ideal statements here; ideal membership (proved
for `a0^3`) is distinct from radical membership; the `T-a1` obstructions
distinguish truncated-source rows from the unwritten remainder of the
Rees package.  All desk probes were read-only, exact, and under one
minute and 1 GiB each; the two timed-out Singular saturations were
abandoned, not trusted, and rerouted to the AWS spec.
